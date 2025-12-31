---
name: speckit-prompt-generator
description: "Generate high-quality, paragraph-style specification and planning prompts compatible with Speckit (Spec-Driven Development) from structured plan documents. Generates TWO prompts per phase (spec + plan) for complete coverage. Translates multi-phase plans into executable prompts for /sp.specify and /sp.plan commands. Use when you have a plan document (spec.md, plan.md, or phase outline) with clear steps/phases and need to generate corresponding Speckit-compatible prompts that can be directly executed. Outputs all prompts in a single consolidated Markdown file with clear labeling, ready for immediate use. Total output: N phases = 2N prompts."
---

# Speckit Prompt Generator

## Quick Start

Provide a path to your plan document (typically `plan.md`, `spec.md`, or a phase outline) that contains clear, sequential steps or phases. The skill will analyze the document, extract each step/phase, and generate **TWO prompts per phase** (spec + plan).

**Usage:**
```
Generate Speckit prompts from: /path/to/plan.md
```

Or paste plan content directly:
```
Generate Speckit prompts for this plan:

## Phase 1 – Requirements
...

## Phase 2 – Architecture
...
```

> **⚠️ Important**: For a plan with **N phases**, the skill generates **2N prompts** (one spec prompt and one plan prompt for each phase). Example: 8 phases = 16 total prompts.

## What This Skill Does

The skill performs these steps automatically:

1. **Parse the plan document** – Identifies all steps, phases, or logical sections
2. **Extract intent and scope** – Captures the objective, outcomes, and high-level scope of each phase
3. **Generate TWO prompts per phase** – Creates both a spec prompt (WHAT to build) and a plan prompt (HOW to build)
4. **Consolidate output** – Saves all prompts to a single Markdown file in the same directory as the input plan
5. **Label clearly** – Each prompt is labeled with its phase number, type (spec/plan), and title for easy reference

### 🎯 Critical: Two Prompts Per Phase

For each phase in your plan, the skill generates **TWO separate prompts**:

1. **Spec Prompt** (`/sp.specify`)
   - Defines **WHAT** needs to be built
   - Focuses on requirements, acceptance criteria, and expected outcomes
   - Specifies constraints, dependencies, and success measures
   - Example: "Specify a database schema with three core tables..."

2. **Plan Prompt** (`/sp.plan`)
   - Defines **HOW** to build it
   - Focuses on architecture, implementation steps, and technical decisions
   - Details the execution strategy and approach
   - Example: "Plan the implementation of database migrations..."

**Total Output**: For a plan with 8 phases, you get **16 prompts** (8 spec + 8 plan)

## Output Format

The skill generates a Markdown file named `speckit-prompts.md` (or similar) containing:

- **File header** with metadata (source plan, generation date, total prompts)
- **Index** organized by phase, listing both spec and plan prompts with links
- **Prompt sections** clearly labeled in pairs:
  - `## Phase 1: [Phase Name]`
    - `### Spec Prompt: Phase 1 – <Title>`
    - `### Plan Prompt: Phase 1 – <Title>`
  - `## Phase 2: [Phase Name]`
    - `### Spec Prompt: Phase 2 – <Title>`
    - `### Plan Prompt: Phase 2 – <Title>`
  - etc.

Each prompt is a well-written paragraph (no bullet lists) that:
- Opens with clarity on the phase objective and scope
- Chains requirements logically and hierarchically
- **Spec prompts** emphasize WHAT, requirements, acceptance criteria, and constraints
- **Plan prompts** emphasize HOW, implementation steps, architecture, and technical decisions
- Concludes with actionable guidance for the Speckit command

## Prompt Quality Standards

Generated prompts adhere to these principles:

- **Paragraph form** – Flowing prose, no bullet points (Speckit works better with narrative prompts)
- **Intent-focused** – Emphasizes "why" and "what" outcomes, not implementation details
- **Concise** – ~60–120 words per prompt for spec prompts; ~100–150 words for plan prompts
- **Outcome-driven** – Repeats key success criteria and constraints
- **Logically chained** – Requirements build on each other in a sensible order
- **Avoids code/details** – No implementation specifics, only high-level architectural guidance

