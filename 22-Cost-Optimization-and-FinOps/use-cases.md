# Use Cases - FinOps

## Scenario 1 - Chargeback

### Context
The consolidated bill is growing, and business units deny responsibility.

### Requirements
Attribute costs by product, cost center, environment and account.

### Recommended architecture
Standardize accounts and tags, use the Cost and Usage Report (CUR), and assign Budgets to each owner.

### Rationale
Visibility and allocation come before reliable optimization.

### Trade-offs
Tags and accounts require governance.

### Why the alternatives are less suitable
Buying discounts without ownership hides waste.

### Exam cue
CFO, chargeback and showback requirements point to CUR, tags and Budgets.

## Scenario 2 - Baseline and peaks

### Context
A web service runs 24/7 with seasonal campaigns.

### Requirements
Maintain availability while reducing costs.

### Recommended architecture
Rightsize, use Auto Scaling, cover the measured baseline with Savings Plans and retain elasticity for peaks.

### Rationale
This separates predictable demand from uncertain demand.

### Trade-offs
It requires measurement and periodic review.

### Why the alternatives are less suitable
Committing to peak consumption wastes money; relying entirely on Spot puts availability at risk.

### Exam cue
A stable baseline with unpredictable peaks calls for a partial commitment.

## Scenario 3 - High transfer costs

### Context
An application replicates data between Regions and serves public downloads without caching.

### Requirements
Reduce cost while preserving the user experience and disaster recovery.

### Recommended architecture
Use CloudFront, review replication against the RPO, apply lifecycle policies and consider private endpoints where supported and cost-effective.

### Rationale
Transfer costs originate in the data-flow design.

### Trade-offs
Caching and data policies add complexity.

### Why the alternatives are less suitable
Cutting replication without considering the RPO is risky.

### Exam cue
High data-transfer costs call for a topology review.
