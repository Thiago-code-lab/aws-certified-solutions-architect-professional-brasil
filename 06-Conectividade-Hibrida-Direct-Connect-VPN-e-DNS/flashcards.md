# Flashcards - Conectividade Hibrida

1. **Quando Direct Connect supera VPN?**
   Quando o requisito dominante e throughput previsivel, menor variabilidade de latencia ou conectividade empresarial dedicada.

2. **Quando Site-to-Site VPN e suficiente?**
   Quando a conectividade e temporaria, de menor custo, com prazo curto ou throughput moderado.

3. **Quando usar DX + VPN backup?**
   Quando DX deve ser caminho primario, mas a arquitetura precisa sobreviver a falha do circuito dedicado.

4. **Qual sinal aponta para Transit Gateway?**
   Muitas VPCs, contas, ambientes ou necessidade de segmentar rotas em um hub.

5. **Quando VGW ainda faz sentido?**
   Em conectividade mais simples e centrada em uma VPC, sem escala multi-account complexa.

6. **Qual papel do Direct Connect Gateway?**
   Facilitar associacao da conectividade DX a VPCs/TGWs em escopos regionais suportados, sem criar circuito por VPC.

7. **O que BGP sinaliza em questoes SAP-C02?**
   Troca dinamica de rotas, preferencia de caminhos e convergencia em falhas.

8. **Quando usar Resolver inbound endpoint?**
   Quando DNS on-premises precisa resolver nomes privados hospedados na AWS.

9. **Quando usar Resolver outbound endpoint?**
   Quando workloads AWS precisam encaminhar consultas para DNS corporativo on-premises.

10. **Qual armadilha sobre Direct Connect e criptografia?**
    Circuito dedicado nao significa automaticamente trafego criptografado; requisitos de compliance podem exigir camada adicional.
