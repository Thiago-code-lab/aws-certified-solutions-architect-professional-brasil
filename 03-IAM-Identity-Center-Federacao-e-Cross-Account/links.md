# Links Oficiais - IAM, Identity Center e Cross-Account

## Essencial

- [AWS IAM User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) - Base para policies, roles e avaliacao de permissoes; leia para consolidar a linguagem usada no SAP-C02.
- [IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) - Prioridade alta para entender credenciais temporarias, service roles e cross-account roles.
- [IAM Identity Center User Guide](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html) - Fonte principal para acesso workforce multi-account com permission sets.
- [AWS STS](https://docs.aws.amazon.com/STS/latest/APIReference/welcome.html) - Referencia para AssumeRole e credenciais temporarias.

## Aprofundamento

- [IAM policy evaluation logic](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html) - Essencial para raciocinar SCP, boundaries, identity policies e resource policies juntas.
- [Permissions boundaries](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html) - Ajuda a diferenciar limites de entidade IAM de limites organizacionais.
- [IAM roles terms and concepts](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html) - Reforca trust policy, principals e sessoes.

## Referencia

- [IAM JSON policy elements](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html) - Use para validar Condition, Principal, Action e Resource.
- [AWS Organizations SCPs](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) - Use quando o cenario envolve limites por OU/conta.
- [IAM Identity Center permission sets](https://docs.aws.amazon.com/singlesignon/latest/userguide/permissionsetsconcept.html) - Leitura direta para atribuicoes multi-account.
