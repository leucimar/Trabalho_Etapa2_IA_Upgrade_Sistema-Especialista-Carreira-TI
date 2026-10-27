"""Lacunas autodeclaradas e sequência de estudos por dependências."""
import math
from .conhecimento import carregar_base, validar_base, numero


def gerar_plano(trilha, conhecimentos, horas_semanais=6, base=None):
    base = carregar_base() if base is None else validar_base(base)
    if trilha not in base['trilhas']:
        raise ValueError('Trilha desconhecida.')
    if not isinstance(conhecimentos, dict) or set(conhecimentos) != set(base['competencias']):
        raise ValueError('Informe o nível atual de todas as competências da base.')
    if any(type(n) is not int or not 0 <= n <= 4 for n in conhecimentos.values()):
        raise ValueError('Conhecimento deve ser um inteiro de 0 a 4.')
    if not numero(horas_semanais, 1, 40):
        raise ValueError('Horas semanais devem estar entre 1 e 40.')
    t = base['trilhas'][trilha]
    requisitos = {r['competencia']: r for r in t['requisitos_junior']}
    gaps = {cid: dict(competencia=cid, nome=base['competencias'][cid]['nome'],
                      atual=conhecimentos[cid], alvo=r['nivel'],
                      deficit=r['nivel']-conhecimentos[cid], prioridade=r['prioridade'])
            for cid, r in requisitos.items() if conhecimentos[cid] < r['nivel']}
    ordem, visitados = [], set()

    def visitar(cid):
        if cid in visitados:
            return
        visitados.add(cid)
        for dep in base['competencias'][cid]['prerequisitos']:
            visitar(dep)
        if cid in gaps:
            ordem.append(cid)
    for cid in sorted(gaps, key=lambda c: (-gaps[c]['prioridade'], c)):
        visitar(cid)
    etapas, decorrido = [], 0
    for cid in ordem:
        c = base['competencias'][cid]
        horas = gaps[cid]['deficit'] * c['horas_por_nivel']
        etapas.append(dict(**gaps[cid], ordem=len(etapas)+1, pratica=c['pratica'],
                           prerequisitos=c['prerequisitos'], horas=horas,
                           semana_inicio=math.floor(decorrido/horas_semanais)+1,
                           semana_fim=math.ceil((decorrido+horas)/horas_semanais)))
        decorrido += horas
    atendidos = len(requisitos)-len(gaps)
    return dict(trilha=trilha, nome=t['nome'], gaps=etapas, requisitos_atendidos=atendidos,
                total_requisitos=len(requisitos), prontidao_autodeclarada=round(100*atendidos/len(requisitos), 2),
                horas_estimadas=decorrido, semanas_estimadas=math.ceil(decorrido/horas_semanais),
                horas_semanais=horas_semanais, certificacoes=t['certificacoes'], portfolio=t['portfolio'],
                aviso='Alvo Júnior definido por esta base didática. Autodeclaração e estimativas não comprovam senioridade nem garantem prazo ou contratação.')


def plano_markdown(analise, plano):
    """Relatório portátil sem depender da interface web."""
    linhas = ['# Meu plano de carreira em TI', '', analise['interpretacao'], '', '## Top 3', '']
    for i, r in enumerate(analise['top3'], 1):
        linhas.append(f"{i}. {r['nome']} — {r['percentual']:.2f}%")
    linhas += ['', *[f'> {a}' for a in analise['avisos']], '', f"## Trilha escolhida: {plano['nome']}", '', plano['aviso'], '',
               f"Requisitos atendidos: {plano['requisitos_atendidos']}/{plano['total_requisitos']}.",
               f"Esforço indicativo: {plano['horas_estimadas']} horas / {plano['semanas_estimadas']} semanas, com {plano['horas_semanais']} horas semanais.", '', '## Roadmap', '']
    if not plano['gaps']:
        linhas.append('Não há lacunas declaradas para o alvo desta base. Valide as competências no projeto de portfólio.')
    for g in plano['gaps']:
        linhas += [f"### {g['ordem']}. {g['nome']} — nível {g['atual']} → {g['alvo']}",
                   f"Semanas {g['semana_inicio']}–{g['semana_fim']} · {g['horas']} horas de prática indicativas.", g['pratica'], '']
    linhas += ['## Certificações opcionais', '']
    for c in plano['certificacoes']:
        linhas += [f"- [{c['nome']}]({c['url']}) — {c['nota']}"]
    linhas += ['', '## Portfólio GitHub', '', plano['portfolio']['titulo'], '']
    linhas += [f'- {e}' for e in plano['portfolio']['entregas']]
    return '\n'.join(linhas)+'\n'
