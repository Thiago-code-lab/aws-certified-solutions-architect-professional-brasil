# Flashcards - FinOps

1. **Quando comprar Savings Plans ou RIs?**
   Depois de medir e ajustar o baseline previsivel; compromisso nao deve cristalizar desperdicio.

2. **Quando Spot e melhor que On-Demand?**
   Quando o workload tolera interrupcao, retry e variacao de capacidade.

3. **Quando On-Demand continua correto?**
   Quando demanda e imprevisivel, critica ou ainda nao possui baseline confiavel.

4. **Por que rightsizing vem antes de commitment?**
   Porque desconto em recurso superdimensionado ainda preserva desperdicio.

5. **Quando Budgets e melhor que Cost Explorer?**
   Para alertar e acompanhar limites; Cost Explorer e melhor para analise historica/tendencia.

6. **Quando tags nao bastam?**
   Quando a separacao de ownership exige contas/OUs distintas, controles e billing boundaries claros.

7. **Qual sinal aponta para storage lifecycle?**
   Dados antigos, grande volume, padrao de acesso frio e requisito de retencao.

8. **Por que olhar data transfer?**
   Porque trafego inter-AZ, inter-region, NAT e internet pode dominar custo mesmo com compute otimizado.

9. **Quando gerenciado pode ser mais barato no total?**
   Quando reduz operacao, incidentes, patching e capacidade ociosa, apesar do preco unitario.

10. **Qual risco de corte de custo sem SLA?**
    Reduzir capacidade, backup ou redundancia pode economizar agora e criar indisponibilidade cara.
