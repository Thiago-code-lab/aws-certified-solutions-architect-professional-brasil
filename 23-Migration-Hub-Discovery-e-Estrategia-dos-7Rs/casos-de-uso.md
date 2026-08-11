# Casos de Uso - Estrategia de Migracao

## Cenario 1 - Saida de data center empresarial

### Contexto

Uma empresa precisa sair de dois data centers em 12 meses e possui centenas de aplicacoes com documentacao incompleta.

### Requisitos

- Cumprir prazo contratual.
- Evitar interrupcao de sistemas criticos.
- Reduzir migracao desnecessaria.
- Preparar landing zone.

### Arquitetura recomendada

Assessment de portfolio, Application Discovery Service para dependencias, Migration Hub para acompanhamento, classificacao 7Rs e waves por dependencia/risco.

### Por que

O problema dominante e coordenacao de portfolio sob prazo. Ferramenta de migracao vem depois da estrategia.

### Trade-offs

Discovery consome tempo inicial, mas reduz retrabalho e indisponibilidade.

### Por que nao as alternativas

Rehost de tudo migra divida e apps desnecessarios; refactor amplo estoura prazo; migrar sem waves quebra dependencias.

### Sinal de prova

"data center exit", "many applications", "unknown dependencies".

## Cenario 2 - Consolidacao apos M&A

### Contexto

Uma empresa adquiriu outra e encontrou sistemas duplicados, contratos de software diferentes e workloads sem dono claro.

### Requisitos

- Reduzir custo.
- Consolidar portfolio.
- Preservar operacao critica.
- Identificar redundancias.

### Arquitetura recomendada

Portfolio assessment com Retire para duplicados sem uso, Repurchase para software comum com SaaS viavel, Retain para bloqueios contratuais e waves para migracao dos sistemas restantes.

### Por que

M&A normalmente exige racionalizacao antes de migrar.

### Trade-offs

Decisoes de retire/repurchase dependem de dono de negocio e gestao de mudanca.

### Por que nao as alternativas

Migrar tudo aumenta custo; replatform sem consolidar perpetua redundancia; retain permanente impede captura de sinergia.

### Sinal de prova

"acquisition", "duplicate applications", "license consolidation".

## Cenario 3 - Modernizacao de monolito critico

### Contexto

Um monolito de pedidos e essencial para receita, mas possui deploy lento, baixa resiliencia e custo operacional alto.

### Requisitos

- Baixo downtime.
- Melhor agilidade.
- Reduzir risco gradualmente.
- Justificar investimento.

### Arquitetura recomendada

Plano faseado: discovery de dominios, possivel replatform inicial para reduzir operacao, strangler pattern e refactor/re-architect dos dominios de maior valor.

### Por que

O valor de negocio justifica modernizacao, mas criticidade exige migracao incremental.

### Trade-offs

Maior duracao e governanca de arquitetura, mas menor risco que big bang.

### Por que nao as alternativas

Rehost preserva gargalos; rewrite completo aumenta risco; retire e inviavel para sistema critico.

### Sinal de prova

"critical monolith", "business agility", "phased modernization".
