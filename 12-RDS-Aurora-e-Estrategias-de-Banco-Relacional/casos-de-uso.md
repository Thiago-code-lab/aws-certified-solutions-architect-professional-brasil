# Casos de Uso - RDS e Aurora

## Cenario 1 - Alta disponibilidade regional para sistema transacional

### Contexto

Uma seguradora executa sistema transacional em banco relacional e precisa reduzir indisponibilidade em falha de AZ.

### Requisitos

- Menor mudanca na aplicacao.
- Failover dentro da mesma regiao.
- Backups automaticos e criptografia.

### Arquitetura recomendada

Amazon RDS Multi-AZ ou Aurora com replicas em AZs distintas, backups automaticos, KMS e janela de manutencao controlada.

### Por que

O problema e HA regional. Multi-AZ e o padrao gerenciado para falha de AZ.

### Trade-offs

Custo maior que Single-AZ e necessidade de testar comportamento da aplicacao durante failover.

### Por que nao as alternativas

Read replica foca leitura; snapshot nao atende RTO baixo; multi-region seria complexidade desnecessaria se o requisito e apenas AZ.

### Sinal de prova

"survive AZ failure", "minimal application changes", "single Region".

## Cenario 2 - Catalogo global read-heavy

### Contexto

Um varejista global tem catalogo consultado mundialmente e escrita concentrada em uma regiao principal.

### Requisitos

- Baixa latencia de leitura global.
- Baixo RPO em desastre regional.
- Escrita centralizada.

### Arquitetura recomendada

Aurora Global Database com writer na regiao primaria e regioes secundarias para leitura, combinado com runbook de failover.

### Por que

O sinal dominante e leitura global com recuperacao regional mais rapida que backup.

### Trade-offs

Mais custo e operacao multi-region; leituras secundarias podem ter atraso de replicacao.

### Por que nao as alternativas

Multi-AZ nao reduz latencia global; backups nao atendem leitura; RDS Proxy nao replica dados.

### Sinal de prova

"global reads", "primary write Region", "low RPO".

## Cenario 3 - Serverless com storm de conexoes

### Contexto

Uma API em Lambda acessa RDS e falha em campanhas por excesso de conexoes simultaneas.

### Requisitos

- Preservar banco relacional.
- Reduzir rejeicao de conexoes.
- Evitar superdimensionamento desnecessario.

### Arquitetura recomendada

RDS Proxy entre Lambda e RDS, com tuning de pool, secrets no Secrets Manager e monitoramento de conexoes.

### Por que

O gargalo descrito e gerenciamento de conexoes, nao necessariamente capacidade bruta de banco.

### Trade-offs

Adiciona componente e custo; queries lentas e falta de indices ainda precisam ser corrigidas.

### Por que nao as alternativas

Escalar instancia pode mascarar o problema; read replica nao recebe escrita; cache nao substitui transacoes quando escrita e necessaria.

### Sinal de prova

"Lambda concurrency", "too many connections", "CPU acceptable".
