# 26 - Modernization: Serverless, Containers and Decoupling

This module approaches modernization as incremental change. The goal is to decide how to evolve legacy workloads without a high-risk rewrite, reduce coupling and improve delivery speed. Understanding Lambda, ECS or EKS individually is only part of that decision.

## Objectives

- Choose rehost, replatform or refactor according to deadlines, risk and value.
- Apply the strangler pattern to replace parts of a monolith gradually.
- Identify synchronous and asynchronous boundaries using SQS, SNS, EventBridge and Step Functions.
- Choose Lambda, ECS, EKS or Fargate according to operations, scale and team skills.
- Avoid unnecessary modernization when a smaller change resolves the constraint.

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

The routing layer sends new capabilities to modern services while the monolith continues to serve domains that have not migrated.

## Critical comparisons

| Decision | Likely choice | Trade-off |
| --- | --- | --- |
| Rehost vs modernize | Rehost for a deadline; modernize for clear architectural value | Rehosting retains technical debt |
| Replatform vs refactor | Replatform reduces operations; refactor changes the design | Refactoring costs more |
| Synchronous vs asynchronous | Asynchronous for peaks, retries and independent consumers | Eventual consistency |
| SQS vs EventBridge | SQS for queues and buffering; EventBridge for events and routing | Different delivery and consumption models |
| Lambda vs containers | Lambda for short event-driven tasks; containers for custom runtimes | Operations and service limits |
| ECS vs EKS | ECS/Fargate for lower operational effort; EKS for Kubernetes maturity | EKS requires platform expertise |
| Big bang vs strangler | Strangler reduces risk incrementally | Temporary coexistence |

## Modernization matrix

| Scenario | Strategy | Possible technology | Benefit | Trade-off |
| --- | --- | --- | --- | --- |
| Stable application with a deadline | Rehost/replatform | EC2, RDS, ECS | Lower change risk | Technical debt remains |
| Stateless API | Partial refactoring | Lambda or Fargate | Independent scaling | Distributed observability |
| Independent events | Decoupling | SQS/EventBridge | Absorbs peaks | Eventual consistency |
| Mature Kubernetes team | Container platform | EKS | Ecosystem | Complex operations |
| Small team | Managed services | Lambda/Fargate | Less toil | Service limits |
| Tightly coupled monolith | Strangler | API layer and services | Migration by domain | Coexistence |
| Batch processing | Replatform/refactor | ECS tasks, AWS Batch, Lambda | On-demand scaling | Idempotency |
| Rapidly changing domain | Selective refactoring | Services organized by capability | Time to market | Design cost |

## Additional learning

- The Associate path is useful here for the fundamentals of Lambda, ECS, EKS, Fargate, SQS, SNS and EventBridge.
- AI Practitioner is not included in this module because it contains no actual Bedrock, generative AI or AI/ML workload example.
- The Professional focus is selecting a modernization path based on business and operational requirements.

## Module files

- [Questions](questions.md)
- [Flashcards](flashcards.md)
- [Cheatsheet](cheatsheet.md)
- [Use cases](use-cases.md)
- [Official references](links.md)
- [Modernization workshop](lab.md)

---

CloudStudy - AWS Solutions Architect Professional Learning Path
---

## Follow CloudStudy

We are building a platform to help Brazilian learners study AWS in a more practical, organized and accessible way.

- Platform: [CloudStudy](https://cloudstudy.com.br)
- Instagram: [cloudstudy.ai](https://www.instagram.com/cloudstudy.ai/)
- LinkedIn: [CloudStudy](https://www.linkedin.com/company/cloudstudy-ai/)

---

## Additional AWS learning paths in English

- [AWS Solutions Architect Associate](https://github.com/Thiago-code-lab/aws-certified-solutions-architect-associate-brasil/tree/saa-c03-english)
- [AWS Cloud Practitioner](https://github.com/Thiago-code-lab/aws-certified-cloud-practitioner-brasil/tree/clf-c02-english)
- [AWS AI Practitioner](https://github.com/Thiago-code-lab/aws-certified-ai-practitioner-brasil/tree/aif-c01-english)

---

> Continue preparing for AWS certifications with [CloudStudy](https://cloudstudy.com.br).
