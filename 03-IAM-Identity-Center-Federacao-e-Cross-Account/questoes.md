# Questoes - IAM, Identity Center e Cross-Account

## Questao 1

Uma empresa possui 100 contas AWS em uma Organization e usa um provedor corporativo de identidade com grupos, MFA e processo formal de desligamento. Ela quer acesso humano multi-account sem criar usuarios IAM em cada conta.

Qual arquitetura atende melhor ao requisito?

A. Criar usuarios IAM individuais em cada conta e sincronizar manualmente os grupos.
B. Integrar o IdP ao IAM Identity Center, mapear grupos para permission sets e atribuir contas conforme funcao.
C. Criar uma unica role administrativa na management account e compartilhar suas credenciais.
D. Usar apenas SCPs para conceder acesso aos usuarios corporativos.

<details>
<summary><strong>Ver resposta</strong></summary>

**Resposta correta:** B

**Por que esta correta:** o problema e workforce federation em escala. IAM Identity Center centraliza acesso humano, usa o IdP existente e provisiona permission sets nas contas.

**Por que as alternativas sao mais fracas:** A espalha lifecycle e credenciais; C viola isolamento e auditoria; D esta errada porque SCP nao concede permissao.

</details>

## Questao 2

Um fornecedor externo precisa acessar uma unica conta de workload por 14 dias para diagnosticar um problema. A empresa exige rastreabilidade, menor privilegio e nenhuma credencial longa.

Qual decisao e mais apropriada?

A. Criar um IAM user para o fornecedor e apagar depois.
B. Criar uma role cross-account com trust policy para o principal do fornecedor, condicoes apropriadas e permission policy minima.
C. Adicionar o fornecedor ao grupo Admin do IAM Identity Center de producao.
D. Criar uma access key compartilhada para o time do fornecedor.

<details>
<summary><strong>Ver resposta</strong></summary>

**Resposta correta:** B

**Por que esta correta:** role cross-account com STS entrega credenciais temporarias e separa quem pode assumir daquilo que pode executar.

**Por que as alternativas sao mais fracas:** A ainda cria credencial longa; C concede escopo excessivo; D elimina rastreabilidade individual e aumenta risco de vazamento.

</details>

## Questao 3

Desenvolvedores precisam permissao ampla em contas de desenvolvimento, mas em producao devem ter apenas leitura. A organizacao tambem quer impedir alteracoes em CloudTrail nas contas produtivas mesmo por administradores locais.

Qual combinacao e mais adequada?

A. Um unico permission set AdministratorAccess para todas as contas.
B. Permission sets separados por ambiente e SCPs na OU de producao bloqueando alteracoes proibidas.
C. Usuarios IAM duplicados com nomes diferentes em dev e prod.
D. Resource-based policies em todos os buckets S3 de producao.

<details>
<summary><strong>Ver resposta</strong></summary>

**Resposta correta:** B

**Por que esta correta:** permission sets modelam acesso humano por ambiente; SCPs definem limites maximos preventivos na OU de producao.

**Por que as alternativas sao mais fracas:** A nao diferencia risco; C aumenta operacao e credenciais; D atua apenas em recursos especificos e nao governa CloudTrail de forma ampla.

</details>

## Questao 4

Uma aplicacao em uma conta precisa ler objetos de um bucket S3 em outra conta. O time quer evitar usuarios IAM e manter auditoria clara de qual workload acessou os dados.

Qual abordagem e mais adequada?

A. Criar um IAM user na conta do bucket e gravar access key na aplicacao.
B. Criar uma role assumida pelo workload e configurar permissao no bucket ou role conforme o modelo cross-account.
C. Copiar todos os objetos para a conta da aplicacao diariamente.
D. Conceder acesso com SCP na OU das duas contas.

<details>
<summary><strong>Ver resposta</strong></summary>

**Resposta correta:** B

**Por que esta correta:** roles e policies cross-account permitem acesso temporario e auditavel. Dependendo do servico, resource-based policy no bucket pode autorizar o principal correto.

**Por que as alternativas sao mais fracas:** A usa credencial longa; C cria duplicacao e atraso; D nao concede acesso.

</details>

## Questao 5

Um time de plataforma permite que equipes criem roles para pipelines, mas quer garantir que nenhuma role criada por essas equipes possa ultrapassar um conjunto maximo de permissoes aprovado.

Qual mecanismo resolve melhor esse limite na entidade IAM?

A. Permissions boundary aplicada as roles criadas pelas equipes.
B. Trust policy permitindo qualquer principal da Organization.
C. IAM Identity Center permission set com AdministratorAccess.
D. CloudTrail multi-region.

<details>
<summary><strong>Ver resposta</strong></summary>

**Resposta correta:** A

**Por que esta correta:** permissions boundary limita o maximo efetivo de uma entidade IAM, mesmo quando outras policies sao anexadas.

**Por que as alternativas sao mais fracas:** B define quem assume, nao o maximo permitido; C e para acesso humano; D registra eventos, mas nao limita permissao.

</details>
