# Speckit Prompt Generator – Implementation Summary

## Overview

The **speckit-prompt-generator** skill is a reusable Claude skill that generates high-quality, paragraph-style specification and planning prompts compatible with Speckit (Spec-Driven Development).

**Primary Purpose:** Transform structured, multi-phase plan documents into executable, AI-ready prompts for `/sp.specify` and `/sp.plan` commands.

## Skill Structure

```
speckit-prompt-generator/
├── SKILL.md                          (Skill definition & user guide)
├── scripts/
│   └── generate_prompts.py          (Python script for prompt generation)
├── references/
│   ├── prompt-quality-standards.md  (Quality guidelines & patterns)
│   └── workflows.md                 (Real-world usage examples)
└── assets/
    └── example-output.md            (Sample generated output)
```

### File Descriptions

#### SKILL.md (Primary Skill Definition)
- **Role:** Main user-facing documentation for the skill
- **Contents:**
  - YAML frontmatter with `name` and `description`
  - Quick start guide for users
  - What the skill does (5-step process)
  - Output format specification
  - Prompt quality standards (embedded)
  - Customization options
  - File location & naming conventions
  - Common scenarios and success criteria
  - Tips & best practices

#### scripts/generate_prompts.py
- **Role:** Executable Python script for prompt generation
- **Functionality:**
  - Parses Markdown plan documents
  - Extracts phases/steps with objectives, scopes, and outcomes
  - Generates high-quality paragraph-style prompts
  - Renders consolidated Markdown output
  - Supports command-line execution
- **Usage:**
  ```bash
  python generate_prompts.py /path/to/plan.md [output_path]
  ```
- **Key Classes:**
  - `PromptGenerator` – Main orchestrator
  - Methods for phase extraction, intent analysis, prompt generation

#### references/prompt-quality-standards.md
- **Role:** Reference guide for prompt quality and design patterns
- **Contents:**
  - 5 core principles (paragraph form, intent-first, concise, chained, constrained)
  - Prompt structure templates for spec and plan prompts
  - Common prompt patterns (security, integration, multi-phase, quality)
  - Anti-patterns (what NOT to do)
  - Quality checklist
  - Example generation process with analysis

#### references/workflows.md
- **Role:** Real-world workflow examples and use cases
- **Contents:**
  - 5 complete workflow scenarios:
    1. Multi-phase feature development
    2. Laravel application build
    3. Existing plan refinement
    4. Quick iteration during planning
    5. Multi-document integration
  - Example outputs for each workflow
  - Tips for best results (6 recommendations)
  - Troubleshooting guide

#### assets/example-output.md
- **Role:** Sample generated output showing format and quality
- **Contents:**
  - Example output from a 5-phase payment processing plan
  - Index of all generated prompts
  - 5 complete prompts demonstrating:
    - Spec prompt format (Phase 1)
    - Plan prompt format (Phases 2–5)
    - Logical chaining and emphasis
  - Usage instructions
  - Next steps for execution

## How Users Interact with the Skill

### Trigger Pattern
The skill activates when users request prompt generation from plan documents:

- `"Generate Speckit prompts from: /path/to/plan.md"`
- `"Create Speckit prompts for my plan"`
- `"Turn my phase plan into /sp.specify and /sp.plan prompts"`

### Workflow
1. **User provides** a structured plan document (file path or pasted content)
2. **Skill reads** SKILL.md (main instructions)
3. **Skill analyzes** the plan structure
4. **Skill generates** paragraph-style prompts
5. **Skill outputs** consolidated Markdown file with all prompts
6. **User takes** each prompt and runs `/sp.specify` or `/sp.plan`

### Output
A single consolidated Markdown file (`speckit-prompts.md`) containing:
- Metadata (source, generation date, total prompts)
- Index with links to each prompt
- Clearly labeled prompt sections with:
  - Phase number and title
  - Command type (spec or plan)
  - Full prompt text in paragraph form

## Key Features

### ✅ Fully Automated
- No user interaction required beyond providing the plan document
- Automatic phase detection and prompt generation
- Consistent formatting and quality standards

### ✅ Smart Phase Analysis
- Detects phase structure from Markdown headings
- Extracts objectives, scope, and outcomes
- Determines appropriate prompt type (spec vs. plan)
- Chains requirements logically

### ✅ High-Quality Output
- Paragraph-style prompts (no bullet lists) optimized for Speckit
- Intent and outcome focused, not implementation details
- Consistent tone and quality across all prompts
- 60–150 word length appropriate for Speckit commands

