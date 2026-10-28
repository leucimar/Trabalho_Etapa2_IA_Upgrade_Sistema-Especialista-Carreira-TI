from streamlit.testing.v1 import AppTest


def responder(app, atividade='visual', entrega='interfaces'):
    for key, value in dict(matematica='media', ferramenta='javascript', objetivo='tecnico', atividade=atividade, entrega=entrega).items():
        app.selectbox(key=key).select(value)
    return app.run()


def test_fluxo_resultado_obsoleto_e_reinicio():
    app = AppTest.from_file('app_atividade08.py').run()
    assert not app.exception
    assert app.button(key='recomendar').disabled
    responder(app)
    app.button(key='recomendar').click().run()
    assert not app.exception
    assert 'Front-end' in app.success[0].value
    app.selectbox(key='entrega').select('dados').run()
    assert not app.success
    assert any('Respostas alteradas' in x.value for x in app.info)
    app.button(key='reiniciar').click().run()
    assert app.selectbox(key='atividade').value is None
    assert app.button(key='recomendar').disabled


def test_entrevista_contextual_e_sem_evidencias():
    app = AppTest.from_file('app_atividade08.py').run()
    responder(app, 'modelos', 'dados')
    assert len(app.radio) == 1
    app.radio[0].set_value('pipelines').run()
    app.button(key='recomendar').click().run()
    assert not app.exception
    assert 'Engenharia de Dados' in app.success[0].value
    app.selectbox(key='atividade').select('visual')
    app.selectbox(key='objetivo').select('explorar')
    app.selectbox(key='ferramenta').select('nenhuma')
    app.selectbox(key='matematica').select('baixa')
    app.run().button(key='recomendar').click().run()
    assert not app.exception
    assert not app.success
    assert any('não ativaram' in x.value for x in app.warning)
