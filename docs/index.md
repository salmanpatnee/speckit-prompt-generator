---
layout: default
title: Speckit Prompt Generator
---

<style>
:root {
  --bg: #ffffff;
  --surface: #f8f9fa;
  --border: #e1e4e8;
  --text: #24292e;
  --text-secondary: #586069;
  --accent: #d97706;
  --accent-light: #fef3c7;
  --code-bg: #f6f8fa;
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica', 'Arial', sans-serif;
  line-height: 1.6;
  color: var(--text);
  background: var(--bg);
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
}

/* Header */
header {
  border-bottom: 1px solid var(--border);
  padding: 2rem 0;
  margin-bottom: 3rem;
}

.logo {
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--text);
}

.badges {
  margin-top: 1rem;
  display: flex;
  gap: 0.5rem;
  flex-wrap: wrap;
}

/* Hero */
.hero {
  margin-bottom: 4rem;
}

h1 {
  font-size: 3rem;
  font-weight: 700;
  margin-bottom: 1rem;
  line-height: 1.2;
}

.subtitle {
  font-size: 1.25rem;
  color: var(--text-secondary);
  margin-bottom: 2rem;
}

.highlight-box {
  background: var(--accent-light);
  border-left: 4px solid var(--accent);
  padding: 1.5rem;
  margin: 2rem 0;
  border-radius: 4px;
}

.stats {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1.5rem;
  margin: 2rem 0;
}

.stat {
  text-align: center;
  padding: 1.5rem;
  background: var(--surface);
  border-radius: 8px;
}

.stat-value {
  font-size: 2rem;
  font-weight: 700;
  color: var(--accent);
}

.stat-label {
  color: var(--text-secondary);
  margin-top: 0.5rem;
}

/* Sections */
section {
  margin: 4rem 0;
}

h2 {
  font-size: 2rem;
  margin-bottom: 1.5rem;
  font-weight: 700;
  border-bottom: 2px solid var(--border);
  padding-bottom: 0.5rem;
}

h3 {
  font-size: 1.5rem;
  margin-bottom: 1rem;
  font-weight: 600;
}

/* Grid */
.grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.5rem;
  margin: 2rem 0;
}

.card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 1.5rem;
  transition: box-shadow 0.2s;
}

.card:hover {
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}

.card h3 {
  margin-top: 0;
  color: var(--accent);
}

/* Code */
pre {
  background: var(--code-bg);
  border: 1px solid var(--border);
  border-radius: 6px;
  padding: 1rem;
  overflow-x: auto;
  margin: 1rem 0;
}

code {
  font-family: 'SF Mono', Monaco, 'Courier New', monospace;
  font-size: 0.9em;
  background: var(--code-bg);
  padding: 0.2em 0.4em;
  border-radius: 3px;
}

pre code {
  background: none;
  padding: 0;
}

/* Lists */
ul, ol {
  margin-left: 1.5rem;
  margin-bottom: 1rem;
}

li {
  margin-bottom: 0.5rem;
}

/* Steps */
.steps {
  counter-reset: step;
}

.step {
  background: var(--surface);
  border-left: 4px solid var(--accent);
  padding: 1rem 1rem 1rem 3.5rem;
  margin-bottom: 1rem;
  border-radius: 4px;
  position: relative;
}

.step::before {
  counter-increment: step;
  content: counter(step);
  position: absolute;
  left: 1rem;
  width: 1.8rem;
  height: 1.8rem;
  background: var(--accent);
  color: white;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 0.9rem;
}

/* Table */
table {
  width: 100%;
  border-collapse: collapse;
  margin: 2rem 0;
}

th, td {
  text-align: left;
  padding: 0.75rem;
  border-bottom: 1px solid var(--border);
}

th {
  font-weight: 600;
  background: var(--surface);
}

/* Links */
a {
  color: var(--accent);
  text-decoration: none;
}

a:hover {
  text-decoration: underline;
}

/* Footer */
footer {
  margin-top: 4rem;
  padding: 2rem 0;
  border-top: 1px solid var(--border);
  text-align: center;
  color: var(--text-secondary);
}

