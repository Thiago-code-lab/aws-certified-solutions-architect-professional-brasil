# Questoes - Modernizacao

## Questao 1

Uma empresa tem monolito de dez anos, banco compartilhado e novas APIs mobile. O negocio nao aceita rewrite de varios anos. Qual abordagem e melhor?

A) Big-bang rewrite.
B) Strangler pattern com camada de roteamento e novos servicos por dominio.
C) Migrar tudo para EKS sem reduzir acoplamento.
D) Recriar todo banco antes de entregar valor.

<details><summary><strong>Ver resposta</strong></summary>

**Resposta correta:** B

Strangler entrega valor incremental e reduz risco. A concentra risco; C troca plataforma sem modernizar; D cria dependencia excessiva.
</details>

## Questao 2

Pedido online dispara email, estoque e analytics. Picos causam lentidao no fluxo sincrono. O que melhora resiliencia?

A) Aumentar timeouts.
B) Usar SQS/EventBridge para desacoplar etapas e permitir retry.
C) Colocar tudo no mesmo container.
D) Remover observabilidade.

<details><summary><strong>Ver resposta</strong></summary>

**Resposta correta:** B

Etapas independentes combinam com assincronia e retry. As demais aumentam acoplamento ou risco operacional.
</details>

## Questao 3

Equipe pequena precisa operar APIs stateless com picos variaveis e pouca experiencia Kubernetes. Qual opcao reduz overhead?

A) EKS altamente customizado.
B) Lambda quando servir ou ECS/Fargate para containers sem gerenciar instancias.
C) EC2 manual sem Auto Scaling.
D) Um cluster por microservico.

<details><summary><strong>Ver resposta</strong></summary>

**Resposta correta:** B

Lambda e Fargate reduzem operacao. EKS pode ser valido, mas exige maturidade.
</details>

## Questao 4

Uma organizacao ja tem Kubernetes maduro, observabilidade e times treinados. Servicos exigem runtime especifico. Qual decisao e defensavel?

A) EKS pode ser adequado, aceitando maior operacao.
B) Lambda substitui todos os containers.
C) S3 executa servicos.
D) Voltar ao monolito.

<details><summary><strong>Ver resposta</strong></summary>

**Resposta correta:** A

Maturidade Kubernetes e necessidade de controle favorecem EKS. As demais alternativas ignoram requisitos.
</details>

## Questao 5

Faturamento muda rapidamente, mas modulo fiscal legado e estavel e regulado. Qual plano e melhor?

A) Modernizar tudo simultaneamente.
B) Refatorar faturamento primeiro e manter fiscal ate haver justificativa e testes.
C) Remover controles fiscais.
D) Criar eventos sem idempotencia.

<details><summary><strong>Ver resposta</strong></summary>

**Resposta correta:** B

Modernizacao prioriza valor e risco. Mexer em dominio regulado sem necessidade aumenta risco sem retorno.
</details>
