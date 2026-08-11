# Cheatsheet — Multi-Account e Landing Zone

## Decisões rápidas

| Sinal do cenário | Arquitetura preferida | Por quê | Trade-off | Armadilha |
|---|---|---|---|---|
| Empresa sem landing zone | Control Tower | Baseline rápido, Account Factory e guardrails | Menos flexível que automação própria | Tratar Control Tower como serviço separado de Organizations |
| Várias unidades de negócio | OUs por função/risco/ambiente | Permite políticas e isolamento por grupo | Exige desenho de governança | Modelar OUs por organograma instável |
| Auditoria central obrigatória | Log archive + audit/security account | Logs protegidos fora das contas de workload | Mais contas e permissões cruzadas | Guardar logs apenas na conta da aplicação |
| Serviço de segurança em todas as contas | Delegated administrator | Operação central sem usar management account | Requer integração organizacional | Usar usuários IAM replicados |
| Bloquear ações proibidas | SCP na OU correta | Limite máximo preventivo | Pode quebrar automações | Aplicar direto na root sem teste |

## Organizations vs Control Tower

| Use | Quando |
|---|---|
| Organizations puro | Estrutura existente, automação própria ou necessidade de controle mais customizado |
| Control Tower | Landing zone inicial, criação padronizada de contas e guardrails prescritivos |

## SCP, IAM e Boundary

| Controle | Escopo | Concede acesso? |
|---|---|---|
| SCP | Conta/OU/organização | Não |
| IAM policy | Principal ou recurso | Sim, se não houver deny efetivo |
| Permissions boundary | Principal IAM | Não diretamente; limita máximo do principal |

## Checklist SAP-C02

- Existe separação entre management, security, log archive, network/shared services e workloads?
- A OU reflete governança real ou apenas organograma?
- O serviço centralizado suporta delegated administrator?
- A SCP foi testada antes de atingir produção?
- Logs críticos ficam fora da conta que gera o evento?