.footer-links {
  display: flex;
  justify-content: center;
  gap: 2rem;
  margin-bottom: 1rem;
}

/* Responsive */
@media (max-width: 768px) {
  .container {
    padding: 0 1rem;
  }

  h1 {
    font-size: 2rem;
  }

  .grid {
    grid-template-columns: 1fr;
  }
}
</style>

<div class="container">

<header>
  <div class="logo">⚡ Speckit Prompt Generator</div>
  <div class="badges">
    <a href="https://github.com/salmanpatnee/speckit-prompt-generator"><img src="https://img.shields.io/github/stars/salmanpatnee/speckit-prompt-generator?style=social" alt="GitHub stars"></a>
    <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License">
    <img src="https://img.shields.io/badge/python-3.7+-blue.svg" alt="Python 3.7+">
  </div>
</header>

<section class="hero">
  <h1>Transform Plans into Perfect Prompts</h1>
  <p class="subtitle">A Claude Code skill that automatically generates high-quality, paragraph-style Speckit prompts from your multi-phase development plans.</p>

  <div class="highlight-box">
    <strong>Turn 1 plan → Get 2N prompts</strong> (spec + plan for each phase)
  </div>

  <div class="stats">
    <div class="stat">
      <div class="stat-value">2×</div>
      <div class="stat-label">Prompts per phase</div>
    </div>
    <div class="stat">
      <div class="stat-value">&lt;1s</div>
      <div class="stat-label">Generation time</div>
    </div>
    <div class="stat">
      <div class="stat-value">100%</div>
      <div class="stat-label">Automated</div>
    </div>
  </div>
</section>

<section>
  <h2>What Problem Does This Solve?</h2>
  <p>When using Spec-Driven Development, writing individual <strong>spec AND plan prompts</strong> for each phase is time-consuming and error-prone. For 8 phases, that's <strong>16 prompts to write manually!</strong></p>
  <p><strong>The Solution:</strong> Provide your plan document → Get back all prompts at once (2 per phase) → Run them through Speckit sequentially.</p>
</section>

<section>
  <h2>Key Features</h2>
  <div class="grid">
    <div class="card">
      <h3>🤖 Fully Automated</h3>
      <p>No user interaction needed; just provide your plan and get production-ready prompts instantly.</p>
    </div>
    <div class="card">
      <h3>💎 High Quality</h3>
      <p>Prompts follow proven patterns and quality standards, ensuring consistency across all phases.</p>
    </div>
    <div class="card">
      <h3>📝 Paragraph Form</h3>
      <p>Optimized for Speckit AI processing with flowing narrative instead of bullet lists.</p>
    </div>
    <div class="card">
      <h3>📦 Consolidated Output</h3>
      <p>Single Markdown file with all prompts, clearly labeled and ready to use.</p>
    </div>
    <div class="card">
      <h3>🎯 Intent-Focused</h3>
      <p>Emphasizes outcomes and constraints, not implementation details.</p>
    </div>
    <div class="card">
      <h3>🔄 Reusable</h3>
      <p>Works with any multi-phase project across different frameworks.</p>
    </div>
  </div>
</section>

<section id="installation">
  <h2>Installation</h2>
  <div class="steps">
    <div class="step">
      <strong>Locate your skills directory</strong>
      <ul>
        <li>macOS/Linux: <code>~/.claude/skills/</code></li>
        <li>Windows: <code>C:\Users\&lt;YourUsername&gt;\.claude\skills\</code></li>
      </ul>
    </div>
    <div class="step">
      <strong>Place the skill file</strong>
      <pre><code>cp speckit-prompt-generator.skill ~/.claude/skills/</code></pre>
    </div>
    <div class="step">
      <strong>Restart Claude Code or reload skills</strong>
    </div>
    <div class="step">
      <strong>Done! Skill is ready to use</strong>
    </div>
  </div>
</section>

