# Cheatsheet - Modernization

| Cue | Choice | Rationale | Trade-off | Pitfall |
| --- | --- | --- | --- | --- |
| Aggressive deadline | Rehost/replatform | Lower change risk | Technical debt remains | Full refactor |
| Critical monolith | Strangler | Migration by domain | Coexistence | Big bang |
| Independent peaks | SQS/EventBridge | Decoupling | Eventual consistency | Longer timeouts |
| Stateful workflow | Step Functions | Orchestration | Workflow modeling | Scattered state |
| Small team | Lambda/Fargate | Less operational effort | Service limits | EKS without maturity |
| Mature Kubernetes capabilities | EKS | Control | Operational effort | Following trends |
| Stateless API | Lambda/Fargate | Scaling | Observability | Retaining unnecessary monolith coupling |
| Regulated domain | Retain temporarily | Avoids change risk | Partial modernization | Changing it only for symmetry |
| Long-running process | Container | Control | Operational effort | Forcing Lambda |
| Many consumers | EventBridge | Rule-based routing | Add queues when consumers require buffering | Using a single SQS queue for broadcast |
