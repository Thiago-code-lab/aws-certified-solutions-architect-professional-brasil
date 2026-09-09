# Casos de Uso - Modernizacao

## Cenario 1 - Monolito com novas APIs

### Contexto
Sistema legado concentra web, batch e regras em uma base unica.

### Requisitos
Novas APIs mobile, menor tempo de release e baixo risco.

### Arquitetura recomendada
Strangler pattern com API layer, novos servicos por dominio e monolito para funcoes estaveis.

### Por que
Entrega valor antes da substituicao completa.

### Trade-offs
Convivencia e observabilidade ficam mais complexas.

### Por que nao as alternativas
Rewrite total aumenta risco; rehost puro nao melhora release.

### Sinal de prova
Sem tolerancia para rewrite longo indica migracao incremental.

## Cenario 2 - Processamento assincrono

### Contexto
Checkout dispara notificacao, antifraude, faturamento e analytics.

### Requisitos
Absorver picos, retry e evitar falha cascata.

### Arquitetura recomendada
EventBridge para eventos de dominio e SQS para consumidores que precisam de buffer.

### Por que
Reduz acoplamento e permite falha parcial.

### Trade-offs
Consistencia eventual e idempotencia obrigatorias.

### Por que nao as alternativas
Chamadas sincrônicas em cadeia ampliam latencia e risco.

### Sinal de prova
Picos e consumidores independentes indicam assincronia.

## Cenario 3 - Escolha de plataforma

### Contexto
Time pequeno entrega servicos simples; area central tem Kubernetes maduro.

### Requisitos
Baixo overhead para alguns servicos e controle de runtime para outros.

### Arquitetura recomendada
Lambda/Fargate para servicos simples e EKS somente onde Kubernetes agrega valor.

### Por que
A escolha respeita skill e restricao operacional.

### Trade-offs
Mais de uma plataforma exige padroes comuns.

### Por que nao as alternativas
Forcar EKS para tudo aumenta toil; forcar Lambda ignora runtime.

### Sinal de prova
Skill do time e overhead operacional sao sinais decisivos.
