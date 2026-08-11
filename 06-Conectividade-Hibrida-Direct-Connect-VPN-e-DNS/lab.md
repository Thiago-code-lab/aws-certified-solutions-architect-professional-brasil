# Workshop - Desenho de Conectividade Hibrida

> Exercicio de arquitetura. Nao provisione recursos AWS.

## Cenario

Uma empresa possui data center em Sao Paulo, Active Directory DNS interno, ERP critico on-premises e tres contas AWS: Production, Development e Shared Services. Cada conta possui multiplas VPCs. A conectividade precisa ser resiliente e permitir crescimento para novos workloads.

## Tarefa 1 - Escolher DX/VPN

Defina:

- Caminho primario.
- Caminho secundario.
- Onde VPN entra no desenho.
- Se criptografia adicional e necessaria.

Explique por que Direct Connect, VPN ou combinacao DX + VPN atende melhor.

## Tarefa 2 - Posicionar DXGW, TGW e contas

Preencha:

| Componente | Conta/local | Responsabilidade |
| --- | --- | --- |
| Direct Connect |  |  |
| Direct Connect Gateway |  |  |
| Transit Gateway |  |  |
| Route tables do TGW |  |  |
| Resolver endpoints |  |  |

## Tarefa 3 - Desenhar DNS hibrido

Fluxo on-prem -> AWS:

```text
AD DNS -> Resolver inbound endpoint -> Private hosted zone
```

Fluxo AWS -> on-prem:

```text
Workload AWS -> Resolver outbound endpoint -> forwarding rule -> AD DNS
```

Defina quais dominios usam forwarding e onde as regras sao administradas.

## Tarefa 4 - Rotas e segmentacao

Explique conceitualmente:

- Como prod acessa ERP.
- Como dev e limitado.
- Como shared services acessa DNS e ferramentas.
- Quais rotas nao devem ser propagadas.

## Tarefa 5 - Comportamento em falhas

Descreva:

- Falha do DX.
- Falha da VPN.
- Falha de um Resolver endpoint/AZ.
- Rota incorreta propagada para dev.

## Entrega esperada

- Diagrama final.
- Justificativa DX/VPN.
- Posicionamento DXGW/TGW.
- Fluxos DNS inbound/outbound.
- Politica de segmentacao de rotas.
- Trade-offs de custo, resiliencia, lead time e complexidade.
- Alternativas rejeitadas e motivo.
