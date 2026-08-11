# Questoes - Seguranca Centralizada

## Questao 1

Uma empresa regulada possui 300 contas AWS. O SOC precisa administrar GuardDuty, Security Hub e Inspector centralmente, enquanto logs de auditoria devem ficar em uma conta separada e protegida.

Qual arquitetura e mais adequada?

A. Habilitar os servicos manualmente em cada conta e enviar relatorios por e-mail.
B. Usar uma Security Account como delegated administrator e uma Log Archive Account separada para CloudTrail/logs.
C. Operar todos os servicos de seguranca na management account diariamente.
D. Criar usuarios IAM do SOC em cada conta de workload.

<details>
<summary><strong>Ver resposta</strong></summary>

**Resposta correta:** B

**Por que esta correta:** administradores delegados centralizam operacao sem usar a management account; Log Archive separa armazenamento de evidencias.

**Por que as alternativas sao mais fracas:** A nao escala; C aumenta risco da management account; D espalha credenciais e lifecycle.

</details>

## Questao 2

Uma access key foi vazada publicamente. A empresa quer detectar uso anomalo, correlacionar o evento com outros findings e investigar chamadas API historicas.

Qual combinacao e mais apropriada?

A. GuardDuty, Security Hub e CloudTrail.
B. Macie, RDS Proxy e CloudFront.
C. AWS Backup, S3 Glacier e DMS.
D. Parameter Store, EFS e Route 53.

<details>
<summary><strong>Ver resposta</strong></summary>

**Resposta correta:** A

**Por que esta correta:** GuardDuty detecta comportamento suspeito, Security Hub agrega findings e CloudTrail fornece trilha de chamadas API.

**Por que as alternativas sao mais fracas:** B mistura descoberta de dados e servicos sem correlacao com credencial; C e backup/migracao; D nao detecta ameaca.

</details>

## Questao 3

Um time criou uma customer managed key para dados sensiveis. Mesmo com IAM policy permitindo `kms:Decrypt`, uma aplicacao em outra conta nao consegue usar a chave.

Qual ponto deve ser verificado primeiro?

A. Se a key policy permite o uso pela conta/principal externo ou permite IAM complementar.
B. Se Security Hub esta habilitado.
C. Se existe uma read replica do banco.
D. Se CloudFront esta configurado.

<details>
<summary><strong>Ver resposta</strong></summary>

**Resposta correta:** A

**Por que esta correta:** KMS exige autorizacao efetiva envolvendo key policy; IAM sozinho pode nao bastar se a key policy nao permitir.

**Por que as alternativas sao mais fracas:** B pode apontar postura, mas nao autoriza KMS; C e D sao irrelevantes para decrypt.

</details>

## Questao 4

Uma empresa quer identificar vulnerabilidades em instancias EC2 e imagens de container, alem de detectar comportamento suspeito como comunicacao com dominios maliciosos.

Qual combinacao diferencia melhor as responsabilidades?

A. Inspector para vulnerabilidades e GuardDuty para comportamento suspeito.
B. Macie para vulnerabilidades e RDS Proxy para comportamento suspeito.
C. Security Hub para varredura de pacotes e Parameter Store para DNS malicioso.
D. AWS Config para criptografar automaticamente todos os volumes.

<details>
<summary><strong>Ver resposta</strong></summary>

**Resposta correta:** A

**Por que esta correta:** Inspector avalia vulnerabilidades; GuardDuty detecta ameacas e anomalias.

**Por que as alternativas sao mais fracas:** Macie e para dados sensiveis em S3; Security Hub agrega findings; Config avalia conformidade, nao criptografa tudo sozinho.

</details>

## Questao 5

Uma organizacao precisa descobrir buckets S3 com dados sensiveis e tambem avaliar se recursos violam regras de configuracao, agregando findings para o SOC.

Qual desenho e mais completo?

A. Macie para descoberta de dados sensiveis, AWS Config para avaliacao de configuracao e Security Hub para agregacao.
B. GuardDuty sozinho, pois ele classifica dados sensiveis em S3.
C. Secrets Manager sozinho, pois ele encontra dados pessoais em objetos.
D. KMS key rotation, pois ela avalia compliance de todos os recursos.

<details>
<summary><strong>Ver resposta</strong></summary>

**Resposta correta:** A

**Por que esta correta:** Macie, Config e Security Hub atuam em camadas complementares: dados sensiveis, conformidade de recursos e agregacao.

**Por que as alternativas sao mais fracas:** GuardDuty nao classifica dados; Secrets Manager gerencia segredos; KMS rotation nao e avaliacao ampla de compliance.

</details>
