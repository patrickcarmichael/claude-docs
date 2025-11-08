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
  title: Submit an embedding request
  version: endpoint_embeddings.createEmbeddings
paths:
  /embeddings:
    post:
      operationId: create-embeddings
      summary: Submit an embedding request
      description: Submits an embedding request to the embeddings router
      tags:
        - - subpackage_embeddings
      parameters:
        - name: Authorization
          in: header
          description: API key as bearer token in Authorization header
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Embedding response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Embeddings_createEmbeddings_Response_200'
        '400':
          description: Bad Request - Invalid request parameters or malformed input
          content: {}
        '401':
          description: Unauthorized - Authentication required or invalid credentials
          content: {}
        '402':
          description: Payment Required - Insufficient credits or quota to complete request
          content: {}
        '404':
          description: Not Found - Resource does not exist
          content: {}
        '429':
          description: Too Many Requests - Rate limit exceeded
          content: {}
        '500':
          description: Internal Server Error - Unexpected server error
          content: {}
        '502':
          description: Bad Gateway - Provider/upstream API failure
          content: {}
        '503':
          description: Service Unavailable - Service temporarily unavailable
          content: {}
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                input:
                  $ref: >-
                    #/components/schemas/EmbeddingsPostRequestBodyContentApplicationJsonSchemaInput
                model:
                  type: string
                provider:
                  $ref: >-
                    #/components/schemas/EmbeddingsPostRequestBodyContentApplicationJsonSchemaProvider
                encoding_format:
                  $ref: >-
                    #/components/schemas/EmbeddingsPostRequestBodyContentApplicationJsonSchemaEncodingFormat
                user:
                  type: string
              required:
                - input
                - model
