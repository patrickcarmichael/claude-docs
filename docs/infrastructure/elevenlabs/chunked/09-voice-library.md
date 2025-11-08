**Navigation:** [← Previous](./08-image-video.md) | [Index](./index.md) | [Next →](./10-consolidated-billing.md)

# Voice Library

> A guide on how to use voices from the Voice Library.

<img src="file:957709e8-fa4b-4be6-bd0e-bd7418699f06" alt="Voice Library" />


## Overview

The [Voice Library](https://elevenlabs.io/app/voice-library) is a marketplace where our community can share Professional Voice Clones and earn rewards when others use them. Currently, only Professional Voice Clones can be shared. Instant Voice Clones and voices created with Voice Design are not shareable.

To access the Voice Library, click **Voices** in the sidebar and select **Explore**.

### Finding voices

You can browse the Voice Library in several ways:

#### Handpicked Collections

Our Handpicked Collections highlight top voices across use cases, genres, and languages. These collections are updated regularly to include new standout voices.

#### Search

Use the search bar to find voices by name, keyword, or voice ID. You can also search by uploading or dragging and dropping an audio file. This will help you find the original voice, if available, along with similar voices.

#### Sort options

You can sort voices by:

* Trending: voices ranked by popularity
* Latest: newly added voices
* Most users
* Character usage

#### Filters

Use filters to refine your search:

<AccordionGroup>
  <Accordion title="Language">
    ##### Language

    The language filter returns voices that have been trained on a specific language. While all voices can be used with any supported language, voices tagged with a specific language will perform best in that language. Some voices have been assessed as performing well in multiple languages, and these voices will also be returned when you search for a specific language.
  </Accordion>

  <Accordion title="Accent">
    ##### Accent

    When you select a language, the Accent filter will also become available, allowing you to filter for specific accents.
  </Accordion>

  <Accordion title="Category">
    ##### Category

    Filter voices by their suggested use case:

    * Narrative & Story
    * Conversational
    * Characters & Animation
    * Social Media
    * Entertainment & TV
    * Advertisement
    * Informative & Educational
  </Accordion>

  <Accordion title="Gender">
    ##### Gender

    * Male
    * Female
    * Neutral
  </Accordion>

  <Accordion title="Age">
    ##### Age

    * Young
    * Middle Aged
    * Old
  </Accordion>

  <Accordion title="Notice period">
    ##### Notice period

    Some voices have a notice period. This is how long you'll continue to have access to the voice if the voice owner decides to remove it from the Voice Library. If the voice's owner stops sharing their voice, you'll receive advance notice through email and in-app notifications. These notifications specify when the voice will become unavailable and recommend similar voices from the Voice Library. If the owner of a voice without a notice period decides to stop sharing their voice, you'll lose access to the voice immediately.

    This filter allows you to only return voices that have a notice period, and search for voices with a specific notice period. The maximum notice period is 2 years.
  </Accordion>

  <Accordion title="Live Moderation enabled">
    ##### Live Moderation enabled

    Some voices have Live Moderation enabled. This is indicated with a label with a shield icon. When you generate using a voice with Live Moderation enabled, we use tools to check whether the text being generated belongs to a number of prohibited categories. This may introduce extra latency when using the voice.

    This filter allows you to exclude voices that have Live Moderation enabled.
  </Accordion>

  <Accordion title="Quality">
    ##### Quality

    Filter voices by their quality level:

    * **Any**: All voices regardless of quality assessment
    * **High-Quality**: Voices that have been recorded with proper equipment, mixed well, and tested to be free from most audio problems such as reverb/echo, distortion, or other artifacts. These voices exhibit an overall professional-sounding tone and are reviewed by our QA testers.
  </Accordion>
</AccordionGroup>

### Using voices from the Voice Library

To use a voice from the Voice Library, you'll need to add it to My Voices. To do this, click the **+** button.

A pop-up will appear which will give you more information about the voice. You can choose to add the voice to an existing personal collection, create a new collection, or add the voice to My Voices without including it in a collection. To confirm, click **Add voice**. This will save it to My Voices using the default name for the voice.

Voices you've added to My Voices will become available for selection in all voice selection menus. You can also use a voice directly from My Voices by clicking the **T** button, which will open Text to Speech with the voice selected.

### My Voices

You can find all the voices you've created yourself, as well as voices you've saved from the Voice Library, in **My Voices**.

You will see the following information about each voice:

* the language it was trained on.
* the category, for example, "Narrative & Story".
* how long the notice period is, if the voice has one.

The voice type is indicated by an icon:

* Yellow tick: Professional Voice Clone.
* Black tick: High Quality Professional Voice Clone.
* Lightning icon: Instant Voice Clone.
* || icon: ElevenLabs Default voice.
* No icon: voice created with Voice Design.

#### More actions

Click **More actions** (three dots) to:

* Copy voice ID: copies the voice ID to your clipboard.
* Edit voice: allows you to change the name and description of the voice. These changes are only visible to you.
* Share voice: generates a link which you can share with others. When they use the link, the voice will be added to My Voices for their account.
* View history: view your previous Text to Speech generations using this voice.
* Delete voice: deleting voices is permanent and you will be asked to confirm the deletion.

#### Collections

To help organize voices you've saved, you can create your own collections and add voices to them.

To create a new collection, click **Collections** and select **Create collection**. Give your new collection a name, and choose from the available icons.

To add individual voices to a collection, click **More actions** (three dots) and select **Add to collection**. You can choose to add the voice to an existing collection, or create a new one.

#### Select multiple voices

You can **Shift + Click** to select multiple voices at once.

#### Drag and drop voices

Both individual voices and multiple voice selections can also be dragged **Collections** and added to an existing collection, or deleted by dragging to the **trash can** icon.

### Sharing a Professional Voice Clone:

<Steps>
  <Step>
    In [My Voices](https://elevenlabs.io/app/voice-lab) find your voice and click **More actions**
    (three dots), then select **Share voice**.
  </Step>

  <Step>
    In the pop-up, enable the 

    **Sharing**

     toggle.
  </Step>

  <Step>
    For private sharing, copy the sharing link. This will allow other users to save your voice to their account.

    You can restrict access to specific users by adding emails to the **Allowlist**. If this is left blank, all users with the link will be able to access your voice.
  </Step>

  <Step>
    To share publicly, enable **Publish to the Voice Library**. This doesn’t make your voice automatically discoverable.

    <Frame background="subtle">
      ![Voice sharing overview](file:bd6fc7c7-69e5-44bc-becc-89bc97ff8477)
    </Frame>
  </Step>

  <Step>
    Before proceeding with the sharing process, you'll have a number of options including setting a notice period and enabling Live Moderation. Please see the [Voice Library Addendum](https://elevenlabs.io/vla) to our [Terms of Service](https://elevenlabs.io/terms) for more information about these options.

    You also have the option to select a custom voice preview. Any generations you've made of 70-150 characters will be available to select. If you don't see any options in the selection menu, there are no eligible generations available.

    <Frame background="subtle">
      ![Voice sharing options](file:6f239e12-62cc-459f-9dfc-c673e95f91bb)
    </Frame>
  </Step>

  <Step>
    Enter a name and description for your voice.
    Make sure the name you give your voice follows our **naming guidelines**:

    <Accordion title="Naming guidelines">
      #### Naming guidelines

      * The naming pattern should be a one-word name followed by a 2-4 word description, separated by a hyphen (-).

      * Your name should NOT include the following:

        * Names of public individuals or entities (company names, band names, influencers or famous people, etc).
        * Social handles (Twitter, Instagram, you name it, etc).
        * ALL CAPS WORDS.
        * Emojis and any other non-letter characters.
        * Explicit or harmful words.
        * The word “voice”.

      * Some examples of names following our guidelines:
        * Anna - calm and kind
        * Robert - friendly grandpa
        * Steve - wise teacher
        * Harmony - soothing serenader
        * Jasper - jovial storyteller
        * Maya - confident narrator
    </Accordion>
  </Step>

  <Step>
    Set labels (language, accent, gender, age, use case, tone, and style) to help others find your
    voice.
  </Step>

  <Step>
    Review and accept the [Voice Library Addendum](https://elevenlabs.io/terms#VLA) to our [Terms of
    Service](https://elevenlabs.io/terms) and provide the required consents and confirmations. Please
    do this carefully and ensure you fully understand our service before sharing. If you have any
    questions at this stage, you can reach out to us at [legal@elevenlabs.io](mailto:legal@elevenlabs.io).
  </Step>

  <Step>
    After submission, your voice will be reviewed by our team. If minor adjustments are needed, we may make these for you. Your request to share your voice may be declined if it doesn't meet our guidelines, and repeated uploads that consistently violate our guidelines may lead to restrictions on uploading and sharing voices.

    We currently do not have an estimate for the review time, as it depends on the queue.
  </Step>
</Steps>



# Voice Cloning

> Learn how to clone your voice to using our best-in-class models.


## Overview

When cloning a voice, there are two main options: Instant Voice Cloning (IVC) and Professional Voice Cloning (PVC). IVC is a quick and easy way to clone your voice, while PVC is a more accurate and customizable option.


## Instant Voice Cloning

<Frame background="subtle">
  ![Instant voice
  cloning](file:0e0b0147-6d62-494e-96f8-8b5d64a8ee8f)
</Frame>

IVC allows you to create voice clones from shorter samples near instantaneously. Creating an instant voice clone does not train or create a custom AI model. Instead, it relies on prior knowledge from training data to make an educated guess rather than training on the exact voice. This works extremely well for a lot of voices.

However, the biggest limitation of IVC is if you are trying to clone a very unique voice with a very unique accent where the AI might not have heard a similar voices before during training. In such cases, creating a custom model with explicit training using PVC might be the best option.


## Professional Voice Cloning

<Frame background="subtle">
  ![Professional voice
  cloning](file:1b0eb16b-665f-40fb-ae88-07457e7e3ab2)
</Frame>

A PVC is a special feature that is available to our Creator+ plans. PVC allows you to train a hyper-realistic model of a voice. This is achieved by training a dedicated model on a large set of voice data to produce a model that’s indistinguishable from the original voice.

Since the custom models require fine-tuning and training, it will take a bit longer to train these PVCs compared to an IVC. Giving an estimate is challenging as it depends on the number of people in the queue before you and a few other factors.

Here are the current estimates for PVC:

* **English:** \~3 hours
* **Multilingual:** \~6 hours


## Beginner's guide to audio recording

If you're new to audio recording, here are some tips to help you get started.

### Recording location

When recording audio, choose a suitable location and set up to minimize room echo/reverb.
So, we want to "deaden" the room as much as possible. This is precisely what a vocal booth that is acoustically treated made for, and if you do not have a vocal booth readily available, you can experiment with some ideas for a DIY vocal booth, “blanket fort”, or closet.

Here are a few YouTube examples of DIY acoustics ideas:

* [I made a vocal booth for \$0.00!](https://www.youtube.com/watch?v=j4wJMDUuHSM)
* [How to Record GOOD Vocals in a BAD Room](https://www.youtube.com/watch?v=TsxdHtu-OpU)
* [The 5 BEST Vocal Home Recording TIPS!](https://www.youtube.com/watch?v=K96mw2QBz34)

### Microphone, pop-filter, and audio interface

A good microphone is crucial. Microphones can range from \$100 to \$10,000, but a professional XLR microphone costing \$150 to \$300 is sufficient for most voiceover work.

For an affordable yet high-quality setup for voiceover work, consider a **Focusrite** interface paired with an **Audio-Technica AT2020** or **Rode NT1 microphone**. This setup, costing between \$300 to \$500, offers high-quality recording suitable for professional use, with minimal self-noise for clean results.

Please ensure that you have a proper **pop-filter** in front of the microphone when recording to avoid plosives as well as breaths and air hitting the diaphragm/microphone directly, as it will sound poor and will also cause issues with the cloning process.

### Digital Audio Workstation (DAW)

There are many different recording solutions out there that all accomplish the same thing: recording audio. However, they are not all created equally. As long as they can record WAV files at 44.1kHz or 48kHz with a bitrate of at least 24 bits, they should be fine. You don't need any fancy post-processing, plugins, denoisers, or anything because we want to keep audio recording simple.

If you want a recommendation, we would suggest something like **REAPER**, which is a fantastic DAW with a tremendous amount of flexibility. It is the industry standard for a lot of audio work. Another good free option is **Audacity**.

Maintain optimal recording levels (not too loud or too quiet) to avoid digital distortion and excessive noise. Aim for peaks of -6 dB to -3 dB and an average loudness of -18 dB for voiceover work, ensuring clarity while minimizing the noise floor. Monitor closely and adjust levels as needed for the best results based on the project and recording environment.

### Positioning

One helpful guideline to follow is to maintain a distance of about two fists away from the microphone, which is approximately 20cm (7-8 in), with a pop filter placed between you and the microphone. Some people prefer to position the pop filter all the way back so that they can press it up right against it. This helps them maintain a consistent distance from the microphone more easily.

Another common technique to avoid directly breathing into the microphone or causing plosive sounds is to speak at an angle. Speaking at an angle ensures that exhaled air is less likely to hit the microphone directly and, instead, passes by it.

### Performance

The performance you give is one of the most crucial aspects of this entire recording session. The AI will try to clone everything about your voice to the best of its ability, which is very high. This means that it will attempt to replicate your cadence, tonality, performance style, the length of your pauses, whether you stutter, take deep breaths, sound breathy, or use a lot of "uhms" and "ahs" – it can even replicate those. Therefore, what we want in the audio file is precisely the performance and voice that we want to clone, nothing less and nothing more. That is also why it's quite important to find a script that you can read that fits the tonality we are aiming for.

When recording for AI, it is very important to be consistent. if you are recording a voice either keep it very animated throughout or keep it very subdued throughout you can't mix and match or the AI can become unstable because it doesn't know what part of the voice to clone. same if you're doing an accent keep the same accent throughout the recording. Consistency is key to a proper clone!



# Instant Voice Cloning

> Learn how to clone your voice instantly using our best-in-class models.

<img src="file:5d7b822b-fa15-49aa-8e08-5e20b5a947d2" alt="Voice cloning product feature" />


## Creating an Instant Voice Clone

When cloning a voice, it's important to consider what the AI has been trained on: which languages and what type of dataset. You can find more information about which languages each model has been trained on in our [help center](https://help.elevenlabs.io/hc/en-us/articles/17883183930129-What-models-do-you-offer-and-what-is-the-difference-between-them).

<Info>
  Read more about each individual model and their strengths in the [Models page](/docs/models)).
</Info>


## Guide

<Warning>
  If you are unsure about what is permissible from a legal standpoint, please consult the [Terms of
  Service](https://elevenlabs.io/terms-of-use) and our [AI Safety
  information](https://elevenlabs.io/safety) for more information.
</Warning>

<Steps>
  ### Navigate to the Instant Voice Cloning page

  In the ElevenLabs dashboard, select the "Voices" section on the left, then click "Add a new voice".

  From the modal, select "Instant Voice Clone".

  ### Upload or record your audio

  Follow the on-screen instructions to upload or record your audio.

  ### Confirm voice details

  <img src="file:149c6fc0-20e5-4464-8e80-fd86301b2f51" alt="Voice cloning IVC modal" />

  Name and label your voice clone, confirm that you have the right and consent to clone the voice, then click "Save voice".

  ### Use your voice clone

  Under the "Voices" section in the dashboard, select the "Personal" tab, then click on your voice clone to begin using it.
</Steps>


## Best practices

<AccordionGroup>
  <Accordion title="Record at least 1 minute of audio">
    #### Record at least 1 minute of audio

    Avoid recording more than 3 minutes, this will yield little improvement and can, in some cases, even be detrimental to the clone.

    How the audio was recorded is more important than the total length (total runtime) of the samples. The number of samples you use doesn't matter; it is the total combined length (total runtime) that is the important part.

    Approximately 1-2 minutes of clear audio without any reverb, artifacts, or background noise of any kind is recommended. When we speak of "audio or recording quality," we do not mean the codec, such as MP3 or WAV; we mean how the audio was captured. However, regarding audio codecs, using MP3 at 128 kbps and above is advised. Higher bitrates don't have a significant impact on the quality of the clone.
  </Accordion>

  <Accordion title="Keep the audio consistent">
    #### Keep the audio consistent

    The AI will attempt to mimic everything it hears in the audio. This includes the speed of the person talking, the inflections, the accent, tonality, breathing pattern and strength, as well as noise and mouth clicks. Even noise and artefacts which can confuse it are factored in.

    Ensure that the voice maintains a consistent tone throughout, with a consistent performance. Also, make sure that the audio quality of the voice remains consistent across all the samples. Even if you only use a single sample, ensure that it remains consistent throughout the full sample. Feeding the AI audio that is very dynamic, meaning wide fluctuations in pitch and volume, will yield less predictable results.
  </Accordion>

  <Accordion title="Replicate your performance">
    #### Replicate your performance

    Another important thing to keep in mind is that the AI will try to replicate the performance of the voice you provide. If you talk in a slow, monotone voice without much emotion, that is what the AI will mimic. On the other hand, if you talk quickly with much emotion, that is what the AI will try to replicate.

    It is crucial that the voice remains consistent throughout all the samples, not only in tone but also in performance. If there is too much variance, it might confuse the AI, leading to more varied output between generations.
  </Accordion>

  <Accordion title="Find a good balance for the volume">
    #### Find a good balance for the volume

    Find a good balance for the volume so the audio is neither too quiet nor too loud. The ideal would be between -23 dB and -18 dB RMS with a true peak of -3 dB.
  </Accordion>
</AccordionGroup>



# Professional Voice Cloning

> Learn how to clone your voice professionally using our best-in-class models.


## Creating a Professional Voice Clone

When cloning a voice, it's important to consider what the AI has been trained on: which languages and what type of dataset. You can find more information about which languages each model has been trained on in our [help center](https://help.elevenlabs.io/hc/en-us/articles/17883183930129-What-models-do-you-offer-and-what-is-the-difference-between-them).

<Info>
  Read more about each individual model and their strengths in the [Models page](/docs/models)).
</Info>


## Guide

<Warning>
  If you are unsure about what is permissible from a legal standpoint, please consult the [Terms of
  Service](https://elevenlabs.io/terms-of-use) and our [AI Safety
  information](https://elevenlabs.io/safety) for more information.
</Warning>

<Steps>
  ### Navigate to the Professional Voice Cloning page

  In the ElevenLabs dashboard, select the **Voices** section on the left, then click **Add a new voice**.

  From the pop-up, select **Professional Voice Clone**.

  ### Upload your audio

  <Frame background="subtle">
    ![Create a new Professional Voice Clone](file:235c525b-d134-4430-8ebf-dc7800f62b78)
  </Frame>

  Upload your audio samples by clicking **Upload samples**.

  If you don't already have pre-recorded training audio, you can also record directly into the interface by selecting **Record yourself**. We've included sample scripts for narrative, conversational and advertising purposes. You can also upload your own script.

  ### Check the feedback on sample length

  Once your audio has been uploaded, you will see feedback on the length of your samples. For the best results, we recommend uploading at least an hour of training audio, and ideally as close to three hours as possible.

  <Frame background="subtle">
    ![Create a new Professional Voice Clone](file:21c744cd-6996-454d-bed1-07aeef0bb7d1)
  </Frame>

  ### Process your audio

  Once your audio samples have been uploaded, you can process them to improve the quality. You can remove any background noise, and you can also separate out different speakers, if your audio includes more than one speaker. To access these options, click the **Audio settings** button next to the clip you want to process.

  <Frame background="subtle">
    ![Create a new Professional Voice Clone](file:f534cd25-f763-4ee9-98e9-a250dc2cb8c0)
  </Frame>

  ### Verify your voice

  Once everything is recorded and uploaded, you will be asked to verify your voice. To ensure a smooth experience, please try to verify your voice using the same or similar equipment used to record the samples and in a tone and delivery that is similar to those present in the samples. If you do not have access to the same equipment, try verifying the best you can. If it fails, you can either wait 24 hours to try verification again, or reach out to support for help.

  ### Wait for your voice to complete fine tuning

  Before you can use your voice, it needs to complete the fine tuning process. You can check the status of your voice in My Voices while it's processing. You'll be notified when it's ready to use.

  ### Use your voice clone

  Under the **Voices** section in the dashboard, select the **Personal** tab, then click **Use** next to your voice clone to begin using it.
</Steps>

There are a few things to be mindful of before you start uploading your samples, and some steps that you need to take to ensure the best possible results.

<Steps>
  ### Record high quality audio

  Professional Voice Cloning is highly accurate in cloning the samples used for its training. It will create a near-perfect clone of what it hears, including all the intricacies and characteristics of that voice, but also including any artifacts and unwanted audio present in the samples. This means that if you upload low-quality samples with background noise, room reverb/echo, or any other type of unwanted sounds like music or multiple people speaking, the AI will try to replicate all of these elements in the clone as well.

  ### Ensure there's only a single speaking voice

  Make sure there's only a single speaking voice throughout the audio, as more than one speaker or excessive noise or anything of the above can confuse the AI. This confusion can result in the AI being unable to discern which voice to clone or misinterpreting what the voice actually sounds like because it is being masked by other sounds, leading to a less-than-optimal clone.

  ### Provide enough material

  Make sure you have enough material to clone the voice properly. The bare minimum we recommend is 30 minutes of audio, but for the optimal result and the most accurate clone, we recommend closer to 2-3 hours of audio. The more audio provided the better the quality of the resulting clone.

  ### Keep the style consistent

  The speaking style in the samples you provide will be replicated in the output, so depending on what delivery you are looking for, the training data should correspond to that style (e.g. if you are looking to voice an audiobook with a clone of your voice, the audio you submit for training should be a recording of you reading a book in the tone of voice you want to use). It is better to just include one style in the uploaded samples for consistencies sake.

  ### Use samples speaking the language you want the PVC to be used for

  It is best to use samples speaking where you are speaking the language that the PVC will mainly be used for. Of course, the AI can speak any language that we currently support. However, it is worth noting that if the voice itself is not native to the language you want the AI to speak - meaning you cloned a voice speaking a different language - it might have an accent from the original language and might mispronounce words and inflections. For instance, if you clone a voice speaking English and then want it to speak Spanish, it will very likely have an English accent when speaking Spanish. We only support cloning samples recorded in one of our supported languages, and the application will reject your sample if it is recorded in an unsupported language.
</Steps>

See the examples below for what to expect from a good and bad recording.

<iframe width="100%" height={90} frameBorder="no" scrolling="no" src={`https://elevenlabs.io/player/index.html?title=Good%20example&small=true&preview=true&audioSrc=https%3A%2F%2Fstorage.googleapis.com%2Feleven-public-cdn%2Faudio%2Fdocs%2Fgood_example.wav`} />

<iframe width="100%" height={90} frameBorder="no" scrolling="no" src={`https://elevenlabs.io/player/index.html?title=Bad%20example&small=true&preview=true&audioSrc=https%3A%2F%2Fstorage.googleapis.com%2Feleven-public-cdn%2Faudio%2Fdocs%2Fbad_example.wav`} />

For now, we only allow you to clone your own voice. You will be asked to go through a verification process before submitting your fine-tuning request.


## Tips and suggestions

<AccordionGroup>
  <Accordion title="Professional Recording Equipment">
    #### Professional Recording Equipment

    Use high-quality recording equipment for optimal results as the AI will clone everything about the audio. High-quality input = high-quality output. Any microphone will work, but an XLR mic going into a dedicated audio interface would be our recommendation. A few general recommendations on low-end would be something like an Audio Technica AT2020 or a Rode NT1 going into a Focusrite interface or similar.
  </Accordion>

  <Accordion title="Use a Pop-Filter">
    #### Use a Pop-Filter

    Use a Pop-Filter when recording. This will minimize plosives when recording.
  </Accordion>

  <Accordion title="Microphone Distance">
    #### Microphone Distance

    Position yourself at the right distance from the microphone - approximately two fists away from the mic is recommended, but it also depends on what type of recording you want.
  </Accordion>

  <Accordion title="Noise-Free Recording">
    #### Noise-Free Recording

    Ensure that the audio input doesn't have any interference, like background music or noise. The AI cloning works best with clean, uncluttered audio.
  </Accordion>

  <Accordion title="Room Acoustics">
    #### Room Acoustics

    Preferably, record in an acoustically-treated room. This reduces unwanted echoes and background noises, leading to clearer audio input for the AI. You can make something temporary using a thick duvet or quilt to dampen the recording space.
  </Accordion>

  <Accordion title="Audio Pre-processing">
    #### Audio Pre-processing

    Consider editing your audio beforehand if you're aiming for a specific sound you want the AI to output. For instance, if you want a polished podcast-like output, pre-process your audio to match that quality, or if you have long pauses or many "uhm"s and "ahm"s between words as the AI will mimic those as well.
  </Accordion>

  <Accordion title="Volume Control">
    #### Volume Control

    Maintain a consistent volume that's loud enough to be clear but not so loud that it causes distortion. The goal is to achieve a balanced and steady audio level. The ideal would be between -23dB and -18dB RMS with a true peak of -3dB.
  </Accordion>

  <Accordion title="Sufficient Audio Length">
    #### Sufficient Audio Length

    Provide at least 30 minutes of high-quality audio that follows the above guidelines for best results - preferably closer to 2+ hours of audio. The more quality data you can feed into the AI, the better the voice clone will be. The number of samples is irrelevant; the total runtime is what matters. However, if you plan to upload multiple hours of audio, it is better to split it into multiple \~30-minute samples. This makes it easier to upload.
  </Accordion>
</AccordionGroup>



# Voice design

> A guide on how to craft voices from a text prompt.

<img src="file:e5ee44be-e2af-4a88-b7e5-ed18e04284ca" alt="Voice design" />


## Overview

Voice Design helps creators fill the gaps when the exact voice they are looking for isn't available in the [Voice Library](https://elevenlabs.io/app/voice-library). If you can't find a suitable voice for your project, you can create one. Note that Voice Design is highly experimental and [Professional Voice Clones (PVC)](/docs/product-guides/voices/voice-cloning) are currently the highest quality voices on our platform. If there is a PVC available in our library that fits your needs, we recommend using it instead.

You can find Voice Design by heading to Voices -> My Voices -> Add a new voice -> Voice Design in the [ElevenLabs app](https://elevenlabs.io/app/voice-lab?create=true\&creationType=voiceDesign) or via the [API](/docs/api-reference/text-to-voice).

When you hit generate, we'll generate three voice options for you. The only charge for using voice design is the number of credits to generate your preview text, which you are only charged once even though we are generating three samples for you. You can see the number of characters that will be deducted in the "Text to preview" text box.

After generating, you'll have the option to select and save one of the generations, which will take up one of your voice slots.

<CardGroup>
  <Card title="API reference" href="/docs/api-reference/text-to-voice">
    See the API reference for Voice Design
  </Card>

  <Card title="Example app" href="https://github.com/elevenlabs/elevenlabs-examples/tree/main/examples/text-to-voice/x-to-voice">
    A Next.js example app for Voice Design
  </Card>
</CardGroup>


## Prompting guide

The prompt is the foundation of your voice. It tells the model what kind of voice you’re trying to create — everything from the accent and character-type to the gender and vibe of the voice. A well-crafted prompt can be the difference between a generic voice and one that truly fits your vision. In general, more descriptive and granular prompts tend to yield more accurate and nuanced results. The more detail you provide — including age, gender, tone, accent, pacing, emotion, style, and more - the better the model can interpret and deliver a voice that feels intentional and tailored.

However, sometimes short and simple prompts can also work, especially when you're aiming for a more neutral or broadly usable voice. For example, “A calm male narrator” might give you exactly what you need without going into detail — particularly if you're not trying to create a very specific character or style. The right level of detail depends on your use case. Are you building a fantasy character? A virtual assistant? A tired New Yorker in her 60s with a dry sense of humor? The more clearly you define it in your prompt, the closer the output will be to what you're imagining.

### Audio Quality

Audio quality refers to the clarity, cleanliness, and overall fidelity of the generated voice. By default, ElevenLabs aims to produce clean and natural-sounding audio — but if your project requires a specific level of quality, it's best to explicitly include it in your prompt.

For high-quality results, you can help the model by adding a phrase such as “**perfect audio quality**” or “**studio-quality recording**” to your voice description. This helps ensure the voice is rendered with maximum clarity, minimal distortion, and a polished finish.

<Warning>
  Including these types of phrases can sometimes reduce the accuracy of the prompt in general if the
  voice is very specific or niche.
</Warning>

There may also be creative cases where lower audio quality is intentional, such as when simulating a phone call, old radio broadcast, or found footage. In those situations, either leave out quality descriptors entirely or explicitly include phrases like:

* “Low-fidelity audio”
* “Poor audio quality”
* “Sounds like a voicemail”
* “Muffled and distant, like on an old tape recorder”

The placement of this phrase in your prompt is flexible — it can appear at the beginning or end, though we’ve found it works well at either.

### Age, Tone/Timbre and Gender

These three characteristics are the foundation of voice design, shaping the overall identity and emotional resonance of the voice. The more detail you provide, the easier it is for the AI to produce a voice that fits your creative vision — whether you're building a believable character, crafting a compelling narrator, or designing a virtual assistant.

#### Age

Describing the perceived age of the voice helps define its maturity, vocal texture, and energy. Use specific terms to guide the AI toward the right vocal quality.

**Useful descriptors:**

* “Adolscent male” / “adolescent female”
* “Young adult” / “in their 20s” / “early 30s”
* “Middle-aged man” / “woman in her 40s”
* “Elderly man” / “older woman” / “man in his 80s”

#### Tone/Timbre

Refers to the physical quality of the voice, shaped by pitch, resonance, and vocal texture. It’s distinct from emotional delivery or attitude.

**Common tone/timbre descriptors:**

* “Deep” / “low-pitched”
* “Smooth” / “rich”
* “Gravelly” / “raspy”
* “Nasally” / “shrill”
* “Airy” / “breathy”
* “Booming” / “resonant”
* “Light” / “thin”
* “Warm” / “mellow”
* “Tinny” / “metallic”

#### Gender

Gender often typically influences pitch, vocal weight, and tonal presence — but you can push beyond simple categories by describing the sound instead of the identity.

**Examples:**

* “A lower-pitched, husky female voice”
* “A masculine male voice, deep and resonant”
* “A neutral gender — soft and mid-pitched”

#### Accent

Accent plays a critical role in defining a voice’s regional, cultural, and emotional identity. If your project depends on an authentic sound — whether it's grounded in realism or stylized for character — being clear and deliberate about the desired accent is essential.

Phrase choice matters - certain terms tend to produce more consistent results. For example, “thick” often yields better results than “strong” when describing how prominent an accent should be. There is lots of trial and error to be had, and we encourage you to experiment with the wording and to be as creative and descriptive as possible.

* **Examples of clear accent prompts:**
  * “A middle-aged man with a thick French accent”
  * “A young woman with a slight Southern drawl”
  * “An old man with a heavy Eastern European accent”
  * “A cheerful woman speaking with a crisp British accent”
  * “A younger male with a soft Irish lilt”
  * “An authoritative voice with a neutral American accent”
  * “A man with a regional Australian accent, laid-back and nasal”

Avoid overly vague descriptors like “foreign” or “exotic” — they’re imprecise and can produce inconsistent results.

Combine accent with other traits like tone, age, or pacing for better control. E.g., “A sarcastic old woman with a thick New York accent, speaking slowly.”

For fantasy or fictional voices, you can suggest real-world accents as inspiration:

* “An elf with a proper thick British accent. He is regal and lyrical.”
* “A goblin with a raspy Eastern European accent.”

### Pacing

Pacing refers to the speed and rhythm at which a voice speaks. It's a key component in shaping the personality, emotional tone, and clarity of the voice. Being explicit about pacing is essential, especially when designing voices for specific use cases like storytelling, advertising, character dialogue, or instructional content.

Use clear language to describe how fast or slow the voice should speak. You can also describe how the pacing feels — whether it's steady, erratic, deliberate, or breezy. If the pacing shifts, be sure to indicate where and why.

**Examples of pacing descriptors:**

* “Speaking quickly” / “at a fast pace”
* “At a normal pace” / “speaking normally”
* “Speaking slowly” / “with a slow rhythm”
* “Deliberate and measured pacing”
* “Drawn out, as if savoring each word”
* “With a hurried cadence, like they’re in a rush”
* “Relaxed and conversational pacing”
* “Rhythmic and musical in pace”
* “Erratic pacing, with abrupt pauses and bursts”
* “Even pacing, with consistent timing between words”
* “Staccato delivery”

### Text to preview

Once you've written a strong voice prompt, the text you use to preview that voice plays a crucial role in shaping how it actually sounds. The preview text acts like a performance script — it sets the tone, pacing, and emotional delivery that the voice will attempt to match.

To get the best results, your preview text should complement the voice description, not contradict it. For example, if your prompt describes a “calm and reflective younger female voice with a slight Japanese accent,” using a sentence like “Hey! I can't stand what you’ve done with the darn place!!!” will clash with that intent. The model will try to reconcile that mismatch, often leading to unnatural or inconsistent results.

Instead, use sample text that reflects the voice’s intended personality and emotional tone. For the example above, something like “It’s been quiet lately... I’ve had time to think, and maybe that’s what I needed most.” supports the prompt and helps generate a more natural, coherent voice.

Additionally, we’ve found that longer preview texts tend to produce more stable and expressive results. Short phrases can sometimes sound abrupt or inconsistent, especially when testing subtle qualities like tone or pacing. Giving the model more context — a full sentence or even a short paragraph — allows it to deliver a smoother and more accurate representation of the voice.

### Parameters

#### Loudness

Controls the volume of the Text to Preview generation, and ultimately the voice once saved.

#### Guidance Scale

Dictates how closely the Prompt is adhered to. Higher values will stick to the prompt more strictly, but could result in poorer audio quality if the prompt is very niche, while lower values will allow the model to be more creative at the cost of prompt accuracy. Use a lower value if the performance and audio quality is generally more important than perfectly nailing the prompt. High values are recommended when accent or tone accuracy is of paramount importance.

### Attributes and Examples

<Note>
  Experiment with the way in which these descriptors are written. For example, “Perfect audio
  quality” can also be written as “the audio quality is perfect”. These can sometimes produce
  different results!
</Note>

| Attribute              | Examples                                                                                         |
| ---------------------- | ------------------------------------------------------------------------------------------------ |
| Age                    | Young, younger, adult, old, elderly, in his/her 40s                                              |
| Accent                 | "thick" Scottish accent, "slight" Asian-American accent, Southern American accent                |
| Gender                 | Male, female, gender-neutral, ambiguous gender                                                   |
| Tone/Timbre/pitch      | Deep, warm, gravelly, smooth, shrill, buttery, raspy, nasally, throaty, harsh, robotic, ethereal |
| Pacing                 | Normal cadence, fast-paced, quickly, slowly, drawn out, calm pace, natural/conversational pace   |
| Audio Quality          | Perfect audio quality, audio quality is 'ok', poor audio quality                                 |
| Character / Profession | Pirate, businessman, farmer, politician, therapist, ogre, godlike being, TV announcer            |
| Emotion                | Energetic, excited, sad, emotional, sarcastic, dry                                               |
| Pitch                  | Low-pitched, high-pitched, normal pitch                                                          |

### Example Prompts and Text Previews

| Voice Type                     | Prompt/Description                                                                                                                                                                                                                                                                                     | Text Preview                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Guidance Scale |
| :----------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------- |
| Female Sports Commentator      | A high-energy female sports commentator with a thick British accent, passionately delivering play-by-play coverage of a football match in a very quick pace. Her voice is lively, enthusiastic, and fully immersed in the action.                                                                      | OH MY WORD — WHAT A GOAL! She picks it up just past midfield, dances through TWO defenders like they're not even THERE, and absolutely SMASHES it into the top corner! The goalkeeper had NO CHANCE! That is WORLD-CLASS from the young forward, and the crowd is on their FEET! This match has come ALIVE, and you can FEEL the momentum SHIFTING!                                                                                                                                                                                                      | 25%            |
| Drill Sergeant                 | An army drill sergeant shouting at his team of soldiers. He sounds angry and is speaking at a fast pace.                                                                                                                                                                                               | LISTEN UP, you sorry lot! I didn't come here to babysit — I came to BUILD SOLDIERS! You move when I say move, and you breathe when I say breathe! You've got ten seconds to fall in line or you'll regret it!!                                                                                                                                                                                                                                                                                                                                           | 25%            |
| Evil Ogre                      | A massive evil ogre speaking at a quick pace. He has a silly and resonant tone.                                                                                                                                                                                                                        | "Your weapons are but toothpicks to me. \[laughs] Surrender now and I may grant you a swift end. I've toppled kingdoms and devoured armies. What hope do you have against me?"                                                                                                                                                                                                                                                                                                                                                                           | 30%            |
| Relatable British Entrepreneur | Excellent audio quality. A man in his 30s to early 40s with a thick British accent speaking at a natural pace like he's talking to a friend.                                                                                                                                                           | \[laughs] See, that's the thing. YOU see a company, while I see... \[lip smacks] I see a promise, ya know what I mean? \[exhales] We don't build just to profit, we build to, to UPLIFT! If our technology doesn't leave the world kinder, smarter, and more connected than we found it… \[sighs] then what are we even doing here?                                                                                                                                                                                                                      | 40%            |
| Southern Woman                 | An older woman with a thick Southern accent. She is sweet and sarcastic.                                                                                                                                                                                                                               | "Well sugar, if all we ever do is chase titles and trophies, we're gonna miss the whole darn point. \[light chuckle] I'd rather build somethin' that makes folks' lives easier—and if I can do it in heels with a smile and a touch of sass, even better."                                                                                                                                                                                                                                                                                               | 35%            |
| Movie Trailer Voice            | Dramatic voice, used to build anticipation in movie trailers, typically associated with action or thrillers                                                                                                                                                                                            | "In a world on the brink of chaos, one hero will rise. Prepare yourself for a story of epic proportions, coming soon to the big screen."                                                                                                                                                                                                                                                                                                                                                                                                                 | 20%            |
| Squeaky Mouse                  | A cute little squeaky mouse                                                                                                                                                                                                                                                                            | "I may be small, but my attitude is anything but! \[giggles] Watch it, big feet, or I'll give your toes a nibble you won't forget!"                                                                                                                                                                                                                                                                                                                                                                                                                      | 20%            |
| Angry Pirate                   | An angry old pirate, loud and boisterous                                                                                                                                                                                                                                                               | "I've faced storms that would turn your hair white and sea monsters that would make your knees quake. You think you can cross Captain Blackheart and live to tell the tale?"                                                                                                                                                                                                                                                                                                                                                                             | 30%            |
| New Yorker                     | Deep, gravelly thick New York accent, tough and world-weary, often cynical                                                                                                                                                                                                                             | "I've been walking these streets longer than you can imagine, kid. There's nothing you can say or do that'll surprise me anymore."                                                                                                                                                                                                                                                                                                                                                                                                                       | 40%            |
| Mad Scientist                  | A voice of an eccentric scientific genius with rapid, erratic speech patterns that accelerate with excitement. His German-tinged accent becomes more pronounced when agitated. The pitch varies widely from contemplative murmurs to manic exclamations, with frequent eruptions of maniacal laughter. | "I am doctor Heinrich, revolutionary genius rejected by the narrow-minded scientific establishment! Bah! They called my theories impossible, my methods unethical—but who is laughing now? (maniacal laughter) For twenty years I have perfected my creation in this mountain laboratory, harnessing energies beyond mortal comprehension! The fools at the academy will regret their mockery when my quantum destabilizer reveals the multiverse. Or perhaps new life forms... the experiment has certain unpredictable variables... FASCINATING ones!" | 38%            |



# Payouts

> Earn rewards by sharing your voice in the Voice Library.

<img src="file:a00e9579-aae9-4bcf-bb5e-3dc6581a3910" alt="Payouts" />


## Overview

The [Payouts](https://elevenlabs.io/payouts) system allows you to earn rewards for sharing voices in the [Voice library](/docs/product-guides/voices/voice-library). ElevenLabs uses <a href="https://stripe.com/connect">Stripe Connect</a> to process reward payouts.


## Account setup

To set up your Payouts account:

* Click on your account in the bottom left and select ["Payouts"](https://elevenlabs.io/app/payouts).

<Frame background="subtle">
  ![Payouts overview](file:290c4809-8205-47cd-ad3a-0c1575f1a071)
</Frame>

* Follow the prompts from Stripe Connect to complete the account setup.


## Tracking usage and earnings

* You can track the usage of your voices by going to ["My Voices"](https://elevenlabs.io/app/voice-lab), clicking "View" to open the detailed view for your voice, then clicking the sharing icon at the bottom. Once you have the Sharing Options open, click "View Metrics".
* The rewards you earn are based on the options you selected when [sharing your voice in the Voice Library](/docs/product-guides/voices/voice-library#sharing-voices).
* You can also see your all-time earnings and past payouts by going back to your Payouts page.


## Reader app rewards

* If your voice is marked as **[High-Quality](/docs/product-guides/voices/voice-library#category)** and you have activated the "Available in ElevenReader" toggle, your voice will made be available in the [ElevenReader app](https://elevenlabs.io/text-reader). Rewards for ElevenReader are reported separately – to view your Reader App rewards, check the "ElevenReader" box on your "View Metrics" screen.


## Things to know

* Rewards accumulate frequently throughout the day, but payouts typically happen once a week as long as you have an active paid subscription and your accrued payouts exceed the minimum threshold. In most cases this is \$10, but some countries may have a higher threshold.

* You can see your past payouts by going to your [Payouts](https://elevenlabs.io/app/payouts) page in the sidebar.


## Supported countries

* Currently, Stripe Connect is not supported in all countries. We are constantly working to expand our reach for Payouts and plan to add availability in more countries when possible.

<Accordion title="Supported countries">
  - Argentina
  - Australia
  - Austria
  - Belgium
  - Bulgaria
  - Canada
  - Chile
  - Colombia
  - Croatia
  - Cyprus
  - Czech Republic
  - Denmark
  - Estonia
  - Finland
  - France
  - Germany
  - Greece
  - Hong Kong SAR
  - China
  - Hungary
  - Iceland
  - India
  - Indonesia
  - Ireland
  - Israel
  - Italy
  - Japan
  - Latvia
  - Liechtenstein
  - Lithuania
  - Luxembourg
  - Malaysia
  - Malta
  - Mexico
  - Monaco
  - Netherlands
  - New Zealand
  - Nigeria
  - Norway
  - Peru
  - Philippines
  - Poland
  - Portugal
  - Qatar
  - Romania
  - Saudi Arabia
  - Singapore
  - Slovakia
  - Slovenia
  - South Africa
  - South Korea
  - Spain
  - Sweden
  - Switzerland
  - Thailand
  - Taiwan
  - Turkey
  - United Arab Emirates
  - United Kingdom
  - United States
  - Uruguay
  - Vietnam
</Accordion>



# Audio Native

> Easily embed ElevenLabs on any web page.

<img src="file:8d43b0aa-9076-4155-9eab-7c0d33be102f" alt="Audio Native" />


## Overview

Audio Native is an embedded audio player that automatically voices content of a web page using ElevenLab’s [Text to Speech](/docs/product-guides/playground/text-to-speech) service. It can also be used to embed pre-generated content from a project into a web page. All it takes to embed on your site is a small HTML snippet. In addition, Audio Native provides built-in metrics allowing you to precisely track audience engagement via a listener dashboard.

The end result will be a Audio Native player that can narrate the content of a page, or, like in the case below, embed pre-generated content from a project:

<iframe width="100%" height="90" seamless src="https://elevenlabs.io/player/index.html?publicUserId=4d7f6f3d38ae27705f5b516ffd3e413a09baa48667073d385e5be1be773eaf69&projectId=gLj1spzTwuTgKuOtyfnX&small=true&textColor=rgba(0,%200,%200,%201)&backgroundColor=rgba(255,%20255,%20255,%201)" />


## Guide

<Steps>
  <Step title="Navigate to Audio Native">
    In the ElevenLabs dashboard, under "Audio Tools" navigate to ["Audio Native"](/app/audio-native).
  </Step>

  <Step title="Configure player appearance">
    Customize the player appearance by selecting background and text colors.
  </Step>

  <Step title="Configure allowed sites">
    The URL allowlist is the list of web pages that will be permitted to play your content.

    You can choose to add a specific web page (e.g. `https://elevenlabs.io/blog`) or add a whole domain to the allowlist (e.g. `http://elevenlabs.io`). If a player is embedded on a page that is not in the allowlist, it will not work as intended.
  </Step>

  <Step title="Get embed code">
    Once you've finished configuring the player and allowlist, copy the embed code and paste it into your website's source code.
  </Step>
</Steps>


## Technology-specific guides

To integrate Audio Native into your web techology of choice, see the following guides:

<CardGroup cols={4}>
  <Card title="React" icon="brands react" href="/docs/product-guides/audio-tools/audio-native/react" />

  <Card title="Ghost" icon="duotone ghost" href="/docs/product-guides/audio-tools/audio-native/ghost" />

  <Card title="Squarespace" icon="brands squarespace" href="/docs/product-guides/audio-tools/audio-native/squarespace" />

  <Card title="Framer" icon="duotone browser" href="/docs/product-guides/audio-tools/audio-native/framer" />

  <Card title="Webflow" icon="brands webflow" href="/docs/product-guides/audio-tools/audio-native/webflow" />

  <Card title="Wordpress" icon="brands wordpress" href="/docs/product-guides/audio-tools/audio-native/word-press" />

  <Card title="Wix" icon="brands wix" href="/docs/product-guides/audio-tools/audio-native/wix" />
</CardGroup>


## Using the API

You can use the [Audio Native API](/docs/api-reference/audio-native/create) to programmatically create an Audio Native player for your existing content.

<CodeBlocks>
  ```python title="Python"
  from elevenlabs import ElevenLabs

  elevenlabs = ElevenLabs(
  api_key="YOUR_API_KEY",
  )
  response = elevenlabs.audio_native.create(
  name="name",
  )

  # Use the snippet in response.html_snippet to embed the player on your website

  ```

  ```javascript title="JavaScript"
  import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

  const elevenlabs = new ElevenLabsClient({ apiKey: "YOUR_API_KEY" });
  const { html_snippet } = await elevenlabs.audioNative.create({
      name: "my-audio-native-player"
  });

  // Use the HTML code in html_snippet to embed the player on your website
  ```
</CodeBlocks>


## Settings

<AccordionGroup>
  <Accordion title="Voice and model">
    ### Voices

    To configure the voice and model that will be used to read the content of the page, navigate to the "Settings" tab and select the voice and model you want to use.
  </Accordion>

  <Accordion title="Pronunciation dictionaries">
    ### Pronunciation dictionaries

    Sometimes you may want to specify the pronunciation of certain words, such as character or brand names, or specify how acronyms should be read. Pronunciation dictionaries allow this functionality by enabling you to upload a lexicon or dictionary file that includes rules about how specified words should be pronounced, either using a phonetic alphabet (phoneme tags) or word substitutions (alias tags).

    Whenever one of these words is encountered in a project, the AI will pronounce the word using the specified replacement. When checking for a replacement word in a pronunciation dictionary, the dictionary is checked from start to end and only the first replacement is used.
  </Accordion>
</AccordionGroup>



# Audio Native with React

> Integrate Audio Native into your React apps.

<Info>
  Follow the steps in the [Audio Native overview](/docs/product-guides/audio-tools/audio-native) to
  get started with Audio Native before continuing with this guide.
</Info>

This guide will show how to integrate Audio Native into React apps. The focus will be on a Next.js project, but the underlying concepts will work for any React based application.

<Steps>
  <Step title="Create an Audio Native React component">
    After completing the steps in the [Audio Native overview](/docs/product-guides/audio-tools/audio-native), you'll have an embed code snippet. Here's an example snippet:

    ```html title="Embed code snippet"
      <div
        id="elevenlabs-audionative-widget"
        data-height="90"
        data-width="100%"
        data-frameborder="no"
        data-scrolling="no"
        data-publicuserid="public-user-id"
        data-playerurl="https://elevenlabs.io/player/index.html"
        data-projectid="project-id"
      >
        Loading the <a href="https://elevenlabs.io/text-to-speech" target="_blank" rel="noopener">Elevenlabs Text to Speech</a> AudioNative Player...
      </div>
      <script src="https://elevenlabs.io/player/audioNativeHelper.js" type="text/javascript"></script>
    ```

    We can extract the data from the snippet to create a customizable React component.

    ```tsx title="ElevenLabsAudioNative.tsx" maxLines=0
    // ElevenLabsAudioNative.tsx

    'use client';

    import { useEffect } from 'react';

    export type ElevenLabsProps = {
      publicUserId: string;
      textColorRgba?: string;
      backgroundColorRgba?: string;
      size?: 'small' | 'large';
      children?: React.ReactNode;
    };

    export const ElevenLabsAudioNative = ({
      publicUserId,
      size,
      textColorRgba,
      backgroundColorRgba,
      children,
    }: ElevenLabsProps) => {
      useEffect(() => {
        const script = document.createElement('script');

        script.src = 'https://elevenlabs.io/player/audioNativeHelper.js';
        script.async = true;
        document.body.appendChild(script);

        return () => {
          document.body.removeChild(script);
        };
      }, []);

      return (
        <div
          id="elevenlabs-audionative-widget"
          data-height={size === 'small' ? '90' : '120'}
          data-width="100%"
          data-frameborder="no"
          data-scrolling="no"
          data-publicuserid={publicUserId}
          data-playerurl="https://elevenlabs.io/player/index.html"
          data-small={size === 'small' ? 'True' : 'False'}
          data-textcolor={textColorRgba ?? 'rgba(0, 0, 0, 1.0)'}
          data-backgroundcolor={backgroundColorRgba ?? 'rgba(255, 255, 255, 1.0)'}
        >
          {children ? children : 'Elevenlabs AudioNative Player'}
        </div>
      );
    };

    export default ElevenLabsAudioNative;
    ```

    The above component can be found on [GitHub](https://github.com/elevenlabs/elevenlabs-examples/blob/main/examples/audio-native/react/ElevenLabsAudioNative.tsx).
  </Step>

  <Step title="Use the Audio Native component">
    Before using the component on your page, you need to retrieve your public user ID from the original code snippet. Copy the contents of `data-publicuserid` from the embed code snippet and insert it into the `publicUserId` prop of the component.

    ```tsx title="page.tsx" maxLines=0
    import { ElevenLabsAudioNative } from './path/to/ElevenLabsAudioNative';

    export default function Page() {
      return (
        <div>
          <h1>Your Page Title</h1>

          // Insert the public user ID from the embed code snippet
          <ElevenLabsAudioNative publicUserId="<your-public-user-id>" />

          <p>Your page content...</p>
        </div>
      );
    }
    ```
  </Step>

  <Step title="Customize the player with component props">
    The component props can be used to customize the player. For example, you can change the size, text color, and background color.

    ```tsx title="page.tsx" maxLines=0
    import { ElevenLabsAudioNative } from './path/to/ElevenLabsAudioNative';

    export default function Page() {
      return (
        <div>
          <h1>Your Page Title</h1>

          <ElevenLabsAudioNative
            publicUserId="<your-public-user-id>"
            size="small"
            textColorRgba="rgba(255, 255, 255, 1.0)"
            backgroundColorRgba="rgba(0, 0, 0, 1.0)"
          />

          <p>Your page content...</p>
        </div>
      );
    }
    ```
  </Step>
</Steps>



# Audio Native with Ghost

> Integrate Audio Native into your Ghost blog.

<Info>
  Follow the steps in the [Audio Native overview](/docs/product-guides/audio-tools/audio-native) to
  get started with Audio Native before continuing with this guide.
</Info>

<Steps>
  <Step title="Add HTML to your blog post">
    Navigate to your Ghost blog, sign in and open the settings page for the blog post you wish to narrate.
  </Step>

  <Step title="Add the embed code to your blog post">
    Click the "+" symbol on the left and select "HTML" from the menu.

    <img src="file:122e0f66-6daf-45b3-bba3-4304baf206f2" alt="Audio Native" />

    Paste the Audio Native embed code into the HTML box and press enter.

    ```html title="Embed code snippet"
        <div
            id="elevenlabs-audionative-widget"
            data-height="90"
            data-width="100%"
            data-frameborder="no"
            data-scrolling="no"
            data-publicuserid="public-user-id"
            data-playerurl="https://elevenlabs.io/player/index.html"
            data-projectid="project-id"
        >
            Loading the <a href="https://elevenlabs.io/text-to-speech" target="_blank" rel="noopener">Elevenlabs Text to Speech</a> AudioNative Player...
        </div>
        <script src="https://elevenlabs.io/player/audioNativeHelper.js" type="text/javascript"></script>
    ```

    <img src="file:2e4441b8-fb9f-4c35-be12-3335fb7281ba" alt="Audio Native" />
  </Step>

  <Step title="Update the blog post">
    Click the "Update" button in the top right corner of the editor, which should now be highlighted in green text.

    <img src="file:1eee11e1-8a70-4396-a09d-1d48dba43e39" alt="Audio Native" />
  </Step>

  <Step title="Navigate to the live version of the blog post">
    Finally, navigate to the live version of the blog post. You should see a message to let you know that the Audio Native project is being created. After a few minutes the text in your blog will be converted to an audio article and the embedded audio player will appear.

    <img src="file:ba0e039a-0e2d-47f1-8f94-ab1c1dc9eee3" alt="Audio Native" />
  </Step>
</Steps>



# Audio Native with Squarespace

> Integrate Audio Native into your Squarespace sites.

<Info>
  Follow the steps in the [Audio Native overview](/docs/product-guides/audio-tools/audio-native) to
  get started with Audio Native before continuing with this guide.
</Info>

<Steps>
  <Step title="Add HTML to your blog post">
    Navigate to your Squarespace site, sign in and open the page you wish to add narration to.
  </Step>

  <Step title="Add the embed code to your blog post">
    Click the "+" symbol on the spot you want to place the Audio Native player and select "Code" from the menu.

    <img src="file:e655db34-6277-4c0c-b0d7-e6c16f52cc0c" alt="Audio Native" />

    Paste the Audio Native embed code into the HTML box and press enter.

    ```html title="Embed code snippet"
        <div
            id="elevenlabs-audionative-widget"
            data-height="90"
            data-width="100%"
            data-frameborder="no"
            data-scrolling="no"
            data-publicuserid="public-user-id"
            data-playerurl="https://elevenlabs.io/player/index.html"
            data-projectid="project-id"
        >
            Loading the <a href="https://elevenlabs.io/text-to-speech" target="_blank" rel="noopener">Elevenlabs Text to Speech</a> AudioNative Player...
        </div>
        <script src="https://elevenlabs.io/player/audioNativeHelper.js" type="text/javascript"></script>
    ```

    <img src="file:e9a662b6-9ae5-49c0-a930-01e926f9ab64" alt="Audio Native" />
  </Step>

  <Step title="Update the blog post">
    Click the "Save" button in the top right corner of the editor, which should now be highlighted.
  </Step>

  <Step title="Navigate to the live version of the blog post">
    Finally, navigate to the live version of the blog post. You should see a message to let you know that the Audio Native project is being created. After a few minutes the text in your blog will be converted to an audio article and the embedded audio player will appear.

    <img src="file:c81b9260-2a11-46bd-b752-e080bc45ef63" alt="Audio Native" />
  </Step>
</Steps>



# Audio Native with Framer

> Integrate Audio Native into your Framer websites.

<Info>
  Follow the steps in the [Audio Native overview](/docs/product-guides/audio-tools/audio-native) to
  get started with Audio Native before continuing with this guide.
</Info>

<Steps>
  <Step title="Add Audio Native script to your page">
    Navigate to your Framer page, sign in and go to your site settings. From the Audio Native embed code, extract the `<script>` tag and paste it in the "End of `<body>` tag" field.

    ```html title="Embed script "
        <script src="https://elevenlabs.io/player/audioNativeHelper.js" type="text/javascript"></script>
    ```

    <img src="file:6ff0cee5-91fe-4eb5-8399-cc52160ab6e8" alt="Audio Native" />
  </Step>

  <Step title="Add an Embed Element">
    On your Framer blog page, add an Embed Element from Utilities.

    <img src="file:51a05f33-cbab-400b-9926-729f6157b999" alt="Audio Native" />

    In the config for the Embed Element, switch the type to HTML and paste the `<div>` snippet from the Audio Native embed code into the HTML box.

    ```html title="Embed div"
        <div
            id="elevenlabs-audionative-widget"
            data-height="90"
            data-width="100%"
            data-frameborder="no"
            data-scrolling="no"
            data-publicuserid="public-user-id"
            data-playerurl="https://elevenlabs.io/player/index.html"
            data-projectid="project-id"
        >
            Loading the <a href="https://elevenlabs.io/text-to-speech" target="_blank" rel="noopener">Elevenlabs Text to Speech</a> AudioNative Player...
        </div>
    ```

    <img src="file:63574bfd-a57a-4c79-902b-4f305126d89f" alt="Audio Native" />
  </Step>

  <Step title="Publish your changes">
    Finally, publish your changes and navigate to the live version of your page. You should see a message to let you know that the Audio Native project is being created. After a few minutes the text in your blog will be converted to an audio article and the embedded audio player will appear.

    <img src="file:cd004784-282e-4bc5-a85d-351879a030db" alt="Audio Native" />
  </Step>
</Steps>



# Audio Native with Webflow

> Integrate Audio Native into your Webflow sites.

<Info>
  Follow the steps in the [Audio Native overview](/docs/product-guides/audio-tools/audio-native) to
  get started with Audio Native before continuing with this guide.
</Info>

<Steps>
  <Step title="Add HTML to your blog post">
    Navigate to your Webflow blog, sign in and open the editor for the blog post you wish to narrate.
  </Step>

  <Step title="Add the embed code to your blog post">
    Click the "+" symbol in the top left and select "Code Embed" from the Elements menu.

    <img src="file:a5fcae68-d688-4fdd-911c-f58ca9597470" alt="Audio Native" />

    Paste the Audio Native embed code into the HTML box and click "Save & Close".

    ```html title="Embed code snippet"
        <div
            id="elevenlabs-audionative-widget"
            data-height="90"
            data-width="100%"
            data-frameborder="no"
            data-scrolling="no"
            data-publicuserid="public-user-id"
            data-playerurl="https://elevenlabs.io/player/index.html"
            data-projectid="project-id"
        >
            Loading the <a href="https://elevenlabs.io/text-to-speech" target="_blank" rel="noopener">Elevenlabs Text to Speech</a> AudioNative Player...
        </div>
        <script src="https://elevenlabs.io/player/audioNativeHelper.js" type="text/javascript"></script>
    ```

    <img src="file:6cbc02bd-cbf3-4b18-9d19-c20df1ffc2cb" alt="Audio Native" />
  </Step>

  <Step title="Re-position the code embed">
    In the Navigator, place the code embed where you want it to appear on the page.

    <img src="file:3c197a1c-1f45-4462-8466-fa3b49252f0e" alt="Audio Native" />
  </Step>

  <Step title="Publish your changes">
    Finally, publish your changes and navigate to the live version of the blog post. You should see a message to let you know that the Audio Native project is being created. After a few minutes the text in your blog will be converted to an audio article and the embedded audio player will appear.

    <img src="file:4acb6332-453a-4f48-98e6-047484a492a0" alt="Audio Native" />
  </Step>
</Steps>



# Audio Native with WordPress

> Integrate Audio Native into your WordPress sites.

<Info>
  Follow the steps in the [Audio Native overview](/docs/product-guides/audio-tools/audio-native) to
  get started with Audio Native before continuing with this guide.
</Info>

<Steps>
  <Step title="Install the WPCode plugin">
    Install the [WPCode plugin](https://wpcode.com/) into your WordPress website to embed HTML code.
  </Step>

  <Step title="Create a new code snippet">
    In the WordPress admin console, click on "Code Snippets". Add the Audio Native embed code to the new code snippet.

    ```html title="Embed code snippet"
        <div
            id="elevenlabs-audionative-widget"
            data-height="90"
            data-width="100%"
            data-frameborder="no"
            data-scrolling="no"
            data-publicuserid="public-user-id"
            data-playerurl="https://elevenlabs.io/player/index.html"
            data-projectid="project-id"
        >
            Loading the <a href="https://elevenlabs.io/text-to-speech" target="_blank" rel="noopener">Elevenlabs Text to Speech</a> AudioNative Player...
        </div>
        <script src="https://elevenlabs.io/player/audioNativeHelper.js" type="text/javascript"></script>
    ```

    <img src="file:796b369e-fa8c-45e6-a32b-3214b7e815e3" alt="Audio Native" />

    Pick "Auto Insert" for the insert method and set the location to be "Insert Before Content".

    <img src="file:62ab8cfb-876f-4f59-ac0d-dfa2ac8ae17a" alt="Audio Native" />
  </Step>

  <Step title="Publish your changes">
    Finally, publish your changes and navigate to the live version of the blog post. You should see a message to let you know that the Audio Native project is being created. After a few minutes the text in your blog will be converted to an audio article and the embedded audio player will appear.

    <img src="file:4f6b969b-b49e-444f-872e-a028b72f159b" alt="Audio Native" />
  </Step>
</Steps>



# Audio Native with Wix

> Integrate Audio Native into your Wix sites.

<Info>
  Follow the steps in the [Audio Native overview](/docs/product-guides/audio-tools/audio-native) to
  get started with Audio Native before continuing with this guide.
</Info>

<Steps>
  <Step title="Add HTML to your blog post">
    Navigate to your Wix site, sign in and open the settings page for the page you wish to narrate.
  </Step>

  <Step title="Add the embed code to your blog post">
    Click the "+" symbol at the top of your content and select "HTML Code" from the menu.

    <img src="file:6693b0d4-e857-4e82-9091-82a42a488dd6" alt="Audio Native" />

    Paste the Audio Native embed code into the HTML box and click "Save".

    ```html title="Embed code snippet"
        <div
            id="elevenlabs-audionative-widget"
            data-height="90"
            data-width="100%"
            data-frameborder="no"
            data-scrolling="no"
            data-publicuserid="public-user-id"
            data-playerurl="https://elevenlabs.io/player/index.html"
            data-projectid="project-id"
        >
            Loading the <a href="https://elevenlabs.io/text-to-speech" target="_blank" rel="noopener">Elevenlabs Text to Speech</a> AudioNative Player...
        </div>
        <script src="https://elevenlabs.io/player/audioNativeHelper.js" type="text/javascript"></script>
    ```

    <img src="file:baf29b48-2314-48c6-9091-ba771a402903" alt="Audio Native" />
  </Step>

  <Step title="Publish the page">
    Click the "Publish" button in the top right corner of the editor.
  </Step>

  <Step title="Navigate to the live version of the blog post">
    Finally, navigate to the live version of the blog post. You should see a message to let you know that the Audio Native project is being created. After a few minutes the text in your blog will be converted to an audio article and the embedded audio player will appear.

    <img src="file:93876038-4fa9-4c1b-bd83-b13042258b01" alt="Audio Native" />
  </Step>
</Steps>



# Voiceover studio

> A guide on how to create long-form content with ElevenLabs Voiceover Studio

<img src="file:ef7d0e82-d778-42fe-a765-84a0f451d5a8" alt="Voiceover studio" />


## Overview

Voiceover Studio combines the audio timeline with our Sound Effects feature, giving you the ability to write a dialogue between any number of speakers, choose those speakers, and intertwine your own creative sound effects anywhere you like.

<iframe width="100%" height="400" src="https://www.youtube.com/embed/GBdOQClluIA?autoplay=0" title="YouTube video player" frameborder="0" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen />


## Guide

<Steps>
  <Step title="Navigate to the Voiceover studio">
    In the ElevenLabs dashboard, click on the "Voiceover Studio" option in the sidebar under "Audio
    Tools".
  </Step>

  <Step title="Create a new voiceover">
    Click the "Create a new voiceover" button to begin. You can optionally upload video or audio to
    create a voiceover from.
  </Step>

  <Step title="Modify the voiceover with the timeline">
    On the bottom half of your screen, use the timeline to add and edit voiceover clips plus add
    sound effects.
  </Step>

  <Step title="Export your voiceover">
    Once you're happy with your voiceover, click the "Export" button in the bottom right, choose the
    format you want and either view or download your voiceover.
  </Step>
</Steps>


## FAQ

<AccordionGroup>
  <Accordion title="How does the timeline work?">
    ### Timeline

    The timeline is a linear representation of your Voiceover project. Each row represents a track, and on the far left section you have the track information for voiceover or SFX tracks. In the middle, you can create the clips that represent when a voice is speaking or a SFX is playing. On the right-hand side, you have the settings for the currently selected clip.
  </Accordion>

  <Accordion title="How do I add tracks?">
    ### Adding Tracks

    To add a track, click the "Add Track" button in the bottom left of the timeline. You can choose to add a voiceover track or an SFX track.

    There are three types of tracks you can add in the studio: Voiceover tracks, SFX tracks and uploaded audio.

    * **Voiceover Tracks:** Voiceover tracks create new Speakers. You can click and add clips on the timeline wherever you like. After creating a clip, start writing your desired text on the speaker cards above and click "Generate". Similar to Dubbing Studio, you will also see a little cogwheel on each Speaker track - simply click on it to adjust the voice settings or replace any speaker with a voice directly from your Voices - including your own Professional Voice Clone if you have created one.

    * **SFX Tracks:** Add a SFX track, then click anywhere on that track to create a SFX clip. Similar to our independent SFX feature, simply start writing your prompt in the Speaker card above and click "Generate" to create your new SFX audio. You can lengthen or shorten SFX clips and move them freely around your timeline to fit your project - make sure to press the "stale" button if you do so.

    * **Uploaded Audio:** Add an audio track including background music or sound effects. It's best to avoid uploading audio with speakers, as any speakers in this track will not be detected, so you won't be able to translate or correct them.
  </Accordion>

  <Accordion title="How does this differ from Dubbing Studio?">
    ### Key Differences from Dubbing Studio

    If you chose not to upload a video when you created your Voiceover project, then the entire timeline is yours to work with and there are no time constraints. This differs from Dubbing Studio as it gives you a lot more freedom to create what you want and adjust the timing more easily.

    When you Add a Voiceover Track, you will instantly be able to create clips on your timeline. Once you create a Voiceover clip, begin by writing in the Speaker Card above. After generating that audio, you will notice your clip on the timeline will automatically adjust its length based on the text prompt - this is called "Dynamic Generation". This option is also available in Dubbing Studio by right-clicking specific clips, but because syncing is more important with dubbed videos, the default generation type there is "Fixed Generation," meaning the clips' lengths are not affected.
  </Accordion>

  <Accordion title="How are credits deducted with Voiceover Studio?">
    ### Credit Costs

    Voiceover Studio does not deduct credits to create your initial project. Credits are deducted every time material is generated. Similar to Speech-Synthesis, credit costs for Voiceover Clips are based on the length of the text prompt. SFX clips will deduct 80 credits per generation.

    If you choose to Dub (translate) your Voiceover Project into different languages, this will also cost additional credits depending on how much material needs to be generated. The cost is 1 credit per character for the translation, plus the cost of generating the new audio for the additional languages.
  </Accordion>

  <Accordion title="How do I upload a script?">
    ### Uploading Scripts

    With Voiceover Studio, you have the option to upload a script for your project as a CSV file. You can either include speaker name and line, or speaker name, line, start time and end time. To upload a script, click on the cog icon in the top right hand corner of the page and select "Import Script".

    Scripts should be provided in the following format:

    ```
    speaker,line
    ```

    Example input:

    ```
    speaker,line
    Joe,"Hey!"
    Maria,"Oh, hi Joe! It's been a while."
    ```

    You can also provide start and end times for each line in the following format:

    ```
    speaker,line,start_time,end_time
    ```

    Example input:

    ```
    speaker,line,start_time,end_time
    Joe,"Hey!",0.1,1.5
    Maria,"Oh, hi Joe! It's been a while.",1.6,2.0
    ```

    Once your script has imported, make sure to assign voices to each speaker before you generate the audio. To do this, click the cog icon in the information for each track, on the left.

    If you don't specify start and end times for your clips, Voiceover Studio will estimate how long each clip will be, and distribute them along your timeline.
  </Accordion>

  <Accordion title="What's the difference between Dynamic Duration and Fixed Duration?">
    ### Dynamic Duration

    By default, Voiceover Studio uses Dynamic Duration, which means that the length of the clip will vary depending on the text input and the voice used. This ensures that the audio sounds as natural as possible, but it means that the length of the clip might change after the audio has been generated. You can easily reposition your clips along the timeline once they have been generated to get a natural sounding flow. If you click "Generate Stale Audio", or use the generate button on the clip, the audio will be generated using Dynamic Duration.

    This also applies if you do specify the start and end time for your clips. The clips will generate based on the start time you specify, but if you use the default Dynamic Duration, the end time is likely to change once you generate the audio.

    ### Fixed Duration

    If you need the clip to remain the length specified, you can choose to generate with Fixed Duration instead. To do this, you need to right click on the clip and select "Generate Audio Fixed Duration". This will adjust the length of the generated audio to fit the specified length of the clip. This could lead to the audio sounding unnaturally quick or slow, depending on the length of your clip.

    If you want to generate multiple clips at once, you can use shift + click to select multiple clips for a speaker at once, then right click on one of them to select "Generate Audio Fixed Duration" for all selected clips.
  </Accordion>
</AccordionGroup>



# Voice isolator

> A guide on how to remove background noise from audio recordings.

<img src="file:e824bbeb-63ec-48bf-8206-7145d8fa0c16" alt="Voice changer product feature" />


## Overview

Voice isolator is a tool that allows you to remove background noise from audio recordings.


## Guide

<img src="file:41a72729-c66a-4fa4-b369-2cf7ca72db67" alt="Voice isolator" />

To use the voice isolator app, navigate to [Voice Isolator](https://elevenlabs.io/app/voice-isolator) under the Audio Tools section. Here you can upload or drag and drop your audio file into the app, or record a new audio file with your device's microphone.

Click "Isolate voice" to start the process. The app will isolate the voice from the background noise and return a new audio file with the isolated voice. Once the process is complete, you can download the audio file or play it back in the app.

The voice isolator functionality is also available via the [API](/docs/api-reference/audio-isolation/audio-isolation) to easily integrate this functionality into your own applications.

<CardGroup>
  <Card title="Voice isolator app" href="https://elevenlabs.io/app/voice-isolator">
    Use the voice isolator app.
  </Card>

  <Card title="API reference" href="/docs/api-reference/audio-isolation/audio-isolation">
    Use the voice isolator API.
  </Card>
</CardGroup>



# AI speech classifier

> A guide on how to detect AI audio

<img src="file:4c6a1788-304c-47c8-a95c-93ca47976582" alt="AI speech classifier" />


## Overview

The AI speech classifier is a tool that allows you to detect if an audio file was generated by ElevenLabs.


## Guide

<Steps>
  <Step title="Navigate to the AI speech classifier page">
    Select the "AI speech classifier" option from the sidebar under "Audio Tools" in the ElevenLabs
    dashboard.
  </Step>

  <Step title="Upload an audio file">
    Click the "Upload audio" button upload an audio file and begin scanning.
  </Step>

  <Step title="Analyze the audio file">
    The AI speech classifier will analyze the audio file and provide a result.
  </Step>
</Steps>


## FAQ

<AccordionGroup>
  <Accordion title="How accurate is the AI speech classifier?">
    Our classifier maintains high accuracy (99% precision, 80% recall) for audio files generated
    with ElevenLabs that have not been modified. We will continue to improve this tool, while
    exploring other detection tools that provide transparency about how content was created.
  </Accordion>

  <Accordion title="Does using the tool cost me anything?">
    No, the tool is free for all to use.
  </Accordion>

  <Accordion title="Do I have to be logged in to use the tool?">
    A [web version](https://elevenlabs.io/ai-speech-classifier) of the tool is available for you to
    use without having to log in.
  </Accordion>
</AccordionGroup>



# Account

> Create and manage your ElevenLabs account to start generating AI audio

To begin using ElevenLabs, you'll need to create an account. Follow these steps:

* **Sign Up**: Visit the [ElevenLabs website](https://elevenlabs.io/sign-up) and click on the 'Get started free' button. You can register using your email or through one of the OAuth providers.
* **Verify Email**: Check your email for a verification link from ElevenLabs. Click the link to verify your account.
* **Initial Setup**: After verification, you'll be directed to the Speech Synthesis page where you can start generating audio from text.

**Exercise**: Try out an example to get started or type something, select a voice and click generate!

<img src="file:f11a23db-23ec-4239-959c-7caaede8294d" alt="Account creation exercise" />

You can sign up with traditional email and password or using popular OAuth providers like Google, Facebook, and GitHub.

If you choose to sign up with your email, you will be asked to verify your email address before you can start using the service. Once you have verified your email, you will be taken to the Speech Synthesis page, where you can immediately start using the service. Simply type anything into the box and press “generate” to convert the text into voiceover narration. Please note that each time you press “generate” anywhere on the website, it will deduct credits from your quota.

If you sign up using Google OAuth, your account will be intrinsically linked to your Google account, meaning you will not be able to change your email address, as it will always be linked to your Google email.



# Billing

> Manage your subscription, view pricing plans, and understand how credit rollover works

<CardGroup>
  <Card title="Pricing" href="https://elevenlabs.io/pricing">
    View the pricing page
  </Card>

  <Card title="Subscription details" href="https://elevenlabs.io/app/subscription">
    View your subscription details
  </Card>
</CardGroup>

When signing up, you will be automatically assigned to the free tier. To view your subscription, click on "My Account" in the bottom left corner and select ["Subscription"](https://elevenlabs.io/app/subscription). You can read more about the different plans [here](https://elevenlabs.io/pricing). At the bottom of the page, you will find a comparison table to understand the differences between the various plans.

We offer five public plans: Free, Starter, Creator, Pro, Scale, and Business. In addition, we also offer an Enterprise option that's specifically tailored to the unique needs and usage of large organizations.

You can see details of all our plans on the subscription page. This includes information about the total monthly credit quota, the number of custom voices you can have saved simultaneously, and the quality of audio produced.

Cloning is only available on the Starter tier and above. The free plan offers three custom voices that you can create using our [Voice Design tool](/docs/product-guides/voices/voice-design), or you can add voices from the [Voice Library](/docs/product-guides/voices/voice-library) if they are not limited to the paid tiers.

You can upgrade your subscription at any time, and any unused quota from your previous plan will roll over to the new one. As long as you don’t cancel or downgrade, unused credits at the end of the month will carry over to the next month, up to a maximum of two months’ worth of credits. For more information, please visit our Help Center articles:

* ["How does credit rollover work?"](https://help.elevenlabs.io/hc/en-us/articles/27561768104081-How-does-credit-rollover-work)
* ["What happens to my subscription and quota at the end of the month?"](https://help.elevenlabs.io/hc/en-us/articles/13514114771857-What-happens-to-my-subscription-and-quota-at-the-end-of-the-month)

From the [subscription page](https://elevenlabs.io/app/subscription), you can also downgrade your subscription at any point in time if you would like. When downgrading, it won't take effect until the current cycle ends, ensuring that you won't lose any of the monthly quota before your month is up.

When generating content on our paid plans, you get commercial rights to use that content. If you are on the free plan, you can use the content non-commercially with attribution. Read more about the license in our [Terms of Service](https://elevenlabs.io/terms) and in our Help Center [here](https://help.elevenlabs.io/hc/en-us/articles/13313564601361-Can-I-publish-the-content-I-generate-on-the-platform-).

For more information on payment methods, please refer to the [Help Center](https://help.elevenlabs.io/).



---
**Navigation:** [← Previous](./08-image-video.md) | [Index](./index.md) | [Next →](./10-consolidated-billing.md)
