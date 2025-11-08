---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Use latest for active development

container={
    "skills": [{
        "type": "custom",
        "skill_id": "skill_01AbCdEfGhIjKlMnOpQrStUv",
        "version": "latest"  # Always get newest

    }]
}
```

### Prompt Caching Considerations

When using prompt caching, note that changing the Skills list in your container will break the cache:
```python
  # First request creates cache

  response1 = client.beta.messages.create(
      model="claude-sonnet-4-5-20250929",
      max_tokens=4096,
      betas=["code-execution-2025-08-25", "skills-2025-10-02", "prompt-caching-2024-07-31"],
      container={
          "skills": [
              {"type": "anthropic", "skill_id": "xlsx", "version": "latest"}
          ]
      },
      messages=[{"role": "user", "content": "Analyze sales data"}],
      tools=[{"type": "code_execution_20250825", "name": "code_execution"}]
  )

  # Adding/removing Skills breaks cache

  response2 = client.beta.messages.create(
      model="claude-sonnet-4-5-20250929",
      max_tokens=4096,
      betas=["code-execution-2025-08-25", "skills-2025-10-02", "prompt-caching-2024-07-31"],
      container={
          "skills": [
              {"type": "anthropic", "skill_id": "xlsx", "version": "latest"},
              {"type": "anthropic", "skill_id": "pptx", "version": "latest"}  # Cache miss

          ]
      },
      messages=[{"role": "user", "content": "Create a presentation"}],
      tools=[{"type": "code_execution_20250825", "name": "code_execution"}]
  )
```
```typescript
  // First request creates cache
  const response1 = await client.beta.messages.create({
    model: 'claude-sonnet-4-5-20250929',
    max_tokens: 4096,
    betas: ['code-execution-2025-08-25', 'skills-2025-10-02', 'prompt-caching-2024-07-31'],
    container: {
      skills: [
        {type: 'anthropic', skill_id: 'xlsx', version: 'latest'}
      ]
    },
    messages: [{role: 'user', content: 'Analyze sales data'}],
    tools: [{type: 'code_execution_20250825', name: 'code_execution'}]
  });

  // Adding/removing Skills breaks cache
  const response2 = await client.beta.messages.create({
    model: 'claude-sonnet-4-5-20250929',
    max_tokens: 4096,
    betas: ['code-execution-2025-08-25', 'skills-2025-10-02', 'prompt-caching-2024-07-31'],
    container: {
      skills: [
        {type: 'anthropic', skill_id: 'xlsx', version: 'latest'},
        {type: 'anthropic', skill_id: 'pptx', version: 'latest'}  // Cache miss
      ]
    },
    messages: [{role: 'user', content: 'Create a presentation'}],
    tools: [{type: 'code_execution_20250825', name: 'code_execution'}]
  });
```
```bash
  # First request creates cache

  curl https://api.anthropic.com/v1/messages \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: code-execution-2025-08-25,skills-2025-10-02,prompt-caching-2024-07-31" \
    -H "content-type: application/json" \
    -d '{
      "model": "claude-sonnet-4-5-20250929",
      "max_tokens": 4096,
      "container": {
        "skills": [
          {"type": "anthropic", "skill_id": "xlsx", "version": "latest"}
        ]
      },
      "messages": [{"role": "user", "content": "Analyze sales data"}],
      "tools": [{"type": "code_execution_20250825", "name": "code_execution"}]
    }'

  # Adding/removing Skills breaks cache

  curl https://api.anthropic.com/v1/messages \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: code-execution-2025-08-25,skills-2025-10-02,prompt-caching-2024-07-31" \
    -H "content-type: application/json" \
    -d '{
      "model": "claude-sonnet-4-5-20250929",
      "max_tokens": 4096,
      "container": {
        "skills": [
          {"type": "anthropic", "skill_id": "xlsx", "version": "latest"},
          {"type": "anthropic", "skill_id": "pptx", "version": "latest"}
        ]
      },
      "messages": [{"role": "user", "content": "Create a presentation"}],
      "tools": [{"type": "code_execution_20250825", "name": "code_execution"}]
    }'
```

For best caching performance, keep your Skills list consistent across requests.

### Error Handling

Handle Skill-related errors gracefully:
```python
  try:
      response = client.beta.messages.create(
          model="claude-sonnet-4-5-20250929",
          max_tokens=4096,
          betas=["code-execution-2025-08-25", "skills-2025-10-02"],
          container={
              "skills": [
                  {"type": "custom", "skill_id": "skill_01AbCdEfGhIjKlMnOpQrStUv", "version": "latest"}
              ]
          },
          messages=[{"role": "user", "content": "Process data"}],
          tools=[{"type": "code_execution_20250825", "name": "code_execution"}]
      )
  except anthropic.BadRequestError as e:
      if "skill" in str(e):
          print(f"Skill error: {e}")
          # Handle skill-specific errors

      else:
          raise
```
```typescript
  try {
    const response = await client.beta.messages.create({
      model: 'claude-sonnet-4-5-20250929',
      max_tokens: 4096,
      betas: ['code-execution-2025-08-25', 'skills-2025-10-02'],
      container: {
        skills: [
          {type: 'custom', skill_id: 'skill_01AbCdEfGhIjKlMnOpQrStUv', version: 'latest'}
        ]
      },
      messages: [{role: 'user', content: 'Process data'}],
      tools: [{type: 'code_execution_20250825', name: 'code_execution'}]
    });
  } catch (error) {
    if (error instanceof Anthropic.BadRequestError && error.message.includes('skill')) {
      console.error(`Skill error: ${error.message}`);
      // Handle skill-specific errors
    } else {
      throw error;
    }
  }
```

***

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
