---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Use Cases

### Organizational Skills

**Brand & Communications**

* Apply company-specific formatting (colors, fonts, layouts) to documents
* Generate communications following organizational templates
* Ensure consistent brand guidelines across all outputs

**Project Management**

* Structure notes with company-specific formats (OKRs, decision logs)
* Generate tasks following team conventions
* Create standardized meeting recaps and status updates

**Business Operations**

* Create company-standard reports, proposals, and analyses
* Execute company-specific analytical procedures
* Generate financial models following organizational templates

### Personal Skills

**Content Creation**

* Custom document templates
* Specialized formatting and styling
* Domain-specific content generation

**Data Analysis**

* Custom data processing pipelines
* Specialized visualization templates
* Industry-specific analytical methods

**Development & Automation**

* Code generation templates
* Testing frameworks
* Deployment workflows

### Example: Financial Modeling

Combine Excel and custom DCF analysis Skills:
```python
  # Create custom DCF analysis Skill

  from anthropic.lib import files_from_dir

  dcf_skill = client.beta.skills.create(
      display_title="DCF Analysis",
      files=files_from_dir("/path/to/dcf_skill"),
      betas=["skills-2025-10-02"]
  )

  # Use with Excel to create financial model

  response = client.beta.messages.create(
      model="claude-sonnet-4-5-20250929",
      max_tokens=4096,
      betas=["code-execution-2025-08-25", "skills-2025-10-02"],
      container={
          "skills": [
              {"type": "anthropic", "skill_id": "xlsx", "version": "latest"},
              {"type": "custom", "skill_id": dcf_skill.id, "version": "latest"}
          ]
      },
      messages=[{
          "role": "user",
          "content": "Build a DCF valuation model for a SaaS company with the attached financials"
      }],
      tools=[{"type": "code_execution_20250825", "name": "code_execution"}]
  )
```
```typescript
  // Create custom DCF analysis Skill
  import { toFile } from '@anthropic-ai/sdk';
  import fs from 'fs';

  const dcfSkill = await client.beta.skills.create({
    displayTitle: 'DCF Analysis',
    files: [
      await toFile(fs.createReadStream('dcf_skill.zip'), 'skill.zip')
    ],
    betas: ['skills-2025-10-02']
  });

  // Use with Excel to create financial model
  const response = await client.beta.messages.create({
    model: 'claude-sonnet-4-5-20250929',
    max_tokens: 4096,
    betas: ['code-execution-2025-08-25', 'skills-2025-10-02'],
    container: {
      skills: [
        {type: 'anthropic', skill_id: 'xlsx', version: 'latest'},
        {type: 'custom', skill_id: dcfSkill.id, version: 'latest'}
      ]
    },
    messages: [{
      role: 'user',
      content: 'Build a DCF valuation model for a SaaS company with the attached financials'
    }],
    tools: [{type: 'code_execution_20250825', name: 'code_execution'}]
  });
```
```bash
  # Create custom DCF analysis Skill

  DCF_SKILL=$(curl -X POST "https://api.anthropic.com/v1/skills" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: skills-2025-10-02" \
    -F "display_title=DCF Analysis" \
    -F "files[]=@dcf_skill/SKILL.md;filename=dcf_skill/SKILL.md")

  DCF_SKILL_ID=$(echo "$DCF_SKILL" | jq -r '.id')

  # Use with Excel to create financial model

  curl https://api.anthropic.com/v1/messages \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: code-execution-2025-08-25,skills-2025-10-02" \
    -H "content-type: application/json" \
    -d "{
      \"model\": \"claude-sonnet-4-5-20250929\",
      \"max_tokens\": 4096,
      \"container\": {
        \"skills\": [
          {
            \"type\": \"anthropic\",
            \"skill_id\": \"xlsx\",
            \"version\": \"latest\"
          },
          {
            \"type\": \"custom\",
            \"skill_id\": \"$DCF_SKILL_ID\",
            \"version\": \"latest\"
          }
        ]
      },
      \"messages\": [{
        \"role\": \"user\",
        \"content\": \"Build a DCF valuation model for a SaaS company with the attached financials\"
      }],
      \"tools\": [{
        \"type\": \"code_execution_20250825\",
        \"name\": \"code_execution\"
      }]
    }"
```typescript

***

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
