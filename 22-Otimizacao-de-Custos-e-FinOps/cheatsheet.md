# Cheatsheet - FinOps e Otimizacao Arquitetural

| Sinal no cenario | Escolha provavel | Por que | Trade-off | Armadilha |
| --- | --- | --- | --- | --- |
| CFO pede custo por BU | Tags/contas/CUR/Budgets | Cria ownership | Governanca continua | Cortar sem saber dono |
| Baseline compute estavel | Savings Plans/RIs | Desconto em uso previsivel | Compromisso | Comprar para pico |
| Picos imprevisiveis | On-Demand/autoscaling | Flexibilidade | Custo maior | Comprometer uso incerto |
| Batch interruptivel | Spot | Baixo custo | Interrupcao | Usar sem retry |
| Banco ocioso | Rightsizing | Reduz desperdicio | Teste de performance | Diminuir sem metricas |
| S3 frio e volumoso | Lifecycle policies | Reduz storage | Custo/latencia de restore | Arquivar dado quente |
| Conta dev 24x7 | Scheduler + ownership | Quick win | Excecoes | Desligar recurso critico |
| Alto custo NAT/transfer | Redesenho de fluxo/endpoints/cache | Ataca driver real | Mudanca arquitetural | Olhar so EC2 |
| Servico autogerenciado caro em operacao | Managed service | Reduz toil | Preco unitario maior | Comparar so infra |

## Ordem de decisao

1. Medir.
2. Alocar.
3. Identificar drivers.
4. Remover ocioso.
5. Rightsizing.
6. Otimizar arquitetura.
7. Assumir commitments.
8. Monitorar anomalias.
