# Casos de Uso - FinOps

## Cenario 1 - Chargeback

### Contexto
Fatura consolidada cresce e areas negam responsabilidade.

### Requisitos
Atribuicao por produto, centro de custo, ambiente e conta.

### Arquitetura recomendada
Padrao de contas e tags, CUR e Budgets por owner.

### Por que
Visibilidade e alocacao precedem otimizacao confiavel.

### Trade-offs
Tags e contas exigem governanca.

### Por que nao as alternativas
Comprar desconto sem ownership esconde desperdicio.

### Sinal de prova
CFO, chargeback e showback indicam CUR, tags e Budgets.

## Cenario 2 - Baseline e picos

### Contexto
Servico web opera 24x7 com campanhas sazonais.

### Requisitos
Disponibilidade e custo menor.

### Arquitetura recomendada
Rightsizing, Auto Scaling, Savings Plans para baseline e elasticidade para pico.

### Por que
Separa demanda previsivel de demanda incerta.

### Trade-offs
Exige medicao e revisao periodica.

### Por que nao as alternativas
Comprometer pico desperdiça; Spot integral arrisca disponibilidade.

### Sinal de prova
Baseline estavel mais pico imprevisivel pede compromisso parcial.

## Cenario 3 - Transferencia alta

### Contexto
Aplicacao replica dados entre regioes e serve downloads publicos sem cache.

### Requisitos
Reduzir custo preservando experiencia e DR.

### Arquitetura recomendada
CloudFront, revisao de replicacao por RPO, lifecycle e endpoints privados quando suportados.

### Por que
Custo de transferencia nasce do desenho de fluxo.

### Trade-offs
Cache e politica de dados aumentam complexidade.

### Por que nao as alternativas
Cortar replicacao sem RPO e arriscado.

### Sinal de prova
Data transfer alto exige revisar topologia.
