# Workshop - Estrategia de Deployment

> Exercicio de desenho. Nenhum deployment precisa ser executado.

## Cenario

Uma plataforma SaaS possui contas separadas de desenvolvimento, staging e producao. O produto atende usuarios globais, tem releases frequentes, disponibilidade estrita e precisa de aprovacao de compliance antes de producao.

## Tarefa 1 - Estrutura IaC

Defina:

- Stacks por dominio.
- O que poderia usar nested stacks.
- O que deveria usar StackSets.
- Como evitar drift.

## Tarefa 2 - Caminho de promocao

```text
Git -> Build/Test -> Dev -> Staging -> Approval -> Production
```

Explique:

- Quem aprova.
- Quais evidencias sao exigidas.
- Quais roles o pipeline assume em cada conta.

## Tarefa 3 - Estrategia de deployment

Escolha uma estrategia para:

| Mudanca | Estrategia | Justificativa |
| --- | --- | --- |
| Alteracao pequena de UI |  |  |
| Nova regra de billing |  |  |
| Nova infraestrutura de rede |  |  |
| Atualizacao de API critica |  |  |

## Tarefa 4 - Rollback e falhas

Documente:

- Rollback de aplicacao.
- Rollback de infraestrutura.
- O que fazer se change set substituir recurso critico.
- Como reduzir blast radius por conta, regiao ou porcentagem de trafego.

## Entrega esperada

- Diagrama de pipeline multi-account.
- Estrutura de stacks/StackSets.
- Estrategia de deployment por tipo de mudanca.
- Approval gates.
- Plano de rollback.
- Trade-offs de velocidade, custo temporario e risco.
