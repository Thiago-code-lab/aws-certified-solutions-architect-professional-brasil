# 26 - Modernizacao: Serverless, Containers e Decoupling

Este modulo trata modernizacao como mudanca incremental. O objetivo nao e aprender Lambda, ECS ou EKS isoladamente, mas decidir como evoluir workloads legados sem rewrite de alto risco, reduzindo acoplamento e melhorando velocidade de entrega.

## Objetivos

- Escolher entre rehost, replatform e refactor conforme prazo, risco e valor.
- Aplicar strangler pattern para substituir partes do monolito gradualmente.
- Identificar limites sincronos e assincronos com SQS, SNS, EventBridge e Step Functions.
- Decidir entre Lambda, ECS, EKS e Fargate conforme operacao, escala e skill.
- Evitar modernizacao artificial quando mudanca menor resolve a restricao.

## Strangler pattern

```text
Users
  |
Legacy Monolith
  |
Database
```

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

A camada de roteamento envia novas capacidades para servicos modernos enquanto o monolito continua atendendo dominios nao migrados.

## Comparacoes criticas

| Decisao | Escolha provavel | Trade-off |
| --- | --- | --- |
| Rehost vs modernize | Rehost para prazo; modernize para valor arquitetural claro | Rehost mantem divida |
| Replatform vs refactor | Replatform reduz operacao; refactor muda desenho | Refactor custa mais |
| Sincrono vs assincrono | Assincrono para picos, retry e consumidores independentes | Consistencia eventual |
| SQS vs EventBridge | SQS para fila/buffer; EventBridge para eventos e roteamento | Modelos diferentes |
| Lambda vs containers | Lambda para eventos curtos; containers para runtime customizado | Operacao e limites |
| ECS vs EKS | ECS/Fargate para menor operacao; EKS para maturidade Kubernetes | EKS exige plataforma |
| Big-bang vs strangler | Strangler reduz risco incrementalmente | Convivencia temporaria |

## Matriz de modernizacao

| Cenario | Estrategia | Tecnologia possivel | Beneficio | Trade-off |
| --- | --- | --- | --- | --- |
| App estavel com deadline | Rehost/replatform | EC2, RDS, ECS | Menor risco | Divida continua |
| API stateless | Refactor parcial | Lambda ou Fargate | Escala independente | Observabilidade distribuida |
| Eventos independentes | Decoupling | SQS/EventBridge | Absorve picos | Consistencia eventual |
| Kubernetes maduro | Plataforma container | EKS | Ecossistema | Operacao complexa |
| Time pequeno | Gerenciado | Lambda/Fargate | Menos toil | Limites do servico |
| Monolito acoplado | Strangler | API layer + servicos | Migra por dominio | Convivencia |
| Batch | Replatform/refactor | ECS tasks, Batch, Lambda | Escala sob demanda | Idempotencia |
| Dominio muda rapido | Refactor seletivo | Servicos por capacidade | Time-to-market | Custo de design |

## Estudos Complementares

- Associate e util apenas para fundamentos de Lambda, ECS, EKS, Fargate, SQS, SNS e EventBridge.
- AI Practitioner nao permanece neste modulo porque nao ha exemplo real de Bedrock, IA generativa ou workload AI/ML.
- O foco Professional e selecionar caminho de modernizacao conforme negocio e operacao.

## Arquivos do modulo

- [Questoes](questoes.md)
- [Flashcards](flashcards.md)
- [Cheatsheet](cheatsheet.md)
- [Casos de uso](casos-de-uso.md)
- [Referencias oficiais](links.md)
- [Workshop de modernizacao](lab.md)

---

CloudStudy - Trilha AWS Solutions Architect Professional
---

## Acompanhe a CloudStudy

Estamos construindo uma plataforma para ajudar brasileiros a estudarem AWS de forma mais pratica, organizada e acessivel.

- Plataforma: [CloudStudy](https://cloudstudy.com.br)
- Instagram: [cloudstudy.ai](https://www.instagram.com/cloudstudy.ai/)
- LinkedIn: [CloudStudy](https://www.linkedin.com/company/cloudstudy-ai/)

---

## Outras trilhas AWS em portugues

- [AWS Solutions Architect Associate](https://github.com/Thiago-code-lab/aws-certified-solutions-architect-associate-brasil)
- [AWS Cloud Practitioner](https://github.com/Thiago-code-lab/aws-certified-cloud-practitioner-brasil)
- [AWS AI Practitioner](https://github.com/Thiago-code-lab/aws-certified-ai-practitioner-brasil)

---

> Continue sua preparacao para certificacoes AWS na [CloudStudy](https://cloudstudy.com.br).
