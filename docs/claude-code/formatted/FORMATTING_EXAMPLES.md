# Formatting Examples - Before & After

This document shows specific examples of formatting improvements made to the Claude Code documentation.

## 1. YAML Front Matter

### Before (Chunked Version)
```markdown
# Getting Started

**Navigation:** [Index](./index.md) | [Next: Features →](./02-features.md)

> **Note:** This is part of the chunked llms-full.txt. For organized topic documentation, see [../README.md](../README.md)

---

# Claude Code overview
```

### After (Formatted Version)
```markdown
---
title: "Getting Started"
description: "Introduction, quickstart, and installation guide"
weight: 1
---

# Getting Started

# Claude Code overview
```

**Improvement:** Clean YAML metadata at the top, no redundant navigation headers.

---

## 2. Special Tags → Markdown

### Before
```html
<Tip>
  See advanced setup for installation options or troubleshooting if you hit issues.
</Tip>
```

### After
```markdown
> **💡 Tip:** See advanced setup for installation options or troubleshooting if you hit issues.
```

### Before
```html
<Warning>
  Do NOT use `sudo npm install -g` as this can lead to permission issues.
</Warning>
```

### After
```markdown
> **⚠️ Warning:** Do NOT use `sudo npm install -g` as this can lead to permission issues.
```

### Before
```html
<Note>
  When you first authenticate Claude Code with your Claude Console account, a workspace called "Claude Code" is automatically created for you.
</Note>
```

### After
```markdown
> **Note:** When you first authenticate Claude Code with your Claude Console account, a workspace called "Claude Code" is automatically created for you.
```

**Improvement:** Standard markdown blockquotes with emoji icons for visual distinction.

---

## 3. Code Blocks

### Before
```markdown
```bash  theme={null}
    curl -fsSL https://claude.ai/install.sh | bash
    ```
```

### After
```markdown
```bash
curl -fsSL https://claude.ai/install.sh | bash
`` `
```

**Improvement:** Removed theme attributes, preserved content, clean formatting.

---

## 4. Tabs → Labeled Sections

### Before
```html
<Tabs>
  <Tab title="macOS/Linux">
    ```bash  theme={null}
    curl -fsSL https://claude.ai/install.sh | bash
    ```
  </Tab>

  <Tab title="Homebrew">
    ```bash  theme={null}
    brew install --cask claude-code
    ```
  </Tab>

  <Tab title="Windows">
    ```powershell  theme={null}
    irm https://claude.ai/install.ps1 | iex
    ```
  </Tab>

  <Tab title="NPM">
    ```bash  theme={null}
    npm install -g @anthropic-ai/claude-code
    ```

    Requires [Node.js 18+](https://nodejs.org/en/download/)
  </Tab>
</Tabs>
```

### After
```markdown
**macOS/Linux:**

```bash
curl -fsSL https://claude.ai/install.sh | bash
`` `

**Homebrew:**

```bash
brew install --cask claude-code
`` `

**Windows:**

```powershell
irm https://claude.ai/install.ps1 | iex
`` `

**NPM:**

```bash
npm install -g @anthropic-ai/claude-code
`` `

Requires [Node.js 18+](https://nodejs.org/en/download/)
```

**Improvement:** Clean section headers with proper code blocks, no HTML.

---

## 5. Cards → Markdown Links

### Before
```html
<CardGroup>
  <Card title="Quickstart" icon="rocket" href="/en/quickstart">
    See Claude Code in action with practical examples
  </Card>

  <Card title="Common workflows" icon="graduation-cap" href="/en/common-workflows">
    Step-by-step guides for common workflows
  </Card>

  <Card title="Troubleshooting" icon="wrench" href="/en/troubleshooting">
    Solutions for common issues with Claude Code
  </Card>
</CardGroup>
```

### After
```markdown
- **[Quickstart](/en/quickstart)**
  See Claude Code in action with practical examples

- **[Common workflows](/en/common-workflows)**
  Step-by-step guides for common workflows

- **[Troubleshooting](/en/troubleshooting)**
  Solutions for common issues with Claude Code
```

**Improvement:** Standard markdown lists with links and descriptions.

---

## 6. Accordions → Sections

