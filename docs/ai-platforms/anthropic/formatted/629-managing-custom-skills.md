---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Managing Custom Skills

### Creating a Skill

Upload your custom Skill to make it available in your workspace. You can upload using either a directory path or individual file objects.
```python
  import anthropic

  client = anthropic.Anthropic()

  # Option 1: Using files_from_dir helper (Python only, recommended)

  from anthropic.lib import files_from_dir

  skill = client.beta.skills.create(
      display_title="Financial Analysis",
      files=files_from_dir("/path/to/financial_analysis_skill"),
      betas=["skills-2025-10-02"]
  )

  # Option 2: Using a zip file

  skill = client.beta.skills.create(
      display_title="Financial Analysis",
      files=[("skill.zip", open("financial_analysis_skill.zip", "rb"))],
      betas=["skills-2025-10-02"]
  )

  # Option 3: Using file tuples (filename, file_content, mime_type)

  skill = client.beta.skills.create(
      display_title="Financial Analysis",
      files=[
          ("financial_skill/SKILL.md", open("financial_skill/SKILL.md", "rb"), "text/markdown"),
          ("financial_skill/analyze.py", open("financial_skill/analyze.py", "rb"), "text/x-python"),
      ],
      betas=["skills-2025-10-02"]
  )

  print(f"Created skill: {skill.id}")
  print(f"Latest version: {skill.latest_version}")
```
```typescript
  import Anthropic, { toFile } from '@anthropic-ai/sdk';
  import fs from 'fs';

  const client = new Anthropic();

  // Option 1: Using a zip file
  const skill = await client.beta.skills.create({
    displayTitle: 'Financial Analysis',
    files: [
      await toFile(
        fs.createReadStream('financial_analysis_skill.zip'),
        'skill.zip'
      )
    ],
    betas: ['skills-2025-10-02']
  });

  // Option 2: Using individual file objects
  const skill = await client.beta.skills.create({
    displayTitle: 'Financial Analysis',
    files: [
      await toFile(
        fs.createReadStream('financial_skill/SKILL.md'),
        'financial_skill/SKILL.md',
        { type: 'text/markdown' }
      ),
      await toFile(
        fs.createReadStream('financial_skill/analyze.py'),
        'financial_skill/analyze.py',
        { type: 'text/x-python' }
      ),
    ],
    betas: ['skills-2025-10-02']
  });

  console.log(`Created skill: ${skill.id}`);
  console.log(`Latest version: ${skill.latest_version}`);
```
```bash
  curl -X POST "https://api.anthropic.com/v1/skills" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: skills-2025-10-02" \
    -F "display_title=Financial Analysis" \
    -F "files[]=@financial_skill/SKILL.md;filename=financial_skill/SKILL.md" \
    -F "files[]=@financial_skill/analyze.py;filename=financial_skill/analyze.py"
```

**Requirements:**

* Must include a SKILL.md file at the top level
* All files must specify a common root directory in their paths
* Total upload size must be under 8MB
* YAML frontmatter requirements:
  * `name`: Maximum 64 characters, lowercase letters/numbers/hyphens only, no XML tags, no reserved words ("anthropic", "claude")
  * `description`: Maximum 1024 characters, non-empty, no XML tags

For complete request/response schemas, see the [Create Skill API reference](/en/api/skills/create-skill).

### Listing Skills

Retrieve all Skills available to your workspace, including both Anthropic pre-built Skills and your custom Skills. Use the `source` parameter to filter by skill type:
```python
  # List all Skills

  skills = client.beta.skills.list(
      betas=["skills-2025-10-02"]
  )

  for skill in skills.data:
      print(f"{skill.id}: {skill.display_title} (source: {skill.source})")

  # List only custom Skills

  custom_skills = client.beta.skills.list(
      source="custom",
      betas=["skills-2025-10-02"]
  )
```
```typescript
  // List all Skills
  const skills = await client.beta.skills.list({
    betas: ['skills-2025-10-02']
  });

  for (const skill of skills.data) {
    console.log(`${skill.id}: ${skill.display_title} (source: ${skill.source})`);
  }

  // List only custom Skills
  const customSkills = await client.beta.skills.list({
    source: 'custom',
    betas: ['skills-2025-10-02']
  });
```
```bash
  # List all Skills

  curl "https://api.anthropic.com/v1/skills" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: skills-2025-10-02"

  # List only custom Skills

  curl "https://api.anthropic.com/v1/skills?source=custom" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: skills-2025-10-02"
```

