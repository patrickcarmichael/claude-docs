**Navigation:** [← Previous](./07-migrate-from-playht-to-elevenlabs.md) | [Index](./index.md) | [Next →](./09-voice-library.md)

# Image & Video

> Complete guide to creating and editing images and videos in ElevenLabs.

<Frame background="subtle">
  ![Image & Video interface](file:631baa2a-6ac3-453b-a681-1f4ff5b06750)
</Frame>


## Overview

Image & Video enables you to create high-quality visual content from simple text descriptions or reference images. Generate static images or dynamic videos in any style, then refine them iteratively with additional prompts, upscale for high-resolution output, and even add lip-sync with audio. Export finished assets as standalone files or import them directly into Studio projects.

<Note>
  This feature is currently in beta.
</Note>


## Guide

Follow these steps to create your first visual asset:

<Steps>
  ### Select your mode

  Use the toggle in the upper right corner of the prompt box to choose between **Image** or **Video** generation.

  ### Provide a prompt or reference

  Describe your desired output using natural language in the prompt box. For more control, drag existing images or videos from the **Explore** or **History** tabs into the reference slots, or upload your own reference images in a wide range of file formats including JPG, PNG, WEBP, and more.

  ### Choose a model and settings

  Select the ideal generative model for your goal (e.g., OpenAI Sora 2 Pro, Google Veo 3.1, Kling 2.5, Flux 1 Kontext Pro). See the [Models](#models) section for detailed information on each model. Adjust settings like aspect ratio, resolution, duration (for video), and the number of variations to generate.

  ### Generate your asset

  Click the **[Generate](/docs/product-guides/playground/image-video#generate-1)** button. Your assets will be created and displayed in the **[History](/docs/product-guides/playground/image-video#history-1)** tab for review.

  ### Enhance and refine

  Use enhancement tools to perfect your media. **Upscale** the resolution, apply realistic **LipSync** with audio, or click **Recreate** to generate a new variation with the same settings.

  ### Share with others

  Click the **Share** button to generate a unique link for your creation. Send it to teammates and collaborators to collect feedback.

  ### Export your creation

  Download the asset as a standalone file or import it directly into a Studio project.
</Steps>


## Workflow

The creation process moves you from inspiration to finished asset in four stages:

### [Explore](/docs/product-guides/playground/image-video#explore-1)

Discover community creations to find inspiration, study effective prompts, or pull references directly into your own work.

### [Generate](/docs/product-guides/playground/image-video#generate-1)

Use the prompt box to describe what you want to create, select a model, fine-tune your settings, and bring your idea to life.

### [History](/docs/product-guides/playground/image-video#history-1)

Review your generations in the History tab to iterate and enhance. Recreate variations, reuse prompts, and apply enhancements like upscaling and lip-syncing.

### [Export](/docs/product-guides/playground/image-video#export-1)

Download finished assets in various formats or send them directly to Studio to use in your projects.


## Explore

The **Explore** tab displays a gallery of community creations for discovering inspiration and finding visuals to use as references.

**Search:** Use the search bar to find images and videos based on keywords.

**Sort:** Toggle between **Trending** and **Newest** to see what's popular or recently added.

**Drag-and-drop:** Pull any result from the grid directly into the prompt box to use as a start frame, end frame, or style reference.

**Preview details:** Click any tile to see the full prompt and settings used to create it.


## Generate

<Frame background="subtle">
  ![Video prompt interface](file:35baddd4-2490-405c-8776-2864c244d5ed)
</Frame>

The prompt box is anchored at the bottom of the page and provides all controls for creating visual content.

### Set mode and prompt

**Select mode:** Use the toggle in the upper right corner to switch between **Image** and **Video** generation.

**Write your prompt:** In the main field, describe what you want to generate using natural language. Be clear and descriptive for best results.

### Choose models and settings

<Frame background="subtle">
  ![Video models selection](file:497a97aa-a43d-46f6-b932-e918ba1b86a9)
</Frame>

**Select model:** Open the model menu to browse available options like OpenAI Sora 2 Pro, Google Veo 3.1, Kling 2.5, or Flux 1 Kontext Pro. Each model has unique strengths and capabilities listed for easy comparison. See the [Models](#models) section for detailed information.

**Adjust settings:** Fine-tune your generation with settings that appear below the prompt. These vary by model but often include:

* **Aspect Ratio**: Control the dimensions of your output
* **Resolution**: Set the quality level
* **Duration**: Specify video length (for video mode)
* **Number of Generations**: Create up to 4 variations at once

**Use controls:** On supported models, enable **Audio**, add a **Negative Prompt** to exclude unwanted elements, or adjust **Sound Control**.

### Add references

<Frame background="subtle">
  ![Video references
  interface](file:6be11989-18c4-403b-9cc4-4c69626188e9)
</Frame>

For greater control over output, add visual references to guide generation. Availability depends on the selected model. We support a wide range of image file formats including JPG, PNG, WEBP, and more.

**Start Frame (Video):** Sets the opening image of your video.

**End Frame (Video):** Sets the final image, influencing the transition.

**Image Refs (Image or Video):** Provide one or more images to guide overall style and look.

<Tip>
  Drag and drop items directly from the **Explore** or **History** tabs into reference slots for a
  faster workflow.
</Tip>

### Generate

Before generating, a cost indicator shows the total cost for the number of assets you've chosen to create. When ready, click **Generate**. Your new creations will appear in the **History** tab.


## History

<Frame background="subtle">
  ![Video history interface](file:ffb16903-15bb-426e-abd5-97290cce7376)
</Frame>

The **History** tab provides a chronological log of everything you've generated and serves as a workspace for refining previous work.

**Browse:** View all past images and videos.

**Inspect:** Click any asset to see the original prompt, model, and settings used to create it.

**Reuse:** Drag items from History back into the prompt box to use as references for new generations.

**Iterate:** Click **Recreate** to run the same prompt and settings again for a new variation, or adjust settings to guide generation in a new direction.

**Share:** Click **Share** to generate a unique link for your asset. Send it to teammates and collaborators for feedback.

**Export:** Download your asset as a standalone file or click **Edit in Studio** to import it directly into Studio.


## Export

Once you have a generation you're satisfied with, use built-in enhancement tools before exporting.

### Enhancing your creations

**Upscale:** Use **Topaz Upscale** to increase resolution by up to 4x while preserving sharp details.

**LipSync:** Apply realistic lip-syncing to your visuals:

* **Omnihuman 1.5**: Animate a static image with an audio track
* **Veed LipSync**: Dub an existing video with new audio

### Exporting your assets

<Frame background="subtle">
  ![Video export interface](file:62935d23-0501-4ac2-815e-81f08df03845)
</Frame>

Export finished assets by downloading them locally or sending them directly to Studio.

**Edit in Studio:** Import the asset directly into a Studio project.

**Download:** Save the asset to your local machine.


## Supported download formats

**Video:**

* **MP4**: Codecs H.264, H.265. Quality up to 4K (with upscaling)

**Image:**

* **PNG**: High-resolution, lossless output


## Models

Image & Video provides access to specialized models optimized for different use cases. Each model offers unique capabilities, from rapid iteration to production-ready quality.

Post-processing models require an existing generated output, though you can also upload your own image or video file.

<AccordionGroup>
  <Accordion title="Video generative models">
    <AccordionGroup>
      <Accordion title="OpenAI Sora 2 Pro">
        The most advanced, high-fidelity video model for cinematic results at your disposal.

        **Generation inputs:**

        * Text-to-Video
        * Start Frame

        **Features:**

        * Highest-fidelity, professional-grade output with synced audio
        * Precise multi-shot control
        * Excels at complex motion and prompt adherence
        * Fixed durations: 4s, 8s, and 12s
        * Batch creation with up to 4 generations at a time

        **Output options:**

        * Resolutions: 720p, 1080p
        * Aspect ratios: 16:9, 9:16

        **Ideal for:**

        * Cinematic, professional-grade video content

        **Cost:** Starts at 12,000 credits for a generation

        <Note>
          End frame is not currently supported. Cannot provide image references. Sound is enabled by default.
        </Note>
      </Accordion>

      <Accordion title="OpenAI Sora 2">
        The standard, high-speed version of OpenAI's advanced video model, tuned for everyday content creation.

        **Generation inputs:**

        * Text-to-Video
        * Start Frame

        **Features:**

        * Realistic, physics-aware videos with synced audio
        * Fine scene control
        * Fixed durations: 4s, 8s, and 12s
        * Batch creation with up to 4 generations at a time
        * Strong narrative and character consistency

        **Output options:**

        * Resolutions: 720p, 1080p
        * Aspect ratios: 16:9, 9:16

        **Ideal for:**

        * Everyday content creation with realistic physics

        **Cost:** Starts at 4,000 credits for default settings

        <Note>
          End frame is not currently supported. Cannot provide image references. Sound is enabled by default.
        </Note>
      </Accordion>

      <Accordion title="Google Veo 3.1">
        A professional-grade model for high-quality, cinematic video generation.

        **Generation inputs:**

        * Text-to-Video
        * Start Frame
        * End Frame
        * Image References

        **Features:**

        * Excellent quality and creative control with negative prompts
        * Fully integrated and synchronized audio
        * Realistic dialogue, lip-sync, and sound effects
        * Fixed durations: 4s, 6s, and 8s
        * Batch creation with up to 4 generations at a time
        * Dedicated sound control

        **Output options:**

        * Resolutions: 720p, 1080p
        * Aspect ratios: 16:9, 9:16

        **Ideal for:**

        * High-quality, cinematic video generation with full creative control

        **Cost:** Starts at 8,000 credits for default settings

        <Note>
          Enabling and disabling sound will change the generation credits.
        </Note>
      </Accordion>

      <Accordion title="Kling 2.5">
        A balanced and versatile model for high-quality, full-HD video generation.

        **Generation inputs:**

        * Text-to-Video
        * Start Frame

        **Features:**

        * Excels at simulating complex motion and realistic physics
        * Accurately models fluid dynamics and expressions
        * Fixed durations: 5s and 10s
        * Batch creation with up to 4 generations at a time

        **Output options:**

        * Resolutions: 1080p
        * Aspect ratios: 16:9, 1:1, 9:16

        **Ideal for:**

        * Realistic physics simulations and complex motion

        **Cost:** Starts at 3,500 credits for default settings

        <Note>
          End frame is not currently supported. Cannot provide image references. Sound control not available.
        </Note>
      </Accordion>

      <Accordion title="Google Veo 3.1 Fast">
        A high-speed model optimized for rapid previews and generations, delivering sharper visuals with lower latency.

        **Generation inputs:**

        * Text-to-Video
        * Start Frame
        * End Frame

        **Features:**

        * Advanced creative control with negative prompts and dedicated sound control
        * Fixed durations: 4s, 6s, and 8s
        * Batch creation with up to 4 generations at a time
        * Accurately models real-world physics for realistic motion and interactions

        **Output options:**

        * Resolutions: 720p, 1080p
        * Aspect ratios: 16:9, 9:16

        **Ideal for:**

        * Quick iteration and A/B testing visuals
        * Fast-paced social media content creation

        **Cost:** Starts at 4,000 credits for default settings
      </Accordion>

      <Accordion title="Google Veo 3">
        Production-ready model delivering exceptional quality, strong physics realism, and coherent narrative audio.

        **Generation inputs:**

        * Text-to-Video
        * Start Frame

        **Features:**

        * Advanced integrated "narrative audio" generation that matches video tone and story
        * Granular creative control with negative prompts and dedicated sound control
        * Fixed durations: 4s, 6s, and 8s
        * Batch creation with up to 4 generations at a time

        **Output options:**

        * Resolutions: 720p, 1080p
        * Aspect ratios: 16:9, 9:16

        **Ideal for:**

        * Final renders and professional marketing content
        * Short-form storytelling

        **Cost:** Starts at 8,000 credits for default settings
      </Accordion>

      <Accordion title="Google Veo 3 Fast">
        A high-speed, cost-efficient model for generating audio-backed video from text or a starting image.

        **Generation inputs:**

        * Text-to-Video
        * Start Frame

        **Features:**

        * Granular creative control with negative prompts and dedicated sound control
        * Fixed durations: 4s, 6s, and 8s
        * Batch creation with up to 4 generations at a time

        **Output options:**

        * Resolutions: 720p, 1080p
        * Aspect ratios: 16:9, 9:16

        **Ideal for:**

        * Rapid iteration and previews
        * Cost-effective content creation

        **Cost:** Starts at 4,000 credits for default settings
      </Accordion>

      <Accordion title="Seedance 1 Pro">
        A specialized model for creating dynamic, multi-shot sequences with large movement and action.

        **Generation inputs:**

        * Text-to-Video
        * Start Frame
        * End Frame

        **Features:**

        * Highly stable physics and seamless transitions between shots
        * Fixed durations: 3s, 4s, 5s, 6s, 7s, 8s, 9s, 10s, 11s, and 12s
        * Batch creation with up to 4 generations at a time
        * Maximum creative flexibility with numerous aspect ratio options

        **Output options:**

        * Resolutions: 480p, 720p, 1080p
        * Aspect ratios: 21:9, 16:9, 4:3, 1:1, 3:4, 9:16

        **Ideal for:**

        * Storytelling and action scenes requiring stable physics

        **Cost:** Starts at 4,800 credits for default settings

        <Note>
          Aspect ratio and resolution do not affect generation credits, but duration does.
        </Note>
      </Accordion>

      <Accordion title="Wan 2.5">
        A versatile model that delivers cinematic motion and high prompt fidelity from text or a starting image.

        **Generation inputs:**

        * Text-to-Video
        * Start Frame (Image-to-Video)

        **Features:**

        * Granular creative control with negative prompts and dedicated sound control
        * Fixed durations: 5s and 10s
        * Batch creation with up to 4 generations at a time

        **Output options:**

        * Resolutions: 480p, 720p, 1080p
        * Aspect ratios: 16:9, 1:1, 9:16

        **Ideal for:**

        * Cinematic content with strong prompt adherence

        **Cost:** Starts at 2,500 credits for default settings

        <Note>
          Generation cost varies based on selected settings.
        </Note>
      </Accordion>
    </AccordionGroup>
  </Accordion>

  <Accordion title="Image generative models">
    <AccordionGroup>
      <Accordion title="Google Nano Banana">
        A high-speed model for quick, high-quality image generation and editing directly from text prompts.

        **Features:**

        * Supports multiple image references to guide generation
        * Generates up to 4 images at a time

        **Output options:**

        * Aspect ratios: 21:9, 16:9, 5:4, 4:3, 3:2, 1:1, 2:3, 3:4, 4:5, 9:16

        **Ideal for:**

        * Rapid image creation and iteration

        **Cost:** Starts at 2,000 credits for default settings; varies based on number of generations
      </Accordion>

      <Accordion title="Seedream 4">
        A specialized image model for generating multi-shot sequences or scenes with large movement and action.

        **Features:**

        * Excels at creating images with stable physics and coherent transitions
        * Supports multiple image references to guide generation
        * Generates up to 4 images at a time

        **Output options:**

        * Aspect ratios: auto, 16:9, 4:3, 1:1, 3:4, 9:16

        **Ideal for:**

        * Action scenes and dynamic compositions

        **Cost:** Starts at 1,200 credits for default settings; varies based on number of generations
      </Accordion>

      <Accordion title="Flux 1 Kontext Pro">
        A professional model for advanced image generation and editing, offering strong scene coherence and style control.

        **Features:**

        * Image-based style control requiring a reference image to guide visual aesthetic
        * Generates up to 4 images at a time

        **Output options:**

        * Aspect ratios: 21:9, 16:9, 4:3, 3:2, 1:1, 2:3, 3:4, 4:5, 9:16, 9:21

        **Ideal for:**

        * Professional content with precise style requirements

        **Cost:** Starts at 1,600 credits; varies based on settings and number of generations
      </Accordion>

      <Accordion title="Wan 2.5">
        An image model with strong prompt fidelity and motion awareness, ideal for capturing dynamic action in a still frame.

        **Features:**

        * Granular control with negative prompts
        * Supports multiple image references to guide generation
        * Generates up to 4 images at a time

        **Output options:**

        * Aspect ratios: 16:9, 4:3, 1:1, 3:4, 9:16

        **Ideal for:**

        * Dynamic still images with motion awareness

        **Cost:** Starts at 2,000 credits; varies based on settings
      </Accordion>

      <Accordion title="OpenAI GPT Image 1">
        A versatile model for precise, high-quality image creation and detailed editing guided by natural language prompts.

        **Features:**

        * Supports multiple image references to guide generation
        * Generates up to 4 images at a time

        **Output options:**

        * Aspect ratios: 3:2, 1:1, 2:3
        * Quality options: low, medium, high

        **Ideal for:**

        * Creating and editing images with precise, text-based control

        **Cost:** Starts at 2,400 credits for default settings; varies based on settings and number of generations
      </Accordion>
    </AccordionGroup>
  </Accordion>

  <Accordion title="Lip-sync models">
    <AccordionGroup>
      <Accordion title="Omnihuman 1.5">
        A dedicated utility model for generating exceptionally realistic, humanlike lip-sync.

        **Inputs:**

        * Static source image
        * Speech audio file

        **Features:**

        * Animates the mouth on the source image to match provided audio
        * Creates high-fidelity "talking" video from still images
        * Lip-sync specific tool, not a full video generation model

        **Ideal for:**

        * Creating talking avatars
        * Adding dialogue to still images
        * Professional dubbing workflows

        **Cost:** Depends on generation input

        <Note>
          For best results, the image should contain a detectable figure.
        </Note>
      </Accordion>

      <Accordion title="Veed LipSync">
        A fast, affordable, and precise utility model for applying realistic lip-sync to videos.

        **Inputs:**

        * Source video
        * New speech audio file

        **Features:**

        * Re-animates mouth movements in source video to match new audio
        * Video-to-video lip-sync tool, not a full video generator

        **Ideal for:**

        * High-volume, cost-effective dubbing
        * Translating content
        * Correcting audio in video clips with realistic results

        **Cost:** Depends on generation input

        <Note>
          For best results, the video should contain a detectable figure.
        </Note>
      </Accordion>
    </AccordionGroup>
  </Accordion>

  <Accordion title="Upscaling model">
    <AccordionGroup>
      <Accordion title="Topaz Upscale">
        A dedicated utility model for image and video upscaling, designed to enhance resolution and detail up to 4x.

        **Features:**

        * Enhancement tool that processes existing media
        * Increases media size while preserving natural textures and minimizing artifacts
        * Highly granular upscale factors: 1x, 1.25x, 1.5x, 1.75x, 2x, 3x, 4x
        * Video-specific: Flexible frame rate control (keep source or convert to 24, 25, 30, 48, 50, or 60 fps)

        **Ideal for:**

        * Improving quality of generated media
        * Restoring legacy footage or photos
        * Preparing assets for high-resolution displays

        **Cost:** Depends on generation input
      </Accordion>
    </AccordionGroup>
  </Accordion>
</AccordionGroup>



# Studio

> Create professional video and audio content with our end-to-end production workflow

<img src="file:f197606a-b3c1-4243-bddb-0ad67345f1b8" alt="Studio timeline overview" />


## Overview

Studio provides an end‑to‑end workflow for creating video and audio content.

With Studio 3.0, you can now add a dedicated **timeline** with a **video track** and **captions** so you can build complete voiceovers. You can also layer **music** and **sound effects** on separate tracks, import external **audio**, and fine‑tune timing down to individual sentences. Once your project is ready for feedback, you can use our new **sharing** and **commenting** features to gather feedback from teammates.

Finally, you can **export** your work in various audio formats (per chapter or whole project) or as a video if a video track was included.

<Note>
  Studio supports our latest speech models, including v3. You can switch models at any time in
  **Project settings**.
</Note>


## Guide

<Frame background="subtle">
  ![Studio create](file:9242ca1a-eee7-47eb-8568-645de9b39fc9)
</Frame>

<Steps>
  <Step title="Create a new project">
    Select one of the starting options at the top of the Studio page.
  </Step>

  <Step title="Select settings">
    Follow the instructions in the pop-up and click 

    **Create**

    .
  </Step>

  <Step title="Enhance your project">
    Add **video**, **narration**, **music**, and **sound effects** to your project using our
    timeline editor.
  </Step>

  <Step title="Collaborate with others">
    Click the **Share** button to share your project and collect feedback from teammates.
  </Step>

  <Step title="Export your project">
    Click the **Export** button to export the project as audio or video.
  </Step>
</Steps>

<Note>
  You can use our [Audio Native](/docs/product-guides/audio-tools/audio-native) feature to easily
  and effortlessly embed any Studio audio project onto your website.
</Note>


## Starting options

Some settings are automatically selected by default when you create a new project.

The default model is Multilingual v2 for most new projects. You can also choose newer models, including v3, in **Project Settings**.

The quality setting is automatically selected depending on your subscription plan, and will not increase your credit usage.

For free, Starter and Creator subscriptions the quality will be 128 kbps MP3, or WAV generated from 128 kbps source.

For Pro, Scale, Business and Enterprise plans, the quality will be 16-bit, 44.1 kHz WAV, or 192 kbps MP3 (Ultra Lossless).

### Quick start

<AccordionGroup>
  <Accordion title="Upload">
    #### Upload

    Upload a file to start from existing media. We’ll analyze it and choose the best layout automatically: text or audio uploads open in the **audio** layout; video files open in the **video** layout with the timeline and **captions** available.
  </Accordion>

  <Accordion title="Start audio project from scratch">
    #### Start audio project from scratch

    Create a blank audio project and begin writing your script. Add **voices**, **music**, and **sound effects** later from the **timeline**.
  </Accordion>

  <Accordion title="Start video project from scratch">
    #### Start video project from scratch

    Create a blank video project with a **video track** ready to add footage, voiceover, and **captions**.
  </Accordion>
</AccordionGroup>

### Audio

<AccordionGroup>
  <Accordion title="New audiobook">
    #### New audiobook

    <Frame background="subtle">
      ![Create an audiobook](file:f1f1d42e-df62-44c8-a9a5-1bfdc82c3587)
    </Frame>

    You’ll see a pop‑up to upload a file; we’ll import it into your new project.

    You can upload EPUB, PDF, TXT, HTML, and DOCX files.

    You can also select a default voice and optionally enable **Auto‑assign voices** to detect characters and assign matching voices. This adds some processing time.
  </Accordion>

  <Accordion title="Create a podcast">
    #### Create a podcast

    <Frame background="subtle">
      ![Create a podcast](file:a7ba4f53-1f74-4923-beb4-9fbff6e15db3)
    </Frame>

    This option will use GenFM to automatically create a podcast based on an uploaded document, a webpage via URL, or an existing project.

    <Note>
      With this option, GenFM will generate a new script from your source. If you want to keep your script unchanged, use **New audiobook** or **Start audio project from scratch**.
    </Note>

    In the format settings, choose a conversation between a host and guest, or a more focused bulletin‑style podcast with a single host. You can also set the duration to short, default, or long.

    You can choose your own preferred voices for the host and guest, or go with our suggested voices.

    You can set the podcast language; if you don’t, it will match the language of the source material.

    Use the **cog** icon to open advanced configuration and specify up to three focus areas.
  </Accordion>

  <Accordion title="URL to audio">
    #### URL to audio

    <Frame background="subtle">
      ![Create an article](file:1f7156a4-7142-47b9-a0a2-e2427492ba67)
    </Frame>

    You’ll see a pop‑up to enter a URL; we’ll import the page text into your project.

    You can also select a default voice for your project and optionally enable **Auto‑assign voices** to detect characters and assign matching voices. This adds some processing time.
  </Accordion>

  <Accordion title="AI Script Generator">
    #### AI Script Generator

    Describe what you want and let the AI draft a script for you. Review the script, make edits, and start a new audio project from it.
  </Accordion>
</AccordionGroup>

### Video

<AccordionGroup>
  <Accordion title="New video voiceover">
    #### New video voiceover

    Create a project optimized for video voiceovers. Import your video, transcribe or generate narration, and enable **captions** with a chosen template.
  </Accordion>

  <Accordion title="Enhance your video">
    #### Enhance your video

    Upload a video and let Studio suggest fitting **music** and **sound effects**. Tweak the mix on the **timeline**.
  </Accordion>

  <Accordion title="Add captions">
    #### Add captions

    Open the **Captions** tab by default to transcribe narration or imported audio, then style captions with templates and positioning.
  </Accordion>

  <Accordion title="Remove background noise">
    #### Remove background noise

    Upload a video and reduce background noise in the audio track. Proceed to add voiceover, music, and SFX as needed.
  </Accordion>

  <Accordion title="Fix voiceover mistakes">
    #### Fix voiceover mistakes

    Upload a video and we’ll automatically transcribe the audio, flag potential misreads or timing issues, and help correct them with targeted speech regeneration.
  </Accordion>

  <Accordion title="AI Soundtrack Generator">
    #### AI Soundtrack Generator

    Automatically generate music that matches your video’s mood and pacing, then place it on a dedicated music track.
  </Accordion>
</AccordionGroup>


## Generating and Editing

Once you've added content, either by importing it or creating it yourself, you can use the **Export**
button to render your chapter or project in one step. Narration will be generated where needed, and the output will be audio or video depending on your tracks and settings.

<Frame background="subtle">
  ![Export your project](file:7098f9dc-4e85-4f4e-8f43-30b9f647b1e4)
</Frame>

This will automatically generate and download an audio or video file, but you can still edit your project after this.

Once you've finished editing, you will need to use the **Export** button again to generate and download a new
version of your project that includes the updated media.

<AccordionGroup>
  <Accordion title="Timeline and tracks">
    #### Timeline and tracks

    <Frame background="subtle">
      ![Studio timeline editing](file:1914463e-b2c2-4145-a905-4b7afb9c6c6e)
    </Frame>

    The **timeline** gives you a chapter‑wide view of your project so you can see narration, music, SFX, and video at a glance.

    You can **adjust timing** between paragraphs and even individual sentences, **trim** clip edges, **split** and **duplicate** clips to iterate quickly, and **zoom** or **pan** to navigate longer chapters. **Waveforms** help you visualize loudness so you can align levels precisely across tracks.
  </Accordion>

  <Accordion title="Contextual sidebar">
    #### Contextual sidebar

    <Frame background="subtle">
      ![Contextual sidebar](file:61969884-89a9-4452-b5e6-b796bc11d0ad)
    </Frame>

    The Contextual sidebar shows tools and details for the currently selected item in your project.
    For narration, you'll see **voice** and **delivery** controls; for media clips (audio, music, SFX,
    or video), you'll see relevant **clip properties** and actions.
  </Accordion>

  <Accordion title="Chapters sidebar">
    #### Chapters sidebar

    When you create a Studio project using the **Create an audiobook** option and import a document that includes chapters, chapters will be automatically enabled for your project. You can toggle the visibility of the Chapters sidebar by clicking **Chapters**.

    <Frame background="subtle">
      ![Studio chapters toggle](file:fe1c195e-76e9-4989-a650-c66d54355456)
    </Frame>

    If you want to add a new chapter, you can do this using the **+** button at the top of the Chapters
    sidebar.

    If you used the **Start from scratch** option to create your project, or your project didn't originally include chapters, you'll need to enable chapters in **Project settings**. You will find the **Enable chapters** toggle in the general settings.

    <Frame background="subtle">
      ![Enable chapters](file:67d16775-e530-4735-a7ed-15b68b21689e)
    </Frame>

    Once you've enabled chapters, you can click **+ Chapter** to add a new chapter to your project. After you've added one chapter, the Chapters sidebar will be enabled, and you can use the **+** button to add additional chapters.
  </Accordion>

  <Accordion title="Generate/Regenerate">
    #### Generate/Regenerate

    <Frame background="subtle">
      ![Generate/Regenerate](file:719c589e-d31c-4cb0-baf9-d8169c5e4f81)
    </Frame>

    The **Generate** button will generate audio if you have not yet generated audio for the selected
    text, or will generate new audio if you have already generated audio. This will cost credits.

    If you have made changes to the paragraph such as changing the text or the voice, then the paragraph
    will lose its converted status, and will need to be generated again.

    The status of a paragraph (converted or unconverted) is indicated by the bar to the left of the paragraph.
    Unconverted paragraphs have a pale grey bar while converted paragraphs have a dark grey bar.

    If the button says **Regenerate**, then this means that you won't be charged for the next generation.
    You're eligible for two free regenerations provided you don't change the voice or the text.

    This action applies to narration and other generated speech. Timeline items like video, external audio, music, SFX, and captions are arranged on the timeline and rendered when you export.
  </Accordion>

  <Accordion title="Play">
    #### Play

    <Frame background="subtle">
      ![Play button](file:0020bd80-f7c7-477c-8738-a2bfdff716a9)
    </Frame>

    You can use the **Play** button in the player at the bottom of the Studio interface to play audio
    that has already been generated, or generate audio if a paragraph has not yet been converted.
    Generating audio will cost credits. If you have already generated audio, then the **Play** button
    will play the audio that has already generated and you won't be charged any credits. There are two
    modes when using the **Play** button. **Until end** will play existing audio, or generate new
    audio for paragraphs that have not yet been generated, from the selected paragraph to the end of
    the current chapter. **Selection** will play or generate audio only for the selected paragraph.
    When a video track is present, the player also previews video in sync with the playhead. Playing
    existing audio or video never consumes credits; only generating narration does.
  </Accordion>

  <Accordion title="Generation history">
    #### Generation history

    <Frame background="subtle">
      ![Generation History
      button](file:9022122e-a13f-4e16-8926-f15e7c076d05)
    </Frame>

    If you click the **Generation history** button, this will show all the previously generated audio
    for the selected paragraph. This allows you to listen to and download each individual generation.

    <Frame background="subtle">
      ![Generation History](file:a3257612-ea2d-4367-aca8-fe1487de9282)
    </Frame>

    If you prefer an earlier version of a paragraph, you can restore it to that previous version.
    You can also remove generations, but be aware that if you
    remove a version, this is permanent and you can't restore it.

    Generation history applies to narration generations. It doesn't track imported media (external audio, music, SFX) or video clips.
  </Accordion>

  <Accordion title="Undo and Redo">
    #### Undo and Redo

    <Frame background="subtle">
      ![Undo and Redo](file:3ca711e3-71a1-4229-8bae-9849795cd69e)
    </Frame>

    If you accidentally make a change, you can use the **Undo** button to restore the previous
    version, and the **Redo** button to restore the change.
  </Accordion>

  <Accordion title="Breaks">
    #### Breaks

    <Frame background="subtle">
      ![Breaks](file:323d3863-a2f1-40f6-9863-2a22b84d3c6d)
    </Frame>

    You can add a pause by using the **Insert break** button. This inserts a break tag. By default, this will be set to 1 second, but you can change the length of the break up to a maximum of 3 seconds.

    <Note>
      For precise timing, prefer the timeline with trimming and sentence‑level control. Some newer models may
      reduce or ignore break tags in favor of natural flow.
    </Note>

    Breaks affect generated speech delivery only; they don't move or pause other timeline tracks. Use the timeline to create precise pauses across music, SFX, and video.
  </Accordion>

  <Accordion title="Actor Mode">
    #### Actor Mode

    <Frame background="subtle">
      ![Actor Mode](file:e9757604-c7e3-4639-9f02-038d6c6545a4)
    </Frame>

    Actor Mode allows you to specify exactly how you would like a section of text to be delivered by uploading a recording, or by recording yourself directly. You can either highlight a selection of text that you want to work on, or select a whole paragraph. Once you have selected the text you want to use Actor Mode with, click the **Actor Mode** button, and the Actor Mode pop-up will appear.

    For an overview of Actor Mode, see [this video](https://www.youtube.com/watch?v=Kj2dgXITrPw).

    <Frame background="subtle">
      ![Actor Mode pop-up](file:8a820a43-05f5-496c-bd2e-afcd034f8546)
    </Frame>

    Either upload or record your audio, and you will then see the option to listen back to the audio or remove it. You will also see how many credits it will cost to generate the selected text using the audio you've provided.

    <Frame background="subtle">
      ![Actor Mode pop-up](file:9dda95be-15f7-461e-8a98-b82d76e849f2)
    </Frame>

    If you're happy with the audio, click **Generate**, and your audio will be used to guide the delivery of the selected text.

    <Note>
      Actor Mode will replicate all aspects of the audio you provide, including the accent.
    </Note>
  </Accordion>

  <Accordion title="Video track and voiceovers">
    #### Video track and voiceovers

    <Frame background="subtle">
      ![Studio video track](file:14795a44-7223-4bc9-b900-d8bf9f5f266d)
    </Frame>

    Add a **video track** to voice over existing footage or to pair narration with b‑roll. Import a video file or add a blank track, then align the narration to key visual beats on the timeline. When needed, enable **captions** and choose a **template** to match your style.
  </Accordion>

  <Accordion title="Captions">
    #### Captions

    <Frame background="subtle">
      ![Studio caption templates](file:e5d37558-8888-4186-ada7-fd51b5d9890d)
    </Frame>

    Convert narration into styled **captions** for accessibility and engagement. Captions are generated automatically and can be customized with **templates** for colors, fonts, and placement. Edit text and timing directly on the **timeline** to correct any mismatches, then export your video with **burned‑in captions**.
  </Accordion>

  <Accordion title="External audio">
    #### External audio

    **Import** your own audio files—such as dialogue, stingers, or ambience—and mix them with narration, music, and SFX. Drag files into the **timeline** or use the import action, then **trim**, **split**, **duplicate**, and adjust clip volume as needed. **Stereo** files remain stereo on export.

    <Frame background="subtle">
      ![Insert audio](file:61b8e827-7a56-4f1f-a66c-cda6c25b97cd)
    </Frame>
  </Accordion>

  <Accordion title="Music">
    #### Music

    Generate **music** directly in Studio and place it on its own track in the timeline. Create new songs from **prompts** (choose a vibe and length) or **import** existing tracks. Music clips can be **trimmed**, **duplicated**, and moved to match the narration, and you can adjust **volume** per clip. When the source is **stereo**, stereo is preserved.

    <Frame background="subtle">
      ![Insert music](file:90f8534c-885d-4991-8690-d0b14135c5ea)
    </Frame>
  </Accordion>

  <Accordion title="Sound effects">
    #### Sound effects

    <Frame background="subtle">
      ![Insert sound effect](file:cba3330b-81a4-4842-b232-24759bf0823b)
    </Frame>

    Add **sound effects** as separate clips on the timeline. You can position them anywhere, layer multiple effects, and adjust their timing precisely with trimming and duplication.

    You can create effects from a text prompt inside Studio or browse and insert items from the **SFX library**.

    You can regenerate previews to explore variants and then apply your chosen effect to the timeline. Deleting and duplicating SFX clips works the same as other timeline clips.

    <Note>
      Sound effects are not supported in ElevenReader exports, or when streaming the project using the Studio API.
    </Note>
  </Accordion>

  <Accordion title="Lock paragraph">
    #### Lock paragraph

    <Frame background="subtle">
      ![Lock paragraph Button](file:ec787181-7c5f-489a-81e3-e6dfc6111288)
    </Frame>

    Once you're happy with the performance of a paragraph, you can use the **Lock paragraph** button
    to prevent any further changes.

    <Frame background="subtle">
      ![Locked paragraph](file:2086372d-a01d-4925-a6e8-90d91fbfcfee)
    </Frame>

    Locked paragraphs are indicated by a lock icon to the left of the paragraph. If you want to unlock
    a paragraph, you can do this by clicking the **Lock paragraph** button again. Locking applies to
    narration content; you can continue editing timeline clips like video, music, and SFX.
  </Accordion>

  <Accordion title="Keyboard shortcuts">
    #### Keyboard shortcuts

    <Frame background="subtle">
      ![Keyboard Shortcuts](file:c1b4bdcb-a9bf-4155-86a1-6052d164e210)
    </Frame>

    There are a range of keyboard shortcuts that can be used in Studio to speed up your workflow. To
    see a list of all available keyboard shortcuts, click the **Project options** button, then select
    **Keyboard shortcuts**.
  </Accordion>
</AccordionGroup>


## Settings

<AccordionGroup>
  <Accordion title="Voices">
    ### Voices

    We offer many types of voices, including the curated Default Voices library; completely synthetic voices created using our Voice Design tool; and you can create your own collection of cloned voices using our two technologies: Instant Voice Cloning and Professional Voice Cloning. Browse through our voice library to find the perfect voice for your production.

    Not all voices are equal, and a lot depends on the source audio used to create that voice. Some voices will perform better than others, while some will be more stable than others. Additionally, certain voices will be more easily cloned by the AI than others, and some voices may work better with one model and one language compared to another. All of these factors are important to consider when selecting your voice.

    If you’re unhappy with a voice, but you’re happy with the delivery of the narration, you can use our Voice Changer functionality to change the voice, but preserve the narration

    [Learn more about voices](/docs/capabilities/voices)
  </Accordion>

  <Accordion title="Voice settings">
    ### Voice settings

    <Frame background="subtle">
      ![Studio voice settings](file:dc629ff3-f288-4b5b-a397-27e958ae325e)
    </Frame>

    Our users have found different workflows that work for them. The most common setting is stability around 50 and similarity near 75, with minimal changes thereafter. Of course, this all depends on the original voice and the style of performance you're aiming for.

    It's important to note that the AI is non-deterministic; setting the sliders to specific values won't guarantee the same results every time. Instead, the sliders function more as a range, determining how wide the randomization can be between each generation.

    If you have a paragraph or text selected, you can use the **Override settings** toggle to change the settings for just the current selection. If you change the settings for the voice without enabling this, then this will change the settings for this voice across the whole of your project. This will mean that you will need to regenerate any audio that you had previously generated using different settings. If you have any locked paragraphs that use this voice, you won't be able to change the settings unless you unlock them.

    #### Alias

    You can use this setting to give the voice an alias that applies only for this project. For example, if you're using a different voice for each character in your audiobook, you could use the character's name as the alias.

    #### Volume

    If you find the generated audio for the voice to be either too quiet or too loud, you can adjust the volume. The default value is 0.00, which means that the audio will be unchanged. The minimum value is -30 dB and the maximum is +5 dB.

    #### Speed

    The speed setting allows you to either speed up or slow down the speed of the generated speech. The default value is 1.0, which means that the speed is not adjusted. Values below 1.0 will slow the voice down, to a minimum of 0.7. Values above 1.0 will speed up the voice, to a maximum of 1.2. Extreme values may affect the quality of the generated speech.

    #### Stability

    The stability slider determines how stable the voice is and the randomness between each generation. Lowering this slider introduces a broader emotional range for the voice. This is influenced heavily by the original voice. Setting the slider too low may result in odd performances that are overly random and cause the character to speak too quickly. On the other hand, setting it too high can lead to a monotonous voice with limited emotion.

    For a more lively and dramatic performance, it is recommended to set the stability slider lower and generate a few times until you find a performance you like.

    On the other hand, if you want a more serious performance, even bordering on monotone at very high values, it is recommended to set the stability slider higher. Since it is more consistent and stable, you usually don't need to generate as many samples to achieve the desired result. Experiment to find what works best for you!

    #### Similarity

    The similarity slider dictates how closely the AI should adhere to the original voice when attempting to replicate it. If the original audio is of poor quality and the similarity slider is set too high, the AI may reproduce artifacts or background noise when trying to mimic the voice if those were present in the original recording.

    #### Style exaggeration

    With the introduction of the newer models, we also added a style exaggeration setting. This setting attempts to amplify the style of the original speaker. It does consume additional computational resources and might increase latency if set to anything other than 0. It's important to note that using this setting has shown to make the model slightly less stable, as it strives to emphasize and imitate the style of the original voice.

    In general, we recommend keeping this setting at 0 at all times.

    #### Speaker boost

    This setting boosts the similarity to the original speaker. However, using this setting requires a slightly higher computational load, which in turn increases latency. The differences introduced by this setting are generally rather subtle.
  </Accordion>

  <Accordion title="Pronunciation dictionaries">
    ### Pronunciation dictionaries

    <Frame background="subtle">
      ![Studio pronunciation dictionaries](file:45f3ddc6-6d37-4a22-a5d2-cafce235a4e7)
    </Frame>

    Sometimes you may want to specify the pronunciation of certain words, such as character or brand names, or specify how acronyms should be read. Pronunciation dictionaries allow this functionality by enabling you to upload a lexicon or dictionary file that includes rules about how specified words should be pronounced, either using a phonetic alphabet (phoneme tags) or word substitutions (alias tags).

    <Note>
      Phoneme tags are only compatible with "Eleven Flash v2", "Eleven Turbo v2" and "Eleven English v1"
      [models](/docs/models).
    </Note>

    Whenever one of these words is encountered in a project, the AI will pronounce the word using the specified replacement. When checking for a replacement word in a pronunciation dictionary, the dictionary is checked from start to end and only the first replacement is used.

    Existing pronunciation dictionaries can be connected to your project from the Pronunciations Editor. You can open this from the toolbar. Find the dictionary you want to connect in the drop down menu and select **Connect**.

    You can create a new pronunciation dictionary from your project by creating an entry in the Pronunciations Editor, or you can upload or create a pronunciation dictionary from **Open all pronunciation dictionaries** in the Pronunciations Editor. You can then select **Connect** to connect the pronunciation dictionary to the current project.

    For more information on pronunciation dictionaries, please see our [prompting best practices guide](/docs/best-practices/prompting#pronunciation-dictionaries).
  </Accordion>

  <Accordion title="Export settings">
    ### Export settings

    Within the **Export** tab under **Project settings** you can add additional metadata such as Title, Author, ISBN and a Description to your project. This information will automatically be added to the downloaded audio files. You can also access previous versions of your project, and enable volume normalization. These settings apply to audio exports; video appearance is controlled by your timeline and caption templates.
  </Accordion>
</AccordionGroup>


## Exporting and Sharing

When you're happy with your chapter or project, use the **Export** button to generate a downloadable version. If you've already generated audio for every paragraph in either your chapter or project, you won't be charged any additional credits to export. If there are any paragraphs that do need converting as part of the export process, you will see a notification of how many credits it will cost to export.

<AccordionGroup>
  <Accordion title="Export options">
    #### Export options

    If your project only has one chapter, you will just see the option to export as either MP3 or WAV (audio), or as video when a video track/captions are present.

    If your project has multiple chapters, you will have the option to export each chapter individually, or export the full project. If you're exporting the full project, you can either export as a single file, or as a ZIP file containing individual files for each chapter. You can also choose whether to download as MP3 or WAV for audio‑only exports.

    For video exports, enable captions and add a video track (or shareable TTS video) before exporting. Video is rendered with your selected caption template.
  </Accordion>

  <Accordion title="Quality setting">
    #### Quality setting

    The quality of the export depends on your subscription plan. For newly created projects, the quality will be:

    * Free, Starter and Creator: 128 kbps MP3, or WAV converted from 128 kbps source.
    * Pro, Scale, Business and Enterprise plans: 16-bit, 44.1 kHz WAV, or 192 kbps MP3 (Ultra Lossless).

    <Note>
      If you have an older project, you may have set the quality setting when you created the project, and this can't be changed. You can check the quality setting for your project in the Export menu by hovering over **Format**
    </Note>
  </Accordion>

  <Accordion title="Downloading">
    #### Downloading

    Once your export is ready, it will be automatically downloaded. For shareable TTS videos, you can also copy a link for quick sharing.

    You can access and download all previous exports, of both chapters and projects, by clicking the **Project options** button and selecting **Exports**.
  </Accordion>

  <Accordion title="Sharing">
    #### Sharing

    From the editor, create a **read‑only link** so others can play your timeline and review your mix without downloading files. You can revoke access at any time. **Commenting** is available at launch, including anonymous comments.

    <Frame background="subtle">
      ![Studio share project](file:32e86d16-5dcd-4763-a6aa-8fac52bed5d7)
    </Frame>
  </Accordion>

  <Accordion title="Commenting">
    #### Commenting

    Invite collaborators or your audience to leave feedback directly on the timeline. Comments are timestamped to the playhead so feedback appears exactly where it’s relevant. Commenters don’t need an ElevenLabs account and can leave a name or post anonymously. Discussions stay organized with **threaded replies** and optional **mentions** of collaborators.

    To add a comment, open a shared project link (or the editor with sharing enabled), move the playhead to the right moment, and click **Add comment**. Type your message and post; use **Reply** to continue the thread. You’ll receive **email notifications** when there’s a new comment or reply in a thread you started or participated in.

    When feedback is addressed, mark the thread as **Resolved**; it will collapse in the list and can be reopened later. Resolving a thread pauses further notifications until it is reopened.
  </Accordion>
</AccordionGroup>


## FAQ

<AccordionGroup>
  <Accordion title="Free regenerations">
    <Frame background="subtle">
      ![Studio free regenerations](file:d6cd6433-14cf-48b0-b520-1a35572e7707)
    </Frame>

    In Studio, provided you don't change the text or voice, you can regenerate a selected paragraph or section of text twice for free.

    If free regenerations are available for the selected paragraph or text, you will see **Regenerate**. If you hover over the **Regenerate** button, the number of free regenerations remaining will be displayed.

    Once your free regenerations have been used, the button will display **Generate**, and you will be charged for subsequent generations.
  </Accordion>

  <Accordion title="Auto-regeneration for bulk conversions">
    When using **Export** to generate audio for a full chapter or project, auto-regeneration automatically checks the output for volume issues, voice similarity, and mispronunciations. If any issues are detected, the tool will automatically regenerate the audio up to twice, at no extra cost.

    This feature may increase the processing time but helps ensure higher quality output for your bulk conversions.
  </Accordion>
</AccordionGroup>



# Music

> Generate and edit custom songs in any style using AI-powered music creation tools

<img src="file:385048f1-e2d3-43f7-9b3d-ecb6e78b7255" alt="Music product feature" />


## Overview

Eleven Music offers an end-to-end workflow for music creation. Generate songs in any style, at your desired length,
and refine every detail with intuitive editing tools. Once complete, export your track as a high-fidelity MP3 audio file,
ready for professional use.


## Guide

<Steps>
  <Step title="Create a new song">
    Describe your song using natural language prompts. Refer to our [Prompting
    Guide](/docs/best-practices/prompting/eleven-music) for best practices on style and lyrics.
  </Step>

  <Step title="Select settings">
    Choose the number of **Variants** and the **Duration**. You can select a fixed length (e.g.,
    30s, 1m) or **Auto** for a dynamically determined length. For building complex songs, a workflow
    we've seen often is to start with a short duration like **30s** and iteratively adding new
    sections as you work on the song.
  </Step>

  <Step title="Make edits">
    Refine your track in the editor. You can edit lyrics, add or remove sections, adjust section
    durations, apply style keywords, or use direct conversational prompts for granular creative
    control. You can even generate completely new variations of the exact same prompt if you want a
    different track based on the same prompt in the same music project, or a different base to work
    from.
  </Step>

  <Step title="Download and share">
    Click the **Download** button to save your high-fidelity audio file, or use the **Share** button
    to generate a link with a customizable visualizer for your track.
  </Step>
</Steps>


## What can I generate with Eleven Music?

Eleven Music is a versatile model that gives you control over many aspects of music creation. You can generate:

<AccordionGroup>
  <Accordion title="Full Songs with Vocals">
    #### Full Songs with Vocals

    Create complete tracks with AI-generated lyrics and vocals in
    multiple languages including English, Spanish, German, and Japanese. The model understands
    nuanced prompts and can generate songs in most styles or genres.
  </Accordion>

  <Accordion title="Instrumental Tracks">
    #### Instrumental Tracks

    Generate purely instrumental music across any genre, from cinematic
    scores to ambient lo-fi beats. Perfect for background music, film scores, or any project
    requiring instrumental accompaniment.
  </Accordion>

  <Accordion title="Specific Song Structures">
    #### Specific Song Structures

    Use sectional descriptions in your prompt to build songs piece by
    piece, defining the Intro, Verse, Chorus, Breakdown, and Outro. This gives you granular control
    over your song's composition and flow.
  </Accordion>

  <Accordion title="Music for Media">
    #### Music for Media

    Design custom soundtracks for videos, advertisements, games, or other media
    by describing the scene or mood. For example: "A high-intensity orchestral track for an epic
    battle scene" or "Upbeat corporate jingle for a tech startup."
  </Accordion>

  <Accordion title="Genre-Specific Music">
    #### Genre-Specific Music

    Generate highly specific styles by including detailed prompts, such as
    "Traditional Spanish flamenco with palmas, nylon guitar, and Spanish-language vocals" or "1980s
    synthwave with analog synthesizers and retro drum machines."
  </Accordion>
</AccordionGroup>


## Editing and Refinement

Once you've generated your initial track, Eleven Music provides powerful editing tools to refine every aspect
of your composition.

<AccordionGroup>
  <Accordion title="Adding and Removing Sections">
    #### Adding and Removing Sections

    **Adding a New Section:**

    * To insert a section between existing ones, hover over the section in the section view and click the
      **"+ Add Section"** icon that appears. This will add a section after the current section.
    * To add a section at the end of your track, scroll to the end of the timeline and click the **"+"** button.
    * Drag the new section in the timeline to adjust its duration.

    **Removing a Section:**

    * Hover over the section you wish to remove in the song structure view.
    * Click the delete icon (X) that appears in the corner of the section block.
  </Accordion>

  <Accordion title="Editing Lyrics and Prompts">
    #### Editing Lyrics and Prompts

    To change the lyrics or instrumental prompts of any existing section:

    * Click inside the text box for that section (e.g., Intro, Main Theme).
    * Type your new lyrics or edit the existing prompt.
    * Use bracketed descriptions like "\[energetic guitar solo]" or "\[drum fill]" for instrumental parts.
  </Accordion>

  <Accordion title="Style Control">
    #### Style Control

    For advanced control over specific musical elements:

    * Hover over the section you want to edit and click **"Edit styles of this section"**.
    * In the "Section styles" window, you can:
      * **Include styles:** Add specific musical characteristics like "gradual filter cutoff",
        "hi-hats fade out", or "long delay feedback on vocals."
      * **Exclude styles:** Prevent certain elements like "abrupt ending" or "new elements."
    * Click **Save** to apply these style rules to that specific section.
  </Accordion>

  <Accordion title="Direct Prompting">
    #### Direct Prompting

    Use the conversation interface at the bottom of the editor to make specific changes with natural language:

    * Type direct instructions like "Make the chorus more energetic" or "Add a guitar solo after the second verse."
    * This allows for creative editing beyond the structured tools.
  </Accordion>

  <Accordion title="Regenerating Changes">
    #### Regenerating Changes

    After making any edits—whether adding, deleting, or modifying sections—your changes are staged but not yet applied to the audio.

    * Your edits will **not** take effect until you click the **Generate** button.
    * Once you click **Generate**, the model creates a new version of the song incorporating all your changes.
    * Feel free to experiment with different combinations of lyrics, styles, and structures between generations.
  </Accordion>
</AccordionGroup>


## Best Practices for Prompting

The key to great results is a descriptive and detailed prompt. The more information you provide, the closer the output will be to your vision.

<AccordionGroup>
  <Accordion title="Be Specific with Genre and Style">
    #### Be Specific with Genre and Style

    Instead of generic terms like "rock music," try detailed descriptions:

    * "Energetic 1980s synth-pop with a driving drum machine beat and male vocals"
    * "Melancholic indie folk with fingerpicked acoustic guitar and ethereal female harmonies"
    * "Heavy metal with palm-muted riffs, double bass drums, and aggressive vocals"
  </Accordion>

  <Accordion title="Layer Multiple Descriptors">
    #### Layer Multiple Descriptors

    Combine mood, instrumentation, tempo, and use case for better results:

    * "A slow, melancholic piano melody over ambient synth textures, suitable for a tragic film scene"
    * "Upbeat corporate jingle with bright synthesizers, punchy drums, and an optimistic melody"
    * "Dark, atmospheric electronic track with deep bass, glitchy percussion, and haunting vocal samples"
  </Accordion>

  <Accordion title="Define Instrumentation">
    #### Define Instrumentation

    Call out specific instruments you want to hear:

    * "Upbeat funk track with a prominent slap bass line, funky rhythm guitar, and a horn section"
    * "Classical string quartet with violin, viola, and cello"
    * "Jazz ensemble with piano, upright bass, brushed drums, and tenor saxophone"
  </Accordion>

  <Accordion title="Use Include/Exclude Styles">
    #### Use Include/Exclude Styles

    Refine your output by explicitly including or excluding certain elements at the track or section level:

    * **Include:** "acoustic," "four-on-the-floor kick", "reverb-heavy vocals", "analog warmth"
    * **Exclude:** "repetitive structure", "electronic elements", "abrupt ending", "distorted vocals"
  </Accordion>

  <Accordion title="Build Section by Section">
    #### Build Section by Section

    For maximum control, start with a short generation (e.g., 30 seconds for an Intro)
    and build your song piece by piece.

    1. Generate the **Intro** and refine until satisfied.
    2. Click **"+ Add Section"** to add the next part.
    3. Specify the style and content for the new section (e.g., Verse, Chorus, Bridge).
    4. Use the conversation interface for specific instructions on each part.
    5. Build your track progressively, ensuring each section flows naturally.
  </Accordion>

  <Accordion title="Iterate and Refine">
    #### Iterate and Refine

    Don't start over if the first generation isn't perfect. Small changes can have a big impact.

    * Adjust your prompt and regenerate specific sections.
    * Use the editing tools to fine-tune individual parts.
    * Experiment with different style combinations.
  </Accordion>
</AccordionGroup>


## Use Cases & Commercial Use

Created in collaboration with artists, labels, and publishers, Eleven Music is, under certain subscriptions and conditions,
**cleared for broad commercial use**. This model allows users to move beyond stock music libraries and create bespoke audio
tailored to their specific needs.

<Note>
  For specific details on supported usage per tier, please refer to our [Music
  Terms](https://elevenlabs.io/music-terms).
</Note>


## Export and Quality

When you're satisfied with your composition, use the **Download** button to export your track.

<AccordionGroup>
  <Accordion title="Export Formats">
    #### Export Formats

    Generated audio is provided in MP3 format with professional-grade quality (44.1kHz, 128-192kbps).
    Other audio formats will be supported soon.
  </Accordion>

  <Accordion title="Quality Settings">
    #### Quality Settings

    Export quality varies by subscription tier:

    * **Free, Starter, and Creator:** Standard quality exports.
    * **Pro, Scale, Business, and Enterprise:** High-fidelity, studio-grade exports.
      All exports maintain the full dynamic range and frequency response of the original generation.
  </Accordion>

  <Accordion title="Sharing">
    #### Sharing

    Use the **Share** button to:

    * Generate a shareable link to your song.
    * Customize the visualizer that accompanies your track.
    * Share your creations with collaborators or audiences.
  </Accordion>
</AccordionGroup>


## Availability & API Access

Eleven Music is available today for all users on the ElevenLabs website. The intuitive interface makes it easy to create professional-quality music without technical expertise.

**API Access:** Public API access is coming soon. Please [reach out](https://elevenlabs.io/eleven-music-api-request) to request early access.

<Note>
  Visit our [Music Product Page](https://elevenlabs.io/music) for the latest information and to
  start creating.
</Note>


## FAQ

<AccordionGroup>
  <Accordion title="How is music generation cost calculated?">
    The cost for generating music is calculated upfront based on your selected settings (like duration)
    and is shown next to the Generate button. Unlike other ElevenLabs tools with fixed credit pricing,
    the number of credits used can vary depending on your subscription plan. This is because the cost
    is based on a fixed fiat price, which translates to a different number of credits for each plan.

    When using the **Auto** duration setting, the cost is fixed for that generation attempt, regardless
    of the final length of the song. This means a 2-minute song generated on "Auto" costs the same as a
    3-minute one, providing predictable upfront pricing.
  </Accordion>

  <Accordion title="How long can my generated songs be?">
    You can create everything from short clips to full-length tracks. For maximum control, you can
    start with a short duration like **30s** to create an initial section, then iteratively use the
    **"+ Add Section"** button to build out your song piece by piece, extending it to your desired
    length.

    The minimum duration of a song is 10 seconds and the maximum is 5 minutes.
  </Accordion>

  <Accordion title="Can I use generated music commercially?">
    Eleven Music is cleared for broad commercial use. See our [Music
    Terms](https://elevenlabs.io/music-terms) for specific usage details per subscription tier.
  </Accordion>

  <Accordion title="What languages are supported for vocals?">
    Eleven Music supports vocals in multiple languages including English, Spanish, German, and
    Japanese. The model can generate lyrics in these languages, or you can provide your own lyrics for
    the AI to sing.
  </Accordion>

  <Accordion title="Can I edit specific parts of my song after generation?">
    You can edit individual sections, modify lyrics, adjust durations, add or remove sections, and fine-tune
    the style of specific parts. Changes take effect when you click **Generate** to create a new version.
  </Accordion>

  <Accordion title="How do I get the best results?">
    The key is detailed, specific prompting. Include genre, mood, instrumentation, tempo, and use case in your
    descriptions. Use the Include/Exclude styles feature for fine control, and build songs section by section for
    maximum precision. See our [Prompting Guide](/docs/best-practices/prompting/eleven-music) for comprehensive tips.
  </Accordion>
</AccordionGroup>



# Dubbing

> Translate audio and video files with ElevenLabs dubbing and dubbing studio.

<img src="file:625ec98a-7cea-4017-97e8-877213130805" alt="Dubbing studio product feature" />

**Dubbing** allows you to translate content across 29 languages in seconds with voice translation, speaker detection, and audio dubbing.

Automated Dubbing or Video Translation is a process for translating and replacing the original audio of a video with a new language, while preserving the unique characteristics of the original speakers' voices.

We offer two different types of Dubbing: Automatic and Studio.

**Automatic Dubbing** is the default, so let’s see the step by step for this type of dubbing.

<Frame background="subtle">
  ![Dubbing new project](file:4a001c85-d12b-4f53-8928-9ebe7b28ec1d)
</Frame>

### Step by step for Automatic Dubbing

1. Go to the Dubbing Studio in your Navigation Menu.
2. Enter the dub name and select the original and target languages.
3. Upload a video/audio file or import one via URL (YouTube, TikTok, etc.).
4. Opt for watermarking if needed.
5. Leave the Create a Dubbing Studio project box unchecked.
6. Click on the **Advanced Settings** option:
   * Choose the number of speakers and video resolution.
   * Select the specific range for dubbing if needed.
7. Click on **Create** and sit back while ElevenLabs does its magic.

**Exercise**: Dub the video found [here](https://www.youtube.com/watch?v=WnNFZt0qjD0) from English to Spanish (or a language of your choosing). Select 6 speakers and keep the watermark.

<CardGroup>
  <Card title="API reference" href="/docs/api-reference/text-to-voice">
    See the API reference for dubbing.
  </Card>

  <Card title="Example app" href="https://github.com/elevenlabs/elevenlabs-examples/tree/main/examples/dubbing">
    A Python flask example app for dubbing.
  </Card>
</CardGroup>

### Dubbing Studio Project

* This is the advanced Dubbing version, which you can access by checking the **Create a Dubbing Studio project** box. Read more about it in the [Dubbing Studio guide](/docs/product-guides/products/dubbing/dubbing-studio).



# Dubbing Studio

> Fine-grained control over your dubs.

<CardGroup cols={1}>
  <video width="100%" height="400" controls>
    <source src="https://storage.googleapis.com/eleven-public-cdn/video/dubbing/new-dubbing-tutorial.mp4" type="video/mp4" />

    Your browser does not support the video tag.
  </video>
</CardGroup>


## Create a Dubbing Studio project

1. Check the 'Create Dubbing Studio' box when creating a dub.

<Frame background="subtle">
  ![Create Dubbing Studio Project](file:e2240ab1-3f5a-4297-a04b-30f9f3cb88b1)
</Frame>

2. Click on **Create Dub**. Once the Dubbing Studio project is created, you will be able to open it.


## Core Concepts

<AccordionGroup>
  <Accordion title="Speaker Cards">
    ## Speaker Cards

    <Frame background="subtle">
      ![Dubbing Studio Speaker Cards](file:ae5ad0f4-95bc-4419-9976-30e101bfb5c2)
    </Frame>

    Speaker cards show the original transcription and translation (if you add one) of dialogue from the source video. You can click 'Transcribe Audio' to retranscribe
    the original speech, or click the arrow to re-translate an existing transcription.

    ### Edit Transcripts and Translations

    Both transcriptions and translations can be edited freely - just click inside a speaker card and start typing to edit the text.

    ### Speaker Identification

    You can see the name of each speaker in the top left of the speaker card. To change the name of a speaker or reassign a clip to a different speaker,
    you'll need to use the Timeline.
  </Accordion>

  <Accordion title="Timeline">
    ## Timeline

    The timeline contains many important elements of Dubbing Studio, covered in more detail in different sections below:

    ### Basic navigation

    There are 3 main ways to navigate the timeline:

    1. Click and drag the cursor
    2. Horizontally scroll
    3. Input a specific timecode on the right side of the timeline

    ### Adjust clips and regenerate audio

    1. Drag the handles on the left or right side of a clip to adjust its length.
    2. Click the refresh icon to regenerate the audio for that clip.

    <Frame background="subtle">
      ![Dubbing Studio Adjust and Regenerate](file:859a83e1-66a0-4138-bb9b-5fc05d837e0c)
    </Frame>

    ##### Dynamic vs. Fixed Generations

    NOTE: By default, all regenerations in Dubbing Studio are <i>Fixed Generations</i>, which means that the system will keep the duration of the clip fixed regardless
    of how much text it contains. This can lead to speech speeding up or slowing down significantly if you adjust the length of a clip without changing the text, or if you add/remove
    a large number of words to a clip.

    Consider a clip with the phrase 'I'm doing well.' If that clip were set to last 10 seconds and the audio were generated using Fixed Generations, the speech would sound
    slow and drawn out.

    Alternatively, you can use <i>Dynamic Generations</i> by right clicking a segment and selecting it from the options. This will attempt to adjust the
    length of the clip to the length of the text and make the audio sound more natural.

    But be careful – using Dynamic Generations could affect sync and timing in your videos. If, for example, you select Dynamic Generation for a clip with many words in it,
    and there is not enough room before the next clip for it to properly expand, the audio may not generate properly.

    <Frame background="subtle">
      ![Dubbing Studio Dynamic Generation](file:cf96fedd-4f12-48b2-8100-54ac918d1db0)
    </Frame>

    ##### Stale Audio

    Stale audio refers to audio that needs to be regenerated for one of many reasons (clip length changes, settings changes, transcription/translation changes, etc). You can regenerate stale
    clips individually or click 'Generate Stale Audio' to bulk generate all stale audio clips.

    ##### Clip History

    You can right click a clip and select 'Clip History' to view previous generations and select the one that sounds best.

    ### Split and Merge clips

    1. To split a clip, move the cursor to a specific timecode and click 'Split'.
    2. To merge two clips, drag the ends of the clips together and click 'Merge.'

    <Frame background="subtle">
      ![Dubbing Studio Merge](file:a1758af0-4bbb-4164-bea0-a84f3890fbd4)
    </Frame>

    As you split and merge clips, the speaker cards above the timeline will update to reflect these changes.

    ### Reassign clips to different speakers

    To reassign a clips to a different speaker, click the segment and drag it to another track.

    <Frame background="subtle">
      ![Dubbing Studio Reassign Clips](file:b9a25ca0-9cb0-41be-a9c8-80d2b985406c)
    </Frame>

    ### Add additional audio tracks

    Use the action buttons at the bottom of the timeline to add new audio tracks

    <Frame background="subtle">
      ![Dubbing Studio Add Tracks](file:295b01b6-a367-48f7-9095-133836f4a84b)
    </Frame>
  </Accordion>

  <Accordion title="Voice Settings">
    ## Voice Settings

    ### Voice Selection

    To select the voice that will be used to generate audio on a specific speaker track, click the settings cog icon on the left side of the timeline near the speaker name.

    There are 3 main types of voices to choose from in Dubbing Studio:

    1. Clip clone - this creates a unique voice clone for each clip based on the source audio for that clip
    2. Track clone - this creates a single voice clone for the whole track based on all source audio for a given speaker
    3. Other voices - you can also choose from thousands of voices available in our Voice Library, each with detailed metadata and tags to help you choose the right one

    You can also create, save, and reuse a voice from a specific clip by right clicking the clip and selecting 'Create Voice from Selection.'

    ### Setting Track vs. Clip Level Settings

    You can set voice settings at two levels:

    1. Track Level - changes will apply across all clips in the track, which can help with stability and consistency.

    2. Clip Level - changes will only apply to a specific clip. To set clip-level settings, use the panel on the right side of the timeline.
       Disable the 'inherit track settings' toggle and configure your desired settings.

    <Frame background="subtle">
      ![Dubbing Studio Voice
      Settings](file:4149709b-a673-4160-91b9-119bd0994047)
    </Frame>
  </Accordion>

  <Accordion title="Exports">
    ## Exports

    Click 'Export' in the bottom right of Dubbing Studio to open the export menu.

    Dubbing Studio currently supports the following export formats:

    * AAC (audio)
    * MP3 (audio)
    * WAV (audio)
    * .zip of audio tracks
    * .zip of audio clips
    * AAF (timeline data)
    * SRT (subtitles/captions)
    * CSV (speaker, start\_time, end\_time, transcription, translation)

    <b>Make sure you select the correct language</b> when exporting.
  </Accordion>
</AccordionGroup>


## Additional Features

* **Voiceover Tracks:** Voiceover tracks create new Speakers. You can click and add clips on the timeline wherever you like. After creating a clip, start writing your desired text on the speaker cards above. You'll first need to translate that text, then you can press "Generate". You can also use our voice changer tool by clicking on the microphone icon on the right side of the screen to use your own voice and then change it into the selected voice.
* **SFX Tracks:** Add a SFX track, then click anywhere on that track to create a SFX clip. Similar to our independent SFX feature, simply start writing your prompt in the Speaker card above and click "Generate" to create your new SFX audio. You can lengthen or shorten SFX clips and move them freely around your timeline to fit your project - make sure to press the "stale" button if you do so.
* **Upload Audio:** This option allows you to upload a non voiced track such as sfx, music or background track. Please keep in mind that if voices are present in this track, they won't be detected so it will not be possible to translate or correct them.


## Manual Dub

In cases where you already have an accurate dubbing script prepared and want to ensure your Dubbing Studio project sticks to your
exact clips and speaker assignment, you can use the <b>Manual Dub</b> option during creation.

To create a Manual Dub, you'll need:

1. Video file
2. Background audio file
3. Foreground audio file
4. CSV where each row contains a speaker, start\_time, end\_time, transcription, and translation field

The CSV file must strictly follow the predefined format in order to be processed correctly. Please see below for samples in the three supported timecodes:

* seconds
* hours:minutes:seconds:frame
* hours:minutes:seconds,milliseconds

### Example CSV files

<CodeBlocks>
  ```csv seconds
  speaker,start_time,end_time,transcription,translation
  Adam,"0.10000","1.15000","Hello, how are you?","Hola, ¿cómo estás?"
  Adam,"1.50000","3.50000","I'm fine, thank you.","Estoy bien, gracias."

  ```

  ```csv hours:minutes:seconds:frame
  speaker,start_time,end_time,transcription,translation
  Adam,"0:00:01:01","0:00:05:01","Hello, how are you?","Hola, ¿cómo estás?"
  Adam,"0:00:06:01","0:00:10:01","I'm fine, thank you.","Estoy bien, gracias."

  ```

  ```csv hours:minutes:seconds,milliseconds
  speaker,start_time,end_time,transcription,translation
  Adam,"0:00:01,000","0:00:05,000","Hello, how are you?","Hola, ¿cómo estás?"
  Adam,"0:00:06,000","0:00:10,000","I'm fine, thank you.","Estoy bien, gracias."

  ```
</CodeBlocks>

| speaker | start\_time | end\_time   | transcription                     | translation                                  |
| ------- | ----------- | ----------- | --------------------------------- | -------------------------------------------- |
| Joe     | 0:00:00.000 | 0:00:02.000 | Hey!                              | Hallo!                                       |
| Maria   | 0:00:02.000 | 0:00:06.000 | Oh, hi, Joe. It has been a while. | Oh, hallo, Joe. Es ist schon eine Weile her. |
| Joe     | 0:00:06.000 | 0:00:11.000 | Yeah, I know. Been busy.          | Ja, ich weiß. War beschäftigt.               |
| Maria   | 0:00:11.000 | 0:00:17.000 | Yeah? What have you been up to?   | Ja? Was hast du gemacht?                     |
| Joe     | 0:00:17.000 | 0:00:23.000 | Traveling mostly.                 | Hauptsächlich gereist.                       |
| Maria   | 0:00:23.000 | 0:00:30.000 | Oh, anywhere I would know?        | Oh, irgendwo, das ich kenne?                 |
| Joe     | 0:00:30.000 | 0:00:36.000 | Spain.                            | Spanien.                                     |



# Transcripts

> Using the ElevenLabs Transcript Editor

<img src="file:2152de2a-c35e-4a23-b498-e3c296b836c7" alt="Transcript Editor Product Feature" />


## Transcript Editor

<Steps>
  <Step title="Open transcript">
    In the ElevenLabs dashboard, navigate to the Speech to Text page and click any transcript to open the Transcript Editor.

    <Frame background="subtle">
      ![Open transcript](file:442b6428-e683-464e-83ff-17f1737484f9)
    </Frame>
  </Step>

  <Step title="Edit basic details">
    You can rename your transcript in the panel on the right side of the screen.

    <Frame background="subtle">
      ![Edit details](file:13195500-6aa9-46a3-ba44-c9cfda46d060)
    </Frame>
  </Step>

  <Step title="Edit text">
    Our transcript editor is WYSIWYG. Click anywhere in the transcript and start typing to edit the text.

    <b>Tip:</b> Use command+z to undo changes easily.

    <Frame background="subtle">
      ![Edit text](file:ae0b91d1-eb42-4457-b796-96b51d18d88d)
    </Frame>
  </Step>

  <Step title="Adjust segment start and end times">
    Drag the handles on the timeline to adjust the start and end timestamps for a segment. You can also type in exact timestamps in the panel on the right side of the screen.

    <Frame background="subtle">
      ![Adjust times](file:e81297b2-4df7-4ff7-9e8f-d5b0d17d6735)
    </Frame>
  </Step>

  <Step title="Split and merge segments">
    To split a segment, click in the text where you want to split and press **Enter.**

    To merge two segments, click the 'merge segments' button. Note that two conditions must be fulfilled for a merge to be possible:

    1. Both segments must belong to the same speaker
    2. The segments must be adjacent to each other

    <Frame background="subtle">
      ![Split and merge](file:e1db7884-d921-4b96-8664-062a6478e72b)
    </Frame>
  </Step>

  <Step title="Add or remove segments">
    To add a segment, click on the 'Add Segment' icon and select a location on the timeline.

    To delete a segment, select the segment and click ‘Delete’ in the panel on the right side of the screen or press the Delete key

    <Frame background="subtle">
      ![Add/remove segments](file:a7dc6ba9-e900-4624-9f90-2f4a4c2687d0)
    </Frame>
  </Step>

  <Step title="Re-align words inside a segment">
    Click ‘align words’ after making changes to a segment to recompute word-level timestamps.

    <Frame background="subtle">
      ![Re-align words](file:db981d19-0527-4863-8e64-809bad1435ff)
    </Frame>
  </Step>

  <Step title="Re-assign segments to different speakers">
    There are 2 ways to assign segments to different speakers:

    1. **Individually**: click the orb next to the speaker name for a segment, and select a new speaker from the dropdown list.
    2. **Bulk:** to reassign all segments from one speaker to another, click on the three dots (⋮) and select 'Move Segments To'. Then select the new speaker.

    <Frame background="subtle">
      ![Re-assign segments](file:a92c4c19-3e68-4f00-a61b-2bfb8f305e73)
    </Frame>
  </Step>

  <Step title="Add or delete speakers">
    To add a speaker, click the '+' icon above the speaker tracks. To delete a speaker, click on the three dots (⋮) next to the speaker’s track and click ‘Delete.’

    **Important note**: if you delete a speaker, all of their associated segments will also be deleted.

    <Frame background="subtle">
      ![Add/delete speakers](file:e987ffea-07b0-4d66-9cbe-16b84b0f8947)
    </Frame>
  </Step>

  <Step title="Reorder speaker tracks and change colors">
    Click and drag to reorder speaker tracks on the timeline. You can also change the color of a speaker track (which also applies to all its segments) by clicking the orb next to the speaker name.

    <Frame background="subtle">
      ![Reorder and color](file:b65f237e-20bf-404c-90a1-dc7b41cc2439)
    </Frame>
  </Step>

  <Step title="Adjust playback speed">
    You can adjust the playback speed of the source media by clicking the indicator next to the play button.

    <Frame background="subtle">
      ![Playback speed](file:4be5ff91-8a31-4da4-af77-9fcbd6960462)
    </Frame>
  </Step>

  <Step title="Export transcript">
    Click the export button in the top right of the screen and select one of the transcript export formats:

    * Plain text
    * JSON
    * HTML
    * SRT
    * VTT

    <Frame background="subtle">
      ![Exports](file:b3505fad-95d5-4752-9935-0cd0df470252)
    </Frame>
  </Step>
</Steps>


## FAQ

<AccordionGroup>
  <Accordion title="Does the transcript editor also support subtitles?">
    Yes – you can add subtitles by clicking the '+' next to 'Subtitles' in the panel on the right
    side of the screen.

    To learn more about editing subtitles, please see our [Subtitle guide](/docs/product-guides/products/subtitles).
  </Accordion>

  <Accordion title="Can someone review my transcript to make sure it's accurate?">
    Yes – our Productions team offers human transcription services from \$2.00 per minute of audio. What you get from us:

    * Expert review by a native speaker
    * Optional 'Verbatim Mode' for maximum coverage of non-verbal sounds (\[cough], \[sigh], etc.) and other environmental sounds and audio events (\[dog barking], \[car horn], etc.)

    For more information please see the 'Productions' section of your ElevenLabs account (currently in beta and available to select users) or contact us at [productions@elevenlabs.io](mailto:productions@elevenlabs.io).
  </Accordion>
</AccordionGroup>



# Subtitles

> Using the ElevenLabs Subtitle Editor

<img src="file:5b949f13-5f3d-4603-bad2-1de24b76c7ba" alt="Subtitle Editor Product Feature" />


## Subtitle Editor

<Steps>
  <Step title="Open transcript editor">
    You can use the subtitling mode of our transcript editor to edit your subtitles. Navigate to the Speech to Text page of your ElevenLabs account and click any transcript to get started.

    <Frame background="subtle">
      ![Open transcript](file:442b6428-e683-464e-83ff-17f1737484f9)
    </Frame>
  </Step>

  <Step title="Edit basic details">
    You can rename your subtitles in the panel on the right side of the screen.

    <Frame background="subtle">
      ![Edit details](file:13195500-6aa9-46a3-ba44-c9cfda46d060)
    </Frame>
  </Step>

  <Step title="Add subtitles">
    If you didn't add subtitles when creating the transcript, you can do so by clicking the "+" next to "Subtitles" in the panel on the right side of the screen.
    You can switch between transcription and subtitling mode at any time using the tabs at the top of the editor.

    <b>Tip:</b> you can also add subtitles during the transcript creation process by enabling the 'Include subtitles' toggle.

    <Frame background="subtle">
      ![Add subtitles](file:95fef0cc-0534-4b7c-858b-913a876140ed)
    </Frame>

    <Frame background="subtle">
      ![Add subtitles](file:3b6955d9-0b21-4602-8712-fba4aba3f89e)
    </Frame>
  </Step>

  <Step title="Edit rules/constraints">
    Our subtitle editor uses red and green colors to give you real-time feedback on whether your subtitles respect formatting rules like characters per line, lines on screen, and cue length.

    To edit these rules, click the three dots next to 'Subtitles' in the panel on the right side of the screen and select 'Edit rules'

    <Frame background="subtle">
      ![Edit rules](file:34a30e7b-fae0-4614-9161-e6094d269fef)
    </Frame>

    <Frame background="subtle">
      ![Edit rules](file:09f184e9-8b5a-4ce5-a031-e164efa59ac6)
    </Frame>
  </Step>

  <Step title="Edit text">
    Our subtitle editor is WYSIWYG. Click anywhere and start typing to edit the text.

    <b>Tip:</b> Use command+z to undo changes easily.

    <Frame background="subtle">
      ![Edit text](file:345d60ac-aaf7-4681-b65c-ab01150697a3)
    </Frame>
  </Step>

  <Step title="Adjust cue start and end times">
    Drag the handles on the timeline to adjust the start and end timestamps for a cue. You can also type in exact timestamps in the panel on the right side of the screen.

    <b>Important:</b> the transcript and subtitles for a video are completely separate from each other. Changes you make to subtitles (e.g. changing cue start/end times, adding/removing words, etc.) do NOT affect the transcription, and vice versa.

    <Frame background="subtle">
      ![Adjust times](file:b8aebacc-3092-40ec-a01a-73b603c6d428)
    </Frame>
  </Step>

  <Step title="Split and merge cues">
    To split a cue, click in the text where you want to split and press **Enter.**

    To merge two cues, click the 'merge cues' button.

    <Frame background="subtle">
      ![Split and merge](file:27f5683c-f245-4390-8032-cc8057d10c73)
    </Frame>
  </Step>

  <Step title="Add or remove cues">
    To add a cue, click 'Add cue' and select a location on the timeline.

    To delete a cue, select the cue and click ‘Delete’ in the panel on the right side of the screen, or press the Delete key.

    <Frame background="subtle">
      ![Add/remove segments](file:2f9669aa-72cf-48f5-9693-328779192b03)
    </Frame>
  </Step>

  <Step title="Adjust playback speed">
    You can adjust the playback speed of the source media by clicking the indicator next to the play button.

    <Frame background="subtle">
      ![Playback speed](file:4be5ff91-8a31-4da4-af77-9fcbd6960462)
    </Frame>
  </Step>

  <Step title="Export subtitles">
    Click the export button in the top right of the screen and select one of the subtitle export formats:

    * SRT
    * VTT

    <Frame background="subtle">
      ![Exports](file:b3505fad-95d5-4752-9935-0cd0df470252)
    </Frame>
  </Step>
</Steps>


## FAQ

<AccordionGroup>
  <Accordion title="Are transcripts and subtitles different?">
    Yes – subtitles have specific formatting rules and requirements that do not apply to transcripts.

    Below is a summary of some (but not all) of the major differences between the two:

    | Feature                        | Transcripts | Subtitles                                                        |
    | ------------------------------ | ----------- | ---------------------------------------------------------------- |
    | Word-level timestamps          | Yes         | No - only start/end times of cues                                |
    | Speaker names/labels           | Yes         | No                                                               |
    | Constraints                    | No          | Yes - characters per line, lines on screen at once, cue duration |
    | Overlapping segments supported | Yes         | No                                                               |

    For more information about transcripts, please see our [Transcripts guide](/docs/product-guides/products/transcripts).
  </Accordion>

  <Accordion title="Do changes to subtitles affect the transcript too?">
    No – transcripts and subtitles are completely separate from each other in our editor. That means that changes you make to one will NOT affect the other.
  </Accordion>

  <Accordion title="Can ElevenLabs help me with my subtitles?">
    Yes – our Productions team offers human subtitling services from \$2.20 per minute. What you get from us:

    * A subtitling expert edits your subtitles to ensure they adhere to all formatting rules and requirements
    * If you choose, our language teams translate your subtitles into different languages

    For more information please see the 'Productions' section of your ElevenLabs account (currently in beta and available to select users) or contact us at [productions@elevenlabs.io](mailto:productions@elevenlabs.io).
  </Accordion>
</AccordionGroup>



---
**Navigation:** [← Previous](./07-migrate-from-playht-to-elevenlabs.md) | [Index](./index.md) | [Next →](./09-voice-library.md)
