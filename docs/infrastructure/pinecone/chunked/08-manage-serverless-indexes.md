**Navigation:** [← Previous](./07-back-up-an-index.md) | [Index](./index.md) | [Next →](./09-target-an-index.md)

# Manage serverless indexes
Source: https://docs.pinecone.io/guides/manage-data/manage-indexes

List, describe, and configure serverless indexes.

This page shows you how to manage your existing serverless indexes.


## List indexes

Use the [`list_indexes`](/reference/api/latest/control-plane/list_indexes) operation to get a complete description of all indexes in a project:

<CodeGroup>
  ```Python Python theme={null}
  from pinecone.grpc import PineconeGRPC as Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  index_list = pc.list_indexes()

  print(index_list)
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' })

  const indexList = await pc.listIndexes();

  console.log(indexList);
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Pinecone;
  import org.openapitools.db_control.client.model.*;

  public class ListIndexesExample {
      public static void main(String[] args) {
          Pinecone pc = new Pinecone.Builder("YOUR_API_KEY").build();
          IndexList indexList = pc.listIndexes();
          System.out.println(indexList);
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

      idxs, err := pc.ListIndexes(ctx)
      if err != nil {
          log.Fatalf("Failed to list indexes: %v", err)
      } else {
          for _, index := range idxs {
              fmt.Printf("index: %v\n", prettifyStruct(index))
          }
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

  curl -i -X GET "https://api.pinecone.io/indexes" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "X-Pinecone-API-Version: 2025-04"
  ```
</CodeGroup>

The response will look like this:

<CodeGroup>
  ```python Python theme={null}
  [{
      "name": "docs-example-sparse",
      "metric": "dotproduct",
      "host": "docs-example-sparse-govk0nt.svc.aped-4627-b74a.pinecone.io",
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
      "vector_type": "sparse",
      "dimension": null,
      "deletion_protection": "disabled",
      "tags": {
          "environment": "development"
      }
  }, {
      "name": "docs-example-dense",
      "metric": "cosine",
      "host": "docs-example-dense-govk0nt.svc.aped-4627-b74a.pinecone.io",
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
      "dimension": 1536,
      "deletion_protection": "disabled",
      "tags": {
          "environment": "development"
      }
  }]
  ```

  ```javascript JavaScript theme={null}
  {
    indexes: [
      {
        name: 'docs-example-sparse',
        dimension: undefined,
        metric: 'dotproduct',
        host: 'docs-example-sparse-govk0nt.svc.aped-4627-b74a.pinecone.io',
        deletionProtection: 'disabled',
        tags: { environment: 'development', example: 'tag' },
        embed: undefined,
        spec: { pod: undefined, serverless: { cloud: 'aws', region: 'us-east-1' } },
        status: { ready: true, state: 'Ready' },
        vectorType: 'sparse'
      },
      {
        name: 'docs-example-dense',
        dimension: 1536,
        metric: 'cosine',
        host: 'docs-example-dense-govk0nt.svc.aped-4627-b74a.pinecone.io',
        deletionProtection: 'disabled',
        tags: { environment: 'development', example: 'tag' },
        embed: undefined,
        spec: { pod: undefined, serverless: { cloud: 'aws', region: 'us-east-1' } },
        status: { ready: true, state: 'Ready' },
        vectorType: 'dense'
      }
    ]
  }
  ```

  ```java Java theme={null}
  class IndexList {
      indexes: [class IndexModel {
          name: docs-example-sparse
          dimension: null
          metric: dotproduct
          host: docs-example-sparse-govk0nt.svc.aped-4627-b74a.pinecone.io
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
          vectorType: sparse
          additionalProperties: null
      }, class IndexModel {
          name: docs-example-dense
          dimension: 1536
          metric: cosine
          host: docs-example-dense-govk0nt.svc.aped-4627-b74a.pinecone.io
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
      }]
      additionalProperties: null
  }
  ```

  ```go Go theme={null}
  index: {
    "name": "docs-example-sparse",
    "host": "docs-example-sparse-govk0nt.svc.aped-4627-b74a.pinecone.io",
    "metric": "dotproduct",
    "vector_type": "sparse",
    "deletion_protection": "disabled",
    "dimension": null,
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
  index: {
    "name": "docs-example-dense",
    "host": "docs-example-dense-govk0nt.svc.aped-4627-b74a.pinecone.io",
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
    "indexes": [
      {
        "name": "docs-example-sparse",
        "metric": "dotproduct",
        "host": "docs-example-sparse-govk0nt.svc.aped-4627-b74a.pinecone.io",
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
        "vector_type": "sparse"
      },
      {
        "name": "docs-example-dense",
        "dimension": 1536,
        "metric": "cosine",
        "host": "docs-example-dense-govk0nt.svc.aped-4627-b74a.pinecone.io",
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
    ]
  }
  ```

  ```json curl theme={null}
  {
    "indexes": [
      {
        "name": "docs-example-sparse",
        "vector_type": "sparse",
        "metric": "dotproduct",
        "dimension": null,
        "status": {
          "ready": true,
          "state": "Ready"
        },
        "host": "docs-example-sparse-govk0nt.svc.aped-4627-b74a.pinecone.io",
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
      },
      {
        "name": "docs-example-dense",
        "vector_type": "dense",
        "metric": "cosine",
        "dimension": 1536,
        "status": {
          "ready": true,
          "state": "Ready"
        },
        "host": "docs-example-dense-govk0nt.svc.aped-4627-b74a.pinecone.io",
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
    ]
  }
  ```
</CodeGroup>

With the Python SDK, you can use the `.names()` helper function to iterate over the index names in the `list_indexes()` response, for example:

```Python Python theme={null}
from pinecone.grpc import PineconeGRPC as Pinecone
from pinecone import ServerlessSpec

for index_name in pc.list_indexes().names:
    print(index_name)
```


## Describe an index

Use the [`describe_index`](/reference/api/latest/control-plane/describe_index/) endpoint to get a complete description of a specific index:

<CodeGroup>
  ```Python Python theme={null}
  from pinecone.grpc import PineconeGRPC as Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  pc.describe_index(name="docs-example")
  ```

  ```JavaScript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  await pc.describeIndex('docs-example');
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Pinecone;
  import org.openapitools.db_control.client.model.*;

  public class DescribeIndexExample {
      public static void main(String[] args) {
          Pinecone pc = new Pinecone.Builder("YOURE_API_KEY").build();
          IndexModel indexModel = pc.describeIndex("docs-example");
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

      idx, err := pc.DescribeIndex(ctx, "docs-example")
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

  var indexModel = await pinecone.DescribeIndexAsync("docs-example");

  Console.WriteLine(indexModel);
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl -i -X GET "https://api.pinecone.io/indexes/docs-example" \
      -H "Api-Key: $PINECONE_API_KEY" \
      -H "X-Pinecone-API-Version: 2025-04"
  ```
</CodeGroup>

The response will look like this:

<CodeGroup>
  ```Python Python theme={null}
  {'deletion_protection': 'disabled',
   'dimension': 1536,
   'host': 'docs-example-dense-govk0nt.svc.aped-4627-b74a.pinecone.io',
   'metric': 'cosine',
   'name': 'docs-example-dense',
   'spec': {'serverless': {'cloud': 'aws', 'region': 'us-east-1'}},
   'status': {'ready': True, 'state': 'Ready'},
   'tags': {'environment': 'development'},
   'vector_type': 'dense'}
  ```

  ```javaScript JavaScript theme={null}
  {
    name: 'docs-example-dense',
    dimension: 1536,
    metric: 'cosine',
    host: 'docs-example-dense-govk0nt.svc.aped-4627-b74a.pinecone.io',
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
      name: docs-example-dense
      dimension: 1536
      metric: cosine
      host: docs-example-dense-govk0nt.svc.aped-4627-b74a.pinecone.io
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
    "name": "docs-example-dense",
    "host": "docs-example-dense-govk0nt.svc.aped-4627-b74a.pinecone.io",
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
    "name": "docs-example-dense",
    "dimension": 1536,
    "metric": "cosine",
    "host": "docs-example-dense-govk0nt.svc.aped-4627-b74a.pinecone.io",
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
    "name": "docs-example-dense",
    "vector_type": "dense",
    "metric": "cosine",
    "dimension": 1536,
    "status": {
      "ready": true,
      "state": "Ready"
    },
    "host": "docs-example-dense-govk0nt.svc.aped-4627-b74a.pinecone.io",
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
</CodeGroup>

<Warning>
  **Do not target an index by name in production.**

  When you target an index by name for data operations such as `upsert` and `query`, the SDK gets the unique DNS host for the index using the `describe_index` operation. This is convenient for testing but should be avoided in production because `describe_index` uses a different API than data operations and therefore adds an additional network call and point of failure. Instead, you should get an index host once and cache it for reuse or specify the host directly.
</Warning>


## Delete an index

Use the [`delete_index`](reference/api/latest/control-plane/delete_index) operation to delete an index and all of its associated resources.

<CodeGroup>
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

  curl -i -X DELETE "https://api.pinecone.io/indexes/docs-example" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-API-Version: 2025-04"
  ```
