# ECS EKS Fargate e Containers

## Visao geral

Este modulo resume o tema ECS EKS Fargate e Containers para a certificacao AWS Certified Solutions Architect Professional (SAP-C02). O foco e reconhecer sinais de arquitetura em cenarios longos e escolher a alternativa que equilibra seguranca, confiabilidade, performance, custo e operacao.

## Conceitos centrais

- Identificar a restricao dominante antes de comparar servicos.
- Validar impacto de identidade, rede, dados, automacao, observabilidade e governanca.
- Preferir servicos gerenciados quando reduzem operacao sem violar requisitos.
- Confirmar limites e comportamento na documentacao oficial.

## Decisao arquitetural

Use este tema quando o cenario pedir uma decisao sustentavel e verificavel. Em SAP-C02, a melhor resposta geralmente nao e a arquitetura mais sofisticada, mas a que atende os requisitos explicitos com menor risco operacional.

## Sinais de prova

1. Requisitos de multi-account, auditoria, RTO/RPO, latencia ou custo mudam a prioridade da solucao.
2. Alternativas tecnicamente validas devem ser comparadas por trade-off e risco.
3. Automacao, rollback e observabilidade contam como parte da arquitetura.
4. O enunciado costuma eliminar solucoes excessivas ou manuais demais.

## Armadilhas comuns

- Escolher um recurso avancado sem necessidade descrita.
- Ignorar limites de servico, falha parcial ou modelo de consistencia.
- Resolver seguranca sem menor privilegio, auditoria e controles verificaveis.
- Confundir migracao, modernizacao e melhoria continua.

## Navegacao

- Modulo anterior: [Lambda API Gateway e Arquiteturas Serverless](../15-Lambda-API-Gateway-e-Arquiteturas-Serverless/README.md)
- Revise tambem: [questoes](./questoes.md), [flashcards](./flashcards.md), [cheatsheet](./cheatsheet.md), [casos de uso](./casos-de-uso.md) e [links recomendados](./links.md).
- Proximo modulo: [CloudFormation CICD e Estrategias de Deployment](../17-CloudFormation-CICD-e-Estrategias-de-Deployment/README.md)

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
