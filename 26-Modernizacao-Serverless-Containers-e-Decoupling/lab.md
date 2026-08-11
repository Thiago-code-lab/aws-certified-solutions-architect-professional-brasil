# Lab Guiado

## Objetivo

Validar um padrão relacionado a Modernização: Serverless, Containers e Decoupling em ambiente de estudo, com escopo pequeno, evidência observável e cleanup claro.

## Serviços sugeridos

Lambda, ECS, EKS, Fargate, SQS, SNS, EventBridge

## Faixa de custo esperada

- Execute em conta de laboratório.
- Prefira recursos elegíveis a baixo custo ou execução curta.
- Remova todos os recursos ao final.

## Passo a passo

1. Defina o cenário e o requisito dominante antes de criar recursos.
2. Implemente o menor fluxo funcional que demonstre a decisão arquitetural.
3. Ative logs, métricas ou evidências mínimas de validação.
4. Simule uma restrição, falha ou mudança de carga compatível com o tema.
5. Registre o que mudaria em produção: governança, custo, segurança e operação.

## Cleanup

1. Remova recursos criados no laboratório.
2. Apague dados temporários, snapshots e endpoints não usados.
3. Verifique custos no dia seguinte.

## Takeaway para prova

O valor do lab é conectar configuração técnica à decisão arquitetural: por que esta solução atende melhor ao cenário do que as alternativas.
