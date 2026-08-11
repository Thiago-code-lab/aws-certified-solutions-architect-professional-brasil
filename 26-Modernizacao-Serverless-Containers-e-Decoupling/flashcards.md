# Flashcards - Modernizacao

1. **Quando strangler supera big-bang rewrite?**
   Quando o sistema e critico, o negocio precisa de valor incremental e uma reescrita concentraria risco.

2. **Quando rehost e aceitavel antes de modernizar?**
   Quando prazo ou risco de data center domina e o workload nao tem dor arquitetural urgente.

3. **Quando replatform supera refactor?**
   Quando trocar a plataforma reduz operacao sem exigir redesign profundo da aplicacao.

4. **Quando usar SQS?**
   Quando o objetivo e fila, buffering, retry e desacoplamento ponto a ponto.

5. **Quando usar EventBridge?**
   Quando eventos de dominios diferentes precisam ser roteados para multiplos consumidores desacoplados.

6. **Quando Lambda e adequado?**
   Para tarefas orientadas a evento, curtas, elásticas e com baixo desejo de operar servidores.

7. **Quando containers sao melhores que Lambda?**
   Quando ha runtime customizado, processos longos, controle de ambiente ou portabilidade de empacotamento.

8. **Quando ECS e melhor que EKS?**
   Quando o time quer containers com menor operacao e nao precisa do ecossistema Kubernetes.

9. **Quando EKS se justifica?**
   Quando a organizacao ja tem plataforma Kubernetes, ferramentas e requisitos que compensam a operacao.

10. **Qual risco de desacoplamento mal feito?**
    Consistencia eventual, duplicidade e ordenacao podem quebrar regras se idempotencia nao for planejada.
