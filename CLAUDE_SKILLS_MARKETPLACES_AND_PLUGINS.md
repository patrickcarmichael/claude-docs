# Claude Skills Marketplaces & Plugins: The Definitive Guide

**Last Updated:** 2025-11-08
**Total Repositories Analyzed:** 20+
**Total Plugins/Skills Tracked:** 500+

---

## Table of Contents

1. [Overview](#overview)
2. [Top Marketplaces by Popularity](#top-marketplaces-by-popularity)
3. [Official Anthropic Resources](#official-anthropic-resources)
4. [Community Marketplaces](#community-marketplaces)
5. [Specialized Marketplaces](#specialized-marketplaces)
6. [Plugin Collections](#plugin-collections)
7. [Installation Guide](#installation-guide)
8. [Comparison Matrix](#comparison-matrix)
9. [Web-Based Marketplaces](#web-based-marketplaces)
10. [Quick Reference](#quick-reference)

---

## Overview

### What Are Claude Skills Marketplaces?

**Marketplaces** are centralized catalogs that make it easy to discover, install, and manage Claude Code plugins and skills. They provide:

- **Version management** for plugins
- **Team distribution** capabilities
- **Centralized discovery** across multiple sources
- **Automated updates** and syncing

### Types of Resources

| Type | Description | Example |
|------|-------------|---------|
| **Official Skills** | Anthropic-maintained skills | anthropics/skills |
| **Marketplaces** | Curated plugin collections | jeremylongshore/claude-code-plugins-plus |
| **Awesome Lists** | Community-curated directories | travisvn/awesome-claude-skills |
| **Plugin Frameworks** | Complete workflow systems | obra/superpowers |
| **Specialized Collections** | Domain-specific skills | netresearch (TYPO3) |

---

## Top Marketplaces by Popularity

Ranked by GitHub stars (as of November 2025):

### 🥇 #1: hesreallyhim/awesome-claude-code
**⭐ 16,600 stars** | 937 forks

```bash
/plugin marketplace add hesreallyhim/awesome-claude-code
```

**Description:** The most comprehensive curated collection of slash-commands, CLAUDE.md files, CLI tools, and workflows for Claude Code.

**Features:**
- ✅ Agent Skills for specialized tasks
- ✅ Workflows & Knowledge Guides
- ✅ Comprehensive Tooling suite (CLI tools, IDE integrations)
- ✅ Status Lines and Hooks library
- ✅ Extensive Slash-Commands organized by category
- ✅ CLAUDE.md templates (language & domain-specific)
- ✅ Alternative client options

**Categories:**
- Version control commands
- Code analysis tools
- Context-loading techniques
- CI/deployment workflows
- Project management systems

**Notable Content:**
- Infrastructure Showcases
- Conversation browsers (Claudex)
- Agent command centers (Omnara)
- 272+ commits with active community

**Best For:** Developers looking for battle-tested workflows and comprehensive tooling

**Repository:** https://github.com/hesreallyhim/awesome-claude-code

---

### 🥈 #2: anthropics/skills
**⭐ 15,900 stars** | 1,400 forks

```bash
/plugin marketplace add anthropics/skills
```

**Description:** Official public repository for Skills from Anthropic.

**Features:**
- ✅ 13+ official skills
- ✅ Document manipulation (Word, PDF, PowerPoint, Excel)
- ✅ Creative & Design tools
- ✅ Development frameworks
- ✅ Enterprise capabilities
- ✅ Available across Claude Code, Claude.ai, and API

**Official Skills:**

**Creative & Design:**
- `algorithmic-art` - Generative art with p5.js, seeded randomness, particle systems
- `canvas-design` - Visual art in PNG/PDF formats
- `slack-gif-creator` - Animated GIFs optimized for Slack

**Development & Technical:**
- `artifacts-builder` - Complex HTML artifacts (React, Tailwind, shadcn/ui)
- `mcp-builder` - Guide for creating MCP servers
- `webapp-testing` - Web app testing with Playwright

**Enterprise & Communication:**
- `brand-guidelines` - Anthropic brand colors and typography
- `internal-comms` - Status reports, newsletters, FAQs
- `theme-factory` - 10 professional themes + custom generation

**Document Skills:**
- `docx` - Word documents with tracked changes
- `pdf` - PDF manipulation (extraction, forms, merging)
- `pptx` - PowerPoint presentations with automation
- `xlsx` - Excel spreadsheets with formulas & analysis

**Meta Skills:**
- `skill-creator` - Guidelines for extending Claude
- `template-skill` - Starter template

**Languages:** Python (87.9%), JavaScript (7.1%), HTML (3.2%), Shell (1.8%)

**Best For:** Production-ready, officially maintained skills with comprehensive documentation

**Repository:** https://github.com/anthropics/skills

---

### 🥉 #3: obra/superpowers
**⭐ 6,200 stars** | 457 forks

```bash
/plugin marketplace add obra/superpowers-marketplace
/plugin install superpowers@superpowers-marketplace
```

**Description:** Comprehensive skills library with 20+ battle-tested skills for systematic development workflows.

**Features:**
- ✅ 20+ proven skills and techniques
- ✅ Automatic skill discovery
- ✅ Mandatory systematic approaches
- ✅ Test-driven development enforcement
- ✅ Three primary slash commands

**Skill Categories:**

**1. Testing Skills** (`skills/testing/`)
- `test-driven-development` - RED-GREEN-REFACTOR cycle methodology
- `condition-based-waiting` - Async testing patterns
- `testing-anti-patterns` - Common testing pitfalls

**2. Debugging Skills** (`skills/debugging/`)
- `systematic-debugging` - Four-phase root cause analysis
- `root-cause-tracing` - Underlying problem identification
- `verification-before-completion` - Pre-completion validation
- `defense-in-depth` - Multiple validation layers

**3. Collaboration Skills** (`skills/collaboration/`)
- `brainstorming` - Socratic-style design refinement
- `writing-plans` - Detailed implementation planning
- `executing-plans` - Batch execution with checkpoints
- `dispatching-parallel-agents` - Concurrent subagent workflows
- `requesting-code-review` - Pre-review checklist
- `receiving-code-review` - Feedback integration
- `using-git-worktrees` - Parallel branch development
- `finishing-a-development-branch` - Merge/PR decisions
- `subagent-driven-development` - Quality-gated rapid iteration

**4. Meta Skills** (`skills/meta/`)
- `writing-skills` - Skill creation best practices
- `sharing-skills` - Contributing via branch and PR
- `testing-skills-with-subagents` - Skill quality validation
- `using-superpowers` - System introduction

**Slash Commands:**
- `/superpowers:brainstorm` - Interactive design refinement
- `/superpowers:write-plan` - Create implementation plan
- `/superpowers:execute-plan` - Execute plan in batches

**Design Philosophy:**
- Test-driven development mandatory
- Systematic over ad-hoc approaches
- Complexity minimization
- Evidence-based verification
- Problem-domain focus

**Latest Release:** v3.3.1 (October 28, 2025)

**Best For:** Teams enforcing systematic development practices and TDD workflows

**Repository:** https://github.com/obra/superpowers

---

### #4: BehiSecc/awesome-claude-skills
**⭐ 2,000 stars** | 140 forks

```bash
/plugin marketplace add BehiSecc/awesome-claude-skills
```

**Description:** Community-curated collection of practical and experimental Claude Skills.

**Features:**
- ✅ ~40 skills across 10 categories
- ✅ Broad coverage from documents to security
- ✅ Scientific research tools
- ✅ Media & content processing

**Skill Categories:**

**📄 Document Skills (4 skills)**
- Word, PDF, PowerPoint, spreadsheet manipulation

**🛠 Development & Code Tools (7 skills)**
- Artifact building, AWS development, MCP creation

**📊 Data & Analysis (2 skills)**
- Error tracing, CSV analysis

**🔬 Scientific & Research Tools (4 skills)**
- Database access (PubMed, PubChem, UniProt, ChEMBL, AlphaFold)
- Lab automation

**✍️ Writing & Research (5 skills)**
- Content creation, research assistance

**📘 Learning & Knowledge (2 skills)**
- Knowledge networking

**🎬 Media & Content (4 skills)**
- Video processing (YouTube transcripts, downloading)
- Image enhancement

**🤝 Collaboration & Project Management (5 skills)**
- Git workflows, project management

**🛡 Security & Web Testing (4 skills)**
- Security testing, debugging, web fuzzing

**🔧 Utility & Automation (4 skills)**
- File organization, task automation

**Notable Skills:**
- `aws-skills` - AWS development with CDK best practices
- `scientific-databases` - Access to 26 scientific databases
- `webapp-testing` - Playwright-based testing
- `youtube-transcript` - Extract YouTube transcripts
- `image-enhancer` - Image processing

**Best For:** Researchers, scientists, and developers needing specialized domain skills

**Repository:** https://github.com/BehiSecc/awesome-claude-skills

---

### #5: brennercruvinel/CCPlugins
**⭐ 2,000 stars** | 125 forks

```bash
/plugin marketplace add brennercruvinel/CCPlugins
```

**Description:** Professional framework with 24 enterprise-grade development commands.

**Features:**
- ✅ 24 professional commands
- ✅ Structured, predictable outcomes
- ✅ Optimized for Opus 4 and Sonnet 4
- ✅ Enterprise-grade workflows
- ✅ Built by developers for developers

**Philosophy:**
"Best Claude Code framework that actually saves time. Built by a dev tired of typing 'please act like a senior engineer' in every conversation."

**Key Commands:**
- `/review` - Comprehensive code review
- `/cleanproject` - Project cleanup
- [22 additional professional commands]

**Best For:** Enterprise developers wanting structured, senior-level workflows

**Repository:** https://github.com/brennercruvinel/CCPlugins

---

### #6: travisvn/awesome-claude-skills
**⭐ 1,700 stars** | 101 forks

```bash
/plugin marketplace add travisvn/awesome-claude-skills
```

**Description:** Curated list of awesome Claude Skills, resources, and tools for customizing Claude AI workflows.

**Features:**
- ✅ Official skills documentation
- ✅ Community skills collections
- ✅ Installation guides
- ✅ Best practices
- ✅ Links to obra/superpowers library

**Coverage:**
- 6+ official document/design skills
- 20+ skills from obra/superpowers
- Individual community skills
- Tutorials and guides

**Categories:**
- Document Skills (DOCX, PDF, PPTX, XLSX)
- Design & Creative
- Development tools
- Communication
- Skill creation

**Best For:** Discovering new skills and learning best practices

**Repository:** https://github.com/travisvn/awesome-claude-skills

---

### #7: EveryInc/every-marketplace
**⭐ 520 stars** | 58 forks

```bash
/plugin marketplace add EveryInc/every-marketplace
```

**Description:** Official Every-Env plugin marketplace for Claude Code extensions with focus on compounding engineering philosophy.

**Features:**
- ✅ Compounding Engineering plugin
- ✅ 17 specialized agents
- ✅ Multi-language support (Rails, TypeScript, Python)
- ✅ Integrated with git worktrees
- ✅ GitHub Issues integration

**Compounding Engineering Plugin:**

**Commands:**
- `/compounding-engineering:plan` - Transform ideas into structured plans
- `/compounding-engineering:work` - Systematic task execution with validation
- `/compounding-engineering:review` - 12+ parallel specialized review agents

**17 Specialized Agents:**
- Code review agents
- Quality assurance
- Architecture analysis
- Security analysis
- Performance optimization
- Research agents
- Workflow automation

**Philosophy:**
"Makes each unit of engineering work easier than the last"

**Features:**
- Codebase research
- Acceptance criteria generation
- Isolated worktrees
- Continuous validation
- Multi-agent code reviews

**Best For:** Teams focused on systematic planning and multi-agent workflows

**Repository:** https://github.com/EveryInc/every-marketplace

---

### #8: jeremylongshore/claude-code-plugins-plus
**⭐ 310 stars** | 40 forks

```bash
/plugin marketplace add jeremylongshore/claude-code-plugins-plus
```

**Description:** Massive plugin hub with 236 production-ready plugins across 15 categories.

**Features:**
- ✅ 236 production-ready plugins
- ✅ 168 Agent Skills (Anthropic spec v1.0 compliant)
- ✅ 5 MCP server plugins
- ✅ 62 AI instruction templates
- ✅ 15 categories

**Plugin Types:**
- AI instruction plugins (97%)
- MCP server plugins (2%)
- Agent Skills (<1%)

**Notable Plugins:**
- **Excel Analyst Pro** - Financial modeling toolkit (DCF models, LBO analysis)
- **Agent Context Manager** - Automatic AGENTS.md detection
- **Skills Powerkit** - First agent skills plugin with 5 auto capabilities:
  - Plugin creator
  - Validator
  - Manager
  - Auditor
  - Version bumper

**15 Categories:**
1. Automation
2. Business Tools
3. DevOps
4. Code Analysis
5. Debugging
6. AI/ML Assistance
7. Frontend Development
8. Security
9. Testing
10. Documentation
11. Performance
12. Database
13. Cloud Infrastructure
14. Accessibility
15. Mobile Development

**Comprehensive Documentation:**
- Learning paths
- Installation guides
- Usage examples

**Website:** https://claudecodeplugins.io or https://jeremylongshore.github.io/claude-code-plugins/

**Best For:** Developers wanting access to the largest collection of plugins in one place

**Repository:** https://github.com/jeremylongshore/claude-code-plugins-plus

---

### #9: GiladShoham/awesome-claude-plugins
**⭐ 32 stars** | 4 forks

```bash
/plugin marketplace add GiladShoham/awesome-claude-plugins
```

**Description:** Curated marketplace following Claude Plugin Marketplace specification.

**Features:**
- ✅ Plugin marketplace framework
- ✅ Structured organization
- ✅ Example plugins (Calculator, Weather, Translation)
- ✅ Validation tools
- ✅ CI automation
- ✅ Local testing support

**Example Plugins:**
- Calculator (v1.0.0)
- Weather service (v1.2.0)
- Translation tool (v2.0.0)

**Tools:**
- Automated validation scripts
- JSON syntax checking
- Semantic versioning validation
- Filename consistency checks

**Best For:** Plugin developers learning marketplace structure and creating their own marketplaces

**Repository:** https://github.com/GiladShoham/awesome-claude-plugins

---

## Official Anthropic Resources

### anthropics/skills
See [#2 in Top Marketplaces](#-2-anthropicsskills)

**Official Documentation:**
- https://docs.claude.com/en/docs/claude-code/skills
- https://www.anthropic.com/news/claude-code-plugins

**License:** Apache 2.0

---

## Community Marketplaces

### Large-Scale Community Collections

#### 1. hesreallyhim/awesome-claude-code
See [#1 in Top Marketplaces](#-1-hesreallyhimawesome-claude-code)

**Special Features:**
- Infrastructure showcases
- Alternative clients
- Conversation browsers
- Agent command centers

---

#### 2. travisvn/awesome-claude-skills
See [#6 in Top Marketplaces](#6-travisvnawesome-claude-skills)

**External Resources:**
- Links to skillsmp.com (2000+ skills search)
- Official documentation
- Community contributions

---

#### 3. BehiSecc/awesome-claude-skills
See [#4 in Top Marketplaces](#4-behiseccawesome-claude-skills)

**Unique Skills:**
- `ship-learn-next` - Next.js learning
- `git-pushing` - Git automation
- `review-implementing` - Review integration
- `test-fixing` - Test debugging

---

### Medium-Scale Collections

#### ComposioHQ/awesome-claude-skills

**Description:** Curated list of Claude Skills and resources for workflow customization.

**Repository:** https://github.com/ComposioHQ/awesome-claude-skills

---

#### VoltAgent/awesome-claude-skills

**Description:** The awesome collection of Claude Skills and resources.

**Repository:** https://github.com/VoltAgent/awesome-claude-skills

---

#### abubakarsiddik31/claude-skills-collection

**Description:** Curated collection of official and community-built Claude Skills.

**Features:**
- Gathers publicly available skills
- Both built-in Anthropic tools
- Creative community contributions

**Repository:** https://github.com/abubakarsiddik31/claude-skills-collection

---

### Framework-Based Collections

#### obra/superpowers
See [#3 in Top Marketplaces](#-3-obrasuperpowers)

**Community Companion:**
- **obra/superpowers-skills** - Community-editable skills for superpowers plugin

**Repository:** https://github.com/obra/superpowers-skills

---

#### brennercruvinel/CCPlugins
See [#5 in Top Marketplaces](#5-brennercruvinelccplugins)

**Fork Variants:**
- ffscoal/ccplugins
- roygabriel/claude-code-plugins

---

## Specialized Marketplaces

### TYPO3 Development: netresearch/claude-code-marketplace

```bash
/plugin marketplace add netresearch/claude-code-marketplace
```

**Description:** Curated collection of Claude Code skills for TYPO3 development by Netresearch DTT GmbH.

**Available Plugins:**
1. **TYPO3 Documentation** (v1.0.0-20251027)
   - Create TYPO3 extension documentation

2. **TYPO3 Testing** (v1.0.0-20251027)
   - Manage TYPO3 extension tests

3. **TYPO3 DDEV Setup** (v1.0.0)
   - Automate DDEV environment setup

4. **TYPO3 Core Contributions** (v1.0.0)
   - Guide TYPO3 core contributions

5. **TYPO3 Conformance** (v1.0.0-20251027)
   - Evaluate TYPO3 standards compliance

6. **Netresearch Branding**

**Sync System:**
- Automated GitHub Actions workflow
- Each skill maintained in own repository
- Auto-sync to marketplace

**Best For:** TYPO3 developers and teams

**Repository:** https://github.com/netresearch/claude-code-marketplace

---

### Multi-Purpose Specialized Marketplaces

#### ccplugins/marketplace

```bash
/plugin marketplace add ccplugins/marketplace
```

**Description:** Claude Code Plugins Marketplace — Only Curated Awesome Plugins

**Features:**
- Hooks for workflow modification
- Dynamic plugin installation
- Lightweight system context
- Community contributions welcome

**Repository:** https://github.com/ccplugins/marketplace

**Companion:** ccplugins/awesome-claude-code-plugins

---

#### ananddtyagi/claude-code-marketplace

```bash
/plugin marketplace add ananddtyagi/claude-code-marketplace
```

**Description:** Community-driven marketplace with automatic syncing from live database.

**Features:**
- Auto-sync when commands published/updated
- Database-driven updates
- Community submissions

**Repository:** https://github.com/ananddtyagi/claude-code-marketplace

---

#### Dev-GOM/claude-code-marketplace

```bash
/plugin marketplace add Dev-GOM/claude-code-marketplace
```

**Description:** Powerful productivity plugins for automating common development workflows.

**Features:**
- Auto-commit functionality
- TODO scanning
- Complexity monitoring
- Workflow automation

**Repository:** https://github.com/Dev-GOM/claude-code-marketplace

---

#### feed-mob/claude-code-marketplace

```bash
/plugin marketplace add feed-mob/claude-code-marketplace
```

**Description:** Claude Plugins from FeedMob Dev Team.

**Repository:** https://github.com/feed-mob/claude-code-marketplace

---

#### getty104/claude-code-marketplace

```bash
/plugin marketplace add getty104/claude-code-marketplace
```

**Repository:** https://github.com/getty104/claude-code-marketplace

---

#### hugoduncan/claude-marketplace

```bash
/plugin marketplace add hugoduncan/claude-marketplace
```

**Repository:** https://github.com/hugoduncan/claude-marketplace

---

#### yanmxa/cc-plugins

```bash
/plugin marketplace add yanmxa/cc-plugins
```

**Description:** Claude Code plugins for lazy developers (in a good way) - automate and capture workflows to reclaim your time.

**Repository:** https://github.com/yanmxa/cc-plugins

---

## Plugin Collections

### Specialized Agent Collections

#### wshobson/agents
**⭐ ~20,000 stars (estimated from search results)**

**Description:** Intelligent automation and multi-agent orchestration for Claude Code.

**Features:**
- Multi-agent orchestration
- Intelligent automation
- Over 80 specialized sub-agents

**Repository:** https://github.com/wshobson/agents

---

#### hesreallyhim/a-list-of-claude-code-agents

**Description:** A list of Claude Code Sub-Agents submitted by the community.

**Repository:** https://github.com/hesreallyhim/a-list-of-claude-code-agents

---

### Awesome Lists

#### ccplugins/awesome-claude-code-plugins

**Description:** Awesome Claude Code plugins — a curated list of slash commands, subagents, MCP servers, and hooks.

**Repository:** https://github.com/ccplugins/awesome-claude-code-plugins

---

#### hekmon8/awesome-claude-code-plugins

**Description:** Find best Claude Code plugins for vibe coding!

**Repository:** https://github.com/hekmon8/awesome-claude-code-plugins

---

#### jqueryscript/awesome-claude-code

**Description:** Curated list of awesome tools, IDE integrations, frameworks, and resources for developers working with Claude Code.

**Repository:** https://github.com/jqueryscript/awesome-claude-code

---

#### alvinunreal/awesome-claude

**Description:** A curated list of awesome things related to Anthropic Claude.

**Repository:** https://github.com/alvinunreal/awesome-claude

---

#### milisp/awesome-claude-dxt

**Description:** Awesome Claude Desktop Extensions (dxt) (not only Claude) mcpb.

**Repository:** https://github.com/milisp/awesome-claude-dxt

---

## Installation Guide

### Adding a Marketplace

```bash
# General syntax
/plugin marketplace add owner/repository-name

# Examples
/plugin marketplace add anthropics/skills
/plugin marketplace add obra/superpowers-marketplace
/plugin marketplace add jeremylongshore/claude-code-plugins-plus
/plugin marketplace add hesreallyhim/awesome-claude-code
```

### Installing Plugins from Marketplace

```bash
# Method 1: Interactive menu
/plugin

# Method 2: Direct installation
/plugin install plugin-name@marketplace-name

# Example
/plugin install superpowers@superpowers-marketplace
```

### Listing Installed Marketplaces

```bash
/plugin marketplace list
```

### Removing a Marketplace

```bash
/plugin marketplace remove marketplace-name
```

### Updating Plugins

```bash
# Update specific plugin
/plugin update plugin-name

# Update all plugins
/plugin update
```

### Listing Available Skills

```bash
/skills
```

### Getting Help

```bash
/help
```

---

## Comparison Matrix

### By Size & Coverage

| Marketplace | Stars | Plugins/Skills | Categories | Type |
|-------------|-------|----------------|------------|------|
| hesreallyhim/awesome-claude-code | 16.6k | 100+ | 8+ | Awesome List |
| anthropics/skills | 15.9k | 13+ | 5 | Official |
| obra/superpowers | 6.2k | 20+ | 4 | Framework |
| BehiSecc/awesome-claude-skills | 2.0k | 40 | 10 | Curated |
| brennercruvinel/CCPlugins | 2.0k | 24 | N/A | Framework |
| travisvn/awesome-claude-skills | 1.7k | 30+ | 5+ | Awesome List |
| EveryInc/every-marketplace | 520 | 17 agents | 1 | Specialized |
| jeremylongshore/claude-code-plugins-plus | 310 | 236 | 15 | Mega Collection |
| GiladShoham/awesome-claude-plugins | 32 | 3 examples | N/A | Template |

---

### By Focus Area

| Focus Area | Best Marketplace | Alternative |
|------------|------------------|-------------|
| **Official Skills** | anthropics/skills | - |
| **Comprehensive Workflows** | hesreallyhim/awesome-claude-code | jqueryscript/awesome-claude-code |
| **Systematic Development** | obra/superpowers | - |
| **Scientific Research** | BehiSecc/awesome-claude-skills | - |
| **Enterprise Workflows** | brennercruvinel/CCPlugins | EveryInc/every-marketplace |
| **Maximum Plugin Count** | jeremylongshore/claude-code-plugins-plus | - |
| **TYPO3 Development** | netresearch/claude-code-marketplace | - |
| **Financial Analysis** | jeremylongshore/claude-code-plugins-plus | - |
| **Multi-Agent Systems** | wshobson/agents | EveryInc/every-marketplace |
| **Learning Resources** | travisvn/awesome-claude-skills | - |
| **Plugin Development** | GiladShoham/awesome-claude-plugins | - |

---

### By Use Case

| Use Case | Recommended Marketplace |
|----------|------------------------|
| **Just Getting Started** | anthropics/skills |
| **Maximum Coverage** | hesreallyhim/awesome-claude-code |
| **Test-Driven Development** | obra/superpowers |
| **Scientific Research** | BehiSecc/awesome-claude-skills |
| **Enterprise Development** | brennercruvinel/CCPlugins |
| **Financial Modeling** | jeremylongshore/claude-code-plugins-plus (Excel Analyst Pro) |
| **TYPO3 CMS** | netresearch/claude-code-marketplace |
| **Learning Best Practices** | travisvn/awesome-claude-skills |
| **Multi-Agent Workflows** | EveryInc/every-marketplace |
| **Creating Your Own Marketplace** | GiladShoham/awesome-claude-plugins |

---

## Web-Based Marketplaces

### skillsmp.com
**URL:** https://skillsmp.com

**Features:**
- 2000+ Claude AI skills
- Intelligent search and filtering
- Category, author, and popularity filters
- All skills open source from GitHub

**Best For:** Discovering skills from a web interface

---

### claudecodeplugins.io
**URL:** https://claudecodeplugins.io
**Alternative:** https://jeremylongshore.github.io/claude-code-plugins/

**Features:**
- 220-236 plugins across 15 categories
- Built with Next.js 15 + PostgreSQL + Cloud Run
- Comprehensive documentation
- Learning paths

**Repository:** jeremylongshore/claude-code-plugins-plus

---

### claudecodemarketplace.com
**URL:** https://claudecodemarketplace.com

**Description:** Website directory cataloging various Claude Code plugins from the community.

**Features:**
- Browse marketplaces
- Search plugins
- Installation instructions

---

### claudelog.com
**URL:** https://claudelog.com/claude-code-mcps/awesome-claude-code/

**Description:** Resource hub for Claude Code with curated awesome list.

---

## Quick Reference

### Top 5 by Stars

1. **hesreallyhim/awesome-claude-code** - 16.6k ⭐
2. **anthropics/skills** - 15.9k ⭐
3. **obra/superpowers** - 6.2k ⭐
4. **BehiSecc/awesome-claude-skills** - 2.0k ⭐
5. **brennercruvinel/CCPlugins** - 2.0k ⭐

---

### Quick Install Commands

```bash
# Official
/plugin marketplace add anthropics/skills

# Most Comprehensive
/plugin marketplace add hesreallyhim/awesome-claude-code

# Systematic Development
/plugin marketplace add obra/superpowers-marketplace
/plugin install superpowers@superpowers-marketplace

# Scientific Research
/plugin marketplace add BehiSecc/awesome-claude-skills

# Enterprise Workflows
/plugin marketplace add brennercruvinel/CCPlugins

# Maximum Plugins
/plugin marketplace add jeremylongshore/claude-code-plugins-plus

# TYPO3 Development
/plugin marketplace add netresearch/claude-code-marketplace

# Multi-Agent Systems
/plugin marketplace add EveryInc/every-marketplace
```

---

### Essential Commands

```bash
# Add marketplace
/plugin marketplace add owner/repo

# List marketplaces
/plugin marketplace list

# Remove marketplace
/plugin marketplace remove marketplace-name

# Browse plugins
/plugin

# Install plugin
/plugin install plugin-name@marketplace-name

# Update plugin
/plugin update plugin-name

# List skills
/skills

# Get help
/help
```

---

## Contributing

Found a marketplace we missed? Submit a pull request to add it to this guide!

### What to Include

1. Repository name and URL
2. Star and fork counts
3. Description
4. Key features
5. Installation command
6. Best use cases

---

## Resources

### Official Documentation
- **Claude Code Docs:** https://docs.claude.com/en/docs/claude-code/
- **Plugin Marketplaces:** https://docs.claude.com/en/docs/claude-code/plugin-marketplaces
- **Skills Documentation:** https://docs.claude.com/en/docs/claude-code/skills
- **Anthropic Blog:** https://www.anthropic.com/news/claude-code-plugins

### Community Resources
- **GitHub Topics:**
  - https://github.com/topics/claude-skills
  - https://github.com/topics/claude-code-plugins
  - https://github.com/topics/claude-code-plugin
  - https://github.com/topics/claude-code
- **Web Marketplaces:**
  - https://skillsmp.com
  - https://claudecodeplugins.io
  - https://claudecodemarketplace.com

### Articles & Guides
- "Anthropic's Claude Skills Are Taking the AI Community by Storm" - https://karozieminski.substack.com/p/claude-skills-anthropic-viral-toolkit-agentic-workflows-community-guide
- "Claude Skills are awesome, maybe a bigger deal than MCP" - https://simonwillison.net/2025/Oct/16/claude-skills/
- "Improving your coding workflow with Claude Code Plugins" - https://composio.dev/blog/claude-code-plugin

---

## Statistics Summary

**Total Resources Documented:** 30+

**Total Stars Across All Repos:** 50,000+

**Total Plugins/Skills Available:** 500+

**Total Categories Covered:** 30+

**Official Skills:** 13+

**Community Marketplaces:** 20+

**Specialized Agents:** 100+

**Web-Based Platforms:** 4

---

## License

This document is provided for informational purposes. Individual repositories have their own licenses:
- **anthropics/skills:** Apache 2.0
- **obra/superpowers:** MIT
- Other repositories: Check individual licenses

---

**Maintained by the Claude Code community**

**Last Updated:** 2025-11-08

**Version:** 1.0
