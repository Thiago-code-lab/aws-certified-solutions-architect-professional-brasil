# 12 - RDS, Aurora e Estrategias de Banco Relacional

Este modulo ensina decisoes de banco relacional sob restricoes de disponibilidade, escala, recuperacao, custo e operacao. No SAP-C02, a resposta correta raramente e "usar RDS" ou "usar Aurora" isoladamente; ela depende de entender se o problema e alta disponibilidade, leitura, conexoes, DR regional, backup, migracao ou reducao de operacao.

## Objetivos

- Escolher entre Amazon RDS e Amazon Aurora conforme requisito arquitetural.
- Diferenciar Multi-AZ, read replicas, Aurora Replicas e Aurora Global Database.
- Separar alta disponibilidade regional de disaster recovery multi-region.
- Usar backups, snapshots e replicacao sem confundir seus objetivos.
- Posicionar RDS Proxy para gerenciamento de conexoes, especialmente com Lambda ou workloads com picos.
- Avaliar failover, manutencao, criptografia, migracao e custo.

## Distincoes criticas

| Comparacao | Decisao Professional |
| --- | --- |
| Multi-AZ vs Read Replica | Multi-AZ e HA/failover; read replica e escala de leitura ou DR limitado conforme engine/configuracao |
| Multi-AZ vs multi-Region DR | Multi-AZ cobre falha de AZ; DR regional exige estrategia em outra regiao |
| RDS vs Aurora | RDS e adequado para engines tradicionais e simplicidade; Aurora oferece arquitetura cloud-native, replicas rapidas e opcoes globais |
| Aurora Replica vs Aurora Global Database | Replica escala leitura na regiao; Global Database reduz latencia de leitura global e melhora DR cross-region |
| Backup vs replicacao | Backup restaura ponto no tempo; replicacao mantem copia ativa/quase ativa para leitura ou recuperacao |
| RDS Proxy vs aumentar banco | Proxy gerencia conexoes e pooling; nao resolve CPU, IO ou queries ruins |
| Read scaling vs HA | Replica de leitura melhora leitura; nao substitui failover automatico Multi-AZ |

## Tabela de decisao

| Cenario | Escolha provavel | Trade-off |
| --- | --- | --- |
| Alta disponibilidade em uma regiao | RDS Multi-AZ ou Aurora com replicas em AZs distintas | Custo maior que Single-AZ |
| Aplicacao read-heavy regional | Read replicas ou Aurora Replicas | Consistencia eventual para leituras |
| Leituras globais com baixa latencia | Aurora Global Database | Custo e complexidade multi-region |
| Recuperacao cross-region com baixo RPO | Aurora Global Database ou replica cross-region conforme engine | Failover regional exige processo claro |
| Picos de conexao vindos de Lambda | RDS Proxy | Nao aumenta capacidade de escrita |
| Menor overhead operacional | RDS/Aurora gerenciado, backups automaticos e manutencao planejada | Menos controle que banco autogerenciado |
| Aplicacao legada relacional | RDS engine compativel | Pode manter limitacoes antigas |
| Sistema financeiro global | Aurora Global Database ou desenho multi-region especifico | Consistencia e failover exigem cuidado extremo |

## Arquitetura de referencia

```text
Users
  |
Route 53
  |
Application
  |
  +-----------------------------+
  |                             |
Primary Region              Secondary Region
Aurora Primary  ----------> Aurora Secondary
     |
Aurora Replicas
```

Fluxo:

- Escritas entram no writer da regiao primaria.
- Leituras locais podem ir para Aurora Replicas na regiao primaria.
- Leituras globais podem ser atendidas pela regiao secundaria quando o desenho permite.
- Replicacao cross-region reduz RPO, mas nao elimina necessidade de runbook de failover.
- Em failover regional, a promocao do secundario e o redirecionamento via DNS/aplicacao precisam ser planejados.

## Raciocinio SAP-C02

### Cenario 1: banco regional critico

- Cenario: sistema transacional precisa sobreviver a falha de AZ.
- Restricoes: nao ha requisito de outra regiao; downtime deve ser minimo.
- Sinal: HA regional, nao DR global.
- Melhor decisao: RDS Multi-AZ ou Aurora com replicas em AZs distintas.
- Trade-off: custo adicional por standby/replicas, mas failover regional gerenciado.
- Por que nao alternativas: snapshot nao atende RTO baixo; read replica isolada nao e HA automatica em todos os cenarios.

### Cenario 2: trafego de leitura global

- Cenario: clientes na Europa e America do Norte fazem muitas consultas de catalogo.
- Restricoes: baixa latencia de leitura; escrita continua centralizada.
- Sinal: leitura global, nao write scaling horizontal generico.
- Melhor decisao: Aurora Global Database quando a aplicacao e compativel e precisa de replica regional de baixa latencia.
- Trade-off: custo e desenho multi-region, com consistencia eventual para regioes secundarias.

### Cenario 3: Lambda gera storm de conexoes

- Cenario: funcoes Lambda escalam rapidamente e abrem milhares de conexoes no banco.
- Restricoes: CPU do banco nao e o gargalo principal; falhas ocorrem por limite de conexoes.
- Sinal: problema de gerenciamento de conexoes.
- Melhor decisao: RDS Proxy.
- Trade-off: adiciona componente gerenciado e custo, mas estabiliza pooling e failover.

## Estudos Complementares

Use a trilha Associate apenas para revisar fundamentos de RDS, backups, replicas e Multi-AZ antes de aprofundar decisoes Professional:

https://github.com/Thiago-code-lab/aws-certified-solutions-architect-associate-brasil

## Arquivos do modulo

- [Questoes](questoes.md)
- [Flashcards](flashcards.md)
- [Cheatsheet](cheatsheet.md)
- [Casos de uso](casos-de-uso.md)
- [Links oficiais](links.md)
- [Lab guiado](lab.md)

---

CloudStudy - Trilha AWS Solutions Architect Professional
