# Mini Simulados por Dominio

## Design Solutions for Organizational Complexity - 26%

1. Landing zone com autonomia e governanca central. **Resposta:** multi-account com OUs, SCPs e logging centralizado.
2. Acesso temporario via provedor corporativo. **Resposta:** IAM Identity Center com permission sets.
3. Compartilhamento controlado de recursos entre contas. **Resposta:** AWS RAM quando aplicavel.

## Design for New Solutions - 29%

4. Conteudo global com baixa latencia. **Resposta:** CloudFront e desenho de origem.
5. Consumidores processam pedidos em ritmos diferentes. **Resposta:** Amazon SQS.
6. Containers com menos administracao de servidores. **Resposta:** AWS Fargate quando requisitos permitirem.

## Continuous Improvement for Existing Solutions - 25%

7. Custo sem rastreabilidade por produto. **Resposta:** tags, Cost Explorer e Budgets.
8. Deteccao de ameacas em varias contas. **Resposta:** GuardDuty e Security Hub com administracao delegada.
9. Limite regional antes de evento de alto trafego. **Resposta:** revisar Service Quotas, testar carga e solicitar aumento.

## Accelerate Workload Migration and Modernization - 20%

10. Migracao grande com dependencias desconhecidas. **Resposta:** discovery e assessment.
11. Banco precisa migrar com replicacao continua. **Resposta:** AWS DMS.
12. Grande volume de dados com link restrito. **Resposta:** DataSync ou Snow Family conforme volume e conectividade.

---

Continue seus estudos na CloudStudy:

[https://cloudstudy.com.br](https://cloudstudy.com.br)
