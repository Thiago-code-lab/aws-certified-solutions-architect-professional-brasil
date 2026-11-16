# Domain Practice Exams

## Design Solutions for Organizational Complexity - 26%

1. A landing zone needs autonomy and central governance. **Answer:** multiple accounts with OUs, SCPs and centralized logging.
2. Temporary access through the corporate identity provider. **Answer:** IAM Identity Center with permission sets.
3. Controlled sharing of resources between accounts. **Answer:** AWS RAM where supported.

## Design for New Solutions - 29%

4. Global content delivery with low latency. **Answer:** CloudFront and an appropriate origin design.
5. Consumers process orders at different rates. **Answer:** Amazon SQS.
6. Containers with less server administration. **Answer:** AWS Fargate where requirements allow it.

## Continuous Improvement for Existing Solutions - 25%

7. Costs cannot be traced to products. **Answer:** tags, Cost Explorer and Budgets.
8. Threat detection across multiple accounts. **Answer:** GuardDuty and Security Hub with delegated administration.
9. A Regional quota may be reached before a high-traffic event. **Answer:** review Service Quotas, load test and request an increase where supported.

## Accelerate Workload Migration and Modernization - 20%

10. A large migration has unknown dependencies. **Answer:** discovery and assessment.
11. A database must migrate with continuous replication. **Answer:** AWS DMS, subject to supported engines and change data capture prerequisites.
12. A large data volume must move over limited connectivity. **Answer:** assess DataSync against an offline transfer option according to data volume, connectivity and availability. Snow Family is historical context; check current eligibility before proposing it.

---

Continue your studies with CloudStudy:

[https://cloudstudy.com.br](https://cloudstudy.com.br)
