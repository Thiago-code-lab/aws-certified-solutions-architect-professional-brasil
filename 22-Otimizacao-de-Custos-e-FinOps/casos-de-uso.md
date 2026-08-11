# Casos de Uso - FinOps

## Cenario 1 - Custo sem ownership

### Contexto

Uma empresa tem billing consolidado e nao consegue explicar custos por produto.

### Requisitos

- Atribuir custos por unidade.
- Alertar desvios.
- Criar accountability.

### Arquitetura recomendada

Padronizar contas/tags, habilitar CUR, usar Cost Explorer para analise, Budgets por owner e processo de revisao recorrente.

### Por que

Sem alocacao, qualquer corte e arbitrario.

### Trade-offs

Governanca de tagging exige disciplina e automacao.

### Por que nao as alternativas

Savings Plans sem visibilidade podem comprometer gasto errado; desligamento aleatorio causa incidente.

### Sinal de prova

"cost attribution", "business unit", "many accounts".

## Cenario 2 - Plataforma com baseline e picos

### Contexto

Um e-commerce tem baseline previsivel e campanhas com demanda variavel.

### Requisitos

- Reduzir custo recorrente.
- Preservar disponibilidade em picos.
- Evitar compromisso excessivo.

### Arquitetura recomendada

Rightsizing, commitment para baseline e autoscaling com On-Demand/Spot para partes tolerantes a interrupcao.

### Por que

Separa uso previsivel de variabilidade.

### Trade-offs

Mais planejamento de capacidade e politicas de fallback.

### Por que nao as alternativas

Commitment para pico desperdiça; On-Demand puro perde desconto; Spot para tudo pode afetar disponibilidade.

### Sinal de prova

"stable baseline", "unpredictable peaks".

## Cenario 3 - Custo de dados e rede

### Contexto

Uma plataforma global reduziu EC2, mas a fatura continua alta por NAT Gateway e transferencia inter-region.

### Requisitos

- Reduzir custo sem quebrar resiliencia.
- Manter usuarios globais.
- Entender fluxo de dados.

### Arquitetura recomendada

Mapear trafego, usar endpoints VPC quando aplicavel, cache/CDN, localidade de processamento e replicacao seletiva.

### Por que

O driver de custo e arquitetura de dados/rede, nao tamanho de instancia.

### Trade-offs

Pode exigir redesenho e revisao de DR/consistencia.

### Por que nao as alternativas

Reserved Instances nao reduzem transferencia; arquivar dados sem padrao de acesso pode quebrar app.

### Sinal de prova

"data transfer bill", "NAT Gateway", "inter-Region".
