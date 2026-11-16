# Lab - Modernization Architecture Workshop

Do not provision any resources.

## Scenario

A company has a ten-year-old monolith, a shared relational database, seasonal peaks, slow releases, a small platform team, background processing and new mobile/API requirements.

## Tasks

1. Identify domain boundaries.
2. Choose what to retain initially.
3. Define the strangler approach.
4. Separate synchronous and asynchronous processing.
5. Choose Lambda or containers for each capability.
6. Design the events.
7. Define the stages.
8. Analyze overhead.
9. Explain why a big-bang rewrite is less suitable.

## Expected architecture

```text
Users / Mobile
      |
 API or Routing Layer
      |
      +--> Legacy Monolith --> Shared Database
      +--> Orders API on Fargate/Lambda
      +--> Background events -> SQS/EventBridge -> Workers
```

## Criteria

- Deliver value before replacing everything.
- Create microservices around domain boundaries.
- Event processing includes idempotency, retries and observability.
- The platform reflects team skills and operational cost.
