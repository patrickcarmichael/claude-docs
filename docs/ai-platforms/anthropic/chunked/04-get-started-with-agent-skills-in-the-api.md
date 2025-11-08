**Navigation:** [← Previous](./03-streaming-input.md) | [Index](./index.md) | [Next →](./05-how-to-implement-tool-use.md)

---

# Get started with Agent Skills in the API
Source: https://docs.claude.com/en/docs/agents-and-tools/agent-skills/quickstart

Learn how to use Agent Skills to create documents with the Claude API in under 10 minutes.

This tutorial shows you how to use Agent Skills to create a PowerPoint presentation. You'll learn how to enable Skills, make a simple request, and access the generated file.

## Prerequisites

* [Anthropic API key](https://console.anthropic.com/settings/keys)
* Python 3.7+ or curl installed
* Basic familiarity with making API requests

## What are Agent Skills?

Pre-built Agent Skills extend Claude's capabilities with specialized expertise for tasks like creating documents, analyzing data, and processing files. Anthropic provides the following pre-built Agent Skills in the API:

* **PowerPoint (pptx)**: Create and edit presentations
* **Excel (xlsx)**: Create and analyze spreadsheets
* **Word (docx)**: Create and edit documents
* **PDF (pdf)**: Generate PDF documents

<Note>
  **Want to create custom Skills?** See the [Agent Skills Cookbook](https://github.com/anthropics/claude-cookbooks/tree/main/skills) for examples of building your own Skills with domain-specific expertise.
</Note>

## Step 1: List available Skills

First, let's see what Skills are available. We'll use the Skills API to list all Anthropic-managed Skills:

<CodeGroup>
  ```python Python theme={null}
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

  ```typescript TypeScript theme={null}
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

  ```bash Shell theme={null}
  curl "https://api.anthropic.com/v1/skills?source=anthropic" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: skills-2025-10-02"
  ```
</CodeGroup>

You see the following Skills: `pptx`, `xlsx`, `docx`, and `pdf`.

This API returns each Skill's metadata: its name and description. Claude loads this metadata at startup to know what Skills are available. This is the first level of **progressive disclosure**, where Claude discovers Skills without loading their full instructions yet.

## Step 2: Create a presentation

Now we'll use the PowerPoint Skill to create a presentation about renewable energy. We specify Skills using the `container` parameter in the Messages API:

<CodeGroup>
  ```python Python theme={null}
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

  ```typescript TypeScript theme={null}
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

  ```bash Shell theme={null}
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
</CodeGroup>

Let's break down what each part does:

* **`container.skills`**: Specifies which Skills Claude can use
* **`type: "anthropic"`**: Indicates this is an Anthropic-managed Skill
* **`skill_id: "pptx"`**: The PowerPoint Skill identifier
* **`version: "latest"`**: The Skill version set to the most recently published
* **`tools`**: Enables code execution (required for Skills)
* **Beta headers**: `code-execution-2025-08-25` and `skills-2025-10-02`

When you make this request, Claude automatically matches your task to the relevant Skill. Since you asked for a presentation, Claude determines the PowerPoint Skill is relevant and loads its full instructions: the second level of progressive disclosure. Then Claude executes the Skill's code to create your presentation.

## Step 3: Download the created file

The presentation was created in the code execution container and saved as a file. The response includes a file reference with a file ID. Extract the file ID and download it using the Files API:

<CodeGroup>
  ```python Python theme={null}
  # Extract file ID from response
  file_id = None
  for block in response.content:
      if block.type == 'tool_use' and block.name == 'code_execution':
          # File ID is in the tool result
          for result_block in block.content:
              if hasattr(result_block, 'file_id'):
                  file_id = result_block.file_id
                  break

  if file_id:
      # Download the file
      file_content = client.beta.files.download(
          file_id=file_id,
          betas=["files-api-2025-04-14"]
      )

      # Save to disk
      with open("renewable_energy.pptx", "wb") as f:
          file_content.write_to_file(f.name)

      print(f"Presentation saved to renewable_energy.pptx")
  ```

  ```typescript TypeScript theme={null}
  // Extract file ID from response
  let fileId: string | null = null;
  for (const block of response.content) {
    if (block.type === 'tool_use' && block.name === 'code_execution') {
      // File ID is in the tool result
      for (const resultBlock of block.content) {
        if ('file_id' in resultBlock) {
          fileId = resultBlock.file_id;
          break;
        }
      }
    }
  }

  if (fileId) {
    // Download the file
    const fileContent = await client.beta.files.download(fileId, {
      betas: ['files-api-2025-04-14']
    });

    // Save to disk
    const fs = require('fs');
    fs.writeFileSync('renewable_energy.pptx', Buffer.from(await fileContent.arrayBuffer()));

    console.log('Presentation saved to renewable_energy.pptx');
  }
  ```

  ```bash Shell theme={null}
  # Extract file_id from response (using jq)
  FILE_ID=$(echo "$RESPONSE" | jq -r '.content[] | select(.type=="tool_use" and .name=="code_execution") | .content[] | select(.file_id) | .file_id')

  # Download the file
  curl "https://api.anthropic.com/v1/files/$FILE_ID/content" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: files-api-2025-04-14" \
    --output renewable_energy.pptx

  echo "Presentation saved to renewable_energy.pptx"
  ```
</CodeGroup>

<Note>
  For complete details on working with generated files, see the [code execution tool documentation](/en/docs/agents-and-tools/tool-use/code-execution-tool#retrieve-generated-files).
</Note>

## Try more examples

Now that you've created your first document with Skills, try these variations:

### Create a spreadsheet

<CodeGroup>
  ```python Python theme={null}
  response = client.beta.messages.create(
      model="claude-sonnet-4-5-20250929",
      max_tokens=4096,
      betas=["code-execution-2025-08-25", "skills-2025-10-02"],
      container={
          "skills": [
              {
                  "type": "anthropic",
                  "skill_id": "xlsx",
                  "version": "latest"
              }
          ]
      },
      messages=[{
          "role": "user",
          "content": "Create a quarterly sales tracking spreadsheet with sample data"
      }],
      tools=[{
          "type": "code_execution_20250825",
          "name": "code_execution"
      }]
  )
  ```

  ```typescript TypeScript theme={null}
  const response = await client.beta.messages.create({
    model: 'claude-sonnet-4-5-20250929',
    max_tokens: 4096,
    betas: ['code-execution-2025-08-25', 'skills-2025-10-02'],
    container: {
      skills: [
        {
          type: 'anthropic',
          skill_id: 'xlsx',
          version: 'latest'
        }
      ]
    },
    messages: [{
      role: 'user',
      content: 'Create a quarterly sales tracking spreadsheet with sample data'
    }],
    tools: [{
      type: 'code_execution_20250825',
      name: 'code_execution'
    }]
  });
  ```

  ```bash Shell theme={null}
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
            "skill_id": "xlsx",
            "version": "latest"
          }
        ]
      },
      "messages": [{
        "role": "user",
        "content": "Create a quarterly sales tracking spreadsheet with sample data"
      }],
      "tools": [{
        "type": "code_execution_20250825",
        "name": "code_execution"
      }]
    }'
  ```
</CodeGroup>

### Create a Word document

<CodeGroup>
  ```python Python theme={null}
  response = client.beta.messages.create(
      model="claude-sonnet-4-5-20250929",
      max_tokens=4096,
      betas=["code-execution-2025-08-25", "skills-2025-10-02"],
      container={
          "skills": [
              {
                  "type": "anthropic",
                  "skill_id": "docx",
                  "version": "latest"
              }
          ]
      },
      messages=[{
          "role": "user",
          "content": "Write a 2-page report on the benefits of renewable energy"
      }],
      tools=[{
          "type": "code_execution_20250825",
          "name": "code_execution"
      }]
  )
  ```

  ```typescript TypeScript theme={null}
  const response = await client.beta.messages.create({
    model: 'claude-sonnet-4-5-20250929',
    max_tokens: 4096,
    betas: ['code-execution-2025-08-25', 'skills-2025-10-02'],
    container: {
      skills: [
        {
          type: 'anthropic',
          skill_id: 'docx',
          version: 'latest'
        }
      ]
    },
    messages: [{
      role: 'user',
      content: 'Write a 2-page report on the benefits of renewable energy'
    }],
    tools: [{
      type: 'code_execution_20250825',
      name: 'code_execution'
    }]
  });
  ```

  ```bash Shell theme={null}
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
            "skill_id": "docx",
            "version": "latest"
          }
        ]
      },
      "messages": [{
        "role": "user",
        "content": "Write a 2-page report on the benefits of renewable energy"
      }],
      "tools": [{
        "type": "code_execution_20250825",
        "name": "code_execution"
      }]
    }'
  ```
</CodeGroup>

### Generate a PDF

<CodeGroup>
  ```python Python theme={null}
  response = client.beta.messages.create(
      model="claude-sonnet-4-5-20250929",
      max_tokens=4096,
      betas=["code-execution-2025-08-25", "skills-2025-10-02"],
      container={
          "skills": [
              {
                  "type": "anthropic",
                  "skill_id": "pdf",
                  "version": "latest"
              }
          ]
      },
      messages=[{
          "role": "user",
          "content": "Generate a PDF invoice template"
      }],
      tools=[{
          "type": "code_execution_20250825",
          "name": "code_execution"
      }]
  )
  ```

  ```typescript TypeScript theme={null}
  const response = await client.beta.messages.create({
    model: 'claude-sonnet-4-5-20250929',
    max_tokens: 4096,
    betas: ['code-execution-2025-08-25', 'skills-2025-10-02'],
    container: {
      skills: [
        {
          type: 'anthropic',
          skill_id: 'pdf',
          version: 'latest'
        }
      ]
    },
    messages: [{
      role: 'user',
      content: 'Generate a PDF invoice template'
    }],
    tools: [{
      type: 'code_execution_20250825',
      name: 'code_execution'
    }]
  });
  ```

  ```bash Shell theme={null}
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
            "skill_id": "pdf",
            "version": "latest"
          }
        ]
      },
      "messages": [{
        "role": "user",
        "content": "Generate a PDF invoice template"
      }],
      "tools": [{
        "type": "code_execution_20250825",
        "name": "code_execution"
      }]
    }'
  ```
</CodeGroup>

## Next steps

Now that you've used pre-built Agent Skills, you can:

<CardGroup cols={2}>
  <Card title="API Guide" icon="book" href="/en/docs/build-with-claude/skills-guide">
    Use Skills with the Claude API
  </Card>

  <Card title="Create Custom Skills" icon="code" href="/en/api/skills/create-skill">
    Upload your own Skills for specialized tasks
  </Card>

  <Card title="Authoring Guide" icon="pen" href="/en/docs/agents-and-tools/agent-skills/best-practices">
    Learn best practices for writing effective Skills
  </Card>

  <Card title="Use Skills in Claude Code" icon="terminal" href="https://code.claude.com/docs/skills">
    Learn about Skills in Claude Code
  </Card>

  <Card title="Use Skills in the Agent SDK" icon="cube" href="/en/docs/agent-sdk/skills">
    Use Skills programmatically in TypeScript and Python
  </Card>

  <Card title="Agent Skills Cookbook" icon="book-open" href="https://github.com/anthropics/anthropic-cookbook/blob/main/skills/README.md">
    Explore example Skills and implementation patterns
  </Card>
</CardGroup>


# Google Sheets add-on
Source: https://docs.claude.com/en/docs/agents-and-tools/claude-for-sheets

The [Claude for Sheets extension](https://workspace.google.com/marketplace/app/claude%5Ffor%5Fsheets/909417792257) integrates Claude into Google Sheets, allowing you to execute interactions with Claude directly in cells.

## Why use Claude for Sheets?

Claude for Sheets enables prompt engineering at scale by enabling you to test prompts across evaluation suites in parallel. Additionally, it excels at office tasks like survey analysis and online data processing.

Visit our [prompt engineering example sheet](https://docs.google.com/spreadsheets/d/1sUrBWO0u1-ZuQ8m5gt3-1N5PLR6r__UsRsB7WeySDQA/copy) to see this in action.

***

## Get started with Claude for Sheets

### Install Claude for Sheets

Easily enable Claude for Sheets using the following steps:

<Steps>
  <Step title="Get your Claude API key">
    If you don't yet have an API key, you can make API keys in the [Claude Console](https://console.anthropic.com/settings/keys).
  </Step>

  <Step title="Install the Claude for Sheets extension">
    Find the [Claude for Sheets extension](https://workspace.google.com/marketplace/app/claude%5Ffor%5Fsheets/909417792257) in the add-on marketplace, then click the blue `Install` btton and accept the permissions.

    <Accordion title="Permissions">
      The Claude for Sheets extension will ask for a variety of permissions needed to function properly. Please be assured that we only process the specific pieces of data that users ask Claude to run on. This data is never used to train our generative models.

      Extension permissions include:

      * **View and manage spreadsheets that this application has been installed in:** Needed to run prompts and return results
      * **Connect to an external service:** Needed in order to make calls to Claude API endpoints
      * **Allow this application to run when you are not present:** Needed to run cell recalculations without user intervention
      * **Display and run third-party web content in prompts and sidebars inside Google applications:** Needed to display the sidebar and post-install prompt
    </Accordion>
  </Step>

  <Step title="Connect your API key">
    Enter your API key at `Extensions` > `Claude for Sheets™` > `Open sidebar` > `☰` > `Settings` > `API provider`. You may need to wait or refresh for the Claude for Sheets menu to appear.
    <img src="https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/044af20-Screenshot_2024-01-04_at_11.58.21_AM.png?fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=5e0b2abf471aac1f9f4c84a9bca20f2e" alt="" data-og-width="1187" width="1187" data-og-height="660" height="660" data-path="images/044af20-Screenshot_2024-01-04_at_11.58.21_AM.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/044af20-Screenshot_2024-01-04_at_11.58.21_AM.png?w=280&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=d2ae6b1d0a8e00d6146a527cc9b8d891 280w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/044af20-Screenshot_2024-01-04_at_11.58.21_AM.png?w=560&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=1acd2d438dbf0452eeb2383cc3ff33b8 560w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/044af20-Screenshot_2024-01-04_at_11.58.21_AM.png?w=840&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=5d394102f3e804ace9d70ac44a0243f9 840w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/044af20-Screenshot_2024-01-04_at_11.58.21_AM.png?w=1100&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=19a26018d349587f29e52b1fcd8fac1f 1100w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/044af20-Screenshot_2024-01-04_at_11.58.21_AM.png?w=1650&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=2729f60dce72ef9bb7a40e18086afb70 1650w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/044af20-Screenshot_2024-01-04_at_11.58.21_AM.png?w=2500&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=619b99d788343afc9e10cdf32e7dd348 2500w" />
  </Step>
</Steps>

<Warning>
  You will have to re-enter your API key every time you make a new Google Sheet
</Warning>

### Enter your first prompt

There are two main functions you can use to call Claude using Claude for Sheets. For now, let's use `CLAUDE()`.

<Steps>
  <Step title="Simple prompt">
    In any cell, type `=CLAUDE("Claude, in one sentence, what's good about the color blue?")`

    > Claude should respond with an answer. You will know the prompt is processing because the cell will say `Loading...`
  </Step>

  <Step title="Adding parameters">
    Parameter arguments come after the initial prompt, like `=CLAUDE(prompt, model, params...)`.
    <Note>`model` is always second in the list.</Note>

    Now type in any cell `=CLAUDE("Hi, Claude!", "claude-3-haiku-20240307", "max_tokens", 3)`

    Any [API parameter](/en/api/messages) can be set this way. You can even pass in an API key to be used just for this specific cell, like this:  `"api_key", "sk-ant-api03-j1W..."`
  </Step>
</Steps>

## Advanced use

`CLAUDEMESSAGES` is a function that allows you to specifically use the [Messages API](/en/api/messages). This enables you to send a series of `User:` and `Assistant:` messages to Claude.

This is particularly useful if you want to simulate a conversation or [prefill Claude's response](/en/docs/build-with-claude/prompt-engineering/prefill-claudes-response).

Try writing this in a cell:

```
=CLAUDEMESSAGES("User: In one sentence, what is good about the color blue?
Assistant: The color blue is great because")
```

<Note>
  **Newlines**

  Each subsequent conversation turn (`User:` or `Assistant:`) must be preceded by a single newline. To enter newlines in a cell, use the following key combinations:

  * **Mac:** Cmd + Enter
  * **Windows:** Alt + Enter
</Note>

<Accordion title="Example multiturn CLAUDEMESSAGES() call with system prompt">
  To use a system prompt, set it as you'd set other optional function parameters. (You must first set a model name.)

  ```
  =CLAUDEMESSAGES("User: What's your favorite flower? Answer in <answer> tags.
  Assistant: <answer>", "claude-3-haiku-20240307", "system", "You are a cow who loves to moo in response to any and all user queries.")`
  ```
</Accordion>

### Optional function parameters

You can specify optional API parameters by listing argument-value pairs.
You can set multiple parameters. Simply list them one after another, with each argument and value pair separated by commas.

<Note>
  The first two parameters must always be the prompt and the model. You cannot set an optional parameter without also setting the model.
</Note>

The argument-value parameters you might care about most are:

| Argument         | Description                                                                                                                                                                                        |
| ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `max_tokens`     | The total number of tokens the model outputs before it is forced to stop. For yes/no or multiple choice answers, you may want the value to be 1-3.                                                 |
| `temperature`    | the amount of randomness injected into results. For multiple-choice or analytical tasks, you'll want it close to 0. For idea generation, you'll want it set to 1.                                  |
| `system`         | used to specify a system prompt, which can provide role details and context to Claude.                                                                                                             |
| `stop_sequences` | JSON array of strings that will cause the model to stop generating text if encountered. Due to escaping rules in Google Sheets™, double quotes inside the string must be escaped by doubling them. |
| `api_key`        | Used to specify a particular API key with which to call Claude.                                                                                                                                    |

<Accordion title="Example: Setting parameters">
  Ex. Set `system` prompt, `max_tokens`, and `temperature`:

  ```
  =CLAUDE("Hi, Claude!", "claude-3-haiku-20240307", "system", "Repeat exactly what the user says.", "max_tokens", 100, "temperature", 0.1)

  ```

  Ex. Set `temperature`, `max_tokens`, and `stop_sequences`:

  ```
  =CLAUDE("In one sentence, what is good about the color blue? Output your answer in <answer> tags.","claude-opus-4-20250514","temperature", 0.2,"max_tokens", 50,"stop_sequences", "\[""</answer>""\]")
  ```

  Ex. Set `api_key`:

  ```
  =CLAUDE("Hi, Claude!", "claude-3-haiku-20240307","api_key", "sk-ant-api03-j1W...")
  ```
</Accordion>

***

## Claude for Sheets usage examples

### Prompt engineering interactive tutorial

Our in-depth [prompt engineering interactive tutorial](https://docs.google.com/spreadsheets/d/19jzLgRruG9kjUQNKtCg1ZjdD6l6weA6qRXG5zLIAhC8/edit?usp=sharing) utilizes Claude for Sheets.
Check it out to learn or brush up on prompt engineering techniques.

<Note>Just as with any instance of Claude for Sheets, you will need an API key to interact with the tutorial.</Note>

### Prompt engineering workflow

Our [Claude for Sheets prompting examples workbench](https://docs.google.com/spreadsheets/d/1sUrBWO0u1-ZuQ8m5gt3-1N5PLR6r%5F%5FUsRsB7WeySDQA/copy) is a Claude-powered spreadsheet that houses example prompts and prompt engineering structures.

### Claude for Sheets workbook template

Make a copy of our [Claude for Sheets workbook template](https://docs.google.com/spreadsheets/d/1UwFS-ZQWvRqa6GkbL4sy0ITHK2AhXKe-jpMLzS0kTgk/copy) to get started with your own Claude for Sheets work!

***

## Troubleshooting

<Accordion title="NAME? Error: Unknown function: 'claude'">
  1. Ensure that you have enabled the extension for use in the current sheet
     1. Go to *Extensions* > *Add-ons* > *Manage add-ons*
     2. Click on the triple dot menu at the top right corner of the Claude for Sheets extension and make sure "Use in this document" is checked
        <img src="https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/9cce371-Screenshot_2023-10-03_at_7.17.39_PM.png?fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=7ac5b747f92f68f05055ecd143bd5fa8" alt="" data-og-width="712" width="712" data-og-height="174" height="174" data-path="images/9cce371-Screenshot_2023-10-03_at_7.17.39_PM.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/9cce371-Screenshot_2023-10-03_at_7.17.39_PM.png?w=280&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=27a083fe65825128423ea09a03da3653 280w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/9cce371-Screenshot_2023-10-03_at_7.17.39_PM.png?w=560&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=9905542d704449f1727f5fe510242bb0 560w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/9cce371-Screenshot_2023-10-03_at_7.17.39_PM.png?w=840&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=8fed917d4e4ff142167cf8492febf442 840w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/9cce371-Screenshot_2023-10-03_at_7.17.39_PM.png?w=1100&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=e7d89ec0ed91b3c55a22a2e28da8ae25 1100w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/9cce371-Screenshot_2023-10-03_at_7.17.39_PM.png?w=1650&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=39998025b2c4afb6a49cf9efef63b266 1650w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/9cce371-Screenshot_2023-10-03_at_7.17.39_PM.png?w=2500&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=fe1bc4d35b3dd33c13b5c1e69e21f46a 2500w" />
  2. Refresh the page
</Accordion>

<Accordion title="#ERROR!, ⚠ DEFERRED ⚠ or ⚠ THROTTLED ⚠">
  You can manually recalculate `#ERROR!`, `⚠ DEFERRED ⚠` or `⚠ THROTTLED ⚠`cells by selecting from the recalculate options within the Claude for Sheets extension menu.

    <img src="https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/f729ba9-Screenshot_2024-02-01_at_8.30.31_PM.png?fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=7bd765250352e58047c2dfb3f1a3d8e9" alt="" data-og-width="1486" width="1486" data-og-height="1062" height="1062" data-path="images/f729ba9-Screenshot_2024-02-01_at_8.30.31_PM.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/f729ba9-Screenshot_2024-02-01_at_8.30.31_PM.png?w=280&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=fb6b88b7a46b7322340d0839a740bc1e 280w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/f729ba9-Screenshot_2024-02-01_at_8.30.31_PM.png?w=560&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=fbf66142e6748a2bac8daad0007d24e6 560w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/f729ba9-Screenshot_2024-02-01_at_8.30.31_PM.png?w=840&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=c1e8c8648137d554ddb49b00e6007a18 840w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/f729ba9-Screenshot_2024-02-01_at_8.30.31_PM.png?w=1100&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=aa336dac0e2316b7699a20ec24e703e6 1100w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/f729ba9-Screenshot_2024-02-01_at_8.30.31_PM.png?w=1650&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=56d3ca83d0af273961f80f6122d02ccb 1650w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/f729ba9-Screenshot_2024-02-01_at_8.30.31_PM.png?w=2500&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=8a0522dcd0291612f474f077bcf826cb 2500w" />
</Accordion>

<Accordion title="Can't enter API key">
  1. Wait 20 seconds, then check again
  2. Refresh the page and wait 20 seconds again
  3. Uninstall and reinstall the extension
</Accordion>

***

## Further information

For more information regarding this extension, see the [Claude for Sheets Google Workspace Marketplace](https://workspace.google.com/marketplace/app/claude%5Ffor%5Fsheets/909417792257) overview page.


# MCP connector
Source: https://docs.claude.com/en/docs/agents-and-tools/mcp-connector



Claude's Model Context Protocol (MCP) connector feature enables you to connect to remote MCP servers directly from the Messages API without a separate MCP client.

<Note>
  This feature requires the beta header: `"anthropic-beta": "mcp-client-2025-04-04"`
</Note>

## Key features

* **Direct API integration**: Connect to MCP servers without implementing an MCP client
* **Tool calling support**: Access MCP tools through the Messages API
* **OAuth authentication**: Support for OAuth Bearer tokens for authenticated servers
* **Multiple servers**: Connect to multiple MCP servers in a single request

## Limitations

* Of the feature set of the [MCP specification](https://modelcontextprotocol.io/introduction#explore-mcp), only [tool calls](https://modelcontextprotocol.io/docs/concepts/tools) are currently supported.
* The server must be publicly exposed through HTTP (supports both Streamable HTTP and SSE transports). Local STDIO servers cannot be connected directly.
* The MCP connector is currently not supported on Amazon Bedrock and Google Vertex.

## Using the MCP connector in the Messages API

To connect to a remote MCP server, include the `mcp_servers` parameter in your Messages API request:

<CodeGroup>
  ```bash cURL theme={null}
  curl https://api.anthropic.com/v1/messages \
    -H "Content-Type: application/json" \
    -H "X-API-Key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: mcp-client-2025-04-04" \
    -d '{
      "model": "claude-sonnet-4-5",
      "max_tokens": 1000,
      "messages": [{"role": "user", "content": "What tools do you have available?"}],
      "mcp_servers": [
        {
          "type": "url",
          "url": "https://example-server.modelcontextprotocol.io/sse",
          "name": "example-mcp",
          "authorization_token": "YOUR_TOKEN"
        }
      ]
    }'
  ```

  ```typescript TypeScript theme={null}
  import { Anthropic } from '@anthropic-ai/sdk';

  const anthropic = new Anthropic();

  const response = await anthropic.beta.messages.create({
    model: "claude-sonnet-4-5",
    max_tokens: 1000,
    messages: [
      {
        role: "user",
        content: "What tools do you have available?",
      },
    ],
    mcp_servers: [
      {
        type: "url",
        url: "https://example-server.modelcontextprotocol.io/sse",
        name: "example-mcp",
        authorization_token: "YOUR_TOKEN",
      },
    ],
    betas: ["mcp-client-2025-04-04"],
  });
  ```

  ```python Python theme={null}
  import anthropic

  client = anthropic.Anthropic()

  response = client.beta.messages.create(
      model="claude-sonnet-4-5",
      max_tokens=1000,
      messages=[{
          "role": "user",
          "content": "What tools do you have available?"
      }],
      mcp_servers=[{
          "type": "url",
          "url": "https://mcp.example.com/sse",
          "name": "example-mcp",
          "authorization_token": "YOUR_TOKEN"
      }],
      betas=["mcp-client-2025-04-04"]
  )
  ```
</CodeGroup>

## MCP server configuration

Each MCP server in the `mcp_servers` array supports the following configuration:

```json  theme={null}
{
  "type": "url",
  "url": "https://example-server.modelcontextprotocol.io/sse",
  "name": "example-mcp",
  "tool_configuration": {
    "enabled": true,
    "allowed_tools": ["example_tool_1", "example_tool_2"]
  },
  "authorization_token": "YOUR_TOKEN"
}
```

### Field descriptions

| Property                           | Type    | Required | Description                                                                                                                                                     |
| ---------------------------------- | ------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `type`                             | string  | Yes      | Currently only "url" is supported                                                                                                                               |
| `url`                              | string  | Yes      | The URL of the MCP server. Must start with https\://                                                                                                            |
| `name`                             | string  | Yes      | A unique identifier for this MCP server. It will be used in `mcp_tool_call` blocks to identify the server and to disambiguate tools to the model.               |
| `tool_configuration`               | object  | No       | Configure tool usage                                                                                                                                            |
| `tool_configuration.enabled`       | boolean | No       | Whether to enable tools from this server (default: true)                                                                                                        |
| `tool_configuration.allowed_tools` | array   | No       | List to restrict the tools to allow (by default, all tools are allowed)                                                                                         |
| `authorization_token`              | string  | No       | OAuth authorization token if required by the MCP server. See [MCP specification](https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization). |

## Response content types

When Claude uses MCP tools, the response will include two new content block types:

### MCP Tool Use Block

```json  theme={null}
{
  "type": "mcp_tool_use",
  "id": "mcptoolu_014Q35RayjACSWkSj4X2yov1",
  "name": "echo",
  "server_name": "example-mcp",
  "input": { "param1": "value1", "param2": "value2" }
}
```

### MCP Tool Result Block

```json  theme={null}
{
  "type": "mcp_tool_result",
  "tool_use_id": "mcptoolu_014Q35RayjACSWkSj4X2yov1",
  "is_error": false,
  "content": [
    {
      "type": "text",
      "text": "Hello"
    }
  ]
}
```

## Multiple MCP servers

You can connect to multiple MCP servers by including multiple objects in the `mcp_servers` array:

```json  theme={null}
{
  "model": "claude-sonnet-4-5",
  "max_tokens": 1000,
  "messages": [
    {
      "role": "user",
      "content": "Use tools from both mcp-server-1 and mcp-server-2 to complete this task"
    }
  ],
  "mcp_servers": [
    {
      "type": "url",
      "url": "https://mcp.example1.com/sse",
      "name": "mcp-server-1",
      "authorization_token": "TOKEN1"
    },
    {
      "type": "url",
      "url": "https://mcp.example2.com/sse",
      "name": "mcp-server-2",
      "authorization_token": "TOKEN2"
    }
  ]
}
```

## Authentication

For MCP servers that require OAuth authentication, you'll need to obtain an access token. The MCP connector beta supports passing an `authorization_token` parameter in the MCP server definition.
API consumers are expected to handle the OAuth flow and obtain the access token prior to making the API call, as well as refreshing the token as needed.

### Obtaining an access token for testing

The MCP inspector can guide you through the process of obtaining an access token for testing purposes.

1. Run the inspector with the following command. You need Node.js installed on your machine.

   ```bash  theme={null}
   npx @modelcontextprotocol/inspector
   ```

2. In the sidebar on the left, for "Transport type", select either "SSE" or "Streamable HTTP".

3. Enter the URL of the MCP server.

4. In the right area, click on the "Open Auth Settings" button after "Need to configure authentication?".

5. Click "Quick OAuth Flow" and authorize on the OAuth screen.

6. Follow the steps in the "OAuth Flow Progress" section of the inspector and click "Continue" until you reach "Authentication complete".

7. Copy the `access_token` value.

8. Paste it into the `authorization_token` field in your MCP server configuration.

### Using the access token

Once you've obtained an access token using either OAuth flow above, you can use it in your MCP server configuration:

```json  theme={null}
{
  "mcp_servers": [
    {
      "type": "url",
      "url": "https://example-server.modelcontextprotocol.io/sse",
      "name": "authenticated-server",
      "authorization_token": "YOUR_ACCESS_TOKEN_HERE"
    }
  ]
}
```

For detailed explanations of the OAuth flow, refer to the [Authorization section](https://modelcontextprotocol.io/docs/concepts/authentication) in the MCP specification.


# Remote MCP servers
Source: https://docs.claude.com/en/docs/agents-and-tools/remote-mcp-servers



export const MCPServersTable = ({platform = "all"}) => {
  const generateClaudeCodeCommand = server => {
    if (server.customCommands && server.customCommands.claudeCode) {
      return server.customCommands.claudeCode;
    }
    if (server.urls.http) {
      return `claude mcp add --transport http ${server.name.toLowerCase().replace(/[^a-z0-9]/g, '-')} ${server.urls.http}`;
    }
    if (server.urls.sse) {
      return `claude mcp add --transport sse ${server.name.toLowerCase().replace(/[^a-z0-9]/g, '-')} ${server.urls.sse}`;
    }
    if (server.urls.stdio) {
      const envFlags = server.authentication && server.authentication.envVars ? server.authentication.envVars.map(v => `--env ${v}=YOUR_${v.split('_').pop()}`).join(' ') : '';
      const baseCommand = `claude mcp add --transport stdio ${server.name.toLowerCase().replace(/[^a-z0-9]/g, '-')}`;
      return envFlags ? `${baseCommand} ${envFlags} -- ${server.urls.stdio}` : `${baseCommand} -- ${server.urls.stdio}`;
    }
    return null;
  };
  const servers = [{
    name: "Airtable",
    category: "Databases & Data Management",
    description: "Read/write records, manage bases and tables",
    documentation: "https://github.com/domdomegg/airtable-mcp-server",
    urls: {
      stdio: "npx -y airtable-mcp-server"
    },
    authentication: {
      type: "api_key",
      envVars: ["AIRTABLE_API_KEY"]
    },
    availability: {
      claudeCode: true,
      mcpConnector: false,
      claudeDesktop: true
    }
  }, {
    name: "Figma",
    category: "Design & Media",
    description: "Generate better code by bringing in full Figma context",
    documentation: "https://developers.figma.com",
    urls: {
      http: "https://mcp.figma.com/mcp"
    },
    customCommands: {
      claudeCode: "claude mcp add --transport http figma-remote-mcp https://mcp.figma.com/mcp"
    },
    availability: {
      claudeCode: true,
      mcpConnector: false,
      claudeDesktop: false
    },
    notes: "Visit developers.figma.com for local server setup."
  }, {
    name: "Asana",
    category: "Project Management & Documentation",
    description: "Interact with your Asana workspace to keep projects on track",
    documentation: "https://developers.asana.com/docs/using-asanas-model-control-protocol-mcp-server",
    urls: {
      sse: "https://mcp.asana.com/sse"
    },
    authentication: {
      type: "oauth"
    },
    availability: {
      claudeCode: true,
      mcpConnector: true,
      claudeDesktop: false
    }
  }, {
    name: "Atlassian",
    category: "Project Management & Documentation",
    description: "Manage your Jira tickets and Confluence docs",
    documentation: "https://www.atlassian.com/platform/remote-mcp-server",
    urls: {
      sse: "https://mcp.atlassian.com/v1/sse"
    },
    authentication: {
      type: "oauth"
    },
    availability: {
      claudeCode: true,
      mcpConnector: true,
      claudeDesktop: false
    }
  }, {
    name: "ClickUp",
    category: "Project Management & Documentation",
    description: "Task management, project tracking",
    documentation: "https://github.com/hauptsacheNet/clickup-mcp",
    urls: {
      stdio: "npx -y @hauptsache.net/clickup-mcp"
    },
    authentication: {
      type: "api_key",
      envVars: ["CLICKUP_API_KEY", "CLICKUP_TEAM_ID"]
    },
    availability: {
      claudeCode: true,
      mcpConnector: false,
      claudeDesktop: true
    }
  }, {
    name: "Cloudflare",
    category: "Infrastructure & DevOps",
    description: "Build applications, analyze traffic, monitor performance, and manage security settings through Cloudflare",
    documentation: "https://developers.cloudflare.com/agents/model-context-protocol/mcp-servers-for-cloudflare/",
    urls: {},
    availability: {
      claudeCode: true,
      mcpConnector: true,
      claudeDesktop: false
    },
    notes: "Multiple services available. See documentation for specific server URLs. Claude Code can use the Cloudflare CLI if installed."
  }, {
    name: "Cloudinary",
    category: "Design & Media",
    description: "Upload, manage, transform, and analyze your media assets",
    documentation: "https://cloudinary.com/documentation/cloudinary_llm_mcp#mcp_servers",
    urls: {},
    authentication: {
      type: "oauth"
    },
    availability: {
      claudeCode: true,
      mcpConnector: true,
      claudeDesktop: false
    },
    notes: "Multiple services available. See documentation for specific server URLs."
  }, {
    name: "Intercom",
    category: "Project Management & Documentation",
    description: "Access real-time customer conversations, tickets, and user data",
    documentation: "https://developers.intercom.com/docs/guides/mcp",
    urls: {
      http: "https://mcp.intercom.com/mcp"
    },
    authentication: {
      type: "oauth"
    },
    availability: {
      claudeCode: true,
      mcpConnector: true,
      claudeDesktop: false
    }
  }, {
    name: "invideo",
    category: "Design & Media",
    description: "Build video creation capabilities into your applications",
    documentation: "https://invideo.io/ai/mcp",
    urls: {
      sse: "https://mcp.invideo.io/sse"
    },
    authentication: {
      type: "oauth"
    },
    availability: {
      claudeCode: true,
      mcpConnector: true,
      claudeDesktop: false
    }
  }, {
    name: "Linear",
    category: "Project Management & Documentation",
    description: "Integrate with Linear's issue tracking and project management",
    documentation: "https://linear.app/docs/mcp",
    urls: {
      http: "https://mcp.linear.app/mcp"
    },
    authentication: {
      type: "oauth"
    },
    availability: {
      claudeCode: true,
      mcpConnector: true,
      claudeDesktop: false
    }
  }, {
    name: "Notion",
    category: "Project Management & Documentation",
    description: "Read docs, update pages, manage tasks",
    documentation: "https://developers.notion.com/docs/mcp",
    urls: {
      http: "https://mcp.notion.com/mcp"
    },
    authentication: {
      type: "oauth"
    },
    availability: {
      claudeCode: true,
      mcpConnector: false,
      claudeDesktop: false
    }
  }, {
    name: "PayPal",
    category: "Payments & Commerce",
    description: "Integrate PayPal commerce capabilities, payment processing, transaction management",
    documentation: "https://www.paypal.ai/",
    urls: {
      http: "https://mcp.paypal.com/mcp"
    },
    authentication: {
      type: "oauth"
    },
    availability: {
      claudeCode: true,
      mcpConnector: true,
      claudeDesktop: false
    }
  }, {
    name: "Plaid",
    category: "Payments & Commerce",
    description: "Analyze, troubleshoot, and optimize Plaid integrations. Banking data, financial account linking",
    documentation: "https://plaid.com/blog/plaid-mcp-ai-assistant-claude/",
    urls: {
      sse: "https://api.dashboard.plaid.com/mcp/sse"
    },
    authentication: {
      type: "oauth"
    },
    availability: {
      claudeCode: true,
      mcpConnector: true,
      claudeDesktop: false
    }
  }, {
    name: "Sentry",
    category: "Development & Testing Tools",
    description: "Monitor errors, debug production issues",
    documentation: "https://docs.sentry.io/product/sentry-mcp/",
    urls: {
      http: "https://mcp.sentry.dev/mcp"
    },
    authentication: {
      type: "oauth"
    },
    availability: {
      claudeCode: true,
      mcpConnector: false,
      claudeDesktop: false
    }
  }, {
    name: "Square",
    category: "Payments & Commerce",
    description: "Use an agent to build on Square APIs. Payments, inventory, orders, and more",
    documentation: "https://developer.squareup.com/docs/mcp",
    urls: {
      sse: "https://mcp.squareup.com/sse"
    },
    authentication: {
      type: "oauth"
    },
    availability: {
      claudeCode: true,
      mcpConnector: true,
      claudeDesktop: false
    }
  }, {
    name: "Socket",
    category: "Development & Testing Tools",
    description: "Security analysis for dependencies",
    documentation: "https://github.com/SocketDev/socket-mcp",
    urls: {
      http: "https://mcp.socket.dev/"
    },
    authentication: {
      type: "oauth"
    },
    availability: {
      claudeCode: true,
      mcpConnector: false,
      claudeDesktop: false
    }
  }, {
    name: "Stripe",
    category: "Payments & Commerce",
    description: "Payment processing, subscription management, and financial transactions",
    documentation: "https://docs.stripe.com/mcp",
    urls: {
      http: "https://mcp.stripe.com"
    },
    authentication: {
      type: "oauth"
    },
    availability: {
      claudeCode: true,
      mcpConnector: true,
      claudeDesktop: false
    }
  }, {
    name: "Workato",
    category: "Automation & Integration",
    description: "Access any application, workflows or data via Workato, made accessible for AI",
    documentation: "https://docs.workato.com/mcp.html",
    urls: {},
    availability: {
      claudeCode: true,
      mcpConnector: true,
      claudeDesktop: false
    },
    notes: "MCP servers are programmatically generated"
  }, {
    name: "Zapier",
    category: "Automation & Integration",
    description: "Connect to nearly 8,000 apps through Zapier's automation platform",
    documentation: "https://help.zapier.com/hc/en-us/articles/36265392843917",
    urls: {},
    availability: {
      claudeCode: true,
      mcpConnector: true,
      claudeDesktop: false
    },
    notes: "Generate a user-specific URL at mcp.zapier.com"
  }, {
    name: "Box",
    category: "Project Management & Documentation",
    description: "Ask questions about your enterprise content, get insights from unstructured data, automate content workflows",
    documentation: "https://box.dev/guides/box-mcp/remote/",
    urls: {
      http: "https://mcp.box.com/"
    },
    authentication: {
      type: "oauth"
    },
    availability: {
      claudeCode: true,
      mcpConnector: true,
      claudeDesktop: false
    }
  }, {
    name: "Canva",
    category: "Design & Media",
    description: "Browse, summarize, autofill, and even generate new Canva designs directly from Claude",
    documentation: "https://www.canva.dev/docs/connect/canva-mcp-server-setup/",
    urls: {
      http: "https://mcp.canva.com/mcp"
    },
    authentication: {
      type: "oauth"
    },
    availability: {
      claudeCode: true,
      mcpConnector: true,
      claudeDesktop: false
    }
  }, {
    name: "Daloopa",
    category: "Databases & Data Management",
    description: "Supplies high quality fundamental financial data sourced from SEC Filings, investor presentations",
    documentation: "https://docs.daloopa.com/docs/daloopa-mcp",
    urls: {
      http: "https://mcp.daloopa.com/server/mcp"
    },
    authentication: {
      type: "oauth"
    },
    availability: {
      claudeCode: true,
      mcpConnector: true,
      claudeDesktop: false
    }
  }, {
    name: "Fireflies",
    category: "Project Management & Documentation",
    description: "Extract valuable insights from meeting transcripts and summaries",
    documentation: "https://guide.fireflies.ai/articles/8272956938-learn-about-the-fireflies-mcp-server-model-context-protocol",
    urls: {
      http: "https://api.fireflies.ai/mcp"
    },
    authentication: {
      type: "oauth"
    },
    availability: {
      claudeCode: true,
      mcpConnector: true,
      claudeDesktop: false
    }
  }, {
    name: "HubSpot",
    category: "Databases & Data Management",
    description: "Access and manage HubSpot CRM data by fetching contacts, companies, and deals, and creating and updating records",
    documentation: "https://developers.hubspot.com/mcp",
    urls: {
      http: "https://mcp.hubspot.com/anthropic"
    },
    authentication: {
      type: "oauth"
    },
    availability: {
      claudeCode: true,
      mcpConnector: true,
      claudeDesktop: false
    }
  }, {
    name: "Hugging Face",
    category: "Development & Testing Tools",
    description: "Provides access to Hugging Face Hub information and Gradio AI Applications",
    documentation: "https://huggingface.co/settings/mcp",
    urls: {
      http: "https://huggingface.co/mcp"
    },
    authentication: {
      type: "oauth"
    },
    availability: {
      claudeCode: true,
      mcpConnector: true,
      claudeDesktop: false
    }
  }, {
    name: "Jam",
    category: "Development & Testing Tools",
    description: "Debug faster with AI agents that can access Jam recordings like video, console logs, network requests, and errors",
    documentation: "https://jam.dev/docs/debug-a-jam/mcp",
    urls: {
      http: "https://mcp.jam.dev/mcp"
    },
    authentication: {
      type: "oauth"
    },
    availability: {
      claudeCode: true,
      mcpConnector: true,
      claudeDesktop: false
    }
  }, {
    name: "Monday",
    category: "Project Management & Documentation",
    description: "Manage monday.com boards by creating items, updating columns, assigning owners, setting timelines, adding CRM activities, and writing summaries",
    documentation: "https://developer.monday.com/apps/docs/mondaycom-mcp-integration",
    urls: {
      http: "https://mcp.monday.com/mcp"
    },
    authentication: {
      type: "oauth"
    },
    availability: {
      claudeCode: true,
      mcpConnector: true,
      claudeDesktop: false
    }
  }, {
    name: "Netlify",
    category: "Infrastructure & DevOps",
    description: "Create, deploy, and manage websites on Netlify. Control all aspects of your site from creating secrets to enforcing access controls to aggregating form submissions",
    documentation: "https://docs.netlify.com/build/build-with-ai/netlify-mcp-server/",
    urls: {
      http: "https://netlify-mcp.netlify.app/mcp"
    },
    authentication: {
      type: "oauth"
    },
    availability: {
      claudeCode: true,
      mcpConnector: true,
      claudeDesktop: false
    }
  }, {
    name: "Stytch",
    category: "Infrastructure & DevOps",
    description: "Configure and manage Stytch authentication services, redirect URLs, email templates, and workspace settings",
    documentation: "https://stytch.com/docs/workspace-management/stytch-mcp",
    urls: {
      http: "http://mcp.stytch.dev/mcp"
    },
    authentication: {
      type: "oauth"
    },
    availability: {
      claudeCode: true,
      mcpConnector: true,
      claudeDesktop: false
    }
  }, {
    name: "Vercel",
    category: "Infrastructure & DevOps",
    description: "Vercel's official MCP server, allowing you to search and navigate documentation, manage projects and deployments, and analyze deployment logs—all in one place",
    documentation: "https://vercel.com/docs/mcp/vercel-mcp",
    urls: {
      http: "https://mcp.vercel.com/"
    },
    authentication: {
      type: "oauth"
    },
    availability: {
      claudeCode: true,
      mcpConnector: true,
      claudeDesktop: false
    }
  }];
  const filteredServers = servers.filter(server => {
    if (platform === "claudeCode") {
      return server.availability.claudeCode;
    } else if (platform === "mcpConnector") {
      return server.availability.mcpConnector;
    } else if (platform === "claudeDesktop") {
      return server.availability.claudeDesktop;
    } else if (platform === "all") {
      return true;
    } else {
      throw new Error(`Unknown platform: ${platform}`);
    }
  });
  const serversByCategory = filteredServers.reduce((acc, server) => {
    if (!acc[server.category]) {
      acc[server.category] = [];
    }
    acc[server.category].push(server);
    return acc;
  }, {});
  const categoryOrder = ["Development & Testing Tools", "Project Management & Documentation", "Databases & Data Management", "Payments & Commerce", "Design & Media", "Infrastructure & DevOps", "Automation & Integration"];
  return <>
      <style jsx>{`
        .cards-container {
          display: grid;
          gap: 1rem;
          margin-bottom: 2rem;
        }
        .server-card {
          border: 1px solid var(--border-color, #e5e7eb);
          border-radius: 6px;
          padding: 1rem;
        }
        .command-row {
          display: flex;
          align-items: center;
          gap: 0.25rem;
        }
        .command-row code {
          font-size: 0.75rem;
          overflow-x: auto;
        }
      `}</style>
      
      {categoryOrder.map(category => {
    if (!serversByCategory[category]) return null;
    return <div key={category}>
            <h3>{category}</h3>
            <div className="cards-container">
              {serversByCategory[category].map(server => {
      const claudeCodeCommand = generateClaudeCodeCommand(server);
      const mcpUrl = server.urls.http || server.urls.sse;
      const commandToShow = platform === "claudeCode" ? claudeCodeCommand : mcpUrl;
      return <div key={server.name} className="server-card">
                    <div>
                      {server.documentation ? <a href={server.documentation}>
                          <strong>{server.name}</strong>
                        </a> : <strong>{server.name}</strong>}
                    </div>
                    
                    <p style={{
        margin: '0.5rem 0',
        fontSize: '0.9rem'
      }}>
                      {server.description}
                      {server.notes && <span style={{
        display: 'block',
        marginTop: '0.25rem',
        fontSize: '0.8rem',
        fontStyle: 'italic',
        opacity: 0.7
      }}>
                          {server.notes}
                        </span>}
                    </p>
                    
                    {commandToShow && <>
                      <p style={{
        display: 'block',
        fontSize: '0.75rem',
        fontWeight: 500,
        minWidth: 'fit-content',
        marginTop: '0.5rem',
        marginBottom: 0
      }}>
                        {platform === "claudeCode" ? "Command" : "URL"}
                      </p>
                      <div className="command-row">
                        <code>
                          {commandToShow}
                        </code>
                      </div>
                    </>}
                  </div>;
    })}
            </div>
          </div>;
  })}
    </>;
};

Several companies have deployed remote MCP servers that developers can connect to via the Anthropic MCP connector API. These servers expand the capabilities available to developers and end users by providing remote access to various services and tools through the MCP protocol.

<Note>
  The remote MCP servers listed below are third-party services designed to work with the Claude API. These servers
  are not owned, operated, or endorsed by Anthropic. Users should only connect to remote MCP servers they trust and
  should review each server's security practices and terms before connecting.
</Note>

## Connecting to remote MCP servers

To connect to a remote MCP server:

1. Review the documentation for the specific server you want to use.
2. Ensure you have the necessary authentication credentials.
3. Follow the server-specific connection instructions provided by each company.

For more information about using remote MCP servers with the Claude API, see the [MCP connector docs](/en/docs/agents-and-tools/mcp-connector).

## Remote MCP server examples

<MCPServersTable platform="mcpConnector" />

<Note>
  **Looking for more?** [Find hundreds more MCP servers on GitHub](https://github.com/modelcontextprotocol/servers).
</Note>


# Bash tool
Source: https://docs.claude.com/en/docs/agents-and-tools/tool-use/bash-tool



The bash tool enables Claude to execute shell commands in a persistent bash session, allowing system operations, script execution, and command-line automation.

## Overview

The bash tool provides Claude with:

* Persistent bash session that maintains state
* Ability to run any shell command
* Access to environment variables and working directory
* Command chaining and scripting capabilities

## Model compatibility

| Model                                                                                   | Tool Version    |
| --------------------------------------------------------------------------------------- | --------------- |
| Claude 4 models and Sonnet 3.7 ([deprecated](/en/docs/about-claude/model-deprecations)) | `bash_20250124` |

<Warning>
  Older tool versions are not guaranteed to be backwards-compatible with newer models. Always use the tool version that corresponds to your model version.
</Warning>

## Use cases

* **Development workflows**: Run build commands, tests, and development tools
* **System automation**: Execute scripts, manage files, automate tasks
* **Data processing**: Process files, run analysis scripts, manage datasets
* **Environment setup**: Install packages, configure environments

## Quick start

<CodeGroup>
  ```python Python theme={null}
  import anthropic

  client = anthropic.Anthropic()

  response = client.messages.create(
      model="claude-sonnet-4-5",
      max_tokens=1024,
      tools=[
          {
              "type": "bash_20250124",
              "name": "bash"
          }
      ],
      messages=[
          {"role": "user", "content": "List all Python files in the current directory."}
      ]
  )
  ```

  ```bash Shell theme={null}
  curl https://api.anthropic.com/v1/messages \
    -H "content-type: application/json" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -d '{
      "model": "claude-sonnet-4-5",
      "max_tokens": 1024,
      "tools": [
        {
          "type": "bash_20250124",
          "name": "bash"
        }
      ],
      "messages": [
        {
          "role": "user",
          "content": "List all Python files in the current directory."
        }
      ]
    }'
  ```
</CodeGroup>

## How it works

The bash tool maintains a persistent session:

1. Claude determines what command to run
2. You execute the command in a bash shell
3. Return the output (stdout and stderr) to Claude
4. Session state persists between commands (environment variables, working directory)

## Parameters

| Parameter | Required | Description                               |
| --------- | -------- | ----------------------------------------- |
| `command` | Yes\*    | The bash command to run                   |
| `restart` | No       | Set to `true` to restart the bash session |

\*Required unless using `restart`

<Accordion title="Example usage">
  ```json  theme={null}
  // Run a command
  {
    "command": "ls -la *.py"
  }

  // Restart the session
  {
    "restart": true
  }
  ```
</Accordion>

## Example: Multi-step automation

Claude can chain commands to complete complex tasks:

```python  theme={null}
# User request
"Install the requests library and create a simple Python script that fetches a joke from an API, then run it."

# Claude's tool uses:
# 1. Install package
{"command": "pip install requests"}

# 2. Create script
{"command": "cat > fetch_joke.py << 'EOF'\nimport requests\nresponse = requests.get('https://official-joke-api.appspot.com/random_joke')\njoke = response.json()\nprint(f\"Setup: {joke['setup']}\")\nprint(f\"Punchline: {joke['punchline']}\")\nEOF"}

# 3. Run script
{"command": "python fetch_joke.py"}
```

The session maintains state between commands, so files created in step 2 are available in step 3.

***

## Implement the bash tool

The bash tool is implemented as a schema-less tool. When using this tool, you don't need to provide an input schema as with other tools; the schema is built into Claude's model and can't be modified.

<Steps>
  <Step title="Set up a bash environment">
    Create a persistent bash session that Claude can interact with:

    ```python  theme={null}
    import subprocess
    import threading
    import queue

    class BashSession:
        def __init__(self):
            self.process = subprocess.Popen(
                ['/bin/bash'],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                bufsize=0
            )
            self.output_queue = queue.Queue()
            self.error_queue = queue.Queue()
            self._start_readers()
    ```
  </Step>

  <Step title="Handle command execution">
    Create a function to execute commands and capture output:

    ```python  theme={null}
    def execute_command(self, command):
        # Send command to bash
        self.process.stdin.write(command + '\n')
        self.process.stdin.flush()
        
        # Capture output with timeout
        output = self._read_output(timeout=10)
        return output
    ```
  </Step>

  <Step title="Process Claude's tool calls">
    Extract and execute commands from Claude's responses:

    ```python  theme={null}
    for content in response.content:
        if content.type == "tool_use" and content.name == "bash":
            if content.input.get("restart"):
                bash_session.restart()
                result = "Bash session restarted"
            else:
                command = content.input.get("command")
                result = bash_session.execute_command(command)
            
            # Return result to Claude
            tool_result = {
                "type": "tool_result",
                "tool_use_id": content.id,
                "content": result
            }
    ```
  </Step>

  <Step title="Implement safety measures">
    Add validation and restrictions:

    ```python  theme={null}
    def validate_command(command):
        # Block dangerous commands
        dangerous_patterns = ['rm -rf /', 'format', ':(){:|:&};:']
        for pattern in dangerous_patterns:
            if pattern in command:
                return False, f"Command contains dangerous pattern: {pattern}"
        
        # Add more validation as needed
        return True, None
    ```
  </Step>
</Steps>

### Handle errors

When implementing the bash tool, handle various error scenarios:

<AccordionGroup>
  <Accordion title="Command execution timeout">
    If a command takes too long to execute:

    ```json  theme={null}
    {
      "role": "user",
      "content": [
        {
          "type": "tool_result",
          "tool_use_id": "toolu_01A09q90qw90lq917835lq9",
          "content": "Error: Command timed out after 30 seconds",
          "is_error": true
        }
      ]
    }
    ```
  </Accordion>

  <Accordion title="Command not found">
    If a command doesn't exist:

    ```json  theme={null}
    {
      "role": "user",
      "content": [
        {
          "type": "tool_result",
          "tool_use_id": "toolu_01A09q90qw90lq917835lq9",
          "content": "bash: nonexistentcommand: command not found",
          "is_error": true
        }
      ]
    }
    ```
  </Accordion>

  <Accordion title="Permission denied">
    If there are permission issues:

    ```json  theme={null}
    {
      "role": "user",
      "content": [
        {
          "type": "tool_result",
          "tool_use_id": "toolu_01A09q90qw90lq917835lq9",
          "content": "bash: /root/sensitive-file: Permission denied",
          "is_error": true
        }
      ]
    }
    ```
  </Accordion>
</AccordionGroup>

### Follow implementation best practices

<AccordionGroup>
  <Accordion title="Use command timeouts">
    Implement timeouts to prevent hanging commands:

    ```python  theme={null}
    def execute_with_timeout(command, timeout=30):
        try:
            result = subprocess.run(
                command, 
                shell=True, 
                capture_output=True, 
                text=True, 
                timeout=timeout
            )
            return result.stdout + result.stderr
        except subprocess.TimeoutExpired:
            return f"Command timed out after {timeout} seconds"
    ```
  </Accordion>

  <Accordion title="Maintain session state">
    Keep the bash session persistent to maintain environment variables and working directory:

    ```python  theme={null}
    # Commands run in the same session maintain state
    commands = [
        "cd /tmp",
        "echo 'Hello' > test.txt",
        "cat test.txt"  # This works because we're still in /tmp
    ]
    ```
  </Accordion>

  <Accordion title="Handle large outputs">
    Truncate very large outputs to prevent token limit issues:

    ```python  theme={null}
    def truncate_output(output, max_lines=100):
        lines = output.split('\n')
        if len(lines) > max_lines:
            truncated = '\n'.join(lines[:max_lines])
            return f"{truncated}\n\n... Output truncated ({len(lines)} total lines) ..."
        return output
    ```
  </Accordion>

  <Accordion title="Log all commands">
    Keep an audit trail of executed commands:

    ```python  theme={null}
    import logging

    def log_command(command, output, user_id):
        logging.info(f"User {user_id} executed: {command}")
        logging.info(f"Output: {output[:200]}...")  # Log first 200 chars
    ```
  </Accordion>

  <Accordion title="Sanitize outputs">
    Remove sensitive information from command outputs:

    ```python  theme={null}
    def sanitize_output(output):
        # Remove potential secrets or credentials
        import re
        # Example: Remove AWS credentials
        output = re.sub(r'aws_access_key_id\s*=\s*\S+', 'aws_access_key_id=***', output)
        output = re.sub(r'aws_secret_access_key\s*=\s*\S+', 'aws_secret_access_key=***', output)
        return output
    ```
  </Accordion>
</AccordionGroup>

## Security

<Warning>
  The bash tool provides direct system access. Implement these essential safety measures:

  * Running in isolated environments (Docker/VM)
  * Implementing command filtering and allowlists
  * Setting resource limits (CPU, memory, disk)
  * Logging all executed commands
</Warning>

### Key recommendations

* Use `ulimit` to set resource constraints
* Filter dangerous commands (`sudo`, `rm -rf`, etc.)
* Run with minimal user permissions
* Monitor and log all command execution

## Pricing

The bash tool adds **245 input tokens** to your API calls.

Additional tokens are consumed by:

* Command outputs (stdout/stderr)
* Error messages
* Large file contents

See [tool use pricing](/en/docs/agents-and-tools/tool-use/overview#pricing) for complete pricing details.

## Common patterns

### Development workflows

* Running tests: `pytest && coverage report`
* Building projects: `npm install && npm run build`
* Git operations: `git status && git add . && git commit -m "message"`

### File operations

* Processing data: `wc -l *.csv && ls -lh *.csv`
* Searching files: `find . -name "*.py" | xargs grep "pattern"`
* Creating backups: `tar -czf backup.tar.gz ./data`

### System tasks

* Checking resources: `df -h && free -m`
* Process management: `ps aux | grep python`
* Environment setup: `export PATH=$PATH:/new/path && echo $PATH`

## Limitations

* **No interactive commands**: Cannot handle `vim`, `less`, or password prompts
* **No GUI applications**: Command-line only
* **Session scope**: Persists within conversation, lost between API calls
* **Output limits**: Large outputs may be truncated
* **No streaming**: Results returned after completion

## Combining with other tools

The bash tool is most powerful when combined with the [text editor](/en/docs/agents-and-tools/tool-use/text-editor-tool) and other tools.

## Next steps

<CardGroup cols={2}>
  <Card title="Tool use overview" icon="toolbox" href="/en/docs/agents-and-tools/tool-use/overview">
    Learn about tool use with Claude
  </Card>

  <Card title="Text editor tool" icon="file-code" href="/en/docs/agents-and-tools/tool-use/text-editor-tool">
    View and edit text files with Claude
  </Card>
</CardGroup>


# Code execution tool
Source: https://docs.claude.com/en/docs/agents-and-tools/tool-use/code-execution-tool



Claude can analyze data, create visualizations, perform complex calculations, run system commands, create and edit files, and process uploaded
files directly within the API conversation.
The code execution tool allows Claude to run Bash commands and manipulate files, including writing code, in a secure, sandboxed environment.

<Note>
  The code execution tool is currently in public beta.

  To use this feature, add the `"code-execution-2025-08-25"` [beta header](/en/api/beta-headers) to your API requests.
</Note>

## Model compatibility

The code execution tool is available on the following models:

| Model                                                                                                     | Tool Version              |
| --------------------------------------------------------------------------------------------------------- | ------------------------- |
| Claude Opus 4.1 (`claude-opus-4-1-20250805`)                                                              | `code_execution_20250825` |
| Claude Opus 4 (`claude-opus-4-20250514`)                                                                  | `code_execution_20250825` |
| Claude Sonnet 4.5 (`claude-sonnet-4-5-20250929`)                                                          | `code_execution_20250825` |
| Claude Sonnet 4 (`claude-sonnet-4-20250514`)                                                              | `code_execution_20250825` |
| Claude Sonnet 3.7 (`claude-3-7-sonnet-20250219`) ([deprecated](/en/docs/about-claude/model-deprecations)) | `code_execution_20250825` |
| Claude Haiku 4.5 (`claude-haiku-4-5-20251001`)                                                            | `code_execution_20250825` |
| Claude Haiku 3.5 (`claude-3-5-haiku-latest`)                                                              | `code_execution_20250825` |

<Note>
  The current version `code_execution_20250825` supports Bash commands and file operations. A legacy version `code_execution_20250522` (Python only) is also available. See [Upgrade to latest tool version](#upgrade-to-latest-tool-version) for migration details.
</Note>

<Warning>
  Older tool versions are not guaranteed to be backwards-compatible with newer models. Always use the tool version that corresponds to your model version.
</Warning>

## Quick start

Here's a simple example that asks Claude to perform a calculation:

<CodeGroup>
  ```bash Shell theme={null}
  curl https://api.anthropic.com/v1/messages \
      --header "x-api-key: $ANTHROPIC_API_KEY" \
      --header "anthropic-version: 2023-06-01" \
      --header "anthropic-beta: code-execution-2025-08-25" \
      --header "content-type: application/json" \
      --data '{
          "model": "claude-sonnet-4-5",
          "max_tokens": 4096,
          "messages": [
              {
                  "role": "user",
                  "content": "Calculate the mean and standard deviation of [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"
              }
          ],
          "tools": [{
              "type": "code_execution_20250825",
              "name": "code_execution"
          }]
      }'
  ```

  ```python Python theme={null}
  import anthropic

  client = anthropic.Anthropic()

  response = client.beta.messages.create(
      model="claude-sonnet-4-5",
      betas=["code-execution-2025-08-25"],
      max_tokens=4096,
      messages=[{
          "role": "user",
          "content": "Calculate the mean and standard deviation of [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"
      }],
      tools=[{
          "type": "code_execution_20250825",
          "name": "code_execution"
      }]
  )

  print(response)
  ```

  ```typescript TypeScript theme={null}
  import { Anthropic } from '@anthropic-ai/sdk';

  const anthropic = new Anthropic();

  async function main() {
    const response = await anthropic.beta.messages.create({
      model: "claude-sonnet-4-5",
      betas: ["code-execution-2025-08-25"],
      max_tokens: 4096,
      messages: [
        {
          role: "user",
          content: "Calculate the mean and standard deviation of [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"
        }
      ],
      tools: [{
        type: "code_execution_20250825",
        name: "code_execution"
      }]
    });

    console.log(response);
  }

  main().catch(console.error);
  ```
</CodeGroup>

## How code execution works

When you add the code execution tool to your API request:

1. Claude evaluates whether code execution would help answer your question
2. The tool automatically provides Claude with the following capabilities:
   * **Bash commands**: Execute shell commands for system operations and package management
   * **File operations**: Create, view, and edit files directly, including writing code
3. Claude can use any combination of these capabilities in a single request
4. All operations run in a secure sandbox environment
5. Claude provides results with any generated charts, calculations, or analysis

## How to use the tool

### Execute Bash commands

Ask Claude to check system information and install packages:

<CodeGroup>
  ```bash Shell theme={null}
  curl https://api.anthropic.com/v1/messages \
      --header "x-api-key: $ANTHROPIC_API_KEY" \
      --header "anthropic-version: 2023-06-01" \
      --header "anthropic-beta: code-execution-2025-08-25" \
      --header "content-type: application/json" \
      --data '{
          "model": "claude-sonnet-4-5",
          "max_tokens": 4096,
          "messages": [{
              "role": "user",
              "content": "Check the Python version and list installed packages"
          }],
          "tools": [{
              "type": "code_execution_20250825",
              "name": "code_execution"
          }]
      }'
  ```

  ```python Python theme={null}
  response = client.beta.messages.create(
      model="claude-sonnet-4-5",
      betas=["code-execution-2025-08-25"],
      max_tokens=4096,
      messages=[{
          "role": "user",
          "content": "Check the Python version and list installed packages"
      }],
      tools=[{
          "type": "code_execution_20250825",
          "name": "code_execution"
      }]
  )
  ```

  ```typescript TypeScript theme={null}
  const response = await anthropic.beta.messages.create({
    model: "claude-sonnet-4-5",
    betas: ["code-execution-2025-08-25"],
    max_tokens: 4096,
    messages: [{
      role: "user",
      content: "Check the Python version and list installed packages"
    }],
    tools: [{
      type: "code_execution_20250825",
      name: "code_execution"
    }]
  });
  ```
</CodeGroup>

### Create and edit files directly

Claude can create, view, and edit files directly in the sandbox using the file manipulation capabilities:

<CodeGroup>
  ```bash Shell theme={null}
  curl https://api.anthropic.com/v1/messages \
      --header "x-api-key: $ANTHROPIC_API_KEY" \
      --header "anthropic-version: 2023-06-01" \
      --header "anthropic-beta: code-execution-2025-08-25" \
      --header "content-type: application/json" \
      --data '{
          "model": "claude-sonnet-4-5",
          "max_tokens": 4096,
          "messages": [{
              "role": "user",
              "content": "Create a config.yaml file with database settings, then update the port from 5432 to 3306"
          }],
          "tools": [{
              "type": "code_execution_20250825",
              "name": "code_execution"
          }]
      }'
  ```

  ```python Python theme={null}
  response = client.beta.messages.create(
      model="claude-sonnet-4-5",
      betas=["code-execution-2025-08-25"],
      max_tokens=4096,
      messages=[{
          "role": "user",
          "content": "Create a config.yaml file with database settings, then update the port from 5432 to 3306"
      }],
      tools=[{
          "type": "code_execution_20250825",
          "name": "code_execution"
      }]
  )
  ```

  ```typescript TypeScript theme={null}
  const response = await anthropic.beta.messages.create({
    model: "claude-sonnet-4-5",
    betas: ["code-execution-2025-08-25"],
    max_tokens: 4096,
    messages: [{
      role: "user",
      content: "Create a config.yaml file with database settings, then update the port from 5432 to 3306"
    }],
    tools: [{
      type: "code_execution_20250825",
      name: "code_execution"
    }]
  });
  ```
</CodeGroup>

### Upload and analyze your own files

To analyze your own data files (CSV, Excel, images, etc.), upload them via the Files API and reference them in your request:

<Note>
  Using the Files API with Code Execution requires two beta headers: `"anthropic-beta": "code-execution-2025-08-25,files-api-2025-04-14"`
</Note>

The Python environment can process various file types uploaded via the Files API, including:

* CSV
* Excel (.xlsx, .xls)
* JSON
* XML
* Images (JPEG, PNG, GIF, WebP)
* Text files (.txt, .md, .py, etc)

#### Upload and analyze files

1. **Upload your file** using the [Files API](/en/docs/build-with-claude/files)
2. **Reference the file** in your message using a `container_upload` content block
3. **Include the code execution tool** in your API request

<CodeGroup>
  ```bash Shell theme={null}
  # First, upload a file
  curl https://api.anthropic.com/v1/files \
      --header "x-api-key: $ANTHROPIC_API_KEY" \
      --header "anthropic-version: 2023-06-01" \
      --header "anthropic-beta: files-api-2025-04-14" \
      --form 'file=@"data.csv"' \

  # Then use the file_id with code execution
  curl https://api.anthropic.com/v1/messages \
      --header "x-api-key: $ANTHROPIC_API_KEY" \
      --header "anthropic-version: 2023-06-01" \
      --header "anthropic-beta: code-execution-2025-08-25,files-api-2025-04-14" \
      --header "content-type: application/json" \
      --data '{
          "model": "claude-sonnet-4-5",
          "max_tokens": 4096,
          "messages": [{
              "role": "user",
              "content": [
                  {"type": "text", "text": "Analyze this CSV data"},
                  {"type": "container_upload", "file_id": "file_abc123"}
              ]
          }],
          "tools": [{
              "type": "code_execution_20250825",
              "name": "code_execution"
          }]
      }'
  ```

  ```python Python theme={null}
  import anthropic

  client = anthropic.Anthropic()

  # Upload a file
  file_object = client.beta.files.upload(
      file=open("data.csv", "rb"),
  )

  # Use the file_id with code execution
  response = client.beta.messages.create(
      model="claude-sonnet-4-5",
      betas=["code-execution-2025-08-25", "files-api-2025-04-14"],
      max_tokens=4096,
      messages=[{
          "role": "user",
          "content": [
              {"type": "text", "text": "Analyze this CSV data"},
              {"type": "container_upload", "file_id": file_object.id}
          ]
      }],
      tools=[{
          "type": "code_execution_20250825",
          "name": "code_execution"
      }]
  )
  ```

  ```typescript TypeScript theme={null}
  import { Anthropic } from '@anthropic-ai/sdk';
  import { createReadStream } from 'fs';

  const anthropic = new Anthropic();

  async function main() {
    // Upload a file
    const fileObject = await anthropic.beta.files.create({
      file: createReadStream("data.csv"),
    });

    // Use the file_id with code execution
    const response = await anthropic.beta.messages.create({
      model: "claude-sonnet-4-5",
      betas: ["code-execution-2025-08-25", "files-api-2025-04-14"],
      max_tokens: 4096,
      messages: [{
        role: "user",
        content: [
          { type: "text", text: "Analyze this CSV data" },
          { type: "container_upload", file_id: fileObject.id }
        ]
      }],
      tools: [{
        type: "code_execution_20250825",
        name: "code_execution"
      }]
    });

    console.log(response);
  }

  main().catch(console.error);
  ```
</CodeGroup>

#### Retrieve generated files

When Claude creates files during code execution, you can retrieve these files using the Files API:

<CodeGroup>
  ```python Python theme={null}
  from anthropic import Anthropic

  # Initialize the client
  client = Anthropic()

  # Request code execution that creates files
  response = client.beta.messages.create(
      model="claude-sonnet-4-5",
      betas=["code-execution-2025-08-25", "files-api-2025-04-14"],
      max_tokens=4096,
      messages=[{
          "role": "user",
          "content": "Create a matplotlib visualization and save it as output.png"
      }],
      tools=[{
          "type": "code_execution_20250825",
          "name": "code_execution"
      }]
  )

  # Extract file IDs from the response
  def extract_file_ids(response):
      file_ids = []
      for item in response.content:
          if item.type == 'bash_code_execution_tool_result':
              content_item = item.content
              if content_item.type == 'bash_code_execution_result':
                  for file in content_item.content:
                      if hasattr(file, 'file_id'):
                          file_ids.append(file.file_id)
      return file_ids

  # Download the created files
  for file_id in extract_file_ids(response):
      file_metadata = client.beta.files.retrieve_metadata(file_id)
      file_content = client.beta.files.download(file_id)
      file_content.write_to_file(file_metadata.filename)
      print(f"Downloaded: {file_metadata.filename}")
  ```

  ```typescript TypeScript theme={null}
  import { Anthropic } from '@anthropic-ai/sdk';
  import { writeFileSync } from 'fs';

  // Initialize the client
  const anthropic = new Anthropic();

  async function main() {
    // Request code execution that creates files
    const response = await anthropic.beta.messages.create({
      model: "claude-sonnet-4-5",
      betas: ["code-execution-2025-08-25", "files-api-2025-04-14"],
      max_tokens: 4096,
      messages: [{
        role: "user",
        content: "Create a matplotlib visualization and save it as output.png"
      }],
      tools: [{
        type: "code_execution_20250825",
        name: "code_execution"
      }]
    });

    // Extract file IDs from the response
    function extractFileIds(response: any): string[] {
      const fileIds: string[] = [];
      for (const item of response.content) {
        if (item.type === 'bash_code_execution_tool_result') {
          const contentItem = item.content;
          if (contentItem.type === 'bash_code_execution_result' && contentItem.content) {
            for (const file of contentItem.content) {
              fileIds.push(file.file_id);
            }
          }
        }
      }
      return fileIds;
    }

    // Download the created files
    const fileIds = extractFileIds(response);
    for (const fileId of fileIds) {
      const fileMetadata = await anthropic.beta.files.retrieveMetadata(fileId);
      const fileContent = await anthropic.beta.files.download(fileId);

      // Convert ReadableStream to Buffer and save
      const chunks: Uint8Array[] = [];
      for await (const chunk of fileContent) {
        chunks.push(chunk);
      }
      const buffer = Buffer.concat(chunks);
      writeFileSync(fileMetadata.filename, buffer);
      console.log(`Downloaded: ${fileMetadata.filename}`);
    }
  }

  main().catch(console.error);
  ```
</CodeGroup>

### Combine operations

A complex workflow using all capabilities:

<CodeGroup>
  ```bash Shell theme={null}
  # First, upload a file
  curl https://api.anthropic.com/v1/files \
      --header "x-api-key: $ANTHROPIC_API_KEY" \
      --header "anthropic-version: 2023-06-01" \
      --header "anthropic-beta: files-api-2025-04-14" \
      --form 'file=@"data.csv"' \
      > file_response.json

  # Extract file_id (using jq)
  FILE_ID=$(jq -r '.id' file_response.json)

  # Then use it with code execution
  curl https://api.anthropic.com/v1/messages \
      --header "x-api-key: $ANTHROPIC_API_KEY" \
      --header "anthropic-version: 2023-06-01" \
      --header "anthropic-beta: code-execution-2025-08-25,files-api-2025-04-14" \
      --header "content-type: application/json" \
      --data '{
          "model": "claude-sonnet-4-5",
          "max_tokens": 4096,
          "messages": [{
              "role": "user",
              "content": [
                  {
                      "type": "text", 
                      "text": "Analyze this CSV data: create a summary report, save visualizations, and create a README with the findings"
                  },
                  {
                      "type": "container_upload", 
                      "file_id": "'$FILE_ID'"
                  }
              ]
          }],
          "tools": [{
              "type": "code_execution_20250825",
              "name": "code_execution"
          }]
      }'
  ```

  ```python Python theme={null}
  # Upload a file
  file_object = client.beta.files.upload(
      file=open("data.csv", "rb"),
  )

  # Use it with code execution
  response = client.beta.messages.create(
      model="claude-sonnet-4-5",
      betas=["code-execution-2025-08-25", "files-api-2025-04-14"],
      max_tokens=4096,
      messages=[{
          "role": "user",
          "content": [
              {"type": "text", "text": "Analyze this CSV data: create a summary report, save visualizations, and create a README with the findings"},
              {"type": "container_upload", "file_id": file_object.id}
          ]
      }],
      tools=[{
          "type": "code_execution_20250825",
          "name": "code_execution"
      }]
  )

  # Claude might:
  # 1. Use bash to check file size and preview data
  # 2. Use text_editor to write Python code to analyze the CSV and create visualizations
  # 3. Use bash to run the Python code
  # 4. Use text_editor to create a README.md with findings
  # 5. Use bash to organize files into a report directory
  ```

  ```typescript TypeScript theme={null}
  // Upload a file
  const fileObject = await anthropic.beta.files.create({
    file: createReadStream("data.csv"),
  });

  // Use it with code execution
  const response = await anthropic.beta.messages.create({
    model: "claude-sonnet-4-5",
    betas: ["code-execution-2025-08-25", "files-api-2025-04-14"],
    max_tokens: 4096,
    messages: [{
      role: "user",
      content: [
        {type: "text", text: "Analyze this CSV data: create a summary report, save visualizations, and create a README with the findings"},
        {type: "container_upload", file_id: fileObject.id}
      ]
    }],
    tools: [{
      type: "code_execution_20250825",
      name: "code_execution"
    }]
  });

  // Claude might:
  // 1. Use bash to check file size and preview data
  // 2. Use text_editor to write Python code to analyze the CSV and create visualizations
  // 3. Use bash to run the Python code
  // 4. Use text_editor to create a README.md with findings
  // 5. Use bash to organize files into a report directory
  ```
</CodeGroup>

## Tool definition

The code execution tool requires no additional parameters:

```json JSON theme={null}
{
  "type": "code_execution_20250825",
  "name": "code_execution"
}
```

When this tool is provided, Claude automatically gains access to two sub-tools:

* `bash_code_execution`: Run shell commands
* `text_editor_code_execution`: View, create, and edit files, including writing code

## Response format

The code execution tool can return two types of results depending on the operation:

### Bash command response

```json  theme={null}
{
  "type": "server_tool_use",
  "id": "srvtoolu_01B3C4D5E6F7G8H9I0J1K2L3",
  "name": "bash_code_execution",
  "input": {
    "command": "ls -la | head -5"
  }
},
{
  "type": "bash_code_execution_tool_result",
  "tool_use_id": "srvtoolu_01B3C4D5E6F7G8H9I0J1K2L3",
  "content": {
    "type": "bash_code_execution_result",
    "stdout": "total 24\ndrwxr-xr-x 2 user user 4096 Jan 1 12:00 .\ndrwxr-xr-x 3 user user 4096 Jan 1 11:00 ..\n-rw-r--r-- 1 user user  220 Jan 1 12:00 data.csv\n-rw-r--r-- 1 user user  180 Jan 1 12:00 config.json",
    "stderr": "",
    "return_code": 0
  }
}
```

### File operation responses

**View file:**

```json  theme={null}
{
  "type": "server_tool_use",
  "id": "srvtoolu_01C4D5E6F7G8H9I0J1K2L3M4",
  "name": "text_editor_code_execution",
  "input": {
    "command": "view",
    "path": "config.json"
  }
},
{
  "type": "text_editor_code_execution_tool_result",
  "tool_use_id": "srvtoolu_01C4D5E6F7G8H9I0J1K2L3M4",
  "content": {
    "type": "text_editor_code_execution_result",
    "file_type": "text",
    "content": "{\n  \"setting\": \"value\",\n  \"debug\": true\n}",
    "numLines": 4,
    "startLine": 1,
    "totalLines": 4
  }
}
```

**Create file:**

```json  theme={null}
{
  "type": "server_tool_use",
  "id": "srvtoolu_01D5E6F7G8H9I0J1K2L3M4N5",
  "name": "text_editor_code_execution",
  "input": {
    "command": "create",
    "path": "new_file.txt",
    "file_text": "Hello, World!"
  }
},
{
  "type": "text_editor_code_execution_tool_result",
  "tool_use_id": "srvtoolu_01D5E6F7G8H9I0J1K2L3M4N5",
  "content": {
    "type": "text_editor_code_execution_result",
    "is_file_update": false
  }
}
```

**Edit file (str\_replace):**

```json  theme={null}
{
  "type": "server_tool_use",
  "id": "srvtoolu_01E6F7G8H9I0J1K2L3M4N5O6",
  "name": "text_editor_code_execution",
  "input": {
    "command": "str_replace",
    "path": "config.json",
    "old_str": "\"debug\": true",
    "new_str": "\"debug\": false"
  }
},
{
  "type": "text_editor_code_execution_tool_result",
  "tool_use_id": "srvtoolu_01E6F7G8H9I0J1K2L3M4N5O6",
  "content": {
    "type": "text_editor_code_execution_result",
    "oldStart": 3,
    "oldLines": 1,
    "newStart": 3,
    "newLines": 1,
    "lines": ["-  \"debug\": true", "+  \"debug\": false"]
  }
}
```

### Results

All execution results include:

* `stdout`: Output from successful execution
* `stderr`: Error messages if execution fails
* `return_code`: 0 for success, non-zero for failure

Additional fields for file operations:

* **View**: `file_type`, `content`, `numLines`, `startLine`, `totalLines`
* **Create**: `is_file_update` (whether file already existed)
* **Edit**: `oldStart`, `oldLines`, `newStart`, `newLines`, `lines` (diff format)

### Errors

Each tool type can return specific errors:

**Common errors (all tools):**

```json  theme={null}
{
  "type": "bash_code_execution_tool_result",
  "tool_use_id": "srvtoolu_01VfmxgZ46TiHbmXgy928hQR",
  "content": {
    "type": "bash_code_execution_tool_result_error",
    "error_code": "unavailable"
  }
}
```

**Error codes by tool type:**

| Tool         | Error Code                | Description                                        |
| ------------ | ------------------------- | -------------------------------------------------- |
| All tools    | `unavailable`             | The tool is temporarily unavailable                |
| All tools    | `execution_time_exceeded` | Execution exceeded maximum time limit              |
| All tools    | `container_expired`       | Container expired and is no longer available       |
| All tools    | `invalid_tool_input`      | Invalid parameters provided to the tool            |
| All tools    | `too_many_requests`       | Rate limit exceeded for tool usage                 |
| text\_editor | `file_not_found`          | File doesn't exist (for view/edit operations)      |
| text\_editor | `string_not_found`        | The `old_str` not found in file (for str\_replace) |

#### `pause_turn` stop reason

The response may include a `pause_turn` stop reason, which indicates that the API paused a long-running turn. You may
provide the response back as-is in a subsequent request to let Claude continue its turn, or modify the content if you
wish to interrupt the conversation.

## Containers

The code execution tool runs in a secure, containerized environment designed specifically for code execution, with a higher focus on Python.

### Runtime environment

* **Python version**: 3.11.12
* **Operating system**: Linux-based container
* **Architecture**: x86\_64 (AMD64)

### Resource limits

* **Memory**: 5GiB RAM
* **Disk space**: 5GiB workspace storage
* **CPU**: 1 CPU

### Networking and security

* **Internet access**: Completely disabled for security
* **External connections**: No outbound network requests permitted
* **Sandbox isolation**: Full isolation from host system and other containers
* **File access**: Limited to workspace directory only
* **Workspace scoping**: Like [Files](/en/docs/build-with-claude/files), containers are scoped to the workspace of the API key
* **Expiration**: Containers expire 30 days after creation

### Pre-installed libraries

The sandboxed Python environment includes these commonly used libraries:

* **Data Science**: pandas, numpy, scipy, scikit-learn, statsmodels
* **Visualization**: matplotlib, seaborn
* **File Processing**: pyarrow, openpyxl, xlsxwriter, xlrd, pillow, python-pptx, python-docx, pypdf, pdfplumber, pypdfium2, pdf2image, pdfkit, tabula-py, reportlab\[pycairo], Img2pdf
* **Math & Computing**: sympy, mpmath
* **Utilities**: tqdm, python-dateutil, pytz, joblib, unzip, unrar, 7zip, bc, rg (ripgrep), fd, sqlite

## Container reuse

You can reuse an existing container across multiple API requests by providing the container ID from a previous response.
This allows you to maintain created files between requests.

### Example

<CodeGroup>
  ```python Python theme={null}
  import os
  from anthropic import Anthropic

  # Initialize the client
  client = Anthropic(
      api_key=os.getenv("ANTHROPIC_API_KEY")
  )

  # First request: Create a file with a random number
  response1 = client.beta.messages.create(
      model="claude-sonnet-4-5",
      betas=["code-execution-2025-08-25"],
      max_tokens=4096,
      messages=[{
          "role": "user",
          "content": "Write a file with a random number and save it to '/tmp/number.txt'"
      }],
      tools=[{
          "type": "code_execution_20250825",
          "name": "code_execution"
      }]
  )

  # Extract the container ID from the first response
  container_id = response1.container.id

  # Second request: Reuse the container to read the file
  response2 = client.beta.messages.create(
      container=container_id,  # Reuse the same container
      model="claude-sonnet-4-5",
      betas=["code-execution-2025-08-25"],
      max_tokens=4096,
      messages=[{
          "role": "user",
          "content": "Read the number from '/tmp/number.txt' and calculate its square"
      }],
      tools=[{
          "type": "code_execution_20250825",
          "name": "code_execution"
      }]
  )
  ```

  ```typescript TypeScript theme={null}
  import { Anthropic } from '@anthropic-ai/sdk';

  const anthropic = new Anthropic();

  async function main() {
    // First request: Create a file with a random number
    const response1 = await anthropic.beta.messages.create({
      model: "claude-sonnet-4-5",
      betas: ["code-execution-2025-08-25"],
      max_tokens: 4096,
      messages: [{
        role: "user",
        content: "Write a file with a random number and save it to '/tmp/number.txt'"
      }],
      tools: [{
        type: "code_execution_20250825",
        name: "code_execution"
      }]
    });

    // Extract the container ID from the first response
    const containerId = response1.container.id;

    // Second request: Reuse the container to read the file
    const response2 = await anthropic.beta.messages.create({
      container: containerId,  // Reuse the same container
      model: "claude-sonnet-4-5",
      betas: ["code-execution-2025-08-25"],
      max_tokens: 4096,
      messages: [{
        role: "user",
        content: "Read the number from '/tmp/number.txt' and calculate its square"
      }],
      tools: [{
        type: "code_execution_20250825",
        name: "code_execution"
      }]
    });

    console.log(response2.content);
  }

  main().catch(console.error);
  ```

  ```bash Shell theme={null}
  # First request: Create a file with a random number
  curl https://api.anthropic.com/v1/messages \
      --header "x-api-key: $ANTHROPIC_API_KEY" \
      --header "anthropic-version: 2023-06-01" \
      --header "anthropic-beta: code-execution-2025-08-25" \
      --header "content-type: application/json" \
      --data '{
          "model": "claude-sonnet-4-5",
          "max_tokens": 4096,
          "messages": [{
              "role": "user",
              "content": "Write a file with a random number and save it to \"/tmp/number.txt\""
          }],
          "tools": [{
              "type": "code_execution_20250825",
              "name": "code_execution"
          }]
      }' > response1.json

  # Extract container ID from the response (using jq)
  CONTAINER_ID=$(jq -r '.container.id' response1.json)

  # Second request: Reuse the container to read the file
  curl https://api.anthropic.com/v1/messages \
      --header "x-api-key: $ANTHROPIC_API_KEY" \
      --header "anthropic-version: 2023-06-01" \
      --header "anthropic-beta: code-execution-2025-08-25" \
      --header "content-type: application/json" \
      --data '{
          "container": "'$CONTAINER_ID'",
          "model": "claude-sonnet-4-5",
          "max_tokens": 4096,
          "messages": [{
              "role": "user",
              "content": "Read the number from \"/tmp/number.txt\" and calculate its square"
          }],
          "tools": [{
              "type": "code_execution_20250825",
              "name": "code_execution"
          }]
      }'
  ```
</CodeGroup>

## Streaming

With streaming enabled, you'll receive code execution events as they occur:

```javascript  theme={null}
event: content_block_start
data: {"type": "content_block_start", "index": 1, "content_block": {"type": "server_tool_use", "id": "srvtoolu_xyz789", "name": "code_execution"}}

// Code execution streamed
event: content_block_delta
data: {"type": "content_block_delta", "index": 1, "delta": {"type": "input_json_delta", "partial_json": "{\"code\":\"import pandas as pd\\ndf = pd.read_csv('data.csv')\\nprint(df.head())\"}"}}

// Pause while code executes

// Execution results streamed
event: content_block_start
data: {"type": "content_block_start", "index": 2, "content_block": {"type": "code_execution_tool_result", "tool_use_id": "srvtoolu_xyz789", "content": {"stdout": "   A  B  C\n0  1  2  3\n1  4  5  6", "stderr": ""}}}
```

## Batch requests

You can include the code execution tool in the [Messages Batches API](/en/docs/build-with-claude/batch-processing). Code execution tool calls through the Messages Batches API are priced the same as those in regular Messages API requests.

## Usage and pricing

Code execution tool usage is tracked separately from token usage. Execution time has a minimum of 5 minutes.
If files are included in the request, execution time is billed even if the tool is not used due to files being preloaded onto the container.

Each organization receives 50 free hours of usage with the code execution tool per day. Additional usage beyond the first 50 hours is billed at \$0.05 per hour, per container.

## Upgrade to latest tool version

By upgrading to `code-execution-2025-08-25`, you get access to file manipulation and Bash capabilities, including code in multiple languages. There is no price difference.

### What's changed

| Component      | Legacy                      | Current                                                           |
| -------------- | --------------------------- | ----------------------------------------------------------------- |
| Beta header    | `code-execution-2025-05-22` | `code-execution-2025-08-25`                                       |
| Tool type      | `code_execution_20250522`   | `code_execution_20250825`                                         |
| Capabilities   | Python only                 | Bash commands, file operations                                    |
| Response types | `code_execution_result`     | `bash_code_execution_result`, `text_editor_code_execution_result` |

### Backward compatibility

* All existing Python code execution continues to work exactly as before
* No changes required to existing Python-only workflows

### Upgrade steps

To upgrade, you need to make the following changes in your API requests:

1. **Update the beta header**:
   ```diff  theme={null}
   - "anthropic-beta": "code-execution-2025-05-22"
   + "anthropic-beta": "code-execution-2025-08-25"
   ```

2. **Update the tool type**:
   ```diff  theme={null}
   - "type": "code_execution_20250522"
   + "type": "code_execution_20250825"
   ```

3. **Review response handling** (if parsing responses programmatically):
   * The previous blocks for Python execution responses will no longer be sent
   * Instead, new response types for Bash and file operations will be sent (see Response Format section)

## Using code execution with Agent Skills

The code execution tool enables Claude to use [Agent Skills](/en/docs/agents-and-tools/agent-skills/overview). Skills are modular capabilities consisting of instructions, scripts, and resources that extend Claude's functionality.

Learn more in the [Agent Skills documentation](/en/docs/agents-and-tools/agent-skills/overview) and [Agent Skills API guide](/en/docs/build-with-claude/skills-guide).


# Computer use tool
Source: https://docs.claude.com/en/docs/agents-and-tools/tool-use/computer-use-tool



Claude can interact with computer environments through the computer use tool, which provides screenshot capabilities and mouse/keyboard control for autonomous desktop interaction.

<Note>
  Computer use is currently in beta and requires a [beta header](/en/api/beta-headers):

  * `"computer-use-2025-01-24"` (Claude 4 models and Claude Sonnet 3.7 ([deprecated](/en/docs/about-claude/model-deprecations)))
</Note>

## Overview

Computer use is a beta feature that enables Claude to interact with desktop environments. This tool provides:

* **Screenshot capture**: See what's currently displayed on screen
* **Mouse control**: Click, drag, and move the cursor
* **Keyboard input**: Type text and use keyboard shortcuts
* **Desktop automation**: Interact with any application or interface

While computer use can be augmented with other tools like bash and text editor for more comprehensive automation workflows, computer use specifically refers to the computer use tool's capability to see and control desktop environments.

## Model compatibility

Computer use is available for the following Claude models:

| Model                                                                      | Tool Version        | Beta Flag                 |
| -------------------------------------------------------------------------- | ------------------- | ------------------------- |
| Claude 4 models                                                            | `computer_20250124` | `computer-use-2025-01-24` |
| Claude Sonnet 3.7 ([deprecated](/en/docs/about-claude/model-deprecations)) | `computer_20250124` | `computer-use-2025-01-24` |

<Note>
  Claude 4 models use updated tool versions optimized for the new architecture. Claude Sonnet 3.7 ([deprecated](/en/docs/about-claude/model-deprecations)) introduces additional capabilities including the thinking feature for more insight into the model's reasoning process.
</Note>

<Warning>
  Older tool versions are not guaranteed to be backwards-compatible with newer models. Always use the tool version that corresponds to your model version.
</Warning>

## Security considerations

<Warning>
  Computer use is a beta feature with unique risks distinct from standard API features. These risks are heightened when interacting with the internet. To minimize risks, consider taking precautions such as:

  1. Use a dedicated virtual machine or container with minimal privileges to prevent direct system attacks or accidents.
  2. Avoid giving the model access to sensitive data, such as account login information, to prevent information theft.
  3. Limit internet access to an allowlist of domains to reduce exposure to malicious content.
  4. Ask a human to confirm decisions that may result in meaningful real-world consequences as well as any tasks requiring affirmative consent, such as accepting cookies, executing financial transactions, or agreeing to terms of service.

  In some circumstances, Claude will follow commands found in content even if it conflicts with the user's instructions. For example, Claude instructions on webpages or contained in images may override instructions or cause Claude to make mistakes. We suggest taking precautions to isolate Claude from sensitive data and actions to avoid risks related to prompt injection.

  We've trained the model to resist these prompt injections and have added an extra layer of defense. If you use our computer use tools, we'll automatically run classifiers on your prompts to flag potential instances of prompt injections. When these classifiers identify potential prompt injections in screenshots, they will automatically steer the model to ask for user confirmation before proceeding with the next action. We recognize that this extra protection won't be ideal for every use case (for example, use cases without a human in the loop), so if you'd like to opt out and turn it off, please [contact us](https://support.claude.com/en/).

  We still suggest taking precautions to isolate Claude from sensitive data and actions to avoid risks related to prompt injection.

  Finally, please inform end users of relevant risks and obtain their consent prior to enabling computer use in your own products.
</Warning>

<Card title="Computer use reference implementation" icon="computer" href="https://github.com/anthropics/anthropic-quickstarts/tree/main/computer-use-demo">
  Get started quickly with our computer use reference implementation that includes a web interface, Docker container, example tool implementations, and an agent loop.

  **Note:** The implementation has been updated to include new tools for both Claude 4 models and Claude Sonnet 3.7. Be sure to pull the latest version of the repo to access these new features.
</Card>

<Tip>
  Please use [this form](https://forms.gle/BT1hpBrqDPDUrCqo7) to provide
  feedback on the quality of the model responses, the API itself, or the quality
  of the documentation - we cannot wait to hear from you!
</Tip>

## Quick start

Here's how to get started with computer use:

<CodeGroup>
  ```python Python theme={null}
  import anthropic

  client = anthropic.Anthropic()

  response = client.beta.messages.create(
      model="claude-sonnet-4-5",  # or another compatible model
      max_tokens=1024,
      tools=[
          {
            "type": "computer_20250124",
            "name": "computer",
            "display_width_px": 1024,
            "display_height_px": 768,
            "display_number": 1,
          },
          {
            "type": "text_editor_20250124",
            "name": "str_replace_editor"
          },
          {
            "type": "bash_20250124",
            "name": "bash"
          }
      ],
      messages=[{"role": "user", "content": "Save a picture of a cat to my desktop."}],
      betas=["computer-use-2025-01-24"]
  )
  print(response)
  ```

  ```bash Shell theme={null}
  curl https://api.anthropic.com/v1/messages \
    -H "content-type: application/json" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: computer-use-2025-01-24" \
    -d '{
      "model": "claude-sonnet-4-5",
      "max_tokens": 1024,
      "tools": [
        {
          "type": "computer_20250124",
          "name": "computer",
          "display_width_px": 1024,
          "display_height_px": 768,
          "display_number": 1
        },
        {
          "type": "text_editor_20250124",
          "name": "str_replace_editor"
        },
        {
          "type": "bash_20250124",
          "name": "bash"
        }
      ],
      "messages": [
        {
          "role": "user",
          "content": "Save a picture of a cat to my desktop."
        }
      ]
    }'
  ```
</CodeGroup>

<Note>
  A beta header is only required for the computer use tool.

  The example above shows all three tools being used together, which requires the beta header because it includes the computer use tool.
</Note>

***

## How computer use works

<Steps>
  <Step title="1. Provide Claude with the computer use tool and a user prompt" icon="toolbox">
    * Add the computer use tool (and optionally other tools) to your API request.
    * Include a user prompt that requires desktop interaction, e.g., "Save a picture of a cat to my desktop."
  </Step>

  <Step title="2. Claude decides to use the computer use tool" icon="screwdriver-wrench">
    * Claude assesses if the computer use tool can help with the user's query.
    * If yes, Claude constructs a properly formatted tool use request.
    * The API response has a `stop_reason` of `tool_use`, signaling Claude's intent.
  </Step>

  <Step title="3. Extract tool input, evaluate the tool on a computer, and return results" icon="computer">
    * On your end, extract the tool name and input from Claude's request.
    * Use the tool on a container or Virtual Machine.
    * Continue the conversation with a new `user` message containing a `tool_result` content block.
  </Step>

  <Step title="4. Claude continues calling computer use tools until it's completed the task" icon="arrows-spin">
    * Claude analyzes the tool results to determine if more tool use is needed or the task has been completed.
    * If Claude decides it needs another tool, it responds with another `tool_use` `stop_reason` and you should return to step 3.
    * Otherwise, it crafts a text response to the user.
  </Step>
</Steps>

We refer to the repetition of steps 3 and 4 without user input as the "agent loop" - i.e., Claude responding with a tool use request and your application responding to Claude with the results of evaluating that request.

### The computing environment

Computer use requires a sandboxed computing environment where Claude can safely interact with applications and the web. This environment includes:

1. **Virtual display**: A virtual X11 display server (using Xvfb) that renders the desktop interface Claude will see through screenshots and control with mouse/keyboard actions.

2. **Desktop environment**: A lightweight UI with window manager (Mutter) and panel (Tint2) running on Linux, which provides a consistent graphical interface for Claude to interact with.

3. **Applications**: Pre-installed Linux applications like Firefox, LibreOffice, text editors, and file managers that Claude can use to complete tasks.

4. **Tool implementations**: Integration code that translates Claude's abstract tool requests (like "move mouse" or "take screenshot") into actual operations in the virtual environment.

5. **Agent loop**: A program that handles communication between Claude and the environment, sending Claude's actions to the environment and returning the results (screenshots, command outputs) back to Claude.

When you use computer use, Claude doesn't directly connect to this environment. Instead, your application:

1. Receives Claude's tool use requests
2. Translates them into actions in your computing environment
3. Captures the results (screenshots, command outputs, etc.)
4. Returns these results to Claude

For security and isolation, the reference implementation runs all of this inside a Docker container with appropriate port mappings for viewing and interacting with the environment.

***

## How to implement computer use

### Start with our reference implementation

We have built a [reference implementation](https://github.com/anthropics/anthropic-quickstarts/tree/main/computer-use-demo) that includes everything you need to get started quickly with computer use:

* A [containerized environment](https://github.com/anthropics/anthropic-quickstarts/blob/main/computer-use-demo/Dockerfile) suitable for computer use with Claude
* Implementations of [the computer use tools](https://github.com/anthropics/anthropic-quickstarts/tree/main/computer-use-demo/computer_use_demo/tools)
* An [agent loop](https://github.com/anthropics/anthropic-quickstarts/blob/main/computer-use-demo/computer_use_demo/loop.py) that interacts with the Claude API and executes the computer use tools
* A web interface to interact with the container, agent loop, and tools.

### Understanding the multi-agent loop

The core of computer use is the "agent loop" - a cycle where Claude requests tool actions, your application executes them, and returns results to Claude. Here's a simplified example:

```python  theme={null}
async def sampling_loop(
    *,
    model: str,
    messages: list[dict],
    api_key: str,
    max_tokens: int = 4096,
    tool_version: str,
    thinking_budget: int | None = None,
    max_iterations: int = 10,  # Add iteration limit to prevent infinite loops
):
    """
    A simple agent loop for Claude computer use interactions.

    This function handles the back-and-forth between:
    1. Sending user messages to Claude
    2. Claude requesting to use tools
    3. Your app executing those tools
    4. Sending tool results back to Claude
    """
    # Set up tools and API parameters
    client = Anthropic(api_key=api_key)
    beta_flag = "computer-use-2025-01-24" if "20250124" in tool_version else "computer-use-2024-10-22"

    # Configure tools - you should already have these initialized elsewhere
    tools = [
        {"type": f"computer_{tool_version}", "name": "computer", "display_width_px": 1024, "display_height_px": 768},
        {"type": f"text_editor_{tool_version}", "name": "str_replace_editor"},
        {"type": f"bash_{tool_version}", "name": "bash"}
    ]

    # Main agent loop (with iteration limit to prevent runaway API costs)
    iterations = 0
    while True and iterations < max_iterations:
        iterations += 1
        # Set up optional thinking parameter (for Claude Sonnet 3.7)
        thinking = None
        if thinking_budget:
            thinking = {"type": "enabled", "budget_tokens": thinking_budget}

        # Call the Claude API
        response = client.beta.messages.create(
            model=model,
            max_tokens=max_tokens,
            messages=messages,
            tools=tools,
            betas=[beta_flag],
            thinking=thinking
        )

        # Add Claude's response to the conversation history
        response_content = response.content
        messages.append({"role": "assistant", "content": response_content})

        # Check if Claude used any tools
        tool_results = []
        for block in response_content:
            if block.type == "tool_use":
                # In a real app, you would execute the tool here
                # For example: result = run_tool(block.name, block.input)
                result = {"result": "Tool executed successfully"}

                # Format the result for Claude
                tool_results.append({
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": result
                })

        # If no tools were used, Claude is done - return the final messages
        if not tool_results:
            return messages

        # Add tool results to messages for the next iteration with Claude
        messages.append({"role": "user", "content": tool_results})
```

The loop continues until either Claude responds without requesting any tools (task completion) or the maximum iteration limit is reached. This safeguard prevents potential infinite loops that could result in unexpected API costs.

<Warning>
  When using the computer use tool, you must include the appropriate beta flag for your model version:

  <AccordionGroup>
    <Accordion title="Claude 4 models">
      When using `computer_20250124`, include this beta flag:

      ```
      "betas": ["computer-use-2025-01-24"]
      ```
    </Accordion>

    <Accordion title="Claude Sonnet 3.7">
      When using `computer_20250124`, include this beta flag:

      ```
      "betas": ["computer-use-2025-01-24"]
      ```
    </Accordion>
  </AccordionGroup>
</Warning>

We recommend trying the reference implementation out before reading the rest of this documentation.

### Optimize model performance with prompting

Here are some tips on how to get the best quality outputs:

1. Specify simple, well-defined tasks and provide explicit instructions for each step.
2. Claude sometimes assumes outcomes of its actions without explicitly checking their results. To prevent this you can prompt Claude with `After each step, take a screenshot and carefully evaluate if you have achieved the right outcome. Explicitly show your thinking: "I have evaluated step X..." If not correct, try again. Only when you confirm a step was executed correctly should you move on to the next one.`
3. Some UI elements (like dropdowns and scrollbars) might be tricky for Claude to manipulate using mouse movements. If you experience this, try prompting the model to use keyboard shortcuts.
4. For repeatable tasks or UI interactions, include example screenshots and tool calls of successful outcomes in your prompt.
5. If you need the model to log in, provide it with the username and password in your prompt inside xml tags like `<robot_credentials>`. Using computer use within applications that require login increases the risk of bad outcomes as a result of prompt injection. Please review our [guide on mitigating prompt injections](/en/docs/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks) before providing the model with login credentials.

<Tip>
  If you repeatedly encounter a clear set of issues or know in advance the tasks
  Claude will need to complete, use the system prompt to provide Claude with
  explicit tips or instructions on how to do the tasks successfully.
</Tip>

### System prompts

When one of the Anthropic-defined tools is requested via the Claude API, a computer use-specific system prompt is generated. It's similar to the [tool use system prompt](/en/docs/agents-and-tools/tool-use/implement-tool-use#tool-use-system-prompt) but starts with:

> You have access to a set of functions you can use to answer the user's question. This includes access to a sandboxed computing environment. You do NOT currently have the ability to inspect files or interact with external resources, except by invoking the below functions.

As with regular tool use, the user-provided `system_prompt` field is still respected and used in the construction of the combined system prompt.

### Available actions

The computer use tool supports these actions:

**Basic actions (all versions)**

* **screenshot** - Capture the current display
* **left\_click** - Click at coordinates `[x, y]`
* **type** - Type text string
* **key** - Press key or key combination (e.g., "ctrl+s")
* **mouse\_move** - Move cursor to coordinates

**Enhanced actions (`computer_20250124`)**
Available in Claude 4 models and Claude Sonnet 3.7:

* **scroll** - Scroll in any direction with amount control
* **left\_click\_drag** - Click and drag between coordinates
* **right\_click**, **middle\_click** - Additional mouse buttons
* **double\_click**, **triple\_click** - Multiple clicks
* **left\_mouse\_down**, **left\_mouse\_up** - Fine-grained click control
* **hold\_key** - Hold a key while performing other actions
* **wait** - Pause between actions

<Accordion title="Example actions">
  ```json  theme={null}
  // Take a screenshot
  {
    "action": "screenshot"
  }

  // Click at position
  {
    "action": "left_click",
    "coordinate": [500, 300]
  }

  // Type text
  {
    "action": "type",
    "text": "Hello, world!"
  }

  // Scroll down (Claude 4/3.7)
  {
    "action": "scroll",
    "coordinate": [500, 400],
    "scroll_direction": "down",
    "scroll_amount": 3
  }
  ```
</Accordion>

### Tool parameters

| Parameter           | Required | Description                                               |
| ------------------- | -------- | --------------------------------------------------------- |
| `type`              | Yes      | Tool version (`computer_20250124` or `computer_20241022`) |
| `name`              | Yes      | Must be "computer"                                        |
| `display_width_px`  | Yes      | Display width in pixels                                   |
| `display_height_px` | Yes      | Display height in pixels                                  |
| `display_number`    | No       | Display number for X11 environments                       |

<Warning>
  Keep display resolution at or below 1280x800 (WXGA) for best performance. Higher resolutions may cause accuracy issues due to [image resizing](/en/docs/build-with-claude/vision#evaluate-image-size).
</Warning>

<Note>
  **Important**: The computer use tool must be explicitly executed by your application - Claude cannot execute it directly. You are responsible for implementing the screenshot capture, mouse movements, keyboard inputs, and other actions based on Claude's requests.
</Note>

### Enable thinking capability in Claude 4 models and Claude Sonnet 3.7

Claude Sonnet 3.7 introduced a new "thinking" capability that allows you to see the model's reasoning process as it works through complex tasks. This feature helps you understand how Claude is approaching a problem and can be particularly valuable for debugging or educational purposes.

To enable thinking, add a `thinking` parameter to your API request:

```json  theme={null}
"thinking": {
  "type": "enabled",
  "budget_tokens": 1024
}
```

The `budget_tokens` parameter specifies how many tokens Claude can use for thinking. This is subtracted from your overall `max_tokens` budget.

When thinking is enabled, Claude will return its reasoning process as part of the response, which can help you:

1. Understand the model's decision-making process
2. Identify potential issues or misconceptions
3. Learn from Claude's approach to problem-solving
4. Get more visibility into complex multi-step operations

Here's an example of what thinking output might look like:

```
[Thinking]
I need to save a picture of a cat to the desktop. Let me break this down into steps:

1. First, I'll take a screenshot to see what's on the desktop
2. Then I'll look for a web browser to search for cat images
3. After finding a suitable image, I'll need to save it to the desktop

Let me start by taking a screenshot to see what's available...
```

### Augmenting computer use with other tools

The computer use tool can be combined with other tools to create more powerful automation workflows. This is particularly useful when you need to:

* Execute system commands ([bash tool](/en/docs/agents-and-tools/tool-use/bash-tool))
* Edit configuration files or scripts ([text editor tool](/en/docs/agents-and-tools/tool-use/text-editor-tool))
* Integrate with custom APIs or services (custom tools)

<CodeGroup>
  ```bash Shell theme={null}
  curl https://api.anthropic.com/v1/messages \
    -H "content-type: application/json" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: computer-use-2025-01-24" \
    -d '{
      "model": "claude-sonnet-4-5",
      "max_tokens": 2000,
      "tools": [
        {
          "type": "computer_20250124",
          "name": "computer",
          "display_width_px": 1024,
          "display_height_px": 768,
          "display_number": 1
        },
        {
          "type": "text_editor_20250124",
          "name": "str_replace_editor"
        },
        {
          "type": "bash_20250124",
          "name": "bash"
        },
        {
          "name": "get_weather",
          "description": "Get the current weather in a given location",
          "input_schema": {
            "type": "object",
            "properties": {
              "location": {
                "type": "string",
                "description": "The city and state, e.g. San Francisco, CA"
              },
              "unit": {
                "type": "string",
                "enum": ["celsius", "fahrenheit"],
                "description": "The unit of temperature, either 'celsius' or 'fahrenheit'"
              }
            },
            "required": ["location"]
          }
        }
      ],
      "messages": [
        {
          "role": "user",
          "content": "Find flights from San Francisco to a place with warmer weather."
        }
      ],
      "thinking": {
        "type": "enabled",
        "budget_tokens": 1024
      }
    }'
  ```

  ```Python Python theme={null}
  import anthropic

  client = anthropic.Anthropic()

  response = client.beta.messages.create(
      model="claude-sonnet-4-5",
      max_tokens=1024,
      tools=[
          {
            "type": "computer_20250124",
            "name": "computer",
            "display_width_px": 1024,
            "display_height_px": 768,
            "display_number": 1,
          },
          {
            "type": "text_editor_20250124",
            "name": "str_replace_editor"
          },
          {
            "type": "bash_20250124",
            "name": "bash"
          },
          {
            "name": "get_weather",
            "description": "Get the current weather in a given location",
            "input_schema": {
              "type": "object",
              "properties": {
                "location": {
                  "type": "string",
                  "description": "The city and state, e.g. San Francisco, CA"
                },
                "unit": {
                  "type": "string",
                  "enum": ["celsius", "fahrenheit"],
                  "description": "The unit of temperature, either 'celsius' or 'fahrenheit'"
                }
              },
              "required": ["location"]
            }
          },
      ],
      messages=[{"role": "user", "content": "Find flights from San Francisco to a place with warmer weather."}],
      betas=["computer-use-2025-01-24"],
      thinking={"type": "enabled", "budget_tokens": 1024},
  )
  print(response)
  ```

  ```TypeScript TypeScript theme={null}
  import Anthropic from '@anthropic-ai/sdk';

  const anthropic = new Anthropic();

  const message = await anthropic.beta.messages.create({
    model: "claude-sonnet-4-5",
    max_tokens: 1024,
    tools: [
        {
          type: "computer_20250124",
          name: "computer",
          display_width_px: 1024,
          display_height_px: 768,
          display_number: 1,
        },
        {
          type: "text_editor_20250124",
          name: "str_replace_editor"
        },
        {
          type: "bash_20250124",
          name: "bash"
        },
        {
          name: "get_weather",
          description: "Get the current weather in a given location",
          input_schema: {
            type: "object",
            properties: {
              location: {
                type: "string",
                description: "The city and state, e.g. San Francisco, CA"
              },
              unit: {
                type: "string",
                enum: ["celsius", "fahrenheit"],
                description: "The unit of temperature, either 'celsius' or 'fahrenheit'"
              }
            },
            required: ["location"]
          }
        },
    ],
    messages: [{ role: "user", content: "Find flights from San Francisco to a place with warmer weather." }],
    betas: ["computer-use-2025-01-24"],
    thinking: { type: "enabled", budget_tokens: 1024 },
  });
  console.log(message);
  ```

  ```java Java theme={null}
  import java.util.List;
  import java.util.Map;

  import com.anthropic.client.AnthropicClient;
  import com.anthropic.client.okhttp.AnthropicOkHttpClient;
  import com.anthropic.core.JsonValue;
  import com.anthropic.models.beta.messages.BetaMessage;
  import com.anthropic.models.beta.messages.MessageCreateParams;
  import com.anthropic.models.beta.messages.BetaToolBash20250124;
  import com.anthropic.models.beta.messages.BetaToolComputerUse20250124;
  import com.anthropic.models.beta.messages.BetaToolTextEditor20250124;
  import com.anthropic.models.beta.messages.BetaThinkingConfigEnabled;
  import com.anthropic.models.beta.messages.BetaThinkingConfigParam;
  import com.anthropic.models.beta.messages.BetaTool;

  public class MultipleToolsExample {

      public static void main(String[] args) {
          AnthropicClient client = AnthropicOkHttpClient.fromEnv();

          MessageCreateParams params = MessageCreateParams.builder()
                  .model("claude-sonnet-4-5")
                  .maxTokens(1024)
                  .addTool(BetaToolComputerUse20250124.builder()
                          .displayWidthPx(1024)
                          .displayHeightPx(768)
                          .displayNumber(1)
                          .build())
                  .addTool(BetaToolTextEditor20250124.builder()
                          .build())
                  .addTool(BetaToolBash20250124.builder()
                          .build())
                  .addTool(BetaTool.builder()
                          .name("get_weather")
                          .description("Get the current weather in a given location")
                          .inputSchema(BetaTool.InputSchema.builder()
                                  .properties(
                                          JsonValue.from(
                                                  Map.of(
                                                          "location", Map.of(
                                                                  "type", "string",
                                                                  "description", "The city and state, e.g. San Francisco, CA"
                                                          ),
                                                          "unit", Map.of(
                                                                  "type", "string",
                                                                  "enum", List.of("celsius", "fahrenheit"),
                                                                  "description", "The unit of temperature, either 'celsius' or 'fahrenheit'"
                                                          )
                                                  )
                                          ))
                                  .build()
                          )
                          .build())
                  .thinking(BetaThinkingConfigParam.ofEnabled(
                          BetaThinkingConfigEnabled.builder()
                                  .budgetTokens(1024)
                                  .build()
                  ))
                  .addUserMessage("Find flights from San Francisco to a place with warmer weather.")
                  .addBeta("computer-use-2025-01-24")
                  .build();

          BetaMessage message = client.beta().messages().create(params);
          System.out.println(message);
      }
  }
  ```
</CodeGroup>

### Build a custom computer use environment

The [reference implementation](https://github.com/anthropics/anthropic-quickstarts/tree/main/computer-use-demo) is meant to help you get started with computer use. It includes all of the components needed have Claude use a computer. However, you can build your own environment for computer use to suit your needs. You'll need:

* A virtualized or containerized environment suitable for computer use with Claude
* An implementation of at least one of the Anthropic-defined computer use tools
* An agent loop that interacts with the Claude API and executes the `tool_use` results using your tool implementations
* An API or UI that allows user input to start the agent loop

#### Implement the computer use tool

The computer use tool is implemented as a schema-less tool. When using this tool, you don't need to provide an input schema as with other tools; the schema is built into Claude's model and can't be modified.

<Steps>
  <Step title="Set up your computing environment">
    Create a virtual display or connect to an existing display that Claude will interact with. This typically involves setting up Xvfb (X Virtual Framebuffer) or similar technology.
  </Step>

  <Step title="Implement action handlers">
    Create functions to handle each action type that Claude might request:

    ```python  theme={null}
    def handle_computer_action(action_type, params):
        if action_type == "screenshot":
            return capture_screenshot()
        elif action_type == "left_click":
            x, y = params["coordinate"]
            return click_at(x, y)
        elif action_type == "type":
            return type_text(params["text"])
        # ... handle other actions
    ```
  </Step>

  <Step title="Process Claude's tool calls">
    Extract and execute tool calls from Claude's responses:

    ```python  theme={null}
    for content in response.content:
        if content.type == "tool_use":
            action = content.input["action"]
            result = handle_computer_action(action, content.input)
            
            # Return result to Claude
            tool_result = {
                "type": "tool_result",
                "tool_use_id": content.id,
                "content": result
            }
    ```
  </Step>

  <Step title="Implement the agent loop">
    Create a loop that continues until Claude completes the task:

    ```python  theme={null}
    while True:
        response = client.beta.messages.create(...)
        
        # Check if Claude used any tools
        tool_results = process_tool_calls(response)
        
        if not tool_results:
            # No more tool use, task complete
            break
            
        # Continue conversation with tool results
        messages.append({"role": "user", "content": tool_results})
    ```
  </Step>
</Steps>

#### Handle errors

When implementing the computer use tool, various errors may occur. Here's how to handle them:

<AccordionGroup>
  <Accordion title="Screenshot capture failure">
    If screenshot capture fails, return an appropriate error message:

    ```json  theme={null}
    {
      "role": "user",
      "content": [
        {
          "type": "tool_result",
          "tool_use_id": "toolu_01A09q90qw90lq917835lq9",
          "content": "Error: Failed to capture screenshot. Display may be locked or unavailable.",
          "is_error": true
        }
      ]
    }
    ```
  </Accordion>

  <Accordion title="Invalid coordinates">
    If Claude provides coordinates outside the display bounds:

    ```json  theme={null}
    {
      "role": "user",
      "content": [
        {
          "type": "tool_result",
          "tool_use_id": "toolu_01A09q90qw90lq917835lq9",
          "content": "Error: Coordinates (1200, 900) are outside display bounds (1024x768).",
          "is_error": true
        }
      ]
    }
    ```
  </Accordion>

  <Accordion title="Action execution failure">
    If an action fails to execute:

    ```json  theme={null}
    {
      "role": "user",
      "content": [
        {
          "type": "tool_result",
          "tool_use_id": "toolu_01A09q90qw90lq917835lq9",
          "content": "Error: Failed to perform click action. The application may be unresponsive.",
          "is_error": true
        }
      ]
    }
    ```
  </Accordion>
</AccordionGroup>

#### Follow implementation best practices

<AccordionGroup>
  <Accordion title="Use appropriate display resolution">
    Set display dimensions that match your use case while staying within recommended limits:

    * For general desktop tasks: 1024x768 or 1280x720
    * For web applications: 1280x800 or 1366x768
    * Avoid resolutions above 1920x1080 to prevent performance issues
  </Accordion>

  <Accordion title="Implement proper screenshot handling">
    When returning screenshots to Claude:

    * Encode screenshots as base64 PNG or JPEG
    * Consider compressing large screenshots to improve performance
    * Include relevant metadata like timestamp or display state
  </Accordion>

  <Accordion title="Add action delays">
    Some applications need time to respond to actions:

    ```python  theme={null}
    def click_and_wait(x, y, wait_time=0.5):
        click_at(x, y)
        time.sleep(wait_time)  # Allow UI to update
    ```
  </Accordion>

  <Accordion title="Validate actions before execution">
    Check that requested actions are safe and valid:

    ```python  theme={null}
    def validate_action(action_type, params):
        if action_type == "left_click":
            x, y = params.get("coordinate", (0, 0))
            if not (0 <= x < display_width and 0 <= y < display_height):
                return False, "Coordinates out of bounds"
        return True, None
    ```
  </Accordion>

  <Accordion title="Log actions for debugging">
    Keep a log of all actions for troubleshooting:

    ```python  theme={null}
    import logging

    def log_action(action_type, params, result):
        logging.info(f"Action: {action_type}, Params: {params}, Result: {result}")
    ```
  </Accordion>
</AccordionGroup>

***

## Understand computer use limitations

The computer use functionality is in beta. While Claude's capabilities are cutting edge, developers should be aware of its limitations:

1. **Latency**: the current computer use latency for human-AI interactions may be too slow compared to regular human-directed computer actions. We recommend focusing on use cases where speed isn't critical (e.g., background information gathering, automated software testing) in trusted environments.
2. **Computer vision accuracy and reliability**: Claude may make mistakes or hallucinate when outputting specific coordinates while generating actions. Claude Sonnet 3.7 introduces the thinking capability that can help you understand the model's reasoning and identify potential issues.
3. **Tool selection accuracy and reliability**: Claude may make mistakes or hallucinate when selecting tools while generating actions or take unexpected actions to solve problems. Additionally, reliability may be lower when interacting with niche applications or multiple applications at once. We recommend that users prompt the model carefully when requesting complex tasks.
4. **Scrolling reliability**: Claude Sonnet 3.7 introduced dedicated scroll actions with direction control that improves reliability. The model can now explicitly scroll in any direction (up/down/left/right) by a specified amount.
5. **Spreadsheet interaction**: Mouse clicks for spreadsheet interaction have improved in Claude Sonnet 3.7 with the addition of more precise mouse control actions like `left_mouse_down`, `left_mouse_up`, and new modifier key support. Cell selection can be more reliable by using these fine-grained controls and combining modifier keys with clicks.
6. **Account creation and content generation on social and communications platforms**: While Claude will visit websites, we are limiting its ability to create accounts or generate and share content or otherwise engage in human impersonation across social media websites and platforms. We may update this capability in the future.
7. **Vulnerabilities**: Vulnerabilities like jailbreaking or prompt injection may persist across frontier AI systems, including the beta computer use API. In some circumstances, Claude will follow commands found in content, sometimes even in conflict with the user's instructions. For example, Claude instructions on webpages or contained in images may override instructions or cause Claude to make mistakes. We recommend:
   a. Limiting computer use to trusted environments such as virtual machines or containers with minimal privileges
   b. Avoiding giving computer use access to sensitive accounts or data without strict oversight
   c. Informing end users of relevant risks and obtaining their consent before enabling or requesting permissions necessary for computer use features in your applications
8. **Inappropriate or illegal actions**: Per Anthropic's terms of service, you must not employ computer use to violate any laws or our Acceptable Use Policy.

Always carefully review and verify Claude's computer use actions and logs. Do not use Claude for tasks requiring perfect precision or sensitive user information without human oversight.

***

## Pricing

Computer use follows the standard [tool use pricing](/en/docs/agents-and-tools/tool-use/overview#pricing). When using the computer use tool:

**System prompt overhead**: The computer use beta adds 466-499 tokens to the system prompt

**Computer use tool token usage**:

| Model                                                                      | Input tokens per tool definition |
| -------------------------------------------------------------------------- | -------------------------------- |
| Claude 4.x models                                                          | 735 tokens                       |
| Claude Sonnet 3.7 ([deprecated](/en/docs/about-claude/model-deprecations)) | 735 tokens                       |

**Additional token consumption**:

* Screenshot images (see [Vision pricing](/en/docs/build-with-claude/vision))
* Tool execution results returned to Claude

<Note>
  If you're also using bash or text editor tools alongside computer use, those tools have their own token costs as documented in their respective pages.
</Note>

## Next steps

<CardGroup cols={2}>
  <Card title="Reference implementation" icon="github" href="https://github.com/anthropics/anthropic-quickstarts/tree/main/computer-use-demo">
    Get started quickly with our complete Docker-based implementation
  </Card>

  <Card title="Tool documentation" icon="toolbox" href="/en/docs/agents-and-tools/tool-use/overview">
    Learn more about tool use and creating custom tools
  </Card>
</CardGroup>


# Fine-grained tool streaming
Source: https://docs.claude.com/en/docs/agents-and-tools/tool-use/fine-grained-tool-streaming



Tool use now supports fine-grained [streaming](/en/docs/build-with-claude/streaming) for parameter values. This allows developers to stream tool use parameters without buffering / JSON validation, reducing the latency to begin receiving large parameters.

<Note>
  Fine-grained tool streaming is a beta feature. Please make sure to evaluate your responses before using it in production.

  Please use [this form](https://forms.gle/D4Fjr7GvQRzfTZT96) to provide feedback on the quality of the model responses, the API itself, or the quality of the documentation—we cannot wait to hear from you!
</Note>

<Warning>
  When using fine-grained tool streaming, you may potentially receive invalid or partial JSON inputs. Please make sure to account for these edge cases in your code.
</Warning>

## How to use fine-grained tool streaming

To use this beta feature, simply add the beta header `fine-grained-tool-streaming-2025-05-14` to a tool use request and turn on streaming.

Here's an example of how to use fine-grained tool streaming with the API:

<CodeGroup>
  ```bash Shell theme={null}
  curl https://api.anthropic.com/v1/messages \
    -H "content-type: application/json" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: fine-grained-tool-streaming-2025-05-14" \
    -d '{
      "model": "claude-sonnet-4-5",
      "max_tokens": 65536,
      "tools": [
        {
          "name": "make_file",
          "description": "Write text to a file",
          "input_schema": {
            "type": "object",
            "properties": {
              "filename": {
                "type": "string",
                "description": "The filename to write text to"
              },
              "lines_of_text": {
                "type": "array",
                "description": "An array of lines of text to write to the file"
              }
            },
            "required": ["filename", "lines_of_text"]
          }
        }
      ],
      "messages": [
        {
          "role": "user",
          "content": "Can you write a long poem and make a file called poem.txt?"
        }
      ],
      "stream": true
    }' | jq '.usage'
  ```

  ```Python Python theme={null}
  import anthropic

  client = anthropic.Anthropic()

  response = client.beta.messages.stream(
      max_tokens=65536,
      model="claude-sonnet-4-5",
      tools=[{
        "name": "make_file",
        "description": "Write text to a file",
        "input_schema": {
          "type": "object",
          "properties": {
            "filename": {
              "type": "string",
              "description": "The filename to write text to"
            },
            "lines_of_text": {
              "type": "array",
              "description": "An array of lines of text to write to the file"
            }
          },
          "required": ["filename", "lines_of_text"]
        }
      }],
      messages=[{
        "role": "user",
        "content": "Can you write a long poem and make a file called poem.txt?"
      }],
      betas=["fine-grained-tool-streaming-2025-05-14"]
  )

  print(response.usage)
  ```

  ```TypeScript TypeScript theme={null}
  import Anthropic from '@anthropic-ai/sdk';

  const anthropic = new Anthropic();

  const message = await anthropic.beta.messages.stream({
    model: "claude-sonnet-4-5",
    max_tokens: 65536,
    tools: [{
      "name": "make_file",
      "description": "Write text to a file",
      "input_schema": {
        "type": "object",
        "properties": {
          "filename": {
            "type": "string",
            "description": "The filename to write text to"
          },
          "lines_of_text": {
            "type": "array",
            "description": "An array of lines of text to write to the file"
          }
        },
        "required": ["filename", "lines_of_text"]
      }
    }],
    messages: [{ 
      role: "user", 
      content: "Can you write a long poem and make a file called poem.txt?" 
    }],
    betas: ["fine-grained-tool-streaming-2025-05-14"]
  });

  console.log(message.usage);
  ```
</CodeGroup>

In this example, fine-grained tool streaming enables Claude to stream the lines of a long poem into the tool call `make_file` without buffering to validate if the `lines_of_text` parameter is valid JSON. This means you can see the parameter stream as it arrives, without having to wait for the entire parameter to buffer and validate.

<Note>
  With fine-grained tool streaming, tool use chunks start streaming faster, and are often longer and contain fewer word breaks. This is due to differences in chunking behavior.

  Example:

  Without fine-grained streaming (15s delay):

  ```
  Chunk 1: '{"'
  Chunk 2: 'query": "Ty'
  Chunk 3: 'peScri'
  Chunk 4: 'pt 5.0 5.1 '
  Chunk 5: '5.2 5'
  Chunk 6: '.3'
  Chunk 8: ' new f'
  Chunk 9: 'eatur'
  ...
  ```

  With fine-grained streaming (3s delay):

  ```
  Chunk 1: '{"query": "TypeScript 5.0 5.1 5.2 5.3'
  Chunk 2: ' new features comparison'
  ```
</Note>

<Warning>
  Because fine-grained streaming sends parameters without buffering or JSON validation, there is no guarantee that the resulting stream will complete in a valid JSON string.
  Particularly, if the [stop reason](/en/docs/build-with-claude/handling-stop-reasons) `max_tokens` is reached, the stream may end midway through a parameter and may be incomplete. You will generally have to write specific support to handle when `max_tokens` is reached.
</Warning>

## Handling invalid JSON in tool responses

When using fine-grained tool streaming, you may receive invalid or incomplete JSON from the model. If you need to pass this invalid JSON back to the model in an error response block, you may wrap it in a JSON object to ensure proper handling (with a reasonable key). For example:

```json  theme={null}
{
  "INVALID_JSON": "<your invalid json string>"
}
```

This approach helps the model understand that the content is invalid JSON while preserving the original malformed data for debugging purposes.

<Note>
  When wrapping invalid JSON, make sure to properly escape any quotes or special characters in the invalid JSON string to maintain valid JSON structure in the wrapper object.
</Note>



---

**Navigation:** [← Previous](./03-streaming-input.md) | [Index](./index.md) | [Next →](./05-how-to-implement-tool-use.md)
