# Speckit Prompt Generator – Skill Documentation

**A reusable Claude skill that transforms structured plan documents into high-quality, paragraph-style Speckit-compatible prompts.**

## Quick Overview

The `speckit-prompt-generator` skill analyzes multi-phase plan documents and generates executable prompts for `/sp.specify` and `/sp.plan` commands. It's designed to support Spec-Driven Development (SDD) workflows by automating the translation from planning phase → implementation phase.

**In one sentence:** Turn your phase plan into ready-to-use Speckit prompts (2 prompts per phase: spec + plan).

## What Problem Does This Solve?

When using Spec-Driven Development, you often have:
- A detailed plan with multiple phases (e.g., Requirements → Architecture → API Design → Frontend)
- The need to run separate `/sp.specify` and `/sp.plan` commands for **each phase**
- Each phase requires **TWO prompts**: one for spec (WHAT) and one for plan (HOW)
- Desire for consistency and quality across all generated prompts

**The Challenge:** Writing individual spec AND plan prompts for each phase is time-consuming and error-prone. For 8 phases, that's 16 prompts to write manually!

**The Solution:** Provide your plan document → Get back **all prompts at once** (2 per phase) → Run them through Speckit sequentially.

## Key Features

| Feature | Benefit |
|---------|---------|
| **Fully Automated** | No user interaction needed; just provide your plan |
| **High Quality** | Prompts follow proven patterns and quality standards |
| **Paragraph Form** | Optimized for Speckit AI processing (not bullet lists) |
| **Consolidated Output** | Single Markdown file with all prompts, ready to use |
| **Intent-Focused** | Emphasizes outcomes and constraints, not implementation details |
| **Reusable** | Works with any multi-phase project |

## Skill Components

```
speckit-prompt-generator/
├── SKILL.md                           ← Start here (user-facing guide)
├── scripts/generate_prompts.py        ← Executable Python script
├── references/
│   ├── prompt-quality-standards.md    ← Design patterns & guidelines
│   └── workflows.md                   ← Real-world examples
├── assets/
│   └── example-output.md              ← Sample generated output
├── IMPLEMENTATION_SUMMARY.md          ← Technical overview
├── PACKAGING_GUIDE.md                 ← Distribution instructions
└── README.md                          ← This file
```

## Installation

1. **Locate your skills directory:**
   - macOS/Linux: `~/.claude/skills/`
   - Windows: `C:\Users\<YourUsername>\.claude\skills\`

2. **Place the skill file:**
   ```bash
   cp speckit-prompt-generator.skill ~/.claude/skills/
   ```

3. **Restart Claude Code** or reload skills

4. **Done!** Skill is ready to use

## Usage – Quick Start

### Step 1: Create a Plan Document

```markdown
# My Feature Plan

## Phase 1 – Requirements Gathering

**Objective**
Understand all user needs and constraints.

**High-Level Scope**
- User stories and use cases
- Non-functional requirements
- Acceptance criteria
- External dependencies

**Outcome**
- Requirements document approved
- Stakeholder sign-off obtained
- Success metrics defined

## Phase 2 – System Architecture

**Objective**
Design the technical foundation.

**High-Level Scope**
- System topology and components
- Database schema
- API contracts
- Security model

**Outcome**
- Architecture diagram with clear boundaries
- API specifications documented
- Security review completed
```

### Step 2: Generate Prompts

In Claude Code, use the skill:

```
Generate Speckit prompts from: /path/to/my-feature-plan.md
```

### Step 3: Review Output

The skill creates `speckit-prompts.md` in the same directory with all prompts ready to use.

### Step 4: Use with Speckit

```bash
# For EACH PHASE, run BOTH prompts in order:

# Phase 1:
/sp.specify
# Paste Phase 1 SPEC prompt

/sp.plan
# Paste Phase 1 PLAN prompt

# Phase 2:
/sp.specify
# Paste Phase 2 SPEC prompt

/sp.plan
# Paste Phase 2 PLAN prompt

