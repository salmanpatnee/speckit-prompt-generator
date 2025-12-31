# Speckit Prompt Quality Standards

This guide details the quality standards and design patterns used to generate high-quality Speckit-compatible prompts.

## Core Principles

### 1. Paragraph Form (No Bullet Lists)
Speckit commands work best with flowing narrative prompts rather than bullet points. Prompts should be complete sentences connected logically.

**Good:**
```
Design the technical architecture for Phase 5: Webhooks, Transactions & Receipts. Plan Stripe webhook event handling with secure signature verification and idempotent processing to prevent duplicate transactions. Design a transaction persistence layer that records payment attempts, completions, and failures with full audit trails.
```

**Avoid:**
```
- Design Stripe webhook handling
- Plan signature verification
- Ensure idempotent processing
- Design transaction persistence layer
```

### 2. Intent-First, Outcomes-Emphasized
Prompts should focus on "why" and "what outcomes," not implementation details. Repeat key success criteria to reinforce acceptance standards.

**Good:**
```
Implement user authentication ensuring all authentication state is persisted securely, user credentials are never exposed in logs or errors, and authentication failures are logged for security auditing.
```

**Avoid:**
```
Use bcrypt to hash passwords, store tokens in a secure cookie, and check the user in the middleware.
```

### 3. Concise Language
- **Spec prompts**: ~60–120 words
- **Plan prompts**: ~100–150 words
- **Cut redundancy**: Remove "it will," "the system should," etc.

**Good:**
```
Build robust Stripe webhook handling to verify payments in real-time, persist transaction records to maintain system state accuracy, synchronize payment status across the application, and generate reliable payment receipts and confirmations. Ensure payments are verified via webhooks, the system reflects accurate payment state at all times, and receipts are generated reliably for audit and customer communication purposes.
```

### 4. Logical Chaining
Requirements should build on each other in a sensible, hierarchical order. Causality should be clear.

**Good Order:**
1. Handle incoming events (webhooks)
2. Verify event authenticity (signature validation)
3. Persist state (transactions)
4. Synchronize across system (status updates)
5. Generate outputs (receipts)

**Pattern:**
```
[Action 1] to [achieve goal 1], [Action 2] to [achieve goal 2], and [Action 3] to [achieve goal 3]. Ensure [outcome 1], [outcome 2], and [outcome 3].
```

### 5. Constraints & Dependencies Embedded
Reference constraints, dependencies, and non-functional requirements naturally within the prompt.

**Good:**
```
Implement database migrations that support zero-downtime deployments, ensuring backward compatibility with existing code during the migration window.
```

**Avoid:**
```
Implement database migrations. Ensure zero-downtime deployments. Support backward compatibility.
```

## Prompt Structure Template

### Spec Prompts (Requirements & Specification)
Use for initial feature definition, requirements gathering, or specification phases.

**Structure:**
```
[Implement/Build/Create] [Feature Name]. [Purpose statement]. [Detailed requirements] ensuring [key success criterion 1], [key success criterion 2], and [key success criterion 3].
```

**Example:**
```
Implement Phase 1: Requirements Gathering. Identify and document all functional and non-functional requirements for the payment processing system, including merchant configuration, payment method support, currency handling, and compliance needs. Ensure requirements are comprehensive and testable, stakeholders have reviewed and approved them, and dependencies on external systems are clearly documented.
```

### Plan Prompts (Architecture & Design)
Use for architectural decisions, design phases, or planning phases.

**Structure:**
```
Design the technical architecture for [Feature Name]. [Key design consideration 1] with [how it will be achieved], [key design consideration 2] with [how it will be achieved], and [key design consideration 3]. Address [critical concern 1], [critical concern 2], and [critical concern 3] to ensure [overall quality attribute].
```

**Example:**
```
Design the technical architecture for Phase 2: System Architecture. Plan the overall system topology separating payment processing, transaction persistence, and notification concerns with clear service boundaries and communication protocols. Design the database schema to support transaction history, idempotency keys, and status tracking. Define API contracts for webhook handlers and payment status queries ensuring consistency and versioning. Address failure modes including webhook retries, database transaction rollback, and payment state reconciliation to ensure reliability and data consistency.
```

## Common Patterns

### Pattern 1: Security-First Prompts
```
Implement [feature] ensuring [security requirement 1], [security requirement 2], and [security requirement 3] are maintained throughout. Use [specific approach] to prevent [threat vector].
```

