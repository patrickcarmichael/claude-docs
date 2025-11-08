**Navigation:** ← Previous | [Index](./index.md) | [Next →](./02-adding-sdk-examples.md)

# AI-native
Source: https://mintlify.com/docs/ai-native

Learn how AI enhances reading, writing, and discovering your documentation

When you host your documentation on Mintlify, built-in AI features help your users find answers and your team maintain content more efficiently. Your content provides the context for these AI-native features to improve the experiences of reading, writing, and discovering your documentation.


## What makes your documentation AI-native

### Reading

In addition to reading individual pages, users can chat with the [assistant](/ai/assistant) in your documentation for immediate answers to their questions and links to relevant content. The assistant helps guide users through your product with accurate information from your documentation. Embed the assistant into custom apps with the [API](api-reference/assistant/create-assistant-message) to extend where users can access your documentation.

### Writing

The [agent](/ai/agent) helps you write and maintain documentation. It creates pull requests with proposed changes based on your prompts, pull requests, and Slack threads. Add the agent to your Slack workspace so that anyone on your team can help maintain your documentation by chatting with the agent. Or embed the agent into custom apps via the [API](/api-reference/agent/create-agent-job).

Configure popular tools like [Cursor](/guides/cursor), [Claude Code](/guides/claude-code), and [Windsurf](/guides/windsurf) to reference the Mintlify schema, your style guide, and best practices.

### Discovering

Your site is automatically optimized for AI tools and search engines to help users discover your documentation. All pages are sent as Markdown to AI agents instead of HTML, which helps these tools process your content faster and use fewer tokens. Every page is also available to view as Markdown by appending `.md` to the URL.

Mintlify hosts `llms.txt` and `llms-full.txt` files for your documentation. These industry-standard files help LLMs index your documentation and respond efficiently with relevant information to user queries.

Your documentation site also hosts an MCP server that lets users connect your documentation directly to their AI tools for up to date information about your product directly where they want it.

Full-text search and semantic understanding help users and AI tools find relevant information quickly. Search understands user intent rather than just matching keywords. And if a user encounters a 404 error, your site suggests related pages to help them find what they're looking for. No configuration required.


## Enable AI features

Select any of the following cards for more information.

<CardGroup cols={2}>
  <Card title="Assistant" icon="bot-message-square" href="/ai/assistant">
    Configure the assistant to search external sites or direct people to your support team if it can't answer their questions.
  </Card>

  <Card title="Agent" icon="pen-line" href="/ai/agent">
    Add the agent to your Slack workspace or embed it into custom apps to have it help write and update your documentation.
  </Card>

  <Card title="Contextual menu" icon="sparkles" href="/ai/contextual-menu">
    Add a menu to pages that lets users query AI tools, connect to your MCP server, and copy pages as context with one click.
  </Card>

  <Card title="MCP integration" icon="plug" href="/ai/model-context-protocol">
    Your site has a hosted MCP server that lets users connect your documentation directly to their AI tools. Make your users aware of your MCP server and how to connect to it.
  </Card>
</CardGroup>



# Agent
Source: https://mintlify.com/docs/ai/agent

The agent helps you write and maintain documentation

