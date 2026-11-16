# DataSync, Snow Family, Transfer Family and Data Transfer

## Overview

This module summarizes DataSync, Snow Family, Transfer Family and Data Transfer for the AWS Certified Solutions Architect – Professional (SAP-C02) certification. The focus is on recognizing architectural cues in long scenarios and choosing the option that balances security, reliability, performance, cost and operations.

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

- Previous module: [AWS MGN, DMS, SCT and Workload Migration](../24-AWS-MGN-DMS-SCT-and-Workload-Migration/README.md)
- Also review: [questions](./questions.md), [flashcards](./flashcards.md), [cheatsheet](./cheatsheet.md), [use cases](./use-cases.md) and [recommended links](./links.md).
- Next module: [Modernization, Serverless, Containers and Decoupling](../26-Modernization-Serverless-Containers-and-Decoupling/README.md)

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

## Availability and transfer decisions

AWS Snow Family devices are no longer available for new customers to order. Preserve Snow examples as historical SAP-C02 context and check eligibility for existing deployments. For new work, evaluate DataSync for online transfer, AWS Data Transfer Terminal for physical transfer where available, or AWS Partner options. Choose against bandwidth, volume, time, location and handling requirements. See the [official Snowball Edge availability notice](https://docs.aws.amazon.com/snowball/latest/developer-guide/snowball-edge-availability-change.html).

## Additional study materials

- [Module lab or architecture workshop](./lab.md).
