# Questoes - Otimizacao de Custos e FinOps

## Questao 1

O CFO quer atribuir custos por unidade de negocio em uma Organization com dezenas de contas. Hoje ha recursos sem tag, ambientes misturados e relatorios manuais inconsistentes.

Qual acao deve ser priorizada?

A. Comprar Savings Plans imediatamente para todo o gasto.
B. Definir estrategia de contas/tags, habilitar relatorios com CUR/Cost Explorer e criar Budgets por owner.
C. Desligar aleatoriamente todos os recursos sem tag.
D. Migrar todos os workloads para Spot.

<details>
<summary><strong>Ver resposta</strong></summary>

**Resposta correta:** B

**Por que esta correta:** o problema principal e visibilidade/alocacao. Sem ownership, otimizacoes podem ser politicamente e tecnicamente erradas.

**Por que as alternativas sao mais fracas:** A compromete gasto antes de medir; C pode causar incidente; D nao serve para todos os workloads.

</details>

## Questao 2

Uma plataforma tem baseline EC2 estavel durante todo o ano e picos imprevisiveis em campanhas. A empresa quer reduzir custo sem perder capacidade durante picos.

Qual abordagem e mais adequada?

A. Commitment para 100% da maior demanda historica.
B. Rightsizing, Savings Plans/RIs para baseline e capacidade flexivel On-Demand/Spot para picos tolerantes.
C. Usar apenas On-Demand para sempre.
D. Desativar Auto Scaling para reduzir variabilidade.

<details>
<summary><strong>Ver resposta</strong></summary>

**Resposta correta:** B

**Por que esta correta:** combina desconto no uso previsivel com flexibilidade para demanda incerta.

**Por que as alternativas sao mais fracas:** A supercompromete; C perde oportunidade de desconto; D reduz resiliencia.

</details>

## Questao 3

Uma arquitetura multi-region apresenta aumento inesperado de custos. A maior parte vem de transferencia inter-region e trafego por NAT Gateways, nao de CPU.

Qual resposta e mais apropriada?

A. Comprar Reserved Instances para EC2 sem mudar arquitetura.
B. Mapear fluxos de dados, reduzir transferencia desnecessaria, aproximar processamento dos dados e avaliar endpoints/cache.
C. Mover todos os dados para Glacier imediatamente.
D. Criar mais contas AWS.

<details>
<summary><strong>Ver resposta</strong></summary>

**Resposta correta:** B

**Por que esta correta:** o driver e arquitetura de rede/dados. A solucao deve atacar fluxo, localidade e caminhos de transferencia.

**Por que as alternativas sao mais fracas:** A atua em compute, nao rede; C pode quebrar acesso; D nao reduz transferencia por si so.

</details>

## Questao 4

Um ambiente de desenvolvimento fica ligado 24x7, mas e usado apenas em horario comercial. A empresa quer quick wins sem afetar producao.

Qual acao e mais defensavel?

A. Agendar desligamento/escala de recursos dev com tags de ownership e excecoes documentadas.
B. Aplicar SCP que impede EC2 em todas as contas, incluindo producao.
C. Comprar RIs para o ambiente dev ocioso.
D. Remover backups de producao.

<details>
<summary><strong>Ver resposta</strong></summary>

**Resposta correta:** A

**Por que esta correta:** ambientes dev ociosos sao candidatos a scheduling, desde que ownership e excecoes estejam claras.

**Por que as alternativas sao mais fracas:** B e amplo demais; C compromete desperdicio; D reduz resiliencia.

</details>

## Questao 5

Um workload batch processa filas durante a madrugada. Ele e idempotente, tolera reprocessamento e pode aguardar capacidade, mas precisa minimizar custo.

Qual opcao e mais apropriada?

A. Spot Instances ou compute tolerante a interrupcao com checkpoint/retry.
B. On-Demand superdimensionado 24x7.
C. Banco Multi-AZ maior para processar filas.
D. CloudFront para executar batch.

<details>
<summary><strong>Ver resposta</strong></summary>

**Resposta correta:** A

**Por que esta correta:** workload interruptivel e idempotente e bom candidato a Spot, com mecanismos de retry/checkpoint.

**Por que as alternativas sao mais fracas:** B desperdiça capacidade; C ataca o componente errado; D e CDN, nao processamento batch.

</details>
