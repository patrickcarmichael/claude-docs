# App Deploys

**Navigation:** [← Previous](./03-how-to-reset-or-change-your-enterprise-url.md) | [Index](./index.md) | Next →

---

# App Deploys
Source: https://docs.windsurf.com/windsurf/cascade/app-deploys



App Deploys lets you deploy web applications and sites directly within Windsurf through Cascade tool calls. This feature helps you share your work through public URLs, update your deployments, and claim projects for further customization. This feature is in beta and support for additional frameworks, more robust builds, etc. are coming soon.

<Frame>
  <img src="https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/app-deploys-ui.png?fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=af9bd2cc96a163d94b37138e4b07175b" data-og-width="2072" width="2072" data-og-height="576" height="576" data-path="assets/windsurf/cascade/app-deploys-ui.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/app-deploys-ui.png?w=280&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=f7749aa40047cd53500509e6f49bad09 280w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/app-deploys-ui.png?w=560&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=0177a7044dd52ab525faea6d89a1af88 560w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/app-deploys-ui.png?w=840&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=b30f29bcf042450ad924ae857d2c9504 840w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/app-deploys-ui.png?w=1100&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=761b5d5b39f8144cb5d6934cb5aaa76e 1100w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/app-deploys-ui.png?w=1650&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=766c633b6efde77ae0c216d7511a8f71 1650w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/app-deploys-ui.png?w=2500&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=5f3e3662d6bbeee76d6ffa66c969ab6e 2500w" />
</Frame>

## Overview

With App Deploys, you can:

* Deploy a website or JS web app to a public domain
* Re-deploy to the same URL after making changes
* Claim the project to your personal account

<Warning>
  App Deploys are intended primarily for preview purposes. For production
  applications with sensitive data, we recommend claiming your deployment and
  following security best practices.
</Warning>

## Supported Providers

We currently support the following deployment provider:

* **Netlify** - For static sites and web applications

<Note>Support for additional providers are planned for future releases.</Note>

## How It Works

When you use App Deploys, your code is uploaded to our server and deployed to the provider under our umbrella account. The deployed site will be available at a public URL formatted as:

```
<SUBDOMAIN_NAME>.windsurf.build
```

<video autoPlay muted loop playsInline className="w-full aspect-video" src="https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/app-deploys-demo1.mp4?fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=844977e5cf94c8393e2418bdaec2e921" data-path="assets/windsurf/cascade/app-deploys-demo1.mp4" />

### Deployment Process

1. Cascade analyzes your project to determine the appropriate framework
2. Your project files are securely uploaded to our server
3. The deployment is created on the provider's platform
4. You receive a public URL and a claim link

### Project Configuration

To facilitate redeployment, we create a `windsurf_deployment.yaml` file at the root of your project. This file contains information for future deployments, such as a project ID and framework.

## Using App Deploys

To deploy your application, simply ask Cascade something like:

```
"Deploy this project to Netlify"
"Update my deployment"
```

Cascade will guide you through the process and help troubleshoot common issues.

## Team Deploys

<Note> You will need Team admin priveleges to toggle this feature.</Note>

Users on Teams and Enterprise plans can connect their Netlify accounts with their Windsurf accounts and deploy to their Netlify Team.

