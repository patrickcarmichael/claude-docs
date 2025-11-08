**Navigation:** ← Previous | [Index](./index.md) | [Next →](./02-metrics.md)

# AI & Vectors

The best vector database is the database you already have.

Supabase provides an open source toolkit for developing AI applications using Postgres and pgvector. Use the Supabase client libraries to store, index, and query your vector embeddings at scale.

The toolkit includes:

*   A [vector store](/docs/guides/ai/vector-columns) and embeddings support using Postgres and pgvector.
*   A [Python client](/docs/guides/ai/vecs-python-client) for managing unstructured embeddings.
*   An [embedding generation](/docs/guides/ai/quickstarts/generate-text-embeddings) process using open source models directly in Edge Functions.
*   [Database migrations](/docs/guides/ai/examples/headless-vector-search#prepare-your-database) for managing structured embeddings.
*   Integrations with all popular AI providers, such as [OpenAI](/docs/guides/ai/examples/openai), [Hugging Face](/docs/guides/ai/hugging-face), [LangChain](/docs/guides/ai/langchain), and more.



## Search

You can use Supabase to build different types of search features for your app, including:

*   [Semantic search](/docs/guides/ai/semantic-search): search by meaning rather than exact keywords
*   [Keyword search](/docs/guides/ai/keyword-search): search by words or phrases
*   [Hybrid search](/docs/guides/ai/hybrid-search): combine semantic search with keyword search



## Examples

Check out all of the AI [templates and examples](https://github.com/supabase/supabase/tree/master/examples/ai) in our GitHub repository.

{/* <!-- vale off --> */}

<div className="grid md:grid-cols-12 gap-4 not-prose">
  {examples.map((x) => (
        <div className="col-span-4" key={x.href}>
          <Link href={x.href} passHref>
            <GlassPanel icon={'/docs/img/icons/github-icon'} hasLightIcon={true} title={x.name}>
              {x.description}
            </GlassPanel>
          </Link>
        </div>
      ))}
</div>

export const examples = [
  {
    name: 'Headless Vector Search',
    description: 'A toolkit to perform vector similarity search on your knowledge base embeddings.',
    href: '/guides/ai/examples/headless-vector-search',
  },
  {
    name: 'Image Search with OpenAI CLIP',
    description: 'Implement image search with the OpenAI CLIP Model and Supabase Vector.',
    href: '/guides/ai/examples/image-search-openai-clip',
  },
  {
    name: 'Hugging Face inference',
    description: 'Generate image captions using Hugging Face.',
    href: '/guides/ai/examples/huggingface-image-captioning',
  },
  {
    name: 'OpenAI completions',
    description: 'Generate GPT text completions using OpenAI in Edge Functions.',
    href: '/guides/ai/examples/openai',
  },
  {
    name: 'Building ChatGPT Plugins',
    description: 'Use Supabase as a Retrieval Store for your ChatGPT plugin.',
    href: '/guides/ai/examples/building-chatgpt-plugins',
  },
  {
    name: 'Vector search with Next.js and OpenAI',
    description:
      'Learn how to build a ChatGPT-style doc search powered by Next.js, OpenAI, and Supabase.',
    href: '/guides/ai/examples/nextjs-vector-search',
  },
]

{/* <!-- vale on --> */}



## Integrations

{/* <!-- vale off --> */}

<div className="grid md:grid-cols-12 gap-4 not-prose">
  {integrations.map((x) => (
        <div className="col-span-4" key={x.href}>
          <Link href={x.href} passHref>
            <GlassPanel title={x.name}>{x.description}</GlassPanel>
          </Link>
        </div>
      ))}
</div>

export const integrations = [
  {
    name: 'OpenAI',
    description:
      'OpenAI is an AI research and deployment company. Supabase provides a simple way to use OpenAI in your applications.',
    href: '/guides/ai/examples/building-chatgpt-plugins',
  },
  {
    name: 'Amazon Bedrock',
    description:
      'A fully managed service that offers a choice of high-performing foundation models from leading AI companies.',
    href: '/guides/ai/integrations/amazon-bedrock',
  },
  {
    name: 'Hugging Face',
    description:
      "Hugging Face is an open-source provider of NLP technologies. Supabase provides a simple way to use Hugging Face's models in your applications.",
    href: '/guides/ai/hugging-face',
  },
  {
    name: 'LangChain',
    description:
      'LangChain is a language-agnostic, open-source, and self-hosted API for text translation, summarization, and sentiment analysis.',
    href: '/guides/ai/langchain',
  },
  {
    name: 'LlamaIndex',
    description: 'LlamaIndex is a data framework for your LLM applications.',
    href: '/guides/ai/integrations/llamaindex',
  },
]

{/* <!-- vale on --> */}



## Case studies

{/* <!-- vale off --> */}

<div className="grid md:grid-cols-12 gap-4 not-prose">
  {[
        {
          name: 'Berri AI Boosts Productivity by Migrating from AWS RDS to Supabase with pgvector',
          description:
            'Learn how Berri AI overcame challenges with self-hosting their vector database on AWS RDS and successfully migrated to Supabase.',
          href: 'https://supabase.com/customers/berriai',
        },
        {
          name: 'Firecrawl switches from Pinecone to Supabase for PostgreSQL vector embeddings',
          description:
            'How Firecrawl boosts efficiency and accuracy of chat powered search for documentation using Supabase with pgvector',
          href: 'https://supabase.com/customers/firecrawl',
        },
        {
          name: 'Markprompt: GDPR-Compliant AI Chatbots for Docs and Websites',
          description:
            "AI-powered chatbot platform, Markprompt, empowers developers to deliver efficient and GDPR-compliant prompt experiences on top of their content, by leveraging Supabase's secure and privacy-focused database and authentication solutions",
          href: 'https://supabase.com/customers/markprompt',
        },
      ].map((x) => (
        <div className="col-span-4" key={x.href}>
          <Link href={x.href} passHref>
            <GlassPanel title={x.name}>{x.description}</GlassPanel>
          </Link>
        </div>
      ))}
</div>

{/* <!-- vale on --> */}



# REST API



Supabase auto-generates an API directly from your database schema allowing you to connect to your database through a restful interface, directly from the browser.

The API is auto-generated from your database and is designed to get you building as fast as possible, without writing a single line of code.

You can use them directly from the browser (two-tier architecture), or as a complement to your own API server (three-tier architecture).



## Features \[#rest-api-overview]

Supabase provides a RESTful API using [PostgREST](https://postgrest.org/). This is a very thin API layer on top of Postgres.
It exposes everything you need from a CRUD API at the URL `https://<project_ref>.supabase.co/rest/v1/`.

The REST interface is automatically reflected from your database's schema and is:

*   **Instant and auto-generated.** <br />As you update your database the changes are immediately accessible through your API.
*   **Self documenting.** <br />Supabase generates documentation in the Dashboard which updates as you make database changes.
*   **Secure.** <br />The API is configured to work with PostgreSQL's Row Level Security, provisioned behind an API gateway with key-auth enabled.
*   **Fast.** <br />Our benchmarks for basic reads are more than 300% faster than Firebase. The API is a very thin layer on top of Postgres, which does most of the heavy lifting.
*   **Scalable.** <br />The API can serve thousands of simultaneous requests, and works well for Serverless workloads.

The reflected API is designed to retain as much of Postgres' capability as possible including:

*   Basic CRUD operations (Create/Read/Update/Delete)
*   Arbitrarily deep relationships among tables/views, functions that return table types can also nest related tables/views.
*   Works with Postgres Views, Materialized Views and Foreign Tables
*   Works with Postgres Functions
*   User defined computed columns and computed relationships
*   The Postgres security model - including Row Level Security, Roles, and Grants.

The REST API resolves all requests to a single SQL statement leading to fast response times and high throughput.

Reference:

*   [Docs](https://postgrest.org/)
*   [Source Code](https://github.com/PostgREST/postgrest)



## API URL and keys

You can find the API URL and Keys in the [Dashboard](/dashboard/project/_/settings/api-keys).



# Auth

Use Supabase to authenticate and authorize your users.

Supabase Auth makes it easy to implement authentication and authorization in your app. We provide client SDKs and API endpoints to help you create and manage users.

Your users can use many popular Auth methods, including password, magic link, one-time password (OTP), social login, and single sign-on (SSO).



## About authentication and authorization

Authentication and authorization are the core responsibilities of any Auth system.

*   **Authentication** means checking that a user is who they say they are.
*   **Authorization** means checking what resources a user is allowed to access.

Supabase Auth uses [JSON Web Tokens (JWTs)](/docs/guides/auth/jwts) for authentication. For a complete reference of all JWT fields, see the [JWT Fields Reference](/docs/guides/auth/jwt-fields). Auth integrates with Supabase's database features, making it easy to use [Row Level Security (RLS)](/docs/guides/database/postgres/row-level-security) for authorization.



## The Supabase ecosystem

You can use Supabase Auth as a standalone product, but it's also built to integrate with the Supabase ecosystem.

Auth uses your project's Postgres database under the hood, storing user data and other Auth information in a special schema. You can connect this data to your own tables using triggers and foreign key references.

Auth also enables access control to your database's automatically generated [REST API](/docs/guides/api). When using Supabase SDKs, your data requests are automatically sent with the user's Auth Token. The Auth Token scopes database access on a row-by-row level when used along with [RLS policies](/docs/guides/database/postgres/row-level-security).



## Providers

Supabase Auth works with many popular Auth methods, including Social and Phone Auth using third-party providers. See the following sections for a list of supported third-party providers.


### Social Auth

<AuthProviders type="social" />


### Phone Auth

<AuthProviders type="phone" />



## Pricing

Charges apply to Monthly Active Users (MAU), Monthly Active Third-Party Users (Third-Party MAU), and Monthly Active SSO Users (SSO MAU) and Advanced MFA Add-ons. For a detailed breakdown of how these charges are calculated, refer to the following pages:

*   [Pricing MAU](/docs/guides/platform/manage-your-usage/monthly-active-users)
*   [Pricing Third-Party MAU](/docs/guides/platform/manage-your-usage/monthly-active-users-third-party)
*   [Pricing SSO MAU](/docs/guides/platform/manage-your-usage/monthly-active-users-sso)
*   [Advanced MFA - Phone](/docs/guides/platform/manage-your-usage/advanced-mfa-phone)



# Local Dev with CLI

Developing locally using the Supabase CLI.

You can use the Supabase CLI to run the entire Supabase stack locally on your machine, by running `supabase init` and then `supabase start`. To install the CLI, see the [installation guide](/docs/guides/cli/getting-started#installing-the-supabase-cli).

The Supabase CLI provides tools to develop your project locally, deploy to the Supabase Platform, handle database migrations, and generate types directly from your database schema.



## Resources

<div className="grid md:grid-cols-12 gap-4 not-prose">
  {[
        {
          name: 'Supabase CLI',
          description:
            'The Supabase CLI provides tools to develop manage your Supabase projects from your local machine.',
          href: 'https://github.com/supabase/cli',
        },
        {
          name: 'GitHub Action',
          description: ' A GitHub action for interacting with your Supabase projects using the CLI.',
          href: 'https://github.com/supabase/setup-cli',
        },
      ].map((x) => (
        <div className="col-span-6" key={x.href}>
          <Link href={x.href} passHref>
            <GlassPanel icon={'/docs/img/icons/github-icon'} hasLightIcon={true} title={x.name}>
              {x.description}
            </GlassPanel>
          </Link>
        </div>
      ))}
</div>



# Cron

Schedule Recurring Jobs with Cron Syntax in Postgres

Supabase Cron is a Postgres Module that simplifies scheduling recurring Jobs with cron syntax and monitoring Job runs inside Postgres.

Cron Jobs can be created via SQL or the [Integrations -> Cron](/dashboard/project/_/integrations) interface inside the Dashboard, and can run anywhere from every second to once a year depending on your use case.

<Image
  alt="Manage cron jobs via the Dashboard"
  src={{
    dark: '/docs/img/guides/cron/cron.jpg',
    light: '/docs/img/guides/cron/cron--light.jpg',
  }}
/>

Every Job can run SQL snippets or database functions with zero network latency or make an HTTP request, such as invoking a Supabase Edge Function, with ease.

<Admonition type="note">
  For best performance, we recommend no more than 8 Jobs run concurrently. Each Job should run no more than 10 minutes.
</Admonition>



## How does Cron work?

Under the hood, Supabase Cron uses the [`pg_cron`](https://github.com/citusdata/pg_cron) Postgres database extension which is the scheduling and execution engine for your Jobs.

The extension creates a `cron` schema in your database and all Jobs are stored on the `cron.job` table. Every Job's run and its status is recorded on the `cron.job_run_details` table.

The Supabase Dashboard provides an interface for you to schedule Jobs and monitor Job runs. You can also do the same with SQL.



## Resources

*   [`pg_cron` GitHub Repository](https://github.com/citusdata/pg_cron)



# Deployment



Deploying your app makes it live and accessible to users. Usually, you will deploy an app to at least two environments: a production environment for users and (one or multiple) staging or preview environments for developers.

Supabase provides several options for environment management and deployment.



## Environment management

You can maintain separate development, staging, and production environments for Supabase:

*   **Development**: Develop with a local Supabase stack using the [Supabase CLI](/docs/guides/local-development).
*   **Staging**: Use [branching](/docs/guides/deployment/branching) to create staging or preview environments. You can use persistent branches for a long-lived staging setup, or ephemeral branches for short-lived previews (which are often tied to a pull request).
*   **Production**: If you have branching enabled, you can use the Supabase GitHub integration to automatically push your migration files when you merge a pull request. Alternatively, you can set up your own continuous deployment pipeline using the Supabase CLI.

<Admonition type="tip" title="Self-hosting">
  See the [self-hosting guides](/docs/guides/self-hosting) for instructions on hosting your own Supabase stack.
</Admonition>



## Deployment

You can automate deployments using:

*   The [Supabase GitHub integration](/dashboard/project/_/settings/integrations) (with branching enabled)
*   The [Supabase CLI](/docs/guides/local-development) in your own continuous deployment pipeline
*   The [Supabase Terraform provider](/docs/guides/deployment/terraform)



# Edge Functions

Globally distributed TypeScript functions.

Edge Functions are server-side TypeScript functions, distributed globally at the edge—close to your users. They can be used for listening to webhooks or integrating your Supabase project with third-parties [like Stripe](https://github.com/supabase/supabase/tree/master/examples/edge-functions/supabase/functions/stripe-webhooks). Edge Functions are developed using [Deno](https://deno.com), which offers a few benefits to you as a developer:

*   It is open source.
*   It is portable. Supabase Edge Functions run locally, and on any other Deno-compatible platform (including self-hosted infrastructure).
*   It is TypeScript first and supports WASM.
*   Edge Functions are globally distributed for low-latency.



## How it works

*   **Request enters an edge gateway (relay)** — the gateway routes traffic, handles auth headers/JWT validation, and applies routing/traffic rules.
*   **Auth & policies are applied** — the gateway (or your function) can validate Supabase JWTs, apply rate-limits, and centralize security checks before executing code.
*   **[Edge runtime](https://github.com/supabase/edge-runtime) executes your function** — the function runs on a regionally-distributed Edge Runtime node closest to the user for minimal latency.
*   **Integrations & data access** — functions commonly call Supabase APIs (Auth, Postgres, Storage) or third-party APIs. For Postgres, prefer connection strategies suited for edge/serverless environments (see the `connect-to-postgres` guide).
*   **Observability and logs** — invocations emit logs and metrics you can explore in the dashboard or downstream monitoring (Sentry, etc.).
*   **Response returns via the gateway** — the gateway forwards the response back to the client and records request metadata.



## Quick technical notes

*   **Runtime:** Supabase Edge Runtime (Deno compatible runtime with TypeScript first). Functions are simple `.ts` files that export a handler.
*   **Local dev parity:** Use Supabase CLI for a local runtime similar to production for faster iteration (`supabase functions serve` command).
*   **Global deployment:** Deploy your Edge Functions via Supabase Dashboard, CLI or MCP.
*   **Cold starts & concurrency:** cold starts are possible — design for short-lived, idempotent operations. Heavy long-running jobs should be moved to [background workers](/docs/guides/functions/background-tasks).
*   **Database connections:** treat Postgres like a remote, pooled service — use connection pools or serverless-friendly drivers.
*   **Secrets:** store credentials in Supabase [project secrets](/docs/reference/cli/supabase-secrets) and access them via environment variables.



## When to use Edge Functions

*   Authenticated or public HTTP endpoints that need low latency.
*   Webhook receivers (Stripe, GitHub, etc.).
*   On-demand image or Open Graph generation.
*   Small AI inference tasks or orchestrating calls to external LLM APIs (like OpenAI)
*   Sending transactional emails.
*   Building messaging bots for Slack, Discord, etc.

<div className="not-prose">
  <Button size="medium" asChild>
    <a href="/docs/guides/functions/quickstart">Get started</a>
  </Button>
</div>



## Examples

Check out the [Edge Function Examples](https://github.com/supabase/supabase/tree/master/examples/edge-functions) in our GitHub repository.

<div className="grid md:grid-cols-12 gap-4 not-prose">
  {[
        {
          name: 'With supabase-js',
          description: 'Use the Supabase client inside your Edge Function.',
          href: '/guides/functions/auth',
        },
        {
          name: 'Type-Safe SQL with Kysely',
          description:
            'Combining Kysely with Deno Postgres gives you a convenient developer experience for interacting directly with your Postgres database.',
          href: '/guides/functions/kysely-postgres',
        },
        {
          name: 'Monitoring with Sentry',
          description: 'Monitor Edge Functions with the Sentry Deno SDK.',
          href: '/guides/functions/examples/sentry-monitoring',
        },
        {
          name: 'With CORS headers',
          description: 'Send CORS headers for invoking from the browser.',
          href: '/guides/functions/cors',
        },
        {
          name: 'React Native with Stripe',
          description: 'Full example for using Supabase and Stripe, with Expo.',
          href: 'https://github.com/supabase-community/expo-stripe-payments-with-supabase-functions',
        },
        {
          name: 'Flutter with Stripe',
          description: 'Full example for using Supabase and Stripe, with Flutter.',
          href: 'https://github.com/supabase-community/flutter-stripe-payments-with-supabase-functions',
        },
        {
          name: 'Building a RESTful Service API',
          description:
            'Learn how to use HTTP methods and paths to build a RESTful service for managing tasks.',
          href: 'https://github.com/supabase/supabase/blob/master/examples/edge-functions/supabase/functions/restful-tasks/index.ts',
        },
        {
          name: 'Working with Supabase Storage',
          description: 'An example on reading a file from Supabase Storage.',
          href: 'https://github.com/supabase/supabase/blob/master/examples/edge-functions/supabase/functions/read-storage/index.ts',
        },
        {
          name: 'Open Graph Image Generation',
          description: 'Generate Open Graph images with Deno and Supabase Edge Functions.',
          href: '/guides/functions/examples/og-image',
        },
        {
          name: 'OG Image Generation & Storage CDN Caching',
          description: 'Cache generated images with Supabase Storage CDN.',
          href: 'https://github.com/supabase/supabase/tree/master/examples/edge-functions/supabase/functions/og-image-with-storage-cdn',
        },
        {
          name: 'Get User Location',
          description: `Get user location data from user's IP address.`,
          href: 'https://github.com/supabase/supabase/tree/master/examples/edge-functions/supabase/functions/location',
        },
        {
          name: 'Cloudflare Turnstile',
          description: `Protecting Forms with Cloudflare Turnstile.`,
          href: '/guides/functions/examples/cloudflare-turnstile',
        },
        {
          name: 'Connect to Postgres',
          description: `Connecting to Postgres from Edge Functions.`,
          href: '/guides/functions/connect-to-postgres',
        },
        {
          name: 'GitHub Actions',
          description: `Deploying Edge Functions with GitHub Actions.`,
          href: '/guides/functions/examples/github-actions',
        },
        {
          name: 'Oak Server Middleware',
          description: `Request Routing with Oak server middleware.`,
          href: 'https://github.com/supabase/supabase/tree/master/examples/edge-functions/supabase/functions/oak-server',
        },
        {
          name: 'Hugging Face',
          description: `Access 100,000+ Machine Learning models.`,
          href: '/guides/ai/examples/huggingface-image-captioning',
        },
        {
          name: 'Amazon Bedrock',
          description: `Amazon Bedrock Image Generator`,
          href: '/guides/functions/examples/amazon-bedrock-image-generator',
        },
        {
          name: 'OpenAI',
          description: `Using OpenAI in Edge Functions.`,
          href: '/guides/ai/examples/openai',
        },
        {
          name: 'Stripe Webhooks',
          description: `Handling signed Stripe Webhooks with Edge Functions.`,
          href: '/guides/functions/examples/stripe-webhooks',
        },
        {
          name: 'Send emails',
          description: `Send emails in Edge Functions with Resend.`,
          href: '/guides/functions/examples/send-emails',
        },
        {
          name: 'Web Stream',
          description: `Server-Sent Events in Edge Functions.`,
          href: 'https://github.com/supabase/supabase/tree/master/examples/edge-functions/supabase/functions/streams',
        },
        {
          name: 'Puppeteer',
          description: `Generate screenshots with Puppeteer.`,
          href: '/guides/functions/examples/screenshots',
        },
        {
          name: 'Discord Bot',
          description: `Building a Slash Command Discord Bot with Edge Functions.`,
          href: '/guides/functions/examples/discord-bot',
        },
        {
          name: 'Telegram Bot',
          description: `Building a Telegram Bot with Edge Functions.`,
          href: '/guides/functions/examples/telegram-bot',
        },
        {
          name: 'Upload File',
          description: `Process multipart/form-data.`,
          href: 'https://github.com/supabase/supabase/tree/master/examples/edge-functions/supabase/functions/file-upload-storage',
        },
        {
          name: 'Upstash Redis',
          description: `Build an Edge Functions Counter with Upstash Redis.`,
          href: '/guides/functions/examples/upstash-redis',
        },
        {
          name: 'Rate Limiting',
          description: `Rate Limiting Edge Functions with Upstash Redis.`,
          href: '/guides/functions/examples/rate-limiting',
        },
        {
          name: 'Slack Bot Mention Edge Function',
          description: `Slack Bot handling Slack mentions in Edge Function`,
          href: '/guides/functions/examples/slack-bot-mention',
        },
      ].map((x) => (
        <div className="col-span-4" key={x.href}>
          <Link href={x.href} passHref>
            <GlassPanel icon={'/docs/img/icons/github-icon'} hasLightIcon={true} title={x.name}>
              {x.description}
            </GlassPanel>
          </Link>
        </div>
      ))}
</div>



# Getting Started



<div className="flex flex-col gap-12 my-12">
  <div>
    <div className="grid grid-cols-12 gap-6 not-prose">
      {[
                  {
                    title: 'Features',
                    hasLightIcon: true,
                    href: '/guides/getting-started/features',
                    description: 'A non-exhaustive list of features that Supabase provides for every project.'
                  },
                  {
                    title: 'Architecture',
                    hasLightIcon: true,
                    href: '/guides/getting-started/architecture',
                    description: "An overview of Supabase's architecture and product principles.",
                  },
                  {
                    title: 'Local Development',
                    hasLightIcon: true,
                    href: '/guides/cli/getting-started',
                    description: 'Use the Supabase CLI to develop locally and collaborate between teams.',
                  }
                ].map((resource) => {
                  return (
                    <Link
                      href={`${resource.href}`}
                      key={resource.title}
                      className={'col-span-12 md:col-span-4'}
                      passHref
                    >
                      <GlassPanel {...resource} background={false} showIconBg={true}>
                        {resource.description}
                      </GlassPanel>
                    </Link>
                  )

            })}
    </div>
  </div>
</div>


### Use cases

<div className="grid lg:grid-cols-12 gap-6 not-prose">
  {[
        {
          title: 'AI, Vectors, and embeddings',
          href: '/guides/ai#examples',
          description: `Build AI-enabled applications using our Vector toolkit.`,
          icon: '/docs/img/icons/openai_logo',
          hasLightIcon: true,
        },
        {
          title: 'Subscription Payments (SaaS)',
          href: 'https://github.com/vercel/nextjs-subscription-payments#nextjs-subscription-payments-starter',
          description: `Clone, deploy, and fully customize a SaaS subscription application with Next.js.`,
          icon: '/docs/img/icons/nextjs-icon',
        },
        {
          title: 'Partner Gallery',
          href: 'https://github.com/supabase-community/partner-gallery-example#supabase-partner-gallery-example',
          description: `Postgres full-text search, image storage, and more.`,
          icon: '/docs/img/icons/nextjs-icon',
        },
      ].map((item) => {
        return (
          <Link href={`${item.href}`} key={item.title} passHref className={'col-span-4'}>
            <GlassPanel
              title={item.title}
              span="col-span-6"
              background={false}
              icon={item.icon}
              hasLightIcon={item.hasLightIcon}
            >
              {item.description}
            </GlassPanel>
          </Link>
        )
      })}
</div>


### Framework quickstarts

<div className="grid lg:grid-cols-12 gap-6 not-prose">
  {[
        {
          title: 'React',
          href: '/guides/getting-started/quickstarts/reactjs',
          description:
            'Learn how to create a Supabase project, add some sample data to your database, and query the data from a React app.',
          icon: '/docs/img/icons/react-icon',
          enabled: isFeatureEnabled('docs:framework_quickstarts'),
        },
        {
          title: 'Next.js',
          href: '/guides/getting-started/quickstarts/nextjs',
          description:
            'Learn how to create a Supabase project, add some sample data to your database, and query the data from a Next.js app.',
          icon: '/docs/img/icons/nextjs-icon',
          hasLightIcon: true,
          enabled: isFeatureEnabled('docs:framework_quickstarts'),
        },
        {
          title: 'Nuxt',
          href: '/guides/getting-started/quickstarts/nuxtjs',
          description:
            'Learn how to create a Supabase project, add some sample data to your database, and query the data from a Nuxt app.',
          icon: '/docs/img/icons/nuxt-icon',
          enabled: isFeatureEnabled('docs:framework_quickstarts'),
        },
        {
          title: 'Hono',
          href: '/guides/getting-started/quickstarts/hono',
          description:
            'Learn how to create a Supabase project, add some sample data to your database, secure it with auth, and query the data from a Hono app.',
          icon: '/docs/img/icons/hono-icon',
          enabled: isFeatureEnabled('docs:framework_quickstarts'),
        },
        {
          title: 'RedwoodJS',
          href: '/guides/getting-started/quickstarts/redwoodjs',
          description:
            'Learn how to create a Supabase project, add some sample data to your database using Prisma migration and seeds, and query the data from a RedwoodJS app.',
          icon: '/docs/img/icons/redwood-icon',
          enabled: isFeatureEnabled('docs:framework_quickstarts'),
        },
        {
          title: 'Flutter',
          href: '/guides/getting-started/quickstarts/flutter',
          description:
            'Learn how to create a Supabase project, add some sample data to your database, and query the data from a Flutter app.',
          icon: '/docs/img/icons/flutter-icon',
          enabled: isFeatureEnabled('sdk:dart'),
        },
        {
          title: 'iOS SwiftUI',
          href: '/guides/getting-started/quickstarts/ios-swiftui',
          description:
            'Learn how to create a Supabase project, add some sample data to your database, and query the data from an iOS app.',
          icon: '/docs/img/icons/swift-icon',
          enabled: isFeatureEnabled('sdk:swift'),
        },
        {
          title: 'Android Kotlin',
          href: '/guides/getting-started/quickstarts/kotlin',
          description:
            'Learn how to create a Supabase project, add some sample data to your database, and query the data from an Android Kotlin app.',
          icon: '/docs/img/icons/kotlin-icon',
          enabled: isFeatureEnabled('sdk:kotlin'),
        },
        {
          title: 'SvelteKit',
          href: '/guides/getting-started/quickstarts/sveltekit',
          description:
            'Learn how to create a Supabase project, add some sample data to your database, and query the data from a SvelteKit app.',
          icon: '/docs/img/icons/svelte-icon',
          enabled: isFeatureEnabled('docs:framework_quickstarts'),
        },
        {
          title: 'SolidJS',
          href: '/guides/getting-started/quickstarts/solidjs',
          description:
            'Learn how to create a Supabase project, add some sample data to your database, and query the data from a SolidJS app.',
          icon: '/docs/img/icons/solidjs-icon',
          enabled: isFeatureEnabled('docs:framework_quickstarts'),
        },
        {
          title: 'Vue',
          href: '/guides/getting-started/quickstarts/vue',
          description:
            'Learn how to create a Supabase project, add some sample data to your database, and query the data from a Vue app.',
          icon: '/docs/img/icons/vuejs-icon',
          enabled: isFeatureEnabled('docs:framework_quickstarts'),
        },
        {
          title: 'refine',
          href: '/guides/getting-started/quickstarts/refine',
          description:
            'Learn how to create a Supabase project, add some sample data to your database, and query the data from a refine app.',
          icon: '/docs/img/icons/refine-icon',
          enabled: isFeatureEnabled('docs:framework_quickstarts'),
        },
      ]
        .filter((item) => item.enabled !== false)
        .map((item) => {
          return (
            <Link href={`${item.href}`} key={item.title} passHref className={'col-span-4'}>
              <GlassPanel
                title={item.title}
                span="col-span-6"
                background={false}
                icon={item.icon}
                hasLightIcon={item.hasLightIcon}
              >
                {item.description}
              </GlassPanel>
            </Link>
          )
        })}
</div>


### Web app demos

<div className="grid lg:grid-cols-12 gap-6 not-prose">
  {
      [
        {
          title: 'Next.js',
          href: '/guides/getting-started/tutorials/with-nextjs',
          description:
            'Learn how to build a user management app with Next.js and Supabase Database, Auth, and Storage functionality.',
          icon: '/docs/img/icons/nextjs-icon',
          hasLightIcon: true,
        },
        {
          title: 'React',
          href: '/guides/getting-started/tutorials/with-react',
          description:
            'Learn how to build a user management app with React and Supabase Database, Auth, and Storage functionality.',
          icon: '/docs/img/icons/react-icon',
        },
        {
          title: 'Vue 3',
          href: '/guides/getting-started/tutorials/with-vue-3',
          description:
            'Learn how to build a user management app with Vue 3 and Supabase Database, Auth, and Storage functionality.',
          icon: '/docs/img/icons/vuejs-icon',
        },
        {
          title: 'Nuxt 3',
          href: '/guides/getting-started/tutorials/with-nuxt-3',
          description:
            'Learn how to build a user management app with Nuxt 3 and Supabase Database, Auth, and Storage functionality.',
          icon: '/docs/img/icons/nuxt-icon',
        },
        {
          title: 'Angular',
          href: '/guides/getting-started/tutorials/with-angular',
          description:
            'Learn how to build a user management app with Angular and Supabase Database, Auth, and Storage functionality.',
          icon: '/docs/img/icons/angular-icon',
        },
        {
          title: 'RedwoodJS',
          href: '/guides/getting-started/tutorials/with-redwoodjs',
          description:
            'Learn how to build a user management app with RedwoodJS and Supabase Database, Auth, and Storage functionality.',
          icon: '/docs/img/icons/redwood-icon',
        },
        {
          title: 'Svelte',
          href: '/guides/getting-started/tutorials/with-svelte',
          description:
            'Learn how to build a user management app with Svelte and Supabase Database, Auth, and Storage functionality.',
          icon: '/docs/img/icons/svelte-icon',
        },
        {
          title: 'SvelteKit',
          href: '/guides/getting-started/tutorials/with-sveltekit',
          description:
            'Learn how to build a user management app with SvelteKit and Supabase Database, Auth, and Storage functionality.',
          icon: '/docs/img/icons/svelte-icon',
        },
        {
          title: 'refine',
          href: '/guides/getting-started/tutorials/with-refine',
          description:
            'Learn how to build a user management app with refine and Supabase Database, Auth, and Storage functionality.',
          icon: '/docs/img/icons/refine-icon',
        }
      ]
    .map((item) => {
        return (
          <Link href={`${item.href}`} key={item.title} passHref className={'col-span-4'}>
            <GlassPanel
              title={item.title}
              span="col-span-6"
              background={false}
              icon={item.icon}
              hasLightIcon={item.hasLightIcon}
            >
              {item.description}
            </GlassPanel>
          </Link>
        )

    })}
</div>


### Mobile tutorials

<div className="grid lg:grid-cols-12 gap-6 not-prose">
  {[
        {
          title: 'Flutter',
          href: '/guides/getting-started/tutorials/with-flutter',
          description:
            'Learn how to build a user management app with Flutter and Supabase Database, Auth, and Storage functionality.',
          icon: '/docs/img/icons/flutter-icon',
          enabled: isFeatureEnabled('sdk:dart')
        },
        {
          title: 'Expo React Native',
          href: '/guides/getting-started/tutorials/with-expo-react-native',
          description:
            'Learn how to build a user management app with Expo React Native and Supabase Database, Auth, and Storage functionality.',
          icon: '/docs/img/icons/expo-icon',
          hasLightIcon: true,
          enabled: true
        },
        {
          title: 'Expo React Native Social Auth',
          href: '/guides/getting-started/tutorials/with-expo-react-native-social-auth',
          description:
            'Learn how to implement social authentication in an app with Expo React Native and Supabase Database and Auth functionality.',
          icon: '/docs/img/icons/expo-icon',
          hasLightIcon: true
        },
        {
          title: 'Android Kotlin',
          href: '/guides/getting-started/tutorials/with-kotlin',
          description:
            'Learn how to build a product management app with Android and Supabase Database, Auth, and Storage functionality.',
          icon: '/docs/img/icons/kotlin-icon',
          enabled: isFeatureEnabled('sdk:kotlin')
        },
        {
          title: 'iOS Swift',
          href: '/guides/getting-started/tutorials/with-swift',
          description:
            'Learn how to build a user management app with iOS and Supabase Database, Auth, and Storage functionality.',
          icon: '/docs/img/icons/swift-icon',
          enabled: isFeatureEnabled('sdk:swift')
        },
        {
          title: 'Ionic React',
          href: '/guides/getting-started/tutorials/with-ionic-react',
          description:
            'Learn how to build a user management app with Ionic React and Supabase Database, Auth, and Storage functionality.',
          icon: '/docs/img/icons/ionic-icon',
          enabled: true
        },
        {
          title: 'Ionic Vue',
          href: '/guides/getting-started/tutorials/with-ionic-vue',
          description:
            'Learn how to build a user management app with Ionic Vue and Supabase Database, Auth, and Storage functionality.',
          icon: '/docs/img/icons/ionic-icon',
          enabled: true
        },
        {
          title: 'Ionic Angular',
          href: '/guides/getting-started/tutorials/with-ionic-angular',
          description:
            'Learn how to build a user management app with Ionic Angular and Supabase Database, Auth, and Storage functionality.',
          icon: '/docs/img/icons/ionic-icon',
          enabled: true
        }
      ]
    .filter((item) => item.enabled !== false)
    .map((item) => {
        return (
          <Link href={`${item.href}`} key={item.title} passHref className={'col-span-4'}>
            <GlassPanel
              title={item.title}
              span="col-span-6"
              background={false}
              icon={item.icon}
              hasLightIcon={item.hasLightIcon}
            >
              {item.description}
            </GlassPanel>
          </Link>
        )

    })}
</div>



# Integrations



Supabase integrates with many of your favorite third-party services.



## Vercel Marketplace

Create and manage your Supabase projects directly through Vercel. [Get started with Vercel](/docs/guides/integrations/vercel-marketplace).



## Supabase Marketplace

Browse tools for extending your Supabase project. [Browse the Supabase Marketplace](/partners/integrations).



# Local Development & CLI

Learn how to develop locally and use the Supabase CLI

Develop locally while running the Supabase stack on your machine.

<Admonition type="note">
  As a prerequisite, you must install a container runtime compatible with Docker APIs.

  *   [Docker Desktop](https://docs.docker.com/desktop/) (macOS, Windows, Linux)
  *   [Rancher Desktop](https://rancherdesktop.io/) (macOS, Windows, Linux)
  *   [Podman](https://podman.io/) (macOS, Windows, Linux)
  *   [OrbStack](https://orbstack.dev/) (macOS)
</Admonition>



## Quickstart

1.  Install the Supabase CLI:

    <Tabs scrollable size="small" type="underlined" defaultActiveId="npm" queryGroup="package-manager">
      <TabPanel id="npm" label="npm">
        ```sh
        npm install supabase --save-dev
        ```
      </TabPanel>

      <TabPanel id="yarn" label="yarn">
        ```sh
        NODE_OPTIONS=--no-experimental-fetch yarn add supabase --dev
        ```
      </TabPanel>

      <TabPanel id="pnpm" label="pnpm">
        ```sh
        pnpm add supabase --save-dev --allow-build=supabase
        ```

        <Admonition type="note">
          The `--allow-build=supabase` flag is required on pnpm version 10 or higher. If you're using an older version of pnpm, omit this flag.
        </Admonition>
      </TabPanel>

      <TabPanel id="brew" label="brew">
        ```sh
        brew install supabase/tap/supabase
        ```
      </TabPanel>
    </Tabs>

2.  In your repo, initialize the Supabase project:

    <Tabs scrollable size="small" type="underlined" defaultActiveId="npm" queryGroup="package-manager">
      <TabPanel id="npm" label="npm">
        ```sh
        npx supabase init
        ```
      </TabPanel>

      <TabPanel id="yarn" label="yarn">
        ```sh
        yarn supabase init
        ```
      </TabPanel>

      <TabPanel id="pnpm" label="pnpm">
        ```sh
        pnpx supabase init
        ```
      </TabPanel>

      <TabPanel id="brew" label="brew">
        ```sh
        supabase init
        ```
      </TabPanel>
    </Tabs>

3.  Start the Supabase stack:

    <Tabs scrollable size="small" type="underlined" defaultActiveId="npm" queryGroup="package-manager">
      <TabPanel id="npm" label="npm">
        ```sh
        npx supabase start
        ```
      </TabPanel>

      <TabPanel id="yarn" label="yarn">
        ```sh
        yarn supabase start
        ```
      </TabPanel>

      <TabPanel id="pnpm" label="pnpm">
        ```sh
        pnpx supabase start
        ```
      </TabPanel>

      <TabPanel id="brew" label="brew">
        ```sh
        supabase start
        ```
      </TabPanel>
    </Tabs>

4.  View your local Supabase instance at [http://localhost:54323](http://localhost:54323).



## Local development

Local development with Supabase allows you to work on your projects in a self-contained environment on your local machine. Working locally has several advantages:

1.  Faster development: You can make changes and see results instantly without waiting for remote deployments.
2.  Offline work: You can continue development even without an internet connection.
3.  Cost-effective: Local development is free and doesn't consume your project's quota.
4.  Enhanced privacy: Sensitive data remains on your local machine during development.
5.  Easy testing: You can experiment with different configurations and features without affecting your production environment.

To get started with local development, you'll need to install the [Supabase CLI](#cli) and Docker. The Supabase CLI allows you to start and manage your local Supabase stack, while Docker is used to run the necessary services.

Once set up, you can initialize a new Supabase project, start the local stack, and begin developing your application using local Supabase services. This includes access to a local Postgres database, Auth, Storage, and other Supabase features.



## CLI

The Supabase CLI is a powerful tool that enables developers to manage their Supabase projects directly from the terminal. It provides a suite of commands for various tasks, including:

*   Setting up and managing local development environments
*   Generating TypeScript types for your database schema
*   Handling database migrations
*   Managing environment variables and secrets
*   Deploying your project to the Supabase platform

With the CLI, you can streamline your development workflow, automate repetitive tasks, and maintain consistency across different environments. It's an essential tool for both local development and CI/CD pipelines.

See the [CLI Getting Started guide](/docs/guides/local-development/cli/getting-started) for more information.



# Supabase Platform



Supabase is a hosted platform which makes it very simple to get started without needing to manage any infrastructure.

Visit [supabase.com/dashboard](/dashboard) and sign in to start creating projects.



## Projects

Each project on Supabase comes with:

*   A dedicated [Postgres database](/docs/guides/database)
*   [Auto-generated APIs](/docs/guides/database/api)
*   [Auth and user management](/docs/guides/auth)
*   [Edge Functions](/docs/guides/functions)
*   [Realtime API](/docs/guides/realtime)
*   [Storage](/docs/guides/storage)



## Organizations

Organizations are a way to group your projects. Each organization can be configured with different team members and billing settings.
Refer to [access control](/docs/guides/platform/access-control) for more information on how to manage team members within an organization.



## Platform status

If Supabase experiences outages, we keep you as informed as possible, as early as possible. We provide the following feedback channels:

*   Status page: [status.supabase.com](https://status.supabase.com/)
*   RSS Feed: [status.supabase.com/history.rss](https://status.supabase.com/history.rss)
*   Atom Feed: [status.supabase.com/history.atom](https://status.supabase.com/history.atom)
*   Slack Alerts: You can receive updates via the RSS feed, using Slack's [built-in RSS functionality](https://slack.com/help/articles/218688467-Add-RSS-feeds-to-Slack) <br />`/feed subscribe https://status.supabase.com/history.atom`

Make sure to review our [SLA](/docs/company/sla) for details on our commitment to Platform Stability.



# Supabase Queues

Durable Message Queues with Guaranteed Delivery in Postgres

Supabase Queues is a Postgres-native durable Message Queue system with guaranteed delivery built on the [pgmq database extension](https://github.com/tembo-io/pgmq). It offers developers a seamless way to persist and process Messages in the background while improving the resiliency and scalability of their applications and services.

Queues couples the reliability of Postgres with the simplicity Supabase's platform and developer experience, enabling developers to manage Background Tasks with zero configuration.



## Features

*   **Postgres Native**
    <br />
    Built on top of the `pgmq` database extension, create and manage Queues with any Postgres tooling.
*   **Guaranteed Message Delivery**
    <br />
    Messages added to Queues are guaranteed to be delivered to your consumers.
*   **Exactly Once Message Delivery**
    <br />A Message is delivered exactly once to a consumer within a customizable visibility window.
*   **Message Durability and Archival**
    <br />
    Messages are stored in Postgres and you can choose to archive them for analytical or auditing purposes.
*   **Granular Authorization**
    <br />
    Control client-side consumer access to Queues with API permissions and Row Level Security (RLS) policies.
*   **Queue Management and Monitoring**
    <br />
    Create, manage, and monitor Queues and Messages in the Supabase Dashboard.



## Resources

*   [Quickstart](/docs/guides/queues/quickstart)
*   [API Reference](/docs/guides/queues/api)
*   [`pgmq` GitHub Repository](https://github.com/tembo-io/pgmq)



# Realtime

Send and receive messages to connected clients.

Supabase provides a globally distributed [Realtime](https://github.com/supabase/realtime) service with the following features:

*   [Broadcast](/docs/guides/realtime/broadcast): Send low-latency messages between clients. Perfect for real-time messaging, database changes, cursor tracking, game events, and custom notifications.
*   [Presence](/docs/guides/realtime/presence): Track and synchronize user state across clients. Ideal for showing who's online, or active participants.
*   [Postgres Changes](/docs/guides/realtime/postgres-changes): Listen to database changes in real-time.



## What can you build?

*   **Chat applications** - Real-time messaging with typing indicators and online presence
*   **Collaborative tools** - Document editing, whiteboards, and shared workspaces
*   **Live dashboards** - Real-time data visualization and monitoring
*   **Multiplayer games** - Synchronized game state and player interactions
*   **Social features** - Live notifications, reactions, and user activity feeds

Check the [Getting Started](/docs/guides/realtime/getting_started) guide to get started.



## Examples

<div className="grid md:grid-cols-12 gap-4 not-prose">
  {[
        {
          name: 'Multiplayer.dev',
          description: 'Showcase application displaying cursor movements and chat messages using Broadcast.',
          href: 'https://multiplayer.dev',
        },
        {
          name: 'Chat',
          description: 'Supabase UI chat component using Broadcast to send message between users.',
          href: 'https://supabase.com/ui/docs/nextjs/realtime-chat'
        },
        {
          name: 'Avatar Stack',
          description: 'Supabase UI avatar stack component using Presence to track connected users.',
          href: 'https://supabase.com/ui/docs/nextjs/realtime-avatar-stack'
        },
        {
          name: 'Realtime Cursor',
          description: "Supabase UI realtime cursor component using Broadcast to share users' cursors to build collaborative applications.",
          href: 'https://supabase.com/ui/docs/nextjs/realtime-cursor'
        }
    ].map((x) => (
      <div className="col-span-6" key={x.href}>
        <Link href={x.href} target="_blank" passHref>
          <GlassPanel title={x.name}>{x.description}</GlassPanel>
        </Link>
      </div>
    ))}
</div>



## Resources

Find the source code and documentation in the Supabase GitHub repository.

<div className="grid md:grid-cols-12 gap-4 not-prose">
  {[
        {
          name: 'Supabase Realtime',
          description: 'View the source code.',
          href: 'https://github.com/supabase/realtime',
        },
        {
          name: 'Realtime: Multiplayer Edition',
          description: 'Read more about Supabase Realtime.',
          href: 'https://supabase.com/blog/supabase-realtime-multiplayer-general-availability',
        },
      ].map((x) => (
        <div className="col-span-6" key={x.href}>
          <Link href={x.href} passHref>
            <GlassPanel title={x.name}>{x.description}</GlassPanel>
          </Link>
        </div>
      ))}
</div>



# Resources



{/* <!-- vale off --> */}

<div className="flex flex-col gap-12 my-12">
  <div>
    <div className="grid grid-cols-12 gap-6 not-prose">
      {
                [
                  {
                    title: 'Examples',
                    hasLightIcon: true,
                    href: '/guides/resources/examples',
                    description: 'Official GitHub examples, curated content from the community, and more.',
                  },
                  {
                    title: 'Glossary',
                    hasLightIcon: true,
                    href: '/guides/resources/glossary',
                    description: 'Definitions for terminology and acronyms used in the Supabase documentation.',
                  }
                ]
            .map((resource) => {
                  return (
                    <Link
                      href={`${resource.href}`}
                      key={resource.title}
                      className={'col-span-12 md:col-span-4'}
                      passHref
                    >
                      <GlassPanel {...resource} background={false} showIconBg={true}>
                        {resource.description}
                      </GlassPanel>
                    </Link>
                  )

            })}
    </div>
  </div>

  <div>
    <div className="max-w-xl mb-6">
      ### Migrate to Supabase
    </div>

    <div className="grid grid-cols-12 gap-6 not-prose">
      {
                [
                  {
                    title: 'Auth0',
                    icon: '/docs/img/icons/auth0-icon',
                    href: '/guides/resources/migrating-to-supabase/auth0',
                    description: 'Move your auth users from Auth0 to a Supabase project.',
                    hasLightIcon: true,
                  },
                  {
                    title: 'Firebase Auth',
                    icon: '/docs/img/icons/firebase-icon',
                    href: '/guides/resources/migrating-to-supabase/firebase-auth',
                    description: 'Move your auth users from a Firebase project to a Supabase project.',
                  },
                  {
                    title: 'Firestore Data',
                    icon: '/docs/img/icons/firebase-icon',
                    href: '/guides/resources/migrating-to-supabase/firestore-data',
                    description: 'Migrate the contents of a Firestore collection to a single PostgreSQL table.',
                  },
                  {
                    title: 'Firebase Storage',
                    icon: '/docs/img/icons/firebase-icon',
                    href: '/guides/resources/migrating-to-supabase/firebase-storage',
                    description: 'Convert your Firebase Storage files to Supabase Storage.'
                  },
                  {
                    title: 'Heroku',
                    icon: '/docs/img/icons/heroku-icon',
                    href: '/guides/resources/migrating-to-supabase/heroku',
                    description: 'Migrate your Heroku Postgres database to Supabase.'
                  },
                  {
                    title: 'Render',
                    icon: '/docs/img/icons/render-icon',
                    href: '/guides/resources/migrating-to-supabase/render',
                    description: 'Migrate your Render Postgres database to Supabase.'
                  },
                  {
                    title: 'Amazon RDS',
                    icon: '/docs/img/icons/aws-rds-icon',
                    href: '/guides/resources/migrating-to-supabase/amazon-rds',
                    description: 'Migrate your Amazon RDS database to Supabase.'
                  },
                  {
                    title: 'Postgres',
                    icon: '/docs/img/icons/postgres-icon',
                    href: '/guides/resources/migrating-to-supabase/postgres',
                    description: 'Migrate your Postgres database to Supabase.'
                  },
                  {
                    title: 'MySQL',
                    icon: '/docs/img/icons/mysql-icon',
                    href: '/guides/resources/migrating-to-supabase/mysql',
                    description: 'Migrate your MySQL database to Supabase.'
                  },
                  {
                    title: 'Microsoft SQL Server',
                    icon: '/docs/img/icons/mssql-icon',
                    href: '/guides/resources/migrating-to-supabase/mssql',
                    description: 'Migrate your Microsoft SQL Server database to Supabase.'
                  }
                ]
            .map((product) => {
                  return (
                    <Link
                      href={`${product.href}`}
                      key={product.title}
                      className={product.span ?? 'col-span-6 md:col-span-3'}
                      passHref
                    >
                      <IconPanel {...product} background={true} showIconBg={true} showLink={true}>
                        {product.description}
                      </IconPanel>
                    </Link>
                  )

            })}
    </div>
  </div>

  <div>
    <div className="max-w-xl mb-6">
      ### Postgres resources
    </div>

    <div className="grid grid-cols-12 gap-6 not-prose">
      {
                [
                  {
                    title: 'Managing Indexes',
                    hasLightIcon: true,
                    href: '/guides/database/postgres/indexes',
                    description: 'Improve query performance using various index types in Postgres.'
                  },
                  {
                    title: 'Cascade Deletes',
                    hasLightIcon: true,
                    href: '/guides/database/postgres/cascade-deletes',
                    description: 'Understand the types of foreign key constraint deletes.'
                  },
                  {
                    title: 'Drop all tables in schema',
                    hasLightIcon: true,
                    href: '/guides/database/postgres/dropping-all-tables-in-schema',
                    description: 'Delete all tables in a given schema.'
                  },
                  {
                    title: 'Select first row per group',
                    hasLightIcon: true,
                    href: '/guides/database/postgres/first-row-in-group',
                    description: 'Retrieve the first row in each distinct group.'
                  },
                  {
                    title: 'Print PostgreSQL version',
                    hasLightIcon: true,
                    href: '/guides/database/postgres/which-version-of-postgres',
                    description: 'Find out which version of Postgres you are running.'
                  }
                ]
            .map((resource) => {
                  return (
                    <Link
                      href={`${resource.href}`}
                      key={resource.title}
                      className={'col-span-12 md:col-span-4'}
                      passHref
                    >
                      <GlassPanel {...resource} background={false} showIconBg={true}>
                        {resource.description}
                      </GlassPanel>
                    </Link>
                  )

            })}
    </div>
  </div>

  {/* end of container */}
</div>



# Supabase Security



Supabase is a hosted platform which makes it very simple to get started without needing to manage any infrastructure. The hosted platform comes with many security and compliance controls managed by Supabase.



# Compliance

Supabase is SOC 2 Type 2 compliant and regularly audited. All projects at Supabase are governed by the same set of compliance controls.
The [SOC 2 Compliance Guide](/docs/guides/security/soc-2-compliance) explains Supabase's SOC 2 responsibilities and controls in more detail.

The [HIPAA Compliance Guide](/docs/guides/security/hipaa-compliance) explains Supabase's HIPAA responsibilities. Additional [security and compliance controls](/docs/guides/deployment/shared-responsibility-model#managing-healthcare-data) for projects that deal with electronic Protected Health Information (ePHI) and require HIPAA compliance are available through the HIPAA add-on.



# Platform configuration

As a hosted platform, Supabase provides additional security controls to further enhance the security posture depending on organizations' own requirements or obligations.

These can be found under the [dedicated security page](/dashboard/org/_/security) under organization settings. And are described in greater detail [here](/docs/guides/security/platform-security).



# Product configuration

Each product offered by Supabase comes with customizable security controls and these security controls help ensure that applications built on Supabase are secure, compliant, and resilient against various threats.

The [security configuration guides](/docs/guides/security/product-security) provide detailed information for configuring individual products.



# Self-Hosting

Host Supabase on your own infrastructure.

There are several ways to host Supabase on your own computer, server, or cloud.



## Officially supported

<div className="grid md:grid-cols-12 gap-4 not-prose">
  <div className="md:col-span-6 xl:col-span-3 relative" key="/guides/self-hosting/docker">
    <span className=" absolute left-28 top-[34px] uppercase text-xs whitespace-nowrap text-foreground-lighter font-mono z-10 border rounded-full px-2 py-0.5">
      Most common
    </span>

    <Link href="/guides/self-hosting/docker" passHref>
      <GlassPanel title="Docker">
        Deploy Supabase within your own infrastructure using Docker Compose.
      </GlassPanel>
    </Link>
  </div>

  <div className="md:col-span-6 xl:col-span-3" key="/pricing">
    <Link href="https://supabase.com/pricing" passHref>
      <GlassPanel title="BYO Cloud">Contact our Enterprise sales team if you need Supabase managed in your own cloud.</GlassPanel>
    </Link>
  </div>
</div>

Supabase is also a hosted platform. If you want to get started for free, visit [supabase.com/dashboard](/dashboard).



## Community supported

There are several community-driven projects to help you deploy Supabase. We encourage you to try them out and contribute back to the community.

<div className="grid md:grid-cols-12 gap-4 not-prose">
  {community.map((x) => (
        <div className="md:col-span-6 xl:col-span-3" key={x.href}>
          <Link href={x.href} passHref>
            <GlassPanel title={x.name}>{x.description}</GlassPanel>
          </Link>
        </div>
      ))}
</div>

export const community = [
  {
    name: 'Kubernetes',
    description: 'Helm charts to deploy a Supabase on Kubernetes.',
    href: 'https://github.com/supabase-community/supabase-kubernetes',
  },
  {
    name: 'Traefik',
    description: 'A self-hosted Supabase setup with Traefik as a reverse proxy.',
    href: 'https://github.com/supabase-community/supabase-traefik',
  },
  {
    name: 'AWS',
    description: 'A CloudFormation template for Supabase.',
    href: 'https://github.com/supabase-community/supabase-on-aws',
  },
]



## Third-party guides

The following third-party providers have shown consistent support for the self-hosted version of Supabase:.

<div className="grid md:grid-cols-12 gap-4 not-prose">
  {[
        {
          name: 'StackGres',
          description: 'Deploys using Kubernetes.',
          href: 'https://stackgres.io/blog/running-supabase-on-top-of-stackgres/',
        },
        {
          name: 'Pigsty',
          description: 'Deploys using Ansible.',
          href: 'https://pigsty.io/blog/db/supabase/',
        },
      ].map((x) => (
        <div className="md:col-span-6" key={x.href}>
          <Link href={x.href} passHref>
            <GlassPanel title={x.name}>{x.description}</GlassPanel>
          </Link>
        </div>
      ))}
</div>



# Storage

Use Supabase to store and serve files.

Supabase Storage makes it simple to upload and serve files of any size, providing a robust framework for file access controls.



## Features

You can use Supabase Storage to store images, videos, documents, and any other file type. Serve your assets with a global CDN to reduce latency from over 285 cities globally. Supabase Storage includes a built-in image optimizer, so you can resize and compress your media files on the fly.



## Examples

Check out all of the Storage [templates and examples](https://github.com/supabase/supabase/tree/master/examples/storage) in our GitHub repository.

<div className="grid md:grid-cols-12 gap-4 not-prose">
  {examples.map((x) => (
        <div className="col-span-12" key={x.href}>
          <Link href={x.href} passHref>
            <GlassPanel icon={'/docs/img/icons/github-icon'} hasLightIcon={true} title={x.name}>
              {x.description}
            </GlassPanel>
          </Link>
        </div>
      ))}
</div>

export const examples = [
  {
    name: 'Resumable Uploads with Uppy',
    description:
      'Use Uppy to upload files to Supabase Storage using the TUS protocol (resumable uploads).',
    href: 'https://github.com/supabase/supabase/tree/master/examples/storage/resumable-upload-uppy',
  },
]



## Resources

Find the source code and documentation in the Supabase GitHub repository.

<div className="grid md:grid-cols-12 gap-4 not-prose">
  {[
        {
          name: 'Supabase Storage API',
          description: 'View the source code.',
          href: 'https://github.com/supabase/storage-api',
        },
        {
          name: 'OpenAPI Spec',
          description: 'See the Swagger Documentation for Supabase Storage.',
          href: 'https://supabase.github.io/storage/',
        },
      ].map((x) => (
        <div className="col-span-6" key={x.href}>
          <Link href={x.href} passHref>
            <GlassPanel title={x.name}>{x.description}</GlassPanel>
          </Link>
        </div>
      ))}
</div>



# Telemetry



Telemetry helps you understand what’s happening inside your app by collecting logs, metrics, and traces.

*   **Logs** capture individual events, such as errors or warnings, providing details about what happened at a specific moment.
*   **Metrics** track numerical data over time, like request latency or database query performance, helping you spot trends.
*   **Traces** show the flow of a request through different services, helping you debug slow or failing operations.

Supabase is working towards full support for the [OpenTelemetry](https://opentelemetry.io/) standard, making it easier to integrate with observability tools.

This section provides guidance on telemetry in Supabase, including how to work with Supabase Logs.



# Advanced Log Filtering




# Querying the logs



## Understanding field references

The log tables are queried with a subset of BigQuery SQL syntax. They all have three columns: `event_message`, `timestamp`, and `metadata`.

| column         | description                 |
| -------------- | --------------------------- |
| timestamp      | time event was recorded     |
| event\_message | the log's message           |
| metadata       | information about the event |

The `metadata` column is an array of JSON objects that stores important details about each recorded event. For example, in the Postgres table, the `metadata.parsed.error_severity` field indicates the error level of an event. To work with its values, you need to `unnest` them using a `cross join`.

This approach is commonly used with JSON and array columns, so it might look a bit unfamiliar if you're not used to working with these data types.

```sql
select
  event_message,
  parsed.error_severity,
  parsed.user_name
from
  postgres_logs
  -- extract first layer
  cross join unnest(postgres_logs.metadata) as metadata
  -- extract second layer
  cross join unnest(metadata.parsed) as parsed;
```



## Expanding results

Logs returned by queries may be difficult to read in table format. A row can be double-clicked to expand the results into more readable JSON:

![Expanding log results](/docs/img/guides/platform/expanded-log-results.png)



## Filtering with [regular expressions](https://en.wikipedia.org/wiki/Regular_expression)

The Logs use BigQuery Style regular expressions with the [regexp\_contains function](https://cloud.google.com/bigquery/docs/reference/standard-sql/string_functions#regexp_contains). In its most basic form, it will check if a string is present in a specified column.

```sql
select
  cast(timestamp as datetime) as timestamp,
  event_message,
  metadata
from postgres_logs
where regexp_contains(event_message, 'is present');
```

There are multiple operators that you should consider using:


### Find messages that start with a phrase

`^` only looks for values at the start of a string

```sql
-- find only messages that start with connection
regexp_contains(event_message, '^connection')
```


### Find messages that end with a phrase:

`$` only looks for values at the end of the string

```sql
-- find only messages that ends with port=12345
regexp_contains(event_message, '$port=12345')
```


### Ignore case sensitivity:

`(?i)` ignores capitalization for all proceeding characters

```sql
-- find all event_messages with the word "connection"
regexp_contains(event_message, '(?i)COnnecTion')
```


### Wildcards:

`.` can represent any string of characters

```sql
-- find event_messages like "hello<anything>world"
regexp_contains(event_message, 'hello.world')
```


### Alphanumeric ranges:

`[1-9a-zA-Z]` finds any strings with only numbers and letters

```sql
-- find event_messages that contain a number between 1 and 5 (inclusive)
regexp_contains(event_message, '[1-5]')
```


### Repeated values:

`x*` zero or more x
`x+` one or more x
`x?` zero or one x
`x{4,}` four or more x
`x{3}` exactly 3 x

```sql
-- find event_messages that contains any sequence of 3 digits
regexp_contains(event_message, '[0-9]{3}')
```


### Escaping reserved characters:

`\.` interpreted as period `.` instead of as a wildcard

```sql
-- escapes .
regexp_contains(event_message, 'hello world\.')
```


### `or` statements:

`x|y` any string with `x` or `y` present

```sql
-- find event_messages that have the word 'started' followed by either the word "host" or "authenticated"
regexp_contains(event_message, 'started host|authenticated')
```


### `and`/`or`/`not` statements in SQL:

`and`, `or`, and `not` are all native terms in SQL and can be used in conjunction with regular expressions to filter results

```sql
select
  cast(timestamp as datetime) as timestamp,
  event_message,
  metadata
from postgres_logs
where
  (regexp_contains(event_message, 'connection') and regexp_contains(event_message, 'host'))
  or not regexp_contains(event_message, 'received');
```


### Filtering and unnesting example

**Filter for Postgres**

```sql
select
  cast(postgres_logs.timestamp as datetime) as timestamp,
  parsed.error_severity,
  parsed.user_name,
  event_message
from
  postgres_logs
  cross join unnest(metadata) as metadata
  cross join unnest(metadata.parsed) as parsed
where regexp_contains(parsed.error_severity, 'ERROR|FATAL|PANIC')
order by timestamp desc
limit 100;
```



## Limitations


### Log tables cannot be joined together

Each product table operates independently without the ability to join with other log tables. This may change in the future.


### The `with` keyword and subqueries are not supported

The parser does not yet support `with` and subquery statements.


### The `ilike` and `similar to` keywords are not supported

Although `like` and other comparison operators can be used, `ilike` and `similar to` are incompatible with BigQuery's variant of SQL. `regexp_contains` can be used as an alternative.


### The wildcard operator `*` to select columns is not supported

The log parser is not able to parse the `*` operator for column selection. Instead, you can access all fields from the `metadata` column:

```sql
select
  cast(postgres_logs.timestamp as datetime) as timestamp,
  event_message,
  metadata
from
  <log_table_name>
order by timestamp desc
limit 100;
```



# Log Drains



Log drains will send all logs of the Supabase stack to one or more desired destinations. It is only available for customers on Team and Enterprise Plans. Log drains is available in the dashboard under [Project Settings > Log Drains](/dashboard/project/_/settings/log-drains).

You can read about the initial announcement [here](/blog/log-drains) and vote for your preferred drains in [this discussion](https://github.com/orgs/supabase/discussions/28324?sort=top).



# Supported destinations

The following table lists the supported destinations and the required setup configuration:

| Destination           | Transport Method | Configuration                                      |
| --------------------- | ---------------- | -------------------------------------------------- |
| Generic HTTP endpoint | HTTP             | URL <br /> HTTP Version <br /> Gzip <br /> Headers |
| DataDog               | HTTP             | API Key <br /> Region                              |
| Loki                  | HTTP             | URL <br /> Headers                                 |
| Sentry                | HTTP             | DSN                                                |

HTTP requests are batched with a max of 250 logs or 1 second intervals, whichever happens first. Logs are compressed via Gzip if the destination supports it.



## Generic HTTP endpoint

Logs are sent as a POST request with a JSON body. Both HTTP/1 and HTTP/2 protocols are supported.
Custom headers can optionally be configured for all requests.

Note that requests are **unsigned**.

<Admonition type="note">
  Unsigned requests to HTTP endpoints are temporary and all requests will signed in the near future.
</Admonition>

<Accordion type="default" openBehaviour="multiple">
  <AccordionItem header="Edge Function Walkthrough (Uncompressed)" id="uncompressed">
    1.  Create and deploy the edge function

    Generate a new edge function template and update it to log out the received JSON payload. For simplicity, we will accept any request with an Anon Key.

    ```bash
    supabase functions new hello-world
    ```

    You can use this example snippet as an illustration of how the received request will be like.

    ```ts
    import 'npm:@supabase/functions-js/edge-runtime.d.ts'

    Deno.serve(async (req) => {
      const data = await req.json()

      console.log(`Received ${data.length} logs, first log:\n ${JSON.stringify(data[0])}`)
      return new Response(JSON.stringify({ message: 'ok' }), {
        headers: { 'Content-Type': 'application/json' },
      })
    })
    ```

    And then deploy it with:

    ```bash
    supabase functions deploy hello-world --project-ref [PROJECT REF]
    ```

    <Admonition type="caution">
      This will create an infinite loop, as we are generating an additional log event that will eventually trigger a new request to this edge function. However, due to the batching nature of how Log Drain events are dispatched, the rate of edge function triggers will not increase greatly and will have an upper bound.
    </Admonition>

    2.  Configure the HTTP Drain

    Create a HTTP drain under the [Project Settings > Log Drains](/dashboard/project/_/settings/log-drains).

    *   Disable the Gzip, as we want to receive the payload without compression.
    *   Under URL, set it to your edge function URL `https://[PROJECT REF].supabase.co/functions/v1/hello-world`
    *   Under Headers, set the `Authorization: Bearer [ANON KEY]`

    <ProjectConfigVariables variable="publishableKey" />
  </AccordionItem>

  <AccordionItem header="Edge Function Gzip Example" id="gzip">
    Gzip payloads can be decompressed using native in-built APIs. Refer to the Edge Function [compression guide](/docs/guides/functions/compression)

    ```ts
    import { gunzipSync } from 'node:zlib'

    Deno.serve(async (req) => {
      try {
        // Check if the request body is gzip compressed
        const contentEncoding = req.headers.get('content-encoding')
        if (contentEncoding !== 'gzip') {
          return new Response('Request body is not gzip compressed', {
            status: 400,
          })
        }

        // Read the compressed body
        const compressedBody = await req.arrayBuffer()

        // Decompress the body
        const decompressedBody = gunzipSync(new Uint8Array(compressedBody))

        // Convert the decompressed body to a string
        const decompressedString = new TextDecoder().decode(decompressedBody)
        const data = JSON.parse(decompressedString)
        // Process the decompressed body as needed
        console.log(`Received: ${data.length} logs.`)

        return new Response('ok', {
          headers: { 'Content-Type': 'text/plain' },
        })
      } catch (error) {
        console.error('Error:', error)
        return new Response('Error processing request', { status: 500 })
      }
    })
    ```
  </AccordionItem>
</Accordion>



## DataDog logs

Logs sent to DataDog have the name of the log source set on the `service` field of the event and the source set to `Supabase`. Logs are gzipped before they are sent to DataDog.

The payload message is a JSON string of the raw log event, prefixed with the event timestamp.

To setup DataDog log drain, generate a DataDog API key [here](https://app.datadoghq.com/organization-settings/api-keys) and the location of your DataDog site.

<Accordion type="default" openBehaviour="multiple">
  <AccordionItem header="Walkthrough" id="walkthrough">
    1.  Generate API Key in [DataDog dashboard](https://app.datadoghq.com/organization-settings/api-keys)
    2.  Create log drain in [Supabase dashboard](/dashboard/project/_/settings/log-drains)
    3.  Watch for events in the [DataDog Logs page](https://app.datadoghq.com/logs)
  </AccordionItem>

  <AccordionItem header="Example destination configuration" id="cfg">
    [Grok parser](https://docs.datadoghq.com/service_management/events/pipelines_and_processors/grok_parser?tab=matchers) matcher for extracting the timestamp to a `date` field

    ```
    %{date("yyyy-MM-dd'T'HH:mm:ss.SSSSSSZZ"):date}
    ```

    [Grok parser](https://docs.datadoghq.com/service_management/events/pipelines_and_processors/grok_parser?tab=matchers) matcher for converting stringified JSON to structured JSON on the `json` field.

    ```
     %{data::json}
    ```

    [Remapper](https://docs.datadoghq.com/service_management/events/pipelines_and_processors/remapper) for setting the log level.

    ```
    metadata.parsed.error_severity, metadata.level
    ```
  </AccordionItem>
</Accordion>

If you are interested in other log drains, upvote them [here](https://github.com/orgs/supabase/discussions/28324)



## Loki

Logs sent to the Loki HTTP API are specifically formatted according to the HTTP API requirements. See the official Loki HTTP API documentation for [more details](https://grafana.com/docs/loki/latest/reference/loki-http-api/#ingest-logs).

Events are batched with a maximum of 250 events per request.

The log source and product name will be used as stream labels.

The `event_message` and `timestamp` fields will be dropped from the events to avoid duplicate data.

Loki must be configured to accept **structured metadata**, and it is advised to increase the default maximum number of structured metadata fields to at least 500 to accommodate large log event payloads of different products.



## Sentry

Logs are sent to Sentry as part of [Sentry's Logging Product](https://docs.sentry.io/product/explore/logs/). Ingesting Supabase logs as Sentry errors is currently not supported.

To setup the Sentry log drain, you need to do the following:

1.  Grab your DSN from your [Sentry project settings](https://docs.sentry.io/concepts/key-terms/dsn-explainer/). It should be of the format `{PROTOCOL}://{PUBLIC_KEY}:{SECRET_KEY}@{HOST}{PATH}/{PROJECT_ID}`.
2.  Create log drain in [Supabase dashboard](/dashboard/project/_/settings/log-drains)
3.  Watch for events in the [Sentry Logs page](https://sentry.io/explore/logs/)

All fields from the log event are attached as attributes to the Sentry log, which can be used for filtering and grouping in the Sentry UI. There are no limits to cardinality or the number of attributes that can be attached to a log.

If you are self-hosting Sentry, Sentry Logs are only supported in self-hosted version [25.9.0](https://github.com/getsentry/self-hosted/releases/tag/25.9.0) and later.



## Pricing

For a detailed breakdown of how charges are calculated, refer to [Manage Log Drain usage](/docs/guides/platform/manage-your-usage/log-drains).



# Logging



The Supabase Platform includes a Logs Explorer that allows log tracing and debugging. Log retention is based on your [project's pricing plan](/pricing).



## Product logs

Supabase provides a logging interface specific to each product. You can use simple regular expressions for keywords and patterns to search log event messages. You can also export and download the log events matching your query as a spreadsheet.

{/* <!-- To update screenshots, ensure that at least one log line is selected to display the metadata. Can use meme.town as an example. --> */}

<Tabs scrollable size="small" type="underlined" defaultActiveId="api" queryGroup="product">
  <TabPanel id="api" label="API">
    [API logs](/dashboard/project/_/logs/edge-logs) show all network requests and response for the REST and GraphQL [APIs](../../guides/database/api). If [Read Replicas](/docs/guides/platform/read-replicas) are enabled, logs are automatically filtered between databases as well as the [API Load Balancer](/docs/guides/platform/read-replicas#api-load-balancer) endpoint. Logs for a specific endpoint can be toggled with the `Source` button on the upper-right section of the dashboard.

    When viewing logs originating from the API Load Balancer endpoint, the upstream database or the one that eventually handles the request can be found under the `Redirect Identifier` field. This is equivalent to `metadata.load_balancer_redirect_identifier` when querying the underlying logs.

    ![API Logs](/docs/img/guides/platform/logs/logs-api.png)
  </TabPanel>

  <TabPanel id="postgres" label="Postgres">
    [Postgres logs](/dashboard/project/_/logs/postgres-logs) show queries and activity for your [database](../../guides/database). If [Read Replicas](/docs/guides/platform/read-replicas) are enabled, logs are automatically filtered between databases. Logs for a specific database can be toggled with the `Source` button on the upper-right section of the dashboard.

    ![Postgres Logs](/docs/img/guides/platform/logs/logs-database.png)
  </TabPanel>

  <TabPanel id="auth" label="Auth">
    [Auth logs](/dashboard/project/_/logs/auth-logs) show all server logs for your [Auth usage](../../guides/auth).

    ![Auth Logs](/docs/img/guides/platform/logs/logs-auth.png)
  </TabPanel>

  <TabPanel id="storage" label="Storage">
    [Storage logs](/dashboard/project/_/logs/storage-logs) shows all server logs for your [Storage API](../../guides/storage).

    ![Storage Logs](/docs/img/guides/platform/logs/logs-storage.png)
  </TabPanel>

  <TabPanel id="realtime" label="Realtime">
    [Realtime logs](/dashboard/project/_/logs/realtime-logs) show all server logs for your [Realtime API usage](../../guides/realtime).

    <Admonition type="note">
      Realtime connections are not logged by default. Turn on [Realtime connection logs per client](#logging-realtime-connections) with the `log_level` parameter.
    </Admonition>

    ![Realtime Logs](/docs/img/guides/platform/logs/logs-realtime.png)
  </TabPanel>

  <TabPanel id="functions" label="Edge Functions">
    For each [Edge Function](/dashboard/project/_/functions), logs are available under the following tabs:

    **Invocations**

    The Invocations tab displays the edge logs of function calls.

    ![Function Edge Logs](/docs/img/guides/platform/logs/logs-functions-edge.png)

    **Logs**

    The Logs tab displays logs emitted during function execution.

    ![Function Logs](/docs/img/guides/platform/logs/logs-functions.png)

    **Log Message Length**

    Edge Function log messages have a max length of 10,000 characters. If you try to log a message longer than that it will be truncated.
  </TabPanel>
</Tabs>

***



## Working with API logs

[API logs](/dashboard/project/_/logs/edge-logs) run through the Cloudflare edge servers and will have attached Cloudflare metadata under the `metadata.request.cf.*` fields.


### Allowed headers

A strict list of request and response headers are permitted in the API logs. Request and response headers will still be received by the server(s) and client(s), but will not be attached to the API logs generated.

Request headers:

*   `accept`
*   `cf-connecting-ip`
*   `cf-ipcountry`
*   `host`
*   `user-agent`
*   `x-forwarded-proto`
*   `referer`
*   `content-length`
*   `x-real-ip`
*   `x-client-info`
*   `x-forwarded-user-agent`
*   `range`
*   `prefer`

Response headers:

*   `cf-cache-status`
*   `cf-ray`
*   `content-location`
*   `content-range`
*   `content-type`
*   `content-length`
*   `date`
*   `transfer-encoding`
*   `x-kong-proxy-latency`
*   `x-kong-upstream-latency`
*   `sb-gateway-mode`
*   `sb-gateway-version`


### Additional request metadata

To attach additional metadata to a request, it is recommended to use the `User-Agent` header for purposes such as device or version identification.

For example:

```
node MyApp/1.2.3 (device-id:abc123)
Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0 MyApp/1.2.3 (Foo v1.3.2; Bar v2.2.2)
```

<Admonition type="note">
  Do not log Personal Identifiable Information (PII) within the `User-Agent` header, to avoid infringing data protection privacy laws. Overly fine-grained and detailed user agents may allow fingerprinting and identification of the end user through PII.
</Admonition>



## Logging Postgres queries

To enable query logs for other categories of statements:

1.  [Enable the pgAudit extension](/dashboard/project/_/database/extensions).
2.  Configure `pgaudit.log` (see below). Perform a fast reboot if needed.
3.  View your query logs under [Logs > Postgres Logs](/dashboard/project/_/logs/postgres-logs).


### Configuring `pgaudit.log`

The stored value under `pgaudit.log` determines the classes of statements that are logged by [pgAudit extension](https://www.pgaudit.org/). Refer to the pgAudit documentation for the [full list of values](https://github.com/pgaudit/pgaudit/blob/master/README.md#pgauditlog).

To enable logging for function calls/do blocks, writes, and DDL statements for a single session, execute the following within the session:

```sql
-- temporary single-session config update
set pgaudit.log = 'function, write, ddl';
```

To *permanently* set a logging configuration (beyond a single session), execute the following, then perform a fast reboot:

```sql
-- equivalent permanent config update.
alter role postgres set pgaudit.log to 'function, write, ddl';
```

To help with debugging, we recommend adjusting the log scope to only relevant statements as having too wide of a scope would result in a lot of noise in your Postgres logs.

Note that in the above example, the role is set to `postgres`. To log user-traffic flowing through the [HTTP APIs](../../guides/database/api#rest-api-overview) powered by PostgREST, set your configuration values for the `authenticator`.

```sql
-- for API-related logs
alter role authenticator set pgaudit.log to 'write';
```

By default, the log level will be set to `log`. To view other levels, run the following:

```sql
-- adjust log level
alter role postgres set pgaudit.log_level to 'info';
alter role postgres set pgaudit.log_level to 'debug5';
```

Note that as per the pgAudit [log\_level documentation](https://github.com/pgaudit/pgaudit/blob/master/README.md#pgauditlog_level), `error`, `fatal`, and `panic` are not allowed.

To reset system-wide settings, execute the following, then perform a fast reboot:

```sql
-- resets stored config.
alter role postgres reset pgaudit.log
```

<Admonition type="note">
  If any permission errors are encountered when executing `alter role postgres ...`, it is likely that your project has yet to receive the patch to the latest version of [supautils](https://github.com/supabase/supautils), which is currently being rolled out.
</Admonition>


### `RAISE`d log messages in Postgres

Messages that are manually logged via `RAISE INFO`, `RAISE NOTICE`, `RAISE WARNING`, and `RAISE LOG` are shown in Postgres Logs. Note that only messages at or above your logging level are shown. Syncing of messages to Postgres Logs may take a few minutes.

If your logs aren't showing, check your logging level by running:

```sql
show log_min_messages;
```

Note that `LOG` is a higher level than `WARNING` and `ERROR`, so if your level is set to `LOG`, you will not see `WARNING` and `ERROR` messages.



## Logging realtime connections

Realtime doesn't log new WebSocket connections or Channel joins by default. Enable connection logging per client by including an `info` `log_level` parameter when instantiating the Supabase client.

```javascript
import { createClient } from '@supabase/supabase-js'

const options = {
  realtime: {
    params: {
      log_level: 'info',
    },
  },
}
const supabase = createClient('https://xyzcompany.supabase.co', 'publishable-or-anon-key', options)
```



## Logs Explorer

The [Logs Explorer](/dashboard/project/_/logs-explorer) exposes logs from each part of the Supabase stack as a separate table that can be queried and joined using SQL.

![Logs Explorer](/docs/img/guides/platform/logs/logs-explorer.png)

You can access the following logs from the **Sources** drop-down:

*   `auth_logs`: GoTrue server logs, containing authentication/authorization activity.
*   `edge_logs`: Edge network logs, containing request and response metadata retrieved from Cloudflare.
*   `function_edge_logs`: Edge network logs for only edge functions, containing network requests and response metadata for each execution.
*   `function_logs`: Function internal logs, containing any `console` logging from within the edge function.
*   `postgres_logs`: Postgres database logs, containing statements executed by connected applications.
*   `realtime_logs`: Realtime server logs, containing client connection information.
*   `storage_logs`: Storage server logs, containing object upload and retrieval information.



## Querying with the Logs Explorer

The Logs Explorer uses BigQuery and supports all [available SQL functions and operators](https://cloud.google.com/bigquery/docs/reference/standard-sql/functions-and-operators).


### Timestamp display and behavior

Each log entry is stored with a `timestamp` as a `TIMESTAMP` data type. Use the appropriate [timestamp function](https://cloud.google.com/bigquery/docs/reference/standard-sql/timestamp_functions#timestamp) to utilize the `timestamp` field in a query.

Raw top-level timestamp values are rendered as unix microsecond. To render the timestamps in a human-readable format, use the `DATETIME()` function to convert the unix timestamp display into an ISO-8601 timestamp.

```sql
-- timestamp column without datetime()
select timestamp from ....
--  1664270180000

-- timestamp column with datetime()
select datetime(timestamp) from ....
-- 2022-09-27T09:17:10.439Z
```


### Unnesting arrays

Each log event stores metadata an array of objects with multiple levels, and can be seen by selecting single log events in the Logs Explorer. To query arrays, use `unnest()` on each array field and add it to the query as a join. This allows you to reference the nested objects with an alias and select their individual fields.

For example, to query the edge logs without any joins:

```sql
select timestamp, metadata from edge_logs as t;
```

The resulting `metadata` key is rendered as an array of objects in the Logs Explorer. In the following diagram, each box represents a nested array of objects:

{/* <!-- Scene is here https://app.excalidraw.com/s/8gj16loJfGZ/3HzccK9MyLx --> */}

![Without Unnesting](/docs/img/unnesting-none.png)

Perform a `cross join unnest()` to work with the keys nested in the `metadata` key.

To query for a nested value, add a join for each array level:

```sql
select timestamp, request.method, header.cf_ipcountry
from
  edge_logs as t
  cross join unnest(t.metadata) as metadata
  cross join unnest(metadata.request) as request
  cross join unnest(request.headers) as header;
```

This surfaces the following columns available for selection:
![With Two Level Unnesting](/docs/img/unnesting-2.png)

This allows you to select the `method` and `cf_ipcountry` columns. In JS dot notation, the full paths for each selected column are:

*   `metadata[].request[].method`
*   `metadata[].request[].headers[].cf_ipcountry`


### LIMIT and result row limitations

The Logs Explorer has a maximum of 1000 rows per run. Use `LIMIT` to optimize your queries by reducing the number of rows returned further.


### Best practices

1.  Include a filter over **timestamp**

Querying your entire log history might seem appealing. For **Enterprise** customers that have a large retention range, you run the risk of timeouts due additional time required to scan the larger dataset.

2.  Avoid selecting large nested objects. Select individual values instead.

When querying large objects, the columnar storage engine selects each column associated with each nested key, resulting in a large number of columns being selected. This inadvertently impacts the query speed and may result in timeouts or memory errors, especially for projects with a lot of logs.

Instead, select only the values required.

```sql
-- ❌ Avoid doing this
select
  datetime(timestamp),
  m as metadata -- <- metadata contains many nested keys
from
  edge_logs as t
  cross join unnest(t.metadata) as m;

-- ✅ Do this
select
  datetime(timestamp),
  r.method -- <- select only the required values
from
  edge_logs as t
  cross join unnest(t.metadata) as m
  cross join unnest(m.request) as r;
```


### Examples and templates

The Logs Explorer includes **Templates** (available in the Templates tab or the dropdown in the Query tab) to help you get started.

For example, you can enter the following query in the SQL Editor to retrieve each user's IP address:

```sql
select datetime(timestamp), h.x_real_ip
from
  edge_logs
  cross join unnest(metadata) as m
  cross join unnest(m.request) as r
  cross join unnest(r.headers) as h
where h.x_real_ip is not null and r.method = "GET";
```


### Logs field reference

Refer to the full field reference for each available source below. Do note that in order to access each nested key, you would need to perform the [necessary unnesting joins](#unnesting-arrays)

<SharedData data="logConstants">
  {(logConstants) => (
        <Tabs scrollable size="small" type="underlined" defaultActiveId="edge_logs" queryGroup="source">
          {logConstants.schemas.map((schema) => (
            <TabPanel id={schema.reference} key={schema.reference} label={schema.name}>
              <table>
                <thead>
                  <tr>
                    <th className="font-bold">Path</th>
                    <th className="font-bold">Type</th>
                  </tr>
                </thead>
                <tbody>
                  {schema.fields
                    .sort((a, b) => a.path - b.path)
                    .map((field) => (
                      <tr>
                        <td className="font-mono">{field.path}</td>
                        <td className="font-mono">{field.type}</td>
                      </tr>
                    ))}
                </tbody>
              </table>
            </TabPanel>
          ))}
        </Tabs>
      )}
</SharedData>



---
**Navigation:** ← Previous | [Index](./index.md) | [Next →](./02-metrics.md)
