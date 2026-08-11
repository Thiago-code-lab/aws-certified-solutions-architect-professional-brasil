# Questoes - Redes Avancadas

## 1. Conectividade entre 80 VPCs e datacenter

Uma empresa possui 80 VPCs distribuidas em 20 contas. Todas precisam acessar alguns sistemas on-premises por Direct Connect, mas os ambientes de producao e desenvolvimento nao devem se comunicar entre si. A equipe quer reduzir operacao manual de rotas.

Qual desenho atende melhor ao cenario?

A. Criar VPC Peering entre todas as VPCs e propagar rotas via tabelas locais.
B. Usar Transit Gateway com attachments por VPC e route tables separadas por ambiente.
C. Criar PrivateLink entre todas as VPCs e o datacenter.
D. Usar NAT Gateway central para rotear todo o trafego privado.

**Resposta:** B

**Justificativa:** Transit Gateway suporta conectividade transitive e segmentacao por route tables. Peering nao escala bem e nao e transitivo. PrivateLink e para exposicao privada de servicos, nao para conectividade geral com datacenter. NAT Gateway nao substitui roteamento privado.

## 2. Servico compartilhado sem acesso a rede do provedor

Uma plataforma interna oferece uma API de billing para varias contas consumidoras. Os consumidores devem acessar apenas a API, sem rotas para bancos, caches ou sub-redes do provedor.

Qual opcao reduz melhor o blast radius?

A. VPC Peering com security groups restritivos.
B. Transit Gateway com route table compartilhada.
C. AWS PrivateLink com endpoint service publicado atras de NLB.
D. VPN Site-to-Site entre as contas consumidoras.

**Resposta:** C

**Justificativa:** PrivateLink permite acesso privado a um servico especifico sem conectividade ampla entre redes. Security groups ajudam, mas peering/TGW ainda expÃµem um plano de conectividade mais amplo.

## 3. InspeÃ§Ã£o centralizada com firewall stateful

Uma organizacao exige que todo egress de VPCs de producao passe por inspeÃ§Ã£o stateful em uma VPC de seguranca. A equipe observou perda de conexoes em testes por retorno assimetrico.

Qual decisao arquitetural e mais importante?

A. Usar uma unica route table do TGW para todos os attachments.
B. Garantir rotas simetricas de ida e volta pela inspection VPC.
C. Substituir TGW por VPC Peering para evitar custo por GB.
D. Criar endpoints S3 Gateway em todas as VPCs e remover firewalls.

**Resposta:** B

**Justificativa:** Firewalls stateful exigem caminho simetrico. TGW route tables devem direcionar ida e retorno pelo mesmo ponto de inspeÃ§Ã£o. Uma unica route table aumenta alcance lateral e nao resolve assimetria.

## 4. CIDR sobreposto apos aquisicao

Uma empresa adquiriu outra organizacao e descobriu que varias VPCs usam CIDRs sobrepostos. Elas precisam consumir um servico privado central durante a fase de integracao.

Qual abordagem e mais adequada no curto prazo?

A. Conectar todas as VPCs ao mesmo TGW e aceitar rotas sobrepostas.
B. Usar VPC Peering entre as VPCs com CIDR igual.
C. Expor o servico via PrivateLink para consumidores autorizados.
D. Usar propagacao automatica de rotas para resolver o conflito.

**Resposta:** C

**Justificativa:** TGW e peering nao resolvem CIDRs sobrepostos para conectividade roteada. PrivateLink evita dependencia de roteamento entre CIDRs e permite consumo privado do servico.

## 5. Alto volume de trafego leste-oeste

Duas VPCs na mesma regiao trocam grande volume de dados continuamente. Nao ha requisito de conectividade com outras VPCs e a topologia deve permanecer simples.

Qual escolha tende a ser mais apropriada?

A. VPC Peering direto entre as duas VPCs.
B. Transit Gateway com inspection VPC obrigatoria.
C. PrivateLink para todos os protocolos bidirecionais.
D. Direct Connect Gateway entre VPCs.

**Resposta:** A

**Justificativa:** Para poucas VPCs com comunicacao direta e previsivel, peering pode ser mais simples e economico. TGW se justifica quando ha escala, roteamento central, segmentacao ou conectividade hibrida.
