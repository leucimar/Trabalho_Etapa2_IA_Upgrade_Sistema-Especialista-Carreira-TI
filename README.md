# 🧭 Consultor Inteligente de Carreiras em TI

Sistema especialista baseado em regras que entrevista o usuário e recomenda uma trilha de carreira, mostrando as evidências que sustentam a conclusão.

**Atividade 08 · Inteligência Artificial · Ciência da Computação · UNIPAC Barbacena**  
**Aluno:** Leucimar Tiago da Silva Carvalho  
**Professor:** Felipe Roncalli de Paula Carneiro

## Executar

Requer Python 3.10 ou superior. Validado neste desenvolvimento com Python 3.12.14. Recomenda-se Python 3.12 para reproduzir o ambiente testado.

```bash
git clone https://github.com/leucimar/Atividade08-Construcao-Sistema-de-Carreiras-de-TI.git
cd Atividade08-Construcao-Sistema-de-Carreiras-de-TI
python -m venv .venv
```

Ative o ambiente conforme seu terminal:

```powershell
# Windows PowerShell
.venv\Scripts\Activate.ps1
```

```bash
# Linux/macOS
source .venv/bin/activate
```

```bash
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

Abra o endereço local informado pelo Streamlit, normalmente http://localhost:8501.

A versão completa está disponível neste repositório, nas branches `main` e `develop`. A evolução por etapas e os commits de origem estão registrados em [docs/PUBLICACAO.md](docs/PUBLICACAO.md).

## Como usar

1. Responda às cinco dimensões: matemática/estatística, ferramentas, objetivo, atividade e entrega.
2. Para dados e infraestrutura, responda à pergunta contextual que refina a atividade.
3. Clique em **Explorar minha trilha**.
4. Leia a recomendação, as regras acionadas e uma sugestão inicial de estudos.
5. Abra os detalhes para comparar o ranking e baixe o resultado em JSON se desejar.

Ao mudar uma resposta, o resultado anterior é ocultado até uma nova consulta. **Reiniciar entrevista** limpa a sessão. As respostas ficam apenas na memória da sessão; não há banco de dados nem cadastro. O download só é gerado quando solicitado.

## As dez trilhas

- Desenvolvimento Back-end
- Desenvolvimento Front-end & UI/UX
- Ciência de Dados e Machine Learning
- Engenharia de Dados
- Cibersegurança (Security / Pentesting)
- DevOps & SRE
- Computação em Nuvem (Cloud Architecture)
- Desenvolvimento Mobile
- Engenharia de Qualidade e Testes (QA)
- Gestão de Produtos (Product Management)

## Base de conhecimento e inferência

A [matriz de decisão](docs/MATRIZ_DECISAO.md) documenta **30 regras lógicas cruzadas**, três por trilha. As condições foram definidas como uma heurística educacional:

| Combinação | Peso |
|---|---:|
| Atividade + entrega coerentes | 6 |
| Atividade + ferramenta | 3 |
| Entrega + objetivo (ou estatística alta, em Ciência de Dados) | 2 |

`Perfil` contém os fatos da entrevista. Cada método decorado com `@Rule` em `Consultor`, subclasse de `KnowledgeEngine`, produz uma `Evidencia`. O Experta executa o encadeamento para frente. A aplicação soma as evidências de cada trilha após a execução e apresenta a trilha de maior pontuação.

Os IDs R01–R30 permitem conferir cada motivo na matriz. Nenhuma recomendação depende da ordem de disparo. Em eventual empate, a política é: afinidade de atividade, afinidade de entrega e ID alfabético; o empate é informado. Na base atual, os pesos e o vocabulário exclusivo evitam empates positivos; a política é mantida para extensões. Se nenhuma regra disparar, o sistema pede revisão das respostas, sem inventar uma recomendação.

A resposta contextual refina a atividade enviada ao motor. O painel de detalhes exibe os valores efetivamente usados. Iniciantes podem obter uma recomendação sem conhecer a ferramenta típica.

**Diferenciação:** modelos, previsões e estatística favorecem Ciência de Dados; pipelines e disponibilidade favorecem Engenharia de Dados. Automação e operação favorecem DevOps; planejamento de infraestrutura favorece Cloud.

## Estrutura

```text
app.py                     Interface Streamlit
carreiras/catalogo.py      Vocabulário e catálogo das trilhas
carreiras/motor.py         Fatos, 30 regras e agregação das evidências
docs/MATRIZ_DECISAO.md     Engenharia de conhecimento
docs/VALIDACAO.md          Evidências e limites dos testes
docs/PUBLICACAO.md         Branches e transferência gradual
tests/personas.json        Dez personas com resultado esperado
tests/test_motor.py        Validação do motor
tests/test_interface.py    Fluxos automatizados da interface
requirements.txt           Dependências principais
requirements-dev.txt       Dependências de desenvolvimento
requirements-lock.txt      Snapshot do ambiente Python 3.12 validado
```

## Testes

```bash
python -m pip install -r requirements-dev.txt
python -m pytest -q
python -m pip check
```

Resultado local: **34 testes aprovados**, incluindo dez personas, cobertura das 30 regras, iniciantes, perfis próximos, entradas inválidas, consultas isoladas, 100 combinações de atividade/entrega sem reforços e entrevista Streamlit via AppTest. Veja [validação](docs/VALIDACAO.md). O snapshot completo do ambiente está em `requirements-lock.txt`; em Python 3.12 pode ser usado com `python -m pip install -r requirements-lock.txt`.

## Compatibilidade e limitações

O Experta 1.9.4 fixa `frozendict==1.2`, que referencia `collections.Mapping`, removido no Python 3.10. `motor.py` restaura esse alias de `collections.abc` antes de importar o Experta. A adaptação está isolada e documentada; não substitui o motor por um simulador. Evite importar Experta diretamente antes desse módulo em novas extensões.

O sistema é didático e não foi validado por especialistas em orientação profissional. Pontos não são probabilidades, percentuais de adequação ou previsão de sucesso. As personas verificam coerência com a base proposta, não comprovam acurácia no mercado. Um perfil contraditório pode receber uma sugestão de evidência limitada, claramente sinalizada. Conhecimento prévio reforça a recomendação, mas não determina a capacidade de aprender uma carreira.

Não são usados modelos generativos nem serviços pagos. O ranking usa preferências declaradas e regras locais.

## Referências técnicas

- [Experta: fatos, regras e KnowledgeEngine](https://experta.readthedocs.io/en/latest/thebasics.html)
- [Experta: referência](https://experta.readthedocs.io/en/latest/reference.html)
- [Streamlit](https://docs.streamlit.io/)
- [Streamlit AppTest](https://docs.streamlit.io/develop/api-reference/app-testing/st.testing.v1.apptest)

Requisitos da atividade: enunciado fornecido pelo professor em **Atividade Aula 08**, de 01/10/2026.
