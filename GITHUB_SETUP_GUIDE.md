# GitHub Setup & Publication Guide

Step-by-step instructions for publishing speckit-prompt-generator to GitHub.

---

## Step 1: Create GitHub Repository

### On GitHub.com

1. Go to [github.com/new](https://github.com/new)
2. Fill in repository details:
   ```
   Repository name: speckit-prompt-generator
   Description: Transform structured plan documents into
                high-quality Speckit-compatible prompts
   Public (checked)
   Initialize with:
   - ☐ README (we'll add our own)
   - ☐ .gitignore
   - ☐ License
   ```

3. Click "Create repository"

### Add License

After creating, go to "Add license" and select **MIT License**

---

## Step 2: Prepare Local Repository

### Initialize Git (First Time)

```bash
cd ~/path/to/speckit-prompt-generator

# Initialize git repository
git init

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: Speckit Prompt Generator v1.0.0

- Core skill with SKILL.md definition
- Python script for prompt generation
- Quality standards reference guide
- Real-world workflow examples
- Comprehensive documentation
- Ready for publication"

# Add remote origin
git remote add origin https://github.com/YOUR_USERNAME/speckit-prompt-generator.git

# Push to GitHub
git branch -M main
git push -u origin main
```

---

## Step 3: Create Repository Files

### Create .gitignore

```bash
cat > .gitignore << 'EOF'
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual environments
venv/
env/
ENV/

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Testing
.pytest_cache/
htmlcov/

# Output
speckit-prompts.md
*.skill
EOF

git add .gitignore
git commit -m "Add .gitignore"
git push
```

### Create LICENSE (MIT)

```bash
cat > LICENSE << 'EOF'
MIT License

Copyright (c) 2025 [Your Name]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
EOF

git add LICENSE
git commit -m "Add MIT License"
git push
```

### Create CONTRIBUTING.md

```bash
cat > CONTRIBUTING.md << 'EOF'
# Contributing to Speckit Prompt Generator

We welcome contributions! Here's how you can help.

## Reporting Bugs

1. Check existing issues first
2. Create a new issue with:
   - Clear title
   - Detailed description
   - Steps to reproduce
   - Expected vs actual behavior
   - Your environment (OS, Python version, etc.)

## Suggesting Features

1. Check discussions/issues for similar ideas
2. Create a discussion or issue with:
   - Clear title
   - Use case explanation
   - Why it would be valuable
   - Potential implementation ideas (optional)

## Code Contributions

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Make your changes
4. Test thoroughly
5. Commit with clear messages
6. Push to your fork
7. Open a pull request with:
   - Clear description
   - Reference to related issues
   - Testing information

## Documentation Contributions

1. Fork the repository
2. Edit or create documentation
3. Submit a pull request

## Code of Conduct

Be respectful and inclusive. We're building a welcoming community.

## Questions?

Ask in Discussions or create an issue. We're here to help!

Thanks for contributing! 🙌
EOF

git add CONTRIBUTING.md
git commit -m "Add contributing guidelines"
git push
```

### Create CHANGELOG.md

```bash
cat > CHANGELOG.md << 'EOF'
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] – 2025-12-31

### Added
- Initial release of Speckit Prompt Generator
- Automated prompt generation from structured plan documents
- Phase detection and analysis
- Objective, scope, and outcome extraction
- Paragraph-style prompt generation
- Consolidated Markdown output
- Python script for standalone execution
- Quality standards reference guide (215+ lines)
- Real-world workflow examples (5 scenarios)
- Complete documentation
  - SKILL.md with quick start
  - README.md with overview
  - Installation guide
  - Usage guide
  - Example output
- GitHub repository setup
- Marketing strategy and templates
- MIT License

### Features
- Support for 1-20+ phase projects
- Automatic prompt type determination (spec vs. plan)
- Logical requirement chaining
- Success criteria emphasis
- Error handling with helpful messages

### Documentation
- Quick start guide (5 minutes to first prompts)
- Quality standards with design patterns
- Workflow examples for common scenarios
- Troubleshooting guide
- Contributing guidelines

### Community
- Open source (MIT License)
- GitHub-hosted
- Community contributions welcome
- Active support and issue resolution

---

## Versioning

- **1.x.x** - Core functionality and improvements
- **2.0.0** - Major new features (multi-format support, UI, integrations)

For detailed roadmap, see [GitHub Discussions](https://github.com/yourname/speckit-prompt-generator/discussions)
EOF

git add CHANGELOG.md
git commit -m "Add changelog"
git push
```

---

## Step 4: Set Up GitHub Pages

### Create docs Directory Structure

```bash
mkdir -p docs

# Move documentation to docs
cp IMPLEMENTATION_SUMMARY.md docs/
cp README.md docs/index.md
```

### Create docs/_config.yml (Jekyll)

```bash
cat > docs/_config.yml << 'EOF'
theme: jekyll-theme-minimal
title: Speckit Prompt Generator
description: Transform plans into prompts automatically
show_downloads: true
github:
  is_project_page: true
  repository_url: https://github.com/YOUR_USERNAME/speckit-prompt-generator

plugins:
  - jekyll-gist
  - jekyll-github-metadata
EOF

git add docs/
git commit -m "Add GitHub Pages documentation"
git push
```

### Enable GitHub Pages

1. Go to repository Settings
2. Scroll to "GitHub Pages"
3. Select "Deploy from a branch"
4. Branch: "main"
5. Folder: "/docs"
6. Click "Save"

Site will be available at: `https://YOUR_USERNAME.github.io/speckit-prompt-generator/`

---

## Step 5: Create Initial Release

### Tag v1.0.0

```bash
git tag -a v1.0.0 -m "Release v1.0.0: Initial release"
git push origin v1.0.0
```

### Create Release on GitHub

1. Go to repository "Releases"
2. Click "Create a new release"
3. Fill in:
   ```
   Tag: v1.0.0
   Title: v1.0.0 – Initial Release
   Description: [Paste release notes below]
   ```

### Release Notes

```
🎉 First Release – Speckit Prompt Generator v1.0.0

## What's New

This release introduces a complete, production-ready tool for automating
Speckit prompt generation from structured plan documents.

## Features

✅ Automated prompt generation from plan documents
✅ High-quality paragraph-style prompts
✅ Support for 1-20+ phase projects
✅ Consolidated output to single file
✅ Python script for standalone execution
✅ Quality standards reference guide
✅ 5 real-world workflow examples
✅ Complete documentation
✅ Open source (MIT License)

## Documentation

- SKILL.md – User guide and quick start
- README.md – Overview and reference
- Getting Started guide – 5-minute walkthrough
- Quality standards – Proven patterns
- Workflow examples – Real-world scenarios

## Installation

```bash
cp speckit-prompt-generator.skill ~/.claude/skills/
```

Or clone: `https://github.com/YOUR_USERNAME/speckit-prompt-generator`

## Getting Started

```bash
python scripts/generate_prompts.py your-plan.md
```

See [Getting Started](./docs/getting-started.md) for details.

## Community

Thanks to everyone who provided feedback during development!

- 📖 Full documentation: See docs/
- 🐛 Report bugs: GitHub Issues
- 💡 Suggest features: GitHub Discussions
- 🤝 Contribute: See CONTRIBUTING.md

## Next Steps

- Feedback welcome in Issues and Discussions
- Community contributions encouraged
- Regular updates planned
- Roadmap: See Discussions

---

Thank you for checking out Speckit Prompt Generator! 🚀
```

---

## Step 6: Configure GitHub Settings

### Repository Settings

1. **General**
   - Description: Keep it clear and concise
   - Website: (optional) link to docs

2. **Topics**
   Add relevant tags:
   ```
   developer-tools
   speckit
   spec-driven-development
   claude-code
   prompt-engineering
   python
   open-source
   ```

3. **Discussions**
   - Enable discussions for community Q&A
   - Set up discussion categories:
     - Announcements
     - Ideas
     - Q&A
     - Showcase (community projects)

4. **Issues**
   - Enable with templates for:
     - Bug Report
     - Feature Request

5. **Security**
   - Enable vulnerability scanning
   - Enable secret scanning

### Create Issue Templates

```bash
mkdir -p .github/ISSUE_TEMPLATE

# Bug report template
cat > .github/ISSUE_TEMPLATE/bug_report.md << 'EOF'
---
name: Bug Report
about: Report a problem
title: "[BUG] "
labels: bug
---

## Description
Clear description of the bug.

## Steps to Reproduce
1. First step
2. Second step

## Expected Behavior
What should happen.

## Actual Behavior
What actually happens.

## Environment
- OS: [e.g. macOS, Windows]
- Python: [e.g. 3.9]
- Version: [e.g. 1.0.0]

## Additional Context
Any other information.
EOF

# Feature request template
cat > .github/ISSUE_TEMPLATE/feature_request.md << 'EOF'
---
name: Feature Request
about: Suggest an improvement
title: "[FEATURE] "
labels: enhancement
---

## Description
Clear description of the feature.

## Use Case
Why would this be valuable?

## Implementation Ideas
(Optional) How might this work?

## Additional Context
Any other information.
EOF

git add .github/
git commit -m "Add issue templates"
git push
```

---

## Step 7: Add Badges to README

```markdown
# Speckit Prompt Generator

[![GitHub stars](https://img.shields.io/github/stars/YOUR_USERNAME/speckit-prompt-generator?style=social)](https://github.com/YOUR_USERNAME/speckit-prompt-generator)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![GitHub Issues](https://img.shields.io/github/issues/YOUR_USERNAME/speckit-prompt-generator)](https://github.com/YOUR_USERNAME/speckit-prompt-generator/issues)
[![GitHub Discussions](https://img.shields.io/discussions/YOUR_USERNAME/speckit-prompt-generator)](https://github.com/YOUR_USERNAME/speckit-prompt-generator/discussions)

[Rest of README...]
```

---

## Step 8: Create social-media-optimized assets

### Create assets/ directory

```bash
mkdir assets

# Add hero image (1200x630px recommended)
# Add feature icons
# Add example outputs
```

---

## Step 9: Link all platforms

### Update profile links

- GitHub bio: Link to docs
- README: Link to GitHub
- Docs: Link to GitHub Issues/Discussions

### Create status badge

Add to docs/index.md:
```markdown
[![GitHub Repo](https://img.shields.io/static/v1?label=Repository&message=GitHub&color=181717&logo=github)](https://github.com/YOUR_USERNAME/speckit-prompt-generator)
[![Documentation](https://img.shields.io/static/v1?label=Docs&message=Read&color=0070f0)](https://YOUR_USERNAME.github.io/speckit-prompt-generator/)
[![Stars](https://img.shields.io/github/stars/YOUR_USERNAME/speckit-prompt-generator?style=social)](https://github.com/YOUR_USERNAME/speckit-prompt-generator)
```

---

## Step 10: Launch Checklist

Before announcing:

- ✅ Repository created and public
- ✅ All files pushed to GitHub
- ✅ README is comprehensive
- ✅ CONTRIBUTING.md is clear
- ✅ LICENSE file (MIT) added
- ✅ CHANGELOG.md created
- ✅ GitHub Pages enabled
- ✅ v1.0.0 tag and release created
- ✅ Discussions/Issues enabled
- ✅ Topics added for discoverability
- ✅ Status badges in README
- ✅ All links verified

---

## Useful GitHub Features

### GitHub Actions (Optional – Future)

Automate testing and releases:
```yaml
# .github/workflows/test.yml
name: Test

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Run tests
        run: python tests/validate_skill.py
```

### GitHub Discussions

Enable community conversations:
```
Categories:
- 📢 Announcements (updates)
- 💡 Ideas (feature requests)
- ❓ Q&A (help)
- 🎓 Show and Tell (user projects)
```

### GitHub Projects

Track development:
```
Board: Development
Columns:
- 📋 Backlog
- 🚀 In Progress
- ✅ Done
- 📖 Documentation
```

---

## Post-Launch: Monitor & Engage

### Daily
- Respond to issues/discussions within 24 hours
- Check for bug reports

### Weekly
- Review community feedback
- Plan improvements
- Publish updates

### Monthly
- Release improvements if applicable
- Publish blog post or update
- Engage with community

---

## Success Metrics to Track

```
Daily:
- GitHub stars growth
- Clone count
- Discussion activity

Weekly:
- New issues
- Pull requests
- Community mentions

Monthly:
- Total stars
- Active contributors
- Downloads/usage
```

---

## Next: Market on LinkedIn

Once GitHub is live and tested, follow up with:
1. Launch announcement post
2. Share repository link
3. Engage with comments
4. Continue publishing content

[See PUBLICATION_STRATEGY.md for LinkedIn details]

---

**You're ready to launch! 🚀**
