**Navigation:** [← Previous](./03-february-17-2025.md) | [Index](./index.md) | [Next →](./05-find-create-an-api-key-at-httpselevenlabsioappsett.md)

# Voice remixing

> Learn how to transform and enhance existing voices by modifying their attributes including gender, accent, style, pacing, audio quality, and more.

<Warning>
  Voice remixing is currently in alpha.
</Warning>


## Overview

ElevenLabs voice remixing is available on the core platform and via API. This feature transforms existing voices by allowing you to modify their core attributes while maintaining the unique characteristics that make them recognizable. This is particularly useful for adapting voices to different contexts, creating variations for different characters, or improving and/or changing the audio quality of existing voice profiles.

As an example, here is an original voice:

<elevenlabs-audio-player audio-title="Original voice" audio-src="https://storage.googleapis.com/eleven-public-cdn/documentation_assets/audio/remix-original-voice.mp3" />

And here is a remixed version, switching to a San Francisco accent:

<elevenlabs-audio-player audio-title="Remixed voice" audio-src="https://storage.googleapis.com/eleven-public-cdn/documentation_assets/audio/remix-sf-accent.mp3" />


## Usage

The voice remixing model allows you to iteratively transform voices you own by adjusting multiple attributes through natural language prompts and customizable settings.

<CardGroup cols={2}>
  <Card title="Voice Remixing Developer quickstart" icon="duotone book-sparkles" href="/docs/cookbooks/voices/remix-a-voice">
    Integrate voice remixing into your application.
  </Card>

  {/* <Card
      title="Product guide"
      icon="duotone book-user"
      href="/docs/product-guides/voices/voice-design"
    >
      Learn how to craft voices from a single prompt.
    </Card> */}
</CardGroup>

### Key Features

* **Attribute Modification**: Change gender, accent, speaking style, pacing, and audio quality of any voice you own
* **Iterative Editing**: Continue refining voices based on previously remixed versions
* **Script Flexibility**: Use default scripts or input custom scripts with v3 model audio tags like `[laughs]` or `[whispers]`
* **Prompt Strength Control**: Adjust remix intensity from low to high for precise control over transformations

### Remixing parameters

#### Prompt Strength

Voice remixing offers varying degrees of prompt strength to control how much your voice transforms:

* **Low**: Subtle changes that maintain most of the original voice characteristics
* **Medium**: Balanced transformation that modifies key attributes while preserving voice identity
* **High**: Strong adherence to remix prompt, may significantly change the tonality of the original voice
* **Max**: A full transformation of the voice, but at the cost of changing the voice entirely

#### Script Options

* **Default Scripts**: Pre-configured scripts optimized for voice remixing
* **Custom Scripts**: Input your own text with support for v3 model audio tags such as:
  * `[laughs]` - Add laughter
  * `[whispers]` - Convert to whispered speech
  * `[sighs]` - Add sighing
  * Additional emotion and style tags supported which can help craft the voice

### Tips and Tricks

#### Getting Started

Start with a high prompt strength early in your experimentation to understand the full range of transformation possibilities. You’ll need to have a voice to start with, if you haven’t already created a voice, experiment with default voices available in your library to understand how different base voices respond to remixing.

You can create custom voices using [Voice Design](/docs/product-guides/voices/voice-design) as starting points for unique remixes.

#### Advanced Techniques

* **Iterative refinement**: Sometimes multiple iterations are needed to achieve the desired voice quality. Each remix can serve as the base for the next transformation
* **Combine attributes gradually**: When making multiple changes (e.g., accent and pacing), consider applying them in separate iterations for more control
* **Test with varied content**: Different scripts may highlight different aspects of your remixed voice

### Supported Voice Formats

#### Input

* Any cloned voice that you personally own (Instant Voice Clone or Professional Voice Clone)
* Voices created through our Voice Design product

#### Output

* Full-quality voice model in v3 (but backwards compatibility to all other models)
* Iteratively editable voice that can be further remixed


## FAQ

<AccordionGroup>
  <Accordion title="What does Voice Remixing cost?">
    Voice remixing costs are calculated based on the length of the test script used during the
    remixing process.
  </Accordion>

  <Accordion title="Can I remix voices I don't own?">
    No, voice remixing is only available for voices in your personal library that you have ownership
    or appropriate permissions for.
  </Accordion>

  <Accordion title="How many times can I remix a voice?">
    There is no limit to iterative remixing. You can continue refining a voice through multiple
    generations of remixes.
  </Accordion>

  <Accordion title="Will remixing affect my original voice?">
    No, remixing creates a new voice variant. Your original voice remains unchanged and available in
    your library.
  </Accordion>

  <Accordion title="What's the difference between Voice Design and Voice Remixing?">
    Voice Design creates new voices from scratch using text prompts, while Voice Remixing modifies
    existing voices you already own.
  </Accordion>
</AccordionGroup>



# Forced Alignment

> Learn how to turn spoken audio and text into a time-aligned transcript with ElevenLabs.


## Overview

The ElevenLabs [Forced Alignment](/docs/api-reference/forced-alignment) API turns spoken audio and text into a time-aligned transcript. This is useful for cases where you have audio recording and a transcript, but need exact timestamps for each word or phrase in the transcript. This can be used for:

* Matching subtitles to a video recording
* Generating timings for an audiobook recording of an ebook


## Usage

The Forced Alignment API can be used by interfacing with the ElevenLabs API directly.

<CardGroup cols={1}>
  <Card title="Developer quickstart" icon="duotone book-sparkles" href="/docs/cookbooks/forced-alignment">
    Learn how to integrate Forced Alignment into your application.
  </Card>
</CardGroup>


## Supported languages

Our multilingual v2 models support 29 languages:

*English (USA, UK, Australia, Canada), Japanese, Chinese, German, Hindi, French (France, Canada), Korean, Portuguese (Brazil, Portugal), Italian, Spanish (Spain, Mexico), Indonesian, Dutch, Turkish, Filipino, Polish, Swedish, Bulgarian, Romanian, Arabic (Saudi Arabia, UAE), Czech, Greek, Finnish, Croatian, Malay, Slovak, Danish, Tamil, Ukrainian & Russian.*


## FAQ