<Info>
  The agent is available on [Pro and Custom plans](https://mintlify.com/pricing?ref=agent) for anyone with access to your dashboard.
</Info>

The agent creates pull requests with proposed changes to your documentation based on your prompts. When you send a request to the agent, it references your documentation, connected repositories, and Slack messages to create content that follows technical writing best practices and adheres to the Mintlify schema. Access the agent in your Slack workspace or embed it in custom applications with the API.

Use the agent to:

* Write new content based on your prompts, links to pull requests, or Slack threads
* Revise outdated code examples and API references
* Search and update existing content
* Answer questions about your docs and technical writing topics

To get started, add the agent to your Slack workspace and mention it with `@mintlify` in a channel.


## Add the agent to your Slack workspace

<Note>
  If your Slack Workspace Owner requires admin approval to install apps, ask them to approve the Mintlify app before you connect it.
</Note>

1. Navigate to the [agent](https://dashboard.mintlify.com/products/agent) page of your dashboard.
2. Select the **Connect** button.
3. Follow the Slack prompts to add the `mintlify` app to your workspace.
4. Follow the Slack prompts to link your Mintlify account to your Slack workspace.
5. Test that the agent is working and responds when you:
   * Send a direct message to it.
   * Mention it with `@mintlify` in a channel.


## Connect repositories as context

The agent can only access repositories that you connect through the Mintlify GitHub App. Modify which repositories the agent can access in the [GitHub App settings](https://github.com/apps/mintlify/installations/new).


## Embed the agent via API

Use the agent endpoints to [create jobs](/api-reference/agent/create-agent-job), [get a specific job](/api-reference/agent/get-agent-job), and [get all jobs](/api-reference/agent/get-all-jobs).


## Write effective prompts

Think of the agent as a helpful assistant that needs your guidance to complete tasks. Give it clear instructions and context. More focused tasks are easier to complete, so break down complex projects into smaller steps.

Make your prompts specific and outcome-focused. Generic prompts like `@mintlify Improve the onboarding page` apply general best practices, but may not improve content in the specific way that you were picturing.

Try prompts based on outcomes you want your users to achieve or problems that they encounter. For example:

* `@mintlify A lot of users have trouble installing the CLI. Review the onboarding page and update the docs so that users can easily install the CLI`
* `@mintlify Developers keep getting 401 errors when following our authentication guide. Review the auth docs and add clearer examples showing how to properly format the API key`

Use broad prompts for general content maintenance like fixing typos, updating redirects, or renaming a feature throughout your docs. For example:

* `@mintlify Find and fix all typos in the docs`
* `@mintlify change all unordered lists to use * instead of -`


## Specify a subdomain

If you have multiple documentation sites with their own subdomains, include the `subdomain` parameter in your message to specify which subdomain the agent should work on.

Use the format `@mintlify subdomain=<your-subdomain> <your-prompt>` to prompt the agent to work on a specific subdomain.

Examples:

* `@mintlify subdomain=public-docs Add a new section to the quickstart about inviting collaborators based on this PR`: Prompts the agent to update the quickstart only on the `public-docs` subdomain.
* `@mintlify subdomain=customer-docs Update the auth docs for the new authentication method`: Prompts the agent to update the auth docs only on the `customer-docs` subdomain.


## Agent workflows

The agent assists with many different documentation tasks. These workflows show some of the ways you can integrate the agent into your documentation process. Try an approach that fits how your team currently works and adapt it to your specific needs.

### Iterate on a prompt in a Slack thread

Prompt the agent, then continue to mention it with `@mintlify` in the same thread to refine and iterate on the pull request that it creates.

For example: `@mintlify Our quickstart page needs a new section on inviting collaborators`. Then `@mintlify The new section should be called "Inviting collaborators"`. Followed by any other iterations.

### Start with the agent, finish manually

Prompt the agent to begin a project, then check out the branch it creates and finish the task in your local environment or the web editor. The agent can help you get started, then you can take over to complete the task.

For example: `@mintlify Update the quickstart page to include information about inviting collaborators` and then checkout the branch to make any additional changes using your preferred method.

### Update docs when merging feature changes

When you merge a feature pull request, share the PR link with the agent to update relevant docs.

For example: `@mintlify This PR adds a new authentication method. Update the docs to include the new auth flow: [PR link]`.

### Generate release notes from a pull request

Prompt the agent with a specific pull request to generate release notes or changelog updates based on the commit history.

For example: `@mintlify Generate release notes for this PR: [PR link]`.

### Generate code examples

Prompt the agent to generate code examples for features throughout your docs or on specific pages.

For example: `@mintlify Generate a code example to make the authentication method easier to understand`.

### Review existing content

Prompt the agent to review existing content for technical accuracy, style, grammar, or other issues.

For example: `@mintlify Review the API rate limiting section. We changed limits last month`.

### Respond to user feedback

Prompt the agent with feedback from your users to make focused updates to your docs.

For example: `@mintlify Users are getting confused by step 3 in the setup guide. What might be making it unclear?`.

### Automate with the API

Integrate the agent into your existing automation tools to automatically update documentation when code changes occur, trigger content reviews, or sync documentation updates across multiple repositories.

Learn how in the [Auto-update documentation when code is merged](/guides/automate-agent) tutorial.



# Assistant
Source: https://mintlify.com/docs/ai/assistant

Help users succeed with your product and find answers faster

<Info>
  The assistant is automatically enabled on [Pro and Custom plans](https://mintlify.com/pricing?ref=assistant).
</Info>


## About the assistant

The assistant answers questions about your documentation through natural language queries. It is embedded directly in your documentation site, providing users with immediate access to contextual help.

The assistant uses agentic RAG (retrieval-augmented generation) with tool calling powered by Claude Sonnet 4. When users ask questions, the assistant:

* **Searches and retrieves** relevant content from your documentation to provide accurate answers.
* **Cites sources** and provides navigable links to take users directly to referenced pages.
* **Generates copyable code examples** to help users implement solutions from your documentation.

Each message sent to the assistant counts toward your plan's message allowance. If you exceed your allowance, additional messages incur overage charges. You can set spending limits or disable the assistant if you reach your message allowance.

You can view assistant usage through your dashboard to understand user behavior and documentation effectiveness. Export and analyze query data to help identify:

* Frequently asked questions that might need better coverage.
* Content gaps where users struggle to find answers.
* Popular topics that could benefit from additional content.


## Configuring the assistant

The assistant is enabled by default for Pro and Custom plans.

Manage the assistant from your [dashboard](https://dashboard.mintlify.com/products/assistant/settings). Click **Configuration** to enable or disable the assistant, configure response handling, add default questions, and set a spend limit.

<Frame>
  <img src="https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/configuration-light.png?fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=fe584b4ff97e6e8c5d29793b49bfc1f1" alt="The assistant toolbar in the dashboard. The Configuration button is emphasized with an orange rectangle." className="block dark:hidden" data-og-width="2036" width="2036" data-og-height="426" height="426" data-path="images/assistant/configuration-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/configuration-light.png?w=280&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=64a1fef5c36972c68d8638c732e1869e 280w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/configuration-light.png?w=560&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=3e923099c726ebc87b023d10acc2b7f0 560w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/configuration-light.png?w=840&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=012442bafc2da6adff66feb70d96ea92 840w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/configuration-light.png?w=1100&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=abad747c9a14d3207cb52cf48b74372d 1100w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/configuration-light.png?w=1650&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=e335a318cb8238e84e4692a85a394bdd 1650w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/configuration-light.png?w=2500&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=2abec94076616987fd205ae8d2894419 2500w" />

  <img src="https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/configuration-dark.png?fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=10cacb17b4649fa239e5ca5bac3adbd7" alt="The assistant toolbar in the dashboard. The Configuration button is emphasized with an orange rectangle." className="hidden dark:block" data-og-width="2038" width="2038" data-og-height="428" height="428" data-path="images/assistant/configuration-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/configuration-dark.png?w=280&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=22ff0b697f2ab609de6786f938ba300b 280w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/configuration-dark.png?w=560&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=01619d849b3f10589ea8c8a93fa7e664 560w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/configuration-dark.png?w=840&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=e432bcc0a82e8ea9c4f9393e5c7da7cf 840w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/configuration-dark.png?w=1100&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=304186a00cd68dbe155670b61ca42eca 1100w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/configuration-dark.png?w=1650&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=28ce427dc69d5af9fda882f639de4b8a 1650w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/configuration-dark.png?w=2500&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=87062d8fda02cad8d0a4b604da7c7555 2500w" />
</Frame>

### Enable or disable the assistant

Toggle the assistant status to enable or disable the assistant for your documentation site.

<Frame>
  <img src="https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/status-light.png?fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=723881f19ac3ad665a774eeb6f3b8652" alt="The assistant status toggle in the dashboard." className="block dark:hidden" data-og-width="2038" width="2038" data-og-height="338" height="338" data-path="images/assistant/status-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/status-light.png?w=280&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=324018ab573007ce00dea0256aec2789 280w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/status-light.png?w=560&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=08fa6f1070c0dfc73518d184244fab09 560w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/status-light.png?w=840&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=9396ddf191ca4433612550f1a6d8aa74 840w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/status-light.png?w=1100&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=08b1fcdd73408ae3aa2d441a1ad7b370 1100w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/status-light.png?w=1650&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=210932e2ffa0ed0f37e67cee7f9f5991 1650w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/status-light.png?w=2500&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=8a9373c2ccd834e7d146b06164874a8d 2500w" />

  <img src="https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/status-dark.png?fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=8c7ae23c57d3db8f67a649b0f09d45c4" alt="The assistant status toggle in the dashboard." className="hidden dark:block" data-og-width="2040" width="2040" data-og-height="338" height="338" data-path="images/assistant/status-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/status-dark.png?w=280&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=0989add1e16e03d0f516c2d0e3271cc7 280w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/status-dark.png?w=560&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=af084192f28f689c1506a15750e50167 560w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/status-dark.png?w=840&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=7b36249ad898762cae73b78c8bc97477 840w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/status-dark.png?w=1100&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=a224b83ac59895b6ce7884c90a24842d 1100w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/status-dark.png?w=1650&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=161b1e9ac9cbf2c1b678fa59240d99cb 1650w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/status-dark.png?w=2500&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=8d5763ab56eba1c7d97c987b60b3148b 2500w" />
</Frame>

### Control placement

Select where the assistant appears on your documentation site. Choose between a floating chat bubble at the bottom of the page or a button next to the search bar.

<Frame>
  <img src="https://mintcdn.com/mintlify/Xfe-YlAgjAXFlRiK/images/assistant/placement-light.png?fit=max&auto=format&n=Xfe-YlAgjAXFlRiK&q=85&s=1c9096e678af41a9e955a005de432610" alt="The assistant placement panel in the dashboard with the bottom of page option selected." className="block dark:hidden" data-og-width="1286" width="1286" data-og-height="722" height="722" data-path="images/assistant/placement-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/Xfe-YlAgjAXFlRiK/images/assistant/placement-light.png?w=280&fit=max&auto=format&n=Xfe-YlAgjAXFlRiK&q=85&s=41f444f20d85904cbe203244f65f63ed 280w, https://mintcdn.com/mintlify/Xfe-YlAgjAXFlRiK/images/assistant/placement-light.png?w=560&fit=max&auto=format&n=Xfe-YlAgjAXFlRiK&q=85&s=d3cc4a83d63f1cfc34fa719d703be619 560w, https://mintcdn.com/mintlify/Xfe-YlAgjAXFlRiK/images/assistant/placement-light.png?w=840&fit=max&auto=format&n=Xfe-YlAgjAXFlRiK&q=85&s=8b61ff7672f6b7c0624ac556c64191d5 840w, https://mintcdn.com/mintlify/Xfe-YlAgjAXFlRiK/images/assistant/placement-light.png?w=1100&fit=max&auto=format&n=Xfe-YlAgjAXFlRiK&q=85&s=25e1a3e918859b10856c70874577d028 1100w, https://mintcdn.com/mintlify/Xfe-YlAgjAXFlRiK/images/assistant/placement-light.png?w=1650&fit=max&auto=format&n=Xfe-YlAgjAXFlRiK&q=85&s=0b6e531c88eaa99700734f14baa35a68 1650w, https://mintcdn.com/mintlify/Xfe-YlAgjAXFlRiK/images/assistant/placement-light.png?w=2500&fit=max&auto=format&n=Xfe-YlAgjAXFlRiK&q=85&s=d7afd18f3ae82099a339e951d94d3208 2500w" />

  <img src="https://mintcdn.com/mintlify/Xfe-YlAgjAXFlRiK/images/assistant/placement-dark.png?fit=max&auto=format&n=Xfe-YlAgjAXFlRiK&q=85&s=d66a9422dad7e5cdd2a8d39f353b262e" alt="The assistant placement panel in the dashboard with the bottom of page option selected." className="hidden dark:block" data-og-width="1288" width="1288" data-og-height="722" height="722" data-path="images/assistant/placement-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/Xfe-YlAgjAXFlRiK/images/assistant/placement-dark.png?w=280&fit=max&auto=format&n=Xfe-YlAgjAXFlRiK&q=85&s=419dca222b2be1a25e188cbf0d5ce3e7 280w, https://mintcdn.com/mintlify/Xfe-YlAgjAXFlRiK/images/assistant/placement-dark.png?w=560&fit=max&auto=format&n=Xfe-YlAgjAXFlRiK&q=85&s=40f493ded5f71918498f27342f4d8508 560w, https://mintcdn.com/mintlify/Xfe-YlAgjAXFlRiK/images/assistant/placement-dark.png?w=840&fit=max&auto=format&n=Xfe-YlAgjAXFlRiK&q=85&s=6c1adcee499867eabc004a5b47c6f7bf 840w, https://mintcdn.com/mintlify/Xfe-YlAgjAXFlRiK/images/assistant/placement-dark.png?w=1100&fit=max&auto=format&n=Xfe-YlAgjAXFlRiK&q=85&s=4ebd42037adba51fec88ed7b6694c77d 1100w, https://mintcdn.com/mintlify/Xfe-YlAgjAXFlRiK/images/assistant/placement-dark.png?w=1650&fit=max&auto=format&n=Xfe-YlAgjAXFlRiK&q=85&s=6bdb464911d7993b31eeeaff18f494b6 1650w, https://mintcdn.com/mintlify/Xfe-YlAgjAXFlRiK/images/assistant/placement-dark.png?w=2500&fit=max&auto=format&n=Xfe-YlAgjAXFlRiK&q=85&s=bfa3fd381854b86706e541d47fda8e35 2500w" />
</Frame>

### Set deflection email

In the response handling section, enable the assistant to redirect unanswered questions to your support team. Specify an email address that the assistant provides to users who ask questions that it cannot answer.

<Frame>
  <img src="https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/deflection-light.png?fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=f55e6cb6a0121034aa40b18decab3d80" alt="The assistant deflection panel in the dashboard. Assistant deflection is toggled on and support@mintlify.com is set as the deflection email." className="block dark:hidden" data-og-width="2040" width="2040" data-og-height="580" height="580" data-path="images/assistant/deflection-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/deflection-light.png?w=280&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=16915ff0e1fee36dd5280a50700c0679 280w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/deflection-light.png?w=560&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=1bf4fb91773e61288d13102b59f7967c 560w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/deflection-light.png?w=840&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=363811453870d3ed3f8621c31db10680 840w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/deflection-light.png?w=1100&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=dc8d8edc71f47b92673a1958b2c26c94 1100w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/deflection-light.png?w=1650&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=99f71ff3e72bdb8b3cc1048aa5d1eaad 1650w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/deflection-light.png?w=2500&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=73ee21cc525db1e1db44eff5fcda10e3 2500w" />

  <img src="https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/deflection-dark.png?fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=43b9454cd12cef2e9a0581306415de29" alt="The assistant deflection panel in the dashboard. Assistant deflection is toggled on and support@mintlify.com is set as the deflection email." className="hidden dark:block" data-og-width="2040" width="2040" data-og-height="580" height="580" data-path="images/assistant/deflection-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/deflection-dark.png?w=280&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=0b3ad456946f37175d208d0ff6e42ff4 280w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/deflection-dark.png?w=560&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=27e4cd4f334cddf9eb607f7582c3d71f 560w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/deflection-dark.png?w=840&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=83f3dc3c9eeeeb6045bcdfb3f669b8f8 840w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/deflection-dark.png?w=1100&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=fcd34d090c6be6872d07eb9bdc336f38 1100w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/deflection-dark.png?w=1650&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=eeefd70e7b15cba074bc8ea1cc57ddf3 1650w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/deflection-dark.png?w=2500&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=a0b6a7547f58a0f536cbc6b5bc64eefc 2500w" />
</Frame>

### Search sites

<Note>
  Site search is in beta. To enable it for your documentation site, [contact our sales team](mailto:gtm@mintlify.com).
</Note>

In the response handling section, configure sites that the assistant can search for additional context when answering questions.

* Sites must be publicly available.
* Sites that require JavaScript to load are not supported.

<Frame>
  <img src="https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/search-sites-light.png?fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=ac5e9756055300a5409375f139458525" alt="The assistant search sites panel in the dashboard. The assistant is configured to search the mintlify.com and mintlify.com/blog domains." className="block dark:hidden" data-og-width="1306" width="1306" data-og-height="646" height="646" data-path="images/assistant/search-sites-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/search-sites-light.png?w=280&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=d4a04fac8b69e372fe398b3f6de4f595 280w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/search-sites-light.png?w=560&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=60f6a18fe56c08e4c474eaf9ed667755 560w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/search-sites-light.png?w=840&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=616231ed12d03848e0e278573841a642 840w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/search-sites-light.png?w=1100&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=388d2e030b23d297e137eead642e9df4 1100w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/search-sites-light.png?w=1650&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=b0f0050e3b5b82aaf9949ada105ead8c 1650w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/search-sites-light.png?w=2500&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=ea5cbac86b8af316f17e270cb87ab1a6 2500w" />

  <img src="https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/search-sites-dark.png?fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=ba632460371199a921559e788f8cecc4" alt="The assistant search sites panel in the dashboard. The assistant is configured to search the mintlify.com and mintlify.com/blog domains." className="hidden dark:block" data-og-width="1306" width="1306" data-og-height="646" height="646" data-path="images/assistant/search-sites-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/search-sites-dark.png?w=280&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=017ae9b79e87eb9b74253fb9e074f65e 280w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/search-sites-dark.png?w=560&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=e3035bbdaeea85ce53a94c1c094bcb63 560w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/search-sites-dark.png?w=840&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=5893bbc5043684fe247a48b4bb25bf8b 840w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/search-sites-dark.png?w=1100&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=b211a9def9b162d07a0343466558a57d 1100w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/search-sites-dark.png?w=1650&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=3573cee1735cd9fcdbac882bcf2d3358 1650w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/search-sites-dark.png?w=2500&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=a66b9bfac0de24128fac9d09cee97169 2500w" />
</Frame>

Use the following filtering syntax for more precise control over what the assistant can search:

* **Domain-level filtering**
  * `example.com`: Search only the `example.com` domain
  * `docs.example.com`: Search only the `docs.example.com` subdomain
  * `*.example.com`: Search all subdomains of `example.com`
* **Path-level filtering**
  * `docs.example.com/api`: Search all pages under the `/api` subpath
* **Multiple patterns**
  * Add multiple entries to target different sections of sites

### Add sample questions

Help your users start questions with the assistant by adding sample questions. In the search suggestions section, add up to three sample questions.

<Frame>
  <img src="https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/search-suggestions-light.png?fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=041635b9ca52f5ba9d8d455bac8ab6a2" alt="The search suggestions panel in the dashboard. What is an OpenAPI spec? is configured as a sample question." className="block dark:hidden" data-og-width="2124" width="2124" data-og-height="590" height="590" data-path="images/assistant/search-suggestions-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/search-suggestions-light.png?w=280&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=f0635e2a6b66cd6c3efffba22d4fe7ab 280w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/search-suggestions-light.png?w=560&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=d66d8295a95de0438c498b8be9da8c35 560w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/search-suggestions-light.png?w=840&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=08405d14a248ab8120d80d0ef9d08cc2 840w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/search-suggestions-light.png?w=1100&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=500e195bfb0521fe75ad53c39dae2173 1100w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/search-suggestions-light.png?w=1650&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=03afbb9113290cf83279e93097a8b206 1650w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/search-suggestions-light.png?w=2500&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=06ceb1f0c6cfbedc2f3a1aff52c44ca9 2500w" />

  <img src="https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/search-suggestions-dark.png?fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=2fd18a1f2903ee2c5fa7303da0de20ca" alt="The search suggestions panel in the dashboard. What is an OpenAPI spec? is configured as a sample question." className="hidden dark:block" data-og-width="2124" width="2124" data-og-height="590" height="590" data-path="images/assistant/search-suggestions-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/search-suggestions-dark.png?w=280&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=837a22d5297e8207d200a48b1e2a8a37 280w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/search-suggestions-dark.png?w=560&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=a4bbf62a48aa3fce5535b111f238a11e 560w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/search-suggestions-dark.png?w=840&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=cb17a1ba40c2314ffb0f8b04078096e1 840w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/search-suggestions-dark.png?w=1100&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=dd01fd42636530007d9a59c98d511888 1100w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/search-suggestions-dark.png?w=1650&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=59405cd8603fec23bce2c0a1ef1c0271 1650w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/search-suggestions-dark.png?w=2500&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=8d4c755afa8cf0309be2dcacf73a4b6e 2500w" />
</Frame>

### Set a spend limit

Set a spend limit to control what happens if you reach your message allowance. By default, the assistant continues to answer user questions after you reach your message allowance, which incurs overages.

When you reach your spend limit, the assistant is disabled until your message allowance resets.

1. Select the **Billing** tab.

<Frame>
  <img src="https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/billing-light.png?fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=0dc4a1790633a9030a591a8e0d161be1" alt="The billing tab on the Assistant Configurations page. The Billing tab is emphasized with an orange rectangle." className="block dark:hidden" style={{ width: '268px', height: 'auto' }} data-og-width="582" width="582" data-og-height="328" height="328" data-path="images/assistant/billing-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/billing-light.png?w=280&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=e8b29e941cc3a88f382936f7747d5427 280w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/billing-light.png?w=560&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=2e6dc3b3c7326f0ea044d8069644fc83 560w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/billing-light.png?w=840&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=cd487a27d9513131d97db962234c8037 840w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/billing-light.png?w=1100&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=872a48286f46c43c610a3f8ed0ba3a2c 1100w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/billing-light.png?w=1650&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=b9d40bbe961b268ad82a605d58f3437b 1650w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/billing-light.png?w=2500&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=5901c45abeb2b040c4f5e7c3cfece8cf 2500w" />

  <img src="https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/billing-dark.png?fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=2a349bae7a1ee7b77cbbc74ee1c196e8" alt="The billing tab on the Assistant Configurations page. The Billing tab is emphasized with an orange rectangle." className="hidden dark:block" style={{ width: '268px', height: 'auto' }} data-og-width="584" width="584" data-og-height="328" height="328" data-path="images/assistant/billing-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/billing-dark.png?w=280&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=acd35de0eb0b3fef80ab437b491c8130 280w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/billing-dark.png?w=560&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=ac38d561c95a35fc09dbe85cc93e594a 560w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/billing-dark.png?w=840&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=dbff6409b9ea72020b78d29f077b8e16 840w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/billing-dark.png?w=1100&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=beb9ced921d14262a7c0c39515d51c90 1100w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/billing-dark.png?w=1650&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=b63243de39c13727b3c68961cb05cf49 1650w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/billing-dark.png?w=2500&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=59cf70b9e8a37bf8b8d87c00e98b3809 2500w" />
</Frame>

2. Set a spend limit for assistant messages beyond your allowance.
3. Set usage alerts to receive an email when you reach a certain percentage of your spend limit.


## Using the assistant

Users can access the assistant in three ways:

* **Keyboard shortcut**: <kbd>Command</kbd> + <kbd>I</kbd> (<kbd>Ctrl</kbd> + <kbd>I</kbd> on Windows)
* **Assistant button** next to the search bar
  <img
    src="https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/assistant/assistant-button-light.png?fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=716582bc54eaea73cb53d26b36a74fb4"
    className="block dark:hidden rounded-2xl border border-gray-100 shadow-lg"
    style={{
    width: '268px',
    height: 'auto',
  }}
    alt="Search bar and assistant button in light mode."
    data-og-width="1806"
    width="1806"
    data-og-height="322"
    height="322"
    data-path="images/assistant/assistant-button-light.png"
    data-optimize="true"
    data-opv="3"
    srcset="https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/assistant/assistant-button-light.png?w=280&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=9ae2bace996e8301def4d07a3151764b 280w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/assistant/assistant-button-light.png?w=560&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=70cde876f7f7ee59c07594108203c93c 560w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/assistant/assistant-button-light.png?w=840&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=95f1633b5e41b8b279a8923f7a1fa075 840w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/assistant/assistant-button-light.png?w=1100&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=11b8f8f14bdeb252e9ba07d622834146 1100w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/assistant/assistant-button-light.png?w=1650&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=b2c08d4d0573c75a3493e6dfd282dd56 1650w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/assistant/assistant-button-light.png?w=2500&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=fc092ff8b664ce5842067bca8bd531c7 2500w"
  />
  <img
    src="https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/assistant/assistant-button-dark.png?fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=34096a771f492853e59eef654567b081"
    className="hidden dark:block rounded-2xl border border-white/10 shadow-lg"
    style={{
    width: '268px',
    height: 'auto',
  }}
    alt="Search bar and assistant button in dark mode."
    data-og-width="1806"
    width="1806"
    data-og-height="324"
    height="324"
    data-path="images/assistant/assistant-button-dark.png"
    data-optimize="true"
    data-opv="3"
    srcset="https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/assistant/assistant-button-dark.png?w=280&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=1b8226b14933399c53d7975e02ad7d9d 280w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/assistant/assistant-button-dark.png?w=560&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=400dff40f5e394fd2d85a52066592e26 560w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/assistant/assistant-button-dark.png?w=840&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=00d387ddc8a0336bbac7e21b1130dfa1 840w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/assistant/assistant-button-dark.png?w=1100&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=860463b82aa2db420d87af6138c61e66 1100w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/assistant/assistant-button-dark.png?w=1650&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=0c15a237b868f23fad34f7838bdc3579 1650w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/assistant/assistant-button-dark.png?w=2500&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=1e88586f53b4f6f07b8336a77f0f940f 2500w"
  />
* **URLs** with `?assistant=open` appended open the assistant when the page loads. For example, [https://mintlify.com/docs?assistant=open](https://mintlify.com/docs?assistant=open).

Each method opens a chat panel on the right side of your docs. Users can ask any question and the assistant searches your documentation for an answer. If no relevant information is found, the assistant responds that it cannot answer the question.


## Making content AI ingestible

Structure your documentation to help the assistant provide accurate, relevant answers. Clear organization and comprehensive context benefit both human readers and AI understanding.

<Card title="Structure and organization">
  * Use semantic markup.
  * Write descriptive headings for sections.
  * Create a logical information hierarchy.
  * Use consistent formatting across your docs.
  * Include comprehensive metadata in page frontmatter.
  * Break up long blocks of text into shorter paragraphs.
</Card>

<Card title="Context">
  * Define specific terms and acronyms when first introduced.
  * Provide sufficient conceptual content about features and procedures.
  * Include examples and use cases.
  * Cross-reference related topics.
  * Add [hidden pages](/organize/hidden-pages) with additional context that users don't need, but the assistant can reference.
</Card>


## Exporting and analyzing queries

Review and export queries from your dashboard to understand how people interact with your documentation and identify improvement opportunities. Some ways that analyzing queries can help you improve your documentation:

* Identify content gaps where frequent queries receive insufficient answers.
* Discover user behavior patterns and common information needs from themes and patterns in queries.
* Prioritize high-traffic pages for accuracy and quality improvements.

You can explore queries from your [dashboard](https://dashboard.mintlify.com/products/assistant), but to get more powerful insights we recommend exporting a `CSV` file of your queries, responses, and sources to analyze with your preferred AI tool.

1. Navigate to the [assistant page](https://dashboard.mintlify.com/products/assistant) in your dashboard.
2. Select **Export to CSV**.
3. Analyze the exported data using your preferred tool.

<Card title="Sample analysis prompts">
  * Summarize the most common themes of the queries.
  * List any queries that had no sources cited.
  * Find patterns in unsuccessful interactions.
</Card>


## Assistant insights

Use assistant insights to understand how users interact with your documentation through two views: categories and chat history.

### Categories

The categories tab uses LLMs to automatically categorize conversations by question topic and theme. Conversations are organized by the most common groupings, helping you quickly identify:

* Which topics generate the most questions
* Patterns in user needs and behavior
* Areas where documentation might need expansion or clarification

Review categories to see what areas of your documentation people frequently ask about and check that you have sufficient coverage of those topics.

### Chat history

The chat history tab displays chronological records of all assistant conversations. Select any message to view the complete chat thread, including the user's question, the assistant's response, and any sources cited.


## Troubleshooting

<Accordion title="Assistant chat bar not visible">
  If the assistant UI is not visible in specific browsers, you may need to submit a false positive report to [EasyList](https://easylist.to). Browsers that use the EasyList Cookies List like Brave and Comet sometimes block the assistant or other UI elements. The EasyList Cookies List includes a domain-specific rule that hides fixed elements on certain domains to block cookie banners. This rule inadvertently affects legitimate UI components.

  Submit a false positive report to [EasyList](https://github.com/easylist/easylist) to request removal of the rule. This resolves the issue for all users once the filter list is updated.
</Accordion>



# Contextual menu
Source: https://mintlify.com/docs/ai/contextual-menu

Add one-click AI integrations to your docs

export const PreviewButton = ({children, href}) => {
  return <a href={href} className="text-sm font-medium text-white dark:!text-zinc-950 bg-zinc-900 hover:bg-zinc-700 dark:bg-zinc-100 hover:dark:bg-zinc-300 rounded-full px-3.5 py-1.5 not-prose">
        {children}
      </a>;
};

The contextual menu provides quick access to AI-optimized content and direct integrations with popular AI tools. When users select the contextual menu on any page, they can copy content as context for AI tools or open conversations in ChatGPT, Claude, Perplexity, or a custom tool of your choice with your documentation already loaded as context.


## Menu options

The contextual menu includes several pre-built options that you can enable by adding their identifier to your configuration.

| Option                  | Identifier   | Description                                                              |
| :---------------------- | :----------- | :----------------------------------------------------------------------- |
| **Copy page**           | `copy`       | Copies the current page as Markdown for pasting as context into AI tools |
| **View as Markdown**    | `view`       | Opens the current page as Markdown                                       |
| **Open in ChatGPT**     | `chatgpt`    | Creates a ChatGPT conversation with the current page as context          |
| **Open in Claude**      | `claude`     | Creates a Claude conversation with the current page as context           |
| **Open in Perplexity**  | `perplexity` | Creates a Perplexity conversation with the current page as context       |
| **Copy MCP server URL** | `mcp`        | Copies your MCP server URL to the clipboard                              |
| **Connect to Cursor**   | `cursor`     | Installs your hosted MCP server in Cursor                                |
| **Connect to VS Code**  | `vscode`     | Installs your hosted MCP server in VS Code                               |
| **Custom options**      | Object       | Add custom options to the contextual menu                                |

<Frame>
  <img src="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/contextual-menu/contextual-menu.png?fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=b37c2bfffdc0db86422a7f7e692adaf7" alt="The expanded contextual menu showing the Copy page, View as Markdown, Open in ChatGPT, and Open in Claude menu items." data-og-width="1396" width="1396" data-og-height="944" height="944" data-path="images/contextual-menu/contextual-menu.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/contextual-menu/contextual-menu.png?w=280&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=1e033f7657ae1505264c11d2c2fdad75 280w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/contextual-menu/contextual-menu.png?w=560&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=7524bf8f46f496c49be56602b2baaab5 560w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/contextual-menu/contextual-menu.png?w=840&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=baac511161b31c496e0e6247a2264dc2 840w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/contextual-menu/contextual-menu.png?w=1100&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=5eb1a550221b48cc99d2a9b39d49f715 1100w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/contextual-menu/contextual-menu.png?w=1650&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=e1a176c05eda0b2ebcba63d57631a57e 1650w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/contextual-menu/contextual-menu.png?w=2500&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=afe09bdac8c5f388deb1e0cc2ff423f0 2500w" />
</Frame>


## Enabling the contextual menu

Add the `contextual` field to your `docs.json` file and specify which options you want to include.

```json  theme={null}
{
 "contextual": {
   "options": [
     "copy",
     "view",
     "chatgpt",
     "claude",
     "perplexity",
     "mcp",
     "cursor",
     "vscode"
   ]
 }
}
```


## Adding custom options

Create custom options in the contextual menu by adding an object to the `options` array. Each custom option requires these properties:

<ResponseField name="title" type="string" required>
  The title of the option.
</ResponseField>

<ResponseField name="description" type="string" required>
  The description of the option. Displayed beneath the title when the contextual menu is expanded.
</ResponseField>

<ResponseField name="icon" type="string" required>
  The icon to display.

  Options:

  * [Font Awesome icon](https://fontawesome.com/icons) name
  * [Lucide icon](https://lucide.dev/icons) name
  * JSX-compatible SVG code wrapped in curly braces
  * URL to an externally hosted icon
  * Path to an icon file in your project

  For custom SVG icons:

  1. Convert your SVG using the [SVGR converter](https://react-svgr.com/playground/).
  2. Paste your SVG code into the SVG input field.
  3. Copy the complete `<svg>...</svg>` element from the JSX output field.
  4. Wrap the JSX-compatible SVG code in curly braces: `icon={<svg ...> ... </svg>}`.
  5. Adjust `height` and `width` as needed.
</ResponseField>

<ResponseField name="iconType" type="string">
  The [Font Awesome](https://fontawesome.com/icons) icon style. Only used with Font Awesome icons.

  Options: `regular`, `solid`, `light`, `thin`, `sharp-solid`, `duotone`, `brands`.
</ResponseField>

<ResponseField name="href" type="string | object" required>
  The href of the option. Use a string for simple links or an object for dynamic links with query parameters.

  <Expandable title="href object">
    <ResponseField name="base" type="string" required>
      The base URL for the option.
    </ResponseField>

    <ResponseField name="query" type="object" required>
      The query parameters for the option.

      <Expandable title="query object">
        <ResponseField name="key" type="string" required>
          The query parameter key.
        </ResponseField>

        <ResponseField name="value" type="string" required>
          The query parameter value. We will replace the following placeholders with the corresponding values:

          * Use `$page` to insert the current page content in Markdown.
          * Use `$path` to insert the current page path.
          * Use `$mcp` to insert the hosted MCP server URL.
        </ResponseField>
      </Expandable>
    </ResponseField>
  </Expandable>
</ResponseField>

Example custom option:

```json {9-14} wrap theme={null}
{
    "contextual": {
        "options": [
            "copy",
            "view",
            "chatgpt",
            "claude",
            "perplexity",
            {
                "title": "Request a feature",
                "description": "Join the discussion on GitHub to request a new feature",
                "icon": "plus",
                "href": "https://github.com/orgs/mintlify/discussions/categories/feature-requests"
            }
        ]
    }
}
```

### Custom option examples

<AccordionGroup>
  <Accordion title="Simple link">
    ```json  theme={null}
    {
      "title": "Request a feature",
      "description": "Join the discussion on GitHub",
      "icon": "plus",
      "href": "https://github.com/orgs/mintlify/discussions/categories/feature-requests"
    }
    ```
  </Accordion>

  <Accordion title="Dynamic link with page content">
    ```json  theme={null}
    {
      "title": "Share on X",
      "description": "Share this page on X",
      "icon": "x",
      "href": {
        "base": "https://x.com/intent/tweet",
        "query": [
          {
          "key": "text",
          "value": "Check out this documentation: $page"
          }
        ]
      }
    }
    ```
  </Accordion>
</AccordionGroup>



# llms.txt
Source: https://mintlify.com/docs/ai/llmstxt

Make your content easier for LLMs to read and index

export const PreviewButton = ({children, href}) => {
  return <a href={href} className="text-sm font-medium text-white dark:!text-zinc-950 bg-zinc-900 hover:bg-zinc-700 dark:bg-zinc-100 hover:dark:bg-zinc-300 rounded-full px-3.5 py-1.5 not-prose">
        {children}
      </a>;
};

The [llms.txt file](https://llmstxt.org) is an industry standard that helps LLMs index content more efficiently, similar to how a sitemap helps search engines. AI tools can use this file to understand your documentation structure and find content relevant to user queries.

Mintlify automatically hosts an `llms.txt` file at the root of your project that lists all available pages in your documentation. This file is always up to date and requires zero maintenance. You can optionally add a custom `llms.txt` file to the root of your project.

View your `llms.txt` by appending `/llms.txt` to your documentation site's URL.

<PreviewButton href="https://mintlify.com/docs/llms.txt">Open the llms.txt for this site.</PreviewButton>


## llms.txt structure

An `llms.txt` file is a plain Markdown file that contains:

* **Site title** as an H1 heading.
* **Structured content sections** with links and a description of each page in your documentation.

Pages are listed alphabetically in the order they appear in your repository, starting from the root directory.

Each page's description comes from the `description` field in its frontmatter. Pages without a `description` field appear in the `llms.txt` file without a description.

```mdx Example llms.txt theme={null}

# Site title


## Docs

- [API](https://example.com/docs/api): Endpoint list and usage
- [Install](https://example.com/docs/install): Setup steps
- [Getting started](https://example.com/docs/start): Intro guide
```

This structured approach allows LLMs to efficiently process your documentation at a high level and locate relevant content for user queries, improving the accuracy and speed of AI-assisted documentation searches.


## llms-full.txt

The `llms-full.txt` file combines your entire documentation site into a single file as context for AI tools and is indexed by LLM traffic.

Mintlify automatically hosts an `llms-full.txt` file at the root of your project. View your `llms-full.txt` by appending `/llms-full.txt` to your documentation site's URL.

<PreviewButton href="https://mintlify.com/docs/llms-full.txt">Open the llms-full.txt for this site.</PreviewButton>


## Custom files

To add a custom `llms.txt` or `llms-full.txt` file, create an `llms.txt` or `llms-full.txt` file at the root of your project. Adding a custom file will override the automatically generated file of the same name. If you delete a custom file, the default file will be used again.

Your custom `llms.txt` or `llms-full.txt` file must have a site title as an H1 heading. Other content is optional. See [Format](https://llmstxt.org/#format) in the `llms.txt` specification for more information on optional sections and best practices.



# Markdown export
Source: https://mintlify.com/docs/ai/markdown-export

Quickly get Markdown versions of pages

export const PreviewButton = ({children, href}) => {
  return <a href={href} className="text-sm font-medium text-white dark:!text-zinc-950 bg-zinc-900 hover:bg-zinc-700 dark:bg-zinc-100 hover:dark:bg-zinc-300 rounded-full px-3.5 py-1.5 not-prose">
        {children}
      </a>;
};

Markdown provides structured text that AI tools can process more efficiently than HTML, which results in better response accuracy, faster processing times, and lower token usage.

Mintlify automatically generates Markdown versions of pages that are optimized for AI tools and external integrations.


## .md URL extension

Add `.md` to any page's URL to view a Markdown version.

<PreviewButton href="https://mintlify.com/docs/ai/markdown-export.md">Open this page as Markdown</PreviewButton>


## Keyboard shortcut

Press <kbd>Command</kbd> + <kbd>C</kbd> (<kbd>Ctrl</kbd> + <kbd>C</kbd> on Windows) to copy a page as Markdown to your clipboard.



# Model Context Protocol
Source: https://mintlify.com/docs/ai/model-context-protocol

Let users access your docs and APIs through their favorite AI tools

export const PreviewButton = ({children, href}) => {
  return <a href={href} className="text-sm font-medium text-white dark:!text-zinc-950 bg-zinc-900 hover:bg-zinc-700 dark:bg-zinc-100 hover:dark:bg-zinc-300 rounded-full px-3.5 py-1.5 not-prose">
        {children}
      </a>;
};


## About MCP servers

The Model Context Protocol (MCP) is an open protocol that creates standardized connections between AI applications and external services, like documentation. Mintlify generates an MCP server from your documentation and OpenAPI specifications, preparing your content for the broader AI ecosystem where any MCP client (like Claude, Cursor, Goose, and others) can connect to your documentation and APIs.

Your MCP server exposes tools for AI applications to search your documentation and interact with your APIs.


## Accessing your MCP server

<Note>
  MCP servers can only be generated for public documentation. Documentation behind end-user authentication cannot be accessed for server generation.
</Note>

Mintlify automatically generates an MCP server for your documentation and hosts it at your documentation URL with the `/mcp` path. For example, Mintlify's MCP server is available at `https://mintlify.com/docs/mcp`.

You can see and copy your MCP server URL in your [dashboard](https://dashboard.mintlify.com/products/mcp).

The `/mcp` path is reserved for hosted MCP servers and cannot be used for other navigation elements.


## Configuring your MCP server

All MCP servers include the `search` tool by default, which allows users to query information from your docs in other tools.

If you have a [Pro or Enterprise plan](https://mintlify.com/pricing?ref=mcp), you can expose endpoints from your OpenAPI specification as MCP tools.

To expose endpoints as MCP tools, use the `mcp` object within the `x-mint` extension at either the file or endpoint level. For example, the Mintlify MCP server includes tools to create assistant chats, get status updates, and trigger updates.

MCP servers follow a security-first approach where API endpoints are not exposed by default. You must explicitly enable endpoints to make them available as MCP tools. Only expose endpoints that are safe for public access through AI tools.

<ResponseField name="mcp" type="object">
  The MCP configuration for the endpoint.

  <Expandable title="MCP">
    <ResponseField name="enabled" type="boolean">
      Whether to expose the endpoint as an MCP tool. Takes precedence over the file-level configuration.
    </ResponseField>

    <ResponseField name="name" type="string">
      The name of the MCP tool.
    </ResponseField>

    <ResponseField name="description" type="string">
      The description of the MCP tool.
    </ResponseField>
  </Expandable>
</ResponseField>

### File-level configuration

Enable MCP for all endpoints by default in an OpenAPI specification file and selectively exclude endpoints:

```json  theme={null}
{
  "openapi": "3.1.0",
  "x-mint": {
    "mcp": {
      "enabled": true
    }
  },
  // ...
  "paths": {
    "/api/v1/users": {
      "get": {
        "x-mint": {
          "mcp": {
            "enabled": false // Disables MCP for this endpoint
          }
        },
        // ...
      }
    }
  }
}
```

### Endpoint-level configuration

Enable MCP for specific endpoints:

```json  theme={null}
{
  "paths": {
    "/api/v1/users": {
      "get": {
        "x-mint": {
          "mcp": {
            "enabled": true,
            "name": "get-users",
            "description": "Get a list of users"
          },
          // ...
        }
      }
    },
    "/api/v1/delete": {
      "delete": {
        // No `x-mint: mcp` so this endpoint is not exposed as an MCP tool
        // ...
      }
    }
  }
}
```


## Using your MCP server

Your users must connect your MCP server to their preferred AI tools.

1. Make your MCP server URL publicly available.
2. Users copy your MCP server URL and add it to their tools.
3. Users access your documentation and API endpoints through their tools.

These are some of the ways you can help your users connect to your MCP server:

<Tabs>
  <Tab title="Contextual menu">
    Add options in the [contextual menu](/ai/contextual-menu) for your users to connect to your MCP server from any page of your documentation.

    | Option                  | Identifier | Description                                         |
    | :---------------------- | :--------- | :-------------------------------------------------- |
    | **Copy MCP server URL** | `mcp`      | Copies your MCP server URL to the user's clipboard. |
    | **Connect to Cursor**   | `cursor`   | Installs your MCP server in Cursor.                 |
    | **Connect to VS Code**  | `vscode`   | Installs your MCP server in VS Code.                |
  </Tab>

  <Tab title="Claude">
    <Steps>
      <Step title="Get your MCP server URL.">
        Navigate to your [dashboard](https://dashboard.mintlify.com/products/mcp) and find your MCP server URL.
      </Step>

      <Step title="Publish your MCP server URL for your users.">
        Create a guide for your users that includes your MCP server URL and the steps to connect it to Claude.

        1. Navigate to the [Connectors](https://claude.ai/settings/connectors) page in the Claude settings.
        2. Select **Add custom connector**.
        3. Add your MCP server name and URL.
        4. Select **Add**.
        5. When using Claude, select the attachments button (the plus icon).
        6. Select your MCP server.
      </Step>
    </Steps>

    See the [Model Context Protocol documentation](https://modelcontextprotocol.io/docs/tutorials/use-remote-mcp-server#connecting-to-a-remote-mcp-server) for more details.
  </Tab>

  <Tab title="Claude Code">
    <Steps>
      <Step title="Get your MCP server URL.">
        Navigate to your [dashboard](https://dashboard.mintlify.com/products/mcp) and find your MCP server URL.
      </Step>

      <Step title="Publish your MCP server URL for your users.">
        Create a guide for your users that includes your MCP server URL and the command to connect it to Claude Code.

        ```bash  theme={null}
        claude mcp add --transport http <name> <url>
        ```
      </Step>
    </Steps>

    See the [Claude Code documentation](https://docs.anthropic.com/en/docs/claude-code/mcp#installing-mcp-servers) for more details.
  </Tab>

  <Tab title="Cursor">
    <Steps>
      <Step title="Get your MCP server URL.">
        Navigate to your [dashboard](https://dashboard.mintlify.com/products/mcp) and find your MCP server URL.
      </Step>

      <Step title="Publish your MCP server URL for your users.">
        Create a guide for your users that includes your MCP server URL and the steps to connect it to Cursor.

        1. Use <kbd>Command</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd> (<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd> on Windows) to open the command palette.
        2. Search for "Open MCP settings".
        3. Select **Add custom MCP**. This will open the `mcp.json` file.
        4. In `mcp.json`, configure your server:

        ```json  theme={null}
        {
          "mcpServers": {
            "<your-mcp-server-name>": {
              "url": "<your-mcp-server-url>"
            }
          }
        }
        ```
      </Step>
    </Steps>

    See the [Cursor documentation](https://docs.cursor.com/en/context/mcp#installing-mcp-servers) for more details.
  </Tab>

  <Tab title="VS Code">
    <Steps>
      <Step title="Get your MCP server URL.">
        Navigate to your [dashboard](https://dashboard.mintlify.com/products/mcp) and find your MCP server URL.
      </Step>

      <Step title="Publish your MCP server URL for your users.">
        Create a guide for your users that includes your MCP server URL and the steps to connect it to VS Code.

        1. Create a `.vscode/mcp.json` file.
        2. In `mcp.json`, configure your server:

        ```json  theme={null}
        {
          "servers": {
            "<your-mcp-server-name>": {
              "type": "http",
              "url": "<your-mcp-server-url>"
            }
          }
        }
        ```
      </Step>
    </Steps>

    See the [VS Code documentation](https://code.visualstudio.com/docs/copilot/chat/mcp-servers) for more details.
  </Tab>
</Tabs>

### Example: Connecting to the Mintlify MCP server

Connect to the Mintlify MCP server to interact with the Mintlify API and search our documentation. This will give you more accurate answers about how to use Mintlify in your local environment and demonstrates how you can help your users connect to your MCP server.

<Tabs>
  <Tab title="Contextual menu">
    At the top of this page, select the contextual menu and choose **Connect to Cursor** or **Connect to VS Code** to connect the Mintlify MCP server to the IDE of your choice.
  </Tab>

  <Tab title="Claude">
    To use the Mintlify MCP server with Claude:

    <Steps>
      <Step title="Add the Mintlify MCP server to Claude">
        1. Navigate to the [Connectors](https://claude.ai/settings/connectors) page in the Claude settings.
        2. Select **Add custom connector**.
        3. Add the Mintlify MCP server:

        * Name: `Mintlify`
        * URL: `https://mintlify.com/docs/mcp`

        4. Select **Add**.
      </Step>

      <Step title="Access the MCP server in your chat">
        1. When using Claude, select the attachments button (the plus icon).
        2. Select the Mintlify MCP server.
        3. Ask Claude a question about Mintlify.
      </Step>
    </Steps>

    See the [Model Context Protocol documentation](https://modelcontextprotocol.io/docs/tutorials/use-remote-mcp-server#connecting-to-a-remote-mcp-server) for more details.
  </Tab>

  <Tab title="Claude Code">
    To use the Mintlify MCP server with Claude Code, run the following command:

    ```bash  theme={null}
    claude mcp add --transport http Mintlify https://mintlify.com/docs/mcp
    ```

    Test the connection by running:

    ```bash  theme={null}
    claude mcp list
    ```

    See the [Claude Code documentation](https://docs.anthropic.com/en/docs/claude-code/mcp#installing-mcp-servers) for more details.
  </Tab>

  <Tab title="Cursor">
    <PreviewButton href="cursor://anysphere.cursor-deeplink/mcp/install?name=mintlify&config=eyJ1cmwiOiJodHRwczovL21pbnRsaWZ5LmNvbS9kb2NzL21jcCJ9">Install in Cursor</PreviewButton>

    To connect the Mintlify MCP server to Cursor, click the **Install in Cursor** button. Or to manually connect the MCP server, follow these steps:

    <Steps>
      <Step title="Open MCP settings">
        1. Use <kbd>Command</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd> (<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd> on Windows) to open the command palette.
        2. Search for "Open MCP settings".
        3. Select **Add custom MCP**. This will open the `mcp.json` file.
      </Step>

      <Step title="Configure the Mintlify MCP server">
        In `mcp.json`, add:

        ```json  theme={null}
        {
          "mcpServers": {
            "Mintlify": {
              "url": "https://mintlify.com/docs/mcp"
            }
          }
        }
        ```
      </Step>

      <Step title="Test the connection">
        In Cursor's chat, ask "What tools do you have available?" Cursor should show the Mintlify MCP server as an available tool.
      </Step>
    </Steps>

    See [Installing MCP servers](https://docs.cursor.com/en/context/mcp#installing-mcp-servers) in the Cursor documentation for more details.
  </Tab>

  <Tab title="VS Code">
    <PreviewButton href="https://vscode.dev/redirect/mcp/install?name=mintlify&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Fmintlify.com%2Fdocs%2Fmcp%22%7D">Install in VS Code</PreviewButton>

    To connect the Mintlify MCP server to VS Code, click the **Install in VS Code** button. Or to manually connect the MCP server, create a `.vscode/mcp.json` file and add:

    ```json  theme={null}
    {
      "servers": {
        "Mintlify": {
          "type": "http",
          "url": "https://mintlify.com/docs/mcp"
        }
      }
    }
    ```

    See the [VS Code documentation](https://code.visualstudio.com/docs/copilot/chat/mcp-servers) for more details.
  </Tab>
</Tabs>


## Authentication

When you enable an API endpoint for MCP, the server includes the authentication requirements defined in your OpenAPI `securitySchemes` and `securityRequirement`. Any keys are handled directly by the tool and not stored or processed by Mintlify.

If a user asks their AI tool to call a protected endpoint, the tool will request the necessary authentication credentials from the user at that moment.


## Monitoring your MCP server

You can view all available MCP tools in the **Available tools** section of the [MCP Server page](https://dashboard.mintlify.com/products/mcp) in your dashboard.

<Frame>
  <img src="https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/mcp/mcp-server-page-light.png?fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=c369f390aa3f129b29193bb4d3434cef" alt="MCP dashboard with Available tools section emphasized" className="block dark:hidden" data-og-width="3024" width="3024" data-og-height="1548" height="1548" data-path="images/mcp/mcp-server-page-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/mcp/mcp-server-page-light.png?w=280&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=c578d322fd05f23a72742fcf6064dba6 280w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/mcp/mcp-server-page-light.png?w=560&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=a4ac282920f79d787429c0660fa1e53c 560w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/mcp/mcp-server-page-light.png?w=840&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=b4bc9185afd76ede33c644fb8b76da86 840w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/mcp/mcp-server-page-light.png?w=1100&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=e009c48bfcb603154c8c65ee5f85af57 1100w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/mcp/mcp-server-page-light.png?w=1650&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=bb94ccfc738c7ab831bdbef0a0d6004d 1650w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/mcp/mcp-server-page-light.png?w=2500&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=4c10450981a41f94529b144529d8d9b5 2500w" />

  <img src="https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/mcp/mcp-server-page-dark.png?fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=77c2901b45017b6e2c978f92f335b813" alt="MCP dashboard with Available tools section emphasized" className="hidden dark:block" data-og-width="3018" width="3018" data-og-height="1540" height="1540" data-path="images/mcp/mcp-server-page-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/mcp/mcp-server-page-dark.png?w=280&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=878922df800c3f6af0a2252751875841 280w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/mcp/mcp-server-page-dark.png?w=560&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=12f14f7dc63efed79e6b236b741537cc 560w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/mcp/mcp-server-page-dark.png?w=840&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=a9b4c02a878876c97cdfd1c678a5f55a 840w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/mcp/mcp-server-page-dark.png?w=1100&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=a5254919bde1cc9276ca77cbfdd729b5 1100w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/mcp/mcp-server-page-dark.png?w=1650&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=a351abe9adc0599d36d946ca17872a8f 1650w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/mcp/mcp-server-page-dark.png?w=2500&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=db77e179fe76df93f369434e1399d223 2500w" />
</Frame>


## Troubleshooting

<AccordionGroup>
  <Accordion title="MCP server only shows search tool">
    If your MCP server only exposes the search tool despite having an OpenAPI specification:

    1. Verify your OpenAPI specification is valid and accessible.
    2. Ensure you've explicitly enabled MCP for specific endpoints using `x-mint.mcp.enabled: true`.
    3. Check your deployment logs for OpenAPI processing errors.

    If OpenAPI processing fails, the server continues with just the search tool to maintain functionality.
  </Accordion>

  <Accordion title="Authentication issues">
    If users report authentication problems:

    1. Check that your OpenAPI specification includes proper `securitySchemes` definitions.
    2. Confirm that enabled endpoints work with the specified authentication methods.
  </Accordion>

  <Accordion title="Tool descriptions missing or unclear">
    If AI tools aren't using your API endpoints effectively:

    1. Add detailed `summary` and `description` fields to your endpoints.
    2. Ensure parameter names and descriptions are self-explanatory.
    3. Use the MCP dashboard to verify how your endpoints appear as tools.
  </Accordion>
</AccordionGroup>



---
**Navigation:** ← Previous | [Index](./index.md) | [Next →](./02-adding-sdk-examples.md)
