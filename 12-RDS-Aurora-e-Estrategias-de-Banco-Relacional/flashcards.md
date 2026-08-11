# Flashcards - RDS e Aurora

1. **Quando Multi-AZ e preferivel a read replica?**
   Quando o requisito principal e failover/alta disponibilidade dentro da regiao.

2. **Quando read replica e preferivel a Multi-AZ?**
   Quando o gargalo principal e leitura e a aplicacao aceita consistencia eventual.

3. **Quando Aurora Global Database entra na decisao?**
   Quando ha leitura global, DR cross-region com baixo RPO ou necessidade de replica regional rapida.

4. **Quando RDS tradicional e melhor que Aurora?**
   Quando a aplicacao exige engine especifica, compatibilidade legada ou simplicidade operacional suficiente.

5. **Por que backup nao substitui replicacao?**
   Backup restaura um ponto no tempo; replicacao mantem copia mais proxima do estado atual para leitura ou recuperacao.

6. **Quando usar RDS Proxy?**
   Quando o problema e excesso de conexoes, failover de conexoes ou workloads serverless com alta concorrencia.

7. **Por que RDS Proxy nao resolve write scaling?**
   Ele gerencia conexoes; nao transforma uma engine relacional em escritor horizontal ilimitado.

8. **Quando Multi-AZ nao basta?**
   Quando o requisito menciona desastre regional, usuarios globais ou failover para outra regiao.

9. **Qual sinal indica problema de leitura, nao HA?**
   Queries de leitura saturam o writer, mas o requisito nao fala em falha de AZ.

10. **Qual risco em failover cross-region?**
    Promocao, DNS, consistencia, aplicacao e failback precisam ser coordenados.
