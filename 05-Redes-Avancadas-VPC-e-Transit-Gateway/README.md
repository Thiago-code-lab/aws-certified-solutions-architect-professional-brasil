# 05 - Redes Avancadas: VPC, Transit Gateway e PrivateLink

Este modulo aprofunda decisoes de conectividade cobradas no SAP-C02: quando centralizar roteamento com AWS Transit Gateway, quando manter conectividade ponto a ponto com VPC Peering, quando expor servicos via AWS PrivateLink e como projetar redes hibridas com isolamento, observabilidade e limites operacionais claros.

## Objetivos

- Escolher entre Transit Gateway, VPC Peering e PrivateLink com base em escala, isolamento, rotas, custo e modelo operacional.
- Projetar arquiteturas hub-and-spoke, multi-account e hibridas com segmentacao por ambiente, dominio ou sensibilidade.
- Aplicar tabelas de rotas do TGW, attachments, propagacao seletiva e inspeção centralizada sem criar alcance lateral indevido.
- Avaliar Direct Connect, VPN Site-to-Site, DNS privado, endpoints VPC e padroes de egress centralizado.
- Reconhecer trade-offs de disponibilidade, custo por GB, complexidade de operacao e blast radius.

## Comparacao de conectividade

| Padrao | Melhor uso | Forca | Limitacao |
| --- | --- | --- | --- |
| Transit Gateway | Muitas VPCs, contas e redes on-premises | Roteamento central, segmentacao por route tables, escala operacional | Custo por attachment/processamento e desenho exige governanca de rotas |
| VPC Peering | Poucas VPCs com trafego direto e previsivel | Simples, baixa latencia, sem appliance central | Sem transitive routing; escala vira malha dificil de governar |
| PrivateLink | Consumir/prover servicos privados sem abrir rede | Isola consumidor e provedor; nao exige rotas entre CIDRs | Unidirecional por servico; nao substitui conectividade geral |

## Arquitetura de referencia

```text
                         On-premises
                             |
                     Direct Connect / VPN
                             |
                       DX Gateway / VPN
                             |
                      +----------------+
                      | Transit Gateway|
                      +----------------+
                       /       |       \
                      /        |        \
             Route table   Route table   Route table
              shared       prod          security
                 |           |             |
          +------+--+   +----+----+   +----+------+
          | Shared  |   | Prod VPC|   | Inspection |
          | Services|   | Apps    |   | VPC        |
          +---------+   +---------+   +------------+
                |             |              |
          Private hosted  Interface     Network Firewall
          zones / DNS     endpoints     egress controls
```

## Raciocinio SAP-C02

### Cenario 1: cem VPCs em multiplas contas

- Cenario: a empresa tem dezenas de contas por unidade de negocio, ambientes separados e conectividade on-premises.
- Restricao: VPC Peering criaria uma malha de rotas dificil de auditar e nao permitiria transitive routing.
- Decisao: usar Transit Gateway com route tables por dominio, propagacao seletiva e attachments gerenciados por conta de rede.
- Trade-off: o custo por attachment e processamento aumenta, mas a arquitetura ganha governanca, segmentacao e operacao previsivel.

### Cenario 2: exposicao de servico interno para parceiros

- Cenario: uma equipe precisa expor uma API privada para VPCs de outras contas sem permitir acesso a sub-redes internas.
- Restricao: peering ou TGW criariam conectividade de rede mais ampla do que o necessario.
- Decisao: publicar o servico com PrivateLink, usando endpoint service com NLB e controles de principals permitidos.
- Trade-off: PrivateLink resolve o consumo de um servico especifico, mas nao serve para roteamento bidirecional generico.

### Cenario 3: inspeção centralizada de trafego

- Cenario: todo egress de workloads produtivos deve passar por firewall gerenciado.
- Restricao: rotas assimetricas quebram inspeção stateful e aumentam risco operacional.
- Decisao: usar TGW route tables direcionando spoke VPCs para uma inspection VPC com AWS Network Firewall ou appliances em GWLB.
- Trade-off: a inspeção central simplifica compliance, mas adiciona dependencia regional e custo por trafego processado.

## Padroes de desenho

- Separe route tables do TGW por finalidade: producao, nao producao, shared services, inspeção e conectividade on-premises.
- Evite propagacao automatica ampla; associe e propague rotas de forma explicita.
- Planeje CIDRs sem sobreposicao antes de escalar multi-account; TGW nao corrige enderecamento ruim.
- Use Route 53 Resolver endpoints para integracao DNS hibrida.
- Prefira endpoints VPC para servicos AWS acessados de forma privada, reduzindo dependencia de NAT para chamadas internas.
- Centralize egress somente quando houver requisito de controle; para workloads de alta vazao, avalie custo e latencia.

## Estudos Complementares

- Revise fundamentos de VPC, sub-redes, route tables, NAT Gateway e endpoints no repositório Associate quando precisar reforcar base operacional.
- Neste modulo, foque a decisao Professional: escala multi-account, segmentacao, conectividade hibrida, inspeção centralizada e trade-offs de custo.

## Arquivos do modulo

- [Questoes](questoes.md)
- [Flashcards](flashcards.md)
- [Cheatsheet](cheatsheet.md)
- [Casos de uso](casos-de-uso.md)
- [Links oficiais](links.md)
- [Lab guiado](lab.md)

---

CloudStudy - Trilha AWS Solutions Architect Professional
