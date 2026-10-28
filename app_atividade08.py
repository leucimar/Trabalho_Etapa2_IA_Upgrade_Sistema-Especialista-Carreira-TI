"""Interface da entrevista, executada com streamlit run app.py."""
import json
from dataclasses import asdict
import streamlit as st
from carreiras.catalogo import OPCOES, TRILHAS
from carreiras.motor import recomendar

st.set_page_config(page_title='Sua carreira em TI', page_icon='🧭', layout='wide')
st.title('🧭 Descubra caminhos em tecnologia')
st.write('Uma conversa sobre suas preferências para explorar dez trilhas de carreira em TI.')
st.caption('Sistema especialista • 30 regras explicáveis • Atividade 08 | Inteligência Artificial')
with st.sidebar:
    st.header('Como funciona')
    st.write('1. Conte suas afinidades.\n2. Explore a recomendação.\n3. Confira as regras e os próximos passos.')
    st.info('Orientação exploratória: a pontuação representa regras compatíveis, não probabilidade de sucesso nem diagnóstico vocacional.')
    st.caption('Leucimar Tiago da Silva Carvalho | UNIPAC Barbacena')
    if st.button('Reiniciar entrevista', key='reiniciar'):
        for key in list(st.session_state):
            del st.session_state[key]
        st.rerun()


def pergunta(campo, rotulo):
    return st.selectbox(rotulo, options=list(OPCOES[campo]), index=None,
                        placeholder='Selecione uma opção',
                        format_func=OPCOES[campo].get, key=campo)

esquerda, direita = st.columns(2)
with esquerda:
    st.subheader('Suas afinidades')
    matematica = pergunta('matematica', 'Como é sua afinidade com matemática e estatística?')
    ferramenta = pergunta('ferramenta', 'Com qual linguagem ou ferramenta você tem mais afinidade?')
    objetivo = pergunta('objetivo', 'Qual é seu objetivo profissional neste momento?')
with direita:
    st.subheader('Seu dia a dia ideal')
    atividade = pergunta('atividade', 'Qual atividade você mais gostaria de realizar?')
    entrega = pergunta('entrega', 'Qual entrega mais motiva você?')
    if atividade in ('modelos', 'pipelines'):
        atividade = st.radio('Dentro de dados, qual desafio prefere?', ['modelos', 'pipelines'],
                            index=['modelos', 'pipelines'].index(atividade),
                            format_func=lambda v: {'modelos':'Interpretar dados e modelar previsões', 'pipelines':'Integrar fontes e disponibilizar dados'}[v],
                            key='refino_dados_'+atividade)
    elif atividade in ('automacao', 'arquitetura'):
        atividade = st.radio('Dentro de infraestrutura, qual desafio prefere?', ['automacao', 'arquitetura'],
                            index=['automacao', 'arquitetura'].index(atividade),
                            format_func=lambda v: {'automacao':'Automatizar entregas e operar serviços', 'arquitetura':'Planejar arquitetura, capacidade e custos'}[v],
                            key='refino_infra_'+atividade)

respostas = dict(matematica=matematica, ferramenta=ferramenta, objetivo=objetivo,
                 atividade=atividade, entrega=entrega)
completas = all(v is not None for v in respostas.values())
st.progress(sum(v is not None for v in respostas.values()) / 5,
            text=f'{sum(v is not None for v in respostas.values())} de 5 dimensões respondidas')
if st.button('Explorar minha trilha', type='primary', disabled=not completas, key='recomendar'):
    st.session_state['resultado'] = asdict(recomendar(respostas))
    st.session_state['respostas_resultado'] = respostas.copy()

# Resultado só é válido para o conjunto atual de respostas.
if st.session_state.get('respostas_resultado') == respostas and 'resultado' in st.session_state:
    resultado = st.session_state['resultado']
    st.divider()
    if resultado['recomendacao']:
        trilha = TRILHAS[resultado['recomendacao']]
        st.success('Trilha recomendada: ' + trilha['nome'])
        st.write(trilha['descricao'])
        if len(resultado['empatadas']) > 1:
            st.warning('Empate em pontos entre: ' + ', '.join(TRILHAS[t]['nome'] for t in resultado['empatadas']) + '. Desempate: atividade, entrega e ID alfabético. Explore também as alternativas.')
        st.subheader('Por que esta trilha?')
        for e in resultado['evidencias']:
            if e['trilha'] == resultado['recomendacao']:
                st.write(f"**{e['regra']} · +{e['pontos']} pontos:** {e['motivo']}")
        st.subheader('Por onde começar')
        st.write(trilha['estudo'])
        if resultado['ranking'][0]['pontos'] < 6:
            st.info('Evidência limitada: nenhuma combinação principal de atividade e entrega convergiu. Revise suas preferências e compare as trilhas.')
    else:
        st.warning('Suas respostas ainda não ativaram regras suficientes para recomendar uma trilha. Revise atividade e entrega; elas podem apontar interesses diferentes.')
    with st.expander('Ver ranking, respostas e todas as regras disparadas'):
        st.table([{'Trilha':TRILHAS[r['trilha']]['nome'], 'Pontos':r['pontos']} for r in resultado['ranking']])
        st.write({c: OPCOES[c][v] for c, v in respostas.items()})
        st.table(resultado['evidencias'])
    st.download_button('Baixar resultado em JSON', json.dumps(dict(respostas=respostas, resultado=resultado),ensure_ascii=False,indent=2),
                       file_name='minha_trilha_ti.json', mime='application/json')
elif 'resultado' in st.session_state:
    st.info('Respostas alteradas. Clique novamente em “Explorar minha trilha” para atualizar o resultado.')

with st.expander('Conhecer as dez trilhas'):
    for trilha in TRILHAS.values():
        st.markdown('**' + trilha['nome'] + '** — ' + trilha['descricao'])
