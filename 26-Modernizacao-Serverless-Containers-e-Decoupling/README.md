# 26 - Modernizacao: Serverless, Containers e Decoupling

Este modulo nao ensina "Lambda, ECS e EKS" como lista de servicos. Ele ensina como modernizar um workload existente sem cair em reescrita grande, cara e arriscada. Modernizacao Professional combina valor de negocio, prazo, skills do time, acoplamento, operacao, escala, dados e capacidade de migrar incrementalmente.

## Objetivos

- Diferenciar rehost, replatform e refactor em decisoes de modernizacao.
- Aplicar strangler pattern para decompor monolitos gradualmente.
- Escolher limites sincronos e assincronos com SQS, SNS, EventBridge e Step Functions.
- Posicionar Lambda, ECS, EKS e Fargate conforme carga, operacao e skills.
- Evitar big-bang rewrite quando o risco supera o beneficio.
- Definir etapas de migracao incremental com rollback e convivencia legado/novo.

## Comparacoes criticas

| Comparacao | Decisao Professional |
| --- | --- |
| Rehost vs modernize | Rehost reduz prazo; modernizacao ataca causas de escala, agilidade e operacao |
| Replatform vs refactor | Replatform muda plataforma com pouca alteracao; refactor muda arquitetura/codigo |
| Monolito vs modular | Monolito pode ser aceitavel se estavel; modularidade ajuda dominios que mudam/escala independentemente |
| Sincrono vs assincrono | Sincrono simplifica resposta imediata; assincrono desacopla e absorve picos |
| SQS vs EventBridge | SQS e fila ponto a ponto com buffering; EventBridge roteia eventos entre produtores/consumidores |
| Lambda vs containers | Lambda reduz operacao para eventos curtos; containers servem runtimes/processos longos ou maior controle |
| ECS vs EKS | ECS reduz operacao AWS-native; EKS faz sentido com padrao Kubernetes e skills existentes |
| Fargate vs instancias | Fargate reduz gestao de servidores; instancias dao mais controle/custo em escala especifica |
| Big-bang rewrite vs strangler | Strangler reduz risco migrando capacidades por fatias |

## Evolucao strangler

Inicial:

```text
Users
  |
Legacy Monolith
  |
Database
```

Transicao:

```text
Users
  |
API / Routing Layer
  |
  +------ Legacy Monolith
  |
  +------ New Service A
  |
  +------ New Service B
              |
           SQS/EventBridge
```

Explicacao:

- A camada de API/roteamento direciona novas capacidades para servicos modernos.
- O monolito continua atendendo partes nao migradas.
- Eventos e filas desacoplam processamento em background.
- Cada fatia migrada precisa observabilidade, rollback e estrategia de dados.
- O objetivo e reduzir risco e entregar valor antes de concluir toda a decomposicao.

## Matriz de modernizacao

| Cenario | Estrategia | Tecnologia possivel | Beneficio | Trade-off |
| --- | --- | --- | --- | --- |
| Legado estavel com prazo curto | Rehost/replatform | EC2/RDS/ECS simples | Cumpre prazo | Pouca melhoria arquitetural |
| API stateless de alto scale | Container/serverless | ECS Fargate ou Lambda | Escala e operacao menor | Limites/runtime precisam ser avaliados |
| Processamento orientado a eventos | Decoupling assincrono | SQS/EventBridge/Step Functions | Absorve picos | Consistencia eventual |
| Organizacao madura em Kubernetes | Containers gerenciados | EKS | Portabilidade/ecossistema | Mais operacao |
| Time pequeno buscando low-ops | Serverless/managed services | Lambda, Fargate, DynamoDB quando aplicavel | Menos toil | Menos controle fino |
| Monolito muito acoplado | Strangler gradual | API Gateway/ALB + novos servicos | Reduz risco | Convive com legado por mais tempo |
| Batch sazonal | Containers ou serverless batch | ECS/Fargate/Lambda conforme duracao | Escala sob demanda | Observabilidade e retry |
| Dominio muda rapidamente | Refactor focalizado | Servico dedicado + eventos | Agilidade | Requer ownership de dominio |

## Raciocinio SAP-C02

### Cenario 1: monolito de 10 anos

- Cenario: release lento, picos sazonais e nova demanda mobile.
- Restricoes: negocio nao aceita rewrite multi-ano.
- Sinal: modernizacao incremental.
- Melhor decisao: strangler pattern, extrair capacidades de maior valor, manter partes estaveis no monolito e introduzir eventos/filas para background.
- Trade-off: convivencia temporaria aumenta complexidade, mas reduz risco.
- Por que nao alternativas: big-bang rewrite atrasa valor e concentra risco; rehost puro nao melhora ciclo de release.

### Cenario 2: processamento de pedidos em picos

- Cenario: pedidos chegam em rajadas e integracoes externas falham.
- Restricoes: nao perder mensagens, desacoplar processamento e permitir retry.
- Melhor decisao: SQS para buffering, consumidores em Lambda/ECS e DLQ; EventBridge se o problema for roteamento de eventos entre dominios.
- Trade-off: consistencia eventual e necessidade de idempotencia.

### Cenario 3: escolha ECS vs EKS

- Cenario: empresa quer containers, mas tem time pequeno e sem Kubernetes maduro.
- Restricoes: reduzir operacao e entregar rapido.
- Melhor decisao: ECS com Fargate para reduzir overhead, salvo requisito claro de Kubernetes.
- Trade-off: menos portabilidade de ecossistema Kubernetes, menor complexidade operacional.

## Estudos Complementares

Use a trilha Associate apenas de forma contextual para revisar fundamentos de Lambda, ECS/EKS/Fargate, SQS, SNS e EventBridge:

https://github.com/Thiago-code-lab/aws-certified-solutions-architect-associate-brasil

## Arquivos do modulo

- [Questoes](questoes.md)
- [Flashcards](flashcards.md)
- [Cheatsheet](cheatsheet.md)
- [Casos de uso](casos-de-uso.md)
- [Referencias oficiais](links.md)
- [Workshop de modernizacao](lab.md)

---

CloudStudy - Trilha AWS Solutions Architect Professional
