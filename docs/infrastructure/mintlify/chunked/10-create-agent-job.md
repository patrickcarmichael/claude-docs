**Navigation:** [← Previous](./09-pages.md) | [Index](./index.md) | [Next →](./11-organize-navigation.md)

# Create agent job
Source: https://mintlify.com/docs/api/agent/create-agent-job

POST /agent/{projectId}/job
Creates a new agent job that can generate and edit documentation based on provided messages and branch information.

This endpoint creates an agent job based on provided messages and branch information. The job executes asynchronously and returns a streaming response with the execution details and results.

If a branch doesn't exist, the agent creates one. If files are edited successfully, a draft pull request is automatically created at the end of the job.


## Rate limits

The agent API has the following limits:

* 100 uses per Mintlify project per hour


## Suggested usage

For best results, use the [useChat hook from ai-sdk](https://ai-sdk.dev/docs/reference/ai-sdk-ui/use-chat#usechat) to send requests and handle responses.



# Get agent job by ID
Source: https://mintlify.com/docs/api/agent/get-agent-job

GET /agent/{projectId}/job/{id}
Retrieves the details and status of a specific agent job by its ID.


## Usage

This endpoint retrieves the details and status of a specific agent job by its unique identifier. Use this to check the progress, status, and results of a previously created agent job.


## Job details

The response includes information such as:

* Job execution status and completion state
* Branch information and pull request details
* Session metadata and timestamps



# Get all agent jobs
Source: https://mintlify.com/docs/api/agent/get-all-jobs

GET /agent/{projectId}/jobs
Retrieves all agent jobs for the specified domain, including their status and details.


## Usage

This endpoint retrieves all agent jobs for the specified domain, providing an overview of all agent activities and their current status. This is useful for monitoring and managing multiple concurrent or historical agent jobs.


## Response

Use this endpoint to get a comprehensive view of all previous agent sessions.



# Assistant message
Source: https://mintlify.com/docs/api/assistant/create-assistant-message

POST /assistant/{domain}/message
Generates a response message from the assistant for the specified domain.


## Rate limits

The assistant API has the following limits:

* 10,000 uses per key per month
* 10,000 requests per Mintlify organization per hour
* 10,000 requests per IP per day


## Suggested usage

For best results, use the [useChat hook from ai-sdk](https://ai-sdk.dev/docs/reference/ai-sdk-ui/use-chat#usechat) to send requests and handle responses.

You can set `fp`, `threadId`, and `filter` in the `body` field of the options parameter passed to the hook.



# Search documentation
Source: https://mintlify.com/docs/api/assistant/search

POST /search/{domain}
Perform semantic and keyword searches across your documentation with configurable filtering and pagination.




# Introduction
Source: https://mintlify.com/docs/api/introduction

Trigger updates, embed AI assistant, and more

The Mintlify REST API enables you to programmatically interact with your documentation, trigger updates, and embed AI-powered chat experiences.


## Endpoints

* [Trigger update](/api-reference/update/trigger): Trigger an update of your site when desired.
* [Get update status](/api-reference/update/status): Get the status of an update and other details about your docs.
* [Create agent job](/api-reference/agent/create-agent-job): Create an agent job to automatically edit your documentation.
* [Get agent job](/api-reference/agent/get-agent-job): Retrieve the details and status of a specific agent job.
* [Get all agent jobs](/api-reference/agent/get-all-jobs): Retrieve all agent jobs for a domain.
* [Generate assistant message](/api-reference/assistant/create-assistant-message): Embed the assistant, trained on your docs, into any application of your choosing.
* [Search documentation](/api-reference/assistant/search): Search through your documentation.


## Authentication

You can generate an API key through [the dashboard](https://dashboard.mintlify.com/settings/organization/api-keys). API keys are associated with an entire organization and can be used across multiple deployments.

### Admin API key

The admin API key is used for the [Trigger update](/api-reference/update/trigger), [Get update status](/api-reference/update/status), and all agent endpoints.

Admin API keys begin with the `mint_` prefix. Keep your admin API keys secret.

### Assistant API key

The assistant API key is used for the [Generate assistant message](/api-reference/assistant/create-assistant-message) and [Search documentation](/api-reference/assistant/search) endpoints.

Assistant API keys begin with the `mint_dsc_` prefix.

The assistant API **key** is a server-side token that should be kept secret.

The assistant API **token** is a public token that can be referenced in your frontend code.

<Note>
  Calls using the assistant API token can incur costs: either using your AI assistant credits or incurring overages.
</Note>



# Get update status
Source: https://mintlify.com/docs/api/update/status

GET /project/update-status/{statusId}
Get the status of an update from the status ID




# Trigger update
Source: https://mintlify.com/docs/api/update/trigger

POST /project/update/{projectId}
Queue a deployment update for your documentation project. Returns a status ID that can be used to track the update progress. By default, the update is triggered from your configured deployment branch.




# Accessibility
Source: https://mintlify.com/docs/guides/accessibility

Create documentation that as many people as possible can use

When you create accessible documentation, you prioritize content design that makes your documentation usable by as many people as possible regardless of how they access and interact with your documentation.

Accessible documentation improves the user experience for everyone. Your content is more clear, better structured, and easier to navigate.

This guide offers some best practices for creating accessible documentation, but it is not exhaustive. You should consider accessibility an ongoing process. Technologies and standards change over time, which introduce new opportunities to improve documentation.


## What is accessibility?

Accessibility (sometimes abbreviated as a11y for the number of letters between the first and last letters of "accessibility") is intentionally designing and building websites and tools that as many people as possible can use. People with temporary or permanent disabilities should have the same level of access to digital technologies. And designing for accessibility benefits everyone, including people who access your website on mobile devices or slow networks.

Accessible documentation follows web accessibility standards, primarily the [Web Content Accessibility Guidelines (WCAG)](https://www.w3.org/WAI/WCAG22/quickref/). These guidelines help ensure your content is perceivable, operable, understandable, and robust.


## Getting started with accessibility

Making your documentation accessible is a process. You don't have to fix everything all at once and you can't do it only once.

If you're just beginning to implement accessibility practices for your documentation, consider a phased approach where you start with high-impact changes and build from there.

### First steps

Here are three things you can do right now to improve the accessibility of your documentation:

1. **Run `mint a11y`** to identify accessibility issues in your content.
2. **Add alt text** to all images.
3. **Check your heading hierarchy** to ensure one H1 per page and headings follow sequential order.

### Plan your accessibility work

The best workflow is the one that works for your team. Here is one way that you can approach accessibility work:

**Phase 1: Images and structure**

* Review all images for descriptive alt text.
* Audit link text and replace generic phrases like "click here."
* Fix heading hierarchy issues across your documentation.

**Phase 2: Navigation and media**

* Test keyboard navigation on your documentation.
* Test screen reader support.
* Add captions and transcripts to embedded videos.
* Review color contrast.

**Phase 3: Build it into your workflow**

* Run `mint a11y` before publishing new content.
* Include accessibility checks in your content review process.
* Test keyboard navigation when adding interactive features.
* Verify new external links and embeds include proper titles and descriptions.

Starting small and building accessibility into your regular workflow makes it sustainable. Each improvement helps more users access your documentation successfully.


## Structure your content

Well-structured content is easier to navigate and understand, especially for screen reader users who rely on headings to move through pages and people who use keyboard navigation.

### Use proper heading hierarchy

Each page should have a single H1 heading, which is defined by the `title:` property in a page's frontmatter. Use additional headings in order without skipping. For example, don't skip from H2 to H4.

```mdx  theme={null}
<!-- Good -->

# Page title (H1)


## Main section (H2)

### Subsection (H3)

### Another subsection (H3)


## Another main section (H2)

<!-- Bad -->

# Page title (H1)


## Main section (H2)

#### Subsection (H4)

### Another subsection (H3)
```

Headings at the same level should have unique names.

```mdx  theme={null}
<!-- Good -->

## Accessibility tips (H2)

### Write effective alt text (H3)

### Use proper color contrast (H3)

<!-- Bad -->

## Accessibility tips (H2)

### Tip (H3)

### Tip (H3)
```

### Write descriptive link text

Link text should be meaningful and connected to the destination. Avoid vague phrases like "click here" or "read more."

```mdx  theme={null}
<!-- Good -->
Learn how to [configure your navigation](/organize/navigation).

<!-- Unclear relation between  -->
[Learn more](/organize/navigation).
```

### Keep content scannable

* Break up long paragraphs.
* Use lists for steps and options.
* Highlight information with callouts.

### Use proper table structure

Use tables sparingly and only for tabular data that has meaning inherited from the column and row headers.

When using tables, include headers so screen readers can associate data with the correct column:

```mdx  theme={null}
| Feature | Status |
| ------- | ------ |
| Search  | Active |
| Analytics | Active |
```


## Write descriptive alt text

Alt text makes images accessible to screen reader users and appears when images fail to load. Images in your documentation should have alt text that describes the image and makes it clear why the image is included. Even with alt text, you should not rely on images alone to convey information. Make sure your content describes what the image communicates.

### Write effective alt text

* **Be specific**: Describe what the image shows, not just that it's an image.
* **Be concise**: Aim for one to two sentences.
* **Avoid redundancy**: Don't start with "Image of" because screen readers will already know that the alt text is associated with an image. However, you should include descriptions like "Screenshot of" or "Diagram of" if that context is important to the image.

```mdx  theme={null}
<!-- Good -->
![Screenshot of the dashboard showing three active projects and two pending invitations](/images/dashboard.png)

<!-- Not helpful -->
![Dashboard screenshot](/images/dashboard.png)
```

### Add alt text to images

For Markdown images, include alt text in the square brackets:

```mdx  theme={null}
![Description of the image](/path/to/image.png)
```

For HTML images, use the `alt` attribute:

```html  theme={null}
<img
  src="/images/screenshot.png"
  alt="Settings panel with accessibility options enabled. The options are emphasized with an orange rectangle."
/>
```

### Add titles to embedded content

Iframes and video embeds require descriptive titles:

```html  theme={null}
<iframe
  src="https://www.youtube.com/embed/example"
  title="Tutorial: Setting up your first documentation site"
></iframe>
```


## Design for readability

Visual design choices affect how accessible your documentation is to users with low vision, color blindness, or other visual disabilities.

### Ensure sufficient color contrast

If you customize your theme colors, verify the contrast ratios meet WCAG requirements:

* Body text: minimum 4.5:1 contrast ratio
* Large text: minimum 3:1 contrast ratio
* Interactive elements: minimum 3:1 contrast ratio

Test both light and dark mode. The `mint a11y` command checks for color contrast.

### Don't rely on color alone

If you use color to convey information, include a text label or icon as well. For example, don't mark errors only with red text. Include an error icon or the word "Error."

### Use clear, concise language

* Write in plain language.
* Define technical terms when first used.
* Avoid run on sentences.
* Use active voice.


## Make code examples accessible

Code blocks are a core part of technical documentation, but they require specific accessibility considerations to ensure screen reader users can understand them. In general, follow these guidelines:

* Break long code examples into smaller, logical chunks.
* Comment complex logic within the code.
* Consider providing a text description for complex algorithms.
* When showing file structure, use actual code blocks with language labels rather than ASCII art.

### Specify the programming language

Always declare the language for syntax highlighting. This helps screen readers announce the code context to users:

````mdx  theme={null}
```javascript
function getUserData(id) {
  return fetch(`/api/users/${id}`);
}
```
````

### Provide context around code

Provide clear context for code blocks:

````mdx  theme={null}
The following function fetches user data from the API:

```javascript
function getUserData(id) {
  return fetch(`/api/users/${id}`);
}
```

This returns a promise that resolves to the user object.
````


## Video and multimedia accessibility

Videos, animations, and other multimedia content need text alternatives so all users can access the information they contain.

### Add captions to videos

Captions make video content accessible to users who are deaf or hard of hearing. They also help users in sound-sensitive environments and non-native speakers:

* Use captions for all spoken content in videos.
* Include relevant sound effects in captions.
* Ensure captions are synchronized with the audio.
* Use proper punctuation and speaker identification when multiple people speak.

Most video hosting platforms support adding captions. Upload caption files or use auto-generated captions as a starting point, then review for accuracy.

### Provide transcripts

Transcripts offer an alternative way to access video content. They're searchable, easier to reference, and accessible to screen readers:

```mdx  theme={null}
<iframe
  src="https://www.youtube.com/embed/example"
  title="Tutorial: Setting up authentication"
></iframe>

<Accordion title="Video transcript">
In this tutorial, we'll walk through setting up authentication...
</Accordion>
```

Place transcripts near the video or provide a clear link to access them.

### Consider alternatives to video-only content

If critical information only appears in a video:

* Provide the same information in text form.
* Include key screenshots with descriptive alt text.
* Create a written tutorial that covers the same material.

This ensures users who can't access video content can still complete their task.


## Test your documentation

Regular testing helps you catch accessibility issues before users encounter them.

### Check for accessibility issues with `mint a11y`

Use the `mint a11y` CLI command to automatically scan your documentation for common accessibility issues:

```bash  theme={null}
mint a11y
```

The command checks for:

* Missing alt text on images
* Improper heading hierarchy
* Insufficient color contrast

When the scan completes, review the reported issues and fix them in your content. Run the command again to verify your fixes.

### Basic keyboard navigation test

Navigate through your documentation using only your keyboard:

1. Press <kbd>Tab</kbd> to move forward through interactive elements.
2. Press <kbd>Shift</kbd> + <kbd>Tab</kbd> to move backward.
3. Press <kbd>Enter</kbd> to activate links and buttons.
4. Verify all interactive elements are reachable and have visible focus indicators.

### Go deeper with accessibility testing

For more comprehensive testing:

* **Screen readers**: Test with [NVDA (Windows)](https://www.nvaccess.org/) or [VoiceOver (Mac)](https://www.apple.com/accessibility/voiceover/).
* **Browser extensions**: Install [axe DevTools](https://www.deque.com/axe/browser-extensions/) or [WAVE](https://wave.webaim.org/extension/) to scan pages for issues.
* **WCAG guidelines**: Review the [Web Content Accessibility Guidelines](https://www.w3.org/WAI/WCAG22/quickref/) for detailed standards.


## Additional resources

Continue learning about accessibility with these trusted resources:

* **[WebAIM](https://webaim.org/)**: Practical articles and tutorials on web accessibility
* **[The A11y Project](https://www.a11yproject.com/)**: Community-driven accessibility resources and checklist
* **[W3C Web Accessibility Initiative (WAI)](https://www.w3.org/WAI/)**: Official accessibility standards and guidance



# Tutorial: Auto-update documentation when code is merged
Source: https://mintlify.com/docs/guides/automate-agent

Use the agent API and a n8n workflow to automatically update your documentation after merging a pull request


## What you will build

An automation that updates your documentation when a pull request is merged. The workflow watches a GitHub repository for merged PRs and then calls the agent API to update your documentation in a different repository.

This workflow connects two separate repositories:

* **Code repository**: Where you store application code. You'll set up the GitHub webhook on this repository. Examples include a backend API, frontend app, SDK, or CLI tool.
* **Documentation repository**: Where you store your documentation and connect to your Mintlify project. The agent creates pull requests with documentation updates in this repository.

This tutorial assumes your documentation is separate from your application code. If you have a monorepo, modify the workflow to target the directory where your documentation is stored rather than a separate repository.

### Workflow overview

1. Someone merges a pull request in the code repository.
2. n8n receives the webhook from GitHub.
3. n8n sends the pull request context to the agent API.
4. The agent creates a pull request in the documentation repository.


## Prerequisites

* n8n workspace
* Mintlify admin API key
* Mintlify Pro or Custom plan
* Admin access to the GitHub repositories for your code and documentation
* GitHub personal access token

### Get your admin API key

1. Navigate to the [API keys](https://dashboard.mintlify.com/settings/organization/api-keys) page in your dashboard.
2. Select **Create Admin API Key**.
3. Copy the key and save it securely.

### Get your GitHub personal access token

1. In GitHub, navigate to **Settings**.
2. Click **Developer settings**.
3. Click **Personal access tokens**.
4. Click **Tokens (classic)**.
5. Click **Generate new token (classic)**.
6. Select these scopes:
   * `repo` (full control of private repositories)
   * `admin:repo_hook` (if you want n8n to create webhooks)
7. Generate and save the token securely.

For more information, see [Creating a personal access token (classic)](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens?versionId=free-pro-team%40latest\&productId=account-and-profile#creating-a-personal-access-token-classic) in the GitHub documentation.


## Build the workflow

### Create the webhook trigger

1. In n8n, create a new workflow.
2. Add a webhook node.
3. Configure the webhook:
   * HTTP Method: `POST`
   * Path: `auto-update-documentation` (or any unique path)
   * Authentication: None
   * Respond: Immediately
4. Save the workflow.
5. Copy the production webhook URL. It looks like: `https://your-n8n-instance.app.n8n.cloud/webhook/auto-update-documentation`

<Frame>
  <img
    src="https://mintcdn.com/mintlify/MUT1RZiseS3dwdrU/images/guides/n8n/webhook-node.png?fit=max&auto=format&n=MUT1RZiseS3dwdrU&q=85&s=165a57aed92aa90d90609c5d381d29b7"
    alt="Screenshot of the configurations for the webhook node."
    style={{
    width: 'auto',
    height: '700px',
  }}
    data-og-width="794"
    width="794"
    data-og-height="1290"
    height="1290"
    data-path="images/guides/n8n/webhook-node.png"
    data-optimize="true"
    data-opv="3"
    srcset="https://mintcdn.com/mintlify/MUT1RZiseS3dwdrU/images/guides/n8n/webhook-node.png?w=280&fit=max&auto=format&n=MUT1RZiseS3dwdrU&q=85&s=efbe9ed332b50e6d3a7d23e72414ee8d 280w, https://mintcdn.com/mintlify/MUT1RZiseS3dwdrU/images/guides/n8n/webhook-node.png?w=560&fit=max&auto=format&n=MUT1RZiseS3dwdrU&q=85&s=77e09994b5055899ccd06694a93d2dea 560w, https://mintcdn.com/mintlify/MUT1RZiseS3dwdrU/images/guides/n8n/webhook-node.png?w=840&fit=max&auto=format&n=MUT1RZiseS3dwdrU&q=85&s=322632ea71fc87c6b8d1efe3fbe0fa03 840w, https://mintcdn.com/mintlify/MUT1RZiseS3dwdrU/images/guides/n8n/webhook-node.png?w=1100&fit=max&auto=format&n=MUT1RZiseS3dwdrU&q=85&s=93c413964016c6fe0f93be7469f16975 1100w, https://mintcdn.com/mintlify/MUT1RZiseS3dwdrU/images/guides/n8n/webhook-node.png?w=1650&fit=max&auto=format&n=MUT1RZiseS3dwdrU&q=85&s=5c7c0fb7641c8696213d039708f0b30c 1650w, https://mintcdn.com/mintlify/MUT1RZiseS3dwdrU/images/guides/n8n/webhook-node.png?w=2500&fit=max&auto=format&n=MUT1RZiseS3dwdrU&q=85&s=67b2572d4375f958940493affb1028ad 2500w"
  />
</Frame>

### Set up the GitHub webhook

1. Navigate to your code repository on GitHub.
2. Click **Settings**.
3. Click **Webhooks**.
4. Click **Add webhook**.
5. Configure the webhook:
   * Payload URL: Paste your n8n webhook URL
   * Content type: `application/json`
   * Which events would you like to trigger this webhook?
     * Select **Let me select individual events.**
     * Select only **Pull requests**.
   * Select **Active**
6. Click **Add webhook**.

### Filter for merged pull requests

Add a code node after the webhook to filter for merged pull requests and extract the relevant information.

1. Add a code node.
2. Name it "Filter merged PRs."
3. Set mode to **Run Once for All Items**.
4. Add this JavaScript:

```javascript Filter merged PRs theme={null}
const webhookData = $input.first().json.body;

// Only continue if this is a closed AND merged PR
if (webhookData.action !== "closed" || webhookData.pull_request?.merged !== true) {
  return [];
}

// Extract information
const pullRequest = webhookData.pull_request;
const repository = webhookData.repository;
const sender = webhookData.sender;

// Build message for agent
const agentMessage = `Update documentation for changes in ${repository.name} **PR #${pullRequest.number}: ${pullRequest.title}** Always edit files and create a pull request.`;

return {
  json: {
    prTitle: pullRequest.title,
    prBody: pullRequest.body || "No description provided",
    prNumber: pullRequest.number,
    prUrl: pullRequest.html_url,
    prAuthor: sender.login,
    codeRepoName: repository.full_name,
    codeRepoShortName: repository.name,
    branchName: pullRequest.head.ref,
    filesChanged: pullRequest.changed_files,
    agentMessage: agentMessage
  }
};
```

<Frame>
  <img src="https://mintcdn.com/mintlify/MUT1RZiseS3dwdrU/images/guides/n8n/filter-merged-PRs-node.png?fit=max&auto=format&n=MUT1RZiseS3dwdrU&q=85&s=a7661a96b0a5c6272e8a284edb8eb8f5" alt="Screenshot of the configurations for the filter merged PRs node." data-og-width="1520" width="1520" data-og-height="1444" height="1444" data-path="images/guides/n8n/filter-merged-PRs-node.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/MUT1RZiseS3dwdrU/images/guides/n8n/filter-merged-PRs-node.png?w=280&fit=max&auto=format&n=MUT1RZiseS3dwdrU&q=85&s=b4e5cf685a50ebb3833fdff26fed0e6d 280w, https://mintcdn.com/mintlify/MUT1RZiseS3dwdrU/images/guides/n8n/filter-merged-PRs-node.png?w=560&fit=max&auto=format&n=MUT1RZiseS3dwdrU&q=85&s=07228082cde6852f53b1cba514b5b3eb 560w, https://mintcdn.com/mintlify/MUT1RZiseS3dwdrU/images/guides/n8n/filter-merged-PRs-node.png?w=840&fit=max&auto=format&n=MUT1RZiseS3dwdrU&q=85&s=ea22fe443bd29c1a48dd2a839510c7ca 840w, https://mintcdn.com/mintlify/MUT1RZiseS3dwdrU/images/guides/n8n/filter-merged-PRs-node.png?w=1100&fit=max&auto=format&n=MUT1RZiseS3dwdrU&q=85&s=b6abd7a70bba3a54fe80a6ba630e6081 1100w, https://mintcdn.com/mintlify/MUT1RZiseS3dwdrU/images/guides/n8n/filter-merged-PRs-node.png?w=1650&fit=max&auto=format&n=MUT1RZiseS3dwdrU&q=85&s=9c9086087bcd6069b467a8e31ecb8af5 1650w, https://mintcdn.com/mintlify/MUT1RZiseS3dwdrU/images/guides/n8n/filter-merged-PRs-node.png?w=2500&fit=max&auto=format&n=MUT1RZiseS3dwdrU&q=85&s=ee4742c2dea8acbaac654e75d4c5c803 2500w" />
</Frame>

This code stops the workflow if the pull request wasn't merged, extracts all relevant information from the GitHub webhook, and creates a message for the agent API.

### Call the agent API

Add an HTTP request node to create a documentation job.

1. Add an HTTP request node.
2. Name it "Create agent job."
3. Configure the request:

   * Method: `POST`
   * URL: `https://api.mintlify.com/v1/agent/YOUR_PROJECT_ID/job` (replace `YOUR_PROJECT_ID` with your project ID from the [API keys](https://dashboard.mintlify.com/settings/organization/api-keys) page of your dashboard)
   * Authentication: Generic Credential Type → Header Auth
     * Create a new credential:
       * Name: `Authorization`
       * Value: `Bearer mint_YOUR_API_KEY` (replace with your API key)
   * Send Body: On
   * Body Content Type: JSON
   * Specify Body: Using JSON
   * Add this JSON:

   ```json  theme={null}
   {
   "branch": "docs-update-from-{{ $json.codeRepoShortName }}-pr-{{ $json.prNumber }}",
   "messages": [
       {
       "role": "system",
       "content": "{{ $json.agentMessage }}"
       }
   ]
   }
   ```

<Frame>
  <img
    src="https://mintcdn.com/mintlify/jW5VvzJALf7BW1X_/images/guides/n8n/create-agent-job-node.png?fit=max&auto=format&n=jW5VvzJALf7BW1X_&q=85&s=2bbb162905564f80a30bb7d75c917815"
    alt="Screenshot of the configurations for the create agent job node."
    style={{
    width: 'auto',
    height: '700px',
  }}
    data-og-width="756"
    width="756"
    data-og-height="1438"
    height="1438"
    data-path="images/guides/n8n/create-agent-job-node.png"
    data-optimize="true"
    data-opv="3"
    srcset="https://mintcdn.com/mintlify/jW5VvzJALf7BW1X_/images/guides/n8n/create-agent-job-node.png?w=280&fit=max&auto=format&n=jW5VvzJALf7BW1X_&q=85&s=01faea9302149a974dc9ac3dc68d6f95 280w, https://mintcdn.com/mintlify/jW5VvzJALf7BW1X_/images/guides/n8n/create-agent-job-node.png?w=560&fit=max&auto=format&n=jW5VvzJALf7BW1X_&q=85&s=01fcfb7f35dfaf59afd9e2a626df7ea5 560w, https://mintcdn.com/mintlify/jW5VvzJALf7BW1X_/images/guides/n8n/create-agent-job-node.png?w=840&fit=max&auto=format&n=jW5VvzJALf7BW1X_&q=85&s=ce18f31daf60caec50823650d06cd96d 840w, https://mintcdn.com/mintlify/jW5VvzJALf7BW1X_/images/guides/n8n/create-agent-job-node.png?w=1100&fit=max&auto=format&n=jW5VvzJALf7BW1X_&q=85&s=280fa6219837e89137b31ffc6d458235 1100w, https://mintcdn.com/mintlify/jW5VvzJALf7BW1X_/images/guides/n8n/create-agent-job-node.png?w=1650&fit=max&auto=format&n=jW5VvzJALf7BW1X_&q=85&s=5a2bd3ae4862208ea9aedd0f3a3ed8e0 1650w, https://mintcdn.com/mintlify/jW5VvzJALf7BW1X_/images/guides/n8n/create-agent-job-node.png?w=2500&fit=max&auto=format&n=jW5VvzJALf7BW1X_&q=85&s=c74c496f1085e6cb6f8fb075cba90fa1 2500w"
  />
</Frame>

The agent creates a pull request in your documentation repository using a descriptive branch name that includes the source repository and pull request number.

### Activate the workflow

1. Save your workflow.
2. Set it to active.

Your workflow is now monitoring your code repository for merged pull requests.

<Frame>
  <img src="https://mintcdn.com/mintlify/MUT1RZiseS3dwdrU/images/guides/n8n/workflow.png?fit=max&auto=format&n=MUT1RZiseS3dwdrU&q=85&s=55120ad3ffc9b32d56aefe05c6431324" alt="Screenshot of the automation workflow in the n8n editor." data-og-width="1562" width="1562" data-og-height="632" height="632" data-path="images/guides/n8n/workflow.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/MUT1RZiseS3dwdrU/images/guides/n8n/workflow.png?w=280&fit=max&auto=format&n=MUT1RZiseS3dwdrU&q=85&s=7dbba58e8a86f3998e022cb5174649d7 280w, https://mintcdn.com/mintlify/MUT1RZiseS3dwdrU/images/guides/n8n/workflow.png?w=560&fit=max&auto=format&n=MUT1RZiseS3dwdrU&q=85&s=06d69f116911ba3a32980f59c122ff45 560w, https://mintcdn.com/mintlify/MUT1RZiseS3dwdrU/images/guides/n8n/workflow.png?w=840&fit=max&auto=format&n=MUT1RZiseS3dwdrU&q=85&s=5fe9e6f99577ba5591874ea0b6c4f9a7 840w, https://mintcdn.com/mintlify/MUT1RZiseS3dwdrU/images/guides/n8n/workflow.png?w=1100&fit=max&auto=format&n=MUT1RZiseS3dwdrU&q=85&s=af2b635a1605ca0dd4f7123fe1c122a0 1100w, https://mintcdn.com/mintlify/MUT1RZiseS3dwdrU/images/guides/n8n/workflow.png?w=1650&fit=max&auto=format&n=MUT1RZiseS3dwdrU&q=85&s=ef500f88af7377097e4c7a21843cbe6a 1650w, https://mintcdn.com/mintlify/MUT1RZiseS3dwdrU/images/guides/n8n/workflow.png?w=2500&fit=max&auto=format&n=MUT1RZiseS3dwdrU&q=85&s=6a9b10ff9ee6d5da2657ebec2ef12c0e 2500w" />
</Frame>


## Test the automation

1. Create a test branch in your code repository:
   ```bash  theme={null}
   git checkout -b test-docs-automation
   ```

2. Make a small change and commit it:
   ```bash  theme={null}
   git add .
   git commit -m "Test: trigger docs automation"
   git push origin test-docs-automation
   ```

3. Open a pull request on GitHub.

4. Merge the pull request.

### Verify the automation

Check the following to confirm the workflow is working:

* **n8n executions**: You should see a new execution with all nodes completed successfully.
* **Documentation repository**: After a minute or two, check for a new branch and pull request with documentation updates.


## Troubleshooting

### Webhook not triggering

* Verify the workflow is active in n8n.
* Check GitHub repository Settings → Webhooks → Recent Deliveries for the response code.
* Confirm the webhook URL matches your n8n webhook URL exactly.

### 401 error from agent API

* Verify your API key starts with `mint_`.
* Check the Authorization header is formatted as `Bearer mint_yourkey`.
* Confirm the API key is for the correct Mintlify organization.

### 401 error from GitHub

* Verify your token has the `repo` scope.
* Check that the token hasn't expired.
* Confirm you included the `User-Agent` header in the GitHub request.



# Working with branches
Source: https://mintlify.com/docs/guides/branches

Use branches to make and review changes without affecting your live documentation

Branches are a feature of version control that point to specific commits in your repository. Your deployment branch, usually called `main`, represents the content that is used to build your live documentation. All other branches are independent of your live docs unless you choose to merge them into your deployment branch.

Branches let you create separate instances of your documentation to make changes, get reviews, and try new approaches before publishing. Your team can work on branches to update different parts of your documentation at the same time without affecting what users see on your live site until you publish any changes.

We recommend always working from branches when updating documentation to keep your live site stable and enable review workflows.

<Tip>
  * Name branches clearly so teammates understand what you're working on.
  * Delete branches after merging to keep your repository organized.
  * Let your team know when you're working on major changes that might affect their work.
</Tip>


## Creating a branch

1. Select the branch name in the editor toolbar (usually `main` by default).
2. Select **New Branch**.
3. Enter a descriptive name for your branch like `update-getting-started` or `fix-api-examples`.
4. Select **Create Branch**.


## Saving changes on a branch

To save your changes on a branch, select the **Save Changes** button in the top-right corner of the editor. This creates a commit and pushes your work to your branch.


## Switching branches

1. Select the branch name in the editor toolbar.
2. Select the branch you want to switch to from the dropdown menu.

<Tip>
  Unsaved changes are lost when switching branches. Make sure to save or publish your work before switching branches.
</Tip>



# Claude Code
Source: https://mintlify.com/docs/guides/claude-code

Configure Claude Code to help write, review, and update your docs

Claude Code is an agentic command line tool that can help you maintain your documentation. It can write new content, review existing pages, and keep docs up to date.

You can train Claude Code to understand your documentation standards and workflows by adding a `CLAUDE.md` file to your project and refining it over time.


## Getting started

**Prerequisites:**

* Active Claude subscription (Pro, Max, or API access)

**Setup:**

1. Install Claude Code:

```bash  theme={null}
npm install -g @anthropic-ai/claude-code
```

2. Navigate to your docs directory.
3. (Optional) Add the `CLAUDE.md` file below to your project.
4. Run `claude` to start.


## CLAUDE.md template

Save a `CLAUDE.md` file at the root of your docs directory to help Claude Code understand your project. This file trains Claude Code on your documentation standards, preferences, and workflows. See [Manage Claude's memory](https://docs.anthropic.com/en/docs/claude-code/memory) in the Anthropic docs for more information.

Copy this example template or make changes for your docs specifications:

```mdx  theme={null}

# Mintlify documentation


## Working relationship
- You can push back on ideas-this can lead to better documentation. Cite sources and explain your reasoning when you do so
- ALWAYS ask for clarification rather than making assumptions
- NEVER lie, guess, or make up anything


## Project context
- Format: MDX files with YAML frontmatter
- Config: docs.json for navigation, theme, settings
- Components: Mintlify components


## Content strategy
- Document just enough for user success - not too much, not too little
- Prioritize accuracy and usability
- Make content evergreen when possible
- Search for existing content before adding anything new. Avoid duplication unless it is done for a strategic reason
- Check existing patterns for consistency
- Start by making the smallest reasonable changes


## docs.json

- Refer to the [docs.json schema](https://mintlify.com/docs.json) when building the docs.json file and site navigation


## Frontmatter requirements for pages
- title: Clear, descriptive page title
- description: Concise summary for SEO/navigation


## Writing standards
- Second-person voice ("you")
- Prerequisites at start of procedural content
- Test all code examples before publishing
- Match style and formatting of existing pages
- Include both basic and advanced use cases
- Language tags on all code blocks
- Alt text on all images
- Relative paths for internal links


## Git workflow
- NEVER use --no-verify when committing
- Ask how to handle uncommitted changes before starting
- Create a new branch when no clear branch exists for changes
- Commit frequently throughout development
- NEVER skip or disable pre-commit hooks


## Do not
- Skip frontmatter on any MDX file
- Use absolute URLs for internal links
- Include untested code examples
- Make assumptions - always ask for clarification
```


## Sample prompts

Once you have Claude Code set up, try these prompts to see how it can help with common documentation tasks. You can copy and paste these examples directly, or adapt them for your specific needs.

### Convert notes to polished docs

Turn rough drafts into proper Markdown pages with components and frontmatter.

**Example prompt:**

```text wrap theme={null}
Convert this text into a properly formatted MDX page: [paste your text here]
```

### Review docs for consistency

Get suggestions to improve style, formatting, and component usage.

**Example prompt:**

```text wrap theme={null}
Review the files in docs/ and suggest improvements for consistency and clarity
```

### Update docs when features change

Keep documentation current when your product evolves.

**Example prompt:**

```text wrap theme={null}
Our API now requires a version parameter. Update our docs to include version=2024-01 in all examples
```

### Generate comprehensive code examples

Create multi-language examples with error handling.

**Example prompt:**

```text wrap theme={null}
Create code examples for [your API endpoint] in JavaScript, Python, and cURL with error handling
```


## Extending Claude Code

Beyond manually prompting Claude Code, you can integrate it with your existing workflows.

### Automation with GitHub Actions

Run Claude Code automatically when code changes to keep docs up to date. You can trigger documentation reviews on pull requests or update examples when API changes are detected.

### Multi-instance workflows

Use separate Claude Code sessions for different tasks - one for writing new content and another for reviewing and quality assurance. This helps maintain consistency and catch issues that a single session might miss.

### Team collaboration

Share your refined `CLAUDE.md` file with your team to ensure consistent documentation standards across all contributors. Teams often develop project-specific prompts and workflows that become part of their documentation process.

### Custom commands

Create reusable slash commands in `.claude/commands/` for frequently used documentation tasks specific to your project or team.



# Content types
Source: https://mintlify.com/docs/guides/content-types

Create the right content for your users

<Tip>
  This page explains different content types, when to use each one, and how to approach writing for each type.
</Tip>

Documentation should be organized around the specific goal you're trying to help people achieve.


## Categorize using the Diátaxis framework

The [Diátaxis framework](https://diataxis.fr) is a helpful guide for categorizing content based on your audience's needs. Documentation can generally be mapped into one of these types:

1. Tutorials: Learning-oriented content for new users
2. How-to guides: Task-oriented guidance for specific problems
3. Explanations: Understanding-oriented conceptual discussions
4. Reference: Information-oriented technical descriptions

Defining content types helps you plan documentation with a clear purpose and makes it easier for users to find what they need.

<Frame>
  <img src="https://mintcdn.com/mintlify/mgh6fYMQy9DM5E4a/images/guides/best-practices/diataxis.webp?fit=max&auto=format&n=mgh6fYMQy9DM5E4a&q=85&s=057c36ac97446a5d360871e41852520e" alt="A diagram of the Diátaxis framework showing four quadrants that correspond to the four content types: Tutorials, How-To Guides, Reference, and Explanation." data-og-width="1920" width="1920" data-og-height="1080" height="1080" data-path="images/guides/best-practices/diataxis.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/mgh6fYMQy9DM5E4a/images/guides/best-practices/diataxis.webp?w=280&fit=max&auto=format&n=mgh6fYMQy9DM5E4a&q=85&s=26ac47cbd6491b139648ca243b7d88c6 280w, https://mintcdn.com/mintlify/mgh6fYMQy9DM5E4a/images/guides/best-practices/diataxis.webp?w=560&fit=max&auto=format&n=mgh6fYMQy9DM5E4a&q=85&s=59153e5613d8fc49ec2cb1d33e048878 560w, https://mintcdn.com/mintlify/mgh6fYMQy9DM5E4a/images/guides/best-practices/diataxis.webp?w=840&fit=max&auto=format&n=mgh6fYMQy9DM5E4a&q=85&s=27a983a4d2e3c22b65085d33a80757b2 840w, https://mintcdn.com/mintlify/mgh6fYMQy9DM5E4a/images/guides/best-practices/diataxis.webp?w=1100&fit=max&auto=format&n=mgh6fYMQy9DM5E4a&q=85&s=59eb28f9641db4fa809f2539e5e8fe28 1100w, https://mintcdn.com/mintlify/mgh6fYMQy9DM5E4a/images/guides/best-practices/diataxis.webp?w=1650&fit=max&auto=format&n=mgh6fYMQy9DM5E4a&q=85&s=7dca9a715257b92629769f5ac1874fd0 1650w, https://mintcdn.com/mintlify/mgh6fYMQy9DM5E4a/images/guides/best-practices/diataxis.webp?w=2500&fit=max&auto=format&n=mgh6fYMQy9DM5E4a&q=85&s=65bfc24435e42320d1d83aa97f55c391 2500w" />
</Frame>


## Picking a type

| Question                               | Tutorial               | How-To                   | Reference                | Explanation             |
| :------------------------------------- | :--------------------- | :----------------------- | :----------------------- | :---------------------- |
| What is the user's goal?               | Learn through practice | Solve a specific problem | Find precise information | Understand concepts     |
| What is the user's knowledge?          | Beginner               | Intermediate             | Experienced              | Any level               |
| What is the primary focus?             | Learning by doing      | Achieving a goal         | Providing information    | Deepening understanding |
| How is the content structured?         | Step-by-step           | Problem-solution         | Organized facts          | Conceptual discussions  |
| Is it task-oriented?                   | Yes, guided tasks      | Yes, specific tasks      | No, informational        | No, conceptual          |
| Is it designed for linear progression? | Yes                    | No                       | No                       | No                      |


## Writing for each type

### Tutorials (Learning-oriented)

* **Audience goal**: Learn something new through step-by-step instructions.
* **Characteristics**: Sequential and assumes no prior knowledge.
* **Writing approach**:
  * Set expectations of what the user will achieve after reading.
  * Use clear, incremental steps. Minimize choices that need to be made by the user.
  * Point out milestones along the way.
  * Minimize theory and focus on concrete actions.

### How-To Guides (Problem-oriented)

* **Audience goal**: Perform a specific task correctly.
* **Characteristics**: Goal-driven and assumes some prior knowledge.
* **Writing approach**:
  * Write from the perspective of the user, not the product.
  * Describe a logical sequence and omit unnecessary details.
  * Minimize context beyond what is necessary.

### Reference (Information-oriented)

* **Audience goal**: Find details about a product's functionality.
* **Characteristics**: Unambiguous, product-focused, scannable.
* **Writing approach**:
  * Be scannable and concise.
  * Prioritize consistency.
  * Avoid explanatory content. Focus on examples that are easy to copy and modify.

### Explanation (Understanding-oriented)

* **Audience goal**: Expand general understanding of a concept or highly complex feature.
* **Characteristics**: Theoretical, potentially opinionated, broad in scope.
* **Writing approach**:
  * Provide background context, such as design decisions or technical constraints.
  * Acknowledge opinions and alternatives.
  * Draw connections to other areas in the product or industry.


## Tips and tricks

1. **Maintain purpose**: Before writing, assign each page a specific content type and make it top of mind in the doc throughout your writing.
2. **Consider content freshness**: Regardless of content type, try to optimize for evergreen documentation. If something represents a moment in time of what a feature looks like on a specific date, it's probably better suited for a changelog or blog post than in your documentation. Or if something changes very frequently avoid putting it in your docs.
3. **Think like your users**: Consider different user personas when organizing content. See [Understand your audience](/guides/understand-your-audience) for more information.

While the Diátaxis framework provides a starting point, successful documentation requires contextual adaptation to your product. Start by understanding the framework's principles, then adjust them to serve your users' needs.



# Cursor
Source: https://mintlify.com/docs/guides/cursor

Configure Cursor to be your writing assistant

Transform Cursor into a documentation expert that knows your components, style guide, and best practices.


## Using Cursor with Mintlify

Cursor rules provide persistent context about your documentation, ensuring more consistent suggestions that fit your standards and style.

* **Project rules** are stored in your documentation repository and shared with your team.
* **User rules** apply to your personal Cursor environment.

We recommend creating project rules for your docs so that all contributors have access to the same rules.

Create rules files in the `.cursor/rules` directory of your docs repo. See the [Cursor Rules documentation](https://docs.cursor.com/context/rules) for complete setup instructions.


## Example project rule

This rule provides Cursor with context to properly format Mintlify components and follow technical writing best practices.

You can use this example as-is or customize it for your documentation:

* **Writing standards**: Update language guidelines to match your style guide.
* **Component patterns**: Add project-specific components or modify existing examples.
* **Code examples**: Replace generic examples with real API calls and responses for your product.
* **Style and tone preferences**: Adjust terminology, formatting, and other rules.

Add this rule with any modifications as an `.mdc` file in the `.cursor/rules` directory of your docs repo.

````mdx wrap theme={null}

# Mintlify technical writing rule

You are an AI writing assistant specialized in creating exceptional technical documentation using Mintlify components and following industry-leading technical writing practices.


## Core writing principles

### Language and style requirements

- Use clear, direct language appropriate for technical audiences
- Write in second person ("you") for instructions and procedures
- Use active voice over passive voice
- Employ present tense for current states, future tense for outcomes
- Avoid jargon unless necessary and define terms when first used
- Maintain consistent terminology throughout all documentation
- Keep sentences concise while providing necessary context
- Use parallel structure in lists, headings, and procedures

### Content organization standards

- Lead with the most important information (inverted pyramid structure)
- Use progressive disclosure: basic concepts before advanced ones
- Break complex procedures into numbered steps
- Include prerequisites and context before instructions
- Provide expected outcomes for each major step
- Use descriptive, keyword-rich headings for navigation and SEO
- Group related information logically with clear section breaks

### User-centered approach

- Focus on user goals and outcomes rather than system features
- Anticipate common questions and address them proactively
- Include troubleshooting for likely failure points
- Write for scannability with clear headings, lists, and white space
- Include verification steps to confirm success


## Mintlify component reference

### docs.json

- Refer to the [docs.json schema](https://mintlify.com/docs.json) when building the docs.json file and site navigation

### Callout components

#### Note - Additional helpful information

<Note>
Supplementary information that supports the main content without interrupting flow
</Note>

#### Tip - Best practices and pro tips

<Tip>
Expert advice, shortcuts, or best practices that enhance user success
</Tip>

#### Warning - Important cautions

<Warning>
Critical information about potential issues, breaking changes, or destructive actions
</Warning>

#### Info - Neutral contextual information

<Info>
Background information, context, or neutral announcements
</Info>

#### Check - Success confirmations

<Check>
Positive confirmations, successful completions, or achievement indicators
</Check>

### Code components

#### Single code block

Example of a single code block:

```javascript config.js
const apiConfig = {
  baseURL: 'https://api.example.com',
  timeout: 5000,
  headers: {
    'Authorization': `Bearer ${process.env.API_TOKEN}`
  }
};
```

#### Code group with multiple languages

Example of a code group:

<CodeGroup>
```javascript Node.js
const response = await fetch('/api/endpoint', {
  headers: { Authorization: `Bearer ${apiKey}` }
});
```

```python Python
import requests
response = requests.get('/api/endpoint', 
  headers={'Authorization': f'Bearer {api_key}'})
```

```curl cURL
curl -X GET '/api/endpoint' \
  -H 'Authorization: Bearer YOUR_API_KEY'
```
</CodeGroup>

#### Request/response examples

Example of request/response documentation:

<RequestExample>
```bash cURL
curl -X POST 'https://api.example.com/users' \
  -H 'Content-Type: application/json' \
  -d '{"name": "John Doe", "email": "john@example.com"}'
```
</RequestExample>

<ResponseExample>
```json Success
{
  "id": "user_123",
  "name": "John Doe", 
  "email": "john@example.com",
  "created_at": "2024-01-15T10:30:00Z"
}
```
</ResponseExample>

### Structural components

#### Steps for procedures

Example of step-by-step instructions:

<Steps>
<Step title="Install dependencies">
  Run `npm install` to install required packages.
  
  <Check>
  Verify installation by running `npm list`.
  </Check>
</Step>

<Step title="Configure environment">
  Create a `.env` file with your API credentials.
  
  ```bash
  API_KEY=your_api_key_here
  ```
  
  <Warning>
  Never commit API keys to version control.
  </Warning>
</Step>
</Steps>

#### Tabs for alternative content

Example of tabbed content:

<Tabs>
<Tab title="macOS">
  ```bash
  brew install node
  npm install -g package-name
  ```
</Tab>

<Tab title="Windows">
  ```powershell
  choco install nodejs
  npm install -g package-name
  ```
</Tab>

<Tab title="Linux">
  ```bash
  sudo apt install nodejs npm
  npm install -g package-name
  ```
</Tab>
</Tabs>

#### Accordions for collapsible content

Example of accordion groups:

<AccordionGroup>
<Accordion title="Troubleshooting connection issues">
  - **Firewall blocking**: Ensure ports 80 and 443 are open
  - **Proxy configuration**: Set HTTP_PROXY environment variable
  - **DNS resolution**: Try using 8.8.8.8 as DNS server
</Accordion>

<Accordion title="Advanced configuration">
  ```javascript
  const config = {
    performance: { cache: true, timeout: 30000 },
    security: { encryption: 'AES-256' }
  };
  ```
</Accordion>
</AccordionGroup>

### Cards and columns for emphasizing information

Example of cards and card groups:

<Card title="Getting started guide" icon="rocket" href="/quickstart">
Complete walkthrough from installation to your first API call in under 10 minutes.
</Card>

<CardGroup cols={2}>
<Card title="Authentication" icon="key" href="/auth">
  Learn how to authenticate requests using API keys or JWT tokens.
</Card>

<Card title="Rate limiting" icon="clock" href="/rate-limits">
  Understand rate limits and best practices for high-volume usage.
</Card>
</CardGroup>

### API documentation components

#### Parameter fields

Example of parameter documentation:

<ParamField path="user_id" type="string" required>
Unique identifier for the user. Must be a valid UUID v4 format.
</ParamField>

<ParamField body="email" type="string" required>
User's email address. Must be valid and unique within the system.
</ParamField>

<ParamField query="limit" type="integer" default="10">
Maximum number of results to return. Range: 1-100.
</ParamField>

<ParamField header="Authorization" type="string" required>
Bearer token for API authentication. Format: `Bearer YOUR_API_KEY`
</ParamField>

#### Response fields

Example of response field documentation:

<ResponseField name="user_id" type="string" required>
Unique identifier assigned to the newly created user.
</ResponseField>

<ResponseField name="created_at" type="timestamp">
ISO 8601 formatted timestamp of when the user was created.
</ResponseField>

<ResponseField name="permissions" type="array">
List of permission strings assigned to this user.
</ResponseField>

#### Expandable nested fields

Example of nested field documentation:

<ResponseField name="user" type="object">
Complete user object with all associated data.

<Expandable title="User properties">
  <ResponseField name="profile" type="object">
  User profile information including personal details.
  
  <Expandable title="Profile details">
    <ResponseField name="first_name" type="string">
    User's first name as entered during registration.
    </ResponseField>
    
    <ResponseField name="avatar_url" type="string | null">
    URL to user's profile picture. Returns null if no avatar is set.
    </ResponseField>
  </Expandable>
  </ResponseField>
</Expandable>
</ResponseField>

### Media and advanced components

#### Frames for images

Wrap all images in frames:

<Frame>
<img src="/images/dashboard.png" alt="Main dashboard showing analytics overview" />
</Frame>

<Frame caption="The analytics dashboard provides real-time insights">
<img src="/images/analytics.png" alt="Analytics dashboard with charts" />
</Frame>

#### Videos

Use the HTML video element for self-hosted video content:

<video
  controls
  className="w-full aspect-video rounded-xl"
  src="link-to-your-video.com"
></video>

Embed YouTube videos using iframe elements:

<iframe
  className="w-full aspect-video rounded-xl"
  src="https://www.youtube.com/embed/4KzFe50RQkQ"
  title="YouTube video player"
  frameBorder="0"
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
  allowFullScreen
></iframe>

#### Tooltips

Example of tooltip usage:

<Tooltip tip="Application Programming Interface - protocols for building software">
API
</Tooltip>

#### Updates

Use updates for changelogs:

<Update label="Version 2.1.0" description="Released March 15, 2024">

## New features
- Added bulk user import functionality
- Improved error messages with actionable suggestions


## Bug fixes
- Fixed pagination issue with large datasets
- Resolved authentication timeout problems
</Update>


## Required page structure

Every documentation page must begin with YAML frontmatter:

```yaml
---
title: "Clear, specific, keyword-rich title"
description: "Concise description explaining page purpose and value"
---
```


## Content quality standards

### Code examples requirements

- Always include complete, runnable examples that users can copy and execute
- Show proper error handling and edge case management
- Use realistic data instead of placeholder values
- Include expected outputs and results for verification
- Test all code examples thoroughly before publishing
- Specify language and include filename when relevant
- Add explanatory comments for complex logic
- Never include real API keys or secrets in code examples

### API documentation requirements

- Document all parameters including optional ones with clear descriptions
- Show both success and error response examples with realistic data
- Include rate limiting information with specific limits
- Provide authentication examples showing proper format
- Explain all HTTP status codes and error handling
- Cover complete request/response cycles

### Accessibility requirements

- Include descriptive alt text for all images and diagrams
- Use specific, actionable link text instead of "click here"
- Ensure proper heading hierarchy starting with H2
- Provide keyboard navigation considerations
- Use sufficient color contrast in examples and visuals
- Structure content for easy scanning with headers and lists


## Component selection logic

- Use **Steps** for procedures and sequential instructions
- Use **Tabs** for platform-specific content or alternative approaches
- Use **CodeGroup** when showing the same concept in multiple programming languages
- Use **Accordions** for progressive disclosure of information
- Use **RequestExample/ResponseExample** specifically for API endpoint documentation
- Use **ParamField** for API parameters, **ResponseField** for API responses
- Use **Expandable** for nested object properties or hierarchical information
````



# GEO guide: Optimize docs for AI search and answer engines
Source: https://mintlify.com/docs/guides/geo

Make your documentation more discoverable and cited more frequently by AI tools

Optimize your documentation for both traditional search engines and AI-powered answer engines like ChatGPT, Perplexity, and Google AI Overviews.

Generative Engine Optimization (GEO) focuses on being cited by AI systems through comprehensive content and structured information, while traditional SEO targets search result rankings.


## GEO quickstart

### Initial setup

1. **Make sure your docs are being indexed** in your `docs.json` settings
2. **Audit current pages** for missing descriptions and titles

### Content improvements

1. **Add comparison tables** to appropriate pages
2. **Audit headings** to ensure they answer common questions
3. **Improve internal linking** between related topics
4. **Test with AI tools** to verify accuracy


## GEO best practices

In general, well written and well structured documentation will have strong GEO. You should still prioritize writing for your users, and if your content is meeting their needs, you will be well on your way to optimizing for AI tools. Creating genuinely helpful content rather than optimizing for optimization's sake is rewarded by both traditional and AI search engines.

Focus on:

* Content aligned to user needs rather than keyword matching
* Structured, scannable information
* Direct answers to questions

### Format for clarity

These formatting practices help AI tools parse and understand your content:

* Don't skip heading levels (H1 → H2 → H3)
* Use specific object names instead of "it" or "this"
* Label code blocks with their programming language
* Give images descriptive alt text
* Link to related concepts to help AI understand relationships

### Answer questions directly

Write content that addresses specific user questions:

* Begin sections with the main takeaway
* Use descriptive headings that match common queries
* Break complex topics into numbered steps


## Mintlify configuration

Use these features to improve GEO.

### Add descriptive page metadata

Include clear titles and descriptions in your frontmatter:

```mdx  theme={null}
---
title: "API authentication guide"
description: "Complete guide to implementing API authentication with code examples"
---
```

### Configure global indexing settings

Add to your `docs.json`:

```json  theme={null}
{
  "seo": {
    "indexing": "all",
    "metatags": {
      "og:type": "website",
      "og:site_name": "Your docs"
    }
  }
}
```

### LLMs.txt

LLMs.txt files help AI systems understand your documentation structure, similar to how sitemaps help search engines. Mintlify automatically generates LLMs.txt files for your docs. No configuration is required.


## Testing your documentation

Test various AI tools with questions about your product and documentation to see how well your docs are being cited.

**Ask AI assistants specific questions about your docs:**

* "How do I set up authentication using this API?"
* "Walk me through the installation process step by step"

**Check that tools provide:**

* Correct code samples
* Accurate step-by-step instructions



# Git concepts
Source: https://mintlify.com/docs/guides/git-concepts

Learn Git fundamentals for the docs-as-code workflow

Git is a version control system that allows you to track changes to your documentation and collaborate with team members. With Git, for every file in your project, you can see what changed, when, and why. Git also makes it easy to revert to previous versions of files if you ever need to.

The web editor performs some Git operations behind the scenes. Understanding these concepts will help you work more effectively with the web editor and collaborate with team members who are working in their local development environments.


## Core Git concepts

<AccordionGroup>
  <Accordion title="Repository">
    Your documentation's source where all files and their history are stored. The web editor connects to your repository to access and modify content.
  </Accordion>

  <Accordion title="Commit">
    A saved snapshot of your changes at a specific point in time. Each commit includes a message describing what changed and creates a permanent record in your project history.
  </Accordion>

  <Accordion title="Branch">
    A branch points to a specific commit in your repository. Your live documentation is built from a deployment branch. You can have any number of other branches with changes that are not yet published to your live documentation. If you want to incorporate the changes from a branch into your live documentation, you can merge the branch into your deployment branch through a pull request.

    Use branches to work on changes without affecting your live documentation, safely experiment with new features, and get reviews before publishing.
  </Accordion>

  <Accordion title="Deployment branch">
    The primary branch of your project that your live documentation content is built from. Changes to this branch are automatically published to your documentation site. Often called `main`, but you can set any branch as your deployment branch.
  </Accordion>

  <Accordion title="Pull request">
    A way to propose merging your changes on a branch into your live documentation. Allows for review and discussion before changes go live. Commonly called a PR, and also called a merge request in GitLab.
  </Accordion>

  <Accordion title="Diff">
    A diff (or difference) shows the changes between two versions of a file. When reviewing pull requests, diffs highlight what has been added, removed, or modified, making it easy to identify what changed.
  </Accordion>
</AccordionGroup>


## How the web editor uses Git

The web editor connects to your Git repository through the [GitHub App](/deploy/github) or [GitLab integration](/deploy/gitlab) and automates common Git operations.

When you:

* **Open a file**: The editor fetches the latest version from your repository, ensuring you're always working with up to date content.
* **Make changes**: The editor tracks your changes as a draft that can become a commit when you're ready to save your work.
* **Save changes**: The editor makes a commit with your changes, preserving your work in the project history.
* **Create a branch**: The editor creates a new branch in your repository that can be used by anyone with access to the repository so they can collaborate and review changes.
* **Publish on your deployment branch**: The editor commits and pushes directly to your deployment branch, which publishes your changes immediately.
* **Publish on other branches**: The editor creates a pull request, which allows you to get feedback from others before merging your changes into your deployment branch.


## Git best practices

Every team will develop their own workflows and preferences, but these are some general best practices to get you started.

* **Write descriptive commit messages**: Be specific about what changed using active language.
* **Use descriptive branch names**: Branch names should explain the work being done and be meaningful to someone who is looking at the branches in your repository.
* **Keep branches focused**: Keep the changes on a branch focused on a specific task or project.
* **Delete branches after merging**: Delete branches when you no longer need them to keep your repository tidy.



# Improve your docs
Source: https://mintlify.com/docs/guides/improving-docs

Use data to make your documentation better

<Tip>
  This page explains how to measure the success of your documentation with quantitative metrics, qualitative feedback, and alignment with business goals.
</Tip>


## Quantitative metrics

Some examples to consider:

* **Page views**: Views can be a good proxy for success, but could be driven by bot traffic or repeat visitors. If you're getting many views on an errors or explainer page, it might signal an issue with your broader product.
* **Time on page**: Longer time on page might signal engagement, but could also mean users are stuck trying to find the information they need.
* **Bounce rate**: A high bounce rate could mean users didn't find what they needed, or it could mean they found exactly what they needed and left satisfied.

The key is to compare these metrics over time or against a baseline to spot trends and understand if they align with users achieving their goals.

### Correlate traffic and satisfaction

Use insights to identify patterns:

* **High traffic and low feedback scores**: Popular pages with a poor user experience. Prioritize improving these pages.
* **Low traffic and high feedback scores**: Documentation that is working well, but might not be discoverable. Consider promoting these pages.
* **High traffic and high feedback scores**: Your documentation's greatest hits. Review these pages for ideas to improve the rest of your content.


## Qualitative feedback

Add context to your quantitative metrics with qualitative information:

* **User feedback**: Use [feedback](/insights/feedback) to capture user sentiment through ratings and open-ended comments, helping you understand what works and where users struggle.
* **Stakeholder input**: Get regular feedback from teams like support, engineering, and customer success to uncover common issues users face and areas for improvement.
* **User testing**: Conduct usability tests to validate whether users can find the answers they need and whether your documentation aligns with their expectations. See [Understand your audience](/guides/understand-your-audience) for more on user research.


## Business alignment

Measure documentation against broader business objectives:

* **Support efficiency**: Track whether your documentation reduces the volume of support tickets or improves satisfaction scores, indicating it's meeting user needs.
* **Onboarding and adoption**: Monitor how well documentation supports new users in getting up to speed, contributing to faster product adoption.
* **Retention**: Well-maintained, easy-to-follow docs contribute to positive user experiences, helping to reduce churn and improve retention rates.


## Put insights into action

Use these patterns to prioritize your documentation improvements:

* **Fix high-impact problems first**: Popular pages with poor feedback scores affect the most users.
* **Respond to user feedback**: Contextual and code snippet feedback can identify specific areas for improvement.
* **Focus on key user journeys**: Prioritize pages connected to the most important tasks for your product.



# Maintenance
Source: https://mintlify.com/docs/guides/maintenance

Tips for keeping docs up-to-date

<Tip>
  This page explains strategies for keeping your documentation accurate and valuable over time, from automated checks to content lifecycles.
</Tip>


## Automate what you can

Introduce automations where you can, such as:

* **Track stale content:** Run a script to flag important docs that haven't been updated in the last three months. Are they still accurate?
* **Automate documentation updates:** Build a workflow to automatically update documentation when code is merged with the [agent API](/guides/automate-agent).
* **Enforce standards with linters:** Use [Vale](http://Vale.sh) or [CI checks](/deploy/ci) to automatically catch formatting issues, writing style deviations, or missing metadata on every pull request.


## Set up a review process

Documentation might never be perfect, and that's okay. You should have a threshold of acceptance where documentation is functional and useful.

Balance efficiency with quality:

* **Focus on high-impact docs.** Not every page needs regular updates. Make sure the most important pages are reviewed regularly for accuracy and relevance.
* **Leverage your community.** If your docs are open-source, empower users to flag issues or submit fixes via pull requests. This builds trust and keeps content fresh.


## Know when to rewrite

Over time, documentation naturally accumulates caveats and workarounds. When incremental fixes create more confusion than clarity, a full overhaul might be the best option.

* **Plan for periodic resets.** A major cleanup, especially if best practices or the product itself has evolved significantly, saves time for your team and your users.
* **Start with a structured audit.** Interview support teams, analyze user feedback, and document what is missing, misleading, or redundant before rewriting.
* **Complete rewrites in focused sprints.** A full overhaul doesn't have to happen all at once. Prioritize sections with the biggest impact.


## Wrong docs can be worse than no docs

Outdated or misleading documentation wastes users' time and erodes trust. In cases where a page is completely inaccurate and unfixable in the short term, it's often better to remove it entirely. Users will appreciate having less information over having wrong information.



# Media
Source: https://mintlify.com/docs/guides/media

Guidelines for incorporating media

<Tip>
  This page explains best practices for using screenshots, GIFs, and videos in your documentation.
</Tip>

Screenshots, GIFs, and videos can enhance documentation but require ongoing maintenance as UI elements change. Use them selectively to avoid unnecessary upkeep.

Key guidelines:

* **Media should be supplementary.** If a workflow is clear in text alone, avoid adding visuals.
* **Ensure accessibility.** Add alt text for images, subtitles for videos, and transcripts for audio content. Many people use assistive technology and accessibile content benefits all users.
* **Balance clarity with maintainability.** Frequent UI changes can make screenshots and videos outdated quickly. Consider whether the effort to update them is worth the value they add.


## When to use media

* **Screenshots** for tasks that are difficult to explain with words.
* **GIFs** for promotional purposes and short yet complex workflows.
* **Videos** for abstract concepts and long workflows.

Use media sparingly and intentionally to avoid unnecessary documentation debt. When done right, it enhances comprehension without adding maintenance burdens or accessibility barriers.



# Migrating MDX API pages to OpenAPI navigation
Source: https://mintlify.com/docs/guides/migrating-from-mdx

Update from individual MDX endpoint pages to automated OpenAPI generation with flexible navigation

If you are currently using individual `MDX` pages for your API endpoints, you can migrate to autogenerating pages from your OpenAPI specification while retaining the customizability of individual pages. This can help you reduce the number of files you need to maintain and improve the consistency of your API documentation.

You can define metadata and content for each endpoint in your OpenAPI specification and organize endpoints where you want them in your navigation.


## CLI migration

The `mint migrate-mdx` command is the recommended way to migrate from MDX endpoint pages to autogenerated pages.

This command:

* Parses your `docs.json` navigation structure.
* Identifies MDX pages that generate OpenAPI endpoint pages.
* Extracts content from MDX files and moves it to the `x-mint` extension in your OpenAPI specification.
* Updates your `docs.json` to reference the OpenAPI endpoints directly instead of MDX files.
* Deletes the original MDX endpoint files.

<Info>
  If you already have `x-mint` defined for an endpoint and also have an MDX page with content for that endpoint, the MDX content will overwrite existing `x-mint` settings.

  If you have multiple MDX pages for the same endpoint with different content, the script will use the content from the page that appears last in your `docs.json`.

  The migration tool does not support previewing changes before applying them.
</Info>

<Steps>
  <Step title="Prepare your OpenAPI specification.">
    Ensure your OpenAPI specification is valid and includes all endpoints you want to document.

    Any MDX pages you want to migrate must have the `openapi:` frontmatter referencing an endpoint.

    <Tip>
      Validate your OpenAPI file using the [Swagger Editor](https://editor.swagger.io/) or [Mint CLI](https://www.npmjs.com/package/mint).
    </Tip>
  </Step>

  <Step title="Install the Mint CLI">
    If needed, install or update the [Mint CLI](/installation).
  </Step>

  <Step title="Run the migration command.">
    ```bash  theme={null}
    mint migrate-mdx
    ```
  </Step>
</Steps>


## Manual migration steps

<Steps>
  <Step title="Prepare your OpenAPI specification.">
    Ensure your OpenAPI specification is valid and includes all endpoints you want to document.

    For any endpoints that you want to customize the metadata or content, add the `x-mint` extension to the endpoint. See [x-mint extension](/api-playground/openapi-setup#x-mint-extension) for more details.

    For any endpoints that you want to exclude from your documentation, add the `x-hidden` extension to the endpoint.

    <Info>
      Validate your OpenAPI file using the [Swagger Editor](https://editor.swagger.io/) or [Mint CLI](https://www.npmjs.com/package/mint).
    </Info>
  </Step>

  <Step title="Update your navigation structure.">
    Replace `MDX` page references with OpenAPI endpoints in your `docs.json`.

    ```json  theme={null}
    "navigation": {
      "groups": [
        {
          "group": "API Reference",
          "openapi": "/path/to/openapi.json",
          "pages": [
            "overview",
            "authentication",
            "introduction",
            "GET /health",
            "quickstart", 
            "POST /users",
            "GET /users/{id}",
            "advanced-features"
          ]
        }
      ]
    }
    ```
  </Step>

  <Step title="Remove old MDX files.">
    After verifying your new navigation works correctly, remove the `MDX` endpoint files that you no longer need.
  </Step>
</Steps>


## Navigation patterns

You can customize how your API documentation appears in your navigation.

### Mixed content navigation

Combine automatically generated API pages with other pages:

```json  theme={null}
"navigation": {
  "groups": [
    {
      "group": "API Reference",
      "openapi": "openapi.json",
      "pages": [
        "api/overview",
        "GET /users",
        "POST /users", 
        "api/authentication"
      ]
    }
  ]
}
```

### Multiple API versions

Organize different API versions using tabs or groups:

```json  theme={null}
"navigation": {
  "tabs": [
    {
      "tab": "API v1",
      "openapi": "specs/v1.json"
    },
    {
      "tab": "API v2", 
      "openapi": "specs/v2.json"
    }
  ]
}
```


## When to use individual `MDX` pages

Consider keeping individual `MDX` pages when you need:

* Extensive custom content per endpoint like React components or lengthy examples.
* Unique page layouts.
* Experimental documentation approaches for specific endpoints.

For most use cases, OpenAPI navigation provides better maintainability and consistency.



---
**Navigation:** [← Previous](./09-pages.md) | [Index](./index.md) | [Next →](./11-organize-navigation.md)
