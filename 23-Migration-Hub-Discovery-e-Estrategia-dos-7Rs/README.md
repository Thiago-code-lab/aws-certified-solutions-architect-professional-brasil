# Migration Hub, Discovery e Estratégia dos 7Rs

## Visão Geral

Este módulo cobre assessment, portfólio, ondas de migração, TCO e escolha de estratégia, com foco no tipo de raciocínio arquitetural exigido no AWS Certified Solutions Architect Professional (SAP-C02).

## Conceitos-Chave

- Domínio predominante: Migration and Modernization.
- Serviços e padrões principais: Migration Hub, Application Discovery Service, Control Tower.
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

Use documentacao oficial de Migration Hub, Application Discovery Service e AWS Prescriptive Guidance para validar assessment, discovery e criterios de escolha dos 7Rs.

---

## ☁️ Acompanhe a CloudStudy

Estamos construindo uma plataforma para ajudar brasileiros a estudarem AWS de forma mais prática, organizada e acessível.

Siga a CloudStudy para acompanhar novos materiais, atualizações e conteúdos sobre certificações AWS:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

