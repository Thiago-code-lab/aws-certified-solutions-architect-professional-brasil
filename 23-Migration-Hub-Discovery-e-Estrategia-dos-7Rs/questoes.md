# Questoes - Estrategia de Migracao

## Questao 1

Uma empresa precisa sair de um data center em 10 meses. O portfolio tem 200 aplicacoes, dependencias pouco documentadas e diferentes criticidades. A diretoria quer reduzir risco de indisponibilidade e evitar modernizar tudo antes da saida.

Qual abordagem e mais adequada?

A. Refatorar todas as aplicacoes antes de qualquer migracao.
B. Fazer discovery, mapear dependencias, preparar landing zone e planejar waves com rehost/replatform para candidatos adequados.
C. Migrar aleatoriamente as aplicacoes menores primeiro sem dependency mapping.
D. Comprar SaaS para todo o portfolio sem assessment.

<details>
<summary><strong>Ver resposta</strong></summary>

**Resposta correta:** B

**Por que esta correta:** prazo e incerteza pedem assessment, dependencia e waves. Rehost/replatform podem reduzir risco de prazo sem ignorar dependencias.

**Por que as alternativas sao mais fracas:** A aumenta risco de prazo; C pode quebrar sistemas dependentes; D ignora adequacao, licenca e dados.

</details>

## Questao 2

Apos uma aquisicao, duas empresas possuem ferramentas internas duplicadas. Uma delas nao tem usuarios ativos ha meses e outra e software comercial disponivel como SaaS gerenciado.

Qual classificacao e mais defensavel?

A. Rehost para ambas, pois toda aplicacao deve ir para AWS.
B. Retire para a ferramenta sem uso e Repurchase para a ferramenta comercial se o SaaS atender requisitos.
C. Refactor para ambas antes de avaliar usuarios.
D. Retain permanente para ambas.

<details>
<summary><strong>Ver resposta</strong></summary>

**Resposta correta:** B

**Por que esta correta:** workload sem uso tende a Retire; software comercial com SaaS adequado tende a Repurchase.

**Por que as alternativas sao mais fracas:** A migra custo desnecessario; C moderniza sem valor; D posterga consolidacao sem justificativa.

</details>

## Questao 3

Um monolito critico gera alta receita, tem deploy mensal arriscado e escala mal em campanhas. O contrato do data center ainda permite 24 meses. A empresa quer melhorar agilidade e resiliencia, aceitando investimento.

Qual estrategia tende a ser mais apropriada?

A. Refactor/Re-architect planejado por dominios, possivelmente com etapas intermediarias.
B. Rehost imediato e encerrar qualquer modernizacao.
C. Retire, pois monolitos nao devem ser migrados.
D. Repurchase sem analisar funcionalidades especificas.

<details>
<summary><strong>Ver resposta</strong></summary>

**Resposta correta:** A

**Por que esta correta:** alto valor, prazo menos agressivo e necessidade de agilidade sinalizam modernizacao justificada.

**Por que as alternativas sao mais fracas:** B preserva problemas centrais; C elimina sistema critico; D pode nao cobrir regras de negocio.

</details>

## Questao 4

Uma aplicacao de baixa criticidade roda em servidor virtual com poucas dependencias. O prazo de migracao e curto, e a meta principal e liberar espaco no data center, mantendo mudanca minima.

Qual R e mais provavel?

A. Rehost.
B. Refactor/Re-architect.
C. Repurchase.
D. Retire.

<details>
<summary><strong>Ver resposta</strong></summary>

**Resposta correta:** A

**Por que esta correta:** baixa dependencia, baixa criticidade e mudanca minima com prazo curto apontam para rehost.

**Por que as alternativas sao mais fracas:** B e excessivo para o valor/tempo; C depende de SaaS equivalente; D requer evidencia de desuso.

</details>

## Questao 5

Um workload deve permanecer on-premises por 18 meses por exigencia contratual de residencia de dados, mas outros sistemas dependentes ja podem migrar.

Como isso deve ser tratado no plano?

A. Retain temporario para o workload bloqueado, documentando dependencia e integracao hibrida nas waves.
B. Rehost imediato ignorando o contrato.
C. Retire o workload para remover dependencia.
D. Refactor obrigatorio antes de qualquer outro sistema migrar.

<details>
<summary><strong>Ver resposta</strong></summary>

**Resposta correta:** A

**Por que esta correta:** bloqueio contratual real aponta para Retain temporario, com plano de dependencia e revisao futura.

**Por que as alternativas sao mais fracas:** B viola restricao; C elimina sistema possivelmente necessario; D pode travar todo o portfolio sem necessidade.

</details>
