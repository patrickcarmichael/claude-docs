---
title: "Bugbot"
source: "https://docs.cursor.com/en/bugbot"
language: "en"
language_name: "English"
---

# Bugbot
Source: https://docs.cursor.com/en/bugbot

AI code review for pull requests

Bugbot reviews pull requests and identifies bugs, security issues, and code quality problems.

<Tip>
  Bugbot includes a free tier: every user gets a limited number of free PR reviews each month. When you reach the limit, reviews pause until your next billing cycle. You can upgrade anytime to a 14‑day free Pro trial for unlimited reviews (subject to standard abuse guardrails).
</Tip>

<Frame>
  <video src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-report-cropped.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=013060fbd22f397ac81f2c32bb8b6b14" alt="Bugbot leaving comments on a PR" autoPlay loop muted playsInline controls data-path="images/bugbot/bugbot-report-cropped.mp4" />
</Frame>

## How it works

Bugbot analyzes PR diffs and leaves comments with explanations and fix suggestions. It runs automatically on each PR update or manually when triggered.

* Runs **automatic reviews** on every PR update
* **Manual trigger** by commenting `cursor review` or `bugbot run` on any PR
* **Fix in Cursor** links open issues directly in Cursor
* **Fix in Web** links open issues directly in [cursor.com/agents](https://cursor.com/agents)

## Setup

Requires Cursor admin access and GitHub org admin access.

1. Go to [cursor.com/dashboard](https://cursor.com/dashboard?tab=bugbot)
2. Navigate to the Bugbot tab
3. Click `Connect GitHub` (or `Manage Connections` if already connected)
4. Follow the GitHub installation flow
5. Return to the dashboard to enable Bugbot on specific repositories

<Frame>
  <video src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-install.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=75745d4464b183c306a44571db86a0c4" alt="Bugbot GitHub setup" autoPlay loop muted playsInline controls data-path="images/bugbot/bugbot-install.mp4" />
</Frame>

## Configuration

<Tabs defaultValue="Team">
  <Tab title="Individual">
    ### Repository settings

    Enable or disable Bugbot per repository from your installations list. Bugbot runs only on PRs you author.

    ### Personal settings

    * Run **only when mentioned** by commenting `cursor review` or `bugbot run`
    * Run **only once** per PR, skipping subsequent commits
  </Tab>

  <Tab title="Team">
    ### Repository settings

    Team admins can enable Bugbot per repository, configure allow/deny lists for reviewers, and set:

    * Run **only once** per PR per installation, skipping subsequent commits
    * **Disable inline reviews** to prevent Bugbot from leaving comments directly on code lines

    Bugbot runs for all contributors to enabled repositories, regardless of team membership.

    ### Personal settings

    Team members can override settings for their own PRs:

    * Run **only when mentioned** by commenting `cursor review` or `bugbot run`
    * Run **only once** per PR, skipping subsequent commits
    * **Enable reviews on draft PRs** to include draft pull requests in automatic reviews
  </Tab>
</Tabs>

### Analytics

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=0b09bc0e61d1c92017c3ca42957c70e1" alt="Bugbot dashboard" data-og-width="1832" width="1832" data-og-height="2022" height="2022" data-path="images/bugbot/bugbot-dashboard.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=fe3c6151118fa404a0a5a100968649cf 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=7a602dfdaa6f737dc6d5010ea90a74b8 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=6a21a6cb4b32248fb2b8cbea9afb8bcc 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=27df9beda1ee9efc84e6f2c339ff1076 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=80cb6507ca96d1c2aa74bcc30170b517 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ce35818f10c462b16b2d697519557019 2500w" />
</Frame>

## Rules

Create `.cursor/BUGBOT.md` files to provide project-specific context for reviews. Bugbot always includes the root `.cursor/BUGBOT.md` file and any additional files found while traversing upward from changed files.

```
project/
  .cursor/BUGBOT.md          # Always included (project-wide rules)
  backend/
    .cursor/BUGBOT.md        # Included when reviewing backend files
    api/
      .cursor/BUGBOT.md      # Included when reviewing API files
  frontend/
    .cursor/BUGBOT.md        # Included when reviewing frontend files
```

<AccordionGroup>
  <Accordion title="Example .cursor/BUGBOT.md">
    ```markdown  theme={null}
    # Project review guidelines

    ## Security focus areas

    - Validate user input in API endpoints
    - Check for SQL injection vulnerabilities in database queries
    - Ensure proper authentication on protected routes

    ## Architecture patterns

    - Use dependency injection for services
    - Follow the repository pattern for data access
    - Implement proper error handling with custom error classes

    ## Common issues

    - Memory leaks in React components (check useEffect cleanup)
    - Missing error boundaries in UI components
    - Inconsistent naming conventions (use camelCase for functions)

    ```
  </Accordion>
</AccordionGroup>

## Pricing

Bugbot offers two tiers: **Free** and **Pro**.

### Free tier

Every user gets a limited number of free PR reviews each month. For teams, each team member gets their own free reviews. When you reach the limit, reviews pause until your next billing cycle. You can upgrade anytime to the 14‑day free Pro trial for unlimited reviews.

### Pro tier

<Tabs defaultValue="Teams">
  <Tab title="Individuals">
    ### Flat rate

    \$40 per month for unlimited Bugbot reviews on up to 200 PRs per month across all repositories.

    ### Getting started

    Subscribe through your account settings.
  </Tab>

  <Tab title="Teams">
    ### Per-user billing

    Teams pay \$40 per user per month for unlimited reviews.

    We count a user as someone who authored PRs reviewed by Bugbot in a month.

    All licenses are relinquished at the start of each billing cycle, and will be assigned out on a first-come, first-served basis. If a user doesn't author any PRs reviewed by Bugbot in a month, the seat can be used by another user.

    ### Seat limits

    Team admins can set maximum Bugbot seats per month to control costs.

    ### Getting started

    Subscribe through your team dashboard to enable billing.

    ### Abuse guardrails

    In order to prevent abuse, we have a pooled cap of 200 pull requests per month for every Bugbot license. If you need more than 200 pull requests per month, please contact us at [hi@cursor.com](mailto:hi@cursor.com) and we'll be happy to help you out.

    For example, if your team has 100 users, your organization will initially be able to review 20,000 pull requests per month. If you reach that limit naturally, please reach out to us and we'll be happy to increase the limit.
  </Tab>
</Tabs>

## Troubleshooting

If Bugbot isn't working:

1. **Enable verbose mode** by commenting `cursor review verbose=true` or `bugbot run verbose=true` for detailed logs and request ID
2. **Check permissions** to verify Bugbot has repository access
3. **Verify installation** to confirm the GitHub app is installed and enabled

Include the request ID from verbose mode when reporting issues.

## FAQ

<AccordionGroup>
  <Accordion title="Is Bugbot privacy-mode compliant?">
    Yes, Bugbot follows the same privacy compliance as Cursor and processes data identically to other Cursor requests.
  </Accordion>

  <Accordion title="What happens when I hit the free tier limit?">
    When you reach your monthly free tier limit, Bugbot reviews pause until your next billing cycle. You can upgrade to the 14‑day free Pro trial for unlimited reviews (subject to standard abuse guardrails).
  </Accordion>
</AccordionGroup>

```
```

---

← Previous: [Web & Mobile](./web-mobile.md) | [Index](./index.md) | Next: [Code Review](./code-review.md) →