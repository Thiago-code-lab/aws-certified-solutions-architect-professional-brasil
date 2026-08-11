# 19 - Seguranca: KMS, Secrets, GuardDuty e Security Hub

Este modulo aprofunda arquitetura de seguranca centralizada em ambientes AWS multi-account. O foco Professional e entender como criptografia, segredos, deteccao, agregacao, compliance e resposta trabalham juntos, nao decorar a funcao isolada de cada servico.

## Objetivos

- Projetar uma conta de seguranca central com administradores delegados.
- Diferenciar AWS KMS key policies, IAM policies e uso cross-account de chaves.
- Posicionar Secrets Manager, Parameter Store, GuardDuty, Security Hub, Inspector, Macie, AWS Config e CloudTrail.
- Entender deteccao, agregacao, compliance evaluation e remediacao automatizada.
- Criar governanca de criptografia e findings em escala organizacional.

## Arquitetura de referencia

```text
AWS Organization
      |
      +---- Security Account
      |       +-- Security Hub administrator
      |       +-- GuardDuty delegated admin
      |       +-- Inspector delegated admin
      |       +-- central findings / automation
      |
      +---- Log Archive Account
      |       +-- CloudTrail organization trails
      |       +-- Config snapshots / immutable logs
      |
      +---- Workload Accounts
              +-- GuardDuty detectors
              +-- Config recorders
              +-- Inspector scans
              +-- KMS customer managed keys
              +-- Secrets Manager secrets
```

Fluxo:

1. Organizations habilita integracoes em escala.
2. A conta de seguranca opera como delegated administrator para servicos suportados.
3. Workload accounts geram findings e configuracoes.
4. Security Hub agrega, normaliza e correlaciona findings.
5. CloudTrail e Config preservam trilha e estado para investigacao.
6. EventBridge/Systems Manager/Lambda podem acionar remediacao controlada.

## Comparacoes criticas

| Comparacao | Decisao Professional |
| --- | --- |
| KMS key policy vs IAM policy | Key policy e autoridade primaria da chave; IAM pode complementar se permitido pela key policy |
| Secrets Manager vs Parameter Store | Secrets Manager favorece rotacao e segredos sensiveis; Parameter Store serve configuracao e parametros, com SecureString quando adequado |
| GuardDuty vs Security Hub | GuardDuty detecta ameacas; Security Hub agrega findings e checks de seguranca |
| Security Hub vs AWS Config | Security Hub agrega postura/finding; Config avalia estado de recursos contra regras |
| GuardDuty vs Inspector | GuardDuty detecta comportamento/anomalia; Inspector avalia vulnerabilidades em workloads suportados |
| Macie vs GuardDuty | Macie descobre dados sensiveis em S3; GuardDuty detecta atividade suspeita |
| Detection vs aggregation vs compliance vs remediation | Cada etapa e separada; automatizar sem contexto pode causar indisponibilidade |

## Raciocinio SAP-C02

### Cenario 1: empresa regulada com centenas de contas

- Cenario: auditoria exige visibilidade central, criptografia governada e trilha imutavel.
- Restricoes: times de workload continuam autonomos; seguranca nao deve operar na management account.
- Sinal: governanca organizacional e delegated administrator.
- Melhor decisao: Security Account como administrador delegado para GuardDuty, Security Hub, Inspector/Config quando aplicavel, Log Archive separado para CloudTrail e logs.
- Trade-off: mais desenho multi-account e automacao, mas menor risco operacional e melhor segregacao.
- Por que nao alternativas: habilitar manualmente por conta nao escala; usar management account como operacional aumenta risco.

### Cenario 2: credencial vazada

- Cenario: access key aparece em repositorio publico e atividade anomala surge em uma conta.
- Restricoes: detectar rapidamente, correlacionar findings e conter dano.
- Sinal: deteccao comportamental + agregacao + resposta.
- Melhor decisao: GuardDuty para deteccao, Security Hub para agregacao, CloudTrail para investigacao e automacao controlada para desativar chave ou isolar principal.
- Trade-off: remediacao automatica deve ter guardrails para evitar impacto indevido.

### Cenario 3: governanca de chaves

- Cenario: dados regulados devem ser criptografados com chaves controladas e uso cross-account restrito.
- Restricoes: workloads em contas diferentes precisam usar chaves sem abrir administracao da key.
- Melhor decisao: customer managed keys, key policies explicitas, IAM complementar, grants quando apropriado e SCP/Config para governanca.
- Trade-off: key policy mal desenhada pode bloquear recuperacao ou abrir uso indevido.

## Estudos Complementares

Use a trilha Associate apenas para revisar fundamentos de IAM, KMS, CloudTrail e seguranca basica antes de aprofundar arquitetura centralizada neste modulo:

https://github.com/Thiago-code-lab/aws-certified-solutions-architect-associate-brasil

## Arquivos do modulo

- [Questoes](questoes.md)
- [Flashcards](flashcards.md)
- [Cheatsheet](cheatsheet.md)
- [Casos de uso](casos-de-uso.md)
- [Links oficiais](links.md)

---

CloudStudy - Trilha AWS Solutions Architect Professional
