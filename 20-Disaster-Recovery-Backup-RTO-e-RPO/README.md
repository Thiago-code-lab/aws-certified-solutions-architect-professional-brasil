# 20 - Disaster Recovery, Backup, RTO e RPO

Este modulo aprofunda decisoes de continuidade de negocio no SAP-C02. O foco nao e decorar nomes de estrategias, mas escolher a arquitetura correta conforme RTO, RPO, criticidade, custo, consistencia de dados, automacao e capacidade operacional da organizacao.

## Objetivos

- Diferenciar RTO e RPO e traduzir metas de negocio em desenho tecnico.
- Comparar Backup & Restore, Pilot Light, Warm Standby e Active-Active/Multi-Site.
- Separar alta disponibilidade Multi-AZ de recuperacao de desastre Multi-Region.
- Escolher entre AWS Backup, snapshots, replicacao nativa, Amazon Route 53, AWS Elastic Disaster Recovery e automacao de infraestrutura.
- Projetar runbooks, testes de failover e mecanismos de retorno controlado.

## Conceitos fundamentais

| Conceito | Significado | Implicacao arquitetural |
| --- | --- | --- |
| RTO | Tempo maximo aceitavel para restaurar o servico | Define quanto ambiente precisa estar pronto antes do desastre |
| RPO | Perda maxima aceitavel de dados | Define frequencia/forma de replicacao e backup |
| Multi-AZ | Resiliencia dentro de uma regiao | Protege contra falha de AZ, nao contra indisponibilidade regional |
| Multi-Region | Recuperacao ou operacao entre regioes | Reduz impacto regional, mas aumenta custo e complexidade |

## Estrategias de DR

| Estrategia | RTO/RPO tipico | Custo | Quando usar |
| --- | --- | --- | --- |
| Backup & Restore | Horas | Baixo | Sistemas menos criticos, baixo custo, recuperacao manual ou semi-automatica |
| Pilot Light | Dezenas de minutos a horas | Medio-baixo | Dados e componentes minimos sempre replicados; compute sobe no desastre |
| Warm Standby | Minutos | Medio-alto | Ambiente reduzido ja ativo em outra regiao |
| Active-Active / Multi-Site | Segundos a poucos minutos | Alto | Sistemas criticos, trafego distribuido e operacao madura |

## AWS Backup vs Elastic Disaster Recovery

| Necessidade | Melhor encaixe |
| --- | --- |
| Politicas centralizadas de backup, retenção e auditoria | AWS Backup |
| Backup cross-account/cross-region de recursos AWS suportados | AWS Backup |
| Recuperacao de servidores com replicacao continua em baixo nivel | AWS Elastic Disaster Recovery |
| Migrar ou recuperar workloads baseados em servidores com baixo RPO | AWS Elastic Disaster Recovery |
| Restaurar dados para ponto no tempo de servicos gerenciados | Backup/snapshot/replicacao nativa do servico |

## Raciocinio SAP-C02

### Cenario 1: ERP interno com RTO de 8 horas

- Cenario: ERP usado em horario comercial, tolera algumas horas de indisponibilidade.
- Restricao: orcamento limitado e equipe pequena.
- Decisao: Backup & Restore com AWS Backup, copias cross-region, IaC para recriar infraestrutura e testes trimestrais.
- Trade-off: menor custo recorrente, mas recuperacao depende de automacao e execucao do runbook.

### Cenario 2: plataforma de pedidos com RTO de 30 minutos

- Cenario: aplicacao critica precisa retomar operacao rapidamente em outra regiao.
- Restricao: nao ha orcamento para capacidade integral duplicada.
- Decisao: Warm Standby com banco replicado, ambiente reduzido ja implantado, Route 53 failover e escalabilidade automatizada.
- Trade-off: custo maior que pilot light, mas reduz tempo de provisionamento no desastre.

### Cenario 3: pagamentos globais com RPO quase zero

- Cenario: plataforma global nao pode perder transacoes confirmadas.
- Restricao: consistencia, latencia e conflitos de escrita sao pontos centrais.
- Decisao: Active-Active quando a aplicacao suporta particionamento, idempotencia e resolucao de conflitos; caso contrario, usar active-passive com replicacao forte onde aplicavel.
- Trade-off: multi-site reduz impacto regional, mas exige maturidade alta de dados, deploy, observabilidade e operacao.

## Arquitetura de referencia

```text
Primary Region                           DR Region
--------------                           ---------
Route 53 health checks  ------------->   Failover records
ALB + Auto Scaling                       ALB + scaled-down ASG
ECS/EKS/EC2 workloads                    Warm standby workloads
RDS/Aurora primary   --replication-->    Read replica / global database
S3 bucket           --CRR----------->    S3 replica bucket
AWS Backup vault    --copy---------->    Backup vault
CloudWatch alarms   --events-------->    Incident automation
```

## Estudos Complementares

- Revise fundamentos de snapshots, S3 versioning, RDS Multi-AZ e Auto Scaling quando necessario.
- Para SAP-C02, priorize a traducao entre requisitos de negocio, RTO/RPO, consistencia de dados, custo e complexidade operacional.

## Arquivos do modulo

- [Questoes](questoes.md)
- [Flashcards](flashcards.md)
- [Cheatsheet](cheatsheet.md)
- [Casos de uso](casos-de-uso.md)
- [Links oficiais](links.md)
- [Lab guiado](lab.md)

---

CloudStudy - Trilha AWS Solutions Architect Professional
