# Casos de Uso - Seguranca Centralizada

## Cenario 1 - Empresa regulada com centenas de contas

### Contexto

Uma instituicao financeira opera centenas de contas e precisa demonstrar trilha de auditoria, postura de seguranca e criptografia consistente.

### Requisitos

- SOC central.
- Logs protegidos.
- Findings agregados.
- Workloads com autonomia controlada.

### Arquitetura recomendada

Security Account como delegated administrator para GuardDuty, Security Hub e Inspector; Log Archive Account para CloudTrail e logs; AWS Config em contas de workload.

### Por que

Separa operacao de seguranca, evidencia e workloads, reduzindo blast radius e melhorando governanca.

### Trade-offs

Exige padronizacao organizacional, onboarding de contas e tratamento de findings em escala.

### Por que nao as alternativas

Habilitar servicos manualmente nao escala; operar na management account aumenta risco; usuarios do SOC em cada conta dificultam lifecycle.

### Sinal de prova

"hundreds of accounts", "central security team", "delegated administrator".

## Cenario 2 - Incidente de credencial vazada

### Contexto

Uma access key foi publicada em um repositorio e houve chamadas suspeitas a APIs AWS.

### Requisitos

- Detectar comportamento anomalo.
- Correlacionar findings.
- Investigar historico.
- Conter com menor impacto.

### Arquitetura recomendada

GuardDuty para deteccao, Security Hub para agregacao, CloudTrail para investigacao e automacao via EventBridge/Systems Manager para desativacao controlada.

### Por que

Cada servico cobre uma etapa diferente do fluxo de incidente.

### Trade-offs

Remediacao automatica precisa regras de severidade e excecoes para nao interromper workloads validos.

### Por que nao as alternativas

Macie nao detecta uso anomalo de credencial; KMS nao investiga chamadas API; backup nao contem credencial.

### Sinal de prova

"compromised credential", "anomalous API calls", "central findings".

## Cenario 3 - Governanca de criptografia e segredos

### Contexto

Aplicacoes em varias contas processam dados sensiveis e precisam usar chaves controladas e segredos rotacionados.

### Requisitos

- Customer managed keys.
- Uso cross-account restrito.
- Rotacao de segredos.
- Evidencia de compliance.

### Arquitetura recomendada

KMS customer managed keys com key policies explicitas, Secrets Manager para segredos com rotacao, AWS Config/Security Hub para postura e CloudTrail para auditoria.

### Por que

Criptografia, segredo, auditoria e compliance precisam ser tratados como camadas integradas.

### Trade-offs

Key policies complexas aumentam risco de lockout; rotacao exige compatibilidade da aplicacao.

### Por que nao as alternativas

IAM policy sem key policy pode nao autorizar KMS; Parameter Store pode ser insuficiente para rotacao complexa; SCP nao substitui politica de chave.

### Sinal de prova

"cross-account KMS", "secret rotation", "regulated data".
