# Cheatsheet - Identidade e Cross-Account

| Sinal no cenario | Escolha provavel | Por que | Trade-off | Armadilha |
| --- | --- | --- | --- | --- |
| Funcionarios acessam muitas contas | IAM Identity Center + IdP | Centraliza autenticacao, grupos e permission sets | Exige governanca de atribuicoes | Criar usuarios IAM por conta |
| Workload precisa chamar AWS | IAM role de servico | Credenciais temporarias e integracao nativa | Requer policies bem escopadas | Gravar access key em codigo |
| Terceiro acessa uma conta por tempo limitado | Cross-account role + STS | Sessao temporaria e auditavel | Trust policy deve ser precisa | Criar IAM user para vendor |
| Time cria roles, mas deve respeitar limite maximo | Permissions boundary | Limita entidade IAM especifica | Nao governa toda a conta | Confundir com SCP |
| OU produtiva nao pode executar acoes proibidas | SCP | Limite maximo da conta/OU | Pode quebrar automacoes | Achar que SCP concede acesso |
| Bucket precisa permitir leitura por outra conta | Resource-based policy ou role cross-account | Autoriza recurso/principal correto | Exige cuidado com principals e condicoes | Abrir para conta inteira sem restricao |
| Role so pode ser assumida por um principal | Trust policy | Define relacao de confianca | Nao define permissoes de uso | Colocar acoes de servico na trust policy |
| Pipeline precisa deploy em outra conta | Role assumida pelo pipeline | Evita usuarios duplicados e melhora auditoria | Requer segregacao por ambiente | Usar mesma role para dev e prod |

## Ordem mental de autorizacao

1. O principal foi autenticado?
2. Ele pode assumir a role ou obter a sessao?
3. A identity policy permite a acao?
4. Alguma resource policy participa?
5. Existe explicit deny?
6. SCP ou permissions boundary limitam o resultado?
7. Condicoes como MFA, tag, IP, principal org ou external ID sao atendidas?

## Sinais de prova

- "corporate IdP", "workforce", "multi-account" -> Identity Center.
- "temporary access", "another account", "vendor" -> STS AssumeRole.
- "maximum permission for created roles" -> permissions boundary.
- "deny across OU" -> SCP.
- "who can assume" -> trust policy.
- "what can do" -> permission policy.
