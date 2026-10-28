# Validação da Etapa 2

Data: 26/10/2026. Ambiente: Linux, Python 3.12.14, Streamlit 1.55.0, Pandas 2.3.3 e pytest 9.1.1.

Executado: `python -m pytest -q` — **80 testes aprovados**. `python -m pip check` — nenhuma inconsistência de dependências.

Resultado reconfirmado em 28/10/2026 na integração da etapa 5 ao oficial, com o mesmo código desta entrega. A etapa 6 altera somente documentação. A verificação de 28/10 usou o mesmo Python, Streamlit, Pandas e pytest; dependências transitivas podem diferir do snapshot inicial.

| Requisito | Implementação e evidência |
|---|---|
| Dez trilhas e afinidade gradual | JSON com 15 perguntas, Likert 1–5 e dez personas novas |
| Conhecimento desacoplado | Pesos, penalidades, requisitos e características carregados do JSON; teste altera peso externo e observa nova nota |
| Top 3 e compatibilidade | Notas independentes, normalizadas por soma dos pesos, ordenação estável e ranking das dez trilhas |
| Penalidades | Ciência de Dados com demais dimensões altas e matemática=1: 68,75% bruto − 12 pontos = 56,75% final |
| Extremos e ambiguidade | Uniformes 1→0%, 3→50%, 5→100%; empate explícito e perfil simultaneamente dados/web |
| Gaps Júnior | Comparação de todos os níveis atuais com alvos externos; conhecimento alto não produz gaps |
| Roadmap | Dependências antes dos dependentes, redução de lacunas já atendidas e adaptação às horas semanais |
| Portfólio e certificações | Um projeto e entregas por trilha; certificações opcionais com referência oficial |
| Wizard | Quatro telas; retenção ao voltar, revisão sem resultado antigo e reset; todos neutros, ausência de evidências e troca da trilha do plano |
| Robustez | Valores ausentes/extras, booleanos, fora da faixa, NaN, JSON inválido, pesos inválidos e ciclos rejeitados |
| Continuidade | Testes originais da Atividade 08 preservados, com interface antiga em app_atividade08.py |

A validação encontrou falha de retenção de widgets durante mudanças de tela. A navegação passou a salvar os valores em callbacks de submissão antes de renderizar a próxima etapa; os fluxos de ida, volta e reinício passaram após o ajuste.

Limites: AppTest verifica comportamento e elementos do Streamlit, não a aparência em cada navegador. Não foi testada a instalação no PC Windows do aluno, desempenho mínimo de hardware, nem todas as versões Python 3.10+. As personas verificam coerência da heurística, não precisão preditiva ou validade de orientação profissional. O guia manual cobre exportação e inspeção visual a serem confirmadas no PC do aluno.
