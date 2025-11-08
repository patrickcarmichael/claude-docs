**Navigation:** [← Previous](./19-type-safe-sql-with-kysely.md) | [Index](./index.md) | [Next →](./21-production-checklist.md)

# Custom Auth Emails with React Email and Resend



Use the [send email hook](/docs/guides/auth/auth-hooks/send-email-hook?queryGroups=language\&language=http) to send custom auth emails with [React Email](https://react.email/) and [Resend](https://resend.com/) in Supabase Edge Functions.

<Admonition type="note">
  Prefer to jump straight to the code? [Check out the example on GitHub](https://github.com/supabase/supabase/tree/master/examples/edge-functions/supabase/functions/auth-hook-react-email-resend).
</Admonition>


### Prerequisites

To get the most out of this guide, you’ll need to:

*   [Create a Resend API key](https://resend.com/api-keys)
*   [Verify your domain](https://resend.com/domains)

Make sure you have the latest version of the [Supabase CLI](/docs/guides/cli#installation) installed.


### 1. Create Supabase function

Create a new function locally:

```bash
supabase functions new send-email
```


### 2. Edit the handler function

Paste the following code into the `index.ts` file:

```tsx supabase/functions/send-email/index.ts
import React from 'npm:react@18.3.1'
import { Webhook } from 'https://esm.sh/standardwebhooks@1.0.0'
import { Resend } from 'npm:resend@4.0.0'
import { renderAsync } from 'npm:@react-email/components@0.0.22'
import { MagicLinkEmail } from './_templates/magic-link.tsx'

const resend = new Resend(Deno.env.get('RESEND_API_KEY') as string)
const hookSecret = Deno.env.get('SEND_EMAIL_HOOK_SECRET') as string

Deno.serve(async (req) => {
  if (req.method !== 'POST') {
    return new Response('not allowed', { status: 400 })
  }

  const payload = await req.text()
  const headers = Object.fromEntries(req.headers)
  const wh = new Webhook(hookSecret)
  try {
    const {
      user,
      email_data: { token, token_hash, redirect_to, email_action_type },
    } = wh.verify(payload, headers) as {
      user: {
        email: string
      }
      email_data: {
        token: string
        token_hash: string
        redirect_to: string
        email_action_type: string
        site_url: string
        token_new: string
        token_hash_new: string
      }
    }

    const html = await renderAsync(
      React.createElement(MagicLinkEmail, {
        supabase_url: Deno.env.get('SUPABASE_URL') ?? '',
        token,
        token_hash,
        redirect_to,
        email_action_type,
      })
    )

    const { error } = await resend.emails.send({
      from: 'welcome <onboarding@resend.dev>',
      to: [user.email],
      subject: 'Supa Custom MagicLink!',
      html,
    })
    if (error) {
      throw error
    }
  } catch (error) {
    console.log(error)
    return new Response(
      JSON.stringify({
        error: {
          http_code: error.code,
          message: error.message,
        },
      }),
      {
        status: 401,
        headers: { 'Content-Type': 'application/json' },
      }
    )
  }

  const responseHeaders = new Headers()
  responseHeaders.set('Content-Type', 'application/json')
  return new Response(JSON.stringify({}), {
    status: 200,
    headers: responseHeaders,
  })
})
```


### 3. Create React Email templates

Create a new folder `_templates` and create a new file `magic-link.tsx` with the following code:

```tsx supabase/functions/send-email/_templates/magic-link.tsx
import {
  Body,
  Container,
  Head,
  Heading,
  Html,
  Link,
  Preview,
  Text,
} from 'npm:@react-email/components@0.0.22'
import * as React from 'npm:react@18.3.1'

interface MagicLinkEmailProps {
  supabase_url: string
  email_action_type: string
  redirect_to: string
  token_hash: string
  token: string
}

export const MagicLinkEmail = ({
  token,
  supabase_url,
  email_action_type,
  redirect_to,
  token_hash,
}: MagicLinkEmailProps) => (
  <Html>
    <Head />
    <Preview>Log in with this magic link</Preview>
    <Body style={main}>
      <Container style={container}>
        <Heading style={h1}>Login</Heading>
        <Link
          href={`${supabase_url}/auth/v1/verify?token=${token_hash}&type=${email_action_type}&redirect_to=${redirect_to}`}
          target="_blank"
          style={{
            ...link,
            display: 'block',
            marginBottom: '16px',
          }}
        >
          Click here to log in with this magic link
        </Link>
        <Text style={{ ...text, marginBottom: '14px' }}>
          Or, copy and paste this temporary login code:
        </Text>
        <code style={code}>{token}</code>
        <Text
          style={{
            ...text,
            color: '#ababab',
            marginTop: '14px',
            marginBottom: '16px',
          }}
        >
          If you didn&apos;t try to login, you can safely ignore this email.
        </Text>
        <Text style={footer}>
          <Link
            href="https://demo.vercel.store/"
            target="_blank"
            style={{ ...link, color: '#898989' }}
          >
            ACME Corp
          </Link>
          , the famouse demo corp.
        </Text>
      </Container>
    </Body>
  </Html>
)

export default MagicLinkEmail

const main = {
  backgroundColor: '#ffffff',
}

const container = {
  paddingLeft: '12px',
  paddingRight: '12px',
  margin: '0 auto',
}

const h1 = {
  color: '#333',
  fontFamily:
    "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue', sans-serif",
  fontSize: '24px',
  fontWeight: 'bold',
  margin: '40px 0',
  padding: '0',
}

const link = {
  color: '#2754C5',
  fontFamily:
    "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue', sans-serif",
  fontSize: '14px',
  textDecoration: 'underline',
}

const text = {
  color: '#333',
  fontFamily:
    "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue', sans-serif",
  fontSize: '14px',
  margin: '24px 0',
}

const footer = {
  color: '#898989',
  fontFamily:
    "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue', sans-serif",
  fontSize: '12px',
  lineHeight: '22px',
  marginTop: '12px',
  marginBottom: '24px',
}

const code = {
  display: 'inline-block',
  padding: '16px 4.5%',
  width: '90.5%',
  backgroundColor: '#f4f4f4',
  borderRadius: '5px',
  border: '1px solid #eee',
  color: '#333',
}
```

<Admonition type="note">
  You can find a selection of React Email templates in the [React Email Examples](https://react.email/examples).
</Admonition>


### 4. Deploy the Function

Deploy function to Supabase:

```bash
supabase functions deploy send-email --no-verify-jwt
```

Note down the function URL, you will need it in the next step!


### 5. Configure the Send Email Hook

*   Go to the [Auth Hooks](/dashboard/project/_/auth/hooks) section of the Supabase dashboard and create a new "Send Email hook".
*   Select HTTPS as the hook type.
*   Paste the function URL in the "URL" field.
*   Click "Generate Secret" to generate your webhook secret and note it down.
*   Click "Create" to save the hook configuration.

Store these secrets in your `.env` file.

```bash supabase/functions/.env
RESEND_API_KEY=your_resend_api_key
SEND_EMAIL_HOOK_SECRET=<base64_secret>
```

<Admonition type="note">
  You can generate the secret in the [Auth Hooks](/dashboard/project/_/auth/hooks) section of the Supabase dashboard. Make sure to remove the `v1,whsec_` prefix!
</Admonition>

Set the secrets from the `.env` file:

```bash
supabase secrets set --env-file supabase/functions/.env
```

Now your Supabase Edge Function will be triggered anytime an Auth Email needs to be sent to the user!



## More resources

*   [Send Email Hooks](/docs/guides/auth/auth-hooks/send-email-hook)
*   [Auth Hooks](/docs/guides/auth/auth-hooks)



# CAPTCHA support with Cloudflare Turnstile



[Cloudflare Turnstile](https://www.cloudflare.com/products/turnstile/) is a friendly, free CAPTCHA replacement, and it works seamlessly with Supabase Edge Functions to protect your forms. [View on GitHub](https://github.com/supabase/supabase/tree/master/examples/edge-functions/supabase/functions/cloudflare-turnstile).



## Setup

*   Follow these steps to set up a new site: [https://developers.cloudflare.com/turnstile/get-started/](https://developers.cloudflare.com/turnstile/get-started/)
*   Add the Cloudflare Turnstile widget to your site: [https://developers.cloudflare.com/turnstile/get-started/client-side-rendering/](https://developers.cloudflare.com/turnstile/get-started/client-side-rendering/)



## Code

Create a new function in your project:

```bash
supabase functions new cloudflare-turnstile
```

And add the code to the `index.ts` file:

```ts index.ts
import { corsHeaders } from '../_shared/cors.ts'

console.log('Hello from Cloudflare Trunstile!')

function ips(req: Request) {
  return req.headers.get('x-forwarded-for')?.split(/\s*,\s*/)
}

Deno.serve(async (req) => {
  // This is needed if you're planning to invoke your function from a browser.
  if (req.method === 'OPTIONS') {
    return new Response('ok', { headers: corsHeaders })
  }

  const { token } = await req.json()
  const clientIps = ips(req) || ['']
  const ip = clientIps[0]

  // Validate the token by calling the
  // "/siteverify" API endpoint.
  let formData = new FormData()
  formData.append('secret', Deno.env.get('CLOUDFLARE_SECRET_KEY') ?? '')
  formData.append('response', token)
  formData.append('remoteip', ip)

  const url = 'https://challenges.cloudflare.com/turnstile/v0/siteverify'
  const result = await fetch(url, {
    body: formData,
    method: 'POST',
  })

  const outcome = await result.json()
  console.log(outcome)
  if (outcome.success) {
    return new Response('success', { headers: corsHeaders })
  }
  return new Response('failure', { headers: corsHeaders })
})
```



## Deploy the server-side validation Edge Functions

*   [https://developers.cloudflare.com/turnstile/get-started/server-side-validation/](https://developers.cloudflare.com/turnstile/get-started/server-side-validation/)

```bash
supabase functions deploy cloudflare-turnstile
supabase secrets set CLOUDFLARE_SECRET_KEY=your_secret_key
```



## Invoke the function from your site

```js
const { data, error } = await supabase.functions.invoke('cloudflare-turnstile', {
  body: { token },
})
```



# Building a Discord Bot



<div class="video-container">
  <iframe src="https://www.youtube-nocookie.com/embed/J24Bvo_m7DM" frameBorder="1" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />
</div>



## Create an application on Discord Developer portal

1.  Go to [https://discord.com/developers/applications](https://discord.com/developers/applications) (login using your discord account if required).
2.  Click on **New Application** button available at left side of your profile picture.
3.  Name your application and click on **Create**.
4.  Go to **Bot** section, click on **Add Bot**, and finally on **Yes, do it!** to confirm.

A new application is created which will hold our Slash Command. Don't close the tab as we need information from this application page throughout our development.

Before we can write some code, we need to curl a discord endpoint to register a Slash Command in our app.

Fill `DISCORD_BOT_TOKEN` with the token available in the **Bot** section and `CLIENT_ID` with the ID available on the **General Information** section of the page and run the command on your terminal.

```bash
BOT_TOKEN='replace_me_with_bot_token'
CLIENT_ID='replace_me_with_client_id'
curl -X POST \
-H 'Content-Type: application/json' \
-H "Authorization: Bot $BOT_TOKEN" \
-d '{"name":"hello","description":"Greet a person","options":[{"name":"name","description":"The name of the person","type":3,"required":true}]}' \
"https://discord.com/api/v8/applications/$CLIENT_ID/commands"
```

This will register a Slash Command named `hello` that accepts a parameter named `name` of type string.



## Code

```ts index.ts
// Sift is a small routing library that abstracts away details like starting a
// listener on a port, and provides a simple function (serve) that has an API
// to invoke a function for a specific path.
import { json, serve, validateRequest } from 'https://deno.land/x/sift@0.6.0/mod.ts'
// TweetNaCl is a cryptography library that we use to verify requests
// from Discord.
import nacl from 'https://cdn.skypack.dev/tweetnacl@v1.0.3?dts'

enum DiscordCommandType {
  Ping = 1,
  ApplicationCommand = 2,
}

// For all requests to "/" endpoint, we want to invoke home() handler.
serve({
  '/discord-bot': home,
})

// The main logic of the Discord Slash Command is defined in this function.
async function home(request: Request) {
  // validateRequest() ensures that a request is of POST method and
  // has the following headers.
  const { error } = await validateRequest(request, {
    POST: {
      headers: ['X-Signature-Ed25519', 'X-Signature-Timestamp'],
    },
  })
  if (error) {
    return json({ error: error.message }, { status: error.status })
  }

  // verifySignature() verifies if the request is coming from Discord.
  // When the request's signature is not valid, we return a 401 and this is
  // important as Discord sends invalid requests to test our verification.
  const { valid, body } = await verifySignature(request)
  if (!valid) {
    return json(
      { error: 'Invalid request' },
      {
        status: 401,
      }
    )
  }

  const { type = 0, data = { options: [] } } = JSON.parse(body)
  // Discord performs Ping interactions to test our application.
  // Type 1 in a request implies a Ping interaction.
  if (type === DiscordCommandType.Ping) {
    return json({
      type: 1, // Type 1 in a response is a Pong interaction response type.
    })
  }

  // Type 2 in a request is an ApplicationCommand interaction.
  // It implies that a user has issued a command.
  if (type === DiscordCommandType.ApplicationCommand) {
    const { value } = data.options.find(
      (option: { name: string; value: string }) => option.name === 'name'
    )
    return json({
      // Type 4 responds with the below message retaining the user's
      // input at the top.
      type: 4,
      data: {
        content: `Hello, ${value}!`,
      },
    })
  }

  // We will return a bad request error as a valid Discord request
  // shouldn't reach here.
  return json({ error: 'bad request' }, { status: 400 })
}

/** Verify whether the request is coming from Discord. */
async function verifySignature(request: Request): Promise<{ valid: boolean; body: string }> {
  const PUBLIC_KEY = Deno.env.get('DISCORD_PUBLIC_KEY')!
  // Discord sends these headers with every request.
  const signature = request.headers.get('X-Signature-Ed25519')!
  const timestamp = request.headers.get('X-Signature-Timestamp')!
  const body = await request.text()
  const valid = nacl.sign.detached.verify(
    new TextEncoder().encode(timestamp + body),
    hexToUint8Array(signature),
    hexToUint8Array(PUBLIC_KEY)
  )

  return { valid, body }
}

/** Converts a hexadecimal string to Uint8Array. */
function hexToUint8Array(hex: string) {
  return new Uint8Array(hex.match(/.{1,2}/g)!.map((val) => parseInt(val, 16)))
}
```



## Deploy the slash command handler

```bash
supabase functions deploy discord-bot --no-verify-jwt
supabase secrets set DISCORD_PUBLIC_KEY=your_public_key
```

Navigate to your Function details in the Supabase Dashboard to get your Endpoint URL.


### Configure Discord application to use our URL as interactions endpoint URL

1.  Go back to your application (Greeter) page on Discord Developer Portal
2.  Fill **INTERACTIONS ENDPOINT URL** field with the URL and click on **Save Changes**.

The application is now ready. Let's proceed to the next section to install it.



## Install the slash command on your Discord server

So to use the `hello` Slash Command, we need to install our Greeter application on our Discord server. Here are the steps:

1.  Go to **OAuth2** section of the Discord application page on Discord Developer Portal
2.  Select `applications.commands` scope and click on the **Copy** button below.
3.  Now paste and visit the URL on your browser. Select your server and click on **Authorize**.

Open Discord, type `/Promise` and press **Enter**.



## Run locally

```bash
supabase functions serve discord-bot --no-verify-jwt --env-file ./supabase/.env.local
ngrok http 54321
```



# Streaming Speech with ElevenLabs

Generate and stream speech through Supabase Edge Functions. Store speech in Supabase Storage and cache responses via built-in CDN.


## Introduction

In this tutorial you will learn how to build an edge API to generate, stream, store, and cache speech using Supabase Edge Functions, Supabase Storage, and [ElevenLabs text to speech API](https://elevenlabs.io/text-to-speech).

<Admonition type="tip">
  Find the [example project on GitHub](https://github.com/elevenlabs/elevenlabs-examples/tree/main/examples/text-to-speech/supabase/stream-and-cache-storage).
</Admonition>



## Requirements

*   An ElevenLabs account with an [API key](/app/settings/api-keys).
*   A [Supabase](https://supabase.com) account (you can sign up for a free account via [database.new](https://database.new)).
*   The [Supabase CLI](/docs/guides/local-development) installed on your machine.
*   The [Deno runtime](https://docs.deno.com/runtime/getting_started/installation/) installed on your machine and optionally [setup in your favourite IDE](https://docs.deno.com/runtime/getting_started/setup_your_environment).



## Setup


### Create a Supabase project locally

After installing the [Supabase CLI](/docs/guides/local-development), run the following command to create a new Supabase project locally:

```bash
supabase init
```


### Configure the storage bucket

You can configure the Supabase CLI to automatically generate a storage bucket by adding this configuration in the `config.toml` file:

```toml ./supabase/config.toml
[storage.buckets.audio]
public = false
file_size_limit = "50MiB"
allowed_mime_types = ["audio/mp3"]
objects_path = "./audio"
```

<Admonition type="tip">
  Upon running `supabase start` this will create a new storage bucket in your local Supabase project. Should you want to push this to your hosted Supabase project, you can run `supabase seed buckets --linked`.
</Admonition>


### Configure background tasks for Supabase Edge Functions

To use background tasks in Supabase Edge Functions when developing locally, you need to add the following configuration in the `config.toml` file:

```toml ./supabase/config.toml
[edge_runtime]
policy = "per_worker"
```

<Admonition type="tip">
  When running with `per_worker` policy, Function won't auto-reload on edits. You will need to manually restart it by running `supabase functions serve`.
</Admonition>


### Create a Supabase Edge Function for speech generation

Create a new Edge Function by running the following command:

```bash
supabase functions new text-to-speech
```

If you're using VS Code or Cursor, select `y` when the CLI prompts "Generate VS Code settings for Deno? \[y/N]"!


### Set up the environment variables

Within the `supabase/functions` directory, create a new `.env` file and add the following variables:

```env supabase/functions/.env

# Find / create an API key at https://elevenlabs.io/app/settings/api-keys
ELEVENLABS_API_KEY=your_api_key
```


### Dependencies

The project uses a couple of dependencies:

*   The [@supabase/supabase-js](/docs/reference/javascript) library to interact with the Supabase database.
*   The ElevenLabs [JavaScript SDK](/docs/quickstart) to interact with the text-to-speech API.
*   The open-source [object-hash](https://www.npmjs.com/package/object-hash) to generate a hash from the request parameters.

Since Supabase Edge Function uses the [Deno runtime](https://deno.land/), you don't need to install the dependencies, rather you can [import](https://docs.deno.com/examples/npm/) them via the `npm:` prefix.



## Code the Supabase Edge Function

In your newly created `supabase/functions/text-to-speech/index.ts` file, add the following code:

```ts supabase/functions/text-to-speech/index.ts
// Setup type definitions for built-in Supabase Runtime APIs
import 'jsr:@supabase/functions-js/edge-runtime.d.ts'
import { createClient } from 'npm:@supabase/supabase-js@2'
import { ElevenLabsClient } from 'npm:elevenlabs@1.52.0'
import * as hash from 'npm:object-hash'

const supabase = createClient(
  Deno.env.get('SUPABASE_URL')!,
  Deno.env.get('SUPABASE_SERVICE_ROLE_KEY')!
)

const client = new ElevenLabsClient({
  apiKey: Deno.env.get('ELEVENLABS_API_KEY'),
})

// Upload audio to Supabase Storage in a background task
async function uploadAudioToStorage(stream: ReadableStream, requestHash: string) {
  const { data, error } = await supabase.storage
    .from('audio')
    .upload(`${requestHash}.mp3`, stream, {
      contentType: 'audio/mp3',
    })

  console.log('Storage upload result', { data, error })
}

Deno.serve(async (req) => {
  // To secure your function for production, you can for example validate the request origin,
  // or append a user access token and validate it with Supabase Auth.
  console.log('Request origin', req.headers.get('host'))
  const url = new URL(req.url)
  const params = new URLSearchParams(url.search)
  const text = params.get('text')
  const voiceId = params.get('voiceId') ?? 'JBFqnCBsd6RMkjVDRZzb'

  const requestHash = hash.MD5({ text, voiceId })
  console.log('Request hash', requestHash)

  // Check storage for existing audio file
  const { data } = await supabase.storage.from('audio').createSignedUrl(`${requestHash}.mp3`, 60)

  if (data) {
    console.log('Audio file found in storage', data)
    const storageRes = await fetch(data.signedUrl)
    if (storageRes.ok) return storageRes
  }

  if (!text) {
    return new Response(JSON.stringify({ error: 'Text parameter is required' }), {
      status: 400,
      headers: { 'Content-Type': 'application/json' },
    })
  }

  try {
    console.log('ElevenLabs API call')
    const response = await client.textToSpeech.convertAsStream(voiceId, {
      output_format: 'mp3_44100_128',
      model_id: 'eleven_multilingual_v2',
      text,
    })

    const stream = new ReadableStream({
      async start(controller) {
        for await (const chunk of response) {
          controller.enqueue(chunk)
        }
        controller.close()
      },
    })

    // Branch stream to Supabase Storage
    const [browserStream, storageStream] = stream.tee()

    // Upload to Supabase Storage in the background
    EdgeRuntime.waitUntil(uploadAudioToStorage(storageStream, requestHash))

    // Return the streaming response immediately
    return new Response(browserStream, {
      headers: {
        'Content-Type': 'audio/mpeg',
      },
    })
  } catch (error) {
    console.log('error', { error })
    return new Response(JSON.stringify({ error: error.message }), {
      status: 500,
      headers: { 'Content-Type': 'application/json' },
    })
  }
})
```



## Run locally

To run the function locally, run the following commands:

```bash
supabase start
```

Once the local Supabase stack is up and running, run the following command to start the function and observe the logs:

```bash
supabase functions serve
```


### Try it out

Navigate to `http://127.0.0.1:54321/functions/v1/text-to-speech?text=hello%20world` to hear the function in action.

Afterwards, navigate to `http://127.0.0.1:54323/project/default/storage/buckets/audio` to see the audio file in your local Supabase Storage bucket.



## Deploy to Supabase

If you haven't already, create a new Supabase account at [database.new](https://database.new) and link the local project to your Supabase account:

```bash
supabase link
```

Once done, run the following command to deploy the function:

```bash
supabase functions deploy
```


### Set the function secrets

Now that you have all your secrets set locally, you can run the following command to set the secrets in your Supabase project:

```bash
supabase secrets set --env-file supabase/functions/.env
```



## Test the function

The function is designed in a way that it can be used directly as a source for an `<audio>` element.

```html
<audio
  src="https://${SUPABASE_PROJECT_REF}.supabase.co/functions/v1/text-to-speech?text=Hello%2C%20world!&voiceId=JBFqnCBsd6RMkjVDRZzb"
  controls
/>
```

You can find an example frontend implementation in the complete code example on [GitHub](https://github.com/elevenlabs/elevenlabs-examples/tree/main/examples/text-to-speech/supabase/stream-and-cache-storage/src/pages/Index.tsx).



# Transcription Telegram Bot

Build a Telegram bot that transcribes audio and video messages in 99 languages using TypeScript with Deno in Supabase Edge Functions.


## Introduction

In this tutorial you will learn how to build a Telegram bot that transcribes audio and video messages in 99 languages using TypeScript and the ElevenLabs Scribe model via the [speech to text API](https://elevenlabs.io/speech-to-text).

To check out what the end result will look like, you can test out the [t.me/ElevenLabsScribeBot](https://t.me/ElevenLabsScribeBot)

<Admonition type="tip">
  Find the [example project on GitHub](https://github.com/elevenlabs/elevenlabs-examples/tree/main/examples/speech-to-text/telegram-transcription-bot).
</Admonition>



## Requirements

*   An ElevenLabs account with an [API key](/app/settings/api-keys).
*   A [Supabase](https://supabase.com) account (you can sign up for a free account via [database.new](https://database.new)).
*   The [Supabase CLI](/docs/guides/local-development) installed on your machine.
*   The [Deno runtime](https://docs.deno.com/runtime/getting_started/installation/) installed on your machine and optionally [setup in your favourite IDE](https://docs.deno.com/runtime/getting_started/setup_your_environment).
*   A [Telegram](https://telegram.org) account.



## Setup


### Register a Telegram bot

Use the [BotFather](https://t.me/BotFather) to create a new Telegram bot. Run the `/newbot` command and follow the instructions to create a new bot. At the end, you will receive your secret bot token. Note it down securely for the next step.

![BotFather](/docs/img/guides/functions/elevenlabs/bot-father.png)


### Create a Supabase project locally

After installing the [Supabase CLI](/docs/guides/local-development), run the following command to create a new Supabase project locally:

```bash
supabase init
```


### Create a database table to log the transcription results

Next, create a new database table to log the transcription results:

```bash
supabase migrations new init
```

This will create a new migration file in the `supabase/migrations` directory. Open the file and add the following SQL:

```sql supabase/migrations/init.sql
CREATE TABLE IF NOT EXISTS transcription_logs (
  id BIGSERIAL PRIMARY KEY,
  file_type VARCHAR NOT NULL,
  duration INTEGER NOT NULL,
  chat_id BIGINT NOT NULL,
  message_id BIGINT NOT NULL,
  username VARCHAR,
  transcript TEXT,
  language_code VARCHAR,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
  error TEXT
);

ALTER TABLE transcription_logs ENABLE ROW LEVEL SECURITY;
```


### Create a Supabase Edge Function to handle Telegram webhook requests

Next, create a new Edge Function to handle Telegram webhook requests:

```bash
supabase functions new scribe-bot
```

If you're using VS Code or Cursor, select `y` when the CLI prompts "Generate VS Code settings for Deno? \[y/N]"!


### Set up the environment variables

Within the `supabase/functions` directory, create a new `.env` file and add the following variables:

```env supabase/functions/.env

# Find / create an API key at https://elevenlabs.io/app/settings/api-keys
ELEVENLABS_API_KEY=your_api_key


# The bot token you received from the BotFather.
TELEGRAM_BOT_TOKEN=your_bot_token


# A random secret chosen by you to secure the function.
FUNCTION_SECRET=random_secret
```


### Dependencies

The project uses a couple of dependencies:

*   The open-source [grammY Framework](https://grammy.dev/) to handle the Telegram webhook requests.
*   The [@supabase/supabase-js](/docs/reference/javascript) library to interact with the Supabase database.
*   The ElevenLabs [JavaScript SDK](/docs/quickstart) to interact with the speech-to-text API.

Since Supabase Edge Function uses the [Deno runtime](https://deno.land/), you don't need to install the dependencies, rather you can [import](https://docs.deno.com/examples/npm/) them via the `npm:` prefix.



## Code the Telegram bot

In your newly created `scribe-bot/index.ts` file, add the following code:

```ts supabase/functions/scribe-bot/index.ts
import { Bot, webhookCallback } from 'https://deno.land/x/grammy@v1.34.0/mod.ts'
import 'jsr:@supabase/functions-js/edge-runtime.d.ts'
import { createClient } from 'npm:@supabase/supabase-js@2'
import { ElevenLabsClient } from 'npm:elevenlabs@1.50.5'

console.log(`Function "elevenlabs-scribe-bot" up and running!`)

const elevenLabsClient = new ElevenLabsClient({
  apiKey: Deno.env.get('ELEVENLABS_API_KEY') || '',
})

const supabase = createClient(
  Deno.env.get('SUPABASE_URL') || '',
  Deno.env.get('SUPABASE_SERVICE_ROLE_KEY') || ''
)

async function scribe({
  fileURL,
  fileType,
  duration,
  chatId,
  messageId,
  username,
}: {
  fileURL: string
  fileType: string
  duration: number
  chatId: number
  messageId: number
  username: string
}) {
  let transcript: string | null = null
  let languageCode: string | null = null
  let errorMsg: string | null = null
  try {
    const sourceFileArrayBuffer = await fetch(fileURL).then((res) => res.arrayBuffer())
    const sourceBlob = new Blob([sourceFileArrayBuffer], {
      type: fileType,
    })

    const scribeResult = await elevenLabsClient.speechToText.convert({
      file: sourceBlob,
      model_id: 'scribe_v1',
      tag_audio_events: false,
    })

    transcript = scribeResult.text
    languageCode = scribeResult.language_code

    // Reply to the user with the transcript
    await bot.api.sendMessage(chatId, transcript, {
      reply_parameters: { message_id: messageId },
    })
  } catch (error) {
    errorMsg = error.message
    console.log(errorMsg)
    await bot.api.sendMessage(chatId, 'Sorry, there was an error. Please try again.', {
      reply_parameters: { message_id: messageId },
    })
  }
  // Write log to Supabase.
  const logLine = {
    file_type: fileType,
    duration,
    chat_id: chatId,
    message_id: messageId,
    username,
    language_code: languageCode,
    error: errorMsg,
  }
  console.log({ logLine })
  await supabase.from('transcription_logs').insert({ ...logLine, transcript })
}

const telegramBotToken = Deno.env.get('TELEGRAM_BOT_TOKEN')
const bot = new Bot(telegramBotToken || '')
const startMessage = `Welcome to the ElevenLabs Scribe Bot\\! I can transcribe speech in 99 languages with super high accuracy\\!
    \nTry it out by sending or forwarding me a voice message, video, or audio file\\!
    \n[Learn more about Scribe](https://elevenlabs.io/speech-to-text) or [build your own bot](https://elevenlabs.io/docs/cookbooks/speech-to-text/telegram-bot)\\!
  `
bot.command('start', (ctx) => ctx.reply(startMessage.trim(), { parse_mode: 'MarkdownV2' }))

bot.on([':voice', ':audio', ':video'], async (ctx) => {
  try {
    const file = await ctx.getFile()
    const fileURL = `https://api.telegram.org/file/bot${telegramBotToken}/${file.file_path}`
    const fileMeta = ctx.message?.video ?? ctx.message?.voice ?? ctx.message?.audio

    if (!fileMeta) {
      return ctx.reply('No video|audio|voice metadata found. Please try again.')
    }

    // Run the transcription in the background.
    EdgeRuntime.waitUntil(
      scribe({
        fileURL,
        fileType: fileMeta.mime_type!,
        duration: fileMeta.duration,
        chatId: ctx.chat.id,
        messageId: ctx.message?.message_id!,
        username: ctx.from?.username || '',
      })
    )

    // Reply to the user immediately to let them know we received their file.
    return ctx.reply('Received. Scribing...')
  } catch (error) {
    console.error(error)
    return ctx.reply(
      'Sorry, there was an error getting the file. Please try again with a smaller file!'
    )
  }
})

const handleUpdate = webhookCallback(bot, 'std/http')

Deno.serve(async (req) => {
  try {
    const url = new URL(req.url)
    if (url.searchParams.get('secret') !== Deno.env.get('FUNCTION_SECRET')) {
      return new Response('not allowed', { status: 405 })
    }

    return await handleUpdate(req)
  } catch (err) {
    console.error(err)
  }
})
```



## Deploy to Supabase

If you haven't already, create a new Supabase account at [database.new](https://database.new) and link the local project to your Supabase account:

```bash
supabase link
```


### Apply the database migrations

Run the following command to apply the database migrations from the `supabase/migrations` directory:

```bash
supabase db push
```

Navigate to the [table editor](/dashboard/project/_/editor) in your Supabase dashboard and you should see and empty `transcription_logs` table.

![Empty table](/docs/img/guides/functions/elevenlabs/supa-empty-table.png)

Lastly, run the following command to deploy the Edge Function:

```bash
supabase functions deploy --no-verify-jwt scribe-bot
```

Navigate to the [Edge Functions view](/dashboard/project/_/functions) in your Supabase dashboard and you should see the `scribe-bot` function deployed. Make a note of the function URL as you'll need it later, it should look something like `https://<project-ref>.functions.supabase.co/scribe-bot`.

![Edge Function deployed](/docs/img/guides/functions/elevenlabs/supa-edge-function-deployed.png)


### Set up the webhook

Set your bot's webhook URL to `https://<PROJECT_REFERENCE>.functions.supabase.co/telegram-bot` (Replacing `<...>` with respective values). In order to do that, run a GET request to the following URL (in your browser, for example):

```
https://api.telegram.org/bot<TELEGRAM_BOT_TOKEN>/setWebhook?url=https://<PROJECT_REFERENCE>.supabase.co/functions/v1/scribe-bot?secret=<FUNCTION_SECRET>
```

Note that the `FUNCTION_SECRET` is the secret you set in your `.env` file.

![Set webhook](/docs/img/guides/functions/elevenlabs/set-webhook.png)


### Set the function secrets

Now that you have all your secrets set locally, you can run the following command to set the secrets in your Supabase project:

```bash
supabase secrets set --env-file supabase/functions/.env
```



## Test the bot

Finally you can test the bot by sending it a voice message, audio or video file.

![Test the bot](/docs/img/guides/functions/elevenlabs/test-bot.png)

After you see the transcript as a reply, navigate back to your table editor in the Supabase dashboard and you should see a new row in your `transcription_logs` table.

![New row in table](/docs/img/guides/functions/elevenlabs/supa-new-row.png)



# GitHub Actions



<div class="video-container">
  <iframe src="https://www.youtube-nocookie.com/embed/l2KlzGrhB6w" frameBorder="1" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />
</div>

Use the Supabase CLI together with GitHub Actions to automatically deploy our Supabase Edge Functions. [View on GitHub](https://github.com/supabase/supabase/tree/master/examples/edge-functions/supabase/functions/github-action-deploy).

```yaml deploy.yaml
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
      SUPABASE_ACCESS_TOKEN: YOUR_SUPABASE_ACCESS_TOKEN
      PROJECT_ID: YOUR_SUPABASE_PROJECT_ID

    steps:
      - uses: actions/checkout@v4

      - uses: supabase/setup-cli@v1
        with:
          version: latest

      - run: supabase functions deploy --project-ref $PROJECT_ID
```

Since Supabase CLI [v1.62.0](https://github.com/supabase/cli/releases/tag/v1.62.0) you can deploy all functions with a single command.

Individual function configuration like [JWT verification](/docs/guides/cli/config#functions.function_name.verify_jwt) and [import map location](/docs/guides/cli/config#functions.function_name.import_map) can be set via the `config.toml` file.

```toml
[functions.hello-world]
verify_jwt = false
```



# Image Manipulation



Supabase Storage has [out-of-the-box support](/docs/guides/storage/serving/image-transformations?queryGroups=language\&language=js) for the most common image transformations and optimizations you need.
If you need to do anything custom beyond what Supabase Storage provides, you can use Edge Functions to write custom image manipulation scripts.

In this example, we will use [`magick-wasm`](https://github.com/dlemstra/magick-wasm) to perform image manipulations. `magick-wasm` is the WebAssembly port of the popular ImageMagick library and supports processing over 100 file formats.

<Admonition type="caution">
  Edge Functions currently doesn't support image processing libraries such as `Sharp`, which depend on native libraries. Only WASM-based libraries are supported.
</Admonition>


### Prerequisites

Make sure you have the latest version of the [Supabase CLI](/docs/guides/cli#installation) installed.


### Create the Edge Function

Create a new function locally:

```bash
supabase functions new image-blur

```


### Write the function

In this example, we are implementing a function allowing users to upload an image and get a blurred thumbnail.

Here's the implementation in `index.ts` file:

<CodeSampleWrapper source="https://github.com/supabase/supabase/blob/2415776436927dedb360dae082d03caee607891a/examples/edge-functions/supabase/functions/image-manipulation/index.ts">
  ```typescript
  // This is an example showing how to use Magick WASM to do image manipulations in Edge Functions.
  //
  import {
    ImageMagick,
    initializeImageMagick,
    MagickFormat,
  } from "npm:@imagemagick/magick-wasm@0.0.30";

  const wasmBytes = await Deno.readFile(
    new URL(
      "magick.wasm",
      import.meta.resolve("npm:@imagemagick/magick-wasm@0.0.30"),
    ),
  );
  await initializeImageMagick(
    wasmBytes,
  );

  Deno.serve(async (req) => {
    const formData = await req.formData();
    const content = await formData.get("file").bytes();

    let result = ImageMagick.read(
      content,
      (img): Uint8Array => {
        // resize the image
        img.resize(500, 300);
        // add a blur of 60x5
        img.blur(60, 5);

        return img.write(
          (data) => data,
        );
      },
    );

    return new Response(
      result,
      { headers: { "Content-Type": "image/png" } },
    );
  });
  ```
</CodeSampleWrapper>


### Test it locally

You can test the function locally by running:

```bash
supabase start
supabase functions serve --no-verify-jwt

```

Then, make a request using `curl` or your favorite API testing tool.

```bash
curl --location '<http://localhost:54321/functions/v1/image-blur>' \\
--form 'file=@"/path/to/image.png"'
--output '/path/to/output.png'

```

If you open the `output.png` file you will find a transformed version of your original image.


### Deploy to your hosted project

Now, let's deploy the function to your Supabase project.

```bash
supabase link
supabase functions deploy image-blur

```

<Admonition type="caution">
  Hosted Edge Functions have [limits](/docs/guides/functions/limits) on memory and CPU usage.

  If you try to perform complex image processing or handle large images (> 5MB) your function may return a resource limit exceeded error.
</Admonition>



# Building an MCP Server with mcp-lite



The [Model Context Protocol](https://modelcontextprotocol.io/introduction) (MCP) enables Large Language Models (LLMs) to interact with external tools and data sources. With `mcp-lite`, you can build lightweight MCP servers that run on Supabase Edge Functions, giving your AI assistants the ability to execute custom tools at the edge.

This guide shows you how to scaffold, develop, and deploy an MCP server using mcp-lite on Supabase Edge Functions.



## What is mcp-lite?

[mcp-lite](https://github.com/fiberplane/mcp-lite) is a lightweight, zero-dependency TypeScript framework for building MCP servers. It works everywhere the Fetch API is available, including Node, Bun, Cloudflare Workers, Deno, and Supabase Edge Functions.



## Why Supabase Edge Functions + mcp-lite?

This combination offers several advantages:

*   **Zero cold starts**: Edge Functions stay warm for fast responses
*   **Global distribution**: Deploy once and run everywhere
*   **Direct database access**: Connect directly to your Supabase Postgres
*   **Minimal footprint**: mcp-lite has zero runtime dependencies
*   **Full type safety**: TypeScript support in Deno
*   **Simple deployment**: One command to production



## Prerequisites

You need:

*   [Docker](https://docs.docker.com/get-docker/) (to run Supabase locally)
*   [Deno](https://deno.land/) (Supabase Edge Functions runtime)
*   [Supabase CLI](/docs/guides/cli/getting-started)



## Create a new MCP server

Starting with `create-mcp-lite@0.3.0`, you can scaffold a complete MCP server that runs on Supabase Edge Functions:

```bash
npm create mcp-lite@latest
```

When prompted, select **Supabase Edge Functions (MCP server)** from the template options.

The template creates a focused structure for Edge Functions development:

```
my-mcp-server/
├── supabase/
│   ├── config.toml                    # Minimal Supabase config (Edge Functions only)
│   └── functions/
│       └── mcp-server/
│           ├── index.ts               # MCP server implementation
│           └── deno.json              # Deno imports and configuration
├── package.json
└── tsconfig.json
```



## Understanding the project structure


### Minimal config.toml

The template includes a minimal `config.toml` that runs only Edge Functions - no database, storage, or Studio UI. This keeps your local setup lightweight:

```toml

# Minimal config for running only Edge Functions (no DB, storage, or studio)
project_id = "starter-mcp-supabase"

[api]
enabled = true
port = 54321

[edge_runtime]
enabled = true
policy = "per_worker"
deno_version = 2
```

You can always add more services as needed.


### Two Hono apps pattern

The template uses a specific pattern required by Supabase Edge Functions:

```ts
// Root handler - matches the function name
const app = new Hono()

// MCP protocol handler
const mcpApp = new Hono()

mcpApp.get('/', (c) => {
  return c.json({
    message: 'MCP Server on Supabase Edge Functions',
    endpoints: {
      mcp: '/mcp',
      health: '/health',
    },
  })
})

mcpApp.all('/mcp', async (c) => {
  const response = await httpHandler(c.req.raw)
  return response
})

// Mount at /mcp-server (the function name)
app.route('/mcp-server', mcpApp)
```

This is required because Supabase routes all requests to `/<function-name>/*`. The outer `app` handles the function-level routing, while `mcpApp` handles your actual MCP endpoints.


### Deno import maps

The template uses Deno's import maps in `deno.json` to manage dependencies:

```json
{
  "compilerOptions": {
    "lib": ["deno.window", "deno.ns"],
    "strict": true
  },
  "imports": {
    "hono": "npm:hono@^4.6.14",
    "mcp-lite": "npm:mcp-lite@0.8.2",
    "zod": "npm:zod@^4.1.12"
  }
}
```

This gives you npm package access while staying in the Deno ecosystem.



## Local development


### Start Supabase

Navigate to your project directory and start Supabase services:

```bash
supabase start
```


### Serve your function

In a separate terminal, serve your MCP function locally:

```bash
supabase functions serve --no-verify-jwt mcp-server
```

Or use the npm script (which runs the same command):

```bash
npm run dev
```

Your MCP server is available at:

```
http://localhost:54321/functions/v1/mcp-server/mcp
```


### Testing your server

Test the MCP server by adding it to your Claude Code, Claude Desktop, Cursor, or your preferred MCP client.

Using Claude Code:

```bash
claude mcp add my-mcp-server -t http http://localhost:54321/functions/v1/mcp-server/mcp
```

You can also test it using the MCP inspector:

```bash
npx @modelcontextprotocol/inspector
```

Then add the MCP endpoint URL in the inspector UI.



## How it works

The MCP server setup is straightforward:

```ts
import { McpServer, StreamableHttpTransport } from 'mcp-lite'
import { z } from 'zod'

// Create MCP server instance
const mcp = new McpServer({
  name: 'starter-mcp-supabase-server',
  version: '1.0.0',
  schemaAdapter: (schema) => z.toJSONSchema(schema as z.ZodType),
})

// Define a tool
mcp.tool('sum', {
  description: 'Adds two numbers together',
  inputSchema: z.object({
    a: z.number(),
    b: z.number(),
  }),
  handler: (args: { a: number; b: number }) => ({
    content: [{ type: 'text', text: String(args.a + args.b) }],
  }),
})

// Bind to HTTP transport
const transport = new StreamableHttpTransport()
const httpHandler = transport.bind(mcp)
```



## Adding more tools

Extend your MCP server by adding tools directly to the `mcp` instance. Here's an example of adding a database search tool:

```ts
mcp.tool('searchDatabase', {
  description: 'Search your Supabase database',
  inputSchema: z.object({
    table: z.string(),
    query: z.string(),
  }),
  handler: async (args) => {
    // Access Supabase client here
    // const { data } = await supabase.from(args.table).select('*')
    return {
      content: [{ type: 'text', text: `Searching ${args.table}...` }],
    }
  },
})
```

You can add tools that:

*   Query your Supabase database
*   Access Supabase Storage for file operations
*   Call external APIs
*   Process data with custom logic
*   Integrate with other Supabase features



## Deploy to production

When ready, deploy to Supabase's global edge network:

```bash
supabase functions deploy --no-verify-jwt mcp-server
```

Or use the npm script:

```bash
npm run deploy
```

Your MCP server will be live at:

```
https://your-project-ref.supabase.co/functions/v1/mcp-server/mcp
```



## Authentication considerations

<Admonition type="caution">
  The template uses `--no-verify-jwt` for quick development. This means authentication is not enforced by Supabase's JWT layer.

  For production, you should implement authentication at the MCP server level following the [MCP Authorization specification](https://modelcontextprotocol.io/specification/draft/basic/authorization). This gives you control over who can access your MCP tools.
</Admonition>


### Security best practices

When deploying MCP servers:

*   **Don't expose sensitive data**: Use the server in development environments with non-production data
*   **Implement authentication**: Add proper authentication for production deployments
*   **Validate inputs**: Always validate and sanitize tool inputs
*   **Limit tool scope**: Only expose tools that are necessary for your use case
*   **Monitor usage**: Track tool calls and monitor for unusual activity

For more security guidance, see the [MCP security guide](/guides/getting-started/mcp#security-risks).



## What's next

With your MCP server running on Supabase Edge Functions, you can:

*   Connect it to your Supabase database for data-driven tools
*   Use Supabase Auth to secure your endpoints
*   Access Supabase Storage for file operations
*   Deploy to multiple regions automatically
*   Scale to handle production traffic
*   Integrate with AI assistants like Claude, Cursor, or custom MCP clients



## Resources

*   [mcp-lite on GitHub](https://github.com/fiberplane/mcp-lite)
*   [Model Context Protocol Spec](https://modelcontextprotocol.io/)
*   [Supabase Edge Functions Docs](/guides/functions)
*   [Deno Runtime Documentation](https://deno.land/)
*   [Fiberplane tutorial](https://blog.fiberplane.com/blog/mcp-lite-supabase-edge-functions/)



# Generating OG Images



<div class="video-container">
  <iframe src="https://www.youtube-nocookie.com/embed/jZgyOJGWayQ" frameBorder="1" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />
</div>

Generate Open Graph images with Deno and Supabase Edge Functions. [View on GitHub](https://github.com/supabase/supabase/tree/master/examples/edge-functions/supabase/functions/opengraph).



## Code

Create a `handler.tsx` file to construct the OG image in React:

```tsx handler.tsx
import React from 'https://esm.sh/react@18.2.0'
import { ImageResponse } from 'https://deno.land/x/og_edge@0.0.4/mod.ts'

export default function handler(req: Request) {
  return new ImageResponse(
    (
      <div
        style={{
          width: '100%',
          height: '100%',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          fontSize: 128,
          background: 'lavender',
        }}
      >
        Hello OG Image!
      </div>
    )
  )
}
```

Create an `index.ts` file to execute the handler on incoming requests:

```ts index.ts
import handler from './handler.tsx'

console.log('Hello from og-image Function!')

Deno.serve(handler)
```



# Sending Push Notifications



Push notifications are an important part of any mobile app. They allow you to send notifications to your users even when they are not using your app. This guide will show you how to send push notifications to different mobile app frameworks from your Supabase edge functions.

<Tabs scrollable size="large" type="underlined" defaultActiveId="expo" queryGroup="platform">
  <TabPanel id="expo" label="Expo Push Notifications">
    [Expo](https://docs.expo.dev/push-notifications/overview/) makes implementing push notifications easy. All the hassle with device information and communicating with Firebase Cloud Messaging (FCM) or Apple Push Notification Service (APNs) is done behind the scenes. This allows you to treat Android and iOS notifications in the same way and save time both on the frontend and backend.

    Find the example code on [GitHub](https://github.com/supabase/supabase/blob/master/examples/user-management/expo-push-notifications/).

    ## Supabase setup

    *   [Create a new Supabase project](https://database.new).
    *   Link your project: `supabase link --project-ref your-supabase-project-ref`
    *   Start Supabase locally: `supabase start`
    *   Push up the schema: `supabase db push` (schema is defined in [supabase/migrations](https://github.com/supabase/supabase/blob/master/examples/user-management/expo-push-notifications/supabase/migrations/))

    ## Expo setup

    To utilize Expo's push notification service, you must configure your app by installing a set of libraries, implementing functions to handle notifications, and setting up credentials for Android and iOS. Follow the official [Expo Push Notifications Setup Guide](https://docs.expo.dev/push-notifications/push-notifications-setup/) to get the credentials for Android and iOS. This project uses [Expo's EAS build](https://docs.expo.dev/build/introduction/) service to simplify this part.

    1.  Install the dependencies: `npm i`
    2.  Create a [new Expo project](https://expo.dev/accounts/_/projects)
    3.  Link this app to your project: `npm install --global eas-cli && eas init --id your-expo-project-id`
    4.  [Create a build for your physical device](https://docs.expo.dev/develop/development-builds/create-a-build/#create-a-build-for-the-device)
    5.  Start the development server for your project: `npx expo start --dev-client`
    6.  Scan the QR code shown in the terminal with your physical device.
    7.  Sign up/in to create a user in Supabase Auth.

    ## Enhanced security for push notifications

    1.  Navigate to your [Expo Access Token Settings](https://expo.dev/accounts/_/settings/access-tokens).
    2.  Create a new token for usage in Supabase Edge Functions.
    3.  Toggle on "Enhanced Security for Push Notifications".
    4.  Create the local `.env` file: `cp .env.local.example .env.local`
    5.  In the newly created `.env.local` file, set your `EXPO_ACCESS_TOKEN` value.

    ## Deploy the Supabase Edge Function

    The database webhook handler to send push notifications is located in [supabase/functions/push/index.ts](https://github.com/supabase/supabase/blob/master/examples/user-management/expo-push-notifications/supabase/functions/push/index.ts). Deploy the function to your linked project and set the `EXPO_ACCESS_TOKEN` secret.

    1.  `supabase functions deploy push`
    2.  `supabase secrets set --env-file .env.local`

    ```ts supabase/functions/push/index.ts
    import { createClient } from 'npm:@supabase/supabase-js@2'

    console.log('Hello from Functions!')

    interface Notification {
      id: string
      user_id: string
      body: string
    }

    interface WebhookPayload {
      type: 'INSERT' | 'UPDATE' | 'DELETE'
      table: string
      record: Notification
      schema: 'public'
      old_record: null | Notification
    }

    const supabase = createClient(
      Deno.env.get('SUPABASE_URL')!,
      Deno.env.get('SUPABASE_SERVICE_ROLE_KEY')!
    )

    Deno.serve(async (req) => {
      const payload: WebhookPayload = await req.json()
      const { data } = await supabase
        .from('profiles')
        .select('expo_push_token')
        .eq('id', payload.record.user_id)
        .single()

      const res = await fetch('https://exp.host/--/api/v2/push/send', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${Deno.env.get('EXPO_ACCESS_TOKEN')}`,
        },
        body: JSON.stringify({
          to: data?.expo_push_token,
          sound: 'default',
          body: payload.record.body,
        }),
      }).then((res) => res.json())

      return new Response(JSON.stringify(res), {
        headers: { 'Content-Type': 'application/json' },
      })
    })
    ```

    ## Create the database webhook

    Navigate to the [Database Webhooks settings](/dashboard/project/_/integrations/webhooks/overview) in your Supabase Dashboard.

    1.  Enable and create a new hook.
    2.  Conditions to fire webhook: Select the `notifications` table and tick the `Insert` event.
    3.  Webhook configuration: Supabase Edge Functions.
    4.  Edge Function: Select the `push` edge function and leave the method as `POST` and timeout as `1000`.
    5.  HTTP Headers: Click "Add new header" > "Add auth header with service key" and leave Content-type: `application/json`.
    6.  Click "Create webhook".

    ## Send push notification

    1.  Navigate to the [table editor](/dashboard/project/_/editor) in your Supabase Dashboard.
    2.  In your `notifications` table, insert a new row.
    3.  Watch the magic happen 🪄
  </TabPanel>

  <TabPanel id="fcm" label="Firebase Cloud Messaging">
    Firebase Cloud Messaging (FCM) is a push notification service offered by Google that allows you to send push notifications to your users' devices on iOS, Android, and Web.

    This guide will show you how to send push notifications to your app when a new row is inserted into a table using FCM, Supabase Edge Functions, and database web hooks.

    ## Supabase setup

    We will create two tables. One to store the user's FCM token and a `notifications` table. The edge function will be triggered when a new row is inserted into the `notifications` table and sends a push notification to the user.

    Create a `notifications` table. Also create a `profiles` table if you don't already have one:

    ```sql
    create table public.profiles (
      id uuid references auth.users(id) not null primary key,
      fcm_token text
    );

    create table public.notifications (
      id uuid not null default gen_random_uuid(),
      user_id uuid references auth.users(id) not null,
      created_at timestamp with time zone not null default now(),
      body text not null
    );
    ```

    If you already have a `profiles` table, alter it to include an `fcm_token` column:

    ```sql
    ALTER TABLE public.profiles
    ADD COLUMN fcm_token text;
    ```

    With the tables created, we can now create the edge function that will be triggered by database webhook when a notification is inserted.

    Create the function using the following command:

    ```bash
    # Initialize Supabase in your working directory
    supabase init
    # Create the push edge function
    supabase functions new push
    ```

    Add the following code to `supabase/functions/push/index.ts`:

    ```ts supabase/functions/push/index.ts
    import { createClient } from 'npm:@supabase/supabase-js@2'
    import { JWT } from 'npm:google-auth-library@9'
    import serviceAccount from '../service-account.json' with { type: 'json' }

    interface Notification {
      id: string
      user_id: string
      body: string
    }

    interface WebhookPayload {
      type: 'INSERT'
      table: string
      record: Notification
      schema: 'public'
    }

    const supabase = createClient(
      Deno.env.get('SUPABASE_URL')!,
      Deno.env.get('SUPABASE_SERVICE_ROLE_KEY')!
    )

    Deno.serve(async (req) => {
      const payload: WebhookPayload = await req.json()

      const { data } = await supabase
        .from('profiles')
        .select('fcm_token')
        .eq('id', payload.record.user_id)
        .single()

      const fcmToken = data!.fcm_token as string

      const accessToken = await getAccessToken({
        clientEmail: serviceAccount.client_email,
        privateKey: serviceAccount.private_key,
      })

      const res = await fetch(
        `https://fcm.googleapis.com/v1/projects/${serviceAccount.project_id}/messages:send`,
        {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            Authorization: `Bearer ${accessToken}`,
          },
          body: JSON.stringify({
            message: {
              token: fcmToken,
              notification: {
                title: `Notification from Supabase`,
                body: payload.record.body,
              },
            },
          }),
        }
      )

      const resData = await res.json()
      if (res.status < 200 || 299 < res.status) {
        throw resData
      }

      return new Response(JSON.stringify(resData), {
        headers: { 'Content-Type': 'application/json' },
      })
    })

    const getAccessToken = ({
      clientEmail,
      privateKey,
    }: {
      clientEmail: string
      privateKey: string
    }): Promise<string> => {
      return new Promise((resolve, reject) => {
        const jwtClient = new JWT({
          email: clientEmail,
          key: privateKey,
          scopes: ['https://www.googleapis.com/auth/firebase.messaging'],
        })
        jwtClient.authorize((err, tokens) => {
          if (err) {
            reject(err)
            return
          }
          resolve(tokens!.access_token!)
        })
      })
    }
    ```

    ## FCM setup

    1.  Follow the official [FCM Setup Guide](https://firebase.google.com/docs/cloud-messaging) to set up FCM for your client side application.
    2.  Generate a new service account private key from the Firebase console `Project Settings > Service Accounts > Generate new private key`.
    3.  Save the service account private key as `service-account.json` under `supabase/functions` directory.

    ## Deploy the function

    Deploy the function with the following command:

    ```bash
    # Link your local Supabase project to the remote Supabase project
    supabase link
    # Deploy the function
    supabase functions deploy push --no-verify-jwt
    ```

    ## Create the database webhook

    Navigate to the [Database Webhooks settings](/dashboard/project/_/database/hooks) in your Supabase Dashboard.

    1.  Enable and create a new hook.
    2.  Conditions to fire webhook: Select the `public.notifications` table and tick the `Insert` event.
    3.  Webhook configuration: Supabase Edge Functions.
    4.  Edge Function: Select the `push` edge function and leave the method as `POST` and timeout as `1000`.
    5.  Click "Create webhook".

    ## Send push notification

    1.  Make sure you have a user with an FCM token in the `profiles` table.
    2.  Navigate to the [table editor](/dashboard/project/_/editor) in your Supabase Dashboard.
    3.  In your `notifications` table, insert a new row.
    4.  Watch the magic happen 🪄

    <div className="video-container">
      <iframe src="https://www.youtube-nocookie.com/embed/CiSv9E6ZKVc" frameBorder="1" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />
    </div>
  </TabPanel>
</Tabs>



# Rate Limiting Edge Functions



<div class="video-container">
  <iframe src="https://www.youtube-nocookie.com/embed/o4ooiE-SdUg" frameBorder="1" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />
</div>

[Redis](https://redis.io/docs/about/) is an open source (BSD licensed), in-memory data structure store used as a database, cache, message broker, and streaming engine. It is optimized for atomic operations like incrementing a value, for example for a view counter or rate limiting. We can even rate limit based on the user ID from Supabase Auth!

[Upstash](https://upstash.com/) provides an HTTP/REST based Redis client which is ideal for serverless use-cases and therefore works well with Supabase Edge Functions.

Find the code on [GitHub](https://github.com/supabase/supabase/tree/master/examples/edge-functions/supabase/functions/upstash-redis-ratelimit).



# Taking Screenshots with Puppeteer



<div class="video-container">
  <iframe src="https://www.youtube-nocookie.com/embed/Q1nfnQggR4c" frameBorder="1" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />
</div>

[Puppeteer](https://pptr.dev/) is a handy tool to programmatically take screenshots and generate PDFs. However, trying to do so in Edge Functions can be challenging due to the size restrictions. Luckily there is a [serverless browser offering available](https://www.browserless.io/) that we can connect to via WebSockets.

Find the code on [GitHub](https://github.com/supabase/supabase/tree/master/examples/edge-functions/supabase/functions/puppeteer).



# Semantic Search

Semantic Search with pgvector and Supabase Edge Functions

[Semantic search](/docs/guides/ai/semantic-search) interprets the meaning behind user queries rather than exact [keywords](/docs/guides/ai/keyword-search). It uses machine learning to capture the intent and context behind the query, handling language nuances like synonyms, phrasing variations, and word relationships.

Since Supabase Edge Runtime [v1.36.0](https://github.com/supabase/edge-runtime/releases/tag/v1.36.0) you can run the [`gte-small` model](https://huggingface.co/Supabase/gte-small) natively within Supabase Edge Functions without any external dependencies! This allows you to generate text embeddings without calling any external APIs!

In this tutorial you're implementing three parts:

1.  A [`generate-embedding`](https://github.com/supabase/supabase/tree/master/examples/ai/edge-functions/supabase/functions/generate-embedding/index.ts) database webhook edge function which generates embeddings when a content row is added (or updated) in the [`public.embeddings`](https://github.com/supabase/supabase/tree/master/examples/ai/edge-functions/supabase/migrations/20240408072601_embeddings.sql) table.
2.  A [`query_embeddings` Postgres function](https://github.com/supabase/supabase/tree/master/examples/ai/edge-functions/supabase/migrations/20240410031515_vector-search.sql) which allows us to perform similarity search from an Edge Function via [Remote Procedure Call (RPC)](/docs/guides/database/functions?language=js).
3.  A [`search` edge function](https://github.com/supabase/supabase/tree/master/examples/ai/edge-functions/supabase/functions/search/index.ts) which generates the embedding for the search term, performs the similarity search via RPC function call, and returns the result.

You can find the complete example code on [GitHub](https://github.com/supabase/supabase/tree/master/examples/ai/edge-functions)


### Create the database table and webhook

Given the [following table definition](https://github.com/supabase/supabase/blob/master/examples/ai/edge-functions/supabase/migrations/20240408072601_embeddings.sql):

```sql
create extension if not exists vector with schema extensions;

create table embeddings (
  id bigint primary key generated always as identity,
  content text not null,
  embedding extensions.vector (384)
);
alter table embeddings enable row level security;

create index on embeddings using hnsw (embedding vector_ip_ops);
```

You can deploy the [following edge function](https://github.com/supabase/supabase/blob/master/examples/ai/edge-functions/supabase/functions/generate-embedding/index.ts) as a [database webhook](/docs/guides/database/webhooks) to generate the embeddings for any text content inserted into the table:

```tsx
const model = new Supabase.ai.Session('gte-small')

Deno.serve(async (req) => {
  const payload: WebhookPayload = await req.json()
  const { content, id } = payload.record

  // Generate embedding.
  const embedding = await model.run(content, {
    mean_pool: true,
    normalize: true,
  })

  // Store in database.
  const { error } = await supabase
    .from('embeddings')
    .update({ embedding: JSON.stringify(embedding) })
    .eq('id', id)
  if (error) console.warn(error.message)

  return new Response('ok')
})
```



## Create a Database Function and RPC

With the embeddings now stored in your Postgres database table, you can query them from Supabase Edge Functions by utilizing [Remote Procedure Calls (RPC)](/docs/guides/database/functions?language=js).

Given the [following Postgres Function](https://github.com/supabase/supabase/blob/master/examples/ai/edge-functions/supabase/migrations/20240410031515_vector-search.sql):

```sql
-- Matches document sections using vector similarity search on embeddings
--
-- Returns a setof embeddings so that we can use PostgREST resource embeddings (joins with other tables)
-- Additional filtering like limits can be chained to this function call
create or replace function query_embeddings(embedding extensions.vector(384), match_threshold float)
returns setof embeddings
language plpgsql
as $$
begin
  return query
  select *
  from embeddings

  -- The inner product is negative, so we negate match_threshold
  where embeddings.embedding <#> embedding < -match_threshold

  -- Our embeddings are normalized to length 1, so cosine similarity
  -- and inner product will produce the same query results.
  -- Using inner product which can be computed faster.
  --
  -- For the different distance functions, see https://github.com/pgvector/pgvector
  order by embeddings.embedding <#> embedding;
end;
$$;
```



## Query vectors in Supabase Edge Functions

You can use `supabase-js` to first generate the embedding for the search term and then invoke the Postgres function to find the relevant results from your stored embeddings, right from your [Supabase Edge Function](https://github.com/supabase/supabase/blob/master/examples/ai/edge-functions/supabase/functions/search/index.ts):

```tsx
const model = new Supabase.ai.Session('gte-small')

Deno.serve(async (req) => {
  const { search } = await req.json()
  if (!search) return new Response('Please provide a search param!')
  // Generate embedding for search term.
  const embedding = await model.run(search, {
    mean_pool: true,
    normalize: true,
  })

  // Query embeddings.
  const { data: result, error } = await supabase
    .rpc('query_embeddings', {
      embedding,
      match_threshold: 0.8,
    })
    .select('content')
    .limit(3)
  if (error) {
    return Response.json(error)
  }

  return Response.json({ search, result })
})
```

You now have AI powered semantic search set up without any external dependencies! Just you, pgvector, and Supabase Edge Functions!



# Sending Emails



Sending emails from Edge Functions using the [Resend API](https://resend.com/).


### Prerequisites

To get the most out of this guide, you’ll need to:

*   [Create an API key](https://resend.com/api-keys)
*   [Verify your domain](https://resend.com/domains)

Make sure you have the latest version of the [Supabase CLI](/docs/guides/cli#installation) installed.


### 1. Create Supabase function

Create a new function locally:

```bash
supabase functions new resend
```

Store the `RESEND_API_KEY` in your `.env` file.


### 2. Edit the handler function

Paste the following code into the `index.ts` file:

```tsx
const RESEND_API_KEY = Deno.env.get('RESEND_API_KEY')

const handler = async (_request: Request): Promise<Response> => {
  const res = await fetch('https://api.resend.com/emails', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      Authorization: `Bearer ${RESEND_API_KEY}`,
    },
    body: JSON.stringify({
      from: 'onboarding@resend.dev',
      to: 'delivered@resend.dev',
      subject: 'hello world',
      html: '<strong>it works!</strong>',
    }),
  })

  const data = await res.json()

  return new Response(JSON.stringify(data), {
    status: 200,
    headers: {
      'Content-Type': 'application/json',
    },
  })
}

Deno.serve(handler)
```


### 3. Deploy and send email

Run function locally:

```bash
supabase start
supabase functions serve --no-verify-jwt --env-file .env
```

Test it: [http://localhost:54321/functions/v1/resend](http://localhost:54321/functions/v1/resend)

Deploy function to Supabase:

```bash
supabase functions deploy resend --no-verify-jwt
```

<Admonition type="caution">
  When you deploy to Supabase, make sure that your `RESEND_API_KEY` is set in [Edge Function Secrets Management](/dashboard/project/_/settings/functions)
</Admonition>

Open the endpoint URL to send an email:


### 4. Try it yourself

Find the complete example on [GitHub](https://github.com/resendlabs/resend-supabase-edge-functions-example).



# Monitoring with Sentry



Add the [Sentry Deno SDK](https://docs.sentry.io/platforms/javascript/guides/deno/) to your Supabase Edge Functions to track exceptions and get notified of errors or performance issues.


### Prerequisites

*   [Create a Sentry account](https://sentry.io/signup/).
*   Make sure you have the latest version of the [Supabase CLI](/docs/guides/cli#installation) installed.


### 1. Create Supabase function

Create a new function locally:

```bash
supabase functions new sentryfied
```


### 2. Add the Sentry Deno SDK

Handle exceptions within your function and send them to Sentry.

```tsx
import * as Sentry from 'https://deno.land/x/sentry/index.mjs'

Sentry.init({
  // https://docs.sentry.io/product/sentry-basics/concepts/dsn-explainer/#where-to-find-your-dsn
  dsn: SENTRY_DSN,
  defaultIntegrations: false,
  // Performance Monitoring
  tracesSampleRate: 1.0,
  // Set sampling rate for profiling - this is relative to tracesSampleRate
  profilesSampleRate: 1.0,
})

// Set region and execution_id as custom tags
Sentry.setTag('region', Deno.env.get('SB_REGION'))
Sentry.setTag('execution_id', Deno.env.get('SB_EXECUTION_ID'))

Deno.serve(async (req) => {
  try {
    const { name } = await req.json()
    // This will throw, as `name` in our example call will be `undefined`
    const data = {
      message: `Hello ${name}!`,
    }

    return new Response(JSON.stringify(data), { headers: { 'Content-Type': 'application/json' } })
  } catch (e) {
    Sentry.captureException(e)
    // Flush Sentry before the running process closes
    await Sentry.flush(2000)
    return new Response(JSON.stringify({ msg: 'error' }), {
      status: 500,
      headers: { 'Content-Type': 'application/json' },
    })
  }
})
```


### 3. Deploy and test

Run function locally:

```bash
supabase start
supabase functions serve --no-verify-jwt
```

Test it: [http://localhost:54321/functions/v1/sentryfied](http://localhost:54321/functions/v1/sentryfied)

Deploy function to Supabase:

```bash
supabase functions deploy sentryfied --no-verify-jwt
```


### 4. Try it yourself

Find the complete example on [GitHub](https://github.com/supabase/supabase/tree/master/examples/edge-functions/supabase/functions/sentryfied/index.ts).



## Working with scopes

Sentry Deno SDK currently do not support `Deno.serve` instrumentation, which means that there is no scope separation between requests. Because of that, when the Edge Functions runtime is reused between multiple requests, all globally captured breadcrumbs and contextual data will be shared, which is not the desired behavior. To work around this, all default integrations in the example code above are disabled, and you should be relying on [`withScope`](https://docs.sentry.io/platforms/javascript/enriching-events/scopes/#using-withscope) to encapsulate all Sentry SDK API calls, or [pass context directly](https://docs.sentry.io/platforms/javascript/enriching-events/context/#passing-context-directly) to the `captureException` or `captureMessage` calls.



# Slack Bot Mention Edge Function



The Slack Bot Mention Edge Function allows you to process mentions in Slack and respond accordingly.



## Configuring Slack apps

For your bot to seamlessly interact with Slack, you'll need to configure Slack Apps:

1.  Navigate to the Slack Apps page.
2.  Under "Event Subscriptions," add the URL of the `slack-bot-mention` function and click to verify the URL.
3.  The Edge function will respond, confirming that everything is set up correctly.
4.  Add `app-mention` in the events the bot will subscribe to.



## Creating the Edge Function

Deploy the following code as an Edge function using the CLI:

```bash
supabase --project-ref nacho_slacker secrets \
set SLACK_TOKEN=<REDACTED_EXAMPLE_TOKEN>
```

Here's the code of the Edge Function, you can change the response to handle the text received:

```ts index.ts
import { WebClient } from 'https://deno.land/x/slack_web_api@6.7.2/mod.js'

const slackBotToken = Deno.env.get('SLACK_TOKEN') ?? ''
const botClient = new WebClient(slackBotToken)

console.log(`Slack URL verification function up and running!`)
Deno.serve(async (req) => {
  try {
    const reqBody = await req.json()
    console.log(JSON.stringify(reqBody, null, 2))
    const { token, challenge, type, event } = reqBody

    if (type == 'url_verification') {
      return new Response(JSON.stringify({ challenge }), {
        headers: { 'Content-Type': 'application/json' },
        status: 200,
      })
    } else if (event.type == 'app_mention') {
      const { user, text, channel, ts } = event
      // Here you should process the text received and return a response:
      const response = await botClient.chat.postMessage({
        channel: channel,
        text: `Hello <@${user}>!`,
        thread_ts: ts,
      })
      return new Response('ok', { status: 200 })
    }
  } catch (error) {
    return new Response(JSON.stringify({ error: error.message }), {
      headers: { 'Content-Type': 'application/json' },
      status: 500,
    })
  }
})
```



# Handling Stripe Webhooks



<div class="video-container">
  <iframe src="https://www.youtube-nocookie.com/embed/6OMVWiiycLs" frameBorder="1" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />
</div>

Handling signed Stripe Webhooks with Edge Functions. [View on GitHub](https://github.com/supabase/supabase/blob/master/examples/edge-functions/supabase/functions/stripe-webhooks/index.ts).

<CodeSampleWrapper source="https://github.com/supabase/supabase/blob/2415776436927dedb360dae082d03caee607891a/examples/edge-functions/supabase/functions/stripe-webhooks/index.ts">
  ```typescript index.ts
  // Follow this setup guide to integrate the Deno language server with your editor:
  // https://deno.land/manual/getting_started/setup_your_environment
  // This enables autocomplete, go to definition, etc.

  // Import via bare specifier thanks to the import_map.json file.
  import Stripe from 'https://esm.sh/stripe@14?target=denonext'

  const stripe = new Stripe(Deno.env.get('STRIPE_API_KEY') as string, {
    // This is needed to use the Fetch API rather than relying on the Node http
    // package.
    apiVersion: '2024-11-20'
  })
  // This is needed in order to use the Web Crypto API in Deno.
  const cryptoProvider = Stripe.createSubtleCryptoProvider()

  console.log('Hello from Stripe Webhook!')

  Deno.serve(async (request) => {
    const signature = request.headers.get('Stripe-Signature')

    // First step is to verify the event. The .text() method must be used as the
    // verification relies on the raw request body rather than the parsed JSON.
    const body = await request.text()
    let receivedEvent
    try {
      receivedEvent = await stripe.webhooks.constructEventAsync(
        body,
        signature!,
        Deno.env.get('STRIPE_WEBHOOK_SIGNING_SECRET')!,
        undefined,
        cryptoProvider
      )
    } catch (err) {
      return new Response(err.message, { status: 400 })
    }
    console.log(`🔔 Event received: ${receivedEvent.id}`)
    return new Response(JSON.stringify({ ok: true }), { status: 200 })
  });
  ```
</CodeSampleWrapper>



# Building a Telegram Bot



<div class="video-container">
  <iframe src="https://www.youtube-nocookie.com/embed/AWfE3a9J_uo" frameBorder="1" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />
</div>

Handle Telegram Bot Webhooks with the [grammY framework](https://grammy.dev/). grammY is an open source Telegram Bot Framework which makes it easy to handle and respond to incoming messages. [View on GitHub](https://github.com/supabase/supabase/tree/master/examples/edge-functions/supabase/functions/telegram-bot).



# Upstash Redis



<div class="video-container">
  <iframe src="https://www.youtube-nocookie.com/embed/OPg3_oPZCh0" frameBorder="1" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />
</div>

A Redis counter example that stores a [hash](https://redis.io/commands/hincrby/) of function invocation count per region. Find the code on [GitHub](https://github.com/supabase/supabase/tree/master/examples/edge-functions/supabase/functions/upstash-redis-counter).



## Redis database setup

Create a Redis database using the [Upstash Console](https://console.upstash.com/) or [Upstash CLI](https://github.com/upstash/cli).

Select the `Global` type to minimize the latency from all edge locations. Copy the `UPSTASH_REDIS_REST_URL` and `UPSTASH_REDIS_REST_TOKEN` to your .env file.

You'll find them under **Details > REST API > .env**.

```bash
cp supabase/functions/upstash-redis-counter/.env.example supabase/functions/upstash-redis-counter/.env
```



## Code

Make sure you have the latest version of the [Supabase CLI installed](/docs/guides/cli#installation).

Create a new function in your project:

```bash
supabase functions new upstash-redis-counter
```

And add the code to the `index.ts` file:

```ts index.ts
import { Redis } from 'https://deno.land/x/upstash_redis@v1.19.3/mod.ts'

console.log(`Function "upstash-redis-counter" up and running!`)

Deno.serve(async (_req) => {
  try {
    const redis = new Redis({
      url: Deno.env.get('UPSTASH_REDIS_REST_URL')!,
      token: Deno.env.get('UPSTASH_REDIS_REST_TOKEN')!,
    })

    const deno_region = Deno.env.get('DENO_REGION')
    if (deno_region) {
      // Increment region counter
      await redis.hincrby('supa-edge-counter', deno_region, 1)
    } else {
      // Increment localhost counter
      await redis.hincrby('supa-edge-counter', 'localhost', 1)
    }

    // Get all values
    const counterHash: Record<string, number> | null = await redis.hgetall('supa-edge-counter')
    const counters = Object.entries(counterHash!)
      .sort(([, a], [, b]) => b - a) // sort desc
      .reduce((r, [k, v]) => ({ total: r.total + v, regions: { ...r.regions, [k]: v } }), {
        total: 0,
        regions: {},
      })

    return new Response(JSON.stringify({ counters }), { status: 200 })
  } catch (error) {
    return new Response(JSON.stringify({ error: error.message }), { status: 200 })
  }
})
```



## Run locally

```bash
supabase start
supabase functions serve --no-verify-jwt --env-file supabase/functions/upstash-redis-counter/.env
```

Navigate to [http://localhost:54321/functions/v1/upstash-redis-counter](http://localhost:54321/functions/v1/upstash-redis-counter).



## Deploy

```bash
supabase functions deploy upstash-redis-counter --no-verify-jwt
supabase secrets set --env-file supabase/functions/upstash-redis-counter/.env
```



# Branching

Use Supabase Branches to test and preview changes

Use branching to safely experiment with changes to your Supabase project.

Supabase branches create separate environments that spin off from your main project. You can use these branching environments to create and test changes like new configurations, database schemas, or features without affecting your production setup. When you're ready to ship your changes, merge your branch to update your production instance with the new changes.



## How branching works

*   **Separate Environments**: Each branch is a separate environment with its own Supabase instance and API credentials.
*   **Preview Branches**: You can create multiple Preview Branches for testing.
*   **Persistent Branches**: Persistent branches are long-lived branches. They aren't automatically paused or deleted due to non-inactivity or merging.
*   **Managing Branches**: You can create, review, and merge branches either automatically via our [GitHub integration](/docs/guides/deployment/branching/github-integration) or directly [through the dashboard](/docs/guides/deployment/branching/dashboard) (currently in beta). All branches show up in the branches page in the dashboard, regardless of how they were created.
*   **Data-less**: New branches do not start with any data from your main project. This is meant to better protect your sensitive production data. To start your branches with data, you can use a [seed file](/docs/guides/deployment/branching/github-integration#seeding) if using the GitHub integration.



## Deploying to production

When you merge any branch into your main project, Supabase automatically runs a deployment workflow to deploy your changes to production. The deployment workflow is expressed as a Directed Acyclic Graph where each node represents one of the following deployment steps.

1.  **Clone** - Checks out your repository at the specified git branch (optional for [Branching via Dashboard](/docs/guides/deployment/branching/dashboard))
2.  **Pull** - Retrieves database migrations from your main project (also initialises the migration history table when Branching via Dashboard)
3.  **Health** - Waits up to 2 minutes for all Supabase services on your branch to be running and healthy, including Auth, API, Database, Storage, and Realtime
4.  **Configure** - Updates service configurations based on your config.toml file (only available for [Branching via GitHub](/docs/guides/deployment/branching/github-integration))
5.  **Migrate** - Applies pending database migrations and vault secrets to your branch
6.  **Seed** - Runs seed files to populate your branch with initial data (must be [enabled in config.toml](/docs/guides/deployment/branching/configuration#branch-configuration-with-remotes) for persistent branches)
7.  **Deploy** - Deploys any changed Edge Functions and updates function secrets

If a parent deployment step fails, all dependent children steps will be skipped. For e.g., if your database migrations failed at step 5, our runner will not seed your branch because step 6 is skipped. If you are using GitHub integration, the same deployment workflow will be run on every commit pushed to your git branch.



# Database Migrations

How to manage schema migrations for your Supabase project.

Database migrations are SQL statements that create, update, or delete your existing database schemas. They are a common way of tracking changes to your database over time.



## Schema migrations

For this guide, we'll create a table called `employees` and see how we can make changes to it.

You will need to [install](/docs/guides/local-development#quickstart) the Supabase CLI and start the local development stack.

<StepHikeCompact>
  <StepHikeCompact.Step step={1}>
    <StepHikeCompact.Details title="Create your first migration file">
      To get started, generate a [new migration](/docs/reference/cli/supabase-migration-new) to store the SQL needed to create our `employees` table.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name="Terminal">
        ```bash name=Terminal
        supabase migration new create_employees_table
        ```
      </NamedCodeBlock>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>
</StepHikeCompact>

<StepHikeCompact>
  <StepHikeCompact.Step step={2}>
    <StepHikeCompact.Details title="Add the SQL to your migration file">
      This creates a new migration file in supabase/migrations directory.

      To that file, add the SQL to create this `employees` table.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name="supabase/migrations/<timestamp>_create_employees_table.sql">
        ```sql name=supabase/migrations/<timestamp>_create_employees_table.sql
        create table if not exists employees (
          id bigint primary key generated always as identity,
          name text not null,
          email text,
          created_at timestamptz default now()
        );
        ```
      </NamedCodeBlock>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>
</StepHikeCompact>

<StepHikeCompact>
  <StepHikeCompact.Step step={3}>
    <StepHikeCompact.Details title="Apply your first migration">
      Run this migration to create the `employees` table.

      Now you can visit your new `employees` table in the local Dashboard.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name="Terminal">
        ```bash name=Terminal
        supabase migration up
        ```
      </NamedCodeBlock>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>
</StepHikeCompact>

<StepHikeCompact>
  <StepHikeCompact.Step step={4}>
    <StepHikeCompact.Details title="Modify your employees table">
      Next, modify your `employees` table by adding a column for `department`.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name="Terminal">
        ```bash name=Terminal
        supabase migration new add_department_column
        ```
      </NamedCodeBlock>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>
</StepHikeCompact>

<StepHikeCompact>
  <StepHikeCompact.Step step={5}>
    <StepHikeCompact.Details title="Add a new column to your table">
      To that new migration file, add the SQL to create a new `department` column.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name="supabase/migrations/<timestamp>_add_department_column.sql">
        ```sql name=supabase/migrations/<timestamp>_add_department_column.sql
        alter table if exists public.employees
        add department text default 'Hooli';
        ```
      </NamedCodeBlock>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>
</StepHikeCompact>

<StepHikeCompact>
  <StepHikeCompact.Step step={6}>
    <StepHikeCompact.Details title="Apply your second migration">
      Run this migration to update your existing `employees` table.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name="Terminal">
        ```bash name=Terminal
        supabase migration up
        ```
      </NamedCodeBlock>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>
</StepHikeCompact>

Finally, you should see the `department` column added to your `employees` table in the local Dashboard.

<Admonition type="note">
  View the [complete code](https://github.com/supabase/supabase/tree/master/examples/database/employees) for this example on GitHub.
</Admonition>


### Seeding data

Now that you are managing your database with migrations scripts, it would be great have some seed data to use every time you reset the database.

<StepHikeCompact>
  <StepHikeCompact.Step step={1}>
    <StepHikeCompact.Details title="Populate your table">
      Create a seed script in supabase/seed.sql.

      To that file, add the SQL to insert data into your `employees` table.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name="supabase/seed.sql">
        ```sql name=supabase/seed.sql
        insert into public.employees
          (name)
        values
          ('Erlich Bachman'),
          ('Richard Hendricks'),
          ('Monica Hall');
        ```
      </NamedCodeBlock>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>
</StepHikeCompact>

<StepHikeCompact>
  <StepHikeCompact.Step step={2}>
    <StepHikeCompact.Details title="Reset your database">
      Reset your database to reapply migrations and populate with seed data.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name="Terminal">
        ```bash name=Terminal
        supabase db reset
        ```
      </NamedCodeBlock>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>
</StepHikeCompact>

You should now see the `employees` table, along with your seed data in the Dashboard! All of your database changes are captured in code, and you can reset to a known state at any time, complete with seed data.


### Diffing changes

This workflow is great if you know SQL and are comfortable creating tables and columns. If not, you can still use the Dashboard to create tables and columns, and then use the CLI to diff your changes and create migrations.

<StepHikeCompact>
  <StepHikeCompact.Step step={1}>
    <StepHikeCompact.Details title="Create your table from the Dashboard">
      Create a new table called `cities`, with columns `id`, `name` and `population`.

      Then generate a [schema diff](/docs/reference/cli/supabase-db-diff).
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name="Terminal">
        ```bash name=Terminal
        supabase db diff -f create_cities_table
        ```
      </NamedCodeBlock>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>
</StepHikeCompact>

<StepHikeCompact>
  <StepHikeCompact.Step step={2}>
    <StepHikeCompact.Details title="Add schema diff as a migration">
      A new migration file is created for you.

      Alternately, you can copy the table definitions directly from the Table Editor.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name="supabase/migrations/<timestamp>_create_cities_table.sql">
        ```sql name=supabase/migrations/<timestamp>_create_cities_table.sql
        create table "public"."cities" (
          "id" bigint primary key generated always as identity,
          "name" text,
          "population" bigint
        );
        ```
      </NamedCodeBlock>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>
</StepHikeCompact>

<StepHikeCompact>
  <StepHikeCompact.Step step={3}>
    <StepHikeCompact.Details title="Test your migration">
      Test your new migration file by resetting your local database.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name="Terminal">
        ```bash name=Terminal
        supabase db reset
        ```
      </NamedCodeBlock>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>
</StepHikeCompact>

The last step is deploying these changes to a live Supabase project.



## Deploy your project

You've been developing your project locally, making changes to your tables via migrations. It's time to deploy your project to the Supabase Platform and start scaling up to millions of users!

Head over to [Supabase](/dashboard) and create a new project to deploy to.

<StepHikeCompact>
  <StepHikeCompact.Step step={1}>
    <StepHikeCompact.Details title="Log in to the Supabase CLI">
      [Login](/docs/reference/cli/supabase-login) to the Supabase CLI using an auto-generated Personal Access Token.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name="Terminal">
        ```bash name=Terminal
        supabase login
        ```
      </NamedCodeBlock>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>
</StepHikeCompact>

<StepHikeCompact>
  <StepHikeCompact.Step step={2}>
    <StepHikeCompact.Details title="Link your project">
      [Link](/docs/reference/cli/supabase-link) to your remote project by selecting from the on-screen prompt.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name="Terminal">
        ```bash name=Terminal
        supabase link
        ```
      </NamedCodeBlock>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>
</StepHikeCompact>

<StepHikeCompact>
  <StepHikeCompact.Step step={3}>
    <StepHikeCompact.Details title="Deploy database migrations">
      [Push](/docs/reference/cli/supabase-db-push) your migrations to the remote database.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name="Terminal">
        ```bash name=Terminal
        supabase db push
        ```
      </NamedCodeBlock>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>
</StepHikeCompact>

<StepHikeCompact>
  <StepHikeCompact.Step step={4}>
    <StepHikeCompact.Details title="Deploy database seed data (optional)">
      [Push](/docs/reference/cli/supabase-db-push) your migrations and seed the remote database.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name="Terminal">
        ```bash name=Terminal
        supabase db push --include-seed
        ```
      </NamedCodeBlock>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>
</StepHikeCompact>

Visiting your live project on [Supabase](/dashboard/project/_), you'll see a new `employees` table, complete with the `department` column you added in the second migration above.



---
**Navigation:** [← Previous](./19-type-safe-sql-with-kysely.md) | [Index](./index.md) | [Next →](./21-production-checklist.md)
