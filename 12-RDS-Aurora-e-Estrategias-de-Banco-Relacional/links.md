# Links Oficiais - RDS e Aurora

## Essencial

- [Amazon RDS User Guide](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html) - Base oficial para operacao gerenciada, backups, Multi-AZ e replicas.
- [Amazon Aurora User Guide](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html) - Leitura prioritaria para entender arquitetura Aurora e diferenca em relacao a RDS tradicional.
- [High availability for Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html) - Essencial para distinguir Multi-AZ de read scaling e DR regional.
- [Aurora Global Database](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database.html) - Prioridade alta para cenarios globais e baixo RPO cross-region.

## Aprofundamento

- [Working with read replicas](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html) - Ajuda a separar escala de leitura de alta disponibilidade.
- [Amazon RDS Proxy](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.html) - Importante para workloads serverless, pooling e failover de conexoes.
- [Backing up and restoring Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_CommonTasks.BackupRestore.html) - Base para diferenciar backup, snapshot e recuperacao point-in-time.

## Referencia

- [Amazon RDS encryption](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html) - Use para validar criptografia, KMS e copias.
- [Aurora Replicas](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Replication.html) - Referencia para leitura e failover em clusters Aurora.
- [AWS Database Migration Service](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html) - Consulte quando o cenario mistura banco relacional e migracao.
