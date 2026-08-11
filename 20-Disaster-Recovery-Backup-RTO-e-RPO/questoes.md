# Questoes - Disaster Recovery

## 1. RTO de 6 horas e baixo custo

Uma aplicacao interna tem RTO de 6 horas e RPO de 24 horas. A empresa quer minimizar custo recorrente, mas exige restauracao testavel em outra regiao.

Qual estrategia e mais adequada?

A. Active-Active Multi-Region com capacidade integral.
B. Backup & Restore com copias cross-region e infraestrutura definida como codigo.
C. Warm Standby com todos os servicos executando 50% da capacidade.
D. Multi-AZ dentro da mesma regiao apenas.

**Resposta:** B

**Justificativa:** RTO/RPO relaxados favorecem Backup & Restore. Copias cross-region e IaC tornam a recuperacao regional possivel. Multi-AZ nao cobre desastre regional.

## 2. RPO baixo para servidores legados

Um conjunto de servidores legados em EC2 precisa de recuperacao em outra regiao com perda minima de dados. A equipe quer evitar reconstruir manualmente volumes e configuracoes.

Qual servico e mais indicado?

A. AWS Elastic Disaster Recovery.
B. AWS Backup apenas com backup semanal.
C. S3 Cross-Region Replication.
D. CloudFront Origin Failover.

**Resposta:** A

**Justificativa:** AWS Elastic Disaster Recovery replica servidores continuamente e permite lancar instancias de recuperacao. AWS Backup e excelente para politicas de backup, mas backup semanal nao atende RPO baixo.

## 3. Multi-AZ confundido com DR regional

Uma aplicacao usa RDS Multi-AZ e Auto Scaling em tres AZs. O diretor afirma que isso ja atende o requisito de recuperacao contra indisponibilidade regional.

Qual avaliacao esta correta?

A. Correto, Multi-AZ equivale a Multi-Region para DR.
B. Incorreto, Multi-AZ melhora disponibilidade regional, mas nao substitui estrategia Multi-Region.
C. Correto apenas se o banco for criptografado com KMS.
D. Incorreto apenas para aplicacoes stateless.

**Resposta:** B

**Justificativa:** Multi-AZ protege contra falhas dentro da regiao. DR regional exige dados, infraestrutura, DNS/failover e operacao preparados em outra regiao.

## 4. Warm Standby para comercio eletronico

Um e-commerce exige RTO de 20 minutos e RPO de 5 minutos. A empresa aceita custo adicional, mas nao capacidade duplicada integral.

Qual desenho melhor atende?

A. Backup & Restore manual com snapshots diarios.
B. Pilot Light apenas com banco replicado e sem camada de aplicacao implantada.
C. Warm Standby com ambiente reduzido, replicacao de dados e automacao de escala no failover.
D. Uma unica regiao com backups em Glacier Deep Archive.

**Resposta:** C

**Justificativa:** Warm Standby mantem ambiente funcional reduzido, reduzindo RTO em comparacao com pilot light. Backup manual e archive frio nao atendem metas agressivas.

## 5. Active-Active e consistencia

Uma plataforma global quer Active-Active Multi-Region para escritas simultaneas. O time ainda nao definiu idempotencia, particionamento de dados nem resolucao de conflitos.

Qual risco principal o arquiteto deve levantar?

A. Active-Active elimina a necessidade de observabilidade.
B. Escritas simultaneas multi-region podem gerar conflitos e inconsistencia sem desenho de dados adequado.
C. Route 53 nao pode rotear usuarios por latencia.
D. Multi-Region reduz automaticamente todos os custos de transferencia.

**Resposta:** B

**Justificativa:** Active-Active exige estrategia explicita de consistencia, conflitos, idempotencia, replicacao e operacao. Sem isso, a arquitetura pode perder integridade de dados.
