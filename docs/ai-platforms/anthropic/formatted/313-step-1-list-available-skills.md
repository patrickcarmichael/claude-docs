---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Step 1: List available Skills

First, let's see what Skills are available. We'll use the Skills API to list all Anthropic-managed Skills:
```python
  import anthropic

  client = anthropic.Anthropic()

  # List Anthropic-managed Skills

  skills = client.beta.skills.list(
      source="anthropic",
      betas=["skills-2025-10-02"]
  )

  for skill in skills.data:
      print(f"{skill.id}: {skill.display_title}")
```
```typescript
  import Anthropic from '@anthropic-ai/sdk';

  const client = new Anthropic();

  // List Anthropic-managed Skills
  const skills = await client.beta.skills.list({
    source: 'anthropic',
    betas: ['skills-2025-10-02']
  });

  for (const skill of skills.data) {
    console.log(`${skill.id}: ${skill.display_title}`);
  }
```
```bash
  curl "https://api.anthropic.com/v1/skills?source=anthropic" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: skills-2025-10-02"
```

You see the following Skills: `pptx`, `xlsx`, `docx`, and `pdf`.

This API returns each Skill's metadata: its name and description. Claude loads this metadata at startup to know what Skills are available. This is the first level of **progressive disclosure**, where Claude discovers Skills without loading their full instructions yet.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
