# Mini Simulados por Domínio

## Como usar

- Resolva por domínio oficial do SAP-C02.
- Leia o enunciado procurando restrição dominante, exceções e objetivos de negócio.
- Corrija imediatamente e registre padrões de erro no caderno.

## Bloco A: Organizational Complexity

1. Uma empresa multinacional quer centralizar governança sem impedir autonomia das unidades de negócio. Qual decisão deve ser priorizada?
A) Uma única conta para todos os workloads.
B) Estratégia multi-account com OUs, guardrails e logging centralizado.
C) Usuários IAM locais em cada workload.
D) Remover auditoria para reduzir operação.

<details>
<summary><strong>Ver resposta</strong></summary>

✅ **Resposta correta:** B

**Explicação:** SAP-C02 favorece desenho organizacional escalável com separação de responsabilidades, governança e rastreabilidade.

</details>

## Bloco B: New Solutions

2. Uma aplicação global exige baixa latência e failover controlado. Qual família de decisões deve ser avaliada?
A) Roteamento global, edge, replicação de dados e estratégia multi-Region.
B) Apenas aumentar uma instância EC2.
C) Criar backups manuais sem teste.
D) Desabilitar observabilidade para reduzir custo.

<details>
<summary><strong>Ver resposta</strong></summary>

✅ **Resposta correta:** A

**Explicação:** O cenário combina latência, disponibilidade e continuidade, exigindo análise de arquitetura global.

</details>
