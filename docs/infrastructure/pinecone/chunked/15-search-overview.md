**Navigation:** [← Previous](./14-lexical-search.md) | [Index](./index.md) | [Next →](./16-delete-vectors.md)

# Search overview
Source: https://docs.pinecone.io/guides/search/search-overview

Explore semantic, lexical, and hybrid search options.


## Search types

* [Semantic search](/guides/search/semantic-search)
* [Lexical search](/guides/search/lexical-search)
* [Hybrid search](/guides/search/hybrid-search)


## Optimization

* [Filter by metadata](/guides/search/filter-by-metadata)
* [Rerank results](/guides/search/rerank-results)
* [Parallel queries](/guides/search/semantic-search#parallel-queries)


## Limits

| Metric            | Limit  |
| :---------------- | :----- |
| Max `top_k` value | 10,000 |
| Max result size   | 4MB    |

The query result size is affected by the dimension of the dense vectors and whether or not dense vector values and metadata are included in the result.

<Tip>
  If a query fails due to exceeding the 4MB result size limit, choose a lower `top_k` value, or use `include_metadata=False` or `include_values=False` to exclude metadata or values from the result.
</Tip>


## Cost

* To understand how cost is calculated for queries, see [Understanding cost](/guides/manage-cost/understanding-cost#query).
* For up-to-date pricing information, see [Pricing](https://www.pinecone.io/pricing/).


## Data freshness

Pinecone is eventually consistent, so there can be a slight delay before new or changed records are visible to queries. You can view index stats to [check data freshness](/guides/index-data/check-data-freshness).



# Semantic search
Source: https://docs.pinecone.io/guides/search/semantic-search

Find semantically similar records using dense vectors.

This page shows you how to search a [dense index](/guides/index-data/indexing-overview#dense-indexes) for records that are most similar in meaning and context to a query. This is often called semantic search, nearest neighbor search, similarity search, or just vector search.

Semantic search uses [dense vectors](https://www.pinecone.io/learn/vector-embeddings/). Each number in a dense vector corresponds to a point in a multidimensional space. Vectors that are closer together in that space are semantically similar.


## Search with text

<Note>
  Searching with text is supported only for [indexes with integrated embedding](/guides/index-data/indexing-overview#integrated-embedding).
</Note>

To search a dense index with a query text, use the [`search_records`](/reference/api/latest/data-plane/search_records) operation with the following parameters:

* The `namespace` to query. To use the default namespace, set the namespace to `"__default__"`.
* The `query.inputs.text` parameter with the query text. Pinecone uses the embedding model integrated with the index to convert the text to a dense vector automatically.
* The `query.top_k` parameter with the number of similar records to return.
* Optionally, you can specify the `fields` to return in the response. If not specified, the response will include all fields.

For example, the following code searches for the 2 records most semantically related to a query text:

<CodeGroup>
  ```python Python theme={null}
  from pinecone import Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  # To get the unique host for an index, 
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  index = pc.Index(host="INDEX_HOST")

  results = index.search(
      namespace="example-namespace", 
      query={
          "inputs": {"text": "Disease prevention"}, 
          "top_k": 2
      },
      fields=["category", "chunk_text"]
  )

  print(results)
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({ apiKey: "YOUR_API_KEY" })

  // To get the unique host for an index, 
  // see https://docs.pinecone.io/guides/manage-data/target-an-index
  const namespace = pc.index("INDEX_NAME", "INDEX_HOST").namespace("example-namespace");

  const response = await namespace.searchRecords({
    query: {
      topK: 2,
      inputs: { text: 'Disease prevention' },
    },
    fields: ['chunk_text', 'category'],
  });

  console.log(response);
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Index;
  import io.pinecone.configs.PineconeConfig;
  import io.pinecone.configs.PineconeConnection;
  import org.openapitools.db_data.client.ApiException;
  import org.openapitools.db_data.client.model.SearchRecordsResponse;

  import java.util.*;

  public class SearchText {
      public static void main(String[] args) throws ApiException {
          PineconeConfig config = new PineconeConfig("YOUR_API_KEY");
          // To get the unique host for an index, 
          // see https://docs.pinecone.io/guides/manage-data/target-an-index
          config.setHost("INDEX_HOST");
          PineconeConnection connection = new PineconeConnection(config);

          Index index = new Index(config, connection, "integrated-dense-java");

          String query = "Disease prevention";
          List<String> fields = new ArrayList<>();
          fields.add("category");
          fields.add("chunk_text");

          // Search the dense index
          SearchRecordsResponse recordsResponse = index.searchRecordsByText(query,  "example-namespace", fields, 2, null, null);

          // Print the results
          System.out.println(recordsResponse);
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

      // To get the unique host for an index, 
      // see https://docs.pinecone.io/guides/manage-data/target-an-index
      idxConnection, err := pc.Index(pinecone.NewIndexConnParams{Host: "INDEX_HOST", Namespace: "example-namespace"})
      if err != nil {
          log.Fatalf("Failed to create IndexConnection for Host: %v", err)
      } 

      res, err := idxConnection.SearchRecords(ctx, &pinecone.SearchRecordsRequest{
          Query: pinecone.SearchRecordsQuery{
              TopK: 2,
              Inputs: &map[string]interface{}{
                  "text": "Disease prevention",
              },
          },
          Fields: &[]string{"chunk_text", "category"},
      })
      if err != nil {
          log.Fatalf("Failed to search records: %v", err)
      }
      fmt.Printf(prettifyStruct(res))
  }
  ```

  ```csharp C# theme={null}
  using Pinecone;

  var pinecone = new PineconeClient("YOUR_API_KEY");

  // To get the unique host for an index, 
  // see https://docs.pinecone.io/guides/manage-data/target-an-index
  var index = pinecone.Index(host: "INDEX_HOST");

  var response = await index.SearchRecordsAsync(
      "example-namespace",
      new SearchRecordsRequest
      {
          Query = new SearchRecordsRequestQuery
          {
              TopK = 4,
              Inputs = new Dictionary<string, object?> { { "text", "Disease prevention" } },
          },
          Fields = ["category", "chunk_text"],
      }
  );

  Console.WriteLine(response);
  ```

  ```shell curl theme={null}
  INDEX_HOST="INDEX_HOST"
  NAMESPACE="YOUR_NAMESPACE"
  PINECONE_API_KEY="YOUR_API_KEY"

  curl "https://$INDEX_HOST/records/namespaces/$NAMESPACE/search" \
    -H "Accept: application/json" \
    -H "Content-Type: application/json" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-API-Version: unstable" \
    -d '{
          "query": {
              "inputs": {"text": "Disease prevention"},
              "top_k": 2
          },
          "fields": ["category", "chunk_text"]
       }'
  ```
</CodeGroup>

The response will look as follows. Each record is returned with a similarity score that represents its distance to the query vector, calculated according to the [similarity metric](/guides/index-data/create-an-index#similarity-metrics) for the index.

<CodeGroup>
  ```python Python theme={null}
  {'result': {'hits': [{'_id': 'rec3',
                        '_score': 0.8204272389411926,
                        'fields': {'category': 'immune system',
                                   'chunk_text': 'Rich in vitamin C and other '
                                                 'antioxidants, apples '
                                                 'contribute to immune health '
                                                 'and may reduce the risk of '
                                                 'chronic diseases.'}},
                       {'_id': 'rec1',
                        '_score': 0.7931625843048096,
                        'fields': {'category': 'digestive system',
                                   'chunk_text': 'Apples are a great source of '
                                                 'dietary fiber, which supports '
                                                 'digestion and helps maintain a '
                                                 'healthy gut.'}}]},
   'usage': {'embed_total_tokens': 8, 'read_units': 6}}
  ```

  ```javascript JavaScript theme={null}
  {
    result: { 
      hits: [ 
        {
          _id: 'rec3',
          _score: 0.82042724,
          fields: {
            category: 'immune system',
            chunk_text: 'Rich in vitamin C and other antioxidants, apples contribute to immune health and may reduce the risk of chronic diseases.'
          }
        },
        {
          _id: 'rec1',
          _score: 0.7931626,
          fields: {
            category: 'digestive system',
            chunk_text: 'Apples are a great source of dietary fiber, which supports digestion and helps maintain a healthy gut.'
          }
        }
      ]
    },
    usage: { 
      readUnits: 6, 
      embedTotalTokens: 8 
    }
  }
  ```

  ```java Java theme={null}
  class SearchRecordsResponse {
      result: class SearchRecordsResponseResult {
          hits: [class Hit {
              id: rec3
              score: 0.8204272389411926
              fields: {category=immune system, chunk_text=Rich in vitamin C and other antioxidants, apples contribute to immune health and may reduce the risk of chronic diseases.}
              additionalProperties: null
          }, class Hit {
              id: rec1
              score: 0.7931625843048096
              fields: {category=endocrine system, chunk_text=Apples are a great source of dietary fiber, which supports digestion and helps maintain a healthy gut.}
              additionalProperties: null
          }]
          additionalProperties: null
      }
      usage: class SearchUsage {
          readUnits: 6
          embedTotalTokens: 13
      }
      additionalProperties: null
  }
  ```

  ```go Go theme={null}
  {
    "result": {
      "hits": [
        {
          "_id": "rec3",
          "_score": 0.82042724,
          "fields": {
            "category": "immune system",
            "chunk_text": "Rich in vitamin C and other antioxidants, apples contribute to immune health and may reduce the risk of chronic diseases."
          }
        },
        {
          "_id": "rec1",
          "_score": 0.7931626,
          "fields": {
            "category": "digestive system",
            "chunk_text": "Apples are a great source of dietary fiber, which supports digestion and helps maintain a healthy gut."
          }
        }
      ]
    },
    "usage": {
      "read_units": 6,
      "embed_total_tokens": 8
    }
  }
  ```

  ```csharp C# theme={null}
  {
      "result": {
          "hits": [
              {
                  "_id": "rec3",
                  "_score": 0.13741668,
                  "fields": {
                      "category": "immune system",
                      "chunk_text": "Rich in vitamin C and other antioxidants, apples contribute to immune health and may reduce the risk of chronic diseases."
                  }
              },
              {
                  "_id": "rec1",
                  "_score": 0.0023413408,
                  "fields": {
                      "category": "digestive system",
                      "chunk_text": "Apples are a great source of dietary fiber, which supports digestion and helps maintain a healthy gut."
                  }
              }
          ]
      },
      "usage": {
          "read_units": 6,
          "embed_total_tokens": 5,
          "rerank_units": 1
      }
  }
  ```

  ```json curl theme={null}
   {
      "result": {
          "hits": [
              {
                  "_id": "rec3",
                  "_score": 0.82042724,
                  "fields": {
                      "category": "immune system",
                      "chunk_text": "Rich in vitamin C and other antioxidants, apples contribute to immune health and may reduce the risk of chronic diseases."
                  }
              },
              {
                  "_id": "rec1",
                  "_score": 0.7931626,
                  "fields": {
                      "category": "digestive system",
                      "chunk_text": "Apples are a great source of dietary fiber, which supports digestion and helps maintain a healthy gut."
                  }
              }
          ]
      },
      "usage": {
          "embed_total_tokens": 8,
          "read_units": 6
      }
  }
  ```
</CodeGroup>


## Search with a dense vector

To search a dense index with a dense vector representation of a query, use the [`query`](/reference/api/latest/data-plane/query) operation with the following parameters:

* The `namespace` to query. To use the default namespace, set the namespace to `"__default__"`.
* The `vector` parameter with the dense vector values representing your query.
* The `top_k` parameter with the number of results to return.
* Optionally, you can set `include_values` and/or `include_metadata` to `true` to include the vector values and/or metadata of the matching records in the response. However, when querying with `top_k` over 1000, avoid returning vector data or metadata for optimal performance.

For example, the following code uses a dense vector representation of the query “Disease prevention” to search for the 3 most semantically similar records in the `example-namespaces` namespace:

<CodeGroup>
  ```Python Python theme={null}
  from pinecone.grpc import PineconeGRPC as Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  # To get the unique host for an index, 
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  index = pc.Index(host="INDEX_HOST")

  index.query(
      namespace="example-namespace",
      vector=[0.0236663818359375,-0.032989501953125, ..., -0.01041412353515625,0.0086669921875], 
      top_k=3,
      include_metadata=True,
      include_values=False
  )
  ```

  ```JavaScript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({ apiKey: "YOUR_API_KEY" })

  // To get the unique host for an index, 
  // see https://docs.pinecone.io/guides/manage-data/target-an-index
  const index = pc.index("INDEX_NAME", "INDEX_HOST")

  const queryResponse = await index.namespace('example-namespace').query({
      vector: [0.0236663818359375,-0.032989501953125,...,-0.01041412353515625,0.0086669921875],
      topK: 3,
      includeValues: false,
      includeMetadata: true,
  });
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Index;
  import io.pinecone.configs.PineconeConfig;
  import io.pinecone.configs.PineconeConnection;
  import io.pinecone.unsigned_indices_model.QueryResponseWithUnsignedIndices;

  import java.util.Arrays;
  import java.util.List;

  public class QueryExample {
      public static void main(String[] args) {
          PineconeConfig config = new PineconeConfig("YOUR_API_KEY");
          // To get the unique host for an index, 
          // see https://docs.pinecone.io/guides/manage-data/target-an-index
          config.setHost("INDEX_HOST");
          PineconeConnection connection = new PineconeConnection(config);
          Index index = new Index(connection, "INDEX_NAME");
          List<Float> query = Arrays.asList(0.0236663818359375f, -0.032989501953125f, ..., -0.01041412353515625f, 0.0086669921875f);
          QueryResponseWithUnsignedIndices queryResponse = index.query(3, query, null, null, null, "example-namespace", null, false, true);
          System.out.println(queryResponse);
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

      // To get the unique host for an index, 
      // see https://docs.pinecone.io/guides/manage-data/target-an-index
      idxConnection, err := pc.Index(pinecone.NewIndexConnParams{Host: "INDEX_HOST", Namespace: "example-namespace"})
      if err != nil {
          log.Fatalf("Failed to create IndexConnection for Host: %v", err)
    	}

      queryVector := []float32{0.0236663818359375,-0.032989501953125,...,-0.01041412353515625,0.0086669921875}

      res, err := idxConnection.QueryByVectorValues(ctx, &pinecone.QueryByVectorValuesRequest{
          Vector:          queryVector,
          TopK:            3,
          IncludeValues:   false,
          includeMetadata: true,
      })
      if err != nil {
          log.Fatalf("Error encountered when querying by vector: %v", err)
      } else {
          fmt.Printf(prettifyStruct(res))
      }
  }
  ```

  ```csharp C# theme={null}
  using Pinecone;

  var pinecone = new PineconeClient("YOUR_API_KEY");

  // To get the unique host for an index, 
  // see https://docs.pinecone.io/guides/manage-data/target-an-index
  var index = pinecone.Index(host: "INDEX_HOST");

  var queryResponse = await index.QueryAsync(new QueryRequest {
      Vector = new[] { 0.0236663818359375f ,-0.032989501953125f, ..., -0.01041412353515625f, 0.0086669921875f },
      Namespace = "example-namespace",
      TopK = 3,
      IncludeMetadata = true,
  });

  Console.WriteLine(queryResponse);
  ```

  ```bash curl theme={null}
  # To get the unique host for an index,
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="INDEX_HOST"

  curl "https://$INDEX_HOST/query" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H 'Content-Type: application/json' \
    -H "X-Pinecone-API-Version: 2025-04" \
    -d '{
          "vector": [0.0236663818359375,-0.032989501953125,...,-0.01041412353515625,0.0086669921875],
          "namespace": "example-namespace",
          "topK": 3,
          "includeMetadata": true,
          "includeValues": false
      }'
  ```
</CodeGroup>

The response will look as follows. Each record is returned with a similarity score that represents its distance to the query vector, calculated according to the [similarity metric](/guides/index-data/create-an-index#similarity-metrics) for the index.

<CodeGroup>
  ```python Python theme={null}
  {'matches': [{'id': 'rec3',
                'metadata': {'category': 'immune system',
                             'chunk_text': 'Rich in vitamin C and other '
                                            'antioxidants, apples contribute to '
                                            'immune health and may reduce the '
                                            'risk of chronic diseases.'},
                'score': 0.82026422,
                'values': []},
               {'id': 'rec1',
                'metadata': {'category': 'digestive system',
                             'chunk_text': 'Apples are a great source of '
                                            'dietary fiber, which supports '
                                            'digestion and helps maintain a '
                                            'healthy gut.'},
                'score': 0.793068111,
                'values': []},
               {'id': 'rec4',
                'metadata': {'category': 'endocrine system',
                             'chunk_text': 'The high fiber content in apples '
                                            'can also help regulate blood sugar '
                                            'levels, making them a favorable '
                                            'snack for people with diabetes.'},
                'score': 0.780169606,
                'values': []}],
   'namespace': 'example-namespace',
   'usage': {'read_units': 6}}
  ```

  ```JavaScript JavaScript theme={null}
  {
    matches: [
      {
        id: 'rec3',
        score: 0.819709897,
        values: [],
        sparseValues: undefined,
        metadata: [Object]
      },
      {
        id: 'rec1',
        score: 0.792900264,
        values: [],
        sparseValues: undefined,
        metadata: [Object]
      },
      {
        id: 'rec4',
        score: 0.780068815,
        values: [],
        sparseValues: undefined,
        metadata: [Object]
      }
    ],
    namespace: 'example-namespace',
    usage: { readUnits: 6 }
  }
  ```

  ```java Java theme={null}
  class QueryResponseWithUnsignedIndices {
      matches: [ScoredVectorWithUnsignedIndices {
          score: 0.8197099
          id: rec3
          values: []
          metadata: fields {
            key: "category"
            value {
              string_value: "immune system"
            }
          }
          fields {
            key: "chunk_text"
            value {
              string_value: "Rich in vitamin C and other antioxidants, apples contribute to immune health and may reduce the risk of chronic diseases."
            }
          }
          
          sparseValuesWithUnsignedIndices: SparseValuesWithUnsignedIndices {
              indicesWithUnsigned32Int: []
              values: []
          }
      }, ScoredVectorWithUnsignedIndices {
          score: 0.79290026
          id: rec1
          values: []
          metadata: fields {
            key: "category"
            value {
              string_value: "digestive system"
            }
          }
          fields {
            key: "chunk_text"
            value {
              string_value: "Apples are a great source of dietary fiber, which supports digestion and helps maintain a healthy gut."
            }
          }
          
          sparseValuesWithUnsignedIndices: SparseValuesWithUnsignedIndices {
              indicesWithUnsigned32Int: []
              values: []
          }
      }, ScoredVectorWithUnsignedIndices {
          score: 0.7800688
          id: rec4
          values: []
          metadata: fields {
            key: "category"
            value {
              string_value: "endocrine system"
            }
          }
          fields {
            key: "chunk_text"
            value {
              string_value: "The high fiber content in apples can also help regulate blood sugar levels, making them a favorable snack for people with diabetes."
            }
          }
          
          sparseValuesWithUnsignedIndices: SparseValuesWithUnsignedIndices {
              indicesWithUnsigned32Int: []
              values: []
          }
      }]
      namespace: example-namespace
      usage: read_units: 6

  }
  ```

  ```go Go theme={null}
  {
    "matches": [
      {
        "vector": {
          "id": "rec3",
          "metadata": {
            "category": "immune system",
            "chunk_text": "Rich in vitamin C and other antioxidants, apples contribute to immune health and may reduce the risk of chronic diseases."
          }
        },
        "score": 0.8197099
      },
      {
        "vector": {
          "id": "rec1",
          "metadata": {
            "category": "digestive system",
            "chunk_text": "Apples are a great source of dietary fiber, which supports digestion and helps maintain a healthy gut."
          }
        },
        "score": 0.79290026
      },
      {
        "vector": {
          "id": "rec4",
          "metadata": {
            "category": "endocrine system",
            "chunk_text": "The high fiber content in apples can also help regulate blood sugar levels, making them a favorable snack for people with diabetes."
          }
        },
        "score": 0.7800688
      }
    ],
    "usage": {
      "read_units": 6
    },
    "namespace": "example-namespace"
  }
  ```

  ```csharp C# theme={null}
  {
    "results": [],
    "matches": [
      {
        "id": "rec3",
        "score": 0.8197099,
        "values": [],
        "metadata": {
          "category": "immune system",
          "chunk_text": "Rich in vitamin C and other antioxidants, apples contribute to immune health and may reduce the risk of chronic diseases."
        }
      },
      {
        "id": "rec1",
        "score": 0.79290026,
        "values": [],
        "metadata": {
          "category": "digestive system",
          "chunk_text": "Apples are a great source of dietary fiber, which supports digestion and helps maintain a healthy gut."
        }
      },
      {
        "id": "rec4",
        "score": 0.7800688,
        "values": [],
        "metadata": {
          "category": "endocrine system",
          "chunk_text": "The high fiber content in apples can also help regulate blood sugar levels, making them a favorable snack for people with diabetes."
        }
      }
    ],
    "namespace": "example-namespace",
    "usage": {
      "readUnits": 6
    }
  }
  ```

  ```json curl theme={null}
  {
      "results": [],
      "matches": [
          {
              "id": "rec3",
              "score": 0.820593238,
              "values": [],
              "metadata": {
                  "category": "immune system",
                  "chunk_text": "Rich in vitamin C and other antioxidants, apples contribute to immune health and may reduce the risk of chronic diseases."
              }
          },
          {
              "id": "rec1",
              "score": 0.792266726,
              "values": [],
              "metadata": {
                  "category": "digestive system",
                  "chunk_text": "Apples are a great source of dietary fiber, which supports digestion and helps maintain a healthy gut."
              }
          },
          {
              "id": "rec4",
              "score": 0.780045748,
              "values": [],
              "metadata": {
                  "category": "endocrine system",
                  "chunk_text": "The high fiber content in apples can also help regulate blood sugar levels, making them a favorable snack for people with diabetes."
              }
          }
      ],
      "namespace": "example-namespace",
      "usage": {
          "readUnits": 6
      }
  }
  ```
</CodeGroup>


## Search with a record ID

When you search with a record ID, Pinecone uses the dense vector associated with the record as the query. To search a dense index with a record ID, use the [`query`](/reference/api/latest/data-plane/query) operation with the following parameters:

* The `namespace` to query. To use the default namespace, set the namespace to `"__default__"`.
* The `id` parameter with the unique record ID containing the vector to use as the query.
* The `top_k` parameter with the number of results to return.
* Optionally, you can set `include_values` and/or `include_metadata` to `true` to include the vector values and/or metadata of the matching records in the response. However, when querying with `top_k` over 1000, avoid returning vector data or metadata for optimal performance.

For example, the following code uses an ID to search for the 3 records in the `example-namespace` namespace that are most semantically similar to the dense vector in the record:

<CodeGroup>
  ```Python Python theme={null}
  from pinecone.grpc import PineconeGRPC as Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  # To get the unique host for an index, 
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  index = pc.Index(host="INDEX_HOST")

  index.query(
      namespace="example-namespace",
      id="rec2", 
      top_k=3,
      include_metadata=True,
      include_values=False
  )
  ```

  ```JavaScript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({ apiKey: "YOUR_API_KEY" })

  // To get the unique host for an index, 
  // see https://docs.pinecone.io/guides/manage-data/target-an-index
  const index = pc.index("INDEX_NAME", "INDEX_HOST")

  const queryResponse = await index.namespace('example-namespace').query({
      id: 'rec2',
      topK: 3,
      includeValues: false,
      includeMetadata: true,
  });
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Index;
  import io.pinecone.configs.PineconeConfig;
  import io.pinecone.configs.PineconeConnection;
  import io.pinecone.unsigned_indices_model.QueryResponseWithUnsignedIndices;

  public class QueryExample {
      public static void main(String[] args) {
          PineconeConfig config = new PineconeConfig("YOUR_API_KEY");
          // To get the unique host for an index, 
          // see https://docs.pinecone.io/guides/manage-data/target-an-index
          config.setHost("INDEX_HOST");
          PineconeConnection connection = new PineconeConnection(config);
          Index index = new Index(connection, "INDEX_NAME");
          QueryResponseWithUnsignedIndices queryRespone = index.queryByVectorId(3, "rec2", "example-namespace", null, false, true);
          System.out.println(queryResponse);
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

      // To get the unique host for an index, 
      // see https://docs.pinecone.io/guides/manage-data/target-an-index
      idxConnection, err := pc.Index(pinecone.NewIndexConnParams{Host: "INDEX_HOST", Namespace: "example-namespace"})
      if err != nil {
          log.Fatalf("Failed to create IndexConnection for Host: %v", err)
    	}

      vectorId := "rec2"
      res, err := idxConnection.QueryByVectorId(ctx, &pinecone.QueryByVectorIdRequest{
          VectorId:      vectorId,
          TopK:          3,
          IncludeValues: false,
          IncludeMetadata: true,
      })
      if err != nil {
          log.Fatalf("Error encountered when querying by vector ID `%v`: %v", vectorId, err)
      } else {
          fmt.Printf(prettifyStruct(res.Matches))
      }
  }
  ```

  ```csharp C# theme={null}
  using Pinecone;

  var pinecone = new PineconeClient("YOUR_API_KEY");

  // To get the unique host for an index, 
  // see https://docs.pinecone.io/guides/manage-data/target-an-index
  var index = pinecone.Index(host: "INDEX_HOST");

  var queryResponse = await index.QueryAsync(new QueryRequest {
      Id = "rec2",
      Namespace = "example-namespace",
      TopK = 3,
      IncludeValues = false,
      IncludeMetadata = true
  });

  Console.WriteLine(queryResponse);
  ```

  ```bash curl theme={null}
  # To get the unique host for an index,
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="INDEX_HOST"

  curl "https://$INDEX_HOST/query" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H 'Content-Type: application/json' \
    -H "X-Pinecone-API-Version: 2025-04" \
    -d '{
          "id": "rec2",
          "namespace": "example-namespace",
          "topK": 3,
          "includeMetadata": true,
          "includeValues": false
      }'
  ```
</CodeGroup>


## Parallel queries

Python SDK v6.0.0 and later provide `async` methods for use with [asyncio](https://docs.python.org/3/library/asyncio.html). Async support makes it possible to use Pinecone with modern async web frameworks such as FastAPI, Quart, and Sanic, and can significantly increase the efficiency of running queries in parallel. For more details, see the [Async requests](/reference/python-sdk#async-requests).



# Configure an index
Source: https://docs.pinecone.io/reference/api/2025-04/control-plane/configure_index

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-04/db_control_2025-04.oas.yaml patch /indexes/{index_name}
Configure an existing index. For serverless indexes, you can configure index deletion protection, tags, and integrated inference embedding settings for the index. For pod-based indexes, you can configure the pod size, number of replicas, tags, and index deletion protection.

It is not possible to change the pod type of a pod-based index. However, you can create a collection from a pod-based index and then [create a new pod-based index with a different pod type](http://docs.pinecone.io/guides/indexes/pods/create-a-pod-based-index#create-a-pod-index-from-a-collection) from the collection. For guidance and examples, see [Configure an index](http://docs.pinecone.io/guides/indexes/pods/manage-pod-based-indexes).

<RequestExample>
  ```python Python theme={null}
  from pinecone import Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  pc.configure_index(
    name="docs-example", 
    deletion_protection="enabled",
    tags={"example": "tag", "environment": "development"}
  )
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone'

  const pinecone = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  await pinecone.configureIndex(
    'docs-example', 
    { 
      deletionProtection: 'enabled', 
      tags: { 
        example: 'tag', 
        environment: 'development' 
      } 
    }
  );
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Pinecone;
  import org.openapitools.db_control.client.model.*;
  import java.util.HashMap;

  public class ConfigureIndexExample {
    public static void main(String[] args) throws Exception {
      Pinecone pc = new Pinecone.Builder("YOUR_API_KEY").build();

      HashMap<String, String> tags = new HashMap<>();
      tags.put("example", "tag");
      tags.put("environment", "development");

      IndexModel indexList = pc.configureServerlessIndex(
        "docs-example",
        DeletionProtection.ENABLED,
        tags,
        null
      );
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

      idx, err := pc.ConfigureIndex(ctx, "docs-example", pinecone.ConfigureIndexParams{
        DeletionProtection: "enabled",
        Tags: map[string]string{
          "example": "tag",
          "environment": "development",
        },
      })
    	if err != nil {
        log.Fatalf("Failed to configure index \"%v\": %v", idx.Name, err)
      } else {
        fmt.Printf("Successfully configured index \"%v\"", idx.Name)
      }
  }
  ```

  ```csharp C# theme={null}
  using Pinecone;

  var pinecone = new PineconeClient("YOUR_API_KEY");
  var request = new ConfigureIndexRequest
  {
    DeletionProtection = DeletionProtection.Enabled,
    Tags = new Dictionary<string, string>
    {
      { "example", "tag" },
      { "environment", "development" }
    }
  };
  var index = await pinecone.ConfigureIndexAsync("docs-example", request);
  ```

  ```shell curl theme={null}
  PROJECT_NAME="YOUR_PROJECT_NAME"
  PINECONE_API_KEY="YOUR_API_KEY"

  curl -X PATCH "https://api.pinecone.io/indexes/$INDEX_NAME" \
       -H "Content-Type: application/json" \
       -H "Api-Key: $PINECONE_API_KEY" \
       -H "X-Pinecone-API-Version: 2025-04" \
       -d '{
              "deletion_protection": "enabled",
               "tags": {
                 "example": "tag",
                 "environment": "development"
               }
           }'
           
  ```

  ```bash CLI theme={null}
  # Target the project that contains the index you'd 
  # like to configure.
  pc target -o "example-org" -p "example-project"
  # Configure the index.
  pc index configure \
    --name "docs-example" \
    --deletion_protection "enabled" 
  ```
</RequestExample>

<ResponseExample>
  ```json Response theme={null}
  {
    "name": "docs-example",
    "vector_type": "dense",
    "metric": "cosine",
    "dimension": 1536,
    "status": {
      "ready": true,
      "state": "Ready"
    },
    "host": "docs-example-1c6ab6aa.svc.aped-4627-b74a.pinecone.io",
    "spec": {
      "serverless": {
        "region": "us-east-1",
        "cloud": "aws"
      }
    },
    "deletion_protection": "enabled",
    "tags": {
      "environment": "development",
      "example": "tag"
    }
  }
  ```
</ResponseExample>



# Create an index with integrated embedding
Source: https://docs.pinecone.io/reference/api/2025-04/control-plane/create_for_model

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-04/db_control_2025-04.oas.yaml post /indexes/create-for-model
Create an index with integrated embedding.

With this type of index, you provide source text, and Pinecone uses a [hosted embedding model](https://docs.pinecone.io/guides/index-data/create-an-index#embedding-models) to convert the text automatically during [upsert](https://docs.pinecone.io/reference/api/2025-01/data-plane/upsert_records) and [search](https://docs.pinecone.io/reference/api/2025-01/data-plane/search_records).

For guidance and examples, see [Create an index](https://docs.pinecone.io/guides/index-data/create-an-index#integrated-embedding).

<RequestExample>
  ```python Python theme={null}
  # pip install --upgrade pinecone
  from pinecone import Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  index_name = "integrated-dense-py"

  index_model = pc.create_index_for_model(
      name=index_name,
      cloud="aws",
      region="us-east-1",
      embed={
          "model":"llama-text-embed-v2",
          "field_map":{"text": "chunk_text"}
      }
  )

  # Import specific classes to get type hints and autocompletions
  from pinecone import CloudProvider, AwsRegion, IndexEmbed, EmbedModel

  index_model = pc.create_index_for_model(
      name=index_name,
      cloud=CloudProvider.AWS,
      region=AwsRegion.US_EAST_1,
      embed=IndexEmbed(
          model=EmbedModel.Multilingual_E5_Large,
          field_map={"text": "chunk_text"},
          metric='cosine'
      )
  )
  ```

  ```javascript JavaScript theme={null}
  // npm install @pinecone-database/pinecone
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  await pc.createIndexForModel({
    name: 'integrated-dense-js',
    cloud: 'aws',
    region: 'us-east-1',
    embed: {
      model: 'llama-text-embed-v2',
      fieldMap: { text: 'chunk_text' },
    },
    waitUntilReady: true,
  });
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Pinecone;
  import org.openapitools.db_control.client.ApiException;
  import org.openapitools.db_control.client.model.CreateIndexForModelRequest;
  import org.openapitools.db_control.client.model.CreateIndexForModelRequestEmbed;
  import org.openapitools.db_control.client.model.DeletionProtection;
  import org.openapitools.db_control.client.model.IndexModel;

  import java.util.HashMap;
  import java.util.Map;

  public class CreateIntegratedIndex {
      public static void main(String[] args) throws ApiException {
          Pinecone pc = new Pinecone.Builder("YOUR_API_KEY").build();
          String indexName = "integrated-dense-java";
          String region = "us-east-1";
          HashMap<String, String> fieldMap = new HashMap<>();
          fieldMap.put("text", "chunk_text");
          CreateIndexForModelRequestEmbed embed = new CreateIndexForModelRequestEmbed()
                  .model("llama-text-embed-v2")
                  .fieldMap(fieldMap);
          Map<String, String> tags = new HashMap<>();
          tags.put("environment", "development");
          IndexModel index = pc.createIndexForModel(
                  indexName,
                  CreateIndexForModelRequest.CloudEnum.AWS,
                  region,
                  embed,
                  DeletionProtection.DISABLED,
                  tags
          );
          System.out.println(index);
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

    	indexName := "integrated-dense-go"
      DeletionProtection: &deletionProtection,

      index, err := pc.CreateIndexForModel(ctx, &pinecone.CreateIndexForModelRequest{
  		Name:   indexName,
  		Cloud:  pinecone.Aws,
  		Region: "us-east-1",
  		Embed: pinecone.CreateIndexForModelEmbed{
  			Model:    "llama-text-embed-v2",
  			FieldMap: map[string]interface{}{"text": "chunk_text"},
  		},
      DeletionProtection: &deletionProtection,
      Tags:   &pinecone.IndexTags{ "environment": "development" },
  	})
      if err != nil {
          log.Fatalf("Failed to create serverless integrated index: %v", idx.Name)
      } else {
          fmt.Printf("Successfully created serverless integrated index: %v", idx.Name)
      }
  }
  ```

  ```csharp C# theme={null}
  using Pinecone;

  var pinecone = new PineconeClient("YOUR_API_KEY");

  var createIndexRequest = await pinecone.CreateIndexForModelAsync(
      new CreateIndexForModelRequest
      {
          Name = "integrated-dense-dotnet",
          Cloud = CreateIndexForModelRequestCloud.Aws,
          Region = "us-east-1",
          Embed = new CreateIndexForModelRequestEmbed
          {
              Model = "llama-text-embed-v2",
              FieldMap = new Dictionary<string, object?>() { { "text", "chunk_text" } },
          },
          DeletionProtection = DeletionProtection.Disabled,
          Tags = new Dictionary<string, string> 
          { 
              { "environment", "development" }
          }
      }
  );
  ```

  ```shell curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl -X POST https://api.pinecone.io/indexes/create-for-model \
       -H "Content-Type: application/json" \
       -H "Api-Key: $PINECONE_API_KEY" \
       -H "X-Pinecone-API-Version: 2025-04" \
       -d '{
             "name": "integrated-dense-curl",
             "cloud": "aws",
             "region": "us-east-1",
             "embed": {
               "model": "llama-text-embed-v2",
               "metric": "cosine",
               "field_map": {
                 "text": "chunk_text"
               },
               "write_parameters": {
                 "input_type": "passage",
                 "truncate": "END"
               },
               "read_parameters": {
                 "input_type": "query",
                 "truncate": "END"
               }
             }
           }'
  ```

  ```bash CLI theme={null}
  # Target the project where you want to create the index.
  pc target -o "example-org" -p "example-project"
  # Create the index.
  pc index create \
    --name "integrated-dense-cli" \
    --dimension 1024 \
    --metric "cosine" \
    --cloud "aws" \
    --region "us-east-1" \
    --model "llama-text-embed-v2" \
    --field_map "text=chunk_text"
  ```
</RequestExample>

<ResponseExample>
  ```python Python theme={null}
  {'deletion_protection': 'disabled',
   'dimension': 1024,
   'embed': {'dimension': 1024,
             'field_map': {'text': 'chunk_text'},
             'metric': 'cosine',
             'model': 'llama-text-embed-v2',
             'read_parameters': {'input_type': 'query', 'truncate': 'END'},
             'write_parameters': {'input_type': 'passage', 'truncate': 'END'}},
   'host': 'integrated-dense-py-govk0nt.svc.aped-4627-b74a.pinecone.io',
   'id': '9dabb7cb-ec0a-4e2e-b79e-c7c997e592ce',
   'metric': 'cosine',
   'name': 'integrated-dense-py',
   'spec': {'serverless': {'cloud': 'aws', 'region': 'us-east-1'}},
   'status': {'ready': True, 'state': 'Ready'},
   'tags': None}
  ```

  ```javascript JavaScript theme={null}
  {
    name: 'integrated-dense-js',
    dimension: 1024,
    metric: 'cosine',
    host: 'integrated-dense-js-govk0nt.svc.aped-4627-b74a.pinecone.io',
    deletionProtection: 'disabled',
    tags: undefined,
    embed: {
      model: 'llama-text-embed-v2',
      metric: 'cosine',
      dimension: 1024,
      vectorType: 'dense',
      fieldMap: { text: 'chunk_text' },
      readParameters: { input_type: 'query', truncate: 'END' },
      writeParameters: { input_type: 'passage', truncate: 'END' }
    },
    spec: { pod: undefined, serverless: { cloud: 'aws', region: 'us-east-1' } },
    status: { ready: true, state: 'Ready' },
    vectorType: 'dense'
  }
  ```

  ```java Java theme={null}
  class IndexModel {
      name: integrated-dense-java
      dimension: 1024
      metric: cosine
      host: integrated-dense-java-govk0nt.svc.aped-4627-b74a.pinecone.io
      deletionProtection: disabled
      tags: {environment=development}
      embed: class ModelIndexEmbed {
          model: llama-text-embed-v2
          metric: cosine
          dimension: 1024
          vectorType: dense
          fieldMap: {text=chunk_text}
          readParameters: {dimension=1024.0, input_type=query, truncate=END}
          writeParameters: {dimension=1024.0, input_type=passage, truncate=END}
          additionalProperties: null
      }
      spec: class IndexModelSpec {
          byoc: null
          pod: null
          serverless: class ServerlessSpec {
              cloud: aws
              region: us-east-1
              additionalProperties: null
          }
          additionalProperties: null
      }
      status: class IndexModelStatus {
          ready: false
          state: Initializing
          additionalProperties: null
      }
      vectorType: dense
      additionalProperties: null
  }
  ```

  ```go Go theme={null}
  {
    "name": "integrated-dense-go",
    "host": "integrated-dense-go-govk0nt.svc.aped-4627-b74a.pinecone.io",
    "metric": "cosine",
    "vector_type": "dense",
    "deletion_protection": "disabled",
    "dimension": 1024,
    "spec": {
      "serverless": {
        "cloud": "aws",
        "region": "us-east-1"
      }
    },
    "status": {
      "ready": true,
      "state": "Ready"
    },
    "embed": {
      "model": "llama-text-embed-v2",
      "dimension": 1024,
      "metric": "cosine",
      "vector_type": "dense",
      "field_map": {
        "text": "chunk_text"
      },
      "read_parameters": {
        "input_type": "query",
        "truncate": "END"
      },
      "write_parameters": {
        "input_type": "passage",
        "truncate": "END"
      }
    }
  }
  ```

  ```csharp C# theme={null}
  {
    "name": "integrated-dense-dotnet",
    "dimension": 1024,
    "metric": "cosine",
    "host": "integrated-dense-dotnet-govk0nt.svc.aped-4627-b74a.pinecone.io",
    "deletion_protection": "disabled",
    "tags": {
      "environment": "development"
    },
    "embed": {
      "model": "llama-text-embed-v2",
      "metric": "cosine",
      "dimension": 1024,
      "vector_type": "dense",
      "field_map": {
        "text": "chunk_text"
      },
      "read_parameters": {
        "dimension": 1024,
        "input_type": "query",
        "truncate": "END"
      },
      "write_parameters": {
        "dimension": 1024,
        "input_type": "passage",
        "truncate": "END"
      }
    },
    "spec": {
      "serverless": {
        "cloud": "aws",
        "region": "us-east-1"
      }
    },
    "status": {
      "ready": true,
      "state": "Ready"
    },
    "vector_type": "dense"
  }
  ```

  ```json curl theme={null}
  {
    "id": "9dabb7cb-ec0a-4e2e-b79e-c7c997e592ce",
    "name": "integrated-dense-curl",
    "metric": "cosine",
    "dimension": 1024,
    "status": {
      "ready": false,
      "state": "Initializing"
    },
    "host": "integrated-dense-curl-govk0nt.svc.aped-4627-b74a.pinecone.io",
    "spec": {
      "serverless": {
        "region": "us-east-1",
        "cloud": "aws"
      }
    },
    "deletion_protection": "disabled",
    "tags": null,
    "embed": {
      "model": "llama-text-embed-v2",
      "field_map": {
        "text": "chunk_text"
      },
      "dimension": 1024,
      "metric": "cosine",
      "write_parameters": {
        "input_type": "passage",
        "truncate": "END"
      },
      "read_parameters": {
        "input_type": "query",
        "truncate": "END"
      }
    }
  }
  ```

  ```text CLI theme={null}
  [SUCCESS] Index integrated-dense-cli created successfully. Run pc index describe --name integrated-dense-cli to check status.


  ATTRIBUTE              VALUE
  Name                   integrated-dense-cli
  Dimension              1024
  Metric                 cosine
  Deletion Protection    disabled
  Vector Type            dense

  State                  Initializing
  Ready                  false
  Host                   integrated-dense-cli-1c6ab6aa.svc.aped-4627-b74a.pinecone.io
  Private Host           <none>

  Spec                   serverless
  Cloud                  aws
  Region                 us-east-1
  Source Collection      <none>

  Model                  llama-text-embed-v2
  Field Map              {"text":"chunk_text"}
  Read Parameters        {"dimension":1024,"input_type":"query","truncate":"END"}
  Write Parameters       {"dimension":1024,"input_type":"passage","truncate":"END"}
  ```
</ResponseExample>



# Create an index
Source: https://docs.pinecone.io/reference/api/2025-04/control-plane/create_index

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-04/db_control_2025-04.oas.yaml post /indexes
Create a Pinecone index. This is where you specify the measure of similarity, the dimension of vectors to be stored in the index, which cloud provider you would like to deploy with, and more.
  
For guidance and examples, see [Create an index](https://docs.pinecone.io/guides/index-data/create-an-index).


<RequestExample>
  ```python Python theme={null}
  # pip install "pinecone[grpc]"
  from pinecone.grpc import PineconeGRPC as Pinecone
  from pinecone import ServerlessSpec

  pc = Pinecone(api_key="YOUR_API_KEY")

  pc.create_index(
    name="docs-example1",
    dimension=1536,
    metric="cosine",
    spec=ServerlessSpec(
      cloud="aws",
      region="us-east-1",
    ),
    deletion_protection="disabled"
  )
  ```

  ```javascript JavaScript theme={null}
  // npm install @pinecone-database/pinecone
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({
    apiKey: 'YOUR_API_KEY'
  });

  await pc.createIndex({
    name: 'docs-example1',
    dimension: 1536,
    metric: 'cosine',
    spec: {
      serverless: {
        cloud: 'aws',
        region: 'us-east-1'
      }
    },
    deletionProtection: 'disabled',
  });
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Pinecone;

  public class CreateServerlessIndexExample {
      public static void main(String[] args) {
          Pinecone pc = new Pinecone.Builder("YOUR_API_KEY").build();
          pc.createServerlessIndex("docs-example1", "cosine", 1536, "aws", "us-east-1", DeletionProtection.disabled);
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

      deletionProtection := pinecone.DeletionProtectionDisabled

      idx, err := pc.CreateServerlessIndex(ctx, &pinecone.CreateServerlessIndexRequest{
          Name:      "docs-example1",
          Dimension: 1536,
          Metric:    pinecone.Cosine,
          Cloud:     pinecone.Aws,
          Region:    "us-east-1",
          DeletionProtection: &deletionProtection,
      })
    	if err != nil {
          log.Fatalf("Failed to create serverless index: %v", err)
      } else {
          fmt.Printf("Successfully created serverless index: %v", idx.Name)
      }
  }
  ```

  ```csharp C# theme={null}
  using Pinecone;

  var pinecone = new PineconeClient("YOUR_API_KEY");

  var createIndexRequest = await pinecone.CreateIndexAsync(new CreateIndexRequest
  {
      Name = "docs-example1",
      Dimension = 1536,
      Metric = MetricType.Cosine,
      Spec = new ServerlessIndexSpec
      {
          Serverless = new ServerlessSpec
          {
              Cloud = ServerlessSpecCloud.Aws,
              Region = "us-east-1",
          }
      },
      DeletionProtection = DeletionProtection.Disabled
  });
  ```

  ```shell curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  # Serverless index
  curl -X POST "https://api.pinecone.io/indexes" \
       -H "Accept: application/json" \
       -H "Content-Type: application/json" \
       -H "Api-Key: $PINECONE_API_KEY" \
       -H "X-Pinecone-API-Version: 2025-04" \
       -d '{
             "name": "docs-example1",
             "vector_type": "dense",
             "dimension": 1536,
             "metric": "cosine",
             "spec": {
                 "serverless": {
                     "cloud": "aws",
                     "region": "us-east-1"
                 }
             },
             "tags": {
                 "example": "tag"
             },
             "deletion_protection": "disabled"
           }'

  # BYOC index
  curl -X POST"https://api.pinecone.io/indexes" \
       -H "Accept: application/json" \
       -H "Content-Type: application/json" \
       -H "Api-Key: $PINECONE_API_KEY" \
       -H "X-Pinecone-API-Version: 2025-04" \
       -d '{
             "name": "example-byoc-index",
             "vector_type": "dense",
             "dimension": 1536,
             "metric": "cosine",
             "spec": {
                 "byoc": {
                     "environment": "aws-us-east-1-b921"
                 }
             },
             "tags": {
                 "example": "tag"
             },
             "deletion_protection": "disabled"
           }'
  ```

  ```bash CLI theme={null}
  # Target the project where you'd like to create the index.
  pc target -o "example-org" -p "example-project"
  # Create the index.
  pc index create \
    --name "docs-example1" \
    --dimension 1536 \
    --metric "cosine" \
    --cloud "aws" \
    --region "us-east-1" \
    --deletion_protection "disabled" \
    --tags "example=tag,example2=tag2"
  ```
</RequestExample>

<ResponseExample>
  ```shell Response theme={null}
  # Serverless index
  {
      "name": "docs-example1",
      "vector_type": "dense",
      "metric": "cosine",
      "dimension": 1536,
      "status": {
          "ready": true,
          "state": "Ready"
      },
      "host": "example-serverless-index-govk0nt.svc.aped-4627-b74a.pinecone.io",
      "spec": {
          "serverless": {
              "region": "us-east-1",
              "cloud": "aws"
          }
      },
      "deletion_protection": "disabled",
      "tags": {
          "example": "tag"
      }
  }

  # BYOC index
  {
      "name": "example-byoc-index",
      "vector_type": "dense",
      "metric": "cosine",
      "dimension": 1536,
      "status": {
          "ready": true,
          "state": "Ready"
      },
      "host": "example-byoc-index-govk0nt.svc.private.aped-4627-b74a.pinecone.io",
      "spec": {
          "byoc": {
              "environment": "aws-us-east-1-b921"
          }
      },
      "deletion_protection": "disabled",
      "tags": {
          "example": "tag"
      }
  }
  ```
</ResponseExample>



# Delete an index
Source: https://docs.pinecone.io/reference/api/2025-04/control-plane/delete_index

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-04/db_control_2025-04.oas.yaml delete /indexes/{index_name}
Delete an existing index.

<RequestExample>
  ```python Python theme={null}
  # pip install "pinecone[grpc]"
  from pinecone.grpc import PineconeGRPC as Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")
  pc.delete_index(name="docs-example")
  ```

  ```javascript JavaScript theme={null}
  // npm install @pinecone-database/pinecone
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({
    apiKey: 'YOUR_API_KEY'
  });

  await pc.deleteIndex('docs-example');
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Pinecone;

  public class DeleteIndexExample {
      public static void main(String[] args) {
          Pinecone pc = new Pinecone.Builder("YOUR_API_KEY").build();
          pc.deleteIndex("docs-example");
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

      indexName := "docs-example"

      err = pc.DeleteIndex(ctx, indexName)
      if err != nil {
          log.Fatalf("Failed to delete index: %v", err)
      } else {
          fmt.Println("Index \"%v\" deleted successfully", indexName)
      }
  }
  ```

  ```csharp C# theme={null}
  using Pinecone;

  var pinecone = new PineconeClient("YOUR_API_KEY");
  await pinecone.DeleteIndexAsync("docs-example");
  ```

  ```shell curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl -X DELETE "https://api.pinecone.io/indexes/docs-example" \
       -H "Api-Key: $PINECONE_API_KEY" \
       -H "X-Pinecone-API-Version: 2025-04"
  ```

  ```bash CLI theme={null}
  # Target the project that contains the index
  pc target -o "example-org" -p "example-project"
  # Delete the index.
  pc index delete --name "docs-example"
  ```
</RequestExample>

<ResponseExample />



# Describe an index
Source: https://docs.pinecone.io/reference/api/2025-04/control-plane/describe_index

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-04/db_control_2025-04.oas.yaml get /indexes/{index_name}
Get a description of an index.

<RequestExample>
  ```python Python theme={null}
  # pip install "pinecone[grpc]"
  from pinecone.grpc import PineconeGRPC as Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")
  pc.describe_index(name="movie-recommendations")
  ```

  ```javascript JavaScript theme={null}
  // npm install @pinecone-database/pinecone
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });
  await pc.describeIndex('movie-recommendations');
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Pinecone;
  import org.openapitools.db_control.client.model.*;

  public class DescribeIndexExample {
      public static void main(String[] args) {
          Pinecone pc = new Pinecone.Builder("YOURE_API_KEY").build();
          IndexModel indexModel = pc.describeIndex("movie-recommendations");
          System.out.println(indexModel);
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

      idx, err := pc.DescribeIndex(ctx, "movie-recommendations")
      if err != nil {
          log.Fatalf("Failed to describe index \"%v\": %v", idx.Name, err)
      } else {
          fmt.Printf("index: %v\n", prettifyStruct(idx))
      }
  }
  ```

  ```csharp C# theme={null}
  using Pinecone;

  var pinecone = new PineconeClient("YOUR_API_KEY");
  var indexModel = await pinecone.DescribeIndexAsync("");
  Console.WriteLine(indexModel);
  ```

  ```shell curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl -X GET "https://api.pinecone.io/indexes/movie-recommendations" \
       -H "Api-Key: $PINECONE_API_KEY" \
       -H "X-Pinecone-API-Version: 2025-04"
  ```

  ```bash CLI theme={null}
  # Target the project that contains the index
  pc target -o "example-org" -p "example-project"
  # Describe the index.
  pc index describe --name "movie-recommendations"
  ```
</RequestExample>

<ResponseExample>
  ```Python Python theme={null}
  {'deletion_protection': 'disabled',
   'dimension': 1536,
   'host': 'movie-recommendations-1c6ab6aa.svc.aped-4627-b74a.pinecone.io',
   'metric': 'cosine',
   'name': 'movie-recommendations',
   'spec': {'serverless': {'cloud': 'aws', 'region': 'us-east-1'}},
   'status': {'ready': True, 'state': 'Ready'},
   'tags': {'environment': 'development'},
   'vector_type': 'dense'}
  ```

  ```javaScript JavaScript theme={null}
  {
    name: 'movie-recommendations',
    dimension: 1536,
    metric: 'cosine',
    host: 'movie-recommendations-1c6ab6aa.svc.aped-4627-b74a.pinecone.io',
    deletionProtection: 'disabled',
    tags: { environment: 'development', example: 'tag' },
    embed: undefined,
    spec: { pod: undefined, serverless: { cloud: 'aws', region: 'us-east-1' } },
    status: { ready: true, state: 'Ready' },
    vectorType: 'dense'
  }
  ```

  ```java Java theme={null}
  class IndexModel {
      name: movie-recommendations
      dimension: 1536
      metric: cosine
      host: movie-recommendations-1c6ab6aa.svc.aped-4627-b74a.pinecone.io
      deletionProtection: disabled
      tags: {environment=development}
      embed: null
      spec: class IndexModelSpec {
          pod: null
          serverless: class ServerlessSpec {
              cloud: aws
              region: us-east-1
              additionalProperties: null
          }
          additionalProperties: null
      }
      status: class IndexModelStatus {
          ready: true
          state: Ready
          additionalProperties: null
      }
      vectorType: dense
      additionalProperties: null
  }
  ```

  ```go Go theme={null}
  index: {
    "name": "movie-recommendations",
    "host": "movie-recommendations-1c6ab6aa.svc.aped-4627-b74a.pinecone.io",
    "metric": "cosine",
    "vector_type": "dense",
    "deletion_protection": "disabled",
    "dimension": 1536,
    "spec": {
      "serverless": {
        "cloud": "aws",
        "region": "us-east-1"
      }
    },
    "status": {
      "ready": true,
      "state": "Ready"
    },
    "tags": {
      "environment": "development"
    }
  }
  ```

  ```csharp C# theme={null}
  {
    "name": "movie-recommendations",
    "dimension": 1536,
    "metric": "cosine",
    "host": "movie-recommendations-1c6ab6aa.svc.aped-4627-b74a.pinecone.io",
    "deletion_protection": "disabled",
    "tags": {
      "environment": "development"
    },
    "spec": {
      "serverless": {
        "cloud": "aws",
        "region": "us-east-1"
      }
    },
    "status": {
      "ready": true,
      "state": "Ready"
    },
    "vector_type": "dense"
  }
  ```

  ```json curl theme={null}
  {
    "name": "movie-recommendations",
    "vector_type": "dense",
    "metric": "cosine",
    "dimension": 1536,
    "status": {
      "ready": true,
      "state": "Ready"
    },
    "host": "movie-recommendations-1c6ab6aa.svc.aped-4627-b74a.pinecone.io",
    "spec": {
      "serverless": {
        "region": "us-east-1",
        "cloud": "aws"
      }
    },
    "deletion_protection": "disabled",
    "tags": {
      "environment": "development"
    }
  }
  ```

  ```text CLI theme={null}
  ATTRIBUTE              VALUE
  Name                   movie-recommendations
  Dimension              1536
  Metric                 cosine
  Deletion Protection    disabled
  Vector Type            dense

  State                  Ready
  Ready                  true
  Host                   movie-recommendations-1c6ab6aa.svc.aped-4627-b74a.pinecone.io
  Private Host           <none>

  Spec                   serverless
  Cloud                  aws
  Region                 us-east-1
  Source Collection      <none>
  ```
</ResponseExample>



# List indexes
Source: https://docs.pinecone.io/reference/api/2025-04/control-plane/list_indexes

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-04/db_control_2025-04.oas.yaml get /indexes
List all indexes in a project.

<RequestExample>
  ```Python Python theme={null}
  from pinecone import Pinecone

  pc = Pinecone(api_key='YOUR_API_KEY')
  index_list = pc.list_indexes()
  print(index_list)
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });
  const indexList = await pc.listIndexes();
  console.log(JSON.stringify(indexList, null, 2));
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Pinecone;
  import org.openapitools.db_control.client.model.*;

  public class ListIndexesExample {
  	public static void main(String[] args) {
  		Pinecone pc = new Pinecone.Builder("YOUR_API_KEY").build();
  		IndexList indexList = pc.listIndexes();
  		System.out.println(indexList.toJson());
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
  	"os"

  	"github.com/pinecone-io/go-pinecone/v4/pinecone"
  )

  func prettifyStruct(obj interface{}) string {
  	bytes, _ := json.MarshalIndent(obj, "", "  ")
  	return string(bytes)
  }

  func main() {
  	ctx := context.Background()

  	pc, err := pinecone.NewClient(pinecone.NewClientParams{
  		ApiKey: os.Getenv("PINECONE_API_KEY"),
  	})
  	if err != nil {
  		log.Fatalf("Failed to create Client: %v", err)
  	}

  	idxs, err := pc.ListIndexes(ctx)
  	if err != nil {
  		log.Fatalf("Failed to list indexes: %v", err)
  	} else {
  		fmt.Printf("%s\n", prettifyStruct(idxs))
  	}
  }
  ```

  ```csharp C# theme={null}
  using Pinecone;

  var pinecone = new PineconeClient("YOUR_API_KEY");
  var indexList = await pinecone.ListIndexesAsync();
  Console.WriteLine(indexList);
  ```

  ```shell curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl -X GET "https://api.pinecone.io/indexes" \
       -H "Api-Key: $PINECONE_API_KEY" \
       -H "X-Pinecone-API-Version: 2025-04"
  ```

  ```bash CLI theme={null}
  # Target the project for which you want to list indexes.
  pc target -o "example-org" -p "example-project"
  # List all indexes in the project
  pc index list
  ```
</RequestExample>

<ResponseExample>
  ```python Python theme={null}
  [
    {
      "name": "example-index",
      "metric": "cosine",
      "host": "example-index-fa77d8e.svc.aped-4627-b74a.pinecone.io",
      "spec": {
        "serverless": {
          "cloud": "aws",
          "region": "us-east-1"
        }
      },
      "status": {
        "ready": true,
        "state": "Ready"
      },
      "vector_type": "dense",
      "dimension": 1024,
      "deletion_protection": "disabled",
      "tags": null,
      "embed": {
        "model": "llama-text-embed-v2",
        "field_map": {
          "text": "text"
        },
        "dimension": 1024,
        "metric": "cosine",
        "write_parameters": {
          "dimension": 1024.0,
          "input_type": "passage",
          "truncate": "END"
        },
        "read_parameters": {
          "dimension": 1024.0,
          "input_type": "query",
          "truncate": "END"
        },
        "vector_type": "dense"
      }
    },
    {
      "name": "example-index-2",
      "metric": "cosine",
      "host": "example-index-2-ea1c34b.svc.aped-4627-b74a.pinecone.io",
      "spec": {
        "serverless": {
          "cloud": "aws",
          "region": "us-east-1"
        }
      },
      "status": {
        "ready": true,
        "state": "Ready"
      },
      "vector_type": "dense",
      "dimension": 1024,
      "deletion_protection": "disabled",
      "tags": null,
      "embed": {
        "model": "llama-text-embed-v2",
        "field_map": {
          "text": "text"
        },
        "dimension": 1024,
        "metric": "cosine",
        "write_parameters": {
          "dimension": 1024.0,
          "input_type": "passage",
          "truncate": "END"
        },
        "read_parameters": {
          "dimension": 1024.0,
          "input_type": "query",
          "truncate": "END"
        },
        "vector_type": "dense"
      }
    }
  ]
  ```

  ```javascript JavaScript theme={null}
  {
    "indexes": [
      {
        "name": "example-index",
        "dimension": 1024,
        "metric": "cosine",
        "host": "example-index-fa77d8e.svc.aped-4627-b74a.pinecone.io",
        "deletionProtection": "disabled",
        "embed": {
          "model": "llama-text-embed-v2",
          "metric": "cosine",
          "dimension": 1024,
          "vectorType": "dense",
          "fieldMap": {
            "text": "text"
          },
          "readParameters": {
            "dimension": 1024,
            "input_type": "query",
            "truncate": "END"
          },
          "writeParameters": {
            "dimension": 1024,
            "input_type": "passage",
            "truncate": "END"
          }
        },
        "spec": {
          "serverless": {
            "cloud": "aws",
            "region": "us-east-1"
          }
        },
        "status": {
          "ready": true,
          "state": "Ready"
        },
        "vectorType": "dense"
      },
      {
        "name": "example-index-2",
        "dimension": 1024,
        "metric": "cosine",
        "host": "example-index-2-ea1c34b.svc.aped-4627-b74a.pinecone.io",
        "deletionProtection": "disabled",
        "embed": {
          "model": "llama-text-embed-v2",
          "metric": "cosine",
          "dimension": 1024,
          "vectorType": "dense",
          "fieldMap": {
            "text": "text"
          },
          "readParameters": {
            "dimension": 1024,
            "input_type": "query",
            "truncate": "END"
          },
          "writeParameters": {
            "dimension": 1024,
            "input_type": "passage",
            "truncate": "END"
          }
        },
        "spec": {
          "serverless": {
            "cloud": "aws",
            "region": "us-east-1"
          }
        },
        "status": {
          "ready": true,
          "state": "Ready"
        },
        "vectorType": "dense"
      }
    ]
  }
  ```

  ```java Java theme={null}
  {
    "indexes": [
      {
        "name": "example-index",
        "dimension": 1024,
        "metric": "cosine",
        "host": "example-index-fa77d8e.svc.aped-4627-b74a.pinecone.io",
        "deletion_protection": "disabled",
        "embed": {
          "model": "llama-text-embed-v2",
          "metric": "cosine",
          "dimension": 1024,
          "vector_type": "dense",
          "field_map": {
            "text": "text"
          },
          "read_parameters": {
            "dimension": 1024.0,
            "input_type": "query",
            "truncate": "END"
          },
          "write_parameters": {
            "dimension": 1024.0,
            "input_type": "passage",
            "truncate": "END"
          }
        },
        "spec": {
          "serverless": {
            "cloud": "aws",
            "region": "us-east-1"
          }
        },
        "status": {
          "ready": true,
          "state": "Ready"
        },
        "vector_type": "dense"
      },
      {
        "name": "example-index-2",
        "dimension": 1024,
        "metric": "cosine",
        "host": "example-index-2-ea1c34b.svc.aped-4627-b74a.pinecone.io",
        "deletion_protection": "disabled",
        "embed": {
          "model": "llama-text-embed-v2",
          "metric": "cosine",
          "dimension": 1024,
          "vector_type": "dense",
          "field_map": {
            "text": "text"
          },
          "read_parameters": {
            "dimension": 1024.0,
            "input_type": "query",
            "truncate": "END"
          },
          "write_parameters": {
            "dimension": 1024.0,
            "input_type": "passage",
            "truncate": "END"
          }
        },
        "spec": {
          "serverless": {
            "cloud": "aws",
            "region": "us-east-1"
          }
        },
        "status": {
          "ready": true,
          "state": "Ready"
        },
        "vector_type": "dense"
      }
    ]
  }
  ```

  ```go Go theme={null}
  [
    {
      "name": "example-index",
      "host": "example-index-fa77d8e.svc.aped-4627-b74a.pinecone.io",
      "metric": "cosine",
      "vector_type": "dense",
      "deletion_protection": "disabled",
      "dimension": 1024,
      "spec": {
        "serverless": {
          "cloud": "aws",
          "region": "us-east-1"
        }
      },
      "status": {
        "ready": true,
        "state": "Ready"
      },
      "embed": {
        "model": "llama-text-embed-v2",
        "dimension": 1024,
        "metric": "cosine",
        "vector_type": "dense",
        "field_map": {
          "text": "text"
        },
        "read_parameters": {
          "dimension": 1024,
          "input_type": "query",
          "truncate": "END"
        },
        "write_parameters": {
          "dimension": 1024,
          "input_type": "passage",
          "truncate": "END"
        }
      }
    },
    {
      "name": "example-index-2",
      "host": "example-index-2-ea1c34b.svc.aped-4627-b74a.pinecone.io",
      "metric": "cosine",
      "vector_type": "dense",
      "deletion_protection": "disabled",
      "dimension": 1024,
      "spec": {
        "serverless": {
          "cloud": "aws",
          "region": "us-east-1"
        }
      },
      "status": {
        "ready": true,
        "state": "Ready"
      },
      "embed": {
        "model": "llama-text-embed-v2",
        "dimension": 1024,
        "metric": "cosine",
        "vector_type": "dense",
        "field_map": {
          "text": "text"
        },
        "read_parameters": {
          "dimension": 1024,
          "input_type": "query",
          "truncate": "END"
        },
        "write_parameters": {
          "dimension": 1024,
          "input_type": "passage",
          "truncate": "END"
        }
      }
    }
  ]
  ```

  ```csharp C# theme={null}
  {
    "indexes": [
      {
        "name": "example-index",
        "dimension": 1024,
        "metric": "cosine",
        "host": "example-index-fa77d8e.svc.aped-4627-b74a.pinecone.io",
        "deletion_protection": "disabled",
        "embed": {
          "model": "llama-text-embed-v2",
          "metric": "cosine",
          "dimension": 1024,
          "vector_type": "dense",
          "field_map": {
            "text": "text"
          },
          "read_parameters": {
            "dimension": 1024,
            "input_type": "query",
            "truncate": "END"
          },
          "write_parameters": {
            "dimension": 1024,
            "input_type": "passage",
            "truncate": "END"
          }
        },
        "spec": {
          "serverless": {
            "cloud": "aws",
            "region": "us-east-1"
          }
        },
        "status": {
          "ready": true,
          "state": "Ready"
        },
        "vector_type": "dense"
      },
      {
        "name": "example-index-2",
        "dimension": 1024,
        "metric": "cosine",
        "host": "example-index-2-ea1c34b.svc.aped-4627-b74a.pinecone.io",
        "deletion_protection": "disabled",
        "embed": {
          "model": "llama-text-embed-v2",
          "metric": "cosine",
          "dimension": 1024,
          "vector_type": "dense",
          "field_map": {
            "text": "text"
          },
          "read_parameters": {
            "dimension": 1024,
            "input_type": "query",
            "truncate": "END"
          },
          "write_parameters": {
            "dimension": 1024,
            "input_type": "passage",
            "truncate": "END"
          }
        },
        "spec": {
          "serverless": {
            "cloud": "aws",
            "region": "us-east-1"
          }
        },
        "status": {
          "ready": true,
          "state": "Ready"
        },
        "vector_type": "dense"
      }
    ]
  }
  ```

  ```json curl theme={null}
  {
    "indexes": [
      {
        "name": "example-index",
        "vector_type": "dense",
        "metric": "cosine",
        "dimension": 1024,
        "status": {
          "ready": true,
          "state": "Ready"
        },
        "host": "example-index-fa77d8e.svc.aped-4627-b74a.pinecone.io",
        "spec": {
          "serverless": {
            "region": "us-east-1",
            "cloud": "aws"
          }
        },
        "deletion_protection": "disabled",
        "tags": null,
        "embed": {
          "model": "llama-text-embed-v2",
          "field_map": {
            "text": "text"
          },
          "dimension": 1024,
          "metric": "cosine",
          "write_parameters": {
            "dimension": 1024,
            "input_type": "passage",
            "truncate": "END"
          },
          "read_parameters": {
            "dimension": 1024,
            "input_type": "query",
            "truncate": "END"
          },
          "vector_type": "dense"
        }
      },
      {
        "name": "example-index-2",
        "vector_type": "dense",
        "metric": "cosine",
        "dimension": 1024,
        "status": {
          "ready": true,
          "state": "Ready"
        },
        "host": "example-index-2-ea1c34b.svc.aped-4627-b74a.pinecone.io",
        "spec": {
          "serverless": {
            "region": "us-east-1",
            "cloud": "aws"
          }
        },
        "deletion_protection": "disabled",
        "tags": null,
        "embed": {
          "model": "llama-text-embed-v2",
          "field_map": {
            "text": "text"
          },
          "dimension": 1024,
          "metric": "cosine",
          "write_parameters": {
            "dimension": 1024,
            "input_type": "passage",
            "truncate": "END"
          },
          "read_parameters": {
            "dimension": 1024,
            "input_type": "query",
            "truncate": "END"
          },
          "vector_type": "dense"
        }
      }
    ]
  }
  ```

  ```text CLI theme={null}
  NAME                   STATUS    HOST                                                          DIMENSION   METRIC    SPEC
  example-index          Ready     example-index-fa77d8e.svc.aped-4627-b74a.pinecone.io          1536        cosine    serverless
  example-index-2        Ready     example-index-2-ea1c34b.svc.aped-4627-b74a.pinecone.io        1024        cosine    serverless
  ```
</ResponseExample>



---
**Navigation:** [← Previous](./14-lexical-search.md) | [Index](./index.md) | [Next →](./16-delete-vectors.md)
