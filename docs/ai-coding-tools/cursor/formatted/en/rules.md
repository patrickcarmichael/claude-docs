---
title: "Rules"
source: "https://docs.cursor.com/en/context/rules"
language: "en"
language_name: "English"
---

# Rules
Source: https://docs.cursor.com/en/context/rules

Control how the Agent model behaves with reusable, scoped instructions.

Rules provide system-level instructions to Agent and Inline Edit. Think of them as persistent context, preferences, or workflows for your projects.

Cursor supports four types of rules:

<CardGroup cols={2}>
  <Card title="Project Rules" icon="folder-tree">
    Stored in `.cursor/rules`, version-controlled and scoped to your codebase.
  </Card>

  <Card title="User Rules" icon="user">
    Global to your Cursor environment. Defined in settings and always applied.
  </Card>

  <Card title="AGENTS.md" icon="robot">
    Agent instructions in markdown format. Simple alternative to `.cursor/rules`.
  </Card>

  <Card title=".cursorrules (Legacy)" icon="clock-rotate-left">
    Still supported, but deprecated. Use Project Rules instead.
  </Card>
</CardGroup>

## How rules work

Large language models don't retain memory between completions. Rules provide persistent, reusable context at the prompt level.

When applied, rule contents are included at the start of the model context. This gives the AI consistent guidance for generating code, interpreting edits, or helping with workflows.

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=e637bab83cfd5dcc8a3b15ed6fd9fc15" alt="Rule applied in context with chat" data-og-width="1198" width="1198" data-og-height="674" height="674" data-path="images/context/rules/rules-applied.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=78e3c392987c6f95a02fc106753c5f98 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=9d3a8b76ba99ada5ca302cba9fb63810 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=f5ab7fb374a1a4c5fe2f50e2e50d233a 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=5d25394a29c1da4172a3e673ee384c07 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=0fc125bd3c2a93551674252c0523d3ec 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=c576ea053ee18c30d2781c6bdd394a70 2500w" />
</Frame>

<Info>
  Rules apply to [Chat](/en/chat/overview) and [Inline
  Edit](/en/inline-edit/overview). Active rules show in the Agent sidebar.
</Info>

## Project rules

Project rules live in `.cursor/rules`. Each rule is a file and version-controlled. They can be scoped using path patterns, invoked manually, or included based on relevance. Subdirectories can include their own `.cursor/rules` directory scoped to that folder.

Use project rules to:

* Encode domain-specific knowledge about your codebase
* Automate project-specific workflows or templates
* Standardize style or architecture decisions

### Rule anatomy

Each rule file is written in **MDC** (`.mdc`), a format supporting metadata and content. Control how rules are applied from the type dropdown which changes properties `description`, `globs`, `alwaysApply`.

| <span class="no-wrap">Rule Type</span>         | Description                                                                      |
| :--------------------------------------------- | :------------------------------------------------------------------------------- |
| <span class="no-wrap">`Always`</span>          | Always included in model context                                                 |
| <span class="no-wrap">`Auto Attached`</span>   | Included when files matching a glob pattern are referenced                       |
| <span class="no-wrap">`Agent Requested`</span> | Available to AI, which decides whether to include it. Must provide a description |
| <span class="no-wrap">`Manual`</span>          | Only included when explicitly mentioned using `@ruleName`                        |

```
---
description: RPC Service boilerplate
globs:
alwaysApply: false
---

- Use our internal RPC pattern when defining services
- Always use snake_case for service names.

@service-template.ts
```

### Nested rules

Organize rules by placing them in `.cursor/rules` directories throughout your project. Nested rules automatically attach when files in their directory are referenced.

```
project/
  .cursor/rules/        # Project-wide rules
  backend/
    server/
      .cursor/rules/    # Backend-specific rules
  frontend/
    .cursor/rules/      # Frontend-specific rules
```

### Creating a rule

