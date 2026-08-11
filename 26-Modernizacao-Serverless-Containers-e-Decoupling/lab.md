# Workshop - Arquitetura de Modernizacao

> Exercicio de desenho. Nao provisione recursos AWS.

## Cenario

Uma empresa possui monolito de 10 anos, banco relacional, picos sazonais, ciclo de release lento, pequena equipe de plataforma, processamento em background e novas exigencias mobile/API. O negocio nao aceita rewrite multi-ano.

## Tarefa 1 - Limites de modernizacao

Identifique:

- Dominios que mudam com frequencia.
- Partes estaveis que nao devem ser modernizadas agora.
- Fluxos que exigem resposta sincrona.
- Fluxos que podem ser assincronos.

## Tarefa 2 - Strangler approach

Desenhe:

```text
Users -> API/Routing -> Legacy Monolith
                  \-> New Service A
                  \-> New Service B -> SQS/EventBridge -> Workers
```

Explique como trafego migra por capacidade.

## Tarefa 3 - Lambda ou containers

Preencha:

| Capacidade | Lambda | ECS/Fargate | EKS | Justificativa |
| --- | --- | --- | --- | --- |
| API simples |  |  |  |  |
| Worker longo |  |  |  |  |
| Integracao por evento |  |  |  |  |
| Servico com runtime customizado |  |  |  |  |

## Tarefa 4 - Eventos e filas

Defina:

- Onde usar SQS.
- Onde usar EventBridge.
- Onde Step Functions ajudaria.
- DLQ e idempotencia.
- Observabilidade de eventos.

## Tarefa 5 - Roadmap

Monte fases:

1. Preparar observabilidade e pipeline.
2. Criar camada de API/roteamento.
3. Extrair primeiro dominio de baixo risco.
4. Desacoplar processamento em background.
5. Migrar dominios de maior valor.
6. Descomissionar partes do monolito quando seguro.

## Entrega esperada

- Limites iniciais.
- O que nao modernizar agora.
- Desenho strangler.
- Decisoes Lambda/containers.
- Fluxo de eventos.
- Plano incremental.
- Trade-offs operacionais.
- Justificativa de por que big-bang rewrite e mais fraco.
