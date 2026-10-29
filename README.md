# Consultor avançado de carreiras e desenvolvimento profissional em TI

**Etapa 2 — Inteligência Artificial — UNIPAC Barbacena**  
Aluno: Leucimar Tiago da Silva Carvalho. Professor: Felipe Roncalli de Paula Carneiro.

Evolução da Atividade 08 para afinidades graduais, compatibilidade percentual de múltiplas trilhas, gaps para o alvo Júnior e plano de ação individualizado.

## Versão e execução

A versão completa da Etapa 2 está neste repositório oficial, nas branches **`main`** e **`develop`**. As seis etapas foram integradas em sequência, após o commit inicial com a base integral da Atividade 08. O histórico de origem está em [docs/ETAPA2_INTEGRACAO.md](docs/ETAPA2_INTEGRACAO.md).

**[Guia completo para instalar, executar e testar no Windows](GUIA_EXECUCAO_E_TESTES_ETAPA2.md)** — inclui requisitos do PC, comandos sem ativação do PowerShell, cenários e resultados esperados.

```powershell
git clone --branch main --single-branch https://github.com/leucimar/Trabalho_Etapa2_IA_Upgrade_Sistema-Especialista-Carreira-TI.git Etapa2_IA
cd Etapa2_IA
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
.\.venv\Scripts\python.exe -m streamlit run app.py
```

Python 3.12 é a versão recomendada para reproduzir a validação; o código usa recursos de Python 3.10+. Abra http://localhost:8501 e percorra o wizard. Não há API paga, GPU, nuvem obrigatória ou banco de dados.

## Funcionalidades

- Quinze respostas Likert de 1 a 5: doze afinidades técnicas e três objetivos.
- Dez trilhas: Back-end, Front-end/UX, Ciência de Dados, Engenharia de Dados, Cibersegurança, DevOps/SRE, Cloud, Mobile, QA e Gestão de Produtos.
- Pesos e penalidades externos, Top 3, gráfico e ranking completo com notas independentes de 0 a 100%.
- Justificativas com contribuições por pergunta, descontos e avisos de empate ou baixa discriminação.
- Vinte e duas competências atuais avaliadas de 0 a 4, com lacunas em relação aos requisitos Júnior da trilha escolhida.
- Roadmap por pré-requisitos, prática sugerida, estimativas de esforço e disponibilidade semanal.
- Certificações opcionais com fontes oficiais, projeto de portfólio GitHub e exportação do plano em Markdown/JSON.
- Navegação com preservação das respostas e reinício de sessão.

## Arquitetura e fórmula

O enunciado permite Experta **ou motor próprio** com soma ponderada. A Etapa 2 usa um motor próprio e determinístico, desacoplado da base JSON. A Atividade 08 permanece disponível para comparação e regressão.

```text
app.py                          Wizard da Etapa 2
app_atividade08.py               Interface anterior preservada
avancado/conhecimento.py         Carregamento e validação do JSON
avancado/motor.py                Pontuação, penalidades, Top 3 e explicação
avancado/roadmap.py              Lacunas, dependências, esforço e exportação
dados/regras_carreiras.json      Perguntas, pesos, regras e trilhas externas
carreiras/                      Motor e catálogo originais da Atividade 08
tests/etapa2/                   Personas e novos testes
docs/ETAPA2_MODELO.md            Fórmula e decisões de modelagem
docs/ETAPA2_VALIDACAO.md         Evidências e limites da validação
docs/ETAPA2_INTEGRACAO.md        Ordem das branches para integração oficial
```

Para resposta `a` entre 1 e 5, `x=(a-1)/4`. A nota bruta é `100 * sum(x*peso)/sum(pesos)`. Subtraem-se as penalidades cujas condições são atendidas e limita-se o resultado ao intervalo 0–100. Conhecimentos atuais só influenciam gaps, nunca a afinidade. Cada trilha é avaliada independentemente; as notas não precisam somar 100%.

As condições, pesos, descontos, requisitos, pré-requisitos, práticas e certificações ficam em `dados/regras_carreiras.json`. O motor valida referências, escalas, valores e ciclos antes do cálculo; o caminho padrão é relativo ao módulo, não ao diretório do terminal.

As notas não são probabilidades de sucesso nem avaliação de senioridade. Requisitos Júnior e estimativas de estudo são heurísticas didáticas. Os pesos não foram validados por pesquisa psicométrica. Em empates, a ordem por ID é apenas estável; zero de aderência em todas as trilhas gera aviso explícito.

## Validação

```powershell
.\.venv\Scripts\python.exe -m pytest -q
.\.venv\Scripts\python.exe -m pip check
```

**80 testes aprovados** no ambiente Python 3.12.14/Linux, inicialmente em 26/10/2026 e reconfirmados na integração da etapa de validação em 28/10/2026. Cobertura: regressão da Atividade 08; dez personas novas; extremos; empates; perfil ambíguo; fórmula e penalidade; alteração do JSON; entradas inválidas; dependências do roadmap; nenhum gap; retenção de respostas e revisão/reinício do wizard. Não houve teste em Windows ou inspeção visual em todos os navegadores.

`requirements-lock.txt` preserva o snapshot do ambiente de dependências validado. Para a instalação usual, utilize `requirements-dev.txt` (aplicação e testes) ou `requirements.txt` (somente aplicação).

## Privacidade e custo

Respostas ficam na sessão local, sem cadastro ou gravação em banco. As exportações são feitas apenas ao clicar nos botões de download. O app não envia código ao GitHub nem provisiona serviços; sugere um projeto para você desenvolver. Atualizar a aba ou encerrar o servidor pode encerrar a sessão; baixe o plano se quiser preservá-lo.

Toda execução pode ser local e gratuita. Certificações são sugestões opcionais; provas podem ter custos e pré-requisitos. Consulte a instituição antes de se inscrever.

## Fontes e continuidade

Enunciado: **Trabalho Etapa 2**, Inteligência Artificial, 22/10/2026, UNIPAC Barbacena. Base: [Atividade 08](https://github.com/leucimar/Atividade08-Construcao-Sistema-de-Carreiras-de-TI), commit `c91b220a3803dd1306e5f9bc737c5185e581a2b8`.

- [AWS: catálogo de certificações](https://aws.amazon.com/pt/certification/)
- [AWS: guias dos exames](https://docs.aws.amazon.com/aws-certification/latest/examguides/)
- [ISC2: Certified in Cybersecurity](https://www.isc2.org/certifications/cc)
- [ISTQB: certificações](https://www.istqb.org/certifications/)
- [Scrum.org: Professional Scrum Product Owner](https://www.scrum.org/professional-scrum-product-owner-certifications)

Documentos sem o prefixo `ETAPA2_` em `docs/` registram a etapa anterior. O guia desta Etapa 2 e os documentos com esse prefixo descrevem a versão atual.