See the [List Skills API reference](/en/api/skills/list-skills) for pagination and filtering options.

### Retrieving a Skill

Get details about a specific Skill:
```python
  skill = client.beta.skills.retrieve(
      skill_id="skill_01AbCdEfGhIjKlMnOpQrStUv",
      betas=["skills-2025-10-02"]
  )

  print(f"Skill: {skill.display_title}")
  print(f"Latest version: {skill.latest_version}")
  print(f"Created: {skill.created_at}")
```
```typescript
  const skill = await client.beta.skills.retrieve(
    'skill_01AbCdEfGhIjKlMnOpQrStUv',
    { betas: ['skills-2025-10-02'] }
  );

  console.log(`Skill: ${skill.display_title}`);
  console.log(`Latest version: ${skill.latest_version}`);
  console.log(`Created: ${skill.created_at}`);
```
```bash
  curl "https://api.anthropic.com/v1/skills/skill_01AbCdEfGhIjKlMnOpQrStUv" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: skills-2025-10-02"
```

### Deleting a Skill

To delete a Skill, you must first delete all its versions:
```python
  # Step 1: Delete all versions

  versions = client.beta.skills.versions.list(
      skill_id="skill_01AbCdEfGhIjKlMnOpQrStUv",
      betas=["skills-2025-10-02"]
  )

  for version in versions.data:
      client.beta.skills.versions.delete(
          skill_id="skill_01AbCdEfGhIjKlMnOpQrStUv",
          version=version.version,
          betas=["skills-2025-10-02"]
      )

  # Step 2: Delete the Skill

  client.beta.skills.delete(
      skill_id="skill_01AbCdEfGhIjKlMnOpQrStUv",
      betas=["skills-2025-10-02"]
  )
```
```typescript
  // Step 1: Delete all versions
  const versions = await client.beta.skills.versions.list(
    'skill_01AbCdEfGhIjKlMnOpQrStUv',
    { betas: ['skills-2025-10-02'] }
  );

  for (const version of versions.data) {
    await client.beta.skills.versions.delete(
      'skill_01AbCdEfGhIjKlMnOpQrStUv',
      version.version,
      { betas: ['skills-2025-10-02'] }
    );
  }

  // Step 2: Delete the Skill
  await client.beta.skills.delete(
    'skill_01AbCdEfGhIjKlMnOpQrStUv',
    { betas: ['skills-2025-10-02'] }
  );
```
```bash
  # Delete all versions first, then delete the Skill

  curl -X DELETE "https://api.anthropic.com/v1/skills/skill_01AbCdEfGhIjKlMnOpQrStUv" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: skills-2025-10-02"
```

Attempting to delete a Skill with existing versions will return a 400 error.

### Versioning

Skills support versioning to manage updates safely:

**Anthropic-Managed Skills**:

* Versions use date format: `20251013`
* New versions released as updates are made
* Specify exact versions for stability

**Custom Skills**:

