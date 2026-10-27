"""Carregamento e validação da base externa, sem IDs de carreiras no motor."""
import json
import math
from pathlib import Path

CAMINHO_PADRAO = Path(__file__).resolve().parents[1] / 'dados' / 'regras_carreiras.json'


def numero(valor, minimo, maximo):
    return (isinstance(valor, (int, float)) and not isinstance(valor, bool)
            and math.isfinite(valor) and minimo <= valor <= maximo)


def validar_base(base):
    """Falha cedo em configurações incompletas, referências inválidas e ciclos."""
    try:
        if not isinstance(base.get('versao'), str) or not base['versao']:
            raise ValueError('Versão ausente.')
        if base['escala_afinidade'] != {'minimo': 1, 'maximo': 5}:
            raise ValueError('A escala de afinidade deve ser 1 a 5.')
        escala = base['escala_conhecimento']
        if escala['minimo'] != 0 or escala['maximo'] != 4 or len(escala['rotulos']) != 5:
            raise ValueError('A escala de conhecimento deve ser 0 a 4.')
        perguntas, competencias, trilhas = (base[k] for k in ('perguntas', 'competencias', 'trilhas'))
        if not perguntas or not competencias or not trilhas:
            raise ValueError('A base deve conter perguntas, competências e trilhas.')
        for q in perguntas.values():
            if not q['rotulo'] or q['etapa'] not in ('afinidades', 'objetivos'):
                raise ValueError('Pergunta sem rótulo ou etapa válida.')
        for c in competencias.values():
            if not c['nome'] or not c['pratica'] or not numero(c['horas_por_nivel'], 0.1, 1000):
                raise ValueError('Competência sem nome, prática ou estimativa válida.')
            if not isinstance(c['prerequisitos'], list) or any(d not in competencias for d in c['prerequisitos']):
                raise ValueError('Pré-requisito desconhecido.')
        visitados, pilha = set(), set()

        def visitar(c):
            if c in pilha:
                raise ValueError('Ciclo nos pré-requisitos.')
            if c not in visitados:
                pilha.add(c)
                for d in competencias[c]['prerequisitos']:
                    visitar(d)
                pilha.remove(c)
                visitados.add(c)
        for c in competencias:
            visitar(c)
        for t in trilhas.values():
            if not t['nome'] or not t['pesos'] or any(q not in perguntas for q in t['pesos']):
                raise ValueError('Trilha sem nome/pesos ou pergunta desconhecida.')
            if any(not numero(w, 0.0001, 1000) for w in t['pesos'].values()):
                raise ValueError('Pesos devem ser positivos e finitos.')
            if len({p['id'] for p in t['penalidades']}) != len(t['penalidades']):
                raise ValueError('IDs de penalidades duplicados.')
            for p in t['penalidades']:
                if not p['motivo'] or not p['condicoes'] or not numero(p['desconto'], 0, 1):
                    raise ValueError('Penalidade inválida.')
                for cond in p['condicoes']:
                    if cond['pergunta'] not in perguntas or not numero(cond['maximo'], 1, 5):
                        raise ValueError('Condição de penalidade inválida.')
            reqs = t['requisitos_junior']
            ids = [r['competencia'] for r in reqs]
            if not ids or len(set(ids)) != len(ids):
                raise ValueError('Requisitos vazios ou duplicados.')
            for r in reqs:
                c = r['competencia']
                if c not in competencias or type(r['nivel']) is not int or not 1 <= r['nivel'] <= 4:
                    raise ValueError('Requisito de competência inválido.')
                if not numero(r['prioridade'], 0, 1000):
                    raise ValueError('Prioridade inválida.')
                if any(d not in ids for d in competencias[c]['prerequisitos']):
                    raise ValueError('Trilha deve incluir os pré-requisitos de suas competências.')
            if not t['portfolio']['titulo'] or not t['portfolio']['entregas']:
                raise ValueError('Portfólio ausente.')
            if not t['certificacoes']:
                raise ValueError('Orientação de certificação ausente.')
            for c in t['certificacoes']:
                if not c['nome'] or not c['nota'] or not c['url'].startswith('https://'):
                    raise ValueError('Certificação sem metadados válidos.')
    except (KeyError, TypeError, AttributeError) as exc:
        raise ValueError('Estrutura inválida da base de conhecimento.') from exc
    return base


def carregar_base(caminho=None):
    try:
        base = json.loads(Path(caminho or CAMINHO_PADRAO).read_text(encoding='utf-8'))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError('Não foi possível ler a base JSON. Confira o arquivo e sua sintaxe.') from exc
    return validar_base(base)
