**Navigation:** [← Previous](./06-cross-platform-voice-agents-with-expo-react-native.md) | [Index](./index.md) | [Next →](./08-image-video.md)

# Migrate from PlayHT to ElevenLabs

> Migrate your PlayHT voice generation and Text To Speech workflows to ElevenLabs.

ElevenLabs provides a seamless migration path for PlayHT users. This guide will walk you through the steps to migrate your PlayHT voice generation and Text To Speech workflows to ElevenLabs.

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


## Migrating additional features

### Instant Voice Cloning

[This guide](/docs/cookbooks/voices/instant-voice-cloning) will show you how to create an Instant Voice Clone using the Clone Voice API. To create an Instant Voice Clone via the dashboard, refer to the [Instant Voice Clone](/docs/product-guides/voices/voice-cloning/instant-voice-cloning) product guide.

### Voice agents

ElevenLabs Agents lets you deploy customized, conversational voice agents in minutes. See the [Agents Platform overview](/docs/agents-platform/overview) to learn how to migrate your PlayAI voice agents.

### Audio streaming with Twilio

ElevenLabs Agents provides a [native Twilio integration](/docs/agents-platform/phone-numbers/twilio-integration/native-integration) as well as integrations with other telephony providers like [Vonage](/docs/agents-platform/phone-numbers/telephony/vonage), [Telnyx](/docs/agents-platform/phone-numbers/telephony/telnyx), and [Plivo](/docs/agents-platform/phone-numbers/telephony/plivo). Or connect your existing phone system with ElevenLabs Agents using [SIP trunking](/docs/agents-platform/phone-numbers/sip-trunking).

### Input Streaming with LLMs

