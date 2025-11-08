**Navigation:** [← Previous](./38-supabase-auth-with-the-nextjs-app-router.md) | [Index](./index.md) | [Next →](./40-concepts.md)

# Understanding API keys



Supabase gives you fine-grained control over which application components are allowed to access your project through API keys.

API keys provide the first layer of authentication for data access. Auth then builds upon that. This chart covers the differences:

| Responsibility                     | Question                           | Answer                                             |
| ---------------------------------- | ---------------------------------- | -------------------------------------------------- |
| API keys                           | **What** is accessing the project? | Web page, mobile app, server, Edge Function...     |
| [Supabase Auth](/docs/guides/auth) | **Who** is accessing the project?  | Monica, Jian Yang, Gavin, Dinesh, Laurie, Fiona... |



## Overview

An API key authenticates an application component to give it access to Supabase services. An application component might be a web page, a mobile app, or a server. The API key *does not* distinguish between users, only between applications.

There are 4 types of API keys that can be used with Supabase:

| Type                                                       | Format                                                           | Privileges | Availability                                              | Use                                                                                                                                                                                                                                                                                               |
| ---------------------------------------------------------- | ---------------------------------------------------------------- | ---------- | --------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Publishable key                                            | <span className="!whitespace-nowrap">`sb_publishable_...`</span> | Low        | Platform                                                  | Safe to expose online: web page, mobile or desktop app, GitHub actions, CLIs, source code.                                                                                                                                                                                                        |
| Secret keys                                                | <span className="!whitespace-nowrap">`sb_secret_...`</span>      | Elevated   | Platform                                                  | **Only use in backend components of your app:** servers, already secured APIs (admin panels), [Edge Functions](/docs/guides/functions), microservices, etc. They provide *full access* to your project's data, bypassing [Row Level Security](/docs/guides/database/postgres/row-level-security). |
| <span className="!whitespace-nowrap">`anon`</span>         | JWT (long lived)                                                 | Low        | <span className="!whitespace-nowrap">Platform, CLI</span> | Exactly like the publishable key.                                                                                                                                                                                                                                                                 |
| <span className="!whitespace-nowrap">`service_role`</span> | JWT (long lived)                                                 | Elevated   | <span className="!whitespace-nowrap">Platform, CLI</span> | Exactly like secret keys.                                                                                                                                                                                                                                                                         |

<Admonition type="note">
  `anon` and `service_role` keys are based on the project's JWT secret. They are generated when your project is created and can only be changed when you rotate the JWT secret. This can cause significant issues in production applications. Use the publishable and secret keys instead.
</Admonition>



## `anon` and publishable keys

The `anon` and publishable keys secure the public components of your application. Public components run in environments where it is impossible to secure any secrets. These include:

*   Web pages, where the key is bundled in source code.
*   Mobile or desktop applications, where the key is bundled inside the compiled packages or executables.
*   CLI, scripts, tools, or other pre-built executables.
*   Other publicly available APIs that return the key without prior additional authorization.

These environments are always considered public because anyone can retrieve the key from the source code or build artifacts. Obfuscation can increase the difficulty, but never eliminate the possibility. (In general, obfuscation, Turing test challenges, and specialized knowledge do not count as authorization for the purpose of securing secrets.)


### Interaction with Supabase Auth

Using the `anon` or publishable key does not mean that your user is anonymous. (Thinking of both these keys as publishable rather than `anon` makes the mental model clearer.)

Your application can be authenticated with the publishable key, while your user is authenticated (via Supabase Auth) with their personal JWT:

| Key             | User logged in via Supabase Auth | Postgres role used for RLS, etc. |
| --------------- | -------------------------------- | -------------------------------- |
| Publishable key | No                               | `anon`                           |
| `anon`          | No                               | `anon`                           |
| Publishable key | Yes                              | `authenticated`                  |
| `anon`          | Yes                              | `authenticated`                  |


### Protection

These keys provide first-layer protection to your project's data, performance and bill, such as:

*   Providing basic Denial-of-Service protection, by requiring a minimal threshold of knowledge.
*   Protecting your bill by ignoring bots, scrapers, automated vulnerability scanners and other well meaning or random Internet activity.


### Security considerations

The publishable and `anon` keys are not intended to protect from the following, since key retrieval is always possible from a public component:

*   Static or dynamic code analysis and reverse engineering attempts.
*   Use of the Network inspector in the browser.
*   Cross-site request forgery, cross-site scripting, phishing attacks.
*   Man-in-the-middle attacks.

When using the publishable or `anon` key, access to your project's data is guarded by Postgres via the built-in `anon` and `authenticated` roles. For full protection make sure:

*   You have enabled Row Level Security on all tables.
*   You regularly review your Row Level Security policies for permissions granted to the `anon` and `authenticated` roles.
*   You do not modify the role's attributes without understanding the changes you are making.

Your project's [Security Advisor](/dashboard/project/_/advisors/security) constantly checks for common security problems with the built-in Postgres roles. Make sure you carefully review each finding before dismissing it.



## `service_role` and secret keys

Unlike the `anon` and publishable key, the `service_role` and secret keys allow elevated access to your project's data. It is meant to be used only in secure, developer-controlled components of your application, such as:

*   Servers that implement prior authorization themselves, such as Edge Functions, microservices, traditional or specialized web servers.
*   Periodic jobs, queue processors, topic subscribers.
*   Admin and back-office tools, with prior authorization checks only.
*   Data processing pipelines, such as for analytics, reports, backups, or database synchronization.

