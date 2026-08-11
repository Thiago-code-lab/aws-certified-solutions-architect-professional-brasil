# 17 - CloudFormation, CI/CD e Estrategias de Deployment

Este modulo ensina deployment architecture e gestao de risco operacional. No SAP-C02, IaC e CI/CD aparecem como mecanismos para reduzir drift, padronizar ambientes, controlar blast radius e escolher rollout/rollback conforme criticidade, compliance e velocidade de entrega.

## Objetivos

- Posicionar CloudFormation, stacks, nested stacks, StackSets, change sets, rollback e drift detection.
- Desenhar pipelines com CodePipeline/CodeBuild e roles cross-account.
- Escolher estrategias all-at-once, rolling, canary, blue/green e immutable.
- Planejar promocao dev -> staging -> prod, approvals e separacao de contas.
- Reduzir blast radius de deployments multi-account e multi-region.

## Comparacoes criticas

| Comparacao | Decisao Professional |
| --- | --- |
| Stack vs StackSets | Stack gerencia um escopo; StackSets distribui stacks por contas/regioes |
| Change set vs update direto | Change set mostra impacto antes de aplicar; update direto e mais rapido, mas menos controlado |
| Blue/green vs canary | Blue/green troca ambientes; canary libera pequena porcentagem e aumenta gradualmente |
| Canary vs rolling | Canary testa com pequena amostra; rolling substitui lotes ao longo do fleet |
| Immutable vs in-place | Immutable cria nova capacidade; in-place altera recursos existentes |
| Manual vs IaC | IaC cria rastreabilidade e repetibilidade; manual aumenta drift |
| Velocidade vs blast radius | Deploy rapido amplia impacto; rollout gradual reduz risco com mais tempo/custo |
| Rollback automatico vs intervencao manual | Automatico reduz MTTR; manual pode ser exigido em mudancas reguladas |

## Matriz de deployment

| Estrategia | Risco | Velocidade | Rollback | Custo temporario | Melhor cenario |
| --- | --- | --- | --- | --- | --- |
| All-at-once | Alto | Alta | Pode ser abrupto | Baixo | Ambientes nao criticos ou mudanca pequena |
| Rolling | Medio | Media | Reverte por lotes | Moderado | Aplicacoes tolerantes a versoes mistas |
| Canary | Baixo/medio | Media/baixa | Reverter antes de ampliar | Moderado | API com metricas claras e alto risco funcional |
| Blue/Green | Baixo/medio | Media | Troca de trafego para ambiente anterior | Alto | Zero/baixo downtime e rollback rapido |
| Immutable | Baixo | Media | Descartar nova capacidade | Alto | Infra/app onde estado local nao deve ser alterado |

## Exemplo multi-account

```text
Git Repository
      |
   Pipeline
      |
      +---- Dev Account
      |
      +---- Staging Account
      |
      +---- Production Account
                |
            Approval Gate
```

Fluxo:

1. Commit aciona pipeline.
2. CodeBuild/testes validam artefatos e templates.
3. Dev recebe deploy automatizado.
4. Staging valida integracao e smoke tests.
5. Production exige approval gate quando compliance ou risco pedem intervencao.
6. Roles cross-account limitam o que o pipeline pode alterar.
7. Change sets e rollback reduzem risco de infraestrutura.

## Raciocinio SAP-C02

### Cenario 1: 100 contas e padronizacao

- Cenario: uma organizacao precisa aplicar baseline de IAM, Config e logging em muitas contas.
- Restricoes: repetibilidade, governanca e multiplas regioes.
- Sinal: deployment organizacional de IaC.
- Melhor decisao: CloudFormation StackSets com permissoes apropriadas e controles de rollout.
- Trade-off: requer governanca de operacoes StackSets, mas reduz configuracao manual e drift.

### Cenario 2: API critica com mudanca arriscada

- Cenario: nova versao altera regra de precificacao.
- Restricoes: usuarios globais, erro caro e rollback rapido.
- Sinal: alto risco funcional com metricas observaveis.
- Melhor decisao: canary ou blue/green conforme capacidade de rotear trafego e manter versoes.
- Trade-off: menor risco, mas mais tempo, custo temporario e automacao de observabilidade.

### Cenario 3: producao regulada

- Cenario: deploys frequentes, mas producao exige aprovacao e evidencia.
- Restricoes: auditoria, segregacao de ambientes e rollback.
- Melhor decisao: pipeline multi-account com gates, change sets, logs de execucao e roles com menor privilegio.
- Trade-off: menos velocidade em prod, mais rastreabilidade.

## Estudos Complementares

Use a trilha Associate apenas para revisar fundamentos de CloudFormation, CodePipeline e deployment antes de aprofundar estrategias de rollout, rollback e governanca Professional:

https://github.com/Thiago-code-lab/aws-certified-solutions-architect-associate-brasil

## Arquivos do modulo

- [Questoes](questoes.md)
- [Flashcards](flashcards.md)
- [Cheatsheet](cheatsheet.md)
- [Casos de uso](casos-de-uso.md)
- [Referencias oficiais](links.md)
- [Workshop de deployment](lab.md)

---

CloudStudy - Trilha AWS Solutions Architect Professional
