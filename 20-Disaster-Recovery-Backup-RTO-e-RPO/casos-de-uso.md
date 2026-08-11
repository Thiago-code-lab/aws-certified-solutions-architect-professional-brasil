# Casos de Uso - Disaster Recovery

## 1. Sistema administrativo com baixo custo

**Cenario:** sistema interno de faturamento usado por poucas areas, com RTO de 8 horas e RPO de 24 horas.

**Restricoes:** a empresa quer custo recorrente minimo e auditoria de retencao.

**Decisao:** usar AWS Backup com politicas por tag, copia cross-region, vault lock quando aplicavel e templates IaC para recriar a stack.

**Trade-off:** baixo custo, mas failover nao e imediato e depende de runbook bem testado.

## 2. Plataforma de pedidos com DR regional

**Cenario:** aplicacao de pedidos precisa voltar em ate 30 minutos com perda maxima de poucos minutos.

**Restricoes:** duplicar capacidade integral e caro; o banco e o componente mais critico.

**Decisao:** Warm Standby em regiao secundaria com banco replicado, servicos em capacidade reduzida, Route 53 failover e automacao de escala.

**Trade-off:** custo maior que pilot light, mas RTO menor e validacao continua do ambiente secundario.

## 3. Aplicacao legada baseada em servidores

**Cenario:** workloads legados em EC2 possuem dependencias locais e configuracoes dificeis de reconstruir manualmente.

**Restricoes:** RPO baixo e pouca tolerancia para reinstalacao manual durante incidente.

**Decisao:** usar AWS Elastic Disaster Recovery para replicacao continua e testes de lancamento em sub-redes isoladas.

**Trade-off:** reduz risco de reconstrucao manual, mas exige operacao do agente, validacao de rede, licencas e runbooks de failover/failback.
