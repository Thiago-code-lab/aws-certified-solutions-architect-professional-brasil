# Cheatsheet - 7Rs e Wave Planning

| Sinal no cenario | Escolha provavel | Por que | Trade-off | Armadilha |
| --- | --- | --- | --- | --- |
| Sem uso, duplicado ou sem dono | Retire | Evita migrar custo inutil | Exige validacao de impacto | Desligar sem confirmar dependencias |
| Bloqueio temporario real | Retain | Respeita contrato/compliance/dependencia | Mantem legado | Virar adiamento indefinido |
| Prazo curto e baixa mudanca | Rehost | Reduz risco de prazo | Carrega divida tecnica | Chamar de modernizacao |
| Banco/servidor pode virar gerenciado | Replatform | Reduz operacao sem redesign total | Testes de compatibilidade | Subestimar tuning |
| SaaS substitui software comum | Repurchase | Remove operacao de plataforma | Mudanca de processo/dados | Ignorar lock-in e compliance |
| Alto valor exige novo desenho | Refactor/Re-architect | Ataca causa raiz | Maior custo e risco | Refatorar tudo sem business case |
| Ambiente VMware precisa mover rapido | Relocate | Move plataforma com menor mudanca | Mantem modelo operacional | Confundir com redesenho cloud-native |
| Dependencias desconhecidas | Discovery primeiro | Evita waves quebradas | Leva tempo | Migrar por tamanho de servidor |

## Sequencia recomendada

1. Inventario de workloads.
2. Dono, criticidade e valor de negocio.
3. Dependencias tecnicas e dados.
4. Restrições: prazo, downtime, compliance, licenca.
5. Landing zone readiness.
6. Classificacao 7Rs.
7. Waves e rollback.
8. Execucao, tracking e aprendizagem.

## Sinais de prova

- "data center contract expires" -> waves e estrategias pragmatica.
- "obsolete tool" -> Retire.
- "commercial software SaaS" -> Repurchase.
- "minimal change" -> Rehost.
- "managed database without app redesign" -> Replatform.
- "business agility and high value" -> Refactor/Re-architect.
