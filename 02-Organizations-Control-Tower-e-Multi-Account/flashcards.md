# Cartões de Revisão

## Card 01

**Pergunta:** Quando Control Tower é preferível a usar apenas Organizations?

<details><summary><strong>Ver resposta</strong></summary>

Quando a organização quer landing zone inicial, Account Factory, guardrails e baseline repetível sem construir toda a automação de governança do zero.

</details>

## Card 02

**Pergunta:** SCP concede permissão?

<details><summary><strong>Ver resposta</strong></summary>

Não. SCP define o limite máximo permitido para contas/OUs. A permissão ainda precisa vir de IAM identity policy, resource policy ou outro mecanismo compatível.

</details>

## Card 03

**Pergunta:** Quando separar workloads em contas diferentes?

<details><summary><strong>Ver resposta</strong></summary>

Quando há diferença de ambiente, criticidade, ownership, compliance, dados sensíveis, billing, risco operacional ou necessidade de reduzir blast radius.

</details>

## Card 04

**Pergunta:** Por que evitar workloads na management account?

<details><summary><strong>Ver resposta</strong></summary>

Porque a management account controla a organização. Workloads aumentam risco operacional, superfície de ataque e complexidade de auditoria.

</details>

## Card 05

**Pergunta:** Delegated administrator resolve qual problema?

<details><summary><strong>Ver resposta</strong></summary>

Permite operar serviços organizacionais em uma conta especializada, como segurança ou auditoria, sem usar a management account no dia a dia.

</details>

## Card 06

**Pergunta:** SCP vs permissions boundary: qual a diferença prática?

<details><summary><strong>Ver resposta</strong></summary>

SCP limita contas/OUs. Permissions boundary limita uma entidade IAM específica. Para governança organizacional, SCP é o mecanismo mais amplo.

</details>

## Card 07

**Pergunta:** O que deve ir em uma conta de log archive?

<details><summary><strong>Ver resposta</strong></summary>

Logs centralizados como CloudTrail, Config, VPC Flow Logs e logs de serviços, com acesso restrito e proteção contra alteração/exclusão.

</details>

## Card 08

**Pergunta:** Qual armadilha aparece em questões sobre OUs?

<details><summary><strong>Ver resposta</strong></summary>

Criar OUs apenas por organograma. Em prova, OUs geralmente devem refletir governança, ambiente, risco, compliance ou função operacional.

</details>

## Card 09

**Pergunta:** Quando aplicar uma SCP primeiro em OU piloto?

<details><summary><strong>Ver resposta</strong></summary>

Quando a SCP pode bloquear automações ou workloads existentes. Testar reduz risco antes de aplicar em OUs críticas.

</details>

## Card 10

**Pergunta:** O que caracteriza uma boa estrutura multi-account no SAP-C02?

<details><summary><strong>Ver resposta</strong></summary>

Isolamento por conta, logging centralizado, segurança delegada, OUs com políticas coerentes, billing consolidado e autonomia controlada para times.

</details>
