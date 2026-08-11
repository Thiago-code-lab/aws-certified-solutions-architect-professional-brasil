# Cheatsheet - Modernizacao

| Sinal | Escolha | Por que | Trade-off | Armadilha |
| --- | --- | --- | --- | --- |
| Prazo agressivo | Rehost/replatform | Menor risco | Divida continua | Refactor total |
| Monolito critico | Strangler | Migra por dominio | Convivencia | Big-bang |
| Picos independentes | SQS/EventBridge | Desacopla | Consistencia eventual | Timeout maior |
| Workflow com estado | Step Functions | Orquestracao | Modelagem | Estado espalhado |
| Time pequeno | Lambda/Fargate | Menos operacao | Limites | EKS sem maturidade |
| Kubernetes maduro | EKS | Controle | Operacao | Usar por moda |
| API stateless | Lambda/Fargate | Escala | Observabilidade | Manter monolito |
| Dominio regulado | Manter temporario | Evita risco | Modernizacao parcial | Mexer por simetria |
| Runtime longo | Container | Controle | Operacao | Forcar Lambda |
| Muitos consumidores | EventBridge | Roteamento | Sem fila principal | SQS para broadcast complexo |
