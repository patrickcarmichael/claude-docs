**Navigation:** [← Previous](./38-creates-a-webhook.md) | [Index](./index.md) | [Next →](./40-waf-custom-rules.md)

---

# Session tracing

Copy page

Ask AI about this page

Last updated October 30, 2025

Session tracing provides insights into your application's interaction with Vercel infrastructure, including routing, middleware, caching, and function startup, helping you:

*   Understand routing, middleware, caching, and function startup.
*   Inspect user-instrumented spans without external tracing tools.
*   Identify performance bottlenecks in your application.
*   View Vercel infrastructure spans alongside your application spans.

## [Anatomy of a trace](#anatomy-of-a-trace)

Each trace displays:

*   Vercel infrastructure spans in black and white with a triangle icon.
*   If you have instrumented your application with [OpenTelemetry](/docs/otel), user spans will be displayed in color. Next.js 13.4+ contributes top-level spans for routes and rendering tasks.
*   Fetch spans

To view details of a span, click on the span in the trace. The sidebar will display the span's details. For infrastructure spans, a "what is this?" explanation will be provided.

To view trace spans in more detail, click and drag to zoom in on a specific area of the trace. You can also use the zoom controls in the bottom right corner of the trace.

## [Prerequisites](#prerequisites)

*   A Vercel account. If you don't have one, you can [sign up for free](https://vercel.com/signup).
*   A Vercel project. If you don't have one, you can [create a new project](https://vercel.com/new).
*   [The toolbar enabled](/docs/vercel-toolbar/in-production-and-localhost) in your preview or production environment.

## [Run a page trace](#run-a-page-trace)

1.  In the Vercel toolbar on your deployment, click (or search for) Tracing.
2.  Select Run Page Trace.
3.  The page will reload, and a toast will indicate the status of the trace. Once the trace has propagated, the toast will indicate that the trace is complete and ready to view.
4.  Click the toast to view the trace in a new browser tab under the Logs tab of the dashboard.

## [View previous session traces](#view-previous-session-traces)

1.  In the Vercel toolbar on your deployment, click (or search for) Tracing.
2.  Select View Previous Session Traces.
3.  The dashboard will open to the Logs tab, filtered to the session ID, and the tracing filter applied - indicated by the lightning icon in the filter bar.

