**Navigation:** [← Previous](./01-ai-vectors.md) | [Index](./index.md) | [Next →](./03-storage-helper-functions.md)

# Metrics



In addition to the reports and charts built in to the Supabase dashboard, each project hosted on the Supabase platform comes with a [Prometheus](https://prometheus.io/)-compatible metrics endpoint, updated every minute, which can be used to gather insight into the health and status of your project.

You can use this endpoint to ingest data into your own monitoring and alerting infrastructure, as long as it is capable of scraping Prometheus-compatible endpoints, in order to set up custom rules beyond those supported by the Supabase dashboard.

<Admonition type="note">
  The endpoint discussed in this article is in beta, and the metrics returned by it might evolve or be changed in the future to increase its utility.
</Admonition>

<Admonition type="note">
  The endpoint discussed in this article is not available on self-hosted.
</Admonition>



## Accessing the metrics endpoint

Your project's metrics endpoint is accessible at `https://<project-ref>.supabase.co/customer/v1/privileged/metrics`.

Access to the endpoint is secured via HTTP Basic Auth:

*   username: `service_role`
*   password: the `service_role` API key or any other secret API key, get these from [Supabase dashboard](/dashboard/project/_/settings/api-keys)

You can also retrieve your service role key programmatically using the Management API:

```bash

# Get your access token from https://supabase.com/dashboard/account/tokens
export SUPABASE_ACCESS_TOKEN="your-access-token"
export PROJECT_REF="your-project-ref"


# Get project API keys including service_role key
curl -H "Authorization: Bearer $SUPABASE_ACCESS_TOKEN" \
  "https://api.supabase.com/v1/projects/$PROJECT_REF/api-keys?reveal=true"
```

<ProjectConfigVariables variable="url" />

```shell
curl <project-url>/customer/v1/privileged/metrics \
    --user 'service_role:sb_secret_...'
```

```shell
curl <project-url>/customer/v1/privileged/metrics \
    --user 'service_role:<service-role-jwt>'
```



## Supabase Grafana

The pre-configured Supabase Grafana Dashboard is an advanced version of the [Dashboard's Database Reports](/dashboard/project/_/reports/database). It visualizes over 200 database performance and health metrics.

![Supabase Grafana](/docs/img/guides/platform/supabase-grafana-prometheus.png)

Instructions are included in the README for deploying the repository using docker.



## Using the metrics endpoint in production

To set up monitoring for your project, you will need two things:

1.  A datastore - a place to store the metrics coming from your Supabase project over time
2.  A dashboard - a place to visualize the state of your Supabase project for a defined period


### Setting up a metrics datastore

One of the more well-known options is [Prometheus](https://prometheus.io/docs/introduction/overview/) and it is the tool used in this guide.

You can [self-host](https://prometheus.io/docs/prometheus/latest/installation/) Prometheus or choose a managed service to store your metrics. Some of the providers offering managed Prometheus are:

*   [Digital Ocean](https://marketplace.digitalocean.com/apps/prometheus)
*   [AWS](https://aws.amazon.com/prometheus/)
*   [Grafana Cloud](https://grafana.com/products/cloud/metrics/)

Follow the guides for the deployment option you choose


#### Adding a scrape job to Prometheus

For Prometheus, modify your `prometheus.yaml` file to add a Supabase job, and set the `metrics_path`, `scheme`, `basic_auth` and `targets` parameters. For example:

```yaml
scrape_configs:
  - job_name: "MySupabaseJob"
    metrics_path: "/customer/v1/privileged/metrics"
    scheme: https
    basic_auth:
      username: "service_role"
      password: "<your service_role JWT>"
    static_configs:
      - targets: [
        "<your Supabase Project ID>.supabase.co:443"
          ]
        labels:
          group: "MyGroupLabel"
```


### Setting up a dashboard

For this guide, we will be using [Grafana](https://grafana.com/docs/grafana/latest/introduction/).

You can [self-host](https://grafana.com/docs/grafana/latest/setup-grafana/installation/) Grafana or many providers offer managed Grafana, some of which are listed below:

*   [DigitalOcean](https://marketplace.digitalocean.com/apps/grafana)
*   [AWS](https://aws.amazon.com/grafana/)
*   [Grafana Cloud](https://grafana.com/grafana/)

Follow the guides of the provider you choose to get Grafana up and running.


### Adding a data source to Grafana

In the left-hand menu, select `Data sources` and click `Add new data source`.

Select `Prometheus` and enter the connection details for the Prometheus instance you have set up.

Under **Interval behavior**, set the **scraping interval** to 60s and test the data source. Once it has passed, save it.


### Adding the Supabase dashboard

In the left-hand menu, select `Dashboards` and click `New`. From the drop-down, select `Import`.

Copy the raw file from our [supabase-grafana](https://raw.githubusercontent.com/supabase/supabase-grafana/refs/heads/main/grafana/dashboard.json) repository and paste it (or upload the file).

Click `Load` and the dashboard will load from the project specified in your Prometheus job.


### Monitoring your project

You can configure alerts from Prometheus or Grafana. The `supabase-grafana` repository has a selection of [example alerts](https://github.com/supabase/supabase-grafana/blob/main/docs/example-alerts.md) that can be configured.

<Admonition type="caution">
  Grafana Cloud has an unofficial integration for scraping Supabase metrics. See their [docs](https://grafana.com/docs/grafana-cloud/monitor-infrastructure/integrations/integration-reference/integration-supabase/) for instructions on how to configure it but note that it is not full-featured nor is it supported
  by Supabase.
</Admonition>



# Reports



Supabase Reports provide comprehensive observability for your project through dedicated monitoring dashboards that visualize key metrics across your database, auth, storage, realtime, and API systems. Each report offers self-debugging tools to gain actionable insights for optimizing performance and troubleshooting issues.

<Admonition type="note">
  Reports are only available for projects hosted on the Supabase Cloud platform and are not available for self-hosted instances.
</Admonition>



## Using reports

Reports can be filtered by time range to focus your analysis on specific periods. Available time ranges are gated by your organization's plan, with higher-tier plans providing access to longer historical periods.

| Time Range      | Free | Pro | Team | Enterprise |
| --------------- | ---- | --- | ---- | ---------- |
| Last 10 minutes | ✅    | ✅   | ✅    | ✅          |
| Last 30 minutes | ✅    | ✅   | ✅    | ✅          |
| Last 60 minutes | ✅    | ✅   | ✅    | ✅          |
| Last 3 hours    | ✅    | ✅   | ✅    | ✅          |
| Last 24 hours   | ✅    | ✅   | ✅    | ✅          |
| Last 7 days     | ❌    | ✅   | ✅    | ✅          |
| Last 14 days    | ❌    | ❌   | ✅    | ✅          |
| Last 28 days    | ❌    | ❌   | ✅    | ✅          |

***



## Database

The Database report provides the most comprehensive view into your Postgres instance's health and performance characteristics. These charts help you identify performance bottlenecks, resource constraints, and optimization opportunities at a glance.

The following charts are available for Free and Pro plans:

| Chart                        | Available Plans | Description                                  | Key Insights                                  |
| ---------------------------- | --------------- | -------------------------------------------- | --------------------------------------------- |
| Memory usage                 | Free, Pro       | RAM usage percentage by the database         | Memory pressure and resource utilization      |
| CPU usage                    | Free, Pro       | Average CPU usage percentage                 | CPU-intensive query identification            |
| Disk IOPS                    | Free, Pro       | Read/write operations per second with limits | IO bottleneck detection and workload analysis |
| Database connections         | Free, Pro       | Number of pooler connections to the database | Connection pool monitoring                    |
| Shared Pooler connections    | All             | Client connections to the shared pooler      | Shared pooler usage patterns                  |
| Dedicated Pooler connections | All             | Client connections to PgBouncer              | Dedicated pooler connection monitoring        |

{/* supa-mdx-lint-disable-next-line Rule001HeadingCase */}


### Advanced Telemetry

The following charts provide a more advanced and detailed view of your database performance and are available only for Teams and Enterprise plans.


### Memory usage

<Image
  alt="Memory usage chart"
  zoomable
  src={{
    dark: '/docs/img/database/reports/memory-usage-chart-dark.png',
    light: '/docs/img/database/reports/memory-usage-chart-light.png',
  }}
/>

| Component           | Description                                            |
| ------------------- | ------------------------------------------------------ |
| **Used**            | RAM actively used by Postgres and the operating system |
| **Cache + buffers** | Memory used for page cache and Postgres buffers        |
| **Free**            | Available unallocated memory                           |

How it helps debug issues:

| Issue                          | Description                                      |
| ------------------------------ | ------------------------------------------------ |
| Memory pressure detection      | Identify when free memory is consistently low    |
| Cache effectiveness monitoring | Monitor cache performance for query optimization |
| Memory leak detection          | Detect inefficient memory usage patterns         |

Actions you can take:

| Action                                                                      | Description                                    |
| --------------------------------------------------------------------------- | ---------------------------------------------- |
| [Upgrade compute size](/docs/guides/platform/compute-and-disk#compute-size) | Increase available memory resources            |
| Optimize queries                                                            | Reduce memory consumption of expensive queries |
| Tune Postgres configuration                                                 | Improve memory management settings             |
| Implement application caching                                               | Add query result caching to reduce memory load |


### CPU usage

<Image
  alt="CPU usage chart"
  zoomable
  src={{
    dark: '/docs/img/database/reports/cpu-usage-chart-dark.png',
    light: '/docs/img/database/reports/cpu-usage-chart-light.png',
  }}
/>

| Category   | Description                                      |
| ---------- | ------------------------------------------------ |
| **System** | CPU time for kernel operations                   |
| **User**   | CPU time for database queries and user processes |
| **IOWait** | CPU time waiting for disk/network IO             |
| **IRQs**   | CPU time handling interrupts                     |
| **Other**  | CPU time for miscellaneous tasks                 |

How it helps debug issues:

| Issue                              | Description                                        |
| ---------------------------------- | -------------------------------------------------- |
| CPU-intensive query identification | Identify expensive queries when User CPU is high   |
| IO bottleneck detection            | Detect disk/network issues when IOWait is elevated |
| System overhead monitoring         | Monitor resource contention and kernel overhead    |

Actions you can take:

| Action                                                         | Description                                                                 |
| -------------------------------------------------------------- | --------------------------------------------------------------------------- |
| Optimize CPU-intensive queries                                 | Target queries causing high User CPU usage                                  |
| Address IO bottlenecks                                         | Resolve disk/network issues when IOWait is high                             |
| [Upgrade compute size](/docs/guides/platform/compute-and-disk) | Increase available CPU capacity                                             |
| Implement proper indexing                                      | Use [query optimization](/docs/guides/database/postgres/indexes) techniques |


### Disk input/output operations per second (IOPS)

<Image
  alt="Disk IOPS chart"
  zoomable
  src={{
    dark: '/docs/img/database/reports/disk-iops-chart-dark.png',
    light: '/docs/img/database/reports/disk-iops-chart-light.png',
  }}
/>

This chart displays read and write IOPS with a reference line showing your compute size's maximum IOPS capacity.

How it helps debug issues:

| Issue                             | Description                                                      |
| --------------------------------- | ---------------------------------------------------------------- |
| Disk IO bottleneck identification | Identify when disk IO becomes a performance constraint           |
| Workload pattern analysis         | Distinguish between read-heavy vs write-heavy operations         |
| Performance correlation           | Spot disk activity spikes that correlate with performance issues |

Actions you can take:

| Action                                                         | Description                                               |
| -------------------------------------------------------------- | --------------------------------------------------------- |
| Optimize indexing                                              | Reduce high read IOPS through better query indexing       |
| Consider read replicas                                         | Distribute read-heavy workloads across multiple instances |
| Batch write operations                                         | Reduce write IOPS by grouping database writes             |
| [Upgrade compute size](/docs/guides/platform/compute-and-disk) | Increase IOPS limits with larger compute instances        |


### Disk IO Usage

<Image
  alt="Disk IO Usage chart"
  zoomable
  src={{
    dark: '/docs/img/database/reports/disk-io-chart-dark.png',
    light: '/docs/img/database/reports/disk-io-chart-light.png',
  }}
/>

This chart displays the percentage of your allocated IOPS (Input/Output Operations Per Second) currently being used.

How it helps debug issues:

| Issue                       | Description                                                 |
| --------------------------- | ----------------------------------------------------------- |
| IOPS limit monitoring       | Identify when approaching your allocated IOPS capacity      |
| Performance correlation     | Correlate high IO usage with application performance issues |
| Operation impact assessment | Monitor how database operations affect disk performance     |

Actions you can take:

| Action                                                         | Description                                        |
| -------------------------------------------------------------- | -------------------------------------------------- |
| Optimize disk-intensive queries                                | Reduce queries that perform excessive reads/writes |
| Add strategic indexes                                          | Reduce sequential scans with appropriate indexing  |
| [Upgrade compute size](/docs/guides/platform/compute-and-disk) | Increase IOPS limits with larger compute instances |
| Review database design                                         | Optimize schema and query patterns for efficiency  |


### Disk size

<Image
  alt="Disk Size chart"
  zoomable
  src={{
    dark: '/docs/img/database/reports/disk-size-chart-dark.png',
    light: '/docs/img/database/reports/disk-size-chart-light.png',
  }}
/>

| Component    | Description                                               |
| ------------ | --------------------------------------------------------- |
| **Database** | Space used by your actual database data (tables, indexes) |
| **WAL**      | Space used by Write-Ahead Logging                         |
| **System**   | Reserved space for system operations                      |

How it helps debug issues:

| Issue                         | Description                                 |
| ----------------------------- | ------------------------------------------- |
| Space consumption monitoring  | Track disk usage trends over time           |
| Growth pattern identification | Identify rapid growth requiring attention   |
| Capacity planning             | Plan upgrades before hitting storage limits |

Actions you can take:

| Action                                                                           | Description                                                          |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| Run [VACUUM](https://www.postgresql.org/docs/current/sql-vacuum.html) operations | Reclaim dead tuple space and optimize storage                        |
| Analyze large tables                                                             | Use CLI commands like `table-sizes` to identify optimization targets |
| Implement data archival                                                          | Archive historical data to reduce active storage needs               |
| [Upgrade disk size](/docs/guides/platform/database-size)                         | Increase storage capacity when approaching limits                    |


### Database connections

<Image
  alt="Database connections chart"
  zoomable
  src={{
    dark: '/docs/img/database/reports/db-connections-chart-dark.png',
    light: '/docs/img/database/reports/db-connections-chart-light.png',
  }}
/>

| Connection Type | Description                                      |
| --------------- | ------------------------------------------------ |
| **Postgres**    | Direct connections from your application         |
| **PostgREST**   | Connections from the PostgREST API layer         |
| **Reserved**    | Administrative connections for Supabase services |
| **Auth**        | Connections from Supabase Auth service           |
| **Storage**     | Connections from Supabase Storage service        |
| **Other roles** | Miscellaneous database connections               |

How it helps debug issues:

| Issue                           | Description                                                 |
| ------------------------------- | ----------------------------------------------------------- |
| Connection pool exhaustion      | Identify when approaching maximum connection limits         |
| Connection leak detection       | Spot applications not properly closing connections          |
| Service distribution monitoring | Monitor connection usage across different Supabase services |

Actions you can take:

| Action                                                                                     | Description                                                     |
| ------------------------------------------------------------------------------------------ | --------------------------------------------------------------- |
| [Upgrade compute size](/docs/guides/platform/compute-and-disk#compute-size)                | Increase maximum connection limits                              |
| Implement [connection pooling](/docs/guides/database/connecting-to-postgres#shared-pooler) | Optimize connection management for high direct connection usage |
| Review application code                                                                    | Ensure proper connection handling and cleanup                   |



## Auth

The Auth report focuses on user authentication patterns and behaviors within your Supabase project.

| Chart                    | Description                                   | Key Insights                                    |
| ------------------------ | --------------------------------------------- | ----------------------------------------------- |
| Active Users             | Count of unique users performing auth actions | User engagement and retention patterns          |
| Sign In Attempts by Type | Breakdown of authentication methods used      | Password vs OAuth vs magic link preferences     |
| Sign Ups                 | Total new user registrations                  | Growth trends and onboarding funnel performance |
| Auth Errors              | Error rates grouped by status code            | Authentication friction and security issues     |
| Password Reset Requests  | Volume of password recovery attempts          | User experience pain points                     |



## Storage

The Storage report provides visibility into how your Supabase Storage is being utilized, including request patterns, performance characteristics, and caching effectiveness.

| Chart           | Description                                | Key Insights                                           |
| --------------- | ------------------------------------------ | ------------------------------------------------------ |
| Total Requests  | Overall request volume to Storage          | Traffic patterns and usage trends                      |
| Response Speed  | Average response time for storage requests | Performance bottlenecks and optimization opportunities |
| Network Traffic | Ingress and egress usage                   | Data transfer costs and CDN effectiveness              |
| Request Caching | Cache hit rates and miss patterns          | CDN performance and cost optimization                  |
| Top Routes      | Most frequently accessed storage paths     | Popular content and usage patterns                     |



## Realtime

The Realtime report tracks WebSocket connections, channel activity, and real-time event patterns in your Supabase project.

| Chart                 | Description                                                   | Key Insights                                      |
| --------------------- | ------------------------------------------------------------- | ------------------------------------------------- |
| Realtime Connections  | Active WebSocket connections over time                        | Concurrent user activity and connection stability |
| Channel Events        | Breakdown of broadcast, Postgres changes, and presence events | Real-time feature usage patterns                  |
| Rate of Channel Joins | Frequency of new channel subscriptions                        | User engagement with real-time features           |
| Total Requests        | HTTP requests to Realtime endpoints                           | API usage alongside WebSocket activity            |
| Response Speed        | Performance of Realtime API endpoints                         | Infrastructure optimization opportunities         |



## Edge Functions

The Edge Functions report provides insights into serverless function performance, execution patterns, and regional distribution across Supabase's global edge network.

| Chart                  | Description                               | Key Insights                                   |
| ---------------------- | ----------------------------------------- | ---------------------------------------------- |
| Execution Status Codes | Function response codes and error rates   | Function reliability and error patterns        |
| Execution Time         | Average function duration and performance | Performance optimization opportunities         |
| Invocations by Region  | Geographic distribution of function calls | Global usage patterns and latency optimization |



## API gateway

The API Gateway report analyzes traffic patterns and performance characteristics of requests flowing through your Supabase project's API layer.

| Chart           | Description                               | Key Insights                                     |
| --------------- | ----------------------------------------- | ------------------------------------------------ |
| Total Requests  | Overall API request volume                | Traffic patterns and growth trends               |
| Response Errors | Error rates with 4XX and 5XX status codes | API reliability and user experience issues       |
| Response Speed  | Average API response times                | Performance bottlenecks and optimization targets |
| Network Traffic | Request and response egress usage         | Data transfer patterns and cost implications     |
| Top Routes      | Most frequently accessed API endpoints    | Usage patterns and optimization priorities       |



# Sentry integration

Integrate Sentry to monitor errors from a Supabase client

You can use [Sentry](https://sentry.io/welcome/) to monitor errors thrown from a Supabase JavaScript client. Install the [Supabase Sentry integration](https://github.com/supabase-community/sentry-integration-js) to get started.

The Sentry integration supports browser, Node, and edge environments.



## Installation

Install the Sentry integration using your package manager:

<Tabs scrollable queryGroup="package-manager" defaultActiveId="npm" type="underlined" size="small">
  <TabPanel id="npm" label="npm">
    ```sh
    npm install @supabase/sentry-js-integration
    ```
  </TabPanel>

  <TabPanel id="yarn" label="yarn">
    ```sh
    yarn add @supabase/sentry-js-integration
    ```
  </TabPanel>

  <TabPanel id="pnpm" label="pnpm">
    ```sh
    pnpm add @supabase/sentry-js-integration
    ```
  </TabPanel>
</Tabs>



## Use

<Admonition type="note">
  If you are using Sentry JavaScript SDK v7, reference [`supabase-community/sentry-integration-js` repository](https://github.com/supabase-community/sentry-integration-js/blob/master/README-7v.md) instead.
</Admonition>

To use the Supabase Sentry integration, add it to your `integrations` list when initializing your Sentry client.

You can supply either the Supabase Client constructor or an already-initiated instance of a Supabase Client.

<Tabs scrollable defaultActiveId="constructor" type="underlined" size="small">
  <TabPanel id="constructor" label="With constructor">
    ```ts
    import * as Sentry from '@sentry/browser'
    import { SupabaseClient } from '@supabase/supabase-js'
    import { supabaseIntegration } from '@supabase/sentry-js-integration'

    Sentry.init({
      dsn: SENTRY_DSN,
      integrations: [
        supabaseIntegration(SupabaseClient, Sentry, {
          tracing: true,
          breadcrumbs: true,
          errors: true,
        }),
      ],
    })
    ```
  </TabPanel>

  <TabPanel id="instance" label="With instance">
    ```ts
    import * as Sentry from '@sentry/browser'
    import { createClient } from '@supabase/supabase-js'
    import { supabaseIntegration } from '@supabase/sentry-js-integration'

    const supabaseClient = createClient(SUPABASE_URL, SUPABASE_KEY)

    Sentry.init({
      dsn: SENTRY_DSN,
      integrations: [
        supabaseIntegration(supabaseClient, Sentry, {
          tracing: true,
          breadcrumbs: true,
          errors: true,
        }),
      ],
    })
    ```
  </TabPanel>
</Tabs>

All available configuration options are available in our [`supabase-community/sentry-integration-js` repository](https://github.com/supabase-community/sentry-integration-js/blob/master/README.md#options).



## Deduplicating spans

If you're already monitoring HTTP errors in Sentry, for example with the HTTP, Fetch, or Undici integrations, you will get duplicate spans for Supabase calls. You can deduplicate the spans by skipping them in your other integration:

```ts
import * as Sentry from '@sentry/browser'
import { SupabaseClient } from '@supabase/supabase-js'
import { supabaseIntegration } from '@supabase/sentry-js-integration'

Sentry.init({
  dsn: SENTRY_DSN,
  integrations: [
    supabaseIntegration(SupabaseClient, Sentry, {
      tracing: true,
      breadcrumbs: true,
      errors: true,
    }),

    // @sentry/browser
    Sentry.browserTracingIntegration({
      shouldCreateSpanForRequest: (url) => {
        return !url.startsWith(`${SUPABASE_URL}/rest`)
      },
    }),

    // or @sentry/node
    Sentry.httpIntegration({
      tracing: {
        ignoreOutgoingRequests: (url) => {
          return url.startsWith(`${SUPABASE_URL}/rest`)
        },
      },
    }),

    // or @sentry/node with Fetch support
    Sentry.nativeNodeFetchIntegration({
      ignoreOutgoingRequests: (url) => {
        return url.startsWith(`${SUPABASE_URL}/rest`)
      },
    }),

    // or @sentry/WinterCGFetch for Next.js Middleware & Edge Functions
    Sentry.winterCGFetchIntegration({
      breadcrumbs: true,
      shouldCreateSpanForRequest: (url) => {
        return !url.startsWith(`${SUPABASE_URL}/rest`)
      },
    }),
  ],
})
```



## Example Next.js configuration

See this example for a setup with Next.js to cover browser, server, and edge environments. First, run through the [Sentry Next.js wizard](https://docs.sentry.io/platforms/javascript/guides/nextjs/#install) to generate the base Next.js configuration. Then add the Supabase Sentry Integration to all your `Sentry.init` calls with the appropriate filters.

<Tabs scrollable defaultActiveId="browser" type="underlined" size="small">
  <TabPanel id="browser" label="Browser">
    ```ts sentry.client.config.ts
    import * as Sentry from '@sentry/nextjs'
    import { SupabaseClient } from '@supabase/supabase-js'
    import { supabaseIntegration } from '@supabase/sentry-js-integration'

    Sentry.init({
      dsn: SENTRY_DSN,
      integrations: [
        supabaseIntegration(SupabaseClient, Sentry, {
          tracing: true,
          breadcrumbs: true,
          errors: true,
        }),
        Sentry.browserTracingIntegration({
          shouldCreateSpanForRequest: (url) => {
            return !url.startsWith(`${process.env.NEXT_PUBLIC_SUPABASE_URL}/rest`)
          },
        }),
      ],

      // Adjust this value in production, or use tracesSampler for greater control
      tracesSampleRate: 1,

      // Setting this option to true will print useful information to the console while you're setting up Sentry.
      debug: true,
    })
    ```
  </TabPanel>

  <TabPanel id="server" label="Server">
    ```ts sentry.server.config.ts
    import * as Sentry from '@sentry/nextjs'
    import { SupabaseClient } from '@supabase/supabase-js'
    import { supabaseIntegration } from '@supabase/sentry-js-integration'

    Sentry.init({
      dsn: SENTRY_DSN,
      integrations: [
        supabaseIntegration(SupabaseClient, Sentry, {
          tracing: true,
          breadcrumbs: true,
          errors: true,
        }),
        Sentry.nativeNodeFetchIntegration({
          breadcrumbs: true,
          ignoreOutgoingRequests: (url) => {
            return url.startsWith(`${process.env.NEXT_PUBLIC_SUPABASE_URL}/rest`)
          },
        }),
      ],
      // Adjust this value in production, or use tracesSampler for greater control
      tracesSampleRate: 1,

      // Setting this option to true will print useful information to the console while you're setting up Sentry.
      debug: true,
    })
    ```
  </TabPanel>

  <TabPanel id="edge" label="Middleware & Edge">
    ```js sentry.edge.config.ts
    import * as Sentry from '@sentry/nextjs'
    import { SupabaseClient } from '@supabase/supabase-js'
    import { supabaseIntegration } from '@supabase/sentry-js-integration'

    Sentry.init({
      dsn: SENTRY_DSN,
      integrations: [
        supabaseIntegration(SupabaseClient, Sentry, {
          tracing: true,
          breadcrumbs: true,
          errors: true,
        }),
        Sentry.winterCGFetchIntegration({
          breadcrumbs: true,
          shouldCreateSpanForRequest: (url) => {
            return !url.startsWith(`${process.env.NEXT_PUBLIC_SUPABASE_URL}/rest`)
          },
        }),
      ],
      // Adjust this value in production, or use tracesSampler for greater control
      tracesSampleRate: 1,

      // Setting this option to true will print useful information to the console while you're setting up Sentry.
      debug: true,
    })
    ```
  </TabPanel>

  <TabPanel id="instrumentation" label="Instrumentation">
    ```js instrumentation.ts
    // https://nextjs.org/docs/app/building-your-application/optimizing/instrumentation
    export async function register() {
      if (process.env.NEXT_RUNTIME === 'nodejs') {
        await import('./sentry.server.config')
      }

      if (process.env.NEXT_RUNTIME === 'edge') {
        await import('./sentry.edge.config')
      }
    }
    ```
  </TabPanel>
</Tabs>

Afterwards, build your application (`npm run build`) and start it locally (`npm run start`). You will now see the transactions being logged in the terminal when making supabase-js requests.



# Storage Quickstart

Learn how to use Supabase to store and serve files.

This guide shows the basic functionality of Supabase Storage. Find a full [example application on GitHub](https://github.com/supabase/supabase/tree/master/examples/user-management/nextjs-user-management).



## Concepts

Supabase Storage consists of Files, Folders, and Buckets.


### Files

Files can be any sort of media file. This includes images, GIFs, and videos. It is best practice to store files outside of your database because of their sizes. For security, HTML files are returned as plain text.


### Folders

Folders are a way to organize your files (just like on your computer). There is no right or wrong way to organize your files. You can store them in whichever folder structure suits your project.


### Buckets

Buckets are distinct containers for files and folders. You can think of them like "super folders". Generally you would create distinct buckets for different Security and Access Rules. For example, you might keep all video files in a "video" bucket, and profile pictures in an "avatar" bucket.

<Admonition type="note">
  File, Folder, and Bucket names **must follow** [AWS object key naming guidelines](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-keys.html) and avoid use of any other characters.
</Admonition>



## Create a bucket

You can create a bucket using the Supabase Dashboard. Since the storage is interoperable with your Postgres database, you can also use SQL or our client libraries. Here we create a bucket called "avatars":

<Tabs scrollable size="small" type="underlined" defaultActiveId="dashboard" queryGroup="language">
  <TabPanel id="dashboard" label="Dashboard">
    1.  Go to the [Storage](/dashboard/project/_/storage/buckets) page in the Dashboard.
    2.  Click **New Bucket** and enter a name for the bucket.
    3.  Click **Create Bucket**.
  </TabPanel>

  <TabPanel id="sql" label="SQL">
    ```sql
    -- Use Postgres to create a bucket.

    insert into storage.buckets
      (id, name)
    values
      ('avatars', 'avatars');
    ```
  </TabPanel>

  <TabPanel id="javascript" label="JavaScript">
    ```js
    // Use the JS library to create a bucket.

    const { data, error } = await supabase.storage.createBucket('avatars')
    ```

    [Reference.](/docs/reference/javascript/storage-createbucket)
  </TabPanel>

  <TabPanel id="dart" label="Dart">
    ```dart
    void main() async {
      final supabase = SupabaseClient('supabaseUrl', 'supabaseKey');

      final storageResponse = await supabase
          .storage
          .createBucket('avatars');
    }
    ```

    [Reference.](https://pub.dev/documentation/storage_client/latest/storage_client/SupabaseStorageClient/createBucket.html)
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    ```swift
    try await supabase.storage.createBucket("avatars")
    ```

    [Reference.](/docs/reference/swift/storage-createbucket)
  </TabPanel>

  <TabPanel id="python" label="Python">
    ```python
    response = supabase.storage.create_bucket('avatars')
    ```

    [Reference.](/docs/reference/python/storage-createbucket)
  </TabPanel>
</Tabs>



## Upload a file

You can upload a file from the Dashboard, or within a browser using our JS libraries.

<Tabs scrollable size="small" type="underlined" defaultActiveId="dashboard" queryGroup="language">
  <TabPanel id="dashboard" label="Dashboard">
    1.  Go to the [Storage](/dashboard/project/_/storage/buckets) page in the Dashboard.
    2.  Select the bucket you want to upload the file to.
    3.  Click **Upload File**.
    4.  Select the file you want to upload.
  </TabPanel>

  <TabPanel id="javascript" label="JavaScript">
    ```js
    const avatarFile = event.target.files[0]
    const { data, error } = await supabase.storage
      .from('avatars')
      .upload('public/avatar1.png', avatarFile)
    ```

    [Reference.](/docs/reference/javascript/storage-from-upload)
  </TabPanel>

  <TabPanel id="dart" label="Dart">
    ```dart
    void main() async {
      final supabase = SupabaseClient('supabaseUrl', 'supabaseKey');

      // Create file `example.txt` and upload it in `public` bucket
      final file = File('example.txt');
      file.writeAsStringSync('File content');
      final storageResponse = await supabase
          .storage
          .from('public')
          .upload('example.txt', file);
    }
    ```

    [Reference.](https://pub.dev/documentation/storage_client/latest/storage_client/SupabaseStorageClient/createBucket.html)
  </TabPanel>
</Tabs>



## Download a file

You can download a file from the Dashboard, or within a browser using our JS libraries.

<Tabs scrollable size="small" type="underlined" defaultActiveId="dashboard" queryGroup="language">
  <TabPanel id="dashboard" label="Dashboard">
    1.  Go to the [Storage](/dashboard/project/_/storage/buckets) page in the Dashboard.
    2.  Select the bucket that contains the file.
    3.  Select the file that you want to download.
    4.  Click **Download**.
  </TabPanel>

  <TabPanel id="javascript" label="JavaScript">
    ```js
    // Use the JS library to download a file.

    const { data, error } = await supabase.storage.from('avatars').download('public/avatar1.png')
    ```

    [Reference.](/docs/reference/javascript/storage-from-download)
  </TabPanel>

  <TabPanel id="dart" label="Dart">
    ```dart
    void main() async {
      final supabase = SupabaseClient('supabaseUrl', 'supabaseKey');

      final storageResponse = await supabase
          .storage
          .from('public')
          .download('example.txt');
    }
    ```

    [Reference.](/docs/reference/dart/storage-from-download)
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    ```swift
    let response = try await supabase.storage.from("avatars").download(path: "public/avatar1.png")
    ```

    [Reference.](/docs/reference/python/storage-from-download)
  </TabPanel>

  <TabPanel id="python" label="Python">
    ```python
    response = supabase.storage.from_('avatars').download('public/avatar1.png')
    ```

    [Reference.](/docs/reference/python/storage-from-download)
  </TabPanel>
</Tabs>



## Add security rules

To restrict access to your files you can use either the Dashboard or SQL.

<Tabs scrollable size="small" type="underlined" defaultActiveId="dashboard" queryGroup="database-method">
  <TabPanel id="dashboard" label="Dashboard">
    1.  Go to the [Storage](/dashboard/project/_/storage/buckets) page in the Dashboard.
    2.  Click **Policies** in the sidebar.
    3.  Click **Add Policies** in the `OBJECTS` table to add policies for Files. You can also create policies for Buckets.
    4.  Choose whether you want the policy to apply to downloads (SELECT), uploads (INSERT), updates (UPDATE), or deletes (DELETE).
    5.  Give your policy a unique name.
    6.  Write the policy using SQL.
  </TabPanel>

  <TabPanel id="sql" label="SQL">
    ```sql
    -- Use SQL to create a policy.

    create policy "Public Access"
      on storage.objects for select
      using ( bucket_id = 'public' );
    ```
  </TabPanel>
</Tabs>

***

{/* Finish with a video. This also appears in the Sidebar via the "tocVideo" metadata */}

<div className="video-container">
  <iframe src="https://www.youtube-nocookie.com/embed/J9mTPY8rIXE" frameBorder="1" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />
</div>



# Limits

Learn how to increase Supabase file limits.


## Global file size

You can set the maximum file size across all your buckets by setting the *Global file size limit* value in your [Storage Settings](/dashboard/project/_/storage/settings). For Free projects, the limit can't exceed 50 MB. On the Pro Plan and up, you can set this value to up to 500 GB. If you need more than 500 GB, [contact us](/dashboard/support/new).

| Plan       | Max File Size Limit |
| ---------- | ------------------- |
| Free       | 50 MB               |
| Pro        | 500 GB              |
| Team       | 500 GB              |
| Enterprise | Custom              |

<Admonition type="note">
  This option is a global limit, which applies to all your buckets.
</Admonition>

Additionally, you can specify the maximum file size on a per [bucket level](/docs/guides/storage/buckets/creating-buckets#restricting-uploads) but it can't be higher than this global limit. As a good practice, the global limit should be set to the highest possible file size that your application accepts, with smaller per-bucket limits set as needed.



## Per bucket restrictions

You can have different restrictions on a per bucket level such as restricting the file types (e.g. `pdf`, `images`, `videos`) or the maximum file size, which should be lower than the global limit. To apply these limit on a bucket level see [Creating Buckets](/docs/guides/storage/buckets/creating-buckets#restricting-uploads).



# Resumable Uploads

Learn how to upload files to Supabase Storage.

The resumable upload method is recommended when:

*   Uploading large files that may exceed 6MB in size
*   Network stability is a concern
*   You want to have progress events for your uploads

Supabase Storage implements the [TUS protocol](https://tus.io/) to enable resumable uploads. TUS stands for The Upload Server and is an open protocol for supporting resumable uploads. The protocol allows the upload process to be resumed from where it left off in case of interruptions. This method can be implemented using the [`tus-js-client`](https://github.com/tus/tus-js-client) library, or other client-side libraries like [Uppy](https://uppy.io/docs/tus/) that support the TUS protocol.

<Admonition type="note">
  For optimal performance when uploading large files you should always use the direct storage hostname. This provides several performance enhancements that will greatly improve performance when uploading large files.

  Instead of `https://project-id.supabase.co` use `https://project-id.storage.supabase.co`
</Admonition>

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    Here's an example of how to upload a file using `tus-js-client`:

    ```javascript
    const tus = require('tus-js-client')

    const projectId = ''

    async function uploadFile(bucketName, fileName, file) {
        const { data: { session } } = await supabase.auth.getSession()

        return new Promise((resolve, reject) => {
            var upload = new tus.Upload(file, {
                // Supabase TUS endpoint (with direct storage hostname)
                endpoint: `https://${projectId}.storage.supabase.co/storage/v1/upload/resumable`,
                retryDelays: [0, 3000, 5000, 10000, 20000],
                headers: {
                    authorization: `Bearer ${session.access_token}`,
                    'x-upsert': 'true', // optionally set upsert to true to overwrite existing files
                },
                uploadDataDuringCreation: true,
                removeFingerprintOnSuccess: true, // Important if you want to allow re-uploading the same file https://github.com/tus/tus-js-client/blob/main/docs/api.md#removefingerprintonsuccess
                metadata: {
                    bucketName: bucketName,
                    objectName: fileName,
                    contentType: 'image/png',
                    cacheControl: 3600,
                    metadata: JSON.stringify({ // custom metadata passed to the user_metadata column
                       yourCustomMetadata: true,
                    }),
                },
                chunkSize: 6 * 1024 * 1024, // NOTE: it must be set to 6MB (for now) do not change it
                onError: function (error) {
                    console.log('Failed because: ' + error)
                    reject(error)
                },
                onProgress: function (bytesUploaded, bytesTotal) {
                    var percentage = ((bytesUploaded / bytesTotal) * 100).toFixed(2)
                    console.log(bytesUploaded, bytesTotal, percentage + '%')
                },
                onSuccess: function () {
                    console.log('Download %s from %s', upload.file.name, upload.url)
                    resolve()
                },
            })


            // Check if there are any previous uploads to continue.
            return upload.findPreviousUploads().then(function (previousUploads) {
                // Found previous uploads so we select the first one.
                if (previousUploads.length) {
                    upload.resumeFromPreviousUpload(previousUploads[0])
                }

                // Start the upload
                upload.start()
            })
        })
    }
    ```
  </TabPanel>

  <TabPanel id="react" label="React">
    Here's an example of how to upload a file using `@uppy/tus` with react:

    ```javascript
    import { useEffect, useState } from "react";
    import { createClient } from "@supabase/supabase-js";
    import Uppy from "@uppy/core";
    import Tus from "@uppy/tus";
    import Dashboard from "@uppy/dashboard";
    import "@uppy/core/dist/style.min.css";
    import "@uppy/dashboard/dist/style.min.css";

    function App() {
        // Initialize Uppy instance with the 'sample' bucket specified for uploads
        const uppy = useUppyWithSupabase({ bucketName: "sample" });

        useEffect(() => {
            // Set up Uppy Dashboard to display as an inline component within a specified target
            uppy.use(Dashboard, {
                inline: true, // Ensures the dashboard is rendered inline
                target: "#drag-drop-area", // HTML element where the dashboard renders
                showProgressDetails: true, // Show progress details for file uploads
            });
        }, []);

        return (
            <div id="drag-drop-area">
            </div>
            {/* Target element for the Uppy Dashboard */}
        );
    }

    export default App;

    /**
     * Custom hook for configuring Uppy with Supabase authentication and TUS resumable uploads
     * @param {Object} options - Configuration options for the Uppy instance.
     * @param {string} options.bucketName - The bucket name in Supabase where files are stored.
     * @returns {Object} uppy - Uppy instance with configured upload settings.
     */
    export const useUppyWithSupabase = ({ bucketName }: { bucketName: string }) => {
        // Initialize Uppy instance only once
        const [uppy] = useState(() => new Uppy());
        // Initialize Supabase client with project URL and anon key
        const supabase = createClient(`https://${projectId}.supabase.co`, anonKey);

        useEffect(() => {
            const initializeUppy = async () => {
            // Retrieve the current user's session for authentication
            const {
                data: { session },
            } = await supabase.auth.getSession();

            uppy.use(Tus, {
                    // Supabase TUS endpoint (with direct storage hostname)
                    endpoint: `https://${projectId}.storage.supabase.co/storage/v1/upload/resumable`,
                    retryDelays: [0, 3000, 5000, 10000, 20000], // Retry delays for resumable uploads
                    headers: {
                        authorization: `Bearer ${session?.access_token}`, // User session access token
                        apikey: anonKey, // API key for Supabase
                    },
                    uploadDataDuringCreation: true, // Send metadata with file chunks
                    removeFingerprintOnSuccess: true, // Remove fingerprint after successful upload
                    chunkSize: 6 * 1024 * 1024, // Chunk size for TUS uploads (6MB)
                    allowedMetaFields: [
                        "bucketName",
                        "objectName",
                        "contentType",
                        "cacheControl",
                        "metadata",
                    ], // Metadata fields allowed for the upload
                    onError: (error) => console.error("Upload error:", error), // Error handling for uploads
                }).on("file-added", (file) => {
                    // Attach metadata to each file, including bucket name and content type
                    file.meta = {
                        ...file.meta,
                        bucketName, // Bucket specified by the user of the hook
                        objectName: file.name, // Use file name as object name
                        contentType: file.type, // Set content type based on file MIME type
                        metadata: JSON.stringify({ // custom metadata passed to the user_metadata column
                            yourCustomMetadata: true,
                        }),
                    };
                });
            };

            // Initialize Uppy with Supabase settings
            initializeUppy();
        }, [uppy, bucketName]);

        // Return the configured Uppy instance
        return uppy;
    };

    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    Kotlin supports resumable uploads natively for all targets:

    ```kotlin
    suspend fun uploadFile(file: File) {
        val upload: ResumableUpload = supabase.storage.from("bucket_name")
            .resumable.createOrContinueUpload("file_path", file)
        upload.stateFlow
            .onEach {
                println(it.progress)
            }
            .launchIn(yourCoroutineScope)
        upload.startOrResumeUploading()
    }

    // On other platforms you might have to give the bytes directly and specify a source if you want to continue it later:
    suspend fun uploadData(bytes: ByteArray) {
        val upload: ResumableUpload = supabase.storage.from("bucket_name")
            .resumable.createOrContinueUpload(bytes, "source", "file_path")

        upload.stateFlow
            .onEach {
                println(it.progress)
            }
            .launchIn(yourCoroutineScope)
        upload.startOrResumeUploading()
    }
    ```
  </TabPanel>

  <TabPanel id="py" label="Python">
    Here's an example of how to upload a file using [`tus-py-client`](https://github.com/tus/tus-py-client):

    ```python
    from io import BufferedReader
    from tusclient import client
    from supabase import create_client

    def upload_file(
        bucket_name: str, file_name: str, file: BufferedReader, access_token: str
    ):
        # create Tus client
        my_client = client.TusClient(
            f"{supabase_url}/storage/v1/upload/resumable",
            headers={"Authorization": f"Bearer {access_token}", "x-upsert": "true"},
        )
        uploader = my_client.uploader(
            file_stream=file,
            chunk_size=(6 * 1024 * 1024),
            metadata={
                "bucketName": bucket_name,
                "objectName": file_name,
                "contentType": "image/png",
                "cacheControl": "3600",
            },
        )
        uploader.upload()

    # create client and sign in
    supabase = create_client(supabase_url, supabase_key)

    # retrieve the current user's session for authentication
    session = supabase.auth.get_session()

    # open file and send file stream to upload
    with open("./assets/40mb.jpg", "rb") as fs:
        upload_file(
            bucket_name="assets",
            file_name="large_file",
            file=fs,
            access_token=session.access_token,
        )
    ```
  </TabPanel>
</Tabs>


### Upload URL

When uploading using the resumable upload endpoint, the storage server creates a unique URL for each upload, even for multiple uploads to the same path. All chunks will be uploaded to this URL using the `PATCH` method.

This unique upload URL will be valid for **up to 24 hours**. If the upload is not completed within 24 hours, the URL will expire and you'll need to start the upload again. TUS client libraries typically create a new URL if the previous one expires.


### Concurrency

When two or more clients upload to the same upload URL only one of them will succeed. The other clients will receive a `409 Conflict` error. Only 1 client can upload to the same upload URL at a time which prevents data corruption.

When two or more clients upload a file to the same path using different upload URLs, the first client to complete the upload will succeed and the other clients will receive a `409 Conflict` error.

If you provide the `x-upsert` header the last client to complete the upload will succeed instead.


### Uppy example

You can check a [full example using Uppy](https://github.com/supabase/supabase/tree/master/examples/storage/resumable-upload-uppy).

Uppy has integrations with different frameworks:

*   [React](https://uppy.io/docs/react/)
*   [Svelte](https://uppy.io/docs/svelte/)
*   [Vue](https://uppy.io/docs/vue/)
*   [Angular](https://uppy.io/docs/angular/)



## Overwriting files

When uploading a file to a path that already exists, the default behavior is to return a `400 Asset Already Exists` error.
If you want to overwrite a file on a specific path you can set the `x-upsert` header to `true`.

We do advise against overwriting files when possible, as the CDN will take some time to propagate the changes to all the edge nodes leading to stale content.
Uploading a file to a new path is the recommended way to avoid propagation delays and stale content.

To learn more, see the [CDN](/docs/guides/storage/cdn/fundamentals) guide.



# S3 Uploads

Learn how to upload files to Supabase Storage using S3.

You can use the S3 protocol to upload files to Supabase Storage. To get started with S3, see the [S3 setup guide](/docs/guides/storage/s3/authentication).

The S3 protocol supports file upload using:

*   A single request
*   Multiple requests via Multipart Upload



## Single request uploads

The `PutObject` action uploads the file in a single request. This matches the behavior of the Supabase SDK [Standard Upload](/docs/guides/storage/uploads/standard-uploads).

Use `PutObject` to upload smaller files, where retrying the entire upload won't be an issue. The maximum file size on paid plans is 500 GB.

For example, using JavaScript and the `aws-sdk` client:

```javascript
import { S3Client, PutObjectCommand } from '@aws-sdk/client-s3'

const s3Client = new S3Client({...})

const file = fs.createReadStream('path/to/file')

const uploadCommand = new PutObjectCommand({
  Bucket: 'bucket-name',
  Key: 'path/to/file',
  Body: file,
  ContentType: 'image/jpeg',
})

await s3Client.send(uploadCommand)
```



## Multipart uploads

Multipart Uploads split the file into smaller parts and upload them in parallel, maximizing the upload speed on a fast network. When uploading large files, this allows you to retry the upload of individual parts in case of network issues.

This method is preferable over [Resumable Upload](/docs/guides/storage/uploads/resumable-uploads) for server-side uploads, when you want to maximize upload speed at the cost of resumability. The maximum file size on paid plans is 500 GB.


### Upload a file in parts

Use the `Upload` class from an S3 client to upload a file in parts. For example, using JavaScript:

```javascript
import { S3Client } from '@aws-sdk/client-s3'
import { Upload } from '@aws-sdk/lib-storage'

const s3Client = new S3Client({...})

const file = fs.createReadStream('path/to/very-large-file')

const upload = new Upload(s3Client, {
  Bucket: 'bucket-name',
  Key: 'path/to/file',
  ContentType: 'image/jpeg',
  Body: file,
})

await uploader.done()
```


### Aborting multipart uploads

All multipart uploads are automatically aborted after 24 hours. To abort a multipart upload before that, you can use the [`AbortMultipartUpload`](https://docs.aws.amazon.com/AmazonS3/latest/API/API_AbortMultipartUpload.html) action.



# Standard Uploads

Learn how to upload files to Supabase Storage.


## Uploading

The standard file upload method is ideal for small files that are not larger than 6MB.

It uses the traditional `multipart/form-data` format and is simple to implement using the supabase-js SDK. Here's an example of how to upload a file using the standard upload method:

<Admonition type="note">
  Though you can upload up to 5GB files using the standard upload method, we recommend using [TUS Resumable Upload](/docs/guides/storage/uploads/resumable-uploads) for uploading files greater than 6MB in size for better reliability.
</Admonition>

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    ```javascript
    // @noImplicitAny: false

    // ---cut---
    import { createClient } from '@supabase/supabase-js'

    // Create Supabase client
    const supabase = createClient('your_project_url', 'your_supabase_api_key')

    // Upload file using standard upload
    async function uploadFile(file) {
      const { data, error } = await supabase.storage.from('bucket_name').upload('file_path', file)
      if (error) {
        // Handle error
      } else {
        // Handle success
      }
    }
    ```
  </TabPanel>

  <TabPanel id="dart" label="Dart">
    ```dart
    // Upload file using standard upload
    Future<void> uploadFile(File file) async {
      await supabase.storage.from('bucket_name').upload('file_path', file);
    }
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    ```swift
    import Supabase

    // Create Supabase client
    let supabase = SupabaseClient(supabaseURL: URL(string: "your_project_url")!, supabaseKey: "your_supabase_api_key")

    try await supabase.storage.from("bucket_name").upload(path: "file_path", file: file)
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    ```kotlin
    supabase.storage.from("bucket_name").upload("file_path", bytes)

    //Or on JVM/Android: (This will stream the data from the file to supabase)
    supabase.storage.from("bucket_name").upload("file_path", file)
    ```
  </TabPanel>

  <TabPanel id="python" label="Python">
    ```python
    response = supabase.storage.from_('bucket_name').upload('file_path', file)
    ```
  </TabPanel>
</Tabs>



## Overwriting files

When uploading a file to a path that already exists, the default behavior is to return a `400 Asset Already Exists` error.
If you want to overwrite a file on a specific path you can set the `upsert` options to `true` or using the `x-upsert` header.

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    ```javascript
    import { createClient } from '@supabase/supabase-js'
    const file = new Blob()

    // ---cut---
    // Create Supabase client
    const supabase = createClient('your_project_url', 'your_supabase_api_key')

    await supabase.storage.from('bucket_name').upload('file_path', file, {
      upsert: true,
    })
    ```
  </TabPanel>

  <TabPanel id="dart" label="Dart">
    ```dart
    await supabase.storage.from('bucket_name').upload(
          'file_path',
          file,
          fileOptions: const FileOptions(upsert: true),
        );
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    ```swift
    import Supabase

    // Create Supabase client
    let supabase = SupabaseClient(supabaseURL: URL(string: "your_project_url")!, supabaseKey: "your_supabase_api_key")

    try await supabase.storage.from("bucket_name")
      .upload(
        path: "file_path",
        file: file,
        options: FileOptions(
          upsert: true
        )
      )
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    ```kotlin
    supabase.storage.from("bucket_name").upload("file_path", bytes) {
        upsert = true
    }
    ```
  </TabPanel>

  <TabPanel id="python" label="Python">
    ```python
    response = supabase.storage.from_('bucket_name').upload('file_path', file, {
      'upsert': 'true',
    })
    ```
  </TabPanel>
</Tabs>

We do advise against overwriting files when possible, as our Content Delivery Network will take sometime to propagate the changes to all the edge nodes leading to stale content.
Uploading a file to a new path is the recommended way to avoid propagation delays and stale content.



## Content type

By default, Storage will assume the content type of an asset from the file extension. If you want to specify the content type for your asset, pass the `contentType` option during upload.

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    ```javascript
    import { createClient } from '@supabase/supabase-js'
    const file = new Blob()

    // ---cut---
    // Create Supabase client
    const supabase = createClient('your_project_url', 'your_supabase_api_key')

    await supabase.storage.from('bucket_name').upload('file_path', file, {
      contentType: 'image/jpeg',
    })
    ```
  </TabPanel>

  <TabPanel id="dart" label="Dart">
    ```dart
    await supabase.storage.from('bucket_name').upload(
          'file_path',
          file,
          fileOptions: const FileOptions(contentType: 'image/jpeg'),
        );
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    ```swift
    import Supabase

    // Create Supabase client
    let supabase = SupabaseClient(supabaseURL: URL(string: "your_project_url")!, supabaseKey: "your_supabase_api_key")

    try await supabase.storage.from("bucket_name")
      .upload(
        path: "file_path",
        file: file,
        options: FileOptions(
          contentType: "image/jpeg"
        )
      )
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    ```kotlin
    supabase.storage.from("bucket_name").upload("file_path", bytes) {
        contentType = ContentType.Image.JPEG
    }
    ```
  </TabPanel>

  <TabPanel id="python" label="Python">
    ```python
    response = supabase.storage.from_('bucket_name').upload('file_path', file, {
      'content-type': 'image/jpeg',
    })
    ```
  </TabPanel>
</Tabs>



## Concurrency

When two or more clients upload a file to the same path, the first client to complete the upload will succeed and the other clients will receive a `400 Asset Already Exists` error.
If you provide the `x-upsert` header the last client to complete the upload will succeed instead.



# Bandwidth & Storage Egress

Bandwidth & Storage Egress


## Bandwidth & Storage egress

Free Plan Organizations in Supabase have a limit of 10 GB of bandwidth (5 GB cached + 5 GB uncached). This limit is calculated by the sum of all the data transferred from the Supabase servers to the client. This includes all the data transferred from the database, storage, and functions.


### Checking Storage egress requests in Logs Explorer

We have a template query that you can use to get the number of requests for each object in [Logs Explorer](/dashboard/project/_/logs/explorer/templates).

```sql
select
  request.method as http_verb,
  request.path as filepath,
  (responseHeaders.cf_cache_status = 'HIT') as cached,
  count(*) as num_requests
from
  edge_logs
  cross join unnest(metadata) as metadata
  cross join unnest(metadata.request) as request
  cross join unnest(metadata.response) as response
  cross join unnest(response.headers) as responseHeaders
where
  (path like '%storage/v1/object/%' or path like '%storage/v1/render/%')
  and request.method = 'GET'
group by 1, 2, 3
order by num_requests desc
limit 100;
```

Example of the output:

```json
[
  {
    "filepath": "/storage/v1/object/sign/large%20bucket/20230902_200037.gif",
    "http_verb": "GET",
    "cached": true,
    "num_requests": 100
  },
  {
    "filepath": "/storage/v1/object/public/demob/Sports/volleyball.png",
    "http_verb": "GET",
    "cached": false,
    "num_requests": 168
  }
]
```


### Calculating egress

If you already know the size of those files, you can calculate the egress by multiplying the number of requests by the size of the file.
You can also get the size of the file with the following cURL:

```bash
curl -s -w "%{size_download}\n" -o /dev/null "https://my_project.supabase.co/storage/v1/object/large%20bucket/20230902_200037.gif"
```

This will return the size of the file in bytes.
For this example, let's say that `20230902_200037.gif` has a file size of 3 megabytes and `volleyball.png` has a file size of 570 kilobytes.

Now, we have to sum all the egress for all the files to get the total egress:

```
100 * 3MB = 300MB
168 * 570KB = 95.76MB
Total Egress = 395.76MB
```

You can see that these values can get quite large, so it's important to keep track of the egress and optimize the files.


### Optimizing egress

See our [scaling tips for egress](/docs/guides/storage/production/scaling#egress).



# Serving assets from Storage

Serving assets from Storage


## Public buckets

As mentioned in the [Buckets Fundamentals](/docs/guides/storage/buckets/fundamentals) all files uploaded in a public bucket are publicly accessible and benefit a high CDN cache HIT ratio.

You can access them by using this conventional URL:

```
https://[project_id].supabase.co/storage/v1/object/public/[bucket]/[asset-name]
```

You can also use the Supabase SDK `getPublicUrl` to generate this URL for you

```js
import { createClient } from '@supabase/supabase-js'
const supabase = createClient('your_project_url', 'your_supabase_api_key')

// ---cut---
const { data } = supabase.storage.from('bucket').getPublicUrl('filePath.jpg')

console.log(data.publicUrl)
```


### Downloading

If you want the browser to start an automatic download of the asset instead of trying serving it, you can add the `?download` query string parameter.

By default it will use the asset name to save the file on disk. You can optionally pass a custom name to the `download` parameter as following: `?download=customname.jpg`



## Private buckets

Assets stored in a non-public bucket are considered private and are not accessible via a public URL like the public buckets.

You can access them only by:

*   Signing a time limited URL on the Server, for example with Edge Functions.
*   with a GET request the URL `https://[project_id].supabase.co/storage/v1/object/authenticated/[bucket]/[asset-name]` and the user Authorization header


### Signing URLs

You can sign a time-limited URL that you can share to your users by invoking the `createSignedUrl` method on the SDK.

```js
import { createClient } from '@supabase/supabase-js'
const supabase = createClient('your_project_url', 'your_supabase_api_key')

// ---cut---
const { data, error } = await supabase.storage
  .from('bucket')
  .createSignedUrl('private-document.pdf', 3600)

if (data) {
  console.log(data.signedUrl)
}
```



# Storage Image Transformations

Transform images with Storage

Supabase Storage offers the functionality to optimize and resize images on the fly. Any image stored in your buckets can be transformed and optimized for fast delivery.

<Admonition type="note">
  Image Resizing is currently enabled for [Pro Plan and above](/pricing).
</Admonition>



## Get a public URL for a transformed image

Our client libraries methods like `getPublicUrl` and `createSignedUrl` support the `transform` option. This returns the URL that serves the transformed image.

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    ```ts
    import { createClient } from '@supabase/supabase-js'
    const supabase = createClient('your_project_url', 'your_supabase_api_key')

    // ---cut---
    supabase.storage.from('bucket').getPublicUrl('image.jpg', {
      transform: {
        width: 500,
        height: 600,
      },
    })
    ```
  </TabPanel>

  <TabPanel id="dart" label="Dart">
    ```dart
    final url = supabase.storage.from('bucket').getPublicUrl(
          'image.jpg',
          transform: const TransformOptions(
            width: 500,
            height: 600,
          ),
        );
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    ```swift
    let url = try await supabase.storage.from("bucket")
      .getPublicURL(
        path: "image.jpg"
        options: TransformOptions(with: 500, height: 600)
      )
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    ```kotlin
    val url = supabase.storage.from("bucket").publicRenderUrl("image.jpg") {
        size(width = 500, height = 600)
    }
    ```
  </TabPanel>

  <TabPanel id="python" label="Python">
    ```python
    url = supabase.storage.from_('avatars').get_public_url(
      'image.jpg',
      {
        'transform': {
          'width': 500,
          'height': 500,
        },
      }
    )
    ```
  </TabPanel>
</Tabs>

An example URL could look like this:

```
https://project_id.supabase.co/storage/v1/render/image/public/bucket/image.jpg?width=500&height=600`
```



## Signing URLs with transformation options

To share a transformed image in a private bucket for a fixed amount of time, provide the transform option when you create the signed URL:

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    ```ts
    import { createClient } from '@supabase/supabase-js'
    const supabase = createClient('your_project_url', 'your_supabase_api_key')

    // ---cut---
    supabase.storage.from('bucket').createSignedUrl('image.jpg', 60000, {
      transform: {
        width: 200,
        height: 200,
      },
    })
    ```
  </TabPanel>

  <TabPanel id="dart" label="Dart">
    ```dart
    final url = await supabase.storage.from('bucket').createSignedUrl(
          'image.jpg',
          60000,
          transform: const TransformOptions(
            width: 200,
            height: 200,
          ),
        );
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    ```swift
    let url = try await supabase.storage.from("bucket")
      .createSignedURL(
        path: "image.jpg",
        expiresIn: 60,
        transform: TransformOptions(
          width: 200,
          height: 200
        )
      )
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    ```kotlin
    val url = supabase.storage.from("bucket").createSignedUrl("image.jpg", 60.seconds) {
    	size(200, 200)
    }
    ```
  </TabPanel>
</Tabs>

The transformation options are embedded into the token attached to the URL — they cannot be changed once signed.



## Downloading images

To download a transformed image, pass the `transform` option to the `download` function.

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    ```ts
    import { createClient } from '@supabase/supabase-js'
    const supabase = createClient('your_project_url', 'your_supabase_api_key')

    // ---cut---
    supabase.storage.from('bucket').download('image.jpg', {
      transform: {
        width: 800,
        height: 300,
      },
    })
    ```
  </TabPanel>

  <TabPanel id="dart" label="Dart">
    ```dart
    final data = await supabase.storage.from('bucket').download(
          'image.jpg',
          transform: const TransformOptions(
            width: 800,
            height: 300,
          ),
        );
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    ```swift
    let data = try await supabase.storage.from("bucket")
      .download(
        path: "image.jpg",
        options: TransformOptions(
          width: 800,
          height: 300
        )
      )
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    ```kotlin
    val data = supabase.storage.from("bucket").downloadAuthenticated("image.jpg") {
        transform {
            size(800, 300)
        }
    }

    //Or on JVM stream directly to a file
    val file = File("image.jpg")
    supabase.storage.from("bucket").downloadAuthenticatedTo("image.jpg", file) {
        transform {
            size(800, 300)
        }
    }
    ```
  </TabPanel>

  <TabPanel id="python" label="Python">
    ```python
    response = supabase.storage.from_('bucket').download(
      'image.jpg',
      {
        'width': 800,
        'height': 300,
      },
    )
    ```
  </TabPanel>
</Tabs>



## Automatic image optimization (WebP)

When using the image transformation API, Storage will automatically find the best format supported by the client and return that to the client, without any code change. For instance, if you use Chrome when viewing a JPEG image and using transformation options, you'll see that images are automatically optimized as `webp` images.

As a result, this will lower the egress that you send to your users and your application will load much faster.

<Admonition type="note">
  We currently only support WebP. AVIF support will come in the near future.
</Admonition>

**Disabling automatic optimization:**

In case you'd like to return the original format of the image and **opt-out** from the automatic image optimization detection, you can pass the `format=origin` parameter when requesting a transformed image, this is also supported in the JavaScript SDK starting from v2.2.0

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    ```ts
    import { createClient } from '@supabase/supabase-js'
    const supabase = createClient('your_project_url', 'your_supabase_api_key')

    // ---cut---
    await supabase.storage.from('bucket').download('image.jpeg', {
      transform: {
        width: 200,
        height: 200,
        format: 'origin',
      },
    })
    ```
  </TabPanel>

  <TabPanel id="dart" label="Dart">
    ```dart
    final data = await supabase.storage.from('bucket').download(
          'image.jpeg',
          transform: const TransformOptions(
            width: 200,
            height: 200,
            format: RequestImageFormat.origin,
          ),
        );
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    ```swift
    let data = try await supabase.storage.from("bucket")
      .download(
        path: "image.jpg",
        options: TransformOptions(
          width: 200,
          height: 200,
          format: "origin"
        )
      )
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    ```kotlin
    val data = supabase.storage.from("bucket").downloadAuthenticated("image.jpg") {
        transform {
            size(200, 200)
            format = ImageTransformation.Format.ORIGIN
        }
    }

    //Or on JVM stream directly to a file
    val file = File("image.jpg")
    supabase.storage.from("bucket").downloadAuthenticatedTo("image.jpg", file) {
        transform {
            size(200, 200)
            format = ImageTransformation.Format.ORIGIN
        }
    }
    ```
  </TabPanel>

  <TabPanel id="python" label="Python">
    ```python
    response = supabase.storage.from_('bucket').download(
      'image.jpeg',
      {
        'transform': {
          'width': 200,
          'height': 200,
          'format': 'origin',
        },
      }
    )
    ```
  </TabPanel>
</Tabs>



## Next.js loader

You can use Supabase Image Transformation to optimize your Next.js images using a custom [Loader](https://nextjs.org/docs/api-reference/next/image#loader-configuration).

To get started, create a `supabase-image-loader.js` file in your Next.js project which exports a default function:

```ts
const projectId = '' // your supabase project id

export default function supabaseLoader({ src, width, quality }) {
  return `https://${projectId}.supabase.co/storage/v1/render/image/public/${src}?width=${width}&quality=${quality || 75}`
}
```

In your `next.config.js` file add the following configuration to instruct Next.js to use our custom loader

```js
module.exports = {
  images: {
    loader: 'custom',
    loaderFile: './supabase-image-loader.js',
  },
}
```

At this point you are ready to use the `Image` component provided by Next.js

```tsx
import Image from 'next/image'

const MyImage = (props) => {
  return <Image src="bucket/image.png" alt="Picture of the author" width={500} height={500} />
}
```



## Transformation options

We currently support a few transformation options focusing on optimizing, resizing, and cropping images.


### Optimizing

You can set the quality of the returned image by passing a value from 20 to 100 (with 100 being the highest quality) to the `quality` parameter. This parameter defaults to 80.

Example:

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    ```ts
    import { createClient } from '@supabase/supabase-js'
    const supabase = createClient('your_project_url', 'your_supabase_api_key')

    // ---cut---
    supabase.storage.from('bucket').download('image.jpg', {
      transform: {
        quality: 50,
      },
    })
    ```
  </TabPanel>

  <TabPanel id="dart" label="Dart">
    ```dart
    final data = await supabase.storage.from('bucket').download(
          'image.jpg',
          transform: const TransformOptions(
            quality: 50,
          ),
        );
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    ```swift
    let data = try await supabase.storage.from("bucket")
      .download(
        path: "image.jpg",
        options: TransformOptions(
          quality: 50
        )
      )
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    ```kotlin
    val data = supabase.storage["bucket"].downloadAuthenticated("image.jpg") {
        transform {
            quality = 50
        }
    }

    //Or on JVM stream directly to a file
    val file = File("image.jpg")
    supabase.storage["bucket"].downloadAuthenticatedTo("image.jpg", file) {
        transform {
            quality = 50
        }
    }
    ```
  </TabPanel>

  <TabPanel id="python" label="Python">
    ```python
    response = supabase.storage.from_('bucket').download(
      'image.jpg',
      {
        'transform': {
          'quality': 50,
        },
      }
    )
    ```
  </TabPanel>
</Tabs>


### Resizing

You can use `width` and `height` parameters to resize an image to a specific dimension. If only one parameter is specified, the image will be resized and cropped, maintaining the aspect ratio.


### Modes

You can use different resizing modes to fit your needs, each of them uses a different approach to resize the image:

Use the `resize` parameter with one of the following values:

*   `cover` : resizes the image while keeping the aspect ratio to fill a given size and crops projecting parts. (default)

*   `contain` : resizes the image while keeping the aspect ratio to fit a given size.

*   `fill` : resizes the image without keeping the aspect ratio.

Example:

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    ```ts
    import { createClient } from '@supabase/supabase-js'
    const supabase = createClient('your_project_url', 'your_supabase_api_key')

    // ---cut---
    supabase.storage.from('bucket').download('image.jpg', {
      transform: {
        width: 800,
        height: 300,
        resize: 'contain', // 'cover' | 'fill'
      },
    })
    ```
  </TabPanel>

  <TabPanel id="dart" label="Dart">
    ```dart
    final data = supabase.storage.from('bucket').download(
          'image.jpg',
          transform: const TransformOptions(
            width: 800,
            height: 300,
            resize: ResizeMode.contain, // 'cover' | 'fill'
          ),
        );
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    ```swift
    let data = try await supabase.storage.from("bucket")
      .download(
        path: "image.jpg",
        options: TransformOptions(
          width: 800,
          height: 300,
          resize: "contain" // "cover" | "fill"
        )
      )
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    ```kotlin
    val data = supabase.storage.from("bucket").downloadAuthenticated("image.jpg") {
        transform {
            size(800, 300)
            resize = ImageTransformation.Resize.CONTAIN
        }
    }

    //Or on JVM stream directly to a file
    val file = File("image.jpg")
    supabase.storage.from("bucket").downloadAuthenticatedTo("image.jpg", file) {
        transform {
            size(800, 300)
            resize = ImageTransformation.Resize.CONTAIN
        }
    }
    ```
  </TabPanel>

  <TabPanel id="python" label="Python">
    ```python
    response = supabase.storage.from_('bucket').download(
      'image.jpg',
      {
        'transform': {
          'width': 800,
          'height': 300,
          'resize': 'contain', # 'cover' | 'fill'
        }
      }
    )
    ```
  </TabPanel>
</Tabs>


### Limits

*   Width and height must be an integer value between 1-2500.
*   The image size cannot exceed 25MB.
*   The image resolution cannot exceed 50MP.


### Supported image formats

| Format | Extension | Source | Result |
| ------ | --------- | ------ | ------ |
| PNG    | `png`     | ☑️     | ☑️     |
| JPEG   | `jpg`     | ☑️     | ☑️     |
| WebP   | `webp`    | ☑️     | ☑️     |
| AVIF   | `avif`    | ☑️     | ☑️     |
| GIF    | `gif`     | ☑️     | ☑️     |
| ICO    | `ico`     | ☑️     | ☑️     |
| SVG    | `svg`     | ☑️     | ☑️     |
| HEIC   | `heic`    | ☑️     | ❌      |
| BMP    | `bmp`     | ☑️     | ☑️     |
| TIFF   | `tiff`    | ☑️     | ☑️     |



## Pricing

<Price price="5" /> per 1,000 origin images. You are only charged for usage exceeding your subscription
plan's quota.

<Admonition type="note">
  The count resets at the start of each billing cycle.
</Admonition>

| Plan       | Quota  | Over-Usage                                  |
| ---------- | ------ | ------------------------------------------- |
| Pro        | 100    | <Price price="5" /> per 1,000 origin images |
| Team       | 100    | <Price price="5" /> per 1,000 origin images |
| Enterprise | Custom | Custom                                      |

For a detailed breakdown of how charges are calculated, refer to [Manage Storage Image Transformations usage](/docs/guides/platform/manage-your-usage/storage-image-transformations).



## Self hosting

Our solution to image resizing and optimization can be self-hosted as with any other Supabase product. Under the hood we use [imgproxy](https://imgproxy.net/)


#### imgproxy configuration:

Deploy an imgproxy container with the following configuration:

```yaml
imgproxy:
  image: darthsim/imgproxy
  environment:
    - IMGPROXY_ENABLE_WEBP_DETECTION=true
    - IMGPROXY_JPEG_PROGRESSIVE=true
```

Note: make sure that this service can only be reachable within an internal network and not exposed to the public internet


#### Storage API configuration:

Once [imgproxy](https://imgproxy.net/) is deployed we need to configure a couple of environment variables in your self-hosted [`storage-api`](https://github.com/supabase/storage-api) service as follows:

```shell
ENABLE_IMAGE_TRANSFORMATION=true
IMGPROXY_URL=yourinternalimgproxyurl.internal.com
```

{/* Finish with a video. This also appears in the Sidebar via the "tocVideo" metadata */}

<div className="video-container">
  <iframe src="https://www.youtube-nocookie.com/embed/dLqSmxX3r7I" frameBorder="1" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />
</div>



# Storage Access Control



Supabase Storage is designed to work perfectly with Postgres [Row Level Security](/docs/guides/database/postgres/row-level-security) (RLS).

You can use RLS to create [Security Access Policies](https://www.postgresql.org/docs/current/sql-createpolicy.html) that are incredibly powerful and flexible, allowing you to restrict access based on your business needs.



## Access policies

By default Storage does not allow any uploads to buckets without RLS policies. You selectively allow certain operations by creating RLS policies on the `storage.objects` table.

You can find the documentation for the storage schema [here](/docs/guides/storage/schema/design) , and to simplify the process of crafting your policies, you can utilize these [helper functions](/docs/guides/storage/schema/helper-functions) .

<Admonition type="note">
  The RLS policies required for different operations are documented [here](/docs/reference/javascript/storage-createbucket)
</Admonition>

For example, the only RLS policy required for [uploading](/docs/reference/javascript/storage-from-upload) objects is to grant the `INSERT` permission to the `storage.objects` table.

To allow overwriting files using the `upsert` functionality you will need to additionally grant `SELECT` and `UPDATE` permissions.



## Policy examples

An easy way to get started would be to create RLS policies for `SELECT`, `INSERT`, `UPDATE`, `DELETE` operations and restrict the policies to meet your security requirements. For example, one can start with the following `INSERT` policy:

```sql
create policy "policy_name"
ON storage.objects
for insert with check (
  true
);
```

and modify it to only allow authenticated users to upload assets to a specific bucket by changing it to:

```sql
create policy "policy_name"
on storage.objects for insert to authenticated with check (
    -- restrict bucket
    bucket_id = 'my_bucket_id'
);
```

This example demonstrates how you would allow authenticated users to upload files to a folder called `private` inside `my_bucket_id`:

```sql
create policy "Allow authenticated uploads"
on storage.objects
for insert
to authenticated
with check (
  bucket_id = 'my_bucket_id' and
  (storage.foldername(name))[1] = 'private'
);
```

This example demonstrates how you would allow authenticated users to upload files to a folder called with their `users.id` inside `my_bucket_id`:

```sql
create policy "Allow authenticated uploads"
on storage.objects
for insert
to authenticated
with check (
  bucket_id = 'my_bucket_id' and
  (storage.foldername(name))[1] = (select auth.uid()::text)
);
```

Allow a user to access a file that was previously uploaded by the same user:

```sql
create policy "Individual user Access"
on storage.objects for select
to authenticated
using ( (select auth.uid()) = owner_id::uuid );
```

***

{/* Finish with a video. This also appears in the Sidebar via the "tocVideo" metadata */}

<div className="video-container">
  <iframe src="https://www.youtube-nocookie.com/embed/4ERX__Y908k" frameBorder="1" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />
</div>



## Bypassing access controls

If you exclusively use Storage from trusted clients, such as your own servers, and need to bypass the RLS policies, you can use the `service key` in the `Authorization` header. Service keys entirely bypass RLS policies, granting you unrestricted access to all Storage APIs.

Remember you should not share the service key publicly.



# Ownership



When creating new buckets or objects in Supabase Storage, an owner is automatically assigned to the bucket or object. The owner is the user who created the resource and the value is derived from the `sub` claim in the JWT.
We store the `owner` in the `owner_id` column.

<Admonition type="note">
  When using the `service_key` to create a resource, the owner will not be set and the resource will be owned by anyone. This is also the case when you are creating Storage resources via the Dashboard.
</Admonition>

<Admonition type="note">
  The Storage schema has 2 fields to represent ownership: `owner` and `owner_id`. `owner` is deprecated and will be removed. Use `owner_id` instead.
</Admonition>



## Access control

By itself, the ownership of a resource does not provide any access control. However, you can enforce the ownership by implementing access control against storage resources scoped to their owner.

For example, you can implement a policy where only the owner of an object can delete it. To do this, check the `owner_id` field of the object and compare it with the `sub` claim of the JWT:

```sql
create policy "User can delete their own objects"
on storage.objects
for delete
to authenticated
using (
    owner_id = (select auth.uid())
);
```

The use of RLS policies is just one way to enforce access control. You can also implement access control in your server code by following the same pattern.



# Custom Roles

Learn about using custom roles with storage schema

In this guide, you will learn how to create and use custom roles with Storage to manage role-based access to objects and buckets. The same approach can be used to use custom roles with any other Supabase service.

Supabase Storage uses the same role-based access control system as any other Supabase service using RLS (Row Level Security).



## Create a custom role

Let's create a custom role `manager` to provide full read access to a specific bucket. For a more advanced setup, see the [RBAC Guide](/docs/guides/auth/custom-claims-and-role-based-access-control-rbac#create-auth-hook-to-apply-user-role).

```sql
create role 'manager';

-- Important to grant the role to the authenticator and anon role
grant manager to authenticator;
grant anon to manager;
```



## Create a policy

Let's create a policy that gives full read permissions to all objects in the bucket `teams` for the `manager` role.

```sql
create policy "Manager can view all files in the bucket 'teams'"
on storage.objects
for select
to manager
using (
 bucket_id = 'teams'
);
```



## Test the policy

To impersonate the `manager` role, you will need a valid JWT token with the `manager` role.
You can quickly create one using the `jsonwebtoken` library in Node.js.

<Admonition type="danger">
  Signing a new JWT requires your `JWT_SECRET`. You must store this secret securely. Never expose it in frontend code, and do not check it into version control.
</Admonition>

```js
const jwt = require('jsonwebtoken')

const JWT_SECRET = 'your-jwt-secret' // You can find this in your Supabase project settings under API. Store this securely.
const USER_ID = '' // the user id that we want to give the manager role

const token = jwt.sign({ role: 'manager', sub: USER_ID }, JWT_SECRET, {
  expiresIn: '1h',
})
```

Now you can use this token to access the Storage API.

```js
const { StorageClient } = require('@supabase/storage-js')

const PROJECT_URL = 'https://your-project-id.supabase.co/storage/v1'

const storage = new StorageClient(PROJECT_URL, {
  authorization: `Bearer ${token}`,
})

await storage.from('teams').list()
```



# The Storage Schema

Learn about the storage schema

Storage uses Postgres to store metadata regarding your buckets and objects. Users can use RLS (Row-Level Security) policies for access control. This data is stored in a dedicated schema within your project called `storage`.

<Admonition type="note">
  When working with SQL, it's crucial to consider all records in Storage tables as read-only. All operations, including uploading, copying, moving, and deleting, should **exclusively go through the API**.

  This is important because the storage schema only stores the metadata and the actual objects are stored in a provider like S3. Deleting the metadata doesn't remove the object in the underlying storage provider. This results in your object being inaccessible, but you'll still be billed for it.
</Admonition>

Here is the schema that represents the Storage service:

<img alt="Storage schema design" src="/docs/img/storage/schema-design.png" />

You have the option to query this table directly to retrieve information about your files in Storage without the need to go through our API.



## Modifying the schema

We strongly recommend refraining from making any alterations to the `storage` schema and treating it as read-only. This approach is important because any modifications to the schema on your end could potentially clash with our future updates, leading to downtime.

However, we encourage you to add custom indexes as they can significantly improve the performance of the RLS policies you create for enforcing access control.



---
**Navigation:** [← Previous](./01-ai-vectors.md) | [Index](./index.md) | [Next →](./03-storage-helper-functions.md)
