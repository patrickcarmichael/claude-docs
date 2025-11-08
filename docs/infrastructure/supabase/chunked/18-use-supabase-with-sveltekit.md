**Navigation:** [← Previous](./17-build-a-user-management-app-with-vue-3.md) | [Index](./index.md) | [Next →](./19-type-safe-sql-with-kysely.md)

# Use Supabase with SvelteKit

Learn how to create a Supabase project, add some sample data to your database, and query the data from a SvelteKit app.

<StepHikeCompact>
  <StepHikeCompact.Step step={1}>
    <StepHikeCompact.Details title="Create a Supabase project">
      Go to [database.new](https://database.new) and create a new Supabase project.

      Alternatively, you can create a project using the Management API:

      ```bash
      # First, get your access token from https://supabase.com/dashboard/account/tokens
      export SUPABASE_ACCESS_TOKEN="your-access-token"

      # List your organizations to get the organization ID
      curl -H "Authorization: Bearer $SUPABASE_ACCESS_TOKEN" \
        https://api.supabase.com/v1/organizations

      # Create a new project (replace <org-id> with your organization ID)
      curl -X POST https://api.supabase.com/v1/projects \
        -H "Authorization: Bearer $SUPABASE_ACCESS_TOKEN" \
        -H "Content-Type: application/json" \
        -d '{
          "organization_id": "<org-id>",
          "name": "My Project",
          "region": "us-east-1",
          "db_pass": "<your-secure-password>"
        }'
      ```

      When your project is up and running, go to the [Table Editor](/dashboard/project/_/editor), create a new table and insert some data.

      Alternatively, you can run the following snippet in your project's [SQL Editor](/dashboard/project/_/sql/new). This will create a `instruments` table with some sample data.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      ```sql SQL_EDITOR
      -- Create the table
      create table instruments (
        id bigint primary key generated always as identity,
        name text not null
      );
      -- Insert some sample data into the table
      insert into instruments (name)
      values
        ('violin'),
        ('viola'),
        ('cello');

      alter table instruments enable row level security;
      ```
    </StepHikeCompact.Code>

    <StepHikeCompact.Details>
      Make the data in your table publicly readable by adding an RLS policy:
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      ```sql SQL_EDITOR
      create policy "public can read instruments"
      on public.instruments
      for select to anon
      using (true);
      ```
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={2}>
    <StepHikeCompact.Details title="Create a SvelteKit app">
      Create a SvelteKit app using the `npm create` command.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name="Terminal">
        ```bash name=Terminal
        npx sv create my-app
        ```
      </NamedCodeBlock>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={3}>
    <StepHikeCompact.Details title="Install the Supabase client library">
      The fastest way to get started is to use the `supabase-js` client library which provides a convenient interface for working with Supabase from a SvelteKit app.

      Navigate to the SvelteKit app and install `supabase-js`.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name="Terminal">
        ```bash name=Terminal
        cd my-app && npm install @supabase/supabase-js
        ```
      </NamedCodeBlock>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={4}>
    <StepHikeCompact.Details title="Declare Supabase Environment Variables">
      Create a `.env` file at the root of your project and populate with your Supabase connection variables:

      <ProjectConfigVariables variable="url" />

      <ProjectConfigVariables variable="publishable" />

      <ProjectConfigVariables variable="anon" />
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
        <TabPanel id=".env" label=".env">
          ```text name=.env
          PUBLIC_SUPABASE_URL=<SUBSTITUTE_SUPABASE_URL>
          PUBLIC_SUPABASE_PUBLISHABLE_KEY=<SUBSTITUTE_SUPABASE_PUBLISHABLE_KEY>
          ```
        </TabPanel>
      </Tabs>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={5}>
    <StepHikeCompact.Details title="Create the Supabase client">
      Create a `src/lib` directory in your SvelteKit app, create a file called `supabaseClient.js` and add the following code to initialize the Supabase client:
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
        <TabPanel id="src/lib/supabaseClient.js" label="src/lib/supabaseClient.js">
          ```js name=src/lib/supabaseClient.js
          import { createClient } from '@supabase/supabase-js';
          import { PUBLIC_SUPABASE_URL, PUBLIC_SUPABASE_PUBLISHABLE_KEY } from '$env/static/public';

          export const supabase = createClient(PUBLIC_SUPABASE_URL, PUBLIC_SUPABASE_PUBLISHABLE_KEY)
          ```
        </TabPanel>

        <TabPanel id="src/lib/supabaseClient.ts" label="src/lib/supabaseClient.ts">
          ```ts name=src/lib/supabaseClient.ts
          import { createClient } from '@supabase/supabase-js';
          import { PUBLIC_SUPABASE_URL, PUBLIC_SUPABASE_PUBLISHABLE_KEY } from '$env/static/public';

          export const supabase = createClient(PUBLIC_SUPABASE_URL, PUBLIC_SUPABASE_PUBLISHABLE_KEY)
          ```
        </TabPanel>
      </Tabs>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={6}>
    <StepHikeCompact.Details title="Query data from the app">
      Use `load` method to fetch the data server-side and display the query results as a simple list.

      Create `+page.server.js` file in the `src/routes` directory with the following code.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
        <TabPanel id="src/routes/+page.server.js" label="src/routes/+page.server.js">
          ```js name=src/routes/+page.server.js
            import { supabase } from "$lib/supabaseClient";

            export async function load() {
              const { data } = await supabase.from("instruments").select();
              return {
                instruments: data ?? [],
              };
            }
          ```
        </TabPanel>

        <TabPanel id="src/routes/+page.server.ts" label="src/routes/+page.server.ts">
          ```ts name=src/routes/+page.server.ts
          import type { PageServerLoad } from './$types';
          import { supabase } from '$lib/supabaseClient';

          type Instrument = {
            id: number;
            name: string;
          };

          export const load: PageServerLoad = async () => {
            const { data, error } = await supabase.from('instruments').select<'instruments', Instrument>();

            if (error) {
              console.error('Error loading instruments:', error.message);
              return { instruments: [] };
            }

            return {
              instruments: data ?? [],
            };
          };
          ```
        </TabPanel>
      </Tabs>
    </StepHikeCompact.Code>

    <StepHikeCompact.Details title="">
      Replace the existing content in your `+page.svelte` file in the `src/routes` directory with the following code.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name="src/routes/+page.svelte">
        ```svelte name=src/routes/+page.svelte
          <script>
            let { data } = $props();
          </script>

          <ul>
            {#each data.instruments as instrument}
              <li>{instrument.name}</li>
            {/each}
          </ul>
        ```
      </NamedCodeBlock>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={7}>
    <StepHikeCompact.Details title="Start the app">
      Start the app and go to [http://localhost:5173](http://localhost:5173) in a browser and you should see the list of instruments.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name="Terminal">
        ```bash name=Terminal
        npm run dev
        ```
      </NamedCodeBlock>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>
</StepHikeCompact>



## Next steps

*   Set up [Auth](/docs/guides/auth) for your app
*   [Insert more data](/docs/guides/database/import-data) into your database
*   Upload and serve static files using [Storage](/docs/guides/storage)



# Use Supabase with Vue

Learn how to create a Supabase project, add some sample data to your database, and query the data from a Vue app.

<StepHikeCompact>
  <StepHikeCompact.Step step={1}>
    <StepHikeCompact.Details title="Create a Supabase project">
      Go to [database.new](https://database.new) and create a new Supabase project.

      Alternatively, you can create a project using the Management API:

      ```bash
      # First, get your access token from https://supabase.com/dashboard/account/tokens
      export SUPABASE_ACCESS_TOKEN="your-access-token"

      # List your organizations to get the organization ID
      curl -H "Authorization: Bearer $SUPABASE_ACCESS_TOKEN" \
        https://api.supabase.com/v1/organizations

      # Create a new project (replace <org-id> with your organization ID)
      curl -X POST https://api.supabase.com/v1/projects \
        -H "Authorization: Bearer $SUPABASE_ACCESS_TOKEN" \
        -H "Content-Type: application/json" \
        -d '{
          "organization_id": "<org-id>",
          "name": "My Project",
          "region": "us-east-1",
          "db_pass": "<your-secure-password>"
        }'
      ```

      When your project is up and running, go to the [Table Editor](/dashboard/project/_/editor), create a new table and insert some data.

      Alternatively, you can run the following snippet in your project's [SQL Editor](/dashboard/project/_/sql/new). This will create a `instruments` table with some sample data.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      ```sql SQL_EDITOR
      -- Create the table
      create table instruments (
        id bigint primary key generated always as identity,
        name text not null
      );
      -- Insert some sample data into the table
      insert into instruments (name)
      values
        ('violin'),
        ('viola'),
        ('cello');

      alter table instruments enable row level security;
      ```
    </StepHikeCompact.Code>

    <StepHikeCompact.Details>
      Make the data in your table publicly readable by adding an RLS policy:
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      ```sql SQL_EDITOR
      create policy "public can read instruments"
      on public.instruments
      for select to anon
      using (true);
      ```
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={2}>
    <StepHikeCompact.Details title="Create a Vue app">
      Create a Vue app using the `npm init` command.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name="Terminal">
        ```sh name=Terminal
        npm init vue@latest my-app
        ```
      </NamedCodeBlock>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={3}>
    <StepHikeCompact.Details title="Install the Supabase client library">
      The fastest way to get started is to use the `supabase-js` client library which provides a convenient interface for working with Supabase from a Vue app.

      Navigate to the Vue app and install `supabase-js`.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name="Terminal">
        ```bash name=Terminal
        cd my-app && npm install @supabase/supabase-js
        ```
      </NamedCodeBlock>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={4}>
    <StepHikeCompact.Details title="Declare Supabase Environment Variables">
      Create a `.env.local` file and populate with your Supabase connection variables:

      <ProjectConfigVariables variable="url" />

      <ProjectConfigVariables variable="publishable" />

      <ProjectConfigVariables variable="anon" />
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
        <TabPanel id=".env.local" label=".env.local">
          ```text name=.env.local
          VITE_SUPABASE_URL=<SUBSTITUTE_SUPABASE_URL>
          VITE_SUPABASE_PUBLISHABLE_KEY=<SUBSTITUTE_SUPABASE_PUBLISHABLE_KEY>
          ```
        </TabPanel>
      </Tabs>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={5}>
    <StepHikeCompact.Details title="Create the Supabase client">
      Create a `/src/lib` directory in your Vue app, create a file called `supabaseClient.js` and add the following code to initialize the Supabase client:
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name="src/lib/supabaseClient.js">
        ```js name=src/lib/supabaseClient.js
        import { createClient } from '@supabase/supabase-js'

        const supabaseUrl = import.meta.env.VITE_SUPABASE_URL
        const supabasePublishableKey = import.meta.env.VITE_SUPABASE_PUBLISHABLE_KEY

        export const supabase = createClient(supabaseUrl, supabasePublishableKey)
        ```
      </NamedCodeBlock>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={6}>
    <StepHikeCompact.Details title="Query data from the app">
      Replace the existing content in your `App.vue` file with the following code.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name="src/App.vue">
        ```vue name=src/App.vue
        <script setup>
        import { ref, onMounted } from 'vue'
        import { supabase } from './lib/supabaseClient'

        const instruments = ref([])

        async function getInstruments() {
          const { data } = await supabase.from('instruments').select()
          instruments.value = data
        }

        onMounted(() => {
           getInstruments()
        })
        </script>

        <template>
          <ul>
            <li v-for="instrument in instruments" :key="instrument.id">{{ instrument.name }}</li>
          </ul>
        </template>
        ```
      </NamedCodeBlock>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={7}>
    <StepHikeCompact.Details title="Start the app">
      Start the app and go to [http://localhost:5173](http://localhost:5173) in a browser and you should see the list of instruments.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name="Terminal">
        ```bash name=Terminal
        npm run dev
        ```
      </NamedCodeBlock>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>
</StepHikeCompact>



# Running AI Models

Run AI models in Edge Functions using the built-in Supabase AI API.

Edge Functions have a built-in API for running AI models. You can use this API to generate embeddings, build conversational workflows, and do other AI related tasks in your Edge Functions.

This allows you to:

*   Generate text embeddings without external dependencies
*   Run Large Language Models via Ollama or Llamafile
*   Build conversational AI workflows

***



## Setup

There are no external dependencies or packages to install to enable the API.

Create a new inference session:

```ts
const model = new Supabase.ai.Session('model-name')
```

<Admonition type="tip">
  To get type hints and checks for the API, import types from `functions-js`:

  ```ts
  import 'jsr:@supabase/functions-js/edge-runtime.d.ts'
  ```
</Admonition>


### Running a model inference

Once the session is instantiated, you can call it with inputs to perform inferences:

```ts
// For embeddings (gte-small model)
const embeddings = await model.run('Hello world', {
  mean_pool: true,
  normalize: true,
})

// For text generation (non-streaming)
const response = await model.run('Write a haiku about coding', {
  stream: false,
  timeout: 30,
})

// For streaming responses
const stream = await model.run('Tell me a story', {
  stream: true,
  mode: 'ollama',
})
```

***



## Generate text embeddings

Generate text embeddings using the built-in [`gte-small`](https://huggingface.co/Supabase/gte-small) model:

<Admonition type="note">
  `gte-small` model exclusively caters to English texts, and any lengthy texts will be truncated to a maximum of 512 tokens. While you can provide inputs longer than 512 tokens, truncation may affect the accuracy.
</Admonition>

```ts
const model = new Supabase.ai.Session('gte-small')

Deno.serve(async (req: Request) => {
  const params = new URL(req.url).searchParams
  const input = params.get('input')
  const output = await model.run(input, { mean_pool: true, normalize: true })
  return new Response(JSON.stringify(output), {
    headers: {
      'Content-Type': 'application/json',
      Connection: 'keep-alive',
    },
  })
})
```

***



## Using Large Language Models (LLM)

Inference via larger models is supported via [Ollama](https://ollama.com/) and [Mozilla Llamafile](https://github.com/Mozilla-Ocho/llamafile). In the first iteration, you can use it with a self-managed Ollama or [Llamafile server](https://www.docker.com/blog/a-quick-guide-to-containerizing-llamafile-with-docker-for-ai-applications/).

<Admonition type="note">
  We are progressively rolling out support for the hosted solution. To sign up for early access, fill out [this form](https://forms.supabase.com/supabase.ai-llm-early-access).
</Admonition>

<video width="99%" muted playsInline controls={true}>
  <source src="https://xguihxuzqibwxjnimxev.supabase.co/storage/v1/object/public/videos/docs/guides/edge-functions-inference-2.mp4" type="video/mp4" />
</video>

***



## Running locally

<Tabs scrollable size="large" type="underlined" defaultActiveId="ollama" queryGroup="platform">
  <TabPanel id="ollama" label="Ollama">
    <StepHikeCompact>
      <StepHikeCompact.Step step={1} fullWidth>
        <StepHikeCompact.Details title="Install Ollama" fullWidth>
          [Install Ollama](https://github.com/ollama/ollama?tab=readme-ov-file#ollama) and pull the Mistral model

          ```bash
          ollama pull mistral
          ```
        </StepHikeCompact.Details>
      </StepHikeCompact.Step>

      <StepHikeCompact.Step step={2} fullWidth>
        <StepHikeCompact.Details title="Run the Ollama server" fullWidth>
          ```bash
          ollama serve
          ```
        </StepHikeCompact.Details>
      </StepHikeCompact.Step>

      <StepHikeCompact.Step step={3} fullWidth>
        <StepHikeCompact.Details title="Set the function secret" fullWidth>
          Set a function secret called `AI_INFERENCE_API_HOST` to point to the Ollama server

          ```bash
          echo "AI_INFERENCE_API_HOST=http://host.docker.internal:11434" >> supabase/functions/.env
          ```
        </StepHikeCompact.Details>
      </StepHikeCompact.Step>

      <StepHikeCompact.Step step={4} fullWidth>
        <StepHikeCompact.Details title="Create a new function" fullWidth>
          ```bash
          supabase functions new ollama-test
          ```

          ```ts supabase/functions/ollama-test/index.ts
          import 'jsr:@supabase/functions-js/edge-runtime.d.ts'
          const session = new Supabase.ai.Session('mistral')

          Deno.serve(async (req: Request) => {
            const params = new URL(req.url).searchParams
            const prompt = params.get('prompt') ?? ''

            // Get the output as a stream
            const output = await session.run(prompt, { stream: true })

            const headers = new Headers({
              'Content-Type': 'text/event-stream',
              Connection: 'keep-alive',
            })

            // Create a stream
            const stream = new ReadableStream({
              async start(controller) {
                const encoder = new TextEncoder()

                try {
                  for await (const chunk of output) {
                    controller.enqueue(encoder.encode(chunk.response ?? ''))
                  }
                } catch (err) {
                  console.error('Stream error:', err)
                } finally {
                  controller.close()
                }
              },
            })

            // Return the stream to the user
            return new Response(stream, {
              headers,
            })
          })
          ```
        </StepHikeCompact.Details>
      </StepHikeCompact.Step>

      <StepHikeCompact.Step step={5} fullWidth>
        <StepHikeCompact.Details title="Serve the function" fullWidth>
          ```bash
          supabase functions serve --env-file supabase/functions/.env
          ```
        </StepHikeCompact.Details>
      </StepHikeCompact.Step>

      <StepHikeCompact.Step step={6} fullWidth>
        <StepHikeCompact.Details title="Execute the function" fullWidth>
          ```bash
          curl --get "http://localhost:54321/functions/v1/ollama-test" \
          --data-urlencode "prompt=write a short rap song about Supabase, the Postgres Developer platform, as sung by Nicki Minaj" \
          -H "Authorization: $ANON_KEY"
          ```
        </StepHikeCompact.Details>
      </StepHikeCompact.Step>
    </StepHikeCompact>
  </TabPanel>

  <TabPanel id="llamafile" label="Mozilla Llamafile">
    Follow the [Llamafile Quickstart](https://github.com/Mozilla-Ocho/llamafile?tab=readme-ov-file#quickstart) to download an run a Llamafile locally on your machine.

    Since Llamafile provides an OpenAI API compatible server, you can either use it with `@supabase/functions-js` or with the official OpenAI Deno SDK.

    <Tabs scrollable size="large" type="underlined" defaultActiveId="supabase-functions-js" queryGroup="sdk">
      <TabPanel id="supabase-functions-js" label="Supabase Functions JS">
        <StepHikeCompact>
          <StepHikeCompact.Step step={1} fullWidth>
            <StepHikeCompact.Details title="Set function secret" fullWidth>
              Set a function secret called `AI_INFERENCE_API_HOST` to point to the Llamafile server

              ```bash
              echo "AI_INFERENCE_API_HOST=http://host.docker.internal:8080" >> supabase/functions/.env
              ```
            </StepHikeCompact.Details>
          </StepHikeCompact.Step>

          <StepHikeCompact.Step step={2} fullWidth>
            <StepHikeCompact.Details title="Create a new function" fullWidth>
              Create a new function with the following code

              ```bash
              supabase functions new llamafile-test
              ```
            </StepHikeCompact.Details>
          </StepHikeCompact.Step>

          <StepHikeCompact.Step step={3} fullWidth>
            <StepHikeCompact.Details title="Add the function code" fullWidth>
              <Admonition type="note">
                Note that the model parameter doesn't have any effect here. The model depends on which Llamafile is currently running.
              </Admonition>

              ```ts supabase/functions/llamafile-test/index.ts
              import 'jsr:@supabase/functions-js/edge-runtime.d.ts'
              const session = new Supabase.ai.Session('LLaMA_CPP')

              Deno.serve(async (req: Request) => {
                const params = new URL(req.url).searchParams
                const prompt = params.get('prompt') ?? ''

                // Get the output as a stream
                const output = await session.run(
                  {
                    messages: [
                      {
                        role: 'system',
                        content:
                          'You are LLAMAfile, an AI assistant. Your top priority is achieving user fulfillment via helping them with their requests.',
                      },
                      {
                        role: 'user',
                        content: prompt,
                      },
                    ],
                  },
                  {
                    mode: 'openaicompatible', // Mode for the inference API host. (default: 'ollama')
                    stream: false,
                  }
                )

                console.log('done')
                return Response.json(output)
              })
              ```
            </StepHikeCompact.Details>
          </StepHikeCompact.Step>

          <StepHikeCompact.Step step={4} fullWidth>
            <StepHikeCompact.Details title="Serve the function" fullWidth>
              ```bash
              supabase functions serve --env-file supabase/functions/.env
              ```
            </StepHikeCompact.Details>
          </StepHikeCompact.Step>

          <StepHikeCompact.Step step={5} fullWidth>
            <StepHikeCompact.Details title="Execute the function" fullWidth>
              ```bash
              curl --get "http://localhost:54321/functions/v1/llamafile-test" \
              --data-urlencode "prompt=write a short rap song about Supabase, the Postgres Developer platform, as sung by Nicki Minaj" \
              -H "Authorization: $ANON_KEY"
              ```
            </StepHikeCompact.Details>
          </StepHikeCompact.Step>
        </StepHikeCompact>
      </TabPanel>

      <TabPanel id="openai" label="OpenAI Deno SDK">
        <StepHikeCompact>
          <StepHikeCompact.Step step={1} fullWidth>
            <StepHikeCompact.Details title="Set function secret" fullWidth>
              Set the following function secrets to point the OpenAI SDK to the Llamafile server

              ```bash
              echo "OPENAI_BASE_URL=http://host.docker.internal:8080/v1" >> supabase/functions/.env
              echo "OPENAI_API_KEY=sk-XXXXXXXX" >> supabase/functions/.env
              ```
            </StepHikeCompact.Details>
          </StepHikeCompact.Step>

          <StepHikeCompact.Step step={2} fullWidth>
            <StepHikeCompact.Details title="Create a new function" fullWidth>
              ```bash
              supabase functions new llamafile-test
              ```
            </StepHikeCompact.Details>
          </StepHikeCompact.Step>

          <StepHikeCompact.Step step={3} fullWidth>
            <StepHikeCompact.Details title="Add the function code" fullWidth>
              <Admonition type="note">
                Note that the model parameter doesn't have any effect here. The model depends on which Llamafile is currently running.
              </Admonition>

              ```ts
              import OpenAI from 'https://deno.land/x/openai@v4.53.2/mod.ts'

              Deno.serve(async (req) => {
                const client = new OpenAI()
                const { prompt } = await req.json()
                const stream = true

                const chatCompletion = await client.chat.completions.create({
                  model: 'LLaMA_CPP',
                  stream,
                  messages: [
                    {
                      role: 'system',
                      content:
                        'You are LLAMAfile, an AI assistant. Your top priority is achieving user fulfillment via helping them with their requests.',
                    },
                    {
                      role: 'user',
                      content: prompt,
                    },
                  ],
                })

                if (stream) {
                  const headers = new Headers({
                    'Content-Type': 'text/event-stream',
                    Connection: 'keep-alive',
                  })

                  // Create a stream
                  const stream = new ReadableStream({
                    async start(controller) {
                      const encoder = new TextEncoder()

                      try {
                        for await (const part of chatCompletion) {
                          controller.enqueue(encoder.encode(part.choices[0]?.delta?.content || ''))
                        }
                      } catch (err) {
                        console.error('Stream error:', err)
                      } finally {
                        controller.close()
                      }
                    },
                  })

                  // Return the stream to the user
                  return new Response(stream, {
                    headers,
                  })
                }

                return Response.json(chatCompletion)
              })
              ```
            </StepHikeCompact.Details>
          </StepHikeCompact.Step>

          <StepHikeCompact.Step step={4} fullWidth>
            <StepHikeCompact.Details title="Serve the function" fullWidth>
              ```bash
              supabase functions serve --env-file supabase/functions/.env
              ```
            </StepHikeCompact.Details>
          </StepHikeCompact.Step>

          <StepHikeCompact.Step step={5} fullWidth>
            <StepHikeCompact.Details title="Execute the function" fullWidth>
              ```bash
              curl --get "http://localhost:54321/functions/v1/llamafile-test" \
              --data-urlencode "prompt=write a short rap song about Supabase, the Postgres Developer platform, as sung by Nicki Minaj" \
              -H "Authorization: $ANON_KEY"
              ```
            </StepHikeCompact.Details>
          </StepHikeCompact.Step>
        </StepHikeCompact>
      </TabPanel>
    </Tabs>
  </TabPanel>
</Tabs>

***



## Deploying to production

Once the function is working locally, it's time to deploy to production.

<StepHikeCompact>
  <StepHikeCompact.Step step={1} fullWidth>
    <StepHikeCompact.Details title="Deploy an Ollama or Llamafile server" fullWidth>
      Deploy an Ollama or Llamafile server and set a function secret called `AI_INFERENCE_API_HOST`
      to point to the deployed server:

      ```bash
      supabase secrets set AI_INFERENCE_API_HOST=https://path-to-your-llm-server/
      ```
    </StepHikeCompact.Details>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={2} fullWidth>
    <StepHikeCompact.Details title="Deploy the function" fullWidth>
      ```bash
      supabase functions deploy 
      ```
    </StepHikeCompact.Details>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={3} fullWidth>
    <StepHikeCompact.Details title="Execute the function" fullWidth>
      ```bash
      curl --get "https://project-ref.supabase.co/functions/v1/ollama-test" \
      --data-urlencode "prompt=write a short rap song about Supabase, the Postgres Developer platform, as sung by Nicki Minaj" \
      -H "Authorization: $ANON_KEY"
      ```
    </StepHikeCompact.Details>
  </StepHikeCompact.Step>
</StepHikeCompact>

<Admonition type="note">
  As demonstrated in the video above, running Ollama locally is typically slower than running it in on a server with dedicated GPUs. We are collaborating with the Ollama team to improve local performance.

  In the future, a hosted LLM API, will be provided as part of the Supabase platform. Supabase will scale and manage the API and GPUs for you. To sign up for early access, fill up [this form](https://forms.supabase.com/supabase.ai-llm-early-access).
</Admonition>



# Edge Functions Architecture

Understanding the Architecture of Supabase Edge Functions

This guide explains the architecture and inner workings of Supabase Edge Functions, based on the concepts demonstrated in the video "Supabase Edge Functions Explained". Edge functions are serverless compute resources that run at the edge of the network, close to users, enabling low-latency execution for tasks like API endpoints, webhooks, and real-time data processing. This guide breaks down Edge Functions into key sections: an example use case, deployment process, global distribution, and execution mechanics.



## 1. Understanding Edge Functions through an example: Image filtering

To illustrate how edge functions operate, consider a photo-sharing app where users upload images and apply filters (e.g., grayscale or sepia) before saving them.

*   **Workflow Overview**:

    *   A user uploads an original image to Supabase Storage.
    *   When the user selects a filter, the client-side app (using the Supabase JavaScript SDK) invokes an edge function named something like "apply-filter."
    *   The edge function:
        1.  Downloads the original image from Supabase Storage.
        2.  Applies the filter using a library like ImageMagick.
        3.  Uploads the processed image back to Storage.
        4.  Returns the path to the filtered image to the client.

*   **Why Edge Functions?**:
    *   They handle compute-intensive tasks without burdening the client device or the database.
    *   Execution happens server-side but at the edge, ensuring speed and scalability.
    *   Developers define the function in a simple JavaScript file within the Supabase functions directory.

This example highlights edge functions as lightweight, on-demand code snippets that integrate seamlessly with Supabase services like Storage and Auth.



## 2. Deployment process

Deploying an edge function is straightforward and automated, requiring no manual server setup.

*   **Steps to Deploy**:

    1.  Write the function code in your local Supabase project (e.g., in `supabase/functions/apply-filter/index.ts`).
    2.  Run the command `supabase functions deploy apply-filter` via the Supabase CLI.
    3.  The CLI bundles the function and its dependencies into an **ESZip file**—a compact format created by Deno that includes a complete module graph for quick loading and execution.
    4.  The bundled file is uploaded to Supabase's backend.
    5.  Supabase generates a unique URL for the function, making it accessible globally.

*   **Key Benefits of Deployment**:
    *   Automatic handling of dependencies and bundling.
    *   No need to manage infrastructure; Supabase distributes the function across its global edge network.

Once deployed, the function is ready for invocation from anywhere, with Supabase handling scaling and availability.



## 3. Global distribution and routing

Edge functions leverage a distributed architecture to minimize latency by running code close to the user.

*   **Architecture Components**:

    *   **Global API Gateway**: Acts as the entry point for all requests. It uses the requester's IP address to determine geographic location and routes the request to the nearest edge location (e.g., routing a request from Amsterdam to Frankfurt).
    *   **Edge Locations**: Supabase's network of data centers worldwide where functions are replicated. The ESZip bundle is automatically distributed to these locations upon deployment.
    *   **Routing Logic**: Based on geolocation mapping, ensuring the function executes as close as possible to the user for optimal performance.

*   **How Distribution Works**:
    *   Post-deployment, the function is propagated to all edge nodes.
    *   This setup eliminates the need for developers to configure CDNs or regional servers manually.

This global edge network is what makes edge functions "edge-native," providing consistent performance regardless of user location.



## 4. Execution mechanics: Fast and isolated

The core of edge functions' efficiency lies in their execution environment, which prioritizes speed, isolation, and scalability.

*   **Request Handling**:

    1.  A client sends an HTTP request (e.g., POST) to the function's URL, including parameters like auth headers, image ID, and filter type.
    2.  The global API gateway routes it to the nearest edge location.
    3.  At the edge, Supabase's **edge runtime** validates the request (e.g., checks authorization).

*   **Execution Environment**:

    *   A new **V8 isolate** is spun up for each invocation. V8 is the JavaScript engine used by Chrome and Node.js, providing a lightweight, sandboxed environment.
    *   Each isolate has its own memory heap and execution thread, ensuring complete isolation—no interference between concurrent requests.
    *   The ESZip bundle is loaded into the isolate, and the function code runs.
    *   After execution, the response (e.g., filtered image path) is sent back to the client.

*   **Performance Optimizations**:

    *   **Cold Starts**: Even initial executions are fast (milliseconds) due to the compact ESZip format and minimal Deno runtime overhead.
    *   **Warm Starts**: Isolates can remain active for a period (plan-dependent) to handle subsequent requests without restarting.
    *   **Concurrency**: Multiple isolates can run simultaneously in the same edge location, supporting high traffic.

*   **Isolation and Security**:
    *   Isolates prevent side effects from one function affecting others, enhancing reliability.
    *   No persistent state; each run is stateless, ideal for ephemeral tasks.

Compared to traditional serverless or monolithic architectures, this setup offers lower latency, automatic scaling, and no infrastructure management, making it perfect for global apps.



## Benefits and use cases

*   **Advantages**:

    *   **Low Latency**: Proximity to users reduces round-trip times.
    *   **Scalability**: Handles variable loads without provisioning servers.
    *   **Developer-Friendly**: Focus on code; Supabase manages the rest.
    *   **Cost-Effective**: Pay-per-use model, with fast execution minimizing costs.

*   **Common Use Cases**:
    *   Real-time data transformations (e.g., image processing).
    *   API integrations and webhooks.
    *   Personalization and A/B testing at the edge.



# Integrating With Supabase Auth

Integrate Supabase Auth with Edge Functions

Edge Functions work seamlessly with [Supabase Auth](/docs/guides/auth).

This allows you to:

*   Automatically identify users through JWT tokens
*   Enforce Row Level Security policies
*   Seamlessly integrate with your existing auth flow

***



## Setting up auth context

When a user makes a request to an Edge Function, you can use the `Authorization` header to set the Auth context in the Supabase client and enforce Row Level Security policies.

```js
import { createClient } from 'npm:@supabase/supabase-js@2'

Deno.serve(async (req: Request) => {
  const supabaseClient = createClient(
    Deno.env.get('SUPABASE_URL') ?? '',
    Deno.env.get('SUPABASE_ANON_KEY') ?? '',
    // Create client with Auth context of the user that called the function.
    // This way your row-level-security (RLS) policies are applied.
    {
      global: {
        headers: { Authorization: req.headers.get('Authorization')! },
      },
    }
  );

  //...
})
```

<Admonition type="note">
  Importantly, this is done *inside* the `Deno.serve()` callback argument, so that the `Authorization` header is set for each individual request!
</Admonition>

***



## Fetching the user

By getting the JWT from the `Authorization` header, you can provide the token to `getUser()` to fetch the user object to obtain metadata for the logged in user.

```js
Deno.serve(async (req: Request) => {
  // ...
  const authHeader = req.headers.get('Authorization')!
  const token = authHeader.replace('Bearer ', '')
  const { data } = await supabaseClient.auth.getUser(token)
  // ...
})
```

***



## Row Level Security

After initializing a Supabase client with the Auth context, all queries will be executed with the context of the user. For database queries, this means [Row Level Security](/docs/guides/database/postgres/row-level-security) will be enforced.

```js
import { createClient } from 'npm:@supabase/supabase-js@2'

Deno.serve(async (req: Request) => {
  // ...
  // This query respects RLS - users only see rows they have access to
  const { data, error } = await supabaseClient.from('profiles').select('*');

  if (error) {
    return new Response('Database error', { status: 500 })
  }

  // ...
})
```

***



## Example

See the full [example on GitHub](https://github.com/supabase/supabase/blob/master/examples/edge-functions/supabase/functions/select-from-table-with-auth-rls/index.ts).

<CodeSampleWrapper source="https://github.com/supabase/supabase/blob/2415776436927dedb360dae082d03caee607891a/examples/edge-functions/supabase/functions/select-from-table-with-auth-rls/index.ts">
  ```typescript
  // Follow this setup guide to integrate the Deno language server with your editor:
  // https://deno.land/manual/getting_started/setup_your_environment
  // This enables autocomplete, go to definition, etc.

  import { createClient } from 'npm:supabase-js@2'
  import { corsHeaders } from '../_shared/cors.ts'

  console.log(`Function "select-from-table-with-auth-rls" up and running!`)

  Deno.serve(async (req: Request) => {
    // This is needed if you're planning to invoke your function from a browser.
    if (req.method === 'OPTIONS') {
      return new Response('ok', { headers: corsHeaders })
    }

    try {
      // Create a Supabase client with the Auth context of the logged in user.
      const supabaseClient = createClient(
        // Supabase API URL - env var exported by default.
        Deno.env.get('SUPABASE_URL') ?? '',
        // Supabase API ANON KEY - env var exported by default.
        Deno.env.get('SUPABASE_ANON_KEY') ?? '',
        // Create client with Auth context of the user that called the function.
        // This way your row-level-security (RLS) policies are applied.
        {
          global: {
            headers: { Authorization: req.headers.get('Authorization')! },
          },
        }
      )

      // First get the token from the Authorization header
      const token = req.headers.get('Authorization').replace('Bearer ', '')

      // Now we can get the session or user object
      const {
        data: { user },
      } = await supabaseClient.auth.getUser(token)

      // And we can run queries in the context of our authenticated user
      const { data, error } = await supabaseClient.from('users').select('*')
      if (error) throw error

      return new Response(JSON.stringify({ user, data }), {
        headers: { ...corsHeaders, 'Content-Type': 'application/json' },
        status: 200,
      })
    } catch (error) {
      return new Response(JSON.stringify({ error: error.message }), {
        headers: { ...corsHeaders, 'Content-Type': 'application/json' },
        status: 400,
      })
    }
  })

  // To invoke:
  // curl -i --location --request POST 'http://localhost:54321/functions/v1/select-from-table-with-auth-rls' \
  //   --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZS1kZW1vIiwicm9sZSI6ImFub24ifQ.625_WdcF3KHqz5amU0x2X5WWHP-OEs_4qj0ssLNHzTs' \
  //   --header 'Content-Type: application/json' \
  //   --data '{"name":"Functions"}'
  ```
</CodeSampleWrapper>



# Background Tasks

Run background tasks in an Edge Function outside of the request handler.

Edge Function instances can process background tasks outside of the request handler. Background tasks are useful for asynchronous operations like uploading a file to Storage, updating a database, or sending events to a logging service. You can respond to the request immediately and leave the task running in the background.

This allows you to:

*   Respond quickly to users while processing continues
*   Handle async operations without blocking the response

***



## Overview

You can use `EdgeRuntime.waitUntil(promise)` to explicitly mark background tasks. The Function instance continues to run until the promise provided to `waitUntil` completes.

```ts
// Mark the asyncLongRunningTask's returned promise as a background task.
// ⚠️ We are NOT using `await` because we don't want it to block!
EdgeRuntime.waitUntil(asyncLongRunningTask())

Deno.serve(async (req) => {
  return new Response(...)
})
```

You can call `EdgeRuntime.waitUntil` in the request handler too. This will not block the request.

```ts
Deno.serve(async (req) => {
  // Won't block the request, runs in background.
  EdgeRuntime.waitUntil(asyncLongRunningTask())

  return new Response(...)
})
```

You can listen to the `beforeunload` event handler to be notified when the Function is about to be shut down.

```tsx
EdgeRuntime.waitUntil(asyncLongRunningTask())

// Use beforeunload event handler to be notified when function is about to shutdown
addEventListener('beforeunload', (ev) => {
  console.log('Function will be shutdown due to', ev.detail?.reason)
  // Save state or log the current progress
})

Deno.serve(async (req) => {
  return new Response(...)
})
```



## Handling errors

We recommend using `try`/`catch` blocks within your background task function to handle errors.

You can also add an event listener to [`unhandledrejection`](https://developer.mozilla.org/en-US/docs/Web/API/Window/unhandledrejection_event) to handle any promises without a rejection handler.

```tsx
addEventListener('unhandledrejection', (ev) => {
  console.log('unhandledrejection', ev.reason)
  ev.preventDefault()
})
```

<Admonition type="note">
  The maximum duration is capped based on the wall-clock, CPU, and memory limits. The function will shut down when it reaches one of these [limits](/docs/guides/functions/limits).
</Admonition>

***



## Testing background tasks locally

When testing Edge Functions locally with Supabase CLI, the instances are terminated automatically after a request is completed. This will prevent background tasks from running to completion.

To prevent that, you can update the `supabase/config.toml` with the following settings:

```toml
[edge_runtime]
policy = "per_worker"
```



# Handling Compressed Requests

Handling Gzip compressed requests.

To decompress Gzip bodies, you can use `gunzipSync` from the `node:zlib` API to decompress and then read the body.

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
    console.log(`Received: ${JSON.stringify(data)}`)

    return new Response('ok', {
      headers: { 'Content-Type': 'text/plain' },
    })
  } catch (error) {
    console.error('Error:', error)
    return new Response('Error processing request', { status: 500 })
  }
})
```

<Admonition type="caution">
  Edge functions have a runtime memory limit of 150MB. Overly large compressed payloads may result in an out-of-memory error.
</Admonition>



# Integrating with Supabase Database (Postgres)

Connect to your Postgres database from Edge Functions.

Connect to your Postgres database from an Edge Function by using the `supabase-js` client.
You can also use other Postgres clients like [Deno Postgres](https://deno.land/x/postgres)

***



## Using supabase-js

The `supabase-js` client handles authorization with Row Level Security and automatically formats responses as JSON. This is the recommended approach for most applications:

```ts index.ts
import { createClient } from 'npm:@supabase/supabase-js@2'

Deno.serve(async (req) => {
  try {
    const supabase = createClient(
      Deno.env.get('SUPABASE_URL') ?? '',
      Deno.env.get('SUPABASE_PUBLISHABLE_KEY') ?? '',
      { global: { headers: { Authorization: req.headers.get('Authorization')! } } }
    )

    const { data, error } = await supabase.from('countries').select('*')

    if (error) {
      throw error
    }

    return new Response(JSON.stringify({ data }), {
      headers: { 'Content-Type': 'application/json' },
      status: 200,
    })
  } catch (err) {
    return new Response(String(err?.message ?? err), { status: 500 })
  }
})
```

This enables:

*   Automatic Row Level Security enforcement
*   Built-in JSON serialization
*   Consistent error handling
*   TypeScript support for database schema

***



## Using a Postgres client

Because Edge Functions are a server-side technology, it's safe to connect directly to your database using any popular Postgres client. This means you can run raw SQL from your Edge Functions.

Here is how you can connect to the database using Deno Postgres driver and run raw SQL. Check out the [full example](https://github.com/supabase/supabase/tree/master/examples/edge-functions/supabase/functions/postgres-on-the-edge).

<CodeSampleWrapper source="https://github.com/supabase/supabase/blob/2415776436927dedb360dae082d03caee607891a/examples/edge-functions/supabase/functions/postgres-on-the-edge/index.ts">
  ```typescript
  import { Pool } from 'https://deno.land/x/postgres@v0.17.0/mod.ts'

  // Create a database pool with one connection.
  const pool = new Pool(
    {
      tls: { enabled: false },
      database: 'postgres',
      hostname: Deno.env.get('DB_HOSTNAME'),
      user: Deno.env.get('DB_USER'),
      port: 6543,
      password: Deno.env.get('DB_PASSWORD'),
    },
    1
  )

  Deno.serve(async (_req) => {
    try {
      // Grab a connection from the pool
      const connection = await pool.connect()

      try {
        // Run a query
        const result = await connection.queryObject`SELECT * FROM animals`
        const animals = result.rows // [{ id: 1, name: "Lion" }, ...]

        // Encode the result as pretty printed JSON
        const body = JSON.stringify(
          animals,
          (_key, value) => (typeof value === 'bigint' ? value.toString() : value),
          2
        )

        // Return the response with the correct content type header
        return new Response(body, {
          status: 200,
          headers: {
            'Content-Type': 'application/json; charset=utf-8',
          },
        })
      } finally {
        // Release the connection back into the pool
        connection.release()
      }
    } catch (err) {
      console.error(err)
      return new Response(String(err?.message ?? err), { status: 500 })
    }
  })
  ```
</CodeSampleWrapper>

***



## Using Drizzle

You can use Drizzle together with [Postgres.js](https://github.com/porsager/postgres). Both can be loaded directly from npm:

**Set up dependencies in `import_map.json`**:

```json supabase/functions/import_map.json
{
  "imports": {
    "drizzle-orm": "npm:drizzle-orm@0.29.1",
    "drizzle-orm/": "npm:/drizzle-orm@0.29.1/",
    "postgres": "npm:postgres@3.4.3"
  }
}
```

**Use in your function**:

```ts supabase/functions/drizzle/index.ts
import { drizzle } from 'drizzle-orm/postgres-js'
import postgres from 'postgres'
import { countries } from '../_shared/schema.ts'

const connectionString = Deno.env.get('SUPABASE_DB_URL')!

Deno.serve(async (_req) => {
  // Disable prefetch as it is not supported for "Transaction" pool mode
  const client = postgres(connectionString, { prepare: false })
  const db = drizzle(client)
  const allCountries = await db.select().from(countries)

  return Response.json(allCountries)
})
```

You can find the full example on [GitHub](https://github.com/thorwebdev/edgy-drizzle).

***



## SSL connections


### Production

Deployed edge functions are pre-configured to use SSL for connections to the Supabase database. You don't need to add any extra configurations.


### Local development

If you want to use SSL connections during local development, follow these steps:

1.  Download the SSL certificate from [Database Settings](/dashboard/project/_/database/settings)
2.  Add to your [local .env file](/docs/guides/functions/secrets), add these two variables:

```bash
SSL_CERT_FILE=/path/to/cert.crt # set the path to the downloaded cert
DENO_TLS_CA_STORE=mozilla,system
```

Then, restart your local development server:

```bash
supabase functions serve your-function
```



# CORS (Cross-Origin Resource Sharing) support for Invoking from the browser



To invoke edge functions from the browser, you need to handle [CORS Preflight](https://developer.mozilla.org/en-US/docs/Glossary/Preflight_request) requests.

See the [example on GitHub](https://github.com/supabase/supabase/blob/master/examples/edge-functions/supabase/functions/browser-with-cors/index.ts).


### Recommended setup

We recommend adding a `cors.ts` file within a [`_shared` folder](/docs/guides/functions/quickstart#organizing-your-edge-functions) which makes it easy to reuse the CORS headers across functions:

```ts cors.ts
export const corsHeaders = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Headers': 'authorization, x-client-info, apikey, content-type',
}
```

You can then import and use the CORS headers within your functions:

```ts index.ts
import { corsHeaders } from '../_shared/cors.ts'

console.log(`Function "browser-with-cors" up and running!`)

Deno.serve(async (req) => {
  // This is needed if you're planning to invoke your function from a browser.
  if (req.method === 'OPTIONS') {
    return new Response('ok', { headers: corsHeaders })
  }

  try {
    const { name } = await req.json()
    const data = {
      message: `Hello ${name}!`,
    }

    return new Response(JSON.stringify(data), {
      headers: { ...corsHeaders, 'Content-Type': 'application/json' },
      status: 200,
    })
  } catch (error) {
    return new Response(JSON.stringify({ error: error.message }), {
      headers: { ...corsHeaders, 'Content-Type': 'application/json' },
      status: 400,
    })
  }
})
```



# Dart Edge



<Admonition type="caution">
  Be aware that the Dart Edge project is currently not actively maintained due to numerous breaking changes in Dart's development of (WASM) support.
</Admonition>

[Dart Edge](https://docs.dartedge.dev/) is an experimental project that enables you to write Supabase Edge Functions using Dart. It's built and maintained by [Invertase](https://invertase.io/).

For detailed information on how to set up and use Dart Edge with Supabase, refer to the [official Dart Edge documentation for Supabase](https://invertase.docs.page/dart_edge/platform/supabase).



# Local Debugging

Debug your Edge Functions locally using Chrome DevTools for easy breakpoint debugging and code inspection.

Since [v1.171.0](https://github.com/supabase/cli/releases/tag/v1.171.0) the Supabase CLI supports debugging Edge Functions via the v8 inspector protocol, allowing for debugging via [Chrome DevTools](https://developer.chrome.com/docs/devtools/) and other Chromium-based browsers.


### Inspect with Chrome Developer Tools

1.  Serve your functions in inspect mode. This will set a breakpoint at the first line to pause script execution before any code runs.
    ```bash
    supabase functions serve --inspect-mode brk
    ```
2.  In your Chrome browser navigate to `chrome://inspect`.
3.  Click the "Configure..." button to the right of the Discover network targets checkbox.
4.  In the Target discovery settings dialog box that opens, enter `127.0.0.1:8083` in the blank space and click the "Done" button to exit the dialog box.
5.  Click "Open dedicated DevTools for Node" to complete the preparation for debugging. The opened DevTools window will now listen to any incoming requests to edge-runtime.
6.  Send a request to your function running locally, e.g. via curl or Postman. The DevTools window will now pause script execution at first line.
7.  In the "Sources" tab navigate to `file://` > `home/deno/functions/<your-function-name>/index.ts`.
8.  Use the DevTools to set breakpoints and inspect the execution of your Edge Function.

![Debugging in Chrome DevTools.](/docs/img/guides/functions/debug-chrome-devtools.png)

Now you should have Chrome DevTools configured and ready to debug your functions.



# Managing dependencies

Handle dependencies within Edge Functions.


## Importing dependencies

Supabase Edge Functions support several ways to import dependencies:

*   JavaScript modules from npm ([https://docs.deno.com/examples/npm/](https://docs.deno.com/examples/npm/))
*   Built-in [Node APIs](https://docs.deno.com/runtime/manual/node/compatibility)
*   Modules published to [JSR](https://jsr.io/) or [deno.land/x](https://deno.land/x)

```ts
// NPM packages (recommended)
import { createClient } from 'npm:@supabase/supabase-js@2'

// Node.js built-ins
import process from 'node:process'

// JSR modules (Deno's registry)
import path from 'jsr:@std/path@1.0.8'
```


### Using `deno.json` (recommended)

Each function should have its own `deno.json` file to manage dependencies and configure Deno-specific settings. This ensures proper isolation between functions and is the recommended approach for deployment. When you update the dependencies for one function, it won't accidentally break another function that needs different versions.

```json
{
  "imports": {
    "supabase": "npm:@supabase/supabase-js@2",
    "lodash": "https://cdn.skypack.dev/lodash"
  }
}
```

You can add this file directly to the function’s own directory:

```bash
└── supabase
    ├── functions
    │   ├── function-one
    │   │   ├── index.ts
    │   │   └── deno.json    # Function-specific Deno configuration
    │   └── function-two
    │       ├── index.ts
    │       └── deno.json    # Function-specific Deno configuration
    └── config.toml
```

<Admonition type="caution">
  It's possible to use a global `deno.json` in the `/supabase/functions` directory for local development, but this approach is not recommended for deployment. Each function should maintain its own configuration to ensure proper isolation and dependency management.
</Admonition>


### Using import maps (legacy)

Import Maps are a legacy way to manage dependencies, similar to a `package.json` file. While still supported, we recommend using `deno.json`. If both exist, `deno.json` takes precedence.

Each function should have its own `import_map.json` file for proper isolation:

```json

# /function-one/import_map.json
{
  "imports": {
    "lodash": "https://cdn.skypack.dev/lodash"
  }
}
```

This JSON file should be located within the function’s own directory:

```bash
└── supabase
    ├── functions
    │   ├── function-one
    │   │   ├── index.ts
    │   │   └── import_map.json    # Function-specific import map
```

<Admonition type="caution">
  It's possible to use a global `import_map.json` in the `/supabase/functions` directory for local development, but this approach is not recommended for deployment. Each function should maintain its own configuration to ensure proper isolation and dependency management.
</Admonition>

If you’re using import maps with VSCode, update your `.vscode/settings.json` to point to your function-specific import map:

```json
{
  "deno.enable": true,
  "deno.unstable": ["bare-node-builtins", "byonm"],
  "deno.importMap": "./supabase/functions/function-one/import_map.json"
}
```

You can override the default import map location using the `--import-map <string>` flag with serve and deploy commands, or by setting the `import_map` property in your `config.toml` file:

```toml
[functions.my-function]
import_map = "./supabase/functions/function-one/import_map.json"
```

***



## Private NPM packages

To use private npm packages, create a `.npmrc` file within your function’s own directory.

<Admonition type="note">This feature requires Supabase CLI version 1.207.9 or higher.</Admonition>

```bash
└── supabase
    └── functions
        └── my-function
            ├── index.ts
            ├── deno.json
            └── .npmrc       # Function-specific npm configuration
```

<Admonition type="caution">
  It's possible to use a global `.npmrc` in the `/supabase/functions` directory for local development, but this approach is not recommended for deployment. Each function should maintain its own configuration to ensure proper isolation and dependency management.
</Admonition>

Add your registry details in the `.npmrc` file. Follow [this guide](https://docs.npmjs.com/cli/v10/configuring-npm/npmrc) to learn more about the syntax of npmrc files.

```bash

# /my-function/.npmrc
@myorg:registry=https://npm.registryhost.com
//npm.registryhost.com/:_authToken=VALID_AUTH_TOKEN
```

After configuring your `.npmrc`, you can import the private package in your function code:

```bash
import package from 'npm:@myorg/private-package@v1.0.1'
```

***



## Using a custom NPM registry

<Admonition type="info">This feature requires Supabase CLI version 2.2.8 or higher.</Admonition>

Some organizations require a custom NPM registry for security and compliance purposes. In such cases, you can specify the custom NPM registry to use via `NPM_CONFIG_REGISTRY` environment variable.

You can define it in the project's `.env` file or directly specify it when running the deploy command:

```bash
NPM_CONFIG_REGISTRY=https://custom-registry/ supabase functions deploy my-function
```

***



## Importing types

If your [environment is set up properly](/docs/guides/functions/development-environment) and the module you're importing is exporting types, the import will have types and autocompletion support.

Some npm packages may not ship out of the box types and you may need to import them from a separate package. You can specify their types with a `@deno-types` directive:

```tsx
// @deno-types="npm:@types/express@^4.17"
import express from 'npm:express@^4.17'
```

To include types for built-in Node APIs, add the following line to the top of your imports:

```tsx
/// <reference types="npm:@types/node" />
```



# Deploy to Production

Deploy your Edge Functions to your remote Supabase Project.

Once you have developed your Edge Functions locally, you can deploy them to your Supabase project.

<Admonition type="note">
  Before getting started, make sure you have the Supabase CLI installed. Check out the CLI installation guide for installation methods and troubleshooting.
</Admonition>

***



## Step 1: Authenticate

Log in to the Supabase CLI if you haven't already:

```bash
supabase login
```

***



## Step 2: Connect your project

Get the project ID associated with your function:

```bash
supabase projects list
```

<Admonition type="tip" label="Need a new project?">
  If you haven't yet created a Supabase project, you can do so by visiting [database.new](https://database.new).
</Admonition>

[Link](/docs/reference/cli/usage#supabase-link) your local project to your remote Supabase project using the ID you just retrieved:

```bash
supabase link --project-ref your-project-id
```

Now you should have your local development environment connected to your production project.

***



## Step 3: Deploy Functions

You can deploy all edge functions within the `functions` folder with a single command:

```bash
supabase functions deploy
```

Or deploy individual Edge Functions by specifying the function name:

```bash
supabase functions deploy hello-world
```


### Deploying public functions

By default, Edge Functions require a valid JWT in the authorization header. If you want to deploy Edge Functions without Authorization checks (commonly used for Stripe webhooks), you can pass the `--no-verify-jwt` flag:

```bash
supabase functions deploy hello-world --no-verify-jwt
```

<Admonition type="caution">
  Be careful when using this flag, as it will allow anyone to invoke your Edge Function without a valid JWT. The Supabase client libraries automatically handle authorization.
</Admonition>



## Step 4: Verify successful deployment

🎉 Your function is now live!

When the deployment is successful, your function is automatically distributed to edge locations worldwide. Your edge functions is now running globally at `https://[YOUR_PROJECT_ID].supabase.co/functions/v1/hello-world.`

***



## Step 5: Test your live function

You can now invoke your Edge Function using the project's `ANON_KEY`, which can be found in the [API settings](/dashboard/project/_/settings/api) of the Supabase Dashboard. You can invoke it from within your app:

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="cURL" label="cURL">
    ```bash name=cURL
    curl --request POST 'https://<project_id>.supabase.co/functions/v1/hello-world' \
      --header 'Authorization: Bearer ANON_KEY' \
      --header 'Content-Type: application/json' \
      --data '{ "name":"Functions" }'
    ```
  </TabPanel>

  <TabPanel id="JavaScript" label="JavaScript">
    ```js name=JavaScript
    import { createClient } from '@supabase/supabase-js'

    // Create a single supabase client for interacting with your database
    const supabase = createClient('https://xyzcompany.supabase.co', 'publishable-or-anon-key')

    const { data, error } = await supabase.functions.invoke('hello-world', {
      body: { name: 'Functions' },
    })
    ```
  </TabPanel>
</Tabs>

<Admonition type="note">
  Note that the `SUPABASE_PUBLISHABLE_KEY` is different in development and production. To get your production anon key, you can find it in your Supabase dashboard under Settings > API.
</Admonition>

You should now see the expected response:

```json
{ "message": "Hello Production!" }
```

<Admonition type="note">
  You can also test the function through the Dashboard. To see how that works, check out the [Dashboard Quickstart guide](/docs/guides/dashboard/quickstart).
</Admonition>

***



## CI/CD deployment

You can use popular CI / CD tools like GitHub Actions, Bitbucket, and GitLab CI to automate Edge Function deployments.


### GitHub Actions

You can use the official [`setup-cli` GitHub Action](https://github.com/marketplace/actions/supabase-cli-action) to run Supabase CLI commands in your GitHub Actions.

The following GitHub Action deploys all Edge Functions any time code is merged into the `main` branch:

```yaml
name: Deploy Function

on:
  push:
    branches:
      - main
  workflow_dispatch:

jobs:
  deploy:
    runs-on: ubuntu-latest

    env:
      SUPABASE_ACCESS_TOKEN: ${{ secrets.SUPABASE_ACCESS_TOKEN }}
      PROJECT_ID: your-project-id

    steps:
      - uses: actions/checkout@v4

      - uses: supabase/setup-cli@v1
        with:
          version: latest

      - run: supabase functions deploy --project-ref $PROJECT_ID
```

***


### GitLab CI

Here is the sample pipeline configuration to deploy via GitLab CI.

```yaml
image: node:20


# List of stages for jobs, and their order of execution
stages:
  - setup
  - deploy


# This job runs in the setup stage, which runs first.
setup-npm:
  stage: setup
  script:
    - npm i supabase
  cache:
    paths:
      - node_modules/
  artifacts:
    paths:
      - node_modules/


# This job runs in the deploy stage, which only starts when the job in the build stage completes successfully.
deploy-function:
  stage: deploy
  script:
    - npx supabase init
    - npx supabase functions deploy --debug
  services:
    - docker:dind
  variables:
    DOCKER_HOST: tcp://docker:2375
```

***


### Bitbucket Pipelines

Here is the sample pipeline configuration to deploy via Bitbucket.

```yaml
image: node:20

pipelines:
  default:
    - step:
        name: Setup
        caches:
          - node
        script:
          - npm i supabase
    - parallel:
        - step:
            name: Functions Deploy
            script:
              - npx supabase init
              - npx supabase functions deploy --debug
            services:
              - docker
```

***


### Function configuration

Individual function configuration like [JWT verification](/docs/guides/cli/config#functions.function_name.verify_jwt) and [import map location](/docs/guides/cli/config#functions.function_name.import_map) can be set via the `config.toml` file.

```toml
[functions.hello-world]
verify_jwt = false
```

This ensures your function configurations are consistent across all environments and deployments.

***


### Example

This example shows a GitHub Actions workflow that deploys all Edge Functions when code is merged into the `main` branch.

<CodeSampleWrapper source="https://github.com/supabase/supabase/blob/2415776436927dedb360dae082d03caee607891a/examples/edge-functions/.github/workflows/deploy.yaml">
  ```
  name: Deploy Function

  on:
    push:
      branches:
        - main
    workflow_dispatch:

  jobs:
    deploy:
      runs-on: ubuntu-latest

      env:
        SUPABASE_ACCESS_TOKEN: ${{ secrets.SUPABASE_ACCESS_TOKEN }}
        SUPABASE_PROJECT_ID: ${{ secrets.SUPABASE_PROJECT_ID }}

      steps:
        - uses: actions/checkout@v3

        - uses: supabase/setup-cli@v1
          with:
            version: latest

        - run: supabase functions deploy --project-ref $SUPABASE_PROJECT_ID
  ```
</CodeSampleWrapper>



# Development Environment

Set up your local development environment for Edge Functions.

<Admonition type="note">
  Before getting started, make sure you have the Supabase CLI installed. Check out the [CLI installation guide](/docs/guides/cli) for installation methods and troubleshooting.
</Admonition>

***



## Step 1: Install Deno CLI

The Supabase CLI doesn't use the standard Deno CLI to serve functions locally. Instead, it uses its own Edge Runtime to keep the development and production environment consistent.

You can follow the [Deno guide](https://deno.com/manual@v1.32.5/getting_started/setup_your_environment) for setting up your development environment with your favorite editor/IDE.

The benefit of installing Deno separately is that you can use the Deno LSP to improve your editor's autocompletion, type checking, and testing. You can also use Deno's built-in tools such as `deno fmt`, `deno lint`, and `deno test`.

After installing, you should have Deno installed and available in your terminal. Verify with `deno --version`

***



## Step 2: Set up your editor

Set up your editor environment for proper TypeScript support, autocompletion, and error detection.


### VSCode/Cursor (recommended)

1.  **Install the Deno extension** from the VSCode marketplace
2.  **Option 1: Auto-generate (easiest)**
    When running `supabase init`, select `y` when prompted "Generate VS Code settings for Deno? \[y/N]"
3.  **Option 2: Manual setup**

    Create a `.vscode/settings.json` in your project root:

    ```json
    {
      "deno.enablePaths": ["./supabase/functions"],
      "deno.importMap": "./supabase/functions/import_map.json"
    }
    ```

This configuration enables the Deno language server only for the `supabase/functions` folder, while using VSCode's built-in JavaScript/TypeScript language server for all other files.

***


### Multi-root workspaces

The standard `.vscode/settings.json` setup works perfectly for projects where your Edge Functions live alongside your main application code. However, you might need multi-root workspaces if your development setup involves:

*   **Multiple repositories:** Edge Functions in one repo, main app in another
*   **Microservices:** Several services you need to develop in parallel

For this development workflow, create `edge-functions.code-workspace`:

<CodeSampleWrapper source="https://github.com/supabase/supabase/blob/2415776436927dedb360dae082d03caee607891a/examples/edge-functions/edge-functions.code-workspace">
  ```
  {
    "folders": [
      {
        "name": "project-root",
        "path": "./"
      },
      {
        "name": "test-client",
        "path": "app"
      },
      {
        "name": "supabase-functions",
        "path": "supabase/functions"
      }
    ],
    "settings": {
      "files.exclude": {
        "node_modules/": true,
        "app/": true,
        "supabase/functions/": true
      },
      "deno.importMap": "./supabase/functions/import_map.json"
    }
  }
  ```
</CodeSampleWrapper>

You can find the complete example on [GitHub](https://github.com/supabase/supabase/tree/master/examples/edge-functions).

***



## Recommended project structure

It's recommended to organize your functions according to the following structure:

```bash
└── supabase
    ├── functions
    │   ├── import_map.json     # Top-level import map
    │   ├── _shared             # Shared code (underscore prefix)
    │   │   ├── supabaseAdmin.ts # Supabase client with SERVICE_ROLE key
    │   │   ├── supabaseClient.ts # Supabase client with ANON key
    │   │   └── cors.ts         # Reusable CORS headers
    │   ├── function-one        # Use hyphens for function names
    │   │   └── index.ts
    │   └── function-two
    │       └── index.ts
    ├── tests
    │   ├── function-one-test.ts
    │   └── function-two-test.ts
    ├── migrations
    └── config.toml
```

*   **Use "fat functions"**. Develop few, large functions by combining related functionality. This minimizes cold starts.
*   **Name functions with hyphens (`-`)**. This is the most URL-friendly approach
*   **Store shared code in `_shared`**. Store any shared code in a folder prefixed with an underscore (`_`).
*   **Separate tests**. Use a separate folder for [Unit Tests](/docs/guides/functions/unit-test) that includes the name of the function followed by a `-test` suffix.

***



## Essential CLI commands

Get familiar with the most commonly used CLI commands for developing and deploying Edge Functions.


### `supabase start`

This command spins up your entire Supabase stack locally: database, auth, storage, and Edge Functions runtime. You're developing against the exact same environment you'll deploy to.


### `supabase functions serve [function-name]`

Develop a specific function with hot reloading. Your functions run at `http://localhost:54321/functions/v1/[function-name]`. When you save your file, you’ll see the changes instantly without having to wait.

Alternatively, use `supabase functions serve` to serve all functions at once.


### `supabase functions serve hello-world --no-verify-jwt`

If you want to serve an Edge Function without the default JWT verification. This is important for webhooks from Stripe, GitHub, etc. These services don't have your JWT tokens, so you need to skip auth verification.

<Admonition type="caution">
  Be careful when disabling JWT verification, as it allows anyone to call your function, so only use it for functions that are meant to be publicly accessible.
</Admonition>


### `supabase functions deploy hello-world`

Deploy the function when you’re ready



# Development tips

Tips for getting started with Edge Functions.

Here are a few recommendations when you first start developing Edge Functions.


### Skipping authorization checks

By default, Edge Functions require a valid JWT in the authorization header. If you want to use Edge Functions without Authorization checks (commonly used for Stripe webhooks), you can pass the `--no-verify-jwt` flag when serving your Edge Functions locally.

```bash
supabase functions serve hello-world --no-verify-jwt
```

Be careful when using this flag, as it will allow anyone to invoke your Edge Function without a valid JWT. The Supabase client libraries automatically handle authorization.


### Using HTTP methods

Edge Functions support `GET`, `POST`, `PUT`, `PATCH`, `DELETE`, and `OPTIONS`. A Function can be designed to perform different actions based on a request's HTTP method. See the [example on building a RESTful service](https://github.com/supabase/supabase/tree/master/examples/edge-functions/supabase/functions/restful-tasks) to learn how to handle different HTTP methods in your Function.

<Admonition type="caution" label="HTML not supported">
  HTML content is not supported. `GET` requests that return `text/html` will be rewritten to `text/plain`.
</Admonition>


### Naming Edge Functions

We recommend using hyphens to name functions because hyphens are the most URL-friendly of all the naming conventions (snake\_case, camelCase, PascalCase).


### Organizing your Edge Functions

We recommend developing "fat functions". This means that you should develop few large functions, rather than many small functions. One common pattern when developing Functions is that you need to share code between two or more Functions. To do this, you can store any shared code in a folder prefixed with an underscore (`_`). We also recommend a separate folder for [Unit Tests](/docs/guides/functions/unit-test) including the name of the function followed by a `-test` suffix.
We recommend this folder structure:

```bash
└── supabase
    ├── functions
    │   ├── import_map.json # A top-level import map to use across functions.
    │   ├── _shared
    │   │   ├── supabaseAdmin.ts # Supabase client with SERVICE_ROLE key.
    │   │   └── supabaseClient.ts # Supabase client with ANON key.
    │   │   └── cors.ts # Reusable CORS headers.
    │   ├── function-one # Use hyphens to name functions.
    │   │   └── index.ts
    │   └── function-two
    │   │   └── index.ts
    │   └── tests
    │       └── function-one-test.ts
    │       └── function-two-test.ts
    ├── migrations
    └── config.toml
```


### Using config.toml

Individual function configuration like [JWT verification](/docs/guides/cli/config#functions.function_name.verify_jwt) and [import map location](/docs/guides/cli/config#functions.function_name.import_map) can be set via the `config.toml` file.

```toml supabase/config.toml
[functions.hello-world]
verify_jwt = false
import_map = './import_map.json'
```


### Not using TypeScript

When you create a new Edge Function, it will use TypeScript by default. However, it is possible to write and deploy Edge Functions using pure JavaScript.

Save your Function as a JavaScript file (e.g. `index.js`) and then update the `supabase/config.toml` as follows:

<Admonition type="note">
  `entrypoint` is available only in Supabase CLI version 1.215.0 or higher.
</Admonition>

```toml supabase/config.toml
[functions.hello-world]

# other entries
entrypoint = './functions/hello-world/index.js' # path must be relative to config.toml
```

You can use any `.ts`, `.js`, `.tsx`, `.jsx` or `.mjs` file as the `entrypoint` for a Function.


### Error handling

The `supabase-js` library provides several error types that you can use to handle errors that might occur when invoking Edge Functions:

```js
import { FunctionsHttpError, FunctionsRelayError, FunctionsFetchError } from '@supabase/supabase-js'

const { data, error } = await supabase.functions.invoke('hello', {
  headers: { 'my-custom-header': 'my-custom-header-value' },
  body: { foo: 'bar' },
})

if (error instanceof FunctionsHttpError) {
  const errorMessage = await error.context.json()
  console.log('Function returned an error', errorMessage)
} else if (error instanceof FunctionsRelayError) {
  console.log('Relay error:', error.message)
} else if (error instanceof FunctionsFetchError) {
  console.log('Fetch error:', error.message)
}
```


### Database Functions vs Edge Functions

For data-intensive operations we recommend using [Database Functions](/docs/guides/database/functions), which are executed within your database and can be called remotely using the [REST and GraphQL API](/docs/guides/api).

For use-cases which require low-latency we recommend [Edge Functions](/docs/guides/functions), which are globally-distributed and can be written in TypeScript.



# File Storage

Use persistent and ephemeral file storage

Edge Functions provides two flavors of file storage:

*   Persistent - backed by S3 protocol, can read/write from any S3 compatible bucket, including Supabase Storage
*   Ephemeral - You can read and write files to the `/tmp` directory. Only suitable for temporary operations

You can use file storage to:

*   Handle complex file transformations and workflows
*   Do data migrations between projects
*   Process user uploaded files and store them
*   Unzip archives and process contents before saving to database

***



## Persistent Storage

The persistent storage option is built on top of the S3 protocol. It allows you to mount any S3-compatible bucket, including Supabase Storage Buckets, as a directory for your Edge Functions.
You can perform operations such as reading and writing files to the mounted buckets as you would in a POSIX file system.

To access an S3 bucket from Edge Functions, you must set the following for environment variables in Edge Function Secrets.

*   `S3FS_ENDPOINT_URL`
*   `S3FS_REGION`
*   `S3FS_ACCESS_KEY_ID`
*   `S3FS_SECRET_ACCESS_KEY`

[Follow this guide](/docs/guides/storage/s3/authentication) to enable and create an access key for Supabase Storage S3.

To access a file path in your mounted bucket from your Edge Function, use the prefix `/s3/YOUR-BUCKET-NAME`.

```tsx
// read from S3 bucket
const data = await Deno.readFile('/s3/my-bucket/results.csv')

// make a directory
await Deno.mkdir('/s3/my-bucket/sub-dir')

// write to S3 bucket
await Deno.writeTextFile('/s3/my-bucket/demo.txt', 'hello world')
```



## Ephemeral storage

Ephemeral storage will reset on each function invocation. This means the files you write during an invocation can only be read within the same invocation.

You can use [Deno File System APIs](https://docs.deno.com/api/deno/file-system) or the [`node:fs`](https://docs.deno.com/api/node/fs/) module to access the `/tmp` path.

```tsx
Deno.serve(async (req) => {
  if (req.headers.get('content-type') !== 'application/zip') {
    return new Response('file must be a zip file', {
      status: 400,
    })
  }

  const uploadId = crypto.randomUUID()
  await Deno.writeFile('/tmp/' + uploadId, req.body)

  // E.g. extract and process the zip file
  const zipFile = await Deno.readFile('/tmp/' + uploadId)
  // You could use a zip library to extract contents
  const extracted = await extractZip(zipFile)

  // Or process the file directly
  console.log(`Processing zip file: ${uploadId}, size: ${zipFile.length} bytes`)
})
```

***



## Common use cases


### Archive processing with background tasks

You can use ephemeral storage with [Background Tasks](/docs/guides/functions/background-tasks) to handle large file processing operations that exceed memory limits.

Imagine you have a Photo Album application that accepts photo uploads as zip files. A streaming implementation will run into memory limit errors with zip files exceeding 100MB, as it retains all archive files in memory simultaneously.

You can write the zip file to ephemeral storage first, then use a background task to extract and upload files to Supabase Storage. This way, you only read parts of the zip file to the memory.

```tsx
import { BlobWriter, ZipReader } from 'https://deno.land/x/zipjs/index.js'
import { createClient } from 'jsr:@supabase/supabase-js@2'

const supabase = createClient(
  Deno.env.get('SUPABASE_URL'),
  Deno.env.get('SUPABASE_SERVICE_ROLE_KEY')
)

async function processZipFile(uploadId: string, filepath: string) {
  const file = await Deno.open(filepath, { read: true })
  const zipReader = new ZipReader(file.readable)
  const entries = await zipReader.getEntries()

  await supabase.storage.createBucket(uploadId, { public: false })

  await Promise.all(
    entries.map(async (entry) => {
      if (entry.directory) return

      // Read file entry from temp storage
      const blobWriter = new BlobWriter()
      const blob = await entry.getData(blobWriter)

      // Upload to permanent storage
      await supabase.storage.from(uploadId).upload(entry.filename, blob)

      console.log('uploaded', entry.filename)
    })
  )

  await zipReader.close()
}

Deno.serve(async (req) => {
  const uploadId = crypto.randomUUID()
  const filepath = `/tmp/${uploadId}.zip`

  // Write zip to ephemeral storage
  await Deno.writeFile(filepath, req.body)

  // Process in background to avoid memory limits
  EdgeRuntime.waitUntil(processZipFile(uploadId, filepath))

  return new Response(JSON.stringify({ uploadId }), {
    headers: { 'Content-Type': 'application/json' },
  })
})
```


### Image manipulation

Custom image manipulation workflows using [`magick-wasm`](/docs/guides/functions/examples/image-manipulation).

```tsx
Deno.serve(async (req) => {
  // Save uploaded image to temp storage
  const imagePath = `/tmp/input-${crypto.randomUUID()}.jpg`
  await Deno.writeFile(imagePath, req.body)

  // Process image with magick-wasm
  const processedPath = `/tmp/output-${crypto.randomUUID()}.jpg`
  // ... image manipulation logic

  // Read processed image and return
  const processedImage = await Deno.readFile(processedPath)
  return new Response(processedImage, {
    headers: { 'Content-Type': 'image/jpeg' },
  })
})
```

***



## Using synchronous file APIs

You can safely use the following synchronous Deno APIs (and their Node counterparts) *during initial script evaluation*:

*   Deno.statSync
*   Deno.removeSync
*   Deno.writeFileSync
*   Deno.writeTextFileSync
*   Deno.readFileSync
*   Deno.readTextFileSync
*   Deno.mkdirSync
*   Deno.makeTempDirSync
*   Deno.readDirSync

**Keep in mind** that the sync APIs are available only during initial script evaluation and aren’t supported in callbacks like HTTP handlers or `setTimeout`.

```tsx
Deno.statSync('...') // ✅

setTimeout(() => {
  Deno.statSync('...') // 💣 ERROR! Deno.statSync is blocklisted on the current context
})

Deno.serve(() => {
  Deno.statSync('...') // 💣 ERROR! Deno.statSync is blocklisted on the current context
})
```

***



## Limits

There are no limits on S3 buckets you mount for Persistent storage.

Ephemeral Storage:

*   Free projects: Up to 256MB of ephemeral storage
*   Paid projects: Up to 512MB of ephemeral storage



# Error Handling

Implement proper error responses and client-side handling to create reliable applications.


## Error handling

Implementing the right error responses and client-side handling helps with debugging and makes your functions much easier to maintain in production.

Within your Edge Functions, return proper HTTP status codes and error messages:

```tsx
Deno.serve(async (req) => {
  try {
    // Your function logic here
    const result = await processRequest(req)
    return new Response(JSON.stringify(result), {
      headers: { 'Content-Type': 'application/json' },
      status: 200,
    })
  } catch (error) {
    console.error('Function error:', error)
    return new Response(JSON.stringify({ error: error.message }), {
      headers: { 'Content-Type': 'application/json' },
      status: 500,
    })
  }
})
```

**Best practices for function errors:**

*   Use the right HTTP status code for each situation. Return `400` for bad user input, 404 when something doesn't exist, 500 for server errors, etc. This helps with debugging and lets client apps handle different error types appropriately.
*   Include helpful error messages in the response body
*   Log errors to the console for debugging (visible in the Logs tab)

***



## Client-side error handling

Within your client-side code, an Edge Function can throw three types of errors:

*   **`FunctionsHttpError`**: Your function executed but returned an error (4xx/5xx status)
*   **`FunctionsRelayError`**: Network issue between client and Supabase
*   **`FunctionsFetchError`**: Function couldn't be reached at all

```jsx
import { FunctionsHttpError, FunctionsRelayError, FunctionsFetchError } from '@supabase/supabase-js'

const { data, error } = await supabase.functions.invoke('hello', {
  headers: { 'my-custom-header': 'my-custom-header-value' },
  body: { foo: 'bar' },
})

if (error instanceof FunctionsHttpError) {
  const errorMessage = await error.context.json()
  console.log('Function returned an error', errorMessage)
} else if (error instanceof FunctionsRelayError) {
  console.log('Relay error:', error.message)
} else if (error instanceof FunctionsFetchError) {
  console.log('Fetch error:', error.message)
}
```

Make sure to handle the errors properly. Functions that fail silently are hard to debug, functions with clear error messages get fixed fast.

***



## Error monitoring

You can see the production error logs in the Logs tab of your Supabase Dashboard.

![Function invocations.](/docs/img/guides/functions/function-logs.png)

For more information on Logging, check out [this guide](/docs/guides/functions/logging).



# Function Configuration

Configure individual function behavior. Customize authentication, dependencies, and other settings per function.


## Configuration

By default, all your Edge Functions have the same settings. In real applications, however, you might need different behaviors between functions.

For example:

*   **Stripe webhooks** need to be publicly accessible (Stripe doesn't have your user tokens)
*   **User profile APIs** should require authentication
*   **Some functions** might need special dependencies or different file types

To enable these per-function rules, create `supabase/config.toml` in your project root:

```toml

# Disables authentication for the Stripe webhook.
[functions.stripe-webhook]
verify_jwt = false


# Custom dependencies for this specific function
[functions.image-processor]
import_map = './functions/image-processor/import_map.json'


# Custom entrypoint for legacy function using JavaScript
[functions.legacy-processor]
entrypoint = './functions/legacy-processor/index.js
```

This configuration tell Supabase that the `stripe-webhook` function doesn't require a valid JWT, the `image-processor` function uses a custom import map, and `legacy-processor` uses a custom entrypoint.

You set these rules once and never worry about them again. Deploy your functions knowing that the security and behavior is exactly what each endpoint needs.

<Admonition type="note">
  To see more general `config.toml` options, check out [this guide](/docs/guides/local-development/managing-config).
</Admonition>

***



## Skipping authorization checks

By default, Edge Functions require a valid JWT in the authorization header. If you want to use Edge Functions without Authorization checks (commonly used for Stripe webhooks), you can configure this in your `config.toml`:

```toml
[functions.stripe-webhook]
verify_jwt = false
```

You can also pass the `--no-verify-jwt` flag when serving your Edge Functions locally:

```bash
supabase functions serve hello-world --no-verify-jwt
```

<Admonition type="caution">
  Be careful when using this flag, as it will allow anyone to invoke your Edge Function without a valid JWT. The Supabase client libraries automatically handle authorization.
</Admonition>

***



## Custom entrypoints

<Admonition type="note">
  `entrypoint` is available only in Supabase CLI version 1.215.0 or higher.
</Admonition>

When you create a new Edge Function, it will use TypeScript by default. However, it is possible to write and deploy Edge Functions using pure JavaScript.

Save your Function as a JavaScript file (e.g. `index.js`) update the `supabase/config.toml` :

```toml
[functions.hello-world]
entrypoint = './index.js' # path must be relative to config.toml
```

You can use any `.ts`, `.js`, `.tsx`, `.jsx` or `.mjs` file as the entrypoint for a Function.



# Routing

Handle different request types in a single function to create efficient APIs.


## Overview

Edge Functions support **`GET`, `POST`, `PUT`, `PATCH`, `DELETE`, and `OPTIONS`**. This means you can build complete REST APIs in a single function:

```tsx
Deno.serve(async (req) => {
  const { method, url } = req
  const { pathname } = new URL(url)

  // Route based on method and path
  if (method === 'GET' && pathname === '/users') {
    return getAllUsers()
  } else if (method === 'POST' && pathname === '/users') {
    return createUser(req)
  }

  return new Response('Not found', { status: 404 })
})
```

Edge Functions allow you to build APIs without needing separate functions for each endpoint. This reduces cold starts and simplifies deployment while keeping your code organized.

<Admonition type="note">
  HTML content is not supported. `GET` requests that return `text/html` will be rewritten to `text/plain`. Edge Functions are designed for APIs and data processing, not serving web pages. Use Supabase for your backend API and your favorite frontend framework for HTML.
</Admonition>

***



## Example

Here's a full example of a RESTful API built with Edge Functions.

<CodeSampleWrapper source="https://github.com/supabase/supabase/blob/2415776436927dedb360dae082d03caee607891a/examples/edge-functions/supabase/functions/restful-tasks/index.ts">
  ```typescript index.ts
  // Follow this setup guide to integrate the Deno language server with your editor:
  // https://deno.land/manual/getting_started/setup_your_environment
  // This enables autocomplete, go to definition, etc.

  import { createClient, SupabaseClient } from 'npm:supabase-js@2'

  const corsHeaders = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Headers': 'authorization, x-client-info, apikey',
    'Access-Control-Allow-Methods': 'POST, GET, OPTIONS, PUT, DELETE',
  }

  interface Task {
    name: string
    status: number
  }

  async function getTask(supabaseClient: SupabaseClient, id: string) {
    const { data: task, error } = await supabaseClient.from('tasks').select('*').eq('id', id)
    if (error) throw error

    return new Response(JSON.stringify({ task }), {
      headers: { ...corsHeaders, 'Content-Type': 'application/json' },
      status: 200,
    })
  }

  async function getAllTasks(supabaseClient: SupabaseClient) {
    const { data: tasks, error } = await supabaseClient.from('tasks').select('*')
    if (error) throw error

    return new Response(JSON.stringify({ tasks }), {
      headers: { ...corsHeaders, 'Content-Type': 'application/json' },
      status: 200,
    })
  }

  async function deleteTask(supabaseClient: SupabaseClient, id: string) {
    const { error } = await supabaseClient.from('tasks').delete().eq('id', id)
    if (error) throw error

    return new Response(JSON.stringify({}), {
      headers: { ...corsHeaders, 'Content-Type': 'application/json' },
      status: 200,
    })
  }

  async function updateTask(supabaseClient: SupabaseClient, id: string, task: Task) {
    const { error } = await supabaseClient.from('tasks').update(task).eq('id', id)
    if (error) throw error

    return new Response(JSON.stringify({ task }), {
      headers: { ...corsHeaders, 'Content-Type': 'application/json' },
      status: 200,
    })
  }

  async function createTask(supabaseClient: SupabaseClient, task: Task) {
    const { error } = await supabaseClient.from('tasks').insert(task)
    if (error) throw error

    return new Response(JSON.stringify({ task }), {
      headers: { ...corsHeaders, 'Content-Type': 'application/json' },
      status: 200,
    })
  }

  Deno.serve(async (req) => {
    const { url, method } = req

    // This is needed if you're planning to invoke your function from a browser.
    if (method === 'OPTIONS') {
      return new Response('ok', { headers: corsHeaders })
    }

    try {
      // Create a Supabase client with the Auth context of the logged in user.
      const supabaseClient = createClient(
        // Supabase API URL - env var exported by default.
        Deno.env.get('SUPABASE_URL') ?? '',
        // Supabase API ANON KEY - env var exported by default.
        Deno.env.get('SUPABASE_ANON_KEY') ?? '',
        // Create client with Auth context of the user that called the function.
        // This way your row-level-security (RLS) policies are applied.
        {
          global: {
            headers: { Authorization: req.headers.get('Authorization')! },
          },
        }
      )

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
      }
    } catch (error) {
      console.error(error)

      return new Response(JSON.stringify({ error: error.message }), {
        headers: { ...corsHeaders, 'Content-Type': 'application/json' },
        status: 400,
      })
    }
  })
  ```
</CodeSampleWrapper>



---
**Navigation:** [← Previous](./17-build-a-user-management-app-with-vue-3.md) | [Index](./index.md) | [Next →](./19-type-safe-sql-with-kysely.md)
