# SAP-C02 English Edition Audit

This edition translates **all 217 source Markdown documents** from Portuguese `main` at `471ebd78a428180b5d12afa320751fb60fbecffc`. The source contains 223 tracked files and 31 numbered modules. Publication is limited to [`sap-c02-english`](https://github.com/Thiago-code-lab/aws-certified-solutions-architect-professional-brasil/tree/sap-c02-english).

## Source coverage and naming

The [source inventory](source-inventory.json) maps every original tracked file to exactly one target. All 31 modules retain their original sequence. **210 complete file paths changed**, including **68 renamed basenames** and **31 renamed module directories**. Basename and directory counts overlap in complete paths; they should not be added together.

Every module retains its README, use cases, cheatsheet, flashcards, questions and official links. All 18 source labs/workshops remain present. The source's 165 flashcards, module 30 review plan and error log, official resource glossary, contribution/security documents, issue templates, changelog, domain paths and module template are translated. The module template's deliberately illustrative concept slots are preserved as template instructions.

The main README retains the banner, logo, CloudStudy destinations, social links, Udemy referral and WhatsApp community links. It adds an English badge, links all modules, domain paths, scenarios, labs, official resources, contribution guidance and the license. Companion learning paths point to the verified SAA-C03, CLF-C02 and AIF-C01 English branches. No reference repository was modified.

## Question and answer audit

The [question audit](question-audit.json) records each original prompt, source and target paths, numbering, type, alternative labels, original answer and reviewed answer signature.

| Material | Questions | Format |
|---|---:|---|
| 28 ordinary module question files | 56 | Multiple choice, two per module |
| Module 06 hybrid connectivity | 5 | Multiple choice |
| Module 26 modernization | 5 | Multiple choice |
| Module 30 mixed sample | 10 | Open response |
| Module 30 domain practice exams | 12 | Open response, three per domain |
| Total | **88** | **66 multiple choice, 22 open response** |

All 66 correct answer letters, question numbers and alternative labels are preserved. The source contains **zero multi-select prompts** and no separate external answer-key files. Multi-select preservation is nevertheless covered by a regression fixture. Module 30 is a small study sample rather than a full-length, domain-weighted exam simulation. No missing questions were invented.

Two open-response answers were corrected or qualified, with exact original and final answer text preserved in the JSON:

1. Mixed sample question 6: the source answers insecure-configuration detection with GuardDuty and Security Hub. The English answer uses **AWS Config and Security Hub CSPM**, with GuardDuty as complementary threat detection. [AWS configuration-check prerequisites](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-setup-prereqs.html) support this distinction.
2. Domain practice question 12: the source offers DataSync or Snow Family without an availability caveat. The English answer makes offline transfer conditional on current availability and eligibility; new customers cannot order Snow Family devices. See the [official Snowball Edge notice](https://docs.aws.amazon.com/snowball/latest/developer-guide/snowball-edge-availability-change.html).

The other open answers retain their recommendations with explicit qualifications for SCP scope, workload requirements, supported database deployments and DMS prerequisites. The hybrid questions retain all original correct letters and explanations of rejected alternatives. Modernization cases retain their context, constraints, business value, selected architecture, coexistence costs and reasons against big-bang replacement.

## Technical review and corrections

The editorial method is documented in the [editorial manifest](editorial-manifest.json): agent review of every distinct source line and shared template, translation in context, and additional review of the substantive hybrid, FinOps and modernization scenarios. This was **not an independent human expert review**. Counts and structural checks support coverage; they do not prove semantic equivalence.

| Topic | Correction or clarification | Official reference |
|---|---|---|
| SAP-C02 lifecycle | Preserve C02 scope; disclose November 16, 2026 as its final exam date and November 17 as SAP-C03 delivery start | [AWS certification update](https://aws.amazon.com/blogs/training-and-certification/september-2026-new-offerings/) |
| Exam domains | Retain the four source domains and 26/29/25/20 percent weights | [SAP-C02 guide](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-professional-02/solutions-architect-professional-02.html) |
| SCPs | Constrain member-account permissions; do not grant access or restrict management-account principals and service-linked roles | [SCP documentation](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) |
| Hybrid encryption | MACsec protects a supported Layer 2 segment; its scope differs from end-to-end encryption | [MACsec](https://docs.aws.amazon.com/directconnect/latest/UserGuide/MACsec.html) |
| Hybrid routing | DXGW/TGW requires the appropriate transit virtual interface; segmentation needs selective propagation, return paths and bypass review | [DXGW/TGW](https://docs.aws.amazon.com/directconnect/latest/UserGuide/direct-connect-transit-gateways.html), [TGW route tables](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-route-tables.html) |
| Hybrid DNS | Explain inbound/outbound direction, forwarding rules and network prerequisites; note current VPC Resolver naming | [Route 53 VPC Resolver](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver.html) |
| Budgeting | Thresholds and optional configured actions do not automatically impose a hard spending cap | [AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html) |
| Commitments | Measure and rightsize before commitment; Savings Plans flexibility depends on type and eligibility | [Savings Plans](https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html) |
| Migration Hub | Closed to new customers since November 7, 2025; evaluate AWS Transform for new projects | [Availability change](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/migrationhub-availability-change.html) |
| MGN | Note current AWS Transform MGN name and distinguish server block replication from DMS and SCT | [MGN overview](https://docs.aws.amazon.com/mgn/latest/ug/what-is-mgn.html) |
| Snow Family | Retain historical context and disclose restrictions for new customers; assess online and physical alternatives | [Availability change](https://docs.aws.amazon.com/snowball/latest/developer-guide/snowball-edge-availability-change.html) |
| Governance controls | Include proactive controls alongside preventive and detective controls | [Control Tower controls](https://docs.aws.amazon.com/controltower/latest/userguide/how-controls-work.html) |
| Well-Architected | Explicitly enumerate all six pillars, including sustainability | [Framework pillars](https://docs.aws.amazon.com/wellarchitected/latest/framework/the-pillars-of-the-framework.html) |
| Modernization | Preserve incremental domain extraction, team-skill and runtime constraints, idempotency, retries and operational costs | [Strangler fig](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/strangler-fig.html), [SQS delivery](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/standard-queues.html) |

Also checked [RDS Multi-AZ deployment distinctions](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html) and [disaster recovery strategies](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html). Existing general recommendations do not claim that a standby always serves reads or that Multi-AZ alone satisfies every Regional disaster requirement.

## Automated verification

The validator follows the CLF-C02 English edition's inventory, Markdown parser, anchor, answer-audit and mutation-test conventions, with SAP-C02-specific exercise formats. Run from the repository root:

```sh
python -m pip install -r scripts/english-edition/requirements.txt
python scripts/english-edition/validate.py
python -m unittest discover -s scripts/english-edition -p "test_*.py"
git diff --check
```

The [validation results](validation-results.json) report source equivalence, preserved-file checksums, module sequence, question/answer signatures, flashcard counts, structural coverage, local links, HTML images, heading anchors, code fences, table widths, expandable answers and targeted Portuguese-language regressions. The 18 regression tests include deliberate answer, alternative, question, explanation, multi-select, flashcard, fence, table, anchor, image and language failures.

Final checks passed: **223 source equivalents, 217 translated documents, 31 modules, 88 prompts, 165 flashcards and all 18 regression tests**. Relative Markdown and HTML image links and heading anchors have no detected failures. `git diff --check` and staged whitespace checks passed. Dependency installation succeeded; pip emitted pre-existing host warnings about unrelated invalid distributions.

The optional HTTP checker examined **106 unique external URLs** after corrections: **104 returned HTTP 200**, one LinkedIn author link returned HTTP 999 and the preserved Udemy referral returned HTTP 403. These two promotional destinations block automated verification and remain unverified. HTTP success does not establish page semantics or fragment-anchor validity. The [initial results](external-link-initial-results.json), [final results](external-link-results.json) and [URL corrections](link-corrections.json) preserve evidence. Replaced two source migration references returning 404 and a forbidden Cost Management directory URL with current official pages; three distinct source URLs were corrected in four file locations.

Only Markdown is included in navigation checks: the original portal and deployment workflow are intentionally preserved. AWS labs were **not executed**, and no AWS resources were provisioned or charges incurred. Static inspection and offline validation are distinct from live AWS behavior.

## Asset preservation and publication

Both original PNG assets, `LICENSE`, `index.html`, `.github/FUNDING.yml` and `.github/workflows/deploy.yml` are preserved. SHA-256 verification normalizes CRLF to LF for text and compares PNG bytes exactly. There are no frontend, hosting or deployment additions.

Protected starting references:

- `main`: `471ebd78a428180b5d12afa320751fb60fbecffc`.
- `gh-pages`: `eb62bf8ccd4482cc7177cec6af6da06d7225662a`.

Published content and validation commit: 55fab99367f21e04a21f7eec14586d1701db76cc. Local HEAD, the fetched English branch and the advertised remote branch matched at this checkpoint. Both protected remote branches retained their starting SHAs. Only the English branch is committed and pushed. Final publication evidence, including local, remote-tracking and advertised remote SHAs, is recorded in [publication.json](publication.json). The final audit checkpoint commit is the commit containing this file, resolvable with `git log -1 --format=%H -- docs/english-edition/README.md` and the [branch history](https://github.com/Thiago-code-lab/aws-certified-solutions-architect-professional-brasil/commits/sap-c02-english/). A commit cannot contain its own immutable hash; the final response reports that exact SHA after push and verification.

## Remaining limitations

- The Portuguese source is a concise public curriculum with substantial repeated introductory templates. Translating all source documents does not make it a comprehensive Professional course. The README preserves and qualifies the source's historical maturity labels; no source learning materials were omitted or condensed further.
- Automated language checks target common regressions. Source-to-target coverage and editorial review cannot establish perfect translation or exhaustively verify every AWS capability.
- Original banner artwork and some promotional destinations remain Portuguese. Companion English branches and service availability can evolve after this review.
- Automated HTTP verification was blocked for the LinkedIn author attribution and Udemy referral; those original promotional links are retained.
- No independent human expert, browser rendering review or live AWS lab run was performed. The untouched HTML portal can still reference Portuguese paths; GitHub Markdown is the supported navigation surface for this edition.

[Return to the English learning path](../../README.md)
