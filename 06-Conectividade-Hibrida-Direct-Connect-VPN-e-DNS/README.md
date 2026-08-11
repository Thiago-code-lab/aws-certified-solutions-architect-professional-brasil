# 06 - Conectividade Hibrida, Direct Connect, VPN e DNS

Este modulo aprofunda decisoes de conectividade entre data centers corporativos e AWS. O foco do SAP-C02 nao e configurar BGP em detalhe, mas escolher o desenho correto quando requisitos de latencia, throughput, criptografia, resiliencia, prazo de provisionamento, custo, DNS e operacao multi-account competem entre si.

## Objetivos

- Escolher entre AWS Direct Connect, Site-to-Site VPN e combinacoes DX + VPN.
- Posicionar Direct Connect Gateway, Transit Gateway e Virtual Private Gateway.
- Projetar conectividade resiliente com caminhos redundantes e VPN como backup.
- Explicar BGP em nivel arquitetural: troca de rotas, preferencia de caminhos e failover.
- Desenhar DNS hibrido com Route 53 Resolver inbound/outbound endpoints e forwarding rules.
- Integrar conectividade em conta central de rede para multiplas contas, VPCs e ambientes.

## Comparacoes criticas

| Comparacao | Decisao Professional |
| --- | --- |
| Direct Connect vs Site-to-Site VPN | DX entrega conectividade dedicada e previsivel; VPN e mais rapida/barata de iniciar, mas usa internet publica |
| Direct Connect + VPN backup | Padrao para combinar previsibilidade com caminho alternativo criptografado |
| Direct Connect Gateway vs Transit Gateway | DXGW conecta DX a VPCs/TGW entre regioes; TGW centraliza roteamento entre VPCs/VPN/DX attachments |
| VGW vs TGW | VGW serve conectividade mais simples por VPC; TGW escala para muitas VPCs/contas e segmentacao |
| Public internet VPN vs dedicated connectivity | VPN depende da internet; DX reduz variabilidade de latencia e throughput |
| Resolver inbound vs outbound | Inbound permite on-prem consultar nomes privados AWS; outbound permite AWS encaminhar consultas para DNS on-prem |
| AWS DNS vs forwarding on-prem | Resolucao local AWS cobre recursos privados; forwarding e necessario para dominios corporativos externos a AWS |
| Single connection vs resilient design | Uma conexao reduz custo, mas nao atende alta disponibilidade empresarial |

## Arquitetura base

```text
             Corporate Data Center
                     |
              Direct Connect
                     |
             Direct Connect GW
                     |
                     v
              Transit Gateway
              /      |       \
             /       |        \
        Prod VPC   Dev VPC   Shared VPC
```

Uso tipico:

- DX fornece caminho primario dedicado.
- DXGW permite associar conectividade dedicada a ambientes em diferentes regioes conforme o desenho.
- TGW centraliza roteamento para multiplas VPCs e contas.
- Route tables do TGW segmentam producao, desenvolvimento e shared services.

## Arquitetura resiliente

```text
        Data Center
        /        \
      DX          VPN
      |            |
      +---- AWS connectivity ----+
                  |
                 TGW
```

Comportamento esperado:

- DX e caminho preferencial para trafego normal quando os anuncios de rota e politicas BGP favorecem esse caminho.
- VPN funciona como caminho alternativo, frequentemente com menor preferencia.
- Em falha do DX, rotas via VPN podem assumir conforme convergencia e configuracao.
- A solucao melhora resiliencia, mas adiciona custo, complexidade de roteamento e necessidade de testes de failover.

## DNS hibrido

### On-premises para AWS private DNS

```text
On-prem DNS
    |
    | consulta app.internal.aws
    v
Route 53 Resolver inbound endpoint
    |
Private hosted zone / AWS private names
```

Use inbound endpoints quando servidores on-premises precisam resolver nomes privados hospedados na AWS.

### AWS para DNS corporativo

```text
AWS workload
    |
    | consulta corp.local
    v
Route 53 Resolver outbound endpoint
    |
Forwarding rule
    |
On-prem DNS
```

Use outbound endpoints e regras de encaminhamento quando workloads AWS precisam resolver dominios mantidos no DNS corporativo. Em ambientes multi-account, uma conta de shared services/networking pode centralizar endpoints e compartilhar regras quando o modelo organizacional permitir.

## Tabela de decisao

| Cenario | Arquitetura recomendada | Por que | Trade-off | Armadilha |
| --- | --- | --- | --- | --- |
| Conectividade temporaria para migracao | Site-to-Site VPN | Provisionamento rapido e baixo custo inicial | Menos previsivel que DX | Usar como solucao permanente para alto throughput |
| Empresa com alto throughput previsivel | Direct Connect redundante | Conectividade dedicada e latencia mais consistente | Lead time e custo | Assumir que uma unica conexao e resiliente |
| Criptografia exigida sobre conectividade | DX + VPN ou MACsec quando aplicavel | DX sozinho nao implica criptografia IPsec | Mais complexidade | Confundir circuito dedicado com trafego criptografado |
| DX com backup resiliente | DX primario + VPN backup | Balanceia previsibilidade e contingencia | Teste de failover obrigatorio | Nao ajustar preferencia de rotas |
| Muitas VPCs | DX integrado a TGW | Escala roteamento hub-and-spoke | Custo de TGW/attachments | Criar VGW por VPC sem governanca |
| Muitas contas | Conta central de rede + TGW | Governanca e segmentacao | Mais operacao central | Misturar workloads na conta de rede |
| DNS hibrido | Resolver inbound/outbound endpoints | Resolve nomes AWS/on-prem nos dois sentidos | Custo e regras compartilhadas | Resolver IP sem plano de forwarding |
| Baixo custo e prazo curto | VPN | Evita lead time de DX | Internet publica e limites de throughput | Ignorar requisitos de latencia |
| Workload regulado | DX redundante + criptografia + logs | Previsibilidade e controles auditaveis | Custo alto | Achar que DX elimina necessidade de criptografia |
| App sensivel a latencia | DX com redundancia | Menor variabilidade | Provisionamento demorado | Usar VPN pela rapidez e falhar SLA |

## Estudos Complementares

Use a trilha Associate apenas para revisar VPC, route tables, VPN e Route 53 basicos antes de estudar decisoes hibridas Professional:

https://github.com/Thiago-code-lab/aws-certified-solutions-architect-associate-brasil

## Arquivos do modulo

- [Questoes](questoes.md)
- [Flashcards](flashcards.md)
- [Cheatsheet](cheatsheet.md)
- [Casos de uso](casos-de-uso.md)
- [Referencias oficiais](links.md)
- [Workshop de conectividade](lab.md)

---

CloudStudy - Trilha AWS Solutions Architect Professional
