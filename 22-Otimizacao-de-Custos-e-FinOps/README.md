# 22 - Otimizacao de Custos e FinOps

Este modulo trata custo como disciplina arquitetural continua. No SAP-C02, otimizar custo nao significa escolher sempre o recurso mais barato; significa equilibrar requisito de negocio, disponibilidade, performance, operacao, risco e modelo de compra com visibilidade suficiente para tomar decisao.

## Objetivos

- Construir visibilidade com Cost Explorer, Budgets, Cost and Usage Report e tags.
- Alocar custos por conta, produto, ambiente e unidade de negocio.
- Diferenciar Savings Plans, Reserved Instances, On-Demand e Spot.
- Aplicar rightsizing, storage lifecycle, desligamento de recursos ociosos e revisao de transferencia de dados.
- Avaliar custo de arquitetura: NAT Gateway, trafego inter-region, overprovisioning, banco, armazenamento e operacao.
- Usar FinOps como ciclo continuo, nao evento unico.

## Loop FinOps

```text
Measure
   |
Allocate
   |
Analyze
   |
Optimize
   |
Commit
   |
Monitor
   |
Repeat
```

Otimização e continua porque uso, arquitetura, trafego, precos, releases e requisitos de negocio mudam. Comprometer gasto antes de medir pode cristalizar desperdicio; otimizar sem alocacao impede accountability.

## Distincoes criticas

| Comparacao | Decisao Professional |
| --- | --- |
| Savings Plans vs Reserved Instances | Savings Plans oferecem flexibilidade de compute; RIs podem ser especificas para familias/servicos e requerem encaixe preciso |
| On-Demand vs Spot | On-Demand para previsibilidade/disponibilidade; Spot para workloads tolerantes a interrupcao |
| Cost Explorer vs Budgets | Cost Explorer analisa historico/tendencia; Budgets alerta/acompanha limites |
| Visibilidade vs controle | Ver custo nao reduz custo sozinho; controle exige ownership e acoes |
| Rightsizing vs compromisso | Rightsizing reduz desperdicio; commitment desconta uso esperado apos estabilizar baseline |
| Compute vs data transfer | Computacao visivel pode esconder transferencia inter-AZ/inter-region/NAT significativa |
| Menor preco infra vs menor custo total | Servico gerenciado pode custar mais em recurso, mas reduzir operacao e risco |

## Tabela de decisao

| Sinal | Estrategia provavel | Beneficio | Risco/Trade-off | Armadilha |
| --- | --- | --- | --- | --- |
| Baseline EC2 estavel | Savings Plans/RIs apos rightsizing | Desconto em uso previsivel | Compromisso financeiro | Comprar antes de medir |
| Workload imprevisivel | On-Demand + autoscaling | Flexibilidade | Custo unitario maior | Comprometer picos temporarios |
| Batch tolerante a interrupcao | Spot Instances | Custo menor | Interrupcoes | Usar para workload stateful critico |
| Recursos dev ociosos | Scheduler/desligamento/tag owner | Quick win | Pode impactar testes | Desligar sem ownership |
| Arquivo S3 massivo | Lifecycle para classes adequadas | Reduz armazenamento | Custo/latencia de recuperacao | Mover dados acessados frequentemente |
| Multi-account sem ownership | Tags + contas por produto + CUR | Alocacao clara | Governanca de tagging | Otimizar sem dono |
| Alta transferencia inter-region | Redesenhar proximidade/cache/replicacao | Reduz custo recorrente | Pode alterar resiliencia | Olhar so compute |
| Banco superdimensionado | Rightsizing/read replicas/cache quando aplicavel | Reduz custo sem perder SLA | Testes de performance | Cortar capacidade sem medir |
| Demanda variavel | Auto Scaling/serverless/managed scaling | Paga mais proximo do uso | Limites e cold starts | Capacidade fixa por medo |

## Raciocinio SAP-C02

### Cenario 1: CFO exige atribuicao por unidade

- Cenario: a conta consolidada cresce, mas times contestam cobrancas.
- Restricoes: multiplas contas, produtos e ambientes.
- Sinal: visibilidade e alocacao antes de corte.
- Melhor decisao: estrategia de contas/tags, Cost Categories/CUR, Budgets por owner e relatorios recorrentes.
- Trade-off: governanca de tagging e disciplina operacional.
- Por que nao alternativas: desligar recursos sem ownership gera conflito; Savings Plans nao resolvem accountability.

### Cenario 2: baseline estavel com picos

- Cenario: aplicacao tem uso minimo previsivel e campanhas sazonais.
- Restricoes: disponibilidade nao pode cair.
- Melhor decisao: rightsizing, commitment para baseline e On-Demand/Spot para partes tolerantes a interrupcao nos picos.
- Trade-off: maior complexidade de capacidade, melhor equilibrio entre desconto e flexibilidade.

### Cenario 3: custo de rede inesperado

- Cenario: arquitetura global tem alto custo de transferencia inter-region e NAT.
- Restricoes: usuarios globais e requisitos de resiliencia.
- Melhor decisao: analisar fluxo de dados, aproximar processamento dos dados, usar cache/CDN/endpoints quando aplicavel e reduzir trafego desnecessario.
- Trade-off: mudancas de arquitetura podem afetar simplicidade e DR.

## Estudos Complementares

Cloud Practitioner e util para revisar billing, pricing, responsabilidade compartilhada e conceitos basicos de cost management antes de aprofundar FinOps arquitetural:

https://github.com/Thiago-code-lab/aws-certified-cloud-practitioner-brasil

## Arquivos do modulo

- [Questoes](questoes.md)
- [Flashcards](flashcards.md)
- [Cheatsheet](cheatsheet.md)
- [Casos de uso](casos-de-uso.md)
- [Referencias oficiais](links.md)
- [Workshop FinOps](lab.md)

---

CloudStudy - Trilha AWS Solutions Architect Professional
