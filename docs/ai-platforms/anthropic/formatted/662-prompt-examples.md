---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Prompt examples

Many of the [prompting techniques](/en/docs/build-with-claude/prompt-engineering/overview) that work well for text-based interactions with Claude can also be applied to image-based prompts.

These examples demonstrate best practice prompt structures involving images.

<Tip>
  Just as with document-query placement, Claude works best when images come
  before text. Images placed after text or interpolated with text will still
  perform well, but if your use case allows it, we recommend an image-then-text
  structure.
</Tip>

### About the prompt examples

The following examples demonstrate how to use Claude's vision capabilities using various programming languages and approaches. You can provide images to Claude in three ways:

1. As a base64-encoded image in `image` content blocks
2. As a URL reference to an image hosted online
3. Using the Files API (upload once, use multiple times)

The base64 example prompts use these variables:
```bash
      # For URL-based images, you can use the URL directly in your JSON request

      
      # For base64-encoded images, you need to first encode the image

      # Example of how to encode an image to base64 in bash:

      BASE64_IMAGE_DATA=$(curl -s "https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg" | base64)
      
      # The encoded data can now be used in your API calls

```
```Python
  import base64
  import httpx

  # For base64-encoded images

  image1_url = "https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg"
  image1_media_type = "image/jpeg"
  image1_data = base64.standard_b64encode(httpx.get(image1_url).content).decode("utf-8")

  image2_url = "https://upload.wikimedia.org/wikipedia/commons/b/b5/Iridescent.green.sweat.bee1.jpg"
  image2_media_type = "image/jpeg"
  image2_data = base64.standard_b64encode(httpx.get(image2_url).content).decode("utf-8")

  # For URL-based images, you can use the URLs directly in your requests

```
```TypeScript
  import axios from 'axios';

  // For base64-encoded images
  async function getBase64Image(url: string): Promise<string> {
    const response = await axios.get(url, { responseType: 'arraybuffer' });
    return Buffer.from(response.data, 'binary').toString('base64');
  }

  // Usage
  async function prepareImages() {
    const imageData = await getBase64Image('https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg');
    // Now you can use imageData in your API calls
  }

  // For URL-based images, you can use the URLs directly in your requests
```
```java
  import java.io.IOException;
  import java.util.Base64;
  import java.io.InputStream;
  import java.net.URL;

  public class ImageHandlingExample {

      public static void main(String[] args) throws IOException, InterruptedException {
          // For base64-encoded images
          String image1Url = "https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg";
          String image1MediaType = "image/jpeg";
          String image1Data = downloadAndEncodeImage(image1Url);

          String image2Url = "https://upload.wikimedia.org/wikipedia/commons/b/b5/Iridescent.green.sweat.bee1.jpg";
          String image2MediaType = "image/jpeg";
          String image2Data = downloadAndEncodeImage(image2Url);

          // For URL-based images, you can use the URLs directly in your requests
      }

      private static String downloadAndEncodeImage(String imageUrl) throws IOException {
          try (InputStream inputStream = new URL(imageUrl).openStream()) {
              return Base64.getEncoder().encodeToString(inputStream.readAllBytes());
          }
      }

  }
```

Below are examples of how to include images in a Messages API request using base64-encoded images and URL references:

### Base64-encoded image example

