**Navigation:** [← Previous](./13-create-a-project.md) | [Index](./index.md) | [Next →](./15-search-overview.md)

# Lexical search
Source: https://docs.pinecone.io/guides/search/lexical-search

Perform keyword-based search on sparse indexes

This page shows you how to search a [sparse index](/guides/index-data/indexing-overview#sparse-indexes) for records that most exactly match the words or phrases in a query. This is often called lexical search or keyword search.

Lexical search uses [sparse vectors](https://www.pinecone.io/learn/sparse-retrieval/), which have a very large number of dimensions, where only a small proportion of values are non-zero. The dimensions represent words from a dictionary, and the values represent the importance of these words in the document. Words are scored independently and then summed, with the most similar records scored highest.


## Search with text

<Note>
  Searching with text is supported only for [indexes with integrated embedding](/guides/index-data/indexing-overview#integrated-embedding).
</Note>

To search a sparse index with a query text, use the [`search_records`](/reference/api/latest/data-plane/search_records) operation with the following parameters:

* `namespace`: The [namespace](/guides/index-data/indexing-overview#namespaces) to query. To use the default namespace, set to `"__default__"`.
* `query.inputs.text`:  The query text. Pinecone uses the [embedding model](/guides/index-data/create-an-index#embedding-models) integrated with the index to convert the text to a sparse vector automatically.
* `query.top_k`:  The number of records to return.
* `query.match_terms`: (Optional) A list of terms that must be present in each search result. For more details, see [Filter by required terms](#filter-by-required-terms).
* `fields`: (Optional) The fields to return in the response. If not specified, the response includes all fields.

For example, the following code converts the query “What is AAPL's outlook, considering both product launches and market conditions?” to a sparse vector and then searches for the 3 most similar vectors in the `example-namespace` namespace:

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
          "inputs": {"text": "What is AAPL's outlook, considering both product launches and market conditions?"}, 
          "top_k": 3
      },
      fields=["chunk_text", "quarter"]
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
      topK: 3,
      inputs: { text: "What is AAPL's outlook, considering both product launches and market conditions?" },
    },
    fields: ['chunk_text', 'quarter']
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

          Index index = new Index(config, connection, "integrated-sparse-java");

          String query = "What is AAPL's outlook, considering both product launches and market conditions?";
          List<String> fields = new ArrayList<>();
          fields.add("category");
          fields.add("chunk_text");

          // Search the sparse index
          SearchRecordsResponse recordsResponse = index.searchRecordsByText(query,  "example-namespace", fields, 3, null, null);

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
              TopK: 3,
              Inputs: &map[string]interface{}{
                  "text": "What is AAPL's outlook, considering both product launches and market conditions?",
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
              TopK = 3,
              Inputs = new Dictionary<string, object?> { { "text", "What is AAPL's outlook, considering both product launches and market conditions?" } },
          },
          Fields = ["category", "chunk_text"],
      }
  );

  Console.WriteLine(response);
  ```

  ```shell curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="INDEX_HOST"

  curl "https://$INDEX_HOST/records/namespaces/example-namespace/search" \
    -H "Content-Type: application/json" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-API-Version: 2025-04" \
    -d '{
          "query": {
            "inputs": { "text": "What is AAPL'\''s outlook, considering both product launches and market conditions?" },
            "top_k": 3
          },
          "fields": ["chunk_text", "quarter"]
      }'
  ```
</CodeGroup>

The results will look as follows. The most similar records are scored highest.

<CodeGroup>
  ```python Python theme={null}
  {'result': {'hits': [{'_id': 'vec2',
                        '_score': 10.77734375,
                        'fields': {'chunk_text': "Analysts suggest that AAPL'''s "
                                                 'upcoming Q4 product launch '
                                                 'event might solidify its '
                                                 'position in the premium '
                                                 'smartphone market.',
                                   'quarter': 'Q4'}},
                       {'_id': 'vec3',
                        '_score': 6.49066162109375,
                        'fields': {'chunk_text': "AAPL'''s strategic Q3 "
                                                 'partnerships with '
                                                 'semiconductor suppliers could '
                                                 'mitigate component risks and '
                                                 'stabilize iPhone production.',
                                   'quarter': 'Q3'}},
                       {'_id': 'vec1',
                        '_score': 5.3671875,
                        'fields': {'chunk_text': 'AAPL reported a year-over-year '
                                                 'revenue increase, expecting '
                                                 'stronger Q3 demand for its '
                                                 'flagship phones.',
                                   'quarter': 'Q3'}}]},
   'usage': {'embed_total_tokens': 18, 'read_units': 1}}
  ```

  ```javascript JavaScript theme={null}
  {
    result: { 
      hits: [ 
        {
          _id: "vec2",
          _score: 10.82421875,
          fields: {
            chunk_text: "Analysts suggest that AAPL'''s upcoming Q4 product launch event might solidify its position in the premium smartphone market.",
            quarter: "Q4"
          }
        },
        {
          _id: "vec3",
          _score: 6.49066162109375,
          fields: {
            chunk_text: "AAPL'''s strategic Q3 partnerships with semiconductor suppliers could mitigate component risks and stabilize iPhone production.",
            quarter: "Q3"
          }
        },
        {
          _id: "vec1",
          _score: 5.3671875,
          fields: {
            chunk_text: "AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones.",
            quarter: "Q3"
          }
        }
      ]
    },
    usage: { 
      readUnits: 1, 
      embedTotalTokens: 18 
    }
  }
  ```

  ```java Java theme={null}
  class SearchRecordsResponse {
      result: class SearchRecordsResponseResult {
          hits: [class Hit {
              id: vec2
              score: 10.82421875
              fields: {chunk_text=Analysts suggest that AAPL's upcoming Q4 product launch event might solidify its position in the premium smartphone market., quarter=Q4}
              additionalProperties: null
          }, class Hit {
              id: vec3
              score: 6.49066162109375
              fields: {chunk_text=AAAPL'''s strategic Q3 partnerships with semiconductor suppliers could mitigate component risks and stabilize iPhone production., quarter=Q3}
              additionalProperties: null
          }, class Hit {
              id: vec1
              score: 5.3671875
              fields: {chunk_text=AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones., quarter=Q3}
              additionalProperties: null
          }]
          additionalProperties: null
      }
      usage: class SearchUsage {
          readUnits: 1
          embedTotalTokens: 18
      }
      additionalProperties: null
  }
  ```

  ```go Go theme={null}
  {
    "result": {
      "hits": [
        {
          "_id": "vec2",
          "_score": 10.833984,
          "fields": {
            "chunk_text": "Analysts suggest that AAPL's upcoming Q4 product launch event might solidify its position in the premium smartphone market.",
            "quarter": "Q4"
          }
        },
        {
          "_id": "vec3",
          "_score": 6.473572,
          "fields": {
            "chunk_text": "AAPL's strategic Q3 partnerships with semiconductor suppliers could mitigate component risks and stabilize iPhone production.",
            "quarter": "Q3"
          }
        },
        {
          "_id": "vec1",
          "_score": 5.3710938,
          "fields": {
            "chunk_text": "AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones.",
            "quarter": "Q3"
          }
        }
      ]
    },
    "usage": {
      "read_units": 6,
      "embed_total_tokens": 18
    }
  }
  ```

  ```csharp C# theme={null}
  {
      "result": {
          "hits": [
              {
                  "_id": "vec2",
                  "_score": 10.833984,
                  "fields": {
                      "chunk_text": "Analysts suggest that AAPL's upcoming Q4 product launch event might solidify its position in the premium smartphone market.",
                      "quarter": "Q4"
                  }
              },
              {
                  "_id": "vec3",
                  "_score": 6.473572,
                  "fields": {
                      "chunk_text": "AAPL's strategic Q3 partnerships with semiconductor suppliers could mitigate component risks and stabilize iPhone production.",
                      "quarter": "Q3"
                  }
              },
              {
                  "_id": "vec1",
                  "_score": 5.3710938,
                  "fields": {
                      "chunk_text": "AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones.",
                      "quarter": "Q3"
                  }
              }
          ]
      },
      "usage": {
          "read_units": 6,
          "embed_total_tokens": 18
      }
  }
  ```

  ```json curl theme={null}
  {
    "result": {
      "hits": [
        {
          "_id": "vec2",
          "_score": 10.82421875,
          "fields": {
            "chunk_text": "Analysts suggest that AAPL'''s upcoming Q4 product launch event might solidify its position in the premium smartphone market.",
            "quarter": "Q4"
          }
        },
        {
          "_id": "vec3",
          "_score": 6.49066162109375,
          "fields": {
            "chunk_text": "AAPL'''s strategic Q3 partnerships with semiconductor suppliers could mitigate component risks and stabilize iPhone production.",
            "quarter": "Q3"
          }
        },
        {
          "_id": "vec1",
          "_score": 5.3671875,
          "fields": {
            "chunk_text": "AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones.",
            "quarter": "Q3"
          }
        }
      ]
    },
    "usage": {
      "embed_total_tokens": 18,
      "read_units": 1
    }
  }
  ```
</CodeGroup>


## Search with a sparse vector

To search a sparse index with a sparse vector representation of a query, use the [`query`](/reference/api/latest/data-plane/query) operation with the following parameters:

* `namespace`: The [namespace](/guides/index-data/indexing-overview#namespaces) to query. To use the default namespace, set to `"__default__"`.
* `sparse_vector`: The sparse vector values and indices.
* `top_k`: The number of results to return.
* `include_values`: Whether to include the vector values of the matching records in the response. Defaults to `false`.
* `include_metadata`: Whether to include the metadata of the matching records in the response. Defaults to `false`.
  <Note>
    When querying with `top_k` over 1000, avoid returning vector data or metadata for optimal performance.
  </Note>

For example, the following code uses a sparse vector representation of the query "What is AAPL's outlook, considering both product launches and market conditions?" to search for the 3 most similar vectors in the `example-namespace` namespace:

<CodeGroup>
  ```python Python theme={null}
  from pinecone import Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  # To get the unique host for an index, 
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  index = pc.Index(host="INDEX_HOST")

  results = index.query(
      namespace="example-namespace",
      sparse_vector={
        "values": [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
        "indices": [767227209, 1640781426, 1690623792, 2021799277, 2152645940, 2295025838, 2443437770, 2779594451, 2956155693, 3476647774, 3818127854, 4283091697]
      }, 
      top_k=3,
      include_metadata=True,
      include_values=False
  )

  print(results)
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({ apiKey: "YOUR_API_KEY" })

  // To get the unique host for an index, 
  // see https://docs.pinecone.io/guides/manage-data/target-an-index
  const index = pc.index("INDEX_NAME", "INDEX_HOST")

  const queryResponse = await index.namespace('example-namespace').query({
      sparseVector: {
          indices: [767227209, 1640781426, 1690623792, 2021799277, 2152645940, 2295025838, 2443437770, 2779594451, 2956155693, 3476647774, 3818127854, 4283091697],
          values: [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
      },
      topK: 3,
      includeValues: false,
      includeMetadata: true
  });

  console.log(queryResponse);
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Pinecone;
  import io.pinecone.unsigned_indices_model.QueryResponseWithUnsignedIndices;
  import io.pinecone.clients.Index;

  import java.util.*;

  public class SearchSparseIndex {
      public static void main(String[] args) throws InterruptedException {
          // Instantiate Pinecone class
          Pinecone pinecone = new Pinecone.Builder("YOUR_API_KEY").build();

          String indexName = "docs-example";

          Index index = pinecone.getIndexConnection(indexName);

          List<Long> sparseIndices = Arrays.asList(
                  767227209L, 1640781426L, 1690623792L, 2021799277L, 2152645940L,
                  2295025838L, 2443437770L, 2779594451L, 2956155693L, 3476647774L,
                  3818127854L, 428309169L);
          List<Float> sparseValues = Arrays.asList(
                  1.0f, 1.0f, 1.0f, 1.0f, 1.0f, 1.0f,
                  1.0f, 1.0f, 1.0f, 1.0f, 1.0f, 1.0f);

          QueryResponseWithUnsignedIndices queryResponse = index.query(3, null, sparseIndices, sparseValues, null, "example-namespace", null, false, true);
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

  	sparseValues := pinecone.SparseValues{
  		Indices: []uint32{767227209, 1640781426, 1690623792, 2021799277, 2152645940, 2295025838, 2443437770, 2779594451, 2956155693, 3476647774, 3818127854, 4283091697},
  		Values:  []float32{1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0},
  	}

  	res, err := idxConnection.QueryByVectorValues(ctx, &pinecone.QueryByVectorValuesRequest{
  		SparseValues:    &sparseValues,
  		TopK:            3,
  		IncludeValues:   false,
  		IncludeMetadata: true,
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

  var index = pinecone.Index("docs-example");

  var queryResponse = await index.QueryAsync(new QueryRequest {
      Namespace = "example-namespace",
      TopK = 4,
      SparseVector = new SparseValues
      {
          Indices = [767227209, 1640781426, 1690623792, 2021799277, 2152645940, 2295025838, 2443437770, 2779594451, 2956155693, 3476647774, 3818127854, 4283091697],
          Values = new[] { 1.0f, 1.0f, 1.0f, 1.0f, 1.0f, 1.0f, 1.0f, 1.0f, 1.0f, 1.0f, 1.0f, 1.0f },
      },
      IncludeValues = false,
      IncludeMetadata = true
  });

  Console.WriteLine(queryResponse);
  ```

  ```shell curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="INDEX_HOST"

  curl "https://$INDEX_HOST/query" \
    -H "Content-Type: application/json" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-API-Version: 2025-04" \
    -d '{
          "sparseVector": {
              "values": [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
              "indices": [767227209, 1640781426, 1690623792, 2021799277, 2152645940, 2295025838, 2443437770, 2779594451, 2956155693, 3476647774, 3818127854, 4283091697]
          },
          "namespace": "example-namespace",
          "topK": 4,
          "includeMetadata": true,
          "includeValues": false
      }'
  ```
</CodeGroup>

The results will look as follows. The most similar records are scored highest.

<CodeGroup>
  ```python Python theme={null}
  {'matches': [{'id': 'vec2',
                'metadata': {'category': 'technology',
                             'quarter': 'Q4',
                             'chunk_text': "Analysts suggest that AAPL'''s "
                                            'upcoming Q4 product launch event '
                                            'might solidify its position in the '
                                            'premium smartphone market.'},
                'score': 10.9042969,
                'values': []},
               {'id': 'vec3',
                'metadata': {'category': 'technology',
                             'quarter': 'Q3',
                             'chunk_text': "AAPL'''s strategic Q3 partnerships "
                                            'with semiconductor suppliers could '
                                            'mitigate component risks and '
                                            'stabilize iPhone production'},
                'score': 6.48010254,
                'values': []},
               {'id': 'vec1',
                'metadata': {'category': 'technology',
                             'quarter': 'Q3',
                             'chunk_text': 'AAPL reported a year-over-year '
                                            'revenue increase, expecting '
                                            'stronger Q3 demand for its flagship '
                                            'phones.'},
                'score': 5.3671875,
                'values': []}],
   'namespace': 'example-namespace',
   'usage': {'read_units': 1}}
  ```

  ```javascript JavaScript theme={null}
  { 
    matches: [
              { 
                id: 'vec2',
                score: 10.9042969,
                values: [],
                metadata: {
                  chunk_text: "Analysts suggest that AAPL'''s upcoming Q4 product launch event might solidify its position in the premium smartphone market.",
                  category: 'technology',
                  quarter: 'Q4'
                }
              },
              {
                id: 'vec3',
                score: 6.48010254,
                values: [],
                metadata: {
                  chunk_text: "AAPL'''s strategic Q3 partnerships with semiconductor suppliers could mitigate component risks and stabilize iPhone production.",
                  category: 'technology',
                  quarter: 'Q3'
                }
              },
              {
                id: 'vec1',
                score: 5.3671875,
                values: [],
                metadata: {
                    chunk_text: 'AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones.',
                    category: 'technology',
                    quarter: 'Q3'
                }
              }
            ],
    namespace: 'example-namespace',
    usage: {readUnits: 1}
  }
  ```

  ```java Java theme={null}
  class QueryResponseWithUnsignedIndices {
      matches: [ScoredVectorWithUnsignedIndices {
          score: 10.34375
          id: vec2
          values: []
          metadata: fields {
            key: "category"
            value {
              string_value: "technology"
            }
          }
          fields {
            key: "chunk_text"
            value {
              string_value: "Analysts suggest that AAPL\'\\\'\'s upcoming Q4 product launch event might solidify its position in the premium smartphone market."
            }
          }
          fields {
            key: "quarter"
            value {
              string_value: "Q4"
            }
          }
          
          sparseValuesWithUnsignedIndices: SparseValuesWithUnsignedIndices {
              indicesWithUnsigned32Int: []
              values: []
          }
      }, ScoredVectorWithUnsignedIndices {
          score: 5.8638916
          id: vec3
          values: []
          metadata: fields {
            key: "category"
            value {
              string_value: "technology"
            }
          }
          fields {
            key: "chunk_text"
            value {
              string_value: "AAPL\'\\\'\'s strategic Q3 partnerships with semiconductor suppliers could mitigate component risks and stabilize iPhone production"
            }
          }
          fields {
            key: "quarter"
            value {
              string_value: "Q3"
            }
          }
          
          sparseValuesWithUnsignedIndices: SparseValuesWithUnsignedIndices {
              indicesWithUnsigned32Int: []
              values: []
          }
      }, ScoredVectorWithUnsignedIndices {
          score: 5.3671875
          id: vec1
          values: []
          metadata: fields {
            key: "category"
            value {
              string_value: "technology"
            }
          }
          fields {
            key: "chunk_text"
            value {
              string_value: "AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones."
            }
          }
          fields {
            key: "quarter"
            value {
              string_value: "Q3"
            }
          }
          
          sparseValuesWithUnsignedIndices: SparseValuesWithUnsignedIndices {
              indicesWithUnsigned32Int: []
              values: []
          }
      }]
      namespace: example-namespace
      usage: read_units: 1

  }
  ```

  ```go Go theme={null}
  {
    "matches": [
      {
        "vector": {
          "id": "vec2",
          "metadata": {
            "category": "technology",
            "quarter": "Q4",
            "chunk_text": "Analysts suggest that AAPL's upcoming Q4 product launch event might solidify its position in the premium smartphone market."
          }
        },
        "score": 10.904296
      },
      {
        "vector": {
          "id": "vec3",
          "metadata": {
            "category": "technology",
            "quarter": "Q3",
            "chunk_text": "AAPL's strategic Q3 partnerships with semiconductor suppliers could mitigate component risks and stabilize iPhone production"
          }
        },
        "score": 6.4801025
      },
      {
        "vector": {
          "id": "vec1",
          "metadata": {
            "category": "technology",
            "quarter": "Q3",
            "chunk_text": "AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones"
          }
        },
        "score": 5.3671875
      }
    ],
    "usage": {
      "read_units": 1
    },
    "namespace": "example-namespace"
  }
  ```

  ```csharp C# theme={null}
  {
    "results": [],
    "matches": [
      {
        "id": "vec2",
        "score": 10.904297,
        "values": [],
        "metadata": {
          "category": "technology",
          "chunk_text": "Analysts suggest that AAPL\u0027\u0027\u0027s upcoming Q4 product launch event might solidify its position in the premium smartphone market.",
          "quarter": "Q4"
        }
      },
      {
        "id": "vec3",
        "score": 6.4801025,
        "values": [],
        "metadata": {
          "category": "technology",
          "chunk_text": "AAPL\u0027\u0027\u0027s strategic Q3 partnerships with semiconductor suppliers could mitigate component risks and stabilize iPhone production",
          "quarter": "Q3"
        }
      },
      {
        "id": "vec1",
        "score": 5.3671875,
        "values": [],
        "metadata": {
          "category": "technology",
          "chunk_text": "AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones.",
          "quarter": "Q3"
        }
      }
    ],
    "namespace": "example-namespace",
    "usage": {
      "readUnits": 1
    }
  }
  ```

  ```json curl theme={null}
  {
    "results": [],
    "matches": [
      {
        "id": "vec2",
        "score": 10.9042969,
        "values": [],
        "metadata": {
          "chunk_text": "Analysts suggest that AAPL'''s upcoming Q4 product launch event might solidify its position in the premium smartphone market.",
          "category": "technology",
          "quarter": "Q4"
        }
      },
      {
        "id": "vec3",
        "score": 6.48010254,
        "values": [],
        "metadata": {
          "chunk_text": "AAPL'''s strategic Q3 partnerships with semiconductor suppliers could mitigate component risks and stabilize iPhone production.",
          "category": "technology",
          "quarter": "Q3"
        }
      },
      {
        "id": "vec1",
        "score": 5.3671875,
        "values": [],
        "metadata": {
            "chunk_text": "AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones.",
            "category": "technology",
            "quarter": "Q3"
        }
      }
    ],
    "namespace": "example-namespace",
    "usage": {
      "readUnits": 1
    }
  }
  ```
</CodeGroup>


## Search with a record ID

When you search with a record ID, Pinecone uses the sparse vector associated with the record as the query. To search a sparse index with a record ID, use the [`query`](/reference/api/latest/data-plane/query) operation with the following parameters:

* `namespace`: The [namespace](/guides/index-data/indexing-overview#namespaces) to query. To use the default namespace, set to `"__default__"`.
* `id`: The unique record ID containing the sparse vector to use as the query.
* `top_k`: The number of results to return.
* `include_values`: Whether to include the vector values of the matching records in the response. Defaults to `false`.
* `include_metadata`: Whether to include the metadata of the matching records in the response. Defaults to `false`.
  <Note>
    When querying with `top_k` over 1000, avoid returning vector data or metadata for optimal performance.
  </Note>

For example, the following code uses an ID to search for the 3 records in the `example-namespace` namespace that best match the sparse vector in the record:

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


## Filter by required terms

<Note>
  This feature is in [public preview](/release-notes/feature-availability) and is available only on the `2025-10` version of the API. See [limitations](#limitations) for details.
</Note>

When [searching with text](#search-with-text), you can specify a list of terms that must be present in each lexical search result. This is especially useful for:

* **Precision filtering**: Ensuring specific entities or concepts appear in results
* **Quality control**: Filtering out results that don't contain essential keywords
* **Domain-specific searches**: Requiring domain-specific terminology in results
* **Entity-based filtering**: Ensuring specific people, places, or things are mentioned

To filter by required terms, add `match_terms` to your query, specifying the `terms` to require and the `strategy` to use. Currently, `all` is the only strategy supported (all terms must be present).

For example, the following request searches for records about Tesla's stock performance while ensuring both "Tesla" and "stock" appear in each result:

```bash curl theme={null}
PINECONE_API_KEY="YOUR_API_KEY"
INDEX_HOST="INDEX_HOST"

curl "https://$INDEX_HOST/records/namespaces/example-namespace/search" \
  -H "Content-Type: application/json" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "X-Pinecone-API-Version: unstable" \
  -d '{
        "query": {
          "inputs": { "text": "What is the current outlook for Tesla stock performance?" },
          "top_k": 3,
          "match_terms": {
            "terms": ["Tesla", "stock"],
            "strategy": "all"
          }
        },
        "fields": ["chunk_text"]
    }'
```

The response includes only records that contain both "Tesla" and "stock":

```json  theme={null}
{
  "result": {
    "hits": [
      {
        "_id": "tesla_q4_earnings",
        "_score": 9.82421875,
        "fields": {
          "chunk_text": "Tesla stock surged 8% in after-hours trading following strong Q4 earnings that exceeded analyst expectations. The company reported record vehicle deliveries and improved profit margins."
        }
      },
      {
        "_id": "tesla_competition_analysis",
        "_score": 7.49066162109375,
        "fields": {
          "chunk_text": "Tesla stock faces increasing competition from traditional automakers entering the electric vehicle market. However, analysts maintain that Tesla's technological lead and brand recognition provide significant advantages."
        }
      },
      {
        "_id": "tesla_production_update",
        "_score": 6.3671875,
        "fields": {
          "chunk_text": "Tesla stock performance is closely tied to production capacity at its Gigafactories. Recent expansion announcements suggest the company is positioning for continued growth in global markets."
        }
      }
    ]
  },
  "usage": {
    "embed_total_tokens": 18,
    "read_units": 1
  }
}
```

Without the `match_terms` filter, you might get results like:

* "Tesla cars are popular in California" (mentions Tesla but not stock)
* "Stock market volatility affects tech companies" (mentions stock but not Tesla)
* "Electric vehicle sales are growing" (neither Tesla nor stock)

### Limitations

* **Integrated indexes only**: Filtering by required terms is supported only for [indexes with integrated embedding](/guides/index-data/indexing-overview#integrated-embedding).
* **Post-processing filter**: The filtering happens after the initial query, so potential matches that weren't included in the initial `top_k` results won't appear in the final results
* **No phrase matching**: Terms are matched individually in any order and location.
* **No case-sensitivity**: Terms are normalized during processing.



# Rerank results
Source: https://docs.pinecone.io/guides/search/rerank-results

Improve the quality of results with reranking.

Reranking is used as part of a two-stage vector retrieval process to improve the quality of results. You first query an index for a given number of relevant results, and then you send the query and results to a reranking model. The reranking model scores the results based on their semantic relevance to the query and returns a new, more accurate ranking. This approach is one of the simplest methods for improving quality in retrieval augmented generation (RAG) pipelines.

Pinecone provides [hosted reranking models](#reranking-models) so it's easy to manage two-stage vector retrieval on a single platform. You can use a hosted model to rerank results as an integrated part of a query, or you can use a hosted model or external model to rerank results as a standalone operation.


## Integrated reranking

To rerank initial results as an integrated part of a query, without any extra steps, use the [`search`](/reference/api/latest/data-plane/search_records) operation with the `rerank` parameter, including the [hosted reranking model](#reranking-models) you want to use, the number of reranked results to return, and the fields to use for reranking, if different than the main query.

For example, the following code searches for the 3 records most semantically related to a query text and uses the `hosted bge-reranker-v2-m3` model to rerank the results and return only the 2 most relevant documents:

<CodeGroup>
  ```python Python theme={null}
  from pinecone import Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  # To get the unique host for an index, 
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  index = pc.Index(host="INDEX_HOST")

  ranked_results = index.search(
      namespace="example-namespace", 
      query={
          "inputs": {"text": "Disease prevention"}, 
          "top_k": 4
      },
      rerank={
          "model": "bge-reranker-v2-m3",
          "top_n": 2,
          "rank_fields": ["chunk_text"]
      },
      fields=["category", "chunk_text"]
  )

  print(ranked_results)
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
    rerank: {
      model: 'bge-reranker-v2-m3',
      rankFields: ['chunk_text'],
      topN: 2,
    },
  });

  console.log(response);
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Index;
  import io.pinecone.configs.PineconeConfig;
  import io.pinecone.configs.PineconeConnection;
  import org.openapitools.db_data.client.ApiException;
  import org.openapitools.db_data.client.model.SearchRecordsRequestRerank;
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

          List<String>rankFields = new ArrayList<>();
          rankFields.add("chunk_text");
          SearchRecordsRequestRerank rerank = new SearchRecordsRequestRerank()
                  .query(query)
                  .model("bge-reranker-v2-m3")
                  .topN(2)
                  .rankFields(rankFields);

          SearchRecordsResponse recordsResponseReranked = index.searchRecordsByText(query,  "example-namespace", fields,4, null, rerank);

          System.out.println(recordsResponseReranked);
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

      topN := int32(2)
      res, err := idxConnection.SearchRecords(ctx, &pinecone.SearchRecordsRequest{
          Query: pinecone.SearchRecordsQuery{
              TopK: 3,
              Inputs: &map[string]interface{}{
                  "text": "Disease prevention",
              },
          },
          Rerank: &pinecone.SearchRecordsRerank{
              Model:      "bge-reranker-v2-m3",
              TopN:       &topN,
              RankFields: []string{"chunk_text"},
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
          Rerank = new SearchRecordsRequestRerank
          {
              Model = "bge-reranker-v2-m3",
              TopN = 2,
              RankFields = ["chunk_text"],
          }
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
              "top_k": 4
          },
          "rerank": {
              "model": "bge-reranker-v2-m3",
              "top_n": 2,
              "rank_fields": ["chunk_text"]
          },
          "fields": ["category", "chunk_text"]
       }'
  ```
</CodeGroup>

The response looks as follows. For each hit, the `_score` represents the relevance of a document to the query, normalized between 0 and 1, with scores closer to 1 indicating higher relevance.

<CodeGroup>
  ```python Python theme={null}
  {'result': {'hits': [{'_id': 'rec3',
                        '_score': 0.004399413242936134,
                        'fields': {'category': 'immune system',
                                   'chunk_text': 'Rich in vitamin C and other '
                                                  'antioxidants, apples '
                                                  'contribute to immune health '
                                                  'and may reduce the risk of '
                                                  'chronic diseases.'}},
                       {'_id': 'rec4',
                        '_score': 0.0029235430993139744,
                        'fields': {'category': 'endocrine system',
                                   'chunk_text': 'The high fiber content in '
                                                  'apples can also help regulate '
                                                  'blood sugar levels, making '
                                                  'them a favorable snack for '
                                                  'people with diabetes.'}}]},
   'usage': {'embed_total_tokens': 8, 'read_units': 6, 'rerank_units': 1}}
  ```

  ```javascript JavaScript theme={null}
  {
    result: { 
      hits: [ 
        {
          _id: 'rec3',
          _score: 0.004399413242936134,
          fields: {
            category: 'immune system',
            chunk_text: 'Rich in vitamin C and other antioxidants, apples contribute to immune health and may reduce the risk of chronic diseases.'
          }
        },
        {
          _id: 'rec4',
          _score: 0.0029235430993139744,
          fields: {
            category: 'endocrine system',
            chunk_text: 'The high fiber content in apples can also help regulate blood sugar levels, making them a favorable snack for people with diabetes.'
          }
        }
      ]
    },
    usage: { 
      readUnits: 6, 
      embedTotalTokens: 8,
      rerankUnits: 1 
    }
  }
  ```

  ```java Java theme={null}
  class SearchRecordsResponse {
      result: class SearchRecordsResponseResult {
          hits: [class Hit {
              id: rec3
              score: 0.004399413242936134
              fields: {category=immune system, chunk_text=Rich in vitamin C and other antioxidants, apples contribute to immune health and may reduce the risk of chronic diseases.}
              additionalProperties: null
          }, class Hit {
              id: rec4
              score: 0.0029235430993139744
              fields: {category=endocrine system, chunk_text=The high fiber content in apples can also help regulate blood sugar levels, making them a favorable snack for people with diabetes.}
              additionalProperties: null
          }]
          additionalProperties: null
      }
      usage: class SearchUsage {
          readUnits: 6
          embedTotalTokens: 13
          rerankUnits: 1
          additionalProperties: null
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
          "_score": 0.13683891,
          "fields": {
            "category": "immune system",
            "chunk_text": "Rich in vitamin C and other antioxidants, apples contribute to immune health and may reduce the risk of chronic diseases."
          }
        },
        {
          "_id": "rec4",
          "_score": 0.0029235430993139744,
          "fields": {
            "category": "endocrine system",
            "chunk_text": "The high fiber content in apples can also help regulate blood sugar levels, making them a favorable snack for people with diabetes."
          }
        }
      ]
    },
    "usage": {
      "read_units": 6,
      "embed_total_tokens": 8,
      "rerank_units": 1
    }
  }
  ```

  ```csharp C# theme={null}
  {
    "result": {
      "hits": [
        {
          "_id": "rec3",
          "_score": 0.004399413242936134,
          "fields": {
            "category": "immune system",
            "chunk_text": "Rich in vitamin C and other antioxidants, apples contribute to immune health and may reduce the risk of chronic diseases."
          }
        },
        {
          "_id": "rec4",
          "_score": 0.0029121784027665854,
          "fields": {
            "category": "endocrine system",
            "chunk_text": "The high fiber content in apples can also help regulate blood sugar levels, making them a favorable snack for people with diabetes."
          }
        }
      ]
    },
    "usage": {
      "read_units": 6,
      "embed_total_tokens": 8,
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
                  "_score": 0.004433765076100826,
                  "fields": {
                      "category": "immune system",
                      "chunk_text": "Rich in vitamin C and other antioxidants, apples contribute to immune health and may reduce the risk of chronic diseases."
                  }
              },
              {
                  "_id": "rec4",
                  "_score": 0.0029121784027665854,
                  "fields": {
                      "category": "endocrine system",
                      "chunk_text": "The high fiber content in apples can also help regulate blood sugar levels, making them a favorable snack for people with diabetes."
                  }
              }
          ]
      },
      "usage": {
          "embed_total_tokens": 8,
          "read_units": 6,
          "rerank_units": 1
      }
  }
  ```
</CodeGroup>


## Standalone reranking

To rerank initial results as a standalone operation, use the [`rerank`](/reference/api/latest/inference/rerank) operation with the [hosted reranking model](#reranking-models) you want to use, the query results and the query, the number of ranked results to return, the field to use for reranking, and any other model-specific parameters.

For example, the following code uses the hosted `bge-reranker-v2-m3` model to rerank the values of the `documents.chunk_text` fields based on their relevance to the query and return only the 2 most relevant documents, along with their score:

<CodeGroup>
  ```python Python theme={null}
  from pinecone import Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  ranked_results = pc.inference.rerank(
      model="bge-reranker-v2-m3",
      query="What is AAPL's outlook, considering both product launches and market conditions?",
      documents=[
          {"id": "vec2", "chunk_text": "Analysts suggest that AAPL'\''s upcoming Q4 product launch event might solidify its position in the premium smartphone market."},
          {"id": "vec3", "chunk_text": "AAPL'\''s strategic Q3 partnerships with semiconductor suppliers could mitigate component risks and stabilize iPhone production."},
          {"id": "vec1", "chunk_text": "AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones."},
      ],
      top_n=2,
      rank_fields=["chunk_text"],
      return_documents=True,
      parameters={
          "truncate": "END"
      }
  )

  print(ranked_results)
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  const rerankingModel = 'bge-reranker-v2-m3';

  const query = "What is AAPL's outlook, considering both product launches and market conditions?";

  const documents = [
    { id: 'vec2', chunk_text: "Analysts suggest that AAPL's upcoming Q4 product launch event might solidify its position in the premium smartphone market." },
    { id: 'vec3', chunk_text: "AAPL's strategic Q3 partnerships with semiconductor suppliers could mitigate component risks and stabilize iPhone production." },
    { id: 'vec1', chunk_text: "AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones." },
  ];

  const rerankOptions = {
    topN: 2,
    rankFields: ['chunk_text'],
    returnDocuments: true,
    parameters: {
      truncate: 'END'
    }, 
  };

  const rankedResults = await pc.inference.rerank(
    rerankingModel,
    query,
    documents,
    rerankOptions
  );

  console.log(rankedResults);
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
          String query = "What is AAPL's outlook, considering both product launches and market conditions?";

          // Add the documents to rerank
          List<Map<String, Object>> documents = new ArrayList<>();
          Map<String, Object> doc1 = new HashMap<>();
          doc1.put("id", "vec2");
          doc1.put("chunk_text", "Analysts suggest that AAPL's upcoming Q4 product launch event might solidify its position in the premium smartphone market.");
          documents.add(doc1);

          Map<String, Object> doc2 = new HashMap<>();
          doc2.put("id", "vec3");
          doc2.put("chunk_text", "AAPL's strategic Q3 partnerships with semiconductor suppliers could mitigate component risks and stabilize iPhone production");
          documents.add(doc2);

          Map<String, Object> doc3 = new HashMap<>();
          doc3.put("id", "vec1");
          doc3.put("chunk_text", "AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones.");
          documents.add(doc3);

          // The fields to rank the documents by. If not provided, the default is "text"
          List<String> rankFields = Arrays.asList("chunk_text");

          // The number of results to return sorted by relevance. Defaults to the number of inputs
          int topN = 2;

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

  	rerankModel := "bge-reranker-v2-m3"
  	topN := 2
  	returnDocuments := true
  	documents := []pinecone.Document{
  		{"id": "vec2", "chunk_text": "Analysts suggest that AAPL's upcoming Q4 product launch event might solidify its position in the premium smartphone market."},
  		{"id": "vec3", "chunk_text": "AAPL's strategic Q3 partnerships with semiconductor suppliers could mitigate component risks and stabilize iPhone production."},
  		{"id": "vec1", "chunk_text": "AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones."},
  	}

  	ranking, err := pc.Inference.Rerank(ctx, &pinecone.RerankRequest{
  		Model:           rerankModel,
  		Query:           "What is AAPL's outlook, considering both product launches and market conditions?",
  		ReturnDocuments: &returnDocuments,
  		TopN:            &topN,
  		RankFields:      &[]string{"chunk_text"},
  		Documents:       documents,
  	})
  	if err != nil {
  		log.Fatalf("Failed to rerank: %v", err)
  	}
  	fmt.Printf(prettifyStruct(ranking))
  }
  ```

  ```csharp C# theme={null}
  using Pinecone;

  var pinecone = new PineconeClient("YOUR_API_KEY");

  // Add the documents to rerank
  var documents = new List<Dictionary<string, object?>>
  {
      new()
      {
          ["id"] = "vec2",
          ["chunk_text"] = "Analysts suggest that AAPL's upcoming Q4 product launch event might solidify its position in the premium smartphone market."
      },
      new()
      {
          ["id"] = "vec3",
          ["chunk_text"] = "AAPL's strategic Q3 partnerships with semiconductor suppliers could mitigate component risks and stabilize iPhone production."
      },
      new()
      {
          ["id"] = "vec1",
          ["chunk_text"] = "AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones."
      }
  };

  // The fields to rank the documents by. If not provided, the default is "text"
  var rankFields = new List<string> { "chunk_text" };

  // Additional model-specific parameters for the reranker
  var parameters = new Dictionary<string, object>
  {
      ["truncate"] = "END"
  };

  // Send ranking request
  var result = await pinecone.Inference.RerankAsync(
      new RerankRequest
      {
          Model = "bge-reranker-v2-m3",
          Query = "What is AAPL's outlook, considering both product launches and market conditions?",
          Documents = documents,
          RankFields = rankFields,
          TopN = 2,
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
    "query": "What is AAPL'\''s outlook, considering both product launches and market conditions?",
    "documents": [
      {"id": "vec2", "chunk_text": "Analysts suggest that AAPL'\''s upcoming Q4 product launch event might solidify its position in the premium smartphone market."},
      {"id": "vec3", "chunk_text": "AAPL'\''s strategic Q3 partnerships with semiconductor suppliers could mitigate component risks and stabilize iPhone production."},
      {"id": "vec1", "chunk_text": "AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones."}
    ],
    "top_n": 2,
    "rank_fields": ["chunk_text"],
    "return_documents": true,
    "parameters": {
      "truncate": "END"
    }
  }'
  ```
</CodeGroup>

The response looks as follows. For each hit, the \_score represents the relevance of a document to the query, normalized between 0 and 1, with scores closer to 1 indicating higher relevance.

<CodeGroup>
  ```python Python theme={null}
  RerankResult(
    model='bge-reranker-v2-m3',
    data=[{
      index=0,
      score=0.004166256,
      document={
          id='vec2',
          chunk_text="Analysts suggest that AAPL'''s upcoming Q4 product launch event might solidify its position in the premium smartphone market."
      }
    },{
      index=2,
      score=0.0011513996,
      document={
          id='vec1',
          chunk_text='AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones.'
      }
    }],
    usage={'rerank_units': 1}
  )
  ```

  ```javascript JavaScript theme={null}
  {
    model: 'bge-reranker-v2-m3',
    data: [
      { index: 0, score: 0.004166256, document: [id: 'vec2', chunk_text: "Analysts suggest that AAPL'''s upcoming Q4 product launch event might solidify its position in the premium smartphone market."] },
      { index: 2, score: 0.0011513996, document: [id: 'vec1', chunk_text: 'AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones.'] }
    ],
    usage: { rerankUnits: 1 }
  }
  ```

  ```java Java theme={null}
  [class RankedDocument {
      index: 0
      score: 0.0063143647
      document: {id=vec2, chunk_text=Analysts suggest that AAPL's upcoming Q4 product launch event might solidify its position in the premium smartphone market.}
      additionalProperties: null
  }, class RankedDocument {
      index: 2
      score: 0.0011513996
      document: {id=vec1, chunk_text=AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones.}
      additionalProperties: null
  }]
  ```

  ```go Go theme={null}
  {
    "data": [
      {
        "document": {
          "id": "vec2",
          "chunk_text": "Analysts suggest that AAPL's upcoming Q4 product launch event might solidify its position in the premium smartphone market."
        },
        "index": 0,
        "score": 0.0063143647
      },
      {
        "document": {
          "id": "vec1",
          "chunk_text": "AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones."
        },
        "index": 2,
        "score": 0.0011513996
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
        "index": 0,
        "score": 0.006289902,
        "document": {
          "chunk_text": "Analysts suggest that AAPL\u0027s upcoming Q4 product launch event might solidify its position in the premium smartphone market.",
          "id": "vec2"
        }
      },
      {
        "index": 3,
        "score": 0.0011513996,
        "document": {
          "chunk_text": "AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones.",
          "id": "vec1"
        }
      }
    ],
    "usage": {
      "rerank_units": 1
    }
  }
  ```

  ```json curl theme={null}
  {
      "model": "bge-reranker-v2-m3",
      "data": [
          {
              "index": 0,
              "document": {
                  "chunk_text": "Analysts suggest that AAPL's upcoming Q4 product launch event might solidify its position in the premium smartphone market.",
                  "id": "vec2"
              },
              "score": 0.007606672
          },
          {
              "index": 3,
              "document": {
                  "chunk_text": "AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones.",
                  "id": "vec1"
              },
              "score": 0.0013406205
          }
      ],
      "usage": {
          "rerank_units": 1
      }
  }
  ```
</CodeGroup>


## Reranking models

Pinecone hosts several reranking models so it's easy to manage two-stage vector retrieval on a single platform. You can use a hosted model to rerank results as an integrated part of a query, or you can use a hosted model to rerank results as a standalone operation.

The following reranking models are hosted by Pinecone.

<Note>
  To understand how cost is calculated for reranking, see [Reranking cost](/guides/manage-cost/understanding-cost#reranking). To get model details via the API, see [List models](/reference/api/latest/inference/list_models) and [Describe a model](/reference/api/latest/inference/describe_model).
</Note>

<AccordionGroup>
  <Accordion title="cohere-rerank-3.5">
    <PaidOnly />

    [`cohere-rerank-3.5`](/models/cohere-rerank-3.5) is Cohere's leading reranking model, balancing performance and latency for a wide range of enterprise search applications.

    **Details**

    * Modality: Text
    * Max tokens per query and document pair: 40,000
    * Max documents: 200

    For rate limits, see [Rerank requests per minute](/reference/api/database-limits#rerank-requests-per-minute-per-model) and [Rerank request per month](/reference/api/database-limits#rerank-requests-per-month-per-model).

    **Parameters**

    The `cohere-rerank-3.5` model supports the following parameters:

    | Parameter            | Type             | Required/Optional | Description                                                                                                                             |            |
    | :------------------- | :--------------- | :---------------- | :-------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
    | `max_chunks_per_doc` | integer          | Optional          | Long documents will be automatically truncated to the specified number of chunks. Accepted range: `1 - 3072`.                           |            |
    | `rank_fields`        | array of strings | Optional          | The fields to use for reranking. The model reranks based on the order of the fields specified (e.g., `["field1", "field2", "field3"]`). | `["text"]` |
  </Accordion>

  <Accordion title="bge-reranker-v2-m3">
    [`bge-reranker-v2-m3`](/models/bge-reranker-v2-m3) is a high-performance, multilingual reranking model that works well on messy data and short queries expected to return medium-length passages of text (1-2 paragraphs).

    **Details**

    * Modality: Text
    * Max tokens per query and document pair: 1024
    * Max documents: 100

    For rate limits, see [Rerank requests per minute](/reference/api/database-limits#rerank-requests-per-minute-per-model) and [Rerank request per month](/reference/api/database-limits#rerank-requests-per-month-per-model).

    **Parameters**

    The `bge-reranker-v2-m3` model supports the following parameters:

    | Parameter     | Type             | Required/Optional | Description                                                                                                                                                                                                                                    | Default    |
    | :------------ | :--------------- | :---------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------- |
    | `truncate`    | string           | Optional          | How to handle inputs longer than those supported by the model. Accepted values: `END` or `NONE`.<br /><br />`END` truncates the input sequence at the input token limit. `NONE` returns an error when the input exceeds the input token limit. | `NONE`     |
    | `rank_fields` | array of strings | Optional          | The field to use for reranking. The model supports only a single rerank field.                                                                                                                                                                 | `["text"]` |
  </Accordion>

  <Accordion title="pinecone-rerank-v0">
    <PP />

    [`pinecone-rerank-v0`](/models/pinecone-rerank-v0) is a state of the art reranking model that out-performs competitors on widely accepted benchmarks. It can handle chunks up to 512 tokens (1-2 paragraphs).

    **Details**

    * Modality: Text
    * Max tokens per query and document pair: 512
    * Max documents: 100

    For rate limits, see [Rerank requests per minute](/reference/api/database-limits#rerank-requests-per-minute-per-model) and [Rerank request per month](/reference/api/database-limits#rerank-requests-per-month-per-model).

    **Parameters**

    The `pinecone-rerank-v0` model supports the following parameters:

    | Parameter     | Type             | Required/Optional | Description                                                                                                                                                                                                                                    | Default    |
    | :------------ | :--------------- | :---------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------- |
    | `truncate`    | string           | Optional          | How to handle inputs longer than those supported by the model. Accepted values: `END` or `NONE`.<br /><br />`END` truncates the input sequence at the input token limit. `NONE` returns an error when the input exceeds the input token limit. | `END`      |
    | `rank_fields` | array of strings | Optional          | The field to use for reranking. The model supports only a single rerank field.                                                                                                                                                                 | `["text"]` |
  </Accordion>
</AccordionGroup>



---
**Navigation:** [← Previous](./13-create-a-project.md) | [Index](./index.md) | [Next →](./15-search-overview.md)
