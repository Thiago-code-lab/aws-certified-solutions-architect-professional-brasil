# Casos de Uso - Redes Avancadas

## 1. Rede corporativa multi-account

**Cenario:** uma empresa separa contas por produto, ambiente e unidade de negocio. Todas precisam acessar servicos compartilhados e alguns sistemas on-premises.

**Restricoes:** nao deve haver comunicacao livre entre desenvolvimento e producao; a equipe de rede precisa auditar rotas por dominio.

**Decisao:** implementar Transit Gateway em conta de rede, com route tables separadas para producao, nao producao, shared services e on-premises.

**Trade-off:** TGW adiciona custo por attachment e trafego, mas reduz malha de peering e permite governanca central de rotas.

## 2. Plataforma compartilhada consumida por outras contas

**Cenario:** uma equipe central fornece um servico de validacao de identidade para workloads de varias contas.

**Restricoes:** consumidores nao devem alcancar bancos, filas ou sub-redes administrativas do provedor.

**Decisao:** publicar o servico com AWS PrivateLink atras de NLB, permitindo principals especificos e DNS privado.

**Trade-off:** a solucao e excelente para servicos bem definidos, mas cada servico publicado exige operacao propria de endpoint service.

## 3. Egress controlado para ambiente regulado

**Cenario:** workloads de pagamento precisam sair para internet e parceiros externos passando por inspeção central.

**Restricoes:** auditoria exige log central, bloqueio por dominio/IP e consistencia no caminho de ida e volta.

**Decisao:** usar TGW com inspection VPC, AWS Network Firewall, route tables dedicadas e endpoints VPC para trafego AWS interno.

**Trade-off:** melhora compliance e visibilidade, mas aumenta latencia e cria dependencia operacional da VPC de inspeção.
