**Navigation:** [← Previous](./05-this-is-grpc-client-aliased-as-pinecone.md) | [Index](./index.md) | [Next →](./07-back-up-an-index.md)

# Restore a pod-based index
Source: https://docs.pinecone.io/guides/indexes/pods/restore-a-pod-based-index

Restore pod-based indexes from collections

<Warning>
  Customers who sign up for a Standard or Enterprise plan on or after August 18, 2025 cannot create pod-based indexes. Instead, create [serverless indexes](/guides/index-data/create-an-index), and consider using [dedicated read nodes](/guides/index-data/dedicated-read-nodes) for large workloads (millions of records or more, and moderate or high query rates).
</Warning>

You can restore a pod-based index by creating a new index from a [collection](/guides/indexes/pods/understanding-collections).


## Create a pod-based index from a collection

To create a pod-based index from a [collection](/guides/manage-data/back-up-an-index#pod-based-index-backups-using-collections), use the [`create_index`](/reference/api/latest/control-plane/create_index) endpoint and provide a [`source_collection`](/reference/api/latest/control-plane/create_index#!path=source%5Fcollection\&t=request) parameter containing the name of the collection from which you wish to create an index. The new index can differ from the original source index: the new index can have a different name, number of pods, or pod type. The new index is queryable and writable.

<CodeGroup>
  ```Python Python theme={null}
  from pinecone.grpc import PineconeGRPC as Pinecone, PodSpec

  pc = Pinecone(api_key="YOUR_API_KEY")

  pc.create_index(
    name="docs-example",
    dimension=128,
    metric="cosine",
    spec=PodSpec(
      environment="us-west-1-gcp",
      pod_type="p1.x1",
      pods=1,
      source_collection="example-collection"
    )
  )
  ```

  ```JavaScript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({
    apiKey: 'YOUR_API_KEY'
  });

  await pc.createIndex({
    name: 'docs-example',
    dimension: 128,
    metric: 'cosine',
    spec: {
      pod: {
        environment: 'us-west-1-gcp',
        podType: 'p1.x1',
        pods: 1,
        sourceCollection: 'example-collection'
      }
    }
  });
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Pinecone;
  import org.openapitools.db_control.client.model.IndexModel;
  import org.openapitools.db_control.client.model.DeletionProtection;

  public class CreateIndexFromCollectionExample {
      public static void main(String[] args) {
          Pinecone pc = new Pinecone.Builder("YOUR_API_KEY").build();
          pc.createPodsIndex("docs-example", 1536, "us-west1-gcp",
                  "p1.x1", "cosine", "example-collection", DeletionProtection.DISABLED);
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
          SourceCollection:   "example-collection",
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
      Dimension = 1538,
      Metric = MetricType.Cosine,
      Spec = new PodIndexSpec
      {
          Pod = new PodSpec
          {
              Environment = "us-east1-gcp",
              PodType = "p1.x1",
              Pods = 1,
              Replicas = 1,
              Shards = 1,
              SourceCollection = "example-collection",
          }
      },
      DeletionProtection = DeletionProtection.Enabled,
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
           "dimension": 128,
           "metric": "cosine",
           "spec": {
              "pod": {
                 "environment": "us-west-1-gcp",
                 "pod_type": "p1.x1",
                 "pods": 1,
                 "source_collection": "example-collection"
              }
           }
        }'
  ```
</CodeGroup>



# Scale pod-based indexes
Source: https://docs.pinecone.io/guides/indexes/pods/scale-pod-based-indexes

Scale indexes vertically or horizontally as needed

<Warning>
  Customers who sign up for a Standard or Enterprise plan on or after August 18, 2025 cannot create pod-based indexes. Instead, create [serverless indexes](/guides/index-data/create-an-index), and consider using [dedicated read nodes](/guides/index-data/dedicated-read-nodes) for large workloads (millions of records or more, and moderate or high query rates).
</Warning>

While your index can still serve queries, new upserts may fail as the capacity becomes exhausted. If you need to scale your environment to accommodate more vectors, you can modify your existing index and scale it vertically or create a new index and scale horizontally.

This page explains how you can scale your [pod-based indexes](/guides/index-data/indexing-overview#pod-based-indexes) horizontally and vertically.


## Vertical vs. horizontal scaling

If you need to scale your environment to accommodate more vectors, you can modify your existing index to scale it vertically or create a new index and scale horizontally. This article will describe both methods and how to scale your index effectively.


## Vertical scaling

[Vertical scaling](https://www.pinecone.io/learn/testing-p2-collections-scaling/#vertical-scaling-on-p1-and-s1) is fast and involves no downtime. This is a good choice when you can't pause upserts and must continue serving traffic. It also allows you to double your capacity instantly. However, there are some factors to consider.

### Increase pod size

The default [pod size](/guides/index-data/indexing-overview#pod-size-and-performance) is `x1`. You can increase the size to `x2`, `x4`, or `x8`. Moving up to the next size effectively doubles the capacity of the index. If you need to scale by smaller increments, then consider horizontal scaling.

Increasing the pod size of your index does not result in downtime. Reads and writes continue uninterrupted during the scaling process, which completes in about 10 minutes. You cannot reduce the pod size of your indexes.

The number of base pods you specify when you initially create the index is static and cannot be changed. For example, if you start with 10 pods of `p1.x1` and vertically scale to `p1.x2`, this equates to 20 pods worth of usage. Pod types (performance versus storage pods) also cannot be changed with vertical scaling. If you want to change your pod type while scaling, then horizontal scaling is the better option.

#### When to increase pod size

If your index is at around 90% fullness, we recommend increasing its size. This helps ensure optimal performance and prevents upserts from failing due to capacity constraints.

#### How to increase pod size

You can increase the pod size in the Pinecone console or using the API.

<Tabs>
  <Tab title="Console">
    1. Open the [Pinecone console](https://app.pinecone.io/organizations/-/projects).
    2. Select the project containing the index you want to configure.
    3. Go to **Database > Indexes**.
    4. Select the index.
    5. Click the **...** button.
    6. Select **Configure**.
    7. In the dropdown, choose the pod size to use.
    8. Click **Confirm**.
  </Tab>

  <Tab title="API">
    Use the [`configure_index`](/reference/api/latest/control-plane/configure_index) operation and append the new size to the `pod_type` parameter, separated by a period (.).

    **Example**

    The following example assumes that `docs-example` has size `x1` and increases the size to `x2`.

    <CodeGroup>
      ```Python Python theme={null}
      from pinecone.grpc import PineconeGRPC as Pinecone

      pc = Pinecone(api_key="YOUR_API_KEY")

      pc.configure_index("docs-example", pod_type="s1.x2")
      ```

      ```JavaScript JavaScript theme={null}
      import { Pinecone } from '@pinecone-database/pinecone'

      const pinecone = new Pinecone({
        apiKey: 'YOUR_API_KEY'
      });

      await pc.configureIndex('docs-example', {
        spec: {
          pod: {
            podType: 's1.x2',
          },
        },
      });
      ```

      ```java Java theme={null}
      import io.pinecone.clients.Pinecone;

      public class ConfigureIndexExample {
          public static void main(String[] args) {
              Pinecone pc = new Pinecone.Builder("PINECONE_API_KEY").build();
              pc.configurePodsIndex("docs-example", "s1.x2");
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

          idx, err := pc.ConfigureIndex(ctx, "docs-example", pinecone.ConfigureIndexParams{PodType: "s1.x2"})
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
          Spec = new ConfigureIndexRequestSpec
          {
              Pod = new ConfigureIndexRequestSpecPod {
                  PodType = "s1.x2",
              }
          }
      });
      ```

      ```bash curl theme={null}
      PINECONE_API_KEY="YOUR_API_KEY"

      curl -s -X PATCH "https://api.pinecone.io/indexes/docs-example-curl" \
        -H "Content-Type: application/json" \
        -H "Api-Key: $PINECONE_API_KEY" \
        -H "X-Pinecone-API-Version: 2025-04" \
        -d '{
               "pod_type": "s1.x2"
            }'
      ```
    </CodeGroup>
  </Tab>
</Tabs>

<Note>
  The size change can take up to 15 minutes to complete.
</Note>

### Decrease pod size

After creating an index, you cannot vertically downscale the index/pod size. Instead, you must [create a collection](/guides/indexes/pods/back-up-a-pod-based-index) and then [create a new index from your collection](/guides/indexes/pods/restore-a-pod-based-index) and specify your desired pod size.

### Check the status of a pod size change

To check the status of a pod size change, use the [`describe_index`](/reference/api/latest/control-plane/describe_index/) endpoint. The `status` field in the results contains the key-value pair `"state":"ScalingUp"` or `"state":"ScalingDown"` during the resizing process and the key-value pair `"state":"Ready"` after the process is complete.

The index fullness metric provided by [`describe_index_stats`](/reference/api/latest/data-plane/describeindexstats) may be inaccurate until the resizing process is complete.

**Example**

The following example uses `describe_index` to get the index status of the index `docs-example`. The `status` field contains the key-value pair `"state":"ScalingUp"`, indicating that the resizing process is still ongoing.

<CodeGroup>
  ```Python Python theme={null}
  from pinecone.grpc import PineconeGRPC as Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  pc.describe_index(name="docs-example")
  ```

  ```JavaScript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({
    apiKey: 'YOUR_API_KEY'
  });

  await pc.describeIndex({
    name: "docs-example",
  });
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Pinecone;
  import org.openapitools.db_control.client.model.*;

  public class DescribeIndexExample {
      public static void main(String[] args) {
          Pinecone pc = new Pinecone.Builder("YOUR_API_KEY").build();
          IndexModel indexModel = pc.describeIndex("docs-example");
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

      idx, err := pc.DescribeIndex(ctx, "docs-example")
    	if err != nil {
          log.Fatalf("Failed to describe index %v: %v", idx.Name, err)
      } else {
          fmt.Printf("Successfully found index: %v", idx.Name)
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

  curl -s -X GET "https://api.pinecone.io/indexes/docs-example-curl" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-API-Version: 2025-04"
  ```
</CodeGroup>


## Horizontal scaling

There are two approaches to horizontal scaling in Pinecone: adding pods and adding replicas. Adding pods increases all resources but requires a pause in upserts; adding replicas only increases throughput and requires no pause in upserts.

### Add pods

Adding additional pods to a running index is not supported directly. However, you can increase the number of pods by using our [collections](/guides/indexes/pods/understanding-collections) feature to create a new index with more pods.

A collection is an immutable snapshot of your index in time: a collection stores the data but not the original index configuration. When you [create an index from a collection](/guides/indexes/pods/create-a-pod-based-index#create-a-pod-index-from-a-collection), you define the new index configuration. This allows you to scale the base pod count horizontally without scaling vertically.

The main advantage of this approach is that you can scale incrementally instead of doubling capacity as with vertical scaling. Also, you can redefine pod types if you are experimenting or if you need to use a different pod type, such as performance-optimized pods or storage-optimized pods. Another advantage of this method is that you can change your [metadata configuration](/guides/indexes/pods/manage-pod-based-indexes#selective-metadata-indexing) to redefine metadata fields as indexed or stored-only. This is important when tuning your index for the best throughput.

Here are the general steps to make a copy of your index and create a new index while changing the pod type, pod count, metadata configuration, replicas, and all typical parameters when creating a new collection:

1. Pause upserts.
2. Create a collection from the current index.
3. Create an index from the collection with new parameters.
4. Continue upserts to the newly created index. Note: the URL has likely changed.
5. Delete the old index if desired.

For detailed steps on creating the collection, see [backup indexes](/guides/manage-data/back-up-an-index#create-a-backup-using-a-collection). For steps on creating an index from a collection, see [Create an index from a collection](/guides/indexes/pods/create-a-pod-based-index#create-a-pod-index-from-a-collection).

### Add replicas

Each replica duplicates the resources and data in an index. This means that adding additional replicas increases the throughput of the index but not its capacity. However, adding replicas does not require downtime.

Throughput in terms of queries per second (QPS) scales linearly with the number of replicas per index.

#### When to add replicas

There are two primary scenarios where adding replicas is beneficial:

**Increase QPS**: The primary reason to add replicas is to increase your index's queries per second (QPS). Each new replica adds another pod for reading from your index and, generally speaking, will increase your QPS by an equal amount as a single pod. For example, if you consistently get 25 QPS for a single pod, each replica will result in 25 more QPS.

If you don't see an increase in QPS after adding replicas, add multiprocessing to your application to ensure you are running parallel operations. You can use the [Pinecone gRPC SDK](/guides/index-data/upsert-data#grpc-python-sdk), or your multiprocessing library of choice.

**Provide data redundancy**: When you add a replica to your index, the Pinecone controller will choose a zone in the same region that does not currently have a replica, up to a maximum of three zones (your fourth and subsequent replicas will be hosted in zones with existing replicas). If your application requires multizone redundancy, this is our recommended approach to achieve that.

#### How to add replicas

To add replicas, use the `configure_index` endpoint to increase the number of replicas for your index:

<CodeGroup>
  ```Python Python theme={null}
  from pinecone.grpc import PineconeGRPC as Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  pc.configure_index("docs-example", replicas=4)
  ```

  ```JavaScript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({
    apiKey: 'YOUR_API_KEY'
  });

  await pc.configureIndex('docs-example', {
    spec: {
      pod: {
        replicas: 4,
      },
    },
  });
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Pinecone;

  public class ConfigureIndexExample {
      public static void main(String[] args) {
          Pinecone pc = new Pinecone.Builder("PINECONE_API_KEY").build();
          pc.configurePodsIndex("docs-example", 4, DeletionProtection.DISABLED);
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

      idx, err := pc.ConfigureIndex(ctx, "docs-example", pinecone.ConfigureIndexParams{Replicas: 4})
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
      Spec = new ConfigureIndexRequestSpec
      {
          Pod = new ConfigureIndexRequestSpecPod {
              Replicas = 4,
          }
      }
  });
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl -s -X PATCH "https://api.pinecone.io/indexes/docs-example-curl" \
    -H "Content-Type: application/json" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-API-Version: 2025-04" \
    -d '{
           "replicas": 4
        }'
  ```
</CodeGroup>


## Next steps

* See our learning center for more information on [vertical scaling](https://www.pinecone.io/learn/testing-p2-collections-scaling/#vertical-scaling-on-p1-and-s1).
* Learn more about [collections](/guides/indexes/pods/understanding-collections).



# Understanding collections
Source: https://docs.pinecone.io/guides/indexes/pods/understanding-collections

Create static backups of pod-based indexes with collections

<Warning>
  Customers who sign up for a Standard or Enterprise plan on or after August 18, 2025 cannot create pod-based indexes. Instead, create [serverless indexes](/guides/index-data/create-an-index), and consider using [dedicated read nodes](/guides/index-data/dedicated-read-nodes) for large workloads (millions of records or more, and moderate or high query rates).
</Warning>

A collection is a static copy of a pod-based index that only consumes storage. It is a non-queryable representation of a set of records. You can [create a collection](/guides/indexes/pods/back-up-a-pod-based-index) of a pod-based index, and you can [create a new pod-based index from a collection](/guides/manage-data/restore-an-index). This allows you to restore the index with the same or different configurations.

<Note>
  Once a collection is created, it cannot be moved to a different project.
</Note>

<PuPr />


## Use cases

Creating a collection is useful when performing tasks like the following:

* Protecting an index from manual or system failures.
* Temporarily shutting down an index.
* Copying the data from one index into a different index.
* Making a backup of your index.
* Experimenting with different index configurations.


## Performance

Collections operations perform differently, depending on the pod type of the index:

* Creating a `p1` or `s1` index from a collection takes approximately 10 minutes.
* Creating a `p2` index from a collection can take several hours when the number of vectors is on the order of 1,000,000.


## Limitations

Collection limitations are as follows:

* You can only perform operations on collections in the current Pinecone project.


## Pricing

See [Pricing](https://www.pinecone.io/pricing/) for up-to-date pricing information.



# Understanding pod-based indexes
Source: https://docs.pinecone.io/guides/indexes/pods/understanding-pod-based-indexes

Learn about pod-based index architecture and types

<Warning>
  Customers who sign up for a Standard or Enterprise plan on or after August 18, 2025 cannot create pod-based indexes. Instead, create [serverless indexes](/guides/index-data/create-an-index), and consider using [dedicated read nodes](/guides/index-data/dedicated-read-nodes) for large workloads (millions of records or more, and moderate or high query rates).
</Warning>

With pod-based indexes, you choose one or more pre-configured units of hardware (pods). Depending on the pod type, pod size, and number of pods used, you get different amounts of storage and higher or lower latency and throughput. Be sure to [choose an appropriate pod type and size](/guides/indexes/pods/choose-a-pod-type-and-size) for your dataset and workload.


## Pod types

Different pod types are priced differently. See [Understanding cost](/guides/manage-cost/understanding-cost) for more details.

<Note>
  Once a pod-based index is created, you cannot change its pod type. However, you can create a collection from an index and then [create a new index with a different pod type](/guides/indexes/pods/create-a-pod-based-index#create-a-pod-index-from-a-collection) from the collection.
</Note>

### s1 pods

These storage-optimized pods provide large storage capacity and lower overall costs with slightly higher query latencies than p1 pods. They are ideal for very large indexes with moderate or relaxed latency requirements.

Each s1 pod has enough capacity for around 5M vectors of 768 dimensions.

### p1 pods

These performance-optimized pods provide very low query latencies, but hold fewer vectors per pod than s1 pods. They are ideal for applications with low latency requirements (\<100ms).

Each p1 pod has enough capacity for around 1M vectors of 768 dimensions.

### p2 pods

The p2 pod type provides greater query throughput with lower latency. For vectors with fewer than 128 dimension and queries where `topK` is less than 50, p2 pods support up to 200 QPS per replica and return queries in less than 10ms. This means that query throughput and latency are better than s1 and p1.

Each p2 pod has enough capacity for around 1M vectors of 768 dimensions. However, capacity may vary with dimensionality.

The data ingestion rate for p2 pods is significantly slower than for p1 pods; this rate decreases as the number of dimensions increases. For example, a p2 pod containing vectors with 128 dimensions can upsert up to 300 updates per second; a p2 pod containing vectors with 768 dimensions or more supports upsert of 50 updates per second. Because query latency and throughput for p2 pods vary from p1 pods, test p2 pod performance with your dataset.

The p2 pod type does not support sparse vector values.


## Pod size and performance

Each pod type supports four pod sizes: `x1`, `x2`, `x4`, and `x8`. Your index storage and compute capacity doubles for each size step. The default pod size is `x1`. You can increase the size of a pod after index creation.

To learn about changing the pod size of an index, see [Configure an index](/guides/indexes/pods/scale-pod-based-indexes#increase-pod-size).


## Pod environments

When creating a pod-based index, you must choose the cloud environment where you want the index to be hosted. The project environment can affect your [pricing](https://pinecone.io/pricing). The following table lists the available cloud regions and the corresponding values of the `environment` parameter for the [`create_index`](/guides/index-data/create-an-index#create-a-pod-based-index) endpoint:

| Cloud | Region                       | Environment                   |
| ----- | ---------------------------- | ----------------------------- |
| GCP   | us-west-1 (N. California)    | `us-west1-gcp`                |
| GCP   | us-central-1 (Iowa)          | `us-central1-gcp`             |
| GCP   | us-west-4 (Las Vegas)        | `us-west4-gcp`                |
| GCP   | us-east-4 (Virginia)         | `us-east4-gcp`                |
| GCP   | northamerica-northeast-1     | `northamerica-northeast1-gcp` |
| GCP   | asia-northeast-1 (Japan)     | `asia-northeast1-gcp`         |
| GCP   | asia-southeast-1 (Singapore) | `asia-southeast1-gcp`         |
| GCP   | us-east-1 (South Carolina)   | `us-east1-gcp`                |
| GCP   | eu-west-1 (Belgium)          | `eu-west1-gcp`                |
| GCP   | eu-west-4 (Netherlands)      | `eu-west4-gcp`                |
| AWS   | us-east-1 (Virginia)         | `us-east-1-aws`               |
| Azure | eastus (Virginia)            | `eastus-azure`                |

[Contact us](http://www.pinecone.io/contact/) if you need a dedicated deployment in other regions.

The environment cannot be changed after the index is created.


## Pod costs

For each pod-based index, billing is determined by the per-minute price per pod and the number of pods the index uses, regardless of index activity. The per-minute price varies by pod type, pod size, account plan, and cloud region. For the latest pod-based index pricing rates, see [Pricing](https://www.pinecone.io/pricing/pods).

Total cost depends on a combination of factors:

* **Pod type.** Each pod type has different per-minute pricing.
* **Number of pods.** This includes replicas, which duplicate pods.
* **Pod size.**  Larger pod sizes have proportionally higher costs per minute.
* **Total pod-minutes.** This includes the total time each pod is running, starting at pod creation and rounded up to 15-minute increments.
* **Cloud provider.** The cost per pod-type and pod-minute varies depending on the cloud provider you choose for your project.
* **Collection storage.** Collections incur costs per GB of data per minute in storage, rounded up to 15-minute increments.
* **Plan.** The free plan incurs no costs; the Standard or Enterprise plans incur different costs per pod-type, pod-minute, cloud provider, and collection storage.

The following equation calculates the total costs accrued over time:

```
(Number of pods) * (pod size) * (number of replicas) * (minutes pod exists) * (pod price per minute) 
+ (collection storage in GB) * (collection storage time in minutes) * (collection storage price per GB per minute)
```

To see a calculation of your current usage and costs, go to [**Settings > Usage**](https://app.pinecone.io/organizations/-/settings/usage) in the Pinecone console.

<Accordion title="Example">
  While our pricing page lists rates on an hourly basis for ease of comparison, this example lists prices per minute, as this is how Pinecone calculates billing.

  An example application has the following requirements:

  * 1,000,000 vectors with 1536 dimensions
  * 150 queries per second with `top_k` = 10
  * Deployment in an EU region
  * Ability to store 1GB of inactive vectors

  [Based on these requirements](/guides/indexes/pods/choose-a-pod-type-and-size), the organization chooses to configure the project to use the Standard billing plan to host one `p1.x2` pod with three replicas and a collection containing 1 GB of data. This project runs continuously for the month of January on the Standard plan. The components of the total cost for this example are given in Table 1 below:

  **Table 1: Example billing components**

  | Billing component             | Value        |
  | ----------------------------- | ------------ |
  | Number of pods                | 1            |
  | Number of replicas            | 3            |
  | Pod size                      | x2           |
  | Total pod count               | 6            |
  | Minutes in January            | 44,640       |
  | Pod-minutes (pods \* minutes) | 267,840      |
  | Pod price per minute          | \$0.0012     |
  | Collection storage            | 1 GB         |
  | Collection storage minutes    | 44,640       |
  | Price per storage minute      | \$0.00000056 |

  The invoice for this example is given in Table 2 below:

  **Table 2: Example invoice**

  | Product       | Quantity | Price per unit | Charge   |
  | ------------- | -------- | -------------- | -------- |
  | Collections   | 44,640   | \$0.00000056   | \$0.025  |
  | P2 Pods (AWS) | 0        |                | \$0.00   |
  | P2 Pods (GCP) | 0        |                | \$0.00   |
  | S1 Pods       | 0        |                | \$0.00   |
  | P1 Pods       | 267,840  | \$0.0012       | \$514.29 |

  Amount due \$514.54
</Accordion>


## Known limitations

* [Pod storage capacity](#pod-types)
  * Each **p1** pod has enough capacity for 1M vectors with 768 dimensions.
  * Each **s1** pod has enough capacity for 5M vectors with 768 dimensions.
* [Metadata](/guides/index-data/indexing-overview#metadata)
  * Metadata with high cardinality, such as a unique value for every vector in a large index, uses more memory than expected and can cause the pods to become full.
* [Collections](/guides/manage-data/back-up-an-index#pod-based-index-backups-using-collections)
  * You cannot query or write to a collection after its creation. For this reason, a collection only incurs storage costs.
  * You can only perform operations on collections in the current Pinecone project.
* [Sparse-dense vectors](/guides/search/hybrid-search#use-a-single-hybrid-index)
  * Only `s1` and `p1` [pod-based indexes](/guides/indexes/pods/understanding-pod-based-indexes#pod-types) using the dotproduct distance metric support sparse-dense vectors.



# Manage cost
Source: https://docs.pinecone.io/guides/manage-cost/manage-cost

Learn strategies for managing cost in Pinecone.

For the latest pricing details, see our [pricing page](https://www.pinecone.io/pricing/).

For help estimating total cost, see [Understanding cost](/guides/manage-cost/understanding-cost). To view or download a detailed report of your current usage and costs, see [Monitor usage and costs](/guides/manage-cost/monitor-usage-and-costs#monitor-organization-level-usage).


## Set monthly spend alerts

You can set up email alerts to monitor your organization's monthly spending. These alerts notify designated recipients when spending reaches specified thresholds. The alerts automatically reset at the start of each monthly billing cycle.

To set a spend alert:

1. Go to [Settings > Spend alerts](https://app.pinecone.io/organizations/-/settings/spend-alerts) in the Pinecone console
2. Click **+ Add Alert**.
3. Enter the dollar amount for the spend alert.
4. Enter the email addresses to send the alert to. [Organization owners](/guides/organizations/understanding-organizations#organization-roles) are listed by default.
5. Click **Create**.

To edit a spend alert:

1. In the row of the spend alert you want to edit, click **ellipsis (...) menu > Edit**.
2. Change the dollar amount and/or email addresses for the spend alert.
3. Click **Update**.

<Note>
  **Auto-spend spike alert**: To protect from unexpected cost increases, Pinecone sends an alert when spending exceeds double your previous month's invoice amount. While the alert threshold is fixed and the alert cannot be deleted, you can modify which email addresses receive the alert and enable or disable the alert notifications.
</Note>


## List by ID prefix

By using a [hierarchical ID schema](/guides/index-data/data-modeling#use-structured-ids), you can retrieve records without performing a query. To do so, you can use [`list`](/reference/api/latest/data-plane/list) to retrieve records by ID prefix, then use `fetch` to retrieve the records you need. This can reduce costs, because [`query` consumes more RUs when scanning a larger namespace](/guides/manage-cost/understanding-cost#query), while [`fetch` consumes a fixed ratio of RUs to records retrieved](/guides/manage-cost/understanding-cost#fetch).


## Use namespaces for multitenancy

If your application requires you to isolate the data of each customer/user, consider [implementing multitenancy with serverless indexes and namespaces](/guides/index-data/implement-multitenancy). With serverless indexes, you pay only for the amount of data stored and operations performed. For queries in particular, the cost is partly based on the total number of records that must be scanned, so using namespaces can significantly reduce query costs.


## Commit to annual spend

Users who commit to an annual contract may qualify for discounted rates. To learn more, [contact Pinecone sales](https://www.pinecone.io/contact/).


## Talk to support

Users on Standard and Enterprise plans can [contact Support](https://app.pinecone.io/organizations/-/settings/support/ticket) for help in optimizing costs.


## See also

* [Understanding cost](/guides/manage-cost/understanding-cost)
* [Monitor usage and costs](/guides/manage-cost/monitor-usage-and-costs)



# Monitor usage and costs
Source: https://docs.pinecone.io/guides/manage-cost/monitor-usage-and-costs

Monitor usage and costs for your Pinecone organization and indexes.


## Monitor organization-level usage and costs

<Note>
  To view usage and costs across your Pinecone organization, you must be an [organization owner](/guides/organizations/understanding-organizations#organization-owners). Also, this feature is available only to organizations on the Standard or Enterprise plans.
</Note>

The **Usage** dashboard in the Pinecone console gives you a detailed report of usage and costs across your organization, broken down by each billable SKU or aggregated by project or service. You can view the report in the console or download it as a CSV file for more detailed analysis.

1. Go to [**Settings > Usage**](https://app.pinecone.io/organizations/-/settings/usage) in the Pinecone console.
2. Select the time range to report on. This defaults to the last 30 days.
3. Select the scope for your report:
   * **SKU:** The usage and cost for each billable SKU, for example, read units per cloud region, storage size per cloud region, or tokens per embedding model.
   * **Project:** The aggregated cost for each project in your organization.
   * **Service:** The aggregated cost for each service your organization uses, for example, database (includes serverless back up and restore), assistants, inference (embedding and reranking), and collections.
4. Choose the specific SKUs, projects, or services you want to report on. This defaults to all.
5. To download the report as a CSV file, click **Download**.

   <Tip>
     The CSV download provides more granular detail than the console view, including breakdowns by individual index as well as project and index tags.
   </Tip>

Dates are shown in UTC to match billing invoices. Cost data is delayed up to three days from the actual usage date.


## Monitor index-level usage

You can monitor index-level usage directly in the Pinecone console, or you can pull them into [Prometheus](https://prometheus.io/). For more details, see [Monitoring](/guides/production/monitoring).


## Monitor operation-level usage

### Read units

[Query](/guides/search/search-overview), [fetch](/guides/manage-data/fetch-data), and [list by ID](/guides/manage-data/list-record-ids) requests return a `usage` parameter with the [read unit](/guides/manage-cost/understanding-cost#read-units) consumption of each request that is made.

<Warning>
  While Pinecone tracks read unit usage with decimal precision, the Pinecone API and SDKs round these values up to the nearest whole number in query, fetch, and list responses. For example, if a query uses 0.45 read units, the API and SDKs will report it as 1 read unit.

  For precise read unit reporting, see [index-level metrics](/guides/production/monitoring) or the organization-wide [Usage dashboard](/guides/manage-cost/monitor-usage-and-costs#monitor-organization-level-usage-and-costs).
</Warning>

Example query request:

<CodeGroup>
  ```Python Python theme={null}
  from pinecone.grpc import PineconeGRPC as Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")
  index = pc.Index("example-index")

  response = index.query(
      vector=[0.22,0.43,0.16,1,...], 
      namespace='example-namespace', 
      top_k=3,
      include_values=False,
      include_metadata=False
  )

  print(response)
  ```

  ```JavaScript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({ apiKey: "YOUR_API_KEY" })
  const index = pc.index("example-index")

  const queryResponse = await index.namespace('example-namespace').query({
      vector: [0.22,0.43,0.16,1,...],
      topK: 3,
      includeValues: false,
      includeMetadata: false,
  });

  console.log(queryResponse);
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Index;
  import io.pinecone.configs.PineconeConfig;
  import io.pinecone.configs.PineconeConnection;
  import io.pinecone.unsigned_indices_model.QueryResponseWithUnsignedIndices;

  import java.util.Arrays;
  import java.util.List;

  public class QueryByVector {
      public static void main(String[] args) {
          PineconeConfig config = new PineconeConfig("YOUR_API_KEY");
          // To get the unique host for an index,
          // see https://docs.pinecone.io/guides/manage-data/target-an-index
          config.setHost("INDEX_HOST");
          PineconeConnection connection = new PineconeConnection(config);
          Index index = new Index(config, connection, "example-index");

          List<Float> query = Arrays.asList(0.22f,0.43f,0.16f,1f,...);
          QueryResponseWithUnsignedIndices queryResponse = index.query(3, query, null, null, null, "example-namespace", null, false, false);
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

  	queryVector := []float32{0.22, 0.43, 0.16, 1, ...}

  	res, err := idxConnection.QueryByVectorValues(ctx, &pinecone.QueryByVectorValuesRequest{
  		Vector:        queryVector,
  		TopK:          3,
  		IncludeValues: false,
  	})
  	if err != nil {
  		log.Fatalf("Error encountered when querying by vector: %v", err)
  	} else {
  		fmt.Printf(prettifyStruct(res))
  	}
  ```

  ```csharp C# theme={null}
  using Pinecone;

  var pinecone = new PineconeClient("YOUR_API_KEY");

  // To get the unique host for an index, 
  // see https://docs.pinecone.io/guides/manage-data/target-an-index
  var index = pinecone.Index(host: "INDEX_HOST");

  var queryResponse = await index.QueryAsync(new QueryRequest {
      Vector = new[] { 0.22f,0.43f,0.16f,1f,... },
      Namespace = "example-namespace",
      TopK = 3,
      IncludeMetadata = false,
  });
  ```
</CodeGroup>

The response looks like this:

<CodeGroup>
  ```python Python theme={null}
  {'matches': [{'id': 'record_193027', 'score': 0.00405937387, 'values': []},
               {'id': 'record_137452', 'score': 0.00405937387, 'values': []},
               {'id': 'record_132264', 'score': 0.00405937387, 'values': []}],
   'namespace': 'example-namespace',
   'usage': {'read_units': 1}}
  ```

  ```javascript JavaScript theme={null}
  {
    matches: [
      {
        id: 'record_186225',
        score: 0.00405937387,
        values: [],
        sparseValues: undefined,
        metadata: undefined
      },
      {
        id: 'record_164994',
        score: 0.00405937387,
        values: [],
        sparseValues: undefined,
        metadata: undefined
      },
      {
        id: 'record_186333',
        score: 0.00405937387,
        values: [],
        sparseValues: undefined,
        metadata: undefined
      }
    ],
    namespace: 'example-namespace',
    usage: { readUnits: 1 }
  }
  ```

  ```java Java theme={null}
  class QueryResponseWithUnsignedIndices {
      matches: [ScoredVectorWithUnsignedIndices {
          score: 0.004059374
          id: record_170370
          values: []
          metadata: 
          sparseValuesWithUnsignedIndices: SparseValuesWithUnsignedIndices {
              indicesWithUnsigned32Int: []
              values: []
          }
      }, ScoredVectorWithUnsignedIndices {
          score: 0.004059374
          id: record_107423
          values: []
          metadata: 
          sparseValuesWithUnsignedIndices: SparseValuesWithUnsignedIndices {
              indicesWithUnsigned32Int: []
              values: []
          }
      }, ScoredVectorWithUnsignedIndices {
          score: 0.004059374
          id: record_171426
          values: []
          metadata: 
          sparseValuesWithUnsignedIndices: SparseValuesWithUnsignedIndices {
              indicesWithUnsigned32Int: []
              values: []
          }
      }]
      namespace: example-index
      usage: read_units: 1
  }
  ```

  ```go Go theme={null}
  {
    "matches": [
      {
        "vector": {
          "id": "record_193027"
        },
        "score": 0.004059374
      },
      {
        "vector": {
          "id": "record_137452"
        },
        "score": 0.004059374
      },
      {
        "vector": {
          "id": "record_132264"
        },
        "score": 0.004059374
      }
    ],
    "usage": {
      "read_units": 1
    },
    "namespace": "example-index"
  }
  ```

  ```csharp C# theme={null}
  {
    "results": [],
    "matches": [
      {
        "id": "record_193027",
        "score": 0.004059374,
        "values": []
      },
      {
        "id": "record_137452",
        "score": 0.004059374,
        "values": []
      },
      {
        "id": "record_132264",
        "score": 0.004059374,
        "values": []
      }
    ],
    "namespace": "example-namespace",
    "usage": {
      "readUnits": 1
    }
  }
  ```
</CodeGroup>

For a more in-depth demonstration of how to use read units to inspect read costs, see [this notebook](https://github.com/pinecone-io/examples/blob/master/docs/read-units-demonstrated.ipynb).

### Embedding tokens

Requests to one of [Pinecone's hosted embedding models](/guides/index-data/create-an-index#embedding-models), either directly via the [`embed` operation](/reference/api/latest/inference/generate-embeddings) or automatically when upserting or querying an [index with integrated embedding](/guides/index-data/indexing-overview#integrated-embedding), return a `usage` parameter with the total tokens generated.

For example, the following request to use the `multilingual-e5-large` model to generate embeddings for sentences related to the word “apple” might return this request and summary of embedding tokens generated:

<CodeGroup>
  ```python Python theme={null}
  # Import the Pinecone library
  from pinecone.grpc import PineconeGRPC as Pinecone
  from pinecone import ServerlessSpec
  import time

  # Initialize a Pinecone client with your API key
  pc = Pinecone(api_key="YOUR_API_KEY")

  # Define a sample dataset where each item has a unique ID and piece of text
  data = [
      {"id": "vec1", "text": "Apple is a popular fruit known for its sweetness and crisp texture."},
      {"id": "vec2", "text": "The tech company Apple is known for its innovative products like the iPhone."},
      {"id": "vec3", "text": "Many people enjoy eating apples as a healthy snack."},
      {"id": "vec4", "text": "Apple Inc. has revolutionized the tech industry with its sleek designs and user-friendly interfaces."},
      {"id": "vec5", "text": "An apple a day keeps the doctor away, as the saying goes."},
      {"id": "vec6", "text": "Apple Computer Company was founded on April 1, 1976, by Steve Jobs, Steve Wozniak, and Ronald Wayne as a partnership."}
  ]

  # Convert the text into numerical vectors that Pinecone can index
  embeddings = pc.inference.embed(
      model="llama-text-embed-v2",
      inputs=[d['text'] for d in data],
      parameters={"input_type": "passage", "truncate": "END"}
  )

  print(embeddings)
  ```

  ```javascript JavaScript theme={null}
  // Import the Pinecone library
  import { Pinecone } from '@pinecone-database/pinecone';

  // Initialize a Pinecone client with your API key
  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  // Define a sample dataset where each item has a unique ID and piece of text
  const data = [
    { id: 'vec1', text: 'Apple is a popular fruit known for its sweetness and crisp texture.' },
    { id: 'vec2', text: 'The tech company Apple is known for its innovative products like the iPhone.' },
    { id: 'vec3', text: 'Many people enjoy eating apples as a healthy snack.' },
    { id: 'vec4', text: 'Apple Inc. has revolutionized the tech industry with its sleek designs and user-friendly interfaces.' },
    { id: 'vec5', text: 'An apple a day keeps the doctor away, as the saying goes.' },
    { id: 'vec6', text: 'Apple Computer Company was founded on April 1, 1976, by Steve Jobs, Steve Wozniak, and Ronald Wayne as a partnership.' }
  ];

  // Convert the text into numerical vectors that Pinecone can index
  const model = 'llama-text-embed-v2';

  const embeddings = await pc.inference.embed(
    model,
    data.map(d => d.text),
    { inputType: 'passage', truncate: 'END' }
  );

  console.log(embeddings);
  ```

  ```java Java theme={null}
  // Import the required classes
  import io.pinecone.clients.Index;
  import io.pinecone.clients.Inference;
  import io.pinecone.clients.Pinecone;
  import org.openapitools.inference.client.ApiException;
  import org.openapitools.inference.client.model.Embedding;
  import org.openapitools.inference.client.model.EmbeddingsList;

  import java.math.BigDecimal;
  import java.util.*;
  import java.util.stream.Collectors;

  public class GenerateEmbeddings {
      public static void main(String[] args) throws ApiException {
          // Initialize a Pinecone client with your API key
          Pinecone pc = new Pinecone.Builder("YOUR_API_KEY").build();
          Inference inference = pc.getInferenceClient();

          // Prepare input sentences to be embedded
          List<DataObject> data = Arrays.asList(
              new DataObject("vec1", "Apple is a popular fruit known for its sweetness and crisp texture."),
              new DataObject("vec2", "The tech company Apple is known for its innovative products like the iPhone."),
              new DataObject("vec3", "Many people enjoy eating apples as a healthy snack."),
              new DataObject("vec4", "Apple Inc. has revolutionized the tech industry with its sleek designs and user-friendly interfaces."),
              new DataObject("vec5", "An apple a day keeps the doctor away, as the saying goes."),
              new DataObject("vec6", "Apple Computer Company was founded on April 1, 1976, by Steve Jobs, Steve Wozniak, and Ronald Wayne as a partnership.")
          );

          List<String> inputs = data.stream()
              .map(DataObject::getText)
              .collect(Collectors.toList());

          // Specify the embedding model and parameters
          String embeddingModel = "llama-text-embed-v2";

          Map<String, Object> parameters = new HashMap<>();
          parameters.put("input_type", "passage");
          parameters.put("truncate", "END");

          // Generate embeddings for the input data
          EmbeddingsList embeddings = inference.embed(embeddingModel, parameters, inputs);

          // Get embedded data
          List<Embedding> embeddedData = embeddings.getData();
      }

      private static List<Float> convertBigDecimalToFloat(List<BigDecimal> bigDecimalValues) {
          return bigDecimalValues.stream()
              .map(BigDecimal::floatValue)
              .collect(Collectors.toList());
      }
  }

  class DataObject {
      private String id;
      private String text;

      public DataObject(String id, String text) {
          this.id = id;
          this.text = text;
      }

      public String getId() {
          return id;
      }
      public String getText() {
          return text;
      }
  }
  ```

  ```go Go theme={null}
  package main

  // Import the required packages
  import (
      "context"
     	"encoding/json"
      "fmt"
      "log"

      "github.com/pinecone-io/go-pinecone/v4/pinecone"
  )

  type Data struct {
      ID   string
      Text string
  }

  type Query struct {
  	Text string
  }

  func prettifyStruct(obj interface{}) string {
      bytes, _ := json.MarshalIndent(obj, "", "  ")
      return string(bytes)
  }

  func main() {
      ctx := context.Background()

      // Initialize a Pinecone client with your API key
      pc, err := pinecone.NewClient(pinecone.NewClientParams{
          ApiKey: "YOUR_API_KEY",
      })
      if err != nil {
          log.Fatalf("Failed to create Client: %v", err)
      }

      // Define a sample dataset where each item has a unique ID and piece of text
      data := []Data{
          {ID: "vec1", Text: "Apple is a popular fruit known for its sweetness and crisp texture."},
          {ID: "vec2", Text: "The tech company Apple is known for its innovative products like the iPhone."},
          {ID: "vec3", Text: "Many people enjoy eating apples as a healthy snack."},
          {ID: "vec4", Text: "Apple Inc. has revolutionized the tech industry with its sleek designs and user-friendly interfaces."},
          {ID: "vec5", Text: "An apple a day keeps the doctor away, as the saying goes."},
          {ID: "vec6", Text: "Apple Computer Company was founded on April 1, 1976, by Steve Jobs, Steve Wozniak, and Ronald Wayne as a partnership."},
      }

      // Specify the embedding model and parameters
      embeddingModel := "llama-text-embed-v2"

      docParameters := pinecone.EmbedParameters{
          InputType: "passage",
          Truncate:  "END",
      }

      // Convert the text into numerical vectors that Pinecone can index
      var documents []string
      for _, d := range data {
          documents = append(documents, d.Text)
      }

      docEmbeddingsResponse, err := pc.Inference.Embed(ctx, &pinecone.EmbedRequest{
          Model:      embeddingModel,
          TextInputs: documents,
          Parameters: docParameters,
      }) 
      if err != nil {
          log.Fatalf("Failed to embed documents: %v", err)
      } else {
          fmt.Printf(prettifyStruct(docEmbeddingsResponse))
      }
  }
  ```

  ```csharp C# theme={null}
  using Pinecone;
  using System;
  using System.Collections.Generic;

  // Initialize a Pinecone client with your API key
  var pinecone = new PineconeClient("YOUR_API_KEY");

  // Prepare input sentences to be embedded
  var data = new[]
  {
      new
      {
          Id = "vec1",
          Text = "Apple is a popular fruit known for its sweetness and crisp texture."
      },
      new
      {
          Id = "vec2",
          Text = "The tech company Apple is known for its innovative products like the iPhone."
      },
      new
      {
          Id = "vec3",
          Text = "Many people enjoy eating apples as a healthy snack."
      },
      new
      {
          Id = "vec4",
          Text = "Apple Inc. has revolutionized the tech industry with its sleek designs and user-friendly interfaces."
      },
      new
      {
          Id = "vec5",
          Text = "An apple a day keeps the doctor away, as the saying goes."
      },
      new
      {
          Id = "vec6",
          Text = "Apple Computer Company was founded on April 1, 1976, by Steve Jobs, Steve Wozniak, and Ronald Wayne as a partnership."
      }
  };

  // Specify the embedding model and parameters
  var embeddingModel = "llama-text-embed-v2";

  // Generate embeddings for the input data
  var embeddings = await pinecone.Inference.EmbedAsync(new EmbedRequest
  {
      Model = embeddingModel,
      Inputs = data.Select(item => new EmbedRequestInputsItem { Text = item.Text }),
      Parameters = new Dictionary<string, object?>
      {
          ["input_type"] = "passage",
          ["truncate"] = "END"
      }
  });

  Console.WriteLine(embeddings);
  ```

  ```shell curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl https://api.pinecone.io/embed \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -H "X-Pinecone-API-Version: 2025-04" \
    -d '{
        "model": "llama-text-embed-v2",
        "parameters": {
          "input_type": "passage",
          "truncate": "END"
        },
        "inputs": [
          {"text": "Apple is a popular fruit known for its sweetness and crisp texture."},
          {"text": "The tech company Apple is known for its innovative products like the iPhone."},
          {"text": "Many people enjoy eating apples as a healthy snack."},
          {"text": "Apple Inc. has revolutionized the tech industry with its sleek designs and user-friendly interfaces."},
          {"text": "An apple a day keeps the doctor away, as the saying goes."},
          {"text": "Apple Computer Company was founded on April 1, 1976, by Steve Jobs, Steve Wozniak, and Ronald Wayne as a partnership."}
        ]
    }'
  ```
</CodeGroup>

The returned object looks like this:

<CodeGroup>
  ```python Python theme={null}
  EmbeddingsList(
      model='llama-text-embed-v2',
      data=[
          {'values': [0.04925537109375, -0.01313018798828125, -0.0112762451171875, ...]},
          ...
      ],
      usage={'total_tokens': 130}
  )
  ```

  ```javascript JavaScript theme={null}
  EmbeddingsList(1) [
    {
      values: [
        0.04925537109375, 
        -0.01313018798828125, 
        -0.0112762451171875,
        ...
      ]
    },
    ...
    model: 'llama-text-embed-v2',
    data: [ { values: [Array] } ],
    usage: { totalTokens: 130 }
  ]
  ```

  ```java Java theme={null}
  class EmbeddingsList {
      model: llama-text-embed-v2
      data: [class Embedding {
          values: [0.04925537109375, -0.01313018798828125, -0.0112762451171875, ...]
          additionalProperties: null
      }, ...]
      usage: class EmbeddingsListUsage {
          totalTokens: 130
          additionalProperties: null
      }
      additionalProperties: null
  }
  ```

  ```go Go theme={null}
  {
    "data": [
      {
        "values": [
          0.03942871,
          -0.010177612,
          -0.046051025,
          ...
        ]
      },
      ...
    ], 
    "model": "llama-text-embed-v2",
    "usage": {
      "total_tokens": 130
    }
  }
  ```

  ```csharp C# theme={null}
  {
    "model": "llama-text-embed-v2",
    "data": [
      {
        "values": [
          0.04913330078125,
          -0.01306915283203125,
          -0.01116180419921875,
          ...
        ]
      },
      ...
    ],
    "usage": {
      "total_tokens": 130
    }
  }
  ```

  ```json curl theme={null}
  {
    "data": [
      {
        "values": [
          0.04925537109375,
          -0.01313018798828125,
          -0.0112762451171875,
          ...
        ]
      }, 
      ...
    ],
    "model": "llama-text-embed-v2",
    "usage": {
      "total_tokens": 130
    }
  }
  ```
</CodeGroup>


## See also

* [Understanding cost](/guides/manage-cost/understanding-cost)
* [Manage cost](/guides/manage-cost/manage-cost)



# Understanding cost
Source: https://docs.pinecone.io/guides/manage-cost/understanding-cost

Understand how costs are incurred in Pinecone.

For the latest pricing details, see [Pricing](https://www.pinecone.io/pricing/).


## Minimum usage

The Standard and Enterprise [pricing plans](https://www.pinecone.io/pricing/) include a monthly minimum usage committment:

| Plan       | Minimum usage |
| ---------- | ------------- |
| Starter    | \$0/month     |
| Standard   | \$50/month    |
| Enterprise | \$500/month   |

Beyond the monthly minimum, customers are charged for what they use each month.

**Examples**

<AccordionGroup>
  <Accordion title="Usage below monthly minimum">
    * You are on the Standard plan.
    * Your usage for the month of August amounts to \$20.
    * Your usage is below the \$50 monthly minimum, so your total for the month is \$50.

    In this case, the August invoice would include line items for each service you used (totaling \$20), plus a single line item covering the rest of the minimum usage commitment (\$30).
  </Accordion>

  <Accordion title="Usage exceeds monthly minimum">
    * You are on the Standard plan.
    * Your usage for the month of August amounts to \$100.
    * Your usage exceeds the \$50 monthly minimum, so your total for the month is \$100.

    In this case, the August invoice would only show line items for each service you used (totaling \$100). Since your usage exceeds the minimum usage commitment, you are only charged for your actual usage and no additional minimum usage line item appears on your invoice.
  </Accordion>
</AccordionGroup>


## Serverless indexes

With serverless indexes, you pay for the amount of data stored and operations performed, based on three usage metrics: [read units](#read-units), [write units](#write-units), and [storage](#storage).

For the latest serverless pricing rates, see [Pricing](https://www.pinecone.io/pricing/).

### Read units

Read units (RUs) measure the compute, I/O, and network resources consumed by the following read requests:

* [Query](#query)
* [Fetch](#fetch)
* [List](#list)

<Tip>
  Read requests return the number of RUs used. You can use this information to [monitor read costs](/guides/manage-cost/monitor-usage-and-costs#read-units).
</Tip>

#### Query

The cost of a query scales linearly with the size of the targeted namespace. Specifically, a query uses 1 RU for every 1 GB of [namespace size](#storage), with a minimum of 0.25 RUs per query.

For example, the following table contains the RU cost of searching indexes at different namespace sizes:

<Tabs>
  <Tab title="Dense index">
    | Records    | Dense dimension | Avg. metadata size | Avg. record size | Namespace size | RUs  |
    | :--------- | :-------------- | :----------------- | :--------------- | :------------- | :--- |
    | 500,000    | 768             | 500 bytes          | 3.57 KB          | 1.78 GB        | 1.78 |
    | 1,000,000  | 1536            | 1000 bytes         | 7.14 KB          | 7.14 GB        | 7.14 |
    | 5,000,000  | 1024            | 15,000 bytes       | 19.10 KB         | 95.5 GB        | 95.5 |
    | 10,000,000 | 1536            | 1000 bytes         | 7.14 KB          | 71.4 GB        | 71.4 |
  </Tab>

  <Tab title="Sparse index">
    | Records    | Sparse non-zero values | Avg. metadata size | Avg. record size | Namespace size | RUs  |
    | :--------- | :--------------------- | :----------------- | :--------------- | :------------- | :--- |
    | 500,000    | 10                     | 500 bytes          | 0.09 KB          | 0.045 GB       | 0.25 |
    | 1,000,000  | 50                     | 1000 bytes         | 1.45 KB          | 1.45 GB        | 1.45 |
    | 5,000,000  | 100                    | 15,000 bytes       | 15.9 KB          | 79.5 GB        | 79.5 |
    | 10,000,000 | 50                     | 1000 bytes         | 1.45 KB          | 14.5 GB        | 14.5 |
  </Tab>

  <Tab title="Hybrid index">
    | Records    | Dense dimension | Sparse non-zero values | Avg. metadata size | Avg. record size | Namespace size | RUs  |
    | :--------- | :-------------- | :--------------------- | :----------------- | :--------------- | :------------- | :--- |
    | 500,000    | 768             | 10                     | 500 bytes          | 3.67 KB          | 1.83 GB        | 1.83 |
    | 1,000,000  | 1536            | 50                     | 1000 bytes         | 7.34 KB          | 7.34 GB        | 7.34 |
    | 5,000,000  | 1024            | 100                    | 15,000 bytes       | 19.44 KB         | 97.2 GB        | 97.2 |
    | 10,000,000 | 1536            | 50                     | 1000 bytes         | 7.34 KB          | 73.4 GB        | 73.4 |
  </Tab>
</Tabs>

<Note>
  Parameters that affect the size of the query response, such as `top_k`, `include_metadata`, and `include_values`, are not relevant for query cost; only the size of the namespace determines the number of RUs used.
</Note>

#### Fetch

A fetch request uses 1 RU for every 10 records fetched, for example:

| Fetched records | RUs |
| --------------- | --- |
| 10              | 1   |
| 50              | 5   |
| 107             | 11  |

Specifying a non-existent ID or adding the same ID more than once does not increase the number of RUs used. However, a fetch request will always use at least 1 RU.

<Note>
  [Fetching records by metadata](/guides/manage-data/fetch-data#fetch-records-by-metadata) uses the same cost model as fetching by ID: 1 RU for every 10 records fetched.
</Note>

#### List

List has a fixed cost of 1 RU per call, with up to 100 records per call.

### Write units

Write units (WUs) measure the storage and compute resources used by the following write requests:

* [Upsert](#upsert)
* [Update](#update)
* [Delete](#delete)

#### Upsert

An upsert request uses 1 WU for each 1 KB of the request, with a minimum of 5 WUs per request. When an upsert modifies an existing record, the request uses 1 WU for each 1 KB of the existing record as well.

For example, the following table shows the WUs used by upsert requests at different batch sizes and record sizes, assuming all records are new:

| Records per batch | Dimension | Avg. metadata size | Avg. record size | WUs  |
| :---------------- | :-------- | :----------------- | :--------------- | :--- |
| 1                 | 768       | 100 bytes          | 3.2 KB           | 5    |
| 2                 | 768       | 100 bytes          | 3.2 KB           | 7    |
| 10                | 1024      | 15,000 bytes       | 19.10 KB         | 191  |
| 100               | 768       | 500 bytes          | 3.57 KB          | 357  |
| 1000              | 1536      | 1000 bytes         | 7.14 KB          | 7140 |

#### Update

An update request uses 1 WU for each 1 KB of the new and existing record, with a minimum of 5 WUs per request.

For example, the following table shows the WUs used by an update at different record sizes:

| New record size | Previous record size | WUs |
| :-------------- | :------------------- | :-- |
| 6.24 KB         | 6.50 KB              | 13  |
| 19.10 KB        | 15 KB                | 25  |
| 3.57 KB         | 5 KB                 | 9   |
| 7.14 KB         | 10 KB                | 18  |
| 3.17 KB         | 3.17 KB              | 7   |

<Note>
  [Updating records by metadata](/guides/manage-data/update-data#update-by-metadata) uses the same cost model as updating by ID: 1 WU for each 1 KB of the new and existing record.
</Note>

#### Delete

A delete request uses 1 WU for each 1 KB of records deleted, with a minimum of 5 WUs per request.

For example, the following table shows the WUs used by delete requests at different batch sizes and record sizes:

| Records per batch | Dimension | Avg. metadata size | Avg. record size | WUs  |
| :---------------- | :-------- | :----------------- | :--------------- | :--- |
| 1                 | 768       | 100 bytes          | 3.2 KB           | 5    |
| 2                 | 768       | 100 bytes          | 3.2 KB           | 7    |
| 10                | 1024      | 15,000 bytes       | 19.10 KB         | 191  |
| 100               | 768       | 500 bytes          | 3.57 KB          | 357  |
| 1000              | 1536      | 1000 bytes         | 7.14 KB          | 7140 |

Specifying a non-existent ID or adding the same ID more than once does not increase WU use.

[Deleting a namespace](/guides/manage-data/manage-namespaces#delete-a-namespace) or [deleting all records in a namespace using `deleteAll`](/guides/manage-data/delete-data#delete-all-records-in-a-namespace) uses 5 WUs.

<Note>
  [Deleting records by metadata](/guides/manage-data/delete-data#delete-records-by-metadata) uses the same cost model as deleting by ID: 1 WU for each 1 KB of records deleted.
</Note>

### Storage

Storage costs are based on the size of an index on a per-Gigabyte (GB) monthly rate. For the latest storage pricing rates, see [Pricing](https://www.pinecone.io/pricing/?plan=standard\&provider=aws\&plans=database\&scrollTo=product-pricing-modal-section).

* The size of an index is defined as the total size of its records across all namespaces.

* The size of a single record is defined as the sum of the following components:

  * ID size
  * Dense vector size (equal to 4 \* the dense dimensions)
  * Sparse vector size (equal to 9 \* each non-zero sparse value)
  * Total metadata size (equal to the total size of all metadata fields)

  Sparse vector size is relevant only for [sparse indexes](/guides/index-data/indexing-overview#sparse-indexes) and [hybrid indexes](/guides/search/hybrid-search#use-a-single-hybrid-index).

The following tables demonstrate index sizes at different record counts:

<Tabs>
  <Tab title="Dense index">
    | Records    | Dense dimension | Avg. metadata size | Avg. record size | Namespace size |
    | :--------- | :-------------- | :----------------- | :--------------- | :------------- |
    | 500,000    | 768             | 500 bytes          | 3.57 KB          | 1.78 GB        |
    | 1,000,000  | 1536            | 1000 bytes         | 7.14 KB          | 7.14 GB        |
    | 5,000,000  | 1024            | 15,000 bytes       | 19.10 KB         | 95.5 GB        |
    | 10,000,000 | 1536            | 1000 bytes         | 7.14 KB          | 71.4 GB        |
  </Tab>

  <Tab title="Sparse index">
    | Records    | Sparse non-zero values | Avg. metadata size | Avg. record size | Namespace size |
    | :--------- | :--------------------- | :----------------- | :--------------- | :------------- |
    | 500,000    | 10                     | 500 bytes          | 0.09 KB          | 0.045 GB       |
    | 1,000,000  | 50                     | 1000 bytes         | 1.45 KB          | 1.45 GB        |
    | 5,000,000  | 100                    | 15,000 bytes       | 15.9 KB          | 79.5 GB        |
    | 10,000,000 | 50                     | 1000 bytes         | 1.45 KB          | 14.5 GB        |
  </Tab>

  <Tab title="Hybrid index">
    | Records    | Dense dimension | Sparse non-zero values | Avg. metadata size | Avg. record size | Namespace size |
    | :--------- | :-------------- | :--------------------- | :----------------- | :--------------- | :------------- |
    | 500,000    | 768             | 10                     | 500 bytes          | 3.67 KB          | 1.83 GB        |
    | 1,000,000  | 1536            | 50                     | 1000 bytes         | 7.34 KB          | 7.34 GB        |
    | 5,000,000  | 1024            | 100                    | 15,000 bytes       | 19.44 KB         | 97.2 GB        |
    | 10,000,000 | 1536            | 50                     | 1000 bytes         | 7.34 KB          | 73.4 GB        |
  </Tab>
</Tabs>


## Imports

[Importing from object storage](/guides/index-data/import-data) is the most efficient and cost-effective method to load large numbers of records into an index. The cost of an import is based on the size of the records read, whether the records were imported successfully or not.

If the import operation fails (e.g., after encountering a vector of the wrong dimension in an import with `on_error="abort"`), you will still be charged for the records read. However, if the import fails because of an internal system error, you will not incur charges. In this case, the import will return the error message `"We were unable to process your request. If the problem persists, please contact us at https://support.pinecone.io"`.

For the latest import pricing rates, see [Pricing](https://www.pinecone.io/pricing/).


## Backups and restores

A [backup](/guides/manage-data/backups-overview) is a static copy of a serverless index. Both the cost of storing a backup and [restoring an index](/guides/manage-data/restore-an-index) from a backup is based on the size of the index. For the latest backup and restore pricing rates, see [Pricing](https://www.pinecone.io/pricing/?plan=standard\&provider=aws\&plans=database\&scrollTo=product-pricing-modal-section).


## Embedding

Pinecone hosts several [embedding models](/guides/index-data/create-an-index#embedding-models) so it's easy to manage your vector storage and search process on a single platform. You can use a hosted model to embed your data as an integrated part of upserting and querying, or you can use a hosted model to embed your data as a standalone operation.

Embedding costs are determined by how many [tokens](https://www.pinecone.io/learn/tokenization/) are in a request. In general, the more words contained in your passage or query, the more tokens you generate.

For example, if you generate embeddings for the query, "What is the maximum diameter of a red pine?", Pinecone Inference generates 10 tokens, then converts them into an embedding. If the price per token for your billing plan is \$.08 per million tokens, then this API call costs \$.00001.

To learn more about tokenization, see [Choosing an embedding model](https://www.pinecone.io/learn/series/rag/embedding-models-rundown/). For the latest embed pricing rates, see [Pricing](https://www.pinecone.io/pricing/?plan=standard\&provider=aws\&plans=inference\&scrollTo=product-pricing-modal-section).

<Tip>
  Embedding requests returns the total tokens generated. You can use this information to [monitor and manage embedding costs](/guides/manage-cost/monitor-usage-and-costs#embedding-tokens).
</Tip>


## Reranking

Pinecone hosts several [reranking models](/guides/search/rerank-results#reranking-models) so it's easy to manage two-stage vector retrieval on a single platform. You can use a hosted model to rerank results as an integrated part of a query, or you can use a hosted model to rerank results as a standalone operation.

Reranking costs are determined by the number of requests to the reranking model. For the latest rerank pricing rates, see [Pricing](https://www.pinecone.io/pricing/?plan=standard\&provider=aws\&plans=inference\&scrollTo=product-pricing-modal-section).


## Assistant

For details on how costs are incurred in Pinecone Assistant, see [Assistant pricing](/guides/assistant/pricing-and-limits).


## See also

* [Manage cost](/guides/manage-cost/manage-cost)
* [Monitor usage](/guides/manage-cost/monitor-usage-and-costs)
* [Pricing](https://www.pinecone.io/pricing/)



---
**Navigation:** [← Previous](./05-this-is-grpc-client-aliased-as-pinecone.md) | [Index](./index.md) | [Next →](./07-back-up-an-index.md)
