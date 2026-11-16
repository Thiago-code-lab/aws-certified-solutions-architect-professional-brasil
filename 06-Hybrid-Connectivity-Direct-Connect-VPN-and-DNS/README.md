# Hybrid Connectivity, Direct Connect, VPN and DNS

## Overview

This module summarizes Hybrid Connectivity, Direct Connect, VPN and DNS for the AWS Certified Solutions Architect – Professional (SAP-C02) certification. The focus is on recognizing architectural cues in long scenarios and choosing the option that balances security, reliability, performance, cost and operations.

## Core concepts

- Identify the dominant constraint before comparing services.
- Assess the impact on identity, networking, data, automation, observability and governance.
- Prefer managed services when they reduce operational effort without violating requirements.
- Confirm quotas and behavior in the official documentation.

## Architectural decision

Use this topic when a scenario calls for a sustainable, verifiable decision. In SAP-C02, the best answer is generally the architecture that meets explicit requirements with the lowest operational risk. Architectural sophistication alone does not justify a choice.

## Exam cues

1. Multi-account, auditing, RTO/RPO, latency or cost requirements change the solution's priorities.
2. Compare technically valid alternatives by their trade-offs and risks.
3. Automation, rollback and observability are part of the architecture.
4. The question often rules out excessive complexity or overly manual solutions.

## Common pitfalls

- Choosing an advanced feature without a stated need.
- Ignoring service quotas, partial failure or the consistency model.
- Addressing security without least privilege, auditing and verifiable controls.
- Confusing migration, modernization and continuous improvement.

## Navigation

- Previous module: [Advanced Networking, VPC and Transit Gateway](../05-Advanced-Networking-VPC-and-Transit-Gateway/README.md)
- Also review: [questions](./questions.md), [flashcards](./flashcards.md), [cheatsheet](./cheatsheet.md), [use cases](./use-cases.md) and [recommended links](./links.md).
- Next module: [PrivateLink, Network Firewall, WAF and Shield](../07-PrivateLink-Network-Firewall-WAF-and-Shield/README.md)

---

## Follow CloudStudy

We are building a platform to help Brazilian learners study AWS in a more practical, organized and accessible way.

- Platform: [CloudStudy](https://cloudstudy.com.br)
- Instagram: [cloudstudy.ai](https://www.instagram.com/cloudstudy.ai/)
- LinkedIn: [CloudStudy](https://www.linkedin.com/company/cloudstudy-ai/)

---

## Additional AWS learning paths in English

- [AWS Solutions Architect Associate](https://github.com/Thiago-code-lab/aws-certified-solutions-architect-associate-brasil/tree/saa-c03-english)
- [AWS Cloud Practitioner](https://github.com/Thiago-code-lab/aws-certified-cloud-practitioner-brasil/tree/clf-c02-english)
- [AWS AI Practitioner](https://github.com/Thiago-code-lab/aws-certified-ai-practitioner-brasil/tree/aif-c01-english)

---

> Continue preparing for AWS certifications with [CloudStudy](https://cloudstudy.com.br).

## Technical review references

- [Direct Connect gateway and Transit Gateway associations](https://docs.aws.amazon.com/directconnect/latest/UserGuide/direct-connect-transit-gateways.html): a transit virtual interface connects Direct Connect to the gateway associated with TGW.
- [MACsec](https://docs.aws.amazon.com/directconnect/latest/UserGuide/MACsec.html): point-to-point Layer 2 protection has a different scope from end-to-end encryption.
- [Route 53 VPC Resolver](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver.html): inbound and outbound endpoints and forwarding rules support hybrid DNS. The source uses the earlier name Route 53 Resolver.
- [TGW route tables](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-route-tables.html): association and selective propagation support routing domains; validate return paths and bypass routes.