<AccordionGroup>
  <Accordion title="What is forced alignment?">
    Forced alignment is a technique used to align spoken audio with text. You provide an audio file and a transcript of the audio file and the API will return a time-aligned transcript.

    It's useful for cases where you have audio recording and a transcript, but need exact timestamps for each word or phrase in the transcript.
  </Accordion>

  <Accordion title="What text input formats are supported?">
    The input text should be a string with no special formatting i.e. JSON.

    Example of good input text:

    ```
    "Hello, how are you?"
    ```

    Example of bad input text:

    ```
    {
        "text": "Hello, how are you?"
    }
    ```
  </Accordion>

  <Accordion title="How much does Forced Alignment cost?">
    Forced Alignment costs the same as the [Speech to Text](/docs/capabilities/speech-to-text#pricing) API.
  </Accordion>

  <Accordion title="Does Forced Alignment support diarization?">
    Forced Alignment does not support diarization. If you provide diarized text, the API will likely return unwanted results.
  </Accordion>

  <Accordion title="What is the maximum audio file size for Forced Alignment?">
    The maximum file size for Forced Alignment is 3GB.
  </Accordion>

  <Accordion title="What is the maximum duration for a Forced Alignment input file?">
    For audio files, the maximum duration is 10 hours.

    For the text input, the maximum length is 675k characters.
  </Accordion>
</AccordionGroup>



# Eleven Music

> Learn how to create studio-grade music with natural language prompts in any style with ElevenLabs.


## Overview

Eleven Music is a Text to Music model that generates studio-grade music with natural language prompts in any style. It's designed to understand intent and generate complete, context-aware audio based on your goals. The model understands both natural language and musical terminology, providing you with state-of-the-art features:

* Complete control over genre, style, and structure
* Vocals or just instrumental
* Multilingual, including English, Spanish, German, Japanese and more
* Edit the sound and lyrics of individual sections or the whole song

Listen to a sample:

<elevenlabs-audio-player audio-title="Eleven Outta Ten" audio-src="https://storage.googleapis.com/eleven-public-cdn/documentation_assets/audio/music-eleven-outta-ten.mp3" />

Created in collaboration with labels, publishers, and artists, Eleven Music is cleared for nearly all commercial uses, from film and television to podcasts and social media videos, and from advertisements to gaming. For more information on supported usage across our different plans, [see our music terms](http://elevenlabs.io/music-terms).


## Usage

Eleven Music is available today on the ElevenLabs website, with public API access and integration into our Agents Platform coming soon.

Created in collaboration with labels, publishers, and artists, Eleven Music is cleared for nearly all commercial uses, from film and television to podcasts and social media videos, and from advertisements to gaming. For more information on supported usage across our different plans, head here.

Eleven Music is available today on our website, with public API access and integration into our Agents Platform coming soon. Check out our prompt engineering guide to help you master the full range of the model’s capabilities.

<CardGroup cols={2}>
  <Card title="Prompting guide" icon="duotone book-sparkles" href="/docs/best-practices/prompting/eleven-music">
    Learn how to use Eleven Music with natural language prompts.
  </Card>

  <Card title="Product guide" icon="duotone book-user" href="/docs/product-guides/products/music">
    Step-by-step guide for using Eleven Music on the ElevenLabs Creative Platform.
  </Card>

  <Card title="Developer quickstart" icon="duotone code" href="/docs/cookbooks/music">
    Step-by-step guide for using Eleven Music with the API.
  </Card>
</CardGroup>


## FAQ

<AccordionGroup>
  <Accordion title="What's the maximum duration for generated music?">
    Generated music has a minimum duration of 10 seconds and a maximum duration of 5 minutes.
  </Accordion>

  <Accordion title="Is there an API available?">
    Yes, refer to the [developer quickstart](/docs/cookbooks/music) for more information.
  </Accordion>

  <Accordion title="Can I use Eleven Music for my business?">
    Yes, Eleven Music is cleared for nearly all commercial uses, from film and television to
    podcasts and social media videos, and from advertisements to gaming. For more information on
    supported usage across our different plans, [see our music
    terms](http://elevenlabs.io/music-terms).
  </Accordion>

  <Accordion title="What audio formats are supported?">
    Generated audio is provided in MP3 format with professional-grade quality (44.1kHz,
    128-192kbps). Other audio formats will be supported soon.
  </Accordion>
</AccordionGroup>



# Streaming text to speech

> Learn how to stream text into speech in Python or Node.js.

In this tutorial, you'll learn how to convert [text to speech](https://elevenlabs.io/text-to-speech) with the ElevenLabs SDK. We’ll start by talking through how to generate speech and receive a file and then how to generate speech and stream the response back. Finally, as a bonus we’ll show you how to upload the generated audio to an AWS S3 bucket, and share it through a signed URL. This signed URL will provide temporary access to the audio file, making it perfect for sharing with users by SMS or embedding into an application.

If you want to jump straight to an example you can find them in the [Python](https://github.com/elevenlabs/elevenlabs-examples/tree/main/examples/text-to-speech/python) and [Node.js](https://github.com/elevenlabs/elevenlabs-examples/tree/main/examples/text-to-speech/node) example repositories.


## Requirements

* An ElevenLabs account with an API key (here’s how to [find your API key](/docs/developer-guides/quickstart#authentication)).
* Python or Node installed on your machine
* (Optionally) an AWS account with access to S3.


## Setup

### Installing our SDK

Before you begin, make sure you have installed the necessary SDKs and libraries. You will need the ElevenLabs SDK for the text to speech conversion. You can install it using pip:

<CodeGroup>
  ```bash Python
  pip install elevenlabs
  ```

  ```bash TypeScript
  npm install @elevenlabs/elevenlabs-js
  ```
</CodeGroup>

Additionally, install necessary packages to manage your environmental variables:

<CodeGroup>
  ```bash Python
  pip install python-dotenv
  ```

  ```bash TypeScript
  npm install dotenv
  npm install @types/dotenv --save-dev
  ```
</CodeGroup>

Next, create a `.env` file in your project directory and fill it with your credentials like so:

```bash .env
ELEVENLABS_API_KEY=your_elevenlabs_api_key_here
```


## Convert text to speech (file)

To convert text to speech and save it as a file, we’ll use the `convert` method of the ElevenLabs SDK and then it locally as a `.mp3` file.

<CodeGroup>
  ```python Python

  import os
  import uuid
  from dotenv import load_dotenv
  from elevenlabs import VoiceSettings
  from elevenlabs.client import ElevenLabs

  load_dotenv()

  ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
  elevenlabs = ElevenLabs(
      api_key=ELEVENLABS_API_KEY,
  )


  def text_to_speech_file(text: str) -> str:
      # Calling the text_to_speech conversion API with detailed parameters
      response = elevenlabs.text_to_speech.convert(
          voice_id="pNInz6obpgDQGcFmaJgB", # Adam pre-made voice
          output_format="mp3_22050_32",
          text=text,
          model_id="eleven_turbo_v2_5", # use the turbo model for low latency
          # Optional voice settings that allow you to customize the output
          voice_settings=VoiceSettings(
              stability=0.0,
              similarity_boost=1.0,
              style=0.0,
              use_speaker_boost=True,
              speed=1.0,
          ),
      )

      # uncomment the line below to play the audio back
      # play(response)

      # Generating a unique file name for the output MP3 file
      save_file_path = f"{uuid.uuid4()}.mp3"

      # Writing the audio to a file
      with open(save_file_path, "wb") as f:
          for chunk in response:
              if chunk:
                  f.write(chunk)

      print(f"{save_file_path}: A new audio file was saved successfully!")

      # Return the path of the saved audio file
      return save_file_path

  ```

  ```typescript TypeScript
  import { ElevenLabsClient } from '@elevenlabs/elevenlabs-js';
  import * as dotenv from 'dotenv';
  import { createWriteStream } from 'fs';
  import { v4 as uuid } from 'uuid';

  dotenv.config();

  const ELEVENLABS_API_KEY = process.env.ELEVENLABS_API_KEY;

  const elevenlabs = new ElevenLabsClient({
    apiKey: ELEVENLABS_API_KEY,
  });

  export const createAudioFileFromText = async (text: string): Promise<string> => {
    return new Promise<string>(async (resolve, reject) => {
      try {
        const audio = await elevenlabs.textToSpeech.convert('JBFqnCBsd6RMkjVDRZzb', {
          modelId: 'eleven_multilingual_v2',
          text,
          outputFormat: 'mp3_44100_128',
          // Optional voice settings that allow you to customize the output
          voiceSettings: {
            stability: 0,
            similarityBoost: 0,
            useSpeakerBoost: true,
            speed: 1.0,
          },
        });

        const fileName = `${uuid()}.mp3`;
        const fileStream = createWriteStream(fileName);

        audio.pipe(fileStream);
        fileStream.on('finish', () => resolve(fileName)); // Resolve with the fileName
        fileStream.on('error', reject);
      } catch (error) {
        reject(error);
      }
    });
  };
  ```
</CodeGroup>

You can then run this function with:

<CodeGroup>
  ```python Python
  text_to_speech_file("Hello World")
  ```

  ```typescript TypeScript
  await createAudioFileFromText('Hello World');
  ```
</CodeGroup>


## Convert text to speech (streaming)

If you prefer to stream the audio directly without saving it to a file, you can use our streaming feature.

<CodeGroup>
  ```python Python

  import os
  from typing import IO
  from io import BytesIO
  from dotenv import load_dotenv
  from elevenlabs import VoiceSettings
  from elevenlabs.client import ElevenLabs

  load_dotenv()

  ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
  elevenlabs = ElevenLabs(
      api_key=ELEVENLABS_API_KEY,
  )


  def text_to_speech_stream(text: str) -> IO[bytes]:
      # Perform the text-to-speech conversion
      response = elevenlabs.text_to_speech.stream(
          voice_id="pNInz6obpgDQGcFmaJgB", # Adam pre-made voice
          output_format="mp3_22050_32",
          text=text,
          model_id="eleven_multilingual_v2",
          # Optional voice settings that allow you to customize the output
          voice_settings=VoiceSettings(
              stability=0.0,
              similarity_boost=1.0,
              style=0.0,
              use_speaker_boost=True,
              speed=1.0,
          ),
      )

      # Create a BytesIO object to hold the audio data in memory
      audio_stream = BytesIO()

      # Write each chunk of audio data to the stream
      for chunk in response:
          if chunk:
              audio_stream.write(chunk)

      # Reset stream position to the beginning
      audio_stream.seek(0)

      # Return the stream for further use
      return audio_stream

  ```

  ```typescript TypeScript
  import { ElevenLabsClient } from '@elevenlabs/elevenlabs-js';
  import * as dotenv from 'dotenv';

  dotenv.config();

  const ELEVENLABS_API_KEY = process.env.ELEVENLABS_API_KEY;

  if (!ELEVENLABS_API_KEY) {
    throw new Error('Missing ELEVENLABS_API_KEY in environment variables');
  }

  const elevenlabs = new ElevenLabsClient({
    apiKey: ELEVENLABS_API_KEY,
  });

  export const createAudioStreamFromText = async (text: string): Promise<Buffer> => {
    const audioStream = await elevenlabs.textToSpeech.stream('JBFqnCBsd6RMkjVDRZzb', {
      modelId: 'eleven_multilingual_v2',
      text,
      outputFormat: 'mp3_44100_128',
      // Optional voice settings that allow you to customize the output
      voiceSettings: {
        stability: 0,
        similarityBoost: 1.0,
        useSpeakerBoost: true,
        speed: 1.0,
      },
    });

    const chunks: Buffer[] = [];
    for await (const chunk of audioStream) {
      chunks.push(chunk);
    }

    const content = Buffer.concat(chunks);
    return content;
  };
  ```
</CodeGroup>

You can then run this function with:

<CodeGroup>
  ```python Python
  text_to_speech_stream("This is James")
  ```

  ```typescript TypeScript
  await createAudioStreamFromText('This is James');
  ```
</CodeGroup>


## Bonus - Uploading to AWS S3 and getting a secure sharing link

Once your audio data is created as either a file or a stream you might want to share this with your users. One way to do this is to upload it to an AWS S3 bucket and generate a secure sharing link.

<AccordionGroup>
  <Accordion title="Creating your AWS credentials">
    To upload the data to S3 you’ll need to add your AWS access key ID, secret access key and AWS region name to your `.env` file. Follow these steps to find the credentials:

    1. Log in to your AWS Management Console: Navigate to the AWS home page and sign in with your account.

    <Frame caption="AWS Console Login">
      <img src="file:1512f696-0a9e-41cc-bac7-6d4b745cb775" />
    </Frame>

    2. Access the IAM (Identity and Access Management) Dashboard: You can find IAM under "Security, Identity, & Compliance" on the services menu. The IAM dashboard manages access to your AWS services securely.

    <Frame caption="AWS IAM Dashboard">
      <img src="file:3fd27741-032d-467f-b8da-56d469399000" />
    </Frame>

    3. Create a New User (if necessary): On the IAM dashboard, select "Users" and then "Add user". Enter a user name.

    <Frame caption="Add AWS IAM User">
      <img src="file:a1730c67-b3b0-439d-b457-ede0bd1f58fc" />
    </Frame>

    4. Set the permissions: attach policies directly to the user according to the access level you wish to grant. For S3 uploads, you can use the AmazonS3FullAccess policy. However, it's best practice to grant least privilege, or the minimal permissions necessary to perform a task. You might want to create a custom policy that specifically allows only the necessary actions on your S3 bucket.

    <Frame caption="Set Permission for AWS IAM User">
      <img src="file:3fa1850b-32c0-4105-a0a2-371989e0c54b" />
    </Frame>

    5. Review and create the user: Review your settings and create the user. Upon creation, you'll be presented with an access key ID and a secret access key. Be sure to download and securely save these credentials; the secret access key cannot be retrieved again after this step.

    <Frame caption="AWS Access Secret Key">
      <img src="file:c8d4bc72-1ee5-49b8-adf0-7ac890fde3f5" />
    </Frame>

    6. Get AWS region name: ex. us-east-1

    <Frame caption="AWS Region Name">
      <img src="file:a97a7c17-6b0c-439d-98d2-22eb7682854a" />
    </Frame>

    If you do not have an AWS S3 bucket, you will need to create a new one by following these steps:

    1. Access the S3 dashboard: You can find S3 under "Storage" on the services menu.

    <Frame caption="AWS S3 Dashboard">
      <img src="file:380611cc-e060-4411-964b-fd20173b1919" />
    </Frame>

    2. Create a new bucket: On the S3 dashboard, click the "Create bucket" button.

    <Frame caption="Click Create Bucket Button">
      <img src="file:e21b7c53-5537-4d84-a6e1-2b0585b53f9e" />
    </Frame>

    3. Enter a bucket name and click on the "Create bucket" button. You can leave the other bucket options as default. The newly added bucket will appear in the list.

    <Frame caption="Enter a New S3 Bucket Name">
      <img src="file:433679d4-f75a-4854-a575-e017d64345a3" />
    </Frame>

    <Frame caption="S3 Bucket List">
      <img src="file:d3ac49e5-c1d1-46aa-ba35-14f464a385c7" />
    </Frame>
  </Accordion>

  <Accordion title="Installing the AWS SDK and adding the credentials">
    Install `boto3` for interacting with AWS services using `pip` and `npm`.

    <CodeGroup>
      ```bash Python
      pip install boto3
      ```

      ```bash TypeScript
      npm install @aws-sdk/client-s3
      npm install @aws-sdk/s3-request-presigner
      ```
    </CodeGroup>

    Then add the environment variables to `.env` file like so:

    ```
    AWS_ACCESS_KEY_ID=your_aws_access_key_id_here
    AWS_SECRET_ACCESS_KEY=your_aws_secret_access_key_here
    AWS_REGION_NAME=your_aws_region_name_here
    AWS_S3_BUCKET_NAME=your_s3_bucket_name_here
    ```
  </Accordion>

  <Accordion title="Uploading to AWS S3 and generating the signed URL">
    Add the following functions to upload the audio stream to S3 and generate a signed URL.

    <CodeGroup>
      ```python s3_uploader.py (Python)

      import os
      import boto3
      import uuid

      AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
      AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
      AWS_REGION_NAME = os.getenv("AWS_REGION_NAME")
      AWS_S3_BUCKET_NAME = os.getenv("AWS_S3_BUCKET_NAME")

      session = boto3.Session(
          aws_access_key_id=AWS_ACCESS_KEY_ID,
          aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
          region_name=AWS_REGION_NAME,
      )
      s3 = session.client("s3")


      def generate_presigned_url(s3_file_name: str) -> str:
          signed_url = s3.generate_presigned_url(
              "get_object",
              Params={"Bucket": AWS_S3_BUCKET_NAME, "Key": s3_file_name},
              ExpiresIn=3600,
          )  # URL expires in 1 hour
          return signed_url


      def upload_audiostream_to_s3(audio_stream) -> str:
          s3_file_name = f"{uuid.uuid4()}.mp3"  # Generates a unique file name using UUID
          s3.upload_fileobj(audio_stream, AWS_S3_BUCKET_NAME, s3_file_name)

          return s3_file_name

      ```

      ```typescript s3_uploader.ts (TypeScript)
      import { S3Client, PutObjectCommand, GetObjectCommand } from '@aws-sdk/client-s3';
      import { getSignedUrl } from '@aws-sdk/s3-request-presigner';
      import * as dotenv from 'dotenv';
      import { v4 as uuid } from 'uuid';

      dotenv.config();

      const { AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION_NAME, AWS_S3_BUCKET_NAME } =
        process.env;

      if (!AWS_ACCESS_KEY_ID || !AWS_SECRET_ACCESS_KEY || !AWS_REGION_NAME || !AWS_S3_BUCKET_NAME) {
        throw new Error('One or more environment variables are not set. Please check your .env file.');
      }

      const s3 = new S3Client({
        credentials: {
          accessKeyId: AWS_ACCESS_KEY_ID,
          secretAccessKey: AWS_SECRET_ACCESS_KEY,
        },
        region: AWS_REGION_NAME,
      });

      export const generatePresignedUrl = async (objectKey: string) => {
        const getObjectParams = {
          Bucket: AWS_S3_BUCKET_NAME,
          Key: objectKey,
          Expires: 3600,
        };
        const command = new GetObjectCommand(getObjectParams);
        const url = await getSignedUrl(s3, command, { expiresIn: 3600 });
        return url;
      };

      export const uploadAudioStreamToS3 = async (audioStream: Buffer) => {
        const remotePath = `${uuid()}.mp3`;
        await s3.send(
          new PutObjectCommand({
            Bucket: AWS_S3_BUCKET_NAME,
            Key: remotePath,
            Body: audioStream,
            ContentType: 'audio/mpeg',
          })
        );
        return remotePath;
      };
      ```
    </CodeGroup>

    You can then call uploading function with the audio stream from the text.

    <CodeGroup>
      ```python Python
      s3_file_name = upload_audiostream_to_s3(audio_stream)
      ```

      ```typescript TypeScript
      const s3path = await uploadAudioStreamToS3(stream);
      ```
    </CodeGroup>

    After uploading the audio file to S3, generate a signed URL to share access to the file. This URL will be time-limited, meaning it will expire after a certain period, making it secure for temporary sharing.

    You can now generate a URL from a file with:

    <CodeGroup>
      ```python Python
      signed_url = generate_presigned_url(s3_file_name)
      print(f"Signed URL to access the file: {signed_url}")
      ```

      ```typescript TypeScript
      const presignedUrl = await generatePresignedUrl(s3path);
      console.log('Presigned URL:', presignedUrl);
      ```
    </CodeGroup>

    If you want to use the file multiple times, you should store the s3 file path in your database and then regenerate the signed URL each time you need rather than saving the signed URL directly as it will expire.
  </Accordion>

  <Accordion title="Putting it all together">
    To put it all together, you can use the following script:

    <CodeGroup>
      ```python main.py (Python)

      import os

      from dotenv import load_dotenv

      load_dotenv()

      from text_to_speech_stream import text_to_speech_stream
      from s3_uploader import upload_audiostream_to_s3, generate_presigned_url


      def main():
          text = "This is James"

          audio_stream = text_to_speech_stream(text)
          s3_file_name = upload_audiostream_to_s3(audio_stream)
          signed_url = generate_presigned_url(s3_file_name)

          print(f"Signed URL to access the file: {signed_url}")


      if __name__ == "__main__":
          main()

      ```

      ```typescript index.ts (Typescript)
      import 'dotenv/config';

      import { generatePresignedUrl, uploadAudioStreamToS3 } from './s3_uploader';
      import { createAudioFileFromText } from './text_to_speech_file';
      import { createAudioStreamFromText } from './text_to_speech_stream';

      (async () => {
        // save the audio file to disk
        const fileName = await createAudioFileFromText(
          'Today, the sky is exceptionally clear, and the sun shines brightly.'
        );

        console.log('File name:', fileName);

        // OR stream the audio, upload to S3, and get a presigned URL
        const stream = await createAudioStreamFromText(
          'Today, the sky is exceptionally clear, and the sun shines brightly.'
        );

        const s3path = await uploadAudioStreamToS3(stream);

        const presignedUrl = await generatePresignedUrl(s3path);

        console.log('Presigned URL:', presignedUrl);
      })();
      ```
    </CodeGroup>
  </Accordion>
</AccordionGroup>


## Conclusion

You now know how to convert text into speech and generate a signed URL to share the audio file. This functionality opens up numerous opportunities for creating and sharing content dynamically.

Here are some examples of what you could build with this.

1. **Educational Podcasts**: Create personalized educational content that can be accessed by students on demand. Teachers can convert their lessons into audio format, upload them to S3, and share the links with students for a more engaging learning experience outside the traditional classroom setting.

2. **Accessibility Features for Websites**: Enhance website accessibility by offering text content in audio format. This can make information on websites more accessible to individuals with visual impairments or those who prefer auditory learning.

3. **Automated Customer Support Messages**: Produce automated and personalized audio messages for customer support, such as FAQs or order updates. This can provide a more engaging customer experience compared to traditional text emails.

4. **Audio Books and Narration**: Convert entire books or short stories into audio format, offering a new way for audiences to enjoy literature. Authors and publishers can diversify their content offerings and reach audiences who prefer listening over reading.

5. **Language Learning Tools**: Develop language learning aids that provide learners with audio lessons and exercises. This makes it possible to practice pronunciation and listening skills in a targeted way.

For more details, visit the following to see the full project files which give a clear structure for setting up your application:

For Python: [example repo](https://github.com/elevenlabs/elevenlabs-examples/tree/main/examples/text-to-speech/python)

For TypeScript: [example repo](https://github.com/elevenlabs/elevenlabs-examples/tree/main/examples/text-to-speech/node)

If you have any questions please create an issue on the [elevenlabs-doc Github](https://github.com/elevenlabs/elevenlabs-docs/issues).



# Stitching multiple requests

> Learn how to maintain voice prosody over multiple chunks/generations.

When converting a large body of text into audio, you may encounter abrupt changes in prosody from one chunk to another. This can be particularly noticeable when converting text that spans multiple paragraphs or sections. In order to maintain voice prosody over multiple chunks, you can use the Request Stitching feature.

This feature allows you to provide context on what has already been generated and what will be generated in the future, helping to maintain a consistent voice and prosody throughout the entire text.

<Info>
  Request stitching is not available for the 

  `eleven_v3`

   model.
</Info>

Here's an example without Request Stitching:

<video controls src="https://eleven-public-cdn.elevenlabs.io/audio/docs/without_request_stitching.mp3" />

And the same example with Request Stitching:

<video controls src="https://eleven-public-cdn.elevenlabs.io/audio/docs/with_request_stitching.mp3" />


## How to use Request Stitching

Request Stitching is easiest when using the ElevenLabs SDKs.

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

  <Step title="Stitch multiple requests together">
    Create a new file named `example.py` or `example.mts`, depending on your language of choice and add the following code:

    <CodeBlocks>
      ```python
      import os
      from io import BytesIO
      from elevenlabs.client import ElevenLabs
      from elevenlabs.play import play
      from dotenv import load_dotenv

      load_dotenv()

      ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")

      elevenlabs = ElevenLabs(
          api_key=ELEVENLABS_API_KEY,
      )

      paragraphs = [
          "The advent of technology has transformed countless sectors, with education ",
          "standing out as one of the most significantly impacted fields.",
          "In recent years, educational technology, or EdTech, has revolutionized the way ",
          "teachers deliver instruction and students absorb information.",
          "From interactive whiteboards to individual tablets loaded with educational software, ",
          "technology has opened up new avenues for learning that were previously unimaginable.",
          "One of the primary benefits of technology in education is the accessibility it provides.",
      ]

      request_ids = []
      audio_buffers = []

      for paragraph in paragraphs:
          # Usually we get back a stream from the convert function, but with_raw_response is
          # used to get the headers from the response
          with elevenlabs.text_to_speech.with_raw_response.convert(
              text=paragraph,
              voice_id="T7QGPtToiqH4S8VlIkMJ",
              model_id="eleven_multilingual_v2",
              previous_request_ids=request_ids
          ) as response:
              request_ids.append(response._response.headers.get("request-id"))

              # response._response.headers also contains useful information like 'character-cost',
              # which shows the cost of the generation in characters.

              audio_data = b''.join(chunk for chunk in response.data)
              audio_buffers.append(BytesIO(audio_data))

      combined_stream = BytesIO(b''.join(buffer.getvalue() for buffer in audio_buffers))

      play(combined_stream)
      ```

      ```typescript
      import "dotenv/config";
      import { ElevenLabsClient, play } from "@elevenlabs/elevenlabs-js";
      import { Readable } from "node:stream";

      const elevenlabs = new ElevenLabsClient({
          apiKey: process.env.ELEVENLABS_API_KEY,
      });

      const paragraphs = [
          "The advent of technology has transformed countless sectors, with education ",
          "standing out as one of the most significantly impacted fields.",
          "In recent years, educational technology, or EdTech, has revolutionized the way ",
          "teachers deliver instruction and students absorb information.",
          "From interactive whiteboards to individual tablets loaded with educational software, ",
          "technology has opened up new avenues for learning that were previously unimaginable.",
          "One of the primary benefits of technology in education is the accessibility it provides.",
      ];

      const requestIds: string[] = [];
      const audioBuffers: Buffer[] = [];

      for (const paragraph of paragraphs) {
          // Usually we get back a stream from the convert function, but withRawResponse() is
          // used to get the headers from the response
          const response = await elevenlabs.textToSpeech
              .convert("T7QGPtToiqH4S8VlIkMJ", {
                  text: paragraph,
                  modelId: "eleven_multilingual_v2",
                  previousRequestIds: requestIds,
              })
              .withRawResponse();

          // response.rawResponse.headers also contains useful information like 'character-cost',
          // which shows the cost of the generation in characters.

          requestIds.push(response.rawResponse.headers.get("request-id") ?? "");

          // Convert stream to buffer
          const chunks: Buffer[] = [];
          for await (const chunk of response.data) {
              chunks.push(Buffer.from(chunk));
          }
          audioBuffers.push(Buffer.concat(chunks));
      }

      // Create a single readable stream from all buffers
      const combinedStream = Readable.from(Buffer.concat(audioBuffers));

      play(combinedStream);
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

    You should hear the combined stitched audio play.
  </Step>
</Steps>


## FAQ

<AccordionGroup>
  <Accordion title="How does Request Stitching work with streaming?">
    In order to use the request IDs of a previous request for conditioning it needs to have processed completely. In case of streaming this means the audio has to be read completely from the response body.
  </Accordion>

  <Accordion title="How much difference does Request Stitching make?">
    The difference depends on the model, voice and voice settings used.
  </Accordion>

  <Accordion title="How old can the request IDs be?">
    The request IDs should be no older than two hours.
  </Accordion>

  <Accordion title="Is Request Stitching available on every plan?">
    Yes, unless you are an enterprise user with increased privacy requirements.
  </Accordion>
</AccordionGroup>



# Using pronunciation dictionaries

> Learn how to manage pronunciation dictionaries programmatically.

In this tutorial, you'll learn how to use a pronunciation dictionary with the ElevenLabs Python SDK. Pronunciation dictionaries are useful for controlling the specific pronunciation of words. We support both [IPA](https://en.wikipedia.org/wiki/International_Phonetic_Alphabet) and [CMU](https://en.wikipedia.org/wiki/CMU_Pronouncing_Dictionary) alphabets. It is useful for correcting rare or specific pronunciations, such as names or companies. For example, the word `nginx` could be pronounced incorrectly. Instead, we can add our version of pronunciation. Based on IPA, `nginx` is pronounced as `/ˈɛndʒɪnˈɛks/`. Finding IPA or CMU of words manually can be difficult. Instead, LLMs like ChatGPT can help you to make the search easier.

We'll start by adding rules to the pronunciation dictionary from a file and comparing the text-to-speech results that use and do not use the dictionary. After that, we'll discuss how to add and remove specific rules to existing dictionaries.

If you want to jump straight to the finished repo you can find it [here](https://github.com/elevenlabs/elevenlabs-examples/tree/main/examples/pronunciation-dictionaries/python)

<Info>
  Phoneme tags only work with `eleven_flash_v2`, `eleven_turbo_v2` & `eleven_monolingual_v1` models.
  If you use phoneme tags with other models, they will silently skip the word.
</Info>


## Requirements

* An ElevenLabs account with an API key (here’s how to [find your API key](/docs/api-reference/text-to-speech#authentication)).
* Python installed on your machine
* FFMPEG to play audio


## Setup

### Installing our SDK

Before you begin, make sure you have installed the necessary SDKs and libraries. You will need the ElevenLabs SDK for the updating pronunciation dictionary and using text-to-speech conversion. You can install it using pip:

```bash
pip install elevenlabs
```

Additionally, install `python-dotenv` to manage your environmental variables:

```bash
pip install python-dotenv
```

Next, create a `.env` file in your project directory and fill it with your credentials like so:

```
ELEVENLABS_API_KEY=your_elevenlabs_api_key_here
```


## Initiate the Client SDK

We'll start by initializing the client SDK.

```python
import os
from elevenlabs.client import ElevenLabs

ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
elevenlabs = ElevenLabs(
    api_key=ELEVENLABS_API_KEY,
)
```


## Create a Pronunciation Dictionary From a File

To create a pronunciation dictionary from a File, we'll create a `.pls` file for our rules.

This rule will use the "IPA" alphabet and update the pronunciation for `tomato` and `Tomato` with a different pronunciation. PLS files are case sensitive which is why we include it both with and without a capital "T". Save it as `dictionary.pls`.

```xml filename="dictionary.pls"
<?xml version="1.0" encoding="UTF-8"?>
<lexicon version="1.0"
      xmlns="http://www.w3.org/2005/01/pronunciation-lexicon"
      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      xsi:schemaLocation="http://www.w3.org/2005/01/pronunciation-lexicon
        http://www.w3.org/TR/2007/CR-pronunciation-lexicon-20071212/pls.xsd"
      alphabet="ipa" xml:lang="en-US">
  <lexeme>
    <grapheme>tomato</grapheme>
    <phoneme>/tə'meɪtoʊ/</phoneme>
  </lexeme>
  <lexeme>
    <grapheme>Tomato</grapheme>
    <phoneme>/tə'meɪtoʊ/</phoneme>
  </lexeme>
</lexicon>
```

In the following snippet, we start by adding rules from a file and get the uploaded result. Finally, we generate and play two different text-to-speech audio to compare the custom pronunciation dictionary.

```python
import requests
from elevenlabs.play import play, PronunciationDictionaryVersionLocator

with open("dictionary.pls", "rb") as f:
    # this dictionary changes how tomato is pronounced
    pronunciation_dictionary = elevenlabs.pronunciation_dictionaries.create_from_file(
        file=f.read(), name="example"
    )

audio_1 = elevenlabs.text_to_speech.convert(
    text="Without the dictionary: tomato",
    voice_id="21m00Tcm4TlvDq8ikWAM",
    model_id="eleven_turbo_v2",
)

audio_2 = elevenlabs.text_to_speech.convert(
    text="With the dictionary: tomato",
    voice_id="21m00Tcm4TlvDq8ikWAM",
    model_id="eleven_turbo_v2",
    pronunciation_dictionary_locators=[
        PronunciationDictionaryVersionLocator(
            pronunciation_dictionary_id=pronunciation_dictionary.id,
            version_id=pronunciation_dictionary.version_id,
        )
    ],
)


# play the audio
play(audio_1)
play(audio_2)
```


## Remove Rules From a Pronunciation Dictionary

To remove rules from a pronunciation dictionary, call the `remove` method in the pronunciation dictionary module. In the following snippet, we start by removing rules based on the rule string and get the updated result. Next, we generate and play another text-to-speech audio to test the difference. In the example, we get the pronunciation dictionary version ID from the `remove` method response as every change to a pronunciation dictionary will generate a new version.

```python
pronunciation_dictionary_rules_removed = (
    elevenlabs.pronunciation_dictionaries.rules.remove(
        pronunciation_dictionary_id=pronunciation_dictionary.id,
        rule_strings=["tomato", "Tomato"],
    )
)

audio_3 = elevenlabs.generate(
    text="With the rule removed: tomato",
    voice="Rachel",
    model="eleven_turbo_v2",
    pronunciation_dictionary_locators=[
        PronunciationDictionaryVersionLocator(
            pronunciation_dictionary_id=pronunciation_dictionary_rules_removed.id,
            version_id=pronunciation_dictionary_rules_removed.version_id,
        )
    ],
)

play(audio_3)
```


## Add Rules to Pronunciation Dictionary

We can add rules directly to the pronunciation dictionary by calling the `add` method. Next, generate and play another text-to-speech audio to test the difference.

```python
from elevenlabs import PronunciationDictionaryRule_Phoneme

pronunciation_dictionary_rules_added = elevenlabs.pronunciation_dictionaries.rules.add(
    pronunciation_dictionary_id=pronunciation_dictionary_rules_removed.id,
    rules=[
        PronunciationDictionaryRule_Phoneme(
            type="phoneme",
            alphabet="ipa",
            string_to_replace="tomato",
            phoneme="/tə'meɪtoʊ/",
        ),
        PronunciationDictionaryRule_Phoneme(
            type="phoneme",
            alphabet="ipa",
            string_to_replace="Tomato",
            phoneme="/tə'meɪtoʊ/",
        ),
    ],
)

audio_4 = elevenlabs.generate(
    text="With the rule added again: tomato",
    voice="Rachel",
    model="eleven_turbo_v2",
    pronunciation_dictionary_locators=[
        PronunciationDictionaryVersionLocator(
            pronunciation_dictionary_id=pronunciation_dictionary_rules_added.id,
            version_id=pronunciation_dictionary_rules_added.version_id,
        )
    ],
)

play(audio_4)
```


## Conclusion

You know how to use a pronunciation dictionary for generating text-to-speech audio. These functionalities open up opportunities to generate Text to Speech audio based on your pronunciation dictionary, making it more flexible for your use case.

For more details, visit our [example repo](https://github.com/elevenlabs/elevenlabs-examples/tree/main/examples/pronunciation-dictionaries/python) to see the full project files which give a clear structure for setting up your application:

* `env.example`: Template for your environment variables.
* `main.py`: The complete code for snippets above.
* `dictionary.pls`: Custom dictionary example with XML format.
* `requirements.txt`: List of python package used for this example.

If you have any questions please create an issue on the [elevenlabs-doc Github](https://github.com/elevenlabs/elevenlabs-docs/issues).



# Streaming and Caching with Supabase

> Generate and stream speech through Supabase Edge Functions. Store speech in Supabase Storage and cache responses via built-in CDN.


## Introduction

In this tutorial you will learn how to build and edge API to generate, stream, store, and cache speech using Supabase Edge Functions, Supabase Storage, and ElevenLabs.

<iframe width="100%" height="400" src="https://www.youtube-nocookie.com/embed/4Roog4PAmZ8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen />

<Tip title="Prefer to jump straight to the code?" icon="lightbulb">
  Find the [example project on
  GitHub](https://github.com/elevenlabs/elevenlabs-examples/tree/main/examples/text-to-speech/supabase/stream-and-cache-storage).
</Tip>


## Requirements

* An ElevenLabs account with an [API key](https://elevenlabs.io/app/settings/api-keys).
* A [Supabase](https://supabase.com) account (you can sign up for a free account via [database.new](https://database.new)).
* The [Supabase CLI](https://supabase.com/docs/guides/local-development) installed on your machine.
* The [Deno runtime](https://docs.deno.com/runtime/getting_started/installation/) installed on your machine and optionally [setup in your facourite IDE](https://docs.deno.com/runtime/getting_started/setup_your_environment).


## Setup

### Create a Supabase project locally

After installing the [Supabase CLI](https://supabase.com/docs/guides/local-development), run the following command to create a new Supabase project locally:

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

<Note>
  Upon running `supabase start` this will create a new storage bucket in your local Supabase
  project. Should you want to push this to your hosted Supabase project, you can run `supabase seed
    buckets --linked`.
</Note>

### Configure background tasks for Supabase Edge Functions

To use background tasks in Supabase Edge Functions when developing locally, you need to add the following configuration in the `config.toml` file:

```toml ./supabase/config.toml
[edge_runtime]
policy = "per_worker"
```

<Note>
  When running with `per_worker` policy, Function won't auto-reload on edits. You will need to
  manually restart it by running `supabase functions serve`.
</Note>

### Create a Supabase Edge Function for Speech generation

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

* The [@supabase/supabase-js](https://supabase.com/docs/reference/javascript) library to interact with the Supabase database.
* The ElevenLabs [JavaScript SDK](/docs/quickstart) to interact with the text-to-speech API.
* The open-source [object-hash](https://www.npmjs.com/package/object-hash) to generate a hash from the request parameters.

Since Supabase Edge Function uses the [Deno runtime](https://deno.land/), you don't need to install the dependencies, rather you can [import](https://docs.deno.com/examples/npm/) them via the `npm:` prefix.


## Code the Supabase Edge Function

In your newly created `supabase/functions/text-to-speech/index.ts` file, add the following code:

```ts supabase/functions/text-to-speech/index.ts
// Setup type definitions for built-in Supabase Runtime APIs
import 'jsr:@supabase/functions-js/edge-runtime.d.ts';
import { createClient } from 'jsr:@supabase/supabase-js@2';
import { ElevenLabsClient } from 'npm:elevenlabs';
import * as hash from 'npm:object-hash';

const supabase = createClient(
  Deno.env.get('SUPABASE_URL')!,
  Deno.env.get('SUPABASE_SERVICE_ROLE_KEY')!
);

const elevenlabs = new ElevenLabsClient({
  apiKey: Deno.env.get('ELEVENLABS_API_KEY'),
});

// Upload audio to Supabase Storage in a background task
async function uploadAudioToStorage(stream: ReadableStream, requestHash: string) {
  const { data, error } = await supabase.storage
    .from('audio')
    .upload(`${requestHash}.mp3`, stream, {
      contentType: 'audio/mp3',
    });

  console.log('Storage upload result', { data, error });
}

Deno.serve(async (req) => {
  // To secure your function for production, you can for example validate the request origin,
  // or append a user access token and validate it with Supabase Auth.
  console.log('Request origin', req.headers.get('host'));
  const url = new URL(req.url);
  const params = new URLSearchParams(url.search);
  const text = params.get('text');
  const voiceId = params.get('voiceId') ?? 'JBFqnCBsd6RMkjVDRZzb';

  const requestHash = hash.MD5({ text, voiceId });
  console.log('Request hash', requestHash);

  // Check storage for existing audio file
  const { data } = await supabase.storage.from('audio').createSignedUrl(`${requestHash}.mp3`, 60);

  if (data) {
    console.log('Audio file found in storage', data);
    const storageRes = await fetch(data.signedUrl);
    if (storageRes.ok) return storageRes;
  }

  if (!text) {
    return new Response(JSON.stringify({ error: 'Text parameter is required' }), {
      status: 400,
      headers: { 'Content-Type': 'application/json' },
    });
  }

  try {
    console.log('ElevenLabs API call');
    const response = await elevenlabs.textToSpeech.stream(voiceId, {
      output_format: 'mp3_44100_128',
      model_id: 'eleven_multilingual_v2',
      text,
    });

    const stream = new ReadableStream({
      async start(controller) {
        for await (const chunk of response) {
          controller.enqueue(chunk);
        }
        controller.close();
      },
    });

    // Branch stream to Supabase Storage
    const [browserStream, storageStream] = stream.tee();

    // Upload to Supabase Storage in the background
    EdgeRuntime.waitUntil(uploadAudioToStorage(storageStream, requestHash));

    // Return the streaming response immediately
    return new Response(browserStream, {
      headers: {
        'Content-Type': 'audio/mpeg',
      },
    });
  } catch (error) {
    console.log('error', { error });
    return new Response(JSON.stringify({ error: error.message }), {
      status: 500,
      headers: { 'Content-Type': 'application/json' },
    });
  }
});
```

### Code deep dive

There's a couple of things worth noting about the code. Let's step through it step by step.

<Steps>
  <Step title="Handle the incoming request">
    To handle the incoming request, use the `Deno.serve` handler. In the demo we don't validate the request origin, but you can for example validate the request origin, or append a user access token and validate it with [Supabase Auth](https://supabase.com/docs/guides/functions/auth).

    From the incoming request, the function extracts the `text` and `voiceId` parameters. The `voiceId` parameter is optional and defaults to the ElevenLabs ID for the "Allison" voice.

    Using the `object-hash` library, the function generates a hash from the request parameters. This hash is used to check for existing audio files in Supabase Storage.

    ```ts {1,5-8}
    Deno.serve(async (req) => {
    // To secure your function for production, you can for example validate the request origin,
    // or append a user access token and validate it with Supabase Auth.
    console.log("Request origin", req.headers.get("host"));
    const url = new URL(req.url);
    const params = new URLSearchParams(url.search);
    const text = params.get("text");
    const voiceId = params.get("voiceId") ?? "JBFqnCBsd6RMkjVDRZzb";

    const requestHash = hash.MD5({ text, voiceId });
    console.log("Request hash", requestHash);

    // ...
    })
    ```
  </Step>

  <Step title="Check for existing audio file in Supabase Storage">
    Supabase Storage comes with a [smart CDN built-in](https://supabase.com/docs/guides/storage/cdn/smart-cdn) allowing you to easily cache and serve your files.

    Here, the function checks for an existing audio file in Supabase Storage. If the file exists, the function returns the file from Supabase Storage.

    ```ts {4,9}
    const { data } = await supabase
      .storage
      .from("audio")
      .createSignedUrl(`${requestHash}.mp3`, 60);

    if (data) {
      console.log("Audio file found in storage", data);
      const storageRes = await fetch(data.signedUrl);
      if (storageRes.ok) return storageRes;
    }
    ```
  </Step>

  <Step title="Generate Speech as a stream and split into two branches">
    Using the streaming capabilities of the ElevenLabs API, the function generates a stream. The benefit here is that even for larger text, you can start streaming the audio back to your user immediately, and then upload the stream to Supabase Storage in the background.

    This allows for the best possible user experience, making even large text blocks feel magically quick. The magic here happens on line 17, where the `stream.tee()` method branches the readablestream into two branches: one for the browser and one for Supabase Storage.

    ```ts {1,17,20,22-27}
    try {
      const response = await elevenlabs.textToSpeech.stream(voiceId, {
        output_format: "mp3_44100_128",
        model_id: "eleven_multilingual_v2",
        text,
      });

      const stream = new ReadableStream({
        async start(controller) {
          for await (const chunk of response) {
            controller.enqueue(chunk);
          }
          controller.close();
        },
      });

      // Branch stream to Supabase Storage
      const [browserStream, storageStream] = stream.tee();

      // Upload to Supabase Storage in the background
      EdgeRuntime.waitUntil(uploadAudioToStorage(storageStream, requestHash));

      // Return the streaming response immediately
      return new Response(browserStream, {
        headers: {
          "Content-Type": "audio/mpeg",
        },
      });
    } catch (error) {
      console.log("error", { error });
      return new Response(JSON.stringify({ error: error.message }), {
        status: 500,
        headers: { "Content-Type": "application/json" },
      });
    }
    ```
  </Step>

  <Step title="Upload the audio stream to Supabase Storage in the background">
    The `EdgeRuntime.waitUntil` method on line 20 in the previous step is used to upload the audio stream to Supabase Storage in the background using the `uploadAudioToStorage` function. This allows the function to return the streaming response immediately to the browser, while the audio is being uploaded to Supabase Storage.

    Once the storage object has been created, the next time your users makes a request with the same parameters, the function will return the audio file from the Supabase Storage CDN.

    ```ts {2,8-10}
    // Upload audio to Supabase Storage in a background task
    async function uploadAudioToStorage(
      stream: ReadableStream,
      requestHash: string,
    ) {
      const { data, error } = await supabase.storage
        .from("audio")
        .upload(`${requestHash}.mp3`, stream, {
          contentType: "audio/mp3",
        });

      console.log("Storage upload result", { data, error });
    }
    ```
  </Step>
</Steps>


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



# Sending generated audio through Twilio

> Learn how to integrate generated speech into phone calls with Twilio.

In this guide, you’ll learn how to send an AI generated message through a phone call using Twilio and ElevenLabs. This process allows you to send high-quality voice messages directly to your callers.


## Create accounts with Twilio and ngrok

We’ll be using Twilio and ngrok for this guide, so go ahead and create accounts with them.

* [twilio.com](https://www.twilio.com)
* [ngrok.com](https://ngrok.com)


## Get the code

If you want to get started quickly, you can get the entire code for this guide on [GitHub](https://github.com/elevenlabs/elevenlabs-examples/tree/main/examples/twilio/call)


## Create the server with Express

### Initialize your project

Create a new folder for your project

```
mkdir elevenlabs-twilio
cd elevenlabs-twilio
npm init -y
```

### Install dependencies

```
npm install @elevenlabs/elevenlabs-js express express-ws twilio
```

### Install dev dependencies

```
npm i @types/node @types/express @types/express-ws @types/ws dotenv tsx typescript
```

### Create your files

```ts
// src/app.ts
import { ElevenLabsClient } from '@elevenlabs/elevenlabs-js';
import 'dotenv/config';
import express, { Response } from 'express';
import ExpressWs from 'express-ws';
import { Readable } from 'stream';
import VoiceResponse from 'twilio/lib/twiml/VoiceResponse';
import { type WebSocket } from 'ws';

const app = ExpressWs(express()).app;
const PORT: number = parseInt(process.env.PORT || '5000');

const elevenlabs = new ElevenLabsClient();
const voiceId = '21m00Tcm4TlvDq8ikWAM';
const outputFormat = 'ulaw_8000';
const text = 'This is a test. You can now hang up. Thank you.';

function startApp() {
  app.post('/call/incoming', (_, res: Response) => {
    const twiml = new VoiceResponse();

    twiml.connect().stream({
      url: `wss://${process.env.SERVER_DOMAIN}/call/connection`,
    });

    res.writeHead(200, { 'Content-Type': 'text/xml' });
    res.end(twiml.toString());
  });

  app.ws('/call/connection', (ws: WebSocket) => {
    ws.on('message', async (data: string) => {
      const message: {
        event: string;
        start?: { streamSid: string; callSid: string };
      } = JSON.parse(data);

      if (message.event === 'start' && message.start) {
        const streamSid = message.start.streamSid;
        const response = await elevenlabs.textToSpeech.convert(voiceId, {
          modelId: 'eleven_flash_v2_5',
          outputFormat: outputFormat,
          text,
        });

        const readableStream = Readable.from(response);
        const audioArrayBuffer = await streamToArrayBuffer(readableStream);

        ws.send(
          JSON.stringify({
            streamSid,
            event: 'media',
            media: {
              payload: Buffer.from(audioArrayBuffer as any).toString('base64'),
            },
          })
        );
      }
    });

    ws.on('error', console.error);
  });

  app.listen(PORT, () => {
    console.log(`Local: http://localhost:${PORT}`);
    console.log(`Remote: https://${process.env.SERVER_DOMAIN}`);
  });
}

function streamToArrayBuffer(readableStream: Readable) {
  return new Promise((resolve, reject) => {
    const chunks: Buffer[] = [];

    readableStream.on('data', (chunk) => {
      chunks.push(chunk);
    });

    readableStream.on('end', () => {
      resolve(Buffer.concat(chunks).buffer);
    });

    readableStream.on('error', reject);
  });
}

startApp();
```

```env

# .env
SERVER_DOMAIN=
ELEVENLABS_API_KEY=
```


## Understanding the code

### Handling the incoming call

When you call your number, Twilio makes a POST request to your endpoint at `/call/incoming`.
We then use twiml.connect to tell Twilio that we want to handle the call via our websocket by setting the url to our `/call/connection` endpoint.

```ts
function startApp() {
  app.post('/call/incoming', (_, res: Response) => {
    const twiml = new VoiceResponse();

    twiml.connect().stream({
      url: `wss://${process.env.SERVER_DOMAIN}/call/connection`,
    });

    res.writeHead(200, { 'Content-Type': 'text/xml' });
    res.end(twiml.toString());
  });
```

### Creating the text to speech

Here we listen for messages that Twilio sends to our websocket endpoint. When we receive a `start` message event, we generate audio using the ElevenLabs [TypeScript SDK](https://github.com/elevenlabs/elevenlabs-js).

```ts
  app.ws('/call/connection', (ws: WebSocket) => {
    ws.on('message', async (data: string) => {
      const message: {
        event: string;
        start?: { streamSid: string; callSid: string };
      } = JSON.parse(data);

      if (message.event === 'start' && message.start) {
        const streamSid = message.start.streamSid;
        const response = await elevenlabs.textToSpeech.convert(voiceId, {
          modelId: 'eleven_flash_v2_5',
          outputFormat: outputFormat,
          text,
        });
```

### Sending the message

Upon receiving the audio back from ElevenLabs, we convert it to an array buffer and send the audio to Twilio via the websocket.

```ts
const readableStream = Readable.from(response);
const audioArrayBuffer = await streamToArrayBuffer(readableStream);

ws.send(
  JSON.stringify({
    streamSid,
    event: 'media',
    media: {
      payload: Buffer.from(audioArrayBuffer as any).toString('base64'),
    },
  })
);
```


## Point ngrok to your application

Twilio requires a publicly accessible URL. We’ll use ngrok to forward the local port of our application and expose it as a public URL.

Run the following command in your terminal:

```
ngrok http 5000
```

Copy the ngrok domain (without https\://) to use in your environment variables.

<img src="file:7f8e9cc9-25fa-41a8-b1eb-5b8bb2e7193c" />


## Update your environment variables

Update the `.env` file with your ngrok domain and ElevenLabs API key.

```

# .env
SERVER_DOMAIN=*******.ngrok.app
ELEVENLABS_API_KEY=*************************
```


## Start the application

Run the following command to start the app:

```
npm run dev
```


## Set up Twilio

Follow Twilio’s guides to create a new number. Once you’ve created your number, navigate to the “Configure” tab in Phone Numbers -> Manage -> Active numbers

In the “A call comes in” section, enter the full URL to your application (make sure to add the`/call/incoming` path):

E.g. https\://**\*\*\***&#x6E;grok.app/call/incoming

<img src="file:38a7ec1f-8734-4bd1-97f9-3f2653ebff00" />


## Make a phone call

Make a call to your number. You should hear a message using the ElevenLabs voice.


## Tips for deploying to production

When running the application in production, make sure to set the `SERVER_DOMAIN` environment variable to that of your server. Be sure to also update the URL in Twilio to point to your production server.


## Conclusion

You should now have a basic understanding of integrating Twilio with ElevenLabs voices. If you have any further questions, or suggestions on how to improve this blog post, please feel free to select the “Suggest edits” or “Raise issue” button below.



# Text to Dialogue quickstart

> Learn how to generate immersive dialogue from text.

This guide will show you how to generate immersive, natural-sounding dialogue from text using the Text to Dialogue API.


## Using the Text to Dialogue API

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
      from dotenv import load_dotenv
      from elevenlabs.client import ElevenLabs
      from elevenlabs.play import play

      load_dotenv()

      elevenlabs = ElevenLabs(
        api_key=os.getenv("ELEVENLABS_API_KEY"),
      )

      audio = elevenlabs.text_to_dialogue.convert(
          inputs=[
              {
                  "text": "[cheerfully] Hello, how are you?",
                  "voice_id": "9BWtsMINqrJLrRacOk9x",
              },
              {
                  "text": "[stuttering] I'm... I'm doing well, thank you",
                  "voice_id": "IKne3meq5aSn9XLyUdCD",
              }
          ]
      )

      play(audio)
      ```

      ```typescript maxLines=0
      // example.mts
      import { ElevenLabsClient, play } from "@elevenlabs/elevenlabs-js";
      import "dotenv/config";

      const elevenlabs = new ElevenLabsClient();

      const audio = await elevenlabs.textToDialogue.convert({
          inputs: [
              {
                  text: "[cheerfully] Hello, how are you?",
                  voiceId: "9BWtsMINqrJLrRacOk9x",
              },
              {
                  text: "[stuttering] I'm... I'm doing well, thank you",
                  voiceId: "IKne3meq5aSn9XLyUdCD",
              },
          ],
      });

      play(audio);
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

    You should hear the dialogue audio play.
  </Step>
</Steps>


## Next steps

Explore the [API reference](/docs/api-reference/text-to-dialogue/convert) for more information on the Text to Dialogue API and its options.



# Speech to Text quickstart

> Learn how to convert spoken audio into text.

This guide will show you how to convert spoken audio into text using the Speech to Text API.


## Using the Speech to Text API

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
      from dotenv import load_dotenv
      from io import BytesIO
      import requests
      from elevenlabs.client import ElevenLabs

      load_dotenv()

      elevenlabs = ElevenLabs(
        api_key=os.getenv("ELEVENLABS_API_KEY"),
      )

      audio_url = (
          "https://storage.googleapis.com/eleven-public-cdn/audio/marketing/nicole.mp3"
      )
      response = requests.get(audio_url)
      audio_data = BytesIO(response.content)

      transcription = elevenlabs.speech_to_text.convert(
          file=audio_data,
          model_id="scribe_v1", # Model to use, for now only "scribe_v1" is supported
          tag_audio_events=True, # Tag audio events like laughter, applause, etc.
          language_code="eng", # Language of the audio file. If set to None, the model will detect the language automatically.
          diarize=True, # Whether to annotate who is speaking
      )

      print(transcription)
      ```

      ```typescript maxLines=0
      // example.mts
      import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";
      import "dotenv/config";

      const elevenlabs = new ElevenLabsClient();

      const response = await fetch(
        "https://storage.googleapis.com/eleven-public-cdn/audio/marketing/nicole.mp3"
      );
      const audioBlob = new Blob([await response.arrayBuffer()], { type: "audio/mp3" });

      const transcription = await elevenlabs.speechToText.convert({
        file: audioBlob,
        modelId: "scribe_v1", // Model to use, for now only "scribe_v1" is supported.
        tagAudioEvents: true, // Tag audio events like laughter, applause, etc.
        languageCode: "eng", // Language of the audio file. If set to null, the model will detect the language automatically.
        diarize: true, // Whether to annotate who is speaking
      });

      console.log(transcription);
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

    You should see the transcription of the audio file printed to the console.
  </Step>
</Steps>


## Next steps

Explore the [API reference](/docs/api-reference/speech-to-text/convert) for more information on the Speech to Text API and its options.



# Multichannel speech-to-text

> Learn how to leverage the multichannel transcription mode.


## Overview

The multichannel Speech to Text feature enables you to transcribe audio files where each channel contains a distinct speaker. This is particularly useful for recordings where speakers are isolated on separate audio channels, providing cleaner transcriptions without the need for speaker diarization.

Each channel is processed independently and automatically assigned a speaker ID based on its channel number (channel 0 → `speaker_0`, channel 1 → `speaker_1`, etc.). The system extracts individual channels from your input audio file and transcribes them in parallel, combining the results sorted by timestamp.

### Common use cases

* **Stereo interview recordings** - Interviewer on left channel, interviewee on right channel
* **Multi-track podcast recordings** - Each participant recorded on a separate track
* **Call center recordings** - Agent and customer separated on different channels
* **Conference recordings** - Individual participants isolated on separate channels
* **Court proceedings** - Multiple parties recorded on distinct channels


## Requirements

* An ElevenLabs account with an [API key](https://elevenlabs.io/app/settings/api-keys)
* Multichannel audio file (WAV, MP3, or other supported formats)
* Maximum 5 channels per audio file
* Each channel should contain only one speaker


## How it works

<Steps>
  <Step title="Prepare your multichannel audio">
    Ensure your audio file has speakers isolated on separate channels. The multichannel feature supports up to 5 channels, with each channel mapped to a specific speaker:

    * Channel 0 → `speaker_0`
    * Channel 1 → `speaker_1`
    * Channel 2 → `speaker_2`
    * Channel 3 → `speaker_3`
    * Channel 4 → `speaker_4`
  </Step>

  <Step title="Configure API parameters">
    When making a speech-to-text request, you must set:

    * `use_multi_channel`: `true`
    * `diarize`: `false` (multichannel mode handles speaker separation via channels)

    The `num_speakers` parameter cannot be used with multichannel mode as the speaker count is automatically determined by the number of channels. Multichannel mode assumes there will exactly one speaker per channel. If there are more, it will assign the same speaker id to all speakers in the channel.
  </Step>

  <Step title="Process the response">
    The API returns a different response format for multichannel audio:

    <Note>
      If you set `use_multi_channel: true` but provide a single-channel (mono) audio file, you'll
      receive a standard single-channel response, not the multichannel format. The multichannel response
      format is only returned when the audio file actually contains multiple channels.
    </Note>

    <CodeBlocks>
      ```python title="Single channel response"
      {
        "language_code": "en",
        "language_probability": 0.98,
        "text": "Hello world",
        "words": [...]
      }
      ```

      ```python title="Multichannel response"
      {
        "transcripts": [
          {
            "language_code": "en",
            "language_probability": 0.98,
            "text": "Hello from channel one.",
            "channel_index": 0,
            "words": [...]
          },
          {
            "language_code": "en",
            "language_probability": 0.97,
            "text": "Greetings from channel two.",
            "channel_index": 1,
            "words": [...]
          }
        ]
      }
      ```
    </CodeBlocks>
  </Step>
</Steps>


## Implementation

### Basic multichannel transcription

Here's a complete example of transcribing a stereo audio file with two speakers:

<CodeBlocks>
  ```python title="Python"
  from elevenlabs import ElevenLabs

  elevenlabs = ElevenLabs(api_key="YOUR_API_KEY")

  def transcribe_multichannel(audio_file_path):
      with open(audio_file_path, 'rb') as audio_file:
          result = elevenlabs.speech_to_text.convert(
              file=audio_file,
              model_id='scribe_v1',
              use_multi_channel=True,
              diarize=False,
              timestamps_granularity='word'
          )
      return result

  # Process the response

  result = transcribe_multichannel('stereo_interview.wav')

  if hasattr(result, 'transcripts'): # Multichannel response
      for transcript in result.transcripts:
          channel = transcript.channel_index
          text = transcript.text
          print(f"Channel {channel} (speaker_{channel}): {text}")
      else: # Single channel response (fallback)
          print(f"Text: {result.text}")

  ```

  ```javascript title="JavaScript"
  import { ElevenLabsClient } from 'elevenlabs';
  import fs from 'fs';

  const elevenlabs = new ElevenLabsClient({
    apiKey: process.env.ELEVENLABS_API_KEY,
  });

  async function transcribeMultichannel(audioFilePath) {
    try {
      const audioFile = fs.createReadStream(audioFilePath);

      const result = await elevenlabs.speechToText.convert({
        file: audioFile,
        modelId: 'scribe_v1',
        useMultiChannel: true,
        diarize: false,
        timestampsGranularity: 'word',
      });

      if (result.transcripts) {
        // Multichannel response
        result.transcripts.forEach((transcript, index) => {
          console.log(`Channel ${transcript.channel_index}: ${transcript.text}`);
        });
      } else {
        // Single channel response
        console.log(`Text: ${result.text}`);
      }

      return result;
    } catch (error) {
      console.error('Error transcribing audio:', error);
      throw error;
    }
  }
  ```

  ```bash title="cURL"
  curl -X POST "https://api.elevenlabs.io/v1/speech-to-text" \
    -H "xi-api-key: YOUR_API_KEY" \
    -F "file=@stereo_audio_file.wav" \
    -F "model_id=scribe_v1" \
    -F "use_multi_channel=true" \
    -F "diarize=false" \
    -F "timestamps_granularity=word"
  ```
</CodeBlocks>

### Creating conversation transcripts

Generate a time-ordered conversation transcript from multichannel audio:

```python
def create_conversation_transcript(multichannel_result):
    """Create a conversation-style transcript with speaker labels"""
    all_words = []

    if hasattr(multichannel_result, 'transcripts'):
        # Collect all words from all channels
        for transcript in multichannel_result.transcripts:
            for word in transcript.words or []:
                if word.type == 'word':
                    all_words.append({
                        'text': word.text,
                        'start': word.start,
                        'speaker_id': word.speaker_id,
                        'channel': transcript.channel_index
                    })

    # Sort by timestamp
    all_words.sort(key=lambda w: w['start'])

    # Group consecutive words by speaker
    conversation = []
    current_speaker = None
    current_text = []

    for word in all_words:
        if word['speaker_id'] != current_speaker:
            if current_text:
                conversation.append({
                    'speaker': current_speaker,
                    'text': ' '.join(current_text)
                })
            current_speaker = word['speaker_id']
            current_text = [word['text']]
        else:
            current_text.append(word['text'])

    # Add the last segment
    if current_text:
        conversation.append({
            'speaker': current_speaker,
            'text': ' '.join(current_text)
        })

    return conversation


# Format the output
conversation = create_conversation_transcript(result)
for turn in conversation:
    print(f"{turn['speaker']}: {turn['text']}")
```


## Using webhooks with multichannel

Multichannel transcription fully supports [webhook delivery](/docs/cookbooks/speech-to-text/webhooks) for asynchronous processing:

```python
from elevenlabs import ElevenLabs

elevenlabs = ElevenLabs(api_key="YOUR_API_KEY")

async def transcribe_multichannel_with_webhook(audio_file_path):
    with open(audio_file_path, 'rb') as audio_file:
        result = await elevenlabs.speech_to_text.convert_async(
            file=audio_file,
            model_id='scribe_v1',
            use_multi_channel=True,
            diarize=False,
            webhook=True  # Enable webhook delivery
        )

    print(f"Transcription started with task ID: {result.task_id}")
    return result.task_id
```


## Error handling

### Common validation errors

<AccordionGroup>
  <Accordion title="Setting diarize=true with multichannel mode">
    **Error**: Multichannel mode does not support diarization and assigns speakers based on the
    channel they speak on.

    **Solution**: Always set `diarize=false` when using multichannel mode.
  </Accordion>

  <Accordion title="Providing num_speakers parameter">
    **Error**: Cannot specify num\_speakers when use\_multi\_channel is enabled. The number of speakers
    is automatically determined by the number of channels. **Solution**: Remove the `num_speakers`
    parameter from your request.
  </Accordion>

  <Accordion title="Audio file with more than 5 channels">
    **Error**: Multichannel mode supports up to 5 channels, but the audio file contains X channels.

    **Solution**: Process only the first 5 channels or pre-process your audio to reduce channel
    count.
  </Accordion>
</AccordionGroup>


## Best practices

### Audio preparation

<Tip>
  For optimal results: - Use 16kHz sample rate for better performance - Remove silent or unused
  channels before processing - Ensure each channel contains only one speaker - Use lossless formats
  (WAV) when possible for best quality
</Tip>

### Performance optimization

The concurrency cost increases linearly with the number of channels. A 60-second 3-channel file has 3x the concurrency cost of a single-channel file.

You can estimate the processing time for multichannel audio using the following formula:

$$
Processing\ Time = (D \cdot 0.3) + 2 + (N \cdot 0.5)
$$

Where:

* $D$ = file duration in seconds
* $N$ = number of channels
* $0.3$ = processing speed factor (approximately 30% of real-time)
* $2$ = fixed overhead in seconds
* $0.5$ = per-channel overhead in seconds

**Example**: For a 60-second stereo file (2 channels):

$$
Processing\ Time = (60 \cdot 0.3) + 2 + (2 \cdot 0.5) = 18 + 2 + 1 = 21\ seconds
$$

### Memory considerations

For large multichannel files, consider streaming or chunking:

<CodeBlocks>
  ```python title="Python"
  def process_large_multichannel_file(file_path, chunk_duration=300):
      """Process large files in chunks (5-minute segments)"""

      from pydub import AudioSegment
      from elevenlabs import ElevenLabs
      import os

      elevenlabs = ElevenLabs(api_key="YOUR_API_KEY")
      audio = AudioSegment.from_file(file_path)
      duration_ms = len(audio)
      chunk_size_ms = chunk_duration * 1000

      all_transcripts = []

      for start_ms in range(0, duration_ms, chunk_size_ms):
          end_ms = min(start_ms + chunk_size_ms, duration_ms)

          # Extract chunk
          chunk = audio[start_ms:end_ms]
          chunk_file = f"temp_chunk_{start_ms}.wav"
          chunk.export(chunk_file, format="wav")

          # Transcribe chunk using SDK
          with open(chunk_file, 'rb') as audio_file:
              result = elevenlabs.speech_to_text.convert(
                  file=audio_file,
                  model_id='scribe_v1',
                  use_multi_channel=True,
                  diarize=False,
                  timestamps_granularity='word'
              )

          # Adjust timestamps
          if hasattr(result, 'transcripts'):
              for transcript in result.transcripts:
                  for word in transcript.words or []:
                      word.start += start_ms / 1000
                      word.end += start_ms / 1000
              all_transcripts.extend(result.transcripts)

          # Clean up
          os.remove(chunk_file)

      return all_transcripts

  ```

  ```javascript title="JavaScript"
  import { exec } from 'child_process';
  import { ElevenLabsClient } from 'elevenlabs';
  import fs from 'fs';
  import path from 'path';
  import { promisify } from 'util';

  const execAsync = promisify(exec);
  const elevenlabs = new ElevenLabsClient({
    apiKey: process.env.ELEVENLABS_API_KEY,
  });

  async function processLargeMultichannelFile(filePath, chunkDuration = 300) {
    /**
     * Process large files in chunks (5-minute segments)
     * Requires ffmpeg to be installed
     */

    // Get audio duration using ffprobe
    const { stdout } = await execAsync(
      `ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "${filePath}"`
    );
    const durationSeconds = parseFloat(stdout);

    const allTranscripts = [];

    for (let startSeconds = 0; startSeconds < durationSeconds; startSeconds += chunkDuration) {
      const endSeconds = Math.min(startSeconds + chunkDuration, durationSeconds);
      const chunkFile = path.join(path.dirname(filePath), `temp_chunk_${startSeconds}.wav`);

      // Extract chunk using ffmpeg
      await execAsync(
        `ffmpeg -i "${filePath}" -ss ${startSeconds} -t ${chunkDuration} -c:a pcm_s16le "${chunkFile}" -y`
      );

      try {
        // Transcribe chunk
        const audioFile = fs.createReadStream(chunkFile);
        const result = await elevenlabs.speechToText.convert({
          file: audioFile,
          modelId: 'scribe_v1',
          useMultiChannel: true,
          diarize: false,
          timestampsGranularity: 'word',
        });

        // Adjust timestamps
        if (result.transcripts) {
          for (const transcript of result.transcripts) {
            for (const word of transcript.words || []) {
              word.start += startSeconds;
              word.end += startSeconds;
            }
          }
          allTranscripts.push(...result.transcripts);
        }
      } finally {
        // Clean up
        fs.unlinkSync(chunkFile);
      }
    }

    return { transcripts: allTranscripts };
  }
  ```
</CodeBlocks>


## FAQ

<AccordionGroup>
  <Accordion title="What happens if my audio has more than 5 channels?">
    The API will return an error. You'll need to either select which 5 channels to send to the API
    or mix down some channels before sending them to the API.
  </Accordion>

  <Accordion title="Can I process mono audio with multichannel mode?">
    Yes, but it's unnecessary. If you send mono audio with `use_multi_channel=true`, you'll receive
    a standard single-channel response, not the multichannel format.
  </Accordion>

  <Accordion title="How are speaker IDs assigned?">
    Speaker IDs are deterministic based on channel number: channel 0 becomes speaker\_0, channel 1
    becomes speaker\_1, and so on.
  </Accordion>

  <Accordion title="Can channels have different languages?">
    Yes, each channel is processed independently and can detect different languages. The language
    detection happens per channel.
  </Accordion>
</AccordionGroup>



# Transcription Telegram Bot

> Build a Telegram bot that transcribes audio and video messages in 99 languages using TypeScript with Deno in Supabase Edge Functions.


## Introduction

In this tutorial you will learn how to build a Telegram bot that transcribes audio and video messages in 99 languages using TypeScript and the ElevenLabs Scribe model via the speech-to-text API.

To check out what the end result will look like, you can test out the [t.me/ElevenLabsScribeBot](https://t.me/ElevenLabsScribeBot)

<iframe width="100%" height="400" src="https://www.youtube-nocookie.com/embed/CE4iPp7kd7Q" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen />

<Tip title="Prefer to jump straight to the code?" icon="lightbulb">
  Find the [example project on
  GitHub](https://github.com/elevenlabs/elevenlabs-examples/tree/main/examples/speech-to-text/telegram-transcription-bot).
</Tip>


## Requirements

* An ElevenLabs account with an [API key](https://elevenlabs.io/app/settings/api-keys).
* A [Supabase](https://supabase.com) account (you can sign up for a free account via [database.new](https://database.new)).
* The [Supabase CLI](https://supabase.com/docs/guides/local-development) installed on your machine.
* The [Deno runtime](https://docs.deno.com/runtime/getting_started/installation/) installed on your machine and optionally [setup in your facourite IDE](https://docs.deno.com/runtime/getting_started/setup_your_environment).
* A [Telegram](https://telegram.org) account.


## Setup

### Register a Telegram bot

Use the [BotFather](https://t.me/BotFather) to create a new Telegram bot. Run the `/newbot` command and follow the instructions to create a new bot. At the end, you will receive your secret bot token. Note it down securely for the next step.

![BotFather](file:454ab81d-7d9c-49e0-9f5d-4d4e2389b549)

### Create a Supabase project locally

After installing the [Supabase CLI](https://supabase.com/docs/guides/local-development), run the following command to create a new Supabase project locally:

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

---
**Navigation:** [← Previous](./03-february-17-2025.md) | [Index](./index.md) | [Next →](./05-find-create-an-api-key-at-httpselevenlabsioappsett.md)
