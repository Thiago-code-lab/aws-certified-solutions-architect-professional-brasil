# Lab - FinOps Architecture Review Workshop

Use fictional data. Do not create any AWS resources.

## Scenario

| Category | Monthly cost | Notes |
| --- | ---: | --- |
| EC2 On-Demand | USD 42,000 | 60% baseline, seasonal peaks |
| RDS | USD 18,000 | Average CPU utilization: 25% |
| S3 Standard | USD 9,000 | 70% not accessed in 180 days |
| NAT Gateway | USD 7,500 | Calls to AWS services |
| Data Transfer | USD 11,000 | Replication and public downloads |
| EBS | USD 5,000 | Old volumes |
| Idle development | USD 6,500 | Environments running 24/7 |

## Tasks

1. Identify cost drivers.
2. Classify quick wins, architectural changes and commitments.
3. Determine rightsizing opportunities.
4. Evaluate Savings Plans or Reserved Instances after measuring demand.
5. Evaluate Spot.
6. Propose S3 lifecycle policies.
7. Preserve availability and disaster recovery.
8. Create a prioritized plan.

## Criteria

- Remove waste before buying commitments.
- Distinguish cost savings from resilience requirements.
- Define ownership.
- Explain the risk of each action.