</CodeGroup>

If deletion protection is enabled on an index, requests to delete it will fail and return a `403 - FORBIDDEN` status with the following error:

```
Deletion protection is enabled for this index. Disable deletion protection before retrying.
```

Before you can delete such an index, you must first [disable deletion protection](/guides/manage-data/manage-indexes#configure-deletion-protection).

<Tip>
  You can delete an index using the [Pinecone console](https://app.pinecone.io/organizations/-/projects/-/indexes). For the index you want to delete, click the three dots to the right of the index name, then click **Delete**.
</Tip>


## Associate an embedding model

[Integrated inference](/guides/index-data/indexing-overview#integrated-embedding) lets you upsert and search without extra steps for embedding data and reranking results.

To configure an existing serverless index for an embedding model, use the [`configure_index`](/reference/api/latest/control-plane/configure_index) operation as follows:

* Set `embed.model` to one of [Pinecone's hosted embedding models](/guides/index-data/create-an-index#embedding-models).
* Set `embed.field_map` to the name of the field in your source document that contains the data for embedding.

<Warning>
  The `vector_type`, `metric`, and `dimension` of the index must be supported by the specified embedding model.
</Warning>

<CodeGroup>
  ```python Python theme={null}
  # pip install --upgrade pinecone
  from pinecone import Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  pc.configure_index(
      name="docs-example",
      embed={
        "model":"llama-text-embed-v2",
        "field_map":{"text": "chunk_text"}
      }
  )
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  await pc.configureIndex('docs-example', {
    embed: {
      model: 'llama-text-embed-v2',
      fieldMap: { text: 'chunk_text' },
    },
  });
  ```

  ```json curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl -s -X PATCH "https://api.pinecone.io/indexes/docs-example" \
      -H "Content-Type: application/json" \
      -H "Api-Key: $PINECONE_API_KEY" \
      -H "X-Pinecone-API-Version: 2025-04" \
      -d '{
        "embed": {
            "model": "llama-text-embed-v2",
            "field_map": {
                "text": "chunk_text"
            }
        }
    }'
  ```
</CodeGroup>


## Configure deletion protection

<Note>
  This feature requires [Pinecone API version](/reference/api/versioning) `2024-07`, [Python SDK](/reference/python-sdk) v5.0.0, [Node.js SDK](/reference/node-sdk) v3.0.0, [Java SDK](/reference/java-sdk) v2.0.0, or [Go SDK](/reference/go-sdk) v1.0.0 or later.
</Note>

### Enable deletion protection

You can prevent an index and its data from accidental deleting when [creating a new index](/guides/index-data/create-an-index) or after its been created. In both cases, you set the `deletion_protection` parameter to `enabled`.

<Warning>
  Enabling deletion protection does *not* prevent [namespace deletions](/guides/manage-data/manage-namespaces#delete-a-namespace).
</Warning>

To enable deletion protection when creating a new index:

<CodeGroup>
  ```python Python theme={null}
  # pip install "pinecone[grpc]"
  # Serverless index
  from pinecone.grpc import PineconeGRPC as Pinecone
  from pinecone import ServerlessSpec

  pc = Pinecone(api_key="YOUR_API_KEY")

  pc.create_index(
    name="docs-example",
    dimension=1536,
    metric="cosine",
    spec=ServerlessSpec(
      cloud="aws",
      region="us-east-1"
    ),
    deletion_protection="enabled"
  )
  ```

  ```javascript JavaScript theme={null}
  // npm install @pinecone-database/pinecone
  // Serverles index
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({
    apiKey: 'YOUR_API_KEY'
  });

  await pc.createIndex({
    name: 'docs-example',
    dimension: 1536,
    metric: 'cosine',
    spec: {
      serverless: {
        cloud: 'aws',
        region: 'us-east-1'
      }
    },
    deletionProtection: 'enabled',
  });
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Pinecone;
  import org.openapitools.db_control.client.model.IndexModel;
  import org.openapitools.db_control.client.model.DeletionProtection;

  // Serverless index
  public class CreateServerlessIndexExample {
      public static void main(String[] args) {
          Pinecone pc = new Pinecone.Builder("YOUR_API_KEY").build();
          pc.createServerlessIndex("docs-example", "cosine", 1536, "aws", "us-east-1", DeletionProtection.enabled);
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
    	indexName := "docs-example"
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

  // Serverless index
  var createIndexRequest = await pinecone.CreateIndexAsync(new CreateIndexRequest
  {
      Name = "docs-example",
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
      DeletionProtection = DeletionProtection.Enabled
  });
  ```

  ```shell curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  # Serverless index
  curl -s "https://api.pinecone.io/indexes" \
    -H "Accept: application/json" \
    -H "Content-Type: application/json" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-API-Version: 2025-04" \
    -d '{
           "name": "docs-example",
           "dimension": 1536,
           "metric": "cosine",
           "spec": {
              "serverless": {
                 "cloud": "aws",
                 "region": "us-east-1"
              }
           },
           "deletion_protection": "enabled"
        }'
  ```
</CodeGroup>

To enable deletion protection when configuring an existing index:

<CodeGroup>
  ```python Python theme={null}
  from pinecone.grpc import PineconeGRPC as Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  pc.configure_index(
     name="docs-example", 
     deletion_protection="enabled"
  )
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const client = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  await client.configureIndex('docs-example', { deletionProtection: 'enabled' });
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Pinecone;
  import org.openapitools.db_control.client.model.*;

  public class ConfigureIndexExample {
      public static void main(String[] args) {
          Pinecone pc = new Pinecone.Builder("YOUR_API_KEY").build();
          pc.configureServerlessIndex("docs-example", DeletionProtection.ENABLED);
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

      idx, err := pc.ConfigureIndex(ctx, "docs-example", pinecone.ConfigureIndexParams{DeletionProtection: "enabled"})
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

  var indexMetadata = await pinecone.ConfigureIndexAsync("docs-example", new ConfigureIndexRequest
  {
      DeletionProtection = DeletionProtection.Enabled,
  });
  ```

  ```shell curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl -s -X PATCH "https://api.pinecone.io/indexes/docs-example-curl" \
      -H "Content-Type: application/json" \
      -H "Api-Key: $PINECONE_API_KEY" \
      -H "X-Pinecone-API-Version: 2025-04" \
      -d '{
          "deletion_protection": "enabled"
          }'
  ```
</CodeGroup>

When deletion protection is enabled on an index, requests to delete the index fail and return a `403 - FORBIDDEN` status with the following error:

```
Deletion protection is enabled for this index. Disable deletion protection before retrying.
```

### Disable deletion protection

Before you can [delete an index](#delete-an-index) with deletion protection enabled, you must first disable deletion protection as follows:

<CodeGroup>
  ```python Python theme={null}
  from pinecone.grpc import PineconeGRPC as Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  pc.configure_index(
     name="docs-example", 
     deletion_protection="disabled"
  )
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const client = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  await client.configureIndex('docs-example', { deletionProtection: 'disabled' });
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Pinecone;
  import org.openapitools.db_control.client.model.*;

  public class ConfigureIndexExample {
      public static void main(String[] args) {
          Pinecone pc = new Pinecone.Builder("YOUR_API_KEY").build();
          pc.configureServerlessIndex("docs-example", DeletionProtection.DISABLED);
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

      idx, err := pc.ConfigureIndex(ctx, "docs-example", pinecone.ConfigureIndexParams{DeletionProtection: "disabled"})
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

  var configureIndexRequest = await pinecone.ConfigureIndexAsync("docs-example", new ConfigureIndexRequest
  {
      DeletionProtection = DeletionProtection.Disabled,
  });
  ```

  ```shell curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl -s -X PATCH "https://api.pinecone.io/indexes/docs-example-curl" \
      -H "Content-Type: application/json" \
      -H "Api-Key: $PINECONE_API_KEY" \
      -H "X-Pinecone-API-Version: 2025-04" \
      -d '{
          "deletion_protection": "disabled"
          }'
  ```
</CodeGroup>


## Configure index tags

Tags are key-value pairs that you can use to categorize and identify the index.

### Add tags

To add tags to an index, use the `tags` parameter when [creating a new index](/guides/index-data/create-an-index) or configuring an existing index.

To add tags when creating a new index:

<CodeGroup>
  ```python Python theme={null}
  from pinecone.grpc import PineconeGRPC as Pinecone
  from pinecone import ServerlessSpec

  pc = Pinecone(api_key="YOUR_API_KEY")

  pc.create_index(
      name="docs-example",
      dimension=1536,
      metric="cosine",
      spec=ServerlessSpec(
          cloud="aws",
          region="us-east-1"
      ),
      deletion_protection="disabled",
      tags={
          "example": "tag", 
          "environment": "development"
      }
  )
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone'

  const client = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  await pc.createIndex({
    name: 'docs-example',
    dimension: 1536,
    metric: 'cosine',
    spec: {
      serverless: {
        cloud: 'aws',
        region: 'us-east-1'
      }
    },
    deletionProtection: 'disabled',
    tags: { example: 'tag', environment: 'development' }, 
  });
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Pinecone;
  import org.openapitools.db_control.client.model.IndexModel;
  import org.openapitools.db_control.client.model.DeletionProtection;
  import java.util.HashMap;

  // Serverless index
  public class CreateServerlessIndexExample {
      public static void main(String[] args) {
          Pinecone pc = new Pinecone.Builder("YOUR_API_KEY").build();
          HashMap<String, String> tags = new HashMap<>();
          tags.put("tag", "development");
          pc.createServerlessIndex("docs-example", "cosine", 1536, "aws", "us-east-1", DeletionProtection.DISABLED, tags);
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
      idx, err := pc.CreateServerlessIndex(ctx, &pinecone.CreateServerlessIndexRequest{
          Name:               "docs-example",
          Dimension:          1536,
          Metric:             pinecone.Cosine,
          Cloud:              pinecone.Aws,
          Region:             "us-east-1",
          DeletionProtection: "disabled",
          Tags:               &pinecone.IndexTags{ "example": "tag", "environment": "development" },
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
      Name = "docs-example",
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
          { "example", "tag" }, 
          { "environment", "development" }
      }
  });
  ```

  ```shell curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  # Serverless index
  curl -s "https://api.pinecone.io/indexes" \
    -H "Accept: application/json" \
    -H "Content-Type: application/json" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-API-Version: 2025-04" \
    -d '{
           "name": "docs-example",
           "dimension": 1536,
           "metric": "cosine",
           "spec": {
              "serverless": {
                 "cloud": "aws",
                 "region": "us-east-1"
              }
           },
          "tags": {
              "example": "tag",
              "environment": "development"
          },
           "deletion_protection": "disabled"
        }'
  ```
</CodeGroup>

<Tip>
  You can add tags during index creation using the [Pinecone console](https://app.pinecone.io/organizations/-/projects/-/create-index/).
</Tip>

To add or update tags when configuring an existing index:

<CodeGroup>
  ```python Python theme={null}
  from pinecone.grpc import PineconeGRPC as Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  pc.configure_index(
      name="docs-example", 
      tags={
          example: "tag", 
          environment: "development" 
      }
  )
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const client = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  await client.configureIndex('docs-example', { tags: { example: 'tag', environment: 'development' }});
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Pinecone;
  import org.openapitools.db_control.client.model.*;
  import java.util.HashMap;

  public class ConfigureIndexExample {
      public static void main(String[] args) {
          Pinecone pc = new Pinecone.Builder("YOUR_API_KEY").build();
          HashMap<String, String> tags = new HashMap<>();
          tags.put("tag", "development");

          pc.configureServerlessIndex("docs-example", DeletionProtection.ENABLED, tags);
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

      idx, err := pc.ConfigureIndex(ctx, 
          "docs-example", 
          pinecone.ConfigureIndexParams{
              Tags: pinecone.IndexTags{
  			    "example": "tag",
                  "environment": "development",
              },
          },
      )    
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

  var configureIndexRequest = await pinecone.ConfigureIndexAsync("docs-example", new ConfigureIndexRequest
  {
      Tags = new Dictionary<string, string> 
      { 
          { "example", "tag" }, 
          { "environment", "development" }
      }
  });
  ```

  ```shell curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl -s -X PATCH "https://api.pinecone.io/indexes/docs-example-curl" \
      -H "Content-Type: application/json" \
      -H "Api-Key: $PINECONE_API_KEY" \
      -H "X-Pinecone-API-Version: 2025-04" \
      -d '{
              "tags": {
                  "example": "tag",
                  "environment": "development"
              }
          }'
  ```
</CodeGroup>

<Tip>
  You can add or update tags when configuring an existing index using the [Pinecone console](https://app.pinecone.io/organizations/-/projects/-/indexes). Find the index to edit and click the **ellipsis (...) menu > Add tags**.
</Tip>

### View tags

To view the tags of an index, [list all indexes](/guides/manage-data/manage-indexes) in a project or [get information about a specific index](/guides/manage-data/manage-indexes).

### Remove tags

To remove a tag from an index, [configure the index](/reference/api/latest/control-plane/configure_index) and use the `tags` parameter to send the tag key with an empty value (`""`).

The following example removes the `example: tag` tag from `docs-example`:

<CodeGroup>
  ```python Python theme={null}
  from pinecone.grpc import PineconeGRPC as Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  pc.configure_index(
      name="docs-example", 
      tags={"example": ""}
  )
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const client = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  await client.configureIndex('docs-example', { tags: { example: '' }});
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Pinecone;
  import org.openapitools.db_control.client.model.*;
  import java.util.HashMap;

  public class ConfigureIndexExample {
      public static void main(String[] args) {
          Pinecone pc = new Pinecone.Builder("YOUR_API_KEY").build();
          HashMap<String, String> tags = new HashMap<>();
          tags.put("example", "");

          pc.configureServerlessIndex("docs-example", DeletionProtection.ENABLED, tags);
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

      idx, err := pc.ConfigureIndex(ctx, 
          "docs-example", 
          pinecone.ConfigureIndexParams{
              Tags: pinecone.IndexTags{
  			    "example": "",
              },
          },
      )    
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

  var configureIndexRequest = await pinecone.ConfigureIndexAsync("docs-example", new ConfigureIndexRequest
  {
      Tags = new Dictionary<string, string> 
      { 
          { "example", "" } 
      }
  });
  ```

  ```shell curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl -s -X PATCH "https://api.pinecone.io/indexes/docs-example-curl" \
      -H "Content-Type: application/json" \
      -H "Api-Key: $PINECONE_API_KEY" \
      -H "X-Pinecone-API-Version: 2025-04" \
      -d '{
              "tags": {
                  "example": ""
              }
          }'
  ```
</CodeGroup>

<Tip>
  You can remove tags from an index using the [Pinecone console](https://app.pinecone.io/organizations/-/projects/-/indexes). Find the index to edit and click the **ellipsis (...) menu > \_\_ tags**.
</Tip>


## List backups for an index

Serverless indexes can be [backed up](/guides/manage-data/back-up-an-index). You can [list all backups for a specific index](/reference/api/latest/control-plane/list_index_backups), as in the following example:

<CodeGroup>
  ```python Python theme={null}
  from pinecone import Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  index_backups = pc.list_backups(index_name="docs-example")

  print(index_backups)
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' })

  const indexBackups = await pc.listBackups({ indexName: 'docs-example' });

  console.log(indexBackups);
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Pinecone;
  import org.openapitools.db_control.client.ApiException;
  import org.openapitools.db_control.client.model.*;

  public class CreateBackup {
      public static void main(String[] args) throws ApiException {
          Pinecone pc = new Pinecone.Builder("YOUR_API_KEY").build();

          String indexName = "docs-example";
          BackupList indexBackupList = pc.listIndexBackups(indexName);

          System.out.println(indexBackupList);
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

  	indexName := "docs-example"
  	limit := 2
  	indexBackups, err := pc.ListBackups(ctx, &pinecone.ListBackupsParams{
  		Limit: &limit,
  		IndexName: &indexName,
  	})
  	if err != nil {
  		log.Fatalf("Failed to list backups: %v", err)
  	}
  	fmt.Printf(prettifyStruct(indexBackups))
  }
  ```

  ```csharp C# theme={null}
  using Pinecone;

  var pinecone = new PineconeClient("YOUR_API_KEY");

  var indexBackups = await pinecone.Backups.ListByIndexAsync( "docs-example", new ListBackupsByIndexRequest());

  Console.WriteLine(indexBackups);
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_NAME="docs-example"

  curl -X GET "https://api.pinecone.io/indexes/$INDEX_NAME/backups" \
      -H "Api-Key: $PINECONE_API_KEY" \
      -H "X-Pinecone-API-Version: 2025-04" \
      -H "accept: application/json"
  ```
</CodeGroup>

The example returns a response like the following:

<CodeGroup>
  ```python Python theme={null}
  [{
      "backup_id": "8c85e612-ed1c-4f97-9f8c-8194e07bcf71",
      "source_index_name": "docs-example",
      "source_index_id": "f73b36c9-faf5-4a2c-b1d6-4013d8b1cc74",
      "status": "Ready",
      "cloud": "aws",
      "region": "us-east-1",
      "tags": {},
      "name": "example-backup",
      "description": "Monthly backup of production index",
      "dimension": 1024,
      "record_count": 98,
      "namespace_count": 3,
      "size_bytes": 1069169,
      "created_at": "2025-05-15T00:52:10.809305882Z"
  }]
  ```

  ```javascript JavaScript theme={null}
  {
    data: [
      {
        backupId: '8c85e612-ed1c-4f97-9f8c-8194e07bcf71',
        sourceIndexName: 'docs-example',
        sourceIndexId: 'f73b36c9-faf5-4a2c-b1d6-4013d8b1cc74',
        name: 'example-backup',
        description: 'Monthly backup of production index',
        status: 'Ready',
        cloud: 'aws',
        region: 'us-east-1',
        dimension: 1024,
        metric: undefined,
        recordCount: 98,
        namespaceCount: 3,
        sizeBytes: 1069169,
        tags: {},
        createdAt: '2025-05-14T16:37:25.625540Z'
      }
    ],
    pagination: undefined
  }
  ```

  ```java Java theme={null}
  class BackupList {
      data: [class BackupModel {
          backupId: 8c85e612-ed1c-4f97-9f8c-8194e07bcf71
          sourceIndexName: docs-example
          sourceIndexId: f73b36c9-faf5-4a2c-b1d6-4013d8b1cc74
          name: example-backup
          description: Monthly backup of production index
          status: Initializing
          cloud: aws
          region: us-east-1
          dimension: null
          metric: null
          recordCount: null
          namespaceCount: null
          sizeBytes: null
          tags: {}
          createdAt: 2025-05-16T19:46:26.248428Z
          additionalProperties: null
      }]
      pagination: null
      additionalProperties: null
  }
  ```

  ```go Go theme={null}
  {
    "data": [
      {
        "backup_id": "bf2cda5d-b233-4a0a-aae9-b592780ad3ff",
        "cloud": "aws",
        "created_at": "2025-05-16T18:01:51.531129Z",
        "description": "Monthly backup of production index",
        "dimension": 0,
        "name": "example-backup",
        "namespace_count": 1,
        "record_count": 96,
        "region": "us-east-1",
        "size_bytes": 86393,
        "source_index_id": "bcb5b3c9-903e-4cb6-8b37-a6072aeb874f",
        "source_index_name": "docs-example",
        "status": "Ready",
        "tags": {}
      },
      {
        "backup_id": "e12269b0-a29b-4af0-9729-c7771dec03e3",
        "cloud": "aws",
        "created_at": "2025-05-14T17:00:45.803146Z",
        "dimension": 0,
        "name": "example-backup2",
        "namespace_count": 1,
        "record_count": 96,
        "region": "us-east-1",
        "size_bytes": 86393,
        "source_index_id": "bcb5b3c9-903e-4cb6-8b37-a6072aeb874f",
        "source_index_name": "docs-example",
        "status": "Ready"
      }
    ],
    "pagination": {
      "next": "eyJsaW1pdCI6Miwib2Zmc2V0IjoyfQ=="
    }
  }
  ```

  ```csharp C# theme={null}
  {
    "data":
    [
      {
        "backup_id":"9947520e-d5a1-4418-a78d-9f464c9969da",
        "source_index_id":"8433941a-dae7-43b5-ac2c-d3dab4a56b2b",
        "source_index_name":"docs-example",
        "tags":{},
        "name":"example-backup",
        "description":"Monthly backup of production index",
        "status":"Pending",
        "cloud":"aws",
        "region":"us-east-1",
        "dimension":1024,
        "record_count":98,
        "namespace_count":3,
        "size_bytes":1069169,
        "created_at":"2025-03-11T18:29:50.549505Z"
      }
    ]
  }
  ```

  ```json curl theme={null}
  {
    "data":
    [
      {
        "backup_id":"9947520e-d5a1-4418-a78d-9f464c9969da",
        "source_index_id":"8433941a-dae7-43b5-ac2c-d3dab4a56b2b",
        "source_index_name":"docs-example",
        "tags":{},
        "name":"example-backup",
        "description":"Monthly backup of production index",
        "status":"Pending",
        "cloud":"aws",
        "region":"us-east-1",
        "dimension":1024,
        "record_count":98,
        "namespace_count":3,
        "size_bytes":1069169,
        "created_at":"2025-03-11T18:29:50.549505Z"
        }
      ],
    "pagination":null
  }
  ```
</CodeGroup>

<Tip>
  You can view the backups for a specific index from either the [Backups](https://app.pinecone.io/organizations/-/projects/-/backups) tab or the [Indexes](https://app.pinecone.io/organizations/-/projects/-/indexes) tab in the Pinecone console.
</Tip>



# Manage namespaces
Source: https://docs.pinecone.io/guides/manage-data/manage-namespaces

Create and manage namespaces in serverless indexes.


## Create a namespace

<Warning>
  This feature is in [early access](/release-notes/feature-availability) and available only on the `2025-10` version of the API.
</Warning>

Namespaces are created automatically during [upsert](/guides/index-data/upsert-data). However, you can also create namespaces ahead of time using the [`create_namespace`](/reference/api/2025-10/data-plane/createnamespace) operation. Specify a name for the namespace and, optionally, the [metadata fields to index](/guides/index-data/create-an-index#metadata-indexing).

```shell curl theme={null}

# To get the unique host for an index,

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
            "document_id": {"filterable": true},
            "document_title": {"filterable": true},
            "chunk_number": {"filterable": true},
            "document_url": {"filterable": true},
            "created_at": {"filterable": true}
          }
        }
      }'
```

The response will look like the following:

```json curl theme={null}
{
    "name": "example-namespace",
    "record_count": "0",
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


## List all namespaces in an index

Use the [`list_namespaces`](/reference/api/latest/data-plane/listnamespaces) operation to list all namespaces in a serverless index.

Up to 100 namespaces are returned at a time by default, in sorted order (bitwise “C” collation). If the `limit` parameter is set, up to that number of namespaces are returned instead. Whenever there are additional namespaces to return, the response also includes a `pagination_token` that you can use to get the next batch of namespaces. When the response does not include a `pagination_token`, there are no more namespaces to return.

<CodeGroup>
  ```python Python theme={null}
  # Not supported with pinecone["grpc"] extras installed
  from pinecone import Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  index = pc.Index(host="INDEX_HOST")

  # Implicit pagination using a generator function
  for namespace in index.list_namespaces():
      print(namespace.name, ":", namespace.record_count)

  # Manual pagination
  namespaces = index.list_namespaces_paginated(
      limit=2,
      pagination_token="eyJza2lwX3Bhc3QiOiIxMDEwMy0="
  )

  print(namespaces)
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' })

  // To get the unique host for an index, 
  // see https://docs.pinecone.io/guides/manage-data/target-an-index
  var index = pinecone.Index(host: "INDEX_HOST");

  const namespaceList = await index.listNamespaces();

  console.log(namespaceList);
  ```

  ```java Java theme={null}
  import io.pinecone.clients.AsyncIndex;
  import io.pinecone.clients.Index;
  import io.pinecone.configs.PineconeConfig;
  import io.pinecone.configs.PineconeConnection;
  import io.pinecone.proto.ListNamespacesResponse;
  import org.openapitools.db_data.client.ApiException;

  public class Namespaces {
      public static void main(String[] args) throws ApiException {
          PineconeConfig config = new PineconeConfig("YOUR_API_KEY");
          // To get the unique host for an index, 
          // see https://docs.pinecone.io/guides/manage-data/target-an-index
          config.setHost("INDEX_HOST");
          PineconeConnection connection = new PineconeConnection(config);

          Index index = new Index(config, connection, "docs-example");

          // List all namespaces with default pagination limit (100)
          ListNamespacesResponse listNamespacesResponse = index.listNamespaces(null, null);

          // List all namespaces with pagination limit of 2
          ListNamespacesResponse listNamespacesResponseWithLimit = index.listNamespaces(2);

          // List all namespaces with pagination limit and token
          ListNamespacesResponse listNamespacesResponsePaginated = index.listNamespaces(5, "eyJza2lwX3Bhc3QiOiIxMDEwMy0=");

          System.out.println(listNamespacesResponseWithLimit);
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
      idxConnection, err := pc.Index(pinecone.NewIndexConnParams{Host: "INDEX_HOST"})
      if err != nil {
          log.Fatalf("Failed to create IndexConnection for Host: %v", err)
      } 

      limit := uint32(10)
      namespaces, err := idxConnection.ListNamespaces(ctx, &pinecone.ListNamespacesParams{
          Limit: &limit,
      })
      if err != nil {
          log.Fatalf("Failed to list namespaces: %v", err)
      }
      fmt.Printf(prettifyStruct(namespaces))
  }
  ```

  ```csharp C# theme={null}
  using Pinecone;

  var pinecone = new PineconeClient("PINECONE_API_KEY");

  // To get the unique host for an index, 
  // see https://docs.pinecone.io/guides/manage-data/target-an-index
  var index = pinecone.Index(host: "INDEX_HOST");

  var namespaces = await index.ListNamespacesAsync(new ListNamespacesRequest());

  Console.WriteLine(namespaces);
  ```

  ```shell curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="INDEX_HOST"

  curl -X GET "https://$INDEX_HOST/namespaces" \
      -H "Api-Key: $PINECONE_API_KEY" \
      -H "X-Pinecone-API-Version: 2025-04"
  ```
</CodeGroup>

The response will look like the following:

<CodeGroup>
  ```python Python theme={null}
  # Implicit pagination
  example-namespace : 20000
  example-namespace2 : 10500
  example-namespace3 : 10000
  ...

  # Manual pagination
  {
      "namespaces": [
          {
              "name": "example-namespace",
              "record_count": "20000"
          },
          {
              "name": "example-namespace2",
              "record_count": "10500"
          }
      ],
      "pagination": {
          "next": "Tm90aGluZyB0byBzZWUgaGVyZQo="
      }
  }
  ```

  ```javascript JavaScript theme={null}
  {
    namespaces: [
      { name: 'example-namespace', recordCount: '20000' },
      { name: 'example-namespace2', recordCount: '10500' },
      ...
    ],
    pagination: "Tm90aGluZyB0byBzZWUgaGVyZQo="
  }
  ```

  ```java Java theme={null}
  namespaces {
    name: "example-namespace"
    record_count: 20000
  }
  namespaces {
    name: "example-namespace2"
    record_count: 10500
  }
  pagination {
    next: "eyJza2lwX3Bhc3QiOiJlZDVhYzFiNi1kMDFiLTQ2NTgtYWVhZS1hYjJkMGI2YzBiZjQiLCJwcmVmaXgiOm51bGx9"
  }
  ```

  ```go Go theme={null}
  {
    "Namespaces": [
      {
        "name": "example-namespace",
        "record_count": 20000
      },
      {
        "name": "example-namespace2",
        "record_count": 10500
      },
      ...
    ],
    "Pagination": {
      "next": "eyJza2lwX3Bhc3QiOiIyNzQ5YTU1YS0zZTQ2LTQ4MDItOGFlNi1hZTJjZGNkMTE5N2IiLCJwcmVmaXgiOm51bGx9"
    }
  }
  ```

  ```csharp C# theme={null}
  {
    "namespaces":[
      {"name":"example-namespace","recordCount":20000},
      {"name":"example-namespace2","recordCount":10500},
      ...
    ],
    "pagination":"Tm90aGluZyB0byBzZWUgaGVyZQo="
  }
  ```

  ```json curl theme={null}
  {
    "namespaces": [
      {
        "name": "example-namespace",
        "record_count": 20000
      },
      {
        "name": "example-namespace2",
        "record_count": 10500
      },
      ...
    ],
    "pagination": {
      "next": "Tm90aGluZyB0byBzZWUgaGVyZQo="
    }
  }
  ```
</CodeGroup>


## Describe a namespace

Use the [`describe_namespace`](/reference/api/latest/data-plane/describenamespace) operation to get details about a namespace in a serverless index, including the total number of vectors in the namespace.

<CodeGroup>
  ```python Python theme={null}
  # Not supported with pinecone["grpc"] extras installed
  from pinecone import Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  index = pc.Index(host="INDEX_HOST")

  namespace = index.describe_namespace(namespace="example-namespace")

  print(namespace)
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' })

  const index = pc.index('docs-example');

  const namespace = await index.describeNamespace('example-namespace');

  console.log(namespace);
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Index;
  import io.pinecone.configs.PineconeConfig;
  import io.pinecone.configs.PineconeConnection;
  import io.pinecone.proto.NamespaceDescription;

  import org.openapitools.db_data.client.ApiException;

  public class Namespaces {
      public static void main(String[] args) throws ApiException {
          PineconeConfig config = new PineconeConfig("YOUR_API_KEY");
          // To get the unique host for an index, 
          // see https://docs.pinecone.io/guides/manage-data/target-an-index
          config.setHost("INDEX_HOST");
          PineconeConnection connection = new PineconeConnection(config);

          Index index = new Index(config, connection, "docs-example");

          NamespaceDescription namespaceDescription = index.describeNamespace("example-namespace");

          System.out.println(namespaceDescription);
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
      idxConnection, err := pc.Index(pinecone.NewIndexConnParams{Host: "INDEX_HOST"})
      if err != nil {
          log.Fatalf("Failed to create IndexConnection for Host: %v", err)
      } 

      namespace, err := idxConnection.DescribeNamespace(ctx, "example-namespace")
      if err != nil {
          log.Fatalf("Failed to describe namespace: %v", err)
      }
      fmt.Printf(prettifyStruct(namespace))
  }
  ```

  ```csharp C# theme={null}
  using Pinecone;

  var pinecone = new PineconeClient("PINECONE_API_KEY");

  // To get the unique host for an index, 
  // see https://docs.pinecone.io/guides/manage-data/target-an-index
  var index = pinecone.Index(host: "INDEX_HOST");

  var @namespace = await index.DescribeNamespaceAsync("example-namespace");

  Console.WriteLine(@namespace);
  ```

  ```shell curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="INDEX_HOST"
  NAMESPACE="NAMESPACE_NAME"  # To target the default namespace, use "__default__".

  curl -X GET "https://$INDEX_HOST/namespaces/$NAMESPACE" \
      -H "Api-Key: $PINECONE_API_KEY" \
      -H "X-Pinecone-API-Version: 2025-04"
  ```
</CodeGroup>

The response will look like the following:

<CodeGroup>
  ```python Python theme={null}
  {
      "name": "example-namespace",
      "record_count": "20000"
  }
  ```

  ```javascript JavaScript theme={null}
  { name: 'example-namespace', recordCount: '20000' }
  ```

  ```java Java theme={null}
  name: "example-namespace"
  record_count: 20000
  ```

  ```go Go theme={null}
  {
    "name": "example-namespace",
    "record_count": 20000
  }
  ```

  ```csharp C# theme={null}
  {"name":"example-namespace","recordCount":20000}
  ```

  ```json curl theme={null}
  {
    "name": "example-namespace",
    "record_count": 20000
  }
  ```
</CodeGroup>


## Delete a namespace

Use the [`delete_namespace`](/reference/api/latest/data-plane/deletenamespace) operation to delete a namespace in a serverless index.

<Warning>
  Deleting a namespace is irreversible. All data in the namespace is permanently deleted.
</Warning>

<CodeGroup>
  ```python Python theme={null}
  # Not supported with pinecone["grpc"] extras installed
  from pinecone import Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  index = pc.Index(host="INDEX_HOST")

  index.delete_namespace(namespace="example-namespace")
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' })

  const index = pc.index('INDEX_NAME', 'INDEX_HOST');

  const namespace = await index.deleteNamespace('example-namespace');

  console.log(namespace);
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Index;
  import io.pinecone.configs.PineconeConfig;
  import io.pinecone.configs.PineconeConnection;

  import java.util.concurrent.ExecutionException;

  public class DeleteNamespace {
      public static void main(String[] args) throws ExecutionException, InterruptedException {
          PineconeConfig config = new PineconeConfig("YOUR_API_KEY");
        // To get the unique host for an index, 
        // see https://docs.pinecone.io/guides/manage-data/target-an-index
          config.setHost("INDEX_HOST");
          PineconeConnection connection = new PineconeConnection(config);

          Index index = new Index(config, connection, "docs-example");

          index.deleteNamespace("example-namespace");
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
      idxConnection, err := pc.Index(pinecone.NewIndexConnParams{Host: "INDEX_HOST"})
      if err != nil {
          log.Fatalf("Failed to create IndexConnection for Host: %v", err)
      } 

      err := idxConnection.DeleteNamespace(ctx, "example-namespace")
      if err != nil {
          log.Fatalf("Failed to delete namespace: %v", err)
      }
  }
  ```

  ```csharp C# theme={null}
  using Pinecone;

  const pinecone = new PineconeClient("PINECONE_API_KEY");

  // To get the unique host for an index, 
  // see https://docs.pinecone.io/guides/manage-data/target-an-index
  const index = pinecone.Index(host: "INDEX_HOST");

  await index.DeleteNamespaceAsync("example-namespace");
  ```

  ```shell curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="INDEX_HOST"
  NAMESPACE="NAMESPACE_NAME" # To target the default namespace, use "__default__".

  curl -X DELETE "https://$INDEX_HOST/namespaces/$NAMESPACE" \
      -H "Api-Key: $PINECONE_API_KEY" \
      -H "X-Pinecone-API-Version: 2025-04"
  ```
</CodeGroup>


## Rename a namespace

Pinecone does not support renaming namespaces directly. Instead, you must [delete the records](/guides/manage-data/delete-data) in the namespace and [upsert the records](/guides/index-data/upsert-data) to a new namespace.


## Move records to a new namespace

Pinecone does not support moving records between namespaces directly. Instead, you must [delete the records](/guides/manage-data/delete-data) in the old namespace and [upsert the records](/guides/index-data/upsert-data) to the new namespace.


## Use the default namespace

To use the default namespace for upserts, queries, or other data operations, set the `namespace` parameter to `__default__`, for example:

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
  NAMESPACE="NAMESPACE_NAME"
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



# Restore an index
Source: https://docs.pinecone.io/guides/manage-data/restore-an-index

Restore serverless indexes from backup snapshots.


## Create a serverless index from a backup

When restoring a serverless index from backup, you can change the index name, tags, and deletion protection setting. All other properties of the restored index will remain identical to the source index, including cloud and region, dimension and similarity metric, and associated embedding model when restoring an index with [integrated embedding](/guides/index-data/indexing-overview#integrated-embedding).

To [create a serverless index from a backup](/reference/api/latest/control-plane/create_index_from_backup), provide the ID of the backup, the name of the new index, and, optionally, changes to the index tags and deletion protection settings:

<CodeGroup>
  ```python Python theme={null}
  from pinecone import Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  pc.create_index_from_backup(
      backup_id="a65ff585-d987-4da5-a622-72e19a6ed5f4",
      name="restored-index",
      tags={
          "tag0": "val0", 
          "tag1": "val1"
      },
      deletion_protection="enabled"
  )
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' })

  const response = await pc.createIndexFromBackup({
    backupId: 'a65ff585-d987-4da5-a622-72e19a6ed5f4',
    name: 'restored-index',
    tags: {
      tag0: 'val0',
      tag1: 'val1'
    },
    deletionProtection: 'enabled'
  });

  console.log(response);
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Pinecone;
  import org.openapitools.db_control.client.ApiException;
  import org.openapitools.db_control.client.model.*;

  public class CreateIndexFromBackup {
      public static void main(String[] args) throws ApiException {
          Pinecone pc = new Pinecone.Builder("YOUR_API_KEY").build();

          String backupID = "a65ff585-d987-4da5-a622-72e19a6ed5f4";
          String indexName = "restored-index";

          CreateIndexFromBackupResponse backupResponse = pc.createIndexFromBackup(backupID, indexName);
          System.out.println(backupResponse);
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
  	"time"

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

  	indexName := "restored-index"
  	restoredIndexTags := pinecone.IndexTags{"restored_on": time.Now().Format("2006-01-02 15:04")}
  	createIndexFromBackupResp, err := pc.CreateIndexFromBackup(ctx, &pinecone.CreateIndexFromBackupParams{
  		BackupId: "e12269b0-a29b-4af0-9729-c7771dec03e3",
  		Name:     indexName,
  		Tags:     &restoredIndexTags,
  	})

  	fmt.Printf(prettifyStruct(createIndexFromBackupResp))
  }
  ```

  ```csharp C# theme={null}
  using Pinecone;

  var pinecone = new PineconeClient("YOUR_API_KEY");

  var response = await pinecone.Backups.CreateIndexFromBackupAsync(
      "a65ff585-d987-4da5-a622-72e19a6ed5f4", 
      new CreateIndexFromBackupRequest
      {
          Name = "restored-index",
          Tags = new Dictionary<string, string> 
          { 
              { "tag0", "val0" },
              { "tag1", "val1" }
          },
          DeletionProtection = DeletionProtection.Enabled
      }
  );

  Console.WriteLine(response);
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  BACKUP_ID="a65ff585-d987-4da5-a622-72e19a6ed5f4"

  curl "https://api.pinecone.io/backups/$BACKUP_ID/create-index" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-API-Version: 2025-04" \
    -H 'Content-Type: application/json' \
    -d '{
          "name": "restored-index",
          "tags": {
            "tag0": "val0",
            "tag1": "val1"
          },
          "deletion_protection": "enabled"
        }'
  ```
</CodeGroup>

The example returns a response like the following:

<CodeGroup>
  ```python Python theme={null}
  {'deletion_protection': 'enabled',
   'dimension': 1024,
   'embed': {'dimension': 1024,
             'field_map': {'text': 'chunk_text'},
             'metric': 'cosine',
             'model': 'multilingual-e5-large',
             'read_parameters': {'input_type': 'query', 'truncate': 'END'},
             'vector_type': 'dense',
             'write_parameters': {'input_type': 'passage', 'truncate': 'END'}},
   'host': 'example-dense-index-python3-govk0nt.svc.aped-4627-b74a.pinecone.io',
   'metric': 'cosine',
   'name': 'example-dense-index-python3',
   'spec': {'serverless': {'cloud': 'aws', 'region': 'us-east-1'}},
   'status': {'ready': True, 'state': 'Ready'},
   'tags': {'tag0': 'val0', 'tag1': 'val1'},
   'vector_type': 'dense'}
  ```

  ```javascript JavaScript theme={null}
  {
    restoreJobId: 'e9ba8ff8-7948-4cfa-ba43-34227f6d30d4',
    indexId: '025117b3-e683-423c-b2d1-6d30fbe5027f'
  }
  ```

  ```java Java theme={null}
  class CreateIndexFromBackupResponse {
      restoreJobId: e9ba8ff8-7948-4cfa-ba43-34227f6d30d4
      indexId: 025117b3-e683-423c-b2d1-6d30fbe5027f
      additionalProperties: null
  }
  ```

  ```go Go theme={null}
  {
    "index_id": "025117b3-e683-423c-b2d1-6d30fbe5027f",
    "restore_job_id": "e9ba8ff8-7948-4cfa-ba43-34227f6d30d4"
  }
  ```

  ```csharp C# theme={null}
  {
      "restore_job_id":"e9ba8ff8-7948-4cfa-ba43-34227f6d30d4",
      "index_id":"025117b3-e683-423c-b2d1-6d30fbe5027f"
  }
  ```

  ```json curl theme={null}
  {
      "restore_job_id":"e9ba8ff8-7948-4cfa-ba43-34227f6d30d4",
      "index_id":"025117b3-e683-423c-b2d1-6d30fbe5027f"
  }
  ```
</CodeGroup>

<Tip>
  You can create a serverless index from a backup using the [Pinecone console](https://app.pinecone.io/organizations/-/projects).
</Tip>


## List restore jobs

You can [list all restore jobs](/reference/api/latest/control-plane/list_restore_jobs) as follows.

<Note>
  Up to 100 restore jobs are returned at a time by default, in sorted order (bitwise “C” collation). If the `limit` parameter is set, up to that number of restore jobs are returned instead. Whenever there are additional restore jobs to return, the response also includes a `pagination_token` that you can use to get the next batch of jobs. When the response does not include a `pagination_token`, there are no more restore jobs to return.
</Note>

<CodeGroup>
  ```python Python theme={null}
  from pinecone import Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  restore_jobs = pc.list_restore_jobs()

  print(restore_jobs)
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' })

  const restoreJobs = await pc.listRestoreJobs();

  console.log(restoreJobs);
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Pinecone;
  import org.openapitools.db_control.client.ApiException;
  import org.openapitools.db_control.client.model.*;

  public class CreateIndexFromBackup {
      public static void main(String[] args) throws ApiException {
          Pinecone pc = new Pinecone.Builder("YOUR_API-KEY").build();

          // List all restore jobs with default pagination limit
          RestoreJobList restoreJobList = pc.listRestoreJobs(null, null);

          // List all restore jobs with pagination limit of 5
          RestoreJobList restoreJobListWithLimit = pc.listRestoreJobs(5);

          // List all restore jobs with pagination limit and token
          RestoreJobList restoreJobListPaginated = pc.listRestoreJobs(5, "eyJza2lwX3Bhc3QiOiIxMDEwMy0=");

          System.out.println(restoreJobList);
          System.out.println(restoreJobListWithLimit);
          System.out.println(restoreJobListPaginated);
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

  	limit := 2
  	restoreJobs, err := pc.ListRestoreJobs(ctx, &pinecone.ListRestoreJobsParams{
  		Limit: &limit,
  	})
  	if err != nil {
  		log.Fatalf("Failed to list restore jobs: %v", err)
  	}

  	fmt.Printf(prettifyStruct(restoreJobs))
  }
  ```

  ```csharp C# theme={null}
  using Pinecone;

  var pinecone = new PineconeClient("YOUR_API_KEY");

  var jobs = await pinecone.RestoreJobs.ListAsync(new ListRestoreJobsRequest());

  Console.WriteLine(jobs);
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl "https://api.pinecone.io/restore-jobs" \
  	-H "X-Pinecone-Api-Version: 2025-04" \
  	-H "Api-Key: $PINECONE_API_KEY"
  ```
</CodeGroup>

The example returns a response like the following:

<CodeGroup>
  ```python Python theme={null}
  [{
      "restore_job_id": "06b08366-a0a9-404d-96c2-e791c71743e5",
      "backup_id": "95707edb-e482-49cf-b5a5-312219a51a97",
      "target_index_name": "restored-index",
      "target_index_id": "027aff93-de40-4f48-a573-6dbcd654f961",
      "status": "Completed",
      "created_at": "2025-05-15T13:59:51.439479+00:00",
      "completed_at": "2025-05-15T14:00:09.222998+00:00",
      "percent_complete": 100.0
  }, {
      "restore_job_id": "4902f735-b876-4e53-a05c-bc01d99251cb",
      "backup_id": "8c85e612-ed1c-4f97-9f8c-8194e07bcf71",
      "target_index_name": "restored-index2",
      "target_index_id": "027aff93-de40-4f48-a573-6dbcd654f961",
      "status": "Completed",
      "created_at": "2025-05-15T21:06:19.906074+00:00",
      "completed_at": "2025-05-15T21:06:39.360509+00:00",
      "percent_complete": 100.0
  }]
  ```

  ```javascript JavaScript theme={null}
  {
    data: [
      {
        restoreJobId: '69acc1d0-9105-4fcb-b1db-ebf97b285c5e',
        backupId: '8c85e612-ed1c-4f97-9f8c-8194e07bcf71',
        targetIndexName: 'restored-index2',
        targetIndexId: 'e6c0387f-33db-4227-9e91-32181106e56b',
        status: 'Completed',
        createdAt: 2025-05-14T17:25:59.378Z,
        completedAt: 2025-05-14T17:26:23.997Z,
        percentComplete: 100
      },
      {
        restoreJobId: '9857add2-99d4-4399-870e-aa7f15d8d326',
        backupId: '94a63aeb-efae-4f7a-b059-75d32c27ca57',
        targetIndexName: 'restored-index',
        targetIndexId: '0d8aed24-adf8-4b77-8e10-fd674309dc85',
        status: 'Completed',
        createdAt: 2025-04-25T18:14:05.227Z,
        completedAt: 2025-04-25T18:14:11.074Z,
        percentComplete: 100
      }
    ],
    pagination: undefined
  }
  ```

  ```java Java theme={null}
  class RestoreJobList {
      data: [class RestoreJobModel {
          restoreJobId: cf597d76-4484-4b6c-b07c-2bfcac3388aa
          backupId: 0d75b99f-be61-4a93-905e-77201286c02e
          targetIndexName: restored-index
          targetIndexId: 8a810881-1505-46c0-b906-947c048b15f5
          status: Completed
          createdAt: 2025-05-16T20:09:18.700631Z
          completedAt: 2025-05-16T20:11:30.673296Z
          percentComplete: 100.0
          additionalProperties: null
      }, class RestoreJobModel {
          restoreJobId: 4902f735-b876-4e53-a05c-bc01d99251cb
          backupId: 8c85e612-ed1c-4f97-9f8c-8194e07bcf71
          targetIndexName: restored-index2
          targetIndexId: 710cb6e6-bfb4-4bf5-a425-9754e5bbc832
          status: Completed
          createdAt: 2025-05-15T21:06:19.906074Z
          completedAt: 2025-05-15T21:06:39.360509Z
          percentComplete: 100.0
          additionalProperties: null
      }]
      pagination: class PaginationResponse {
          next: eyJsaW1pdCI6Miwib2Zmc2V0IjoyfQ==
          additionalProperties: null
      }
      additionalProperties: null
  }
  ```

  ```go Go theme={null}
  {
    "data": [
      {
        "backup_id": "8c85e612-ed1c-4f97-9f8c-8194e07bcf71",
        "completed_at": "2025-05-16T20:11:30.673296Z",
        "created_at": "2025-05-16T20:09:18.700631Z",
        "percent_complete": 100,
        "restore_job_id": "e9ba8ff8-7948-4cfa-ba43-34227f6d30d4",
        "status": "Completed",
        "target_index_id": "025117b3-e683-423c-b2d1-6d30fbe5027f",
        "target_index_name": "restored-index"
      },
      {
        "backup_id": "95707edb-e482-49cf-b5a5-312219a51a97",
        "completed_at": "2025-05-15T21:04:34.2463Z",
        "created_at": "2025-05-15T21:04:15.949067Z",
        "percent_complete": 100,
        "restore_job_id": "eee4f8b8-cd3e-45fe-9ed5-93c28e237f24",
        "status": "Completed",
        "target_index_id": "5a0d555f-7ccd-422a-a3a6-78f7b73350c0",
        "target_index_name": "restored-index2"
      }
    ],
    "pagination": {
      "next": "eyJsaW1pdCI6MTAsIm9mZnNldCI6MTB9"
    }
  }
  ```

  ```csharp C# theme={null}
  {
    "data": [
      {
        "restore_job_id": "9857add2-99d4-4399-870e-aa7f15d8d326",
        "backup_id": "94a63aeb-efae-4f7a-b059-75d32c27ca57",
        "target_index_name": "restored-index",
        "target_index_id": "0d8aed24-adf8-4b77-8e10-fd674309dc85",
        "status": "Completed",
        "created_at": "2025-04-25T18:14:05.227526Z",
        "completed_at": "2025-04-25T18:14:11.074618Z",
        "percent_complete": 100
      },
      {
        "restore_job_id": "69acc1d0-9105-4fcb-b1db-ebf97b285c5e",
        "backup_id": "8c85e612-ed1c-4f97-9f8c-8194e07bcf71",
        "target_index_name": "restored-index2",
        "target_index_id": "e6c0387f-33db-4227-9e91-32181106e56b",
        "status": "Completed",
        "created_at": "2025-05-14T17:25:59.378989Z",
        "completed_at": "2025-05-14T17:26:23.997284Z",
        "percent_complete": 100
      }
    ]
  }
  ```

  ```json curl theme={null}
  {
    "data": [
      {
        "restore_job_id": "9857add2-99d4-4399-870e-aa7f15d8d326",
        "backup_id": "94a63aeb-efae-4f7a-b059-75d32c27ca57",
        "target_index_name": "restored-index",
        "target_index_id": "0d8aed24-adf8-4b77-8e10-fd674309dc85",
        "status": "Completed",
        "created_at": "2025-04-25T18:14:05.227526Z",
        "completed_at": "2025-04-25T18:14:11.074618Z",
        "percent_complete": 100
      },
      {
        "restore_job_id": "69acc1d0-9105-4fcb-b1db-ebf97b285c5e",
        "backup_id": "8c85e612-ed1c-4f97-9f8c-8194e07bcf71",
        "target_index_name": "restored-index2",
        "target_index_id": "e6c0387f-33db-4227-9e91-32181106e56b",
        "status": "Completed",
        "created_at": "2025-05-14T17:25:59.378989Z",
        "completed_at": "2025-05-14T17:26:23.997284Z",
        "percent_complete": 100
      }
    ],
    "pagination": null
  }
  ```
</CodeGroup>


## View restore job details

You can [view the details of a specific restore job](/reference/api/latest/control-plane/describe_restore_job), as in the following example:

<CodeGroup>
  ```python Python theme={null}
  from pinecone import Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  restore_job = pc.describe_restore_job(job_id="9857add2-99d4-4399-870e-aa7f15d8d326")

  print(restore_job)
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' })

  const restoreJob = await pc.describeRestoreJob('9857add2-99d4-4399-870e-aa7f15d8d326');

  console.log(restoreJob);
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Pinecone;
  import org.openapitools.db_control.client.ApiException;
  import org.openapitools.db_control.client.model.*;

  public class CreateIndexFromBackup {
      public static void main(String[] args) throws ApiException {
          Pinecone pc = new Pinecone.Builder("YOUR_API-KEY").build();

          RestoreJobModel restoreJob = pc.describeRestoreJob("9857add2-99d4-4399-870e-aa7f15d8d326");

          System.out.println(restoreJob);
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

  	restoreJob, err := pc.DescribeRestoreJob(ctx, "e9ba8ff8-7948-4cfa-ba43-34227f6d30d4")
  	if err != nil {
  		log.Fatalf("Failed to describe restore job: %v", err)
  	}

  	fmt.Printf(prettifyStruct(restoreJob))
  }
  ```

  ```csharp C# theme={null}
  using Pinecone;

  var pinecone = new PineconeClient("YOUR_API_KEY");

  var job = await pinecone.RestoreJobs.GetAsync("9857add2-99d4-4399-870e-aa7f15d8d326");

  Console.WriteLine(job);
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  JOB_ID="9857add2-99d4-4399-870e-aa7f15d8d326"

  curl "https://api.pinecone.io/restore-jobs/$JOB_ID" \
      -H "X-Pinecone-Api-Version: 2025-04" \
      -H "Api-Key: $PINECONE_API_KEY" \
      -H 'accept: application/json'
  ```
</CodeGroup>

The example returns a response like the following:

<CodeGroup>
  ```python Python theme={null}
  {'backup_id': '94a63aeb-efae-4f7a-b059-75d32c27ca57',
   'completed_at': datetime.datetime(2025, 4, 25, 18, 14, 11, 74618, tzinfo=tzutc()),
   'created_at': datetime.datetime(2025, 4, 25, 18, 14, 5, 227526, tzinfo=tzutc()),
   'percent_complete': 100.0,
   'restore_job_id': '9857add2-99d4-4399-870e-aa7f15d8d326',
   'status': 'Completed',
   'target_index_id': '0d8aed24-adf8-4b77-8e10-fd674309dc85',
   'target_index_name': 'restored-index'}
  ```

  ```javascript JavaScript theme={null}
  {
    restoreJobId: '9857add2-99d4-4399-870e-aa7f15d8d326',
    backupId: '94a63aeb-efae-4f7a-b059-75d32c27ca57',
    targetIndexName: 'restored-index',
    targetIndexId: '0d8aed24-adf8-4b77-8e10-fd674309dc85',
    status: 'Completed',
    createdAt: 2025-04-25T18:14:05.227Z,
    completedAt: 2025-04-25T18:14:11.074Z,
    percentComplete: 100
  }
  ```

  ```java Java theme={null}
  class RestoreJobModel {
      restoreJobId: cf597d76-4484-4b6c-b07c-2bfcac3388aa
      backupId: 0d75b99f-be61-4a93-905e-77201286c02e
      targetIndexName: restored-index
      targetIndexId: 0d8aed24-adf8-4b77-8e10-fd674309dc85
      status: Completed
      createdAt: 2025-05-16T20:09:18.700631Z
      completedAt: 2025-05-16T20:11:30.673296Z
      percentComplete: 100.0
      additionalProperties: null
  }
  ```

  ```go Go theme={null}
  {
    "backup_id": "8c85e612-ed1c-4f97-9f8c-8194e07bcf71",
    "completed_at": "2025-05-16T20:11:30.673296Z",
    "created_at": "2025-05-16T20:09:18.700631Z",
    "percent_complete": 100,
    "restore_job_id": "e9ba8ff8-7948-4cfa-ba43-34227f6d30d4",
    "status": "Completed",
    "target_index_id": "025117b3-e683-423c-b2d1-6d30fbe5027f",
    "target_index_name": "restored-index"
  }
  ```

  ```csharp C# theme={null}
  {
    "restore_job_id": "9857add2-99d4-4399-870e-aa7f15d8d326",
    "backup_id": "94a63aeb-efae-4f7a-b059-75d32c27ca57",
    "target_index_name": "restored-index",
    "target_index_id": "0d8aed24-adf8-4b77-8e10-fd674309dc85",
    "status": "Completed",
    "created_at": "2025-04-25T18:14:05.227526Z",
    "completed_at": "2025-04-25T18:14:11.074618Z",
    "percent_complete": 100
  }
  ```

  ```json curl theme={null}
  {
    "restore_job_id": "9857add2-99d4-4399-870e-aa7f15d8d326",
    "backup_id": "94a63aeb-efae-4f7a-b059-75d32c27ca57",
    "target_index_name": "restored-index",
    "target_index_id": "0d8aed24-adf8-4b77-8e10-fd674309dc85",
    "status": "Completed",
    "created_at": "2025-04-25T18:14:05.227526Z",
    "completed_at": "2025-04-25T18:14:11.074618Z",
    "percent_complete": 100
  }
  ```
</CodeGroup>



---
**Navigation:** [← Previous](./07-back-up-an-index.md) | [Index](./index.md) | [Next →](./09-target-an-index.md)
