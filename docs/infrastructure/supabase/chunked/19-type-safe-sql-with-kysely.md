**Navigation:** [← Previous](./18-use-supabase-with-sveltekit.md) | [Index](./index.md) | [Next →](./20-custom-auth-emails-with-react-email-and-resend.md)

# Type-Safe SQL with Kysely



<div class="video-container">
  <iframe src="https://www.youtube-nocookie.com/embed/zd9a_Lk3jAc" frameBorder="1" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />
</div>

Supabase Edge Functions can [connect directly to your Postgres database](/docs/guides/functions/connect-to-postgres) to execute SQL queries. [Kysely](https://github.com/kysely-org/kysely#kysely) is a type-safe and autocompletion-friendly typescript SQL query builder.

Combining Kysely with Deno Postgres gives you a convenient developer experience for interacting directly with your Postgres database.



## Code

Find the example on [GitHub](https://github.com/supabase/supabase/tree/master/examples/edge-functions/supabase/functions/kysely-postgres)

Get your database connection credentials from the project's [**Connect** panel](/dashboard/project/_/?showConnect=true) and store them in an `.env` file:

```bash .env
DB_HOSTNAME=
DB_PASSWORD=
DB_SSL_CERT="-----BEGIN CERTIFICATE-----
GET YOUR CERT FROM YOUR PROJECT DASHBOARD
-----END CERTIFICATE-----"
```

Create a `DenoPostgresDriver.ts` file to manage the connection to Postgres via [deno-postgres](https://deno-postgres.com/):

```ts DenoPostgresDriver.ts
import {
  CompiledQuery,
  DatabaseConnection,
  Driver,
  PostgresCursorConstructor,
  QueryResult,
  TransactionSettings,
} from 'https://esm.sh/kysely@0.23.4'
import { freeze, isFunction } from 'https://esm.sh/kysely@0.23.4/dist/esm/util/object-utils.js'
import { extendStackTrace } from 'https://esm.sh/kysely@0.23.4/dist/esm/util/stack-trace-utils.js'
import { Pool, PoolClient } from 'https://deno.land/x/postgres@v0.17.0/mod.ts'

export interface PostgresDialectConfig {
  pool: Pool | (() => Promise<Pool>)
  cursor?: PostgresCursorConstructor
  onCreateConnection?: (connection: DatabaseConnection) => Promise<void>
}

const PRIVATE_RELEASE_METHOD = Symbol()

export class PostgresDriver implements Driver {
  readonly #config: PostgresDialectConfig
  readonly #connections = new WeakMap<PoolClient, DatabaseConnection>()
  #pool?: Pool

  constructor(config: PostgresDialectConfig) {
    this.#config = freeze({ ...config })
  }

  async init(): Promise<void> {
    this.#pool = isFunction(this.#config.pool) ? await this.#config.pool() : this.#config.pool
  }

  async acquireConnection(): Promise<DatabaseConnection> {
    const client = await this.#pool!.connect()
    let connection = this.#connections.get(client)

    if (!connection) {
      connection = new PostgresConnection(client, {
        cursor: this.#config.cursor ?? null,
      })
      this.#connections.set(client, connection)

      // The driver must take care of calling `onCreateConnection` when a new
      // connection is created. The `pg` module doesn't provide an async hook
      // for the connection creation. We need to call the method explicitly.
      if (this.#config?.onCreateConnection) {
        await this.#config.onCreateConnection(connection)
      }
    }

    return connection
  }

  async beginTransaction(
    connection: DatabaseConnection,
    settings: TransactionSettings
  ): Promise<void> {
    if (settings.isolationLevel) {
      await connection.executeQuery(
        CompiledQuery.raw(`start transaction isolation level ${settings.isolationLevel}`)
      )
    } else {
      await connection.executeQuery(CompiledQuery.raw('begin'))
    }
  }

  async commitTransaction(connection: DatabaseConnection): Promise<void> {
    await connection.executeQuery(CompiledQuery.raw('commit'))
  }

  async rollbackTransaction(connection: DatabaseConnection): Promise<void> {
    await connection.executeQuery(CompiledQuery.raw('rollback'))
  }

  async releaseConnection(connection: PostgresConnection): Promise<void> {
    connection[PRIVATE_RELEASE_METHOD]()
  }

  async destroy(): Promise<void> {
    if (this.#pool) {
      const pool = this.#pool
      this.#pool = undefined
      await pool.end()
    }
  }
}

interface PostgresConnectionOptions {
  cursor: PostgresCursorConstructor | null
}

class PostgresConnection implements DatabaseConnection {
  #client: PoolClient
  #options: PostgresConnectionOptions

  constructor(client: PoolClient, options: PostgresConnectionOptions) {
    this.#client = client
    this.#options = options
  }

  async executeQuery<O>(compiledQuery: CompiledQuery): Promise<QueryResult<O>> {
    try {
      const result = await this.#client.queryObject<O>(compiledQuery.sql, [
        ...compiledQuery.parameters,
      ])

      if (
        result.command === 'INSERT' ||
        result.command === 'UPDATE' ||
        result.command === 'DELETE'
      ) {
        const numAffectedRows = BigInt(result.rowCount || 0)

        return {
          numUpdatedOrDeletedRows: numAffectedRows,
          numAffectedRows,
          rows: result.rows ?? [],
        } as any
      }

      return {
        rows: result.rows ?? [],
      }
    } catch (err) {
      throw extendStackTrace(err, new Error())
    }
  }

  async *streamQuery<O>(
    _compiledQuery: CompiledQuery,
    chunkSize: number
  ): AsyncIterableIterator<QueryResult<O>> {
    if (!this.#options.cursor) {
      throw new Error(
        "'cursor' is not present in your postgres dialect config. It's required to make streaming work in postgres."
      )
    }

    if (!Number.isInteger(chunkSize) || chunkSize <= 0) {
      throw new Error('chunkSize must be a positive integer')
    }

    // stream not available
    return null
  }

  [PRIVATE_RELEASE_METHOD](): void {
    this.#client.release()
  }
}
```

Create an `index.ts` file to execute a query on incoming requests:

```ts index.ts
import { serve } from 'https://deno.land/std@0.175.0/http/server.ts'
import { Pool } from 'https://deno.land/x/postgres@v0.17.0/mod.ts'
import {
  Kysely,
  Generated,
  PostgresAdapter,
  PostgresIntrospector,
  PostgresQueryCompiler,
} from 'https://esm.sh/kysely@0.23.4'
import { PostgresDriver } from './DenoPostgresDriver.ts'

console.log(`Function "kysely-postgres" up and running!`)

interface AnimalTable {
  id: Generated<bigint>
  animal: string
  created_at: Date
}

// Keys of this interface are table names.
interface Database {
  animals: AnimalTable
}

// Create a database pool with one connection.
const pool = new Pool(
  {
    tls: { caCertificates: [Deno.env.get('DB_SSL_CERT')!] },
    database: 'postgres',
    hostname: Deno.env.get('DB_HOSTNAME'),
    user: 'postgres',
    port: 5432,
    password: Deno.env.get('DB_PASSWORD'),
  },
  1
)

// You'd create one of these when you start your app.
const db = new Kysely<Database>({
  dialect: {
    createAdapter() {
      return new PostgresAdapter()
    },
    createDriver() {
      return new PostgresDriver({ pool })
    },
    createIntrospector(db: Kysely<unknown>) {
      return new PostgresIntrospector(db)
    },
    createQueryCompiler() {
      return new PostgresQueryCompiler()
    },
  },
})

serve(async (_req) => {
  try {
    // Run a query
    const animals = await db.selectFrom('animals').select(['id', 'animal', 'created_at']).execute()

    // Neat, it's properly typed \o/
    console.log(animals[0].created_at.getFullYear())

    // Encode the result as pretty printed JSON
    const body = JSON.stringify(
      animals,
      (key, value) => (typeof value === 'bigint' ? value.toString() : value),
      2
    )

    // Return the response with the correct content type header
    return new Response(body, {
      status: 200,
      headers: {
        'Content-Type': 'application/json; charset=utf-8',
      },
    })
  } catch (err) {
    console.error(err)
    return new Response(String(err?.message ?? err), { status: 500 })
  }
})
```



# Limits

Limits applied Edge Functions in Supabase's hosted platform.


## Runtime limits

*   Maximum Memory: 256MB
*   Maximum Duration (Wall clock limit):
    This is the duration an Edge Function worker will stay active. During this period, a worker can serve multiple requests or process background tasks.
    *   Free plan: 150s
    *   Paid plans: 400s
*   Maximum CPU Time: 2s (Amount of actual time spent on the CPU per request - does not include async I/O.)
*   Request idle timeout: 150s (If an Edge Function doesn't send a response before the timeout, 504 Gateway Timeout will be returned)



## Platform limits

*   Maximum Function Size: 20MB (After bundling using CLI)
*   Maximum no. of Functions per project:
    *   Free: 100
    *   Pro: 500
    *   Team: 1000
    *   Enterprise: Unlimited
*   Maximum log message length: 10,000 characters
*   Log event threshold: 100 events per 10 seconds



## Other limits & restrictions

*   Outgoing connections to ports `25` and `587` are not allowed.
*   Serving of HTML content is only supported with [custom domains](/docs/reference/cli/supabase-domains) (Otherwise `GET` requests that return `text/html` will be rewritten to `text/plain`).
*   Web Worker API (or Node `vm` API) are not available.
*   Static files cannot be deployed using the API flag. You need to build them with [Docker on the CLI](/docs/guides/functions/quickstart#step-6-deploy-to-production).
*   Node Libraries that require multithreading are not supported. Examples: [`libvips`](https://github.com/libvips/libvips), [sharp](https://github.com/lovell/sharp).



# Logging

Monitor your Edge Functions with logging to track execution, debug issues, and optimize performance.

Logs are provided for each function invocation, locally and in hosted environments.

***



## Accessing logs


### Production

Access logs from the Functions section of your Dashboard:

1.  Navigate to the [Functions section](/dashboard/project/_/functions) of the Dashboard
2.  Select your function from the list
3.  Choose your log view:
    *   **Invocations:** Request/Response data including headers, body, status codes, and execution duration. Filter by date, time, or status code.
    *   **Logs:** Platform events, uncaught exceptions, and custom log messages. Filter by timestamp, level, or message content.

![Function invocations.](/docs/img/guides/functions/function-logs.png)


### Development

When [developing locally](/docs/guides/functions/quickstart) you will see error messages and console log statements printed to your local terminal window.

***



## Log event types


### Automatic logs

Your functions automatically capture several types of events:

*   **Uncaught exceptions**: Uncaught exceptions thrown by a function during execution are automatically logged. You can see the error message and stack trace in the Logs tool.
*   **Custom log events**: You can use `console.log`, `console.error`, and `console.warn` in your code to emit custom log events. These events also appear in the Logs tool.
*   **Boot and Shutdown Logs**: The Logs tool extends its coverage to include logs for the boot and shutdown of functions.


### Custom logs

You can add your own log messages using standard console methods:

```js
Deno.serve(async (req) => {
  try {
    const { name } = await req.json()

    if (!name) {
      // Log a warning message
      console.warn('Empty name parameter received')
    }

    // Log a message
    console.log(`Processing request for: ${name}`)

    const data = {
      message: `Hello ${name || 'Guest'}!`,
    }

    return new Response(JSON.stringify(data), {
      headers: { 'Content-Type': 'application/json' },
    })
  } catch (error) {
    // Log an error message
    console.error(`Request processing failed: ${error.message}`)
    return new Response(JSON.stringify({ error: 'Internal Server Error' }), {
      status: 500,
      headers: { 'Content-Type': 'application/json' },
    })
  }
})
```

<Admonition type="note">
  A custom log message can contain up to 10,000 characters. A function can log up to 100 events within a 10 second period.
</Admonition>

***



## Logging tips


### Logging request headers

When debugging Edge Functions, a common mistake is to try to log headers to the developer console via code like this:

```ts index.ts
// ❌ This doesn't work as expected

Deno.serve(async (req) => {
  console.log(`Headers: ${JSON.stringify(req.headers)}`) // Outputs: "{}"
})
```

The `req.headers` object appears empty because Headers objects don't store data in enumerable JavaScript properties, making them opaque to `JSON.stringify()`.

Instead, you have to convert headers to a plain object first, for example using `Object.fromEntries`.

```ts index.ts
// ✅ This works correctly
Deno.serve(async (req) => {
  const headersObject = Object.fromEntries(req.headers)
  const headersJson = JSON.stringify(headersObject, null, 2)

  console.log(`Request headers:\n${headersJson}`)
})
```

This results in something like:

```json
Request headers: {
    "accept": "*/*",
    "accept-encoding": "gzip",
    "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InN1cGFuYWNobyIsInJvbGUiOiJhbm9uIiwieW91IjoidmVyeSBzbmVha3ksIGh1aD8iLCJpYXQiOjE2NTQ1NDA5MTYsImV4cCI6MTk3MDExNjkxNn0.cwBbk2tq-fUcKF1S0jVKkOAG2FIQSID7Jjvff5Do99Y",
    "cdn-loop": "cloudflare; subreqs=1",
    "cf-ew-via": "15",
    "cf-ray": "8597a2fcc558a5d7-GRU",
    "cf-visitor": "{\"scheme\":\"https\"}",
    "cf-worker": "supabase.co",
    "content-length": "20",
    "content-type": "application/x-www-form-urlencoded",
    "host": "edge-runtime.supabase.com",
    "my-custom-header": "abcd",
    "user-agent": "curl/8.4.0",
    "x-deno-subhost": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImtpZCI6InN1cGFiYXNlIn0.eyJkZXBsb3ltZW50X2lkIjoic3VwYW5hY2hvX2M1ZGQxMWFiLTFjYmUtNDA3NS1iNDAxLTY3ZTRlZGYxMjVjNV8wMDciLCJycGNfcm9vdCI6Imh0dHBzOi8vc3VwYWJhc2Utb3JpZ2luLmRlbm8uZGV2L3YwLyIsImV4cCI6MTcwODYxMDA4MiwiaWF0IjoxNzA4NjA5MTgyfQ.-fPid2kEeEM42QHxWeMxxv2lJHZRSkPL-EhSH0r_iV4",
    "x-forwarded-host": "edge-runtime.supabase.com",
    "x-forwarded-port": "443",
    "x-forwarded-proto": "https"
}
```



# Pricing



<Price price="2" /> per 1 million invocations. You are only charged for usage exceeding your subscription
plan's quota.

| Plan       | Quota     | Over-Usage                                    |
| ---------- | --------- | --------------------------------------------- |
| Free       | 500,000   | -                                             |
| Pro        | 2 million | <Price price="2" /> per 1 million invocations |
| Team       | 2 million | <Price price="2" /> per 1 million invocations |
| Enterprise | Custom    | Custom                                        |

For a detailed explanation of how charges are calculated, refer to [Manage Edge Function Invocations usage](/docs/guides/platform/manage-your-usage/edge-function-invocations).



# Getting Started with Edge Functions (Dashboard)

Learn how to create, test, and deploy your first Edge Function using the Supabase Dashboard.

Supabase allows you to create Supabase Edge Functions directly from the Supabase Dashboard, making it easy to deploy functions without needing to set up a local development environment. The Edge Functions editor in the Dashboard has built-in syntax highlighting and type-checking for Deno and Supabase-specific APIs.

This guide will walk you through creating, testing, and deploying your first Edge Function using the Supabase Dashboard. You'll have a working function running globally in under 10 minutes.

<Admonition type="tip" label="Prefer using the CLI?">
  You can also create and deploy functions using the Supabase CLI. Check out our [CLI Quickstart guide](/docs/guides/functions/quickstart).
</Admonition>

<Admonition type="note" label="New to Supabase?">
  You'll need a Supabase project to get started. If you don't have one yet, create a new project at [database.new](https://database.new/).
</Admonition>

***



## Step 1: Navigate to the Edge Functions tab

Navigate to your Supabase project dashboard and locate the Edge Functions section:

1.  Go to your [Supabase Dashboard](/dashboard)
2.  Select your project
3.  In the left sidebar, click on **Edge Functions**

You'll see the Edge Functions overview page where you can manage all your functions.

***



## Step 2: Create your first function

Click the **"Deploy a new function"** button and select **"Via Editor"** to create a function directly in the dashboard.

<Image
  alt="Scaffold functions through the dashboard editor"
  src={{
    light: '/docs/img/guides/functions/dashboard/create-edge-function--light.png',
    dark: '/docs/img/guides/functions/dashboard/create-edge-function--dark.png',
  }}
  zoomable
/>

<Admonition type="note" label="Pre-built templates">
  The dashboard offers several pre-built templates for common use cases, such as Stripe Webhooks, OpenAI proxying, uploading files to Supabase Storage, and sending emails.

  For this guide, we’ll select the **"Hello World"** template. If you’d rather start from scratch, you can ignore the pre-built templates.
</Admonition>

***



## Step 3: Customize your function code

The dashboard will load your chosen template in the code editor. Here's what the "Hello World" template looks like:

<Image
  alt="Hello World template"
  src={{
    light: '/docs/img/guides/functions/dashboard/edge-function-template--light.png',
    dark: '/docs/img/guides/functions/dashboard/edge-function-template--dark.png',
  }}
  zoomable
/>

If needed, you can modify this code directly in the browser editor. The function accepts a JSON payload with a `name` field and returns a greeting message.

***



## Step 4: Deploy your function

Once you're happy with your function code:

1.  Click the **"Deploy function"** button at the bottom of the editor
2.  Wait for the deployment to complete (usually takes 10-30 seconds)
3.  You'll see a success message when deployment is finished

🚀 Your function is now automatically distributed to edge locations worldwide, running at `https://YOUR_PROJECT_ID.supabase.co/functions/v1/hello-world`

***



## Step 5: Test your function

Supabase has built-in tools for testing your Edge Functions from the Dashboard. You can execute your Edge Function with different request payloads, headers, and query parameters. The built-in tester returns the response status, headers, and body.

On your function's details page:

1.  Click the **"Test"** button
2.  Configure your test request:
    *   **HTTP Method**: POST (or whatever your function expects)
    *   **Headers**: Add any required headers like `Content-Type: application/json`
    *   **Query Parameters**: Add URL parameters if needed
    *   **Request Body**: Add your JSON payload
    *   **Authorization**: Change the authorization token (anon key or user key)

Click **"Send Request"** to test your function.

<Image
  alt="Test your function"
  src={{
    light: '/docs/img/guides/functions/dashboard/edge-function-test--light.png',
    dark: '/docs/img/guides/functions/dashboard/edge-function-test--dark.png',
  }}
  zoomable
/>

In this example, we successfully tested our Hello World function by sending a JSON payload with a name field, and received the expected greeting message back.

***



## Step 6: Get your function URL and keys

Your function is now live at:

```
https://YOUR_PROJECT_ID.supabase.co/functions/v1/hello-world
```

To invoke this Edge Function from within your application, you'll need API keys. Navigate to **Settings > API Keys** in your dashboard to find:

*   **Anon Key** - For client-side requests (safe to use in browsers with RLS enabled)
*   **Service Role Key** - For server-side requests (keep this secret! bypasses RLS)

***

If you’d like to update the deployed function code, click on the function you want to edit, modify the code as needed, then click Deploy updates. This will overwrite the existing deployment with the newly edited function code.

<Admonition type="caution" label="No version control">
  There is currently **no version control** for edits! The Dashboard's Edge Function editor currently does not support version control, versioning, or rollbacks. We recommend using it only for quick testing and prototypes.
</Admonition>

***



## Usage

Now that your function is deployed, you can invoke it from within your app:

<Tabs scrollable size="small" type="underlined" defaultActiveId="supabase-js">
  <TabPanel id="supabase-js" label="Supabase Client">
    ```jsx
    import { createClient } from '@supabase/supabase-js'

    const supabase = createClient('https://[YOUR_PROJECT_ID].supabase.co', 'YOUR_ANON_KEY')

    const { data, error } = await supabase.functions.invoke('hello-world', {
      body: { name: 'JavaScript' },
    })

    console.log(data) // { message: "Hello JavaScript!" }
    ```
  </TabPanel>

  <TabPanel id="fetch" label="Fetch API">
    ```jsx
    const response = await fetch('https://[YOUR_PROJECT_ID].supabase.co/functions/v1/hello-world', {
      method: 'POST',
      headers: {
        Authorization: 'Bearer YOUR_ANON_KEY',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ name: 'Fetch' }),
    })

    const data = await response.json()
    console.log(data) // { message: "Hello Fetch!" }
    ```
  </TabPanel>
</Tabs>

***



## Deploy via Assistant

You can also use Supabase's AI Assistant to generate and deploy functions automatically.

Go to your project > **Deploy a new function** > **Via AI Assistant**.

<Image
  alt="Create Edge Function via AI Assistant"
  src={{
    light: '/docs/img/guides/functions/dashboard/create-ai-edge-function--light.png',
    dark: '/docs/img/guides/functions/dashboard/create-ai-edge-function--dark.png',
  }}
  zoomable
/>

Describe what you want your function to do in the prompt

<Image
  alt="Create Edge Function via AI Assistant"
  src={{
    light: '/docs/img/guides/functions/dashboard/ai-edge-function--light.png',
    dark: '/docs/img/guides/functions/dashboard/ai-edge-function--dark.png',
  }}
  zoomable
/>

Click **Deploy** and the Assistant will create and deploy the function for you.

***



## Download Edge Functions

Now that your function is deployed, you can access it from your local development environment. To use your Edge Function code within your local development environment, you can download your function source code either through the dashboard, or the CLI.


### Dashboard

1.  Go to your function's page
2.  In the top right corner, click the **"Download"** button


### CLI

<Admonition type="note" label="CLI not installed?">
  Before getting started, make sure you have the **Supabase CLI installed**. Check out the [CLI installation guide](/docs/guides/cli) for installation methods and troubleshooting.
</Admonition>

```bash

# Link your project to your local environment
supabase link --project-ref [project-ref]


# List all functions in the linked project
supabase functions list


# Download a function
supabase functions download hello-world
```

At this point, your function has been downloaded to your local environment. Make the required changes, and redeploy when you're ready.

```bash

# Run a function locally
supabase functions serve hello-world


# Redeploy when you're ready with your changes
supabase functions deploy hello-world
```



# Getting Started with Edge Functions

Learn how to create, test, and deploy your first Edge Function using the Supabase CLI.

Before getting started, make sure you have the **Supabase CLI installed**. Check out the [CLI installation guide](/docs/guides/cli) for installation methods and troubleshooting.

<Admonition type="tip" label="Prefer using the Supabase Dashboard?">
  You can also create and deploy functions directly from the Supabase Dashboard. Check out our [Dashboard Quickstart guide](/docs/guides/functions/quickstart-dashboard).
</Admonition>

***



## Step 1: Create or configure your project

If you don't have a project yet, initialize a new Supabase project in your current directory.

```bash
supabase init my-edge-functions-project
cd my-edge-functions-project
```

Or, if you already have a project locally, navigate to your project directory. If your project hasn't been configured for Supabase yet, make sure to run the `supabase init` command.

```bash
cd your-existing-project
supabase init # Initialize Supabase, if you haven't already
```

<Admonition type="note">
  After this step, you should have a project directory with a `supabase` folder containing `config.toml` and an empty `functions` directory.
</Admonition>

***



## Step 2: Create your first function

Within your project, generate a new Edge Function with a basic template:

```bash
supabase functions new hello-world
```

This creates a new function at `supabase/functions/hello-world/index.ts` with this starter code:

```tsx
Deno.serve(async (req) => {
  const { name } = await req.json()
  const data = {
    message: `Hello ${name}!`,
  }

  return new Response(JSON.stringify(data), { headers: { 'Content-Type': 'application/json' } })
})
```

This function accepts a JSON payload with a `name` field and returns a greeting message.

<Admonition type="note">
  After this step, you should have a new file at `supabase/functions/hello-world/index.ts` containing the starter Edge Function code.
</Admonition>

***



## Step 3: Test your function locally

Start the local development server to test your function:

```bash
supabase start  # Start all Supabase services
supabase functions serve hello-world
```

<Admonition type="note" label="First time running Supabase services?">
  The `supabase start` command downloads Docker images, which can take a few minutes initially.
</Admonition>

<Admonition type="note">
  **Function not starting locally?**

  *   Make sure Docker is running
  *   Run `supabase stop` then `supabase start` to restart services

  **Port already in use?**

  *   Check what's running with `supabase status`
  *   Stop other Supabase instances with `supabase stop`
</Admonition>

Your function is now running at [`http://localhost:54321/functions/v1/hello-world`](http://localhost:54321/functions/v1/hello-world). Hot reloading is enabled, which means that the server will automatically reload when you save changes to your function code.

<Admonition type="note">
  After this step, you should have all Supabase services running locally, and your Edge Function serving at the local URL. Keep these terminal windows open.
</Admonition>

***



## Step 4: Send a test request

Open a new terminal and test your function with curl:

<Admonition type="tip">
  **Need your `SUPABASE_PUBLISHABLE_KEY`?**

  Run `supabase status` to see your local anon key and other credentials.
</Admonition>

```bash
curl -i --location --request POST 'http://localhost:54321/functions/v1/hello-world' \
  --header 'Authorization: Bearer SUPABASE_PUBLISHABLE_KEY' \
  --header 'Content-Type: application/json' \
  --data '{"name":"Functions"}'
```

After running this curl command, you should see:

```json
{ "message": "Hello Functions!" }
```

You can also try different inputs. Change `"Functions"` to `"World"` in the curl command and run it again to see the response change.

<Admonition type="note">
  After this step, you should have successfully tested your Edge Function locally and received a JSON response with your greeting message.
</Admonition>

***



## Step 5: Connect to your Supabase project

To deploy your function globally, you need to connect your local project to a Supabase project.

<Admonition type="tip" label="Need to create new Supabase project?">
  Create one at [database.new](https://database.new/).
</Admonition>

First, login to the CLI if you haven't already, and authenticate with Supabase. This opens your browser to authenticate with Supabase; complete the login process in your browser.

```bash
supabase login
```

Next, list your Supabase projects to find your project ID:

```bash
supabase projects list
```

Next, copy your project ID from the output, then connect your local project to your remote Supabase project. Replace `YOUR_PROJECT_ID` with the ID from the previous step.

```bash
supabase link --project-ref [YOUR_PROJECT_ID]
```

<Admonition type="note">
  After this step, you should have your local project authenticated and linked to your remote Supabase project. You can verify this by running `supabase status`.
</Admonition>

***



## Step 6: Deploy to production

Deploy your function to Supabase's global edge network:

```bash
supabase functions deploy hello-world


# If you want to deploy all functions, run the `deploy` command without specifying a function name:
supabase functions deploy
```

<Admonition type="tip" label="Docker not required">
  The CLI automatically falls back to API-based deployment if Docker isn't available. You can also explicitly use API deployment with the `--use-api` flag:

  ```bash
  supabase functions deploy hello-world --use-api
  ```
</Admonition>

If you want to skip JWT verification, you can add the `--no-verify-jwt` flag for webhooks that don't need authentication:

```bash
supabase functions deploy hello-world --no-verify-jwt
```

<Admonition type="caution" label="Security Warning">
  **Use `--no-verify-jwt` carefully.** It allows anyone to invoke your function without authentication!
</Admonition>

When the deployment is successful, your function is automatically distributed to edge locations worldwide.

<Admonition type="note">
  Now, you should have your Edge Function deployed and running globally at `https://[YOUR_PROJECT_ID].supabase.co/functions/v1/hello-world`.
</Admonition>

***



## Step 7: Test your live function

🎉 Your function is now live! Test it with your project's anon key:

```bash
curl --request POST 'https://[YOUR_PROJECT_ID].supabase.co/functions/v1/hello-world' \
  --header 'Authorization: Bearer SUPABASE_PUBLISHABLE_KEY' \
  --header 'Content-Type: application/json' \
  --data '{"name":"Production"}'
```

**Expected response:**

```json
{ "message": "Hello Production!" }
```

<Admonition type="note" label="Production vs Development Keys">
  The `SUPABASE_PUBLISHABLE_KEY` is different in development and production. To get your production anon key, you can find it in your Supabase dashboard under **Settings > API**.
</Admonition>

Finally, you should have a fully deployed Edge Function that you can call from anywhere in the world.

***



## Usage

Now that your function is deployed, you can invoke it from within your app:

<Tabs scrollable size="small" type="underlined" defaultActiveId="supabase-js">
  <TabPanel id="supabase-js" label="Supabase Client">
    ```jsx
    import { createClient } from '@supabase/supabase-js'

    const supabase = createClient('https://[YOUR_PROJECT_ID].supabase.co', 'YOUR_ANON_KEY')

    const { data, error } = await supabase.functions.invoke('hello-world', {
      body: { name: 'JavaScript' },
    })

    console.log(data) // { message: "Hello JavaScript!" }
    ```
  </TabPanel>

  <TabPanel id="fetch" label="Fetch API">
    ```jsx
    const response = await fetch('https://[YOUR_PROJECT_ID].supabase.co/functions/v1/hello-world', {
      method: 'POST',
      headers: {
        Authorization: 'Bearer YOUR_ANON_KEY',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ name: 'Fetch' }),
    })

    const data = await response.json()
    console.log(data)
    ```
  </TabPanel>
</Tabs>



# Regional Invocations

Execute Edge Functions in specific regions for optimal performance.

Edge Functions automatically execute in the region closest to the user making the request. This reduces network latency and provides faster responses.

However, if your function performs intensive database or storage operations, executing in the same region as your database often provides better performance:

*   **Bulk database operations:** Adding or editing many records
*   **File uploads:** Processing large files or multiple uploads
*   **Complex queries:** Operations requiring multiple database round trips

***



## Available regions

The following regions are supported:

**Asia Pacific:**

*   `ap-northeast-1` (Tokyo)
*   `ap-northeast-2` (Seoul)
*   `ap-south-1` (Mumbai)
*   `ap-southeast-1` (Singapore)
*   `ap-southeast-2` (Sydney)

**North America:**

*   `ca-central-1` (Canada Central)
*   `us-east-1` (N. Virginia)
*   `us-west-1` (N. California)
*   `us-west-2` (Oregon)

**Europe:**

*   `eu-central-1` (Frankfurt)
*   `eu-west-1` (Ireland)
*   `eu-west-2` (London)
*   `eu-west-3` (Paris)

**South America:**

*   `sa-east-1` (São Paulo)

***



## Usage

You can specify the region programmatically using the Supabase Client library, or using the `x-region` HTTP header.

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="JavaScript" label="JavaScript">
    ```js name=JavaScript
    import { createClient, FunctionRegion } from '@supabase/supabase-js'

    const { data, error } = await supabase.functions.invoke('function-name', {
      ...
      region: FunctionRegion.UsEast1, // Execute in us-east-1 region
    })
    ```
  </TabPanel>

  <TabPanel id="cURL" label="cURL">
    ```bash name=cURL
    curl --request POST 'https://<project_ref>.supabase.co/functions/v1/function-name' \
      --header 'x-region: us-east-1'  # Execute in us-east-1 region
    ```
  </TabPanel>
</Tabs>

In case you cannot add the `x-region` header to the request (e.g.: CORS requests, Webhooks), you can use `forceFunctionRegion` query parameter.

<Admonition type="note">
  You can verify the execution region by looking at the `x-sb-edge-region` HTTP header in the response. You can also find it as metadata in [Edge Function Logs](/docs/guides/functions/logging).
</Admonition>

***



## Region outages

When you explicitly specify a region via the `x-region` header, requests will NOT be automatically
re-routed to another region.

During outages, consider temporarily changing to a different region.

<Admonition type="caution">
  Test your function's performance with and without regional specification to determine if the benefits outweigh automatic region selection.
</Admonition>



# Handling Routing in Functions

Handle custom routing within Edge Functions.

Usually, an Edge Function is written to perform a single action (e.g. write a record to the database). However, if your app's logic is split into multiple Edge Functions, requests to each action may seem slower.

Each Edge Function needs to be booted before serving a request (known as cold starts). If an action is performed less frequently (e.g. deleting a record), there is a high chance of that function experiencing a cold start.

One way to reduce cold starts and increase performance is to combine multiple actions into a single Edge Function. This way only one instance needs to be booted and it can handle multiple requests to different actions.

This allows you to:

*   Reduce cold starts by combining multiple actions into one function
*   Build complete REST APIs in a single function
*   Improve performance by keeping one instance warm for multiple endpoints

***

For example, we can use a single Edge Function to create a typical CRUD API (create, read, update, delete records).

To combine multiple endpoints into a single Edge Function, you can use web application frameworks such as [Express](https://expressjs.com/), [Oak](https://oakserver.github.io/oak/), or [Hono](https://hono.dev).

***



## Basic routing example

Here's a simple hello world example using some popular web frameworks:

<Tabs scrollable size="small" type="underlined" defaultActiveId="hono" queryGroup="framework">
  <TabPanel id="deno" label="Deno">
    ```ts
    Deno.serve(async (req) => {
      if (req.method === 'GET') {
        return new Response('Hello World!')
      }
      const { name } = await req.json()
      if (name) {
        return new Response(`Hello ${name}!`)
      }
      return new Response('Hello World!')
    })
    ```
  </TabPanel>

  <TabPanel id="expressjs" label="Express">
    ```ts
    import express from 'npm:express@4.18.2'

    const app = express()
    app.use(express.json())
    // If you want a payload larger than 100kb, then you can tweak it here:
    // app.use( express.json({ limit : "300kb" }));

    const port = 3000

    app.get('/hello-world', (req, res) => {
      res.send('Hello World!')
    })

    app.post('/hello-world', (req, res) => {
      const { name } = req.body
      res.send(`Hello ${name}!`)
    })

    app.listen(port, () => {
      console.log(`Example app listening on port ${port}`)
    })
    ```
  </TabPanel>

  <TabPanel id="oak" label="Oak">
    ```ts
    import { Application } from 'jsr:@oak/oak@15/application'
    import { Router } from 'jsr:@oak/oak@15/router'

    const router = new Router()

    router.get('/hello-world', (ctx) => {
      ctx.response.body = 'Hello world!'
    })

    router.post('/hello-world', async (ctx) => {
      const { name } = await ctx.request.body.json()
      ctx.response.body = `Hello ${name}!`
    })

    const app = new Application()
    app.use(router.routes())
    app.use(router.allowedMethods())

    app.listen({ port: 3000 })
    ```
  </TabPanel>

  <TabPanel id="hono" label="Hono">
    ```ts
    import { Hono } from 'jsr:@hono/hono'

    const app = new Hono()

    app.post('/hello-world', async (c) => {
      const { name } = await c.req.json()
      return new Response(`Hello ${name}!`)
    })

    app.get('/hello-world', (c) => {
      return new Response('Hello World!')
    })

    Deno.serve(app.fetch)
    ```
  </TabPanel>
</Tabs>

<Admonition type="caution">
  Within Edge Functions, paths should always be prefixed with the function name (in this case `hello-world`).
</Admonition>

***



## Using route parameters

You can use route parameters to capture values at specific URL segments (e.g. `/tasks/:taskId/notes/:noteId`).

Keep in mind paths must be prefixed by function name. Route parameters can only be used after the function name prefix.

<Tabs scrollable size="small" type="underlined" defaultActiveId="deno" queryGroup="framework">
  <TabPanel id="deno" label="Deno">
    ```ts
    interface Task {
      id: string
      name: string
    }

    let tasks: Task[] = []

    const router = new Map<string, (req: Request) => Promise<Response>>()

    async function getAllTasks(): Promise<Response> {
      return new Response(JSON.stringify(tasks))
    }

    async function getTask(id: string): Promise<Response> {
      const task = tasks.find((t) => t.id === id)
      if (task) {
        return new Response(JSON.stringify(task))
      } else {
        return new Response('Task not found', { status: 404 })
      }
    }

    async function createTask(req: Request): Promise<Response> {
      const id = Math.random().toString(36).substring(7)
      const task = { id, name: '' }
      tasks.push(task)
      return new Response(JSON.stringify(task), { status: 201 })
    }

    async function updateTask(id: string, req: Request): Promise<Response> {
      const index = tasks.findIndex((t) => t.id === id)
      if (index !== -1) {
        tasks[index] = { ...tasks[index] }
        return new Response(JSON.stringify(tasks[index]))
      } else {
        return new Response('Task not found', { status: 404 })
      }
    }

    async function deleteTask(id: string): Promise<Response> {
      const index = tasks.findIndex((t) => t.id === id)
      if (index !== -1) {
        tasks.splice(index, 1)
        return new Response('Task deleted successfully')
      } else {
        return new Response('Task not found', { status: 404 })
      }
    }

    Deno.serve(async (req) => {
      const url = new URL(req.url)
      const method = req.method
      // Extract the last part of the path as the command
      const command = url.pathname.split('/').pop()
      // Assuming the last part of the path is the task ID
      const id = command
      try {
        switch (method) {
          case 'GET':
            if (id) {
              return getTask(id)
            } else {
              return getAllTasks()
            }
          case 'POST':
            return createTask(req)
          case 'PUT':
            if (id) {
              return updateTask(id, req)
            } else {
              return new Response('Bad Request', { status: 400 })
            }
          case 'DELETE':
            if (id) {
              return deleteTask(id)
            } else {
              return new Response('Bad Request', { status: 400 })
            }
          default:
            return new Response('Method Not Allowed', { status: 405 })
        }
      } catch (error) {
        return new Response(`Internal Server Error: ${error}`, { status: 500 })
      }
    })
    ```
  </TabPanel>

  <TabPanel id="expressjs" label="Express">
    ```ts
    import express from 'npm:express@4.18.2'

    const app = express()
    app.use(express.json())

    app.get('/tasks', async (req, res) => {
      // return all tasks
    })

    app.post('/tasks', async (req, res) => {
      // create a task
    })

    app.get('/tasks/:id', async (req, res) => {
      const id = req.params.id
      const task = {} // get task

      res.json(task)
    })

    app.patch('/tasks/:id', async (req, res) => {
      const id = req.params.id
      // modify task
    })

    app.delete('/tasks/:id', async (req, res) => {
      const id = req.params.id
      // delete task
    })
    ```
  </TabPanel>

  <TabPanel id="oak" label="Oak">
    ```ts
    import { Application } from 'jsr:@oak/oak/application'
    import { Router } from 'jsr:@oak/oak/router'

    const router = new Router()

    let tasks: { [id: string]: any } = {}

    router
      .get('/tasks', (ctx) => {
        ctx.response.body = Object.values(tasks)
      })
      .post('/tasks', async (ctx) => {
        const body = ctx.request.body()
        const { name } = await body.value
        const id = Math.random().toString(36).substring(7)
        tasks[id] = { id, name }
        ctx.response.body = tasks[id]
      })
      .get('/tasks/:id', (ctx) => {
        const id = ctx.params.id
        const task = tasks[id]
        if (task) {
          ctx.response.body = task
        } else {
          ctx.response.status = 404
          ctx.response.body = 'Task not found'
        }
      })
      .patch('/tasks/:id', async (ctx) => {
        const id = ctx.params.id
        const body = ctx.request.body()
        const updates = await body.value
        const task = tasks[id]
        if (task) {
          tasks[id] = { ...task, ...updates }
          ctx.response.body = tasks[id]
        } else {
          ctx.response.status = 404
          ctx.response.body = 'Task not found'
        }
      })
      .delete('/tasks/:id', (ctx) => {
        const id = ctx.params.id
        if (tasks[id]) {
          delete tasks[id]
          ctx.response.body = 'Task deleted successfully'
        } else {
          ctx.response.status = 404
          ctx.response.body = 'Task not found'
        }
      })

    const app = new Application()
    app.use(router.routes())
    app.use(router.allowedMethods())

    app.listen({ port: 3000 })
    ```
  </TabPanel>

  <TabPanel id="hono" label="Hono">
    ```ts
    import { Hono } from 'jsr:@hono/hono'

    // You can set the basePath with Hono
    const functionName = 'tasks'
    const app = new Hono().basePath(`/${functionName}`)

    // /tasks/id
    app.get('/:id', async (c) => {
      const id = c.req.param('id')
      const task = {} // Fetch task by id here
      if (task) {
        return new Response(JSON.stringify(task))
      } else {
        return new Response('Task not found', { status: 404 })
      }
    })

    app.patch('/:id', async (c) => {
      const id = c.req.param('id')
      const body = await c.req.body()
      const updates = body.value
      const task = {} // Fetch task by id here
      if (task) {
        Object.assign(task, updates)
        return new Response(JSON.stringify(task))
      } else {
        return new Response('Task not found', { status: 404 })
      }
    })

    app.delete('/:id', async (c) => {
      const id = c.req.param('id')
      const task = {} // Fetch task by id here
      if (task) {
        // Delete task
        return new Response('Task deleted successfully')
      } else {
        return new Response('Task not found', { status: 404 })
      }
    })

    Deno.serve(app.fetch)
    ```
  </TabPanel>
</Tabs>

***

{/* supa-mdx-lint-disable Rule001HeadingCase */}



## URL Patterns API

If you prefer not to use a web framework, you can directly use [URL Pattern API](https://developer.mozilla.org/en-US/docs/Web/API/URL_Pattern_API) within your Edge Functions to implement routing.

This works well for small apps with only a couple of routes:

<CodeSampleWrapper source="https://github.com/supabase/supabase/blob/2415776436927dedb360dae082d03caee607891a/examples/edge-functions/supabase/functions/restful-tasks/index.ts">
  ```typescript restful-tasks/index.ts
  // ...

      // For more details on URLPattern, check https://developer.mozilla.org/en-US/docs/Web/API/URL_Pattern_API
      const taskPattern = new URLPattern({ pathname: '/restful-tasks/:id' })
      const matchingPath = taskPattern.exec(url)
      const id = matchingPath ? matchingPath.pathname.groups.id : null

      let task = null
      if (method === 'POST' || method === 'PUT') {
        const body = await req.json()
        task = body.task
      }

      // call relevant method based on method and id
      switch (true) {
        case id && method === 'GET':
          return getTask(supabaseClient, id as string)
        case id && method === 'PUT':
          return updateTask(supabaseClient, id as string, task)
        case id && method === 'DELETE':
          return deleteTask(supabaseClient, id as string)
        case method === 'POST':
          return createTask(supabaseClient, task)
        case method === 'GET':
          return getAllTasks(supabaseClient)
        default:
          return getAllTasks(supabaseClient)

      // ...
  ```
</CodeSampleWrapper>



# Scheduling Edge Functions



<div class="video-container">
  <iframe src="https://www.youtube-nocookie.com/embed/-U6DJcjVvGo" frameBorder="1" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />
</div>

The hosted Supabase Platform supports the [`pg_cron` extension](/docs/guides/database/extensions/pgcron), a recurring job scheduler in Postgres.

In combination with the [`pg_net` extension](/docs/guides/database/extensions/pgnet), this allows us to invoke Edge Functions periodically on a set schedule.

<Admonition type="caution">
  To access the auth token securely for your Edge Function call, we recommend storing them in [Supabase Vault](/docs/guides/database/vault).
</Admonition>



## Examples


### Invoke an Edge Function every minute

Store `project_url` and `anon_key` in Supabase Vault:

```sql
select vault.create_secret('https://project-ref.supabase.co', 'project_url');
select vault.create_secret('YOUR_SUPABASE_PUBLISHABLE_KEY', 'publishable_key');
```

Make a POST request to a Supabase Edge Function every minute:

```sql
select
  cron.schedule(
    'invoke-function-every-minute',
    '* * * * *', -- every minute
    $$
    select
      net.http_post(
          url:= (select decrypted_secret from vault.decrypted_secrets where name = 'project_url') || '/functions/v1/function-name',
          headers:=jsonb_build_object(
            'Content-type', 'application/json',
            'Authorization', 'Bearer ' || (select decrypted_secret from vault.decrypted_secrets where name = 'anon_key')
          ),
          body:=concat('{"time": "', now(), '"}')::jsonb
      ) as request_id;
    $$
  );
```



## Resources

*   [`pg_net` extension](/docs/guides/database/extensions/pgnet)
*   [`pg_cron` extension](/docs/guides/database/extensions/pgcron)



# Environment Variables

Manage sensitive data securely across environments.


## Default secrets

Edge Functions have access to these secrets by default:

*   `SUPABASE_URL`: The API gateway for your Supabase project
*   `SUPABASE_ANON_KEY`: The `anon` key for your Supabase API. This is safe to use in a browser when you have Row Level Security enabled
*   `SUPABASE_SERVICE_ROLE_KEY`: The `service_role` key for your Supabase API. This is safe to use in Edge Functions, but it should NEVER be used in a browser. This key will bypass Row Level Security
*   `SUPABASE_DB_URL`: The URL for your Postgres database. You can use this to connect directly to your database

In a hosted environment, functions have access to the following environment variables:

*   `SB_REGION`: The region function was invoked
*   `SB_EXECUTION_ID`: A UUID of function instance ([isolate](/docs/guides/functions/architecture#4-execution-mechanics-fast-and-isolated))
*   `DENO_DEPLOYMENT_ID`: Version of the function code (`{project_ref}_{function_id}_{version}`)

***



## Accessing environment variables

You can access environment variables using Deno's built-in handler, and passing it the name of the environment variable you’d like to access.

```js
Deno.env.get('NAME_OF_SECRET')
```

For example, in a function:

```js
import { createClient } from 'npm:@supabase/supabase-js@2'

// For user-facing operations (respects RLS)
const supabase = createClient(
  Deno.env.get('SUPABASE_URL')!,
  Deno.env.get('SUPABASE_ANON_KEY')!
)

// For admin operations (bypasses RLS)
const supabaseAdmin = createClient(
  Deno.env.get('SUPABASE_URL')!,
  Deno.env.get('SUPABASE_SERVICE_ROLE_KEY')!
)
```

***


### Local secrets

In development, you can load environment variables in two ways:

1.  Through an `.env` file placed at `supabase/functions/.env`, which is automatically loaded on `supabase start`
2.  Through the `--env-file` option for `supabase functions serve`. This allows you to use custom file names like `.env.local` to distinguish between different environments.

```bash
supabase functions serve --env-file .env.local
```

<Admonition type="caution">
  Never check your `.env` files into Git! Instead, add the path to this file to your `.gitignore`.
</Admonition>

We can automatically access the secrets in our Edge Functions through Deno’s handler

```tsx
const secretKey = Deno.env.get('STRIPE_SECRET_KEY')
```

Now we can invoke our function locally. If you're using the default `.env` file at `supabase/functions/.env`, it's automatically loaded:

```bash
supabase functions serve hello-world
```

Or you can specify a custom `.env` file with the `--env-file` flag:

```bash
supabase functions serve hello-world --env-file .env.local
```

This is useful for managing different environments (development, staging, etc.).

***


### Production secrets

You will also need to set secrets for your production Edge Functions. You can do this via the Dashboard or using the CLI.

**Using the Dashboard**:

1.  Visit [Edge Function Secrets Management](/dashboard/project/_/settings/functions) page in your Dashboard.
2.  Add the Key and Value for your secret and press Save

<Image
  alt="Edge Functions Secrets Management"
  src={{
    light: '/docs/img/edge-functions-secrets--light.jpg',
    dark: '/docs/img/edge-functions-secrets.jpg',
  }}
/>

Note that you can paste multiple secrets at a time.

**Using the CLI**

You can create a `.env` file to help deploy your secrets to production

```bash

# .env
STRIPE_SECRET_KEY=sk_live_...
```

<Admonition type="caution">
  Never check your `.env` files into Git! Instead, add the path to this file to your `.gitignore`.
</Admonition>

You can push all the secrets from the `.env` file to your remote project using `supabase secrets set`. This makes the environment visible in the dashboard as well.

```bash
supabase secrets set --env-file .env
```

Alternatively, this command also allows you to set production secrets individually rather than storing them in a `.env` file.

```bash
supabase secrets set STRIPE_SECRET_KEY=sk_live_...
```

To see all the secrets which you have set remotely, you can use `supabase secrets list`

```bash
supabase secrets list
```

<Admonition type="note">
  You don't need to re-deploy after setting your secrets. They're available immediately in your
  functions.
</Admonition>



# Status codes

Understand HTTP status codes returned by Edge Functions to properly debug issues and handle responses.

{/* supa-mdx-lint-disable Rule001HeadingCase */}



## Success Responses


### 2XX Success

Your Edge Function executed successfully and returned a valid response. This includes any status code in the 200-299 range that your function explicitly returns.


### 3XX Redirect

Your Edge Function used the `Response.redirect()` API to redirect the client to a different URL. This is a normal response when implementing authentication flows or URL forwarding.

***



## Client Errors

These errors indicate issues with the request itself, which typically require changing how the function is called.


### 401 Unauthorized

**Cause:** The Edge Function has JWT verification enabled, but the request was made with an invalid or missing JWT token.

**Solution:**

*   Ensure you're passing a valid JWT token in the `Authorization` header
*   Check that your token hasn't expired
*   For webhooks or public endpoints, consider disabling JWT verification


### 404 Not Found

**Cause:** The requested Edge Function doesn't exist or the URL path is incorrect.

**Solution:**

*   Verify the function name and project reference in your request URL
*   Check that the function has been deployed successfully


### 405 Method Not Allowed

**Cause:** You're using an unsupported HTTP method. Edge Functions only support: `GET`, `POST`, `PUT`, `PATCH`, `DELETE`, and `OPTIONS`.

**Solution:** Update your request to use a supported HTTP method.

***



## Server Errors

These errors indicate issues with the function execution or underlying platform.


### 500 Internal Server Error

**Cause:** Your Edge Function threw an uncaught exception (`WORKER_ERROR`).

**Common causes:**

*   Unhandled JavaScript errors in your function code
*   Missing error handling for async operations
*   Invalid JSON parsing

**Solution:** Check your Edge Function logs to identify the specific error and add proper error handling to your code.

```tsx
// ✅ Good error handling
try {
  const result = await someAsyncOperation()
  return new Response(JSON.stringify(result))
} catch (error) {
  console.error('Function error:', error)
  return new Response('Internal error', { status: 500 })
}
```

You can see the output in the [Edge Function Logs](/docs/guides/functions/logging).


### 503 Service Unavailable

**Cause:** Your Edge Function failed to start (`BOOT_ERROR`).

**Common causes:**

*   Syntax errors preventing the function from loading
*   Import errors or missing dependencies
*   Invalid function configuration

**Solution:** Check your Edge Function logs and verify your function code can be executed locally with `supabase functions serve`.


### 504 Gateway Timeout

**Cause:** Your Edge Function didn't respond within the [request timeout limit](/docs/guides/functions/limits).

**Common causes:**

*   Long-running database queries
*   Slow external API calls
*   Infinite loops or blocking operations

**Solution:**

*   Optimize slow operations
*   Add timeout handling to external requests
*   Consider breaking large operations into smaller chunks


### 546 Resource Limit (Custom Error Code)

**Cause:** Your Edge Function execution was stopped due to exceeding resource limits (`WORKER_LIMIT`). Edge Function logs should provide which [resource limit](/docs/guides/functions/limits) was exceeded.

**Common causes:**

*   Memory usage exceeded available limits
*   CPU time exceeded execution quotas
*   Too many concurrent operations

**Solution:** Check your Edge Function logs to see which resource limit was exceeded, then optimize your function accordingly.



# Integrating with Supabase Storage



Edge Functions work seamlessly with [Supabase Storage](/docs/guides/storage). This allows you to:

*   Upload generated content directly from your functions
*   Implement cache-first patterns for better performance
*   Serve files with built-in CDN capabilities

***



## Basic file operations

Use the Supabase client to upload files directly from your Edge Functions. You'll need the service role key for server-side storage operations:

```typescript
import { createClient } from 'npm:@supabase/supabase-js@2'

Deno.serve(async (req) => {
  const supabaseAdmin = createClient(
    Deno.env.get('SUPABASE_URL') ?? '',
    Deno.env.get('SUPABASE_SERVICE_ROLE_KEY') ?? ''
  )

  // Generate your content
  const fileContent = await generateImage()

  // Upload to storage
  const { data, error } = await supabaseAdmin.storage
    .from('images')
    .upload(`generated/${filename}.png`, fileContent.body!, {
      contentType: 'image/png',
      cacheControl: '3600',
      upsert: false,
    })

  if (error) {
    throw error
  }

  return new Response(JSON.stringify({ path: data.path }))
})
```

<Admonition type="caution">
  Always use the `SUPABASE_SERVICE_ROLE_KEY` for server-side operations. Never expose this key in client-side code!
</Admonition>

***



## Cache-first pattern

Check storage before generating new content to improve performance:

```typescript
const STORAGE_URL = 'https://your-project.supabase.co/storage/v1/object/public/images'

Deno.serve(async (req) => {
  const url = new URL(req.url)
  const username = url.searchParams.get('username')

  try {
    // Try to get existing file from storage first
    const storageResponse = await fetch(`${STORAGE_URL}/avatars/${username}.png`)

    if (storageResponse.ok) {
      // File exists in storage, return it directly
      return storageResponse
    }

    // File doesn't exist, generate it
    const generatedImage = await generateAvatar(username)

    // Upload to storage for future requests
    const { error } = await supabaseAdmin.storage
      .from('images')
      .upload(`avatars/${username}.png`, generatedImage.body!, {
        contentType: 'image/png',
        cacheControl: '86400', // Cache for 24 hours
      })

    if (error) {
      console.error('Upload failed:', error)
    }

    return generatedImage
  } catch (error) {
    return new Response('Error processing request', { status: 500 })
  }
})
```



# Troubleshooting Common Issues

How to solve common problems and issues related to Edge Functions.

{/* supa-mdx-lint-disable Rule001HeadingCase */}

When developing Edge Functions, you can run into various issues during development, deployment, and at runtime. Most problems fall under these categories:

*   [Deployment issues](/docs/guides/functions/troubleshooting#deployment-issues)
*   [Runtime issues](/docs/guides/functions/troubleshooting#runtime-issues)
*   [Performance issues](/docs/guides/functions/troubleshooting#performance-optimization)
*   [Local development problems](/docs/guides/functions/troubleshooting#local-development-issues)

This guide will cover most of the common issues.

<Admonition type="note">
  Before troubleshooting, make sure you're using the latest version of the Supabase CLI:

  ```bash
  supabase --version
  supabase update
  ```
</Admonition>

***



## Deployment issues


### Unable to deploy Edge Function

1.  **Check function syntax:** Run `deno check` on your function files locally
2.  **Review dependencies:** Verify all imports are accessible and compatible with Deno
3.  **Examine bundle size:** Large functions may fail to deploy

```bash

# Check for syntax errors
deno check ./supabase/functions/your-function/index.ts


# Deploy with verbose output
supabase functions deploy your-function --debug
```

<Admonition type="note">
  If these steps don't resolve the issue, open a support ticket via the Supabase Dashboard and
  include all output from the diagnostic commands.
</Admonition>


### Bundle size issues

Functions have a 10MB source code limit. Check your bundle size:

```bash
deno info /path/to/function/index.ts
```

Look for the "size" field in the output. If your bundle is too large:

*   Remove unused dependencies
*   Use selective imports: `import { specific } from 'npm:package/specific'`
*   Consider splitting large functions into smaller ones

***



## Runtime issues


### Edge Function takes too long to respond

Functions have a 60-second execution limit.

1.  **Check function logs:** Navigate to Functions > \[Your Function] > Logs in the dashboard
2.  **Examine boot times:** Look for `booted` events and check for consistent boot times
3.  **Identify bottlenecks:** Review your code for slow operations
    *   If the boot times are similar, it’s likely an issue with your function’s code, such as a large dependency, a slow API call, or a complex computation. You can try to optimize your code, reduce the size of your dependencies, or use caching techniques to improve the performance of your function.
    *   If only some of the `booted` events are slow, find the affected `region` in the metadata and submit a support request via the "Help" button at the top.

```tsx
// ✅ Optimize database queries
const { data } = await supabase
  .from('users')
  .select('id, name') // Only select needed columns
  .limit(10)

// ❌ Avoid fetching large datasets
const { data } = await supabase.from('users').select('*') // Fetches all columns
```


### 546 Error Response

The 546 error typically indicates resource exhaustion or code issues:

*   **Memory or CPU Limits:** Your function may have exceeded available resources. Check the resource usage metrics in your dashboard.
*   **Event Loop Completion:** If logs show "Event loop completed," your function has implementation issues. You should check your function code for any syntax errors, infinite loops, or unresolved promises that might cause this error.

    You can also try running the function locally (using Supabase CLI **`functions serve`**) to see if you can debug the error. The local console should give a full stack trace on the error with line numbers of the source code. You can also refer to [Edge Functions examples](https://github.com/supabase/supabase/tree/master/examples/edge-functions) for guidance.

Run the function locally with `supabase functions serve` to get detailed stack traces.


### Unable to call Edge Function

For invocation or CORS issues:

1.  **Review CORS configuration:** Check out the [CORS guide](/docs/guides/functions/cors), and ensure you've properly configured CORS headers
2.  **Check function logs:** Look for errors in the Functions > Logs section
3.  **Verify authentication:** Confirm JWT tokens and permissions are correct

```tsx
// ✅ Proper CORS handling
Deno.serve(async (req) => {
  if (req.method === 'OPTIONS') {
    return new Response(null, {
      status: 200,
      headers: {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'POST, GET, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type, Authorization',
      },
    })
  }

  // Your function logic here
  return new Response('Success', {
    headers: { 'Access-Control-Allow-Origin': '*' },
  })
})
```

There are two debugging tools available: Invocations and Logs. Invocations shows the Request and Response for each execution, while Logs shows any platform events, including deployments and errors.

***



## Local development issues


### Issues serving functions locally

When `supabase functions serve` fails:

1.  **Use debug mode:** Run with the `--debug` flag for detailed output
2.  **Check port availability:** Ensure ports `54321` and `8081` are available

```bash

# Serve with debug output
supabase functions serve your-function --debug


# Check specific port usage
lsof -i :54321
```

If the problem persists, search the [Edge Runtime](https://github.com/supabase/edge-runtime) and [CLI](https://github.com/supabase/cli) repositories for similar error messages.

<Admonition type="note">
  If the output from the commands above does not help you to resolve the issue, open a support
  ticket via the Supabase Dashboard (by clicking the "Help" button at the top right) and include all
  output and details about your commands.
</Admonition>



## Performance optimization


### Monitoring resource usage

Track your function's performance through the dashboard:

1.  Navigate to Edge Functions > \[Your Function] > Metrics
2.  Review CPU, memory, and execution time charts
3.  Identify potential problems in resource consumption

<Admonition type="note">
  Edge Functions have limited resources compared to traditional servers. Optimize for:

  *   **Memory efficiency:** Avoid loading large datasets into memory
  *   **CPU optimization:** Minimize complex computations
  *   **Execution time:** Keep functions under 60 seconds
</Admonition>


### Understanding CPU limits

An isolate is like a worker that can handle multiple requests for a function. It works until a time limit of 400 seconds is reached. Edge Functions use isolates with soft and hard CPU limits:

1.  **Soft Limit**: When the isolate hits the soft limit, it retires. This means it won't take on any new requests, but it will finish processing the ones it's already working on. It keeps going until it either hits the hard limit for CPU time or reaches the 400-second time limit, whichever comes first.
2.  **Hard Limit**: If there are new requests after the soft limit is reached, a new isolate is created to handle them. The original isolate continues until it hits the hard limit or the time limit. This ensures that existing requests are completed, and new ones will be managed by a newly created isolate.


### Dependency Analysis

It’s important to optimize your dependencies for better performance. Large or unnecessary dependencies can significantly impact bundle size, boot time, and memory usage.

**Deno Dependencies**

Start by analyzing your dependency tree to understand what's being imported:

```bash

# Basic dependency analysis
deno info /path/to/function/index.ts


# With import map (if using one)
deno info --import-map=/path/to/import_map.json /path/to/function/index.ts
```

Review the output for:

*   **Large dependencies:** Look for packages that contribute significantly to bundle size
*   **Redundant imports:** Multiple packages providing similar functionality
*   **Outdated versions:** Dependencies that can be updated to more efficient versions
*   **Unused imports:** Dependencies imported but not actually used in your code

**NPM Dependencies**

When using NPM modules, keep their impact on bundle size in mind. Many NPM packages are designed for Node.js and may include unnecessary polyfills or large dependency trees.

Use selective imports to minimize overhead:

```tsx
// ✅ Import specific submodules
import { Sheets } from 'npm:@googleapis/sheets'
import { JWT } from 'npm:google-auth-library/build/src/auth/jwtclient'

// ❌ Import entire package
import * as googleapis from 'npm:googleapis'
import * as googleAuth from 'npm:google-auth-library'
```

*   **Tree-shake aggressively:** Only import what you actually use
*   **Choose lightweight alternatives:** Research smaller packages that provide the same functionality
*   **Bundle analysis:** Use `deno info` before and after changes to measure impact
*   **Version pinning:** Lock dependency versions to avoid unexpected size increases



# Testing your Edge Functions

Writing Unit Tests for Edge Functions using Deno Test

Testing is an essential step in the development process to ensure the correctness and performance of your Edge Functions.

***



## Testing in Deno

Deno has a built-in test runner that you can use for testing JavaScript or TypeScript code. You can read the [official documentation](https://docs.deno.com/runtime/manual/basics/testing/) for more information and details about the available testing functions.

***



## Folder structure

We recommend creating your testing in a `supabase/functions/tests` directory, using the same name as the Function followed by `-test.ts`:

```bash
└── supabase
    ├── functions
    │   ├── function-one
    │   │   └── index.ts
    │   └── function-two
    │   │   └── index.ts
    │   └── tests
    │       └── function-one-test.ts  # Tests for function-one
    │       └── function-two-test.ts  # Tests for function-two
    └── config.toml
```

***



## Example

The following script is a good example to get started with testing your Edge Functions:

```typescript function-one-test.ts
// Import required libraries and modules
import { assert, assertEquals } from 'jsr:@std/assert@1'
import { createClient, SupabaseClient } from 'npm:@supabase/supabase-js@2'

// Will load the .env file to Deno.env
import 'jsr:@std/dotenv/load'

// Set up the configuration for the Supabase client
const supabaseUrl = Deno.env.get('SUPABASE_URL') ?? ''
const supabaseKey = Deno.env.get('SUPABASE_PUBLISHABLE_KEY') ?? ''
const options = {
  auth: {
    autoRefreshToken: false,
    persistSession: false,
    detectSessionInUrl: false,
  },
}

// Test the creation and functionality of the Supabase client
const testClientCreation = async () => {
  var client: SupabaseClient = createClient(supabaseUrl, supabaseKey, options)

  // Verify if the Supabase URL and key are provided
  if (!supabaseUrl) throw new Error('supabaseUrl is required.')
  if (!supabaseKey) throw new Error('supabaseKey is required.')

  // Test a simple query to the database
  const { data: table_data, error: table_error } = await client
    .from('my_table')
    .select('*')
    .limit(1)
  if (table_error) {
    throw new Error('Invalid Supabase client: ' + table_error.message)
  }
  assert(table_data, 'Data should be returned from the query.')
}

// Test the 'hello-world' function
const testHelloWorld = async () => {
  var client: SupabaseClient = createClient(supabaseUrl, supabaseKey, options)

  // Invoke the 'hello-world' function with a parameter
  const { data: func_data, error: func_error } = await client.functions.invoke('hello-world', {
    body: { name: 'bar' },
  })

  // Check for errors from the function invocation
  if (func_error) {
    throw new Error('Invalid response: ' + func_error.message)
  }

  // Log the response from the function
  console.log(JSON.stringify(func_data, null, 2))

  // Assert that the function returned the expected result
  assertEquals(func_data.message, 'Hello bar!')
}

// Register and run the tests
Deno.test('Client Creation Test', testClientCreation)
Deno.test('Hello-world Function Test', testHelloWorld)
```

This test case consists of two parts.

1.  The first part tests the client library and verifies that the database can be connected to and returns values from a table (`my_table`).
2.  The second part tests the edge function and checks if the received value matches the expected value. Here's a brief overview of the code:
    *   We import various testing functions from the Deno standard library, including `assert`, `assertExists`, and `assertEquals`.
    *   We import the `createClient` and `SupabaseClient` classes from the `@supabase/supabase-js` library to interact with the Supabase client.
    *   We define the necessary configuration for the Supabase client, including the Supabase URL, API key, and authentication options.
    *   The `testClientCreation` function tests the creation of a Supabase client instance and queries the database for data from a table. It verifies that data is returned from the query.
    *   The `testHelloWorld` function tests the "Hello-world" Edge Function by invoking it using the Supabase client's `functions.invoke` method. It checks if the response message matches the expected greeting.
    *   We run the tests using the `Deno.test` function, providing a descriptive name for each test case and the corresponding test function.

<Admonition type="note">
  Make sure to replace the placeholders (`supabaseUrl`, `supabaseKey`, `my_table`) with the actual values relevant to your Supabase setup.
</Admonition>

***



## Running Edge Functions locally

To locally test and debug Edge Functions, you can utilize the Supabase CLI. Let's explore how to run Edge Functions locally using the Supabase CLI:

1.  Ensure that the Supabase server is running by executing the following command:

    ```bash
    supabase start
    ```

2.  In your terminal, use the following command to serve the Edge Functions locally:

    ```bash
    supabase functions serve
    ```

    This command starts a local server that runs your Edge Functions, enabling you to test and debug them in a development environment.

3.  Create the environment variables file:

    ```bash
    # creates the file
    touch .env
    # adds the SUPABASE_URL secret
    echo "SUPABASE_URL=http://localhost:54321" >> .env
    # adds the SUPABASE_PUBLISHABLE_KEY secret
    echo "SUPABASE_PUBLISHABLE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZS1kZW1vIiwicm9sZSI6ImFub24iLCJleHAiOjE5ODM4MTI5OTZ9.CRXP1A7WOeoJeXxjNni43kdQwgnWNReilDMblYTn_I0" >> .env
    # Alternatively, you can open it in your editor:
    open .env
    ```

4.  To run the tests, use the following command in your terminal:

    ```bash
    deno test --allow-all supabase/functions/tests/function-one-test.ts
    ```

***



## Resources

*   Full guide on Testing Supabase Edge Functions on [Mansueli's tips](https://blog.mansueli.com/testing-supabase-edge-functions-with-deno-test)



# Using Wasm modules

Use WebAssembly in Edge Functions.

Edge Functions supports running [WebAssembly (Wasm)](https://developer.mozilla.org/en-US/docs/WebAssembly) modules. WebAssembly is useful if you want to optimize code that's slower to run in JavaScript or require low-level manipulation.

This allows you to:

*   Optimize performance-critical code beyond JavaScript capabilities
*   Port existing libraries from other languages (C, C++, Rust) to JavaScript
*   Access low-level system operations not available in JavaScript

For example, libraries like [magick-wasm](/docs/guides/functions/examples/image-manipulation) port existing C libraries to WebAssembly for complex image processing.

***


### Writing a Wasm module

You can use different languages and SDKs to write Wasm modules. For this tutorial, we will write a simple Wasm module in Rust that adds two numbers.

<Admonition type="note">
  Follow this [guide on writing Wasm modules in Rust](https://developer.mozilla.org/en-US/docs/WebAssembly/Rust_to_Wasm) to setup your dev environment.
</Admonition>

<StepHikeCompact>
  <StepHikeCompact.Step step={1} fullWidth>
    <StepHikeCompact.Details title="Create a new Edge Function" fullWidth>
      Create a new Edge Function called `wasm-add`

      ```bash
      supabase functions new wasm-add
      ```
    </StepHikeCompact.Details>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={2} fullWidth>
    <StepHikeCompact.Details title="Create a new Cargo project" fullWidth>
      Create a new Cargo project for the Wasm module inside the function's directory:

      ```bash
      cd supabase/functions/wasm-add
      cargo new --lib add-wasm
      ```
    </StepHikeCompact.Details>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={3} fullWidth>
    <StepHikeCompact.Details title="Add the Wasm module code" fullWidth>
      Add the following code to `add-wasm/src/lib.rs`.

      <CodeSampleWrapper source="https://github.com/supabase/supabase/blob/2415776436927dedb360dae082d03caee607891a/examples/edge-functions/supabase/functions/wasm-modules/add-wasm/src/lib.rs">
        ```
        use wasm_bindgen::prelude::*;

        #[wasm_bindgen]
        pub fn add(a: u32, b: u32) -> u32 {
            a + b
        }
        ```
      </CodeSampleWrapper>
    </StepHikeCompact.Details>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={4} fullWidth>
    <StepHikeCompact.Details title="Update the Cargo.toml file" fullWidth>
      Update the `add-wasm/Cargo.toml` to include the `wasm-bindgen` dependency.

      <CodeSampleWrapper source="https://github.com/supabase/supabase/blob/2415776436927dedb360dae082d03caee607891a/examples/edge-functions/supabase/functions/wasm-modules/add-wasm/Cargo.toml">
        ```
        [package]
        name = "add-wasm"
        version = "0.1.0"
        description = "A simple wasm module that adds two numbers"
        license = "MIT/Apache-2.0"
        edition = "2021"

        [lib]
        crate-type = ["cdylib"]

        [dependencies]
        wasm-bindgen = "0.2"
        ```
      </CodeSampleWrapper>
    </StepHikeCompact.Details>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={5} fullWidth>
    <StepHikeCompact.Details title="Build the Wasm module" fullWidth>
      Build the package by running:

      ```bash
      wasm-pack build --target deno
      ```

      This will produce a Wasm binary file inside `add-wasm/pkg` directory.
    </StepHikeCompact.Details>
  </StepHikeCompact.Step>
</StepHikeCompact>

***



## Calling the Wasm module from the Edge Function

Update your Edge Function to call the add function from the Wasm module:

<CodeSampleWrapper source="https://github.com/supabase/supabase/blob/2415776436927dedb360dae082d03caee607891a/examples/edge-functions/supabase/functions/wasm-modules/index.ts">
  ```typescript index.ts
  import { add } from "./add-wasm/pkg/add_wasm.js";

  Deno.serve(async (req) => {
    const { a, b } = await req.json();
    return new Response(
      JSON.stringify({ result: add(a, b) }),
      { headers: { "Content-Type": "application/json" } },
    );
  });
  ```
</CodeSampleWrapper>

<Admonition type="note">
  Supabase Edge Functions currently use Deno 1.46. From [Deno 2.1, importing Wasm modules](https://deno.com/blog/v2.1) will require even less boilerplate code.
</Admonition>

***



## Bundle and deploy

Before deploying, ensure the Wasm module is bundled with your function by defining it in `supabase/config.toml`:

<Admonition type="note">
  *   You will need update Supabase CLI to 2.7.0 or higher for the `static_files` support.
  *   Static files cannot be deployed using the `--use-api` API flag. You need to build them with [Docker on the CLI](/docs/guides/functions/quickstart#step-6-deploy-to-production).
</Admonition>

```toml
[functions.wasm-add]
static_files = [ "./functions/wasm-add/add-wasm/pkg/*"]
```

Deploy the function by running:

```bash
supabase functions deploy wasm-add
```



# Handling WebSockets

Handle WebSocket connections in Edge Functions.

Edge Functions supports hosting WebSocket servers that can facilitate bi-directional communications with browser clients.

This allows you to:

*   Build real-time applications like chat or live updates
*   Create WebSocket relay servers for external APIs
*   Establish both incoming and outgoing WebSocket connections

***



## Creating WebSocket servers

Here are some basic examples of setting up WebSocket servers using Deno and Node.js APIs.

<Tabs scrollable size="small" type="underlined" defaultActiveId="deno" queryGroup="runtime">
  <TabPanel id="deno" label="Deno">
    ```ts
    Deno.serve((req) => {
      const upgrade = req.headers.get('upgrade') || ''

      if (upgrade.toLowerCase() != 'websocket') {
        return new Response("request isn't trying to upgrade to WebSocket.", { status: 400 })
      }

      const { socket, response } = Deno.upgradeWebSocket(req)

      socket.onopen = () => console.log('socket opened')
      socket.onmessage = (e) => {
        console.log('socket message:', e.data)
        socket.send(new Date().toString())
      }

      socket.onerror = (e) => console.log('socket errored:', e.message)
      socket.onclose = () => console.log('socket closed')

      return response
    })
    ```
  </TabPanel>

  <TabPanel id="node" label="Node.js">
    ```ts
    import { createServer } from 'node:http'
    import { WebSocketServer } from 'npm:ws'

    const server = createServer()
    // Since we manually created the HTTP server,
    // turn on the noServer mode.
    const wss = new WebSocketServer({ noServer: true })

    wss.on('connection', (ws) => {
      console.log('socket opened')
      ws.on('message', (data /** Buffer \*/, isBinary /** bool \*/) => {
        if (isBinary) {
          console.log('socket message:', data)
        } else {
          console.log('socket message:', data.toString())
        }

        ws.send(new Date().toString())
      })

      ws.on('error', (err) => {
        console.log('socket errored:', err.message)
      })

      ws.on('close', () => console.log('socket closed'))
    })

    server.on('upgrade', (req, socket, head) => {
      wss.handleUpgrade(req, socket, head, (ws) => {
        wss.emit('connection', ws, req)
      })
    })

    server.listen(8080)
    ```
  </TabPanel>
</Tabs>

***


### Outbound WebSockets

You can also establish an outbound WebSocket connection to another server from an Edge Function.

Combining it with incoming WebSocket servers, it's possible to use Edge Functions as a WebSocket proxy, for example as a [relay server](https://github.com/supabase-community/openai-realtime-console?tab=readme-ov-file#using-supabase-edge-functions-as-a-relay-server) for the [OpenAI Realtime API](https://platform.openai.com/docs/guides/realtime/overview).

<CodeSampleWrapper source="https://github.com/supabase-community/openai-realtime-console/blob/0f93657a71670704fbf77c48cf54d6c9eb956698/supabase/functions/relay/index.ts">
  ```typescript supabase/functions/relay/index.ts
  import { createServer } from "node:http";
  import { WebSocketServer } from "npm:ws";
  import { RealtimeClient } from "https://raw.githubusercontent.com/openai/openai-realtime-api-beta/refs/heads/main/lib/client.js";

  // ...

  const OPENAI_API_KEY = Deno.env.get("OPENAI_API_KEY");

  const server = createServer();
  // Since we manually created the HTTP server,
  // turn on the noServer mode.
  const wss = new WebSocketServer({ noServer: true });

  wss.on("connection", async (ws) => {
    console.log("socket opened");
    if (!OPENAI_API_KEY) {
      throw new Error("OPENAI_API_KEY is not set");
    }
    // Instantiate new client
    console.log(`Connecting with key "${OPENAI_API_KEY.slice(0, 3)}..."`);
    const client = new RealtimeClient({ apiKey: OPENAI_API_KEY });

    // Relay: OpenAI Realtime API Event -> Browser Event
    client.realtime.on("server.*", (event) => {
      console.log(`Relaying "${event.type}" to Client`);
      ws.send(JSON.stringify(event));
    });
    client.realtime.on("close", () => ws.close());

    // Relay: Browser Event -> OpenAI Realtime API Event
    // We need to queue data waiting for the OpenAI connection
    const messageQueue = [];
    const messageHandler = (data) => {
      try {
        const event = JSON.parse(data);
        console.log(`Relaying "${event.type}" to OpenAI`);
        client.realtime.send(event.type, event);
      } catch (e) {
        console.error(e.message);
        console.log(`Error parsing event from client: ${data}`);
      }
    };

    ws.on("message", (data) => {
      if (!client.isConnected()) {
        messageQueue.push(data);
      } else {
        messageHandler(data);
      }
    });
    ws.on("close", () => client.disconnect());

    // Connect to OpenAI Realtime API
    try {
      console.log(`Connecting to OpenAI...`);
      await client.connect();
    } catch (e) {
      console.log(`Error connecting to OpenAI: ${e.message}`);
      ws.close();
      return;
    }
    console.log(`Connected to OpenAI successfully!`);
    while (messageQueue.length) {
      messageHandler(messageQueue.shift());
    }
  });

  server.on("upgrade", (req, socket, head) => {
    wss.handleUpgrade(req, socket, head, (ws) => {
      wss.emit("connection", ws, req);
    });
  });

  server.listen(8080);
  ```
</CodeSampleWrapper>

***



## Authentication

WebSocket browser clients don't have the option to send custom headers. Because of this, Edge Functions won't be able to perform the usual authorization header check to verify the JWT.

You can skip the default authorization header checks by explicitly providing `--no-verify-jwt` when serving and deploying functions.

To authenticate the user making WebSocket requests, you can pass the JWT in URL query params or via a custom protocol.

<Tabs scrollable size="small" type="underlined" defaultActiveId="query" queryGroup="auth">
  <TabPanel id="query" label="Using query params">
    ```ts
    import { createClient } from 'npm:@supabase/supabase-js@2'

    const supabase = createClient(
      Deno.env.get('SUPABASE_URL'),
      Deno.env.get('SUPABASE_SERVICE_ROLE_KEY')
    )

    Deno.serve((req) => {
      const upgrade = req.headers.get('upgrade') || ''
      if (upgrade.toLowerCase() != 'WebSocket') {
        return new Response("request isn't trying to upgrade to WebSocket.", { status: 400 })
      }

      // Please be aware query params may be logged in some logging systems.
      const url = new URL(req.url)
      const jwt = url.searchParams.get('jwt')

      if (!jwt) {
        console.error('Auth token not provided')
        return new Response('Auth token not provided', { status: 403 })
      }

      const { error, data } = await supabase.auth.getClaims()

      if (error) {
        console.error(error)
        return new Response('Invalid token provided', { status: 403 })
      }

      if (!data.user) {
        console.error('user is not authenticated')
        return new Response('User is not authenticated', { status: 403 })
      }

      const { socket, response } = Deno.upgradeWebSocket(req)

      socket.onopen = () => console.log('socket opened')
      socket.onmessage = (e) => {
        console.log('socket message:', e.data)
        socket.send(new Date().toString())
      }

      socket.onerror = (e) => console.log('socket errored:', e.message)
      socket.onclose = () => console.log('socket closed')

      return response
    })
    ```
  </TabPanel>

  <TabPanel id="protocol" label="Using custom protocol">
    ```ts
    import { createClient } from 'npm:@supabase/supabase-js@2'

    const supabase = createClient(
      Deno.env.get('SUPABASE_URL'),
      Deno.env.get('SUPABASE_SERVICE_ROLE_KEY')
    )

    Deno.serve((req) => {
      const upgrade = req.headers.get('upgrade') || ''
      if (upgrade.toLowerCase() != 'WebSocket') {
        return new Response("request isn't trying to upgrade to WebSocket.", { status: 400 })
      }

      // Sec-WebScoket-Protocol may return multiple protocol values `jwt-TOKEN, value1, value 2`
      const customProtocols = (req.headers.get('Sec-WebSocket-Protocol') ?? '')
        .split(',')
        .map((p) => p.trim())
      const jwt = customProtocols.find((p) => p.startsWith('jwt')).replace('jwt-', '')

      if (!jwt) {
        console.error('Auth token not provided')
        return new Response('Auth token not provided', { status: 403 })
      }

      const { error, data } = await supabase.auth.getClaims()
      if (error) {
        console.error(error)
        return new Response('Invalid token provided', { status: 403 })
      }

      if (!data.user) {
        console.error('user is not authenticated')
        return new Response('User is not authenticated', { status: 403 })
      }

      const { socket, response } = Deno.upgradeWebSocket(req)

      socket.onopen = () => console.log('socket opened')
      socket.onmessage = (e) => {
        console.log('socket message:', e.data)
        socket.send(new Date().toString())
      }

      socket.onerror = (e) => console.log('socket errored:', e.message)
      socket.onclose = () => console.log('socket closed')

      return response
    })
    ```
  </TabPanel>
</Tabs>

<Admonition type="caution">
  The maximum duration is capped based on the wall-clock, CPU, and memory limits. The Function will shutdown when it reaches one of these [limits](/docs/guides/functions/limits).
</Admonition>

***



## Testing WebSockets locally

When testing Edge Functions locally with Supabase CLI, the instances are terminated automatically after a request is completed. This will prevent keeping WebSocket connections open.

To prevent that, you can update the `supabase/config.toml` with the following settings:

```toml
[edge_runtime]
policy = "per_worker"
```

<Admonition type="caution">
  When running with `per_worker` policy, Function won't auto-reload on edits. You will need to manually restart it by running `supabase functions serve`.
</Admonition>



# Generate Images with Amazon Bedrock



[Amazon Bedrock](https://aws.amazon.com/bedrock) is a fully managed service that offers a choice of high-performing foundation models (FMs) from leading AI companies like AI21 Labs, Anthropic, Cohere, Meta, Mistral AI, Stability AI, and Amazon. Each model is accessible through a common API which implements a broad set of features to help build generative AI applications with security, privacy, and responsible AI in mind.

This guide will walk you through an example using the Amazon Bedrock JavaScript SDK in Supabase Edge Functions to generate images using the [Amazon Titan Image Generator G1](https://aws.amazon.com/blogs/machine-learning/use-amazon-titan-models-for-image-generation-editing-and-searching/) model.



## Setup

*   In your AWS console, navigate to Amazon Bedrock and under "Request model access", select the Amazon Titan Image Generator G1 model.
*   In your Supabase project, create a `.env` file in the `supabase` directory with the following contents:

```txt
AWS_DEFAULT_REGION="<your_region>"
AWS_ACCESS_KEY_ID="<replace_your_own_credentials>"
AWS_SECRET_ACCESS_KEY="<replace_your_own_credentials>"
AWS_SESSION_TOKEN="<replace_your_own_credentials>"


# Mocked config files
AWS_SHARED_CREDENTIALS_FILE="./aws/credentials"
AWS_CONFIG_FILE="./aws/config"
```


### Configure Storage

*   \[locally] Run `supabase start`
*   Open Studio URL: [locally](http://127.0.0.1:54323/project/default/storage/buckets) | [hosted](https://app.supabase.com/project/_/storage/buckets)
*   Navigate to Storage
*   Click "New bucket"
*   Create a new public bucket called "images"



## Code

Create a new function in your project:

```bash
supabase functions new amazon-bedrock
```

And add the code to the `index.ts` file:

```ts index.ts
// We need to mock the file system for the AWS SDK to work.
import { prepareVirtualFile } from 'https://deno.land/x/mock_file@v1.1.2/mod.ts'

import { BedrockRuntimeClient, InvokeModelCommand } from 'npm:@aws-sdk/client-bedrock-runtime'
import { createClient } from 'npm:@supabase/supabase-js'
import { decode } from 'npm:base64-arraybuffer'

console.log('Hello from Amazon Bedrock!')

Deno.serve(async (req) => {
  prepareVirtualFile('./aws/config')
  prepareVirtualFile('./aws/credentials')

  const client = new BedrockRuntimeClient({
    region: Deno.env.get('AWS_DEFAULT_REGION') ?? 'us-west-2',
    credentials: {
      accessKeyId: Deno.env.get('AWS_ACCESS_KEY_ID') ?? '',
      secretAccessKey: Deno.env.get('AWS_SECRET_ACCESS_KEY') ?? '',
      sessionToken: Deno.env.get('AWS_SESSION_TOKEN') ?? '',
    },
  })

  const { prompt, seed } = await req.json()
  console.log(prompt)
  const input = {
    contentType: 'application/json',
    accept: '*/*',
    modelId: 'amazon.titan-image-generator-v1',
    body: JSON.stringify({
      taskType: 'TEXT_IMAGE',
      textToImageParams: { text: prompt },
      imageGenerationConfig: {
        numberOfImages: 1,
        quality: 'standard',
        cfgScale: 8.0,
        height: 512,
        width: 512,
        seed: seed ?? 0,
      },
    }),
  }

  const command = new InvokeModelCommand(input)
  const response = await client.send(command)
  console.log(response)

  if (response.$metadata.httpStatusCode === 200) {
    const { body, $metadata } = response

    const textDecoder = new TextDecoder('utf-8')
    const jsonString = textDecoder.decode(body.buffer)
    const parsedData = JSON.parse(jsonString)
    console.log(parsedData)
    const image = parsedData.images[0]

    const supabaseClient = createClient(
      // Supabase API URL - env var exported by default.
      Deno.env.get('SUPABASE_URL')!,
      // Supabase API ANON KEY - env var exported by default.
      Deno.env.get('SUPABASE_SERVICE_ROLE_KEY')!
    )

    const { data: upload, error: uploadError } = await supabaseClient.storage
      .from('images')
      .upload(`${$metadata.requestId ?? ''}.png`, decode(image), {
        contentType: 'image/png',
        cacheControl: '3600',
        upsert: false,
      })
    if (!upload) {
      return Response.json(uploadError)
    }
    const { data } = supabaseClient.storage.from('images').getPublicUrl(upload.path!)
    return Response.json(data)
  }

  return Response.json(response)
})
```



## Run the function locally

1.  Run `supabase start` (see: [https://supabase.com/docs/reference/cli/supabase-start](https://supabase.com/docs/reference/cli/supabase-start))
2.  Start with env: `supabase functions serve --env-file supabase/.env`
3.  Make an HTTP request:

```bash
  curl -i --location --request POST 'http://127.0.0.1:54321/functions/v1/amazon-bedrock' \
    --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZS1kZW1vIiwicm9sZSI6ImFub24iLCJleHAiOjE5ODM4MTI5OTZ9.CRXP1A7WOeoJeXxjNni43kdQwgnWNReilDMblYTn_I0' \
    --header 'Content-Type: application/json' \
    --data '{"prompt":"A beautiful picture of a bird"}'
```

4.  Navigate back to your storage bucket. You might have to hit the refresh button to see the uploaded image.



## Deploy to your hosted project

```bash
supabase link
supabase functions deploy amazon-bedrock
supabase secrets set --env-file supabase/.env
```

You've now deployed a serverless function that uses AI to generate and upload images to your Supabase storage bucket.



---
**Navigation:** [← Previous](./18-use-supabase-with-sveltekit.md) | [Index](./index.md) | [Next →](./20-custom-auth-emails-with-react-email-and-resend.md)
