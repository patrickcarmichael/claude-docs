**Navigation:** [← Previous](./15-search-overview.md) | [Index](./index.md) | [Next →](./17-upsert-text.md)

# Delete vectors
Source: https://docs.pinecone.io/reference/api/2025-04/data-plane/delete

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-04/db_data_2025-04.oas.yaml post /vectors/delete
Delete vectors by id from a single namespace.

For guidance and examples, see [Delete data](https://docs.pinecone.io/guides/manage-data/delete-data).

<RequestExample>
  ```python Python theme={null}
  # pip install "pinecone[grpc]"
  from pinecone.grpc import PineconeGRPC as Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  # To get the unique host for an index, 
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  index = pc.Index(host="INDEX_HOST")

  index.delete(ids=["id-1", "id-2"], namespace="example-namespace")
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' })

  // To get the unique host for an index, 
  // see https://docs.pinecone.io/guides/manage-data/target-an-index
  const index = pc.index("INDEX_NAME", "INDEX_HOST")

  const ns = index.namespace('example-namespace')
  // Delete one record by ID.
  await ns.deleteOne('id-1');
  // Delete more than one record by ID.
  await ns.deleteMany(['id-2', 'id-3']);
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Index;
  import io.pinecone.configs.PineconeConfig;
  import io.pinecone.configs.PineconeConnection;

  import java.util.Arrays;
  import java.util.List;

  public class DeleteVectorsExample {
      public static void main(String[] args) {
          PineconeConfig config = new PineconeConfig("YOUR_API_KEY");
          // To get the unique host for an index, 
          // see https://docs.pinecone.io/guides/manage-data/target-an-index
          config.setHost("INDEX_HOST");
          PineconeConnection connection = new PineconeConnection(config);
          Index index = new Index(connection, "INDEX_NAME");
          List<String> ids = Arrays.asList("id-1  ", "id-2");
          index.deleteByIds(ids, "example-namespace");
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
      idxConnection, err := pc.Index(pinecone.NewIndexConnParams{Host: "INDEX_HOST", Namespace: "example-namespace"})
      if err != nil {
          log.Fatalf("Failed to create IndexConnection for Host: %v", err)
    	}

      id1 := "id-1"
      id2 := "id-2"

      err = idxConnection.DeleteVectorsById(ctx, []string{id1, id2})
      if err != nil {
          log.Fatalf("Failed to delete vector with ID %v: %v", id, err)
      }
  }
  ```

  ```csharp C# theme={null}
  using Pinecone;

  var pinecone = new PineconeClient("YOUR_API_KEY");

  // To get the unique host for an index, 
  // see https://docs.pinecone.io/guides/manage-data/target-an-index
  var index = pinecone.Index(host: "INDEX_HOST");

  var deleteResponse = await index.DeleteAsync(new DeleteRequest {
      Ids = new List<string> { "id-1", "id-2" },
      Namespace = "example-namespace",
  });
  ```

  ```shell curl theme={null}
  # To get the unique host for an index,
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="INDEX_HOST"

  curl "https://$INDEX_HOST/vectors/delete" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -H "X-Pinecone-API-Version: 2025-04" \
    -d '{
      "ids": [
        "id-1", 
        "id-2"
      ],
      "namespace": "example-namespace"
    }
  '
  ```
</RequestExample>

<ResponseExample>
  ```json  theme={null}
  {}
  ```
</ResponseExample>



# Delete a namespace
Source: https://docs.pinecone.io/reference/api/2025-04/data-plane/deletenamespace

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-04/db_data_2025-04.oas.yaml delete /namespaces/{namespace}
Delete a namespace from a serverless index. Deleting a namespace is irreversible; all data in the namespace is permanently deleted.

For guidance and examples, see [Manage namespaces](https://docs.pinecone.io/guides/manage-data/manage-namespaces).

**Note:** This operation is not supported for pod-based indexes.

<RequestExample>
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

  const index = pc.index('docs-example');

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

  var pinecone = new PineconeClient("PINECONE_API_KEY");

  // To get the unique host for an index, 
  // see https://docs.pinecone.io/guides/manage-data/target-an-index
  var index = pinecone.Index(host: "INDEX_HOST");

  await index.DeleteNamespaceAsync("example-namespace");
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="YOUR_INDEX_HOST"
  NAMESPACE="YOUR_NAMESPACE" # To target the default namespace, use "__default__".

  curl -X DELETE "https://$INDEX_HOST/namespaces/$NAMESPACE" \
      -H "Api-Key: $PINECONE_API_KEY" \
      -H "X-Pinecone-API-Version: 2025-04"
  ```
</RequestExample>

<ResponseExample />



# Get index stats
Source: https://docs.pinecone.io/reference/api/2025-04/data-plane/describeindexstats

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-04/db_data_2025-04.oas.yaml post /describe_index_stats
Return statistics about the contents of an index, including the vector count per namespace, the number of dimensions, and the index fullness.

Serverless indexes scale automatically as needed, so index fullness is relevant only for pod-based indexes.

<RequestExample>
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
  // npm install @pinecone-database/pinecone
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
</RequestExample>

<ResponseExample>
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
</ResponseExample>



# Describe a namespace
Source: https://docs.pinecone.io/reference/api/2025-04/data-plane/describenamespace

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-04/db_data_2025-04.oas.yaml get /namespaces/{namespace}
Describe a namespace in a serverless index, including the total number of vectors in the namespace.

For guidance and examples, see [Manage namespaces](https://docs.pinecone.io/guides/manage-data/manage-namespaces).

**Note:** This operation is not supported for pod-based indexes.

<RequestExample>
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

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="YOUR_INDEX_HOST"
  NAMESPACE="YOUR_NAMESPACE"  # To target the default namespace, use "__default__".

  curl "https://$INDEX_HOST/namespaces/$NAMESPACE" \
      -H "Api-Key: $PINECONE_API_KEY" \
      -H "X-Pinecone-API-Version: 2025-04"
  ```
</RequestExample>

<ResponseExample>
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
</ResponseExample>



# Fetch vectors
Source: https://docs.pinecone.io/reference/api/2025-04/data-plane/fetch

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-04/db_data_2025-04.oas.yaml get /vectors/fetch
Look up and return vectors by ID from a single namespace. The returned vectors include the vector data and/or metadata.

For guidance and examples, see [Fetch data](https://docs.pinecone.io/guides/manage-data/fetch-data).

<RequestExample>
  ```python Python theme={null}
  # pip install "pinecone[grpc]"
  from pinecone.grpc import PineconeGRPC as Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  # To get the unique host for an index, 
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  index = pc.Index(host="INDEX_HOST")

  index.fetch(ids=["id-1", "id-2"], namespace="example-namespace")
  ```

  ```javascript JavaScript theme={null}
  // npm install @pinecone-database/pinecone
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' })

  // To get the unique host for an index, 
  // see https://docs.pinecone.io/guides/manage-data/target-an-index
  const index = pc.index("INDEX_NAME", "INDEX_HOST")

  const fetchResult = await index.namespace('example-namespace').fetch(['id-1', 'id-2']);
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Index;
  import io.pinecone.configs.PineconeConfig;
  import io.pinecone.configs.PineconeConnection;
  import io.pinecone.proto.FetchResponse;

  import java.util.Arrays;
  import java.util.List;

  public class FetchExample {
      public static void main(String[] args) {
          PineconeConfig config = new PineconeConfig("YOUR_API_KEY");
          // To get the unique host for an index, 
          // see https://docs.pinecone.io/guides/manage-data/target-an-index
          config.setHost("INDEX_HOST");
          PineconeConnection connection = new PineconeConnection(config);
          Index index = new Index(connection, "INDEX_NAME");
          List<String> ids = Arrays.asList("id-1", "id-2");
          FetchResponse fetchResponse = index.fetch(ids, "example-namespace");
          System.out.println(fetchResponse);
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

      res, err := idxConnection.FetchVectors(ctx, []string{"id-1", "id-2"})
      if err != nil {
          log.Fatalf("Failed to fetch vectors: %+v", err)
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

  var fetchResponse = await index.FetchAsync(new FetchRequest {
      Ids = new List<string> { "id-1", "id-2" },
      Namespace = "example-namespace",
  });

  Console.WriteLine(fetchResponse);
  ```

  ```shell curl theme={null}
  # To get the unique host for an index,
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="INDEX_HOST"

  curl -X GET "https://$INDEX_HOST/vectors/fetch?ids=id-1&ids=id-2&namespace=example-namespace" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-API-Version: 2025-04"
  ```
</RequestExample>

<ResponseExample>
  ```Python Python theme={null}
  {'namespace': 'example-namespace',
   'usage': {'readUnits': 1},
   'vectors': {'id-1': {'id': 'id-1',
                        'values': [0.568879, 0.632687092, 0.856837332, ...]},
               'id-2': {'id': 'id-2',
                        'values': [0.00891787093, 0.581895, 0.315718859, ...]}}}
  ```

  ```JavaScript JavaScript theme={null}
  {'namespace': 'example-namespace',
   'usage': {'readUnits': 1},
   'records': {'id-1': {'id': 'id-1',
                        'values': [0.568879, 0.632687092, 0.856837332, ...]},
               'id-2': {'id': 'id-2',
                        'values': [0.00891787093, 0.581895, 0.315718859, ...]}}}
  ```

  ```java Java theme={null}
  namespace: "example-namespace"
  vectors {
    key: "id-1"
    value {
      id: "id-1"
      values: 0.568879
      values: 0.632687092
      values: 0.856837332
      ...
    }
  }
  vectors {
    key: "id-2"
    value {
      id: "id-2"
      values: 0.00891787093
      values: 0.581895
      values: 0.315718859
      ...
    }
  }
  usage {
    read_units: 1
  }
  ```

  ```go Go theme={null}
  {
    "vectors": {
      "id-1": {
        "id": "id-1",
        "values": [
          -0.0089730695,
          -0.020010853,
          -0.0042787646,
          ...
        ]
      },
      "id-2": {
        "id": "id-2",
        "values": [
          -0.005380766,
          0.00215196,
          -0.014833462,
          ...
        ]
      }
    },
    "usage": {
      "read_units": 1
    }
  }
  ```

  ```csharp C# theme={null}
  {
    "vectors": {
      "id-1": {
        "id": "id-1",
        "values": [
          -0.0089730695,
          -0.020010853,
          -0.0042787646,
          ...
        ],
        "sparseValues": null,
        "metadata": null
      },
      "vec1": {
        "id": "id-2",
        "values": [
          -0.005380766,
          0.00215196,
          -0.014833462,
          ...
        ],
        "sparseValues": null,
        "metadata": null
      }
    },
    "namespace": "example-namespace",
    "usage": {
      "readUnits": 1
    }
  ```

  ```json curl theme={null}
  {
    "vectors": {
      "id-1": {
        "id": "id-1",
        "values": [0.568879, 0.632687092, 0.856837332, ...]
      },
      "id-2": {
        "id": "id-2",
        "values": [0.00891787093, 0.581895, 0.315718859, ...]
      }
    },
    "namespace": "example-namespace",
    "usage": {"readUnits": 1},
  }
  ```
</ResponseExample>



# List vector IDs
Source: https://docs.pinecone.io/reference/api/2025-04/data-plane/list

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-04/db_data_2025-04.oas.yaml get /vectors/list
List the IDs of vectors in a single namespace of a serverless index. An optional prefix can be passed to limit the results to IDs with a common prefix.

Returns up to 100 IDs at a time by default in sorted order (bitwise "C" collation). If the `limit` parameter is set, `list` returns up to that number of IDs instead. Whenever there are additional IDs to return, the response also includes a `pagination_token` that you can use to get the next batch of IDs. When the response does not include a `pagination_token`, there are no more IDs to return.

For guidance and examples, see [List record IDs](https://docs.pinecone.io/guides/manage-data/list-record-ids).

**Note:** `list` is supported only for serverless indexes.

<RequestExample>
  ```python Python theme={null}
  # pip install "pinecone[grpc]"
  from pinecone.grpc import PineconeGRPC as Pinecone

  pc = Pinecone(api_key='YOUR_API_KEY')

  # To get the unique host for an index, 
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  index = pc.Index(host="INDEX_HOST")

  # Implicit pagination using a generator function
  for ids in index.list(prefix="doc1#", namespace="example-namespace"):
      print(ids)

  # Manual pagination
  results = index.list_paginated(
      prefix="doc1#",
      limit=3,
      namespace="example-namespace",
      pagination_token="eyJza2lwX3Bhc3QiOiIxMDEwMy0="
  )

  print(results)
  ```

  ```javascript JavaScript theme={null}
  // npm install @pinecone-database/pinecone
  import { Pinecone } from '@pinecone-database/pinecone';
  const pc = new Pinecone();

  // To get the unique host for an index, 
  // see https://docs.pinecone.io/guides/manage-data/target-an-index
  const index = pc.index("INDEX_NAME", "INDEX_HOST").namespace("example-namespace");

  const results = await index.listPaginated({ prefix: 'doc1#', limit: 3 });
  console.log(results);

  // Fetch the next page of results
  await index.listPaginated({ prefix: 'doc1#', paginationToken: results.pagination.next});
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Index;
  import io.pinecone.configs.PineconeConfig;
  import io.pinecone.configs.PineconeConnection;
  import io.pinecone.proto.ListResponse;

  public class ListExample {
      public static void main(String[] args) {
          PineconeConfig config = new PineconeConfig("YOUR_API_KEY");
          // To get the unique host for an index, 
          // see https://docs.pinecone.io/guides/manage-data/target-an-index
          config.setHost("INDEX_HOST");
          PineconeConnection connection = new PineconeConnection(config);
          Index index = new Index(connection, "INDEX_NAME");
          ListResponse listResponse = index.list("example-namespace", "doc1#", 3);
          System.out.println(listResponse);
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

      limit := uint32(3)
      prefix := "doc1#"

      res, err := idxConnection.ListVectors(ctx, &pinecone.ListVectorsRequest{
          Limit:  &limit,
          Prefix: &prefix,
      })
      if len(res.VectorIds) == 0 {
          fmt.Println("No vectors found")
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

  var listResponse = await index.ListAsync(new ListRequest {
      Namespace = "example-namespace",
      Prefix = "doc1#",
      Limit = 3,
  });

  Console.WriteLine(listResponse);
  ```

  ```shell curl theme={null}
  # To get the unique host for an index,
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="INDEX_HOST"

  curl -X GET "https://$INDEX_HOST/vectors/list?namespace=example-namespace&prefix=doc1#&limit=3" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-API-Version: 2025-04"
  ```
</RequestExample>

<ResponseExample>
  ```python Python theme={null}
  # Implicit pagination
  ['doc1#chunk1', 'doc1#chunk2', 'doc1#chunk3', 'doc1chunk4', ...]

  # Manual pagination
  {'namespace': 'example-namespace',
   'pagination': {'next': 'eyJza2lwX3Bhc3QiOiJkb2MxI2NodW5rMiIsInByZWZpeCI6ImRvYzEjIn0='},
   'usage': {'read_units': 1},
   'vectors': [{'id': 'doc1#chunk1'}, {'id': 'doc1#chunk2'}, {'id': 'doc1#chunk3'}]}
  ```

  ```js JavaScript theme={null}
  {
    vectors: [
      { id: 'doc1#chunk1' }, { id: 'doc1#chunk2' }, { id: 'doc1#chunk3' }
    ],
    pagination: {
      next: 'eyJza2lwX3Bhc3QiOiJwcmVUZXN0LS04MCIsInByZWZpeCI6InByZVRlc3QifQ=='
    },
    namespace: 'example-namespace',
    usage: { readUnits: 1 }
  }
  ```

  ```java Java theme={null}
  vectors {
    id: "doc1#chunk1"
  }
  vectors {
    id: "doc1#chunk2"
  }
  vectors {
    id: "doc1#chunk3"
  }
  pagination {
    next: "eyJza2lwX3Bhc3QiOiJhbHN0cm9lbWVyaWEtcGVydXZpYW4iLCJwcmVmaXgiOm51bGx9"
  }
  namespace: "example-namespace"
  usage {
    read_units: 1
  }
  ```

  ```go Go theme={null}
  {
    "vector_ids": [
      "doc1#chunk1",
      "doc1#chunk2",
      "doc1#chunk3"
    ],
    "usage": {
      "read_units": 1
    },
    "next_pagination_token": "eyJza2lwX3Bhc3QiOiIwMDBkMTc4OC0zMDAxLTQwZmMtYjZjNC0wOWI2N2I5N2JjNDUiLCJwcmVmaXgiOm51bGx9"
  }
  ```

  ```csharp C# theme={null}
  {
    "vectors": [
      {
        "id": "doc1#chunk1"
      },
      {
        "id": "doc1#chunk2"
      },
      {
        "id": "doc1#chunk3"
      }
    ],
    "pagination": "eyJza2lwX3Bhc3QiOiIwMDBkMTc4OC0zMDAxLTQwZmMtYjZjNC0wOWI2N2I5N2JjNDUiLCJwcmVmaXgiOm51bGx9",
    "namespace": "example-namespace",
    "usage": {
      "readUnits": 1
    }
  }
  ```

  ```json curl theme={null}
  {
    "vectors": [
      { "id": "doc1#chunk1" },
      { "id": "doc1#chunk2" },
      { "id": "doc1#chunk3" }
    ],
    "pagination": {
      "next": "c2Vjb25kY2FsbA=="
    },
    "namespace": "example-namespace",
    "usage": {
      "readUnits": 1
    }
  }
  ```
</ResponseExample>



# List namespaces
Source: https://docs.pinecone.io/reference/api/2025-04/data-plane/listnamespaces

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-04/db_data_2025-04.oas.yaml get /namespaces
List all namespaces in a serverless index.

Up to 100 namespaces are returned at a time by default, in sorted order (bitwise “C” collation). If the `limit` parameter is set, up to that number of namespaces are returned instead. Whenever there are additional namespaces to return, the response also includes a `pagination_token` that you can use to get the next batch of namespaces. When the response does not include a `pagination_token`, there are no more namespaces to return.

For guidance and examples, see [Manage namespaces](https://docs.pinecone.io/guides/manage-data/manage-namespaces).

**Note:** This operation is not supported for pod-based indexes.

<RequestExample>
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
  const index = pc.index("INDEX_NAME", "INDEX_HOST")

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
          ListNamespacesResponse listNamespacesResponseWithLimit = index.listNamespaces(null,2);

          // List all namespaces with pagination limit and token
          ListNamespacesResponse listNamespacesResponsePaginated = index.listNamespaces("eyJza2lwX3Bhc3QiOiIxMDEwMy0=", 5);

          System.out.println(restoreJobListWithLimit);
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

  ```bash curl theme={null}
  # To get the unique host for an index,
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="INDEX_HOST"

  curl "https://$INDEX_HOST/namespaces" \
      -H "Api-Key: $PINECONE_API_KEY" \
      -H "X-Pinecone-API-Version: 2025-04"
  ```
</RequestExample>

<ResponseExample>
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
      { name: 'example-namespace2', recordCount: '10500' }
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
</ResponseExample>



# Search with a vector
Source: https://docs.pinecone.io/reference/api/2025-04/data-plane/query

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-04/db_data_2025-04.oas.yaml post /query
Search a namespace using a query vector. It retrieves the ids of the most similar items in a namespace, along with their similarity scores.

For guidance, examples, and limits, see [Search](https://docs.pinecone.io/guides/search/search-overview).

<RequestExample>
  ```python Python theme={null}
  # pip install "pinecone[grpc]"
  from pinecone.grpc import PineconeGRPC as Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  # To get the unique host for an index, 
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  index = pc.Index(host="INDEX_HOST")

  index.query(
      namespace="example-namespace",
      vector=[0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3],
      filter={
          "genre": {"$eq": "documentary"}
      },
      top_k=3,
      include_values=True
  )
  ```

  ```javascript JavaScript theme={null}
  // npm install @pinecone-database/pinecone
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' })

  // To get the unique host for an index, 
  // see https://docs.pinecone.io/guides/manage-data/target-an-index
  const index = pc.index("INDEX_NAME", "INDEX_HOST")

  const queryResponse = await index.namespace('example-namespace').query({
      vector: [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3],
      filter: {
        'genre': {'$eq': 'documentary'}
      },
      topK: 3,
      includeValues: true
  });
  ```

  ```java Java theme={null}
  import com.google.protobuf.Struct;
  import com.google.protobuf.Value;
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
          List<Float> query = Arrays.asList(0.3f, 0.3f, 0.3f, 0.3f, 0.3f, 0.3f, 0.3f, 0.3f);
          Struct filter = Struct.newBuilder()
                  .putFields("genre", Value.newBuilder()
                          .setStructValue(Struct.newBuilder()
                                  .putFields("$eq", Value.newBuilder()
                                          .setStringValue("documentary")
                                          .build()))
                          .build())
                  .build();

          QueryResponseWithUnsignedIndices queryResponse = index.query(3, query, null, null, null, "example-namespace", filter, false, true);

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
      "google.golang.org/protobuf/types/known/structpb"
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

      queryVector := []float32{0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3}

      metadataMap := map[string]interface{}{
          "genre": map[string]interface{}{
              "$eq": "documentary",
          },
      }

      metadataFilter, err := structpb.NewStruct(metadataMap)
      if err != nil {
          log.Fatalf("Failed to create metadata map: %v", err)
      }

      res, err := idxConnection.QueryByVectorValues(ctx, &pinecone.QueryByVectorValuesRequest{
          Vector:         queryVector,
          TopK:           3,
          MetadataFilter: metadataFilter,
          IncludeValues:  true,
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
      Vector = new[] { 0.3f, 0.3f, 0.3f, 0.3f, 0.3f, 0.3f, 0.3f, 0.3f },
      Namespace = "example-namespace",
      TopK = 3,
      Filter = new Metadata
      {
          ["genre"] =
              new Metadata
              {
                  ["$eq"] = "documentary",
              }
      }
  });

  Console.WriteLine(queryResponse);
  ```

  ```shell curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="INDEX_HOST"

  curl "https://$INDEX_HOST/query" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -H "X-Pinecone-API-Version: 2025-04" \
    -d '{
      "namespace": "example-namespace",
      "vector": [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3],
      "filter": {"genre": {"$eq": "documentary"}},
      "topK": 3,
      "includeValues": true
    }'
  ```
</RequestExample>

<ResponseExample>
  ```shell  theme={null}
  {
    "matches":[
      {
        "id": "vec3",
        "score": 0,
        "values": [0.3,0.3,0.3,0.3,0.3,0.3,0.3,0.3]
      },
      {
        "id": "vec2",
        "score": 0.0800000429,
        "values": [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]
      },
      {
        "id": "vec4",
        "score": 0.0799999237,
        "values": [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4]
      }
    ],
    "namespace": "example-namespace",
    "usage": {"read_units": 6}
  }
  ```
</ResponseExample>



# Search with text
Source: https://docs.pinecone.io/reference/api/2025-04/data-plane/search_records

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-04/db_data_2025-04.oas.yaml post /records/namespaces/{namespace}/search
Search a namespace with a query text, query vector, or record ID and return the most similar records, along with their similarity scores. Optionally, rerank the initial results based on their relevance to the query. 

Searching with text is supported only for [indexes with integrated embedding](https://docs.pinecone.io/guides/indexes/create-an-index#integrated-embedding). Searching with a query vector or record ID is supported for all indexes. 

For guidance, examples, and limits, see [Search](https://docs.pinecone.io/guides/search/search-overview).

<RequestExample>
  ```python Python theme={null}
  from pinecone import Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  # To get the unique host for an index, 
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  index = pc.Index("docs-example")

  # Search with a query text and rerank the results
  # Supported only for indexes with integrated embedding
  search_with_text = index.search(
      namespace="example-namespace", 
      query={
          "inputs": {"text": "Disease prevention"}, 
          "top_k": 4
      },
      fields=["category", "chunk_text"],
      rerank={
          "model": "bge-reranker-v2-m3",
          "top_n": 2,
          "rank_fields": ["chunk_text"] # Specified field must also be included in 'fields'
      }
  )

  print(search_with_text)

  # Search with a query vector and rerank the results
  search_with_vector = index.search(
      namespace="example-namespace", 
      query={
          "vector": {
              "values": [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3]
          }, 
          "top_k": 4
      },
      fields=["category", "chunk_text"],
      rerank={
          "query": "Disease prevention",
          "model": "bge-reranker-v2-m3",
          "top_n": 2,
          "rank_fields": ["chunk_text"] # Specified field must also be included in 'fields'
      }
  )

  print(search_with_vector)

  # Search with a record ID and rerank the results
  search_with_id = index.search(
      namespace="example-namespace", 
      query={
          "id": "rec1", 
          "top_k": 4
      },
      fields=["category", "chunk_text"],
      rerank={
          "query": "Disease prevention",
          "model": "bge-reranker-v2-m3",
          "top_n": 2,
          "rank_fields": ["chunk_text"] # Specified field must also be included in 'fields'
      }
  )

  print(search_with_id)
  ```

  ```javascript JavaScript theme={null}
  // npm install @pinecone-database/pinecone
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({ apiKey: "YOUR_API_KEY" })

  // To get the unique host for an index, 
  // see https://docs.pinecone.io/guides/manage-data/target-an-index
  const namespace = pc.index("INDEX_NAME", "INDEX_HOST").namespace("example-namespace");

  // Search with a query text and rerank the results
  // Supported only for indexes with integrated embedding
  const searchWithText = await namespace.searchRecords({
    query: {
      topK: 4,
      inputs: { text: 'Disease prevention' },
    },
    fields: ['chunk_text', 'category'],
    rerank: {
      model: 'bge-reranker-v2-m3',
      rankFields: ['chunk_text'],
      topN: 2,
    },
  });

  console.log(searchWithText);

  // Search with a query vector and rerank the results
  const searchWithVector = await namespace.searchRecords({
    query: {
      topK: 4,
      vector: {
        values: [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3]
      },
      inputs: { text: 'Disease prevention' },
    },
    fields: ['chunk_text', 'category'],
    rerank: {
      query: "Disease prevention",
      model: 'bge-reranker-v2-m3',
      rankFields: ['chunk_text'],
      topN: 2,
    },
  });

  console.log(searchWithVector);

  // Search with a record ID and rerank the results
  const searchWithId = await namespace.searchRecords({
    query: {
      topK: 4,
      id: 'rec1',
    },
    fields: ['chunk_text', 'category'],
    rerank: {
      query: "Disease prevention",
      model: 'bge-reranker-v2-m3',
      rankFields: ['chunk_text'],
      topN: 2,
    },
  });

  console.log(searchWithId);
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Index;
  import io.pinecone.configs.PineconeConfig;
  import io.pinecone.configs.PineconeConnection;
  import org.openapitools.db_data.client.ApiException;
  import org.openapitools.db_data.client.model.SearchRecordsRequestRerank;
  import org.openapitools.db_data.client.model.SearchRecordsResponse;
  import org.openapitools.db_data.client.model.SearchRecordsVector;

  import java.util.*;

  public class SearchText {
      public static void main(String[] args) throws ApiException {
          PineconeConfig config = new PineconeConfig("YOUR_API_KEY");
          config.setHost("INDEX_HOST");
          PineconeConnection connection = new PineconeConnection(config);

          Index index = new Index(config, connection, "integrated-dense-java");

          String query = "Famous historical structures and monuments";
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

          // Search with a query text and rerank the results
          // Supported only for indexes with integrated embedding
          SearchRecordsResponse searchWithText = index.searchRecordsByText(query,  "example-namespace", fields, 10, null, rerank);

          System.out.println(searchWithText);

          // Search with a query vector and rerank the results
          SearchRecordsVector queryVector = new SearchRecordsVector();
          queryVector.setValues(Arrays.asList(0.3f, 0.3f, 0.3f, 0.3f, 0.3f, 0.3f, 0.3f, 0.3f));
          SearchRecordsResponse searchWithVector = index.searchRecordsByVector(queryVector, "example-namespace", fields, 4, null, rerank);
          
          System.out.println(searchWithVector);

          // Search with a record ID and rerank the results
          SearchRecordsResponse searchWithID = index.searchRecordsById("rec1", "example-namespace", fields, 4, null, rerank);

          System.out.println(searchWithID);
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

      // Search with a query text and rerank the results
      // Supported only for indexes with integrated embedding
      topN := int32(2)
      searchWithText, err := idxConnection.SearchRecords(ctx, &pinecone.SearchRecordsRequest{
          Query: pinecone.SearchRecordsQuery{
              TopK: 4,
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
      fmt.Printf(prettifyStruct(searchWithText))

      // Search with a query vector and rerank the results
      topN := int32(2)
      searchWithVector, err := idxConnection.SearchRecords(ctx, &pinecone.SearchRecordsRequest{
          Query: pinecone.SearchRecordsQuery{
              TopK: 4,
              Vector: pinecone.SearchRecordsVector{
                  Values: []float32{0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3},
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
      fmt.Printf(prettifyStruct(resSearchWithVector))

      // Search with a query ID and rerank the results
      topN := int32(2)
      searchWithId, err := idxConnection.SearchRecords(ctx, &pinecone.SearchRecordsRequest{
          Query: pinecone.SearchRecordsQuery{
              TopK: 4,
              Id: "rec1",
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
      fmt.Printf(prettifyStruct(searchWithId))
  }
  ```

  ```csharp C# theme={null}
  using Pinecone;

  var pinecone = new PineconeClient("YOUR_API_KEY");

  var index = pinecone.Index(host: "INDEX_HOST");

  // Search with a query text and rerank the results
  var searchWithText = await index.SearchRecordsAsync(
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
          },
      }
  );

  Console.WriteLine(searchWithText);

  // Search with a query vector and rerank the results
  var searchWithVector = await index.SearchRecordsAsync(
      "example-namespace",
      new SearchRecordsRequest
      {
          Query = new SearchRecordsRequestQuery
          {
              TopK = 4,
              Vector = new SearchRecordsVector
              {
                  Values = new float[] { 0.3f, 0.3f, 0.3f, 0.3f, 0.3f, 0.3f, 0.3f, 0.3f },
              },
          },
          Fields = ["category", "chunk_text"],
          Rerank = new SearchRecordsRequestRerank
          {
              Model = "bge-reranker-v2-m3",
              TopN = 2,
              RankFields = ["chunk_text"],
          },
      }
  );

  Console.WriteLine(searchWithVector);

  // Search with a query ID and rerank the results
  var searchWithId = await index.SearchRecordsAsync(
      "example-namespace",
      new SearchRecordsRequest
      {
          Query = new SearchRecordsRequestQuery
          {
              TopK = 4,
              Id = "rec1",
          },
          Fields = ["category", "chunk_text"],
          Rerank = new SearchRecordsRequestRerank
          {
              Model = "bge-reranker-v2-m3",
              TopN = 2,
              RankFields = ["chunk_text"],
          },
      }
  );

  Console.WriteLine(searchWithId);
  ```

  ```shell curl theme={null}
  INDEX_HOST="INDEX_HOST"
  NAMESPACE="YOUR_NAMESPACE"
  PINECONE_API_KEY="YOUR_API_KEY"

  # Search with a query text and rerank the results
  # Supported only for indexes with integrated embedding
  curl "https://$INDEX_HOST/records/namespaces/$NAMESPACE/search" \
    -H "Accept: application/json" \
    -H "Content-Type: application/json" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-API-Version: 2025-01" \
    -d '{
          "query": {
              "inputs": {"text": "Disease prevention"},
              "top_k": 4,
          },
          "fields": ["category", "chunk_text"]
          "rerank": {
              "model": "bge-reranker-v2-m3",
              "top_n": 2,
              "rank_fields": ["chunk_text"] # Specified field must also be included in 'fields'
          }
       }'

  # Search with a query vector and rerank the results
  curl "https://$INDEX_HOST/records/namespaces/$NAMESPACE/search" \
    -H "Accept: application/json" \
    -H "Content-Type: application/json" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-API-Version: 2025-01" \
    -d '{
          "query": {
              "vector": {
                  "values": [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3]
              },
              "top_k": 4,
          },
          "fields": ["category", "chunk_text"]
          "rerank": {
              "query": "Disease prevention",
              "model": "bge-reranker-v2-m3",
              "top_n": 2,
              "rank_fields": ["chunk_text"] # Specified field must also be included in 'fields'
          }
       }'

  # Search with a record ID and rerank the results
  # Supported only for indexes with integrated embedding
  curl "https://$INDEX_HOST/records/namespaces/$NAMESPACE/search" \
    -H "Accept: application/json" \
    -H "Content-Type: application/json" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-API-Version: 2025-01" \
    -d '{
          "query": {
              "id": "rec1",
              "top_k": 4,
          },
          "fields": ["category", "chunk_text"]
          "rerank": {
              "query": "Disease prevention",
              "model": "bge-reranker-v2-m3",
              "top_n": 2,
              "rank_fields": ["chunk_text"]
          }
       }'
  ```
</RequestExample>

<ResponseExample>
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
          "_score": 0.004399413242936134,
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
</ResponseExample>



# Update a vector
Source: https://docs.pinecone.io/reference/api/2025-04/data-plane/update

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-04/db_data_2025-04.oas.yaml post /vectors/update
Update a vector in a namespace. If a value is included, it will overwrite the previous value. If a `set_metadata` is included, the values of the fields specified in it will be added or overwrite the previous value.

For guidance and examples, see [Update data](https://docs.pinecone.io/guides/manage-data/update-data).

<RequestExample>
  ```python Python theme={null}
  # pip install "pinecone[grpc]"
  from pinecone.grpc import PineconeGRPC as Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  # To get the unique host for an index, 
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  index = pc.Index(host="INDEX_HOST")

  index.update(
  	id="id-3", 
  	values=[4.0, 2.0], 
  	set_metadata={"genre": "comedy"},
  	namespace="example-namespace"
  )
  ```

  ```javascript JavaScript theme={null}
  // npm install @pinecone-database/pinecone
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({ apiKey: "YOUR_API_KEY" })

  // To get the unique host for an index, 
  // see https://docs.pinecone.io/guides/manage-data/target-an-index
  const index = pc.index("INDEX_NAME", "INDEX_HOST")

  await index.namespace('example-namespace').update({
    id: 'id-3',
    values: [4.0, 2.0],
    metadata: {
      genre: "comedy",
    },
  });
  ```

  ```java Java theme={null}
  import com.google.protobuf.Struct;
  import com.google.protobuf.Value;
  import io.pinecone.clients.Index;
  import io.pinecone.configs.PineconeConfig;
  import io.pinecone.configs.PineconeConnection;
  import io.pinecone.proto.UpdateResponse;

  import java.util.Arrays;
  import java.util.List;

  public class UpdateExample {
      public static void main(String[] args) {
          PineconeConfig config = new PineconeConfig("YOUR_API_KEY");
          // To get the unique host for an index, 
          // see https://docs.pinecone.io/guides/manage-data/target-an-index
          config.setHost("INDEX_HOST");
          PineconeConnection connection = new PineconeConnection(config);
          Index index = new Index(connection, "INDEX_NAME");
          List<Float> values = Arrays.asList(4.0f, 2.0f);
  		Struct metaData = Struct.newBuilder()
  			.putFields("genre",
  					Value.newBuilder().setStringValue("comedy").build())
  			.build();
          UpdateResponse updateResponse = index.update("id-3", values, metaData, "example-namespace", null, null);
          System.out.println(updateResponse);
      }
  }
  ```

  ```go Go theme={null}
  package main

  import (
      "context"
      "log"

      "github.com/pinecone-io/go-pinecone/v4/pinecone"
      "google.golang.org/protobuf/types/known/structpb"
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
      idxConnection, err := pc.Index(pinecone.NewIndexConnParams{Host: "INDEX_HOST", Namespace: "example-namespace"})
      if err != nil {
          log.Fatalf("Failed to create IndexConnection for Host: %v", err)
    	}

      id := "id-3"

      metadataMap := map[string]interface{}{
          "genre": "comedy",
      }

      metadataFilter, err := structpb.NewStruct(metadataMap)
      if err != nil {
          log.Fatalf("Failed to create metadata map: %v", err)
      }

      err = idxConnection.UpdateVector(ctx, &pinecone.UpdateVectorRequest{
          Id:       id,
          Metadata: metadataFilter,
      })
      if err != nil {
          log.Fatalf("Failed to update vector with ID %v: %v", id, err)
      }
  }
  ```

  ```csharp C# theme={null}
  using Pinecone;

  var pinecone = new PineconeClient("YOUR_API_KEY");

  // To get the unique host for an index, 
  // see https://docs.pinecone.io/guides/manage-data/target-an-index
  var index = pinecone.Index(host: "INDEX_HOST");

  var updateResponse = await index.UpdateAsync(new UpdateRequest {
      Id = "id-3",
      Values = new[] { 4.0f, 2.0f },
      SetMetadata = new Metadata { ["genre"] = "comedy" },
      Namespace = "example-namespace",
  });
  ```

  ```shell curl theme={null}
  # To get the unique host for an index,
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="INDEX_HOST"

  curl "https://$INDEX_HOST/vectors/update" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -H "X-Pinecone-API-Version: 2025-04" \
    -d '{
          "id": "id-3",
          "values": [4.0, 2.0],
          "setMetadata": {"type": "comedy"},
          "namespace": "example-namespace"
        }'
  ```
</RequestExample>

<ResponseExample>
  ```json  theme={null}
  {}
  ```
</ResponseExample>



# Upsert vectors
Source: https://docs.pinecone.io/reference/api/2025-04/data-plane/upsert

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-04/db_data_2025-04.oas.yaml post /vectors/upsert
Upsert vectors into a namespace. If a new value is upserted for an existing vector ID, it will overwrite the previous value.

For guidance, examples, and limits, see [Upsert data](https://docs.pinecone.io/guides/index-data/upsert-data).

<Tip>
  To control costs when ingesting large datasets (10,000,000+ records), use [import](/guides/index-data/import-data) instead of upsert.
</Tip>

<RequestExample>
  ```python Python theme={null}
  # pip install "pinecone[grpc]"
  from pinecone.grpc import PineconeGRPC as Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  # To get the unique host for an index, 
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  index = pc.Index(host="INDEX_HOST")

  index.upsert(
    vectors=[
      {
        "id": "vec1", 
        "values": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1], 
        "metadata": {"genre": "comedy", "year": 2020}
      },
      {
        "id": "vec2", 
        "values": [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2],
        "metadata": {"genre": "documentary", "year": 2019}
      }
    ],
    namespace="example-namespace"
  )
  ```

  ```javascript JavaScript theme={null}
  // npm install @pinecone-database/pinecone
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({ apiKey: "YOUR_API_KEY" })

  // To get the unique host for an index, 
  // see https://docs.pinecone.io/guides/manage-data/target-an-index
  const index = pc.index("INDEX_NAME", "INDEX_HOST")

  const records = [
      {
        id: 'vec1',
        values: [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1],
        metadata: { genre: "comedy", year: 2020 },
      },
      {
        id: 'vec2',
        values: [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2],
        metadata: { genre: "documentary", year: 2019 },
      }
  ]

  await index.('example-namespace').upsert(records);
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

      // To get the unique host for an index, 
      // see https://docs.pinecone.io/guides/manage-data/target-an-index
      idxConnection, err := pc.Index(pinecone.NewIndexConnParams{Host: "INDEX_HOST", Namespace: "example-namespace"})
      if err != nil {
          log.Fatalf("Failed to create IndexConnection for Host: %v", err)
  	  }

      // Upsert records into a namespace
      // `chunk_text` fields are converted to sparse vectors
      // `category` and `quarter` fields are stored as metadata
  	records := []*pinecone.IntegratedRecord{
  		{
  			"_id":        "vec1",
  			"chunk_text": "AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones.",
  			"category":   "technology",
  			"quarter":    "Q3",
  		},
  		{
  			"_id":        "vec2",
  			"chunk_text": "Analysts suggest that AAPL's upcoming Q4 product launch event might solidify its position in the premium smartphone market.",
  			"category":   "technology",
  			"quarter":    "Q4",
  		},
  		{
  			"_id":        "vec3",
  			"chunk_text": "AAPL's strategic Q3 partnerships with semiconductor suppliers could mitigate component risks and stabilize iPhone production.",
  			"category":   "technology",
  			"quarter":    "Q3",
  		},
  		{
  			"_id":        "vec4",
  			"chunk_text": "AAPL may consider healthcare integrations in Q4 to compete with tech rivals entering the consumer wellness space.",
  			"category":   "technology",
  			"quarter":    "Q4",
  		},
  	}

  	err = idxConnection.UpsertRecords(ctx, records)
  	if err != nil {
  		log.Fatalf("Failed to upsert vectors: %v", err)
  	}
  }
  ```

  ```java Java theme={null}
  import com.google.protobuf.Struct;
  import com.google.protobuf.Value;
  import io.pinecone.clients.Index;
  import io.pinecone.configs.PineconeConfig;
  import io.pinecone.configs.PineconeConnection;

  import java.util.Arrays;
  import java.util.List;

  public class UpsertExample {
      public static void main(String[] args) {
          PineconeConfig config = new PineconeConfig("YOUR_API_KEY");
          // To get the unique host for an index, 
          // see https://docs.pinecone.io/guides/manage-data/target-an-index
          config.setHost("INDEX_HOST");
          PineconeConnection connection = new PineconeConnection(config);
          Index index = new Index(connection, "INDEX_NAME");
          List<Float> values1 = Arrays.asList(0.1f, 0.1f, 0.1f, 0.1f, 0.1f, 0.1f, 0.1f, 0.1f);
          List<Float> values2 = Arrays.asList(0.2f, 0.2f, 0.2f, 0.2f, 0.2f, 0.2f, 0.2f, 0.2f);
          Struct metaData1 = Struct.newBuilder()
                  .putFields("genre", Value.newBuilder().setStringValue("comedy").build())
                  .putFields("year", Value.newBuilder().setNumberValue(2020).build())
                  .build();
          Struct metaData2 = Struct.newBuilder()
                  .putFields("genre", Value.newBuilder().setStringValue("documentary").build())
                  .putFields("year", Value.newBuilder().setNumberValue(2019).build())
                  .build();

          index.upsert("vec1", values1, null, null, metaData1, 'example-namespace');
          index.upsert("vec2", values2, null, null, metaData2, 'example-namespace');
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
      "google.golang.org/protobuf/types/known/structpb"
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
      idxConnection, err := pc.Index(pinecone.NewIndexConnParams{Host: "INDEX_HOST", Namespace: "example-namespace"})
      if err != nil {
          log.Fatalf("Failed to create IndexConnection for Host: %v", err)
  	  }

      metadataMap1 := map[string]interface{}{
          "genre": "comedy",
          "year": 2020,
      }

      metadata1, err := structpb.NewStruct(metadataMap1)
      if err != nil {
          log.Fatalf("Failed to create metadata map: %v", err)
      }

      metadataMap2 := map[string]interface{}{
          "genre": "documentary",
          "year": 2019,
      }

      metadata2, err := structpb.NewStruct(metadataMap2)
      if err != nil {
          log.Fatalf("Failed to create metadata map: %v", err)
      }

      vectors := []*pinecone.Vector{
          {
              Id:     "vec1",
              Values: []float32{0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1},
              Metadata: metadata1,
          },
          {
              Id:     "vec2",
              Values: []float32{0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2},
              Metadata: metadata2,
          },
      }

      count, err := idxConnection.UpsertVectors(ctx, vectors)
      if err != nil {
          log.Fatalf("Failed to upsert vectors: %v", err)
      } else {
          fmt.Printf("Successfully upserted %d vector(s)!\n", count)
      }
  }
  ```

  ```csharp C# theme={null}
  using Pinecone;

  var pinecone = new PineconeClient("YOUR_API_KEY");

  // To get the unique host for an index, 
  // see https://docs.pinecone.io/guides/manage-data/target-an-index
  var index = pinecone.Index(host: "INDEX_HOST");

  var upsertResponse = await index.UpsertAsync(new UpsertRequest {
      Vectors = new[]
      {
          new Vector
          {
              Id = "vec1",
              Values = new[] { 0.1f, 0.1f, 0.1f, 0.1f, 0.1f, 0.1f, 0.1f, 0.1f },
              Metadata = new Metadata {
                  ["genre"] = new("comedy"),
                  ["year"] = new(2020),
              },
          },
          new Vector
          {
              Id = "vec2",
              Values = new[] { 0.2f, 0.2f, 0.2f, 0.2f, 0.2f, 0.2f, 0.2f, 0.2f },
              Metadata = new Metadata {
                  ["genre"] = new("documentary"),
                  ["year"] = new(2019),
              },
          }
      },
      Namespace = "example-namespace",
  });
  ```

  ```shell curl theme={null}
  # To get the unique host for an index,
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="INDEX_HOST"

  curl "https://$INDEX_HOST/vectors/upsert" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H 'Content-Type: application/json' \
    -H "X-Pinecone-API-Version: 2025-04" \
    -d '{
      "vectors": [
        {
          "id": "vec1",
          "values": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1],
          "metadata": {"genre": "comedy", "year": 2020}
        },
        {
          "id": "vec2",
          "values": [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2],
          "metadata": {"genre": "documentary", "year": 2019}
        }
      ],
      "namespace": "example-namespace"
    }'
  ```
</RequestExample>

<ResponseExample>
  ```json  theme={null}
  {"upsertedCount":2}
  ```
</ResponseExample>



---
**Navigation:** [← Previous](./15-search-overview.md) | [Index](./index.md) | [Next →](./17-upsert-text.md)
