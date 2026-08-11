# Referencias Oficiais

## Essencial

- [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) - Base oficial para stacks, updates, rollback e IaC; leitura prioritaria.
- [AWS CloudFormation StackSets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.html) - Essencial para deployment multi-account e multi-region.
- [AWS CodePipeline User Guide](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html) - Cobre orquestracao de pipeline; importante para promocao entre ambientes.

## Aprofundamento

- [CloudFormation change sets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-changesets.html) - Ajuda a avaliar impacto antes de atualizar.
- [CloudFormation drift detection](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html) - Importante para detectar divergencia entre IaC e estado real.
- [AWS CodeBuild User Guide](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html) - Relevante para build/testes e validacao automatizada.

## Referencia

- [AWS CodeDeploy User Guide](https://docs.aws.amazon.com/codedeploy/latest/userguide/welcome.html) - Consulte para estrategias de deployment e rollback de aplicacoes.
- [Amazon ECS deployment types](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-types.html) - Referencia para rolling e blue/green em containers.
- [Lambda deployments with CodeDeploy](https://docs.aws.amazon.com/lambda/latest/dg/configuring-alias-routing.html) - Util para canary/linear deployments em funcoes Lambda.
