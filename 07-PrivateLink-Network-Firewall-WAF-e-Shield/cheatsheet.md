# Guia Rápido

## Critérios de decisão

| Sinal do cenário | Decisão esperada | Risco ao ignorar |
|---|---|---|
| Múltiplas contas ou unidades de negócio | Considerar governança, acesso e limites por conta | Arquitetura sem controle centralizado |
| Requisito de continuidade | Validar RTO/RPO, failover e testes | Recuperação incompatível com o negócio |
| Ambiente híbrido ou global | Avaliar conectividade, DNS, latência e roteamento | Ponto único de falha ou latência alta |
| Pressão de custo | Comparar custo recorrente, operação e transferência de dados | Economia local que aumenta custo total |

## Checklist de revisão

- Qual requisito domina a decisão?
- A solução escala para contas, regiões e times envolvidos?
- Existe rastreabilidade operacional e de segurança?
- A complexidade proposta é necessária para o cenário?