Create rules using the `New Cursor Rule` command or going to `Cursor Settings > Rules`. This creates a new rule file in `.cursor/rules`. From settings you can see all rules and their status.

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rule-settings.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=db8142786bbb7b7771ae0db8b2704b0b" alt="Comparison of concise vs long rules" data-og-width="6016" width="6016" data-og-height="3334" height="3334" data-path="images/context/rules/rule-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rule-settings.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=0b6e9b8d6ca799d1af62957726b1cc52 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rule-settings.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=8bfe1482ab9afc0995fe13371b26074b 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rule-settings.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=a847d915b3f106c42cba7cb1245bb138 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rule-settings.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=356963b3607152f7ffe128cd1a2d050e 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rule-settings.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=1b1e50d3721d42c691a434189729921c 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rule-settings.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=d2081cf016d65053f1e517eb5734079e 2500w" />
</Frame>

### Generating rules

Generate rules directly in conversations using the `/Generate Cursor Rules` command. Useful when you've made decisions about agent behavior and want to reuse them.

<Frame>
  <video src="https://www.cursor.com/changelog/049/generate-rules.mp4" controls>
    Your browser does not support the video tag.
  </video>
</Frame>

## Best practices

Good rules are focused, actionable, and scoped.

* Keep rules under 500 lines
* Split large rules into multiple, composable rules
* Provide concrete examples or referenced files
* Avoid vague guidance. Write rules like clear internal docs
* Reuse rules when repeating prompts in chat

## Examples

<AccordionGroup>
  <Accordion title="Standards for frontend components and API validation">
    This rule provides standards for frontend components:

    When working in components directory:

    * Always use Tailwind for styling
    * Use Framer Motion for animations
    * Follow component naming conventions

    This rule enforces validation for API endpoints:

    In API directory:

    * Use zod for all validation
    * Define return types with zod schemas
    * Export types generated from schemas
  </Accordion>

  <Accordion title="Templates for Express services and React components">
    This rule provides a template for Express services:

    Use this template when creating Express service:

    * Follow RESTful principles
    * Include error handling middleware
    * Set up proper logging

    @express-service-template.ts

    This rule defines React component structure:

    React components should follow this layout:

    * Props interface at top
    * Component as named export
    * Styles at bottom

    @component-template.tsx
  </Accordion>

  <Accordion title="Automating development workflows and documentation generation">
    This rule automates app analysis:

    When asked to analyze the app:

    1. Run dev server with `npm run dev`
    2. Fetch logs from console
    3. Suggest performance improvements

    This rule helps generate documentation:

    Help draft documentation by:

    * Extracting code comments
    * Analyzing README.md
    * Generating markdown documentation
  </Accordion>

  <Accordion title="Adding a new setting in Cursor">
    First create a property to toggle in `@reactiveStorageTypes.ts`.

    Add default value in `INIT_APPLICATION_USER_PERSISTENT_STORAGE` in `@reactiveStorageService.tsx`.

    For beta features, add toggle in `@settingsBetaTab.tsx`, otherwise add in `@settingsGeneralTab.tsx`. Toggles can be added as `<SettingsSubSection>` for general checkboxes. Look at the rest of the file for examples.

    ```
    <SettingsSubSection
    				label="Your feature name"
    				description="Your feature description"
    				value={
    					vsContext.reactiveStorageService.applicationUserPersistentStorage
    						.myNewProperty ?? false
    				}
    				onChange={(newVal) => {
    					vsContext.reactiveStorageService.setApplicationUserPersistentStorage(
    						'myNewProperty',
    						newVal
    					);
    				}}
    			/>
    ```

    To use in the app, import reactiveStorageService and use the property:

    ```
    const flagIsEnabled = vsContext.reactiveStorageService.applicationUserPersistentStorage.myNewProperty
    ```
  </Accordion>
</AccordionGroup>

Many examples available from providers and frameworks. Community-contributed rules are found across crowdsourced collections and repositories online.

## AGENTS.md

`AGENTS.md` is a simple markdown file for defining agent instructions. Place it in your project root as an alternative to `.cursor/rules` for straightforward use cases.

Unlike Project Rules, `AGENTS.md` is a plain markdown file without metadata or complex configurations. It's perfect for projects that need simple, readable instructions without the overhead of structured rules.

```markdown  theme={null}

---

← Previous: [Memories](./memories.md) | [Index](./index.md) | Next: [Concepts](./concepts.md) →