<section id="getting-started">
  <h2>Quick Start</h2>

  <h3>Step 1: Create a Plan Document</h3>
  <pre><code>## Phase 1 – Requirements Gathering

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
- Success metrics defined</code></pre>

  <h3>Step 2: Generate Prompts</h3>
  <pre><code>Generate Speckit prompts from: /path/to/my-feature-plan.md</code></pre>

  <h3>Step 3: Review Output</h3>
  <p>The skill creates <code>speckit-prompts.md</code> in the same directory with all prompts ready to use.</p>

  <h3>Step 4: Use with Speckit</h3>
  <pre><code># For each phase, run both prompts:
/sp.specify
# Paste Phase 1 SPEC prompt

/sp.plan
# Paste Phase 1 PLAN prompt</code></pre>
</section>

<section id="examples">
  <h2>Example Output</h2>

  <h3>Spec Prompt (WHAT to build)</h3>
  <div class="card">
    <p><em>"Specify the system architecture requirements for Phase 2: System Architecture. The architecture must support high availability with 99.9% uptime, handle 10,000 concurrent users, maintain data consistency across distributed services..."</em></p>
  </div>

  <h3>Plan Prompt (HOW to build it)</h3>
  <div class="card">
    <p><em>"Plan the implementation of the system architecture for Phase 2: System Architecture. Design the overall system topology separating concerns with clear service boundaries and communication protocols..."</em></p>
  </div>

  <p><strong>Key Differences:</strong></p>
  <ul>
    <li><strong>Spec Prompt:</strong> Focuses on requirements, constraints, success criteria</li>
    <li><strong>Plan Prompt:</strong> Focuses on implementation steps, technical approach</li>
    <li>Both are paragraph form (not bullets)</li>
    <li>Both ready to use with respective Speckit commands</li>
  </ul>
</section>

<section id="patterns">
  <h2>Quality Standards</h2>
  <table>
    <thead>
      <tr>
        <th>Standard</th>
        <th>Implementation</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Paragraph form</strong></td>
        <td>Flowing prose, no bullet points</td>
      </tr>
      <tr>
        <td><strong>Intent-first</strong></td>
        <td>Emphasizes "why" and "what outcomes"</td>
      </tr>
      <tr>
        <td><strong>Concise</strong></td>
        <td>60–150 words depending on complexity</td>
      </tr>
      <tr>
        <td><strong>Logically chained</strong></td>
        <td>Requirements build on each other</td>
      </tr>
      <tr>
        <td><strong>Outcome-emphasized</strong></td>
        <td>Repeats key success criteria</td>
      </tr>
      <tr>
        <td><strong>No tech details</strong></td>
        <td>Avoids specific framework names</td>
      </tr>
    </tbody>
  </table>
</section>

<section id="workflows">
  <h2>Common Use Cases</h2>
  <div class="grid">
    <div class="card">
      <h3>Multi-Phase Feature</h3>
      <p>5–7 phase plan for complex features like payment processing. Generate all prompts at once.</p>
    </div>
    <div class="card">
      <h3>Multi-Service System</h3>
      <p>Multiple microservices or components, each with phases.</p>
    </div>
    <div class="card">
      <h3>Framework Setup</h3>
      <p>Learning or setting up new frameworks (Laravel, React, etc.).</p>
    </div>
    <div class="card">
      <h3>Iterative Refinement</h3>
      <p>Refine your plan as you learn more and regenerate prompts.</p>
    </div>
  </div>
</section>

<section id="documentation">
  <h2>Documentation</h2>
  <div class="grid">
    <div class="card">
      <h3>📖 Usage Guide</h3>
      <p>Learn how to write effective plan documents</p>
      <a href="#usage-guide">Read →</a>
    </div>
    <div class="card">
      <h3>📚 Quality Patterns</h3>
      <p>Design patterns and quality checklists</p>
      <a href="https://github.com/salmanpatnee/speckit-prompt-generator/blob/main/references/prompt-quality-standards.md">Read →</a>
    </div>
    <div class="card">
      <h3>🛠️ Workflows</h3>
      <p>5 detailed real-world workflow examples</p>
      <a href="https://github.com/salmanpatnee/speckit-prompt-generator/blob/main/references/workflows.md">Read →</a>
    </div>
    <div class="card">
      <h3>⚙️ API Reference</h3>
      <p>Script documentation and technical details</p>
      <a href="#api-reference">Read →</a>
    </div>
  </div>
