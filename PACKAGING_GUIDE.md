# Packaging & Distribution Guide

This guide explains how to package the `speckit-prompt-generator` skill for distribution and use in other projects.

## Prerequisites

- Access to the skill-creator tools
- Python 3.7+ for packaging scripts
- The complete skill directory with all files

## Skill Contents Checklist

Before packaging, verify all files are present and correct:

```
speckit-prompt-generator/
├── SKILL.md                          ✅ Required – Skill definition
├── scripts/
│   └── generate_prompts.py          ✅ Executable prompt generation
├── references/
│   ├── prompt-quality-standards.md  ✅ Quality guidelines
│   └── workflows.md                 ✅ Usage examples
└── assets/
    └── example-output.md            ✅ Sample output demonstration
```

**File sizes (approximate):**
- SKILL.md: ~5 KB
- generate_prompts.py: ~8 KB
- prompt-quality-standards.md: ~12 KB
- workflows.md: ~15 KB
- example-output.md: ~6 KB

**Total skill size:** ~46 KB (very lightweight)

## Packaging Steps

### Step 1: Validate the Skill

Before packaging, ensure the skill meets all quality standards:

```bash
# Check SKILL.md frontmatter
cat "C:\Users\salmanabdul.ghani\.claude\skills\speckit-prompt-generator\SKILL.md" | head -5
```

Expected output:
```
---
name: speckit-prompt-generator
description: Generate high-quality, paragraph-style specification...
---
```

### Step 2: Test the Skill

Test the prompt generation script manually:

```bash
# Create a test plan file
cat > test-plan.md << 'EOF'
## Phase 1 – Requirements
**Objective**
Gather requirements.

**High-Level Scope**
- User stories
- Acceptance criteria

**Outcome**
- Requirements approved
EOF

# Run the script
python generate_prompts.py test-plan.md

# Check output
cat speckit-prompts.md
```

Expected: `speckit-prompts.md` created with prompt for Phase 1

### Step 3: Package the Skill

Use the skill-creator's packaging script:

```bash
cd "C:\Users\salmanabdul.ghani\.claude\skills\skill-creator"

python3 scripts/package_skill.py \
  "C:\Users\salmanabdul.ghani\.claude\skills\speckit-prompt-generator" \
  --output "./dist"
```

Expected output:
```
✓ Validating skill...
✓ YAML frontmatter valid
✓ Description complete and helpful
✓ All referenced resources present
✓ Packaging skill...
✓ Created: ./dist/speckit-prompt-generator.skill
```

### Step 4: Verify the Package

The `.skill` file is a ZIP archive. Verify contents:

```bash
# List contents of skill package
unzip -l "./dist/speckit-prompt-generator.skill"
```

Expected structure:
```
speckit-prompt-generator/
├── SKILL.md
├── scripts/generate_prompts.py
├── references/prompt-quality-standards.md
├── references/workflows.md
└── assets/example-output.md
```

## Distribution Methods

### Option 1: GitHub Release (Recommended)

1. **Create a GitHub repository** for your skills:
   ```
   your-org/claude-skills
   ```

2. **Upload the skill package:**
   ```
   releases/
   └── speckit-prompt-generator/
       ├── speckit-prompt-generator.skill
       ├── README.md
       └── CHANGELOG.md
   ```

3. **Document the release:**
   ```markdown
   # speckit-prompt-generator v1.0.0

   Generate Speckit-compatible prompts from structured plan documents.

   ## Installation

   Download: `speckit-prompt-generator.skill`

   ## Usage

   ```
   Generate Speckit prompts from: /path/to/plan.md
   ```

   See SKILL.md for complete documentation.
   ```

### Option 2: Direct File Sharing

1. **Package the skill** (creates `.skill` file)
2. **Share the file** via:
   - Email attachment
   - Cloud storage (Dropbox, Google Drive, etc.)
   - Direct download link

3. **Installation instructions for recipients:**
   ```
   1. Download speckit-prompt-generator.skill
   2. Place in ~/.claude/skills/ directory
   3. Skill automatically available in next session
   ```

### Option 3: Private Skill Registry

If you maintain a private skill registry:

1. **Push to registry:**
   ```bash
   skill-registry push speckit-prompt-generator.skill
   ```

2. **Users install from registry:**
   ```bash
   skill-registry install speckit-prompt-generator
   ```

## Version Management

