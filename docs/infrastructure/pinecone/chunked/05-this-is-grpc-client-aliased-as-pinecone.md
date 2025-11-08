**Navigation:** [← Previous](./04-indexing-overview.md) | [Index](./index.md) | [Next →](./06-restore-a-pod-based-index.md)

# This is gRPC client aliased as "Pinecone"
pc = Pinecone(api_key='YOUR_API_KEY')  


# To get the unique host for an index, 

# see https://docs.pinecone.io/guides/manage-data/target-an-index
index = pc.Index(host="INDEX_HOST")
```

To launch multiple read and write requests in parallel, pass `async_req` to the `upsert` operation:

```Python Python theme={null}
def chunker(seq, batch_size):
  return (seq[pos:pos + batch_size] for pos in range(0, len(seq), batch_size))

async_results = [
  index.upsert(vectors=chunk, async_req=True)
  for chunk in chunker(data, batch_size=200)
]


# Wait for and retrieve responses (in case of error)
[async_result.result() for async_result in async_results]
```

<Note>
  It is possible to get write-throttled faster when upserting using the gRPC SDK. If you see this often, [implement retry logic with exponential backoff](/guides/production/error-handling#implement-retry-logic) while upserting.

  The syntax for upsert, query, fetch, and delete with the gRPC SDK remain the same as the standard SDK.
</Note>


## Upsert limits

| Metric                                                             | Limit                                                         |
| :----------------------------------------------------------------- | :------------------------------------------------------------ |
| Max [batch size](/guides/index-data/upsert-data#upsert-in-batches) | 2 MB or 1000 records with vectors <br /> 96 records with text |
| Max metadata size per record                                       | 40 KB                                                         |
| Max length for a record ID                                         | 512 characters                                                |
| Max dimensionality for dense vectors                               | 20,000                                                        |
| Max non-zero values for sparse vectors                             | 2048                                                          |
| Max dimensionality for sparse vectors                              | 4.2 billion                                                   |



# Back up a pod-based index
Source: https://docs.pinecone.io/guides/indexes/pods/back-up-a-pod-based-index

Backup pod-based indexes using Pinecone collections

<Warning>
  Customers who sign up for a Standard or Enterprise plan on or after August 18, 2025 cannot create pod-based indexes. Instead, create [serverless indexes](/guides/index-data/create-an-index), and consider using [dedicated read nodes](/guides/index-data/dedicated-read-nodes) for large workloads (millions of records or more, and moderate or high query rates).
</Warning>

This page describes how to create a static copy of a pod-based index, also known as a [collection](/guides/indexes/pods/understanding-collections).


## Create a collection

To create a backup of your pod-based index, use the [`create_collection`](/reference/api/latest/control-plane/create_collection) operation.

The following example creates a [collection](/guides/indexes/pods/understanding-collections) named `example-collection` from an index named `docs-example`:

<CodeGroup>
  ```python Python theme={null}
  # pip install "pinecone[grpc]"
  from pinecone.grpc import PineconeGRPC as Pinecone

  pc = Pinecone(api_key="API_KEY")
  pc.create_collection("example-collection", "docs-example")
  ```

  ```javascript JavaScript theme={null}
  // npm install @pinecone-database/pinecone
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({
    apiKey: 'YOUR_API_KEY'
  });

  await pc.createCollection({
    name: "example-collection",
    source: "docs-example",
  });
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Pinecone;

  public class CreateCollectionExample {
      public static void main(String[] args) {
          Pinecone pc = new Pinecone.Builder("YOUR_API_KEY").build();

          pc.createCollection("example-collection", "docs-example");
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

      collection, err := pc.CreateCollection(ctx, &pinecone.CreateCollectionRequest{
          Name: "example-collection", 
          Source: "docs-example",
      })
      if err != nil {
          log.Fatalf("Failed to create collection: %v", err)
      } else {
          fmt.Printf("Successfully created collection: %v", collection.Name)
      }
  }
  ```

  ```csharp C# theme={null}
  using Pinecone;

  var pinecone = new PineconeClient("YOUR_API_KEY");

  var collectionModel = await pinecone.CreateCollectionAsync(new CreateCollectionRequest {
      Name = "example-collection",
      Source = "docs-example",
  });
  ```

  ```shell curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl -s POST "https://api.pinecone.io/collections" \
    -H "Accept: application/json" \
    -H "Content-Type: application/json" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-API-Version: 2025-04" \
    -d '{
          "name": "example-collection",
          "source": "docs-example"
    }'
  ```
</CodeGroup>

<Tip>
  You can create a collection using the [Pinecone console](https://app.pinecone.io/organizations/-/projects/-/backups).
</Tip>


## Check the status of a collection

To retrieve the status of the process creating a collection and the size of the collection, use the [`describe_collection`](/reference/api/latest/control-plane/describe_collection) operation. Specify the name of the collection to check. You can only call `describe_collection` on a collection in the current project.

The `describe_collection` operation returns an object containing key-value pairs representing the name of the collection, the size in bytes, and the creation status of the collection.

The following example gets the creation status and size of a collection named `example-collection`.

<CodeGroup>
  ```python Python theme={null}
  # pip install "pinecone[grpc]"
  from pinecone.grpc import PineconeGRPC as Pinecone

  pc = Pinecone(api_key='API_KEY')
  pc.describe_collection(name="example-collection")
  ```

  ```javascript JavaScript theme={null}
  // npm install @pinecone-database/pinecone
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  await pc.describeCollection('example-collection');
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Pinecone;
  import org.openapitools.client.model.CollectionModel;

  public class DescribeCollectionExample {
      public static void main(String[] args) {
          Pinecone pc = new Pinecone.Builder("YOUR_API_KEY").build();
          CollectionModel collectionModel = pc.describeCollection("example-collection");
          System.out.println(collectionModel);
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

      collectionName := "example-collection"

      collection, err := pc.DescribeCollection(ctx, collectionName)
      if err != nil {
          log.Fatalf("Error describing collection %v: %v", collectionName, err)
      } else {
          fmt.Printf("Collection: %+v", collection)
      }
  }
  ```

  ```csharp C# theme={null}
  using Pinecone;

  var pinecone = new PineconeClient("YOUR_API_KEY");

  var collectionModel = await pinecone.DescribeCollectionAsync("example-collection");

  Console.WriteLine(collectionModel);
  ```

  ```shell curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl -i -X GET "https://api.pinecone.io/collections/example-collection" \
      -H "Api-Key: $PINECONE_API_KEY" \
      -H "X-Pinecone-API-Version: 2025-04"
  ```
</CodeGroup>

<Tip>
  You can check the status of a collection using the [Pinecone console](https://app.pinecone.io/organizations/-/projects/-/backups).
</Tip>


## List your collections

To get a list of the collections in the current project, use the [`list_collections`](/reference/api/latest/control-plane/list_collections) operation.

<CodeGroup>
  ```python Python theme={null}
  from pinecone.grpc import PineconeGRPC as Pinecone

  pc = Pinecone(api_key='API_KEY')
  pc.list_collections()
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' })

  await pc.listCollections();
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Pinecone;
  import org.openapitools.client.model.CollectionModel;

  public class ListCollectionsExample {
      public static void main(String[] args) {
          Pinecone pc = new Pinecone.Builder("YOUR_API_KEY").build();
          List<CollectionModel> collectionList = pc.listCollections().getCollections();
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

      collections, err := pc.ListCollections(ctx)
      if err != nil {
  	    log.Fatalf("Failed to list collections: %v", err)
      } else {
          if len(collections) == 0 {
              fmt.Printf("No collections found in project")
          } else {
              for _, collection := range collections {
                  fmt.Printf("collection: %v\n", prettifyStruct(collection))
              }
          }
      }
  }
  ```

  ```csharp C# theme={null}
  using Pinecone;

  var pinecone = new PineconeClient("YOUR_API_KEY");

  var collectionList = await pinecone.ListCollectionsAsync();

  Console.WriteLine(collectionList);
  ```

  ```shell curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl -i -X GET "https://api.pinecone.io/collections" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-API-Version: 2025-04"
  ```

  <Tip>
    You can view a list of your collections using the [Pinecone console](https://app.pinecone.io/organizations/-/projects/-/backups).
  </Tip>
</CodeGroup>

<Tip>
  You can view a list of your collections using the [Pinecone console](https://app.pinecone.io/organizations/-/projects/-/backups).
</Tip>


## Delete a collection

To delete a collection, use the [`delete_collection`](/reference/api/latest/control-plane/delete_collection) operation. Specify the name of the collection to delete.

Deleting the collection takes several minutes. During this time, the [`describe_collection`](#check-the-status-of-a-collection) operation returns the status "deleting".

<CodeGroup>
  ```python Python theme={null}
  # pip install "pinecone[grpc]"
  from pinecone.grpc import PineconeGRPC as Pinecone

  pc = Pinecone(api_key='API_KEY')
  pc.delete_collection("example-collection")
  ```

  ```javascript JavaScript theme={null}
  // npm install @pinecone-database/pinecone
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' })

  await pc.deleteCollection("example-collection");
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Pinecone;

  public class DeleteCollectionExample {
      public static void main(String[] args) {
          Pinecone pc = new Pinecone.Builder("YOUR_API_KEY").build();
          pc.deleteCollection("example-collection");
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

      collectionName := "example-collection"

      err = pc.DeleteCollection(ctx, collectionName)
      if err != nil {
  	    log.Fatalf("Failed to delete collection: %v\n", err)
      } else {
          if len(collections) == 0 {
              fmt.Printf("No collections found in project")
          } else {
              fmt.Printf("Successfully deleted collection \"%v\"\n", collectionName)
          }
      }
  }
  ```

  ```csharp C# theme={null}
  using Pinecone;

  var pinecone = new PineconeClient("YOUR_API_KEY");

  await pinecone.DeleteCollectionAsync("example-collection");
  ```

  ```shell curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl -i -X DELETE "https://api.pinecone.io/collections/example-collection" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-API-Version: 2025-04"
  ```
</CodeGroup>

<Tip>
  You can delete a collection using the [Pinecone console](https://app.pinecone.io/organizations/-/projects/-/backups).
</Tip>



# Choose a pod type and size
Source: https://docs.pinecone.io/guides/indexes/pods/choose-a-pod-type-and-size

Select the right pod configuration for your workload

<Warning>
  Customers who sign up for a Standard or Enterprise plan on or after August 18, 2025 cannot create pod-based indexes. Instead, create [serverless indexes](/guides/index-data/create-an-index), and consider using [dedicated read nodes](/guides/index-data/dedicated-read-nodes) for large workloads (millions of records or more, and moderate or high query rates).
</Warning>

When planning your Pinecone deployment, it is important to understand the approximate storage requirements of your vectors to choose the appropriate pod type and number. This page will give guidance on sizing to help you plan accordingly.

As with all guidelines, these considerations are general and may not apply to your specific use case. We caution you to always test your deployment and ensure that the index configuration you are using is appropriate to your requirements.

[Collections](/guides/indexes/pods/understanding-collections) allow you to create new versions of your index with different pod types and sizes. This also allows you to test different configurations. This guide is merely an overview of sizing considerations; test your index configuration before moving to production.

<Tip>
  Users on Standard and Enterprise plans can [contact Support](https://app.pinecone.io/organizations/-/settings/support/ticket) for further help with sizing and testing.
</Tip>


## Overview

There are five main considerations when deciding how to configure your Pinecone index:

* Number of vectors
* Dimensionality of your vectors
* Size of metadata on each vector
* Queries per second (QPS) throughput
* Cardinality of indexed metadata

Each of these considerations comes with requirements for index size, pod type, and replication strategy.

### Number of vectors

The most important consideration in sizing is the [number of vectors](/guides/index-data/upsert-data) you plan on working with. As a rule of thumb, a single p1 pod can store approximately 1M vectors, while a s1 pod can store 5M vectors. However, this can be affected by other factors, such as dimensionality and metadata, which are explained below.

### Dimensionality of vectors

The rules of thumb above for how many vectors can be stored in a given pod assumes a typical configuration of 768 [dimensions per vector](/guides/index-data/create-an-index). As your individual use case will dictate the dimensionality of your vectors, the amount of space required to store them may necessarily be larger or smaller.

Each dimension on a single vector consumes 4 bytes of memory and storage per dimension, so if you expect to have 1M vectors with 768 dimensions each, that’s about 3GB of storage without factoring in metadata or other overhead. Using that reference, we can estimate the typical pod size and number needed for a given index. Table 1 below gives some examples of this.

**Table 1: Estimated number of pods per 1M vectors by dimensionality**

| Pod type | Dimensions | Estimated max vectors per pod |
| -------- | ---------: | ----------------------------: |
| **p1**   |        512 |                     1,250,000 |
|          |        768 |                     1,000,000 |
|          |       1024 |                       675,000 |
|          |       1536 |                       500,000 |
| **p2**   |        512 |                     1,250,000 |
|          |        768 |                     1,100,000 |
|          |       1024 |                     1,000,000 |
|          |       1536 |                       550,000 |
| **s1**   |        512 |                     8,000,000 |
|          |        768 |                     5,000,000 |
|          |       1024 |                     4,000,000 |
|          |       1536 |                     2,500,000 |

Pinecone does not support fractional pod deployments, so always round up to the next nearest whole number when choosing your pods.


## Queries per second (QPS)

QPS speeds are governed by a combination of the [pod type](/guides/indexes/pods/understanding-pod-based-indexes#pod-types) of the index, the number of [replicas](/guides/indexes/pods/scale-pod-based-indexes#add-replicas), and the `top_k` value of queries. The pod type is the primary factor driving QPS, as the different pod types are optimized for different approaches.

The [p1 pods](/guides/index-data/indexing-overview/#p1-pods) are performance-optimized pods which provide very low query latencies, but hold fewer vectors per pod than [s1 pods](/guides/index-data/indexing-overview/#s1-pods). They are ideal for applications with low latency requirements (\<100ms). The s1 pods are optimized for storage and provide large storage capacity and lower overall costs with slightly higher query latencies than p1 pods. They are ideal for very large indexes with moderate or relaxed latency requirements.

The [p2 pod type](/guides/index-data/indexing-overview/#p2-pods) provides greater query throughput with lower latency. They support 200 QPS per replica and return queries in less than 10ms. This means that query throughput and latency are better than s1 and p1, especially for low dimension vectors (\<512D).

As a rule, a single p1 pod with 1M vectors of 768 dimensions each and no replicas can handle about 20 QPS. It’s possible to get greater or lesser speeds, depending on the size of your metadata, number of vectors, the dimensionality of your vectors, and the `top_K` value for your search. See Table 2 below for more examples.

**Table 2: QPS by pod type and `top_k` value**\*

| Pod type | top\_k 10 | top\_k 250 | top\_k 1000 |
| -------- | --------- | ---------- | ----------- |
| p1       | 30        | 25         | 20          |
| p2       | 150       | 50         | 20          |
| s1       | 10        | 10         | 10          |

\*The QPS values in Table 2 represent baseline QPS with 1M vectors and 768 dimensions.

[Adding replicas](/guides/indexes/pods/scale-pod-based-indexes#add-replicas) is the simplest way to increase your QPS. Each replica increases the throughput potential by roughly the same QPS, so aiming for 150 QPS using p1 pods means using the primary pod and 5 replicas. Using threading or multiprocessing in your application is also important, as issuing single queries sequentially still subjects you to delays from any underlying latency. The [Pinecone gRPC SDK](/guides/index-data/upsert-data#grpc-python-sdk) can also be used to increase throughput of upserts.

### Metadata cardinality and size

The last consideration when planning your indexes is the cardinality and size of your [metadata](/guides/index-data/upsert-data#inserting-vectors-with-metadata). While the increases are small when talking about a few million vectors, they can have a real impact as you grow to hundreds of millions or billions of vectors.

Indexes with very high cardinality, like those storing a unique user ID on each vector, can have significant memory requirements, resulting in fewer vectors fitting per pod. Also, if the size of the metadata per vector is larger, the index requires more storage. Limiting which metadata fields are indexed using [selective metadata indexing](/guides/indexes/pods/manage-pod-based-indexes#selective-metadata-indexing) can help lower memory usage.

### Pod sizes

You can also start with one of the larger [pod sizes](/guides/index-data/indexing-overview/#pod-size-and-performance), like p1.x2. Each step up in pod size doubles the space available for your vectors. We recommend starting with x1 pods and scaling as you grow. This way, you don’t start with too large a pod size and have nowhere else to go up, meaning you have to migrate to a new index before you’re ready.

### Example applications

The following examples will showcase how to use the sizing guidelines above to choose the appropriate type, size, and number of pods for your index.

#### Example 1: Semantic search of news articles

In our first example, we’ll use the demo app for semantic search from our documentation. In this case, we’re only working with 204,135 vectors. The vectors use 300 dimensions each, well under the general measure of 768 dimensions. Using the rule of thumb above of up to 1M vectors per p1 pod, we can run this app comfortably with a single p1.x1 pod.

#### Example 2: Facial recognition

For this example, suppose you’re building an application to identify customers using facial recognition for a secure banking app. Facial recognition can work with as few as 128 dimensions, but in this case, because the app will be used for access to finances, we want to make sure we’re certain that the person using it is the right one. We plan for 100M customers and use 2048 dimensions per vector.

We know from our rules of thumb above that 1M vectors with 768 dimensions fit nicely in a p1.x1 pod. We can just divide those numbers into the new targets to get the ratios we’ll need for our pod estimate:

```
100M / 1M = 100 base p1 pods
2048 / 768 = 2.667 vector ratio
2.667 * 100 = 267 rounding up
```

So we need 267 p1.x1 pods. We can reduce that by switching to s1 pods instead, sacrificing latency by increasing storage availability. They hold five times the storage of p1.x1, so the math is simple:

```
267 / 5 = 54 rounding up
```

So we estimate that we need 54 s1.x1 pods to store very high dimensional data for the face of each of the bank’s customers.



# Create a pod-based index
Source: https://docs.pinecone.io/guides/indexes/pods/create-a-pod-based-index

Create and configure a pod-based Pinecone index

<Warning>
  Customers who sign up for a Standard or Enterprise plan on or after August 18, 2025 cannot create pod-based indexes. Instead, create [serverless indexes](/guides/index-data/create-an-index), and consider using [dedicated read nodes](/guides/index-data/dedicated-read-nodes) for large workloads (millions of records or more, and moderate or high query rates).
</Warning>

This page shows you how to create a pod-based index. For guidance on serverless indexes, see [Create a serverless index](/guides/index-data/create-an-index).


## Create a pod index

To create a pod index, use the [`create_index`](/reference/api/latest/control-plane/create_index) operation as follows:

* Provide a `name` for the index.
* Specify the `dimension` and `metric` of the vectors you'll store in the index. This should match the dimension and metric supported by your embedding model.
* Set `spec.environment` to the [environment](/guides/index-data/create-an-index#cloud-regions) where the index should be deployed. For Python, you also need to import the `ServerlessSpec` class.
* Set `spec.pod_type` to the [pod type](/guides/indexes/pods/understanding-pod-based-indexes#pod-types) and [size](/guides/index-data/indexing-overview#pod-size-and-performance) that you want.

Other parameters are optional. See the [API reference](/reference/api/latest/control-plane/create_index) for details.

<CodeGroup>
  ```Python Python theme={null}
  from pinecone.grpc import PineconeGRPC as Pinecone, PodSpec

  pc = Pinecone(api_key="YOUR_API_KEY")

  pc.create_index(
    name="docs-example",
    dimension=1536,
    metric="cosine",
    spec=PodSpec(
      environment="us-west1-gcp",
      pod_type="p1.x1",
      pods=1
    ),
    deletion_protection="disabled"

  )
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({
    apiKey: 'YOUR_API_KEY'
  });

  await pc.createIndex({
    name: 'docs-example',
    dimension: 1536,
    metric: 'cosine',
    spec: {
      pod: {
        environment: 'us-west1-gcp',
        podType: 'p1.x1',
        pods: 1
      }
    },
    deletionProtection: 'disabled',
  });
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Pinecone;
  import org.openapitools.db_control.client.model.IndexModel;
  import org.openapitools.db_control.client.model.DeletionProtection;

  public class CreateIndexExample {
      public static void main(String[] args) {
          Pinecone pc = new Pinecone.Builder("YOUR_API_KEY").build();
          pc.createPodsIndex("docs-example", 1536, "us-west1-gcp",
                  "p1.x1", "cosine", DeletionProtection.DISABLED);
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
    	metric := pinecone.Dotproduct
  	  deletionProtection := pinecone.DeletionProtectionDisabled

      idx, err := pc.CreatePodIndex(ctx, &pinecone.CreatePodIndexRequest{
          Name:               indexName,
          Metric:             &metric,
          Dimension:          1536,
          Environment:        "us-east1-gcp",
          PodType:            "p1.x1",
          DeletionProtection: &deletionProtection,
      })
      if err != nil {
          log.Fatalf("Failed to create pod-based index: %v", idx.Name)
      } else {
          fmt.Printf("Successfully created pod-based index: %v", idx.Name)
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
      Spec = new PodIndexSpec
      {
          Pod = new PodSpec
          {
              Environment = "us-east1-gcp",
              PodType = "p1.x1",
              Pods = 1,
          }
      },
      DeletionProtection = DeletionProtection.Disabled
  });
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

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
              "pod": {
                 "environment": "us-west1-gcp",
                 "pod_type": "p1.x1",
                 "pods": 1
              }
           },
           "deletion_protection": "disabled"
        }'
  ```
</CodeGroup>


## Create a pod index from a collection

You can create a pod-based index from a collection. For more details, see [Restore an index](/guides/indexes/pods/restore-a-pod-based-index).



# Manage pod-based indexes
Source: https://docs.pinecone.io/guides/indexes/pods/manage-pod-based-indexes

List, describe, and configure pod-based indexes

<Warning>
  Customers who sign up for a Standard or Enterprise plan on or after August 18, 2025 cannot create pod-based indexes. Instead, create [serverless indexes](/guides/index-data/create-an-index), and consider using [dedicated read nodes](/guides/index-data/dedicated-read-nodes) for large workloads (millions of records or more, and moderate or high query rates).
</Warning>

This page shows you how to manage pod-based indexes.

For guidance on serverless indexes, see [Manage serverless indexes](/guides/manage-data/manage-indexes).


## Describe a pod-based index

Use the [`describe_index`](/reference/api/latest/control-plane/describe_index/) endpoint to get a complete description of a specific index:

<CodeGroup>
  ```Python Python theme={null}
  from pinecone.grpc import PineconeGRPC as Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  pc.describe_index(name="docs-example")

  # Response:
  # {'dimension': 1536,
  #  'host': 'docs-example-4mkljsz.svc.aped-4627-b74a.pinecone.io',
  #  'metric': 'cosine',
  #  'name': 'docs-example',
  #  'spec': {'pod': {'environment': 'us-east-1-aws',
  #                   'pod_type': 's1.x1',
  #                   'pods': 1,
  #                   'replicas': 1,
  #                   'shards': 1}},
  #  'status': {'ready': True, 'state': 'Ready'}}
  ```

  ```JavaScript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  await pc.describeIndex('docs-example');

  // Response:
  // {
  //    "name": "docs-example",
  //    "dimension": 1536,
  //    "metric": "cosine",
  //    "host": "docs-example-4mkljsz.svc.aped-4627-b74a.pinecone.io",
  //    "deletionProtection": "disabled",
  //    "spec": {
  //       "pod": {
  //          "environment": "us-east-1-aws",
  //          "pod_type": "s1.x1",
  //          "pods": 1,
  //          "replicas": 1,
  //          "shards": 1
  //       }
  //    },
  //    "status": {
  //       "ready": true,
  //       "state": "Ready"
  //    }
  // }
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

  // Response:
  // class IndexModel {
  //     name: docs-example
  //     dimension: 1536
  //     metric: cosine
  //     host: docs-example-4mkljsz.svc.aped-4627-b74a.pinecone.io
  //     deletionProtection: disabled
  //     spec: class IndexModelSpec {
  //         serverless: null
  //         pod: class PodSpec {
  //             cloud: aws
  //             region: us-east-1
  //             environment: us-east-1-aws,
  //             podType: s1.x1,
  //             pods: 1,
  //             replicas: 1,
  //             shards: 1
  //         }
  //     }
  //     status: class IndexModelStatus {
  //         ready: true
  //         state: Ready
  //     }
  // }
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

  // Response:
  // index: {
  // 	"name": "docs-example",
  // 	"dimension": 1536,
  // 	"host": "docs-example-4mkljsz.svc.aped-4627-b74a.pinecone.io",
  // 	"metric": "cosine",
  //  "deletion_protection": "disabled",
  // 	"spec": {
  // 	  "pod": {
  //       "environment": "us-east-1-aws",
  //       "pod_type": "s1.x1",
  //       "pods": 1,
  //       "replicas": 1,
  //       "shards": 1
  // 	  }
  // 	},
  // 	"status": {
  // 	  "ready": true,
  // 	  "state": "Ready"
  // 	}
  // }
  ```

  ```csharp C# theme={null}
  using Pinecone;

  var pinecone = new PineconeClient("YOUR_API_KEY");

  var indexModel = await pinecone.DescribeIndexAsync("docs-example");

  Console.WriteLine(indexModel);

  // Response:
  // {
  //   "name": "docs-example",
  //   "dimension": 1536,
  //   "metric": "cosine",
  //   "host": "docs-example-4mkljsz.svc.aped-4627-b74a.pinecone.io",
  //   "deletion_protection": "disabled",
  //   "spec": {
  //     "serverless": null,
  //     "pod": {
  //        "environment": "us-east-1-aws",
  //        "pod_type": "s1.x1",
  //        "pods": 1,
  //        "replicas": 1,
  //        "shards": 1
  //     }
  //   },
  //   "status": {
  //     "ready": true,
  //     "state": "Ready"
  //   }
  // }
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl -i -X GET "https://api.pinecone.io/indexes/docs-example" \
      -H "Api-Key: $PINECONE_API_KEY" \
      -H "X-Pinecone-API-Version: 2025-04"
  # Response:
  # {
  #    "name": "docs-example",
  #    "metric": "cosine",
  #    "dimension": 1536,
  #    "status": {
  #       "ready": true,
  #       "state": "Ready"
  #    },
  #    "host": "docs-example-4mkljsz.svc.aped-4627-b74a.pinecone.io",
  #    "spec": {
  #       "pod": {
  #          "environment": "us-east-1-aws",
  #          "pod_type": "s1.x1",
  #          "pods": 1,
  #          "replicas": 1,
  #          "shards": 1
  #       }
  #    }
  # }
  ```
</CodeGroup>

<Warning>
  **Do not target an index by name in production.**

  When you target an index by name for data operations such as `upsert` and `query`, the SDK gets the unique DNS host for the index using the `describe_index` operation. This is convenient for testing but should be avoided in production because `describe_index` uses a different API than data operations and therefore adds an additional network call and point of failure. Instead, you should get an index host once and cache it for reuse or specify the host directly.
</Warning>


## Delete a pod-based index

Use the [`delete_index`](/reference/api/latest/control-plane/delete_index) operation to delete a pod-based index and all of its associated resources.

<Note>
  You are billed for a pod-based index even when it is not in use.
</Note>

<CodeGroup>
  ```python Python theme={null}
  # pip install "pinecone[grpc]"
  from pinecone.grpc import PineconeGRPC as Pinecone, PodSpec

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


## Selective metadata indexing

For pod-based indexes, Pinecone indexes all metadata fields by default. When metadata fields contains many unique values, pod-based indexes will consume significantly more memory, which can lead to performance issues, pod fullness, and a reduction in the number of possible vectors that fit per pod.

To avoid indexing high-cardinality metadata that is not needed for [filtering your queries](/guides/index-data/indexing-overview#metadata) and keep memory utilization low, specify which metadata fields to index using the `metadata_config` parameter.

<Note>
  Since high-cardinality metadata does not cause high memory utilization in serverless indexes, selective metadata indexing is not supported.
</Note>

The value for the `metadata_config` parameter is a JSON object containing the names of the metadata fields to index.

```JSON JSON theme={null}
{
    "indexed": [
        "metadata-field-1",
        "metadata-field-2",
        "metadata-field-n"
    ]
}
```

**Example**

The following example creates a pod-based index that only indexes the `genre` metadata field. Queries against this index that filter for the `genre` metadata field may return results; queries that filter for other metadata fields behave as though those fields do not exist.

<CodeGroup>
  ```Python Python theme={null}
  from pinecone.grpc import PineconeGRPC as Pinecone, PodSpec

  pc = Pinecone(api_key="YOUR_API_KEY")

  pc.create_index(
    name="docs-example",
    dimension=1536,
    metric="cosine",
    spec=PodSpec(
      environment="us-west1-gcp",
      pod_type="p1.x1",
      pods=1,
      metadata_config = {
        "indexed": ["genre"]
      }
    ),
    deletion_protection="disabled"

  )
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({
    apiKey: 'YOUR_API_KEY'
  });

  await pc.createIndex({
    name: 'docs-example',
    dimension: 1536,
    metric: 'cosine',
    spec: {
      pod: {
        environment: 'us-west1-gcp',
        podType: 'p1.x1',
        pods: 1,
        metadata_config: {
          indexed: ["genre"]
        }
      }
    },
    deletionProtection: 'disabled',
  });
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Pinecone;
  import org.openapitools.db_control.client.model.IndexModel;
  import org.openapitools.db_control.client.model.DeletionProtection;

  public class CreateIndexExample {
      public static void main(String[] args) {
          Pinecone pc = new Pinecone.Builder("YOUR_API_KEY").build();
          CreateIndexRequestSpecPodMetadataConfig podSpecMetadataConfig = new CreateIndexRequestSpecPodMetadataConfig();
          List<String> indexedItems = Arrays.asList("genre", "year");
          podSpecMetadataConfig.setIndexed(indexedItems);
          pc.createPodsIndex("docs-example", 1536, "us-west1-gcp",
                  "p1.x1", "cosine", podSpecMetadataConfig, DeletionProtection.DISABLED);
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

      podIndexMetadata := &pinecone.PodSpecMetadataConfig{
          Indexed: &[]string{"genre"},
      }

      indexName := "docs-example"
    	metric := pinecone.Dotproduct
  	deletionProtection := pinecone.DeletionProtectionDisabled

  	idx, err := pc.CreatePodIndex(ctx, &pinecone.CreatePodIndexRequest{
          Name:               indexName,
          Metric:             &metric,
          Dimension:          1536,
          Environment:        "us-east1-gcp",
          PodType:            "p1.x1",
          DeletionProtection: &deletionProtection,
    	})
    	if err != nil {
          log.Fatalf("Failed to create pod-based index: %v", idx.Name)
      } else {
          fmt.Printf("Successfully created pod-based index: %v", idx.Name)
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
      Spec = new PodIndexSpec
      {
          Pod = new PodSpec
          {
              Environment = "us-east1-gcp",
              PodType = "p1.x1",
              Pods = 1,
              MetadataConfig = new PodSpecMetadataConfig
              {
                  Indexed = new List<string> { "genre" },
              },
          }
      },
      DeletionProtection = DeletionProtection.Disabled
  });
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl -s https://api.pinecone.io/indexes \
    -H "Accept: application/json" \
    -H "Content-Type: application/json" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-API-Version: 2025-04" \
    -d '{
           "name": "docs-example",
           "dimension": 1536,
           "metric": "cosine",
           "spec": {
              "pod": {
                 "environment": "us-west1-gcp",
                 "pod_type": "p1.x1",
                 "pods": 1,
                 "metadata_config": {
                    "indexed": ["genre"]
                 }
              }
           },
           "deletion_protection": "disabled"
        }'
  ```
</CodeGroup>


## Prevent index deletion

<Note>
  This feature requires [Pinecone API version](/reference/api/versioning) `2024-07`, [Python SDK](/reference/python-sdk) v5.0.0, [Node.js SDK](/reference/node-sdk) v3.0.0, [Java SDK](/reference/java-sdk) v2.0.0, or [Go SDK](/reference/go-sdk) v1.0.0 or later.
</Note>

You can prevent an index and its data from accidental deleting when [creating a new index](/guides/index-data/create-an-index) or when [configuring an existing index](/guides/indexes/pods/manage-pod-based-indexes). In both cases, you set the `deletion_protection` parameter to `enabled`.

To enable deletion protection when creating a new index:

<CodeGroup>
  ```python Python theme={null}
  # pip install "pinecone[grpc]"
  from pinecone.grpc import PineconeGRPC as Pinecone, PodSpec

  pc = Pinecone(api_key="YOUR_API_KEY")

  pc.create_index(
    name="docs-example",
    dimension=1536,
    metric="cosine",
    spec=PodSpec(
      environment="us-west1-gcp",
      pod_type="p1.x1",
      pods=1
    ),
      deletion_protection="enabled"
  )
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({
    apiKey: 'YOUR_API_KEY'
  });

  await pc.createIndex({
    name: 'docs-example',
    dimension: 1536,
    metric: 'cosine',
    spec: {
      pod: {
        environment: 'us-west1-gcp',
        podType: 'p1.x1',
        pods: 1
      }
    },
    deletionProtection: 'enabled',
  });
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Pinecone;
  import org.openapitools.db_control.client.model.IndexModel;
  import org.openapitools.db_control.client.model.DeletionProtection;

  public class CreateIndexExample {
      public static void main(String[] args) {
          Pinecone pc = new Pinecone.Builder("YOUR_API_KEY").build();
          pc.createPodsIndex("docs-example", 1536, "us-west1-gcp",
                  "p1.x1", "cosine", DeletionProtection.ENABLED);
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
    	metric := pinecone.Dotproduct
  	deletionProtection := pinecone.DeletionProtectionDisabled

  	idx, err := pc.CreatePodIndex(ctx, &pinecone.CreatePodIndexRequest{
          Name:               indexName,
          Metric:             &metric,
          Dimension:          1536,
          Environment:        "us-east1-gcp",
          PodType:            "p1.x1",
          DeletionProtection: &deletionProtection,
    	})
    	if err != nil {
          log.Fatalf("Failed to create pod-based index: %v", idx.Name)
      } else {
          fmt.Printf("Successfully created pod-based index: %v", idx.Name)
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
      Spec = new PodIndexSpec
      {
          Pod = new PodSpec
          {
              Environment = "us-east1-gcp",
              PodType = "p1.x1",
              Pods = 1,
          }
      },
      DeletionProtection = DeletionProtection.Enabled
  });
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

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
              "pod": {
                 "environment": "us-west1-gcp",
                 "pod_type": "p1.x1",
                 "pods": 1
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
          pc.configurePodsIndex("docs-example", DeletionProtection.ENABLED);
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

  curl -s -X PATCH "https://api.pinecone.io/indexes/docs-example" \
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


## Disable deletion protection

Before you can [delete an index](#delete-a-pod-based-index) with deletion protection enabled, you must first disable deletion protection as follows:

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
          pc.configurePodsIndex("docs-example", DeletionProtection.DISABLED);
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

  curl -s -X PATCH "https://api.pinecone.io/indexes/docs-example" \
      -H "Content-Type: application/json" \
      -H "Api-Key: $PINECONE_API_KEY" \
      -H "X-Pinecone-API-Version: 2025-04" \
      -d '{
          "deletion_protection": "disabled"
          }'
  ```
</CodeGroup>


## Delete an entire namespace

In pod-based indexes, reads and writes share compute resources, so deleting an entire namespace with many records can increase the latency of read operations. In such cases, consider [deleting records in batches](#delete-records-in-batches).


## Delete records in batches

In pod-based indexes, reads and writes share compute resources, so deleting an entire namespace or a large number of records can increase the latency of read operations. To avoid this, delete records in batches of up to 1000, with a brief sleep between requests. Consider using smaller batches if the index has active read traffic.

<CodeGroup>
  ```python Batch delete a namespace theme={null}
  from pinecone import Pinecone
  import numpy as np
  import time

  pc = Pinecone(api_key='API_KEY')

  INDEX_NAME = 'INDEX_NAME'
  NAMESPACE = 'NAMESPACE_NAME'
  # Consider using smaller batches if you have a high RPS for read operations
  BATCH = 1000

  index = pc.Index(name=INDEX_NAME)
  dimensions = index.describe_index_stats()['dimension']

  # Create the query vector
  query_vector = np.random.uniform(-1, 1, size=dimensions).tolist()
  results = index.query(vector=query_vector, namespace=NAMESPACE, top_k=BATCH)

  # Delete in batches until the query returns no results
  while len(results['matches']) > 0:
      ids = [i['id'] for i in results['matches']]
      index.delete(ids=ids, namespace=NAMESPACE)
      time.sleep(0.01)
      results = index.query(vector=query_vector, namespace=NAMESPACE, top_k=BATCH)
  ```

  ```python Batch delete by metadata theme={null}
  from pinecone import Pinecone
  import numpy as np
  import time

  pc = Pinecone(api_key='API_KEY')

  INDEX_NAME = 'INDEX_NAME'
  NAMESPACE = 'NAMESPACE_NAME'
  # Consider using smaller batches if you have a high RPS for read operations
  BATCH = 1000

  index = pc.Index(name=INDEX_NAME)
  dimensions = index.describe_index_stats()['dimension']

  METADATA_FILTER = {}

  # Create the query vector with a filter
  query_vector = np.random.uniform(-1, 1, size=dimensions).tolist()
  results = index.query(vector=query_vector, namespace=NAMESPACE, filter=METADATA_FILTER, top_k=BATCH)

  # Delete in batches until the query returns no results
  while len(results['matches']) > 0:
      ids = [i['id'] for i in results['matches']]
      index.delete(ids=ids, namespace=NAMESPACE)
      time.sleep(0.01)
      results = index.query(vector=query_vector, namespace=NAMESPACE, filter=METADATA_FILTER, top_k=BATCH)
  ```
</CodeGroup>


## Delete records by metadata

<Note>
  In pod-based indexes, if you are targeting a large number of records for deletion and the index has active read traffic, consider [deleting records in batches](#delete-records-in-batches).
</Note>

To delete records from a namespace based on their metadata values, pass a [metadata filter expression](/guides/index-data/indexing-overview#metadata-filter-expressions) to the `delete` operation. This deletes all records in the namespace that match the filter expression.

For example, the following code deletes all records with a `genre` field set to `documentary` from namespace `example-namespace`:

<CodeGroup>
  ```Python Python theme={null}
  # pip install "pinecone[grpc]"
  from pinecone.grpc import PineconeGRPC as Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  # To get the unique host for an index, 
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  index = pc.Index(host="INDEX_HOST")

  index.delete(
      filter={
          "genre": {"$eq": "documentary"}
      },
      namespace="example-namespace" 
  )
  ```

  ```JavaScript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({ apiKey: "YOUR_API_KEY" })

  // To get the unique host for an index, 
  // see https://docs.pinecone.io/guides/manage-data/target-an-index
  const index = pc.index("INDEX_NAME", "INDEX_HOST")

  const ns = index.namespace('example-namespace')

  await ns.deleteMany({
    genre: { $eq: "documentary" },
  });
  ```

  ```java Java theme={null}
  import com.google.protobuf.Struct;
  import com.google.protobuf.Value;
  import io.pinecone.clients.Index;
  import io.pinecone.configs.PineconeConfig;
  import io.pinecone.configs.PineconeConnection;

  import java.util.Arrays;
  import java.util.List;

  public class DeleteExample {
      public static void main(String[] args) {
          PineconeConfig config = new PineconeConfig("YOUR_API_KEY");
          // To get the unique host for an index, 
          // see https://docs.pinecone.io/guides/manage-data/target-an-index
          config.setHost("INDEX_HOST");
          PineconeConnection connection = new PineconeConnection(config);
          Index index = new Index(connection, "INDEX_NAME");
          Struct filter = Struct.newBuilder()
                  .putFields("genre", Value.newBuilder()
                          .setStructValue(Struct.newBuilder()
                                  .putFields("$eq", Value.newBuilder()
                                          .setStringValue("documentary")
                                          .build()))
                          .build())
                  .build();
          index.deleteByFilter(filter, "example-namespace");
          
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

      metadataFilter := map[string]interface{}{
  		"genre": map[string]interface{}{
  			"$eq": "documentary",
  		},
      }

      filter, err := structpb.NewStruct(metadataFilter)
      if err != nil {
          log.Fatalf("Failed to create metadata filter: %v", err)
      }

      err = idxConnection.DeleteVectorsByFilter(ctx, filter)
      if err != nil {
          log.Fatalf("Failed to delete vector(s) with filter %+v: %v", filter, err)
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
      Namespace = "example-namespace",
      Filter = new Metadata
      {
          ["genre"] =
              new Metadata
              {
                  ["$eq"] = "documentary"
              }
      }
  });
  ```

  ```bash curl theme={null}
  # To get the unique host for an index,
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="INDEX_HOST"

  curl -i "https://$INDEX_HOST/vectors/delete" \
    -H 'Api-Key: $PINECONE_API_KEY' \
    -H 'Content-Type: application/json' \
    -H "X-Pinecone-API-Version: 2025-04" \
    -d '{
      "filter": {"genre": {"$eq": "documentary"}},
      "namespace": "example-namespace"
    }'
  ```
</CodeGroup>


## Tag an index

When configuring an index, you can tag the index to help with index organization and management. For more details, see [Tag an index](/guides/manage-data/manage-indexes#configure-index-tags).


## Manage costs

### Set a project pod limit

To control costs, [project owners](/guides/projects/understanding-projects#project-roles) can [set the maximum total number of pods](/reference/api/database-limits#pods-per-project) allowed across all pod-based indexes in a project. The default pod limit is 5.

<Tabs>
  <Tab title="Pinecone console">
    1. Go to [Settings > Projects](https://app.pinecone.io/organizations/-/settings/projects).
    2. For the project you want to update, click the **ellipsis (...) menu > Configure**.
    3. In the **Pod Limit** section, update the number of pods.
    4. Click **Save Changes**.
  </Tab>

  <Tab title="API">
    <token />

    ```bash curl theme={null}
    PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"
    PROJECT_ID="YOUR_PROJECT_ID"

    curl -X PATCH "https://api.pinecone.io/admin/projects/$PROJECT_ID" \
      -H "accept: application/json" \
      -H "Content-Type: application/json" \
    	-H "X-Pinecone-Api-Version: 2025-04" \
      -d '{
        "max_pods": 5
        }'
    ```

    The example returns a response like the following:

    ```json  theme={null}
    {
      "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "name": "example-project",
      "max_pods": 5,
      "force_encryption_with_cmek": false,
      "organization_id": "string",
      "created_at": "2025-03-17T00:42:31.912Z"
    }
    ```
  </Tab>
</Tabs>

### Back up inactive pod-based indexes

For each pod-based index, billing is determined by the per-minute price per pod and the number of pods the index uses, regardless of index activity. When a pod-based index is not in use, [back it up using collections](/guides/indexes/pods/back-up-a-pod-based-index) and delete the inactive index. When you're ready to use the vectors again, you can [create a new index from the collection](/guides/indexes/pods/create-a-pod-based-index#create-a-pod-index-from-a-collection). This new index can also use a different index type or size. Because it's relatively cheap to store collections, you can reduce costs by only running an index when it's in use.

### Choose the right index type and size

Pod sizes are designed for different applications, and some are more expensive than others. [Choose the appropriate pod type and size](/guides/indexes/pods/choose-a-pod-type-and-size), so you pay for the resources you need. For example, the `s1` pod type provides large storage capacity and lower overall costs with slightly higher query latencies than `p1` pods. By switching to a different pod type, you may be able to reduce costs while still getting the performance your application needs.

<Note>
  For pod-based indexes, project owners can [set limits for the total number of pods](/reference/api/database-limits#pods-per-project) across all indexes in the project. The default pod limit is 5.
</Note>


## Monitor performance

Pinecone generates time-series performance metrics for each Pinecone index. You can monitor these metrics directly in the Pinecone console or with tools like Prometheus or Datadog.

### Use the Pinecone Console

To view performance metrics in the Pinecone console:

1. Open the [Pinecone console](https://app.pinecone.io/organizations/-/projects).
2. Select the project containing the index you want to monitor.
3. Go to **Database > Indexes**.
4. Select the index.
5. Go to the **Metrics** tab.

### Use Datadog

To monitor Pinecone with Datadog, use Datadog's [Pinecone integration](/integrations/datadog).

<Note>
  This feature is available on [Standard and Enterprise plans](https://www.pinecone.io/pricing/).
</Note>

### Use Prometheus

<Note>
  This feature is available on [Standard and Enterprise plans](https://www.pinecone.io/pricing/). When using [Bring Your Own Cloud](/guides/production/bring-your-own-cloud), you must configure Prometheus monitoring within your VPC.
</Note>

To monitor all pod-based indexes in a specific region of a project, insert the following snippet into the [`scrape_configs`](https://prometheus.io/docs/prometheus/latest/configuration/configuration/#scrape_config) section of your `prometheus.yml` file and update it with values for your Prometheus integration:

```YAML  theme={null}
scrape_configs:
  - job_name: "pinecone-pod-metrics"
    scheme: https
    metrics_path: '/metrics'
    authorization:
      credentials: API_KEY
    static_configs:
      - targets: ["metrics.ENVIRONMENT.pinecone.io" ]
```

* Replace `API_KEY` with an API key for the project you want to monitor. If necessary, you can [create an new API key](/reference/api/authentication) in the Pinecone console.

* Replace `ENVIRONMENT` with the [environment](/guides/indexes/pods/understanding-pod-based-indexes#pod-environments) of the pod-based indexes you want to monitor.

For more configuration details, see the [Prometheus docs](https://prometheus.io/docs/prometheus/latest/configuration/configuration/).

#### Available metrics

The following metrics are available when you integrate Pinecone with Prometheus:

| Name                                 | Type      | Description                                                                       |
| :----------------------------------- | :-------- | :-------------------------------------------------------------------------------- |
| `pinecone_vector_count`              | gauge     | The number of records per pod in the index.                                       |
| `pinecone_request_count_total`       | counter   | The number of data plane calls made by clients.                                   |
| `pinecone_request_error_count_total` | counter   | The number of data plane calls made by clients that resulted in errors.           |
| `pinecone_request_latency_seconds`   | histogram | The distribution of server-side processing latency for pinecone data plane calls. |
| `pinecone_index_fullness`            | gauge     | The fullness of the index on a scale of 0 to 1.                                   |

#### Metric labels

Each metric contains the following labels:

| Label          | Description                                                                                                                                    |
| :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------- |
| `pid`          | Process identifier.                                                                                                                            |
| `index_name`   | Name of the index to which the metric applies.                                                                                                 |
| `project_name` | Name of the project containing the index.                                                                                                      |
| `request_type` | Type of request: `upsert`, `delete`, `fetch`, `query`, or `describe_index_stats`. This label is included only in `pinecone_request_*` metrics. |

#### Example queries

Return the average latency in seconds for all requests against the Pinecone index `docs-example`:

```shell  theme={null}
avg by (request_type) (pinecone_request_latency_seconds{index_name="docs-example"})
```

Return the vector count for the Pinecone index `docs-example`:

```shell  theme={null}
sum ((avg by (app) (pinecone_vector_count{index_name="docs-example"})))
```

Return the total number of requests against the Pinecone index `docs-example` over one minute:

```shell  theme={null}
sum by (request_type)(increase(pinecone_request_count_total{index_name="docs-example"}[60s]))
```

Return the total number of upsert requests against the Pinecone index `docs-example` over one minute:

```shell  theme={null}
sum by (request_type)(increase(pinecone_request_count_total{index_name="docs-example", request_type="upsert"}[60s]))
```

Return the total errors returned by the Pinecone index `docs-example` over one minute:

```shell  theme={null}
sum by (request_type) (increase(pinecone_request_error_count{
      index_name="docs-example"}[60s]))
```

Return the index fullness metric for the Pinecone index `docs-example`:

```
round(max (pinecone_index_fullness{index_name="docs-example"} * 100))
```


## Troubleshooting

### Index fullness errors

Serverless indexes automatically scale as needed.

However, pod-based indexes can run out of capacity. When that happens, upserting new records will fail with the following error:

```console console theme={null}
Index is full, cannot accept data.
```

### High-cardinality metadata and over-provisioning

This [Loom video walkthrough](https://www.loom.com/share/ce6f5dd0c3e14ba0b988fe32d96b703a?sid=48646dfe-c10c-4143-82c6-031fefe05a68) shows you how to manage two scenarios:

* The first scenario involves customers loading an index replete with high cardinality metadata. This can trigger a series of unforeseen challenges, and hence, it's vital to comprehend how to manage this situation effectively. This methodology can be applied whenever you need to change your metadata configuration.

* The second scenario that we will address involves customers who have over-provisioned the number of pods they need. More specifically, we will discuss the process of re-scaling an index in instances where the customer has previously scaled vertically and now desires to scale the index back down.



# Migrate a pod-based index to serverless
Source: https://docs.pinecone.io/guides/indexes/pods/migrate-a-pod-based-index-to-serverless

Migrate existing pod indexes to cost-effective serverless

This page shows you how to migrate a pod-based index to [serverless](/guides/get-started/database-architecture). The migration process is free; the standard costs of upserting records to a new serverless index are not applied.

<Warning>
  In most cases, migrating to serverless reduces costs significantly. However, costs can increase for read-heavy workloads with more than 1 query per second and for indexes with many records in a single namespace. Before migrating, consider [contacting Pinecone Support](/troubleshooting/contact-support) for help estimating and managing cost implications.
</Warning>


## Limitations

Migration is supported for pod-based indexes with less than 25 million records and 20,000 namespaces across all supported clouds (AWS, GCP, and Azure).

Also, serverless indexes do not support the following features. If you were using these features for your pod-based index, you will need to adapt your code. If you are blocked by these limitations, [contact Pinecone Support](/troubleshooting/contact-support).

* [Selective metadata indexing](/guides/indexes/pods/manage-pod-based-indexes#selective-metadata-indexing)

  * Because high-cardinality metadata in serverless indexes does not cause high memory utilization, this operation is not relevant.
* [Filtering index statistics by metadata](/reference/api/latest/data-plane/describeindexstats)


## How it works

Migrating a pod-based index to serverless is a 2-step process:

<Steps>
  <Step title="Save the pod-based index as a collection" />

  <Step title="Create a new serverless index from the collection" />
</Steps>

After migration, you will have both a new serverless index and the original pod-based index. Once you've switched your workload to the serverless index, you can delete the pod-based index to avoid paying for unused resources.


## 1. Understand cost implications

In most cases, migrating to serverless reduces costs significantly. However, costs can increase for read-heavy workloads with more than 1 query per second and for indexes with many records in a single namespace.

Before migrating, consider [contacting Pinecone Support](/troubleshooting/contact-support) for help estimating and managing cost implications.


## 2. Prepare for migration

Migrating a pod-based index to serverless can take anywhere from a few minutes to several hours, depending on the size of the index. During that time, you can continue reading from the pod-based index. However, all [upserts](/guides/index-data/upsert-data), [updates](/guides/manage-data/update-data), and [deletes](/guides/manage-data/delete-data) to the pod-based index will not automatically be reflected in the new serverless index, so be sure to prepare in one of the following ways:

* **Pause write traffic:** If downtime is acceptable, pause traffic to the pod-based index before starting migration. After migration, you will start sending traffic to the serverless index.

* **Log your writes:** If you need to continue reading from the pod-based index during migration, send read traffic to the pod-based index, but log your writes to a temporary location outside of Pinecone (e.g., S3). After migration, you will replay the logged writes to the new serverless index and start sending all traffic to the serverless index.


## 3. Start migration

<Tabs>
  <Tab title="Pinecone console">
    1. In the [Pinecone console](https://app.pinecone.io/), go to your pod-based index and click the **ellipsis (...) menu > Migrate to serverless**.

       <img className="block max-w-full" noZoom src="https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/migrate-to-serverless.png?fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=24217a2e791ffce162686b8fdef47948" data-og-width="1184" width="1184" data-og-height="252" height="252" data-path="images/migrate-to-serverless.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/migrate-to-serverless.png?w=280&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=6ccfc31bcf3e4348c53ed95c0ce4965c 280w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/migrate-to-serverless.png?w=560&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=0cc7ead9e2f5f6552ed7ef29bf0140fb 560w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/migrate-to-serverless.png?w=840&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=780e1acbe7dbdf582d6b46bd8b2a8e4b 840w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/migrate-to-serverless.png?w=1100&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=89bccffcedc7cedecb621f3c453f8938 1100w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/migrate-to-serverless.png?w=1650&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=f732644be14d0a1ff10ef79a5e48ada1 1650w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/migrate-to-serverless.png?w=2500&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=8a77b4f2dd850dd607c84a3ec29a4fff 2500w" />

       <Note>
         The dropdown will not display **Migrate to serverless** if the index has any of the listed [limitations](#limitations).
       </Note>

    2. To save the legacy index and create a new serverless index now, follow the prompts.

       Depending on the size of the index, migration can take anywhere from a few minutes to several hours. While migration is in progress, you'll see the yellow **Initializing** status:
       <img src="https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/create-serverless-from-collection-initializing.png?fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=acffe738f1cbe2e08e4bc2fad7e957dd" alt="create index from collection - initializing status" data-og-width="2202" width="2202" data-og-height="506" height="506" data-path="images/create-serverless-from-collection-initializing.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/create-serverless-from-collection-initializing.png?w=280&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=6f4464d50c752857a48f220414c61372 280w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/create-serverless-from-collection-initializing.png?w=560&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=fa65345532ef65a5f57007e2e233b30d 560w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/create-serverless-from-collection-initializing.png?w=840&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=9720ae95b7630f338f021e642c35942d 840w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/create-serverless-from-collection-initializing.png?w=1100&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=75802502e5b8b22ab0c49728f26c37b7 1100w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/create-serverless-from-collection-initializing.png?w=1650&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=362c1d22e182242489d383254856f612 1650w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/create-serverless-from-collection-initializing.png?w=2500&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=0d439490afc512a8d8e1ddaffbb22544 2500w" />

       When the new serverless index is ready, the status will change to green:

       <img src="https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/create-serverless-from-collection-ready.png?fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=e04b6b0d892301435be282e5c4fa394b" alt="create index from collection - ready status" data-og-width="2202" width="2202" data-og-height="500" height="500" data-path="images/create-serverless-from-collection-ready.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/create-serverless-from-collection-ready.png?w=280&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=e9f3525138da438aca544f9f9e91ec97 280w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/create-serverless-from-collection-ready.png?w=560&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=f3b774060c9b08569720013a324dd9d0 560w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/create-serverless-from-collection-ready.png?w=840&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=195db840282f07a709bff77931856714 840w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/create-serverless-from-collection-ready.png?w=1100&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=f40328d14f9aa1dac2aacf82115ac53b 1100w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/create-serverless-from-collection-ready.png?w=1650&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=8a50755a42dd444ce4457673473507bc 1650w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/create-serverless-from-collection-ready.png?w=2500&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=490d2bf71be87a7560493ea47b586bcb 2500w" />
  </Tab>

  <Tab title="API/SDK">
    1. Use the [`create_collection`](/reference/api/latest/control-plane/create_collection) operation to create a backup of your pod-based index:

       <CodeGroup>
         ```javascript JavaScript theme={null}
         // Requires Node.js SDK v6.1.2 or later
         import { Pinecone } from '@pinecone-database/pinecone'

         const pc = new Pinecone({
           apiKey: 'YOUR_API_KEY'
         });

         await pc.createCollection({
           name: "pod-collection",
           source: "pod-index"
         });
         ```

         ```go Go theme={null}
         // Requires Go SDK v4.1.2 or later
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

             collection, err := pc.CreateCollection(ctx, &pinecone.CreateCollectionRequest{
                 Name: "pod-collection", 
                 Source: "pod-index",
             })
             if err != nil {
                 log.Fatalf("Failed to create collection: %v", err)
             } else {
                 fmt.Printf("Successfully created collection: %v", collection.Name)
             }
         }
         ```

         ```shell curl theme={null}
         PINECONE_API_KEY="YOUR_API_KEY"

         curl -s POST "https://api.pinecone.io/collections" \
         -H "Accept: application/json" \
         -H "Content-Type: application/json" \
         -H "Api-Key: $PINECONE_API_KEY" \
         -H "X-Pinecone-API-Version: 2025-04" \
         -d '{
                 "name": "pod-collection",
                 "source": "pod-index"
         }'
         ```
       </CodeGroup>

    2. Use the [`create_index`](/reference/api/latest/control-plane/create_index) operation to create a new serverless index from the collection:

       * Use API verison `2025-04` or later. Creating a serverless index from a collection is not supported in earlier versions.
       * Set `dimension` to the same dimension as the pod-based index. Changing the dimension is not supported.
       * Set `cloud` to the cloud where the pod-based index is hosted. Migrating to a different cloud is not supported.
       * Set `source_collection` to the name of the collection you created in step 1.

       <CodeGroup>
         ```javascript JavaScript theme={null}
         import { Pinecone } from '@pinecone-database/pinecone'

         const pc = new Pinecone({
           apiKey: 'YOUR_API_KEY'
         });

         await pc.createIndex({
           name: 'serverless-index',
           vectorType: 'dense',
           dimension: 1536,
           metric: 'cosine',
           spec: {
             serverless: {
               cloud: 'aws',
               region: 'us-east-1',
               sourceCollection: 'pod-collection'
             }
           }
         });
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

             idx, err := pc.CreateServerlessIndex(ctx, &pinecone.CreateServerlessIndexRequest{
                 Name:      "serverless-index",
                 VectorType: "dense",
                 Dimension: 1536,
                 Metric:    pinecone.Cosine,
                 Cloud:     pinecone.Aws,
                 Region:    "us-east-1",
                 SourceCollection: "pod-collection",
             })
             if err != nil {
                 log.Fatalf("Failed to create serverless index: %v", err)
             } else {
                 fmt.Printf("Successfully created serverless index: %v", idx.Name)
             }
         }
         ```

         ```shell curl theme={null}
         PINECONE_API_KEY="YOUR_API_KEY"

         curl -s "https://api.pinecone.io/indexes" \
         -H "Accept: application/json" \
         -H "Content-Type: application/json" \
         -H "Api-Key: $PINECONE_API_KEY" \
         -H "X-Pinecone-API-Version: 2025-04" \
         -d '{
                 "name": "serverless-index",
                 "vector_type": "dense",
                 "dimension": 1536,
                 "metric": "cosine",
                 "spec": {
                     "serverless": {
                         "cloud": "aws",
                         "region": "us-east-1",
                         "source_collection": "pod-collection"
                     }
                 }
             }'
         ```
       </CodeGroup>
  </Tab>
</Tabs>


## 4. Update SDKs

If you are using an older version of the Python, Node.js, Java, or Go SDK, you must update the SDK to work with serverless indexes.

1. Check your SDK version:

   <CodeGroup>
     ```shell Python theme={null}
     pip show pinecone  
     ```

     ```shell JavaScript theme={null}
     npm list | grep @pinecone-database/pinecone  
     ```

     ```shell Java  theme={null}
     # Check your dependency file or classpath
     ```

     ```shell Go theme={null}
     go list -u -m all | grep go-pinecone
     ```
   </CodeGroup>

2. If your SDK version is less than 3.0.0 for [Python](https://github.com/pinecone-io/pinecone-python-client/blob/main/README.md), 2.0.0 for [Node.js](https://sdk.pinecone.io/typescript/), 1.0.0 for [Java](https://github.com/pinecone-io/pinecone-java-client), or 1.0.0 for [Go](https://github.com/pinecone-io/go-pinecone), upgrade the SDK as follows:

   <CodeGroup>
     ```Python Python theme={null}
     pip install "pinecone[grpc]" --upgrade  
     ```

     ```JavaScript JavaScript theme={null}
     npm install @pinecone-database/pinecone@latest  
     ```

     ```shell Java theme={null}
     # Maven
     <dependency>
       <groupId>io.pinecone</groupId>
       <artifactId>pinecone-client</artifactId>
       <version>5.0.0</version>
     </dependency>

     # Gradle
     implementation "io.pinecone:pinecone-client:5.0.0"
     ```

     ```go Go theme={null}
     go get -u github.com/pinecone-io/go-pinecone/v4/pinecone@latest
     ```
   </CodeGroup>

   If you are using the [.NET SDK](/reference/dotnet-sdk), add a package reference to your project file:

   ```shell C# theme={null}
   dotnet add package Pinecone.Client 
   ```


## 5. Adapt existing code

You must make some minor code changes to work with serverless indexes.

<Warning>
  Serverless indexes do not support some features, as outlined in [Limitations](#limitations). If you were relying on these features for your pod-based index, you’ll need to adapt your code.
</Warning>

1. Change how you import the Pinecone library and authenticate and initialize the client:

   <CodeGroup>
     ```Python Python theme={null}
     from pinecone.grpc import PineconeGRPC as Pinecone
     from pinecone import ServerlessSpec, PodSpec  
     # ServerlessSpec and PodSpec are required only when  
     # creating serverless and pod-based indexes.  
     pc = Pinecone(api_key="YOUR_API_KEY")  
     ```

     ```JavaScript JavaScript theme={null}
     import { Pinecone } from '@pinecone-database/pinecone';  

     const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });
     ```

     ```java Java theme={null}
     import io.pinecone.clients.Pinecone;
     import org.openapitools.db_control.client.model.*;

     public class InitializeClientExample {
         public static void main(String[] args) {
             Pinecone pc = new Pinecone.Builder("YOUR_API_KEY").build();
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
     }
     ```

     ```csharp C# theme={null}
     using Pinecone;

     var pinecone = new PineconeClient("YOUR_API_KEY");
     ```
   </CodeGroup>

2. [Listing indexes](/guides/manage-data/manage-indexes) now fetches a complete description of each index. If you were relying on the output of this operation, you'll need to adapt your code.

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

   The `list_indexes` operation now returns a response like the following:

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

3. [Describing an index](/guides/manage-data/manage-indexes) now returns a description of an index in a different format. It also returns the index host needed to run data plane operations against the index. If you were relying on the output of this operation, you'll need to adapt your code.

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


## 6. Use your new index

When you're ready to cutover to your new serverless index:

1. Your new serverless index has a different name and unique endpoint than your pod-based index. Update your code to target the new serverless index:

   <CodeGroup>
     ```Python Python theme={null}
     index = pc.Index("YOUR_SERVERLESS_INDEX_NAME")  
     ```

     ```JavaScript JavaScript theme={null}
     const index = pc.index("YOUR_SERVERLESS_INDEX_NAME");
     ```

     ```java Java theme={null}
     import io.pinecone.clients.Index;
     import io.pinecone.clients.Pinecone;

     public class TargetIndexExample {
         public static void main(String[] args) {
             Pinecone pc = new Pinecone.Builder("YOUR_API_KEY").build();
             Index index = pc.getIndexConnection("YOUR_SERVERLESS_INDEX_NAME");
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

         idx, err := pc.DescribeIndex(ctx, "YOUR_SERVERLESS_INDEX_NAME")
         if err != nil {
             log.Fatalf("Failed to describe index \"%v\": %v", idx.Name, err)
         }

         idxConnection, err := pc.Index(pinecone.NewIndexConnParams{Host: idx.Host, Namespace: "example-namespace"})
         if err != nil {
             log.Fatalf("Failed to create IndexConnection for Host %v: %v", idx.Host, err)
         }
     }
     ```

     ```csharp C# theme={null}
     using Pinecone;

     var pinecone = new PineconeClient("YOUR_API_KEY");

     var index = pinecone.Index("YOUR_SERVERLESS_INDEX_NAME");
     ```

     ```bash curl theme={null}
     # When using the API directly, you need the unique endpoint for your new serverless index. 
     # See https://docs.pinecone.io/guides/manage-data/target-an-index for details.
     PINECONE_API_KEY="YOUR_API_KEY"
     INDEX_HOST="INDEX_HOST"

     curl -X POST "https://$INDEX_HOST/describe_index_stats" \  
         -H "Api-Key: $PINECONE_API_KEY" \
         -H "X-Pinecone-API-Version: 2025-04" 
     ```
   </CodeGroup>

2. Reinitialize your clients.

3. If you logged writes to the pod-based index during migration, replay the logged writes to your serverless index.

4. [Delete the pod-based index](/guides/manage-data/manage-indexes#delete-an-index) to avoid paying for unused resources.

   <Warning>
     It is not possible to save a serverless index as a collection, so if you want to retain the option to recreate your pod-based index, be sure to keep the collection you created earlier.
   </Warning>


## See also

* [Limits](/reference/api/database-limits)
* [Serverless architecture](/guides/get-started/database-architecture)
* [Understanding serverless cost](/guides/manage-cost/understanding-cost)



---
**Navigation:** [← Previous](./04-indexing-overview.md) | [Index](./index.md) | [Next →](./06-restore-a-pod-based-index.md)