```bash
  curl https://api.anthropic.com/v1/messages \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "content-type: application/json" \
    -d '{
      "model": "claude-sonnet-4-5",
      "max_tokens": 1024,
      "messages": [
        {
          "role": "user",
          "content": [
            {
              "type": "image",
              "source": {
                "type": "base64",
                "media_type": "image/jpeg",
                "data": "'"$BASE64_IMAGE_DATA"'"
              }
            },
            {
              "type": "text",
              "text": "Describe this image."
            }
          ]
        }
      ]
    }'
```
```Python
  import anthropic

  client = anthropic.Anthropic()
  message = client.messages.create(
      model="claude-sonnet-4-5",
      max_tokens=1024,
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "image",
                      "source": {
                          "type": "base64",
                          "media_type": image1_media_type,
                          "data": image1_data,
                      },
                  },
                  {
                      "type": "text",
                      "text": "Describe this image."
                  }
              ],
          }
      ],
  )
  print(message)
```
```TypeScript
  import Anthropic from '@anthropic-ai/sdk';

  const anthropic = new Anthropic({
    apiKey: process.env.ANTHROPIC_API_KEY,
  });

  async function main() {
    const message = await anthropic.messages.create({
      model: "claude-sonnet-4-5",
      max_tokens: 1024,
      messages: [
        {
          role: "user",
          content: [
            {
              type: "image",
              source: {
                type: "base64",
                media_type: "image/jpeg",
                data: imageData, // Base64-encoded image data as string
              }
            },
            {
              type: "text",
              text: "Describe this image."
            }
          ]
        }
      ]
    });
    
    console.log(message);
  }

  main();
```
```Java
  import java.io.IOException;
  import java.util.List;

  import com.anthropic.client.AnthropicClient;
  import com.anthropic.client.okhttp.AnthropicOkHttpClient;
  import com.anthropic.models.messages.*;

  public class VisionExample {
      public static void main(String[] args) throws IOException, InterruptedException {
          AnthropicClient client = AnthropicOkHttpClient.fromEnv();
          String imageData = ""; // // Base64-encoded image data as string

          List<ContentBlockParam> contentBlockParams = List.of(
                  ContentBlockParam.ofImage(
                          ImageBlockParam.builder()
                                  .source(Base64ImageSource.builder()
                                          .data(imageData)
                                          .build())
                                  .build()
                  ),
                  ContentBlockParam.ofText(TextBlockParam.builder()
                          .text("Describe this image.")
                          .build())
          );
          Message message = client.messages().create(
                  MessageCreateParams.builder()
                          .model(Model.CLAUDE_3_7_SONNET_LATEST)
                          .maxTokens(1024)
                          .addUserMessageOfBlockParams(contentBlockParams)
                          .build()
          );

          System.out.println(message);
      }
  }
```

### URL-based image example

```bash
  curl https://api.anthropic.com/v1/messages \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "content-type: application/json" \
    -d '{
      "model": "claude-sonnet-4-5",
      "max_tokens": 1024,
      "messages": [
        {
          "role": "user",
          "content": [
            {
              "type": "image",
              "source": {
                "type": "url",
                "url": "https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg"
              }
            },
            {
              "type": "text",
              "text": "Describe this image."
            }
          ]
        }
      ]
    }'
```
```Python
  import anthropic

  client = anthropic.Anthropic()
  message = client.messages.create(
      model="claude-sonnet-4-5",
      max_tokens=1024,
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "image",
                      "source": {
                          "type": "url",
                          "url": "https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg",
                      },
                  },
                  {
                      "type": "text",
                      "text": "Describe this image."
                  }
              ],
          }
      ],
  )
  print(message)
```
```TypeScript
  import Anthropic from '@anthropic-ai/sdk';

  const anthropic = new Anthropic({
    apiKey: process.env.ANTHROPIC_API_KEY,
  });

  async function main() {
    const message = await anthropic.messages.create({
      model: "claude-sonnet-4-5",
      max_tokens: 1024,
      messages: [
        {
          role: "user",
          content: [
            {
              type: "image",
              source: {
                type: "url",
                url: "https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg"
              }
            },
            {
              type: "text",
              text: "Describe this image."
            }
          ]
        }
      ]
    });
    
    console.log(message);
  }

  main();
```
```Java
  import java.io.IOException;
  import java.util.List;

  import com.anthropic.client.AnthropicClient;
  import com.anthropic.client.okhttp.AnthropicOkHttpClient;
  import com.anthropic.models.messages.*;

  public class VisionExample {

      public static void main(String[] args) throws IOException, InterruptedException {
          AnthropicClient client = AnthropicOkHttpClient.fromEnv();

          List<ContentBlockParam> contentBlockParams = List.of(
                  ContentBlockParam.ofImage(
                          ImageBlockParam.builder()
                                  .source(UrlImageSource.builder()
                                          .url("https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg")
                                          .build())
                                  .build()
                  ),
                  ContentBlockParam.ofText(TextBlockParam.builder()
                          .text("Describe this image.")
                          .build())
          );
          Message message = client.messages().create(
                  MessageCreateParams.builder()
                          .model(Model.CLAUDE_3_7_SONNET_LATEST)
                          .maxTokens(1024)
                          .addUserMessageOfBlockParams(contentBlockParams)
                          .build()
          );
          System.out.println(message);
      }
  }
```

### Files API image example

