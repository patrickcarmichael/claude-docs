**Navigation:** [← Previous](./14-limits.md) | [Index](./index.md) | [Next →](./16-são-paulo-brazil-gru1-pricing.md)

---

# Notebooks

Copy page

Ask AI about this page

Last updated October 7, 2025

Notebooks are available on [Enterprise](/docs/plans/enterprise) and [Pro](/docs/plans/pro) plans

Notebooks allow you to collect and manage multiple queries related to your application's metrics and performance data.

Within a single notebook, you can store multiple queries that examine different aspects of your system - each with its own specific filters, time ranges, and data aggregations. This facilitates the building of comprehensive dashboards or analysis workflows by grouping related queries together.

You need to enable [Observability Plus](/docs/observability/observability-plus) to use Notebooks since you need run queries.

## [Using and managing notebooks](#using-and-managing-notebooks)

You can use notebooks to organize and save your queries. Each notebook is a collection of queries that you can keep personal or share with your team.

### [Create a notebook](#create-a-notebook)

1.  From the Observability tab of your dashboard, click Notebooks from the left navigation of the Observability Overview page
2.  Edit the notebook name by clicking the pencil icon on the top left of the default title which uses your username and created date and time.

### [Add a query to a notebook](#add-a-query-to-a-notebook)

1.  From the Notebooks page, click the Create Notebook button or select an existing Notebook
2.  Click the + icon to open the query builder and build your query
3.  Edit the query name by clicking the pencil icon on the top left of the default query title
4.  Select the most appropriate view for your query: line chart, volume chart, table or big number
5.  Once you're happy with your query results, save it by clicking Save Query
6.  Your query is now available in your notebook

### [Delete a query](#delete-a-query)

1.  From the Notebooks page, select an existing Notebook
2.  Click the three-dot menu on the top-right corner of a query, and select Delete. This action is permanent and cannot be undone.

### [Delete a notebook](#delete-a-notebook)

1.  From the Notebooks page, select the Notebook you'd like to delete from the list
2.  Click the three-dot menu on the top-right corner of the notebook, and select Delete notebook. This action is permanent and cannot be undone.

## [Notebook types and access](#notebook-types-and-access)

You can create 2 types of notebooks.

*   Personal Notebooks: Only the creator and owner can view them.
*   Team Notebooks: All team members can view them and they share ownership.

When created, notebooks are personal by default. You can use the Share button to turn them to Team Notebooks for collaboration. When shared, all team members have full access to modify, add, or remove content within the notebook.

As a Notebook owner, you have complete control over your notebook. You can add new queries, edit existing ones, remove individual queries, or delete the entire notebook if it's no longer needed.

--------------------------------------------------------------------------------
title: "Notifications"
description: "Learn how to use Notifications to view and manage important alerts about your deployments, domains, integrations, account, and usage."
last_updated: "null"
source: "https://vercel.com/docs/notifications"
--------------------------------------------------------------------------------

# Notifications

Copy page

Ask AI about this page

Last updated October 14, 2025

Notifications are available on [all plans](/docs/plans)

Vercel sends configurable notifications to you through the [dashboard](/dashboard) and email. These notifications enable you to view and manage important alerts about your [deployments](/docs/deployments), [domains](/docs/domains), [integrations](/docs/integrations), [account](/docs/accounts), and [usage](/docs/limits/usage).

## [Receiving notifications](#receiving-notifications)

There are a number of places where you can receive notifications:

