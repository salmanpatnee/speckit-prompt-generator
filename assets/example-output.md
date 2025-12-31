# Speckit Prompts – Example Output

This example shows what the skill generates when given a typical multi-phase plan.

---

**Generated:** 2025-12-31 14:32:05
**Source:** `specs/payment-processing/plan.md`
**Total Prompts:** 5

## Index

- [SPEC – Phase 1: Requirements Gathering](#prompt-1)
- [PLAN – Phase 2: System Architecture](#prompt-2)
- [PLAN – Phase 3: Database Design & Models](#prompt-3)
- [PLAN – Phase 4: API Design & Security](#prompt-4)
- [PLAN – Phase 5: Webhooks, Transactions & Receipts](#prompt-5)

## Prompts

### Spec Prompt: Phase 1 – Requirements Gathering
{#prompt-1}

**Command:** `/sp.specify`

**Prompt:**

> Implement Phase 1: Requirements Gathering. Identify and document all functional and non-functional requirements for the payment processing system, including merchant onboarding workflows, payment method support (cards, wallets, ACH), multi-currency handling, compliance and regulatory requirements, and integration touchpoints. Ensure requirements are comprehensive and testable, stakeholders have reviewed and approved them, dependencies on external systems like Stripe are clearly documented, and success metrics are defined for each requirement area.

---

### Plan Prompt: Phase 2 – System Architecture
{#prompt-2}

**Command:** `/sp.plan`

**Prompt:**

> Design the technical architecture for Phase 2: System Architecture. Plan the overall system topology separating payment processing, transaction persistence, and notification concerns with clear service boundaries and communication protocols. Design the database schema to support transaction history, idempotency keys, payment status tracking, and merchant configuration. Define API contracts for payment initiation, status queries, and webhook handlers ensuring consistency and API versioning strategy. Address failure modes including payment retries, database transaction rollback, state reconciliation, and observability requirements to ensure system reliability and data consistency throughout.

---

### Plan Prompt: Phase 3 – Database Design & Models
{#prompt-3}

**Command:** `/sp.plan`

**Prompt:**

> Design the technical architecture for Phase 3: Database Design & Models. Plan the database schema with tables for merchants, payment methods, transactions, refunds, and audit logs, using appropriate relationships (HasMany, BelongsToMany) and indices for performance. Design Laravel Eloquent models with type-hinted relationships, proper casting (dates, JSON, enums), and query optimization strategies to prevent N+1 queries. Create factories that generate realistic test data for merchants, payment scenarios, and edge cases. Create seeders for local development and testing workflows. Address data retention policies, archival strategies, and migration safety for altering schema without downtime.

---

### Plan Prompt: Phase 4 – API Design & Security
{#prompt-4}

**Command:** `/sp.plan`

**Prompt:**

> Design the technical architecture for Phase 4: API Design & Security. Plan REST API endpoints following RESTful conventions for initiating payments, querying status, handling refunds, and managing merchant configurations. Implement authentication using Laravel Fortify or Sanctum with token-based authorization and role-based access control. Design endpoints for filtering, sorting, pagination, and idempotent operations to handle duplicate requests safely. Address API security concerns including rate limiting per merchant, CSRF protection, input validation and sanitization, secure error responses, and encryption for sensitive data in transit. Ensure API versioning strategy supports backward compatibility and graceful deprecation of old endpoints.

---

### Plan Prompt: Phase 5 – Webhooks, Transactions & Receipts
{#prompt-5}

**Command:** `/sp.plan`

**Prompt:**

> Design the technical architecture for Phase 5: Webhooks, Transactions & Receipts. Plan Stripe webhook event handling with secure HMAC signature verification and idempotent processing to prevent duplicate transactions. Design a transaction persistence layer that records payment attempts, completions, failures, and state transitions with full audit trails for compliance. Establish payment status synchronization mechanisms that keep the database and Stripe state consistent, including handling for webhook delivery failures, exponential backoff retries, and reconciliation jobs. Define the receipt generation pipeline including email delivery templates, PDF generation, secure storage, and delivery reliability. Address failure modes, monitoring and alerting, and recovery strategies to ensure system reliability and accurate payment state reflection at all times.

---

## How to Use These Prompts

Each prompt above is ready to be used immediately with the corresponding Speckit command:

```bash
# Phase 1 – Run specification
/sp.specify
# Paste the Phase 1 prompt above

# Phase 2 – Run planning
/sp.plan
# Paste the Phase 2 prompt above

# Phase 3 – Run planning
/sp.plan
# Paste the Phase 3 prompt above

# And so on...
```

The prompts are written in paragraph form (not bullet lists) to work optimally with Speckit's AI processing. Each prompt:
- Opens with a clear phase objective
- Chains requirements logically (cause → effect)
- Emphasizes success criteria and acceptance conditions
- Avoids implementation details
- Includes relevant constraints and non-functional requirements

## Notes

- **Spec prompts** (Phase 1) guide `/sp.specify` to create detailed specifications
- **Plan prompts** (Phases 2–5) guide `/sp.plan` to create architectural and design plans
- All prompts are self-contained and can be run independently
- Prompts are designed to produce consistent, high-quality Speckit artifacts
- Generated prompts can be edited if you want to adjust emphasis or add context

## Next Steps

1. Copy the prompt for Phase 1 into a `/sp.specify` command
2. Let Speckit generate the specification document
3. Review the specification and refine if needed
4. Move to Phase 2 and repeat for each subsequent phase
5. As each phase completes, the output feeds naturally into the next phase's planning

This workflow ensures each phase builds logically on previous work while maintaining consistency across the entire feature development.
