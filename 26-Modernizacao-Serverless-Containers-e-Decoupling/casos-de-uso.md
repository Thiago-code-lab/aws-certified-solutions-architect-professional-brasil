# Casos de Uso - Modernizacao

## Cenario 1 - Monolito com demanda mobile

### Contexto

Uma empresa tem monolito relacional de 10 anos e precisa lancar APIs mobile rapidamente.

### Requisitos

- Evitar rewrite multi-ano.
- Entregar valor incremental.
- Reduzir risco operacional.
- Manter regras legadas funcionando.

### Arquitetura recomendada

Strangler pattern com API/routing layer, novos servicos para capacidades mobile e monolito mantendo funcoes estaveis.

### Por que

O negocio precisa de modernizacao incremental, nao substituicao total imediata.

### Trade-offs

Convivencia temporaria, integracao de dados e observabilidade mais complexas.

### Por que nao as alternativas

Big-bang rewrite atrasa valor; rehost puro nao resolve release; EKS sem decomposicao so muda runtime.

### Sinal de prova

"old monolith", "new API/mobile", "cannot accept multi-year rewrite".

## Cenario 2 - Processamento em background

### Contexto

Pedidos acionam integracoes externas lentas e variaveis.

### Requisitos

- Nao bloquear requisicao principal.
- Retry e DLQ.
- Absorver picos.

### Arquitetura recomendada

SQS para buffering, consumidores Lambda ou ECS conforme duracao/processamento, DLQ e idempotencia.

### Por que

O limite assincrono reduz acoplamento e protege a experiencia do usuario.

### Trade-offs

Consistencia eventual e necessidade de rastrear estados.

### Por que nao as alternativas

Fluxo sincrono aumenta latencia; aumentar timeout mascara falhas; EventBridge pode ser complementar, mas fila e melhor para buffering direto.

### Sinal de prova

"background processing", "retry", "traffic spikes".

## Cenario 3 - Containers sem Kubernetes maduro

### Contexto

Um time pequeno quer empacotar servicos em containers, mas nao possui plataforma Kubernetes.

### Requisitos

- Baixa operacao.
- Deploy rapido.
- Stateless services.
- Escala sob demanda.

### Arquitetura recomendada

ECS com Fargate, pipeline de containers e observabilidade padronizada.

### Por que

Entrega containers com menor overhead operacional.

### Trade-offs

Menos controle/ecossistema Kubernetes, mas melhor encaixe para time pequeno.

### Por que nao as alternativas

EKS adiciona plataforma a operar; EC2 autogerenciado aumenta toil; Lambda pode nao encaixar se o processo for longo/customizado.

### Sinal de prova

"small team", "containers", "no Kubernetes expertise".
