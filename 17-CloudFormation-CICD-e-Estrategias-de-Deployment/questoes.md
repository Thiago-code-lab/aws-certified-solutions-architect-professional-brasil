# Questoes - Deployment e IaC

## Questao 1

Uma empresa global precisa aplicar uma configuracao padrao de AWS Config e CloudTrail em 100 contas e varias regioes. A equipe quer evitar criacao manual e manter controle central de atualizacoes.

Qual abordagem e mais adequada?

A. CloudFormation StackSets com escopo de contas/regioes e operacao controlada.
B. Criar manualmente cada stack em cada conta.
C. Copiar templates por e-mail para cada time aplicar.
D. Usar apenas Route 53 health checks.

<details>
<summary><strong>Ver resposta</strong></summary>

**Resposta correta:** A

**Por que esta correta:** StackSets foram desenhados para distribuir stacks entre multiplas contas e regioes com governanca.

**Por que as alternativas sao mais fracas:** B e C aumentam drift e erro humano; D nao gerencia infraestrutura.

</details>

## Questao 2

Uma API de checkout tera uma mudanca de regra de negocio com risco alto. A empresa possui metricas de erro e conversao em tempo quase real e quer expor a nova versao inicialmente a poucos usuarios.

Qual estrategia e mais defensavel?

A. Canary deployment.
B. All-at-once deployment.
C. Atualizacao manual em producao sem observabilidade.
D. Desativar rollback para acelerar a entrega.

<details>
<summary><strong>Ver resposta</strong></summary>

**Resposta correta:** A

**Por que esta correta:** canary reduz blast radius liberando gradualmente e usando metricas para decidir avancar ou reverter.

**Por que as alternativas sao mais fracas:** B amplia impacto; C remove controle; D aumenta risco operacional.

</details>

## Questao 3

Um template CloudFormation altera sub-redes, security groups e um load balancer de producao. Antes de aplicar, o time precisa revisar quais recursos serao substituidos.

Qual recurso atende melhor?

A. Change set.
B. Stack drift detection apenas depois da mudanca.
C. All-at-once deployment.
D. S3 lifecycle rule.

<details>
<summary><strong>Ver resposta</strong></summary>

**Resposta correta:** A

**Por que esta correta:** change set permite visualizar mudancas planejadas antes da execucao, incluindo possiveis substituicoes.

**Por que as alternativas sao mais fracas:** B detecta divergencia, nao antecipa update; C e estrategia de rollout, nao revisao de IaC; D e irrelevante.

</details>

## Questao 4

Uma plataforma SaaS precisa promover mudancas de dev para staging e producao em contas separadas. Producao exige aprovacao formal, roles com menor privilegio e evidencias de deploy.

Qual desenho e mais adequado?

A. Pipeline multi-account com roles cross-account, approval gate antes de producao e logs de execucao.
B. Usuario IAM compartilhado com AdministratorAccess em todas as contas.
C. Deploy direto de laptops dos desenvolvedores em producao.
D. Stack unica na management account para todos os recursos.

<details>
<summary><strong>Ver resposta</strong></summary>

**Resposta correta:** A

**Por que esta correta:** separa ambientes, controla promocao, registra evidencias e limita permissao do pipeline.

**Por que as alternativas sao mais fracas:** B e C violam auditoria e menor privilegio; D mistura escopos e aumenta blast radius.

</details>

## Questao 5

Uma aplicacao critica precisa de rollback rapido com baixo downtime. A empresa consegue manter temporariamente dois ambientes completos e alternar trafego.

Qual estrategia tende a ser mais apropriada?

A. Blue/green deployment.
B. All-at-once em ambiente unico.
C. Atualizacao in-place sem health checks.
D. Criar snapshot manual apos o deploy.

<details>
<summary><strong>Ver resposta</strong></summary>

**Resposta correta:** A

**Por que esta correta:** blue/green permite validar novo ambiente e alternar trafego, mantendo caminho de retorno ao ambiente anterior.

**Por que as alternativas sao mais fracas:** B e C aumentam downtime/blast radius; D nao e estrategia de rollback de aplicacao.

</details>
