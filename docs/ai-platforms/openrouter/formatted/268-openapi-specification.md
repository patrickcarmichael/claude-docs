---
title: "OpenRouter Documentation"
description: "Formatted documentation for OpenRouter"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Get a model's supported parameters and data about which are most popular
  version: endpoint_parameters.getParameters
paths:
  /parameters/{author}/{slug}:
    get:
      operationId: get-parameters
      summary: Get a model's supported parameters and data about which are most popular
      tags:
        - - subpackage_parameters
      parameters:
        - name: author
          in: path
          required: true
          schema:
            type: string
        - name: slug
          in: path
          required: true
          schema:
            type: string
        - name: provider
          in: query
          required: false
          schema:
            $ref: '#/components/schemas/ParametersAuthorSlugGetParametersProvider'
        - name: Authorization
          in: header
          description: API key as bearer token in Authorization header
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Returns the parameters for the specified model
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Parameters_getParameters_Response_200'
        '401':
          description: Unauthorized - Authentication required or invalid credentials
          content: {}
        '404':
          description: Not Found - Model or provider does not exist
          content: {}
        '500':
          description: Internal Server Error - Unexpected server error
          content: {}
components:
  schemas:
    ParametersAuthorSlugGetParametersProvider:
      type: string
      enum:
        - value: AI21
        - value: AionLabs
        - value: Alibaba
        - value: Amazon Bedrock
        - value: Anthropic
        - value: AtlasCloud
        - value: Atoma
        - value: Avian
        - value: Azure
        - value: BaseTen
        - value: Cerebras
        - value: Chutes
        - value: Cirrascale
        - value: Clarifai
        - value: Cloudflare
        - value: Cohere
        - value: CrofAI
        - value: Crusoe
        - value: DeepInfra
        - value: DeepSeek
        - value: Enfer
        - value: Featherless
        - value: Fireworks
        - value: Friendli
        - value: GMICloud
        - value: Google
        - value: Google AI Studio
        - value: Groq
        - value: Hyperbolic
        - value: Inception
        - value: InferenceNet
        - value: Infermatic
        - value: Inflection
        - value: Kluster
        - value: Lambda
        - value: Liquid
        - value: Mancer 2
        - value: Meta
        - value: Minimax
        - value: ModelRun
        - value: Mistral
        - value: Modular
        - value: Moonshot AI
        - value: Morph
        - value: NCompass
        - value: Nebius
        - value: NextBit
        - value: Nineteen
        - value: Novita
        - value: Nvidia
        - value: OpenAI
        - value: OpenInference
        - value: Parasail
        - value: Perplexity
        - value: Phala
        - value: Relace
        - value: SambaNova
        - value: SiliconFlow
        - value: Stealth
        - value: Switchpoint
        - value: Targon
        - value: Together
        - value: Ubicloud
        - value: Venice
        - value: WandB
        - value: xAI
        - value: Z.AI
        - value: FakeProvider
    ParametersAuthorSlugGetResponsesContentApplicationJsonSchemaDataSupportedParametersItems:
      type: string
      enum:
        - value: temperature
        - value: top_p
        - value: top_k
        - value: min_p
        - value: top_a
        - value: frequency_penalty
        - value: presence_penalty
        - value: repetition_penalty
        - value: max_tokens
        - value: logit_bias
        - value: logprobs
        - value: top_logprobs
        - value: seed
        - value: response_format
        - value: structured_outputs
        - value: stop
        - value: tools
        - value: tool_choice
        - value: parallel_tool_calls
        - value: include_reasoning
        - value: reasoning
        - value: web_search_options
        - value: verbosity
    ParametersAuthorSlugGetResponsesContentApplicationJsonSchemaData:
      type: object
      properties:
        model:
          type: string
        supported_parameters:
          type: array
          items:
            $ref: >-
              #/components/schemas/ParametersAuthorSlugGetResponsesContentApplicationJsonSchemaDataSupportedParametersItems
      required:
        - model
        - supported_parameters
    Parameters_getParameters_Response_200:
      type: object
      properties:
        data:
          $ref: >-
            #/components/schemas/ParametersAuthorSlugGetResponsesContentApplicationJsonSchemaData
      required:
        - data
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
