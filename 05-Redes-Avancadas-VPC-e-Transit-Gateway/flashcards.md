# Flashcards - Redes Avancadas

1. **Quando escolher Transit Gateway?**
   Quando muitas VPCs, contas ou redes on-premises precisam de conectividade centralizada com segmentacao e roteamento transitive.

2. **Quando VPC Peering e suficiente?**
   Quando poucas VPCs precisam se comunicar diretamente, sem roteamento transitivo e sem grande complexidade operacional.

3. **Quando PrivateLink e a melhor resposta?**
   Quando consumidores precisam acessar um servico privado especifico sem receber rotas para a rede do provedor.

4. **Qual o risco de propagacao automatica ampla no TGW?**
   Ela pode criar alcance lateral indesejado entre ambientes ou unidades de negocio.

5. **O que sao TGW route tables?**
   Sao tabelas que controlam quais attachments podem alcancar quais destinos, permitindo segmentacao no hub.

6. **Por que CIDR planning e critico?**
   CIDRs sobrepostos impedem conectividade roteada previsivel entre VPCs, TGW e redes on-premises.

7. **Como integrar DNS hibrido?**
   Com Route 53 Resolver inbound/outbound endpoints e regras compartilhadas conforme o modelo multi-account.

8. **Qual cuidado com firewall stateful centralizado?**
   Garantir caminhos simetricos para ida e volta do trafego.

9. **Quando usar endpoints VPC?**
   Para acessar servicos AWS privadamente, reduzindo exposicao a internet e dependencia de NAT Gateway para chamadas internas.

10. **Qual trade-off do egress centralizado?**
    Ele melhora controle e auditoria, mas adiciona custo, latencia e dependencia de uma VPC central.
