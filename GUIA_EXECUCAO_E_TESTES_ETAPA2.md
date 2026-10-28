# Guia de execução e testes — Etapa 2 de Inteligência Artificial

Aluno: Leucimar Tiago da Silva Carvalho. Professor: Felipe Roncalli de Paula Carneiro.

## 1. Onde está a versão para testar

A versão completa está no repositório oficial [Trabalho_Etapa2_IA_Upgrade_Sistema-Especialista-Carreira-TI](https://github.com/leucimar/Trabalho_Etapa2_IA_Upgrade_Sistema-Especialista-Carreira-TI), branches **`main`** e **`develop`**. A publicação das seis etapas foi concluída após o commit inicial com a base integral da Atividade 08.

O temporário preserva o desenvolvimento em `etapa2/main` e `etapa2/develop`, mas não é necessário acessá-lo para instalar a versão oficial. Se você já baixou o temporário, pode continuar usando essa cópia para testar; os comandos abaixo fazem um novo clone do oficial.

## 2. O que seu PC precisa ter

- Windows 10/11 e **Python 3.12 de 64 bits**, recomendado para reproduzir a versão testada. O código usa Python 3.10+, mas a validação desta rodada foi em Python 3.12.14/Linux.
- **Git**, se usar os comandos de clone. Alternativa: baixar o ZIP da branch `main` do repositório oficial e extraí-lo.
- Navegador atualizado, como Chrome, Edge ou Firefox.
- Internet para baixar o código e instalar as bibliotecas. A execução local e o motor não dependem de API externa nem de internet após a instalação.
- Como referência de planejamento, reserve cerca de 2 GB livres para código, ambiente e pacotes; 4 GB de RAM é uma configuração inicial razoável para este projeto pequeno. Esses valores são sugestões, não um mínimo aferido em teste de desempenho.

Não precisa de GPU, Docker, conta AWS/Azure, banco de dados, assinatura paga ou chave de API. VS Code é opcional. Os links de certificações são consultas opcionais; exames podem ser pagos.

Para instalar Python e Git, use os sites oficiais: https://www.python.org/downloads/ e https://git-scm.com/downloads. Durante a instalação do Python, habilite sua inclusão no PATH se essa opção estiver disponível.

## 3. Baixar a branch correta

Abra PowerShell ou o terminal do VS Code na pasta onde deseja guardar o projeto:

```powershell
git clone --branch main --single-branch https://github.com/leucimar/Trabalho_Etapa2_IA_Upgrade_Sistema-Especialista-Carreira-TI.git Etapa2_IA
cd Etapa2_IA
```

Não coloque senha ou token no código, nos comandos compartilhados ou nos commits.

Se preferir ZIP: abra o repositório oficial, escolha a branch **main**, use **Code → Download ZIP**, extraia e abra o terminal dentro da pasta que contém `app.py` e `requirements.txt`.

## 4. Criar o ambiente e instalar

No Windows, estes comandos não exigem ativar o ambiente virtual nem alterar a política do PowerShell:

```powershell
py -3.12 --version
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
```

`requirements-dev.txt` instala tanto as bibliotecas da aplicação quanto o pytest. Se quiser apenas usar o sistema, substitua o último arquivo por `requirements.txt`.

Se `py` não existir, tente `python --version`. Se ele mostrar Python 3.12, use `python -m venv .venv` no lugar do comando com `py`. Se nenhum existir, instale o Python e reabra o terminal.

O arquivo `requirements-lock.txt` registra as versões completas do ambiente validado em Python 3.12. Ele é um snapshot para reprodução, não uma promessa de compatibilidade com todas as plataformas. A instalação normal usa os arquivos acima.

## 5. Executar

Dentro da pasta do projeto:

```powershell
.\.venv\Scripts\python.exe -m streamlit run app.py
```

Abra o endereço informado no terminal, normalmente **http://localhost:8501**. Mantenha o terminal aberto. Para encerrar, pressione **Ctrl+C**.

Se a porta estiver ocupada:

```powershell
.\.venv\Scripts\python.exe -m streamlit run app.py --server.port 8502
```

A aplicação tem quatro telas:

1. **Perfil pessoal:** momento atual e horas disponíveis por semana. Não pede nome nem dados sensíveis.
2. **Afinidades e competências:** 12 afinidades de 1 a 5 e 22 competências de 0 a 4. Revise os níveis: todos começam em 0 para conhecimento e em 3 para afinidade.
3. **Objetivos de carreira:** três objetivos graduais; mais de um pode receber nota alta.
4. **Resultados e plano:** Top 3, gráfico das dez trilhas, justificativas, penalidades, gaps Júnior, roadmap, certificações opcionais e projeto de portfólio. Você pode trocar a trilha do plano sem repetir a entrevista.

O conhecimento atual altera o plano, sem reduzir a afinidade por uma área ainda não estudada. O contexto profissional do passo 1 é informativo e não muda a nota.

## 6. Roteiro manual de teste

### Caso A — Perfil Back-end forte

- Passo 1: escolha Iniciante e 6 horas semanais.
- Passo 2: coloque **5** em Lógica e programação, Análise e organização de dados, Testes e atenção a detalhes, Planejamento de arquitetura e capacidade. Coloque **2** nas outras afinidades. Mantenha todas as competências em **0**.
- Passo 3: coloque **5** em construir produtos; **2** em operar serviços e apoiar decisões.
- Resultado esperado: **Back-end em primeiro, com 100% de aderência ao modelo**. Haverá lacunas, estudos ordenados e projeto de API. Essa nota não significa que você já domina Back-end.

### Caso B — Perfil neutro e empate

- Reinicie e mantenha todas as afinidades e todos os objetivos em **3**.
- Resultado esperado: todas as trilhas com **50%**, aviso de respostas uniformes e empate. O Top 3 usa IDs em ordem alfabética apenas para estabilidade: Back-end, Ciência de Dados e Cloud.
- As notas não somam 100%: são compatibilidades independentes.

### Caso C — Nenhuma evidência positiva

- Coloque todas as afinidades e todos os objetivos em **1**.
- Resultado esperado: todas as trilhas com **0%** e aviso de que o Top 3 não representa uma recomendação positiva. Não há nota negativa.

### Caso D — Pessoa com competências já dominadas

- Escolha um perfil de afinidades e coloque **4 em todas as competências atuais**.
- Resultado esperado: nenhuma lacuna para o alvo Júnior da base. O portfólio e as certificações opcionais continuam disponíveis. O sistema não declara que a pessoa é Sênior.

### Caso E — Preferências conflitantes

- Coloque todas as afinidades e objetivos em **5**, exceto Matemática e estatística em **1**.
- Na tela final, escolha **Ciência de Dados** para explorar o plano e abra **Entender o cálculo desta trilha**.
- Resultado esperado: nota bruta **68,75%**, penalidade **P-ciencia de 12 pontos percentuais**, aderência final **56,75%**. A penalidade é explicada.

### Caso F — Voltar sem perder respostas

- Altere horas semanais para 8. Na tela seguinte, coloque Matemática em 5 e Git em 3.
- Use Voltar ao perfil e depois avance novamente.
- Resultado esperado: as 8 horas e os valores 5/3 são preservados. Ao revisar a entrevista, os resultados antigos deixam de ser mostrados até novo cálculo.

### Caso G — Plano e exportação

- Troque a trilha escolhida para Gestão de Produtos. Confira que os requisitos e o portfólio mudam.
- Baixe **meu plano (.md)** e **análise completa (.json)**. Abra os arquivos e confira se correspondem à trilha escolhida.
- O sistema apenas sugere o projeto: ele não cria automaticamente outro repositório nem envia seus dados.

## 7. Testes automatizados

```powershell
.\.venv\Scripts\python.exe -m pytest -q
.\.venv\Scripts\python.exe -m pip check
```

Resultado da validação, reconfirmado em 28/10/2026: **80 testes aprovados**, com Experta real nos testes legados e Streamlit AppTest nos fluxos web. `pip check` não apontou inconsistências.

Os novos testes estão em `tests/etapa2/`. Há dez personas com respostas e trilha esperada em `tests/etapa2/personas.json`.

A execução em Windows ainda precisa ser confirmada no seu PC. AppTest verifica comportamento e elementos renderizados pelo Streamlit; não substitui inspeção visual no seu navegador.

## 8. Como atualizar quando houver novas correções

Se usou clone e não modificou arquivos localmente:

```powershell
git pull --ff-only
.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
```

Se houver mudanças suas, salve-as antes de integrar atualizações; não use comandos de descarte sem revisá-las.

## 9. Problemas comuns

| Sintoma | O que verificar |
|---|---|
| `No module named streamlit` | Use o Python de `.venv` e instale `requirements-dev.txt` |
| `git` ou `py` não reconhecido | Instale a ferramenta, confira PATH e reabra o terminal |
| `Repository not found` no clone | Confira a URL do repositório oficial e a conexão com o GitHub |
| Interface antiga da AECO | Confirme que está em `main` do repositório oficial atualizado e executando `app.py`; `app_atividade08.py` é a interface anterior |
| Base JSON não encontrada ou inválida | Restaure `dados/regras_carreiras.json`; não execute só uma cópia isolada do app |
| Porta 8501 ocupada | Use `--server.port 8502` |
| Erro `collections.Mapping` ao testar Experta | Use os módulos legados pelo projeto: `carreiras/motor.py` aplica a compatibilidade antes do import |

## 10. Linux/macOS

Use Python 3.12 e, na pasta do projeto:

```bash
python3.12 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/python -m pytest -q
.venv/bin/python -m streamlit run app.py
```

## 11. Interpretação correta

As notas medem aderência a uma base didática de preferências. Não são probabilidades, testes psicológicos, garantia de emprego ou certificação de senioridade. O alvo Júnior e a estimativa de 6 horas por incremento de nível são decisões de modelagem, sujeitas a revisão. Os gaps dependem da sua autoavaliação. Provas de certificação podem cobrar taxas; não há necessidade de fazer compras para executar a atividade.