### Before
```html
<AccordionGroup>
  <Accordion title="Be specific with your requests">
    Instead of: "fix the bug"

    Try: "fix the login bug where users see a blank screen after entering wrong credentials"
  </Accordion>

  <Accordion title="Use step-by-step instructions">
    Break complex tasks into steps:

    ```
    > 1. create a new database table for user profiles
    > 2. create an API endpoint to get and update user profiles
    > 3. build a webpage that allows users to see and edit their information
    ```
  </Accordion>
</AccordionGroup>
```

### After
```markdown
**Be specific with your requests**

Instead of: "fix the bug"

Try: "fix the login bug where users see a blank screen after entering wrong credentials"

**Use step-by-step instructions**

Break complex tasks into steps:

`` `
> 1. create a new database table for user profiles
> 2. create an API endpoint to get and update user profiles
> 3. build a webpage that allows users to see and edit their information
`` `
```

**Improvement:** Clean sections with bold headings, no HTML.

---

## 7. Navigation

### Before (Top of File)
```markdown
# Features

**Navigation:** [← Previous: Getting Started](./01-getting-started.md) | [Index](./index.md) | [Next: Configuration →](./03-configuration.md)

> **Note:** This is part of the chunked llms-full.txt. For organized topic documentation, see [../README.md](../README.md)

---

# Checkpointing
```

### Before (Bottom of File)
```markdown
* Editing: `x`, `dw`/`de`/`db`/`dd`/`D`, `cw`/`ce`/`cb`/`cc`/`C`, `.` (repeat)


---

**Navigation:** [← Previous: Getting Started](./01-getting-started.md) | [Index](./index.md) | [Next: Configuration →](./03-configuration.md)
```

### After (Top of File)
```markdown
---
title: "Features"
description: "Core features and capabilities"
weight: 2
---

# Features

# Checkpointing
```

### After (Bottom of File)
```markdown
* Editing: `x`, `dw`/`de`/`db`/`dd`/`D`, `cw`/`ce`/`cb`/`cc`/`C`, `.` (repeat)

---

[← Previous: Getting Started](./01-getting-started.md) | [📑 Index](./index.md) | [Next: Configuration →](./03-configuration.md)
```

**Improvement:**
- Top: Clean YAML instead of navigation headers
- Bottom: Simplified footer with emoji icon for index
- Removed redundant note about chunked version

---

## 8. Table Formatting

### Before & After (No Change Needed)
Tables were already well-formatted in the source:

```markdown
| Command             | What it does                      | Example                             |
| ------------------- | --------------------------------- | ----------------------------------- |
| `claude`            | Start interactive mode            | `claude`                            |
| `claude "task"`     | Run a one-time task               | `claude "fix the build error"`      |
| `claude -p "query"` | Run one-off query, then exit      | `claude -p "explain this function"` |
```

**Improvement:** Preserved existing clean table formatting.

---

## 9. Code Block Language Identifiers

### Before
```markdown
```bash  theme={null}
# Install stable version (default)
curl -fsSL https://claude.ai/install.sh | bash

# Install latest version
curl -fsSL https://claude.ai/install.sh | bash -s latest
`` `
```

### After
```markdown
```bash
# Install stable version (default)
curl -fsSL https://claude.ai/install.sh | bash

# Install latest version
curl -fsSL https://claude.ai/install.sh | bash -s latest
`` `
```

**Languages Identified:**
- `bash` - Shell scripts
- `powershell` - Windows PowerShell
- `python` - Python code
- `yaml` - YAML configuration
- `json` - JSON data
- `javascript` - JavaScript code
- `typescript` - TypeScript code
- `batch` - Windows batch files

**Improvement:** Clean language identifiers for syntax highlighting.

---

## Summary of Improvements

| Feature | Before | After |
|---------|--------|-------|
| **Metadata** | None | YAML front matter |
| **Callouts** | `<Note>`, `<Tip>`, `<Warning>` | `> **Note:**`, `> **💡 Tip:**`, `> **⚠️ Warning:**` |
| **Tabs** | `<Tabs>`, `<Tab>` | `**Label:**` sections |
| **Cards** | `<Card>`, `<CardGroup>` | Markdown lists with links |
| **Accordions** | `<Accordion>` | Bold section headers |
| **Code Blocks** | ` ```lang theme={null} ` | ` ```lang ` |
| **Navigation** | Header + footer | YAML + clean footer |
| **Spacing** | Variable | Consistent |

---

**All formatting improvements maintain:**
- ✅ Complete content preservation
- ✅ Valid markdown syntax
- ✅ Wide compatibility
- ✅ Better readability
- ✅ SEO optimization
- ✅ AI-friendly structure
