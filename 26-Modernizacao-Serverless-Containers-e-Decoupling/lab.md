# Lab - Modernization Architecture Workshop

Nenhum recurso deve ser provisionado.

## Cenario

Empresa com monolito de 10 anos, banco relacional compartilhado, picos sazonais, release lento, time pequeno de plataforma, background processing e novas demandas mobile/API.

## Tarefas

1. Identifique limites de dominio.
2. Escolha o que nao modernizar inicialmente.
3. Defina strangler approach.
4. Separe sync e async.
5. Escolha Lambda ou containers por capacidade.
6. Desenhe eventos.
7. Defina etapas.
8. Analise overhead.
9. Explique por que big-bang e mais fraco.

## Arquitetura esperada

```text
Users / Mobile
      |
 API or Routing Layer
      |
      +--> Legacy Monolith --> Shared Database
      +--> Orders API on Fargate/Lambda
      +--> Background events -> SQS/EventBridge -> Workers
```

## Criterios

- Entrega valor antes de substituir tudo.
- Nao cria microservicos sem limite de dominio.
- Eventos incluem idempotencia, retry e observabilidade.
- Plataforma reflete skill e custo operacional.
