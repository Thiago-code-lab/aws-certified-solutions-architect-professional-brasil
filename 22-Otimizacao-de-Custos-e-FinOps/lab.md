# Lab - FinOps Architecture Review Workshop

Use dados ficticios. Nenhum recurso AWS deve ser criado.

## Cenario

| Categoria | Custo mensal | Observacao |
| --- | ---: | --- |
| EC2 On-Demand | USD 42.000 | Baseline 60%, picos sazonais |
| RDS | USD 18.000 | CPU media 25% |
| S3 Standard | USD 9.000 | 70% sem acesso em 180 dias |
| NAT Gateway | USD 7.500 | Chamadas a servicos AWS |
| Data Transfer | USD 11.000 | Replicacao e download publico |
| EBS | USD 5.000 | Volumes antigos |
| Dev ocioso | USD 6.500 | Ambientes 24x7 |

## Tarefas

1. Identifique drivers.
2. Classifique quick wins, arquitetura e compromisso.
3. Determine rightsizing.
4. Avalie Savings Plans ou RI apos medir.
5. Avalie Spot.
6. Proponha lifecycle S3.
7. Preserve disponibilidade e DR.
8. Crie plano priorizado.

## Criterios

- Nao comprar compromisso antes de remover desperdicio.
- Separar custo de resiliencia.
- Definir ownership.
- Explicar risco de cada acao.
