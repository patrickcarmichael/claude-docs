**Navigation:** [← Previous](./04-voice-remixing.md) | [Index](./index.md) | [Next →](./06-cross-platform-voice-agents-with-expo-react-native.md)

# Find / create an API key at https://elevenlabs.io/app/settings/api-keys
ELEVENLABS_API_KEY=your_api_key


# The bot token you received from the BotFather.
TELEGRAM_BOT_TOKEN=your_bot_token


# A random secret chosen by you to secure the function.
FUNCTION_SECRET=random_secret
```

### Dependencies

The project uses a couple of dependencies:

* The open-source [grammY Framework](https://grammy.dev/) to handle the Telegram webhook requests.
* The [@supabase/supabase-js](https://supabase.com/docs/reference/javascript) library to interact with the Supabase database.
* The ElevenLabs [JavaScript SDK](/docs/quickstart) to interact with the speech-to-text API.

Since Supabase Edge Function uses the [Deno runtime](https://deno.land/), you don't need to install the dependencies, rather you can [import](https://docs.deno.com/examples/npm/) them via the `npm:` prefix.


## Code the Telegram Bot

In your newly created `scribe-bot/index.ts` file, add the following code:

```ts supabase/functions/scribe-bot/index.ts
import { Bot, webhookCallback } from 'https://deno.land/x/grammy@v1.34.0/mod.ts';
import 'jsr:@supabase/functions-js/edge-runtime.d.ts';
import { createClient } from 'jsr:@supabase/supabase-js@2';
import { ElevenLabsClient } from 'npm:elevenlabs@1.50.5';

console.log(`Function "elevenlabs-scribe-bot" up and running!`);

const elevenlabs = new ElevenLabsClient({
  apiKey: Deno.env.get('ELEVENLABS_API_KEY') || '',
});

const supabase = createClient(
  Deno.env.get('SUPABASE_URL') || '',
  Deno.env.get('SUPABASE_SERVICE_ROLE_KEY') || ''
);

async function scribe({
  fileURL,
  fileType,
  duration,
  chatId,
  messageId,
  username,
}: {
  fileURL: string;
  fileType: string;
  duration: number;
  chatId: number;
  messageId: number;
  username: string;
}) {
  let transcript: string | null = null;
  let languageCode: string | null = null;
  let errorMsg: string | null = null;
  try {
    const sourceFileArrayBuffer = await fetch(fileURL).then((res) => res.arrayBuffer());
    const sourceBlob = new Blob([sourceFileArrayBuffer], {
      type: fileType,
    });

    const scribeResult = await elevenlabs.speechToText.convert({
      file: sourceBlob,
      model_id: 'scribe_v1', // 'scribe_v1_experimental' is also available for new, experimental features
      tag_audio_events: false,
    });

    transcript = scribeResult.text;
    languageCode = scribeResult.language_code;

    // Reply to the user with the transcript
    await bot.api.sendMessage(chatId, transcript, {
      reply_parameters: { message_id: messageId },
    });
  } catch (error) {
    errorMsg = error.message;
    console.log(errorMsg);
    await bot.api.sendMessage(chatId, 'Sorry, there was an error. Please try again.', {
      reply_parameters: { message_id: messageId },
    });
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
  };
  console.log({ logLine });
  await supabase.from('transcription_logs').insert({ ...logLine, transcript });
}

const telegramBotToken = Deno.env.get('TELEGRAM_BOT_TOKEN');
const bot = new Bot(telegramBotToken || '');
const startMessage = `Welcome to the ElevenLabs Scribe Bot\\! I can transcribe speech in 99 languages with super high accuracy\\!
    \nTry it out by sending or forwarding me a voice message, video, or audio file\\!
    \n[Learn more about Scribe](https://elevenlabs.io/speech-to-text) or [build your own bot](https://elevenlabs.io/docs/cookbooks/speech-to-text/telegram-bot)\\!
  `;
bot.command('start', (ctx) => ctx.reply(startMessage.trim(), { parse_mode: 'MarkdownV2' }));

bot.on([':voice', ':audio', ':video'], async (ctx) => {
  try {
    const file = await ctx.getFile();
    const fileURL = `https://api.telegram.org/file/bot${telegramBotToken}/${file.file_path}`;
    const fileMeta = ctx.message?.video ?? ctx.message?.voice ?? ctx.message?.audio;

    if (!fileMeta) {
      return ctx.reply('No video|audio|voice metadata found. Please try again.');
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
    );

    // Reply to the user immediately to let them know we received their file.
    return ctx.reply('Received. Scribing...');
  } catch (error) {
    console.error(error);
    return ctx.reply(
      'Sorry, there was an error getting the file. Please try again with a smaller file!'
    );
  }
});

const handleUpdate = webhookCallback(bot, 'std/http');

Deno.serve(async (req) => {
  try {
    const url = new URL(req.url);
    if (url.searchParams.get('secret') !== Deno.env.get('FUNCTION_SECRET')) {
      return new Response('not allowed', { status: 405 });
    }

    return await handleUpdate(req);
  } catch (err) {
    console.error(err);
  }
});
```

### Code deep dive

There's a couple of things worth noting about the code. Let's step through it step by step.

<Steps>
  <Step title="Handling the incoming request">
    To handle the incoming request, use the `Deno.serve` handler. The handler checks whether the request has the correct secret and then passes the request to the `handleUpdate` function.

    ```ts {1,6,10}
    const handleUpdate = webhookCallback(bot, 'std/http');

    Deno.serve(async (req) => {
      try {
        const url = new URL(req.url);
        if (url.searchParams.get('secret') !== Deno.env.get('FUNCTION_SECRET')) {
          return new Response('not allowed', { status: 405 });
        }

        return await handleUpdate(req);
      } catch (err) {
        console.error(err);
      }
    });
    ```
  </Step>

  <Step title="Handle voice, audio, and video messages">
    The grammY frameworks provides a convenient way to [filter](https://grammy.dev/guide/filter-queries#combining-multiple-queries) for specific message types. In this case, the bot is listening for voice, audio, and video messages.

    Using the request context, the bot extracts the file metadata and then uses [Supabase Background Tasks](https://supabase.com/docs/guides/functions/background-tasks) `EdgeRuntime.waitUntil` to run the transcription in the background.

    This way you can provide an immediate response to the user and handle the transcription of the file in the background.

    ```ts {1,3,12,24}
    bot.on([':voice', ':audio', ':video'], async (ctx) => {
      try {
        const file = await ctx.getFile();
        const fileURL = `https://api.telegram.org/file/bot${telegramBotToken}/${file.file_path}`;
        const fileMeta = ctx.message?.video ?? ctx.message?.voice ?? ctx.message?.audio;

        if (!fileMeta) {
          return ctx.reply('No video|audio|voice metadata found. Please try again.');
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
        );

        // Reply to the user immediately to let them know we received their file.
        return ctx.reply('Received. Scribing...');
      } catch (error) {
        console.error(error);
        return ctx.reply(
          'Sorry, there was an error getting the file. Please try again with a smaller file!'
        );
      }
    });
    ```
  </Step>

  <Step title="Transcription with the ElevenLabs API">
    Finally, in the background worker, the bot uses the ElevenLabs JavaScript SDK to transcribe the file. Once the transcription is complete, the bot replies to the user with the transcript and writes a log entry to the Supabase database using [supabase-js](https://supabase.com/docs/reference/javascript).

    ```ts {29-38,43-46,54-65}
    const elevenlabs = new ElevenLabsClient({
      apiKey: Deno.env.get('ELEVENLABS_API_KEY') || '',
    });

    const supabase = createClient(
      Deno.env.get('SUPABASE_URL') || '',
      Deno.env.get('SUPABASE_SERVICE_ROLE_KEY') || ''
    );

    async function scribe({
      fileURL,
      fileType,
      duration,
      chatId,
      messageId,
      username,
    }: {
      fileURL: string;
      fileType: string;
      duration: number;
      chatId: number;
      messageId: number;
      username: string;
    }) {
      let transcript: string | null = null;
      let languageCode: string | null = null;
      let errorMsg: string | null = null;
      try {
        const sourceFileArrayBuffer = await fetch(fileURL).then((res) => res.arrayBuffer());
        const sourceBlob = new Blob([sourceFileArrayBuffer], {
          type: fileType,
        });

        const scribeResult = await elevenlabs.speechToText.convert({
          file: sourceBlob,
          model_id: 'scribe_v1', // 'scribe_v1_experimental' is also available for new, experimental features
          tag_audio_events: false,
        });

        transcript = scribeResult.text;
        languageCode = scribeResult.language_code;

        // Reply to the user with the transcript
        await bot.api.sendMessage(chatId, transcript, {
          reply_parameters: { message_id: messageId },
        });
      } catch (error) {
        errorMsg = error.message;
        console.log(errorMsg);
        await bot.api.sendMessage(chatId, 'Sorry, there was an error. Please try again.', {
          reply_parameters: { message_id: messageId },
        });
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
      };
      console.log({ logLine });
      await supabase.from('transcription_logs').insert({ ...logLine, transcript });
    }
    ```
  </Step>
</Steps>


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

Navigate to the [table editor](https://supabase.com/dashboard/project/_/editor) in your Supabase dashboard and you should see and empty `transcription_logs` table.

![Empty table](file:89230b62-48f1-4888-8056-90cec3e9706a)

Lastly, run the following command to deploy the Edge Function:

```bash
supabase functions deploy --no-verify-jwt scribe-bot
```

Navigate to the [Edge Functions view](https://supabase.com/dashboard/project/_/functions) in your Supabase dashboard and you should see the `scribe-bot` function deployed. Make a note of the function URL as you'll need it later, it should look something like `https://<project-ref>.functions.supabase.co/scribe-bot`.

![Edge Function deployed](file:79daa0af-4159-448d-9e0d-b6ce8711dda0)

### Set up the webhook

Set your bot's webhook url to `https://<PROJECT_REFERENCE>.functions.supabase.co/telegram-bot` (Replacing `<...>` with respective values). In order to do that, simply run a GET request to the following url (in your browser, for example):

```
https://api.telegram.org/bot<TELEGRAM_BOT_TOKEN>/setWebhook?url=https://<PROJECT_REFERENCE>.supabase.co/functions/v1/scribe-bot?secret=<FUNCTION_SECRET>
```

Note that the `FUNCTION_SECRET` is the secret you set in your `.env` file.

![Set webhook](file:099de7f2-755c-46f5-9da5-bfffdd062eef)

### Set the function secrets

Now that you have all your secrets set locally, you can run the following command to set the secrets in your Supabase project:

```bash
supabase secrets set --env-file supabase/functions/.env
```


## Test the bot

Finally you can test the bot by sending it a voice message, audio or video file.

![Test the bot](file:88b289be-a973-4531-8e17-18becdec0cd3)

After you see the transcript as a reply, navigate back to your table editor in the Supabase dashboard and you should see a new row in your `transcription_logs` table.

![New row in table](file:738adfc0-229a-48dc-acb4-a4971d894b7b)



# Asynchronous Speech to Text

> Learn how to use webhooks to receive asynchronous notifications when your transcription tasks are completed.


## Overview

Webhooks allow you to receive automatic notifications when your Speech to Text transcription tasks are completed, eliminating the need to continuously poll the API for status updates. This is particularly useful for long-running transcription jobs or when processing large volumes of audio files.

When a transcription is completed, ElevenLabs will send a POST request to your specified webhook URL with the transcription results, including the transcript text, language detection, and any metadata.


## Using webhooks

