**Navigation:** ← Previous | [Index](./index.md) | [Next →](./02-august-11-2025.md)

# ElevenLabs

> ElevenLabs is an AI audio research and deployment company.

{/* Light mode wave */}

<div id="overview-wave">
  <ElevenLabsWaveform color="blue" />
</div>

{/* Dark mode wave */}

<div id="overview-wave">
  <ElevenLabsWaveform color="gray" />
</div>


## Most popular

<CardGroup>
  <Card title="Developer quickstart" href="/docs/quickstart">
    Learn how to integrate ElevenLabs
  </Card>

  <Card title="Agents Platform" href="/docs/agents-platform/overview">
    Deploy voice agents in minutes
  </Card>

  <Card title="Product guides" href="/docs/product-guides/overview">
    Learn how to use ElevenLabs
  </Card>

  <Card title="API reference" href="/docs/api-reference/introduction">
    Dive into our API reference
  </Card>
</CardGroup>


## Meet the models

<CardGroup cols={2} rows={2}>
  <Card title={<div className="flex items-start gap-2"><div>Eleven v3</div><div><img src="file:d66e9c4a-daa5-42e3-84d7-a745c2eea254" alt="Alpha" /></div></div>} href="/docs/models#eleven-v3-alpha">
    Our most emotionally rich, expressive speech synthesis model

    <div>
      <div>
        Dramatic delivery and performance
      </div>

      <div>
        70+ languages supported
      </div>

      <div>
        3,000 character limit
      </div>

      <div>
        Support for natural multi-speaker dialogue
      </div>
    </div>
  </Card>

  <Card title="Eleven Multilingual v2" href="/docs/models#multilingual-v2">
    Lifelike, consistent quality speech synthesis model

    <div>
      <div>
        Natural-sounding output
      </div>

      <div>
        29 languages supported
      </div>

      <div>
        10,000 character limit
      </div>

      <div>
        Most stable on long-form generations
      </div>
    </div>
  </Card>

  <Card title="Eleven Flash v2.5" href="/docs/models#flash-v25">
    Our fast, affordable speech synthesis model

    <div>
      <div>
        Ultra-low latency (~75ms†)
      </div>

      <div>
        32 languages supported
      </div>

      <div>
        40,000 character limit
      </div>

      <div>
        Faster model, 50% lower price per character
      </div>
    </div>
  </Card>

  <Card title="Eleven Turbo v2.5" href="/docs/models#turbo-v25">
    High quality, low-latency model with a good balance of quality and speed

    <div>
      <div>
        High quality voice generation
      </div>

      <div>
        32 languages supported
      </div>

      <div>
        40,000 character limit
      </div>

      <div>
        Low latency (~250ms-300ms†), 50% lower price per character
      </div>
    </div>
  </Card>
</CardGroup>

<CardGroup cols={1} rows={1}>
  <Card title="Scribe v1" href="/docs/models#scribe-v1">
    State-of-the-art speech recognition model

    <div>
      <div>
        Accurate transcription in 99 languages
      </div>

      <div>
        Precise word-level timestamps
      </div>

      <div>
        Speaker diarization
      </div>

      <div>
        Dynamic audio tagging
      </div>
    </div>
  </Card>
</CardGroup>

<div>
  <div>
    [Explore all](/docs/models)
  </div>
</div>


## Capabilities

<CardGroup cols={2}>
  <Card href="/docs/capabilities/text-to-speech">
    <div>
      <div>
        <div>
          Text to Speech
        </div>

        <p>
          Convert text into lifelike speech
        </p>
      </div>
    </div>
  </Card>

  <Card href="/docs/capabilities/speech-to-text">
    <div>
      <div>
        <div>
          Speech to Text
        </div>

        <p>
          Transcribe spoken audio into text
        </p>
      </div>
    </div>
  </Card>

  <Card href="/docs/capabilities/voice-changer">
    <div>
      <div>
        <div>
          Voice changer
        </div>

        <p>
          Modify and transform voices
        </p>
      </div>
    </div>
  </Card>

  <Card href="/docs/capabilities/voice-isolator">
    <div>
      <div>
        <div>
          Voice isolator
        </div>

        <p>
          Isolate voices from background noise
        </p>
      </div>
    </div>
  </Card>

  <Card href="/docs/capabilities/dubbing">
    <div>
      <div>
        <div>
          Dubbing
        </div>

        <p>
          Dub audio and videos seamlessly
        </p>
      </div>
    </div>
  </Card>

  <Card href="/docs/capabilities/sound-effects">
    <div>
      <div>
        <div>
          Sound effects
        </div>

        <p>
          Create cinematic sound effects
        </p>
      </div>
    </div>
  </Card>

  <Card href="/docs/capabilities/voices">
    <div>
      <div>
        <div>
          Voices
        </div>

        <p>
          Clone and design custom voices
        </p>
      </div>
    </div>
  </Card>

  <Card href="/docs/agents-platform/overview">
    <div>
      <div>
        <div>
          Agents Platform
        </div>

        <p>
          Deploy intelligent voice agents
        </p>
      </div>
    </div>
  </Card>
</CardGroup>


## Product guides

<CardGroup cols={1}>
  <Card href="/docs/product-guides/overview">
    <div>
      <div>
        <div>
          Product guides
        </div>

        <p>
          Explore our product guides for step-by-step guidance
        </p>
      </div>

      <div>
        <img src="file:d81931dc-279a-4f2c-9203-f5237800cc89" alt="Voice library" />
      </div>
    </div>
  </Card>
</CardGroup>

<small>
  † Excluding application & network latency
</small>



# Developer quickstart

> Learn how to make your first ElevenLabs API request.

