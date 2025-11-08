# Community Skills Patterns: awesome-claude-skills Analysis

**Source:** https://github.com/travisvn/awesome-claude-skills
**Date:** 2025-11-08
**Official Skills Repo:** https://github.com/anthropics/skills

---

## Table of Contents

1. [Repository Overview](#repository-overview)
2. [Official Skills Patterns](#official-skills-patterns)
3. [Community Contributions](#community-contributions)
4. [Skill Structure Patterns](#skill-structure-patterns)
5. [Creation & Distribution Patterns](#creation--distribution-patterns)
6. [Best Practices from Community](#best-practices-from-community)
7. [Key Insights & Takeaways](#key-insights--takeaways)

---

## Repository Overview

### Purpose
**awesome-claude-skills** is a curated community repository showcasing:
- Official Anthropic skills with examples
- Community-contributed skill libraries
- Best practices and patterns
- Installation guides and tutorials
- Security recommendations

### Statistics
- **Official Skills Repo:** 15.9k stars, 1.4k forks
- **License:** Apache 2.0 (open source)
- **Platforms:** Claude Code CLI, Claude Desktop, Claude API

### Key Resources
- **Official Docs:** https://docs.claude.com/en/docs/claude-code/skills
- **Community Hub:** https://github.com/travisvn/awesome-claude-skills
- **Official Skills:** https://github.com/anthropics/skills
- **Major Community Library:** https://github.com/obra/superpowers

---

## Official Skills Patterns

### 1. Document Processing Skills

**Pattern: Microsoft Office Suite Integration**

| Skill | Purpose | Key Features |
|-------|---------|-------------|
| **docx** | Word documents | Tracked changes, comments, formatting preservation, text extraction |
| **pdf** | PDF manipulation | Extract text/tables, create PDFs, merge/split, handle forms |
| **pptx** | PowerPoint | Layouts, templates, charts, automated slide generation |
| **xlsx** | Excel spreadsheets | Formulas, formatting, data analysis, visualization |

**Pattern Insight:** These skills focus on **comprehensive manipulation** rather than simple creation. They include:
- Advanced formatting preservation
- Complex data structures (formulas, charts)
- Document analysis capabilities
- Professional output quality

---

### 2. Design & Creative Skills

**Pattern: Generative Content Creation**

| Skill | Purpose | Technology | Output |
|-------|---------|-----------|--------|
| **algorithmic-art** | Generative art | p5.js | Seeded randomness, flow fields, particle systems |
| **canvas-design** | Visual design | Design principles | PNG, PDF formats |
| **slack-gif-creator** | Animated GIFs | Size optimization | Slack-ready animations |

**Pattern Insight:** Creative skills emphasize:
- **Deterministic output** via seeded randomness (reproducibility)
- **Platform optimization** (e.g., Slack size constraints)
- **Professional design philosophy** over ad-hoc generation

---

### 3. Development Skills

**Pattern: Framework-Specific Builders**

| Skill | Purpose | Tech Stack | Use Case |
|-------|---------|-----------|----------|
| **artifacts-builder** | UI components | React, Tailwind, shadcn/ui | Complex claude.ai artifacts |
| **mcp-builder** | MCP servers | Python/FastMCP, TypeScript/SDK | External API integration |
| **webapp-testing** | Web testing | Playwright | UI verification, debugging |

**Pattern Insight:** Development skills follow **structured workflows**:
- **Phase-based approach** (research → implementation → review → evaluation)
- **Technology-specific branching** (Python vs. Node paths)
- **Quality gates** at each phase
- **Comprehensive testing** built-in

**Example: mcp-builder Workflow**
```
Phase 1: Deep Research & Planning
  ├── Study API documentation
  ├── Review framework docs
  └── Create comprehensive plan

Phase 2: Implementation
  ├── Project setup
  ├── Core infrastructure
  └── Systematic tool development

Phase 3: Review & Refine
  ├── Quality assurance
  ├── Testing validation
  └── Performance review

Phase 4: Create Evaluations
  └── Develop test scenarios
```

---

### 4. Communication Skills

**Pattern: Enterprise Branding & Documentation**

| Skill | Purpose | Use Case |
|-------|---------|----------|
| **brand-guidelines** | Branding standards | Apply Anthropic colors, typography |
| **internal-comms** | Internal docs | Status reports, newsletters, FAQs |
| **theme-factory** | Theme generation | 10 professional presets + custom themes |

**Pattern Insight:** Communication skills enforce **consistency**:
- Predefined brand standards
- Template-based generation
- Professional tone and formatting
- Reusable preset libraries

---

### 5. Meta Skills

**Pattern: Self-Referential Skill Creation**

| Skill | Purpose | Approach |
|-------|---------|----------|
| **skill-creator** | Build new skills | Interactive Q&A, templates |
| **template-skill** | Starter template | Scaffold structure |

**Pattern Insight:** Meta skills use **progressive disclosure**:
```
Metadata (name, description, license)
    ↓
SKILL.md (lean instructions)
    ↓
Bundled Resources
    ├── scripts/ (executable code)
    ├── references/ (detailed docs)
    └── assets/ (templates, images)
```

---

## Community Contributions

### obra/superpowers Library

**Stats:** 20+ skills, comprehensive development workflow system
**Philosophy:** Mandatory systematic approaches over ad-hoc solutions
**Installation:** Via marketplace (`/plugin marketplace add obra/superpowers-marketplace`)

#### Skill Categories

**1. Testing Skills** (`skills/testing/`)

| Skill | Pattern | Methodology |
|-------|---------|-------------|
| **test-driven-development** | RED-GREEN-REFACTOR cycle | Mandatory TDD workflow |
| **condition-based-waiting** | Async testing | Patterns for async scenarios |
| **testing-anti-patterns** | Documentation | Common testing pitfalls |

**Key Pattern:** Testing skills enforce **test-first development** as non-negotiable.

---

**2. Debugging Skills** (`skills/debugging/`)

| Skill | Pattern | Approach |
|-------|---------|----------|
| **systematic-debugging** | Four-phase process | Root cause analysis |
| **root-cause-tracing** | Methodology | Identify underlying problems |
| **verification-before-completion** | Validation | Pre-completion checks |
| **defense-in-depth** | Multi-layer | Multiple validation layers |

**Key Pattern:** Debugging follows **systematic, evidence-based processes**:

```
1. Reproduce the issue
2. Isolate the root cause
3. Develop and test fix
4. Verify completion (defense-in-depth)
```

---

**3. Collaboration Skills** (`skills/collaboration/`)

| Skill | Pattern | Purpose |
|-------|---------|---------|
| **brainstorming** | Socratic questioning | Design refinement (not prescriptive) |
| **writing-plans** | Detailed planning | Implementation blueprints |
| **executing-plans** | Batch execution | Checkpointed progress |
| **dispatching-parallel-agents** | Concurrent workflows | Parallel subagent execution |
| **requesting-code-review** | Checklist | Pre-review preparation |
| **receiving-code-review** | Integration | Feedback incorporation |
| **using-git-worktrees** | Parallel branches | Concurrent development |
| **finishing-a-development-branch** | Decision framework | Merge/PR decisions |
| **subagent-driven-development** | Quality gates | Rapid iteration with validation |

**Key Pattern:** Collaboration skills emphasize **structured communication**:
- **Socratic brainstorming** > prescriptive design
- **Batch execution** > streaming implementation
- **Quality gates** > continuous delivery
- **Parallel workflows** where appropriate

---

**4. Meta Skills** (`skills/meta/`)

| Skill | Pattern | Purpose |
|-------|---------|---------|
| **writing-skills** | Best practices | New skill creation |
| **sharing-skills** | Contribution | Branch and PR workflow |
| **testing-skills-with-subagents** | Quality validation | Skill testing |
| **using-superpowers** | Introduction | System onboarding |

**Key Pattern:** Self-improvement via **meta-circular development**:
- Skills for creating skills
- Skills for testing skills
- Skills for sharing skills

---

#### Superpowers Design Philosophy

**Core Principles:**

1. **Mandatory Systematic Approaches**
   - "When a skill exists for your task, using it becomes required"
   - Enforces best practices over improvisation

2. **Test-Driven Development**
   - "Write tests first, always"
   - RED-GREEN-REFACTOR as foundational workflow

3. **Complexity Minimization**
   - Simplicity as primary design goal
   - Domain-level focus over implementation details

4. **Evidence-Based Verification**
   - "Verify before declaring success"
   - Multiple validation layers (defense-in-depth)

5. **Automatic Activation**
   - Skills trigger contextually during workflows
   - TDD activates during features
   - Debugging activates during problem diagnosis
   - Verification activates before completion

**Unique Pattern: SessionStart Hook Integration**

```
SessionStart hook loads "using-superpowers" skill initially
    ↓
Claude Code discovers relevant skills automatically
    ↓
Skills activate contextually during conversation
    ↓
Mandatory workflows enforce systematic approaches
```

---

### Other Community Skills

| Skill | Repository | Focus |
|-------|-----------|-------|
| **ios-simulator-skill** | Community | iOS app simulation |
| **ffuf-web-fuzzing** | Community | Web security testing |
| **playwright-skill** | Community | Advanced Playwright automation |
| **claude-d3js-skill** | Community | D3.js visualization |
| **claude-scientific-skills** | Community | Scientific computing |
| **web-asset-generator** | Community | Web asset creation |

**Pattern Insight:** Community skills focus on **specialized domains** not covered by official skills.

---

## Skill Structure Patterns

### 1. YAML Frontmatter Pattern

**Minimal Required Structure:**
```yaml
name: my-skill-name
description: "Clear description of what this skill does and when Claude should use it"
```

**Extended Structure with License:**
```yaml
name: my-skill-name
description: "Detailed description with activation triggers"
license: Apache-2.0
```

**Best Practice Pattern:**
```yaml
name: security-scanner
description: "Reviews code for security vulnerabilities including SQL injection, XSS, CSRF, and authentication issues. Use when user asks to: review security, audit code, find vulnerabilities, check for exploits, analyze security risks, or perform security assessment."
license: Apache-2.0
```

**Key Insight:** The `description` field is **critical for activation**. Include:
- What the skill does
- When Claude should use it
- Natural trigger phrases users would say
- Specific use cases or keywords

---

### 2. Directory Structure Patterns

**Pattern A: Simple Skill (Instructions Only)**
```
my-skill/
└── SKILL.md
```

**Pattern B: Skill with References**
```
my-skill/
├── SKILL.md
└── references/
    ├── api-docs.md
    └── examples.md
```

**Pattern C: Skill with Scripts**
```
my-skill/
├── SKILL.md
└── scripts/
    ├── helper.py
    └── validator.js
```

**Pattern D: Complete Skill Bundle**
```
my-skill/
├── SKILL.md           # Required: Main instructions
├── scripts/           # Optional: Executable code
│   ├── process.py
│   └── validate.sh
├── references/        # Optional: Detailed documentation
│   ├── guide.md
│   └── api-reference.md
└── assets/            # Optional: Templates, images
    ├── template.json
    └── diagram.png
```

**Progressive Disclosure Pattern:**
```
User request → Claude reads description
    ↓
Skill activated → Claude reads SKILL.md
    ↓
Needs more info → Claude reads references/
    ↓
Needs execution → Claude runs scripts/
    ↓
Needs templates → Claude uses assets/
```

---

### 3. SKILL.md Content Patterns

**Pattern: Phase-Based Workflow (from mcp-builder)**

```markdown
# Skill Name

## Phase 1: Research and Planning
- Step 1: Study documentation
- Step 2: Analyze requirements
- Step 3: Create comprehensive plan

## Phase 2: Implementation
- Step 1: Setup project structure
- Step 2: Implement core features
- Step 3: Add error handling

## Phase 3: Review and Refine
- Step 1: Quality assurance
- Step 2: Testing
- Step 3: Documentation

## Phase 4: Validation
- Step 1: Create test scenarios
- Step 2: Verify functionality
- Step 3: Performance check
```

**Pattern: Principles-Based (from superpowers testing)**

```markdown
# Test-Driven Development

## Core Principles
1. Write tests first, always
2. RED: Write failing test
3. GREEN: Make test pass
4. REFACTOR: Improve code quality

## When to Activate
- Implementing new features
- Adding functionality
- Changing behavior

## Process
1. Understand requirements
2. Write failing test
3. Implement minimal code
4. Verify test passes
5. Refactor for quality
6. Repeat
```

**Pattern: Checklist-Based (from code review)**

```markdown
# Code Review

## Review Checklist

### Security
- [ ] No SQL injection vulnerabilities
- [ ] No XSS vulnerabilities
- [ ] Authentication properly implemented
- [ ] Authorization checks present

### Performance
- [ ] No N+1 queries
- [ ] Efficient algorithms used
- [ ] Proper caching implemented

### Code Quality
- [ ] Follows project style
- [ ] Properly documented
- [ ] Error handling present
```

**Pattern: Socratic/Interactive (from brainstorming)**

```markdown
# Brainstorming

## Approach
Use questioning techniques to refine design:

1. Ask about requirements and constraints
2. Explore alternative approaches
3. Identify trade-offs
4. Guide user toward optimal solution

## Questions to Ask
- What problem are we solving?
- Who are the users?
- What are the constraints?
- What are alternative approaches?
- What are the trade-offs?
```

---

### 4. Instruction Writing Patterns

**Pattern A: Imperative Voice**
```markdown
To accomplish X:
1. Do Y
2. Then do Z
3. Finally, verify A
```

**Pattern B: Conditional Logic**
```markdown
If the project uses Python:
- Use FastMCP framework
- Follow Python conventions

If the project uses TypeScript:
- Use MCP SDK
- Follow TypeScript patterns
```

**Pattern C: Layered Complexity**
```markdown
## Basic Usage
Simple instructions for common cases

## Advanced Usage
Complex scenarios with edge cases

## Reference Materials
Detailed documentation for deep dives
```

---

## Creation & Distribution Patterns

### 1. Creation Workflow (from skill-creator)

**Six-Step Process:**

```
1. Understand with Examples
   ├── Gather concrete use cases
   ├── Identify common patterns
   └── Define scope

2. Plan Reusable Contents
   ├── Identify needed scripts
   ├── Determine reference docs
   └── List required assets

3. Initialize
   ├── Run init_skill.py (if using tools)
   ├── Or manually create directory structure
   └── Create basic SKILL.md

4. Edit
   ├── Write metadata (name, description)
   ├── Populate SKILL.md with instructions
   ├── Add scripts, references, assets
   └── Use imperative language

5. Package
   ├── Run package_skill.py (if using tools)
   ├── Or validate manually
   └── Test activation

6. Iterate
   ├── Test in real scenarios
   ├── Gather feedback
   └── Refine based on usage
```

---

### 2. Distribution Patterns

**Pattern A: Personal Skills**
```bash
# Location: ~/.claude/skills/my-skill/
# Scope: Your machine only
# Distribution: Not shared

# Creation
mkdir -p ~/.claude/skills/my-skill
cd ~/.claude/skills/my-skill
# Create SKILL.md and resources
```

**Pattern B: Project Skills**
```bash
# Location: .claude/skills/team-skill/
# Scope: Git repository (team-shared)
# Distribution: Via git

# Creation
mkdir -p .claude/skills/team-skill
cd .claude/skills/team-skill
# Create SKILL.md and resources

# Share with team
git add .claude/skills/team-skill
git commit -m "Add team-skill for [purpose]"
git push
```

**Pattern C: Plugin Skills**
```bash
# Location: my-plugin/skills/
# Scope: Bundled with plugin
# Distribution: Via plugin marketplace

# Structure
my-plugin/
├── .claude-plugin/
│   └── plugin.json
└── skills/
    └── my-skill/
        └── SKILL.md

# Distribution
/plugin marketplace add author/plugin-marketplace
/plugin install my-plugin@plugin-marketplace
```

**Pattern D: Standalone Repository**
```bash
# Location: GitHub repository
# Scope: Public/community
# Distribution: Via awesome-claude-skills or direct

# Example: obra/superpowers
/plugin marketplace add obra/superpowers-marketplace
/plugin install superpowers@superpowers-marketplace

# Verify
/help  # Check for new commands
/skills  # List installed skills
```

---

### 3. Installation Pattern Comparison

| Pattern | Command | Use Case |
|---------|---------|----------|
| **Marketplace** | `/plugin marketplace add author/repo` | Official or popular plugins |
| **Local Directory** | `/plugin add /path/to/skill` | Development and testing |
| **Git Clone** | Manual clone + `/plugin add` | Custom repositories |
| **Claude Desktop** | Settings > Capabilities | Desktop app users |
| **API** | `/v1/skills` endpoint | API integration |

---

## Best Practices from Community

### 1. Description Writing (Critical!)

**❌ Bad Descriptions:**
```yaml
description: "Helps with code"
description: "Useful tool"
description: "General purpose skill"
```

**✅ Good Descriptions:**
```yaml
description: "Reviews code for security vulnerabilities including SQL injection, XSS, CSRF, and authentication issues. Use when user asks to: review security, audit code, find vulnerabilities, check for exploits, analyze security risks."

description: "Generates comprehensive unit and integration tests following project patterns. Use when user asks to: write tests, add test coverage, generate test cases, create unit tests, add integration tests."

description: "Creates generative art using p5.js with seeded randomness, flow fields, and particle systems. Use when user asks to: create art, generate visuals, make algorithmic art, design generative graphics."
```

**Pattern Insight:** Include:
- **What it does** (specific, not vague)
- **When to activate** (explicit triggers)
- **Natural language phrases** users would say
- **Specific technologies or methods** used

---

### 2. Skill Scope (Focus Over Breadth)

**❌ Too Broad:**
```
database-everything/     # Tries to handle all database tasks
code-helper/             # Vague, unclear purpose
general-tool/            # Not specific enough
```

**✅ Focused:**
```
sql-optimizer/           # Specific: SQL query optimization
postgres-migration/      # Specific: PostgreSQL migrations
redis-cache-pattern/     # Specific: Redis caching patterns
```

**Pattern Insight:**
- One skill = one clear responsibility
- Better to have 5 focused skills than 1 broad skill
- Easier for Claude to decide when to activate
- More maintainable and testable

---

### 3. Tool Restrictions (Principle of Least Privilege)

**Pattern: Analysis Only**
```yaml
name: code-reviewer
allowed-tools: [Read, Grep, Glob]
# Read-only: Can analyze but not modify
```

**Pattern: Modification Allowed**
```yaml
name: test-generator
allowed-tools: [Read, Write, Edit, Grep, Glob, Bash]
# Can create and modify files
```

**Pattern: Research & Web**
```yaml
name: research-assistant
allowed-tools: [Read, Write, Edit, WebFetch, WebSearch, Grep, Glob]
# Can search web and create research documents
```

**Pattern Insight:**
- Use **minimal tools** needed for the task
- Analysis skills: Read, Grep, Glob only
- Generation skills: Add Write, Edit
- Execution skills: Add Bash cautiously
- Research skills: Add WebFetch, WebSearch

---

### 4. Security Considerations

**Community Warning (from awesome-claude-skills):**
> "Skills can execute arbitrary code in Claude's environment"

**Recommended Practices:**

1. **Review Code Before Installation**
   ```bash
   # Clone and inspect before adding
   git clone https://github.com/author/skill-repo
   cd skill-repo
   # Review SKILL.md and scripts/
   cat skills/*/SKILL.md
   cat skills/*/scripts/*

   # Then add if safe
   /plugin add ./skill-repo
   ```

2. **Establish Enterprise Vetting**
   - Team review process for new skills
   - Approved skills list
   - Security audit for script-based skills

3. **Tool Restriction Enforcement**
   - Always specify `allowed-tools`
   - Never grant unnecessary permissions
   - Audit tool usage in scripts

4. **Source Verification**
   - Prefer official Anthropic skills
   - Verify well-known community authors
   - Check repository stars/forks
   - Review commit history

---

### 5. Token Efficiency

**Community Insight (from awesome-claude-skills):**
> "Skills consume approximately 30-50 tokens until activated"

**Pattern Implications:**

1. **Keep SKILL.md Lean**
   ```markdown
   # Good: Concise main instructions
   ## Process
   1. Do X
   2. Do Y
   3. See references/detailed-guide.md for details
   ```

   ```markdown
   # Bad: Everything in SKILL.md
   ## Process
   [5000 words of detailed instructions]
   ```

2. **Progressive Disclosure**
   ```
   SKILL.md (lean, ~500 tokens)
       ↓
   references/ (detailed, loaded as needed)
       ↓
   assets/ (templates, loaded when used)
   ```

3. **Multiple Focused Skills > One Large Skill**
   ```
   ✅ Better:
   - sql-optimizer/        (activated when optimizing SQL)
   - sql-migration/        (activated when migrating)
   - sql-debugging/        (activated when debugging SQL)

   ❌ Worse:
   - sql-everything/       (always loads all instructions)
   ```

---

### 6. Testing & Validation

**Pattern from superpowers: testing-skills-with-subagents**

```markdown
## Skill Testing Process

1. Create test scenarios
2. Launch subagent with skill
3. Verify behavior matches expectations
4. Iterate based on results
```

**Pattern: Real-World Testing**
```
1. Test with actual user requests
2. Monitor activation accuracy
3. Check output quality
4. Refine description based on false positives/negatives
```

**Pattern: Quality Gates**
```
Phase 1: Unit test the skill in isolation
Phase 2: Integration test with other skills
Phase 3: User acceptance test with real scenarios
Phase 4: Production monitoring
```

---

### 7. Documentation Patterns

**Pattern: Inline Examples**
```markdown
## Process

To review code for security:
1. Scan for SQL injection patterns
   Example: Look for raw string concatenation in queries

2. Check for XSS vulnerabilities
   Example: Verify HTML escaping on user input

3. Validate authentication
   Example: Ensure protected routes check auth tokens
```

**Pattern: Reference Separation**
```
SKILL.md               # Quick reference, process steps
└── references/
    ├── examples.md    # Detailed examples
    ├── patterns.md    # Common patterns
    └── anti-patterns.md  # What to avoid
```

**Pattern: Language-Specific Branching**
```markdown
## Implementation

For Python projects:
- Use FastMCP framework
- Follow PEP 8 style
- Add type hints

For TypeScript projects:
- Use MCP SDK
- Follow project ESLint config
- Add JSDoc comments
```

---

### 8. Naming Conventions

**Pattern Analysis:**

**Official Skills Use:**
- Lowercase with hyphens: `algorithmic-art`, `mcp-builder`
- Descriptive, not abbreviated: `webapp-testing` not `webtest`
- Technology-specific when relevant: `slack-gif-creator`

**Community Skills Use:**
- Domain-method pattern: `test-driven-development`
- Problem-solution pattern: `systematic-debugging`
- Tool-purpose pattern: `playwright-skill`

**Recommended Pattern:**
```
✅ Good:
- security-scanner
- api-docs-generator
- sql-query-optimizer
- react-component-builder

❌ Avoid:
- sec (too abbreviated)
- helper (too vague)
- tool123 (not descriptive)
- my_skill (use hyphens, not underscores)
```

---

## Key Insights & Takeaways

### 1. Skills vs Other Approaches

**Skills vs MCP Servers:**
| Aspect | Skills | MCP Servers |
|--------|--------|-------------|
| **Purpose** | Task-specific expertise | External data/API integration |
| **Activation** | Autonomous (Claude decides) | Tool calls (explicit) |
| **Portability** | Platform-independent | Platform-dependent |
| **Use Case** | Workflows, methodologies | Data sources, services |

**Skills vs System Prompts:**
| Aspect | Skills | System Prompts |
|--------|--------|----------------|
| **Modularity** | Highly modular | Monolithic |
| **Reusability** | Easily shared | Hard to share |
| **Activation** | Contextual | Always loaded |
| **Token Cost** | 30-50 until activated | Always consuming |
| **Distribution** | Via marketplace/git | Manual copy |

---

### 2. Architecture Patterns

**Pattern: Automatic Skill Stacking**

Community insight:
> "Multiple skills stack automatically without manual combination"

```
User: "Review this authentication code and generate tests"

Claude automatically activates:
1. security-scanner skill (reviews auth code)
2. test-generator skill (creates tests)
3. verification-before-completion skill (validates results)

No explicit skill combination needed!
```

**Pattern: Mandatory Workflow Enforcement** (superpowers)

```yaml
description: "Test-driven development. MUST be used when implementing features."

# Result: Enforces best practices automatically
User: "Add login feature"
→ TDD skill activates
→ Enforces test-first workflow
→ Prevents ad-hoc implementation
```

---

### 3. Community Ecosystem Patterns

**Distribution Hierarchy:**
```
Official Anthropic Skills
    ├── General-purpose capabilities
    ├── Widely applicable patterns
    └── Well-documented, tested

Major Community Libraries (e.g., superpowers)
    ├── Comprehensive workflow systems
    ├── Opinionated best practices
    └── Domain-specific excellence

Individual Community Skills
    ├── Specialized use cases
    ├── Experimental features
    └── Niche requirements
```

**Contribution Pattern:**
1. Individual creates skill for personal use
2. Tests and refines in real projects
3. Publishes to GitHub repository
4. Submits to awesome-claude-skills
5. Community adopts and provides feedback
6. Skill improves through iterations
7. May become part of larger library

---

### 4. Evolution Patterns

**From Simple to Complex:**

```
Stage 1: Simple SKILL.md
my-skill/
└── SKILL.md

Stage 2: Add References
my-skill/
├── SKILL.md
└── references/
    └── guide.md

Stage 3: Add Scripts
my-skill/
├── SKILL.md
├── references/
└── scripts/
    └── helper.py

Stage 4: Complete Bundle
my-skill/
├── SKILL.md
├── scripts/
├── references/
└── assets/
```

**From Personal to Team to Community:**

```
Stage 1: Personal (~/.claude/skills/)
- Solve your own problems
- Rapid iteration
- No coordination needed

Stage 2: Team (.claude/skills/)
- Share via git
- Team standards
- Code review process

Stage 3: Community (GitHub + marketplace)
- Public repository
- Documentation
- Maintenance commitment
```

---

### 5. Integration Patterns

**Pattern: Skills + Hooks + MCP** (from README.md:2935-2951)

```
Scenario: Security-First Development

Components:
1. Security-scanner skill (automatic code review)
2. Pre-commit hook (blocks commits with issues)
3. MCP server (logs findings to Jira)

Workflow:
User: "Review this authentication code"
→ Security skill activates
→ Finds SQL injection vulnerability
→ Reports to user
User: "Let me fix that. [makes changes]"
User: "Commit the changes"
→ Pre-commit hook runs
→ Security skill runs again
→ Still finds issues → Blocks commit
→ MCP logs to Jira
User: [fixes remaining issues]
→ Hook passes → Commit succeeds
→ MCP logs successful review
```

**Pattern: Skill Composition**

```
Complex task automatically triggers multiple skills:

User: "Build a secure REST API with tests and docs"

Activated skills:
1. api-design skill (structure endpoints)
2. security-scanner skill (review security)
3. test-generator skill (create tests)
4. api-docs-generator skill (generate docs)
5. verification skill (validate completeness)

Result: Comprehensive, quality-checked implementation
```

---

### 6. Success Patterns

**Characteristics of Successful Community Skills:**

1. **Clear, Specific Purpose**
   - Example: `test-driven-development` (not `testing-helper`)

2. **Excellent Description**
   - Includes natural trigger phrases
   - Specific about when to activate

3. **Well-Structured Instructions**
   - Phase-based or checklist format
   - Clear, imperative language
   - Progressive disclosure

4. **Appropriate Tool Restrictions**
   - Minimal permissions needed
   - Security-conscious

5. **Real-World Testing**
   - Used in actual projects
   - Refined based on feedback

6. **Good Documentation**
   - README explaining purpose
   - Examples of usage
   - Installation instructions

7. **Active Maintenance**
   - Responds to issues
   - Updates for new features
   - Community engagement

---

### 7. Anti-Patterns to Avoid

**❌ Vague Descriptions**
```yaml
description: "Helps with code"
# Claude won't know when to activate this!
```

**❌ Overly Broad Scope**
```yaml
name: database-everything
description: "Handles all database tasks"
# Too many responsibilities, unclear activation
```

**❌ Too Many Tools**
```yaml
allowed-tools: [Read, Write, Edit, Bash, WebFetch, WebSearch, Grep, Glob, ...]
# Grants unnecessary permissions
```

**❌ No Examples**
```markdown
## Process
1. Do the thing
2. Do the other thing
# What thing? How? No examples!
```

**❌ Everything in SKILL.md**
```markdown
[10,000 words of detailed instructions in SKILL.md]
# Should use references/ for details
```

**❌ Inconsistent Naming**
```
my_skill/     # Underscore
mySkill/      # CamelCase
MY-SKILL/     # All caps
# Use lowercase-with-hyphens
```

---

## Summary: Community Wisdom

### Top 10 Patterns from awesome-claude-skills

1. **Description is Everything**
   - Most important field for skill activation
   - Include natural trigger phrases
   - Be specific about when to activate

2. **Focus Beats Breadth**
   - One clear responsibility per skill
   - Multiple focused skills > one broad skill
   - Easier to activate, test, maintain

3. **Progressive Disclosure**
   - SKILL.md: lean instructions (~500 tokens)
   - references/: detailed documentation
   - assets/: templates and resources

4. **Tool Restriction = Security**
   - Use minimal tools needed
   - Analysis: Read, Grep, Glob only
   - Modification: Add Write, Edit cautiously
   - Review code before installation

5. **Systematic Workflows**
   - Phase-based approaches (research → implement → review → validate)
   - Checklist-based verification
   - Quality gates at each phase

6. **Automatic Activation**
   - Skills activate contextually
   - Multiple skills can stack
   - No manual combination needed

7. **Test in Real Scenarios**
   - Use in actual projects
   - Monitor activation accuracy
   - Refine based on feedback

8. **Community Distribution**
   - Personal → Team → Community evolution
   - Git for team sharing
   - Marketplace for wide distribution

9. **Meta-Circular Improvement**
   - Skills for creating skills
   - Skills for testing skills
   - Skills for sharing skills

10. **Integration Mindset**
    - Skills + Hooks + MCP work together
    - Composition over monoliths
    - Ecosystem thinking

---

## Resources

### Official
- **Claude Code Docs:** https://docs.claude.com/en/docs/claude-code/skills
- **Official Skills Repo:** https://github.com/anthropics/skills (15.9k stars)
- **Skills API:** `/v1/skills` endpoint

### Community
- **Awesome Claude Skills:** https://github.com/travisvn/awesome-claude-skills
- **Superpowers Library:** https://github.com/obra/superpowers
- **Claude Code GitHub:** https://github.com/anthropics/claude-code

### Installation
```bash
# Official skills
/plugin marketplace add anthropics/skills

# Community library
/plugin marketplace add obra/superpowers-marketplace
/plugin install superpowers@superpowers-marketplace

# Local development
/plugin add /path/to/skill

# Verify
/skills  # List all installed skills
/help    # See available commands
```

---

**Document Version:** 1.0
**Last Updated:** 2025-11-08
**Patterns Analyzed:** 40+ skills from official and community repositories
