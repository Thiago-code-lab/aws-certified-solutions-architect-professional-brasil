# Cheatsheet - Decisoes de Banco Relacional

| Sinal no cenario | Escolha provavel | Por que | Trade-off | Armadilha |
| --- | --- | --- | --- | --- |
| Falha de AZ com baixa mudanca | Multi-AZ | Failover regional gerenciado | Custo maior | Confundir com DR regional |
| Muitas leituras regionais | Read replica ou Aurora Replica | Escala leitura | Consistencia eventual | Esperar escala de escrita |
| Leituras globais | Aurora Global Database | Replica regional de baixa latencia | Custo/complexidade | Usar backup para leitura global |
| RPO baixo cross-region | Replicacao cross-region/Aurora Global Database | Menor perda de dados | Failover exige runbook | Achar que snapshot basta |
| Lambda abre conexoes demais | RDS Proxy | Pooling e controle de conexoes | Nao reduz queries ruins | Escalar instancia sem tratar conexoes |
| Engine legada certificada | RDS da engine compativel | Menor mudanca | Menos recursos cloud-native | Forcar Aurora sem compatibilidade |
| Sistema exige criptografia | KMS + encryption at rest + TLS | Governanca e compliance | Planejamento de keys | Criptografar backup e esquecer replicas |
| Janela de manutencao critica | Manutencao planejada e Multi-AZ | Reduz impacto | Requer teste | Ignorar upgrades e patches |

## HA vs escala vs DR

| Objetivo | Padrao |
| --- | --- |
| HA regional | Multi-AZ |
| Escala de leitura | Read replica / Aurora Replica |
| DR regional | Replica cross-region / Aurora Global Database / backup copy |
| Menor RTO/RPO | Replicacao e runbook de failover |
| Menor custo | Backup & Restore, se RTO/RPO permitirem |

## Checklist SAP-C02

- O requisito fala de leitura, escrita, conexao, AZ ou regiao?
- A aplicacao suporta endpoint de leitura separado?
- A consistencia eventual e aceitavel?
- O failover e automatico ou operacional?
- Backups e replicas usam chaves KMS corretas?
- Existe plano de teste e failback?