The ElevenLabs API provides a simple interface to state-of-the-art audio [models](/docs/models) and [features](/docs/api-reference/introduction). Follow this guide to learn how to create lifelike speech with our Text to Speech API. See the [developer guides](/docs/quickstart#explore-our-developer-guides) for more examples with our other products.


## Using the Text to Speech API

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

  <Step title="Make your first request">
    Create a new file named `example.py` or `example.mts`, depending on your language of choice and add the following code:

    {/* This snippet was auto-generated */}

    <CodeBlocks>
      ```python
      from dotenv import load_dotenv
      from elevenlabs.client import ElevenLabs
      from elevenlabs.play import play
      import os

      load_dotenv()

      elevenlabs = ElevenLabs(
        api_key=os.getenv("ELEVENLABS_API_KEY"),
      )

      audio = elevenlabs.text_to_speech.convert(
          text="The first move is what sets everything in motion.",
          voice_id="JBFqnCBsd6RMkjVDRZzb",
          model_id="eleven_multilingual_v2",
          output_format="mp3_44100_128",
      )

      play(audio)

      ```

      ```typescript
      import { ElevenLabsClient, play } from '@elevenlabs/elevenlabs-js';
      import { Readable } from 'stream';
      import 'dotenv/config';

      const elevenlabs = new ElevenLabsClient();
      const audio = await elevenlabs.textToSpeech.convert('JBFqnCBsd6RMkjVDRZzb', {
        text: 'The first move is what sets everything in motion.',
        modelId: 'eleven_multilingual_v2',
        outputFormat: 'mp3_44100_128',
      });

      const reader = audio.getReader();
      const stream = new Readable({
        async read() {
          const { done, value } = await reader.read();
          if (done) {
            this.push(null);
          } else {
            this.push(value);
          }
        },
      });

      await play(stream);

      ```
    </CodeBlocks>
  </Step>

  <Step title="Run the code">
    <CodeBlocks>
      ```python
      python example.py
      ```

      ```typescript
      npx tsx example.mts
      ```
    </CodeBlocks>

    You should hear the audio play through your speakers.
  </Step>
</Steps>


## Explore our developer guides

Now that you've made your first ElevenLabs API request, you can explore the other products that ElevenLabs offers.

<CardGroup cols={2}>
  <Card title="Speech to Text" icon="duotone pen-clip" href="/docs/cookbooks/speech-to-text/quickstart">
    Convert spoken audio into text
  </Card>

  <Card title="ElevenLabs Agents" icon="duotone comments" href="/docs/agents-platform/quickstart">
    Deploy conversational voice agents
  </Card>

  <Card title="Music" icon="duotone music" href="/docs/cookbooks/music/quickstart">
    Generate studio-quality music
  </Card>

  <Card title="Voice Cloning" icon="duotone clone" href="/docs/cookbooks/voices/instant-voice-cloning">
    Clone a voice
  </Card>

  <Card title="Voice Remixing" icon="duotone shuffle" href="/docs/cookbooks/voices/remix-a-voice">
    Remix a voice
  </Card>

  <Card title="Sound Effects" icon="duotone explosion" href="/docs/cookbooks/sound-effects">
    Generate sound effects from text
  </Card>

  <Card title="Voice Changer" icon="duotone message-pen" href="/docs/cookbooks/voice-changer">
    Transform the voice of an audio file
  </Card>

  <Card title="Voice Isolator" icon="duotone ear" href="/docs/cookbooks/voice-isolator">
    Isolate background noise from audio
  </Card>

  <Card title="Voice Design" icon="duotone paint-brush" href="/docs/cookbooks/voices/voice-design">
    Generate voices from a single text prompt
  </Card>

  <Card title="Dubbing" icon="duotone language" href="/docs/cookbooks/dubbing">
    Dub audio/video from one language to another
  </Card>

  <Card title="Forced Alignment" icon="duotone objects-align-left" href="/docs/cookbooks/forced-alignment">
    Generate time-aligned transcripts for audio
  </Card>
</CardGroup>



# Models

> Learn about the models that power the ElevenLabs API.


## Flagship models

### Text to Speech

<CardGroup cols={2} rows={2}>
  <Card title={<div className="flex items-start gap-2"><div>Eleven v3</div><div><img src="file:d66e9c4a-daa5-42e3-84d7-a745c2eea254" alt="Alpha" /></div></div>} href="/docs/models#eleven-v3-alpha">
    Our most emotionally rich, expressive speech synthesis model

    <div>
      <div>
        Dramatic delivery and performance
      </div>

      <div>
        70+ languages supported
      </div>

      <div>
        3,000 character limit
      </div>

      <div>
        Support for natural multi-speaker dialogue
      </div>
    </div>
  </Card>

  <Card title="Eleven Multilingual v2" href="/docs/models#multilingual-v2">
    Lifelike, consistent quality speech synthesis model

    <div>
      <div>
        Natural-sounding output
      </div>

      <div>
        29 languages supported
      </div>

      <div>
        10,000 character limit
      </div>

      <div>
        Most stable on long-form generations
      </div>
    </div>
  </Card>

  <Card title="Eleven Flash v2.5" href="/docs/models#flash-v25">
    Our fast, affordable speech synthesis model

    <div>
      <div>
        Ultra-low latency (~75ms†)
      </div>

      <div>
        32 languages supported
      </div>

      <div>
        40,000 character limit
      </div>

      <div>
        Faster model, 50% lower price per character
      </div>
    </div>
  </Card>

  <Card title="Eleven Turbo v2.5" href="/docs/models#turbo-v25">
    High quality, low-latency model with a good balance of quality and speed

    <div>
      <div>
        High quality voice generation
      </div>

      <div>
        32 languages supported
      </div>

      <div>
        40,000 character limit
      </div>

      <div>
        Low latency (~250ms-300ms†), 50% lower price per character
      </div>
    </div>
  </Card>
</CardGroup>

### Speech to Text

<CardGroup cols={1} rows={1}>
  <Card title="Scribe v1" href="/docs/models#scribe-v1">
    State-of-the-art speech recognition model

    <div>
      <div>
        Accurate transcription in 99 languages
      </div>

      <div>
        Precise word-level timestamps
      </div>

      <div>
        Speaker diarization
      </div>

      <div>
        Dynamic audio tagging
      </div>
    </div>
  </Card>
</CardGroup>

### Music

<CardGroup cols={1} rows={1}>
  <Card title="Eleven Music" href="/docs/models#eleven-music">
    Studio-grade music with natural language prompts in any style

    <div>
      <div>
        Complete control over genre, style, and structure
      </div>

      <div>
        Vocals or just instrumental
      </div>

      <div>
        Multilingual, including English, Spanish, German, Japanese and more
      </div>

      <div>
        Edit the sound and lyrics of individual sections or the whole song
      </div>
    </div>
  </Card>
</CardGroup>

<div>
  <div>
    [Pricing](https://elevenlabs.io/pricing/api)
  </div>
</div>


## Models overview

The ElevenLabs API offers a range of audio models optimized for different use cases, quality levels, and performance requirements.

| Model ID                     | Description                                                                                                                                                                                                           | Languages                                                                                                                                                                                       |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `eleven_v3`                  | Human-like and expressive speech generation                                                                                                                                                                           | [70+ languages](/docs/models#supported-languages)                                                                                                                                               |
| `eleven_ttv_v3`              | Human-like and expressive voice design model (Text to Voice)                                                                                                                                                          | [70+ languages](/docs/models#supported-languages)                                                                                                                                               |
| `eleven_multilingual_v2`     | Our most lifelike model with rich emotional expression                                                                                                                                                                | `en`, `ja`, `zh`, `de`, `hi`, `fr`, `ko`, `pt`, `it`, `es`, `id`, `nl`, `tr`, `fil`, `pl`, `sv`, `bg`, `ro`, `ar`, `cs`, `el`, `fi`, `hr`, `ms`, `sk`, `da`, `ta`, `uk`, `ru`                   |
| `eleven_flash_v2_5`          | Ultra-fast model optimized for real-time use (\~75ms†)                                                                                                                                                                | All `eleven_multilingual_v2` languages plus: `hu`, `no`, `vi`                                                                                                                                   |
| `eleven_flash_v2`            | Ultra-fast model optimized for real-time use (\~75ms†)                                                                                                                                                                | `en`                                                                                                                                                                                            |
| `eleven_turbo_v2_5`          | High quality, low-latency model with a good balance of quality and speed (\~250ms-300ms)                                                                                                                              | `en`, `ja`, `zh`, `de`, `hi`, `fr`, `ko`, `pt`, `it`, `es`, `id`, `nl`, `tr`, `fil`, `pl`, `sv`, `bg`, `ro`, `ar`, `cs`, `el`, `fi`, `hr`, `ms`, `sk`, `da`, `ta`, `uk`, `ru`, `hu`, `no`, `vi` |
| `eleven_turbo_v2`            | High quality, low-latency model with a good balance of quality and speed (\~250ms-300ms)                                                                                                                              | `en`                                                                                                                                                                                            |
| `eleven_multilingual_sts_v2` | State-of-the-art multilingual voice changer model (Speech to Speech)                                                                                                                                                  | `en`, `ja`, `zh`, `de`, `hi`, `fr`, `ko`, `pt`, `it`, `es`, `id`, `nl`, `tr`, `fil`, `pl`, `sv`, `bg`, `ro`, `ar`, `cs`, `el`, `fi`, `hr`, `ms`, `sk`, `da`, `ta`, `uk`, `ru`                   |
| `eleven_multilingual_ttv_v2` | State-of-the-art multilingual voice designer model (Text to Voice)                                                                                                                                                    | `en`, `ja`, `zh`, `de`, `hi`, `fr`, `ko`, `pt`, `it`, `es`, `id`, `nl`, `tr`, `fil`, `pl`, `sv`, `bg`, `ro`, `ar`, `cs`, `el`, `fi`, `hr`, `ms`, `sk`, `da`, `ta`, `uk`, `ru`                   |
| `eleven_english_sts_v2`      | English-only voice changer model (Speech to Speech)                                                                                                                                                                   | `en`                                                                                                                                                                                            |
| `scribe_v1`                  | State-of-the-art speech recognition model                                                                                                                                                                             | [99 languages](/docs/capabilities/speech-to-text#supported-languages)                                                                                                                           |
| `scribe_v1_experimental`     | State-of-the-art speech recognition model with experimental features: improved multilingual performance, reduced hallucinations during silence, fewer audio tags, and better handling of early transcript termination | [99 languages](/docs/capabilities/speech-to-text#supported-languages)                                                                                                                           |

<small>
  † Excluding application & network latency
</small>

### Deprecated models

<Error>
  The `eleven_monolingual_v1` and `eleven_multilingual_v1` models are deprecated and will be removed in the future. Please migrate to newer models for continued service.
</Error>

| Model ID                 | Description                                          | Languages                                      | Replacement model suggestion |
| ------------------------ | ---------------------------------------------------- | ---------------------------------------------- | ---------------------------- |
| `eleven_monolingual_v1`  | First generation TTS model (outclassed by v2 models) | `en`                                           | `eleven_multilingual_v2`     |
| `eleven_multilingual_v1` | First multilingual model (outclassed by v2 models)   | `en`, `fr`, `de`, `hi`, `it`, `pl`, `pt`, `es` | `eleven_multilingual_v2`     |


## Eleven v3 (alpha)

<Warning>
  This model is currently in alpha and is subject to change. Eleven v3 is not made for real-time
  applications like Agents Platform. When integrating Eleven v3 into your application, consider
  generating several generations and allowing the user to select the best one.
</Warning>

Eleven v3 is our latest and most advanced speech synthesis model. It is a state-of-the-art model that produces natural, life-like speech with high emotional range and contextual understanding across multiple languages.

This model works well in the following scenarios:

* **Character Discussions**: Excellent for audio experiences with multiple characters that interact with each other.
* **Audiobook Production**: Perfect for long-form narration with complex emotional delivery.
* **Emotional Dialogue**: Generate natural, lifelike dialogue with high emotional range and contextual understanding.

With Eleven v3 comes a new Text to Dialogue API, which allows you to generate natural, lifelike dialogue with high emotional range and contextual understanding across multiple languages. Eleven v3 can also be used with the Text to Speech API to generate natural, lifelike speech with high emotional range and contextual understanding across multiple languages.

Read more about the Text to Dialogue API [here](/docs/capabilities/text-to-dialogue).

### Supported languages

The Eleven v3 model supports 70+ languages, including:

*Afrikaans (afr), Arabic (ara), Armenian (hye), Assamese (asm), Azerbaijani (aze), Belarusian (bel), Bengali (ben), Bosnian (bos), Bulgarian (bul), Catalan (cat), Cebuano (ceb), Chichewa (nya), Croatian (hrv), Czech (ces), Danish (dan), Dutch (nld), English (eng), Estonian (est), Filipino (fil), Finnish (fin), French (fra), Galician (glg), Georgian (kat), German (deu), Greek (ell), Gujarati (guj), Hausa (hau), Hebrew (heb), Hindi (hin), Hungarian (hun), Icelandic (isl), Indonesian (ind), Irish (gle), Italian (ita), Japanese (jpn), Javanese (jav), Kannada (kan), Kazakh (kaz), Kirghiz (kir), Korean (kor), Latvian (lav), Lingala (lin), Lithuanian (lit), Luxembourgish (ltz), Macedonian (mkd), Malay (msa), Malayalam (mal), Mandarin Chinese (cmn), Marathi (mar), Nepali (nep), Norwegian (nor), Pashto (pus), Persian (fas), Polish (pol), Portuguese (por), Punjabi (pan), Romanian (ron), Russian (rus), Serbian (srp), Sindhi (snd), Slovak (slk), Slovenian (slv), Somali (som), Spanish (spa), Swahili (swa), Swedish (swe), Tamil (tam), Telugu (tel), Thai (tha), Turkish (tur), Ukrainian (ukr), Urdu (urd), Vietnamese (vie), Welsh (cym).*


## Multilingual v2

Eleven Multilingual v2 is our most advanced, emotionally-aware speech synthesis model. It produces natural, lifelike speech with high emotional range and contextual understanding across multiple languages.

The model delivers consistent voice quality and personality across all supported languages while maintaining the speaker's unique characteristics and accent.

This model excels in scenarios requiring high-quality, emotionally nuanced speech:

* **Character Voiceovers**: Ideal for gaming and animation due to its emotional range.
* **Professional Content**: Well-suited for corporate videos and e-learning materials.
* **Multilingual Projects**: Maintains consistent voice quality across language switches.
* **Stable Quality**: Produces consistent, high-quality audio output.

While it has a higher latency & cost per character than Flash models, it delivers superior quality for projects where lifelike speech is important.

Our multilingual v2 models support 29 languages:

*English (USA, UK, Australia, Canada), Japanese, Chinese, German, Hindi, French (France, Canada), Korean, Portuguese (Brazil, Portugal), Italian, Spanish (Spain, Mexico), Indonesian, Dutch, Turkish, Filipino, Polish, Swedish, Bulgarian, Romanian, Arabic (Saudi Arabia, UAE), Czech, Greek, Finnish, Croatian, Malay, Slovak, Danish, Tamil, Ukrainian & Russian.*


## Flash v2.5

Eleven Flash v2.5 is our fastest speech synthesis model, designed for real-time applications and Agents Platform. It delivers high-quality speech with ultra-low latency (\~75ms†) across 32 languages.

The model balances speed and quality, making it ideal for interactive applications while maintaining natural-sounding output and consistent voice characteristics across languages.

This model is particularly well-suited for:

* **Agents Platform**: Perfect for real-time voice agents and chatbots.
* **Interactive Applications**: Ideal for games and applications requiring immediate response.
* **Large-Scale Processing**: Efficient for bulk text-to-speech conversion.

With its lower price point and 75ms latency, Flash v2.5 is the cost-effective option for anyone needing fast, reliable speech synthesis across multiple languages.

Flash v2.5 supports 32 languages - all languages from v2 models plus:

*Hungarian, Norwegian & Vietnamese*

<small>
  † Excluding application & network latency
</small>

### Considerations

<AccordionGroup>
  <Accordion title="Text normalization with numbers">
    When using Flash v2.5, numbers aren't normalized by default in a way you might expect. For example, phone numbers might be read out in way that isn't clear for the user. Dates and currencies are affected in a similar manner.

    By default, normalization is disabled for Flash v2.5 to maintain the low latency. However, Enterprise customers can now enable text normalization for v2.5 models by setting the `apply_text_normalization` parameter to "on" in your request.

    The Multilingual v2 model does a better job of normalizing numbers, so we recommend using it for phone numbers and other cases where number normalization is important.

    For low-latency or Agents Platform applications, best practice is to have your LLM [normalize the text](/docs/best-practices/prompting/normalization) before passing it to the TTS model, or use the `apply_text_normalization` parameter (Enterprise plans only for v2.5 models).
  </Accordion>
</AccordionGroup>


## Turbo v2.5

Eleven Turbo v2.5 is our high-quality, low-latency model with a good balance of quality and speed.

This model is an ideal choice for all scenarios where you'd use Flash v2.5, but where you're willing to trade off latency for higher quality voice generation.


## Model selection guide

<AccordionGroup>
  <Accordion title="Requirements">
    <CardGroup cols={1}>
      <Card title="Quality">
        Use `eleven_multilingual_v2`

        Best for high-fidelity audio output with rich emotional expression
      </Card>

      <Card title="Low-latency">
        Use Flash models

        Optimized for real-time applications (\~75ms latency)
      </Card>

      <Card title="Multilingual">
        Use either either `eleven_multilingual_v2` or `eleven_flash_v2_5`

        Both support up to 32 languages
      </Card>

      <Card title="Balanced">
        Use `eleven_turbo_v2_5`

        Good balance between quality and speed
      </Card>
    </CardGroup>
  </Accordion>

  <Accordion title="Use case">
    <CardGroup cols={1}>
      <Card title="Content creation">
        Use `eleven_multilingual_v2`

        Ideal for professional content, audiobooks & video narration.
      </Card>

      <Card title="Agents Platform">
        Use `eleven_flash_v2_5`, `eleven_flash_v2`, `eleven_multilingual_v2`, `eleven_turbo_v2_5` or `eleven_turbo_v2`

        Perfect for real-time conversational applications
      </Card>

      <Card title="Voice changer">
        Use `eleven_multilingual_sts_v2`

        Specialized for Speech-to-Speech conversion
      </Card>
    </CardGroup>
  </Accordion>
</AccordionGroup>


## Character limits

The maximum number of characters supported in a single text-to-speech request varies by model.

| Model ID                 | Character limit | Approximate audio duration |
| ------------------------ | --------------- | -------------------------- |
| `eleven_v3`              | 3,000           | \~3 minutes                |
| `eleven_flash_v2_5`      | 40,000          | \~40 minutes               |
| `eleven_flash_v2`        | 30,000          | \~30 minutes               |
| `eleven_turbo_v2_5`      | 40,000          | \~40 minutes               |
| `eleven_turbo_v2`        | 30,000          | \~30 minutes               |
| `eleven_multilingual_v2` | 10,000          | \~10 minutes               |
| `eleven_multilingual_v1` | 10,000          | \~10 minutes               |
| `eleven_english_sts_v2`  | 10,000          | \~10 minutes               |
| `eleven_english_sts_v1`  | 10,000          | \~10 minutes               |

<Note>
  For longer content, consider splitting the input into multiple requests.
</Note>


## Scribe v1

Scribe v1 is our state-of-the-art speech recognition model designed for accurate transcription across 99 languages. It provides precise word-level timestamps and advanced features like speaker diarization and dynamic audio tagging.

This model excels in scenarios requiring accurate speech-to-text conversion:

* **Transcription Services**: Perfect for converting audio/video content to text
* **Meeting Documentation**: Ideal for capturing and documenting conversations
* **Content Analysis**: Well-suited for audio content processing and analysis
* **Multilingual Recognition**: Supports accurate transcription across 99 languages

Key features:

* Accurate transcription with word-level timestamps
* Speaker diarization for multi-speaker audio
* Dynamic audio tagging for enhanced context
* Support for 99 languages

Read more about Scribe v1 [here](/docs/capabilities/speech-to-text).


## Eleven Music

Eleven Music is our studio-grade music generation model. It allows you to generate music with natural language prompts in any style.

This model is excellent for the following scenarios:

* **Game Soundtracks**: Create immersive soundtracks for games
* **Podcast Backgrounds**: Enhance podcasts with professional music
* **Marketing**: Add background music to ad reels

Key features:

* Complete control over genre, style, and structure
* Vocals or just instrumental
* Multilingual, including English, Spanish, German, Japanese and more
* Edit the sound and lyrics of individual sections or the whole song

Read more about Eleven Music [here](/docs/capabilities/music).


## Concurrency and priority

Your subscription plan determines how many requests can be processed simultaneously and the priority level of your requests in the queue.
Speech to Text has an elevated concurrency limit.
Once the concurrency limit is met, subsequent requests are processed in a queue alongside lower-priority requests.
In practice this typically only adds \~50ms of latency.

| Plan       | Concurrency Limit<br /> (Multilingual v2) | Concurrency Limit<br /> (Turbo & Flash) | STT Concurrency Limit | Music Concurrency limit | Priority level |
| ---------- | ----------------------------------------- | --------------------------------------- | --------------------- | ----------------------- | -------------- |
| Free       | 2                                         | 4                                       | 8                     | N/A                     | 3              |
| Starter    | 3                                         | 6                                       | 12                    | 2                       | 4              |
| Creator    | 5                                         | 10                                      | 20                    | 2                       | 5              |
| Pro        | 10                                        | 20                                      | 40                    | 2                       | 5              |
| Scale      | 15                                        | 30                                      | 60                    | 3                       | 5              |
| Business   | 15                                        | 30                                      | 60                    | 3                       | 5              |
| Enterprise | Elevated                                  | Elevated                                | Elevated              | Highest                 | Highest        |

<Note>
  Startup grants recipients receive Scale level benefits.
</Note>

The response headers include `current-concurrent-requests` and `maximum-concurrent-requests` which you can use to monitor your concurrency.

### API requests per minute vs concurrent requests

It's important to understand that **API requests per minute** and **concurrent requests** are different metrics that depend on your usage patterns.

API requests per minute can be different from concurrent requests since it depends on the length of time for each request and how the requests are batched.

**Example 1: Spaced requests**
If you had 180 requests per minute that each took 1 second to complete and you sent them each 0.33 seconds apart, the max concurrent requests would be 3 and the average would be 3 since there would always be 3 in flight.

**Example 2: Batched requests**
However, if you had a different usage pattern such as 180 requests per minute that each took 3 seconds to complete but all fired at once, the max concurrent requests would be 180 and the average would be 9 (first 3 seconds of the minute saw 180 requests at once, final 57 seconds saw 0 requests).

Since our system cares about concurrency, requests per minute matter less than how long each of the requests take and the pattern of when they are sent.

How endpoint requests are made impacts concurrency limits:

* With HTTP, each request counts individually toward your concurrency limit.
* With a WebSocket, only the time where our model is generating audio counts towards your concurrency limit, this means a for most of the time an open websocket doesn't count towards your concurrency limit at all.

### Understanding concurrency limits

The concurrency limit associated with your plan should not be interpreted as the maximum number of simultaneous conversations, phone calls character voiceovers, etc that can be handled at once.
The actual number depends on several factors, including the specific AI voices used and the characteristics of the use case.

As a general rule of thumb, a concurrency limit of 5 can typically support up to approximately 100 simultaneous audio broadcasts.

This is because of the speed it takes for audio to be generated relative to the time it takes for the TTS request to be processed.
The diagram below is an example of how 4 concurrent calls with different users can be facilitated while only hitting 2 concurrent requests.

<Frame background="subtle">
  <img src="file:a013851a-7cc1-4e94-b90b-c626482cca56" alt="Concurrency limits" />
</Frame>

<AccordionGroup>
  <Accordion title="Building AI Voice Agents">
    Where TTS is used to facilitate dialogue, a concurrency limit of 5 can support about 100 broadcasts for balanced conversations between AI agents and human participants.

    For use cases in which the AI agent speaks less frequently than the human, such as customer support interactions, more than 100 simultaneous conversations could be supported.
  </Accordion>

  <Accordion title="Character voiceovers">
    Generally, more than 100 simultaneous character voiceovers can be supported for a concurrency limit of 5.

    The number can vary depending on the character’s dialogue frequency, the length of pauses, and in-game actions between lines.
  </Accordion>

  <Accordion title="Live Dubbing">
    Concurrent dubbing streams generally follow the provided heuristic.

    If the broadcast involves periods of conversational pauses (e.g. because of a soundtrack, visual scenes, etc), more simultaneous dubbing streams than the suggestion may be possible.
  </Accordion>
</AccordionGroup>

If you exceed your plan's concurrency limits at any point and you are on the Enterprise plan, model requests may still succeed, albeit slower, on a best efforts basis depending on available capacity.

<Note>
  To increase your concurrency limit & queue priority, [upgrade your subscription
  plan](https://elevenlabs.io/pricing/api).

  Enterprise customers can request a higher concurrency limit by contacting their account manager.
</Note>

### Scale testing concurrency limits

Scale testing can be useful to identify client side scaling issues and to verify concurrency limits are set correctly for your usecase.

It is heavily recommended to test end-to-end workflows as close to real world usage as possible, simulating and measuring how many users can be supported is the recommended methodology for achieving this. It is important to:

* Simulate users, not raw requests
* Simulate typical user behavior such as waiting for audio playback, user speaking or transcription to finish before making requests
* Ramp up the number of users slowly over a period of minutes
* Introduce randomness to request timings and to the size of requests
* Capture latency metrics and any returned error codes from the API

For example, to test an agent system designed to support 100 simultaneous conversations you would create up to 100 individual "users" each simulating a conversation. Conversations typically consist of a repeating cycle of \~10 seconds of user talking, followed by the TTS API call for \~150 characters, followed by \~10 seconds of audio playback to the user. Therefore, each user should follow the pattern of making a websocket Text-to-Speech API call for 150 characters of text every 20 seconds, with a small amount of randomness introduced to the wait period and the number of characters requested. The test would consist of spawning one user per second until 100 exist and then testing for 10 minutes in total to test overall stability.

<AccordionGroup>
  <Accordion title="Scale testing script example">
    This example uses [locust](https://locust.io/) as the testing framework with direct API calls to the ElevenLabs API.

    It follows the example listed above, testing a conversational agent system with each user sending 1 request every 20 seconds.

    <CodeBlocks>
      ```python title="Python" {12}
      import json
      import random
      import time
      import gevent
      import locust
      from locust import User, task, events, constant_throughput
      import websocket

      # Averages up to 10 seconds of audio when played, depends on the voice speed
      DEFAULT_TEXT = (
          "Hello, this is a test message. I am testing if a long input will cause issues for the model "
          "like this sentence. "
      )

      TEXT_ARRAY = [
          "Hello.",
          "Hello, this is a test message.",
          DEFAULT_TEXT,
          DEFAULT_TEXT * 2,
          DEFAULT_TEXT * 3
      ]

      # Custom command line arguments
      @events.init_command_line_parser.add_listener
      def on_parser_init(parser):
          parser.add_argument("--api-key", default="YOUR_API_KEY", help="API key for authentication")
          parser.add_argument("--encoding", default="mp3_22050_32", help="Encoding")
          parser.add_argument("--text", default=DEFAULT_TEXT, help="Text to use")
          parser.add_argument("--use-text-array", default="false", help="Text to use")
          parser.add_argument("--voice-id", default="aria", help="Text to use")


      class WebSocketTTSUser(User):
          # Each user will send a request every 20 seconds, regardless of how long each request takes
          wait_time = constant_throughput(0.05)

          def __init__(self, *args, **kwargs):
              super().__init__(*args, **kwargs)
              self.api_key = self.environment.parsed_options.api_key
              self.voice_id = self.environment.parsed_options.voice_id
              self.text = self.environment.parsed_options.text
              self.encoding = self.environment.parsed_options.encoding
              self.use_text_array = self.environment.parsed_options.use_text_array
              if self.use_text_array:
                  self.text = random.choice(TEXT_ARRAY)
              self.all_recieved = False

          @task
          def tts_task(self):
              # Do jitter waiting of up to 1 second
              # Users appear to be spawned every second so this ensures requests are not aligned
              gevent.sleep(random.random())

              max_wait_time = 10

              # Connection details
              uri = f"{self.environment.host}/v1/text-to-speech/{self.voice_id}/stream-input?auto_mode=true&output_format={self.encoding}"
              headers = {"xi-api-key": self.api_key}

              ws = None
              self.all_recieved = False
              try:
                  init_msg = {"text": " "}
                  # Use proper header format for websocket - this is case sensitive!
                  ws = websocket.create_connection(uri, header=headers)
                  ws.send(json.dumps(init_msg))

                  # Start measuring after websocket initiated but before any messages are sent
                  send_request_time = time.perf_counter()
                  ws.send(json.dumps({"text": self.text}))

                  # Send to flush and receive the audio
                  ws.send(json.dumps({"text": ""}))

                  def _receive():
                      t_first_response = None
                      audio_size = 0
                      try:
                          while True:
                              # Wait up to 10 seconds for a response
                              ws.settimeout(max_wait_time)
                              response = ws.recv()
                              response_data = json.loads(response)

                              if "audio" in response_data and response_data["audio"]:
                                  audio_size = audio_size + len(response_data["audio"])

                              if t_first_response is None:
                                  t_first_response = time.perf_counter()
                                  first_byte_ms = (
                                      t_first_response - send_request_time
                                  ) * 1000
                                  if audio_size is None:
                                      # The first response should always have audio
                                      locust.events.request.fire(
                                          request_type="websocket",
                                          name="Bad Response (no audio)",
                                          response_time=first_byte_ms,
                                          response_length=audio_size,
                                          exception=Exception("Response has no audio"),
                                      )
                                      break

                              if "isFinal" in response_data and response_data["isFinal"]:
                                  # Fire this event once finished streaming, but report the important TTFB metric
                                  locust.events.request.fire(
                                      request_type="websocket",
                                      name="TTS Stream Success (First Byte)",
                                      response_time=first_byte_ms,
                                      response_length=audio_size,
                                      exception=None,
                                  )
                                  break

                      except websocket.WebSocketTimeoutException:
                          locust.events.request.fire(
                              request_type="websocket",
                              name="TTS Stream Timeout",
                              response_time=max_wait_time * 1000,
                              response_length=audio_size,
                              exception=Exception("Timeout waiting for response"),
                          )
                      except Exception as e:
                          # Typically JSON decode error if the server returns HTTP backoff error
                          locust.events.request.fire(
                              request_type="websocket",
                              name="TTS Stream Failure",
                              response_time=0,
                              response_length=0,
                              exception=e,
                          )
                      finally:
                          self.all_recieved = True

                  gevent.spawn(_receive)

                  # Sleep until recieved so new tasks aren't spawned
                  while not self.all_recieved:
                      gevent.sleep(1)

              except websocket.WebSocketTimeoutException:
                  locust.events.request.fire(
                      request_type="websocket",
                      name="TTS Stream Timeout",
                      response_time=max_wait_time * 1000,
                      response_length=0,
                      exception=Exception("Timeout waiting for response"),
                  )
              except Exception as e:
                  locust.events.request.fire(
                      request_type="websocket",
                      name="TTS Stream Failure",
                      response_time=0,
                      response_length=0,
                      exception=e,
                  )
              finally:
                  # Try and close the websocket gracefully
                  try:
                      if ws:
                          ws.close()
                  except Exception:
                      pass

      ```
    </CodeBlocks>
  </Accordion>
</AccordionGroup>



# November 5, 2025

### UI

- **Improved notifications**: Updated notification system to display notifications relevant to the active platform you're viewing, providing a more focused and contextual experience.

### Agents Platform

- **Dynamic variable transfer destinations**: Agent transfers now support dynamic variables for phone numbers and SIP URIs, enabling runtime-determined transfer destinations based on conversation context.
- **MCP tool configuration overrides**: Added the ability to create, update, retrieve, and delete custom configuration overrides for specific MCP Server tools, allowing fine-grained control over tool behavior and parameters.

### Text to Dialogue

- **Timestamps and voice segments**: Text to Dialogue now supports timestamped outputs with character-level alignment and voice segment tracking, making it easier to synchronize dialogue with animations or subtitles.

### Music API

- **Stem separation**: Added new stem separation endpoint to isolate different audio components (vocals, drums, bass, instruments) from existing music tracks.
- **Increased prompt length**: Music generation now supports prompts up to 4,100 characters, with individual lyric lines supporting up to 200 characters.

### Security

- **Single-use tokens**: Introduced time-limited single-use token generation for secure operations, providing enhanced security for sensitive API operations.

### SDK Releases

#### JavaScript SDK

- [v2.22.0](https://github.com/elevenlabs/elevenlabs-js/releases/tag/v2.22.0) - Updated with latest API schema changes including workspace model approvals and MCP tool configuration endpoints.
- [v2.21.0](https://github.com/elevenlabs/elevenlabs-js/releases/tag/v2.21.0) - Added support for intercepting raw WebSocket messages via a general `message` handler, allowing developers to access all messages beyond the standard callbacks, including undocumented message types like `agent_tool_response`.

#### Python SDK

- [v2.22.0](https://github.com/elevenlabs/elevenlabs-python/releases/tag/v2.22.0) - Updated with latest API schema changes including workspace model approvals and MCP tool configuration endpoints.
- [v2.21.0](https://github.com/elevenlabs/elevenlabs-python/releases/tag/v2.21.0) - Replaced print statements with proper logging to support better debugging and production use cases.

#### Agents Packages

- [@elevenlabs/agents-cli@0.6.1](https://github.com/elevenlabs/packages/releases/tag/%40elevenlabs/agents-cli%400.6.1) - Package deprecated in favor of the unified [ElevenLabs CLI](https://www.npmjs.com/package/@elevenlabs/cli).
- [@elevenlabs/react@0.9.1](https://github.com/elevenlabs/packages/releases/tag/%40elevenlabs/react%400.9.1) - Fixed issue where `end_call` tool wasn't properly ending conversations, and improved React Native reconnection logic after manual disconnection.
- [@elevenlabs/react-native@0.5.2](https://github.com/elevenlabs/packages/releases/tag/%40elevenlabs/react-native%400.5.2) - Fixed issue where `end_call` tool wasn't properly ending conversations, and improved reconnection logic after manual disconnection.
- [@elevenlabs/client@0.9.1](https://github.com/elevenlabs/packages/releases/tag/%40elevenlabs/client%400.9.1) - Fixed issue where `end_call` tool wasn't properly ending conversations, and improved React Native reconnection logic.

#### Android SDK

- [v0.4.0](https://github.com/elevenlabs/elevenlabs-android/releases/tag/v0.4.0) - Improved type safety by using `ConversationMode` enums instead of strings, migrated from LiveData to StateFlow with backward compatibility support, and fixed bug where agents wouldn't end calls when requested.

#### iOS SDK

- [v2.0.16](https://github.com/elevenlabs/elevenlabs-swift-sdk/releases/tag/v2.0.16) - Fixed issue where the `end_call` tool wasn't properly ending conversations, ensuring agents can correctly terminate calls.

#### CLI

- [@elevenlabs/cli@0.2.0](https://github.com/elevenlabs/cli/releases/tag/%40elevenlabs/cli%400.2.0) - Removed `--env` flag support for virtual environment isolation. This feature will be reintroduced once proper environment isolation is supported in the product.

### API

#### TLS

Our TLS endpoints no longer allow some older and insecure cipher modes. Most clients should not be affected as they already negotiate a modern cipher mode.

<Accordion title="View API changes">


## New Endpoints

### Agents Platform

#### MCP Tool Configuration

- [POST /v1/convai/mcp-servers/{mcp_server_id}/tool-configs](/docs/api-reference/mcp/tool-configuration/create) - Create configuration overrides for a specific MCP tool.
- [GET /v1/convai/mcp-servers/{mcp_server_id}/tool-configs/{tool_name}](/docs/api-reference/mcp/tool-configuration/get) - Retrieve configuration overrides for a specific MCP tool.
- [PATCH /v1/convai/mcp-servers/{mcp_server_id}/tool-configs/{tool_name}](/docs/api-reference/mcp/tool-configuration/update) - Update configuration overrides for a specific MCP tool.
- [DELETE /v1/convai/mcp-servers/{mcp_server_id}/tool-configs/{tool_name}](/docs/api-reference/mcp/tool-configuration/delete) - Remove configuration overrides for a specific MCP tool.

### Text to Dialogue

- [POST /v1/text-to-dialogue/with-timestamps](/docs/api-reference/text-to-dialogue/convert-with-timestamps) - Generate dialogue with character-level alignment and voice segment information.
- [POST /v1/text-to-dialogue/stream/with-timestamps](/docs/api-reference/text-to-dialogue/stream-with-timestamps) - Stream dialogue generation with character-level alignment and voice segment information.

### Tokens

- [POST /v1/single-use-token/{token_type}](/docs/api-reference/single-use/create) - Generate time-limited single-use tokens for secure operations.

### Music API

- [POST /v1/music/stem-separation](/docs/api-reference/music/separate-stems) - Separate audio into individual stems (vocals, drums, bass, instruments). Accepts multipart file upload and returns a ZIP archive.


## Updated Endpoints

### Text to Dialogue

- [Text to dialogue with timestamps](/docs/api-reference/text-to-dialogue/convert-with-timestamps)

  - Added `voice_segments` array with required `dialogue_input_index` field to track which dialogue input each segment corresponds to
  - Enhanced response schema with character-level alignment data

- [Stream text to dialogue with timestamps](/docs/api-reference/text-to-dialogue/stream-with-timestamps)
  - Added streaming support for `voice_segments` with character-level alignment
  - Includes `dialogue_input_index` in voice segment chunks

### Music

- Music prompt endpoints updated:
  - Maximum prompt length increased from previous limit to 4,100 characters
  - Lyrics lines now support up to 200 characters per line

### Workspace

- [Get workspace resource](/docs/api-reference/workspace/resources/get)
  - Added `dashboard` and `dashboard_configuration` to `WorkspaceResourceType` enum
  - Response schema changes (breaking compatibility - see migration notes below)

### Billing

- [Get subscription](/docs/api-reference/user/subscription/get)
  - Added `next_billing_period` field (required) to `PendingSubscriptionSwitchResponseModel`
  - Added `subtotal_cents` and `tax_cents` (nullable) to `InvoiceResponseModel` for better invoice breakdown

### Agents Platform

#### Batch Calling

- [Submit batch calling](/docs/api-reference/batch-calling/create)

  - Made `agent_phone_number_id` nullable and optional
  - Made `phone_number` nullable and optional in recipient models
  - Response schema changes (breaking compatibility - see migration notes below)

- [Get batch calling status](/docs/api-reference/batch-calling/get)

  - Made `phone_number_id` and `phone_provider` nullable

- [Cancel batch calling](/docs/api-reference/batch-calling/cancel) & [Retry batch calling](/docs/api-reference/batch-calling/retry)
  - Made phone-related fields nullable
  - Response schema changes (breaking compatibility - see migration notes below)

#### Transfer Destinations

- Transfer-related endpoints now support dynamic variable transfer destinations:
  - Added `PhoneNumberDynamicVariableTransferDestination` type for phone number transfers using dynamic variables
  - Added `SIPUriDynamicVariableTransferDestination` type for SIP URI transfers using dynamic variables
  - Updated `PhoneNumberTransfer` discriminators to include dynamic variable types

#### MCP Servers

- [Create MCP server](/docs/api-reference/mcp/create), [Get MCP server](/docs/api-reference/mcp/get), [Update MCP server](/docs/api-reference/mcp/update)
  - Added `tool_config_overrides` field for per-tool configuration customization
  - Added `request_headers` support in `MCPServerConfigUpdateRequestModel`
  - Added `tool_call_sound` and `tool_call_sound_behavior` configuration options

#### Tools

- Tool schema enhancements:
  - `LiteralJsonSchemaProperty` now includes `is_system_provided` flag
  - Agent tool headers now support `ConvAIDynamicVariable` for dynamic header values

#### Twilio Integration

- Phone number endpoints updated:
  - Added optional `region_config` field for Twilio phone numbers
  - Added `TwilioRegionId` enum for region selection
  - Added `TwilioEdgeLocation` enum for edge location configuration

#### Agents

- [Get agent](/docs/api-reference/agents/get) & [Update agent](/docs/api-reference/agents/update)
  - Response schema changes (breaking compatibility - see migration notes below)

</Accordion>



# October 27, 2025

### Workspaces

- **External voice sharing controls**: External voice sharing and Voice Library publishing can now be disabled via workspace groups. Internal (in-organization) voice sharing is not impacted.

### Agents Platform

- **Multi-environment agent management**: The Agents CLI now supports the `--env` flag, allowing you to manage agents deployed to multiple accounts simultaneously.
- **Search functionality**: Added `search` parameter to the [Get conversations](/docs/api-reference/conversations/get-conversations) endpoint for filtering conversations.

### SDK Releases

#### JavaScript SDK

- [v2.20.1](https://github.com/elevenlabs/elevenlabs-js/releases/tag/v2.20.1) - Fixed Music API type definitions and added Realtime Scribe language code support
- [v2.20.0](https://github.com/elevenlabs/elevenlabs-js/releases/tag/v2.20.0) - Added helper methods for Realtime Scribe with improved ASR capabilities. This is a beta feature and not widely available yet

#### Python SDK

- [v2.20.1](https://github.com/elevenlabs/elevenlabs-python/releases/tag/v2.20.1) - Fixed file parameter handling in client methods
- [v2.20.0](https://github.com/elevenlabs/elevenlabs-python/releases/tag/v2.20.0) - API schema updates and improvements
- [v2.19.0](https://github.com/elevenlabs/elevenlabs-python/releases/tag/v2.19.0) - Added helper method for Scribe Realtime with improved ASR capabilities. This is a beta feature and not widely available yet

#### Agents CLI

- [@elevenlabs/agents-cli@0.6.0](https://github.com/elevenlabs/packages/releases/tag/@elevenlabs/agents-cli@0.6.0) - Added support for `--env` flag to manage agents across multiple accounts, plus bug fixes and reliability improvements

#### React Native

- [@elevenlabs/react-native@0.5.1](https://github.com/elevenlabs/packages/releases/tag/@elevenlabs/react-native@0.5.1) - Removed build script and postinstall steps for improved installation experience

#### React

- [@elevenlabs/react@0.8.1](https://github.com/elevenlabs/packages/releases/tag/@elevenlabs/react@0.8.1) - Removed build script and postinstall steps for improved installation experience

#### Client

- [@elevenlabs/client@0.8.1](https://github.com/elevenlabs/packages/releases/tag/@elevenlabs/client@0.8.1) - Removed build script and postinstall steps for improved installation experience

### API

<Accordion title="View API changes">


## Updated Endpoints

### Agents Platform

- [Get conversations](/docs/api-reference/conversations/list)

  - Added optional `search` query parameter (string) for full-text or fuzzy search over transcript messages

- [Create agent](/docs/api-reference/agents/create), [Get agent](/docs/api-reference/agents/get), [Update agent](/docs/api-reference/agents/update)

  - Added optional `tool_call_sound` field to play predefined sounds during tool execution
  - Added optional `tool_call_sound_behavior` field (default: `auto`) to control when tool call sounds play

- [Simulate conversation](/docs/api-reference/agents/simulate-conversation), [Simulate conversation stream](/docs/api-reference/agents/simulate-conversation-stream)
  - Added optional `tool_call_sound` field for tool execution audio feedback
  - Added optional `tool_call_sound_behavior` field for sound playback control

### MCP Servers

- [Update MCP server](/docs/api-reference/mcp/update)

  - Added optional `execution_mode` field to control when and how tools execute (`immediate`, `post_tool_speech`, or `async`)

- [Create MCP server](/docs/api-reference/mcp/create), [Get MCP server](/docs/api-reference/mcp/get)
  - Added `execution_mode` field (default: `immediate`) for tool execution timing control

### Server Tools

- Server tool configuration schemas now support:
  - `execution_mode` field to control tool execution timing (immediate, post-speech, or async)
  - `tool_call_sound` and `tool_call_sound_behavior` fields for audio feedback

### Supported LLM Models

- Added support for new Claude Haiku models:
  - `claude-haiku-4-5`
  - `claude-haiku-4-5@20251001`

### User Management

- [Get user info](/docs/api-reference/user/get)
  - Removed `subscription_extras` field from response

</Accordion>



# October 20, 2025

### Agents Platform

- **Genesys configuration overrides**: Genesys users can now override agent configuration directly from their Genesys flows using session variables. Use `system__override_system_prompt`, `system__override_first_message`, and `system__override_language` to customize the agent's behavior, first message, and language for specific call flows without modifying the base agent configuration.

- **Batch call ID copying**: Added copy-to-clipboard functionality for batch call IDs throughout the Agents Platform interface. Click on batch call IDs in the batch call details page or conversation history to quickly copy them for API interactions, support requests, or debugging.

### SDK Releases

#### Python SDK

- [v2.18.0](https://github.com/elevenlabs/elevenlabs-python/releases/tag/v2.18.0) - Added streaming support for Agents Platform conversations via the `Conversation` class, Music API inpainting with new output format options, and Agent Workflows support including workflow models, node types, and conditional logic operators (AND, OR, equals, greater than, less than, etc.)

#### JavaScript SDK

- [v2.19.0](https://github.com/elevenlabs/elevenlabs-js/releases/tag/v2.19.0) - Added Agent Workflows support including `AgentWorkflowRequestModel`, `AgentWorkflowResponseModel`, and AST node types for building workflow conditions (boolean nodes, dynamic variable nodes, comparison operators), Music API inpainting with new output format options, and the `archived` parameter for agent list requests

#### Agents CLI

- [@elevenlabs/agents-cli@0.6.0](https://www.npmjs.com/package/@elevenlabs/agents-cli/v/0.6.0) - Added `--env` flag to manage agents deployed to multiple accounts simultaneously
- [@elevenlabs/agents-cli@0.5.0](https://www.npmjs.com/package/@elevenlabs/agents-cli/v/0.5.0) - Reworked agents pull functionality

#### React Native

- [@elevenlabs/react-native@0.4.3](https://www.npmjs.com/package/@elevenlabs/react-native/v/0.4.3) - Fixed `onConnect` timing issue
- [@elevenlabs/react-native@0.4.2](https://www.npmjs.com/package/@elevenlabs/react-native/v/0.4.2) - Reverted change to ICE transport policy

### API

<Accordion title="View API changes">


## Updated Endpoints

### Studio

- [Create podcast](/docs/api-reference/studio/create-podcast) - Added `safety-identifier` header parameter

</Accordion>



# October 14, 2025

### Agents Platform

- **LLM overrides**: Added support for overriding an agent's LLM during a conversation, enabling you to specify a different language model on a per-conversation basis. This is useful for testing different models or accommodating specific requirements while maintaining HIPAA and data residency compliance.
- **Post-call webhook failures**: Added the option to send post-call webhook events in the event of a phone call failure. This allows you to track and respond to failed call attempts through your webhook endpoint, providing better visibility into call issues.

### SDK Releases

#### Python SDK

- [v2.18.0](https://github.com/elevenlabs/elevenlabs-python/releases/tag/v2.18.0) - Added support for streaming, Music API inpainting, and Agent Workflows

#### JavaScript SDK

- [v2.19.0](https://github.com/elevenlabs/elevenlabs-js/releases/tag/v2.19.0) - Added support for Music API inpainting and Agent Workflows
- [v2.18.0](https://github.com/elevenlabs/elevenlabs-js/releases/tag/v2.18.0) - API schema updates

#### Client Packages

- [@elevenlabs/agents-cli@0.5.0](https://github.com/elevenlabs/packages/releases/tag/@elevenlabs/agents-cli@0.5.0) - Significantly reworked agents pull command with bugfixes and improvements
- [@elevenlabs/react@0.8.0](https://github.com/elevenlabs/packages/releases/tag/@elevenlabs/react@0.8.0) - Fixed import issues
- [@elevenlabs/react-native@0.4.3](https://github.com/elevenlabs/packages/releases/tag/@elevenlabs/react-native@0.4.3) - Fixed onConnect timing
- [@elevenlabs/react-native@0.4.2](https://github.com/elevenlabs/packages/releases/tag/@elevenlabs/react-native@0.4.2) - Reverted change to ICE transport policy
- [@elevenlabs/react-native@0.4.1](https://github.com/elevenlabs/packages/releases/tag/@elevenlabs/react-native@0.4.1) - Fixed import issues



# October 7, 2025

### Agents Platform

- **Gemini 2.5 Flash Preview models**: Added support for `gemini-2.5-flash-preview-09-2025` and `gemini-2.5-flash-lite-preview-09-2025` LLM models, providing access to the latest September 2025 preview versions of Google's Gemini 2.5 Flash models.
- **Claude Sonnet 4.5**: Added support for `claude-sonnet-4-5` and `claude-sonnet-4-5@20250929` models, enabling access to the latest Claude Sonnet 4.5 model released on September 29, 2025.
- **Test invocations listing**: Added new `GET /v1/convai/test-invocations` endpoint to list all test invocations with pagination support. Includes `agent_id` filter, `page_size` parameter (default 30, max 100), and `cursor` for pagination. Response includes test run counts, pass/fail statistics, and titles.
- **Agent archiving**: Added `archived` field (boolean, default false) to agent platform settings, allowing agents to be archived without deletion while keeping them out of active agent lists.
- **MCP Server interruption control**: Added `disable_interruptions` field (boolean, default false) to MCP server configuration, preventing user interruptions during tool execution for more reliable tool completion.
- **Streaming agent responses**: Added `agent_chat_response_part` WebSocket event type for receiving partial agent chat responses in real-time during streaming conversations.
- **Workflow edge ordering**: Added `edge_order` field (array of strings) to all workflow node types, enabling explicit control over edge evaluation order for deterministic workflow execution.
- **Test suite agent tracking**: Added `agent_id` field (string, nullable) to test invocation responses for associating test runs with specific agents.

### Voice Management

- **Voice generation source tracking**: Added `VoiceGeneration` as a new source type in the History API for tracking audio generated from voice generation features.

### Telephony

- **SIP trunk TLS validation**: Added `remote_domains` field (array of strings, nullable) to SIP trunk configuration for specifying domains used in TLS certificate validation.


## SDK Releases

### JavaScript SDK

- [v2.18.0](https://github.com/elevenlabs/elevenlabs-js/releases/tag/v2.18.0) - Updated with latest API schema changes from October 8, 2025

### Python SDK

- [v2.17.0](https://github.com/elevenlabs/elevenlabs-python/releases/tag/v2.17.0) - Updated with latest API schema changes and URL generation fixes from October 6, 2025

### Packages

All packages updated with latest API schema changes:

- [@elevenlabs/react-native@0.3.2](https://github.com/elevenlabs/elevenlabs-js/releases/tag/%40elevenlabs%2Freact-native%400.3.2) - Updated TypeScript types and API client with new fields for agent archiving, MCP server configuration, and test invocations
- [@elevenlabs/react@0.7.1](https://github.com/elevenlabs/elevenlabs-js/releases/tag/%40elevenlabs%2Freact%400.7.1) - Updated React hooks and components with support for new agent settings and WebSocket events
- [@elevenlabs/client@0.7.1](https://github.com/elevenlabs/elevenlabs-js/releases/tag/%40elevenlabs%2Fclient%400.7.1) - Core client library updated with new endpoint for test invocations listing and reorganized SDK method paths for secrets management
- [@elevenlabs/agents-cli@0.4.2](https://github.com/elevenlabs/elevenlabs-js/releases/tag/%40elevenlabs%2Fagents-cli%400.4.2) - CLI tool updated with support for new agent archiving flag and test invocation commands

### MCP Server

- [v0.9.0](https://github.com/elevenlabs/elevenlabs-mcp/releases/tag/v0.9.0) - Added option to return MCP server results as resource items for better integration with resource-based workflows


## API

<Accordion title="View API changes">


## New Endpoints

### Agents Platform

- `GET /v1/convai/test-invocations` - List all test invocations with pagination support
  - **Parameters:**
    - `agent_id` (required, string) - Filter by agent ID
    - `page_size` (optional, integer, default=30, max=100) - Number of results per page
    - `cursor` (optional, string) - Pagination cursor from previous response
  - **Response:** Returns paginated list with test run counts, pass/fail statistics, titles, and next cursor


## New Fields

### Agents Platform

- **Agent Settings**: Added `archived` field (boolean, default false) to `AgentPlatformSettingsRequestModel` and `AgentPlatformSettingsResponseModel` for archiving agents
- **MCP Servers**: Added `disable_interruptions` field (boolean, default false) to MCP server configuration schemas for preventing user interruptions during tool execution
- **Workflows**: Added `edge_order` field (array of strings) to all workflow node types for explicit edge evaluation ordering
- **Test Invocations**: Added `agent_id` field (string, nullable) to `GetTestSuiteInvocationResponseModel` for agent tracking

### Telephony

- **SIP Trunks**: Added `remote_domains` field (array of strings, nullable) to `GetPhoneNumberInboundSIPTrunkConfigResponseModel` and `InboundSIPTrunkConfigRequestModel` for TLS certificate validation

### WebSocket Events

- Added `agent_chat_response_part` to `ServerEventType` enum for streaming partial agent chat responses

### Voice Management

- Added `VoiceGeneration` to speech history source types


## New LLM Models

Added the following models to the LLM enum:

- `claude-sonnet-4-5` - Claude Sonnet 4.5 latest
- `claude-sonnet-4-5@20250929` - Claude Sonnet 4.5 dated release (September 29, 2025)
- `gemini-2.5-flash-preview-09-2025` - Gemini 2.5 Flash preview (September 2025)
- `gemini-2.5-flash-lite-preview-09-2025` - Gemini 2.5 Flash Lite preview (September 2025)


## Other Changes

### Pronunciation Dictionaries

- Updated parameter description for `version_id` in `GET /v1/pronunciation-dictionaries/{dictionary_id}/{version_id}/download` from "The id of the version of the pronunciation dictionary" to "The id of the pronunciation dictionary version"
- Removed documentation note about UI limitation for multiple pronunciation dictionaries (multiple dictionaries now fully supported in UI)

### Conversation History

- Made `type` field optional in `ConversationHistoryTranscriptOtherToolsResultCommonModel` (previously required)

</Accordion>



# September 29, 2025

### v1 TTS model deprecation

The `eleven_monolingual_v1` and `eleven_multilingual_v1` models are deprecated and will be removed on December 15th, 2025. Please [migrate to newer models](https://elevenlabs.io/docs/models#deprecated-models) for continued service.

### Agents Platform

- **Workflow Expressions**: Workflows now support complex expressions that allow for defining deterministic conditions using logical operators, dynamic variables and LLM evaluation. This enables more sophisticated agent logic and decision-making capabilities.
- **MCP Server Interrupt Control**: Added option to disable interruptions during all tool calls for MCP Servers, providing better control over agent behavior during tool execution.
- **Audio Alignment Data**: Agents now have a flag to enable alignment data in audio events, useful for audio-text synchronization use cases such as lip sync applications.
- **Ignore Default Personality Setting**: The Agents Platform configuration page now includes a checkbox to toggle whether agents should ignore the default helpful personality, giving developers more control over agent behavior.

### Speech to Text

- **Fixed Base64 Encoding Flag**: Resolved an issue where the `is_base64_encoded` flag in STT responses was incorrectly set to false for PDF and DOCX formats, even when content was actually base64 encoded.

### SDK Releases

#### JavaScript SDK

- **v2.16.0**: Updated with latest API schema changes from September 19, 2025.

#### Packages

- **@elevenlabs/types@0.0.1**: New public TypeScript types package providing shared type definitions across ElevenLabs integrations.
- **@elevenlabs/react@0.7.0** and **@elevenlabs/client@0.7.0**: Added support for passing custom script paths to avoid blob: and data: URLs for improved security and flexibility.
- **@elevenlabs/convai-widget-embed@0.3.0** and **@elevenlabs/convai-widget-core@0.3.0**: Added `use_rtc` attribute for widget functionality and added expand event support for better widget interaction handling.

### API

<Accordion title="View API changes">


## Updated Endpoints

### Agents Platform

- **POST /v1/convai/agents/create**: Added `ignore_default_personality` boolean parameter to control whether agents should ignore the default helpful personality behavior
- **PATCH /v1/convai/agents/{agent_id}**: Added `ignore_default_personality` field support for agent updates
- **GET /v1/convai/agents/{agent_id}**: Response now includes `ignore_default_personality` field in agent configuration
- **POST /v1/convai/mcp-servers**: Added interrupt control configuration parameters for disabling interruptions during tool calls
- **PATCH /v1/convai/mcp-servers/{mcp_server_id}**: Enhanced with interrupt control settings for MCP server configuration
- **GET /v1/convai/mcp-servers/{mcp_server_id}**: Response includes new interrupt control configuration fields
- **GET /v1/convai/conversations/{conversation_id}**: Response enhanced with alignment data fields for audio-text synchronization support
- **POST /v1/convai/agent-testing/create**: Enhanced to support workflow expressions functionality in agent testing
- **GET /v1/convai/agent-testing/{test_id}**: Response includes additional fields for workflow expression test results
- **PUT /v1/convai/agent-testing/{test_id}**: Request and response schemas updated for workflow expression support
- **POST /v1/convai/agents/{agent_id}/simulate-conversation**: Request schema updated to support workflow expressions in conversation simulation
- **POST /v1/convai/agents/{agent_id}/simulate-conversation/stream**: Streaming conversation simulation with workflow expression support
- **GET /v1/convai/settings**: Response includes new platform configuration options
- **PATCH /v1/convai/settings**: Request schema updated with new platform settings
- **POST /v1/convai/batch-calling/submit**: Request schema updates for batch calling functionality
- **PATCH /v1/convai/mcp-servers/{mcp_server_id}/approval-policy**: Response schema updated for approval policy management
- **POST /v1/convai/mcp-servers/{mcp_server_id}/tool-approvals**: Response schema enhanced for tool approval handling
- **DELETE /v1/convai/mcp-servers/{mcp_server_id}/tool-approvals/{tool_name}**: Response schema updated for tool approval removal

### Speech to Text

- **POST /v1/speech-to-text**: Fixed `is_base64_encoded` boolean flag to correctly return `true` when PDF and DOCX document content is base64 encoded

### Text to Speech

- **POST /v1/text-to-speech/{voice_id}/with-timestamps**: Request and response schemas updated for enhanced timestamp functionality
- **POST /v1/text-to-speech/{voice_id}/stream**: Request schema updated for improved streaming parameters
- **POST /v1/text-to-speech/{voice_id}/stream/with-timestamps**: Request and response schemas updated for streaming with timestamps
- **POST /v1/text-to-voice/create-previews**: Request schema enhanced with new preview generation options
- **POST /v1/text-to-voice**: Response schema updated with additional voice creation data
- **POST /v1/text-to-voice/{voice_id}/remix**: Request schema enhanced for voice remixing parameters

### Voice Management

- **GET /v1/voices**: Response schema updated with new voice metadata fields
- **GET /v1/voices/{voice_id}**: Response schema enhanced with additional voice properties
- **GET /v1/voices/settings/default**: Response schema updated for default voice settings
- **GET /v1/voices/{voice_id}/settings**: Response schema enhanced with new configuration options
- **POST /v1/voices/{voice_id}/settings/edit**: Request schema updated for voice settings modification
- **POST /v1/voices/pvc/{voice_id}/samples/{sample_id}**: Request schema enhanced for PVC sample management
- **GET /v1/voices/pvc/{voice_id}/samples/{sample_id}/audio**: Response schema updated for audio sample retrieval
- **GET /v1/voices/pvc/{voice_id}/samples/{sample_id}/speakers/{speaker_id}/audio**: Response schema enhanced for speaker-specific audio
- **POST /v1/voice-generation/create-voice**: Response schema updated with new voice generation data

### Studio

- **POST /v1/studio/podcasts**: Request schema enhanced with new podcast creation parameters

### User Management

- **GET /v1/user**: Response schema updated with additional user profile data

All changes are backward compatible and do not require immediate action from developers.

</Accordion>



# September 22, 2025

### Productions launch

Introducing Productions - our new managed service offering for ordering human-edited content that looks, sounds and feels natural. Made for creators and media businesses.

Our network of linguists and audio professionals offer end-to-end production quality for:

- Dubbing
- Captions and subtitles
- Transcription
- Audiobooks

You can order a project directly from the 'Productions' page in your ElevenLabs account, or by emailing productions@elevenlabs.io. Pricing starts at $2/minute, contact us for more details.

### Agents Platform

- **MCP pre-tool speech**: Added support for configuring tools extracted from an MCP Server to require pre-tool execution speech. This enhancement allows agents to provide verbal context before executing specific tools, improving the conversational flow during tool usage.

- **ElevenLabs hosted LLMs**: Added support for [ElevenLabs hosted LLMs](/docs/agents-platform/customization/llm#elevenlabs-experimental) which unlock lower latency by running on ElevenLabs infrastructure alongside Speech to Text and Text to Speech services.

- **Enum values for tool parameters**: Added support for specifying a tool's parameters as [enum values](/docs/api-reference/tools/create#response.body.tool_config.WebhookToolConfig.api_schema.request_body_schema.properties.LiteralJsonSchemaProperty.enum) for greater control

### SDK Releases

#### JavaScript SDK

- **v2.16.0**: Updated the [elevenlabs-js](https://github.com/elevenlabs/elevenlabs-js) SDK with the latest API schema changes, including new MCP server endpoints and enhanced history filtering capabilities.

#### Python SDK

- **v2.16.0**: Updated the [elevenlabs-python](https://github.com/elevenlabs/elevenlabs-python) SDK with the latest API schema changes, including new MCP server endpoints and enhanced history filtering capabilities.
- **v2.15.1**: Fixed conversation handling when no authentication is required and added asyncio event loop support for better async operations.

#### Package Updates

- **@elevenlabs/agents-cli@0.3.2**: Updated the Agents CLI package with improvements to agent development tools. The ConvAI CLI has been renamed to Agents CLI to align with the ElevenLabs Agents Platform branding.
- **@elevenlabs/convai-cli@0.2.3**: Final release of the legacy ConvAI CLI package before migration to the new Agents CLI.
- **@elevenlabs/react@0.6.3**: Updated the React components package with enhanced functionality.

### API

<Accordion title="View API changes">


## New Endpoints

- `PATCH /v1/convai/mcp-servers/{mcp_server_id}` - [Update MCP Server Configuration](/docs/api-reference/mcp/update): Added new endpoint to update MCP server configurations, replacing the deprecated approval policy endpoint.


## Updated Endpoints

### History Management

- `GET /v1/history` - [Get generated items](/docs/api-reference/history/list): Enhanced with additional filtering parameters:
  - Added `model_id` parameter for filtering by specific models
  - Added `date_before_unix` parameter for filtering items before a specific date
  - Added `date_after_unix` parameter for filtering items after a specific date
  - Added `sort_direction` parameter for controlling sort order


## Deprecated Endpoints

- `PATCH /v1/convai/mcp-servers/{mcp_server_id}/approval-policy` - Deprecated in favor of the new general MCP server update endpoint

</Accordion>



# September 15, 2025

### Text to Speech

- **WebSocket output format**: Added support for specifying output format in the first message of a WebSocket connection, providing greater flexibility for real-time audio streaming workflows.

### Agents Platform

- **First message interruption control**: Added `disable_first_message_interruptions` setting to prevent agents from being interrupted during important opening messages like legal disclaimers.

### MCP Server

- **Version 0.8.1**: Added data residency support.


## SDK Releases

### JavaScript SDK

- **v2.15.0** - Added new Text to Voice Remix endpoint

### Python SDK

- **v2.15.1** - Fixed conversation authentication issue and added asyncio event loop support
- **v2.15.0** - Added new Text to Voice Remix endpoint and fixed Pydantic issues

### Packages

- **@elevenlabs/react@0.6.2** - Added correction and MCP tool call events
- **@elevenlabs/client@0.6.2** - Added correction and MCP tool call events
- **@elevenlabs/react-native@0.3.1** - Added correction and MCP tool call events


## API

<Accordion title="View API changes">


## New Endpoints

- `DELETE /v1/speech-to-text/transcripts/{transcription_id}` - [Delete Transcript By Id](/docs/api-reference/speech-to-text/delete)


## Updated Endpoints

### Backward Compatible Changes

- [Get dubbing](/docs/api-reference/dubbing/get) - Added the optional `order_by` and `order_direction` parameters.
- [List Agents](/docs/api-reference/agents/list) - Added the optional `sort_by` and `sort_direction` parameters.
- [List knowledge base documents](/docs/api-reference/knowledge-base/list) - Added the optional `sort_by` and `sort_direction` parameters.

</Accordion>



# September 8, 2025

### Text to Speech

- **Language code support**: All Text to Speech models now support language codes for improved output. Normalization has been enabled for Eleven v3, Flash, and Turbo models to enhance audio quality and consistency.

### Agents Platform

- **Multi-voice agent history**: Messages from multi-voice agents are now displayed in conversation history with clear separation by voice, making it easier to follow which voice spoke which part of a conversation.

### SDK Releases

#### JavaScript SDK

- **v2.15.0** - Adds support for new voice remix functionality

#### Python SDK

- **v2.15.0** - Adds support for new voice remix functionality. Also fixed an issue with Pydantic.

#### React Components

- **@elevenlabs/react@0.6.1** - Fix output bytes and device input/output switching
- **@elevenlabs/client@0.6.1** - Fix output bytes and device input/output switching

### MCP Server

- **v0.7.0** - Latest release of the [ElevenLabs MCP Server](https://github.com/elevenlabs/elevenlabs-mcp) with new features and improvements for Claude Desktop integration. Includes new `loop` parameter for SFX generation.

### API

<Accordion title="View API changes">


## New Endpoints

- [Remix a voice](/docs/api-reference/text-to-voice/remix) - Create voice variations from existing voices
- [Get Transcript By Id](/docs/api-reference/speech-to-text/get) - Retrieve specific transcription results


## Updated Endpoints

### Backward Compatible Changes

- [Get Project](/docs/api-reference/studio/get-project) - Added optional `share_id` query parameter for project sharing functionality
- [Convert Speech to Text](/docs/api-reference/speech-to-text/convert) - Modified `enable_logging` parameter for improved logging control

All API changes in this release are backward compatible and will not break existing integrations.

</Accordion>



# September 1, 2025

### Agents Platform

- **Gemini 2.5 Flash Lite HIPAA compliance**: Added Gemini 2.5 Flash Lite to the list of [HIPAA approved models](/docs/agents-platform/legal/hipaa) for compliant conversations when a BAA is signed and zero-retention mode is enabled.
- **Conversation ID in signed URLs**: Added support for including conversation IDs in signed URL requests, providing better tracking and identification capabilities for conversation audio access.


## SDK Releases

### JavaScript SDK

- **[v2.13.0](https://github.com/elevenlabs/elevenlabs-js)** - Released August 29, 2025. Adds support for new `loop` parameter in SFX.

### Python SDK

- **[v2.13.0](https://github.com/elevenlabs/elevenlabs-python)** - Released August 29, 2025. Adds support for new `loop` parameter in SFX.

### ConvAI packages

- **[@elevenlabs/react v0.6.0 and @elevenlabs/client v0.6.0](https://github.com/elevenlabs/packages)** - Released August 29, 2025. Fixed setVolume functionality, added client tool debugging, and added audio device controls.

### MCP Server

- **[ElevenLabs MCP Server v0.6.0](https://github.com/elevenlabs/elevenlabs-mcp)** - Released August 26, 2025. Fixed diarization functionality in speech-to-text and added music generation endpoints.


## API

<Accordion title="View API changes">


## Updated Endpoints

### Dubbing

- **[Render project](/docs/api-reference/dubbing/resources/render-project)** - Added optional `should_normalize_volume` query parameter to control audio normalization during rendering

### Agents Platform

- **[Get signed URL](/docs/api-reference/conversations/get-signed-url)** - Added optional `include_conversation_id` query parameter to include conversation ID in the response

### Sound Effects

- **[Create sound effect](/docs/api-reference/text-to-sound-effects/convert)** - Added optional `loop` parameter to create sound effects that loop smoothly


## Removed Endpoints

- **Delete workspace member** - Removed the `DELETE /v1/workspace/members` endpoint for deleting workspace members. This endpoint was never meant to be publicly available.

</Accordion>



# August 25, 2025

### Agents Platform

- **Agent testing framework**: Introduced a comprehensive testing framework for ElevenLabs agents, allowing developers to create, manage, and execute automated tests for their agents. This includes test creation, execution tracking, and result analysis capabilities.
- **Test invocation management**: Added support for resubmitting failed test invocations and viewing detailed test results to help developers debug and improve their agents.
- **Enhanced agent configuration**: Improved agent creation and management with additional workspace override capabilities and refined platform settings.

### Text to Speech

- **Pronunciation dictionary updates**: Added support for updating pronunciation dictionaries with PATCH operations, enabling more flexible dictionary management.
- **Enhanced timestamp support**: Improved timestamp generation for text-to-speech conversions with better alignment data and streaming capabilities.

### SDK Releases

- **TypeScript SDK v2.12.2**: Updated with the latest API schema changes, including full support for the new agent testing endpoints and enhanced Agents Platform capabilities.
- **Python SDK v2.12.1**: Released with complete support for all new API features, including agent testing framework and improved workspace resource management.

### API

<Accordion title="View API changes">


## New Endpoints

Added 10 new endpoints this week:

### ElevenLabs agent Testing

- `POST /v1/convai/agent-testing/create` - [Create Agent Response Test](/docs/api-reference/tests/create) - Create automated tests for your ElevenLabs agents
- `GET /v1/convai/agent-testing/{test_id}` - [Get Agent Response Test By Id](/docs/api-reference/tests/get) - Retrieve specific test configurations and results
- `PUT /v1/convai/agent-testing/{test_id}` - [Update Agent Response Test](/docs/api-reference/tests/update) - Modify existing test setups and parameters
- `DELETE /v1/convai/agent-testing/{test_id}` - [Delete Agent Response Test](/docs/api-reference/tests/delete) - Remove test configurations from your workspace
- `POST /v1/convai/agent-testing/summaries` - [Get Agent Response Test Summaries By Ids](/docs/api-reference/tests/summaries) - Retrieve aggregated test results for multiple tests
- `GET /v1/convai/agent-testing` - [List Agent Response Tests](/docs/api-reference/tests/list) - Browse all available tests in your workspace
- `POST /v1/convai/agents/{agent_id}/run-tests` - [Run Tests On The Agent](/docs/api-reference/tests/run-tests) - Execute test suites against specific agents
- `GET /v1/convai/test-invocations/{test_invocation_id}` - [Get Test Invocation](/docs/api-reference/tests/test-invocations/get) - Retrieve detailed test execution results
- `POST /v1/convai/test-invocations/{test_invocation_id}/resubmit` - [Resubmit Tests](/docs/api-reference/tests/test-invocations/resubmit) - Re-run failed test invocations

### Pronunciation Dictionaries

- `PATCH /v1/pronunciation-dictionaries/{pronunciation_dictionary_id}` - [Update Pronunciation Dictionary](/docs/api-reference/pronunciation-dictionaries/update) - Update existing pronunciation dictionaries with new rules or modifications

</Accordion>



# August 20, 2025

### Eleven v3 API

Eleven v3 is now available via the API.

To start using it, simply specify the model ID `eleven_v3` when making [Text to Speech requests](/docs/api-reference/text-to-speech/convert).

Additionally the [Text to Dialogue](/docs/cookbooks/text-to-dialogue) API endpoint is now available to all.

### Music Generation API

The Eleven Music API is now freely available to all paid users.

Visit the [quickstart](/docs/cookbooks/music/quickstart) to lean how to integrate. The API section below highlights the new endpoints that have been released.

### Global TTS API preview

ElevenLabs is launching inference servers in additional geographical regions to reduce latency for clients outside of the US. Initial request processing will be available in the Netherlands and in Singapore in addition to the US.

To learn how to get started [head to the docs](/docs/best-practices/latency-optimization#global-tts-api-preview).

### API

<Accordion title="View API changes">


## New Endpoints

- Added 4 new endpoints:
  - [Compose music](/docs/api-reference/music/compose) - Create music from text prompts
  - [Create composition plan](/docs/api-reference/music/create-composition-plan) - Optimize music generation parameters before processing
  - [Compose music with details](/docs/api-reference/music/compose-detailed) - Advanced music generation with detailed parameters
  - [Stream music](/docs/api-reference/music/stream) - Real-time streaming music generation


## Updated Endpoints

### Text to Speech

- Updated Text to Speech endpoints with improved parameter handling:
  - [Convert text to speech](/docs/api-reference/text-to-speech/convert) - Enhanced voice settings and text input parameter handling
  - [Stream text to speech](/docs/api-reference/text-to-speech/convert-as-stream) - Improved streaming parameter management
  - [Convert with timestamps](/docs/api-reference/text-to-speech/convert-with-timestamps) - Better alignment parameter handling

### Voice Management

- Updated Voice endpoints with enhanced parameter support:
  - [Create voice previews](/docs/api-reference/legacy/voices/create-previews) - Improved preview generation parameters
  - [Create voice from preview](/docs/api-reference/text-to-voice/create) - Enhanced voice creation options
  - [Get voice](/docs/api-reference/voices/get) - Updated voice parameter responses
  - [List voices](/docs/api-reference/voices/search) - Improved voice listing parameters

### Speech to Text

- Updated Speech to Text endpoint:
  - [Convert speech to text](/docs/api-reference/speech-to-text/convert) - Enhanced transcription parameter handling

### Usage and Analytics

- Updated Usage endpoints:
  - [Get character stats](/docs/api-reference/usage/get) - Added aggregation bucket size parameter and improved breakdown type options

### Workspace Management

- Updated Workspace endpoints:
  - [Get workspace resource](/docs/api-reference/workspace/get-resource) - Enhanced resource type parameter handling
  - [Share workspace resource](/docs/api-reference/workspace/share-workspace-resource) - Updated sharing parameter structure
  - [Unshare workspace resource](/docs/api-reference/workspace/unshare-workspace-resource) - Updated unsharing parameter structure

</Accordion>



---
**Navigation:** ← Previous | [Index](./index.md) | [Next →](./02-august-11-2025.md)