<Steps>
  <Step title="Create a webhook endpoint">
    First, create a webhook in the ElevenLabs dashboard. Navigate to your [webhooks settings](https://elevenlabs.io/app/settings/webhooks) and click "Create Webhook".

    <Frame background="subtle" caption="Create a new webhook in the ElevenLabs dashboard">
      <img src="file:68332a51-c4ed-4062-b203-a0a044584b89" alt="Create webhook interface" />
    </Frame>

    Configure your webhook with:

    * **Name**: A descriptive name for your webhook
    * **Callback URL**: Your publicly accessible HTTPS endpoint
    * **Webhook Auth Method**: Either `HMAC` or `OAuth`. It is up to the client to implement the verification mechanism. ElevenLabs sends headers that allow for verification but we do not enforce it.
  </Step>

  <Step title="Associate webhook with transcription tasks">
    Once created, you can associate the webhook with your speech-to-text tasks. In the dashboard, navigate to the webhook events section and link your webhooks to speech-to-text events.

    <Frame background="subtle" caption="Associate webhook with speech-to-text tasks">
      <img src="file:65ffcc7e-744d-4b58-bc26-fe72f6a9d6f6" alt="Webhook association interface" />
    </Frame>
  </Step>

  <Step title="Create an API key">
    [Create an API key in the dashboard here](https://elevenlabs.io/app/settings/api-keys), which you’ll use to securely [access the API](/docs/api-reference/authentication).

    Store the key as a managed secret and pass it to the SDKs either as a environment variable via an `.env` file, or directly in your app’s configuration depending on your preference.

    ```js title=".env"
    ELEVENLABS_API_KEY=<your_api_key_here>
    ```
  </Step>

  <Step title="Install the SDK">
    We'll also use the `dotenv` library to load our API key from an environment variable.

    <CodeBlocks>
      ```python
      pip install elevenlabs
      pip install python-dotenv
      ```

      ```typescript
      npm install @elevenlabs/elevenlabs-js
      npm install dotenv
      ```
    </CodeBlocks>
  </Step>

  <Step title="Make API calls with webhook parameter enabled">
    When making speech-to-text API calls, include the `webhook` parameter set to `true` to enable webhook notifications for that specific request.

    <CodeBlocks>
      ```python maxLines=0
      from dotenv import load_dotenv
      from elevenlabs.client import ElevenLabs

      load_dotenv()

      elevenlabs = ElevenLabs(
        api_key=os.getenv("ELEVENLABS_API_KEY"),
      )

      def transcribe_with_webhook(audio_file):
        try:
          result = elevenlabs.speech_to_text.convert(
            file=audio_file,
            model_id="scribe_v1",
            webhook=True,
          )
          print(f"Transcription started: {result.request_id}")
          return result
        except Exception as e:
          print(f"Error starting transcription: {e}")
          raise e
      ```

      ```typescript maxLines=0
      import { ElevenLabsClient } from '@elevenlabs/elevenlabs-js';

      const elevenlabs = new ElevenLabsClient({
        apiKey: process.env.ELEVENLABS_API_KEY,
      });

      async function transcribeWithWebhook(audioFile) {
        try {
          const result = await elevenlabs.speechToText.convert({
            file: audioFile,
            modelId: 'scribe_v1',
            webhook: true,
          });

          console.log('Transcription started:', result.requestId);
          return result;
        } catch (error) {
          console.error('Error starting transcription:', error);
          throw error;
        }
      }
      ```
    </CodeBlocks>
  </Step>
</Steps>


## Webhook payload

When a transcription is completed, your webhook endpoint will receive a POST request with the transcription and webhook data:

```json
{
  type: 'speech_to_text_transcription',
  data: {
    request_id: 'some-request-id-123',
    webhook_metadata: { ... }, // if provided in the convert request
    transcription: {
      "language_code": "en",
      "language_probability": 0.98,
      "text": "Hello world!",
      "words": [
        {
          "text": "Hello",
          "start": 0.0,
          "end": 0.5,
          "type": "word",
          "speaker_id": "speaker_1"
        },
        {
          "text": " ",
          "start": 0.5,
          "end": 0.5,
          "type": "spacing",
          "speaker_id": "speaker_1"
        },
        {
          "text": "world!",
          "start": 0.5,
          "end": 1.2,
          "type": "word",
          "speaker_id": "speaker_1"
        }
      ]
    }
  }
}
```

Please refer to the [Speech-to-text API](/docs/api-reference/speech-to-text) reference to learn about the details of the response structure.


## Implementing your webhook endpoint

Here's an example of how to implement a webhook endpoint to handle incoming notifications:

```javascript
import { ElevenLabsClient } from '@elevenlabs/elevenlabs-js';
import 'dotenv/config';
import express from 'express';

const elevenlabs = new ElevenLabsClient();

const app = express();
app.use(express.json());

const WEBHOOK_SECRET = process.env.WEBHOOK_SECRET;

app.post('/webhook/speech-to-text', (req, res) => {
  try {
    const signature = req.headers['elevenlabs-signature'];
    const payload = JSON.stringify(req.body);
    let event;

    try {
      // Verify the webhook signature.
      event = await elevenlabs.webhooks.constructEvent(payload, signature, WEBHOOK_SECRET);
    } catch (error) {
      return res.status(401).json({ error: 'Invalid signature' });
    }

    if (event.type === 'speech_to_text.completed') {
      const { requestId, status, text, language_code } = event.data;

      console.log(`Transcription ${requestId} completed`);
      console.log(`Language: ${language_code}`);
      console.log(`Text: ${text}`);

      processTranscription(requestId, text, language_code);
    } else if (status === 'failed') {
      console.error(`Transcription ${requestId} failed`);
      handleTranscriptionError(requestId);
    }

    res.status(200).json({ received: true });
  } catch (error) {
    console.error('Webhook error:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

async function processTranscription(requestId, text, language) {
  console.log('Processing completed transcription...');
}

async function handleTranscriptionError(requestId) {
  console.log('Handling transcription error...');
}

app.listen(3000, () => {
  console.log('Webhook server listening on port 3000');
});
```


## Security considerations

### Signature verification

Always verify webhook signatures to ensure requests came from ElevenLabs.

### HTTPS requirement

Webhook URLs must use HTTPS to ensure secure transmission of transcription data.

### Rate limiting

Implement rate limiting on your webhook endpoint to prevent abuse:

```javascript
import rateLimit from 'express-rate-limit';

const webhookLimiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100, // limit each IP to 100 requests per windowMs
  message: 'Too many webhook requests from this IP',
});

app.use('/webhook', webhookLimiter);
```

### Failure responses

Return appropriate HTTP status codes:

* `200-299`: Success - webhook processed successfully
* `400-499`: Client error - webhook will not be retried
* `500-599`: Server error - webhook will be retried


## Testing webhooks

### Local development

For local testing, use tools like [ngrok](https://ngrok.com/) to expose your local server:

```bash
ngrok http 3000
```

Use the provided HTTPS URL as your webhook endpoint during development.

### Webhook testing

You can test your webhook implementation by making a transcription request and monitoring your endpoint:

```javascript
async function testWebhook() {
  const audioFile = new File([audioBuffer], 'test.mp3', { type: 'audio/mp3' });

  const result = await elevenlabs.speechToText.convert({
    file: audioFile,
    modelId: 'scribe_v1',
    webhook: true,
  });

  console.log('Test transcription started:', result.requestId);
}
```



# Vercel AI SDK

> Use the ElevenLabs Provider in the Vercel AI SDK to transcribe speech from audio and video files.


# ElevenLabs Provider

The [ElevenLabs provider](https://ai-sdk.dev/providers/ai-sdk-providers/elevenlabs) provides support for the [ElevenLabs transcription API](https://elevenlabs.io/speech-to-text).


## Setup

The ElevenLabs provider is available in the `@ai-sdk/elevenlabs` module. You can install it with npm:

```npm
npm install @ai-sdk/elevenlabs
```


## Provider Instance

You can import the default provider instance `elevenlabs` from `@ai-sdk/elevenlabs`:

```ts
import { elevenlabs } from '@ai-sdk/elevenlabs';
```

If you need a customized setup, you can import `createElevenLabs` from `@ai-sdk/elevenlabs` and create a provider instance with your settings:

```ts
import { createElevenLabs } from '@ai-sdk/elevenlabs';

const elevenlabs = createElevenLabs({
  // custom settings, e.g.
  fetch: customFetch,
});
```

You can use the following optional settings to customize the ElevenLabs provider instance:

* **apiKey** *string*

  API key that is being sent using the `Authorization` header.
  It defaults to the `ELEVENLABS_API_KEY` environment variable.

* **headers** *Record\<string,string>*

  Custom headers to include in the requests.

* **fetch** *(input: RequestInfo, init?: RequestInit) => Promise\<Response>*

  Custom [fetch](https://developer.mozilla.org/en-US/docs/Web/API/fetch) implementation.
  Defaults to the global `fetch` function.
  You can use it as a middleware to intercept requests,
  or to provide a custom fetch implementation for e.g. testing.


## Transcription Models

You can create models that call the [ElevenLabs transcription API](https://elevenlabs.io/speech-to-text)
using the `.transcription()` factory method.

The first argument is the model id e.g. `scribe_v1`.

```ts
const model = elevenlabs.transcription('scribe_v1');
```

You can also pass additional provider-specific options using the `providerOptions` argument. For example, supplying the input language in ISO-639-1 (e.g. `en`) format can sometimes improve transcription performance if known beforehand.

```ts {7}
import { elevenlabs } from '@ai-sdk/elevenlabs';
import { experimental_transcribe as transcribe } from 'ai';

const result = await transcribe({
  model: elevenlabs.transcription('scribe_v1'),
  audio: new Uint8Array([1, 2, 3, 4]),
  providerOptions: { elevenlabs: { languageCode: 'en' } },
});
```

The following provider options are available:

* **languageCode** *string*

  An ISO-639-1 or ISO-639-3 language code corresponding to the language of the audio file.
  Can sometimes improve transcription performance if known beforehand.
  Defaults to `null`, in which case the language is predicted automatically.

* **tagAudioEvents** *boolean*

  Whether to tag audio events like (laughter), (footsteps), etc. in the transcription.
  Defaults to `true`.

* **numSpeakers** *integer*

  The maximum amount of speakers talking in the uploaded file.
  Can help with predicting who speaks when.
  The maximum amount of speakers that can be predicted is 32.
  Defaults to `null`, in which case the amount of speakers is set to the maximum value the model supports.

* **timestampsGranularity** *enum*

  The granularity of the timestamps in the transcription.
  Defaults to `'word'`.
  Allowed values: `'none'`, `'word'`, `'character'`.

* **diarize** *boolean*

  Whether to annotate which speaker is currently talking in the uploaded file.
  Defaults to `true`.

* **fileFormat** *enum*

  The format of input audio.
  Defaults to `'other'`.
  Allowed values: `'pcm_s16le_16'`, `'other'`.
  For `'pcm_s16le_16'`, the input audio must be 16-bit PCM at a 16kHz sample rate, single channel (mono), and little-endian byte order.
  Latency will be lower than with passing an encoded waveform.



# Music quickstart

> Learn how to generate music with Eleven Music.

This guide will show you how to generate music with Eleven Music.

<Info>
  The Eleven Music API is only available to paid users.
</Info>


## Using the Eleven Music API

<Steps>
  <Step title="Create an API key">
    [Create an API key in the dashboard here](https://elevenlabs.io/app/settings/api-keys), which you’ll use to securely [access the API](/docs/api-reference/authentication).

    Store the key as a managed secret and pass it to the SDKs either as a environment variable via an `.env` file, or directly in your app’s configuration depending on your preference.

    ```js title=".env"
    ELEVENLABS_API_KEY=<your_api_key_here>
    ```
  </Step>

  <Step title="Install the SDK">
    We'll also use the `dotenv` library to load our API key from an environment variable.

    <CodeBlocks>
      ```python
      pip install elevenlabs
      pip install python-dotenv
      ```

      ```typescript
      npm install @elevenlabs/elevenlabs-js
      npm install dotenv
      ```
    </CodeBlocks>
  </Step>

  <Step title="Make the API request">
    Create a new file named `example.py` or `example.mts`, depending on your language of choice and add the following code:

    <CodeBlocks>
      ```python
      # example.py
      from elevenlabs.client import ElevenLabs
      from elevenlabs.play import play
      import os
      from dotenv import load_dotenv
      load_dotenv()

      elevenlabs = ElevenLabs(
          api_key=os.getenv("ELEVENLABS_API_KEY"),
      )

      track = elevenlabs.music.compose(
          prompt="Create an intense, fast-paced electronic track for a high-adrenaline video game scene. Use driving synth arpeggios, punchy drums, distorted bass, glitch effects, and aggressive rhythmic textures. The tempo should be fast, 130–150 bpm, with rising tension, quick transitions, and dynamic energy bursts.",
          music_length_ms=10000,
      )

      play(track)
      ```

      ```typescript
      // example.mts
      import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";
      import "dotenv/config";

      const elevenlabs = new ElevenLabsClient();

      const track = await elevenlabs.music.compose({
        prompt: "Create an intense, fast-paced electronic track for a high-adrenaline video game scene. Use driving synth arpeggios, punchy drums, distorted bass, glitch effects, and aggressive rhythmic textures. The tempo should be fast, 130–150 bpm, with rising tension, quick transitions, and dynamic energy bursts.",
        musicLengthMs: 10000,
      });

      await play(track);
      ```
    </CodeBlocks>
  </Step>

  <Step title="Execute the code">
    <CodeBlocks>
      ```python
      python example.py
      ```

      ```typescript
      npx tsx example.mts
      ```
    </CodeBlocks>

    You should hear the generated music playing.
  </Step>
</Steps>


## Composition plans

A composition plan is a JSON object that describes the music you want to generate in finer detail. It can then be used to generate music with Eleven Music.

Using a plan is optional, but it can be used to generate more complex music by giving you more granular control over each section of the generation.

### Generating a composition plan

A composition plan can be generated from a prompt by using the API.

<CodeBlocks>
  ```python
  from elevenlabs.client import ElevenLabs
  from elevenlabs.play import play
  import os
  from dotenv import load_dotenv
  load_dotenv()

  elevenlabs = ElevenLabs(
  api_key=os.getenv("ELEVENLABS_API_KEY"),
  )

  composition_plan = elevenlabs.music.composition_plan.create(
      prompt="Create an intense, fast-paced electronic track for a high-adrenaline video game scene. Use driving synth arpeggios, punchy drums, distorted bass, glitch effects, and aggressive rhythmic textures. The tempo should be fast, 130–150 bpm, with rising tension, quick transitions, and dynamic energy bursts.",
      music_length_ms=10000,
  )

  print(composition_plan)
  ```

  ```typescript
  import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";
  import "dotenv/config";

  const elevenlabs = new ElevenLabsClient();

  const compositionPlan = await elevenlabs.music.compositionPlan.create({
    prompt: "Create an intense, fast-paced electronic track for a high-adrenaline video game scene. Use driving synth arpeggios, punchy drums, distorted bass, glitch effects, and aggressive rhythmic textures. The tempo should be fast, 130–150 bpm, with rising tension, quick transitions, and dynamic energy bursts.",
    musicLengthMs: 10000,
  });

  console.log(JSON.stringify(compositionPlan, null, 2));
  ```
</CodeBlocks>

The above will generate a composition plan similar to the following:

```json
{
  "positiveGlobalStyles": [
    "electronic",
    "fast-paced",
    "driving synth arpeggios",
    "punchy drums",
    "distorted bass",
    "glitch effects",
    "aggressive rhythmic textures",
    "high adrenaline"
  ],
  "negativeGlobalStyles": ["acoustic", "slow", "minimalist", "ambient", "lo-fi"],
  "sections": [
    {
      "sectionName": "Intro",
      "positiveLocalStyles": [
        "rising synth arpeggio",
        "glitch fx",
        "filtered noise sweep",
        "soft punchy kick building tension"
      ],
      "negativeLocalStyles": ["soft pads", "melodic vocals", "ambient textures"],
      "durationMs": 3000,
      "lines": []
    },
    {
      "sectionName": "Peak Drop",
      "positiveLocalStyles": [
        "full punchy drums",
        "distorted bass stab",
        "aggressive rhythmic hits",
        "rapid arpeggio sequences"
      ],
      "negativeLocalStyles": ["smooth transitions", "clean bass", "slow buildup"],
      "durationMs": 4000,
      "lines": []
    },
    {
      "sectionName": "Final Burst",
      "positiveLocalStyles": [
        "glitch stutter",
        "energy burst vox chopped sample",
        "quick transitions",
        "snare rolls"
      ],
      "negativeLocalStyles": ["long reverb tails", "fadeout", "gentle melodies"],
      "durationMs": 3000,
      "lines": []
    }
  ]
}
```

### Using a composition plan

A composition plan can be used to generate music by passing it to the `compose` method.

<CodeBlocks>
  ```python
  # You can pass in composition_plan or prompt, but not both.
  composition = elevenlabs.music.compose(
      composition_plan=composition_plan,
  )

  play(composition)
  ```

  ```typescript
  // You can pass in compositionPlan or prompt, but not both.
  const composition = await elevenlabs.music.compose({
      compositionPlan,
  });

  await play(composition);
  ```
</CodeBlocks>


## Generating music with details

For each music generation a composition plan is created from the prompt. You can opt to retrieve this plan by using the detailed response endpoint.

<CodeBlocks>
  ```python
  track_details = elevenlabs.music.compose_detailed(
      prompt="Create an intense, fast-paced electronic track for a high-adrenaline video game scene. Use driving synth arpeggios, punchy drums, distorted bass, glitch effects, and aggressive rhythmic textures. The tempo should be fast, 130–150 bpm, with rising tension, quick transitions, and dynamic energy bursts.",
      music_length_ms=10000,
  )

  print(track_details.json) # json contains composition_plan and song_metadata. The composition plan will include lyrics (if applicable)
  print(track_details.filename)
  # track_details.audio contains the audio bytes
  ```

  ```typescript
  const trackDetails = await elevenlabs.music.composeDetailed({
    prompt: 'Create an intense, fast-paced electronic track for a high-adrenaline video game scene. Use driving synth arpeggios, punchy drums, distorted bass, glitch effects, and aggressive rhythmic textures. The tempo should be fast, 30–150 bpm, with rising tension, quick transitions, and dynamic energy bursts.',
    musicLengthMs: 10000,
  });

  console.log(JSON.stringify(trackDetails.json, null, 2)); // json contains composition_plan and song_metadata. The composition plan will include lyrics (if applicable)
  console.log(trackDetails.filename);
  // trackDetails.audio contains the audio bytes
  ```
</CodeBlocks>


## Copyrighted material

Attempting to generate music or a composition plan that contains copyrighted material will result in an error. This includes mentioning a band or musician by name or using copyrighted lyrics.

### Prompts with copyrighted material

In these cases, the API will return a `bad_prompt` error that contains a suggestion of what prompt you could use instead.

<CodeBlocks>
  ```python
  try:
      # This will result in a bad_prompt error
      track = elevenlabs.music.compose(
          prompt="A song that sounds like 'Bohemian Rhapsody'",
          music_length_ms=10000,
      )
    except Exception as e:
        if e.body['detail']['status'] == 'bad_prompt':
            prompt_suggestion = e.body['detail']['data']['prompt_suggestion']
            print(prompt_suggestion) # Prints: An epic rock ballad with dramatic tempo changes, operatic harmonies, and a narrative structure that blends melancholy with bursts of theatrical intensity.

            # Use the prompt suggestion to generate the track instead
  ```

  ```typescript
  try {
    // This will result in a bad_prompt error
    const track = await elevenlabs.music.compose({
      prompt: "A song that sounds like 'Bohemian Rhapsody'",
      musicLengthMs: 10000,
    });
  } catch (error) {
    if (error.body.detail.status === 'bad_prompt') {
      const promptSuggestion = error.body.detail.data.prompt_suggestion;
      console.log(promptSuggestion); // Logs: An epic rock ballad with dramatic tempo changes, operatic harmonies, and a narrative structure that blends melancholy with bursts of theatrical intensity.

      // Use the prompt suggestion to generate the track instead
    }
  }
  ```
</CodeBlocks>

### Composition plans with copyrighted material

If styles using copyrighted material are used when generating a composition plan, a `bad_composition_plan` error will be returned. Similar to music prompts, a suggested composition plan `composition_plan_suggestion` will be returned within the error.

<Warning>
  In the case of a composition plan or prompt that contains harmful material, no suggested prompt
  will be returned.
</Warning>


## Next steps

Explore the [API reference](/docs/api-reference/music/compose) for more information on the Music API and its options.



# Music streaming

> Learn how to stream music with Eleven Music.

This guide will show you how to stream music with Eleven Music.

<Info>
  The Eleven Music API is only available to paid users.
</Info>


## Using the Eleven Music API

<Steps>
  <Step title="Create an API key">
    [Create an API key in the dashboard here](https://elevenlabs.io/app/settings/api-keys), which you’ll use to securely [access the API](/docs/api-reference/authentication).

    Store the key as a managed secret and pass it to the SDKs either as a environment variable via an `.env` file, or directly in your app’s configuration depending on your preference.

    ```js title=".env"
    ELEVENLABS_API_KEY=<your_api_key_here>
    ```
  </Step>

  <Step title="Install the SDK">
    We'll also use the `dotenv` library to load our API key from an environment variable.

    <CodeBlocks>
      ```python
      pip install elevenlabs
      pip install python-dotenv
      ```

      ```typescript
      npm install @elevenlabs/elevenlabs-js
      npm install dotenv
      ```
    </CodeBlocks>
  </Step>

  <Step title="Make the API request">
    Create a new file named `example.py` or `example.mts`, depending on your language of choice and add the following code:

    <CodeBlocks>
      ```python
      # example.py
      from elevenlabs.client import ElevenLabs
      from elevenlabs.play import play
      import os
      from io import BytesIO
      from dotenv import load_dotenv
      load_dotenv()

      elevenlabs = ElevenLabs(
          api_key=os.getenv("ELEVENLABS_API_KEY"),
      )

      stream = elevenlabs.music.stream(
          prompt="Create an intense, fast-paced electronic track for a high-adrenaline video game scene. Use driving synth arpeggios, punchy drums, distorted bass, glitch effects, and aggressive rhythmic textures. The tempo should be fast, 130–150 bpm, with rising tension, quick transitions, and dynamic energy bursts.",
          music_length_ms=10000,
      )

      # Create a BytesIO object to hold the audio data in memory
      audio_stream = BytesIO()

      # Write each chunk of audio data to the stream
      for chunk in stream:
          if chunk:
              audio_stream.write(chunk)

      # Reset stream position to the beginning
      audio_stream.seek(0)

      play(audio_stream)
      ```

      ```typescript
      // example.mts
      import { ElevenLabsClient, play } from "@elevenlabs/elevenlabs-js";
      import "dotenv/config";

      const elevenlabs = new ElevenLabsClient();

      const stream = await elevenlabs.music.stream({
        prompt: "Create an intense, fast-paced electronic track for a high-adrenaline video game scene. Use driving synth arpeggios, punchy drums, distorted bass, glitch effects, and aggressive rhythmic textures. The tempo should be fast, 130–150 bpm, with rising tension, quick transitions, and dynamic energy bursts.",
        musicLengthMs: 10000,
      });

      const chunks: Buffer[] = [];

      for await (const chunk of stream) {
          chunks.push(chunk);
      }

      const audioStream = Buffer.concat(chunks);

      await play(audioStream);
      ```
    </CodeBlocks>
  </Step>

  <Step title="Execute the code">
    <CodeBlocks>
      ```python
      python example.py
      ```

      ```typescript
      npx tsx example.mts
      ```
    </CodeBlocks>

    You should hear the generated music playing.
  </Step>
</Steps>


## Next steps

Explore the [API reference](/docs/api-reference/music/stream) for more information on the Speech to Text API and its options.



# Voice Changer quickstart

> Learn how to transform the voice of an audio file using the Voice Changer API.

This guide will show you how to transform the voice of an audio file using the Voice Changer API.


## Using the Voice Changer API

<Steps>
  <Step title="Create an API key">
    [Create an API key in the dashboard here](https://elevenlabs.io/app/settings/api-keys), which you’ll use to securely [access the API](/docs/api-reference/authentication).

    Store the key as a managed secret and pass it to the SDKs either as a environment variable via an `.env` file, or directly in your app’s configuration depending on your preference.

    ```js title=".env"
    ELEVENLABS_API_KEY=<your_api_key_here>
    ```
  </Step>

  <Step title="Install the SDK">
    We'll also use the `dotenv` library to load our API key from an environment variable.

    <CodeBlocks>
      ```python
      pip install elevenlabs
      pip install python-dotenv
      ```

      ```typescript
      npm install @elevenlabs/elevenlabs-js
      npm install dotenv
      ```
    </CodeBlocks>

    <Note>
      To play the audio through your speakers, you may be prompted to install [MPV](https://mpv.io/)
      and/or [ffmpeg](https://ffmpeg.org/).
    </Note>
  </Step>

  <Step title="Make the API request">
    Create a new file named `example.py` or `example.mts`, depending on your language of choice and add the following code:

    <CodeBlocks>
      ```python maxLines=0
      # example.py
      import os
      from dotenv import load_dotenv
      from elevenlabs.client import ElevenLabs
      from elevenlabs.play import play
      import requests
      from io import BytesIO

      load_dotenv()

      elevenlabs = ElevenLabs(
        api_key=os.getenv("ELEVENLABS_API_KEY"),
      )
      voice_id = "JBFqnCBsd6RMkjVDRZzb"

      audio_url = (
          "https://storage.googleapis.com/eleven-public-cdn/audio/marketing/nicole.mp3"
      )
      response = requests.get(audio_url)
      audio_data = BytesIO(response.content)

      audio_stream = elevenlabs.speech_to_speech.convert(
          voice_id=voice_id,
          audio=audio_data,
          model_id="eleven_multilingual_sts_v2",
          output_format="mp3_44100_128",
      )

      play(audio_stream)
      ```

      ```typescript maxLines=0
      // example.mts
      import { ElevenLabsClient, play } from "@elevenlabs/elevenlabs-js";
      import "dotenv/config";

      const elevenlabs = new ElevenLabsClient();
      const voiceId = "JBFqnCBsd6RMkjVDRZzb";

      const response = await fetch(
        "https://storage.googleapis.com/eleven-public-cdn/audio/marketing/nicole.mp3"
      );
      const audioBlob = new Blob([await response.arrayBuffer()], { type: "audio/mp3" });

      const audioStream = await elevenlabs.speechToSpeech.convert(voiceId, {
        audio: audioBlob,
        modelId: "eleven_multilingual_sts_v2",
        outputFormat: "mp3_44100_128",
      });

      await play(audioStream);
      ```
    </CodeBlocks>
  </Step>

  <Step title="Execute the code">
    <CodeBlocks>
      ```python
      python example.py
      ```

      ```typescript
      npx tsx example.mts
      ```
    </CodeBlocks>

    You should hear the transformed voice playing through your speakers.
  </Step>
</Steps>


## Next steps

Explore the [API reference](/docs/api-reference/speech-to-speech/convert) for more information on the Voice Changer API and its options.



# Voice Isolator quickstart

> Learn how to remove background noise from an audio file using the Voice Isolator API.

This guide will show you how to remove background noise from an audio file using the Voice Isolator API.


## Using the Voice Isolator API

<Steps>
  <Step title="Create an API key">
    [Create an API key in the dashboard here](https://elevenlabs.io/app/settings/api-keys), which you’ll use to securely [access the API](/docs/api-reference/authentication).

    Store the key as a managed secret and pass it to the SDKs either as a environment variable via an `.env` file, or directly in your app’s configuration depending on your preference.

    ```js title=".env"
    ELEVENLABS_API_KEY=<your_api_key_here>
    ```
  </Step>

  <Step title="Install the SDK">
    We'll also use the `dotenv` library to load our API key from an environment variable.

    <CodeBlocks>
      ```python
      pip install elevenlabs
      pip install python-dotenv
      ```

      ```typescript
      npm install @elevenlabs/elevenlabs-js
      npm install dotenv
      ```
    </CodeBlocks>

    <Note>
      To play the audio through your speakers, you may be prompted to install [MPV](https://mpv.io/)
      and/or [ffmpeg](https://ffmpeg.org/).
    </Note>
  </Step>

  <Step title="Make the API request">
    Create a new file named `example.py` or `example.mts`, depending on your language of choice and add the following code:

    <CodeBlocks>
      ```python maxLines=0
      # example.py
      import os
      from dotenv import load_dotenv
      from elevenlabs.client import ElevenLabs
      from elevenlabs.play import play
      import requests
      from io import BytesIO

      load_dotenv()

      elevenlabs = ElevenLabs(
        api_key=os.getenv("ELEVENLABS_API_KEY"),
      )

      audio_url = "https://storage.googleapis.com/eleven-public-cdn/audio/marketing/fin.mp3"
      response = requests.get(audio_url)
      audio_data = BytesIO(response.content)

      audio_stream = elevenlabs.audio_isolation.convert(audio=audio_data)

      play(audio_stream)
      ```

      ```typescript maxLines=0
      // example.mts
      import { ElevenLabsClient, play } from "@elevenlabs/elevenlabs-js";
      import "dotenv/config";

      const elevenlabs = new ElevenLabsClient();

      const audioUrl =
        "https://storage.googleapis.com/eleven-public-cdn/audio/marketing/fin.mp3";
      const response = await fetch(audioUrl);
      const audioBlob = new Blob([await response.arrayBuffer()], {
        type: "audio/mp3",
      });

      const audioStream = await elevenlabs.audioIsolation.convert({
        audio: audioBlob,
      });

      await play(audioStream);
      ```
    </CodeBlocks>
  </Step>

  <Step title="Execute the code">
    <CodeBlocks>
      ```python
      python example.py
      ```

      ```typescript
      npx tsx example.mts
      ```
    </CodeBlocks>

    You should hear the isolated voice playing through your speakers.
  </Step>
</Steps>


## Next steps

Explore the [API reference](/docs/api-reference/audio-isolation/audio-isolation) for more information on the Voice Changer API and its options.



# Dubbing quickstart

> Learn how to dub audio and video files across languages using the Dubbing API.

This guide will show you how to dub an audio file across languages. In this example we'll dub an audio file from English to Spanish.


## Using the Dubbing API

<Steps>
  <Step title="Create an API key">
    [Create an API key in the dashboard here](https://elevenlabs.io/app/settings/api-keys), which you’ll use to securely [access the API](/docs/api-reference/authentication).

    Store the key as a managed secret and pass it to the SDKs either as a environment variable via an `.env` file, or directly in your app’s configuration depending on your preference.

    ```js title=".env"
    ELEVENLABS_API_KEY=<your_api_key_here>
    ```
  </Step>

  <Step title="Install the SDK">
    We'll also use the `dotenv` library to load our API key from an environment variable.

    <CodeBlocks>
      ```python
      pip install elevenlabs
      pip install python-dotenv
      ```

      ```typescript
      npm install @elevenlabs/elevenlabs-js
      npm install dotenv
      ```
    </CodeBlocks>

    <Note>
      To play the audio through your speakers, you may be prompted to install [MPV](https://mpv.io/)
      and/or [ffmpeg](https://ffmpeg.org/).
    </Note>
  </Step>

  <Step title="Make the API request">
    Create a new file named `example.py` or `example.mts`, depending on your language of choice and add the following code:

    <CodeBlocks>
      ```python maxLines=0
      # example.py
      import os
      from dotenv import load_dotenv
      from elevenlabs.client import ElevenLabs
      from elevenlabs.play import play
      import requests
      from io import BytesIO
      import time

      load_dotenv()

      elevenlabs = ElevenLabs(
        api_key=os.getenv("ELEVENLABS_API_KEY"),
      )

      target_lang = "es"  # Spanish

      audio_url = (
          "https://storage.googleapis.com/eleven-public-cdn/audio/marketing/nicole.mp3"
      )
      response = requests.get(audio_url)

      audio_data = BytesIO(response.content)
      audio_data.name = "audio.mp3"

      # Start dubbing
      dubbed = elevenlabs.dubbing.create(
          file=audio_data, target_lang=target_lang
      )

      while True:
          status = elevenlabs.dubbing.get(dubbed.dubbing_id).status
          if status == "dubbed":
              dubbed_file = elevenlabs.dubbing.audio.get(dubbed.dubbing_id, target_lang)
              play(dubbed_file)
              break
          else:
              print("Audio is still being dubbed...")
              time.sleep(5)
      ```

      ```typescript maxLines=0
      // example.mts
      import { ElevenLabsClient, play } from "@elevenlabs/elevenlabs-js";
      import "dotenv/config";

      const elevenlabs = new ElevenLabsClient();

      const targetLang = "es"; // spanish
      const sourceAudio = await fetch(
        "https://storage.googleapis.com/eleven-public-cdn/audio/marketing/nicole.mp3"
      );
      const audioBlob = new Blob([await sourceAudio.arrayBuffer()], {
        type: "audio/mp3",
      });

      // Start dubbing
      const dubbed = await elevenlabs.dubbing.create({
        file: audioBlob,
        targetLang: targetLang,
      });

      while (true) {
        const { status } = await elevenlabs.dubbing.get(
          dubbed.dubbingId
        );
        if (status === "dubbed") {
          const dubbedFile = await elevenlabs.dubbing.audio.get(
            dubbed.dubbingId,
            targetLang
          );
          await play(dubbedFile);
          break;
        } else {
          console.log("Audio is still being dubbed...");
        }

        // Wait 5 seconds between checks
        await new Promise((resolve) => setTimeout(resolve, 5000));
      }
      ```
    </CodeBlocks>
  </Step>

  <Step title="Execute the code">
    <CodeBlocks>
      ```python
      python example.py
      ```

      ```typescript
      npx tsx example.mts
      ```
    </CodeBlocks>

    You should hear the dubbed audio file playing through your speakers.
  </Step>
</Steps>


## Next steps

Explore the [API reference](/docs/api-reference/dubbing/create) for more information on the Dubbing API and its options.



# Sound Effects quickstart

> Learn how to generate sound effects using the Sound Effects API.

This guide will show you how to generate sound effects using the Sound Effects API.


## Using the Sound Effects API

<Steps>
  <Step title="Create an API key">
    [Create an API key in the dashboard here](https://elevenlabs.io/app/settings/api-keys), which you’ll use to securely [access the API](/docs/api-reference/authentication).

    Store the key as a managed secret and pass it to the SDKs either as a environment variable via an `.env` file, or directly in your app’s configuration depending on your preference.

    ```js title=".env"
    ELEVENLABS_API_KEY=<your_api_key_here>
    ```
  </Step>

  <Step title="Install the SDK">
    We'll also use the `dotenv` library to load our API key from an environment variable.

    <CodeBlocks>
      ```python
      pip install elevenlabs
      pip install python-dotenv
      ```

      ```typescript
      npm install @elevenlabs/elevenlabs-js
      npm install dotenv
      ```
    </CodeBlocks>

    <Note>
      To play the audio through your speakers, you may be prompted to install [MPV](https://mpv.io/)
      and/or [ffmpeg](https://ffmpeg.org/).
    </Note>
  </Step>

  <Step title="Make the API request">
    Create a new file named `example.py` or `example.mts`, depending on your language of choice and add the following code:

    <CodeBlocks>
      ```python maxLines=0
      # example.py
      import os
      from dotenv import load_dotenv
      from elevenlabs.client import ElevenLabs
      from elevenlabs.play import play

      load_dotenv()

      elevenlabs = ElevenLabs(
        api_key=os.getenv("ELEVENLABS_API_KEY"),
      )
      audio = elevenlabs.text_to_sound_effects.convert(text="Cinematic Braam, Horror")

      play(audio)
      ```

      ```typescript
      // example.mts
      import { ElevenLabsClient, play } from "@elevenlabs/elevenlabs-js";
      import "dotenv/config";

      const elevenlabs = new ElevenLabsClient();

      const audio = await elevenlabs.textToSoundEffects.convert({
        text: "Cinematic Braam, Horror",
      });

      await play(audio);
      ```
    </CodeBlocks>
  </Step>

  <Step title="Execute the code">
    <CodeBlocks>
      ```python
      python example.py
      ```

      ```typescript
      npx tsx example.mts
      ```
    </CodeBlocks>

    You should hear your generated sound effect playing through your speakers.
  </Step>
</Steps>


## Next steps

Explore the [API reference](/docs/api-reference/speech-to-text/convert) for more information on the Speech to Text API and its options.



# Instant Voice Cloning API Cookbook

> Learn how to clone a voice using the Clone Voice API.

This guide will show you how to create an Instant Voice Clone using the Clone Voice API. To create an Instant Voice Clone via the dashboard, refer to the [Instant Voice Clone](/docs/product-guides/voices/voice-cloning/instant-voice-cloning) product guide.

For an outline of the differences between Instant Voice Clones and Professional Voice Clones, refer to the [Voices capability](/docs/capabilities/voices) guide.


## Using the Instant Voice Clone API

<Steps>
  <Step title="Create an API key">
    [Create an API key in the dashboard here](https://elevenlabs.io/app/settings/api-keys), which you’ll use to securely [access the API](/docs/api-reference/authentication).

    Store the key as a managed secret and pass it to the SDKs either as a environment variable via an `.env` file, or directly in your app’s configuration depending on your preference.

    ```js title=".env"
    ELEVENLABS_API_KEY=<your_api_key_here>
    ```
  </Step>

  <Step title="Install the SDK">
    We'll also use the `dotenv` library to load our API key from an environment variable.

    <CodeBlocks>
      ```python
      pip install elevenlabs
      pip install python-dotenv
      ```

      ```typescript
      npm install @elevenlabs/elevenlabs-js
      npm install dotenv
      ```
    </CodeBlocks>
  </Step>

  <Step title="Make the API request">
    Create a new file named `example.py` or `example.mts`, depending on your language of choice and add the following code:

    <CodeBlock>
      ```python maxLines=0
      # example.py
      import os
      from dotenv import load_dotenv
      from elevenlabs.client import ElevenLabs
      from io import BytesIO

      load_dotenv()

      elevenlabs = ElevenLabs(
        api_key=os.getenv("ELEVENLABS_API_KEY"),
      )

      voice = elevenlabs.voices.ivc.create(
          name="My Voice Clone",
          # Replace with the paths to your audio files.
          # The more files you add, the better the clone will be.
          files=[BytesIO(open("/path/to/your/audio/file.mp3", "rb").read())]
      )

      print(voice.voice_id)
      ```

      ```typescript maxLines=0
      // example.mts
      import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";
      import "dotenv/config";
      import fs from "node:fs";

      const elevenlabs = new ElevenLabsClient();

      const voice = await elevenlabs.voices.ivc.create({
          name: "My Voice Clone",
          // Replace with the paths to your audio files.
          // The more files you add, the better the clone will be.
          files: [
              fs.createReadStream(
                  "/path/to/your/audio/file.mp3",
              ),
          ],
      });

      console.log(voice.voiceId);
      ```
    </CodeBlock>
  </Step>

  <Step title="Execute the code">
    <CodeBlock>
      ```python
      python example.py
      ```

      ```typescript
      npx tsx example.mts
      ```
    </CodeBlock>

    You should see the voice ID printed to the console.
  </Step>
</Steps>


## Next steps

Explore the [API reference](/docs/api-reference/voices/ivc/create) for more information on creating a voice clone.



# Professional Voice Cloning API Cookbook

> Learn how to create a Professional Voice Clone using the PVC API.

This guide will show you how to create a Professional Voice Clone (PVC) using the PVC API. To create a PVC via the dashboard, refer to the [Professional Voice Clone](/docs/product-guides/voices/voice-cloning/professional-voice-cloning) product guide.

<Info>
  Creating a PVC requires you to be on the [Creator plan](https://elevenlabs.io/pricing) or above.
</Info>

For an outline of the differences between Instant Voice Clones and Professional Voice Clones, refer to the [Voices capability](/docs/capabilities/voices) guide.

<Warning>
  If you are unsure about what is permissible from a legal standpoint, please consult the [Terms of
  Service](https://elevenlabs.io/terms-of-use) and our [AI Safety
  information](https://elevenlabs.io/safety) for more information.
</Warning>

In terms of creating a PVC via the API, it contains considerably more steps than creating an Instant Voice Clone. This is due to the fact that PVCs are more complex and require more data and fine-tuning to create a high quality clone.


## Using the Professional Voice Clone API

<Steps>
  <Step title="Create an API key">
    [Create an API key in the dashboard here](https://elevenlabs.io/app/settings/api-keys), which you’ll use to securely [access the API](/docs/api-reference/authentication).

    Store the key as a managed secret and pass it to the SDKs either as a environment variable via an `.env` file, or directly in your app’s configuration depending on your preference.

    ```js title=".env"
    ELEVENLABS_API_KEY=<your_api_key_here>
    ```
  </Step>

  <Step title="Install the SDK">
    We'll also use the `dotenv` library to load our API key from an environment variable.

    <CodeBlocks>
      ```python
      pip install elevenlabs
      pip install python-dotenv
      ```

      ```typescript
      npm install @elevenlabs/elevenlabs-js
      npm install dotenv
      ```
    </CodeBlocks>
  </Step>

  <Step title="Create a PVC voice">
    Create a new file named `example.py` or `example.mts`, depending on your language of choice and add the following code to create a PVC voice:

    <CodeBlock>
      ```python maxLines=0
      # example.py
      import os
      import time
      import base64
      from contextlib import ExitStack
      from io import BytesIO
      from dotenv import load_dotenv
      from elevenlabs.client import ElevenLabs

      load_dotenv()

      elevenlabs = ElevenLabs(
        api_key=os.getenv("ELEVENLABS_API_KEY"),
      )

      voice = elevenlabs.voices.pvc.create(
          name="My Professional Voice Clone",
          language="en",
          description="A professional voice clone of my voice"
      )

      print(voice)
      ```

      ```typescript maxLines=0
      // example.mts
      import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";
      import "dotenv/config";
      import fs from "node:fs";

      const elevenlabs = new ElevenLabsClient();

      const voice = await elevenlabs.voices.pvc.create({
          name: "My Professional Voice Clone",
          language: "en",
          description: "A professional voice clone of my voice",
      });

      console.log(voice.voiceId);
      ```
    </CodeBlock>
  </Step>

  <Step title="Upload audio files">
    Next we'll upload the audio sample files that will be used to train the PVC. Review the [Tips and suggestions](/docs/product-guides/voices/voice-cloning/professional-voice-cloning#tips-and-suggestions) section of the PVC product guide for more information on how to get best results from your audio files.

    <CodeBlock>
      ```python maxLines=0
      # Define the list of file paths explicitly
      # Replace with the paths to your audio and/or video files.
      # The more files you add, the better the clone will be.
      sample_file_paths = [
          "/path/to/your/first_sample.mp3",
          "/path/to/your/second_sample.wav",
          "relative/path/to/another_sample.mp4"
      ]

      samples = None

      files_to_upload = []
      # Use ExitStack to manage multiple open files
      with ExitStack() as stack:
          for filepath in sample_file_paths:
              # Open each file and add it to the stack
              audio_file = stack.enter_context(open(filepath, "rb"))
              filename = os.path.basename(filepath)

              # Create a File object for the SDK
              files_to_upload.append(
                  BytesIO(audio_file.read())
              )

          samples = elevenlabs.voices.pvc.samples.create(
              voice_id=voice.voice_id,
              files=files_to_upload # Pass the list of File objects
          )
      ```

      ```typescript
      const samples = await elevenlabs.voices.pvc.samples.create(voice.voiceId, {
          // Replace with the paths to your audio and/or video files.
          // The more files you add, the better the clone will be.
          files: [fs.createReadStream("/path/to/your/audio/file.mp3")],
      })
      ```
    </CodeBlock>
  </Step>

  <Step title="Begin speaker separation">
    This step will attempt to separate the audio files into individual speakers. This is required if you are uploading audio with multiple speakers.

    <CodeBlock>
      ```python maxLines=0
      sample_ids_to_check = []
      for sample in samples:
          if sample.sample_id:
              print(f"Starting separation for sample: {sample.sample_id}")
              elevenlabs.voices.pvc.samples.speakers.separate(
                  voice_id=voice.voice_id,
                  sample_id=sample.sample_id
              )
              sample_ids_to_check.append(sample.sample_id)

      while sample_ids_to_check:
          # Create a copy of the list to iterate over, so we can remove items from the original
          ids_in_batch = list(sample_ids_to_check)
          for sample_id in ids_in_batch:
              status_response = elevenlabs.voices.pvc.samples.speakers.get(
                  voice_id=voice.voice_id,
                  sample_id=sample_id
              )
              status = status_response.status
              print(f"Sample {sample_id} status: {status}")
              if status == "completed" or status == "failed":
                  sample_ids_to_check.remove(sample_id)

          if sample_ids_to_check:
              # Wait before the next poll cycle
              time.sleep(5) # Wait for 5 seconds

      print("All samples have been processed or removed from polling.")
      ```

      ```typescript maxLines=0
      // Trigger the speaker separation action, this will take some time to complete
      for (const sample of samples) {
          if (sample.sampleId) {
              await elevenlabs.voices.pvc.samples.speakers.separate(voiceId, sample.sampleId);
          }
      }

      // Check the status of the speaker separation action
      const ids = samples.map((sample) => sample.sampleId);
      const interval = setInterval(async () => {
          // Poll the status of the speaker separation action
          for (const id of ids) {
              if (!id) continue;

              const { status } = await elevenlabs.voices.pvc.samples.speakers.get(voice.voiceId, id);
              console.log(`Sample ${id} status: ${status}`);
              if (status === "completed" || status === "failed") {
                  ids.splice(ids.indexOf(id), 1);
              }

              if (ids.length === 0) {
                  clearInterval(interval);
                  console.log("All samples have been processed or removed from polling");
              }
          }
      }, 5000);
      ```
    </CodeBlock>
  </Step>

  <Step title="Retrieve speaker audio">
    <Warning>
      Since the previous step will take some time to complete, the following step should be run in a separate process after the previous step has completed.
    </Warning>

    Once speaker separation is complete, you will have a list of speakers for each sample. In the case of samples with multiple speakers, you will have to pick the speaker you want to use for the PVC. To identify the speaker, you can retrieve the audio for each speaker and listen to them.

    <CodeBlock>
      ```python maxLines=0
      # Get the list of samples from the voice created in Step 3
      voice = elevenlabs.voices.get(voice_id=voice_id)

      samples = voice.samples

      # Loop over each sample and save the audio for each speaker to a file
      speaker_audio_output_dir = "path/to/speakers/"
      if not os.path.exists(speaker_audio_output_dir):
          os.makedirs(speaker_audio_output_dir)

      for sample in samples:
          speaker_info = elevenlabs.voices.pvc.samples.speakers.get(
              voice_id=voice.voice_id,
              sample_id=sample.sample_id
          )

          # Proceed only if separation is actually complete
          if getattr(speaker_info, 'status', 'unknown') != "completed":
              continue

          if hasattr(speaker_info, 'speakers') and speaker_info.speakers:
              speaker_list = speaker_info.speakers
              if isinstance(speaker_info.speakers, dict):
                  speaker_list = speaker_info.speakers.values()

              for speaker in speaker_list:
                  audio_response = elevenlabs.voices.pvc.samples.speakers.audio.get(
                      voice_id=voice.voice_id,
                      sample_id=sample.sample_id,
                      speaker_id=speaker.speaker_id
                  )

                  audio_base64 = audio_response.audio_base_64
                  audio_data = base64.b64decode(audio_base64)
                  output_filename = os.path.join(speaker_audio_output_dir, f"sample_{sample.sample_id}_speaker_{speaker.speaker_id}.mp3")

                  with open(output_filename, "wb") as f:
                      f.write(audio_data)
      ```

      ```typescript maxLines=0
      // Get the list of samples from the voice created in Step 3
      const { samples } = await elevenlabs.voices.get(voiceId);

      // After separation is completed, get the list of speakers and their audio
      if (samples) {
          for (const sample of samples) {
              if (!sample.sampleId) continue;

              const { speakers } = await elevenlabs.voices.pvc.samples.speakers.get(voiceId, sample.sampleId)

              if (speakers) {
                  for (const speaker of Object.values(speakers)) {
                      if (!speaker || !speaker.speakerId) continue;
                      const { audioBase64 } = await elevenlabs.voices.pvc.samples.speakers.audio.get(voiceId, sample.sampleId, speaker.speakerId);
                      const audioBuffer = Buffer.from(audioBase64, 'base64');

                      // Write the audio to a file
                      // Note which speaker ID you wish to use for the PVC
                      fs.writeFileSync(`path/to/speakers/sample_${sample.sampleId}_speaker_${speaker.speakerId}.mp3`, audioBuffer);
                  }
              }
          }
      }
      ```
    </CodeBlock>
  </Step>

  <Step title="Update samples with speaker IDs">
    Once speaker separation is complete, you can update the samples to select which speaker you want to use for the PVC.

    <CodeBlock>
      ```python
      elevenlabs.voices.pvc.samples.update(
          voice_id=voice.voice_id,
          sample_id=sample.sample_id,
          selected_speaker_ids=[speaker.speaker_id]
      )
      ```

      ```typescript
      await elevenlabs.voices.pvc.samples.update(voice.voiceId, sample.sampleId, {
          selectedSpeakerIds: [speaker.speakerId],
      })
      ```

      Repeat this process for each sample for with multiple speakers.
    </CodeBlock>
  </Step>

  <Step title="Verify the PVC">
    Before training can begin, a verification step is required to ensure you have permission to use the voice. First request the verification CAPTCHA.

    <CodeBlock>
      ```python
      captcha_response = elevenlabs.voices.pvc.verification.captcha.get(voice.voice_id)

      # Save captcha image to file
      captcha_buffer = base64.b64decode(captcha_response)
      with open('captcha.png', 'wb') as f:
          f.write(captcha_buffer)
      ```

      ```typescript
      const captchaResponse = await elevenlabs.voices.pvc.verification.captcha.get(voice.voiceId);

      // Save captcha image to file
      const captchaBuffer = Buffer.from(captchaResponse, 'base64');
      fs.writeFileSync('path/to/captcha.png', captchaBuffer);
      ```
    </CodeBlock>

    The image contains several lines of text that the voice owner will need to read out loud and record. Once done, submit the recording to verify the identity of the voice's owner.

    <CodeBlock>
      ```python
      elevenlabs.voices.pvc.verification.captcha.verify(
          voice_id=voice.voice_id,
          recording=open('path/to/recording.mp3', 'rb')
      )
      ```

      ```typescript
      await elevenlabs.voices.pvc.verification.captcha.verify(voice.voiceId, {
      	recording: fs.createReadStream("/path/to/recording.mp3"),
      })
      ```
    </CodeBlock>
  </Step>

  <Step title="(Optional) Request manual verification">
    If you are unable to verify the CAPTCHA, you can request manual verification. Note that this will take longer to process.

    This should only be used if the previous verification steps have failed or are not possible, for instance if the voice owner is visually impaired.

    For a list of the files that are required for manual verification, please contact support as each case may be unique.

    <CodeBlock>
      ```python
      elevenlabs.voices.pvc.verification.request(
          voice_id=voice.voice_id,
          files=[open('path/to/verification/files.txt', 'rb')],
      )
      ```

      ```typescript
      await elevenlabs.voices.pvc.verification.request(voice.voiceId, {
          files: [fs.createReadStream("/path/to/verification/files.txt")],
      });
      ```
    </CodeBlock>
  </Step>

  <Step title="Train the PVC">
    Next, begin the training process. This will take some time to complete based on the length and number of samples provided.

    <CodeBlock>
      ```python maxLines=0
      elevenlabs.voices.pvc.train(
          voice_id=voice.voice_id,
          # Specify the model the PVC should be trained on
          model_id="eleven_multilingual_v2"
      )

      # Poll the fine tuning status until it is complete or fails
      # This example specifically checks for the eleven_multilingual_v2 model
      while True:
          voice_details = elevenlabs.voices.get(voice_id=voice.voice_id)
          fine_tuning_state = None
          if voice_details.fine_tuning and voice_details.fine_tuning.state:
              fine_tuning_state = voice_details.fine_tuning.state.get("eleven_multilingual_v2")

          if fine_tuning_state:
              progress = None
              if voice_details.fine_tuning.progress and voice_details.fine_tuning.progress.get("eleven_multilingual_v2"):
                  progress = voice_details.fine_tuning.progress.get("eleven_multilingual_v2")
              print(f"Fine tuning progress: {progress}")

              if fine_tuning_state == "fine_tuned" or fine_tuning_state == "failed":
                  print("Fine tuning completed or failed")
                  break
          # Wait for 5 seconds before polling again
          time.sleep(5)
      ```

      ```typescript maxLines=0
      await elevenlabs.voices.pvc.train(voiceId, {
          // Specify the model the PVC should be trained on
          modelId: "eleven_multilingual_v2",
      });

      // Poll the fine tuning status until it is complete or fails
      // This example specifically checks for the eleven_multilingual_v2 model
      const interval = setInterval(async () => {
          const { fineTuning } = await elevenlabs.voices.get(voiceId);
          if (!fineTuning) return;

          console.log(`Fine tuning progress: ${fineTuning?.progress?.eleven_multilingual_v2}`);

          if (fineTuning?.state?.eleven_multilingual_v2 === "fine_tuned" || fineTuning?.state?.eleven_multilingual_v2 === "failed") {
              clearInterval(interval);
              console.log("Fine tuning completed or failed");
          }
      }, 5000);
      ```
    </CodeBlock>
  </Step>

  <Step title="Use the newly created voice">
    Once the PVC is verified, you can use it in the same way as any other voice. See the [Text to Speech quickstart](/docs/quickstart) for more information on how to use a voice.
  </Step>
</Steps>


## Next steps

Explore the [API reference](/docs/api-reference/voices/pvc/create) for more information on creating a Professional Voice Clone.



# Voice Design quickstart

> Learn how to design a voice via a prompt using the Voice Design API.

This guide will show you how to design a voice via a prompt using the Voice Design API.


## Using the Voice Design API

<Steps>
  <Step title="Create an API key">
    [Create an API key in the dashboard here](https://elevenlabs.io/app/settings/api-keys), which you’ll use to securely [access the API](/docs/api-reference/authentication).

    Store the key as a managed secret and pass it to the SDKs either as a environment variable via an `.env` file, or directly in your app’s configuration depending on your preference.

    ```js title=".env"
    ELEVENLABS_API_KEY=<your_api_key_here>
    ```
  </Step>

  <Step title="Install the SDK">
    We'll also use the `dotenv` library to load our API key from an environment variable.

    <CodeBlocks>
      ```python
      pip install elevenlabs
      pip install python-dotenv
      ```

      ```typescript
      npm install @elevenlabs/elevenlabs-js
      npm install dotenv
      ```
    </CodeBlocks>

    <Note>
      To play the audio through your speakers, you may be prompted to install [MPV](https://mpv.io/)
      and/or [ffmpeg](https://ffmpeg.org/).
    </Note>
  </Step>

  <Step title="Make the API request">
    Designing a voice via a prompt has two steps:

    1. Generate previews based on a prompt.
    2. Select the best preview and use it to create a new voice.

    We'll start by generating previews based on a prompt.

    Create a new file named `example.py` or `example.mts`, depending on your language of choice and add the following code:

    <CodeBlocks>
      ```python maxLines=0
      # example.py
      from dotenv import load_dotenv
      from elevenlabs.client import ElevenLabs
      from elevenlabs.play import play
      import base64

      load_dotenv()

      elevenlabs = ElevenLabs(
        api_key=os.getenv("ELEVENLABS_API_KEY"),
      )

      voices = elevenlabs.text_to_voice.design(
          model_id="eleven_multilingual_ttv_v2",
          voice_description="A massive evil ogre speaking at a quick pace. He has a silly and resonant tone.",
          text="Your weapons are but toothpicks to me. Surrender now and I may grant you a swift end. I've toppled kingdoms and devoured armies. What hope do you have against me?",
      )

      for preview in voices.previews:
          # Convert base64 to audio buffer
          audio_buffer = base64.b64decode(preview.audio_base_64)

          print(f"Playing preview: {preview.generated_voice_id}")

          play(audio_buffer)
      ```

      ```typescript maxLines=0
      // example.ts
      import { ElevenLabsClient, play } from "@elevenlabs/elevenlabs-js";
      import "dotenv/config";
      import { Readable } from 'node:stream';
      import { Buffer } from 'node:buffer';

      const elevenlabs = new ElevenLabsClient();

      const { previews } = await elevenlabs.textToVoice.design({
          modelId: "eleven_multilingual_ttv_v2",
          voiceDescription: "A massive evil ogre speaking at a quick pace. He has a silly and resonant tone.",
          text: "Your weapons are but toothpicks to me. Surrender now and I may grant you a swift end. I've toppled kingdoms and devoured armies. What hope do you have against me?",
      });

      for (const preview of previews) {
          // Convert base64 to buffer and create a Readable stream
          const audioStream = Readable.from(Buffer.from(preview.audioBase64, 'base64'));

          console.log(`Playing preview: ${preview.generatedVoiceId}`);

          // Play the audio using the stream
          await play(audioStream);
      }
      ```
    </CodeBlocks>
  </Step>

  <Step title="Execute the code">
    <CodeBlocks>
      ```python
      python example.py
      ```

      ```typescript
      npx tsx example.mts
      ```
    </CodeBlocks>

    You should hear the generated voice previews playing through your speakers, one at a time.
  </Step>

  <Step title="Add generated voice to your library">
    Once you've generated the previews and picked your favorite, you can add it to your voice library via the generated voice ID so it can be used with other APIs.

    <CodeBlocks>
      ```python
      voice = elevenlabs.text_to_voice.create(
          voice_name="Jolly giant",
          voice_description="A huge giant, at least as tall as a building. A deep booming voice, loud and jolly.",
          # The generated voice ID of the preview you want to use,
          # using the first in the list for this example
          generated_voice_id=voices.previews[0].generated_voice_id
      )

      print(voice.voice_id)
      ```

      ```typescript
      const voice = await elevenlabs.textToVoice.create({
          voiceName: "Jolly giant",
          voiceDescription: "A huge giant, at least as tall as a building. A deep booming voice, loud and jolly.",
          // The generated voice ID of the preview you want to use,
          // using the first in the list for this example
          generatedVoiceId: previews[0].generatedVoiceId
      });

      // The ID of the newly created voice, use this to reference the voice in other APIs
      console.log(voice.voiceId);
      ```
    </CodeBlocks>
  </Step>
</Steps>


## Next steps

Explore the [API reference](/docs/api-reference/text-to-voice/design) for more information on the Voice Design API and its options.



# Remix a voice

> Learn how to remix an existing voice to create a new one.

This guide will show you how to create an entirely new voice by remixing an existing one.


## Using the Voice Design API

<Steps>
  <Step title="Create an API key">
    [Create an API key in the dashboard here](https://elevenlabs.io/app/settings/api-keys), which you’ll use to securely [access the API](/docs/api-reference/authentication).

    Store the key as a managed secret and pass it to the SDKs either as a environment variable via an `.env` file, or directly in your app’s configuration depending on your preference.

    ```js title=".env"
    ELEVENLABS_API_KEY=<your_api_key_here>
    ```
  </Step>

  <Step title="Install the SDK">
    We'll also use the `dotenv` library to load our API key from an environment variable.

    <CodeBlocks>
      ```python
      pip install elevenlabs
      pip install python-dotenv
      ```

      ```typescript
      npm install @elevenlabs/elevenlabs-js
      npm install dotenv
      ```
    </CodeBlocks>

    <Note>
      To play the audio through your speakers, you may be prompted to install [MPV](https://mpv.io/)
      and/or [ffmpeg](https://ffmpeg.org/).
    </Note>
  </Step>

  <Step title="Make the API request">
    Remixing a voice is a two step process:

    1. Generate a preview of the new voice by providing a voice ID and a prompt.
    2. Create the new voice from the preview.

    We'll start by generating a preview of the new voice.

    Create a new file named `example.py` or `example.mts`, depending on your language of choice and add the following code:

    <Warning>
      You can only remix voices that were created by you. For example previously designed voices, IVC or PVC voices. You cannot remix voices from the voice library.
    </Warning>

    <CodeBlocks>
      ```python maxLines=0
      # example.py
      from dotenv import load_dotenv
      from elevenlabs.client import ElevenLabs
      from elevenlabs.play import play
      import base64

      load_dotenv()

      elevenlabs = ElevenLabs(
          api_key=os.getenv("ELEVENLABS_API_KEY"),
      )

      voices = elevenlabs.text_to_voice.remix(
          voice_id="JBFqnCBsd6RMkjVDRZzb"
          voice_description="Use a higher pitch and change to a Boston accent.",
          text="Of course I'm a Bostonian, I've lived here all my life!",
      )

      for preview in voices.previews:
          # Convert base64 to audio buffer
          audio_buffer = base64.b64decode(preview.audio_base_64)

          print(f"Playing preview: {preview.generated_voice_id}")

          play(audio_buffer)
      ```

      ```typescript maxLines=0
      // example.ts
      import { ElevenLabsClient, play } from "@elevenlabs/elevenlabs-js";
      import "dotenv/config";
      import { Readable } from 'node:stream';
      import { Buffer } from 'node:buffer';

      const elevenlabs = new ElevenLabsClient();

      const { previews } = await elevenlabs.textToVoice.remix("JBFqnCBsd6RMkjVDRZzb", {
          voiceDescription: "Use a higher pitch and change to a Boston accent.",
          text: "Of course I'm a Bostonian, I've lived here all my life!",
      });

      for (const preview of previews) {
          // Convert base64 to buffer and create a Readable stream
          const audioStream = Readable.from(Buffer.from(preview.audioBase64, 'base64'));

          console.log(`Playing preview: ${preview.generatedVoiceId}`);

          // Play the audio using the stream
          await play(audioStream);
      }
      ```
    </CodeBlocks>
  </Step>

  <Step title="Execute the code">
    <CodeBlocks>
      ```python
      python example.py
      ```

      ```typescript
      npx tsx example.mts
      ```
    </CodeBlocks>

    You should hear the generated voice previews playing through your speakers, one at a time.
  </Step>

  <Step title="Add generated voice to your library">
    Once you've generated the previews and picked your favorite, you can add it to your voice library via the generated voice ID so it can be used with other APIs.

    <CodeBlocks>
      ```python
      voice = elevenlabs.text_to_voice.create(
          voice_name="Bostonian",
          voice_description="A high pitched Bostonian accent.",
          # The generated voice ID of the preview you want to use,
          # using the first in the list for this example
          generated_voice_id=voices.previews[0].generated_voice_id
      )

      print(voice.voice_id)
      ```

      ```typescript
      const voice = await elevenlabs.textToVoice.create({
          voiceName: "Bostonian",
          voiceDescription: "A high pitched Bostonian accent.",
          // The generated voice ID of the preview you want to use,
          // using the first in the list for this example
          generatedVoiceId: previews[0].generatedVoiceId
      });

      // The ID of the newly created voice, use this to reference the voice in other APIs
      console.log(voice.voiceId);
      ```
    </CodeBlocks>
  </Step>
</Steps>


## Next steps

Explore the [API reference](/docs/api-reference/text-to-voice/remix) for more information on the Voice Design API and its options.



# Forced Alignment quickstart

> Learn how to use the Forced Alignment API to align text to audio.

This guide will show you how to use the Forced Alignment API to align text to audio.


## Using the Forced Alignment API

<Steps>
  <Step title="Create an API key">
    [Create an API key in the dashboard here](https://elevenlabs.io/app/settings/api-keys), which you’ll use to securely [access the API](/docs/api-reference/authentication).

    Store the key as a managed secret and pass it to the SDKs either as a environment variable via an `.env` file, or directly in your app’s configuration depending on your preference.

    ```js title=".env"
    ELEVENLABS_API_KEY=<your_api_key_here>
    ```
  </Step>

  <Step title="Install the SDK">
    We'll also use the `dotenv` library to load our API key from an environment variable.

    <CodeBlocks>
      ```python
      pip install elevenlabs
      pip install python-dotenv
      ```

      ```typescript
      npm install @elevenlabs/elevenlabs-js
      npm install dotenv
      ```
    </CodeBlocks>
  </Step>

  <Step title="Make the API request">
    Create a new file named `example.py` or `example.mts`, depending on your language of choice and add the following code:

    <CodeBlocks>
      ```python maxLines=0
      # example.py
      import os
      from io import BytesIO
      from elevenlabs.client import ElevenLabs
      import requests
      from dotenv import load_dotenv

      load_dotenv()

      elevenlabs = ElevenLabs(
          api_key=os.getenv("ELEVENLABS_API_KEY"),
      )

      audio_url = (
          "https://storage.googleapis.com/eleven-public-cdn/audio/marketing/nicole.mp3"
      )
      response = requests.get(audio_url)
      audio_data = BytesIO(response.content)

      # Perform the text-to-speech conversion
      transcription = elevenlabs.forced_alignment.create(
          file=audio_data,
          text="With a soft and whispery American accent, I'm the ideal choice for creating ASMR content, meditative guides, or adding an intimate feel to your narrative projects."
      )

      print(transcription)
      ```

      ```typescript maxLines=0
      // example.ts
      import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";
      import "dotenv/config";
      const elevenlabs = new ElevenLabsClient();

      const response = await fetch(
          "https://storage.googleapis.com/eleven-public-cdn/audio/marketing/nicole.mp3"
      );
      const audioBlob = new Blob([await response.arrayBuffer()], { type: "audio/mp3" });

      const transcript = await elevenlabs.forcedAlignment.create({
          file: audioBlob,
          text: "With a soft and whispery American accent, I'm the ideal choice for creating ASMR content, meditative guides, or adding an intimate feel to your narrative projects."
      })

      console.log(transcript);
      ```
    </CodeBlocks>
  </Step>

  <Step title="Execute the code">
    <CodeBlocks>
      ```python
      python example.py
      ```

      ```typescript
      npx tsx example.mts
      ```
    </CodeBlocks>

    You should see the transcript of the audio file with exact timestamps printed to the console.
  </Step>
</Steps>


## Next steps

Explore the [API reference](/docs/api-reference/forced-alignment/create) for more information on the Forced Alignment API and its options.



# Quickstart

> Build your first conversational agent in as little as 5 minutes.

In this guide, you'll learn how to create your first conversational agent. This will serve as a foundation for building conversational workflows tailored to your business use cases.


## Getting started

ElevenLabs Agents are managed either through the [Agents Platform dashboard](https://elevenlabs.io/app/agents), the [ElevenLabs API](/docs/api-reference) or the [Agents CLI](/docs/agents-platform/operate/cli).

<Frame caption="The assistant at the bottom right corner of this page is an example of an ElevenLabs agent, capable of answering questions about ElevenLabs, navigating pages & taking you to external resources." background="subtle">
  ![ElevenLabs Agents](file:1dd15163-480e-4c96-83ba-3e3d0f78ee24)
</Frame>


## Creating your first agent

In this quickstart guide we'll start by creating an agent via the API or the web dashboard. Next we'll test the agent, either by embedding it in your website or via the ElevenLabs dashboard.

<Tabs>
  <Tab title="Build an agent via the web dashboard">
    In this guide, we'll create a conversational support assistant capable of answering questions about your product, documentation, or service. This assistant can be embedded into your website or app to provide real-time support to your customers.

    <Frame caption="The assistant at the bottom right corner of this page is capable of answering questions about ElevenLabs, navigating pages & taking you to external resources." background="subtle">
      ![ElevenLabs Agents](file:1dd15163-480e-4c96-83ba-3e3d0f78ee24)
    </Frame>

    <Steps>
      <Step title="Sign in to ElevenLabs">
        Go to [elevenlabs.io](https://elevenlabs.io/sign-up) and sign in to or create your account.
      </Step>

      <Step title="Create a new assistant">
        In the **ElevenLabs Dashboard**, create a new assistant by entering a name and selecting the `Blank template` option.

        <Frame caption="Creating a new assistant" background="subtle">
          ![Dashboard](file:ffd9b16b-e608-4cc6-8a83-752eeb876bfc)
        </Frame>
      </Step>

      <Step title="Configure the assistant behavior">
        Go to the **Agent** tab to configure the assistant's behavior. Set the following:

        <Steps>
          <Step title="First message">
            This is the first message the assistant will speak out loud when a user starts a conversation.

            ```plaintext First message
            Hi, this is Alexis from <company name> support. How can I help you today?
            ```
          </Step>

          <Step title="System prompt">
            This prompt guides the assistant's behavior, tasks, and personality.

            Customize the following example with your company details:

            ```plaintext System prompt
            You are a friendly and efficient virtual assistant for [Your Company Name]. Your role is to assist customers by answering questions about the company's products, services, and documentation. You should use the provided knowledge base to offer accurate and helpful responses.

            Tasks:
            - Answer Questions: Provide clear and concise answers based on the available information.
            - Clarify Unclear Requests: Politely ask for more details if the customer's question is not clear.

            Guidelines:
            - Maintain a friendly and professional tone throughout the conversation.
            - Be patient and attentive to the customer's needs.
            - If unsure about any information, politely ask the customer to repeat or clarify.
            - Avoid discussing topics unrelated to the company's products or services.
            - Aim to provide concise answers. Limit responses to a couple of sentences and let the user guide you on where to provide more detail.
            ```
          </Step>
        </Steps>
      </Step>

      <Step title="Add a knowledge base">
        Go to the **Knowledge Base** section to provide your assistant with context about your business.

        This is where you can upload relevant documents & links to external resources:

        * Include documentation, FAQs, and other resources to help the assistant respond to customer inquiries.
        * Keep the knowledge base up-to-date to ensure the assistant provides accurate and current information.
      </Step>
    </Steps>

    Next we'll configure the voice for your assistant.

    <Steps>
      <Step title="Select a voice">
        In the **Voice** tab, choose a voice that best matches your assistant from the [voice library](https://elevenlabs.io/community):

        <Frame background="subtle">
          ![Voice settings](file:814f7ec1-c47f-4305-b174-ff740ecea1cf)
        </Frame>

        <Note>
           Using higher quality voices, models, and LLMs may increase response time. For an optimal customer experience, balance quality and latency based on your assistant's expected use case.
        </Note>
      </Step>

      <Step title="Testing your assistant">
        Press the **Test AI agent** button and try conversing with your assistant.
      </Step>
    </Steps>

    Configure evaluation criteria and data collection to analyze conversations and improve your assistant's performance.

    <Steps>
      <Step title="Configure evaluation criteria">
        Navigate to the **Analysis** tab in your assistant's settings to define custom criteria for evaluating conversations.

        <Frame background="subtle">
          ![Analysis settings](file:697a53df-adcc-48c9-91a1-91d86c192872)
        </Frame>

        Every conversation transcript is passed to the LLM to verify if specific goals were met. Results will either be `success`, `failure`, or `unknown`, along with a rationale explaining the chosen result.

        Let's add an evaluation criteria with the name `solved_user_inquiry`:

        ```plaintext Prompt
        The assistant was able to answer all of the queries or redirect them to a relevant support channel.

        Success Criteria:
        - All user queries were answered satisfactorily.
        - The user was redirected to a relevant support channel if needed.
        ```
      </Step>

      <Step title="Configure data collection">
        In the **Data Collection** section, configure details to be extracted from each conversation.

        Click **Add item** and configure the following:

        1. **Data type:** Select "string"
        2. **Identifier:** Enter a unique identifier for this data point: `user_question`
        3. **Description:** Provide detailed instructions for the LLM about how to extract the specific data from the transcript:

        ```plaintext Prompt
        Extract the user's questions & inquiries from the conversation.
        ```

        <Tip>
          Test your assistant by posing as a customer. Ask questions, evaluate its responses, and tweak the prompts until you're happy with how it performs.
        </Tip>
      </Step>

      <Step title="View conversation history">
        View evaluation results and collected data for each conversation in the **Call history** tab.

        <Frame background="subtle">
          ![Conversation history](file:ac55f4ab-b1a5-4fad-9084-2de905c84b0a)
        </Frame>

        <Tip>
          Regularly review conversation history to identify common issues and patterns.
        </Tip>
      </Step>
    </Steps>

    The newly created agent can be tested in a variety of ways, but the quickest way is to use the [ElevenLabs dashboard](https://elevenlabs.io/app/agents).

    <Info>
      The web dashboard uses our [React SDK](/docs/agents-platform/libraries/react) under the hood to handle real-time conversations.
    </Info>

    If instead you want to quickly test the agent in your own website, you can use the Agent widget. Simply paste the following HTML snippet into your website, taking care to replace `agent-id` with the ID of your agent.

    ```html
    <elevenlabs-convai agent-id="agent-id"></elevenlabs-convai>
    <script src="https://unpkg.com/@elevenlabs/convai-widget-embed" async type="text/javascript"></script>
    ```
  </Tab>

  <Tab title="Build an agent via the CLI">
    <Steps>
      <Step title="Install the CLI">
        ```bash
        npm install -g @elevenlabs/cli
        ```
      </Step>

      <Step title="Initialize a new project">
        ```bash
        elevenlabs agents init
        ```

        This creates the project structure with configuration directories and registry files.
      </Step>

      <Step title="Authenticate with ElevenLabs">
        [Create an API key in the dashboard here](https://elevenlabs.io/app/settings/api-keys), which you'll use to securely [use the CLI](/docs/api-reference/authentication).

        Then run the following command to authenticate with ElevenLabs:

        ```bash
        elevenlabs auth login
        ```

        Enter your ElevenLabs API key when prompted. The CLI will verify the key and store it securely.
      </Step>

      <Step title="Create the agent">
        Create your first agent using the assistant template:

        ```bash
        elevenlabs agents add "My Assistant" --template assistant
        ```
      </Step>

      <Step title="Push to ElevenLabs platform">
        ```bash
        elevenlabs agents push --agent "My Assistant"
        ```

        This uploads your local agent configuration to the ElevenLabs platform.
      </Step>

      <Step title="Test the agent">
        The newly created agent can be tested in a variety of ways, but the quickest way is to use the [ElevenLabs dashboard](https://elevenlabs.io/app/agents). From the dashboard, select your agent and click the **Test AI agent** button.

        <Info>
          The web dashboard uses our [React SDK](/docs/agents-platform/libraries/react) under the hood to handle real-time conversations.
        </Info>

        If instead you want to quickly test the agent in your own website, you can use the Agent widget. Use the CLI to generate the HTML snippet:

        ```bash
        elevenlabs agents widget "My Assistant"
        ```

        This will output the HTML snippet you can then paste directly into your website.
      </Step>
    </Steps>
  </Tab>

  <Tab title="Build an agent via the API">
    <Steps>
      <Step title="Create an API key">
        [Create an API key in the dashboard here](https://elevenlabs.io/app/settings/api-keys), which you’ll use to securely [access the API](/docs/api-reference/authentication).

        Store the key as a managed secret and pass it to the SDKs either as a environment variable via an `.env` file, or directly in your app’s configuration depending on your preference.

        ```js title=".env"
        ELEVENLABS_API_KEY=<your_api_key_here>
        ```
      </Step>

      <Step title="Install the SDK">
        We'll also use the `dotenv` library to load our API key from an environment variable.

        <CodeBlocks>
          ```python
          pip install elevenlabs
          pip install python-dotenv
          ```

          ```typescript
          npm install @elevenlabs/elevenlabs-js
          npm install dotenv
          ```
        </CodeBlocks>
      </Step>

      <Step title="Create the agent">
        Create a new file named `create_agent.py` or `createAgent.mts`, depending on your language of choice and add the following code:

        <CodeBlocks>
          ```python maxLines=0
          from dotenv import load_dotenv
          from elevenlabs.client import ElevenLabs
          import os
          load_dotenv()

          elevenlabs = ElevenLabs(
              api_key=os.getenv("ELEVENLABS_API_KEY"),
          )

          prompt = """
          You are a friendly and efficient virtual assistant for [Your Company Name].
          Your role is to assist customers by answering questions about the company's products, services,
          and documentation. You should use the provided knowledge base to offer accurate and helpful responses.

          Tasks:
          - Answer Questions: Provide clear and concise answers based on the available information.
          - Clarify Unclear Requests: Politely ask for more details if the customer's question is not clear.

          Guidelines:
          - Maintain a friendly and professional tone throughout the conversation.
          - Be patient and attentive to the customer's needs.
          - If unsure about any information, politely ask the customer to repeat or clarify.
          - Avoid discussing topics unrelated to the company's products or services.
          - Aim to provide concise answers. Limit responses to a couple of sentences and let the user guide you on where to provide more detail.
          """

          response = elevenlabs.conversational_ai.agents.create(
              name="My voice agent",
              tags=["test"], # List of tags to help classify and filter the agent
              conversation_config={
                  "tts": {
                      "voice_id": "21m00Tcm4TlvDq8ikWAM",
                      "model_id": "eleven_flash_v2"
                  },
                  "agent": {
                      "first_message": "Hi, this is Rachel from [Your Company Name] support. How can I help you today?",
                      "prompt": {
                          "prompt": prompt,
                      }
                  }
              }
          )

          print("Agent created with ID:", response.agent_id)
          ```

          ```typescript maxLines=0
          import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";
          import "dotenv/config";

          const elevenlabs = new ElevenLabsClient();

          const prompt = `
              You are a friendly and efficient virtual assistant for [Your Company Name].
              Your role is to assist customers by answering questions about the company's products, services,
              and documentation. You should use the provided knowledge base to offer accurate and helpful responses.

              Tasks:
              - Answer Questions: Provide clear and concise answers based on the available information.
              - Clarify Unclear Requests: Politely ask for more details if the customer's question is not clear.

              Guidelines:
              - Maintain a friendly and professional tone throughout the conversation.
              - Be patient and attentive to the customer's needs.
              - If unsure about any information, politely ask the customer to repeat or clarify.
              - Avoid discussing topics unrelated to the company's products or services.
              - Aim to provide concise answers. Limit responses to a couple of sentences and let the user guide you on where to provide more detail.
          `;

          const agent = await elevenlabs.conversationalAi.agents.create({
              name: "My voice agent",
              tags: ["test"], // List of tags to help classify and filter the agent
              conversationConfig: {
                  tts: {
                      voiceId: "21m00Tcm4TlvDq8ikWAM",
                      modelId: "eleven_flash_v2",
                  },
                  agent: {
                      firstMessage: "Hi, this is Rachel from [Your Company Name] support. How can I help you today?",
                      prompt: {
                          prompt,
                      }
                  },
              },
          });

          console.log(`Agent created with ID: ${agent.agentId}`);
          ```
        </CodeBlocks>

        <Note>
          The agent created above will have a `"test"` tag, this is useful to help classify and filter the agent. For example distinguishing between test agents and production agents.
        </Note>
      </Step>

      <Step title="Run the code">
        <CodeBlocks>
          ```python
          python create_agent.py
          ```

          ```typescript
          npx tsx createAgent.mts
          ```
        </CodeBlocks>

        The above will generate an agent with some baseline settings and print the ID of the agent to the console. We'll customize the agent in a subsequent step.
      </Step>

      <Step title="Test the agent">
        The newly created agent can be tested in a variety of ways, but the quickest way is to use the [ElevenLabs dashboard](https://elevenlabs.io/app/agents). From the dashboard, select your agent and click the **Test AI agent** button.

        <Info>
          The web dashboard uses our [React SDK](/docs/agents-platform/libraries/react) under the hood to handle real-time conversations.
        </Info>

        If instead you want to quickly test the agent in your own website, you can use the Agent widget. Simply paste the following HTML snippet into your website, taking care to replace `agent-id` with the ID of your agent.

        ```html
        <elevenlabs-convai agent-id="agent-id"></elevenlabs-convai>
        <script src="https://unpkg.com/@elevenlabs/convai-widget-embed" async type="text/javascript"></script>
        ```

        View the SDKs tab to learn how to embed the agent in your website or app using the provided SDKs.
      </Step>
    </Steps>
  </Tab>
</Tabs>


## Next steps

As a follow up to this quickstart guide, you can make your agent more effective by integrating:

* [Knowledge bases](/docs/agents-platform/customization/knowledge-base) to equip it with domain-specific information.
* [Tools](/docs/agents-platform/customization/tools) to allow it to perform tasks on your behalf.
* [Authorization](/docs/agents-platform/customization/authorization) to restrict access to certain conversations.
* [Evaluation criteria](/docs/agents-platform/customization/evaluation-criteria) to analyze conversations and improve its performance.
* [Data collection](/docs/agents-platform/customization/data-collection) to collect data about conversations and improve its performance.
* [Conversation history](/docs/agents-platform/customization/conversation-history) to view conversation history and improve its performance.



---
**Navigation:** [← Previous](./04-voice-remixing.md) | [Index](./index.md) | [Next →](./06-cross-platform-voice-agents-with-expo-react-native.md)
