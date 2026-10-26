import ast
from pathlib import Path
import pytest
from carreiras.catalogo import TRILHAS, OPCOES
from carreiras.motor import recomendar


def perfil(trilha):
    t = TRILHAS[trilha]
    return dict(atividade=t['atividade'], entrega=t['entrega'], ferramenta=t['ferramenta'],
                matematica='alta' if trilha == 'ciencia' else 'media',
                objetivo='pessoas' if trilha == 'produto' else 'tecnico')


@pytest.mark.parametrize('trilha', TRILHAS)
def test_personas_de_cada_trilha(trilha):
    resultado = recomendar(perfil(trilha))
    assert resultado.recomendacao == trilha
    assert resultado.ranking[0]['pontos'] == 11
    assert len(resultado.evidencias) == 3


@pytest.mark.parametrize('trilha', TRILHAS)
def test_iniciante_nao_e_excluido(trilha):
    p = perfil(trilha)
    p['ferramenta'] = 'nenhuma'
    assert recomendar(p).recomendacao == trilha


def test_perfis_proximos_com_mesma_ferramenta():
    p = perfil('engenharia')
    p['ferramenta'] = 'python'
    assert recomendar(p).recomendacao == 'engenharia'
    p = perfil('cloud')
    p['ferramenta'] = 'linux'
    assert recomendar(p).recomendacao == 'cloud'


def test_preferencias_divergentes_e_ausencia_de_evidencias():
    p = perfil('frontend')
    p.update(entrega='apis', objetivo='tecnico', ferramenta='nenhuma')
    # Apenas backend R03 = 2: uma preferência isolada não ativa regra principal.
    assert recomendar(p).recomendacao == 'backend'
    p.update(ferramenta='javascript', entrega='previsoes', matematica='alta')
    assert recomendar(p).recomendacao == 'frontend'  # 3 versus 2
    p.update(ferramenta='nenhuma', entrega='previsoes', matematica='baixa', objetivo='explorar')
    assert recomendar(p).recomendacao is None


def test_consultas_isoladas_e_deterministicas():
    a = recomendar(perfil('ciencia'))
    recomendar(perfil('seguranca'))
    assert recomendar(perfil('ciencia')) == a
    assert len(a.evidencias) == len({e['regra'] for e in a.evidencias})


@pytest.mark.parametrize('campo', OPCOES)
def test_valores_invalidos(campo):
    p = perfil('qa')
    p[campo] = 'inexistente'
    with pytest.raises(ValueError):
        recomendar(p)


def test_campos_ausentes_e_extras():
    with pytest.raises(ValueError):
        recomendar({})
    with pytest.raises(ValueError):
        recomendar(dict(perfil('qa'), outro='valor'))


def test_trinta_regras_distintas_disparadas_pelas_personas():
    disparadas = {e['regra'] for t in TRILHAS for e in recomendar(perfil(t)).evidencias}
    assert disparadas == {f'R{i:02}' for i in range(1, 31)}
    arvore = ast.parse(Path('carreiras/motor.py').read_text())
    assert sum(isinstance(n, ast.FunctionDef) and n.name.startswith('r') and n.name[1:].isdigit() for n in ast.walk(arvore)) == 30


def test_todas_combinacoes_sem_afinidade_tecnica():
    # Cobertura de ausência de evidência para combinações divergentes.
    for a in OPCOES['atividade']:
        for e in OPCOES['entrega']:
            p = dict(atividade=a, entrega=e, ferramenta='nenhuma', matematica='baixa', objetivo='explorar')
            r = recomendar(p)
            correspondem = any(t['atividade'] == a and t['entrega'] == e for t in TRILHAS.values())
            assert bool(r.recomendacao) == correspondem


def test_personas_documentadas():
    import json
    personas = json.loads(Path('tests/personas.json').read_text())
    for persona in personas:
        assert recomendar(persona['respostas']).recomendacao == persona['esperado'], persona['nome']