# Continue for all phases...
# Total commands = phases × 2
```

## Example Output

Here's what the generated prompts look like for **one phase**:

### Spec Prompt (WHAT to build)
```
Specify the system architecture requirements for Phase 2: System Architecture.
The architecture must support high availability with 99.9% uptime, handle 10,000
concurrent users, maintain data consistency across distributed services, and
integrate with existing authentication and payment systems. Define clear service
boundaries, API contracts with versioning, security requirements including
encryption at rest and in transit, and monitoring requirements for observability.
Success criteria include approved architecture diagrams, documented API contracts,
security review completion, and stakeholder sign-off on scalability targets.
```

### Plan Prompt (HOW to build it)
```
Plan the implementation of the system architecture for Phase 2: System Architecture.
Design the overall system topology separating concerns with clear service boundaries
and communication protocols. Design the database schema to support transaction history,
idempotency keys, and status tracking. Define API contracts for service interactions
ensuring consistency and versioning. Select appropriate technologies for the tech stack
based on scalability and team expertise. Address failure modes including retries,
rollback, and state reconciliation to ensure reliability and data consistency throughout.
Document the architecture with diagrams showing component interactions and data flows.
```

Notice the difference:
- **Spec Prompt**: Focuses on requirements, constraints, success criteria, what needs to be achieved
- **Plan Prompt**: Focuses on implementation steps, technical approach, how to achieve it
- Both are paragraph form (not bullets)
- Both have clear objectives and logical flow
- Both emphasize outcomes and quality standards
- Both ready to use with their respective Speckit commands

## How to Write Good Plan Documents

For the skill to generate optimal prompts, your plan should include:

### ✅ Required Structure

Each phase needs:
```markdown
## Phase X – Phase Title

**Objective**
Why this phase exists; what it accomplishes.

**High-Level Scope**
- Item 1
- Item 2
- Item 3
- Item 4 (ideally 4+ items)

**Outcome**
- Expected result 1
- Expected result 2
- Expected result 3
```

### ✅ Phase Numbering
```markdown
## Phase 1 – Requirements
## Phase 2 – Architecture
## Phase 3 – Implementation
```

### ❌ What Doesn't Work

```markdown
# Requirements (missing phase number)
PHASE 1 (all caps, no heading syntax)
Phase 1: (colon instead of – dash)
```

## Real-World Examples

See `references/workflows.md` for 5 complete examples:
1. Multi-phase feature development (5 phases)
2. Laravel application build (5 phases)
3. Existing plan refinement
4. Quick iteration during planning
5. Multi-document integration

## Quality Standards

All generated prompts follow proven quality standards:

| Standard | Example |
|----------|---------|
| **Paragraph form** | "Design the architecture by planning the topology..." |
| **Intent-first** | Emphasizes "why" and "what outcomes" not "how" |
| **Concise** | 60–150 words depending on complexity |
| **Logically chained** | Requirements build on each other |
| **Outcome-emphasized** | Repeats key success criteria |
| **No tech details** | Avoids specific framework/library names |

See `references/prompt-quality-standards.md` for complete guidance.

## Common Use Cases

### 1. Multi-Phase Feature
5–7 phase plan for a complex feature (e.g., payment processing, admin dashboard)
→ Generate all prompts at once
→ Run through Speckit sequentially

### 2. Multi-Service System
Multiple microservices or components, each with phases
→ Generate prompts for overall architecture
→ Generate prompts for each service

### 3. Framework/Stack Setup
Learning or setting up a new framework (Laravel, React, etc.)
→ Phase plan with setup steps
→ Generate prompts for configuration and best practices

### 4. Iterative Refinement
Refine your plan as you learn more
→ Regenerate prompts to capture updates
→ New prompts reflect evolved understanding

## Troubleshooting

### "No phases found in plan document"

**Check:**
- Headings are `## Phase X – Title` format
- Not `# Phase` (top-level heading)
- Not `PHASE 1` (plain text)

**Fix:**
```markdown
## Phase 1 – Requirements  ✅
## Phase 2 – Architecture  ✅
```

