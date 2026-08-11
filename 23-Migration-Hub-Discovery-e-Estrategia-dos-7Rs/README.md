# 23 - Migration Hub, Discovery e Estrategia dos 7Rs

Este modulo trata migracao como decisao de portfolio antes de ferramenta. No SAP-C02, o ponto central e reconhecer negocio, dependencias, prazo, risco, licenciamento, downtime, divida tecnica e prontidao da landing zone para escolher a estrategia correta entre os 7Rs.

## Objetivos

- Conduzir discovery de portfolio e dependencias antes de selecionar ferramenta.
- Usar AWS Migration Hub, Application Discovery Service, Migration Evaluator e TCO quando apropriado.
- Planejar waves de migracao com base em criticidade, dependencia, risco e valor.
- Aplicar os 7Rs: Retire, Retain, Rehost, Relocate, Replatform, Repurchase, Refactor/Re-architect.
- Explicar por que uma estrategia foi escolhida e por que as alternativas foram rejeitadas.

## Mental model Professional

```text
Scenario
  -> constraints
  -> architectural signal
  -> options
  -> best decision
  -> trade-off
  -> why not the alternatives
```

## 7Rs orientados por decisao

| Pergunta | Sinal | R provavel | Cuidado |
| --- | --- | --- | --- |
| O workload ainda e necessario? | Sem dono, sem uso, duplicado | Retire | Validar impacto antes de desligar |
| Deve ficar onde esta por compliance, latencia ou contrato? | Bloqueio temporario real | Retain | Reavaliar depois; nao virar adiamento eterno |
| Pode mover com mudanca minima e prazo agressivo? | Baixa dependencia, app estavel | Rehost | Pode carregar divida tecnica |
| Pode mudar plataforma sem redesenhar app? | Banco/servidor compativel com gerenciado | Replatform | Testar compatibilidade e performance |
| Existe SaaS que substitui melhor? | Software comercial comum | Repurchase | Migracao de dados e processos |
| Business value justifica redesign? | Escala, agilidade, custo ou resiliencia exigem mudanca | Refactor/Re-architect | Maior custo, prazo e risco |
| Workload VMware pode mover como plataforma? | Ambiente VMware e requisito de rapidez | Relocate | Mantem modelo operacional semelhante |

## Exemplo de portfolio e waves

| Aplicacao | Perfil | R provavel | Wave | Racional |
| --- | --- | --- | --- | --- |
| A | Baixa dependencia, baixa criticidade | Rehost | Wave 1 | Bom candidato para validar landing zone e processo |
| B | Depende de banco compartilhado, criticidade media | Replatform | Wave 2 | Banco gerenciado reduz operacao, mas dependencia exige sequenciamento |
| C | Monolito legado, alto valor de negocio | Refactor/Re-architect | Wave 3+ | Modernizacao justificada, mas precisa discovery profundo e roadmap |
| D | Ferramenta interna obsoleta | Retire | Antes da Wave 1 | Evita migrar o que nao gera valor |
| E | Software comercial disponivel como SaaS | Repurchase | Wave 2 | Reduz operacao, mas exige avaliacao de dados, usuarios e contrato |

## Raciocinio SAP-C02

### Cenario 1: data-center exit com prazo fixo

- Cenario: contrato do data center vence em 12 meses.
- Restricoes: prazo domina; nem todos os apps podem ser modernizados.
- Sinal: migracao em waves com quick wins e baixa mudanca.
- Melhor decisao: discovery, agrupamento por dependencia, landing zone pronta, rehost/replatform para workloads aptos e retain para bloqueios reais.
- Trade-off: parte da divida tecnica continua, mas o risco de prazo cai.
- Por que nao alternativas: refatorar tudo antes da saida aumenta risco; migrar sem discovery quebra dependencias.

### Cenario 2: aquisicao

- Cenario: empresa adquirida tem portfolio desconhecido, licencas distintas e apps duplicados.
- Restricoes: consolidar custo e reduzir redundancia sem interromper negocio.
- Melhor decisao: assessment, dependencia, TCO e classificacao: retire duplicados, repurchase softwares comuns, retain bloqueados e migrar waves de baixo risco primeiro.
- Trade-off: analise inicial demora, mas evita migracao desnecessaria.

### Cenario 3: monolito critico

- Cenario: monolito gera receita, tem deploy lento e escala irregular.
- Restricoes: baixo downtime, alto valor de modernizacao, dependencias complexas.
- Melhor decisao: decompor roadmap; talvez replatform inicial para reduzir operacao e refactor gradual de dominios de maior valor.
- Trade-off: abordagem faseada reduz risco, mas demora mais que rehost simples.

## Estudos Complementares

Este modulo e inerentemente Professional. Use documentacao oficial e prescriptive guidance para validar estrategia, discovery, readiness e wave planning. Nao ha recomendacao cross-repository generica para esta fase.

## Arquivos do modulo

- [Questoes](questoes.md)
- [Flashcards](flashcards.md)
- [Cheatsheet](cheatsheet.md)
- [Casos de uso](casos-de-uso.md)
- [Links oficiais](links.md)
- [Workshop de migracao](lab.md)

---

CloudStudy - Trilha AWS Solutions Architect Professional
