# 03 - IAM, Identity Center, Federacao e Cross-Account

Este modulo aprofunda arquitetura de identidade em escala organizacional. No SAP-C02, identidade nao e apenas "dar permissao": e escolher a camada correta para autenticar pessoas, autorizar workloads, reduzir credenciais de longo prazo, delegar acesso entre contas e impor limites sem travar a operacao.

## Objetivos

- Diferenciar IAM users, IAM roles, credenciais temporarias, AWS STS e IAM Identity Center.
- Projetar acesso workforce multi-account com IdP corporativo, permission sets e menor privilegio.
- Desenhar acesso cross-account para times internos, vendors, pipelines e servicos.
- Separar trust policy, permission policy, resource-based policy, SCP e permissions boundary.
- Reduzir credenciais estaticas e definir conceitos de break-glass auditavel.

## Qual camada resolve qual problema?

| Problema | Camada principal | Observacao Professional |
| --- | --- | --- |
| Pessoas acessando muitas contas | IAM Identity Center + IdP externo | Centraliza lifecycle, MFA, grupos e permission sets |
| Workload AWS acessando recurso AWS | IAM role de servico | Evita chaves estaticas em instancia, container ou funcao |
| Acesso temporario entre contas | IAM role + STS AssumeRole | Trust policy define quem pode assumir; permission policy define o que pode fazer |
| Limite organizacional por conta/OU | SCP | Nao concede acesso; limita o maximo permitido |
| Limite para roles criadas por equipes | Permissions boundary | Controla o maximo de uma entidade IAM especifica |
| Acesso direto a um recurso compartilhado | Resource-based policy | Util para S3, KMS, SQS, Lambda e outros servicos que suportam policy no recurso |

## Comparacoes criticas

| Comparacao | Decisao |
| --- | --- |
| IAM user vs IAM role | Use users apenas quando inevitavel; roles com credenciais temporarias reduzem risco operacional |
| IAM role vs permission set | Role e entidade assumida em uma conta; permission set e modelo do Identity Center que provisiona permissoes nas contas atribuídas |
| Permission policy vs trust policy | Permission policy diz o que a role pode fazer; trust policy diz quem pode assumir a role |
| Identity-based vs resource-based policy | Identity-based acompanha o principal; resource-based fica no recurso e pode permitir principals externos |
| Permissions boundary vs SCP | Boundary limita entidade IAM; SCP limita conta/OU inteira |
| Credencial longa vs temporaria | Credencial temporaria expira e deve ser preferida para acesso humano e de workloads |
| Cross-account role vs usuarios duplicados | Role centraliza governanca e auditoria; usuarios duplicados espalham lifecycle e segredo |

## Exemplo multi-account

```text
Corporate IdP
     |
     v
IAM Identity Center
     |
     +---- Production Account
     |       +-- ReadOnly permission set
     |       +-- Admin permission set with approval
     |
     +---- Development Account
     |       +-- Developer permission set
     |
     +---- Security Account
             +-- SecurityAudit permission set
```

Fluxo:

1. O usuario autentica no IdP corporativo com MFA e politicas de ciclo de vida da empresa.
2. O IdP federa para IAM Identity Center usando SAML/OIDC conforme integracao.
3. O Identity Center avalia grupos e atribuicoes de contas.
4. O usuario escolhe conta e permission set autorizado.
5. A AWS entrega credenciais temporarias para a role provisionada na conta alvo.
6. IAM policies, SCPs, boundaries e resource policies ainda participam da decisao final de autorizacao.

## Raciocinio SAP-C02

### Cenario 1: cem contas e IdP corporativo

- Cenario: colaboradores entram e saem frequentemente; grupos ja existem no diretorio corporativo.
- Restricoes: MFA central, acesso multi-account e revogacao rapida.
- Sinal arquitetural: problema de workforce federation, nao de usuarios IAM locais.
- Opcoes: IAM users replicados, roles manuais por conta, ou Identity Center com permission sets.
- Melhor decisao: IAM Identity Center integrado ao IdP, grupos corporativos e permission sets por funcao/ambiente.
- Trade-off: exige governanca de atribuicoes e desenho de permission sets, mas reduz credenciais longas e operacao por conta.
- Por que nao alternativas: usuarios duplicados quebram lifecycle; roles manuais sem Identity Center aumentam manutencao.

### Cenario 2: vendor com acesso temporario a uma conta

- Cenario: fornecedor precisa diagnosticar uma aplicacao por duas semanas.
- Restricoes: acesso limitado, auditavel, sem usuario permanente.
- Sinal arquitetural: acesso cross-account temporario com escopo estrito.
- Melhor decisao: IAM role na conta workload com trust policy para principal aprovado, external ID se aplicavel, MFA/condicoes e permission policy minima.
- Trade-off: requer configuracao cuidadosa de trust e expiração operacional do acordo.
- Por que nao alternativas: criar IAM user para vendor deixa credencial longa; compartilhar usuario interno viola rastreabilidade.

### Cenario 3: seguranca precisa leitura em todas as contas

- Cenario: SOC precisa investigar findings sem administrar workloads.
- Restricoes: acesso amplo em contas, mas somente leitura e auditoria.
- Melhor decisao: permission set SecurityAudit via Identity Center para equipe humana e roles/administrador delegado para servicos organizacionais.
- Trade-off: precisa separar acesso humano, integracao de servicos e SCPs para impedir mudancas indevidas.

### Cenario 4: dev diferente de prod

- Cenario: desenvolvedores podem administrar dev, mas apenas ler prod.
- Restricoes: reduzir risco de mudanca acidental em producao.
- Melhor decisao: permission sets distintos por ambiente e grupos separados; SCPs de prod podem bloquear acoes proibidas.
- Trade-off: mais atribuicoes para manter, mas menor blast radius.

### Cenario 5: eliminacao de access keys

- Cenario: auditoria encontrou access keys antigas em repositorios e notebooks.
- Restricoes: workloads precisam continuar acessando AWS.
- Melhor decisao: substituir chaves por roles de instancia, task roles, Lambda execution roles, IAM Roles Anywhere ou federacao conforme origem.
- Trade-off: migracao exige inventario e ajuste de aplicacoes, mas reduz segredo persistente.

## Estudos Complementares

Use a trilha Associate apenas para revisar fundamentos de IAM, roles, policies e MFA antes de estudar decisoes multi-account e federacao neste modulo:

https://github.com/Thiago-code-lab/aws-certified-solutions-architect-associate-brasil

## Arquivos do modulo

- [Questoes](questoes.md)
- [Flashcards](flashcards.md)
- [Cheatsheet](cheatsheet.md)
- [Casos de uso](casos-de-uso.md)
- [Links oficiais](links.md)

---

CloudStudy - Trilha AWS Solutions Architect Professional