### ✅ Progressive Disclosure
- **SKILL.md:** Quick start + essential guidance (~5k words)
- **References:** Detailed patterns and workflows (loaded as needed)
- **Scripts:** Executable generation logic (can run without loading into context)
- **Assets:** Example output for reference

### ✅ Reusable Resources
- `generate_prompts.py` can be run independently
- Prompt quality standards can be shared with teams
- Workflows provide proven usage patterns
- Example output demonstrates expected results

## Design Principles Applied

### 1. Concise is Key
- SKILL.md keeps essential info for triggering and quick start
- Detailed content (patterns, workflows) in separate reference files
- Script is self-contained and executable

### 2. Set Appropriate Degrees of Freedom
- **Low freedom (script):** Prompt generation algorithm is deterministic
- **Medium freedom (SKILL.md):** Users choose between file path or pasted content
- **High freedom (references):** Workflow examples show multiple valid use cases

### 3. Progressive Disclosure
- Metadata always in context (name + description)
- SKILL.md loaded when skill triggers
- References loaded as Claude determines they're needed
- Script executable without loading entire context

## Quality Standards Embedded in the Skill

### Prompt Quality Checklist
✅ Paragraph form (no bullet lists)
✅ Opens with clear phase and objective
✅ Chains requirements logically
✅ Emphasizes key success criteria
✅ References constraints/dependencies
✅ No implementation details
✅ 60–150 words
✅ Ends with actionable context
✅ Active voice & imperative mood
✅ Avoids unnecessary jargon

### Anti-Patterns to Avoid
❌ Bullet lists instead of prose
❌ Implementation-specific details
❌ Vague or unmeasurable outcomes
❌ Over-specification of technology
❌ Forgetting success criteria

## Use Cases

### 1. Multi-Phase Feature Development
Transform a detailed phase plan (5–7 phases) into prompts for systematic feature development using Speckit.

### 2. Laravel Application Build
Guide multi-phase application development (Requirements → Architecture → API → Frontend → Testing) with consistent, interconnected prompts.

### 3. Complex System Architecture
Break down complex systems (webhooks, persistence, synchronization) into manageable planning prompts.

### 4. Iterative Planning
Regenerate prompts as your plan evolves, capturing updated intent and scope.

### 5. Team Collaboration
Share generated prompts with team members to ensure everyone follows the same development phases.

## Technical Details

### Input Requirements
- Markdown document with clear phase structure
- Each phase should have:
  - **Heading** (## Phase X – Title)
  - **Objective** (brief description of why)
  - **Scope** (high-level items, usually bulleted)
  - **Outcome** (expected results, usually bulleted)

### Output Guarantee
- **Format:** Single consolidated Markdown file
- **Location:** Same directory as input plan
- **Naming:** `speckit-prompts.md` (or custom if specified)
- **Contents:**
  - Metadata header
  - Index with links
  - Numbered prompt sections
  - Each prompt ready for `/sp.specify` or `/sp.plan`

### Error Handling
Script provides clear error messages for:
- Missing input file
- No phases detected
- File write permission issues

## How This Skill Fits into SDD

The speckit-prompt-generator is a **supporting tool** in Spec-Driven Development workflows:

1. **Phases:** Align with SDD's multi-phase approach (spec → plan → tasks → implementation)
2. **Reusability:** Prompts are designed to be reused and refined across projects
3. **Consistency:** Standardized prompt format ensures consistent Speckit output
4. **Documentation:** Outputs (specs, plans) are version-controlled artifacts

## Testing & Validation

The skill has been validated with:
- ✅ Example payment processing plan (5 phases)
- ✅ Example Laravel admin dashboard plan (5 phases)
- ✅ Generated prompts reviewed against quality standards
- ✅ Output format and structure verified
- ✅ Reference materials tested for clarity and completeness

## Future Enhancements (Optional)

Potential improvements for future versions:
1. **Multi-format input:** Support YAML, JSON, or structured text
2. **Custom prompt templates:** Allow users to define prompt patterns
3. **Batch processing:** Generate prompts for multiple plans
4. **Validation:** Check generated prompts against quality standards
5. **Integration:** Direct `/sp.specify` or `/sp.plan` invocation from output

## Summary

The **speckit-prompt-generator** skill successfully fulfills all requirements:

✅ **Single responsibility:** Generates high-quality Speckit-compatible prompts from structured plans
✅ **Reusable:** Can be used for any multi-phase project or feature
✅ **Paragraph-style output:** Optimized for Speckit command processing
✅ **Consolidated delivery:** Single Markdown file with all prompts
✅ **Production-ready:** Includes Python script, quality standards, workflows, and examples
✅ **Well-documented:** SKILL.md, references, workflows, and example output

The skill is ready for immediate use with Speckit workflows.
