# Cheatsheet - Redes Avancadas

## Escolha rapida

| Necessidade | Servico/padrao |
| --- | --- |
| Muitas VPCs e contas com roteamento central | Transit Gateway |
| Duas ou poucas VPCs com comunicacao direta | VPC Peering |
| Expor apenas uma aplicacao privada | PrivateLink |
| Conexao dedicada com datacenter | Direct Connect |
| Backup criptografado de conectividade hibrida | VPN Site-to-Site |
| Resolver nomes entre AWS e on-premises | Route 53 Resolver endpoints |
| Acesso privado a servicos AWS | Gateway/interface VPC endpoints |

## Transit Gateway

- Use attachments por VPC, VPN ou Direct Connect Gateway.
- Separe route tables por dominio de seguranca.
- Associe cada attachment a uma route table.
- Propague rotas apenas onde houver necessidade.
- Para inspeção, modele ida e retorno pela inspection VPC.
- Monitore bytes processados, rotas, propagacoes e limites regionais.

## VPC Peering

- Nao e transitivo.
- Nao suporta CIDRs sobrepostos.
- E simples para poucas conexoes.
- Pode ficar ingovernavel em malha completa.
- Exige rotas explicitas nos dois lados.

## PrivateLink

- Usa endpoint service no provedor e interface endpoint no consumidor.
- O consumidor acessa DNS privado do endpoint, nao a rede inteira do provedor.
- Ideal para SaaS interno, servicos compartilhados e integracao com parceiros.
- Nao substitui TGW para conectividade bidirecional ampla.

## Perguntas de prova

- Existe necessidade de transitive routing?
- Quantas VPCs e contas participam?
- O trafego e para uma rede inteira ou para um servico especifico?
- Ha CIDRs sobrepostos?
- O modelo exige inspeção centralizada?
- O custo por GB do caminho centralizado e aceitavel?
- O caminho de retorno passa pelo mesmo firewall?

## Armadilhas comuns

- Usar peering para arquitetura multi-account grande.
- Usar TGW quando PrivateLink resolveria exposicao de um unico servico.
- Centralizar todo egress sem avaliar vazao e custo.
- Ignorar DNS em arquiteturas hibridas.
- Permitir propagacao ampla de rotas no TGW por conveniencia operacional.
