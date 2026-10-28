"""Wizard da Etapa 2. Execute: python -m streamlit run app.py."""
import json
import pandas as pd
import streamlit as st
from avancado.conhecimento import carregar_base
from avancado.motor import analisar
from avancado.roadmap import gerar_plano, plano_markdown

st.set_page_config(page_title='Carreiras TI · Etapa 2', page_icon='🧭', layout='wide')
try:
    base = carregar_base()
except ValueError as exc:
    st.error(str(exc))
    st.stop()

if 'formulario' not in st.session_state:
    st.session_state.formulario = dict(experiencia='Iniciante', horas=6,
                                       respostas={q: 3 for q in base['perguntas']},
                                       conhecimentos={c: 0 for c in base['competencias']})
    st.session_state.passo = 0
formulario = st.session_state.formulario
rotulos = ['Perfil pessoal', 'Afinidades e competências', 'Objetivos de carreira', 'Resultados e plano']
st.title('🧭 Carreiras em TI: afinidades e próximos passos')
st.caption('Etapa 2 · Inteligência Artificial · Leucimar Tiago da Silva Carvalho · UNIPAC Barbacena')
with st.sidebar:
    st.header('Sua jornada')
    for i, nome in enumerate(rotulos):
        st.write(('➜ ' if i == st.session_state.passo else '• ') + nome)
    st.info('Aderência é uma nota do modelo de preferências. Não é probabilidade de sucesso nem diagnóstico vocacional.')
    st.caption('As afinidades usam 1–5. Conhecimento atual usa 0–4. A análise de lacunas visa o alvo Júnior desta base didática.')
    st.button('Reiniciar tudo', key='reiniciar_e2', on_click=st.session_state.clear)
passo = st.session_state.passo
st.progress(passo/3, text=f'Passo {passo+1} de 4 · {rotulos[passo]}')


def avancar(n):
    st.session_state.passo = n
    st.session_state.pop('analise', None)


def salvar_perfil():
    st.session_state.formulario.update(experiencia=st.session_state.experiencia, horas=st.session_state.horas)
    avancar(1)


def salvar_afinidades(destino):
    f = st.session_state.formulario
    for q, p in base['perguntas'].items():
        if p['etapa'] == 'afinidades':
            f['respostas'][q] = st.session_state['a_'+q]
    for cid in base['competencias']:
        f['conhecimentos'][cid] = st.session_state['c_'+cid]
    avancar(destino)


def salvar_objetivos(destino):
    f = st.session_state.formulario
    for q, p in base['perguntas'].items():
        if p['etapa'] == 'objetivos':
            f['respostas'][q] = st.session_state['o_'+q]
    avancar(destino)
    if destino == 3:
        st.session_state.analise = analisar(f['respostas'], base)


if passo == 0:
    st.subheader('1. Contexto e disponibilidade')
    st.write('O contexto ajuda a interpretar o plano; afinidade e lacunas são calculadas separadamente.')
    with st.form('perfil'):
        niveis = ['Iniciante', 'Estudante com projetos', 'Profissional em transição', 'Profissional de TI']
        experiencia = st.selectbox('Como você descreve seu momento?', niveis,
                                  index=niveis.index(formulario['experiencia']), key='experiencia')
        horas = st.number_input('Horas disponíveis por semana', min_value=1, max_value=40,
                                value=formulario['horas'], step=1, key='horas')
        st.caption('Não pedimos dados pessoais. O contexto é informativo e não altera sua pontuação.')
        st.form_submit_button('Próximo: afinidades', key='proximo_perfil', on_click=salvar_perfil)
elif passo == 1:
    st.subheader('2. Afinidades técnicas e conhecimento atual')
    st.write('Afinidade: 1 = muito baixa · 2 = baixa · 3 = moderada · 4 = alta · 5 = muito alta.')
    with st.form('afinidades'):
        respostas = formulario['respostas'].copy()
        cols = st.columns(2)
        perguntas = [(q, p) for q, p in base['perguntas'].items() if p['etapa'] == 'afinidades']
        for i, (q, p) in enumerate(perguntas):
            with cols[i % 2]:
                respostas[q] = st.slider(p['rotulo'], 1, 5, respostas[q], key='a_'+q)
        st.divider()
        st.markdown('**O que você já consegue fazer?**')
        st.caption('Os níveis começam em 0. Revise todos: isso muda seu plano de estudos, não sua afinidade.')
        conhecimentos = formulario['conhecimentos'].copy()
        with st.expander('Avaliar competências atuais (0 a 4)', expanded=True):
            cols = st.columns(2)
            for i, (cid, c) in enumerate(base['competencias'].items()):
                with cols[i % 2]:
                    conhecimentos[cid] = st.selectbox(c['nome'], range(5), index=conhecimentos[cid],
                                                      format_func=lambda v: f"{v} · {base['escala_conhecimento']['rotulos'][v]}", key='c_'+cid)
        esquerda, direita = st.columns(2)
        esquerda.form_submit_button('Voltar ao perfil', key='voltar_afinidades', on_click=salvar_afinidades, args=(0,))
        direita.form_submit_button('Próximo: objetivos', key='proximo_afinidades', on_click=salvar_afinidades, args=(2,))