For images you'll use repeatedly or when you want to avoid encoding overhead, use the [Files API](/en/docs/build-with-claude/files):
```bash
  # First, upload your image to the Files API

  curl -X POST https://api.anthropic.com/v1/files \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: files-api-2025-04-14" \
    -F "file=@image.jpg"

  # Then use the returned file_id in your message

  curl https://api.anthropic.com/v1/messages \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: files-api-2025-04-14" \
    -H "content-type: application/json" \
    -d '{
      "model": "claude-sonnet-4-5",
      "max_tokens": 1024,
      "messages": [
        {
          "role": "user",
          "content": [
            {
              "type": "image",
              "source": {
                "type": "file",
                "file_id": "file_abc123"
              }
            },
            {
              "type": "text",
              "text": "Describe this image."
            }
          ]
        }
      ]
    }'
```
```python
  import anthropic

  client = anthropic.Anthropic()

  # Upload the image file

  with open("image.jpg", "rb") as f:
      file_upload = client.beta.files.upload(file=("image.jpg", f, "image/jpeg"))

  # Use the uploaded file in a message

  message = client.beta.messages.create(
      model="claude-sonnet-4-5",
      max_tokens=1024,
      betas=["files-api-2025-04-14"],
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "image",
                      "source": {
                          "type": "file",
                          "file_id": file_upload.id
                      }
                  },
                  {
                      "type": "text",
                      "text": "Describe this image."
                  }
              ]
          }
      ],
  )

  print(message.content)
```
```typescript
  import { Anthropic, toFile } from '@anthropic-ai/sdk';
  import fs from 'fs';

  const anthropic = new Anthropic();

  async function main() {
    // Upload the image file
    const fileUpload = await anthropic.beta.files.upload({
      file: toFile(fs.createReadStream('image.jpg'), undefined, { type: "image/jpeg" })
    }, {
      betas: ['files-api-2025-04-14']
    });

    // Use the uploaded file in a message
    const response = await anthropic.beta.messages.create({
      model: 'claude-sonnet-4-5',
      max_tokens: 1024,
      betas: ['files-api-2025-04-14'],
      messages: [
        {
          role: 'user',
          content: [
            {
              type: 'image',
              source: {
                type: 'file',
                file_id: fileUpload.id
              }
            },
            {
              type: 'text',
              text: 'Describe this image.'
            }
          ]
        }
      ]
    });

    console.log(response);
  }

  main();
```
```java
  import java.io.IOException;
  import java.nio.file.Files;
  import java.nio.file.Path;
  import java.util.List;

  import com.anthropic.client.AnthropicClient;
  import com.anthropic.client.okhttp.AnthropicOkHttpClient;
  import com.anthropic.models.File;
  import com.anthropic.models.files.FileUploadParams;
  import com.anthropic.models.messages.*;

  public class ImageFilesExample {
      public static void main(String[] args) throws IOException {
          AnthropicClient client = AnthropicOkHttpClient.fromEnv();

          // Upload the image file
          File file = client.beta().files().upload(FileUploadParams.builder()
                  .file(Files.newInputStream(Path.of("image.jpg")))
                  .build());

          // Use the uploaded file in a message
          ImageBlockParam imageParam = ImageBlockParam.builder()
                  .fileSource(file.id())
                  .build();

          MessageCreateParams params = MessageCreateParams.builder()
                  .model(Model.CLAUDE_3_7_SONNET_LATEST)
                  .maxTokens(1024)
                  .addUserMessageOfBlockParams(
                          List.of(
                                  ContentBlockParam.ofImage(imageParam),
                                  ContentBlockParam.ofText(
                                          TextBlockParam.builder()
                                                  .text("Describe this image.")
                                                  .build()
                                  )
                          )
                  )
                  .build();

          Message message = client.messages().create(params);
          System.out.println(message.content());
      }
  }
```

See [Messages API examples](/en/api/messages) for more example code and parameter details.

<AccordionGroup>
  <Accordion title="Example: One image">
    It’s best to place images earlier in the prompt than questions about them or instructions for tasks that use them.

    Ask Claude to describe one image.

    | Role | Content                       |
    | ---- | ----------------------------- |
    | User | \[Image] Describe this image. |

    Here is the corresponding API call using the Claude Sonnet 3.7 model.

    <Tabs>
      <Tab title="Using Base64">
```Python
        message = client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=1024,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "image",
                            "source": {
                                "type": "base64",
                                "media_type": image1_media_type,
                                "data": image1_data,
                            },
                        },
                        {
                            "type": "text",
                            "text": "Describe this image."
                        }
                    ],
                }
            ],
        )
```
      </Tab>

      <Tab title="Using URL">
```Python
        message = client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=1024,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "image",
                            "source": {
                                "type": "url",
                                "url": "https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg",
                            },
                        },
                        {
                            "type": "text",
                            "text": "Describe this image."
                        }
                    ],
                }
            ],
        )
```
      </Tab>
    </Tabs>
  </Accordion>

  <Accordion title="Example: Multiple images">
    In situations where there are multiple images, introduce each image with `Image 1:` and `Image 2:` and so on. You don’t need newlines between images or between images and the prompt.

    Ask Claude to describe the differences between multiple images.

    | Role | Content                                                                 |
    | ---- | ----------------------------------------------------------------------- |
    | User | Image 1: \[Image 1] Image 2: \[Image 2] How are these images different? |

    Here is the corresponding API call using the Claude Sonnet 3.7 model.

    <Tabs>
      <Tab title="Using Base64">
