# Cheatsheet - Seguranca Centralizada

| Sinal no cenario | Escolha provavel | Por que | Trade-off | Armadilha |
| --- | --- | --- | --- | --- |
| SOC central para muitas contas | Security Account + delegated admin | Opera servicos em escala | Exige Organizations bem configurado | Usar management account diariamente |
| Logs imutaveis e auditoria | Log Archive Account + CloudTrail org trail | Evidencia fora das contas de workload | Mais controle de acesso | Guardar logs na mesma conta da app |
| Credencial comprometida | GuardDuty + CloudTrail + Security Hub | Detecta, investiga e agrega | Remediacao precisa contexto | Achar que Security Hub detecta tudo sozinho |
| Vulnerabilidades em EC2/container | Inspector | Avalia CVEs e exposicao suportada | Precisa triagem | Confundir com GuardDuty |
| Dados sensiveis em S3 | Macie | Descobre/classifica dados | Custo por analise | Usar GuardDuty para classificacao |
| Compliance de configuracao | AWS Config rules | Avalia estado de recursos | Pode gerar muito finding | Confundir com remediacao automatica |
| Segredo com rotacao | Secrets Manager | Rotacao e integracoes | Custo maior | Colocar segredo em texto plano |
| Configuracao simples | Parameter Store | Hierarquia e baixo overhead | Menos recursos de rotacao | Usar para tudo sem criterio |
| Uso cross-account de chave | KMS key policy + IAM | Key policy precisa permitir | Politica complexa | Achar que IAM sempre basta |

## Camadas de seguranca

| Camada | Servicos tipicos |
| --- | --- |
| Criptografia | KMS, ACM, encryption at rest |
| Segredos | Secrets Manager, Parameter Store |
| Deteccao | GuardDuty |
| Vulnerabilidade | Inspector |
| Dados sensiveis | Macie |
| Compliance/estado | AWS Config |
| Agregacao | Security Hub |
| Evidencia | CloudTrail, logs centralizados |
| Resposta | EventBridge, Systems Manager, Lambda |