* Auto-generated epoch timestamps: `1759178010641129`
* Use `"latest"` to always get the most recent version
* Create new versions when updating Skill files
```python
  # Create a new version

  from anthropic.lib import files_from_dir

  new_version = client.beta.skills.versions.create(
      skill_id="skill_01AbCdEfGhIjKlMnOpQrStUv",
      files=files_from_dir("/path/to/updated_skill"),
      betas=["skills-2025-10-02"]
  )

  # Use specific version

  response = client.beta.messages.create(
      model="claude-sonnet-4-5-20250929",
      max_tokens=4096,
      betas=["code-execution-2025-08-25", "skills-2025-10-02"],
      container={
          "skills": [{
              "type": "custom",
              "skill_id": "skill_01AbCdEfGhIjKlMnOpQrStUv",
              "version": new_version.version
          }]
      },
      messages=[{"role": "user", "content": "Use updated Skill"}],
      tools=[{"type": "code_execution_20250825", "name": "code_execution"}]
  )

  # Use latest version

  response = client.beta.messages.create(
      model="claude-sonnet-4-5-20250929",
      max_tokens=4096,
      betas=["code-execution-2025-08-25", "skills-2025-10-02"],
      container={
          "skills": [{
              "type": "custom",
              "skill_id": "skill_01AbCdEfGhIjKlMnOpQrStUv",
              "version": "latest"
          }]
      },
      messages=[{"role": "user", "content": "Use latest Skill version"}],
      tools=[{"type": "code_execution_20250825", "name": "code_execution"}]
  )
```
```typescript
  // Create a new version using a zip file
  const fs = require('fs');

  const newVersion = await client.beta.skills.versions.create(
    'skill_01AbCdEfGhIjKlMnOpQrStUv',
    {
      files: [
        fs.createReadStream('updated_skill.zip')
      ],
      betas: ['skills-2025-10-02']
    }
  );

  // Use specific version
  const response = await client.beta.messages.create({
    model: 'claude-sonnet-4-5-20250929',
    max_tokens: 4096,
    betas: ['code-execution-2025-08-25', 'skills-2025-10-02'],
    container: {
      skills: [{
        type: 'custom',
        skill_id: 'skill_01AbCdEfGhIjKlMnOpQrStUv',
        version: newVersion.version
      }]
    },
    messages: [{role: 'user', content: 'Use updated Skill'}],
    tools: [{type: 'code_execution_20250825', name: 'code_execution'}]
  });

  // Use latest version
  const response = await client.beta.messages.create({
    model: 'claude-sonnet-4-5-20250929',
    max_tokens: 4096,
    betas: ['code-execution-2025-08-25', 'skills-2025-10-02'],
    container: {
      skills: [{
        type: 'custom',
        skill_id: 'skill_01AbCdEfGhIjKlMnOpQrStUv',
        version: 'latest'
      }]
    },
    messages: [{role: 'user', content: 'Use latest Skill version'}],
    tools: [{type: 'code_execution_20250825', name: 'code_execution'}]
  });
```
```bash
  # Create a new version

  NEW_VERSION=$(curl -X POST "https://api.anthropic.com/v1/skills/skill_01AbCdEfGhIjKlMnOpQrStUv/versions" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: skills-2025-10-02" \
    -F "files[]=@updated_skill/SKILL.md;filename=updated_skill/SKILL.md")

  VERSION_NUMBER=$(echo "$NEW_VERSION" | jq -r '.version')

  # Use specific version

  curl https://api.anthropic.com/v1/messages \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: code-execution-2025-08-25,skills-2025-10-02" \
    -H "content-type: application/json" \
    -d "{
      \"model\": \"claude-sonnet-4-5-20250929\",
      \"max_tokens\": 4096,
      \"container\": {
        \"skills\": [{
          \"type\": \"custom\",
          \"skill_id\": \"skill_01AbCdEfGhIjKlMnOpQrStUv\",
          \"version\": \"$VERSION_NUMBER\"
        }]
      },
      \"messages\": [{\"role\": \"user\", \"content\": \"Use updated Skill\"}],
      \"tools\": [{\"type\": \"code_execution_20250825\", \"name\": \"code_execution\"}]
    }"

  # Use latest version

  curl https://api.anthropic.com/v1/messages \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: code-execution-2025-08-25,skills-2025-10-02" \
    -H "content-type: application/json" \
    -d '{
      "model": "claude-sonnet-4-5-20250929",
      "max_tokens": 4096,
      "container": {
        "skills": [{
          "type": "custom",
          "skill_id": "skill_01AbCdEfGhIjKlMnOpQrStUv",
          "version": "latest"
        }]
      },
      "messages": [{"role": "user", "content": "Use latest Skill version"}],
      "tools": [{"type": "code_execution_20250825", "name": "code_execution"}]
    }'
```

See the [Create Skill Version API reference](/en/api/skills/create-skill-version) for complete details.

***

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
