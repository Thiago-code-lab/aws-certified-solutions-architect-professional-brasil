# Flashcards - Disaster Recovery

1. **O que e RTO?**
   Tempo maximo aceitavel para restaurar um servico apos interrupcao.

2. **O que e RPO?**
   Quantidade maxima aceitavel de perda de dados medida no tempo.

3. **Quando usar Backup & Restore?**
   Para workloads com RTO/RPO menos agressivos e forte pressao de custo.

4. **O que e Pilot Light?**
   Dados e componentes minimos ficam prontos na regiao de DR; compute completo sobe durante o desastre.

5. **O que e Warm Standby?**
   Ambiente reduzido ja executa na regiao secundaria e escala no failover.

6. **O que e Active-Active/Multi-Site?**
   Duas ou mais regioes atendem trafego simultaneamente, exigindo desenho cuidadoso de dados e operacao.

7. **Multi-AZ substitui Multi-Region?**
   Nao. Multi-AZ melhora disponibilidade dentro de uma regiao; Multi-Region trata desastre regional.

8. **Quando AWS Backup e forte?**
   Politicas centralizadas, copias cross-account/cross-region, retenÃ§Ã£o, auditoria e restauracao de recursos suportados.

9. **Quando Elastic Disaster Recovery e forte?**
   Recuperacao de servidores com replicacao continua e lancamento rapido de instancias em regiao alvo.

10. **Qual componente e critico para failover publico?**
    Route 53 com health checks, failover records ou politicas de roteamento adequadas.

11. **Por que testar DR?**
    Porque backup sem restauracao validada e apenas uma hipotese operacional.

12. **Qual risco de DR sem IaC?**
    Recuperacao lenta, inconsistente e dependente de operacao manual em crise.
