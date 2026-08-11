# Cheatsheet - Disaster Recovery

## Matriz de decisao

| Requisito | Estrategia recomendada | Observacao |
| --- | --- | --- |
| RTO em horas, baixo custo | Backup & Restore | Exige backup testado e IaC |
| RTO em menos de 1-2 horas | Pilot Light | Dados e componentes essenciais sempre prontos |
| RTO em minutos | Warm Standby | Ambiente reduzido ja operando |
| RTO/RPO quase zero | Active-Active/Multi-Site | Alto custo e alta complexidade de dados |
| Protecao contra falha de AZ | Multi-AZ | Nao e DR regional |
| Protecao contra falha regional | Multi-Region | Exige dados, DNS, rede e runbook |

## RTO vs RPO

- RTO responde: quanto tempo posso ficar fora?
- RPO responde: quantos dados posso perder?
- RTO direciona capacidade pronta e automacao.
- RPO direciona frequencia de backup, replicacao e consistencia.

## Servicos e padroes

| Necessidade | AWS |
| --- | --- |
| Politica central de backup | AWS Backup |
| Copia cross-region de backups | AWS Backup copy / snapshots |
| DR de servidores | AWS Elastic Disaster Recovery |
| Failover DNS | Amazon Route 53 |
| Replicacao de objetos | S3 Cross-Region Replication |
| Banco relacional Multi-Region | Aurora Global Database ou replica cross-region conforme engine |
| Recriacao de infraestrutura | CloudFormation/CDK/Terraform |
| Automacao de runbook | Systems Manager Automation |

## Perguntas de prova

- O requisito fala em AZ ou regiao?
- O RTO permite provisionar recursos no desastre?
- O RPO exige replicacao continua ou backup periodico basta?
- A aplicacao suporta escrita ativa em multiplas regioes?
- Como o DNS muda no failover?
- Como segredos, KMS keys e parametros existem na regiao secundaria?
- O failback foi planejado?

## Armadilhas

- Confundir backup com DR completo.
- Usar Multi-AZ como resposta para desastre regional.
- Escolher Active-Active sem modelo de consistencia.
- Nao testar restauracao.
- Replicar dados sem replicar infraestrutura, IAM, parametros e observabilidade.
