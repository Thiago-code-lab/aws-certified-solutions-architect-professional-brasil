# Questions - SAP-C02 Sample

1. A company uses multiple AWS accounts and must prevent workloads outside the security OU from disabling CloudTrail. **Answer:** apply an SCP to the relevant workload OUs. SCPs constrain permissions in member accounts; they do not grant permissions or restrict the management account or service-linked roles.
2. An application needs predictable connectivity between the data center and AWS, with VPN for contingency. **Answer:** Direct Connect with Site-to-Site VPN as backup.
3. A global API must reduce latency and maintain controlled failover. **Answer:** evaluate Route 53, CloudFront, Global Accelerator and the origin strategy against the API's routing and caching requirements.
4. A critical relational database must reduce downtime after an AZ failure. **Answer:** Multi-AZ or Aurora with managed failover, using a supported deployment configuration.
5. An architecture with unpredictable peaks must decouple producers and consumers. **Answer:** SQS, SNS, EventBridge or Step Functions according to the required messaging or orchestration pattern.
6. An organization wants to detect insecure configurations across multiple accounts. **Answer:** AWS Config and Security Hub CSPM with organizational aggregation and delegated administration where supported. GuardDuty complements these controls with threat detection.
7. A team must reduce cost without affecting critical workloads. **Answer:** tags, Cost Explorer, Budgets and rightsizing before commitments.
8. A migration includes hundreds of servers and needs prioritized waves. **Answer:** discovery, dependency mapping and selection among the 7 Rs.
9. A company wants to modernize a monolith gradually. **Answer:** extract capabilities through APIs, events and managed components.
10. Two alternatives are technically viable. **Answer:** choose according to explicit requirements, operational risk, cost and governance.

---

Continue your studies with CloudStudy:

[https://cloudstudy.com.br](https://cloudstudy.com.br)
