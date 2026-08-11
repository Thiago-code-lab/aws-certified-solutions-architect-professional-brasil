# Lab Guiado - Arquitetura de Rede com TGW e PrivateLink

> Lab de arquitetura. Nao execute em conta real sem revisar custo de TGW, NAT Gateway, endpoints e trafego processado.

## Objetivo

Desenhar uma rede multi-account com conectividade central via Transit Gateway, inspeção opcional de egress e exposicao de um servico compartilhado via PrivateLink.

## Topologia alvo

```text
Accounts:

network-account
  Transit Gateway
  Route tables: prod, nonprod, shared, inspection

security-account
  Inspection VPC
  AWS Network Firewall
  Central logging

shared-services-account
  Shared Services VPC
  NLB + Endpoint Service
  Route 53 Resolver endpoints

app-prod-account
  Prod VPC
  Interface endpoint to shared service
  TGW attachment

app-dev-account
  Dev VPC
  TGW attachment with isolated nonprod routes
```

## Passo 1 - Definir enderecamento

Crie uma tabela de CIDRs sem sobreposicao:

| VPC | CIDR exemplo | Observacao |
| --- | --- | --- |
| Prod | 10.10.0.0/16 | Workloads criticos |
| Dev | 10.20.0.0/16 | Sem rota para prod |
| Shared | 10.30.0.0/16 | DNS, ferramentas, servicos comuns |
| Inspection | 10.40.0.0/16 | Firewalls e egress |
| On-premises | 172.16.0.0/16 | Via DX/VPN |

Checkpoint: nenhum CIDR pode se sobrepor.

## Passo 2 - Modelar route tables do TGW

Crie route tables logicas:

- `rt-prod`: recebe rotas de prod, shared, inspection e on-premises autorizadas.
- `rt-nonprod`: recebe dev e shared, sem rota para prod.
- `rt-shared`: permite retorno para prod e nonprod conforme necessidade.
- `rt-inspection`: concentra rotas de retorno para spokes.

Decisao: nao habilite propagacao irrestrita. O objetivo e demonstrar isolamento.

## Passo 3 - Definir caminho de inspeção

Para egress produtivo:

1. Sub-redes privadas de prod apontam default route para o TGW.
2. `rt-prod` aponta `0.0.0.0/0` para inspection VPC.
3. Inspection VPC envia trafego ao firewall e depois ao NAT/Internet Gateway.
4. Rotas de retorno passam novamente pela inspection VPC.

Checkpoint: confirme simetria. Firewalls stateful falham com retorno assimetrico.

## Passo 4 - Publicar servico via PrivateLink

No shared-services-account:

1. Coloque a aplicacao atras de um Network Load Balancer.
2. Crie um endpoint service PrivateLink.
3. Permita principals das contas consumidoras.
4. Habilite DNS privado se o dominio for controlado e validado.

Nas contas consumidoras:

1. Crie interface endpoints nas sub-redes privadas.
2. Aplique security groups permitindo apenas portas necessarias.
3. Teste resolucao DNS e conectividade.

Checkpoint: consumidores acessam o servico, mas nao recebem rota para o CIDR da VPC provedora.

## Passo 5 - Validar decisoes

- Prod alcanca shared services?
- Dev permanece isolado de prod?
- On-premises alcanca apenas redes autorizadas?
- Egress produtivo passa por inspeção?
- Servico compartilhado e acessivel por PrivateLink sem peering?
- Existe dependencia desnecessaria de NAT para servicos AWS que poderiam usar endpoints?

## Resultado esperado

Ao final, a arquitetura deve explicar:

- Por que TGW foi usado para conectividade ampla.
- Por que PrivateLink foi usado para exposicao de servico.
- Onde a segmentacao e aplicada.
- Qual custo/complexidade adicional foi aceito em troca de governanca.
