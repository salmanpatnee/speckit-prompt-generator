# Speckit Prompt Generator – Workflows & Examples

This guide shows real-world workflows for using the skill effectively.

## Workflow 1: Multi-Phase Feature Development

**Scenario:** You have a detailed plan with 5+ phases for a complex feature and need prompts for `/sp.specify` and `/sp.plan`.

**Input Document:** `specs/payment-processing/plan.md`

```markdown
# Payment Processing System – Development Plan

## Phase 1 – Requirements Gathering
**Objective**
Define all functional and non-functional requirements.

**High-Level Scope**
- Merchant onboarding requirements
- Payment method support (cards, wallets, ACH)
- Multi-currency handling
- Compliance and regulatory requirements
- Rate limiting and throttling

**Outcome**
- Comprehensive requirements document
- Stakeholder sign-off
- Clear success metrics

## Phase 2 – System Architecture
**Objective**
Design the overall system topology and component boundaries.

**High-Level Scope**
- Service architecture (synchronous vs asynchronous)
- Database design and relationships
- API contract design
- Security model and authentication flow
- Webhook architecture for external systems

**Outcome**
- Architecture diagram with component boundaries
- API specifications
- Security model documentation

[Phases 3–5 follow similar structure...]
```

**Skill Invocation:**
```
Generate Speckit prompts from: specs/payment-processing/plan.md
```

**Output:** `specs/payment-processing/speckit-prompts.md`

Contains:
1. SPEC prompt for Phase 1 (Requirements)
2. PLAN prompt for Phase 2 (Architecture)
3. PLAN prompt for Phase 3 (Data Modeling)
4. PLAN prompt for Phase 4 (API Design)
5. PLAN prompt for Phase 5 (Validation)

**Next Steps:**
```bash
/sp.specify < Phase 1 prompt from speckit-prompts.md
/sp.plan < Phase 2 prompt from speckit-prompts.md
# ... continue for each phase
```

---

## Workflow 2: Laravel Application Build

**Scenario:** Building a Laravel application with distinct phases. You want to maintain consistency across phases while treating each independently.

**Input Document:** `specs/admin-dashboard/plan.md`

```markdown
# Admin Dashboard – Development Plan

## Phase 1 – Requirements & User Stories
**Objective**
Document all admin workflows and use cases.

**High-Level Scope**
- Admin authentication and role-based access
- Dashboard home view with KPIs
- User management interface
- Report generation and export
- Activity logging and audit trails

**Outcome**
- Detailed user stories with acceptance criteria
- Wireframes of all admin screens
- Data requirements identified

## Phase 2 – Database Design & Models
**Objective**
Design the database schema and Laravel Eloquent models.

**High-Level Scope**
- Database schema for users, roles, permissions
- Relationship design (HasMany, BelongsToMany)
- Model factories and seeders for testing
- Migration strategy for safe deployment

**Outcome**
- Complete database schema
- Eloquent models with relationships
- Factories and seeders for development

## Phase 3 – API & Endpoints
**Objective**
Design REST API endpoints for admin operations.

**High-Level Scope**
- API authentication (Sanctum / Fortify)
- CRUD endpoints for all resources
- Filtering, sorting, and pagination
- Rate limiting and security headers
- API versioning strategy

**Outcome**
- Complete API specification
- OpenAPI/Swagger documentation
- Security review completed

## Phase 4 – Frontend & Inertia Pages
**Objective**
Build the Vue 3 frontend using Inertia and Tailwind.

**High-Level Scope**
- Dashboard layout and navigation
- Vue components for all admin screens
- Form validation and error handling
- Real-time data updates using Inertia polling
- Responsive design and accessibility

**Outcome**
- Fully functional admin interface
- All components tested in isolation
- Dark mode support verified

## Phase 5 – Testing & Deployment
**Objective**
Ensure quality and readiness for production.

**High-Level Scope**
- Unit tests for models and services
- Feature tests for API endpoints
- Browser tests for frontend workflows
- Performance profiling and optimization
- Deployment strategy and rollback plan

**Outcome**
- Test coverage above 80%
- All workflows tested end-to-end
- Production deployment checklist complete
```

**Skill Invocation:**
```
Generate Speckit prompts from: specs/admin-dashboard/plan.md
```

**Output:** `specs/admin-dashboard/speckit-prompts.md`

Contains 5 prompts, each ready to guide the corresponding Speckit command.

**Execution Flow:**
```
1. /sp.specify (Phase 1 – Requirements)
   → Creates detailed spec for admin dashboard

2. /sp.plan (Phase 2 – Database Design)
   → Plans database schema and model architecture

3. /sp.plan (Phase 3 – API & Endpoints)
   → Plans REST API design and security

4. /sp.plan (Phase 4 – Frontend & Inertia)
   → Plans Vue 3 component structure and state

5. /sp.plan (Phase 5 – Testing & Deployment)
   → Plans testing strategy and deployment workflow
```

---

