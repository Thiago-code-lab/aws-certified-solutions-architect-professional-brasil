# Questoes - RDS e Aurora

## Questao 1

Uma aplicacao regional usa RDS PostgreSQL Single-AZ. O requisito novo e reduzir indisponibilidade em falha de AZ, sem mudar a aplicacao e sem criar arquitetura multi-region.

Qual alternativa atende melhor?

A. Habilitar RDS Multi-AZ.
B. Criar snapshot diario e restaurar quando houver falha.
C. Criar read replica na mesma AZ.
D. Colocar CloudFront na frente do banco.

<details>
<summary><strong>Ver resposta</strong></summary>

**Resposta correta:** A

**Por que esta correta:** Multi-AZ entrega standby/failover gerenciado para falha de AZ, com baixa mudanca na aplicacao.

**Por que as alternativas sao mais fracas:** snapshot tem RTO maior; read replica e para leitura/replicacao e nao substitui HA regional automaticamente; CloudFront nao acelera acesso a banco relacional.

</details>

## Questao 2

Um catalogo global recebe muitas leituras de clientes na Europa e America do Norte, mas as escritas devem permanecer concentradas em uma regiao primaria. A empresa quer baixa latencia de leitura e baixo RPO regional.

Qual escolha e mais apropriada?

A. Aurora Global Database.
B. Apenas RDS Multi-AZ na regiao primaria.
C. Backups automaticos com retencao de 35 dias.
D. RDS Proxy sem replicas.

<details>
<summary><strong>Ver resposta</strong></summary>

**Resposta correta:** A

**Por que esta correta:** Aurora Global Database permite replicas em regioes secundarias para leitura global e melhora postura de recuperacao cross-region.

**Por que as alternativas sao mais fracas:** Multi-AZ e regional; backups nao atendem leitura global; RDS Proxy gerencia conexoes, nao replica dados globalmente.

</details>

## Questao 3

Uma API serverless com Lambda usa RDS MySQL. Em campanhas, milhares de execucoes simultaneas abrem conexoes e o banco passa a rejeitar sessoes, mesmo quando CPU e IO ainda estao aceitaveis.

Qual acao deve ser priorizada?

A. Adicionar RDS Proxy entre Lambda e o banco.
B. Criar snapshots mais frequentes.
C. Migrar todos os dados para S3 Glacier.
D. Criar uma read replica para receber escritas.

<details>
<summary><strong>Ver resposta</strong></summary>

**Resposta correta:** A

**Por que esta correta:** o sinal e storm de conexoes. RDS Proxy fornece pooling e melhora comportamento de failover.

**Por que as alternativas sao mais fracas:** snapshots nao reduzem conexoes; Glacier nao e banco transacional; read replica nao recebe escritas da aplicacao.

</details>

## Questao 4

Uma empresa acredita que backups automaticos cross-region bastam para atender RPO de poucos segundos em desastre regional de um banco relacional critico.

Qual avaliacao e mais correta?

A. Backups sao suficientes para RPO de segundos em qualquer engine.
B. Replicacao cross-region ou Aurora Global Database devem ser avaliadas; backup e restauracao geralmente nao atendem RPO tao baixo.
C. Multi-AZ resolve desastre regional.
D. RDS Proxy substitui replicacao.

<details>
<summary><strong>Ver resposta</strong></summary>

**Resposta correta:** B

**Por que esta correta:** RPO de segundos aponta para replicacao, nao apenas backup. Backup e restauracao tendem a ter RTO/RPO maiores.

**Por que as alternativas sao mais fracas:** A ignora limites de backup; C confunde AZ com regiao; D resolve conexoes, nao perda de dados.

</details>

## Questao 5

Uma aplicacao legada certificada para SQL Server precisa migrar para AWS com baixa alteracao de codigo e operacao gerenciada. Nao ha requisito de arquitetura global, mas ha requisito de HA dentro da regiao.

Qual decisao e mais defensavel?

A. Amazon RDS for SQL Server com Multi-AZ, backups automaticos e criptografia.
B. Aurora Global Database, mesmo sem compatibilidade da aplicacao.
C. DynamoDB global tables.
D. EC2 autogerenciado sem backups automatizados.

<details>
<summary><strong>Ver resposta</strong></summary>

**Resposta correta:** A

**Por que esta correta:** RDS preserva compatibilidade de engine e reduz operacao; Multi-AZ atende HA regional.

**Por que as alternativas sao mais fracas:** Aurora nao e SQL Server; DynamoDB exigiria redesign; EC2 autogerenciado aumenta overhead e risco.

</details>
