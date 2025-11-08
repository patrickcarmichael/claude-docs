---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

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

>   **⚠️ Warning**
>
> You will have to re-enter your API key every time you make a new Google Sheet

### Enter your first prompt

There are two main functions you can use to call Claude using Claude for Sheets. For now, let's use `CLAUDE()`.

<Steps>
  <Step title="Simple prompt">
    In any cell, type `=CLAUDE("Claude, in one sentence, what's good about the color blue?")`

    > Claude should respond with an answer. You will know the prompt is processing because the cell will say `Loading...`
  </Step>

  <Step title="Adding parameters">
    Parameter arguments come after the initial prompt, like `=CLAUDE(prompt, model, params...)`.
    >   **📝 Note**
>
> `model` is always second in the list.

    Now type in any cell `=CLAUDE("Hi, Claude!", "claude-3-haiku-20240307", "max_tokens", 3)`

    Any [API parameter](/en/api/messages) can be set this way. You can even pass in an API key to be used just for this specific cell, like this:  `"api_key", "sk-ant-api03-j1W..."`
  </Step>
</Steps>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