## Customization

The skill operates fully automatically. No user customization is required. Simply provide the plan document and the skill will generate all prompts.

If you want to refine generated prompts after output, you can:
- Edit the output file directly to adjust tone or emphasis
- Re-run the skill with a revised plan document
- Provide feedback on the output to improve future generations

## Example Workflow

**Input:** A plan document with 3 phases
```markdown
## Phase 1 – Requirements Gathering
## Phase 2 – System Architecture
## Phase 3 – Data Modeling
```

**Output:** `speckit-prompts.md` containing **6 prompts total** (2 per phase):
```markdown
# Speckit Prompts - My Project
**Total Prompts**: 6 (3 phases × 2 prompts each)

## Phase 1: Requirements Gathering

### Spec Prompt: Phase 1 – Requirements Gathering
Specify comprehensive requirements for the system including user stories,
acceptance criteria, constraints, and success metrics...

**Command**: `/sp.specify "[paste this prompt]"`

### Plan Prompt: Phase 1 – Requirements Gathering
Plan the requirements gathering process by scheduling stakeholder interviews,
creating documentation templates, and establishing validation workflows...

**Command**: `/sp.plan "[paste this prompt]"`

## Phase 2: System Architecture

### Spec Prompt: Phase 2 – System Architecture
Specify the system architecture requirements including scalability targets,
security constraints, integration points, and performance criteria...

**Command**: `/sp.specify "[paste this prompt]"`

### Plan Prompt: Phase 2 – System Architecture
Plan the architecture implementation by designing the component topology,
defining service boundaries, selecting technologies, and documenting patterns...

**Command**: `/sp.plan "[paste this prompt]"`

...
```

**Workflow for each phase:**
1. Copy the **spec prompt** → Run `/sp.specify`
2. Copy the **plan prompt** → Run `/sp.plan`
3. Continue with `/sp.tasks` and `/sp.implement`

## File Location & Naming

- **Input**: Provide the absolute path to your plan document (e.g., `C:\path\to\plan.md`)
- **Output**: Saved as `speckit-prompts.md` in the same directory as the input plan
- **Example**: If plan is at `specs/my-feature/plan.md`, output is at `specs/my-feature/speckit-prompts.md`

## Common Scenarios

### Multi-Phase Laravel Application
Provide a plan with phases like "Authentication," "Database Setup," "API Endpoints," "Frontend," "Testing." The skill generates prompts that maintain overall consistency while treating each phase independently.

### Feature Development Workflow
Provide a phased approach (Requirements → Design → Implementation → Testing). The skill generates prompts that guide Speckit through the entire feature lifecycle.

### Complex System Architecture
Provide detailed phases covering different system concerns (Webhooks, Persistence, Sync, Receipts). The skill generates architectural prompts that balance depth with clarity.

## Success Criteria

A successful run produces:

- ✅ One consolidated Markdown file with all prompts
- ✅ **TWO prompts per phase** (one spec, one plan)
- ✅ **Total prompts = phases × 2** (e.g., 8 phases = 16 prompts)
- ✅ Clear labeling for each prompt (phase number, type, title)
- ✅ Paragraph-style prompts (no bullet lists)
- ✅ Spec prompts focus on WHAT (requirements, acceptance criteria)
- ✅ Plan prompts focus on HOW (implementation, architecture)
- ✅ Prompts are ready to use with Speckit commands immediately
- ✅ Each prompt captures the phase's objective, scope, and expected outcomes
- ✅ All prompts follow consistent tone and quality standards

## Tips & Best Practices

1. **Provide clear phase titles** – Titles like "Phase 1 – Webhooks, Transactions & Receipts" work best
2. **Include objectives and scope** – Plans with explicit objectives and high-level scope are processed more accurately
3. **Use consistent formatting** – Heading levels and structure help the skill parse phases correctly
4. **Reference the output file** – After generation, keep the `speckit-prompts.md` file alongside your plan for easy access
5. **Iterate as needed** – If you refine your plan, re-run the skill to regenerate prompts
