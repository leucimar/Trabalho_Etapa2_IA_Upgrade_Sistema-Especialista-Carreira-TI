# Validação

Executada em 22/10/2026, com Python 3.12.14, Experta 1.9.4, Streamlit 1.55.0 e pytest 9.1.1 em ambiente virtual.

Comandos: `python -m pytest -q` e `python -m pip check`.

Resultado: **34 testes aprovados**; nenhuma dependência inconsistente detectada.

Verificação final repetida em 23/10/2026, antes da integração da documentação ao repositório oficial: **34 testes aprovados**, com `python -m pytest -q`; `python -m pip check` sem inconsistências. As referências locais do README também foram conferidas.

| Grupo | Evidência |
|---|---|
| Dez trilhas | Persona canônica de cada trilha obtém a recomendação esperada com 11 pontos |
| Personas explícitas | `tests/personas.json` registra dez entrevistas com nomes, respostas e expectativas |
| Cobertura de regras | Todas as regras R01–R30 produzem evidências nas personas |
| Iniciantes | Dez casos sem ferramenta prévia preservam a recomendação por atividade e entrega |
| Perfis próximos | Python em pipelines continua indicando Engenharia; Linux em arquitetura continua indicando Cloud |
| Ambiguidade | Preferências divergentes respeitam pesos e podem gerar ausência de evidências |
| Combinatória | 100 pares atividade/entrega sem reforços; só pares convergentes recebem sugestão |
| Validação | Ausência, excesso de campos e valores fora do vocabulário são rejeitados |
| Isolamento | Consultas intercaladas mantêm resultados independentes e determinísticos |
| Interface | AppTest verifica bloqueio inicial, recomendação, alteração de respostas, reinício e refinamento contextual |

Os testes usam o Experta real. A interface foi executada pelo mecanismo AppTest do próprio Streamlit; isso não equivale a uma inspeção visual em navegadores e dispositivos reais. Não foram executados testes em Windows ou em todas as versões de Python 3.10+. A matriz e os pesos ainda precisam de validação humana com estudantes e profissionais; não há estimativa de precisão estatística.
