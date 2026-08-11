# Cheatsheet - Conectividade Hibrida

| Sinal no cenario | Escolha provavel | Por que | Trade-off | Armadilha |
| --- | --- | --- | --- | --- |
| Prazo curto e baixo custo | Site-to-Site VPN | Rapida de iniciar | Internet publica e menor previsibilidade | Virar solucao permanente sem revisar |
| Alto throughput previsivel | Direct Connect | Caminho dedicado | Lead time/custo | Usar uma conexao unica |
| Requisito de criptografia | VPN sobre DX ou MACsec quando aplicavel | Atende compliance de trafego criptografado | Complexidade | Achar que DX criptografa por padrao |
| Muitas VPCs/contas | TGW em conta de rede | Hub escalavel e segmentado | Custo e governanca | Criar conexoes por VPC |
| Uma VPC simples | VGW | Simples e direto | Pouca escala | Forcar TGW sem necessidade |
| DX para multiplos ambientes | DXGW + TGW/VGW conforme desenho | Reuso de conectividade dedicada | Regras e limites precisam ser validados | Confundir DXGW com roteador de VPCs |
| AWS resolve DNS corporativo | Resolver outbound | Encaminha para DNS on-prem | Endpoints/regras | Criar public zones indevidas |
| On-prem resolve nomes AWS | Resolver inbound | Expoe entrada de resolucao privada | Controle de rede e SG | Copiar registros manualmente |
| Failover de conectividade | DX + VPN backup com BGP | Caminho alternativo | Testes e convergencia | Backup nunca testado |

## Checklist de desenho

- Qual e o SLA de conectividade?
- O trafego exige criptografia alem de conectividade dedicada?
- Quantas VPCs, contas e regioes participam?
- Quem administra rotas: conta de rede, time local ou cada workload?
- Como DNS resolve nos dois sentidos?
- Existe teste de falha de DX, VPN e DNS?
- O custo do TGW, DX, VPN e endpoints foi considerado?