### Semantic Versioning

Use semantic versioning for skill releases:

- **v1.0.0**: Initial release with core functionality
- **v1.1.0**: Added features (e.g., custom output directory option)
- **v1.0.1**: Bug fix (e.g., improved phase detection)
- **v2.0.0**: Breaking changes (e.g., different input format)

### Version in Skill

Update SKILL.md description if major features change:

```yaml
---
name: speckit-prompt-generator
description: |
  v1.0.0: Generate high-quality, paragraph-style specification
  and planning prompts compatible with Speckit...
---
```

## Changelog Template

Create `CHANGELOG.md` for your release:

```markdown
# Changelog – speckit-prompt-generator

## [1.0.0] – 2025-12-31

### Added
- Initial release
- Phase detection from Markdown documents
- Prompt generation for spec and plan phases
- Consolidated output to single Markdown file
- Python script for standalone execution
- Quality standards reference guide
- Real-world workflow examples
- Example output demonstrations

### Documentation
- SKILL.md with quick start and usage guide
- prompt-quality-standards.md with design patterns
- workflows.md with 5 complete scenarios
- example-output.md showing expected results

## Future Versions

### [1.1.0] – Planned
- [ ] Multi-document input support
- [ ] Custom prompt templates
- [ ] Batch processing multiple plans
- [ ] Direct Speckit command invocation

### [2.0.0] – Planned
- [ ] Support for YAML and JSON input formats
- [ ] CLI tool with configuration file support
- [ ] Validation against prompt quality standards
```

## User Installation Instructions

For users receiving the skill:

### Installation

1. **Locate skill directory:**
   ```bash
   # macOS/Linux
   ~/.claude/skills/

   # Windows
   C:\Users\<YourUsername>\.claude\skills\
   ```

2. **Place the skill file:**
   ```bash
   cp speckit-prompt-generator.skill ~/.claude/skills/
   ```

3. **Restart Claude Code** or reload the skill browser

4. **Verify installation:**
   The skill is ready to use when you see it listed in the skills browser

### First Use

1. **Create a plan document:**
   ```markdown
   ## Phase 1 – Requirements
   **Objective**
   Define all requirements.

   **High-Level Scope**
   - User stories
   - Acceptance criteria

   **Outcome**
   - Requirements approved
   ```

2. **Generate prompts:**
   ```
   Generate Speckit prompts from: /path/to/plan.md
   ```

3. **Review output:**
   Check `speckit-prompts.md` in the same directory as your plan

4. **Use prompts with Speckit:**
   ```
   /sp.specify
   [Paste Phase 1 prompt]
   ```

## Troubleshooting

### Issue: Skill not recognized after installation

**Solution:** Restart Claude Code or reload the skill list

### Issue: "No phases found" error

**Solution:** Ensure plan document uses proper Markdown heading syntax:
```markdown
## Phase 1 – Title
## Phase 2 – Title
```

Not:
```markdown
# Phase 1 – Title (top-level)
PHASE 1 (not a heading)
```

### Issue: Output file not created

**Solution:** Check write permissions in the output directory
```bash
# Test write permission
touch /path/to/directory/test.txt
```

### Issue: Script fails to run

**Solution:** Ensure Python 3.7+ is installed and in PATH
```bash
python --version  # Should show Python 3.7+
```

## Support & Maintenance

### Getting Help

If users encounter issues:

1. **Check references:**
   - `workflows.md` – Common use cases and solutions
   - `prompt-quality-standards.md` – Quality expectations

2. **Review example output:**
   - `example-output.md` – Shows expected results

3. **Test with simple plan:**
   - Use minimal 2–3 phase plan to isolate issues

### Contributing Improvements

To improve the skill:

1. **Report issues:**
   - Describe problem and expected behavior
   - Share example input that fails

2. **Suggest enhancements:**
   - New features or patterns
   - Better examples or documentation

3. **Submit updates:**
   - Fork the skill repository
   - Make improvements
   - Create pull request

## Summary

The `speckit-prompt-generator` skill is ready for distribution:

✅ **Package:** Creates `.skill` file for distribution
✅ **Install:** Users place file in `~/.claude/skills/`
✅ **Use:** Skill automatically available next session
✅ **Document:** Complete SKILL.md included
✅ **Support:** References and examples included
✅ **Maintain:** Changelog and version management ready

**Ready to share!**
