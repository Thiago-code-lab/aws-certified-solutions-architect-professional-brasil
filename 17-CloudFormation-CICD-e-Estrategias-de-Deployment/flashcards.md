# Flashcards - Deployment e IaC

1. **Quando StackSets e melhor que stack simples?**
   Quando a mesma infraestrutura precisa ser implantada em multiplas contas ou regioes.

2. **Quando usar change set?**
   Quando a equipe precisa revisar impacto antes de aplicar atualizacao CloudFormation.

3. **Quando drift detection e util?**
   Quando ha suspeita de mudanca manual ou divergencia entre IaC e estado real.

4. **Quando canary supera all-at-once?**
   Quando uma mudanca arriscada pode ser exposta gradualmente com metricas de decisao.

5. **Quando blue/green e forte?**
   Quando rollback rapido e baixo downtime justificam manter ambiente paralelo temporario.

6. **Quando rolling e aceitavel?**
   Quando a aplicacao tolera versoes mistas e substituicao gradual de instancias/tasks.

7. **Quando immutable supera in-place?**
   Quando alterar recursos existentes aumenta risco e nova capacidade pode ser criada e validada.

8. **Qual sinal aponta para approval gate?**
   Compliance, producao regulada, alto risco financeiro ou necessidade de aprovacao formal.

9. **Por que IaC reduz risco?**
   Porque torna mudancas versionadas, repetiveis, revisaveis e menos dependentes de passos manuais.

10. **Qual risco de pipeline com permissao ampla?**
    Um erro de automacao pode alterar muitos recursos/contas; roles devem limitar blast radius.
