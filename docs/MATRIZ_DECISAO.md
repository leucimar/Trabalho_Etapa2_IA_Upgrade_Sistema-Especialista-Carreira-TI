# Matriz de decisão

As regras são uma heurística didática, sem validade psicométrica. Cada regra cruza duas ou mais respostas.

| Regra | Trilha | Condição (SE) | Pontos (ENTÃO) |
|---|---|---|---|
| R01 | Desenvolvimento Back-end | atividade=logica E entrega=apis | 6 |
| R02 | Desenvolvimento Back-end | atividade=logica E ferramenta=python | 3 |
| R03 | Desenvolvimento Back-end | entrega=apis E objetivo=técnico | 2 |
| R04 | Desenvolvimento Front-end & UI/UX | atividade=visual E entrega=interfaces | 6 |
| R05 | Desenvolvimento Front-end & UI/UX | atividade=visual E ferramenta=javascript | 3 |
| R06 | Desenvolvimento Front-end & UI/UX | entrega=interfaces E objetivo=técnico | 2 |
| R07 | Ciência de Dados e Machine Learning | atividade=modelos E entrega=previsoes | 6 |
| R08 | Ciência de Dados e Machine Learning | atividade=modelos E ferramenta=python | 3 |
| R09 | Ciência de Dados e Machine Learning | entrega=previsoes E matemática=alta | 2 |
| R10 | Engenharia de Dados | atividade=pipelines E entrega=dados | 6 |
| R11 | Engenharia de Dados | atividade=pipelines E ferramenta=sql | 3 |
| R12 | Engenharia de Dados | entrega=dados E objetivo=técnico | 2 |
| R13 | Cibersegurança (Security / Pentesting) | atividade=seguranca E entrega=protecao | 6 |
| R14 | Cibersegurança (Security / Pentesting) | atividade=seguranca E ferramenta=linux | 3 |
| R15 | Cibersegurança (Security / Pentesting) | entrega=protecao E objetivo=técnico | 2 |
| R16 | DevOps & SRE | atividade=automacao E entrega=confiabilidade | 6 |
| R17 | DevOps & SRE | atividade=automacao E ferramenta=linux | 3 |
| R18 | DevOps & SRE | entrega=confiabilidade E objetivo=técnico | 2 |
| R19 | Computação em Nuvem (Cloud Architecture) | atividade=arquitetura E entrega=infraestrutura | 6 |
| R20 | Computação em Nuvem (Cloud Architecture) | atividade=arquitetura E ferramenta=cloud | 3 |
| R21 | Computação em Nuvem (Cloud Architecture) | entrega=infraestrutura E objetivo=técnico | 2 |
| R22 | Desenvolvimento Mobile | atividade=mobile E entrega=aplicativos | 6 |
| R23 | Desenvolvimento Mobile | atividade=mobile E ferramenta=mobile | 3 |
| R24 | Desenvolvimento Mobile | entrega=aplicativos E objetivo=técnico | 2 |
| R25 | Engenharia de Qualidade e Testes (QA) | atividade=testes E entrega=qualidade | 6 |
| R26 | Engenharia de Qualidade e Testes (QA) | atividade=testes E ferramenta=testes | 3 |
| R27 | Engenharia de Qualidade e Testes (QA) | entrega=qualidade E objetivo=técnico | 2 |
| R28 | Gestão de Produtos (Product Management) | atividade=negocio E entrega=valor | 6 |
| R29 | Gestão de Produtos (Product Management) | atividade=negocio E ferramenta=gestao | 3 |
| R30 | Gestão de Produtos (Product Management) | entrega=valor E objetivo=pessoas | 2 |

## Resolução de conflitos

Encadeamento para frente: Perfil → Evidencia, via Experta. Agregação posterior soma evidências por trilha. A ordem de disparo não altera a pontuação. Empates são resolvidos por atividade, depois entrega, depois ID alfabético (critério explícito, não força de evidência). A interface informa empate. Sem regras disparadas, não há recomendação e são solicitadas respostas mais específicas.

Ciência de Dados privilegia modelos/previsões/estatística; Engenharia de Dados privilegia pipelines/dados/SQL. DevOps privilegia automação/confiabilidade; Cloud privilegia arquitetura/infraestrutura. Ferramentas prévias reforçam afinidade, mas não são pré-requisito.

## Entrevista

Cinco dimensões obrigatórias: matemática, atividade diária, ferramenta, entrega de valor e objetivo. Para atividade modelos/pipelines, uma pergunta contextual diferencia interpretação/modelagem e integração/disponibilidade. Para automação/arquitetura, diferencia operação e planejamento. A resposta refina a atividade antes da inferência; todas as respostas são exibidas na interface.