</section>

<section id="usage-guide">
  <h2>Writing Good Plan Documents</h2>

  <h3>✅ Required Structure</h3>
  <pre><code>## Phase X – Phase Title

**Objective**
Why this phase exists; what it accomplishes.

**High-Level Scope**
- Item 1
- Item 2
- Item 3

**Outcome**
- Expected result 1
- Expected result 2</code></pre>

  <h3>✅ Phase Numbering</h3>
  <pre><code>## Phase 1 – Requirements
## Phase 2 – Architecture
## Phase 3 – Implementation</code></pre>

  <h3>❌ What Doesn't Work</h3>
  <pre><code># Requirements (missing phase number)
PHASE 1 (all caps, no heading syntax)
Phase 1: (colon instead of – dash)</code></pre>
</section>

<section id="faq">
  <h2>FAQ</h2>

  <div class="card">
    <h3>❓ "No phases found in plan document"</h3>
    <p><strong>Check:</strong> Headings are <code>## Phase X – Title</code> format, not <code># Phase</code> or plain text.</p>
  </div>

  <div class="card">
    <h3>❓ "Prompts are too short"</h3>
    <p><strong>Fix:</strong> Add more detail to your <strong>Objective</strong>, <strong>Scope</strong>, and <strong>Outcome</strong> sections.</p>
  </div>

  <div class="card">
    <h3>❓ "Can I run the script directly?"</h3>
    <p>Yes! Use: <code>python scripts/generate_prompts.py /path/to/plan.md</code></p>
  </div>
</section>

<section id="api-reference">
  <h2>API Reference</h2>

  <h3>Input Requirements</h3>
  <ul>
    <li><strong>Format:</strong> Markdown (<code>.md</code>)</li>
    <li><strong>Structure:</strong> Clear <code>## Phase X – Title</code> headings</li>
    <li><strong>Content:</strong> Objective, Scope, Outcome sections for each phase</li>
    <li><strong>Size:</strong> Works with 1–20+ phases</li>
  </ul>

  <h3>Output Guarantee</h3>
  <ul>
    <li><strong>Format:</strong> Single consolidated Markdown file</li>
    <li><strong>Location:</strong> Same directory as input plan</li>
    <li><strong>Naming:</strong> <code>speckit-prompts.md</code> (or custom path)</li>
  </ul>

  <h3>Direct Script Usage</h3>
  <pre><code>python scripts/generate_prompts.py /path/to/plan.md [output_path]</code></pre>
  <p><strong>Use cases:</strong> CI/CD integration, batch processing, custom output handling</p>
</section>

<section id="contributing">
  <h2>Contributing</h2>
  <div class="grid">
    <div class="card">
      <h3>Share Use Cases</h3>
      <p>Share examples of successful prompt generation and real-world applications.</p>
    </div>
    <div class="card">
      <h3>Suggest Features</h3>
      <p>Propose new features or patterns that would enhance the skill.</p>
    </div>
    <div class="card">
      <h3>Report Issues</h3>
      <p>Describe the issue, expected behavior, and steps to reproduce.</p>
    </div>
    <div class="card">
      <h3>Improve Docs</h3>
      <p>Help enhance guides, examples, and quality standards.</p>
    </div>
  </div>
</section>

<footer>
  <div class="footer-links">
    <a href="https://github.com/salmanpatnee/speckit-prompt-generator">GitHub</a>
    <a href="https://github.com/salmanpatnee/speckit-prompt-generator/blob/main/SKILL.md">Documentation</a>
    <a href="https://github.com/salmanpatnee/speckit-prompt-generator/issues">Issues</a>
    <a href="https://github.com/salmanpatnee/speckit-prompt-generator/blob/main/LICENSE">License</a>
  </div>
  <p>Speckit Prompt Generator v1.0.0 · MIT License · Python 3.7+</p>
</footer>

</div>
