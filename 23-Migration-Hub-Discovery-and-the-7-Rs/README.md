# Migration Hub, Discovery and the 7 Rs

## Overview

This module summarizes Migration Hub, Discovery and the 7 Rs for the AWS Certified Solutions Architect – Professional (SAP-C02) certification. The focus is on recognizing architectural cues in long scenarios and choosing the option that balances security, reliability, performance, cost and operations.

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

- Previous module: [Cost Optimization and FinOps](../22-Cost-Optimization-and-FinOps/README.md)
- Also review: [questions](./questions.md), [flashcards](./flashcards.md), [cheatsheet](./cheatsheet.md), [use cases](./use-cases.md) and [recommended links](./links.md).
- Next module: [AWS MGN, DMS, SCT and Workload Migration](../24-AWS-MGN-DMS-SCT-and-Workload-Migration/README.md)

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

## Current service availability

Migration Hub stopped accepting new customers on November 7, 2025. Existing customers can complete ongoing projects. For new migration planning, evaluate AWS Transform. Discovery, dependency mapping, wave planning and the 7 Rs remain relevant architectural practices. See the [official Migration Hub availability notice](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/migrationhub-availability-change.html).
