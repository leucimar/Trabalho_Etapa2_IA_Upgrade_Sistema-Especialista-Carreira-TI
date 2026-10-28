from streamlit.testing.v1 import AppTest


def test_wizard_retencao_resultado_revisao_e_reinicio():
    app = AppTest.from_file('app.py').run()
    assert not app.exception
    app.number_input(key='horas').set_value(8)
    app.button(key='proximo_perfil').click().run()
    assert not app.exception
    app.slider(key='a_matematica').set_value(5)
    app.selectbox(key='c_git').select(3)
    app.button(key='voltar_afinidades').click().run()
    assert app.number_input(key='horas').value == 8
    app.button(key='proximo_perfil').click().run()
    assert app.slider(key='a_matematica').value == 5
    assert app.selectbox(key='c_git').value == 3
    app.button(key='proximo_afinidades').click().run()
    app.slider(key='o_decidir').set_value(5)
    app.button(key='calcular').click().run()
    assert not app.exception
    assert len(app.metric) == 3
    assert len(app.dataframe) >= 2
    assert app.selectbox(key='trilha_plano').value
    app.selectbox(key='trilha_plano').select('produto').run()
    assert not app.exception
    assert any('Discovery de produto' in x.value for x in app.markdown)
    app.button(key='revisar').click().run()
    assert not app.metric
    app.button(key='proximo_perfil').click().run()
    assert app.slider(key='a_matematica').value == 5
    app.button(key='reiniciar_e2').click().run()
    assert app.number_input(key='horas').value == 6
    assert not app.metric


def test_neutro_empate_e_todas_competencias_altas():
    app=AppTest.from_file('app.py').run()
    app.button(key='proximo_perfil').click().run()
    for widget in app.selectbox:
        if widget.key.startswith('c_'):widget.select(4)
    app.button(key='proximo_afinidades').click().run()
    app.button(key='calcular').click().run()
    assert not app.exception
    assert len(app.metric)==3
    assert all(m.value=='50.00%' for m in app.metric)
    assert app.warning
    assert any('Nenhuma lacuna' in s.value for s in app.success)


def test_wizard_sem_evidencias():
    app = AppTest.from_file('app.py').run()
    app.button(key='proximo_perfil').click().run()
    for widget in app.slider:
        widget.set_value(1)
    app.button(key='proximo_afinidades').click().run()
    for widget in app.slider:
        widget.set_value(1)
    app.button(key='calcular').click().run()
    assert not app.exception
    assert all(m.value == '0.00%' for m in app.metric)
    assert any('Nenhuma trilha' in w.value for w in app.warning)
