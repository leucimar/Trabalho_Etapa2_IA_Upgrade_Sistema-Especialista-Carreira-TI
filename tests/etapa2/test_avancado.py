from copy import deepcopy
import json
import math
from pathlib import Path
import pytest
from avancado.conhecimento import carregar_base
from avancado.motor import analisar
from avancado.roadmap import gerar_plano, plano_markdown


@pytest.fixture
def base():
    return carregar_base()


def respostas(base, valor=3):
    return dict.fromkeys(base['perguntas'], valor)


def conhecimentos(base, valor=0):
    return dict.fromkeys(base['competencias'], valor)


def test_estrutura_e_dez_trilhas(base):
    assert len(base['trilhas']) == 10
    assert len(base['perguntas']) == 15
    assert all(len(t['pesos']) >= 5 for t in base['trilhas'].values())


@pytest.mark.parametrize('valor,percentual', [(1,0),(3,50),(5,100)])
def test_limites_uniformes(base, valor, percentual):
    a = analisar(respostas(base, valor), base)
    assert all(r['percentual'] == percentual for r in a['ranking'])
    assert a['avisos'] and len(a['top3']) == 3
    assert a['sem_evidencias'] == (valor == 1)


@pytest.mark.parametrize('valor', [0,6,True,False,2.5,'5',None,float('nan')])
def test_entrada_invalida(base, valor):
    r = respostas(base)
    r['logica'] = valor
    with pytest.raises(ValueError):
        analisar(r, base)


def test_campos_ausentes_extras(base):
    with pytest.raises(ValueError):
        analisar({}, base)
    with pytest.raises(ValueError):
        analisar(dict(respostas(base), extra=4), base)


def test_formula_penalidade_e_justificativa(base):
    r = respostas(base, 5)
    r['matematica'] = 1
    ciencia = next(x for x in analisar(r, base)['ranking'] if x['trilha'] == 'ciencia')
    assert ciencia['bruto'] == 68.75
    assert ciencia['percentual'] == 56.75
    assert ciencia['desconto_aplicado'] == 12
    assert ciencia['penalidades'][0]['id'] == 'P-ciencia'
    assert sum(x['pontos_percentuais'] for x in ciencia['contribuicoes']) == pytest.approx(ciencia['bruto'], abs=1e-5)


def test_configuracao_externa_muda_resultado(base, tmp_path):
    r = respostas(base)
    r['logica'] = 5
    b = deepcopy(base)
    b['trilhas']['backend']['pesos'] = {'logica':100}
    arquivo = tmp_path/'nova.json'
    arquivo.write_text(json.dumps(b), encoding='utf-8')
    a = analisar(r, carregar_base(arquivo))
    assert a['ranking'][0]['trilha'] == 'backend'
    assert a['ranking'][0]['percentual'] == 100


def test_empate_parcial_e_ordem_estavel(base):
    r = respostas(base)
    a = analisar(r, base)
    invertida = deepcopy(base)
    invertida['trilhas'] = dict(reversed(list(base['trilhas'].items())))
    assert analisar(r, invertida)['ranking'] == a['ranking']
    assert len(a['empates'][0]['trilhas']) == 10
    assert [x['trilha'] for x in a['top3']] == ['backend','ciencia','cloud']
    assert sum(x['percentual'] for x in a['ranking']) == 500


@pytest.mark.parametrize('mutacao', ['peso_zero','peso_nan','pergunta','ciclo','prerequisito','alvo','condicao'])
def test_base_invalida(base, mutacao):
    b = deepcopy(base)
    if mutacao == 'peso_zero': b['trilhas']['backend']['pesos'] = {'logica':0}
    elif mutacao == 'peso_nan': b['trilhas']['backend']['pesos'] = {'logica':math.nan}
    elif mutacao == 'pergunta': b['trilhas']['backend']['pesos'] = {'desconhecida':1}
    elif mutacao == 'ciclo': b['competencias']['git']['prerequisitos'] = ['git']
    elif mutacao == 'prerequisito': b['competencias']['git']['prerequisitos'] = ['ausente']
    elif mutacao == 'alvo': b['trilhas']['backend']['requisitos_junior'][0]['nivel'] = 8
    elif mutacao == 'condicao': b['trilhas']['backend']['penalidades'][0]['condicoes'][0]['pergunta'] = 'ausente'
    with pytest.raises(ValueError):
        analisar(respostas(base), b)


def test_json_inexistente_e_malformado(tmp_path):
    with pytest.raises(ValueError): carregar_base(tmp_path/'nao.json')
    p = tmp_path/'invalido.json';p.write_text('{')
    with pytest.raises(ValueError): carregar_base(p)


@pytest.mark.parametrize('trilha', ['backend','frontend','ciencia','engenharia','seguranca','devops','cloud','mobile','qa','produto'])
def test_gaps_prerequisitos_e_portfolio(base, trilha):
    p = gerar_plano(trilha, conhecimentos(base), 6, base)
    assert p['gaps'] and p['certificacoes'] and p['portfolio']['titulo']
    pos = {g['competencia']:i for i,g in enumerate(p['gaps'])}
    for g in p['gaps']:
        assert g['atual'] < g['alvo']
        for dep in g['prerequisitos']:
            assert pos[dep] < pos[g['competencia']]
    assert p['horas_estimadas'] == sum(g['horas'] for g in p['gaps'])
    assert p['semanas_estimadas'] == math.ceil(p['horas_estimadas']/6)


def test_conhecimento_alto_sem_gaps(base):
    p = gerar_plano('backend', conhecimentos(base,4), 6, base)
    assert not p['gaps']
    assert p['prontidao_autodeclarada'] == 100
    assert p['horas_estimadas'] == p['semanas_estimadas'] == 0
    assert 'Não há lacunas' in plano_markdown(analisar(respostas(base),base),p)


def test_personalizacao_e_disponibilidade(base):
    k = conhecimentos(base)
    inicial = gerar_plano('ciencia',k,6,base)
    k['git'] = k['logica'] = 4
    depois = gerar_plano('ciencia',k,6,base)
    assert depois['horas_estimadas'] < inicial['horas_estimadas']
    rapido = gerar_plano('ciencia',k,12,base)
    assert rapido['semanas_estimadas'] <= depois['semanas_estimadas']
    assert [g['competencia'] for g in depois['gaps']] == [g['competencia'] for g in rapido['gaps']]


@pytest.mark.parametrize('horas',[0,41,True,float('nan')])
def test_horas_invalidas(base,horas):
    with pytest.raises(ValueError): gerar_plano('backend',conhecimentos(base),horas,base)


def test_entradas_roadmap_invalidas(base):
    with pytest.raises(ValueError): gerar_plano('desconhecida',conhecimentos(base),base=base)
    with pytest.raises(ValueError): gerar_plano('backend',{},base=base)
    k=conhecimentos(base);k['git']=5
    with pytest.raises(ValueError): gerar_plano('backend',k,base=base)


def test_personas_arquivo(base):
    personas = json.loads(Path('tests/etapa2/personas.json').read_text())
    for p in personas:
        a = analisar(p['respostas'],base)
        assert a['ranking'][0]['trilha'] == p['esperado'], p['nome']


def test_perfil_ambiguo_dados_web(base):
    r = respostas(base)
    for q in ('visual','logica','dados','matematica','construir','decidir'):r[q]=5
    a = analisar(r,base)
    assert {'frontend','ciencia'}.issubset({x['trilha'] for x in a['top3']})
    assert all(0 <= x['percentual'] <= 100 for x in a['ranking'])
