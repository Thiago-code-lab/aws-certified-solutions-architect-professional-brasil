# Casos de Uso - Conectividade Hibrida

## Cenario 1 - ERP on-premises integrado a workloads AWS

### Contexto

Uma empresa mantem ERP no data center e moderniza aplicacoes satelite em contas AWS de producao e desenvolvimento.

### Requisitos

- Baixa variabilidade de latencia.
- Alto throughput em horario comercial.
- Separacao entre prod e dev.
- DNS corporativo integrado.

### Arquitetura recomendada

Direct Connect redundante para conta central de rede, Direct Connect Gateway, Transit Gateway com route tables segmentadas e Route 53 Resolver inbound/outbound.

### Por que

O requisito mistura previsibilidade, escala multi-account e DNS hibrido. Uma malha de VPNs por VPC aumentaria operacao.

### Trade-offs

Maior custo e prazo de provisionamento, mas melhor governanca e previsibilidade.

### Por que nao as alternativas

VPN isolada por VPC nao escala; VGW por workload reduz governanca central; public DNS nao resolve nomes privados com seguranca.

### Sinal de prova

"ERP on-premises", "many AWS accounts", "predictable latency".

## Cenario 2 - Migracao temporaria com prazo curto

### Contexto

Um projeto de migracao precisa conectar data center e AWS em poucas semanas para replicacao inicial de dados.

### Requisitos

- Baixo custo inicial.
- Inicio rapido.
- Trafego moderado.
- Solucao pode ser substituida depois.

### Arquitetura recomendada

Site-to-Site VPN com BGP, monitoramento e plano para evoluir para Direct Connect se o trafego se tornar permanente/critico.

### Por que

O prazo e mais importante que previsibilidade maxima.

### Trade-offs

Menor custo e lead time, mas dependencia de internet publica e throughput menos previsivel.

### Por que nao as alternativas

Esperar DX pode atrasar migracao; criar links manuais por workload dificulta governanca.

### Sinal de prova

"temporary", "migration deadline", "moderate traffic".

## Cenario 3 - DNS hibrido com Active Directory

### Contexto

Aplicacoes AWS precisam consultar `corp.local`, e usuarios on-premises precisam acessar nomes privados de servicos AWS.

### Requisitos

- Manter AD DNS como autoridade corporativa.
- Resolver private hosted zones da AWS.
- Evitar registros duplicados manuais.

### Arquitetura recomendada

Route 53 Resolver outbound endpoint com forwarding rules para `corp.local` e inbound endpoint para consultas on-premises aos nomes privados AWS.

### Por que

Resolver endpoints resolvem o problema bidirecional sem tornar nomes privados publicos.

### Trade-offs

Exige conectividade de rede, security groups, regras de encaminhamento e governanca de contas.

### Por que nao as alternativas

Public hosted zones expõem nomes indevidos; editar hosts files nao escala; NAT Gateway nao resolve DNS hibrido.

### Sinal de prova

"Active Directory DNS", "private hosted zone", "both directions".
