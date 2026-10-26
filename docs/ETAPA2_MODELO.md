# Modelo da Etapa 2

Base: Atividade 08, commit c91b220a3803dd1306e5f9bc737c5185e581a2b8.
Enunciado: Trabalho Etapa 2, Inteligência Artificial, 22/10/2026, UNIPAC.

## Fórmula

Afinidade a de 1 a 5 vira x=(a-1)/4. Para cada trilha, base=sum(x*peso)/sum(pesos).
Cada penalidade externa dispara quando TODAS as condições de baixa afinidade são atendidas.
Aderência=100*max(0,min(1,base-sum(descontos))). O desconto de 0,12 corresponde a até 12 pontos percentuais.
As notas de cada trilha são independentes: não precisam somar 100%. Não são probabilidades nem confiança estatística.
Os pesos, condições, descontos e requisitos Júnior estão no JSON. O motor conhece apenas o esquema, não IDs de carreiras.
Conhecimento atual é de 0 a 4 e só entra na análise de lacunas; não reduz afinidade por uma área que a pessoa ainda não estudou.

## Conflitos e empates

Baixa afinidade com dimensão central (1 ou 2) aplica a penalidade descrita na base.
A ordem é aderência decrescente, seguida do ID da trilha em ordem alfabética para estabilidade.
Empates na precisão exibida (duas casas) são informados; o Top 3 não é tratado como vencedor absoluto.
Todas as trilhas com zero geram um aviso de ausência de evidências, sem recomendação positiva.
Todas as respostas neutras (3) geram aviso de baixa discriminação. Todo o ranking continua disponível.

## Lacunas e plano

Cada requisito tem nível-alvo, prioridade e pré-requisitos. O plano inclui somente competências abaixo do alvo e respeita a ordem de dependências. Cada incremento de nível estima 6 horas de prática (heurística, não prazo garantido). As horas semanais informadas convertem esforço em blocos semanais. A avaliação é autodeclarada, sem certificar senioridade profissional.
Certificações são opcionais e podem ter provas pagas. Toda execução do software e os projetos sugeridos podem ser locais; não exigem assinatura de nuvem.

## Etapas de integração

1. JSON e modelagem; 2. motor ponderado; 3. gaps e roadmap; 4. wizard Streamlit; 5. testes; 6. documentação.
O repositório oficial da Etapa 2 recebe inicialmente apenas a cópia integral da Atividade 08. Melhorias ficam no temporário até nova instrução.
