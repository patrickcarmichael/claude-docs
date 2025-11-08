**Navigation:** [← Previous](./01-quickstart.md) | [Index](./index.md) | [Next →](./03-tool-calling.md)

---

# Image Generation

> Generate images using AI models through the OpenRouter API.

OpenRouter supports image generation through models that have `"image"` in their `output_modalities`. These models can create images from text prompts when you specify the appropriate modalities in your request.

## Model Discovery

You can find image generation models in several ways:

### On the Models Page

Visit the [Models page](/models) and filter by output modalities to find models capable of image generation. Look for models that list `"image"` in their output modalities.

### In the Chatroom

When using the [Chatroom](/chat), click the **Image** button to automatically filter and select models with image generation capabilities. If no image-capable model is active, you'll be prompted to add one.

## API Usage

To generate images, send a request to the `/api/v1/chat/completions` endpoint with the `modalities` parameter set to include both `"image"` and `"text"`.

### Basic Image Generation

<Template
  data={{
  API_KEY_REF,
  MODEL: 'google/gemini-2.5-flash-image-preview'
}}
>
  <CodeGroup>
    ```typescript title="TypeScript SDK"
    import { OpenRouter } from '@openrouter/sdk';

    const openRouter = new OpenRouter({
      apiKey: '{{API_KEY_REF}}',
    });

    const result = await openRouter.chat.send({
      model: '{{MODEL}}',
      messages: [
        {
          role: 'user',
          content: 'Generate a beautiful sunset over mountains',
        },
      ],
      modalities: ['image', 'text'],
      stream: false,
    });

    // The generated image will be in the assistant message
    if (result.choices) {
      const message = result.choices[0].message;
      if (message.images) {
        message.images.forEach((image, index) => {
          const imageUrl = image.imageUrl.url; // Base64 data URL
          console.log(`Generated image ${index + 1}: ${imageUrl.substring(0, 50)}...`);
        });
      }
    }
    ```

    ```python
    import requests
    import json

    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY_REF}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "{{MODEL}}",
        "messages": [
            {
                "role": "user",
                "content": "Generate a beautiful sunset over mountains"
            }
        ],
        "modalities": ["image", "text"]
    }

    response = requests.post(url, headers=headers, json=payload)
    result = response.json()

    # The generated image will be in the assistant message
    if result.get("choices"):
        message = result["choices"][0]["message"]
        if message.get("images"):
            for image in message["images"]:
                image_url = image["image_url"]["url"]  # Base64 data URL
                print(f"Generated image: {image_url[:50]}...")
    ```

    ```typescript title="TypeScript (fetch)"
    const response = await fetch('https://openrouter.ai/api/v1/chat/completions', {
      method: 'POST',
      headers: {
        Authorization: `Bearer ${API_KEY_REF}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        model: '{{MODEL}}',
        messages: [
          {
            role: 'user',
            content: 'Generate a beautiful sunset over mountains',
          },
        ],
        modalities: ['image', 'text'],
      }),
    });

    const result = await response.json();

    // The generated image will be in the assistant message
    if (result.choices) {
      const message = result.choices[0].message;
      if (message.images) {
        message.images.forEach((image, index) => {
          const imageUrl = image.image_url.url; // Base64 data URL
          console.log(`Generated image ${index + 1}: ${imageUrl.substring(0, 50)}...`);
        });
      }
    }
    ```
  </CodeGroup>
</Template>

### Image Aspect Ratio Configuration

Gemini image-generation models let you request specific aspect ratios by setting `image_config.aspect_ratio`. Read more about using Gemini Image Gen models here: [https://ai.google.dev/gemini-api/docs/image-generation](https://ai.google.dev/gemini-api/docs/image-generation)

**Supported aspect ratios:**

* `1:1` → 1024×1024 (default)
* `2:3` → 832×1248
* `3:2` → 1248×832
* `3:4` → 864×1184
* `4:3` → 1184×864
* `4:5` → 896×1152
* `5:4` → 1152×896
* `9:16` → 768×1344
* `16:9` → 1344×768
* `21:9` → 1536×672

<Template
  data={{
  API_KEY_REF,
  MODEL: 'google/gemini-2.5-flash-image-preview'
}}
>
  <CodeGroup>
    ```python
    import requests
    import json

    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY_REF}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "{{MODEL}}",
        "messages": [
            {
                "role": "user",
                "content": "Create a picture of a nano banana dish in a fancy restaurant with a Gemini theme"
            }
        ],
        "modalities": ["image", "text"],
        "image_config": {
            "aspect_ratio": "16:9"
        }
    }

    response = requests.post(url, headers=headers, json=payload)
    result = response.json()

    if result.get("choices"):
        message = result["choices"][0]["message"]
        if message.get("images"):
            for image in message["images"]:
                image_url = image["image_url"]["url"]
                print(f"Generated image: {image_url[:50]}...")
    ```

    ```typescript
    const response = await fetch('https://openrouter.ai/api/v1/chat/completions', {
      method: 'POST',
      headers: {
        Authorization: `Bearer ${API_KEY_REF}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        model: '{{MODEL}}',
        messages: [
          {
            role: 'user',
            content: 'Create a picture of a nano banana dish in a fancy restaurant with a Gemini theme',
          },
        ],
        modalities: ['image', 'text'],
        image_config: {
          aspect_ratio: '16:9',
        },
      }),
    });

    const result = await response.json();

    if (result.choices) {
      const message = result.choices[0].message;
      if (message.images) {
        message.images.forEach((image, index) => {
          const imageUrl = image.image_url.url;
          console.log(`Generated image ${index + 1}: ${imageUrl.substring(0, 50)}...`);
        });
      }
    }
    ```
  </CodeGroup>
</Template>

### Streaming Image Generation

Image generation also works with streaming responses:

<Template
  data={{
  API_KEY_REF,
  MODEL: 'google/gemini-2.5-flash-image-preview'
}}
>
  <CodeGroup>
    ```python
    import requests
    import json

    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY_REF}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "{{MODEL}}",
        "messages": [
            {
                "role": "user",
                "content": "Create an image of a futuristic city"
            }
        ],
        "modalities": ["image", "text"],
        "stream": True
    }

    response = requests.post(url, headers=headers, json=payload, stream=True)

    for line in response.iter_lines():
        if line:
            line = line.decode('utf-8')
            if line.startswith('data: '):
                data = line[6:]
                if data != '[DONE]':
                    try:
                        chunk = json.loads(data)
                        if chunk.get("choices"):
                            delta = chunk["choices"][0].get("delta", {})
                            if delta.get("images"):
                                for image in delta["images"]:
                                    print(f"Generated image: {image['image_url']['url'][:50]}...")
                    except json.JSONDecodeError:
                        continue
    ```

    ```typescript
    const response = await fetch('https://openrouter.ai/api/v1/chat/completions', {
      method: 'POST',
      headers: {
        Authorization: `Bearer ${API_KEY_REF}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        model: '{{MODEL}}',
        messages: [
          {
            role: 'user',
            content: 'Create an image of a futuristic city',
          },
        ],
        modalities: ['image', 'text'],
        stream: true,
      }),
    });

    const reader = response.body?.getReader();
    const decoder = new TextDecoder();

    while (true) {
      const { done, value } = await reader.read();
      if (done) break;

      const chunk = decoder.decode(value);
      const lines = chunk.split('\n');

      for (const line of lines) {
        if (line.startsWith('data: ')) {
          const data = line.slice(6);
          if (data !== '[DONE]') {
            try {
              const parsed = JSON.parse(data);
              if (parsed.choices) {
                const delta = parsed.choices[0].delta;
                if (delta?.images) {
                  delta.images.forEach((image, index) => {
                    console.log(`Generated image ${index + 1}: ${image.image_url.url.substring(0, 50)}...`);
                  });
                }
              }
            } catch (e) {
              // Skip invalid JSON
            }
          }
        }
      }
    }
    ```
  </CodeGroup>
</Template>

## Response Format

When generating images, the assistant message includes an `images` field containing the generated images:

```json
{
  "choices": [
    {
      "message": {
        "role": "assistant",
        "content": "I've generated a beautiful sunset image for you.",
        "images": [
          {
            "type": "image_url",
            "image_url": {
              "url": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAA..."
            }
          }
        ]
      }
    }
  ]
}
```

### Image Format

* **Format**: Images are returned as base64-encoded data URLs
* **Types**: Typically PNG format (`data:image/png;base64,`)
* **Multiple Images**: Some models can generate multiple images in a single response
* **Size**: Image dimensions vary by model capabilities

## Model Compatibility

Not all models support image generation. To use this feature:

1. **Check Output Modalities**: Ensure the model has `"image"` in its `output_modalities`
2. **Set Modalities Parameter**: Include `"modalities": ["image", "text"]` in your request
3. **Use Compatible Models**: Examples include:
   * `google/gemini-2.5-flash-image-preview`
   * Other models with image generation capabilities

## Best Practices

* **Clear Prompts**: Provide detailed descriptions for better image quality
* **Model Selection**: Choose models specifically designed for image generation
* **Error Handling**: Check for the `images` field in responses before processing
* **Rate Limits**: Image generation may have different rate limits than text generation
* **Storage**: Consider how you'll handle and store the base64 image data

## Troubleshooting

**No images in response?**

* Verify the model supports image generation (`output_modalities` includes `"image"`)
* Ensure you've included `"modalities": ["image", "text"]` in your request
* Check that your prompt is requesting image generation

**Model not found?**

* Use the [Models page](/models) to find available image generation models
* Filter by output modalities to see compatible models


# PDF Inputs

> Send PDF documents to any model on OpenRouter.

OpenRouter supports PDF processing through the `/api/v1/chat/completions` API. PDFs can be sent as **direct URLs** or **base64-encoded data URLs** in the messages array, via the file content type. This feature works on **any** model on OpenRouter.

**URL support**: Send publicly accessible PDFs directly without downloading or encoding
**Base64 support**: Required for local files or private documents that aren't publicly accessible

PDFs also work in the chat room for interactive testing.

<Info>
  When a model supports file input natively, the PDF is passed directly to the
  model. When the model does not support file input natively, OpenRouter will
  parse the file and pass the parsed results to the requested model.
</Info>

<Tip>
  You can send both PDFs and other file types in the same request.
</Tip>

## Plugin Configuration

To configure PDF processing, use the `plugins` parameter in your request. OpenRouter provides several PDF processing engines with different capabilities and pricing:

```typescript
{
  plugins: [
    {
      id: 'file-parser',
      pdf: {
        engine: 'pdf-text', // or 'mistral-ocr' or 'native'
      },
    },
  ],
}
```

## Pricing

OpenRouter provides several PDF processing engines:

1. <code>"{PDFParserEngine.MistralOCR}"</code>: Best for scanned documents or
   PDFs with images (\${MISTRAL_OCR_COST.toString()} per 1,000 pages).
2. <code>"{PDFParserEngine.PDFText}"</code>: Best for well-structured PDFs with
   clear text content (Free).
3. <code>"{PDFParserEngine.Native}"</code>: Only available for models that
   support file input natively (charged as input tokens).

If you don't explicitly specify an engine, OpenRouter will default first to the model's native file processing capabilities, and if that's not available, we will use the <code>"{DEFAULT_PDF_ENGINE}"</code> engine.

## Using PDF URLs

For publicly accessible PDFs, you can send the URL directly without needing to download and encode the file:

<Template
  data={{
  API_KEY_REF,
  MODEL: 'anthropic/claude-sonnet-4',
  ENGINE: PDFParserEngine.MistralOCR,
}}
>
  <CodeGroup>
    ```typescript title="TypeScript SDK"
    import { OpenRouter } from '@openrouter/sdk';

    const openRouter = new OpenRouter({
      apiKey: '{{API_KEY_REF}}',
    });

    const result = await openRouter.chat.send({
      model: '{{MODEL}}',
      messages: [
        {
          role: 'user',
          content: [
            {
              type: 'text',
              text: 'What are the main points in this document?',
            },
            {
              type: 'file',
              file: {
                filename: 'document.pdf',
                fileData: 'https://bitcoin.org/bitcoin.pdf',
              },
            },
          ],
        },
      ],
      // Optional: Configure PDF processing engine
      plugins: [
        {
          id: 'file-parser',
          pdf: {
            engine: '{{ENGINE}}',
          },
        },
      ],
      stream: false,
    });

    console.log(result);
    ```

    ```python
    import requests
    import json

    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY_REF}",
        "Content-Type": "application/json"
    }

    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "What are the main points in this document?"
                },
                {
                    "type": "file",
                    "file": {
                        "filename": "document.pdf",
                        "file_data": "https://bitcoin.org/bitcoin.pdf"
                    }
                },
            ]
        }
    ]

    # Optional: Configure PDF processing engine
    plugins = [
        {
            "id": "file-parser",
            "pdf": {
                "engine": "{{ENGINE}}"
            }
        }
    ]

    payload = {
        "model": "{{MODEL}}",
        "messages": messages,
        "plugins": plugins
    }

    response = requests.post(url, headers=headers, json=payload)
    print(response.json())
    ```

    ```typescript title="TypeScript (fetch)"
    const response = await fetch('https://openrouter.ai/api/v1/chat/completions', {
      method: 'POST',
      headers: {
        Authorization: `Bearer ${API_KEY_REF}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        model: '{{MODEL}}',
        messages: [
          {
            role: 'user',
            content: [
              {
                type: 'text',
                text: 'What are the main points in this document?',
              },
              {
                type: 'file',
                file: {
                  filename: 'document.pdf',
                  file_data: 'https://bitcoin.org/bitcoin.pdf',
                },
              },
            ],
          },
        ],
        // Optional: Configure PDF processing engine
        plugins: [
          {
            id: 'file-parser',
            pdf: {
              engine: '{{ENGINE}}',
            },
          },
        ],
      }),
    });

    const data = await response.json();
    console.log(data);
    ```
  </CodeGroup>
</Template>

<Info>
  PDF URLs work with all processing engines. For Mistral OCR, the URL is passed directly to the service. For other engines, OpenRouter fetches the PDF and processes it internally.
</Info>

## Using Base64 Encoded PDFs

For local PDF files or when you need to send PDF content directly, you can base64 encode the file:

<Template
  data={{
  API_KEY_REF,
  MODEL: 'google/gemma-3-27b-it',
  ENGINE: PDFParserEngine.PDFText,
  DEFAULT_PDF_ENGINE,
}}
>
  <CodeGroup>
    ```python
    import requests
    import json
    import base64
    from pathlib import Path

    def encode_pdf_to_base64(pdf_path):
        with open(pdf_path, "rb") as pdf_file:
            return base64.b64encode(pdf_file.read()).decode('utf-8')

    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY_REF}",
        "Content-Type": "application/json"
    }

    # Read and encode the PDF
    pdf_path = "path/to/your/document.pdf"
    base64_pdf = encode_pdf_to_base64(pdf_path)
    data_url = f"data:application/pdf;base64,{base64_pdf}"

    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "What are the main points in this document?"
                },
                {
                    "type": "file",
                    "file": {
                        "filename": "document.pdf",
                        "file_data": data_url
                    }
                },
            ]
        }
    ]

    # Optional: Configure PDF processing engine
    # PDF parsing will still work even if the plugin is not explicitly set
    plugins = [
        {
            "id": "file-parser",
            "pdf": {
                "engine": "{{ENGINE}}"  # defaults to "{{DEFAULT_PDF_ENGINE}}". See Pricing above
            }
        }
    ]

    payload = {
        "model": "{{MODEL}}",
        "messages": messages,
        "plugins": plugins
    }

    response = requests.post(url, headers=headers, json=payload)
    print(response.json())
    ```

    ```typescript
    async function encodePDFToBase64(pdfPath: string): Promise<string> {
      const pdfBuffer = await fs.promises.readFile(pdfPath);
      const base64PDF = pdfBuffer.toString('base64');
      return `data:application/pdf;base64,${base64PDF}`;
    }

    // Read and encode the PDF
    const pdfPath = 'path/to/your/document.pdf';
    const base64PDF = await encodePDFToBase64(pdfPath);

    const response = await fetch('https://openrouter.ai/api/v1/chat/completions', {
      method: 'POST',
      headers: {
        Authorization: `Bearer ${API_KEY_REF}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        model: '{{MODEL}}',
        messages: [
          {
            role: 'user',
            content: [
              {
                type: 'text',
                text: 'What are the main points in this document?',
              },
              {
                type: 'file',
                file: {
                  filename: 'document.pdf',
                  file_data: base64PDF,
                },
              },
            ],
          },
        ],
        // Optional: Configure PDF processing engine
        // PDF parsing will still work even if the plugin is not explicitly set
        plugins: [
          {
            id: 'file-parser',
            pdf: {
              engine: '{{ENGINE}}', // defaults to "{{DEFAULT_PDF_ENGINE}}". See Pricing above
            },
          },
        ],
      }),
    });

    const data = await response.json();
    console.log(data);
    ```
  </CodeGroup>
</Template>

## Skip Parsing Costs

When you send a PDF to the API, the response may include file annotations in the assistant's message. These annotations contain structured information about the PDF document that was parsed. By sending these annotations back in subsequent requests, you can avoid re-parsing the same PDF document multiple times, which saves both processing time and costs.

Here's how to reuse file annotations:

<Template
  data={{
  API_KEY_REF,
  MODEL: 'google/gemma-3-27b-it'
}}
>
  <CodeGroup>
    ```python
    import requests
    import json
    import base64
    from pathlib import Path

    # First, encode and send the PDF
    def encode_pdf_to_base64(pdf_path):
        with open(pdf_path, "rb") as pdf_file:
            return base64.b64encode(pdf_file.read()).decode('utf-8')

    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY_REF}",
        "Content-Type": "application/json"
    }

    # Read and encode the PDF
    pdf_path = "path/to/your/document.pdf"
    base64_pdf = encode_pdf_to_base64(pdf_path)
    data_url = f"data:application/pdf;base64,{base64_pdf}"

    # Initial request with the PDF
    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "What are the main points in this document?"
                },
                {
                    "type": "file",
                    "file": {
                        "filename": "document.pdf",
                        "file_data": data_url
                    }
                },
            ]
        }
    ]

    payload = {
        "model": "{{MODEL}}",
        "messages": messages
    }

    response = requests.post(url, headers=headers, json=payload)
    response_data = response.json()

    # Store the annotations from the response
    file_annotations = None
    if response_data.get("choices") and len(response_data["choices"]) > 0:
        if "annotations" in response_data["choices"][0]["message"]:
            file_annotations = response_data["choices"][0]["message"]["annotations"]

    # Follow-up request using the annotations (without sending the PDF again)
    if file_annotations:
        follow_up_messages = [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "What are the main points in this document?"
                    },
                    {
                        "type": "file",
                        "file": {
                            "filename": "document.pdf",
                            "file_data": data_url
                        }
                    }
                ]
            },
            {
                "role": "assistant",
                "content": "The document contains information about...",
                "annotations": file_annotations
            },
            {
                "role": "user",
                "content": "Can you elaborate on the second point?"
            }
        ]

        follow_up_payload = {
            "model": "{{MODEL}}",
            "messages": follow_up_messages
        }

        follow_up_response = requests.post(url, headers=headers, json=follow_up_payload)
        print(follow_up_response.json())
    ```

    ```typescript
    import fs from 'fs/promises';

    async function encodePDFToBase64(pdfPath: string): Promise<string> {
      const pdfBuffer = await fs.readFile(pdfPath);
      const base64PDF = pdfBuffer.toString('base64');
      return `data:application/pdf;base64,${base64PDF}`;
    }

    // Initial request with the PDF
    async function processDocument() {
      // Read and encode the PDF
      const pdfPath = 'path/to/your/document.pdf';
      const base64PDF = await encodePDFToBase64(pdfPath);

      const initialResponse = await fetch(
        'https://openrouter.ai/api/v1/chat/completions',
        {
          method: 'POST',
          headers: {
            Authorization: `Bearer ${API_KEY_REF}`,
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            model: '{{MODEL}}',
            messages: [
              {
                role: 'user',
                content: [
                  {
                    type: 'text',
                    text: 'What are the main points in this document?',
                  },
                  {
                    type: 'file',
                    file: {
                      filename: 'document.pdf',
                      file_data: base64PDF,
                    },
                  },
                ],
              },
            ],
          }),
        },
      );

      const initialData = await initialResponse.json();

      // Store the annotations from the response
      let fileAnnotations = null;
      if (initialData.choices && initialData.choices.length > 0) {
        if (initialData.choices[0].message.annotations) {
          fileAnnotations = initialData.choices[0].message.annotations;
        }
      }

      // Follow-up request using the annotations (without sending the PDF again)
      if (fileAnnotations) {
        const followUpResponse = await fetch(
          'https://openrouter.ai/api/v1/chat/completions',
          {
            method: 'POST',
            headers: {
              Authorization: `Bearer ${API_KEY_REF}`,
              'Content-Type': 'application/json',
            },
            body: JSON.stringify({
              model: '{{MODEL}}',
              messages: [
                {
                  role: 'user',
                  content: [
                    {
                      type: 'text',
                      text: 'What are the main points in this document?',
                    },
                    {
                      type: 'file',
                      file: {
                        filename: 'document.pdf',
                        file_data: base64PDF,
                      },
                    },
                  ],
                },
                {
                  role: 'assistant',
                  content: 'The document contains information about...',
                  annotations: fileAnnotations,
                },
                {
                  role: 'user',
                  content: 'Can you elaborate on the second point?',
                },
              ],
            }),
          },
        );

        const followUpData = await followUpResponse.json();
        console.log(followUpData);
      }
    }

    processDocument();
    ```
  </CodeGroup>
</Template>

<Info>
  When you include the file annotations from a previous response in your
  subsequent requests, OpenRouter will use this pre-parsed information instead
  of re-parsing the PDF, which saves processing time and costs. This is
  especially beneficial for large documents or when using the `mistral-ocr`
  engine which incurs additional costs.
</Info>

## Response Format

The API will return a response in the following format:

```json
{
  "id": "gen-1234567890",
  "provider": "DeepInfra",
  "model": "google/gemma-3-27b-it",
  "object": "chat.completion",
  "created": 1234567890,
  "choices": [
    {
      "message": {
        "role": "assistant",
        "content": "The document discusses..."
      }
    }
  ],
  "usage": {
    "prompt_tokens": 1000,
    "completion_tokens": 100,
    "total_tokens": 1100
  }
}
```


# Audio Inputs

> Send audio files to speech-capable models through the OpenRouter API.

OpenRouter supports sending audio files to compatible models via the API. This guide will show you how to work with audio using our API.

**Note**: Audio files must be **base64-encoded** - direct URLs are not supported for audio content.

## Audio Inputs

Requests with audio files to compatible models are available via the `/api/v1/chat/completions` API with the `input_audio` content type. Audio files must be base64-encoded and include the format specification. Note that only models with audio processing capabilities will handle these requests.

You can search for models that support audio by filtering to audio input modality on our [Models page](/models?fmt=cards\&input_modalities=audio).

### Sending Audio Files

Here's how to send an audio file for processing:

<Template
  data={{
  API_KEY_REF,
  MODEL: 'google/gemini-2.5-flash'
}}
>
  <CodeGroup>
    ```typescript title="TypeScript SDK"
    import { OpenRouter } from '@openrouter/sdk';
    import fs from "fs/promises";

    const openRouter = new OpenRouter({
      apiKey: '{{API_KEY_REF}}',
    });

    async function encodeAudioToBase64(audioPath: string): Promise<string> {
      const audioBuffer = await fs.readFile(audioPath);
      return audioBuffer.toString("base64");
    }

    // Read and encode the audio file
    const audioPath = "path/to/your/audio.wav";
    const base64Audio = await encodeAudioToBase64(audioPath);

    const result = await openRouter.chat.send({
      model: "{{MODEL}}",
      messages: [
        {
          role: "user",
          content: [
            {
              type: "text",
              text: "Please transcribe this audio file.",
            },
            {
              type: "input_audio",
              inputAudio: {
                data: base64Audio,
                format: "wav",
              },
            },
          ],
        },
      ],
      stream: false,
    });

    console.log(result);
    ```

    ```python
    import requests
    import json
    import base64

    def encode_audio_to_base64(audio_path):
        with open(audio_path, "rb") as audio_file:
            return base64.b64encode(audio_file.read()).decode('utf-8')

    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY_REF}",
        "Content-Type": "application/json"
    }

    # Read and encode the audio file
    audio_path = "path/to/your/audio.wav"
    base64_audio = encode_audio_to_base64(audio_path)

    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Please transcribe this audio file."
                },
                {
                    "type": "input_audio",
                    "input_audio": {
                        "data": base64_audio,
                        "format": "wav"
                    }
                }
            ]
        }
    ]

    payload = {
        "model": "{{MODEL}}",
        "messages": messages
    }

    response = requests.post(url, headers=headers, json=payload)
    print(response.json())
    ```

    ```typescript title="TypeScript (fetch)"
    import fs from "fs/promises";

    async function encodeAudioToBase64(audioPath: string): Promise<string> {
      const audioBuffer = await fs.readFile(audioPath);
      return audioBuffer.toString("base64");
    }

    // Read and encode the audio file
    const audioPath = "path/to/your/audio.wav";
    const base64Audio = await encodeAudioToBase64(audioPath);

    const response = await fetch("https://openrouter.ai/api/v1/chat/completions", {
      method: "POST",
      headers: {
        Authorization: `Bearer ${API_KEY_REF}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        model: "{{MODEL}}",
        messages: [
          {
            role: "user",
            content: [
              {
                type: "text",
                text: "Please transcribe this audio file.",
              },
              {
                type: "input_audio",
                input_audio: {
                  data: base64Audio,
                  format: "wav",
                },
              },
            ],
          },
        ],
      }),
    });

    const data = await response.json();
    console.log(data);
    ```
  </CodeGroup>
</Template>

Supported audio formats are:

* `wav`
* `mp3`


# Video Inputs

> Send video files to video-capable models through the OpenRouter API.

OpenRouter supports sending video files to compatible models via the API. This guide will show you how to work with video using our API.

OpenRouter supports both **direct URLs** and **base64-encoded data URLs** for videos:

* **URLs**: Efficient for publicly accessible videos as they don't require local encoding
* **Base64 Data URLs**: Required for local files or private videos that aren't publicly accessible

<Info>
  **Important:** Video URL support varies by provider. OpenRouter only sends video URLs to providers that explicitly support them. For example, Google Gemini on AI Studio only supports YouTube links (not Vertex AI).
</Info>

## Video Inputs

Requests with video files to compatible models are available via the `/api/v1/chat/completions` API with the `input_video` content type. The `video_url` can either be a URL or a base64-encoded data URL. Note that only models with video processing capabilities will handle these requests.

You can search for models that support video by filtering to video input modality on our [Models page](/models?fmt=cards\&input_modalities=video).

### Using Video URLs

Here's how to send a video using a URL. Note that for Google Gemini on AI Studio, only YouTube links are supported:

<Template
  data={{
  API_KEY_REF,
  MODEL: 'google/gemini-2.5-flash'
}}
>
  <CodeGroup>
    ```typescript title="TypeScript SDK"
    import { OpenRouter } from '@openrouter/sdk';

    const openRouter = new OpenRouter({
      apiKey: '{{API_KEY_REF}}',
    });

    const result = await openRouter.chat.send({
      model: "{{MODEL}}",
      messages: [
        {
          role: "user",
          content: [
            {
              type: "text",
              text: "Please describe what's happening in this video.",
            },
            {
              type: "input_video",
              videoUrl: {
                url: "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
              },
            },
          ],
        },
      ],
      stream: false,
    });

    console.log(result);
    ```

    ```python
    import requests
    import json

    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY_REF}",
        "Content-Type": "application/json"
    }

    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Please describe what's happening in this video."
                },
                {
                    "type": "input_video",
                    "video_url": {
                        "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
                    }
                }
            ]
        }
    ]

    payload = {
        "model": "{{MODEL}}",
        "messages": messages
    }

    response = requests.post(url, headers=headers, json=payload)
    print(response.json())
    ```

    ```typescript title="TypeScript (fetch)"
    const response = await fetch("https://openrouter.ai/api/v1/chat/completions", {
      method: "POST",
      headers: {
        Authorization: `Bearer ${API_KEY_REF}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        model: "{{MODEL}}",
        messages: [
          {
            role: "user",
            content: [
              {
                type: "text",
                text: "Please describe what's happening in this video.",
              },
              {
                type: "input_video",
                video_url: {
                  url: "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                },
              },
            ],
          },
        ],
      }),
    });

    const data = await response.json();
    console.log(data);
    ```
  </CodeGroup>
</Template>

### Using Base64 Encoded Videos

For locally stored videos, you can send them using base64 encoding as data URLs:

<Template
  data={{
  API_KEY_REF,
  MODEL: 'google/gemini-2.5-flash'
}}
>
  <CodeGroup>
    ```typescript title="TypeScript SDK"
    import { OpenRouter } from '@openrouter/sdk';
    import * as fs from 'fs';

    const openRouter = new OpenRouter({
      apiKey: '{{API_KEY_REF}}',
    });

    async function encodeVideoToBase64(videoPath: string): Promise<string> {
      const videoBuffer = await fs.promises.readFile(videoPath);
      const base64Video = videoBuffer.toString('base64');
      return `data:video/mp4;base64,${base64Video}`;
    }

    // Read and encode the video
    const videoPath = 'path/to/your/video.mp4';
    const base64Video = await encodeVideoToBase64(videoPath);

    const result = await openRouter.chat.send({
      model: '{{MODEL}}',
      messages: [
        {
          role: 'user',
          content: [
            {
              type: 'text',
              text: "What's in this video?",
            },
            {
              type: 'input_video',
              videoUrl: {
                url: base64Video,
              },
            },
          ],
        },
      ],
      stream: false,
    });

    console.log(result);
    ```

    ```python
    import requests
    import json
    import base64
    from pathlib import Path

    def encode_video_to_base64(video_path):
        with open(video_path, "rb") as video_file:
            return base64.b64encode(video_file.read()).decode('utf-8')

    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY_REF}",
        "Content-Type": "application/json"
    }

    # Read and encode the video
    video_path = "path/to/your/video.mp4"
    base64_video = encode_video_to_base64(video_path)
    data_url = f"data:video/mp4;base64,{base64_video}"

    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "What's in this video?"
                },
                {
                    "type": "input_video",
                    "video_url": {
                        "url": data_url
                    }
                }
            ]
        }
    ]

    payload = {
        "model": "{{MODEL}}",
        "messages": messages
    }

    response = requests.post(url, headers=headers, json=payload)
    print(response.json())
    ```

    ```typescript title="TypeScript (fetch)"
    import * as fs from 'fs';

    async function encodeVideoToBase64(videoPath: string): Promise<string> {
      const videoBuffer = await fs.promises.readFile(videoPath);
      const base64Video = videoBuffer.toString('base64');
      return `data:video/mp4;base64,${base64Video}`;
    }

    // Read and encode the video
    const videoPath = 'path/to/your/video.mp4';
    const base64Video = await encodeVideoToBase64(videoPath);

    const response = await fetch('https://openrouter.ai/api/v1/chat/completions', {
      method: 'POST',
      headers: {
        Authorization: `Bearer ${API_KEY_REF}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        model: '{{MODEL}}',
        messages: [
          {
            role: 'user',
            content: [
              {
                type: 'text',
                text: "What's in this video?",
              },
              {
                type: 'input_video',
                video_url: {
                  url: base64Video,
                },
              },
            ],
          },
        ],
      }),
    });

    const data = await response.json();
    console.log(data);
    ```
  </CodeGroup>
</Template>

## Supported Video Formats

OpenRouter supports the following video formats:

* `video/mp4`
* `video/mpeg`
* `video/mov`
* `video/webm`

## Common Use Cases

Video inputs enable a wide range of applications:

* **Video Summarization**: Generate text summaries of video content
* **Object and Activity Recognition**: Identify objects, people, and actions in videos
* **Scene Understanding**: Describe settings, environments, and contexts
* **Sports Analysis**: Analyze gameplay, movements, and tactics
* **Surveillance**: Monitor and analyze security footage
* **Educational Content**: Analyze instructional videos and provide insights

## Best Practices

### File Size Considerations

Video files can be large, which affects both upload time and processing costs:

* **Compress videos** when possible to reduce file size without significant quality loss
* **Trim videos** to include only relevant segments
* **Consider resolution**: Lower resolutions (e.g., 720p vs 4K) reduce file size while maintaining usability for most analysis tasks
* **Frame rate**: Lower frame rates can reduce file size for videos where high temporal resolution isn't critical

### Optimal Video Length

Different models may have different limits on video duration:

* Check model-specific documentation for maximum video length
* For long videos, consider splitting into shorter segments
* Focus on key moments rather than sending entire long-form content

### Quality vs. Size Trade-offs

Balance video quality with practical considerations:

* **High quality** (1080p+, high bitrate): Best for detailed visual analysis, object detection, text recognition
* **Medium quality** (720p, moderate bitrate): Suitable for most general analysis tasks
* **Lower quality** (480p, lower bitrate): Acceptable for basic scene understanding and action recognition

## Provider-Specific Video URL Support

Video URL support varies significantly by provider:

* **Google Gemini (AI Studio)**: Only supports YouTube links (e.g., `https://www.youtube.com/watch?v=...`)
* **Google Gemini (Vertex AI)**: Does not support video URLs - use base64-encoded data URLs instead
* **Other providers**: Check model-specific documentation for video URL support

## Troubleshooting

**Video not processing?**

* Verify the model supports video input (check `input_modalities` includes `"video"`)
* If using a video URL, confirm the provider supports video URLs (see Provider-Specific Video URL Support above)
* For Gemini on AI Studio, ensure you're using a YouTube link, not a direct video file URL
* If the video URL isn't working, try using a base64-encoded data URL instead
* Check that the video format is supported
* Verify the video file isn't corrupted

**Large file errors?**

* Compress the video to reduce file size
* Reduce video resolution or frame rate
* Trim the video to a shorter duration
* Check model-specific file size limits
* Consider using a video URL (if supported by the provider) instead of base64 encoding for large files

**Poor analysis results?**

* Ensure video quality is sufficient for the task
* Provide clear, specific prompts about what to analyze
* Consider if the video duration is appropriate for the model
* Check if the video content is clearly visible and well-lit


# Message Transforms

> Transform and optimize messages before sending them to AI models. Learn about middle-out compression and context window optimization with OpenRouter.

To help with prompts that exceed the maximum context size of a model, OpenRouter supports a custom parameter called `transforms`:

```typescript
{
  transforms: ["middle-out"], // Compress prompts that are > context size.
  messages: [...],
  model // Works with any model
}
```

This can be useful for situations where perfect recall is not required. The transform works by removing or truncating messages from the middle of the prompt, until the prompt fits within the model's context window.

In some cases, the issue is not the token context length, but the actual number of messages. The transform addresses this as well: For instance, Anthropic's Claude models enforce a maximum of {anthropicMaxMessagesCount} messages. When this limit is exceeded with middle-out enabled, the transform will keep half of the messages from the start and half from the end of the conversation.

When middle-out compression is enabled, OpenRouter will first try to find models whose context length is at least half of your total required tokens (input + completion). For example, if your prompt requires 10,000 tokens total, models with at least 5,000 context length will be considered. If no models meet this criteria, OpenRouter will fall back to using the model with the highest available context length.

The compression will then attempt to fit your content within the chosen model's context window by removing or truncating content from the middle of the prompt. If middle-out compression is disabled and your total tokens exceed the model's context length, the request will fail with an error message suggesting you either reduce the length or enable middle-out compression.

<Note>
  [All OpenRouter endpoints](/models) with 8k (8,192 tokens) or less context
  length will default to using `middle-out`. To disable this, set `transforms:   []` in the request body.
</Note>

The middle of the prompt is compressed because [LLMs pay less attention](https://arxiv.org/abs/2307.03172) to the middle of sequences.


# Uptime Optimization

> Learn how OpenRouter maximizes AI model uptime through real-time monitoring, intelligent routing, and automatic fallbacks across multiple providers.

OpenRouter continuously monitors the health and availability of AI providers to ensure maximum uptime for your applications. We track response times, error rates, and availability across all providers in real-time, and route based on this feedback.

## How It Works

OpenRouter tracks response times, error rates, and availability across all providers in real-time. This data helps us make intelligent routing decisions and provides transparency about service reliability.

## Uptime Example: Claude 4 Sonnet

<UptimeChart permaslug="anthropic/claude-4-sonnet-20250522" />

## Uptime Example: Llama 3.3 70B Instruct

<UptimeChart permaslug="meta-llama/llama-3.3-70b-instruct" />

## Customizing Provider Selection

While our smart routing helps maintain high availability, you can also customize provider selection using request parameters. This gives you control over which providers handle your requests while still benefiting from automatic fallback when needed.

Learn more about customizing provider selection in our [Provider Routing documentation](/docs/features/provider-routing).


# Web Search

> Enable real-time web search capabilities in your AI model responses. Add factual, up-to-date information to any model's output with OpenRouter's web search feature.

You can incorporate relevant web search results for *any* model on OpenRouter by activating and customizing the `web` plugin, or by appending `:online` to the model slug:

```json
{
  "model": "openai/gpt-4o:online"
}
```

This is a shortcut for using the `web` plugin, and is exactly equivalent to:

```json
{
  "model": "openrouter/auto",
  "plugins": [{ "id": "web" }]
}
```

The web search plugin is powered by native search for Anthropic and OpenAI natively and by [Exa](https://exa.ai) for other models. For Exa, it uses their ["auto"](https://docs.exa.ai/reference/how-exa-search-works#combining-neural-and-keyword-the-best-of-both-worlds-through-exa-auto-search) method (a combination of keyword search and embeddings-based web search) to find the most relevant results and augment/ground your prompt.

## Parsing web search results

Web search results for all models (including native-only models like Perplexity and OpenAI Online) are available in the API and standardized by OpenRouterto follow the same annotation schema in the [OpenAI Chat Completion Message type](https://platform.openai.com/docs/api-reference/chat/object):

```json
{
  "message": {
    "role": "assistant",
    "content": "Here's the latest news I found: ...",
    "annotations": [
      {
        "type": "url_citation",
        "url_citation": {
          "url": "https://www.example.com/web-search-result",
          "title": "Title of the web search result",
          "content": "Content of the web search result", // Added by OpenRouter if available
          "start_index": 100, // The index of the first character of the URL citation in the message.
          "end_index": 200 // The index of the last character of the URL citation in the message.
        }
      }
    ]
  }
}
```

## Customizing the Web Plugin

The maximum results allowed by the web plugin and the prompt used to attach them to your message stream can be customized:

```json
{
  "model": "openai/gpt-4o:online",
  "plugins": [
    {
      "id": "web",
      "engine": "exa", // Optional: "native", "exa", or undefined
      "max_results": 1, // Defaults to 5
      "search_prompt": "Some relevant web results:" // See default below
    }
  ]
}
```

By default, the web plugin uses the following search prompt, using the current date:

```
A web search was conducted on `date`. Incorporate the following web search results into your response.

IMPORTANT: Cite them using markdown links named using the domain of the source.
Example: [nytimes.com](https://nytimes.com/some-page).
```

## Engine Selection

The web search plugin supports the following options for the `engine` parameter:

* **`native`**: Always uses the model provider's built-in web search capabilities
* **`exa`**: Uses Exa's search API for web results
* **`undefined` (not specified)**: Uses native search if available for the provider, otherwise falls back to Exa

### Default Behavior

When the `engine` parameter is not specified:

* **Native search is used by default** for OpenAI and Anthropic models that support it
* **Exa search is used** for all other models or when native search is not supported

When you explicitly specify `"engine": "native"`, it will always attempt to use the provider's native search, even if the model doesn't support it (which may result in an error).

### Forcing Engine Selection

You can explicitly specify which engine to use:

```json
{
  "model": "openai/gpt-4o",
  "plugins": [
    {
      "id": "web",
      "engine": "native"
    }
  ]
}
```

Or force Exa search even for models that support native search:

```json
{
  "model": "openai/gpt-4o",
  "plugins": [
    {
      "id": "web",
      "engine": "exa",
      "max_results": 3
    }
  ]
}
```

### Engine-Specific Pricing

* **Native search**: Pricing is passed through directly from the provider (see provider-specific pricing sections below)
* **Exa search**: Uses OpenRouter credits at \$4 per 1000 results (default 5 results = \$0.02 per request)

## Pricing

### Exa Search Pricing

When using Exa search (either explicitly via `"engine": "exa"` or as fallback), the web plugin uses your OpenRouter credits and charges *\$4 per 1000 results*. By default, `max_results` set to 5, this comes out to a maximum of \$0.02 per request, in addition to the LLM usage for the search result prompt tokens.

### Native Search Pricing (Provider Passthrough)

Some models have built-in web search. These models charge a fee based on the search context size, which determines how much search data is retrieved and processed for a query.

### Search Context Size Thresholds

Search context can be 'low', 'medium', or 'high' and determines how much search context is retrieved for a query:

* **Low**: Minimal search context, suitable for basic queries
* **Medium**: Moderate search context, good for general queries
* **High**: Extensive search context, ideal for detailed research

### Specifying Search Context Size

You can specify the search context size in your API request using the `web_search_options` parameter:

```json
{
  "model": "openai/gpt-4.1",
  "messages": [
    {
      "role": "user",
      "content": "What are the latest developments in quantum computing?"
    }
  ],
  "web_search_options": {
    "search_context_size": "high"
  }
}
```

### OpenAI Model Pricing

For GPT-4.1, GPT-4o, and GPT-4o search preview Models:

| Search Context Size | Price per 1000 Requests |
| ------------------- | ----------------------- |
| Low                 | \$30.00                 |
| Medium              | \$35.00                 |
| High                | \$50.00                 |

For GPT-4.1-Mini, GPT-4o-Mini, and GPT-4o-Mini-Search-Preview Models:

| Search Context Size | Price per 1000 Requests |
| ------------------- | ----------------------- |
| Low                 | \$25.00                 |
| Medium              | \$27.50                 |
| High                | \$30.00                 |

### Perplexity Model Pricing

For Sonar and SonarReasoning:

| Search Context Size | Price per 1000 Requests |
| ------------------- | ----------------------- |
| Low                 | \$5.00                  |
| Medium              | \$8.00                  |
| High                | \$12.00                 |

For SonarPro and SonarReasoningPro:

| Search Context Size | Price per 1000 Requests |
| ------------------- | ----------------------- |
| Low                 | \$6.00                  |
| Medium              | \$10.00                 |
| High                | \$14.00                 |

<Note title="Engine Parameter">
  The pricing above applies when using `"engine": "native"` or when native search is used by default for supported models. When using `"engine": "exa"`, the Exa search pricing (\$4 per 1000 results) applies instead.
</Note>

<Note title="Pricing Documentation">
  For more detailed information about pricing models, refer to the official documentation:

  * [OpenAI Pricing](https://platform.openai.com/docs/pricing#web-search)
  * [Anthropic Pricing](https://docs.claude.com/en/docs/agents-and-tools/tool-use/web-search-tool#usage-and-pricing)
  * [Perplexity Pricing](https://docs.perplexity.ai/guides/pricing)
</Note>


# Zero Completion Insurance

> Learn how OpenRouter protects users from being charged for failed or empty AI responses with zero completion insurance.

OpenRouter provides zero completion insurance to protect users from being charged for failed or empty responses. When a response contains no output tokens and either has a blank finish reason or an error, you will not be charged for the request, even if the underlying provider charges for prompt processing.

<Note>
  Zero completion insurance is automatically enabled for all accounts and requires no configuration.
</Note>

## How It Works

Zero completion insurance automatically applies to all requests across all models and providers. When a response meets either of these conditions, no credits will be deducted from your account:

* The response has zero completion tokens AND a blank/null finish reason
* The response has an error finish reason

## Viewing Protected Requests

On your activity page, requests that were protected by zero completion insurance will show zero credits deducted. This applies even in cases where OpenRouter may have been charged by the provider for prompt processing.


# Provisioning API Keys

> Manage OpenRouter API keys programmatically through dedicated management endpoints. Create, read, update, and delete API keys for automated key distribution and control.

OpenRouter provides endpoints to programmatically manage your API keys, enabling key creation and management for applications that need to distribute or rotate keys automatically.

## Creating a Provisioning API Key

To use the key management API, you first need to create a Provisioning API key:

1. Go to the [Provisioning API Keys page](https://openrouter.ai/settings/provisioning-keys)
2. Click "Create New Key"
3. Complete the key creation process

Provisioning keys cannot be used to make API calls to OpenRouter's completion endpoints - they are exclusively for key management operations.

## Use Cases

Common scenarios for programmatic key management include:

* **SaaS Applications**: Automatically create unique API keys for each customer instance
* **Key Rotation**: Regularly rotate API keys for security compliance
* **Usage Monitoring**: Track key usage and automatically disable keys that exceed limits (with optional daily/weekly/monthly limit resets)

## Example Usage

All key management endpoints are under `/api/v1/keys` and require a Provisioning API key in the Authorization header.

<CodeGroup>
  ```typescript title="TypeScript SDK"
  import { OpenRouter } from '@openrouter/sdk';

  const openRouter = new OpenRouter({
    apiKey: 'your-provisioning-key', // Use your Provisioning API key
  });

  // List the most recent 100 API keys
  const keys = await openRouter.apiKeys.list();

  // You can paginate using the offset parameter
  const keysPage2 = await openRouter.apiKeys.list({ offset: 100 });

  // Create a new API key
  const newKey = await openRouter.apiKeys.create({
    name: 'Customer Instance Key',
    limit: 1000, // Optional credit limit
  });

  // Get a specific key
  const keyHash = '<YOUR_KEY_HASH>';
  const key = await openRouter.apiKeys.get(keyHash);

  // Update a key
  const updatedKey = await openRouter.apiKeys.update(keyHash, {
    name: 'Updated Key Name',
    disabled: true, // Optional: Disable the key
    includeByokInLimit: false, // Optional: control BYOK usage in limit
    limitReset: 'daily', // Optional: reset limit every day at midnight UTC
  });

  // Delete a key
  await openRouter.apiKeys.delete(keyHash);
  ```

  ```python title="Python"
  import requests

  PROVISIONING_API_KEY = "your-provisioning-key"
  BASE_URL = "https://openrouter.ai/api/v1/keys"

  # List the most recent 100 API keys
  response = requests.get(
      BASE_URL,
      headers={
          "Authorization": f"Bearer {PROVISIONING_API_KEY}",
          "Content-Type": "application/json"
      }
  )

  # You can paginate using the offset parameter
  response = requests.get(
      f"{BASE_URL}?offset=100",
      headers={
          "Authorization": f"Bearer {PROVISIONING_API_KEY}",
          "Content-Type": "application/json"
      }
  )

  # Create a new API key
  response = requests.post(
      f"{BASE_URL}/",
      headers={
          "Authorization": f"Bearer {PROVISIONING_API_KEY}",
          "Content-Type": "application/json"
      },
      json={
          "name": "Customer Instance Key",
          "limit": 1000  # Optional credit limit
      }
  )

  # Get a specific key
  key_hash = "<YOUR_KEY_HASH>"
  response = requests.get(
      f"{BASE_URL}/{key_hash}",
      headers={
          "Authorization": f"Bearer {PROVISIONING_API_KEY}",
          "Content-Type": "application/json"
      }
  )

  # Update a key
  response = requests.patch(
      f"{BASE_URL}/{key_hash}",
      headers={
          "Authorization": f"Bearer {PROVISIONING_API_KEY}",
          "Content-Type": "application/json"
      },
      json={
          "name": "Updated Key Name",
          "disabled": True,  # Optional: Disable the key
          "include_byok_in_limit": False,  # Optional: control BYOK usage in limit
          "limit_reset": "daily"  # Optional: reset limit every day at midnight UTC
      }
  )

  # Delete a key
  response = requests.delete(
      f"{BASE_URL}/{key_hash}",
      headers={
          "Authorization": f"Bearer {PROVISIONING_API_KEY}",
          "Content-Type": "application/json"
      }
  )
  ```

  ```typescript title="TypeScript (fetch)"
  const PROVISIONING_API_KEY = 'your-provisioning-key';
  const BASE_URL = 'https://openrouter.ai/api/v1/keys';

  // List the most recent 100 API keys
  const listKeys = await fetch(BASE_URL, {
    headers: {
      Authorization: `Bearer ${PROVISIONING_API_KEY}`,
      'Content-Type': 'application/json',
    },
  });

  // You can paginate using the `offset` query parameter
  const listKeys = await fetch(`${BASE_URL}?offset=100`, {
    headers: {
      Authorization: `Bearer ${PROVISIONING_API_KEY}`,
      'Content-Type': 'application/json',
    },
  });

  // Create a new API key
  const createKey = await fetch(`${BASE_URL}`, {
    method: 'POST',
    headers: {
      Authorization: `Bearer ${PROVISIONING_API_KEY}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      name: 'Customer Instance Key',
      limit: 1000, // Optional credit limit
    }),
  });

  // Get a specific key
  const keyHash = '<YOUR_KEY_HASH>';
  const getKey = await fetch(`${BASE_URL}/${keyHash}`, {
    headers: {
      Authorization: `Bearer ${PROVISIONING_API_KEY}`,
      'Content-Type': 'application/json',
    },
  });

  // Update a key
  const updateKey = await fetch(`${BASE_URL}/${keyHash}`, {
    method: 'PATCH',
    headers: {
      Authorization: `Bearer ${PROVISIONING_API_KEY}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      name: 'Updated Key Name',
      disabled: true, // Optional: Disable the key
      include_byok_in_limit: false, // Optional: control BYOK usage in limit
      limit_reset: 'daily', // Optional: reset limit every day at midnight UTC
    }),
  });

  // Delete a key
  const deleteKey = await fetch(`${BASE_URL}/${keyHash}`, {
    method: 'DELETE',
    headers: {
      Authorization: `Bearer ${PROVISIONING_API_KEY}`,
      'Content-Type': 'application/json',
    },
  });
  ```
</CodeGroup>

## Response Format

API responses return JSON objects containing key information:

```json
{
  "data": [
    {
      "created_at": "2025-02-19T20:52:27.363244+00:00",
      "updated_at": "2025-02-19T21:24:11.708154+00:00",
      "hash": "<YOUR_KEY_HASH>",
      "label": "sk-or-v1-abc...123",
      "name": "Customer Key",
      "disabled": false,
      "limit": 10,
      "limit_remaining": 10,
      "limit_reset": null,
      "include_byok_in_limit": false,
      "usage": 0,
      "usage_daily": 0,
      "usage_weekly": 0,
      "usage_monthly": 0,
      "byok_usage": 0,
      "byok_usage_daily": 0,
      "byok_usage_weekly": 0,
      "byok_usage_monthly": 0
    }
  ]
}
```

When creating a new key, the response will include the key string itself. Read more in the [API reference](/docs/api-reference/api-keys/create-api-key).


# App Attribution

> Learn how to attribute your API usage to your app and appear in OpenRouter's app rankings and model analytics.

App attribution allows developers to associate their API usage with their application, enabling visibility in OpenRouter's public rankings and detailed analytics. By including simple headers in your requests, your app can appear in our leaderboards and gain insights into your model usage patterns.

## Benefits of App Attribution

When you properly attribute your app usage, you gain access to:

* **Public App Rankings**: Your app appears in OpenRouter's [public rankings](https://openrouter.ai/rankings) with daily, weekly, and monthly leaderboards
* **Model Apps Tabs**: Your app is featured on individual model pages showing which apps use each model most
* **Detailed Analytics**: Access comprehensive analytics showing your app's model usage over time, token consumption, and usage patterns
* **Professional Visibility**: Showcase your app to the OpenRouter developer community

## Attribution Headers

OpenRouter tracks app attribution through two optional HTTP headers:

### HTTP-Referer

The `HTTP-Referer` header identifies your app's URL and is used as the primary identifier for rankings.

### X-Title

The `X-Title` header sets or modifies your app's display name in rankings and analytics.

<Tip>
  Both headers are optional, but including them enables all attribution features. Apps using localhost URLs must include a title to be tracked.
</Tip>

## Implementation Examples

<CodeGroup>
  ```typescript title="TypeScript SDK"
  import { OpenRouter } from '@openrouter/sdk';

  const openRouter = new OpenRouter({
    apiKey: '<OPENROUTER_API_KEY>',
    defaultHeaders: {
      'HTTP-Referer': 'https://myapp.com', // Your app's URL
      'X-Title': 'My AI Assistant', // Your app's display name
    },
  });

  const completion = await openRouter.chat.send({
    model: 'openai/gpt-4o',
    messages: [
      {
        role: 'user',
        content: 'Hello, world!',
      },
    ],
    stream: false,
  });

  console.log(completion.choices[0].message);
  ```

  ```python title="Python (OpenAI SDK)"
  from openai import OpenAI

  client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="<OPENROUTER_API_KEY>",
  )

  completion = client.chat.completions.create(
    extra_headers={
      "HTTP-Referer": "https://myapp.com", # Your app's URL
      "X-Title": "My AI Assistant", # Your app's display name
    },
    model="openai/gpt-4o",
    messages=[
      {
        "role": "user",
        "content": "Hello, world!"
      }
    ]
  )
  ```

  ```typescript title="TypeScript (OpenAI SDK)"
  import OpenAI from 'openai';

  const openai = new OpenAI({
    baseURL: 'https://openrouter.ai/api/v1',
    apiKey: '<OPENROUTER_API_KEY>',
    defaultHeaders: {
      'HTTP-Referer': 'https://myapp.com', // Your app's URL
      'X-Title': 'My AI Assistant', // Your app's display name
    },
  });

  async function main() {
    const completion = await openai.chat.completions.create({
      model: 'openai/gpt-4o',
      messages: [
        {
          role: 'user',
          content: 'Hello, world!',
        },
      ],
    });

    console.log(completion.choices[0].message);
  }

  main();
  ```

  ```python title="Python (Direct API)"
  import requests
  import json

  response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
      "Authorization": "Bearer <OPENROUTER_API_KEY>",
      "HTTP-Referer": "https://myapp.com", # Your app's URL
      "X-Title": "My AI Assistant", # Your app's display name
      "Content-Type": "application/json",
    },
    data=json.dumps({
      "model": "openai/gpt-4o",
      "messages": [
        {
          "role": "user",
          "content": "Hello, world!"
        }
      ]
    })
  )
  ```

  ```typescript title="TypeScript (fetch)"
  fetch('https://openrouter.ai/api/v1/chat/completions', {
    method: 'POST',
    headers: {
      Authorization: 'Bearer <OPENROUTER_API_KEY>',
      'HTTP-Referer': 'https://myapp.com', // Your app's URL
      'X-Title': 'My AI Assistant', // Your app's display name
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      model: 'openai/gpt-4o',
      messages: [
        {
          role: 'user',
          content: 'Hello, world!',
        },
      ],
    }),
  });
  ```

  ```shell title="cURL"
  curl https://openrouter.ai/api/v1/chat/completions \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $OPENROUTER_API_KEY" \
    -H "HTTP-Referer: https://myapp.com" \
    -H "X-Title: My AI Assistant" \
    -d '{
    "model": "openai/gpt-4o",
    "messages": [
      {
        "role": "user",
        "content": "Hello, world!"
      }
    ]
  }'
  ```
</CodeGroup>

## Where Your App Appears

### App Rankings

Your attributed app will appear in OpenRouter's main rankings page at [openrouter.ai/rankings](https://openrouter.ai/rankings). The rankings show:

* **Top Apps**: Largest public apps by token usage
* **Time Periods**: Daily, weekly, and monthly views
* **Usage Metrics**: Total token consumption across all models

### Model Apps Tabs

On individual model pages (e.g., [GPT-4o](https://openrouter.ai/models/openai/gpt-4o)), your app will be featured in the "Apps" tab showing:

* **Top Apps**: Apps using that specific model most
* **Weekly Rankings**: Updated weekly based on usage
* **Usage Context**: How your app compares to others using the same model

### Individual App Analytics

Once your app is tracked, you can access detailed analytics at `openrouter.ai/apps?url=<your-app-url>` including:

* **Model Usage Over Time**: Charts showing which models your app uses
* **Token Consumption**: Detailed breakdown of prompt and completion tokens
* **Usage Patterns**: Historical data to understand your app's AI usage trends

## Best Practices

### URL Requirements

* Use your app's primary domain (e.g., `https://myapp.com`)
* Avoid using subdomains unless they represent distinct apps
* For localhost development, always include a title header

### Title Guidelines

* Keep titles concise and descriptive
* Use your app's actual name as users know it
* Avoid generic names like "AI App" or "Chatbot"

### Privacy Considerations

* Only public apps, meaning those that send headers, are included in rankings
* Attribution headers don't expose sensitive information about your requests

## Related Documentation

* [Quickstart Guide](/docs/quickstart) - Basic setup with attribution headers
* [API Reference](/docs/api-reference/overview) - Complete header documentation
* [Usage Accounting](/docs/use-cases/usage-accounting) - Understanding your API usage


# API Reference

> Comprehensive guide to OpenRouter's API. Learn about request/response schemas, authentication, parameters, and integration with multiple AI model providers.

OpenRouter's request and response schemas are very similar to the OpenAI Chat API, with a few small differences. At a high level, **OpenRouter normalizes the schema across models and providers** so you only need to learn one.

## Requests

### Completions Request Format

Here is the request schema as a TypeScript type. This will be the body of your `POST` request to the `/api/v1/chat/completions` endpoint (see the [quick start](/docs/quick-start) above for an example).

For a complete list of parameters, see the [Parameters](/docs/api-reference/parameters).

<CodeGroup>
  ```typescript title="Request Schema"
  // Definitions of subtypes are below
  type Request = {
    // Either "messages" or "prompt" is required
    messages?: Message[];
    prompt?: string;

    // If "model" is unspecified, uses the user's default
    model?: string; // See "Supported Models" section

    // Allows to force the model to produce specific output format.
    // See models page and note on this docs page for which models support it.
    response_format?: { type: 'json_object' };

    stop?: string | string[];
    stream?: boolean; // Enable streaming

    // See LLM Parameters (openrouter.ai/docs/api-reference/parameters)
    max_tokens?: number; // Range: [1, context_length)
    temperature?: number; // Range: [0, 2]

    // Tool calling
    // Will be passed down as-is for providers implementing OpenAI's interface.
    // For providers with custom interfaces, we transform and map the properties.
    // Otherwise, we transform the tools into a YAML template. The model responds with an assistant message.
    // See models supporting tool calling: openrouter.ai/models?supported_parameters=tools
    tools?: Tool[];
    tool_choice?: ToolChoice;

    // Advanced optional parameters
    seed?: number; // Integer only
    top_p?: number; // Range: (0, 1]
    top_k?: number; // Range: [1, Infinity) Not available for OpenAI models
    frequency_penalty?: number; // Range: [-2, 2]
    presence_penalty?: number; // Range: [-2, 2]
    repetition_penalty?: number; // Range: (0, 2]
    logit_bias?: { [key: number]: number };
    top_logprobs: number; // Integer only
    min_p?: number; // Range: [0, 1]
    top_a?: number; // Range: [0, 1]

    // Reduce latency by providing the model with a predicted output
    // https://platform.openai.com/docs/guides/latency-optimization#use-predicted-outputs
    prediction?: { type: 'content'; content: string };

    // OpenRouter-only parameters
    // See "Prompt Transforms" section: openrouter.ai/docs/transforms
    transforms?: string[];
    // See "Model Routing" section: openrouter.ai/docs/model-routing
    models?: string[];
    route?: 'fallback';
    // See "Provider Routing" section: openrouter.ai/docs/provider-routing
    provider?: ProviderPreferences;
    user?: string; // A stable identifier for your end-users. Used to help detect and prevent abuse.
  };

  // Subtypes:

  type TextContent = {
    type: 'text';
    text: string;
  };

  type ImageContentPart = {
    type: 'image_url';
    image_url: {
      url: string; // URL or base64 encoded image data
      detail?: string; // Optional, defaults to "auto"
    };
  };

  type ContentPart = TextContent | ImageContentPart;

  type Message =
    | {
        role: 'user' | 'assistant' | 'system';
        // ContentParts are only for the "user" role:
        content: string | ContentPart[];
        // If "name" is included, it will be prepended like this
        // for non-OpenAI models: `{name}: {content}`
        name?: string;
      }
    | {
        role: 'tool';
        content: string;
        tool_call_id: string;
        name?: string;
      };

  type FunctionDescription = {
    description?: string;
    name: string;
    parameters: object; // JSON Schema object
  };

  type Tool = {
    type: 'function';
    function: FunctionDescription;
  };

  type ToolChoice =
    | 'none'
    | 'auto'
    | {
        type: 'function';
        function: {
          name: string;
        };
      };
  ```
</CodeGroup>

The `response_format` parameter ensures you receive a structured response from the LLM. The parameter is only supported by OpenAI models, Nitro models, and some others - check the providers on the model page on openrouter.ai/models to see if it's supported, and set `require_parameters` to true in your Provider Preferences. See [Provider Routing](/docs/features/provider-routing)

### Headers

OpenRouter allows you to specify some optional headers to identify your app and make it discoverable to users on our site.

* `HTTP-Referer`: Identifies your app on openrouter.ai
* `X-Title`: Sets/modifies your app's title

<CodeGroup>
  ```typescript title="TypeScript"
  fetch('https://openrouter.ai/api/v1/chat/completions', {
    method: 'POST',
    headers: {
      Authorization: 'Bearer <OPENROUTER_API_KEY>',
      'HTTP-Referer': '<YOUR_SITE_URL>', // Optional. Site URL for rankings on openrouter.ai.
      'X-Title': '<YOUR_SITE_NAME>', // Optional. Site title for rankings on openrouter.ai.
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      model: 'openai/gpt-4o',
      messages: [
        {
          role: 'user',
          content: 'What is the meaning of life?',
        },
      ],
    }),
  });
  ```
</CodeGroup>

<Info title="Model routing">
  If the `model` parameter is omitted, the user or payer's default is used.
  Otherwise, remember to select a value for `model` from the [supported
  models](/models) or [API](/api/v1/models), and include the organization
  prefix. OpenRouter will select the least expensive and best GPUs available to
  serve the request, and fall back to other providers or GPUs if it receives a
  5xx response code or if you are rate-limited.
</Info>

<Info title="Streaming">
  [Server-Sent Events
  (SSE)](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#event_stream_format)
  are supported as well, to enable streaming *for all models*. Simply send
  `stream: true` in your request body. The SSE stream will occasionally contain
  a "comment" payload, which you should ignore (noted below).
</Info>

<Info title="Non-standard parameters">
  If the chosen model doesn't support a request parameter (such as `logit_bias`
  in non-OpenAI models, or `top_k` for OpenAI), then the parameter is ignored.
  The rest are forwarded to the underlying model API.
</Info>

### Assistant Prefill

OpenRouter supports asking models to complete a partial response. This can be useful for guiding models to respond in a certain way.

To use this features, simply include a message with `role: "assistant"` at the end of your `messages` array.

<CodeGroup>
  ```typescript title="TypeScript"
  fetch('https://openrouter.ai/api/v1/chat/completions', {
    method: 'POST',
    headers: {
      Authorization: 'Bearer <OPENROUTER_API_KEY>',
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      model: 'openai/gpt-4o',
      messages: [
        { role: 'user', content: 'What is the meaning of life?' },
        { role: 'assistant', content: "I'm not sure, but my best guess is" },
      ],
    }),
  });
  ```
</CodeGroup>

## Responses

### CompletionsResponse Format

OpenRouter normalizes the schema across models and providers to comply with the [OpenAI Chat API](https://platform.openai.com/docs/api-reference/chat).

This means that `choices` is always an array, even if the model only returns one completion. Each choice will contain a `delta` property if a stream was requested and a `message` property otherwise. This makes it easier to use the same code for all models.

Here's the response schema as a TypeScript type:

```typescript TypeScript
// Definitions of subtypes are below
type Response = {
  id: string;
  // Depending on whether you set "stream" to "true" and
  // whether you passed in "messages" or a "prompt", you
  // will get a different output shape
  choices: (NonStreamingChoice | StreamingChoice | NonChatChoice)[];
  created: number; // Unix timestamp
  model: string;
  object: 'chat.completion' | 'chat.completion.chunk';

  system_fingerprint?: string; // Only present if the provider supports it

  // Usage data is always returned for non-streaming.
  // When streaming, you will get one usage object at
  // the end accompanied by an empty choices array.
  usage?: ResponseUsage;
};
```

```typescript
// If the provider returns usage, we pass it down
// as-is. Otherwise, we count using the GPT-4 tokenizer.

type ResponseUsage = {
  /** Including images and tools if any */
  prompt_tokens: number;
  /** The tokens generated */
  completion_tokens: number;
  /** Sum of the above two fields */
  total_tokens: number;
};
```

```typescript
// Subtypes:
type NonChatChoice = {
  finish_reason: string | null;
  text: string;
  error?: ErrorResponse;
};

type NonStreamingChoice = {
  finish_reason: string | null;
  native_finish_reason: string | null;
  message: {
    content: string | null;
    role: string;
    tool_calls?: ToolCall[];
  };
  error?: ErrorResponse;
};

type StreamingChoice = {
  finish_reason: string | null;
  native_finish_reason: string | null;
  delta: {
    content: string | null;
    role?: string;
    tool_calls?: ToolCall[];
  };
  error?: ErrorResponse;
};

type ErrorResponse = {
  code: number; // See "Error Handling" section
  message: string;
  metadata?: Record<string, unknown>; // Contains additional error information such as provider details, the raw error message, etc.
};

type ToolCall = {
  id: string;
  type: 'function';
  function: FunctionCall;
};
```

Here's an example:

```json
{
  "id": "gen-xxxxxxxxxxxxxx",
  "choices": [
    {
      "finish_reason": "stop", // Normalized finish_reason
      "native_finish_reason": "stop", // The raw finish_reason from the provider
      "message": {
        // will be "delta" if streaming
        "role": "assistant",
        "content": "Hello there!"
      }
    }
  ],
  "usage": {
    "prompt_tokens": 0,
    "completion_tokens": 4,
    "total_tokens": 4
  },
  "model": "openai/gpt-3.5-turbo" // Could also be "anthropic/claude-2.1", etc, depending on the "model" that ends up being used
}
```

### Finish Reason

OpenRouter normalizes each model's `finish_reason` to one of the following values: `tool_calls`, `stop`, `length`, `content_filter`, `error`.

Some models and providers may have additional finish reasons. The raw finish\_reason string returned by the model is available via the `native_finish_reason` property.

### Querying Cost and Stats

The token counts that are returned in the completions API response are **not** counted via the model's native tokenizer. Instead it uses a normalized, model-agnostic count (accomplished via the GPT4o tokenizer). This is because some providers do not reliably return native token counts. This behavior is becoming more rare, however, and we may add native token counts to the response object in the future.

Credit usage and model pricing are based on the **native** token counts (not the 'normalized' token counts returned in the API response).

For precise token accounting using the model's native tokenizer, you can retrieve the full generation information via the `/api/v1/generation` endpoint.

You can use the returned `id` to query for the generation stats (including token counts and cost) after the request is complete. This is how you can get the cost and tokens for *all models and requests*, streaming and non-streaming.

<CodeGroup>
  ```typescript title="Query Generation Stats"
  const generation = await fetch(
    'https://openrouter.ai/api/v1/generation?id=$GENERATION_ID',
    { headers },
  );

  const stats = await generation.json();
  ```
</CodeGroup>

Please see the [Generation](/docs/api-reference/get-a-generation) API reference for the full response shape.

Note that token counts are also available in the `usage` field of the response body for non-streaming completions.


# Streaming

> Learn how to implement streaming responses with OpenRouter's API. Complete guide to Server-Sent Events (SSE) and real-time model outputs.

The OpenRouter API allows streaming responses from *any model*. This is useful for building chat interfaces or other applications where the UI should update as the model generates the response.

To enable streaming, you can set the `stream` parameter to `true` in your request. The model will then stream the response to the client in chunks, rather than returning the entire response at once.

Here is an example of how to stream a response, and process it:

<Template
  data={{
  API_KEY_REF,
  MODEL: Model.GPT_4_Omni
}}
>
  <CodeGroup>
    ```typescript title="TypeScript SDK"
    import { OpenRouter } from '@openrouter/sdk';

    const openRouter = new OpenRouter({
      apiKey: '{{API_KEY_REF}}',
    });

    const question = 'How would you build the tallest building ever?';

    const stream = await openRouter.chat.send({
      model: '{{MODEL}}',
      messages: [{ role: 'user', content: question }],
      stream: true,
      streamOptions: { includeUsage: true }
    });

    for await (const chunk of stream) {
      const content = chunk.choices?.[0]?.delta?.content;
      if (content) {
        console.log(content);
      }

      // Final chunk includes usage stats
      if (chunk.usage) {
        console.log('Usage:', chunk.usage);
      }
    }
    ```

    ```python Python
    import requests
    import json

    question = "How would you build the tallest building ever?"

    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
      "Authorization": f"Bearer {{API_KEY_REF}}",
      "Content-Type": "application/json"
    }

    payload = {
      "model": "{{MODEL}}",
      "messages": [{"role": "user", "content": question}],
      "stream": True
    }

    buffer = ""
    with requests.post(url, headers=headers, json=payload, stream=True) as r:
      for chunk in r.iter_content(chunk_size=1024, decode_unicode=True):
        buffer += chunk
        while True:
          try:
            # Find the next complete SSE line
            line_end = buffer.find('\n')
            if line_end == -1:
              break

            line = buffer[:line_end].strip()
            buffer = buffer[line_end + 1:]

            if line.startswith('data: '):
              data = line[6:]
              if data == '[DONE]':
                break

              try:
                data_obj = json.loads(data)
                content = data_obj["choices"][0]["delta"].get("content")
                if content:
                  print(content, end="", flush=True)
              except json.JSONDecodeError:
                pass
          except Exception:
            break
    ```

    ```typescript title="TypeScript (fetch)"
    const question = 'How would you build the tallest building ever?';
    const response = await fetch('https://openrouter.ai/api/v1/chat/completions', {
      method: 'POST',
      headers: {
        Authorization: `Bearer ${API_KEY_REF}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        model: '{{MODEL}}',
        messages: [{ role: 'user', content: question }],
        stream: true,
      }),
    });

    const reader = response.body?.getReader();
    if (!reader) {
      throw new Error('Response body is not readable');
    }

    const decoder = new TextDecoder();
    let buffer = '';

    try {
      while (true) {
        const { done, value } = await reader.read();
        if (done) break;

        // Append new chunk to buffer
        buffer += decoder.decode(value, { stream: true });

        // Process complete lines from buffer
        while (true) {
          const lineEnd = buffer.indexOf('\n');
          if (lineEnd === -1) break;

          const line = buffer.slice(0, lineEnd).trim();
          buffer = buffer.slice(lineEnd + 1);

          if (line.startsWith('data: ')) {
            const data = line.slice(6);
            if (data === '[DONE]') break;

            try {
              const parsed = JSON.parse(data);
              const content = parsed.choices[0].delta.content;
              if (content) {
                console.log(content);
              }
            } catch (e) {
              // Ignore invalid JSON
            }
          }
        }
      }
    } finally {
      reader.cancel();
    }
    ```
  </CodeGroup>
</Template>

### Additional Information

For SSE (Server-Sent Events) streams, OpenRouter occasionally sends comments to prevent connection timeouts. These comments look like:

```text
: OPENROUTER PROCESSING
```

Comment payload can be safely ignored per the [SSE specs](https://html.spec.whatwg.org/multipage/server-sent-events.html#event-stream-interpretation). However, you can leverage it to improve UX as needed, e.g. by showing a dynamic loading indicator.

Some SSE client implementations might not parse the payload according to spec, which leads to an uncaught error when you `JSON.stringify` the non-JSON payloads. We recommend the following clients:

* [eventsource-parser](https://github.com/rexxars/eventsource-parser)
* [OpenAI SDK](https://www.npmjs.com/package/openai)
* [Vercel AI SDK](https://www.npmjs.com/package/ai)

### Stream Cancellation

Streaming requests can be cancelled by aborting the connection. For supported providers, this immediately stops model processing and billing.

<Accordion title="Provider Support">
  **Supported**

  * OpenAI, Azure, Anthropic
  * Fireworks, Mancer, Recursal
  * AnyScale, Lepton, OctoAI
  * Novita, DeepInfra, Together
  * Cohere, Hyperbolic, Infermatic
  * Avian, XAI, Cloudflare
  * SFCompute, Nineteen, Liquid
  * Friendli, Chutes, DeepSeek

  **Not Currently Supported**

  * AWS Bedrock, Groq, Modal
  * Google, Google AI Studio, Minimax
  * HuggingFace, Replicate, Perplexity
  * Mistral, AI21, Featherless
  * Lynn, Lambda, Reflection
  * SambaNova, Inflection, ZeroOneAI
  * AionLabs, Alibaba, Nebius
  * Kluster, Targon, InferenceNet
</Accordion>

To implement stream cancellation:

<Template
  data={{
  API_KEY_REF,
  MODEL: Model.GPT_4_Omni
}}
>
  <CodeGroup>
    ```typescript title="TypeScript SDK"
    import { OpenRouter } from '@openrouter/sdk';

    const openRouter = new OpenRouter({
      apiKey: '{{API_KEY_REF}}',
    });

    const controller = new AbortController();

    try {
      const stream = await openRouter.chat.send({
        model: '{{MODEL}}',
        messages: [{ role: 'user', content: 'Write a story' }],
        stream: true,
      }, {
        signal: controller.signal,
      });

      for await (const chunk of stream) {
        const content = chunk.choices?.[0]?.delta?.content;
        if (content) {
          console.log(content);
        }
      }
    } catch (error) {
      if (error.name === 'AbortError') {
        console.log('Stream cancelled');
      } else {
        throw error;
      }
    }

    // To cancel the stream:
    controller.abort();
    ```

    ```python Python
    import requests
    from threading import Event, Thread

    def stream_with_cancellation(prompt: str, cancel_event: Event):
        with requests.Session() as session:
            response = session.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers={"Authorization": f"Bearer {{API_KEY_REF}}"},
                json={"model": "{{MODEL}}", "messages": [{"role": "user", "content": prompt}], "stream": True},
                stream=True
            )

            try:
                for line in response.iter_lines():
                    if cancel_event.is_set():
                        response.close()
                        return
                    if line:
                        print(line.decode(), end="", flush=True)
            finally:
                response.close()

    # Example usage:
    cancel_event = Event()
    stream_thread = Thread(target=lambda: stream_with_cancellation("Write a story", cancel_event))
    stream_thread.start()

    # To cancel the stream:
    cancel_event.set()
    ```

    ```typescript title="TypeScript (fetch)"
    const controller = new AbortController();

    try {
      const response = await fetch(
        'https://openrouter.ai/api/v1/chat/completions',
        {
          method: 'POST',
          headers: {
            Authorization: `Bearer ${{{API_KEY_REF}}}`,
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            model: '{{MODEL}}',
            messages: [{ role: 'user', content: 'Write a story' }],
            stream: true,
          }),
          signal: controller.signal,
        },
      );

      // Process the stream...
    } catch (error) {
      if (error.name === 'AbortError') {
        console.log('Stream cancelled');
      } else {
        throw error;
      }
    }

    // To cancel the stream:
    controller.abort();
    ```
  </CodeGroup>
</Template>

<Warning>
  Cancellation only works for streaming requests with supported providers. For
  non-streaming requests or unsupported providers, the model will continue
  processing and you will be billed for the complete response.
</Warning>

### Handling Errors During Streaming

OpenRouter handles errors differently depending on when they occur during the streaming process:

#### Errors Before Any Tokens Are Sent

If an error occurs before any tokens have been streamed to the client, OpenRouter returns a standard JSON error response with the appropriate HTTP status code. This follows the standard error format:

```json
{
  "error": {
    "code": 400,
    "message": "Invalid model specified"
  }
}
```

Common HTTP status codes include:

* **400**: Bad Request (invalid parameters)
* **401**: Unauthorized (invalid API key)
* **402**: Payment Required (insufficient credits)
* **429**: Too Many Requests (rate limited)
* **502**: Bad Gateway (provider error)
* **503**: Service Unavailable (no available providers)

#### Errors After Tokens Have Been Sent (Mid-Stream)

If an error occurs after some tokens have already been streamed to the client, OpenRouter cannot change the HTTP status code (which is already 200 OK). Instead, the error is sent as a Server-Sent Event (SSE) with a unified structure:

```text
data: {"id":"cmpl-abc123","object":"chat.completion.chunk","created":1234567890,"model":"gpt-3.5-turbo","provider":"openai","error":{"code":"server_error","message":"Provider disconnected unexpectedly"},"choices":[{"index":0,"delta":{"content":""},"finish_reason":"error"}]}
```

Key characteristics of mid-stream errors:

* The error appears at the **top level** alongside standard response fields (id, object, created, etc.)
* A `choices` array is included with `finish_reason: "error"` to properly terminate the stream
* The HTTP status remains 200 OK since headers were already sent
* The stream is terminated after this unified error event

#### Code Examples

Here's how to properly handle both types of errors in your streaming implementation:

<Template
  data={{
  API_KEY_REF,
  MODEL: Model.GPT_4_Omni
}}
>
  <CodeGroup>
    ```typescript title="TypeScript SDK"
    import { OpenRouter } from '@openrouter/sdk';

    const openRouter = new OpenRouter({
      apiKey: '{{API_KEY_REF}}',
    });

    async function streamWithErrorHandling(prompt: string) {
      try {
        const stream = await openRouter.chat.send({
          model: '{{MODEL}}',
          messages: [{ role: 'user', content: prompt }],
          stream: true,
        });

        for await (const chunk of stream) {
          // Check for errors in chunk
          if ('error' in chunk) {
            console.error(`Stream error: ${chunk.error.message}`);
            if (chunk.choices?.[0]?.finish_reason === 'error') {
              console.log('Stream terminated due to error');
            }
            return;
          }

          // Process normal content
          const content = chunk.choices?.[0]?.delta?.content;
          if (content) {
            console.log(content);
          }
        }
      } catch (error) {
        // Handle pre-stream errors
        console.error(`Error: ${error.message}`);
      }
    }
    ```

    ```python Python
    import requests
    import json

    async def stream_with_error_handling(prompt):
        response = requests.post(
            'https://openrouter.ai/api/v1/chat/completions',
            headers={'Authorization': f'Bearer {{API_KEY_REF}}'},
            json={
                'model': '{{MODEL}}',
                'messages': [{'role': 'user', 'content': prompt}],
                'stream': True
            },
            stream=True
        )

        # Check initial HTTP status for pre-stream errors
        if response.status_code != 200:
            error_data = response.json()
            print(f"Error: {error_data['error']['message']}")
            return

        # Process stream and handle mid-stream errors
        for line in response.iter_lines():
            if line:
                line_text = line.decode('utf-8')
                if line_text.startswith('data: '):
                    data = line_text[6:]
                    if data == '[DONE]':
                        break

                    try:
                        parsed = json.loads(data)

                        # Check for mid-stream error
                        if 'error' in parsed:
                            print(f"Stream error: {parsed['error']['message']}")
                            # Check finish_reason if needed
                            if parsed.get('choices', [{}])[0].get('finish_reason') == 'error':
                                print("Stream terminated due to error")
                            break

                        # Process normal content
                        content = parsed['choices'][0]['delta'].get('content')
                        if content:
                            print(content, end='', flush=True)

                    except json.JSONDecodeError:
                        pass
    ```

    ```typescript title="TypeScript (fetch)"
    async function streamWithErrorHandling(prompt: string) {
      const response = await fetch(
        'https://openrouter.ai/api/v1/chat/completions',
        {
          method: 'POST',
          headers: {
            'Authorization': `Bearer ${{{API_KEY_REF}}}`,
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            model: '{{MODEL}}',
            messages: [{ role: 'user', content: prompt }],
            stream: true,
          }),
        }
      );

      // Check initial HTTP status for pre-stream errors
      if (!response.ok) {
        const error = await response.json();
        console.error(`Error: ${error.error.message}`);
        return;
      }

      const reader = response.body?.getReader();
      if (!reader) throw new Error('No response body');

      const decoder = new TextDecoder();
      let buffer = '';

      try {
        while (true) {
          const { done, value } = await reader.read();
          if (done) break;

          buffer += decoder.decode(value, { stream: true });

          while (true) {
            const lineEnd = buffer.indexOf('\n');
            if (lineEnd === -1) break;

            const line = buffer.slice(0, lineEnd).trim();
            buffer = buffer.slice(lineEnd + 1);

            if (line.startsWith('data: ')) {
              const data = line.slice(6);
              if (data === '[DONE]') return;

              try {
                const parsed = JSON.parse(data);

                // Check for mid-stream error
                if (parsed.error) {
                  console.error(`Stream error: ${parsed.error.message}`);
                  // Check finish_reason if needed
                  if (parsed.choices?.[0]?.finish_reason === 'error') {
                    console.log('Stream terminated due to error');
                  }
                  return;
                }

                // Process normal content
                const content = parsed.choices[0].delta.content;
                if (content) {
                  console.log(content);
                }
              } catch (e) {
                // Ignore parsing errors
              }
            }
          }
        }
      } finally {
        reader.cancel();
      }
    }
    ```
  </CodeGroup>
</Template>

#### API-Specific Behavior

Different API endpoints may handle streaming errors slightly differently:

* **OpenAI Chat Completions API**: Returns `ErrorResponse` directly if no chunks were processed, or includes error information in the response if some chunks were processed
* **OpenAI Responses API**: May transform certain error codes (like `context_length_exceeded`) into a successful response with `finish_reason: "length"` instead of treating them as errors


# Limits

> Learn about OpenRouter's API rate limits, credit-based quotas, and DDoS protection. Configure and monitor your model usage limits effectively.

<Tip>
  Making additional accounts or API keys will not affect your rate limits, as we
  govern capacity globally. We do however have different rate limits for
  different models, so you can share the load that way if you do run into
  issues.
</Tip>

## Rate Limits and Credits Remaining

To check the rate limit or credits left on an API key, make a GET request to `https://openrouter.ai/api/v1/key`.

<Template data={{ API_KEY_REF }}>
  <CodeGroup>
    ```typescript title="TypeScript SDK"
    import { OpenRouter } from '@openrouter/sdk';

    const openRouter = new OpenRouter({
      apiKey: '{{API_KEY_REF}}',
    });

    const keyInfo = await openRouter.apiKeys.getCurrent();
    console.log(keyInfo);
    ```

    ```python title="Python"
    import requests
    import json

    response = requests.get(
      url="https://openrouter.ai/api/v1/key",
      headers={
        "Authorization": f"Bearer {{API_KEY_REF}}"
      }
    )

    print(json.dumps(response.json(), indent=2))
    ```

    ```typescript title="TypeScript (Raw API)"
    const response = await fetch('https://openrouter.ai/api/v1/key', {
      method: 'GET',
      headers: {
        Authorization: 'Bearer {{API_KEY_REF}}',
      },
    });

    const keyInfo = await response.json();
    console.log(keyInfo);
    ```
  </CodeGroup>
</Template>

If you submit a valid API key, you should get a response of the form:

```typescript title="TypeScript"
type Key = {
  data: {
    label: string;
    limit: number | null; // Credit limit for the key, or null if unlimited
    limit_reset: string | null; // Type of limit reset for the key, or null if never resets
    limit_remaining: number | null; // Remaining credits for the key, or null if unlimited
    include_byok_in_limit: boolean;  // Whether to include external BYOK usage in the credit limit

    usage: number; // Number of credits used (all time)
    usage_daily: number; // Number of credits used (current UTC day)
    usage_weekly: number; // ... (current UTC week, starting Monday)
    usage_monthly: number; // ... (current UTC month)

    byok_usage: number; // Same for external BYOK usage
    byok_usage_daily: number;
    byok_usage_weekly: number;
    byok_usage_monthly: number;

    is_free_tier: boolean; // Whether the user has paid for credits before
    // rate_limit: { ... } // A deprecated object in the response, safe to ignore
  };
};
```

There are a few rate limits that apply to certain types of requests, regardless of account status:

1. Free usage limits: If you're using a free model variant (with an ID ending in <code>{sep}{Variant.Free}</code>), you can make up to {FREE_MODEL_RATE_LIMIT_RPM} requests per minute. The following per-day limits apply:

* If you have purchased less than {FREE_MODEL_CREDITS_THRESHOLD} credits, you're limited to {FREE_MODEL_NO_CREDITS_RPD} <code>{sep}{Variant.Free}</code> model requests per day.

* If you purchase at least {FREE_MODEL_CREDITS_THRESHOLD} credits, your daily limit is increased to {FREE_MODEL_HAS_CREDITS_RPD} <code>{sep}{Variant.Free}</code> model requests per day.

2. **DDoS protection**: Cloudflare's DDoS protection will block requests that dramatically exceed reasonable usage.

If your account has a negative credit balance, you may see <code>{HTTPStatus.S402_Payment_Required}</code> errors, including for free models. Adding credits to put your balance above zero allows you to use those models again.


# Authentication

> Learn how to authenticate with OpenRouter using API keys and Bearer tokens. Complete guide to secure authentication methods and best practices.

You can cover model costs with OpenRouter API keys.

Our API authenticates requests using Bearer tokens. This allows you to use `curl` or the [OpenAI SDK](https://platform.openai.com/docs/frameworks) directly with OpenRouter.

<Warning>
  API keys on OpenRouter are more powerful than keys used directly for model APIs.

  They allow users to set credit limits for apps, and they can be used in [OAuth](/docs/use-cases/oauth-pkce) flows.
</Warning>

## Using an API key

To use an API key, [first create your key](https://openrouter.ai/keys). Give it a name and you can optionally set a credit limit.

If you're calling the OpenRouter API directly, set the `Authorization` header to a Bearer token with your API key.

If you're using the OpenAI Typescript SDK, set the `api_base` to `https://openrouter.ai/api/v1` and the `apiKey` to your API key.

<CodeGroup>
  ```typescript title="TypeScript SDK"
  import { OpenRouter } from '@openrouter/sdk';

  const openRouter = new OpenRouter({
    apiKey: '<OPENROUTER_API_KEY>',
    defaultHeaders: {
      'HTTP-Referer': '<YOUR_SITE_URL>', // Optional. Site URL for rankings on openrouter.ai.
      'X-Title': '<YOUR_SITE_NAME>', // Optional. Site title for rankings on openrouter.ai.
    },
  });

  const completion = await openRouter.chat.send({
    model: 'openai/gpt-4o',
    messages: [{ role: 'user', content: 'Say this is a test' }],
    stream: false,
  });

  console.log(completion.choices[0].message);
  ```

  ```python title="Python (OpenAI SDK)"
  from openai import OpenAI

  client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="<OPENROUTER_API_KEY>",
  )

  response = client.chat.completions.create(
    extra_headers={
      "HTTP-Referer": "<YOUR_SITE_URL>",  # Optional. Site URL for rankings on openrouter.ai.
      "X-Title": "<YOUR_SITE_NAME>",     # Optional. Site title for rankings on openrouter.ai.
    },
    model="openai/gpt-4o",
    messages=[
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "Hello!"}
    ],
  )

  reply = response.choices[0].message
  ```

  ```typescript title="TypeScript (OpenAI SDK)"
  import OpenAI from 'openai';

  const openai = new OpenAI({
    baseURL: 'https://openrouter.ai/api/v1',
    apiKey: '<OPENROUTER_API_KEY>',
    defaultHeaders: {
      'HTTP-Referer': '<YOUR_SITE_URL>', // Optional. Site URL for rankings on openrouter.ai.
      'X-Title': '<YOUR_SITE_NAME>', // Optional. Site title for rankings on openrouter.ai.
    },
  });

  async function main() {
    const completion = await openai.chat.completions.create({
      model: 'openai/gpt-4o',
      messages: [{ role: 'user', content: 'Say this is a test' }],
    });

    console.log(completion.choices[0].message);
  }

  main();
  ```

  ```typescript title="TypeScript (Raw API)"
  fetch('https://openrouter.ai/api/v1/chat/completions', {
    method: 'POST',
    headers: {
      Authorization: 'Bearer <OPENROUTER_API_KEY>',
      'HTTP-Referer': '<YOUR_SITE_URL>', // Optional. Site URL for rankings on openrouter.ai.
      'X-Title': '<YOUR_SITE_NAME>', // Optional. Site title for rankings on openrouter.ai.
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      model: 'openai/gpt-4o',
      messages: [
        {
          role: 'user',
          content: 'What is the meaning of life?',
        },
      ],
    }),
  });
  ```

  ```shell title="cURL"
  curl https://openrouter.ai/api/v1/chat/completions \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $OPENROUTER_API_KEY" \
    -d '{
    "model": "openai/gpt-4o",
    "messages": [
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "Hello!"}
    ]
  }'
  ```
</CodeGroup>

To stream with Python, [see this example from OpenAI](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_stream_completions.ipynb).

## If your key has been exposed

<Warning>
  You must protect your API keys and never commit them to public repositories.
</Warning>

OpenRouter is a GitHub secret scanning partner, and has other methods to detect exposed keys. If we determine that your key has been compromised, you will receive an email notification.

If you receive such a notification or suspect your key has been exposed, immediately visit [your key settings page](https://openrouter.ai/settings/keys) to delete the compromised key and create a new one.

Using environment variables and keeping keys out of your codebase is strongly recommended.


# Parameters

> Learn about all available parameters for OpenRouter API requests. Configure temperature, max tokens, top_p, and other model-specific settings.

Sampling parameters shape the token generation process of the model. You may send any parameters from the following list, as well as others, to OpenRouter.

OpenRouter will default to the values listed below if certain parameters are absent from your request (for example, `temperature` to 1.0). We will also transmit some provider-specific parameters, such as `safe_prompt` for Mistral or `raw_mode` for Hyperbolic directly to the respective providers if specified.

Please refer to the model’s provider section to confirm which parameters are supported. For detailed guidance on managing provider-specific parameters, [click here](/docs/features/provider-routing#requiring-providers-to-support-all-parameters-beta).

## Temperature

* Key: `temperature`

* Optional, **float**, 0.0 to 2.0

* Default: 1.0

* Explainer Video: [Watch](https://youtu.be/ezgqHnWvua8)

This setting influences the variety in the model's responses. Lower values lead to more predictable and typical responses, while higher values encourage more diverse and less common responses. At 0, the model always gives the same response for a given input.

## Top P

* Key: `top_p`

* Optional, **float**, 0.0 to 1.0

* Default: 1.0

* Explainer Video: [Watch](https://youtu.be/wQP-im_HInk)

This setting limits the model's choices to a percentage of likely tokens: only the top tokens whose probabilities add up to P. A lower value makes the model's responses more predictable, while the default setting allows for a full range of token choices. Think of it like a dynamic Top-K.

## Top K

* Key: `top_k`

* Optional, **integer**, 0 or above

* Default: 0

* Explainer Video: [Watch](https://youtu.be/EbZv6-N8Xlk)

This limits the model's choice of tokens at each step, making it choose from a smaller set. A value of 1 means the model will always pick the most likely next token, leading to predictable results. By default this setting is disabled, making the model to consider all choices.

## Frequency Penalty

* Key: `frequency_penalty`

* Optional, **float**, -2.0 to 2.0

* Default: 0.0

* Explainer Video: [Watch](https://youtu.be/p4gl6fqI0_w)

This setting aims to control the repetition of tokens based on how often they appear in the input. It tries to use less frequently those tokens that appear more in the input, proportional to how frequently they occur. Token penalty scales with the number of occurrences. Negative values will encourage token reuse.

## Presence Penalty

* Key: `presence_penalty`

* Optional, **float**, -2.0 to 2.0

* Default: 0.0

* Explainer Video: [Watch](https://youtu.be/MwHG5HL-P74)

Adjusts how often the model repeats specific tokens already used in the input. Higher values make such repetition less likely, while negative values do the opposite. Token penalty does not scale with the number of occurrences. Negative values will encourage token reuse.

## Repetition Penalty

* Key: `repetition_penalty`

* Optional, **float**, 0.0 to 2.0

* Default: 1.0

* Explainer Video: [Watch](https://youtu.be/LHjGAnLm3DM)

Helps to reduce the repetition of tokens from the input. A higher value makes the model less likely to repeat tokens, but too high a value can make the output less coherent (often with run-on sentences that lack small words). Token penalty scales based on original token's probability.

## Min P

* Key: `min_p`

* Optional, **float**, 0.0 to 1.0

* Default: 0.0

Represents the minimum probability for a token to be
considered, relative to the probability of the most likely token. (The value changes depending on the confidence level of the most probable token.) If your Min-P is set to 0.1, that means it will only allow for tokens that are at least 1/10th as probable as the best possible option.

## Top A

* Key: `top_a`

* Optional, **float**, 0.0 to 1.0

* Default: 0.0

Consider only the top tokens with "sufficiently high" probabilities based on the probability of the most likely token. Think of it like a dynamic Top-P. A lower Top-A value focuses the choices based on the highest probability token but with a narrower scope. A higher Top-A value does not necessarily affect the creativity of the output, but rather refines the filtering process based on the maximum probability.

## Seed

* Key: `seed`

* Optional, **integer**

If specified, the inferencing will sample deterministically, such that repeated requests with the same seed and parameters should return the same result. Determinism is not guaranteed for some models.

## Max Tokens

* Key: `max_tokens`

* Optional, **integer**, 1 or above

This sets the upper limit for the number of tokens the model can generate in response. It won't produce more than this limit. The maximum value is the context length minus the prompt length.

## Logit Bias

* Key: `logit_bias`

* Optional, **map**

Accepts a JSON object that maps tokens (specified by their token ID in the tokenizer) to an associated bias value from -100 to 100. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect will vary per model, but values between -1 and 1 should decrease or increase likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant token.

## Logprobs

* Key: `logprobs`

* Optional, **boolean**

Whether to return log probabilities of the output tokens or not. If true, returns the log probabilities of each output token returned.

## Top Logprobs

* Key: `top_logprobs`

* Optional, **integer**

An integer between 0 and 20 specifying the number of most likely tokens to return at each token position, each with an associated log probability. logprobs must be set to true if this parameter is used.

## Response Format

* Key: `response_format`

* Optional, **map**

Forces the model to produce specific output format. Setting to `{ "type": "json_object" }` enables JSON mode, which guarantees the message the model generates is valid JSON.

**Note**: when using JSON mode, you should also instruct the model to produce JSON yourself via a system or user message.

## Structured Outputs

* Key: `structured_outputs`

* Optional, **boolean**

If the model can return structured outputs using response\_format json\_schema.

## Stop

* Key: `stop`

* Optional, **array**

Stop generation immediately if the model encounter any token specified in the stop array.

## Tools

* Key: `tools`

* Optional, **array**

Tool calling parameter, following OpenAI's tool calling request shape. For non-OpenAI providers, it will be transformed accordingly. [Click here to learn more about tool calling](/docs/requests#tool-calls)

## Tool Choice

* Key: `tool_choice`

* Optional, **array**

Controls which (if any) tool is called by the model. 'none' means the model will not call any tool and instead generates a message. 'auto' means the model can pick between generating a message or calling one or more tools. 'required' means the model must call one or more tools. Specifying a particular tool via `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool.

## Parallel Tool Calls

* Key: `parallel_tool_calls`

* Optional, **boolean**

* Default: **true**

Whether to enable parallel function calling during tool use. If true, the model can call multiple functions simultaneously. If false, functions will be called sequentially. Only applies when tools are provided.

## Verbosity

* Key: `verbosity`

* Optional, **enum** (low, medium, high)

* Default: **medium**

Controls the verbosity and length of the model response. Lower values produce more concise responses, while higher values produce more detailed and comprehensive responses.


# Errors

> Learn how to handle errors in OpenRouter API interactions. Comprehensive guide to error codes, messages, and best practices for error handling.

For errors, OpenRouter returns a JSON response with the following shape:

```typescript
type ErrorResponse = {
  error: {
    code: number;
    message: string;
    metadata?: Record<string, unknown>;
  };
};
```

The HTTP Response will have the same status code as `error.code`, forming a request error if:

* Your original request is invalid
* Your API key/account is out of credits

Otherwise, the returned HTTP response status will be <code>{HTTPStatus.S200_OK}</code> and any error occurred while the LLM is producing the output will be emitted in the response body or as an SSE data event.

Example code for printing errors in JavaScript:

```typescript
const request = await fetch('https://openrouter.ai/...');
console.log(request.status); // Will be an error code unless the model started processing your request
const response = await request.json();
console.error(response.error?.status); // Will be an error code
console.error(response.error?.message);
```

## Error Codes

* **{HTTPStatus.S400_Bad_Request}**: Bad Request (invalid or missing params, CORS)
* **{HTTPStatus.S401_Unauthorized}**: Invalid credentials (OAuth session expired, disabled/invalid API key)
* **{HTTPStatus.S402_Payment_Required}**: Your account or API key has insufficient credits. Add more credits and retry the request.
* **{HTTPStatus.S403_Forbidden}**: Your chosen model requires moderation and your input was flagged
* **{HTTPStatus.S408_Request_Timeout}**: Your request timed out
* **{HTTPStatus.S429_Too_Many_Requests}**: You are being rate limited
* **{HTTPStatus.S502_Bad_Gateway}**: Your chosen model is down or we received an invalid response from it
* **{HTTPStatus.S503_Service_Unavailable}**: There is no available model provider that meets your routing requirements

## Moderation Errors

If your input was flagged, the `error.metadata` will contain information about the issue. The shape of the metadata is as follows:

```typescript
type ModerationErrorMetadata = {
  reasons: string[]; // Why your input was flagged
  flagged_input: string; // The text segment that was flagged, limited to 100 characters. If the flagged input is longer than 100 characters, it will be truncated in the middle and replaced with ...
  provider_name: string; // The name of the provider that requested moderation
  model_slug: string;
};
```

## Provider Errors

If the model provider encounters an error, the `error.metadata` will contain information about the issue. The shape of the metadata is as follows:

```typescript
type ProviderErrorMetadata = {
  provider_name: string; // The name of the provider that encountered the error
  raw: unknown; // The raw error from the provider
};
```

## When No Content is Generated

Occasionally, the model may not generate any content. This typically occurs when:

* The model is warming up from a cold start
* The system is scaling up to handle more requests

Warm-up times usually range from a few seconds to a few minutes, depending on the model and provider.

If you encounter persistent no-content issues, consider implementing a simple retry mechanism or trying again with a different provider or model that has more recent activity.

Additionally, be aware that in some cases, you may still be charged for the prompt processing cost by the upstream provider, even if no content is generated.

## Streaming Error Formats

When using streaming mode (`stream: true`), errors are handled differently depending on when they occur:

### Pre-Stream Errors

Errors that occur before any tokens are sent follow the standard error format above, with appropriate HTTP status codes.

### Mid-Stream Errors

Errors that occur after streaming has begun are sent as Server-Sent Events (SSE) with a unified structure that includes both the error details and a completion choice:

```typescript
type MidStreamError = {
  id: string;
  object: 'chat.completion.chunk';
  created: number;
  model: string;
  provider: string;
  error: {
    code: string | number;
    message: string;
  };
  choices: [{
    index: 0;
    delta: { content: '' };
    finish_reason: 'error';
    native_finish_reason?: string;
  }];
};
```

Example SSE data:

```text
data: {"id":"cmpl-abc123","object":"chat.completion.chunk","created":1234567890,"model":"gpt-3.5-turbo","provider":"openai","error":{"code":"server_error","message":"Provider disconnected"},"choices":[{"index":0,"delta":{"content":""},"finish_reason":"error"}]}
```

Key characteristics:

* The error appears at the **top level** alongside standard response fields
* A `choices` array is included with `finish_reason: "error"` to properly terminate the stream
* The HTTP status remains 200 OK since headers were already sent
* The stream is terminated after this event

## OpenAI Responses API Error Events

The OpenAI Responses API (`/api/alpha/responses`) uses specific event types for streaming errors:

### Error Event Types

1. **`response.failed`** - Official failure event
   ```json
   {
     "type": "response.failed",
     "response": {
       "id": "resp_abc123",
       "status": "failed",
       "error": {
         "code": "server_error",
         "message": "Internal server error"
       }
     }
   }
   ```

2. **`response.error`** - Error during response generation
   ```json
   {
     "type": "response.error",
     "error": {
       "code": "rate_limit_exceeded",
       "message": "Rate limit exceeded"
     }
   }
   ```

3. **`error`** - Plain error event (undocumented but sent by OpenAI)
   ```json
   {
     "type": "error",
     "error": {
       "code": "invalid_api_key",
       "message": "Invalid API key provided"
     }
   }
   ```

### Error Code Transformations

The Responses API transforms certain error codes into successful completions with specific finish reasons:

| Error Code                | Transformed To | Finish Reason |
| ------------------------- | -------------- | ------------- |
| `context_length_exceeded` | Success        | `length`      |
| `max_tokens_exceeded`     | Success        | `length`      |
| `token_limit_exceeded`    | Success        | `length`      |
| `string_too_long`         | Success        | `length`      |

This allows for graceful handling of limit-based errors without treating them as failures.

## API-Specific Error Handling

Different OpenRouter API endpoints handle errors in distinct ways:

### OpenAI Chat Completions API (`/api/v1/chat/completions`)

* **No tokens sent**: Returns standalone `ErrorResponse`
* **Some tokens sent**: Embeds error information within the `choices` array of the final response
* **Streaming**: Errors sent as SSE events with top-level error field

### OpenAI Responses API (`/api/alpha/responses`)

* **Error transformations**: Certain errors become successful responses with appropriate finish reasons
* **Streaming events**: Uses typed events (`response.failed`, `response.error`, `error`)
* **Graceful degradation**: Handles provider-specific errors with fallback behavior

### Error Response Type Definitions

```typescript
// Standard error response
interface ErrorResponse {
  error: {
    code: number;
    message: string;
    metadata?: Record<string, unknown>;
  };
}

// Mid-stream error with completion data
interface StreamErrorChunk {
  error: {
    code: string | number;
    message: string;
  };
  choices: Array<{
    delta: { content: string };
    finish_reason: 'error';
    native_finish_reason: string;
  }>;
}

// Responses API error event
interface ResponsesAPIErrorEvent {
  type: 'response.failed' | 'response.error' | 'error';
  error?: {
    code: string;
    message: string;
  };
  response?: {
    id: string;
    status: 'failed';
    error: {
      code: string;
      message: string;
    };
  };
}
```


# Responses API Beta

> Beta version of OpenRouter's OpenAI-compatible Responses API. Stateless transformation layer with support for reasoning, tool calling, and web search.

<Warning title="Beta API">
  This API is in **beta stage** and may have breaking changes. Use with caution in production environments.
</Warning>

<Info title="Stateless Only">
  This API is **stateless** - each request is independent and no conversation state is persisted between requests. You must include the full conversation history in each request.
</Info>

OpenRouter's Responses API Beta provides OpenAI-compatible access to multiple AI models through a unified interface, designed to be a drop-in replacement for OpenAI's Responses API. This stateless API offers enhanced capabilities including reasoning, tool calling, and web search integration, with each request being independent and no server-side state persisted.

## Base URL

```
https://openrouter.ai/api/v1/responses
```

## Authentication

All requests require authentication using your OpenRouter API key:

<CodeGroup>
  ```typescript title="TypeScript"
  const response = await fetch('https://openrouter.ai/api/v1/responses', {
    method: 'POST',
    headers: {
      'Authorization': 'Bearer YOUR_OPENROUTER_API_KEY',
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      model: 'openai/o4-mini',
      input: 'Hello, world!',
    }),
  });
  ```

  ```python title="Python"
  import requests

  response = requests.post(
      'https://openrouter.ai/api/v1/responses',
      headers={
          'Authorization': 'Bearer YOUR_OPENROUTER_API_KEY',
          'Content-Type': 'application/json',
      },
      json={
          'model': 'openai/o4-mini',
          'input': 'Hello, world!',
      }
  )
  ```

  ```bash title="cURL"
  curl -X POST https://openrouter.ai/api/v1/responses \
    -H "Authorization: Bearer YOUR_OPENROUTER_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "openai/o4-mini",
      "input": "Hello, world!"
    }'
  ```
</CodeGroup>

## Core Features

### [Basic Usage](./basic-usage)

Learn the fundamentals of making requests with simple text input and handling responses.

### [Reasoning](./reasoning)

Access advanced reasoning capabilities with configurable effort levels and encrypted reasoning chains.

### [Tool Calling](./tool-calling)

Integrate function calling with support for parallel execution and complex tool interactions.

### [Web Search](./web-search)

Enable web search capabilities with real-time information retrieval and citation annotations.

## Error Handling

The API returns structured error responses:

```json
{
  "error": {
    "code": "invalid_prompt",
    "message": "Missing required parameter: 'model'."
  },
  "metadata": null
}
```

For comprehensive error handling guidance, see [Error Handling](./error-handling).

## Rate Limits

Standard OpenRouter rate limits apply. See [API Limits](/docs/api-reference/limits) for details.


# Basic Usage

> Learn the basics of OpenRouter's Responses API Beta with simple text input examples and response handling.

<Warning title="Beta API">
  This API is in **beta stage** and may have breaking changes.
</Warning>

The Responses API Beta supports both simple string input and structured message arrays, making it easy to get started with basic text generation.

## Simple String Input

The simplest way to use the API is with a string input:

<CodeGroup>
  ```typescript title="TypeScript"
  const response = await fetch('https://openrouter.ai/api/v1/responses', {
    method: 'POST',
    headers: {
      'Authorization': 'Bearer YOUR_OPENROUTER_API_KEY',
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      model: 'openai/o4-mini',
      input: 'What is the meaning of life?',
      max_output_tokens: 9000,
    }),
  });

  const result = await response.json();
  console.log(result);
  ```

  ```python title="Python"
  import requests

  response = requests.post(
      'https://openrouter.ai/api/v1/responses',
      headers={
          'Authorization': 'Bearer YOUR_OPENROUTER_API_KEY',
          'Content-Type': 'application/json',
      },
      json={
          'model': 'openai/o4-mini',
          'input': 'What is the meaning of life?',
          'max_output_tokens': 9000,
      }
  )

  result = response.json()
  print(result)
  ```

  ```bash title="cURL"
  curl -X POST https://openrouter.ai/api/v1/responses \
    -H "Authorization: Bearer YOUR_OPENROUTER_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "openai/o4-mini",
      "input": "What is the meaning of life?",
      "max_output_tokens": 9000
    }'
  ```
</CodeGroup>

## Structured Message Input

For more complex conversations, use the message array format:

<CodeGroup>
  ```typescript title="TypeScript"
  const response = await fetch('https://openrouter.ai/api/v1/responses', {
    method: 'POST',
    headers: {
      'Authorization': 'Bearer YOUR_OPENROUTER_API_KEY',
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      model: 'openai/o4-mini',
      input: [
        {
          type: 'message',
          role: 'user',
          content: [
            {
              type: 'input_text',
              text: 'Tell me a joke about programming',
            },
          ],
        },
      ],
      max_output_tokens: 9000,
    }),
  });

  const result = await response.json();
  ```

  ```python title="Python"
  import requests

  response = requests.post(
      'https://openrouter.ai/api/v1/responses',
      headers={
          'Authorization': 'Bearer YOUR_OPENROUTER_API_KEY',
          'Content-Type': 'application/json',
      },
      json={
          'model': 'openai/o4-mini',
          'input': [
              {
                  'type': 'message',
                  'role': 'user',
                  'content': [
                      {
                          'type': 'input_text',
                          'text': 'Tell me a joke about programming',
                      },
                  ],
              },
          ],
          'max_output_tokens': 9000,
      }
  )

  result = response.json()
  ```

  ```bash title="cURL"
  curl -X POST https://openrouter.ai/api/v1/responses \
    -H "Authorization: Bearer YOUR_OPENROUTER_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "openai/o4-mini",
      "input": [
        {
          "type": "message",
          "role": "user",
          "content": [
            {
              "type": "input_text",
              "text": "Tell me a joke about programming"
            }
          ]
        }
      ],
      "max_output_tokens": 9000
    }'
  ```
</CodeGroup>

## Response Format

The API returns a structured response with the generated content:

```json
{
  "id": "resp_1234567890",
  "object": "response",
  "created_at": 1234567890,
  "model": "openai/o4-mini",
  "output": [
    {
      "type": "message",
      "id": "msg_abc123",
      "status": "completed",
      "role": "assistant",
      "content": [
        {
          "type": "output_text",
          "text": "The meaning of life is a philosophical question that has been pondered for centuries...",
          "annotations": []
        }
      ]
    }
  ],
  "usage": {
    "input_tokens": 12,
    "output_tokens": 45,
    "total_tokens": 57
  },
  "status": "completed"
}
```

## Streaming Responses

Enable streaming for real-time response generation:

<CodeGroup>
  ```typescript title="TypeScript"
  const response = await fetch('https://openrouter.ai/api/v1/responses', {
    method: 'POST',
    headers: {
      'Authorization': 'Bearer YOUR_OPENROUTER_API_KEY',
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      model: 'openai/o4-mini',
      input: 'Write a short story about AI',
      stream: true,
      max_output_tokens: 9000,
    }),
  });

  const reader = response.body?.getReader();
  const decoder = new TextDecoder();

  while (true) {
    const { done, value } = await reader.read();
    if (done) break;

    const chunk = decoder.decode(value);
    const lines = chunk.split('\n');

    for (const line of lines) {
      if (line.startsWith('data: ')) {
        const data = line.slice(6);
        if (data === '[DONE]') return;

        try {
          const parsed = JSON.parse(data);
          console.log(parsed);
        } catch (e) {
          // Skip invalid JSON
        }
      }
    }
  }
  ```

  ```python title="Python"
  import requests
  import json

  response = requests.post(
      'https://openrouter.ai/api/v1/responses',
      headers={
          'Authorization': 'Bearer YOUR_OPENROUTER_API_KEY',
          'Content-Type': 'application/json',
      },
      json={
          'model': 'openai/o4-mini',
          'input': 'Write a short story about AI',
          'stream': True,
          'max_output_tokens': 9000,
      },
      stream=True
  )

  for line in response.iter_lines():
      if line:
          line_str = line.decode('utf-8')
          if line_str.startswith('data: '):
              data = line_str[6:]
              if data == '[DONE]':
                  break
              try:
                  parsed = json.loads(data)
                  print(parsed)
              except json.JSONDecodeError:
                  continue
  ```
</CodeGroup>

### Example Streaming Output

The streaming response returns Server-Sent Events (SSE) chunks:

```
data: {"type":"response.created","response":{"id":"resp_1234567890","object":"response","status":"in_progress"}}

data: {"type":"response.output_item.added","response_id":"resp_1234567890","output_index":0,"item":{"type":"message","id":"msg_abc123","role":"assistant","status":"in_progress","content":[]}}

data: {"type":"response.content_part.added","response_id":"resp_1234567890","output_index":0,"content_index":0,"part":{"type":"output_text","text":""}}

data: {"type":"response.content_part.delta","response_id":"resp_1234567890","output_index":0,"content_index":0,"delta":"Once"}

data: {"type":"response.content_part.delta","response_id":"resp_1234567890","output_index":0,"content_index":0,"delta":" upon"}

data: {"type":"response.content_part.delta","response_id":"resp_1234567890","output_index":0,"content_index":0,"delta":" a"}

data: {"type":"response.content_part.delta","response_id":"resp_1234567890","output_index":0,"content_index":0,"delta":" time"}

data: {"type":"response.output_item.done","response_id":"resp_1234567890","output_index":0,"item":{"type":"message","id":"msg_abc123","role":"assistant","status":"completed","content":[{"type":"output_text","text":"Once upon a time, in a world where artificial intelligence had become as common as smartphones..."}]}}

data: {"type":"response.done","response":{"id":"resp_1234567890","object":"response","status":"completed","usage":{"input_tokens":12,"output_tokens":45,"total_tokens":57}}}

data: [DONE]
```

## Common Parameters

| Parameter           | Type            | Description                                         |
| ------------------- | --------------- | --------------------------------------------------- |
| `model`             | string          | **Required.** Model to use (e.g., `openai/o4-mini`) |
| `input`             | string or array | **Required.** Text or message array                 |
| `stream`            | boolean         | Enable streaming responses (default: false)         |
| `max_output_tokens` | integer         | Maximum tokens to generate                          |
| `temperature`       | number          | Sampling temperature (0-2)                          |
| `top_p`             | number          | Nucleus sampling parameter (0-1)                    |

## Error Handling

Handle common errors gracefully:

<CodeGroup>
  ```typescript title="TypeScript"
  try {
    const response = await fetch('https://openrouter.ai/api/v1/responses', {
      method: 'POST',
      headers: {
        'Authorization': 'Bearer YOUR_OPENROUTER_API_KEY',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        model: 'openai/o4-mini',
        input: 'Hello, world!',
      }),
    });

    if (!response.ok) {
      const error = await response.json();
      console.error('API Error:', error.error.message);
      return;
    }

    const result = await response.json();
    console.log(result);
  } catch (error) {
    console.error('Network Error:', error);
  }
  ```

  ```python title="Python"
  import requests

  try:
      response = requests.post(
          'https://openrouter.ai/api/v1/responses',
          headers={
              'Authorization': 'Bearer YOUR_OPENROUTER_API_KEY',
              'Content-Type': 'application/json',
          },
          json={
              'model': 'openai/o4-mini',
              'input': 'Hello, world!',
          }
      )

      if response.status_code != 200:
          error = response.json()
          print(f"API Error: {error['error']['message']}")
      else:
          result = response.json()
          print(result)

  except requests.RequestException as e:
      print(f"Network Error: {e}")
  ```
</CodeGroup>

## Multiple Turn Conversations

Since the Responses API Beta is stateless, you must include the full conversation history in each request to maintain context:

<CodeGroup>
  ```typescript title="TypeScript"
  // First request
  const firstResponse = await fetch('https://openrouter.ai/api/beta/responses', {
    method: 'POST',
    headers: {
      'Authorization': 'Bearer YOUR_OPENROUTER_API_KEY',
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      model: 'openai/o4-mini',
      input: [
        {
          type: 'message',
          role: 'user',
          content: [
            {
              type: 'input_text',
              text: 'What is the capital of France?',
            },
          ],
        },
      ],
      max_output_tokens: 9000,
    }),
  });

  const firstResult = await firstResponse.json();

  // Second request - include previous conversation
  const secondResponse = await fetch('https://openrouter.ai/api/beta/responses', {
    method: 'POST',
    headers: {
      'Authorization': 'Bearer YOUR_OPENROUTER_API_KEY',
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      model: 'openai/o4-mini',
      input: [
        {
          type: 'message',
          role: 'user',
          content: [
            {
              type: 'input_text',
              text: 'What is the capital of France?',
            },
          ],
        },
        {
          type: 'message',
          role: 'assistant',
          id: 'msg_abc123',
          status: 'completed',
          content: [
            {
              type: 'output_text',
              text: 'The capital of France is Paris.',
              annotations: []
            }
          ]
        },
        {
          type: 'message',
          role: 'user',
          content: [
            {
              type: 'input_text',
              text: 'What is the population of that city?',
            },
          ],
        },
      ],
      max_output_tokens: 9000,
    }),
  });

  const secondResult = await secondResponse.json();
  ```

  ```python title="Python"
  import requests

  # First request
  first_response = requests.post(
      'https://openrouter.ai/api/v1/responses',
      headers={
          'Authorization': 'Bearer YOUR_OPENROUTER_API_KEY',
          'Content-Type': 'application/json',
      },
      json={
          'model': 'openai/o4-mini',
          'input': [
              {
                  'type': 'message',
                  'role': 'user',
                  'content': [
                      {
                          'type': 'input_text',
                          'text': 'What is the capital of France?',
                      },
                  ],
              },
          ],
          'max_output_tokens': 9000,
      }
  )

  first_result = first_response.json()

  # Second request - include previous conversation
  second_response = requests.post(
      'https://openrouter.ai/api/v1/responses',
      headers={
          'Authorization': 'Bearer YOUR_OPENROUTER_API_KEY',
          'Content-Type': 'application/json',
      },
      json={
          'model': 'openai/o4-mini',
          'input': [
              {
                  'type': 'message',
                  'role': 'user',
                  'content': [
                      {
                          'type': 'input_text',
                          'text': 'What is the capital of France?',
                      },
                  ],
              },
              {
                  'type': 'message',
                  'role': 'assistant',
                  'id': 'msg_abc123',
                  'status': 'completed',
                  'content': [
                      {
                          'type': 'output_text',
                          'text': 'The capital of France is Paris.',
                          'annotations': []
                      }
                  ]
              },
              {
                  'type': 'message',
                  'role': 'user',
                  'content': [
                      {
                          'type': 'input_text',
                          'text': 'What is the population of that city?',
                      },
                  ],
              },
          ],
          'max_output_tokens': 9000,
      }
  )

  second_result = second_response.json()
  ```
</CodeGroup>

<Info title="Required Fields">
  The `id` and `status` fields are required for any `assistant` role messages included in the conversation history.
</Info>

<Info title="Conversation History">
  Always include the complete conversation history in each request. The API does not store previous messages, so context must be maintained client-side.
</Info>

## Next Steps

* Learn about [Reasoning](./reasoning) capabilities
* Explore [Tool Calling](./tool-calling) functionality
* Try [Web Search](./web-search) integration


# Reasoning

> Access advanced reasoning capabilities with configurable effort levels and encrypted reasoning chains using OpenRouter's Responses API Beta.

<Warning title="Beta API">
  This API is in **beta stage** and may have breaking changes.
</Warning>

The Responses API Beta supports advanced reasoning capabilities, allowing models to show their internal reasoning process with configurable effort levels.

## Reasoning Configuration

Configure reasoning behavior using the `reasoning` parameter:

<CodeGroup>
  ```typescript title="TypeScript"
  const response = await fetch('https://openrouter.ai/api/v1/responses', {
    method: 'POST',
    headers: {
      'Authorization': 'Bearer YOUR_OPENROUTER_API_KEY',
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      model: 'openai/o4-mini',
      input: 'What is the meaning of life?',
      reasoning: {
        effort: 'high'
      },
      max_output_tokens: 9000,
    }),
  });

  const result = await response.json();
  console.log(result);
  ```

  ```python title="Python"
  import requests

  response = requests.post(
      'https://openrouter.ai/api/v1/responses',
      headers={
          'Authorization': 'Bearer YOUR_OPENROUTER_API_KEY',
          'Content-Type': 'application/json',
      },
      json={
          'model': 'openai/o4-mini',
          'input': 'What is the meaning of life?',
          'reasoning': {
              'effort': 'high'
          },
          'max_output_tokens': 9000,
      }
  )

  result = response.json()
  print(result)
  ```

  ```bash title="cURL"
  curl -X POST https://openrouter.ai/api/v1/responses \
    -H "Authorization: Bearer YOUR_OPENROUTER_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "openai/o4-mini",
      "input": "What is the meaning of life?",
      "reasoning": {
        "effort": "high"
      },
      "max_output_tokens": 9000
    }'
  ```
</CodeGroup>

## Reasoning Effort Levels

The `effort` parameter controls how much computational effort the model puts into reasoning:

| Effort Level | Description                                       |
| ------------ | ------------------------------------------------- |
| `minimal`    | Basic reasoning with minimal computational effort |
| `low`        | Light reasoning for simple problems               |
| `medium`     | Balanced reasoning for moderate complexity        |
| `high`       | Deep reasoning for complex problems               |

## Complex Reasoning Example

For complex mathematical or logical problems:

<CodeGroup>
  ```typescript title="TypeScript"
  const response = await fetch('https://openrouter.ai/api/v1/responses', {
    method: 'POST',
    headers: {
      'Authorization': 'Bearer YOUR_OPENROUTER_API_KEY',
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      model: 'openai/o4-mini',
      input: [
        {
          type: 'message',
          role: 'user',
          content: [
            {
              type: 'input_text',
              text: 'Was 1995 30 years ago? Please show your reasoning.',
            },
          ],
        },
      ],
      reasoning: {
        effort: 'high'
      },
      max_output_tokens: 9000,
    }),
  });

  const result = await response.json();
  console.log(result);
  ```

  ```python title="Python"
  import requests

  response = requests.post(
      'https://openrouter.ai/api/v1/responses',
      headers={
          'Authorization': 'Bearer YOUR_OPENROUTER_API_KEY',
          'Content-Type': 'application/json',
      },
      json={
          'model': 'openai/o4-mini',
          'input': [
              {
                  'type': 'message',
                  'role': 'user',
                  'content': [
                      {
                          'type': 'input_text',
                          'text': 'Was 1995 30 years ago? Please show your reasoning.',
                      },
                  ],
              },
          ],
          'reasoning': {
              'effort': 'high'
          },
          'max_output_tokens': 9000,
      }
  )

  result = response.json()
  print(result)
  ```
</CodeGroup>

## Reasoning in Conversation Context

Include reasoning in multi-turn conversations:

<CodeGroup>
  ```typescript title="TypeScript"
  const response = await fetch('https://openrouter.ai/api/v1/responses', {
    method: 'POST',
    headers: {
      'Authorization': 'Bearer YOUR_OPENROUTER_API_KEY',
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      model: 'openai/o4-mini',
      input: [
        {
          type: 'message',
          role: 'user',
          content: [
            {
              type: 'input_text',
              text: 'What is your favorite color?',
            },
          ],
        },
        {
          type: 'message',
          role: 'assistant',
          id: 'msg_abc123',
          status: 'completed',
          content: [
            {
              type: 'output_text',
              text: "I don't have a favorite color.",
              annotations: []
            }
          ]
        },
        {
          type: 'message',
          role: 'user',
          content: [
            {
              type: 'input_text',
              text: 'How many Earths can fit on Mars?',
            },
          ],
        },
      ],
      reasoning: {
        effort: 'high'
      },
      max_output_tokens: 9000,
    }),
  });

  const result = await response.json();
  console.log(result);
  ```

  ```python title="Python"
  import requests

  response = requests.post(
      'https://openrouter.ai/api/v1/responses',
      headers={
          'Authorization': 'Bearer YOUR_OPENROUTER_API_KEY',
          'Content-Type': 'application/json',
      },
      json={
          'model': 'openai/o4-mini',
          'input': [
              {
                  'type': 'message',
                  'role': 'user',
                  'content': [
                      {
                          'type': 'input_text',
                          'text': 'What is your favorite color?',
                      },
                  ],
              },
              {
                  'type': 'message',
                  'role': 'assistant',
                  'id': 'msg_abc123',
                  'status': 'completed',
                  'content': [
                      {
                          'type': 'output_text',
                          'text': "I don't have a favorite color.",
                          'annotations': []
                      }
                  ]
              },
              {
                  'type': 'message',
                  'role': 'user',
                  'content': [
                      {
                          'type': 'input_text',
                          'text': 'How many Earths can fit on Mars?',
                      },
                  ],
              },
          ],
          'reasoning': {
              'effort': 'high'
          },
          'max_output_tokens': 9000,
      }
  )

  result = response.json()
  print(result)
  ```
</CodeGroup>

## Streaming Reasoning

Enable streaming to see reasoning develop in real-time:

<CodeGroup>
  ```typescript title="TypeScript"
  const response = await fetch('https://openrouter.ai/api/v1/responses', {
    method: 'POST',
    headers: {
      'Authorization': 'Bearer YOUR_OPENROUTER_API_KEY',
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      model: 'openai/o4-mini',
      input: 'Solve this step by step: If a train travels 60 mph for 2.5 hours, how far does it go?',
      reasoning: {
        effort: 'medium'
      },
      stream: true,
      max_output_tokens: 9000,
    }),
  });

  const reader = response.body?.getReader();
  const decoder = new TextDecoder();

  while (true) {
    const { done, value } = await reader.read();
    if (done) break;

    const chunk = decoder.decode(value);
    const lines = chunk.split('\n');

    for (const line of lines) {
      if (line.startsWith('data: ')) {
        const data = line.slice(6);
        if (data === '[DONE]') return;

        try {
          const parsed = JSON.parse(data);
          if (parsed.type === 'response.reasoning.delta') {
            console.log('Reasoning:', parsed.delta);
          }
        } catch (e) {
          // Skip invalid JSON
        }
      }
    }
  }
  ```

  ```python title="Python"
  import requests
  import json

  response = requests.post(
      'https://openrouter.ai/api/v1/responses',
      headers={
          'Authorization': 'Bearer YOUR_OPENROUTER_API_KEY',
          'Content-Type': 'application/json',
      },
      json={
          'model': 'openai/o4-mini',
          'input': 'Solve this step by step: If a train travels 60 mph for 2.5 hours, how far does it go?',
          'reasoning': {
              'effort': 'medium'
          },
          'stream': True,
          'max_output_tokens': 9000,
      },
      stream=True
  )

  for line in response.iter_lines():
      if line:
          line_str = line.decode('utf-8')
          if line_str.startswith('data: '):
              data = line_str[6:]
              if data == '[DONE]':
                  break
              try:
                  parsed = json.loads(data)
                  if parsed.get('type') == 'response.reasoning.delta':
                      print(f"Reasoning: {parsed.get('delta', '')}")
              except json.JSONDecodeError:
                  continue
  ```
</CodeGroup>

## Response with Reasoning

When reasoning is enabled, the response includes reasoning information:

```json
{
  "id": "resp_1234567890",
  "object": "response",
  "created_at": 1234567890,
  "model": "openai/o4-mini",
  "output": [
    {
      "type": "reasoning",
      "id": "rs_abc123",
      "encrypted_content": "gAAAAABotI9-FK1PbhZhaZk4yMrZw3XDI1AWFaKb9T0NQq7LndK6zaRB...",
      "summary": [
        "First, I need to determine the current year",
        "Then calculate the difference from 1995",
        "Finally, compare that to 30 years"
      ]
    },
    {
      "type": "message",
      "id": "msg_xyz789",
      "status": "completed",
      "role": "assistant",
      "content": [
        {
          "type": "output_text",
          "text": "Yes. In 2025, 1995 was 30 years ago. In fact, as of today (Aug 31, 2025), it's exactly 30 years since Aug 31, 1995.",
          "annotations": []
        }
      ]
    }
  ],
  "usage": {
    "input_tokens": 15,
    "output_tokens": 85,
    "output_tokens_details": {
      "reasoning_tokens": 45
    },
    "total_tokens": 100
  },
  "status": "completed"
}
```

## Best Practices

1. **Choose appropriate effort levels**: Use `high` for complex problems, `low` for simple tasks
2. **Consider token usage**: Reasoning increases token consumption
3. **Use streaming**: For long reasoning chains, streaming provides better user experience
4. **Include context**: Provide sufficient context for the model to reason effectively

## Next Steps

* Explore [Tool Calling](./tool-calling) with reasoning
* Learn about [Web Search](./web-search) integration
* Review [Basic Usage](./basic-usage) fundamentals



---

**Navigation:** [← Previous](./01-quickstart.md) | [Index](./index.md) | [Next →](./03-tool-calling.md)
