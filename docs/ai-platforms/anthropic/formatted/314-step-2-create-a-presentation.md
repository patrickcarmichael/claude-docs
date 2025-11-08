---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Step 2: Create a presentation

Now we'll use the PowerPoint Skill to create a presentation about renewable energy. We specify Skills using the `container` parameter in the Messages API:
```python
  import anthropic

  client = anthropic.Anthropic()

  # Create a message with the PowerPoint Skill

  response = client.beta.messages.create(
      model="claude-sonnet-4-5-20250929",
      max_tokens=4096,
      betas=["code-execution-2025-08-25", "skills-2025-10-02"],
      container={
          "skills": [
              {
                  "type": "anthropic",
                  "skill_id": "pptx",
                  "version": "latest"
              }
          ]
      },
      messages=[{
          "role": "user",
          "content": "Create a presentation about renewable energy with 5 slides"
      }],
      tools=[{
          "type": "code_execution_20250825",
          "name": "code_execution"
      }]
  )

  print(response.content)
```
```typescript
  import Anthropic from '@anthropic-ai/sdk';

  const client = new Anthropic();

  // Create a message with the PowerPoint Skill
  const response = await client.beta.messages.create({
    model: 'claude-sonnet-4-5-20250929',
    max_tokens: 4096,
    betas: ['code-execution-2025-08-25', 'skills-2025-10-02'],
    container: {
      skills: [
        {
          type: 'anthropic',
          skill_id: 'pptx',
          version: 'latest'
        }
      ]
    },
    messages: [{
      role: 'user',
      content: 'Create a presentation about renewable energy with 5 slides'
    }],
    tools: [{
      type: 'code_execution_20250825',
      name: 'code_execution'
    }]
  });

  console.log(response.content);
```
```bash
  curl https://api.anthropic.com/v1/messages \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: code-execution-2025-08-25,skills-2025-10-02" \
    -H "content-type: application/json" \
    -d '{
      "model": "claude-sonnet-4-5-20250929",
      "max_tokens": 4096,
      "container": {
        "skills": [
          {
            "type": "anthropic",
            "skill_id": "pptx",
            "version": "latest"
          }
        ]
      },
      "messages": [{
        "role": "user",
        "content": "Create a presentation about renewable energy with 5 slides"
      }],
      "tools": [{
        "type": "code_execution_20250825",
        "name": "code_execution"
      }]
    }'
```

Let's break down what each part does:

* **`container.skills`**: Specifies which Skills Claude can use
* **`type: "anthropic"`**: Indicates this is an Anthropic-managed Skill
* **`skill_id: "pptx"`**: The PowerPoint Skill identifier
* **`version: "latest"`**: The Skill version set to the most recently published
* **`tools`**: Enables code execution (required for Skills)
* **Beta headers**: `code-execution-2025-08-25` and `skills-2025-10-02`

When you make this request, Claude automatically matches your task to the relevant Skill. Since you asked for a presentation, Claude determines the PowerPoint Skill is relevant and loads its full instructions: the second level of progressive disclosure. Then Claude executes the Skill's code to create your presentation.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
