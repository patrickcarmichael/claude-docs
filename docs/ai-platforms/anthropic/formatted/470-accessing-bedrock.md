---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Accessing Bedrock

### Subscribe to Anthropic models

Go to the [AWS Console > Bedrock > Model Access](https://console.aws.amazon.com/bedrock/home?region=us-west-2#/modelaccess) and request access to Anthropic models. Note that Anthropic model availability varies by region. See [AWS documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/models-regions.html) for latest information.

#### API model IDs

| Model                                                                            | Base Bedrock model ID                                        | `global` | `us` | `eu` | `jp` | `apac` |
| :------------------------------------------------------------------------------- | :----------------------------------------------------------- | :------- | :--- | :--- | :--- | :----- |
| Claude Sonnet 4.5                                                                | <ModelId>anthropic.claude-sonnet-4-5-20250929-v1:0</ModelId> | Yes      | Yes  | Yes  | Yes  | No     |
| Claude Sonnet 4                                                                  | <ModelId>anthropic.claude-sonnet-4-20250514-v1:0</ModelId>   | Yes      | Yes  | Yes  | No   | Yes    |
| Claude Sonnet 3.7 <Tooltip tip="Deprecated as of October 28, 2025.">⚠️</Tooltip> | <ModelId>anthropic.claude-3-7-sonnet-20250219-v1:0</ModelId> | No       | Yes  | Yes  | No   | Yes    |
| Claude Opus 4.1                                                                  | <ModelId>anthropic.claude-opus-4-1-20250805-v1:0</ModelId>   | No       | Yes  | No   | No   | No     |
| Claude Opus 4                                                                    | <ModelId>anthropic.claude-opus-4-20250514-v1:0</ModelId>     | No       | Yes  | No   | No   | No     |
| Claude Opus 3 <Tooltip tip="Deprecated as of June 30, 2025.">⚠️</Tooltip>        | <ModelId>anthropic.claude-3-opus-20240229-v1:0</ModelId>     | No       | Yes  | No   | No   | No     |
| Claude Haiku 4.5                                                                 | <ModelId>anthropic.claude-haiku-4-5-20251001-v1:0</ModelId>  | Yes      | Yes  | Yes  | No   | No     |
| Claude Haiku 3.5                                                                 | <ModelId>anthropic.claude-3-5-haiku-20241022-v1:0</ModelId>  | No       | Yes  | No   | No   | No     |
| Claude Haiku 3                                                                   | <ModelId>anthropic.claude-3-haiku-20240307-v1:0</ModelId>    | No       | Yes  | Yes  | No   | Yes    |

For more information about regional vs global model IDs, see the [Global vs regional endpoints](#global-vs-regional-endpoints) section below.

### List available models

The following examples show how to print a list of all the Claude models available through Bedrock:
```bash AWS CLI theme={null}
  aws bedrock list-foundation-models --region=us-west-2 --by-provider anthropic --query "modelSummaries[*].modelId"
```
```python Boto3 (Python) theme={null}
  import boto3

  bedrock = boto3.client(service_name="bedrock")
  response = bedrock.list_foundation_models(byProvider="anthropic")

  for summary in response["modelSummaries"]:
      print(summary["modelId"])
```

### Making requests

The following examples show how to generate text from Claude on Bedrock:
```Python
  from anthropic import AnthropicBedrock

  client = AnthropicBedrock(
      # Authenticate by either providing the keys below or use the default AWS credential providers, such as

      # using ~/.aws/credentials or the "AWS_SECRET_ACCESS_KEY" and "AWS_ACCESS_KEY_ID" environment variables.

      aws_access_key="<access key>",
      aws_secret_key="<secret key>",
      # Temporary credentials can be used with aws_session_token.

      # Read more at https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html.

      aws_session_token="<session_token>",
      # aws_region changes the aws region to which the request is made. By default, we read AWS_REGION,

      # and if that's not present, we default to us-east-1. Note that we do not read ~/.aws/config for the region.

      aws_region="us-west-2",
  )

  message = client.messages.create(
      model="global.anthropic.claude-sonnet-4-5-20250929-v1:0",
      max_tokens=256,
      messages=[{"role": "user", "content": "Hello, world"}]
  )
  print(message.content)
```
```TypeScript
  import AnthropicBedrock from '@anthropic-ai/bedrock-sdk';

  const client = new AnthropicBedrock({
    // Authenticate by either providing the keys below or use the default AWS credential providers, such as
    // using ~/.aws/credentials or the "AWS_SECRET_ACCESS_KEY" and "AWS_ACCESS_KEY_ID" environment variables.
    awsAccessKey: '<access key>',
    awsSecretKey: '<secret key>',

    // Temporary credentials can be used with awsSessionToken.
    // Read more at https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html.
    awsSessionToken: '<session_token>',

    // awsRegion changes the aws region to which the request is made. By default, we read AWS_REGION,
    // and if that's not present, we default to us-east-1. Note that we do not read ~/.aws/config for the region.
    awsRegion: 'us-west-2',
  });

  async function main() {
    const message = await client.messages.create({
      model: 'global.anthropic.claude-sonnet-4-5-20250929-v1:0',
      max_tokens: 256,
      messages: [{"role": "user", "content": "Hello, world"}]
    });
    console.log(message);
  }
  main().catch(console.error);
```
```python Boto3 (Python) theme={null}
  import boto3
  import json

  bedrock = boto3.client(service_name="bedrock-runtime")
  body = json.dumps({
    "max_tokens": 256,
    "messages": [{"role": "user", "content": "Hello, world"}],
    "anthropic_version": "bedrock-2023-05-31"
  })

  response = bedrock.invoke_model(body=body, modelId="global.anthropic.claude-sonnet-4-5-20250929-v1:0")

  response_body = json.loads(response.get("body").read())
  print(response_body.get("content"))
```

See our [client SDKs](/en/api/client-sdks) for more details, and the official Bedrock docs [here](https://docs.aws.amazon.com/bedrock/).

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
