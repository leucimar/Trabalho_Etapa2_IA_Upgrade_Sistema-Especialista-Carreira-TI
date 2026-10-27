"""Soma ponderada normalizada com penalidades explicáveis, orientada pelo JSON."""
from .conhecimento import carregar_base, validar_base


def validar_respostas(respostas, base):
    if not isinstance(respostas, dict) or set(respostas) != set(base['perguntas']):
        raise ValueError('Responda exatamente todas as perguntas da base.')
    for k, v in respostas.items():
        if type(v) is not int or not 1 <= v <= 5:
            raise ValueError(f'A resposta de {k} deve ser um inteiro de 1 a 5.')


def analisar(respostas, base=None):
    base = carregar_base() if base is None else validar_base(base)
    validar_respostas(respostas, base)
    ranking = []
    for tid, trilha in base['trilhas'].items():
        total = sum(trilha['pesos'].values())
        contribuicoes = [dict(pergunta=q, rotulo=base['perguntas'][q]['rotulo'],
                             resposta=respostas[q], peso=peso,
                             pontos_percentuais=round(100 * ((respostas[q] - 1) / 4) * peso / total, 6))
                         for q, peso in trilha['pesos'].items()]
        # Calcula com precisão completa; arredonda apenas para apresentação.
        bruta = sum(((respostas[q] - 1) / 4) * peso for q, peso in trilha['pesos'].items()) / total
        penalidades = [dict(id=p['id'], motivo=p['motivo'], pontos_percentuais=100*p['desconto'])
                       for p in trilha['penalidades']
                       if all(respostas[c['pergunta']] <= c['maximo'] for c in p['condicoes'])]
        desconto = sum(p['pontos_percentuais'] for p in penalidades)
        final = round(max(0, min(100, 100*bruta - desconto)), 2)
        ranking.append(dict(trilha=tid, nome=trilha['nome'], percentual=final,
                            bruto=round(100*bruta, 6), desconto_aplicado=round(min(100*bruta, desconto), 6),
                            contribuicoes=sorted(contribuicoes, key=lambda c: (-c['pontos_percentuais'], c['pergunta'])),
                            penalidades=penalidades))
    ranking.sort(key=lambda r: (-r['percentual'], r['trilha']))
    avisos = []
    if len(set(respostas.values())) == 1:
        avisos.append('Respostas uniformes diferenciam pouco seus interesses. Revise exemplos reais antes de escolher uma trilha.')
    sem_evidencias = ranking[0]['percentual'] == 0
    if sem_evidencias:
        avisos.append('Nenhuma trilha obteve aderência positiva. O Top 3 é apenas uma ordenação técnica, não uma recomendação.')
    grupos = {}
    for r in ranking:
        grupos.setdefault(r['percentual'], []).append(r['trilha'])
    empates = [dict(percentual=k, trilhas=v) for k, v in grupos.items() if len(v) > 1]
    if any(ranking[0]['trilha'] in e['trilhas'] for e in empates):
        avisos.append('Há empate no topo. A ordem alfabética dos IDs serve apenas para estabilidade; compare as trilhas empatadas.')
    return dict(versao_base=base['versao'], ranking=ranking, top3=ranking[:3], empates=empates,
                avisos=avisos, sem_evidencias=sem_evidencias,
                interpretacao='Aderência independente ao modelo de preferências; não é probabilidade nem avaliação de senioridade.')