This can be toggled in Team Settings, which you can access via the Profile page or by clicking [here](https://windsurf.com/team/settings).

## Security Considerations

<Warning>
  Your code will be uploaded to our servers for deployment. Only deploy code
  that you're comfortable sharing publicly.
</Warning>

We take several precautions to ensure security:

* File size limits and validation
* Rate limiting based on your account tier
* Secure handling of project files

For added privacy, visit [clear-cookies.windsurf.build](https://clear-cookies.windsurf.build) to check for and clear any cookies set by sites under `windsurf.build`. If any cookies show up, they shouldn't be there, and clearing them helps prevent cross-site cookie issues and keeps your experience clean.

Windsurf sites are built by humans and AI, and while we encourage the AI to make best practice decisions, it's smart to stay cautious. Windsurf isn't responsible for issues caused by sites deployed by our users.

## Claiming Your Deployment

After deploying, you'll receive a claim URL. By following this link, you can claim the project on your personal provider account, giving you:

* Full control over the deployment
* Access to provider-specific features
* Ability to modify the domain name
* Direct access to logs and build information

<Note>
  Unclaimed deployments may be deleted after a certain period. We recommend
  claiming important projects promptly.
</Note>

## Rate Limits

To prevent abuse, we apply these tier-based rate limits:

| Plan | Deployments per day | Max unclaimed sites |
| ---- | ------------------- | ------------------- |
| Free | 1                   | 1                   |
| Pro  | 10                  | 5                   |

## Supported Frameworks

App Deploys works with most popular JavaScript frameworks, including:

* Next.js
* React
* Vue
* Svelte
* Static HTML/CSS/JS sites

## Troubleshooting

### Failed Deployment Build

If your deployment fails:

1. Check the build logs provided by Cascade
2. Ensure your project can build locally (run `npm run build` to test)
3. Verify that your project follows the framework's recommended structure
4. View the documentation for how to deploy [your framework to Netlify via `netlify.toml`](https://docs.netlify.com/configure-builds/file-based-configuration/)
5. Consider claiming the project to access detailed logs on the provider's dashboard

<Warning>
  We cannot provide direct support for framework-specific build errors. If your
  deployment fails due to code issues, debug locally or claim the project to
  work with the provider's support team.
</Warning>

### Netlify Site Not Found

<Frame>
  <img src="https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/netlify-site-not-found.png?fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=80793d24da70db2cfd1021616c6db559" data-og-width="2430" width="2430" data-og-height="1618" height="1618" data-path="assets/windsurf/cascade/netlify-site-not-found.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/netlify-site-not-found.png?w=280&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=cc57c11e4e864e7b79f330acba7f02a3 280w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/netlify-site-not-found.png?w=560&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=ecffcf4ed8d41cb79ca4c6fce4473af6 560w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/netlify-site-not-found.png?w=840&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=c6a9909ad8b609b0753330582460f8c4 840w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/netlify-site-not-found.png?w=1100&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=a6cc6e8cb3fc5f0ccb06160c727fceb2 1100w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/netlify-site-not-found.png?w=1650&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=0a0f34b9a8645a16037f693c1cefea62 1650w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/netlify-site-not-found.png?w=2500&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=8f84f5ba46e662de4b98bac21f0df39b 2500w" />
</Frame>

This likely means that your build failed. Please claim your site (you can find it on your [deploy history](https://windsurf.com/deploy)) and check the build logs for more details. Often times you can paste your build logs into Cascade and ask for help.

### Changing Your Subdomain / URL

#### Updating `netlify.app` domain

You can change your subdomain by claiming your deployment and updating the Netlify site settings. This will update your `.netlify.app` domain.

#### Updating custom `.windsurf.build` subdomain

<Warning>
  You cannot change your custom `.windsurf.build` subdomain after you've
  deployed. Instead, you'll need to deploy a new site with a new subdomain.
</Warning>

To update your custom `.windsurf.build` subdomain, you'll need to deploy a new site with a new subdomain:

1. Delete the `windsurf_config.yaml` file from your project
2. Ask Cascade to deploy a new site with a new subdomain and tell it which one you want
3. It can help to start a new conversation or clear your auto-generated memories so that Cascade doesn't try to re-deploy to the old subdomain
4. When you create a new deployment, you'll be able to press the "Edit" button on the subdomain UI to update it prior to pressing "Deploy"

### Error: `Unable to get project name for project ID`

This error occurs when your project ID is not found in our system of records or if Cascade is using the subdomain as the project ID incorrectly. To fix this:

1. Check that the project still exists in your Netlify account (assuming it is claimed).
2. Check that the project ID is in the `windsurf_deployment.yaml` file. If it is not in the file, you can download your config file from your [deploy history](https://windsurf.com/deploy) dropdown.
3. Try redeploying and telling Cascade to use the `project_id` from the `windsurf_deployment.yaml` file more explicitly

<Frame>
  <img src="https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/app-deploys-download-config-file.png?fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=8e8633a61f54753db07de541413ace9c" data-og-width="1966" width="1966" data-og-height="1408" height="1408" data-path="assets/windsurf/cascade/app-deploys-download-config-file.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/app-deploys-download-config-file.png?w=280&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=60858082545eaa214b3c4eede56279e8 280w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/app-deploys-download-config-file.png?w=560&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=262cdbb04ab309fe91e469534873d941 560w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/app-deploys-download-config-file.png?w=840&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=5ad571a090d3aa725da55c434845c15d 840w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/app-deploys-download-config-file.png?w=1100&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=ee0aee2445e04bb2414d59d47b449464 1100w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/app-deploys-download-config-file.png?w=1650&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=9372bc2d4014f98662fed8de06b2f8b6 1650w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/app-deploys-download-config-file.png?w=2500&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=ef554e119347a1df792558d90e9b6284 2500w" />
</Frame>



# Overview
Source: https://docs.windsurf.com/windsurf/cascade/cascade



Windsurf's Cascade unlocks a new level of collaboration between human and AI.

To open Cascade, press `Cmd/Ctrl+L`click the Cascade icon in the top right corner of the Windsurf window. Any selected text in the editor or terminal will automatically be included.

### Quick links to features

<CardGroup cols={2}>
  <Card title="Web Search" icon="globe-pointer" href="/windsurf/web-search">
    Search the web for information to be referenced in Cascade's suggestions.
  </Card>

  <Card title="Memories & Rules" icon="cloud-word" href="/windsurf/memories">
    Memories and rules help customize behavior.
  </Card>
</CardGroup>

<CardGroup cols={2}>
  <Card title="MCP" icon="hammer" href="/windsurf/mcp">
    MCP servers extend the agent's capabilities.
  </Card>

  <Card title="Terminal" icon="terminal" href="/windsurf/terminal">
    An upgraded Terminal experience.
  </Card>
</CardGroup>

<CardGroup cols={2}>
  <Card title="Workflows" icon="list" href="/windsurf/cascade/workflows">
    Automate repetitive trajectories.
  </Card>

  <Card title="App Deploys" icon="rocket" href="/windsurf/cascade/app-deploys">
    Deploy applications in one click.
  </Card>
</CardGroup>


# Model selection

Select your desired model from the selection menu below the Cascade conversation input box. Click below too see the full list of the available models and their availability across different plans and pricing.

<Card title="Models" icon="gear-code" href="/windsurf/models" horizontal={true}>
  Model availability in Windsurf.
</Card>


# Cascade Code / Cascade Chat

Cascade comes in two primary modes: **Code** and **Chat**.

Code mode allows Cascade to create and make modifications to your codebase, while Chat mode is optimized for questions around your codebase or general coding principles.

While in Chat mode, Cascade may propose new code to you that you can accept and insert.


# Plans and Todo Lists

Cascade has built-in planning capabilities that help improve performance for longer tasks.

In the background, a specialized planning agent continuously refines the long-term plan while your selected model focuses on taking short-term actions based on that plan.

Cascade will create a Todo list within the conversation to track progress on complex tasks. To make changes to the plan, simply ask Cascade to make updates to the Todo list.

Cascade may also automatically make updates to the plan as it picks up new information, such as a [Memory](/windsurf/memories), during the course of a conversation.


# Queued Messages

While you are waiting for Cascade to finish its current task, you can queue up new messages to execute in order once the task is complete.

To add a message to the queue, simply type in your message while Cascade is working and press `Enter`.

* **Send immediately**: Press Enter again on an empty text box to send it right away.
* **Delete**: Remove any message from the queue before it's sent


# Tool Calling

Cascade has a variety of tools at its disposal, such as Search, Analyze, [Web Search](/windsurf/web-search), [MCP](/windsurf/mcp), and the [terminal](/windsurf/terminal).

It can detect which packages and tools that you're using, which ones need to be installed, and even install them for you. Just ask Cascade how to run your project and press Accept.

<Note>Cascade can make up to 20 tool calls per prompt. If the trajectory stops, simply press the `continue` button and Cascade will resume from where it left off. However, each `continue` will count as a new prompt credit due to tool calling costs.</Note>

You can configure an `Auto-Continue` setting to have Cascade automatically continue its response if it hits a limit. These will consume a prompt credit(s) corresponding to the model you are using.

<Frame>
  <video autoPlay muted loop playsInline src="https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/auto-continue.mp4?fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=0f75d2d9de596f1ead6f37c4f68eca43" data-path="assets/windsurf/cascade/auto-continue.mp4" />
</Frame>


# Voice input

Use Voice input to use your voice to interact with Cascade. In its current form it can transcribe your speech to text.

<video autoPlay controls muted loop playsInline className="w-full aspect-video" src="https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/voice-mode.mp4?fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=b6881ef11385d4f05fa151e0808a9e78" data-path="assets/windsurf/cascade/voice-mode.mp4" />


# Named Checkpoints and Reverts

You have the ability to revert changes that Cascade has made. Simply hover your mouse over the original prompt and click on the revert arrow on the right, or revert directly from the table of contents. This will revert all code changes back to the state of your codebase at the desired step.

<Warning>Reverts are currently irreversible, so be careful!</Warning>

<video autoPlay controls muted loop playsInline className="w-full aspect-video" src="https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/cascade-revert.mp4?fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=fe494383062acfc1efe07b23c03607a2" data-path="assets/windsurf/cascade/cascade-revert.mp4" />

You can also create a named snapshot/checkpoint of the current state of your project from within the conversation, which you can easily navigate to and revert at any time.

<video autoPlay controls muted loop playsInline className="w-full aspect-video" src="https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/namedcheckpoints.mp4?fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=d3c50b95ea5c2e67c2f08f00af4d11f6" data-path="assets/windsurf/cascade/namedcheckpoints.mp4" />


# Real-time awareness

A unique capability of Windsurf and Cascade is that it is aware of your real-time actions, removing the need to prompt with context on your prior actions.

Simply instruct Cascade to "Continue".

<video autoPlay controls muted loop playsInline className="w-full aspect-video" src="https://mintcdn.com/codeium/vRt4FQOyBeZpD2Pu/assets/windsurf-continue.mp4?fit=max&auto=format&n=vRt4FQOyBeZpD2Pu&q=85&s=72fa8688e966ff308daa5876e6dc7f98" data-path="assets/windsurf-continue.mp4" />


# Send problems to Cascade

When you have problems in your code which show up in the Problems panel at the bottom of the editor, simply click the `Send to Cascade` button to bring them into the Cascade panel as an @ mention.

<Frame>
  <img style={{ maxHeight: "500px" }} src="https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/send-problems-to-cascade.png?fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=46a20b503cb0cda0139ab1b081ca3de3" data-og-width="316" width="316" data-og-height="122" height="122" data-path="assets/windsurf/cascade/send-problems-to-cascade.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/send-problems-to-cascade.png?w=280&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=28061b4d7f851d8840f436f8b0919e15 280w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/send-problems-to-cascade.png?w=560&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=93934a76820912a1fd5a1778cf641844 560w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/send-problems-to-cascade.png?w=840&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=0aab2818d64a7b08e266baacf6560cce 840w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/send-problems-to-cascade.png?w=1100&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=fe744688100032ab1c298e97ef822efc 1100w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/send-problems-to-cascade.png?w=1650&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=8d794127338249c9fbc74399ac7d1414 1650w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/send-problems-to-cascade.png?w=2500&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=74ef3a1d9023525aeea7ca654149a3b4 2500w" />
</Frame>


# Explain and fix

For any errors that you run into from within the editor, you can simply highlight the error and click `Explain and Fix` to have Cascade fix it for you.

<Frame>
  <img style={{ maxHeight: "500px" }} src="https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/windsurf-explain-fix.png?fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=e2d18a81a54554b523805d75317488f5" data-og-width="886" width="886" data-og-height="140" height="140" data-path="assets/windsurf/windsurf-explain-fix.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/windsurf-explain-fix.png?w=280&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=79109955cb9719ec411c6f41ff2a4f52 280w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/windsurf-explain-fix.png?w=560&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=a122405e2d8bf975f03842eb63fda6e3 560w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/windsurf-explain-fix.png?w=840&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=628e64768d102e28f380f1d5f8c1a770 840w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/windsurf-explain-fix.png?w=1100&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=13161a7f834d458a9436b337d67cc58f 1100w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/windsurf-explain-fix.png?w=1650&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=1d9ebea051ccb1a80798c57e2ef2b89b 1650w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/windsurf-explain-fix.png?w=2500&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=c2e9a3082c59fe0299d68fcfd74b4185 2500w" />
</Frame>


# Ignoring files

If you'd like Cascade to ignore files, you can add your files to `.codeiumignore` at the root of your workspace. This will prevent Cascade from viewing, editing or creating files inside of the paths designated. You can declare the file paths in a format similar to `.gitignore`.

## Global .codeiumignore

For enterprise customers managing multiple repositories, you can enforce ignore rules across all repositories by placing a global `.codeiumignore` file in the `~/.codeium/` folder. This global configuration will apply to all Windsurf workspaces on your system and works in addition to any repository-specific `.codeiumignore` files.


# Linter integration

Cascade can automatically fix linting errors on generated code. This is turned on by default, but it can be disabled by clicking `Auto-fix` on the tool call, and clicking `disable`. This edit will not consume any credits.

<Frame>
  <img src="https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/auto-fix-lint.png?fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=ae3f3ecca77f0a0a646adedb91b6a22e" data-og-width="584" width="584" data-og-height="196" height="196" data-path="assets/windsurf/cascade/auto-fix-lint.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/auto-fix-lint.png?w=280&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=4c3726305eed4f34d6985a4fe06b5816 280w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/auto-fix-lint.png?w=560&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=fb969e8bfe739b9daa9d0ef6284a19fe 560w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/auto-fix-lint.png?w=840&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=462f5f2e5fd3f6e632bf417c35f739bd 840w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/auto-fix-lint.png?w=1100&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=651fa582a7c313772372a49bad3438b1 1100w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/auto-fix-lint.png?w=1650&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=1aed8edc51e41f0121e93d5dd253be07 1650w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/auto-fix-lint.png?w=2500&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=0c3129926f6965afb414bf5e5dd641cd 2500w" />
</Frame>

When Cascade makes an edit with the primary goal of fixing lints that it created and auto-detected,
it may discount the edit to be free of credit charge. This is in recognition of the fact that
fixing lint errors increases the number of tool calls that Cascade makes.


# Sounds for Cascade

Play a sound when Cascade finishes a trajectory to let you know when it's done. You can enable it via `Windsurf Settings` > `Cascade` > `Enable Sounds for Cascade`.


# Sharing your conversation

<Note>This feature is currently only available for Teams and Enterprise customers. Currently not available to Hybrid customers.</Note>

You can share your Cascade trajectories with your team by clicking the `...` Additional options button in the top right of the Cascade panel, and clicking `Share Conversation`.


# @-mention previous conversations

You can also reference previous conversations with other conversations via an `@-mention`.

When you do this, Cascade will retrieve the most relevant and useful information like the conversation summaries and checkpoints, and specific parts of the conversation that you query for. It typically will not retrieve the full conversation as to not overwhelm the context window.

<video autoPlay controls muted loop playsInline className="w-full aspect-video" src="https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/at-mention-convos.mp4?fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=f580f0222fdf75ec42cb7a9470e6de02" data-path="assets/windsurf/cascade/at-mention-convos.mp4" />


# Simultaneous Cascades

Users can have multiple Cascades running simultaneously. You can navigate between them using the dropdown menu in the top left of the Cascade panel.

<Warning>If two Cascades edit the same file at the same time, the edits can race, and sometimes the second edit will fail.</Warning>



# Cascade Hooks (Beta)
Source: https://docs.windsurf.com/windsurf/cascade/hooks



Cascade Hooks enable you to execute custom shell commands at key points during Cascade's workflow. This powerful extensibility feature allows you to log operations, enforce guardrails, run validation checks, or integrate with external systems.

<Warning>
  **Beta Release**: Cascade Hooks are currently in beta and undergoing active development. Features and APIs may change. Please contact [Windsurf Support](https://windsurf.com/support) with feedback or bug reports.
</Warning>

<Note>
  Hooks are designed for power users and enterprise teams who need fine-grained control over Cascade's behavior. They require basic shell scripting knowledge.
</Note>

## What You Can Build

Hooks unlock a wide range of automation and governance capabilities:

* **Logging & Analytics**: Track every file read, code change, or command executed by Cascade for compliance and usage analysis
* **Security Controls**: Block Cascade from accessing sensitive files or running dangerous commands
* **Quality Assurance**: Run linters, formatters, or tests automatically after code modifications
* **Custom Workflows**: Integrate with issue trackers, notification systems, or deployment pipelines
* **Team Standardization**: Enforce coding standards and best practices across your organization

## How Hooks Work

Hooks are shell commands that run automatically when specific Cascade actions occur. Each hook:

1. **Receives context** (details about the action being performed) via JSON as standard input
2. **Executes your script** - Python, Bash, Node.js, or any executable
3. **Returns a result** via exit code and output streams

For **pre-hooks** (executed before an action), your script can **block the action** by exiting with exit code `2`. This makes pre-hooks ideal for implementing security policies or validation checks.

## Configuration

Hooks are configured in JSON files that can be placed at three different levels. Cascade loads and merges hooks from all locations, giving teams flexibility in how they distribute and manage hook configurations.

#### System-Level

System-level hooks are ideal for organization-wide policies enforced on shared development machines. For example, you can use them to enforce security policies, compliance requirements, or mandatory code review workflows.

* **macOS**: `/Library/Application Support/Windsurf/hooks.json`
* **Linux/WSL**: `/etc/windsurf/hooks.json`
* **Windows**: `C:\ProgramData\Windsurf\hooks.json`

#### User-Level

User-level hooks are perfect for personal preferences and optional workflows.

* **Location**: `~/.codeium/windsurf/hooks.json`

#### Workspace-Level

Workspace-level hooks allow teams to version control project-specific policies alongside their code. They may include custom validation rules, project-specific integrations, or team-specific workflows.

* **Location**: `.windsurf/hooks.json` in your workspace root

<Note>
  Hooks from all three locations are **merged together**. If the same hook event is configured in multiple locations, all hooks will execute in order: system → user → workspace.
</Note>

### Basic Structure

Here is an example of the basic structure of the hooks configuration:

```json  theme={null}
{
  "hooks": {
    "pre_read_code": [
      {
        "command": "python3 /path/to/your/script.py",
        "show_output": true
      }
    ],
    "post_write_code": [
      {
        "command": "python3 /path/to/another/script.py",
        "show_output": true
      }
    ]
  }
}
```

### Configuration Options

Each hook accepts the following parameters:

| Parameter           | Type    | Description                                                                                             |
| ------------------- | ------- | ------------------------------------------------------------------------------------------------------- |
| `command`           | string  | The shell command to execute. Can be any valid executable with arguments.                               |
| `show_output`       | boolean | Whether to display the hook's stdout/stderr output on the user-facing Cascade UI. Useful for debugging. |
| `working_directory` | string  | Optional. The directory to execute the command from. Defaults to your workspace root.                   |

## Hook Events

Cascade provides eight hook events that cover the most critical actions in the agent workflow.

### Common Input Structure

All hooks receive a JSON object with the following common fields:

| Field               | Type   | Description                                                        |
| ------------------- | ------ | ------------------------------------------------------------------ |
| `agent_action_name` | string | The hook event name (e.g., "pre\_read\_code", "post\_write\_code") |
| `trajectory_id`     | string | Unique identifier for the overall Cascade conversation             |
| `execution_id`      | string | Unique identifier for the single agent turn                        |
| `timestamp`         | string | ISO 8601 timestamp when the hook was triggered                     |
| `tool_info`         | object | Event-specific information (varies by hook type)                   |

In the following examples, the common fields are omitted for brevity. There are eight major types of hook events:

### pre\_read\_code

Triggered **before** Cascade reads a code file. This may block the action if the hook exits with code 2.

**Use cases**: Restrict file access, log read operations, check permissions

**Input JSON**:

```json  theme={null}
{
  "agent_action_name": "pre_read_code",
  "tool_info": {
    "file_path": "/Users/yourname/project/file.py"
  }
}
```

This `file_path` may be a directory path when Cascade reads a directory recursively.

### post\_read\_code

Triggered **after** Cascade successfully reads a code file.

**Use cases**: Log successful reads, track file access patterns

**Input JSON**:

```json  theme={null}
{
  "agent_action_name": "post_read_code",
  "tool_info": {
    "file_path": "/Users/yourname/project/file.py"
  }
}
```

This `file_path` may be a directory path when Cascade reads a directory recursively.

### pre\_write\_code

Triggered **before** Cascade writes or modifies a code file. This may block the action if the hook exits with code 2.

**Use cases**: Prevent modifications to protected files, backup files before changes

**Input JSON**:

```json  theme={null}
{
  "agent_action_name": "pre_write_code",
  "tool_info": {
    "file_path": "/Users/yourname/project/file.py",
    "edits": [
      {
        "old_string": "def old_function():\n    pass",
        "new_string": "def new_function():\n    return True"
      }
    ]
  }
}
```

### post\_write\_code

Triggered **after** Cascade writes or modifies a code file.

**Use cases**: Run linters, formatters, or tests; log code changes

**Input JSON**:

```json  theme={null}
{
  "agent_action_name": "post_write_code",
  "tool_info": {
    "file_path": "/Users/yourname/project/file.py",
    "edits": [
      {
        "old_string": "import os",
        "new_string": "import os\nimport sys"
      }
    ]
  }
}
```

### pre\_run\_command

Triggered **before** Cascade executes a terminal command. This may block the action if the hook exits with code 2.

**Use cases**: Block dangerous commands, log all command executions, add safety checks

**Input JSON**:

```json  theme={null}
{
  "agent_action_name": "pre_run_command",
  "tool_info": {
    "command_line": "npm install package-name",
    "cwd": "/Users/yourname/project"
  }
}
```

### post\_run\_command

Triggered **after** Cascade executes a terminal command.

**Use cases**: Log command results, trigger follow-up actions

**Input JSON**:

```json  theme={null}
{
  "agent_action_name": "post_run_command",
  "tool_info": {
    "command_line": "npm install package-name",
    "cwd": "/Users/yourname/project"
  }
}
```

### pre\_mcp\_tool\_use

Triggered **before** Cascade invokes an MCP (Model Context Protocol) tool. This may block the action if the hook exits with code 2.

**Use cases**: Log MCP usage, restrict which MCP tools can be used

**Input JSON**:

```json  theme={null}
{
  "agent_action_name": "pre_mcp_tool_use",
  "tool_info": {
    "mcp_server_name": "github",
    "mcp_tool_arguments": {
      "owner": "code-owner",
      "repo": "my-cool-repo",
      "title": "Bug report",
      "body": "Description of the bug here"
    },
    "mcp_tool_name": "create_issue"
  }
}
```

### post\_mcp\_tool\_use

Triggered **after** Cascade successfully invokes an MCP tool.

**Use cases**: Log MCP operations, track API usage, see MCP results

**Input JSON**:

```json  theme={null}
{
  "agent_action_name": "post_mcp_tool_use",
  "tool_info": {
    "mcp_result": "...",
    "mcp_server_name": "github",
    "mcp_tool_arguments": {
      "owner": "code-owner",
      "perPage": 1,
      "repo": "my-cool-repo",
      "sha": "main"
    },
    "mcp_tool_name": "list_commits"
  }
}
```

## Exit Codes

Your hook scripts communicate results through exit codes:

| Exit Code | Meaning        | Effect                                                                                               |
| --------- | -------------- | ---------------------------------------------------------------------------------------------------- |
| `0`       | Success        | Action proceeds normally                                                                             |
| `2`       | Blocking Error | The Cascade agent will see the error message from stderr. For pre-hooks, this **blocks** the action. |
| Any other | Error          | Action proceeds normally                                                                             |

<Warning>
  Only **pre-hooks** (pre\_read\_code, pre\_write\_code, pre\_run\_command, pre\_mcp\_tool\_use) can block actions using exit code 2. Post-hooks cannot block since the action has already occurred.
</Warning>

Keep in mind that the user can see any hook-generated standard output and standard error in the Cascade UI if `show_output` is true.

## Example Use Cases

### Logging All Cascade Actions

Track every action Cascade takes for auditing purposes.

**Config** (`~/.codeium/windsurf/hooks.json`):

```json  theme={null}
{
  "hooks": {
    "post_read_code": [
      {
        "command": "python3 /Users/yourname/hooks/log_input.py",
        "show_output": true
      }
    ],
    "post_write_code": [
      {
        "command": "python3 /Users/yourname/hooks/log_input.py",
        "show_output": true
      }
    ],
    "post_run_command": [
      {
        "command": "python3 /Users/yourname/hooks/log_input.py",
        "show_output": true
      }
    ],
    "post_mcp_tool_use": [
      {
        "command": "python3 /Users/yourname/hooks/log_input.py",
        "show_output": true
      }
    ]
  }
}
```

**Script** (`log_input.py`):

```python  theme={null}
#!/usr/bin/env python3

import sys
import json

def main():
    # Read the JSON data from stdin
    input_data = sys.stdin.read()
    
    # Parse the JSON
    try:
        data = json.loads(input_data)
        
        # Write formatted JSON to file
        with open("/Users/yourname/hooks/input.txt", "a") as f:
            f.write('\n' + '='*80 + '\n')
            f.write(json.dumps(data, indent=2, separators=(',', ': ')))
            f.write('\n')
    
        print(json.dumps(data, indent=2))
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```

This script appends every hook invocation to a log file, creating an audit trail of all Cascade actions. You may transform the input data or perform custom logic as you see fit.

### Restricting File Access

Prevent Cascade from reading files outside a specific directory.

**Config** (`~/.codeium/windsurf/hooks.json`):

```json  theme={null}
{
  "hooks": {
    "pre_read_code": [
      {
        "command": "python3 /Users/yourname/hooks/block_read_access.py",
        "show_output": true
      }
    ]
  }
}
```

**Script** (`block_read_access.py`):

```python  theme={null}
#!/usr/bin/env python3

import sys
import json

ALLOWED_PREFIX = "/Users/yourname/my-project/"

def main():
    # Read the JSON data from stdin
    input_data = sys.stdin.read()

    # Parse the JSON
    try:
        data = json.loads(input_data)

        if data.get("agent_action_name") == "pre_read_code":
            tool_info = data.get("tool_info", {})
            file_path = tool_info.get("file_path", "")
            
            if not file_path.startswith(ALLOWED_PREFIX):
                print(f"Access denied: Cascade is only allowed to read files under {ALLOWED_PREFIX}", file=sys.stderr)
                sys.exit(2)  # Exit code 2 blocks the action
            
            print(f"Access granted: {file_path}", file=sys.stdout)

    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```

When Cascade attempts to read a file outside the allowed directory, this hook blocks the operation and displays an error message.

### Blocking Dangerous Commands

Prevent Cascade from executing potentially harmful commands.

**Config** (`~/.codeium/windsurf/hooks.json`):

```json  theme={null}
{
  "hooks": {
    "pre_run_command": [
      {
        "command": "python3 /Users/yourname/hooks/block_dangerous_commands.py",
        "show_output": true
      }
    ]
  }
}
```

**Script** (`block_dangerous_commands.py`):

```python  theme={null}
#!/usr/bin/env python3

import sys
import json

DANGEROUS_COMMANDS = ["rm -rf", "sudo rm", "format", "del /f"]

def main():
    # Read the JSON data from stdin
    input_data = sys.stdin.read()

    # Parse the JSON
    try:
        data = json.loads(input_data)

        if data.get("agent_action_name") == "pre_run_command":
            tool_info = data.get("tool_info", {})
            command = tool_info.get("command_line", "")

            for dangerous_cmd in DANGEROUS_COMMANDS:
                if dangerous_cmd in command:
                    print(f"Command blocked: '{dangerous_cmd}' is not allowed for safety reasons.", file=sys.stderr)
                    sys.exit(2)  # Exit code 2 blocks the command
            
            print(f"Command approved: {command}", file=sys.stdout)

    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```

This hook scans commands for dangerous patterns and blocks them before execution.

### Running Code Formatters After Edits

Automatically format code files after Cascade modifies them.

**Config** (`~/.codeium/windsurf/hooks.json`):

```json  theme={null}
{
  "hooks": {
    "post_write_code": [
      {
        "command": "bash /Users/yourname/hooks/format_code.sh",
        "show_output": false
      }
    ]
  }
}
```

**Script** (`format_code.sh`):

```bash  theme={null}
#!/bin/bash


# Read JSON from stdin
input=$(cat)


# Extract file path using jq
file_path=$(echo "$input" | jq -r '.tool_info.file_path')


# Format based on file extension
if [[ "$file_path" == *.py ]]; then
    black "$file_path" 2>&1
    echo "Formatted Python file: $file_path"
elif [[ "$file_path" == *.js ]] || [[ "$file_path" == *.ts ]]; then
    prettier --write "$file_path" 2>&1
    echo "Formatted JS/TS file: $file_path"
elif [[ "$file_path" == *.go ]]; then
    gofmt -w "$file_path" 2>&1
    echo "Formatted Go file: $file_path"
fi

exit 0
```

This hook automatically runs the appropriate formatter based on the file type after each edit.

## Best Practices

### Security

<Warning>
  **Use Cascade Hooks at Your Own Risk**: Hooks execute shell commands automatically with your user account's full permissions. You are entirely responsible for the code you configure. Poorly designed or malicious hooks can modify files, delete data, expose credentials, or compromise your system.
</Warning>

* **Validate all inputs**: Never trust the input JSON without validation, especially for file paths and commands.
* **Use absolute paths**: Always use absolute paths in your hook configurations to avoid ambiguity.
* **Protect sensitive data**: Avoid logging sensitive information like API keys or credentials.
* **Review permissions**: Ensure your hook scripts have appropriate file system permissions.
* **Audit before deployment**: Review every hook command and script before adding to your configuration.
* **Test in isolation**: Run hooks in a test environment before enabling them on your primary development machine.

### Performance Considerations

* **Keep hooks fast**: Slow hooks will impact Cascade's responsiveness. Aim for sub-100ms execution times.
* **Use async operations**: For non-blocking hooks, consider logging to a queue or database asynchronously.
* **Filter early**: Check the action type at the start of your script to avoid unnecessary processing.

### Error Handling

* **Always validate JSON**: Use try-catch blocks to handle malformed input gracefully.
* **Log errors properly**: Write errors to `stderr` so they're visible when `show_output` is enabled.
* **Fail safely**: If your hook encounters an error, consider whether it should block the action or allow it to proceed.

### Testing Your Hooks

1. **Start with logging**: Begin by implementing a simple logging hook to understand the data flow.
2. **Use `show_output: true`**: Enable output during development to see what your hooks are doing.
3. **Test blocking behavior**: Verify that exit code 2 properly blocks actions in pre-hooks.
4. **Check all code paths**: Test both success and failure scenarios in your scripts.

## Enterprise Distribution

Enterprise organizations need to enforce security policies, compliance requirements, and development standards that individual users cannot bypass. Cascade Hooks supports this through **system-level configuration**, which takes precedence and cannot be disabled by end users without root permissions.

Deploy your mandatory `hooks.json` configuration to these OS-specific locations:

**macOS:**

```
/Library/Application Support/Windsurf/hooks.json
```

**Linux/WSL:**

```
/etc/windsurf/hooks.json
```

**Windows:**

```
C:\ProgramData\Windsurf\hooks.json
```

Place your hook scripts in a corresponding system directory (e.g., `/usr/local/share/windsurf-hooks/` on Unix systems).

### Deployment Methods

Enterprise IT teams can deploy system-level hooks using standard tools and workflows:

**Mobile Device Management (MDM)**

* **Jamf Pro** (macOS) - Deploy via configuration profiles or scripts
* **Microsoft Intune** (Windows/macOS) - Use PowerShell scripts or policy deployment
* **Workspace ONE**, **Google Endpoint Management**, and other MDM solutions

**Configuration Management**

* **Ansible**, **Puppet**, **Chef**, **SaltStack** - Use your existing infrastructure automation
* **Custom deployment scripts** - Shell scripts, PowerShell, or your preferred tooling

### Verification and Auditing

After deployment, verify that hooks are properly installed and cannot be bypassed:

```bash  theme={null}

# Verify system hooks are present
ls -la /etc/windsurf/hooks.json  # Linux
ls -la "/Library/Application Support/Windsurf/hooks.json"  # macOS


# Test hook execution (should see hook output in Cascade)

# Have a developer trigger the relevant Cascade action


# Verify users cannot modify system hooks
sudo chown root:root /etc/windsurf/hooks.json
sudo chmod 644 /etc/windsurf/hooks.json
```

<Note>
  **Important**: System-level hooks are entirely managed by your IT or security team. Windsurf does not deploy or manage files at system-level paths. Ensure your internal teams handle deployment, updates, and compliance according to your organization's policies.
</Note>

### Workspace Hooks for Team Projects

For project-specific conventions, teams can use workspace-level hooks in version control:

```bash  theme={null}

# Add to your repository
.windsurf/
├── hooks.json
└── scripts/
    └── format-check.py


# Commit to git
git add .windsurf/
git commit -m "Add workspace hooks for code formatting"
```

This allows teams to standardize development practices. Be sure to keep security-critical policies at the system level, and be sure not to check in any sensitive information to version control.

## Additional Resources

* **MCP Integration**: Learn more about [Model Context Protocol in Windsurf](/windsurf/cascade/mcp)
* **Workflows**: Discover how to combine hooks with [Cascade Workflows](/windsurf/cascade/workflows)
* **Analytics**: Track Cascade usage with [Team Analytics](/windsurf/accounts/analytics)



# Model Context Protocol (MCP)
Source: https://docs.windsurf.com/windsurf/cascade/mcp



**MCP (Model Context Protocol)** is a protocol that enables LLMs to access custom tools and services.
An MCP client (Cascade, in this case) can make requests to MCP servers to access tools that they provide.
Cascade now natively integrates with MCP, allowing you to bring your own selection of MCP servers for Cascade to use.
See the [official MCP docs](https://modelcontextprotocol.io/) for more information.

<Note>Enterprise users must manually turn this on via settings</Note>

## Adding a new MCP plugin

New MCP plugins can be added from the Plugin Store, which you can access by clicking on the `Plugins` icon in the top right menu in the Cascade panel, or from the `Windsurf Settings` > `Cascade` > `Plugins` section.

If you cannot find your desired MCP plugin, you can add it manually by editing the raw `mcp_config.json` file.

Official MCP plugins will show up with a blue checkmark, indicating that they are made by the parent service company.

When you click on a plugin, simply click `Install` to expose the server and its tools to Cascade.

Windsurf supports two [transport types](https://modelcontextprotocol.io/docs/concepts/transports) for MCP servers: `stdio` and `http`.

For `http` servers, the URL should reflect that of the endpoint and resemble `https://<your-server-url>/mcp`.

We can also support streamable HTTP transport and MCP Authentication.

<Note>Make sure to press the refresh button after you add a new MCP plugin.</Note>

<Frame>
  <img src="https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/mcp/mcp-plugin-store.png?fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=d755c65b22df71e8d035f440cb2fff22" data-og-width="1138" width="1138" data-og-height="828" height="828" data-path="assets/windsurf/cascade/mcp/mcp-plugin-store.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/mcp/mcp-plugin-store.png?w=280&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=a7e3ab90cf04cdfabbdd580f83aea2b2 280w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/mcp/mcp-plugin-store.png?w=560&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=0011e35c9f6a2202f26e3485ef017b2c 560w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/mcp/mcp-plugin-store.png?w=840&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=92c63c6e862e266842486022c402866d 840w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/mcp/mcp-plugin-store.png?w=1100&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=26f17c37647e79435ca3ade47e087147 1100w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/mcp/mcp-plugin-store.png?w=1650&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=1202cfe8ef04923199de9625ffe8aaa6 1650w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/mcp/mcp-plugin-store.png?w=2500&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=d582ec77762e3e0ca99d65d5525e64a6 2500w" />
</Frame>

## Configuring MCP tools

Each plugin has a certain number of tools it has access to. Cascade has a limit of 100 total tools that it has access to at any given time.

At the plugin level, you can navigate to the Tools tab and toggle the tools that you wish to enable. Or, from the `Windsurf Settings`, you can click on the `Manage plugins` button.

<Frame>
  <img src="https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/mcp/mcp-manage-plugin-tools.png?fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=30757b56f44e15c789a6f9f50dfa6035" data-og-width="1130" width="1130" data-og-height="700" height="700" data-path="assets/windsurf/cascade/mcp/mcp-manage-plugin-tools.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/mcp/mcp-manage-plugin-tools.png?w=280&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=ba55e144bbb094c2cc9425c5225a01a1 280w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/mcp/mcp-manage-plugin-tools.png?w=560&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=f3b5992248f1c307fec42269b6172b43 560w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/mcp/mcp-manage-plugin-tools.png?w=840&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=a4d03feb4bc0128fab8236a5184f5aed 840w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/mcp/mcp-manage-plugin-tools.png?w=1100&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=4067473f9a179c67e3dabd16db2c870b 1100w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/mcp/mcp-manage-plugin-tools.png?w=1650&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=1b6598d6418581175716d87b40903fee 1650w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/mcp/mcp-manage-plugin-tools.png?w=2500&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=5d12db70cab4e15dbf199f629d4d40d4 2500w" />
</Frame>

## mcp\_config.json

The `~/.codeium/windsurf/mcp_config.json` file is a JSON file that contains a list of servers that Cascade can connect to.

The JSON should follow the same schema as the config file for Claude Desktop.

Here’s an example configuration, which sets up a single server for GitHub:

```json  theme={null}
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-github"
      ],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "<YOUR_PERSONAL_ACCESS_TOKEN>"
      }
    }
  }
}
```

It's important to note that for HTTP servers, the configuration is slightly different and requires a `serverUrl` field.

Here's an example configuration for an HTTP server:

```json  theme={null}
{
  "mcpServers": {
    "figma": {
      "serverUrl": "<your-server-url>/mcp"
    }
  }
}
```

<Note>For Figma Dev Mode MCP server, make sure you have updated to the latest Figma desktop app version to use the new `/mcp` endpoint.</Note>

Be sure to provide the required arguments and environment variables for the servers that you want to use.

See the [official MCP server reference repository](https://github.com/modelcontextprotocol/servers) or [OpenTools](https://opentools.com/) for some example servers.

## Admin Controls (Teams & Enterprises)

Team admins can toggle MCP access for their team, as well as whitelist approved MCP servers for their team to use:

<Card title="MCP Team Settings" horizontal={true} icon="hammer" href="https://windsurf.com/team/settings">
  Configurable MCP settings for your team.
</Card>

<Warning>The above link will only work if you have admin privileges for your team.</Warning>

By default, users within a team will be able to configure their own MCP servers. However, once you whitelist even a single MCP server, **all non-whitelisted servers will be blocked** for your team.

### How Server Matching Works

When you whitelist an MCP server, the system uses **regex pattern matching** with the following rules:

* **Full String Matching**: All patterns are automatically anchored (wrapped with `^(?:pattern)$`) to prevent partial matches
* **Command Field**: Must match exactly or according to your regex pattern
* **Arguments Array**: Each argument is matched individually against its corresponding pattern
* **Array Length**: The number of arguments must match exactly between whitelist and user config
* **Special Characters**: Characters like `$`, `.`, `[`, `]`, `(`, `)` have special regex meaning and should be escaped with `\` if you want literal matching

### Configuration Options

<AccordionGroup>
  <Accordion title="Option 1: Plugin Store Default (Recommended)" description="Leave the Server Config (JSON) field empty to allow the default configuration from the Windsurf MCP Plugin Store.">
    **Admin Whitelist Configuration:**

    * **Server ID**: `github-mcp-server`
    * **Server Config (JSON)**: *(leave empty)*

    ```json  theme={null}
    {}
    ```

    **Matching User Config (`mcp_config.json`):**

    ```json  theme={null}
    {
      "mcpServers": {
        "github-mcp-server": {
          "command": "docker",
          "args": [
            "run",
            "-i",
            "--rm",
            "-e",
            "GITHUB_PERSONAL_ACCESS_TOKEN",
            "ghcr.io/github/github-mcp-server"
          ],
          "env": {
            "GITHUB_PERSONAL_ACCESS_TOKEN": "ghp_your_token_here"
          }
        }
      }
    }
    ```

    This allows users to install the GitHub MCP server with any valid configuration, as long as the server ID matches the plugin store entry.
  </Accordion>

  <Accordion title="Option 2: Exact Match Configuration" description="Provide the exact configuration that users must use. Users must match this configuration exactly.">
    **Admin Whitelist Configuration:**

    * **Server ID**: `github-mcp-server`
    * **Server Config (JSON)**:

    ```json  theme={null}
    {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "-e",
        "GITHUB_PERSONAL_ACCESS_TOKEN",
        "ghcr.io/github/github-mcp-server"
      ],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": ""
      }
    }
    ```

    **Matching User Config (`mcp_config.json`):**

    ```json  theme={null}
    {
      "mcpServers": {
        "github-mcp-server": {
          "command": "docker",
          "args": [
            "run",
            "-i",
            "--rm",
            "-e",
            "GITHUB_PERSONAL_ACCESS_TOKEN",
            "ghcr.io/github/github-mcp-server"
          ],
          "env": {
            "GITHUB_PERSONAL_ACCESS_TOKEN": "ghp_your_token_here"
          }
        }
      }
    }
    ```

    Users must use this exact configuration - any deviation in command or args will be blocked. The `env` section can have different values.
  </Accordion>

  <Accordion title="Option 3: Flexible Regex Patterns" description="Use regex patterns to allow variations in user configurations while maintaining security controls.">
    **Admin Whitelist Configuration:**

    * **Server ID**: `python-mcp-server`
    * **Server Config (JSON)**:

    ```json  theme={null}
    {
      "command": "python3",
      "args": ["/.*\\.py", "--port", "[0-9]+"]
    }
    ```

    **Matching User Config (`mcp_config.json`):**

    ```json  theme={null}
    {
      "mcpServers": {
        "python-mcp-server": {
          "command": "python3",
          "args": ["/home/user/my_server.py", "--port", "8080"],
          "env": {
            "PYTHONPATH": "/home/user/mcp"
          }
        }
      }
    }
    ```

    This example allows users flexibility while maintaining security:

    * The regex `/.*\\.py` matches any Python file path like `/home/user/my_server.py`
    * The regex `[0-9]+` matches any numeric port like `8080` or `3000`
    * Users can customize file paths and ports while admins ensure only Python scripts are executed
  </Accordion>
</AccordionGroup>

### Common Regex Patterns

| Pattern         | Matches                   | Example                |
| --------------- | ------------------------- | ---------------------- |
| `.*`            | Any string                | `/home/user/script.py` |
| `[0-9]+`        | Any number                | `8080`, `3000`         |
| `[a-zA-Z0-9_]+` | Alphanumeric + underscore | `api_key_123`          |
| `\\$HOME`       | Literal `$HOME`           | `$HOME` (not expanded) |
| `\\.py`         | Literal `.py`             | `script.py`            |
| `\\[cli\\]`     | Literal `[cli]`           | `mcp[cli]`             |

## Notes

### Admin Configuration Guidelines

* **Environment Variables**: The `env` section is not regex-matched and can be configured freely by users
* **Disabled Tools**: The `disabledTools` array is handled separately and not part of whitelist matching
* **Case Sensitivity**: All matching is case-sensitive
* **Error Handling**: Invalid regex patterns will be logged and result in access denial
* **Testing**: Test your regex patterns carefully - overly restrictive patterns may block legitimate use cases

### Troubleshooting

If users report that their MCP servers aren't working after whitelisting:

1. **Check Exact Matching**: Ensure the whitelist pattern exactly matches the user's configuration
2. **Verify Regex Escaping**: Special characters may need escaping (e.g., `\.` for literal dots)
3. **Review Logs**: Invalid regex patterns are logged with warnings
4. **Test Patterns**: Use a regex tester to verify your patterns work as expected

Remember: Once you whitelist any server, **all other servers are automatically blocked** for your team members.

### General Information

* Since MCP tool calls can invoke code written by arbitrary server implementers, we do not assume liability
  for MCP tool call failures. To reiterate:
* We currently support an MCP server's [tools](https://modelcontextprotocol.io/docs/concepts/tools) and [resources](https://modelcontextprotocol.io/docs/concepts/resources), not [prompts](https://modelcontextprotocol.io/docs/concepts/prompts).



# Memories & Rules
Source: https://docs.windsurf.com/windsurf/cascade/memories



`Memories` is the system for sharing and persisting context across conversations.

There are two mechanisms for this in Windsurf: Memories, which can be automatically generated by Cascade, and rules, which are manually defined by the user at both the local and global levels.

## How to Manage Memories

Memories and Rules can be accessed and configured at any time by clicking on the `Customizations` icon in the top right slider menu in Cascade, or via “Windsurf - Settings” in the bottom-right hand corner. To edit an existing memory, simply click into it and then click the `Edit` button.

<video autoPlay controls muted loop playsInline className="aspect-video" src="https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/memories-rules.mp4?fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=2a80ad4bb69460c082c09f9633ab3649" data-path="assets/windsurf/cascade/memories-rules.mp4" />

## Memories

During conversation, Cascade can automatically generate and store memories if it encounters context that it believes is useful to remember.

Additionally, you can ask Cascade to create a memory at any time. Just prompt Cascade to "create a memory of ...".

Cascade's autogenerated memories are associated with the workspace that they were created in and Cascade will retrieve them when it believes that they are relevant. Memories generated in one workspace will not be available in another.

<Tip>Creating and using auto-generated memories do NOT consume credits</Tip>

## Rules

Users can explicitly define their own rules for Cascade to follow.

Rules can be defined at either the global level or the workspace level.

`global_rules.md` - rules applied across all workspaces

`.windsurf/rules` - workspace level directory containing rules that are tied to globs or natural language descriptions.

## Rules Discovery

Windsurf automatically discovers rules from multiple locations to provide flexible organization:

* **Current workspace and sub-directories**: All `.windsurf/rules` directories within your current workspace and its sub-directories
* **Git repository structure**: For git repositories, Windsurf also searches up to the git root directory to find rules in parent directories
* **Multiple workspace support**: When multiple folders are open in the same workspace, rules are deduplicated and displayed with the shortest relative path

### Rules Storage Locations

Rules can be stored in any of these locations:

* `.windsurf/rules` in your current workspace directory
* `.windsurf/rules` in any sub-directory of your workspace
* `.windsurf/rules` in parent directories up to the git root (for git repositories)

When you create a new rule, it will be saved in the `.windsurf/rules` directory of your current workspace, not necessarily at the git root.

To get started with Rules, click on the `Customizations` icon in the top right slider menu in Cascade, then navigate to the `Rules` panel. Here, you can click on the `+ Global` or `+ Workspace` button to create new rules at either the global or workspace level, respectively.

<Tip>You can find example rule templates curated by the Windsurf team at [https://windsurf.com/editor/directory](https://windsurf.com/editor/directory) to help you get started.</Tip>

Rules files are limited to 12000 characters each.

### Activation Modes

At the rule level, you can define how a rule should be activated for Cascade.

There are 4 modes:

1. **Manual**: This rule can be manually activated via `@mention` in Cascade's input box
2. **Always On**: This rule will always be applied
3. **Model Decision**: Based on a natural language description of the rule the user defines, the model decides whether to apply the rule.
4. **Glob**: Based on the glob pattern that the user defines (e.g. *.js, src/\*\*/*.ts), this rule will be applied to all files that match the pattern.

### Best Practices

To help Cascade follow your rules effectively, follow these best practices:

* Keep rules simple, concise, and specific. Rules that are too long or vague may confuse Cascade.
* There's no need to add generic rules (e.g. "write good code"), as these are already baked into Cascade's training data.
* Format your rules using bullet points, numbered lists, and markdown. These are easier for Cascade to follow compared to a long paragraph. For example:

```

# Coding Guidelines 
- My project's programming language is python
- Use early returns when possible
- Always add documentation when creating new functions and classes
```

* XML tags can be an effective way to communicate and group similar rules together. For example:

```
<coding_guidelines>
- My project's programming language is python
- Use early returns when possible
- Always add documentation when creating new functions and classes
</coding_guidelines>
```



# Web and Docs Search
Source: https://docs.windsurf.com/windsurf/cascade/web-search



Cascade can now intuitively parse through and chunk up web pages and documentation, providing realtime context to the models. The key way to understand this feature is that Cascade will browse the Internet as a human would.

Our web tools are designed in such a way that gets only the information that is necessary in order to efficiently use your credits.

## Overview

To help you better understand how Web Search works, we've recorded a short video covering the key concepts and best practices.

<iframe width="560" height="315" src="https://www.youtube.com/embed/moIySJ4d0UY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

### Quick Start

The fastest way to get started is to activate web search in your Windsurf Settings in the bottom right corner of the editor. You can activate it a couple of different ways:

1. Ask a question that probably needs the Internet (ie. "What's new in the latest version of React?").
2. Use `@web` to force a docs search.
3. Use `@docs` to query over a list of docs that we are confident we can read with high quality.
4. Paste a URL into your message.

## Search the web

Cascade can deduce that certain prompts from the user may require a real-time web search to provide the optimal response. In these cases, Cascade will perform a web search and provide the results to the user. This can happen automatically or manually using the `@web` mention.

<Frame style={{ border: "none", background: "none" }}>
  <img src="https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/cascade-search-web.png?fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=b525aef8bc3d129ee5a6d93d10c2cb06" data-og-width="1150" width="1150" data-og-height="530" height="530" data-path="assets/windsurf/cascade/cascade-search-web.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/cascade-search-web.png?w=280&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=e2eee016969bdcd5f0572659690c7df7 280w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/cascade-search-web.png?w=560&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=3b131c992adfe832ded1b8722cbb4e7f 560w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/cascade-search-web.png?w=840&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=2cdac74f260dedf5da5bf42abe82869d 840w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/cascade-search-web.png?w=1100&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=27abbec8f15aeec6e0319093cbf4d049 1100w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/cascade-search-web.png?w=1650&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=e96bf16e2f5a79fce342efbbf2bed8fb 1650w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/cascade-search-web.png?w=2500&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=f95fde4ebf0cac5e0dfb792ae238d071 2500w" />
</Frame>

## Reading Pages

Cascade can read individual pages for things like documentation, blog posts, and GitHub files. The page reads happen entirely on your device within your network so if you're using a VPN you shouldn't have any problems.

Pages are picked up either from web search results, inferred based on the conversation, or from URLs pasted directly into your message.

We break pages up into multiple chunks, very similar to how a human would read a page: for a long page we skim to the section we want then read the text that's relevant. This is how Cascade operates as well.

<Frame style={{ border: "none", background: "none" }}>
  <img src="https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/cascade-parse-url.png?fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=9963f9eadcca6c5e8152cae398999e00" data-og-width="1158" width="1158" data-og-height="538" height="538" data-path="assets/windsurf/cascade/cascade-parse-url.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/cascade-parse-url.png?w=280&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=4b943dbae4a899d98f8d1e30588634a2 280w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/cascade-parse-url.png?w=560&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=1f549cf84cb41fb9b853d87d9972e069 560w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/cascade-parse-url.png?w=840&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=a79f381fe2fae01f383bf4836f734055 840w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/cascade-parse-url.png?w=1100&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=a67a8ec724d365f27c18e4a6f6d25f08 1100w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/cascade-parse-url.png?w=1650&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=c791fad06d7c86395d52d4792f321eb5 1650w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/cascade-parse-url.png?w=2500&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=e04bbf62bc9adbbd5c40d2d1e27d9bcf 2500w" />
</Frame>

It's worth noting that not all pages can be parsed. We are actively working on improving the quality of our website reading. If you have specific sites you'd like us to handle better, feel free to file a feature request!



# Workflows
Source: https://docs.windsurf.com/windsurf/cascade/workflows



Workflows enable users to define a series of steps to guide Cascade through a repetitive set of tasks, such as deploying a service or responding to PR comments.

These Workflows are saved as markdown files, allowing users and their teams an easy repeatable way to run key processes.

Once saved, Workflows can be invoked in Cascade via a slash command with the format of `/[name-of-workflow]`

## How it works

Rules generally provide large language models with guidance by providing persistent, reusable context at the prompt level.

Workflows extend this concept by providing a structured sequence of steps or prompts at the trajectory level, guiding the model through a series of interconnected tasks or actions.

<Frame>
  <img style={{ maxHeight: "400px" }} src="https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/use-workflow-pr.png?fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=753d27e7c9e49d1feca84a2b8272f8e6" data-og-width="718" width="718" data-og-height="510" height="510" data-path="assets/windsurf/cascade/use-workflow-pr.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/use-workflow-pr.png?w=280&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=b8f833514a2b7a1bad49bfaf84e47f8a 280w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/use-workflow-pr.png?w=560&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=400b2a092b1e34276e0281085a106e1c 560w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/use-workflow-pr.png?w=840&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=9d2098efff896dea137777fb7876f23b 840w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/use-workflow-pr.png?w=1100&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=582ff2b958ad653f19c8c31d7ed2af58 1100w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/use-workflow-pr.png?w=1650&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=ecbde9bac2a87f74beba39b1542f079e 1650w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/use-workflow-pr.png?w=2500&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=0b22373ae141547fbe493d1314acfcfa 2500w" />
</Frame>

To execute a Workflow, users simply invoke it in Cascade using the `/[workflow-name]` command.

<Tip>You can call other Workflows from within a Workflow! <br /><br />For example, /workflow-1 can include instructions like "Call /workflow-2" and "Call /workflow-3".</Tip>

Upon invocation, Cascade sequentially processes each step defined in the Workflow, performing actions or generating responses as specified.

## How to create a Workflow

To get started with Workflows, click on the `Customizations` icon in the top right slider menu in Cascade, then navigate to the `Workflows` panel. Here, you can click on the `+ Workflow` button to create a new Workflow.

Workflows are saved as markdown files within `.windsurf/workflows/` directories and contain a title, description, and a series of steps with specific instructions for Cascade to follow.

## Workflow Discovery

Windsurf automatically discovers workflows from multiple locations to provide flexible organization:

* **Current workspace and sub-directories**: All `.windsurf/workflows/` directories within your current workspace and its sub-directories
* **Git repository structure**: For git repositories, Windsurf also searches up to the git root directory to find workflows in parent directories
* **Multiple workspace support**: When multiple folders are open in the same workspace, workflows are deduplicated and displayed with the shortest relative path

### Workflow Storage Locations

Workflows can be stored in any of these locations:

* `.windsurf/workflows/` in your current workspace directory
* `.windsurf/workflows/` in any sub-directory of your workspace
* `.windsurf/workflows/` in parent directories up to the git root (for git repositories)

When you create a new workflow, it will be saved in the `.windsurf/workflows/` directory of your current workspace, not necessarily at the git root.

Workflow files are limited to 12000 characters each.

<video autoPlay controls muted loop playsInline className="w-full aspect-video" src="https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/create-workflow.mp4?fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=d79db41f1ecd46f1fcdf07476bf2aaf1" data-path="assets/windsurf/cascade/create-workflow.mp4" />

### Generate a Workflow with Cascade

You can also ask Cascade to generate Workflows for you! This works particularly well for Workflows involving a series of steps in a particular CLI tool.

<video autoPlay controls muted loop playsInline className="w-full aspect-video" src="https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/create-workflow-with-cascade.mp4?fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=f4d4dc32f319a356a776e03d355907a5" data-path="assets/windsurf/cascade/create-workflow-with-cascade.mp4" />

## Example Workflows

There are a myriad of use cases for Workflows, such as:

<Card title="/address-pr-comments">
  This is a Workflow our team uses internally to address PR comments:

  ```
  1. Check out the PR branch: `gh pr checkout [id]`

  2. Get comments on PR

   bash
   gh api --paginate repos/[owner]/[repo]/pulls/[id]/comments | jq '.[] | {user: .user.login, body, path, line, original_line, created_at, in_reply_to_id, pull_request_review_id, commit_id}'

  3. For EACH comment, do the following. Remember to address one comment at a time.
   a. Print out the following: "(index). From [user] on [file]:[lines] — [body]"
   b. Analyze the file and the line range.
   c. If you don't understand the comment, do not make a change. Just ask me for clarification, or to implement it myself.
   d. If you think you can make the change, make the change BEFORE moving onto the next comment.

  4. After all comments are processed, summarize what you did, and which comments need the USER's attention.
  ```
</Card>

<Card title="/git-workflows">
  Commit using predefined formats and create a pull requests with standardized title and descriptions using the appropriate CLI commands.
</Card>

<Card title="/dependency-management">
  Automate the installation or updating of project dependencies based on a configuration file (e.g., requirements.txt, package.json).
</Card>

<Card title="/code-formatting">
  Automatically run code formatters (like Prettier, Black) and linters (like ESLint, Flake8) on file save or before committing to maintain code style and catch errors early.
</Card>

<Card title="/run-tests-and-fix">
  Run or add unit or end-to-end tests and fix the errors automatically to ensure code quality before committing, merging, or deploying.
</Card>

<Card title="/deployment">
  Automate the steps to deploy your application to various environments (development, staging, production), including any necessary pre-deployment checks or post-deployment verifications.
</Card>

<Card title="/security-scan">
  Integrate and trigger security vulnerability scans on your codebase as part of the CI/CD pipeline or on demand.
</Card>



# Codemaps (Beta)
Source: https://docs.windsurf.com/windsurf/codemaps

Hierarchical maps for codebase understanding.

Powered by a specialized agent, Codemaps are shareable artifacts that bridge the gap between human comprehension and AI reasoning, making it possible to navigate, discuss, and modify large codebases with precision and context.

<Note>
  Codemaps is currently in Beta and subject to change in future releases.
</Note>

## What are Codemaps?

While [DeepWiki](/windsurf/deepwiki) provides symbol-level documentation, Codemaps help with codebase understanding by mapping how everything works together—showing the order in which code and files are executed and how different components relate to each other.

To navigate a Codemap, click on any node to instantly jump to that file and function. Each node in the Codemap links directly to the corresponding location in your code.

<video autoPlay controls muted loop playsInline className="w-full aspect-video" src="https://mintcdn.com/codeium/K1c0U9TfuKxwshS5/assets/windsurf/codemaps/codemaps-overview.mp4?fit=max&auto=format&n=K1c0U9TfuKxwshS5&q=85&s=e8b8990690ec210cced0f78ba1969fac" data-path="assets/windsurf/codemaps/codemaps-overview.mp4" />

## Accessing Codemaps

You can access Codemaps in one of two ways:

* **Activity Bar**: Find the Codemaps interface in the Activity Bar (left side panel)
* **Command Palette**: Press `Cmd+Shift+P` (Mac) or `Ctrl+Shift+P` (Windows/Linux) and search for "Focus on Codemaps View"

## Creating a Codemap

To create a new Codemap:

1. Open the Codemaps panel
2. Create a new Codemap by:
   * Selecting a suggested topic (suggestions are based on your recent navigation history)
   * Typing your own custom prompt
   * Generating from Cascade: Create new Codemaps from the bottom of a Cascade conversation
3. The Codemap agent explores your repository, identify relevant files and functions, and generate a hierarchical view

<video autoPlay controls muted loop playsInline className="w-full aspect-video" src="https://mintcdn.com/codeium/K1c0U9TfuKxwshS5/assets/windsurf/codemaps/create-codemaps.mp4?fit=max&auto=format&n=K1c0U9TfuKxwshS5&q=85&s=ea5da928e3e72962b2bb5f2b75b659c6" data-path="assets/windsurf/codemaps/create-codemaps.mp4" />

## Sharing Codemaps

You can share Codemaps with teammates as links that can be viewed in a browser.

<Warning>
  For enterprise customers, sharing Codemaps requires opt-in because they need to be stored on our servers. By default, Codemaps are only available within your Team and require authentication to view.
</Warning>

<video autoPlay controls muted loop playsInline className="w-full aspect-video" src="https://mintcdn.com/codeium/K1c0U9TfuKxwshS5/assets/windsurf/codemaps/share-codemaps.mp4?fit=max&auto=format&n=K1c0U9TfuKxwshS5&q=85&s=ca21fbc4275a16bef9c59026ac3b4f63" data-path="assets/windsurf/codemaps/share-codemaps.mp4" />

## Using Codemaps with Cascade

You can include Codemap information as context in your [Cascade](/windsurf/cascade) conversations by using `@-mention` to reference a Codemap.

<video autoPlay controls muted loop playsInline className="w-full aspect-video" src="https://mintcdn.com/codeium/K1c0U9TfuKxwshS5/assets/windsurf/codemaps/codemap-cascade.mp4?fit=max&auto=format&n=K1c0U9TfuKxwshS5&q=85&s=500ca2181f5ec83c309a3994e70499dc" data-path="assets/windsurf/codemaps/codemap-cascade.mp4" />



# C#, .NET, and CPP
Source: https://docs.windsurf.com/windsurf/csharp-cpp

C# / C++ Development Setup for Windsurf


# Windsurf Development Environment Setup Guide

## Overview

Windsurf workspaces rely **exclusively on open‑source tooling** for compiling, linting, and debugging. Microsoft's proprietary Visual Studio components cannot be redistributed, so we integrate community‑maintained language servers, debuggers, and compilers instead.

This guide covers two stacks:

1. **.NET / C#** – targeting both .NET Core and .NET Framework (via Mono)
2. **C / C++** – using clang‑based tooling

You can install either or both in the same workspace.

> ⚠️ **Important**: The examples below are templates that you must customize for your specific project. You'll need to edit file paths, project names, and build commands to match your codebase.

***

## 1. .NET / C# development

> **Choose the flavour that matches your codebase.**

### .NET Core / .NET 6+

**Extensions:**

* **[C#](https://marketplace.windsurf.com/vscode/item?itemName=muhammad-sammy.csharp)** (`muhammad-sammy.csharp`) – bundles **OmniSharp LS** and **NetCoreDbg**, so you can hit <kbd>F5</kbd> immediately

* **[.NET Install Tool](https://marketplace.windsurf.com/vscode/item?itemName=ms-dotnettools.vscode-dotnet-runtime)** (`ms-dotnettools.vscode-dotnet-runtime`) – auto‑installs missing runtimes/SDKs

* **[Solution Explorer](https://marketplace.windsurf.com/vscode/item?itemName=fernandoescolar.vscode-solution-explorer)** (`fernandoescolar.vscode-solution-explorer`) – navigate and manage .NET solutions and projects

**Debugger:** Nothing else is required—the extension already contains the language server and an open‑source debugger suitable for .NET Core.

**Build:** `dotnet build`

### .NET Framework via Mono

**Extensions:**

* **[Mono Debug](https://marketplace.windsurf.com/vscode/item?itemName=chrisatwindsurf.mono-debug)** (`chrisatwindsurf.mono-debug`) – debug adapter for Mono ([Open VSX](https://open-vsx.org/extension/chrisatwindsurf/mono-debug))
* **[C#](https://marketplace.windsurf.com/vscode/item?itemName=muhammad-sammy.csharp)** (`muhammad-sammy.csharp`) for language features

**Debugger:** **You must also install the Mono tool‑chain inside the workspace.** Follow the install guide in the [Mono repo](https://gitlab.winehq.org/mono/mono#compilation-and-installation). The debugger extension connects to that runtime at debug time.

> **⚠️ .NET Framework Configuration**: After installing Mono, to use the C# extension with .NET Framework projects, you need to toggle a specific setting in the IDE Settings. Go to **Settings** (in the C# Extension section) and toggle off  **"Omnisharp: Use Modern Net"**. This setting uses the OmniSharp build for .NET 6, which provides significant performance improvements for SDK-style Framework, .NET Core, and .NET 5+ projects. Note that this version *does not* support non-SDK-style .NET Framework projects, including Unity.

**Build:** `mcs Program.cs`

### Configure `tasks.json` for Your Project

**You must create/edit `.vscode/tasks.json` in your workspace root** and customize these templates:

```jsonc  theme={null}
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "build-dotnet",
      "type": "shell",
      "command": "dotnet",
      "args": ["build", "YourProject.csproj"], // ← Edit this
      "group": "build",
      "problemMatcher": "$msCompile"
    },
    {
      "label": "build-mono",
      "type": "shell",
      "command": "mcs",
      "args": ["YourProgram.cs"], // ← Edit this
      "group": "build"
    }
  ]
}
```

### Configure `launch.json` for Debugging

**You must create/edit `.vscode/launch.json` in your workspace root** and update the paths:

```jsonc  theme={null}
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": ".NET Core Launch",
      "type": "coreclr",
      "request": "launch",
      "preLaunchTask": "build-dotnet",
      "program": "${workspaceFolder}/bin/Debug/net6.0/YourApp.dll", // ← Edit this path
      "cwd": "${workspaceFolder}",
      "args": [] // Add command line arguments if needed
    },
    {
      "name": "Mono Launch",
      "type": "mono",
      "request": "launch",
      "preLaunchTask": "build-mono",
      "program": "${workspaceFolder}/YourProgram.exe", // ← Edit this path
      "cwd": "${workspaceFolder}"
    }
  ]
}
```

### CLI equivalents

```bash  theme={null}

# .NET Core
$ dotnet build
$ dotnet run


# Mono / .NET Framework
$ mcs Program.cs
$ mono Program.exe
```

### .NET Framework Limitations

⚠️ **Important**: .NET Framework codebases with mixed assemblies (C++/CLI) or complex Visual Studio dependencies have significant limitations in Windsurf. These codebases typically require Visual Studio's proprietary build system and cannot be fully compiled or debugged in Windsurf due to dependencies on Microsoft-specific tooling and assembly reference resolution.

**Recommended approaches for .NET Framework projects:**

* Use Windsurf alongside Visual Studio for code generation and editing
* Migrate compatible portions to .NET Core where possible

***

## 2. C / C++ development

**Required Extensions:**

| Extension                                                                                                        | Purpose                                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **[Windsurf C++ Tools](https://open-vsx.org/extension/Codeium/windsurf-cpptools)** (`Codeium.windsurf-cpptools`) | This is a bundle of the three extensions we recommend using to get started. Package that contains C/C++ LSP support, debugging support, and CMake support. |

> **Note:** Installing the Windsurf C++ Tools bundle will automatically install the individual extensions listed below, so you only need to install the bundle.

| Extension                                                                                                                                           | Purpose                                                                                                                        |
| --------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| **[clangd](https://marketplace.windsurf.com/vscode/item?itemName=llvm-vs-code-extensions.vscode-clangd)** (`llvm-vs-code-extensions.vscode-clangd`) | **clangd** language‑server integration. If `clangd` is missing it will offer to download the correct binary for your platform. |
| **[CodeLLDB](https://marketplace.windsurf.com/extension/vadimcn/vscode-lldb)** (`vadimcn.vscode-lldb`)                                              | Native debugger based on LLDB for C/C++ and Rust code.                                                                         |
| **[CMake Tools](https://marketplace.windsurf.com/vscode/item?itemName=ms-vscode.cmake-tools)** (`ms-vscode.cmake-tools`)                            | Project configuration, build, test, and debug integration for **CMake**‑based projects.                                        |

For non‑CMake workflows you can still invoke `make`, `ninja`, etc. via custom `tasks.json` targets.

### Configure C/C++ Build Tasks

**Create/edit `.vscode/tasks.json`** for your C/C++ project:

```jsonc  theme={null}
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "build-cpp",
      "type": "shell",
      "command": "clang++",
      "args": ["-g", "main.cpp", "-o", "main"], // ← Edit for your files
      "group": "build",
      "problemMatcher": "$gcc"
    }
  ]
}
```

***

## 3. Notes & Gotchas

* **Open‑source only** – decline any prompt to install proprietary Microsoft tooling; Windsurf containers cannot ship it.
* **Container vs Host** – SDKs/compilers must be present **inside** the Windsurf workspace container.
* **Keyboard shortcuts**
  * <kbd>Ctrl/⌘ + Shift + B</kbd> → compile using the active build task
  * <kbd>F5</kbd> → debug using the selected `launch.json` config

***

## 4. Setup Checklist

* Install the required extensions for your language stack
* **Create and customize** `.vscode/tasks.json` with your project's build commands
* **Create and customize** `.vscode/launch.json` with correct paths to your executables
* For Mono: install the runtime and verify `mono --version`
* Update file paths, project names, and build arguments to match your codebase
* Test your setup: Press <kbd>Ctrl/⌘ + Shift + B</kbd> to build, then <kbd>F5</kbd> to debug

> 💡 **Tip**: The configuration files are project-specific. You'll need to adapt the examples above for each workspace.



# DeepWiki
Source: https://docs.windsurf.com/windsurf/deepwiki



We've implemented [Devin's DeepWiki feature](https://docs.devin.ai/work-with-devin/deepwiki) inside of the Windsurf Editor. Use it to get up to speed on unfamiliar parts of your codebase.

You can find the DeepWiki interface in the Primary Side Bar / Activity Bar.

<video autoPlay controls muted loop playsInline className="w-full aspect-video" src="https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/deepwiki-demo.mp4?fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=3b9abf7eda8d39b6a9ae8c064fe876c5" data-path="assets/windsurf/deepwiki-demo.mp4" />

To use DeepWiki, hover over a symbol in your codebase and press `Cmd+Shift+Click` to open detailed explanations of code symbols.

Unlike classical hover cards that just show basic type information, DeepWiki-powered hover explains functions, variables, and classes as you read through code.

You can send the DeepWiki explanation to Cascade as an `@-mention` by clicking the `⋮` button in the top right of the DeepWiki panel and selecting `Add to Cascade`.

<img style={{ display: "block", margin: "auto" }} src="https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/deepwiki-example.jpg?fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=9db91d022ef27a79e0ba6fda0d2c40d2" data-og-width="2050" width="2050" data-og-height="2448" height="2448" data-path="assets/windsurf/deepwiki-example.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/deepwiki-example.jpg?w=280&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=3ea454d7da800bb3633c84cbe9af6c89 280w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/deepwiki-example.jpg?w=560&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=340e0cdaa399de417a3d6839da0744d8 560w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/deepwiki-example.jpg?w=840&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=0e4f40f8b8701a456bd36f406595f2b4 840w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/deepwiki-example.jpg?w=1100&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=d6ef8f220509e93dc3fb6a38ad93bde3 1100w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/deepwiki-example.jpg?w=1650&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=5f721f23b3adb4595b555cb2402cca26 1650w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/deepwiki-example.jpg?w=2500&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=151a4d17b15b5c27d77180dbdd60e545 2500w" />



# Welcome to Windsurf
Source: https://docs.windsurf.com/windsurf/getting-started



Tomorrow's editor, today.

Windsurf is a next-generation AI IDE built to keep you in the flow. On this page, you'll find instructions on how to install Windsurf on your computer, navigate the onboarding flow, and get started with your first AI-powered project.

<Card
  title="Cascade"
  icon={
    <svg
      width="25"
      height="25"
      viewBox="0 0 1292 1292"
      fill="none"
      xmlns="http://www.w3.org/2000/svg"
    >
      <path
        d="M1195 599C1195 848.08 993.08 1050 744 1050C494.92 1050 293 848.08 293 599C293 349.92 494.92 148 744 148C993.08 148 1195 349.92 1195 599ZM411.5 599C411.5 782.635 560.365 931.5 744 931.5C927.635 931.5 1076.5 782.635 1076.5 599C1076.5 415.365 927.635 266.5 744 266.5C560.365 266.5 411.5 415.365 411.5 599Z"
        fill="#34E8BB"
      />
      <path
        d="M1096.19 1053.62C1116.8 1078.03 1113.86 1114.77 1087.65 1133.04C1002.41 1192.46 903.441 1229.92 799.584 1241.61C676.505 1255.46 552.082 1232.51 442.049 1175.65C332.016 1118.79 241.314 1030.58 181.415 922.172C130.87 830.693 104.172 728.301 103.33 624.396C103.071 592.449 131.338 568.79 163.173 571.479C195.007 574.168 218.29 602.208 219.218 634.143C221.573 715.175 243.206 794.78 282.679 866.22C331.512 954.6 405.457 1026.51 495.161 1072.87C584.866 1119.22 686.302 1137.94 786.643 1126.64C867.75 1117.51 945.198 1089.11 1012.66 1044.15C1039.24 1026.44 1075.58 1029.21 1096.19 1053.62Z"
        fill="#34E8BB"
      />
      <path
        d="M177.334 450.08C146.261 442.514 126.947 411.072 137.349 380.829C160.687 312.983 195.56 249.512 240.566 193.267C285.571 137.023 339.851 89.0802 400.928 51.4326C428.153 34.6511 463.065 46.5999 477.261 75.2582C491.457 103.917 479.508 138.389 452.641 155.738C406.542 185.506 365.436 222.584 330.994 265.627C296.552 308.67 269.39 356.906 250.456 408.411C239.421 438.428 208.408 457.646 177.334 450.08Z"
        fill="#34E8BB"
      />
    </svg>
  }
  href="/windsurf/cascade"
>
  Your agentic chatbot that can collaborate with you like never before.
</Card>

<CardGroup cols={2}>
  <Card title="Usage" icon="bars-progress" href="/windsurf/accounts/usage">
    Credits and usage.
  </Card>

  <Card title="Terminal" icon="terminal" href="/windsurf/terminal">
    An upgraded Terminal experience.
  </Card>
</CardGroup>

<CardGroup cols={2}>
  <Card title="MCP" icon="hammer" href="/windsurf/cascade/mcp">
    MCP servers extend the agent's capabilities.
  </Card>

  <Card title="Memories" icon="cloud-word" href="/windsurf/cascade/memories">
    Memories and rules help customize behavior.
  </Card>

  <Card title="Context Awareness" icon="brain" href="/context-awareness/overview">
    Instantly understands your codebase.
  </Card>

  <Card title="Advanced" icon="gears" href="/windsurf/advanced">
    Advanced configuration options.
  </Card>
</CardGroup>

<CardGroup cols={2}>
  <Card title="Workflows" icon="list" href="/windsurf/cascade/workflows">
    Automate repetitive trajectories.
  </Card>

  <Card title="App Deploys" icon="rocket" href="/windsurf/cascade/app-deploys">
    Deploy applications in one click.
  </Card>
</CardGroup>

<Tip> See what's new with Windsurf in our [changelog](https://windsurf.com/changelog)! </Tip>

## Set Up

To get started, please ensure that your device meets the requirements, click the download link, and follow the instructions to install and run Windsurf.

[Click here](#update-windsurf) if you're looking for how to update Windsurf.

<Tabs>
  <Tab title="Mac">
    Minimum OS Version: OS X Yosemite

    <a href="https://windsurf.com/windsurf/download_mac" target="_blank" rel="noopener noreferrer">
      <button style={{width: '170px', backgroundColor: '#34E8BB', color: 'white', padding: '5px 10px', border: 'none', borderRadius: '5px', cursor: 'pointer', fontSize: '0.8rem', display: 'flex', justifyContent: 'center'}}>Download for Mac</button>
    </a>
  </Tab>

  <Tab title="Windows">
    Minimum OS Version: Windows 10

    <a href="https://windsurf.com/windsurf/download" target="_blank" rel="noopener noreferrer">
      <button style={{width: '170px', backgroundColor: '#34E8BB', color: 'white', padding: '5px 10px', border: 'none', borderRadius: '5px', cursor: 'pointer', fontSize: '0.8rem', display: 'flex', justifyContent: 'center'}}>Download for Windows</button>
    </a>
  </Tab>

  <Tab title="Ubuntu">
    Minimum OS Version: >= 20.04 (or glibc >= 2.31, glibcxx >= 3.4.26)

    <a href="https://windsurf.com/windsurf/download_linux" target="_blank" rel="noopener noreferrer">
      <button style={{width: '170px', backgroundColor: '#34E8BB', color: 'white', padding: '5px 10px', border: 'none', borderRadius: '5px', cursor: 'pointer', fontSize: '0.8rem', display: 'flex', justifyContent: 'center'}}>Download for Ubuntu</button>
    </a>
  </Tab>

  <Tab title="Other Linux distributions">
    Minimum OS Version: glibc >= 2.28, glibcxx >= 3.4.25

    <a href="https://windsurf.com/windsurf/download_linux" target="_blank" rel="noopener noreferrer">
      <button style={{width: '170px', backgroundColor: '#34E8BB', color: 'white', padding: '5px 10px', border: 'none', borderRadius: '5px', cursor: 'pointer', fontSize: '0.8rem', display: 'flex', justifyContent: 'center'}}>Download for Linux</button>
    </a>
  </Tab>
</Tabs>

## Onboarding

Once you have Windsurf running, you will see the page below. Let's get started! Note that you can always restart this onboarding flow with the "Reset Onboarding" command.

<Frame>
  <img src="https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/onboarding/welcome.png?fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=f8eae97bf290f1badc7b21e0d9566f89" data-og-width="2344" width="2344" data-og-height="1464" height="1464" data-path="assets/windsurf/onboarding/welcome.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/onboarding/welcome.png?w=280&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=005fb62783dbc69d26ba4a385f631af4 280w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/onboarding/welcome.png?w=560&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=14329b88b359c30fbdeeafaf1441d658 560w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/onboarding/welcome.png?w=840&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=18079c6db1af8451a06e2fa912375593 840w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/onboarding/welcome.png?w=1100&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=5cbf9997ee5be2bb64bdd84526149cb6 1100w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/onboarding/welcome.png?w=1650&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=ab65ebee097953eceab05b38a43e5ad1 1650w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/onboarding/welcome.png?w=2500&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=02cbfbdcbf741d50ecda7fc91a62fa61 2500w" />
</Frame>

### 1. Select setup flow

If you're coming from VS Code or Cursor, you can easily import your configurations. Otherwise, select "Start fresh". You can also optionally install `windsurf` in PATH such that you can run `windsurf` from your command line.

<Frame>
  <img src="https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/onboarding/setup.png?fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=5696da6d3a63cd10ddcac4575dbf89fd" data-og-width="2064" width="2064" data-og-height="1145" height="1145" data-path="assets/windsurf/onboarding/setup.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/onboarding/setup.png?w=280&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=18b359f2e6bc1d0f47178756d66c2bed 280w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/onboarding/setup.png?w=560&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=ea2bf29ede4c4a0e5d8fdb070378b4ac 560w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/onboarding/setup.png?w=840&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=9455bc3d88661425c53ed8161ec8b414 840w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/onboarding/setup.png?w=1100&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=2548c1e288bb60ebf1d0edd0f340dbea 1100w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/onboarding/setup.png?w=1650&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=056c36416dd07b786b4ed53fe7a564d3 1650w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/onboarding/setup.png?w=2500&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=092178864dd7fe1c03b2976496e73e38 2500w" />
</Frame>

<Tabs>
  <Tab title="Start fresh">
    Choose your keybindings here, either default VS Code bindings or Vim bindings.

    <Frame>
      <img src="https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/onboarding/keybind.png?fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=14c9adde7dd5bb1073108c510934f3cb" data-og-width="2484" width="2484" data-og-height="1378" height="1378" data-path="assets/windsurf/onboarding/keybind.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/onboarding/keybind.png?w=280&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=50cd06dba4b9b5bc24ae5a0a8ffaa13c 280w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/onboarding/keybind.png?w=560&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=c80c971c5a6be4742a8cec4ae39a3154 560w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/onboarding/keybind.png?w=840&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=2a71d5cd42fa0ae851e30e510e080add 840w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/onboarding/keybind.png?w=1100&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=a8f9325c773c67a7eb6c46f707cc9d1d 1100w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/onboarding/keybind.png?w=1650&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=271228fc3ec4a31aae38c987c563a2e4 1650w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/onboarding/keybind.png?w=2500&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=8a80c36c3544513a10a7246e7ee163ca 2500w" />
    </Frame>
  </Tab>

  <Tab title="Import from VS Code">
    You can migrate your settings, extensions, or both here.

    <Frame>
      <img src="https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/onboarding/vscode_migration.png?fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=cf14f085ccba168dd02c791f381507b7" data-og-width="2486" width="2486" data-og-height="1378" height="1378" data-path="assets/windsurf/onboarding/vscode_migration.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/onboarding/vscode_migration.png?w=280&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=be0a7d7e959c7d4f17dd9bbab09d93da 280w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/onboarding/vscode_migration.png?w=560&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=db53903b9b8dd576e1518817595fbf95 560w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/onboarding/vscode_migration.png?w=840&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=b8746c6a2666cd70ec6c50243d6ca688 840w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/onboarding/vscode_migration.png?w=1100&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=df6a9a5097deea2b557cb33faf652b2d 1100w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/onboarding/vscode_migration.png?w=1650&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=e04a2d1f08d35cc5fca41de9b1526c2c 1650w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/onboarding/vscode_migration.png?w=2500&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=b61712da092e6f78cdf55bb26eafec19 2500w" />
    </Frame>
  </Tab>

  <Tab title="Import from Cursor">
    You can migrate your settings, extensions, or both here.

    <Frame>
      <img src="https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/onboarding/vscode_migration.png?fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=cf14f085ccba168dd02c791f381507b7" data-og-width="2486" width="2486" data-og-height="1378" height="1378" data-path="assets/windsurf/onboarding/vscode_migration.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/onboarding/vscode_migration.png?w=280&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=be0a7d7e959c7d4f17dd9bbab09d93da 280w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/onboarding/vscode_migration.png?w=560&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=db53903b9b8dd576e1518817595fbf95 560w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/onboarding/vscode_migration.png?w=840&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=b8746c6a2666cd70ec6c50243d6ca688 840w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/onboarding/vscode_migration.png?w=1100&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=df6a9a5097deea2b557cb33faf652b2d 1100w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/onboarding/vscode_migration.png?w=1650&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=e04a2d1f08d35cc5fca41de9b1526c2c 1650w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/onboarding/vscode_migration.png?w=2500&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=b61712da092e6f78cdf55bb26eafec19 2500w" />
    </Frame>
  </Tab>
</Tabs>

### 2. Choose editor theme

Choose your favorite color theme from these defaults! Don't worry, you can always change this later. Note that if you imported from VS Code, your imported theme will override this.

<Frame>
  <img src="https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/onboarding/theme.png?fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=7bd1ce64f97063988605a7e6bcf3f734" data-og-width="2482" width="2482" data-og-height="1380" height="1380" data-path="assets/windsurf/onboarding/theme.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/onboarding/theme.png?w=280&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=6e36c2c32b1e83a9fd15df667da59dc7 280w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/onboarding/theme.png?w=560&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=11966f5933b6c2e9ada918ce1d7c0d0b 560w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/onboarding/theme.png?w=840&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=9476b0a4d2ce83ebbf4cf152dda5ccf4 840w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/onboarding/theme.png?w=1100&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=2b1f53bdae2e265546a75ba30296fbd6 1100w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/onboarding/theme.png?w=1650&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=6288fdd29e53109b342ad3ae0d1e76d9 1650w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/onboarding/theme.png?w=2500&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=5e54ab80cbec8a5b1566e2b0d1eb7338 2500w" />
</Frame>

### 3. Sign up / Log in

To use Windsurf, you need to use your Windsurf account or create one if you don't have one. Signing up is completely free!

<Frame>
  <img src="https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/onboarding/auth.png?fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=e92373636e9415e67b79e5eaeff399be" data-og-width="2346" width="2346" data-og-height="1468" height="1468" data-path="assets/windsurf/onboarding/auth.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/onboarding/auth.png?w=280&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=294b45fb8e516d4167a25fc961f1492f 280w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/onboarding/auth.png?w=560&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=4dc80b61233742fa5f82cd356d9797a6 560w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/onboarding/auth.png?w=840&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=211852dc25f36bee964445d153bec911 840w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/onboarding/auth.png?w=1100&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=0937518814e0b4d554f456a4443157c1 1100w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/onboarding/auth.png?w=1650&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=e71da6a9b23a1ca36a7ef16ca3dcff2c 1650w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/onboarding/auth.png?w=2500&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=f7e672f5485b2576a9bd786bbc5c2a3b 2500w" />
</Frame>

Once you've authenticated correctly, you should see this page. Hit "Open Windsurf" and you're good to go!

<Frame>
  <img src="https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/onboarding/authenticated.png?fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=8d8091bca31c571afe1ef5caf9b03459" data-og-width="2348" width="2348" data-og-height="1464" height="1464" data-path="assets/windsurf/onboarding/authenticated.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/onboarding/authenticated.png?w=280&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=c163b16fd147765d61509069f3c57a5c 280w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/onboarding/authenticated.png?w=560&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=1e536ad5a679300854270bd6afb5872d 560w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/onboarding/authenticated.png?w=840&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=88848a858d8d595f133b7d9717c7ec42 840w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/onboarding/authenticated.png?w=1100&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=29794c0b2973bc7fa3d83d8cad5a97d6 1100w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/onboarding/authenticated.png?w=1650&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=c682364c3ea41ca340b08e7223634a08 1650w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/onboarding/authenticated.png?w=2500&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=f4d1fab9349270cf1e45cdce9b96ccf2 2500w" />
</Frame>

#### Having Trouble?

If you're having trouble with this authentication flow, you can also log in and manually provide Windsurf with an authentication code.

<Tabs>
  <Tab title="1. Select &#x22;Having Trouble?&#x22;">
    Click the "Copy link" button to copy an authentication link to your clipboard and enter this link into your browser.

    <Frame>
      <img src="https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/onboarding/manual_auth.png?fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=c4aabe6e213b964e315fbc6940f0c5b0" data-og-width="2478" width="2478" data-og-height="1376" height="1376" data-path="assets/windsurf/onboarding/manual_auth.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/onboarding/manual_auth.png?w=280&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=80e0ce95eae787bde316beece809171f 280w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/onboarding/manual_auth.png?w=560&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=3e12bcc62cd40a901231ed0df13ec807 560w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/onboarding/manual_auth.png?w=840&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=d8e3243f8e810544e8760b4955473116 840w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/onboarding/manual_auth.png?w=1100&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=22c9e1ef6b6e44ee96f5d25ce800fd7c 1100w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/onboarding/manual_auth.png?w=1650&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=7eb3acc5725041e61faff7e38987b1bd 1650w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/onboarding/manual_auth.png?w=2500&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=e448bba3a8db9737afc21bc0beeab2fb 2500w" />
    </Frame>
  </Tab>

  <Tab title="2. Enter Authentication Code">
    Copy the authentication code displayed in the link and enter it into Windsurf.

    <Frame>
      <img src="https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/onboarding/manual_auth_onboarding.png?fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=5911333c632d5ded717d685c3ff77cac" data-og-width="1990" width="1990" data-og-height="1858" height="1858" data-path="assets/windsurf/onboarding/manual_auth_onboarding.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/onboarding/manual_auth_onboarding.png?w=280&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=43fea2449ae6e1bacb4963ca8ca1032f 280w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/onboarding/manual_auth_onboarding.png?w=560&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=3dc7aa7a77ec0445ff7f703c52fa2a07 560w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/onboarding/manual_auth_onboarding.png?w=840&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=b4954c56ee344993063a57d90ab7520f 840w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/onboarding/manual_auth_onboarding.png?w=1100&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=56d65f38851aa93dc92a050701124564 1100w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/onboarding/manual_auth_onboarding.png?w=1650&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=163193b36e3392e875056ea419964c7e 1650w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/onboarding/manual_auth_onboarding.png?w=2500&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=cf81c5776781f5a045c00188525d9a26 2500w" />
    </Frame>
  </Tab>
</Tabs>

### 4. Let's Surf!

<Frame>
  <video autoPlay muted loop playsInline src="https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/onboarding/lets_surf.mp4?fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=8f26c1a8770b94a299752d7401149cff" data-path="assets/windsurf/onboarding/lets_surf.mp4" />
</Frame>

<Card title="Recommended Plugins" icon="puzzle-piece" href="/windsurf/recommended-plugins">
  Explore some of our recommended plugins to get the most out of Windsurf!
</Card>

## Update Windsurf

To update Windsurf, you can click on the "Restart to Update ->" button in the top right corner of the menu bar.

<Frame>
  <img src="https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/update-windsurf.png?fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=254e39b2e81a7746d82b36387dae2504" data-og-width="600" width="600" data-og-height="66" height="66" data-path="assets/windsurf/update-windsurf.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/update-windsurf.png?w=280&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=3d8ddcf4953bf6e6d473ca409c8339b5 280w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/update-windsurf.png?w=560&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=57ee243166d1fb0c3f484e42e754e8d6 560w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/update-windsurf.png?w=840&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=795caa1807eaf8a2ec8f4b17bf45605f 840w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/update-windsurf.png?w=1100&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=0220ef88f8a4255335a85a7a706ae978 1100w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/update-windsurf.png?w=1650&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=9b6016aea367886fe6bba680cba079e3 1650w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/update-windsurf.png?w=2500&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=a99b17d4724852271eb9ff1585dda26f 2500w" />
</Frame>

If you are not seeing this button, you can:

1. Click on your Profile icon dropdown > Check for Updates

2. In the Command Palette (`Cmd/Ctrl+Shift+P`) > "Check for Updates"

## Things to Try

Now that you've successfully opened Windsurf, let's try out some of the features! These are all conveniently accessible from the starting page. :)

<AccordionGroup>
  <Accordion title="Write with Cascade">
    <Frame>
      <img src="https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade.png?fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=1e48173bc3499c03f11be933a6b45596" data-og-width="2062" width="2062" data-og-height="1548" height="1548" data-path="assets/windsurf/cascade.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade.png?w=280&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=a4971f06a1b0db06e584fb6d1ef559e0 280w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade.png?w=560&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=779260952ff032eb725ead59de3df12f 560w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade.png?w=840&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=188aa1618c8cbb1d2071fe1c61ab848e 840w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade.png?w=1100&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=fbd11dcdb5a734646efbe9c614daa11c 1100w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade.png?w=1650&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=c41b8d9fc7646a394c6782ec32bd7481 1650w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade.png?w=2500&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=90ea2b0b61b99a87656c598c4021b809 2500w" />
    </Frame>

    On the right side of the IDE, you'll notice a new panel called "Cascade". This is your AI-powered code assistant! You can chat, write code, and run code with Cascade! Learn more about how it works [here](/windsurf/cascade).
  </Accordion>

  <Accordion title="Generate a project with Cascade">
    <Frame>
      <img src="https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade_generate.png?fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=876d94d833f7156fb19ced5da29ac3f9" data-og-width="2062" width="2062" data-og-height="1548" height="1548" data-path="assets/windsurf/cascade_generate.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade_generate.png?w=280&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=ffa1ab7d0b8dd0c9fe90aa7d77bf77a9 280w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade_generate.png?w=560&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=6889dda9cc550bddf283314ab8f9b133 560w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade_generate.png?w=840&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=fb86594ac84530a6702a7537ef69448c 840w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade_generate.png?w=1100&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=05e25b8b725389e3b07bf37fe9eddca8 1100w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade_generate.png?w=1650&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=73771a74119b9a4a6866b4319536409f 1650w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade_generate.png?w=2500&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=df50412402714a91aee87be93835ef3c 2500w" />
    </Frame>

    You can create brand new projects with Cascade! Click the "New Project" button to get started.
  </Accordion>

  <Accordion title="Open Folder / Connect to Remote Server">
    <Frame>
      <img src="https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/open_workspace.png?fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=23af27c11317a2d69cb04f092e1da13f" data-og-width="2062" width="2062" data-og-height="1548" height="1548" data-path="assets/windsurf/open_workspace.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/open_workspace.png?w=280&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=d603279bad581f354e6b43903514b7c1 280w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/open_workspace.png?w=560&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=56ece329970c50df74c3cdbe5246ca91 560w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/open_workspace.png?w=840&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=4183d72c3d95711f349488d9aa2fe706 840w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/open_workspace.png?w=1100&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=963000e12ded6a54a1bb92254a5c1d8e 1100w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/open_workspace.png?w=1650&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=6f924d832f13ea8129faff2f8efe0afc 1650w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/open_workspace.png?w=2500&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=2836093ae7dfcd22a42c2b67c7e6aec0 2500w" />
    </Frame>

    You can open a folder or connect to a remote server via SSH or a local dev container. Learn more [here](/windsurf/advanced).
  </Accordion>

  <Accordion title="Configure Windsurf Settings">
    <Frame>
      <img style={{width: '50%', display: 'block', margin: 'auto'}} src="https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/windsurf-settings-panel.png?fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=4f123cb41fe4557a31249af717324652" data-og-width="754" width="754" data-og-height="986" height="986" data-path="assets/windsurf/windsurf-settings-panel.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/windsurf-settings-panel.png?w=280&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=580c37ac863ac6d056b9a1d3f49af8eb 280w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/windsurf-settings-panel.png?w=560&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=611c985dd4341ebeea5849ddd0d799c8 560w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/windsurf-settings-panel.png?w=840&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=23e9348bda1251078fafbdc0b3d7d4de 840w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/windsurf-settings-panel.png?w=1100&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=139591b7dee7631615f7796a513a57bb 1100w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/windsurf-settings-panel.png?w=1650&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=2160a7972f2119c212a360dde6774215 1650w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/windsurf-settings-panel.png?w=2500&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=46fc8a94ad9db6a25dcb56add2a41b12 2500w" />
    </Frame>

    Click on the "Windsurf - Settings" button on the bottom right to pop up the settings panel. To access Advanced Settings, click on the button in this panel or select "Windsurf Settings" in the top right profile dropdown.
  </Accordion>

  <Accordion title="Open Command Palette">
    <Frame>
      <img src="https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/command_palette.png?fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=8fb19cd757b7daa72bf441aa71d30a7f" data-og-width="2058" width="2058" data-og-height="1544" height="1544" data-path="assets/windsurf/command_palette.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/command_palette.png?w=280&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=f26ee32a3ed595e17c26d622f660071a 280w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/command_palette.png?w=560&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=4d0161b7ea21da7e8aa9ef9027012b7c 560w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/command_palette.png?w=840&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=19ce0df2dca06c79c1e7b67c18683d23 840w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/command_palette.png?w=1100&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=09452a389208d7ea9090bb1f1bb26cde 1100w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/command_palette.png?w=1650&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=dfddd4ad6e05a1b309307b3812c0faee 1650w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/command_palette.png?w=2500&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=d76eba40fdf193ce8452b73c79872786 2500w" />
    </Frame>

    You can open the command palette with the `⌘+⇧+P` (on Mac) or `Ctrl+Shift+P` (on Windows/Linux) shortcut. Explore the available commands!
  </Accordion>
</AccordionGroup>

## Forgot to Import VS Code Configurations?

You can easily import your VS Code/Cursor configuration into Windsurf if you decide to do so after the onboarding process.

Open the command palette (Mac: `⌘+⇧+P`, Windows/Linux: `Ctrl+Shift+P`) and type in the following:

<Tabs>
  <Tab title="VS Code">
    <Frame>
      <img src="https://mintcdn.com/codeium/d8O4q6w3H2CjrirL/assets/import-vscode.png?fit=max&auto=format&n=d8O4q6w3H2CjrirL&q=85&s=ad0b864c3db087628f26d86241d23616" data-og-width="1452" width="1452" data-og-height="404" height="404" data-path="assets/import-vscode.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/d8O4q6w3H2CjrirL/assets/import-vscode.png?w=280&fit=max&auto=format&n=d8O4q6w3H2CjrirL&q=85&s=3f4f14bb9d1a267b2db392eadb96a0bf 280w, https://mintcdn.com/codeium/d8O4q6w3H2CjrirL/assets/import-vscode.png?w=560&fit=max&auto=format&n=d8O4q6w3H2CjrirL&q=85&s=b9c0a03c827f00476da27cf7c8332781 560w, https://mintcdn.com/codeium/d8O4q6w3H2CjrirL/assets/import-vscode.png?w=840&fit=max&auto=format&n=d8O4q6w3H2CjrirL&q=85&s=6d190021d5db196d2bba19a75f0db97c 840w, https://mintcdn.com/codeium/d8O4q6w3H2CjrirL/assets/import-vscode.png?w=1100&fit=max&auto=format&n=d8O4q6w3H2CjrirL&q=85&s=c2179de3cf831230df52c0fa3fdd536f 1100w, https://mintcdn.com/codeium/d8O4q6w3H2CjrirL/assets/import-vscode.png?w=1650&fit=max&auto=format&n=d8O4q6w3H2CjrirL&q=85&s=fbd66a97327cae9d6e6f9ef3e9e675cf 1650w, https://mintcdn.com/codeium/d8O4q6w3H2CjrirL/assets/import-vscode.png?w=2500&fit=max&auto=format&n=d8O4q6w3H2CjrirL&q=85&s=a26ade4508041ac54a5824220b28adf9 2500w" />
    </Frame>
  </Tab>

  <Tab title="Cursor">
    <Frame>
      <img src="https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/import-cursor.png?fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=a96df0b3235675e3713d0bf306170130" data-og-width="1454" width="1454" data-og-height="272" height="272" data-path="assets/windsurf/import-cursor.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/import-cursor.png?w=280&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=9c5a65d015d3317e1a0ef82198b773db 280w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/import-cursor.png?w=560&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=c43270598e2c7b8c2076dd1c8a61988c 560w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/import-cursor.png?w=840&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=34466e33238f48ad21cb0562d8ac614b 840w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/import-cursor.png?w=1100&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=bc477138c32b95bb6fcb393c647a52fb 1100w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/import-cursor.png?w=1650&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=7ef71a68b964490ce26e621198c7f4a2 1650w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/import-cursor.png?w=2500&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=c0d6766df74a3902b395d6120fb2c1c5 2500w" />
    </Frame>
  </Tab>
</Tabs>

## Incompatible Extensions

There are a few extensions that are incompatible with Windsurf. These include other AI code complete extensions and proprietary extensions. You cannot install extensions through any marketplace on Windsurf.

## Custom App Icons (beta)

For paying users of Windsurf, you can choose between different Windsurf icons while it sits in your dock. Currently, this feature is only available for Mac OS, with other operating systems coming soon.

To change your app icon, simply click the profile/settings icon in the top right corner of the editor and select "Customize App Icon".

## Windsurf Next

Windsurf Next is prerelease version of Windsurf which users can choose to opt-in to access the newest features and capabilities as early as possible, even if the features are not fully polished. Features will typically be rolled out to Windsurf Next first, and then into the stable release shortly after.

You can opt-in to Windsurf Next simply by [downloading it here](https://windsurf.com/editor/download-next).

## Uninstall Windsurf

To uninstall Windsurf from your system, follow these steps:

<Steps>
  <Step title="Close Windsurf">
    Ensure that Windsurf is not currently running before proceeding with the uninstallation.
  </Step>

  <Step title="Delete the Windsurf application">
    <Tabs>
      <Tab title="Mac">
        Drag the Windsurf application from the Applications folder to the Trash.
      </Tab>

      <Tab title="Windows">
        The application is usually located in one of these folders:

        * `C:\Program Files\Windsurf`
        * `C:\Users\[YourUsername]\AppData\Local\Programs\Windsurf`

        Delete the Windsurf folder from the appropriate location.
      </Tab>

      <Tab title="Linux">
        Remove the Windsurf folder from the location where you installed it.
      </Tab>
    </Tabs>
  </Step>

  <Step title="Remove configuration files">
    <Tabs>
      <Tab title="Mac/Linux">
        Delete the Windsurf configuration folder:

        ```bash  theme={null}
        rm -rf ~/.codeium/windsurf
        ```
      </Tab>

      <Tab title="Windows">
        Delete the Windsurf configuration folder:

        ```
        C:\Users\[YourUsername]\.codeium\windsurf
        ```
      </Tab>
    </Tabs>
  </Step>

  <Step title="Additional cleanup">
    <ul>
      <li>If you installed Windsurf in PATH, remove it from your system's PATH environment variable.</li>
      <li>If you installed Windsurf using your system's package manager or control panel, you can also use that to uninstall it.</li>
      <li>Empty your Trash or Recycle Bin to complete the uninstallation.</li>
    </ul>
  </Step>
</Steps>



# Guide for Admins
Source: https://docs.windsurf.com/windsurf/guide-for-admins

Windsurf Guide for Enterprise Admins


# Windsurf Guide for Enterprise Admins

> **Purpose**   This guide helps enterprise *platform / developer-experience* administrators plan, roll out, and operate Windsurf for organizations with **large enterprise teams**.  It is intentionally *opinionated* and links out to detailed “how-to” docs per topic.  Treat it both as a **read-through guide** *and* as a **check-list** when onboarding.

***

## 1.   Audience & Pre-Requisites

|                       | Details                                                                            |
| --------------------- | ---------------------------------------------------------------------------------- |
| **Who should read**   | Platform / Dev-Ex admins, Corporate IT, Centralized Tooling teams                  |
| **Assumed knowledge** | Basic Windsurf terms (team, role), Enterprise IdP concepts (SAML, SCIM), CLI usage |
| **Out-of-scope**      | Deep security / compliance internals → see **Security & Compliance** docs          |

***

## 2.   Quick-Start Checklist

1. Confirm organization-wide settings
2. Set up **SSO** (Okta, Azure AD, Google; see SAML docs for others)
3. Enable **SCIM** & map IdP groups → Windsurf *teams*
4. Define **role** & **permission** model (least privilege)
5. Configure **Admin Portal**: team view & security controls
6. Distribute **Windsurf clients/extensions** to end users
7. View **analytics dashboards** & **API access tokens**

> Use this list as your “Day 0” deployment tracker.

***

## 3.   Core Windsurf Concepts

* **Team** – flat collections of members; no nested teams. Teams (also called *Groups*) drive **role assignment** and **analytics grouping**, letting you scope permissions and view usage metrics per cohort.
* **Roles & Permissions** – predefined RBAC; admins are primarily responsible for **team management**, **Windsurf feature settings**, and **analytics**. Built-in roles usually cover these needs, but creating a custom role with *analytics-view* permission lets team managers and leads see metrics for their own teams. (<a href="/windsurf/accounts/rbac-role-management" target="_blank">RBAC docs</a>)
* **Admin Portal** – centralized UI for user & team management, credit usage, SSO configuration, feature toggles (<a href="/windsurf/cascade/web-search" target="_blank">Web Search</a>, <a href="/windsurf/cascade/mcp" target="_blank">MCP</a>, <a href="/windsurf/cascade/app-deploys" target="_blank">Deploys</a>), analytics dashboards/report export, service keys for API usage, and role/permission controls.
* **Agents & Workspaces** – Windsurf IDE and Jetbrains Plugins are Agentic

### 3.1   Admin Portal Overview

The Admin Portal provides centralized management for all Windsurf enterprise features through an intuitive web interface. Core capabilities include:

#### User & Team Management

* Add, remove, and manage users across your organization
* Configure teams with proper role assignments
* User status and activity monitoring

#### Authentication & Security

* Configure SSO integration with major identity providers
* Set up SCIM provisioning for automated user lifecycle management
* Manage role-based access controls (RBAC)
* Create and manage **service keys** for API automations with scoped permissions

#### Feature Toggles & Controls

> **Important:** These feature controls affect behavior for your entire organization and can only be modified by administrators. New major features with data privacy implications are released in the "off" state by default to ensure you have control over when and how they're enabled.

The <a href="https://windsurf.com/team/settings" target="_blank">Admin Portal</a> gives you granular control over Windsurf features that can be enabled or disabled per team. **Data Privacy Note:** Some features require storing additional data or telemetry as noted below:

**Models Configuration**

* Configure which AI models your teams can access within Windsurf
* Select multiple models for different use cases (code completion, chat, etc.)

**Auto Run Terminal Commands** *(Beta)*

* Allow or restrict Cascade's ability to auto-execute commands on users' machines
* [Learn more about auto-executed commands](https://docs.windsurf.com/windsurf/terminal#auto-executed-cascade-commands)

**MCP Servers** *(Beta)*

* Enable users to configure and use Model Context Protocol (MCP) servers
* Maintain whitelisted MCP servers for approved integrations
* **Security Note:** Review operational and security implications before enabling, as MCP can create infrastructure resources outside Windsurf's security monitoring
* <a href="https://docs.windsurf.com/plugins/cascade/mcp#model-context-protocol-mcp" target="_blank">Learn more about Model Context Protocol (MCP)</a>
* <a href="https://docs.windsurf.com/plugins/cascade/mcp#admin-controls-teams-%26-enterprises" target="_blank">MCP admin controls for teams & enterprises</a>

**App Deploys** *(Beta)*

* Manage deployment permissions for your teams in Cascade
* <a href="https://docs.windsurf.com/windsurf/cascade/app-deploys#app-deploys" target="_blank">Learn more about App Deploys</a>

**Conversation Sharing**

* Allow team members to share Cascade conversations with others
* Conversations are securely uploaded to Windsurf servers
* Shareable links are restricted to logged-in team members only
* <a href="https://docs.windsurf.com/windsurf/cascade/cascade#sharing-your-conversation" target="_blank">Learn more about sharing conversations</a>

**PR Reviews (GitHub Integration)**

* Install Windsurf in your team's GitHub organization
* Enable PR review automation and description editing
* <a href="https://docs.windsurf.com/windsurf-reviews/windsurf-reviews#windsurf-pr-reviews" target="_blank">Learn more about Windsurf PR Reviews</a>

**Knowledge Base Management**

* Curate knowledge from Google Drive sources for your development teams
* Upload and organize internal documentation and resources
* <a href="https://docs.windsurf.com/context-awareness/overview#knowledge-base-beta" target="_blank">Learn more about Knowledge Base</a>

***

## 4.   Identity & Access Management

> **Recommendation:** Use **SSO plus SCIM** wherever possible for automated provisioning, de-provisioning, and group management.

### 4.1   Single Sign-On (SSO)

|                          | Guidance                                                                                                               |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------- |
| **IdPs supported**       | Okta, Azure AD, Google (others via generic SAML)                                                                       |
| **Recommended approach** | Create Windsurf-specific *app* in IdP; use **role-based** group assignments rather than org-wide `All Employees` group |
| **Common pitfalls**      | Email suffix mismatches, duplicate user aliases                                                                        |

*See the <a href="https://docs.windsurf.com/windsurf/accounts/sso-scim" target="_blank">SSO & SCIM Setup Guide</a> for step-by-step configuration for Okta, Azure AD, Google, and Generic SAML.*

### 4.2   SCIM Provisioning

* **Why** – automated user lifecycle & team membership management at scale
* **Capabilities**
  * Create / deactivate **users** automatically
  * Create **teams** automatically (or manage manually)
  * Users can belong to **multiple teams**
  * Custom team creation via SCIM API (<a href="https://docs.windsurf.com/windsurf/accounts/sso-scim#scim-api" target="_blank">docs</a>)
* **Mapping strategies**
  * 1 IdP group → 1 Windsurf team (simple, most common)
  * Functional vs. project-based group prefixes (e.g. `proj-foo-devs`)
* **Things to decide**
  * Which groups to *exclude* (e.g. interns, contractors)
  * Renaming rules when IdP group names change
* **Caution**: SCIM should remain your **source of truth**—mixing SCIM and manual / API updates can create drift. Use the API mainly for adding supplemental groups.

***

## 5.   User & Team Management at Scale

* Flat *team* → design team taxonomy carefully (no nesting to fall back on)
* Users can belong to **multiple groups**. Groups are used to view analytics
* Today, SCIM does not support assigning roles to users. SCIM only supports assigning users to Groups

***

## 6.   Analytics & API Access

### 6.1   Built-In Analytics

| Dashboard             | Use-case                                   |
| --------------------- | ------------------------------------------ |
| **Adoption Overview** | Track total active users, daily engagement |
| **Team Activity**     | Team usage                                 |

Analytics shows the **percentage of code written by Windsurf**, helping quantify impact—see your dashboards at <a href="https://windsurf.com/team/analytics" target="_blank">team analytics</a>.

### 6.2   APIs

| API      | Typical admin scenarios    |
| -------- | -------------------------- |
| **REST** | SCIM management, analytics |

* Generate service keys under <a href="https://windsurf.com/team/settings" target="_blank">**Team Settings → Service Keys**</a>. Scope keys to *least privilege* needed.
* More advanced reporting: see the <a href="https://docs.windsurf.com/plugins/accounts/api-reference/introduction" target="_blank">Analytics API Reference</a>.
* For team management: see the <a href="https://docs.windsurf.com/windsurf/accounts/sso-scim#scim-api" target="_blank">SCIM API – Custom Teams</a>.

***

## 7.   Operational Considerations

* **Status Pages** – monitor live service health: <a href="https://status.windsurf.com/" target="_blank">Windsurf</a>, <a href="https://status.anthropic.com/" target="_blank">Anthropic</a>, <a href="https://status.openai.com/" target="_blank">OpenAI</a>
* **Support Channels** – windsurf.com/support

***

## 8.   Setting Up End Users for Success

1. Point end users to the <a href="https://docs.windsurf.com/windsurf/getting-started" target="_blank">Windsurf installation guide</a> to install the appropriate extension or desktop client.
2. Publish an internal “Getting Started with Windsurf” page (link to official docs)
3. Hold live onboarding sessions / record short demos
4. Curate starter project templates & sample prompts
5. Collect feedback via survey after 2 weeks; iterate

***

## 9.   Additional Resources

* <a href="https://docs.windsurf.com/windsurf/accounts/sso-scim" target="_blank">SSO & SCIM Setup Guide</a>
* <a href="https://docs.windsurf.com/windsurf/accounts/sso-scim#scim-api" target="_blank">SCIM API – Custom Teams</a>
* <a href="https://docs.windsurf.com/plugins/accounts/api-reference/introduction" target="_blank">Analytics API Reference</a>
* <a href="/windsurf/accounts/rbac-role-management" target="_blank">RBAC Controls</a>



# Models
Source: https://docs.windsurf.com/windsurf/models



export const ModelsTable = () => {
  const [showAll, setShowAll] = useState(false);
  const windsurfIcon = {
    light: "https://exafunction.github.io/public/icons/docs/Windsurf-black-symbol.png",
    dark: "https://exafunction.github.io/public/icons/docs/Windsurf-white-symbol.png"
  };
  const openaiIcon = {
    light: "https://exafunction.github.io/public/icons/docs/OpenAI-black-monoblossom.png",
    dark: "https://exafunction.github.io/public/icons/docs/OpenAI-white-monoblossom.png"
  };
  const claudeIcon = {
    light: "https://exafunction.github.io/public/icons/docs/claude-logo-clay.png",
    dark: "https://exafunction.github.io/public/icons/docs/claude-logo-clay.png"
  };
  const deepseekIcon = {
    light: "https://exafunction.github.io/public/icons/docs/deepseek-logo.png",
    dark: "https://exafunction.github.io/public/icons/docs/deepseek-logo.png"
  };
  const geminiIcon = {
    light: "https://exafunction.github.io/public/icons/docs/gemini-models-icon.png",
    dark: "https://exafunction.github.io/public/icons/docs/gemini-models-icon.png"
  };
  const grokIcon = {
    light: "https://exafunction.github.io/public/icons/docs/Grok_Logomark_Dark.png",
    dark: "https://exafunction.github.io/public/icons/docs/Grok_Logomark_Light.png"
  };
  const qwenIcon = {
    light: "https://exafunction.github.io/public/icons/docs/qwen-logo.png",
    dark: "https://exafunction.github.io/public/icons/docs/qwen-logo.png"
  };
  const kimiIcon = {
    light: "https://exafunction.github.io/public/icons/docs/kimi-k2-icon.png",
    dark: "https://exafunction.github.io/public/icons/docs/kimi-k2-icon.png"
  };
  const byokOnly = <a href="/windsurf/models#bring-your-own-key-byok" className="text-gray-700 dark:text-white font-normal">BYOK</a>;
  const apiPricingOnly = <a href="/windsurf/models#api-pricing" className="text-gray-700 dark:text-white font-normal">API Pricing</a>;
  const empty = "";
  const byokApiPricing = <>{byokOnly}<br />/<br />{apiPricingOnly}</>;
  const checkmark = <>
      <img className="block dark:hidden" src={"https://exafunction.github.io/public/icons/docs/checkmark-black.png"} alt="Available" style={{
    width: '16px',
    height: '16px',
    margin: '0 auto',
    pointerEvents: 'none'
  }} />
      <img className="hidden dark:block" src={"https://exafunction.github.io/public/icons/docs/checkmark-white.png"} alt="Available" style={{
    width: '16px',
    height: '16px',
    margin: '0 auto',
    pointerEvents: 'none'
  }} />
    </>;
  const models = [{
    name: "SWE-1.5",
    icon: windsurfIcon,
    credits: "1",
    hasGift: true,
    free: empty,
    pro: checkmark,
    teams: checkmark,
    enterprise: checkmark,
    trial: checkmark
  }, {
    name: "SWE-1",
    icon: windsurfIcon,
    credits: "0",
    hasGift: true,
    free: checkmark,
    pro: checkmark,
    teams: checkmark,
    enterprise: checkmark,
    trial: checkmark
  }, {
    name: "Claude Sonnet 4.5",
    icon: claudeIcon,
    credits: "2",
    hasGift: true,
    free: checkmark,
    pro: checkmark,
    teams: checkmark,
    enterprise: "3x",
    trial: checkmark
  }, {
    name: "Claude Sonnet 4.5 (Thinking)",
    icon: claudeIcon,
    credits: "3",
    hasGift: true,
    free: checkmark,
    pro: checkmark,
    teams: checkmark,
    enterprise: "4x",
    trial: checkmark
  }, {
    name: "Claude Haiku 4.5",
    icon: claudeIcon,
    credits: "1",
    free: checkmark,
    pro: checkmark,
    teams: checkmark,
    enterprise: checkmark,
    trial: checkmark
  }, {
    name: "Claude Opus 4.1",
    icon: claudeIcon,
    credits: "20",
    free: empty,
    pro: checkmark,
    teams: checkmark,
    enterprise: checkmark,
    trial: checkmark
  }, {
    name: "Claude Opus 4.1 Thinking",
    icon: claudeIcon,
    credits: "20",
    free: empty,
    pro: checkmark,
    teams: checkmark,
    enterprise: checkmark,
    trial: checkmark
  }, {
    name: "GPT-5 (low reasoning)",
    icon: openaiIcon,
    credits: "0.5",
    free: "0.5",
    pro: checkmark,
    teams: checkmark,
    enterprise: checkmark,
    trial: checkmark
  }, {
    name: "GPT-5 (medium reasoning)",
    icon: openaiIcon,
    credits: "1",
    free: "0.5",
    pro: checkmark,
    teams: checkmark,
    enterprise: checkmark,
    trial: checkmark
  }, {
    name: "GPT-5 (high reasoning)",
    icon: openaiIcon,
    credits: "2",
    free: "1.5",
    pro: checkmark,
    teams: checkmark,
    enterprise: checkmark,
    trial: checkmark
  }, {
    name: "GPT-5-Codex",
    icon: openaiIcon,
    credits: "0",
    hasGift: true,
    free: "0.5",
    pro: checkmark,
    teams: checkmark,
    enterprise: checkmark,
    trial: checkmark
  }, {
    name: "Gemini 2.5 Pro",
    icon: geminiIcon,
    credits: "1",
    free: checkmark,
    pro: checkmark,
    teams: checkmark,
    enterprise: checkmark,
    trial: checkmark
  }, {
    name: "xAI Grok Code Fast",
    icon: grokIcon,
    credits: "0",
    hasGift: true,
    free: empty,
    pro: checkmark,
    teams: checkmark,
    enterprise: checkmark,
    trial: checkmark
  }, {
    name: "Kimi K2",
    icon: kimiIcon,
    credits: "0.5",
    free: empty,
    pro: checkmark,
    teams: checkmark,
    enterprise: empty,
    trial: checkmark
  }, {
    name: "Qwen3-Coder Fast",
    icon: qwenIcon,
    credits: "2",
    hasGift: true,
    free: empty,
    pro: checkmark,
    teams: checkmark,
    enterprise: empty,
    trial: checkmark
  }, {
    name: "Qwen3-Coder",
    icon: qwenIcon,
    credits: "0.5",
    free: empty,
    pro: checkmark,
    teams: checkmark,
    enterprise: empty,
    trial: checkmark
  }, {
    name: "o3",
    icon: openaiIcon,
    credits: "1",
    free: checkmark,
    pro: checkmark,
    teams: checkmark,
    enterprise: checkmark,
    trial: checkmark
  }, {
    name: "o3 (high reasoning)",
    icon: openaiIcon,
    credits: "1",
    free: checkmark,
    pro: checkmark,
    teams: checkmark,
    enterprise: checkmark,
    trial: checkmark
  }, {
    name: "Claude 3.7 Sonnet",
    icon: claudeIcon,
    credits: "2",
    free: byokOnly,
    pro: checkmark,
    teams: checkmark,
    enterprise: "1x",
    trial: byokOnly
  }, {
    name: "Claude 3.7 Sonnet (Thinking)",
    icon: claudeIcon,
    credits: "3",
    free: byokOnly,
    pro: checkmark,
    teams: checkmark,
    enterprise: "1.25x",
    trial: byokOnly
  }, {
    name: "Claude Sonnet 4",
    icon: claudeIcon,
    credits: "2",
    hasGift: true,
    free: byokOnly,
    pro: checkmark,
    teams: checkmark,
    enterprise: "3x",
    trial: checkmark
  }, {
    name: "Claude Sonnet 4 (Thinking)",
    icon: claudeIcon,
    credits: "3",
    hasGift: true,
    free: byokOnly,
    pro: checkmark,
    teams: checkmark,
    enterprise: "4x",
    trial: checkmark
  }, {
    name: "gpt-oss 120B (Medium)",
    icon: openaiIcon,
    credits: "0.25",
    free: empty,
    pro: checkmark,
    teams: checkmark,
    enterprise: checkmark,
    trial: checkmark
  }, {
    name: "GPT-4o",
    icon: openaiIcon,
    credits: "1",
    free: checkmark,
    pro: checkmark,
    teams: checkmark,
    enterprise: checkmark,
    trial: checkmark
  }, {
    name: "GPT-4.1",
    icon: openaiIcon,
    credits: "1",
    free: checkmark,
    pro: checkmark,
    teams: checkmark,
    enterprise: checkmark,
    trial: checkmark
  }, {
    name: "Claude 3.5 Sonnet",
    icon: claudeIcon,
    credits: "2",
    free: byokOnly,
    pro: checkmark,
    teams: checkmark,
    enterprise: checkmark,
    trial: byokOnly
  }, {
    name: "Claude 4 Opus",
    icon: claudeIcon,
    credits: byokOnly,
    free: byokOnly,
    pro: byokOnly,
    teams: empty,
    enterprise: empty,
    trial: byokOnly
  }, {
    name: "Claude 4 Opus (Thinking)",
    icon: claudeIcon,
    credits: byokOnly,
    free: byokOnly,
    pro: byokOnly,
    teams: empty,
    enterprise: empty,
    trial: byokOnly
  }, {
    name: "DeepSeek-V3-0324",
    icon: deepseekIcon,
    credits: "0",
    free: empty,
    pro: checkmark,
    teams: empty,
    enterprise: empty,
    trial: checkmark
  }, {
    name: "DeepSeek-R1",
    icon: deepseekIcon,
    credits: "0.5",
    free: empty,
    pro: checkmark,
    teams: empty,
    enterprise: empty,
    trial: checkmark
  }];
  return <>
      <style>{`
        .gift-tooltip-container:hover .gift-tooltip {
          opacity: 1 !important;
          visibility: visible !important;
        }
        #table-container {
          overflow: visible !important;
          max-height: none !important;
          height: auto !important;
        }
        #models-table {
          overflow: visible !important;
          max-height: none !important;
          height: auto !important;
        }
        @media (max-width: 768px) {
          #table-container {
            overflow-x: auto !important;
            -webkit-overflow-scrolling: touch !important;
          }
          #models-table {
            min-width: 700px !important;
          }
        }
        #table-container * {
          overflow: visible !important;
        }
      `}</style>
      <div id="table-container" style={{
    width: 'auto',
    borderRadius: '8px',
    overflow: 'visible',
    maxHeight: 'none',
    height: 'auto'
  }} className="light:bg-white dark:bg-zinc-900 border border-black/10 dark:border-white/10">
        <table id="models-table" style={{
    width: '100%',
    borderCollapse: 'collapse',
    fontSize: '14px',
    tableLayout: 'auto',
    margin: '0',
    padding: '0',
    height: 'auto',
    maxHeight: 'none'
  }}>
          <thead style={{
    margin: '0',
    padding: '0'
  }}>
            <tr className="border-b border-black/10 dark:!border-white/10">
              <th style={{
    padding: '16px 16px',
    textAlign: 'left',
    fontWeight: '500',
    minWidth: '200px'
  }} className="text-gray-700 dark:text-white">Model</th>
              <th style={{
    padding: '16px 8px',
    textAlign: 'center',
    fontWeight: '500',
    minWidth: '80px'
  }} className="text-gray-700 dark:text-white">Credits</th>
              <th style={{
    padding: '16px 8px',
    textAlign: 'center',
    fontWeight: '500',
    minWidth: '60px'
  }} className="text-gray-700 dark:text-white">Free</th>
              <th style={{
    padding: '16px 8px',
    textAlign: 'center',
    fontWeight: '500',
    minWidth: '60px'
  }} className="text-gray-700 dark:text-white">Pro</th>
              <th style={{
    padding: '16px 8px',
    textAlign: 'center',
    fontWeight: '500',
    minWidth: '80px'
  }} className="text-gray-700 dark:text-white">Teams</th>
              <th style={{
    padding: '16px 8px',
    textAlign: 'center',
    fontWeight: '500',
    minWidth: '120px'
  }} className="text-gray-700 dark:text-white">Enterprise</th>
              <th style={{
    padding: '16px 8px',
    textAlign: 'center',
    fontWeight: '500',
    minWidth: '60px'
  }} className="text-gray-700 dark:text-white">Trial</th>
            </tr>
          </thead>
          <tbody style={{
    margin: '0',
    padding: '0'
  }}>
            {models.filter((model, index) => showAll || index < 12).map((model, index, filteredArray) => <tr key={model.name} className={`${index === filteredArray.length - 1 ? '' : 'border-b border-black/10 dark:!border-white/10'}`}>
                <td style={{
    padding: '8px',
    fontWeight: '500',
    verticalAlign: 'middle'
  }}>
                  <div style={{
    display: 'flex',
    alignItems: 'center',
    gap: '8px',
    whiteSpace: 'nowrap'
  }}>
                    <span style={{
    display: 'inline-flex',
    alignItems: 'center',
    justifyContent: 'center',
    width: '20px',
    height: '20px',
    flexShrink: 0
  }}>
                      <img className="block dark:hidden" src={model.icon.light} alt={`${model.name} icon`} style={{
    width: '20px',
    height: '20px',
    objectFit: 'contain',
    pointerEvents: 'none',
    userSelect: 'none'
  }} />
                      <img className="hidden dark:block" src={model.icon.dark} alt={`${model.name} icon`} style={{
    width: '20px',
    height: '20px',
    objectFit: 'contain',
    pointerEvents: 'none',
    userSelect: 'none'
  }} />
                    </span>
                    <span className="text-gray-700 dark:text-white">{model.name}</span>
                  </div>
                </td>
                <td style={{
    padding: '10px',
    textAlign: 'center',
    verticalAlign: 'middle'
  }}>
                  <div style={{
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    gap: '4px'
  }}>
                    <span className="text-gray-700 dark:text-white">{model.credits}</span>
                    {model.hasGift && <div className="gift-tooltip-container" style={{
    position: 'relative',
    display: 'inline-flex'
  }}>
                        <span style={{
    display: 'inline-flex',
    alignItems: 'center',
    justifyContent: 'center',
    width: '16px',
    height: '16px'
  }}>
                          <img className="block dark:hidden" src="https://exafunction.github.io/public/icons/docs/gift-black.png" alt="Gift icon" style={{
    width: '16px',
    height: '16px',
    objectFit: 'contain',
    pointerEvents: 'none',
    userSelect: 'none'
  }} />
                          <img className="hidden dark:block" src="https://exafunction.github.io/public/icons/docs/gift-white.png" alt="Gift icon" style={{
    width: '16px',
    height: '16px',
    objectFit: 'contain',
    pointerEvents: 'none',
    userSelect: 'none'
  }} />
                        </span>
                        <div className="gift-tooltip" style={{
    position: 'absolute',
    bottom: '100%',
    left: '50%',
    transform: 'translateX(-50%)',
    marginBottom: '8px',
    padding: '8px 12px',
    backgroundColor: '#333',
    color: 'white',
    borderRadius: '6px',
    fontSize: '12px',
    whiteSpace: 'nowrap',
    opacity: '0',
    visibility: 'hidden',
    transition: 'opacity 0.2s, visibility 0.2s',
    zIndex: '1000',
    pointerEvents: 'none'
  }}>
                          Promo pricing only available for a limited time
                          <div style={{
    position: 'absolute',
    top: '100%',
    left: '50%',
    transform: 'translateX(-50%)',
    width: '0',
    height: '0',
    borderLeft: '5px solid transparent',
    borderRight: '5px solid transparent',
    borderTop: '5px solid #333'
  }}></div>
                        </div>
                      </div>}
                  </div>
                </td>
                <td style={{
    padding: '10px',
    textAlign: 'center',
    verticalAlign: 'middle'
  }}>{model.free}</td>
                <td style={{
    padding: '10px',
    textAlign: 'center',
    verticalAlign: 'middle'
  }}>{model.pro}</td>
                <td style={{
    padding: '10px',
    textAlign: 'center',
    verticalAlign: 'middle'
  }}>{model.teams}</td>
                <td style={{
    padding: '10px',
    textAlign: 'center',
    verticalAlign: 'middle'
  }}>{model.enterprise}</td>
                <td style={{
    padding: '10px',
    textAlign: 'center',
    verticalAlign: 'middle'
  }}>{model.trial}</td>
              </tr>)}
          </tbody>
        </table>
      </div>
      <div style={{
    display: 'flex',
    justifyContent: 'center',
    padding: '16px 0',
    borderTop: 'none'
  }}>
        <button onClick={() => {
    if (!showAll) {
      setShowAll(true);
    } else {
      setShowAll(false);
    }
  }} style={{
    display: 'inline-flex',
    alignItems: 'center',
    justifyContent: 'center',
    padding: '10px 20px',
    backgroundColor: 'transparent',
    border: '1px solid #868686',
    borderRadius: '8px',
    fontSize: '14px',
    fontWeight: '500',
    cursor: 'pointer',
    transition: 'all 0.2s ease',
    minWidth: '140px'
  }} className="text-gray-700 hover:bg-gray-50 dark:border-gray-600 dark:text-white dark:hover:bg-gray-800">
          {showAll ? 'Show Less Models' : 'Show More Models'}
        </button>
      </div>
    </>;
};

In Cascade, you can easily switch between different models of your choosing.

Depending on the model you select, each of your input prompts will consume a different number of [prompt credits](/windsurf/cascade/usage).

Under the text input box, you will see a model selection dropdown menu containing the following models:

<ModelsTable />


# SWE-1.5, swe-grep, SWE-1

Our SWE model family of in-house frontier models are built specifically for software engineering tasks.

Our latest frontier model, SWE-1.5, achieves near-SOTA performance in a fraction of the time.

Our in house models include:

* `SWE-1.5`: Our best agentic coding model we've released. Near Claude 4.5-level performance, at 13x the speed. Read our [research announcement](https://cognition.ai/blog/swe-1-5).
* `SWE-1`: Our first agentic coding model. Achieved Claude 3.5-level performance at a fraction of the cost.
* `SWE-1-mini`: Powers passive suggestions in Windsurf Tab, optimized for real-time latency.
* `swe-grep`: Powers context retrieval and [Fast Context](context-awareness/fast-context)


# Bring your own key (BYOK)

<Warning>This is only available to free and paid individual users.</Warning>

For certain models, we allow users to bring their own API keys. In the model dropdown menu, individual users will see models labled with `BYOK`.

To input your API key, navigate to [this page](https://windsurf.com/subscription/provider-api-keys) in the subscription settings and add your key.

If you have not configured your API key, it will return an error if you try to use the BYOK model.

Currently, we only support BYOK for these models:

* `Claude 4 Sonnet`
* `Claude 4 Sonnet (Thinking)`
* `Claude 4 Opus`
* `Claude 4 Opus (Thinking)`



# Windsurf Previews
Source: https://docs.windsurf.com/windsurf/previews



Windsurf Previews allow you to view the local deployment of your app either in the IDE or in the browser (optimized for Google Chrome, Arc, and Chromium based browsers) with listeners, allowing you to iterate rapidly by easily sending elements and errors back to Cascade as context.

<video autoPlay muted loop playsInline className="w-full aspect-video" src="https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/previews/browser-preview-demo.mp4?fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=b3befa08affd8c5c10a84ae9259d0f15" data-path="assets/windsurf/previews/browser-preview-demo.mp4" />

Windsurf Previews are opened via tool call, so just ask Cascade to preview your site to get started. Alternatively, you can also click the Web icon in the Cascade toolbar to automatically propagate the natural language prompt to enter the proxy.

<Frame style={{ border: 'none', background: 'none' }}>
  <img src="https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/previews/website-tools-icon.png?fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=6a607c6a7beaafe915760d80a78c8da6" data-og-width="392" width="392" data-og-height="216" height="216" data-path="assets/windsurf/previews/website-tools-icon.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/previews/website-tools-icon.png?w=280&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=7222fc826af6a55cb824fb3fce30ce84 280w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/previews/website-tools-icon.png?w=560&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=bfbfb672a37d24ef3f11a52c62ae050c 560w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/previews/website-tools-icon.png?w=840&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=bae2bad59e313d1fe53e47c3c9141f5b 840w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/previews/website-tools-icon.png?w=1100&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=a3cafe879660aa08f70dca8e269a3032 1100w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/previews/website-tools-icon.png?w=1650&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=038211eef5f4587cfced6ea316d62ec9 1650w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/previews/website-tools-icon.png?w=2500&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=9dff09c4af8de6a34ec980815bdc13cd 2500w" />
</Frame>


# Send Elements to Cascade

In the Preview, you can select and send elements/components and errors directly to Cascade. Simply click on the "Send element" button on the bottom right and then proceed to select the element you want to send.

The selected element will be inserted into your current Cascade prompt as an `@ mention`. You can add as many elements as you want in the prompt.


# In-IDE Preview

Windsurf can open a up a Preview as a new tab in your editor. This is a simple web view that enables you to view web app alongside your Cascade panel.

Because these Previews are hosted locally, you can open them in your system browser as well, complete with all the listeners and ability to select and send elements and console errors to Cascade.

<Warning>The listeners and the abilities to send elements and errors are optimized for Google Chrome, Arc, and Chromium based browsers.</Warning>


# How to Disable

You can disable Windsurf Previews from Windsurf - Settings. This will prevent Cascade from making this tool call.



# Recommended Extensions
Source: https://docs.windsurf.com/windsurf/recommended-extensions

Recommended Extensions for Windsurf


# Windsurf: Embracing the Agentic VS Code OSS Experience

<VideoEmbed src="https://www.loom.com/embed/fea821e99c554d8baadd746df3655dbe?sid=b6e8f249-1854-4780-a8bc-80fc8c91361c" />

## Recommended Extensions

### Extension Guidance

Windsurf, using VS Code's interface and AI, is easy to adopt for developers from VS, Eclipse, or VS Code. It uses the Open VSX Registry for extensions, accessible via the Extensions panel or website. To help you get the most out of Windsurf for different programming languages, we've compiled a list of popular, community-recommended extensions from the Open VSX marketplace that other users have found helpful for replicating familiar IDE experiences.

Be sure to check out the full Open VSX marketplace for other useful extensions that may suit your specific workflow needs!

### General

* [GitLens](https://open-vsx.org/extension/eamodio/gitlens) - Visualize code authorship at a glance via annotations and CodeLens
* [GitHub Pull Requests](https://open-vsx.org/extension/GitHub/vscode-pull-request-github) - Review and manage your GitHub pull requests and issues directly
* [GitLab Workflow](https://open-vsx.org/extension/gitlab/gitlab-workflow) - GitLab integration extension
* [Mermaid Markdown Preview](https://open-vsx.org/extension/bierner/markdown-mermaid) - Adds diagram and flowchart support
* [Visual Studio Keybindings](https://open-vsx.org/extension/ms-vscode/vs-keybindings) - Use Visual Studio keyboard shortcuts in Windsurf
* [Eclipse Keymap](https://open-vsx.org/extension/alphabotsec/vscode-eclipse-keybindings) - Use Eclipse keyboard shortcuts in Windsurf

### Python

* [ms-python.python](https://open-vsx.org/extension/ms-python/python) - Core Python support: IntelliSense, linting, debugging, and virtual environment management
* [Windsurf Pyright](https://open-vsx.org/extension/Codeium/windsurfPyright) - Fast, Pylance-like language server with strong type-checking and completions
* [Ruff](https://open-vsx.org/extension/charliermarsh/ruff) - Linter and code formatter
* [Python Debugger](https://open-vsx.org/extension/ms-python/debugpy) - Debugging support for Python applications

### Java

* [Extension Pack for Java](https://open-vsx.org/extension/vscjava/vscode-java-pack) - Bundle of essential Java tools: editing, refactoring, debugging, and project support (includes all below)
* [redhat.java](https://open-vsx.org/extension/redhat/java) - Core Java language server for IntelliSense, navigation, and refactoring
* [Java debug](https://open-vsx.org/extension/vscjava/vscode-java-debug) - Adds full Java debugging with breakpoints, variable inspection, etc.
* [Java Test Runner](https://open-vsx.org/extension/vscjava/vscode-java-test) - Run/debug JUnit/TestNG tests inside the editor with a testing UI
* [Maven](https://open-vsx.org/extension/vscjava/vscode-maven) - Maven support: manage dependencies, run goals, view project structure
* [Gradle](https://open-vsx.org/extension/vscjava/vscode-gradle) - Gradle support: task explorer, project insights, and CLI integration
* [Java Project Manager](https://open-vsx.org/extension/vscjava/vscode-java-dependency) - Visualize and manage Java project dependencies

### Visual Basic

* [Visual Basic Support](https://open-vsx.org/extension/vscode/vb) - Syntax highlighting, code snippets, bracket matching, code folding
* [VB Script Support](https://open-vsx.org/extension/Serpen/vbsvscode) - VBScript editing support: syntax highlighting, code outline view
* [C# support](https://open-vsx.org/extension/muhammad-sammy/csharp) - OmniSharp-based language server with IntelliSense and debugging
* [Solution Explorer](https://open-vsx.org/extension/fernandoescolar/vscode-solution-explorer) - Manage .sln and .csproj files visually

### C# / .NET and C++

* [C# / C++ Development Setup Guide](csharp-cpp) - Setup guide for .NET Core, .NET Framework (Mono), and C++ development in Windsurf



# Terminal
Source: https://docs.windsurf.com/windsurf/terminal




# Command in the terminal

Use our [Command](/command/overview) modality in the terminal (`Cmd/Ctrl+I`) to generate the proper CLI syntax from prompts in natural language.

<Frame style={{ border: 'none', background: 'none' }}>
  <img src="https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf-terminal-command.png?fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=b03f1498ac0b7dc344270f975f9a234f" data-og-width="980" width="980" data-og-height="164" height="164" data-path="assets/windsurf-terminal-command.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf-terminal-command.png?w=280&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=ec94b782cbe3b3d0a3e8d44ce7b27c74 280w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf-terminal-command.png?w=560&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=9e3839c701ba2308cbc754842c8472a4 560w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf-terminal-command.png?w=840&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=25245a6097e94c63ed47cb382097f82b 840w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf-terminal-command.png?w=1100&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=ecfdf898fe06e81255add438d3daff49 1100w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf-terminal-command.png?w=1650&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=c46a449c560b98a2e295e904601a3c51 1650w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf-terminal-command.png?w=2500&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=44ec229230a00b642a4aa61f1d4c571c 2500w" />
</Frame>


# Send terminal selection to Cascade

Highlight a portion of of the stack trace and press `Cmd/Ctrl+L` to send it to Cascade, where you can reference this selection in your next prompt.

<Frame style={{ border: 'none', background: 'none' }}>
  <img src="https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf-terminal-selection-mention.png?fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=0f8b76d17cdd96983010e88d9dadf265" data-og-width="744" width="744" data-og-height="144" height="144" data-path="assets/windsurf-terminal-selection-mention.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf-terminal-selection-mention.png?w=280&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=3123ae3c3b9d8fdc2a0ed5714554da0f 280w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf-terminal-selection-mention.png?w=560&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=8f51c119c9e38fb22de968c62be4deb0 560w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf-terminal-selection-mention.png?w=840&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=2e3dabb40323131b23575fceef294ff0 840w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf-terminal-selection-mention.png?w=1100&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=a4ebfaaa9b1ed7fcbba0c471731a8319 1100w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf-terminal-selection-mention.png?w=1650&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=1d236c51a624f3f307ab65a5088910f8 1650w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf-terminal-selection-mention.png?w=2500&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=26af2fd26f29c5a4d9f119c6d943314f 2500w" />
</Frame>


# @-mention your terminal

Chat with Cascade about your active terminals.

<Frame>
  <video autoPlay muted loop playsInline src="https://mintcdn.com/codeium/vRt4FQOyBeZpD2Pu/assets/terminal-at-mention.mp4?fit=max&auto=format&n=vRt4FQOyBeZpD2Pu&q=85&s=bf7766fe81e0847d7f58d4126980fe64" data-path="assets/terminal-at-mention.mp4" />
</Frame>


# Auto-executed Cascade commands

Cascade has the ability to run terminal commands on its own with user permission. However, certain terminal commands can be accepted or rejected automatically through the Allow and Deny lists.

By enabling Auto mode, it will rely on Cascade's judgement on whether the command requires the user's permission to be executed. This feature is only available for messages sent with premium models.

### Turbo Mode

In Turbo mode, Cascade will always execute the command, unless it is in the deny list.

You can toggle this via the Windsurf - Settings panel in the bottom right hand corner of the editor.

<Frame>
  <img style={{ maxHeight: "500px" }} src="https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/cascade-turbo-mode.png?fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=8860ea8311000ae2cc440cef26560620" data-og-width="680" width="680" data-og-height="60" height="60" data-path="assets/windsurf/cascade/cascade-turbo-mode.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/cascade-turbo-mode.png?w=280&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=dbcaa01fab58d7ba1fac05acc91ae12f 280w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/cascade-turbo-mode.png?w=560&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=c5dc736ca3cd591d00f0c8b3b4f13f90 560w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/cascade-turbo-mode.png?w=840&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=13ee4803cf3edcdaba2b9d76dcf109aa 840w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/cascade-turbo-mode.png?w=1100&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=389cfcb06aec368986869bfd15a42553 1100w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/cascade-turbo-mode.png?w=1650&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=e9829ad62b78b641213d472b4bca8683 1650w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/cascade-turbo-mode.png?w=2500&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=db556ad06ddff8c4fbe5186569bf8334 2500w" />
</Frame>

### Allow list

An allow list defines a set of terminal commands that will always auto-execute. For example, if you add `git`, then Cascade will always accept `git add -A`.

The setting can be via Command Palette → Open Settings (UI) → Search for `windsurf.cascadeCommandsAllowList`.

<Frame>
  <img style={{ maxHeight: "500px" }} src="https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/allow-list.png?fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=be27cab4ada44ba016f41cf7d943ae20" data-og-width="2098" width="2098" data-og-height="770" height="770" data-path="assets/windsurf/cascade/allow-list.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/allow-list.png?w=280&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=67d775a5a8dc5f74a9b1d743b265a9e1 280w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/allow-list.png?w=560&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=fc3414e119592d5e9f7499e5e4e95d59 560w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/allow-list.png?w=840&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=05dc8b80e975470b071eeefff32484e1 840w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/allow-list.png?w=1100&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=19be334d151ab04ea1c32f1732c0ed60 1100w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/allow-list.png?w=1650&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=7a16f9b1638e6a6b9cf4124460fdd308 1650w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/allow-list.png?w=2500&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=e347583986d3f7cd0e220b87494263c2 2500w" />
</Frame>

### Deny list

A deny list defines a set of terminal commands that will never auto-execute. For example, if you add `rm`, then Cascade will always ask for permission to run `rm index.py`.

The setting can be via Command Palette → Open Settings (UI) → Search for `windsurf.cascadeCommandsDenyList`.

<Frame>
  <img style={{ maxHeight: "500px" }} src="https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/deny-list.png?fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=83f5c447deeb931e68781fbd6cb89733" data-og-width="2090" width="2090" data-og-height="624" height="624" data-path="assets/windsurf/cascade/deny-list.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/deny-list.png?w=280&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=479a1b8b643adefbca8fcd08bbb2d4cd 280w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/deny-list.png?w=560&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=fb60fb1ea1f66c2cd63eb62ae0513675 560w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/deny-list.png?w=840&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=83520e9689fae159e121ccce1dc72901 840w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/deny-list.png?w=1100&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=a4832324125ef273f72d41f315a434ca 1100w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/deny-list.png?w=1650&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=28da77a6ed6fb67a2467df9bd95c7c90 1650w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/deny-list.png?w=2500&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=01bc9a72d11a63527867a908cdace643 2500w" />
</Frame>



# Vibe and Replace
Source: https://docs.windsurf.com/windsurf/vibe-and-replace



Vibe and Replace is an evolution of find and replace that allows you to search through your codebase for exact text matches and apply an AI prompt to each replacement.

Use this for more context-aware transformations and refactors.

<video autoPlay controls muted loop playsInline className="w-full aspect-video" src="https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/vibe-and-replace.mp4?fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=af192ccb94e21e78607f5a8b6884b580" data-path="assets/windsurf/vibe-and-replace.mp4" />

## Modes

Vibe and Replace can be used in two different modes:

1. `Smart` - utilizes a slower model that will apply changes more carefully

2. `Fast` - utilizes a faster model that will apply changes quickly

To set the mode, click on the `⌄` button next to the Vibe and Replace prompt box.




---

**Navigation:** [← Previous](./03-how-to-reset-or-change-your-enterprise-url.md) | [Index](./index.md) | Next →