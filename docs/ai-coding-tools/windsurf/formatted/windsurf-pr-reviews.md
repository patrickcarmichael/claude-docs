---
title: "Windsurf PR Reviews"
source: "https://docs.windsurf.com/windsurf-reviews/windsurf-reviews"
---

# Windsurf PR Reviews
Source: https://docs.windsurf.com/windsurf-reviews/windsurf-reviews



Windsurf PR Reviews helps teams streamline code reviews with AI-powered feedback on GitHub pull requests. This feature is currently in beta for Teams and Enterprise customers using GitHub Cloud.

<Frame style={{ border: 'none', background: 'none', margin: '0 auto', display: 'flex'}}>
  <img src="https://mintcdn.com/codeium/d8O4q6w3H2CjrirL/assets/external-apps/github-bot-pr.png?fit=max&auto=format&n=d8O4q6w3H2CjrirL&q=85&s=b1e100ae9ff71de84cf1b2b939db8e12" data-og-width="2120" width="2120" data-og-height="1156" height="1156" data-path="assets/external-apps/github-bot-pr.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/d8O4q6w3H2CjrirL/assets/external-apps/github-bot-pr.png?w=280&fit=max&auto=format&n=d8O4q6w3H2CjrirL&q=85&s=cd92e04121f32251117b939eaa666b2d 280w, https://mintcdn.com/codeium/d8O4q6w3H2CjrirL/assets/external-apps/github-bot-pr.png?w=560&fit=max&auto=format&n=d8O4q6w3H2CjrirL&q=85&s=c8f9c2350fa281444d6a3337fae74ea1 560w, https://mintcdn.com/codeium/d8O4q6w3H2CjrirL/assets/external-apps/github-bot-pr.png?w=840&fit=max&auto=format&n=d8O4q6w3H2CjrirL&q=85&s=5ef52c4a1e831b14885aa116054c0075 840w, https://mintcdn.com/codeium/d8O4q6w3H2CjrirL/assets/external-apps/github-bot-pr.png?w=1100&fit=max&auto=format&n=d8O4q6w3H2CjrirL&q=85&s=e1d052ca684b4ca413b15eb871d1666c 1100w, https://mintcdn.com/codeium/d8O4q6w3H2CjrirL/assets/external-apps/github-bot-pr.png?w=1650&fit=max&auto=format&n=d8O4q6w3H2CjrirL&q=85&s=4548978dd7d615103c1dc2778ecea0ee 1650w, https://mintcdn.com/codeium/d8O4q6w3H2CjrirL/assets/external-apps/github-bot-pr.png?w=2500&fit=max&auto=format&n=d8O4q6w3H2CjrirL&q=85&s=0eed14d8f1f05325371337e5f3a9068a 2500w" />
</Frame>

## How It Works

Once enabled, Windsurf automatically reviews eligible pull requests in selected repositories and provides feedback as GitHub review comments.

Reviews can be manually triggered when you mark a PR as “ready for review” or you type `/windsurf-review` in a PR comment.

You can also edit a PR title by typing `/windsurf` into the PR title.

Example workflow:

1. Developer opens a pull request in an enabled repository
2. Developer marks the PR as ready for review or types “@windsurf /review” in a PR comment
3. Windsurf reviews the PR and posts feedback as GitHub review comments
4. Developer addresses feedback and updates the PR

<Note>Limitations: 50 files per PR and Organization-wide limit of 500 reviews/month.</Note>

## Setup

An organization admin must connect the Windsurf GitHub bot to your GitHub Cloud organization to enable Windsurf PR Reviews:

1. Navigate to the Windsurf Team Settings page and click on Github Integration, or click [here](https://windsurf.com/team/settings)
2. During installation on the Github side, select which repositories to enable for PR reviews
3. Back in the Windsurf settings, configure toggles for allowing reviews/edits, define PR Guidelines for Reviews and Descriptions
4. All users in the organization can then receive PR reviews on their pull requests

<Warning>Reviews are not triggered on draft pull requests.</Warning>

## Disabling PR Reviews

To disable Windsurf PR Reviews, disconnect the Windsurf GitHub bot from your organization or remove it from specific repositories via GitHub settings.

## Best Practices

For effective PR reviews:

* Use natural language in PR Guidelines
* Don't be too vague about the purpose of your changes
* Include detailed examples where helpful

---

← Previous: [Gathering Logs](./gathering-logs.md) | [Index](./index.md) | Next: [Analytics](./analytics.md) →