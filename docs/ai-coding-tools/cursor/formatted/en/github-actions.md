---
title: "GitHub Actions"
source: "https://docs.cursor.com/en/cli/github-actions"
language: "en"
language_name: "English"
---

# GitHub Actions
Source: https://docs.cursor.com/en/cli/github-actions

Learn how to use Cursor CLI in GitHub Actions and other continuous integration systems

Use Cursor CLI in GitHub Actions and other CI/CD systems to automate development tasks.

## GitHub Actions integration

Basic setup:

```yaml  theme={null}
- name: Install Cursor CLI
  run: |
    curl https://cursor.com/install -fsS | bash
    echo "$HOME/.cursor/bin" >> $GITHUB_PATH

- name: Run Cursor Agent
  env:
    CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
  run: |
    cursor-agent -p "Your prompt here" --model gpt-5
```

## Cookbook examples

See our cookbook examples for practical workflows: [updating documentation](/en/cli/cookbook/update-docs) and [fixing CI issues](/en/cli/cookbook/fix-ci).

## Other CI systems

Use Cursor CLI in any CI/CD system with:

* **Shell script execution** (bash, zsh, etc.)
* **Environment variables** for API key configuration
* **Internet connectivity** to reach Cursor's API

## Autonomy levels

Choose your agent's autonomy level:

### Full autonomy approach

Give the agent complete control over git operations, API calls, and external interactions. Simpler setup, requires more trust.

**Example:** In our [Update Documentation](/en/cli/cookbook/update-docs) cookbook, the first workflow lets the agent:

* Analyze PR changes
* Create and manage git branches
* Commit and push changes
* Post comments on pull requests
* Handle all error scenarios

```yaml  theme={null}
- name: Update docs (full autonomy)
  run: |
    cursor-agent -p "You have full access to git, GitHub CLI, and PR operations. 
    Handle the entire docs update workflow including commits, pushes, and PR comments."
```

### Restricted autonomy approach

<Note>
  We recommend using this approach with **permission-based restrictions** for production CI workflows. This gives you the best of both worlds: the agent can intelligently handle complex analysis and file modifications while critical operations remain deterministic and auditable.
</Note>

Limit agent operations while handling critical steps in separate workflow steps. Better control and predictability.

**Example:** The second workflow in the same cookbook restricts the agent to only file modifications:

```yaml  theme={null}
- name: Generate docs updates (restricted)
  run: |
    cursor-agent -p "IMPORTANT: Do NOT create branches, commit, push, or post PR comments. 
    Only modify files in the working directory. A later workflow step handles publishing."

- name: Publish docs branch (deterministic)
  run: |
    # Deterministic git operations handled by CI
    git checkout -B "docs/${{ github.head_ref }}"
    git add -A
    git commit -m "docs: update for PR"
    git push origin "docs/${{ github.head_ref }}"

- name: Post PR comment (deterministic)  
  run: |
    # Deterministic PR commenting handled by CI
    gh pr comment ${{ github.event.pull_request.number }} --body "Docs updated"
```

### Permission-based restrictions

Use [permission configurations](/en/cli/reference/permissions) to enforce restrictions at the CLI level:

```json  theme={null}
{
  "permissions": {
    "allow": [
      "Read(**/*.md)",
      "Write(docs/**/*)",
      "Shell(grep)",
      "Shell(find)"
    ],
    "deny": [
      "Shell(git)",
      "Shell(gh)", 
      "Write(.env*)",
      "Write(package.json)"
    ]
  }
}
```

## Authentication

### Generate your API key

First, [generate an API key](/en/cli/reference/authentication#api-key-authentication) from your Cursor dashboard.

### Configure repository secrets

Store your Cursor API key securely in your repository:

1. Go to your GitHub repository
2. Click **Settings** → **Secrets and variables** → **Actions**
3. Click **New repository secret**
4. Name it `CURSOR_API_KEY`
5. Paste your API key as the value
6. Click **Add secret**

### Use in workflows

Set your `CURSOR_API_KEY` environment variable:

```yaml  theme={null}
env:
  CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
```

---

← Previous: [Update Docs](./update-docs.md) | [Index](./index.md) | Next: [Using Headless CLI](./using-headless-cli.md) →