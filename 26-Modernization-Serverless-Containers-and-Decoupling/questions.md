# Questions - Modernization

## Question 1

A company has a ten-year-old monolith, a shared database and new mobile APIs. The business cannot accept a multiyear rewrite. Which approach is best?

A) A big-bang rewrite.
B) The strangler pattern with a routing layer and new services by domain.
C) Migrate everything to EKS without reducing coupling.
D) Rebuild the entire database before delivering value.

<details><summary><strong>Show answer</strong></summary>

**Correct answer:** B

Strangler delivers value incrementally and reduces risk. A concentrates risk; C changes the platform without modernizing the design; D creates an excessive dependency before delivery.
</details>

## Question 2

An online order triggers email, inventory updates and analytics. Peaks slow the synchronous flow. What improves resilience?

A) Increase timeouts.
B) Use SQS/EventBridge to decouple stages and support retries.
C) Put everything in the same container.
D) Remove observability.

<details><summary><strong>Show answer</strong></summary>

**Correct answer:** B

Independent stages suit asynchronous processing and retries. The other options increase coupling or operational risk.
</details>

## Question 3

A small team must operate stateless APIs with variable peaks and little Kubernetes experience. Which option reduces overhead?

A) A highly customized EKS deployment.
B) Lambda where appropriate, or ECS/Fargate for containers without managing instances.
C) Manually managed EC2 without Auto Scaling.
D) One cluster per microservice.

<details><summary><strong>Show answer</strong></summary>

**Correct answer:** B

Lambda and Fargate reduce operational effort. EKS can be valid, but requires maturity.
</details>

## Question 4

An organization already has mature Kubernetes capabilities, observability and trained teams. Its services require specific runtimes. Which decision is defensible?

A) EKS can be appropriate, accepting greater operational effort.
B) Lambda replaces all containers.
C) S3 runs the services.
D) Return to the monolith.

<details><summary><strong>Show answer</strong></summary>

**Correct answer:** A

Kubernetes maturity and the need for control favor EKS. The other alternatives ignore the requirements.
</details>

## Question 5

Billing changes rapidly, but a legacy tax module is stable and regulated. Which plan is best?

A) Modernize everything simultaneously.
B) Refactor billing first and retain the tax module until changes are justified and tested.
C) Remove tax controls.
D) Create events without idempotency.

<details><summary><strong>Show answer</strong></summary>

**Correct answer:** B

Modernization prioritizes value and risk. Changing a regulated domain unnecessarily adds risk without a corresponding return.
</details>