## Workflow 3: Existing Plan Refinement

**Scenario:** You have an existing `plan.md` but want to regenerate prompts after refining the plan.

**Steps:**

1. Edit your existing plan file to clarify objectives and scope
2. Re-run the skill:
   ```
   Generate Speckit prompts from: specs/my-feature/plan.md
   ```
3. Review the regenerated `speckit-prompts.md`
4. Use prompts with updated context

**Why:** As plans evolve, prompt quality improves. Re-generating captures the latest intent.

---

## Workflow 4: Quick Iteration During Planning

**Scenario:** You're mid-planning and want to test a prompt without committing the entire plan.

**Steps:**

1. Copy one phase from your plan:
   ```
   ## Phase 2 – System Architecture
   [content]
   ```

2. Create a temporary test file: `test-phase.md`

3. Run the skill:
   ```
   Generate Speckit prompts from: test-phase.md
   ```

4. Review the generated prompt

5. If satisfied, integrate back into main plan and regenerate all prompts

---

## Workflow 5: Multi-Document Integration

**Scenario:** You have multiple documents (requirements, architecture docs, implementation guide) that should be consolidated into a single plan with prompts.

**Steps:**

1. Create a new master plan file that consolidates all phases:
   ```
   specs/feature-name/plan.md
   ```

2. Copy phase sections from each source document

3. Run the skill once on the consolidated plan:
   ```
   Generate Speckit prompts from: specs/feature-name/plan.md
   ```

4. Output `speckit-prompts.md` now reflects all consolidated phases

---

## Example Outputs

### Phase 1 Spec Prompt (Requirements)
```
Implement Phase 1: Requirements Gathering. Identify and document
all functional and non-functional requirements for the admin
dashboard, including authentication, role-based access control,
user management, reporting, and audit logging. Ensure requirements
are comprehensive and testable, stakeholders have reviewed and
approved them, and success metrics are defined for each feature area.
```

### Phase 2 Plan Prompt (Architecture)
```
Design the technical architecture for Phase 2: Database Design & Models.
Plan the database schema for users, roles, and permissions with
appropriate relationships (HasMany, BelongsToMany, Polymorphic).
Design Laravel Eloquent models with proper relationship methods,
type hints, and casting. Create factories and seeders for development
and testing workflows. Address migration safety, including strategies
for altering schema without downtime and supporting rollback. Ensure
the data model is normalized, performant, and extensible for future
permission types.
```

### Phase 3 Plan Prompt (API Design)
```
Design the technical architecture for Phase 3: API & Endpoints. Plan
REST API endpoints following RESTful conventions for all admin resources.
Implement authentication using Laravel Sanctum with token-based
authorization and role-based access control. Design endpoints for
filtering, sorting, pagination, and bulk operations. Address API
versioning, rate limiting, and security headers to prevent common
attacks (CSRF, XSS, injection). Ensure API responses are consistent,
errors are actionable, and documentation is comprehensive and
maintainable.
```

---

## Tips for Best Results

### 1. Clear Phase Titles
Use consistent naming:
```
✅ ## Phase 1 – Requirements Gathering
✅ ## Phase 2 – System Architecture
❌ ## Step 1: Requirements
❌ ## Architecture Design (no phase number)
```

### 2. Explicit Objectives & Scope
```
✅ **Objective**: Ensure all payment workflows are documented
✅ **High-Level Scope**
   - Merchant onboarding
   - Payment processing
   - Refunds and disputes

❌ **What**: Requirements
❌ Just descriptions with no structure
```

### 3. Clear Outcomes
```
✅ **Outcome**
   - Comprehensive requirements document
   - Stakeholder approval obtained
   - Success metrics defined

❌ Requirements gathered
❌ Vague or unmeasurable outcomes
```

### 4. Consistent Formatting
- Use `## Phase X – Title` format
- Use `**Bold**` for section headers
- Use bullet points for scope and outcomes
- Keep formatting consistent across all phases

### 5. Reasonable Phase Count
- 3–7 phases: Optimal for most features
- 10+ phases: Consider grouping into meta-phases
- 1–2 phases: May be too simple; consider breaking down

---

## Troubleshooting

### Problem: "No phases found in plan document"
**Solution:** Ensure your document uses heading patterns like:
```
## Phase 1 – Title
## Phase 2 – Title
```

Not:
```
# Phase 1 – Title (top-level, might not be detected)
PHASE 1 – TITLE (no heading)
Phase 1 - Title (might need exact – symbol)
```

### Problem: Generated prompts are too short or vague
**Solution:** Ensure each phase includes:
- Clear **Objective** section
- **High-Level Scope** with 4+ items
- Clear **Outcome** with measurable results

More detailed input → More detailed output

### Problem: Output file not found
**Solution:** Check file permissions in the output directory. The skill writes to the same directory as the input plan by default.

### Problem: Prompts don't match my intent
**Solution:** Edit the source plan to clarify intent, then regenerate. The skill learns from structure and content clarity.
