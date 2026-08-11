# 29 - Labs Praticos

Este modulo e o hub de laboratorios da trilha SAP-C02. Ele nao substitui os labs específicos dos modulos flagship; organiza a pratica por objetivo arquitetural, custo, risco e ordem recomendada de execucao.

## Como usar este hub

1. Escolha um lab pelo dominio arquitetural que voce quer treinar.
2. Leia o objetivo, restricoes e criterios de sucesso antes de abrir o console.
3. Estime custo e defina uma janela curta de execucao.
4. Registre decisoes, evidencias e lacunas encontradas.
5. Destrua recursos quando o lab for executado em conta real.

## Indice de labs por tema

| Tema | Lab principal | Resultado esperado |
| --- | --- | --- |
| Governanca multi-account | [Modulo 02 - Organizations e Control Tower](../02-Organizations-Control-Tower-e-Multi-Account/README.md) | Estrutura de contas, OUs, SCPs, logging e seguranca centralizada |
| Rede avancada | [Modulo 05 - TGW, Peering e PrivateLink](../05-Redes-Avancadas-VPC-e-Transit-Gateway/lab.md) | Desenho hub-and-spoke, segmentacao de rotas e exposicao privada de servico |
| Disaster Recovery | [Modulo 20 - DR Multi-Region](../20-Disaster-Recovery-Backup-RTO-e-RPO/lab.md) | Estrategia Warm Standby, matriz RTO/RPO e runbook de failover |
| Migracao | [Modulo 23 - Estrategia dos 7Rs](../23-Migration-Hub-Discovery-e-Estrategia-dos-7Rs/README.md) | Escolha de estrategia por restricao de negocio e dependencia tecnica |
| Transferencia de dados | [Modulo 25 - Transferencia em escala](../25-DataSync-Snow-Transfer-Family-e-Transferencia-de-Dados/README.md) | Escolha entre DataSync, Snow Family, Transfer Family e transferencia online |
| Casos integrados | [Modulo 28 - Casos de uso reais](../28-Casos-de-Uso-Reais/README.md) | Analise de cenarios com multiplas restricoes simultaneas |

## Template de execucao

Use este checklist para qualquer lab:

| Etapa | Pergunta |
| --- | --- |
| Objetivo | Qual decisao arquitetural o lab valida? |
| Escopo | Quais contas, regioes e servicos participam? |
| Restricoes | Qual requisito domina: custo, seguranca, RTO/RPO, latencia, operacao ou compliance? |
| Evidencia | Que logs, metricas, outputs ou diagramas comprovam o resultado? |
| Limpeza | Quais recursos precisam ser removidos ao final? |

## Labs recomendados para a fase atual

### 1. Organizacao multi-account

- Definir OUs para Security, Infrastructure, Workloads e Sandbox.
- Mapear quais contas recebem GuardDuty, Security Hub, CloudTrail e logs centralizados.
- Criar uma matriz SCP: negar regioes nao aprovadas, proteger logging e bloquear acoes destrutivas de seguranca.

### 2. Rede hub-and-spoke

- Desenhar TGW com route tables separadas.
- Comparar o mesmo requisito com VPC Peering e PrivateLink.
- Documentar onde cada padrao deixa de ser adequado.

### 3. DR Warm Standby

- Definir RTO/RPO por componente.
- Mapear replicacao de banco, S3, segredos, infraestrutura e DNS.
- Escrever runbook de failover com checkpoints mensuraveis.

## Regras de seguranca e custo

- Nao execute labs em contas de producao.
- Use tags de identificacao e expiração.
- Prefira desenho arquitetural quando o custo de execucao real for alto.
- Evite deixar NAT Gateway, TGW attachments, endpoints, replicas ou ambientes standby ativos sem necessidade.
- Revise permissoes antes de criar recursos multi-account.

## Estudos Complementares

- Para cada lab, retorne ao modulo teorico correspondente antes de executar.
- Use documentacao oficial da AWS para validar limites, custos e comportamento atual dos servicos.
- Registre duvidas e erros recorrentes no modulo de revisao/simulado da trilha antes de avancar.

---

CloudStudy - Trilha AWS Solutions Architect Professional
