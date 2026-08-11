# Cheatsheet - Modernizacao

| Sinal no cenario | Escolha provavel | Por que | Trade-off | Armadilha |
| --- | --- | --- | --- | --- |
| Prazo curto, app estavel | Rehost/replatform | Menor risco inicial | Pouca melhoria | Chamar de modernizacao completa |
| Monolito critico e lento | Strangler pattern | Migra por fatias | Convivencia legado/novo | Big-bang rewrite |
| Picos e retry | SQS + consumidores | Buffer e desacoplamento | Consistencia eventual | Processar tudo sincrono |
| Eventos entre dominios | EventBridge | Roteamento desacoplado | Governanca de schemas | Uma fila para tudo |
| Workflow com etapas | Step Functions | Orquestracao visivel | Custo/definicao | Logica distribuida sem controle |
| Funcoes curtas/eventos | Lambda | Baixa operacao e escala | Limites/runtime | Usar para processo longo |
| Servico stateless containerizado | ECS/Fargate | Menor operacao | Menos controle de host | EKS sem necessidade |
| Kubernetes maduro | EKS | Ecossistema e portabilidade | Mais operacao | Subestimar plataforma |
| Equipe pequena | Managed/serverless primeiro | Reduz toil | Menos controle fino | Autogerenciar por habito |

## Checklist de modernizacao

- Qual parte do monolito muda mais?
- Qual parte e estavel e pode ficar para depois?
- O limite precisa ser sincrono ou assincrono?
- Quem e dono de cada novo servico?
- Como dados serao compartilhados ou separados?
- Qual e o rollback de uma fatia migrada?
- O time consegue operar a tecnologia escolhida?
