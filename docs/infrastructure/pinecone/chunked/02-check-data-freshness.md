**Navigation:** [← Previous](./01-concepts.md) | [Index](./index.md) | [Next →](./03-delete-all-chunks-for-a-document.md)

# Check data freshness
Source: https://docs.pinecone.io/guides/index-data/check-data-freshness

Monitor data freshness in Pinecone using log sequence numbers and vector counts.

Pinecone is eventually consistent, so there can be a slight delay before new or changed records are visible to queries. This page describes two ways of checking the data freshness of a Pinecone index:

* To check if a serverless index queries reflect recent writes to the index, [check the log sequence number](#check-the-log-sequence-number).

* To check whether an index contains recently inserted or deleted vectors, [verify the number of vectors in the index](#verify-vector-counts).


## Check the log sequence number

<Note>
  This method is only available for serverless indexes through the [Database API](https://docs.pinecone.io/reference/api/latest/data-plane/upsert).
</Note>

### Log sequence numbers

When you make a write request to a serverless index namespace, Pinecone assigns a monotonically increasing log sequence number (LSN) to the write operation. The LSN reflects upserts as well as updates and deletes to that namespace. Writes to one namespace do not increase the LSN for other namespaces.

You can use LSNs to verify that specific write operations are reflected in your query responses. If the LSN contained in the query response header is greater than or equal to the LSN of the relevant write operation, then that operation is reflected in the query response. If the LSN contained in the query response header is *greater than* the LSN of the relevant write operation, then subsequent operations are also reflected in the query response.

Follow the steps below to compare the LSNs for a write and a subsequent query.

### 1. Get the LSN for a write operation

Every time you modify records in your namespace, the HTTP response contains the LSN for the upsert. This is contained in a header called `x-pinecone-request-lsn`.

The following example demonstrates how to get the LSN for an `upsert` request using the `curl` option `-i`. This option tells curl to include headers in the displayed response. Use the same method to get the LSN for an `update` or `delete` request.

```shell curl theme={null}
PINECONE_API_KEY="YOUR_API_KEY"
INDEX_HOST="INDEX_HOST"

curl -i "https://$INDEX_HOST/vectors/upsert" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "content-type: application/json" \
  -H "X-Pinecone-API-Version: 2025-04" \
  -d '{
        "vectors": [
          {
            "id": "vec1",
            "values": [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8],
          }
        ],
        "namespace": "example-namespace"
      }'
```

The preceding request receives a response like the following example:

```shell curl theme={null}
HTTP/2 200 
date: Wed, 21 Aug 2024 15:23:04 GMT
content-type: application/json
content-length: 66
x-pinecone-max-indexed-lsn: 4
x-pinecone-request-latency-ms: 1149
x-pinecone-request-id: 3687967458925971419
x-envoy-upstream-service-time: 1150
grpc-status: 0
server: envoy

{"upsertedCount":1}
```

In the preceding example response, the value of `x-pinecone-max-indexed-lsn` is 4. This means that the index has performed 4 write operations since its creation.

### 2. Get the LSN for a query

Every time you query your index, the HTTP response contains the LSN for the query. This is contained in a header called `x-pinecone-max-indexed-lsn`.

By checking the LSN in your query results, you can confirm that the LSN is greater than or equal to the LSN of the relevant write operation, indicating that the results of that operation are present in the query results.

The following example makes a `query` request to the index:

```shell  theme={null}
PINECONE_API_KEY="YOUR_API_KEY"
INDEX_HOST="INDEX_HOST"

curl -i "https://$INDEX_HOST/query" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "X-Pinecone-API-Version: 2025-04" \
  -d '{
    "vector": [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3],
    "namespace": "example-namespace",
    "topK": 3,
    "includeValues": true
  }'
```

The preceding request receives a response like the following example:

```shell  theme={null}
HTTP/2 200 
date: Wed, 21 Aug 2024 15:33:36 GMT
content-type: application/json
content-length: 66
x-pinecone-max-indexed-lsn: 5
x-pinecone-request-latency-ms: 40
x-pinecone-request-id: 6683088825552978933
x-envoy-upstream-service-time: 41
grpc-status: 0
server: envoy

{
  "results":[],
  "matches":[
    {
      "id":"vec1",
      "score":0.891132772,
      "values":[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8],
    }
  ],
  "namespace":"example-namespace",
  "usage":{"readUnits":6}
}
```

In the preceding example response, the value of `x-pinecone-max-indexed-lsn` is 5.

### 3. Compare LSNs for writes and queries

If the LSN of a query is greater than or equal to the LSN for a write operation, then the results of the query reflect the results of the write operation.

In [step 1](#1-get-the-lsn-for-a-write-operation), the LSN contained in the response headers is 4.

In [step 2](#2-get-the-lsn-for-a-query), the LSN contained in the response headers is 5.

5 is greater than or equal to 4; therefore, the results of the query reflect the results of the upsert. However, this does not guarantee that the records upserted are still present or unmodified: the write operation with LSN of 5 may have updated or deleted these records, or upserted additional records.


## Verify record counts

If you insert new records or delete records, the number of records in the index may change. This means that the record count for an index can indicate whether Pinecone has indexed your latest inserts and deletes: if the record count for the index matches the count you expect after inserting or deleting records, the index is probably up-to-date. However, this is not always true. For example, if you delete the same number of records that you insert, the expected record count may remain the same. Also, some write operations, such as updates to an index configuration or vector data values, do not change the number of records in the index.

To verify that your index contains the number of records you expect, [view index stats](/reference/api/latest/data-plane/describeindexstats):

<CodeGroup>
  ```python Python theme={null}
  # pip install "pinecone[grpc]"
  from pinecone.grpc import PineconeGRPC as Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  # To get the unique host for an index, 
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  index = pc.Index(host="INDEX_HOST")

  index.describe_index_stats()
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' })

  // To get the unique host for an index, 
  // see https://docs.pinecone.io/guides/manage-data/target-an-index
  const index = pc.index("INDEX_NAME", "INDEX_HOST")

  const stats = await index.describeIndexStats();
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Index;
  import io.pinecone.configs.PineconeConfig;
  import io.pinecone.configs.PineconeConnection;
  import io.pinecone.proto.DescribeIndexStatsResponse;

  public class DescribeIndexStatsExample {
      public static void main(String[] args) {
          PineconeConfig config = new PineconeConfig("YOUR_API_KEY");
          // To get the unique host for an index, 
          // see https://docs.pinecone.io/guides/manage-data/target-an-index
          config.setHost("INDEX_HOST");
          PineconeConnection connection = new PineconeConnection(config);
          Index index = new Index(connection, "INDEX_NAME");
          DescribeIndexStatsResponse indexStatsResponse = index.describeIndexStats();
          System.out.println(indexStatsResponse);
      }
  }
  ```

  ```go Go theme={null}
  package main

  import (
      "context"
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

      // To get the unique host for an index, 
      // see https://docs.pinecone.io/guides/manage-data/target-an-index
      idxConnection, err := pc.Index(pinecone.NewIndexConnParams{Host: "INDEX_HOST"})
      if err != nil {
          log.Fatalf("Failed to create IndexConnection for Host: %v", err)
    	}

      stats, err := idxConnection.DescribeIndexStats(ctx)
      if err != nil {
          log.Fatalf("Failed to describe index \"%v\": %v", idx.Name, err)
      } else {
          fmt.Printf("%+v", *stats)
      }
  }
  ```

  ```csharp C# theme={null}
  using Pinecone;

  var pinecone = new PineconeClient("YOUR_API_KEY");

  // To get the unique host for an index, 
  // see https://docs.pinecone.io/guides/manage-data/target-an-index
  var index = pinecone.Index(host: "INDEX_HOST");

  var indexStatsResponse = await index.DescribeIndexStatsAsync(new DescribeIndexStatsRequest());

  Console.WriteLine(indexStatsResponse);
  ```

  ```shell curl theme={null}
  # To get the unique host for an index,
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="INDEX_HOST"

  curl -X POST "https://$INDEX_HOST/describe_index_stats" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-API-Version: 2025-04"
  ```
</CodeGroup>

The response will look like this:

<CodeGroup>
  ```Python Python theme={null}
  {'dimension': 1024,
   'index_fullness': 0,
   'namespaces': {'example-namespace1': {'vector_count': 4}, 'example-namespace2': {'vector_count': 4}},
   'total_vector_count': 8}
  ```

  ```JavaScript JavaScript theme={null}
  Returns:
  {
    namespaces: { example-namespace1: { recordCount: 4 }, example-namespace2: { recordCount: 4 } },
    dimension: 1024,
    indexFullness: 0,
    totalRecordCount: 8
  }

  // Note: the value of totalRecordCount is the same as total_vector_count.
  ```

  ```java Java theme={null}
  namespaces {
    key: "example-namespace1"
    value {
      vector_count: 4
    }
  }
  namespaces {
    key: "example-namespace2"
    value {
      vector_count: 4
    }
  }
  dimension: 1024
  total_vector_count: 8
  ```

  ```go Go theme={null}
  {
    "dimension": 1024,
    "index_fullness": 0,
    "total_vector_count": 8,
    "namespaces": {
      "example-namespace1": {
        "vector_count": 4
      },
      "example-namespace2": {
        "vector_count": 4
      }
    }
  }
  ```

  ```csharp C# theme={null}
  {
    "namespaces": {
      "example-namespace1": {
        "vectorCount": 4
      },
      "example-namespace2": {
        "vectorCount": 4
      }
    },
    "dimension": 1024,
    "indexFullness": 0,
    "totalVectorCount": 8
  }
  ```

  ```shell curl theme={null}
  {
    "namespaces": {
      "example-namespace1": {
        "vectorCount": 4
      },
      "example-namespace2": {
        "vectorCount": 4
      }
    },
    "dimension": 1024,
    "indexFullness": 0,
    "totalVectorCount": 8
  }
  ```
</CodeGroup>



# Create an index
Source: https://docs.pinecone.io/guides/index-data/create-an-index

Create dense or sparse indexes for semantic and lexical search.

* **Dense indexes** store dense vectors, which are numerical representations of the meaning and relationships of text, images, or other types of data. You use dense indexes for [semantic search](/guides/search/semantic-search) or in combination with sparse indexes for [hybrid search](/guides/search/hybrid-search).

* **Sparse indexes** store sparse vectors, which are numerical representations of the words or phrases in a document. You use sparse indexes for [lexical search](/guides/search/lexical-search), or in combination with dense indexes for [hybrid search](/guides/search/hybrid-search).

<Tip>
  You can create an index using the [Pinecone console](https://app.pinecone.io/organizations/-/projects/-/create-index/serverless).
</Tip>


## Create a dense index

You can create a dense index with [integrated vector embedding](/guides/index-data/indexing-overview#integrated-embedding) or a dense index for storing vectors generated with an external embedding model.

### Integrated embedding

<Note>
  Indexes with integrated embedding do not support [updating](/guides/manage-data/update-data) or [importing](/guides/index-data/import-data) with text.
</Note>

If you want to upsert and search with source text and have Pinecone convert it to dense vectors automatically, [create a dense index with integrated embedding](/reference/api/latest/control-plane/create_for_model) as follows:

* Provide a `name` for the index.
* Set `cloud` and `region` to the [cloud and region](/guides/index-data/create-an-index#cloud-regions) where the index should be deployed.
* Set `embed.model` to one of [Pinecone's hosted embedding models](/guides/index-data/create-an-index#embedding-models).
* Set `embed.field_map` to the name of the field in your source document that contains the data for embedding.

Other parameters are optional. See the [API reference](/reference/api/latest/control-plane/create_for_model) for details.

<CodeGroup>
  ```python Python theme={null}
  from pinecone import Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  index_name = "integrated-dense-py"

  if not pc.has_index(index_name):
      pc.create_index_for_model(
          name=index_name,
          cloud="aws",
          region="us-east-1",
          embed={
              "model":"llama-text-embed-v2",
              "field_map":{"text": "chunk_text"}
          }
      )
  ```

  ```javascript JavaScript theme={null}
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
          pc.createIndexForModel(
                  indexName,
                  CreateIndexForModelRequest.CloudEnum.AWS,
                  region,
                  embed,
                  DeletionProtection.DISABLED,
                  tags
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

    	indexName := "integrated-dense-go"
     	deletionProtection := pinecone.DeletionProtectionDisabled

      idx, err := pc.CreateIndexForModel(ctx, &pinecone.CreateIndexForModelRequest{
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
              FieldMap = new Dictionary<string, object?>() 
              { 
                  { "text", "chunk_text" } 
              }
          },
          DeletionProtection = DeletionProtection.Disabled,
          Tags = new Dictionary<string, string> 
          { 
              { "environment", "development" }
          }
      }
  );
  ```

  ```json curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl -X POST "https://api.pinecone.io/indexes/create-for-model" \
       -H "Content-Type: application/json" \
       -H "Api-Key: $PINECONE_API_KEY" \
       -H "X-Pinecone-API-Version: 2025-04" \
       -d '{
             "name": "integrated-dense-curl",
             "cloud": "aws",
             "region": "us-east-1",
             "embed": {
               "model": "llama-text-embed-v2",
               "field_map": {
                 "text": "chunk_text"
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
    --metric "cosine" \
    --cloud "aws" \
    --region "us-east-1" \
    --model "llama-text-embed-v2" \
    --field_map "text=chunk_text" \
    --tags "environment=development"
  ```
</CodeGroup>

### Bring your own vectors

If you use an external embedding model to convert your data to dense vectors, [create a dense index](/reference/api/latest/control-plane/create_index) as follows:

* Provide a `name` for the index.
* Set the `vector_type` to `dense`.
* Specify the `dimension` and similarity `metric` of the vectors you'll store in the index. This should match the dimension and metric supported by your embedding model.
* Set `spec.cloud` and `spec.region` to the [cloud and region](/guides/index-data/create-an-index#cloud-regions) where the index should be deployed. For Python, you also need to import the `ServerlessSpec` class.

Other parameters are optional. See the [API reference](/reference/api/latest/control-plane/create_index) for details.

<CodeGroup>
  ```python Python theme={null}
  from pinecone.grpc import PineconeGRPC as Pinecone
  from pinecone import ServerlessSpec

  pc = Pinecone(api_key="YOUR_API_KEY")

  index_name = "standard-dense-py"

  if not pc.has_index(index_name):
      pc.create_index(
          name=index_name,
          vector_type="dense",
          dimension=1536,
          metric="cosine",
          spec=ServerlessSpec(
              cloud="aws",
              region="us-east-1"
          ),
          deletion_protection="disabled",
          tags={
              "environment": "development"
          }
      )
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  await pc.createIndex({
    name: 'standard-dense-js',
    vectorType: 'dense',
    dimension: 1536,
    metric: 'cosine',
    spec: {
      serverless: {
        cloud: 'aws',
        region: 'us-east-1'
      }
    },
    deletionProtection: 'disabled',
    tags: { environment: 'development' }, 
  });
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Pinecone;
  import org.openapitools.db_control.client.model.IndexModel;
  import org.openapitools.db_control.client.model.DeletionProtection;
  import java.util.HashMap;

  public class CreateServerlessIndexExample {
      public static void main(String[] args) {
          Pinecone pc = new Pinecone.Builder("YOUR_API_KEY").build();
          String indexName = "standard-dense-java";
          String cloud = "aws";
          String region = "us-east-1";
          String vectorType = "dense";
          Map<String, String> tags = new HashMap<>();
          tags.put("environment", "development");
          pc.createServerlessIndex(
              indexName,
              "cosine", 
              1536, 
              cloud,
              region,
              DeletionProtection.DISABLED, 
              tags, 
              vectorType
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

      // Serverless index
    	indexName := "standard-dense-go"
  	vectorType := "dense"
      dimension := int32(1536)
      metric := pinecone.Cosine
  	deletionProtection := pinecone.DeletionProtectionDisabled

      idx, err := pc.CreateServerlessIndex(ctx, &pinecone.CreateServerlessIndexRequest{
          Name:               indexName,
          VectorType:         &vectorType,
          Dimension:          &dimension,
          Metric:             &metric,
          Cloud:              pinecone.Aws,
          Region:             "us-east-1",
          DeletionProtection: &deletionProtection,
          Tags:               &pinecone.IndexTags{ "environment": "development" },
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
      Name = "standard-dense-dotnet",
      VectorType = VectorType.Dense,
      Dimension = 1536,
      Metric = MetricType.Cosine,
      Spec = new ServerlessIndexSpec
      {
          Serverless = new ServerlessSpec
          {
              Cloud = ServerlessSpecCloud.Aws,
              Region = "us-east-1"
          }
      },
      DeletionProtection = DeletionProtection.Disabled,
      Tags = new Dictionary<string, string> 
      {  
          { "environment", "development" }
      }
  });
  ```

  ```shell curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl -X POST "https://api.pinecone.io/indexes" \
       -H "Accept: application/json" \
       -H "Content-Type: application/json" \
       -H "Api-Key: $PINECONE_API_KEY" \
       -H "X-Pinecone-API-Version: 2025-04" \
       -d '{
             "name": "standard-dense-curl",
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
                "environment": "development"
              },
              "deletion_protection": "disabled"
           }'
  ```

  ```bash CLI theme={null}
  # Target the project where you want to create the index.
  pc target -o "example-org" -p "example-project"
  # Create the index.
  pc index create \
    --name "standard-dense-cli" \
    --vector_type "dense" \
    --dimension 1536 \
    --metric "cosine" \
    --cloud "aws" \
    --region "us-east-1" \
    --tags "environment=development" \
    --deletion_protection "disabled"
  ```
</CodeGroup>


## Create a sparse index

You can create a sparse index with [integrated vector embedding](/guides/index-data/indexing-overview#integrated-embedding) or a sparse index for storing vectors generated with an external embedding model.

### Integrated embedding

If you want to upsert and search with source text and have Pinecone convert it to sparse vectors automatically, [create a sparse index with integrated embedding](/reference/api/latest/control-plane/create_for_model) as follows:

* Provide a `name` for the index.
* Set `cloud` and `region` to the [cloud and region](/guides/index-data/create-an-index#cloud-regions) where the index should be deployed.
* Set `embed.model` to one of [Pinecone's hosted sparse embedding models](/guides/index-data/create-an-index#embedding-models).
* Set `embed.field_map` to the name of the field in your source document that contains the text for embedding.
* If needed, `embed.read_parameters` and `embed.write_parameters` can be used to override the default model embedding behavior.

Other parameters are optional. See the [API reference](/reference/api/latest/control-plane/create_for_model) for details.

<CodeGroup>
  ```python Python theme={null}
  from pinecone import Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  index_name = "integrated-sparse-py"

  if not pc.has_index(index_name):
      pc.create_index_for_model(
          name=index_name,
          cloud="aws",
          region="us-east-1",
          embed={
              "model":"pinecone-sparse-english-v0",
              "field_map":{"text": "chunk_text"}
          }
      )
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  await pc.createIndexForModel({
    name: 'integrated-sparse-js',
    cloud: 'aws',
    region: 'us-east-1',
    embed: {
      model: 'pinecone-sparse-english-v0',
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
  import java.util.HashMap;
  import java.util.Map;

  public class CreateIntegratedIndex {
      public static void main(String[] args) throws ApiException {
          Pinecone pc = new Pinecone.Builder("YOUR_API_KEY").build();
          String indexName = "integrated-sparse-java";
          String region = "us-east-1";
          HashMap<String, String> fieldMap = new HashMap<>();
          fieldMap.put("text", "chunk_text");
          CreateIndexForModelRequestEmbed embed = new CreateIndexForModelRequestEmbed()
                  .model("pinecone-sparse-english-v0")
                  .fieldMap(fieldMap);
          Map<String, String> tags = new HashMap<>();
          tags.put("environment", "development");
          pc.createIndexForModel(
                  indexName,
                  CreateIndexForModelRequest.CloudEnum.AWS,
                  region,
                  embed,
                  DeletionProtection.DISABLED,
                  tags
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

    	indexName := "integrated-sparse-go"
  	deletionProtection := pinecone.DeletionProtectionDisabled

      idx, err := pc.CreateIndexForModel(ctx, &pinecone.CreateIndexForModelRequest{
  		Name:   indexName,
  		Cloud:  pinecone.Aws,
  		Region: "us-east-1",
  		Embed: pinecone.CreateIndexForModelEmbed{
  			Model:    "pinecone-sparse-english-v0",
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
          Name = "integrated-sparse-dotnet",
          Cloud = CreateIndexForModelRequestCloud.Aws,
          Region = "us-east-1",
          Embed = new CreateIndexForModelRequestEmbed
          {
              Model = "pinecone-sparse-english-v0",
              FieldMap = new Dictionary<string, object?>() 
              { 
                  { "text", "chunk_text" } 
              }
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

  curl -X POST "https://api.pinecone.io/indexes/create-for-model" \
       -H "Content-Type: application/json" \
       -H "Api-Key: $PINECONE_API_KEY" \
       -H "X-Pinecone-API-Version: 2025-04" \
       -d '{
             "name": "integrated-sparse-curl",
             "cloud": "aws",
             "region": "us-east-1",
             "embed": {
               "model": "pinecone-sparse-english-v0",
               "field_map": {
                 "text": "chunk_text"
               }
             }
           }'
  ```

  ```bash CLI theme={null}
  # Target the project where you want to create the index.
  pc target -o "example-org" -p "example-project"
  # Create the index.
  pc index create \
    --name "integrated-sparse-cli" \
    --cloud "aws" \
    --region "us-east-1" \
    --model "pinecone-sparse-english-v0" \
    --field_map "text=chunk_text" \
    --tags "environment=development"
  ```
</CodeGroup>

### Bring your own vectors

If you use an external embedding model to convert your data to sparse vectors, [create a sparse index](/reference/api/latest/control-plane/create_index) as follows:

* Provide a `name` for the index.
* Set the `vector_type` to `sparse`.
* Set the distance `metric` to `dotproduct`. Sparse indexes do not support other [distance metrics](/guides/index-data/indexing-overview#distance-metrics).
* Set `spec.cloud` and `spec.region` to the cloud and region where the index should be deployed.

Other parameters are optional. See the [API reference](/reference/api/latest/control-plane/create_index) for details.

<CodeGroup>
  ```python Python theme={null}
  from pinecone import Pinecone, ServerlessSpec

  pc = Pinecone(api_key="YOUR_API_KEY")

  index_name = "standard-sparse-py"

  if not pc.has_index(index_name):
      pc.create_index(
          name=index_name,
          vector_type="sparse",
          metric="dotproduct",
          spec=ServerlessSpec(cloud="aws", region="us-east-1")
      )
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  await pc.createIndex({
    name: 'standard-sparse-js',
    vectorType: 'sparse',
    metric: 'dotproduct',
    spec: {
      serverless: {
        cloud: 'aws',
        region: 'us-east-1'
      },
    },
  });
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Pinecone;
  import org.openapitools.db_control.client.model.DeletionProtection;

  import java.util.*;

  public class SparseIndex {
      public static void main(String[] args) throws InterruptedException {
          // Instantiate Pinecone class
          Pinecone pinecone = new Pinecone.Builder("YOUR_API_KEY").build();

          // Create sparse Index
          String indexName = "standard-sparse-java";
          String cloud = "aws";
          String region = "us-east-1";
          String vectorType = "sparse";
          Map<String, String> tags = new HashMap<>();
          tags.put("env", "test");
          pinecone.createSparseServelessIndex(indexName,
                  cloud,
                  region,
                  DeletionProtection.DISABLED,
                  tags,
                  vectorType);
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

  	indexName := "standard-sparse-go"
  	vectorType := "sparse"
  	metric := pinecone.Dotproduct
  	deletionProtection := pinecone.DeletionProtectionDisabled

  	idx, err := pc.CreateServerlessIndex(ctx, &pinecone.CreateServerlessIndexRequest{
  		Name:               indexName,
  		Metric:             &metric,
  		VectorType:         &vectorType,
  		Cloud:              pinecone.Aws,
  		Region:             "us-east-1",
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
      Name = "standard-sparse-dotnet",
      VectorType = VectorType.Sparse,
      Metric = MetricType.Dotproduct,
      Spec = new ServerlessIndexSpec
      {
          Serverless = new ServerlessSpec
          {
              Cloud = ServerlessSpecCloud.Aws,
              Region = "us-east-1"
          }
      }
  });
  ```

  ```shell curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl -X POST "https://api.pinecone.io/indexes" \
       -H "Accept: application/json" \
       -H "Content-Type: application/json" \
       -H "Api-Key: $PINECONE_API_KEY" \
       -H "X-Pinecone-API-Version: 2025-04" \
       -d '{
              "name": "standard-sparse-curl",
              "vector_type": "sparse",
              "metric": "dotproduct",
              "spec": {
                 "serverless": {
                    "cloud": "aws",
                    "region": "us-east-1"
                 }
              }
           }'
  ```

  ```bash CLI theme={null}
  # Target the project where you want to create the index.
  pc target -o "example-org" -p "example-project"
  # Create the index.
  pc index create \
    --name "standard-sparse-cli" \
    --vector_type "sparse" \
    --metric "dotproduct" \
    --cloud "aws" \
    --region "us-east-1" \
    --tags "environment=development"
  ```
</CodeGroup>


## Create an index from a backup

You can create a dense or sparse index from a backup. For more details, see [Restore an index](/guides/manage-data/restore-an-index).


## Metadata indexing

<Warning>
  This feature is in [early access](/release-notes/feature-availability) and available only on the `2025-10` version of the API. The CLI does not yet support this feature.
</Warning>

Pinecone indexes all metadata fields by default. However, large amounts of metadata can cause slower [index building](/guides/get-started/database-architecture#index-builder) as well as slower [query execution](/guides/get-started/database-architecture#query-executors), particularly when data is not cached in a query executor's memory and local SSD and must be fetched from object storage.

To prevent performance issues due to excessive metadata, you can limit metadata indexing to the fields that you plan to use for [query filtering](/guides/search/filter-by-metadata).

### Set metadata indexing

You can set metadata indexing during index creation or [namespace creation](/reference/api/2025-10/data-plane/createnamespace):

* Index-level metadata indexing rules apply to all namespaces that don't have explicit metadata indexing rules.
* Namespace-level metadata indexing rules overrides index-level metadata indexing rules.

For example, let's say you want to store records that represent chunks of a document, with each record containing many metadata fields. Since you plan to use only a few of the metadata fields to filter queries, you would specify the metadata fields to index as follows.

<Warning>
  Metadata indexing cannot be changed after index or namespace creation.
</Warning>

<CodeGroup>
  ```shell Index-level metadata indexing theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl "https://api.pinecone.io/indexes" \
    -H "Accept: application/json" \
    -H "Content-Type: application/json" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-API-Version: 2025-10" \
    -d '{
          "name": "example-index-metadata",
          "vector_type": "dense",
          "dimension": 1536,
          "metric": "cosine",
          "spec": {
            "serverless": {
              "cloud": "aws",
              "region": "us-east-1",
              "schema": {
                "fields": {
                  "document_id": {
                    "filterable": true
                  },
                  "document_title": {
                    "filterable": true
                  },
                  "chunk_number": {
                    "filterable": true
                  },
                  "document_url": {
                    "filterable": true
                  },
                  "created_at": {
                    "filterable": true
                  }
                }
              }
            }
          },
          "deletion_protection": "disabled"
        }'
  ```

  ```shell Namespace-level metadata indexing theme={null}
  # To learn how to get the unique host for an index,
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="INDEX_HOST"

  curl "https://$INDEX_HOST/namespaces" \
    -H "Accept: application/json" \
    -H "Content-Type: application/json" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-API-Version: 2025-10" \
    -d '{
          "name": "example-namespace",
          "schema": {
            "fields": {
              "document_id": {
                "filterable": true
              },
              "document_title": {
                "filterable": true
              },
              "chunk_number": {
                "filterable": true
              },
              "document_url": {
                "filterable": true
              },
              "created_at": {
                "filterable": true
              }
            }
          }
        }'
  ```
</CodeGroup>

### Check metadata indexing

To check which metadata fields are indexed, you can describe the index or namespace:

<CodeGroup>
  ```shell Describe index theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl -X GET "https://api.pinecone.io/indexes/example-index-metadata" \
       -H "Api-Key: $PINECONE_API_KEY" \
       -H "X-Pinecone-API-Version: 2025-10"
  ```

  ```shell Describe namespace theme={null}
  # To learn how to get the unique host for an index,
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="INDEX_HOST"

  curl -X GET "https://$INDEX_HOST/namespaces/example-namespace" \
       -H "Api-Key: $PINECONE_API_KEY" \
       -H "X-Pinecone-API-Version: 2025-10"
  ```
</CodeGroup>

The response includes the `schema` object with the names of the metadata fields explicitly indexed during index or namespace creation.

<Note>
  The response does not include unindexed metadata fields or metadata fields indexed by default.
</Note>

<CodeGroup>
  ```json Describe index theme={null}
  {
    "id": "751ab850-6e61-4f92-bd23-fa129803d207",
    "vector_type": "dense",
    "name": "example-index",
    "metric": "cosine",
    "dimension": 1536,
    "status": {
      "ready": false,
      "state": "Initializing"
    },
    "host": "example-index-fa77d8e.svc.aped-4627-b74a.pinecone.io",
    "spec": {
      "serverless": {
        "region": "us-east-1",
        "cloud": "aws",
        "read_capacity": {
          "mode": "OnDemand",
          "status": "Ready"
        },
        "schema": {
          "fields": {
            "document_id": {
              "filterable": true
            },
            "document_title": {
              "filterable": true
            },
            "created_at": {
              "filterable": true
            },
            "chunk_number": {
              "filterable": true
            },
            "document_url": {
              "filterable": true
            }
          }
        }
      }
    },
    "deletion_protection": "disabled",
    "tags": null
  }

  ```

  ```json Describe namespace theme={null}
  {
    "name": "example-namespace",
    "record_count": "20000",
    "schema": {
      "fields": {
        "document_title": {
          "filterable": true
        },
        "document_url": {
          "filterable": true
        },
        "chunk_number": {
          "filterable": true
        },
        "document_id": {
          "filterable": true
        },
        "created_at": {
          "filterable": true
        }
      }
    }
  }
  ```
</CodeGroup>


## Index options

### Cloud regions

When creating an index, you must choose the cloud and region where you want the index to be hosted. The following table lists the available public clouds and regions and the plans that support them:

| Cloud   | Region                       | [Supported plans](https://www.pinecone.io/pricing/) | [Availability phase](/release-notes/feature-availability) |
| ------- | ---------------------------- | --------------------------------------------------- | --------------------------------------------------------- |
| `aws`   | `us-east-1` (Virginia)       | Starter, Standard, Enterprise                       | General availability                                      |
| `aws`   | `us-west-2` (Oregon)         | Standard, Enterprise                                | General availability                                      |
| `aws`   | `eu-west-1` (Ireland)        | Standard, Enterprise                                | General availability                                      |
| `gcp`   | `us-central1` (Iowa)         | Standard, Enterprise                                | General availability                                      |
| `gcp`   | `europe-west4` (Netherlands) | Standard, Enterprise                                | General availability                                      |
| `azure` | `eastus2` (Virginia)         | Standard, Enterprise                                | General availability                                      |

The cloud and region cannot be changed after a serverless index is created.

<Note>
  On the free Starter plan, you can create serverless indexes in the `us-east-1` region of AWS only. To create indexes in other regions, [upgrade your plan](/guides/organizations/manage-billing/upgrade-billing-plan).
</Note>

### Similarity metrics

When creating a dense index, you can choose from the following similarity metrics. For the most accurate results, choose the similarity metric used to train the embedding model for your vectors. For more information, see [Vector Similarity Explained](https://www.pinecone.io/learn/vector-similarity/).

<Note>[Sparse indexes](#sparse-indexes) must use the `dotproduct` metric.</Note>

<AccordionGroup>
  <Accordion title="Euclidean">
    Querying indexes with this metric returns a similarity score equal to the squared Euclidean distance between the result and query vectors.

    This metric calculates the square of the distance between two data points in a plane. It is one of the most commonly used distance metrics. For an example, see our [IT threat detection example](https://colab.research.google.com/github/pinecone-io/examples/blob/master/docs/it-threat-detection.ipynb).

    When you use `metric='euclidean'`, the most similar results are those with the **lowest similarity score**.
  </Accordion>

  <Accordion title="Cosine">
    This is often used to find similarities between different documents. The advantage is that the scores are normalized to \[-1,1] range. For an example, see our [generative question answering example](https://colab.research.google.com/github/pinecone-io/examples/blob/master/docs/gen-qa-openai.ipynb).
  </Accordion>

  <Accordion title="Dotproduct">
    This is used to multiply two vectors. You can use it to tell us how similar the two vectors are. The more positive the answer is, the closer the two vectors are in terms of their directions. For an example, see our [semantic search example](https://colab.research.google.com/github/pinecone-io/examples/blob/master/docs/semantic-search.ipynb).
  </Accordion>
</AccordionGroup>

### Embedding models

[Dense vectors](/guides/get-started/concepts#dense-vector) and [sparse vectors](/guides/get-started/concepts#sparse-vector) are the basic units of data in Pinecone and what Pinecone was specially designed to store and work with. Dense vectors represents the semantics of data such as text, images, and audio recordings, while sparse vectors represent documents or queries in a way that captures keyword information.

To transform data into vector format, you use an embedding model. Pinecone hosts several embedding models so it's easy to manage your vector storage and search process on a single platform. You can use a hosted model to embed your data as an integrated part of upserting and querying, or you can use a hosted model to embed your data as a standalone operation.

The following embedding models are hosted by Pinecone.

<Note>
  To understand how cost is calculated for embedding, see [Embedding cost](/guides/manage-cost/understanding-cost#embedding). To get model details via the API, see [List models](/reference/api/latest/inference/list_models) and [Describe a model](/reference/api/latest/inference/describe_model).
</Note>

#### multilingual-e5-large

[`multilingual-e5-large`](/models/multilingual-e5-large) is an efficient dense embedding model trained on a mixture of multilingual datasets. It works well on messy data and short queries expected to return medium-length passages of text (1-2 paragraphs).

**Details**

* Vector type: Dense
* Modality: Text
* Dimension: 1024
* Recommended similarity metric: Cosine
* Max sequence length: 507 tokens
* Max batch size: 96 sequences

For rate limits, see [Embedding tokens per minute](/reference/api/database-limits#embedding-tokens-per-minute-per-model) and [Embedding tokens per month](/reference/api/database-limits#embedding-tokens-per-month-per-model).

**Parameters**

The `multilingual-e5-large` model supports the following parameters:

| Parameter    | Type   | Required/Optional | Description                                                                                                                                                                                                                                    | Default |
| :----------- | :----- | :---------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------ |
| `input_type` | string | Required          | The type of input data. Accepted values: `query` or `passage`.                                                                                                                                                                                 |         |
| `truncate`   | string | Optional          | How to handle inputs longer than those supported by the model. Accepted values: `END` or `NONE`.<br /><br />`END` truncates the input sequence at the input token limit. `NONE` returns an error when the input exceeds the input token limit. | `END`   |

#### llama-text-embed-v2

[`llama-text-embed-v2`](/models/llama-text-embed-v2) is a high-performance dense embedding model optimized for text retrieval and ranking tasks. It is trained on a diverse range of text corpora and provides strong performance on longer passages and structured documents.

**Details**

* Vector type: Dense
* Modality: Text
* Dimension: 1024 (default), 2048, 768, 512, 384
* Recommended similarity metric: Cosine
* Max sequence length: 2048 tokens
* Max batch size: 96 sequences

For rate limits, see [Embedding tokens per minute](/reference/api/database-limits#embedding-tokens-per-minute-per-model) and [Embedding tokens per month](/reference/api/database-limits#embedding-tokens-per-month-per-model).

**Parameters**

The `llama-text-embed-v2` model supports the following parameters:

| Parameter    | Type    | Required/Optional | Description                                                                                                                                                                                                                                    | Default |
| :----------- | :------ | :---------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------ |
| `input_type` | string  | Required          | The type of input data. Accepted values: `query` or `passage`.                                                                                                                                                                                 |         |
| `truncate`   | string  | Optional          | How to handle inputs longer than those supported by the model. Accepted values: `END` or `NONE`.<br /><br />`END` truncates the input sequence at the input token limit. `NONE` returns an error when the input exceeds the input token limit. | `END`   |
| `dimension`  | integer | Optional          | Dimension of the vector to return.                                                                                                                                                                                                             | 1024    |

#### pinecone-sparse-english-v0

[`pinecone-sparse-english-v0`](/models/pinecone-sparse-english-v0) is a sparse embedding model for converting text to [sparse vectors](/guides/get-started/concepts#sparse-vector) for keyword or hybrid semantic/keyword search. Built on the innovations of the [DeepImpact architecture](https://arxiv.org/pdf/2104.12016), the model directly estimates the lexical importance of tokens by leveraging their context, unlike traditional retrieval models like BM25, which rely solely on term frequency.

**Details**

* Vector type: Sparse
* Modality: Text
* Recommended similarity metric: Dotproduct
* Max sequence length: 512 or 2048
* Max batch size: 96 sequences

For rate limits, see [Embedding tokens per minute](/reference/api/database-limits#embedding-tokens-per-minute-per-model) and [Embedding tokens per month](/reference/api/database-limits#embedding-tokens-per-month-per-model).

**Parameters**

The `pinecone-sparse-english-v0` model supports the following parameters:

| Parameter                 | Type    | Required/Optional | Description                                                                                                                                                                                                                                                                    | Default |
| :------------------------ | :------ | :---------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------ |
| `input_type`              | string  | Required          | The type of input data. Accepted values: `query` or `passage`.                                                                                                                                                                                                                 |         |
| `max_tokens_per_sequence` | integer | Optional          | Maximum number of tokens to embed. Accepted values: `512` or `2048`.                                                                                                                                                                                                           | `512`   |
| `truncate`                | string  | Optional          | How to handle inputs longer than those supported by the model. Accepted values: `END` or `NONE`.<br /><br />`END` truncates the input sequence at the the `max_tokens_per_sequence` limit. `NONE` returns an error when the input exceeds the `max_tokens_per_sequence` limit. | `END`   |
| `return_tokens`           | boolean | Optional          | Whether to return the string tokens.                                                                                                                                                                                                                                           | `false` |



# Data ingestion overview
Source: https://docs.pinecone.io/guides/index-data/data-ingestion-overview

Learn about the different ways to ingest data into Pinecone.

<Tip>
  To control costs when ingesting large datasets (10,000,000+ records), use [import](/guides/index-data/import-data) instead of upsert.
</Tip>


## Import from object storage

[Importing from object storage](/guides/index-data/import-data) is the most efficient and cost-effective method to load large numbers of records into an index. You store your data as Parquet files in object storage, integrate your object storage with Pinecone, and then start an asynchronous, long-running operation that imports and indexes your records.

<Note>
  This feature is in [public preview](/release-notes/feature-availability) and available only on [Standard and Enterprise plans](https://www.pinecone.io/pricing/).
</Note>


## Upsert

For ongoing ingestion into an index, either one record at a time or in batches, use the [upsert](/guides/index-data/upsert-data) operation. [Batch upserting](/guides/index-data/upsert-data#upsert-in-batches) can improve throughput performance and is a good option for larger numbers of records if you cannot work around import's current [limitations](/guides/index-data/import-data#import-limits).


## Ingestion cost

* To understand how cost is calculated for imports, see [Import cost](/guides/manage-cost/understanding-cost#imports).
* To understand how cost is calculated for upserts, see [Upsert cost](/guides/manage-cost/understanding-cost#upsert).
* For up-to-date pricing information, see [Pricing](https://www.pinecone.io/pricing/).


## Data freshness

Pinecone is eventually consistent, so there can be a slight delay before new or changed records are visible to queries. You can view index stats to [check data freshness](/guides/index-data/check-data-freshness).



# Data modeling
Source: https://docs.pinecone.io/guides/index-data/data-modeling

Learn how to structure records for efficient data retrieval and management in Pinecone.


## Record format

<Tabs>
  <Tab title="Text">
    When you upsert raw text for Pinecone to convert to vectors automatically, each record consists of the following:

    * **ID**: A unique string identifier for the record.
    * **Text**: The raw text for Pinecone to convert to a dense vector for [semantic search](/guides/search/semantic-search) or a sparse vector for [lexical search](/guides/search/lexical-search), depending on the [embedding model](/guides/index-data/create-an-index#embedding-models) integrated with the index. This field name must match the `embed.field_map` defined in the index.
    * **Metadata** (optional): All additional fields are stored as record metadata. You can filter by metadata when searching or deleting records.

    <Note>
      Upserting raw text is supported only for [indexes with integrated embedding](/guides/index-data/indexing-overview#vector-embedding).
    </Note>

    Example:

    ```json  theme={null}
    {
      "_id": "document1#chunk1", 
      "chunk_text": "First chunk of the document content...", // Text to convert to a vector. 
      "document_id": "document1", // This and subsequent fields stored as metadata. 
      "document_title": "Introduction to Vector Databases",
      "chunk_number": 1,
      "document_url": "https://example.com/docs/document1", 
      "created_at": "2024-01-15",
      "document_type": "tutorial"
    }
    ```
  </Tab>

  <Tab title="Vectors">
    When you upsert pre-generated vectors, each record consists of the following:

    * **ID**: A unique string identifier for the record.
    * **Vector**: A dense vector for [semantic search](/guides/search/semantic-search), a sparse vector for [lexical search](/guides/search/lexical-search), or both for [hybrid search](/guides/search/hybrid-search) using a single hybrid index.
    * **Metadata** (optional):  A flat JSON document containing key-value pairs with additional information (nested objects are not supported). You can filter by metadata when searching or deleting records.

    <Note>
      When importing data from object storage, records must be in Parquet format. For more details, see [Import data](/guides/index-data/import-data#prepare-your-data).
    </Note>

    Example:

    <CodeGroup>
      ```json Dense theme={null}
      {
        "id": "document1#chunk1", 
        "values": [0.0236663818359375, -0.032989501953125, ..., -0.01041412353515625, 0.0086669921875], 
        "metadata": {
          "document_id": "document1",
          "document_title": "Introduction to Vector Databases",
          "chunk_number": 1,
          "chunk_text": "First chunk of the document content...",
          "document_url": "https://example.com/docs/document1",
          "created_at": "2024-01-15",
          "document_type": "tutorial"
        }
      }
      ```

      ```json Sparse theme={null}
      {
        "id": "document1#chunk1", 
        "sparse_values": {
          "values": [1.7958984, 0.41577148, ..., 4.4414062, 3.3554688],
          "indices": [822745112, 1009084850, ..., 3517203014, 3590924191]
        },
        "metadata": {
          "document_id": "document1",
          "document_title": "Introduction to Vector Databases",
          "chunk_number": 1,
          "chunk_text": "First chunk of the document content...",
          "document_url": "https://example.com/docs/document1",
          "created_at": "2024-01-15",
          "document_type": "tutorial"
        }
      }
      ```

      ```json Hybrid theme={null}
      {
        "id": "document1#chunk1", 
        "values": [0.0236663818359375, -0.032989501953125, ..., -0.01041412353515625, 0.0086669921875], 
        "sparse_values": {
          "values": [1.7958984, 0.41577148, ..., 4.4414062, 3.3554688],
          "indices": [822745112, 1009084850, ..., 3517203014, 3590924191]
        },
        "metadata": {
          "document_id": "document1",
          "document_title": "Introduction to Vector Databases",
          "chunk_number": 1,
          "chunk_text": "First chunk of the document content...",
          "document_url": "https://example.com/docs/document1",
          "created_at": "2024-01-15",
          "document_type": "tutorial"
        }
      }
      ```
    </CodeGroup>
  </Tab>
</Tabs>


## Use structured IDs

Use a structured, human-readable format for record IDs, including ID prefixes that reflect the type of data you're storing, for example:

* **Document chunks**: `document_id#chunk_number`
* **User data**: `user_id#data_type#item_id`
* **Multi-tenant data**: `tenant_id#document_id#chunk_id`

Choose a delimiter for your ID prefixes that won't appear elsewhere in your IDs. Common patterns include:

* `document1#chunk1` - Using hash delimiter
* `document1_chunk1` - Using underscore delimiter
* `document1:chunk1` - Using colon delimiter

Structuring IDs in this way provides several advantages:

* **Efficiency**: Applications can quickly identify which record it should operate on.
* **Clarity**: Developers can easily understand what they're looking at when examining records.
* **Flexibility**: ID prefixes enable list operations for fetching and updating records.


## Include metadata

Include [metadata key-value pairs](/guides/index-data/indexing-overview#metadata) that support your application's key operations, for example:

* **Enable query-time filtering**: Add fields for time ranges, categories, or other criteria for [filtering searches for increased accuracy and relevance](/guides/search/filter-by-metadata).
* **Link related chunks**: Use fields like `document_id` and `chunk_number` to keep track of related records and enable efficient [chunk deletion](#delete-chunks) and [document updates](#update-an-entire-document).
* **Link back to original data**: Include `chunk_text` or `document_url` for traceability and user display.

Metadata keys must be strings, and metadata values must be one of the following data types:

* String
* Number (integer or floating point, gets converted to a 64-bit floating point)
* Boolean (true, false)
* List of strings

<Note>
  Pinecone supports 40 KB of metadata per record.
</Note>


## Example

This example demonstrates how to manage document chunks in Pinecone using structured IDs and comprehensive metadata. It covers the complete lifecycle of chunked documents: upserting, searching, fetching, updating, and deleting chunks, and updating an entire document.

### Upsert chunks

When [upserting](/guides/index-data/upsert-data) documents that have been split into chunks, combine structured IDs with comprehensive metadata:

<Tabs>
  <Tab title="Upsert text">
    <Note>
      Upserting raw text is supported only for [indexes with integrated embedding](/guides/index-data/create-an-index#integrated-embedding).
    </Note>

    ```python Python theme={null}
    from pinecone.grpc import PineconeGRPC as Pinecone

    pc = Pinecone(api_key="YOUR_API_KEY")

    # To get the unique host for an index, 
    # see https://docs.pinecone.io/guides/manage-data/target-an-index
    index = pc.Index(host="INDEX_HOST")

    index.upsert_records(
      "example-namespace",
      [
        {
          "_id": "document1#chunk1", 
          "chunk_text": "First chunk of the document content...",
          "document_id": "document1",
          "document_title": "Introduction to Vector Databases",
          "chunk_number": 1,
          "document_url": "https://example.com/docs/document1",
          "created_at": "2024-01-15",
          "document_type": "tutorial"
        },
        {
          "_id": "document1#chunk2", 
          "chunk_text": "Second chunk of the document content...",
          "document_id": "document1",
          "document_title": "Introduction to Vector Databases", 
          "chunk_number": 2,
          "document_url": "https://example.com/docs/document1",
          "created_at": "2024-01-15",
          "document_type": "tutorial"
        },
        {
          "_id": "document1#chunk3", 
          "chunk_text": "Third chunk of the document content...",
          "document_id": "document1",
          "document_title": "Introduction to Vector Databases",
          "chunk_number": 3, 
          "document_url": "https://example.com/docs/document1",
          "created_at": "2024-01-15",
          "document_type": "tutorial"
        },
      ]
    )
    ```
  </Tab>

  <Tab title="Upsert vectors">
    ```python Python theme={null}
    from pinecone.grpc import PineconeGRPC as Pinecone

    pc = Pinecone(api_key="YOUR_API_KEY")

    # To get the unique host for an index, 
    # see https://docs.pinecone.io/guides/manage-data/target-an-index
    index = pc.Index(host="INDEX_HOST")

    index.upsert(
      namespace="example-namespace",
      vectors=[
        {
          "id": "document1#chunk1", 
          "values": [0.0236663818359375, -0.032989501953125, ..., -0.01041412353515625, 0.0086669921875], 
          "metadata": {
            "document_id": "document1",
            "document_title": "Introduction to Vector Databases",
            "chunk_number": 1,
            "chunk_text": "First chunk of the document content...",
            "document_url": "https://example.com/docs/document1",
            "created_at": "2024-01-15",
            "document_type": "tutorial"
          }
        },
        {
          "id": "document1#chunk2", 
          "values": [-0.0412445068359375, 0.028839111328125, ..., 0.01953125, -0.0174560546875],
          "metadata": {
            "document_id": "document1",
            "document_title": "Introduction to Vector Databases", 
            "chunk_number": 2,
            "chunk_text": "Second chunk of the document content...",
            "document_url": "https://example.com/docs/document1",
            "created_at": "2024-01-15",
            "document_type": "tutorial"
          }
        },
        {
          "id": "document1#chunk3", 
          "values": [0.0512237548828125, 0.041656494140625, ..., 0.02130126953125, -0.0394287109375],
          "metadata": {
            "document_id": "document1",
            "document_title": "Introduction to Vector Databases",
            "chunk_number": 3, 
            "chunk_text": "Third chunk of the document content...",
            "document_url": "https://example.com/docs/document1",
            "created_at": "2024-01-15",
            "document_type": "tutorial"
          }
        }
      ]
    )
    ```
  </Tab>
</Tabs>

### Search chunks

To search the chunks of a document, use a [metadata filter expression](/guides/search/filter-by-metadata#metadata-filter-expressions) that limits the search appropriately:

<Tabs>
  <Tab title="Search with text">
    <Note>
      Searching with text is supported only for [indexes with integrated embedding](/guides/index-data/create-an-index#integrated-embedding).
    </Note>

    ```python Python theme={null}
    from pinecone import Pinecone

    pc = Pinecone(api_key="YOUR_API_KEY")

    # To get the unique host for an index, 
    # see https://docs.pinecone.io/guides/manage-data/target-an-index
    index = pc.Index(host="INDEX_HOST")

    filtered_results = index.search(
        namespace="example-namespace", 
        query={
            "inputs": {"text": "What is a vector database?"}, 
            "top_k": 3,
            "filter": {"document_id": "document1"}
        },
        fields=["chunk_text"]
    )

    print(filtered_results)
    ```
  </Tab>

  <Tab title="Search with a vector">
    ```python Python theme={null}
    from pinecone.grpc import PineconeGRPC as Pinecone

    pc = Pinecone(api_key="YOUR_API_KEY")

    # To get the unique host for an index, 
    # see https://docs.pinecone.io/guides/manage-data/target-an-index
    index = pc.Index(host="INDEX_HOST")

    filtered_results = index.query(
        namespace="example-namespace",
        vector=[0.0236663818359375,-0.032989501953125, ..., -0.01041412353515625,0.0086669921875], 
        top_k=3,
        filter={
            "document_id": {"$eq": "document1"}
        },
        include_metadata=True,
        include_values=False
    )

    print(filtered_results)
    ```
  </Tab>
</Tabs>

### Fetch chunks

To retrieve all chunks for a specific document, first [list the record IDs](/guides/manage-data/list-record-ids) using the document prefix, and then [fetch](/guides/manage-data/fetch-data) the complete records:

```python Python theme={null}
from pinecone.grpc import PineconeGRPC as Pinecone

pc = Pinecone(api_key="YOUR_API_KEY")


# To get the unique host for an index, 

# see https://docs.pinecone.io/guides/manage-data/target-an-index
index = pc.Index(host="INDEX_HOST")


# List all chunks for document1 using ID prefix
chunk_ids = []
for record_id in index.list(prefix='document1#', namespace='example-namespace'):
    chunk_ids.append(record_id)

print(f"Found {len(chunk_ids)} chunks for document1")


# Fetch the complete records by ID
if chunk_ids:
    records = index.fetch(ids=chunk_ids, namespace='example-namespace')
    
    for record_id, record_data in records['vectors'].items():
        print(f"Chunk ID: {record_id}")
        print(f"Chunk text: {record_data['metadata']['chunk_text']}")
        # Process the vector values and metadata as needed
```

<Note>
  Pinecone is [eventually consistent](/guides/index-data/check-data-freshness), so it's possible that a write (upsert, update, or delete) followed immediately by a read (query, list, or fetch) may not return the latest version of the data. If your use case requires retrieving data immediately, consider implementing a small delay or [retry logic](/guides/production/error-handling#implement-retry-logic) after writes.
</Note>

### Update chunks

To [update](/guides/manage-data/update-data) specific chunks within a document, first list the chunk IDs, and then update individual records:

```python Python theme={null}
from pinecone.grpc import PineconeGRPC as Pinecone

pc = Pinecone(api_key="YOUR_API_KEY")


# To get the unique host for an index, 

# see https://docs.pinecone.io/guides/manage-data/target-an-index
index = pc.Index(host="INDEX_HOST")


# List all chunks for document1
chunk_ids = []
for record_id in index.list(prefix='document1#', namespace='example-namespace'):
    chunk_ids.append(record_id)


# Update specific chunks (e.g., update chunk 2)
if 'document1#chunk2' in chunk_ids:
    index.update(
        id='document1#chunk2',
        values=[<new dense vector>],
        set_metadata={
            "document_id": "document1",
            "document_title": "Introduction to Vector Databases - Revised",
            "chunk_number": 2,
            "chunk_text": "Updated second chunk content...",
            "document_url": "https://example.com/docs/document1",
            "created_at": "2024-01-15",
            "updated_at": "2024-02-15",
            "document_type": "tutorial"
        },
        namespace='example-namespace'
    )
    print("Updated chunk 2 successfully")
```

### Delete chunks

To [delete](/guides/manage-data/delete-data#delete-records-by-metadata) chunks of a document, use a [metadata filter expression](/guides/search/filter-by-metadata#metadata-filter-expressions) that limits the deletion appropriately:

```python Python theme={null}
from pinecone.grpc import PineconeGRPC as Pinecone

pc = Pinecone(api_key="YOUR_API_KEY")


# To get the unique host for an index, 

# see https://docs.pinecone.io/guides/manage-data/target-an-index
index = pc.Index(host="INDEX_HOST")


# Delete chunks 1 and 3
index.delete(
    namespace="example-namespace",
    filter={
        "document_id": {"$eq": "document1"},
        "chunk_number": {"$in": [1, 3]}
    }
)


---
**Navigation:** [← Previous](./01-concepts.md) | [Index](./index.md) | [Next →](./03-delete-all-chunks-for-a-document.md)
