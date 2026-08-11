# Lab Guiado - Exercicio de Desenho Relacional Global

> Este lab e um exercicio de arquitetura. Nao provisione recursos AWS.

## Cenario

Uma empresa global de comercio opera na America do Norte e Europa. A regiao primaria recebe alto volume de escrita para pedidos, pagamentos e estoque. Clientes em ambas as regioes consultam catalogo e historico com baixa latencia. A empresa tem requisitos rigorosos de disponibilidade, baixa tolerancia a perda de dados e restricoes de custo.

## Decisoes obrigatorias

Preencha cada item com escolha, justificativa e alternativa rejeitada.

| Decisao | Escolha | Justificativa | Alternativa rejeitada |
| --- | --- | --- | --- |
| 1. RDS ou Aurora |  |  |  |
| 2. Estrategia Multi-AZ |  |  |  |
| 3. Estrategia de leitura |  |  |  |
| 4. Estrategia cross-region |  |  |  |
| 5. Backup |  |  |  |
| 6. Failover |  |  |  |
| 7. Conexoes |  |  |  |
| 8. Custo vs resiliencia |  |  |  |

## Arquitetura base para avaliar

```text
North America users        Europe users
        |                      |
        +------ Route 53 ------+
                  |
             Application
                  |
        +---------+----------+
        |                    |
Primary Region         Secondary Region
Aurora writer  ----->  Aurora global secondary
Aurora replicas        Read endpoint
RDS Proxy              Scaled application tier
AWS Backup copy        Backup vault
```

## Passo 1 - Identificar requisito dominante

Classifique:

- Escrita: concentrada ou multi-writer?
- Leitura: regional ou global?
- RTO/RPO: baixo, medio ou relaxado?
- Consistencia: quais leituras toleram atraso?
- Custo: qual capacidade pode ficar ativa fora da regiao primaria?

## Passo 2 - Escolher mecanismo relacional

Compare:

- RDS tradicional: compatibilidade de engine, menor mudanca para legado.
- Aurora: replicas rapidas, arquitetura de cluster, Global Database.

Explique por que sua escolha atende melhor ao conjunto de restricoes.

## Passo 3 - Desenhar HA regional

Defina como a regiao primaria sobrevive a falha de AZ:

- Multi-AZ para RDS.
- Aurora replicas em multiplas AZs para Aurora.
- Teste de failover e comportamento da aplicacao.

## Passo 4 - Desenhar leitura e DR

Decida:

- Endpoint de leitura regional.
- Regiao secundaria para leitura global.
- Replicacao cross-region.
- Procedimento de promocao em desastre.

## Passo 5 - Tratar conexoes

Avalie RDS Proxy se:

- ha Lambda ou containers com alta elasticidade;
- o banco sofre com excesso de sessoes;
- failover precisa reduzir erro de conexao.

## Entrega esperada

O estudante deve entregar:

- Diagrama final.
- Tabela de decisoes preenchida.
- Riscos de consistencia e failover.
- Estrategia de backup e restauracao.
- Explicacao de custo/resiliencia.
- Razoes para rejeitar alternativas como Multi-AZ isolado, apenas snapshots ou replica de leitura sem plano de DR.
