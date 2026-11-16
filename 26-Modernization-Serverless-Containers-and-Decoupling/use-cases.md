# Use Cases - Modernization

## Scenario 1 - A monolith with new APIs

### Context
A legacy system combines web, batch processing and business rules in one codebase.

### Requirements
Deliver new mobile APIs with shorter release cycles and low risk.

### Recommended architecture
Use the strangler pattern with an API layer, new services by domain and the monolith for stable functions.

### Rationale
This delivers value before full replacement.

### Trade-offs
Coexistence and observability become more complex.

### Why the alternatives are less suitable
A full rewrite increases risk; a pure rehost does not improve release delivery.

### Exam cue
An inability to tolerate a long rewrite points to incremental migration.

## Scenario 2 - Asynchronous processing

### Context
Checkout triggers notifications, fraud checks, billing and analytics.

### Requirements
Absorb peaks, support retries and prevent cascading failures.

### Recommended architecture
Use EventBridge for domain events and SQS for consumers that need buffering.

### Rationale
This reduces coupling and allows partial failure.

### Trade-offs
The design must address eventual consistency and implement idempotency.

### Why the alternatives are less suitable
Chains of synchronous calls increase latency and risk.

### Exam cue
Peaks and independent consumers point to asynchronous processing.

## Scenario 3 - Platform selection

### Context
A small team delivers simple services; a central department has mature Kubernetes capabilities.

### Requirements
Keep overhead low for some services while controlling the runtime for others.

### Recommended architecture
Use Lambda/Fargate for simple services and EKS where Kubernetes adds value.

### Rationale
The choice respects skills and operational constraints.

### Trade-offs
Multiple platforms require shared standards.

### Why the alternatives are less suitable
Forcing everything onto EKS increases toil; forcing everything onto Lambda ignores runtime requirements.

### Exam cue
Team skills and operational overhead are decisive cues.