### "Output file not created"

**Check:**
- Write permission in output directory
- No file path typos
- Enough disk space

**Test:**
```bash
touch /path/to/directory/test.txt
```

### "Prompts are too short"

**Reason:** Plan has minimal detail
**Fix:** Add more to your **Objective**, **Scope**, and **Outcome** sections

### "Prompts don't match my intent"

**Solution:**
1. Edit your source plan to clarify intent
2. Re-run the skill
3. Generated prompts will improve

## Technical Details

### Input Requirements
- **Format:** Markdown (`.md`)
- **Structure:** Clear `## Phase X – Title` headings
- **Content:** Objective, Scope, Outcome sections for each phase
- **Size:** Works with 1–20+ phases

### Output Guarantee
- **Format:** Single consolidated Markdown file
- **Location:** Same directory as input plan
- **Naming:** `speckit-prompts.md` (or custom path)
- **Quality:** All prompts validated against quality standards

### Execution
- **Method:** Python 3.7+
- **Time:** < 1 second for typical 5-phase plan
- **Error Handling:** Clear messages for common issues

## Advanced Topics

### Running the Script Directly

Instead of using the skill, you can run the Python script directly:

```bash
python scripts/generate_prompts.py /path/to/plan.md [output_path]
```

**Use cases:**
- Integrate with your CI/CD pipeline
- Batch process multiple plans
- Custom output handling

### Customizing Prompts

After generation, prompts can be edited:

1. Generated output in `speckit-prompts.md`
2. Edit prompt text as needed
3. Copy individual prompts to `/sp.specify` or `/sp.plan`

### Regenerating After Plan Changes

Your plan will evolve as you develop. To regenerate:

1. Update your source plan
2. Re-run: `Generate Speckit prompts from: /path/to/updated-plan.md`
3. Review updated `speckit-prompts.md`

## Files in This Skill

| File | Purpose |
|------|---------|
| **SKILL.md** | User guide, quick start, usage examples |
| **scripts/generate_prompts.py** | Executable prompt generation script |
| **references/prompt-quality-standards.md** | Design patterns, anti-patterns, quality checklist |
| **references/workflows.md** | Real-world examples, tips, troubleshooting |
| **assets/example-output.md** | Sample generated output for reference |
| **IMPLEMENTATION_SUMMARY.md** | Technical overview and architecture |
| **PACKAGING_GUIDE.md** | Distribution and version management |
| **README.md** | This file – overview and quick reference |

## Support & Resources

### Start Here
- `SKILL.md` – Quick start and basic usage
- `example-output.md` – See what output looks like

### For Detailed Guidance
- `prompt-quality-standards.md` – Understand quality principles
- `workflows.md` – Real-world usage examples
- `IMPLEMENTATION_SUMMARY.md` – Technical details

### For Distribution
- `PACKAGING_GUIDE.md` – How to package and share the skill
- Version management and changelog guidance

## Contributing & Feedback

This skill was created to support Spec-Driven Development workflows. Feedback helps improve it:

- **What works well?** Share examples and use cases
- **What's missing?** Suggest new features or patterns
- **Found a bug?** Describe the issue and expected behavior
- **Ideas for improvement?** Tell us your thoughts

## Version Information

- **Version:** 1.0.0
- **Created:** 2025-12-31
- **Compatible with:** Claude Code, Speckit (Spec-Driven Development)
- **Python requirement:** 3.7+

## License

This skill is provided as-is for use with Claude Code and Speckit workflows.

---

## Quick Links

- 📖 **User Guide:** See `SKILL.md`
- 🎯 **Examples:** See `example-output.md`
- 📚 **Patterns:** See `references/prompt-quality-standards.md`
- 🛠️ **Workflows:** See `references/workflows.md`
- 📦 **Distribution:** See `PACKAGING_GUIDE.md`

---

**Ready to generate your first set of Speckit prompts?**

Create your plan document with clear phases, then ask:
```
Generate Speckit prompts from: /path/to/plan.md
```

The skill will handle the rest. Happy prompting! 🚀
