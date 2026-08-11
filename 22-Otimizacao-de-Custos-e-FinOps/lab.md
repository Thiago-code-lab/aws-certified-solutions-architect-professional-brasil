# Workshop - Revisao Arquitetural FinOps

> Exercicio de analise. Nao acesse console nem altere recursos reais.

## Cenario

Uma empresa SaaS multi-account quer reduzir custo mensal sem comprometer disponibilidade dos clientes.

## Dados mensais ficticios

| Categoria | Custo mensal | Observacao |
| --- | --- | --- |
| EC2 | USD 42.000 | 60% baseline estavel, 40% picos |
| RDS | USD 28.000 | Duas instancias superdimensionadas |
| S3 | USD 18.000 | 70% dados raramente acessados |
| NAT Gateway | USD 12.000 | Alto trafego para servicos AWS publicos |
| Data Transfer | USD 15.000 | Replicacao inter-region ampla |
| EBS | USD 7.000 | Volumes antigos sem owner |
| CloudFront | USD 4.000 | Reduz origem, custo aceitavel |
| Idle development | USD 9.000 | Ambientes ligados 24x7 |

## Tarefa 1 - Identificar drivers

Classifique:

- Custo de compute.
- Custo de banco.
- Custo de armazenamento.
- Custo de rede.
- Custo ocioso.

## Tarefa 2 - Quick wins

Liste acoes de baixo risco:

- Scheduling dev.
- Volumes EBS sem owner.
- Tags obrigatorias.
- Budgets por time.

## Tarefa 3 - Commitment

Defina:

- Qual parte do EC2 e baseline.
- O que pode receber Savings Plans/RIs.
- O que deve continuar flexivel.
- Quais workloads podem usar Spot.

## Tarefa 4 - Mudancas arquiteturais

Avalie:

- VPC endpoints para reduzir NAT quando aplicavel.
- Lifecycle S3.
- Rightsizing RDS.
- Revisao de replicacao inter-region.
- Cache/CDN para reduzir origem.

## Tarefa 5 - Plano priorizado

Monte:

| Prioridade | Acao | Beneficio esperado | Risco | Validacao |
| --- | --- | --- | --- | --- |
| 1 |  |  |  |  |
| 2 |  |  |  |  |
| 3 |  |  |  |  |

## Entrega esperada

- Ranking de oportunidades.
- Separacao quick win vs mudanca arquitetural.
- Decisoes de commitment.
- Riscos de disponibilidade.
- Mecanismo de monitoramento continuo.
- Explicacao de por que menor preco unitario nem sempre e menor custo total.