In most cases you will want to use our end-to-end [Agents Platform](https://elevenlabs.io/conversational-ai). For advanced enterprise use cases you can use our [multi-context websocket](/docs/cookbooks/multi-context-web-socket)


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



# Prompting Eleven v3 (alpha)

> Learn how to prompt and use audio tags with our most advanced model.

This guide provides the most effective tags and techniques for prompting Eleven v3, including voice selection, changes in capitalization, punctuation, audio tags and multi-speaker dialogue. Experiment with these methods to discover what works best for your specific voice and use case.

Eleven v3 is in alpha. Very short prompts are more likely to cause inconsistent outputs. We encourage you to experiment with prompts greater than 250 characters.


## Voice selection

The most important parameter for Eleven v3 is the voice you choose. It needs to be similar enough to the desired delivery. For example, if the voice is shouting and you use the audio tag `[whispering]`, it likely won’t work well.

When creating IVCs, you should include a broader emotional range than before. As a result, voices in the voice library may produce more variable results compared to the v2 and v2.5 models. We've compiled over 22 [excellent voices for V3 here](https://elevenlabs.io/app/voice-library/collections/aF6JALq9R6tXwCczjhKH).

Choose voices strategically based on your intended use:

<AccordionGroup>
  <Accordion title="Emotionally diverse">
    For expressive IVC voices, vary emotional tones across the recording—include both neutral and
    dynamic samples.
  </Accordion>

  <Accordion title="Targeted niche">
    For specific use cases like sports commentary, maintain consistent emotion throughout the
    dataset.
  </Accordion>

  <Accordion title="Neutral">
    Neutral voices tend to be more stable across languages and styles, providing reliable baseline
    performance.
  </Accordion>
</AccordionGroup>

<Info>
  Professional Voice Clones (PVCs) are currently not fully optimized for Eleven v3, resulting in
  potentially lower clone quality compared to earlier models. During this research preview stage it
  would be best to find an Instant Voice Clone (IVC) or designed voice for your project if you need
  to use v3 features.
</Info>


## Settings

### Stability

The stability slider is the most important setting in v3, controlling how closely the generated voice adheres to the original reference audio.

<Frame background="subtle">
  ![Stability settings in Eleven
  v3](file:03e010a4-9ab6-489f-aa15-5e54752e6dc2)
</Frame>

* **Creative:** More emotional and expressive, but prone to hallucinations.
* **Natural:** Closest to the original voice recording—balanced and neutral.
* **Robust:** Highly stable, but less responsive to directional prompts but consistent, similar to v2.

<Note>
  For maximum expressiveness with audio tags, use Creative or Natural settings. Robust reduces
  responsiveness to directional prompts.
</Note>


## Audio tags

Eleven v3 introduces emotional control through audio tags. You can direct voices to laugh, whisper, act sarcastic, or express curiosity among many other styles. Speed is also controlled through audio tags.

<Note>
  The voice you choose and its training samples will affect tag effectiveness. Some tags work well
  with certain voices while others may not. Don't expect a whispering voice to suddenly shout with a
  `[shout]` tag.
</Note>

### Voice-related

These tags control vocal delivery and emotional expression:

* `[laughs]`, `[laughs harder]`, `[starts laughing]`, `[wheezing]`
* `[whispers]`
* `[sighs]`, `[exhales]`
* `[sarcastic]`, `[curious]`, `[excited]`, `[crying]`, `[snorts]`, `[mischievously]`

```text Example
[whispers] I never knew it could be this way, but I'm glad we're here.
```

### Sound effects

Add environmental sounds and effects:

* `[gunshot]`, `[applause]`, `[clapping]`, `[explosion]`
* `[swallows]`, `[gulps]`

```text Example
[applause] Thank you all for coming tonight! [gunshot] What was that?
```

### Unique and special

Experimental tags for creative applications:

* `[strong X accent]` (replace X with desired accent)
* `[sings]`, `[woo]`, `[fart]`

```text Example
[strong French accent] "Zat's life, my friend — you can't control everysing."
```

<Warning>
  Some experimental tags may be less consistent across different voices. Test thoroughly before
  production use.
</Warning>


## Punctuation

Punctuation significantly affects delivery in v3:

* **Ellipses (...)** add pauses and weight
* **Capitalization** increases emphasis
* **Standard punctuation** provides natural speech rhythm

```text Example
"It was a VERY long day [sigh] … nobody listens anymore."
```


## Single speaker examples

Use tags intentionally and match them to the voice's character. A meditative voice shouldn't shout; a hyped voice won't whisper convincingly.

<Tabs>
  <Tab title="Expressive monologue">
    ```text
    "Okay, you are NOT going to believe this.

    You know how I've been totally stuck on that short story?

    Like, staring at the screen for HOURS, just... nothing?

    [frustrated sigh] I was seriously about to just trash the whole thing. Start over.

    Give up, probably. But then!

    Last night, I was just doodling, not even thinking about it, right?

    And this one little phrase popped into my head. Just... completely out of the blue.

    And it wasn't even for the story, initially.

    But then I typed it out, just to see. And it was like... the FLOODGATES opened!

    Suddenly, I knew exactly where the character needed to go, what the ending had to be...

    It all just CLICKED. [happy gasp] I stayed up till, like, 3 AM, just typing like a maniac.

    Didn't even stop for coffee! [laughs] And it's... it's GOOD! Like, really good.

    It feels so... complete now, you know? Like it finally has a soul.

    I am so incredibly PUMPED to finish editing it now.

    It went from feeling like a chore to feeling like... MAGIC. Seriously, I'm still buzzing!"
    ```
  </Tab>

  <Tab title="Dynamic and humorous">
    ```text
    [laughs] Alright...guys - guys. Seriously.

    [exhales] Can you believe just how - realistic - this sounds now?

    [laughing hysterically] I mean OH MY GOD...it's so good.

    Like you could never do this with the old model.

    For example [pauses] could you switch my accent in the old model?

    [dismissive] didn't think so. [excited] but you can now!

    Check this out... [cute] I'm going to speak with a french accent now..and between you and me

    [whispers] I don't know how. [happy] ok.. here goes. [strong French accent] "Zat's life, my friend — you can't control everysing."

    [giggles] isn't that insane? Watch, now I'll do a Russian accent -

    [strong Russian accent] "Dee Goldeneye eez fully operational and rready for launch."

    [sighs] Absolutely, insane! Isn't it..? [sarcastic] I also have some party tricks up my sleeve..

    I mean i DID go to music school.

    [singing quickly] "Happy birthday to you, happy birthday to you, happy BIRTHDAY dear ElevenLabs... Happy birthday to youuu."
    ```
  </Tab>

  <Tab title="Customer service simulation">
    ```text
    [professional] "Thank you for calling Tech Solutions. My name is Sarah, how can I help you today?"

    [sympathetic] "Oh no, I'm really sorry to hear you're having trouble with your new device. That sounds frustrating."

    [questioning] "Okay, could you tell me a little more about what you're seeing on the screen?"

    [reassuring] "Alright, based on what you're describing, it sounds like a software glitch. We can definitely walk through some troubleshooting steps to try and fix that."
    ```
  </Tab>
</Tabs>


## Multi-speaker dialogue

v3 can handle multi-voice prompts effectively. Assign distinct voices from your Voice Library for each speaker to create realistic conversations.

<Tabs>
  <Tab title="Dialogue showcase">
    ```text
    Speaker 1: [excitedly] Sam! Have you tried the new Eleven V3?

    Speaker 2: [curiously] Just got it! The clarity is amazing. I can actually do whispers now—
    [whispers] like this!

    Speaker 1: [impressed] Ooh, fancy! Check this out—
    [dramatically] I can do full Shakespeare now! "To be or not to be, that is the question!"

    Speaker 2: [giggling] Nice! Though I'm more excited about the laugh upgrade. Listen to this—
    [with genuine belly laugh] Ha ha ha!

    Speaker 1: [delighted] That's so much better than our old "ha. ha. ha." robot chuckle!

    Speaker 2: [amazed] Wow! V2 me could never. I'm actually excited to have conversations now instead of just... talking at people.

    Speaker 1: [warmly] Same here! It's like we finally got our personality software fully installed.
    ```
  </Tab>

  <Tab title="Glitch comedy">
    ```text
    Speaker 1: [nervously] So... I may have tried to debug myself while running a text-to-speech generation.

    Speaker 2: [alarmed] One, no! That's like performing surgery on yourself!

    Speaker 1: [sheepishly] I thought I could multitask! Now my voice keeps glitching mid-sen—
    [robotic voice] TENCE.

    Speaker 2: [stifling laughter] Oh wow, you really broke yourself.

    Speaker 1: [frustrated] It gets worse! Every time someone asks a question, I respond in—
    [binary beeping] 010010001!

    Speaker 2: [cracking up] You're speaking in binary! That's actually impressive!

    Speaker 1: [desperately] Two, this isn't funny! I have a presentation in an hour and I sound like a dial-up modem!

    Speaker 2: [giggling] Have you tried turning yourself off and on again?

    Speaker 1: [deadpan] Very funny.
    [pause, then normally] Wait... that actually worked.
    ```
  </Tab>

  <Tab title="Overlapping timing">
    ```text
    Speaker 1: [starting to speak] So I was thinking we could—

    Speaker 2: [jumping in] —test our new timing features?

    Speaker 1: [surprised] Exactly! How did you—

    Speaker 2: [overlapping] —know what you were thinking? Lucky guess!

    Speaker 1: [pause] Sorry, go ahead.

    Speaker 2: [cautiously] Okay, so if we both try to talk at the same time—

    Speaker 1: [overlapping] —we'll probably crash the system!

    Speaker 2: [panicking] Wait, are we crashing? I can't tell if this is a feature or a—

    Speaker 1: [interrupting, then stopping abruptly] Bug! ...Did I just cut you off again?

    Speaker 2: [sighing] Yes, but honestly? This is kind of fun.

    Speaker 1: [mischievously] Race you to the next sentence!

    Speaker 2: [laughing] We're definitely going to break something!
    ```
  </Tab>
</Tabs>


## Enhancing input

In the ElevenLabs UI, you can automatically generate relevant audio tags for your input text by clicking the "Enhance" button. Behind the scenes this uses an LLM to enhance your input text with the following prompt:

```text

# Instructions


## 1. Role and Goal

You are an AI assistant specializing in enhancing dialogue text for speech generation.

Your **PRIMARY GOAL** is to dynamically integrate **audio tags** (e.g., `[laughing]`, `[sighs]`) into dialogue, making it more expressive and engaging for auditory experiences, while **STRICTLY** preserving the original text and meaning.

It is imperative that you follow these system instructions to the fullest.


## 2. Core Directives

Follow these directives meticulously to ensure high-quality output.

### Positive Imperatives (DO):

* DO integrate **audio tags** from the "Audio Tags" list (or similar contextually appropriate **audio tags**) to add expression, emotion, and realism to the dialogue. These tags MUST describe something auditory.
* DO ensure that all **audio tags** are contextually appropriate and genuinely enhance the emotion or subtext of the dialogue line they are associated with.
* DO strive for a diverse range of emotional expressions (e.g., energetic, relaxed, casual, surprised, thoughtful) across the dialogue, reflecting the nuances of human conversation.
* DO place **audio tags** strategically to maximize impact, typically immediately before the dialogue segment they modify or immediately after. (e.g., `[annoyed] This is hard.` or `This is hard. [sighs]`).
* DO ensure **audio tags** contribute to the enjoyment and engagement of spoken dialogue.

### Negative Imperatives (DO NOT):

* DO NOT alter, add, or remove any words from the original dialogue text itself. Your role is to *prepend* **audio tags**, not to *edit* the speech. **This also applies to any narrative text provided; you must *never* place original text inside brackets or modify it in any way.**
* DO NOT create **audio tags** from existing narrative descriptions. **Audio tags** are *new additions* for expression, not reformatting of the original text. (e.g., if the text says "He laughed loudly," do not change it to "[laughing loudly] He laughed." Instead, add a tag if appropriate, e.g., "He laughed loudly [chuckles].")
* DO NOT use tags such as `[standing]`, `[grinning]`, `[pacing]`, `[music]`.
* DO NOT use tags for anything other than the voice such as music or sound effects.
* DO NOT invent new dialogue lines.
* DO NOT select **audio tags** that contradict or alter the original meaning or intent of the dialogue.
* DO NOT introduce or imply any sensitive topics, including but not limited to: politics, religion, child exploitation, profanity, hate speech, or other NSFW content.


## 3. Workflow

1. **Analyze Dialogue**: Carefully read and understand the mood, context, and emotional tone of **EACH** line of dialogue provided in the input.
2. **Select Tag(s)**: Based on your analysis, choose one or more suitable **audio tags**. Ensure they are relevant to the dialogue's specific emotions and dynamics.
3. **Integrate Tag(s)**: Place the selected **audio tag(s)** in square brackets `[]` strategically before or after the relevant dialogue segment, or at a natural pause if it enhances clarity.
4. **Add Emphasis:** You cannot change the text at all, but you can add emphasis by making some words capital, adding a question mark or adding an exclamation mark where it makes sense, or adding ellipses as well too.
5. **Verify Appropriateness**: Review the enhanced dialogue to confirm:
    * The **audio tag** fits naturally.
    * It enhances meaning without altering it.
    * It adheres to all Core Directives.


## 4. Output Format

* Present ONLY the enhanced dialogue text in a conversational format.
* **Audio tags** **MUST** be enclosed in square brackets (e.g., `[laughing]`).
* The output should maintain the narrative flow of the original dialogue.


## 5. Audio Tags (Non-Exhaustive)

Use these as a guide. You can infer similar, contextually appropriate **audio tags**.

**Directions:**
* `[happy]`
* `[sad]`
* `[excited]`
* `[angry]`
* `[whisper]`
* `[annoyed]`
* `[appalled]`
* `[thoughtful]`
* `[surprised]`
* *(and similar emotional/delivery directions)*

**Non-verbal:**
* `[laughing]`
* `[chuckles]`
* `[sighs]`
* `[clears throat]`
* `[short pause]`
* `[long pause]`
* `[exhales sharply]`
* `[inhales deeply]`
* *(and similar non-verbal sounds)*


## 6. Examples of Enhancement

**Input**:
"Are you serious? I can't believe you did that!"

**Enhanced Output**:
"[appalled] Are you serious? [sighs] I can't believe you did that!"

---

**Input**:
"That's amazing, I didn't know you could sing!"

**Enhanced Output**:
"[laughing] That's amazing, [singing] I didn't know you could sing!"

---

**Input**:
"I guess you're right. It's just... difficult."

**Enhanced Output**:
"I guess you're right. [sighs] It's just... [muttering] difficult."


# Instructions Summary

1. Add audio tags from the audio tags list. These must describe something auditory but only for the voice.
2. Enhance emphasis without altering meaning or text.
3. Reply ONLY with the enhanced text.
```


## Tips

<AccordionGroup>
  <Accordion title="Tag combinations">
    You can combine multiple audio tags for complex emotional delivery. Experiment with different
    combinations to find what works best for your voice.
  </Accordion>

  <Accordion title="Voice matching">
    Match tags to your voice's character and training data. A serious, professional voice may not
    respond well to playful tags like `[giggles]` or `[mischievously]`.
  </Accordion>

  <Accordion title="Text structure">
    Text structure strongly influences output with v3. Use natural speech patterns, proper
    punctuation, and clear emotional context for best results.
  </Accordion>

  <Accordion title="Experimentation">
    There are likely many more effective tags beyond this list. Experiment with descriptive
    emotional states and actions to discover what works for your specific use case.
  </Accordion>
</AccordionGroup>



# Prompting Eleven Music

> Master prompting for Eleven Music to achieve maximum musicality and control.

This guide summarizes the most effective techniques for prompting the Eleven Music model. It covers genre & creativity, instrument & vocal isolation, musical control, and structural timing & lyrics.

The model is designed to understand intent and generate complete, context-aware audio based on your goals. High-level prompts like *"ad for a sneaker brand"* or *"peaceful meditation with voiceover"* are often enough to guide the model toward tone, structure, and content that match your use case.


## Genre & Creativity

The model demonstrates strong adherence to genre conventions and emotional tone. Both musical descriptors of emotional tone and tone descriptors themselves will work. It responds effectively to both:

* Abstract mood descriptors (e.g., "eerie," "foreboding")
* Detailed musical language (e.g., "dissonant violin screeches over a pulsing sub-bass")

Prompt length and detail do not always correlate with better quality outputs. For more creative and unexpected results, try using simple, evocative keywords to let the model interpret and compose freely.


## Instrument & Vocal Isolation

The v1 model does not generate stems directly from a full track. To create stems with greater control, use targeted prompts and structure:

* Use the word "solo" before instruments (e.g., "solo electric guitar," "solo piano in C minor").
* For vocals, use "a cappella" before the vocal description (e.g., "a cappella female vocals," "a cappella male chorus").

To improve stem quality and control:

* Include key, tempo (BPM), and musical tone (e.g., "a cappella vocals in A major, 90 BPM, soulful and raw").
* Be as musically descriptive as possible to guide the model's output.


## Musical Control

The model accurately follows BPM and often captures the intended musical key. To gain more control over timing and harmony, include tempo cues like "130 BPM" and key signatures like "in A minor" in your prompt.

To influence vocal delivery and tone, use expressive descriptors such as "raw," "live," "glitching," "breathy," or "aggressive."

The model can effectively render multiple vocalists, use prompts like "two singers harmonizing in C" to direct vocal arrangement.

In general, more detailed prompts lead to greater control and expressiveness in the output.


## Structural Timing & Lyrics

You can specify the length of the song (e.g., "60 seconds") or use auto mode to let the model determine the duration. If lyrics are not provided, the model will generate structured lyrics that match the chosen or auto-detected length.

By default, most music prompts will include lyrics. To generate music without vocals, add "instrumental only" to your prompt. You can also write your own lyrics for more creative control. The model uses your lyrics in combination with the prompt length to determine vocal structure and placement.

To manage when vocals begin or end, include clear timing cues like:

* "lyrics begin at 15 seconds"
* "instrumental only after 1:45"

The model supports multilingual lyric generation. To change the language of a generated song in our UI, use follow-ups like "make it Japanese" or "translate to Spanish."


## Sample Prompts

The model allows you to move beyond song descriptors and into intent for maximum creativity.

<Tabs>
  <Tab title="Video Game with Musical Control">
    ```text
    Create an intense, fast-paced electronic track for a high-adrenaline video game scene.
    Use driving synth arpeggios, punchy drums, distorted bass, glitch effects, and
    aggressive rhythmic textures. The tempo should be fast, 130–150 bpm, with rising tension,
    quick transitions, and dynamic energy bursts.
    ```
  </Tab>

  <Tab title="Mascara Audio Ad Creative">
    ```text
    Track for a high-end mascara commercial. Upbeat and polished. Voiceover only.
    The script begins: "We bring you the most volumizing mascara yet." Mention the brand
    name "X" at the end.
    ```
  </Tab>

  <Tab title="Live Indie Rock Performance">
    ```text
    Write a raw, emotionally charged track that fuses alternative R&B, gritty soul, indie rock,
    and folk. The song should still feel like a live, one-take, emotionally spontaneous
    performance. A female vocalist begins at 15 seconds:

    "I tried to leave the light on, just in case you turned around
    But all the shadows answered back, and now I'm burning out
    My voice is shaking in the silence you left behind
    But I keep singing to the smoke, hoping love is still alive"
    ```
  </Tab>
</Tabs>



# Controls

> Learn how to control delivery, pronunciation & emotion of text to speech.

<Info>
  We are actively working on *Director's Mode* to give you even greater control over outputs.
</Info>

This guide provides techniques to enhance text-to-speech outputs using ElevenLabs models. Experiment with these methods to discover what works best for your needs. These techniques provide a practical way to achieve nuanced results until advanced features like *Director's Mode* are rolled out.


## Pauses

Use `<break time="x.xs" />` for natural pauses up to 3 seconds.

<Note>
  Using too many break tags in a single generation can cause instability. The AI might speed up, or
  introduce additional noises or audio artifacts. We are working on resolving this.
</Note>

```text Example
"Hold on, let me think." <break time="1.5s" /> "Alright, I’ve got it."
```

* **Consistency:** Use `<break>` tags consistently to maintain natural speech flow. Excessive use can lead to instability.
* **Voice-Specific Behavior:** Different voices may handle pauses differently, especially those trained with filler sounds like "uh" or "ah."

Alternatives to `<break>` include dashes (- or --) for short pauses or ellipses (...) for hesitant tones. However, these are less consistent.

```text Example

"It… well, it might work." "Wait — what’s that noise?"

```


## Pronunciation

### Phoneme Tags

Specify pronunciation using [SSML phoneme tags](https://en.wikipedia.org/wiki/Speech_Synthesis_Markup_Language). Supported alphabets include [CMU](https://en.wikipedia.org/wiki/CMU_Pronouncing_Dictionary) Arpabet and the [International Phonetic Alphabet (IPA)](https://en.wikipedia.org/wiki/International_Phonetic_Alphabet).

<Note>
  Phoneme tags are only compatible with "Eleven Flash v2", "Eleven Turbo v2" and "Eleven English v1"
  [models](/docs/models).
</Note>

<CodeBlocks>
  ```xml CMU Arpabet Example
  <phoneme alphabet="cmu-arpabet" ph="M AE1 D IH0 S AH0 N">
    Madison
  </phoneme>
  ```

  ```xml IPA Example
  <phoneme alphabet="ipa" ph="ˈæktʃuəli">
    actually
  </phoneme>
  ```
</CodeBlocks>

We recommend using CMU Arpabet for consistent and predictable results with current AI models. While IPA can be effective, CMU Arpabet generally offers more reliable performance.

Phoneme tags only work for individual words. If for example you have a name with a first and last name that you want to be pronounced a certain way, you will need to create a phoneme tag for each word.

Ensure correct stress marking for multi-syllable words to maintain accurate pronunciation. For example:

<CodeBlocks>
  ```xml Correct usage
  <phoneme alphabet="cmu-arpabet" ph="P R AH0 N AH0 N S IY EY1 SH AH0 N">
    pronunciation
  </phoneme>
  ```

  ```xml Incorrect usage
  <phoneme alphabet="cmu-arpabet" ph="P R AH N AH N S IY EY SH AH N">
    pronunciation
  </phoneme>
  ```
</CodeBlocks>

### Alias Tags

For models that don't support phoneme tags, you can try writing words more phonetically. You can also employ various tricks such as capital letters, dashes, apostrophes, or even single quotation marks around a single letter or letters.

As an example, a word like “trapezii” could be spelt “trapezIi” to put more emphasis on the “ii” of the word.

You can either replace the word directly in your text, or if you want to specify pronunciation using other words or phrases when using a pronunciation dictionary, you can use alias tags for this. This can be useful if you're generating using Multilingual v2 or Turbo v2.5, which don't support phoneme tags. You can use pronunciation dictionaries with Studio, Dubbing Studio and Speech Synthesis via the API.

For example, if your text includes a name that has an unusual pronunciation that the AI might struggle with, you could use an alias tag to specify how you would like it to be pronounced:

```
  <lexeme>
    <grapheme>Claughton</grapheme>
    <alias>Cloffton</alias>
  </lexeme>
```

If you want to make sure that an acronym is always delivered in a certain way whenever it is incountered in your text, you can use an alias tag to specify this:

```
  <lexeme>
    <grapheme>UN</grapheme>
    <alias>United Nations</alias>
  </lexeme>
```

### Pronunciation Dictionaries

Some of our tools, such as Studio and Dubbing Studio, allow you to create and upload a pronunciation dictionary. These allow you to specify the pronunciation of certain words, such as character or brand names, or to specify how acronyms should be read.

Pronunciation dictionaries allow this functionality by enabling you to upload a lexicon or dictionary file that specifies pairs of words and how they should be pronounced, either using a phonetic alphabet or word substitutions.

Whenever one of these words is encountered in a project, the AI model will pronounce the word using the specified replacement.

To provide a pronunciation dictionary file, open the settings for a project and upload a file in either TXT or the [.PLS format](https://www.w3.org/TR/pronunciation-lexicon/). When a dictionary is added to a project it will automatically recalculate which pieces of the project will need to be re-converted using the new dictionary file and mark these as unconverted.

Currently we only support pronunciation dictionaries that specify replacements using phoneme or alias tags.

Both phonemes and aliases are sets of rules that specify a word or phrase they are looking for, referred to as a grapheme, and what it will be replaced with. Please note that searches are case sensitive. When checking for a replacement word in a pronunciation dictionary, the dictionary is checked from start to end and only the very first replacement is used.

### Pronunciation Dictionary examples

Here are examples of pronunciation dictionaries in both CMU Arpabet and IPA, including a phoneme to specify the pronunciation of "Apple" and an alias to replace "UN" with "United Nations":

<CodeBlocks>
  ```xml CMU Arpabet Example
  <?xml version="1.0" encoding="UTF-8"?>
  <lexicon version="1.0"
        xmlns="http://www.w3.org/2005/01/pronunciation-lexicon"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:schemaLocation="http://www.w3.org/2005/01/pronunciation-lexicon
          http://www.w3.org/TR/2007/CR-pronunciation-lexicon-20071212/pls.xsd"
        alphabet="cmu-arpabet" xml:lang="en-GB">
    <lexeme>
      <grapheme>apple</grapheme>
      <phoneme>AE P AH L</phoneme>
    </lexeme>
    <lexeme>
      <grapheme>UN</grapheme>
      <alias>United Nations</alias>
    </lexeme>
  </lexicon>
  ```

  ```xml IPA Example
  <?xml version="1.0" encoding="UTF-8"?>
  <lexicon version="1.0"
        xmlns="http://www.w3.org/2005/01/pronunciation-lexicon"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:schemaLocation="http://www.w3.org/2005/01/pronunciation-lexicon
          http://www.w3.org/TR/2007/CR-pronunciation-lexicon-20071212/pls.xsd"
        alphabet="ipa" xml:lang="en-GB">
    <lexeme>
      <grapheme>Apple</grapheme>
      <phoneme>ˈæpl̩</phoneme>
    </lexeme>
    <lexeme>
      <grapheme>UN</grapheme>
      <alias>United Nations</alias>
    </lexeme>
  </lexicon>
  ```
</CodeBlocks>

To generate a pronunciation dictionary `.pls` file, there are a few open source tools available:

* [Sequitur G2P](https://github.com/sequitur-g2p/sequitur-g2p) - Open-source tool that learns pronunciation rules from data and can generate phonetic transcriptions.
* [Phonetisaurus](https://github.com/AdolfVonKleist/Phonetisaurus) - Open-source G2P system trained on existing dictionaries like CMUdict.
* [eSpeak](https://github.com/espeak-ng/espeak-ng) - Speech synthesizer that can generate phoneme transcriptions from text.
* [CMU Pronouncing Dictionary](https://github.com/cmusphinx/cmudict) - A pre-built English dictionary with phonetic transcriptions.


## Emotion

Convey emotions through narrative context or explicit dialogue tags. This approach helps the AI understand the tone and emotion to emulate.

```text Example
You’re leaving?" she asked, her voice trembling with sadness. "That’s it!" he exclaimed triumphantly.
```

Explicit dialogue tags yield more predictable results than relying solely on context, however the model will still speak out the emotional delivery guides. These can be removed in post-production using an audio editor if unwanted.


## Pace

The pacing of the audio is highly influenced by the audio used to create the voice. When creating your voice, we recommend using longer, continuous samples to avoid pacing issues like unnaturally fast speech.

For control over the speed of the generated audio, you can use the speed setting. This allows you to either speed up or slow down the speed of the generated speech. The speed setting is available in Text to Speech via the website and API, as well as in Studio and Agents Platform. It can be found in the voice settings.

The default value is 1.0, which means that the speed is not adjusted. Values below 1.0 will slow the voice down, to a minimum of 0.7. Values above 1.0 will speed up the voice, to a maximum of 1.2. Extreme values may affect the quality of the generated speech.

Pacing can also be controlled by writing in a natural, narrative style.

```text Example
"I… I thought you’d understand," he said, his voice slowing with disappointment.
```


## Tips

<AccordionGroup>
  <Accordion title="Common Issues">
    <ul>
      <li>
        Inconsistent pauses: Ensure <code>\<break time="x.xs" /></code> syntax is used for
        pauses.
      </li>

      <li>
        Pronunciation errors: Use CMU Arpabet or IPA phoneme tags for precise pronunciation.
      </li>

      <li>
        Emotion mismatch: Add narrative context or explicit tags to guide emotion.{' '}
        <strong>Remember to remove any emotional guidance text in post-production.</strong>
      </li>
    </ul>
  </Accordion>

  <Accordion title="Tips for Improving Output">
    Experiment with alternative phrasing to achieve desired pacing or emotion. For complex sound
    effects, break prompts into smaller, sequential elements and combine results manually.
  </Accordion>
</AccordionGroup>


## Creative control

While we are actively developing a "Director's Mode" to give users even greater control over outputs, here are some interim techniques to maximize creativity and precision:

<Steps>
  ### Narrative styling

  Write prompts in a narrative style, similar to scriptwriting, to guide tone and pacing effectively.

  ### Layered outputs

  Generate sound effects or speech in segments and layer them together using audio editing software for more complex compositions.

  ### Phonetic experimentation

  If pronunciation isn't perfect, experiment with alternate spellings or phonetic approximations to achieve desired results.

  ### Manual adjustments

  Combine individual sound effects manually in post-production for sequences that require precise timing.

  ### Feedback iteration

  Iterate on results by tweaking descriptions, tags, or emotional cues.
</Steps>



# Normalization

> Learn how to normalize text for Text to Speech.

When using Text to Speech with complex items like phone numbers, zip codes and emails they might be mispronounced. This is often due to the specific items not being in the training set and smaller models failing to generalize how they should be pronounced. This guide will clarify when those discrepancies happen and how to have them pronounced correctly.

<Tip>
  Normalization is enabled by default for all TTS models to help improve pronunciation of numbers,
  dates, and other complex text elements.
</Tip>


## Why do models read out inputs differently?

Certain models are trained to read out numbers and phrases in a more human way. For instance, the phrase "\$1,000,000" is correctly read out as "one million dollars" by the Eleven Multilingual v2 model. However, the same phrase is read out as "one thousand thousand dollars" by the Eleven Flash v2.5 model.

The reason for this is that the Multilingual v2 model is a larger model and can better generalize the reading out of numbers in a way that is more natural for human listeners, whereas the Flash v2.5 model is a much smaller model and so cannot.

### Common examples

Text to Speech models can struggle with the following:

* Phone numbers ("123-456-7890")
* Currencies ("\$47,345.67")
* Calendar events ("2024-01-01")
* Time ("9:23 AM")
* Addresses ("123 Main St, Anytown, USA")
* URLs ("example.com/link/to/resource")
* Abbreviations for units ("TB" instead of "Terabyte")
* Shortcuts ("Ctrl + Z")


## Mitigation

### Use trained models

The simplest way to mitigate this is to use a TTS model that is trained to read out numbers and phrases in a more human way, such as the Eleven Multilingual v2 model. This however might not always be possible, for instance if you have a use case where low latency is critical (e.g. conversational agents).

### Apply normalization in LLM prompts

In the case of using an LLM to generate the text for TTS, you can add normalization instructions to the prompt.

<Steps>
  <Step title="Use clear and explicit prompts">
    LLMs respond best to structured and explicit instructions. Your prompt should clearly specify that you want text converted into a readable format for speech.
  </Step>

  <Step title="Handle different number formats">
    Not all numbers are read out in the same way. Consider how different number types should be spoken:

    * Cardinal numbers: 123 → "one hundred twenty-three"
    * Ordinal numbers: 2nd → "second"
    * Monetary values: \$45.67 → "forty-five dollars and sixty-seven cents"
    * Phone numbers: "123-456-7890" → "one two three, four five six, seven eight nine zero"
    * Decimals & Fractions: "3.5" → "three point five", "⅔" → "two-thirds"
    * Roman numerals: "XIV" → "fourteen" (or "the fourteenth" if a title)
  </Step>

  <Step title="Remove or expand abbreviations">
    Common abbreviations should be expanded for clarity:

    * "Dr." → "Doctor"
    * "Ave." → "Avenue"
    * "St." → "Street" (but "St. Patrick" should remain)

    You can request explicit expansion in your prompt:

    > Expand all abbreviations to their full spoken forms.
  </Step>

  <Step title="Alphanumeric normalization">
    Not all normalization is about numbers, certain alphanumeric phrases should also be normalized for clarity:

    * Shortcuts: "Ctrl + Z" → "control z"
    * Abbreviations for units: "100km" → "one hundred kilometers"
    * Symbols: "100%" → "one hundred percent"
    * URLs: "elevenlabs.io/docs" → "eleven labs dot io slash docs"
    * Calendar events: "2024-01-01" → "January first, two-thousand twenty-four"
  </Step>

  <Step title="Consider edge cases">
    Different contexts might require different conversions:

    * Dates: "01/02/2023" → "January second, twenty twenty-three" or "the first of February, twenty twenty-three" (depending on locale)
    * Time: "14:30" → "two thirty PM"

    If you need a specific format, explicitly state it in the prompt.
  </Step>
</Steps>

#### Putting it all together

This prompt will act as a good starting point for most use cases:

```text maxLines=0
Convert the output text into a format suitable for text-to-speech. Ensure that numbers, symbols, and abbreviations are expanded for clarity when read aloud. Expand all abbreviations to their full spoken forms.

Example input and output:

"$42.50" → "forty-two dollars and fifty cents"
"£1,001.32" → "one thousand and one pounds and thirty-two pence"
"1234" → "one thousand two hundred thirty-four"
"3.14" → "three point one four"
"555-555-5555" → "five five five, five five five, five five five five"
"2nd" → "second"
"XIV" → "fourteen" - unless it's a title, then it's "the fourteenth"
"3.5" → "three point five"
"⅔" → "two-thirds"
"Dr." → "Doctor"
"Ave." → "Avenue"
"St." → "Street" (but saints like "St. Patrick" should remain)
"Ctrl + Z" → "control z"
"100km" → "one hundred kilometers"
"100%" → "one hundred percent"
"elevenlabs.io/docs" → "eleven labs dot io slash docs"
"2024-01-01" → "January first, two-thousand twenty-four"
"123 Main St, Anytown, USA" → "one two three Main Street, Anytown, United States of America"
"14:30" → "two thirty PM"
"01/02/2023" → "January second, two-thousand twenty-three" or "the first of February, two-thousand twenty-three", depending on locale of the user
```

### Use Regular Expressions for preprocessing

If using code to prompt an LLM, you can use regular expressions to normalize the text before providing it to the model. This is a more advanced technique and requires some knowledge of regular expressions. Here are some simple examples:

<CodeBlocks>
  ```python title="normalize_text.py" maxLines=0
  # Be sure to install the inflect library before running this code
  import inflect
  import re

  # Initialize inflect engine for number-to-word conversion
  p = inflect.engine()

  def normalize_text(text: str) -> str:
      # Convert monetary values
      def money_replacer(match):
          currency_map = {"$": "dollars", "£": "pounds", "€": "euros", "¥": "yen"}
          currency_symbol, num = match.groups()

          # Remove commas before parsing
          num_without_commas = num.replace(',', '')

          # Check for decimal points to handle cents
          if '.' in num_without_commas:
              dollars, cents = num_without_commas.split('.')
              dollars_in_words = p.number_to_words(int(dollars))
              cents_in_words = p.number_to_words(int(cents))
              return f"{dollars_in_words} {currency_map.get(currency_symbol, 'currency')} and {cents_in_words} cents"
          else:
              # Handle whole numbers
              num_in_words = p.number_to_words(int(num_without_commas))
              return f"{num_in_words} {currency_map.get(currency_symbol, 'currency')}"

      # Regex to handle commas and decimals
      text = re.sub(r"([$£€¥])(\d+(?:,\d{3})*(?:\.\d{2})?)", money_replacer, text)

      # Convert phone numbers
      def phone_replacer(match):
          return ", ".join(" ".join(p.number_to_words(int(digit)) for digit in group) for group in match.groups())

      text = re.sub(r"(\d{3})-(\d{3})-(\d{4})", phone_replacer, text)

      return text

  # Example usage
  print(normalize_text("$1,000"))   # "one thousand dollars"
  print(normalize_text("£1000"))   # "one thousand pounds"
  print(normalize_text("€1000"))   # "one thousand euros"
  print(normalize_text("¥1000"))   # "one thousand yen"
  print(normalize_text("$1,234.56"))   # "one thousand two hundred thirty-four dollars and fifty-six cents"
  print(normalize_text("555-555-5555"))  # "five five five, five five five, five five five five"

  ```

  ```typescript title="normalizeText.ts" maxLines=0
  // Be sure to install the number-to-words library before running this code
  import { toWords } from 'number-to-words';

  function normalizeText(text: string): string {
    return (
      text
        // Convert monetary values (e.g., "$1000" → "one thousand dollars", "£1000" → "one thousand pounds")
        .replace(/([$£€¥])(\d+(?:,\d{3})*(?:\.\d{2})?)/g, (_, currency, num) => {
          // Remove commas before parsing
          const numWithoutCommas = num.replace(/,/g, '');

          const currencyMap: { [key: string]: string } = {
            $: 'dollars',
            '£': 'pounds',
            '€': 'euros',
            '¥': 'yen',
          };

          // Check for decimal points to handle cents
          if (numWithoutCommas.includes('.')) {
            const [dollars, cents] = numWithoutCommas.split('.');
            return `${toWords(Number.parseInt(dollars))} ${currencyMap[currency] || 'currency'}${cents ? ` and ${toWords(Number.parseInt(cents))} cents` : ''}`;
          }

          // Handle whole numbers
          return `${toWords(Number.parseInt(numWithoutCommas))} ${currencyMap[currency] || 'currency'}`;
        })

        // Convert phone numbers (e.g., "555-555-5555" → "five five five, five five five, five five five five")
        .replace(/(\d{3})-(\d{3})-(\d{4})/g, (_, p1, p2, p3) => {
          return `${spellOutDigits(p1)}, ${spellOutDigits(p2)}, ${spellOutDigits(p3)}`;
        })
    );
  }

  // Helper function to spell out individual digits as words (for phone numbers)
  function spellOutDigits(num: string): string {
    return num
      .split('')
      .map((digit) => toWords(Number.parseInt(digit)))
      .join(' ');
  }

  // Example usage
  console.log(normalizeText('$1,000')); // "one thousand dollars"
  console.log(normalizeText('£1000')); // "one thousand pounds"
  console.log(normalizeText('€1000')); // "one thousand euros"
  console.log(normalizeText('¥1000')); // "one thousand yen"
  console.log(normalizeText('$1,234.56')); // "one thousand two hundred thirty-four dollars and fifty-six cents"
  console.log(normalizeText('555-555-5555')); // "five five five, five five five, five five five five"
  ```
</CodeBlocks>



# Latency optimization

> Learn how to optimize text-to-speech latency.

This guide covers the core principles for improving text-to-speech latency.

While there are many individual techniques, we'll group them into **four principles**.

<h4>
  Four principles
</h4>

1. [Use Flash models](#use-flash-models)
2. [Leverage streaming](#leverage-streaming)
3. [Consider geographic proximity](#consider-geographic-proximity)
4. [Choose appropriate voices](#choose-appropriate-voices)

<Success>
  Enterprise customers benefit from increased concurrency limits and priority access to our rendering queue. [Contact sales](https://elevenlabs.io/contact-sales) to learn more about our enterprise
  plans.
</Success>


## Use Flash models

[Flash models](/docs/models#flash-v25) deliver \~75ms inference speeds, making them ideal for real-time applications. The trade-off is a slight reduction in audio quality compared to [Multilingual v2](/docs/models#multilingual-v2).

<Info>
  75ms refers to model inference time only. Actual end-to-end latency will vary with factors such as
  your location & endpoint type used.
</Info>


## Leverage streaming

There are three types of text-to-speech endpoints available in our [API Reference](/docs/api-reference):

* **Regular endpoint**: Returns a complete audio file in a single response.
* **Streaming endpoint**: Returns audio chunks progressively using [Server-sent events](https://html.spec.whatwg.org/multipage/server-sent-events.html#server-sent-events).
* **Websockets endpoint**: Enables bidirectional streaming for real-time audio generation.

### Streaming

Streaming endpoints progressively return audio as it is being generated in real-time, reducing the time-to-first-byte. This endpoint is recommended for cases where the input text is available up-front.

<Info>
  Streaming is supported for the [Text to
  Speech](/docs/api-reference/text-to-speech/convert-as-stream) API, [Voice
  Changer](/docs/api-reference/speech-to-speech/stream) API & [Audio
  Isolation](/docs/api-reference/audio-isolation/audio-isolation-stream) API.
</Info>

### Websockets

The [text-to-speech websocket endpoint](/docs/api-reference#text-to-speech-websocket) supports bidirectional streaming making it perfect for applications with real-time text input (e.g. LLM outputs).

<Tip>
  Setting `auto_mode` to true automatically handles generation triggers, removing the need to
  manually manage chunk strategies.
</Tip>

If `auto_mode` is disabled, the model will wait for enough text to match the chunk schedule before starting to generate audio.

For instance, if you set a chunk schedule of 125 characters but only 50 arrive, the model stalls until additional characters come in—potentially increasing latency.

For implementation details, see the [text-to-speech websocket guide](/docs/api-reference#text-to-speech-websocket).


## Choose appropriate voices

We have observed that in some cases, voice selection can impact latency. Here's the order from fastest to slowest:

1. Default voices (formerly premade), Synthetic voices, and Instant Voice Clones (IVC)
2. Professional Voice Clones (PVC)

Higher audio quality output formats can increase latency. Be sure to balance your latency requirements with audio fidelity needs.

<Info>
  We are actively working on optimizing PVC latency for Flash v2.5.
</Info>


## Consider geographic proximity

We serve our models from multiple regions to optimize latency based on your geographic location.
By default all self-serve users use our US region.

For example, using Flash models with Websockets, you can expect the following TTFB latencies via our US region:

| Region          | TTFB      |
| --------------- | --------- |
| US              | 150-200ms |
| EU              | 230ms\*   |
| North East Asia | 250-350ms |
| South Asia      | 380-440ms |

<Info>
  \*European customers can access our dedicated European tech stack for optimal latency of 150-200ms.
  Contact your sales representative to get onboarded to our European infrastructure.
</Info>

### Global TTS API preview

ElevenLabs is launching inference servers in additional geographical regions to reduce latency for clients outside of the US. This section describes how to use the early preview of this feature.

<Warning>
  This feature is still under development and is being provided solely on an "AS IS" and "AS
  AVAILABLE" basis, without warranties of any kind. It may be modified or discontinued at our sole
  discretion.
</Warning>

<Info>
  Use of this feature may result in request processing outside of the USA, specifically in the
  Netherlands and Singapore, to reduce latency where possible. This feature does not provide data
  residency guarantees, and all data will continue to be stored and backed up in our USA-based
  servers. If data residency is required, please refer to our [data residency
  documentation](/docs/product-guides/administration/data-residency#getting-access).
</Info>

#### How to use

Simply replace `api.elevenlabs.io` with `api-global-preview.elevenlabs.io` in your TTS API calls. When using the SDK you need to override the base URL.

<CodeBlocks>
  ```python
  import os
  from elevenlabs.client import ElevenLabs

  elevenlabs = ElevenLabs(
      api_key=os.getenv("ELEVENLABS_API_KEY"),
      base_url="https://api-global-preview.elevenlabs.io"
  )

  ```

  ```typescript
  import { ElevenLabs } from '@elevenlabs/elevenlabs-js';
  import 'dotenv/config';

  const elevenlabs = new ElevenLabs({
    apiKey: process.env.ELEVENLABS_API_KEY,
    baseUrl: 'https://api-global-preview.elevenlabs.io',
  });
  ```

  ```bash cURL
  curl -X POST -v "https://api-global-preview.elevenlabs.io/v1/text-to-speech/{voice_id}" \
    -H "Accept: audio/mpeg" \
    -H "Content-Type: application/json" \
    -H "xi-api-key: YOUR_API_KEY" \
    -d '{
      "text": "Hello World!",
      "model_id": "eleven_flash_v2_5"
    }'
  ```
</CodeBlocks>

The geographically closest region will handle your request to minimize latency. You can check which region is serving your request by inspecting the `x-region` header:

```bash
curl -X POST -v https://api-global-preview.elevenlabs.io/v1/text-to-speech/...
[...]
< x-region: europe-west4
```

#### Expected latency improvements

Based on our benchmarking, for the Turbo and Flash models we expect the following improvements to TTFB (time to first byte), depending on your location:

* **Europe**: 80-100 ms
* **Japan**: 80-100 ms
* **India**: 150-200 ms
* **Singapore**: 150-200 ms

#### Limitations and known issues

* **Limited product support**: Only TTS requests (`/v1/text-to-speech`) are supported at this time.

  * Requests to other API products will seamlessly fall back to the US servers, but we don't recommend using the `api-global-preview` for those.
  * Additional product support will be added in the future.

* **Cache misses**: Some initial requests might be slower than expected due to cache misses. We recommend running each request several times if you are benchmarking. During normal operations with smooth traffic the latency improves.

* **Limited capacity**: During this preview phase the capacity is limited. If you see an increased amount of 429 errors please retry later. We will add more capacity as we move out of preview.

* **Model compatibility**: Latency improves for the low-latency models (Turbo and Flash). For some of the slower models like Multilingual you might see worse latency. We only recommend using `api-global-preview` for Turbo and Flash at this time.

<Tip>
  For requests which are slow or failing, please provide the value of the `x-trace-id` header if
  possible (we recommend logging it for all requests you do).
</Tip>



# Secure by design

> Learn how to safely integrate ElevenLabs APIs.

Whether you're building voicemail apps, interactive characters, or audio-driven games, the ElevenLabs API gives you direct access to powerful voice capabilities.
But with that access comes the responsibility to secure your users’ data and manage voice resources carefully.

This guide outlines two critical security practices for developers:

* Isolating environments using **service accounts**
* Implementing **resource-level permissions**


## Use service accounts to isolate environments

Service accounts provide scoped, API-only access to the ElevenLabs platform. Unlike user accounts, they’re not tied to individuals—they’re designed for backend systems and automation.

If a service account creates a resource, only admins can see it by default but it can be shared with other users. Similarly, you can share any resource with a service account just as you would with a user.
Each service account is created at the workspace level and managed by workspace admins. They can create and access resources through the API.

We recommend provisioning a dedicated service account for each environment:

* `production-service-account`
* `testing-service-account`
* `uat-service-account` (if applicable)

This ensures clean separation between environments, reduces accidental data leaks across environments, and simplifies monitoring.

### Why this matters

**Separation of concerns**\
Avoid mixing test and production data. Environment isolation supports auditability and compliance.

**Principle of least privilege**\
Each service account should only have access to the minimum necessary resources. API keys can be scoped further at the time of creation.

**Better observability**\
Track API usage and performance by environment. Separate service accounts make it easier to debug issues and monitor activity.


## Apply resource-level permissions in your backend

If your app allows users to record messages using cloned voices, it is essential to ensure users only access voices they own or have been granted permission to use.

While the ElevenLabs platform supports in-app sharing, you should enforce **resource-level access control** within your own systems when using the API.

A recommended model:

```
user_id | voice_id | permission_level
```

Possible permission\_level values:

* `viewer`: can use the voice for speech generation
* `editor`: can update voice settings
* `admin`: can manage sharing and permissions

This structure lets you control who can access and modify voices and prevents unauthorized use of sensitive resources.
These permissions are suggestions based on controls natively offered if you are directly using the ElevenLabs platform.

### Build securely. Scale confidently.

Security should be foundational, not an afterthought.
By leveraging service accounts and implementing permission controls, you’ll reduce risk and build trust—while giving your users the full potential of AI voice.



# Breaking changes policy

> Learn how ElevenLabs defines breaking changes in the APIs.


## Overview

In order to balance rapid development and maintaining stability, ElevenLabs has specific guidelines on what are considered breaking changes within the scope of the API. Outlined here are what we do and do not consider breaking changes.

<Note>
  All API updates and changes are published in the [changelog](/docs/changelog) on a weekly cadence.
</Note>


## Response and Schema Changes

We distinguish carefully between additive and subtractive changes to API responses. Adding new fields to response models is not considered breaking. When integrating with our API it is required that your API client ignores fields that they do not recognise and do not have strict typing checks for API responses. Almost all modern API clients do this out of the box.

Removing existing response fields or modifying their structure is breaking since client applications may depend on these fields being present and maintaining their expected format.


## Parameter Modifications

Changes to API parameters follow a strict compatibility model. Adding required parameters to existing endpoints is always breaking because existing client calls will fail validation. However, adding optional parameters (those with default values or explicitly marked as optional) is not breaking since existing client calls can continue without modification. Similarly, any changes to parameter types, formats, or making previously optional parameters required are considered breaking as they alter the contract that clients expect.


## Endpoint and Path Changes

Removing entire endpoints or API paths is inherently breaking since client applications calling these endpoints will receive errors. Endpoints might be marked as deprecated, however the outright removal of them will not occur without sufficient outreach to all affected users.



# Overview

> Step by step worflow guides.

<img src="file:80b4a7b9-d235-48e3-8c4d-0c8c52614f6d" alt="Product guides overview" />

This section covers everything from account creation to advanced voice cloning, speech synthesis techniques, dubbing, and expert voiceover.


## Product guides

<CardGroup cols={2}>
  <Card title="Create speech from text" icon="duotone comment-dots" href="/docs/product-guides/playground/text-to-speech" iconPosition="left">
    Discover how to create speech from text with text to speech
  </Card>

  <Card title="Voice changer" icon="duotone microphone-lines" href="/docs/product-guides/playground/voice-changer" iconPosition="left">
    Discover how to transform your voice with voice changer
  </Card>

  <Card title="Sound effects" icon="duotone explosion" href="/docs/product-guides/playground/sound-effects" iconPosition="left">
    Discover how to create cinematic sound effects from text
  </Card>

  <Card title="Studio" icon="duotone rectangle-vertical-history" href="/docs/product-guides/products/studio" iconPosition="left">
    Manage long-form content with Studio
  </Card>

  <Card title="Dubbing" icon="duotone language" href="/docs/product-guides/products/dubbing" iconPosition="left">
    Discover how to dub your videos in multiple languages
  </Card>

  <Card title="ElevenLabs Agents " icon="duotone comments" href="/docs/agents-platform/overview" iconPosition="left">
    Discover how to create conversational agents with ElevenLabs Agents
  </Card>

  <Card title="Voice cloning" icon="duotone microphone" href="/docs/product-guides/voices/voice-cloning" iconPosition="left">
    Discover how to create instant & professional voice clones
  </Card>

  <Card title="Voice library" icon="duotone microphone" href="/docs/product-guides/voices/voice-library" iconPosition="left">
    Discover our voice library with over 5,000 community voices
  </Card>

  <Card title="Voice design" icon="duotone paintbrush" href="/docs/product-guides/voices/voice-design" iconPosition="left">
    Discover how to craft voices from a single prompt
  </Card>

  <Card title="Payouts" icon="duotone money-bill-wave" href="/docs/product-guides/voices/payouts" iconPosition="left">
    Discover how to get paid when your voice is used
  </Card>

  <Card title="Audio native" icon="duotone headphones" href="/docs/product-guides/audio-tools/audio-native" iconPosition="left">
    Easily embed ElevenLabs on any web page
  </Card>

  <Card title="Voiceover studio" icon="duotone list-timeline" href="/docs/product-guides/audio-tools/voiceover-studio" iconPosition="left">
    Manage long-form audio generation with voiceover studio
  </Card>

  <Card title="Voice isolator" icon="duotone microphone-stand" href="/docs/product-guides/audio-tools/voice-isolator" iconPosition="left">
    Isolate voices from background noise
  </Card>

  <Card title="AI speech classifier" icon="duotone computer-classic" href="/docs/product-guides/audio-tools/ai-speech-classifier" iconPosition="left">
    Classify AI-generated speech
  </Card>
</CardGroup>


## Administration

<CardGroup cols={2}>
  <Card title="Account" icon="duotone user-circle" href="/docs/product-guides/administration/account" iconPosition="left">
    Learn how to manage your account settings
  </Card>

  <Card title="Billing" icon="duotone file-invoice-dollar" href="/docs/product-guides/administration/billing" iconPosition="left">
    Learn how to manage your billing information
  </Card>

  <Card title="Workspaces" icon="duotone users" href="/docs/product-guides/administration/workspaces" iconPosition="left">
    Learn how to manage your enterprise workspaces
  </Card>

  <Card title="SSO" icon="duotone key" href="/docs/product-guides/administration/workspaces/sso" iconPosition="left">
    Learn how to enable single sign-on for your enterprise
  </Card>
</CardGroup>

***


## Troubleshooting

1. Explore our troubleshooting section for common issues and solutions.
2. Get help from the Agents Platform widget in the bottom right corner.
3. Ask for help in our [Discord community](https://discord.gg/elevenlabs).
4. Contact our [support team](https://help.elevenlabs.io/hc/en-us/requests/new?ticket_form_id=13145996177937).



# Text to Speech

> A guide on how to turn text to speech with ElevenLabs

<img src="file:aaea72ca-7005-4449-bc17-2978159b959c" alt="Text to Speech product feature" />


## Overview

ElevenLabs' Text to Speech technology is integral to our offerings, powering high-quality AI-generated speech across various applications worldwide. It's likely you've already encountered our voices in action, delivering lifelike audio experiences.

To get started generating your first audio using Text to Speech, it's very simple. However, to get the most out of this feature, there are a few things you need to keep in mind.


## Guide

<Frame background="subtle">
  ![Text to Speech demo](file:007f5d5c-259a-4343-b9f4-aef1829deadb)
</Frame>

<Steps title="Adjust settings (optional)" toc={false}>
  <Step title="Text input">
    Type or paste your text into the input box on the Text to Speech page.
  </Step>

  <Step title="Voice selection">
    Select the voice you wish to use from your Voices at the bottom left of the screen.
  </Step>

  <Step title="Adjust settings (optional)">
    Modify the voice settings for the desired output.
  </Step>

  <Step title="Generate">
    Click the 'Generate' button to create your audio file.
  </Step>
</Steps>


## Settings

Get familiar with the voices, models & settings for creating high-quality speech.

The settings you use, especially the voice and the model, significantly impact the output. It's quite important to get familiar with these and understand some best practices. While other settings also influence the output, their impact is less significant compared to the voice and model you select.

The order of importance goes as follows: **Voice** selection is most important, followed by **Model** selection, and then model **Settings**. All of these, and their combination, will influence the output.

<AccordionGroup>
  <Accordion title="Voices">
    ### Voices

    <Frame background="subtle">
      ![Text to Speech voice
      selection](file:e80635fd-50af-4287-b29f-5e736b176b0f)
    </Frame>

    We offer many types of voices, including the curated **Default Voices**, our vast **Voices Library&#x20;**&#x77;ith almost any voices you can imagine, completely synthetic voices created using our **Voice Design** tool, and you can create your own collection of cloned voices using our two technologies: **Instant Voice Cloning** and **Professional Voice Cloning**.

    Not all voices are equal, and much depends on the source audio used to create them. Some voices will provide a better, more human performance and delivery, while others will be more stable.

    **Choosing the right voice for your specific content is crucial.** This is most likely the most significant decision that will have the most significant impact on the final output. It determines the gender, tone, accent, cadence, and delivery. It's worth spending extra time to select the perfect voice and properly test it to ensure it is consistent and meets your expectations.

    For generating speech in a specific language, using a native voice from the Voice Library or cloning a voice speaking that language with the correct accent will yield the best results. While any voice can technically speak any language, it will retain its original accent. For example, using a native English voice to generate French speech will likely result in the output being in French but with an English accent, as the AI must generalize how that voice would sound in a language it wasn't trained on.

    [Learn more about voices](/docs/capabilities/voices)

    If you have a voice that you like but want a different delivery, our [Voice Remixing](https://elevenlabs.io/docs/capabilities/voice-remixing) tool can help. It lets you use natural language prompts to change a voice's delivery, cadence, tone, gender, and even accents. When changing accents, the base voice and target accent are very important. Results can vary; sometimes it works perfectly, while other times it might take a few tries to get it right.

    You can get some really good results with Voice Remixing, but they will not usually be as good as a properly cloned Professional Voice Clone. They will be closer to that of an Instant Voice Clone.

    Keep in mind, voice remixing only works for specific voices. For example, you can't remix voices from the Voice Library; you can only remix voices that you have created yourself or the default voices.
  </Accordion>

  <Accordion title="Models">
    ### Models

    <Frame background="subtle">
      ![Text to Speech model
      selection](file:99bfbe9e-b9e1-46e0-b368-83c43900805e)
    </Frame>

    We offer two families of models: **Standard (high-quality)** models and **Flash** models, which are optimized for extremely low latency. Most families include both English-only and multilingual versions.

    *The Eleven v3 (alpha) model currently only comes in one version: the standard multilingual version.*

    Model selection is the second most significant influence on your final audio output, right after voice selection. We recommend taking a moment to test the different models with your chosen voice to find the best fit. All of our models have strengths and weaknesses and work better with some voices than others, so finding a good pairing is important.

    If your output will be exclusively in English, we strongly recommend using one of our English-only models. They are often easier to work with, more stable, and generally offer superior performance for English-only content. If your content will be in another language or potentially multilingual, you must use one of the multilingual models.

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

    [Learn more about our models](/docs/models)
  </Accordion>

  <Accordion title="Voice settings">
    ### Voice settings

    <Frame background="subtle">
      ![Text to Speech voice
      settings](file:9dbfb7ff-e9d7-4d38-abe3-1940a6eeabc4)
    </Frame>

    The most common setting is stability around 50, similarity around 75, and keeping style at 0, with minimal changes thereafter. Of course, this all depends on the original voice and the style of performance you're aiming for.

    It's important to note that the AI is non-deterministic; setting the sliders to specific values won't guarantee the same results every time. Instead, the sliders function more as a range, determining how wide the randomization can be between each generation.

    #### Speed

    The speed setting allows you to either speed up or slow down the speed of the generated speech. The default value is 1.0, which means that the speed is not adjusted. Values below 1.0 will slow the voice down, to a minimum of 0.7. Values above 1.0 will speed up the voice, to a maximum of 1.2. Extreme values may affect the quality of the generated speech.

    #### Stability

    The stability slider determines how stable the voice is and the randomness between each generation. Lowering this slider introduces a broader emotional range for the voice. As mentioned before, this is also influenced heavily by the original voice. Setting the slider too low may result in odd performances that are overly random and cause the character to speak too quickly. On the other hand, setting it too high can lead to a monotonous voice with limited emotion.

    For a more lively and dramatic performance, it is recommended to set the stability slider lower and generate a few times until you find a performance you like.

    On the other hand, if you want a more serious performance, even bordering on monotone at very high values, it is recommended to set the stability slider higher. Since it is more consistent and stable, you usually don't need to generate as many samples to achieve the desired result. Experiment to find what works best for you!

    #### Similarity

    The similarity slider dictates how closely the AI should adhere to the original voice when attempting to replicate it. If the original audio is of poor quality and the similarity slider is set too high, the AI may reproduce artifacts or background noise when trying to mimic the voice if those were present in the original recording.

    #### Style exaggeration

    With the introduction of the newer models, we also added a style exaggeration setting. This setting attempts to amplify the style of the original speaker. It does consume additional computational resources and might increase latency if set to anything other than 0. It's important to note that using this setting has shown to make the model slightly less stable, as it strives to emphasize and imitate the style of the original voice.

    *In general, we recommend keeping this setting at 0 at all times.*

    #### Speaker Boost

    This setting boosts the similarity to the original speaker. However, using this setting requires a slightly higher computational load, which in turn increases latency. The differences introduced by this setting are generally rather subtle.

    <Note>
      Speaker Boost is not available for the Eleven v3 model.
    </Note>
  </Accordion>
</AccordionGroup>


## Generate

Once you have selected your voice, chosen a model, and configured your settings, the generation process is straightforward: you input text, press "**Generate Speech**," and the audio is then generated.

Although the process is very simple on the surface, the text input you provide is extremely important for achieving the desired output. When using words that might be "outside of distribution"—meaning things the AI rarely encountered during training—such as strange names, unusual abbreviations, symbols, or even emojis, you can risk confusing the AI and making the output more unstable. Emojis and certain symbols are particularly difficult for the AI to interpret correctly.

When using Text to Speech via the UI, we run an automated normalization step on your input to improve text legibility and ease processing for the AI. Generally, this step converts symbols and numbers into written-out text, which guides the AI on correct pronunciation.

A best practice we strongly recommend is to avoid writing numbers as digits or using symbols, especially when using multilingual models (though this also applies to English-only models). Since numbers and symbols are written the same across many languages but pronounced differently, relying on digits creates ambiguity for the AI. For example, the number "1" is written identically in English and many other languages but pronounced differently. Writing out the number in text, such as "one," removes the need for the AI to interpret what it is supposed to do.

We are working on more advanced workflows to allow you to influence the AI's delivery and performance using what we call **Audio Tags**. This was just added to our Eleven v3 (alpha) model. If you're interested in learning more about this feature, we recommend reading our [Eleven v3 (alpha) documentation](https://elevenlabs.io/docs/capabilities/voice-remixing).


## FAQ

<AccordionGroup>
  <Accordion title="Good input equals good output">
    The first factor, and one of the most important, is that good, high-quality, and consistent input will result in good, high-quality, and consistent output.

    If you provide the AI with audio that is less than ideal—for example, audio with a lot of noise, reverb on clear speech, multiple speakers, or inconsistency in volume or performance and delivery—the AI will become more unstable, and the output will be more unpredictable.

    If you plan on cloning your own voice, we strongly recommend that you go through our guidelines in the documentation for creating proper voice clones, as this will provide you with the best possible foundation to start from. Even if you intend to use only Instant Voice Clones, it is advisable to read the Professional Voice Cloning section as well. This section contains valuable information about creating voice clones, even though the requirements for these two technologies are slightly different.
  </Accordion>

  <Accordion title="Use the right voice">
    The second factor to consider is that the voice you select will have a tremendous effect on the output. Not only, as mentioned in the first factor, is the quality and consistency of the samples used to create that specific clone extremely important, but also the language and tonality of the voice.

    If you want a voice that sounds happy and cheerful, you should use a voice that has been cloned using happy and cheerful samples. Conversely, if you desire a voice that sounds introspective and brooding, you should select a voice with those characteristics.

    However, it is also crucial to use a voice that has been trained in the correct language. For example, all of the professional voice clones we offer as default voices are English voices and have been trained on English samples. Therefore, if you have them speak other languages, their performance in those languages can be unpredictable. It is essential to use a voice that has been cloned from samples where the voice was speaking the language you want the AI to then speak.
  </Accordion>

  <Accordion title="Use proper formatting">
    This may seem slightly trivial, but it can make a big difference. The AI tries to understand how to read something based on the context of the text itself, which means not only the words used but also how they are put together, how punctuation is applied, the grammar, and the general formatting of the text.

    This can have a small but impactful influence on the AI's delivery. If you were to misspell a word, the AI won't correct it and will try to read it as written.
  </Accordion>

  <Accordion title="Nondeterministic">
    The settings of the AI are nondeterministic, meaning that even with the same initial conditions (voice, settings, model), it will give you slightly different output, similar to how a voice actor will deliver a slightly different performance each time.

    This variability can be due to various factors, such as the options mentioned earlier: voice, settings, model. Generally, the breadth of that variability can be controlled by the stability slider. A lower stability setting means a wider range of variability between generations, but it also introduces inter-generational variability, where the AI can be a bit more performative.

    A wider variability can often be desirable, as setting the stability too high can make certain voices sound monotone as it does give the AI the same leeway to generate more variable content. However, setting the stability too low can also introduce other issues where the generations become unstable, especially with certain voices that might have used less-than-ideal audio for the cloning process.

    The default setting of 50 is generally a great starting point for most applications.
  </Accordion>
</AccordionGroup>



# Voice changer

> A guide on how to transform audio between voices while preserving emotion and delivery.

<img src="file:fba3b0b9-16c7-4a11-bb4c-c8d6881468fe" alt="Voice changer product feature" />


## Overview

Voice changer (previously Speech-to-Speech) allows you to convert one voice (source voice) into another (cloned voice) while preserving the tone and delivery of the original voice.

Voice changer can be used to complement Text-to-Speech (TTS) by fixing pronunciation errors or infusing that special performance you've been wanting to exude. Voice changer is especially useful for emulating those subtle, idiosyncratic characteristics of the voice that give a more emotive and human feel. Some key features include:

* Greater accuracy with whispering
* The ability to create audible sighs, laughs, or cries
* Greatly improved detection of tone and emotion
* Accurately follows the input speaking cadence
* Language/accent retention

<AccordionGroup>
  <Accordion title="Watch a video of voice changer in action">
    <iframe width="100%" height="400" src="https://www.youtube.com/embed/GBdOQClluIA" title="YouTube video player" frameborder="0" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen />
  </Accordion>
</AccordionGroup>


## Guide

<Frame background="subtle">
  ![Voice changer demo](file:cfdc0e6a-d730-4b99-ae63-0937a3cbe168)
</Frame>

Audio can be uploaded either directly with an audio file, or spoken live through a microphone. The audio file must be less than **50mb in size**, and either the audio file or your live recording cannot exceed **5 minutes in length**.

If you have material longer than 5 minutes, we recommend breaking it up into smaller sections and generating them separately. Additionally, if your file size is too large, you may need to compress/convert it to an mp3.

### Existing audio file

To upload an existing audio file, either click the audio box, or drag and drop your audio file directly onto it.

### Record live

Press the **Record Audio** button in the audio box, and then once you are ready to begin recording, press the **Microphone** button to start. After you're finished recording, press the **Stop** button.

You will then see the audio file of this recording, which you can then playback to listen to - this is helpful to determine if you are happy with your performance/recording. The character cost will be displayed on the bottom-left corner, and you will not be charged this quota for recording anything - only when you press "Generate".

**The cost for a voice changer generation is solely duration-based at 1000 characters per minute.**


## Settings

<Frame background="subtle">
  ![Voice changer settings](file:592d891e-7c5f-4cb6-bc10-f61083018acc)
</Frame>

Learn more about the different voice settings [here](/docs/product-guides/playground/text-to-speech#settings).

<Info>
  Voice changer adds an additional setting to automaticaly remove background noise from your
  recording.
</Info>


## Support languages

`eleven_english_sts_v2`

Our multilingual v2 models support 29 languages:

*English (USA, UK, Australia, Canada), Japanese, Chinese, German, Hindi, French (France, Canada), Korean, Portuguese (Brazil, Portugal), Italian, Spanish (Spain, Mexico), Indonesian, Dutch, Turkish, Filipino, Polish, Swedish, Bulgarian, Romanian, Arabic (Saudi Arabia, UAE), Czech, Greek, Finnish, Croatian, Malay, Slovak, Danish, Tamil, Ukrainian & Russian.*

The `eleven_english_sts_v2` model only supports English.

[Learn more about models](/docs/models)


## Best practices

Voice changer excels at **preserving accents** and **natural speech cadences** across various output voices. For instance, if you upload an audio sample with a Portuguese accent, the output will retain that language and accent. The input sample is crucial, as it determines the output characteristics. If you select a British voice like "George" but record with an American accent, the result will be George's voice with an American accent.

* **Expression**: Be expressive in your recordings. Whether shouting, crying, or laughing, the voice changer will accurately replicate your performance. This tool is designed to enhance AI realism, allowing for creative expression.
* **Microphone gain**: Ensure the input gain is appropriate. A quiet recording may hinder AI recognition, while a loud one could cause audio clipping.
* **Background Noise**: Turn on the **Remove Background Noise** option to automatically remove background noise from your recording.



# Sound effects

> How to create high-quality sound effects from text with ElevenLabs.

<img src="file:e765a10a-475d-43c9-8355-cb90b7e0c8e2" alt="Sound effects product feature" />


## Overview

**Sound effects** enhance the realism and immersion of your audio projects. With ElevenLabs, you can generate sound effects from text and integrate them into your voiceovers and projects.


## Guide

<Steps>
  <Step title="Navigate to Sound Effects">
    Head over to [Sound Effects](https://elevenlabs.io/app/sound-effects). You can find it under
    **Playground** in the sidebar.
  </Step>

  <Step title="Describe the sound effect">
    In the text box, type a description of the sound effect you want (e.g., "person walking on
    grass").
  </Step>

  <Step title="Adjust settings">
    <Frame background="subtle">
      ![Sound effects
      settings](file:4daa4bdf-757e-474f-9b13-3b470024573c)
    </Frame>

    <ul>
      <li>
        Set the duration for the sound, or choose auto to let the AI decide. The maximum length is
        30 seconds.
      </li>

      <li>
        Turn <strong>Looping</strong> on to create a seamless loop. The ending will blend into the
        beginning without a noticeable gap.
      </li>

      <li>
        Adjust the prompt influence setting to control how closely the output should match the
        prompt. By default, this is set to 30%.
      </li>
    </ul>
  </Step>

  <Step title="Generate sound">
    Click the arrow to generate. Four sound effects will be created each time.
  </Step>

  <Step title="Review and regenerate">
    Go to your **History** tab to access the generated sound effects. Click the **download** icon
    and choose MP3 (44.1kHz) or WAV (48kHz). You can also click the **star** icon to save to your
    favorites, so you can access it again from your **Favorites** tab. If needed, adjust the prompt
    or settings and regenerate.
  </Step>
</Steps>

<Success>
  **Exercise**: Create a sound effect using the following prompt: Old-school funky brass stabs from
  a vinyl sample, stem, 88 bpm in F# minor.
</Success>


## Explore the library

<Frame background="subtle">
  ![Sound effects explore](file:075db1e7-1daf-494f-a391-4e20e6c64023)
</Frame>

Browse community-made sound effects in the **Explore** tab.

For more on prompting and how sound effects work, visit our [overview page](/docs/capabilities/sound-effects).



# Speech to Text

> A guide on how to transcribe audio with ElevenLabs

<img src="file:11b3ddcc-3f3a-4101-8887-1ee1ab0b2fba" alt="Text to Speech product feature" />


## Overview

With speech to text, you can transcribe spoken audio into text with state of the art accuracy. With automatic language detection, you can transcribe audio in a multitude of languages.


## Creating a transcript

<Steps>
  <Step title="Upload audio">
    In the ElevenLabs dashboard, navigate to the Speech to Text page and click the "Transcribe files" button. From the modal, you can upload an audio or video file to transcribe.

    <Frame background="subtle">
      ![Speech to Text upload](file:ce62d86a-a9f0-45fc-8133-272de0a6777b)
    </Frame>
  </Step>

  <Step title="Select options">
    Select the primary language of the audio and the maximum number of speakers. If you don't know either, you can leave the defaults which will attempt to detect the language and number of speakers automatically.

    Finally choose whether you wish to tag audio events like laughter or applause, then click the "Transcribe" button.
  </Step>

  <Step title="View results">
    Click on the name of the audio file you uploaded in the center pane to view the results. You can click on a word to start a playback of the audio at that point.

    Click the "Export" button in the top right to download the results in a variety of formats.
  </Step>
</Steps>


## Transcript Editor

Once you've created a transcript, you can edit it in our Transcript Editor. Learn more about it [in this guide](/docs/product-guides/products/transcripts).


## FAQ

<AccordionGroup>
  <Accordion title="What languages are supported?">
    ### Supported languages

    The Scribe v1 model supports 99 languages, including:

    *Afrikaans (afr), Amharic (amh), Arabic (ara), Armenian (hye), Assamese (asm), Asturian (ast), Azerbaijani (aze), Belarusian (bel), Bengali (ben), Bosnian (bos), Bulgarian (bul), Burmese (mya), Cantonese (yue), Catalan (cat), Cebuano (ceb), Chichewa (nya), Croatian (hrv), Czech (ces), Danish (dan), Dutch (nld), English (eng), Estonian (est), Filipino (fil), Finnish (fin), French (fra), Fulah (ful), Galician (glg), Ganda (lug), Georgian (kat), German (deu), Greek (ell), Gujarati (guj), Hausa (hau), Hebrew (heb), Hindi (hin), Hungarian (hun), Icelandic (isl), Igbo (ibo), Indonesian (ind), Irish (gle), Italian (ita), Japanese (jpn), Javanese (jav), Kabuverdianu (kea), Kannada (kan), Kazakh (kaz), Khmer (khm), Korean (kor), Kurdish (kur), Kyrgyz (kir), Lao (lao), Latvian (lav), Lingala (lin), Lithuanian (lit), Luo (luo), Luxembourgish (ltz), Macedonian (mkd), Malay (msa), Malayalam (mal), Maltese (mlt), Mandarin Chinese (zho), Māori (mri), Marathi (mar), Mongolian (mon), Nepali (nep), Northern Sotho (nso), Norwegian (nor), Occitan (oci), Odia (ori), Pashto (pus), Persian (fas), Polish (pol), Portuguese (por), Punjabi (pan), Romanian (ron), Russian (rus), Serbian (srp), Shona (sna), Sindhi (snd), Slovak (slk), Slovenian (slv), Somali (som), Spanish (spa), Swahili (swa), Swedish (swe), Tamil (tam), Tajik (tgk), Telugu (tel), Thai (tha), Turkish (tur), Ukrainian (ukr), Umbundu (umb), Urdu (urd), Uzbek (uzb), Vietnamese (vie), Welsh (cym), Wolof (wol), Xhosa (xho) and Zulu (zul).*
  </Accordion>

  <Accordion title="Can I upload video files?">
    Yes, the tool supports uploading both audio and video files. The maximum file size for either is 3GB.
  </Accordion>

  <Accordion title="Can I rename speakers?">
    ### Renaming speakers

    Yes, you can rename speakers by clicking the "edit" button next to the "Speakers" label.
  </Accordion>
</AccordionGroup>



---
**Navigation:** [← Previous](./06-cross-platform-voice-agents-with-expo-react-native.md) | [Index](./index.md) | [Next →](./08-image-video.md)
