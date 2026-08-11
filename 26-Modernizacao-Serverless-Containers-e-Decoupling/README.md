# Modernização: Serverless, Containers e Decoupling

## Visão Geral

Este módulo cobre refatoração progressiva, desacoplamento, eventos, containers e serverless em sistemas legados, com foco no tipo de raciocínio arquitetural exigido no AWS Certified Solutions Architect Professional (SAP-C02).

## Conceitos-Chave

- Domínio predominante: Migration and Modernization.
- Serviços e padrões principais: Lambda, ECS, EKS, Fargate, SQS, SNS, EventBridge.
- Decisão orientada por requisitos de negócio, risco operacional, segurança, resiliência, performance e custo.
- Avaliação de impactos em ambientes multi-conta, multi-Region, híbridos ou em migração quando aplicável.

## Relevância para o SAP-C02

O SAP-C02 cobra cenários com múltiplas restrições e alternativas tecnicamente válidas. O objetivo aqui é treinar por que uma arquitetura é preferível, quando outra opção se torna melhor e quais detalhes do enunciado mudam a decisão.

## Decisões Arquiteturais

- Identificar o requisito dominante antes de escolher serviços.
- Validar dependências entre contas, redes, dados, identidade e operação.
- Preferir serviços gerenciados quando reduzem risco sem violar requisitos explícitos.
- Documentar exceções quando controle, latência, compliance ou custo justificarem maior complexidade.

## Trade-offs

- Menor operação versus maior controle.
- Resiliência multi-AZ versus multi-Region e seu impacto em custo e complexidade.
- Centralização de governança versus autonomia de times e contas.
- Otimização de custo versus requisitos de desempenho, recuperação e segurança.

## Cenários de Prova

- Organizações com múltiplas contas e times independentes.
- Ambientes híbridos com conectividade, DNS e segurança centralizados.
- Workloads com requisitos conflitantes de RTO/RPO, compliance, custo e latência.
- Migração ou modernização gradual sem indisponibilidade significativa.

## Armadilhas Comuns

- Escolher serviço por reconhecimento de nome, sem validar a restrição principal.
- Resolver um problema organizacional com uma configuração local de uma única conta.
- Ignorar operação contínua, automação, rastreabilidade e governança.
- Escolher a arquitetura mais completa quando a pergunta pede menor esforço operacional ou menor custo.

## Próximo Passo de Revisão

1. Leia cheatsheet.md para consolidar critérios de decisão.
2. Use casos-de-uso.md para treinar análise de cenários.
3. Resolva questoes.md sem consulta e registre padrões de erro no módulo 30.
4. Consulte links.md para validar detalhes em documentação oficial.

## Estudos Complementares

Para revisar Lambda, ECS/EKS, SQS, SNS e EventBridge antes de aprofundar modernização com serverless, containers e desacoplamento:

https://github.com/Thiago-code-lab/aws-certified-solutions-architect-associate-brasil

Se a modernização envolver Amazon Bedrock, IA generativa ou workloads de IA na AWS:

https://github.com/Thiago-code-lab/aws-certified-ai-practitioner-brasil

---

## ☁️ Acompanhe a CloudStudy

Estamos construindo uma plataforma para ajudar brasileiros a estudarem AWS de forma mais prática, organizada e acessível.

Siga a CloudStudy para acompanhar novos materiais, atualizações e conteúdos sobre certificações AWS:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

