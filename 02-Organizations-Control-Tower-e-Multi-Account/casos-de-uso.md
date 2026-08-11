# Casos de Uso

## Caso 1: Empresa adquirida precisa entrar na governança corporativa

**Cenário:** A matriz comprou uma empresa com contas AWS próprias. A exigência é consolidar billing, habilitar auditoria central e manter autonomia temporária dos times adquiridos.

**Decisão:** Convidar/migrar contas para Organizations, criar OU de transição, aplicar SCPs mínimas, habilitar CloudTrail/Config centralizados e planejar evolução para OUs definitivas.

**Trade-off:** A OU de transição reduz risco imediato sem exigir refatoração operacional completa no primeiro dia.

## Caso 2: Sandbox está gerando custo e risco público

**Cenário:** Times criam recursos experimentais com portas abertas e instâncias caras. Produção não pode ser afetada.

**Decisão:** Criar OU Sandbox, aplicar SCPs contra regiões/serviços proibidos, exigir tags de owner e usar Budgets/alertas separados.

**Trade-off:** Restringe liberdade total, mas preserva autonomia controlada e evita impacto em contas produtivas.

## Caso 3: Segurança precisa operar serviços centralizados

**Cenário:** GuardDuty, Security Hub e Config precisam estar habilitados em todas as contas. A management account não deve ser usada para operação diária.

**Decisão:** Usar conta de segurança como delegated administrator, agregar findings centralmente e enviar logs para log archive.

**Trade-off:** Exige desenho claro de roles e responsabilidades, mas reduz risco operacional e melhora rastreabilidade.
