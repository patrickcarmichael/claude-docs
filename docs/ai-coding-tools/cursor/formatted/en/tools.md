---
title: "Tools"
source: "https://docs.cursor.com/en/agent/tools"
language: "en"
language_name: "English"
---

# Tools
Source: https://docs.cursor.com/en/agent/tools

Tools available to agents for searching, editing, and running code

A list of all tools available to modes within the [Agent](/en/agent/overview), which you can enable or disable when building your own [custom modes](/en/agent/modes#custom).

<Note>
  There is no limit on the number of tool calls Agent can make during a task. Agent will continue using tools as needed to complete your request.
</Note>

## Search

Tools used to search your codebase and the web to find relevant information.

<AccordionGroup>
  <Accordion title="Read File" icon="file-lines">
    Reads up to 250 lines (750 in max mode) of a file.
  </Accordion>

  <Accordion title="List Directory" icon="folder-open">
    Read the structure of a directory without reading file contents.
  </Accordion>

  <Accordion title="Codebase" icon="database">
    Perform semantic searches within your [indexed
    codebase](/en/context/codebase-indexing).
  </Accordion>

  <Accordion title="Grep" icon="magnifying-glass">
    Search for exact keywords or patterns within files.
  </Accordion>

  <Accordion title="Search Files" icon="file-magnifying-glass">
    Find files by name using fuzzy matching.
  </Accordion>

  <Accordion title="Web" icon="globe">
    Generate search queries and perform web searches.
  </Accordion>

  <Accordion title="Fetch Rules" icon="gavel">
    Retrieve specific [rules](/en/context/rules) based on type and description.
  </Accordion>
</AccordionGroup>

## Edit

Tools used to make specific edits to your files and codebase.

<AccordionGroup>
  <Accordion title="Edit & Reapply" icon="pencil">
    Suggest edits to files and [apply](/en/agent/apply) them automatically.
  </Accordion>

  <Accordion title="Delete File" icon="trash">
    Delete files autonomously (can be disabled in settings).
  </Accordion>
</AccordionGroup>

## Run

Chat can interact with your terminal.

<AccordionGroup>
  <Accordion title="Terminal" icon="terminal">
    Execute terminal commands and monitor output.
  </Accordion>
</AccordionGroup>

<Note>By default, Cursor uses the first terminal profile available.</Note>

To set your preferred terminal profile:

1. Open Command Palette (`Cmd/Ctrl+Shift+P`)
2. Search for "Terminal: Select Default Profile"
3. Choose your desired profile

## MCP

Chat can use configured MCP servers to interact with external services, such as databases or 3rd party APIs.

<AccordionGroup>
  <Accordion title="Toggle MCP Servers" icon="server">
    Toggle available MCP servers. Respects auto-run configuration.
  </Accordion>
</AccordionGroup>

Learn more about [Model Context Protocol](/en/context/model-context-protocol) and explore available servers in the [MCP directory](/en/tools).

## Advanced options

<AccordionGroup>
  <Accordion title="Auto-apply Edits" icon="check">
    Automatically apply edits without manual confirmation.
  </Accordion>

  <Accordion title="Auto-run" icon="play">
    Automatically execute terminal commands and accept edits. Useful for running test suites and verifying changes.

    <Frame>
      <img src="https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=3135722076a5aa636d27dbedec665bae" data-og-width="1624" width="1624" data-og-height="1012" height="1012" data-path="images/agent/auto-run.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=280&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=9f2e2bed8f634201adc51ccb2bd96cd2 280w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=560&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=51704cac2f270a04856fffbeaccf9700 560w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=840&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=01a5034975497a8dff4f41dca0d19f2e 840w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=1100&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=5f19026a0c6e5fb28c935ce795edb706 1100w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=1650&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=a108fc86f8ee7c0db6e5b7ab80ede738 1650w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=2500&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=9ce5f45879c29049640bb5a1494db11e 2500w" />
    </Frame>
  </Accordion>

  <Accordion title="Guardrails" icon="shield">
    Configure allow lists to specify which tools can execute automatically. Allow lists provide better security by explicitly defining permitted operations.
  </Accordion>

  <Accordion title="Auto-fix Errors" icon="wrench">
    Automatically resolve linter errors and warnings when encountered by Agent.
  </Accordion>
</AccordionGroup>

---

← Previous: [Terminal](./terminal.md) | [Index](./index.md) | Next: [Background Agents](./background-agents.md) →