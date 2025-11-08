---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Accessing Vertex AI

### Model Availability

Note that Anthropic model availability varies by region. Search for "Claude" in the [Vertex AI Model Garden](https://cloud.google.com/model-garden) or go to [Use Claude 3](https://cloud.google.com/vertex-ai/generative-ai/docs/partner-models/use-claude) for the latest information.

#### API model IDs

| Model                                                                            | Vertex AI API model ID                         |
| -------------------------------------------------------------------------------- | ---------------------------------------------- |
| Claude Sonnet 4.5                                                                | <ModelId>claude-sonnet-4-5\@20250929</ModelId> |
| Claude Sonnet 4                                                                  | <ModelId>claude-sonnet-4\@20250514</ModelId>   |
| Claude Sonnet 3.7 <Tooltip tip="Deprecated as of October 28, 2025.">⚠️</Tooltip> | <ModelId>claude-3-7-sonnet\@20250219</ModelId> |
| Claude Opus 4.1                                                                  | <ModelId>claude-opus-4-1\@20250805</ModelId>   |
| Claude Opus 4                                                                    | <ModelId>claude-opus-4\@20250514</ModelId>     |
| Claude Opus 3 <Tooltip tip="Deprecated as of June 30, 2025.">⚠️</Tooltip>        | <ModelId>claude-3-opus\@20240229</ModelId>     |
| Claude Haiku 4.5                                                                 | <ModelId>claude-haiku-4-5\@20251001</ModelId>  |
| Claude Haiku 3.5                                                                 | <ModelId>claude-3-5-haiku\@20241022</ModelId>  |
| Claude Haiku 3                                                                   | <ModelId>claude-3-haiku\@20240307</ModelId>    |

### Making requests

Before running requests you may need to run `gcloud auth application-default login` to authenticate with GCP.

The following examples shows how to generate text from Claude on Vertex AI:
```Python
  from anthropic import AnthropicVertex

  project_id = "MY_PROJECT_ID"
  region = "global"

  client = AnthropicVertex(project_id=project_id, region=region)

  message = client.messages.create(
      model="claude-sonnet-4-5@20250929",
      max_tokens=100,
      messages=[
          {
              "role": "user",
              "content": "Hey Claude!",
          }
      ],
  )
  print(message)
```
```TypeScript
  import { AnthropicVertex } from '@anthropic-ai/vertex-sdk';

  const projectId = 'MY_PROJECT_ID';
  const region = 'global';

  // Goes through the standard `google-auth-library` flow.
  const client = new AnthropicVertex({
    projectId,
    region,
  });

  async function main() {
    const result = await client.messages.create({
      model: 'claude-sonnet-4-5@20250929',
      max_tokens: 100,
      messages: [
        {
          role: 'user',
          content: 'Hey Claude!',
        },
      ],
    });
    console.log(JSON.stringify(result, null, 2));
  }

  main();
```
```bash
  MODEL_ID=claude-sonnet-4-5@20250929
  LOCATION=global
  PROJECT_ID=MY_PROJECT_ID

  curl \
  -X POST \
  -H "Authorization: Bearer $(gcloud auth print-access-token)" \
  -H "Content-Type: application/json" \
  https://$LOCATION-aiplatform.googleapis.com/v1/projects/${PROJECT_ID}/locations/${LOCATION}/publishers/anthropic/models/${MODEL_ID}:streamRawPredict -d \
  '{
    "anthropic_version": "vertex-2023-10-16",
    "messages": [{
      "role": "user",
      "content": "Hey Claude!"
    }],
    "max_tokens": 100,
  }'
```

See our [client SDKs](/en/api/client-sdks) and the official [Vertex AI docs](https://cloud.google.com/vertex-ai/docs) for more details.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
