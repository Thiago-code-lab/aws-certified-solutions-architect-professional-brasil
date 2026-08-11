# Casos de Uso

## Cenário 1: Organização com múltiplas contas

**Padrão recomendado:** separar responsabilidades por conta, centralizar governança e automatizar controles essenciais.  
**Motivo:** reduz blast radius e melhora auditoria sem bloquear autonomia dos times.  
**Sinal de prova:** termos como unidades de negócio, conta compartilhada, compliance, logging centralizado ou acesso cross-account.

## Cenário 2: Requisito conflitante de custo e resiliência

**Padrão recomendado:** comparar níveis de disponibilidade e recuperação contra impacto financeiro e operacional.  
**Motivo:** SAP-C02 frequentemente testa a alternativa suficiente, não a arquitetura mais sofisticada.  
**Sinal de prova:** RTO/RPO, orçamento limitado, operação enxuta, múltiplas regiões ou indisponibilidade tolerável.

## Cenário 3: Modernização ou migração gradual

**Padrão recomendado:** reduzir acoplamento, planejar ondas e manter coexistência temporária quando necessário.  
**Motivo:** evita cortes arriscados e permite validar arquitetura por etapas.  
**Sinal de prova:** legado, data center, baixa tolerância a downtime, dependências desconhecidas ou janela de migração curta.
