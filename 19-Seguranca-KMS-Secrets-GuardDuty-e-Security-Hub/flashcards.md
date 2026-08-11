# Flashcards - Seguranca Centralizada

1. **Quando KMS key policy e mais importante que IAM policy?**
   Sempre que a chave precisa permitir ou negar uso/admin; IAM so funciona dentro dos limites permitidos pela key policy.

2. **Quando Secrets Manager e preferivel a Parameter Store?**
   Quando ha segredo sensivel com rotacao, auditoria e integracao gerenciada com bancos ou aplicacoes.

3. **Quando Parameter Store ainda faz sentido?**
   Para configuracoes e parametros hierarquicos; SecureString pode servir segredos simples sem rotacao gerenciada completa.

4. **Quando GuardDuty e o servico certo?**
   Quando o requisito envolve deteccao de ameacas, comportamento anomalo, credenciais comprometidas ou atividade suspeita.

5. **Quando Security Hub entra na arquitetura?**
   Quando findings de multiplas contas e servicos precisam ser agregados, normalizados e priorizados.

6. **Quando AWS Config e mais adequado que Security Hub?**
   Quando o objetivo e avaliar estado/configuracao de recursos contra regras.

7. **Quando Inspector e mais adequado que GuardDuty?**
   Quando o foco e vulnerabilidade em EC2, imagens de container ou workloads suportados.

8. **Quando Macie e relevante?**
   Quando o requisito e descobrir ou monitorar dados sensiveis em S3.

9. **Por que usar delegated administrator?**
   Para operar servicos organizacionais em uma conta especializada, sem transformar a management account em conta operacional.

10. **Qual cuidado com remediacao automatizada?**
    Automatizar contencao sem contexto pode causar indisponibilidade; use severidade, escopo e aprovacoes quando necessario.