```Python
        message = client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=1024,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "Image 1:"
                        },
                        {
                            "type": "image",
                            "source": {
                                "type": "base64",
                                "media_type": image1_media_type,
                                "data": image1_data,
                            },
                        },
                        {
                            "type": "text",
                            "text": "Image 2:"
                        },
                        {
                            "type": "image",
                            "source": {
                                "type": "base64",
                                "media_type": image2_media_type,
                                "data": image2_data,
                            },
                        },
                        {
                            "type": "text",
                            "text": "How are these images different?"
                        }
                    ],
                }
            ],
        )
```
      </Tab>

      <Tab title="Using URL">
```Python
        message = client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=1024,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "Image 1:"
                        },
                        {
                            "type": "image",
                            "source": {
                                "type": "url",
                                "url": "https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg",
                            },
                        },
                        {
                            "type": "text",
                            "text": "Image 2:"
                        },
                        {
                            "type": "image",
                            "source": {
                                "type": "url",
                                "url": "https://upload.wikimedia.org/wikipedia/commons/b/b5/Iridescent.green.sweat.bee1.jpg",
                            },
                        },
                        {
                            "type": "text",
                            "text": "How are these images different?"
                        }
                    ],
                }
            ],
        )
```
      </Tab>
    </Tabs>
  </Accordion>

  <Accordion title="Example: Multiple images with a system prompt">
    Ask Claude to describe the differences between multiple images, while giving it a system prompt for how to respond.

    | Content |                                                                         |
    | ------- | ----------------------------------------------------------------------- |
    | System  | Respond only in Spanish.                                                |
    | User    | Image 1: \[Image 1] Image 2: \[Image 2] How are these images different? |

    Here is the corresponding API call using the Claude Sonnet 3.7 model.

    <Tabs>
      <Tab title="Using Base64">
```Python
        message = client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=1024,
            system="Respond only in Spanish.",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "Image 1:"
                        },
                        {
                            "type": "image",
                            "source": {
                                "type": "base64",
                                "media_type": image1_media_type,
                                "data": image1_data,
                            },
                        },
                        {
                            "type": "text",
                            "text": "Image 2:"
                        },
                        {
                            "type": "image",
                            "source": {
                                "type": "base64",
                                "media_type": image2_media_type,
                                "data": image2_data,
                            },
                        },
                        {
                            "type": "text",
                            "text": "How are these images different?"
                        }
                    ],
                }
            ],
        )
```
      </Tab>

      <Tab title="Using URL">
```Python
        message = client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=1024,
            system="Respond only in Spanish.",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "Image 1:"
                        },
                        {
                            "type": "image",
                            "source": {
                                "type": "url",
                                "url": "https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg",
                            },
                        },
                        {
                            "type": "text",
                            "text": "Image 2:"
                        },
                        {
                            "type": "image",
                            "source": {
                                "type": "url",
                                "url": "https://upload.wikimedia.org/wikipedia/commons/b/b5/Iridescent.green.sweat.bee1.jpg",
                            },
                        },
                        {
                            "type": "text",
                            "text": "How are these images different?"
                        }
                    ],
                }
            ],
        )
```
      </Tab>
    </Tabs>
  </Accordion>

  <Accordion title="Example: Four images across two conversation turns">
    Claude’s vision capabilities shine in multimodal conversations that mix images and text. You can have extended back-and-forth exchanges with Claude, adding new images or follow-up questions at any point. This enables powerful workflows for iterative image analysis, comparison, or combining visuals with other knowledge.

    Ask Claude to contrast two images, then ask a follow-up question comparing the first images to two new images.

    | Role      | Content                                                                            |
    | --------- | ---------------------------------------------------------------------------------- |
    | User      | Image 1: \[Image 1] Image 2: \[Image 2] How are these images different?            |
    | Assistant | \[Claude's response]                                                               |
    | User      | Image 1: \[Image 3] Image 2: \[Image 4] Are these images similar to the first two? |
    | Assistant | \[Claude's response]                                                               |

    When using the API, simply insert new images into the array of Messages in the `user` role as part of any standard [multiturn conversation](/en/api/messages) structure.
  </Accordion>
</AccordionGroup>

***

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
