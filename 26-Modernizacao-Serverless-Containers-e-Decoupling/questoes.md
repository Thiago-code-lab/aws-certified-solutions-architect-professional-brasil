# Questoes - Modernizacao

## Questao 1

Uma empresa possui um monolito de 10 anos com release trimestral e muitas regras de negocio. O negocio precisa de novas APIs mobile em meses, mas nao aceita uma reescrita multi-ano.

Qual abordagem e mais adequada?

A. Big-bang rewrite completo antes de entregar qualquer funcionalidade.
B. Strangler pattern, extraindo capacidades novas por tras de uma camada de API/roteamento e mantendo partes estaveis no monolito.
C. Rehost do monolito e proibicao de novas APIs.
D. Migrar tudo para EKS sem alterar arquitetura.

<details>
<summary><strong>Ver resposta</strong></summary>

**Resposta correta:** B

**Por que esta correta:** strangler permite modernizacao incremental, entrega de valor e reducao de risco.

**Por que as alternativas sao mais fracas:** A concentra risco e atrasa valor; C nao atende negocio; D troca plataforma sem resolver acoplamento.

</details>

## Questao 2

Um sistema recebe picos de eventos de pedidos. O processamento chama provedores externos instaveis e precisa de retry sem bloquear a API principal.

Qual desenho e mais defensavel?

A. Processar tudo sincronicamente na requisicao do usuario.
B. Usar SQS para desacoplar, consumidores idempotentes e DLQ para falhas.
C. Aumentar timeout da API para varios minutos.
D. Usar apenas CloudFront.

<details>
<summary><strong>Ver resposta</strong></summary>

**Resposta correta:** B

**Por que esta correta:** fila desacopla picos, permite retry e evita bloquear a experiencia principal.

**Por que as alternativas sao mais fracas:** A e C ampliam acoplamento e latencia; D nao processa eventos.

</details>

## Questao 3

Uma organizacao quer adotar containers, mas tem time pequeno, pouca experiencia Kubernetes e objetivo de reduzir operacao. As aplicacoes sao stateless e nao exigem recursos especificos de Kubernetes.

Qual escolha e mais apropriada?

A. ECS com Fargate.
B. EKS obrigatoriamente, pois todo container moderno deve usar Kubernetes.
C. EC2 autogerenciado com scripts manuais.
D. Lambda para processos longos sem avaliar limites.

<details>
<summary><strong>Ver resposta</strong></summary>

**Resposta correta:** A

**Por que esta correta:** ECS/Fargate reduz overhead operacional para containers stateless quando Kubernetes nao e requisito.

**Por que as alternativas sao mais fracas:** B adiciona complexidade desnecessaria; C aumenta toil; D pode ser inadequado para processos longos.

</details>

## Questao 4

Um dominio de notificacoes precisa receber eventos de varios sistemas e rotear para consumidores diferentes, sem acoplar produtores a filas especificas.

Qual servico tende a se encaixar melhor?

A. EventBridge.
B. Uma unica fila SQS compartilhada por todos sem schema.
C. EBS snapshots.
D. Direct Connect.

<details>
<summary><strong>Ver resposta</strong></summary>

**Resposta correta:** A

**Por que esta correta:** EventBridge favorece roteamento baseado em eventos entre produtores e consumidores desacoplados.

**Por que as alternativas sao mais fracas:** B cria acoplamento e mistura consumidores; C e armazenamento/backup; D e conectividade hibrida.

</details>

## Questao 5

Um workload legado e estavel, tem prazo de migracao curto por encerramento de data center e nao sofre com escala ou release. A empresa quer minimizar risco inicial.

Qual estrategia deve ser considerada antes de refatorar?

A. Rehost ou replatform com modernizacao posterior se houver valor.
B. Refactor completo imediato.
C. Big-bang rewrite para microservicos.
D. Repurchase sem SaaS equivalente.

<details>
<summary><strong>Ver resposta</strong></summary>

**Resposta correta:** A

**Por que esta correta:** prazo curto e baixo problema arquitetural favorecem mover com menor mudanca e modernizar depois se houver justificativa.

**Por que as alternativas sao mais fracas:** B e C aumentam risco sem necessidade; D depende de alternativa SaaS real.

</details>
