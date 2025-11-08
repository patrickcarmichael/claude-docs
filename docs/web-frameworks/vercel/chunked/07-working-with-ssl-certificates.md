**Navigation:** [← Previous](./06-trusted-ips.md) | [Index](./index.md) | [Next →](./08-framework-environment-variables.md)

---

# Working with SSL Certificates

Copy page

Ask AI about this page

Last updated September 24, 2025

An SSL certificate enables encrypted communication between user's browser and your web server to be encrypted. The certificate is installed on the web server and allows for website authentication and data encryption. This is particularly important if you are working with any sort of authentication and personal or financial data.

SSL certificates are issued from a certificate authority (CA) for each domain. While it is possible to [create and upload your own custom certificate](custom-SSL-certificate), Vercel will automatically try to generate a certificate for every domain once it is added to a project, regardless of if it was registered through Vercel or not. However, it will only work once the certificate validation request is successful, which happens once DNS records are added and propagated.

Vercel uses LetsEncrypt for certificates. For all non-wildcard domains, we use the [HTTP-01 challenge method](https://letsencrypt.org/docs/challenge-types/#http-01-challenge) and providing the request can make it to Vercel, then our infrastructure will deal with it. For wildcard requests, we use the [DNS-01 challenge method](https://letsencrypt.org/docs/challenge-types/#dns-01-challenge). This is why we require nameservers to be with Vercel to use wildcard domains - if the DNS isn't with us, we can't make the DNS record to approve it.

Issuing a certificate happens in the following way:

1.  Vercel asks LetsEncrypt for a certificate for that domain and asks how it can prove control of the domain
2.  Let's Encrypt reviews the domain and issues Vercel with a [challenge](https://letsencrypt.org/docs/challenge-types/) in order to authorise the certificate to be generated. This is usually in the format of creating a file or DNS record with a particular code.
3.  Vercel creates that file with the code on the HTTP-01 or DNS-01 validation path and tells LetsEncrypt it's done
4.  LetsEncrypt then check to see if the file is there and if they can see the file, they send us the certificate
5.  Vercel then adds the certificate to our infrastructure and it then starts working on HTTPS

For information about when SSL certificate renewals happen, see [When is the SSL Certificate on my Vercel Domain renewed?](https://vercel.com/guides/renewal-of-ssl-certificates-with-a-vercel-domain)

The /.well-known path is reserved and cannot be redirected or rewritten. Only Enterprise teams can configure custom SSL. [Contact sales](/contact/sales) to learn more.

## [Troubleshooting](#troubleshooting)

To learn more about common SSL issues, see the [troubleshooting](/docs/domains/troubleshooting#common-ssl-certificate-issues) doc.

## [Related](#related)

[

#### Domains overview

Learn the concepts behind how domains work

](/docs/domains)

[

#### Working with Domains

Learn how domains work and the options Vercel provides for managing them.

](/docs/domains/working-with-domains)

[

#### Working with DNS

Learn how DNS works in order to properly configure your domain.

](/docs/domains/working-with-dns)

[

#### Working with Nameservers

Learn about nameservers and the benefits Vercel nameservers provide.

](/docs/domains/working-with-nameservers)

[

#### Troubleshooting Domains

Learn about common reasons for domain misconfigurations and how to troubleshoot your domain on Vercel.

](/docs/domains/troubleshooting)

--------------------------------------------------------------------------------
title: "Draft Mode"
description: "Vercel's Draft Mode enables you to view your unpublished headless CMS content on your site before publishing it."
last_updated: "null"
source: "https://vercel.com/docs/draft-mode"
--------------------------------------------------------------------------------

# Draft Mode

Copy page

Ask AI about this page

Last updated September 24, 2025

Draft Mode lets you view your unpublished headless CMS content on your website rendered with all the normal styling and layout that you would see once published.

Both [Next.js](/docs/frameworks/nextjs#draft-mode) and [SvelteKit](/docs/frameworks/sveltekit#draft-mode) support Draft Mode. Any framework that uses the [Build Output API](/docs/build-output-api/v3) can support Draft Mode by adding the `bypassToken` option to [prerender configuration](/docs/build-output-api/v3/primitives#prerender-functions).

Draft Mode was called Preview Mode before the release of Next.js [13.4](https://nextjs.org/blog/next-13-4). The name was changed to avoid confusion with [preview deployments](/docs/deployments/environments#preview-environment-pre-production), which is a different product.

You can use Draft Mode if you:

1.  Use [Incremental Static Regeneration (ISR)](/docs/incremental-static-regeneration) to fetch and render data from a headless CMS
2.  Want to view your unpublished headless CMS content on your site without rebuilding your pages when you make changes
3.  Want to protect your unpublished content from being viewed publicly

## [How Draft Mode works](#how-draft-mode-works)

Draft Mode allows you to bypass [ISR](/docs/incremental-static-regeneration) caching to fetch the latest CMS content at request time. This is useful for seeing your draft content on your website without waiting for the cache to refresh, or manually revalidating the page.

The process works like this:

1.  Each ISR route has a `bypassToken` configuration option, which is assigned a generated, cryptographically-secure value at build time
2.  When someone visits an ISR route with a `bypassToken` configured, the page will check for a `__prerender_bypass` cookie
3.  If the `__prerender_bypass` cookie exists and has the same value as the `bypassToken` your project is using, the visitor will view the page in Draft Mode

Only team members will be able to view pages in Draft Mode.

## [Getting started](#getting-started)

To use Draft Mode with Next.js on Vercel, you must:

1.  [Enable ISR](/docs/incremental-static-regeneration) on pages that fetch content. Using ISR is required on pages that you want to view in Draft Mode
    
2.  Add code to your ISR pages to detect when Draft Mode is enabled and render the draft content
    
3.  Toggle Draft Mode in the Vercel Toolbar by selecting Draft Mode in [the toolbar menu](/docs/vercel-toolbar#using-the-toolbar-menu) to view your draft content. Once toggled, the toolbar will turn purple, indicating that Draft Mode is enabled
    
    Next.js (/app)Next.js (/pages)SvelteKit
    
    app/page.tsx
    
    TypeScript
    
    TypeScriptJavaScript
    
    ```
    import { draftMode } from 'next/headers';
     
    async function getContent() {
      const { isEnabled } = await draftMode();
     
      const contentUrl = isEnabled
        ? 'https://draft.example.com'
        : 'https://production.example.com';
     
      // This line enables ISR, required for draft mode
      const res = await fetch(contentUrl, { next: { revalidate: 120 } });
     
      return res.json();
    }
     
    export default async function Page() {
      const { title, desc } = await getContent();
     
      return (
        <main>
          <h1>{title}</h1>
          <p>{desc}</p>
        </main>
      );
    }
    ```
    

See the Next.js docs to learn how to use Draft Mode with self-hosted Next.js projects:

*   [App Router](https://nextjs.org/docs/app/building-your-application/configuring/draft-mode)
*   [Pages Router](https://nextjs.org/docs/pages/building-your-application/configuring/draft-mode)

Once implemented, team members can access Draft Mode from the Vercel Toolbar by selecting the eye icon . Once selected, the toolbar will turn purple to indicate that Draft Mode is enabled.

## [Sharing drafts](#sharing-drafts)

To share a draft URL, it must have the `?__vercel_draft=1` query parameter. For example:

```
https://my-site.com/blog/post-01?__vercel_draft=1
```

Viewers outside your Vercel team cannot enable Draft Mode or see your draft content, even with a draft URL.

--------------------------------------------------------------------------------
title: "Working with Drains"
description: "Drains collect logs, traces, speed insights, and analytics from your applications. Forward observability data to custom endpoints or popular services."
last_updated: "null"
source: "https://vercel.com/docs/drains"
--------------------------------------------------------------------------------

# Working with Drains

Copy page

Ask AI about this page

Last updated October 16, 2025

Drains are available on [Enterprise](/docs/plans/enterprise) and [Pro](/docs/plans/pro) plans

Drains let you forward observability data from your applications to external services for debugging, performance optimization, analysis, and alerting, so that you can:

*   Store observability data persistently in your preferred external services
*   Process large volumes of telemetry data using your own tools
*   Set up alerts based on application behavior patterns
*   Build custom metrics and dashboards from your data

## [Getting started with Drains](#getting-started-with-drains)

You can add Drains in two ways:

*   Custom endpoints: [Configure](/docs/drains/using-drains#configuring-drains) any data type to send to a [custom HTTP endpoint](/docs/drains/using-drains#custom-endpoint)
*   Native integrations: [Configure](/docs/drains/using-drains#configuring-drains) logs and trace data types to send to popular services like Dash0 and Braintrust using [native integrations](/docs/drains/using-drains#native-integrations)

Learn how to [manage your active drains](/docs/drains/using-drains#managing-your-active-drains).

## [Data types](#data-types)

You can drain four types of data:

*   Logs: Runtime, build, and static logs from your deployments (supports custom endpoints and native integrations)
*   Traces: Distributed tracing data in OpenTelemetry format (supports custom endpoints and native integrations)
*   Speed Insights: Performance metrics and web vitals (custom endpoints only)
*   Web Analytics: Page views and custom events (custom endpoints only)

### [Data type references](#data-type-references)

Each drain data type has specific formats, fields, and schemas. Review the reference documentation for [logs](/docs/drains/reference/logs), [traces](/docs/drains/reference/traces), [speed insights](/docs/drains/reference/speed-insights), and [analytics](/docs/drains/reference/analytics) to understand the data structure you'll receive from each data type.

## [Security](#security)

You can secure your drains by checking for valid signatures and hiding IP addresses. Learn how to [add security to your drains](/docs/drains/security).

## [Usage and pricing](#usage-and-pricing)

Drains are available to all users on the [Pro](/docs/plans/pro) and [Enterprise](/docs/plans/enterprise) plans. If you are on the [Hobby](/docs/plans/hobby) or [Pro Trial](/docs/plans/pro-plan/trials) plan, you'll need to [upgrade to Pro](/docs/plans/hobby#upgrading-to-pro) to access drains.

Drains usage is billed based on the pricing table below. Pricing is the same regardless of data type:

Managed Infrastructure pricing
| 
Resource

 | 

Unit (Billing Cycle)

 |
| --- | --- |
| 

[Drains](/docs/drains#usage-and-pricing)

 | $0.50 per 1 GB |

To learn more about Managed Infrastructure on the Pro plan, and how to understand your invoices, see [understanding my invoice.](/docs/pricing/understanding-my-invoice)

See [Optimizing Drains](/docs/pricing/observability#optimizing-drains-usage) for information on how to manage costs associated with Drains.

## [More resources](#more-resources)

For more information on Drains, check out the following resources:

*   [Configure Drains](/docs/drains/using-drains)
*   [Log Drains reference](/docs/drains/reference/logs)
*   [Traces reference](/docs/drains/reference/traces)
*   [Speed Insights reference](/docs/drains/reference/speed-insights)
*   [Analytics reference](/docs/drains/reference/analytics)

--------------------------------------------------------------------------------
title: "Web Analytics Drains Reference"
description: "Learn about Web Analytics Drains - data formats and custom events configuration."
last_updated: "null"
source: "https://vercel.com/docs/drains/reference/analytics"
--------------------------------------------------------------------------------

# Web Analytics Drains Reference

Copy page

Ask AI about this page

Last updated September 24, 2025

If a Web Analytics Drains has been configured, Vercel will send page views and custom events from your applications to external endpoints for storage and analysis over HTTPS when your application tracks events.

## [Web Analytics Schema](#web-analytics-schema)

The following table describes the possible fields that are sent via Web Analytics Drains:

| Name | Type | Description | Example |
| --- | --- | --- | --- |
| `schema` | string | Schema version identifier | `vercel.analytics.v1` |
| `eventType` | string | Type of analytics event | `pageview` or `event` |
| `eventName` | string | Name of the custom event | `button_click` |
| `eventData` | string | Additional data associated with the event | `{"button": "signup"}` |
| `timestamp` | number | Unix timestamp when the event was recorded | 1694723400000 |
| `projectId` | string | Identifier for the Vercel project | `Qmc52npNy86S8VV4Mt8a8dP1LEkRNbgosW3pBCQytkcgf2` |
| `ownerId` | string | Identifier for the project owner | `team_nLlpyC6REAqxydlFKbrMDlud` |
| `dataSourceName` | string | Name of the data source | `web-analytics` |
| `sessionId` | number | Unique session identifier | 12345 |
| `deviceId` | number | Unique device identifier | 67890 |
| `origin` | string | Origin URL where the event was recorded | `https://example.com` |
| `path` | string | URL path where the event was recorded | `/dashboard` |
| `referrer` | string | Referrer URL | `https://google.com` |
| `queryParams` | string | Query parameters from the URL | `utm_source=google&utm_medium=cpc` |
| `route` | string | Route pattern for the page | `/dashboard/[id]` |
| `country` | string | Country code of the user | `US` |
| `region` | string | Region code of the user | `CA` |
| `city` | string | City of the user | `San Francisco` |
| `osName` | string | Operating system name | `macOS` |
| `osVersion` | string | Operating system version | `13.4` |
| `clientName` | string | Client browser name | `Chrome` |
| `clientType` | string | Type of client | `browser` |
| `clientVersion` | string | Client browser version | `114.0.5735.90` |
| `deviceType` | string | Type of device | `desktop` |
| `deviceBrand` | string | Device brand | `Apple` |
| `deviceModel` | string | Device model | `MacBook Pro` |
| `browserEngine` | string | Browser engine name | `Blink` |
| `browserEngineVersion` | string | Browser engine version | `114.0.5735.90` |
| `sdkVersion` | string | SDK version used to track events | `2.1.0` |
| `sdkName` | string | SDK name used to track events | `@vercel/analytics` |
| `sdkVersionFull` | string | Full SDK version string | `2.1.0-beta.1` |
| `vercelEnvironment` | string | Vercel environment | `production` |
| `vercelUrl` | string | Vercel deployment URL | `*.vercel.app` |
| `flags` | string | Feature flags information | `{"feature_a": true}` |
| `deployment` | string | Identifier for the Vercel deployment | `dpl_2YZzo1cJAjijSf1hwDFK5ayu2Pid` |

## [Format](#format)

Vercel supports the following formats for Web Analytics Drains, which you can configure when [setting the Drain destination](/docs/drains/using-drains#configure-destination):

### [JSON](#json)

Vercel sends Web Analytics data as JSON arrays containing event objects:

```
[
  { "schema": "vercel.analytics.v1", "eventType": "pageview", "timestamp": 1694723400000, "projectId": "Qmc52npNy86S8VV4Mt8a8dP1LEkRNbgosW3pBCQytkcgf2", "ownerId": "team_nLlpyC6REAqxydlFKbrMDlud", "dataSourceName": "web-analytics", "sessionId": 12345, "deviceId": 67890, "origin": "https://example.com", "path": "/dashboard" },
  { "schema": "vercel.analytics.v1", "eventType": "event", "eventName": "button_click", "eventData": "{\"button\": \"signup\"}", "timestamp": 1694723405000, "projectId": "Qmc52npNy86S8VV4Mt8a8dP1LEkRNbgosW3pBCQytkcgf2", "ownerId": "team_nLlpyC6REAqxydlFKbrMDlud", "dataSourceName": "web-analytics", "sessionId": 12345, "deviceId": 67890, "origin": "https://example.com", "path": "/signup" }
]
```

### [NDJSON](#ndjson)

Vercel sends Web Analytics data as newline-delimited JSON objects:

```
{"schema": "vercel.analytics.v1","eventType": "pageview","timestamp": 1694723400000,"projectId": "Qmc52npNy86S8VV4Mt8a8dP1LEkRNbgosW3pBCQytkcgf2","ownerId": "team_nLlpyC6REAqxydlFKbrMDlud","dataSourceName": "web-analytics","sessionId": 12345,"deviceId": 67890,"origin": "https://example.com","path": "/dashboard"}
{"schema": "vercel.analytics.v1","eventType": "event","eventName": "button_click","eventData": "{\"button\": \"signup\"}","timestamp": 1694723405000,"projectId": "Qmc52npNy86S8VV4Mt8a8dP1LEkRNbgosW3pBCQytkcgf2","ownerId": "team_nLlpyC6REAqxydlFKbrMDlud","dataSourceName": "web-analytics","sessionId": 12345,"deviceId": 67890,"origin": "https://example.com","path": "/signup"}
```

## [Sampling Rate](#sampling-rate)

When you configure a Web Analytics Drain in the Vercel UI, you can set the sampling rate to control the volume of data sent. This helps manage costs when you have high traffic volumes.

## [More resources](#more-resources)

For more information on Web Analytics Drains and how to use them, refer to the following resources:

*   [Drains overview](/docs/drains)
*   [Configure Drains](/docs/drains/using-drains)

--------------------------------------------------------------------------------
title: "Log Drains Reference"
description: "Learn about Log Drains - data formats, sources, environments, and security configuration."
last_updated: "null"
source: "https://vercel.com/docs/drains/reference/logs"
--------------------------------------------------------------------------------

# Log Drains Reference

Copy page

Ask AI about this page

Last updated October 31, 2025

Log Drains forward logs from your deployments to external endpoints for storage and analysis. You can configure Log Drains in two ways:

*   [Custom endpoint](/docs/drains/using-drains#custom-endpoint): Send logs to any HTTP endpoint you configure
*   [Native integration](/docs/drains/using-drains#native-integrations): Use integrations from the Vercel Marketplace like [Dash0](https://vercel.com/marketplace/dash0)

Vercel sends logs to endpoints over HTTPS every time your deployments generate logs. Multiple logs may be batched into a single request when possible to optimize delivery performance.

## [Logs Schema](#logs-schema)

The following table describes the possible fields that are sent via Log Drains:

| Name | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `id` | string | Yes | Unique identifier for the log entry | `1573817187330377061717300000` |
| `deploymentId` | string | Yes | Identifier for the Vercel deployment | `dpl_233NRGRjVZX1caZrXWtz5g1TAksD` |
| `source` | enum | Yes | Origin of the log | `build`, `edge`, `lambda`, `static`, `external`, `firewall`, or `redirect` |
| `host` | string | Yes | Hostname of the request | `test.vercel.app` |
| `timestamp` | number | Yes | Unix timestamp when the log was generated | 1573817187330 |
| `projectId` | string | Yes | Identifier for the Vercel project | `gdufoJxB6b9b1fEqr1jUtFkyavUU` |
| `level` | enum | Yes | Log severity level | `info`, `warning`, `error`, or `fatal` |
| `message` | string | No | Log message content (may be truncated if over 256 KB) | `Adding customer to database...` |
| `buildId` | string | No | Identifier for the Vercel build | `bld_cotnkcr76` (only present on build logs) |
| `entrypoint` | string | No | Entrypoint for the request | `api/index.js` |
| `destination` | string | No | Origin of the external content | `https://vitals.vercel-insights.com/v1` (only on `external` and `redirect` logs) |
| `path` | string | No | Function or dynamic path of the request | `/dynamic/[route].json` |
| `type` | string | No | Log output type | `command`, `stdout`, `stderr`, `exit`, `deployment-state`, `delimiter`, `middleware`, `middleware-invocation`, `edge-function-invocation`, `metric`, `report`, `fatal` |
| `statusCode` | number | No | HTTP status code of the request | 200 (`-1` means no response returned and the lambda crashed) |
| `requestId` | string | No | Identifier of the request | `643af4e3-975a-4cc7-9e7a-1eda11539d90` |
| `environment` | enum | No | Deployment environment | `production` or `preview` |
| `branch` | string | No | Git branch name | `main` |
| `ja3Digest` | string | No | JA3 fingerprint digest | `769c83e5b...` |
| `ja4Digest` | string | No | JA4 fingerprint digest | `t13d1516h2...` |
| `edgeType` | enum | No | Type of edge runtime | `edge-function` or `middleware` |
| `projectName` | string | No | Name of the Vercel project | `my-app` |
| `executionRegion` | string | No | Region where the request is executed | `sfo1` |
| `traceId` | string | No | Trace identifier for distributed tracing | `1b02cd14bb8642fd092bc23f54c7ffcd` |
| `spanId` | string | No | Span identifier for distributed tracing | `f24e8631bd11faa7` |
| `trace.id` | string | No | Trace | `1b02cd14bb8642fd092bc23f54c7ffcd` |
| `span.id` | string | No | Span | `f24e8631bd11faa7` |
| `proxy` | object | No | Contains information about proxy requests | See proxy fields below |
| `proxy.timestamp` | number | Yes\* | Unix timestamp when the proxy request was made | 1573817250172 |
| `proxy.method` | string | Yes\* | HTTP method of the request | `GET` |
| `proxy.host` | string | Yes\* | Hostname of the request | `test.vercel.app` |
| `proxy.path` | string | Yes\* | Request path with query parameters | `/dynamic/some-value.json?route=some-value` |
| `proxy.userAgent` | array | Yes\* | User agent strings of the request | `["Mozilla/5.0..."]` |
| `proxy.region` | string | Yes\* | Region where the request is processed | `sfo1` |
| `proxy.referer` | string | No | Referer of the request | `*.vercel.app` |
| `proxy.statusCode` | number | No | HTTP status code of the proxy request | 200 (`-1` means revalidation occurred in the background) |
| `proxy.clientIp` | string | No | Client IP address | `120.75.16.101` |
| `proxy.scheme` | string | No | Protocol of the request | `https` |
| `proxy.responseByteSize` | number | No | Size of the response in bytes | 1024 |
| `proxy.cacheId` | string | No | Original request ID when request is served from cache | `pdx1::v8g4b-1744143786684-93dafbc0f70d` |
| `proxy.pathType` | string | No | How the request was served based on its path and project configuration | `func`, `prerender`, `background_func`, `edge`, `middleware`, `streaming_func`, `partial_prerender`, `external`, `static`, `not_found`, `unknown`, `api` |
| `proxy.pathTypeVariant` | string | No | Variant of the path type | `api` |
| `proxy.vercelId` | string | No | Vercel-specific identifier | `sfo1::abc123` |
| `proxy.vercelCache` | enum | No | Cache status sent to the browser | `MISS`, `HIT`, `STALE`, `BYPASS`, `PRERENDER`, `REVALIDATED` |
| `proxy.lambdaRegion` | string | No | Region where lambda function executed | `sfo1` |
| `proxy.wafAction` | enum | No | Action taken by firewall rules | `log`, `challenge`, `deny`, `bypass`, `rate_limit` |
| `proxy.wafRuleId` | string | No | ID of the firewall rule that matched | `rule_gAHz8jtSB1Gy` |

\*Required when `proxy` object is present

## [Format](#format)

Vercel supports the following formats for Log Drains. You can configure the format when [configuring the Drain destination](/docs/drains/using-drains#configure-destination):

### [JSON](#json)

Vercel sends logs as JSON arrays containing log objects:

```
{ "id": "1573817187330377061717300000", "deploymentId": "dpl_233NRGRjVZX1caZrXWtz5g1TAksD", "source": "build", "host": "my-app-abc123.vercel.app", "timestamp": 1573817187330, "projectId": "gdufoJxB6b9b1fEqr1jUtFkyavUU", "level": "info", "message": "Build completed successfully", "buildId": "bld_cotnkcr76", "type": "stdout", "projectName": "my-app" }
{ "id": "1573817250283254651097202070", "deploymentId": "dpl_233NRGRjVZX1caZrXWtz5g1TAksD", "source": "lambda", "host": "my-app-abc123.vercel.app", "timestamp": 1573817250283, "projectId": "gdufoJxB6b9b1fEqr1jUtFkyavUU", "level": "info", "message": "API request processed", "entrypoint": "api/index.js", "requestId": "643af4e3-975a-4cc7-9e7a-1eda11539d90", "statusCode": 200, "path": "/api/users", "executionRegion": "sfo1", "environment": "production", "traceId": "1b02cd14bb8642fd092bc23f54c7ffcd", "spanId": "f24e8631bd11faa7", "trace.id": "1b02cd14bb8642fd092bc23f54c7ffcd", "span.id": "f24e8631bd11faa7", "proxy": { "timestamp": 1573817250172, "method": "GET", "host": "my-app.vercel.app", "path": "/api/users?page=1", "userAgent": ["Mozilla/5.0..."], "referer": "https://my-app.vercel.app", "region": "sfo1", "statusCode": 200, "clientIp": "120.75.16.101", "scheme": "https", "vercelCache": "MISS" } }
```

### [NDJSON](#ndjson)

Vercel sends logs as newline-delimited JSON objects:

```
{"id": "1573817187330377061717300000","deploymentId": "dpl_233NRGRjVZX1caZrXWtz5g1TAksD","source": "build","host": "my-app-abc123.vercel.app","timestamp": 1573817187330,"projectId": "gdufoJxB6b9b1fEqr1jUtFkyavUU","level": "info","message": "Build completed successfully","buildId": "bld_cotnkcr76","type": "stdout","projectName": "my-app"}
{"id": "1573817250283254651097202070","deploymentId": "dpl_233NRGRjVZX1caZrXWtz5g1TAksD","source": "lambda","host": "my-app-abc123.vercel.app","timestamp": 1573817250283,"projectId": "gdufoJxB6b9b1fEqr1jUtFkyavUU","level": "info","message": "API request processed","entrypoint": "api/index.js","requestId": "643af4e3-975a-4cc7-9e7a-1eda11539d90","statusCode": 200,"path": "/api/users","executionRegion": "sfo1","environment": "production","traceId": "1b02cd14bb8642fd092bc23f54c7ffcd","spanId": "f24e8631bd11faa7","trace.id": "1b02cd14bb8642fd092bc23f54c7ffcd","span.id": "f24e8631bd11faa7","proxy": {"timestamp": 1573817250172,"method": "GET","host": "my-app.vercel.app","path": "/api/users?page=1","userAgent": ["Mozilla/5.0..."],"referer": "https://my-app.vercel.app","region": "sfo1","statusCode": 200,"clientIp": "120.75.16.101","scheme": "https","vercelCache": "MISS"}}
```

## [Log Sources](#log-sources)

When you configure a Log Drain in the Vercel UI, you can set which sources to receive logs from:

| value | Details |
| --- | --- |
| `static` | Requests to static assets like HTML and CSS files |
| `lambda` | Output from Vercel Functions like [API Routes](/docs/functions) |
| `edge` | Output from Vercel Functions using Edge runtime |
| `build` | Output from the [Build Step](/docs/deployments/configure-a-build) |
| `external` | External [rewrites](/docs/project-configuration#rewrites) to a different domain. Includes [cached external rewrites](/docs/rewrites#caching-external-rewrites) |
| `firewall` | Outputs log data from requests denied by [Vercel Firewall](/docs/vercel-firewall) rules |
| `redirect` | Requests that are redirected by [redirect rules](/docs/project-configuration#redirects) |

## [Log Environments](#log-environments)

When you configure a Log Drain in the Vercel UI, you can set which environments to receive logs from:

| value | Details |
| --- | --- |
| `production` | Logs from production deployments with assigned domain(s) |
| `preview` | Logs from deployments accessed through the [generated deployment URL](/docs/deployments/generated-urls) |

## [Sampling Rate](#sampling-rate)

When you configure a Log Drain in the Vercel UI, you can set the sampling rate to control the volume of data sent. This helps manage costs when you have high traffic volumes.

## [More resources](#more-resources)

For more information on Log Drains and how to use them, check out the following resources:

*   [Drains overview](/docs/drains)
*   [Configure Drains](/docs/drains/using-drains)

--------------------------------------------------------------------------------
title: "Speed Insights Drains Reference"
description: "Learn about Speed Insights Drains - data formats and performance metrics configuration."
last_updated: "null"
source: "https://vercel.com/docs/drains/reference/speed-insights"
--------------------------------------------------------------------------------

# Speed Insights Drains Reference

Copy page

Ask AI about this page

Last updated September 24, 2025

Speed Insights Drains send performance metrics and web vitals from your applications to external endpoints for storage and analysis. To enable Speed Insights Drains, [create a drain](/docs/drains/using-drains) and choose the Speed Insights data type.

Vercel sends Speed Insights data to endpoint URLs over HTTPS when your application collects performance metrics.

## [Speed Insights Schema](#speed-insights-schema)

The following table describes the possible fields that are sent via Speed Insights Drains:

| Name | Type | Description | Example |
| --- | --- | --- | --- |
| `schema` | string | Schema version identifier | `vercel.speed_insights.v1` |
| `timestamp` | string | ISO timestamp when the metric was collected | `2023-09-14T15:30:00.000Z` |
| `projectId` | string | Identifier for the Vercel project | `Qmc52npNy86S8VV4Mt8a8dP1LEkRNbgosW3pBCQytkcgf2` |
| `ownerId` | string | Identifier for the project owner | `team_nLlpyC6REAqxydlFKbrMDlud` |
| `deviceId` | number | Unique device identifier | 12345 |
| `metricType` | string | Type of performance metric | `CLS`, `LCP`, `FID`, `FCP`, `TTFB`, `INP` |
| `value` | number | Metric value | 0.1 |
| `origin` | string | Origin URL where the metric was collected | `https://example.com` |
| `path` | string | URL path where the metric was collected | `/dashboard` |
| `route` | string | Route pattern for the page | `/dashboard/[id]` |
| `country` | string | Country code of the user | `US` |
| `region` | string | Region code of the user | `CA` |
| `city` | string | City of the user | `San Francisco` |
| `osName` | string | Operating system name | `macOS` |
| `osVersion` | string | Operating system version | `13.4` |
| `clientName` | string | Client browser name | `Chrome` |
| `clientType` | string | Type of client | `browser` |
| `clientVersion` | string | Client browser version | `114.0.5735.90` |
| `deviceType` | string | Type of device | `desktop` |
| `deviceBrand` | string | Device brand | `Apple` |
| `connectionSpeed` | string | Network connection speed | `4g` |
| `browserEngine` | string | Browser engine name | `Blink` |
| `browserEngineVersion` | string | Browser engine version | `114.0.5735.90` |
| `scriptVersion` | string | Speed Insights script version | `1.0.0` |
| `sdkVersion` | string | SDK version used to collect metrics | `2.1.0` |
| `sdkName` | string | SDK name used to collect metrics | `@vercel/speed-insights` |
| `vercelEnvironment` | string | Vercel environment | `production` |
| `vercelUrl` | string | Vercel deployment URL | `*.vercel.app` |
| `deploymentId` | string | Identifier for the Vercel deployment | `dpl_2YZzo1cJAjijSf1hwDFK5ayu2Pid` |
| `attribution` | string | Attribution information for the metric | `attribution-data` |

## [Format](#format)

Vercel supports the following formats for Speed Insights Drains. You can configure the format when [configuring the Drain destination](/docs/drains/using-drains#configure-destination):

### [JSON](#json)

Vercel sends Speed Insights data as JSON arrays containing metric objects:

```
[
  { "schema": "vercel.speed_insights.v1", "timestamp": "2023-09-14T15:30:00.000Z", "projectId": "Qmc52npNy86S8VV4Mt8a8dP1LEkRNbgosW3pBCQytkcgf2", "ownerId": "team_nLlpyC6REAqxydlFKbrMDlud", "deviceId": 12345, "metricType": "CLS", "value": 0.1, "origin": "https://example.com", "path": "/dashboard" },
  { "schema": "vercel.speed_insights.v1", "timestamp": "2023-09-14T15:30:05.000Z", "projectId": "Qmc52npNy86S8VV4Mt8a8dP1LEkRNbgosW3pBCQytkcgf2", "ownerId": "team_nLlpyC6REAqxydlFKbrMDlud", "deviceId": 67890, "metricType": "LCP", "value": 2.5, "origin": "https://example.com", "path": "/home" }
]
```

### [NDJSON](#ndjson)

Vercel sends Speed Insights data as newline-delimited JSON objects:

```
{"schema": "vercel.speed_insights.v1","timestamp": "2023-09-14T15:30:00.000Z","projectId": "Qmc52npNy86S8VV4Mt8a8dP1LEkRNbgosW3pBCQytkcgf2","ownerId": "team_nLlpyC6REAqxydlFKbrMDlud","deviceId": 12345,"metricType": "CLS","value": 0.1,"origin": "https://example.com","path": "/dashboard"}
{"schema": "vercel.speed_insights.v1","timestamp": "2023-09-14T15:30:05.000Z","projectId": "Qmc52npNy86S8VV4Mt8a8dP1LEkRNbgosW3pBCQytkcgf2","ownerId": "team_nLlpyC6REAqxydlFKbrMDlud","deviceId": 67890,"metricType": "LCP","value": 2.5,"origin": "https://example.com","path": "/home"}
```

## [Sampling Rate](#sampling-rate)

When you configure a Speed Insights Drain in the Vercel UI, you can set the sampling rate to control the volume of data sent. This helps manage costs when you have high traffic volumes.

## [More resources](#more-resources)

For more information on Speed Insights Drains and how to use them, check out the following resources:

*   [Drains overview](/docs/drains)
*   [Configure Drains](/docs/drains/using-drains)

--------------------------------------------------------------------------------
title: "Trace Drains Reference"
description: "Learn about Trace Drains - OpenTelemetry-compliant distributed tracing data formats and configuration."
last_updated: "null"
source: "https://vercel.com/docs/drains/reference/traces"
--------------------------------------------------------------------------------

# Trace Drains Reference

Copy page

Ask AI about this page

Last updated October 30, 2025

Trace Drains forward distributed tracing data from your deployments to external endpoints for storage and analysis. You can configure Trace Drains in two ways:

*   [Custom endpoint](/docs/drains/using-drains#custom-endpoint): Send traces to any HTTP endpoint you configure
*   [Native integration](/docs/drains/using-drains#native-integrations): Use integrations from the Vercel Marketplace like [Braintrust](https://vercel.com/marketplace/braintrust)

Vercel sends traces to endpoints over HTTPS following the [OpenTelemetry Protocol (OTLP)](https://opentelemetry.io/docs/concepts/signals/traces/) specification.

## [Traces Schema](#traces-schema)

Trace Drains follow the [OpenTelemetry traces specification](https://opentelemetry.io/docs/concepts/signals/traces/). Vercel automatically adds these specific resource attributes to all traces:

| Name | Type | Description | Example |
| --- | --- | --- | --- |
| `vercel.projectId` | string | Identifier for the Vercel project | `"Qmc52npNy86S8VV4Mt8a8dP1LEkRNbgosW3pBCQytkcgf2"` |
| `vercel.deploymentId` | string | Identifier for the Vercel deployment | `"dpl_2YZzo1cJAjijSf1hwDFK5ayu2Pid"` |

## [Format](#format)

Vercel supports the following formats for Trace Drains. You can configure the format when [configuring the Drain destination](/docs/drains/using-drains#configure-destination):

### [JSON](#json)

Vercel sends traces as JSON objects following the OpenTelemetry specification:

```
{ "resourceSpans": [{ "resource": { "attributes": [{ "key": "service.name", "value": { "stringValue": "vercel-function" } }] }, "scopeSpans": [{ "scope": { "name": "vercel" }, "spans": [{ "traceId": "7bba9f33312b3dbb8b2c2c62bb7abe2d", "spanId": "086e83747d0e381e", "name": "GET /api/users", "kind": "server", "startTimeUnixNano": "1694723400000000000", "endTimeUnixNano": "1694723400150000000" }] }] }] }
```

### [Protobuf](#protobuf)

Vercel sends traces in binary protobuf format following the OTLP/HTTP specification. This format is more efficient for high-volume trace data transmission.

## [Sampling Rate](#sampling-rate)

When you configure a Trace Drain in the Vercel UI, you can set the sampling rate to control the volume of data sent. This helps manage costs when you have high traffic volumes.

## [Limitations](#limitations)

Custom spans from functions using the [Edge runtime](/docs/functions/runtimes/edge) are not forwarded via the Trace Drain.

## [More resources](#more-resources)

For more information on Trace Drains and how to use them, check out the following resources:

*   [Drains overview](/docs/drains)
*   [Configure Drains](/docs/drains/using-drains)
*   [OpenTelemetry traces specification](https://opentelemetry.io/docs/concepts/signals/traces/)

--------------------------------------------------------------------------------
title: "Drains Security"
description: "Learn how to secure your Drains endpoints with authentication and signature verification."
last_updated: "null"
source: "https://vercel.com/docs/drains/security"
--------------------------------------------------------------------------------

# Drains Security

Copy page

Ask AI about this page

Last updated October 9, 2025

All Drains support transport-level encryption using HTTPS protocol.

When your server starts receiving payloads, a third party could send data to your server if it knows the URL. Therefore, you should verify the request is coming from Vercel.

## [Secure Drains](#secure-drains)

Vercel sends an `x-vercel-signature` header with each drain, which is a hash of the payload body created using your Drain signature secret. You can find or update this secret by clicking Edit in the Drains list.

To verify the request is coming from Vercel, you can generate the hash and compare it with the header value as shown below:

Next.js (/app)Next.js (/pages)Other frameworks

server.ts

TypeScript

TypeScriptJavaScript

```
import crypto from 'crypto';
 
export async function POST(request: Request) {
  // Store the signature secret in environment variables
  const signatureSecret = '<Drain signature secret>';
 
  const rawBody = await request.text();
  const rawBodyBuffer = Buffer.from(rawBody, 'utf-8');
  const bodySignature = sha1(rawBodyBuffer, signatureSecret);
 
  if (bodySignature !== request.headers.get('x-vercel-signature')) {
    return Response.json(
      {
        code: 'invalid_signature',
        error: "signature didn't match",
      },
      { status: 403 },
    );
  }
 
  console.log(rawBody);
 
  return Response.json({ success: true });
}
 
function sha1(data: Buffer, secret: string): string {
  return crypto.createHmac('sha1', secret).update(data).digest('hex');
}
```

For additional authentication or identification purposes, you can also add custom headers when [configuring the Drain destination](/docs/drains/using-drains#custom-headers-optional)

## [IP Address Visibility](#ip-address-visibility)

Managing IP address visibility is available on [Enterprise](/docs/plans/enterprise) and [Pro](/docs/plans/pro) plans

Those with the [owner, admin](/docs/rbac/access-roles#owner, admin-role) role can access this feature

Drains can include public IP addresses in the data, which may be considered personal information under certain data protection laws. To hide IP addresses in your drains:

1.  Go to the Vercel [dashboard](/dashboard) and ensure your team is selected in the scope selector
2.  Go to the Settings tab and navigate to Security & Privacy
3.  Under IP Address Visibility, toggle the switch off so the text reads IP addresses are hidden in your Drains

This setting is applied team-wide across all projects and drains.

## [More resources](#more-resources)

For more information on Drains security and how to use them, check out the following resources:

*   [Drains overview](/docs/drains)
*   [Configure Drains](/docs/drains/using-drains)
*   [Log Drains reference](/docs/drains/reference/logs)

--------------------------------------------------------------------------------
title: "Using Drains"
description: "Learn how to configure drains to forward observability data to custom HTTP endpoints and add integrations."
last_updated: "null"
source: "https://vercel.com/docs/drains/using-drains"
--------------------------------------------------------------------------------

# Using Drains

Copy page

Ask AI about this page

Last updated October 31, 2025

Drains are available on [Enterprise](/docs/plans/enterprise) and [Pro](/docs/plans/pro) plans

You can add drains to your project by following the configuration steps below. When you configure the destination, choose between sending data to a [custom HTTP endpoint](#custom-endpoint) and using a [native integration](#native-integrations) or an [external integration](#external-integrations) to send your data to popular services.

## [Configuring Drains](#configuring-drains)

Teams on [Pro](/docs/plans/pro) and [Enterprise](/docs/plans/enterprise) plans can configure drains to forward observability data. You can send logs, traces, speed insights, and analytics data to a custom HTTP endpoint or use integrations from the [Vercel Marketplace](/marketplace) to send logs and traces data to popular services.

1.  ### [Add a drain](#add-a-drain)
    
    From the Vercel dashboard, go to Team Settings > Drains and click Add Drain.
    
2.  ### [Choose data type](#choose-data-type)
    
    Select the type of observability data you want to drain:
    
    *   Logs: Runtime, build and static logs from your deployments
    *   Traces: Distributed tracing data using OpenTelemetry Protocol
    *   Speed Insights: Performance metrics and web vitals
    *   Web Analytics: Page views and custom events
    
    At any time, you can also add an [external integration](#external-integrations) to available [connectable account](/docs/integrations#connectable-accounts) log drain integrations by clicking the External Integrations link on the top right of the Add Drain side bar.
    
3.  ### [Configure the drain](#configure-the-drain)
    
    Provide a name for your drain and select which projects should send data to your endpoint. You can choose all projects or select specific ones.
    
    Configure the sampling rate to control the volume of data sent to your drain. This can help manage costs when you have high traffic volumes.
    
    #### [Additional configuration for logs](#additional-configuration-for-logs)
    
    If you selected logs as your data type, you can also configure:
    
    Sources - Select which log sources to collect:
    
    *   Functions: Outputs log data from Vercel Functions like API Routes
    *   Edge Functions: Outputs log data from Vercel Functions or Routing Middleware using Edge runtime
    *   Static Files: Collects logs for static assets like HTML and CSS files
    *   Rewrites: Collects log results for external [rewrites](/docs/project-configuration#rewrites) to a different domain
    *   Builds: Outputs log data from the Build Step
    *   Firewall: Outputs log data from requests denied by [Vercel Firewall](/docs/vercel-firewall) rules
    *   Redirects: Collects log data from [redirect](/docs/project-configuration#redirects) events
    
    Environments - Select which environments to drain from:
    
    *   [Production](/docs/deployments/environments#production-environment): Logs from production deployments with assigned domain(s)
    *   [Preview](/docs/deployments/environments#preview-environment-pre-production): Logs from deployments accessed through the [generated deployment URL](/docs/deployments/generated-urls)
4.  ### [Configure destination](#configure-destination)
    
    Choose how you want to receive your drain data by selecting either the [Custom Endpoint](#custom-endpoint) or [Native Integrations](#native-integrations) tab.
    
    #### [Custom endpoint](#custom-endpoint)
    
    Configure a custom HTTP endpoint to receive drain data for any data type.
    
    Endpoint URL
    
    This is the URL of the endpoint we will send your data to. The request will be sent over HTTPS using the POST method. Make sure your endpoint responds with a 200 OK status code.
    
    Format
    
    Choose the delivery format based on your data type:
    
    *   Logs: JSON or NDJSON (see [Logs reference](/docs/drains/reference/logs))
    *   Traces: JSON or Protobuf (see [Traces reference](/docs/drains/reference/traces))
    *   Speed Insights: JSON or NDJSON (see [Speed Insights reference](/docs/drains/reference/speed-insights))
    *   Web Analytics: JSON or NDJSON (see [Analytics reference](/docs/drains/reference/analytics))
    
    Signature Verification Secret (Optional)
    
    You can secure your endpoint by comparing the `x-vercel-signature` header with this secret. See [Securing your Drains](/docs/drains/security#secure-drains) for implementation details.
    
    A secret will be automatically generated for you, and you can change it and provide your own secret at any time.
    
    Custom Headers (Optional)
    
    Add custom headers for authentication, identification, or routing purposes. Common use cases include:
    
    *   Authentication: Bearer tokens, API keys, or custom auth headers
    *   Routing: Headers to route requests to specific services or regions
    *   Identification: Custom headers to identify the source or type of data
    *   Content negotiation: Headers to specify preferred response formats
    
    Format headers as `Header-Name: Header-Value` with one header per line.
    
    #### [Native integrations](#native-integrations)
    
    Native integrations are available for log and traces data. You have 2 options:
    
    1.  Installed Products
        
        If you've already installed a marketplace integration product that supports drains, you can select it here. The integration will handle endpoint configuration automatically.
        
    2.  Available Products
        
        Browse and install available product integrations for this drain type:
        
        *   Click Install on any available product. This opens the Marketplace integration creation page in a new window.
        *   Update the default product name if needed and select a subscription plan
        *   Click Create and click Done once the integration has been created
        *   Go back to the Project's settings Drains page and select your newly created integration
    
    You can also add a Drain from your team's Integrations tab
    
    *   Select the installed integration from the list. (Trace data shows under "Observability" and log data shows under "Logging")
    *   Click Manage and select your installed product
    *   Under Drains, click Add Drain
    *   Configure which project you would like to send data from and click Create Drain
5.  ### [Create the drain](#create-the-drain)
    
    Once you have configured all settings, click Create Drain. If you configured a custom endpoint, it will be tested automatically when you create the drain. Vercel will immediately start forwarding data based on your configuration.
    
    You can test your endpoint anytime by clicking the Test button to ensure it receives the data correctly.
    

## [Logs and traces correlation](#logs-and-traces-correlation)

Vercel automatically correlates logs with distributed traces when using [OpenTelemetry](/docs/otel). Any logs generated during traced requests are enriched with correlation identifiers:

*   `traceId` - The trace identifier
*   `spanId` - The span identifier

This correlation happens automatically without code changes. For example, this log:

```
console.log('User logged in', { userId: 123 });
```

Will be automatically enriched with [trace and span identifiers](/docs/drains/reference/logs#json-format-fields).

Limitations: Only applies to user code logs during traced requests, not build-time logs.

## [Drain integrations](#drain-integrations)

You can create Drains with native integrations for the following data types by using [native integrations](#native-integrations) during the configuration step:

*   Log drains: [Logging services](https://vercel.com/marketplace/category/logging) like [Dash0](https://vercel.com/marketplace/dash0)
*   Trace drains: [Observability services](https://vercel.com/marketplace/category/observability) like [Braintrust](https://vercel.com/marketplace/braintrust) for OpenTelemetry trace streaming

### [External integrations](#external-integrations)

1.  From the Vercel dashboard, go to Team Settings > Drains and click Add Drain.
2.  Click the External Integrations link on the top right of the Add Drain side modal.
3.  From the External Integration Log Drains modal, select the installed or available external integration you would like to use and follow the steps to create the drain to that service.

Learn more about [native integrations](/docs/integrations#native-integrations) and [external (connectable accounts) integrations](/docs/integrations#connectable-accounts).

## [Errored Drains](#errored-drains)

Occasionally your drain endpoints can return an error. If more than 80% of drain deliveries fail or the number of failures exceed 50 for the past hour, we will send a notification email and indicate the error status on your Drains page.

![Errored drain will show a warning status.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Flogs%2Fdrain-error-light.png&w=1920&q=75)![Errored drain will show a warning status.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Flogs%2Fdrain-error-dark.png&w=1920&q=75)

Errored drain will show a warning status.

## [Managing your active Drains](#managing-your-active-drains)

1.  From your team's [dashboard](/dashboard), select the Settings tab
2.  Select Drains from the sidebar
3.  In available Drains, click on the menu on the right and click Pause to pause a drain or Resume to resume it
4.  In available Drains, click on the menu on the right and click Delete to delete a drain

## [More resources](#more-resources)

For more information on Drains and how to use them, check out the following resources:

*   [Drains overview](/docs/drains)
*   [Log Drains reference](/docs/drains/reference/logs)
*   [Traces reference](/docs/drains/reference/traces)
*   [Speed Insights reference](/docs/drains/reference/speed-insights)
*   [Analytics reference](/docs/drains/reference/analytics)

--------------------------------------------------------------------------------
title: "Vercel Cache"
description: "Vercel's Cache caches your content at the edge in order to serve data to your users as fast as possible. Learn how Vercel caches works in this guide."
last_updated: "null"
source: "https://vercel.com/docs/edge-cache"
--------------------------------------------------------------------------------

# Vercel Cache

Copy page

Ask AI about this page

Last updated October 10, 2025

Vercel's [CDN Cache](/docs/edge-cache) caches your content at the edge in order to serve data to your users as fast as possible. Vercel's caching is available for all deployments and domains on your account, regardless of the [pricing plan](https://vercel.com/pricing).

Vercel uses the CDN to cache your content globally and serve data to your users as quickly as possible. There are two ways to cache content:

*   [Static file caching](#static-files-caching) is automatic for all deployments, requiring no manual configuration
*   To cache dynamic content, including SSR content, you can use `Cache-Control` [headers](/docs/headers#cache-control-header)

## [How to cache responses](#how-to-cache-responses)

You can cache responses on Vercel with `Cache-Control` headers defined in:

1.  Responses from [Vercel Functions](/docs/functions)
2.  Route definitions in `vercel.json` or `next.config.js`

You can use any combination of the above options, but if you return `Cache-Control` headers in a Vercel Function, it will override the headers defined for the same route in `vercel.json` or `next.config.js`.

### [Using Vercel Functions](#using-vercel-functions)

To cache the response of Functions on Vercel's CDN, you must include [`Cache-Control`](/docs/headers#cache-control-header) headers with any of the following directives:

*   `s-maxage=N`
*   `s-maxage=N, stale-while-revalidate=Z`

`proxy-revalidate` and `stale-if-error` are not currently supported.

The following example demonstrates a [function](/docs/functions) that caches its response and revalidates it every 1 second:

Next.js (/app)Next.js (/pages)Other frameworks

app/api/cache-control-example/route.ts

TypeScript

TypeScriptJavaScript

```
export async function GET() {
  return new Response('Cache Control example', {
    status: 200,
    headers: {
      'Cache-Control': 'public, s-maxage=1',
      'CDN-Cache-Control': 'public, s-maxage=60',
      'Vercel-CDN-Cache-Control': 'public, s-maxage=3600',
    },
  });
}
```

For direct control over caching on Vercel and downstream CDNs, you can use [CDN-Cache-Control](#cdn-cache-control) headers.

### [Using `vercel.json` and `next.config.js`](#using-vercel.json-and-next.config.js)

You can define route headers in `vercel.json` or `next.config.js` files. These headers will be overridden by [headers defined in Function responses](#using-vercel-functions).

The following example demonstrates a `vercel.json` file that adds `Cache-Control` headers to a route:

vercel.json

```
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "headers": [
    {
      "source": "/about.js",
      "headers": [
        {
          "key": "Cache-Control",
          "value": "s-maxage=1, stale-while-revalidate=59"
        }
      ]
    }
  ]
}
```

If you're building your app with Next.js, you should use `next.config.js` rather than `vercel.json`. The following example demonstrates a `next.config.js` file that adds `Cache-Control` headers to a route:

next.config.js

```
/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  async headers() {
    return [
      {
        source: '/about',
        headers: [
          {
            key: 'Cache-Control',
            value: 's-maxage=1, stale-while-revalidate=59',
          },
        ],
      },
    ];
  },
};
 
module.exports = nextConfig;
```

See [the Next docs](https://nextjs.org/docs/app/api-reference/next-config-js) to learn more about `next.config.js`.

### [Static Files Caching](#static-files-caching)

Static files are automatically cached at the edge on Vercel's CDN for the lifetime of the deployment after the first request.

*   If a static file is unchanged, the cached value can persist across deployments due to the hash used in the filename
*   Optimized images cached will persist across deployments for both [static images](/docs/image-optimization#local-images-cache-key) and [remote images](/docs/image-optimization#remote-images-cache-key)

#### [Browser](#browser)

*   `max-age=N, public`
*   `max-age=N, immutable`

Where `N` is the number of seconds the response should be cached. The response must also meet the [caching criteria](/docs/edge-cache#how-to-cache-responses).

## [Cache control options](#cache-control-options)

You can cache dynamic content through [Vercel Functions](/docs/functions), including SSR, by adding `Cache-Control` [headers](/docs/headers#cache-control-header) to your response. When you specify `Cache-Control` headers in a function, responses will be cached in the region the function was requested from.

See [our docs on Cache-Control headers](/docs/headers#cache-control-header) to learn how to best use `Cache-Control` directives on Vercel's CDN.

### [CDN-Cache-Control](#cdn-cache-control)

Vercel supports two [Targeted Cache-Control headers](https://httpwg.org/specs/rfc9213.html):

*   `CDN-Cache-Control`, which allows you to control the Vercel Cache or other CDN cache _separately_ from the browser's cache. The browser will not be affected by this header
*   `Vercel-CDN-Cache-Control`, which allows you to specifically control Vercel's Cache. Neither other CDNs nor the browser will be affected by this header

By default, the headers returned to the browser are as follows:

*   `Cache-Control`
*   `CDN-Cache-Control`

`Vercel-CDN-Cache-Control` headers are not returned to the browser or forwarded to other CDNs.

To learn how these headers work in detail, see [our dedicated headers docs](/docs/headers/cache-control-headers#cdn-cache-control-header).

The following example demonstrates `Cache-Control` headers that instruct:

*   Vercel's Cache to have a [TTL](https://en.wikipedia.org/wiki/Time_to_live) of `3600` seconds
*   Downstream CDNs to have a TTL of `60` seconds
*   Clients to have a TTL of `10` seconds

Next.js (/app)Next.js (/pages)Other frameworks

app/api/cache-control-headers/route.ts

TypeScript

TypeScriptJavaScript

```
export async function GET() {
  return new Response('Cache Control example', {
    status: 200,
    headers: {
      'Cache-Control': 'max-age=10',
      'CDN-Cache-Control': 'max-age=60',
      'Vercel-CDN-Cache-Control': 'max-age=3600',
    },
  });
}
```

If you set `Cache-Control` without a `CDN-Cache-Control`, the Vercel CDN strips `s-maxage` and `stale-while-revalidate` from the response before sending it to the browser. To determine if the response was served from the cache, check the [`x-vercel-cache`](#x-vercel-cache) header in the response.

### [Vary header](#vary-header)

The `Vary` response header instructs caches to use specific request headers as part of the cache key. This allows you to serve different cached responses to different users based on their request headers.

The `Vary` header only has an effect when used in combination with `Cache-Control` headers that enable caching (such as `s-maxage`). Without a caching directive, the `Vary` header has no behavior.

When Vercel's CDN receives a request, it combines the cache key (described in the [Cache Invalidation](#cache-invalidation) section) with the values of any request headers specified in the `Vary` header to create a unique cache entry for each distinct combination.

#### [Use cases](#use-cases)

Vercel's CDN already includes the `Accept` and `Accept-Encoding` headers as part of the cache key by default. You do not need to explicitly include these headers in your `Vary` header.

The most common use case for the `Vary` header is content negotiation, serving different content based on:

*   User location (e.g., `X-Vercel-IP-Country`)
*   Device type (e.g., `User-Agent`)
*   Language preferences (e.g., `Accept-Language`)

Example: Country-specific content

You can use the `Vary` header with Vercel's `X-Vercel-IP-Country` request header to cache different responses for users from different countries:

Next.js (/app)Next.js (/pages)Other frameworks

app/api/country-specific/route.ts

TypeScript

TypeScriptJavaScript

```
import { type NextRequest } from 'next/server';
 
export async function GET(request: NextRequest) {
  const country = request.headers.get('x-vercel-ip-country') || 'unknown';
 
  // Serve different content based on country
  let content;
  if (country === 'US') {
    content = { message: 'Hello from the United States!' };
  } else if (country === 'GB') {
    content = { message: 'Hello from the United Kingdom!' };
  } else {
    content = { message: `Hello from ${country}!` };
  }
 
  return Response.json(content, {
    status: 200,
    headers: {
      'Cache-Control': 's-maxage=3600',
      Vary: 'X-Vercel-IP-Country',
    },
  });
}
```

#### [Setting the `Vary` header](#setting-the-vary-header)

You can set the `Vary` header in the same ways you set other response headers:

In Vercel Functions

Next.js (/app)Next.js (/pages)Other frameworks

app/api/data/route.ts

TypeScript

TypeScriptJavaScript

```
import { type NextRequest } from 'next/server';
 
export async function GET(request: NextRequest) {
  return Response.json(
    { data: 'This response varies by country' },
    {
      status: 200,
      headers: {
        Vary: 'X-Vercel-IP-Country',
        'Cache-Control': 's-maxage=3600',
      },
    },
  );
}
```

Using `vercel.json`

vercel.json

```
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "headers": [
    {
      "source": "/api/data",
      "headers": [
        {
          "key": "Vary",
          "value": "X-Vercel-IP-Country"
        },
        {
          "key": "Cache-Control",
          "value": "s-maxage=3600"
        }
      ]
    }
  ]
}
```

Using `next.config.js`

If you're building your app with Next.js, use `next.config.js`:

next.config.js

```
/** @type {import('next').NextConfig} */
const nextConfig = {
  async headers() {
    return [
      {
        source: '/api/data',
        headers: [
          {
            key: 'Vary',
            value: 'X-Vercel-IP-Country',
          },
          {
            key: 'Cache-Control',
            value: 's-maxage=3600',
          },
        ],
      },
    ];
  },
};
 
module.exports = nextConfig;
```

#### [Multiple `Vary` headers](#multiple-vary-headers)

You can specify multiple headers in a single `Vary` value by separating them with commas:

```
res.setHeader('Vary', 'X-Vercel-IP-Country, Accept-Language');
```

This will create separate cache entries for each unique combination of country and language preference.

#### [Best practices](#best-practices)

*   Use `Vary` headers selectively, as each additional header exponentially increases the number of cache entries — this doesn't directly impact your bill, but can result in more cache misses than desired
*   Only include headers that meaningfully impact content generation
*   Consider combining multiple variations into a single header value when possible

## [Cacheable response criteria](#cacheable-response-criteria)

The `Cache-Control` field is an HTTP header specifying caching rules for client (browser) requests and server responses. A cache must obey the requirements defined in the `Cache-Control` header.

For server responses to be successfully cached with Vercel's CDN, the following criteria must be met:

*   Request uses `GET` or `HEAD` method.
*   Request does not contain `Range` header.
*   Request does not contain `Authorization` header.
*   Response uses `200`, `404`, `301`, `302`, `307` or `308` status code.
*   Response does not exceed `10MB` in content length.
*   Response does not contain the `set-cookie` header.
*   Response does not contain the `private`, `no-cache` or `no-store` directives in the `Cache-Control` header.
*   Response does not contain `Vary: *` header, which is treated as equivalent to `Cache-Control: private`.

Vercel does not allow bypassing the cache for static files by design.

## [Cache invalidation](#cache-invalidation)

To learn about cache keys, manually purging the cache, and the differences between invalidate and delete methods, see [Purging Vercel Cache](/docs/edge-cache/purge).

## [`x-vercel-cache`](#x-vercel-cache)

The `x-vercel-cache` header is included in HTTP responses to the client, and describes the state of the cache.

See [our headers docs](/docs/headers/response-headers#x-vercel-cache) to learn more.

## [Limits](#limits)

Vercel's Edge Cache is segmented [by region](/docs/regions). The following caching limits apply to [Vercel Function](/docs/functions) responses:

*   Max cacheable response size:
    *   Streaming functions: 20MB
    *   Non-streaming functions: 10MB
*   Max cache time: 1 year
    *   `s-maxage`
    *   `max-age`
    *   `stale-while-revalidate`

While you can put the maximum time for server-side caching, cache times are best-effort and not guaranteed. If an asset is requested often, it is more likely to live the entire duration. If your asset is rarely requested (e.g. once a day), it may be evicted from the regional cache.

### [`proxy-revalidate` and `stale-if-error`](#proxy-revalidate-and-stale-if-error)

Vercel does not currently support using `proxy-revalidate` and `stale-if-error` for server-side caching.

--------------------------------------------------------------------------------
title: "Purging Vercel Cache"
description: "Learn how to invalidate and purge cached content on Vercel's CDN, including cache keys and manual purging options."
last_updated: "null"
source: "https://vercel.com/docs/edge-cache/purge"
--------------------------------------------------------------------------------

# Purging Vercel Cache

Copy page

Ask AI about this page

Last updated October 16, 2025

Cache purging is available on [all plans](/docs/plans)

Those with the [owner](/docs/rbac/access-roles#owner-role) and [member](/docs/rbac/access-roles#member-role) roles can access this feature

Learn how to invalidate and purge cached content on Vercel's CDN, including cache keys and manual purging options.

## [Cache keys](#cache-keys)

Each request to Vercel's CDN has a cache key derived from the following:

*   The request method (such as `GET`, `POST`, etc)
*   The request URL (query strings are ignored for static files)
*   The host domain
*   The unique [deployment URL](/docs/deployments/generated-urls)
*   The scheme (whether it's `https` or `http`)

Since each deployment has a different cache key, you can [promote a new deployment](/docs/deployments/promoting-a-deployment) to production without affecting the cache of the previous deployment.

The cache key for Image Optimization behaves differently for [static images](/docs/image-optimization#local-images-cache-key) and [remote images](/docs/image-optimization#remote-images-cache-key).

## [Understanding cache purging](#understanding-cache-purging)

### [Invalidating the cache](#invalidating-the-cache)

When you invalidate a cache tag, all cached content associated with that tag is marked as stale. The next request serves the stale content instantly while revalidation happens in the background. This approach has no latency impact for users while ensuring content gets updated.

### [Deleting the cache](#deleting-the-cache)

When you delete a cache tag, the cached entries are marked for deletion. The next request fetches content from your origin before responding to the user. This can slow down the first request after deletion. If many users request the same deleted content simultaneously, it can create a cache stampede where multiple requests hit your origin at once.

### [Cache tags](#cache-tags)

Cache tags are case-sensitive. The tags `product` and `Product` are treated as different tags.

#### [Cache tag scope](#cache-tag-scope)

Cache tags are scoped to your project. When you purge a tag, you can target production deployments, preview deployments, or both. By default, purging affects all cached responses across all deployments in that project that use that tag.

## [Manually purging Vercel Cache](#manually-purging-vercel-cache)

In some circumstances, you may need to delete all cached data and force revalidation. For example, you might have set a `Cache-Control` to cache the response for a month but the content changes more frequently than once a month. You can do this by purging the cache:

1.  Under your project, go to the Settings tab.
2.  In the left sidebar, select Caches.
3.  In the CDN Cache section, click Purge CDN Cache.
4.  In the dialog, you'll see two options:
    *   Invalidate: Marks a cache tag as stale, causing cache entries associated with that tag to be revalidated in the background on the next request. This is the recommended method for most use cases.
    *   Delete: Marks a cache tag as deleted, causing cache entries associated with that tag to be revalidated in the foreground on the next request. Use this method with caution because one tag can be associated with many paths and deleting the cache can cause many concurrent requests to the origin leading to [cache stampede problem](https://en.wikipedia.org/wiki/Cache_stampede). A good use case for deleting the cache is when the origin has also been deleted, for example it returns a `404` or `410` status code.
5.  In the dialog, enter one or more cache tags, separated by commas. You can use `*` to purge all cache tags.
6.  Finally, click the Purge button in the dialog to confirm.

The purge event itself is not billed but it can temporarily increase Function Duration, Functions Invocations, Edge Function Executions, Fast Origin Transfer, Image Optimization Transformations, Image Optimization Cache Writes, and ISR Writes.

Purge is not the same as creating a new deployment because it will also purge Image Optimization content, which is usually preserved between deployments, as well as ISR content, which is often generated at build time for new deployments.

## [Limits](#limits)

|  | Hobby | Pro | Enterprise |
| --- | --- | --- | --- |
| Rest API calls per minute | 5 | 5 | 5 |
| Tags per Rest API call | 16 | 16 | 16 |
| Tag character limit | 256 | 256 | 256 |
| Tags per cached response | 128 | 128 | 128 |

--------------------------------------------------------------------------------
title: "Vercel Edge Config"
description: "An Edge Config is a global data store that enables experimentation with feature flags, A/B testing, critical redirects, and more."
last_updated: "null"
source: "https://vercel.com/docs/edge-config"
--------------------------------------------------------------------------------

# Vercel Edge Config

Copy page

Ask AI about this page

Last updated September 24, 2025

Edge Config is available on [all plans](/docs/plans)

An [Edge Config](/edge-config) is a global data store that [enables experimentation with feature flags, A/B testing, critical redirects, and IP blocking](#use-cases). It enables you to read data at the edge without querying an external database or hitting upstream servers.

With Vercel's optimizations, you can read Edge Config data at negligible latency. The vast majority of your reads will complete within 15ms [at P99](/docs/speed-insights/metrics#how-the-percentages-are-calculated), or often less than 1ms.

You can use an Edge Config in [Middleware](/docs/routing-middleware) and [Vercel Functions](/docs/functions).

Vercel's Edge Config read optimizations are only available on the Edge and Node.js runtimes. Optimizations can be enabled for other runtimes, [such as Ruby, Go, and Python](/docs/functions/runtimes) upon request. See [our Edge Config limits docs](/docs/edge-config/edge-config-limits) to learn more.

## [Use cases](#use-cases)

Edge Configs are great for data that is accessed frequently and updated infrequently. Here are some examples of storage data suitable for Edge Config:

**Feature flags and A/B testing**: Experiment with A/B testing by storing feature flags in your Edge Config. Fetching such data from Edge Config rather than a database can cut page loads by hundreds of milliseconds. [Deploy the template](https://vercel.com/templates/next.js/feature-flag-apple-store)

**Critical redirects**: When you need to redirect a URL urgently, Edge Configs offer a fast solution that doesn't require you to redeploy your website. With Middleware, you can read from your Edge Config to redirect users visiting incorrect URLs. For an example, see the [Maintenance Page template](https://vercel.com/templates/next.js/maintenance-page).

Alternatively, use the Vercel WAF to configure a [Redirect action](/docs/security/vercel-waf/rule-configuration#actions) based on specific conditions. For more details, check the [emergency redirect](/docs/security/vercel-waf/examples#emergency-redirect) example.

**Malicious IP and User Agent blocking**: Store a set of malicious IPs in your Edge Config, then block them upon detection without invoking upstream servers

## [Getting started](#getting-started)

You can create and manage your Edge Config from either [Vercel REST API](/docs/edge-config/vercel-api) or [Dashboard](/docs/edge-config/edge-config-dashboard). You can scope your Edge Configs to your Hobby team or [team](/docs/accounts/create-a-team), and connect them to as many projects as you want.

To get started, see [our quickstart](/docs/edge-config/get-started).

## [Using Edge Config in your workflow](#using-edge-config-in-your-workflow)

If you'd like to know whether or not Edge Config can be integrated into your workflow, it's worth knowing the following:

*   You can have one or more Edge Configs per Vercel account, depending on your plan as explained in [Limits](/docs/edge-config/edge-config-limits)
*   You can use multiple Edge Configs in one Vercel project
*   Each Edge Config can be accessed by multiple Vercel projects
*   Edge Configs can be scoped to different environments within projects using environment variables
*   Edge Config access is secure by default. A [read access token](/docs/edge-config/using-edge-config#creating-a-read-access-token) is required to read from them, and an [API token](/docs/rest-api#creating-an-access-token) is required to write to them

See [our Edge Config limits docs to learn more](/docs/edge-config/edge-config-limits)

## [Why use Edge Config instead of alternatives?](#why-use-edge-config-instead-of-alternatives)

There are alternative solutions to Edge Config for handling A/B testing, feature flags, and IP blocking. The following table lays out how those solutions compare to Edge Config:

| Edge Config vs alternatives | Read latency | Write latency | Redeployment required | Added risk of downtime |
| --- | --- | --- | --- | --- |
| Edge Config | Ultra-low | Varies | No | No |
| Remote JSON files | Varies | Varies | No | Yes |
| Embedded JSON files | Lowest | Highest | Yes | No |
| Environment Variables | Lowest | Highest | Yes | No |

## [Limits](#limits)

To learn about Edge Config limits and pricing, see [our Edge Config limits docs](/docs/edge-config/edge-config-limits).

## [More resources](#more-resources)

*   [Quickstart](/docs/edge-config/get-started)
*   [Read with the SDK](/docs/edge-config/edge-config-sdk)
*   [Use the Dashboard](/docs/edge-config/edge-config-dashboard)
*   [Manage with the API](/docs/edge-config/vercel-api)
*   [Edge Config Limits](/docs/edge-config/edge-config-limits)

--------------------------------------------------------------------------------
title: "Managing Edge Configs with the Dashboard"
description: "Learn how to create, view and update your Edge Configs and the data inside them in your Vercel Dashboard at the Hobby team, team, and project levels."
last_updated: "null"
source: "https://vercel.com/docs/edge-config/edge-config-dashboard"
--------------------------------------------------------------------------------

# Managing Edge Configs with the Dashboard

Copy page

Ask AI about this page

Last updated September 24, 2025

You can create, view and update your [Edge Configs](/edge-config), and the data inside them, in your Vercel Dashboard at both the [account level](/docs/accounts) and the [project level](/docs/projects/overview).

## [Creating an Edge Config](#creating-an-edge-config)

### [At the account level](#at-the-account-level)

To add an Edge Config at the Hobby team or team level, follow these steps:

1.  Make sure that you are in the [right Hobby team or team](/docs/dashboard-features)
    
2.  Click on the Storage tab
    
3.  Click the Create Store button
    
4.  Type a name for your Edge Config in the dialog and click Create. The name shouldn't exceed 32 characters and can only contain alphanumeric letters, "\_", and "-".
    
5.  On creation, you are taken to the `my_edge_config_id` config page. By default, a key-value pair of `"greeting": "hello world"` is created. On the detail page of the newly created Edge Config you can:
    
    *   View and manage stored items
    *   Connect projects to and disconnect projects from this Edge Config
    *   Generate, copy, and delete tokens associated with this Edge Config

Your Edge Config is now ready to be used. You can also [create an Edge Config at the project level](/docs/edge-config/edge-config-dashboard#at-the-project-level).

If you're creating a project at the account-level, we won't automatically create a token, connection string, and environment variable until a project has been connected.

### [At the project level](#at-the-project-level)

1.  Navigate to your [project](/docs/projects/overview) page and click on the Edge Config tab
    
2.  Click Create Project Store and type a name slug for your Edge Config in the dialog that opens. The name shouldn't exceed 32 characters and can only contain alphanumeric letters, "\_", and "-".
    
3.  Click Create.
    
4.  Once created, you can click on the Edge Config to [manage it](#managing-edge-configs). The following items are automatically created:
    
    *   An environment variable `EDGE_CONFIG` that holds a [connection string](/docs/edge-config/using-edge-config#using-a-connection-string). If you go to your projects's Settings > Environment Variables, you'll see the newly created environment variable.
    *   A [read access token](/docs/edge-config/using-edge-config#creating-a-read-access-token). This token, along with your EDGE CONFIG ID is used to create a [connection string](/docs/edge-config/using-edge-config#using-a-connection-string). This connection string is saved as the value of your `EDGE_CONFIG` environment variable. Using this enables you to use the SDK in your project to read the contents of the store.

## [Managing Edge Configs](#managing-edge-configs)

To view a list of all Edge Configs available in your Hobby team or team, go to Storage then select Edge Config from the drop-down after making sure that you are in the [correct Hobby team or team](/docs/dashboard-features).

![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fstorage%2Fedge-config%2Fedge-config-view-all-configs-light.png&w=3840&q=75)![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fstorage%2Fedge-config%2Fedge-config-view-all-configs-dark.png&w=3840&q=75)

List of Edge Configs in a team account

In the Used by column, you can see in which project(s) the Edge Config is used. The right column shows the size of the data contained in the config. To manage the Edge Config, its store and tokens, click on the Edge Config's row to open the detail page.

![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fstorage%2Fedge-config%2Fedge-config-usage-light.png&w=3840&q=75)![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fstorage%2Fedge-config%2Fedge-config-usage-dark.png&w=3840&q=75)

Edge Config detail page

To rename the Edge Config, select the Settings item in the sidebar, update the Edge Config Name, and select Save.

To delete the Edge Config, select the Settings item in the sidebar, then select Delete Edge Config.

## [Managing items in the store](#managing-items-in-the-store)

The default view of the Edge Config's detail page shows the list of all items in the store. You will see an open accordion titled Learn how to use this in code if the Edge Config is connected to at least one project. This accordion provides the steps with a code example on how to read your store items.

To add, edit or delete any item in your store, edit the `json` object in the right panel and click Save Items.

### [Restoring Edge Config backups](#restoring-edge-config-backups)

Backups of your Edge Config are automatically created when you make changes, and are stored for a [length of time](/docs/edge-config/edge-config-limits#backup-retention) determined by your plan. To restore one:

1.  From your dashboard, select the Storage tab and then select your Edge Config
2.  From the left section, select the Backups tab
3.  From the list, select the backup that you would like to view. You'll be taken to the Items tab to view a comparison of the backup version and current version
4.  To restore the backup, select the Restore button and confirm the action

To learn more about backups, see [Edge Config backups](/docs/edge-config/using-edge-config#edge-config-backups).

When protected by a JSON schema, the backup must pass schema validation to be restored.

## [Schema validation](#schema-validation)

You can protect your Edge Config by adding a JSON schema to it. Vercel uses this schema to validate the data that is added to the store and prevent updates that fail validation. To add a schema:

1.  From your dashboard, select the Storage tab and then select your Edge Config
2.  Toggle the Schema button to open the schema editing tab
3.  Enter your [JSON schema](https://json-schema.org/) into the editor. Vercel will use the schema to validate your data in real-time
4.  Click Save. This will save changes to both the schema and data

The following snippet is an example of a schema that allows you to set boolean flags and a list of redirects.

schema.json

```
{
  "$schema": "http://json-schema.org/draft-07/schema",
  "type": "object",
  "additionalProperties": false,
  "required": ["flags", "redirects"],
  "properties": {
    "flags": {
      "type": "object",
      "patternProperties": {
        "^.*$": {
          "type": "boolean"
        }
      }
    },
    "redirects": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "from": { "type": "string" },
          "to": { "type": "string" }
        }
      }
    }
  }
}
```

## [Managing connected projects](#managing-connected-projects)

![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fstorage%2Fedge-config%2Fedge-config-projects-light.png&w=1920&q=75)![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fstorage%2Fedge-config%2Fedge-config-projects-dark.png&w=1920&q=75)

List of connected projects

Click on Projects in the left panel of the Edge Config detail page to open a view that shows the projects connected with this Edge Config.

To delete a connection, click on the vertical ellipsis icon on the right hand side of the row and click Delete environment variable and confirm by clicking Delete connection in the dialog.

Deleting a connection does not delete the underlying token used by that Connection String. To learn how to delete tokens, review [Managing read access tokens](#managing-read-access-tokens).

To connect the Edge Config with another project, click Connect Project, find the project from the drop-down in the dialog and click Connect. If you receive a warning that this project already has an `EDGE_CONFIG` environment variable, open the Advanced Options and change the environment variable name in the corresponding field to a name other than `EDGE_CONFIG`. The Connect button will be enabled once the new enviroment variable does not already exist in the project.

## [Managing read access tokens](#managing-read-access-tokens)

![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fstorage%2Fedge-config%2Fedge-config-tokens-light.png&w=3840&q=75)![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fstorage%2Fedge-config%2Fedge-config-tokens-dark.png&w=3840&q=75)

List of tokens

To delete a token, click on the vertical ellipsis icon on the right hand side of the token's row and click Delete Token and confirm by clicking Delete Token in the dialog.

You can copy the connection string to be used in your code by clicking on Copy Connection String from the same pop up from the vertical ellipsis icon.

You can generate a new token by clicking the Generate Token button, typing a name slug in the dialog that opens and clicking Create.

## [Up Next](#up-next)

[

#### Managing with the Vercel REST API

Using the Vercel REST API, you can create and update Edge Configs

](/docs/edge-config/vercel-api)

--------------------------------------------------------------------------------
title: "Using Edge Config with an integration"
description: "Learn how to use Edge Config with popular A/B testing and feature flag service integrations."
last_updated: "null"
source: "https://vercel.com/docs/edge-config/edge-config-integrations"
--------------------------------------------------------------------------------

# Using Edge Config with an integration

Copy page

Ask AI about this page

Last updated May 23, 2025

Edge Config integrations are available on [all plans](/docs/plans)

Vercel has partnered with A/B testing and feature flag services such as LaunchDarkly and Statsig to make it easier to integrate Edge Config into your workflow. These integrations sync feature flag definitions into Edge Config, allowing you to evaluate flags at the edge without making network calls to your preferred service provider.

To see these integrations in action, explore a template:

You can get started with any of these Edge Config integrations by following the quickstart:

*   [LaunchDarkly](/docs/edge-config/integrations/launchdarkly-edge-config)
*   [Statsig](/docs/edge-config/integrations/statsig-edge-config)
*   [Hypertune](/docs/edge-config/integrations/hypertune-edge-config)
*   [Split](/docs/edge-config/integrations/split-edge-config)
*   [DevCycle](/docs/edge-config/integrations/devcycle-edge-config)

## [More resources](#more-resources)

*   [Quickstart](/docs/edge-config/get-started)
*   [Read with the SDK](/docs/edge-config/edge-config-sdk)
*   [Use the Dashboard](/docs/edge-config/edge-config-dashboard)
*   [Manage with the API](/docs/edge-config/vercel-api)
*   [Edge Config Limits](/docs/edge-config/edge-config-limits)

--------------------------------------------------------------------------------
title: "Using Edge Config with DevCycle"
description: "Learn how to use Edge Config with Vercel's DevCycle integration."
last_updated: "null"
source: "https://vercel.com/docs/edge-config/edge-config-integrations/devcycle-edge-config"
--------------------------------------------------------------------------------

# Using Edge Config with DevCycle

Copy page

Ask AI about this page

Last updated October 9, 2025

This guide will help you get started with using Vercel's DevCycle integration with Edge Config. This integration allows you to use Edge Config as a configuration source for your DevCycle feature flags.

The DevCycle Edge Config integration is available in [Beta](/docs/release-phases#beta) on [all plans](/docs/plans)

DevCycle is a feature management platform designed for developers. DevCycle allows you to work with feature flags more naturally, where you write code, so you can deliver better features, faster.

With DevCycle and Vercel Edge Config the decision logic for your features lives with your hosted site, so you can run your feature rollouts or experiments with ultra-low latency.

## [Prerequisites](#prerequisites)

Before using this integration, you should have:

1.  The latest version of Vercel CLI. To check your version, use `vercel --version`. To [install](/docs/cli#installing-vercel-cli) or update Vercel CLI, use:
    
    pnpmyarnnpmbun
    
    ```
    pnpm i -g vercel@latest
    ```
    
2.  A project. If you don't have one, you can run the following terminal commands to create a Next.js project:
    
    pnpmyarnnpmbun
    
    ```
    pnpm i next
    ```
    
    terminal
    
    ```
    npx create-next-app@latest
    ```
    
3.  A Vercel project. If you don't have one, see [Creating a Project](/docs/projects/overview#creating-a-project)
    
4.  An Edge Config. If you don't have one, follow [the Edge Config quickstart](/docs/edge-config/get-started)
    
5.  The Edge Config SDK:
    
    pnpmyarnnpmbun
    
    ```
    pnpm i @vercel/edge-config
    ```
    

1.  ### [Set up the DevCycle integration](#set-up-the-devcycle-integration)
    
    Visit [the DevCycle page in the Integration Marketplace](/integrations/devcycle) and select the Add Integration button. From the modal that opens:
    
    1.  Select your Vercel team and project.
    2.  Continue and log into DevCycle.
    3.  Select the DevCycle Organization and Project you want to use with Vercel Edge Config.
    4.  Connect your DevCycle project to an existing or new Edge Config store.
    5.  Click Finish Setup.
2.  ### [Install the DevCycle Edge Config package](#install-the-devcycle-edge-config-package)
    
    pnpmyarnnpmbun
    
    ```
    pnpm i @devcycle/vercel-edge-config @vercel/edge-config
    ```
    
3.  ### [Use the DevCycle integration in your code](#use-the-devcycle-integration-in-your-code)
    
    For more information on DevCycle Next.js SDK usage, see the [DevCycle docs](https://docs.devcycle.com/sdk/client-side-sdks/nextjs).
    
    Next.js (/app)Next.js (/pages)Node.js
    
    app/index.tsx
    
    TypeScript
    
    TypeScriptJavaScript
    
    ```
    import { createClient } from '@vercel/edge-config';
    import { EdgeConfigSource } from '@devcycle/vercel-edge-config';
    import { setupDevCycle } from '@devcycle/nextjs-sdk/server';
     
    const edgeClient = createClient(process.env.EDGE_CONFIG ?? '');
    const edgeConfigSource = new EdgeConfigSource(edgeClient);
     
    export const { getVariableValue, getClientContext } = setupDevCycle({
      serverSDKKey: process.env.DEVCYCLE_SERVER_SDK_KEY ?? '',
      clientSDKKey: process.env.NEXT_PUBLIC_DEVCYCLE_CLIENT_SDK_KEY ?? '',
      userGetter: () => ({ user_id: 'test_user' }),
      options: {
        // pass the configSource option with the instance of EdgeConfigSource
        configSource: edgeConfigSource,
      },
    });
    ```
    

## [Next steps](#next-steps)

Now that you have the DevCycle Edge Config integration set up, you can explore the following topics to learn more:

*   [Get started with Edge Config](/docs/edge-config/get-started)
*   [Read with the SDK](/docs/edge-config/edge-config-sdk)
*   [Use the dashboard](/docs/edge-config/edge-config-dashboard)
*   [Edge Config limits](/docs/edge-config/edge-config-limits)

--------------------------------------------------------------------------------
title: "Using Edge Config with Hypertune"
description: "Learn how to use Hypertune's integration with Vercel Edge Config."
last_updated: "null"
source: "https://vercel.com/docs/edge-config/edge-config-integrations/hypertune-edge-config"
--------------------------------------------------------------------------------

# Using Edge Config with Hypertune

Copy page

Ask AI about this page

Last updated September 24, 2025

Hypertune is a feature flag, A/B testing and app configuration platform with full type-safety and Git version control.

The Hypertune Edge Config integration synchronizes with your Functions for low latency retrieval without fetch requests.

## [Prerequisites](#prerequisites)

Before using this integration, you should have the latest version of Vercel CLI.

To check your version, use `vercel --version`. To install or update Vercel CLI, use:

pnpmyarnnpmbun

```
pnpm i -g vercel@latest
```

## [Get Started](#get-started)

If you deploy a template like the [Hypertune Flags SDK Example](https://vercel.com/templates/next.js/flags-sdk-hypertune-nextjs), it will guide you through most of these steps.

Navigate to your Project and click the Flags tab.

Install a flag provider, select Hypertune and click continue, then toggle Enable Edge Config Syncing on.

1.  ### [Set up your local environment](#set-up-your-local-environment)
    
    Open your project in your development environment and link it to Vercel.
    
    ```
    vercel link
    ```
    
    Once linked, you can pull the environment variables that were added to your project.
    
    ```
    vercel env pull
    ```
    
    You should have a `.env.local` file with the following environment variables:
    
    ```
    EXPERIMENTATION_CONFIG="..."
    EXPERIMENTATION_CONFIG_ITEM_KEY="..."
    NEXT_PUBLIC_HYPERTUNE_TOKEN="..."
    ```
    
    If you don't see these environment variables, ensure your project is linked to the Hypertune integration in the Flags tab.
    
2.  ### [Manage your flags in Hypertune](#manage-your-flags-in-hypertune)
    
    From the Flags tab, click Open in Hypertune to make changes in your Hypertune project.
    
    When you click save, changes will be synchronized to your Edge Config and ready for use.
    
3.  ### [Generate a type-safe client](#generate-a-type-safe-client)
    
    Run code generation to produce the type-safe client for use with the Hypertune SDK.
    
    ```
    npx hypertune
    ```
    
    You should now have a `generated` directory with generated code reflecting your saved changes.
    
4.  ### [Declare flags in your code](#declare-flags-in-your-code)
    
    You can declare server side flags using the Flags SDK with Hypertune as follows:
    
    flags.ts
    
    TypeScript
    
    TypeScriptJavaScript
    
    ```
    import {
      createSource,
      vercelFlagDefinitions as flagDefinitions,
      flagFallbacks,
      type FlagValues,
      type Context,
    } from '@/generated/hypertune';
    import { flag } from 'flags/next';
    import { createHypertuneAdapter } from '@flags-sdk/hypertune';
    import { identify } from './lib/identify';
     
    // Generate a Flags SDK adapter from generated Hypertune code
    const hypertuneAdapter = createHypertuneAdapter<FlagValues, Context>({
      createSource,
      flagDefinitions,
      flagFallbacks,
      identify,
    });
     
    // Use generated definitions to declare flags in your framework
    export const exampleFlag = flag(hypertuneAdapter.declarations.exampleFlag);
    ```
    
    See the [more resources](#more-resources) section for more information about the Hypertune and Flags SDK.
    
5.  ### [Use flags in your app](#use-flags-in-your-app)
    
    app/page.tsx
    
    TypeScript
    
    TypeScriptJavaScript
    
    ```
    import { exampleFlag } from '@/flags';
     
    export default async function Home() {
      const isExampleFlagEnabled = await exampleFlag();
      return <div>Example Flag is {isExampleFlagEnabled ? 'enabled' : 'disabled'}</div>;
    }
    ```
    

## [Next steps](#next-steps)

Learn more about Edge Config:

*   [Get started with Edge Config](/docs/edge-config/get-started)
*   [Manage Edge Config on the dashboard](/docs/edge-config/edge-config-dashboard)
*   [View the Edge Config SDK reference](/docs/edge-config/edge-config-sdk)
*   [View Edge Config limits](/docs/edge-config/edge-config-limits)

## [More resources](#more-resources)

Learn more about Hypertune and the Flags SDK adapter:

*   [Hypertune App Router Quickstart](https://docs.hypertune.com/getting-started/next.js-app-router-quickstart)
*   [Flags SDK Hypertune Provider](https://flags-sdk.dev/providers/hypertune)

--------------------------------------------------------------------------------
title: "Using Edge Config with LaunchDarkly"
description: "Learn how to use Edge Config with Vercel's LaunchDarkly integration."
last_updated: "null"
source: "https://vercel.com/docs/edge-config/edge-config-integrations/launchdarkly-edge-config"
--------------------------------------------------------------------------------

# Using Edge Config with LaunchDarkly

Copy page

Ask AI about this page

Last updated September 24, 2025

This guide will help you get started with using Vercel's LaunchDarkly integration with Edge Config. This integration allows you to use Edge Config as a configuration source for your LaunchDarkly feature flags.

[LaunchDarkly](https://docs.launchdarkly.com/home) allows you to enable and disable feature flags dynamically, decoupling feature rollouts from deployments. The LaunchDarkly Edge Config integration enables you to evaluate flags at the edge without making network calls to LaunchDarkly.

The LaunchDarkly Edge Config integration is only available to Enterprise LaunchDarkly customers. However, you do not need to have a Vercel [Enterprise](/docs/plans/enterprise) account.

## [Prerequisites](#prerequisites)

Before using this integration, you should have:

1.  The latest version of Vercel CLI. To check your version, use `vercel --version`. To [install](/docs/cli#installing-vercel-cli) or update Vercel CLI, use:
    
    pnpmyarnnpmbun
    
    ```
    pnpm i -g vercel@latest
    ```
    
2.  A project. If you don't have one, you can run the following terminal commands to create a Next project:
    
    pnpmyarnnpmbun
    
    ```
    pnpm i next
    ```
    
    terminal
    
    ```
    npx create-next-app@latest
    ```
    
3.  A Vercel project. If you don't have one, see [Creating a Project](/docs/projects/overview#creating-a-project)
    
4.  An Edge Config. If you don't have one, follow [the Edge Config quickstart](/docs/edge-config/get-started)
    
5.  The Edge Config SDK:
    
    pnpmyarnnpmbun
    
    ```
    pnpm i @vercel/edge-config
    ```
    

1.  ### [Set up the LaunchDarkly integration](#set-up-the-launchdarkly-integration)
    
    Visit [the LaunchDarkly page in the Integration Marketplace](/integrations/launchdarkly) and select the Add Integration button. From the Integration dialog:
    
    1.  Select a Vercel team and project to connect the integration to
    2.  Log into LaunchDarkly
    3.  Select the Authorize button to allow the integration to access your LaunchDarkly account data
    4.  Name the integration, and select an existing Edge Config or create a new one
2.  ### [Get your client-side ID](#get-your-client-side-id)
    
    To use the integration, you'll need your client-side ID from LaunchDarkly. Here's how to add it to your project:
    
    1.  [Go to the settings page of your LaunchDarkly dashboard](https://app.launchdarkly.com/settings/projects).
    2.  Select the LaunchDarkly project your integration is connected to
    3.  On the next page, copy the Client-side ID under the environment your integration is connected to (for example, Test or Production)
    
    Now, you must add the value to your project as an Environment Variable:
    
    1.  Navigate to [your Vercel dashboard](/dashboard) and select the project you want to use LaunchDarkly with
    2.  Under the Settings tab, navigate to Environment Variables, and create an `LD_CLIENT_SIDE_ID` variable with the value of your client-side ID
    
    [See our Environment Variables docs to learn more](/docs/environment-variables#creating-environment-variables).
    
3.  ### [Use the LaunchDarkly integration in your code](#use-the-launchdarkly-integration-in-your-code)
    
    Open your project's code on your local machine and do the following:
    
    1.  Install LaunchDarkly's Vercel Server SDK:
        
        pnpmyarnnpmbun
        
        ```
        pnpm i @launchdarkly/vercel-server-sdk
        ```
        
    2.  Use [Vercel CLI](/docs/cli#installing-vercel-cli) to pull your Vercel project's environment variables:
        
        ```
        vercel env pull
        ```
        
    3.  Finally, create a `middleware.ts` file at the root of your project. This file will configure a Middleware that redirects your site visitors from `/homepage` to `/new-homepage` based on a feature flag fetched from LaunchDarkly:
        
        middleware.ts
        
        TypeScript
        
        TypeScriptJavaScript
        
        ```
        import { init } from '@launchdarkly/vercel-server-sdk';
        import { createClient } from '@vercel/edge-config';
         
        const edgeConfigClient = createClient(process.env.EDGE_CONFIG!);
        const launchDarklyClient = init('YOUR CLIENT-SIDE ID', edgeConfigClient);
         
        export const config = {
          // Only run the middleware on the dashboard route
          matcher: '/homepage',
        };
         
        export default function middleware(request: Request): Response {
          await launchDarklyClient.initFromServerIfNeeded();
          const launchDarklyContext = { kind: 'org', key: 'my-org-key' };
          const showExperimentalHomepage = await launchDarklyClient.variation(
            'experimental-homepage',
            launchDarklyContext,
            true,
          );
         
          if (showExperimentalHomepage) {
            const url = new URL(request.url);
            url.pathname = '/new-homepage';
            return Response.redirect(url);
          }
        }
        ```
        

## [Next steps](#next-steps)

Now that you have set up the LaunchDarkly Edge Config integration, you can explore the following topics to learn more:

*   [Get started with Edge Config](/docs/edge-config/get-started)
*   [Read with the SDK](/docs/edge-config/edge-config-sdk)
*   [Use the dashboard](/docs/edge-config/edge-config-dashboard)
*   [Edge Config limits](/docs/edge-config/edge-config-limits)

--------------------------------------------------------------------------------
title: "Using Edge Config with Split"
description: "Learn how to use Edge Config with Vercel's Split integration."
last_updated: "null"
source: "https://vercel.com/docs/edge-config/edge-config-integrations/split-edge-config"
--------------------------------------------------------------------------------

# Using Edge Config with Split

Copy page

Ask AI about this page

Last updated September 24, 2025

This guide will help you get started with using Vercel's Split integration with Edge Config. This integration allows you to use Edge Config as a configuration source for your Split feature flags.

The Split Edge Config integration is available in [Beta](/docs/release-phases#beta) on [all plans](/docs/plans)

Split is a feature flag provider that tracks event data, enabling you to release features, target them to audiences, and measure their impact on customer experience metrics securely.

The Split Edge Config integration enables you to write your [Split rollout plan](https://help.split.io/hc/en-us/articles/9805284145549-Creating-a-rollout-plan) to an Edge Config. Doing so will allow you to evaluate feature flags at ultra-low latency with Vercel's CDN while tracking events and impressions data with Split.

## [Prerequisites](#prerequisites)

Before using this integration, you should have:

1.  The latest version of Vercel CLI. To check your version, use `vercel --version`. To [install](/docs/cli#installing-vercel-cli) or update Vercel CLI, use:
    
    pnpmyarnnpmbun
    
    ```
    pnpm i -g vercel@latest
    ```
    
2.  A project. If you don't have one, you can run the following terminal commands to create a Next project:
    
    pnpmyarnnpmbun
    
    ```
    pnpm i next
    ```
    
    terminal
    
    ```
    npx create-next-app@latest
    ```
    
3.  A Vercel project. If you don't have one, see [Creating a Project](/docs/projects/overview#creating-a-project)
    
4.  An Edge Config. If you don't have one, follow [the Edge Config quickstart](/docs/edge-config/get-started)
    
5.  The Edge Config SDK:
    
    pnpmyarnnpmbun
    
    ```
    pnpm i @vercel/edge-config
    ```
    

To configure this integration, Split Admin access (Split Admin users can add feature flags and segments, and edit them at will) is required.

1.  ### [Set up the Split integration](#set-up-the-split-integration)
    
    Visit [the Split page in the Vercel Integration Marketplace](/integrations/split) and select the Add Integration button. From the Integration dialog:
    
    1.  Select a Vercel team and project to connect the integration to
    2.  Log into Split
    3.  Select the [Split Environment](https://help.split.io/hc/en-us/articles/360019915771-Environments) you want to use
    4.  Select an existing Edge Config or create a new one
    5.  Copy the Edge Config item key provided on this page. You'll need it to add it to your Environment Variables
    
    You can also find your Edge Config Split item key in [your dashboard on Vercel](/dashboard/integrations). In the **Integrations** tab, select **Manage**, then select **Configure** on the integration page. You should see the item key on the page that opens.
    
2.  ### [Create your feature flags](#create-your-feature-flags)
    
    If you already have existing feature flags, you can skip this step and use those. In this example, we'll create one called `New_Marketing_Page`. You can set the user targeting to Joe and Bobby.
    
    To create a feature flag in Split:
    
    1.  Log into your [Split management console](https://app.split.io/login) and select the workspace icon near the top-left of the page
    2.  In the sidebar, under Target, select Feature flags. Add the name `New_Marketing_Page`, and set the traffic type to `user`. Select Create to finish
    3.  With your feature flag created, select the feature flag and select the Definition tab. Select Initiate Environment to configure your flag
    4.  Add valid users to the feature flag
    5.  Scroll down to Targeting and select Add new individual target
    6.  Under To user, add any username you want to test. This example uses `Joe`.
    7.  Select Add new individual target, then set the Description option to `off`. Add another username under To user. This example uses `Bobby`
    8.  Select Review Changes, then Create to finish
    
    Next, you need to add your credentials to your project's local environment to use the Split integration in your code.
    
3.  ### [Get your credentials](#get-your-credentials)
    
    Next, you'll add the following credentials to your Vercel project:
    
    *   `SPLIT_SDK_CLIENT_API_KEY`
    *   `EDGE_CONFIG_SPLIT_ITEM_KEY`
    *   `EDGE_CONFIG`
    
    To add environment variables to your project, visit [your Vercel dashboard](/dashboard) and select the project you want to use the Split integration with. Then select Settings > Environment Variables.
    
    To get your Split client-side API keys:
    
    1.  Log into your [Split management console](https://app.split.io/login) and select the workspace icon near the top-left of the page
    2.  In the list of options that appears, select Admin Settings, then navigate to API Keys -> SDK API Keys
    3.  Copy the client-side keys associated with the workspace and environment you're using
    
    To add your Edge Config Split item key, if you didn't copy it after setting up the integration on Vercel:
    
    1.  Visit [your dashboard on Vercel](/dashboard/integrations)
    2.  In the Integrations tab, select Manage
    3.  On the integration page, select Configure
    4.  You should see the item key on the page that opens. Copy it
    
    To add your Edge Config's connection string to your project:
    
    1.  Visit your project's page in [the dashboard](/dashboard)
    2.  Select the Storage tab. Select Connect Store and select the Edge Config associated with your Split integration. The `EDGE_CONFIG` environment variable will be set automatically.
    
    Now you're ready to use the Split Edge Config integration in your code.
    
4.  ### [Use the Split integration in your code](#use-the-split-integration-in-your-code)
    
    Open your project's code on your local machine and do the following:
    
    1.  Install Split's Browser SDK, Vercel integration utilities, and Vercel's Edge Config SDK:
        
        pnpmyarnnpmbun
        
        ```
        pnpm i @splitsoftware/splitio-browserjs @splitsoftware/vercel-integration-utils @vercel/edge-config
        ```
        
    2.  Create an API route in your project. The following example fetches a treatement based on which user is visiting. You can specify the user by appending `?userKey=Joe` or `?userKey=Bobby` to the URL when visiting the route:
        
    
    Next.js (/app)Next.js (/pages)Other frameworks
    
    app/api/marketing-example/route.ts
    
    TypeScript
    
    TypeScriptJavaScript
    
    ```
    import {
      SplitFactory,
      PluggableStorage,
      ErrorLogger,
    } from '@splitsoftware/splitio-browserjs';
    import { EdgeConfigWrapper } from '@splitsoftware/vercel-integration-utils';
    import { createClient } from '@vercel/edge-config';
     
    export async function GET(request: Request) {
      const { EDGE_CONFIG_SPLIT_ITEM_KEY, SPLIT_SDK_CLIENT_API_KEY } = process.env;
     
      if (!SPLIT_SDK_CLIENT_API_KEY || !EDGE_CONFIG_SPLIT_ITEM_KEY)
        return new Response(
          `Failed to find your SDK Key (${SPLIT_SDK_CLIENT_API_KEY})
          or item key ${EDGE_CONFIG_SPLIT_ITEM_KEY}`,
        );
     
      const edgeConfigClient = createClient(process.env.EDGE_CONFIG);
      const { searchParams } = new URL(request.url);
      const userKey = searchParams.get('userKey') || 'anonymous';
      const client = SplitFactory({
        core: {
          authorizationKey: SPLIT_SDK_CLIENT_API_KEY,
          key: userKey,
        },
        mode: 'consumer_partial',
        storage: PluggableStorage({
          wrapper: EdgeConfigWrapper({
            // The Edge Config item key where Split stores
            // feature flag definitions
            edgeConfigItemKey: EDGE_CONFIG_SPLIT_ITEM_KEY,
            // The Edge Config client
            edgeConfig: edgeConfigClient,
          }),
        }),
        // Disable or keep only ERROR log level in production,
        // to minimize performance impact
        debug: ErrorLogger(),
      }).client();
     
      await new Promise((resolve) => {
        client.on(client.Event.SDK_READY, () => resolve);
        client.on(client.Event.SDK_READY_TIMED_OUT, () => resolve);
      });
     
      // Replace this with the feature flag you want
      const FEATURE_FLAG = 'New_Marketing_Page';
      const treatment = await client.getTreatment(FEATURE_FLAG);
     
      // Must await in app-router; waitUntil() is not
      // yet supported
      await client.destroy();
     
      // treatment will be 'control' if the SDK timed out
      if (treatment == 'control') return new Response('Control marketing page');
     
      return treatment === 'on'
        ? new Response('New marketing page')
        : new Response('Old marketing page');
    }
    ```
    
5.  ### [Test your code](#test-your-code)
    
    1.  Start a local development server. If you're using Vercel CLI, enter the following command in the terminal:
    
    terminal
    
    ```
    vercel dev
    ```
    
    1.  Navigate to [http://localhost:3000/api/split-example?userKey=Joe](http://localhost:3000/api/split-example?userKey=Joe). You should see either `New marketing page` or `Old marketing page` based on how your feature flags are configured in Split
        *   Try changing the `userKey` search param's value to `Bobby`, or deleting it altogether, to see different responses when you visit the route

## [Next steps](#next-steps)

Now that you have set up the Split Edge Config integration, you can explore the following topics to learn more:

*   [Get started with Edge Config](/docs/edge-config/get-started)
*   [Read with the SDK](/docs/edge-config/edge-config-sdk)
*   [Use the dashboard](/docs/edge-config/edge-config-dashboard)
*   [Edge Config limits](/docs/edge-config/edge-config-limits)

--------------------------------------------------------------------------------
title: "Using Edge Config with Statsig"
description: "Learn how to use Edge Config with Vercel's Statsig integration."
last_updated: "null"
source: "https://vercel.com/docs/edge-config/edge-config-integrations/statsig-edge-config"
--------------------------------------------------------------------------------

# Using Edge Config with Statsig

Copy page

Ask AI about this page

Last updated October 9, 2025

This guide will help you get started with using Vercel's Statsig integration with Edge Config. This integration allows you to use Edge Config as a configuration source for your Statsig feature flags.

Statsig is a statistics engine that enables you to automate A/B testing and make data-driven decisions at scale. The Statsig integration enables you to replace hard-coded values in your application with dynamic values on the server.

## [Prerequisites](#prerequisites)

Before using this integration, you should have:

1.  The latest version of Vercel CLI. To check your version, use `vercel --version`. To [install](/docs/cli#installing-vercel-cli) or update Vercel CLI, use:
    
    pnpmyarnnpmbun
    
    ```
    pnpm i -g vercel@latest
    ```
    
2.  A project. If you don't have one, you can run the following terminal commands to create a Next project:
    
    pnpmyarnnpmbun
    
    ```
    pnpm i next
    ```
    
    terminal
    
    ```
    npx create-next-app@latest
    ```
    
3.  A Vercel project. If you don't have one, see [Creating a Project](/docs/projects/overview#creating-a-project)
    
4.  An Edge Config. If you don't have one, follow [the Edge Config quickstart](/docs/edge-config/get-started)
    
5.  The Edge Config SDK:
    
    pnpmyarnnpmbun
    
    ```
    pnpm i @vercel/edge-config
    ```
    

1.  ### [Set up the Statsig integration](#set-up-the-statsig-integration)
    
    Visit [the Statsig page in the Integration Marketplace](/integrations/statsig) and select the Add Integration button. Then:
    
    1.  Select a Vercel team and Vercel project for your integration to be applied to
    2.  Log into Statsig
    3.  Select or create a new Edge Config to connect to Statsig
    4.  Statsig will provide you with a [Connection String](/docs/edge-config/using-edge-config#using-a-connection-string) and Edge Config Item Key. Save both, as you'll need them later in the setup
2.  ### [Add your Environment Variables](#add-your-environment-variables)
    
    Navigate to [your Vercel dashboard](/dashboard), and select the project you want to use the Statsig integration with.
    
    Under the Settings tab, navigate to Environment Variables, and add the following variables:
    
    1.  `EDGE_CONFIG`: Set this to the value of your Connection String
    2.  `EDGE_CONFIG_ITEM_KEY`: Set this to the value of your Edge Config Item Key
    
    See [our Environment Variables documentation](/docs/environment-variables#creating-environment-variables) to learn more.
    
3.  ### [Use the Statsig integration in your code](#use-the-statsig-integration-in-your-code)
    
    Statsig's [`statsig-node-vercel`](https://www.npmjs.com/package/statsig-node-vercel) package offers an `EdgeConfigDataAdapter` class, which you can use to initialize Statsig experiments with Edge Config.
    
    The following example sets up a Statsig experiment with Edge Config in an [Middleware](/docs/routing-middleware) file, using the `EDGE_CONFIG_ITEM_KEY` environment variable.
    
    Next.js (/app)Next.js (/pages)Other frameworks
    
    middleware.ts
    
    TypeScript
    
    TypeScriptJavaScript
    
    ```
    import { NextResponse } from 'next/server';
    import type { NextRequest, NextFetchEvent } from 'next/server';
    import Statsig from 'statsig-node';
    import { createClient } from '@vercel/edge-config';
    import { EdgeConfigDataAdapter } from 'statsig-node-vercel';
     
    export const config = {
      matcher: '/',
    };
     
    const edgeConfigClient = createClient(process.env.EDGE_CONFIG!);
    const dataAdapter = new EdgeConfigDataAdapter({
      edgeConfigClient: edgeConfigClient,
      edgeConfigItemKey: process.env.EDGE_CONFIG_ITEM_KEY!,
    });
     
    export async function middleware(request: NextRequest, event: NextFetchEvent) {
      await Statsig.initialize('statsig-server-api-key-here', { dataAdapter });
     
      const experiment = await Statsig.getExperiment(
        { userID: 'exampleId' },
        'statsig_example_experiment',
      );
     
      // Do any other experiment actions here
     
      // Ensure that all logged events are flushed to Statsig servers before the middleware exits
      event.waitUntil(Statsig.flush());
     
      return NextResponse.next();
    }
    ```
    

## [Next steps](#next-steps)

Now that you have set up the Statsig Edge Config integration, you can explore the following topics to learn more:

*   [Get started with Edge Config](/docs/edge-config/get-started)
*   [Read with the SDK](/docs/edge-config/edge-config-sdk)
*   [Use the dashboard](/docs/edge-config/edge-config-dashboard)
*   [Edge Config limits](/docs/edge-config/edge-config-limits)

--------------------------------------------------------------------------------
title: "Edge Config Limits and pricing"
description: "Learn about the Edge Configs limits and pricing based on account plans."
last_updated: "null"
source: "https://vercel.com/docs/edge-config/edge-config-limits"
--------------------------------------------------------------------------------

# Edge Config Limits and pricing

Copy page

Ask AI about this page

Last updated September 15, 2025

An [Edge Config](/edge-config) is a global data store that [enables experimentation with feature flags, A/B testing, critical redirects, and IP blocking](/edge-config#use-cases). It enables you to read data at the edge without querying an external database or hitting upstream servers.

Keep the number of stores to a minimum. Fewer large stores improve your overall latency.

## [Pricing](#pricing)

The following table outlines the price for each resource according to the plan you are on:

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

[Edge Config Reads](/docs/edge-config/using-edge-config)

 | First 100,000 | $3.00/1,000,000 Reads |
| 

[Edge Config Writes](/docs/edge-config/using-edge-config)

 | First 100 | $5.00/500 Writes |

## [Limits by plan](#limits-by-plan)

The following table outlines the limits for each resource according to the plan you are on:

|  | Hobby | Pro | Enterprise |
| --- | --- | --- | --- |
| [Maximum store size](#maximum-store-size) | 8 KB | 64 KB | 512 KB  
Can request higher limit by [contacting customer success](/help)

 |
| [Maximum number of stores (total)](#maximum-number-of-stores) | 1 | 3 | 10  

Can request higher limit by [contacting customer success](/help)

 |
| [Maximum number of stores connected to a project](#maximum-number-of-stores-connected-to-a-project) | 1 | 3 | 3 |
| [Maximum item key name length](#maximum-item-key-name-length) | 256 characters | 256 characters | 256 characters |
| 

[Write propagation](#write-propagation) | Up to 10 seconds globally | Up to 10 seconds globally | Up to 10 seconds globally |
| [Backup retention](#backup-retention) | 7 days | 90 days | 365 days |

## [Usage](#usage)

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

See the [manage and optimize Edge Config usage](/docs/pricing/edge-config) section for more information on how to optimize your usage.

### [Reads](#reads)

Reads indicate how often your project has requested access to Edge Config to retrieve data through the SDK or the REST API. Vercel counts it as one read, regardless of whether you retrieve one or all items.

### [Writes](#writes)

Writes represent how often you updated your Edge Config through the SDK or the REST API.

### [Maximum store size](#maximum-store-size)

The maximum store size represents the total size limit of each Edge Config store, including all keys and values of the document.

### [Maximum number of stores](#maximum-number-of-stores)

The maximum number of stores represents the total number of Edge Config stores that you can create for your account or team.

### [Maximum number of stores connected to a project](#maximum-number-of-stores-connected-to-a-project)

The maximum number of stores connected to a project represents the total number of Edge Config stores that you can connect to a single project. Exceeding this amount will result in an [error](/docs/edge-config/edge-config-limits#edge-config-limit-reached).

### [Maximum item key name length](#maximum-item-key-name-length)

Each key name in your Edge Config can be up to 256 characters long. The key name must adhere to the regex pattern `^[\w-]+$`, which is equivalent to `/^[A-Za-z0-9_-]+$/`, and allows A-Z, a-z, 0-9, `_`, and `-`.

### [Write propagation](#write-propagation)

When updating an item in your Edge Config, it may take up to 10 seconds for the update to be globally propagated. You should avoid using Edge Configs for frequently updated data or data that needs to be accessed immediately after updating.

### [Backup retention](#backup-retention)

Backups are automatically saved when you make any changes, allowing you to [restore](/docs/edge-config/edge-config-dashboard#restoring-edge-config-backups) to a previous version. See the table above to learn about how long backups are saved for.

To learn more about backups, see [Edge Config backups](/docs/edge-config/using-edge-config#edge-config-backups)

## [Reviewing Edge Config reads](#reviewing-edge-config-reads)

The Reads chart shows the number of times your [Edge Config](/docs/functions/edge-config) has been read. You can filter the data by Count or Projects.

### [Optimizing Edge Config reads](#optimizing-edge-config-reads)

*   Select the Project tab to identify which project has the most Edge Config reads
*   Review how you access the stores through both the [REST API](/docs/edge-config/vercel-api) and the [SDK](/docs/edge-config/edge-config-sdk). They both count toward your reads
*   Where possible, use [`getAll()`](/docs/edge-config/edge-config-sdk#read-multiple-values) instead of separate [`get(key)`](/docs/edge-config/edge-config-sdk#read-a-single-value) calls with the SDK, ensuring they count as a single read.

## [Managing Edge Config writes](#managing-edge-config-writes)

The Writes chart shows the number of times your [Edge Configs](/docs/functions/edge-config) were updated. You can filter the data by Count or Edge Configs.

### [Optimizing Edge Config writes](#optimizing-edge-config-writes)

*   Select the Edge Configs tab to identify which Edge Config has the most Edge Config writes
*   Review your points of updating the stores through the [REST API](/docs/edge-config/vercel-api) as they count towards your writes

## [Troubleshooting](#troubleshooting)

If reading from your Edge Config seems slower than expected, ensure that the following are true:

*   You've set [the connection string](/docs/edge-config/using-edge-config#using-a-connection-string) as an environment variable
*   You are using the [SDK](/docs/edge-config/edge-config-sdk) to read from your Edge Config
*   You see the Edge Config icon on the row for the connected environment variable on the Environment Variables page of your project settings
*   You are testing on your Vercel deployment, as the optimizations happen only when you deploy to Vercel
    
    ![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fstorage%2Fedge-config%2Fedge-config-env-icon-light.png&w=1920&q=75)![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fstorage%2Fedge-config%2Fedge-config-env-icon-dark.png&w=1920&q=75)
    
    Edge Config icon with connected environment variable
    
*   You are testing your Vercel deployment. The optimizations happen only when you deploy to Vercel

### [Edge Config Limit reached](#edge-config-limit-reached)

Error: `Tried to attach 4 Edge Configs. Only 3 can be attached to one Deployment at a time.`

Depending on your plan, you can have up to 10 Edge Config stores created for your account. However, you are limited to a maximum of 3 Edge Config stores connected to any single project.

If you get this error, review your storage by visiting [the Vercel Dashboard](/dashboard), selecting your project, and selecting the Storage tab. You can use the search filter to see only your Edge Configs. You will have to disconnect one of the stores and redeploy your project.

To learn how to prevent this error, see [best practices](#edge-config-best-practices).

### [Edge Config update rejected](#edge-config-update-rejected)

Updates to items in your Edge Config will be rejected if the resulting size of your Edge Config would exceed your account plan's limits. When this happens, all members of your team will receive a [notification](/docs/notifications) from Vercel, whether the error originated in the dashboard, an API request, or an [Integration](/docs/edge-config/integrations). The Edge Config editor in your dashboard can detect many cases where the final size would exceed the limit and warn you upfront without triggering the notification.

To resolve this issue, you can:

*   Delete unused entries from your Edge Config to free up space
*   [Upgrade your plan](/pricing)
*   [Contact sales](/contact/sales) to unlock larger Edge Config store sizes

## [Edge Config best practices](#edge-config-best-practices)

*   Where possible, having fewer large stores is better than having multiple small stores, as having fewer Edge Config stores requested more often leads to lower overall latency.

## [Security](#security)

If you are developing locally or self-hosting, your Edge Config is loaded through the public internet network. In this case, you may wonder if it's safe to have the token as a parameter in the connection string.

*   It is safe to have the token as a parameter in the connection string, because the SDK parses the passed string, then sends the token through an `Authorization` header instead

--------------------------------------------------------------------------------
title: "@vercel/edge-config"
description: "The Edge Config client SDK is the most ergonomic way to read data from Edge Configs. Learn how to set up the SDK so you can start reading Edge Configs."
last_updated: "null"
source: "https://vercel.com/docs/edge-config/edge-config-sdk"
--------------------------------------------------------------------------------

# @vercel/edge-config

Copy page

Ask AI about this page

Last updated July 18, 2025

The [Edge Config](/edge-config) client SDK is the most ergonomic way to read data from Edge Configs. It provides several helper methods for reading values from one or multiple Edge Configs, and is compatible with Node.js, [the Edge Runtime](/docs/functions/runtimes/edge), and the browser.

It does not have functionality for _creating_ new Edge Configs and _writing_ to existing Edge Configs, which can be done [using the Vercel REST API](/docs/edge-config/vercel-api) or the [Dashboard](/docs/edge-config/edge-config-dashboard).

You can also [read Edge Config data with the Vercel REST API](/docs/edge-config/vercel-api#read-all-items). Review [Reading from an Edge Config](/docs/edge-config/using-edge-config#reading-data-from-edge-configs) to understand when to use the SDK versus the Vercel REST API.

## [Requirements](#requirements)

Before you can start using the SDK, you need to have done the following:

*   Created an Edge Config, which can be done using the [API](/docs/edge-config/vercel-api#create-an-edge-config) or the [Dashboard](/docs/edge-config/edge-config-dashboard#creating-an-edge-config)
*   Added [an Edge Config read access token](/docs/edge-config/using-edge-config#creating-a-read-access-token) to access your Edge Config
*   Defined [a connection string](/docs/edge-config/using-edge-config#using-a-connection-string) with the Edge Config read access token and Edge Config id and stored it as an environment variable

## [Setting up the SDK](#setting-up-the-sdk)

To get started, install the SDK:

pnpmyarnnpmbun

```
pnpm i @vercel/edge-config
```

## [Use connection strings](#use-connection-strings)

Use connection strings to connect your Edge Config to one or more projects. This allows Vercel to optimize your reads when you read the Edge Config through the SDK. You can learn how to create a connection string [here](/docs/edge-config/using-edge-config#using-a-connection-string).

By default, the SDK will run all helper methods using the connection string stored in the `EDGE_CONFIG` environment variable. That means, if you have the `EDGE_CONFIG` environment variable set in your project, you can import any of the helper methods and use them like so:

example.ts

```
import { NextResponse } from 'next/server';
import { getAll } from '@vercel/edge-config';
 
const configItems = await getAll();
```

However, you can store your connection string as any environment variable, and even connect to multiple Edge Configs by storing more than one connection string in your environment variables.

To do so, you must use the `createClient` helper.

The `createClient` helper method takes a connection string and returns an object that lets you use helper methods on the associated Edge Config. Using `createClient`, you can store multiple Edge Configs as environment variables and read data from all of them.

```
import { createClient } from '@vercel/edge-config';
 
// Fetch a single value from one config
const firstConfig = createClient(process.env.FIRST_EDGE_CONFIG);
const firstExampleValue1 = await firstConfig.get('other_example_key_1');
 
// Fetch all values from another config
const secondConfig = createClient(process.env.SECOND_EDGE_CONFIG);
const allValues = await secondConfig.getAll();
```

The following sections will teach you how to use all of the SDK's helper methods.

## [Read a single value](#read-a-single-value)

The `get` helper method allows you to fetch a value at a given key in your Edge Config.

Next.js (/app)Next.js (/pages)Other frameworks

app/api/get-example/route.ts

TypeScript

TypeScriptJavaScript

```
import { NextResponse } from 'next/server';
import { get } from '@vercel/edge-config';
 
export async function GET() {
  const val = await get('key');
 
  return NextResponse.json({
    label: `Value of "key" in my Edge Config.`,
    value: val,
  });
}
```

## [Read multiple values](#read-multiple-values)

The `getAll` helper method returns all of your Edge Config's items.

Next.js (/app)Next.js (/pages)Other frameworks

app/api/getall-example/route.ts

TypeScript

TypeScriptJavaScript

```
import { NextResponse } from 'next/server';
import { getAll } from '@vercel/edge-config';
 
export async function GET() {
  const configItems = await getAll();
 
  return NextResponse.json({
    label: `These are all the values in my Edge Config.`,
    value: configItems,
  });
}
```

Passing an array of key names causes `getAll` to return only the specified keys.

Next.js (/app)Next.js (/pages)Other frameworks

app/api/getall-keys-example/route.ts

TypeScript

TypeScriptJavaScript

```
import { NextResponse } from 'next/server';
import { getAll } from '@vercel/edge-config';
 
export async function GET() {
  const someItems = await getAll(['keyA', 'keyB']);
 
  return NextResponse.json({
    label: `These are a few values in my Edge Config.`,
    value: someItems,
  });
}
```

## [Check if a key exists](#check-if-a-key-exists)

The `has` helper method lets you verify if a key exists in your Edge Config. It returns `true` if the key does, and `false` if it doesn't.

Next.js (/app)Next.js (/pages)Other frameworks

app/api/has-example/route.ts

TypeScript

TypeScriptJavaScript

```
import { NextResponse } from 'next/server';
import { has } from '@vercel/edge-config';
 
export async function GET() {
  const exists = await has('key');
 
  return NextResponse.json({
    keyExists: exists ? `The key exists!` : `The key doesn't exist!`,
  });
}
```

## [Check the Edge Config version](#check-the-edge-config-version)

Every Edge Config has a hash string associated with it, which is updated whenever the Config is updated. Checking this digest can help you verify whether your Edge Config has properly updated, and confirm which version of the Config you're working with.

The `digest` helper method lets you check the version of the Edge Config you're reading.

Next.js (/app)Next.js (/pages)Other frameworks

app/api/digest-example/route.ts

TypeScript

TypeScriptJavaScript

```
import { NextResponse } from 'next/server';
import { digest } from '@vercel/edge-config';
 
export async function GET() {
  const version = await digest();
 
  return NextResponse.json({
    digest: version,
  });
}
```

The digest's creation may change, so it is not documented. A matching digest indicates that the Edge Config content remains unchanged, while a different digest suggests changes but does not guarantee them.

## [Writing Edge Config Items](#writing-edge-config-items)

You cannot write to Edge Config items using the Edge Config SDK. Instead, you can programmatically write using the [Vercel REST API](/docs/edge-config/vercel-api#update-your-edge-config-items).

The Edge Config SDK is designed to read from our `edge-config.vercel.com` endpoint using read only tokens to authenticate reads, while writing requires [Vercel Access Tokens to authenticate with the Vercel REST API](/docs/rest-api#authentication). This core distinction makes it impractical to use the SDK for writes.

If your project requires frequent writes, you should [learn more about Vercel KV](/docs/storage/vercel-kv).

## [Errors](#errors)

All helper methods throw errors when:

*   Your Edge Config read access token is invalid
*   The Edge Config you're reading from doesn't exists
*   A network error occurs

## [Up Next](#up-next)

[

#### Manage with the Dashboard

Manage your Edge Configs at different levels in your Vercel Dashboard

](/docs/edge-config/edge-config-dashboard)

--------------------------------------------------------------------------------
title: "Getting started with Edge Config"
description: "Learn how to create an Edge Config store and read from it in your project."
last_updated: "null"
source: "https://vercel.com/docs/edge-config/get-started"
--------------------------------------------------------------------------------

# Getting started with Edge Config

Copy page

Ask AI about this page

Last updated September 24, 2025

Edge Config is a distributed key-value store that allows you to store and retrieve data at the network edge, close to your users. It is designed for high performance and low latency, making it ideal for use cases such as feature flags, A/B testing, and dynamic configuration.

This guide will help you will create an Edge Config called `hello_world_store` at the project-level, through the Vercel [dashboard](/dashboard). A token and environment variable `EDGE_CONFIG`, that stores the connection string, will be automatically created for you. You'll update the store with a key-value data pair and read the value of `"greeting"` from a local Next.js project.

## [Prerequisites](#prerequisites)

*   Install the Edge Config SDK:
    
    pnpmyarnnpmbun
    
    ```
    pnpm i @vercel/edge-config
    ```
    
*   An existing project. This quickstart uses Next.js, but you can use any supported framework with Edge Config storage
*   [Install](/docs/cli#installing-vercel-cli) or [update](/docs/cli#updating-vercel-cli) to the latest version of Vercel CLI
    
    pnpmyarnnpmbun
    
    ```
    pnpm i -g vercel@latest
    ```
    

1.  ### [Create an Edge Config store](#create-an-edge-config-store)
    
    Navigate to the [Project](/docs/projects/overview) you'd like to add an Edge Config store to. Click on the Storage tab, then click the Create Database button. Select Edge Config and click Continue.
    
    Create a new store by typing `hello_world_store` under Edge Config in the dialog that opens, and click Create.
    
    The name can only contain alphanumeric letters, "\_" and "-". It cannot exceed 32 characters.
    
2.  ### [Review what was created](#review-what-was-created)
    
    Once created, select `hello_world_store` to see a summary of what was created for you. Notice the following:
    
    *   If you select Project, you'll see that your project was connected to the Edge Config by using an environment variable. If you go to your projects's Settings > Environment Variables, you'll see the newly created environment variable.
    *   If you select Tokens, you'll see a [read access token](/docs/edge-config/using-edge-config#creating-a-read-access-token). This token, along with your EDGE CONFIG ID, is used to create a [connection string](/docs/edge-config/using-edge-config#using-a-connection-string). This connection string is saved as the value of your `EDGE_CONFIG` environment variable. This enables you to use the SDK in your project to read the store's contents.
    
    If you're creating a project at the account-level, we won't automatically create a token, connection string, and environment variable until a project has been connected.
    
3.  ### [Add a key-value pair](#add-a-key-value-pair)
    
    Under Items, add the following key-value pair and click Save Items:
    
    ```
    {
      "greeting": "hello world"
    }
    ```
    
    You can see more information about what can be stored in an Edge Config in the [limits](/docs/edge-config/edge-config-limits) documentation.
    
4.  ### [Connect your Vercel project](#connect-your-vercel-project)
    
    Once you've created the store, you need to set up your project to read the contents of the store. This is detailed under Learn how to use this in code in the dashboard, but is described in the following steps in more detail.
    
    On your local machine, connect your Vercel Project. If you haven't already, install the Edge Config SDK, as mentioned in [prerequisites](#prerequisites).
    
5.  ### [Pull the latest environment variables](#pull-the-latest-environment-variables)
    
    Using Vercel CLI, pull the latest environment variables, specifically `EDGE_CONFIG`, so that it's available to your project locally:
    
    terminal
    
    ```
    vercel env pull
    ```
    
6.  ### [Create a Middleware](#create-a-middleware)
    
    Create a [Middleware](/docs/routing-middleware) for your project by creating a new file called `middleware.js` at the root of the project and if using Next.js, add the following code:
    
    middleware.ts
    
    TypeScript
    
    TypeScriptJavaScript
    
    ```
    import { NextResponse } from 'next/server';
    import { get } from '@vercel/edge-config';
     
    export const config = { matcher: '/welcome' };
     
    export async function middleware() {
      const greeting = await get('greeting');
      return NextResponse.json(greeting);
    }
    ```
    
    `NextResponse.json` requires at least Next v13.1 or enabling `experimental.allowMiddlewareResponseBody` in `next.config.js`.
    
7.  ### [Run your application locally](#run-your-application-locally)
    
    Run your application locally and visit `localhost:3000/welcome` to see your greeting. The middleware intercepts requests to `localhost:3000/welcome` and responds with a greeting, read from your Edge Config store.
    

Your project is now ready to read more key-value data pairs from the `hello_world_store` Edge Config using the [SDK](/docs/edge-config/edge-config-sdk) or [Vercel REST API](/docs/edge-config/vercel-api).

Your Edge Config uses the public internet for reads when you develop locally. Therefore, you will see higher response times. However, when you deploy your application to Vercel, the reads are optimized to happen at ultra low latency without any network requests.

## [Next steps](#next-steps)

Now that you've created an Edge Config store and read from it, you can explore the following:

*   [Creating the Edge Config at the account level](/docs/edge-config/edge-config-dashboard#at-the-account-level)
*   [Creating a read access token](/docs/edge-config/using-edge-config#creating-a-read-access-token)
*   [Setting up a connection string](/docs/edge-config/using-edge-config#using-a-connection-string)
*   [Learn about the `@vercel/edge-config` package](https://github.com/vercel/storage/tree/main/packages/edge-config#readme)
*   [Explore the SDK](/docs/edge-config/edge-config-sdk)

--------------------------------------------------------------------------------
title: "Using Edge Config"
description: "Learn how to use Edge Configs in your projects."
last_updated: "null"
source: "https://vercel.com/docs/edge-config/using-edge-config"
--------------------------------------------------------------------------------

# Using Edge Config

Copy page

Ask AI about this page

Last updated September 24, 2025

[Edge Config](/docs/edge-config) is a global data store that offers ultra-low latency read speeds from anywhere in the world thanks to [Vercel's CDN](/docs/cdn).

We recommend using [the Edge Config client SDK](/docs/edge-config/edge-config-sdk) to read data from your Edge Configs. To write data to your Edge Configs, use [Vercel REST API](/docs/rest-api) as outlined in [our docs on managing Edge Configs with the API](/docs/edge-config/vercel-api).

This page outlines all the ways you can interact with your Edge Configs, and our recommended best approaches.

## [Reading data from Edge Configs](#reading-data-from-edge-configs)

There are multiple ways to read data from your Edge Configs, but we recommend using [our Edge Config client SDK](/docs/edge-config/edge-config-sdk) in your projects.

If you prefer making direct API requests to your Edge Config, we recommend sending them to your [Edge Config endpoint](#understanding-edge-config-endpoints). You can request data through Vercel REST API, but we recommend against ever doing so. Requests to Vercel REST API do not benefit from the optimizations Vercel applies to Edge Config reads. Requests to an Edge Config endpoint do.

Edge Config is optimized to work with Vercel's CDN. As a result, Edge Configs accessed from local development environments cannot benefit from Vercel's optimizations and will be over 100 milliseconds slower than production.

### [Understanding Edge Config endpoints](#understanding-edge-config-endpoints)

Edge Config is available at two separate REST APIs which are built for distinct use cases:

*   `api.vercel.com`: [Vercel REST API](/docs/rest-api) built for managing Edge Config
*   `edge-config.vercel.com`: [Edge Config endpoint](/docs/edge-config/using-edge-config#querying-edge-config-endpoints) intended for reading Edge Config at high volume

#### [`api.vercel.com`](#api.vercel.com)

*   This endpoint is part of the [Vercel REST API](/docs/rest-api)
*   It is intended to [manage Edge Configs](/docs/edge-config/vercel-api)
*   You can use this endpoint to create, update, and delete Edge Configs
*   This endpoint is served from a single region and we do not apply any of our read optimizations
*   This endpoint is rate limited to 20 Edge Config Item reads per minute
*   Reading Edge Config from this endpoint will always return the latest version of an Edge Config
*   This endpoint uses the [Vercel REST API authentication](/docs/rest-api#authentication)

#### [`edge-config.vercel.com`](#edge-config.vercel.com)

*   This is a highly optimized, globally distributed, actively replicated endpoint built for global, low latency, high volume reads
*   This endpoint has no rate limits
*   This is the endpoint [`@vercel/edge-config`](/docs/edge-config/edge-config-sdk) reads from
*   This endpoint uses the Edge Config's own [Read Access tokens](/docs/edge-config/using-edge-config#creating-a-read-access-token)

#### [Querying Edge Config endpoints](#querying-edge-config-endpoints)

You can use the following routes when querying your Edge Config endpoint:

*   `/<edgeConfigId>/items`
*   `/<edgeConfigId>/item/<itemKey>`
*   `/<edgeConfigId>/digest`

You can authenticate with a [Read Access token](/docs/edge-config/using-edge-config#creating-a-read-access-token), which you can add to the `Authorization` header of your request, setting `Bearer <token>` as the value.

### [Finding your Edge Config ID](#finding-your-edge-config-id)

You can find your Edge Config ID with one of the following methods:

*   In your dashboard, under the Storage tab. Select your Edge Config, and you'll see the ID under the Edge Config ID label near the top of the page, as shown in the screenshot below:

![Your Edge Config ID in the Vercel Dashboard.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fstorage%2Fedge-config%2Fconfig-id-light.png&w=3840&q=75)![Your Edge Config ID in the Vercel Dashboard.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fstorage%2Fedge-config%2Fconfig-id-dark.png&w=3840&q=75)

Your Edge Config ID in the Vercel Dashboard.

*   Send a `GET` request to the `/edge-config` endpoint of Vercel REST API, as outlined in [our API reference](/docs/rest-api/reference/endpoints/edge-config/get-edge-configs). The response will be a list of Edge Configs associated with your account (or team, if you add the `teamId` query parameter)

```
https://api.vercel.com/v1/edge-config?teamId=<teamId>
```

### [Creating a read access token](#creating-a-read-access-token)

A read access token is automatically generated when you connect an Edge Config to a project.

There are multiple ways to create a Read Access token for your Edge Config manually:

*   In the Storage tab of your project dashboard. See [our Edge Config dashboard docs](/docs/edge-config/edge-config-dashboard#managing-read-access-tokens) to learn how
*   Through a `POST` request to Vercel REST API

#### [Using Vercel API](#using-vercel-api)

First, you'll need an access token for Vercel REST API, which you must add to an `Authorization` header with the `Bearer <token>` pattern to validate requests. To learn more, see [Creating an access token](/docs/rest-api#creating-an-access-token).

Then you can send a `POST` request to the [`/edge-config/<edgeConfigId>/token`](/docs/rest-api/reference/endpoints/edge-config/create-an-edge-config) path, as shown below, inserting [your Edge Config's ID](#finding-your-edge-config-id) where appropriate:

cURLfetch

cURL

```
curl -X 'POST' 'https://api.vercel.com/v1/edge-config/my_edge_config_id/token' \
     -H 'Authorization: Bearer your_vercel_api_token_here' \
     -H 'Content-Type: application/json; charset=utf-8' \
     -d $'{ "label": "my edge config token label" }'
```

fetch

```
try {
  const createReadAccessToken = await fetch(
    'https://api.vercel.com/v1/edge-config/my_edge_config_id/token',
    {
      method: 'POST',
      headers: {
        Authorization: `Bearer ${your_vercel_api_token_here}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        label: 'my edge config token label',
      }),
    },
  );
  const result = await createReadAccessToken.json();
  console.log(result);
} catch (error) {
  console.log(error);
}
```

Append the `teamId` query parameter to if the config is scoped to a Vercel team.

The response from the API will be a JSON object with a `"token"` key that contains the value for the Edge Config read access token:

response

```
{ "token": "your_edge_config_read_access_token_here" }
```

### [Using a connection string](#using-a-connection-string)

A connection string is a URL that connects a project to an Edge Config.

To find and copy the connection string:

1.  Navigate to the Tokens tab of your project's Storage dashboard
2.  Select the three dots icon displayed in the list of tokens
3.  Select Copy Connection String from the dropdown menu

![Copy your Edge Config connection string from the dashboard.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fedge-config%2Fcopy-edge-config-connection-string-light.png&w=2048&q=75)![Copy your Edge Config connection string from the dashboard.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fedge-config%2Fcopy-edge-config-connection-string-dark.png&w=2048&q=75)

Copy your Edge Config connection string from the dashboard.

A token is not created when you create an Edge Config at the account level, until you connect a project.

Vercel will optimize your reads to be faster if you set the connection string as an environment variable. Hard-coding your connection string into your application as a string will not allow Vercel to detect the URL and optimize your reads.

The variable can be called anything, but [our Edge Config client SDK](/docs/edge-config/edge-config-sdk) will search for `process.env.EDGE_CONFIG` by default. See our [environment variables](/docs/environment-variables#creating-environment-variables) docs to learn how to create one.

## [Writing data to Edge Configs](#writing-data-to-edge-configs)

Edge Config is optimized for many reads and few writes. To write data to your Edge Configs, see [our docs on doing so with Vercel REST API](/docs/edge-config/vercel-api).

## [Edge Config backups](#edge-config-backups)

Edge Config backups are a backup and restore functionality that allows you to access and roll back to a previous point in time.

Restoring a backup will immediately update the live data, and the data that was live before the restore will become available as a new backup.

Backups are taken when you make any changes either through the dashboard or API. They do not contribute to your storage size. The length of time each backup is held for depends on your plan, see [Limits and Pricing](/docs/edge-config/edge-config-limits) for more information.

--------------------------------------------------------------------------------
title: "Managing Edge Configs with Vercel REST API"
description: "Learn how to use the Vercel REST API to create and update Edge Configs. You can also read data stored in Edge Configs with the Vercel REST API."
last_updated: "null"
source: "https://vercel.com/docs/edge-config/vercel-api"
--------------------------------------------------------------------------------

# Managing Edge Configs with Vercel REST API

Copy page

Ask AI about this page

Last updated September 24, 2025

We recommend you use the Vercel REST API only for creating and updating an [Edge Config](/edge-config). For reading data (which you should do more often), we highly recommend using the [SDK](/docs/edge-config/edge-config-sdk).

Updates to your Edge Config can take up to a few seconds to propagate globally, and therefore might not be available from the Edge Config API endpoint immediately. However, fetching your Edge Config data from the Vercel REST API will always return the latest version of your Config. The request will not have Vercel's optimizations, and the response will not be served through Vercel's [CDN](/docs/cdn).

You can also request metadata about your Edge Configs through the API.

This section will show you how to update, read metadata about, and read the contents of your Edge Configs with the Vercel REST API. To learn about other Vercel REST API functionality with Edge Configs, [read our API spec reference](/docs/rest-api/reference/endpoints/edge-config).

## [Create an Edge Config](#create-an-edge-config)

To create an Edge Config with the [Vercel REST API](/docs/rest-api), make a `POST` request to the `edge-config` path of the API endpoint. Your URL should look like this:

endpoint

```
'https://api.vercel.com/v1/edge-config';
```

The request body should be a JSON object containing a `"slug"` with the name you would like to call your Edge Config as its value.

The name can only contain alphanumeric letters, "\_" and "-". It cannot exceed 32 characters.

See the example below:

cURLfetch

cURL

```
curl  -X 'POST' 'https://api.vercel.com/v1/edge-config' \
      -H 'Authorization: Bearer your_vercel_api_token_here' \
      -H 'Content-Type: application/json; charset=utf-8' \
      -d $'{ "slug": "your_edge_config_name_here" }'
```

fetch

```
try {
  const createEdgeConfig = await fetch(
    'https://api.vercel.com/v1/edge-config',
    {
      method: 'POST',
      headers: {
        Authorization: `Bearer ${your_vercel_api_token_here}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        slug: 'your_edge_config_name_here',
      }),
    },
  );
  const result = await createEdgeConfig.json();
  console.log(result);
} catch (error) {
  console.log(error);
}
```

Upon success, you should receive a JSON response similar to the following:

response

```
{
  "createdAt": 1234567890123,
  "updatedAt": 1234567890123,
  "slug": "your_edge_config_slug_here",
  "id": "your_edge_config_id_here",
  "digest": "abc123efg456hij789",
  "sizeInBytes": 2,
  "itemCount": 0,
  "ownerId": "your_id_here"
}
```

The above example will create an Edge Config scoped to your Hobby team. To scope your Edge Config to a Vercel Team:

*   [Generate a Vercel REST API access token](/docs/rest-api/vercel-api-integrations#create-an-access-token) that is scoped to the appropriate Vercel Team
*   Add the `?teamId` query parameter to your `POST` request. Set its value to [the Team's ID](/docs/accounts#find-your-team-id), which you can find under the Settings tab in the Team's Dashboard on Vercel.

The `"ownerId"` key's value will be your [Vercel Team's ID](/docs/accounts#find-your-team-id) if you created the Edge Config using the `?teamId` query parameter.

## [Update your Edge Config items](#update-your-edge-config-items)

To add an item to or update an item in your Edge Config, send a `PATCH` request to the `edge-config` endpoint, appending `/your_edge_config_id_here/items` to the end.

If you're requesting an Edge Config scoped to a team, add `?teamId=` to the end of the endpoint, pasting [the Vercel Team's ID](/docs/accounts#find-your-team-id) after the `=` symbol.

Your URL should look like this:

endpoint

```
'https://api.vercel.com/v1/edge-config/your_edge_config_id_here/items?teamId=your_team_id_here';
```

Your request body should be a JSON object containing an `"items"` array. The `"items"` array must contain objects that describe the change you want to make to the Edge Config. The following table outlines valid keys and values for these objects:

| Property | Description | Valid values |
| --- | --- | --- |
| `"operation"` | The change you want to make to your Edge Config. | `"create"`, `"update"`, `"upsert"`, `"delete"` |
| `"key"` | The name of the key you want to add to or update within your Edge Config. | String of alphanumeric characters, "\_" and "-" only. Up to 256 characters. |
| `"value"` | The value you want to assign to the key. | Strings, JSON objects, `null` objects, Numbers and arrays of the previous four types |

The following example demonstrates a request body that creates an `"example_key_1"` key with a value of `"example_value_1"`, then updates the `"example_key_2"` key with a new value of `"new_value"`:

body

```
{
  "items": [
    {
      "operation": "create",
      "key": "example_key_1",
      "value": "example_value_1"
    },
    {
      "operation": "update",
      "key": "example_key_2",
      "value": "new_value"
    }
  ]
}
```

The following is an API call that sends the above request body to your Edge Config:

cURLfetch

cURL

```
curl -X 'PATCH' 'https://api.vercel.com/v1/edge-config/your_edge_config_id_here/items' \
     -H 'Authorization: Bearer your_vercel_api_token_here' \
     -H 'Content-Type: application/json' \
     -d $'{ "items": [ { "operation": "create", "key": "example_key_1", "value": "example_value_1" }, { "operation": "update", "key": "example_key_2", "value": "new_value" } ] }'
```

fetch

```
try {
  const updateEdgeConfig = await fetch(
    'https://api.vercel.com/v1/edge-config/your_edge_config_id_here/items',
    {
      method: 'PATCH',
      headers: {
        Authorization: `Bearer ${your_vercel_api_token_here}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        items: [
          {
            operation: 'create',
            key: 'example_key_1',
            value: 'example_value_1',
          },
          {
            operation: 'update',
            key: 'example_key_2',
            value: 'new_value',
          },
        ],
      }),
    },
  );
  const result = await updateEdgeConfig.json();
  console.log(result);
} catch (error) {
  console.log(error);
}
```

Successful requests will receive a response of `{"status":"ok"}`.

### [Failing Edge Config `PATCH` requests](#failing-edge-config-patch-requests)

If only one of the operations in the `"items"` array of your `PATCH` request body fails, the entire request will fail. Failed requests will receive a response JSON object containing an `"error"` property with an object that contains information about why the request failed.

For example:

error

```
{
  "error": {
    "code": "forbidden",
    "message": "The request is missing an authentication token",
    "missingToken": true
  }
}
```

## [Read all items](#read-all-items)

Reading items from your Edge Configs with the Vercel REST API is not recommended. Instead, you should [use the SDK](/docs/edge-config/edge-config-sdk#read-multiple-values) or fetch Edge Config data with [the Edge Config endpoint](#make-requests-to-the-edge-config-endpoint).

However, if you must read your Edge Config with the API, you can do so by making a `GET` request to the `edge-config` endpoint.

Your URL should look like this:

endpoint

```
'https://api.vercel.com/v1/edge-config/your_edge_config_id_here/items?teamId=your_team_id_here';
```

The following is an example of a request that fetches an Edge Config's items with the Vercel REST API:

cURLfetch

request

```
curl "https://api.vercel.com/v1/edge-config/your_edge_config_id_here/items?teamId=your_team_id_here" \
     -H 'Authorization: Bearer your_vercel_api_token_here'
```

fetch

```
try {
  const readItems = await fetch(
    'https://api.vercel.com/v1/edge-config/your_edge_config_id_here/items?teamId=your_team_id_here',
    {
      method: 'GET',
      headers: {
        Authorization: `Bearer ${your_vercel_api_token_here}`,
      },
    },
  );
  const result = await readItems.json();
  console.log(result);
} catch (error) {
  console.log(error);
}
```

## [Read metadata](#read-metadata)

You can read your Edge Config's metadata (but not its key-value pair contents) by making a `GET` request to the `edge-config` API endpoint. Append the Edge Config's id to the endpoint as a path, as demonstrated below. If the Edge Config is associated with a Team, add the `teamId` query param to the end.

The following is an example `GET` request that fetches metadata about an Edge Config associated with a Vercel Team.

cURLfetch

request

```
curl "https://api.vercel.com/v1/edge-config/your_edge_config_id_here?teamId=your_team_id_here" \
     -H 'Authorization: Bearer your_vercel_api_token_here'
```

fetch

```
try {
  const readMetadata = await fetch(
    'https://api.vercel.com/v1/edge-config/your_edge_config_id_here?teamId=your_team_id_here',
    {
      method: 'GET',
      headers: {
        Authorization: `Bearer ${your_vercel_api_token_here}`,
      },
    },
  );
  const result = await readMetadata.json();
  console.log(result);
} catch (error) {
  console.log(error);
}
```

If the Edge Config exists, the response will be the same JSON object you receive when [creating your Edge Config with the Vercel REST API](#create-an-edge-config):

response

```
{
  "createdAt": 1234567890123,
  "updatedAt": 1234567890123,
  "slug": "your_edge_config_slug_here",
  "id": "your_edge_config_id_here",
  "digest": "abc123efg456hij789",
  "sizeInBytes": 2,
  "itemCount": 0,
  "ownerId": "your_id_here"
}
```

## [List all Edge Configs](#list-all-edge-configs)

You can list all of your Edge Configs in a specific Hobby team or team with a `GET` request to the `edge-config` API endpoint. For example:

cURLfetch

request

```
curl "https://api.vercel.com/v1/edge-config?teamId=your_team_id_here" \
     -H 'Authorization: Bearer your_vercel_api_token_here'
```

fetch

```
try {
  const listItems = await fetch(
    'https://api.vercel.com/v1/edge-config?teamId=your_team_id_here',
    {
      method: 'GET',
      headers: {
        Authorization: `Bearer ${your_vercel_api_token_here}`,
      },
    },
  );
  const result = await listItems.json();
  console.log(result);
} catch (error) {
  console.log(error);
}
```

The response should be similar to this:

response

```
[
  {
    "slug": "example_config_1",
    "itemCount": 0,
    "createdAt": 1234567890123,
    "updatedAt": 1234567890123,
    "id": "your_edge_config_id_here",
    "digest": "abc123efg456hij789",
    "sizeInBytes": 2,
    "ownerId": "your_id_here"
  },
  {
    "slug": "example_config_2",
    "itemCount": 0,
    "createdAt": 0123456789012,
    "updatedAt": 0123456789012,
    "id": "your_edge_config_id_here",
    "digest": "123efg456hij789abc",
    "sizeInBytes": 2,
    "ownerId": "your_id_here"
  }
]
```

## [Make requests to the Edge Config endpoint](#make-requests-to-the-edge-config-endpoint)

We recommend storing your [connection string](/docs/edge-config/using-edge-config#using-a-connection-string) as an environment variable in your project and [using our SDK](/docs/edge-config/edge-config-sdk) to read Edge Config data. However, you can make requests to the Edge Config endpoint to read your Edge Config's data as well.

To do so, create an [Edge Config read access token](/docs/edge-config/using-edge-config#creating-a-read-access-token), which will be used to authenticate requests to the Edge Config endpoint.

The Edge Config endpoint used in the connection string is distinct from a Vercel REST API endpoint. Its root is `https://edge-config.vercel.com`. Making requests to the Edge Config endpoint allows you to take advantage of the optimizations that make Vercel's Edge Config reads hundreds of milliseconds faster than alternative options at the edge.

### [Request all items](#request-all-items)

To read all of your Edge Config's items, send a `GET` request to the appropriate edge config endpoint by adding your Edge Config's ID and Edge Config read access token in the appropriate places in the below URL:

cURLfetch

cURL

```
curl 'https://edge-config.vercel.com/your_edge_config_id_here/items?token=your_edge_config_read_access_token_here'
```

fetch

```
try {
  const readAllEdgeConfigItems = await fetch(
    'https://edge-config.vercel.com/your_edge_config_id_here/items?token=your_edge_config_read_access_token_here',
  );
  const result = await readAllEdgeConfigItems.json();
  console.log(result);
} catch (error) {
  console.log(error);
}
```

You can also send your Edge Config read access token in an Authorization header rather than as a query param.

cURLfetch

request

```
curl "https://edge-config.vercel.com/your_edge_config_id_here/items" \
     -H 'Authorization: Bearer your_edge_config_read_access_token_here'
```

fetch

```
try {
  const readAllWithAuth = await fetch(
    'https://edge-config.vercel.com/your_edge_config_id_here/items',
    {
      method: 'GET',
      headers: {
        Authorization: `Bearer ${your_edge_config_read_access_token_here}`,
      },
    },
  );
  const result = await readAllWithAuth.json();
  console.log(result);
} catch (error) {
  console.log(error);
}
```

The response will be a JSON object containing all key-value pairs in the Edge Config. For example:

response

```
{
  "example_key_1": "example_value_1",
  "example_key_2": "example_value_2",
  "example_key_3": "example_value_3"
}
```

### [Request a single item](#request-a-single-item)

To request a single item, you can use the `/item` path instead of `/items`, then add the key of the item you want as the final path as shown below:

cURLfetch

request

```
curl "https://edge-config.vercel.com/your_edge_config_id_here/item/example_key_1?token=your_edge_config_read_access_token_here" \
```

fetch

```
try {
  const readSingle = await fetch(
    'https://edge-config.vercel.com/your_edge_config_id_here/item/example_key_1?token=your_edge_config_read_access_token_here',
  );
  const result = await readSingle.json();
  console.log(result);
} catch (error) {
  console.log(error);
}
```

You can also send your Edge Config read access token in an Authorization header rather than as a query param.

cURLfetch

request

```
curl -X 'https://edge-config.vercel.com/your_edge_config_id_here/item/example_key_1' \
     -H 'Authorization: Bearer your_edge_config_read_access_token_here'
```

fetch

```
try {
  const readSingleWithAuth = await fetch(
    'https://edge-config.vercel.com/your_edge_config_id_here/item/example_key_1',
    {
      method: 'GET',
      headers: {
        Authorization: `Bearer ${your_edge_config_read_access_token_here}`,
      },
    },
  );
  const result = await readSingleWithAuth.json();
  console.log(result);
} catch (error) {
  console.log(error);
}
```

The response will be the raw value at the specified key. For example, if `example_key_1` has a string value of `"example_value"`, the response will be:

response

```
"example_value"
```

### [Request the digest](#request-the-digest)

When you create an Edge Config, a hash string called a digest is generated and attached to it. This digest is replaced with a new hash string whenever you update your config. You can check this digest to verify whether your Edge Config has properly updated, and confirm which version of the Config you're working with.

To fetch an Edge Config's digest, send a `GET` request to your edge config endpoint, as shown below:

cURLfetch

request

```
curl "https://edge-config.vercel.com/your_edge_config_id_here/digest?teamId=your_team_id_here&token=your_edge_config_read_access_token_here"
```

fetch

```
try {
  const readDigest = await fetch(
    'https://edge-config.vercel.com/your_edge_config_id_here/digest?teamId=your_team_id_here&token=your_edge_config_read_access_token_here',
  );
  const result = await readDigest.json();
  console.log(result);
} catch (error) {
  console.log(error);
}
```

You can also send the Edge Config read access token in the `Authorization` header of your request using the `Bearer token` format:

cURLfetch

request

```
curl  -X 'GET' 'https://edge-config.vercel.com/your_edge_config_id_here/digest?teamId=your_team_id_here' \
      -H 'Authorization: Bearer your_edge_config_read_access_token_here
```

fetch

```
try {
  const readDigestWithAuth = await fetch(
    'https://edge-config.vercel.com/your_edge_config_id_here/digest?teamId=your_team_id_here',
    {
      method: 'GET',
      headers: {
        Authorization: `Bearer ${your_edge_config_read_access_token_here}`,
      },
    },
  );
  const result = await readDigestWithAuth.json();
  console.log(result);
} catch (error) {
  console.log(error);
}
```

## [Up Next](#up-next)

[

#### Limits

Data size and request limits based on account plans

](/docs/edge-config/edge-config-limits)

--------------------------------------------------------------------------------
title: "Edit Mode"
description: "Discover how Vercel's Edit Mode enhances content management for headless CMSs, enabling real-time editing, and seamless collaboration."
last_updated: "null"
source: "https://vercel.com/docs/edit-mode"
--------------------------------------------------------------------------------

# Edit Mode

Copy page

Ask AI about this page

Last updated March 12, 2025

Edit Mode is available on [Enterprise](/docs/plans/enterprise) and [Pro](/docs/plans/pro) plans

Content editing in CMSs usually occurs separately from the website's layout and design. This separation makes it hard for authors to visualize their changes. Edit Mode allows authors to edit content within the website's context, offering a clearer understanding of the impact on design and user experience. The ability to jump from content to the editing interface further enhances this experience.

## [Accessing Edit Mode](#accessing-edit-mode)

To access Edit Mode:

1.  Ensure you're logged into the [Vercel Toolbar](/docs/vercel-toolbar) with your Vercel account.
2.  Navigate to a page with editable content. The Edit Mode option will only appear in the [Vercel Toolbar](/docs/vercel-toolbar) menu when there are elements on the page matched to fields in the CMS.
3.  Select the Edit Mode option in the toolbar menu. This will highlight the editable fields as [Content Links](/docs/edit-mode#content-link), which turn blue as you hover near them.

## [Content Link](#content-link)

Content Link is available on [Enterprise](/docs/plans/enterprise) and [Pro](/docs/plans/pro) plans

Content Link enables you to edit content on websites using headless CMSs by providing links on elements that match a content model in the CMS. This real-time content visualization allows collaborators to make changes without needing a developer's assistance.

You can enable Content Link on a preview deployment by selecting Edit Mode in the [Vercel Toolbar](/docs/vercel-toolbar) menu.

The corresponding model in the CMS determines an editable field. You can hover over an element to display a link in the top-right corner of the element and then select the link to open the related CMS field for editing.

You don't need any additional configuration or code changes on the page to use this feature.

The following CMS integrations support Content Link:

*   [
    
    Contentful
    
    ](https://www.contentful.com/developers/docs/tools/vercel/content-source-maps-with-vercel/)
*   [
    
    Sanity
    
    ](https://www.sanity.io/docs/vercel-visual-editing)
*   [
    
    Builder
    
    ](https://www.builder.io/c/docs/vercel-visual-editing)
*   [
    
    TinaCMS
    
    ](https://tina.io/docs/contextual-editing/overview/)
*   [
    
    DatoCMS
    
    ](https://www.datocms.com/docs/visual-editing/how-to-use-visual-editing)
*   [
    
    Payload
    
    ](https://payloadcms.com/docs/integrations/vercel-visual-editing)
*   [
    
    Uniform
    
    ](https://www.uniform.dev/blogs/visual-editing-with-vercel-uniform)
*   [
    
    Strapi
    
    ](https://strapi.io/blog/announcing-visual-editing-for-strapi-powered-by-vercel)

See the [CMS integration documentation](/docs/integrations/cms) for information on how to use Content Link with your chosen CMS.

--------------------------------------------------------------------------------
title: "Encryption"
description: "Learn how Vercel encrypts data in transit and at rest."
last_updated: "null"
source: "https://vercel.com/docs/encryption"
--------------------------------------------------------------------------------

# Encryption

Copy page

Ask AI about this page

Last updated September 24, 2025

Out of the box, every deployment on Vercel is served over an HTTPS connection. The [SSL](https://en.wikipedia.org/wiki/Transport_Layer_Security) certificates for these unique URLs are automatically generated free of charge.

Any HTTP requests to your deployment are automatically forwarded to HTTPS using the `308` status code:

```
HTTP/1.1 308 Moved Permanently
Content-Type: text/plain
Location: https://<your-deployment-host>
```

An example showing how all `HTTP` requests are forwarded to `HTTPS`.

Enabling HTTPS redirection for deployments is considered an industry standard, and therefore it is not possible to disable it. This ensures that web content is always served over a secure connection, which helps protect users' data and privacy.

If the client that is issuing requests to your deployment wants to establish a WebSocket connection, please ensure it is connecting using HTTPS. directly, as the WSS protocol does not support redirections.

## [Supported TLS versions](#supported-tls-versions)

​Vercel supports TLS version [1.2](https://en.wikipedia.org/wiki/Transport_Layer_Security#TLS_1.2) and TLS version [1.3](https://en.wikipedia.org/wiki/Transport_Layer_Security#TLS_1.3).

## [TLS resumption](#tls-resumption)

​Vercel supports both Session Identifiers and Session Tickets as methods for [resuming a TLS connection](https://hpbn.co/transport-layer-security-tls/#tls-session-resumption). This can significantly improve Time To First Byte for second time visitors.

## [OCSP stapling](#ocsp-stapling)

To ensure clients can validate TLS certificates as quickly as possible, we [staple an OCSP response](https://en.wikipedia.org/wiki/OCSP_stapling) allowing them to skip a network request to check for revocation, which improves TTFB for first-time visitors.

## [Supported ciphers](#supported-ciphers)

In order to ensure the integrity of the data received and sent by any deployment running on the Vercel platform, we only support strong ciphers with [forward secrecy](https://en.wikipedia.org/wiki/Forward_secrecy).

The following cipher algorithms are supported:

*   `TLS_AES_128_GCM_SHA256` (TLS 1.3)
*   `TLS_AES_256_GCM_SHA384` (TLS 1.3)
*   `TLS_CHACHA20_POLY1305_SHA256` (TLS 1.3)
*   `ECDHE-ECDSA-AES128-GCM-SHA256` (TLS 1.2)
*   `ECDHE-RSA-AES128-GCM-SHA256` (TLS 1.2)
*   `ECDHE-ECDSA-AES256-GCM-SHA384` (TLS 1.2)
*   `ECDHE-RSA-AES256-GCM-SHA384` (TLS 1.2)
*   `ECDHE-ECDSA-CHACHA20-POLY1305` (TLS 1.2)
*   `ECDHE-RSA-CHACHA20-POLY1305` (TLS 1.2)
*   `DHE-RSA-AES256-GCM-SHA384` (TLS 1.2)

This is the [recommended configuration from Mozilla](https://wiki.mozilla.org/Security/Server_Side_TLS#Intermediate_compatibility_.28recommended.29).

## [Support for HSTS](#support-for-hsts)

The `.vercel.app` domain (and therefore all of its sub domains, which are the unique URLs set when creating a deployment) support [HSTS](https://developer.mozilla.org/docs/Web/HTTP/Headers/Strict-Transport-Security) automatically and are preloaded.

```
Strict-Transport-Security: max-age=63072000; includeSubDomains; preload;
```

The default `Strict-Transport-Security` header for \*.vercel.app

Custom domains use HSTS, but only for the particular subdomain.

```
Strict-Transport-Security: max-age=63072000;
```

The default `Strict-Transport-Security` header for custom domains

You can modify the `Strict-Transport-Security` header by configuring [custom response headers](/docs/headers/cache-control-headers#custom-response-headers) in your project.

Theoretically, you could set the `max-age` parameter to a different value (it indicates how long the client should remember that your site is only accessible over HTTPS), but since we do not allow connections made over HTTP, there is no point in setting it to a shorter value, as the client can just remember it forever.

You can test whether your site qualifies for HSTS Preloading [here](https://hstspreload.org/). It also allows submitting the domain to Google Chrome's hardcoded HSTS list. Making it onto that list means your site will become even faster, as it is always accessed over HTTPS right away, instead of the browser following the redirection issued by our Network layer.

## [How certificates are handled](#how-certificates-are-handled)

The unique URLs generated when creating a deployment are handled using a wildcard certificate issued for the `.vercel.app` domain. The Vercel platform generates wildcard certificates using [LetsEncrypt](https://letsencrypt.org/) and keeps them updated automatically.

When custom certificates are generated using `vercel certs issue`, however, their keys are placed in our database and [encrypted at rest](https://en.wikipedia.org/wiki/Data_at_rest#Encryption) within the Network layer.

Then, once a hostname is requested, the certificate and key are read from the database and used for establishing the secure connection. In addition, both are cached in memory for optimal SSL termination performance.

## [Full specification](#full-specification)

Any features of the encryption mechanism that were left uncovered are documented on [SSL Labs](https://www.ssllabs.com/ssltest/analyze.html?d=vercel.com). You only need to make sure to select any IP address of your choice (it does not matter which one you pick – the results are the same for all).

--------------------------------------------------------------------------------
title: "Environment variables"
description: "Learn more about environment variables on Vercel."
last_updated: "null"
source: "https://vercel.com/docs/environment-variables"
--------------------------------------------------------------------------------

# Environment variables

Copy page

Ask AI about this page

Last updated September 24, 2025

Environment variables are key-value pairs configured outside your source code so that each value can change depending on the [Environment](/docs/deployments/environments). These values are encrypted at rest and visible to any user that has access to the [project](/docs/projects/overview). It is safe to use both non-sensitive and sensitive data, such as tokens.

Your source code can read these values to change behavior during the [Build Step](/docs/deployments/configure-a-build) or during [Function](/docs/functions) execution.

Any change you make to environment variables are not applied to previous deployments, they only apply to new deployments.

## [Creating environment variables](#creating-environment-variables)

Environment variables can either be declared at the team or project level. When declared at the team level, they are available to all projects within the team. When declared at the project level, they are only available to that project.

To learn how to create and manage environment variables, see [Managing environment variables](/docs/environment-variables/managing-environment-variables).

## [Environment Variable size](#environment-variable-size)

Developers on all plans using the runtimes stated below can use a total of 64 KB in Environments Variables per-Deployment on Vercel. This [limit](/docs/limits#environment-variables) is for all variables combined, and so no single variable can be larger than 64 KB. The total size includes any variables configured through the dashboard or the [CLI](/docs/cli).

With support for 64 KB of environment variables, you can add large values for authentication tokens, JWTs, or certificates.

Deployments using the following runtimes can support environment variables up to 64 KB:

*   Node.js
*   Python
*   Ruby
*   Go
*   [PHP Community Runtime](https://github.com/vercel-community/php)

Vercel also provides support for custom runtimes, through the Build Output API. For information on creating custom runtime support, see the following guides:

*   [Guides for runtime builders](https://github.com/vercel/vercel/blob/main/DEVELOPING_A_RUNTIME.md#supporting-large-environment)
*   [Build Output API documentation](/docs/build-output-api/v3/primitives#base-config)

While Vercel allows environment variables up to a total of 64KB in size, Edge Functions and Middleware using the `edge` runtime are limited to 5KB per Environment Variable.

## [Environments](#environments)

For each Environment Variable, you can select one or more Environments to apply the Variable to:

| Environment | Description |
| --- | --- |
| [Production](/docs/deployments/environments#production-environment) | When selected, the Environment Variable will be applied to your next Production Deployment. To create a Production Deployment, push a commit to the [Production Branch](/docs/git#production-branch) (usually `main`) or run `vercel --prod`. |
| [Preview](#preview-environment-variables) | The Environment Variable is applied to your next Preview Deployment. Preview Deployments are created when you push to a branch that is not the [Production Branch](/docs/git#production-branch) or run `vercel`. |
| [Custom environments](/docs/deployments/environments#custom-environments) | With custom environments you can choose to [import environment variables](/docs/custom-environments#import-variables-from-another-environment) from another environment and [detach](/docs/custom-environments#detaching-an-environment-variable) when you need to update the environment variable for your custom environment |
| [Development](#development-environment-variables) | The Environment Variable is used when running your project locally with `vercel dev` or your preferred development command. To download Development Environment Variables, run [`vercel env pull`](/docs/cli/env). |

### [Preview environment variables](#preview-environment-variables)

You need Vercel CLI version 22.0.0 or higher to use the features described in this section.

Preview environment variables are applied to deployments from any Git branch that does not match the [Production Branch](/docs/git#production-branch). When you add a preview environment variable, you can choose to apply to all non-production branches or you can select a specific branch.

![Adding an Environment Variable](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fprojects%2Fenvironment-variables%2Fenv-var-section-light.png&w=1920&q=75)![Adding an Environment Variable](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fprojects%2Fenvironment-variables%2Fenv-var-section-dark.png&w=1920&q=75)

Adding an Environment Variable

Any branch-specific variables will override other preview environment variables with the same name. This means you don't need to replicate all your existing preview environment variables for each branch – you only need to add the values you wish to override.

### [Development environment variables](#development-environment-variables)

You need Vercel CLI version 21.0.1 or higher to use the features described in this section.

Environment variables for local development are defined in the `.env.local` file. This is a plain text file that contains `key=value` pairs of environment variables, that you can manually create in your project's root directory to define specific variables.

You can use the `vercel env pull` command to automatically create and populate the `.env` file (which serves the same purpose as `.env.local`) with the environment variables from your Vercel project:

vercel env pull
Downloading Development Environment Variables for Project my-lovely-project
✅ Created .env file \[510ms\]

This command creates a `.env` file in your project's current directory with the environment variables from your Vercel project's Development environment.

If you're using [`vercel dev`](/docs/cli/dev), there's no need to run `vercel env pull`, as `vercel dev` automatically downloads the Development Environment Variables into memory. For more information on the `vercel env` command, see the [CLI](/docs/cli/env) docs.

For more information, see [Environment variables for local development](/docs/deployments/local-env#environment-variables-for-local-development).

## [Integration environment variables](#integration-environment-variables)

[Integrations](/docs/integrations) can automatically add environment variables to your Project Settings. In that case, the Integration that added the Variable will be displayed in your project settings:

![An Environment Variable added by the MongoDB Integration.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fprojects%2Fenvironment-variables%2Fintegration-env-variable-light.png&w=1920&q=75)![An Environment Variable added by the MongoDB Integration.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fprojects%2Fenvironment-variables%2Fintegration-env-variable-dark.png&w=1920&q=75)

An Environment Variable added by the MongoDB Integration.

--------------------------------------------------------------------------------
title: "Framework environment variables"
description: "Framework environment variables are automatically populated by the Vercel, based on your project's framework."
last_updated: "null"
source: "https://vercel.com/docs/environment-variables/framework-environment-variables"
--------------------------------------------------------------------------------


---

**Navigation:** [← Previous](./06-trusted-ips.md) | [Index](./index.md) | [Next →](./08-framework-environment-variables.md)
