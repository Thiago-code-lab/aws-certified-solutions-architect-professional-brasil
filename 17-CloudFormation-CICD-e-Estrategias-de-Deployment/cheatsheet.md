# Cheatsheet - Deployment e IaC

| Sinal no cenario | Escolha provavel | Por que | Trade-off | Armadilha |
| --- | --- | --- | --- | --- |
| Muitas contas/regioes | StackSets | Distribui stacks em escala | Governanca de operacoes | Criar manualmente por conta |
| Revisar impacto antes | Change set | Mostra mudancas planejadas | Mais etapa no processo | Atualizar direto recurso critico |
| Suspeita de mudanca manual | Drift detection | Compara IaC e estado real | Nao corrige sozinho | Confundir com rollback |
| Alto risco funcional | Canary | Reduz blast radius inicial | Mais lento | Sem metricas para decidir |
| Rollback rapido e ambiente duplicado permitido | Blue/green | Alterna trafego | Custo temporario alto | Esquecer estado/dados |
| Fleet tolera versoes mistas | Rolling | Troca por lotes | Rollback pode ser gradual | Usar se versoes forem incompativeis |
| Evitar mutacao in-place | Immutable | Cria nova capacidade | Custo temporario | Estado local preso em instancias |
| Producao regulada | Approval gate | Evidencia e controle | Menor velocidade | Aprovar sem validar change set |

## Pipeline seguro

1. Validar template e testes.
2. Criar artefato imutavel.
3. Deploy automatico em dev.
4. Promover para staging.
5. Criar change set para prod.
6. Approval gate quando exigido.
7. Deploy com estrategia adequada.
8. Monitorar metricas e executar rollback se necessario.
