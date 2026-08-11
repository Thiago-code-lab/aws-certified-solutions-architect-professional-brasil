# Casos de Uso - Identidade e Cross-Account

## Cenario 1 - Workforce federation em empresa global

### Contexto

Uma empresa possui 100 contas AWS, IdP corporativo, MFA obrigatorio e times distribuidos por produto.

### Requisitos

- Acesso humano multi-account.
- Revogacao rapida quando alguem sai da empresa.
- Permissoes diferentes por ambiente.

### Arquitetura recomendada

IAM Identity Center integrado ao IdP, grupos corporativos mapeados para permission sets e atribuicoes por conta/OUs.

### Por que

O requisito principal e lifecycle centralizado de pessoas. Identity Center reduz usuarios locais e permite acesso temporario as contas.

### Trade-offs

Exige desenho cuidadoso de grupos, permission sets e processo de revisao de acesso.

### Por que nao as alternativas

IAM users por conta espalham credenciais; roles manuais sem Identity Center aumentam operacao; SCPs nao autenticam usuarios.

### Sinal de prova

"corporate identity provider", "many AWS accounts", "workforce access".

## Cenario 2 - Vendor temporario

### Contexto

Um fornecedor precisa acessar logs e metricas de uma aplicacao especifica por duas semanas.

### Requisitos

- Sem usuario permanente.
- Acesso somente leitura.
- Auditoria de sessoes.

### Arquitetura recomendada

IAM role cross-account com trust policy para principal do fornecedor, condicoes de seguranca e permission policy minima.

### Por que

STS entrega credenciais temporarias e CloudTrail registra a role assumida.

### Trade-offs

A trust policy precisa ser revisada para evitar principal amplo demais; o encerramento do acesso deve fazer parte do processo.

### Por que nao as alternativas

Access keys compartilhadas e usuarios IAM permanentes aumentam risco e reduzem rastreabilidade.

### Sinal de prova

"temporary vendor access", "one account", "auditability".

## Cenario 3 - Governanca de roles criadas por equipes

### Contexto

Equipes de plataforma criam roles para pipelines em contas de desenvolvimento.

### Requisitos

- Autonomia de criacao.
- Limite maximo aprovado por seguranca.
- Sem impedir toda a conta de operar.

### Arquitetura recomendada

Permissions boundary obrigatoria para roles criadas por automacao das equipes, combinada com SCPs apenas para denies organizacionais criticos.

### Por que

Boundary limita entidades especificas; SCP seria amplo demais para esse controle fino.

### Trade-offs

Exige enforcement no processo de criacao e revisao continua das boundaries.

### Por que nao as alternativas

SCP na OU inteira pode bloquear casos validos; confiar apenas em revisao manual nao escala.

### Sinal de prova

"teams can create roles but must not exceed maximum permissions".