elif passo == 2:
    st.subheader('3. Objetivos de carreira')
    with st.form('objetivos'):
        respostas = formulario['respostas'].copy()
        for q, p in base['perguntas'].items():
            if p['etapa'] == 'objetivos':
                respostas[q] = st.slider(p['rotulo'], 1, 5, respostas[q], key='o_'+q)
        st.caption('1 = muito pouco · 3 = moderadamente · 5 = muito. Mais de um objetivo pode ser importante para você.')
        esquerda, direita = st.columns(2)
        esquerda.form_submit_button('Voltar às afinidades', key='voltar_objetivos', on_click=salvar_objetivos, args=(1,))
        direita.form_submit_button('Calcular compatibilidade', key='calcular', on_click=salvar_objetivos, args=(3,))
else:
    analise = st.session_state.get('analise')
    if analise is None:
        st.session_state.passo = 0
        st.rerun()
    st.subheader('Seu Top 3 de aderência')
    for aviso in analise['avisos']:
        st.warning(aviso)
    for empate in analise['empates']:
        if set(empate['trilhas']) & {r['trilha'] for r in analise['top3']}:
            st.caption(f"Empate em {empate['percentual']:.2f}%: " + ', '.join(base['trilhas'][t]['nome'] for t in empate['trilhas']))
    cols = st.columns(3)
    for col, r in zip(cols, analise['top3']):
        col.metric(r['nome'], f"{r['percentual']:.2f}%")
    st.caption('As notas são independentes e não somam necessariamente 100%. A ordem em empates usa o ID da trilha, sem indicar superioridade.')
    df = pd.DataFrame([{'Trilha':r['nome'], 'Aderência (%)':r['percentual']} for r in analise['ranking']])
    st.bar_chart(df, x='Trilha', y='Aderência (%)', horizontal=True)
    st.dataframe(df, hide_index=True, use_container_width=True)
    st.subheader('Escolha a trilha para seu plano')
    ids = [r['trilha'] for r in analise['ranking']]
    tid = st.selectbox('Você pode explorar qualquer uma das dez trilhas', ids,
                       format_func=lambda t: base['trilhas'][t]['nome'], key='trilha_plano')
    selecionada = next(r for r in analise['ranking'] if r['trilha'] == tid)
    with st.expander('Entender o cálculo desta trilha'):
        st.write(f"Base ponderada: {selecionada['bruto']:.2f}%. Desconto efetivo: {selecionada['desconto_aplicado']:.2f} pontos percentuais.")
        st.dataframe(pd.DataFrame(selecionada['contribuicoes']), hide_index=True, use_container_width=True)
        if selecionada['penalidades']:
            for pen in selecionada['penalidades']:
                st.write(f"**{pen['id']}**: {pen['motivo']} Desconto previsto de {pen['pontos_percentuais']:.0f} pontos, limitado à nota disponível.")
        else:
            st.write('Nenhuma penalidade disparada para esta trilha.')
    plano = gerar_plano(tid, formulario['conhecimentos'], formulario['horas'], base)
    st.subheader('Lacunas para o alvo Júnior')
    st.info(plano['aviso'])
    st.write(f"{plano['requisitos_atendidos']} de {plano['total_requisitos']} requisitos atendidos pela sua autoavaliação.")
    if not plano['gaps']:
        st.success('Nenhuma lacuna declarada. Valide o conhecimento no projeto de portfólio.')
    else:
        st.dataframe(pd.DataFrame([{'Ordem':g['ordem'],'Competência':g['nome'],'Atual':g['atual'],'Alvo':g['alvo'],
                                   'Horas estimadas':g['horas'],'Semanas':f"{g['semana_inicio']}–{g['semana_fim']}"} for g in plano['gaps']]),
                     hide_index=True, use_container_width=True)
        st.subheader('Roadmap de prática')
        for g in plano['gaps']:
            st.markdown(f"**{g['ordem']}. {g['nome']}** · semanas {g['semana_inicio']}–{g['semana_fim']}  \n{g['pratica']}")
        st.caption(f"Estimativa heurística: {plano['horas_estimadas']} horas, distribuídas em {plano['semanas_estimadas']} semanas. Ajuste ao seu ritmo.")
    st.subheader('Certificações opcionais')
    for c in plano['certificacoes']:
        st.markdown(f"[{c['nome']}]({c['url']}) — {c['nota']}")
    st.subheader('Seu projeto de portfólio no GitHub')
    st.write(plano['portfolio']['titulo'])
    for e in plano['portfolio']['entregas']:
        st.write('• '+e)
    with st.expander('Revisar respostas usadas na análise'):
        st.json(formulario)
    st.download_button('Baixar meu plano (.md)', plano_markdown(analise, plano), 'meu_plano_carreira_ti.md', 'text/markdown', key='baixar_md')
    st.download_button('Baixar análise completa (.json)', json.dumps(dict(perfil=formulario, analise=analise, plano=plano),ensure_ascii=False,indent=2),
                       'minha_analise_carreira.json','application/json',key='baixar_json')
    st.button('Revisar entrevista', key='revisar', on_click=avancar, args=(0,))
