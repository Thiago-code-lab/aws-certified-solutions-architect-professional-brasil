# Casos de Uso - Deployment e IaC

## Cenario 1 - Baseline em multiplas contas

### Contexto

Uma organizacao quer habilitar recursos padrao de governanca em dezenas de contas e regioes.

### Requisitos

- Repetibilidade.
- Controle central.
- Baixo drift.
- Atualizacoes rastreaveis.

### Arquitetura recomendada

CloudFormation StackSets com escopo controlado, roles adequadas e rollout por lotes.

### Por que

StackSets resolvem distribuicao multi-account/multi-region sem scripts manuais por conta.

### Trade-offs

Exige processo de mudanca, permissao correta e teste em OU piloto.

### Por que nao as alternativas

Stacks manuais geram drift; scripts sem governanca dificultam auditoria; management account nao deve virar conta operacional geral.

### Sinal de prova

"many accounts", "same baseline", "multi-region".

## Cenario 2 - Release de alto risco em API publica

### Contexto

Uma API publica muda regra de elegibilidade de compra e erro pode impactar receita.

### Requisitos

- Reduzir blast radius.
- Medir erro/conversao.
- Reverter rapidamente.

### Arquitetura recomendada

Canary deployment com metricas, alarmes e rollback; blue/green se a necessidade principal for troca rapida entre ambientes completos.

### Por que

O risco funcional exige exposicao gradual e decisao baseada em sinais.

### Trade-offs

Mais tempo de release, automacao e monitoramento.

### Por que nao as alternativas

All-at-once aumenta impacto; deploy manual nao oferece rastreabilidade; rolling pode expor mais usuarios se a mudanca for muito arriscada.

### Sinal de prova

"small percentage of traffic", "observe metrics", "high-risk change".

## Cenario 3 - Producao regulada

### Contexto

Uma plataforma financeira faz releases frequentes, mas producao exige aprovacao e evidencia.

### Requisitos

- Dev, staging e prod separados.
- Menor privilegio.
- Aprovacao antes de producao.
- Rollback documentado.

### Arquitetura recomendada

Pipeline multi-account com CodePipeline/CodeBuild, roles cross-account, change sets, approval gate e logs de execucao.

### Por que

Separa ambientes e combina automacao com controle regulatorio.

### Trade-offs

Producao fica menos automatica que ambientes inferiores, mas a auditoria melhora.

### Por que nao as alternativas

Usuario compartilhado quebra rastreabilidade; deploy local de laptop aumenta risco; permissao ampla do pipeline expande blast radius.

### Sinal de prova

"regulated production", "approval", "multi-account promotion".
