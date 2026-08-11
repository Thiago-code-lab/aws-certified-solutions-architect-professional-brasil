# QuestÃµes de RevisÃ£o

## QuestÃ£o 1

Uma empresa global usa uma Ãºnica conta AWS para produÃ§Ã£o, homologaÃ§Ã£o e dados compartilhados. O time de seguranÃ§a precisa trilha de auditoria imutÃ¡vel e os times de produto precisam autonomia para deploy. Qual desenho Ã© mais adequado?

A) Manter uma conta Ãºnica e criar grupos IAM por time.
B) Separar contas por funÃ§Ã£o/ambiente, criar conta de log archive, conta de auditoria e aplicar OUs com SCPs.
C) Criar uma VPC por aplicaÃ§Ã£o dentro da mesma conta e ativar CloudTrail local.
D) Usar apenas permissions boundaries para todos os usuÃ¡rios IAM.

<details>
<summary><strong>Ver resposta</strong></summary>

âœ… **Resposta correta:** B

**ExplicaÃ§Ã£o:** O requisito Ã© organizacional: blast radius, auditoria central e autonomia por time. IAM local ou VPCs nÃ£o resolvem isolamento de conta nem logging central imutÃ¡vel.

</details>

## QuestÃ£o 2

Uma organizaÃ§Ã£o quer impedir que contas de sandbox criem instÃ¢ncias GPU e desativem CloudTrail. As contas de produÃ§Ã£o nÃ£o devem ser afetadas. Qual abordagem reduz risco com menor impacto?

A) Aplicar uma SCP na root bloqueando EC2 e CloudTrail para todas as contas.
B) Criar uma OU Sandbox e aplicar SCPs especÃ­ficas nessa OU.
C) Remover permissÃµes IAM manualmente de todos os usuÃ¡rios.
D) Criar uma bucket policy no log archive.

<details>
<summary><strong>Ver resposta</strong></summary>

âœ… **Resposta correta:** B

**ExplicaÃ§Ã£o:** SCP por OU aplica limite mÃ¡ximo apenas nas contas alvo. Aplicar na root pode quebrar produÃ§Ã£o. IAM manual Ã© frÃ¡gil e bucket policy nÃ£o controla criaÃ§Ã£o de recursos.

</details>

## QuestÃ£o 3

Uma empresa sem landing zone quer criar contas padronizadas com guardrails, logging bÃ¡sico e processo repetÃ­vel para novas equipes. Ela nÃ£o possui automaÃ§Ã£o madura prÃ³pria. O que Ã© mais apropriado?

A) Criar contas manualmente em Organizations e documentar o processo em planilha.
B) Usar Control Tower com Account Factory e guardrails iniciais.
C) Criar todas as aplicaÃ§Ãµes na management account.
D) Usar uma SCP para conceder permissÃµes administrativas aos times.

<details>
<summary><strong>Ver resposta</strong></summary>

âœ… **Resposta correta:** B

**ExplicaÃ§Ã£o:** Control Tower entrega landing zone prescritiva e acelera governanÃ§a inicial. SCP nÃ£o concede permissÃµes, e workloads nÃ£o devem operar na management account.

</details>

## QuestÃ£o 4

O time de seguranÃ§a precisa administrar GuardDuty e Security Hub em todas as contas sem usar a management account para operaÃ§Ã£o diÃ¡ria. Qual padrÃ£o atende melhor?

A) Delegated administrator em uma conta de seguranÃ§a.
B) UsuÃ¡rio IAM administrativo replicado em todas as contas.
C) Compartilhar a senha root da management account.
D) Criar uma role local sem integraÃ§Ã£o organizacional.

<details>
<summary><strong>Ver resposta</strong></summary>

âœ… **Resposta correta:** A

**ExplicaÃ§Ã£o:** Administrador delegado centraliza operaÃ§Ã£o de serviÃ§os de seguranÃ§a sem transformar a management account em conta operacional.

</details>

## QuestÃ£o 5

Uma SCP nega `s3:PutBucketPublicAccessBlock` em uma OU. Um usuÃ¡rio administrador na conta tenta executar a aÃ§Ã£o com policy IAM `AdministratorAccess`. O que acontece?

A) A aÃ§Ã£o Ã© permitida porque AdministratorAccess vence SCP.
B) A aÃ§Ã£o Ã© negada porque SCP define o limite mÃ¡ximo da conta.
C) A aÃ§Ã£o Ã© permitida se o bucket estiver criptografado.
D) A aÃ§Ã£o Ã© permitida se houver permissions boundary.

<details>
<summary><strong>Ver resposta</strong></summary>

âœ… **Resposta correta:** B

**ExplicaÃ§Ã£o:** SCP nÃ£o concede permissÃµes, mas limita o mÃ¡ximo permitido. Uma negaÃ§Ã£o efetiva por SCP impede a aÃ§Ã£o mesmo com permissÃµes IAM amplas.

</details>
