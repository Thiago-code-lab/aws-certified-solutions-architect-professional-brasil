# Referencias Oficiais

## Essencial

- [AWS Direct Connect User Guide](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html) - Cobre conectividade dedicada, gateways e conceitos de DX; prioridade alta para cenarios de throughput e latencia.
- [AWS Site-to-Site VPN User Guide](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html) - Explica VPN gerenciada e opcoes de roteamento; importante para conectividade temporaria e backup.
- [AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html) - Base para entender o hub de conectividade de muitas VPCs/contas.

## Aprofundamento

- [Direct Connect gateways](https://docs.aws.amazon.com/directconnect/latest/UserGuide/direct-connect-gateways-intro.html) - Leitura para posicionar DXGW em desenhos multi-VPC/multi-Region.
- [Site-to-Site VPN routing options](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPNRoutingTypes.html) - Ajuda a raciocinar BGP, rotas dinamicas e failover.
- [Route 53 Resolver](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver.html) - Essencial para DNS hibrido inbound/outbound.

## Referencia

- [Transit Gateway route tables](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-route-tables.html) - Use para validar segmentacao de rotas.
- [Virtual private gateways](https://docs.aws.amazon.com/vpn/latest/s2svpn/vpn-concepts.html) - Referencia para posicionar VGW em cenarios simples.
- [AWS Direct Connect resiliency recommendations](https://docs.aws.amazon.com/directconnect/latest/UserGuide/resiliency_toolkit.html) - Prioridade para desenhos resilientes.
