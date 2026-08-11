# Workshop Pratico - Assessment de Migracao

> Este lab e um workshop de assessment. Nao provisione recursos AWS.

## Objetivo

Classificar um portfolio ficticio, escolher estrategias dos 7Rs, planejar waves, identificar dependencias, blockers e rollback.

## Portfolio ficticio

| Workload | Descricao | Dependencias | Criticidade | Restricoes |
| --- | --- | --- | --- | --- |
| BillingApp | Aplicacao Java em VMs com banco Oracle compartilhado | ERP, OracleDB | Alta | Downtime maximo 4h |
| IntranetLegacy | Portal interno sem dono claro | LDAP antigo | Baixa | Uso desconhecido |
| CRMOnPrem | Software comercial com SaaS oficial | AD, relatorios | Media | Contrato expira em 9 meses |
| AnalyticsBatch | Jobs noturnos em servidores Linux | S3-like storage, DB read-only | Media | Janela noturna |
| PaymentsCore | Monolito critico com deploy manual | Mainframe, OracleDB, filas | Alta | Alto valor de modernizacao |
| FileArchive | Servidor de arquivos historicos | Nenhuma critica | Baixa | Retencao legal |

## Tarefa 1 - Classificar workloads

Preencha:

| Workload | R escolhido | Justificativa | Alternativas rejeitadas |
| --- | --- | --- | --- |
| BillingApp |  |  |  |
| IntranetLegacy |  |  |  |
| CRMOnPrem |  |  |  |
| AnalyticsBatch |  |  |  |
| PaymentsCore |  |  |  |
| FileArchive |  |  |  |

## Tarefa 2 - Identificar dependencias

Para cada workload, responda:

- Quais sistemas precisam migrar antes?
- Quais podem permanecer on-premises temporariamente?
- Ha dependencia de identidade, rede, banco, licenca ou dados?
- Qual dependencia torna a wave arriscada?

## Tarefa 3 - Planejar waves

Modelo sugerido:

| Wave | Workloads | Motivo | Blockers |
| --- | --- | --- | --- |
| Pre-wave | Retire/assessment adicional | Reduz escopo | Confirmar uso real |
| Wave 1 | Baixo risco | Validar landing zone | Rede/IAM/logging |
| Wave 2 | Media dependencia | Ganhar escala | Banco/licenca |
| Wave 3 | Criticos/modernizacao | Maior valor | Downtime e rollback |

## Tarefa 4 - Blockers e rollback

Liste para cada wave:

- Blockers tecnicos.
- Blockers de negocio.
- Plano de rollback.
- Criterios de sucesso.
- Observabilidade necessaria.

## Tarefa 5 - Defender decisoes

Para cada workload, escreva:

1. Por que o R escolhido e o melhor.
2. Por que pelo menos duas alternativas foram rejeitadas.
3. Qual risco residual permanece.
4. Qual informacao adicional poderia mudar a decisao.

## Exemplo de resposta esperada

- `IntranetLegacy`: provavel Retire ou Retain curto para confirmar uso. Rehost seria fraco se nao houver dono/uso.
- `CRMOnPrem`: provavel Repurchase se SaaS atender compliance e migracao de dados for viavel.
- `PaymentsCore`: provavel Refactor/Re-architect faseado, talvez com etapa intermediaria, porque valor e dor operacional justificam investimento.

## Entrega final

O estudante deve produzir:

- Matriz 7Rs preenchida.
- Mapa de dependencias.
- Plano de waves.
- Lista de blockers.
- Plano de rollback por wave.
- Justificativa das alternativas rejeitadas.