components:
  schemas:
    EmbeddingsPostRequestBodyContentApplicationJsonSchemaInput:
      oneOf:
        - type: string
        - type: array
          items:
            type: string
        - type: array
          items:
            type: number
            format: double
        - type: array
          items:
            type: array
            items:
              type: number
              format: double
    EmbeddingsPostRequestBodyContentApplicationJsonSchemaProviderDataCollection:
      type: string
      enum:
        - value: deny
        - value: allow
    ProviderName:
      type: string
      enum:
        - value: AnyScale
        - value: Cent-ML
        - value: HuggingFace
        - value: Hyperbolic 2
        - value: Lepton
        - value: Lynn 2
        - value: Lynn
        - value: Mancer
        - value: Modal
        - value: OctoAI
        - value: Recursal
        - value: Reflection
        - value: Replicate
        - value: SambaNova 2
        - value: SF Compute
        - value: Together 2
        - value: 01.AI
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
        - value: InoCloud
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
    EmbeddingsPostRequestBodyContentApplicationJsonSchemaProviderOrderItems:
      oneOf:
        - $ref: '#/components/schemas/ProviderName'
        - type: string
    EmbeddingsPostRequestBodyContentApplicationJsonSchemaProviderOnlyItems:
      oneOf:
        - $ref: '#/components/schemas/ProviderName'
        - type: string
    EmbeddingsPostRequestBodyContentApplicationJsonSchemaProviderIgnoreItems:
      oneOf:
        - $ref: '#/components/schemas/ProviderName'
        - type: string
    Quantization:
      type: string
      enum:
        - value: int4
        - value: int8
        - value: fp4
        - value: fp6
        - value: fp8
        - value: fp16
        - value: bf16
        - value: fp32
        - value: unknown
    EmbeddingsPostRequestBodyContentApplicationJsonSchemaProviderSort:
      type: string
      enum:
        - value: price
        - value: throughput
        - value: latency
    BigNumberUnion:
      oneOf:
        - type: number
          format: double
        - type: string
        - type: number
          format: double
    EmbeddingsPostRequestBodyContentApplicationJsonSchemaProviderMaxPrice:
      type: object
      properties:
        prompt:
          $ref: '#/components/schemas/BigNumberUnion'
        completion:
          $ref: '#/components/schemas/BigNumberUnion'
        image:
          $ref: '#/components/schemas/BigNumberUnion'
        audio:
          $ref: '#/components/schemas/BigNumberUnion'
        request:
          $ref: '#/components/schemas/BigNumberUnion'
    EmbeddingsPostRequestBodyContentApplicationJsonSchemaProvider:
      type: object
      properties:
        allow_fallbacks:
          type:
            - boolean
            - 'null'
        require_parameters:
          type:
            - boolean
            - 'null'
        data_collection:
          oneOf:
            - $ref: >-
                #/components/schemas/EmbeddingsPostRequestBodyContentApplicationJsonSchemaProviderDataCollection
            - type: 'null'
        zdr:
          type:
            - boolean
            - 'null'
        enforce_distillable_text:
          type:
            - boolean
            - 'null'
        order:
          type:
            - array
            - 'null'
          items:
            $ref: >-
              #/components/schemas/EmbeddingsPostRequestBodyContentApplicationJsonSchemaProviderOrderItems
        only:
          type:
            - array
            - 'null'
          items:
            $ref: >-
              #/components/schemas/EmbeddingsPostRequestBodyContentApplicationJsonSchemaProviderOnlyItems
        ignore:
          type:
            - array
            - 'null'
          items:
            $ref: >-
              #/components/schemas/EmbeddingsPostRequestBodyContentApplicationJsonSchemaProviderIgnoreItems
        quantizations:
          type:
            - array
            - 'null'
          items:
            $ref: '#/components/schemas/Quantization'
        sort:
          oneOf:
            - $ref: >-
                #/components/schemas/EmbeddingsPostRequestBodyContentApplicationJsonSchemaProviderSort
            - type: 'null'
        max_price:
          $ref: >-
            #/components/schemas/EmbeddingsPostRequestBodyContentApplicationJsonSchemaProviderMaxPrice
    EmbeddingsPostRequestBodyContentApplicationJsonSchemaEncodingFormat0:
      type: string
      enum:
        - value: float
    EmbeddingsPostRequestBodyContentApplicationJsonSchemaEncodingFormat1:
      type: string
      enum:
        - value: base64
    EmbeddingsPostRequestBodyContentApplicationJsonSchemaEncodingFormat:
      oneOf:
        - $ref: >-
            #/components/schemas/EmbeddingsPostRequestBodyContentApplicationJsonSchemaEncodingFormat0
        - $ref: >-
            #/components/schemas/EmbeddingsPostRequestBodyContentApplicationJsonSchemaEncodingFormat1
    EmbeddingsPostResponsesContentApplicationJsonSchemaObject:
      type: string
      enum:
        - value: list
    EmbeddingsPostResponsesContentApplicationJsonSchemaDataItemsObject:
      type: string
      enum:
        - value: embedding
    EmbeddingsPostResponsesContentApplicationJsonSchemaDataItemsEmbedding:
      oneOf:
        - type: array
          items:
            type: number
            format: double
        - type: string
    EmbeddingsPostResponsesContentApplicationJsonSchemaDataItems:
      type: object
      properties:
        object:
          $ref: >-
            #/components/schemas/EmbeddingsPostResponsesContentApplicationJsonSchemaDataItemsObject
        embedding:
          $ref: >-
            #/components/schemas/EmbeddingsPostResponsesContentApplicationJsonSchemaDataItemsEmbedding
        index:
          type: number
          format: double
      required:
        - object
        - embedding
    EmbeddingsPostResponsesContentApplicationJsonSchemaUsage:
      type: object
      properties:
        prompt_tokens:
          type: number
          format: double
        total_tokens:
          type: number
          format: double
        cost:
          type: number
          format: double
      required:
        - prompt_tokens
        - total_tokens
    Embeddings_createEmbeddings_Response_200:
      type: object
      properties:
        id:
          type: string
        object:
          $ref: >-
            #/components/schemas/EmbeddingsPostResponsesContentApplicationJsonSchemaObject
        data:
          type: array
          items:
            $ref: >-
              #/components/schemas/EmbeddingsPostResponsesContentApplicationJsonSchemaDataItems
        model:
          type: string
        usage:
          $ref: >-
            #/components/schemas/EmbeddingsPostResponsesContentApplicationJsonSchemaUsage
      required:
        - object
        - data
        - model
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