<Admonition type="caution">
  Never expose your `service_role` and secret keys publicly. Your data is at risk. **Do not:**

  *   Add in web pages, public documents, source code, bundle in executables or packages for mobile, desktop or CLI apps.
  *   Send over chat applications, email or SMS to your peers.
  *   Never use in a browser, even on `localhost`!
  *   Do not pass in URLs or query params, as these are often logged.
  *   Be careful passing them in request headers without prior log sanitization.
  *   Take extra care logging even potentially **invalid API keys**. Simple typos might reveal the real key in the future.
  *   Reveal, copy, use or manipulate on hardware devices without full disk encryption and which you do not directly own or control (such as public computers, friend's laptop, etc.)

  Ensure you handle them with care and using [secure coding practices](https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/stable-en/).
</Admonition>

Secret keys and the `service_role` JWT-based API key authorize access to your project's data via the built-in `service_role` Postgres role. By design, this role has full access to your project's data. It also uses the [`BYPASSRLS` attribute](https://www.postgresql.org/docs/current/ddl-rowsecurity.html#:~:text=BYPASSRLS), skipping any and all Row Level Security policies you attach.

The secret key is an improvement over the old JWT-based `service_role` key, and we recommend using it where possible. It adds more checks to prevent misuse, specifically:

*   You cannot use a secret key in the browser (matches on the `User-Agent` header) and it will always reply with HTTP 401 Unauthorized.
*   You don't need to have any secret keys if you are not using them.


### Best practices for handling secret keys

Below are some starting guidelines on how to securely work with secret keys:

*   Always work with secret keys on computers you fully own or control.
*   Use secure & encrypted send tools to share API keys with others (often provided by good password managers), but prefer the [API Keys](/dashboard/project/_/settings/api-keys/new) dashboard instead.
*   Prefer encrypting them when stored in files or environment variables.
*   Do not add in source control, especially for CI scripts and tools. Prefer using the tool's native secrets capability instead.
*   Prefer using a separate secret key for each separate backend component of your application, so that if one is found to be vulnerable or to have leaked the key you will only need to change it and not all.
*   Even though a secret key will always return HTTP 401 Unauthorized error when used in a browser, it does not mean that attackers will not use it with other tools. Delete immediately!
*   If you must include them in logs, log the first few random characters (but never more than 6).
*   If you wish to log or store which valid API key was used, store it as a SHA256 hash.


### What to do if a secret key or `service_role` has been leaked or compromised?

Don't rush if this has happened, or you are suspecting it has. Make sure you have fully considered the situation and have remediated the root cause of the suspicion or vulnerability **first**. Consider using the [OWASP Risk Rating Methodology](https://owasp.org/www-community/OWASP_Risk_Rating_Methodology) as an easy way to identify the severity of the incident and to plan your next steps.

Rotating a secret key (`sb_secret_...`) is easy and painless. Use the [API Keys](/dashboard/project/_/settings/api-keys/new) dashboard to create a new secret API key, then replace it with the compromised key. Once all components are using the new key, delete the compromised one.

**Deleting a secret key is irreversible and once done it will be gone forever.**

If you are still using the JWT-based `service_role` key, there are two options.

1.  **Strongly recommended:** Replace the `service_role` key with a new secret key instead. Follow the guide from above as if you are rotating an existing secret key.
2.  [Rotate your project's JWT secret.](/dashboard/project/_/settings/jwt) This operation is only recommended if you suspect that the JWT secret has leaked itself. Consider switching your `anon` JWT-based key to the publishable key, and all `service_role` JWT-based keys to secret keys. Only then rotate the JWT secret. Check the FAQ below if you use the JWT-based keys in mobile, desktop or CLI applications!



## Known limitations and compatibility differences

As the publishable and secret keys are no longer JWT-based, there are some known limitations and compatibility differences that you may need to plan for:

*   You cannot send a publishable or secret key in the `Authorization: Bearer ...` header, except if the value exactly equals the `apikey` header. In this case, your request will be forwarded down to your project's database, but will be rejected as the value is not a JWT.
*   Edge Functions **only support JWT verification** via the `anon` and `service_role` JWT-based API keys. You will need to use the `--no-verify-jwt` option when using publishable and secret keys. The Supabase platform does not verify the `apikey` header when using Edge Functions in this way. Implement your own `apikey`-header authorization logic inside the Edge Function code itself.
*   Public Realtime connections are limited to 24 hours in duration, unless the connection is upgraded and further maintained with user-level authentication via Supabase Auth or a supported Third-Party Auth provider.



## Frequently asked questions

{/* supa-mdx-lint-disable Rule004ExcludeWords */}


### I am using JWT-based `anon` key in a mobile, desktop, or CLI application and need to rotate my `service_role` JWT secret?

If you know or suspect that the JWT secret itself is leaked, refer to the section on [rotating the JWT](#what-to-do-if-a-secret-key-or-servicerole-has-been-leaked-or-compromised).

If the JWT secret is secure, prefer substituting the `service_role` JWT-based key with a new secret key which you can create in the [API Keys](/dashboard/project/_/settings/api-keys/new) dashboard. This will prevent downtime for your application.


### Can I still use my old `anon` and `service-role` API keys after enabling the publishable and secret keys?

Yes. This allows you to transition between the API keys with zero downtime by gradually swapping your clients while both sets of keys are active. See the next question for how to deactivate your keys once all your clients are switched over.


### How do I deactivate the `anon` and `service_role` JWT-based API keys after moving to publishable and secret keys?

You can do this in the [API Keys](/dashboard/project/_/settings/api-keys/new) dashboard. To prevent downtime in your application's components, use the last used indicators on the page to confirm that these are no longer used before deactivating.

You can re-activate them should you need to.


### Why are `anon` and `service_role` JWT-based keys no longer recommended?

Since the start of Supabase, the JWT-based `anon` and `service_role` keys were the right trade-off against simplicity and relative security for your project. Unfortunately they pose some real challenges in live applications, especially around rotation and security best practices.

The main reasons for preferring the publishable and secret keys (`sb_publishable_...` and `sb_secret_...`) are:

*   Tight coupling between the JWT secret (which itself can be compromised, if you mint your own JWTs), the `anon` (low privilege) and `service_role` (high privilege) and `authenticated` (issued by Supabase Auth) Postgres roles.
*   Inability to independently rotate each aspect of the keys, without downtime.
*   Inability to roll-back an unnecessary or problematic JWT secret rotation.
*   Publishing new versions of mobile applications can take days and often weeks in the app review phase with Apple's App Store and Google's Play Store. A forced rotation can cause weeks of downtime for mobile app users.
*   Users may continue using desktop, CLI and mobile apps with very old versions, making rotation impossible without a forced version upgrade.
*   JWTs had 10-year expiry duration, giving malicious actors more to work with.
*   JWTs were self-referential and full of redundant information not necessary for achieving their primary purpose.
*   JWTs are large, hard to parse, verify, and manipulate -- leading to insecure logging or bad security practices.
*   They were signed with a symmetric JWT secret.


### Why is there no publishable or secret keys in the CLI / self-hosting?

Publishable and secret keys are only available on the Supabase hosted platform. They are managed by our API Gateway component, which does not currently have a CLI equivalent.

We are looking into providing similar but limited in scope support for publishable or secret keys in the future. For now you can only use the `anon` and `service_role` JWT-based keys there.

For advanced users, see the following question on how these keys are implemented on the hosted platform for an idea on how to provide similar functionality for yourself.


### How are publishable and secret keys implemented on the hosted platform?

When your applications use the Supabase APIs they go through a component called the API Gateway on the Supabase hosted platform. This provides us (and therefore you) with the following features:

*   Observability and logging.
*   Performance and request routing (such as to read-replicas).
*   Security, for blocking malicious patterns or behavior on a global scale.

This API Gateway component is able to verify the API key (sent in the `apikey` request header, or for WebSocket in a query param) against your project's publishable and secret key list. If the match is found, it mints a temporary, short-lived JWT that is then forwarded down to your project's servers.

It may be possible to replicate similar behavior if you self-host by using programmable proxies such as [Kong](https://konghq.com/), [Envoy](https://www.envoyproxy.io/), [NGINX](https://nginx.org/) or similar.



# How to do automatic retries with `supabase-js`

Learn how to add automatic retries to your Supabase API requests using `fetch-retry`.

<Admonition type="danger" title="Important">
  You should only enable retries if your requests fail with network errors (e.g. 520 status from Cloudflare). A high number of retries have the potential to exhaust the Data API connection pool, which could result in lower throughput and failed requests.
</Admonition>

The `fetch-retry` package allows you to add retry logic to `fetch` requests, making it a useful tool for enhancing the resilience of API calls in your Supabase applications. Here's a step-by-step guide on how to integrate `fetch-retry` with the `supabase-js` library.



## 1. Install dependencies

To get started, ensure you have both `supabase-js` and `fetch-retry` installed in your project:

```bash
npm install @supabase/supabase-js fetch-retry
```



## 2. Wrap the fetch function

The `fetch-retry` package works by wrapping the native `fetch` function. You can create a custom fetch instance with retry logic and pass it to the `supabase-js` client.

```javascript
import { createClient } from '@supabase/supabase-js'
import fetchRetry from 'fetch-retry'

// Wrap the global fetch with fetch-retry
const fetchWithRetry = fetchRetry(fetch)

// Create a Supabase client instance with the custom fetch
const supabase = createClient(
  'https://your-supabase-url.supabase.co',
  'sb_publishable_... or anon key',
  {
    global: {
      fetch: fetchWithRetry,
    },
  }
)
```



## 3. Configure retry options

You can configure `fetch-retry` options to control retry behavior, such as the number of retries, retry delay, and which errors should trigger a retry.

Here is an example with custom retry options:

```javascript
const fetchWithRetry = fetchRetry(fetch, {
  retries: 3, // Number of retry attempts
  retryDelay: (attempt) => Math.min(1000 * 2 ** attempt, 30000), // Exponential backoff
  retryOn: [520], // Retry only on Cloudflare errors
})
```

In this example, the `retryDelay` function implements an exponential backoff strategy, and retries are triggered only for specific HTTP status codes.



## 4. Using the Supabase client

With `fetch-retry` integrated, you can use the Supabase client as usual. The retry logic will automatically apply to all network requests made by `supabase-js`.

```javascript
async function fetchData() {
  const { data, error } = await supabase.from('your_table').select('*')

  if (error) {
    console.error('Error fetching data:', error)
  } else {
    console.log('Fetched data:', data)
  }
}

fetchData()
```



## 5. Fine-Tuning retries for specific requests

If you need different retry logic for certain requests, you can use the `retryOn` with a custom function to inspect the URL or response and decide whether to retry the request.

```javascript
const fetchWithRetry = fetchRetry(fetch, {
  retryDelay: (attempt) => Math.min(1000 * 2 ** attempt, 30000),
  retryOn: (attempt, error, response) => {
    const shouldRetry
      = (attempt: number, error: Error | null, response: Response | null) =>
        attempt < 3
          && response
          && response.status == 520 // Cloudflare errors
          && response.url.includes('rpc/your_stored_procedure')

    if (shouldRetry(attempt, error, response)) {
      console.log(`Retrying request... Attempt #${attempt}`, response)
      return true
    }

    return false
  }
})

async function yourStoredProcedure() {
  const { data, error } = await supabase
    .rpc('your_stored_procedure', { param1: 'value1' });

  if (error) {
    console.log('Error executing RPC:', error);
  } else {
    console.log('Response:', data);
  }
}

yourStoredProcedure();
```

By using `retryOn` with a custom function, you can define specific conditions for retrying requests. In this example, the retry logic is applied only to requests targeting a specific stored procedure.



## Conclusion

Integrating `fetch-retry` with `supabase-js` is a straightforward way to add robustness to your Supabase API requests. By handling transient errors and implementing retry strategies, you can improve the reliability of your application while maintaining a seamless user experience.



# Creating API Routes



API routes are automatically created when you create Postgres Tables, Views, or Functions.



## Create a table

Let's create our first API route by creating a table called `todos` to store tasks.
This creates a corresponding route `todos` which can accept `GET`, `POST`, `PATCH`, & `DELETE` requests.

<Tabs scrollable size="small" type="underlined" defaultActiveId="dashboard" queryGroup="database-method">
  <TabPanel id="dashboard" label="Dashboard">
    1.  Go to the [Table editor](/dashboard/project/_/editor) page in the Dashboard.
    2.  Click **New Table** and create a table with the name `todos`.
    3.  Click **Save**.
    4.  Click **New Column** and create a column with the name `task` and type `text`.
    5.  Click **Save**.

    <video width="99%" muted playsInline controls={true}>
      <source src="https://xguihxuzqibwxjnimxev.supabase.co/storage/v1/object/public/videos/docs/api/api-create-table-sm.mp4" type="video/mp4" />
    </video>
  </TabPanel>

  <TabPanel id="sql" label="SQL">
    ```sql
     -- Create a table called "todos" with a column to store tasks.
    create table
      todos (
        id bigint generated by default as identity primary key,
        task text check (char_length(task) > 3)
      );
    ```
  </TabPanel>
</Tabs>



## API URL and keys

Every Supabase project has a unique API URL. Your API is secured behind an API gateway which requires an API Key for every request.

1.  Go to the [Settings](/dashboard/project/_/settings/general) page in the Dashboard.
2.  Click **API** in the sidebar.
3.  Find your API `URL`, `anon`, and `service_role` keys on this page.

<video width="99%" muted playsInline controls={true}>
  <source src="https://xguihxuzqibwxjnimxev.supabase.co/storage/v1/object/public/videos/docs/api/api-url-and-key.mp4" type="video/mp4" />
</video>

The REST API is accessible through the URL `https://<project_ref>.supabase.co/rest/v1`

Both of these routes require the `anon` key to be passed through an `apikey` header.



## Using the API

You can interact with your API directly via HTTP requests, or you can use the client libraries which we provide.

Let's see how to make a request to the `todos` table which we created in the first step,
using the API URL (`SUPABASE_URL`) and Key (`SUPABASE_PUBLISHABLE_KEY`) we provided:

<Tabs scrollable size="small" type="underlined" defaultActiveId="javascript" queryGroup="language">
  <TabPanel id="javascript" label="Javascript">
    ```javascript
    // Initialize the JS client
    import { createClient } from '@supabase/supabase-js'
    const supabase = createClient(SUPABASE_URL, SUPABASE_PUBLISHABLE_KEY)

    // Make a request
    const { data: todos, error } = await supabase.from('todos').select('*')
    ```
  </TabPanel>

  <TabPanel id="curl" label="cURL">
    ```bash
    # Append /rest/v1/ to your URL, and then use the table name as the route
    curl '<SUPABASE_URL>/rest/v1/todos' \
    -H "apikey: <SUPABASE_PUBLISHABLE_KEY>" \
    -H "Authorization: Bearer <SUPABASE_PUBLISHABLE_KEY>"
    ```
  </TabPanel>
</Tabs>

JS Reference: [`select()`](/docs/reference/javascript/select),
[`insert()`](/docs/reference/javascript/insert),
[`update()`](/docs/reference/javascript/update),
[`upsert()`](/docs/reference/javascript/upsert),
[`delete()`](/docs/reference/javascript/delete),
[`rpc()`](/docs/reference/javascript/rpc) (call Postgres functions).



# Build an API route in less than 2 minutes.

Create your first API route by creating a table called `todos` to store tasks.

Let's create our first REST route which we can query using `cURL` or the browser.

We'll create a database table called `todos` for storing tasks. This creates a corresponding API route `/rest/v1/todos` which can accept `GET`, `POST`, `PATCH`, & `DELETE` requests.

<StepHikeCompact>
  <StepHikeCompact.Step step={1}>
    <StepHikeCompact.Details title="Set up a Supabase project with a 'todos' table">
      [Create a new project](/dashboard) in the Supabase Dashboard.

      After your project is ready, create a table in your Supabase database. You can do this with either the Table interface or the [SQL Editor](/dashboard/project/_/sql).
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <Tabs scrollable size="small" type="underlined" defaultActiveId="sql" queryGroup="database-method">
        <TabPanel id="sql" label="SQL">
          ```sql
          -- Create a table called "todos"
          -- with a column to store tasks.
          create table todos (
            id serial primary key,
            task text
          );
          ```
        </TabPanel>

        <TabPanel id="dashboard" label="Dashboard">
          <video width="99%" muted playsInline controls={true}>
            <source src="https://xguihxuzqibwxjnimxev.supabase.co/storage/v1/object/public/videos/docs/api/api-create-table-sm.mp4" type="video/mp4" />
          </video>
        </TabPanel>
      </Tabs>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={2}>
    <StepHikeCompact.Details title="Allow public access">
      Let's turn on Row Level Security for this table and allow public access.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      ```sql
      -- Turn on security
      alter table "todos"
      enable row level security;

      -- Allow anonymous access
      create policy "Allow public access"
        on todos
        for select
        to anon
        using (true);
      ```
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={3}>
    <StepHikeCompact.Details title="Insert some dummy data">
      Now we can add some data to our table which we can access through our API.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      ```sql
      insert into todos (task)
      values
        ('Create tables'),
        ('Enable security'),
        ('Add data'),
        ('Fetch data from the API');
      ```
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={4}>
    <StepHikeCompact.Details title="Fetch the data">
      Find your API URL and Keys in your Dashboard [API Settings](/dashboard/project/_/settings/api). You can now query your "todos" table by appending `/rest/v1/todos` to the API URL.

      Copy this block of code, substitute `<PROJECT_REF>` and `<ANON_KEY>`, then run it from a terminal.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      ```bash Terminal
      curl 'https://<PROJECT_REF>.supabase.co/rest/v1/todos' \
      -H "apikey: <ANON_KEY>" \
      -H "Authorization: Bearer <ANON_KEY>"
      ```
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>
</StepHikeCompact>



## Bonus

There are several options for accessing your data:


### Browser

You can query the route in your browser, by appending the `anon` key as a query parameter:

`https://<PROJECT_REF>.supabase.co/rest/v1/todos?apikey=<ANON_KEY>`


### Client libraries

We provide a number of [Client Libraries](https://github.com/supabase/supabase#client-libraries).

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    ```js
    const { data, error } = await supabase.from('todos').select()
    ```
  </TabPanel>

  <TabPanel id="dart" label="Dart">
    ```dart
    final data = await supabase.from('todos').select('*');
    ```
  </TabPanel>

  <TabPanel id="python" label="Python">
    ```python
    response = supabase.table('todos').select("*").execute()
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    ```swift
    let response = try await supabase.from("todos").select()
    ```
  </TabPanel>
</Tabs>



# Securing your API



The data APIs are designed to work with Postgres Row Level Security (RLS). If you use [Supabase Auth](/docs/guides/auth), you can restrict data based on the logged-in user.

To control access to your data, you can use [Policies](/docs/guides/auth#policies).



## Enabling row level security

Any table you create in the `public` schema will be accessible via the Supabase Data API.

To restrict access, enable Row Level Security (RLS) on all tables, views, and functions in the `public` schema. You can then write RLS policies to grant users access to specific database rows or functions based on their authentication token.

<Admonition type="danger">
  Always enable Row Level Security on tables, views, and functions in the `public` schema to protect your data.
</Admonition>

Any table created through the Supabase Dashboard will have RLS enabled by default. If you created the tables via the SQL editor or via another way, enable RLS like so:

<Tabs scrollable size="small" type="underlined" defaultActiveId="dashboard" queryGroup="database-method">
  <TabPanel id="dashboard" label="Dashboard">
    1.  Go to the [Authentication > Policies](/dashboard/project/_/auth/policies) page in the Dashboard.
    2.  Select **Enable RLS** to enable Row Level Security.
  </TabPanel>

  <TabPanel id="sql" label="SQL">
    ```sql
    alter table
      todos enable row level security;
    ```
  </TabPanel>
</Tabs>

With RLS enabled, you can create Policies that allow or disallow users to access and update data. We provide a detailed guide for creating Row Level Security Policies in our [Authorization documentation](/docs/guides/database/postgres/row-level-security).

<Admonition type="danger">
  Any table **without RLS enabled** in the `public` schema will be accessible to the public, using the `anon` role. Always make sure that RLS is enabled or that you've got other security measures in place to avoid unauthorized access to your project's data!
</Admonition>



## Disable the API or restrict to custom schema

If you don't use the Data API, or if you don't want to expose the `public` schema, you can either disable it entirely or change the automatically exposed schema to one of your choice. See **[Hardening the Data API](/docs/guides/database/hardening-data-api)** for instructions.



## Enforce additional rules on each request

Using Row Level Security policies may not always be adequate or sufficient to protect APIs.

Here are some common situations where additional protections are necessary:

*   Enforcing per-IP or per-user rate limits.
*   Checking custom or additional API keys before allowing further access.
*   Rejecting requests after exceeding a quota or requiring payment.
*   Disallowing direct access to certain tables, views or functions in the `public` schema.

You can build these cases in your application by creating a Postgres function that will read information from the request and perform additional checks, such as counting the number of requests received or checking that an API key is already registered in your database before serving the response.

Define a function like so:

```sql
create function public.check_request()
  returns void
  language plpgsql
  security definer
  as $$
begin
  -- your logic here
end;
$$;
```

And register it to run on every Data API request using:

```sql
alter role authenticator
  set pgrst.db_pre_request = 'public.check_request';
```

This configures the `public.check_request` function to run on every Data API request. To have the changes take effect, you should run:

```sql
notify pgrst, 'reload config';
```

Inside the function you can perform any additional checks on the request headers or JWT and raise an exception to prevent the request from completing. For example, this exception raises a HTTP 402 Payment Required response with a `hint` and additional `X-Powered-By` header:

```sql
raise sqlstate 'PGRST' using
  message = json_build_object(
    'code',    '123',
    'message', 'Payment Required',
    'details', 'Quota exceeded',
    'hint',    'Upgrade your plan')::text,
  detail = json_build_object(
    'status',  402,
    'headers', json_build_object(
      'X-Powered-By', 'Nerd Rage'))::text;
```

When raised within the `public.check_request` function, the resulting HTTP response will look like:

```http
HTTP/1.1 402 Payment Required
Content-Type: application/json; charset=utf-8
X-Powered-By: Nerd Rage

{
  "message": "Payment Required",
  "details": "Quota exceeded",
  "hint": "Upgrade your plan",
  "code": "123"
}
```

Use the [JSON operator functions](https://www.postgresql.org/docs/current/functions-json.html) to build rich and dynamic responses from exceptions.

If you use a custom HTTP status code like 419, you can supply the `status_text` key in the `detail` clause of the exception to describe the HTTP status.

If you're using PostgREST version 11 or lower ([find out your PostgREST version](/dashboard/project/_/settings/infrastructure)) a different and less powerful [syntax](https://postgrest.org/en/stable/references/errors.html#raise-errors-with-http-status-codes) needs to be used.


### Accessing request information

Like with RLS policies, you can access information about the request by using the `current_setting()` Postgres function. Here are some examples on how this works:

```sql
-- To get all the headers sent in the request
SELECT current_setting('request.headers', true)::json;

-- To get a single header, you can use JSON arrow operators
SELECT current_setting('request.headers', true)::json->>'user-agent';

-- Access Cookies
SELECT current_setting('request.cookies', true)::json;
```

| `current_setting()` | Example                                         | Description                          |
| ------------------- | ----------------------------------------------- | ------------------------------------ |
| `request.method`    | `GET`, `HEAD`, `POST`, `PUT`, `PATCH`, `DELETE` | Request's method                     |
| `request.path`      | `table`                                         | Table's path                         |
| `request.path`      | `view`                                          | View's path                          |
| `request.path`      | `rpc/function`                                  | Functions's path                     |
| `request.headers`   | `{ "User-Agent": "...", ... }`                  | JSON object of the request's headers |
| `request.cookies`   | `{ "cookieA": "...", "cookieB": "..." }`        | JSON object of the request's cookies |
| `request.jwt`       | `{ "sub": "a7194ea3-...", ... }`                | JSON object of the JWT payload       |

To access the IP address of the client look up the [X-Forwarded-For header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Forwarded-For) in the `request.headers` setting. For example:

```sql
SELECT split_part(
  current_setting('request.headers', true)::json->>'x-forwarded-for',
  ',', 1); -- takes the client IP before the first comma (,)
```

Read more about [PostgREST's pre-request function](https://postgrest.org/en/stable/references/transactions.html#pre-request).


### Examples

<Tabs scrollable size="small" type="underlined" defaultActiveId="rate-limit-per-ip" queryGroup="pre-request">
  <TabPanel id="rate-limit-per-ip" label="Rate limit per IP">
    You can only rate-limit `POST`, `PUT`, `PATCH` and `DELETE` requests. This is because `GET` and `HEAD` requests run in read-only mode, and will be served by [Read Replicas](/docs/guides/platform/read-replicas) which do not support writing to the database.

    Outline:

    *   A new row is added to a `private.rate_limits` table each time a modifying action is done to the database containing the IP address and the timestamp of the action.
    *   If there are over 100 requests from the same IP address in the last 5 minutes, the request is rejected with a HTTP 420 code.

    Create the table:

    ```sql
    create table private.rate_limits (
      ip inet,
      request_at timestamp
    );

    -- add an index so that lookups are fast
    create index rate_limits_ip_request_at_idx on private.rate_limits (ip, request_at desc);
    ```

    The `private` schema is used as it cannot be accessed over the API!

    Create the `public.check_request` function:

    ```sql
    create function public.check_request()
      returns void
      language plpgsql
      security definer
      as $$
    declare
      req_method text := current_setting('request.method', true);
      req_ip inet := split_part(
        current_setting('request.headers', true)::json->>'x-forwarded-for',
        ',', 1)::inet;
      count_in_five_mins integer;
    begin
      if req_method = 'GET' or req_method = 'HEAD' or req_method is null then
        -- rate limiting can't be done on GET and HEAD requests
        return;
      end if;

      select
        count(*) into count_in_five_mins
      from private.rate_limits
      where
        ip = req_ip and request_at between now() - interval '5 minutes' and now();

      if count_in_five_mins > 100 then
        raise sqlstate 'PGRST' using
          message = json_build_object(
            'message', 'Rate limit exceeded, try again after a while')::text,
          detail = json_build_object(
            'status',  420,
            'status_text', 'Enhance Your Calm')::text;
      end if;

      insert into private.rate_limits (ip, request_at) values (req_ip, now());
    end;
      $$;
    ```

    Finally, configure the `public.check_request()` function to run on every Data API request:

    ```sql
    alter role authenticator
      set pgrst.db_pre_request = 'public.check_request';

    notify pgrst, 'reload config';
    ```

    To clear old entries in the `private.rate_limits` table, set up a [pg\_cron](/docs/guides/database/extensions/pg_cron) job to clean them up.
  </TabPanel>

  <TabPanel id="use-additional-api-key" label="Use additional API keys">
    Some applications can benefit from using additional API keys managed by the application **in addition to the [Supabase API keys](/docs/guides/api/api-keys)**. This is commonly necessary in cases like:

    *   Applications that use the Data API without RLS policies.
    *   Applications that do not use [Supabase Auth](/auth) or any other authentication system and rely on the `anon` role.

    <Admonition type="tip">
      Using the `apikey` header with the [Supabase API keys](/docs/guides/api/api-keys) is mandatory and not configurable. If you use additional API keys, you have to distribute both the `anon` API key and your application's custom API key.
    </Admonition>

    Outline:

    *   Your application requires the presence of the `x-app-api-key` header when the `anon` role is used to prevent abuse of your API.
    *   These API keys are stored in the `private.anon_api_keys` table, and are distributed independently.
    *   Each request using the `anon` role will be blocked with HTTP 403 if the `x-app-api-key` header is not registered in the table.

    Set up the table:

    ```sql
    create table private.anon_api_keys (
      id uuid primary key,
      -- other relevant fields
    );
    ```

    Create the `public.check_request` function:

    ```sql
    create function public.check_request()
      returns void
      language plpgsql
      security definer
      as $$
    declare
      req_app_api_key text := current_setting('request.headers', true)::json->>'x-app-api-key';
      is_app_api_key_registered boolean;
      jwt_role text := current_setting('request.jwt.claims', true)::json->>'role';
    begin
      if jwt_role <> 'anon' then
        -- not `anon` role, allow the request to pass
        return;
      end if;

      select
        true into is_app_api_key_registered
      from private.anon_api_keys
      where
        id = req_app_api_key::uuid
      limit 1;

      if is_app_api_key_registered is true then
        -- api key is registered, allow the request to pass
        return;
      end if;

      raise sqlstate 'PGRST' using
        message = json_build_object(
          'message', 'No registered API key found in x-app-api-key header.')::text,
        detail = json_build_object(
          'status', 403)::text;
    end;
      $$;
    ```

    Finally, configure the `public.check_request()` function to run on every Data API request:

    ```sql
    alter role authenticator
      set pgrst.db_pre_request = 'public.check_request';

    notify pgrst, 'reload config';
    ```
  </TabPanel>
</Tabs>



# Converting SQL to JavaScript API



Many common SQL queries can be written using the JavaScript API, provided by the SDK to wrap Data API calls. Below are a few examples of conversions between SQL and JavaScript patterns.



## Select statement with basic clauses

Select a set of columns from a single table with where, order by, and limit clauses.

```sql
select first_name, last_name, team_id, age
from players
where age between 20 and 24 and team_id != 'STL'
order by last_name, first_name desc
limit 20;
```

```js
const { data, error } = await supabase
  .from('players')
  .select('first_name,last_name,team_id,age')
  .gte('age', 20)
  .lte('age', 24)
  .not('team_id', 'eq', 'STL')
  .order('last_name', { ascending: true }) // or just .order('last_name')
  .order('first_name', { ascending: false })
  .limit(20)
```



## Select statement with complex Boolean logic clause

Select all columns from a single table with a complex where clause: OR AND OR

```sql
select *
from players
where ((team_id = 'CHN' or team_id is null) and (age > 35 or age is null));
```

```js
const { data, error } = await supabase
  .from('players')
  .select() // or .select('*')
  .or('team_id.eq.CHN,team_id.is.null')
  .or('age.gt.35,age.is.null') // additional filters imply "AND"
```

Select all columns from a single table with a complex where clause: AND OR AND

```sql
select *
from players
where ((team_id = 'CHN' and age > 35) or (team_id != 'CHN' and age is not null));
```

```js
const { data, error } = await supabase
  .from('players')
  .select() // or .select('*')
  .or('and(team_id.eq.CHN,age.gt.35),and(team_id.neq.CHN,.not.age.is.null)')
```



## Resources

*   [Supabase - Get started for free](https://supabase.com)
*   [PostgREST Operators](https://postgrest.org/en/stable/api.html#operators)
*   [Supabase API: JavaScript select](/docs/reference/javascript/select)
*   [Supabase API: JavaScript modifiers](/docs/reference/javascript/using-modifiers)
*   [Supabase API: JavaScript filters](/docs/reference/javascript/using-filters)



# SQL to REST API Translator

Translate SQL queries to HTTP requests and Supabase client code

Sometimes it's challenging to translate SQL queries to the equivalent [PostgREST](https://postgrest.org/) request or Supabase client code. Use this tool to help with this translation.

<Admonition type="note">
  PostgREST supports a subset of SQL, so not all SQL queries will translate.
</Admonition>

<SqlToRest
  defaultValue={`select
  title,
  description
from
  books
where
  description ilike '%cheese%'
order by
  title desc
limit
  5
offset
  10`}
/>



# Using Custom Schemas



By default, your database has a `public` schema which is automatically exposed on data APIs.



## Creating custom schemas

You can create your own custom schema/s by running the following SQL, substituting `myschema` with the name you want to use for your schema:

```sql
CREATE SCHEMA myschema;
```



## Exposing custom schemas

You can expose custom database schemas - to do so you need to follow these steps:

1.  Go to [API settings](/dashboard/project/_/settings/api) and add your custom schema to "Exposed schemas".
2.  Run the following SQL, substituting `myschema` with your schema name:

```sql
GRANT USAGE ON SCHEMA myschema TO anon, authenticated, service_role;
GRANT ALL ON ALL TABLES IN SCHEMA myschema TO anon, authenticated, service_role;
GRANT ALL ON ALL ROUTINES IN SCHEMA myschema TO anon, authenticated, service_role;
GRANT ALL ON ALL SEQUENCES IN SCHEMA myschema TO anon, authenticated, service_role;
ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA myschema GRANT ALL ON TABLES TO anon, authenticated, service_role;
ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA myschema GRANT ALL ON ROUTINES TO anon, authenticated, service_role;
ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA myschema GRANT ALL ON SEQUENCES TO anon, authenticated, service_role;
```

Now you can access these schemas from data APIs:

<Tabs scrollable size="small" type="underlined" defaultActiveId="javascript" queryGroup="language">
  <TabPanel id="javascript" label="JavaScript">
    ```js
    // Initialize the JS client
    import { createClient } from '@supabase/supabase-js'
    const supabase = createClient(SUPABASE_URL, SUPABASE_PUBLISHABLE_KEY, {
      db: { schema: 'myschema' },
    })

    // Make a request
    const { data: todos, error } = await supabase.from('todos').select('*')

    // You can also change the target schema on a per-query basis
    const { data: todos, error } = await supabase.schema('myschema').from('todos').select('*')
    ```
  </TabPanel>

  <TabPanel id="dart" label="Dart">
    ```dart
    // Initialize the Flutter client
    await Supabase.initialize(
      url: supabaseUrl,
      anonKey: supabaseKey,
      postgrestOptions: const PostgrestClientOptions(schema: 'myschema'),
    );
    final supabase = Supabase.instance.client;

    // Make a request
    final data = await supabase.from('todos').select();

    // You can also change the target schema on a per-query basis
    final data = await supabase.schema('myschema').from('todos').select();

    ```
  </TabPanel>

  <TabPanel id="curl" label="cURL">
    ```bash
    # Append /rest/v1/ to your URL, and then use the table name as the route.

    # for GET or HEAD request use Accept-Profile
    curl '<SUPABASE_URL>/rest/v1/todos' \
      -H "apikey: <SUPABASE_PUBLISHABLE_KEY>" \
      -H "Authorization: Bearer <SUPABASE_PUBLISHABLE_KEY>" \
      -H "Accept-Profile: myschema"

    # for POST, PATCH, PUT and DELETE Request use Content-Profile
    curl -X POST '<SUPABASE_URL>/rest/v1/todos' \
      -H "apikey: <SUPABASE_PUBLISHABLE_KEY>" \
      -H "Authorization: Bearer <SUPABASE_PUBLISHABLE_KEY>" \
      -H "Content-Type: application/json" \
      -H "Content-Profile: myschema" \
      -d '{"column_name": "value"}'
    ```
  </TabPanel>
</Tabs>



# Auto-generated documentation



Supabase generates documentation in the [Dashboard](/dashboard) which updates as you make database changes.

1.  Go to the [API](/dashboard/project/_/api) page in the Dashboard.
2.  Select any table under **Tables and Views** in the sidebar.
3.  Switch between the JavaScript and the cURL docs using the tabs.

<video width="99%" muted playsInline controls={true}>
  <source src="https://xguihxuzqibwxjnimxev.supabase.co/storage/v1/object/public/videos/docs/api/api-docs.mp4" type="video/mp4" />
</video>



# Client Libraries



Supabase provides client libraries for the REST and Realtime APIs. Some libraries are officially supported, and some are contributed by the community.



## Official libraries

| `Language`            | `Source Code`                                                                                        | `Documentation`                                 |
| --------------------- | ---------------------------------------------------------------------------------------------------- | ----------------------------------------------- |
| Javascript/Typescript | [supabase-js](https://github.com/supabase/supabase-js)                                               | [Docs](/docs/reference/javascript/introduction) |
| Dart/Flutter          | [supabase-flutter](https://github.com/supabase/supabase-flutter/tree/main/packages/supabase_flutter) | [Docs](/docs/reference/dart/introduction)       |
| Swift                 | [supabase-swift](https://github.com/supabase/supabase-swift)                                         | [Docs](/docs/reference/swift/introduction)      |
| Python                | [supabase-py](https://github.com/supabase/supabase-py)                                               | [Docs](/docs/reference/python/initializing)     |



## Community libraries

| `Language`              | `Source Code`                                                                    | `Documentation`                             |
| ----------------------- | -------------------------------------------------------------------------------- | ------------------------------------------- |
| C#                      | [supabase-csharp](https://github.com/supabase-community/supabase-csharp)         | [Docs](/docs/reference/csharp/introduction) |
| Go                      | [supabase-go](https://github.com/supabase-community/supabase-go)                 |                                             |
| Kotlin                  | [supabase-kt](https://github.com/supabase-community/supabase-kt)                 | [Docs](/docs/reference/kotlin/introduction) |
| Ruby                    | [supabase-rb](https://github.com/supabase-community/supabase-rb)                 |                                             |
| Godot Engine (GDScript) | [supabase-gdscript](https://github.com/supabase-community/godot-engine.supabase) |                                             |



# Generating TypeScript Types

How to generate types for your API and Supabase libraries.

Supabase APIs are generated from your database, which means that we can use database introspection to generate type-safe API definitions.



## Generating types from project dashboard

Supabase allows you to generate and download TypeScript types directly from the [project dashboard](/dashboard/project/_/api?page=tables-intro).



## Generating types using Supabase CLI

The Supabase CLI is a single binary Go application that provides everything you need to setup a local development environment.

You can [install the CLI](https://www.npmjs.com/package/supabase) via npm or other supported package managers. The minimum required version of the CLI is [v1.8.1](https://github.com/supabase/cli/releases).

```bash
npm i supabase@">=1.8.1" --save-dev
```

Login with your Personal Access Token:

```bash
npx supabase login
```

Before generating types, ensure you initialize your Supabase project:

```bash
npx supabase init
```

Generate types for your project to produce the `database.types.ts` file:

```bash
npx supabase gen types typescript --project-id "$PROJECT_REF" --schema public > database.types.ts
```

or in case of local development:

```bash
npx supabase gen types typescript --local > database.types.ts
```

These types are generated from your database schema. Given a table `public.movies`, the generated types will look like:

```sql
create table public.movies (
  id bigint generated always as identity primary key,
  name text not null,
  data jsonb null
);
```

```ts ./database.types.ts
export type Json = string | number | boolean | null | { [key: string]: Json | undefined } | Json[]

export interface Database {
  public: {
    Tables: {
      movies: {
        Row: {
          // the data expected from .select()
          id: number
          name: string
          data: Json | null
        }
        Insert: {
          // the data to be passed to .insert()
          id?: never // generated columns must not be supplied
          name: string // `not null` columns with no default must be supplied
          data?: Json | null // nullable columns can be omitted
        }
        Update: {
          // the data to be passed to .update()
          id?: never
          name?: string // `not null` columns are optional on .update()
          data?: Json | null
        }
      }
    }
  }
}
```



## Using TypeScript type definitions

You can supply the type definitions to `supabase-js` like so:

```ts ./index.tsx
import { createClient } from '@supabase/supabase-js'
import { Database } from './database.types'

const supabase = createClient<Database>(
  process.env.SUPABASE_URL,
  process.env.SUPABASE_PUBLISHABLE_KEY
)
```



## Helper types for tables and joins

You can use the following helper types to make the generated TypeScript types easier to use.

Sometimes the generated types are not what you expect. For example, a view's column may show up as nullable when you expect it to be `not null`. Using [type-fest](https://github.com/sindresorhus/type-fest), you can override the types like so:

```ts ./database-generated.types.ts
export type Json = // ...

export interface Database {
  // ...
}
```

```ts ./database.types.ts
import { MergeDeep } from 'type-fest'
import { Database as DatabaseGenerated } from './database-generated.types'
export { Json } from './database-generated.types'

// Override the type for a specific column in a view:
export type Database = MergeDeep<
  DatabaseGenerated,
  {
    public: {
      Views: {
        movies_view: {
          Row: {
            // id is a primary key in public.movies, so it must be `not null`
            id: number
          }
        }
      }
    }
  }
>
```

<Admonition type="note">
  To use `MergeDeep`, set `compilerOptions.strictNullChecks` to `true` in your `tsconfig.json`.
</Admonition>



## Enhanced type inference for JSON fields

Starting from [supabase-js v2.48.0](https://github.com/supabase/supabase-js/releases/tag/v2.48.0), you can define custom types for JSON fields and get enhanced type inference when using JSON selectors with the `->` and `->>` operators. This makes your code more type-safe and intuitive when working with JSON/JSONB columns.


### Defining custom JSON types

You can extend your generated database types to include custom JSON schemas using `MergeDeep`:

```ts ./database.types.ts
import { MergeDeep } from 'type-fest'
import { Database as DatabaseGenerated } from './database-generated.types'

// Define your custom JSON type
type CustomJsonType = {
  foo: string
  bar: { baz: number }
  en: 'ONE' | 'TWO' | 'THREE'
}

export type Database = MergeDeep<
  DatabaseGenerated,
  {
    public: {
      Tables: {
        your_table: {
          Row: {
            data: CustomJsonType | null
          }
          // Optional: Use if you want type-checking for inserts and updates
          // Insert: {
          //   data?: CustomJsonType | null;
          // };
          // Update: {
          //   data?: CustomJsonType | null;
          // };
        }
      }
      Views: {
        your_view: {
          Row: {
            data: CustomJsonType | null
          }
        }
      }
    }
  }
>
```


### Type-safe JSON querying

Once you've defined your custom JSON types, TypeScript will automatically infer the correct types when using JSON selectors:

```ts
const res = await client.from('your_table').select('data->bar->baz, data->en, data->bar')

if (res.data) {
  console.log(res.data)
  // TypeScript infers the shape of your JSON data:
  // [
  //   {
  //     baz: number;
  //     en: 'ONE' | 'TWO' | 'THREE';
  //     bar: { baz: number };
  //   }
  // ]
}
```

This feature works with:

*   Single-level JSON access: `data->foo`
*   Nested JSON access: `data->bar->baz`
*   Text extraction: `data->>foo` (returns string)
*   Mixed selections combining multiple JSON paths

The type inference automatically handles the difference between `->` (returns JSON) and `->>` (returns text) operators, ensuring your TypeScript types match the actual runtime behavior.

You can also override the type of an individual successful response if needed:

```ts
// Partial type override allows you to only override some of the properties in your results
const { data } = await supabase.from('countries').select().overrideTypes<Array<{ id: string }>>()
// For a full replacement of the original return type use the `{ merge: false }` property as second argument
const { data } = await supabase
  .from('countries')
  .select()
  .overrideTypes<Array<{ id: string }>, { merge: false }>()
// Use it with `maybeSingle` or `single`
const { data } = await supabase.from('countries').select().single().overrideTypes<{ id: string }>()
```


### Type shorthands

The generated types provide shorthands for accessing tables and enums.

```ts ./index.ts
import { Database, Tables, Enums } from "./database.types.ts";

// Before 😕
let movie: Database['public']['Tables']['movies']['Row'] = // ...

// After 😍
let movie: Tables<'movies'>
```


### Response types for complex queries

`supabase-js` always returns a `data` object (for success), and an `error` object (for unsuccessful requests).

These helper types provide the result types from any query, including nested types for database joins.

Given the following schema with a relation between cities and countries:

```sql
create table countries (
  "id" serial primary key,
  "name" text
);

create table cities (
  "id" serial primary key,
  "name" text,
  "country_id" int references "countries"
);
```

We can get the nested `CountriesWithCities` type like this:

```ts
import { QueryResult, QueryData, QueryError } from '@supabase/supabase-js'

const countriesWithCitiesQuery = supabase.from('countries').select(`
  id,
  name,
  cities (
    id,
    name
  )
`)
type CountriesWithCities = QueryData<typeof countriesWithCitiesQuery>

const { data, error } = await countriesWithCitiesQuery
if (error) throw error
const countriesWithCities: CountriesWithCities = data
```



## Update types automatically with GitHub Actions

One way to keep your type definitions in sync with your database is to set up a GitHub action that runs on a schedule.

Add the following script to your `package.json` to run it using `npm run update-types`

```json
"update-types": "npx supabase gen types --lang=typescript --project-id \"$PROJECT_REF\" > database.types.ts"
```

Create a file `.github/workflows/update-types.yml` with the following snippet to define the action along with the environment variables. This script will commit new type changes to your repo every night.

```yaml
name: Update database types

on:
  schedule:
    # sets the action to run daily. You can modify this to run the action more or less frequently
    - cron: '0 0 * * *'

jobs:
  update:
    runs-on: ubuntu-latest
    permissions:
      contents: write
    env:
      SUPABASE_ACCESS_TOKEN: ${{ secrets.ACCESS_TOKEN }}
      PROJECT_REF: <your-project-id>
    steps:
      - uses: actions/checkout@v4
        with:
          persist-credentials: false
          fetch-depth: 0
      - uses: actions/setup-node@v4
        with:
          node-version: 22
      - run: npm run update-types
      - name: check for file changes
        id: git_status
        run: |
          echo "status=$(git status -s)" >> $GITHUB_OUTPUT
      - name: Commit files
        if: ${{contains(steps.git_status.outputs.status, ' ')}}
        run: |
          git add database.types.ts
          git config --local user.email "41898282+github-actions[bot]@users.noreply.github.com"
          git config --local user.name "github-actions[bot]"
          git commit -m "Update database types" -a
      - name: Push changes
        if: ${{contains(steps.git_status.outputs.status, ' ')}}
        uses: ad-m/github-push-action@master
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          branch: ${{ github.ref }}
```

Alternatively, you can use a community-supported GitHub action: [`generate-supabase-db-types-github-action`](https://github.com/lyqht/generate-supabase-db-types-github-action).



## Resources

*   [Generating Supabase types with GitHub Actions](https://blog.esteetey.dev/how-to-create-and-test-a-github-action-that-generates-types-from-supabase-database)



# Automatic embeddings



Vector embeddings enable powerful [semantic search](/docs/guides/ai/semantic-search) capabilities in Postgres, but managing them alongside your content has traditionally been complex. This guide demonstrates how to automate embedding generation and updates using Supabase [Edge Functions](/docs/guides/functions), [pgmq](/docs/guides/database/extensions/pgmq), [pg\_net](/docs/guides/database/extensions/pg_net), and [pg\_cron](/docs/guides/cron).



## Understanding the challenge

When implementing semantic search with pgvector, developers typically need to:

1.  Generate embeddings via an external API (like OpenAI)
2.  Store these embeddings alongside the content
3.  Keep embeddings in sync when content changes
4.  Handle failures and retries in the embedding generation process

While Postgres [full-text search](/docs/guides/database/full-text-search) can handle this internally through synchronous calls to `to_tsvector` and [triggers](https://www.postgresql.org/docs/current/textsearch-features.html#TEXTSEARCH-UPDATE-TRIGGERS), semantic search requires asynchronous API calls to a provider like OpenAI to generate vector embeddings. This guide demonstrates how to use triggers, queues, and Supabase Edge Functions to bridge this gap.



## Understanding the architecture

We'll leverage the following Postgres and Supabase features to create the automated embedding system:

1.  [pgvector](/docs/guides/database/extensions/pgvector): Stores and queries vector embeddings
2.  [pgmq](/docs/guides/queues): Queues embedding generation requests for processing and retries
3.  [pg\_net](/docs/guides/database/extensions/pg_net): Handles asynchronous HTTP requests to Edge Functions directly from Postgres
4.  [pg\_cron](/docs/guides/cron): Automatically processes and retries embedding generations
5.  [Triggers](/docs/guides/database/postgres/triggers): Detects content changes and enqueues embedding generation requests
6.  [Edge Functions](/docs/guides/functions): Generates embeddings via an API like OpenAI (customizable)

We'll design the system to:

1.  Be generic, so that it can be used with any table and content. This allows you to configure embeddings in multiple places, each with the ability to customize the input used for embedding generation. These will all use the same queue infrastructure and Edge Function to generate the embeddings.

2.  Handle failures gracefully, by retrying failed jobs and providing detailed information about the status of each job.



## Implementation

We'll start by setting up the infrastructure needed to queue and process embedding generation requests. Then we'll create an example table with triggers to enqueue these embedding requests whenever content is inserted or updated.


### Step 1: Enable extensions

First, let's enable the required extensions:

<Tabs scrollable size="small" type="underlined" defaultActiveId="sql" queryGroup="database-method">
  <TabPanel id="sql" label="SQL">
    ```sql
    -- For vector operations
    create extension if not exists vector
    with
      schema extensions;

    -- For queueing and processing jobs
    -- (pgmq will create its own schema)
    create extension if not exists pgmq;

    -- For async HTTP requests
    create extension if not exists pg_net
    with
      schema extensions;

    -- For scheduled processing and retries
    -- (pg_cron will create its own schema)
    create extension if not exists pg_cron;

    -- For clearing embeddings during updates
    create extension if not exists hstore
    with
      schema extensions;
    ```

    Even though the SQL code is `create extension`, this is the equivalent of "enabling the extension".
    To disable an extension, call `drop extension`.
  </TabPanel>

  <TabPanel id="dashboard" label="Dashboard">
    1.  Go to the [Extensions](/dashboard/project/_/database/extensions) page in the Dashboard.
    2.  Search for and enable the following extensions:
        *   `vector`
        *   `pgmq`
        *   `pg_net`
        *   `pg_cron`
        *   `hstore`
  </TabPanel>
</Tabs>


### Step 2: Create utility functions

Before we set up our embedding logic, we need to create some utility functions:

```sql
-- Schema for utility functions
create schema util;

-- Utility function to get the Supabase project URL (required for Edge Functions)
create function util.project_url()
returns text
language plpgsql
security definer
as $$
declare
  secret_value text;
begin
  -- Retrieve the project URL from Vault
  select decrypted_secret into secret_value from vault.decrypted_secrets where name = 'project_url';
  return secret_value;
end;
$$;

-- Generic function to invoke any Edge Function
create or replace function util.invoke_edge_function(
  name text,
  body jsonb,
  timeout_milliseconds int = 5 * 60 * 1000  -- default 5 minute timeout
)
returns void
language plpgsql
as $$
declare
  headers_raw text;
  auth_header text;
begin
  -- If we're in a PostgREST session, reuse the request headers for authorization
  headers_raw := current_setting('request.headers', true);

  -- Only try to parse if headers are present
  auth_header := case
    when headers_raw is not null then
      (headers_raw::json->>'authorization')
    else
      null
  end;

  -- Perform async HTTP request to the edge function
  perform net.http_post(
    url => util.project_url() || '/functions/v1/' || name,
    headers => jsonb_build_object(
      'Content-Type', 'application/json',
      'Authorization', auth_header
    ),
    body => body,
    timeout_milliseconds => timeout_milliseconds
  );
end;
$$;

-- Generic trigger function to clear a column on update
create or replace function util.clear_column()
returns trigger
language plpgsql as $$
declare
    clear_column text := TG_ARGV[0];
begin
    NEW := NEW #= hstore(clear_column, NULL);
    return NEW;
end;
$$;
```

Here we create:

*   A schema `util` to store utility functions.
*   A function to retrieve the Supabase project URL from [Vault](/docs/guides/database/vault). We'll add this secret next.
*   A generic function to invoke any Edge Function with a given name and request body.
*   A generic trigger function to clear a column on update. This function accepts the column name as an argument and sets it to `NULL` in the `NEW` record. We'll explain how to use this function later.

Every project has a unique API URL that is required to invoke Edge Functions. Let's go ahead and add the project URL secret to Vault depending on your environment.

When working with a local Supabase stack, add the following to your `supabase/seed.sql` file:

```sql
select
  vault.create_secret('http://api.supabase.internal:8000', 'project_url');
```

When deploying to the cloud platform, open the [SQL editor](/dashboard/project/_/sql/new) and run the following, replacing `<project-url>` with your [project's API URL](/dashboard/project/_/settings/api):

```sql
select
  vault.create_secret('<project-url>', 'project_url');
```


### Step 3: Create queue and triggers

Our goal is to automatically generate embeddings whenever content is inserted or updated within a table. We can use triggers and queues to achieve this. Our approach is to automatically queue embedding jobs whenever records are inserted or updated in a table, then process them asynchronously using a cron job. If a job fails, it will remain in the queue and be retried in the next scheduled task.

First we create a `pgmq` queue for processing embedding requests:

```sql
-- Queue for processing embedding jobs
select pgmq.create('embedding_jobs');
```

Next we create a trigger function to queue embedding jobs. We'll use this function to handle both insert and update events:

```sql
-- Generic trigger function to queue embedding jobs
create or replace function util.queue_embeddings()
returns trigger
language plpgsql
security definer
set search_path = ''
as $$
declare
  content_function text = TG_ARGV[0];
  embedding_column text = TG_ARGV[1];
begin
  perform pgmq.send(
    queue_name => 'embedding_jobs',
    msg => jsonb_build_object(
      'id', NEW.id,
      'schema', TG_TABLE_SCHEMA,
      'table', TG_TABLE_NAME,
      'contentFunction', content_function,
      'embeddingColumn', embedding_column
    )
  );
  return NEW;
end;
$$;
```

Our `util.queue_embeddings` trigger function is generic and can be used with any table and content function. It accepts two arguments:

1.  `content_function`: The name of a function that returns the text content to be embedded. The function should accept a single row as input and return text (see the `embedding_input` example).

    This allows you to customize the text input passed to the embedding model - for example, you could concatenate multiple columns together like `title` and `content` and use the result as input.

2.  `embedding_column`: The name of the destination column where the embedding will be stored.

Note that the `util.queue_embeddings` trigger function requires a `for each row` clause to work correctly. See [Usage](#usage) for an example of how to use this trigger function with your table.

Next we'll create a function to process the embedding jobs. This function will read jobs from the queue, group them into batches, and invoke the Edge Function to generate embeddings. We'll use `pg_cron` to schedule this function to run every 10 seconds.

```sql
-- Function to process embedding jobs from the queue
create or replace function util.process_embeddings(
  batch_size int = 10,
  max_requests int = 10,
  timeout_milliseconds int = 5 * 60 * 1000 -- default 5 minute timeout
)
returns void
language plpgsql
as $$
declare
  job_batches jsonb[];
  batch jsonb;
begin
  with
    -- First get jobs and assign batch numbers
    numbered_jobs as (
      select
        message || jsonb_build_object('jobId', msg_id) as job_info,
        (row_number() over (order by 1) - 1) / batch_size as batch_num
      from pgmq.read(
        queue_name => 'embedding_jobs',
        vt => timeout_milliseconds / 1000,
        qty => max_requests * batch_size
      )
    ),
    -- Then group jobs into batches
    batched_jobs as (
      select
        jsonb_agg(job_info) as batch_array,
        batch_num
      from numbered_jobs
      group by batch_num
    )
  -- Finally aggregate all batches into array
  select array_agg(batch_array)
  from batched_jobs
  into job_batches;

  -- Invoke the embed edge function for each batch
  foreach batch in array job_batches loop
    perform util.invoke_edge_function(
      name => 'embed',
      body => batch,
      timeout_milliseconds => timeout_milliseconds
    );
  end loop;
end;
$$;

-- Schedule the embedding processing
select
  cron.schedule(
    'process-embeddings',
    '10 seconds',
    $$
    select util.process_embeddings();
    $$
  );
```

Let's discuss some common questions about this approach:


#### Why not generate all embeddings in a single Edge Function request?

While this is possible, it can lead to long processing times and potential timeouts. Batching allows us to process multiple embeddings concurrently and handle failures more effectively.


#### Why not one request per row?

This approach can lead to API rate limiting and performance issues. Batching provides a balance between efficiency and reliability.


#### Why queue requests instead of processing them immediately?

Queuing allows us to handle failures gracefully, retry requests, and manage concurrency more effectively. Specifically we are using `pgmq`'s visibility timeouts to ensure that failed requests are retried.


#### How do visibility timeouts work?

Every time we read a message from the queue, we set a visibility timeout which tells `pgmq` to hide the message from other readers for a certain period. If the Edge Function fails to process the message within this period, the message becomes visible again and will be retried by the next scheduled task.


#### How do we handle retries?

We use `pg_cron` to schedule a task that reads messages from the queue and processes them. If the Edge Function fails to process a message, it becomes visible again after a timeout and can be retried by the next scheduled task.


#### Is 10 seconds a good interval for processing?

This interval is a good starting point, but you may need to adjust it based on your workload and the time it takes to generate embeddings. You can adjust the `batch_size`, `max_requests`, and `timeout_milliseconds` parameters to optimize performance.


### Step 4: Create the Edge Function

Finally we'll create the Edge Function to generate embeddings. We'll use OpenAI's API in this example, but you can replace it with any other embedding generation service.

Use the Supabase CLI to create a new Edge Function:

```bash
supabase functions new embed
```

This will create a new directory `supabase/functions/embed` with an `index.ts` file. Replace the contents of this file with the following:

*supabase/functions/embed/index.ts*:

```typescript
// Setup type definitions for built-in Supabase Runtime APIs
import 'jsr:@supabase/functions-js/edge-runtime.d.ts'

// We'll use the OpenAI API to generate embeddings
import OpenAI from 'jsr:@openai/openai'

import { z } from 'npm:zod'

// We'll make a direct Postgres connection to update the document
import postgres from 'https://deno.land/x/postgresjs@v3.4.5/mod.js'

// Initialize OpenAI client
const openai = new OpenAI({
  // We'll need to manually set the `OPENAI_API_KEY` environment variable
  apiKey: Deno.env.get('OPENAI_API_KEY'),
})

// Initialize Postgres client
const sql = postgres(
  // `SUPABASE_DB_URL` is a built-in environment variable
  Deno.env.get('SUPABASE_DB_URL')!
)

const jobSchema = z.object({
  jobId: z.number(),
  id: z.number(),
  schema: z.string(),
  table: z.string(),
  contentFunction: z.string(),
  embeddingColumn: z.string(),
})

const failedJobSchema = jobSchema.extend({
  error: z.string(),
})

type Job = z.infer<typeof jobSchema>
type FailedJob = z.infer<typeof failedJobSchema>

type Row = {
  id: string
  content: unknown
}

const QUEUE_NAME = 'embedding_jobs'

// Listen for HTTP requests
Deno.serve(async (req) => {
  if (req.method !== 'POST') {
    return new Response('expected POST request', { status: 405 })
  }

  if (req.headers.get('content-type') !== 'application/json') {
    return new Response('expected json body', { status: 400 })
  }

  // Use Zod to parse and validate the request body
  const parseResult = z.array(jobSchema).safeParse(await req.json())

  if (parseResult.error) {
    return new Response(`invalid request body: ${parseResult.error.message}`, {
      status: 400,
    })
  }

  const pendingJobs = parseResult.data

  // Track jobs that completed successfully
  const completedJobs: Job[] = []

  // Track jobs that failed due to an error
  const failedJobs: FailedJob[] = []

  async function processJobs() {
    let currentJob: Job | undefined

    while ((currentJob = pendingJobs.shift()) !== undefined) {
      try {
        await processJob(currentJob)
        completedJobs.push(currentJob)
      } catch (error) {
        failedJobs.push({
          ...currentJob,
          error: error instanceof Error ? error.message : JSON.stringify(error),
        })
      }
    }
  }

  try {
    // Process jobs while listening for worker termination
    await Promise.race([processJobs(), catchUnload()])
  } catch (error) {
    // If the worker is terminating (e.g. wall clock limit reached),
    // add pending jobs to fail list with termination reason
    failedJobs.push(
      ...pendingJobs.map((job) => ({
        ...job,
        error: error instanceof Error ? error.message : JSON.stringify(error),
      }))
    )
  }

  // Log completed and failed jobs for traceability
  console.log('finished processing jobs:', {
    completedJobs: completedJobs.length,
    failedJobs: failedJobs.length,
  })

  return new Response(
    JSON.stringify({
      completedJobs,
      failedJobs,
    }),
    {
      // 200 OK response
      status: 200,

      // Custom headers to report job status
      headers: {
        'content-type': 'application/json',
        'x-completed-jobs': completedJobs.length.toString(),
        'x-failed-jobs': failedJobs.length.toString(),
      },
    }
  )
})

/**
 * Generates an embedding for the given text.
 */
async function generateEmbedding(text: string) {
  const response = await openai.embeddings.create({
    model: 'text-embedding-3-small',
    input: text,
  })
  const [data] = response.data

  if (!data) {
    throw new Error('failed to generate embedding')
  }

  return data.embedding
}

/**
 * Processes an embedding job.
 */
async function processJob(job: Job) {
  const { jobId, id, schema, table, contentFunction, embeddingColumn } = job

  // Fetch content for the schema/table/row combination
  const [row]: [Row] = await sql`
    select
      id,
      ${sql(contentFunction)}(t) as content
    from
      ${sql(schema)}.${sql(table)} t
    where
      id = ${id}
  `

  if (!row) {
    throw new Error(`row not found: ${schema}.${table}/${id}`)
  }

  if (typeof row.content !== 'string') {
    throw new Error(`invalid content - expected string: ${schema}.${table}/${id}`)
  }

  const embedding = await generateEmbedding(row.content)

  await sql`
    update
      ${sql(schema)}.${sql(table)}
    set
      ${sql(embeddingColumn)} = ${JSON.stringify(embedding)}
    where
      id = ${id}
  `

  await sql`
    select pgmq.delete(${QUEUE_NAME}, ${jobId}::bigint)
  `
}

/**
 * Returns a promise that rejects if the worker is terminating.
 */
function catchUnload() {
  return new Promise((reject) => {
    addEventListener('beforeunload', (ev: any) => {
      reject(new Error(ev.detail?.reason))
    })
  })
}
```

The Edge Function listens for incoming HTTP requests from `pg_net` and processes each embedding job. It is a generic worker that can handle embedding jobs for any table and column. It uses OpenAI's API to generate embeddings and updates the corresponding row in the database. It also deletes the job from the queue once it has been processed.

The function is designed to process multiple jobs independently. If one job fails, it will not affect the processing of other jobs. The function returns a `200 OK` response with a list of completed and failed jobs. We can use this information to diagnose failed jobs. See [Troubleshooting](#troubleshooting) for more details.

You will need to set the `OPENAI_API_KEY` environment variable to authenticate with OpenAI. When running the Edge Function locally, you can add it to a `.env` file:

*.env*:

```
OPENAI_API_KEY=your-api-key
```

When you're ready to deploy the Edge Function, set can set the environment variable using the Supabase CLI:

```shell
supabase secrets set --env-file .env
```

or

```shell
supabase secrets set OPENAI_API_KEY=<your-api-key>
```

Alternatively, you can replace the `generateEmbedding` function with your own embedding generation logic.

See [Deploy to Production](/docs/guides/functions/deploy) for more information on how to deploy the Edge Function.



## Usage

Now that the infrastructure is in place, let's go through an example of how to use this system to automatically generate embeddings for a table of documents. You can use this approach with multiple tables and customize the input for each embedding generation as needed.


### 1. Create table to store documents with embeddings

We'll set up a new `documents` table that will store our content and embeddings:

```sql
-- Table to store documents with embeddings
create table documents (
  id integer primary key generated always as identity,
  title text not null,
  content text not null,
  embedding halfvec(1536),
  created_at timestamp with time zone default now()
);

-- Index for vector search over document embeddings
create index on documents using hnsw (embedding halfvec_cosine_ops);
```

Our `documents` table stores the title and content of each document along with its vector embedding. We use a `halfvec(1536)` column to store the embeddings.

`halfvec` is a `pgvector` data type that stores float values in half precision (16 bits) to save space. Our Edge Function used OpenAI's `text-embedding-3-small` model which generates 1536-dimensional embeddings, so we use the same dimensionality here. Adjust this based on the number of dimensions your embedding model generates.

We use an [HNSW index](/docs/guides/ai/vector-indexes/hnsw-indexes) on the vector column. Note that we are choosing `halfvec_cosine_ops` as the index method, which means our future queries will need to use cosine distance (`<=>`) to find similar embeddings. Also note that HNSW indexes support a maximum of 4000 dimensions for `halfvec` vectors, so keep this in mind when choosing an embedding model. If your model generates embeddings with more than 4000 dimensions, you will need to reduce the dimensionality before indexing them. See [Matryoshka embeddings](/blog/matryoshka-embeddings) for a potential solution to shortening dimensions.

Also note that the table must have a primary key column named `id` for our triggers to work correctly with the `util.queue_embeddings` function and for our Edge Function to update the correct row.


### 2. Create triggers to enqueue embedding jobs

Now we'll set up the triggers to enqueue embedding jobs whenever content is inserted or updated:

```sql
-- Customize the input for embedding generation
-- e.g. Concatenate title and content with a markdown header
create or replace function embedding_input(doc documents)
returns text
language plpgsql
immutable
as $$
begin
  return '# ' || doc.title || E'\n\n' || doc.content;
end;
$$;

-- Trigger for insert events
create trigger embed_documents_on_insert
  after insert
  on documents
  for each row
  execute function util.queue_embeddings('embedding_input', 'embedding');

-- Trigger for update events
create trigger embed_documents_on_update
  after update of title, content -- must match the columns in embedding_input()
  on documents
  for each row
  execute function util.queue_embeddings('embedding_input', 'embedding');
```

We create 2 triggers:

1.  `embed_documents_on_insert`: Enqueues embedding jobs whenever new rows are inserted into the `documents` table.

2.  `embed_documents_on_update`: Enqueues embedding jobs whenever the `title` or `content` columns are updated in the `documents` table.

Both of these triggers use the same `util.queue_embeddings` function that will queue the embedding jobs for processing. They accept 2 arguments:

1.  `embedding_input`: The name of the function that generates the input for embedding generation. This function allows you to customize the text input passed to the embedding model (e.g. concatenating the title and content). The function should accept a single row as input and return text.

2.  `embedding`: The name of the destination column where the embedding will be stored.

Note that the update trigger only fires when the `title` or `content` columns are updated. This is to avoid unnecessary updates to the embedding column when other columns are updated. Make sure that these columns match the columns used in the `embedding_input` function.

{/* supa-mdx-lint-disable-next-line Rule001HeadingCase */}


#### (Optional) Clearing embeddings on update

Note that our trigger will enqueue new embedding jobs when content is updated, but it will not clear any existing embeddings. This means that an embedding can be temporarily out of sync with the content until the new embedding is generated and updated.

If it is more important to have *accurate* embeddings than *any* embedding, you can add another trigger to clear the existing embedding until the new one is generated:

```sql
-- Trigger to clear the embedding column on update
create trigger clear_document_embedding_on_update
  before update of title, content -- must match the columns in embedding_input()
  on documents
  for each row
  execute function util.clear_column('embedding');
```

`util.clear_column` is a generic trigger function we created earlier that can be used to clear any column in a table.

*   It accepts the column name as an argument. This column must be nullable.
*   It requires a `before` trigger with a `for each row` clause.
*   It requires the `hstore` extension we created earlier.

This example will clear the `embedding` column whenever the `title` or `content` columns are updated (note the `of title, content` clause). This ensures that the embedding is always in sync with the title and content, but it will result in temporary gaps in search results until the new embedding is generated.

We intentionally use a `before` trigger because it allows us to modify the record before it's written to disk, avoiding an extra `update` statement that would be needed with an `after` trigger.


### 3. Insert and update documents

Let's insert a new document and update its content to see the embedding generation in action:

```sql
-- Insert a new document
insert into documents (title, content)
values
  ('Understanding Vector Databases', 'Vector databases are specialized...');

-- Immediately check the embedding column
select id, embedding
from documents
where title = 'Understanding Vector Databases';
```

You should observe that the `embedding` column is initially `null` after inserting the document. This is because the embedding generation is asynchronous and will be processed by the Edge Function in the next scheduled task.

Wait up to 10 seconds for the next task to run, then check the `embedding` column again:

```sql
select id, embedding
from documents
where title = 'Understanding Vector Databases';
```

You should see the generated embedding for the document.

Next let's update the content of the document:

```sql
-- Update the content of the document
update documents
set content = 'Vector databases allow you to query...'
where title = 'Understanding Vector Databases';

-- Immediately check the embedding column
select id, embedding
from documents
where title = 'Understanding Vector Databases';
```

You should observe that the `embedding` column is reset to `null` after updating the content. This is because of the trigger we added to clear existing embeddings whenever the content is updated. The embedding will be regenerated by the Edge Function in the next scheduled task.

Wait up to 10 seconds for the next task to run, then check the `embedding` column again:

```sql
select id, embedding
from documents
where title = 'Understanding Vector Databases';
```

You should see the updated embedding for the document.

Finally we'll update the title of the document:

```sql
-- Update the title of the document
update documents
set title = 'Understanding Vector Databases with Supabase'
where title = 'Understanding Vector Databases';
```

You should observe that the `embedding` column is once again reset to `null` after updating the title. This is because the trigger we added to clear existing embeddings fires when either the `content` or `title` columns are updated. The embedding will be regenerated by the Edge Function in the next scheduled task.

Wait up to 10 seconds for the next task to run, then check the `embedding` column again:

```sql
select id, embedding
from documents
where title = 'Understanding Vector Databases with Supabase';
```

You should see the updated embedding for the document.



## Troubleshooting

The `embed` Edge Function processes a batch of embedding jobs and returns a `200 OK` response with a list of completed and failed jobs in the body. For example:

```json
{
  "completedJobs": [
    {
      "jobId": "1",
      "id": "1",
      "schema": "public",
      "table": "documents",
      "contentFunction": "embedding_input",
      "embeddingColumn": "embedding"
    }
  ],
  "failedJobs": [
    {
      "jobId": "2",
      "id": "2",
      "schema": "public",
      "table": "documents",
      "contentFunction": "embedding_input",
      "embeddingColumn": "embedding",
      "error": "error connecting to openai api"
    }
  ]
}
```

It also returns the number of completed and failed jobs in the response headers. For example:

```
x-completed-jobs: 1
x-failed-jobs: 1
```

You can also use the `x-deno-execution-id` header to trace the execution of the Edge Function within the [dashboard](/dashboard/project/_/functions) logs.

Each failed job includes an `error` field with a description of the failure. Reasons for a job failing could include:

*   An error generating the embedding via external API
*   An error connecting to the database
*   The edge function being terminated (e.g. due to a wall clock limit)
*   Any other error thrown during processing

`pg_net` stores HTTP responses in the `net._http_response` table, which can be queried to diagnose issues with the embedding generation process.

```sql
select
  *
from
  net._http_response
where
  (headers->>'x-failed-jobs')::int > 0;
```



## Conclusion

Automating embedding generation and updates in Postgres allow you to build powerful semantic search capabilities without the complexity of managing embeddings manually.

By combining Postgres features like triggers, queues, and other extensions with Supabase Edge Functions, we can create a robust system that handles embedding generation asynchronously and retries failed jobs automatically.

This system can be customized to work with any content and embedding generation service, providing a flexible and scalable solution for semantic search in Postgres.



## See also

*   [What are embeddings?](/docs/guides/ai/concepts)
*   [Semantic search](/docs/guides/ai/semantic-search)
*   [Vector indexes](/docs/guides/ai/vector-indexes)
*   [Supabase Edge Functions](/docs/guides/functions)



# Choosing your Compute Add-on

Choosing the right Compute Add-on for your vector workload.

You have two options for scaling your vector workload:

1.  Increase the size of your database. This guide will help you choose the right size for your workload.
2.  Spread your workload across multiple databases. You can find more details about this approach in [Engineering for Scale](engineering-for-scale).



## Dimensionality

The number of dimensions in your embeddings is the most important factor in choosing the right Compute Add-on. In general, the lower the dimensionality the better the performance. We've provided guidance for some of the more common embedding dimensions below. For each benchmark, we used [Vecs](https://github.com/supabase/vecs) to create a collection, upload the embeddings to a single table, and create both the `IVFFlat` and `HNSW` indexes for `inner-product` distance measure for the embedding column. We then ran a series of queries to measure the performance of different compute add-ons:



## HNSW


### 384 dimensions \[#hnsw-384-dimensions]

This benchmark uses the dbpedia-entities-openai-1M dataset containing 1,000,000 embeddings of text, regenerated for 384 dimension embeddings. Each embedding is generated using [gte-small](https://huggingface.co/Supabase/gte-small).

<Tabs scrollable size="small" type="underlined" defaultActiveId="gte384" queryGroup="benchmark">
  <TabPanel id="gte384" label="gte-small-384">
    | Compute Size | Vectors   | m  | ef\_construction | ef\_search | QPS  | Latency Mean | Latency p95 | RAM Usage  | RAM    |
    | ------------ | --------- | -- | ---------------- | ---------- | ---- | ------------ | ----------- | ---------- | ------ |
    | Micro        | 100,000   | 16 | 64               | 60         | 580  | 0.017 sec    | 0.024 sec   | 1.2 (Swap) | 1 GB   |
    | Small        | 250,000   | 24 | 64               | 60         | 440  | 0.022 sec    | 0.033 sec   | 2 GB       | 2 GB   |
    | Medium       | 500,000   | 24 | 64               | 80         | 350  | 0.028 sec    | 0.045 sec   | 4 GB       | 4 GB   |
    | Large        | 1,000,000 | 32 | 80               | 100        | 270  | 0.073 sec    | 0.108 sec   | 7 GB       | 8 GB   |
    | XL           | 1,000,000 | 32 | 80               | 100        | 525  | 0.038 sec    | 0.059 sec   | 9 GB       | 16 GB  |
    | 2XL          | 1,000,000 | 32 | 80               | 100        | 790  | 0.025 sec    | 0.037 sec   | 9 GB       | 32 GB  |
    | 4XL          | 1,000,000 | 32 | 80               | 100        | 1650 | 0.015 sec    | 0.018 sec   | 11 GB      | 64 GB  |
    | 8XL          | 1,000,000 | 32 | 80               | 100        | 2690 | 0.015 sec    | 0.016 sec   | 13 GB      | 128 GB |
    | 12XL         | 1,000,000 | 32 | 80               | 100        | 3900 | 0.014 sec    | 0.016 sec   | 13 GB      | 192 GB |
    | 16XL         | 1,000,000 | 32 | 80               | 100        | 4200 | 0.014 sec    | 0.016 sec   | 20 GB      | 256 GB |

    Accuracy was 0.99 for benchmarks.
  </TabPanel>
</Tabs>


### 960 dimensions \[#hnsw-960-dimensions]

This benchmark uses the [gist-960](http://corpus-texmex.irisa.fr/) dataset, which contains 1,000,000 embeddings of images. Each embedding is 960 dimensions.

<Tabs scrollable size="small" type="underlined" defaultActiveId="gist960" queryGroup="benchmark">
  <TabPanel id="gist960" label="gist-960">
    | Compute Size | Vectors   | m  | ef\_construction | ef\_search | QPS  | Latency Mean | Latency p95 | RAM Usage     | RAM    |
    | ------------ | --------- | -- | ---------------- | ---------- | ---- | ------------ | ----------- | ------------- | ------ |
    | Micro        | 30,000    | 16 | 64               | 65         | 430  | 0.024 sec    | 0.034 sec   | 1.2 GB (Swap) | 1 GB   |
    | Small        | 100,000   | 32 | 80               | 60         | 260  | 0.040 sec    | 0.054 sec   | 2.2 GB (Swap) | 2 GB   |
    | Medium       | 250,000   | 32 | 80               | 90         | 120  | 0.083 sec    | 0.106 sec   | 4 GB          | 4 GB   |
    | Large        | 500,000   | 32 | 80               | 120        | 160  | 0.063 sec    | 0.087 sec   | 7 GB          | 8 GB   |
    | XL           | 1,000,000 | 32 | 80               | 200        | 200  | 0.049 sec    | 0.072 sec   | 13 GB         | 16 GB  |
    | 2XL          | 1,000,000 | 32 | 80               | 200        | 340  | 0.025 sec    | 0.029 sec   | 17 GB         | 32 GB  |
    | 4XL          | 1,000,000 | 32 | 80               | 200        | 630  | 0.031 sec    | 0.050 sec   | 18 GB         | 64 GB  |
    | 8XL          | 1,000,000 | 32 | 80               | 200        | 1100 | 0.034 sec    | 0.048 sec   | 19 GB         | 128 GB |
    | 12XL         | 1,000,000 | 32 | 80               | 200        | 1420 | 0.041 sec    | 0.095 sec   | 21 GB         | 192 GB |
    | 16XL         | 1,000,000 | 32 | 80               | 200        | 1650 | 0.037 sec    | 0.081 sec   | 23 GB         | 256 GB |

    Accuracy was 0.99 for benchmarks.

    QPS can also be improved by increasing [`m` and `ef_construction`](/docs/guides/ai/going-to-prod#hnsw-understanding-efconstruction--efsearch--and-m). This will allow you to use a smaller value for `ef_search` and increase QPS.
  </TabPanel>
</Tabs>


### 1536 dimensions \[#hnsw-1536-dimensions]

This benchmark uses the [dbpedia-entities-openai-1M](https://huggingface.co/datasets/KShivendu/dbpedia-entities-openai-1M) dataset, which contains 1,000,000 embeddings of text. And 224,482 embeddings from [Wikipedia articles](https://huggingface.co/datasets/Supabase/wikipedia-en-embeddings) for compute add-ons `large` and below. Each embedding is 1536 dimensions created with the [OpenAI Embeddings API](https://platform.openai.com/docs/guides/embeddings).

<Tabs scrollable size="small" type="underlined" defaultActiveId="openai1536" queryGroup="benchmark">
  <TabPanel id="openai1536" label="OpenAI-1536">
    | Compute Size | Vectors   | m  | ef\_construction | ef\_search | QPS  | Latency Mean | Latency p95 | RAM Usage     | RAM    |
    | ------------ | --------- | -- | ---------------- | ---------- | ---- | ------------ | ----------- | ------------- | ------ |
    | Micro        | 15,000    | 16 | 40               | 40         | 480  | 0.011 sec    | 0.016 sec   | 1.2 GB (Swap) | 1 GB   |
    | Small        | 50,000    | 32 | 64               | 100        | 175  | 0.031 sec    | 0.051 sec   | 2.2 GB (Swap) | 2 GB   |
    | Medium       | 100,000   | 32 | 64               | 100        | 240  | 0.083 sec    | 0.126 sec   | 4 GB          | 4 GB   |
    | Large        | 224,482   | 32 | 64               | 100        | 280  | 0.017 sec    | 0.028 sec   | 8 GB          | 8 GB   |
    | XL           | 500,000   | 24 | 56               | 100        | 360  | 0.055 sec    | 0.135 sec   | 13 GB         | 16 GB  |
    | 2XL          | 1,000,000 | 24 | 56               | 250        | 560  | 0.036 sec    | 0.058 sec   | 32 GB         | 32 GB  |
    | 4XL          | 1,000,000 | 24 | 56               | 250        | 950  | 0.021 sec    | 0.033 sec   | 39 GB         | 64 GB  |
    | 8XL          | 1,000,000 | 24 | 56               | 250        | 1650 | 0.016 sec    | 0.023 sec   | 40 GB         | 128 GB |
    | 12XL         | 1,000,000 | 24 | 56               | 250        | 1900 | 0.015 sec    | 0.021 sec   | 38 GB         | 192 GB |
    | 16XL         | 1,000,000 | 24 | 56               | 250        | 2200 | 0.015 sec    | 0.020 sec   | 40 GB         | 256 GB |

    Accuracy was 0.99 for benchmarks.

    QPS can also be improved by increasing [`m` and `ef_construction`](/docs/guides/ai/going-to-prod#hnsw-understanding-efconstruction--efsearch--and-m). This will allow you to use a smaller value for `ef_search` and increase QPS. For example, increasing `m` to 32 and `ef_construction` to 80 for 4XL will increase QPS to 1280.
  </TabPanel>
</Tabs>

<Admonition type="note">
  It is possible to upload more vectors to a single table if Memory allows it (for example, 4XL plan and higher for OpenAI embeddings). But it will affect the performance of the queries: QPS will be lower, and latency will be higher. Scaling should be almost linear, but it is recommended to benchmark your workload to find the optimal number of vectors per table and per database instance.
</Admonition>

<Image
  alt="multi database"
  src={{
    light: '/docs/img/ai/instance-type/hnsw-dims--light.png',
    dark: '/docs/img/ai/instance-type/hnsw-dims--dark.png',
  }}
  zoomable
/>



## IVFFlat


### 384 dimensions \[#ivfflat-384-dimensions]

This benchmark uses the dbpedia-entities-openai-1M dataset containing 1,000,000 embeddings of text, regenerated for 384 dimension embeddings. Each embedding is generated using [gte-small](https://huggingface.co/Supabase/gte-small).

<Tabs scrollable size="small" type="underlined" defaultActiveId="gte384_98" queryGroup="benchmark">
  <TabPanel id="gte384_98" label="gte-small-384, accuracy=.98">
    | Compute Size | Vectors   | Lists | Probes | QPS  | Latency Mean | Latency p95 | RAM Usage     | RAM    |
    | ------------ | --------- | ----- | ------ | ---- | ------------ | ----------- | ------------- | ------ |
    | Micro        | 100,000   | 500   | 50     | 205  | 0.048 sec    | 0.066 sec   | 1.2 GB (Swap) | 1 GB   |
    | Small        | 250,000   | 1000  | 60     | 160  | 0.062 sec    | 0.079 sec   | 2 GB          | 2 GB   |
    | Medium       | 500,000   | 2000  | 80     | 120  | 0.082 sec    | 0.104 sec   | 3.2 GB        | 4 GB   |
    | Large        | 1,000,000 | 5000  | 150    | 75   | 0.269 sec    | 0.375 sec   | 6.5 GB        | 8 GB   |
    | XL           | 1,000,000 | 5000  | 150    | 150  | 0.131 sec    | 0.178 sec   | 9 GB          | 16 GB  |
    | 2XL          | 1,000,000 | 5000  | 150    | 300  | 0.066 sec    | 0.099 sec   | 10 GB         | 32 GB  |
    | 4XL          | 1,000,000 | 5000  | 150    | 570  | 0.035 sec    | 0.046 sec   | 10 GB         | 64 GB  |
    | 8XL          | 1,000,000 | 5000  | 150    | 1400 | 0.023 sec    | 0.028 sec   | 12 GB         | 128 GB |
    | 12XL         | 1,000,000 | 5000  | 150    | 1550 | 0.030 sec    | 0.039 sec   | 12 GB         | 192 GB |
    | 16XL         | 1,000,000 | 5000  | 150    | 1800 | 0.030 sec    | 0.039 sec   | 16 GB         | 256 GB |
  </TabPanel>

  <TabPanel id="gte384_99" label="gte-small-384, accuracy=.99">
    | Compute Size | Vectors   | Lists | Probes | QPS  | Latency Mean | Latency p95 | RAM Usage     | RAM    |
    | ------------ | --------- | ----- | ------ | ---- | ------------ | ----------- | ------------- | ------ |
    | Micro        | 100,000   | 500   | 70     | 160  | 0.062 sec    | 0.079 sec   | 1.2 GB (Swap) | 1 GB   |
    | Small        | 250,000   | 1000  | 100    | 100  | 0.096 sec    | 0.113 sec   | 2 GB          | 2 GB   |
    | Medium       | 500,000   | 2000  | 120    | 85   | 0.117 sec    | 0.147 sec   | 3.2 GB        | 4 GB   |
    | Large        | 1,000,000 | 5000  | 250    | 50   | 0.394 sec    | 0.521 sec   | 6.5 GB        | 8 GB   |
    | XL           | 1,000,000 | 5000  | 250    | 100  | 0.197 sec    | 0.255 sec   | 10 GB         | 16 GB  |
    | 2XL          | 1,000,000 | 5000  | 250    | 200  | 0.098 sec    | 0.140 sec   | 10 GB         | 32 GB  |
    | 4XL          | 1,000,000 | 5000  | 250    | 390  | 0.051 sec    | 0.066 sec   | 11 GB         | 64 GB  |
    | 8XL          | 1,000,000 | 5000  | 250    | 850  | 0.036 sec    | 0.042 sec   | 12 GB         | 128 GB |
    | 12XL         | 1,000,000 | 5000  | 250    | 1000 | 0.043 sec    | 0.055 sec   | 13 GB         | 192 GB |
    | 16XL         | 1,000,000 | 5000  | 250    | 1200 | 0.043 sec    | 0.055 sec   | 16 GB         | 256 GB |
  </TabPanel>
</Tabs>


### 960 dimensions \[#ivfflat-960-dimensions]

This benchmark uses the [gist-960](http://corpus-texmex.irisa.fr/) dataset, which contains 1,000,000 embeddings of images. Each embedding is 960 dimensions.

<Tabs scrollable size="small" type="underlined" defaultActiveId="gist960" queryGroup="benchmark">
  <TabPanel id="gist960" label="gist-960, probes = 10">
    | Compute Size | Vectors   | Lists | QPS  | Latency Mean | Latency p95 | RAM Usage     | RAM    |
    | ------------ | --------- | ----- | ---- | ------------ | ----------- | ------------- | ------ |
    | Micro        | 30,000    | 30    | 75   | 0.065 sec    | 0.088 sec   | 1.1 GB (Swap) | 1 GB   |
    | Small        | 100,000   | 100   | 78   | 0.064 sec    | 0.092 sec   | 1.8 GB        | 2 GB   |
    | Medium       | 250,000   | 250   | 58   | 0.085 sec    | 0.129 sec   | 3.2 GB        | 4 GB   |
    | Large        | 500,000   | 500   | 55   | 0.088 sec    | 0.140 sec   | 5 GB          | 8 GB   |
    | XL           | 1,000,000 | 1000  | 110  | 0.046 sec    | 0.070 sec   | 14 GB         | 16 GB  |
    | 2XL          | 1,000,000 | 1000  | 235  | 0.083 sec    | 0.136 sec   | 10 GB         | 32 GB  |
    | 4XL          | 1,000,000 | 1000  | 420  | 0.071 sec    | 0.106 sec   | 11 GB         | 64 GB  |
    | 8XL          | 1,000,000 | 1000  | 815  | 0.072 sec    | 0.106 sec   | 13 GB         | 128 GB |
    | 12XL         | 1,000,000 | 1000  | 1150 | 0.052 sec    | 0.078 sec   | 15.5 GB       | 192 GB |
    | 16XL         | 1,000,000 | 1000  | 1345 | 0.072 sec    | 0.106 sec   | 17.5 GB       | 256 GB |
  </TabPanel>
</Tabs>


### 1536 dimensions \[#ivfflat-1536-dimensions]

This benchmark uses the [dbpedia-entities-openai-1M](https://huggingface.co/datasets/KShivendu/dbpedia-entities-openai-1M) dataset, which contains 1,000,000 embeddings of text. Each embedding is 1536 dimensions created with the [OpenAI Embeddings API](https://platform.openai.com/docs/guides/embeddings).

<Tabs scrollable size="small" type="underlined" defaultActiveId="dbpedia1536" queryGroup="benchmark">
  <TabPanel id="dbpedia1536" label="OpenAI-1536, probes = 10">
    | Compute Size | Vectors   | Lists | QPS  | Latency Mean | Latency p95 | RAM Usage     | RAM    |
    | ------------ | --------- | ----- | ---- | ------------ | ----------- | ------------- | ------ |
    | Micro        | 20,000    | 40    | 135  | 0.372 sec    | 0.412 sec   | 1.2 GB (Swap) | 1 GB   |
    | Small        | 50,000    | 100   | 140  | 0.357 sec    | 0.398 sec   | 1.8 GB        | 2 GB   |
    | Medium       | 100,000   | 200   | 130  | 0.383 sec    | 0.446 sec   | 3.7 GB        | 4 GB   |
    | Large        | 250,000   | 500   | 130  | 0.378 sec    | 0.434 sec   | 7 GB          | 8 GB   |
    | XL           | 500,000   | 1000  | 235  | 0.213 sec    | 0.271 sec   | 13.5 GB       | 16 GB  |
    | 2XL          | 1,000,000 | 2000  | 380  | 0.133 sec    | 0.236 sec   | 30 GB         | 32 GB  |
    | 4XL          | 1,000,000 | 2000  | 720  | 0.068 sec    | 0.120 sec   | 35 GB         | 64 GB  |
    | 8XL          | 1,000,000 | 2000  | 1250 | 0.039 sec    | 0.066 sec   | 38 GB         | 128 GB |
    | 12XL         | 1,000,000 | 2000  | 1600 | 0.030 sec    | 0.052 sec   | 41 GB         | 192 GB |
    | 16XL         | 1,000,000 | 2000  | 1790 | 0.029 sec    | 0.051 sec   | 45 GB         | 256 GB |

    For 1,000,000 vectors 10 probes results to accuracy of 0.91. And for 500,000 vectors and below 10 probes results to accuracy in the range of 0.95 - 0.99. To increase accuracy, you need to increase the number of probes.
  </TabPanel>

  <TabPanel id="dbpedia1536_40" label="OpenAI-1536, probes = 40">
    | Compute Size | Vectors   | Lists | QPS | Latency Mean | Latency p95 | RAM Usage | RAM    |
    | ------------ | --------- | ----- | --- | ------------ | ----------- | --------- | ------ |
    | Micro        | 20,000    | 40    | -   | -            | -           | -         | 1 GB   |
    | Small        | 50,000    | 100   | -   | -            | -           | -         | 2 GB   |
    | Medium       | 100,000   | 200   | -   | -            | -           | -         | 4 GB   |
    | Large        | 250,000   | 500   | -   | -            | -           | -         | 8 GB   |
    | XL           | 500,000   | 1000  | -   | -            | -           | -         | 16 GB  |
    | 2XL          | 1,000,000 | 2000  | 140 | 0.358 sec    | 0.575 sec   | 30 GB     | 32 GB  |
    | 4XL          | 1,000,000 | 2000  | 270 | 0.186 sec    | 0.304 sec   | 35 GB     | 64 GB  |
    | 8XL          | 1,000,000 | 2000  | 470 | 0.104 sec    | 0.166 sec   | 38 GB     | 128 GB |
    | 12XL         | 1,000,000 | 2000  | 600 | 0.085 sec    | 0.132 sec   | 41 GB     | 192 GB |
    | 16XL         | 1,000,000 | 2000  | 670 | 0.081 sec    | 0.129 sec   | 45 GB     | 256 GB |

    For 1,000,000 vectors 40 probes results to accuracy of 0.98. Note that exact values may vary depending on the dataset and queries, we recommend to run benchmarks with your own data to get precise results. Use this table as a reference.
  </TabPanel>
</Tabs>

<Image
  alt="multi database"
  src={{
    light: '/docs/img/ai/going-prod/size-to-rps--light.png',
    dark: '/docs/img/ai/going-prod/size-to-rps--dark.png',
  }}
  zoomable
/>

<Admonition type="note">
  It is possible to upload more vectors to a single table if Memory allows it (for example, 4XL plan and higher for OpenAI embeddings). But it will affect the performance of the queries: QPS will be lower, and latency will be higher. Scaling should be almost linear, but it is recommended to benchmark your workload to find the optimal number of vectors per table and per database instance.
</Admonition>



## Performance tips

There are various ways to improve your pgvector performance. Here are some tips:


### Pre-warming your database

It's useful to execute a few thousand “warm-up” queries before going into production. This helps help with RAM utilization. This can also help to determine that you've selected the right compute size for your workload.


### Fine-tune index parameters

You can increase the Requests per Second by increasing `m` and `ef_construction` or `lists`. This also has an important caveat: building the index takes longer with higher values for these parameters.

<Tabs scrollable size="small" type="underlined" defaultActiveId="hnsw" queryGroup="index-type">
  <TabPanel id="hnsw" label="HNSW">
    <Image
      alt="multi database"
      src={{
    light: '/docs/img/ai/going-prod/dbpedia-hnsw-build-parameters--light.png',
    dark: '/docs/img/ai/going-prod/dbpedia-hnsw-build-parameters--dark.png',
  }}
      zoomable
    />
  </TabPanel>

  <TabPanel id="ivfflat" label="IVFFlat">
    <Image
      alt="multi database"
      src={{
    light: '/docs/img/ai/instance-type/lists-for-1m--light.png',
    dark: '/docs/img/ai/instance-type/lists-for-1m--dark.png',
  }}
      zoomable
    />
  </TabPanel>
</Tabs>

Check out more tips and the complete step-by-step guide in [Going to Production for AI applications](going-to-prod).



## Benchmark methodology

We follow techniques outlined in the [ANN Benchmarks](https://github.com/erikbern/ann-benchmarks) methodology. A Python test runner is responsible for uploading the data, creating the index, and running the queries. The pgvector engine is implemented using [vecs](https://github.com/supabase/vecs), a Python client for pgvector.

<Image
  alt="multi database"
  src={{
    light: '/docs/img/ai/instance-type/vecs-benchmark--light.png',
    dark: '/docs/img/ai/instance-type/vecs-benchmark--dark.png',
  }}
  className="max-h-[650px]"
  zoomable
/>

Each test is run for a minimum of 30-40 minutes. They include a series of experiments executed at different concurrency levels to measure the engine's performance under different load types. The results are then averaged.

As a general recommendation, we suggest using a concurrency level of 5 or more for most workloads and 30 or more for high-load workloads.



---
**Navigation:** [← Previous](./38-supabase-auth-with-the-nextjs-app-router.md) | [Index](./index.md) | [Next →](./40-concepts.md)
