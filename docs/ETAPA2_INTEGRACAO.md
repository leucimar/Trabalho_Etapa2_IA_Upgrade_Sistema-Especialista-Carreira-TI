# Histórico de integração da Etapa 2

## Estado concluído

As seis etapas foram integradas ao oficial `leucimar/Trabalho_Etapa2_IA_Upgrade_Sistema-Especialista-Carreira-TI`, após o commit inicial com a cópia integral da Atividade 08. As branches `main` e `develop` contêm a versão completa.

O marco inicial `08780128b52349c0d85e6d5400385942533879ea` reproduz a árvore da Atividade 08 em `c91b220a3803dd1306e5f9bc737c5185e581a2b8`. É uma cópia rastreável com novo commit raiz; não é um fork nativo vinculado pelo GitHub. A árvore foi comparada à origem para garantir igualdade.

O temporário preserva a linha de desenvolvimento em `etapa2/main`, `etapa2/develop` e `feature/e2-*`. As branches antigas da AECO foram preservadas. Cada integração no oficial produz um commit com o marco correspondente, e as refs avançam por fast-forward sem reescrever o histórico.

## Rastreabilidade

| Etapa | Branch de origem no temporário | SHA de origem | Commit no oficial |
|---|---|---|---|
| Base AECO | etapa2/main inicial | `66d122c7a2d4436ed7258f9d6860b8a02b956b53` | `08780128b52349c0d85e6d5400385942533879ea` |
| 1. Conhecimento | feature/e2-01-conhecimento | `475df6cfb0280ab999df5d9e881688dfd4665b6f` | `af06ee8113effbb6f8f8892b7cb59f6b444f19c2` |
| 2. Inferência | feature/e2-02-inferencia | `be55508497e89f9d40ac1a5e45efc30112748e5a` | `e81cb2e2b7062cf0aca53009056e89c9d6e48a56` |
| 3. Roadmap | feature/e2-03-roadmap | `278018d96bcf967bb348e459246e1e386a2c5959` | `316a35dbd04f2cf5e765093360984a54b3cfc8dd` |
| 4. Interface | feature/e2-04-interface | `41aa36a9a0139b8e7cb7d04103e0b4aa44b60721` | `4f0f9058f49928e6d2d6fff822830097ef2a6342` |
| 5. Validação | feature/e2-05-validacao | `9091458c99a6d6c54d814fc64f5535a6133f5957` | `d6c61c305a69f681b108db48aa7311caa09f2c59` |
| 6. Documentação | feature/e2-06-documentacao | `8e89b816d71fb09d23c93dbb7f4cb18e98420802` | Commit que adiciona este documento |

A etapa 4 antecipou as correções de navegação de `app.py` já validadas na origem da etapa 5. O corpo do commit registra as duas origens. A etapa 5 manteve essa correção e acrescentou os testes e o aviso de empates do motor, sem reverter a interface.

A etapa 6 adapta README, guia de execução, evidências e este histórico ao estado concluído do oficial. Os comandos de clone agora usam a URL oficial e a branch `main`. Os documentos no temporário continuam registrando o contexto anterior, no qual as melhorias aguardavam integração.

## Validação e continuidade

A etapa 5 foi verificada em 28/10/2026: 80 testes aprovados e `pip check` sem inconsistências. A etapa 6 altera apenas documentos e mantém o mesmo código.

Novos ajustes podem continuar em branches de funcionalidades ou correções, conforme o resultado dos testes do aluno em Windows. Preserve os commits anteriores e registre a validação relevante em cada alteração.

Datas de commits representam trabalho ou integração efetivamente realizados, sem retrodatação.