You can filter traces using [all the same filters available](/docs/runtime-logs#log-filters) in the Logs tab of the dashboard. To view traces for requests to your browser, press the user icon next to the lightning icon in the filter bar.

![View previous session traces in the dashboard.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fobservability%2Fprevious-session-traces-light.png%3Flightbox&w=3840&q=75)![View previous session traces in the dashboard.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fobservability%2Fprevious-session-traces-dark.png%3Flightbox&w=3840&q=75)

View previous session traces in the dashboard.

Zoom Image

![View previous session traces in the dashboard.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fobservability%2Fprevious-session-traces-light.png%3Flightbox&w=3840&q=75)![View previous session traces in the dashboard.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fobservability%2Fprevious-session-traces-dark.png%3Flightbox&w=3840&q=75)

View previous session traces in the dashboard.

## [Viewing trace spans within the Logs tab](#viewing-trace-spans-within-the-logs-tab)

With the tracing filter applied, you can view traces in the Logs tab of the dashboard.

Select a request from the list and click the Trace button at the bottom of the request details panel. This will open the traces for that request in an accordion and has the same functionality as viewing traces on the full page.

![View traces in the logs tab.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fobservability%2Ftrace-panel-2-light.png%3Flightbox&w=3840&q=75)![View traces in the logs tab.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fobservability%2Ftrace-panel-2-dark.png%3Flightbox&w=3840&q=75)

View traces in the logs tab.

Zoom Image

![View traces in the logs tab.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fobservability%2Ftrace-panel-2-light.png%3Flightbox&w=3840&q=75)![View traces in the logs tab.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fobservability%2Ftrace-panel-2-dark.png%3Flightbox&w=3840&q=75)

View traces in the logs tab.

## [Tracing sessions](#tracing-sessions)

1.  In the Vercel toolbar on your deployment, click (or search for) Tracing.
2.  Select Start Tracing Session.

Once enabled, the page reloads, and the toolbar turns blue, indicating the session trace is active.

You can then select any of the following options:

*   View Page Trace: View the trace for the current page.
*   View Session Traces: View all traced requests from your active session.
*   Stop Tracing Session: Stop tracing the current session.
*   Restart Tracing Session: Restart tracing the current session.

![View session trace options in the toolbar.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fobservability%2Fsession-trace-options-light.png&w=1920&q=75)![View session trace options in the toolbar.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fobservability%2Fsession-trace-options-dark.png&w=1920&q=75)

View session trace options in the toolbar.

Selecting View Page Trace will open the trace for the current page in a new tab. This is the same as running a page trace.

While selecting View Session Traces will open the dashboard to the Logs tab, filtered to the session ID, and the tracing filter applied - indicated by the lightning icon in the filter bar.

## [Adding custom spans](#adding-custom-spans)

To add custom spans to your traces, you can use the `@opentelemetry/api` package. This allows you to instrument your code and capture additional spans that are relevant to your application.

custom-span.ts

```
import { trace } from '@opentelemetry/api';
 
const tracer = trace.getTracer('custom-tracer');
 
async function performOperation() {
  const span = tracer.startSpan('operation-name');
  try {
    // Your operation logic here
    span.setAttributes({
      'custom.attribute': 'value',
    });
  } finally {
    span.end();
  }
}
```

See the [OpenTelemetry documentation](/docs/otel) steps [three](/docs/otel#initialize-otel) and [four](/docs/otel#start-tracing-requests-in-your-project) for more details on how to use the `@opentelemetry/api` package.

## [Usage and pricing](#usage-and-pricing)

Tracing is available on all plans with a limit up to 1 million spans per month, per team.

| Plan | Monthly Span Limit per Team |
| --- | --- |
| Hobby | 1 million |
| Pro | 1 million |
| Enterprise | 1 million |

## [Limitations](#limitations)

Custom spans from functions using the [Edge runtime](/docs/functions/runtimes/edge) are not supported.

## [More resources](#more-resources)

*   [Learn about the Vercel toolbar](/docs/vercel-toolbar)
*   [Explore Observability on Vercel](/docs/observability)
*   [Learn about the Vercel OpenTelemetry integration](/docs/otel)

--------------------------------------------------------------------------------
title: "Skew Protection"
description: "Learn how Vercel's Skew Protection ensures that the client and server stay in sync for any particular deployment."
last_updated: "null"
source: "https://vercel.com/docs/skew-protection"
--------------------------------------------------------------------------------

# Skew Protection

Copy page

Ask AI about this page

Last updated October 28, 2025

Skew Protection is available on [Enterprise](/docs/plans/enterprise) and [Pro](/docs/plans/pro) plans

Those with the [owner, admin, member](/docs/rbac/access-roles#owner, admin, member-role) role can access this feature

[Version skew](https://www.industrialempathy.com/posts/version-skew/) occurs when different versions of your application run on client and server, causing application errors and other unexpected behavior. For example, imagine your newest deployment modifies the data structure by adding a required field to a user's profile. Older clients wouldn't expect this new field, leading to errors when they submit it.

Vercel's Skew Protection resolves this problem at the platform and framework layer by using [version locking](https://www.industrialempathy.com/posts/version-skew/#version-locking), which ensures client and server use the exact same version. In our example, outdated clients continue to communicate with servers that understand the old data structure, while updated clients use the most recent deployment.

![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fdeployments-basics%2Fnested-layouts-light.png&w=3840&q=75)![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fdeployments-basics%2Fnested-layouts-dark.png&w=3840&q=75)

By implementing Skew Protection, you can reduce user-facing errors during new rollouts and boost developer productivity, minimizing concerns about API compatibility across versions.

## [Enable Skew Protection](#enable-skew-protection)

Projects created after November 19th 2024 using one of the [supported frameworks](#supported-frameworks) already have Skew Protection enabled by default.

For older projects, you can enable Skew Protection in your project's settings.

1.  Ensure your project has the [Automatically expose system environment variables](/docs/environment-variables/system-environment-variables#automatically-expose-system-environment-variables) setting enabled
2.  Ensure your deployment method is not using the `vercel deploy --prebuilt` option. To learn more, see [When not to use --prebuilt](/docs/cli/deploy#when-not-to-use---prebuilt)
3.  Select the project in the Vercel dashboard
4.  Select the Settings tab in the top menu
5.  Select the Advanced tab in the side menu
6.  Scroll down to Skew Protection and enable the switch
7.  You can optionally set a custom maximum age (see [limitations](#limitations))
8.  [Redeploy](/docs/deployments/managing-deployments#redeploy-a-project) your latest production deployment.

![A screenshot of the Skew Protection section containing an enabled/disabled toggle switch.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fprojects%2Fskew-protection-light.jpg&w=1920&q=75)![A screenshot of the Skew Protection section containing an enabled/disabled toggle switch.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fprojects%2Fskew-protection-dark.jpg&w=1920&q=75)

A screenshot of the Skew Protection section containing an enabled/disabled toggle switch.

## [Custom Skew Protection Threshold](#custom-skew-protection-threshold)

In some cases, you may have problematic deployments you want to ensure no longer resolves requests from any other active clients.

Once you deploy a fix, you can set a Skew Protection threshold with the following:

1.  Select the deployment that fixed the problem in the deployment list
2.  Select the button (near the Visit button)
3.  Click Skew Protection Threshold
4.  Click Set to apply the changes

This ensure that deployments created before the fixed deployment will no longer resolve requests from outdated clients.

![A screenshot of the popover menu containing a menu item for Skew Protection Threshold.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fskew-protection%2Fconfigure-skew-protection-light.png&w=640&q=75)![A screenshot of the popover menu containing a menu item for Skew Protection Threshold.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fskew-protection%2Fconfigure-skew-protection-dark.png&w=640&q=75)

A screenshot of the popover menu containing a menu item for Skew Protection Threshold.

## [Monitor Skew Protection](#monitor-skew-protection)

You can observe how many requests are protected from version skew by visiting the [Monitoring](/docs/observability/monitoring) page in the Vercel dashboard.

For example, on the `requests` event, filter where `skew_protection = 'active'`.

You can view Edge Requests that are successfully fulfilled without the need for skew protection by using `skew_protection = 'inactive'`.

![A screenshot of a query of requests filtered by active skew protection.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fprojects%2Fskew-protection-monitoring-query-light-colinUpdate.png&w=1920&q=75)![A screenshot of a query of requests filtered by active skew protection.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fprojects%2Fskew-protection-monitoring-query-dark-colinUpdate.png&w=1920&q=75)

A screenshot of a query of requests filtered by active skew protection.

## [Supported frameworks](#supported-frameworks)

Skew Protection is available with zero configuration when using the following frameworks:

*   [Next.js](#skew-protection-with-next.js)
*   [SvelteKit](#skew-protection-with-sveltekit)
*   [Qwik](#skew-protection-with-qwik)
*   [Astro](#skew-protection-with-astro)
*   Nuxt ([coming soon](https://github.com/nitrojs/nitro/issues/2311))

Other frameworks can implement Skew Protection by checking if `VERCEL_SKEW_PROTECTION_ENABLED` has value `1` and then appending the value of `VERCEL_DEPLOYMENT_ID` to each request using one of the following options.

*   `dpl` query string parameter:
    
    option1.ts
    
    ```
    const query =
      process.env.VERCEL_SKEW_PROTECTION_ENABLED === '1'
        ? `?dpl=${process.env.VERCEL_DEPLOYMENT_ID}`
        : '';
     
    const res = await fetch(`/get${query}`);
    ```
    
*   `x-deployment-id` header:
    
    option2.ts
    
    ```
    const headers =
      process.env.VERCEL_SKEW_PROTECTION_ENABLED === '1'
        ? { 'x-deployment-id': process.env.VERCEL_DEPLOYMENT_ID }
        : {};
     
    const res = await fetch('/get', { headers });
    ```
    
*   `__vdpl` cookie:
    
    option3.ts
    
    ```
    export default function handler(req, res) {
      if (
        process.env.VERCEL_SKEW_PROTECTION_ENABLED === '1' &&
        req.headers['sec-fetch-dest'] === 'document'
      ) {
        res.setHeader('Set-Cookie', [
          `__vdpl=${process.env.VERCEL_DEPLOYMENT_ID}; HttpOnly`,
        ]);
      }
      res.end('<h1>Hello World</h1>');
    }
    ```
    

## [Skew Protection with Next.js](#skew-protection-with-next.js)

If you're building outside of Vercel and then deploying using the `vercel deploy --prebuilt` command, Skew Protection will not be enabled because the Deployment ID was not known at build time. For more information, see [When not to use --prebuilt](/docs/cli/deploy#when-not-to-use---prebuilt).

If you are using Next.js 14.1.4 or newer, there is no additional configuration needed to [enable Skew Protection](#enable-skew-protection).

Older versions of Next.js require additional [`next.config.js`](https://nextjs.org/docs/app/api-reference/next-config-js) configuration.

**View config for 13.4.7 to 14.1.3**  

next.config.js

```
/** @type {import('next').NextConfig} */
const nextConfig = {
  experimental: {
    useDeploymentId: true,
    // Optionally, use with Server Actions
    useDeploymentIdServerActions: true,
  },
};
 
module.exports = nextConfig;
```

The `useDeploymentId` configuration enables Skew Protection for all framework-managed static file requests from your Next.js app such as for JavaScript and CSS files. You can also opt-into Skew Protection for [Next.js Server Actions](https://nextjs.org/docs/app/building-your-application/data-fetching/server-actions-and-mutations) with `useDeploymentIdServerActions`.

## [Skew Protection with SvelteKit](#skew-protection-with-sveltekit)

If you are using SvelteKit, you will need to install `@sveltejs/adapter-vercel` version 5.2.0 or newer in order to [enable Skew Protection](#enable-skew-protection).

Older versions can be upgraded by running `npm i -D @sveltejs/adapter-vercel@latest`.

## [Skew Protection with Qwik](#skew-protection-with-qwik)

If you are using Qwik 1.5.3 or newer, there is no additional configuration needed to [enable Skew Protection](#enable-skew-protection).

Older versions can be upgraded by running `npm i @builder.io/qwik@latest`.

## [Skew Protection with Astro](#skew-protection-with-astro)

If you are using Astro, you will need to install `@astrojs/vercel` version 9.0.0 or newer in order to [enable Skew Protection](#enable-skew-protection).

astro.config.mjs

```
import { defineConfig } from 'astro/config';
import vercel from '@astrojs/vercel';
 
export default defineConfig({
  // ...
  output: 'server',
  adapter: vercel({
    skewProtection: true,
  }),
});
```

Older versions can be upgraded by running `npm i -D @astrojs/vercel@latest`.

## [Limitations](#limitations)

Skew Protection is only available for Pro and Enterprise, not for Hobby teams. You can configure a custom maximum age up to your less than your project's [retention policy](/docs/deployment-retention).

Vercel automatically adjusts the maximum age to 60 days for requests from Googlebot and Bingbot in order to handle any delay between document crawl and render.

Deployments that have been deleted either manually or automatically using a [retention policy](/docs/deployment-retention) will not be accessible through Skew Protection.

## [More resources](#more-resources)

*   [Version Skew Protection blog](/blog/version-skew-protection)
*   [Version Skew](https://www.industrialempathy.com/posts/version-skew/)

--------------------------------------------------------------------------------
title: "Speed Insights Overview"
description: "This page lists out and explains all the performance metrics provided by Vercel's Speed Insights feature."
last_updated: "null"
source: "https://vercel.com/docs/speed-insights"
--------------------------------------------------------------------------------

# Speed Insights Overview

Copy page

Ask AI about this page

Last updated September 24, 2025

Speed Insights is available on [all plans](/docs/plans)

Vercel Speed Insights provides you with a detailed view of your website's performance [metrics](/docs/speed-insights/metrics), based on [Core Web Vitals](/docs/speed-insights/metrics#core-web-vitals-explained), enabling you to make data-driven decisions for optimizing your site. For granular visitor data, use [Web Analytics](/docs/analytics).

The Speed Insights dashboard offers in-depth information about scores and individual metrics without the need for code modifications or leaving the Vercel dashboard.

To get started, follow the quickstart to [enable Speed Insights](/docs/speed-insights/quickstart) and learn more about the [dashboard view](/docs/speed-insights#dashboard-view) and [metrics](/docs/speed-insights/metrics).

When you enable Speed Insights, data will be tracked on all deployed environments, including [preview](/docs/deployments/environments#preview-environment-pre-production) and [production](/docs/deployments/environments#production-environment) deployments.

## [Dashboard view](#dashboard-view)

![A snapshot of the Speed Insights tab from the project view.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fspeed-insights%2Fv2%2Fres-chart-light.png&w=3840&q=75)![A snapshot of the Speed Insights tab from the project view.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fspeed-insights%2Fv2%2Fres-chart-dark.png&w=3840&q=75)

A snapshot of the Speed Insights tab from the project view.

Once you [enable Speed Insights](/docs/speed-insights/quickstart), you can access the dashboard by selecting your project in the Vercel [dashboard](/dashboard), and clicking the Speed Insights tab.

The Speed Insights dashboard displays data that you can sort and inspect based on a variety of parameters:

*   Device type: Toggle between mobile and desktop.
*   Environment: Filter by preview, production, or all environments.
*   Time range: Select the timeframe dropdown in the top-right of the page to choose a predefined timeframe. Alternatively, select the Calendar icon to specify a custom timeframe. The [available durations vary](/docs/speed-insights/limits-and-pricing#reporting-window-for-data-points), depending on the account type.
*   [Performance metric](/docs/speed-insights/metrics): Switch between parameters that include Real Experience Score (RES), First Contentful Paint (FCP) and Largest Contentful Paint (LCP), and use the views to view more information.
*   Performance metric views: When you select a performance metric, the dashboard displays three views:
    *   Time-based line graph that, by default, shows the P75 [percentile of data](/docs/speed-insights/metrics#how-the-percentages-are-calculated) for the selected metric [data points](/docs/speed-insights/metrics#understanding-data-points) and time range. You can include P90, P95 and P99 in this view.
    *   Kanban board that shows which routes, paths, or HTML elements need improvement (URLs that make up less than 0.5% of visits are not shown by default).
    *   Geographical map showing the experience metric by country:
        
        ![Geographic map of the P75 score where the color intensity indicates the relative amount of data points per country](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fspeed-insights%2Fv2%2Fcountry-map-light.png&w=3840&q=75)![Geographic map of the P75 score where the color intensity indicates the relative amount of data points per country](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fspeed-insights%2Fv2%2Fcountry-map-dark.png&w=3840&q=75)
        
        Geographic map of the P75 score where the color intensity indicates the relative amount of data points per country
        

The data in the Kanban and map views is selectable so that you can filter by country, route, path and HTML element. The red, orange and green colors in the map view indicate the P75 score.

*   [Quickstart](/docs/speed-insights/quickstart)
*   [Usage and pricing](/docs/speed-insights/limits-and-pricing#pricing)
*   [Data points](/docs/speed-insights/metrics#understanding-data-points)
*   [Metrics](/docs/speed-insights/metrics)

## [More resources](#more-resources)

*   [How Core Web Vitals affect SEO: Understand your application's Google page experience ranking and Lighthouse scores](https://www.youtube.com/watch?v=qIyEwOEKnE0)

--------------------------------------------------------------------------------
title: "Speed Insights Intake API"
description: "Learn how to use Speed Insights in Vercel with any frontend framework or project through the Speed Insights intake API."
last_updated: "null"
source: "https://vercel.com/docs/speed-insights/api"
--------------------------------------------------------------------------------

# Speed Insights Intake API

Copy page

Ask AI about this page

Last updated September 24, 2025

This API is deprecated. Use the [@vercel/speed-insights](/docs/speed-insights/package) framework agnostic package instead.

Vercel Speed Insights supports Next.js, Nuxt, and Gatsby with zero configuration through build plugins. You can use Speed Insights with any frontend framework or project through the Speed Insights API as shown below.

#### POST /v1/vitals

Send web vitals data to the Vercel Speed Insights API.

Show More

## [Getting Started](#getting-started)

To use the Speed Insights API, you'll need to retrieve the analytics ID for your Vercel project. This value is exposed during the build and can be accessed by `process.env.VERCEL_ANALYTICS_ID` inside Node.js.

Inside your framework or Node.js script, you can then use this value in the `body` of your request to the Vercel Speed Insights API.

`vercel pull` does not pull `VERCEL_ANALYTICS_ID` as the Vercel Analytics ID environment variable is inlined during the build process. It is not part of your project Environment Variables, which can be pulled locally using Vercel CLI.

## [Example](#example)

You can view an example of the following code implemented inside our [Create React App](https://github.com/vercel/vercel/tree/main/examples/create-react-app) and [SvelteKit](https://github.com/vercel/vercel/tree/main/examples/sveltekit) starters.

vitals.js

```
import { getCLS, getFCP, getFID, getLCP, getTTFB } from 'web-vitals';
 
const vitalsUrl = 'https://vitals.vercel-analytics.com/v1/vitals';
 
function getConnectionSpeed() {
  return 'connection' in navigator &&
    navigator['connection'] &&
    'effectiveType' in navigator['connection']
    ? navigator['connection']['effectiveType']
    : '';
}
 
function sendToAnalytics(metric, options) {
  const page = Object.entries(options.params).reduce(
    (acc, [key, value]) => acc.replace(value, `[${key}]`),
    options.path,
  );
 
  const body = {
    dsn: options.analyticsId, // qPgJqYH9LQX5o31Ormk8iWhCxZO
    id: metric.id, // v2-1653884975443-1839479248192
    page, // /blog/[slug]
    href: location.href, // https://{my-example-app-name-here}/blog/my-test
    event_name: metric.name, // TTFB
    value: metric.value.toString(), // 60.20000000298023
    speed: getConnectionSpeed(), // 4g
  };
 
  if (options.debug) {
    console.log('[Analytics]', metric.name, JSON.stringify(body, null, 2));
  }
 
  const blob = new Blob([new URLSearchParams(body).toString()], {
    // This content type is necessary for `sendBeacon`
    type: 'application/x-www-form-urlencoded',
  });
  if (navigator.sendBeacon) {
    navigator.sendBeacon(vitalsUrl, blob);
  } else
    fetch(vitalsUrl, {
      body: blob,
      method: 'POST',
      credentials: 'omit',
      keepalive: true,
    });
}
 
export function webVitals(options) {
  try {
    getFID((metric) => sendToAnalytics(metric, options));
    getTTFB((metric) => sendToAnalytics(metric, options));
    getLCP((metric) => sendToAnalytics(metric, options));
    getCLS((metric) => sendToAnalytics(metric, options));
    getFCP((metric) => sendToAnalytics(metric, options));
  } catch (err) {
    console.error('[Analytics]', err);
  }
}
```

--------------------------------------------------------------------------------
title: "Limits and Pricing for Speed Insights"
description: "Learn about our limits and pricing when using Vercel Speed Insights. Different limitations are applied depending on your plan."
last_updated: "null"
source: "https://vercel.com/docs/speed-insights/limits-and-pricing"
--------------------------------------------------------------------------------

# Limits and Pricing for Speed Insights

Copy page

Ask AI about this page

Last updated September 26, 2025

Speed Insights is available on [all plans](/docs/plans)

## [Pricing](#pricing)

Speed Insights is available on the Hobby, Pro, and Enterprise plans.

On the Hobby plan, Speed Insights is free and can be enabled on one project with a [set allotment](/docs/speed-insights/limits-and-pricing#limitations) of data points.

On the Pro plan, the base fee for Speed Insights is $10 per-project, per-month.

The following table outlines the price for each resource according to the plan you are on.

Managed Infrastructure hobby and pro resources
| 
Resource

 | 

Hobby Included

 | 

On-demand Rates

 |
| --- | --- | --- |
| 

[Speed Insights Data Points](/docs/speed-insights/metrics#understanding-data-points)

 | First 10,000 | $0.65 per 10,000 Data points/10,000 Data points |

Pro teams can [set up Spend Management](/docs/spend-management#managing-your-spend-amount) to get notified or to automatically take action, such as [using a webhook](/docs/spend-management#configuring-a-webhook) or pausing your projects when your usage hits a set spend amount.

## [Limitations](#limitations)

Once you've enabled Speed Insights, different limitations are applied depending on your plan:

|  | Hobby | Pro | Enterprise |
| --- | --- | --- | --- |
| Reporting Window for Data Points | 7 Day | 30 Days | 90 Days |
| Maximum Number of Data Points per Month | 10,000 | None | None |

Once the maximum limit of data points is reached, no more data points will be recorded until the current day has passed. On the next day, the recording will resume. When recording is paused, you can still access all existing data points.

You can reduce the number of data points collected by adjusting the [Sample Rate](#sample-rate) at the project level by using the `@vercel/speed-insights`. To learn more, see [Sample Rate](/docs/speed-insights/package#samplerate).

## [Sample rate](#sample-rate)

By default, all incoming data points are used to calculate the scores you're being presented with on the Speed Insights view.

To reduce cost, you can change the sample rate at a project level by using the `@vercel/speed-insights` package as explained in [Sample rate](/docs/speed-insights/package#samplerate). To learn more about how to configure the `sampleRate` option, see the [Sending a sample of events to Speed Insights](/guides/sending-sample-to-speed-insights) recipe.

## [Prorating](#prorating)

Teams on the Pro or Enterprise plan will immediately be charged the base fee when enabling Speed Insights for each project. However, you will only be charged for the remaining time in your billing cycle. For example:

*   If there ten days are remaining in your current billing cycle — _that's roughly 30% of your billing cycle_ – you will only pay around 3 USD for each project that has Speed Insights enabled. For every new billing cycle after that, you'll be charged a total 10 USD for each project at the beginning of the cycle.
*   If you disable Speed Insights before the billing cycle ends Vercel will continue to show the already collected data points until the end of that specific billing cycle. However, no new data will be recorded.
*   Once the billing cycle is over, Speed Insights will automatically turn off, and you will lose access to existing data. You won't be refunded any amounts already paid. Also, you cannot export the Speed Insights data for later use
*   If you decide to re-enable the feature after cancellation, you won't be charged when you enable it. Instead, the usual 10 USD base fee will apply at the beginning of every upcoming billing cycle

## [Usage](#usage)

The table below shows the metrics for the [Observability](/docs/pricing/observability) section of the Usage dashboard where you can view your Speed Insights usage.

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
| [Data points](/docs/pricing/observability#managing-speed-insights-data-points) | The number of data points reported from browsers | [Yes](/docs/pricing#managed-infrastructure-billable-resources) | [Learn More](/docs/pricing/observability#optimizing-speed-insights-data-points) |

See the [manage and optimize Observability usage](/docs/pricing/observability) section for more information on how to optimize your usage.

Speed Insights and Web Analytics require scripts to do collection of [data points](/docs/speed-insights/metrics#understanding-data-points). These scripts are loaded on the client-side and therefore may incur additional usage and costs for [Data Transfer](/docs/manage-cdn-usage#fast-data-transfer) and [Edge Requests](/docs/manage-cdn-usage#edge-requests).

--------------------------------------------------------------------------------
title: "Speed Insights Metrics"
description: "Learn what each performance metric on Speed Insights means and how the scores are calculated."
last_updated: "null"
source: "https://vercel.com/docs/speed-insights/metrics"
--------------------------------------------------------------------------------

# Speed Insights Metrics

Copy page

Ask AI about this page

Last updated September 24, 2025

## [Real Experience Score (RES)](#real-experience-score-res)

### [Real user monitoring](#real-user-monitoring)

While many performance measurement tools, like [Lighthouse](https://web.dev/measure/), estimate user experience based on lab simulations, Vercel's Real Experience Score (RES) uses real data points collected from your users' devices.

As a result, RES shows how real users experience your application. This real-time data helps you understand your application's performance and track changes as they happen.

You can use these insights to see how new deployments affect performance, helping you improve your application's user experience.

![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fspeed-insights%2Fv2%2Fres-light.png&w=1920&q=75)![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fspeed-insights%2Fv2%2Fres-dark.png&w=1920&q=75)

An example of a Real Experience Score over time.

The timestamps in the Speed Insights view are in local time (not UTC).

## [Core Web Vitals explained](#core-web-vitals-explained)

The Core Web Vitals, as defined by Google and the [Web Performance Working Group](https://www.w3.org/webperf/), are key metrics that assess your web application's loading speed, responsiveness, and visual stability.

Speed Insights now uses Lighthouse 10 scoring criteria instead of Lighthouse 6 criteria as explained in [Updated Scoring Criteria](/docs/speed-insights/migrating-from-legacy#updated-scoring-criteria)

| Metric | Description | Target Value |
| --- | --- | --- |
| [Largest Contentful Paint (LCP)](#largest-contentful-paint-lcp) | Measures the time from page start to when the largest content element is fully visible. | 2.5 seconds or less |
| [Cumulative Layout Shift (CLS)](#cumulative-layout-shift-cls) | Quantifies the fraction of layout shift experienced by the user over the lifespan of the page. | 0.1 or less |
| [Interaction to Next Paint (INP)](#interaction-to-next-paint-inp) | Measures the time from user interaction to when the browser renders the next frame. | 200 millisecond or less |
| [First Contentful Paint (FCP)](#first-contentful-paint-fcp) | Measures the time from page start to the rendering of the first piece of DOM content. | 1.8 seconds or less |
| [First Input Delay (FID)](#first-input-delay-fid) | Measures the time from a user's first interaction to the time the browser is able to respond. | 100 milliseconds or less |
| [Total Blocking Time (TBT)](#total-blocking-time-tbt) | Measures the total amount of time between FCP and TTI where the main thread was blocked long enough to prevent input responsiveness. | Under 800 milliseconds |
| [Time to First Byte (TTFB)](#time-to-first-byte-ttfb) | Measures the time from the request of a resource to when the first byte of a response begins to arrive. | Under 800 milliseconds |

### [Largest Contentful Paint (LCP)](#largest-contentful-paint-lcp)

[Largest Contentful Paint](https://web.dev/articles/lcp) (LCP) is a performance metric that measures the time from when the page starts loading to when the largest content element in the viewable screen is fully displayed. This could be an image, a video, or a block of text. LCP is important as it gives a measure of when the main content of the page is visible to the user.

A good LCP time is considered to be 2.5 seconds or less.

### [Cumulative Layout Shift (CLS)](#cumulative-layout-shift-cls)

[Cumulative Layout Shift](https://web.dev/articles/cls) (CLS) is a performance metric that quantifies the fraction of layout shift experienced by the user. A layout shift occurs any time a visible element changes its position from one rendered frame to the next.

The score is calculated from the product of two measures:

*   The impact fraction - the area of the viewport impacted by the shift
*   The distance fraction - the distance the elements have moved relative to the viewport between frames

A good CLS score is considered to be 0.1 or less.

### [Interaction to Next Paint (INP)](#interaction-to-next-paint-inp)

[Interaction to Next Paint](https://web.dev/articles/inp) (INP) is a metric that measures the time from when a user interacts with your site to the time the browser renders the next frame in response to that interaction.

This metric is used to gauge the responsiveness of a page to user interactions. The quicker the page responds to user input, the better the INP.

Lower INP times are better, with an INP time of 200 milliseconds or less being considered good.

### [First Contentful Paint (FCP)](#first-contentful-paint-fcp)

[First Contentful Paint](https://web.dev/articles/fcp) (FCP) is a performance metric that measures the time from the moment the page starts loading to the moment the first piece of content from the Document Object Model (DOM) is rendered on the screen. This could be any content from the webpage such as an image, a block of text, or a canvas render. The FCP is important because it indicates when the user first sees something useful on the screen, providing an insight into your webpage's loading speed.

Lower FCP times are better, with an FCP time of 1.8 seconds or less being considered good.

## [Other metrics](#other-metrics)

### [Time to First Byte (TTFB)](#time-to-first-byte-ttfb)

Time to First Byte (TTFB) measures the time between the request for a resource and when the first byte of a response begins to arrive.

Lower TTFB times are better, with a good TTFB time being considered as under 800 milliseconds.

### [First Input Delay (FID)](#first-input-delay-fid)

[First Input Delay](https://web.dev/articles/fid) (FID) measures the time from when a user first interacts with your site (by selecting a link for example) to the time when the browser is able to respond to that interaction. This metric is important on pages where the user needs to do something, because it captures some of the delay that users feel when trying to interact with the page.

A good FID score is 100 milliseconds or less.

As [stated by Google](https://web.dev/vitals/#lab-tools-to-measure-core-web-vitals), simulating an environment to measure Web Vitals necessitates a different approach since no real user request is involved.

### [Total Blocking Time (TBT)](#total-blocking-time-tbt)

Total Blocking Time (TBT) quantifies how non-interactive a page is. It measures the total time between the First Contentful Paint (FCP) and Time to Interactive (TTI) where the main thread was blocked for long enough to prevent user input. Long tasks (over 50 ms) block the main thread, preventing the user from interacting with the page. The sum of the time portions exceeding 50 ms constitutes the TBT.

Lower TBT times are better, with a good TBT time being considered as under 800 milliseconds.

For more in-depth information related to performance metrics, visit the PageSpeed Insights [documentation](https://developers.google.com/speed/docs/insights/v5/about).

## [How the scores are determined](#how-the-scores-are-determined)

Vercel calculates performance scores using real-world data obtained from the [HTTP Archive](https://httparchive.org/). This process involves assigning each collected metric (e.g., [First Contentful Paint (FCP)](#first-contentful-paint-fcp)) a score ranging from 0 to 100. The score is determined based on where the raw metric value falls within a log-normal distribution derived from actual website performance data.

For instance, if [HTTP Archive](https://httparchive.org/) data shows that the top-performing sites render the Largest Contentful Paint (LCP) in approximately 1220 milliseconds, this value is mapped to a score of 99. Vercel then uses this correlation, along with your project's specific LCP metric value, to compute your LCP score.

The Real Experience Score is a weighted average of all individual metric scores. Vercel has assigned each metric a specific weighting, which best represents user's perceived performance on mobile and desktop devices.

## [Understanding data points](#understanding-data-points)

In the context of Vercel's Speed Insights, a data point is a single unit of information that represents a measurement of a specific Web Vital metric during a user's visit to your website.

Data points are collected on hard navigations, which in the case of Next.js apps, are only the first-page view in a session. During a user's visit, data points are gathered during the initial page load, user interaction, and upon leaving the page.

As of now, up to 6 data points can be potentially tracked per visit:

*   On page load: Time to First Byte ([TTFB](#time-to-first-byte-ttfb)) and First Contentful Paint ([FCP](#first-contentful-paint-fcp))
*   On interaction: First Input Delay ([FID](#first-input-delay-fid)) and Largest Contentful Paint ([LCP](#largest-contentful-paint-lcp))
*   On leave: Interaction to Next Paint ([INP](#interaction-to-next-paint-inp)), Cumulative Layout Shift ([CLS](#cumulative-layout-shift-cls)), and, if not already sent, Largest Contentful Paint ([LCP](#largest-contentful-paint-lcp)).

The collection of metrics may vary depending on how users interact with or exit the page. On average, you can expect to collect between 3 and 6 metrics per visit.

These data points provide insights into various performance aspects of your website, such as the time it takes to display the first content ([FCP](#first-contentful-paint-fcp)) and the delay between user input and response ([FID](#first-input-delay-fid)). By analyzing these data points, you can gain valuable information to optimize and enhance the performance of your website.

### [How the percentages are calculated?](#how-the-percentages-are-calculated)

By default, the user experience percentile is set to P75, which offers a balanced overview of the majority of user experiences. You can view the data for the other percentiles by selecting them in the time-based line graph.

The chosen percentile corresponds to the proportion of users who experience a load time faster than a specific value. Here's how each percentile is defined:

*   P75: Represents the experience of the fastest 75% of your users, excluding the slowest 25%.
*   P90: Represents the experience of the fastest 90% of your users, excluding the slowest 10%.
*   P95: Represents the experience of the fastest 95% of your users, excluding the slowest 5%.
*   P99: Represents the experience of the fastest 99% of your users, excluding the slowest 1%.

For instance, a P75 score of 1 second for [First Contentful Paint (FCP)](#first-contentful-paint-fcp) means that 75% of your users experience an FCP faster than 1 second. Similarly, a P99 score of 8 seconds means 99% of your users experience an FCP faster than 8 seconds.

## [Interpreting performance scores](#interpreting-performance-scores)

Performance metrics, including the [Real Experience Score](#real-user-monitoring), the [Virtual Experience Score](#predictive-performance-metrics-with-virtual-experience-score), and the individual [Core Web Vitals](#core-web-vitals-explained) (along with [Other Web Vitals](#other-metrics)) are color-coded as follows:

*   0 to 49 (red): Poor
*   50 to 89 (orange): Needs Improvement
*   90 to 100 (green): Good

Aim for 'Good' scores (90 to 100) for both Real and Virtual Experience Scores. Keep in mind that reaching a score of 100 is extremely challenging due to diminishing returns. For example, improving from 99 to 100 is much harder than moving from 90 to 94, as the effort needed increases dramatically at higher scores.

### [Implications of scores for the end-user experience](#implications-of-scores-for-the-end-user-experience)

Higher Real Experience and Virtual Experience Scores generally translate to better end-user experiences, making it worthwhile to strive for improved Web Vital Scores. Performance scores are color-coded and improvements within the same color range will enhance user experience but don't significantly impact search engine rankings.

If you aim to boost your site's search ranking, aim to move your scores into a higher color-coded category, for instance, from 'Needs Improvement' (orange) to 'Good' (green). This change reflects substantial improvements in performance and is more likely to be rewarded with higher search engine rankings.

## [Predictive performance metrics with Virtual Experience Score](#predictive-performance-metrics-with-virtual-experience-score)

The Real Experience Score ([RES](#real-user-monitoring)) displayed in the Speed Insights tab is derived from actual data points collected from your visitors' devices. As such, it can only offer insight into your app's performance post-deployment. While it's critical to gather these real-world data points, they only reflect user experiences after the fact, limiting their predictive power.

In contrast, the Virtual Experience Score (VES) is a predictive performance metric that allows you to anticipate the impact of changes on your app's performance, ensuring there's no regression in user experience. This metric is provided by [integrations](/integrations) like [Checkly](/integrations/checkly) that employ Deployment Checks.

Setting up an integration supporting performance checks enables these checks to run for each deployment. These checks assess whether the user experience is likely to improve or deteriorate with the proposed changes, helping guide your decision-making process.

Like RES, the VES draws from four separate Speed Insights, albeit with some variations:

*   In place of the First Input Delay ([FID](#first-input-delay-fid)) Core Web Vital, the Virtual Experience Score utilizes Total Blocking Time ([TBT](#total-blocking-time-tbt))
*   The specific device type used for checks depends on the Integration you've set up. For example, Checkly only uses "Desktop" for determining scores

## [Breaking down data in Speed Insights](#breaking-down-data-in-speed-insights)

Speed Insights offers a variety of views to help you analyze your application's performance data. This allows you to identify areas that need improvement and make informed decisions about how to optimize your site. To learn more, see [Using Speed Insights](/docs/speed-insights/using-speed-insights).

--------------------------------------------------------------------------------
title: "Speed Insights Configuration with @vercel/speed-insights"
description: "Learn how to configure your application to capture and send web performance metrics to Vercel using the @vercel/speed-insights npm package."
last_updated: "null"
source: "https://vercel.com/docs/speed-insights/package"
--------------------------------------------------------------------------------

# Speed Insights Configuration with @vercel/speed-insights

Copy page

Ask AI about this page

Last updated September 24, 2025

Speed Insights is available on [all plans](/docs/plans)

With the `@vercel/speed-insights` npm package, you're able to configure your application to capture and send web performance metrics to Vercel.

## [Getting started](#getting-started)

To get started with Speed Insights, refer to our [Quickstart](/docs/speed-insights/quickstart) guide which will walk you through the process of setting up Speed Insights for your project.

## [`sampleRate`](#samplerate)

In prior versions of Speed Insights this was managed in the UI. This option is now managed through code with the package.

This parameter determines the percentage of events that are sent to the server. By default, all events are sent. Lowering this parameter allows for cost savings but may result in a decrease in the overall accuracy of the data being sent. For example, a `sampleRate` of `0.5` would mean that only 50% of the events will be sent to the server.

To learn more about how to configure the `sampleRate` option, see the [Sending a sample of events to Speed Insights](/guides/sending-sample-to-speed-insights) recipe.

## [`beforeSend`](#beforesend)

With the `beforeSend` function, you can modify or filter out the event data before it's sent to Vercel. You can use this to redact sensitive data or to avoid sending certain events.

For instance, if you wish to ignore events from a specific URL or modify them, you can do so with this option.

```
// Example usage of beforeSend
beforeSend: (data) => {
  if (data.url.includes('/sensitive-path')) {
    return null; // this will ignore the event
  }
  return data; // this will send the event as is
};
```

## [`debug`](#debug)

With the debug mode, you can view all Speed Insights events in the browser's console. This option is especially useful during development.

This option is automatically enabled if the `NODE_ENV` environment variable is available and either `development` or `test`.

You can manually disable it to prevent debug messages in your browsers console.

## [`route`](#route)

The `route` option allows you to specify the current dynamic route (such as `/blog/[slug]`). This is particularly beneficial when you need to aggregate performance metrics for similar routes.

This option is automatically set when using a framework specific import such as for Next.js, Nuxt, SvelteKit and Remix.

## [`endpoint`](#endpoint)

The `endpoint` option allows you to report the collected metrics to a different url than the default: `https://yourdomain.com/_vercel/speed-insights/vitals`.

This is useful when deploying several projects under the same domain, as it allows you to keep each application isolated.

For example, when `yourdomain.com` is managed outside of Vercel:

1.  "alice-app" is deployed under `yourdomain.com/alice/*`, vercel alias is `alice-app.vercel.sh`
2.  "bob-app" is deployed under `yourdomain.com/bob/*`, vercel alias is `bob-app.vercel.sh`
3.  `yourdomain.com/_vercel/*` is routed to `alice-app.vercel.sh`

Both applications are sending their metrics to `alice-app.vercel.sh`. To restore the isolation, "bob-app" should use:

```
<SpeedInsights endpoint="https://bob-app.vercel.sh/_vercel/speed-insights/vitals" />
```

## [`scriptSrc`](#scriptsrc)

The `scriptSrc` option allows you to load the Speed Insights script from a different URL than the default one.

```
<SpeedInsights scriptSrc="https://bob-app.vercel.sh/_vercel/speed-insights/script.js" />
```

## [More resources](#more-resources)

*   [Sending a sample of your events](/guides/sending-sample-to-speed-insights)

--------------------------------------------------------------------------------
title: "Vercel Speed Insights Privacy & Compliance"
description: "Learn how Vercel follows the latest privacy and data compliance standards with its Speed Insights feature."
last_updated: "null"
source: "https://vercel.com/docs/speed-insights/privacy-policy"
--------------------------------------------------------------------------------

# Vercel Speed Insights Privacy & Compliance

Copy page

Ask AI about this page

Last updated March 4, 2025

Speed Insights is available on [all plans](/docs/plans)

To ensure that the Speed Insights feature can be used despite many different regulatory limitations around the world, we've designed it in such a way that it provides you with information without being tied to, or associated with, any individual visitor or IP address.

The recording of data points is anonymous and the Speed Insights feature does not collect or store information that would enable us to reconstruct a browsing session across pages or identify a user.

The following information is stored with every data point:

| Collected Value | Example Value |
| --- | --- |
| Route | /blog/\[slug\] |
| URL | /blog/nextjs-10 |
| Network Speed | 4g (or slow-2g, 2g, 3g) |
| Browser | Chrome 86 (Blink) |
| Device Type | Mobile (or Desktop/Tablet) |
| Device OS | Android 10 |
| Country (ISO 3166-1 alpha-2) | US |
| Web Vital | FCP 1.0s |
| Web Vital Attribution | html>body img.header |
| SDK Information | @vercel/speed-insights 0.1.0 |
| Server-Received Event Time | 2023-10-29 09:06:30 |

See our [Privacy Notice](/legal/privacy-policy) for more information, including how Vercel Speed Insights complies with the GDPR.

## [How the data points are tracked](#how-the-data-points-are-tracked)

Once you've followed the dashboard's instructions for enabling Speed Insights and installed the `@vercel/speed-insights` package, it will automatically start tracking data points for your project.

The package injects a script that retrieves the visitor's [Web Vitals](/docs/speed-insights/metrics) by invoking native browser APIs and reporting them to Vercel's servers on every page load.

Learn more about the [first-party intake data ingestion method](/docs/speed-insights/migrating-from-legacy#first-party-intake), which enables a faster and more reliable experience.

--------------------------------------------------------------------------------
title: "Getting started with Speed Insights"
description: "Vercel Speed Insights provides you detailed insights into your website's performance. This quickstart guide will help you get started with using Speed Insights on Vercel."
last_updated: "null"
source: "https://vercel.com/docs/speed-insights/quickstart"
--------------------------------------------------------------------------------

# Getting started with Speed Insights

Copy page

Ask AI about this page

Last updated September 24, 2025

This guide will help you get started with using Vercel Speed Insights on your project, showing you how to enable it, add the package to your project, deploy your app to Vercel, and view your data in the dashboard.

Speed Insights is available on [all plans](/docs/plans)

To view instructions on using the Vercel Speed Insights in your project for your framework, use the Choose a framework dropdown on the right (at the bottom in mobile view).

## [Prerequisites](#prerequisites)

*   A Vercel account. If you don't have one, you can [sign up for free](https://vercel.com/signup).
*   A Vercel project. If you don't have one, you can [create a new project](https://vercel.com/new).
*   The Vercel CLI installed. If you don't have it, you can install it using the following command:
    
    pnpmyarnnpmbun
    
    ```
    pnpm i -g vercel
    ```
    

1.  ### [Enable Speed Insights in Vercel](#enable-speed-insights-in-vercel)
    
    On the [Vercel dashboard](/dashboard), select your Project followed by the Speed Insights tab. You can also select the button below to be taken there. Then, select Enable from the dialog.
    
    [Go to Speed Insights](/d?to=%2F%5Bteam%5D%2F%5Bproject%5D%2Fspeed-insights&title=Open+Speed+Insights)
    
    Enabling Speed Insights will add new routes (scoped at`/_vercel/speed-insights/*`) after your next deployment.
    
2.  ### [Add `@vercel/speed-insights` to your project](#add-@vercel/speed-insights-to-your-project)
    
    Using the package manager of your choice, add the `@vercel/speed-insights` package to your project:
    
    pnpmyarnnpmbun
    
    ```
    pnpm i @vercel/speed-insights
    ```
    
3.  ### [Add the `SpeedInsights` component to your app](#add-the-speedinsights-component-to-your-app)
    
    The `SpeedInsights` component is a wrapper around the tracking script, offering more seamless integration with Next.js.
    
    Add the following component to the root layout:
    
    Next.js v13.5+Older Next.js versions
    
    Add the following component to your main app file:
    
    app/layout.tsx
    
    Next.js (/app)
    
    Next.js (/app)Next.js (/pages)SvelteKitCreate React AppNuxtVueRemixAstroHTMLOther frameworks
    
    TypeScript
    
    TypeScriptJavaScript
    
    ```
    import { SpeedInsights } from '@vercel/speed-insights/next';
     
    export default function RootLayout({
      children,
    }: {
      children: React.ReactNode;
    }) {
      return (
        <html lang="en">
          <head>
            <title>Next.js</title>
          </head>
          <body>
            {children}
            <SpeedInsights />
          </body>
        </html>
      );
    }
    ```
    
    For versions of Next.js older than 13.5, import the `<SpeedInsights>` component from `@vercel/speed-insights/react`.
    
    Create a dedicated component to avoid opting out from SSR on the layout and pass the pathname of the route to the `SpeedInsights` component:
    
    app/insights.tsx
    
    Next.js (/app)
    
    Next.js (/app)Next.js (/pages)SvelteKitCreate React AppNuxtVueRemixAstroHTMLOther frameworks
    
    TypeScript
    
    TypeScriptJavaScript
    
    ```
    'use client';
     
    import { SpeedInsights } from '@vercel/speed-insights/react';
    import { usePathname } from 'next/navigation';
     
    export function Insights() {
      const pathname = usePathname();
     
      return <SpeedInsights route={pathname} />;
    }
    ```
    
    Then, import the `Insights` component in your layout:
    
    app/layout.tsx
    
    Next.js (/app)
    
    Next.js (/app)Next.js (/pages)SvelteKitCreate React AppNuxtVueRemixAstroHTMLOther frameworks
    
    TypeScript
    
    TypeScriptJavaScript
    
    ```
    import type { ReactNode } from 'react';
    import { Insights } from './insights';
     
    export default function RootLayout({ children }: { children: ReactNode }) {
      return (
        <html lang="en">
          <head>
            <title>Next.js</title>
          </head>
          <body>
            {children}
            <Insights />
          </body>
        </html>
      );
    }
    ```
    
4.  ### [Deploy your app to Vercel](#deploy-your-app-to-vercel)
    
    You can deploy your app to Vercel's global [CDN](/docs/cdn) by running the following command from your terminal:
    
    terminal
    
    ```
    vercel deploy
    ```
    
    Alternatively, you can [connect your project's git repository](/docs/git#deploying-a-git-repository), which will enable Vercel to deploy your latest pushes and merges to main.
    
    Once your app is deployed, it's ready to begin tracking performance metrics.
    
    If everything is set up correctly, you should be able to find the `/_vercel/speed-insights/script.js` script inside the body tag of your page.
    
5.  ### [View your data in the dashboard](#view-your-data-in-the-dashboard)
    
    Once your app is deployed, and users have visited your site, you can view the data in the dashboard.
    
    To do so, go to your [dashboard](/dashboard), select your project, and click the Speed Insights tab.
    
    After a few days of visitors, you'll be able to start exploring your metrics. For more information on how to use Speed Insights, see [Using Speed Insights](/docs/speed-insights/using-speed-insights).
    

Learn more about how Vercel supports [privacy and data compliance standards](/docs/speed-insights/privacy-policy) with Vercel Speed Insights.

## [Next steps](#next-steps)

Now that you have Vercel Speed Insights set up, you can explore the following topics to learn more:

*   [Learn how to use the `@vercel/speed-insights` package](/docs/speed-insights/package)
*   [Learn about metrics](/docs/speed-insights/metrics)
*   [Read about privacy and compliance](/docs/speed-insights/privacy-policy)
*   [Explore pricing](/docs/speed-insights/limits-and-pricing)
*   [Troubleshooting](/docs/speed-insights/troubleshooting)

--------------------------------------------------------------------------------
title: "Troubleshooting Vercel Speed Insights"
description: "Learn about common issues and how to troubleshoot Vercel Speed Insights."
last_updated: "null"
source: "https://vercel.com/docs/speed-insights/troubleshooting"
--------------------------------------------------------------------------------

# Troubleshooting Vercel Speed Insights

Copy page

Ask AI about this page

Last updated March 4, 2025

Speed Insights is available on [all plans](/docs/plans)

## [No data visible in Speed Insights dashboard](#no-data-visible-in-speed-insights-dashboard)

If you are experiencing a situation where data is not visible in the Speed Insights dashboard, it could be due to a couple of reasons.

How to fix:

1.  Double check if you followed the quickstart instructions correctly
2.  Check if your adblocker is interfering with the Speed Insights script. If so, consider disabling it

## [Requests are not getting called](#requests-are-not-getting-called)

If `/_vercel/speed-insights/script.js` is correctly loading but not sending any data (e.g. no `vitals` request), ensure that you're checking for the request after navigating to a different page, or switching tabs. Speed Insights data is only sent on window blur or unload events.

## [Speed Insights is not working with proxy](#speed-insights-is-not-working-with-proxy)

We do not recommend placing a reverse proxy in front of Vercel, as it may interfere with the proper functioning of Speed Insights.

How to fix:

1.  Check your proxy configuration to make sure that all desired pages are correctly proxied to the deployment
2.  Additionally, forward all requests to `/_vercel/speed-insights/*` to the deployments to ensure proper functioning of Speed Insights through the proxy

--------------------------------------------------------------------------------
title: "Using Speed Insights"
description: "Learn how to use Speed Insights to analyze your application's performance data."
last_updated: "null"
source: "https://vercel.com/docs/speed-insights/using-speed-insights"
--------------------------------------------------------------------------------

# Using Speed Insights

Copy page

Ask AI about this page

Last updated September 24, 2025

## [Accessing Speed Insights](#accessing-speed-insights)

To access Speed Insights:

1.  Select a project from your dashboard and navigate to the Speed Insights tab.
2.  Select the [timeframe](/docs/analytics/using-web-analytics#specifying-a-timeframe) and [environment](/docs/analytics/using-web-analytics#viewing-environment-specific-data) you want to view data for.
3.  Use the panels to [filter](/docs/analytics/filtering) the page or event data you want to view.

## [Breaking down data in Speed Insights](#breaking-down-data-in-speed-insights)

Speed Insights offers a variety of views to help you analyze your application's performance data. This allows you to identify areas that need improvement and make informed decisions about how to optimize your site.

### [Breakdown by route or path](#breakdown-by-route-or-path)

To view metrics for a specific route or path:

1.  Select a project from your dashboard and navigate to the Speed Insights tab.
2.  From the left-hand panel, select the [metric](/docs/speed-insights/metrics) you want to view data for.
3.  From the URL view, select the corresponding tab to view by the Route (the actual pages you built), or by Path (the URLs requested by the visitor).
4.  The information is organized by performance score and sorted by data points. Scroll the list to view more all paths or routes, or click the View all button to view and filter all data.
5.  You can also edit the \[timeframe\]/docs/analytics/using-web-analytics#specifying-a-timeframe) and \[environment\]/docs/analytics/using-web-analytics#viewing-environment-specific-data) you want to view data for.

![Speed Insights URL view for routes and paths of your project.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fspeed-insights%2Fv2%2Fkanban-light.png&w=3840&q=75)![Speed Insights URL view for routes and paths of your project.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fspeed-insights%2Fv2%2Fkanban-dark.png&w=3840&q=75)

Speed Insights URL view for routes and paths of your project.

### [Breakdown by HTML elements](#breakdown-by-html-elements)

To view a detailed breakdown of the performance of individual HTML elements on your site:

1.  Select a project from your dashboard and navigate to the Speed Insights tab.
2.  From the left-hand panel, select the [metric](/docs/speed-insights/metrics) you want to view data for. HTML element attribution is only available for the following metrics:
    *   Interaction to Next Paint (INP)
    *   First Input Delay (FID)
    *   Cumulative Layout Shift (CLS)
    *   Largest Contentful Paint (LCP)
3.  From the URL view, select the Selectors tab.
4.  The information is organized by performance score and sorted by data points. Scroll the list to view more all elements, or click the View all button to view and filter all data.
5.  You can also edit the \[timeframe\]/docs/analytics/using-web-analytics#specifying-a-timeframe) and \[environment\]/docs/analytics/using-web-analytics#viewing-environment-specific-data) you want to view data for.

This view is particularly useful for identifying specific elements that may be causing performance issues.

### [Breakdown by country](#breakdown-by-country)

This view is helpful for identifying regions where your application may be underperforming.

To view a geographical breakdown of your application's performance:

1.  Select a project from your dashboard and navigate to the Speed Insights tab.
2.  From the left-hand panel, select the [metric](/docs/speed-insights/metrics) you want to view data for.
3.  Scroll down to the Countries section.
4.  The map is colored based on the experience metric per country. Click on a country to view more detailed data.

![Geographic map of the P75 score where the color intensity indicates the relative amount of data points per country](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fspeed-insights%2Fv2%2Fcountry-map-light.png&w=3840&q=75)![Geographic map of the P75 score where the color intensity indicates the relative amount of data points per country](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fspeed-insights%2Fv2%2Fcountry-map-dark.png&w=3840&q=75)

Geographic map of the P75 score where the color intensity indicates the relative amount of data points per country

## [Disabling Speed Insights](#disabling-speed-insights)

You may want to disable Speed Insights in your project if you find you no longer need it. You can disable Speed Insights from within the project settings in the Vercel dashboard. If you are unsure if a project has Speed Insights enabled, see [Identifying if Speed Insights is enabled](#identifying-if-speed-insights-is-enabled).

If you transfer a project with Speed Insights enabled from a Hobby team to a Pro plan, it will continue to be enabled but with increased limits, as documented in the [pricing docs](/docs/speed-insights/limits-and-pricing). This means that Speed Insights will be added to your Pro plan invoice automatically.

1.  Select a project from your [dashboard](/dashboard).
2.  Navigate to the Speed Insights tab.
3.  Click on the ellipsis on the top-right of the Speed Insights page and select Disable Speed Insights.

![Disable Speed Insights option.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fspeed-insights%2Fv2%2Fdisable-light.png&w=1920&q=75)![Disable Speed Insights option.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fspeed-insights%2Fv2%2Fdisable-dark.png&w=1920&q=75)

Disable Speed Insights option.

When you disable Speed Insights in the middle of your billing cycle, it will not be removed instantly. Instead it will stop collecting new data points but will continue to show already collected data until the end of the cycle, see the [prorating docs](/docs/speed-insights/limits-and-pricing#prorating) for more information.

If you are on an Enterprise plan, check your contract entitlements as you may have custom limits included. If you have any questions about your billing/contract regarding Speed Insights you can reach out to your Customer Success Manager (CSM) or Account Executive (AE) for further clarification.

## [Identifying if Speed Insights is enabled](#identifying-if-speed-insights-is-enabled)

If you have many projects on your Vercel account and are not sure which of them has Speed Insights enabled, you can see this from the [dashboard](/dashboard) without needing to check each project separately. The different circles in the right corner of each project card will show the Speed Insights status.

If Speed Insights is not enabled, then the circle will be gray, with the speed insights logo. For example:

![Speed Insights not enabled for a project.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fspeed-insights%2Fv2%2Fready-to-enable-light.png&w=828&q=75)![Speed Insights not enabled for a project.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fspeed-insights%2Fv2%2Fready-to-enable-dark.png&w=828&q=75)

Speed Insights not enabled for a project.

If Speed Insights is enabled but no data points have been collected yet then it will show an empty circle, like the below:

![Speed Insights enabled for a project but no data points have been collected.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fspeed-insights%2Fv2%2Fenabled-no-data-light.png&w=828&q=75)![Speed Insights enabled for a project but no data points have been collected.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fspeed-insights%2Fv2%2Fenabled-no-data-dark.png&w=828&q=75)

Speed Insights enabled for a project but no data points have been collected.

If Speed Insights is enabled and data points have been collected then the circle will be colored with a number inside, similar to the below image:

![Speed Insights enabled for a project and has data points.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fspeed-insights%2Fv2%2Fenabled-light.png&w=828&q=75)![Speed Insights enabled for a project and has data points.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fspeed-insights%2Fv2%2Fenabled-dark.png&w=828&q=75)

Speed Insights enabled for a project and has data points.

--------------------------------------------------------------------------------
title: "Spend Management"
description: "Learn how to get notified about your account spend and configure a webhook."
last_updated: "null"
source: "https://vercel.com/docs/spend-management"
--------------------------------------------------------------------------------

# Spend Management

Copy page

Ask AI about this page

Last updated September 29, 2025

Spend Management is available on [Pro plans](/docs/plans/pro)

Those with the [owner](/docs/rbac/access-roles#owner-role) and [billing](/docs/rbac/access-roles#billing-role) roles can access this feature

Spend management is a way for you to notify or to automatically take action on your account when your team hits a [set spend amount](#what-does-spend-management-include). The actions you can take are:

*   [Receive a notification](/docs/spend-management#managing-alert-threshold-notifications)
*   [Trigger a webhook](/docs/spend-management#configuring-a-webhook)
*   [Pause the production deployment of all your projects](/docs/spend-management#pausing-projects)

Setting a spend amount does not automatically stop usage. If you want to pause all your projects at a certain amount, you must [enable the option](#pausing-projects).

The spend amount is set per billing cycle.

Setting the amount halfway through a billing cycle considers your current spend. You can increase or decrease your spend amount as needed. If you configure it below the current monthly spend, Spend Management will trigger any configured actions (including pausing all projects).

## [What does Spend Management include?](#what-does-spend-management-include)

The spend amount that you set covers [metered resources](/docs/limits#additional-resources) that go beyond your Pro plan [credits and usage allocation](/docs/plans/pro-plan#credit-and-usage-allocation) for all projects on your team.

It does not include seats, integrations (such as Marketplace), or separate [add-ons](/docs/pricing#pro-plan-add-ons), which Vercel charges on a monthly basis.

### [How Vercel checks your spend amount](#how-vercel-checks-your-spend-amount)

Vercel checks your metered resource usage often to determine if you are approaching or have exceeded your spend amount. This check happens every few minutes.

## [Managing your spend amount](#managing-your-spend-amount)

1.  To enable spend management, you must have an [Owner](/docs/rbac/access-roles#owner-role) or [Billing](/docs/rbac/access-roles#billing-role) role on your [Pro](/docs/plans/pro-plan) team
2.  From your team's [dashboard](/dashboard), select the Settings tab
3.  Select Billing from the list
4.  Under Spend Management, toggle the switch to enabled:
    
    ![Spend Management section with toggle enabled.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fteams%2Fspend-manage-light.png&w=1920&q=75)![Spend Management section with toggle enabled.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fteams%2Fspend-manage-dark.png&w=1920&q=75)
    
    Spend Management section with toggle enabled.
    
5.  Set the amount in USD at which you would like to receive a notification or trigger an action
6.  Select the action(s) to happen when your spend amount is reached: [pause all your projects](#pausing-projects), [send notifications](#managing-alert-threshold-notifications), or [trigger a webhook URL](#configuring-a-webhook)

## [Managing alert threshold notifications](#managing-alert-threshold-notifications)

When you set a spend amount, Vercel automatically enables web and email notifications for your team. These get triggered when spending on your team reaches 50%, 75%, and 100% of the spend amount. You can also receive [SMS notifications](/docs/spend-management#sms-notifications) when your team reaches 100% of the spend amount. To manage your notifications:

1.  You must have an [Owner](/docs/rbac/access-roles#owner-role) or [Billing](/docs/rbac/access-roles#billing-role) role on your [Pro](/docs/plans/pro-plan) team
2.  From your team's [dashboard](/dashboard), select the Settings tab
3.  Select My Notifications from the list
4.  Under Team, ensure that Spend Management is selected
5.  Select the icon and select the thresholds for which you would like to receive web and email notification, as described in [Notifications](/docs/notifications)
6.  Repeat the previous step for the Web, Email, and SMS notification sections

Following these steps only configures **your** notifications. Team members with the Owner or Billing role can configure their own preferences

### [SMS notifications](#sms-notifications)

In addition to web and email notifications, you can enable SMS notifications for Spend Management. They are only triggered when you reach 100% of your spend amount.

To enable SMS notifications:

1.  You must have an [Owner](/docs/rbac/access-roles#owner-role) or [Billing](/docs/rbac/access-roles#billing-role) role on your [Pro](/docs/plans/pro-plan) team. Note that following these steps only configures your SMS notifications. Each member with an Owner or Billing role can configure their own SMS notifications for Spend Management
2.  Set your [spend amount](#managing-your-spend-amount)
3.  From your team's [dashboard](/dashboard), select the Settings tab
4.  Select My Notifications from the list, scroll to SMS at the bottom of the page and toggle the switch to Enabled. If your personal profile has a phone number associated with it, SMS notifications will be enabled by default
5.  Under Team, ensure that Spend Management is selected
6.  Enter your phone number and follow the steps to verify it

## [Pausing projects](#pausing-projects)

Vercel provides an option to automatically pause the production deployment for all of your projects when your spend amount is reached.

1.  In the Spend Management section of your team's settings, enable and set your [spend amount](#managing-your-spend-amount)
2.  Ensure the Pause production deployment switch is Enabled
3.  Confirm the action by entering the team name and select Continue. Your changes save automatically
4.  When your team reaches the spend amount, Vercel automatically pauses the production deployment for all projects on your team

When visitors access your production deployment while it is paused, they will see a [503 DEPLOYMENT\_PAUSED error](/docs/errors/DEPLOYMENT_PAUSED).

### [Unpausing projects](#unpausing-projects)

Projects need to be resumed on an individual basis, either [through the dashboard](/docs/projects/overview#resuming-a-project) or the [Vercel REST API](/docs/rest-api/reference/endpoints/projects/unpause-a-project).

Projects won't automatically unpause if you increase the spend amount, you must resume each project manually.

## [Configuring a webhook](#configuring-a-webhook)

You can configure a webhook URL to trigger events such as serving a static version of your site, [pausing a project](/docs/projects/overview#pausing-a-project), or sending a Slack notification.

Vercel will send a [HTTPS POST request](#webhook-payload) to the URL that you provide when the following events happen:

*   [When a spend amount reaches 100%](#spend-amount)
*   [At the end of your billing cycle](#end-of-billing-cycle)

To configure a webhook for spend management:

1.  In the Spend Management section of your team's settings, set your [spend amount](#managing-your-spend-amount)
2.  Enter the webhook URL for the endpoint that will receive a POST request. In order to be accessible, make sure your endpoints are public
3.  Secure your webhooks by comparing the [`x-vercel-signature`](/docs/headers/request-headers#x-vercel-signature) request header to the SHA that is generated when you save your webhook. To learn more, see the [securing webhooks](/docs/webhooks/webhooks-api#securing-webhooks) documentation

### [Webhook payload](#webhook-payload)

The webhook URL receives an HTTP POST request with the following JSON payload for each event:

#### [Spend amount](#spend-amount)

Sent when the team hits 50%, 75%, and 100% of their spend amount. For budgets created before September 2025, this is only sent at 100%.

| Parameters | Type | Description |
| --- | --- | --- |
| `budgetAmount` | 
int

 | The [spend amount](/docs/spend-management#managing-your-spend-amount) that you have set |
| `currentSpend` | 

int

 | The [total cost](/docs/spend-management#managing-your-spend-amount) that your team [has accrued](/docs/spend-management#what-does-spend-management-include) during the current billing cycle. |
| `teamId` | 

string

 | Your Vercel Team ID |
| `thresholdPercent` | 

int

 | The percentage of the total budget amount for the threshold that triggered this alert |

webhook-payload.json

```
{
  "budgetAmount": 500,
  "currentSpend": 500,
  "teamId": "team_jkT8yZ3oE1u6xLo8h6dxfNc3",
  "thresholdPercent": 100
}
```

### [End of billing cycle](#end-of-billing-cycle)

Sent when the billing cycle ends. You can use this event to resume paused projects.

| Parameters | Type | Description |
| --- | --- | --- |
| `teamId` | 
string

 | Your Vercel Team ID |
| `type` | 

string

 | The type of event |

webhook-payload.json

```
{
  "teamId": "team_jkT8yZ3oE1u6xLo8h6dxfNc3",
  "type": "endOfBillingCycle"
}
```

## [Spend Management activity](#spend-management-activity)

Vercel displays all spend management activity in the Activity tab of your [team's dashboard](/docs/observability/activity-log). This includes spend amount creation and updates, and project pausing and unpausing.

## [More resources](#more-resources)

For more information on Vercel's pricing, guidance on optimizing consumption, and invoices, see the following resources:

*   [How are resources used on Vercel?](/docs/pricing/how-does-vercel-calculate-usage-of-resources)
*   [Manage and optimize usage](/docs/pricing/manage-and-optimize-usage)
*   [Understanding my invoice](/docs/pricing/understanding-my-invoice)
*   [Spend limits for Vercel](https://youtu.be/-_vpoayWTps?si=Jv6b8szx68lVHGYz)

--------------------------------------------------------------------------------
title: "Vercel Storage"
description: "Store key-value data, transactional data, large files, and more with Vercel's suite of storage products."
last_updated: "null"
source: "https://vercel.com/docs/storage"
--------------------------------------------------------------------------------

# Vercel Storage

Copy page

Ask AI about this page

Last updated September 24, 2025

Vercel offers a suite of managed, serverless storage products that integrate with your frontend framework.

*   [Vercel Blob](/docs/storage/vercel-blob): Large file storage
*   [Vercel Edge Config](/docs/edge-config): Global, low-latency data store

You can also find storage solutions in the [Vercel Marketplace](https://vercel.com/marketplace/category/storage).

*   Explore [Marketplace Redis (KV) integrations](https://vercel.com/marketplace?category=storage&search=redis)
*   Explore [Marketplace Postgres integrations](https://vercel.com/marketplace?category=storage&search=postgres)

This page will help you choose the right storage product for your use case.

## [Choosing a storage product](#choosing-a-storage-product)

Choosing the correct storage solution depends on your needs for latency, durability, and consistency, among many other considerations.

To help you choose, we've created a table below to summarize the benefits of each storage option in relation to each other:

| Product | Reads | Writes | Use Case | Limits | Plans |
| --- | --- | --- | --- | --- | --- |
| [Blob](/docs/storage/vercel-blob) | Fast | Milliseconds | Large, content-addressable files ("blobs") | [Learn more](/docs/storage/vercel-blob/usage-and-pricing) | Hobby, Pro |
| [Edge Config](/docs/edge-config) | Ultra-fast | Seconds | Runtime configuration (e.g., feature flags) | [Learn more](/docs/edge-config/edge-config-limits) | Hobby, Pro, Enterprise |

Read our section on [best practices](#best-practices) to get the most out of our storage products.

## [Vercel Blob](#vercel-blob)

Vercel Blob is available on [all plans](/docs/plans)

Those with the [owner, member, developer](/docs/rbac/access-roles#owner, member, developer-role) role can access this feature

Vercel Blob offers optimized storage for images, videos, and other files.

You should use Vercel Blob if you need to:

*   Store images: For example, storing user avatars or product images
*   Store videos: For example, storing user-generated video content

### [Explore Vercel Blob](#explore-vercel-blob)

*   [Overview](/docs/storage/vercel-blob)
*   [Quickstart](/docs/storage/vercel-blob/server-upload)

## [Edge Config](#edge-config)

Edge Config is available on [all plans](/docs/plans)

An Edge Config is a global data store that enables you to read data at the edge without querying an external database or hitting upstream servers. Most lookups return in less than 1ms, and 99% of reads will return under 10ms.

You should use Edge Config if you need to:

*   Fetch data at ultra-low latency: For example, you should store feature flags in an Edge Config store.
*   Store data that is read often but changes rarely: For example, you should store critical redirect URLs in an Edge Config store.
*   Read data in every region: Edge Config data is actively replicated to all regions in the Vercel CDN.

### [Explore Edge Config](#explore-edge-config)

*   [Overview](/docs/edge-config)
*   [Quickstart](/docs/edge-config/get-started)
*   [Limits & Pricing](/docs/edge-config/edge-config-limits)

## [Best practices](#best-practices)

When choosing a storage option, we recommend considering these best practices:

### [Locate your data close to your functions](#locate-your-data-close-to-your-functions)

To ensure low-latency responses, it's crucial to have compute close to your databases. Always deploy your databases in [regions](/docs/regions) closest to your Functions to avoid long network roundtrips.

*   [Vercel functions](/docs/functions): Defaults to `iad1`, but can be deployed to any region
    *   If using Vercel Postgres, ensure your database is in the same region as your Function
    *   If using Vercel KV and replicated regions, place your stores in the same regions as your Functions
    *   If using Vercel Postgres, ensure your database is in the same region as your Function
    *   If using Vercel KV and replicated regions, place your stores in the same regions as your Functions
*   [Middleware](/docs/routing-middleware): Global only; always executed in the region nearest the user
    *   Since Middleware are part of request processing, it is best suited for extremely fast and globally replicated data like [Edge Config](/docs/edge-config)

### [Optimize for high cache hit rates](#optimize-for-high-cache-hit-rates)

Vercel's CDN provides caching in every region globally. To ensure the fastest response times, ensure data fetched from your data store is properly [cached](/docs/edge-cache) at the edge.

[Incremental Static Regeneration](/docs/concepts/incremental-static-regeneration/overview) automates properly setting up caching headers and globally storing generated assets for you. This ensures the highest availability for your traffic and prevents accidental misconfiguration of cache-control headers.

You can manually configure cache-control headers when using [Vercel Functions](/docs/edge-cache#using-vercel-functions) to cache the response data in every CDN region. Middleware runs before the CDN cache layer and cannot use cache-control headers.

## [Transferring your store](#transferring-your-store)

You can bring your Blob or Edge Config stores along with your account as you upgrade from Hobby to Pro, or downgrade from Pro to Hobby. To do so:

1.  Navigate to the [dashboard](/dashboard) and select the Storage tab
2.  Select the store that you would like to transfer
3.  Select Settings, then select Transfer Store
4.  Select a destination account or team. If you're upgrading to Pro, select your new Pro team. If downgrading, select your Hobby team

When successful, you'll be taken to the Storage tab of the account or team you transferred the store to.

--------------------------------------------------------------------------------
title: "Two-factor Authentication"
description: "Learn how to configure two-factor authentication for your Vercel account."
last_updated: "null"
source: "https://vercel.com/docs/two-factor-authentication"
--------------------------------------------------------------------------------

# Two-factor Authentication

Copy page

Ask AI about this page

Last updated September 15, 2025

To add an additional layer of security to your Vercel account, you can enable two-factor authentication (2FA). This feature requires you to provide a second form of verification when logging in to your account. There are two methods available for 2FA on Vercel:

*   Authenticator App: Use an authenticator app like Google Authenticator to generate a time-based one-time password (TOTP).
*   Passkey: Authenticate using any WebAuthN compatible device, such as a security key or biometric key.

## [Enabling Two-factor Authentication](#enabling-two-factor-authentication)

1.  Navigate to your [account settings](https://vercel.com/account/settings/authenticate#two-factor-authentication) on Vercel
2.  Toggle the switch to enable 2FA
3.  Set up your 2FA methods
4.  Confirm your setup
5.  Save your recovery codes

![Two-factor authentication settings.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Ftwo-factor%2Ftwo-factor-settings.png&w=2048&q=75)![Two-factor authentication settings.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Ftwo-factor%2Ftwo-factor-settings-dark.png&w=2048&q=75)

Two-factor authentication settings.

### [Configuring an Authenticator App (TOTP)](#configuring-an-authenticator-app-totp)

Scan the QR code with your authenticator app or manually enter the provided key. Once added, enter the generated 6-digit code to verify your setup.

![The time-based one-time password (TOTP) setup modal.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Ftwo-factor%2Ftotp.png&w=1080&q=75)![The time-based one-time password (TOTP) setup modal.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Ftwo-factor%2Ftotp-dark.png&w=1080&q=75)

The time-based one-time password (TOTP) setup modal.

### [Configuring a Passkey](#configuring-a-passkey)

See the [Login with passkeys](/docs/accounts/create-an-account#login-with-passkeys) for more information on setting up a security key or biometric key.

### [Recovery Codes](#recovery-codes)

After setting up two-factor authentication (2FA), you will be prompted to save your recovery codes. Store these codes in a safe place, as they can be used to access your account if you lose access to your 2FA methods.

Each recovery code can only be used once, and you can generate a new set of codes at any time.

![The recovery codes modal.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Ftwo-factor%2Frecovery-codes.png&w=1080&q=75)![The recovery codes modal.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Ftwo-factor%2Frecovery-codes-dark.png&w=1080&q=75)

The recovery codes modal.

## [Enforcing Two-Factor Authentication](#enforcing-two-factor-authentication)

Teams can enforce two-factor authentication (2FA) for all members. Once enabled, team members must configure 2FA before accessing team resources. Visit the [Two-Factor Enforcement](/docs/two-factor-enforcement) documentation for more information on how to enforce 2FA for your team.

--------------------------------------------------------------------------------
title: "Two-factor enforcement"
description: "Learn how to enforce two-factor authentication (2FA) for your Vercel team members to enhance security."
last_updated: "null"
source: "https://vercel.com/docs/two-factor-enforcement"
--------------------------------------------------------------------------------

# Two-factor enforcement

Copy page

Ask AI about this page

Last updated September 15, 2025

To enhance the security of your Vercel team, you can enforce two-factor authentication (2FA) for all team members. When enabled, members will be required to configure 2FA before they can access team resources.

What to expect:

*   Team members will not be able to access team resources until they have 2FA enabled.
*   Team members will continue to occupy a team seat.
*   Any CI/CD pipeline tokens associated with users without 2FA will cease to work.
*   Managed accounts, like service accounts or bots, will also need to have 2FA enabled.
*   Members without 2FA will be prompted to enable it when visiting the team dashboard.
*   Builds will fail for members without 2FA.
*   Notifications will continue to be sent to members without 2FA.

For more information on how to set up two-factor authentication for your account, see the [two-factor authentication](/docs/two-factor-authentication) documentation.

## [Viewing team members' 2FA status](#viewing-team-members'-2fa-status)

Team owners can view the two-factor authentication status of all team members in the [team members page](/docs/rbac/managing-team-members). Users without 2FA will have a label indicating their state. A filter is available on the same page to show members with two-factor authentication enabled or disabled.

![Two-factor authentication status on the Members page.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Ftwo-factor%2Fmembers-2fa-light.png&w=2048&q=75)![Two-factor authentication status on the Members page.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Ftwo-factor%2Fmembers-2fa-dark.png&w=2048&q=75)

Two-factor authentication status on the Members page.

## [Enabling team 2FA enforcement](#enabling-team-2fa-enforcement)

Before enabling 2FA enforcement for your team, you must have 2FA enabled on your own account. To prevent workflow disruptions, we recommend notifying your team members about the policy change beforehand.

Steps to follow:

1.  Go to Team Settings then Security & Privacy and scroll to Two-Factor Authentication Enforcement
2.  Toggle the switch to enforce 2FA
3.  Click the Save button to confirm the action

![Two-factor authentication enforcement team setting.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Ftwo-factor%2Fteam-2fa-enforcement-light.png&w=2048&q=75)![Two-factor authentication enforcement team setting.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Ftwo-factor%2Fteam-2fa-enforcement-dark.png&w=2048&q=75)

Two-factor authentication enforcement team setting.

--------------------------------------------------------------------------------
title: "Vercel Blob"
description: "Vercel Blob is a scalable, and cost-effective object storage service for static assets, such as images, videos, audio files, and more."
last_updated: "null"
source: "https://vercel.com/docs/vercel-blob"
--------------------------------------------------------------------------------

# Vercel Blob

Copy page

Ask AI about this page

Last updated September 24, 2025

Vercel Blob is available on [all plans](/docs/plans)

Those with the [owner, member, developer](/docs/rbac/access-roles#owner, member, developer-role) role can access this feature

## [Use cases](#use-cases)

[Vercel Blob](/storage/blob) is a great solution for storing [blobs](https://developer.mozilla.org/docs/Web/API/Blob) that need to be frequently read. Here are some examples suitable for Vercel Blob:

*   Files that are programmatically uploaded or generated at build time, for display and download such as avatars, screenshots, cover images and videos
*   Large files such as videos and audios to take advantage of the global network
*   Files that you would normally store in an external file storage solution like Amazon S3. With your project hosted on Vercel, you can readily access and manage these files with Vercel Blob

Stored files are referred to as "blobs" once they're in the storage system, following cloud storage terminology.

## [Getting started](#getting-started)

```
import { put } from '@vercel/blob';
 
const blob = await put('avatar.jpg', imageFile, {
  access: 'public',
});
```

You can create and manage your Vercel Blob stores from your [account dashboard](/dashboard) or the [Vercel CLI](/docs/cli/blob). You can create blob stores in any of the 19 [regions](/docs/regions#region-list) to optimize performance and meet data residency requirements. You can scope your Vercel Blob stores to your Hobby team or [team](/docs/accounts/create-a-team), and connect them to as many projects as you want.

To get started, see the [server-side](/docs/storage/vercel-blob/server-upload), or [client-side](/docs/storage/vercel-blob/client-upload) quickstart guides. Or visit the full API reference for the [Vercel Blob SDK](/docs/storage/vercel-blob/using-blob-sdk).

## [Using Vercel Blob in your workflow](#using-vercel-blob-in-your-workflow)

If you'd like to know whether or not Vercel Blob can be integrated into your workflow, it's worth knowing the following:

*   You can have one or more Vercel Blob stores per Vercel account
*   You can use multiple Vercel Blob stores in one Vercel project
*   Each Vercel Blob store can be accessed by multiple Vercel projects Vercel Blob URLs are publicly accessible, but you can make them [unguessable](/docs/vercel-blob/security).
*   To add to or remove from the content of a Blob store, a valid [token](/docs/storage/vercel-blob/using-blob-sdk#read-write-token) is required

### [Transferring to another project](#transferring-to-another-project)

If you need to transfer your blob store from one project to another project in the same or different team, review [Transferring your store](/docs/storage#transferring-your-store).

## [Viewing and downloading blobs](#viewing-and-downloading-blobs)

Each Blob is served with a `content-disposition` header. Based on the MIME type of the uploaded blob, it is either set to `attachment` (force file download) or `inline` (can render in a browser tab). This is done to prevent hosting specific files on `@vercel/blob` like HTML web pages. Your browser will automatically download the blob instead of displaying it for these cases.

Currently `text/plain`, `text/xml`, `application/json`, `application/pdf`, `image/*`, `audio/*` and `video/*` resolve to a `content-disposition: inline` header.

All other MIME types default to `content-disposition: attachment`.

If you need a blob URL that always forces a download you can use the `downloadUrl` property on the blob object. This URL always has the `content-disposition: attachment` header no matter its MIME type.

```
import { list } from '@vercel/blob';
 
export default async function Page() {
  const response = await list();
 
  return (
    <>
      {response.blobs.map((blob) => (
        <a key={blob.pathname} href={blob.downloadUrl}>
          {blob.pathname}
        </a>
      ))}
    </>
  );
}
```

Alternatively the SDK exposes a helper function called `getDownloadUrl` that returns the same URL.

## [Caching](#caching)

When you request a blob URL using a browser, the content is cached in two places:

1.  Your browser's cache
2.  Vercel's [cache](/docs/edge-cache)

Both caches store blobs for up to 1 month by default to ensure optimal performance when serving content. While both systems aim to respect this duration, blobs may occasionally expire earlier.

Vercel will cache blobs up to [512 MB](/docs/vercel-blob/usage-and-pricing#size-limits). Bigger blobs will always be served from the origin (your store).

### [Configuring cache duration](#configuring-cache-duration)

You can customize the caching duration using the `cacheControlMaxAge` option in the [`put()`](/docs/storage/vercel-blob/using-blob-sdk#put) and [`handleUpload`](/docs/storage/vercel-blob/using-blob-sdk#handleupload) methods.

The minimum configurable value is 60 seconds (1 minute). This represents the maximum time needed for our cache to update content behind a blob URL. For applications requiring faster updates, consider using a [Vercel function](/docs/functions) instead.

### [Important considerations when updating blobs](#important-considerations-when-updating-blobs)

When you delete or update (overwrite) a blob, the changes may take up to 60 seconds to propagate through our cache. However, browser caching presents additional challenges:

*   While our cache can update to serve the latest content, browsers will continue serving the cached version
*   To force browsers to fetch the updated content, add a unique query parameter to the blob URL:

```
<img
  src="https://1sxstfwepd7zn41q.public.blob.vercel-storage.com/blob-oYnXSVczoLa9yBYMFJOSNdaiiervF5.png?v=123456"
/>
```

For more information about updating existing blobs, see the [Overwriting blobs](#overwriting-blobs) section.

### [Best practice: Treat blobs as immutable](#best-practice:-treat-blobs-as-immutable)

For optimal performance and to avoid caching issues, consider treating blobs as immutable objects:

*   Instead of updating existing blobs, create new ones with different pathnames (or use `addRandomSuffix: true` option)
*   This approach avoids unexpected behaviors like outdated content appearing in your application

There are still valid use cases for mutable blobs with shorter cache durations, such as a single JSON file that's updated every 5 minutes with a top list of sales or other regularly refreshed data. For these scenarios, set an appropriate `cacheControlMaxAge` value and be mindful of caching behaviors.

## [Overwriting blobs](#overwriting-blobs)

By default, Vercel Blob prevents you from accidentally overwriting existing blobs by using the same pathname twice. When you attempt to upload a blob with a pathname that already exists, the operation will throw an error.

### [Using `allowOverwrite`](#using-allowoverwrite)

To explicitly allow overwriting existing blobs, you can use the `allowOverwrite` option:

```
const blob = await put('user-profile.jpg', imageFile, {
  access: 'public',
  allowOverwrite: true, // Enable overwriting an existing blob with the same pathname
});
```

This option is available in these methods:

*   `put()`
*   In client uploads via the `onBeforeGenerateToken()` function

### [When to use overwriting](#when-to-use-overwriting)

Overwriting blobs can be appropriate for certain use cases:

1.  Regularly updated files: For files that need to maintain the same URL but contain updated content (like JSON data files or configuration files)
2.  Content with predictable update patterns: For data that changes on a schedule and where consumers expect updates at the same URL

When overwriting blobs, be aware that due to [caching](#caching), changes won't be immediately visible. The minimum time for changes to propagate is 60 seconds, and browser caches may need to be explicitly refreshed.

### [Alternatives to overwriting](#alternatives-to-overwriting)

If you want to avoid overwriting existing content (recommended for most use cases), you have two options:

1.  Use `addRandomSuffix: true`: This automatically adds a unique random suffix to your pathnames:

```
const blob = await put('avatar.jpg', imageFile, {
  access: 'public',
  addRandomSuffix: true, // Creates a pathname like 'avatar-oYnXSVczoLa9yBYMFJOSNdaiiervF5.jpg'
});
```

1.  Generate unique pathnames programmatically: Create unique pathnames by adding timestamps, UUIDs, or other identifiers:

```
const timestamp = Date.now();
const blob = await put(`user-profile-${timestamp}.jpg`, imageFile, {
  access: 'public',
});
```

## [Blob Data Transfer](#blob-data-transfer)

Vercel Blob delivers content through a specialized network optimized for static assets:

*   Region-based distribution: Content is served from 19 regional hubs strategically located around the world
*   Optimized for non-critical assets: Well-suited for content "below the fold" that isn't essential for initial page rendering metrics like First Contentful Paint (FCP) or Largest Contentful Paint (LCP)
*   Cost-optimized for large assets: 3x more cost-efficient than [Fast Data Transfer](/docs/cdn) on average
*   Great for media delivery: Ideal for large media files like images, videos, and documents

While [Fast Data Transfer](/docs/manage-cdn-usage#fast-data-transfer) provides city-level, ultra-low latency, Blob Data Transfer prioritizes cost-efficiency for larger assets where ultra-low latency isn't essential.

Blob Data Transfer fees apply only to downloads (outbound traffic), not uploads. See [pricing documentation](/docs/vercel-blob/usage-and-pricing) for details.

## [Upload charges](#upload-charges)

Upload charges depend on your implementation method:

*   [Client Uploads](/docs/vercel-blob/client-upload): No data transfer charges for uploads
*   [Server Uploads](/docs/vercel-blob/server-upload): [Fast Data Transfer](/docs/manage-cdn-usage#fast-data-transfer) transfer charges apply when your Vercel application receives the file

## [SEO and search engine indexing](#seo-and-search-engine-indexing)

### [Search engine visibility of blobs](#search-engine-visibility-of-blobs)

While Vercel Blob URLs can be designed to be unique and unguessable (when using `addRandomSuffix: true`), they can still be indexed by search engines under certain conditions:

*   If you link to blob URLs from public webpages
*   If you embed blob content (images, PDFs, etc.) in indexed content
*   If you share blob URLs publicly, even in contexts outside your application

By default, Vercel Blob does not provide a `robots.txt` file or other indexing controls. This means search engines like Google may discover and index your blob content if they find links to it.

### [Preventing search engine indexing](#preventing-search-engine-indexing)

If you want to prevent search engines from indexing your blob content, you need to upload a `robots.txt` file directly to your blob store:

1.  Go to your [Storage page](https://vercel.com/d?to=%2F%5Bteam%5D%2F~%2Fstores&title=Go+to+Storage) and select your blob store
2.  Upload a `robots.txt` file to the root of your blob store with appropriate directives

Example `robots.txt` content to block all crawling of your blob store:

`User-agent: * Disallow: /`

### [Removing already indexed blob content](#removing-already-indexed-blob-content)

If your blob content has already been indexed by search engines:

1.  Verify your website ownership in [Google Search Console](https://search.google.com/search-console/)
2.  Upload a `robots.txt` file to your blob store as described above
3.  Use the "Remove URLs" tool in Google Search Console to request removal

## [Choosing your Blob store region](#choosing-your-blob-store-region)

You can create Blob stores in any of the 19 [regions](/docs/regions#region-list). Use the region selector in the dashboard at blob store creation time, or use the [CLI](/docs/cli/blob) with the `--region` option.

Select a region close to your customers and functions to minimize upload time. Region selection also helps meet data regulatory requirements. Vercel Blob [pricing](/docs/vercel-blob/usage-and-pricing) is regionalized, so check the pricing for your selected region.

You cannot change the region once the store is created.

## [Simple operations](#simple-operations)

Simple operations in Vercel Blob are specific read actions counted for billing purposes:

*   When the [`head()`](/docs/vercel-blob/using-blob-sdk#head) method is called to retrieve blob metadata
*   When a blob is accessed by its URL and it's a cache MISS

A cache MISS occurs when the blob is accessed for the first time or when its previously cached version has expired. Note that blob URL access resulting in a cache HIT does not count as a Simple Operation.

## [Advanced operations](#advanced-operations)

Advanced operations in Vercel Blob are write, copy, and listing actions counted for billing purposes:

*   When the [`put()`](/docs/vercel-blob/using-blob-sdk#put) method is called to upload a blob
*   When the [`upload()`](/docs/vercel-blob/using-blob-sdk#upload) method is used for client-side uploads
*   When the [`copy()`](/docs/vercel-blob/using-blob-sdk#copy) method is called to copy an existing blob
*   When the [`list()`](/docs/vercel-blob/using-blob-sdk#list) method is called to list blobs in your store

### [Dashboard usage counts as operations](#dashboard-usage-counts-as-operations)

Using the Vercel Blob file browser in your dashboard will count as operations. Each time you refresh the blob list, upload files through the dashboard, or view blob details, these actions use the same API methods that count toward your usage limits and billing.

Common dashboard actions that count as operations:

*   Refreshing the file browser: Uses `list()` to display your blobs
*   Uploading files via dashboard: Uses `put()` for each file uploaded
*   Viewing blob details: May trigger additional API calls
*   Navigating folders: Uses `list()` with different prefixes

If you notice unexpected increases in your operations count, check whether team members are browsing your blob store through the Vercel dashboard.

For [multipart uploads](#multipart-uploads), multiple advanced operations are counted:

*   One operation when starting the upload
*   One operation for each part uploaded
*   One operation for completing the upload

Delete operations using the [`del()`](/docs/vercel-blob/using-blob-sdk#del) are free of charge. They are considered advanced operations for [operation rate limits](/docs/vercel-blob/usage-and-pricing#operation-rate-limits) but not for billing.

## [Storage calculation](#storage-calculation)

Vercel Blob measures your storage usage by taking snapshots of your blob store size every 15 minutes and averages these measurements over the entire month to calculate your GB-month usage. This approach accounts for fluctuations in storage as blobs are added and removed, ensuring you're only billed for your actual usage over time, not peak usage.

The Vercel dashboard displays two metrics:

*   Latest value: The most recent measurement of your blob store size
*   Monthly average: The average of all measurements throughout the billing period (this is what you're billed for)

Example:

1.  Day 1: Upload a 2GB file → Store size: 2GB
2.  Day 15: Add 1GB file → Store size: 3GB
3.  Day 25: Delete 2GB file → Store size: 1GB

Month end billing:

*   Latest value: 1GB
*   Monthly average: ~2GB (billed amount)

If no changes occur in the following month (no new uploads or deletions), each 15-minute measurement would consistently show 1 GB. In this case, your next month's billing would be exactly 1 GB/month, as your monthly average would equal your latest value.

## [Multipart uploads](#multipart-uploads)

Vercel Blob supports [multipart uploads](/docs/vercel-blob/using-blob-sdk#multipart-uploads) for large files, which provides significant advantages when transferring substantial amounts of data.

Multipart uploads work by splitting large files into smaller chunks (parts) that are uploaded independently and then reassembled on the server. This approach offers several key benefits:

*   Improved upload reliability: If a network issue occurs during upload, only the affected part needs to be retried instead of restarting the entire upload
*   Better performance: Multiple parts can be uploaded in parallel, significantly increasing transfer speed
*   Progress tracking: More granular upload progress reporting as each part completes

We recommend using multipart uploads for files larger than 100 MB. Both the [`put()`](/docs/vercel-blob/using-blob-sdk#put) and [`upload()`](/docs/vercel-blob/using-blob-sdk#upload) methods handle all the complexity of splitting, uploading, and reassembling the file for you.

For billing purposes, multipart uploads count as multiple advanced operations:

*   One operation when starting the upload
*   One operation for each part uploaded
*   One operation for completing the upload

This approach ensures reliable handling of large files while maintaining the performance and efficiency expected from modern cloud storage solutions.

## [Durability and availability](#durability-and-availability)

Vercel Blob leverages [Amazon S3](https://aws.amazon.com/s3/) as its underlying storage infrastructure, providing industry-leading durability and availability:

*   Durability: Vercel Blob offers 99.999999999% (11 nines) durability. This means that even with one billion objects, you could expect to go a hundred years without losing a single one.
*   Availability: Vercel Blob provides 99.99% (4 nines) availability in a given year, ensuring that your data is accessible when you need it.

These guarantees are backed by [S3's robust architecture](https://docs.aws.amazon.com/AmazonS3/latest/userguide/DataDurability.html), which includes automatic replication and error correction mechanisms.

## [Folders and slashes](#folders-and-slashes)

Vercel Blob has folders support to organize your blobs:

```
const blob = await put('folder/file.txt', 'Hello World!', { access: 'public' });
```

The path `folder/file.txt` creates a folder named `folder` and a blob named `file.txt`. To list all blobs within a folder, use the [`list`](/docs/storage/vercel-blob/using-blob-sdk#list-blobs) function:

```
const listOfBlobs = await list({
  cursor,
  limit: 1000,
  prefix: 'folder/',
});
```

You don't need to create folders. Upload a file with a path containing a slash `/`, and Vercel Blob will interpret the slashes as folder delimiters.

In the Vercel Blob file browser on the Vercel dashboard, any pathname with a slash `/` is treated as a folder. However, these are not actual folders like in a traditional file system; they are used for organizing blobs in listings and the file browser.

## [Blob sorting and organization](#blob-sorting-and-organization)

Blobs are returned in lexicographical order by pathname (not creation date) when using [`list()`](/docs/vercel-blob/using-blob-sdk#list). Numbers are treated as characters, so `file10.txt` comes before `file2.txt`.

Sort by creation date: Include timestamps in pathnames:

```
const timestamp = new Date().toISOString().split('T')[0]; // YYYY-MM-DD
await put(`reports/${timestamp}-quarterly-report.pdf`, file, {
  access: 'public',
});
```

Use prefixes for search: Consider lowercase pathnames for consistent matching:

```
await put('user-uploads/avatar.jpg', file, { access: 'public' });
const userUploads = await list({ prefix: 'user-uploads/' });
```

For complex sorting, sort results client-side using `uploadedAt` or other properties.

## [More resources](#more-resources)

*   [Client Upload Quickstart](/docs/storage/vercel-blob/client-upload)
*   [Server Upload Quickstart](/docs/storage/vercel-blob/server-upload)
*   [Vercel Blob SDK](/docs/storage/vercel-blob/using-blob-sdk)
*   [Vercel Blob CLI](/docs/cli/blob)
*   [Vercel Blob Pricing](/docs/vercel-blob/usage-and-pricing)
*   [Vercel Blob Security](/docs/storage/vercel-blob/security)
*   [Vercel Blob Examples](/docs/storage/vercel-blob/examples)
*   [Observability](/docs/observability)

--------------------------------------------------------------------------------
title: "Client Uploads with Vercel Blob"
description: "Learn how to upload files larger than 4.5 MB directly from the browser to Vercel Blob"
last_updated: "null"
source: "https://vercel.com/docs/vercel-blob/client-upload"
--------------------------------------------------------------------------------

# Client Uploads with Vercel Blob

Copy page

Ask AI about this page

Last updated September 17, 2025

Vercel Blob is available on [all plans](/docs/plans)

Those with the [owner, member, developer](/docs/rbac/access-roles#owner, member, developer-role) role can access this feature

In this guide, you'll learn how to do the following:

*   Use the Vercel dashboard to create a Blob store connected to a project
*   Upload a file using the Blob SDK from a browser

## [Prerequisites](#prerequisites)

Vercel Blob works with any frontend framework. First, install the package:

pnpmyarnnpmbun

```
pnpm i @vercel/blob
```

1.  ### [Create a Blob store](#create-a-blob-store)
    
    Navigate to the [Project](/docs/projects/overview) you'd like to add the blob store to. Select the Storage tab, then select the Connect Database button.
    
    Under the Create New tab, select Blob and then the Continue button.
    
    Use the name "Images" and select Create a new Blob store. Select the environments where you would like the read-write token to be included. You can also update the prefix of the Environment Variable in Advanced Options
    
    Once created, you are taken to the Vercel Blob store page.
    
2.  ### [Prepare your local project](#prepare-your-local-project)
    
    Since you created the Blob store in a project, we automatically created and added the following Environment Variable to the project for you.
    
    *   `BLOB_READ_WRITE_TOKEN`
    
    To use this Environment Variable locally, we recommend pulling it with the Vercel CLI:
    
    ```
    vercel env pull
    ```
    

When you need to upload files larger than 4.5 MB, you can use client uploads. In this case, the file is sent directly from the client (a browser in this example) to Vercel Blob. This transfer is done securely as to not expose your Vercel Blob store to anonymous uploads. The security mechanism is based on a token exchange between your server and Vercel Blob.

1.  ### [Create a client upload page](#create-a-client-upload-page)
    
    This page allows to upload files to Vercel Blob. The files will go directly from the browser to Vercel Blob without going through your server.
    
    Behind the scenes, the upload is done securely by exchanging a token with your server before uploading the file.
    
    Next.js (/app)Next.js (/pages)Other frameworks
    
    src/app/avatar/upload/page.tsx
    
    TypeScript
    
    TypeScriptJavaScript
    
    ```
    'use client';
     
    import { type PutBlobResult } from '@vercel/blob';
    import { upload } from '@vercel/blob/client';
    import { useState, useRef } from 'react';
     
    export default function AvatarUploadPage() {
      const inputFileRef = useRef<HTMLInputElement>(null);
      const [blob, setBlob] = useState<PutBlobResult | null>(null);
      return (
        <>
          <h1>Upload Your Avatar</h1>
     
          <form
            onSubmit={async (event) => {
              event.preventDefault();
     
              if (!inputFileRef.current?.files) {
                throw new Error('No file selected');
              }
     
              const file = inputFileRef.current.files[0];
     
              const newBlob = await upload(file.name, file, {
                access: 'public',
                handleUploadUrl: '/api/avatar/upload',
              });
     
              setBlob(newBlob);
            }}
          >
            <input name="file" ref={inputFileRef} type="file" required />
            <button type="submit">Upload</button>
          </form>
          {blob && (
            <div>
              Blob url: <a href={blob.url}>{blob.url}</a>
            </div>
          )}
        </>
      );
    }
    ```
    
2.  ### [Create a client upload route](#create-a-client-upload-route)
    
    The responsibility of this client upload route is to:
    
    1.  Generate tokens for client uploads
    2.  Listen for completed client uploads, so you can update your database with the URL of the uploaded file for example
    
    The `@vercel/blob` npm package exposes a helper to implement said responsibilities.
    
    Next.js (/app)Next.js (/pages)Other frameworks
    
    src/app/api/avatar/upload/route.ts
    
    TypeScript
    
    TypeScriptJavaScript
    
    ```
    import { handleUpload, type HandleUploadBody } from '@vercel/blob/client';
    import { NextResponse } from 'next/server';
     
    export async function POST(request: Request): Promise<NextResponse> {
      const body = (await request.json()) as HandleUploadBody;
     
      try {
        const jsonResponse = await handleUpload({
          body,
          request,
          onBeforeGenerateToken: async (
            pathname,
            /* clientPayload */
          ) => {
            // Generate a client token for the browser to upload the file
            // Make sure to authenticate and authorize users before generating the token.
            // Otherwise, you're allowing anonymous uploads.
     
            return {
              allowedContentTypes: ['image/jpeg', 'image/png', 'image/webp'],
              addRandomSuffix: true,
              // callbackUrl: 'https://example.com/api/avatar/upload',
              // optional, `callbackUrl` is automatically computed when hosted on Vercel
              tokenPayload: JSON.stringify({
                // optional, sent to your server on upload completion
                // you could pass a user id from auth, or a value from clientPayload
              }),
            };
          },
          onUploadCompleted: async ({ blob, tokenPayload }) => {
            // Called by Vercel API on client upload completion
            // Use tools like ngrok if you want this to work locally
     
            console.log('blob upload completed', blob, tokenPayload);
     
            try {
              // Run any logic after the file upload completed
              // const { userId } = JSON.parse(tokenPayload);
              // await db.update({ avatar: blob.url, userId });
            } catch (error) {
              throw new Error('Could not update user');
            }
          },
        });
     
        return NextResponse.json(jsonResponse);
      } catch (error) {
        return NextResponse.json(
          { error: (error as Error).message },
          { status: 400 }, // The webhook will retry 5 times waiting for a 200
        );
      }
    }
    ```
    

## [Testing your page](#testing-your-page)

1.  ### [Run your application locally](#run-your-application-locally)
    
    Run your application locally and visit `/avatar/upload` to upload the file to your store. The browser will display the unique URL created for the file.
    
2.  ### [Review the Blob object metadata](#review-the-blob-object-metadata)
    
    *   Go to the Vercel Project where you created the store
    *   Select the Storage tab and select your new store
    *   Paste the blob object URL returned in the previous step in the Blob URL input box in the Browser section and select Lookup
    *   The following blob object metadata will be displayed: file name, path, size, uploaded date, content type and HTTP headers
    *   You also have the option to download and delete the file from this page

You have successfully uploaded an object to your Vercel Blob store and are able to review it's metadata, download, and delete it from your Vercel Storage Dashboard.

### [`onUploadCompleted` callback behavior](#onuploadcompleted-callback-behavior)

The `onUploadCompleted` callback is called by Vercel API when a client upload completes. For this to work, `@vercel/blob` computes the correct callback URL to call based on the environment variables of your project.

We use the following environment variables to compute the callback URL:

*   `VERCEL_BRANCH_URL` in preview environments
*   `VERCEL_URL` in preview environments where `VERCEL_BRANCH_URL` is not set
*   `VERCEL_PROJECT_PRODUCTION_URL` in production environments

These variables are automatically set by Vercel through [System Environment Variables](/docs/environment-variables/system-environment-variables). If you're not using System Environment Variables, use the `callbackUrl` option at the [`onBeforeGenerateToken`](/docs/vercel-blob/using-blob-sdk#onbeforegeneratetoken) step in `handleUpload`.

#### [Local development](#local-development)

When running your application locally, the `onUploadCompleted` callback will not work as Vercel Blob cannot contact your localhost. Instead, we recommend you run your local application through a tunneling service like [ngrok](https://ngrok.com/), so you can experience the full Vercel Blob development flow locally.

When using ngrok in local development, you can configure the domain to call for onUploadCompleted by using the `VERCEL_BLOB_CALLBACK_URL` environment variable in your [`.env.local` file](https://nextjs.org/docs/pages/guides/environment-variables) when using Next.js:

```
VERCEL_BLOB_CALLBACK_URL=https://abc123.ngrok-free.app
```

## [Next steps](#next-steps)

*   Learn how to [use the methods](/docs/storage/vercel-blob/using-blob-sdk) available with the `@vercel/blob` package

--------------------------------------------------------------------------------
title: "Vercel Blob examples"
description: "Examples on how to use Vercel Blob in your applications"
last_updated: "null"
source: "https://vercel.com/docs/vercel-blob/examples"
--------------------------------------------------------------------------------

# Vercel Blob examples

Copy page

Ask AI about this page

Last updated September 3, 2025

Vercel Blob is available on [all plans](/docs/plans)

Those with the [owner, member, developer](/docs/rbac/access-roles#owner, member, developer-role) role can access this feature

## [Range requests](#range-requests)

Vercel Blob supports [range requests](https://developer.mozilla.org/docs/Web/HTTP/Range_requests) for partial downloads. This means you can download only a portion of a blob, here are examples:

Terminal

```
# First 4 bytes
curl -r 0-3 https://1sxstfwepd7zn41q.public.blob.vercel-storage.com/pi.txt
# 3.14
 
# Last 5 bytes
curl -r -5 https://1sxstfwepd7zn41q.public.blob.vercel-storage.com/pi.txt
# 58151
 
# Bytes 3-6
curl -r 3-6 https://1sxstfwepd7zn41q.public.blob.vercel-storage.com/pi.txt
# 4159
```

## [Upload progress](#upload-progress)

You can track the upload progress when uploading blobs with the `onUploadProgress` callback:

```
const blob = await upload('big-file.mp4', file, {
  access: 'public',
  handleUploadUrl: '/api/upload',
  onUploadProgress: (progressEvent) => {
    console.log(`Loaded ${progressEvent.loaded} bytes`);
    console.log(`Total ${progressEvent.total} bytes`);
    console.log(`Percentage ${progressEvent.percentage}%`);
  },
});
```

`onUploadProgress` is available on `put` and `upload` methods.

## [Aborting requests](#aborting-requests)

Every Vercel Blob operation can be canceled, just like a fetch call. This is useful when you want to abort an ongoing operation, for example, when a user navigates away from a page or when the request takes too long.

```
const abortController = new AbortController();
 
try {
  const blobPromise = vercelBlob.put('hello.txt', 'Hello World!', {
    access: 'public',
    abortSignal: abortController.signal,
  });
 
  const timeout = setTimeout(() => {
    // Abort the request after 1 second
    abortController.abort();
  }, 1000);
 
  const blob = await blobPromise;
 
  console.info('blob put request completed', blob);
 
  clearTimeout(timeout);
 
  return blob.url;
} catch (error) {
  if (error instanceof vercelBlob.BlobRequestAbortedError) {
    // Handle the abort
    console.info('canceled put request');
  }
 
  // Handle other errors
}
```

## [Deleting all blobs](#deleting-all-blobs)

If you want to delete all the blobs in your store you can use the following code snippet to delete them in batches. This is useful if you have a lot of blobs and you want to avoid hitting the rate limits.

Either execute this code in a [Vercel Cron Job](/docs/cron-jobs), as a serverless function or on your local machine.

```
import { list, del, BlobServiceRateLimited } from '@vercel/blob';
import { setTimeout } from 'node:timers/promises';
 
async function deleteAllBlobs() {
  let cursor: string | undefined;
  let totalDeleted = 0;
 
  // Batch size to respect rate limits (conservative approach)
  const BATCH_SIZE = 100; // Conservative batch size
  const DELAY_MS = 1000; // 1 second delay between batches
 
  do {
    const listResult = await list({
      cursor,
      limit: BATCH_SIZE,
    });
 
    if (listResult.blobs.length > 0) {
      const batchUrls = listResult.blobs.map((blob) => blob.url);
 
      // Retry logic with exponential backoff
      let retries = 0;
      const maxRetries = 3;
 
      while (retries <= maxRetries) {
        try {
          await del(batchUrls);
          totalDeleted += listResult.blobs.length;
          console.log(
            `Deleted ${listResult.blobs.length} blobs (${totalDeleted} total)`,
          );
          break; // Success, exit retry loop
        } catch (error) {
          retries++;
 
          if (retries > maxRetries) {
            console.error(
              `Failed to delete batch after ${maxRetries} retries:`,
              error,
            );
            throw error; // Re-throw after max retries
          }
 
          // Exponential backoff: wait longer with each retry
          let backoffDelay = 2 ** retries * 1000;
 
          if (error instanceof BlobServiceRateLimited) {
            backoffDelay = error.retryAfter * 1000;
          }
 
          console.warn(
            `Retry ${retries}/${maxRetries} after ${backoffDelay}ms delay`,
          );
 
          await setTimeout(backoffDelay);
        }
 
        await setTimeout(DELAY_MS);
      }
    }
 
    cursor = listResult.cursor;
  } while (cursor);
 
  console.log(`All blobs were deleted. Total: ${totalDeleted}`);
}
 
deleteAllBlobs().catch((error) => {
  console.error('An error occurred:', error);
});
```

## [Backups](#backups)

While there's no native backup system for Vercel Blob, here are two ways to backup your blobs:

1.  Continuous backup: When using [Client Uploads](/docs/storage/vercel-blob/using-blob-sdk#client-uploads) you can leverage the `onUploadCompleted` callback from the `handleUpload` server-side function to save every Blob upload to another storage.
2.  Periodic backup: Using [Cron Jobs](/docs/cron-jobs) and the [Vercel Blob SDK](/docs/storage/vercel-blob/using-blob-sdk) you can periodically list all blobs and save them.

Here's an example implementation of a periodic backup as a Cron Job:

```
import { Readable } from 'node:stream';
import { S3Client } from '@aws-sdk/client-s3';
import { list } from '@vercel/blob';
import { Upload } from '@aws-sdk/lib-storage';
import type { NextRequest } from 'next/server';
import type { ReadableStream } from 'node:stream/web';
 
export async function GET(request: NextRequest) {
  const authHeader = request.headers.get('authorization');
  if (authHeader !== `Bearer ${process.env.CRON_SECRET}`) {
    return new Response('Unauthorized', {
      status: 401,
    });
  }
 
  const s3 = new S3Client({
    region: 'us-east-1',
  });
 
  let cursor: string | undefined;
 
  do {
    const listResult = await list({
      cursor,
      limit: 250,
    });
 
    if (listResult.blobs.length > 0) {
      await Promise.all(
        listResult.blobs.map(async (blob) => {
          const res = await fetch(blob.url);
          if (res.body) {
            const parallelUploads3 = new Upload({
              client: s3,
              params: {
                Bucket: 'vercel-blob-backup',
                Key: blob.pathname,
                Body: Readable.fromWeb(res.body as ReadableStream),
              },
              leavePartsOnError: false,
            });
 
            await parallelUploads3.done();
          }
        }),
      );
    }
 
    cursor = listResult.cursor;
  } while (cursor);
 
  return new Response('Backup done!');
}
```

This script optimizes the process by streaming the content directly from Vercel Blob to the backup storage, avoiding buffering all the content into memory.

You can split your backup process into smaller chunks if you're hitting an execution limit. In this case you would save the `cursor` to a database and resume the backup process from where it left off.

--------------------------------------------------------------------------------
title: "Security"
description: "Learn how your Vercel Blob store is secured"
last_updated: "null"
source: "https://vercel.com/docs/vercel-blob/security"
--------------------------------------------------------------------------------

# Security

Copy page

Ask AI about this page

Last updated September 24, 2025

Vercel Blob is available on [all plans](/docs/plans)

Those with the [owner, member, developer](/docs/rbac/access-roles#owner, member, developer-role) role can access this feature

Vercel Blob URLs, although publicly accessible, are unique and hard to guess when you use the `addRandomSuffix: true` option. They consist of a unique store id, a pathname, and a unique random blob id generated when the blob is created.

This is similar to [Share a file publicly](https://support.google.com/drive/answer/2494822?hl=en&co=GENIE.Platform%3DDesktop#zippy=%2Cshare-a-file-publicly) in Google Docs. You should ensure that the URLs are only shared to authorized users

Headers that enhance security by preventing unauthorized downloads, blocking external content from being embedded, and protecting against malicious file type manipulation, are enforced on each blob. They are:

*   `content-security-policy`: `default-src "none"`
*   `x-frame-options`: `DENY`
*   `x-content-type-options`: `nosniff`
*   `content-disposition`: `attachment/inline; filename="filename.extension"`

### [Encryption](#encryption)

All files stored on Vercel Blob are secured using AES-256 encryption. This encryption process is applied at rest and is transparent, ensuring that files are encrypted before being saved to the disk and decrypted upon retrieval.

### [Firewall and WAF integration](#firewall-and-waf-integration)

Vercel Blob is protected by Vercel's [platform-wide firewall](/docs/vercel-firewall#platform-wide-firewall) which provides DDoS mitigation and blocks abnormal or suspicious levels of incoming requests.

Vercel Blob does not currently support [Vercel WAF](/docs/vercel-firewall/vercel-waf). If you need WAF rules on your blob URLs, consider using a [Vercel function](/docs/functions) to proxy the blob URL. This approach may introduce some latency to your requests but will enable the use of WAF rules on the blob URLs.

--------------------------------------------------------------------------------
title: "Server Uploads with Vercel Blob"
description: "Learn how to upload files to Vercel Blob using Server Actions and Route Handlers"
last_updated: "null"
source: "https://vercel.com/docs/vercel-blob/server-upload"
--------------------------------------------------------------------------------

# Server Uploads with Vercel Blob

Copy page

Ask AI about this page

Last updated October 23, 2025

Vercel Blob is available on [all plans](/docs/plans)

Those with the [owner, member, developer](/docs/rbac/access-roles#owner, member, developer-role) role can access this feature

In this guide, you'll learn how to do the following:

*   Use the Vercel dashboard to create a Blob store connected to a project
*   Upload a file using the Blob SDK from the server

Vercel has a [4.5 MB request body size limit](/docs/functions/runtimes#request-body-size) on Vercel Functions. If you need to upload larger files, use [client uploads](/docs/storage/vercel-blob/client-upload).

## [Prerequisites](#prerequisites)

Vercel Blob works with any frontend framework. First, install the package:

TypeScriptPython

pnpmyarnnpmbun

```
pnpm i @vercel/blob
```

1.  ### [Create a Blob store](#create-a-blob-store)
    
    Navigate to the [Project](/docs/projects/overview) you'd like to add the blob store to. Select the Storage tab, then select the Connect Database button.
    
    Under the Create New tab, select Blob and then the Continue button.
    
    Use the name "Images" and select Create a new Blob store. Select the environments where you would like the read-write token to be included. You can also update the prefix of the Environment Variable in Advanced Options
    
    Once created, you are taken to the Vercel Blob store page.
    
2.  ### [Prepare your local project](#prepare-your-local-project)
    
    Since you created the Blob store in a project, we automatically created and added the following Environment Variable to the project for you.
    
    *   `BLOB_READ_WRITE_TOKEN`
    
    To use this Environment Variable locally, we recommend pulling it with the Vercel CLI:
    
    ```
    vercel env pull
    ```
    

Server uploads are perfectly fine as long as you do not need to upload files larger than [4.5 MB on Vercel](/docs/functions/runtimes#request-body-size). If you need to upload larger files, consider using [client uploads](/docs/storage/vercel-blob/client-upload).

## [Upload a file using Server Actions](#upload-a-file-using-server-actions)

TypeScriptPython

The following example shows how to use a [Server Action](https://nextjs.org/docs/app/building-your-application/data-fetching/server-actions-and-mutations) with Next.js App Router to upload a file to Vercel Blob.

app/components/form.tsx

```
import { put } from '@vercel/blob';
import { revalidatePath } from 'next/cache';
 
export async function Form() {
  async function uploadImage(formData: FormData) {
    'use server';
    const imageFile = formData.get('image') as File;
    const blob = await put(imageFile.name, imageFile, {
      access: 'public',
      addRandomSuffix: true,
    });
    revalidatePath('/');
    return blob;
  }
 
  return (
    <form action={uploadImage}>
      <label htmlFor="image">Image</label>
      <input
        type="file"
        id="image"
        name="image"
        accept="image/jpeg, image/png, image/webp"
        required
      />
      <button>Upload</button>
    </form>
  );
}
```

Then, add the hostname to your `next.config.js` file including the store id from the dashboard:

next.config.js

```
/** @type {import('next').NextConfig} */
const nextConfig = {
  images: {
    remotePatterns: [
      new URL('https://my-store-id.public.blob.vercel-storage.com/**'),
    ],
  },
};
 
module.exports = nextConfig;
```

This will allow you to use [`next/image`](https://nextjs.org/docs/app/api-reference/components/image) to display images from your Vercel Blob store.

app/components/images.tsx

```
import { list } from '@vercel/blob';
import Image from 'next/image';
 
export async function Images() {
  const { blobs } = await list();
 
  return (
    <section>
      {blobs.map((image, i) => (
        <Image
          priority={i < 2}
          key={image.pathname}
          src={image.url}
          alt="My Image"
          width={200}
          height={200}
        />
      ))}
    </section>
  );
}
```

Read more about [Server Actions](https://nextjs.org/docs/app/building-your-application/data-fetching/server-actions-and-mutations) and [App Router](https://nextjs.org/docs) on the Next.js documentation.

## [Upload a file using a server upload page and route](#upload-a-file-using-a-server-upload-page-and-route)

You can upload files to Vercel Blob using Route Handlers/API Routes. The following example shows how to upload a file to Vercel Blob using a server upload page and route.

1.  ### [Create a server upload page](#create-a-server-upload-page)
    
    This page will upload files to your server. The files will then be sent to Vercel Blob.
    
    TypeScriptPython
    
    Next.js (/app)Next.js (/pages)
    
    src/app/avatar/upload/page.tsx
    
    TypeScript
    
    TypeScriptJavaScript
    
    ```
    'use client';
     
    import type { PutBlobResult } from '@vercel/blob';
    import { useState, useRef } from 'react';
     
    export default function AvatarUploadPage() {
      const inputFileRef = useRef<HTMLInputElement>(null);
      const [blob, setBlob] = useState<PutBlobResult | null>(null);
      return (
        <>
          <h1>Upload Your Avatar</h1>
     
          <form
            onSubmit={async (event) => {
              event.preventDefault();
     
              if (!inputFileRef.current?.files) {
                throw new Error('No file selected');
              }
     
              const file = inputFileRef.current.files[0];
     
              const response = await fetch(
                `/api/avatar/upload?filename=${file.name}`,
                {
                  method: 'POST',
                  body: file,
                },
              );
     
              const newBlob = (await response.json()) as PutBlobResult;
     
              setBlob(newBlob);
            }}
          >
            <input
              name="file"
              ref={inputFileRef}
              type="file"
              accept="image/jpeg, image/png, image/webp"
              required
            />
            <button type="submit">Upload</button>
          </form>
          {blob && (
            <div>
              Blob url: <a href={blob.url}>{blob.url}</a>
            </div>
          )}
        </>
      );
    }
    ```
    
2.  ### [Create a server upload route](#create-a-server-upload-route)
    
    This route forwards the file to Vercel Blob and returns the URL of the uploaded file to the browser.
    
    TypeScriptPython
    
    Next.js (/app)Next.js (/pages)
    
    src/app/api/avatar/upload/route.ts
    
    TypeScript
    
    TypeScriptJavaScript
    
    ```
    import { put } from '@vercel/blob';
    import { NextResponse } from 'next/server';
     
    export async function POST(request: Request): Promise<NextResponse> {
      const { searchParams } = new URL(request.url);
      const filename = searchParams.get('filename');
     
      const blob = await put(filename, request.body, {
        access: 'public',
        addRandomSuffix: true,
      });
     
      return NextResponse.json(blob);
    }
    ```
    

### [Testing your page](#testing-your-page)

1.  ### [Run your application locally](#run-your-application-locally)
    
    Run your application locally and visit `/avatar/upload` to upload the file to your store. The browser will display the unique URL created for the file.
    
2.  ### [Review the Blob object metadata](#review-the-blob-object-metadata)
    
    *   Go to the Vercel Project where you created the store
    *   Select the Storage tab and select your new store
    *   Paste the blob object URL returned in the previous step in the Blob URL input box in the Browser section and select Lookup
    *   The following blob object metadata will be displayed: file name, path, size, uploaded date, content type and HTTP headers
    *   You also have the option to download and delete the file from this page

You have successfully uploaded an object to your Vercel Blob store and are able to review it's metadata, download, and delete it from your Vercel Storage Dashboard.

## [Next steps](#next-steps)

*   Learn how to [use the methods](/docs/storage/vercel-blob/using-blob-sdk) available with the `@vercel/blob` package

--------------------------------------------------------------------------------
title: "Vercel Blob Pricing"
description: "Learn about the pricing for Vercel Blob."
last_updated: "null"
source: "https://vercel.com/docs/vercel-blob/usage-and-pricing"
--------------------------------------------------------------------------------

# Vercel Blob Pricing

Copy page

Ask AI about this page

Last updated September 24, 2025

Vercel Blob is available on [all plans](/docs/plans)

Those with the [owner, member, developer](/docs/rbac/access-roles#owner, member, developer-role) role can access this feature

## [Usage](#usage)

Vercel Blob usage is measured based on the following:

*   Storage Size: Monthly average of your blob store size (GB-month)
*   Simple Operations: Counts when a blob is accessed by its URL and it's a cache MISS or when using the [`head()`](/docs/vercel-blob/using-blob-sdk#head) method
*   Advanced Operations: Counts when using [`put()`](/docs/vercel-blob/using-blob-sdk#put), [`copy()`](/docs/vercel-blob/using-blob-sdk#copy), or [`list()`](/docs/vercel-blob/using-blob-sdk#list) methods
*   Blob Data Transfer: Charged when blobs are downloaded or viewed
*   [Edge Requests](/docs/pricing/networking#edge-requests): Each blob access by its URL counts as one Edge Request, regardless if it's a MISS or HIT
*   [Fast Origin Transfer](/docs/pricing/networking#fast-origin-transfer): Applied only for cache MISS scenarios

See the [usage details](#usage-details) and [pricing example](#pricing-example) sections for more information on how usage is calculated.

Stored files are referred to as "blobs" once they're in the storage system, following cloud storage terminology.

## [Pricing](#pricing)

Select a Region

Cape Town, South Africa (cpt1)Cleveland, USA (cle1)Dubai, UAE (dxb1)Dublin, Ireland (dub1)Frankfurt, Germany (fra1)Hong Kong (hkg1)London, UK (lhr1)Mumbai, India (bom1)Osaka, Japan (kix1)Paris, France (cdg1)Portland, USA (pdx1)San Francisco, USA (sfo1)São Paulo, Brazil (gru1)Seoul, South Korea (icn1)Singapore (sin1)Stockholm, Sweden (arn1)Sydney, Australia (syd1)Tokyo, Japan (hnd1)Washington, D.C., USA (iad1)

Managed Infrastructure pricing
| 
Resource

 | 

Hobby Included

 | 

On-demand Rates

 |
| --- | --- | --- |
| 

[Blob Storage Size](/docs/vercel-blob/usage-and-pricing#pricing)

 | 1GB/month | $0.023 per GB |
| 

[Blob Simple Operations](/docs/vercel-blob/usage-and-pricing#pricing)

 | First 10,000 | $0.400 per 1M |
| 

[Blob Advanced Operations](/docs/vercel-blob/usage-and-pricing#pricing)

 | First 2,000 | $5.000 per 1M |
| 

[Blob Data Transfer](/docs/vercel-blob/usage-and-pricing#pricing)

 | First 10 GB | $0.050 per GB |

  

[Edge Requests](/docs/pricing/networking#edge-requests) and [Fast Origin Transfer](/docs/pricing/networking#fast-origin-transfer) for blobs are billed at standard [CDN rates](/docs/cdn#pricing). The included resource usage for the Hobby plan is shared across all Vercel services in your project.

## [Usage details](#usage-details)

*   Cache HITs do not count as Simple Operations
*   Cache HITs do not incur Fast Origin Transfer charges
*   The maximum size of a blob in cache is [512 MB](/usage-and-pricing#size-limits). Any blob larger than this will generate a cache MISS on every access, resulting in a Fast Origin Transfer and Edge Request charge each time it is accessed
*   Uploads do not incur data transfer charges when using [Client Uploads](/docs/vercel-blob/client-upload)
*   Uploads incur [Fast Data Transfer](/docs/manage-cdn-usage#fast-data-transfer) charges when using [Server Uploads](/docs/vercel-blob/server-upload) if your Vercel application is the one receiving the file upload
*   [Multipart uploads](/docs/vercel-blob/using-blob-sdk#multipart-uploads) count as multiple Advanced Operations: one when starting, one per part, one for completion
*   [`del()`](/docs/vercel-blob/using-blob-sdk#del) operations are free
*   Dashboard interactions count as operations: Each time you interact with the Vercel dashboard to browse your blob store, upload files, or view blob details, these actions count as Advanced Operations and will appear in your usage metrics.

## [Hobby](#hobby)

Vercel Blob is free for Hobby users within the [usage limits](#pricing).

Vercel will send you emails as you are nearing your usage limits. You will not pay for any additional usage. However, you will not be able to access Vercel Blob if limits are exceeded. In this scenario, you will have to wait until 30 days have passed before using Blob storage again.

## [Pro](#pro)

You pay for usage using your [monthly credit allocation](/docs/plans/pro-plan#credit-and-usage-allocation) which switches to on-demand once you have used your included credits.

Pro teams can [set up Spend Management](/docs/spend-management#managing-your-spend-amount) to get notified or to automatically take action, such as [using a webhook](/docs/spend-management#configuring-a-webhook) or pausing your projects when your usage hits a set spend amount.

## [Enterprise](#enterprise)

Vercel Blob is available for all Enterprise teams at the same price as Pro. Contact your account team for pricing or support questions.

## [Pricing Example](#pricing-example)

Let's say during one month of usage, you upload 120,000 blobs of which 30% (36,000 blobs) are uploaded using multipart uploads with 5 parts each. Your storage averages 50 GB and your blobs are downloaded 2.5 million times, with a 70% cache HIT ratio (meaning 30% or 750,000 downloads are cache MISSes), for a total of 350 GB of data transfer.

Here's the cost breakdown:

*   Storage: 50 GB total - 5 GB included = 45 GB extra at $0.023/GB = $1.04
*   Simple Operations: 750K (30% cache MISSes of 2.5M downloads + head calls) - 100K included = 650K extra at $0.40/1M = $0.26
*   Advanced Operations:
    *   Single uploads: 84K (70% of 120K blobs)
    *   Multipart uploads: 36K × (1 start + 5 parts + 1 completion) = 252K operations
    *   Total: 336K - 10K included = 326K extra at $5.00/1M = $1.63
*   Data Transfer (iad1): 350 GB total - 100 GB included = 250 GB extra at $0.050/GB = $12.50
*   Edge Requests: 2.5M requests (all downloads) - 10M included = $0.00
*   Fast Origin Transfer (iad1): 105 GB (30% cache MISSes of 350 GB) - 100 GB included = 5 GB extra at $0.06/GB = $0.30

Total: $15.73/month

## [Limits](#limits)

Vercel Blob has certain [limits](/docs/limits) that you should be aware of when designing your application.

### [Operation rate limits](#operation-rate-limits)

| Plan | Simple Operations | Advanced Operations |
| --- | --- | --- |
| Hobby | 1,200/min (20/s) | 900/min (15/s) |
| Pro | 7,200/min (120/s) | 4,500/min (75/s) |
| Enterprise | 9,000/min (150/s) | 7,500/min (125/s) |

Note: Rate limits are based on the number of operations, not HTTP requests. For example, when using `del([pathnames])` to delete multiple blobs in one call, each blob deletion counts as a separate operation toward your rate limit. Deleting 100 blobs in a batch counts as 100 operations, not one.

### [Size limits](#size-limits)

*   Cache Size Limit: 512 MB per blob
    
    *   Blobs larger than 512 MB will not be cached
    *   Accessing these blobs will always count as a cache MISS (generating one [Simple Operation](/docs/vercel-blob#simple-operations))
    *   These large blobs will also incur [Fast Origin Transfer](/docs/manage-cdn-usage#fast-origin-transfer) charges for each access
*   Maximum File Size: 5TB (5,000GB)
    
    *   This is the absolute maximum size for any individual file uploaded to Vercel Blob
    *   For files larger than 100MB, we recommend using [multipart uploads](/docs/vercel-blob#multipart-uploads)

## [Observability](#observability)

You can monitor and analyze your Vercel Blob usage with the [Observability tab](https://vercel.com/d?to=%2F%5Bteam%5D%2F~%2Fobservability%2Fblob&title=Go+to+Blob+Observability) in the Vercel Dashboard.

--------------------------------------------------------------------------------
title: "@vercel/blob"
description: "Learn how to use the Vercel Blob SDK to access your blob store from your apps."
last_updated: "null"
source: "https://vercel.com/docs/vercel-blob/using-blob-sdk"
--------------------------------------------------------------------------------

# @vercel/blob

Copy page

Ask AI about this page

Last updated October 23, 2025

Vercel Blob is available on [all plans](/docs/plans)

Those with the [owner, member, developer](/docs/rbac/access-roles#owner, member, developer-role) role can access this feature

## [Getting started](#getting-started)

To start using [Vercel Blob](/storage/blob) SDK, follow the steps below:

You can also interact with Vercel Blob using the [Vercel CLI](/docs/cli/blob) for command-line operations. For example, you might want to quickly upload assets during local development without writing additional code.

Vercel Blob works with any frontend framework. begin by installing the package:

TypeScriptPython

pnpmyarnnpmbun

```
pnpm i @vercel/blob
```

1.  ### [Create a Blob store](#create-a-blob-store)
    
    Navigate to the [Project](/docs/projects/overview) you'd like to add the blob store to. Select the Storage tab, then select the Connect Database button.
    
    Under the Create New tab, select Blob and then the Continue button.
    
    Choose a name for your store and select Create a new Blob store. Select the environments where you would like the read-write token to be included. You can also update the prefix of the Environment Variable in Advanced Options
    
    Once created, you are taken to the Vercel Blob store page.
    
2.  ### [Prepare your local project](#prepare-your-local-project)
    
    Since you created the Blob store in a project, environment variables are automatically created and added to the project for you.
    
    *   `BLOB_READ_WRITE_TOKEN`
    
    To use this environment variable locally, use the Vercel CLI to [pull the values into your local project](/docs/cli/env#exporting-development-environment-variables):
    
    ```
    vercel env pull
    ```
    

## [Read-write token](#read-write-token)

A read-write token is required to interact with the Blob SDK. When you create a Blob store in your Vercel Dashboard, an environment variable with the value of the token is created for you. You have the following options when deploying your application:

*   If you deploy your application in the same Vercel project where your Blob store is located, you _do not_ need to specify the `token` parameter, as it's default value is equal to the store's token environment variable
*   If you deploy your application in a different Vercel project or scope, you can create an environment variable there and assign the token value from your Blob store settings to this variable. You will then set the `token` parameter to this environment variable
*   If you deploy your application outside of Vercel, you can copy the `token` value from the store settings and pass it as the `token` parameter when you call a Blob SDK method

## [Using the SDK methods](#using-the-sdk-methods)

In the examples below, we use [Fluid compute](/docs/fluid-compute) for optimal performance and scalability.

## [Upload a blob](#upload-a-blob)

This example creates a Function that accepts a file from a `multipart/form-data` form and uploads it to the Blob store. The function returns a unique URL for the blob.

TypeScriptPython

Next.js (/app)Next.js (/pages)Other frameworks

app/upload/route.ts

TypeScript

TypeScriptJavaScript

```
import { put } from '@vercel/blob';
 
export async function PUT(request: Request) {
  const form = await request.formData();
  const file = form.get('file') as File;
  const blob = await put(file.name, file, {
    access: 'public',
    addRandomSuffix: true,
  });
 
  return Response.json(blob);
}
```

### [`put()`](#put)

The `put` method uploads a blob object to the Blob store.

TypeScriptPython

```
put(pathname, body, options);
```

It accepts the following parameters:

*   `pathname`: (Required) A string specifying the base value of the return URL
*   `body`: (Required) A blob object as `ReadableStream`, `String`, `ArrayBuffer` or `Blob` based on these [supported body types](https://developer.mozilla.org/docs/Web/API/fetch#body)
*   `options`: (Required) A `JSON` object with the following required and optional parameters:

| Parameter | Required | Values |
| --- | --- | --- |
| `access` | Yes | `public` |
| `addRandomSuffix` | No | A boolean specifying whether to add a random suffix to the `pathname`. It defaults to `false`. We recommend using this option to ensure there are no conflicts in your blob filenames. |
| `allowOverwrite` | No | A boolean to allow overwriting blobs. By default an error will be thrown if you try to overwrite a blob by using the same `pathname` for multiple blobs. |
| `cacheControlMaxAge` | No | A number in seconds to configure how long Blobs are cached. Defaults to one month. Cannot be set to a value lower than 1 minute. See the [caching](/docs/storage/vercel-blob#caching) documentation for more details. |
| `contentType` | No | A string indicating the [media type](https://developer.mozilla.org/docs/Web/HTTP/Headers/Content-Type). By default, it's extracted from the pathname's extension. |
| `token` | No | A string specifying the token to use when making requests. It defaults to `process.env.BLOB_READ_WRITE_TOKEN` when deployed on Vercel as explained in [Read-write token](#read-write-token). You can also pass a client token created with the `generateClientTokenFromReadWriteToken` method |
| `multipart` | No | Pass `multipart: true` when uploading large files. It will split the file into multiple parts, upload them in parallel and retry failed parts. |
| `abortSignal` | No | An [AbortSignal](https://developer.mozilla.org/en-US/docs/Web/API/AbortSignal) to cancel the operation |
| `onUploadProgress` | No | Callback to track upload progress: `onUploadProgress({loaded: number, total: number, percentage: number})` |

#### [Example code with folder output](#example-code-with-folder-output)

To upload your file to an existing [folder](#folders) inside your blob storage, pass the folder name in the `pathname` as shown below:

TypeScriptPython

```
const imageFile = formData.get('image') as File;
const blob = await put(`existingBlobFolder/${imageFile.name}`, imageFile, {
  access: 'public',
  addRandomSuffix: true,
});
```

#### [Example responses](#example-responses)

`put()` returns a `JSON` object with the following data for the created blob object:

```
{
  "pathname": "string",
  "contentType": "string",
  "contentDisposition": "string",
  "url": "string",
  "downloadUrl": "string"
}
```

An example blob (uploaded with `addRandomSuffix: true`) is:

```
{
  "pathname": "profilesv1/user-12345-NoOVGDVcqSPc7VYCUAGnTzLTG2qEM2.txt",
  "contentType": "text/plain",
  "contentDisposition": "attachment; filename=\"user-12345-NoOVGDVcqSPc7VYCUAGnTzLTG2qEM2.txt\"",
  "url": "https://ce0rcu23vrrdzqap.public.blob.vercel-storage.com/profilesv1/user-12345-NoOVGDVcqSPc7VYCUAGnTzLTG2qEM2.txt",
  "downloadUrl": "https://ce0rcu23vrrdzqap.public.blob.vercel-storage.com/profilesv1/user-12345-NoOVGDVcqSPc7VYCUAGnTzLTG2qEM2.txt?download=1"
}
```

An example blob uploaded without `addRandomSuffix: true` (default) is:

```
{
  "pathname": "profilesv1/user-12345.txt",
  "contentType": "text/plain",
  "contentDisposition": "attachment; filename=\"user-12345.txt\"",
  // no automatic random suffix added 👇
  "url": "https://ce0rcu23vrrdzqap.public.blob.vercel-storage.com/profilesv1/user-12345.txt",
  "downloadUrl": "https://ce0rcu23vrrdzqap.public.blob.vercel-storage.com/profilesv1/user-12345.txt?download=1"
}
```

## [Multipart Uploads](#multipart-uploads)

When uploading large files you should use multipart uploads to have a more reliable upload process. A multipart upload splits the file into multiple parts, uploads them in parallel and retries failed parts. This process consists of three phases: creating a multipart upload, uploading the parts and completing the upload. `@vercel/blob` offers three different ways to create multipart uploads:

### [Automatic](#automatic)

This method has everything baked in and is easiest to use. It's part of the `put` and `upload` API's. Under the hood it will start the upload, split your file into multiple parts with the same size, upload them in parallel and complete the upload.

TypeScriptPython

```
const blob = await put('large-movie.mp4', file, {
  access: 'public',
  multipart: true,
});
```

### [Manual](#manual)

This method gives you full control over the multipart upload process. It consists of three phases:

Phase 1: Create a multipart upload

TypeScriptPython

```
const multipartUpload = await createMultipartUpload(pathname, options);
```

`createMultipartUpload` accepts the following parameters:

*   `pathname`: (Required) A string specifying the path inside the blob store. This will be the base value of the return URL and includes the filename and extension.
*   `options`: (Required) A `JSON` object with the following required and optional parameters:

| Parameter | Required | Values |
| --- | --- | --- |
| `access` | Yes | `public` |
| `contentType` | No | The [media type](https://developer.mozilla.org/docs/Web/HTTP/Headers/Content-Type) for the file. If not specified, it's derived from the file extension. Falls back to `application/octet-stream` when no extension exists or can't be matched. |
| `token` | No | A string specifying the token to use when making requests. It defaults to `process.env.BLOB_READ_WRITE_TOKEN` when deployed on Vercel as explained in [Read-write token](#read-write-token). You can also pass a client token created with the `generateClientTokenFromReadWriteToken` method |
| `addRandomSuffix` | No | A boolean specifying whether to add a random suffix to the pathname. It defaults to `true`. |
| `cacheControlMaxAge` | No | A number in seconds to configure the edge and browser cache. Defaults to one year. See the [caching](/docs/storage/vercel-blob#caching) documentation for more details. |
| `abortSignal` | No | An [AbortSignal](https://developer.mozilla.org/en-US/docs/Web/API/AbortSignal) to cancel the operation |

`createMultipartUpload()` returns a `JSON` object with the following data for the created upload:

```
{
  "key": "string",
  "uploadId": "string"
}
```

Phase 2: Upload all the parts

In the multipart uploader process, it's necessary for you to manage both memory usage and concurrent upload requests. Additionally, each part must be a minimum of 5MB, except the last one which can be smaller, and all parts should be of equal size.

TypeScriptPython

```
const part = await uploadPart(pathname, chunkBody, options);
```

`uploadPart` accepts the following parameters:

*   `pathname`: (Required) Same value as the `pathname` parameter passed to `createMultipartUpload`
*   `chunkBody`: (Required) A blob object as `ReadableStream`, `String`, `ArrayBuffer` or `Blob` based on these [supported body types](https://developer.mozilla.org/docs/Web/API/fetch#body)
*   `options`: (Required) A `JSON` object with the following required and optional parameters:

| Parameter | Required | Values |
| --- | --- | --- |
| `access` | Yes | `public` |
| `partNumber` | Yes | A number identifying which part is uploaded |
| `key` | Yes | A string returned from `createMultipartUpload` which identifies the blob object |
| `uploadId` | Yes | A string returned from `createMultipartUpload` which identifies the multipart upload |
| `token` | No | A string specifying the token to use when making requests. It defaults to `process.env.BLOB_READ_WRITE_TOKEN` when deployed on Vercel as explained in [Read-write token](#read-write-token). You can also pass a client token created with the `generateClientTokenFromReadWriteToken` method |
| `abortSignal` | No | An [AbortSignal](https://developer.mozilla.org/en-US/docs/Web/API/AbortSignal) to cancel the operation |

`uploadPart()` returns a `JSON` object with the following data for the uploaded part:

```
{
  "etag": "string",
  "partNumber": "string"
}
```

Phase 3: Complete the multipart upload

TypeScriptPython

```
const blob = await completeMultipartUpload(pathname, parts, options);
```

`completeMultipartUpload` accepts the following parameters:

*   `pathname`: (Required) Same value as the `pathname` parameter passed to `createMultipartUpload`
*   `parts`: (Required) An array containing all the uploaded parts
*   `options`: (Required) A `JSON` object with the following required and optional parameters:

| Parameter | Required | Values |
| --- | --- | --- |
| `access` | Yes | `public` |
| `key` | Yes | A string returned from `createMultipartUpload` which identifies the blob object |
| `uploadId` | Yes | A string returned from `createMultipartUpload` which identifies the multipart upload |
| `contentType` | No | The [media type](https://developer.mozilla.org/docs/Web/HTTP/Headers/Content-Type) for the file. If not specified, it's derived from the file extension. Falls back to `application/octet-stream` when no extension exists or can't be matched. |
| `token` | No | A string specifying the token to use when making requests. It defaults to `process.env.BLOB_READ_WRITE_TOKEN` when deployed on Vercel as explained in [Read-write token](#read-write-token). You can also pass a client token created with the `generateClientTokenFromReadWriteToken` method |
| `addRandomSuffix` | No | A boolean specifying whether to add a random suffix to the pathname. It defaults to `true`. |
| `cacheControlMaxAge` | No | A number in seconds to configure the edge and browser cache. Defaults to one year. See the [caching](/docs/storage/vercel-blob#caching) documentation for more details. |
| `abortSignal` | No | An [AbortSignal](https://developer.mozilla.org/en-US/docs/Web/API/AbortSignal) to cancel the operation |

`completeMultipartUpload()` returns a `JSON` object with the following data for the created blob object:

```
{
  "pathname": "string",
  "contentType": "string",
  "contentDisposition": "string",
  "url": "string",
  "downloadUrl": "string"
}
```

### [Uploader](#uploader)

A less verbose way than the manual process is the multipart uploader method. It's a wrapper around the manual multipart upload process and takes care of the data that is the same for all the three multipart phases. This results in a simpler API, but still requires you to handle memory usage and concurrent upload requests.

Phase 1: Create the multipart uploader

TypeScriptPython

```
const uploader = await createMultipartUploader(pathname, options);
```

`createMultipartUploader` accepts the following parameters:

*   `pathname`: (Required) A string specifying the path inside the blob store. This will be the base value of the return URL and includes the filename and extension.
*   `options`: (Required) A `JSON` object with the following required and optional parameters:

| Parameter | Required | Values |
| --- | --- | --- |
| `access` | Yes | `public` |
| `contentType` | No | The [media type](https://developer.mozilla.org/docs/Web/HTTP/Headers/Content-Type) for the file. If not specified, it's derived from the file extension. Falls back to `application/octet-stream` when no extension exists or can't be matched. |
| `token` | No | A string specifying the token to use when making requests. It defaults to `process.env.BLOB_READ_WRITE_TOKEN` when deployed on Vercel as explained in [Read-write token](#read-write-token). You can also pass a client token created with the `generateClientTokenFromReadWriteToken` method |
| `addRandomSuffix` | No | A boolean specifying whether to add a random suffix to the pathname. It defaults to `true`. |
| `cacheControlMaxAge` | No | A number in seconds to configure the edge and browser cache. Defaults to one year. See the [caching](/docs/storage/vercel-blob#caching) documentation for more details. |
| `abortSignal` | No | An [AbortSignal](https://developer.mozilla.org/en-US/docs/Web/API/AbortSignal) to cancel the operation |

`createMultipartUploader()` returns an `Uploader` object with the following attributes and methods:

TypeScriptPython

```
{
  key: string;
  uploadId: string;
  uploadPart: (partNumber: number, body: BodyInit) => Promise<Part>;
  complete: (parts: Part[]) => Promise<PutBlobResult>;
}
```

Phase 2: Upload all the parts

In the multipart uploader process, it's necessary for you to manage both memory usage and concurrent upload requests. Additionally, each part must be a minimum of 5MB, except the last one which can be smaller, and all parts should be of equal size.

TypeScriptPython

```
const part1 = await uploader.uploadPart(1, chunkBody1);
const part2 = await uploader.uploadPart(2, chunkBody2);
const part3 = await uploader.uploadPart(3, chunkBody3);
```

`uploader.uploadPart` accepts the following parameters:

*   `partNumber`: (Required) A number identifying which part is uploaded
*   `chunkBody`: (Required) A blob object as `ReadableStream`, `String`, `ArrayBuffer` or `Blob` based on these [supported body types](https://developer.mozilla.org/docs/Web/API/fetch#body)

`uploader.uploadPart()` returns an object with the following data for the uploaded part:

TypeScriptPython

```
{
  etag: string;
  partNumber: string;
}
```

Phase 3: Complete the multipart upload

TypeScriptPython

```
const blob = await uploader.complete([part1, part2, part3]);
```

`uploader.complete` accepts the following parameters:

*   `parts`: (Required) An array containing all the uploaded parts

`uploader.complete()` returns an object with the following data for the created blob object:

TypeScriptPython

```
{
  pathname: string;
  contentType: string;
  contentDisposition: string;
  url: string;
  downloadUrl: string;
}
```

## [Deleting blobs](#deleting-blobs)

This example creates a function that deletes a blob object from the Blob store. You can delete multiple blob objects in a single request by passing an array of blob URLs.

Next.js (/app)Next.js (/pages)Other frameworks

app/delete/route.ts

TypeScript

TypeScriptJavaScript

```
import { del } from '@vercel/blob';
 
export async function DELETE(request: Request) {
  const { searchParams } = new URL(request.url);
  const urlToDelete = searchParams.get('url') as string;
  await del(urlToDelete);
 
  return new Response();
}
```

### [`del()`](#del)

The `del` method deletes one or multiple blob objects from the Blob store.

Since blobs are cached, it may take up to one minute for them to be fully removed from the Vercel cache.

TypeScriptPython

```
del(urlOrPathname, options);
 
del([urlOrPathname], options); // You can pass an array to delete multiple blob objects
```

It accepts the following parameters:

*   `urlOrPathname`: (Required) A string or array of strings specifying the URL(s) or pathname(s) of the blob object(s) to delete.
*   `options`: (Optional) A `JSON` object with the following optional parameter:

| Parameter | Required | Values |
| --- | --- | --- |
| `token` | No | A string specifying the read-write token to use when making requests. It defaults to `process.env.BLOB_READ_WRITE_TOKEN` when deployed on Vercel as explained in [Read-write token](#read-write-token) |
| `abortSignal` | No | An [AbortSignal](https://developer.mozilla.org/en-US/docs/Web/API/AbortSignal) to cancel the operation |

`del()` returns a `void` response. A delete action is always successful if the blob url exists. A delete action won't throw if the blob url doesn't exists.

## [Get blob metadata](#get-blob-metadata)

This example creates a Function that returns a blob object's metadata.

Next.js (/app)Next.js (/pages)Other frameworks

app/get-blob/route.ts

TypeScript

TypeScriptJavaScript

```
import { head } from '@vercel/blob';
 
export async function GET(request: Request) {
  const { searchParams } = new URL(request.url);
  const blobUrl = searchParams.get('url');
  const blobDetails = await head(blobUrl);
 
  return Response.json(blobDetails);
}
```

### [`head()`](#head)

The `head` method returns a blob object's metadata.

TypeScriptPython

```
head(urlOrPathname, options);
```

It accepts the following parameters:

*   `urlOrPathname`: (Required) A string specifying the URL or pathname of the blob object to read.
*   `options`: (Optional) A `JSON` object with the following optional parameter:

| Parameter | Required | Values |
| --- | --- | --- |
| `token` | No | A string specifying the read-write token to use when making requests. It defaults to `process.env.BLOB_READ_WRITE_TOKEN` when deployed on Vercel as explained in [Read-write token](#read-write-token) |
| `abortSignal` | No | An [AbortSignal](https://developer.mozilla.org/en-US/docs/Web/API/AbortSignal) to cancel the operation |

`head()` returns one of the following:

*   a `JSON` object with the requested blob object's metadata
*   throws a `BlobNotFoundError` if the blob object was not found

TypeScriptPython

```
{
  size: number;
  uploadedAt: Date;
  pathname: string;
  contentType: string;
  contentDisposition: string;
  url: string;
  downloadUrl: string;
  cacheControl: string;
}
```

## [List blobs](#list-blobs)

This example creates a Function that returns a list of blob objects in a Blob store.

Next.js (/app)Next.js (/pages)Other frameworks

app/get-blobs/route.ts

TypeScript

TypeScriptJavaScript

```
import { list } from '@vercel/blob';
 
export async function GET(request: Request) {
  const { blobs } = await list();
  return Response.json(blobs);
}
```

### [`list()`](#list)

The `list` method returns a list of blob objects in a Blob store.

TypeScriptPython

```
list(options);
```

It accepts the following parameters:

*   `options`: (Optional) A `JSON` object with the following optional parameters:

| Parameter | Required | Values |
| --- | --- | --- |
| `token` | No | A string specifying the read-write token to use when making requests. It defaults to `process.env.BLOB_READ_WRITE_TOKEN` when deployed on Vercel as explained in [Read-write token](#read-write-token) |
| `limit` | No | A number specifying the maximum number of blob objects to return. It defaults to 1000 |
| `prefix` | No | A string used to filter for blob objects contained in a specific folder assuming that the folder name was used in the `pathname` when the blob object was uploaded |
| `cursor` | No | A string obtained from a previous `list` response to be used for reading the next page of results |
| `mode` | No | A string specifying the response format. Can either be `expanded` (default) or `folded`. In `folded` mode all blobs that are located inside a folder will be folded into a single folder string entry |
| `abortSignal` | No | An [AbortSignal](https://developer.mozilla.org/en-US/docs/Web/API/AbortSignal) to cancel the operation |

`list()` returns a `JSON` object in the following format:

TypeScriptPython

```
{
  blobs: {
    size: number;
    uploadedAt: Date;
    pathname: string;
    url: string;
    downloadUrl: string;
  }[];
  cursor?: string;
  hasMore: boolean;
  folders?: string[];
}
```

### [Pagination](#pagination)

For a long list of blob objects (the default list `limit` is 1000), you can use the `cursor` and `hasMore` parameters to paginate through the results as shown in the example below:

TypeScriptPython

```
let hasMore = true;
let cursor;
 
while (hasMore) {
  const listResult = await list({
    cursor,
  });
 
  hasMore = listResult.hasMore;
  cursor = listResult.cursor;
}
```

### [Folders](#folders)

To retrieve the folders from your blob store, alter the `mode` parameter to modify the response format of the list operation. The default value of `mode` is `expanded`, which returns all blobs in a single array of objects.

Alternatively, you can set `mode` to `folded` to roll up all blobs located inside a folder into a single entry. These entries will be included in the response as `folders`. Blobs that are not located in a folder will still be returned in the blobs property.

By using the `folded` mode, you can efficiently retrieve folders and subsequently list the blobs inside them by using the returned `folders` as a `prefix` for further requests. Omitting the `prefix` parameter entirely, will return all folders in the root of your store. Be aware that the blobs pathnames and the folder names will always be fully quantified and never relative to the prefix you passed.

TypeScriptPython

```
const {
  folders: [firstFolder],
  blobs: rootBlobs,
} = await list({ mode: 'folded' });
 
const { folders, blobs } = await list({ mode: 'folded', prefix: firstFolder });
```

## [Copy a blob](#copy-a-blob)

This example creates a Function that copies an existing blob to a new path in the store.

Next.js (/app)Next.js (/pages)Other frameworks

app/copy-blob/route.ts

TypeScript

TypeScriptJavaScript

```
import { copy } from '@vercel/blob';
 
export async function PUT(request: Request) {
  const form = await request.formData();
 
  const fromUrl = form.get('fromUrl') as string;
  const toPathname = form.get('toPathname') as string;
 
  const blob = await copy(fromUrl, toPathname, { access: 'public' });
 
  return Response.json(blob);
}
```

### [`copy()`](#copy)

The `copy` method copies an existing blob object to a new path inside the blob store.

The `contentType` and `cacheControlMaxAge` will not be copied from the source blob. If the values should be carried over to the copy, they need to be defined again in the options object.

Contrary to `put()`, `addRandomSuffix` is false by default. This means no automatic random id suffix is added to your blob url, unless you pass `addRandomSuffix: true`. This also means `copy()` overwrites files per default, if the operation targets a pathname that already exists.

TypeScriptPython

```
copy(fromUrlOrPathname, toPathname, options);
```

It accepts the following parameters:

*   `fromUrlOrPathname`: (Required) A blob URL or pathname identifying an already existing blob
*   `toPathname`: (Required) A string specifying the new path inside the blob store. This will be the base value of the return URL
*   `options`: (Required) A `JSON` object with the following required and optional parameters:

| Parameter | Required | Values |
| --- | --- | --- |
| `access` | Yes | `public` |
| `contentType` | No | A string indicating the [media type](https://developer.mozilla.org/docs/Web/HTTP/Headers/Content-Type). By default, it's extracted from the toPathname's extension. |
| `token` | No | A string specifying the token to use when making requests. It defaults to `process.env.BLOB_READ_WRITE_TOKEN` when deployed on Vercel as explained in [Read-write token](#read-write-token) |
| `addRandomSuffix` | No | A boolean specifying whether to add a random suffix to the pathname. It defaults to `false`. |
| `cacheControlMaxAge` | No | A number in seconds to configure the edge and browser cache. Defaults to one year. See the [caching](/docs/storage/vercel-blob#caching) documentation for more details. |
| `abortSignal` | No | An [AbortSignal](https://developer.mozilla.org/en-US/docs/Web/API/AbortSignal) to cancel the operation |

`copy()` returns a `JSON` object with the following data for the copied blob object:

TypeScriptPython

```
{
  pathname: string;
  contentType: string;
  contentDisposition: string;
  url: string;
  downloadUrl: string;
}
```

An example blob is:

```
{
  "pathname": "profilesv1/user-12345-copy.txt",
  "contentType": "text/plain",
  "contentDisposition": "attachment; filename=\"user-12345-copy.txt\"",
  "url": "https://ce0rcu23vrrdzqap.public.blob.vercel-storage.com/profilesv1/user-12345-copy.txt",
  "downloadUrl": "https://ce0rcu23vrrdzqap.public.blob.vercel-storage.com/profilesv1/user-12345-copy.txt?download=1"
}
```

## [Client uploads](#client-uploads)

As seen in the [client uploads quickstart docs](/docs/storage/vercel-blob/client-upload), you can upload files directly from clients (like browsers) to the Blob store.

All client uploads related methods are available under `@vercel/blob/client`.

### [`upload()`](#upload)

The `upload` method is dedicated to [client uploads](/docs/storage/vercel-blob/client-upload). It fetches a client token on your server using the `handleUploadUrl` before uploading the blob. Read the [client uploads](/docs/storage/vercel-blob/client-upload) documentation to learn more.

```
upload(pathname, body, options);
```

It accepts the following parameters:

*   `pathname`: (Required) A string specifying the base value of the return URL
*   `body`: (Required) A blob object as `ReadableStream`, `String`, `ArrayBuffer` or `Blob` based on these [supported body types](https://developer.mozilla.org/docs/Web/API/fetch#body)
*   `options`: (Required) A `JSON` object with the following required and optional parameters:

| Parameter | Required | Values |
| --- | --- | --- |
| `access` | Yes | `public` |
| `contentType` | No | A string indicating the [media type](https://developer.mozilla.org/docs/Web/HTTP/Headers/Content-Type). By default, it's extracted from the pathname's extension. |
| `handleUploadUrl` | Yes\* | A string specifying the route to call for generating client tokens for [client uploads](/docs/storage/vercel-blob/client-upload). |
| `clientPayload` | No | A string to be sent to your `handleUpload` server code. Example use-case: attaching the post id an image relates to. So you can use it to update your database. |
| `multipart` | No | Pass `multipart: true` when uploading large files. It will split the file into multiple parts, upload them in parallel and retry failed parts. |
| `abortSignal` | No | An [AbortSignal](https://developer.mozilla.org/en-US/docs/Web/API/AbortSignal) to cancel the operation |
| `onUploadProgress` | No | Callback to track upload progress: `onUploadProgress({loaded: number, total: number, percentage: number})` |

`upload()` returns a `JSON` object with the following data for the created blob object:

```
{
  pathname: string;
  contentType: string;
  contentDisposition: string;
  url: string;
  downloadUrl: string;
}
```

An example `url` is:

`https://ce0rcu23vrrdzqap.public.blob.vercel-storage.com/profilesv1/user-12345-NoOVGDVcqSPc7VYCUAGnTzLTG2qEM2.txt`

### [`handleUpload()`](#handleupload)

A server-side route helper to manage client uploads, it has two responsibilities:

1.  Generate tokens for client uploads
2.  Listen for completed client uploads, so you can update your database with the URL of the uploaded file for example

```
handleUpload(options);
```

It accepts the following parameters:

*   `options`: (Required) A `JSON` object with the following parameters:

| Parameter | Required | Values |
| --- | --- | --- |
| `token` | No | A string specifying the read-write token to use when making requests. It defaults to `process.env.BLOB_READ_WRITE_TOKEN` when deployed on Vercel as explained in [Read-write token](#read-write-token) |
| `request` | Yes | An `IncomingMessage` or `Request` object to be used to determine the action to take |
| [`onBeforeGenerateToken`](#onbeforegeneratetoken) | Yes | A function to be called right before generating client tokens for client uploads. See below for usage |
| [`onUploadCompleted`](#onuploadcompleted) | Yes | A function to be called by Vercel Blob when the client upload finishes. This is useful to update your database with the blob url that was uploaded |
| `body` | Yes | The request body |

`handleUpload()` returns:

```
Promise<
  | { type: 'blob.generate-client-token'; clientToken: string }
  | { type: 'blob.upload-completed'; response: 'ok' }
>;
```

#### [`onBeforeGenerateToken()`](#onbeforegeneratetoken)

The `onBeforeGenerateToken` function receives the following arguments:

*   `pathname`: The destination path for the blob
*   `clientPayload`: A string payload specified on the client when calling `upload()`
*   `multipart`: A boolean specifying whether the file is a multipart upload.

The function must return an object with the following properties:

| Parameter | Required | Values |
| --- | --- | --- |
| `addRandomSuffix` | No | A boolean specifying whether to add a random suffix to the `pathname`. It defaults to `false`. We recommend using this option to ensure there are no conflicts in your blob filenames. |
| `allowedContentTypes` | No | An array of strings specifying the [media type](https://developer.mozilla.org/docs/Web/HTTP/Headers/Content-Type) that are allowed to be uploaded. By default, it's all content types. Wildcards are supported (`text/*`) |
| `maximumSizeInBytes` | No | A number specifying the maximum size in bytes that can be uploaded. The maximum is 5TB. |
| `validUntil` | No | A number specifying the timestamp in ms when the token will expire. By default, it's now + 1 hour. |
| `allowOverwrite` | No | A boolean to allow overwriting blobs. By default an error will be thrown if you try to overwrite a blob by using the same `pathname` for multiple blobs. |
| `cacheControlMaxAge` | No | A number in seconds to configure how long Blobs are cached. Defaults to one month. Cannot be set to a value lower than 1 minute. See the [caching](/docs/storage/vercel-blob#caching) documentation for more details. |
| `callbackUrl` | No | A string specifying the URL that Vercel Blob will call when the upload completes. See [client uploads](/docs/storage/vercel-blob/client-upload) for examples. |
| `tokenPayload` | No | A string specifying a payload to be sent to your server on upload completion. |

#### [`onUploadCompleted()`](#onuploadcompleted)

The `onUploadCompleted` function receives the following arguments:

*   `blob`: The blob that was uploaded. See the return type of [`put()`](#put) for more details.
*   `tokenPayload`: The payload that was defined in the [`onBeforeGenerateToken()`](#onbeforegeneratetoken) function.

### [Client uploads routes](#client-uploads-routes)

Here's an example Next.js App Router route handler that uses `handleUpload()`:

app/api/post/upload/route.ts

```
import { handleUpload, type HandleUploadBody } from '@vercel/blob/client';
import { NextResponse } from 'next/server';
 
// Use-case: uploading images for blog posts
export async function POST(request: Request): Promise<NextResponse> {
  const body = (await request.json()) as HandleUploadBody;
 
  try {
    const jsonResponse = await handleUpload({
      body,
      request,
      onBeforeGenerateToken: async (pathname, clientPayload) => {
        // Generate a client token for the browser to upload the file
        // ⚠️ Authenticate and authorize users before generating the token.
        // Otherwise, you're allowing anonymous uploads.
 
        // ⚠️ When using the clientPayload feature, make sure to validate it
        // otherwise this could introduce security issues for your app
        // like allowing users to modify other users' posts
 
        return {
          allowedContentTypes: [
            // optional, default to all content types
            'image/jpeg',
            'image/png',
            'image/webp',
            'text/*',
          ],
          // callbackUrl: 'https://example.com/api/avatar/upload',
          // optional, `callbackUrl` is automatically computed when hosted on Vercel
        };
      },
      onUploadCompleted: async ({ blob, tokenPayload }) => {
        // Get notified of client upload completion
        // ⚠️ This will not work on `localhost` websites,
        // Use ngrok or similar to get the full upload flow
 
        console.log('blob upload completed', blob, tokenPayload);
 
        try {
          // Run any logic after the file upload completed,
          // If you've already validated the user and authorization prior, you can
          // safely update your database
        } catch (error) {
          throw new Error('Could not update post');
        }
      },
    });
 
    return NextResponse.json(jsonResponse);
  } catch (error) {
    return NextResponse.json(
      { error: error instanceof Error ? error.message : String(error) },
      { status: 400 }, // The webhook will retry 5 times waiting for a 200
    );
  }
}
```

## [Handling errors](#handling-errors)

When you make a request to the SDK using any of the above methods, they will return an error if the request fails due to any of the following reasons:

*   Missing required parameters
*   An invalid token or a token that does have access to the Blob object
*   Suspended Blob store
*   Blob file or Blob store not found
*   Unforeseen or unknown errors

To catch these errors, wrap your requests with a `try/catch` statement as shown below:

TypeScriptPython

```
import { put, BlobAccessError } from '@vercel/blob';
 
try {
  await put(...);
} catch (error) {
  if (error instanceof BlobAccessError) {
    // handle a recognized error
  } else {
    // throw the error again if it's unknown
  throw error;
  }
}
```

--------------------------------------------------------------------------------
title: "Vercel Firewall"
description: "Learn how Vercel Firewall helps protect your applications and websites from malicious attacks and unauthorized access."
last_updated: "null"
source: "https://vercel.com/docs/vercel-firewall"
--------------------------------------------------------------------------------

# Vercel Firewall

Copy page

Ask AI about this page

Last updated September 5, 2025

The Vercel Firewall is a robust, multi-layered security system designed to protect your applications from a wide range of threats. Every incoming request goes through the following firewall layers:

*   [Platform-wide firewall](#platform-wide-firewall): With [DDoS mitigation](/docs/security/ddos-mitigation), it protects against large-scale attacks such as DDoS and TCP floods and is available for free for all customers without any configuration required.
*   [Web Application Firewall (WAF)](#vercel-waf): A customizable layer for fine-tuning security measures with logic tailored to your needs and [observability](#observability) into your web traffic.

### [Concepts](#concepts)

Understand the fundamentals:

*   How [Vercel protects every request](/docs/security/firewall-concepts#how-vercel-secures-requests).
*   Why [DDoS](/docs/security/firewall-concepts#understanding-ddos) needs to be mitigated.
*   How the firewall decides [which rule to apply first](#rule-execution-order).
*   How the firewall uses [JA3 and JA4 TLS fingerprints](/docs/security/firewall-concepts#ja3-and-ja4-tls-fingerprints) to identify and restrict malicious traffic.

## [Rule execution order](#rule-execution-order)

The automatic rules of the platform-wide firewall and the custom rules of the WAF work together in the following execution order:

1.  [DDoS mitigation rules](/docs/security/ddos-mitigation)
2.  [WAF IP blocking rules](/docs/security/vercel-waf/ip-blocking)
3.  [WAF custom rules](/docs/security/vercel-waf/custom-rules)
4.  [Managed rulesets](/docs/security/vercel-waf/managed-rulesets)

When you have more than one custom rule, you can [customize](/docs/security/vercel-waf/custom-rules#custom-rule-configuration) their order in the Firewall tab of the project.

## [Platform-wide firewall](#platform-wide-firewall)

DDoS Mitigation is available on [all plans](/docs/plans)

Vercel provides automated [DDoS mitigation](/docs/security/ddos-mitigation) for all deployments, regardless of the plan that you are on. With this automated DDoS mitigation, we block incoming traffic if we identify abnormal or suspicious levels of incoming requests.

## [Vercel WAF](#vercel-waf)

Vercel WAF is available on [all plans](/docs/plans)

Those with the [member](/docs/rbac/access-roles#member-role), [viewer](/docs/rbac/access-roles#viewer-role), [developer](/docs/rbac/access-roles#developer-role) and [administrator](/docs/rbac/access-roles#project-administrators) roles can access this feature

The [Vercel WAF](/docs/security/vercel-waf) complements the platform-wide firewall by allowing you to define custom protection strategies using the following tools:

*   [Custom Rules](/docs/security/vercel-waf/custom-rules)
*   [IP Blocking](/docs/security/vercel-waf/ip-blocking)
*   [Managed Rulesets](/docs/security/vercel-waf/managed-rulesets)
*   [Attack Challenge Mode](/docs/attack-challenge-mode)

## [Observability](#observability)

You can use the following tools to [monitor the internet traffic](/docs/vercel-firewall/firewall-observability) at your team or project level:

*   The [Monitoring](/docs/observability/monitoring) feature at the team level allows you to create [queries](/docs/observability/monitoring/monitoring-reference#example-queries) to visualize the traffic across your Vercel projects.
*   The Firewall tab of the Vercel dashboard on every project allows you to monitor the internet traffic to your deployments with a [traffic monitoring view](/docs/vercel-firewall/firewall-observability#traffic-monitoring) that includes a live traffic window.
*   [Firewall alerts](/docs/vercel-firewall/firewall-observability#firewall-alerts) allow you to react quickly to potential security threats.
*   Use [Log Drains](/docs/drains/using-drains) to send your application logs to a Security Information and Event Management (SIEM) system.

--------------------------------------------------------------------------------
title: "Attack Challenge Mode"
description: "Learn how to use Attack Challenge Mode to help control who has access to your site when it's under attack."
last_updated: "null"
source: "https://vercel.com/docs/vercel-firewall/attack-challenge-mode"
--------------------------------------------------------------------------------

# Attack Challenge Mode

Copy page

Ask AI about this page

Last updated September 24, 2025

Attack Challenge Mode is available on [all plans](/docs/plans)

Those with the [member](/docs/rbac/access-roles#member-role) role can access this feature

Attack Challenge Mode is a security feature that protects your site during DDoS attacks. When enabled, visitors must complete a [security challenge](/docs/vercel-firewall/firewall-concepts#challenge) before accessing your site, while known bots (like search engines and webhook providers) are automatically allowed through.

The Vercel Firewall automatically [mitigates against DDoS attacks](/docs/security/ddos-mitigation), but Attack Challenge Mode provides an extra layer of protection for highly targeted attacks.

Attack Challenge Mode is available for [free](#pricing) on all [plans](/docs/plans) and requests blocked by challenge mode do not count towards your usage limits.

## [Known bots support](#known-bots-support)

Vercel maintains and continuously updates a comprehensive directory of known legitimate bots from across the internet. Attack Challenge Mode automatically recognizes and allows these bots to pass through without being challenged.

Review [Verified bots](/docs/bot-management#verified-bots) for examples of bot categories and services that are automatically allowed. [Internal Requests](#internal-requests) are also allowed through.

Vercel's bot directory is regularly updated to include new legitimate services as they emerge, ensuring your SEO, analytics, integrations, and essential services continue to function even with Attack Challenge Mode enabled.

To block specific known bots instead of allowing them through, you can create a [Custom Rule](/docs/security/vercel-waf/custom-rules) that matches their User Agent.

## [Internal requests](#internal-requests)

When Attack Challenge Mode is enabled, requests from your own [Functions](/docs/functions) and [Cron Jobs](/docs/cron-jobs) are automatically allowed through without being challenged. This means your application's internal operations will continue to work normally.

For example, if you have multiple projects in your Vercel account:

*   Your projects can communicate with each other without being challenged
*   Only requests from outside your account will be challenged
*   Each Vercel account has its own secure boundary

Other Vercel accounts cannot bypass Attack Challenge Mode on your projects. The security is strictly enforced per account, ensuring that only your own projects can communicate without challenges.

## [Enabling attack challenge mode](#enabling-attack-challenge-mode)

While Vercel's Firewall [automatically monitors for and mitigates attacks](/docs/security/ddos-mitigation#what-to-do-in-case-of-a-ddos-attack), you can enable Attack Challenge Mode during targeted attacks for additional security.

To enable:

1.  Select your project from the [Dashboard](/dashboard).
2.  Navigate to the Firewall tab.
3.  Click Bot Management.
4.  Under Attack Challenge Mode, select Enable.

All traffic initiated by web browsers, including API traffic, is supported. For example, a Next.js frontend calling a Next.js API in the same project will work properly.

Standalone APIs, other backend frameworks, and non-recognized automated services may not be able to pass challenges and could be blocked. If you need more control over what traffic is challenged, consider using [Custom Rules with the Vercel WAF](/docs/security/vercel-waf/custom-rules).

## [How long to keep it enabled](#how-long-to-keep-it-enabled)

Attack Challenge Mode can be safely used for extended periods without affecting search engine indexing or webhook functionality. However, since Vercel's Firewall already provides automatic DDoS protection, we recommend using it primarily when facing highly targeted attacks rather than as a permanent setting.

## [Disabling attack challenge mode](#disabling-attack-challenge-mode)

When you no longer need the additional protection:

1.  Select your project from the [Dashboard](/dashboard)
2.  Navigate to the Firewall tab.
3.  Click Bot Management.
4.  Under Attack Challenge Mode, select Disable.

## [Challenging with custom rules](#challenging-with-custom-rules)

For more granular control, define a [Custom Rule with the Vercel WAF](/docs/security/vercel-waf/custom-rules) to challenge specific web traffic.

## [Search indexing](#search-indexing)

Search engine crawlers like Googlebot are automatically allowed through Attack Challenge Mode without being challenged. This means enabling Attack Challenge Mode will not negatively impact your site's SEO or search engine indexing, even when used for extended periods.

## [Pricing](#pricing)

Attack Challenge Mode is available for free on all plans.

All mitigations by Attack Challenge Mode are free and unlimited, and there are zero costs associated with traffic blocked by Attack Challenge Mode.

--------------------------------------------------------------------------------
title: "DDoS Mitigation"
description: "Learn how the Vercel Firewall mitigates against DoS and DDoS attacks"
last_updated: "null"
source: "https://vercel.com/docs/vercel-firewall/ddos-mitigation"
--------------------------------------------------------------------------------

# DDoS Mitigation

Copy page

Ask AI about this page

Last updated September 24, 2025

DDoS Mitigation is available on [all plans](/docs/plans)

Vercel provides automatic DDoS mitigation for all deployments, regardless of your plan. We block incoming traffic if we identify abnormal or suspicious levels of incoming requests.

Vercel does not charge customers for traffic that gets blocked with DDoS mitigation.

It works by:

*   Monitoring traffic: Vercel Firewall continuously analyzes incoming traffic to detect signs of DDoS attacks. This helps to identify and mitigate threats in real-time
*   Blocking traffic: Vercel Firewall filters out malicious traffic while allowing legitimate requests to pass through
*   Scaling resources: During a DDoS attack, Vercel Firewall dynamically scales resources to absorb the increased traffic, preventing your applications or sites from being overwhelmed

If you need further control over incoming traffic, you can temporarily enable [Attack Challenge Mode](/docs/attack-challenge-mode) to challenge all traffic to your site, ensuring only legitimate users can access it.

Learn more about [DoS, DDoS and the Open System Interconnection model](/docs/security/firewall-concepts#understanding-ddos).

## [Responding to DDoS attacks](#responding-to-ddos-attacks)

Vercel mitigates against L3, L4, and L7 DDoS attacks regardless of the plan you are on. The Vercel Firewall uses hundreds of signals and detection factors to fingerprint request patterns, determining if they appear to be an attack, and challenging or blocking requests if they appear illegitimate.

However, there are other steps you can take to protect your site during DDoS attacks:

*   Enable [Attack Challenge Mode](/docs/attack-challenge-mode) to challenge all visitors to your site. This is a temporary measure and provides another layer of security to ensure all traffic to your site is legitimate
*   You can set up [IP Blocking](/docs/security/vercel-waf/ip-blocking) to block specific IP addresses from accessing your projects. Enterprise teams can also receive dedicated DDoS support
*   You can add [Custom Rules](/docs/security/vercel-waf/custom-rules) to deny or challenge specific traffic to your site based on the conditions of the rules
*   You can also use Middleware to [block requests](https://github.com/vercel/examples/tree/main/edge-middleware/geolocation-country-block) based on specific criteria or to implement [rate limiting](/guides/rate-limiting-edge-middleware-vercel-kv).

Pro teams can [set up Spend Management](/docs/spend-management#managing-your-spend-amount) to get notified or to automatically take action, such as [using a webhook](/docs/spend-management#configuring-a-webhook) or pausing your projects when your usage hits a set spend amount.

## [Bypass System-level Mitigations](#bypass-system-level-mitigations)

Bypass System-level Mitigations are available on [Enterprise](/docs/plans/enterprise) and [Pro](/docs/plans/pro) plans

While Vercel's system-level mitigations (such as [DDoS protection](/docs/security/ddos-mitigation)) safeguards your websites and applications, it can happen that they block traffic from trusted sources like proxies or shared networks in situations where traffic from these proxies or shared networks was identified as malicious. You can temporarily pause all automatic mitigations for a specific project. This can be useful on business-critical events such as Black Friday.

To temporarily pause all automatic mitigations for a specific project:

1.  Click the menu button with the ellipsis icon at the top right of the Firewall tab for your project.
2.  Select Pause System Mitigations.
3.  Review the warning in the Pause System Mitigations dialog and confirm that you would like to pause all automatic mitigations for that project for the next 24 hours.

To resume the automatic mitigations before the 24 hour period ends:

1.  Click the menu button with the ellipsis icon at the top right of the Firewall tab for your project.
2.  Select Resume System Mitigations.
3.  Select Resume from the Resume System Mitigations dialog.

You are responsible for all usage fees incurred when using this feature, including illegitimate traffic that may otherwise have been blocked.

### [System Bypass Rules](#system-bypass-rules)

In situations where you need a more granular and permanent approach, you can use [System Bypass Rules](/docs/security/vercel-waf/system-bypass-rules) to ensure that essential traffic is never blocked by DDoS protection.

This feature is available for Pro and Enterprise customers. Learn how to [set up a System Bypass rule](/docs/security/vercel-waf/system-bypass-rules#get-started) for your project and [limits](/docs/security/vercel-waf/system-bypass-rules#limits) that apply based on your plan.

## [Dedicated DDoS support for Enterprise teams](#dedicated-ddos-support-for-enterprise-teams)

For larger, distributed attacks on Enterprise Teams, we collaborate with you to keep your site(s) online during an attack. Automated prevention and direct communication from our Customer Success Managers or Account Executives ensure your site remains resilient.

## [DDoS and billing](#ddos-and-billing)

[Vercel automatically mitigates against L3, L4, and L7 DDoS attacks](/docs/security/ddos-mitigation) at the platform level for all plans. Vercel does not charge customers for traffic that gets blocked by the Firewall.

Usage will be incurred for requests that are successfully served prior to us automatically mitigating the event. Usage will also be incurred for requests that are not recognized as a DDoS event, which may include bot and crawler traffic.

For an additional layer of security, we recommend that you enable [Attack Challenge Mode](/docs/attack-challenge-mode) when you are under attack, which is available for free on all plans. While some malicious traffic is automatically challenged, enabling Attack Challenge Mode will challenge all traffic, including legitimate traffic to ensure that only real users can access your site.

You can monitor usage in the [Vercel Dashboard](/dashboard) under the Usage tab, although you will [receive notifications](/docs/notifications#on-demand-usage-notifications) when nearing your usage limits.

--------------------------------------------------------------------------------
title: "Using the REST API with the Firewall"
description: "Learn how to interact with the security endpoints of the Vercel REST API programmatically."
last_updated: "null"
source: "https://vercel.com/docs/vercel-firewall/firewall-api"
--------------------------------------------------------------------------------

# Using the REST API with the Firewall

Copy page

Ask AI about this page

Last updated May 1, 2025

The security section of the [Vercel REST API](/docs/rest-api) allows you to programmatically interact with some of the functionality of the Vercel Firewall such as [creating a system bypass rule](/docs/rest-api/reference/endpoints/security/create-system-bypass-rule) and [updating your Vercel WAF rule configuration](/docs/rest-api/reference/endpoints/security/update-firewall-configuration).

You can use the REST API programmatically as follows:

*   Install the [Vercel SDK](/docs/rest-api/sdk) and use the [security methods](https://github.com/vercel/sdk/blob/HEAD/docs/sdks/security/README.md).
*   [Call the endpoints directly](/docs/rest-api) and use the [security endpoints](/docs/rest-api/reference/endpoints/security).

To define firewall rules in code that apply across multiple projects, you can use the [Vercel Terraform provider](https://registry.terraform.io/providers/vercel/vercel/latest).

After [setting up Terraform](/guides/integrating-terraform-with-vercel), you can use the following rules:

*   [vercel\_firewall\_config](https://registry.terraform.io/providers/vercel/vercel/latest/docs/resources/firewall_config)
*   [vercel\_firewall\_bypass](https://registry.terraform.io/providers/vercel/vercel/latest/docs/resources/firewall_bypass)

## [Examples](#examples)

Learn how to use some of these endpoints with specific examples for the Vercel WAF.

*   [Challenge `cURL` requests](/guides/challenge-curl-requests)
*   [Challenge cookieless requests on a specific path](/guides/challenge-cookieless-requests-on-a-specific-path)
*   [Deny non-browser traffic or blocklisted ASNs](/guides/deny-non-browser-traffic-or-blocklisted-asns)
*   [Deny traffic from a set of IP addresses](/guides/deny-traffic-from-a-set-of-ip-addresses)
*   [Vercel Firewall Terraform configuration](/guides/firewall-terraform-configuration)

--------------------------------------------------------------------------------
title: "Firewall concepts"
description: "Understand the fundamentals behind the Vercel Firewall."
last_updated: "null"
source: "https://vercel.com/docs/vercel-firewall/firewall-concepts"
--------------------------------------------------------------------------------

# Firewall concepts

Copy page

Ask AI about this page

Last updated September 15, 2025

## [How Vercel secures requests](#how-vercel-secures-requests)

To safeguard your application against malicious activity, Vercel's platform-wide firewall is the first line of defense, inspecting requests as they arrive at Vercel's CDN. Once a request passes this layer, [deployment protection](/docs/security/deployment-protection) checks whether it can continue based on access rules set at the level of your project.

If allowed to go through, the request is subject to the rules that you configured with the [Web Application Firewall (WAF)](/docs/security/vercel-waf) at the level of your project. If the request is not blocked by the WAF rules, your deployment can process and serve it.

If you [enabled a persistent action](/docs/security/vercel-waf/custom-rules#persistent-actions) for a WAF rule and it blocks the request, the source IP address is stored in the platform firewall so that future requests from this source continue to be blocked for the specified time period. These future blocks happen at the level of the platform-wide firewall.

![How Vercel protects every incoming request with multiple layers](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fsecurity%2Fvercel-firewall-protection-concept-light.png&w=1200&q=75)![How Vercel protects every incoming request with multiple layers](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fsecurity%2Fvercel-firewall-protection-concept-dark.png&w=1200&q=75)

How Vercel protects every incoming request with multiple layers

## [Firewall actions](#firewall-actions)

The Vercel Firewall allows several possible actions to be taken when traffic matches a rule. These actions, that can be taken by custom rules or system DDoS mitigations, apply when detecting malicious traffic. You can view the actions and their results in the [Firewall and Monitoring](/docs/vercel-firewall#observability) tabs.

### [Log](#log)

The log action allows you to monitor and record specific traffic patterns without affecting the request. When a request matches a rule with the log action:

*   The request is allowed to proceed normally.
*   Details about the request are logged and displayed in the Firewall and Monitoring tabs, and sent to log drains for analysis.
*   There is no impact on the visitor's experience.

This is useful for monitoring suspicious patterns or gathering data about specific types of traffic before implementing stricter actions.

### [Deny](#deny)

The deny action blocks requests immediately when they match a rule. When a request is denied:

*   A `403 Forbidden` response is returned.
*   The request does not reach your application.
*   Usage is incurred only for the edge request and ingress [Fast Data Transfer](/docs/manage-cdn-usage#fast-data-transfer) which are required to process the custom rule.

This is the most restrictive action and you should use it for known malicious traffic patterns or IP addresses.

### [Challenge](#challenge)

A security challenge verifies that incoming traffic originates from a real web browser with JavaScript capabilities. Only human visitors using a web browser can pass the challenge and access protected resources, while non-browser clients (bots, scripts, etc.) cannot.

Use the challenge action when you want to block automated traffic while allowing legitimate users to access your content. It offers a middle ground between the log and deny actions, protecting against bots while maintaining accessibility for real visitors through a simple one-time verification.

When the challenge action is applied:

1.  ### [Initial challenge](#initial-challenge)
    
    During this process, visitors see a Vercel Security Checkpoint screen:
    
    ![Vercel challenge page](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fsecurity%2Fchallenge-light.png&w=1920&q=75)![Vercel challenge page](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fsecurity%2Fchallenge-dark.png&w=1920&q=75)
    
    Vercel challenge page
    
    *   The browser must execute JavaScript code to prove it's a real browser.
    *   The code computes and submits a challenge solution.
    *   The system validates browser characteristics to prevent automated tools from passing.
    *   If the challenge succeeds, the [WAF](/docs/vercel-firewall/vercel-waf) validates the request as a legitimate browser client and continues processing the request, which includes evaluating any additional WAF rules.
    *   If the challenge fails, the request is blocked before reaching your application.
    
    The checkpoint page localizes to a language based on the visitor's browser settings and respects their preferred color scheme, ensuring a seamless experience for legitimate users.
    
2.  ### [Challenge session](#challenge-session)
    
    *   Upon successful verification, a challenge session is created in the browser.
    *   Sessions are valid for 1 hour.
    *   All subsequent requests within the session are allowed.
    *   Challenge sessions are tied to the browser that completed the challenge, ensuring secure session management.
    *   After session expiration, the client must re-solve the challenge.

#### [Challenge subrequests and APIs](#challenge-subrequests-and-apis)

If your application makes additional requests (e.g., API calls) during a valid session, they automatically succeed. This is particularly useful for server-side rendered applications where the server makes additional requests to APIs in the same application.

#### [Challenge limitations](#challenge-limitations)

*   API routes that are protected by a challenge rule can only be accessed within a valid challenge session.
*   Direct API calls (e.g., from scripts, cURL, or Postman) will fail if they require challenge validation.
*   Direct API calls from outside a valid challenge session will not succeed.
*   If a user hasn't completed a challenge session through your website first, they cannot access challenged API routes.
*   Automated tools and scripts cannot establish challenge sessions. For legitimate automation needs, use [Bypass](#bypass) to allow specific trusted sources.

### [Bypass](#bypass)

The bypass action allows specific traffic to skip any subsequent firewall rules. When a request matches a bypass rule:

*   For custom rule bypasses, the request is allowed through any custom or managed rules.
*   For system bypasses, the request is allowed through any system-level mitigations.
*   The request proceeds directly to your application.

This is useful for trusted traffic sources, internal tools, or critical services that should never be blocked.

## [Understanding DDoS](#understanding-ddos)

A Denial of Service (DoS) attack happens when one device attempts to exhaust the resources of a system using methods such as sending a large amount of data to a server or network. These attacks can often be mitigated by finding and closing off the connection to the source of the attack.

A Distributed Denial of Service (DDoS) attack happens when multiple connected devices are used to simultaneously overwhelm a site with targeted, illegitimate traffic. The goal of DoS and DDoS attacks is to disrupt access to the servers hosting the site.

In addition to built-in systems like [rate limits](/docs/limits#rate-limits), you can protect yourself against such attacks with [WAF custom rules](/docs/vercel-firewall/vercel-waf/custom-rules), [WAF Rate Limiting](/docs/vercel-firewall/vercel-waf/rate-limiting) and securing your backend with [Secure Compute](/docs/secure-compute) and [OIDC](/docs/oidc).

### [Open System Interconnection (OSI) model](#open-system-interconnection-osi-model)

The OSI model is a concept that outlines the different communication steps of a networking system. Different attack types can target different layers of the [OSI model](https://en.wikipedia.org/wiki/OSI_model).

DDoS attacks target either the [network](#layer-3-ddos) (layer 3), the [transport](#layer-4-ddos) (layer 4) or the [application](#layer-7-ddos) (layer 7) layer of the OSI model. Vercel mitigates against these attacks, and protects the entire platform and all customers from attacks that would otherwise affect reliability.

### [Layer 3 DDoS](#layer-3-ddos)

The goal of a layer 3 (L3) DDoS attack is to slow down and ultimately crash applications, servers, and entire networks. These attacks are often used to target specific IP addresses, but can also target entire networks.

### [Layer 4 DDoS](#layer-4-ddos)

The goal of a layer 4 (L4) DDoS attack is to crash and slow down applications. They target the 3-way-handshake used to establish a reliable connection between TCP connections. This is often called a SYN flood. Layer 4 DDoS attacks are used to target specific ports, but can also target entire protocols.

### [Layer 7 DDoS](#layer-7-ddos)

The goal of a Layer 7 (L7) DDoS attack is to crash and slow down software at the application layer by targeting protocols such as HTTP, which is often done with GET and POST requests. They are often silent and look to leverage vulnerabilities by sending many innocuous requests to a single page. Vercel provides sophisticated proprietary L7 mitigation and is constantly tuning and adjusting attack detection techniques.

## [JA3 and JA4 TLS fingerprints](#ja3-and-ja4-tls-fingerprints)

Vercel Firewall leverages [JA3](#ja3) and [JA4](#ja4) TLS fingerprints to identify and restrict malicious traffic. TLS fingerprints allow the unique identification of user sessions inspecting details in the Transport Layer Security (TLS) protocol initiation process.

TLS Fingerprints are available on [all plans](/docs/plans)

### [TLS fingerprinting](#tls-fingerprinting)

TLS fingerprinting is a process used to identify and categorize encrypted network traffic.

It creates a unique identifier from the details of a [TLS client hello packet](https://serializethoughts.com/2014/07/27/dissecting-tls-client-hello-message), such as the version of TLS, supported cipher suites, and included extensions.

*   TLS fingerprints allow the unique identification of user session
*   JA3 and JA4 transform the TLS handshake details into a hash
*   The hash is used as a fingerprint to monitor and restrict access
*   The hash can then be read from your Functions through the request headers

### [Why track TLS fingerprints?](#why-track-tls-fingerprints)

Controlling access by TLS fingerprint allows us to mitigate malicious actors that use sophisticated methods of attack. For example, a DDoS attack that is spread across multiple user agents, IPs, or geographic locations might share the same TLS fingerprint. With fingerprinting, the Vercel Firewall can block all of the traffic that matches that TLS fingerprint.

#### [JA4](#ja4)

JA4 is part of the [JA4+ suite](https://github.com/FoxIO-LLC/ja4?tab=readme-ov-file#ja4-details). It offers a more granular and flexible approach to network fingerprinting, helping to mitigate malicious traffic and prevent bot traffic.

With JA4, it's possible to identify, track, and categorize server-side encrypted network traffic. This is crucial in detecting and mitigating potential security threats, as it provides a more comprehensive view of the network traffic when used in conjunction with other fields.

#### [JA3](#ja3)

JA3 is a tool that uses TLS fingerprinting to track and identify potential security threats. It specifically focuses on the details of the TLS client hello packet, generating a unique hash from it. This [client hello packet](https://serializethoughts.com/2014/07/27/dissecting-tls-client-hello-message) contains specific information such as the TLS version, supported cipher suites, and any extensions used.

#### [Monitor JA4 signatures](#monitor-ja4-signatures)

In the Allowed Requests view of the [Vercel WAF monitoring page](/docs/security/vercel-waf#traffic-monitoring), you can group the web traffic by JA4 Digest to review the fingerprints of the live traffic or the past 24 hours.

### [Request headers](#request-headers)

The following headers are sent to each deployment and can be used to process the [request](https://developer.mozilla.org/en-US/docs/Web/API/Request) before sending back a response. These headers can be read from the [Request](https://nodejs.org/api/http.html#http_message_headers) object in your [Function](/docs/functions/functions-api-reference#function-signature).

#### [`x-vercel-ja4-digest` (preferred)](#x-vercel-ja4-digest-preferred)

Unique client fingerprint hash generated by the JA4 algorithm. JA4 is preferred as it offers a more granular and flexible approach to network fingerprinting, which helps with mitigating malicious traffic.

#### [`x-vercel-ja3-digest`](#x-vercel-ja3-digest)

Unique client fingerprint hash generated by the JA3 algorithm.

--------------------------------------------------------------------------------
title: "Firewall Observability"
description: "Learn how firewall traffic monitoring and alerts help you react quickly to potential security threats."
last_updated: "null"
source: "https://vercel.com/docs/vercel-firewall/firewall-observability"
--------------------------------------------------------------------------------

# Firewall Observability

Copy page

Ask AI about this page

Last updated October 6, 2025

## [Traffic monitoring](#traffic-monitoring)

In the Firewall tab of your project, view a line graph displaying total incoming web traffic over a specific period for your production deployment. The default view shows an Overview of traffic for the past hour, and can be changed to show the last 24 hours or a live 10-minute window.

![Web traffic monitoring view with live 10-minute graph](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fsecurity%2Fvercel-waf-overview-graph-light.png&w=3840&q=75)![Web traffic monitoring view with live 10-minute graph](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fsecurity%2Fvercel-waf-overview-graph-dark.png&w=3840&q=75)

Web traffic monitoring view with live 10-minute graph

Use the following settings to change the monitoring view:

*   Traffic grouping:
    *   Overview: The default option shows the traffic grouped by Category (of [traffic control](/docs/vercel-firewall/firewall-observability#traffic-monitoring) rules) or Action (Allow, challenge, deny, or log) applied to the traffic with the firewall rules
    *   The remaining options show the traffic for the selected set by Region, IP Address, User Agent, Request Path, Route, [JA4](/docs/vercel-firewall/firewall-concepts#ja4) Digest, or Country
        *   Allowed Requests
        *   Custom Rule list: A list of your enabled custom rules
        *   Managed Ruleset list (Enterprise plan): A list of your enabled managed rulesets
*   Time period:
    *   Live (10-minute window)
    *   Past Hour
    *   Past Day (24 hours)
    *   Past 3 Days (72 hours, Enterprise plan)

## [Firewall Alerts](#firewall-alerts)

Firewall Alerts are available on [all plans](/docs/plans)

### [How alerts work](#how-alerts-work)

To help protect your site effectively, you can configure alerts to be notified of potential security threats and firewall actions. To do so, you can either create a webhook and subscribe to the listener URL or subscribe to the event through the Vercel Slack app.

### [DDoS attacks alerts](#ddos-attacks-alerts)

When Vercel's [DDoS Mitigation](/docs/security/ddos-mitigation) detects malicious traffic on your site that exceeds 100,000 requests over a 10-minute period, an alert is generated.

To receive notifications from these alerts, you can use one of the following methods:

*   Create a [webhook](/docs/webhooks) and subscribe to the URL to receive notifications
    1.  Follow the [configure a webhook](/docs/webhooks#configure-a-webhook) guide to create a webhook with the Attack Detected Firewall Event checked and the specific project(s) you would like to be notified about
    2.  Subscribe to the created webhook URL
*   Use the [Vercel Slack app](https://vercel.com/integrations/slack) to enable notifications for Attack Detected Firewall Events
    1.  Add the Slack app for your team by following the [Use the Vercel Slack app](/docs/comments/integrations#use-the-vercel-slack-app) guide

1.  Subscribe your team to DDoS attack alerts using your [`team_id`](/docs/accounts#find-your-team-id)
    *   Use the command `/vercel subscribe {team_id} firewall_attack`
2.  Review the [Vercel Slack app command reference](/docs/comments/integrations#vercel-slack-app-command-reference) for additional options.

--------------------------------------------------------------------------------
title: "Vercel WAF"
description: "Learn how to secure your website with the Vercel Web Application Firewall (WAF)"
last_updated: "null"
source: "https://vercel.com/docs/vercel-firewall/vercel-waf"
--------------------------------------------------------------------------------

# Vercel WAF

Copy page

Ask AI about this page

Last updated July 18, 2025

Vercel WAF is available on [all plans](/docs/plans)

Those with the [member](/docs/rbac/access-roles#member-role), [viewer](/docs/rbac/access-roles#viewer-role), [developer](/docs/rbac/access-roles#developer-role) and [administrator](/docs/rbac/access-roles#project-administrators) roles can access this feature

The Vercel WAF, part of the [Firewall](/docs/vercel-firewall), provides security controls to [monitor](/docs/vercel-firewall/firewall-observability#traffic-monitoring) and [control](/docs/vercel-firewall/firewall-observability#traffic-monitoring) the internet traffic to your site through logging, blocking and challenging. When you apply a configuration change to the firewall, it takes effect globally within 300ms and can be instantly [rolled back](#instant-rollback) to prior configurations.

*   [Configure your first Custom Rule](/docs/security/vercel-waf/custom-rules)
*   [Add IP Blocks](/docs/security/vercel-waf/ip-blocking)
*   [Explore Managed Rulesets](/docs/security/vercel-waf/managed-rulesets)

## [Traffic control](#traffic-control)

You can control the internet traffic to your website in the following ways:

*   IP blocking: Learn how to [configure IP blocking](/docs/security/vercel-waf/ip-blocking)
*   Custom rules: Learn how to [configure custom rules](/docs/security/vercel-waf/custom-rules) for your project
*   Managed rulesets: Learn how to [enable managed rulesets](/docs/security/vercel-waf/managed-rulesets) for your project (Enterprise plan)

## [Instant rollback](#instant-rollback)

You can quickly revert to a previous version of your firewall configuration. This can be useful in situations that require a quick recovery from unexpected behavior or rule creation.

To restore to a previous version:

1.  From your dashboard, select the project that you'd like to configure a rule for and then select the Firewall tab
2.  Select the View Audit Log option by clicking on the ellipsis menu at the top right
3.  Find the version that you would like to restore to by using the date and time selectors
4.  Select Restore and then Restore Configuration on the confirmation modal

## [Limits](#limits)

Depending on your plan, there are limits for each Vercel WAF feature.

| Feature | Hobby | Pro | Enterprise |
| --- | --- | --- | --- |
| [Project level IP Blocking](/docs/security/vercel-waf/ip-blocking#project-level-ip-blocking) | Up to 10 | Up to 100 | Custom |
| [Account-level IP Blocking](/docs/security/vercel-waf/ip-blocking#account-level-ip-blocking) | N/A | N/A | Custom |
| [Custom Rules](/docs/security/vercel-waf/custom-rules) | Up to 3 | Up to 40 | Up to 1000 |
| [Custom Rule Parameters](/docs/security/vercel-waf/rule-configuration#parameters) | All | All | All |
| [Managed Rulesets](/docs/security/vercel-waf/managed-rulesets) | N/A | N/A | Contact sales |

*   For Account-level IP Blocking, CIDR rules are limited to `/16` for IPv4 and `/48` for IPv6
*   For Custom Rule Parameters, JA3 (Legacy) is available on Enterprise plans

--------------------------------------------------------------------------------
title: "WAF Custom Rules"
description: "Learn how to add and manage custom rules to configure the Vercel Web Application Firewall (WAF)."
last_updated: "null"
source: "https://vercel.com/docs/vercel-firewall/vercel-waf/custom-rules"
--------------------------------------------------------------------------------


---

**Navigation:** [← Previous](./38-creates-a-webhook.md) | [Index](./index.md) | [Next →](./40-waf-custom-rules.md)
