#!/usr/bin/env python3
"""
Speckit Prompt Generator Script

Parses a structured plan document (Markdown with phases/steps) and generates
high-quality, paragraph-style Speckit-compatible prompts (/sp.specify and /sp.plan).

Usage:
    python generate_prompts.py /path/to/plan.md
    python generate_prompts.py /path/to/plan.md /output/path/speckit-prompts.md

Output: Consolidated Markdown file with all generated prompts ready for Speckit.
"""

import re
import sys
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Tuple


class PromptGenerator:
    """Analyzes plan documents and generates Speckit-compatible prompts."""

    def __init__(self, plan_content: str, plan_path: str = None):
        self.plan_content = plan_content
        self.plan_path = plan_path
        self.phases = self._extract_phases()

    def _extract_phases(self) -> List[Dict]:
        """Extract phases/steps from plan content."""
        phases = []

        # Pattern: ## Phase X – <Title> or similar heading patterns
        phase_pattern = r'^#+\s+(?:Phase|Step|Section)?\s*(\d+)?\s*(?:–|-|:)?\s*(.+?)$'

        lines = self.plan_content.split('\n')
        current_phase = None
        content_buffer = []

        for i, line in enumerate(lines):
            match = re.match(phase_pattern, line, re.IGNORECASE)

            if match:
                # Save previous phase if exists
                if current_phase is not None:
                    current_phase['content'] = '\n'.join(content_buffer).strip()
                    phases.append(current_phase)
                    content_buffer = []

                # Start new phase
                phase_num = match.group(1) or len(phases) + 1
                phase_title = match.group(2).strip()

                current_phase = {
                    'number': int(phase_num),
                    'title': phase_title,
                    'content': '',
                    'heading_level': len(re.match(r'^#+', line).group()),
                }
            elif current_phase is not None:
                content_buffer.append(line)

        # Save last phase
        if current_phase is not None:
            current_phase['content'] = '\n'.join(content_buffer).strip()
            phases.append(current_phase)

        return sorted(phases, key=lambda p: p['number'])

    def _extract_intent(self, phase_content: str) -> Tuple[str, str, str]:
        """Extract objective, scope, and outcomes from phase content."""
        objective = ""
        scope = ""
        outcome = ""

        lines = phase_content.split('\n')

        # Look for Objective, Scope, Outcome sections
        current_section = None
        section_content = []

        for line in lines:
            if re.match(r'^\*?\*?Objective\*?\*?', line, re.IGNORECASE):
                current_section = 'objective'
                continue
            elif re.match(r'^\*?\*?Scope\*?\*?|^\*?\*?High-Level Scope\*?\*?', line, re.IGNORECASE):
                current_section = 'scope'
                continue
            elif re.match(r'^\*?\*?Outcome\*?\*?', line, re.IGNORECASE):
                current_section = 'outcome'
                continue
            elif line.strip().startswith('*') or line.strip().startswith('-'):
                # Bullet point
                if current_section:
                    section_content.append(line.strip().lstrip('*- '))
            elif line.strip() == '':
                continue
            else:
                # Regular text
                if current_section and section_content:
                    pass  # Continue collecting for current section
                else:
                    if current_section:
                        text = ' '.join(section_content).strip()
                        if current_section == 'objective':
                            objective = text
                        elif current_section == 'scope':
                            scope = text
                        elif current_section == 'outcome':
                            outcome = text
                        section_content = []
                        current_section = None

        # Capture final section
        text = ' '.join(section_content).strip()
        if current_section == 'objective':
            objective = text
        elif current_section == 'scope':
            scope = text
        elif current_section == 'outcome':
            outcome = text

        return objective, scope, outcome

    def _determine_prompt_type(self, phase_num: int) -> str:
        """Determine if phase should use /sp.specify or /sp.plan."""
        # First phase typically spec, others plan
        # Can be enhanced with heuristics based on keywords
        if phase_num == 1:
            return "spec"
        return "plan"

    def generate_prompt(self, phase: Dict) -> str:
        """Generate a high-quality Speckit prompt for a phase."""
        objective, scope, outcome = self._extract_intent(phase['content'])
        prompt_type = self._determine_prompt_type(phase['number'])

        # Build prompt
        prompt_parts = []

        # Opening statement
        opening = f"Implement Phase {phase['number']}: {phase['title']}."
        prompt_parts.append(opening)

        # Add objective if available
        if objective:
            objective_clean = objective.replace('Objective: ', '').strip()
            if objective_clean:
                prompt_parts.append(objective_clean + ".")

        # Add scope interpretation
        if scope:
            scope_items = [item.strip() for item in scope.split('\n') if item.strip()]
            if scope_items:
                scope_text = " ".join(scope_items)
                if not scope_text.endswith('.'):
                    scope_text += "."
                prompt_parts.append(scope_text)

        # Add outcomes with emphasis
        if outcome:
            outcome_items = [item.strip() for item in outcome.split('\n') if item.strip()]
            if outcome_items:
                outcome_text = "Ensure " + ", ".join(outcome_items) + "."
                prompt_parts.append(outcome_text)

        # Join and refine
        prompt_text = " ".join(prompt_parts)

        # Clean up common patterns
        prompt_text = re.sub(r'\.+', '.', prompt_text)  # Remove multiple periods
        prompt_text = re.sub(r'\s+', ' ', prompt_text)  # Remove extra whitespace

        # Trim to reasonable length if too long
        if len(prompt_text) > 500:
            # Keep first 450 chars and end at sentence boundary
            truncated = prompt_text[:450]
            last_period = truncated.rfind('.')
            if last_period > 400:
                prompt_text = truncated[:last_period + 1]

        return prompt_text.strip()

    def generate_all_prompts(self) -> List[Dict]:
        """Generate prompts for all phases."""
        prompts = []
        for phase in self.phases:
            prompt_text = self.generate_prompt(phase)
            prompts.append({
                'number': phase['number'],
                'title': phase['title'],
                'type': self._determine_prompt_type(phase['number']),
                'prompt': prompt_text,
            })
        return prompts

    def render_output(self, prompts: List[Dict]) -> str:
        """Render prompts to Markdown output."""
        lines = []

        # Header
        lines.append("# Speckit Prompts")
        lines.append("")
        lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        if self.plan_path:
            lines.append(f"Source: `{self.plan_path}`")
        lines.append(f"Total Prompts: {len(prompts)}")
        lines.append("")

        # Index
        lines.append("## Index")
        lines.append("")
        for p in prompts:
            anchor = f"prompt-{p['number']}"
            lines.append(f"- [{p['type'].upper()} – Phase {p['number']}: {p['title']}](#{anchor})")
        lines.append("")

        # Prompts
        lines.append("## Prompts")
        lines.append("")
        for p in prompts:
            anchor = f"prompt-{p['number']}"
            prompt_type_label = "Spec" if p['type'] == 'spec' else "Plan"
            lines.append(f"### {prompt_type_label} Prompt: Phase {p['number']} – {p['title']}")
            lines.append(f"{{#{anchor}}}")
            lines.append("")
            lines.append(f"**Command:** `/sp.{p['type']}`")
            lines.append("")
            lines.append(f"**Prompt:**")
            lines.append("")
            lines.append(f"> {p['prompt']}")
            lines.append("")
            lines.append("---")
            lines.append("")

        return '\n'.join(lines)


def main():
    if len(sys.argv) < 2:
        print("Usage: python generate_prompts.py <input_plan_path> [output_path]")
        print("Example: python generate_prompts.py /path/to/plan.md")
        sys.exit(1)

    input_path = Path(sys.argv[1])

    if not input_path.exists():
        print(f"Error: File not found: {input_path}")
        sys.exit(1)

    # Read plan content
    plan_content = input_path.read_text(encoding='utf-8')

    # Generate prompts
    generator = PromptGenerator(plan_content, str(input_path))
    prompts = generator.generate_all_prompts()

    if not prompts:
        print("Error: No phases found in plan document.")
        print("Ensure your plan uses headings like: ## Phase 1 – Title")
        sys.exit(1)

    # Render output
    output_content = generator.render_output(prompts)

    # Determine output path
    if len(sys.argv) > 2:
        output_path = Path(sys.argv[2])
    else:
        output_path = input_path.parent / "speckit-prompts.md"

    # Write output
    output_path.write_text(output_content, encoding='utf-8')
    print(f"✓ Generated {len(prompts)} prompts")
    print(f"✓ Saved to: {output_path}")


if __name__ == '__main__':
    main()