*   Web: The Vercel dashboard displays a popover, which contains all relevant notifications
*   Email: You'll receive an email when any of the alerts that you set either on your Hobby team or team have been triggered
*   SMS: SMS notifications can only be configured on a per-user basis for [Spend Management](/docs/spend-management#managing-alert-threshold-notifications) notifications.

By default, you will receive both web and email notifications for all [types of alerts](#types-of-notifications). You can [manage these notifications](#managing-notifications) from the Settings tab, but any changes you make will only affect _your_ notifications.

## [Basic capabilities](#basic-capabilities)

There are two main ways to interact with web notifications:

*   Read: Unread notifications are displayed with a counter on the bell icon. When you view a notification on the web, it will be marked as read once you close the popover. Because of this, we also will not send an email if you have already read it on the web.
*   Archive: You can manage the list of notifications by archiving them. You can view these archived notifications in the archive tab, where they will be visible for 365 days.

## [Managing notifications](#managing-notifications)

You can manage your own notifications by using the following steps:

1.  Select your team from the [scope selector](/docs/dashboard-features#scope-selector).
2.  Go to the Settings tab of your account or team's dashboard, and under Account, select My Notifications.
3.  From here, you can toggle [where](#receiving-notifications) _you_ would like to receive notifications for each different [type of notification](#types-of-notifications).

Any changes you make will only be reflected for your notifications and not for any other members of the team. You cannot configure notifications for other users.

### [Notifications for Comments](#notifications-for-comments)

You can receive feedback on your deployments with the Comments feature. When someone leaves a comment, you'll receive a notification on Vercel. You can see all new comments in the Comments tab of your notifications.

[Learn more in the Comments docs](/docs/comments/managing-comments#notifications).

### [On-demand usage notifications](#on-demand-usage-notifications)

Customizing on-demand usage notifications is available on [Pro plans](/docs/plans/pro)

Those with the [owner](/docs/rbac/access-roles#owner-role) role can access this feature

You'll receive notifications as you accrue usage past the [included amounts](/docs/limits#included-usage) for products like Vercel Functions, Image Optimization, and more.

Team owners on the Pro plan can customize which usage categories they want to receive notifications for based on percentage thresholds or absolute dollar values.

Emails are sent out at specific usage thresholds which vary based on the feature and plan you are on.

If you choose to disable notifications, you won't receive alerts for any excessive charges within that category. This may result in unexpected additional costs on your bill. It is recommended that you carefully consider the implications of turning off notifications for any usage thresholds before making changes to your notification settings.

## [Types of notifications](#types-of-notifications)

The types of notifications available for you to manage depend on the [role](/docs/rbac/access-roles/team-level-roles) you are assigned within your team. For example, someone with a [Developer](/docs/rbac/access-roles#developer-role) role will only be able to be notified of Deployment failures and Integration updates.

### [Critical notifications](#critical-notifications)

It is _not_ possible to disable all notifications for alerts that are critical to your Vercel workflow. You can opt-out of [one specific channel](#receiving-notifications), like email, but not both email and web notifications. This is because of the importance of these notifications for using the Vercel platform. The list below provides information on which alerts are critical.

### [Notification details](#notification-details)

| Notification group | Type of notification | Explanation | [Critical notification?](#critical-notifications) |
| --- | --- | --- | --- |
| Account |  |  |  |
|  | Team join requests | Team owners will be notified when someone requests access to join their team and can follow a link from the notification to manage the request. |  |
| Alerts |  |  |  |
|  | Usage Anomalies | Triggered when the usage of your project exceeds a certain threshold |  |
|  | Error Anomalies | Triggered when a high rate of failed function invocations (those with a status code of 5xx) in your project exceeds a certain threshold |  |
| Deployment |  |  |  |
|  | Deployment Failures | Deployment owners will be notified about any deployment failures that occur for any Project on your account or team. |  |
| Domain |  |  |  |
|  | Configuration - Certificate renewal failed | Team owners will be notified if the SSL Certification renewal for any of their team's domains has failed. For more information, see [When is the SSL Certificate on my Vercel Domain renewed?](/guides/renewal-of-ssl-certificates-with-a-vercel-domain). |  |
|  | Configuration - Domain Configured | Team owners will be notified of any domains that have been added to a project. For more information, see [Add a domain](/docs/domains/add-a-domain). |  |
|  | Configuration - Domain Misconfigured | Team owners will be notified of any domains that have been added to a project and are misconfigured. These notifications will be batched. For more information, see [Add a domain](/docs/domains/add-a-domain). |  |
|  | Configuration - Domain no payment source or payment failure | Team owners will be notified if there were any payment issues while [Adding a domain](/docs/domains/add-a-domain). Ensure a valid payment option is adding to Settings > Billing |  |
|  | Renewals - Domain renewals | Team owners will be notified 17 days and 7 days before [renewal attempts](/docs/domains/renew-a-domain#auto-renewal-on). |  |
|  | Renewals - Domain expiration | Team owners will be notified 24 and 14 days before a domain is set to expire about, if [auto-renewal is off](/docs/domains/renew-a-domain#auto-renewal-off). A final email will notify you when the Domain expires. |  |
|  | Transfers - Domain moves requested or completed | Team owners will be notified when a domain has requested to move or successfully moved in or out of their team. For more information see, [Transfer a domain to another Vercel user or team](/docs/domains/working-with-domains/transfer-your-domain#transfer-a-domain-to-another-vercel-user-or-team) |  |
|  | Transfers - Domain transfers initiated, cancelled, and completed | Team owners will be notified about any information regarding any [domain transfers](/docs/domains/working-with-domains/transfer-your-domain) in or out of your team. |  |
|  | Transfers - Domain transfers pending approval | Team owners will be notified when a domain is being [transferred into Vercel](/docs/domains/working-with-domains/transfer-your-domain#transfer-a-domain-to-vercel), but the approval is required from the original registrar. |  |
| Integrations |  |  |  |
|  | Integration configuration disabled | Everyone will be notified about integration updates such as a [disabled Integration](/docs/integrations/install-an-integration/manage-integrations-reference#disabled-integrations). |  |
|  | Integration scope changed | Team owners will be notified if any of the Integrations used on their team have updated their [scope](/docs/rest-api/vercel-api-integrations#scopes). |  |
| Usage |  |  |  |
|  | Usage increased | Team owners will be notified about all [usage alerts](/docs/limits) regarding billing, and other usage warnings. |  |
|  | Usage limit reached | Users will be notified when they reach the limits outlined in the [Fair Usage Policy](/docs/limits/fair-use-guidelines). |  |
| Non-configurable |  |  |  |
|  | Email changed confirmation | You will be notified when you have successfully updated the email connected to your Hobby team |  |
|  | Email changed verification | You will be notified when you have updated the email connected to your Hobby team. You will need to verify this email to confirm. |  |
|  | User invited | You will be sent this when you have been invited to join a new team. |  |
|  | Invoice payment failed | Users who can manage billing settings will be notified when they have an [outstanding invoice](/docs/plans/enterprise/billing#why-am-i-overdue). |  |
|  | Project role changed | You will be sent this when your [role](/docs/accounts/team-members-and-roles) has changed |  |
|  | User deleted | You will be sent this when you have chosen to delete their account. This notification is sent by email only. |  |
| Edge Config | Size Limit Alerts | Members will be notified when Edge Config size exceeds its limits for the current plan |  |
|  | Schema Validation Errors | Members will be notified (at most once per hour) if API updates are rejected by [schema protection](/docs/edge-config/edge-config-dashboard#schema-validation) |  |

--------------------------------------------------------------------------------
title: "Observability"
description: "Observability on Vercel provides framework-aware insights enabling you to optimize infrastructure and application performance."
last_updated: "null"
source: "https://vercel.com/docs/observability"
--------------------------------------------------------------------------------

# Observability

Copy page

Ask AI about this page

Last updated October 31, 2025

Observability is available on [all plans](/docs/plans)

Observability provides a way for you to monitor and analyze the performance and traffic of your projects on Vercel through a variety of [events](#tracked-events) and [insights](#available-insights), aligned with your app's architecture.

*   Learn how to [use Observability](#using-observability) and the available [insight sections](/docs/observability#available-insights)
*   Learn how you can save and organize your Observability queries with [Notebooks](/docs/notebooks)

### [Observability feature access](#observability-feature-access)

You can use Observability on all plans to monitor your projects. If you are on the Pro or Enterprise plan, you can [upgrade](/docs/observability/observability-plus#enabling-observability-plus) to [Observability Plus](/docs/observability/observability-plus) to get access to [additional features and metrics](/docs/observability/observability-plus#limitations), [Monitoring](/docs/observability/monitoring) access, higher limits, and increased retention.

[Try Observability](https://vercel.com/d?to=%2F%5Bteam%5D%2F%7E%2Fobservability&title=Try+Observability) to get started.

![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fobservability%2FO11y-Tab-Light.png&w=3840&q=75)![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fobservability%2FO11y-Tab-Dark.png&w=3840&q=75)

## [Using Observability](#using-observability)

How you use Observability depends on the needs of your project, for example, perhaps builds are taking longer than expected, or your Vercel Functions seem to be increasing in cost. A brief overview of how you might use the tab would be:

1.  Decide what feature you want to investigate. For example, Vercel Functions.
2.  Use the date picker or the time range selector to choose the time period you want to investigate. Users on [Observability Plus](/docs/observability/observability-plus) will have a longer retention period and more granular data.
3.  Let's investigate our graphs in more detail, for example, Error Rate. Click and drag to select a period of time and press the Zoom In button.
    
    ![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fobservability%2Ferror-rate-light.png&w=1080&q=75)![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fobservability%2Ferror-rate-dark.png&w=1080&q=75)
    
4.  Then, from the list of routes below, choose to reorder either based on the error rate or the duration to get an idea of which routes are causing the most issues.
5.  To learn more about specific routes, click on the route.
6.  The functions view will show you the performance of each route or function, including details about the function, latency, paths, and External APIs. Note that Latency and breakdown by path are only available for [Observability Plus](/docs/observability/observability-plus) users.
7.  The function view also provides a direct link to the logs for that function, enabling you to pinpoint the cause of the issue.

### [Available insights](#available-insights)

Observability provides different sections of features and traffic sources that help you monitor, analyze, and manage your applications either at the team or the project level. The following table shows their availability at each level:

| Data source | Team Level | Project Level |
| --- | --- | --- |
| [Vercel Functions](/docs/observability/insights#vercel-functions) | ✓ | ✓ |
| [Edge Functions](/docs/observability/insights#edge-requests) | ✓ | ✓ |
| [External APIs](/docs/observability/insights#external-apis) | ✓ | ✓ |
| [Edge Requests](/docs/observability/insights#edge-requests) | ✓ | ✓ |
| [Middleware](/docs/observability/insights#middleware) | ✓ | ✓ |
| [Fast Data Transfer](/docs/observability/insights#fast-data-transfer) | ✓ | ✓ |
| [Image Optimization](/docs/observability/insights#image-optimization) | ✓ | ✓ |
| [ISR (Incremental Static Regeneration)](/docs/observability/insights#isr-incremental-static-regeneration) | ✓ | ✓ |
| [Blob](/docs/observability/insights#blob) | ✓ |  |
| [Build Diagnostics](/docs/observability/insights#build-diagnostics) |  | ✓ |
| [AI Gateway](/docs/observability/insights#ai-gateway) | ✓ | ✓ |
| [External Rewrites](/docs/observability/insights#external-rewrites) | ✓ | ✓ |
| [Microfrontends](/docs/observability/insights#microfrontends) | ✓ | ✓ |

## [Tracked events](#tracked-events)

Vercel tracks the following event types for Observability:

*   Edge Requests
*   Vercel Functions Invocations
*   Edge Functions Invocations
*   External API Requests
*   Routing Middleware Invocations
*   AI Gateway Requests

Vercel creates one or more of these events each time a request is made to your site. Depending on your application and configuration a single request to Vercel might be:

*   1 edge request event if it's cached.
*   1 Edge Request, 1 Middleware, 1 Function Invocation, 2 External API calls, and 1 AI Gateway request, for a total of 6 events.
*   1 edge request event if it's a static asset.

Events are tracked on a team level, and so the events are counted across all projects in the team.

## [Pricing and limitations](#pricing-and-limitations)

Users on all plans can use Observability at no additional cost, with some [limitations](/docs/observability/observability-plus#limitations). The Observability tab is available on the project dashboard for all projects in the team.

[Owners](/docs/rbac/access-roles#owner-role) on Pro and Enterprise teams can [upgrade](/docs/observability/observability-plus#enabling-observability-plus) to Observability Plus to get access to additional features higher limits, and increased retention.

For more information on pricing, see [Pricing](/docs/observability/observability-plus#pricing).

## [Existing Monitoring users](#existing-monitoring-users)

Monitoring is now automatically included with [Observability Plus](/docs/observability/observability-plus) and cannot be purchased separately. For existing Monitoring users, [the Monitoring tab](/docs/observability/monitoring) on your dashboard will continue to exist and can be used in the same way that you've always used it.

Teams that are currently paying for Monitoring, will not automatically see the [Observability Plus](/docs/observability/observability-plus) features and benefits on the Observability tab, but will be able to see [reduced pricing](/changelog/monitoring-pricing-reduced-up-to-87). In order to use [Observability Plus](/docs/observability/observability-plus) you should [migrate using the modal](/docs/observability/observability-plus#enabling-observability-plus). Once you upgrade to Observability Plus, you cannot roll back to the original Monitoring plan. To learn more, see [Monitoring Limits and Pricing](/docs/observability/monitoring/limits-and-pricing).

In addition, teams that subscribe to [Observability Plus](/docs/observability/observability-plus) will have access to the Monitoring tab and its features.

--------------------------------------------------------------------------------
title: "Observability Insights"
description: "List of available data sources that you can view and monitor with Observability on Vercel."
last_updated: "null"
source: "https://vercel.com/docs/observability/insights"
--------------------------------------------------------------------------------

# Observability Insights

Copy page

Ask AI about this page

Last updated October 31, 2025

Vercel organizes Observability through sections that correspond to different features and traffic sources that you can view, monitor and filter.

## [Vercel Functions](#vercel-functions)

The Vercel Functions tab provides a detailed view of the performance of your Vercel Functions. You can see the number of invocations and the error rate of your functions. You can also see the performance of your functions broken down by route.

For more information, see [Vercel Functions](/docs/functions). See [understand the cost impact of function invocations](/guides/understand-cost-impact-of-function-invocations) for more information on how to optimize your functions.

### [CPU Throttling](#cpu-throttling)

When your function uses too much CPU time, Vercel pauses its execution periodically to stay within limits. This means your function may take longer to complete, which, in a worst-case scenario, can cause timeouts or slow responses for users.

CPU throttling itself isn't necessarily a problem as it's designed to keep functions within their resource limits. Some throttling is normal when your functions are making full use of their allocated resources. In general, low throttling rates (under 10% on average) aren't an issue. However, if you're seeing high latency, timeouts, or slow response times, check your CPU throttling metrics. High throttling rates can help explain why your functions are performing poorly, even when your code is optimized.

To reduce throttling, optimize heavy computations, add caching, or increase the memory size of the affected functions.

## [External APIs](#external-apis)

You can use the External APIs tab to understand more information about requests from your functions to external APIs. You can organize by number of requests, p75 (latency), and error rate to help you understand potential causes for slow upstream times or timeouts.

### [External APIs Recipes](#external-apis-recipes)

*   [Investigate Latency Issues and Slowness on Vercel](/guides/investigate-latency-issues-and-slowness)

## [Middleware](#middleware)

The Middleware observability tab shows invocation counts and performance metrics of your application's middleware.

Observability Plus users receive additional insights and tooling:

*   Analyze invocations by request path, matched against your middleware config
*   Break down middleware actions by type (e.g., redirect, rewrite)
*   View rewrite targets and frequency
*   Query middleware invocations using the query builder

## [Edge Requests](#edge-requests)

You can use the Edge Requests tab to understand the requests to each of static and dynamic routes through the edge network. This includes the number of requests, the regions, and the requests that have been cached for each route.

It also provides detailed breakdowns for individual bots and bot categories, including AI crawlers and search engines.

Additionally, Observability Plus users can:

*   Filter traffic by bot category, such as AI
*   View metrics for individual bots
*   Break down traffic by bot or category in the query builder
*   Filter traffic by redirect location
*   Break down traffic by redirect location in the query builder

## [Fast Data Transfer](#fast-data-transfer)

You can use the Fast Data Transfer tab to understand how data is being transferred within the edge network for your project.

For more information, see [Fast Data Transfer](/docs/manage-cdn-usage#fast-data-transfer).

## [Image Optimization](#image-optimization)

The Image Optimization tab provides deeper insights into image transformations and efficiency.

It contains:

*   Transformation insights: View formats, quality settings, and width adjustments
*   Optimization analysis: Identify high-frequency transformations to help inform caching strategies
*   Bandwidth savings: Compare transformed images against their original sources to measure bandwidth reduction and efficiency
*   Image-specific views: See all referrers and unique variants of an optimized image in one place

For more information, see [Image Optimization](/docs/image-optimization).

## [ISR (Incremental Static Regeneration)](#isr-incremental-static-regeneration)

You can use the ISR tab to understand your revalidations and cache hit ratio to help you optimize towards cached requests by default.

For more information on ISR, see [Incremental Static Regeneration](/docs/incremental-static-regeneration).

## [Blob](#blob)

Use the Vercel Blob tab to gain visibility into how Blob stores are used across your applications. It allows you to understand usage patterns, identify inefficiencies, and optimize how your application stores and serves assets.

At the team level, you will access:

*   Total data transfer
*   Download volume
*   Cache activity
*   API operations

You can also drill into activity by user agent, edge region, and client IP.

Learn more about [Vercel Blob](/docs/storage/vercel-blob).

## [Build Diagnostics](#build-diagnostics)

You can use the Build Diagnostics tab to view the performance of your builds. You can see the build time and resource usage for each of your builds. In addition, you can see the build time broken down by each step in the build and deploy process.

To learn more, see [Builds](/docs/deployments/builds).

## [AI Gateway](#ai-gateway)

With the AI Gateway you can switch between ~100 AI models without needing to manage API keys, rate limits, or provider accounts.

The AI Gateway tab surfaces metrics related to the AI Gateway, and provides visibility into:

*   Requests by model
*   Time to first token (TTFT)
*   Request duration
*   Input/output token count
*   Cost per request (free while in alpha)

You can view these metrics across all projects or drill into per-project and per-model usage to understand which models are performing well, how they compare on latency, and what each request would cost in production.

For more information, see [the AI Gateway announcement](/blog/ai-gateway).

## [Sandbox](#sandbox)

With [Vercel Sandbox](/docs/vercel-sandbox), you can safely run untrusted or user-generated code on Vercel in an ephemeral compute primitive using the `@vercel/sandbox` SDK.

In the Sandboxes section (under Compute) of the Observability tab of a Vercel project, you can view a list of sandboxes that were started for this project. For each sandbox, you can see:

*   Time started
*   Status such as pending or stopped
*   Runtime such as `node22`
*   Resources such as `4x CPU 8.19 KB`
*   Duration it ran for

Clicking on a sandbox item from the list takes you to the detail page that provides detailed information, including the URL and port of the sandbox.

## [External Rewrites](#external-rewrites)

The External Rewrites tab gives you visibility into how your external rewrites are performing at both the team and project levels. For each external rewrite, you can see:

*   Total external rewrites
*   External rewrites by hostnames

Additionally, Observability Plus users can view:

*   External rewrite connection latency
*   External rewrites by source/destination paths

To learn more, see [External Rewrites](/docs/rewrites#external-rewrites).

## [Microfrontends](#microfrontends)

Vercel's microfrontends support allows you to split large applications into smaller ones to move faster and develop with independent tech stacks.

The Microfrontends tab provides visibility into microfrontends routing on Vercel:

*   The response reason from the microfrontends routing logic
*   The path expression used to route the request to that microfrontend

For more information, see [Microfrontends](/docs/microfrontends).

--------------------------------------------------------------------------------
title: "Observability Plus"
description: "Learn about using Observability Plus and its limits."
last_updated: "null"
source: "https://vercel.com/docs/observability/observability-plus"
--------------------------------------------------------------------------------

# Observability Plus

Copy page

Ask AI about this page

Last updated October 22, 2025

Observability Plus is an optional upgrade that enables Pro and Enterprise teams to explore data at a more granular level, helping you to pinpoint exactly when and why issues occurred.

To learn more about Observability Plus, see [Limitations](#limitations) or [pricing](#pricing).

## [Using Observability Plus](#using-observability-plus)

### [Enabling Observability Plus](#enabling-observability-plus)

By default, all users on all plans have access to Observability at both a team and project level.

To upgrade to Observability Plus:

1.  From your [dashboard](/dashboard), navigate to [the Observability tab](https://vercel.com/d?to=%2F%5Bteam%5D%2F%7E%2Fobservability&title=Try+Observability).
2.  Next to the time range selector, click the button and select Upgrade to Observability Plus.
3.  From the Upgrade to Observability Plus modal, click Continue.
    *   If you're an existing Monitoring user, the modal will be Migrate from Monitoring to Observability Plus and will display the reduced pricing.
    *   If you're an Enterprise user, you may be prompted to Contact Support to upgrade.
4.  Then, view the charges and click Confirm and Pay.

You'll be charged and upgraded immediately. You will immediately have access to the Observability Plus features and can view [events](/docs/observability#tracked-events) based on data that was collected before you enabled it.

{"@context":"https://schema.org","@type":"HowTo","name":"Enabling Observability Plus","step":\[{"@type":"HowToStep","text":"From your dashboard, navigate to the Observability tab"},{"@type":"HowToStep","text":"Next to the time range selector, click the ellipsis button and select Upgrade to Observability Plus"},{"@type":"HowToStep","text":"From the Upgrade to Observability Plus modal, click Continue"},{"@type":"HowToStep","text":"View the charges and click Confirm and Pay"}\]}

### [Disabling Observability Plus](#disabling-observability-plus)

1.  From your [dashboard](/dashboard), navigate to [the Observability tab](https://vercel.com/d?to=%2F%5Bteam%5D%2F%7E%2Fobservability).
2.  Next to the time range selector, click the button and select Observability Settings.
3.  This takes you to the [Observability Plus section of your project's Billing settings](https://vercel.com/d?to=%2F%5Bteam%5D%2F%7E%2Fsettings/billing#observability)
    *   Click the toggle button to disable it
    *   Click the Confirm button in the Turn off Observability Plus dialog

{"@context":"https://schema.org","@type":"HowTo","name":"Disabling Observability Plus","step":\[{"@type":"HowToStep","text":"From your dashboard, navigate to the Observability tab"},{"@type":"HowToStep","text":"Next to the time range selector, click the ellipsis button and select Observability Settings"},{"@type":"HowToStep","text":"From the Observability Plus section of your project's Billing settings, click the toggle button to disable it"},{"@type":"HowToStep","text":"Click the Confirm button in the Turn off Observability Plus dialog"}\]}

## [Pricing](#pricing)

Users on all plans can use Observability at no additional cost, with some [limitations](#limitations). Observability is available for all projects in the team.

Owners on Pro and Enterprise teams can upgrade to Observability Plus to get access to additional features, the [Monitoring](/docs/observability/monitoring) tab, higher limits, and increased retention. See the table below for more details on pricing:

| Resource | Base Fee | Usage-based pricing |
| --- | --- | --- |
| Observability Plus  
**(Add-on for Pro and Enterprise)** | Pro: $10/month  
Enterprise: none | $1.20 per 1 million [events](/docs/observability#tracked-events) |

## [Limitations](#limitations)

| Feature | Observability | Observability Plus |
| --- | --- | --- |
| Data Retention | Hobby: 12 hours  
Pro: 1 day  
Enterprise: 3 days | 30 days |
| Monitoring access | Not Included | Included.  
See [Existing monitoring users](/docs/observability#existing-monitoring-users) for more information |
| Vercel Functions | No Latency (p75) data, no breakdown by path | Latency data, sort by p75, breakdown by path and routes |
| External APIs | No ability to sort by error rate or p75 duration, only request totals for each hostname | Sorting and filtering by requests, p75 duration, and duration. Latency, Requests, API Endpoint and function calls for each hostname |
| Edge Requests | No breakdown by path | Full request data |
| Fast Data Transfer | No breakdown by path | Full request data |
| ISR (Incremental Static Regeneration) | No access to average duration or revalidation data. Limited function data for each route | Access to sorting and filtering by duration and revalidation. Full function data for each route |
| Build Diagnostics | Full access | Full access |
| In-function Concurrency | Full access when enabled | Full access when enabled |
| Runtime logs | Hobby: 1 hour  
Pro: 1 day  
Enterprise: 3 days | 30 days, max selection window of 14 consecutive days |

## [Prorating](#prorating)

Pro teams are charged a base fee when enabling Observability Plus. However, you will only be charged for the remaining time in your billing cycle. For example,

*   If ten days remain in your current billing cycle, you will only pay around $3. For every new billing cycle after that, you'll be charged a total of $10 at the beginning of the cycle.
*   Events are prorated. This means that if your team incurs 100K events over the included allotment, you would will only pay $0.12 over the base fee. Not $1.20 and the base fee.
*   Suppose you disable Observability Plus before the billing cycle ends. In that case, Observability Plus will automatically turn off, we will stop collecting events, and you will lose access to existing data. Also, you cannot export the Observability Plus data for later use.
*   Once the billing cycle is over, you will be charged for the events collected prior to disabling. You won't be refunded any amounts already paid.
*   Re-enabling Observability Plus before the end of the billing cycle won't cost you another base fee. Instead, the usual base fee of $10 will apply at the beginning of every upcoming billing cycle.

--------------------------------------------------------------------------------
title: "Open Graph (OG) Image Generation"
description: "Learn how to optimize social media image generation through the Open Graph Protocol and @vercel/og library."
last_updated: "null"
source: "https://vercel.com/docs/og-image-generation"
--------------------------------------------------------------------------------

# Open Graph (OG) Image Generation

Copy page

Ask AI about this page

Last updated September 15, 2025

To assist with generating dynamic [Open Graph (OG)](https://ogp.me/) images, you can use the Vercel `@vercel/og` library to compute and generate social card images using [Vercel Functions](/docs/functions).

## [Benefits](#benefits)

*   Performance: With a small amount of code needed to generate images, [functions](/docs/functions) can be started almost instantly. This allows the image generation process to be fast and recognized by tools like the [Open Graph Debugger](https://en.rakko.tools/tools/9/)
*   Ease of use: You can define your images using HTML and CSS and the library will dynamically generate images from the markup
*   Cost-effectiveness: `@vercel/og` automatically adds the correct headers to cache computed images at the edge, helping reduce cost and recomputation

## [Supported features](#supported-features)

*   Basic CSS layouts including flexbox and absolute positioning
*   Custom fonts, text wrapping, centering, and nested images
*   Ability to download the subset characters of the font from Google Fonts
*   Compatible with any framework and application deployed on Vercel
*   View your OG image and other metadata before your deployment goes to production through the [Open Graph](/docs/deployments/og-preview) tab

## [Runtime support](#runtime-support)

Vercel OG image generation is supported on the [Node.js runtime](/docs/functions/runtimes/node-js).

Local resources can be loaded directly using `fs.readFile`. Alternatively, `fetch` can be used to load remote resources.

og.js

```
const fs = require('fs').promises;
 
const loadLocalImage = async () => {
  const imageData = await fs.readFile('/path/to/image.png');
  // Process image data
};
```

### [Runtime caveats](#runtime-caveats)

There are limitations when using `vercel/og` with the Next.js Pages Router and the Node.js runtime. Specifically, this combination does not support the `return new Response(…)` syntax. The table below provides a breakdown of the supported syntaxes for different configurations.

| Configuration | Supported Syntax | Notes |
| --- | --- | --- |
| `pages/` + Edge runtime | `return new Response(…)` | Fully supported. |
| `app/` + Node.js runtime | `return new Response(…)` | Fully supported. |
| `app/` + Edge runtime | `return new Response(…)` | Fully supported. |
| `pages/` + Node.js runtime | Not supported | Does not support `return new Response(…)` syntax with `vercel/og`. |

## [Usage](#usage)

### [Requirements](#requirements)

*   Install Node.js 22 or newer by visiting [nodejs.org](https://nodejs.org)
*   Install `@vercel/og` by running the following command inside your project directory. This isn't required for Next.js App Router projects, as the package is already included:

pnpmyarnnpmbun

```
pnpm i @vercel/og
```

*   For Next.js implementations, make sure you are using Next.js v12.2.3 or newer
*   Create API endpoints that you can call from your front-end to generate the images. Since the HTML code for generating the image is included as one of the parameters of the `ImageResponse` function, the use of `.jsx` or `.tsx` files is recommended as they are designed to handle this kind of syntax
*   To avoid the possibility of social media providers not being able to fetch your image, it is recommended to add your OG image API route(s) to `Allow` inside your `robots.txt` file. For example, if your OG image API route is `/api/og/`, you can add the following line:
    
    robots.txt
    
    ```
    Allow: /api/og/*
    ```
    
    If you are using Next.js, review [robots.txt](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/robots#static-robotstxt) to learn how to add or generate a `robots.txt` file.

### [Getting started](#getting-started)

Get started with an example that generates an image from static text using Next.js by setting up a new app with the following command:

pnpmyarnnpmbun

```
pnpm create next-app
```

Create an API endpoint by adding `route.tsx` under the `app/api/og` directory in the root of your project.

Then paste the following code:

Next.js (/app)Next.js (/pages)Other frameworks

app/api/og/route.tsx

TypeScript

TypeScriptJavaScript

```
import { ImageResponse } from 'next/og';
// App router includes @vercel/og.
// No need to install it.
 
export async function GET() {
  return new ImageResponse(
    (
      <div
        style={{
          fontSize: 40,
          color: 'black',
          background: 'white',
          width: '100%',
          height: '100%',
          padding: '50px 200px',
          textAlign: 'center',
          justifyContent: 'center',
          alignItems: 'center',
        }}
      >
        👋 Hello
      </div>
    ),
    {
      width: 1200,
      height: 630,
    },
  );
}
```

If you're not using a framework, you must either add `"type": "module"` to your `package.json` or change your JavaScript Functions' file extensions from `.js` to `.mjs`

Run the following command:

pnpmyarnnpmbun

```
pnpm dev
```

Then, browse to `http://localhost:3000/api/og`. You will see the following image:

![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Ffunctions%2Fog-image%2Fog-language.png&w=3840&q=75)

### [Consume the OG route](#consume-the-og-route)

Deploy your project to obtain a publicly accessible path to the OG image API endpoint. You can find an example deployment at [https://og-examples.vercel.sh/api/static](https://og-examples.vercel.sh/api/static).

Then, based on the [Open Graph Protocol](https://ogp.me/#metadata), create the web content for your social media post as follows:

*   Create a `<meta>` tag inside the `<head>` of the webpage
*   Add the `property` attribute with value `og:image` to the `<meta>` tag
*   Add the `content` attribute with value as the absolute path of the `/api/og` endpoint to the `<meta>` tag

With the example deployment at [https://og-examples.vercel.sh/api/static](https://og-examples.vercel.sh/api/static), use the following code:

index.js

```
<head>
  <title>Hello world</title>
  <meta
    property="og:image"
    content="https://og-examples.vercel.sh/api/static"
  />
</head>
```

Every time you create a new social media post, you need to update the API endpoint with the new content. However, if you identify which parts of your `ImageResponse` will change for each post, you can then pass those values as parameters of the endpoint so that you can use the same endpoint for all your posts.

In the examples below, we explore using parameters and including other types of content with `ImageResponse`.

## [Examples](#examples)

*   [Dynamic title](/docs/og-image-generation/examples#dynamic-title): Passing the image title as a URL parameter
*   [Dynamic external image](/docs/og-image-generation/examples#dynamic-external-image): Passing the username as a URL parameter to pull an external profile image for the image generation
*   [Emoji](/docs/og-image-generation/examples#emoji): Using emojis to generate the image
*   [SVG](/docs/og-image-generation/examples#svg): Using SVG embedded content to generate the image
*   [Custom font](/docs/og-image-generation/examples#custom-font): Using a custom font available in the file system to style your image title
*   [Tailwind CSS](/docs/og-image-generation/examples#tailwind-css): Using Tailwind CSS (Experimental) to style your image content
*   [Internationalization](/docs/og-image-generation/examples#internationalization): Using other languages in the text for generating your image
*   [Secure URL](/docs/og-image-generation/examples#secure-url): Encrypting parameters so that only certain values can be passed to generate your image

## [Technical details](#technical-details)

*   Recommended OG image size: 1200x630 pixels
*   `@vercel/og` uses [Satori](https://github.com/vercel/satori) and Resvg to convert HTML and CSS into PNG
*   `@vercel/og` [API reference](/docs/og-image-generation/og-image-api)

## [Limitations](#limitations)

*   Only `ttf`, `otf`, and `woff` font formats are supported. To maximize the font parsing speed, `ttf` or `otf` are preferred over `woff`
*   Only flexbox (`display: flex`) and a subset of CSS properties are supported. Advanced layouts (`display: grid`) will not work. See [Satori](https://github.com/vercel/satori)'s documentation for more details on supported CSS properties
*   Maximum bundle size of 500KB. The bundle size includes your JSX, CSS, fonts, images, and any other assets. If you exceed the limit, consider reducing the size of any assets or fetching at runtime

--------------------------------------------------------------------------------
title: "OG Image Generation Examples"
description: "Learn how to use the @vercel/og library with examples."
last_updated: "null"
source: "https://vercel.com/docs/og-image-generation/examples"
--------------------------------------------------------------------------------

# OG Image Generation Examples

Copy page

Ask AI about this page

Last updated April 28, 2025

## [Dynamic title](#dynamic-title)

Create an api route with `route.tsx` in `/app/api/og/` and paste the following code:

Next.js (/app)Next.js (/pages)Other frameworks

app/api/og/route.tsx

TypeScript

TypeScriptJavaScript

```
import { ImageResponse } from 'next/og';
// App router includes @vercel/og.
// No need to install it.
 
export async function GET(request: Request) {
  try {
    const { searchParams } = new URL(request.url);
 
    // ?title=<title>
    const hasTitle = searchParams.has('title');
    const title = hasTitle
      ? searchParams.get('title')?.slice(0, 100)
      : 'My default title';
 
    return new ImageResponse(
      (
        <div
          style={{
            backgroundColor: 'black',
            backgroundSize: '150px 150px',
            height: '100%',
            width: '100%',
            display: 'flex',
            textAlign: 'center',
            alignItems: 'center',
            justifyContent: 'center',
            flexDirection: 'column',
            flexWrap: 'nowrap',
          }}
        >
          <div
            style={{
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              justifyItems: 'center',
            }}
          >
            <img
              alt="Vercel"
              height={200}
              src="data:image/svg+xml,%3Csvg width='116' height='100' fill='white' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M57.5 0L115 100H0L57.5 0z' /%3E%3C/svg%3E"
              style={{ margin: '0 30px' }}
              width={232}
            />
          </div>
          <div
            style={{
              fontSize: 60,
              fontStyle: 'normal',
              letterSpacing: '-0.025em',
              color: 'white',
              marginTop: 30,
              padding: '0 120px',
              lineHeight: 1.4,
              whiteSpace: 'pre-wrap',
            }}
          >
            {title}
          </div>
        </div>
      ),
      {
        width: 1200,
        height: 630,
      },
    );
  } catch (e: any) {
    console.log(`${e.message}`);
    return new Response(`Failed to generate the image`, {
      status: 500,
    });
  }
}
```

## [Dynamic external image](#dynamic-external-image)

Create an api route with `route.tsx` in `/app/api/og/` and paste the following code:

Next.js (/app)Next.js (/pages)Other frameworks

app/api/og/route.tsx

TypeScript

TypeScriptJavaScript

```
import { ImageResponse } from 'next/og';
// App router includes @vercel/og.
// No need to install it.
 
export async function GET(request: Request) {
  const { searchParams } = new URL(request.url);
  const username = searchParams.get('username');
  if (!username) {
    return new ImageResponse(<>Visit with &quot;?username=vercel&quot;</>, {
      width: 1200,
      height: 630,
    });
  }
 
  return new ImageResponse(
    (
      <div
        style={{
          display: 'flex',
          fontSize: 60,
          color: 'black',
          background: '#f6f6f6',
          width: '100%',
          height: '100%',
          paddingTop: 50,
          flexDirection: 'column',
          justifyContent: 'center',
          alignItems: 'center',
        }}
      >
        <img
          width="256"
          height="256"
          src={`https://github.com/${username}.png`}
          style={{
            borderRadius: 128,
          }}
        />
        <p>github.com/{username}</p>
      </div>
    ),
    {
      width: 1200,
      height: 630,
    },
  );
}
```

## [Emoji](#emoji)

Create an api route with `route.tsx` in `/app/api/og/` and paste the following code:

Next.js (/app)Next.js (/pages)Other frameworks

app/api/og/route.tsx

TypeScript

TypeScriptJavaScript

```
import { ImageResponse } from 'next/og';
// App router includes @vercel/og.
// No need to install it.
 
export async function GET() {
  return new ImageResponse(
    (
      <div
        style={{
          fontSize: 100,
          color: 'black',
          background: 'white',
          width: '100%',
          height: '100%',
          padding: '50px 200px',
          textAlign: 'center',
          justifyContent: 'center',
          alignItems: 'center',
        }}
      >
        👋, 🌎
      </div>
    ),
    {
      width: 1200,
      height: 630,
      // Supported options: 'twemoji', 'blobmoji', 'noto', 'openmoji', 'fluent' and 'fluentFlat'
      // Default to 'twemoji'
      emoji: 'twemoji',
    },
  );
}
```

## [SVG](#svg)

Create an api route with `route.tsx` in `/app/api/og/` and paste the following code:

Next.js (/app)Next.js (/pages)Other frameworks

app/api/og/route.tsx

TypeScript

TypeScriptJavaScript

```
import { ImageResponse } from 'next/og';
// App router includes @vercel/og.
// No need to install it.
 
export async function GET() {
  return new ImageResponse(
    (
      <div
        style={{
          display: 'flex',
          fontSize: 40,
          color: 'black',
          background: 'white',
          width: '100%',
          height: '100%',
          textAlign: 'center',
          justifyContent: 'center',
          alignItems: 'center',
        }}
      >
        <svg fill="black" viewBox="0 0 284 65">
          <path d="M141.68 16.25c-11.04 0-19 7.2-19 18s8.96 18 20 18c6.67 0 12.55-2.64 16.19-7.09l-7.65-4.42c-2.02 2.21-5.09 3.5-8.54 3.5-4.79 0-8.86-2.5-10.37-6.5h28.02c.22-1.12.35-2.28.35-3.5 0-10.79-7.96-17.99-19-17.99zm-9.46 14.5c1.25-3.99 4.67-6.5 9.45-6.5 4.79 0 8.21 2.51 9.45 6.5h-18.9zm117.14-14.5c-11.04 0-19 7.2-19 18s8.96 18 20 18c6.67 0 12.55-2.64 16.19-7.09l-7.65-4.42c-2.02 2.21-5.09 3.5-8.54 3.5-4.79 0-8.86-2.5-10.37-6.5h28.02c.22-1.12.35-2.28.35-3.5 0-10.79-7.96-17.99-19-17.99zm-9.45 14.5c1.25-3.99 4.67-6.5 9.45-6.5 4.79 0 8.21 2.51 9.45 6.5h-18.9zm-39.03 3.5c0 6 3.92 10 10 10 4.12 0 7.21-1.87 8.8-4.92l7.68 4.43c-3.18 5.3-9.14 8.49-16.48 8.49-11.05 0-19-7.2-19-18s7.96-18 19-18c7.34 0 13.29 3.19 16.48 8.49l-7.68 4.43c-1.59-3.05-4.68-4.92-8.8-4.92-6.07 0-10 4-10 10zm82.48-29v46h-9v-46h9zM37.59.25l36.95 64H.64l36.95-64zm92.38 5l-27.71 48-27.71-48h10.39l17.32 30 17.32-30h10.39zm58.91 12v9.69c-1-.29-2.06-.49-3.2-.49-5.81 0-10 4-10 10v14.8h-9v-34h9v9.2c0-5.08 5.91-9.2 13.2-9.2z" />
        </svg>
      </div>
    ),
    {
      width: 1200,
      height: 630,
    },
  );
}
```

## [Custom font](#custom-font)

Create an api route with `route.tsx` in `/app/api/og/` and paste the following code:

Next.js (/app)Next.js (/pages)Other frameworks

app/api/og/route.tsx

TypeScript

TypeScriptJavaScript

```
import { ImageResponse } from 'next/og';
// App router includes @vercel/og.
// No need to install it.
 
async function loadGoogleFont (font: string, text: string) {
  const url = `https://fonts.googleapis.com/css2?family=${font}&text=${encodeURIComponent(text)}`
  const css = await (await fetch(url)).text()
  const resource = css.match(/src: url\((.+)\) format\('(opentype|truetype)'\)/)
 
  if (resource) {
    const response = await fetch(resource[1])
    if (response.status == 200) {
      return await response.arrayBuffer()
    }
  }
 
  throw new Error('failed to load font data')
}
 
export async function GET() {
  const text = 'Hello world!'
 
  return new ImageResponse(
    (
      <div
        style={{
          backgroundColor: 'white',
          height: '100%',
          width: '100%',
          fontSize: 100,
          fontFamily: 'Geist',
          paddingTop: '100px',
          paddingLeft: '50px',
        }}
      >
        {text}
      </div>
    ),
    {
      width: 1200,
      height: 630,
      fonts: [
        {
          name: 'Geist',
          data: await loadGoogleFont('Geist', text),
          style: 'normal',
        },
      ],
    },
  );
}
```

## [Tailwind CSS](#tailwind-css)

Create an api route with `route.tsx` in `/app/api/og/` and paste the following code:

Next.js (/app)Next.js (/pages)Other frameworks

app/api/og/route.tsx

TypeScript

TypeScriptJavaScript

```
import { ImageResponse } from 'next/og';
// App router includes @vercel/og.
// No need to install it.
 
export async function GET() {
  return new ImageResponse(
    (
      // Modified based on https://tailwindui.com/components/marketing/sections/cta-sections
      <div
        style={{
          height: '100%',
          width: '100%',
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          justifyContent: 'center',
          backgroundColor: 'white',
        }}
      >
        <div tw="bg-gray-50 flex">
          <div tw="flex flex-col md:flex-row w-full py-12 px-4 md:items-center justify-between p-8">
            <h2 tw="flex flex-col text-3xl sm:text-4xl font-bold tracking-tight text-gray-900 text-left">
              <span>Ready to dive in?</span>
              <span tw="text-indigo-600">Start your free trial today.</span>
            </h2>
            <div tw="mt-8 flex md:mt-0">
              <div tw="flex rounded-md shadow">
                <a
                  href="#"
                  tw="flex items-center justify-center rounded-md border border-transparent bg-indigo-600 px-5 py-3 text-base font-medium text-white"
                >
                  Get started
                </a>
              </div>
              <div tw="ml-3 flex rounded-md shadow">
                <a
                  href="#"
                  tw="flex items-center justify-center rounded-md border border-transparent bg-white px-5 py-3 text-base font-medium text-indigo-600"
                >
                  Learn more
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>
    ),
    {
      width: 1200,
      height: 630,
    },
  );
}
```

## [Internationalization](#internationalization)

Create an api route with `route.tsx` in `/app/api/og/` and paste the following code:

Next.js (/app)Next.js (/pages)Other frameworks

app/api/og/route.tsx

TypeScript

TypeScriptJavaScript

```
import { ImageResponse } from 'next/og';
// App router includes @vercel/og.
// No need to install it.
 
export async function GET() {
  return new ImageResponse(
    (
      <div
        style={{
          fontSize: 40,
          color: 'black',
          background: 'white',
          width: '100%',
          height: '100%',
          padding: '50px 200px',
          textAlign: 'center',
          justifyContent: 'center',
          alignItems: 'center',
        }}
      >
        👋 Hello 你好 नमस्ते こんにちは สวัสดีค่ะ 안녕 добрий день Hallá
      </div>
    ),
    {
      width: 1200,
      height: 630,
    },
  );
}
```

## [Secure URL](#secure-url)

Next.js (/app)Next.js (/pages)Other frameworks

app/api/encrypted/route.tsx

TypeScript

TypeScriptJavaScript

```
import { ImageResponse } from 'next/og';
// App router includes @vercel/og.
// No need to install it.
 
const key = crypto.subtle.importKey(
  'raw',
  new TextEncoder().encode('my_secret'),
  { name: 'HMAC', hash: { name: 'SHA-256' } },
  false,
  ['sign'],
);
 
function toHex(arrayBuffer: ArrayBuffer) {
  return Array.prototype.map
    .call(new Uint8Array(arrayBuffer), (n) => n.toString(16).padStart(2, '0'))
    .join('');
}
 
export async function GET(request: Request) {
  const { searchParams } = new URL(request.url);
 
  const id = searchParams.get('id');
  const token = searchParams.get('token');
 
  const verifyToken = toHex(
    await crypto.subtle.sign(
      'HMAC',
      await key,
      new TextEncoder().encode(JSON.stringify({ id })),
    ),
  );
 
  if (token !== verifyToken) {
    return new Response('Invalid token.', { status: 401 });
  }
 
  return new ImageResponse(
    (
      <div
        style={{
          display: 'flex',
          fontSize: 40,
          color: 'black',
          background: 'white',
          width: '100%',
          height: '100%',
          padding: '50px 200px',
          textAlign: 'center',
          justifyContent: 'center',
          alignItems: 'center',
        }}
      >
        <h1>Card generated, id={id}.</h1>
      </div>
    ),
    {
      width: 1200,
      height: 630,
    },
  );
}
```

Create the dynamic route `[id]/page` under `/app/encrypted` and paste the following code:

Next.js (/app)Next.js (/pages)Other frameworks

app/encrypted/\[id\]/page.tsx

TypeScript

TypeScriptJavaScript

```
// This page generates the token to prevent generating OG images with random parameters (`id`).
import { createHmac } from 'node:crypto';
 
function getToken(id: string): string {
  const hmac = createHmac('sha256', 'my_secret');
  hmac.update(JSON.stringify({ id: id }));
  const token = hmac.digest('hex');
  return token;
}
 
interface PageParams {
  params: {
    id: string;
  };
}
 
export default function Page({ params }: PageParams) {
  console.log(params);
  const { id } = params;
  const token = getToken(id);
 
  return (
    <div>
      <h1>Encrypted Open Graph Image.</h1>
      <p>Only /a, /b, /c with correct tokens are accessible:</p>
      <a
        href={`/api/encrypted?id=${id}&token=${token}`}
        target="_blank"
        rel="noreferrer"
      >
        <code>
          /api/encrypted?id={id}&token={token}
        </code>
      </a>
    </div>
  );
}
```

--------------------------------------------------------------------------------
title: "@vercel/og Reference"
description: "This reference provides information on how the @vercel/og package works on Vercel."
last_updated: "null"
source: "https://vercel.com/docs/og-image-generation/og-image-api"
--------------------------------------------------------------------------------

# @vercel/og Reference

Copy page

Ask AI about this page

Last updated July 18, 2025

The package exposes an `ImageResponse` constructor, with the following parameters:

ImageResponse Interface

TypeScript

TypeScriptJavaScript

```
import { ImageResponse } from '@vercel/og'
 
new ImageResponse(
  element: ReactElement,
  options: {
    width?: number = 1200
    height?: number = 630
    emoji?: 'twemoji' | 'blobmoji' | 'noto' | 'openmoji' = 'twemoji',
    fonts?: {
      name: string,
      data: ArrayBuffer,
      weight: number,
      style: 'normal' | 'italic'
    }[]
    debug?: boolean = false
 
    // Options that will be passed to the HTTP response
    status?: number = 200
    statusText?: string
    headers?: Record<string, string>
  },
)
```

### [Main parameters](#main-parameters)

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `element` | `ReactElement` | — | The React element to generate the image from. |
| `options` | `object` | — | Options to customize the image and HTTP response. |

### [Options parameters](#options-parameters)

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `width` | `number` | `1200` | The width of the image. |
| `height` | `number` | `630` | The height of the image. |
| `emoji` | `twemoji` `blobmoji` `noto` `openmoji` `twemoji` | The emoji set to use. |  |
| `debug` | `boolean` | `false` | Debug mode flag. |
| `status` | `number` | `200` | The HTTP status code for the response. |
| `statusText` | `string` | — | The HTTP status text for the response. |
| `headers` | `Record<string, string>` | — | The HTTP headers for the response. |

### [Fonts parameters (within options)](#fonts-parameters-within-options)

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `name` | `string` | — | The name of the font. |
| `data` | `ArrayBuffer` | — | The font data. |
| `weight` | `number` | — | The weight of the font. |
| `style` | `normal` `italic` | — | The style of the font. |

By default, the following headers will be included by `@vercel/og`:

included-headers

```
'content-type': 'image/png',
'cache-control': 'public, immutable, no-transform, max-age=31536000',
```

## [Supported HTML and CSS features](#supported-html-and-css-features)

Refer to [Satori's documentation](https://github.com/vercel/satori#documentation) for a list of supported HTML and CSS features.

By default, `@vercel/og` only has the Noto Sans font included. If you need to use other fonts, you can pass them in the `fonts` option. View the [custom font example](/docs/recipes/using-custom-font) for more details.

## [Acknowledgements](#acknowledgements)

*   [Twemoji](https://github.com/twitter/twemoji)
*   [Google Fonts](https://fonts.google.com) and [Noto Sans](https://www.google.com/get/noto/)
*   [Resvg](https://github.com/RazrFalcon/resvg) and [Resvg.js](https://github.com/yisibl/resvg-js)

--------------------------------------------------------------------------------
title: "OpenID Connect (OIDC) Federation"
description: "Secure the access to your backend using OIDC Federation to enable auto-generated, short-lived, and non-persistent credentials."
last_updated: "null"
source: "https://vercel.com/docs/oidc"
--------------------------------------------------------------------------------

# OpenID Connect (OIDC) Federation

Copy page

Ask AI about this page

Last updated June 6, 2025

Secure backend access with OIDC federation is available on [all plans](/docs/plans)

When you create long-lived, persistent credentials in your backend to allow access from your web applications, you increase the security risk of these credentials being leaked and hacked. You can mitigate this risk with OpenID Connect (OIDC) federation which issues short-lived, non-persistent tokens that are signed by Vercel's OIDC Identity Provider (IdP).

Cloud providers such as Amazon Web Services, Google Cloud Platform, and Microsoft Azure can trust these tokens and exchange them for short-lived credentials. This way, you can avoid storing long-lived credentials as Vercel environment variables.

### [Benefits](#benefits)

*   No persisted credentials: There is no need to copy and paste long-lived access tokens from your cloud provider into your Vercel environment variables. Instead, you can exchange the OIDC token for short-lived access tokens with your trusted cloud provider
*   Granular access control: You can configure your cloud providers to grant different permissions depending on project or environment. For instance, you can separate your development, preview and production environments on your cloud provider and only grant Vercel issued OIDC tokens access to the necessary environment(s)
*   Local development access: You can configure your cloud provider to trust local development environments so that long-lived credentials do not need to be stored locally

## [Getting started](#getting-started)

To securely connect your deployment with your backend, configure your backend to trust Vercel's OIDC Identity Provider and connect to it from your Vercel deployment:

*   [Connect to Amazon Web Services (AWS)](/docs/oidc/aws)
*   [Connect to Google Cloud Platform (GCP)](/docs/oidc/gcp)
*   [Connect to Microsoft Azure](/docs/oidc/azure)
*   [Connect to your own API](/docs/oidc/api)

## [Issuer mode](#issuer-mode)

There are two options available configure the token's issuer URL (`iss`):

1.  Team _(Recommended)_: The issuer URL is bespoke to your team e.g. `https://oidc.vercel.com/acme`.
2.  Global: The issuer URL is generic e.g. `https://oidc.vercel.com`

To change the issuer mode:

*   Open your project from the Vercel dashboard
*   Select the Settings tab
*   Navigate to Security
*   From Secure backend access with OIDC federation section, toggle between Team or Global and click "Save".

## [How OIDC token federation works](#how-oidc-token-federation-works)

### [In Builds](#in-builds)

When you run a build, Vercel automatically generates a new token and assigns it to the `VERCEL_OIDC_TOKEN` environment variable. You can then exchange the token for short-lived access tokens with your cloud provider.

### [In Vercel Functions](#in-vercel-functions)

When your application invokes a function, the OIDC token is set to the `x-vercel-oidc-token` header on the function's `Request` object.

Vercel does not generate a fresh OIDC token for each execution but caches the token for a maximum of 45 minutes. While the token has a Time to Live (TTL) of 60 minutes, Vercel provides the difference to ensure the token doesn't expire within the lifecycle of a function's maximum execution duration.

### [In Local Development](#in-local-development)

You can download the `VERCEL_OIDC_TOKEN` straight to your local development environment using the CLI command `vercel env pull`.

terminal

```
vercel env pull
```

This writes the `VERCEL_OIDC_TOKEN` environment variable and other environment variables targeted to `development` to the `.env.local` file of your project folder. See the [CLI docs](/docs/cli/env) for more information.

## [Related](#related)

[

#### Helper libraries

Review libraries to help you connect to your backend with OIDC.

](/docs/oidc/reference#helper-libraries)

[

#### OIDC token anatomy

Understand the structure of an OIDC token.

](/docs/oidc/reference#oidc-token-anatomy)

--------------------------------------------------------------------------------
title: "Connect to your own API"
description: "Learn how to configure your own API to trust Vercel's OpenID Connect (OIDC) Identity Provider (IdP)"
last_updated: "null"
source: "https://vercel.com/docs/oidc/api"
--------------------------------------------------------------------------------

# Connect to your own API

Copy page

Ask AI about this page

Last updated October 27, 2025

Secure backend access with OIDC federation is available on [all plans](/docs/plans)

## [Validate the tokens](#validate-the-tokens)

To configure your own API to accept Vercel's OIDC tokens, you need to validate the tokens using Vercel's JSON Web Keys (JWTs), available at `https://oidc.vercel.com/[TEAM_SLUG]/.well-known/jwks` with the team issuer mode, and `https://oidc.vercel.com/.well-known/jwks` for the global issuer mode.

### [Use the `jose.jwtVerify` function](#use-the-jose.jwtverify-function)

Install the following package:

pnpmyarnnpmbun

```
pnpm i jose
```

In the code example below, you use the `jose.jwtVerify` function to verify the token. The `issuer`, `audience`, and `subject` are validated against the token's claims.

server.ts

```
import http from 'node:http';
import * as jose from 'jose';
 
const ISSUER_URL = `https://oidc.vercel.com/[TEAM_SLUG]`;
// or use `https://oidc.vercel.com` if your issuer mode is set to Global.
 
const JWKS = jose.createRemoteJWKSet(new URL(ISSUER_URL, '/.well-known/jwks'));
 
const server = http.createServer((req, res) => {
  const token = req.headers['authorization']?.split('Bearer ')[1];
 
  if (!token) {
    res.statusCode = 401;
    res.end('Unauthorized');
    return;
  }
 
  try {
    const { payload } = jose.jwtVerify(token, JWKS, {
      issuer: ISSUER_URL,
      audience: 'https://vercel.com/[TEAM_SLUG]',
      subject:
        'owner:[TEAM_SLUG]:project:[PROJECT_NAME]:environment:[ENVIRONMENT]',
    });
 
    res.statusCode = 200;
    res.end('OK');
  } catch (error) {
    res.statusCode = 401;
    res.end('Unauthorized');
  }
});
 
server.listen(3000);
```

Make sure that you:

*   Replace `[TEAM_SLUG]` with your team identifier from the Vercel's team URL
*   Replace `[PROJECT_NAME]` with your [project's name](https://vercel.com/docs/projects/overview#project-name) in your [project's settings](https://vercel.com/docs/projects/overview#project-settings)
*   Replace `[ENVIRONMENT]` with one of Vercel's [environments](https://vercel.com/docs/deployments/environments#deployment-environments), `development`, `preview` or `production`

### [Use the `getVercelOidcToken` function](#use-the-getverceloidctoken-function)

Install the following package:

pnpmyarnnpmbun

```
pnpm i @vercel/functions
```

In the code example below, the `getVercelOidcToken` function is used to retrieve the OIDC token from your Vercel environment. You can then use this token to authenticate the request to the external API.

/api/custom-api/route.ts

```
import { getVercelOidcToken } from '@vercel/oidc';
 
export const GET = async () => {
  const result = await fetch('https://api.example.com', {
    headers: {
      Authorization: `Bearer ${await getVercelOidcToken()}`,
    },
  });
 
  return Response.json(await result.json());
};
```

--------------------------------------------------------------------------------
title: "Connect to Amazon Web Services (AWS)"
description: "Learn how to configure your AWS account to trust Vercel's OpenID Connect (OIDC) Identity Provider (IdP)."
last_updated: "null"
source: "https://vercel.com/docs/oidc/aws"
--------------------------------------------------------------------------------

# Connect to Amazon Web Services (AWS)

Copy page

Ask AI about this page

Last updated October 27, 2025

Secure backend access with OIDC federation is available on [all plans](/docs/plans)

To understand how AWS supports OIDC, and for a detailed user guide on creating an OIDC identity provider with AWS, consult the [AWS OIDC documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_oidc.html).

## [Configure your AWS account](#configure-your-aws-account)

1.  ### [Create an OIDC identity provider](#create-an-oidc-identity-provider)
    
    1.  Navigate to the [AWS Console](https://console.aws.amazon.com/)
    2.  Navigate to IAM then Identity Providers
    3.  Select Add Provider
    4.  Select OpenID Connect from the provider type
    5.  Enter the Provider URL, the URL will depend on the issuer mode setting:
        *   Team: `https://oidc.vercel.com/[TEAM_SLUG]`, replacing `[TEAM_SLUG]` with the path from your Vercel team URL
        *   Global: `https://oidc.vercel.com`
    6.  Enter `https://vercel.com/[TEAM_SLUG]` in the Audience field, replacing `[TEAM_SLUG]` with the path from your Vercel team URL
    7.  Select Add Provider
    
    ![Add provider values for the Global issuer mode setting. For the Team issuer mode setting, set the Provider URL to https://vercel.com/[TEAM_SLUG]](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Foidc-tokens%2Faws-create-id-provider.png&w=1080&q=75)![Add provider values for the Global issuer mode setting. For the Team issuer mode setting, set the Provider URL to https://vercel.com/[TEAM_SLUG]](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Foidc-tokens%2Faws-create-id-provider.png&w=1080&q=75)
    
    Add provider values for the Global issuer mode setting. For the Team issuer mode setting, set the Provider URL to https://vercel.com/\[TEAM\_SLUG\]
    
2.  ### [Create an IAM role](#create-an-iam-role)
    
    To use AWS OIDC Federation you must have an [IAM role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html). [IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html) require a "trust relationship" (also known as a "trust policy") that describes which "Principal(s)" are allowed to assume the role under certain "Condition(s)".
    
    Here is an example of a trust policy using the Team issuer mode:
    
    trust-policy.json
    
    ```
    {
      "Version": "2012-10-17",
      "Statement": [
        {
          "Effect": "Allow",
          "Principal": {
            "Federated": "arn:aws:iam::[YOUR AWS ACCOUNT ID]:oidc-provider/oidc.vercel.com/[TEAM_SLUG]"
          },
          "Action": "sts:AssumeRoleWithWebIdentity",
          "Condition": {
            "StringEquals": {
              "oidc.vercel.com/[TEAM_SLUG]:sub": "owner:[TEAM SLUG]:project:[PROJECT NAME]:environment:production",
              "oidc.vercel.com/[TEAM_SLUG]:aud": "https://vercel.com/[TEAM SLUG]"
            }
          }
        }
      ]
    }
    ```
    
    The above policy's conditions are quite strict. It requires the `aud` sub `sub` claims to match exactly, but it's possible to configure less strict trust policies conditions:
    
    trust-policy.json
    
    ```
    {
      "Version": "2012-10-17",
      "Statement": [
        {
          "Effect": "Allow",
          "Principal": {
            "Federated": "arn:aws:iam::[YOUR AWS ACCOUNT ID]:oidc-provider/oidc.vercel.com/[TEAM_SLUG]"
          },
          "Action": "sts:AssumeRoleWithWebIdentity",
          "Condition": {
            "StringEquals": {
              "oidc.vercel.com/[TEAM_SLUG]:aud": "https://vercel.com/[TEAM SLUG]"
            },
            "StringLike": {
              "oidc.vercel.com/[TEAM_SLUG]:sub": [
                "owner:[TEAM SLUG]:project:*:environment:preview",
                "owner:[TEAM SLUG]:project:*:environment:production"
              ]
            }
          }
        }
      ]
    }
    ```
    
    This policy allows any project matched by the `*` that are targeted to `preview` and `production` but not `development`.
    
3.  ### [Define the role ARN as environment variable](#define-the-role-arn-as-environment-variable)
    
    Once you have created the role, copy the [role's ARN](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-arns) and [declare it as an environment variable](/docs/environment-variables#creating-environment-variables) in your Vercel project with key name `AWS_ROLE_ARN`.
    
    .env.local
    
    ```
    AWS_ROLE_ARN=arn:aws:iam::accountid:user/username
    ```
    
    You are now ready to connect to your AWS resource in your project's code. Review the examples below.
    

## [Examples](#examples)

In the following examples, you create a [Vercel function](/docs/functions/quickstart#create-a-vercel-function) in the Vercel project where you have defined the OIDC role ARN environment variable. The function will connect to a specific resource in your AWS backend using OIDC and perform a specific action using the AWS SDK.

### [List objects in an AWS S3 bucket](#list-objects-in-an-aws-s3-bucket)

Install the following packages:

pnpmyarnnpmbun

```
pnpm i @aws-sdk/client-s3 @vercel/functions
```

In the API route for the function, use the AWS SDK for JavaScript to list objects in an S3 bucket with the following code:

/api/aws-s3/route.ts

```
import * as S3 from '@aws-sdk/client-s3';
import { awsCredentialsProvider } from '@vercel/oidc-aws-credentials-provider';
 
const AWS_REGION = process.env.AWS_REGION!;
const AWS_ROLE_ARN = process.env.AWS_ROLE_ARN!;
const S3_BUCKET_NAME = process.env.S3_BUCKET_NAME!;
 
// Initialize the S3 Client
const s3client = new S3.S3Client({
  region: AWS_REGION,
  // Use the Vercel AWS SDK credentials provider
  credentials: awsCredentialsProvider({
    roleArn: AWS_ROLE_ARN,
  }),
});
 
export async function GET() {
  const result = await s3client.send(
    new S3.ListObjectsV2Command({
      Bucket: S3_BUCKET_NAME,
    }),
  );
  return result?.Contents?.map((object) => object.Key) ?? [];
}
```

Vercel sends the OIDC token to the SDK using the `awsCredentialsProvider` function from `@vercel/functions`.

### [Query an AWS RDS instance](#query-an-aws-rds-instance)

Install the following packages:

pnpmyarnnpmbun

```
pnpm i @aws-sdk/rds-signer @vercel/functions pg
```

In the API route for the function, use the AWS SDK for JavaScript to perform a database `SELECT` query from an AWS RDS instance with the following code:

/api/aws-rds/route.ts

```
import { awsCredentialsProvider } from '@vercel/oidc-aws-credentials-provider';
import { Signer } from '@aws-sdk/rds-signer';
import { Pool } from 'pg';
 
const RDS_PORT = parseInt(process.env.RDS_PORT!);
const RDS_HOSTNAME = process.env.RDS_HOSTNAME!;
const RDS_DATABASE = process.env.RDS_DATABASE!;
const RDS_USERNAME = process.env.RDS_USERNAME!;
const AWS_REGION = process.env.AWS_REGION!;
const AWS_ROLE_ARN = process.env.AWS_ROLE_ARN!;
 
// Initialize the RDS Signer
const signer = new Signer({
  // Use the Vercel AWS SDK credentials provider
  credentials: awsCredentialsProvider({
    roleArn: AWS_ROLE_ARN,
  }),
  region: AWS_REGION,
  port: RDS_PORT,
  hostname: RDS_HOSTNAME,
  username: RDS_USERNAME,
});
 
// Initialize the Postgres Pool
const pool = new Pool({
  password: signer.getAuthToken,
  user: RDS_USERNAME,
  host: RDS_HOSTNAME,
  database: RDS_DATABASE,
  port: RDS_PORT,
});
 
// Export the route handler
export async function GET() {
  try {
    const client = await pool.connect();
    const { rows } = await client.query('SELECT * FROM my_table');
    return Response.json(rows);
  } finally {
    client.release();
  }
}
```

--------------------------------------------------------------------------------
title: "Connect to Microsoft Azure"
description: "Learn how to configure your Microsoft Azure account to trust Vercel's OpenID Connect (OIDC) Identity Provider (IdP)."
last_updated: "null"
source: "https://vercel.com/docs/oidc/azure"
--------------------------------------------------------------------------------

# Connect to Microsoft Azure

Copy page

Ask AI about this page

Last updated October 27, 2025

Secure backend access with OIDC federation is available on [all plans](/docs/plans)

To understand how Azure supports OIDC through Workload Identity Federation, consult the [Azure documentation](https://learn.microsoft.com/en-us/entra/workload-id/workload-identity-federation).

## [Configure your Azure account](#configure-your-azure-account)

1.  ### [Create a Managed Identity](#create-a-managed-identity)
    
    *   Navigate to All services
    *   Select Identity
    *   Select Manage Identities and select Create
    *   Choose your Azure Subscription, Resource Group, Region and Name
2.  ### [Create a Federated Credential](#create-a-federated-credential)
    
    *   Go to Federated credentials and select Add Credential
    *   In the Federated credential scenario field select Other
    *   Enter the Issuer URL, the URL will depend on the issuer mode setting:
        *   Team: `https://oidc.vercel.com/[TEAM_SLUG]`, replacing `[TEAM_SLUG]` with the path from your Vercel team URL
        *   Global: `https://oidc.vercel.com`
    *   In the Subject identifier field use: `owner:[TEAM_SLUG]:project[PROJECT_NAME]:environment:[preview | production | development]`
        *   Replace `[TEAM_SLUG]` with your team identifier from the Vercel's team URL
        *   Replace `[PROJECT_NAME]` with your [project's name](https://vercel.com/docs/projects/overview#project-name) in your [project's settings](https://vercel.com/docs/projects/overview#project-settings)
    *   In the Name field, use a name for your own reference such as: `[Project name] - [Environment]`
    *   In the Audience field use: `https://vercel.com/[TEAM_SLUG]`
        *   Replace `[TEAM_SLUG]` with your team identifier from the Vercel's team URL
    
    Azure does not allow for partial claim conditions so you must specify the `Subject` and `Audience` fields exactly. However, it is possible to create mutliple federated credentials on the same managed identity to allow for the various `sub` claims.
    
3.  ### [Grant access to the Azure service](#grant-access-to-the-azure-service)
    
    In order to connect to the Azure service that you would like to use, you need to allow your Managed Identity to access it.
    
    For example, to use Azure CosmosDB, associate a role definition to the Managed Identity using the Azure CLI, as explained in the [Azure CosmosDB documentation](https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/tutorial-vm-managed-identities-cosmos?tabs=azure-cli#grant-access).
    
    You are now ready to connect to your Azure service from your project's code. Review the example below.
    

## [Example](#example)

In the following example, you create a [Vercel function](/docs/functions/quickstart#create-a-vercel-function) in a Vercel project where you have [defined Azure account environment variables](/docs/environment-variables#creating-environment-variables). The function will connect to Azure using OIDC and use a specific resource that you have allowed the Managed Identity to access.

### [Query an Azure CosmosDB instance](#query-an-azure-cosmosdb-instance)

Install the following packages:

pnpmyarnnpmbun

```
pnpm i @azure/identity @azure/cosmos @vercel/functions
```

In the API route for this function, use the following code to perform a database `SELECT` query from an Azure CosmosDB instance:

/api/azure-cosmosdb/route.ts

```
import {
  ClientAssertionCredential,
  AuthenticationRequiredError,
} from '@azure/identity';
import * as cosmos from '@azure/cosmos';
import { getVercelOidcToken } from '@vercel/oidc';
 
/**
 * The Azure Active Directory tenant (directory) ID.
 * Added to environment variables
 */
const AZURE_TENANT_ID = process.env.AZURE_TENANT_ID!;
 
/**
 * The client (application) ID of an App Registration in the tenant.
 * Added to environment variables
 */
const AZURE_CLIENT_ID = process.env.AZURE_CLIENT_ID!;
const COSMOS_DB_ENDPOINT = process.env.COSMOS_DB_ENDPOINT!;
const COSMOS_DB_ID = process.env.COSMOS_DB_ID!;
const COSMOS_DB_CONTAINER_ID = process.env.COSMOS_DB_CONTAINER_ID!;
 
const tokenCredentials = new ClientAssertionCredential(
  AZURE_TENANT_ID,
  AZURE_CLIENT_ID,
  getVercelOidcToken,
);
 
const cosmosClient = new cosmos.CosmosClient({
  endpoint: COSMOS_DB_ENDPOINT,
  aadCredentials: tokenCredentials,
});
 
const container = cosmosClient
  .database(COSMOS_DB_ID)
  .container(COSMOS_DB_CONTAINER_ID);
 
export async function GET() {
  const { resources } = await container.items
    .query('SELECT * FROM my_table')
    .fetchAll();
 
  return Response.json(resources);
}
```

--------------------------------------------------------------------------------
title: "Connect to Google Cloud Platform (GCP)"
description: "Learn how to configure your GCP project to trust Vercel's OpenID Connect (OIDC) Identity Provider (IdP)."
last_updated: "null"
source: "https://vercel.com/docs/oidc/gcp"
--------------------------------------------------------------------------------

# Connect to Google Cloud Platform (GCP)

Copy page

Ask AI about this page

Last updated October 27, 2025

Secure backend access with OIDC federation is available on [all plans](/docs/plans)

To understand how GCP supports OIDC through Workload Identity Federation, consult the [GCP documentation](https://cloud.google.com/iam/docs/workload-identity-federation).

## [Configure your GCP project](#configure-your-gcp-project)

1.  ### [Configure a Workload Identity Federation](#configure-a-workload-identity-federation)
    
    1.  Navigate to the [Google Cloud Console](https://console.cloud.google.com/)
    2.  Navigate to IAM & Admin then Workload Identity Federation
    3.  Click on Create Pool
2.  ### [Create an identity pool](#create-an-identity-pool)
    
    1.  Enter a name for the pool, e.g. `Vercel`
    2.  Enter an ID for the pool, e.g. `vercel` and click Continue
    
    ![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Foidc-tokens%2Fgcp-create-id-pool.png&w=1080&q=75)![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Foidc-tokens%2Fgcp-create-id-pool.png&w=1080&q=75)
    
3.  ### [Add a provider to the identity pool](#add-a-provider-to-the-identity-pool)
    
    1.  Select `OpenID Connect (OIDC)` from the provider types
    2.  Enter a name for the provider, e.g. `Vercel`
    3.  Enter an ID for the provider, e.g. `vercel`
    4.  Enter the Issuer URL, the URL will depend on the issuer mode setting:
        *   Team: `https://oidc.vercel.com/[TEAM_SLUG]`, replacing `[TEAM_SLUG]` with the path from your Vercel team URL
        *   Global: `https://oidc.vercel.com`
    5.  Leave JWK file (JSON) empty
    6.  Select `Allowed audiences` from "Audience"
    7.  Enter `https://vercel.com/[TEAM_SLUG]` in the "Audience 1" field and click "Continue"
    
    ![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Foidc-tokens%2Fgcp-create-id-pool-2.png&w=1080&q=75)![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Foidc-tokens%2Fgcp-create-id-pool-2.png&w=1080&q=75)
    
4.  ### [Configure the provider attributes](#configure-the-provider-attributes)
    
    1.  Assign the `google.subject` mapping to `assertion.sub`
    2.  Click Save
    
    ![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Foidc-tokens%2Fgcp-create-id-pool-3.png&w=1080&q=75)![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Foidc-tokens%2Fgcp-create-id-pool-3.png&w=1080&q=75)
    
5.  ### [Create a service account](#create-a-service-account)
    
    1.  Copy the IAM Principal from the pool details page from the previous step. It should look like `principal://iam.googleapis.com/projects/012345678901/locations/global/workloadIdentityPools/vercel/subject/SUBJECT_ATTRIBUTE_VALUE`
    2.  Navigate to IAM & Admin then Service Accounts
    3.  Click on Create Service Account
    
    ![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Foidc-tokens%2Fgcp-copy-pool-id.png&w=1080&q=75)![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Foidc-tokens%2Fgcp-copy-pool-id.png&w=1080&q=75)
    
6.  ### [Enter the service account details](#enter-the-service-account-details)
    
    1.  Enter a name for the service account, e.g. `Vercel`.
    2.  Enter an ID for the service account, e.g. `vercel` and click Create and continue.
    
    ![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Foidc-tokens%2Fgcp-create-service-account-1.png&w=1080&q=75)![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Foidc-tokens%2Fgcp-create-service-account-1.png&w=1080&q=75)
    
7.  ### [Grant the service account access to the project](#grant-the-service-account-access-to-the-project)
    
    1.  Select a role or roles for the service account, e.g. `Storage Object Admin`.
    2.  Click Continue.
    
    ![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Foidc-tokens%2Fgcp-create-service-account-2.png&w=1080&q=75)![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Foidc-tokens%2Fgcp-create-service-account-2.png&w=1080&q=75)
    
8.  ### [Grant users access to the service account](#grant-users-access-to-the-service-account)
    
    1.  Paste in the IAM Principal copied from the pool details page in the Service account users role field.
        *   Replace `SUBJECT_ATTRIBUTE_VALUE` with `owner:[VERCEL_TEAM]:project:[PROJECT_NAME]:environment:[ENVIRONMENT]`. e.g. `principal://iam.googleapis.com/projects/012345678901/locations/global/workloadIdentityPools/vercel/subject/owner:acme:project:my-project:environment:production`.
        *   You can add multiple principals to this field, add a principal for each project and environment you want to grant access to.
    2.  Click Done.
    
    ![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Foidc-tokens%2Fgcp-create-service-account-3.png&w=1080&q=75)![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Foidc-tokens%2Fgcp-create-service-account-3.png&w=1080&q=75)
    
9.  ### [Define GCP account values as environment variables](#define-gcp-account-values-as-environment-variables)
    
    Once you have configured your GCP project with OIDC access, gather the following values from the Google Cloud Console:
    
    | Value | Location | Environment Variable | Example |
    | --- | --- | --- | --- |
    | Project ID | IAM & Admin -> Settings | `GCP_PROJECT_ID` | `my-project-123456` |
    | Project Number | IAM & Admin -> Settings | `GCP_PROJECT_NUMBER` | `1234567890` |
    | Service Account Email | IAM & Admin -> Service Accounts | `GCP_SERVICE_ACCOUNT_EMAIL` | `vercel@my-project-123456.iam.gserviceaccount.com` |
    | Workload Identity Pool ID | IAM & Admin -> Workload Identity Federation -> Pools | `GCP_WORKLOAD_IDENTITY_POOL_ID` | `vercel` |
    | Workload Identity Pool Provider ID | IAM & Admin -> Workload Identity Federation -> Pools -> Providers | `GCP_WORKLOAD_IDENTITY_POOL_PROVIDER_ID` | `vercel` |
    
    Then, [declare them as environment variables](/docs/environment-variables#creating-environment-variables) in your Vercel project.
    
    You are now ready to connect to your GCP resource from your project's code. Review the example below.
    

## [Example](#example)

In the following example, you create a [Vercel function](/docs/functions/quickstart#create-a-vercel-function) in the Vercel project where you have defined the GCP account environment variables. The function will connect to GCP using OIDC and use a specific resource provided by Google Cloud services.

### [Return GCP Vertex AI generated text](#return-gcp-vertex-ai-generated-text)

Install the following packages:

pnpmyarnnpmbun

```
pnpm i google-auth-library @ai-sdk/google-vertex ai @vercel/functions
```

In the API route for this function, use the following code to perform the following tasks:

*   Use `google-auth-library` to create an External Account Client
*   Use it to authenticate with Google Cloud Services
*   Use Vertex AI with [Google Vertex Provider](https://sdk.vercel.ai/providers/ai-sdk-providers/google-vertex) to generate text from a prompt

/api/gcp-vertex-ai/route.ts

```
import { getVercelOidcToken } from '@vercel/oidc';
import { ExternalAccountClient } from 'google-auth-library';
import { createVertex } from '@ai-sdk/google-vertex';
import { generateText } from 'ai';
 
const GCP_PROJECT_ID = process.env.GCP_PROJECT_ID;
const GCP_PROJECT_NUMBER = process.env.GCP_PROJECT_NUMBER;
const GCP_SERVICE_ACCOUNT_EMAIL = process.env.GCP_SERVICE_ACCOUNT_EMAIL;
const GCP_WORKLOAD_IDENTITY_POOL_ID = process.env.GCP_WORKLOAD_IDENTITY_POOL_ID;
const GCP_WORKLOAD_IDENTITY_POOL_PROVIDER_ID =
  process.env.GCP_WORKLOAD_IDENTITY_POOL_PROVIDER_ID;
 
// Initialize the External Account Client
const authClient = ExternalAccountClient.fromJSON({
  type: 'external_account',
  audience: `//iam.googleapis.com/projects/${GCP_PROJECT_NUMBER}/locations/global/workloadIdentityPools/${GCP_WORKLOAD_IDENTITY_POOL_ID}/providers/${GCP_WORKLOAD_IDENTITY_POOL_PROVIDER_ID}`,
  subject_token_type: 'urn:ietf:params:oauth:token-type:jwt',
  token_url: 'https://sts.googleapis.com/v1/token',
  service_account_impersonation_url: `https://iamcredentials.googleapis.com/v1/projects/-/serviceAccounts/${GCP_SERVICE_ACCOUNT_EMAIL}:generateAccessToken`,
  subject_token_supplier: {
    // Use the Vercel OIDC token as the subject token
    getSubjectToken: getVercelOidcToken,
  },
});
 
const vertex = createVertex({
  project: GCP_PROJECT_ID,
  location: 'us-central1',
  googleAuthOptions: {
    authClient,
    projectId: GCP_PROJECT_ID,
  },
});
 
// Export the route handler
export const GET = async (req: Request) => {
  const result = generateText({
    model: vertex('gemini-1.5-flash'),
    prompt: 'Write a vegetarian lasagna recipe for 4 people.',
  });
  return Response.json(result);
};
```

--------------------------------------------------------------------------------
title: "OIDC Federation Reference"
description: "Review helper libraries to help you connect with your backend and understand the structure of an OIDC token."
last_updated: "null"
source: "https://vercel.com/docs/oidc/reference"
--------------------------------------------------------------------------------

# OIDC Federation Reference

Copy page

Ask AI about this page

Last updated October 27, 2025

Secure backend access with OIDC federation is available on [all plans](/docs/plans)

## [Helper libraries](#helper-libraries)

Vercel provides helper libraries to make it easier to exchange the OIDC token for short-lived credentials with your cloud provider. They are available from the [@vercel/oidc](https://www.npmjs.com/package/@vercel/oidc) and [@vercel/oidc-aws-credentials-provider](https://www.npmjs.com/package/@vercel/oidc-aws-credentials-provider) packages on npm.

### [AWS SDK credentials provider](#aws-sdk-credentials-provider)

`awsCredentialsProvider()` is a helper function that returns a function that can be used as the `credentials` property of the AWS SDK client. It exchanges the OIDC token for short-lived credentials with AWS by calling the `AssumeRoleWithWebIdentity` operation.

#### [AWS S3 usage example](#aws-s3-usage-example)

```
import { awsCredentialsProvider } from '@vercel/oidc-aws-credentials-provider';
import * as s3 from '@aws-sdk/client-s3';
 
const s3client = new s3.S3Client({
  region: process.env.AWS_REGION!,
  credentials: awsCredentialsProvider({
    roleArn: process.env.AWS_ROLE_ARN!,
  }),
});
```

### [Other cloud providers](#other-cloud-providers)

`getVercelOidcToken()` returns the OIDC token from the `VERCEL_OIDC_TOKEN` environment variable in builds and local development environments or the `x-vercel-oidc-token` in Vercel functions.

#### [Azure / CosmosDB example](#azure-/-cosmosdb-example)

```
import { getVercelOidcToken } from '@vercel/oidc';
import { ClientAssertionCredential } from '@azure/identity';
import { CosmosClient } from '@azure/cosmos';
 
const credentialsProvider = new ClientAssertionCredential(
  process.env.AZURE_TENANT_ID,
  process.env.AZURE_CLIENT_ID,
  getVercelOidcToken,
);
 
const cosmosClient = new CosmosClient({
  endpoint: process.env.COSMOS_DB_ENDPOINT,
  aadCredentials: credentialsProvider,
});
```

In the Vercel function environments, you cannot execute the `getVercelOidcToken()` function directly at the module level because the token is only available in the `Request` object as the `x-vercel-oidc-token` header.

## [Team and project name changes](#team-and-project-name-changes)

If you change the name of your team or project, the claims within the OIDC token will reflect the new names. This can affect your trust and access control policies. You should consider this when you plan to rename your team or project and update your policies accordingly.

AWS roles can support multiple conditions so you can allow access to both the old and new team and project names. The following example shows when the issuer mode is set to global:

aws-trust-policy.json

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Federated": "arn:aws:iam::[YOUR AWS ACCOUNT ID]:oidc-provider/oidc.vercel.com"
      },
      "Action": "sts:AssumeRoleWithWebIdentity",
      "Condition": {
        "StringEquals": {
          "oidc.vercel.com:aud": [
            "https://vercel.com/[OLD_TEAM_SLUG]",
            "https://vercel.com/[NEW_TEAM_SLUG]"
          ],
          "oidc.vercel.com:sub": [
            "owner:[OLD_TEAM_SLUG]:project:[OLD_PROJECT_NAME]:environment:production",
            "owner:[NEW_TEAM_SLUG]:project:[NEW_PROJECT_NAME]:environment:production"
          ]
        }
      }
    }
  ]
}
```

If your project is using the `team` issuer mode, you will need to create a new OIDC provider and add another statement to the trust policy:

aws-trust-policy.json

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "OldTeamName",
      "Effect": "Allow",
      "Principal": {
        "Federated": "arn:aws:iam::[YOUR AWS ACCOUNT ID]:oidc-provider/oidc.vercel.com/[OLD_TEAM_SLUG]"
      },
      "Action": "sts:AssumeRoleWithWebIdentity",
      "Condition": {
        "StringEquals": {
          "oidc.vercel.com/[OLD_TEAM_SLUG]:aud": [
            "https://vercel.com/[OLD_TEAM_SLUG]"
          ],
          "oidc.vercel.com/[OLD_TEAM_SLUG]:sub": [
            "owner:[OLD_TEAM_SLUG]:project:[OLD_PROJECT_NAME]:environment:production"
          ]
        }
      }
    },
    {
      "Sid": "NewTeamName",
      "Effect": "Allow",
      "Principal": {
        "Federated": "arn:aws:iam::[YOUR AWS ACCOUNT ID]:oidc-provider/oidc.vercel.com/[NEW_TEAM_SLUG]"
      },
      "Action": "sts:AssumeRoleWithWebIdentity",
      "Condition": {
        "StringEquals": {
          "oidc.vercel.com/[NEW_TEAM_SLUG]:aud": [
            "https://vercel.com/[NEW_TEAM_SLUG]"
          ],
          "oidc.vercel.com/[NEW_TEAM_SLUG]:sub": [
            "owner:[NEW_TEAM_SLUG]:project:[NEW_PROJECT_NAME]:environment:production"
          ]
        }
      }
    }
  ]
}
```

## [OIDC token anatomy](#oidc-token-anatomy)

You can validate OpenID Connect tokens by using the issuer's OpenID Connect Discovery Well Known location, which is either `https://oidc.vercel.com/.well-known/openid-configuration` or `https://oidc.vercel.com/[TEAM_SLUG]/.well-known/openid-configuration` depending on the issuer mode in your project settings. There, you can find a property called `jwks_uri` which provides a URI to Vercel's public JSON Web Keys (JWKs). You can use the corresponding JWK identified by `kid` to verify tokens that are signed with the same `kid` in the token's header.

### [Example token](#example-token)

```
// Header:
{
  "typ": "JWT",
  "alg": "RS256",
  "kid": "example-key-id"
}
// Claims:
{
  "iss": "https://oidc.vercel.com/acme",
  "aud": "https://vercel.com/acme",
  "sub": "owner:acme:project:acme_website:environment:production",
  "iat": 1718885593,
  "nfb": 1718885593,
  "exp": 1718889193,
  "owner": "acme",
  "owner_id": "team_7Gw5ZMzpQA8h90F832KGp7nwbuh3",
  "project": "acme_website",
  "project_id": "prj_7Gw5ZMBpQA8h9GF832KGp7nwbuh3",
  "environment": "production"
}
```

### [Standard OpenID Connect claims](#standard-openid-connect-claims)

This is a list of standard tokens that you can expect from an OpenID Connect JWT:

| Claim | Kind | Description |
| --- | --- | --- |
| `iss` | Issuer | When using the team issuer mode, the issuer is set to `https://oidc.vercel.com/[TEAM_SLUG]`  
When using the global issuer mode, the issuer is set to `https://oidc.vercel.com` |
| `aud` | Audience | The audience is set to `https://vercel.com/[TEAM_SLUG]` |
| `sub` | Subject | The subject is set to `owner:[TEAM_SLUG]:project:[PROJECT_NAME]:environment:[ENVIRONMENT]` |
| `iat` | Issued at | The time the token was created |
| `nbf` | Not before | The token is not valid before this time |
| `exp` | Expires at | The time the token has or will expire. `preview` and `production` tokens expire one hour after creation, `development` tokens expire in 12 hours. |

### [Additional claims](#additional-claims)

These claims provide more granular access control:

| Claim | Description |
| --- | --- |
| `owner` | The team slug, e.g. `acme` |
| `owner_id` | The team ID, e.g. `team_7Gw5ZMzpQA8h90F832KGp7nwbuh3` |
| `project` | The project name, e.g. `acme_website` |
| `project_id` | The project ID, e.g. `prj_7Gw5ZMBpQA8h9GF832KGp7nwbuh3` |
| `environment` | The environment: `development` or `preview` or `production` |
| `user_id` | When environment is `development`, this is the ID of the user who was issued the token |

### [JWT headers](#jwt-headers)

These headers are standard to the JWT tokens:

| Header | Kind | Description |
| --- | --- | --- |
| `alg` | Algorithm | The algorithm used by the issuer |
| `kid` | Key ID | The identifier of the key used to sign the token |
| `typ` | Type | The type of token, this is set to `jwt`. |

--------------------------------------------------------------------------------
title: "Quickstart for using OpenTelemetry with Vercel Functions"
description: "Learn how to get started with OTel on Vercel to send traces from your functions to application performance monitoring (APM) vendors."
last_updated: "null"
source: "https://vercel.com/docs/otel"
--------------------------------------------------------------------------------

# Quickstart for using OpenTelemetry with Vercel Functions

Copy page

Ask AI about this page

Last updated October 31, 2025

Drains are available on [Enterprise](/docs/plans/enterprise) and [Pro](/docs/plans/pro) plans

Vercel supports [OpenTelemetry](https://opentelemetry.io/) traces. OpenTelemetry is an open standard for collecting traces from your application.

With OpenTelemetry on Vercel, you can:

*   Export traces to your preferred observability provider using [Vercel Drains](/docs/drains).
*   Automatically instrument Vercel infrastructure and fetch requests from Vercel Functions.
*   Collect traces and spans you create with the OpenTelemetry SDK.
*   Store traces on Vercel that are created with [Session Tracing](/docs/session-tracing).

### [Get started with Vercel Trace Drains](#get-started-with-vercel-trace-drains)

1.  ### [Initialize OTel](#initialize-otel)
    
    Using `@vercel/otel` wrapperUsing OpenTelemetry SDK
    
    For JavaScript and Typescript users on Vercel, you can use the `@vercel/otel` package to call the correct OpenTelemetry SDK for you.
    
    Install the OpenTelemetry JavaScript SDK and `@vercel/otel`:
    
    pnpmyarnnpmbun
    
    ```
    pnpm i @opentelemetry/api @vercel/otel
    ```
    
    Create an `instrumentation.ts` file in the root of your project, or, on Next.js [it must be placed](https://nextjs.org/docs/pages/building-your-application/optimizing/open-telemetry#using-vercelotel) in the `src` directory if you are using one. Add the following code to initialize and configure OTel using `@vercel/otel`.
    
    Next.js (/app)Next.js (/pages)Other frameworks
    
    instrumentation.ts
    
    TypeScript
    
    TypeScriptJavaScript
    
    ```
    import { registerOTel } from '@vercel/otel';
     
    export function register() {
      registerOTel({ serviceName: 'your-project-name' });
    }
    // NOTE: You can replace `your-project-name` with the actual name of your project
    ```
    
    Before receiving traces from an APM vendor (such as DataDog), it may be necessary to first create the service you intend to use as a `serviceName` within the service catalog. Refer to the APM vendor's documentation for specific requirements.
    
    You can use standard OpenTelemetry SDK to send traces to our collector. List of all supported languages by OpenTelemetry and their SDK can be found in [OpenTelemetry docs](https://opentelemetry.io/docs/instrumentation).
    
    Begin by installing the following packages:
    
    pnpmyarnnpmbun
    
    ```
    pnpm i @opentelemetry/api @opentelemetry/sdk-node @opentelemetry/resources @opentelemetry/semantic-conventions @opentelemetry/sdk-trace-base @opentelemetry/exporter-trace-otlp-http @opentelemetry/sdk-trace-node
    ```
    
    Next, create an `instrumentation.ts` file in the root of your project and add the following code to initialize and configure OTel.
    
    Next.js (/app)Next.js (/pages)Other frameworks
    
    instrumentation.ts
    
    TypeScript
    
    TypeScriptJavaScript
    
    ```
    import { NodeSDK } from '@opentelemetry/sdk-node';
    import { OTLPTraceExporter } from '@opentelemetry/exporter-trace-otlp-http';
    import { Resource } from '@opentelemetry/resources';
    import { SemanticResourceAttributes } from '@opentelemetry/semantic-conventions';
    import { SimpleSpanProcessor } from '@opentelemetry/sdk-trace-node';
     
    export async function register() {
      const sdk = new NodeSDK({
        resource: new Resource({
          [SemanticResourceAttributes.SERVICE_NAME]: 'your-project-name',
          // NOTE: You can replace `your-project-name` with the actual name of your project
        }),
        spanProcessor: new SimpleSpanProcessor(new OTLPTraceExporter()),
      });
     
      await sdk.start();
    }
    ```
    
    The provided service name will be used in your OpenTelemetry backend to distinguish traces from different services. You need to specify what you want to do with generated spans, there are two types of span processors:
    
    *   `SimpleSpanProcessor`: sends each span to the collector right away. This type is shown in code above
    *   `BatchSpanProcessor`: collects a number of spans and sends them together to the collector. If you choose this type, you'll need to call `processor.forceFlush()` at the end of the invocation to immediately export all spans
    
    A span processor needs to know what to do with processed traces. In order to export traces to Vercel OpenTelemetry collector, you need to use one of these exporters:
    
    *   `@opentelemetry/exporter-trace-otlp-http`
    *   `@opentelemetry/exporter-trace-otlp-grpc`
    
2.  ### [Start tracing requests in your project](#start-tracing-requests-in-your-project)
    
    Next.js 13.4+Other frameworks
    
    Next.js 13.4+ supports auto-instrumentation which means you no longer have to create a span for each request. To use this feature in Next.js 13 & 14, you must explicitly opt-in by adding `experimental.instrumentationHook = true` to your `next.config.js`. This is not required in Next.js 15+.
    
    For more information, please refer to the [Next.js docs for auto-instrumentation](https://nextjs.org/docs/app/guides/open-telemetry#default-spans-in-nextjs).
    
    For non-Next.js frameworks or Next.js version older than `13.4`, you will need to manually create spans for each request.
    
    ```
    import { trace, context, propagation, SpanStatusCode } from '@opentelemetry/api';
     
    export default async function getUser(request, response) {
      const incomingContext = propagation.extract(context.active(), request.headers);
      const tracer = trace.getTracer('your-project-name');
      return tracer.startActiveSpan('get-user', async (span) => {
        try {
          const result = someFnThatMightThrowError(span);
          span.end();
          return result;
        } catch (e) {
          span.recordException(e);
          span.setStatus({ code: SpanStatusCode.ERROR, message: e.message });
          throw e;
        }
      }, incomingContext);
    }
    ```
    
    In the code above we are importing the OTel tracer to the `pages/api/get-user.ts` file to create spans for tracking performance. You'll need to include this import to any file that uses the tracer.
    

### [Using custom OpenTelemetry setup with Sentry](#using-custom-opentelemetry-setup-with-sentry)

If you are using Sentry v8+, follow the [Sentry documentation](https://docs.sentry.io/platforms/javascript/guides/nextjs/opentelemetry/custom-setup/) to learn how to use your existing custom OpenTelemetry setup.

Using Vercel OTel instead of Sentry: If you prefer to use Vercel's OpenTelemetry setup instead of Sentry's OTel instrumentation, add `skipOpenTelemetrySetup: true` to your Sentry initialization in your `instrumentation.ts` file. This resolves conflicts between Vercel's OTel and Sentry v8+ that can prevent traces from reaching downstream providers.

--------------------------------------------------------------------------------
title: "Package Managers"
description: "Discover the package managers supported by Vercel for dependency management. Learn how Vercel detects and uses npm, Yarn, pnpm, and Bun for optimal build performance."
last_updated: "null"
source: "https://vercel.com/docs/package-managers"
--------------------------------------------------------------------------------

# Package Managers

Copy page

Ask AI about this page

Last updated September 24, 2025

Vercel will automatically detect the package manager used in your project and install the dependencies when you [create a deployment](/docs/deployments/builds#build-process). It does this by looking at the lock file in your project and inferring the correct package manager to use.

If you are using [Corepack](/docs/deployments/configure-a-build#corepack), Vercel will use the package manager specified in the `package.json` file's `packageManager` field instead.

## [Supported package managers](#supported-package-managers)

The following table lists the package managers supported by Vercel, with their install commands and versions:

| Package Manager | Lock File | Install Command | Supported Versions |
| --- | --- | --- | --- |
| Yarn | [`yarn.lock`](https://classic.yarnpkg.com/lang/en/docs/yarn-lock/) | [`yarn install`](https://classic.yarnpkg.com/lang/en/docs/cli/install/) | 1, 2, 3 |
| npm | [`package-lock.json`](https://docs.npmjs.com/cli/v10/configuring-npm/package-lock-json) | [`npm install`](https://docs.npmjs.com/cli/v8/commands/npm-install) | 8, 9, 10 |
| pnpm | [`pnpm-lock.yaml`](https://pnpm.io/git) | [`pnpm install`](https://pnpm.io/cli/install) | 6, 7, 8, 9, 10 |
| Bun 1 | [`bun.lockb`](https://bun.sh/docs/install/lockfile) or [`bun.lock`](https://bun.sh/docs/install/lockfile#text-based-lockfile) | [`bun install`](https://bun.sh/docs/cli/install) | 1 |
| Vlt
Beta

 | `vlt-lock.json` | [`vlt install`](https://docs.vlt.sh/) | 0.x |

While Vercel automatically selects the package manager based on the lock file present in your project, the specific version of that package manager is determined by the version information in the lock file or associated configuration files.

The npm and pnpm package managers create a `lockfileVersion` property when they generate a lock file. This property specifies the lock file's format version, ensuring proper processing and compatibility. For example, a `pnpm-lock.yaml` file with `lockfileVersion: 9.0` will be interpreted by pnpm 9, while a `pnpm-lock.yaml` file with `lockfileVersion: 5.4` will be interpreted by pnpm 7.

| Package Manager | Condition | Install Command | Version Used |
| --- | --- | --- | --- |
| pnpm | `pnpm-lock.yaml`: present | `pnpm install` | Varies |
|  | `lockfileVersion`: 9.0 | \- | pnpm 9 or 10\* |
|  | `lockfileVersion`: 7.0 | \- | pnpm 9 |
|  | `lockfileVersion`: 6.0/6.1 | \- | pnpm 8 |
|  | `lockfileVersion`: 5.3/5.4 | \- | pnpm 7 |
|  | Otherwise | \- | pnpm 6 |
| npm | `package-lock.json`: present | `npm install` | Varies |
|  | `lockfileVersion`: 2 | \- | npm 8 |
|  | Node 20 | \- | npm 10 |
|  | Node 22 | \- | npm 10 |
| Bun | `bun.lockb`: present | `bun install` | Bun <1.2 |
|  | `bun.lock`: present | `bun install --save-text-lockfile` | Bun 1 |
|  | `bun.lock`: present | `bun install` | Bun >=1.2 |
| Yarn | `yarn.lock`: present | `yarn install` | Yarn 1 |
| Vlt | `vlt-lock.json`: present | `vlt install` | Vlt 0.x |

`pnpm-lock.yaml` version 9.0 can be generated by pnpm 9 or 10. Newer projects will prefer 10, while older prefer 9. Check [build logs](/docs/deployments/logs) to see which version is used for your project.

When no lock file exists, Vercel uses npm by default. Npm's default version aligns with the Node.js version as described in the table above. Defaults can be overridden using [`installCommand`](/docs/project-configuration#installcommand) or [Corepack](/docs/deployments/configure-a-build#corepack) for specific package manager versions.

## [Manually specifying a package manager](#manually-specifying-a-package-manager)

You can manually specify a package manager to use on a per-project, or per-deployment basis.

### [Project override](#project-override)

To specify a package manager for all deployments in your project, use the Override setting in your project's [Build & Development Settings](/docs/deployments/configure-a-build#build-and-development-settings):

1.  Navigate to your [dashboard](/dashboard) and select your project
2.  Select the Settings tab
3.  From the left navigation, select General
4.  Enable the Override toggle in the [Build & Development Settings](/docs/deployments/configure-a-build#build-and-development-settings) section and add your install command. Once you save, it will be applied on your next deployment

When using an override install command like `pnpm install`, Vercel will use the oldest version of the specified package manager available in the build container. For example, if you specify `pnpm install` as your override install command, Vercel will use pnpm 6.

### [Deployment override](#deployment-override)

To specify a package manager for a deployment, use the [`installCommand`](/docs/project-configuration#installcommand) property in your projects `vercel.json`.

vercel.json

```
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "installCommand": "pnpm install"
}
```

--------------------------------------------------------------------------------
title: "Account Plans on Vercel"
description: "Learn about the different plans available on Vercel."
last_updated: "null"
source: "https://vercel.com/docs/plans"
--------------------------------------------------------------------------------

# Account Plans on Vercel

Copy page

Ask AI about this page

Last updated September 9, 2025

Vercel offers multiple account plans: Hobby, Pro, Pro (legacy), and Enterprise.

Each plan is designed to meet the needs of different types of users, from personal projects to large enterprises. The Hobby plan is free and includes base features, while Pro and Enterprise plans offer enhanced features, team collaboration, and flexible resource management.

## [Hobby](#hobby)

The Hobby plan is designed for personal projects and developers. It includes CLI and personal [Git integrations](/docs/git), built-in CI/CD, [automatic HTTPS/SSL](/docs/security/encryption), and [previews deployments](/docs/deployments/environments#preview-environment-pre-production) for every Git push.

It also provides base resources for [Vercel Functions](/docs/functions), [Middleware](/docs/routing-middleware), and [Image Optimization](/docs/image-optimization), along with 100 GB of Fast Data Transfer and 1 hour of [runtime logs](/docs/runtime-logs).

See the [Hobby plan](/docs/plans/hobby) page for more details.

## [Pro](#pro)

The Pro plan is designed for professional developers, freelancers, and businesses who need enhanced features and team collaboration. It includes all features of the [Hobby plan](/docs/plans/hobby) with significant improvements in resource management and team capabilities.

Pro introduces a flexible credit-based system that provides transparent, usage-based billing. You get enhanced team collaboration with viewer roles, advanced analytics, and the option to add enterprise features through add-ons.

Key features include team roles and permissions, credit-based resource management, enhanced monitoring, and email support with optional priority support upgrades.

See the [Pro plan](/docs/plans/pro-plan) page for more details.

## [Pro (Legacy)](#pro-legacy)

The legacy Pro plan is available for existing customers and offers fixed resource limits with traditional billing. It includes team collaboration features, email support, and increased limits compared to Hobby.

New customers are encouraged to choose the new Pro plan for better flexibility and enhanced features. Existing legacy Pro customers can switch to the new Pro plan at any time to take advantage of credit-based billing and new collaboration features.

See the [legacy Pro plan](/docs/plans/pro) page for more details or learn about [switching to the new Pro plan](/docs/plans/pro-plan/switching).

## [Enterprise](#enterprise)

The Enterprise plan caters to large organizations and enterprises requiring custom options, advanced security, and dedicated support. It includes all features of the Pro plan with custom limits, dedicated infrastructure, and enterprise-grade security features.

Enterprise customers benefit from [Single Sign-On (SSO)](/docs/saml), enhanced [observability and logging](/docs/observability), isolated build infrastructure, dedicated customer success managers, and SLAs.

See the [Enterprise plan](/docs/plans/enterprise) page for more details.

## [General billing information](#general-billing-information)

### [Where do I understand my usage?](#where-do-i-understand-my-usage)

On the [usage page of your dashboard](/dashboard). To learn how your usage relates to your bill and how to optimize your usage, see [Manage and optimize usage](/docs/pricing/manage-and-optimize-usage).

You can also learn more about how [usage incurs on your site](/docs/pricing/how-does-vercel-calculate-usage-of-resources) or how to [understand your invoice](/docs/pricing/understanding-my-invoice).

### [What happens when I reach 100% usage?](#what-happens-when-i-reach-100%-usage)

All plans [receive notifications](/docs/notifications#on-demand-usage-notifications) by email and on the dashboard when they are approaching and exceed their usage limits.

*   Hobby plans will be paused when they exceed the included free tier usage
*   Pro and legacy Pro plans users can configure [Spend Management](/docs/spend-management) to automatically pause deployments, trigger a webhook, or send SMS notifications when they reach 100% usage

For Pro, legacy Pro, and Enterprise teams, when you reach 100% usage your deployments are not automatically stopped. Rather, Vercel enables you to incur on-demand usage as your site grows. It's important to be aware of the [usage page of your dashboard](/docs/limits/usage) to see if you are approaching your limit.

One of the benefits to always being on, is that you don't have to worry about downtime in the event of a huge traffic spike caused by announcements or other events. Keeping your site live during these times can be critical to your business.

See [Manage & optimize usage](/docs/pricing/manage-and-optimize-usage) for more information on how to optimize your usage.

--------------------------------------------------------------------------------
title: "Vercel Enterprise Plan"
description: "Learn about the Enterprise plan for Vercel, including features, pricing, and more."
last_updated: "null"
source: "https://vercel.com/docs/plans/enterprise"
--------------------------------------------------------------------------------

# Vercel Enterprise Plan

Copy page

Ask AI about this page

Last updated September 24, 2025

Vercel offers an Enterprise plan for organizations and enterprises that need high [performance](#performance-and-reliability), advanced [security](#security-and-compliance), and dedicated [support](#administration-and-support).

## [Performance and reliability](#performance-and-reliability)

The Enterprise plan uses isolated build infrastructure on high-grade hardware with no queues to ensure exceptional performance and a seamless experience.

*   Greater function limits for [Vercel Functions](/docs/functions/runtimes) including bundle size, duration, memory, and concurrency
*   Automatic failover regions for [Vercel Functions](/docs/functions/configuring-functions/region#automatic-failover)
*   Greater multi-region limits for [Vercel Functions](/docs/functions/configuring-functions/region#project-configuration)
*   Vercel functions memory [configurable](/docs/functions/runtimes#size-limits) to 3009 MB
*   Configurable [Vercel Function](/docs/functions) up to a [maximum duration](/docs/functions/runtimes#max-duration) of 900-seconds
*   Unlimited [domains](/docs/domains) per project
*   [Custom SSL Certificates](/docs/domains/custom-SSL-certificate)
*   Automatic concurrency scaling up to 100,000 for [Vercel Functions](/docs/functions/concurrency-scaling#automatic-concurrency-scaling)
*   [Isolated build infrastructure](/docs/security#do-enterprise-accounts-run-on-a-different-infrastructure), with the ability to have [larger memory and storage](/docs/deployments/troubleshoot-a-build#build-container-resources)
*   [Trusted Proxy](/docs/headers/request-headers#x-forwarded-for)

## [Security and compliance](#security-and-compliance)

Data and infrastructure security is paramount in the Enterprise plan with advanced features including:

*   [SSO/SAML Login](/docs/saml)
*   [Compliance measures](/docs/security)
*   Access management for your deployments such as [Password Protection](/docs/security/deployment-protection/methods-to-protect-deployments/password-protection), [Private Production Deployments](/docs/security/deployment-protection#configuring-deployment-protection), and [Trusted IPs](/docs/security/deployment-protection/methods-to-protect-deployments/trusted-ips)
*   [Secure Compute](/docs/secure-compute) (Paid add-on for Enterprise)
*   [Directory Sync](/docs/security/directory-sync)
*   [SIEM Integration](/docs/observability/audit-log#custom-siem-log-streaming) (Paid add-on for Enterprise)
*   [Vercel Firewall](/docs/vercel-firewall), including [dedicated DDoS support](/docs/vercel-firewall/ddos-mitigation#dedicated-ddos-support-for-enterprise-teams), [WAF account-level IP Blocking](/docs/security/vercel-waf/ip-blocking#account-level-ip-blocking) and [WAF Managed Rulesets](/docs/security/vercel-waf/managed-rulesets)

## [Conformance and Code Owners](#conformance-and-code-owners)

[Conformance](/docs/conformance) is a suite of tools designed for static code analysis. Conformance ensures high standards in performance, security, and code health, which are integral for enterprise projects. Code Owners enables you to define users or teams that are responsible for directories and files in your codebase.

*   [Allowlists](/docs/conformance/allowlist)
*   [Curated rules](/docs/conformance/rules)
*   [Custom rules](/docs/conformance/custom-rules)
*   [Code Owners](/docs/code-owners) for GitHub

## [Observability and Reporting](#observability-and-reporting)

Gain actionable insights with enhanced observability & logging.

*   Enhanced [Observability and Logging](/docs/observability)
*   [Audit Logs](/docs/observability/audit-log)
*   Increased retention with [Speed Insights](/docs/speed-insights/limits-and-pricing)
*   [Custom Events](/docs/analytics/custom-events) tracking and more filters, such as UTM Parameters
*   3 days of [Runtime Logs](/docs/runtime-logs) and increased row data
*   Increased retention with [Vercel Monitoring](/docs/observability/monitoring)
*   [OpenTelemetry](/docs/otel/quickstart) support
*   Configurable [log drains](/docs/drains/using-drains)
*   Integrations, like [Datadog](/integrations/datadog), [New Relic](/integrations/newrelic), and [Middleware](/integrations/middleware)

## [Administration and Support](#administration-and-support)

The Enterprise plan allows for streamlined team collaboration and offers robust support with:

*   [Role-Based Access Control (RBAC)](/docs/rbac/access-roles)
*   [Access Groups](/docs/rbac/access-groups)
*   [Vercel Support Center](/docs/dashboard-features/support-center)
*   A dedicated Success Manager
*   [SLAs](https://vercel.com/legal/sla), including [response time](https://vercel.com/legal/support-terms)
*   Audits for Next.js
*   Professional services

--------------------------------------------------------------------------------
title: "Billing FAQ for Enterprise Plan"
description: "This page covers frequently asked questions around payments, invoices, and billing on the Enterprise plan."
last_updated: "null"
source: "https://vercel.com/docs/plans/enterprise/billing"
--------------------------------------------------------------------------------

# Billing FAQ for Enterprise Plan

Copy page

Ask AI about this page

Last updated September 24, 2025

The Vercel Enterprise plan is perfect for [teams](/docs/accounts/create-a-team) with increased performance, collaboration, and security needs. This page covers frequently asked questions around payments, invoices, and billing on the Enterprise plan.

## [Payments](#payments)

### [When are payments taken?](#when-are-payments-taken)

*   Pay by credit card: When the invoice is finalized in Stripe
*   Pay by ACH/Wire: Due by due date on the invoice

### [What payment methods are available?](#what-payment-methods-are-available)

*   Credit card
*   ACH/Wire

### [What currency can I pay in?](#what-currency-can-i-pay-in)

You can pay in any currency so long as the credit card provider allows charging in USD _after_ conversion.

### [Can I delay my payment?](#can-i-delay-my-payment)

Contact your Customer Success Manager (CSM) or Account Executive (AE) if you feel payment might be delayed.

### [Can I pay annually?](#can-i-pay-annually)

Yes.

### [What card types can I pay with?](#what-card-types-can-i-pay-with)

*   American Express
*   China UnionPay (CUP)
*   Discover & Diners
*   Japan Credit Bureau (JCB)
*   Mastercard
*   Visa

#### [If paying by ACH, do I need to cover the payment fee cost on top of the payment?](#if-paying-by-ach-do-i-need-to-cover-the-payment-fee-cost-on-top-of-the-payment)

Yes, when paying with ACH, the payment fee is often deducted by the sender. You need to add this fee to the amount you send, otherwise the payment may be rejected.

### [Can I change my payment method?](#can-i-change-my-payment-method)

Yes. You are free to remove your current payment method, so long as you have ACH payments set up. Once you have ACH payments set up, notify your Customer Success Manager (CSM) or Account Executive (AE). They can verify your account changes.

## [Invoices](#invoices)

### [Can I pay by invoice?](#can-i-pay-by-invoice)

*   Yes. After checking the invoice, you can make a payment. You will receive a receipt after your credit card gets charged
*   If you are paying with ACH, you will receive an email containing the bank account details you can wire the payment to
*   If you are paying with ACH, you should provide the invoice number as a reference on the payment

### [Why am I overdue?](#why-am-i-overdue)

Payment was not received from you by the invoice due date. This could be due to an issue with your credit card, like reaching your payment limit or your card having expired.

### [Can I change an existing invoice detail?](#can-i-change-an-existing-invoice-detail)

No. Unless you provide specific justification to your Customer Success Manager (CSM) or Account Executive (AE). This addition will get added to future invoices, not to the current invoice.

## [Billing](#billing)

### [Is there a Billing role available?](#is-there-a-billing-role-available)

Yes. Learn more about [Roles and Permissions](/docs/accounts/team-members-and-roles).

### [How do I update my billing information?](#how-do-i-update-my-billing-information)

1.  ### [Go to the **Settings** page](#go-to-the-settings-page)
    
    *   Navigate to the [Dashboard](/dashboard)
    *   Select your team from the scope selector on the top left as explained [here](/docs/teams-and-accounts/create-or-join-a-team#creating-a-team)
    *   Select the Settings tab
2.  ### [Go to the Billing section to update the appropriate fields](#go-to-the-billing-section-to-update-the-appropriate-fields)
    
    Select Billing from the sidebar. Scroll down to find the following editable fields. You can update these if you are a [team owner](/docs/rbac/access-roles#owner-role) or have the [billing role](/docs/rbac/access-roles#billing-role):
    
    *   Invoice Email Recipient: A custom destination email for your invoices. By default, they get sent to the first owner of the team
    *   Company Name: The company name that shows up on your invoices. By default, it is set to your team name
    *   Billing Address: A postal address added to every invoice. By default, it is blank
    *   Invoice Language: The language of your invoices which is set to English by default
    *   Invoice Purchase Order: A line that includes a purchase order on your invoices. By default, it is blank
    *   Tax ID: A line for rendering a specific tax ID on your invoices. By default, it is blank
    
    Your changes only affect future invoices, not existing ones.
    

### [What do I do if I think my bill is wrong?](#what-do-i-do-if-i-think-my-bill-is-wrong)

Please [open a support ticket](/help#issues) to log your request, which will allow our support team to look into the case for you.

When you contact support the following information will be needed:

*   Invoice ID
*   The account email
*   The Team name
*   If the query is related to the monthly plan, or usage billing

### [Do I get billed for DDoS?](#do-i-get-billed-for-ddos)

[Vercel automatically mitigates against L3, L4, and L7 DDoS attacks](/docs/security/ddos-mitigation) at the platform level for all plans. Vercel does not charge customers for traffic that gets blocked by the Firewall.

Usage will be incurred for requests that are successfully served prior to us automatically mitigating the event. Usage will also be incurred for requests that are not recognized as a DDoS event, which may include bot and crawler traffic.

For an additional layer of security, we recommend that you enable [Attack Challenge Mode](/docs/attack-challenge-mode) when you are under attack, which is available for free on all plans. While some malicious traffic is automatically challenged, enabling Attack Challenge Mode will challenge all traffic, including legitimate traffic to ensure that only real users can access your site.

You can monitor usage in the [Vercel Dashboard](/dashboard) under the Usage tab, although you will [receive notifications](/docs/notifications#on-demand-usage-notifications) when nearing your usage limits.

### [What is a billing cycle?](#what-is-a-billing-cycle)

The billing cycle refers to the period of time between invoices. The start date depends on when you created the account. You will be billed every 1, 2, 3, 6, or 12 months depending on your contract.

--------------------------------------------------------------------------------
title: "Vercel Hobby Plan"
description: "Learn about the Hobby plan and how it compares to the Pro plan."
last_updated: "null"
source: "https://vercel.com/docs/plans/hobby"
--------------------------------------------------------------------------------

# Vercel Hobby Plan

Copy page

Ask AI about this page

Last updated September 9, 2025

The Hobby plan is free and aimed at developers with personal projects, and small-scale applications. It offers a generous set of features for individual users on a per month basis:

| Resource | Hobby Included Usage |
| --- | --- |
| [Edge Config Reads](/docs/edge-config/using-edge-config#reading-data-from-edge-configs) | First 100,000 |
| [Edge Config Writes](/docs/edge-config/using-edge-config#writing-data-to-edge-configs) | First 100 |
| [Active CPU](/docs/functions/usage-and-pricing) | 4 CPU-hrs |
| [Provisioned Memory](/docs/functions/usage-and-pricing) | 360 GB-hrs |
| [Function Invocations](/docs/functions/usage-and-pricing) | First 1,000,000 |
| [Function Duration](/docs/functions/configuring-functions/duration) | First 100 GB-Hours |
| [Image Optimization Source Images](/docs/image-optimization/legacy-pricing#source-images) | First 1,000 |
| [Speed Insights Data Points](/docs/speed-insights/metrics#understanding-data-points) | First 10,000 |
| [Speed Insights Projects](/docs/speed-insights) | 1 Project |
| [Web Analytics Events](/docs/analytics/limits-and-pricing#what-is-an-event-in-vercel-web-analytics) | First 50,000 Events |

## [Hobby billing cycle](#hobby-billing-cycle)

As the Hobby plan is a free tier there are no billing cycles. In most cases, if you exceed your usage limits on the Hobby plan, you will have to wait until 30 days have passed before you can use the feature again.

Some features have shorter or longer time periods:

*   [Web Analytics](/docs/analytics/limits-and-pricing#hobby)

As stated in the [fair use guidelines](/docs/limits/fair-use-guidelines#commercial-usage), the Hobby plan restricts users to non-commercial, personal use only.

When your personal account gets converted to a Hobby team, your usage and activity log will be reset. To learn more about this change, read the [changelog](/changelog/2024-01-account-changes).

## [Comparing Hobby and Pro plans](#comparing-hobby-and-pro-plans)

The Pro plan offers more resources and advanced features compared to the Hobby plan. The following table provides a side-by-side comparison of the two plans:

| Feature | Hobby | Pro |
| --- | --- | --- |
| Active CPU | 4 CPU-hrs | 16 CPU-hrs |
| Provisioned Memory | 360 GB-hrs | 1440 GB-hrs |
| ISR Reads | Up to 1,000,000 Reads | 10,000,000 included |
| ISR Writes | Up to 200,000 | 2,000,000 included |
| Edge Requests | Up to 1,000,000 requests | 10,000,000 requests included |
| Projects | 200 | Unlimited |
| Vercel Function maximum duration | 10s (default) - [configurable up to 60s (1 minute)](/docs/functions/limitations#max-duration) | 15s (default) - [configurable up to 300s (5 minutes)](/docs/functions/configuring-functions/duration) |
| Build execution minutes | 6,000 | 24,000 |
| Team collaboration features | \- | Yes |
| Domains per project | 50 | Unlimited |
| Deployments per day | 100 | 6,000 |
| Analytics | 50,000 included Events  
1 month of data | 100,000 included Events  
12 months of data  
Custom events |
| Email support | \- | Yes |
| [Vercel AI Playground models](https://sdk.vercel.ai/) | Llama, GPT 3.5, Mixtral | GPT-4, Claude, Mistral Large, Code Llama |
| [RBAC](/docs/rbac/access-roles) available | N/A | [Owner](/docs/rbac/access-roles#owner-role), [Member](/docs/rbac/access-roles#member-role), [Billing](/docs/rbac/access-roles#billing-role), [Viewer Pro](/docs/rbac/access-roles#viewer-pro-role) |
| [Comments](/docs/comments) | Available | Available for team collaboration |
| Log Drains | \- | [Configurable](/docs/drains/using-drains) (not on a trial) |
| Spend Management | N/A | [Configurable](/docs/spend-management) |
| [Vercel Toolbar](/docs/vercel-toolbar) | Available for certain features | Available |
| [Storage](/docs/storage) | Blob (Beta) | Blob (Beta) |
| [Activity Logs](/docs/observability/activity-log) | Available | Available |
| [Runtime Logs](/docs/runtime-logs) | 1 hour of logs and up to 4000 rows of log data | 1 day of logs and up to 100,000 rows of log data |
| [DDoS Mitigation](/docs/security/ddos-mitigation) | On by default. Optional [Attack Challenge Mode](/docs/attack-challenge-mode). | On by default. Optional [Attack Challenge Mode](/docs/attack-challenge-mode). |
| [Vercel WAF IP Blocking](/docs/security/vercel-waf/ip-blocking) | Up to 10 | Up to 100 |
| [Vercel WAF Custom Rules](/docs/security/vercel-waf/custom-rules) | Up to 3 | Up to 40 |
| Deployment Protection | [Vercel Authentication](/docs/security/deployment-protection/methods-to-protect-deployments/vercel-authentication) | [Vercel Authentication](/docs/security/deployment-protection/methods-to-protect-deployments/vercel-authentication), [Password Protection](/docs/security/deployment-protection/methods-to-protect-deployments/password-protection) (Add-on), [Sharable Links](/docs/security/deployment-protection/methods-to-bypass-deployment-protection/sharable-links) |
| [Deployment Retention](/docs/security/deployment-retention) | Unlimited by default. | Unlimited by default. |

## [Upgrading to Pro](#upgrading-to-pro)

You can take advantage of Vercel's Pro trial to explore [Pro features](/docs/plans/pro-plan) for free during the trial period, with some [limitations](/docs/plans/pro-plan/trials#trial-limitations).

### Experience Vercel Pro for free

Unlock the full potential of Vercel Pro during your 14-day trial with $20 in credits. Benefit from 1 TB Fast Data Transfer, 10,000,000 Edge Requests, up to 200 hours of Build Execution, and access to Pro features like team collaboration and enhanced analytics.

[Start your free Pro trial](/upgrade/docs-trial-button)

To upgrade from a Hobby plan:

1.  Go to your [dashboard](/dashboard). If you're upgrading a team, make sure to select the team you want to upgrade
2.  Go to the Settings tab and select Billing
3.  Under Plan, if your team is eligible for an upgrade, you can click the Upgrade button. Or, you may need to create or select a team to upgrade. In that case, you can click Create a Team or Upgrade a Team
4.  Optionally, add team members. Each member incurs a $20 per user / month charge
5.  Enter your card details
6.  Click Confirm and Upgrade

If you would like to end your paid plan, you can [downgrade to Hobby](/docs/plans/pro#downgrading-to-hobby).

--------------------------------------------------------------------------------
title: "Vercel Pro Plan"
description: "Learn about the Vercel Pro plan with credit-based billing, free viewer seats, and self-serve enterprise features for professional teams."
last_updated: "null"
source: "https://vercel.com/docs/plans/pro-plan"
--------------------------------------------------------------------------------

# Vercel Pro Plan

Copy page

Ask AI about this page

Last updated September 24, 2025

The Vercel Pro plan is designed for professional developers, freelancers, and businesses who need enhanced features and team collaboration.

Teams created on or after September 9, 2025, will be on this pricing model automatically. Teams on the [legacy Pro plan](/docs/plans/pro) are still supported, but will be moved to the new pricing model later this year. [Follow this guide](/docs/plans/pro-plan/switching) to switch early.

## [Pro plan features](#pro-plan-features)

*   [Credit-based billing](#monthly-credit): Pro includes monthly credit that can be used flexibly across [usage dimensions](/docs/pricing#managed-infrastructure-billable-resources)
*   [Free viewer seats](#viewer-team-seat): Unlimited read-only access to the Vercel dashboard for team collaboration
*   [Paid add-ons](#paid-add-ons): Additional enterprise-grade features are available as add-ons

For a full breakdown of the features included in the Pro plan, see the [pricing page](https://vercel.com/pricing).

## [Monthly credit](#monthly-credit)

Every Pro plan comes with $20 in monthly credit. You can use your monthly credit across all infrastructure resources. Once you have used your monthly credit, Vercel bills additional usage on-demand.

The monthly credit applies to all [managed infrastructure billable resources](/docs/pricing#managed-infrastructure-billable-resources) after their respective included allocations are exceeded.

### [Credit and usage allocation](#credit-and-usage-allocation)

*   Monthly credit: Every Pro plan has $20 in monthly credit.
*   Included infrastructure usage: Each month, you have 1 TB [Fast Data Transfer](/docs/edge-network/manage-usage#fast-data-transfer) and 10,000,000 [Edge Requests](/docs/edge-network/manage-usage#edge-requests) included. Once you exceed these included allocations, Vercel will charge usage against your monthly credit before switching to on-demand billing.

### [Credit expiration](#credit-expiration)

The credit and allocations expire at the end of the month if they are not used, and are reset at the beginning of the following month.

### [Managing your spend amount](#managing-your-spend-amount)

You will receive automatic notifications when your usage has reached 75% of your monthly credit. Once you exceed the monthly credit, Vercel switches your team to on-demand usage and you will receive daily and weekly summary emails of your usage.

You can also set up alerts and automatic actions when your account hits a certain spend threshold as described in the [spend management documentation](/docs/spend-management). This can be useful to manage your spend amount once you have used your included credit.

By default, Vercel enables spend management notifications for new customers at a spend amount of $200 per billing cycle.

## [Team seats](#team-seats)

On the Pro plan, your team starts with 1 included paid seat that can deploy projects, manage the team, and access all member-level permissions.

You can add (See the [Managing Team Members documentation](/docs/rbac/managing-team-members#adding-team-members-and-assigning-roles) for more information):

*   Additional paid seats ([Owner](/docs/rbac/access-roles#owner-role) or [Member](/docs/rbac/access-roles#member-role) roles) for $20/month each
*   Unlimited free [Viewer seats](#viewer-team-seat) with read-only access

See the [Team Level Roles Reference](/docs/rbac/access-roles/team-level-roles) for a complete list of roles and their permissions.

## [Viewer team seat](#viewer-team-seat)

Each viewer team seat has the [Viewer Pro](/docs/rbac/access-roles#viewer-pro-role) role with the following access:

*   Read-only access to Vercel to view analytics, speed insights, or access project deployments
*   Ability to comment and collaborate on deployed previews

Viewers cannot configure or deploy projects.

## [Pro plan pricing](#pro-plan-pricing)

The Pro plan is billed monthly based on the number of deploying team seats, paid add-ons, and any on-demand usage during the billing period. Each product has its own pricing structure, and includes both included resources and extra usage charges.

## [Platform fee](#platform-fee)

*   $20/month Pro platform fee
    *   1 deploying team seat included
    *   $20/month in usage credit

See the [pricing](/docs/pricing) page for more information about the pricing for resource usage.

### [Additional team seats](#additional-team-seats)

*   Seats with [Owner](/docs/rbac/access-roles#owner-role) or [Member](/docs/rbac/access-roles#member-role) roles: $20/month each
    *   These team seats have the ability to configure & deploy projects
*   [Viewer Pro](/docs/rbac/access-roles#viewer-pro-role) (read-only) seats: Free

## [Paid add-ons](#paid-add-ons)

The following features are available as add-ons:

*   [SAML Single Sign-On](/docs/saml): $300/month
*   [HIPAA BAA](/docs/security/compliance#hipaa): Healthcare compliance agreements for $350/month
*   [Flags Explorer](/docs/feature-flags/flags-explorer): $250/month
*   [Observability Plus](/docs/observability/observability-plus): $10/month
*   [Web Analytics Plus](/docs/analytics/limits-and-pricing#pro-with-web-analytics-plus): $10/month
*   [Speed Insights](/docs/speed-insights): $10/month per project

## [Downgrading to Hobby](#downgrading-to-hobby)

Each account is limited to one team on the Hobby plan. If you attempt to downgrade a Pro team while already having a Hobby team, the platform will either require one team to be deleted or the two teams to be merged.

To downgrade from a Pro to Hobby plan without losing access to the team's projects:

1.  Navigate to your [dashboard](/dashboard) and select your team from the [scope selector](/docs/dashboard-features#scope-selector)
2.  Select the Settings tab
3.  Select Billing in the Settings navigation
4.  Click Downgrade Plan in the Plan sub-section

When you downgrade a Pro team, all active members except for the original owner are removed.

Due to restrictions in the downgrade flow, Pro teams will need to [manually transfer any connected Stores](/docs/storage#transferring-your-store) and/or [Domains](/docs/domains/working-with-domains/transfer-your-domain#transferring-domains-between-projects) to a new destination before proceeding with downgrade.

### Interested in the Enterprise plan?

Maximize your enterprise with Vercel's tailored plan. Experience high performance, advanced security, and dedicated support. Access empowering features

[Contact Sales](/contact/sales)

--------------------------------------------------------------------------------
title: "Billing FAQ for Pro Plan"
description: "This page covers frequently asked questions around payments, invoices, and billing on the Pro plan."
last_updated: "null"
source: "https://vercel.com/docs/plans/pro-plan/billing"
--------------------------------------------------------------------------------

# Billing FAQ for Pro Plan

Copy page

Ask AI about this page

Last updated September 24, 2025

The Vercel Pro plan is designed for professional developers, freelancers, and businesses who need enhanced features and team collaboration. This page covers frequently asked questions around payments, invoices, and billing on the Pro plan.

## [Payments](#payments)

### [What is the price of the Pro plan?](#what-is-the-price-of-the-pro-plan)

See the [pricing page](/docs/pricing).

### [When are payments taken?](#when-are-payments-taken)

At the beginning of each [billing cycle](#what-is-a-billing-cycle). Each invoice charges for the upcoming billing cycle. It includes any additional usage that occurred during the previous billing cycle.

### [What payment methods are available?](#what-payment-methods-are-available)

Credit/Debit card only.

### [What card types can I pay with?](#what-card-types-can-i-pay-with)

*   American Express
*   China UnionPay (CUP)
*   Discover & Diners
*   Japan Credit Bureau (JCB)
*   Mastercard
*   Visa

### [What currency can I pay in?](#what-currency-can-i-pay-in)

You can pay in any currency so long as the credit card provider allows charging in USD _after_ conversion.

### [What happens when I cannot pay?](#what-happens-when-i-cannot-pay)

When an account goes overdue, some account features are restricted until you make a payment. This means:

*   You can't create new Projects
*   You can't add new team members
*   You can't redeploy existing projects

For subscription renewals, payment must be successfully made within 14 days, else all deployments on your account will be paused. For new subscriptions, the initial payment must be successfully made within 24 hours.

You can be overdue when:

*   The card attached to the team expires
*   The bank declined the payment
    *   Possible incorrect card details
    *   The card is reported lost or stolen
*   There was no card on record or a payment method was removed

To fix, you can add a new payment method to bring your account back online.

### [Can I delay my payment?](#can-i-delay-my-payment)

No, you cannot delay your payment.

### [Can I pay annually?](#can-i-pay-annually)

No. Only monthly payments are supported. You can pay annually if you upgrade to an [Enterprise](/pricing) plan. The Enterprise plan offers increased performance, collaboration, and security needs.

### [Can I change my payment method?](#can-i-change-my-payment-method)

Yes. You will have to add a new payment method before you can remove the old one. To do this:

1.  From your dashboard, select your team in the Scope selector
2.  Go to the Settings tab and select Billing from the left nav
3.  Scroll to Payment Method and select the Add new card button

![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdashboard%2Fscope-selector-light.png&w=640&q=75)![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdashboard%2Fscope-selector-dark.png&w=640&q=75)

Scope selector to switch between teams and accounts.

## [Invoices](#invoices)

### [Can I pay by invoice?](#can-i-pay-by-invoice)

Yes. If you have a card on file, Vercel will charge it automatically. A receipt is then sent to you after your credit card gets charged. To view your past invoices:

*   From your [dashboard](/docs/dashboard-features), go to the Team's page from the scope selector
*   Select the Settings tab followed by the Invoices link on the left

If you do not have a card on file, then you will have to add a payment method, and you will receive a receipt of payment.

### [Why am I overdue?](#why-am-i-overdue)

We were unable to charge your payment method for your latest invoice. This likely means that the payment was not successfully processed with the credit card on your account profile.

Some senders deduct a payment fee for transaction costs. This could mean that the amount charged on the invoice, does not reflect the amount due. To fix this make sure you add the transaction fee to the amount you send.

See [What happens when I cannot pay](#what-happens-when-i-cannot-pay) for more information.

### [Can I change an existing invoice detail?](#can-i-change-an-existing-invoice-detail)

Invoice details must be accurate before adding a credit card at the end of a trial, or prior to the upcoming invoice being finalized. You can update your billing details on the [Billing settings page](/account/billing).

Changes are reflected on future invoices only. Details on previous invoices will remain as they were issued and cannot be changed.

### [Does Vercel possess and display their VAT ID on invoices?](#does-vercel-possess-and-display-their-vat-id-on-invoices)

No. Vercel is a US-based entity and does not have a VAT ID. If applicable, customers are encouraged to add their own VAT ID to their billing details for self-reporting and tax compliance reasons within their respective country.

### [Can invoices be sent to my email?](#can-invoices-be-sent-to-my-email)

Yes. By default, invoices are sent to the email address of the first [owner](/docs/accounts/team-members-and-roles/access-roles#owner-role) of the team. To set a custom destination email address for your invoices, follow these steps:

1.  From your [dashboard](/dashboard), navigate to the Settings tab
2.  Select Billing from the sidebar
3.  Scroll down to find the editable Invoice Email Recipient field

If you are having trouble receiving these emails, please review the spam settings of your email workspace as these emails may be getting blocked.

### [Can I repay an invoice if I've used the wrong payment method?](#can-i-repay-an-invoice-if-i've-used-the-wrong-payment-method)

No. Once an invoice is paid, it cannot be recharged with a different payment method, and refunds are not provided in these cases.

## [Billing](#billing)

### [How are add-ons billed?](#how-are-add-ons-billed)

Pro add-ons are billed in the subsequent billing cycle as a line item on your invoice.

### [What happens if I purchase an add-on by mistake?](#what-happens-if-i-purchase-an-add-on-by-mistake)

[Open a support ticket](/help#issues) for your request and our team will assist you.

### [What do I do if I think my bill is wrong?](#what-do-i-do-if-i-think-my-bill-is-wrong)

Please [open a support ticket](/help#issues) and provide the following information:

*   Invoice ID
*   The account email
*   The Team name
*   If your query relates to the monthly plan, or usage billing

### [Do I get billed for DDoS?](#do-i-get-billed-for-ddos)

[Vercel automatically mitigates against L3, L4, and L7 DDoS attacks](/docs/security/ddos-mitigation) at the platform level for all plans. Vercel does not charge customers for traffic that gets blocked by the Firewall.

Usage will be incurred for requests that are successfully served prior to us automatically mitigating the event. Usage will also be incurred for requests that are not recognized as a DDoS event, which may include bot and crawler traffic.

For an additional layer of security, we recommend that you enable [Attack Challenge Mode](/docs/attack-challenge-mode) when you are under attack, which is available for free on all plans. While some malicious traffic is automatically challenged, enabling Attack Challenge Mode will challenge all traffic, including legitimate traffic to ensure that only real users can access your site.

You can monitor usage in the [Vercel Dashboard](/dashboard) under the Usage tab, although you will [receive notifications](/docs/notifications#on-demand-usage-notifications) when nearing your usage limits.

### [What is a billing cycle?](#what-is-a-billing-cycle)

The billing cycle refers to the period of time between invoices. The start date depends on when you created the account, or the account's trial phase ended. You can view your current and previous billing cycles on the Usage tab of your dashboard.

The second tab indicates the range of the billing cycle. During this period, you would get billed for:

*   The amount of Team seats you have, and any addons you have purchased - Billed for the next 30 days of usage
*   The usage consumed during the last billing cycle - Billed for the last 30 days of additional usage

You can't change a billing cycle or the dates on which you get billed. You can view the current billing cycle by going to the Settings tab and selecting Billing.

### [What if my usage goes over the included credit?](#what-if-my-usage-goes-over-the-included-credit)

You will be charged for on-demand usage, which is billed at the end of the month.

### [What's the benefit of the credit-based model?](#what's-the-benefit-of-the-credit-based-model)

The monthly credit gives teams flexibility to allocate usage based on their actual workload, rather than being locked into rigid usage buckets they may not fully use.

## [Access](#access)

### [What can the Viewer seat do?](#what-can-the-viewer-seat-do)

[Viewer seats](/docs/plans/pro-plan#viewer-team-seat) can:

*   View and comment on deployments
*   Access analytics and project insights

--------------------------------------------------------------------------------
title: "Switching to the new pricing model"
description: "Learn how to switch from the legacy Pro plan to the new pricing model."
last_updated: "null"
source: "https://vercel.com/docs/plans/pro-plan/switching"
--------------------------------------------------------------------------------

# Switching to the new pricing model

Copy page

Ask AI about this page

Last updated September 24, 2025

This guide is for existing customers who would like to switch to the [new pricing model](/docs/plans/pro-plan), which you can do in [a few steps](#switch-to-the-new-pricing-model). For a smooth transition and to optimize your usage in advance, this guide includes [recommended tasks](#before-switching-to-the-new-pricing-model) you can perform before making the switch.

*   Learn more about the [new pricing model](/docs/plans/pro-plan#pro-plan-features) before switching.
*   Follow this [link](https://vercel.com/d?to=%2F%5Bteam%5D%2F%7E%2Fsettings%2Fbilling&title=) to select an existing Pro team and switch now.

Teams created on or after September 9, 2025, will be on this pricing model automatically. The [legacy Pro plan](/docs/plans/pro) is still supported, but all teams will move to the new pricing model later this year.

## [Before switching to the new pricing model](#before-switching-to-the-new-pricing-model)

### [Enable the new Image Optimization pricing](#enable-the-new-image-optimization-pricing)

If your team is still using the [legacy Image Optimization pricing](/docs/image-optimization/legacy-pricing), enabling the [new pricing model](/docs/image-optimization/limits-and-pricing) before switching will typically lower your overall usage.

1.  Navigate to your Pro plan Team Settings tab. Select Billing and go down to Image Optimization.
2.  If its not already activated, click on Review Cost Estimate to review.
3.  Click Accept to enable the new pricing model.

### [Ensure Fluid compute is enabled](#ensure-fluid-compute-is-enabled)

[Fluid compute](/docs/fluid-compute) with active CPU pricing optimizes Vercel Function costs. It is enabled by default for all recent projects. You can ensure it is enabled for other projects by following the steps below:

1.  Navigate to the Settings tab of your [project](/docs/projects/project-dashboard).
2.  Select Functions from the left sidebar.
3.  Under Fluid compute, ensure that the toggle is enabled.

### [Plan for Viewer seats](#plan-for-viewer-seats)

[Viewer seats](/docs/plans/pro-plan#viewer-team-seat) are unlimited and free on the new pricing model. To maximize savings, review your team and switch non-deploying team members to the Viewer role after switching.

1.  Navigate to your Pro plan Team Settings tab and select Members.
2.  Create a list of team members who don't need to deploy code (e.g., content editors, designers, project managers).
3.  Review their current permissions and access needs.
4.  Plan to convert this list to Viewer seats immediately after switching.

## [Switch to the new pricing model](#switch-to-the-new-pricing-model)

If you are an existing customer, you can choose to switch to the new pricing model now or continue using the [legacy Pro plan](/docs/plans/pro) until you are transitioned automatically.

You can switch by doing one of the following:

*   Clicking the Pro badge button to the right of your team name in the [dashboard](/dashboard) if this team is on the Pro plan.
*   Clicking Review and Switch by following this [link](https://vercel.com/d?to=%2F%5Bteam%5D%2F%7E%2Fsettings%2Fbilling&title=) and choosing an existing Pro team.
*   Following these steps:
    1.  Navigate to your [dashboard](/dashboard) and select your team from the [scope selector](/docs/dashboard-features#scope-selector)
    2.  Select the Settings tab and select Billing.
    3.  From the Pro Plan section, click Review & Switch.
    4.  Review the summary of the total charges and available credits and click Switch to proceed.
    5.  Once the transition is complete, your Pro Plan in Billing will be updated to the new pricing model.

--------------------------------------------------------------------------------
title: "Understanding Vercel's Pro Plan Trial"
description: "Learn all about Vercel's Pro Plan free trial, including features, usage limits, and options post-trial. Learn how to manage your team's projects with Vercel's Pro Plan trial."
last_updated: "null"
source: "https://vercel.com/docs/plans/pro-plan/trials"
--------------------------------------------------------------------------------

# Understanding Vercel's Pro Plan Trial

Copy page

Ask AI about this page

Last updated October 9, 2025

Vercel offers three plan tiers: Hobby, Pro, and Enterprise.

The Pro trial offers an opportunity to explore [Pro features](/docs/plans/pro-plan) for free during the trial period. There are some [limitations](/docs/plans/pro-plan/trials#trial-limitations).

## [Starting a trial](#starting-a-trial)

There is a limit of two Pro plan trials per user account.

1.  Select the [scope selector](/docs/dashboard-features#scope-selector) from the dashboard. From the bottom of the list select Create Team. Alternatively, click this button:
    
    ### Experience Vercel Pro for free
    
    Unlock the full potential of Vercel Pro during your 14-day trial with $20 in credits. Benefit from 1 TB Fast Data Transfer, 10,000,000 Edge Requests, up to 200 hours of Build Execution, and access to Pro features like team collaboration and enhanced analytics.
    
    [Start your free Pro trial](/upgrade/docs-trial-button)
    
2.  Name your team
3.  Select the Pro Trial option from the dialog. If this option does not appear, it means you have already reached your limit of two trials:

![Selecting a team plan.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fteams%2Fnew-team-light.png&w=1080&q=75)![Selecting a team plan.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fteams%2Fnew-team-dark.png&w=1080&q=75)

Selecting a team plan.

## [Trial Limitations](#trial-limitations)

The trial plan includes a $20 credit and follows the same [general limits](/docs/limits#general-limits) as a regular plan but with specified usage restrictions. See how these compare to the [non-trial usage limits](/docs/limits#included-usage):

|  | Pro Trial Limits |
| --- | --- |
| Owner Members | 1 |
| Team Members (total, including Owners) | 10 |
| Projects | 200 |
| [Active CPU](/docs/functions/usage-and-pricing) | 8 CPU-hrs |
| [Provisioned Memory](/docs/functions/usage-and-pricing) | 720 GB-hrs |
| [Function Invocations](/docs/functions/usage-and-pricing) | 1,000,000/month |
| Build Execution | Max. 200 Hrs |
| [Image transformations](/docs/image-optimization/limits-and-pricing#image-transformations) | Max. 5K/month |
| [Image cache reads](/docs/image-optimization/limits-and-pricing#image-cache-reads) | Max. 300K/month |
| [Image cache writes](/docs/image-optimization/limits-and-pricing#image-cache-writes) | Max. 100K/month |
| [Monitoring](/docs/observability/monitoring) | Max. 125,000 metrics |
| Domains per Project | 50 |

To monitor the current usage of your Team's projects, see the [Usage](/docs/limits/usage) guide.

The following Pro features are not available on the trial:

*   [Log drains](/docs/log-drains)
*   [Account webhooks](/docs/webhooks#account-webhooks)
*   Certain models (GPT-5 and Claude) on [Vercel AI Playground](https://sdk.vercel.ai/)

Once your usage of [Active CPU](/docs/functions/usage-and-pricing), [Provisioned Memory](/docs/functions/usage-and-pricing), or [Function Invocations](/docs/functions/usage-and-pricing) exceeds or reaches 100% of the Pro trial usage, your trial will be paused.

## [Post-Trial Decision](#post-trial-decision)

Your trial finishes after 14 days or once your team exceeds the usage limits, whichever happens first. After which, you can opt for one of two paths:

*   [Upgrade to a paid Pro plan](#upgrade-to-a-paid-pro-plan)
*   [Revert to a Hobby plan](#revert-to-a-hobby-plan)

### [Upgrade to a paid Pro plan](#upgrade-to-a-paid-pro-plan)

If you wish to continue on the Pro plan, you must add a payment method to ensure a seamless transition from the trial to the paid plan when your trial ends.

To add a payment method, navigate to the Billings page through Settings > Billing. From this point, you will get billed according to the [number of users in your team](/docs/plans/pro/billing#what-is-a-billing-cycle).

#### [When will I get billed?](#when-will-i-get-billed)

Billing begins immediately after your trial ends if you have added a payment method.

### [Revert to a Hobby plan](#revert-to-a-hobby-plan)

Without a payment method, your account reverts to a Hobby plan when the trial ends. Alternatively, you can use the Downgrade button located in the Pro Plan section of your [team's Billing page](https://vercel.com/d?to=%2F%5Bteam%5D%2F%7E%2Fsettings%2Fbilling&title=Go+to+Billing) to immediately end your trial and return to a Hobby plan. All team members will be removed from your team, and all Hobby limits will apply to your team.

Charges apply only if you have a payment method. If a trial finishes and you haven't set payment method, you will **not** get charged.

You can upgrade to a Pro plan anytime later by visiting Settings > Billing and adding a payment method.

### [Downgraded to Hobby](#downgraded-to-hobby)

If your Pro trial account gets downgraded to a Hobby team, you can revert this by upgrading to Pro. If you've transferred out the projects that were exceeding the included Hobby usage and want to unpause your Hobby team, [contact support](/help).

When you upgrade to Pro, the pause status on your account will get lifted. This reinstates:

*   Full access to all previous projects and deployments
*   Access to the increased limits and features of a Pro account

#### [What if I resume using Vercel months after my trial ends?](#what-if-i-resume-using-vercel-months-after-my-trial-ends)

No charges apply for the months of inactivity. Billing will only cover the current billing cycle.

--------------------------------------------------------------------------------
title: "Postgres on Vercel"
description: "Learn how to use Postgres databases through the Vercel Marketplace."
last_updated: "null"
source: "https://vercel.com/docs/postgres"
--------------------------------------------------------------------------------

# Postgres on Vercel

Copy page

Ask AI about this page

Last updated July 22, 2025

Vercel lets you connect external Postgres databases through the [Marketplace](/marketplace), allowing you to connect external Postgres databases to your Vercel projects without managing database servers.

*   Explore [Marketplace storage postgres integrations](/marketplace?category=storage&search=postgres).
*   Learn how to [add a Marketplace native integration](/docs/integrations/install-an-integration/product-integration).

## [Connecting to the Marketplace](#connecting-to-the-marketplace)

Vercel enables you to use Postgres by integrating with external database providers. By using the Marketplace, you can:

*   Select from a [range of Postgres providers](/marketplace?category=storage&search=postgres)
*   Provision and configure a Postgres database with minimal setup.
*   Have credentials and [environment variables](/docs/environment-variables) injected into your Vercel project.

--------------------------------------------------------------------------------
title: "Pricing on Vercel"
description: "Learn about Vercel's pricing model, including the resources and services that are billed, and how they are priced."
last_updated: "null"
source: "https://vercel.com/docs/pricing"
--------------------------------------------------------------------------------

# Pricing on Vercel

Copy page

Ask AI about this page

Last updated October 30, 2025

This page provides an overview of Vercel's pricing model and outlines all billable metrics and their pricing models.

For a full breakdown of Vercel's pricing by plan, see the [pricing page](https://vercel.com/pricing/coming-soon).

To learn how resources are triggered through a real-world app scenario, see the [calculating resource usage](/docs/pricing/how-does-vercel-calculate-usage-of-resources) guide.

## [Managed Infrastructure](#managed-infrastructure)

Vercel provides [Managed Infrastructure](https://vercel.com/products/managed-infrastructure) to deploy, scale, and secure your applications.

These resources are usage based, and billed based on the amount of data transferred, the number of requests made, and the duration of compute resources used.

Each product's usage breaks down into resources, with each one billed based on the usage of a specific metric. For example, [Function Duration](/docs/functions/configuring-functions/duration) generates bills based on the total execution time of a Vercel Function.

### [Managed Infrastructure billable resources](#managed-infrastructure-billable-resources)

Most resources include an amount of usage your projects can use within your billing cycle. If you exceed the included amount, you are charged for the extra usage.

See the following pages for more information on the pricing of each managed infrastructure resource:

*   [Vercel Functions](/docs/functions/usage-and-pricing)
*   [Image Optimization](/docs/image-optimization/limits-and-pricing)
*   [Edge Config](/docs/edge-config/edge-config-limits)
*   [Web Analytics](/docs/analytics/limits-and-pricing)
*   [Speed Insights](/docs/speed-insights/limits-and-pricing)
*   [Drains](/docs/drains#usage-and-pricing)
*   [Monitoring](/docs/monitoring/limits-and-pricing)
*   [Observability](/docs/observability/limits-and-pricing)
*   [Blob](/docs/vercel-blob/usage-and-pricing)
*   [Microfrontends](/docs/microfrontends#limits-and-pricing)

For [Enterprise](/docs/plans/enterprise) pricing, contact our [sales team](/contact/sales).

#### [Pro plan add-ons](#pro-plan-add-ons)

To enable any of the Pro plan add-ons:

1.  Visit the Vercel [dashboard](/dashboard) and select your team from the [scope selector](/docs/dashboard-features#scope-selector).
2.  Select the Settings tab and go to Billing.
3.  In the Add-Ons section, find the add-on you'd like to add. Switch the toggle to Enabled and configure the add-on as necessary.

#### [Regional pricing](#regional-pricing)

See the [regional pricing](/docs/pricing/regional-pricing) page for more information on Managed Infrastructure pricing in different regions.

## [Developer Experience Platform](#developer-experience-platform)

Vercel's Developer Experience Platform [(DX Platform)](https://vercel.com/products/dx-platform) offers a monthly billed suite of tools and services focused on building, deploying, and optimizing web applications.

### [DX Platform billable resources](#dx-platform-billable-resources)

The below table lists the billable DX Platform resources for the Pro plan. These resources are not usage based, and are billed at a fixed monthly rate.

DX Platform pricing
| 
Resource

 | 

Included

 | 

Price

 |
| --- | --- | --- |
| 

[Team seats](/docs/plans/pro#team-seats)

 | N/A | $20 / month per additional paid seat |
| 

[Preview Deployment Suffix](/docs/deployments/generated-urls#preview-deployment-suffix)

Pro add-on

 | N/A | $100 / month |
| 

[SAML Single Sign-On](/docs/saml)

Pro add-on

 | N/A | $300 / month |
| 

[HIPAA BAA](/docs/security/compliance#hipaa)

Pro add-on

 | N/A | $350 / month |
| 

[Flags Explorer](/docs/feature-flags/flags-explorer)

Pro add-on

 | N/A | $250 / month |
| 

[Observability Plus](/docs/observability/observability-plus)

Pro add-on

 | N/A | $10 / month |
| 

[Web Analytics Plus](/docs/analytics/limits-and-pricing#pro-with-web-analytics-plus)

Pro add-on

 | N/A | $10 / month |
| 

[Speed Insights](/docs/speed-insights)

Pro add-on

 | N/A | $10 / month per project |

To learn more about DX Platform on the Pro plan, and how to understand your invoices, see [understanding my invoice.](/docs/plans/pro)

## [More resources](#more-resources)

For more information on Vercel's pricing, guidance on optimizing consumption, and invoices, see the following resources:

*   [How are resources used on Vercel?](/docs/pricing/how-does-vercel-calculate-usage-of-resources)
*   [Manage and optimize usage](/docs/pricing/manage-and-optimize-usage)
*   [Understanding my invoice](/docs/pricing/understanding-my-invoice)
*   [Improved infrastructure pricing](/blog/improved-infrastructure-pricing)
*   [Regional pricing](/docs/pricing/regional-pricing)

--------------------------------------------------------------------------------
title: "Calculating usage of resources"
description: "Understand how Vercel measures and calculates your resource usage based on a typical user journey."
last_updated: "null"
source: "https://vercel.com/docs/pricing/how-does-vercel-calculate-usage-of-resources"
--------------------------------------------------------------------------------

# Calculating usage of resources

Copy page

Ask AI about this page

Last updated September 24, 2025

It's important to understand how usage and accrual happen on Vercel, in order to make the best choices for your project. This guide helps you understand that by exploring a user journey through an ecommerce store.

You'll learn how resources are used at each stage of the journey, from entering the site, to browsing products, interacting with dynamic content, and engaging with A/B testing for personalized content.

## [Understanding Vercel resources](#understanding-vercel-resources)

The scenarios and resource usage described in this guide are for illustrative purposes only.

Usage is accrued as users visit your site. Vercel's framework-defined infrastructure determines how your site renders and how your costs accrue, based on the makeup of your application code, and the framework you use.

A typical user journey through an ecommerce store touches on multiple resources used in Vercel's [managed infrastructure](/docs/pricing#managed-infrastructure).

The ecommerce store employs a combination of caching strategies to optimize both static and dynamic content delivery. For static pages, it uses [Incremental Static Regeneration (ISR)](/docs/incremental-static-regeneration).

For dynamic content like product price discounts, the site uses [Vercel Data Cache](/docs/infrastructure/data-cache) to store and retrieve the latest product information. This ensures that all users see the most up-to-date pricing information, while minimizing the need to fetch data from the backend on each request.

For dynamic, user-specific content like shopping cart states, [Vercel KV](/docs/storage/vercel-kv) is used. This allows the site to store and retrieve user-specific data in real-time, ensuring a seamless experience across sessions.

The site also uses [Middleware](/docs/routing-middleware) to A/B test a product carousel, showing different variants to different users based on their behavior or demographics.

The following sections outline the resources used at each stage of the user journey.

### [1\. User enters the site](#1.-user-enters-the-site)

![1. User enters your site](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fpricing%2Fenters-site-light.png&w=3840&q=75)![1. User enters your site](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fpricing%2Fenters-site-dark.png&w=3840&q=75)

1\. User enters your site

The browser requests the page from Vercel. Since it's static and cached on our global [CDN](/docs/cdn), this only involves [Edge Requests](/docs/manage-cdn-usage#edge-requests) (the network requests required to get the content of the page) and [Fast Data Transfer](/docs/manage-cdn-usage#fast-data-transfer) (the amount of content sent back to the browser).

Priced resources

*   Edge Requests: Charged per network request to the CDN
*   Fast Data Transfer : Charged based on data moved to the user from the CDN

### [2\. Product browsing](#2.-product-browsing)

![2. User browses products](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fpricing%2Fbrowse-products-light.png&w=3840&q=75)![2. User browses products](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fpricing%2Fbrowse-products-dark.png&w=3840&q=75)

2\. User browses products

During the user's visit to the site, they browse the All Products page, which is populated with a list of cached product images and price details. The request to view the page triggers an [Edge Request](/docs/manage-cdn-usage#edge-requests) to Vercel's CDN, which serves the static assets from the [cache](/docs/edge-cache).

Priced resources

*   Edge Requests: Charged for network requests to fetch product images/details
*   Fast Data Transfer : Data movement charges from CDN to the user

### [3\. Viewing updated product details](#3.-viewing-updated-product-details)

![3. User browses updated products](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fpricing%2Fupdated-product-light.png&w=3840&q=75)![3. User browses updated products](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fpricing%2Fupdated-product-dark.png&w=3840&q=75)

3\. User browses updated products

The user decides to view the details of a product. This products price was recently updated and the first view of the page shows the stale content from the cache due to the revalidation period having ended.

Behind the scenes the site uses [Incremental Static Regeneration (ISR)](/docs/incremental-static-regeneration) to update the products description and image. The new information for the product is then cached on Vercel's [CDN](/docs/cdn) for future requests, and the revalidation period is reset.

For products with real-time discounts, these discounts are calculated using a [Vercel Function](/docs/functions) that fetches the latest product information from the backend. The results, which include any standard discounts applicable to all users, are cached using the [Vercel Data Cache](/docs/infrastructure/data-cache).

Upon viewing a product, if the discount data is already in the Data Cache and still fresh, it will be served from there. If the data is stale, it will be re-fetched and cached again for future requests. This ensures that all users see the most up-to-date pricing information.

Priced resources

*   Edge requests: Network request charges for fetching updated product information
*   Function Invocations : Charges for activating a function to update content
*   Function Duration : CPU runtime charges for the function processing the update

### [4\. Dynamic interactions (Cart)](#4.-dynamic-interactions-cart)

![4. User interacts with dynamic cart](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fpricing%2Fdynamic-cart-light.png&w=3840&q=75)![4. User interacts with dynamic cart](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fpricing%2Fdynamic-cart-dark.png&w=3840&q=75)

4\. User interacts with dynamic cart

The user decides to add a product to their cart. The cart is a dynamic feature that requires real-time updates. When the user adds an item to their cart, [Vercel KV](/docs/storage/vercel-kv) is used to store the cart state. If the user leaves and returns to the site, the cart state is retrieved from the KV store, ensuring a seamless experience across sessions.

Priced resources

*   Edge Requests: Network request charges for cart updates
*   Function Invocations : Function activation charges for managing cart logic
*   Function Duration : CPU runtime charges for the function processing the cart logic
*   Fast origin Transfer : Data movement charges for fetching cart state from the cache
*   KV Requests: Charges for reading and writing cart state to the KV store
*   KV Storage: Charges for storing cart state in the KV store
*   KV Data Transfer: Data movement charges for fetching cart state from the KV store

### [5\. Engaging with A/B testing for personalized content](#5.-engaging-with-a/b-testing-for-personalized-content)

![5. User is shown a variant of the site based on their behavior or demographics](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fpricing%2Fa-b-test-light.png&w=3840&q=75)![5. User is shown a variant of the site based on their behavior or demographics](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fpricing%2Fa-b-test-dark.png&w=3840&q=75)

5\. User is shown a variant of the site based on their behavior or demographics

Having added an item to the cart, the user decides to continue browsing the site. They scroll to the bottom of the page and are shown a product carousel. This carousel is part of an A/B test using [Middleware](/docs/routing-middleware), and the user is shown a variant based on their behavior or demographics.

Priced resources

*   Edge Requests: Network request charges for delivering test variants

## [Summary and next steps](#summary-and-next-steps)

Throughout the user journey through the site, a variety of resources are used from Vercel's [managed infrastructure](/docs/pricing#managed-infrastructure). When thinking about how to optimize resource consumption, it's important to consider how each resource is triggered and how it accrues usage over time and across different user interactions.

To learn more about each of the resources used in this guide, see the [managed infrastructure billable resources](/docs/pricing#managed-infrastructure-billable-resources) documentation. To learn about how to optimize resource consumption, see the [Manage and optimize usage](/docs/pricing/manage-and-optimize-usage) guide.

## [More resources](#more-resources)

For more information on Vercel's pricing, guidance on optimizing consumption, and invoices, see the following resources:

*   [Learn about Vercel's pricing model and how it works](/docs/pricing)
*   [Learn how Vercel usage is calculated and how it accrues](/docs/pricing/manage-and-optimize-usage)
*   [Learn how to understand your Vercel invoice](/docs/pricing/understanding-my-invoice)

--------------------------------------------------------------------------------
title: "Legacy Metrics"
description: "Learn about Bandwidth, Requests, Vercel Function Invocations, and Vercel Function Execution metrics."
last_updated: "null"
source: "https://vercel.com/docs/pricing/legacy"
--------------------------------------------------------------------------------

# Legacy Metrics

Copy page

Ask AI about this page

Last updated September 24, 2025

## [Bandwidth](#bandwidth)

Bandwidth is the amount of data your deployments have sent or received. This chart includes traffic for both [preview](/docs/deployments/environments#preview-environment-pre-production) and [production](/docs/deployments/environments#production-environment) deployments.

You are not billed for bandwidth usage on [blocked or paused](https://vercel.com/guides/why-is-my-account-deployment-blocked#pausing-process) deployments.

The total traffic of your projects is the sum of the outgoing and incoming bandwidth.

*   Outgoing: Outgoing bandwidth measures the amount of data that your deployments have sent to your users. Data used by [ISR](/docs/incremental-static-regeneration) and the responses from the [CDN](/docs/cdn) and [Vercel functions](/docs/functions) count as outgoing bandwidth
*   Incoming: Incoming bandwidth measures the amount of data that your deployments have received from your users

An example of incoming bandwidth would be page views requested by the browser. All requests sent to the [CDN](/docs/cdn) and [Vercel functions](/docs/functions) are collected as incoming bandwidth.

Incoming bandwidth is usually much smaller than outgoing bandwidth for website projects.

## [Requests](#requests)

Requests are the number of requests made to your deployments. This chart includes traffic for both [preview](/docs/deployments/environments#preview-environment-pre-production) and [production](/docs/deployments/environments#production-environment) deployments.

Requests can be filtered by:

*   Ratio: The ratio of requests that are cached and uncached by the [CDN](/docs/cdn)
*   Projects: The projects that the requests are made to

## [Vercel Function Invocations](#vercel-function-invocations)

Vercel Function Invocations are the number of times your [Vercel functions](/docs/functions) have receive a request, excluding cache hits.

Vercel Function Invocations can be filtered by:

*   Ratio: The ratio of invocations that are Successful, Errored, or Timed out
*   Projects: The projects that the invocations are made to

## [Vercel Function Execution](#vercel-function-execution)

Vercel Function Execution is the amount of time your [Vercel functions](/docs/functions) have spent computing resources.

Vercel Function Execution can be filtered by:

*   Ratio: The ratio of execution time that is Completed, Errored, or Timed out
*   Projects: The projects that the execution time is spent on

--------------------------------------------------------------------------------
title: "Manage and optimize usage"
description: "Understand how to manage and optimize your usage on Vercel, learn how to track your usage, set up alerts, and optimize your usage to save costs."
last_updated: "null"
source: "https://vercel.com/docs/pricing/manage-and-optimize-usage"
--------------------------------------------------------------------------------

# Manage and optimize usage

Copy page

Ask AI about this page

Last updated September 15, 2025

## [What pricing plan am I on?](#what-pricing-plan-am-i-on)

There are three plans on Vercel: Hobby, Pro, and Enterprise. To see which plan you are on, select your team from the [scope selector](/docs/dashboard-features#scope-selector). Next to your team name, you will see the plan you are on.

## [Viewing usage](#viewing-usage)

The Usage page shows the usage of all projects in your Vercel account by default. To access it, select the Usage tab from your Vercel [dashboard](/dashboard).

To use the usage page:

1.  To investigate the usage of a specific team, use the scope selector to select your team
2.  From your dashboard, select the Usage tab
3.  We recommend you look at usage over the last 30 days to determine patterns. Change the billing cycle dropdown under Usage to Last 30 days
4.  You can choose to view the usage of a particular project by selecting it from the dropdown
5.  In the overview, you'll see an allotment indicator. It shows how much of your usage you've consumed in the current cycle and the projected cost for each item
6.  Use the [Top Paths](/docs/manage-cdn-usage#top-paths) chart to understand the metrics causing the high usage

## [Usage alerts, notification, and spend management](#usage-alerts-notification-and-spend-management)

The usage dashboard helps you understand and project your usage. You can also set up alerts to notify you when you're approaching usage limits. You can set up the following features:

*   Spend Management: Spend management is an opt-in feature. Pro teams can set up a spend amount for your team to trigger notifications or actions. For example a webhook or pausing your projects when you hit your set amount
*   Usage Notifications: Usage notifications are set up automatically. Pro teams can also [configure the threshold](/docs/notifications#on-demand-usage-notifications) for usage alerts to notify you when you're approaching your usage limits

### Interested in the Enterprise plan?

Contact our sales team to learn more about the Enterprise plan and how it can benefit your team.

[Contact Sales](/contact/sales)

## [Networking](#networking)

The table below shows the metrics for the [Networking](/docs/pricing/networking) section of the Usage dashboard.

To view information on managing each resource, select the resource link in the Metric column. To jump straight to guidance on optimization, select the corresponding resource link in the Optimize column.

Manage and Optimize pricing
| 
Metric

 | 

Description

 | 

Priced

 | 

Optimize

 |
| --- | --- | --- | --- |
| [Top Paths](/docs/manage-cdn-usage#top-paths) | The paths that consume the most resources on your team | N/A | N/A |
| [Fast Data Transfer](/docs/manage-cdn-usage#fast-data-transfer) | The data transfer between Vercel's CDN and your sites' end users. | [Yes](/docs/pricing/regional-pricing) | [Learn More](/docs/manage-cdn-usage#optimizing-fast-data-transfer) |
| [Fast Origin Transfer](/docs/manage-cdn-usage#fast-origin-transfer) | The data transfer between Vercel's CDN to Vercel Compute | [Yes](/docs/pricing/regional-pricing) | [Learn More](/docs/manage-cdn-usage#optimizing-fast-origin-transfer) |
| [Edge Requests](/docs/manage-cdn-usage#edge-requests) | The number of cached and uncached requests that your deployments have received | [Yes](/docs/pricing/regional-pricing) | [Learn More](/docs/manage-cdn-usage#optimizing-edge-requests) |

## [Serverless Functions](#serverless-functions)

The table below shows the metrics for the [Serverless Functions](/docs/pricing/serverless-functions) section of the Usage dashboard.

To view information on managing each resource, select the resource link in the Metric column. To jump straight to guidance on optimization, select the corresponding resource link in the Optimize column.

Manage and Optimize pricing
| 
Metric

 | 

Description

 | 

Priced

 | 

Optimize

 |
| --- | --- | --- | --- |
| [Function Invocations](/docs/pricing/serverless-functions#managing-function-invocations) | The number of times your Functions have been invoked | [Yes](/docs/pricing#managed-infrastructure-billable-resources) | [Learn More](/docs/pricing/serverless-functions#optimizing-function-invocations) |
| [Function Duration](/docs/pricing/serverless-functions#managing-function-duration) | The time your Serverless Functions have spent responding to requests | [Yes](/docs/pricing#managed-infrastructure-billable-resources) | [Learn More](/docs/pricing/serverless-functions#optimizing-function-duration) |
| [Throttles](/docs/pricing/serverless-functions#throttles) | Instances where requests to Functions are not served due to concurrency limits | No | N/A |

## [Builds](#builds)

The table below shows the metrics for the [Builds](/docs/builds/managing-builds) section of the Usage dashboard.

To view information on managing each resource, select the resource link in the Metric column. To jump straight to guidance on optimization, select the corresponding resource link in the Optimize column.

Manage and Optimize pricing
| 
Metric

 | 

Description

 | 

Priced

 | 

Optimize

 |
| --- | --- | --- | --- |
| [Build Time](/docs/builds/managing-builds#managing-build-time) | The amount of time your Deployments have spent being queued or building | No | [Learn More](/docs/builds/managing-builds#managing-build-time) |
| [Number of Builds](/docs/builds/managing-builds#number-of-builds) | How many times a build was issued for one of your Deployments | No | N/A |

## [Artifacts](#artifacts)

The table below shows the metrics for the [Remote Cache Artifacts](/docs/monorepos/remote-caching#artifacts) section of the Usage dashboard.

To view information on managing each resource, select the resource link in the Metric column. To jump straight to guidance on optimization, select the corresponding resource link in the Optimize column.

Manage and Optimize pricing
| 
Metric

 | 

Description

 | 

Priced

 | 

Optimize

 |
| --- | --- | --- | --- |
| [Number of Remote Cache Artifacts](/docs/monorepos/remote-caching#number-of-remote-cache-artifacts) | The number of uploaded and downloaded artifacts using the Remote Cache API | No | N/A |
| [Total Size of Remote Cache Artifacts](/docs/monorepos/remote-caching#managing-total-size-of-remote-cache-artifacts) | The size of uploaded and downloaded artifacts using the Remote Cache API | No | [Learn More](/docs/monorepos/remote-caching#optimizing-total-size-of-remote-cache-artifacts) |
| [Time Saved](/docs/monorepos/remote-caching#time-saved) | The time saved by using artifacts cached on the Vercel Remote Cache API | No | N/A |

## [Edge Config](#edge-config)

The table below shows the metrics for the [Edge Config](/docs/pricing/edge-config) section of the Usage dashboard.

To view information on managing each resource, select the resource link in the Metric column. To jump straight to guidance on optimization, select the corresponding resource link in the Optimize column.

Manage and Optimize pricing
| 
Metric

 | 

Description

 | 

Priced

 | 

Optimize

 |
| --- | --- | --- | --- |
| [Reads](/docs/pricing/edge-config#reviewing-edge-config-reads) | The number of times your Edge Config has been read | [Yes](/docs/pricing#managed-infrastructure-billable-resources) | [Learn More](/docs/pricing/edge-config#optimizing-edge-config-reads) |
| [Writes](/docs/pricing/edge-config#managing-edge-config-writes) | The number of times your Edge Config has been updated | [Yes](/docs/pricing#managed-infrastructure-billable-resources) | [Learn More](/docs/pricing/edge-config#optimizing-edge-config-writes) |

## [Data Cache](#data-cache)

The table below shows the metrics for the [Data Cache](/docs/data-cache) section of the Usage dashboard.

To view information on managing each resource, select the resource link in the Metric column. To jump straight to guidance on optimization, select the corresponding resource link in the Optimize column.

Manage and Optimize pricing
| 
Metric

 | 

Description

 | 

Priced

 | 

Optimize

 |
| --- | --- | --- | --- |
| [Overview](/docs/data-cache) | The usage from fetch requests to origins | No | [Learn More](/docs/data-cache) |
| [Reads](/docs/data-cache) | The total amount of Read Units used to access the Data Cache | No | [Learn More](/docs/data-cache) |
| [Writes](/docs/data-cache) | The total amount of Write Units used to store new data in the Data Cache | No | [Learn More](/docs/data-cache) |

## [Incremental Static Regeneration (ISR)](#incremental-static-regeneration-isr)

The table below shows the metrics for the [Incremental Static Regeneration](/docs/pricing/incremental-static-regeneration) section of the Usage dashboard.

To view information on managing each resource, select the resource link in the Metric column. To jump straight to guidance on optimization, select the corresponding resource link in the Optimize column.

Manage and Optimize pricing
| 
Metric

 | 

Description

 | 

Priced

 | 

Optimize

 |
| --- | --- | --- | --- |
| [Reads](/docs/incremental-static-regeneration/limits-and-pricing#isr-reads-chart) | The total amount of Read Units used to access ISR data | [Yes](/docs/pricing/regional-pricing) | [Learn More](/docs/incremental-static-regeneration/limits-and-pricing#optimizing-isr-reads-and-writes) |
| [Writes](/docs/incremental-static-regeneration/limits-and-pricing#isr-writes-chart) | The total amount of Write Units used to store new ISR data | [Yes](/docs/pricing/regional-pricing) | [Learn More](/docs/incremental-static-regeneration/limits-and-pricing#optimizing-isr-reads-and-writes) |

## [Observability](#observability)

The table below shows the metrics for the [Web Analytics](/docs/pricing/observability#managing-web-analytics-events), [Speed Insights](/docs/pricing/observability#managing-speed-insights-data-points), and [Monitoring](/docs/manage-and-optimize-observability#optimizing-monitoring-events) sections of the Usage dashboard.

To view information on managing each resource, select the resource link in the Metric column. To jump straight to guidance on optimization, select the corresponding resource link in the Optimize column.

Manage and Optimize pricing
| 
Metric

 | 

Description

 | 

Priced

 | 

Optimize

 |
| --- | --- | --- | --- |
| [Web Analytics Events](/docs/pricing/observability#managing-web-analytics-events) | The number of page views and custom events tracked across all your projects | [Yes](/docs/pricing#managed-infrastructure-billable-resources) | [Learn More](/docs/manage-and-optimize-observability#optimizing-web-analytics-events) |
| [Speed Insights Data points](/docs/pricing/observability#managing-speed-insights-data-points) | The number of data points reported from browsers for Speed Insights | [Yes](/docs/pricing#managed-infrastructure-billable-resources) | [Learn More](/docs/speed-insights/limits-and-pricing#optimizing-speed-insights-data-points) |
| [Observability Plus Events](/docs/pricing/observability#managing-observability-events) | The number of events collected, based on requests made to your site | [Yes](/docs/pricing#managed-infrastructure-billable-resources) | [Learn More](/docs/manage-and-optimize-observability#optimizing-observability-events) |
| [Monitoring Events](/docs/manage-and-optimize-observability#optimizing-monitoring-events) | The number of requests made to your website | [Yes](/docs/pricing#managed-infrastructure-billable-resources) | [Learn More](/docs/manage-and-optimize-observability#optimizing-monitoring-events) |

## [Image Optimization](#image-optimization)

The table below shows the metrics for the [Image Optimization](/docs/image-optimization/managing-image-optimization-costs) section of the Usage dashboard.

To view information on managing each resource, select the resource link in the Metric column. To jump straight to guidance on optimization, select the corresponding resource link in the Optimize column.

Manage and Optimize pricing
| 
Metric

 | 

Description

 | 

Priced

 | 

Optimize

 |
| --- | --- | --- | --- |
| [Source images](/docs/image-optimization/managing-image-optimization-costs#source-image-optimizations) | The number of images that have been optimized using the Image Optimization feature | [Yes](/docs/pricing#managed-infrastructure-billable-resources) | [Learn More](/docs/image-optimization/managing-image-optimization-costs#how-to-optimize-your-costs) |

## [Viewing Options](#viewing-options)

### [Count](#count)

Count shows the total number of a certain metric, across all projects in your account. This is useful to understand past trends about your usage.

### [Project](#project)

Project shows the total usage of a certain metric, per project. This is useful to understand how different projects are using resources and is useful to help you start understanding the best opportunities for optimizing your usage.

### [Region](#region)

For region-based pricing, you can view the usage of a certain metric, per region. This is useful to understand the requests your site is getting from different regions.

### [Ratio](#ratio)

*   Requests: The ratio of cached vs uncached requests
*   Fast Data Transfer: The ratio of incoming vs outgoing data transfer
*   Fast Origin Transfer: The ratio of incoming vs outgoing data transfer
*   Serverless Functions invocations: Successful vs errored vs timed out invocations
*   Serverless Functions execution: Successful vs errored vs timed out invocations
*   Builds: Completed vs errored builds
*   Remote Cache Artifacts: Uploaded vs downloaded artifacts
*   Remote Cache total size: Uploaded vs downloaded artifacts

### [Average](#average)

This shows the average usage of a certain metric over a 24 hour period.

## [More resources](#more-resources)

For more information on Vercel's pricing, guidance on optimizing consumption, and invoices, see the following resources:

*   [How are resources used on Vercel?](/docs/pricing/how-does-vercel-calculate-usage-of-resources)
*   [Understanding my invoice](/docs/pricing/understanding-my-invoice)

--------------------------------------------------------------------------------
title: "Regional pricing"
description: "Vercel pricing for Managed Infrastructure resources in different regions."
last_updated: "null"
source: "https://vercel.com/docs/pricing/regional-pricing"
--------------------------------------------------------------------------------

# Regional pricing

Copy page

Ask AI about this page

Last updated June 25, 2025

When using Managed Infrastructure resources on Vercel, some, but not all, are priced based on region. The following table shows the price range for resources priced by region. Your team will be charged based on the usage of your projects for each resource per region.

The Included column shows the amount of usage covered in your [billing cycle](/docs/pricing/understanding-my-invoice#understanding-your-invoice). If you use more than this amount, the Additional column lists the rates for any extra usage as a range.

Active CPU and Provisioned Memory are billed at different rates depending on the region your [fluid compute](/docs/fluid-compute) is deployed. The rates for each region can be found in the [fluid pricing](/docs/functions/usage-and-pricing) documentation.

| Resource | Included (Billing Cycle) | On-demand (Billing Cycle) |
| --- | --- | --- |
| [Fast Data Transfer](/docs/edge-network/manage-usage#fast-data-transfer) | First 1 TB | 1 GB for $0.15 - $0.35 |
| [Edge Requests](/docs/edge-network/manage-usage#edge-requests) | First 10,000,000 | 1,000,000 Requests for $2.00 - $3.20 |

| Resource | On-demand (Billing Cycle) |
| --- | --- |
| [ISR Writes](/docs/incremental-static-regeneration/limits-and-pricing#isr-writes-chart) | 1,000,000 Write Units for $4.00 - $6.40 |
| [ISR Reads](/docs/incremental-static-regeneration/limits-and-pricing#isr-reads-chart) | 1,000,000 Read Units for $0.40 - $0.64 |
| [Fast Origin Transfer](/docs/edge-network/manage-usage#fast-origin-transfer) | 1 GB for $0.06 - $0.43 |
| [Edge Request Additional CPU Duration](/docs/edge-network/manage-usage#edge-request-cpu-duration) | 1 Hour for $0.30 - $0.48 |
| [Image Optimization Transformations](/docs/image-optimization/limits-and-pricing#image-transformations) | $0.05 - $0.0812 per 1K |
| [Image Optimization Cache Reads](/docs/image-optimization/limits-and-pricing#image-cache-reads) | $0.40 - $0.64 per 1M |
| [Image Optimization Cache Writes](/docs/image-optimization/limits-and-pricing#image-cache-writes) | $4.00 - $6.40 per 1M |
| [Runtime Cache Writes](/docs/functions/functions-api-reference/vercel-functions-package#getcache) | 1,000,000 Write Units for $4.00 - $6.40 |
| [Runtime Cache Reads](/docs/functions/functions-api-reference/vercel-functions-package#getcache) | 1,000,000 Read Units for $0.40 - $0.64 |
| [WAF Rate Limiting](/docs/security/vercel-waf/usage-and-pricing#rate-limiting-pricing) | 1,000,000 Allowed Requests for $0.50 - $0.80 |
| [OWASP CRS per request number](/docs/security/vercel-waf/usage-and-pricing#managed-ruleset-pricing) | 1,000,000 Inspected Requests for $0.80 - $1.28 |
| [OWASP CRS per request size](/docs/security/vercel-waf/usage-and-pricing#managed-ruleset-pricing) | 1 GB of inspected request payload for $0.20 - $0.32 |
| [Blob Storage Size](/docs/vercel-blob/usage-and-pricing#pricing) | 1 GB for $0.02 - $0.04 |
| [Blob Simple Operations](/docs/vercel-blob/usage-and-pricing#pricing) | 1,000,000 for $0.35 - $0.56 |
| [Blob Advanced Operations](/docs/vercel-blob/usage-and-pricing#pricing) | 1,000,000 for $4.50 - $7.00 |
| [Blob Data Transfer](/docs/vercel-blob/usage-and-pricing#pricing) | 1 GB for $0.05 - $0.12 |
| [Private Data Transfer](/docs/connectivity/static-ips) | 1 GB for $0.15 - $0.31 |

## [Specific region pricing](#specific-region-pricing)

For specific, region based pricing, see the following pages:

*   [Cape Town, South Africa (cpt1)](/docs/pricing/regional-pricing/cpt1)
*   [Cleveland, USA (cle1)](/docs/pricing/regional-pricing/cle1)
*   [Dubai, UAE (dxb1)](/docs/pricing/regional-pricing/dxb1)
*   [Dublin, Ireland (dub1)](/docs/pricing/regional-pricing/dub1)
*   [Frankfurt, Germany (fra1)](/docs/pricing/regional-pricing/fra1)
*   [Hong Kong (hkg1)](/docs/pricing/regional-pricing/hkg1)
*   [London, UK (lhr1)](/docs/pricing/regional-pricing/lhr1)
*   [Mumbai, India (bom1)](/docs/pricing/regional-pricing/bom1)
*   [Osaka, Japan (kix1)](/docs/pricing/regional-pricing/kix1)
*   [Paris, France (cdg1)](/docs/pricing/regional-pricing/cdg1)
*   [Portland, USA (pdx1)](/docs/pricing/regional-pricing/pdx1)
*   [San Francisco, USA (sfo1)](/docs/pricing/regional-pricing/sfo1)
*   [Seoul, South Korea (icn1)](/docs/pricing/regional-pricing/icn1)
*   [Singapore (sin1)](/docs/pricing/regional-pricing/sin1)
*   [Stockholm, Sweden (arn1)](/docs/pricing/regional-pricing/arn1)
*   [Sydney, Australia (syd1)](/docs/pricing/regional-pricing/syd1)
*   [São Paulo, Brazil (gru1)](/docs/pricing/regional-pricing/gru1)
*   [Tokyo, Japan (hnd1)](/docs/pricing/regional-pricing/hnd1)
*   [Washington, D.C. USA (iad1)](/docs/pricing/regional-pricing/iad1)

For more information on Managed Infrastructure pricing, see the [pricing documentation](/docs/pricing#managed-infrastructure).

--------------------------------------------------------------------------------
title: "Stockholm, Sweden (arn1) pricing"
description: "Vercel pricing for the Stockholm, Sweden (arn1) region."
last_updated: "null"
source: "https://vercel.com/docs/pricing/regional-pricing/arn1"
--------------------------------------------------------------------------------

# Stockholm, Sweden (arn1) pricing

Copy page

Ask AI about this page

Last updated September 9, 2025

The table below shows Managed Infrastructure products with pricing specific to the Stockholm, Sweden (arn1) region. This pricing is available only to [Pro plan](/docs/plans/pro) users. Your team will be charged based on the usage of your projects for each resource in this region.

The Included column shows the amount of usage covered in your [billing cycle](/docs/pricing/understanding-my-invoice#understanding-your-invoice). If you use more than this amount, the Additional column lists the rates for any extra usage.

Active CPU and Provisioned Memory are billed at different rates depending on the region your [fluid compute](/docs/fluid-compute) is deployed. The rates for each region can be found in the [fluid pricing](/docs/functions/usage-and-pricing) documentation.

Managed Infrastructure pricing
| 
Resource

 | 

On-demand (Billing Cycle)

 |
| --- | --- |
| 

[Fast Data Transfer](/docs/pricing/regional-pricing)

 | Included 1TB, then $0.15 per 1 GB |
| 

[Fast Origin Transfer](/docs/pricing/regional-pricing)

 | $0.06 per 1 GB |
| 

[Edge Requests](/docs/pricing/regional-pricing)

 | Included 10,000,000, then $2.20 per 1,000,000 Requests |
| 

[ISR Reads](/docs/data-cache)

 | $0.44 per 1,000,000 Read Units |
| 

[ISR Writes](/docs/data-cache)

 | $4.40 per 1,000,000 Write Units |
| 

[Edge Request Additional CPU Duration](/docs/pricing/regional-pricing)

 | $0.33 per 1 Hour |
| 

[Image Optimization Transformations](/docs/image-optimization)

 | $0.054 per 1K |
| 

[Image Optimization Cache Reads](/docs/image-optimization)

 | $0.44 per 1M |
| 

[Image Optimization Cache Writes](/docs/image-optimization)

 | $4.40 per 1M |
| 

[WAF Rate Limiting](/docs/vercel-firewall/vercel-waf/rate-limiting)

 | $0.55 per 1,000,000 Allowed Requests |
| 

[OWASP CRS per request number](/docs/vercel-firewall/vercel-waf/managed-rulesets)

 | $0.88 per 1,000,000 Inspected Requests |
| 

[OWASP CRS per request size](/docs/vercel-firewall/vercel-waf/managed-rulesets)

 | $0.22 per 1 GB of inspected request payload |
| 

[Blob Storage Size](/docs/vercel-blob/usage-and-pricing#pricing)

 | $0.023 per GB |
| 

[Blob Simple Operations](/docs/vercel-blob/usage-and-pricing#pricing)

 | $0.400 per 1M |
| 

[Blob Advanced Operations](/docs/vercel-blob/usage-and-pricing#pricing)

 | $5.000 per 1M |
| 

[Blob Data Transfer](/docs/vercel-blob/usage-and-pricing#pricing)

 | $0.050 per GB |
| 

[Private Data Transfer](/docs/connectivity/static-ips)

 | $0.153 per 1 GB |
| 

[Workflow Storage](/docs/workflow#pricing)

 | $0.55 per 1 GB per month |
| 

[Workflow Steps](/docs/workflow#pricing)

 | $27.50 per 1,000,000 Steps |

Learn more about the different regions available on Vercel in the [regions](/docs/regions) documentation. See the [pricing](/docs/pricing#managed-infrastructure) documentation for more information on Managed Infrastructure.

--------------------------------------------------------------------------------
title: "Mumbai, India (bom1) pricing"
description: "Vercel pricing for the Mumbai, India (bom1) region."
last_updated: "null"
source: "https://vercel.com/docs/pricing/regional-pricing/bom1"
--------------------------------------------------------------------------------

# Mumbai, India (bom1) pricing

Copy page

Ask AI about this page

Last updated September 9, 2025

The table below shows Managed Infrastructure products with pricing specific to the Mumbai, India (bom1) region. This pricing is available only to [Pro plan](/docs/plans/pro) users. Your team will be charged based on the usage of your projects for each resource in this region.

The Included column shows the amount of usage covered in your [billing cycle](/docs/pricing/understanding-my-invoice#understanding-your-invoice). If you use more than this amount, the Additional column lists the rates for any extra usage.

Active CPU and Provisioned Memory are billed at different rates depending on the region your [fluid compute](/docs/fluid-compute) is deployed. The rates for each region can be found in the [fluid pricing](/docs/functions/usage-and-pricing) documentation.

Managed Infrastructure pricing
| 
Resource

 | 

On-demand (Billing Cycle)

 |
| --- | --- |
| 

[Fast Data Transfer](/docs/pricing/regional-pricing)

 | Included 1TB, then $0.20 per 1 GB |
| 

[Fast Origin Transfer](/docs/pricing/regional-pricing)

 | $0.25 per 1 GB |
| 

[Edge Requests](/docs/pricing/regional-pricing)

 | Included 10,000,000, then $2.20 per 1,000,000 Requests |
| 

[ISR Reads](/docs/data-cache)

 | $0.44 per 1,000,000 Read Units |
| 

[ISR Writes](/docs/data-cache)

 | $4.40 per 1,000,000 Write Units |
| 

[Edge Request Additional CPU Duration](/docs/pricing/regional-pricing)

 | $0.33 per 1 Hour |
| 

[Image Optimization Transformations](/docs/image-optimization)

 | $0.0527 per 1K |
| 

[Image Optimization Cache Reads](/docs/image-optimization)

 | $0.44 per 1M |
| 

[Image Optimization Cache Writes](/docs/image-optimization)

 | $4.40 per 1M |
| 

[WAF Rate Limiting](/docs/vercel-firewall/vercel-waf/rate-limiting)

 | $0.55 per 1,000,000 Allowed Requests |
| 

[OWASP CRS per request number](/docs/vercel-firewall/vercel-waf/managed-rulesets)

 | $0.88 per 1,000,000 Inspected Requests |
| 

[OWASP CRS per request size](/docs/vercel-firewall/vercel-waf/managed-rulesets)

 | $0.22 per 1 GB of inspected request payload |
| 

[Blob Storage Size](/docs/vercel-blob/usage-and-pricing#pricing)

 | $0.025 per GB |
| 

[Blob Simple Operations](/docs/vercel-blob/usage-and-pricing#pricing)

 | $0.400 per 1M |
| 

[Blob Advanced Operations](/docs/vercel-blob/usage-and-pricing#pricing)

 | $5.000 per 1M |
| 

[Blob Data Transfer](/docs/vercel-blob/usage-and-pricing#pricing)

 | $0.067 per GB |
| 

[Private Data Transfer](/docs/connectivity/static-ips)

 | $0.187 per 1 GB |
| 

[Workflow Storage](/docs/workflow#pricing)

 | $0.55 per 1 GB per month |
| 

[Workflow Steps](/docs/workflow#pricing)

 | $27.50 per 1,000,000 Steps |

Learn more about the different regions available on Vercel in the [regions](/docs/regions) documentation. See the [pricing](/docs/pricing#managed-infrastructure) documentation for more information on Managed Infrastructure.

--------------------------------------------------------------------------------
title: "Paris, France (cdg1) pricing"
description: "Vercel pricing for the Paris, France (cdg1) region."
last_updated: "null"
source: "https://vercel.com/docs/pricing/regional-pricing/cdg1"
--------------------------------------------------------------------------------

# Paris, France (cdg1) pricing

Copy page

Ask AI about this page

Last updated September 9, 2025

The table below shows Managed Infrastructure products with pricing specific to the Paris, France (cdg1) region. This pricing is available only to [Pro plan](/docs/plans/pro) users. Your team will be charged based on the usage of your projects for each resource in this region.

The Included column shows the amount of usage covered in your [billing cycle](/docs/pricing/understanding-my-invoice#understanding-your-invoice). If you use more than this amount, the Additional column lists the rates for any extra usage.

Active CPU and Provisioned Memory are billed at different rates depending on the region your [fluid compute](/docs/fluid-compute) is deployed. The rates for each region can be found in the [fluid pricing](/docs/functions/usage-and-pricing) documentation.

Managed Infrastructure pricing
| 
Resource

 | 

On-demand (Billing Cycle)

 |
| --- | --- |
| 

[Fast Data Transfer](/docs/pricing/regional-pricing)

 | Included 1TB, then $0.15 per 1 GB |
| 

[Fast Origin Transfer](/docs/pricing/regional-pricing)

 | $0.06 per 1 GB |
| 

[Edge Requests](/docs/pricing/regional-pricing)

 | Included 10,000,000, then $2.40 per 1,000,000 Requests |
| 

[ISR Reads](/docs/data-cache)

 | $0.48 per 1,000,000 Read Units |
| 

[ISR Writes](/docs/data-cache)

 | $4.80 per 1,000,000 Write Units |
| 

[Edge Request Additional CPU Duration](/docs/pricing/regional-pricing)

 | $0.36 per 1 Hour |
| 

[Image Optimization Transformations](/docs/image-optimization)

 | $0.0626 per 1K |
| 

[Image Optimization Cache Reads](/docs/image-optimization)

 | $0.48 per 1M |
| 

[Image Optimization Cache Writes](/docs/image-optimization)

 | $4.80 per 1M |
| 

[WAF Rate Limiting](/docs/vercel-firewall/vercel-waf/rate-limiting)

 | $0.60 per 1,000,000 Allowed Requests |
| 

[OWASP CRS per request number](/docs/vercel-firewall/vercel-waf/managed-rulesets)

 | $0.96 per 1,000,000 Inspected Requests |
| 

[OWASP CRS per request size](/docs/vercel-firewall/vercel-waf/managed-rulesets)

 | $0.24 per 1 GB of inspected request payload |
| 

[Blob Storage Size](/docs/vercel-blob/usage-and-pricing#pricing)

 | $0.024 per GB |
| 

[Blob Simple Operations](/docs/vercel-blob/usage-and-pricing#pricing)

 | $0.420 per 1M |
| 

[Blob Advanced Operations](/docs/vercel-blob/usage-and-pricing#pricing)

 | $5.300 per 1M |
| 

[Blob Data Transfer](/docs/vercel-blob/usage-and-pricing#pricing)

 | $0.050 per GB |
| 

[Private Data Transfer](/docs/connectivity/static-ips)

 | $0.167 per 1 GB |
| 

[Workflow Storage](/docs/workflow#pricing)

 | $0.60 per 1 GB per month |
| 

[Workflow Steps](/docs/workflow#pricing)

 | $30.00 per 1,000,000 Steps |

Learn more about the different regions available on Vercel in the [regions](/docs/regions) documentation. See the [pricing](/docs/pricing#managed-infrastructure) documentation for more information on Managed Infrastructure.

--------------------------------------------------------------------------------
title: "Cleveland, USA (cle1) pricing"
description: "Vercel pricing for the Cleveland, USA (cle1) region."
last_updated: "null"
source: "https://vercel.com/docs/pricing/regional-pricing/cle1"
--------------------------------------------------------------------------------

# Cleveland, USA (cle1) pricing

Copy page

Ask AI about this page

Last updated September 9, 2025

The table below shows Managed Infrastructure products with pricing specific to the Cleveland, USA (cle1) region. This pricing is available only to [Pro plan](/docs/plans/pro) users. Your team will be charged based on the usage of your projects for each resource in this region.

The Included column shows the amount of usage covered in your [billing cycle](/docs/pricing/understanding-my-invoice#understanding-your-invoice). If you use more than this amount, the Additional column lists the rates for any extra usage.

Active CPU and Provisioned Memory are billed at different rates depending on the region your [fluid compute](/docs/fluid-compute) is deployed. The rates for each region can be found in the [fluid pricing](/docs/functions/usage-and-pricing) documentation.

Managed Infrastructure pricing
| 
Resource

 | 

On-demand (Billing Cycle)

 |
| --- | --- |
| 

[Fast Data Transfer](/docs/pricing/regional-pricing)

 | Included 1TB, then $0.15 per 1 GB |
| 

[Fast Origin Transfer](/docs/pricing/regional-pricing)

 | $0.06 per 1 GB |
| 

[Edge Requests](/docs/pricing/regional-pricing)

 | Included 10,000,000, then $2.00 per 1,000,000 Requests |
| 

[ISR Reads](/docs/data-cache)

 | $0.40 per 1,000,000 Read Units |
| 

[ISR Writes](/docs/data-cache)

 | $4.00 per 1,000,000 Write Units |
| 

[Edge Request Additional CPU Duration](/docs/pricing/regional-pricing)

 | $0.30 per 1 Hour |
| 

[Image Optimization Transformations](/docs/image-optimization)

 | $0.05 per 1K |
| 

[Image Optimization Cache Reads](/docs/image-optimization)

 | $0.40 per 1M |
| 

[Image Optimization Cache Writes](/docs/image-optimization)

 | $4.00 per 1M |
| 

[WAF Rate Limiting](/docs/vercel-firewall/vercel-waf/rate-limiting)

 | $0.50 per 1,000,000 Allowed Requests |
| 

[OWASP CRS per request number](/docs/vercel-firewall/vercel-waf/managed-rulesets)

 | $0.80 per 1,000,000 Inspected Requests |
| 

[OWASP CRS per request size](/docs/vercel-firewall/vercel-waf/managed-rulesets)

 | $0.20 per 1 GB of inspected request payload |
| 

[Blob Storage Size](/docs/vercel-blob/usage-and-pricing#pricing)

 | $0.023 per GB |
| 

[Blob Simple Operations](/docs/vercel-blob/usage-and-pricing#pricing)

 | $0.400 per 1M |
| 

[Blob Advanced Operations](/docs/vercel-blob/usage-and-pricing#pricing)

 | $5.000 per 1M |
| 

[Blob Data Transfer](/docs/vercel-blob/usage-and-pricing#pricing)

 | $0.050 per GB |
| 

[Private Data Transfer](/docs/connectivity/static-ips)

 | $0.150 per 1 GB |
| 

[Workflow Storage](/docs/workflow#pricing)

 | $0.50 per 1 GB per month |
| 

[Workflow Steps](/docs/workflow#pricing)

 | $25.00 per 1,000,000 Steps |

Learn more about the different regions available on Vercel in the [regions](/docs/regions) documentation. See the [pricing](/docs/pricing#managed-infrastructure) documentation for more information on Managed Infrastructure.

--------------------------------------------------------------------------------
title: "Cape Town, South Africa (cpt1) pricing"
description: "Vercel pricing for the Cape Town, South Africa (cpt1) region."
last_updated: "null"
source: "https://vercel.com/docs/pricing/regional-pricing/cpt1"
--------------------------------------------------------------------------------

# Cape Town, South Africa (cpt1) pricing

Copy page

Ask AI about this page

Last updated September 9, 2025

The table below shows Managed Infrastructure products with pricing specific to the Cape Town, South Africa (cpt1) region. This pricing is available only to [Pro plan](/docs/plans/pro) users. Your team will be charged based on the usage of your projects for each resource in this region.

The Included column shows the amount of usage covered in your [billing cycle](/docs/pricing/understanding-my-invoice#understanding-your-invoice). If you use more than this amount, the Additional column lists the rates for any extra usage.

Active CPU and Provisioned Memory are billed at different rates depending on the region your [fluid compute](/docs/fluid-compute) is deployed. The rates for each region can be found in the [fluid pricing](/docs/functions/usage-and-pricing) documentation.

Managed Infrastructure pricing
| 
Resource

 | 

On-demand (Billing Cycle)

 |
| --- | --- |
| 

[Fast Data Transfer](/docs/pricing/regional-pricing)

 | Included 1TB, then $0.28 per 1 GB |
| 

[Fast Origin Transfer](/docs/pricing/regional-pricing)

 | $0.43 per 1 GB |
| 

[Edge Requests](/docs/pricing/regional-pricing)

 | Included 10,000,000, then $2.80 per 1,000,000 Requests |
| 

[ISR Reads](/docs/data-cache)

 | $0.56 per 1,000,000 Read Units |
| 

[ISR Writes](/docs/data-cache)

 | $5.60 per 1,000,000 Write Units |
| 

[Edge Request Additional CPU Duration](/docs/pricing/regional-pricing)

 | $0.42 per 1 Hour |
| 

[Image Optimization Transformations](/docs/image-optimization)

 | $0.0735 per 1K |
| 

[Image Optimization Cache Reads](/docs/image-optimization)

 | $0.56 per 1M |
| 

[Image Optimization Cache Writes](/docs/image-optimization)

 | $5.60 per 1M |
| 

[WAF Rate Limiting](/docs/vercel-firewall/vercel-waf/rate-limiting)

 | $0.70 per 1,000,000 Allowed Requests |
| 

[OWASP CRS per request number](/docs/vercel-firewall/vercel-waf/managed-rulesets)

 | $1.12 per 1,000,000 Inspected Requests |
| 

[OWASP CRS per request size](/docs/vercel-firewall/vercel-waf/managed-rulesets)

 | $0.28 per 1 GB of inspected request payload |
| 

[Blob Storage Size](/docs/vercel-blob/usage-and-pricing#pricing)

 | $0.027 per GB |
| 

[Blob Simple Operations](/docs/vercel-blob/usage-and-pricing#pricing)

 | $0.400 per 1M |
| 

[Blob Advanced Operations](/docs/vercel-blob/usage-and-pricing#pricing)

 | $6.000 per 1M |
| 

[Blob Data Transfer](/docs/vercel-blob/usage-and-pricing#pricing)

 | $0.093 per GB |
| 

[Private Data Transfer](/docs/connectivity/static-ips)

 | $0.190 per 1 GB |
| 

[Workflow Storage](/docs/workflow#pricing)

 | $0.70 per 1 GB per month |
| 

[Workflow Steps](/docs/workflow#pricing)

 | $35.00 per 1,000,000 Steps |

Learn more about the different regions available on Vercel in the [regions](/docs/regions) documentation. See the [pricing](/docs/pricing#managed-infrastructure) documentation for more information on Managed Infrastructure.

--------------------------------------------------------------------------------
title: "Dublin, Ireland (dub1) pricing"
description: "Vercel pricing for the Dublin, Ireland (dub1) region."
last_updated: "null"
source: "https://vercel.com/docs/pricing/regional-pricing/dub1"
--------------------------------------------------------------------------------

# Dublin, Ireland (dub1) pricing

Copy page

Ask AI about this page

Last updated September 9, 2025

The table below shows Managed Infrastructure products with pricing specific to the Dublin, Ireland (dub1) region. This pricing is available only to [Pro plan](/docs/plans/pro) users. Your team will be charged based on the usage of your projects for each resource in this region.

The Included column shows the amount of usage covered in your [billing cycle](/docs/pricing/understanding-my-invoice#understanding-your-invoice). If you use more than this amount, the Additional column lists the rates for any extra usage.

Active CPU and Provisioned Memory are billed at different rates depending on the region your [fluid compute](/docs/fluid-compute) is deployed. The rates for each region can be found in the [fluid pricing](/docs/functions/usage-and-pricing) documentation.

Managed Infrastructure pricing
| 
Resource

 | 

On-demand (Billing Cycle)

 |
| --- | --- |
| 

[Fast Data Transfer](/docs/pricing/regional-pricing)

 | Included 1TB, then $0.15 per 1 GB |
| 

[Fast Origin Transfer](/docs/pricing/regional-pricing)

 | $0.06 per 1 GB |
| 

[Edge Requests](/docs/pricing/regional-pricing)

 | Included 10,000,000, then $2.40 per 1,000,000 Requests |
| 

[ISR Reads](/docs/data-cache)

 | $0.48 per 1,000,000 Read Units |
| 

[ISR Writes](/docs/data-cache)

 | $4.80 per 1,000,000 Write Units |
| 

[Edge Request Additional CPU Duration](/docs/pricing/regional-pricing)

 | $0.36 per 1 Hour |
| 

[Image Optimization Transformations](/docs/image-optimization)

 | $0.0567 per 1K |
| 

[Image Optimization Cache Reads](/docs/image-optimization)

 | $0.48 per 1M |
| 

[Image Optimization Cache Writes](/docs/image-optimization)

 | $4.80 per 1M |
| 

[WAF Rate Limiting](/docs/vercel-firewall/vercel-waf/rate-limiting)

 | $0.60 per 1,000,000 Allowed Requests |
| 

[OWASP CRS per request number](/docs/vercel-firewall/vercel-waf/managed-rulesets)

 | $0.96 per 1,000,000 Inspected Requests |
| 

[OWASP CRS per request size](/docs/vercel-firewall/vercel-waf/managed-rulesets)

 | $0.24 per 1 GB of inspected request payload |
| 

[Blob Storage Size](/docs/vercel-blob/usage-and-pricing#pricing)

 | $0.023 per GB |
| 

[Blob Simple Operations](/docs/vercel-blob/usage-and-pricing#pricing)

 | $0.400 per 1M |
| 

[Blob Advanced Operations](/docs/vercel-blob/usage-and-pricing#pricing)

 | $5.000 per 1M |
| 

[Blob Data Transfer](/docs/vercel-blob/usage-and-pricing#pricing)

 | $0.050 per GB |
| 

[Private Data Transfer](/docs/connectivity/static-ips)

 | $0.160 per 1 GB |
| 

[Workflow Storage](/docs/workflow#pricing)

 | $0.60 per 1 GB per month |
| 

[Workflow Steps](/docs/workflow#pricing)

 | $30.00 per 1,000,000 Steps |

Learn more about the different regions available on Vercel in the [regions](/docs/regions) documentation. See the [pricing](/docs/pricing#managed-infrastructure) documentation for more information on Managed Infrastructure.

--------------------------------------------------------------------------------
title: "Dubai, United Arab Emirates (dxb1) pricing"
description: "Vercel pricing for the Dubai, UAE (dxb1) region."
last_updated: "null"
source: "https://vercel.com/docs/pricing/regional-pricing/dxb1"
--------------------------------------------------------------------------------

# Dubai, United Arab Emirates (dxb1) pricing

Copy page

Ask AI about this page

Last updated September 9, 2025

The table below shows Managed Infrastructure products with pricing specific to the Dubai, UAE (dxb1) region. This pricing is available only to [Pro plan](/docs/plans/pro) users. Your team will be charged based on the usage of your projects for each resource in this region.

The Included column shows the amount of usage covered in your [billing cycle](/docs/pricing/understanding-my-invoice#understanding-your-invoice). If you use more than this amount, the Additional column lists the rates for any extra usage.

Managed Infrastructure pricing
| 
Resource

 | 

On-demand (Billing Cycle)

 |
| --- | --- |
| 

[Fast Data Transfer](/docs/pricing/regional-pricing)

 | Included 1TB, then $0.20 per 1 GB |
| 

[Fast Origin Transfer](/docs/pricing/regional-pricing)

 | $0.30 per 1 GB |
| 

[Edge Requests](/docs/pricing/regional-pricing)

 | Included 10,000,000, then $2.20 per 1,000,000 Requests |
| 

[ISR Reads](/docs/data-cache)

 | $0.44 per 1,000,000 Read Units |
| 

[ISR Writes](/docs/data-cache)

 | $4.40 per 1,000,000 Write Units |
| 

[Edge Request Additional CPU Duration](/docs/pricing/regional-pricing)

 | $0.33 per 1 Hour |
| 

[Image Optimization Transformations](/docs/image-optimization)

 | $0.0527 per 1K |
| 

[Image Optimization Cache Reads](/docs/image-optimization)

 | $0.44 per 1M |
| 

[Image Optimization Cache Writes](/docs/image-optimization)

 | $4.40 per 1M |
| 

[WAF Rate Limiting](/docs/vercel-firewall/vercel-waf/rate-limiting)

 | $0.55 per 1,000,000 Allowed Requests |
| 

[OWASP CRS per request number](/docs/vercel-firewall/vercel-waf/managed-rulesets)

 | $0.88 per 1,000,000 Inspected Requests |
| 

[OWASP CRS per request size](/docs/vercel-firewall/vercel-waf/managed-rulesets)

 | $0.22 per 1 GB of inspected request payload |
| 

[Blob Storage Size](/docs/vercel-blob/usage-and-pricing#pricing)

 | $0.025 per GB |
| 

[Blob Simple Operations](/docs/vercel-blob/usage-and-pricing#pricing)

 | $0.440 per 1M |
| 

[Blob Advanced Operations](/docs/vercel-blob/usage-and-pricing#pricing)

 | $5.500 per 1M |
| 

[Blob Data Transfer](/docs/vercel-blob/usage-and-pricing#pricing)

 | $0.110 per GB |
| 

[Private Data Transfer](/docs/connectivity/static-ips)

 | $0.187 per 1 GB |
| 

[Workflow Storage](/docs/workflow#pricing)

 | $0.55 per 1 GB per month |
| 

[Workflow Steps](/docs/workflow#pricing)

 | $27.50 per 1,000,000 Steps |

Learn more about the different regions available on Vercel in the [regions](/docs/regions) documentation. See the [pricing](/docs/pricing#managed-infrastructure) documentation for more information on Managed Infrastructure.

--------------------------------------------------------------------------------
title: "Frankfurt, Germany (fra1) pricing"
description: "Vercel pricing for the Frankfurt, Germany (fra1) region."
last_updated: "null"
source: "https://vercel.com/docs/pricing/regional-pricing/fra1"
--------------------------------------------------------------------------------

# Frankfurt, Germany (fra1) pricing

Copy page

Ask AI about this page

Last updated September 9, 2025

The table below shows Managed Infrastructure products with pricing specific to the Frankfurt, Germany (fra1) region. This pricing is available only to [Pro plan](/docs/plans/pro) users. Your team will be charged based on the usage of your projects for each resource in this region.

The Included column shows the amount of usage covered in your [billing cycle](/docs/pricing/understanding-my-invoice#understanding-your-invoice). If you use more than this amount, the Additional column lists the rates for any extra usage.

Active CPU and Provisioned Memory are billed at different rates depending on the region your [fluid compute](/docs/fluid-compute) is deployed. The rates for each region can be found in the [fluid pricing](/docs/functions/usage-and-pricing) documentation.

Managed Infrastructure pricing
| 
Resource

 | 

On-demand (Billing Cycle)

 |
| --- | --- |
| 

[Fast Data Transfer](/docs/pricing/regional-pricing)

 | Included 1TB, then $0.15 per 1 GB |
| 

[Fast Origin Transfer](/docs/pricing/regional-pricing)

 | $0.06 per 1 GB |
| 

[Edge Requests](/docs/pricing/regional-pricing)

 | Included 10,000,000, then $2.60 per 1,000,000 Requests |
| 

[ISR Reads](/docs/data-cache)

 | $0.52 per 1,000,000 Read Units |
| 

[ISR Writes](/docs/data-cache)

 | $5.20 per 1,000,000 Write Units |
| 

[Edge Request Additional CPU Duration](/docs/pricing/regional-pricing)

 | $0.39 per 1 Hour |
| 

[Image Optimization Transformations](/docs/image-optimization)

 | $0.0601 per 1K |
| 

[Image Optimization Cache Reads](/docs/image-optimization)

 | $0.52 per 1M |
| 

[Image Optimization Cache Writes](/docs/image-optimization)

 | $5.20 per 1M |
| 

[WAF Rate Limiting](/docs/vercel-firewall/vercel-waf/rate-limiting)

 | $0.65 per 1,000,000 Allowed Requests |
| 

[OWASP CRS per request number](/docs/vercel-firewall/vercel-waf/managed-rulesets)

 | $1.04 per 1,000,000 Inspected Requests |
| 

[OWASP CRS per request size](/docs/vercel-firewall/vercel-waf/managed-rulesets)

 | $0.26 per 1 GB of inspected request payload |
| 

[Blob Storage Size](/docs/vercel-blob/usage-and-pricing#pricing)

 | $0.025 per GB |
| 

[Blob Simple Operations](/docs/vercel-blob/usage-and-pricing#pricing)

 | $0.430 per 1M |
| 

[Blob Advanced Operations](/docs/vercel-blob/usage-and-pricing#pricing)

 | $5.400 per 1M |
| 

[Blob Data Transfer](/docs/vercel-blob/usage-and-pricing#pricing)

 | $0.050 per GB |
| 

[Private Data Transfer](/docs/connectivity/static-ips)

 | $0.173 per 1 GB |
| 

[Workflow Storage](/docs/workflow#pricing)

 | $0.65 per 1 GB per month |
| 

[Workflow Steps](/docs/workflow#pricing)

 | $32.50 per 1,000,000 Steps |

Learn more about the different regions available on Vercel in the [regions](/docs/regions) documentation. See the [pricing](/docs/pricing#managed-infrastructure) documentation for more information on Managed Infrastructure.

--------------------------------------------------------------------------------
title: "São Paulo, Brazil (gru1) pricing"
description: "Vercel pricing for the São Paulo, Brazil (gru1) region."
last_updated: "null"
source: "https://vercel.com/docs/pricing/regional-pricing/gru1"
--------------------------------------------------------------------------------


---

**Navigation:** [← Previous](./14-limits.md) | [Index](./index.md) | [Next →](./16-são-paulo-brazil-gru1-pricing.md)
