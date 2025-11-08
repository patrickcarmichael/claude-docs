---
title: "GitHub"
source: "https://docs.cursor.com/en/integrations/github"
language: "en"
language_name: "English"
---

# GitHub
Source: https://docs.cursor.com/en/integrations/github

Official Cursor GitHub app for background agents

[Background Agents](/en/background-agent) and [Bugbot](/en/bugbot) require the Cursor GitHub app to clone repositories and push changes.

## Installation

1. Go to [Integrations in Dashboard](https://cursor.com/dashboard?tab=integrations)
2. Click **Connect** next to GitHub
3. Choose repository either **All repositories** or **Selected repositories**

To disconnect your GitHub account, return to the integrations dashboard and click **Disconnect Account**.

## Using Agent in GitHub

The GitHub integration enables background agent workflows directly from pull requests and issues. You can trigger an agent to read context, implement fixes, and push commits by commenting `@cursor [prompt]` on any PR or issue.

If you have [Bugbot](/en/bugbot) enabled, you can comment `@cursor fix` to read the suggested fix from Bugbot to trigger a background agent to address the issue.

## Permissions

The GitHub app requires specific permissions to work with background agents:

<div className="full-width-table">
  | Permission                | Purpose                                          |
  | ------------------------- | ------------------------------------------------ |
  | **Repository access**     | Clone your code and create working branches      |
  | **Pull requests**         | Create PRs with agent changes for your review    |
  | **Issues**                | Track bugs and tasks that agents discover or fix |
  | **Checks and statuses**   | Report on code quality and test results          |
  | **Actions and workflows** | Monitor CI/CD pipelines and deployment status    |
</div>

All permissions follow the principle of least privilege needed for background agent functionality.

## IP Allow List Configuration

If your organization uses GitHub's IP allow list feature to restrict access to your repositories, you'll need to contact support first to enable IP allowlist functionality for your team.

### Contact Support

Before configuring IP allowlists, contact [hi@cursor.com](mailto:hi@cursor.com) to enable this feature for your team. This is required for both configuration methods below.

### Enable IP allow list configuration for installed GitHub Apps (Recommended)

The Cursor GitHub app has the IP list already pre-configured. You can enable the allowlist for installed apps to automatically inherit this list. This is the **recommended approach**, as it allows us to update the list and your organization receives updates automatically.

To enable this:

1. Go to your organization's Security settings
2. Navigate to IP allow list settings
3. Check **"Allow access by GitHub Apps"**

For detailed instructions, see [GitHub's documentation](https://docs.github.com/en/enterprise-cloud@latest/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/managing-allowed-ip-addresses-for-your-organization#allowing-access-by-github-apps).

### Add IPs directly to your allowlist

If your organization uses IdP-defined allowlists in GitHub or otherwise cannot use the pre-configured allowlist, you can manually add the IP addresses:

```
184.73.225.134
3.209.66.12
52.44.113.131
```

<Note>
  The list of IP addresses may infrequently change. Teams using IP allow lists will be given advanced notice before IP addresses are added or removed.
</Note>

## Troubleshooting

<AccordionGroup>
  <Accordion title="Agent can't access repository">
    * Install the GitHub app with repository access
    * Check repository permissions for private repos
    * Verify your GitHub account permissions
  </Accordion>

  <Accordion title="Permission denied for pull requests">
    * Grant the app write access to pull requests
    * Check branch protection rules
    * Reinstall if the app installation expired
  </Accordion>

  <Accordion title="App not visible in GitHub settings">
    * Check if installed at organization level
    * Reinstall from [github.com/apps/cursor](https://github.com/apps/cursor)
    * Contact support if installation is corrupted
  </Accordion>
</AccordionGroup>

---

← Previous: [Git](./git.md) | [Index](./index.md) | Next: [Linear](./linear.md) →