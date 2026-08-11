# Organizations, Control Tower e Multi-Account

## Visão Geral

No SAP-C02, multi-account não é um detalhe administrativo. É uma decisão arquitetural para reduzir blast radius, separar responsabilidades, aplicar governança centralizada e viabilizar crescimento organizacional sem transformar uma conta AWS em um monolito operacional.

Este módulo trata de como desenhar uma estrutura de contas com AWS Organizations, AWS Control Tower, OUs, SCPs, administradores delegados, logging centralizado e contas compartilhadas. A pergunta central não é “como criar uma conta?”, mas “qual desenho de organização reduz risco e ainda permite autonomia para times diferentes?”.

## Conceitos-Chave

- **AWS Organizations:** base para agrupar contas, aplicar SCPs, consolidar billing e habilitar integrações organizacionais.
- **AWS Control Tower:** acelera a criação de landing zone com Account Factory, guardrails, contas essenciais e governança inicial.
- **Organizational Units (OUs):** agrupam contas por função, criticidade, ambiente, unidade de negócio ou requisitos regulatórios.
- **SCPs:** definem limites máximos de permissão para contas/OUs; não concedem acesso por si só.
- **Delegated administrator:** permite que serviços como GuardDuty, Security Hub, Config e Firewall Manager sejam administrados por contas especializadas.
- **Contas compartilhadas:** normalmente incluem management, log archive, audit/security, networking/shared services e workloads.
- **Centralized logging:** CloudTrail, Config, VPC Flow Logs e logs de serviços enviados para uma conta de log imutável.

## Relevância para o SAP-C02

O exame frequentemente descreve empresas com múltiplas unidades de negócio, workloads regulados, aquisições, times independentes ou necessidade de padronizar contas. A resposta correta tende a combinar Organizations, OUs, SCPs, Control Tower, logging centralizado e administradores delegados, em vez de resolver tudo com IAM local em uma única conta.

## Estrutura multi-account de exemplo

```text
Root
├── Security OU
│   ├── Audit account
│   └── Log archive account
├── Infrastructure OU
│   ├── Network account
│   └── Shared services account
├── Workloads OU
│   ├── Prod app account
│   ├── Non-prod app account
│   └── Data platform account
├── Sandbox OU
│   └── Experiment accounts
└── Suspended OU
    └── Closed or quarantined accounts
```

Esse desenho separa segurança, rede, serviços compartilhados e workloads. Em cenários regulados, uma OU adicional pode existir para workloads com requisitos específicos, como dados sensíveis, residência de dados ou aprovação manual de mudanças.

## Decisões Arquiteturais

| Cenário | Decisão preferida | Trade-off |
|---|---|---|
| Empresa começando landing zone do zero | Control Tower com Account Factory e guardrails | Menos flexibilidade inicial, mais velocidade e consistência |
| Organização grande já operando Organizations | Evoluir OUs, SCPs e delegated admins sem refazer tudo | Exige governança incremental e cuidado com impacto em contas existentes |
| Times independentes com workloads críticos | Separar contas por ambiente e domínio de negócio | Mais contas para operar, menor blast radius |
| Segurança precisa investigar todas as contas | Delegar GuardDuty/Security Hub/Config para conta de segurança | Exige integração organizacional correta e permissões bem definidas |
| Bloquear ações proibidas em toda uma OU | SCP na OU ou conta | Pode quebrar automações se aplicado sem teste |

## Organizations vs Control Tower

| Escolha | Quando usar | Quando evitar |
|---|---|---|
| AWS Organizations | Você precisa da base de contas, OUs, SCPs, billing consolidado e integrações organizacionais | Quando a empresa quer uma landing zone padronizada rapidamente e ainda não tem governança madura |
| AWS Control Tower | Você quer landing zone prescritiva, Account Factory, guardrails e baseline inicial consistente | Quando há customizações profundas que conflitam com a opinião operacional do Control Tower |

Control Tower usa Organizations por baixo. A decisão não é “um ou outro” em termos absolutos; normalmente é “usar Organizations diretamente” ou “usar Control Tower como camada de governança e provisionamento sobre Organizations”.

## SCP vs IAM Policy vs Permissions Boundary

| Mecanismo | O que faz | Armadilha comum |
|---|---|---|
| SCP | Define o máximo permitido para contas/OUs | Não concede permissão; apenas limita |
| IAM policy | Concede ou nega ações para usuários, grupos ou roles | Não impede outra role de ter permissão se não houver limite organizacional |
| Permissions boundary | Define o máximo permitido para uma entidade IAM específica | Não substitui SCP para governança de conta/OUs |

## Cenários de Prova

- Uma empresa adquiriu outra e precisa integrar contas sem misturar logs e permissões.
- Uma unidade de negócio quer autonomia para deploy, mas segurança exige trilha de auditoria central.
- Um time de sandbox cria recursos caros ou públicos; a organização precisa limitar ações sem travar produção.
- Várias contas precisam habilitar GuardDuty, Security Hub e Config de forma centralizada.
- Workloads regulados devem ficar separados de workloads comuns por requisitos de auditoria.

## Armadilhas Comuns

- Usar apenas IAM quando o requisito é controle organizacional.
- Aplicar SCP restritiva direto em produção sem testar em OU piloto.
- Colocar workloads na management account.
- Tratar conta de log como conta operacional comum.
- Criar OUs por organograma instável em vez de função, risco, ambiente ou governança.
- Confundir delegated administrator com acesso administrativo irrestrito.

## Próximo Passo de Revisão

1. Revise `cheatsheet.md` para fixar decisões entre Organizations, Control Tower, SCP, IAM e boundaries.
2. Estude `casos-de-uso.md` e tente desenhar a árvore de OUs antes de ler a decisão recomendada.
3. Resolva `questoes.md` prestando atenção a blast radius, auditoria, autonomia de times e governança.
4. Consulte `links.md` para validar limites, comportamento de SCPs e recursos atuais do Control Tower.

## Estudos Complementares

Se você ainda precisa reforçar fundamentos de IAM, Organizations e governança básica antes de desenhar uma landing zone Professional, revise a trilha Associate de forma pontual:

https://github.com/Thiago-code-lab/aws-certified-solutions-architect-associate-brasil

---

## ☁️ Acompanhe a CloudStudy

Estamos construindo uma plataforma para ajudar brasileiros a estudarem AWS de forma mais prática, organizada e acessível.

Siga a CloudStudy para acompanhar novos materiais, atualizações e conteúdos sobre certificações AWS:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/
