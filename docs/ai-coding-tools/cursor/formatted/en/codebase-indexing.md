---
title: "Codebase Indexing"
source: "https://docs.cursor.com/en/context/codebase-indexing"
language: "en"
language_name: "English"
---

# Codebase Indexing
Source: https://docs.cursor.com/en/context/codebase-indexing

How Cursor learns your codebase for better understanding

Cursor indexes your codebase by computing embeddings for each file. This improves AI-generated answers about your code. When you open a project, Cursor starts indexing automatically. New files are indexed incrementally.
Check indexing status at: `Cursor Settings` > `Indexing & Docs`

<Frame>
  <img src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=47c946c1a46c8047feda127ef84faa9d" alt="Codebase indexing progress indicator" data-og-width="2048" width="2048" data-og-height="1183" height="1183" data-path="images/get-started/codebase-indexing.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=3d628d1692d4cc512f4a81ece7e4a2c5 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=d5e20a24a9f38c97eb83249cd063ae41 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=ea26f1d9bf65ae5093333d15035ec96d 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=1d532fe92021c50bee36b97e541419df 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=01c4cfe42a58ac06f6ac18e6e565782e 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=41d02dff523bfa3a33c6d4e86e79732a 2500w" />
</Frame>

## Configuration

Cursor indexes all files except those in [ignore files](/en/context/ignore-files) (e.g. `.gitignore`, `.cursorignore`).

Click `Show Settings` to:

* Enable automatic indexing for new repositories
* Configure which files to ignore

<Tip>
  [Ignoring large content files](/en/context/ignore-files) improves answer
  accuracy.
</Tip>

### View indexed files

To see indexed file paths: `Cursor Settings` > `Indexing & Docs` > `View included files`

This opens a `.txt` file listing all indexed files.

## Multi-root workspaces

Cursor supports [multi-root workspaces](https://code.visualstudio.com/docs/editor/workspaces#_multiroot-workspaces), letting you work with multiple codebases:

* All codebases get indexed automatically
* Each codebase's context is available to AI
* `.cursor/rules` work in all folders

## PR search

PR search helps you understand your codebase's evolution by making historical changes searchable and accessible through AI.

### How it works

Cursor automatically **indexes all merged PRs** from your repository history. Summaries appear in semantic search results, with smart filtering to prioritize recent changes.

Agent can **fetch PRs, commits, issues, or branches** into context using `@[PR number]`, `@[commit hash]`, or `@[branch name]`. Includes GitHub comments and Bugbot reviews when connected.

**Platform support** includes GitHub, GitHub Enterprise, and Bitbucket. GitLab is not currently supported.

<Note>
  GitHub Enterprise users: The fetch tool falls back to git commands due to
  VSCode auth limitations.
</Note>

### Using PR search

Ask questions like "How are services implemented in other PRs?" and Agent will automatically fetch relevant PRs into context to provide comprehensive answers based on your repository's history.

## FAQ

<AccordionGroup>
  <Accordion title="Where can I see all indexed codebases?">
    No global list exists yet. Check each project individually by opening it in
    Cursor and checking Codebase Indexing settings.
  </Accordion>

  <Accordion title="How do I delete all indexed codebases?">
    Delete your Cursor account from Settings to remove all indexed codebases.
    Otherwise, delete individual codebases from each project's Codebase Indexing
    settings.
  </Accordion>

  <Accordion title="How long are indexed codebases retained?">
    Indexed codebases are deleted after 6 weeks of inactivity. Reopening the
    project triggers re-indexing.
  </Accordion>

  <Accordion title="Is my source code stored on Cursor servers?">
    No. Cursor creates embeddings without storing filenames or source code. Filenames are obfuscated and code chunks are encrypted.

    When Agent searches the codebase, Cursor retrieves the embeddings from the server and decrypts the chunks.
  </Accordion>
</AccordionGroup>

---

← Previous: [/command](./command.md) | [Index](./index.md) | Next: [Ignore files](./ignore-files.md) →