**Navigation:** ← Previous | [Index](./index.md) | [Next →](./02-usage-billing.md)

---

# Vercel Documentation

Copy page

Ask AI about this page

Last updated November 7, 2025

Vercel is the AI Cloud for building and deploying modern web applications, from static sites to AI-powered agents.

## [Get started with Vercel](#get-started-with-vercel)

You can build and host many different types of applications on Vercel, static sites with your favorite [framework](/docs/frameworks), [multi-tenant](/docs/multi-tenant) applications, or [microfrontends](/docs/microfrontends), to [AI-powered agents](/guides/how-to-build-ai-agents-with-vercel-and-the-ai-sdk).

You can also use the [Vercel Marketplace](/docs/integrations) to find and install integrations such as AI providers, databases, CMSs, analytics, storage, and more.

When you are ready to build, connect your [Git repository](/docs/git) to deploy on every push, with [automatic preview environments](/docs/deployments/environments#preview-environment-pre-production) for testing changes before production.

See the [getting started guide](/docs/getting-started-with-vercel) for more information, or the [incremental migration guide](/docs/incremental-migration) for a step-by-step guide to migrating your existing application to Vercel.

## [Build your applications](#build-your-applications)

Use one or more of the following tools to build your application depending on your needs:

*   [Next.js](/docs/frameworks/nextjs): Build full-stack applications with Next.js, or any of our [supported frameworks](/docs/frameworks/more-frameworks)
*   [Functions](/docs/functions): API routes with [Fluid compute](/docs/fluid-compute), [active CPU, and provisioned memory](/docs/functions/usage-and-pricing), perfect for AI workloads
*   [Routing Middleware](/docs/routing-middleware): Customize your application's behavior with code that runs before a request is processed
*   [Incremental Static Regeneration](/docs/incremental-static-regeneration): Automatically regenerate your pages on a schedule or when a request is made
*   [Image Optimization](/docs/image-optimization): Optimize your images for the web
*   [Manage environments](/docs/deployments/environments): Local, preview, production, and custom environments
*   [Feature flags](/docs/feature-flags): Control the visibility of features in your application

## [Use Vercel's AI infrastructure](#use-vercel's-ai-infrastructure)

Add intelligence to your applications with Vercel's AI-first infrastructure:

*   : Iterate on ideas with Vercel's AI-powered development assistant
*   [AI SDK](/docs/ai-sdk): Integrate language models with streaming and tool calling
*   [AI Gateway](/docs/ai-gateway): Route to any AI provider with automatic failover
*   [Agents](/guides/how-to-build-ai-agents-with-vercel-and-the-ai-sdk): Build autonomous workflows and conversational interfaces
*   [MCP Servers](/docs/mcp): Create tools for AI agents to interact with your systems
*   [Sandbox](/docs/vercel-sandbox): Secure execution environments for untrusted code
*   [Claim deployments](/docs/deployments/claim-deployments): Allow AI agents to deploy a project and let a human take over

## [Collaborate with your team](#collaborate-with-your-team)

Collaborate with your team using the following tools:

*   [Toolbar](/docs/vercel-toolbar): An in-browser toolbar that lets you leave feedback, manage feature flags, preview drafts, edit content live, inspect [performance](/docs/vercel-toolbar/interaction-timing-tool)/[layout](/docs/vercel-toolbar/layout-shift-tool)/[accessibility](/docs/vercel-toolbar/accessibility-audit-tool), and navigate/share deployment pages
*   [Comments](/docs/comments): Let teams and invited collaborators comment on your preview deployments and production environments
*   [Draft mode](/docs/draft-mode): View your unpublished headless CMS content on your site

## [Secure your applications](#secure-your-applications)

Secure your applications with the following tools:

*   [Deployment Protection](/docs/deployment-protection): Protect your applications from unauthorized access
*   [RBAC](/docs/rbac): Role-based access control for your applications
*   [Configurable WAF](/docs/vercel-firewall/vercel-waf): Customizable rules to protect against attacks, scrapers, and unwanted traffic
*   [Bot Management](/docs/bot-management): Protect your applications from bots and automated traffic
*   [BotID](/docs/botid): An invisible CAPTCHA that protects against sophisticated bots without showing visible challenges or requiring manual intervention
*   [AI bot filtering](/docs/bot-management#ai-bots-managed-ruleset): Control traffic from AI bots
*   [Platform DDoS Mitigation](/docs/security/ddos-mitigation): Protect your applications from DDoS attacks

## [Deploy and scale](#deploy-and-scale)

Vercel handles infrastructure automatically based on your framework and code, and provides the following tools to help you deploy and scale your applications:

*   [Vercel Delivery Network](/docs/cdn): Fast, globally distributed execution
*   [Rolling Releases](/docs/rolling-releases): Roll out new deployments in increments
*   [Rollback deployments](/docs/instant-rollback): Roll back to a previous deployment, for swift recovery from production incidents, like breaking changes or bugs
*   [Observability suite](/docs/observability): Monitor performance and debug your AI workflows and apps

--------------------------------------------------------------------------------
title: "Account Management"
description: "Learn how to manage your Vercel account and team members."
last_updated: "null"
source: "https://vercel.com/docs/accounts"
--------------------------------------------------------------------------------

# Account Management

Copy page

Ask AI about this page

Last updated October 30, 2025

When you first sign up for Vercel, you'll create an account. This account is used to manage your Vercel resources. Vercel has three types of plans:

*   [Hobby](/docs/plans/hobby)
*   [Pro](/docs/plans/pro)
*   [Enterprise](/docs/plans/enterprise)

Each plan offers different features and resources, allowing you to choose the right plan for your needs.

When signing up for Vercel, you can choose to sign up with an email address or a Git provider.

## [Sign up with email](#sign-up-with-email)

To sign up with email:

1.  Enter your email address to receive the six-digit one-time password (OTP)
2.  Enter the OTP to proceed with logging in successfully.

When signing up with your email, no Git provider will be connected by default. See [login methods and connections](#login-methods-and-connections) for information on how to connect a Git provider. If no Git provider is connected, you will be asked to verify your account on every login attempt.

## [Sign up with a Git provider](#sign-up-with-a-git-provider)

You can sign up with any of the following supported Git providers:

*   [GitHub](/docs/git/vercel-for-github)
*   [GitLab](/docs/git/vercel-for-gitlab)
*   [Bitbucket](/docs/git/vercel-for-bitbucket)

Authorize Vercel to access your Git provider account. This will be the default login connection on your account.

Once signed up you can manage your login connections in the [authentication section](/account/authentication) of your dashboard.

## [Login methods and connections](#login-methods-and-connections)

You can manage your login connections in the Authentication section of [your account settings](/account/authentication). To find this section:

1.  Select your profile picture near the top-right of the dashboard
2.  Select Settings in the dropdown that appears
3.  Select Authentication in the list near the left side of the page

![The Authentication section of your account settings.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Faccounts%2Fauthentication-page-light.png&w=1920&q=75)![The Authentication section of your account settings.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Faccounts%2Fauthentication-page-dark.png&w=1920&q=75)

The Authentication section of your account settings.

### [Login with passkeys](#login-with-passkeys)

Passkeys allow you to log into your Vercel account using biometrics such as face or fingerprint recognition, PINs, hardware security keys, and more.

To add a new passkey:

1.  From the dashboard, click your account avatar and select Settings. In your [account settings](/account/authentication), go to the Authentication item
2.  Under Add New, select the Passkey button and then click Continue
3.  Select the authenticator of preference. This list depends on your browser and your eligible devices. By default, Vercel will default to a password manager if you have one installed on your browser and will automatically prompt you to save the passkey
4.  Follow the instructions on the device or with the account you've chosen as an authenticator

When you're done, the passkey will appear in a list of login methods on the Authentication page, alongside your other connections.

### [Logging in with SAML Single Sign-On](#logging-in-with-saml-single-sign-on)

SAML Single Sign-On enables you to log into your Vercel team with your organization's identity provider which manages your credentials.

SAML Single Sign-On is available to Enterprise teams, or Pro teams can purchase it as a paid add-on from their [Billing settings](https://vercel.com/d?to=%2F%5Bteam%5D%2F%7E%2Fsettings%2Fbilling%23paid-add-ons). The feature can be configured by team Owners from the team's Security & Privacy settings.

### [Choosing a connection when creating a project](#choosing-a-connection-when-creating-a-project)

When you create an account on Vercel, you will be prompted to create a project by either importing a Git repository or using a template.

Either way, you must connect a Git provider to your account, which you'll be able to use as a login method in the future.

### [Using an existing login connection](#using-an-existing-login-connection)

Your Hobby team on Vercel can have only one login connection per third-party service. For example, you can only log into your Hobby team with a single GitHub account.

For multiple logins from the same service, create a new Vercel Hobby team.

## [Teams](#teams)

Teams on Vercel let you collaborate with other members on projects and access additional resources.

### [Creating a team](#creating-a-team)

DashboardcURLSDK

1.  Click on the scope selector at the top left of the nav bar
2.  Choose to create a new team
3.  Name your team
4.  Depending on the types of team plans that you have already created, you'll be able to select a team plan option:

![Selecting a team plan.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fteams%2Fnew-team-light.png&w=1080&q=75)![Selecting a team plan.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fteams%2Fnew-team-dark.png&w=1080&q=75)

Selecting a team plan.

To create an Authorization Bearer token, see the [access token](/docs/rest-api/reference/welcome#creating-an-access-token) section of the API documentation.

cURL

```
curl --request POST \
  --url https://api.vercel.com/v1/teams \
  --header "Authorization: Bearer $VERCEL_TOKEN" \
  --header "Content-Type: application/json" \
  --data '{
  "slug": "<team-slug>",
  "name": "<team-name>"
}'
```

To create an Authorization Bearer token, see the [access token](/docs/rest-api/reference/welcome#creating-an-access-token) section of the API documentation.

createTeam

```
import { Vercel } from '@vercel/sdk';
 
const vercel = new Vercel({
  bearerToken: '<YOUR_BEARER_TOKEN_HERE>',
});
 
async function run() {
  const result = await vercel.teams.createTeam({
    slug: 'team-slug',
    name: 'team-name',
  });
 
  // Handle the result
  console.log(result);
}
 
run();
```

Collaborating with other members on projects is available on the [Pro](/docs/plans/pro) and [Enterprise](/docs/plans/enterprise) plans.

Upgrade from the [Hobby](/docs/plans/hobby) plan to [Pro](/docs/plans/hobby#upgrading-to-pro) to add team members.

### Experience Vercel Pro for free

Unlock the full potential of Vercel Pro during your 14-day trial with $20 in credits. Benefit from 1 TB Fast Data Transfer, 10,000,000 Edge Requests, up to 200 hours of Build Execution, and access to Pro features like team collaboration and enhanced analytics.

[Start your free Pro trial](/upgrade/docs-trial-button)

After [creating a new trial](/docs/plans/pro-plan/trials), you'll have 14 days of Pro premium features and collaboration for free.

### [Team membership](#team-membership)

You can join a Vercel team through an invitation from a [team owner](/docs/rbac/access-roles#owner-role), automatic addition by a team's [identity provider](/docs/saml), or by requesting access yourself. To request access, you can push a commit to a private Git repository owned by the team.

### [Leaving a team](#leaving-a-team)

You can't leave a team if you are the last remaining [owner](/docs/rbac/access-roles#owner-role) or the last confirmed [member](/docs/rbac/access-roles#member-role).

To leave a team:

1.  If there isn't another owner for your team, you must assign a different confirmed member as the team owner
2.  Go to your team's dashboard and select the Settings tab
3.  Scroll to the Leave Team section and select the Leave Team button
4.  Click Confirm
5.  If you are the only remaining member, you should delete the team instead

### [Deleting a team](#deleting-a-team)

To delete a team:

1.  Remove all team domains
2.  Go to your team's dashboard and select the Settings tab
3.  Scroll to the Delete Team section and select the Delete Team button
4.  Click Confirm

If you'd prefer to cease payment instead of deleting your team, you can [downgrade to Hobby](/docs/plans/pro#downgrading-to-hobby).

### [Default team](#default-team)

Your default team will be used when you make a request through the [API](/docs/rest-api) or [CLI](/docs/cli) and don’t specify a specific team. It will also be the team shown whenever you first log in to Vercel or navigate to `/dashboard`. The first Hobby or Pro team you create will automatically be nominated as the default team.

#### [How to change your default team](#how-to-change-your-default-team)

If you delete, leave, or are removed from your default team, Vercel will automatically choose a new default team for you. However, you may want to choose a default team yourself. To do that:

1.  Navigate to [vercel.com/account/settings](https://vercel.com/account/settings)
2.  Under Default Team, select your new default team from the dropdown
3.  Press Save

### [Find your team ID](#find-your-team-id)

Your Team ID is a unique and unchangeable identifier that's automatically assigned when your team is created.

There are a couple of methods you can use to locate your Team ID:

*   Vercel API: Use the [Vercel API](/docs/rest-api/reference/endpoints/teams/list-all-teams) to retrieve your Team ID
*   Dashboard: Find your Team ID directly from your team's Dashboard on Vercel:
    *   Navigate to the following URL, replacing `your_team_name_here` with your actual team's name: `https://vercel.com/teams/your_team_name_here/settings#team-id`. If you're unable to locate your Team ID using the URL method, follow these steps:
    *   Open your team's dashboard and head over to the Settings tab
    *   Choose General from the left-hand navigation
    *   Scroll down to the Team ID section and your Team ID will be there ready for you to copy

## [Managing emails](#managing-emails)

To access your email settings from the dashboard:

1.  Select your avatar in the top right corner of the [dashboard](/dashboard).
2.  Select Account Settings from the list.
3.  Select the Settings tab and scroll down to the Emails section.
4.  You can then [add](/docs/accounts#adding-a-new-email-address), [remove](/docs/accounts#removing-an-email-address), or [change](/docs/accounts#changing-your-primary-email-address) the primary email address associated with your account.

## [Adding a new email address](#adding-a-new-email-address)

To add a new email address

1.  Follow the steps above and select the Add Another button in the Emails section of your account settings.
2.  Once you have added the new email address, Vercel will send an email with a verification link to the newly added email. Follow the link in the email to verify your new email address.
3.  Once verified, all email addresses can be used to log in to your account, including your primary email address.

You can add up to three emails per account, with a single email domain shared by two emails at most.

![Your account email addresses.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Faccounts%2Faccount-emails-2-light.png&w=1920&q=75)![Your account email addresses.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Faccounts%2Faccount-emails-2-dark.png&w=1920&q=75)

Your account email addresses.

## [Changing your primary email address](#changing-your-primary-email-address)

Your primary email address is the email address that will be used to send you notifications, such as when you receive a new [preview comment](/docs/comments) or when you are [invited to a team](/docs/rbac/managing-team-members#invite-link).

Once you have added and verified a new email address, you can change your primary email address by selecting Set as Primary in the dot menu.

![Setting your primary email address.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Faccounts%2Faccount-emails-set-primary-2-light.png&w=1920&q=75)![Setting your primary email address.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Faccounts%2Faccount-emails-set-primary-2-dark.png&w=1920&q=75)

Setting your primary email address.

## [Removing an email address](#removing-an-email-address)

To remove an email address select the Delete button in the dot menu.

If you wish to remove your primary email address, you will need to set a new primary email address first.

--------------------------------------------------------------------------------
title: "Using the Activity Log"
description: "Learn how to use the Activity Log, which provides a list of all events on a Hobby team or team, chronologically organized since its creation."
last_updated: "null"
source: "https://vercel.com/docs/activity-log"
--------------------------------------------------------------------------------

# Using the Activity Log

Copy page

Ask AI about this page

Last updated September 24, 2025

Activity Log is available on [all plans](/docs/plans)

The [Activity Log](/dashboard/activity) provides a list of all events on a Hobby team or team, chronologically organized since its creation. These events include:

*   User(s) involved with the event
*   Type of event performed
*   Type of account
*   Time of the event (hover over the time to reveal the exact timestamp)

Vercel does not emit any logs to third-party services. The Activity Log is only available to the account owner and team members.

![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fobservability%2Factivity-logs-light.png&w=3840&q=75)![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fobservability%2Factivity-logs-dark.png&w=3840&q=75)

Example events list on the **Activity** page.

## [When to use the Activity log](#when-to-use-the-activity-log)

Common use cases for viewing the Activity log include:

*   If a user was removed or deleted by mistake, use the list to find when the event happened and who requested it
*   A domain can be disconnected from your deployment. Use the list to see if a domain related event was recently triggered
*   Check if a specific user was removed from a team

## [Events logged](#events-logged)

The table below shows a list of events logged on the Activity page.

Active

Deprecated

Replaced

Types of events logged.
| 
Event Type

 | 

Description

 |
| --- | --- |
| access-group-created | A user created an access group. |
| access-group-deleted | A user deleted an access group. |
| access-group-project-updated | A project was changed in an access group. |
| access-group-user-added | A user was added to an access group. |
| access-group-user-removed | A user was removed from an access group. |
| alias | An alias was assigned. |
| alias-invite-created | An invite was sent for an alias. |
| alias-invite-joined | A user joined an alias they were given access to. |
| alias-invite-revoked | An invite was revoked for an alias. |
| alias-protection-bypass-created | A shareable link was created for an alias. |
| alias-protection-bypass-exception | A Deployment Protection Exception was updated for an alias. |
| alias-protection-bypass-regenerated | A shareable link was regenerated for an alias. |
| alias-protection-bypass-revoked | A shareable link was revoked for an alias. |
| alias-user-scoped-access-denied | A user's access request for an alias was denied. |
| alias-user-scoped-access-granted | A user's access request for an alias was granted. |
| alias-user-scoped-access-requested | A user requested access to an alias. |
| alias-user-scoped-access-revoked | A user's access for an alias was revoked. |
| auto-expose-system-envs | Automatically exposing System Environment Variables for the project. |
| avatar | An avatar was created for the profile of a personal account. |
| cert | An SSL certificate was created for a custom domain in a personal account or team. |
| cert-delete | An SSL certificate connected to a custom domain was deleted. |
| connect-bitbucket | A BitBucket account was connected to a personal. |
| connect-github | A GitHub account was connected to a personal. |
| connect-gitlab | A GitLab account was connected to a personal. |
| deploy-hook-deduped | If a deploy hook triggers a deployment for a commit that already triggered a deployment via Git, then the deployment from the deploy hook is stopped. This action is reported with the deploy-hook-deduped event. |
| deploy-hook-processed | A deployment was successfully triggered by a specific deploy hook. |
| deployment | A deployment was created for a project. |
| deployment-creation-blocked | A deployment was blocked because the Git user is not part of the team. |
| deployment-delete | A specific deployment was deleted. |
| disabled-integration-installation-removed | A disabled integration was automatically uninstalled |
| dns-add | A DNS record was added to the personal account or team domain records for a specific domain. |
| dns-delete | A DNS record was deleted from the personal account or team domain records for a specific domain. |
| dns-update | A DNS record was updated in the personal account or team domain records for a specific domain. |
| domain | A domain connection was created in a personal account or team. |
| domain-buy | A domain was successfully purchased in a personal account or team. |
| domain-delegated | A domain was successfully delegated to another personal account or team so it can also be used there. |
| domain-delete | A domain was removed from a personal account or team. |
| domain-move-in | A domain was moved in from another personal account or team to the current personal account or team. |
| domain-move-out | A domain was moved out from the current personal account or team to another personal account or team. |
| domain-move-out-request-sent | The request to move a domain from the current personal account or team to another personal account or team was sent. |
| domain-renew-change | A domain hosted with Vercel was renewed. |
| domain-transfer-in | A domain was transferred from an external provider to Vercel. |
| drain-created | A drain was created. |
| drain-deleted | A drain was deleted. |
| drain-disabled | A drain was disabled. |
| drain-enabled | A drain was enabled. |
| drain-updated | A drain was updated. |
| edge-cache-purge-all | The edge cache was purged. |
| edge-cache-rollback-purge | The edge cache purge was rolled back. |
| edge-config-created | An Edge Config was created. |
| edge-config-deleted | An Edge Config was deleted. |
| edge-config-items-updated | The values in an Edge Config were updated. |
| edge-config-token-created | An access token for an Edge Config was created. |
| edge-config-token-deleted | An access token for an Edge Config was deleted. |
| edge-config-updated | An Edge Config was updated. |
| email | The email of the current user was updated. |
| env-variable-add | An automatically encrypted environment variable was added to a project. |
| env-variable-delete | An existing environment variable was deleted from a project. |
| env-variable-edit | An existing environment variable in a project was updated. |
| env-variable-read | The plain text value of an encrypted environment variable was read. |
| firewall-bypass-created | A bypass of system firewall rules was created |
| firewall-bypass-deleted | A bypass of system firewall rules was deleted |
| flags-explorer-subscription | The Flags Explorer subscription was updated. |
| hipaa-baa-subscription | The HIPAA BAA subscription was updated. |
| instant-rollback-created | An instant rollback was created. |
| integration-configuration-scope-change-confirmed | The permissions upgrade request from an installed integration was confirmed. |
| integration-configurations-disabled | One or more integrations were disabled because their owner has left the team |
| integration-installation-completed | An integration was installed in one or all projects under a personal account or team. |
| integration-installation-permission-updated | The permissions for an installed integration was updated. |
| integration-installation-removed | An integration was removed from a project or personal account or team. |
| integration-scope-changed | The scopes for an integration were changed. |
| log-drain-created | A log drain was created. |
| log-drain-deleted | A log drain was deleted. |
| log-drain-disabled | A log drain was disabled. |
| log-drain-enabled | A log drain was enabled. |
| login | A user logged in at a specific time with a login method. |
| manual-deployment-promotion-created | A deployment was manually promoted to production. |
| microfrontend-group-added | A new microfrontend group was created |
| microfrontend-group-deleted | A microfrontend group was deleted |
| microfrontend-group-updated | A microfrontend group was updated |
| microfrontend-project-added-to-group | A project was added to a microfrontend group |
| microfrontend-project-removed-from-group | A project was removed from a microfrontend group |
| microfrontend-project-updated | A project's microfrontend settings were updated |
| monitoring-disabled | Monitoring was disabled for the team |
| monitoring-enabled | Monitoring was enabled for the team. |
| oauth-app-connection-created | A user authorized an app. |
| oauth-app-connection-removed | A user removed an app authorization. |
| oauth-app-connection-updated | A user updated an app authorization. |
| observability-disabled | Observability Plus was disabled for the team. |
| observability-enabled | Observability Plus was enabled for the team. |
| passkey-created | A new passkey was created. |
| passkey-deleted | An existing passkey was deleted. |
| passkey-updated | The name of the existing passkey was updated. |
| password-protection-disabled | Advanced Deployment Protection was disabled for the team. |
| password-protection-enabled | Advanced Deployment Protection was enabled for the team. |
| plan | A payment plan (hobby, pro or enterprise) was added to a personal account. |
| preview-deployment-suffix-disabled | The preview deployment suffix for a team was disabled. |
| preview-deployment-suffix-enabled | The preview deployment suffix for a team was enabled. |
| preview-deployment-suffix-update | The preview deployment suffix for a team was updated. |
| production-branch-updated | The production branch for a project was updated. |
| project-analytics-disabled | Legacy Speed Insights was disabled for a specific project. |
| project-analytics-enabled | Legacy Speed Insights was enabled for a specific project. |
| project-automation-bypass | Protection Bypass for Automation for a project was modified. |
| project-created | A new project was created. |
| project-delete | A specific project was deleted. |
| project-domain-unverified | The ownership of a domain added to Vercel became unverified. |
| project-domain-verified | The project domain ownership was verified. |
| project-functions-fluid-disabled | Fluid compute was disabled for a specific project. |
| project-functions-fluid-enabled | Fluid compute was enabled for a specific project. |
| project-member-added | A user was added to a project. |
| project-member-invited | A user was invited to a project. |
| project-member-removed | A user was removed from a project. |
| project-member-updated | A user was updated in a project. |
| project-move-in-success | The transfer of a project to the current personal account or team succeeded. |
| project-move-out-failed | The transfer of a project from the current personal account or team failed. |
| project-move-out-started | The transfer of a project from the current personal account or team was initiated. |
| project-move-out-success | The transfer of a project from the current personal account or team succeeded. |
| project-options-allowlist | OPTIONS Allowlist was modified. |
| project-password-protection | Password Protection for a project was modified. |
| project-paused | The project's production deployment was paused. |
| project-rolling-release-aborted | A production canary rollout was aborted for a project. |
| project-rolling-release-approved | Advancing to the next stage of a production canary rollout was approved for a project. |
| project-rolling-release-completed | A production canary rollout was completed for a project. |
| project-rolling-release-configured | The rolling release configuration was updated for a project. |
| project-rolling-release-disabled | Rolling releases were disabled for a project. |
| project-rolling-release-enabled | Rolling releases were enabled for a project. |
| project-rolling-release-started | A production canary rollout was started for a project. |
| project-rolling-release-timer | A production canary rollout was automatically advanced to the next stage for a project. |
| project-speed-insights-disabled | Speed Insights was disabled for a specific project. |
| project-speed-insights-enabled | Speed Insights was enabled for a specific project. |
| project-sso-protection | Vercel Authentication (formerly SSO protection) for a project was modified. |
| project-static-ips-updated | A project's Static IPs configuration was updated. |
| project-trusted-ips | Trusted IPs for a project was modified. |
| project-unpaused | The project's production deployment was resumed. |
| project-web-analytics-disabled | Web Analytics was disabled for a project. |
| project-web-analytics-enabled | Web Analytics was enabled for a project. |
| secondary-email-added | An email was added to the account |
| secondary-email-removed | An email was removed from the account |
| secondary-email-verified | An email was verified |
| secret-add | An encrypted environment variable was added to a project. (Only possible through the API and CLI) |
| secret-delete | An encrypted environment variable was deleted from a project. (Only possible through the API and CLI) |
| secret-rename | An encrypted environment variable was renamed in a project. (Only possible through the API and CLI) |
| set-name | The full name on the personal account was set. |
| shared-env-variable-create | An automatically encrypted shared environment variable was created. |
| shared-env-variable-delete | An existing shared environment variable was deleted. |
| shared-env-variable-read | The plain text value of an encrypted shared environment variable was read. |
| shared-env-variable-update | An existing shared environment variable was updated. |
| spend-created | A spend management budget was added. |
| spend-deleted | A spend management budget was deleted. |
| spend-updated | A spend management budget was updated. |
| storage-accept-tos | Acceptance of storage terms of service |
| storage-accessed-data-browser | Made a query to the store from the Data tab |
| storage-connect-project | A store was connected to a project |
| storage-create | A new store was created |
| storage-delete | A store was deleted |
| storage-disconnect-project | A store was disconnected to a project |
| storage-inactive-store-deleted | An inactive store was deleted |
| storage-reset-credentials | The credentials for a store were reset |
| storage-update | A store was updated |
| storage-view-secret | Viewed a secret for a store |
| team | A team was created in a personal account. |
| team-avatar-update | The avatar of a specific team was updated. |
| team-delete | A specific team was deleted. |
| team-member-add | A member was added to a specific team. |
| team-member-confirm-request | The request for a user to join a team was confirmed. |
| team-member-decline-request | The request for a user to join a team was declined. |
| team-member-delete | A specific team member was deleted from a team. |
| team-member-entitlement-added | A team member was added to an entitlement. |
| team-member-entitlement-canceled | A team member entitlement was canceled and set not to renew. |
| team-member-entitlement-reactivated | A team member had an entitlement reactivated. |
| team-member-entitlement-removed | A team member was removed from an entitlement. |
| team-member-join | A team member joined the current team. |
| team-member-leave | A team member left the current team. |
| team-member-request-access | A user requested access to join a team. |
| team-member-role-update | The role of a specific team member was updated. |
| team-name-update | The name of a team was updated. |
| team-remote-caching-update | The Remote Caching status was changed. |
| team-slug-update | The slug of a team was updated. |
| user-mfa-challenge-verified | A two-factor challenge was verified |
| user-mfa-configuration-updated | Two-factor configuration was updated |
| user-mfa-recovery-codes-regenerated | Two-factor recovery codes were regenerated |
| user-mfa-totp-verified | A Two-factor authenticator app was added |
| user-primary-email-updated | The primary email was changed |
| username | The username of a personal account was updated. |
| web-analytics-tier-updated | The Web Analytics subscription tier was changed. |

--------------------------------------------------------------------------------
title: "Vercel Agent"
description: "AI-powered development tools that speed up your workflow and help resolve issues faster"
last_updated: "null"
source: "https://vercel.com/docs/agent"
--------------------------------------------------------------------------------

# Vercel Agent

Copy page

Ask AI about this page

Last updated October 28, 2025

Vercel Agent is available in [Beta](/docs/release-phases#beta) on [Enterprise](/docs/plans/enterprise) and [Pro](/docs/plans/pro) plans

Vercel Agent is a suite of AI-powered development tools built to speed up your workflow. Instead of spending hours debugging production issues or waiting for code reviews, Agent helps you catch problems faster and resolve incidents quickly.

Agent works because it already understands your application. Vercel builds your code, deploys your functions, and serves your traffic. Agent uses this deep context about your codebase, deployment history, and runtime behavior to provide intelligent assistance right where you need it.

Everything runs on [Vercel's AI Cloud](https://vercel.com/ai), infrastructure designed specifically for AI workloads. This means Agent can use secure sandboxes to reproduce issues, access the latest models, and provide reliable results you can trust.

## [Features](#features)

### [Code Review](#code-review)

Get automatic code reviews on every pull request. Code Review analyzes your changes, identifies potential issues, and suggests fixes you can apply directly.

What it does:

*   Performs multi-step reasoning to identify security vulnerabilities, logic errors, and performance issues
*   Generates patches and runs them in secure sandboxes with your real builds, tests, and linters
*   Only suggests fixes that pass validation checks, allowing you to apply specific code changes with one click

Learn more in the [Code Review docs](/docs/agent/pr-review).

### [Investigation](#investigation)

When error alerts fire, Vercel Agent Investigations can analyze what's happening to help you debug faster. Instead of manually digging through logs and metrics, AI does the analysis and shows you what might be causing the issue.

What it does:

*   Queries logs and metrics around the time of the alert
*   Looks for patterns and correlations that might explain the problem
*   Provides insights about potential root causes

Learn more in the [Agent Investigation docs](/docs/agent/investigation).

## [Getting started](#getting-started)

You can enable Vercel Agent in the [Agent tab](https://vercel.com/d?to=%2F%5Bteam%5D%2F%7E%2Fvercel-agent&title=Open+Vercel+Agent) of your dashboard. Setup varies by feature:

*   Code Review: You'll need to configure which repositories to review and whether to review draft PRs. See [Code Review setup](/docs/agent/pr-review#how-to-set-up-code-review) for details.
*   Agent Investigation: This requires [Observability Plus](/docs/observability/observability-plus) and in order to run investigations automatically, you'll need to enable Vercel Agent Investigations. See [Investigation setup](/docs/agent/investigation#how-to-enable-agent-investigation) to get started.

## [Pricing](#pricing)

Vercel Agent uses a credit-based system. Each review or investigation costs a fixed $0.30 USD plus token costs billed at the Agent's underlying AI provider's rate, with no additional markup. Pro teams can redeem a $100 USD promotional credit when enabling Agent.

You can [purchase credits and enable auto-reload](/docs/agent/pricing#adding-credits) in the Agent tab of your dashboard. For complete pricing details, credit management, and cost tracking information, see [Vercel Agent Pricing](/docs/agent/pricing).

## [Privacy](#privacy)

Vercel Agent doesn't store or train on your data. It only uses LLMs from providers on our [subprocessor list](https://security.vercel.com/?itemUid=e3fae2ca-94a9-416b-b577-5c90e382df57&source=click), and we have agreements in place that don't allow them to train on your data.

--------------------------------------------------------------------------------
title: "Build with AI agents on Vercel"
description: "Install AI agents and services through the Vercel Marketplace to automate workflows and build custom AI systems."
last_updated: "null"
source: "https://vercel.com/docs/agent-integrations"
--------------------------------------------------------------------------------

# Build with AI agents on Vercel

Copy page

Ask AI about this page

Last updated October 23, 2025

Integrating AI agents in your application often means working with separate dashboards, billing systems, and authentication flows for each agent you want to use. This can be time-consuming and frustrating.

With [AI agents](#ai-agents) and [AI agent services](#ai-agent-services) on the Vercel Marketplace, you can add AI-powered workflows to your projects through [native integrations](/docs/integrations#native-integrations) and get a unified dashboard with billing, observability, and installation flows.

You have access to two types of AI building blocks:

*   [Agents](#ai-agents): Pre-built systems that handle specialized workflows on your behalf
*   [Services](#ai-agent-services): Infrastructure you use to build and run your own agents

## [Getting started](#getting-started)

To add an agent or service to your project:

1.  Go to the [AI agents and services section](https://vercel.com/marketplace/category/agents) of the Vercel Marketplace and select the agent or service you want to add.
    
2.  Review the details and click Install.
    
3.  If you selected an agent that needs GitHub access for tasks like code reviews, you'll be prompted to select a Git namespace.
    
4.  Choose an Installation Plan from the available options.
    
5.  Click Continue.
    
6.  On the configuration page, update the Resource Name, review your selections, and click Create.
    
7.  Click Done once the installation is complete.
    

You'll be taken to the installation detail page where you can complete the onboarding process to connect your project with the agent or service.

### [Providers](#providers)

If you're building agents or AI infrastructure, check out [Integrate with Vercel](/docs/integrations/create-integration) to learn how to create a native integration. When you're ready to proceed, submit a [request to join](https://vercel.com/marketplace-providers#become-a-provider) the Vercel Marketplace.

## [AI agents](#ai-agents)

Agents are pre-built systems that reason, act, and adapt inside your existing workflows, like CodeRabbit, Corridor, and Sourcery. For example, instead of building code review automation from scratch, you install an agent that operates where your applications already run.

Each agent integrates with GitHub through a single onboarding flow. Once installed, the agent begins monitoring your repositories and acting on changes according to its specialization.

## [AI agent services](#ai-agent-services)

Services give you the foundation to create, customize, monitor, and scale your own agents, including Braintrust, Kubiks, Autonoma, Chatbase, Kernel, and BrowserUse.

These services plug into your Vercel workflows so you can build agents specific to your company, products, and customers. They'll integrate with your CI/CD, observability, or automation workflows on Vercel.

## [More resources](#more-resources)

*   [AI agents and services on the Vercel Marketplace](https://vercel.com/marketplace/category/agents)
*   [Learn how to add and manage a native integration](/docs/integrations/install-an-integration/product-integration)
*   [Learn how to create a native integration](/docs/integrations/create-integration/marketplace-product)

--------------------------------------------------------------------------------
title: "Vercel Agent Investigation"
description: "Let AI investigate your error alerts to help you debug faster"
last_updated: "null"
source: "https://vercel.com/docs/agent/investigation"
--------------------------------------------------------------------------------

# Vercel Agent Investigation

Copy page

Ask AI about this page

Last updated October 28, 2025

Agent Investigation is available in [Beta](/docs/release-phases#beta) on [Enterprise](/docs/plans/enterprise) and [Pro](/docs/plans/pro) plans with [Observability Plus](/docs/observability/observability-plus)

When you get an error alert, Vercel Agent can investigate what's happening in your logs and metrics to help you figure out the root cause. Instead of manually digging through data, AI will do the detective work and display highlights of the anomaly in the Vercel dashboard.

Investigations happen automatically when an error alert fires. The AI digs into patterns in your data, checks what changed, and gives you insights about what might be causing the issue.

## [Getting started with Agent Investigation](#getting-started-with-agent-investigation)

You'll need two things before you can use Agent Investigation:

1.  An [Observability Plus](/docs/observability/observability-plus) subscription
2.  [Sufficient credits](/docs/agent/pricing) to cover the cost of an investigation

To allow investigations to run automatically for every error alert, you should [enable Vercel Agent Investigations](#enable-agent-investigations) for your team.

You can [run an investigation manually](#run-an-investigation-manually) if you want to investigate an alert that has already fired.

Agent Investigation will not automatically start running if you had previously only enabled Vercel Agent for code review. You will need to [enable Agent Investigations](#enable-agent-investigations) separately.

### [Enable Agent Investigations](#enable-agent-investigations)

To run investigations automatically for every error alert, enable Vercel Agent Investigations in your team's settings:

1.  Go to your team's [Settings](https://vercel.com/d?to=%2Fteams%2F%5Bteam%5D%2Fsettings&title=Go+to+Settings&personalTo=%2Faccount) page.
2.  In the General section, find Vercel Agent and under Investigations, switch the toggle to Enabled.
3.  Select Save to confirm your changes.

Once enabled, investigations will run automatically when an error alert fires, provided you have sufficient credits. You'll need to make sure your team has [enough credits](/docs/agent/pricing#adding-credits) to cover the cost of investigations.

## [How to use Agent Investigation](#how-to-use-agent-investigation)

When [Agent Investigations are enabled](#enable-agent-investigations), they run automatically when an error alert fires. The AI queries your logs and metrics around the time of the alert, looks for patterns that might explain the issue, checks for related errors or anomalies, and provides insights about what it found.

To view an investigation:

1.  Go to your [Vercel dashboard](https://vercel.com/d?to=%2F%5Bteam%5D%2F%7E%2Fobservability%2Falerts&title=Open+Alerts) and navigate to Observability, then Alerts.
2.  Find the alert you want to review and click on it.
3.  The investigation results will appear alongside your alert details. You'll see the analysis stream in real time if the investigation is still running.

If you want to run the investigation again with fresh data, click the Rerun button.

### [Run an investigation manually](#run-an-investigation-manually)

If you do not have Agent Investigations enabled and running automatically, you can run an investigation manually from the alert details page.

1.  Go to your [Vercel dashboard](https://vercel.com/d?to=%2F%5Bteam%5D%2F%7E%2Fobservability%2Falerts&title=Open+Alerts) and navigate to Observability, then Alerts.
2.  Find the alert you want to review and click on it.
3.  Click the Investigate (or Rerun) button to run an investigation manually.

## [Pricing](#pricing)

Agent Investigation uses a credit-based system. Each investigation costs a fixed $0.30 USD plus token costs billed at the Agent's underlying AI provider's rate, with no additional markup. The token cost varies based on how much data the AI needs to analyze from your logs and metrics.

Pro teams can redeem a $100 USD promotional credit when enabling Agent. You can [purchase credits and enable auto-reload](/docs/agent/pricing#adding-credits) in the Agent tab of your dashboard. For complete pricing details, credit management, and cost tracking information, see [Vercel Agent Pricing](/docs/agent/pricing).

## [Disable Agent Investigation](#disable-agent-investigation)

To disable Agent Investigation:

1.  Go to the your team's [Settings](https://vercel.com/d?to=%2Fteams%2F%5Bteam%5D%2Fsettings&title=Go+to+Settings&personalTo=%2Faccount) page.
2.  In the General section, find Vercel Agent and under Investigations, switch the toggle to Disabled.
3.  Select Save to confirm your changes.

Once disabled, Agent Investigation won't run automatically on any new alerts. You can re-enable Agent Investigation at any time from the same menu or [run an investigation manually](#run-an-investigation-manually) from the alert details page.

--------------------------------------------------------------------------------
title: "Vercel Agent Code Review"
description: "Get automatic AI-powered code reviews on your pull requests"
last_updated: "null"
source: "https://vercel.com/docs/agent/pr-review"
--------------------------------------------------------------------------------

# Vercel Agent Code Review

Copy page

Ask AI about this page

Last updated October 28, 2025

Vercel Agent Code Review is available in [Beta](/docs/release-phases#beta) on [Enterprise](/docs/plans/enterprise) and [Pro](/docs/plans/pro) plans

AI Code Review is part of [Vercel Agent](/docs/agent), a suite of AI-powered development tools. When you open a pull request, it automatically analyzes your changes using multi-step reasoning to catch security vulnerabilities, logic errors, and performance issues.

It generates patches and runs them in [secure sandboxes](/docs/vercel-sandbox) with your real builds, tests, and linters to validate fixes before suggesting them. Only validated suggestions that pass these checks appear in your PR, allowing you to apply specific code changes with one click.

## [How to set up Code Review](#how-to-set-up-code-review)

To enable code reviews for your [repositories](/docs/git#supported-git-providers), navigate to the [Agent tab](/d?to=%2F%5Bteam%5D%2F%7E%2Fvercel-agent&title=Open+Vercel+Agent) of the dashboard.

1.  Click Enable to turn on Vercel Agent.
2.  Under Repositories, choose which repositories to review:
    *   All repositories (default)
    *   Public only
    *   Private only
3.  Under Review Draft PRs, select whether to:
    *   Skip draft PRs (default)
    *   Review draft PRs
4.  Optionally, configure Auto-Recharge to keep your balance topped up automatically:
    *   Set the threshold for When Balance Falls Below
    *   Set the amount for Recharge To Target Balance
    *   Optionally, add a Monthly Spending Limit
5.  Click Save to confirm your settings.

Once you've set up Code Review, it will automatically review pull requests in repositories connected to your Vercel projects.

## [How it works](#how-it-works)

Code Review runs automatically when:

*   A pull request is created
*   A batch of commits is pushed to an open PR
*   A draft PR is created, if you've enabled draft reviews in your settings

When triggered, Code Review analyzes all human-readable files in your codebase, including:

*   Source code files (JavaScript, TypeScript, Python, etc.)
*   Test files
*   Configuration files (`package.json`, YAML files, etc.)
*   Documentation (markdown files, README files)
*   Comments within code

The AI uses your entire codebase as context to understand how your changes fit into the larger system.

Code Review then generates patches, runs them in [secure sandboxes](/docs/vercel-sandbox), and executes your real builds, tests, and linters. Only validated suggestions that pass these checks appear in your PR.

## [Managing reviews](#managing-reviews)

Check out [Managing Reviews](/docs/agent/pr-review/usage) for details on how to customize which repositories get reviewed and monitor your review metrics and spending.

## [Pricing](#pricing)

Code Review uses a credit-based system. Each review costs a fixed $0.30 USD plus token costs billed at the Agent's underlying AI provider's rate, with no additional markup. The token cost varies based on how complex your changes are and how much code the AI needs to analyze.

Pro teams can redeem a $100 USD promotional credit when enabling Agent. You can [purchase credits and enable auto-reload](/docs/agent/pricing#adding-credits) in the Agent tab of your dashboard. For complete pricing details, credit management, and cost tracking information, see [Vercel Agent Pricing](/docs/agent/pricing).

## [Privacy](#privacy)

Code Review doesn't store or train on your data. It only uses LLMs from providers on our [subprocessor list](https://security.vercel.com/?itemUid=e3fae2ca-94a9-416b-b577-5c90e382df57&source=click), and we have agreements in place that don't allow them to train on your data.

--------------------------------------------------------------------------------
title: "Managing Code Reviews"
description: "Customize which repositories get reviewed and track your review metrics and spending."
last_updated: "null"
source: "https://vercel.com/docs/agent/pr-review/usage"
--------------------------------------------------------------------------------

# Managing Code Reviews

Copy page

Ask AI about this page

Last updated October 23, 2025

Once you've [set up Code Review](/docs/agent/pr-review#how-to-set-up-code-review), you can customize settings and monitor performance from the [Agent tab](https://vercel.com/d?to=%2F%5Bteam%5D%2F%7E%2Fvercel-agent&title=Open+Vercel+Agent) in your dashboard. This is your central hub for managing which repositories get reviewed, tracking costs, and analyzing how reviews are performing.

## [Choose which repositories to review](#choose-which-repositories-to-review)

You might want to control which repositories receive automatic reviews, especially when you're testing Code Review for the first time or managing costs across a large organization.

To choose which repositories get reviewed:

1.  Go to the [Agent tab](https://vercel.com/d?to=%2F%5Bteam%5D%2F%7E%2Fvercel-agent&title=Open+Vercel+Agent) in your dashboard.
2.  Click the … button, and then select Settings to view the Vercel Agent settings.
3.  Under Repositories, choose which repositories to review:
    *   All repositories (default): Reviews every repository connected to your Vercel projects
    *   Public only: Only reviews publicly accessible repositories
    *   Private only: Only reviews private repositories
4.  Click Save to apply your changes.

These settings help you start small with specific repos or focus on the repositories that matter most to your team.

## [Allow reviews on draft PRs](#allow-reviews-on-draft-prs)

By default, Code Review skips draft pull requests since they're often work-in-progress. You can enable draft reviews if you want early feedback even on unfinished code.

To enable reviews on draft PRs:

1.  Go to the [Agent tab](https://vercel.com/d?to=%2F%5Bteam%5D%2F%7E%2Fvercel-agent&title=Open+Vercel+Agent) in your dashboard.
2.  Click the … button, and then select Settings to view the Vercel Agent settings.
3.  Under Review Draft PRs, select Review draft PRs.
4.  Click Save to apply your changes.

Enabling this setting means you'll use credits on drafts, but you'll get feedback earlier in your development process.

## [Track spending and costs](#track-spending-and-costs)

You can monitor your spending in real time to manage your budget. The Agent tab shows the cost of each review and your total spending over a given period.

For detailed information about tracking costs, viewing your credit balance, and understanding cost breakdowns, see the [cost tracking section in the pricing docs](/docs/agent/pricing#track-costs-and-spending).

## [Track the suggestions](#track-the-suggestions)

The Agent tab also shows you the total number of suggestions over a given period, as well as the number of suggestions for each individual review.

To view suggestions:

1.  Go to the [Agent tab](https://vercel.com/d?to=%2F%5Bteam%5D%2F%7E%2Fvercel-agent&title=Open+Vercel+Agent).
2.  Check the Suggestions column for each review.

A high number of suggestions might indicate complex changes or code that needs more attention. A low number might mean your code is already following best practices, or the changes are straightforward.

## [Review agent efficiency](#review-agent-efficiency)

Understanding how Code Review performs helps you optimize your setup and get the most value from your credits.

The Agent tab provides several metrics for each review:

*   Repository: Which repository was reviewed
*   PR: The pull request identifier (click to view the PR)
*   Suggestions: Number of code changes recommended
*   Review time: How long the review took to complete
*   Files read: Number of files the AI analyzed
*   Spend: Total cost for that review
*   Time: When the review occurred

Use this data to identify patterns:

*   Expensive reviews: If certain repositories consistently have high costs, consider whether they need special handling or different review settings
*   Long review times: Reviews taking longer than expected might indicate complex codebases or large PRs that could benefit from smaller, incremental changes
*   High file counts: Repositories with many files analyzed might benefit from more focused review scopes

## [Export review metrics](#export-review-metrics)

You can export all your review data to CSV for deeper analysis, reporting, or tracking trends over time.

To export your data:

1.  Go to the [Agent tab](https://vercel.com/d?to=%2F%5Bteam%5D%2F%7E%2Fvercel-agent&title=Open+Vercel+Agent).
2.  Click the Export button.
3.  Save the CSV file to your computer.

The exported data includes all metrics from the dashboard, letting you:

*   Create custom reports for your team or stakeholders
*   Analyze trends across multiple repositories
*   Calculate ROI by comparing review costs to time saved
*   Track adoption and usage patterns over time

## [Disable Vercel Agent](#disable-vercel-agent)

If you need to turn off Vercel Agent completely, you can disable it from the Agent tab. This stops all reviews across all repositories.

To disable Vercel Agent:

1.  Go to the [Agent tab](https://vercel.com/d?to=%2F%5Bteam%5D%2F%7E%2Fvercel-agent&title=Open+Vercel+Agent) in your dashboard.
2.  Click the … button, and then select Disable Vercel Agent.
3.  Confirm the action in the prompt that appears.

Once disabled, Code Review won't run on any new pull requests. You can re-enable Vercel Agent at any time from the same menu.

--------------------------------------------------------------------------------
title: "Vercel Agent Pricing"
description: "Understand how Vercel Agent pricing works and how to manage your credits"
last_updated: "null"
source: "https://vercel.com/docs/agent/pricing"
--------------------------------------------------------------------------------

# Vercel Agent Pricing

Copy page

Ask AI about this page

Last updated October 28, 2025

Vercel Agent uses a credit-based system and all agent features and tools will use the same credit pool.

Each review or investigation costs both:

| Cost component | Price | Details |
| --- | --- | --- |
| Fixed cost | $0.30 USD | Charged for each review or investigation |
| Token costs | Pass-through pricing | Billed at the Agent's underlying AI provider's rate, with no additional markup |

Your total cost per action is the fixed cost plus the token costs.

The token cost varies based on the complexity and amount of data the AI needs to analyze. You can track your spending in real time in the [Agent tab](https://vercel.com/d?to=%2F%5Bteam%5D%2F%7E%2Fvercel-agent&title=Open+Vercel+Agent) of your dashboard.

## [Promotional credit](#promotional-credit)

When you enable Agent for the first time, Pro teams can redeem a $100 USD promotional credit. This credit can be used by any Vercel Agent feature, can only be redeemed once, and is only valid for 2 weeks.

To redeem your promotional credit:

1.  Go to the [Agent tab](https://vercel.com/d?to=%2F%5Bteam%5D%2F%7E%2Fvercel-agent&title=Open+Vercel+Agent) in your dashboard.
2.  If you haven't enabled Agent yet, you'll be prompted to Enable with $100 free credits.

Once your promotional credit is redeemed, you can track your remaining credits in the [Agent tab](https://vercel.com/d?to=%2F%5Bteam%5D%2F%7E%2Fvercel-agent&title=Open+Vercel+Agent) of your dashboard.

## [Track costs and spending](#track-costs-and-spending)

Every review or investigation costs $0.30 USD plus token costs. You can monitor your spending in real time to manage your budget.

To view costs:

1.  Go to the [Agent tab](https://vercel.com/d?to=%2F%5Bteam%5D%2F%7E%2Fvercel-agent&title=Open+Vercel+Agent).
2.  Check your current credit balance at the top of the page. Click the Credits button to view more details and add credits.
3.  View the Cost column in the reviews table to see the cost of each individual review or investigation.

The Agent tab shows you the cost of all reviews and investigations over a given period, as well as the cost of each individual action. If certain repositories or alerts consistently cost more, you can use this data to decide whether to adjust your settings.

## [Adding credits](#adding-credits)

You can add credits to your account at any time through manual purchases or by enabling auto-reload to keep your balance topped up automatically.

### [Manual credit purchases](#manual-credit-purchases)

To manually add credits:

1.  Go to the [Agent tab](https://vercel.com/d?to=%2F%5Bteam%5D%2F%7E%2Fvercel-agent&title=Open+Vercel+Agent) in your dashboard.
2.  Click the Credits button at the top of the page.
3.  In the dialog that appears, enter the amount you want to add to your balance.
4.  Click Continue to Payment to enter your card details and complete the purchase.

Your new credit balance will be available immediately and will be used for all Agent features.

### [Auto-reload](#auto-reload)

Auto-reload automatically adds credits when your balance falls below a threshold you set. This helps prevent the Vercel Agent tools from stopping due to insufficient credits.

To enable auto-reload:

1.  Go to the [Agent tab](https://vercel.com/d?to=%2F%5Bteam%5D%2F%7E%2Fvercel-agent&title=Open+Vercel+Agent) in your dashboard.
2.  Click the Credits button at the top of the page and select Enable next to the auto-reload option.
3.  On the next screen, toggle the switch to Enabled.
4.  Then, configure your auto-reload preferences:
    *   When Balance Falls Below: Set the threshold that triggers an automatic recharge (for example, $10 USD)
    *   Recharge To Target Balance: Set the amount your balance will be recharged to (for example, $50 USD)
    *   Monthly Spending Limit (optional): Set a maximum amount VercelAgent can spend per month to control costs
5.  Click Save to enable auto-reload.

When your balance drops below the threshold, Vercel will automatically charge your payment method and add the specified amount to your credit balance. If you've set a monthly spending limit, auto-reload will stop once you reach that limit for the current month.

--------------------------------------------------------------------------------
title: "Build with AI on Vercel"
description: "Integrate powerful AI services and models seamlessly into your Vercel projects."
last_updated: "null"
source: "https://vercel.com/docs/ai"
--------------------------------------------------------------------------------

# Build with AI on Vercel

Copy page

Ask AI about this page

Last updated October 23, 2025

AI services and models help enhance and automate the building and deployment of applications for various use cases:

*   Chatbots and virtual assistants improve customer interactions.
*   AI-powered content generation automates and optimizes digital content.
*   Recommendation systems deliver personalized experiences.
*   Natural language processing (NLP) enables advanced text analysis and translation.
*   Retrieval-augmented generation (RAG) enhances documentation with context-aware responses.
*   AI-driven image and media services optimize visual content.

## [Integrating with AI providers](#integrating-with-ai-providers)

With Vercel AI integrations, you can build and deploy these AI-powered applications efficiently. Through the Vercel Marketplace, you can research which AI service fits your needs with example use cases. Then, you can install and manage two types of AI integrations:

*   Native integrations: Built-in solutions that work seamlessly with Vercel and include resources with built-in billing and account provisioning.
*   Connectable accounts: Third-party services you can link to your projects.

## [Using AI integrations](#using-ai-integrations)

You can view your installed AI integrations by navigating to the AI tab of your Vercel [dashboard](/dashboard). If you don't have installed integrations, you can browse and connect to the AI models and services that best fit your project's needs. Otherwise, you will see a list of your installed native and connectable account integrations, with an indication of which project(s) they are connected to. You will be able to browse available services, models and templates below the list of installed integrations.

See the [adding a provider](/docs/ai/adding-a-provider) guide to learn how to add a provider to your Vercel project, or the [adding a model](/docs/ai/adding-a-model) guide to learn how to add a model to your Vercel project.

## [Featured AI integrations](#featured-ai-integrations)

[

### xAIMarketplace native integration

An AI service with an efficient text model and a wide context image understanding model.

](/docs/ai/xai)[

### GroqMarketplace native integration

A high-performance AI inference service with an ultra-fast Language Processing Unit (LPU) architecture.

](/docs/ai/groq)[

### falMarketplace native integration

A serverless AI inferencing platform for creative processes.

](/docs/ai/fal)[

### DeepInfraMarketplace native integration

A platform with access to a vast library of open-source models.

](/docs/ai/deepinfra)

[

### PerplexityMarketplace connectable account

Learn how to integrate Perplexity with Vercel.

](/docs/ai/perplexity)[

### ReplicateMarketplace connectable account

Learn how to integrate Replicate with Vercel.

](/docs/ai/replicate)[

### ElevenLabsMarketplace connectable account

Learn how to integrate ElevenLabs with Vercel.

](/docs/ai/elevenlabs)[

### LMNTMarketplace connectable account

Learn how to integrate LMNT with Vercel.

](/docs/ai/lmnt)[

### Together AIMarketplace connectable account

Learn how to integrate Together AI with Vercel.

](/docs/ai/togetherai)[

### OpenAIGuide

Connect powerful AI models like GPT-4

](/docs/ai/openai)

## [More resources](#more-resources)

*   [AI Integrations for Vercel](https://www.youtube.com/watch?v=so4Jatc85Aw)

--------------------------------------------------------------------------------
title: "AI Gateway"
description: "TypeScript toolkit for building AI-powered applications with React, Next.js, Vue, Svelte and Node.js"
last_updated: "null"
source: "https://vercel.com/docs/ai-gateway"
--------------------------------------------------------------------------------

# AI Gateway

Copy page

Ask AI about this page

Last updated October 23, 2025

AI Gateway is available on [all plans](/docs/plans) and your use is subject to [AI Product Terms](/legal/ai-product-terms).

The [AI Gateway](https://vercel.com/ai-gateway) provides a unified API to access [hundreds of models](https://vercel.com/ai-gateway/models) through a single endpoint. It gives you the ability to set budgets, monitor usage, load-balance requests, and manage fallbacks.

The design allows it to work seamlessly with [AI SDK 5](/docs/ai-gateway/getting-started), [OpenAI SDK](/docs/ai-gateway/openai-compat), or your [preferred framework](/docs/ai-gateway/framework-integrations).

## [Key features](#key-features)

*   Unified API: helps you switch between providers and models with minimal code changes
*   High reliability: automatically retries requests to other providers if one fails
*   Embeddings support: generate vector embeddings for search, retrieval, and other tasks
*   Spend monitoring: monitor your spending across different providers
*   No markup on tokens: tokens cost the same as they would from the provider directly, with 0% markup, including with [Bring Your Own Key (BYOK)](/docs/ai-gateway/byok).

AI SDKPythonOpenAI HTTP

index.ts

```
import { generateText } from 'ai';
 
const { text } = generateText({
  model: 'anthropic/claude-sonnet-4',
  prompt: 'What is the capital of France?',
});
```

index.py

```
import os
from openai import OpenAI
 
client = OpenAI(
  api_key=os.getenv('AI_GATEWAY_API_KEY'),
  base_url='https://ai-gateway.vercel.sh/v1'
)
 
response = client.chat.completions.create(
  model='xai/grok-4',
  messages=[
    {
      'role': 'user',
      'content': 'Why is the sky blue?'
    }
  ]
)
```

index.sh

```
curl -X POST "https://ai-gateway.vercel.sh/v1/chat/completions" \
-H "Authorization: Bearer $AI_GATEWAY_API_KEY" \
-H "Content-Type: application/json" \
-d '{
  "model": "openai/gpt-5",
  "messages": [
    {
      "role": "user",
      "content": "Why is the sky blue?"
    }
  ],
  "stream": false
}'
```

## [More resources](#more-resources)

*   [Getting started with AI Gateway](/docs/ai-gateway/getting-started)
*   [Models and providers](/docs/ai-gateway/models-and-providers)
*   [Provider options (routing & fallbacks)](/docs/ai-gateway/provider-options)
*   [Observability](/docs/ai-gateway/observability)
*   [OpenAI compatibility](/docs/ai-gateway/openai-compat)
*   [Usage and billing](/docs/ai-gateway/usage)
*   [Authentication](/docs/ai-gateway/authentication)
*   [Bring your own key](/docs/ai-gateway/byok)
*   [Framework integrations](/docs/ai-gateway/framework-integrations)
*   [App attribution](/docs/ai-gateway/app-attribution)

--------------------------------------------------------------------------------
title: "App Attribution"
description: "Attribute your requests so Vercel can identify and feature your app on AI Gateway pages"
last_updated: "null"
source: "https://vercel.com/docs/ai-gateway/app-attribution"
--------------------------------------------------------------------------------

# App Attribution

Copy page

Ask AI about this page

Last updated October 21, 2025

App attribution allows Vercel to identify the application making a request through AI Gateway. When provided, your app can be featured on AI Gateway pages, driving awareness.

App Attribution is optional. If you do not send these headers, your requests will work normally.

## [How it works](#how-it-works)

AI Gateway reads two request headers when present:

*   `http-referer`: The URL of the page or site making the request.
*   `x-title`: A human‑readable name for your app (for example, _"Acme Chat"_).

You can set these headers directly in your server-side requests to AI Gateway.

## [Examples](#examples)

TypeScript (AI SDK)TypeScript (OpenAI)Python (OpenAI)

ai-sdk.ts

```
import { streamText } from 'ai';
 
const result = streamText({
  headers: {
    'http-referer': 'https://myapp.vercel.app',
    'x-title': 'MyApp',
  },
  model: 'anthropic/claude-sonnet-4',
  prompt: 'Hello, world!',
});
 
for await (const part of result.textStream) {
  process.stdout.write(part);
}
```

openai.ts

```
import OpenAI from 'openai';
 
const openai = new OpenAI({
  apiKey: process.env.AI_GATEWAY_API_KEY,
  baseURL: 'https://ai-gateway.vercel.sh/v1',
});
 
const response = await openai.chat.completions.create(
  {
    model: 'anthropic/claude-sonnet-4',
    messages: [
      {
        role: 'user',
        content: 'Hello, world!',
      },
    ],
  },
  {
    headers: {
      'http-referer': 'https://myapp.vercel.app',
      'x-title': 'MyApp',
    },
  },
);
 
console.log(response.choices[0].message.content);
```

openai.py

```
import os
from openai import OpenAI
 
client = OpenAI(
  api_key=os.getenv('AI_GATEWAY_API_KEY'),
  base_url='https://ai-gateway.vercel.sh/v1'
)
 
response = client.chat.completions.create(
    model='anthropic/claude-sonnet-4',
    messages=[
        {
            'role': 'user',
            'content': 'Hello, world!',
        },
    ],
    extra_headers={
        'http-referer': 'https://myapp.vercel.app',
        'x-title': 'MyApp',
    },
)
 
print(response.choices[0].message.content)
```

## [Setting headers at the provider level](#setting-headers-at-the-provider-level)

You can also configure attribution headers when you create the AI Gateway provider instance. This way, the headers are automatically included in all requests without needing to specify them for each function call.

provider-level.ts

```
import { streamText } from 'ai';
import { createGateway } from '@ai-sdk/gateway';
 
const gateway = createGateway({
  headers: {
    'http-referer': 'https://myapp.vercel.app',
    'x-title': 'MyApp',
  },
});
 
const result = streamText({
  model: gateway('anthropic/claude-sonnet-4'),
  prompt: 'Hello, world!',
});
 
for await (const part of result.textStream) {
  process.stdout.write(part);
}
```

## [Using the Global Default Provider](#using-the-global-default-provider)

You can also use the AI SDK's [global provider configuration](https://ai-sdk.dev/docs/ai-sdk-core/provider-management#global-provider-configuration) to set your custom provider instance as the default. This allows you to use plain string model IDs throughout your application while automatically including your attribution headers.

global-provider.ts

```
import { streamText } from 'ai';
import { createGateway } from '@ai-sdk/gateway';
 
const gateway = createGateway({
  headers: {
    'http-referer': 'https://myapp.vercel.app',
    'x-title': 'MyApp',
  },
});
 
// Set your provider as the default to allow plain-string model id creation with this instance
globalThis.AI_SDK_DEFAULT_PROVIDER = gateway;
 
// Now you can use plain string model IDs and they'll use your custom provider
const result = streamText({
  model: 'anthropic/claude-sonnet-4', // Uses the gateway provider with headers
  prompt: 'Hello, world!',
});
 
for await (const part of result.textStream) {
  process.stdout.write(part);
}
```

--------------------------------------------------------------------------------
title: "Authentication"
description: "Learn how to authenticate with the AI Gateway using API keys and OIDC tokens."
last_updated: "null"
source: "https://vercel.com/docs/ai-gateway/authentication"
--------------------------------------------------------------------------------

# Authentication

Copy page

Ask AI about this page

Last updated October 21, 2025

To use the AI Gateway, you need to authenticate your requests. There are two authentication methods available:

1.  API Key Authentication: Create and manage API keys through the Vercel Dashboard
2.  OIDC Token Authentication: Use Vercel's automatically generated OIDC tokens

## [API key](#api-key)

API keys provide a secure way to authenticate your requests to the AI Gateway. You can create and manage multiple API keys through the Vercel Dashboard.

### [Creating an API Key](#creating-an-api-key)

1.  ### [Navigate to the AI Gateway tab](#navigate-to-the-ai-gateway-tab)
    
    From the [Vercel dashboard](https://vercel.com/dashboard), click the AI Gateway tab to access the AI Gateway settings.
    
2.  ### [Access API key management](#access-api-key-management)
    
    Click API keys on the left sidebar to view and manage your API keys.
    
3.  ### [Create a new API key](#create-a-new-api-key)
    
    Click Create key and proceed with Create key from the dialog to generate a new API key.
    
4.  ### [Save your API key](#save-your-api-key)
    
    Once you have the API key, save it to `.env.local` at the root of your project (or in your preferred environment file):
    
    .env.local
    
    ```
    AI_GATEWAY_API_KEY=your_api_key_here
    ```
    

### [Using the API key](#using-the-api-key)

When you specify a model id as a plain string, the AI SDK will automatically use the Vercel AI Gateway provider to route the request. The AI Gateway provider looks for the API key in the `AI_GATEWAY_API_KEY` environment variable by default.

app/api/chat/route.ts

```
import { generateText } from 'ai';
 
export async function GET() {
  const result = await generateText({
    model: 'xai/grok-3',
    prompt: 'Why is the sky blue?',
  });
  return Response.json(result);
}
```

## [OIDC token](#oidc-token)

The [Vercel OIDC token](/docs/oidc) is a way to authenticate your requests to the AI Gateway without needing to manage an API key. Vercel automatically generates the OIDC token that it associates with your Vercel project.

Vercel OIDC tokens are only valid for 12 hours, so you will need to refresh them periodically during local development. You can do this by running `vercel env pull` again.

### [Setting up OIDC authentication](#setting-up-oidc-authentication)

1.  ### [Link to a Vercel project](#link-to-a-vercel-project)
    
    Before you can use the OIDC token during local development, ensure that you link your application to a Vercel project:
    
    terminal
    
    ```
    vercel link
    ```
    
2.  ### [Pull environment variables](#pull-environment-variables)
    
    Pull the environment variables from Vercel to get the OIDC token:
    
    terminal
    
    ```
    vercel env pull
    ```
    
3.  ### [Use OIDC authentication in your code](#use-oidc-authentication-in-your-code)
    
    With OIDC authentication, you can directly use the gateway provider without needing to obtain an API key or set it in an environment variable:
    
    app/api/chat/route.ts
    
    ```
    import { generateText } from 'ai';
     
    export async function GET() {
      const result = await generateText({
        model: 'xai/grok-3',
        prompt: 'Why is the sky blue?',
      });
      return Response.json(result);
    }
    ```

--------------------------------------------------------------------------------
title: "Bring Your Own Key (BYOK)"
description: "Learn how to configure your own provider keys with the AI Gateway."
last_updated: "null"
source: "https://vercel.com/docs/ai-gateway/byok"
--------------------------------------------------------------------------------

# Bring Your Own Key (BYOK)

Copy page

Ask AI about this page

Last updated October 21, 2025

Using your own credentials with an external AI provider allows AI Gateway to authenticate requests on your behalf with [no added markup](/docs/ai-gateway/pricing#using-a-custom-api-key). This approach is useful for utilizing credits provided by the AI provider or executing AI queries that access private cloud data. If a query using your credentials fails, AI Gateway will retry the query with its system credentials to improve service availability.

Integrating credentials like this with AI Gateway is sometimes referred to as Bring-Your-Own-Key, or BYOK. In the Vercel dashboard this feature is found in the AI Gateway tab under the Integrations section in the sidebar.

Provider credentials are scoped to be available throughout your Vercel team, so you can use the same credentials across multiple projects.

## [Getting started](#getting-started)

1.  ### [Retrieve credentials from your AI provider](#retrieve-credentials-from-your-ai-provider)
    
    First, retrieve credentials from your AI provider. These credentials will be used first to authenticate requests made to that provider through the AI Gateway. If a query made with your credentials fails, AI Gateway will re-attempt with system credentials, aiming to provide improved availability.
    
2.  ### [Add the credentials to your Vercel team](#add-the-credentials-to-your-vercel-team)
    
    1.  Go to the [AI Gateway](https://vercel.com/d?to=%2F%5Bteam%5D%2F%7E%2Fai%2F&title=) tab in your [Vercel dashboard](https://vercel.com/dashboard).
    2.  Click on the Integrations section on the left sidebar.
    3.  Find your provider from the list and click Add.
    4.  In the dialog that appears, enter the credentials you retrieved from the provider.
    5.  Ensure that the Enabled toggle is turned on so that the credentials are active.
    6.  Click Test Key to validate and add your credentials.
3.  ### [Use the credentials in your AI Gateway requests](#use-the-credentials-in-your-ai-gateway-requests)
    
    Once the credentials are added, it will automatically be included in your requests to the AI Gateway. You can now use these credentials to authenticate your requests.
    

## [Testing your credentials](#testing-your-credentials)

After successfully adding your credentials for a provider, you can verify that they're working directly from the Integrations tab. To test your credentials:

1.  In the [AI Gateway](https://vercel.com/d?to=%2F%5Bteam%5D%2F%7E%2Fai%2F&title=) tab, navigate to the Integrations section.
2.  Click the menu for your configured provider.
3.  Select Test Key from the dropdown.

This will execute a small test query using a cheap and fast model from the selected provider to verify the health of your credentials. The test is designed to be minimal and cost-effective while ensuring your authentication is working properly.

Once the test completes, you can click on the test result badge to open a detailed test result modal. This modal includes:

*   The code used to make the test request
*   The raw JSON response returned by the AI Gateway

--------------------------------------------------------------------------------
title: "Framework Integrations"
description: "Explore available community framework integrations with Vercel AI Gateway"
last_updated: "null"
source: "https://vercel.com/docs/ai-gateway/framework-integrations"
--------------------------------------------------------------------------------

# Framework Integrations

Copy page

Ask AI about this page

Last updated October 21, 2025

The Vercel [AI Gateway](/docs/ai-gateway) integrates with popular community AI frameworks and tools, enabling you to build powerful AI applications while leveraging the Gateway's features like [cost tracking](/docs/ai-gateway/observability) and [unified API access](/docs/ai-gateway/models-and-providers).

### [Integration overview](#integration-overview)

You can integrate the AI Gateway with popular frameworks in several ways:

*   OpenAI Compatibility Layer: Use the AI Gateway's [OpenAI-compatible endpoints](/docs/ai-gateway/openai-compat)
*   Native Support: Direct integration through plugins or official support
*   AI SDK Integration: Leverage the [AI SDK](/docs/ai-sdk) to access [AI Gateway](/docs/ai-gateway) capabilities directly

### [Supported frameworks](#supported-frameworks)

The following below list is a non-exhaustive list of frameworks that currently support AI Gateway integration:

*   [LangChain](/docs/ai-gateway/framework-integrations/langchain)
*   [LangFuse](/docs/ai-gateway/framework-integrations/langfuse)
*   [LiteLLM](/docs/ai-gateway/framework-integrations/litellm)
*   [LlamaIndex](/docs/ai-gateway/framework-integrations/llamaindex)
*   [Mastra](/docs/ai-gateway/framework-integrations/mastra)
*   [Pydantic AI](/docs/ai-gateway/framework-integrations/pydantic-ai)

--------------------------------------------------------------------------------
title: "LangChain"
description: "Learn how to integrate Vercel AI Gateway with LangChain to access multiple AI models through a unified interface"
last_updated: "null"
source: "https://vercel.com/docs/ai-gateway/framework-integrations/langchain"
--------------------------------------------------------------------------------

# LangChain

Copy page

Ask AI about this page

Last updated September 24, 2025

[LangChain](https://js.langchain.com) gives you tools for every step of the agent development lifecycle. This guide demonstrates how to integrate [Vercel AI Gateway](/docs/ai-gateway) with LangChain to access various AI models and providers.

## [Getting started](#getting-started)

1.  ### [Create a new project](#create-a-new-project)
    
    First, create a new directory for your project and initialize it:
    
    terminal
    
    ```
    mkdir langchain-ai-gateway
    cd langchain-ai-gateway
    pnpm dlx init -y
    ```
    
2.  ### [Install dependencies](#install-dependencies)
    
    Install the required LangChain packages along with the `dotenv` and `@types/node` packages:
    
    pnpmyarnnpmbun
    
    ```
    pnpm i langchain @langchain/core @langchain/openai dotenv @types/node
    ```
    
3.  ### [Configure environment variables](#configure-environment-variables)
    
    Create a `.env` file with your [Vercel AI Gateway API key](/docs/ai-gateway#using-the-ai-gateway-with-an-api-key):
    
    .env
    
    ```
    AI_GATEWAY_API_KEY=your-api-key-here
    ```
    
    If you're using the [AI Gateway from within a Vercel deployment](/docs/ai-gateway#using-the-ai-gateway-with-a-vercel-oidc-token), you can also use the `VERCEL_OIDC_TOKEN` environment variable which will be automatically provided.
    
4.  ### [Create your LangChain application](#create-your-langchain-application)
    
    Create a new file called `index.ts` with the following code:
    
    index.ts
    
    ```
    import 'dotenv/config';
    import { ChatOpenAI } from '@langchain/openai';
    import { HumanMessage } from '@langchain/core/messages';
     
    async function main() {
      console.log('=== LangChain Chat Completion with AI Gateway ===');
     
      const apiKey =
        process.env.AI_GATEWAY_API_KEY || process.env.VERCEL_OIDC_TOKEN;
     
      const chat = new ChatOpenAI({
        apiKey: apiKey,
        modelName: 'openai/gpt-5',
        temperature: 0.7,
        configuration: {
          baseURL: 'https://ai-gateway.vercel.sh/v1',
        },
      });
     
      try {
        const response = await chat.invoke([
          new HumanMessage('Write a one-sentence bedtime story about a unicorn.'),
        ]);
     
        console.log('Response:', response.content);
      } catch (error) {
        console.error('Error:', error);
      }
    }
     
    main().catch(console.error);
    ```
    
    The following code:
    
    *   Initializes a `ChatOpenAI` instance configured to use the AI Gateway
    *   Sets the model `temperature` to `0.7`
    *   Makes a chat completion request
    *   Handles any potential errors
5.  ### [Running the application](#running-the-application)
    
    Run your application using Node.js:
    
    pnpmyarnnpmbun
    
    ```
    pnpm dlx tsx index.ts
    ```
    
    You should see a response from the AI model in your console.

--------------------------------------------------------------------------------
title: "LangFuse"
description: "Learn how to integrate Vercel AI Gateway with LangFuse to access multiple AI models through a unified interface"
last_updated: "null"
source: "https://vercel.com/docs/ai-gateway/framework-integrations/langfuse"
--------------------------------------------------------------------------------

# LangFuse

Copy page

Ask AI about this page

Last updated September 24, 2025

[LangFuse](https://langfuse.com/) is an LLM engineering platform that helps teams collaboratively develop, monitor, evaluate, and debug AI applications. This guide demonstrates how to integrate [Vercel AI Gateway](/docs/ai-gateway) with LangFuse to access various AI models and providers.

## [Getting started](#getting-started)

1.  ### [Create a new project](#create-a-new-project)
    
    First, create a new directory for your project and initialize it:
    
    terminal
    
    ```
    mkdir langfuse-ai-gateway
    cd langfuse-ai-gateway
    pnpm dlx init -y
    ```
    
2.  ### [Install dependencies](#install-dependencies)
    
    Install the required LangFuse packages along with the `dotenv` and `@types/node` packages:
    
    pnpmyarnnpmbun
    
    ```
    pnpm i langfuse openai dotenv @types/node
    ```
    
3.  ### [Configure environment variables](#configure-environment-variables)
    
    Create a `.env` file with your [Vercel AI Gateway API key](/docs/ai-gateway#using-the-ai-gateway-with-an-api-key) and LangFuse API keys:
    
    .env
    
    ```
    AI_GATEWAY_API_KEY=your-api-key-here
     
    LANGFUSE_PUBLIC_KEY=your_langfuse_public_key
    LANGFUSE_SECRET_KEY=your_langfuse_secret_key
    LANGFUSE_HOST=https://cloud.langfuse.com
    ```
    
    If you're using the [AI Gateway from within a Vercel deployment](/docs/ai-gateway#using-the-ai-gateway-with-a-vercel-oidc-token), you can also use the `VERCEL_OIDC_TOKEN` environment variable which will be automatically provided.
    
4.  ### [Create your LangFuse application](#create-your-langfuse-application)
    
    Create a new file called `index.ts` with the following code:
    
    index.ts
    
    ```
    import { observeOpenAI } from 'langfuse';
    import OpenAI from 'openai';
     
    const openaiClient = new OpenAI({
      apiKey: process.env.AI_GATEWAY_API_KEY,
      baseURL: 'https://ai-gateway.vercel.sh/v1',
    });
     
    const client = observeOpenAI(openaiClient, {
      generationName: 'fun-fact-request', // Optional: Name of the generation in Langfuse
    });
     
    const response = await client.chat.completions.create({
      model: 'moonshotai/kimi-k2',
      messages: [
        { role: 'system', content: 'You are a helpful assistant.' },
        { role: 'user', content: 'Tell me about the food scene in San Francisco.' },
      ],
    });
     
    console.log(response.choices[0].message.content);
    ```
    
    The following code:
    
    *   Creates an OpenAI client configured to use the Vercel AI Gateway
    *   Uses `observeOpenAI` to wrap the client for automatic tracing and logging
    *   Makes a chat completion request through the AI Gateway
    *   Automatically captures request/response data, token usage, and metrics
5.  ### [Running the application](#running-the-application)
    
    Run your application using Node.js:
    
    pnpmyarnnpmbun
    
    ```
    pnpm dlx tsx index.ts
    ```
    
    You should see a response from the AI model in your console.

--------------------------------------------------------------------------------
title: "LiteLLM"
description: "Learn how to integrate Vercel AI Gateway with LiteLLM to access multiple AI models through a unified interface"
last_updated: "null"
source: "https://vercel.com/docs/ai-gateway/framework-integrations/litellm"
--------------------------------------------------------------------------------

# LiteLLM

Copy page

Ask AI about this page

Last updated September 24, 2025

[LiteLLM](https://www.litellm.ai/) is an open-source library that provides a unified interface to call LLMs. This guide demonstrates how to integrate [Vercel AI Gateway](/docs/ai-gateway) with LiteLLM to access various AI models and providers.

## [Getting started](#getting-started)

1.  ### [Create a new project](#create-a-new-project)
    
    First, create a new directory for your project:
    
    terminal
    
    ```
    mkdir litellm-ai-gateway
    cd litellm-ai-gateway
    ```
    
2.  ### [Install dependencies](#install-dependencies)
    
    Install the required LiteLLM Python package:
    
    terminal
    
    ```
    pip install litellm python-dotenv
    ```
    
3.  ### [Configure environment variables](#configure-environment-variables)
    
    Create a `.env` file with your [Vercel AI Gateway API key](/docs/ai-gateway#using-the-ai-gateway-with-an-api-key):
    
    .env
    
    ```
    VERCEL_AI_GATEWAY_API_KEY=your-api-key-here
    ```
    
    If you're using the [AI Gateway from within a Vercel deployment](/docs/ai-gateway#using-the-ai-gateway-with-a-vercel-oidc-token), you can also use the `VERCEL_OIDC_TOKEN` environment variable which will be automatically provided.
    
4.  ### [Create your LiteLLM application](#create-your-litellm-application)
    
    Create a new file called `main.py` with the following code:
    
    main.py
    
    ```
    import os
    import litellm
    from dotenv import load_dotenv
     
    load_dotenv()
     
    os.environ["VERCEL_AI_GATEWAY_API_KEY"] = os.getenv("VERCEL_AI_GATEWAY_API_KEY")
     
    # Define messages
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Tell me about the food scene in San Francisco."}
    ]
     
    response = litellm.completion(
        model="vercel_ai_gateway/openai/gpt-4o",
        messages=messages
    )
     
    print(response.choices[0].message.content)
    ```
    
    The following code:
    
    *   Uses LiteLLM's `completion` function to make requests through Vercel AI Gateway
    *   Specifies the model using the `vercel_ai_gateway/` prefix
    *   Makes a chat completion request and prints the response
5.  ### [Running the application](#running-the-application)
    
    Run your Python application:
    
    terminal
    
    ```
    python main.py
    ```
    
    You should see a response from the AI model in your console.

--------------------------------------------------------------------------------
title: "LlamaIndex"
description: "Learn how to integrate Vercel AI Gateway with LlamaIndex to access multiple AI models through a unified interface"
last_updated: "null"
source: "https://vercel.com/docs/ai-gateway/framework-integrations/llamaindex"
--------------------------------------------------------------------------------

# LlamaIndex

Copy page

Ask AI about this page

Last updated September 24, 2025

[LlamaIndex](https://www.llamaindex.ai/) makes it simple to build knowledge assistants using LLMs connected to your enterprise data. This guide demonstrates how to integrate [Vercel AI Gateway](/docs/ai-gateway) with LlamaIndex to access various AI models and providers.

## [Getting started](#getting-started)

1.  ### [Create a new project](#create-a-new-project)
    
    First, create a new directory for your project and initialize it:
    
    terminal
    
    ```
    mkdir llamaindex-ai-gateway
    cd llamaindex-ai-gateway
    ```
    
2.  ### [Install dependencies](#install-dependencies)
    
    Install the required LlamaIndex packages along with the `python-dotenv` package:
    
    terminal
    
    ```
    pip install llama-index-llms-vercel-ai-gateway llama-index python-dotenv
    ```
    
3.  ### [Configure environment variables](#configure-environment-variables)
    
    Create a `.env` file with your [Vercel AI Gateway API key](/docs/ai-gateway#using-the-ai-gateway-with-an-api-key):
    
    .env
    
    ```
    AI_GATEWAY_API_KEY=your-api-key-here
    ```
    
    If you're using the [AI Gateway from within a Vercel deployment](/docs/ai-gateway#using-the-ai-gateway-with-a-vercel-oidc-token), you can also use the `VERCEL_OIDC_TOKEN` environment variable which will be automatically provided.
    
4.  ### [Create your LlamaIndex application](#create-your-llamaindex-application)
    
    Create a new file called `main.py` with the following code:
    
    main.py
    
    ```
    from dotenv import load_dotenv
    from llama_index.llms.vercel_ai_gateway import VercelAIGateway
    from llama_index.core.llms import ChatMessage
    import os
     
    load_dotenv()
     
    llm = VercelAIGateway(
        api_key=os.getenv("AI_GATEWAY_API_KEY"),
        max_tokens=200000,
        context_window=64000,
        model="anthropic/claude-4-sonnet",
    )
     
    message = ChatMessage(role="user", content="Tell me a story in 250 words")
    resp = llm.stream_chat([message])
    for r in resp:
        print(r.delta, end="")
    ```
    
    The following code:
    
    *   Initializes a `VercelAIGateway` LLM instance with your API key
    *   Configures the model to use Anthropic's Claude 4 Sonnet via the AI Gateway
    *   Creates a chat message and streams the response
5.  ### [Running the application](#running-the-application)
    
    Run your application using Python:
    
    terminal
    
    ```
    python main.py
    ```
    
    You should see a streaming response from the AI model.

--------------------------------------------------------------------------------
title: "Mastra"
description: "Learn how to integrate Vercel AI Gateway with Mastra to access multiple AI models through a unified interface"
last_updated: "null"
source: "https://vercel.com/docs/ai-gateway/framework-integrations/mastra"
--------------------------------------------------------------------------------

# Mastra

Copy page

Ask AI about this page

Last updated September 24, 2025

[Mastra](https://mastra.ai) is a framework for building and deploying AI-powered features using a modern JavaScript stack powered by the [Vercel AI SDK](/docs/ai-sdk). Integrating with AI Gateway provides unified model management and routing capabilities.

## [Getting started](#getting-started)

1.  ### [Create a new Mastra project](#create-a-new-mastra-project)
    
    First, create a new Mastra project using the CLI:
    
    terminal
    
    ```
    pnpm dlx create-mastra@latest
    ```
    
    During the setup, the system prompts you to name your project, choose a default provider, and more. and more. Feel free to use the default settings.
    
2.  ### [Install dependencies](#install-dependencies)
    
    To use the AI Gateway provider, install the `@ai-sdk/gateway` package along with Mastra:
    
    pnpmyarnnpmbun
    
    ```
    pnpm i @ai-sdk/gateway mastra @mastra/core @mastra/memory
    ```
    
3.  ### [Configure environment variables](#configure-environment-variables)
    
    Create or update your `.env` file with your [Vercel AI Gateway API key](/docs/ai-gateway#using-the-ai-gateway-with-an-api-key):
    
    .env
    
    ```
    AI_GATEWAY_API_KEY=your-api-key-here
    ```
    
4.  ### [Configure your agent to use AI Gateway](#configure-your-agent-to-use-ai-gateway)
    
    Now, swap out the `@ai-sdk/openai` package (or your existing model provider) for the `@ai-sdk/gateway` package.
    
    Update your agent configuration file, typically `src/mastra/agents/weather-agent.ts` to the following code:
    
    src/mastra/agents/weather-agent.ts
    
    ```
    import 'dotenv/config';
    import { gateway } from '@ai-sdk/gateway';
    import { Agent } from '@mastra/core/agent';
    import { Memory } from '@mastra/memory';
    import { LibSQLStore } from '@mastra/libsql';
    import { weatherTool } from '../tools/weather-tool';
     
    export const weatherAgent = new Agent({
      name: 'Weather Agent',
      instructions: `
          You are a helpful weather assistant that provides accurate weather information and can help planning activities based on the weather.
     
          Your primary function is to help users get weather details for specific locations. When responding:
          - Always ask for a location if none is provided
          - If the location name isn't in English, please translate it
          - If giving a location with multiple parts (e.g. "New York, NY"), use the most relevant part (e.g. "New York")
          - Include relevant details like humidity, wind conditions, and precipitation
          - Keep responses concise but informative
          - If the user asks for activities and provides the weather forecast, suggest activities based on the weather forecast.
          - If the user asks for activities, respond in the format they request.
     
          Use the weatherTool to fetch current weather data.
    `,
      model: gateway('google/gemini-2.5-flash'),
      tools: { weatherTool },
      memory: new Memory({
        storage: new LibSQLStore({
          url: 'file:../mastra.db', // path is relative to the .mastra/output directory
        }),
      }),
    });
     
    (async () => {
      try {
        const response = await weatherAgent.generate(
          "What's the weather in San Francisco today?",
        );
        console.log('Weather Agent Response:', response.text);
      } catch (error) {
        console.error('Error invoking weather agent:', error);
      }
    })();
    ```
    
5.  ### [Running the application](#running-the-application)
    
    Since your agent is now configured to use AI Gateway, run the Mastra development server:
    
    pnpmyarnnpmbun
    
    ```
    pnpm dev
    ```
    
    Open the [Mastra Playground and Mastra API](https://mastra.ai/en/docs/server-db/local-dev-playground) to test your agents, workflows, and tools.

--------------------------------------------------------------------------------
title: "Pydantic AI"
description: "Learn how to integrate Vercel AI Gateway with Pydantic AI to access multiple AI models through a unified interface"
last_updated: "null"
source: "https://vercel.com/docs/ai-gateway/framework-integrations/pydantic-ai"
--------------------------------------------------------------------------------

# Pydantic AI

Copy page

Ask AI about this page

Last updated September 24, 2025

[Pydantic AI](https://ai.pydantic.dev/) is a Python agent framework designed to make it easy to build production grade applications with AI. This guide demonstrates how to integrate [Vercel AI Gateway](/docs/ai-gateway) with Pydantic AI to access various AI models and providers.

## [Getting started](#getting-started)

1.  ### [Create a new project](#create-a-new-project)
    
    First, create a new directory for your project and initialize it:
    
    terminal
    
    ```
    mkdir pydantic-ai-gateway
    cd pydantic-ai-gateway
    ```
    
2.  ### [Install dependencies](#install-dependencies)
    
    Install the required Pydantic AI packages along with the `python-dotenv` package:
    
    terminal
    
    ```
    pip install pydantic-ai python-dotenv
    ```
    
3.  ### [Configure environment variables](#configure-environment-variables)
    
    Create a `.env` file with your [Vercel AI Gateway API key](/docs/ai-gateway#using-the-ai-gateway-with-an-api-key):
    
    .env
    
    ```
    VERCEL_AI_GATEWAY_API_KEY=your-api-key-here
    ```
    
    If you're using the [AI Gateway from within a Vercel deployment](/docs/ai-gateway#using-the-ai-gateway-with-a-vercel-oidc-token), you can also use the `VERCEL_OIDC_TOKEN` environment variable which will be automatically provided.
    
4.  ### [Create your Pydantic AI application](#create-your-pydantic-ai-application)
    
    Create a new file called `main.py` with the following code:
    
    main.py
    
    ```
    from dotenv import load_dotenv
    from pydantic import BaseModel
    from pydantic_ai import Agent
    from pydantic_ai.models.openai import OpenAIModel
    from pydantic_ai.providers.vercel import VercelProvider
     
    load_dotenv()
     
    class CityInfo(BaseModel):
        city: str
        country: str
        population: int
        famous_for: str
     
    agent = Agent(
        OpenAIModel('anthropic/claude-4-sonnet', provider=VercelProvider()),
        output_type=CityInfo,
        system_prompt='Provide accurate city information.'
    )
     
    if __name__ == '__main__':
        cities = ["Tokyo", "Paris", "New York"]
     
        for city in cities:
            result = agent.run_sync(f'Tell me about {city}')
            info = result.output
     
            print(f"City: {info.city}")
            print(f"Country: {info.country}")
            print(f"Population: {info.population:,}")
            print(f"Famous for: {info.famous_for}")
            print("-" * 5)
    ```
    
    The following code:
    
    *   Defines a `CityInfo` Pydantic model for structured output
    *   Uses the `VercelProvider` to route requests through the AI Gateway
    *   Handles the response data using Pydantic's type validation
5.  ### [Running the application](#running-the-application)
    
    Run your application using Python:
    
    terminal
    
    ```
    python main.py
    ```
    
    You should see structured city information for Tokyo, Paris, and New York displayed in your console.

--------------------------------------------------------------------------------
title: "Getting Started"
description: "Guide to getting started with AI Gateway"
last_updated: "null"
source: "https://vercel.com/docs/ai-gateway/getting-started"
--------------------------------------------------------------------------------

# Getting Started

Copy page

Ask AI about this page

Last updated October 23, 2025

This quickstart will walk you through making an AI model request with Vercel's [AI Gateway](https://vercel.com/ai-gateway). While this guide uses the [AI SDK](https://ai-sdk.dev), you can also integrate with the [OpenAI SDK](/docs/ai-gateway/openai-compat) or other [community frameworks](/docs/ai-gateway/framework-integrations).

1.  ### [Set up your application](#set-up-your-application)
    
    Start by creating a new directory using the `mkdir` command. Change into your new directory and then run the `pnpm init` command, which will create a `package.json`.
    
    terminal
    
    ```
    mkdir demo
    cd demo
    pnpm init
    ```
    
2.  ### [Install dependencies](#install-dependencies)
    
    Install the AI SDK package, `ai`, along with other necessary dependencies.
    
    pnpmyarnnpmbun
    
    ```
    pnpm i ai dotenv @types/node tsx typescript
    ```
    
    `dotenv` is used to access environment variables (your AI Gateway API key) within your application. The `tsx` package is a TypeScript runner that allows you to run your TypeScript code. The `typescript` package is the TypeScript compiler. The `@types/node` package is the TypeScript definitions for the Node.js API.
    
3.  ### [Set up your API key](#set-up-your-api-key)
    
    To create an API key, go to the [AI Gateway](https://vercel.com/d?to=%2F%5Bteam%5D%2F%7E%2Fai&title=Go+to+AI+Gateway) tab of the dashboard:
    
    1.  Select API keys on the left side bar
    2.  Then select Create key and proceed with Create key from the dialog
    
    Once you have the API key, create a `.env.local` file and save your API key:
    
    .env.local
    
    ```
    AI_GATEWAY_API_KEY=your_ai_gateway_api_key
    ```
    
    Instead of using an API key, you can use [OIDC tokens](/docs/ai-gateway/authentication#oidc-token-authentication) to authenticate your requests.
    
    The AI Gateway provider will default to using the `AI_GATEWAY_API_KEY` environment variable.
    
4.  ### [Create and run your script](#create-and-run-your-script)
    
    Create an `index.ts` file in the root of your project and add the following code:
    
    index.ts
    
    ```
    import { streamText } from 'ai';
    import 'dotenv/config';
     
    async function main() {
      const result = streamText({
        model: 'openai/gpt-5',
        prompt: 'Invent a new holiday and describe its traditions.',
      });
     
      for await (const textPart of result.textStream) {
        process.stdout.write(textPart);
      }
     
      console.log();
      console.log('Token usage:', await result.usage);
      console.log('Finish reason:', await result.finishReason);
    }
     
    main().catch(console.error);
    ```
    
    Now, run your script:
    
    terminal
    
    ```
    pnpm tsx index.ts
    ```
    
    You should see the AI model's response to your prompt.
    
5.  ### [Next steps](#next-steps)
    
    Continue with the [AI SDK documentation](https://ai-sdk.dev/getting-started) to learn advanced configuration, set up [provider and model routing with fallbacks](/docs/ai-gateway/provider-options), and explore more integration examples.
    

## [Using OpenAI SDK](#using-openai-sdk)

The AI Gateway provides OpenAI-compatible API endpoints that allow you to use existing OpenAI client libraries and tools with the AI Gateway.

The OpenAI-compatible API includes:

*   Model Management: List and retrieve the available models
*   Chat Completions: Create chat completions that support streaming, images, and file attachments
*   Tool Calls: Call functions with automatic or explicit tool selection
*   Existing Tool Integration: Use your existing OpenAI client libraries and tools without needing modifications

Learn more about using the OpenAI SDK with the AI Gateway in the [OpenAI-Compatible API page](/docs/ai-gateway/openai-compat).

## [Using other community frameworks](#using-other-community-frameworks)

The AI Gateway is designed to work with any framework that supports the OpenAI API or AI SDK 5.

Read more about using the AI Gateway with other community frameworks in the [framework integrations](/docs/ai-gateway/framework-integrations) section.

--------------------------------------------------------------------------------
title: "Image Generation"
description: "Generate and edit images using AI models through Vercel AI Gateway with support for multiple providers and modalities."
last_updated: "null"
source: "https://vercel.com/docs/ai-gateway/image-generation"
--------------------------------------------------------------------------------

# Image Generation

Copy page

Ask AI about this page

Last updated October 21, 2025

AI Gateway supports image generation and editing capabilities. You can generate new images from text prompts, edit existing images, and create variations with natural language instructions.

You can view all available models that support image generation by using the Image filter at the [AI Gateway Models page](https://vercel.com/ai-gateway/models).

## [Google Gemini 2.5 Flash Image](#google-gemini-2.5-flash-image)

Google's [Gemini 2.5 Flash Image model](https://developers.googleblog.com/en/introducing-gemini-2-5-flash-image/) offers state-of-the-art image generation and editing capabilities. This model supports [specifying response modalities](https://ai-sdk.dev/providers/ai-sdk-providers/google-generative-ai#image-outputs) to enable image outputs alongside text responses. Find details on this model in the [Model Library](https://vercel.com/ai-gateway/models/gemini-2.5-flash-image-preview).

## [Basic image generation](#basic-image-generation)

Generate images from text prompts using the `generateText` or `streamText` functions with appropriate provider options.

TypeScript (generateText)TypeScript (streamText)

generate-image.ts

```
import 'dotenv/config';
import { generateText } from 'ai';
import fs from 'node:fs';
import path from 'node:path';
 
async function main() {
  const result = await generateText({
    model: 'google/gemini-2.5-flash-image-preview',
    providerOptions: {
      google: { responseModalities: ['TEXT', 'IMAGE'] },
    },
    prompt:
      'Render two versions of a pond tortoise sleeping on a log in a lake at sunset.',
  });
 
  if (result.text) {
    console.log(result.text);
  }
 
  // Save generated images to local filesystem
  const imageFiles = result.files.filter((f) =>
    f.mediaType?.startsWith('image/'),
  );
 
  if (imageFiles.length > 0) {
    // Create output directory if it doesn't exist
    const outputDir = 'output';
    fs.mkdirSync(outputDir, { recursive: true });
 
    const timestamp = Date.now();
 
    for (const [index, file] of imageFiles.entries()) {
      const extension = file.mediaType?.split('/')[1] || 'png';
      const filename = `image-${timestamp}-${index}.${extension}`;
      const filepath = path.join(outputDir, filename);
 
      await fs.promises.writeFile(filepath, file.uint8Array);
      console.log(`Saved image to ${filepath}`);
    }
  }
 
  console.log();
  console.log('Usage: ', JSON.stringify(result.usage, null, 2));
  console.log(
    'Provider metadata: ',
    JSON.stringify(result.providerMetadata, null, 2),
  );
}
 
main().catch(console.error);
```

stream-image.ts

```
import 'dotenv/config';
import { streamText } from 'ai';
import fs from 'node:fs';
import path from 'node:path';
 
async function main() {
  const result = streamText({
    model: 'google/gemini-2.5-flash-image-preview',
    providerOptions: {
      google: { responseModalities: ['TEXT', 'IMAGE'] },
    },
    prompt: 'Render a pond tortoise sleeping on a log in a lake at sunset.',
  });
 
  // Create output directory if it doesn't exist
  const outputDir = 'output';
  fs.mkdirSync(outputDir, { recursive: true });
  const timestamp = Date.now();
  let imageIndex = 0;
 
  for await (const delta of result.fullStream) {
    switch (delta.type) {
      case 'text-delta': {
        process.stdout.write(delta.text);
        break;
      }
 
      case 'file': {
        if (delta.file.mediaType.startsWith('image/')) {
          console.log();
 
          const extension = delta.file.mediaType?.split('/')[1] || 'png';
          const filename = `image-${timestamp}-${imageIndex}.${extension}`;
          const filepath = path.join(outputDir, filename);
 
          await fs.promises.writeFile(filepath, delta.file.uint8Array);
          console.log(`Saved image to ${filepath}`);
          imageIndex++;
        }
        break;
      }
    }
  }
  process.stdout.write('\n\n');
 
  console.log();
  console.log('Finish reason: ', result.finishReason);
  console.log('Usage: ', JSON.stringify(await result.usage, null, 2));
  console.log(
    'Provider metadata: ',
    JSON.stringify(await result.providerMetadata, null, 2),
  );
}
 
main().catch(console.error);
```

## [Use images as input](#use-images-as-input)

Provide existing images as input to edit images, combine images, or create variations of existing content.

use-images-as-input.ts

```
import { generateText } from 'ai';
import fs from 'node:fs';
 
const result = await generateText({
  model: 'google/gemini-2.5-flash-image-preview',
  providerOptions: {
    google: { responseModalities: ['TEXT', 'IMAGE'] },
  },
  messages: [
    {
      role: 'user',
      content: [
        {
          type: 'text',
          text: 'Combine these two images into one artistic composition.',
        },
        {
          type: 'file',
          mediaType: 'image/png',
          data: fs.readFileSync('/path/to/your/first-image.png'),
        },
        {
          type: 'file',
          mediaType: 'image/jpeg',
          data: fs.readFileSync('/path/to/your/second-image.jpg'),
        },
      ],
    },
  ],
});
```

Check the [AI SDK provider documentation](https://ai-sdk.dev/providers/ai-sdk-providers) for more on provider/model-specific image generation configuration.

For OpenAI-compatible API usage with image generation, see the [OpenAI-Compatible API Image Generation section](/docs/ai-gateway/openai-compat#image-generation).

## [OpenAI-compatible API response format](#openai-compatible-api-response-format)

When using the OpenAI-compatible API (`/v1/chat/completions`) for image generation, responses follow a specific format that separates text content from generated images:

### [Response structure](#response-structure)

```
{
  "id": "chatcmpl-123",
  "object": "chat.completion",
  "created": 1677652288,
  "model": "google/gemini-2.5-flash-image-preview",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "I've generated a beautiful sunset image for you.",
        "images": [
          {
            "type": "image_url",
            "image_url": {
              "url": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAA..."
            }
          }
        ]
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 15,
    "completion_tokens": 28,
    "total_tokens": 43
  }
}
```

### [Key format details](#key-format-details)

*   `content`: Contains the text description as a string
*   `images`: Array of generated images, each with:
    *   `type`: Always `"image_url"`
    *   `image_url.url`: Base64-encoded data URI of the generated image

### [Streaming responses](#streaming-responses)

For streaming requests, images are delivered in delta chunks:

```
{
  "id": "chatcmpl-123",
  "object": "chat.completion.chunk",
  "created": 1677652288,
  "model": "google/gemini-2.5-flash-image-preview",
  "choices": [
    {
      "index": 0,
      "delta": {
        "images": [
          {
            "type": "image_url",
            "image_url": {
              "url": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAA..."
            }
          }
        ]
      },
      "finish_reason": null
    }
  ]
}
```

## [Handling generated images](#handling-generated-images)

Generated images are returned as `GeneratedFile` objects in the `result.files` array. Each contains:

*   `base64`: The file as a base 64 data string
*   `uint8Array`: The file as a `Uint8Array`
*   `mediaType`: The MIME type (e.g., `image/png`, `image/jpeg`)

## [Streaming image generation](#streaming-image-generation)

When using `streamText`, images are delivered through `fullStream` as `file` events:

```
for await (const delta of result.fullStream) {
  switch (delta.type) {
    case 'text-delta':
      // Handle text chunks
      process.stdout.write(delta.text);
      break;
 
    case 'file':
      // Handle generated files (images)
      if (delta.file.mediaType.startsWith('image/')) {
        await saveImage(delta.file);
      }
      break;
  }
}
```

--------------------------------------------------------------------------------
title: "Model Variants"
description: "Enable provider-specific capabilities (like Anthropic 1M context) via headers when calling models through AI Gateway."
last_updated: "null"
source: "https://vercel.com/docs/ai-gateway/model-variants"
--------------------------------------------------------------------------------

# Model Variants

Copy page

Ask AI about this page

Last updated October 21, 2025

Some AI inference providers offer special variants of models. These models can have different features such as a larger context size. They may incur different costs associated with requests as well.

When AI Gateway makes these models available they will be highlighted on the model detail page with a Model Variants section in the relevant provider card providing an overview of the feature set and linking to more detail.

Model variants sometimes rely on preview or beta features offered by the inference provider. Their ongoing availability can therefore be less predictable than that of a stable model feature. Check the provider's site for the latest information.

### [Anthropic Claude Sonnet 4: 1M token context (beta)](#anthropic-claude-sonnet-4:-1m-token-context-beta)

Enable with header `anthropic-beta: context-1m-2025-08-07`.

*   Learn more: [Announcement](https://www.anthropic.com/news/1m-context), [Context windows docs](https://docs.anthropic.com/en/docs/build-with-claude/context-windows#1m-token-context-window)
*   Pricing (summary): If total input tokens (prompt + cache reads/writes) exceed 200K, input is charged 2× and output 1.5×; otherwise standard rates apply. See [pricing details](https://docs.anthropic.com/en/docs/about-claude/pricing#long-context-pricing).

TypeScript (AI SDK)TypeScript (OpenAI)Python (OpenAI)

ai-sdk.ts

```
import { streamText } from 'ai';
import { largePrompt } from './largePrompt.ts';
 
const result = streamText({
  headers: {
    'anthropic-beta': 'context-1m-2025-08-07',
  },
  model: 'anthropic/claude-sonnet-4',
  prompt: `You have a big brain. Summarize into 3 sentences: ${largePrompt}`,
  providerOptions: {
    gateway: { only: ['anthropic'] },
  },
});
 
for await (const part of result.textStream) {
  process.stdout.write(part);
}
// Log final chunk with provider metadata detail.
console.log(JSON.stringify(await result.providerMetadata, null, 2));
```

openai.ts

```
import OpenAI from 'openai';
import { largePrompt } from './largePrompt.ts';
 
const openai = new OpenAI({
  apiKey: process.env.AI_GATEWAY_API_KEY,
  baseURL: 'https://ai-gateway.vercel.sh/v1',
});
 
// @ts-expect-error
const stream = await openai.chat.completions.create(
  {
    model: 'anthropic/claude-sonnet-4',
    messages: [
      {
        role: 'user',
        content: `You have a big brain. Summarize into 3 sentences: ${largePrompt}`,
      },
    ],
    stream: true,
    providerOptions: {
      gateway: { only: ['anthropic'] },
    },
  },
  {
    headers: {
      'anthropic-beta': 'context-1m-2025-08-07',
    },
  },
);
 
for await (const chunk of stream) {
  const content = chunk.choices[0]?.delta?.content;
  if (content) {
    process.stdout.write(content);
  } else {
    // Log final chunk with provider metadata detail.
    console.log(JSON.stringify(chunk, null, 2));
  }
}
```

openai.py

```
import json
import os
from openai import OpenAI
 
client = OpenAI(
  api_key=os.getenv('AI_GATEWAY_API_KEY'),
  base_url='https://ai-gateway.vercel.sh/v1'
)
large_prompt = 'your-large-prompt'
 
stream = client.chat.completions.create(
    model='anthropic/claude-sonnet-4',
    messages=[
        {
            'role': 'user',
            'content': f'You have a big brain. Summarize into 3 sentences: {large_prompt}',
        },
    ],
    extra_headers={
        'anthropic-beta': 'context-1m-2025-08-07',
    },
    stream=True
)
 
for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end='', flush=True)
    # Log final chunk with provider metadata detail.
    if chunk.choices[0].finish_reason and hasattr(chunk.choices[0].delta, 'provider_metadata') and chunk.choices[0].delta.provider_metadata:
        print('\nProvider metadata:')
        print(json.dumps(
            chunk.choices[0].delta.provider_metadata, indent=2))
```

--------------------------------------------------------------------------------
title: "Models & Providers"
description: "Learn about models and providers for the AI Gateway."
last_updated: "null"
source: "https://vercel.com/docs/ai-gateway/models-and-providers"
--------------------------------------------------------------------------------

# Models & Providers

Copy page

Ask AI about this page

Last updated October 23, 2025

The AI Gateway's unified API is built to be flexible, allowing you to switch between [different AI models](https://vercel.com/ai-gateway/models) and providers without rewriting parts of your application. This is useful for testing different models or when you want to change the underlying AI provider for cost or performance reasons. You can also configure [provider routing and model fallbacks](/docs/ai-gateway/provider-options) to ensure high availability and reliability.

To view the list of supported models and providers, check out the [AI Gateway models page](https://vercel.com/ai-gateway/models).

### [What are models and providers?](#what-are-models-and-providers)

Models are AI algorithms that process your input data to generate responses, such as [Grok](https://docs.x.ai/docs/models), [GPT-5](https://platform.openai.com/docs/models/gpt-5), or [Claude Sonnet 4](https://www.anthropic.com/claude/sonnet). Providers are the companies or services that host these models, such as [xAI](https://x.ai), [OpenAI](https://openai.com), or [Anthropic](https://anthropic.com).

In some cases, multiple providers, including the model creator, host the same model. For example, you can use the `xai/grok-4` model from [xAI](https://x.ai/) or the `openai/gpt-5` model from [OpenAI](https://openai.com), following the format `creator/model-name`.

Different providers may have different specifications for the same model such as different pricing and performance. You can choose the one that best fits your needs.

You can view the list of supported models and providers by following these steps:

1.  Go to the [AI Gateway tab](https://vercel.com/d?to=%2F%5Bteam%5D%2F%7E%2Fai&title=Go+to+AI+Gateway) in your Vercel dashboard.
2.  Click on the Model List section on the left sidebar.

### [Specifying the model](#specifying-the-model)

There are two ways to specify the model and provider to use for an AI Gateway request:

*   [As part of an AI SDK function call](#as-part-of-an-ai-sdk-function-call)
*   [Globally for all requests in your application](#globally-for-all-requests-in-your-application)

#### [As part of an AI SDK function call](#as-part-of-an-ai-sdk-function-call)

In the AI SDK, you can specify the model and provider directly in your API calls using either plain strings or the AI Gateway provider. This allows you to switch models or providers for specific requests without affecting the rest of your application.

To use AI Gateway, specify a model and provider via a plain string, for example:

app/api/chat/route.ts

```
import { generateText } from 'ai';
import { NextRequest } from 'next/server';
 
export async function GET() {
  const result = await generateText({
    model: 'xai/grok-3',
    prompt: 'Tell me the history of the San Francisco Mission-style burrito.',
  });
  return Response.json(result);
}
```

You can test different models by changing the `model` parameter and opening your browser to `http://localhost:3000/api/chat`.

You can also use a provider instance. This can be useful if you'd like to create models to use with a [custom provider](https://ai-sdk.dev/docs/ai-sdk-core/provider-management#custom-providers) or if you'd like to use a Gateway provider with the AI SDK [Provider Registry](https://v5.ai-sdk.dev/docs/ai-sdk-core/provider-management#provider-registry).

Install the `@ai-sdk/gateway` package directly as a dependency in your project.

terminal

```
pnpm install @ai-sdk/gateway
```

You can change the model by changing the string passed to `gateway()`.

app/api/chat/route.ts

```
import { generateText } from 'ai';
import { gateway } from '@ai-sdk/gateway';
import { NextRequest } from 'next/server';
 
export async function GET() {
  const result = await generateText({
    model: gateway('xai/grok-3'),
    prompt: 'Tell me the history of the San Francisco Mission-style burrito.',
  });
  return Response.json(result);
}
```

The example above uses the default `gateway` provider instance. You can also create a custom provider instance to use in your application. Creating a custom instance is useful when you need to specify a different environment variable for your API key, or when you need to set a custom base URL (for example, if you're working behind a corporate proxy server).

app/api/chat/route.ts

```
import { generateText } from 'ai';
import { createGateway } from '@ai-sdk/gateway';
 
const gateway = createGateway({
  apiKey: process.env.AI_GATEWAY_API_KEY, // the default environment variable for the API key
  baseURL: 'https://ai-gateway.vercel.sh/v1/ai', // the default base URL
});
 
export async function GET() {
  const result = await generateText({
    model: gateway('xai/grok-3'),
    prompt: 'Why is the sky blue?',
  });
  return Response.json(result);
}
```

#### [Globally for all requests in your application](#globally-for-all-requests-in-your-application)

The Vercel AI Gateway is the default provider for the AI SDK when a model is specified as a string. You can set a different provider as the default by assigning the provider instance to the `globalThis.AI_SDK_DEFAULT_PROVIDER` variable.

This is intended to be done in a file that runs before any other AI SDK calls. In the case of a Next.js application, you can do this in [`instrumentation.ts`](https://nextjs.org/docs/app/guides/instrumentation):

instrumentation.ts

```
import { openai } from '@ai-sdk/openai';
 
export async function register() {
  // This runs once when the Node.js runtime starts
  globalThis.AI_SDK_DEFAULT_PROVIDER = openai;
 
  // You can also do other initialization here
  console.log('App initialization complete');
}
```

Then, you can use the `generateText` function without specifying the provider in each call.

app/api/chat/route.ts

```
import { generateText } from 'ai';
import { NextRequest } from 'next/server';
 
export async function GET(request: NextRequest) {
  const { searchParams } = new URL(request.url);
  const prompt = searchParams.get('prompt');
 
  if (!prompt) {
    return Response.json({ error: 'Prompt is required' }, { status: 400 });
  }
 
  const result = await generateText({
    model: 'openai/gpt-5',
    prompt,
  });
 
  return Response.json(result);
}
```

### [Embedding models](#embedding-models)

Generate vector embeddings for semantic search, similarity matching, and retrieval-augmented generation (RAG).

#### [Single value](#single-value)

app/api/embed/route.ts

```
import { embed } from 'ai';
 
export async function GET() {
  const result = await embed({
    model: 'openai/text-embedding-3-small',
    value: 'Sunny day at the beach',
  });
 
  return Response.json(result);
}
```

#### [Multiple values](#multiple-values)

app/api/embed/route.ts

```
import { embedMany } from 'ai';
 
export async function GET() {
  const result = await embedMany({
    model: 'openai/text-embedding-3-small',
    values: ['Sunny day at the beach', 'Cloudy city skyline'],
  });
 
  return Response.json(result);
}
```

#### [Gateway provider instance](#gateway-provider-instance)

Alternatively, if you're using the Gateway provider instance, specify embedding models with `gateway.textEmbeddingModel(...)`.

app/api/embed/route.ts

```
import { embed } from 'ai';
import { gateway } from '@ai-sdk/gateway';
 
export async function GET() {
  const result = await embed({
    model: gateway.textEmbeddingModel('openai/text-embedding-3-small'),
    value: 'Sunny day at the beach',
  });
 
  return Response.json(result);
}
```

### [Dynamic model discovery](#dynamic-model-discovery)

The `getAvailableModels` function retrieves detailed information about all models configured for the `gateway` provider, including each model's `id`, `name`, `description`, and `pricing` details.

app/api/chat/route.ts

```
import { gateway } from '@ai-sdk/gateway';
import { generateText } from 'ai';
 
const availableModels = await gateway.getAvailableModels();
 
availableModels.models.forEach((model) => {
  console.log(`${model.id}: ${model.name}`);
  if (model.description) {
    console.log(`  Description: ${model.description}`);
  }
  if (model.pricing) {
    console.log(`  Input: $${model.pricing.input}/token`);
    console.log(`  Output: $${model.pricing.output}/token`);
    if (model.pricing.cachedInputTokens) {
      console.log(
        `  Cached input (read): $${model.pricing.cachedInputTokens}/token`,
      );
    }
    if (model.pricing.cacheCreationInputTokens) {
      console.log(
        `  Cache creation (write): $${model.pricing.cacheCreationInputTokens}/token`,
      );
    }
  }
});
 
const { text } = await generateText({
  model: availableModels.models[0].id, // e.g., 'openai/gpt-5'
  prompt: 'Hello world',
});
```

#### [Filtering models by type](#filtering-models-by-type)

You can filter the available models by their type (e.g., to separate language models from embedding models) using the `modelType` property:

app/api/models/route.ts

```
import { gateway } from '@ai-sdk/gateway';
 
const { models } = await gateway.getAvailableModels();
const textModels = models.filter((m) => m.modelType === 'language');
const embeddingModels = models.filter((m) => m.modelType === 'embedding');
 
console.log(
  'Language models:',
  textModels.map((m) => m.id),
);
console.log(
  'Embedding models:',
  embeddingModels.map((m) => m.id),
);
```

--------------------------------------------------------------------------------
title: "Observability"
description: "Learn how to monitor and debug your AI Gateway requests."
last_updated: "null"
source: "https://vercel.com/docs/ai-gateway/observability"
--------------------------------------------------------------------------------

# Observability

Copy page

Ask AI about this page

Last updated October 21, 2025

The AI Gateway logs observability metrics related to your requests, which you can use to monitor and debug.

You can view these [metrics](#metrics):

*   [The Observability tab in your Vercel dashboard](#observability-tab)
*   [The AI Gateway tab in your Vercel dashboard](#ai-gateway-tab)

## [Observability tab](#observability-tab)

You can access these metrics from the Observability tab of your Vercel dashboard by clicking AI Gateway on the left side of the Observability Overview page

![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fai-gateway%2Flrhvrkgfsmh7lkqbzbgi.png&w=3840&q=75)![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fai-gateway%2Fh3eofbxma8gjfjfmiaac.png&w=3840&q=75)

### [Team scope](#team-scope)

When you access the AI Gateway section of the Observability tab under the [team scope](/docs/dashboard-features#scope-selector), you can view the metrics for all requests made to the AI Gateway across all projects in your team. This is useful for monitoring the overall usage and performance of the AI Gateway.

![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fai-gateway%2Frrectrxazvow2qvkcusn.png&w=3840&q=75)![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fai-gateway%2Feefy948y9bt3byjccsdx.png&w=3840&q=75)

### [Project scope](#project-scope)

When you access the AI Gateway section of the Observability tab for a specific project, you can view metrics for all requests to the AI Gateway for that project.

![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fai-gateway%2Fjfvdu3ac3bgyg4cobrs7.png&w=3840&q=75)![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fai-gateway%2Fibp9anutc5p7ussyotir.png&w=3840&q=75)

## [AI Gateway tab](#ai-gateway-tab)

You can also access these metrics by clicking the AI Gateway tab of your Vercel dashboard under the team scope. You can see a recent overview of the requests made to the AI Gateway in the Activity section.

![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fai-gateway%2Fpgvk5xxep9zwsvl1ygm3.png&w=3840&q=75)![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fai-gateway%2Fsntkvarxttyl5trdmlhb.png&w=3840&q=75)

## [Metrics](#metrics)

### [Requests by Model](#requests-by-model)

The Requests by Model chart shows the number of requests made to each model over time. This can help you identify which models are being used most frequently and whether there are any spikes in usage.

### [Time to First Token (TTFT)](#time-to-first-token-ttft)

The Time to First Token chart shows the average time it takes for the AI Gateway to return the first token of a response. This can help you understand the latency of your requests and identify any performance issues.

### [Input/output Token Counts](#input/output-token-counts)

The Input/output Token Counts chart shows the number of input and output tokens for each request. This can help you understand the size of the requests being made and the responses being returned.

### [Spend](#spend)

The Spend chart shows the total amount spent on AI Gateway requests over time. This can help you monitor your spending and identify any unexpected costs.

--------------------------------------------------------------------------------
title: "OpenAI-Compatible API"
description: "Use OpenAI-compatible API endpoints with the AI Gateway for seamless integration with existing tools and libraries."
last_updated: "null"
source: "https://vercel.com/docs/ai-gateway/openai-compat"
--------------------------------------------------------------------------------

# OpenAI-Compatible API

Copy page

Ask AI about this page

Last updated October 23, 2025

AI Gateway provides OpenAI-compatible API endpoints, letting you use multiple AI providers through a familiar interface. You can use existing OpenAI client libraries, switch to the AI Gateway with a URL change, and keep your current tools and workflows without code rewrites.

The OpenAI-compatible API implements the same specification as the [OpenAI API](https://platform.openai.com/docs/api-reference/chat).

## [Base URL](#base-url)

The OpenAI-compatible API is available at the following base URL:

`https://ai-gateway.vercel.sh/v1`

## [Authentication](#authentication)

The OpenAI-compatible API supports the same authentication methods as the main AI Gateway:

*   API key: Use your AI Gateway API key with the `Authorization: Bearer <token>` header
*   OIDC token: Use your Vercel OIDC token with the `Authorization: Bearer <token>` header

You only need to use one of these forms of authentication. If an API key is specified it will take precedence over any OIDC token, even if the API key is invalid.

## [Supported endpoints](#supported-endpoints)

The AI Gateway supports the following OpenAI-compatible endpoints:

*   [`GET /models`](#list-models) - List available models
*   [`GET /models/{model}`](#retrieve-model) - Retrieve a specific model
*   [`POST /chat/completions`](#chat-completions) - Create chat completions with support for streaming, attachments, tool calls, and image generation
*   [`POST /embeddings`](#embeddings) - Generate vector embeddings

## [Integration with existing tools](#integration-with-existing-tools)

You can use the AI Gateway's OpenAI-compatible API with existing tools and libraries like the [OpenAI client libraries](https://platform.openai.com/docs/libraries) and [AI SDK 4](https://v4.ai-sdk.dev/). Point your existing client to the AI Gateway's base URL and use your AI Gateway [API key](/docs/ai-gateway/authentication#api-key) or [OIDC token](/docs/ai-gateway/authentication#oidc-token) for authentication.

### [OpenAI client libraries](#openai-client-libraries)

TypeScriptPython

client.ts

```
import OpenAI from 'openai';
 
const openai = new OpenAI({
  apiKey: process.env.AI_GATEWAY_API_KEY,
  baseURL: 'https://ai-gateway.vercel.sh/v1',
});
 
const response = await openai.chat.completions.create({
  model: 'anthropic/claude-sonnet-4',
  messages: [{ role: 'user', content: 'Hello, world!' }],
});
```

client.py

```
import os
from openai import OpenAI
 
client = OpenAI(
    api_key=os.getenv('AI_GATEWAY_API_KEY'),
    base_url='https://ai-gateway.vercel.sh/v1'
)
 
response = client.chat.completions.create(
    model='anthropic/claude-sonnet-4',
    messages=[
        {'role': 'user', 'content': 'Hello, world!'}
    ]
)
```

### [AI SDK 4](#ai-sdk-4)

For compatibility with [AI SDK v4](https://v4.ai-sdk.dev/) and AI Gateway, install the [@ai-sdk/openai-compatible](https://ai-sdk.dev/providers/openai-compatible-providers) package.

Verify that you are using AI SDK 4 by using the following package versions: `@ai-sdk/openai-compatible` version `<1.0.0` (e.g., `0.2.16`) and `ai` version `<5.0.0` (e.g., `4.3.19`).

TypeScript

client.ts

```
import { createOpenAICompatible } from '@ai-sdk/openai-compatible';
import { generateText } from 'ai';
 
const gateway = createOpenAICompatible({
  name: 'openai',
  apiKey: process.env.AI_GATEWAY_API_KEY,
  baseURL: 'https://ai-gateway.vercel.sh/v1',
});
 
const response = await generateText({
  model: gateway('anthropic/claude-sonnet-4'),
  prompt: 'Hello, world!',
});
```

## [List models](#list-models)

Retrieve a list of all available models that can be used with the AI Gateway.

Endpoint

`GET /models`

Example request

TypeScriptPython

list-models.ts

```
import OpenAI from 'openai';
 
const openai = new OpenAI({
  apiKey: process.env.AI_GATEWAY_API_KEY,
  baseURL: 'https://ai-gateway.vercel.sh/v1',
});
 
const models = await openai.models.list();
console.log(models);
```

list-models.py

```
import os
from openai import OpenAI
 
client = OpenAI(
    api_key=os.getenv('AI_GATEWAY_API_KEY'),
    base_url='https://ai-gateway.vercel.sh/v1'
)
 
models = client.models.list()
print(models)
```

Response format

The response follows the OpenAI API format:

```
{
  "object": "list",
  "data": [
    {
      "id": "anthropic/claude-sonnet-4",
      "object": "model",
      "created": 1677610602,
      "owned_by": "anthropic"
    },
    {
      "id": "openai/gpt-4.1-mini",
      "object": "model",
      "created": 1677610602,
      "owned_by": "openai"
    }
  ]
}
```

## [Retrieve model](#retrieve-model)

Retrieve details about a specific model.

Endpoint

`GET /models/{model}`

Parameters

*   `model` (required): The model ID to retrieve (e.g., `anthropic/claude-sonnet-4`)

Example request

TypeScriptPython

retrieve-model.ts

```
import OpenAI from 'openai';
 
const openai = new OpenAI({
  apiKey: process.env.AI_GATEWAY_API_KEY,
  baseURL: 'https://ai-gateway.vercel.sh/v1',
});
 
const model = await openai.models.retrieve('anthropic/claude-sonnet-4');
console.log(model);
```

retrieve-model.py

```
import os
from openai import OpenAI
 
client = OpenAI(
    api_key=os.getenv('AI_GATEWAY_API_KEY'),
    base_url='https://ai-gateway.vercel.sh/v1'
)
 
model = client.models.retrieve('anthropic/claude-sonnet-4')
print(model)
```

Response format

```
{
  "id": "anthropic/claude-sonnet-4",
  "object": "model",
  "created": 1677610602,
  "owned_by": "anthropic"
}
```

## [Chat completions](#chat-completions)

Create chat completions using various AI models available through the AI Gateway.

Endpoint

`POST /chat/completions`

### [Basic chat completion](#basic-chat-completion)

Create a non-streaming chat completion.

Example request

TypeScriptPython

chat-completion.ts

```
import OpenAI from 'openai';
 
const apiKey = process.env.AI_GATEWAY_API_KEY || process.env.VERCEL_OIDC_TOKEN;
 
const openai = new OpenAI({
  apiKey,
  baseURL: 'https://ai-gateway.vercel.sh/v1',
});
 
const completion = await openai.chat.completions.create({
  model: 'anthropic/claude-sonnet-4',
  messages: [
    {
      role: 'user',
      content: 'Write a one-sentence bedtime story about a unicorn.',
    },
  ],
  stream: false,
});
 
console.log('Assistant:', completion.choices[0].message.content);
console.log('Tokens used:', completion.usage);
```

chat-completion.py

```
import os
from openai import OpenAI
 
api_key = os.getenv('AI_GATEWAY_API_KEY') or os.getenv('VERCEL_OIDC_TOKEN')
 
client = OpenAI(
    api_key=api_key,
    base_url='https://ai-gateway.vercel.sh/v1'
)
 
completion = client.chat.completions.create(
    model='anthropic/claude-sonnet-4',
    messages=[
        {
            'role': 'user',
            'content': 'Write a one-sentence bedtime story about a unicorn.'
        }
    ],
    stream=False,
)
 
print('Assistant:', completion.choices[0].message.content)
print('Tokens used:', completion.usage)
```

Response format

```
{
  "id": "chatcmpl-123",
  "object": "chat.completion",
  "created": 1677652288,
  "model": "anthropic/claude-sonnet-4",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Once upon a time, a gentle unicorn with a shimmering silver mane danced through moonlit clouds, sprinkling stardust dreams upon sleeping children below."
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 15,
    "completion_tokens": 28,
    "total_tokens": 43
  }
}
```

### [Streaming chat completion](#streaming-chat-completion)

Create a streaming chat completion that streams tokens as they are generated.

Example request

TypeScriptPython

streaming-chat.ts

```
import OpenAI from 'openai';
 
const apiKey = process.env.AI_GATEWAY_API_KEY || process.env.VERCEL_OIDC_TOKEN;
 
const openai = new OpenAI({
  apiKey,
  baseURL: 'https://ai-gateway.vercel.sh/v1',
});
 
const stream = await openai.chat.completions.create({
  model: 'anthropic/claude-sonnet-4',
  messages: [
    {
      role: 'user',
      content: 'Write a one-sentence bedtime story about a unicorn.',
    },
  ],
  stream: true,
});
 
for await (const chunk of stream) {
  const content = chunk.choices[0]?.delta?.content;
  if (content) {
    process.stdout.write(content);
  }
}
```

streaming-chat.py

```
import os
from openai import OpenAI
 
api_key = os.getenv('AI_GATEWAY_API_KEY') or os.getenv('VERCEL_OIDC_TOKEN')
 
client = OpenAI(
    api_key=api_key,
    base_url='https://ai-gateway.vercel.sh/v1'
)
 
stream = client.chat.completions.create(
    model='anthropic/claude-sonnet-4',
    messages=[
        {
            'role': 'user',
            'content': 'Write a one-sentence bedtime story about a unicorn.'
        }
    ],
    stream=True,
)
 
for chunk in stream:
    content = chunk.choices[0].delta.content
    if content:
        print(content, end='', flush=True)
```

#### [Streaming response format](#streaming-response-format)

Streaming responses are sent as [Server-Sent Events (SSE)](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events), a web standard for real-time data streaming over HTTP. Each event contains a JSON object with the partial response data.

The response format follows the OpenAI streaming specification:

```
data: {"id":"chatcmpl-123","object":"chat.completion.chunk","created":1677652288,"model":"anthropic/claude-sonnet-4","choices":[{"index":0,"delta":{"content":"Once"},"finish_reason":null}]}
 
data: {"id":"chatcmpl-123","object":"chat.completion.chunk","created":1677652288,"model":"anthropic/claude-sonnet-4","choices":[{"index":0,"delta":{"content":" upon"},"finish_reason":null}]}
 
data: [DONE]
```

Key characteristics:

*   Each line starts with `data:` followed by JSON
*   Content is delivered incrementally in the `delta.content` field
*   The stream ends with `data: [DONE]`
*   Empty lines separate events

SSE Parsing Libraries:

If you're building custom SSE parsing (instead of using the OpenAI SDK), these libraries can help:

*   JavaScript/TypeScript: [`eventsource-parser`](https://www.npmjs.com/package/eventsource-parser) - Robust SSE parsing with support for partial events
*   Python: [`httpx-sse`](https://pypi.org/project/httpx-sse/) - SSE support for HTTPX, or [`sseclient-py`](https://pypi.org/project/sseclient-py/) for requests

For more details about the SSE specification, see the [W3C specification](https://html.spec.whatwg.org/multipage/server-sent-events.html).

### [Image attachments](#image-attachments)

Send images as part of your chat completion request.

Example request

TypeScriptPython

image-analysis.ts

```
import fs from 'node:fs';
import OpenAI from 'openai';
 
const apiKey = process.env.AI_GATEWAY_API_KEY || process.env.VERCEL_OIDC_TOKEN;
 
const openai = new OpenAI({
  apiKey,
  baseURL: 'https://ai-gateway.vercel.sh/v1',
});
 
// Read the image file as base64
const imageBuffer = fs.readFileSync('./path/to/image.png');
const imageBase64 = imageBuffer.toString('base64');
 
const completion = await openai.chat.completions.create({
  model: 'anthropic/claude-sonnet-4',
  messages: [
    {
      role: 'user',
      content: [
        { type: 'text', text: 'Describe this image in detail.' },
        {
          type: 'image_url',
          image_url: {
            url: `data:image/png;base64,${imageBase64}`,
            detail: 'auto',
          },
        },
      ],
    },
  ],
  stream: false,
});
 
console.log('Assistant:', completion.choices[0].message.content);
console.log('Tokens used:', completion.usage);
```

image-analysis.py

```
import os
import base64
from openai import OpenAI
 
api_key = os.getenv('AI_GATEWAY_API_KEY') or os.getenv('VERCEL_OIDC_TOKEN')
 
client = OpenAI(
    api_key=api_key,
    base_url='https://ai-gateway.vercel.sh/v1'
)
 
# Read the image file as base64
with open('./path/to/image.png', 'rb') as image_file:
    image_base64 = base64.b64encode(image_file.read()).decode('utf-8')
 
completion = client.chat.completions.create(
    model='anthropic/claude-sonnet-4',
    messages=[
        {
            'role': 'user',
            'content': [
                {'type': 'text', 'text': 'Describe this image in detail.'},
                {
                    'type': 'image_url',
                    'image_url': {
                        'url': f'data:image/png;base64,{image_base64}',
                        'detail': 'auto'
                    }
                }
            ]
        }
    ],
    stream=False,
)
 
print('Assistant:', completion.choices[0].message.content)
print('Tokens used:', completion.usage)
```

### [PDF attachments](#pdf-attachments)

Send PDF documents as part of your chat completion request.

Example request

TypeScriptPython

pdf-analysis.ts

```
import fs from 'node:fs';
import OpenAI from 'openai';
 
const apiKey = process.env.AI_GATEWAY_API_KEY || process.env.VERCEL_OIDC_TOKEN;
 
const openai = new OpenAI({
  apiKey,
  baseURL: 'https://ai-gateway.vercel.sh/v1',
});
 
// Read the PDF file as base64
const pdfBuffer = fs.readFileSync('./path/to/document.pdf');
const pdfBase64 = pdfBuffer.toString('base64');
 
const completion = await openai.chat.completions.create({
  model: 'anthropic/claude-sonnet-4',
  messages: [
    {
      role: 'user',
      content: [
        {
          type: 'text',
          text: 'What is the main topic of this document? Please summarize the key points.',
        },
        {
          type: 'file',
          file: {
            data: pdfBase64,
            media_type: 'application/pdf',
            filename: 'document.pdf',
          },
        },
      ],
    },
  ],
  stream: false,
});
 
console.log('Assistant:', completion.choices[0].message.content);
console.log('Tokens used:', completion.usage);
```

pdf-analysis.py

```
import os
import base64
from openai import OpenAI
 
api_key = os.getenv('AI_GATEWAY_API_KEY') or os.getenv('VERCEL_OIDC_TOKEN')
 
client = OpenAI(
    api_key=api_key,
    base_url='https://ai-gateway.vercel.sh/v1'
)
 
# Read the PDF file as base64
with open('./path/to/document.pdf', 'rb') as pdf_file:
    pdf_base64 = base64.b64encode(pdf_file.read()).decode('utf-8')
 
completion = client.chat.completions.create(
    model='anthropic/claude-sonnet-4',
    messages=[
        {
            'role': 'user',
            'content': [
                {
                    'type': 'text',
                    'text': 'What is the main topic of this document? Please summarize the key points.'
                },
                {
                    'type': 'file',
                    'file': {
                        'data': pdf_base64,
                        'media_type': 'application/pdf',
                        'filename': 'document.pdf'
                    }
                }
            ]
        }
    ],
    stream=False,
)
 
print('Assistant:', completion.choices[0].message.content)
print('Tokens used:', completion.usage)
```

### [Tool calls](#tool-calls)

The AI Gateway supports OpenAI-compatible function calling, allowing models to call tools and functions. This follows the same specification as the [OpenAI Function Calling API](https://platform.openai.com/docs/guides/function-calling).

#### [Basic tool calls](#basic-tool-calls)

TypeScriptPython

tool-calls.ts

```
import OpenAI from 'openai';
 
const apiKey = process.env.AI_GATEWAY_API_KEY || process.env.VERCEL_OIDC_TOKEN;
 
const openai = new OpenAI({
  apiKey,
  baseURL: 'https://ai-gateway.vercel.sh/v1',
});
 
const tools: OpenAI.Chat.Completions.ChatCompletionTool[] = [
  {
    type: 'function',
    function: {
      name: 'get_weather',
      description: 'Get the current weather in a given location',
      parameters: {
        type: 'object',
        properties: {
          location: {
            type: 'string',
            description: 'The city and state, e.g. San Francisco, CA',
          },
          unit: {
            type: 'string',
            enum: ['celsius', 'fahrenheit'],
            description: 'The unit for temperature',
          },
        },
        required: ['location'],
      },
    },
  },
];
 
const completion = await openai.chat.completions.create({
  model: 'anthropic/claude-sonnet-4',
  messages: [
    {
      role: 'user',
      content: 'What is the weather like in San Francisco?',
    },
  ],
  tools: tools,
  tool_choice: 'auto',
  stream: false,
});
 
console.log('Assistant:', completion.choices[0].message.content);
console.log('Tool calls:', completion.choices[0].message.tool_calls);
```

tool-calls.py

```
import os
from openai import OpenAI
 
api_key = os.getenv('AI_GATEWAY_API_KEY') or os.getenv('VERCEL_OIDC_TOKEN')
 
client = OpenAI(
    api_key=api_key,
    base_url='https://ai-gateway.vercel.sh/v1'
)
 
tools = [
    {
        'type': 'function',
        'function': {
            'name': 'get_weather',
            'description': 'Get the current weather in a given location',
            'parameters': {
                'type': 'object',
                'properties': {
                    'location': {
                        'type': 'string',
                        'description': 'The city and state, e.g. San Francisco, CA'
                    },
                    'unit': {
                        'type': 'string',
                        'enum': ['celsius', 'fahrenheit'],
                        'description': 'The unit for temperature'
                    }
                },
                'required': ['location']
            }
        }
    }
]
 
completion = client.chat.completions.create(
    model='anthropic/claude-sonnet-4',
    messages=[
        {
            'role': 'user',
            'content': 'What is the weather like in San Francisco?'
        }
    ],
    tools=tools,
    tool_choice='auto',
    stream=False,
)
 
print('Assistant:', completion.choices[0].message.content)
print('Tool calls:', completion.choices[0].message.tool_calls)
```

Controlling tool selection: By default, `tool_choice` is set to `'auto'`, allowing the model to decide when to use tools. You can also:

*   Set to `'none'` to disable tool calls
*   Force a specific tool with: `tool_choice: { type: 'function', function: { name: 'your_function_name' } }`

#### [Tool call response format](#tool-call-response-format)

When the model makes tool calls, the response includes tool call information:

```
{
  "id": "chatcmpl-123",
  "object": "chat.completion",
  "created": 1677652288,
  "model": "anthropic/claude-sonnet-4",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": null,
        "tool_calls": [
          {
            "id": "call_123",
            "type": "function",
            "function": {
              "name": "get_weather",
              "arguments": "{\"location\": \"San Francisco, CA\", \"unit\": \"celsius\"}"
            }
          }
        ]
      },
      "finish_reason": "tool_calls"
    }
  ],
  "usage": {
    "prompt_tokens": 82,
    "completion_tokens": 18,
    "total_tokens": 100
  }
}
```

### [Structured outputs](#structured-outputs)

Generate structured JSON responses that conform to a specific schema, ensuring predictable and reliable data formats for your applications.

#### [JSON Schema format](#json-schema-format)

Use the OpenAI standard `json_schema` response format for the most robust structured output experience. This follows the official [OpenAI Structured Outputs specification](https://platform.openai.com/docs/guides/structured-outputs).

Example request

TypeScriptPython

structured-output-json-schema.ts

```
import OpenAI from 'openai';
 
const apiKey = process.env.AI_GATEWAY_API_KEY || process.env.VERCEL_OIDC_TOKEN;
 
const openai = new OpenAI({
  apiKey,
  baseURL: 'https://ai-gateway.vercel.sh/v1',
});
 
const completion = await openai.chat.completions.create({
  model: 'openai/gpt-5',
  messages: [
    {
      role: 'user',
      content: 'Create a product listing for a wireless gaming headset.',
    },
  ],
  stream: false,
  response_format: {
    type: 'json_schema',
    json_schema: {
      name: 'product_listing',
      description: 'A product listing with details and pricing',
      schema: {
        type: 'object',
        properties: {
          name: {
            type: 'string',
            description: 'Product name',
          },
          brand: {
            type: 'string',
            description: 'Brand name',
          },
          price: {
            type: 'number',
            description: 'Price in USD',
          },
          category: {
            type: 'string',
            description: 'Product category',
          },
          description: {
            type: 'string',
            description: 'Product description',
          },
          features: {
            type: 'array',
            items: { type: 'string' },
            description: 'Key product features',
          },
        },
        required: ['name', 'brand', 'price', 'category', 'description'],
        additionalProperties: false,
      },
    },
  },
});
 
console.log('Assistant:', completion.choices[0].message.content);
 
// Parse the structured response
const structuredData = JSON.parse(completion.choices[0].message.content);
console.log('Structured Data:', structuredData);
```

structured-output-json-schema.py

```
import os
import json
from openai import OpenAI
 
api_key = os.getenv('AI_GATEWAY_API_KEY') or os.getenv('VERCEL_OIDC_TOKEN')
 
client = OpenAI(
    api_key=api_key,
    base_url='https://ai-gateway.vercel.sh/v1'
)
 
completion = client.chat.completions.create(
    model='openai/gpt-5',
    messages=[
        {
            'role': 'user',
            'content': 'Create a product listing for a wireless gaming headset.'
        }
    ],
    stream=False,
    response_format={
        'type': 'json_schema',
        'json_schema': {
            'name': 'product_listing',
            'description': 'A product listing with details and pricing',
            'schema': {
                'type': 'object',
                'properties': {
                    'name': {
                        'type': 'string',
                        'description': 'Product name'
                    },
                    'brand': {
                        'type': 'string',
                        'description': 'Brand name'
                    },
                    'price': {
                        'type': 'number',
                        'description': 'Price in USD'
                    },
                    'category': {
                        'type': 'string',
                        'description': 'Product category'
                    },
                    'description': {
                        'type': 'string',
                        'description': 'Product description'
                    },
                    'features': {
                        'type': 'array',
                        'items': {'type': 'string'},
                        'description': 'Key product features'
                    }
                },
                'required': ['name', 'brand', 'price', 'category', 'description'],
                'additionalProperties': False
            },
        }
    }
)
 
print('Assistant:', completion.choices[0].message.content)
 
# Parse the structured response
structured_data = json.loads(completion.choices[0].message.content)
print('Structured Data:', json.dumps(structured_data, indent=2))
```

Response format

The response contains structured JSON that conforms to your specified schema:

```
{
  "id": "chatcmpl-123",
  "object": "chat.completion",
  "created": 1677652288,
  "model": "openai/gpt-5",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "{\"name\":\"SteelSeries Arctis 7P\",\"brand\":\"SteelSeries\",\"price\":149.99,\"category\":\"Gaming Headsets\",\"description\":\"Wireless gaming headset with 7.1 surround sound\",\"features\":[\"Wireless 2.4GHz\",\"7.1 Surround Sound\",\"24-hour battery\",\"Retractable microphone\"]}"
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 25,
    "completion_tokens": 45,
    "total_tokens": 70
  }
}
```

#### [JSON Schema parameters](#json-schema-parameters)

*   `type`: Must be `"json_schema"`
*   `json_schema`: Object containing schema definition
    *   `name` (required): Name of the response schema
    *   `description` (optional): Human-readable description of the expected output
    *   `schema` (required): Valid JSON Schema object defining the structure

#### [Legacy JSON format (alternative)](#legacy-json-format-alternative)

Legacy format: The following format is supported for backward compatibility. For new implementations, use the `json_schema` format above.

TypeScriptPython

structured-output-legacy.ts

```
import OpenAI from 'openai';
 
const apiKey = process.env.AI_GATEWAY_API_KEY || process.env.VERCEL_OIDC_TOKEN;
 
const openai = new OpenAI({
  apiKey,
  baseURL: 'https://ai-gateway.vercel.sh/v1',
});
 
const completion = await openai.chat.completions.create({
  model: 'openai/gpt-5',
  messages: [
    {
      role: 'user',
      content: 'Create a product listing for a wireless gaming headset.',
    },
  ],
  stream: false,
  // @ts-expect-error - Legacy format not in OpenAI types
  response_format: {
    type: 'json',
    name: 'product_listing',
    description: 'A product listing with details and pricing',
    schema: {
      type: 'object',
      properties: {
        name: { type: 'string', description: 'Product name' },
        brand: { type: 'string', description: 'Brand name' },
        price: { type: 'number', description: 'Price in USD' },
        category: { type: 'string', description: 'Product category' },
        description: { type: 'string', description: 'Product description' },
        features: {
          type: 'array',
          items: { type: 'string' },
          description: 'Key product features',
        },
      },
      required: ['name', 'brand', 'price', 'category', 'description'],
    },
  },
});
 
console.log('Assistant:', completion.choices[0].message.content);
```

structured-output-legacy.py

```
import os
import json
from openai import OpenAI
 
api_key = os.getenv('AI_GATEWAY_API_KEY') or os.getenv('VERCEL_OIDC_TOKEN')
 
client = OpenAI(
    api_key=api_key,
    base_url='https://ai-gateway.vercel.sh/v1'
)
 
completion = client.chat.completions.create(
    model='openai/gpt-5',
    messages=[
        {
            'role': 'user',
            'content': 'Create a product listing for a wireless gaming headset.'
        }
    ],
    stream=False,
    response_format={
        'type': 'json',
        'name': 'product_listing',
        'description': 'A product listing with details and pricing',
        'schema': {
            'type': 'object',
            'properties': {
                'name': {'type': 'string', 'description': 'Product name'},
                'brand': {'type': 'string', 'description': 'Brand name'},
                'price': {'type': 'number', 'description': 'Price in USD'},
                'category': {'type': 'string', 'description': 'Product category'},
                'description': {'type': 'string', 'description': 'Product description'},
                'features': {
                    'type': 'array',
                    'items': {'type': 'string'},
                    'description': 'Key product features'
                }
            },
            'required': ['name', 'brand', 'price', 'category', 'description']
        }
    }
)
 
print('Assistant:', completion.choices[0].message.content)
 
# Parse the structured response
structured_data = json.loads(completion.choices[0].message.content)
print('Structured Data:', json.dumps(structured_data, indent=2))
```

#### [Streaming with structured outputs](#streaming-with-structured-outputs)

Both `json_schema` and legacy `json` formats work with streaming responses:

TypeScriptPython

structured-streaming.ts

```
import OpenAI from 'openai';
 
const openai = new OpenAI({
  apiKey: process.env.AI_GATEWAY_API_KEY,
  baseURL: 'https://ai-gateway.vercel.sh/v1',
});
 
const stream = await openai.chat.completions.create({
  model: 'openai/gpt-5',
  messages: [
    {
      role: 'user',
      content: 'Create a product listing for a wireless gaming headset.',
    },
  ],
  stream: true,
  response_format: {
    type: 'json_schema',
    json_schema: {
      name: 'product_listing',
      description: 'A product listing with details and pricing',
      schema: {
        type: 'object',
        properties: {
          name: { type: 'string', description: 'Product name' },
          brand: { type: 'string', description: 'Brand name' },
          price: { type: 'number', description: 'Price in USD' },
          category: { type: 'string', description: 'Product category' },
          description: { type: 'string', description: 'Product description' },
          features: {
            type: 'array',
            items: { type: 'string' },
            description: 'Key product features',
          },
        },
        required: ['name', 'brand', 'price', 'category', 'description'],
        additionalProperties: false,
      },
    },
  },
});
 
let completeResponse = '';
for await (const chunk of stream) {
  const content = chunk.choices[0]?.delta?.content;
  if (content) {
    process.stdout.write(content);
    completeResponse += content;
  }
}
 
// Parse the complete structured response
const structuredData = JSON.parse(completeResponse);
console.log('\nParsed Product:', structuredData);
```

structured-streaming.py

```
import os
import json
from openai import OpenAI
 
client = OpenAI(
    api_key=os.getenv('AI_GATEWAY_API_KEY'),
    base_url='https://ai-gateway.vercel.sh/v1'
)
 
stream = client.chat.completions.create(
    model='openai/gpt-5',
    messages=[
        {
            'role': 'user',
            'content': 'Create a product listing for a wireless gaming headset.'
        }
    ],
    stream=True,
    response_format={
        'type': 'json_schema',
        'json_schema': {
            'name': 'product_listing',
            'description': 'A product listing with details and pricing',
            'schema': {
                'type': 'object',
                'properties': {
                    'name': {'type': 'string', 'description': 'Product name'},
                    'brand': {'type': 'string', 'description': 'Brand name'},
                    'price': {'type': 'number', 'description': 'Price in USD'},
                    'category': {'type': 'string', 'description': 'Product category'},
                    'description': {'type': 'string', 'description': 'Product description'},
                    'features': {
                        'type': 'array',
                        'items': {'type': 'string'},
                        'description': 'Key product features'
                    }
                },
                'required': ['name', 'brand', 'price', 'category', 'description'],
                'additionalProperties': False
            },
        }
    }
)
 
complete_response = ''
for chunk in stream:
    if chunk.choices and chunk.choices[0].delta.content:
        content = chunk.choices[0].delta.content
        print(content, end='', flush=True)
        complete_response += content
 
# Parse the complete structured response
structured_data = json.loads(complete_response)
print('\nParsed Product:', json.dumps(structured_data, indent=2))
```

Streaming assembly: When using structured outputs with streaming, you'll need to collect all the content chunks and parse the complete JSON response once the stream is finished.

### [Reasoning configuration](#reasoning-configuration)

Configure reasoning behavior for models that support extended thinking or chain-of-thought reasoning. The `reasoning` parameter allows you to control how reasoning tokens are generated and returned.

Example request

TypeScript (OpenAI SDK)TypeScript (fetch)Python

reasoning-openai-sdk.ts

```
import OpenAI from 'openai';
 
const apiKey = process.env.AI_GATEWAY_API_KEY || process.env.VERCEL_OIDC_TOKEN;
 
const openai = new OpenAI({
  apiKey,
  baseURL: 'https://ai-gateway.vercel.sh/v1',
});
 
// @ts-expect-error - reasoning parameter not yet in OpenAI types
const completion = await openai.chat.completions.create({
  model: 'anthropic/claude-sonnet-4',
  messages: [
    {
      role: 'user',
      content: 'What is the meaning of life? Think before answering.',
    },
  ],
  stream: false,
  reasoning: {
    max_tokens: 2000, // Limit reasoning tokens
    enabled: true, // Enable reasoning
  },
});
 
console.log('Reasoning:', completion.choices[0].message.reasoning);
console.log('Answer:', completion.choices[0].message.content);
console.log(
  'Reasoning tokens:',
  completion.usage.completion_tokens_details?.reasoning_tokens,
);
```

reasoning-fetch.ts

```
const apiKey = process.env.AI_GATEWAY_API_KEY || process.env.VERCEL_OIDC_TOKEN;
 
const response = await fetch(
  'https://ai-gateway.vercel.sh/v1/chat/completions',
  {
    method: 'POST',
    headers: {
      Authorization: `Bearer ${apiKey}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      model: 'anthropic/claude-sonnet-4',
      messages: [
        {
          role: 'user',
          content: 'What is the meaning of life? Think before answering.',
        },
      ],
      stream: false,
      reasoning: {
        max_tokens: 2000,
        enabled: true,
      },
    }),
  },
);
 
const completion = await response.json();
console.log('Reasoning:', completion.choices[0].message.reasoning);
console.log('Answer:', completion.choices[0].message.content);
```

reasoning.py

```
import os
from openai import OpenAI
 
api_key = os.getenv('AI_GATEWAY_API_KEY') or os.getenv('VERCEL_OIDC_TOKEN')
 
client = OpenAI(
    api_key=api_key,
    base_url='https://ai-gateway.vercel.sh/v1'
)
 
completion = client.chat.completions.create(
    model='anthropic/claude-sonnet-4',
    messages=[
        {
            'role': 'user',
            'content': 'What is the meaning of life? Think before answering.'
        }
    ],
    stream=False,
    extra_body={
        'reasoning': {
            'max_tokens': 2000,
            'enabled': True
        }
    }
)
 
print('Reasoning:', completion.choices[0].message.reasoning)
print('Answer:', completion.choices[0].message.content)
print('Reasoning tokens:', completion.usage.completion_tokens_details.reasoning_tokens)
```

#### [Reasoning parameters](#reasoning-parameters)

The `reasoning` object supports the following parameters:

*   `enabled` (boolean, optional): Enable reasoning output. When `true`, the model will provide its reasoning process.
*   `max_tokens` (number, optional): Maximum number of tokens to allocate for reasoning. This helps control costs and response times. Cannot be used with `effort`.
*   `effort` (string, optional): Control reasoning effort level. Accepts `'low'`, `'medium'`, or `'high'`. Cannot be used with `max_tokens`.
*   `exclude` (boolean, optional): When `true`, excludes reasoning content from the response but still generates it internally. Useful for reducing response payload size.

Mutually exclusive parameters: You cannot specify both `effort` and `max_tokens` in the same request. Choose one based on your use case.

#### [Response format with reasoning](#response-format-with-reasoning)

When reasoning is enabled, the response includes reasoning content:

```
{
  "id": "chatcmpl-123",
  "object": "chat.completion",
  "created": 1677652288,
  "model": "anthropic/claude-sonnet-4",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "The meaning of life is a deeply personal question...",
        "reasoning": "Let me think about this carefully. The question asks about..."
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 15,
    "completion_tokens": 150,
    "total_tokens": 165,
    "completion_tokens_details": {
      "reasoning_tokens": 50
    }
  }
}
```

#### [Streaming with reasoning](#streaming-with-reasoning)

Reasoning content is streamed incrementally in the `delta.reasoning` field:

TypeScriptPython

reasoning-streaming.ts

```
import OpenAI from 'openai';
 
const openai = new OpenAI({
  apiKey: process.env.AI_GATEWAY_API_KEY,
  baseURL: 'https://ai-gateway.vercel.sh/v1',
});
 
// @ts-expect-error - reasoning parameter not yet in OpenAI types
const stream = await openai.chat.completions.create({
  model: 'anthropic/claude-sonnet-4',
  messages: [
    {
      role: 'user',
      content: 'What is the meaning of life? Think before answering.',
    },
  ],
  stream: true,
  reasoning: {
    enabled: true,
  },
});
 
for await (const chunk of stream) {
  const delta = chunk.choices[0]?.delta;
 
  // Handle reasoning content
  if (delta?.reasoning) {
    process.stdout.write(`[Reasoning] ${delta.reasoning}`);
  }
 
  // Handle regular content
  if (delta?.content) {
    process.stdout.write(delta.content);
  }
}
```

reasoning-streaming.py

```
import os
from openai import OpenAI
 
client = OpenAI(
    api_key=os.getenv('AI_GATEWAY_API_KEY'),
    base_url='https://ai-gateway.vercel.sh/v1'
)
 
stream = client.chat.completions.create(
    model='anthropic/claude-sonnet-4',
    messages=[
        {
            'role': 'user',
            'content': 'What is the meaning of life? Think before answering.'
        }
    ],
    stream=True,
    extra_body={
        'reasoning': {
            'enabled': True
        }
    }
)
 
for chunk in stream:
    if chunk.choices and chunk.choices[0].delta:
        delta = chunk.choices[0].delta
 
        # Handle reasoning content
        if hasattr(delta, 'reasoning') and delta.reasoning:
            print(f"[Reasoning] {delta.reasoning}", end='', flush=True)
 
        # Handle regular content
        if hasattr(delta, 'content') and delta.content:
            print(delta.content, end='', flush=True)
```

#### [Preserving reasoning details across providers](#preserving-reasoning-details-across-providers)

The AI Gateway preserves reasoning details from models across interactions, normalizing the different formats used by OpenAI, Anthropic, and other providers into a consistent structure. This allows you to switch between models without rewriting your conversation management logic.

This is particularly useful during tool calling workflows where the model needs to resume its thought process after receiving tool results.

Controlling reasoning details

When `reasoning.enabled` is `true` (or when `reasoning.exclude` is not set), responses include a `reasoning_details` array alongside the standard `reasoning` text field. This structured field captures cryptographic signatures, encrypted content, and other verification data that providers include with their reasoning output.

Each detail object contains:

*   `type`: one or more of the below, depending on the provider and model
    *   `'reasoning.text'`: Contains the actual reasoning content as plain text in the `text` field. May include a `signature` field (Anthropic models) for cryptographic verification.
    *   `'reasoning.encrypted'`: Contains encrypted or redacted reasoning content in the `data` field. Used by OpenAI models when reasoning is protected, or by Anthropic models when thinking is redacted. Preserves the encrypted payload for verification purposes.
    *   `'reasoning.summary'`: Contains a condensed version of the reasoning process in the `summary` field. Used by OpenAI models to provide a readable summary alongside encrypted reasoning.
*   `id` (optional): Unique identifier for the reasoning block, used for tracking and correlation
*   `format`: Provider format identifier - `'openai-responses-v1'`, `'anthropic-claude-v1'`, or `'unknown'`
*   `index` (optional): Position in the reasoning sequence (for responses with multiple reasoning blocks)

Example response with reasoning details

For Anthropic models:

```
{
  "id": "chatcmpl-123",
  "object": "chat.completion",
  "created": 1677652288,
  "model": "anthropic/claude-sonnet-4",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "The meaning of life is a deeply personal question...",
        "reasoning": "Let me think about this carefully. The question asks about...",
        "reasoning_details": [
          {
            "type": "reasoning.text",
            "text": "Let me think about this carefully. The question asks about...",
            "signature": "anthropic-signature-xyz",
            "format": "anthropic-claude-v1",
            "index": 0
          }
        ]
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 15,
    "completion_tokens": 150,
    "total_tokens": 165,
    "completion_tokens_details": {
      "reasoning_tokens": 50
    }
  }
}
```

For OpenAI models (returns both summary and encrypted):

```
{
  "id": "chatcmpl-456",
  "object": "chat.completion",
  "created": 1677652288,
  "model": "openai/o3-mini",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "The answer is 42.",
        "reasoning": "Let me calculate this step by step...",
        "reasoning_details": [
          {
            "type": "reasoning.summary",
            "summary": "Let me calculate this step by step...",
            "format": "openai-responses-v1",
            "index": 0
          },
          {
            "type": "reasoning.encrypted",
            "data": "encrypted_reasoning_content_xyz",
            "format": "openai-responses-v1",
            "index": 1
          }
        ]
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 15,
    "completion_tokens": 150,
    "total_tokens": 165,
    "completion_tokens_details": {
      "reasoning_tokens": 50
    }
  }
}
```

Streaming reasoning details

When streaming, reasoning details are delivered incrementally in `delta.reasoning_details`:

For Anthropic models:

```
{
  "id": "chatcmpl-123",
  "object": "chat.completion.chunk",
  "created": 1677652288,
  "model": "anthropic/claude-sonnet-4",
  "choices": [
    {
      "index": 0,
      "delta": {
        "reasoning": "Let me think.",
        "reasoning_details": [
          {
            "type": "reasoning.text",
            "text": "Let me think.",
            "signature": "anthropic-signature-xyz",
            "format": "anthropic-claude-v1",
            "index": 0
          }
        ]
      },
      "finish_reason": null
    }
  ]
}
```

For OpenAI models (summary chunks during reasoning, then encrypted at end):

```
{
  "id": "chatcmpl-456",
  "object": "chat.completion.chunk",
  "created": 1677652288,
  "model": "openai/o3-mini",
  "choices": [
    {
      "index": 0,
      "delta": {
        "reasoning": "Step 1:",
        "reasoning_details": [
          {
            "type": "reasoning.summary",
            "summary": "Step 1:",
            "format": "openai-responses-v1",
            "index": 0
          }
        ]
      },
      "finish_reason": null
    }
  ]
}
```

#### [Provider-specific behavior](#provider-specific-behavior)

The AI Gateway automatically maps reasoning parameters to each provider's native format:

*   OpenAI: Maps `effort` to `reasoningEffort` and controls summary detail
*   Anthropic: Maps `max_tokens` to thinking budget tokens
*   Google: Maps to `thinkingConfig` with budget and visibility settings
*   Groq: Maps `exclude` to control reasoning format (hidden/parsed)
*   xAI: Maps `effort` to reasoning effort levels
*   Other providers: Generic mapping applied for compatibility

Automatic extraction: For models that don't natively support reasoning output, the gateway automatically extracts reasoning from `<think>` tags in the response.

### [Provider options](#provider-options)

The AI Gateway can route your requests across multiple AI providers for better reliability and performance. You can control which providers are used and in what order through the `providerOptions` parameter.

Example request

TypeScriptPython

provider-options.ts

```
import OpenAI from 'openai';
 
const apiKey = process.env.AI_GATEWAY_API_KEY || process.env.VERCEL_OIDC_TOKEN;
 
const openai = new OpenAI({
  apiKey,
  baseURL: 'https://ai-gateway.vercel.sh/v1',
});
 
// @ts-expect-error
const completion = await openai.chat.completions.create({
  model: 'anthropic/claude-sonnet-4',
  messages: [
    {
      role: 'user',
      content:
        'Tell me the history of the San Francisco Mission-style burrito in two paragraphs.',
    },
  ],
  stream: false,
  // Provider options for gateway routing preferences
  providerOptions: {
    gateway: {
      order: ['vertex', 'anthropic'], // Try Vertex AI first, then Anthropic
    },
  },
});
 
console.log('Assistant:', completion.choices[0].message.content);
console.log('Tokens used:', completion.usage);
```

provider-options.py

```
import os
from openai import OpenAI
 
api_key = os.getenv('AI_GATEWAY_API_KEY') or os.getenv('VERCEL_OIDC_TOKEN')
 
client = OpenAI(
    api_key=api_key,
    base_url='https://ai-gateway.vercel.sh/v1'
)
 
completion = client.chat.completions.create(
    model='anthropic/claude-sonnet-4',
    messages=[
        {
            'role': 'user',
            'content': 'Tell me the history of the San Francisco Mission-style burrito in two paragraphs.'
        }
    ],
    stream=False,
    # Provider options for gateway routing preferences
    extra_body={
        'providerOptions': {
            'gateway': {
                'order': ['vertex', 'anthropic']  # Try Vertex AI first, then Anthropic
            }
        }
    }
)
 
print('Assistant:', completion.choices[0].message.content)
print('Tokens used:', completion.usage)
```

Provider routing: In this example, the gateway will first attempt to use Vertex AI to serve the Claude model. If Vertex AI is unavailable or fails, it will fall back to Anthropic. Other providers are still available but will only be used after the specified providers.

#### [Model fallbacks](#model-fallbacks)

You can specify fallback models that will be tried in order if the primary model fails. There are two ways to do this:

###### Option 1: Direct `models` field

The simplest way is to use the `models` field directly at the top level of your request:

TypeScriptPython

model-fallbacks.ts

```
import OpenAI from 'openai';
 
const apiKey = process.env.AI_GATEWAY_API_KEY || process.env.VERCEL_OIDC_TOKEN;
 
const openai = new OpenAI({
  apiKey,
  baseURL: 'https://ai-gateway.vercel.sh/v1',
});
 
const completion = await openai.chat.completions.create({
  model: 'openai/gpt-4o', // Primary model
  // @ts-ignore - models is a gateway extension
  models: ['openai/gpt-5-nano', 'gemini-2.0-flash'], // Fallback models
  messages: [
    {
      role: 'user',
      content: 'Write a haiku about TypeScript.',
    },
  ],
  stream: false,
});
 
console.log('Assistant:', completion.choices[0].message.content);
 
// Check which model was actually used
console.log('Model used:', completion.model);
```

model-fallbacks.py

```
import os
from openai import OpenAI
 
api_key = os.getenv('AI_GATEWAY_API_KEY') or os.getenv('VERCEL_OIDC_TOKEN')
 
client = OpenAI(
    api_key=api_key,
    base_url='https://ai-gateway.vercel.sh/v1'
)
 
completion = client.chat.completions.create(
    model='openai/gpt-4o',  # Primary model
    messages=[
        {
            'role': 'user',
            'content': 'Write a haiku about TypeScript.'
        }
    ],
    stream=False,
    # models is a gateway extension for fallback models
    extra_body={
        'models': ['openai/gpt-5-nano', 'gemini-2.0-flash']  # Fallback models
    }
)
 
print('Assistant:', completion.choices[0].message.content)
 
# Check which model was actually used
print('Model used:', completion.model)
```

###### Option 2: Via provider options

Alternatively, you can specify model fallbacks through the `providerOptions.gateway.models` field:

TypeScriptPython

model-fallbacks-provider-options.ts

```
import OpenAI from 'openai';
 
const apiKey = process.env.AI_GATEWAY_API_KEY || process.env.VERCEL_OIDC_TOKEN;
 
const openai = new OpenAI({
  apiKey,
  baseURL: 'https://ai-gateway.vercel.sh/v1',
});
 
// @ts-expect-error
const completion = await openai.chat.completions.create({
  model: 'openai/gpt-4o', // Primary model
  messages: [
    {
      role: 'user',
      content: 'Write a haiku about TypeScript.',
    },
  ],
  stream: false,
  // Model fallbacks via provider options
  providerOptions: {
    gateway: {
      models: ['openai/gpt-5-nano', 'gemini-2.0-flash'], // Fallback models
    },
  },
});
 
console.log('Assistant:', completion.choices[0].message.content);
console.log('Model used:', completion.model);
```

model-fallbacks-provider-options.py

```
import os
from openai import OpenAI
 
api_key = os.getenv('AI_GATEWAY_API_KEY') or os.getenv('VERCEL_OIDC_TOKEN')
 
client = OpenAI(
    api_key=api_key,
    base_url='https://ai-gateway.vercel.sh/v1'
)
 
completion = client.chat.completions.create(
    model='openai/gpt-4o',  # Primary model
    messages=[
        {
            'role': 'user',
            'content': 'Write a haiku about TypeScript.'
        }
    ],
    stream=False,
    # Model fallbacks via provider options
    extra_body={
        'providerOptions': {
            'gateway': {
                'models': ['openai/gpt-5-nano', 'gemini-2.0-flash']  # Fallback models
            }
        }
    }
)
 
print('Assistant:', completion.choices[0].message.content)
print('Model used:', completion.model)
```

Which approach to use: Both methods achieve the same result. Use the direct `models` field (Option 1) for simplicity, or use `providerOptions` (Option 2) if you're already using provider options for other configurations.

Both configurations will:

1.  Try the primary model (`openai/gpt-4o`) first
2.  If it fails, try `openai/gpt-5-nano`
3.  If that also fails, try `gemini-2.0-flash`
4.  Return the result from the first model that succeeds

#### [Streaming with provider options](#streaming-with-provider-options)

Provider options work with streaming requests as well:

TypeScriptPython

streaming-provider-options.ts

```
import OpenAI from 'openai';
 
const apiKey = process.env.AI_GATEWAY_API_KEY || process.env.VERCEL_OIDC_TOKEN;
 
const openai = new OpenAI({
  apiKey,
  baseURL: 'https://ai-gateway.vercel.sh/v1',
});
 
// @ts-expect-error
const stream = await openai.chat.completions.create({
  model: 'anthropic/claude-sonnet-4',
  messages: [
    {
      role: 'user',
      content:
        'Tell me the history of the San Francisco Mission-style burrito in two paragraphs.',
    },
  ],
  stream: true,
  providerOptions: {
    gateway: {
      order: ['vertex', 'anthropic'],
    },
  },
});
 
for await (const chunk of stream) {
  const content = chunk.choices[0]?.delta?.content;
  if (content) {
    process.stdout.write(content);
  }
}
```

streaming-provider-options.py

```
import os
from openai import OpenAI
 
api_key = os.getenv('AI_GATEWAY_API_KEY') or os.getenv('VERCEL_OIDC_TOKEN')
 
client = OpenAI(
    api_key=api_key,
    base_url='https://ai-gateway.vercel.sh/v1'
)
 
stream = client.chat.completions.create(
    model='anthropic/claude-sonnet-4',
    messages=[
        {
            'role': 'user',
            'content': 'Tell me the history of the San Francisco Mission-style burrito in two paragraphs.'
        }
    ],
    stream=True,
    extra_body={
        'providerOptions': {
            'gateway': {
                'order': ['vertex', 'anthropic']
            }
        }
    }
)
 
for chunk in stream:
    content = chunk.choices[0].delta.content
    if content:
        print(content, end='', flush=True)
```

For more details about available providers and advanced provider configuration, see the [Provider Options documentation](/docs/ai-gateway/provider-options).

### [Parameters](#parameters)

The chat completions endpoint supports the following parameters:

#### [Required parameters](#required-parameters)

*   `model` (string): The model to use for the completion (e.g., `anthropic/claude-sonnet-4`)
*   `messages` (array): Array of message objects with `role` and `content` fields

#### [Optional parameters](#optional-parameters)

*   `stream` (boolean): Whether to stream the response. Defaults to `false`
*   `temperature` (number): Controls randomness in the output. Range: 0-2
*   `max_tokens` (integer): Maximum number of tokens to generate
*   `top_p` (number): Nucleus sampling parameter. Range: 0-1
*   `frequency_penalty` (number): Penalty for frequent tokens. Range: -2 to 2
*   `presence_penalty` (number): Penalty for present tokens. Range: -2 to 2
*   `stop` (string or array): Stop sequences for the generation
*   `tools` (array): Array of tool definitions for function calling
*   `tool_choice` (string or object): Controls which tools are called (`auto`, `none`, or specific function)
*   `providerOptions` (object): [Provider routing and configuration options](#provider-options)
*   `response_format` (object): Controls the format of the model's response
    *   For OpenAI standard format: `{ type: "json_schema", json_schema: { name, schema, strict?, description? } }`
    *   For legacy format: `{ type: "json", schema?, name?, description? }`
    *   For plain text: `{ type: "text" }`
    *   See [Structured outputs](#structured-outputs) for detailed examples

### [Message format](#message-format)

Messages support different content types:

#### [Text messages](#text-messages)

```
{
  "role": "user",
  "content": "Hello, how are you?"
}
```

#### [Multimodal messages](#multimodal-messages)

```
{
  "role": "user",
  "content": [
    { "type": "text", "text": "What's in this image?" },
    {
      "type": "image_url",
      "image_url": {
        "url": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD..."
      }
    }
  ]
}
```

#### [File messages](#file-messages)

```
{
  "role": "user",
  "content": [
    { "type": "text", "text": "Summarize this document" },
    {
      "type": "file",
      "file": {
        "data": "JVBERi0xLjQKJcfsj6IKNSAwIG9iago8PAovVHlwZSAvUGFnZQo...",
        "media_type": "application/pdf",
        "filename": "document.pdf"
      }
    }
  ]
}
```

## [Image generation](#image-generation)

Generate images using AI models that support multimodal output through the OpenAI-compatible API. This feature allows you to create images alongside text responses using models like Google's Gemini 2.5 Flash Image.

Endpoint

`POST /chat/completions`

Parameters

To enable image generation, include the `modalities` parameter in your request:

*   `modalities` (array): Array of strings specifying the desired output modalities. Use `['text', 'image']` for both text and image generation, or `['image']` for image-only generation.

Example requests

TypeScriptPython

image-generation.ts

```
import OpenAI from 'openai';
 
const apiKey = process.env.AI_GATEWAY_API_KEY || process.env.VERCEL_OIDC_TOKEN;
 
const openai = new OpenAI({
  apiKey,
  baseURL: 'https://ai-gateway.vercel.sh/v1',
});
 
const completion = await openai.chat.completions.create({
  model: 'google/gemini-2.5-flash-image-preview',
  messages: [
    {
      role: 'user',
      content:
        'Generate a beautiful sunset over mountains and describe the scene.',
    },
  ],
  // @ts-expect-error - modalities not yet in OpenAI types but supported by gateway
  modalities: ['text', 'image'],
  stream: false,
});
 
const message = completion.choices[0].message;
 
// Text content is always a string
console.log('Text:', message.content);
 
// Images are in a separate array
if (message.images && Array.isArray(message.images)) {
  console.log(`Generated ${message.images.length} images:`);
  for (const [index, img] of message.images.entries()) {
    if (img.type === 'image_url' && img.image_url) {
      console.log(`Image ${index + 1}:`, {
        size: img.image_url.url?.length || 0,
        preview: `${img.image_url.url?.substring(0, 50)}...`,
      });
    }
  }
}
```

image-generation.py

```
import os
from openai import OpenAI
 
api_key = os.getenv('AI_GATEWAY_API_KEY') or os.getenv('VERCEL_OIDC_TOKEN')
 
client = OpenAI(
    api_key=api_key,
    base_url='https://ai-gateway.vercel.sh/v1'
)
 
completion = client.chat.completions.create(
    model='google/gemini-2.5-flash-image-preview',
    messages=[
        {
            'role': 'user',
            'content': 'Generate a beautiful sunset over mountains and describe the scene.'
        }
    ],
    # Note: modalities parameter is not yet in OpenAI Python types but supported by our gateway
    extra_body={'modalities': ['text', 'image']},
    stream=False,
)
 
message = completion.choices[0].message
 
# Text content is always a string
print(f"Text: {message.content}")
 
# Images are in a separate array
if hasattr(message, 'images') and message.images:
    print(f"Generated {len(message.images)} images:")
    for i, img in enumerate(message.images):
        if img.get('type') == 'image_url' and img.get('image_url'):
            image_url = img['image_url']['url']
            data_size = len(image_url) if image_url else 0
            print(f"Image {i+1}: size: {data_size} chars")
            print(f"Preview: {image_url[:50]}...")
 
print(f'Tokens used: {completion.usage}')
```

Response format

When image generation is enabled, the response separates text content from generated images:

```
{
  "id": "chatcmpl-123",
  "object": "chat.completion",
  "created": 1677652288,
  "model": "google/gemini-2.5-flash-image-preview",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Here's a beautiful sunset scene over the mountains...",
        "images": [
          {
            "type": "image_url",
            "image_url": {
              "url": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8/5+hHgAHggJ/PchI7wAAAABJRU5ErkJggg=="
            }
          }
        ]
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 15,
    "completion_tokens": 28,
    "total_tokens": 43
  }
}
```

### [Response structure details](#response-structure-details)

*   `content`: Contains the text description as a string
*   `images`: Array of generated images, each with:
    *   `type`: Always `"image_url"`
    *   `image_url.url`: Base64-encoded data URI of the generated image

### [Streaming responses](#streaming-responses)

For streaming requests, images are delivered in delta chunks:

```
{
  "id": "chatcmpl-123",
  "object": "chat.completion.chunk",
  "created": 1677652288,
  "model": "google/gemini-2.5-flash-image-preview",
  "choices": [
    {
      "index": 0,
      "delta": {
        "images": [
          {
            "type": "image_url",
            "image_url": {
              "url": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8/5+hHgAHggJ/PchI7wAAAABJRU5ErkJggg=="
            }
          }
        ]
      },
      "finish_reason": null
    }
  ]
}
```

### [Handling streaming image responses](#handling-streaming-image-responses)

When processing streaming responses, check for both text content and images in each delta:

TypeScriptPython

streaming-images.ts

```
import OpenAI from 'openai';
 
const openai = new OpenAI({
  apiKey: process.env.AI_GATEWAY_API_KEY,
  baseURL: 'https://ai-gateway.vercel.sh/v1',
});
 
const stream = await openai.chat.completions.create({
  model: 'google/gemini-2.5-flash-image-preview',
  messages: [{ role: 'user', content: 'Generate a sunset image' }],
  // @ts-expect-error - modalities not yet in OpenAI types
  modalities: ['text', 'image'],
  stream: true,
});
 
for await (const chunk of stream) {
  const delta = chunk.choices[0]?.delta;
 
  // Handle text content
  if (delta?.content) {
    process.stdout.write(delta.content);
  }
 
  // Handle images
  if (delta?.images) {
    for (const img of delta.images) {
      if (img.type === 'image_url' && img.image_url) {
        console.log(`\n[Image received: ${img.image_url.url.length} chars]`);
      }
    }
  }
}
```

streaming-images.py

```
import os
from openai import OpenAI
 
client = OpenAI(
    api_key=os.getenv('AI_GATEWAY_API_KEY'),
    base_url='https://ai-gateway.vercel.sh/v1'
)
 
stream = client.chat.completions.create(
    model='google/gemini-2.5-flash-image-preview',
    messages=[{'role': 'user', 'content': 'Generate a sunset image'}],
    extra_body={'modalities': ['text', 'image']},
    stream=True,
)
 
for chunk in stream:
    if chunk.choices and chunk.choices[0].delta:
        delta = chunk.choices[0].delta
 
        # Handle text content
        if hasattr(delta, 'content') and delta.content:
            print(delta.content, end='', flush=True)
 
        # Handle images
        if hasattr(delta, 'images') and delta.images:
            for img in delta.images:
                if img.get('type') == 'image_url' and img.get('image_url'):
                    image_url = img['image_url']['url']
                    print(f"\n[Image received: {len(image_url)} chars]")
```

Image generation support: Currently, image generation is supported by Google's Gemini 2.5 Flash Image model. The generated images are returned as base64-encoded data URIs in the response. For more detailed information about image generation capabilities, see the [Image Generation documentation](/docs/ai-gateway/image-generation).

## [Embeddings](#embeddings)

Generate vector embeddings from input text for semantic search, similarity matching, and retrieval-augmented generation (RAG).

Endpoint

`POST /embeddings`

Example request

TypeScriptPython

embeddings.ts

```
import OpenAI from 'openai';
 
const apiKey = process.env.AI_GATEWAY_API_KEY || process.env.VERCEL_OIDC_TOKEN;
 
const openai = new OpenAI({
  apiKey,
  baseURL: 'https://ai-gateway.vercel.sh/v1',
});
 
const response = await openai.embeddings.create({
  model: 'openai/text-embedding-3-small',
  input: 'Sunny day at the beach',
});
 
console.log(response.data[0].embedding);
```

embeddings.py

```
import os
from openai import OpenAI
 
api_key = os.getenv("AI_GATEWAY_API_KEY") or os.getenv("VERCEL_OIDC_TOKEN")
 
client = OpenAI(
    api_key=api_key,
    base_url="https://ai-gateway.vercel.sh/v1",
)
 
response = client.embeddings.create(
    model="openai/text-embedding-3-small",
    input="Sunny day at the beach",
)
 
print(response.data[0].embedding)
```

Response format

```
{
  "object": "list",
  "data": [
    {
      "object": "embedding",
      "index": 0,
      "embedding": [-0.0038, 0.021, ...]
    },
  ],
  "model": "openai/text-embedding-3-small",
  "usage": {
    "prompt_tokens": 6,
    "total_tokens": 6
  },
  "providerMetadata": {
    "gateway": {
      "routing": { ... }, // Detailed routing info
      "cost": "0.00000012"
    }
  }
}
```

Dimensions parameter

You can set the root-level `dimensions` field (from the [OpenAI Embeddings API spec](https://platform.openai.com/docs/api-reference/embeddings/create)) and the gateway will auto-map it to each provider's expected field; `providerOptions.[provider]` still passes through as-is and isn't required for `dimensions` to work.

TypeScriptPython

embeddings-dimensions.ts

```
const response = await openai.embeddings.create({
  model: 'openai/text-embedding-3-small',
  input: 'Sunny day at the beach',
  dimensions: 768,
});
```

embeddings-dimensions.py

```
response = client.embeddings.create(
    model='openai/text-embedding-3-small',
    input='Sunny day at the beach',
    dimensions=768,
)
```

## [Error handling](#error-handling)

The API returns standard HTTP status codes and error responses:

### [Common error codes](#common-error-codes)

*   `400 Bad Request`: Invalid request parameters
*   `401 Unauthorized`: Invalid or missing authentication
*   `403 Forbidden`: Insufficient permissions
*   `404 Not Found`: Model or endpoint not found
*   `429 Too Many Requests`: Rate limit exceeded
*   `500 Internal Server Error`: Server error

### [Error response format](#error-response-format)

```
{
  "error": {
    "message": "Invalid request: missing required parameter 'model'",
    "type": "invalid_request_error",
    "param": "model",
    "code": "missing_parameter"
  }
}
```

## [Direct REST API usage](#direct-rest-api-usage)

If you prefer to use the AI Gateway API directly without the OpenAI client libraries, you can make HTTP requests using any HTTP client. Here are examples using `curl` and JavaScript's `fetch` API:

### [List models](#list-models)

cURLJavaScript

list-models.sh

```
curl -X GET "https://ai-gateway.vercel.sh/v1/models" \
  -H "Authorization: Bearer $AI_GATEWAY_API_KEY" \
  -H "Content-Type: application/json"
```

list-models.js

```
const response = await fetch('https://ai-gateway.vercel.sh/v1/models', {
  method: 'GET',
  headers: {
    Authorization: `Bearer ${process.env.AI_GATEWAY_API_KEY}`,
    'Content-Type': 'application/json',
  },
});
 
const models = await response.json();
console.log(models);
```

### [Basic chat completion](#basic-chat-completion)

cURLJavaScript

chat-completion.sh

```
curl -X POST "https://ai-gateway.vercel.sh/v1/chat/completions" \
  -H "Authorization: Bearer $AI_GATEWAY_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "anthropic/claude-sonnet-4",
    "messages": [
      {
        "role": "user",
        "content": "Write a one-sentence bedtime story about a unicorn."
      }
    ],
    "stream": false
  }'
```

chat-completion.js

```
const response = await fetch(
  'https://ai-gateway.vercel.sh/v1/chat/completions',
  {
    method: 'POST',
    headers: {
      Authorization: `Bearer ${process.env.AI_GATEWAY_API_KEY}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      model: 'anthropic/claude-sonnet-4',
      messages: [
        {
          role: 'user',
          content: 'Write a one-sentence bedtime story about a unicorn.',
        },
      ],
      stream: false,
    }),
  },
);
 
const result = await response.json();
console.log(result);
```

### [Streaming chat completion](#streaming-chat-completion)

cURLJavaScript

streaming-chat.sh

```
curl -X POST "https://ai-gateway.vercel.sh/v1/chat/completions" \
  -H "Authorization: Bearer $AI_GATEWAY_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "anthropic/claude-sonnet-4",
    "messages": [
      {
        "role": "user",
        "content": "Write a one-sentence bedtime story about a unicorn."
      }
    ],
    "stream": true
  }' \
  --no-buffer
```

streaming-chat.js

```
const response = await fetch(
  'https://ai-gateway.vercel.sh/v1/chat/completions',
  {
    method: 'POST',
    headers: {
      Authorization: `Bearer ${process.env.AI_GATEWAY_API_KEY}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      model: 'anthropic/claude-sonnet-4',
      messages: [
        {
          role: 'user',
          content: 'Write a one-sentence bedtime story about a unicorn.',
        },
      ],
      stream: true,
    }),
  },
);
 
const reader = response.body.getReader();
const decoder = new TextDecoder();
 
while (true) {
  const { done, value } = await reader.read();
  if (done) break;
 
  const chunk = decoder.decode(value);
  const lines = chunk.split('\n');
 
  for (const line of lines) {
    if (line.startsWith('data: ')) {
      const data = line.slice(6);
      if (data === '[DONE]') {
        console.log('Stream complete');
        break;
      } else if (data.trim()) {
        const parsed = JSON.parse(data);
        const content = parsed.choices?.[0]?.delta?.content;
        if (content) {
          process.stdout.write(content);
        }
      }
    }
  }
}
```

### [Image analysis](#image-analysis)

cURLJavaScript

image-analysis.sh

```
# First, convert your image to base64
IMAGE_BASE64=$(base64 -i ./path/to/image.png)
 
curl -X POST "https://ai-gateway.vercel.sh/v1/chat/completions" \
  -H "Authorization: Bearer $AI_GATEWAY_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "anthropic/claude-sonnet-4",
    "messages": [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "Describe this image in detail."
          },
          {
            "type": "image_url",
            "image_url": {
              "url": "data:image/png;base64,'"$IMAGE_BASE64"'",
              "detail": "auto"
            }
          }
        ]
      }
    ],
    "stream": false
  }'
```

image-analysis.js

```
import fs from 'node:fs';
 
// Read the image file as base64
const imageBuffer = fs.readFileSync('./path/to/image.png');
const imageBase64 = imageBuffer.toString('base64');
 
const response = await fetch(
  'https://ai-gateway.vercel.sh/v1/chat/completions',
  {
    method: 'POST',
    headers: {
      Authorization: `Bearer ${process.env.AI_GATEWAY_API_KEY}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      model: 'anthropic/claude-sonnet-4',
      messages: [
        {
          role: 'user',
          content: [
            { type: 'text', text: 'Describe this image in detail.' },
            {
              type: 'image_url',
              image_url: {
                url: `data:image/png;base64,${imageBase64}`,
                detail: 'auto',
              },
            },
          ],
        },
      ],
      stream: false,
    }),
  },
);
 
const result = await response.json();
console.log(result);
```

### [Tool calls](#tool-calls)

cURLJavaScript

tool-calls.sh

```
curl -X POST "https://ai-gateway.vercel.sh/v1/chat/completions" \
  -H "Authorization: Bearer $AI_GATEWAY_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "anthropic/claude-sonnet-4",
    "messages": [
      {
        "role": "user",
        "content": "What is the weather like in San Francisco?"
      }
    ],
    "tools": [
      {
        "type": "function",
        "function": {
          "name": "get_weather",
          "description": "Get the current weather in a given location",
          "parameters": {
            "type": "object",
            "properties": {
              "location": {
                "type": "string",
                "description": "The city and state, e.g. San Francisco, CA"
              },
              "unit": {
                "type": "string",
                "enum": ["celsius", "fahrenheit"],
                "description": "The unit for temperature"
              }
            },
            "required": ["location"]
          }
        }
      }
    ],
    "tool_choice": "auto",
    "stream": false
  }'
```

tool-calls.js

```
const response = await fetch(
  'https://ai-gateway.vercel.sh/v1/chat/completions',
  {
    method: 'POST',
    headers: {
      Authorization: `Bearer ${process.env.AI_GATEWAY_API_KEY}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      model: 'anthropic/claude-sonnet-4',
      messages: [
        {
          role: 'user',
          content: 'What is the weather like in San Francisco?',
        },
      ],
      tools: [
        {
          type: 'function',
          function: {
            name: 'get_weather',
            description: 'Get the current weather in a given location',
            parameters: {
              type: 'object',
              properties: {
                location: {
                  type: 'string',
                  description: 'The city and state, e.g. San Francisco, CA',
                },
                unit: {
                  type: 'string',
                  enum: ['celsius', 'fahrenheit'],
                  description: 'The unit for temperature',
                },
              },
              required: ['location'],
            },
          },
        },
      ],
      tool_choice: 'auto',
      stream: false,
    }),
  },
);
 
const result = await response.json();
console.log(result);
```

### [Provider options](#provider-options)

cURLJavaScript

provider-options.sh

```
curl -X POST "https://ai-gateway.vercel.sh/v1/chat/completions" \
  -H "Authorization: Bearer $AI_GATEWAY_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "anthropic/claude-sonnet-4",
    "messages": [
      {
        "role": "user",
        "content": "Tell me the history of the San Francisco Mission-style burrito in two paragraphs."
      }
    ],
    "stream": false,
    "providerOptions": {
      "gateway": {
        "order": ["vertex", "anthropic"]
      }
    }
  }'
```

provider-options.js

```
const response = await fetch(
  'https://ai-gateway.vercel.sh/v1/chat/completions',
  {
    method: 'POST',
    headers: {
      Authorization: `Bearer ${process.env.AI_GATEWAY_API_KEY}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      model: 'anthropic/claude-sonnet-4',
      messages: [
        {
          role: 'user',
          content:
            'Tell me the history of the San Francisco Mission-style burrito in two paragraphs.',
        },
      ],
      stream: false,
      providerOptions: {
        gateway: {
          order: ['vertex', 'anthropic'], // Try Vertex AI first, then Anthropic
        },
      },
    }),
  },
);
 
const result = await response.json();
console.log(result);
```

--------------------------------------------------------------------------------
title: "Pricing"
description: "Learn about pricing for the AI Gateway."
last_updated: "null"
source: "https://vercel.com/docs/ai-gateway/pricing"
--------------------------------------------------------------------------------

# Pricing

Copy page

Ask AI about this page

Last updated October 21, 2025

You only pay for what you use on the AI Gateway by purchasing [AI Gateway Credits through the Vercel dashboard](#view-your-ai-gateway-credits-balance). There are no markups to use the AI Gateway, so you're only charged for what your AI providers would bill you if you were using the provider directly.

Charges are automatically deducted from your AI Gateway Credits balance and you can [top up the balance](#top-up-your-ai-gateway-credits) at any time.

## [Free and paid tiers](#free-and-paid-tiers)

The AI Gateway offers both a free tier and a paid tier for AI Gateway Credits. For the paid tier, tokens are provided with zero markup, even in the case of bring your own key.

### [Free tier](#free-tier)

Every Vercel team account includes $5 of free usage per month, giving you the opportunity to explore the AI Gateway without any upfront costs.

How it works:

*   $5 monthly credit: you'll receive $5 AI Gateway Credits every 30 days after you make your first AI Gateway request.
*   Model flexibility: choose from any available models, your free credits work across our entire model catalog.
*   No commitment: you can stay on the free tier as long as you do not purchase AI Gateway Credits through the AI Gateway.

### [Moving to paid tier](#moving-to-paid-tier)

You can purchase AI Gateway Credits and move to a paid account on the AI Gateway, enabling you to run larger workloads.

Once you purchase AI Gateway Credits, your account transitions to our pay-as-you-go model:

*   No lock-in: purchase AI Gateway Credits as you use them, with no obligation to renew your commitment.
*   No free tier: once you create a paid account, you will not receive $5 of AI Gateway Credits per month.

## [AI Gateway Rates](#ai-gateway-rates)

No matter whether you access the AI Gateway through a free or paid account, you'll pay the AI Gateway rates listed in the Models section of the AI Gateway tab for each request. The AI Gateway's rates are based on the provider's list price. We strive to keep the prices listed in the Model page in the AI Gateway tab of the Vercel dashboard up to date.

The charge for each request depends on the AI provider and model you select, and the number of input and output tokens processed. You're responsible for any payment processing fees that may apply.

## [Using a custom API key](#using-a-custom-api-key)

The AI Gateway also supports [using a custom API key](/docs/ai-gateway/byok) for any provider listed in our catalog. If you use a custom API key, there is no markup or fee from AI Gateway.

## [View your AI Gateway Credits balance](#view-your-ai-gateway-credits-balance)

To view your balance:

1.  Go to the AI Gateway tab of your Vercel dashboard.
2.  On the upper right corner, you will see your AI Gateway Credits balance displayed.

## [Top up your AI Gateway Credits](#top-up-your-ai-gateway-credits)

To add AI Gateway Credits:

1.  Go to the AI Gateway tab of your Vercel dashboard.
2.  In the upper right corner, click on the button that shows your AI Gateway Credits balance.
3.  In the dialog that appears, you can select the amount of AI Gateway Credits you want to add.
4.  Click on Continue to Payment.
5.  Choose your payment method and click on Confirm and Pay to complete your purchase.

--------------------------------------------------------------------------------
title: "Provider Options"
description: "Configure provider routing, ordering, and fallback behavior in Vercel AI Gateway"
last_updated: "null"
source: "https://vercel.com/docs/ai-gateway/provider-options"
--------------------------------------------------------------------------------

# Provider Options

Copy page

Ask AI about this page

Last updated October 28, 2025

AI Gateway can route your AI model requests across multiple AI providers. Each provider offers different models, pricing, and performance characteristics. By default, Vercel AI Gateway dynamically chooses the default providers to give you the best experience based on a combination recent uptime and latency.

With the Gateway Provider Options however, you have control over the routing order and fallback behavior of the models.

If you want to customize individual AI model provider settings rather than general AI Gateway behavior, please refer to the model-specific provider options in the [AI SDK documentation](https://ai-sdk.dev/docs/foundations/prompts#provider-options).

## [Basic provider ordering](#basic-provider-ordering)

You can use the `order` array to specify the sequence in which providers should be attempted. Providers are specified using their `slug` string. You can find the slugs in the [table of available providers](#available-providers).

You can also copy the provider slug using the copy button next to a provider's name on a model's detail page. In the Vercel Dashboard:

1.  Click the AI Gateway tab,
2.  Then, click the Model List sub-tab on the left
3.  Click a model entry in the list.

The bottom section of the page lists the available providers for that model. The copy button next to a provider's name will copy their slug for pasting.

### [Getting started with adding a provider option](#getting-started-with-adding-a-provider-option)

1.  ### [Install the AI SDK package](#install-the-ai-sdk-package)
    
    First, ensure you have the necessary package installed:
    
    terminal
    
    ```
    pnpm install ai
    ```
    
2.  ### [Configure the provider order in your request](#configure-the-provider-order-in-your-request)
    
    Use the `providerOptions.gateway.order` configuration:
    
    app/api/chat/route.ts
    
    ```
    import { streamText } from 'ai';
     
    export async function POST(request: Request) {
      const { prompt } = await request.json();
     
      const result = streamText({
        model: 'anthropic/claude-sonnet-4',
        prompt,
        providerOptions: {
          gateway: {
            order: ['bedrock', 'anthropic'], // Try Amazon Bedrock first, then Anthropic
          },
        },
      });
     
      return result.toUIMessageStreamResponse();
    }
    ```
    
    In this example:
    
    *   The gateway will first attempt to use Amazon Bedrock to serve the Claude 4 Sonnet model
    *   If Amazon Bedrock is unavailable or fails, it will fall back to Anthropic
    *   Other providers (like Vertex AI) are still available but will only be used after the specified providers
3.  ### [Test the routing behavior](#test-the-routing-behavior)
    
    You can monitor which provider you used by checking the provider metadata in the response.
    
    app/api/chat/route.ts
    
    ```
    import { streamText } from 'ai';
     
    export async function POST(request: Request) {
      const { prompt } = await request.json();
     
      const result = streamText({
        model: 'anthropic/claude-sonnet-4',
        prompt,
        providerOptions: {
          gateway: {
            order: ['bedrock', 'anthropic'],
          },
        },
      });
     
      // Log which provider was actually used
      console.log(JSON.stringify(await result.providerMetadata, null, 2));
     
      return result.toUIMessageStreamResponse();
    }
    ```
    

## [Example provider metadata output](#example-provider-metadata-output)

```
{
  "zai": {},
  "gateway": {
    "routing": {
      "originalModelId": "zai/glm-4.6",
      "resolvedProvider": "zai",
      "resolvedProviderApiModelId": "glm-4.6",
      "internalResolvedModelId": "zai:glm-4.6",
      "fallbacksAvailable": [],
      "internalReasoning": "Selected zai as preferred provider for glm-4.6. 0 fallback(s) available: ",
      "planningReasoning": "System credentials planned for: zai. Total execution order: zai(system)",
      "canonicalSlug": "zai/glm-4.6",
      "finalProvider": "zai",
      "attempts": [
        {
          "provider": "zai",
          "internalModelId": "zai:glm-4.6",
          "providerApiModelId": "glm-4.6",
          "credentialType": "system",
          "success": true,
          "startTime": 458753.407267,
          "endTime": 459891.705775
        }
      ],
      "modelAttemptCount": 1,
      "modelAttempts": [
        {
          "modelId": "zai/glm-4.6",
          "canonicalSlug": "zai/glm-4.6",
          "success": true,
          "providerAttemptCount": 1,
          "providerAttempts": [
            {
              "provider": "zai",
              "internalModelId": "zai:glm-4.6",
              "providerApiModelId": "glm-4.6",
              "credentialType": "system",
              "success": true,
              "startTime": 458753.407267,
              "endTime": 459891.705775
            }
          ]
        }
      ],
      "totalProviderAttemptCount": 1
    },
    "cost": "0.0045405",
    "marketCost": "0.0045405",
    "generationId": "gen_01K8KPJ0FZA7172X6CSGNZGDWY"
  }
}
```

The `gateway.cost` value is the amount debited from your AI Gateway Credits balance for this request. It is returned as a decimal string. The `gateway.marketCost` represents the market rate cost for the request. The `gateway.generationId` is a unique identifier for this generation that can be used with the [Generation Lookup API](/docs/ai-gateway/usage#generation-lookup). For more on pricing see [Pricing](/docs/ai-gateway/pricing).

In cases where your request encounters issues with one or more providers or if your BYOK credentials fail, you'll find error detail in the `attempts` field of the provider metadata:

```
"attempts": [
  {
    "provider": "novita",
    "internalModelId": "novita:zai-org/glm-4.5",
    "providerApiModelId": "zai-org/glm-4.5",
    "credentialType": "byok",
    "success": false,
    "error": "Unauthorized",
    "startTime": 1754639042520,
    "endTime": 1754639042710
  },
  {
    "provider": "novita",
    "internalModelId": "novita:zai-org/glm-4.5",
    "providerApiModelId": "zai-org/glm-4.5",
    "credentialType": "system",
    "success": true,
    "startTime": 1754639042710,
    "endTime": 1754639043353
  }
]
```

## [Restrict providers with the `only` filter](#restrict-providers-with-the-only-filter)

Use the `only` array to restrict routing to a specific subset of providers. Providers are specified by their slug and are matched against the model's available providers.

app/api/chat/route.ts

```
import { streamText } from 'ai';
 
export async function POST(request: Request) {
  const { prompt } = await request.json();
 
  const result = streamText({
    model: 'anthropic/claude-sonnet-4',
    prompt,
    providerOptions: {
      gateway: {
        only: ['bedrock', 'anthropic'], // Only consider these providers.
        // This model is also available via 'vertex', but it won't be considered.
      },
    },
  });
 
  return result.toUIMessageStreamResponse();
}
```

In this example:

*   Restriction: Only `bedrock` and `anthropic` will be considered for routing and fallbacks.
*   Error on mismatch: If none of the specified providers are available for the model, the request fails with an error indicating the allowed providers.

## [Using `only` together with `order`](#using-only-together-with-order)

When both `only` and `order` are provided, the `only` filter is applied first to define the allowed set, and then `order` defines the priority within that filtered set. Practically, the end result is the same as taking your `order` list and intersecting it with the `only` list.

app/api/chat/route.ts

```
import { streamText } from 'ai';
 
export async function POST(request: Request) {
  const { prompt } = await request.json();
 
  const result = streamText({
    model: 'anthropic/claude-sonnet-4',
    prompt,
    providerOptions: {
      gateway: {
        only: ['anthropic', 'vertex'],
        order: ['vertex', 'bedrock', 'anthropic'],
      },
    },
  });
 
  return result.toUIMessageStreamResponse();
}
```

The final order will be `vertex → anthropic` (providers listed in `order` but not in `only` are ignored).

## [Model fallbacks with the `models` option](#model-fallbacks-with-the-models-option)

You can specify fallback models that will be tried in order if the primary model fails or is unavailable. This provides model-level fallback in addition to provider-level routing.

app/api/chat/route.ts

```
import { streamText } from 'ai';
 
export async function POST(request: Request) {
  const { prompt } = await request.json();
 
  const result = streamText({
    model: 'openai/gpt-4o', // Primary model
    prompt,
    providerOptions: {
      gateway: {
        models: ['openai/gpt-5-nano', 'gemini-2.0-flash'], // Fallback models
      },
    },
  });
 
  return result.toUIMessageStreamResponse();
}
```

In this example:

*   The gateway will first attempt to use the primary model (`openai/gpt-4o`)
*   If the primary model fails or is unavailable, it will try `openai/gpt-5-nano`
*   If that also fails, it will try `gemini-2.0-flash`
*   The response will come from the first model that succeeds

### [Combining `models` with provider options](#combining-models-with-provider-options)

You can combine model fallbacks with provider routing options for comprehensive failover strategies:

app/api/chat/route.ts

```
import { streamText } from 'ai';
 
export async function POST(request: Request) {
  const { prompt } = await request.json();
 
  const result = streamText({
    model: 'openai/gpt-4o',
    prompt,
    providerOptions: {
      gateway: {
        models: ['openai/gpt-5-nano', 'anthropic/claude-sonnet-4'],
        order: ['azure', 'openai'], // Provider preference for each model
      },
    },
  });
 
  return result.toUIMessageStreamResponse();
}
```

This configuration will:

1.  Try `openai/gpt-4o` via Azure first, then OpenAI
2.  If both fail, try `openai/gpt-5-nano` via Azure first, then OpenAI
3.  If those fail, try `anthropic/claude-sonnet-4` via available providers

## [Combining AI Gateway provider options with provider-specific options](#combining-ai-gateway-provider-options-with-provider-specific-options)

You can combine AI Gateway provider options with provider-specific options. This allows you to control both the routing behavior and provider-specific settings in the same request:

app/api/chat/route.ts

```
import { streamText } from 'ai';
 
export async function POST(request: Request) {
  const { prompt } = await request.json();
 
  const result = streamText({
    model: 'anthropic/claude-sonnet-4',
    prompt,
    providerOptions: {
      anthropic: {
        thinkingBudget: 0.001,
      },
      gateway: {
        order: ['vertex'],
      },
    },
  });
 
  return result.toUIMessageStreamResponse();
}
```

In this example:

*   We're using an Anthropic model (e.g. Claude 4 Sonnet) but accessing it through Vertex AI
*   The Anthropic-specific options still apply to the model:
    *   `thinkingBudget` sets a cost limit of $0.001 per request for the Claude model
*   You can read more about provider-specific options in the [AI SDK documentation](https://ai-sdk.dev/docs/foundations/prompts#provider-options)

## [Reasoning](#reasoning)

For models that support reasoning (also known as "thinking"), you can use `providerOptions` to configure reasoning behavior. The example below shows how to control the computational effort and summary detail level when using OpenAI's `gpt-oss-120b` model.

For more details on reasoning support across different models and providers, see the [AI SDK providers documentation](https://ai-sdk.dev/providers/ai-sdk-providers), including [OpenAI](https://ai-sdk.dev/providers/ai-sdk-providers/openai#reasoning), [DeepSeek](https://ai-sdk.dev/providers/ai-sdk-providers/deepseek#reasoning), and [Anthropic](https://ai-sdk.dev/providers/ai-sdk-providers/anthropic#reasoning).

app/api/chat/route.ts

```
import { streamText } from 'ai';
 
export async function POST(request: Request) {
  const { prompt } = await request.json();
 
  const result = streamText({
    model: 'openai/gpt-oss-120b',
    prompt,
    providerOptions: {
      openai: {
        reasoningEffort: 'high',
        reasoningSummary: 'detailed',
      },
    },
  });
 
  return result.toUIMessageStreamResponse();
}
```

## [Available providers](#available-providers)

You can view the available models for a provider in the Model List section under the [AI Gateway](https://vercel.com/d?to=%2F%5Bteam%5D%2F%7E%2Fai&title=Go+to+AI+Gateway) tab in your Vercel dashboard or in the public [models page](https://vercel.com/ai-gateway/models).

| Slug | Name | Website |
| --- | --- | --- |
| `alibaba` | Alibaba Cloud | [alibabacloud.com](https://www.alibabacloud.com) |
| `anthropic` | [Anthropic](https://ai-sdk.dev/providers/ai-sdk-providers/anthropic) | [anthropic.com](https://anthropic.com) |
| `azure` | [Azure](https://ai-sdk.dev/providers/ai-sdk-providers/azure) | [ai.azure.com](https://ai.azure.com/) |
| `baseten` | [Baseten](https://ai-sdk.dev/providers/openai-compatible-providers/baseten) | [baseten.co](https://www.baseten.co/)  |
| `bedrock` | [Amazon Bedrock](https://ai-sdk.dev/providers/ai-sdk-providers/amazon-bedrock) | [aws.amazon.com/bedrock](https://aws.amazon.com/bedrock) |
| `cerebras` | [Cerebras](https://ai-sdk.dev/providers/ai-sdk-providers/cerebras) | [cerebras.net](https://www.cerebras.net) |
| `cohere` | [Cohere](https://ai-sdk.dev/providers/ai-sdk-providers/cohere) | [cohere.com](https://cohere.com) |
| `deepinfra` | [DeepInfra](https://ai-sdk.dev/providers/ai-sdk-providers/deepinfra) | [deepinfra.com](https://deepinfra.com) |
| `deepseek` | [DeepSeek](https://ai-sdk.dev/providers/ai-sdk-providers/deepseek) | [deepseek.ai](https://deepseek.ai) |
| `fireworks` | [Fireworks](https://ai-sdk.dev/providers/ai-sdk-providers/fireworks) | [fireworks.ai](https://fireworks.ai) |
| `google` | [Google](https://ai-sdk.dev/providers/ai-sdk-providers/google-generative-ai) | [ai.google.dev](https://ai.google.dev/) |
| `groq` | [Groq](https://ai-sdk.dev/providers/ai-sdk-providers/groq) | [groq.com](https://groq.com) |
| `inception` | Inception | [inceptionlabs.ai](https://inceptionlabs.ai) |
| `meituan` | Meituan | [longcat.ai](https://longcat.ai/) |
| `minimax` | MiniMax | [minimax.io](https://www.minimax.io/) |
| `mistral` | [Mistral](https://ai-sdk.dev/providers/ai-sdk-providers/mistral) | [mistral.ai](https://mistral.ai) |
| `moonshotai` | Moonshot AI | [moonshot.ai](https://www.moonshot.ai) |
| `morph` | Morph | [morphllm.com](https://morphllm.com) |
| `novita` | Novita | [novita.ai](https://novita.ai/) |
| `openai` | [OpenAI](https://ai-sdk.dev/providers/ai-sdk-providers/openai) | [openai.com](https://openai.com) |
| `parasail` | Parasail | [parasail.com](https://www.parasail.io) |
| `perplexity` | [Perplexity](https://ai-sdk.dev/providers/ai-sdk-providers/perplexity) | [perplexity.ai](https://www.perplexity.ai) |
| `vercel` | [Vercel](https://ai-sdk.dev/providers/ai-sdk-providers/vercel) |  |
| `vertex` | [Vertex AI](https://ai-sdk.dev/providers/ai-sdk-providers/google-vertex) | [cloud.google.com/vertex-ai](https://cloud.google.com/vertex-ai) |
| `voyage` | [Voyage AI](https://ai-sdk.dev/providers/community-providers/voyage-ai) | [voyageai.com](https://www.voyageai.com) |
| `xai` | [xAI](https://ai-sdk.dev/providers/ai-sdk-providers/xai) | [x.ai](https://x.ai) |
| `zai` | Z.ai | [z.ai](https://z.ai/model-api) |

Provider availability may vary by model. Some models may only be available through specific providers or may have different capabilities depending on the provider used.

--------------------------------------------------------------------------------
title: "Usage & Billing"
description: "Monitor your AI Gateway credit balance, usage, and generation details."
last_updated: "null"
source: "https://vercel.com/docs/ai-gateway/usage"
--------------------------------------------------------------------------------


---

**Navigation:** ← Previous | [Index](./index.md) | [Next →](./02-usage-billing.md)
