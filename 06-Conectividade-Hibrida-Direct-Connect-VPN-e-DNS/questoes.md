# Questoes - Conectividade Hibrida

## Questao 1

Uma empresa precisa conectar centenas de workloads em varias contas AWS ao data center com baixa variacao de latencia. Qual arquitetura atende melhor?

A) VPN por VPC.
B) Direct Connect para DXGW associado a Transit Gateway central.
C) Peering entre todas as VPCs.
D) PrivateLink para todo trafego.

<details><summary><strong>Ver resposta</strong></summary>

**Resposta correta:** B

DX entrega previsibilidade e DXGW/TGW escalam multi-account. As outras opcoes nao escalam ou servem outro objetivo.
</details>

## Questao 2

Instituicao financeira exige link dedicado e criptografia controlada entre on-premises e AWS. O que escolher?

A) Direct Connect sozinho.
B) Direct Connect com VPN sobre o caminho ou MACsec quando aplicavel.
C) Internet Gateway.
D) VPC Peering.

<details><summary><strong>Ver resposta</strong></summary>

**Resposta correta:** B

DX dedicado nao deve ser confundido automaticamente com criptografia fim a fim. A ignora requisito; C e D nao atendem.
</details>

## Questao 3

ERP usa DX primario e aceita modo degradado, mas nao indisponibilidade total. Qual desenho e melhor?

A) Um unico DX.
B) DX redundante ou VPN backup com BGP, preferencia de rota e teste de failover.
C) Mais EC2.
D) NAT adicional.

<details><summary><strong>Ver resposta</strong></summary>

**Resposta correta:** B

O risco e caminho hibrido. Backup precisa ser roteavel, testado e dimensionado. C e D nao resolvem falha de conectividade.
</details>

## Questao 4

AWS precisa resolver `corp.local` e on-premises precisa resolver nomes privados AWS. O que usar?

A) Apenas private hosted zones.
B) Resolver outbound para AWS -> on-prem e inbound para on-prem -> AWS.
C) Public hosted zones.
D) Copia manual.

<details><summary><strong>Ver resposta</strong></summary>

**Resposta correta:** B

Inbound e outbound tratam direcoes diferentes. As demais opcoes sao incompletas, inseguras ou pouco operaveis.
</details>

## Questao 5

Como evitar alcance lateral entre producao e desenvolvimento em conectividade hibrida compartilhada?

A) Uma route table TGW propagando tudo.
B) TGW com route tables por dominio e propagacao seletiva.
C) Peering total.
D) Uma VPC unica.

<details><summary><strong>Ver resposta</strong></summary>

**Resposta correta:** B

Route tables separadas controlam rotas aprendidas por cada dominio. As demais ampliam blast radius.
</details>
