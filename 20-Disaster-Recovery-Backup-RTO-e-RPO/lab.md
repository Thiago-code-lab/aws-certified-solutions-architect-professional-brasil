# Lab Guiado - Arquitetura de DR Multi-Region

> Lab de desenho arquitetural. Antes de executar em conta real, estime custos de duplicacao regional, replicacao, backups, NAT, endpoints, Route 53 e trafego inter-regional.

## Objetivo

Desenhar uma estrategia de DR para uma aplicacao web com RTO de 30 minutos e RPO de 5 minutos, usando Warm Standby como referencia.

## Requisitos

- Aplicacao publica com usuarios externos.
- Banco relacional critico.
- Uploads de usuarios armazenados em S3.
- Failover regional.
- Recuperacao testavel sem impactar producao.

## Arquitetura alvo

```text
Primary Region                         DR Region
--------------                         ---------
Route 53 weighted/failover records --> ALB standby
ALB + Auto Scaling / ECS               Auto Scaling / ECS reduzido
RDS/Aurora primary  ---------------->  Replica / global database
S3 uploads bucket   ---------------->  S3 replica bucket
Secrets Manager     ---------------->  Replicated secrets
CloudWatch alarms   ---------------->  Incident notifications
AWS Backup vault    ---------------->  DR backup vault
```

## Passo 1 - Definir metas

Documente:

| Item | Valor |
| --- | --- |
| RTO | 30 minutos |
| RPO | 5 minutos |
| Estrategia | Warm Standby |
| Failover | Manual aprovado ou automatizado por health check |
| Failback | Planejado apos consistencia de dados |

Checkpoint: se RTO fosse 8 horas, Backup & Restore poderia bastar. Se RTO/RPO fossem quase zero, Active-Active entraria na discussao.

## Passo 2 - Dados

Defina o caminho por tipo de dado:

- Banco: replica cross-region, Aurora Global Database ou mecanismo equivalente da engine.
- Objetos: S3 Cross-Region Replication com versioning.
- Backups: AWS Backup com copia cross-region e retencao adequada.
- Segredos: replicacao de secrets ou automacao para recriacao segura na regiao secundaria.
- Chaves: estrategia KMS multi-region quando aplicavel.

Checkpoint: RPO depende do mecanismo mais lento ou mais fraco da cadeia de dados.

## Passo 3 - Infraestrutura

Modele tudo com IaC:

- VPCs, sub-redes, rotas e security groups.
- ALB, target groups e compute.
- IAM roles, policies e parametros.
- Observabilidade: alarms, dashboards e logs.
- Runbooks de failover e validacao.

Checkpoint: infraestrutura nao versionada aumenta RTO real.

## Passo 4 - Failover

Sequencia sugerida:

1. Declarar incidente e congelar mudancas.
2. Verificar saude da regiao primaria e estado da replicacao.
3. Promover banco/replica conforme procedimento do servico.
4. Escalar compute na regiao DR.
5. Atualizar Route 53 para enviar trafego ao endpoint secundario.
6. Validar login, escrita, leitura, jobs e integracoes externas.
7. Registrar RTO/RPO obtidos.

## Passo 5 - Teste controlado

Execute um teste em janela aprovada:

- Simule indisponibilidade usando ambiente isolado ou failover planejado.
- Meça tempo ate aplicacao funcional.
- Meça perda ou atraso de dados.
- Verifique alarmes e logs.
- Atualize runbook com lacunas encontradas.

## Resultado esperado

A entrega do lab deve conter:

- Estrategia escolhida e justificativa.
- Matriz RTO/RPO por componente.
- Diagrama de failover.
- Runbook resumido.
- Lista de riscos: consistencia, DNS cache, segredos, integracoes externas, failback e custo.