### Pattern 2: Integration Prompts
```
Integrate [external system] by implementing [component 1] to [handle task 1], [component 2] to [handle task 2], and [component 3] to [handle task 3]. Ensure [integration quality criterion 1], [integration quality criterion 2], and [integration quality criterion 3].
```

### Pattern 3: Multi-Phase Prompts
```
Implement Phase X: [Phase Name]. Build [first subsystem] that [achieves goal 1], [second subsystem] that [achieves goal 2], and [third subsystem] that [achieves goal 3]. Ensure [outcome 1], [outcome 2], and [outcome 3] are met throughout.
```

### Pattern 4: Quality & Performance Prompts
```
Implement [feature] with [performance characteristic] performance, [reliability characteristic] reliability, and [maintainability characteristic] maintainability. Consider [non-functional requirement 1], [non-functional requirement 2], and ensure [quality metric].
```

## Anti-Patterns (What NOT to Do)

### ❌ Don't: Use Bullet Lists
```
- Use Stripe SDK
- Implement retry logic
- Add error handling
```
✅ Instead: `Use Stripe SDK to handle payment requests with automatic retry logic and comprehensive error handling.`

### ❌ Don't: Reference Implementation Details
```
Use the PostgreSQL JSONB column type to store transaction metadata in the database.
```
✅ Instead: `Design a transaction persistence layer that captures all payment metadata and state changes for audit and debugging purposes.`

### ❌ Don't: Over-Specify Technology
```
Use Redis for caching and Bull for job queues.
```
✅ Instead: `Implement an efficient caching strategy for frequently accessed payment states and an asynchronous job processing system for receipt generation.`

### ❌ Don't: Be Vague About Outcomes
```
Make the system better.
```
✅ Instead: `Ensure payments are verified reliably, system state is accurate at all times, and failures are logged with sufficient detail for debugging.`

### ❌ Don't: Forget to Emphasize Success Criteria
```
Generate receipts for customers.
```
✅ Instead: `Generate reliable payment receipts ensuring they are delivered within 5 minutes of payment completion, contain all required audit information, and maintain a complete archive for compliance.`

## Quality Checklist

For each generated prompt, verify:

- ✅ Written in paragraph form (no bullet lists)
- ✅ Opens with clear phase name and objective
- ✅ Chains requirements logically (cause → effect)
- ✅ Emphasizes key success criteria at least once
- ✅ References constraints or dependencies where relevant
- ✅ No implementation details (no specific tech names)
- ✅ 60–150 words depending on complexity
- ✅ Ends with actionable context or acceptance criteria
- ✅ Uses active voice and imperative mood
- ✅ Avoids jargon unless necessary; explains complex concepts

## Example Generation Process

**Input Phase:**
```
## Phase 5 – Webhooks, Transactions & Receipts

**Objective**
Ensure payment reliability and system consistency.

**High-Level Scope**

* Stripe webhook handling
* Transaction persistence
* Payment status synchronization
* Payment receipts and confirmations

**Outcome**

* Payments are verified via webhooks
* System reflects accurate payment state
* Receipts are generated reliably
```

**Analysis:**
- Number: 5
- Title: Webhooks, Transactions & Receipts
- Objective: Ensure payment reliability and system consistency
- Scope items: 4 (webhooks, persistence, synchronization, receipts)
- Outcomes: 3 (verified, accurate state, reliable receipts)
- Type: Plan (not first phase)

**Generated Prompt:**
```
Design the technical architecture for Phase 5: Webhooks, Transactions & Receipts. Plan Stripe webhook event handling with secure signature verification and idempotent processing to prevent duplicate transactions. Design a transaction persistence layer that records payment attempts, completions, and failures with full audit trails. Establish payment status synchronization mechanisms that keep the database and Stripe state consistent, including handling for webhook delivery failures and retries. Define the receipt generation pipeline—including email delivery, PDF generation, and storage—ensuring reliability and compliance. Address failure modes, retry strategies, and monitoring requirements to ensure system reliability and accurate payment state reflection at all times.
```

**Quality Check:**
- ✅ Paragraph form
- ✅ Logical chaining (webhooks → verification → persistence → sync → receipts)
- ✅ Success criteria emphasized (reliable, accurate, consistent)
- ✅ No implementation details
- ✅ ~120 words (appropriate for plan prompt)
- ✅ Ready for `/sp.plan`
