**Navigation:** [← Previous](./24-list-collections.md) | [Index](./index.md) | [Next →](./26-delete-all-locally-tracked-managed-keys-cli-create.md)

# List available models
Source: https://docs.pinecone.io/reference/api/2025-04/inference/list_models

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-04/inference_2025-04.oas.yaml get /models
List the embedding and reranking models hosted by Pinecone. 

You can use hosted models as an integrated part of Pinecone operations or for standalone embedding and reranking. For more details, see [Vector embedding](https://docs.pinecone.io/guides/index-data/indexing-overview#vector-embedding) and [Rerank results](https://docs.pinecone.io/guides/search/rerank-results).

<RequestExample>
  ```python Python theme={null}
  from pinecone import Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  models = pc.inference.list_models()

  print(models)
  ```

  ```javascript JavaScript theme={null}
  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  const models = await pc.inference.listModels();

  console.log(models);
  ```

  ```java Java  theme={null}
  import io.pinecone.clients.Inference;
  import io.pinecone.clients.Pinecone;
  import org.openapitools.inference.client.ApiException;
  import org.openapitools.inference.client.model.ModelInfo;
  import org.openapitools.inference.client.model.ModelInfoList;

  public class ListModels {
      public static void main(String[] args) throws ApiException {
          Pinecone pinecone = new Pinecone.Builder("YOUR_API_KEY").build();

          Inference inference = pinecone.getInferenceClient();

          // List all models
          ModelInfoList models = inference.listModels();
          System.out.println(models);

          // List by model type ("embed" or "rerank")
          ModelInfoList modelsByModelType = inference.listModels("rerank");
          System.out.println(modelsByModelType);

          // List by model type ("embed" or "rerank") and vector type ("dense" or "sparse")
          ModelInfoList modelsByModelTypeAndVectorType = inference.listModels("embed", "dense");
          System.out.println(modelsByModelTypeAndVectorType);
      }
  }
  ```

  ```go Go theme={null}
  package main

  import (
      "context"
      "encoding/json"
      "fmt"
      "log"

      "github.com/pinecone-io/go-pinecone/v4/pinecone"
  )

  func prettifyStruct(obj interface{}) string {
    	bytes, _ := json.MarshalIndent(obj, "", "  ")
      return string(bytes)
  }

  func main() {
      ctx := context.Background()

      pc, err := pinecone.NewClient(pinecone.NewClientParams{
          ApiKey: "YOUR_API_KEY",
      })
      if err != nil {
          log.Fatalf("Failed to create Client: %v", err)
      }

      embed := "embed"
      rerank := "rerank"

      embedModels, err := pc.Inference.ListModels(ctx, &pinecone.ListModelsParams{
          Type: &embed,
      })
      if err != nil {
          log.Fatalf("Failed to list embedding models: %v", err)
      }
      fmt.Printf(prettifyStruct(embedModels))

      rerankModels, err := pc.Inference.ListModels(ctx, &pinecone.ListModelsParams{
          Type: &rerank,
      })
      if err != nil {
          log.Fatalf("Failed to list reranking models: %v", err)
      }
      fmt.Printf(prettifyStruct(rerankModels))
  }
  ```

  ```csharp C# theme={null}
  using Pinecone;
  using Pinecone.Inference;

  var pinecone = new PineconeClient("YOUR_API_KEY");

  var models = await pinecone.Inference.Models.ListAsync(new ListModelsRequest());

  Console.WriteLine(models);
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl "https://api.pinecone.io/models" \
      -H "Api-Key: $PINECONE_API_KEY" \
      -H "X-Pinecone-API-Version: 2025-04"
  ```
</RequestExample>

<ResponseExample>
  ```python Python theme={null}
  [{
      "model": "llama-text-embed-v2",
      "short_description": "A high performance dense embedding model optimized for multilingual and cross-lingual text question-answering retrieval with support for long documents (up to 2048 tokens) and dynamic embedding size (Matryoshka Embeddings).",
      "type": "embed",
      "supported_parameters": [
          {
              "parameter": "input_type",
              "type": "one_of",
              "value_type": "string",
              "required": true,
              "allowed_values": [
                  "query",
                  "passage"
              ]
          },
          {
              "parameter": "truncate",
              "type": "one_of",
              "value_type": "string",
              "required": false,
              "default": "END",
              "allowed_values": [
                  "END",
                  "NONE",
                  "START"
              ]
          },
          {
              "parameter": "dimension",
              "type": "one_of",
              "value_type": "integer",
              "required": false,
              "default": 1024,
              "allowed_values": [
                  384,
                  512,
                  768,
                  1024,
                  2048
              ]
          }
      ],
      "vector_type": "dense",
      "default_dimension": 1024,
      "modality": "text",
      "max_sequence_length": 2048,
      "max_batch_size": 96,
      "provider_name": "NVIDIA",
      "supported_metrics": [
          "cosine",
          "dotproduct"
      ],
      "supported_dimensions": [
          384,
          512,
          768,
          1024,
          2048
      ]
  }, {
      "model": "multilingual-e5-large",
      "short_description": "A high-performance dense embedding model trained on a mixture of multilingual datasets. It works well on messy data and short queries expected to return medium-length passages of text (1-2 paragraphs)",
      "type": "embed",
      "supported_parameters": [
          {
              "parameter": "input_type",
              "type": "one_of",
              "value_type": "string",
              "required": true,
              "allowed_values": [
                  "query",
                  "passage"
              ]
          },
          {
              "parameter": "truncate",
              "type": "one_of",
              "value_type": "string",
              "required": false,
              "default": "END",
              "allowed_values": [
                  "END",
                  "NONE"
              ]
          }
      ],
      "vector_type": "dense",
      "default_dimension": 1024,
      "modality": "text",
      "max_sequence_length": 507,
      "max_batch_size": 96,
      "provider_name": "Microsoft",
      "supported_metrics": [
          "cosine",
          "euclidean"
      ],
      "supported_dimensions": [
          1024
      ]
  }, {
      "model": "pinecone-sparse-english-v0",
      "short_description": "A sparse embedding model for converting text to sparse vectors for keyword or hybrid semantic/keyword search. Built on the innovations of the DeepImpact architecture.",
      "type": "embed",
      "supported_parameters": [
          {
              "parameter": "input_type",
              "type": "one_of",
              "value_type": "string",
              "required": true,
              "allowed_values": [
                  "query",
                  "passage"
              ]
          },
          {
              "parameter": "truncate",
              "type": "one_of",
              "value_type": "string",
              "required": false,
              "default": "END",
              "allowed_values": [
                  "END",
                  "NONE"
              ]
          },
          {
              "parameter": "return_tokens",
              "type": "any",
              "value_type": "boolean",
              "required": false,
              "default": false
          }
      ],
      "vector_type": "sparse",
      "modality": "text",
      "max_sequence_length": 512,
      "max_batch_size": 96,
      "provider_name": "Pinecone",
      "supported_metrics": [
          "dotproduct"
      ]
  }, {
      "model": "bge-reranker-v2-m3",
      "short_description": "A high-performance, multilingual reranking model that works well on messy data and short queries expected to return medium-length passages of text (1-2 paragraphs)",
      "type": "rerank",
      "supported_parameters": [
          {
              "parameter": "truncate",
              "type": "one_of",
              "value_type": "string",
              "required": false,
              "default": "NONE",
              "allowed_values": [
                  "END",
                  "NONE"
              ]
          }
      ],
      "modality": "text",
      "max_sequence_length": 1024,
      "max_batch_size": 100,
      "provider_name": "BAAI",
      "supported_metrics": []
  }, {
      "model": "cohere-rerank-3.5",
      "short_description": "Cohere's leading reranking model, balancing performance and latency for a wide range of enterprise search applications.",
      "type": "rerank",
      "supported_parameters": [
          {
              "parameter": "max_chunks_per_doc",
              "type": "numeric_range",
              "value_type": "integer",
              "required": false,
              "default": 3072,
              "min": 1.0,
              "max": 3072.0
          }
      ],
      "modality": "text",
      "max_sequence_length": 40000,
      "max_batch_size": 200,
      "provider_name": "Cohere",
      "supported_metrics": []
  }, {
      "model": "pinecone-rerank-v0",
      "short_description": "A state of the art reranking model that out-performs competitors on widely accepted benchmarks. It can handle chunks up to 512 tokens (1-2 paragraphs)",
      "type": "rerank",
      "supported_parameters": [
          {
              "parameter": "truncate",
              "type": "one_of",
              "value_type": "string",
              "required": false,
              "default": "END",
              "allowed_values": [
                  "END",
                  "NONE"
              ]
          }
      ],
      "modality": "text",
      "max_sequence_length": 512,
      "max_batch_size": 100,
      "provider_name": "Pinecone",
      "supported_metrics": []
  }]
  ```

  ```javascript JavaScript theme={null}
  {
    models: [
      {
        model: 'llama-text-embed-v2',
        shortDescription: 'A high performance dense embedding model optimized for multilingual and cross-lingual text question-answering retrieval with support for long documents (up to 2048 tokens) and dynamic embedding size (Matryoshka Embeddings).',
        type: 'embed',
        vectorType: 'dense',
        defaultDimension: 1024,
        modality: 'text',
        maxSequenceLength: 2048,
        maxBatchSize: 96,
        providerName: 'NVIDIA',
        supportedDimensions: [Array],
        supportedMetrics: [Array],
        supportedParameters: [Array]
      },
      {
        model: 'multilingual-e5-large',
        shortDescription: 'A high-performance dense embedding model trained on a mixture of multilingual datasets. It works well on messy data and short queries expected to return medium-length passages of text (1-2 paragraphs)',
        type: 'embed',
        vectorType: 'dense',
        defaultDimension: 1024,
        modality: 'text',
        maxSequenceLength: 507,
        maxBatchSize: 96,
        providerName: 'Microsoft',
        supportedDimensions: [Array],
        supportedMetrics: [Array],
        supportedParameters: [Array]
      },
      {
        model: 'pinecone-sparse-english-v0',
        shortDescription: 'A sparse embedding model for converting text to sparse vectors for keyword or hybrid semantic/keyword search. Built on the innovations of the DeepImpact architecture.',
        type: 'embed',
        vectorType: 'sparse',
        defaultDimension: undefined,
        modality: 'text',
        maxSequenceLength: 512,
        maxBatchSize: 96,
        providerName: 'Pinecone',
        supportedDimensions: undefined,
        supportedMetrics: [Array],
        supportedParameters: [Array]
      },
      {
        model: 'bge-reranker-v2-m3',
        shortDescription: 'A high-performance, multilingual reranking model that works well on messy data and short queries expected to return medium-length passages of text (1-2 paragraphs)',
        type: 'rerank',
        vectorType: undefined,
        defaultDimension: undefined,
        modality: 'text',
        maxSequenceLength: 1024,
        maxBatchSize: 100,
        providerName: 'BAAI',
        supportedDimensions: undefined,
        supportedMetrics: undefined,
        supportedParameters: [Array]
      },
      {
        model: 'cohere-rerank-3.5',
        shortDescription: "Cohere's leading reranking model, balancing performance and latency for a wide range of enterprise search applications.",
        type: 'rerank',
        vectorType: undefined,
        defaultDimension: undefined,
        modality: 'text',
        maxSequenceLength: 40000,
        maxBatchSize: 200,
        providerName: 'Cohere',
        supportedDimensions: undefined,
        supportedMetrics: undefined,
        supportedParameters: [Array]
      },
      {
        model: 'pinecone-rerank-v0',
        shortDescription: 'A state of the art reranking model that out-performs competitors on widely accepted benchmarks. It can handle chunks up to 512 tokens (1-2 paragraphs)',
        type: 'rerank',
        vectorType: undefined,
        defaultDimension: undefined,
        modality: 'text',
        maxSequenceLength: 512,
        maxBatchSize: 100,
        providerName: 'Pinecone',
        supportedDimensions: undefined,
        supportedMetrics: undefined,
        supportedParameters: [Array]
      }
    ]
  }
  ```

  ```java Java theme={null}
  class ModelInfoList {
      models: [class ModelInfo {
          model: llama-text-embed-v2
          shortDescription: A high performance dense embedding model optimized for multilingual and cross-lingual text question-answering retrieval with support for long documents (up to 2048 tokens) and dynamic embedding size (Matryoshka Embeddings).
          type: embed
          vectorType: dense
          defaultDimension: 1024
          modality: text
          maxSequenceLength: 2048
          maxBatchSize: 96
          providerName: NVIDIA
          supportedDimensions: [384, 512, 768, 1024, 2048]
          supportedMetrics: [cosine, dotproduct]
          supportedParameters: [class ModelInfoSupportedParameter {
              parameter: input_type
              type: one_of
              valueType: string
              required: true
              allowedValues: [class class org.openapitools.inference.client.model.ModelInfoSupportedParameterAllowedValuesInner {
                  instance: query
                  isNullable: false
                  schemaType: anyOf
              }, class class org.openapitools.inference.client.model.ModelInfoSupportedParameterAllowedValuesInner {
                  instance: passage
                  isNullable: false
                  schemaType: anyOf
              }]
              min: null
              max: null
              _default: null
              additionalProperties: null
          }, class ModelInfoSupportedParameter {
              parameter: truncate
              type: one_of
              valueType: string
              required: false
              allowedValues: [class class org.openapitools.inference.client.model.ModelInfoSupportedParameterAllowedValuesInner {
                  instance: END
                  isNullable: false
                  schemaType: anyOf
              }, class class org.openapitools.inference.client.model.ModelInfoSupportedParameterAllowedValuesInner {
                  instance: NONE
                  isNullable: false
                  schemaType: anyOf
              }, class class org.openapitools.inference.client.model.ModelInfoSupportedParameterAllowedValuesInner {
                  instance: START
                  isNullable: false
                  schemaType: anyOf
              }]
              min: null
              max: null
              _default: class class org.openapitools.inference.client.model.ModelInfoSupportedParameterDefault {
                  instance: END
                  isNullable: false
                  schemaType: anyOf
              }
              additionalProperties: null
          }, class ModelInfoSupportedParameter {
              parameter: dimension
              type: one_of
              valueType: integer
              required: false
              allowedValues: [class class org.openapitools.inference.client.model.ModelInfoSupportedParameterAllowedValuesInner {
                  instance: 384
                  isNullable: false
                  schemaType: anyOf
              }, class class org.openapitools.inference.client.model.ModelInfoSupportedParameterAllowedValuesInner {
                  instance: 512
                  isNullable: false
                  schemaType: anyOf
              }, class class org.openapitools.inference.client.model.ModelInfoSupportedParameterAllowedValuesInner {
                  instance: 768
                  isNullable: false
                  schemaType: anyOf
              }, class class org.openapitools.inference.client.model.ModelInfoSupportedParameterAllowedValuesInner {
                  instance: 1024
                  isNullable: false
                  schemaType: anyOf
              }, class class org.openapitools.inference.client.model.ModelInfoSupportedParameterAllowedValuesInner {
                  instance: 2048
                  isNullable: false
                  schemaType: anyOf
              }]
              min: null
              max: null
              _default: class class org.openapitools.inference.client.model.ModelInfoSupportedParameterDefault {
                  instance: 1024
                  isNullable: false
                  schemaType: anyOf
              }
              additionalProperties: null
          }]
          additionalProperties: null
      }, class ModelInfo {
          model: multilingual-e5-large
          shortDescription: A high-performance dense embedding model trained on a mixture of multilingual datasets. It works well on messy data and short queries expected to return medium-length passages of text (1-2 paragraphs)
          type: embed
          vectorType: dense
          defaultDimension: 1024
          modality: text
          maxSequenceLength: 507
          maxBatchSize: 96
          providerName: Microsoft
          supportedDimensions: [1024]
          supportedMetrics: [cosine, euclidean]
          supportedParameters: [class ModelInfoSupportedParameter {
              parameter: input_type
              type: one_of
              valueType: string
              required: true
              allowedValues: [class class org.openapitools.inference.client.model.ModelInfoSupportedParameterAllowedValuesInner {
                  instance: query
                  isNullable: false
                  schemaType: anyOf
              }, class class org.openapitools.inference.client.model.ModelInfoSupportedParameterAllowedValuesInner {
                  instance: passage
                  isNullable: false
                  schemaType: anyOf
              }]
              min: null
              max: null
              _default: null
              additionalProperties: null
          }, class ModelInfoSupportedParameter {
              parameter: truncate
              type: one_of
              valueType: string
              required: false
              allowedValues: [class class org.openapitools.inference.client.model.ModelInfoSupportedParameterAllowedValuesInner {
                  instance: END
                  isNullable: false
                  schemaType: anyOf
              }, class class org.openapitools.inference.client.model.ModelInfoSupportedParameterAllowedValuesInner {
                  instance: NONE
                  isNullable: false
                  schemaType: anyOf
              }]
              min: null
              max: null
              _default: class class org.openapitools.inference.client.model.ModelInfoSupportedParameterDefault {
                  instance: END
                  isNullable: false
                  schemaType: anyOf
              }
              additionalProperties: null
          }]
          additionalProperties: null
      }, class ModelInfo {
          model: pinecone-sparse-english-v0
          shortDescription: A sparse embedding model for converting text to sparse vectors for keyword or hybrid semantic/keyword search. Built on the innovations of the DeepImpact architecture.
          type: embed
          vectorType: sparse
          defaultDimension: null
          modality: text
          maxSequenceLength: 512
          maxBatchSize: 96
          providerName: Pinecone
          supportedDimensions: null
          supportedMetrics: [dotproduct]
          supportedParameters: [class ModelInfoSupportedParameter {
              parameter: input_type
              type: one_of
              valueType: string
              required: true
              allowedValues: [class class org.openapitools.inference.client.model.ModelInfoSupportedParameterAllowedValuesInner {
                  instance: query
                  isNullable: false
                  schemaType: anyOf
              }, class class org.openapitools.inference.client.model.ModelInfoSupportedParameterAllowedValuesInner {
                  instance: passage
                  isNullable: false
                  schemaType: anyOf
              }]
              min: null
              max: null
              _default: null
              additionalProperties: null
          }, class ModelInfoSupportedParameter {
              parameter: truncate
              type: one_of
              valueType: string
              required: false
              allowedValues: [class class org.openapitools.inference.client.model.ModelInfoSupportedParameterAllowedValuesInner {
                  instance: END
                  isNullable: false
                  schemaType: anyOf
              }, class class org.openapitools.inference.client.model.ModelInfoSupportedParameterAllowedValuesInner {
                  instance: NONE
                  isNullable: false
                  schemaType: anyOf
              }]
              min: null
              max: null
              _default: class class org.openapitools.inference.client.model.ModelInfoSupportedParameterDefault {
                  instance: END
                  isNullable: false
                  schemaType: anyOf
              }
              additionalProperties: null
          }, class ModelInfoSupportedParameter {
              parameter: return_tokens
              type: any
              valueType: boolean
              required: false
              allowedValues: null
              min: null
              max: null
              _default: class class org.openapitools.inference.client.model.ModelInfoSupportedParameterDefault {
                  instance: false
                  isNullable: false
                  schemaType: anyOf
              }
              additionalProperties: null
          }, class ModelInfoSupportedParameter {
              parameter: max_tokens_per_sequence
              type: one_of
              valueType: integer
              required: false
              allowedValues: [class class org.openapitools.inference.client.model.ModelInfoSupportedParameterAllowedValuesInner {
                  instance: 512
                  isNullable: false
                  schemaType: anyOf
              }, class class org.openapitools.inference.client.model.ModelInfoSupportedParameterAllowedValuesInner {
                  instance: 2048
                  isNullable: false
                  schemaType: anyOf
              }]
              min: null
              max: null
              _default: class class org.openapitools.inference.client.model.ModelInfoSupportedParameterDefault {
                  instance: 512
                  isNullable: false
                  schemaType: anyOf
              }
              additionalProperties: null
          }]
          additionalProperties: null
      }, class ModelInfo {
          model: bge-reranker-v2-m3
          shortDescription: A high-performance, multilingual reranking model that works well on messy data and short queries expected to return medium-length passages of text (1-2 paragraphs)
          type: rerank
          vectorType: null
          defaultDimension: null
          modality: text
          maxSequenceLength: 1024
          maxBatchSize: 100
          providerName: BAAI
          supportedDimensions: null
          supportedMetrics: null
          supportedParameters: [class ModelInfoSupportedParameter {
              parameter: truncate
              type: one_of
              valueType: string
              required: false
              allowedValues: [class class org.openapitools.inference.client.model.ModelInfoSupportedParameterAllowedValuesInner {
                  instance: END
                  isNullable: false
                  schemaType: anyOf
              }, class class org.openapitools.inference.client.model.ModelInfoSupportedParameterAllowedValuesInner {
                  instance: NONE
                  isNullable: false
                  schemaType: anyOf
              }]
              min: null
              max: null
              _default: class class org.openapitools.inference.client.model.ModelInfoSupportedParameterDefault {
                  instance: NONE
                  isNullable: false
                  schemaType: anyOf
              }
              additionalProperties: null
          }]
          additionalProperties: null
      }, class ModelInfo {
          model: cohere-rerank-3.5
          shortDescription: Cohere's leading reranking model, balancing performance and latency for a wide range of enterprise search applications.
          type: rerank
          vectorType: null
          defaultDimension: null
          modality: text
          maxSequenceLength: 40000
          maxBatchSize: 200
          providerName: Cohere
          supportedDimensions: null
          supportedMetrics: null
          supportedParameters: [class ModelInfoSupportedParameter {
              parameter: max_chunks_per_doc
              type: numeric_range
              valueType: integer
              required: false
              allowedValues: null
              min: 1
              max: 3072
              _default: class class org.openapitools.inference.client.model.ModelInfoSupportedParameterDefault {
                  instance: 3072
                  isNullable: false
                  schemaType: anyOf
              }
              additionalProperties: null
          }]
          additionalProperties: null
      }, class ModelInfo {
          model: pinecone-rerank-v0
          shortDescription: A state of the art reranking model that out-performs competitors on widely accepted benchmarks. It can handle chunks up to 512 tokens (1-2 paragraphs)
          type: rerank
          vectorType: null
          defaultDimension: null
          modality: text
          maxSequenceLength: 512
          maxBatchSize: 100
          providerName: Pinecone
          supportedDimensions: null
          supportedMetrics: null
          supportedParameters: [class ModelInfoSupportedParameter {
              parameter: truncate
              type: one_of
              valueType: string
              required: false
              allowedValues: [class class org.openapitools.inference.client.model.ModelInfoSupportedParameterAllowedValuesInner {
                  instance: END
                  isNullable: false
                  schemaType: anyOf
              }, class class org.openapitools.inference.client.model.ModelInfoSupportedParameterAllowedValuesInner {
                  instance: NONE
                  isNullable: false
                  schemaType: anyOf
              }]
              min: null
              max: null
              _default: class class org.openapitools.inference.client.model.ModelInfoSupportedParameterDefault {
                  instance: END
                  isNullable: false
                  schemaType: anyOf
              }
              additionalProperties: null
          }]
          additionalProperties: null
      }]
      additionalProperties: null
  }
  ```

  ```go Go theme={null}
  {
    "models": [
      {
        "default_dimension": 1024,
        "max_batch_size": 96,
        "max_sequence_length": 2048,
        "modality": "text",
        "model": "llama-text-embed-v2",
        "provider_name": "NVIDIA",
        "short_description": "A high performance dense embedding model optimized for multilingual and cross-lingual text question-answering retrieval with support for long documents (up to 2048 tokens) and dynamic embedding size (Matryoshka Embeddings).",
        "supported_dimensions": [
          384,
          512,
          768,
          1024,
          2048
        ],
        "supported_metrics": [
          "cosine",
          "dotproduct"
        ],
        "supported_parameters": [
          {
            "allowed_values": [
              {
                "StringValue": "query",
                "IntValue": null,
                "FloatValue": null,
                "BoolValue": null
              },
              {
                "StringValue": "passage",
                "IntValue": null,
                "FloatValue": null,
                "BoolValue": null
              }
            ],
            "parameter": "input_type",
            "required": true,
            "type": "one_of",
            "value_type": "string"
          },
          {
            "allowed_values": [
              {
                "StringValue": "END",
                "IntValue": null,
                "FloatValue": null,
                "BoolValue": null
              },
              {
                "StringValue": "NONE",
                "IntValue": null,
                "FloatValue": null,
                "BoolValue": null
              },
              {
                "StringValue": "START",
                "IntValue": null,
                "FloatValue": null,
                "BoolValue": null
              }
            ],
            "default": {
              "StringValue": "END",
              "IntValue": null,
              "FloatValue": null,
              "BoolValue": null
            },
            "parameter": "truncate",
            "required": false,
            "type": "one_of",
            "value_type": "string"
          },
          {
            "allowed_values": [
              {
                "StringValue": null,
                "IntValue": 384,
                "FloatValue": null,
                "BoolValue": null
              },
              {
                "StringValue": null,
                "IntValue": 512,
                "FloatValue": null,
                "BoolValue": null
              },
              {
                "StringValue": null,
                "IntValue": 768,
                "FloatValue": null,
                "BoolValue": null
              },
              {
                "StringValue": null,
                "IntValue": 1024,
                "FloatValue": null,
                "BoolValue": null
              },
              {
                "StringValue": null,
                "IntValue": 2048,
                "FloatValue": null,
                "BoolValue": null
              }
            ],
            "default": {
              "StringValue": null,
              "IntValue": 1024,
              "FloatValue": null,
              "BoolValue": null
            },
            "parameter": "dimension",
            "required": false,
            "type": "one_of",
            "value_type": "integer"
          }
        ],
        "type": "embed",
        "vector_type": "dense"
      },
      {
        "default_dimension": 1024,
        "max_batch_size": 96,
        "max_sequence_length": 507,
        "modality": "text",
        "model": "multilingual-e5-large",
        "provider_name": "Microsoft",
        "short_description": "A high-performance dense embedding model trained on a mixture of multilingual datasets. It works well on messy data and short queries expected to return medium-length passages of text (1-2 paragraphs)",
        "supported_dimensions": [
          1024
        ],
        "supported_metrics": [
          "cosine",
          "euclidean"
        ],
        "supported_parameters": [
          {
            "allowed_values": [
              {
                "StringValue": "query",
                "IntValue": null,
                "FloatValue": null,
                "BoolValue": null
              },
              {
                "StringValue": "passage",
                "IntValue": null,
                "FloatValue": null,
                "BoolValue": null
              }
            ],
            "parameter": "input_type",
            "required": true,
            "type": "one_of",
            "value_type": "string"
          },
          {
            "allowed_values": [
              {
                "StringValue": "END",
                "IntValue": null,
                "FloatValue": null,
                "BoolValue": null
              },
              {
                "StringValue": "NONE",
                "IntValue": null,
                "FloatValue": null,
                "BoolValue": null
              }
            ],
            "default": {
              "StringValue": "END",
              "IntValue": null,
              "FloatValue": null,
              "BoolValue": null
            },
            "parameter": "truncate",
            "required": false,
            "type": "one_of",
            "value_type": "string"
          }
        ],
        "type": "embed",
        "vector_type": "dense"
      },
      {
        "max_batch_size": 96,
        "max_sequence_length": 512,
        "modality": "text",
        "model": "pinecone-sparse-english-v0",
        "provider_name": "Pinecone",
        "short_description": "A sparse embedding model for converting text to sparse vectors for keyword or hybrid semantic/keyword search. Built on the innovations of the DeepImpact architecture.",
        "supported_metrics": [
          "dotproduct"
        ],
        "supported_parameters": [
          {
            "allowed_values": [
              {
                "StringValue": "query",
                "IntValue": null,
                "FloatValue": null,
                "BoolValue": null
              },
              {
                "StringValue": "passage",
                "IntValue": null,
                "FloatValue": null,
                "BoolValue": null
              }
            ],
            "parameter": "input_type",
            "required": true,
            "type": "one_of",
            "value_type": "string"
          },
          {
            "allowed_values": [
              {
                "StringValue": "END",
                "IntValue": null,
                "FloatValue": null,
                "BoolValue": null
              },
              {
                "StringValue": "NONE",
                "IntValue": null,
                "FloatValue": null,
                "BoolValue": null
              }
            ],
            "default": {
              "StringValue": "END",
              "IntValue": null,
              "FloatValue": null,
              "BoolValue": null
            },
            "parameter": "truncate",
            "required": false,
            "type": "one_of",
            "value_type": "string"
          },
          {
            "default": {
              "StringValue": null,
              "IntValue": null,
              "FloatValue": null,
              "BoolValue": false
            },
            "parameter": "return_tokens",
            "required": false,
            "type": "any",
            "value_type": "boolean"
          },
          {
            "allowed_values": [
              {
                "StringValue": null,
                "IntValue": 512,
                "FloatValue": null,
                "BoolValue": null
              },
              {
                "StringValue": null,
                "IntValue": 2048,
                "FloatValue": null,
                "BoolValue": null
              }
            ],
            "default": {
              "StringValue": null,
              "IntValue": 512,
              "FloatValue": null,
              "BoolValue": null
            },
            "parameter": "max_tokens_per_sequence",
            "required": false,
            "type": "one_of",
            "value_type": "integer"
          }
        ],
        "type": "embed",
        "vector_type": "sparse"
      }
    ]
  }{
    "models": [
      {
        "max_batch_size": 100,
        "max_sequence_length": 1024,
        "modality": "text",
        "model": "bge-reranker-v2-m3",
        "provider_name": "BAAI",
        "short_description": "A high-performance, multilingual reranking model that works well on messy data and short queries expected to return medium-length passages of text (1-2 paragraphs)",
        "supported_parameters": [
          {
            "allowed_values": [
              {
                "StringValue": "END",
                "IntValue": null,
                "FloatValue": null,
                "BoolValue": null
              },
              {
                "StringValue": "NONE",
                "IntValue": null,
                "FloatValue": null,
                "BoolValue": null
              }
            ],
            "default": {
              "StringValue": "NONE",
              "IntValue": null,
              "FloatValue": null,
              "BoolValue": null
            },
            "parameter": "truncate",
            "required": false,
            "type": "one_of",
            "value_type": "string"
          }
        ],
        "type": "rerank"
      },
      {
        "max_batch_size": 200,
        "max_sequence_length": 40000,
        "modality": "text",
        "model": "cohere-rerank-3.5",
        "provider_name": "Cohere",
        "short_description": "Cohere's leading reranking model, balancing performance and latency for a wide range of enterprise search applications.",
        "supported_parameters": [
          {
            "default": {
              "StringValue": null,
              "IntValue": 3072,
              "FloatValue": null,
              "BoolValue": null
            },
            "max": 3072,
            "min": 1,
            "parameter": "max_chunks_per_doc",
            "required": false,
            "type": "numeric_range",
            "value_type": "integer"
          }
        ],
        "type": "rerank"
      },
      {
        "max_batch_size": 100,
        "max_sequence_length": 512,
        "modality": "text",
        "model": "pinecone-rerank-v0",
        "provider_name": "Pinecone",
        "short_description": "A state of the art reranking model that out-performs competitors on widely accepted benchmarks. It can handle chunks up to 512 tokens (1-2 paragraphs)",
        "supported_parameters": [
          {
            "allowed_values": [
              {
                "StringValue": "END",
                "IntValue": null,
                "FloatValue": null,
                "BoolValue": null
              },
              {
                "StringValue": "NONE",
                "IntValue": null,
                "FloatValue": null,
                "BoolValue": null
              }
            ],
            "default": {
              "StringValue": "END",
              "IntValue": null,
              "FloatValue": null,
              "BoolValue": null
            },
            "parameter": "truncate",
            "required": false,
            "type": "one_of",
            "value_type": "string"
          }
        ],
        "type": "rerank"
      }
    ]
  }
  ```

  ```csharp C# theme={null}
  {
      "models": [
          {
              "model": "llama-text-embed-v2",
              "short_description": "A high performance dense embedding model optimized for multilingual and cross-lingual text question-answering retrieval with support for long documents (up to 2048 tokens) and dynamic embedding size (Matryoshka Embeddings).",
              "type": "embed",
              "vector_type": "dense",
              "default_dimension": 1024,
              "modality": "text",
              "max_sequence_length": 2048,
              "max_batch_size": 96,
              "provider_name": "NVIDIA",
              "supported_dimensions": [
                  384,
                  512,
                  768,
                  1024,
                  2048
              ],
              "supported_metrics": [
                  "cosine",
                  "cosine"
              ],
              "supported_parameters": [
                  {
                      "parameter": "input_type",
                      "type": "one_of",
                      "value_type": "string",
                      "required": true,
                      "allowed_values": [
                          "query",
                          "passage"
                      ]
                  },
                  {
                      "parameter": "truncate",
                      "type": "one_of",
                      "value_type": "string",
                      "required": false,
                      "allowed_values": [
                          "END",
                          "NONE",
                          "START"
                      ],
                      "default": "END"
                  },
                  {
                      "parameter": "dimension",
                      "type": "one_of",
                      "value_type": "integer",
                      "required": false,
                      "allowed_values": [
                          384,
                          512,
                          768,
                          1024,
                          2048
                      ],
                      "default": 1024
                  }
              ]
          },
          {
              "model": "multilingual-e5-large",
              "short_description": "A high-performance dense embedding model trained on a mixture of multilingual datasets. It works well on messy data and short queries expected to return medium-length passages of text (1-2 paragraphs)",
              "type": "embed",
              "vector_type": "dense",
              "default_dimension": 1024,
              "modality": "text",
              "max_sequence_length": 507,
              "max_batch_size": 96,
              "provider_name": "Microsoft",
              "supported_dimensions": [
                  1024
              ],
              "supported_metrics": [
                  "cosine",
                  "cosine"
              ],
              "supported_parameters": [
                  {
                      "parameter": "input_type",
                      "type": "one_of",
                      "value_type": "string",
                      "required": true,
                      "allowed_values": [
                          "query",
                          "passage"
                      ]
                  },
                  {
                      "parameter": "truncate",
                      "type": "one_of",
                      "value_type": "string",
                      "required": false,
                      "allowed_values": [
                          "END",
                          "NONE"
                      ],
                      "default": "END"
                  }
              ]
          },
          {
              "model": "pinecone-sparse-english-v0",
              "short_description": "A sparse embedding model for converting text to sparse vectors for keyword or hybrid semantic/keyword search. Built on the innovations of the DeepImpact architecture.",
              "type": "embed",
              "vector_type": "sparse",
              "modality": "text",
              "max_sequence_length": 512,
              "max_batch_size": 96,
              "provider_name": "Pinecone",
              "supported_metrics": [
                  "cosine"
              ],
              "supported_parameters": [
                  {
                      "parameter": "input_type",
                      "type": "one_of",
                      "value_type": "string",
                      "required": true,
                      "allowed_values": [
                          "query",
                          "passage"
                      ]
                  },
                  {
                      "parameter": "truncate",
                      "type": "one_of",
                      "value_type": "string",
                      "required": false,
                      "allowed_values": [
                          "END",
                          "NONE"
                      ],
                      "default": "END"
                  },
                  {
                      "parameter": "return_tokens",
                      "type": "any",
                      "value_type": "boolean",
                      "required": false,
                      "default": false
                  }
              ]
          },
          {
              "model": "bge-reranker-v2-m3",
              "short_description": "A high-performance, multilingual reranking model that works well on messy data and short queries expected to return medium-length passages of text (1-2 paragraphs)",
              "type": "rerank",
              "modality": "text",
              "max_sequence_length": 1024,
              "max_batch_size": 100,
              "provider_name": "BAAI",
              "supported_parameters": [
                  {
                      "parameter": "truncate",
                      "type": "one_of",
                      "value_type": "string",
                      "required": false,
                      "allowed_values": [
                          "END",
                          "NONE"
                      ],
                      "default": "NONE"
                  }
              ]
          },
          {
              "model": "cohere-rerank-3.5",
              "short_description": "Cohere\u0027s leading reranking model, balancing performance and latency for a wide range of enterprise search applications.",
              "type": "rerank",
              "modality": "text",
              "max_sequence_length": 40000,
              "max_batch_size": 200,
              "provider_name": "Cohere",
              "supported_parameters": [
                  {
                      "parameter": "max_chunks_per_doc",
                      "type": "numeric_range",
                      "value_type": "integer",
                      "required": false,
                      "min": 1,
                      "max": 3072,
                      "default": 3072
                  }
              ]
          },
          {
              "model": "pinecone-rerank-v0",
              "short_description": "A state of the art reranking model that out-performs competitors on widely accepted benchmarks. It can handle chunks up to 512 tokens (1-2 paragraphs)",
              "type": "rerank",
              "modality": "text",
              "max_sequence_length": 512,
              "max_batch_size": 100,
              "provider_name": "Pinecone",
              "supported_parameters": [
                  {
                      "parameter": "truncate",
                      "type": "one_of",
                      "value_type": "string",
                      "required": false,
                      "allowed_values": [
                          "END",
                          "NONE"
                      ],
                      "default": "END"
                  }
              ]
          }
      ]
  }
  ```

  ```json curl theme={null}
  {
    "models": [
      {
        "model": "llama-text-embed-v2",
        "short_description": "A high performance dense embedding model optimized for multilingual and cross-lingual text question-answering retrieval with support for long documents (up to 2048 tokens) and dynamic embedding size (Matryoshka Embeddings).",
        "type": "embed",
        "vector_type": "dense",
        "default_dimension": 1024,
        "modality": "text",
        "max_sequence_length": 2048,
        "max_batch_size": 96,
        "provider_name": "NVIDIA",
        "supported_metrics": [
          "Cosine",
          "DotProduct"
        ],
        "supported_dimensions": [
          384,
          512,
          768,
          1024,
          2048
        ],
        "supported_parameters": [
          {
            "parameter": "input_type",
            "required": true,
            "type": "one_of",
            "value_type": "string",
            "allowed_values": [
              "query",
              "passage"
            ]
          },
          {
            "parameter": "truncate",
            "required": false,
            "default": "END",
            "type": "one_of",
            "value_type": "string",
            "allowed_values": [
              "END",
              "NONE",
              "START"
            ]
          },
          {
            "parameter": "dimension",
            "required": false,
            "default": 1024,
            "type": "one_of",
            "value_type": "integer",
            "allowed_values": [
              384,
              512,
              768,
              1024,
              2048
            ]
          }
        ]
      },
      {
        "model": "multilingual-e5-large",
        "short_description": "A high-performance dense embedding model trained on a mixture of multilingual datasets. It works well on messy data and short queries expected to return medium-length passages of text (1-2 paragraphs)",
        "type": "embed",
        "vector_type": "dense",
        "default_dimension": 1024,
        "modality": "text",
        "max_sequence_length": 507,
        "max_batch_size": 96,
        "provider_name": "Microsoft",
        "supported_metrics": [
          "Cosine",
          "Euclidean"
        ],
        "supported_dimensions": [
          1024
        ],
        "supported_parameters": [
          {
            "parameter": "input_type",
            "required": true,
            "type": "one_of",
            "value_type": "string",
            "allowed_values": [
              "query",
              "passage"
            ]
          },
          {
            "parameter": "truncate",
            "required": false,
            "default": "END",
            "type": "one_of",
            "value_type": "string",
            "allowed_values": [
              "END",
              "NONE"
            ]
          }
        ]
      },
      {
        "model": "pinecone-sparse-english-v0",
        "short_description": "A sparse embedding model for converting text to sparse vectors for keyword or hybrid semantic/keyword search. Built on the innovations of the DeepImpact architecture.",
        "type": "embed",
        "vector_type": "sparse",
        "modality": "text",
        "max_sequence_length": 512,
        "max_batch_size": 96,
        "provider_name": "Pinecone",
        "supported_metrics": [
          "DotProduct"
        ],
        "supported_parameters": [
          {
            "parameter": "input_type",
            "required": true,
            "type": "one_of",
            "value_type": "string",
            "allowed_values": [
              "query",
              "passage"
            ]
          },
          {
            "parameter": "truncate",
            "required": false,
            "default": "END",
            "type": "one_of",
            "value_type": "string",
            "allowed_values": [
              "END",
              "NONE"
            ]
          },
          {
            "parameter": "return_tokens",
            "required": false,
            "default": false,
            "type": "any",
            "value_type": "boolean"
          }
        ]
      },
      {
        "model": "bge-reranker-v2-m3",
        "short_description": "A high-performance, multilingual reranking model that works well on messy data and short queries expected to return medium-length passages of text (1-2 paragraphs)",
        "type": "rerank",
        "modality": "text",
        "max_sequence_length": 1024,
        "max_batch_size": 100,
        "provider_name": "BAAI",
        "supported_parameters": [
          {
            "parameter": "truncate",
            "required": false,
            "default": "NONE",
            "type": "one_of",
            "value_type": "string",
            "allowed_values": [
              "END",
              "NONE"
            ]
          }
        ]
      },
      {
        "model": "cohere-rerank-3.5",
        "short_description": "Cohere's leading reranking model, balancing performance and latency for a wide range of enterprise search applications.",
        "type": "rerank",
        "modality": "text",
        "max_sequence_length": 40000,
        "max_batch_size": 200,
        "provider_name": "Cohere",
        "supported_parameters": [
          {
            "parameter": "max_chunks_per_doc",
            "required": false,
            "default": 3072,
            "type": "numeric_range",
            "value_type": "integer",
            "min": 1,
            "max": 3072
          }
        ]
      },
      {
        "model": "pinecone-rerank-v0",
        "short_description": "A state of the art reranking model that out-performs competitors on widely accepted benchmarks. It can handle chunks up to 512 tokens (1-2 paragraphs)",
        "type": "rerank",
        "modality": "text",
        "max_sequence_length": 512,
        "max_batch_size": 100,
        "provider_name": "Pinecone",
        "supported_parameters": [
          {
            "parameter": "truncate",
            "required": false,
            "default": "END",
            "type": "one_of",
            "value_type": "string",
            "allowed_values": [
              "END",
              "NONE"
            ]
          }
        ]
      }
    ]
  }
  ```
</ResponseExample>



# Rerank documents
Source: https://docs.pinecone.io/reference/api/2025-04/inference/rerank

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-04/inference_2025-04.oas.yaml post /rerank
Rerank results according to their relevance to a query.

For guidance and examples, see [Rerank results](https://docs.pinecone.io/guides/search/rerank-results).

<RequestExample>
  ```python Python theme={null}
  from pinecone.grpc import PineconeGRPC as Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  result = pc.inference.rerank(
      model="bge-reranker-v2-m3",
      query="The tech company Apple is known for its innovative products like the iPhone.",
      documents=[
          {"id": "vec1", "text": "Apple is a popular fruit known for its sweetness and crisp texture."},
          {"id": "vec2", "text": "Many people enjoy eating apples as a healthy snack."},
          {"id": "vec3", "text": "Apple Inc. has revolutionized the tech industry with its sleek designs and user-friendly interfaces."},
          {"id": "vec4", "text": "An apple a day keeps the doctor away, as the saying goes."},
      ],
      top_n=4,
      return_documents=True,
      parameters={
          "truncate": "END"
      }
  )

  print(result)
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  const rerankingModel = 'bge-reranker-v2-m3';

  const query = 'The tech company Apple is known for its innovative products like the iPhone.';

  const documents = [
    { id: 'vec1', text: 'Apple is a popular fruit known for its sweetness and crisp texture.' },
    { id: 'vec2', text: 'Many people enjoy eating apples as a healthy snack.' },
    { id: 'vec3', text: 'Apple Inc. has revolutionized the tech industry with its sleek designs and user-friendly interfaces.' },
    { id: 'vec4', text: 'An apple a day keeps the doctor away, as the saying goes.' },
  ];

  const rerankOptions = {
    topN: 4,
    returnDocuments: true,
    parameters: {
      truncate: 'END'
    }, 
  };

  const response = await pc.inference.rerank(
    rerankingModel,
    query,
    documents,
    rerankOptions
  );

  console.log(response);
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Inference;
  import io.pinecone.clients.Pinecone;
  import org.openapitools.inference.client.model.RerankResult;
  import org.openapitools.inference.client.ApiException;

  import java.util.*;

  public class RerankExample {
      public static void main(String[] args) throws ApiException {
          Pinecone pc = new Pinecone.Builder("YOUR_API_KEY").build();
          Inference inference = pc.getInferenceClient();

          // The model to use for reranking
          String model = "bge-reranker-v2-m3";

          // The query to rerank documents against
          String query = "The tech company Apple is known for its innovative products like the iPhone.";

          // Add the documents to rerank
          List<Map<String, Object>> documents = new ArrayList<>();
          Map<String, Object> doc1 = new HashMap<>();
          doc1.put("id", "vec1");
          doc1.put("text", "Apple is a popular fruit known for its sweetness and crisp texture.");
          documents.add(doc1);

          Map<String, Object> doc2 = new HashMap<>();
          doc2.put("id", "vec2");
          doc2.put("text", "Many people enjoy eating apples as a healthy snack.");
          documents.add(doc2);

          Map<String, Object> doc3 = new HashMap<>();
          doc3.put("id", "vec3");
          doc3.put("text", "Apple Inc. has revolutionized the tech industry with its sleek designs and user-friendly interfaces.");
          documents.add(doc3);

          Map<String, Object> doc4 = new HashMap<>();
          doc4.put("id", "vec4");
          doc4.put("text", "An apple a day keeps the doctor away, as the saying goes.");
          documents.add(doc4);

          // The fields to rank the documents by. If not provided, the default is "text"
          List<String> rankFields = Arrays.asList("text");

          // The number of results to return sorted by relevance. Defaults to the number of inputs
          int topN = 4;

          // Whether to return the documents in the response
          boolean returnDocuments = true;

          // Additional model-specific parameters for the reranker
          Map<String, Object> parameters = new HashMap<>();
          parameters.put("truncate", "END");

          // Send ranking request
          RerankResult result = inference.rerank(model, query, documents, rankFields, topN, returnDocuments, parameters);

          // Get ranked data
          System.out.println(result.getData());
      }
  }
  ```

  ```go Go theme={null}
  package main

  import (
      "context"
      "fmt"
      "log"

      "github.com/pinecone-io/go-pinecone/v4/pinecone"
  )

  func main() {
      ctx := context.Background()

      pc, err := pinecone.NewClient(pinecone.NewClientParams{
          ApiKey: "YOUR_API_KEY",
      })
      if err != nil {
          log.Fatalf("Failed to create Client: %v", err)
      }

      rerankModel := "bge-reranker-v2-m3"
      topN := 4
      returnDocuments := true
      documents := []pinecone.Document{
          {"id": "vec1", "text": "Apple is a popular fruit known for its sweetness and crisp texture."},
          {"id": "vec2", "text": "Many people enjoy eating apples as a healthy snack."},
          {"id": "vec3", "text": "Apple Inc. has revolutionized the tech industry with its sleek designs and user-friendly interfaces."},
          {"id": "vec4", "text": "An apple a day keeps the doctor away, as the saying goes."},
      }

      ranking, err := pc.Inference.Rerank(ctx, &pinecone.RerankRequest{
          Model:           rerankModel,
          Query:           "The tech company Apple is known for its innovative products like the iPhone.",
          ReturnDocuments: &returnDocuments,
          TopN:            &topN,
          RankFields:      &[]string{"text"},
          Documents:       documents,
      })
      if err != nil {
          log.Fatalf("Failed to rerank: %v", err)
      }
      fmt.Printf("Rerank result: %+v\n", ranking)
  }
  ```

  ```csharp C# theme={null}
  using Pinecone;

  var pinecone = new PineconeClient("YOUR_API_KEY");

  // The model to use for reranking
  var model = "bge-reranker-v2-m3";

  // The query to rerank documents against
  var query = "The tech company Apple is known for its innovative products like the iPhone.";

  // Add the documents to rerank
  var documents = new List<Dictionary<string, object>>
  {
      new()
      {
          ["id"] = "vec1",
          ["my_field"] = "Apple is a popular fruit known for its sweetness and crisp texture."
      },
      new()
      {
          ["id"] = "vec2",
          ["my_field"] = "Many people enjoy eating apples as a healthy snack."
      },
      new()
      {
          ["id"] = "vec3",
          ["my_field"] =
              "Apple Inc. has revolutionized the tech industry with its sleek designs and user-friendly interfaces."
      },
      new()
      {
          ["id"] = "vec4",
          ["my_field"] = "An apple a day keeps the doctor away, as the saying goes."
      }
  };

  // The fields to rank the documents by. If not provided, the default is "text"
  var rankFields = new List<string> { "my_field" };

  // The number of results to return sorted by relevance. Defaults to the number of inputs
  int topN = 4;

  // Whether to return the documents in the response
  bool returnDocuments = true;

  // Additional model-specific parameters for the reranker
  var parameters = new Dictionary<string, object>
  {
      ["truncate"] = "END"
  };

  // Send ranking request
  var result = await pinecone.Inference.RerankAsync(
      new RerankRequest
      {
          Model = model,
          Query = query,
          Documents = documents,
          RankFields = rankFields,
          TopN = topN,
          ReturnDocuments = true,
          Parameters = parameters
      });

  Console.WriteLine(result);
  ```

  ```shell curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl https://api.pinecone.io/rerank \
    -H "Content-Type: application/json" \
    -H "Accept: application/json" \
    -H "X-Pinecone-API-Version: 2025-04" \
    -H "Api-Key: $PINECONE_API_KEY" \
  -d '{
    "model": "bge-reranker-v2-m3",
    "query": "The tech company Apple is known for its innovative products like the iPhone.",
    "return_documents": true,
    "top_n": 4,
    "documents": [
      {"id": "vec1", "text": "Apple is a popular fruit known for its sweetness and crisp texture."},
      {"id": "vec2", "text": "Many people enjoy eating apples as a healthy snack."},
      {"id": "vec3", "text": "Apple Inc. has revolutionized the tech industry with its sleek designs and user-friendly interfaces."},
      {"id": "vec4", "text": "An apple a day keeps the doctor away, as the saying goes."}
    ],
    "parameters": {
      "truncate": "END"
    }
  }'
  ```
</RequestExample>

<ResponseExample>
  ```python Python theme={null}
  RerankResult(
    model='bge-reranker-v2-m3',
    data=[
      { index=2, score=0.48357219,
        document={id="vec3", text="Apple Inc. has re..."} },
      { index=0, score=0.048405956,
        document={id="vec1", text="Apple is a popula..."} },
      { index=3, score=0.007846239,
        document={id="vec4", text="An apple a day ke..."} },
      { index=1, score=0.0006563728,
        document={id="vec2", text="Many people enjoy..."} }
    ],
    usage={'rerank_units': 1}
  )
  ```

  ```javascript JavaScript theme={null}
  {
    model: 'bge-reranker-v2-m3',
    data: [
      { index: 2, score: 0.48357219, document: [Object] },
      { index: 0, score: 0.048405956, document: [Object] },
      { index: 3, score: 0.007846239, document: [Object] },
      { index: 1, score: 0.0006563728, document: [Object] }
    ],
    usage: { rerankUnits: 1 }
  }
  ```

  ```java Java theme={null}
  [class RankedDocument {
      index: 2
      score: 0.48357219
      document: {id=vec3, text=Apple Inc. has revolutionized the tech industry with its sleek designs and user-friendly interfaces.}
      additionalProperties: null
  }, class RankedDocument {
      index: 0
      score: 0.048405956
      document: {id=vec1, text=Apple is a popular fruit known for its sweetness and crisp texture.}
      additionalProperties: null
  }, class RankedDocument {
      index: 3
      score: 0.007846239
      document: {id=vec4, text=An apple a day keeps the doctor away, as the saying goes.}
      additionalProperties: null
  }, class RankedDocument {
      index: 1
      score: 0.0006563728
      document: {id=vec2, text=Many people enjoy eating apples as a healthy snack.}
      additionalProperties: null
  }]
  ```

  ```go Go theme={null}
  Rerank result: {
    "data": [
      {
        "document": {
          "id": "vec3",
          "text": "Apple Inc. has revolutionized the tech industry with its sleek designs and user-friendly interfaces."
        },
        "index": 2,
        "score": 0.48357219
      },
      {
        "document": {
          "id": "vec1",
          "text": "Apple is a popular fruit known for its sweetness and crisp texture."
        },
        "index": 0,
        "score": 0.048405956
      },
      {
        "document": {
          "id": "vec4",
          "text": "An apple a day keeps the doctor away, as the saying goes."
        },
        "index": 3,
        "score": 0.007846239
      },
      {
        "document": {
          "id": "vec2",
          "text": "Many people enjoy eating apples as a healthy snack."
        },
        "index": 1,
        "score": 0.0006563728
      }
    ],
    "model": "bge-reranker-v2-m3",
    "usage": {
      "rerank_units": 1
    }
  }
  ```

  ```csharp C# theme={null}
  {
    "model": "bge-reranker-v2-m3",
    "data": [
      {
        "index": 2,
        "score": 0.48357219,
        "document": {
          "id": "vec3",
          "my_field": "Apple Inc. has revolutionized the tech industry with its sleek designs and user-friendly interfaces."
        }
      },
      {
        "index": 0,
        "score": 0.048405956,
        "document": {
          "id": "vec1",
          "my_field": "Apple is a popular fruit known for its sweetness and crisp texture."
        }
      },
      {
        "index": 3,
        "score": 0.007846239,
        "document": {
          "id": "vec4",
          "my_field": "An apple a day keeps the doctor away, as the saying goes."
        }
      },
      {
        "index": 1,
        "score": 0.0006563728,
        "document": {
          "id": "vec2",
          "my_field": "Many people enjoy eating apples as a healthy snack."
        }
      }
    ],
    "usage": {
      "rerank_units": 1
    }
  }
  ```

  ```JSON curl theme={null}
  {
    "data":[
      {
        "index":2,
        "document":{
          "id":"vec3",
          "text":"Apple Inc. has revolutionized the tech industry with its sleek designs and user-friendly interfaces."
        },
        "score":0.47654688
      },
      {
        "index":0,
        "document":{
          "id":"vec1",
          "text":"Apple is a popular fruit known for its sweetness and crisp texture."
        },
        "score":0.047963805
      },
      {
        "index":3,
        "document":{
          "id":"vec4",
          "text":"An apple a day keeps the doctor away, as the saying goes."
        },
        "score":0.007587992
      },
      {
        "index":1,
        "document":{
          "id":"vec2",
          "text":"Many people enjoy eating apples as a healthy snack."
        },
        "score":0.0006491712
      }
    ],
    "usage":{
      "rerank_units":1
    }
  }
  ```
</ResponseExample>



# CLI authentication
Source: https://docs.pinecone.io/reference/cli/authentication



<Note>
  This feature is in [public preview](/release-notes/feature-availability).
</Note>

This document describes how to authenticate the Pinecone CLI to manage your Pinecone resources.


## Authenticating

There are three ways to authenticate the Pinecone CLI: through a web browser with [user login](#user-login), using a [service account](#service-account), or with an [API key](#api-key).

This table describes the Pinecone operations supported by each authentication method:

| Method          | Admin API | Control plane |
| :-------------- | :-------- | :------------ |
| User login      | ✅         | ✅             |
| Service account | ✅         | ✅             |
| API key         | ❌         | ✅             |

* Admin API–related commands (organization and project management, API key operations):
  * `pc organization` (`list`, `describe`, `update`, `delete`)
  * `pc project` (`create`, `list`, `describe`, `update`, `delete`)
  * `pc api-key` (`create`, `list`, `describe`, `update`, `delete`)

* Control plane–related commands (index management):
  * `pc index` (`create`, `list`, `describe`, `configure`, `delete`)

<Note>
  Commands for data plane operations will be added in a future release.
</Note>

### User login

User login requires you to authenticate through a web browser. Subsequent CLI requests use a locally stored auth token that expires after 30 minutes but refreshes automatically. After 24 hours, you must re-authenticate.

```bash  theme={null}

# Authenticate in a web browser
pc auth login
```

When you authenticate with `pc auth login`, the CLI automatically targets:

* The default organization returned by the server for your user.
* The first project in the list of that organization's projects.

However, you can change organization and project as needed:

```bash  theme={null}
pc auth target -o "my-org" -p "my-project"
```

When you authenticate with user login, the CLI uses [managed API keys](#managed-keys) for control plane operations, unless you've set a default API key.

<Tip>
  To learn more about targeting organizations and projects, see [CLI target context](/reference/cli/target-context). To understand how the CLI prioritizes authentication methods, see [Auth priority](#auth-priority).
</Tip>

### Service account

To authenticate with a service account, provide a client ID and secret associated with a [service account](/guides/organizations/manage-service-accounts).

```bash  theme={null}
pc auth configure \
  --client-id "YOUR_CLIENT_ID" \
  --client-secret "YOUR_CLIENT_SECRET"


# Or specify a project directly
pc auth configure \
  --client-id "YOUR_CLIENT_ID" \
  --client-secret "YOUR_CLIENT_SECRET" \
  --project-id "YOUR_PROJECT_ID"
```

Or set these environment variables:

```bash  theme={null}
export PINECONE_CLIENT_ID="your-client-id"
export PINECONE_CLIENT_SECRET="your-client-secret"
```

When you authentiate with a service account:

* If your organization has only one project, the CLI automatically targets that project.
* If your organization has multiple projects, the CLI prompts you to select a project (or you can use the `--project-id` flag, as shown above).
* If your organization has no projects, create one. Then, set it as the target:

  ```bash  theme={null}
  # Specify a project
  pc target -p "my-project"
  # Select a project interactively
  pc target
  ```

When you authenticate with a service account, the CLI uses [managed API keys](#managed-keys) for control plane operations, unless you've set a default API key.

<Tip>
  To learn more about targeting organizations and projects, see [CLI target context](/reference/cli/target-context). To understand how the CLI prioritizes authentication methods, see [Auth priority](#auth-priority).
</Tip>

### API key

You can also use an API to authenticate the CLI with Pinecone. This is useful for automation or CI/CD scenarios where you can't use interactive user login or a service account.

Since each API key is associated with a specific project, the CLI uses that key's project for all operations. A default (manually specified) API key overrides any [target context](/reference/cli/target-context) you've set — you don't need to run `pc target`.

```bash  theme={null}
pc auth configure --api-key "YOUR_API_KEY"
```

Or set this environment variable:

```bash  theme={null}
export PINECONE_API_KEY="YOUR_API_KEY"
```

<Note>
  Because API keys are associated with a specific organization and project, they do not require [target context](/reference/cli/target-context). Also, to understand how the CLI prioritizes authentication methods, see [Auth priority](#auth-priority).
</Note>


## Auth priority

The CLI chooses which authentication method to use based on the type of operation.

### Control plane operations (indexes)

Control plane operations prioritize authentication credentials in the following order:

1. Default API key - Uses the project associated with the key.
2. User login token - Creates and uses [managed keys](#managed-keys).
3. Service account - Creates and uses [managed keys](#managed-keys).

### Admin API operations (organizations, projects, API keys)

Admin API operations prioritize authentication credentials in the following order:

1. User login token
2. Service account

<Note>
  Default API keys do not provide Admin API access.
</Note>

### Environment variables vs. stored configuration

Within each credential type, environment variables always override stored configuration:

* `PINECONE_API_KEY` (env var) overrides default API key stored via `pc auth configure --api-key`.
* `PINECONE_CLIENT_ID` and `PINECONE_CLIENT_SECRET` (env vars) override service account credentials stored via `pc auth configure`.
* User login tokens have no environment variable equivalent. They're always stored locally.

**Example scenarios:**

* If `PINECONE_API_KEY` (env var) is set, the CLI uses it for control plane operations, regardless of any stored default API key value.
* If you're logged in via `pc auth login` and also have `PINECONE_CLIENT_ID` and `PINECONE_CLIENT_SECRET` set:
  * Control plane operations: User login token is used (creates managed keys).
  * Admin API operations: User login token is used.
  * The service account env vars are ignored.
* If you have a default API key stored via `pc auth configure --api-key` and are also logged in through the web browser:
  * Control plane operations: Default API key is used.
  * Admin API operations: User login token is used.

Environment variables are never persisted to local storage. They only override stored values at runtime.

### Default API keys and target context

<Warning>
  Default (manually specified) API keys override any [target context](/reference/cli/target-context). Control plane operations always use the project associated with the API key, regardless of what you've set with `pc target`.
</Warning>

When you set a default API key (via `pc auth configure --api-key` or `PINECONE_API_KEY`):

* The default API key is used for control plane operations.
* [Managed keys](#managed-keys) are not created.
* If you also have user login or service account credentials, those are still used for Admin API operations.

Setting a default API key (via `pc auth configure --api-key` or `PINECONE_API_KEY`) does not clear user login tokens or service account credentials.

### User login and service accounts

User login and service accounts are mutually exclusive when configured via CLI commands:

* Running `pc auth login` clears any stored service account credentials.
* Running `pc auth configure --client-id --client-secret` clears the stored auth token from `pc auth login`.

However, if you set service account environment variables (`PINECONE_CLIENT_ID` and `PINECONE_CLIENT_SECRET`) without running `pc auth configure`, the CLI does not clear your stored user login token.

<Note>
  User login and service accounts both use [managed keys](#managed-keys) for control plane operations (unless you've set a default API key).
</Note>


## Clearing credentials (logging out)

To clear your authentication credentials:

```bash  theme={null}
pc auth logout
```

This command clears local data:

* User login token
* Service account credentials (client ID and secret)
* Default (manually specified) API key
* Locally managed keys (for all projects)
* [Target organization and project context](/reference/cli/target-context)

<Note>
  `pc auth logout` does not delete managed API keys from Pinecone's servers. Those keys remain active and can be used to access your projects. To fully clean up, run `pc auth local-keys prune` before logging out. See [Deleting API keys](#deleting-api-keys) for details.
</Note>


## Managed keys

When authenticated with [user login](#user-login) or a [service account](#service-account), the CLI automatically creates and manages API keys for control plane operations. This happens transparently, the first time you run a control plane command like `pc index list`. You don't need to create or manage these keys yourself.

### When managed keys are created

Managed keys are created only when you're authenticated via user login or service account, and there's no default (manually specified) API key set.

After authenticating, the first time you run a control plane command like `pc index list`:

1. The CLI checks if a managed key already exists locally for the target project.
2. If not found, the CLI creates a new API key via the Admin API.
3. The key is stored both remotely (in Pinecone) and locally for future use.

Subsequent commands targeting the same project reuse the stored key.

<Note>
  If you set a default API key, managed keys are not created. The default API key is used instead.
</Note>

### Where managed keys are stored

Managed API keys are stored locally and remotely:

* Local: Stored in `~/.config/pinecone/secrets.yaml` under the `project_api_keys` field as plain text, with file permissions set to 0600 (owner read/write only). For more details, see [Local data storage](#local-data-storage).
* Remote: Stored in Pinecone as regular API keys, visible in the web console.

<Note>
  The CLI will not display managed API keys after they're created.
</Note>

### Identifying managed keys

In the Pinecone web console, CLI-created keys have:

* Name: `pinecone-cli-{6-character-alphanumeric}` (for example, `pinecone-cli-a3f9k2`)
* Origin: `cli_created`

To list all managed keys stored locally:

```bash  theme={null}
pc auth local-keys list
```

This shows managed keys tracked in your local `secrets.yaml` file, including which projects they belong to.

### Deleting API keys

There are a few ways to use the CLI to delete API keys (managed or not), locally and remotely.

**Delete locally tracked managed keys (local and remote)**:

The `pc auth local-keys prune` command deletes managed keys that are tracked in your local `secrets.yaml` file. It does not affect API keys that were created outside the CLI or aren't tracked locally.

```bash  theme={null}

---
**Navigation:** [← Previous](./24-list-collections.md) | [Index](./index.md) | [Next →](./26-delete-all-locally-tracked-managed-keys-cli-create.md)
