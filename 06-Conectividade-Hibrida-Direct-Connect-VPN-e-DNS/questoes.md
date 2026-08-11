# Questoes - Conectividade Hibrida

## Questao 1

Uma empresa possui um data center corporativo e centenas de workloads em varias contas AWS. O trafego entre o ERP on-premises e aplicacoes em producao exige throughput previsivel, baixa variabilidade de latencia e segmentacao entre producao e desenvolvimento.

Qual arquitetura e mais adequada?

A. Uma Site-to-Site VPN por VPC, sem Transit Gateway.
B. Direct Connect integrado a uma conta central de rede, com Direct Connect Gateway/Transit Gateway e route tables segmentadas.
C. VPC Peering entre todas as VPCs e o data center.
D. NAT Gateway central para rotear trafego privado ao data center.

<details>
<summary><strong>Ver resposta</strong></summary>

**Resposta correta:** B

**Por que esta correta:** o cenario combina alto throughput, previsibilidade, muitas contas/VPCs e segmentacao. DX com TGW em conta de rede escala melhor e permite governanca de rotas.

**Por que as alternativas sao mais fracas:** A aumenta operacao e nao entrega previsibilidade de DX; C nao conecta diretamente data center e nao escala como hub; D nao e mecanismo de conectividade privada hibrida.

</details>

## Questao 2

Uma instituicao financeira quer conectividade dedicada ao data center, mas a area de compliance exige criptografia em transito para trafego sensivel entre on-premises e AWS.

Qual decisao deve ser considerada?

A. Direct Connect sozinho, pois circuito dedicado sempre criptografa trafego IP.
B. Direct Connect com camada de criptografia, como VPN sobre DX ou MACsec quando aplicavel.
C. Apenas Internet Gateway nas VPCs privadas.
D. Route 53 Resolver outbound endpoint.

<details>
<summary><strong>Ver resposta</strong></summary>

**Resposta correta:** B

**Por que esta correta:** DX oferece conectividade dedicada, mas a exigencia de criptografia precisa ser atendida por mecanismo adicional apropriado.

**Por que as alternativas sao mais fracas:** A confunde dedicado com criptografado; C expoe caminho inadequado; D resolve DNS, nao criptografia de trafego.

</details>

## Questao 3

Uma empresa usa Direct Connect como caminho primario para AWS. Durante falha no circuito, os sistemas precisam continuar acessando workloads criticos com degradacao aceitavel e convergencia automatizada de rotas.

Qual desenho atende melhor?

A. Direct Connect unico sem caminho alternativo.
B. VPN Site-to-Site como backup, com BGP e preferencia de rotas configurada para DX primario.
C. Criar snapshots dos servidores on-premises.
D. Usar apenas Resolver inbound endpoint.

<details>
<summary><strong>Ver resposta</strong></summary>

**Resposta correta:** B

**Por que esta correta:** VPN backup fornece caminho alternativo e BGP permite troca/convergencia de rotas conforme o desenho.

**Por que as alternativas sao mais fracas:** A nao e resiliente; C e backup de dados/servidores, nao conectividade; D trata DNS, nao caminho de rede.

</details>

## Questao 4

Workloads em AWS precisam resolver nomes `corp.local` mantidos no Active Directory DNS on-premises. Servidores no data center tambem precisam resolver nomes privados de aplicacoes em VPCs AWS.

Qual combinacao e mais adequada?

A. Route 53 Resolver outbound endpoint para consultas AWS -> on-prem e inbound endpoint para on-prem -> AWS.
B. Apenas public hosted zones no Route 53.
C. Apenas NAT Gateway nas sub-redes privadas.
D. Apenas Security Hub em todas as contas.

<details>
<summary><strong>Ver resposta</strong></summary>

**Resposta correta:** A

**Por que esta correta:** outbound encaminha consultas da AWS para DNS on-prem; inbound permite que on-prem consulte zonas privadas AWS.

**Por que as alternativas sao mais fracas:** B torna nomes publicos e nao resolve DNS privado hibrido; C e saida de rede, nao DNS; D e seguranca, nao resolucao.

</details>

## Questao 5

Uma organizacao opera workloads em duas regioes e dezenas de VPCs. Ela quer conectar o data center sem criar conectividade ponto a ponto para cada VPC e precisa manter controle central de rotas.

Qual opcao e mais defensavel?

A. Direct Connect Gateway associado a Transit Gateway conforme o desenho regional, com TGW route tables por dominio.
B. Uma VPN manual para cada subnet.
C. Copiar as zonas privadas para o DNS on-premises e nao criar conectividade.
D. Criar IAM roles cross-account para transportar trafego.

<details>
<summary><strong>Ver resposta</strong></summary>

**Resposta correta:** A

**Por que esta correta:** DXGW/TGW permitem conectividade centralizada e roteamento escalavel para multiplas VPCs/regioes conforme suporte e desenho.

**Por que as alternativas sao mais fracas:** B nao escala; C resolve no maximo nomes, nao trafego; D IAM nao transporta rede.

</details>
