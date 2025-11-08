**Navigation:** [← Previous](./16-delete-vectors.md) | [Index](./index.md) | [Next →](./18-ai-engine.md)

# Upsert text
Source: https://docs.pinecone.io/reference/api/2025-04/data-plane/upsert_records

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-04/db_data_2025-04.oas.yaml post /records/namespaces/{namespace}/upsert
Upsert text into a namespace. Pinecone converts the text to vectors automatically using the hosted embedding model associated with the index.

Upserting text is supported only for [indexes with integrated embedding](https://docs.pinecone.io/reference/api/2025-01/control-plane/create_for_model).

For guidance, examples, and limits, see [Upsert data](https://docs.pinecone.io/guides/index-data/upsert-data).

<RequestExample>
  ```python Python theme={null}
  # pip install --upgrade pinecone
  from pinecone import Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  # To get the unique host for an index, 
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  index = pc.Index(host="INDEX_HOST")

  # Upsert records into a namespace
  # `chunk_text` fields are converted to dense vectors
  # `category` fields are stored as metadata
  index.upsert_records(
      "example-namespace",
      [
          {
              "_id": "rec1",
              "chunk_text": "Apples are a great source of dietary fiber, which supports digestion and helps maintain a healthy gut.",
              "category": "digestive system", 
          },
          {
              "_id": "rec2",
              "chunk_text": "Apples originated in Central Asia and have been cultivated for thousands of years, with over 7,500 varieties available today.",
              "category": "cultivation",
          },
          {
              "_id": "rec3",
              "chunk_text": "Rich in vitamin C and other antioxidants, apples contribute to immune health and may reduce the risk of chronic diseases.",
              "category": "immune system",
          },
          {
              "_id": "rec4",
              "chunk_text": "The high fiber content in apples can also help regulate blood sugar levels, making them a favorable snack for people with diabetes.",
              "category": "endocrine system",
          },
      ]
  )
  ```

  ```javascript JavaScript theme={null}
  // npm install @pinecone-database/pinecone
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({ apiKey: "YOUR_API_KEY" })

  // To get the unique host for an index, 
  // see https://docs.pinecone.io/guides/manage-data/target-an-index
  const namespace = pc.index("INDEX_NAME", "INDEX_HOST").namespace("example-namespace");

  // Upsert records into a namespace
  // `chunk_text` fields are converted to dense vectors
  // `category` ios stored as metadata
  await namespace.upsertRecords([
      {
          "_id": "rec1",
          "chunk_text": "Apples are a great source of dietary fiber, which supports digestion and helps maintain a healthy gut.",
          "category": "digestive system", 
      },
      {
          "_id": "rec2",
          "chunk_text": "Apples originated in Central Asia and have been cultivated for thousands of years, with over 7,500 varieties available today.",
          "category": "cultivation",
      },
      {
          "_id": "rec3",
          "chunk_text": "Rich in vitamin C and other antioxidants, apples contribute to immune health and may reduce the risk of chronic diseases.",
          "category": "immune system",
      },
      {
          "_id": "rec4",
          "chunk_text": "The high fiber content in apples can also help regulate blood sugar levels, making them a favorable snack for people with diabetes.",
          "category": "endocrine system",
      }
  ]);
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Index;
  import io.pinecone.configs.PineconeConfig;
  import io.pinecone.configs.PineconeConnection;
  import org.openapitools.db_data.client.ApiException;

  import java.util.*;

  public class UpsertText {
      public static void main(String[] args) throws ApiException {
          PineconeConfig config = new PineconeConfig("YOUR_API_KEY");
          config.setHost("INDEX_HOST");
          PineconeConnection connection = new PineconeConnection(config);

          Index index = new Index(config, connection, "integrated-dense-java");
          ArrayList<Map<String, String>> upsertRecords = new ArrayList<>();

          HashMap<String, String> record1 = new HashMap<>();
          record1.put("_id", "rec1");
          record1.put("category", "digestive system");
          record1.put("chunk_text", "Apples are a great source of dietary fiber, which supports digestion and helps maintain a healthy gut.");

          HashMap<String, String> record2 = new HashMap<>();
          record2.put("_id", "rec2");
          record2.put("category", "cultivation");
          record2.put("chunk_text", "Apples originated in Central Asia and have been cultivated for thousands of years, with over 7,500 varieties available today.");

          HashMap<String, String> record3 = new HashMap<>();
          record3.put("_id", "rec3");
          record3.put("category", "immune system");
          record3.put("chunk_text", "Rich in vitamin C and other antioxidants, apples contribute to immune health and may reduce the risk of chronic diseases.");

          HashMap<String, String> record4 = new HashMap<>();
          record4.put("_id", "rec4");
          record4.put("category", "endocrine system");
          record4.put("chunk_text", "The high fiber content in apples can also help regulate blood sugar levels, making them a favorable snack for people with diabetes.");

          upsertRecords.add(record1);
          upsertRecords.add(record2);
          upsertRecords.add(record3);
          upsertRecords.add(record4);

          index.upsertRecords("example-namespace", upsertRecords);
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

      // To get the unique host for an index, 
      // see https://docs.pinecone.io/guides/manage-data/target-an-index
      idxConnection, err := pc.Index(pinecone.NewIndexConnParams{Host: "INDEX_HOST", Namespace: "example-namespace"})
      if err != nil {
          log.Fatalf("Failed to create IndexConnection for Host: %v", err)
  	  }

      // Upsert records into a namespace
      // `chunk_text` fields are converted to dense vectors
      // `category` is stored as metadata
  	records := []*pinecone.IntegratedRecord{
          {
              "_id": "rec1",
              "chunk_text": "Apples are a great source of dietary fiber, which supports digestion and helps maintain a healthy gut.",
              "category": "digestive system", 
          },
          {
              "_id": "rec2",
              "chunk_text": "Apples originated in Central Asia and have been cultivated for thousands of years, with over 7,500 varieties available today.",
              "category": "cultivation",
          },
          {
              "_id": "rec3",
              "chunk_text": "Rich in vitamin C and other antioxidants, apples contribute to immune health and may reduce the risk of chronic diseases.",
              "category": "immune system",
          },
          {
              "_id": "rec4",
              "chunk_text": "The high fiber content in apples can also help regulate blood sugar levels, making them a favorable snack for people with diabetes.",
              "category": "endocrine system",
          },
  	}

  	err = idxConnection.UpsertRecords(ctx, records)
  	if err != nil {
  		log.Fatalf("Failed to upsert vectors: %v", err)
  	}
  }
  ```

  ```csharp C# theme={null}
  using Pinecone;

  var pinecone = new PineconeClient("YOUR_API_KEY");

  var index = pinecone.Index(host: "INDEX_HOST");

  await index.UpsertRecordsAsync(
      "example-namespace",
      [
          new UpsertRecord
          {
              Id = "rec1",
              AdditionalProperties =
              {
                  ["chunk_text"] = "Apples are a great source of dietary fiber, which supports digestion and helps maintain a healthy gut.",
                  ["category"] = "digestive system",
              },
          },
          new UpsertRecord
          {
              Id = "rec2",
              AdditionalProperties =
              {
                  ["chunk_text"] = "Apples originated in Central Asia and have been cultivated for thousands of years, with over 7,500 varieties available today.",
                  ["category"] = "cultivation",
              },
          },  
          new UpsertRecord
          {
              Id = "rec3",
              AdditionalProperties =
              {
                  ["chunk_text"] = "Rich in vitamin C and other antioxidants, apples contribute to immune health and may reduce the risk of chronic diseases.",
                  ["category"] = "immune system",
              },
          },
          new UpsertRecord
          {
              Id = "rec4",
              AdditionalProperties =
              {
                  ["chunk_text"] = "The high fiber content in apples can also help regulate blood sugar levels, making them a favorable snack for people with diabetes.",
                  ["category"] = "endocrine system",
              },
          },
      ]
  );
  ```

  ```shell curl theme={null}
  # To get the unique host for an index,
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  INDEX_HOST="INDEX_HOST"
  NAMESPACE="YOUR_NAMESPACE"
  PINECONE_API_KEY="YOUR_API_KEY"

  # Upsert records into a namespace
  # `chunk_text` fields are converted to dense vectors
  # `category` fields are stored as metadata
  curl "https://$INDEX_HOST/records/namespaces/$NAMESPACE/upsert" \
    -H "Content-Type: application/x-ndjson" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-API-Version: 2025-04" \
    -d '{"_id": "rec1", "chunk_text": "Apples are a great source of dietary fiber, which supports digestion and helps maintain a healthy gut.", "category": "digestive system"}
        {"_id": "rec2", "chunk_text": "Apples originated in Central Asia and have been cultivated for thousands of years, with over 7,500 varieties available today.", "category": "cultivation"}
        {"_id": "rec3", "chunk_text": "Rich in vitamin C and other antioxidants, apples contribute to immune health and may reduce the risk of chronic diseases.", "category": "immune system"}
        {"_id": "rec4", "chunk_text": "The high fiber content in apples can also help regulate blood sugar levels, making them a favorable snack for people with diabetes.", "category": "endocrine system"}'
  ```
</RequestExample>

<ResponseExample />



# Authentication
Source: https://docs.pinecone.io/reference/api/authentication



All requests to [Pinecone APIs](/reference/api/introduction) must contain a valid [API key](/guides/production/security-overview#api-keys) for the target project.


## Get an API key

[Create a new API key](https://app.pinecone.io/organizations/-/projects/-/keys) in the Pinecone console, or use the connect widget below to generate a key.

<div style={{minWidth: '450px', minHeight:'152px'}}>
  <div id="pinecone-connect-widget">
    <div class="connect-widget-skeleton">
      <div class="skeleton-content" />
    </div>
  </div>
</div>

Copy your generated key:

```
PINECONE_API_KEY="{{YOUR_API_KEY}}"


# This API key has ReadWrite access to all indexes in your project.
```


## Initialize a client

When using a [Pinecone SDK](/reference/pinecone-sdks), initialize a client object with your API key and then reuse the authenicated client in subsquent function calls. For example:

<CodeGroup>
  ```Python Python theme={null}
  from pinecone.grpc import PineconeGRPC as Pinecone
  from pinecone import ServerlessSpec

  pc = Pinecone(api_key='YOUR_API_KEY')

  # Creates an index using the API key stored in the client 'pc'.
  pc.create_index(
      name="docs-example",
      dimension=1536,
      metric="cosine",
      spec=ServerlessSpec(
          cloud='aws', 
          region='us-east-1'
      ) 
  ) 
  ```

  ```JavaScript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({
      apiKey: 'YOUR_API_KEY' 
  });

  // Creates an index using the API key stored in the client 'pc'.
  await pc.createIndex({
      name: 'docs-example',
      dimension: 1536,
      metric: 'cosine',
      spec: { 
          serverless: { 
              cloud: 'aws', 
              region: 'us-east-1' 
          }
      } 
  }) 
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Pinecone;
  import org.openapitools.db_control.client.model.IndexModel;
  import org.openapitools.db_control.client.model.DeletionProtection;

  public class CreateServerlessIndexExample {
      public static void main(String[] args) {
          Pinecone pc = new Pinecone.Builder("YOUR_API_KEY").build();

          // Creates an index using the API key stored in the client 'pc'.
          pc.createServerlessIndex("docs-example", "cosine", 1536, "aws", "us-east-1");
      }
  }
  ```

  ```go Go theme={null}
  package main

  import (
      "context"
      "fmt"
      "log"

      "github.com/pinecone-io/go-pinecone/v3/pinecone"
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
      })
      if err != nil {
          log.Fatalf("Failed to create serverless index: %v", err)
      } else {
          fmt.Printf("Successfully created serverless index: %v", idx.Name)
      }
  }
  ```

  ```shell curl theme={null}
  curl -s "https://api.pinecone.io/indexes" \
      -H "Api-Key: YOUR_API_KEY" \
      -H "Content-Type: application/json" \
      -H "X-Pinecone-API-Version: 2025-04" \
      -d '{
          "name":  "docs-example",
          "dimension": 1536,
          "metric": "cosine",
          "spec": {
              "serverless": {
                 "cloud":"aws",
                 "region": "us-east-1"
              }
          }
      }'
  ```
</CodeGroup>


## Add headers to an HTTP request

All HTTP requests to Pinecone APIs must contain an `Api-Key` header that specifies a valid [API key](/guides/production/security-overview#api-keys) and must be encoded as JSON with the `Content-Type: application/json` header. For example:

```shell curl theme={null}
curl https://api.pinecone.io/indexes \
   -H "Content-Type: application/json" \
   -H "Api-Key: $PINECONE_API_KEY" \
  -H "X-Pinecone-API-Version: 2025-01" \
   -d '{
         "name":  "docs-example",
         "dimension": 1536,
         "metric": "cosine",
         "spec": {
            "serverless": {
               "cloud":"aws",
               "region": "us-east-1"
            }
         }
      }'
```


## Troubleshooting

<AccordionGroup>
  <Accordion title="Initialization errors due to outdated SDKs">
    Older versions of Pinecone required you to initialize a client with an `init` method that takes both `api_key` and `environment` parameters, for example:

    <CodeGroup>
      ```python Python theme={null}
      # Legacy initialization
      import pinecone

      pc = pinecone.init(
          api_key="PINECONE_API_KEY",
          environment="PINECONE_ENVIRONMENT"
      )
      ```

      ```javascript JavaScript theme={null}
      // Legacy initialization
      import { Pinecone } from '@pinecone-database/pinecone';

      const pineconeClient = new PineconeClient();
      await pineconeClient.init({
          apiKey: 'PINECONE_API_KEY',
          environment: 'PINECONE_ENVIRONMENT',
      });
      ```
    </CodeGroup>

    In more recent versions of Pinecone, this has changed. Initialization no longer requires an `init` step, and cloud environment is defined for each index rather than an entire project. Client initialization now only requires an `api_key` parameter, for example:

    <CodeGroup>
      ```python Python theme={null}
      # New initialization
      from pinecone import Pinecone

      pc = Pinecone(api_key="YOUR_API_KEY")
      ```

      ```javascript JavaScript theme={null}
      // New initialization
      import { Pinecone } from '@pinecone-database/pinecone';

      const pc = new Pinecone({
          apiKey: 'YOUR_API_KEY' 
      });
      ```
    </CodeGroup>

    If you are receiving errors about initialization, upgrade your [Pinecone SDK](/reference/pinecone-sdks) to the latest version, for example:

    <CodeGroup>
      ```shell Python theme={null}
      # Upgrade Pinecone SDK
      pip install pinecone --upgrade
      ```

      ```shell JavaScript theme={null}
      # Upgrade Pinecone SDK
      npm install @pinecone-database/pinecone@latest
      ```
    </CodeGroup>

    Also, note that some third-party tutorials and examples still reference the older initialization method. In such cases, follow the example above and the examples throughout the Pinecone documentation instead.
  </Accordion>
</AccordionGroup>



# Pinecone Database limits
Source: https://docs.pinecone.io/reference/api/database-limits



This page describes different types of limits for Pinecone Database.


## Rate limits

Rate limits help protect your applications from misuse and maintain the health of our shared serverless infrastructure. These limits are designed to support typical production workloads while ensuring reliable performance for all users.

**Most rate limits can be adjusted upon request.** If you need higher limits to scale your application, [contact Support](https://app.pinecone.io/organizations/-/settings/support/ticket) with details about your use case. Pinecone is committed to supporting your growth and can often accommodate higher throughput requirements.

Rate limits vary based on [pricing plan](https://www.pinecone.io/pricing/) and apply to [serverless indexes](/guides/index-data/indexing-overview) only.

| Metric                                                                                                        | Starter plan   | Standard plan  | Enterprise plan |
| :------------------------------------------------------------------------------------------------------------ | :------------- | :------------- | :-------------- |
| [Read units per month per project](#read-units-per-month-per-project)                                         | 1,000,000      | Unlimited      | Unlimited       |
| [Write units per month per project](#write-units-per-month-per-project)                                       | 2,000,000      | Unlimited      | Unlimited       |
| [Upsert size per second per namespace](#upsert-size-per-second-per-namespace)                                 | 50 MB          | 50 MB          | 50 MB           |
| [Query read units per second per index](#query-read-units-per-second-per-index)                               | 2,000          | 2,000          | 2,000           |
| [Update records per second per namespace](#update-records-per-second-per-namespace)                           | 100            | 100            | 100             |
| [Update by metadata requests per second per namespace](#update-by-metadata-requests-per-second-per-namespace) | 5              | 5              | 5               |
| [Update by metadata requests per second per index](#update-by-metadata-requests-per-second-per-index)         | 500            | 500            | 500             |
| [Fetch requests per second per index](#fetch-requests-per-second-per-index)                                   | 100            | 100            | 100             |
| [List requests per second per index](#list-requests-per-second-per-index)                                     | 200            | 200            | 200             |
| [Describe index stats requests per second per index](#describe-index-stats-requests-per-second-per-index)     | 100            | 100            | 100             |
| [Delete records per second per namespace](#delete-records-per-second-per-namespace)                           | 5,000          | 5,000          | 5,000           |
| [Delete records per second per index](#delete-records-per-second-per-index)                                   | 5,000          | 5,000          | 5,000           |
| [Delete by metadata requests per second per namespace](#delete-by-metadata-requests-per-second-per-namespace) | 5              | 5              | 5               |
| [Delete by metadata requests per second per index](#delete-by-metadata-requests-per-second-per-index)         | 500            | 500            | 500             |
| [Embedding tokens per minute per model](#embedding-tokens-per-minute-per-model)                               | Model-specific | Model-specific | Model-specific  |
| [Embedding tokens per month per model](#embedding-tokens-per-month-per-model)                                 | 5,000,000      | Unlimited      | Unlimited       |
| [Rerank requests per minute per model](#rerank-requests-per-minute-per-model)                                 | Model-specific | Model-specific | Model-specific  |
| [Rerank requests per month per model](#rerank-requests-per-month-per-model)                                   | 500            | Model-specific | Model-specific  |

### Read units per month per project

| Starter plan | Standard plan | Enterprise plan |
| ------------ | ------------- | --------------- |
| 1,000,000    | Unlimited     | Unlimited       |

[Read units](/guides/manage-cost/understanding-cost#read-units) measure the compute, I/O, and network resources used by [fetch](/guides/manage-data/fetch-data), [query](/guides/search/search-overview), and [list](/guides/manage-data/list-record-ids) requests to serverless indexes. When you reach the monthly read unit limit for a project, fetch, query, and list requests to serverless indexes in the project will fail and return a `429 - TOO_MANY_REQUESTS` status with the following error:

```
Request failed. You've reached your read unit limit for the current month limit. 
To continue reading data, upgrade your plan. 
```

To continue reading from serverless indexes in the project, [upgrade your plan](/guides/organizations/manage-billing/upgrade-billing-plan).

To check how close you are to the monthly read unit limit for a project, do the following:

1. Open the [Pinecone console](https://app.pinecone.io/organizations/-/projects).
2. Select the project.
3. Select any index in the project.
4. Look under **Starter Usage**.

### Write units per month per project

| Starter plan | Standard plan | Enterprise plan |
| ------------ | ------------- | --------------- |
| 2,000,000    | Unlimited     | Unlimited       |

[Write units](/guides/manage-cost/understanding-cost#write-units) measure the storage and compute resources used by [upsert](/guides/index-data/upsert-data), [update](/guides/manage-data/update-data), and [delete](/guides/manage-data/delete-data) requests to serverless indexes. When you reach the monthly write unit limit for a project, upsert, update, and delete requests to serverless indexes in the project will fail and return a `429 - TOO_MANY_REQUESTS` status with the following error:

```
Request failed. You've reached your write unit limit for the current month. 
To continue writing data, upgrade your plan.
```

To continue writing data to serverless indexes in the project, [upgrade your plan](/guides/organizations/manage-billing/upgrade-billing-plan).

To check how close you are to the monthly read unit limit for a project, do the following:

1. Open the [Pinecone console](https://app.pinecone.io/organizations/-/projects).
2. Select the project.
3. Select any index in the project.
4. Look under **Starter Usage**.

### Upsert size per second per namespace

| Starter plan | Standard plan | Enterprise plan |
| ------------ | ------------- | --------------- |
| 50 MB        | 50 MB         | 50 MB           |

When you reach the per second [upsert](/guides/index-data/upsert-data) size for a namespace in an index, additional upserts will fail and return a `429 - TOO_MANY_REQUESTS` status with the following error:

```
Request failed. You've reached the max upsert size limit per second for index <index name>. 
Pace your upserts or contact Pinecone Support (https://app.pinecone.io/organizations/-/settings/support/ticket) to request a higher limit.
```

To handle this limit, [implement retry logic with exponential backoff](/guides/production/error-handling#implement-retry-logic). If you need a higher limit for your use case, [contact Support](https://app.pinecone.io/organizations/-/settings/support/ticket).

### Query read units per second per index

| Starter plan | Standard plan | Enterprise plan |
| ------------ | ------------- | --------------- |
| 2,000        | 2,000         | 2,000           |

Pinecone measures [query](/guides/search/search-overview) usage in [read units](/guides/manage-cost/understanding-cost#read-units). When you reach the per second limit for queries across all namespaces in an index, additional queries will fail and return a `429 - TOO_MANY_REQUESTS` status with the following error:

```
Request failed. You've reached the max query read units per second for index <index name>. 
Pace your queries or contact Pinecone Support (https://app.pinecone.io/organizations/-/settings/support/ticket) to request a higher limit.
```

To handle this limit, [implement retry logic with exponential backoff](/guides/production/error-handling#implement-retry-logic). If you need a higher limit for your use case, [contact Support](https://app.pinecone.io/organizations/-/settings/support/ticket).

To check how many read units a query consumes, [check the query response](/guides/manage-cost/monitor-usage-and-costs#read-units).

### Update records per second per namespace

| Starter plan | Standard plan | Enterprise plan |
| ------------ | ------------- | --------------- |
| 100          | 100           | 100             |

When you reach the per second [update](/guides/manage-data/update-data) limit for a namespace in an index, additional updates will fail and return a `429 - TOO_MANY_REQUESTS` status with the following error:

```
Request failed. You've reached the max update records per second for namespace <namespace name>. 
Pace your update requests or contact Pinecone Support (https://app.pinecone.io/organizations/-/settings/support/ticket) to request a higher limit.
```

To handle this limit, [implement retry logic with exponential backoff](/guides/production/error-handling#implement-retry-logic). If you need a higher limit for your use case, [contact Support](https://app.pinecone.io/organizations/-/settings/support/ticket).

### Update by metadata requests per second per namespace

| Starter plan | Standard plan | Enterprise plan |
| ------------ | ------------- | --------------- |
| 5            | 5             | 5               |

When you reach the per second [update by metadata](/guides/manage-data/update-data#update-metadata-across-multiple-records) request limit for a namespace in an index, additional update by metadata requests will fail and return a `429 - TOO_MANY_REQUESTS` status with the following error:

```
Request failed. You've reached the max update by metadata requests per second for namespace <namespace name>. Pace your update by metadata requests or contact Pinecone Support (https://app.pinecone.io/organizations/-/settings/support/ticket) to request a higher limit.
```

To handle this limit, [implement retry logic with exponential backoff](/guides/production/error-handling#implement-retry-logic). If you need a higher limit for your use case, [contact Support](https://app.pinecone.io/organizations/-/settings/support/ticket).

### Update by metadata requests per second per index

| Starter plan | Standard plan | Enterprise plan |
| ------------ | ------------- | --------------- |
| 500          | 500           | 500             |

When you reach the per second [update by metadata](/guides/manage-data/update-data#update-metadata-across-multiple-records) request limit across all namespaces in an index, additional update by metadata requests will fail and return a `429 - TOO_MANY_REQUESTS` status with the following error:

```
Request failed. You've reached the max update by metadata requests per second for index <index name>. Pace your update by metadata requests or contact Pinecone Support (https://app.pinecone.io/organizations/-/settings/support/ticket) to request a higher limit.
```

To handle this limit, [implement retry logic with exponential backoff](/guides/production/error-handling#implement-retry-logic). If you need a higher limit for your use case, [contact Support](https://app.pinecone.io/organizations/-/settings/support/ticket).

### Fetch requests per second per index

| Starter plan | Standard plan | Enterprise plan |
| ------------ | ------------- | --------------- |
| 100          | 100           | 100             |

When you reach the per second [fetch](/guides/manage-data/fetch-data) limit across all namespaces in an index, additional fetch requests will fail and return a `429 - TOO_MANY_REQUESTS` status with the following error:

```
Request failed. You've reached the max fetch requests per second for index <index name>.
Pace your fetch requests or contact Pinecone Support (https://app.pinecone.io/organizations/-/settings/support/ticket) to request a higher limit.
```

To handle this limit, [implement retry logic with exponential backoff](/guides/production/error-handling#implement-retry-logic). If you need a higher limit for your use case, [contact Support](https://app.pinecone.io/organizations/-/settings/support/ticket).

### List requests per second per index

| Starter plan | Standard plan | Enterprise plan |
| ------------ | ------------- | --------------- |
| 200          | 200           | 200             |

When you reach the per second [list](/guides/manage-data/list-record-ids) limit across all namespaces in an index, additional list requests will fail and return a `429 - TOO_MANY_REQUESTS` status with the following error:

```
Request failed. You've reached the max list requests per second for index <index name>.
Pace your list requests or contact Pinecone Support (https://app.pinecone.io/organizations/-/settings/support/ticket) to request a higher limit.
```

To handle this limit, [implement retry logic with exponential backoff](/guides/production/error-handling#implement-retry-logic). If you need a higher limit for your use case, [contact Support](https://app.pinecone.io/organizations/-/settings/support/ticket).

### Describe index stats requests per second per index

| Starter plan | Standard plan | Enterprise plan |
| ------------ | ------------- | --------------- |
| 100          | 100           | 100             |

When you reach the per second [describe index stats](/reference/api/2024-10/data-plane/describeindexstats) limit across all namespaces in an index, additional list requests will fail and return a `429 - TOO_MANY_REQUESTS` status with the following error:

```
Request failed. You've reached the max describe_index_stats requests per second for index <index>. 
Pace your describe_index_stats requests or contact Pinecone Support (https://app.pinecone.io/organizations/-/settings/support/ticket) to request a higher limit.
```

To handle this limit, [implement retry logic with exponential backoff](/guides/production/error-handling#implement-retry-logic). If you need a higher limit for your use case, [contact Support](https://app.pinecone.io/organizations/-/settings/support/ticket).

### Delete records per second per namespace

| Starter plan | Standard plan | Enterprise plan |
| ------------ | ------------- | --------------- |
| 5000         | 5000          | 5000            |

When you reach the per second [delete](/guides/manage-data/delete-data) limit for a namespace in an index, additional deletes will fail and return a `429 - TOO_MANY_REQUESTS` status with the following error:

```
Request failed. You've reached the max delete records per second for namespace <namespace name>. 
Pace your delete requests or contact Pinecone Support (https://app.pinecone.io/organizations/-/settings/support/ticket) to request a higher limit.
```

To handle this limit, [implement retry logic with exponential backoff](/guides/production/error-handling#implement-retry-logic). If you need a higher limit for your use case, [contact Support](https://app.pinecone.io/organizations/-/settings/support/ticket).

### Delete records per second per index

| Starter plan | Standard plan | Enterprise plan |
| ------------ | ------------- | --------------- |
| 5000         | 5000          | 5000            |

When you reach the per second [delete](/guides/manage-data/delete-data) limit across all namespaces in an index, additional deletes will fail and return a `429 - TOO_MANY_REQUESTS` status with the following error:

```
Request failed. You've reached the max delete records per second for index <index name>. 
Pace your delete requests or contact Pinecone Support (https://app.pinecone.io/organizations/-/settings/support/ticket) to request a higher limit.
```

To handle this limit, [implement retry logic with exponential backoff](/guides/production/error-handling#implement-retry-logic). If you need a higher limit for your use case, [contact Support](https://app.pinecone.io/organizations/-/settings/support/ticket).

### Delete by metadata requests per second per namespace

| Starter plan | Standard plan | Enterprise plan |
| ------------ | ------------- | --------------- |
| 5            | 5             | 5               |

When you reach the per second [delete by metadata](/guides/manage-data/delete-data#delete-records-by-metadata) request limit for a namespace in an index, additional delete by metadata requests will fail and return a `429 - TOO_MANY_REQUESTS` status with the following error:

```
Request failed. You've reached the max delete by metadata requests per second for namespace <namespace name>. Pace your delete by metadata requests or contact Pinecone Support (https://app.pinecone.io/organizations/-/settings/support/ticket) to request a higher limit.
```

To handle this limit, [implement retry logic with exponential backoff](/guides/production/error-handling#implement-retry-logic). If you need a higher limit for your use case, [contact Support](https://app.pinecone.io/organizations/-/settings/support/ticket).

### Delete by metadata requests per second per index

| Starter plan | Standard plan | Enterprise plan |
| ------------ | ------------- | --------------- |
| 500          | 500           | 500             |

When you reach the per second [delete by metadata](/guides/manage-data/delete-data#delete-records-by-metadata) request limit across all namespaces in an index, additional delete by metadata requests will fail and return a `429 - TOO_MANY_REQUESTS` status with the following error:

```
Request failed. You've reached the max delete by metadata requests per second for index <index name>. Pace your delete by metadata requests or contact Pinecone Support (https://app.pinecone.io/organizations/-/settings/support/ticket) to request a higher limit.
```

To handle this limit, [implement retry logic with exponential backoff](/guides/production/error-handling#implement-retry-logic). If you need a higher limit for your use case, [contact Support](https://app.pinecone.io/organizations/-/settings/support/ticket).

### Embedding tokens per minute per model

| Embedding model              | Input type | Starter plan | Standard plan | Enterprise plan |
| :--------------------------- | :--------- | :----------- | :------------ | :-------------- |
| `llama-text-embed-v2`        | Passage    | 250,000      | 1,000,000     | 1,000,000       |
|                              | Query      | 50,000       | 250,000       | 250,000         |
| `multilingual-e5-large`      | Passage    | 250,000      | 1,000,000     | 1,000,000       |
|                              | Query      | 50,000       | 250,000       | 250,000         |
| `pinecone-sparse-english-v0` | Passage    | 250,000      | 3,000,000     | 3,000,000       |
|                              | Query      | 250,000      | 3,000,000     | 3,000,000       |

When you reach the per minute token limit for an [embedding model](/guides/index-data/create-an-index#embedding-models) hosted by Pinecone, additional embeddings will fail and return a `429 - TOO_MANY_REQUESTS` status with the following error:

```
Request failed. You've reached the max embedding tokens per minute (<limit>) model '<model name>'' and input type '<passage|query>' for the current project. 
To increase this limit, upgrade your plan.
```

To increase this limit, [upgrade your plan](/guides/organizations/manage-billing/upgrade-billing-plan). Otherwise, you can handle this limit by [implementing retry logic with exponential backoff](/guides/production/error-handling#implement-retry-logic).

### Embedding tokens per month per model

| Starter plan | Standard plan | Enterprise plan |
| ------------ | ------------- | --------------- |
| 5,000,000    | Unlimited     | Unlimited       |

When you reach the monthly token limit for an [embedding model](/guides/index-data/create-an-index#embedding-models) hosted by Pinecone, additional embeddings will fail and return a `429 - TOO_MANY_REQUESTS` status with the following error:

```
Request failed. You've reached the embedding token limit (<limit>) for model <model name> for the current month. 
To continue using this model, upgrade your plan.
```

To increase this limit, [upgrade your plan](/guides/organizations/manage-billing/upgrade-billing-plan) or [contact Support](https://app.pinecone.io/organizations/-/settings/support/ticket).

### Rerank requests per minute per model

| Reranking model      | Starter plan  | Standard plan | Enterprise plan |
| :------------------- | :------------ | :------------ | :-------------- |
| `cohere-rerank-3.5`  | Not available | 300           | 300             |
| `bge-reranker-v2-m3` | 60            | 60            | 60              |
| `pinecone-rerank-v0` | 60            | 60            | 60              |

When you reach the per minute request limit for a [reranking model](/guides/search/rerank-results#reranking-models) hosted by Pinecone, additional reranking requests will fail and return a `429 - TOO_MANY_REQUESTS` status with the following error:

```
Request failed. You've reached the max rerank requests per minute (<limit>) for model '<model name>' for the current project. 
To increase this limit, upgrade your plan.
```

To increase this limit, [upgrade your plan](/guides/organizations/manage-billing/upgrade-billing-plan).

### Rerank requests per month per model

| Reranking model      | Starter plan  | Standard plan | Enterprise plan |
| :------------------- | :------------ | :------------ | :-------------- |
| `cohere-rerank-3.5`  | Not available | Unlimited     | Unlimited       |
| `bge-reranker-v2-m3` | 500           | Unlimited     | Unlimited       |
| `pinecone-rerank-v0` | 500           | Unlimited     | Unlimited       |

When you reach the monthly request limit for a [reranking model](/guides/search/rerank-results#reranking-models) hosted by Pinecone, additional reranking requests will fail and return a `429 - TOO_MANY_REQUESTS` status with the following error:

```
Request failed. You've reached the rerank request limit (<limit>) for model <model name> for the current month. 
To continue using this model, upgrade your plan.
```

To increase this limit, [upgrade your plan](/guides/organizations/manage-billing/upgrade-billing-plan) or [contact Support](https://app.pinecone.io/organizations/-/settings/support/ticket).


## Object limits

Object limits are restrictions on the number or size of objects in Pinecone. Object limits vary based on [pricing plan](https://www.pinecone.io/pricing/).

| Metric                                                                         | Starter plan | Standard plan | Enterprise plan |
| :----------------------------------------------------------------------------- | :----------- | :------------ | :-------------- |
| [Projects per organization](#projects-per-organization)                        | 1            | 20            | 100             |
| [Serverless indexes per project](#serverless-indexes-per-project) <sup>1</sup> | 5            | 20            | 200             |
| [Serverless index storage per project](#serverless-index-storage-per-project)  | 2 GB         | N/A           | N/A             |
| [Namespaces per serverless index](#namespaces-per-serverless-index)            | 100          | 100,000       | 100,000         |
| [Serverless backups per project](#serveless-backups-per-project)               | N/A          | 500           | 1000            |
| [Namespaces per serverless backup](#namespaces-per-serverless-backup)          | N/A          | 2000          | 2000            |
| [Collections per project](#collections-per-project)                            | 100          | N/A           | N/A             |

<sup>1 On the Starter plan, all serverless must be in the `us-east-1` region of AWS.</sup><br />

### Projects per organization

| Starter plan | Standard plan | Enterprise plan |
| ------------ | ------------- | --------------- |
| 1            | 20            | 100             |

When you reach this quota for an organization, trying to [create projects](/guides/projects/create-a-project) will fail and return a `403 - QUOTA_EXCEEDED` status with the following error:

```
Request failed. You've reached the max projects allowed in organization <org name>. 
To add more projects, upgrade your plan.
```

To increase this quota, [upgrade your plan](/guides/organizations/manage-billing/upgrade-billing-plan) or [contact Support](https://app.pinecone.io/organizations/-/settings/support/ticket).

### Serverless indexes per project

| Starter plan | Standard plan | Enterprise plan |
| ------------ | ------------- | --------------- |
| 5            | 20            | 200             |

When you reach this quota for a project, trying to [create serverless indexes](/guides/index-data/create-an-index#create-a-serverless-index) in the project will fail and return a `403 - QUOTA_EXCEEDED` status with the following error:

```
Request failed. You've reached the max serverless indexes allowed in project <project>. 
Use namespaces to partition your data into logical groups, or upgrade your plan to add more serverless indexes.
```

To stay under this quota, consider using [namespaces](/guides/index-data/create-an-index#namespaces) instead of creating multiple indexes. Namespaces let you partition your data into logical groups within a single index. This approach not only helps you stay within index limits, but can also improve query performance and lower costs by limiting searches to relevant data subsets.

To increase this quota, [upgrade your plan](/guides/organizations/manage-billing/upgrade-billing-plan).

### Serverless index storage per project

<Note>This limit applies to organizations on the Starter plan only.</Note>

| Starter plan | Standard plan | Enterprise plan |
| ------------ | ------------- | --------------- |
| 2 GB         | N/A           | N/A             |

When you've reached this quota for a project, updates and upserts into serverless indexes will fail and return a `403 - QUOTA_EXCEEDED` status with the following error:

```
Request failed. You've reached the max storage allowed for project <project name>. 
To update or upsert new data, delete records or upgrade your plan.
```

To continue writing data into your serverless indexes, [delete records](/guides/manage-data/delete-data) to bring your project under the limit or [upgrade your plan](/guides/organizations/manage-billing/upgrade-billing-plan).

### Namespaces per serverless index

| Starter plan | Standard plan | Enterprise plan |
| ------------ | ------------- | --------------- |
| 100          | 100,000       | 100,000         |

When you reach this quota for a serverless index, trying to [upsert records into a new namespace](/guides/index-data/upsert-data) in the index will fail and return a `403 - QUOTA_EXCEEDED` status with the following error:

```
Request failed. You've reached the max namespaces allowed in serverless index <index name>. 
To add more namespaces, upgrade your plan.
```

To increase this quota, [upgrade your plan](/guides/organizations/manage-billing/upgrade-billing-plan).

<Note>
  While the Standard and Enterprise plans support up to [100,000 namespaces per index](/reference/api/database-limits#namespaces-per-serverless-index), Pinecone can accommodate million-scale namespaces and beyond for specific use cases. If your application requires more than 100,000 namespaces, [contact Support](https://app.pinecone.io/organizations/-/settings/support/ticket).
</Note>

### Serverless backups per project

| Starter plan | Standard plan | Enterprise plan |
| ------------ | ------------- | --------------- |
| N/A          | 500           | 1000            |

When you reach this quota for a project, trying to [create serverless backups](/guides/manage-data/back-up-an-index) in the project will fail and return a `403 - QUOTA_EXCEEDED` status with the following error:

```
Backup failed to create. Quota for number of backups per index exceeded.
```

### Namespaces per serverless backup

| Starter plan | Standard plan | Enterprise plan |
| ------------ | ------------- | --------------- |
| N/A          | 2000          | 2000            |

When you reach this quota for a backup, trying to [create serverless backups](/guides/manage-data/back-up-an-index) will fail and return a `403 - QUOTA_EXCEEDED` status.

### Collections per project

| Starter plan | Standard plan | Enterprise plan |
| ------------ | ------------- | --------------- |
| 100          | N/A           | N/A             |

When you reach this quota for a project, trying to [create collections](/guides/manage-data/back-up-an-index) in the project will fail and return a `403 - QUOTA_EXCEEDED` status with the following error:

```
Request failed. You've reached the max collections allowed in project <project name>. 
To add more collections, upgrade your plan.
```

To increase this quota, [upgrade your plan](/guides/organizations/manage-billing/upgrade-billing-plan).


## Operation limits

Operation limits are restrictions on the size, number, or other characteristics of operations in Pinecone. Operation limits are fixed and do not vary based on pricing plan.

### Upsert limits

| Metric                                                             | Limit                                                         |
| :----------------------------------------------------------------- | :------------------------------------------------------------ |
| Max [batch size](/guides/index-data/upsert-data#upsert-in-batches) | 2 MB or 1000 records with vectors <br /> 96 records with text |
| Max metadata size per record                                       | 40 KB                                                         |
| Max length for a record ID                                         | 512 characters                                                |
| Max dimensionality for dense vectors                               | 20,000                                                        |
| Max non-zero values for sparse vectors                             | 2048                                                          |
| Max dimensionality for sparse vectors                              | 4.2 billion                                                   |

### Import limits

<Note>
  If your import exceeds these limits, you'll get an `Exceeds system limit` error. Pinecone can help unblock these imports quickly. [Contact Pinecone support](https://app.pinecone.io/organizations/-/settings/support/ticket) for assistance.
</Note>

| Metric                    | Limit   |
| :------------------------ | :------ |
| Max namespaces per import | 10,000  |
| Max size per namespace    | 500 GB  |
| Max files per import      | 100,000 |
| Max size per file         | 10 GB   |

### Query limits

| Metric            | Limit  |
| :---------------- | :----- |
| Max `top_k` value | 10,000 |
| Max result size   | 4MB    |

The query result size is affected by the dimension of the dense vectors and whether or not dense vector values and metadata are included in the result.

<Tip>
  If a query fails due to exceeding the 4MB result size limit, choose a lower `top_k` value, or use `include_metadata=False` or `include_values=False` to exclude metadata or values from the result.
</Tip>

### Fetch limits

| Metric                           | Limit |
| :------------------------------- | :---- |
| Max record IDs per fetch request | 1,000 |

### Delete limits

| Metric                            | Limit |
| :-------------------------------- | :---- |
| Max record IDs per delete request | 1,000 |


## Identifier limits

An identifier is a string of characters (up to 255 characters in length) used to identify "named" [objects in Pinecone](/guides/get-started/concepts). The following Pinecone objects use strings as identifiers:

| Object                                                    | Field       | Max # characters | Allowed characters           |
| --------------------------------------------------------- | ----------- | ---------------- | ---------------------------- |
| [Organization](/guides/get-started/concepts#organization) | `name`      | 512              | UTF-8 except `\0`            |
| [Project](/guides/get-started/concepts#project)           | `name`      | 512              | UTF-8 except `\0`            |
| [Index](/guides/get-started/concepts#index)               | `name`      | 45               | `A-Z`, `a-z`, `0-9`, and `-` |
| [Namespace](/guides/get-started/concepts#namespace)       | `namespace` | 512              | ASCII except `\0`            |
| [Record](/guides/get-started/concepts#record)             | `id`        | 512              | ASCII except `\0`            |



# Errors
Source: https://docs.pinecone.io/reference/api/errors



Pinecone uses conventional HTTP response codes to indicate the success or failure of an API request. In general, codes in the `2xx` range indicate success, codes in the `4xx` range indicate an error that failed given the information provided, and codes in the `5xx` range indicate an error with Pinecone's servers.

For guidance on handling errors in production, see [Error handling](/guides/production/error-handling).


## 200 - OK

The request succeeded.


## 201 - CREATED

The request succeeded and a new resource was created.


## 202 - NO CONTENT

The request succeeded, but there is no content to return.


## 400 - INVALID ARGUMENT

The request failed due to an invalid argument.


## 401 - UNAUTHENTICATED

The request failed due to a missing or invalid [API key](/guides/projects/understanding-projects#api-keys).


## 402 - PAYMENT REQUIRED

The request failed due to delinquent payment.


## 403 - FORBIDDEN

The request failed due to an exceeded [quota](/reference/api/database-limits#object-limits) or [index deletion protection](/guides/manage-data/manage-indexes#configure-deletion-protection).


## 404 - NOT FOUND

The request failed because the resource was not found.


## 409 - ALREADY EXISTS

The request failed because the resource already exists.


## 412 - FAILED PRECONDITIONS

The request failed due to preconditions not being met. |


## 422 - UNPROCESSABLE ENTITY

The request failed because the server was unable to process the contained instructions.


## 429 - TOO MANY REQUESTS

The request was [rate-limited](/reference/api/database-limits#rate-limits). [Implement retry logic with exponential backoff](/guides/production/error-handling#handle-rate-limits-429) to handle this error.


## 500 - UNKNOWN

An internal server error occurred. [Implement retry logic with exponential backoff](/guides/production/error-handling#implement-retry-logic) to handle transient errors.


## 502 - BAD GATEWAY

The API gateway received an invalid response from a backend service. This is typically a temporary error. [Implement retry logic with exponential backoff](/guides/production/error-handling#implement-retry-logic) to handle transient errors.


## 503 - UNAVAILABLE

The server is currently unavailable. [Implement retry logic with exponential backoff](/guides/production/error-handling#implement-retry-logic) to handle transient errors.


## 504 - GATEWAY TIMEOUT

The API gateway did not receive a timely response from the backend server. This can occur due to slow requests or backend processing delays. [Implement retry logic with exponential backoff](/guides/production/error-handling#implement-retry-logic) to handle transient errors.



# API reference
Source: https://docs.pinecone.io/reference/api/introduction



Pinecone's APIs let you interact programmatically with your Pinecone account.

<Note>
  [SDK versions](/reference/pinecone-sdks#sdk-versions) are pinned to specific API versions.
</Note>


## Database

Use the Database API to store and query records in [Pinecone Database](/guides/get-started/quickstart).

The following Pinecone SDKs support the Database API:

<CardGroup cols={3}>
  <Card title="Python SDK" icon="python" href="/reference/python-sdk" />

  <Card title="Node.js SDK" icon="node-js" href="/reference/node-sdk" />

  <Card title="Java SDK" icon="java" href="/reference/java-sdk" />

  <Card title="Go SDK" icon="golang" href="/reference/go-sdk" />

  <Card title=".NET SDK" icon="microsoft" href="/reference/dotnet-sdk" />

  <Card title="Rust SDK" icon="rust" href="/reference/rust-sdk" />
</CardGroup>


## Inference

Use the Inference API to generate vector embeddings and rerank results using [embedding models](/guides/index-data/create-an-index#embedding-models) and [reranking models](/guides/search/rerank-results#reranking-models) hosted on Pinecone's infrastructure.

There are two ways to use the Inference API:

* As a standalone service, through the [Rerank documents](/reference/api/latest/inference/rerank) and [Generate vectors](/reference/api/latest/inference/generate-embeddings) endpoints.
* As an integrated part of database operations, through the [Create an index with integrated embedding](/reference/api/latest/control-plane/create_for_model), [Upsert text](/reference/api/latest/data-plane/upsert_records), and [Search with text](/reference/api/latest/data-plane/search_records) endpoints.

The following Pinecone SDKs support using the Inference API:

<CardGroup cols={3}>
  <Card title="Python SDK" icon="python" href="/reference/python-sdk" />

  <Card title="Node.js SDK" icon="node-js" href="/reference/node-sdk" />

  <Card title="Java SDK" icon="java" href="/reference/java-sdk" />

  <Card title="Go SDK" icon="golang" href="/reference/go-sdk" />

  <Card title=".NET SDK" icon="microsoft" href="/reference/dotnet-sdk" />
</CardGroup>



# Known limitations
Source: https://docs.pinecone.io/reference/api/known-limitations



This page describes known limitations and feature restrictions in Pinecone.


## General

* [Upserts](/guides/index-data/upsert-data)
  * Pinecone is eventually consistent, so there can be a slight delay before upserted records are available to query.

    After upserting records, use the [`describe_index_stats`](/reference/api/2024-10/data-plane/describeindexstats) operation to check if the current vector count matches the number of records you expect, although this method may not work for pod-based indexes with multiple replicas.
  * Only indexes using the [dotproduct distance metric](/guides/index-data/indexing-overview#dotproduct) support querying sparse-dense vectors.

    Upserting, updating, and fetching sparse-dense vectors in indexes with a different distance metric will succeed, but querying will return an error.
  * Indexes created before February 22, 2023 do not support sparse vectors.
* [Metadata](/guides/index-data/upsert-data#upsert-with-metadata-filters)
  * Null metadata values aren't supported. Instead of setting a key to `null`, remove the key from the metadata payload.
  * Nested JSON objects are not supported.


## Serverless indexes

Serverless indexes do not support the following features:

* [Filtering index statistics by metadata](/reference/api/2024-10/data-plane/describeindexstats)
* [Private endpoints](/guides/production/connect-to-aws-privatelink)

  * This feature is available on AWS only.



# API versioning
Source: https://docs.pinecone.io/reference/api/versioning



Pinecone's APIs are versioned to ensure that your applications continue to work as expected as the platform evolves. Versions are named by release date in the format `YYYY-MM`, for example, `2025-04`.


## Release schedule

On a quarterly basis, Pinecone releases a new **stable** API version as well as a **release candidate** of the next stable version.

* **Stable:** Each stable version remains unchanged and supported for a minimum of 12 months. Since stable versions are released every 3 months, this means you have at least 9 months to test and migrate your app to the newest stable version before support for the previous version is removed.

* **Release candidate:** The release candidate gives you insight into the upcoming changes in the next stable version. It is available for approximately 3 months before the release of the stable version and can include new features, improvements, and [breaking changes](#breaking-changes).

Below is an example of Pinecone's release schedule:

<img className="block max-w-full dark:hidden" noZoom src="https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/api-versioning.png?fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=be4366853edee83e003c3863e31fa1ce" data-og-width="2120" width="2120" data-og-height="960" height="960" data-path="images/api-versioning.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/api-versioning.png?w=280&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=66d593bf5bc7c842b28392daebb93c4a 280w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/api-versioning.png?w=560&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=c241a0f2c0e6e3ec3b1415e10a8516c8 560w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/api-versioning.png?w=840&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=0b88fe499a3c01dbd424ee943e9ab0c9 840w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/api-versioning.png?w=1100&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=fcdffc7f6d2b907681018e42cdbe0920 1100w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/api-versioning.png?w=1650&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=bc180b4a9a96edc502c5b49470ca3881 1650w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/api-versioning.png?w=2500&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=70bbd09f29afc200f6c9111495cd5f05 2500w" />

<img className="hidden max-w-full dark:block" noZoom src="https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/api-versioning-dark.png?fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=47a32d4f515a118a7500a0e2aec3beed" data-og-width="2120" width="2120" data-og-height="960" height="960" data-path="images/api-versioning-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/api-versioning-dark.png?w=280&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=deb21035b92a663a67b5cfe9420d999d 280w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/api-versioning-dark.png?w=560&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=8519ab97f6f889abeaab6105ea681e31 560w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/api-versioning-dark.png?w=840&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=dd4ef1e1e99cb42da31c83a7cd0d5e5d 840w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/api-versioning-dark.png?w=1100&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=927c7d86e73e85f417c832a96e98fdbb 1100w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/api-versioning-dark.png?w=1650&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=eb0c5f538f0b3422c475280f09476a62 1650w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/api-versioning-dark.png?w=2500&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=eacb669a6469064133034bdc1e30add1 2500w" />


## Specify an API version

<Warning>
  When using the API directly, it is important to specify an API version in your requests. If you don't, requests default to the oldest supported stable version. Once support for that version ends, your requests will default to the next oldest stable version, which could include breaking changes that require you to update your integration.
</Warning>

To specify an API version, set the `X-Pinecone-API-Version` header to the version name.

For example, based on the version support diagram above, if it is currently July 2024 and you want to use the latest stable version to describe an index, you would set `"X-Pinecone-API-Version: 2024-07"`:

```shell curl theme={null}
PINECONE_API_KEY="YOUR_API_KEY"

curl -i -X GET "https://api.pinecone.io/indexes/movie-recommendations" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-API-Version: 2024-07"
```

If you want to use the release candidate of the next stable version instead, you would set `"X-Pinecone-API-Version: 2024-10"`:

```shell curl theme={null}
PINECONE_API_KEY="YOUR_API_KEY"

curl -i -X GET "https://api.pinecone.io/indexes/movie-recommendations" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-API-Version: 2024-10"
```


## SDK versions

Official [Pinecone SDKs](/reference/pinecone-sdks) provide convenient access to Pinecone APIs. SDK versions are pinned to specific API versions. When a new API version is released, a new version of the SDK is also released.

For the mapping between SDK and API versions, see [SDK versions](/reference/pinecone-sdks#sdk-versions).


## Breaking changes

Breaking changes are changes that can potentially break your integration with a Pinecone API. Breaking changes include:

* Removing an entire operation
* Removing or renaming a parameter
* Removing or renaming a response field
* Adding a new required parameter
* Making a previously optional parameter required
* Changing the type of a parameter or response field
* Removing enum values
* Adding a new validation rule to an existing parameter
* Changing authentication or authorization requirements


## Non-breaking changes

Non-breaking changes are additive and should not break your integration. Additive changes include:

* Adding an operation
* Adding an optional parameter
* Adding an optional request header
* Adding a response field
* Adding a response header
* Adding enum values


## Get updates

To ensure you always know about upcoming API changes, follow the [Release notes](/release-notes/).



# Notebooks
Source: https://docs.pinecone.io/examples/notebooks



export const UtilityExampleCard = ({title, text, link}) => {
  return <a href={link} className="example-card group">
            <h2 className="font-bold" style={{
    fontSize: "0.875rem"
  }}>{title}</h2>
            <p style={{
    fontSize: "0.875rem",
    marginTop: "0"
  }}>{text}</p>
        </a>;
};

export const ExampleCard = ({title, text, link, children, arrow, vectors, namespaces}) => {
  return <a href={link} className="example-card group">
            <h2 className="font-semibold text-base">{title}</h2>
            <p>{text}</p>

            {children && <div className="tags">{children}</div>}

            {arrow && <svg xmlns="http://www.w3.org/2000/svg" className="arrow" width="24" height="24" viewBox="0 0 24 24" fill="none">
                <path d="M5.30739 20L4 18.6926L16.8249 5.8677H5.05837V4H20V18.9416H18.1323V7.1751L5.30739 20Z" fill="var(--text-secondary)" />
            </svg>}

            {(vectors || namespaces) && <div className="vectors">
                {vectors && <span>{vectors} vectors</span>}
                {namespaces && <span>{namespaces} namespaces</span>}
            </div>}
        </a>;
};

export const Tag = ({text, icon}) => {
  return <span className="card-tag">
            {icon && <img src={icon} className={`w-4 h-4 object-contain ${icon.includes("openai") ? "dark-inverted" : ""}`} />}
            {text}
        </span>;
};

<h2 className="examples-h2">Search</h2>

<div className="card-grid not-prose">
  <ExampleCard title="Semantic search" text="Implement semantic search over a dense index to find records that are similar in meaning to a given query." link="https://colab.research.google.com/github/pinecone-io/examples/blob/master/docs/semantic-search.ipynb" arrow>
    <Tag text="Pinecone Integrated Inference" />

    <Tag text="Hugging Face Datasets" icon="https://mintlify.s3-us-west-1.amazonaws.com/pinecone-2-sample-apps/images/examples/huggingface-icon.svg" />

    <Tag text="llama-text-embed-v2" />
  </ExampleCard>

  <ExampleCard title="Lexical search" text="Implement lexical search over a sparse index to find records that most exactly match the words or phrases in a query." link="https://colab.research.google.com/github/pinecone-io/examples/blob/master/docs/lexical-search.ipynb" arrow>
    <Tag text="Pinecone Integrated Inference" />

    <Tag text="pinecone-sparse-english-v0" />

    <Tag text="bge-reranker-v2-m3" />
  </ExampleCard>

  <ExampleCard title="Cascading retrieval" text="Implement cascading retrieval (hybrid search with two indexes) to combine the benefits of semantic and lexical search." link="https://colab.research.google.com/github/pinecone-io/examples/blob/master/docs/cascading-retrieval.ipynb" arrow>
    <Tag text="Pinecone Integrated Inference" />

    <Tag text="llama-text-embed-v2" />

    <Tag text="pinecone-sparse-english-v0" />

    <Tag text="bge-reranker-v2-m3" />
  </ExampleCard>

  <ExampleCard title="Reranking search results" text="Use Pinecone's reranking feature to enhance the accuracy of search results." link="https://colab.research.google.com/github/pinecone-io/examples/blob/master/docs/pinecone-reranker.ipynb" arrow>
    <Tag text="Pinecone Inference" />

    <Tag text="bge-reranker-v2-m3" icon="https://cdn.sanity.io/images/vr8gru94/production/40b1d05ee1325e6d9e4886af4e76ff06d844faff-188x188.jpg" />
  </ExampleCard>
</div>

<h2 className="examples-h2">Retrieval-augmented generation (RAG)</h2>

<div className="card-grid not-prose">
  <ExampleCard title="RAG with hybrid search and Claude" text="Implement simple retrieval-augmented generation with hybrid search and Anthropic's Claude models" link="https://colab.research.google.com/github/pinecone-io/examples/blob/master/learn/generation/traditional-rag/traditional-rag-with-claude-and-hybrid.ipynb" arrow>
    <Tag text="claude-3-5-haiku-latest" />

    <Tag text="llama-text-embed-v2" />

    <Tag text="pinecone-sparse-english-v0" />

    <Tag text="Dense Indexes" />

    <Tag text="Sparse Indexes" />

    <Tag text="Hybrid Search" />
  </ExampleCard>

  <ExampleCard title="Agentic RAG with Claude" text="Build an agentic RAG pipeline that uses tools to retrieve data from web search and Pinecone semantic search, then generates responses using Anthropic's Claude models" link="https://colab.research.google.com/github/pinecone-io/examples/blob/master/learn/generation/agentic-rag/agentic-rag-with-claude.ipynb" arrow>
    <Tag text="claude-3-5-haiku-latest" />

    <Tag text="llama-text-embed-v2" />

    <Tag text="Dense Indexes" />

    <Tag text="Tool use" />
  </ExampleCard>

  <ExampleCard title="RAG with LangChain and OpenAI" text="Learn how RAG can be used with Pinecone to reduce hallucinations, by grounding responses using our own release notes" link="https://colab.research.google.com/github/pinecone-io/examples/blob/master/docs/langchain-retrieval-augmentation.ipynb" arrow>
    <Tag text="gpt-5" icon="https://mintlify.s3-us-west-1.amazonaws.com/pinecone-2-sample-apps/images/examples/openai-icon.svg" />

    <Tag text="text-embedding-3-small" icon="https://mintlify.s3-us-west-1.amazonaws.com/pinecone-2-sample-apps/images/examples/openai-icon.svg" />

    <Tag text="OpenAI" />

    <Tag text="LangChain" />
  </ExampleCard>

  <ExampleCard title="RAG with cascading retrieval and OpenAI " text="Investigate research papers by implementing cascading retrieval, then pass results to OpenAI to generate answers" link="https://colab.research.google.com/github/pinecone-io/examples/blob/master/docs/gen-qa-openai.ipynb" arrow>
    <Tag text="gpt-4o-mini" icon="https://mintlify.s3-us-west-1.amazonaws.com/pinecone-2-sample-apps/images/examples/openai-icon.svg" />

    <Tag text="llama-text-embed-v2" />

    <Tag text="pinecone-sparse-english-v0" />

    <Tag text="Dense Indexes" />

    <Tag text="Sparse Indexes" />

    <Tag text="Cascading Retrieval" />
  </ExampleCard>

  <ExampleCard title="Retrieval Agents with Pinecone Assistant, LangChain and LangGraph" text="Create a study guide generator using agentic retrieval and the Pinecone Assistant Context API" link="https://colab.research.google.com/github/pinecone-io/examples/blob/master/docs/langchain-retrieval-agent.ipynb" arrow>
    <Tag text="gpt-4o-mini" icon="https://mintlify.s3-us-west-1.amazonaws.com/pinecone-2-sample-apps/images/examples/openai-icon.svg" />

    <Tag text="gpt-4.1" icon="https://mintlify.s3-us-west-1.amazonaws.com/pinecone-2-sample-apps/images/examples/openai-icon.svg" />

    <Tag text="LangChain" />

    <Tag text="LangGraph" />

    <Tag text="Agentic Retrieval" />

    <Tag text="Structured Generation" />
  </ExampleCard>
</div>

<h2 className="examples-h2">Miscellaneous</h2>

<div className="card-grid not-prose">
  <ExampleCard title="Import from object storage" text="Import records from Parquet files in Amazon S3 bucket into a serverless index." link="https://colab.research.google.com/github/pinecone-io/examples/blob/master/docs/pinecone-import.ipynb" arrow>
    <Tag text="Amazon S3" />
  </ExampleCard>
</div>



# Reference architectures
Source: https://docs.pinecone.io/examples/reference-architectures



<Card title="AWS Reference Architecture" icon="text-size" iconType="duotone">
  <br />

  The official AWS Reference Architecture for high-scale systems using Pinecone.

  <br />

  <a href="#" className="documentation-link">
    [Documentation](https://github.com/pinecone-io/aws-reference-architecture-pulumi/blob/main/README.md)
  </a>

  <a href="#" className="documentation-link">
    [Video tutorial](https://youtu.be/ySznARngHts)
  </a>

  <a href="#" className="documentation-link">
    [Source code](https://github.com/pinecone-io/aws-reference-architecture-pulumi)
  </a>
</Card>



# Sample apps
Source: https://docs.pinecone.io/examples/sample-apps



export const Tag = ({text, icon}) => {
  return <span className="card-tag">
            {icon && <img src={icon} className={`w-4 h-4 object-contain ${icon.includes("openai") ? "dark-inverted" : ""}`} />}
            {text}
        </span>;
};

export const UtilityExampleCard = ({title, text, link}) => {
  return <a href={link} className="example-card group">
            <h2 className="font-bold" style={{
    fontSize: "0.875rem"
  }}>{title}</h2>
            <p style={{
    fontSize: "0.875rem",
    marginTop: "0"
  }}>{text}</p>
        </a>;
};

export const ExampleCard = ({title, text, link, children, arrow, vectors, namespaces}) => {
  return <a href={link} className="example-card group">
            <h2 className="font-semibold text-base">{title}</h2>
            <p>{text}</p>

            {children && <div className="tags">{children}</div>}

            {arrow && <svg xmlns="http://www.w3.org/2000/svg" className="arrow" width="24" height="24" viewBox="0 0 24 24" fill="none">
                <path d="M5.30739 20L4 18.6926L16.8249 5.8677H5.05837V4H20V18.9416H18.1323V7.1751L5.30739 20Z" fill="var(--text-secondary)" />
            </svg>}

            {(vectors || namespaces) && <div className="vectors">
                {vectors && <span>{vectors} vectors</span>}
                {namespaces && <span>{namespaces} namespaces</span>}
            </div>}
        </a>;
};

<div>
  <div className="card-grid not-prose">
    <ExampleCard title="Semantic search" text="The Legal Semantic Search app shows you how to perform semantic search over PDF documents." link="/examples/sample-apps/legal-semantic-search">
      <Tag text="NextJS" icon="https://mintlify.s3-us-west-1.amazonaws.com/pinecone-2-sample-apps/images/examples/nextjs.svg" />

      <Tag text="OpenAI" icon="https://mintlify.s3-us-west-1.amazonaws.com/pinecone-2-sample-apps/images/examples/openai-icon.svg" />
    </ExampleCard>

    <ExampleCard title="Multi-tenant RAG" text="Namespace Notes is a simple multi-tenant RAG app. Upload documents that feed workspaces with context isolated by namespace." link="/examples/sample-apps/namespace-notes">
      <Tag text="NextJS" icon="https://mintlify.s3-us-west-1.amazonaws.com/pinecone-2-sample-apps/images/examples/nextjs.svg" />

      <Tag text="OpenAI" icon="https://mintlify.s3-us-west-1.amazonaws.com/pinecone-2-sample-apps/images/examples/openai-icon.svg" />
    </ExampleCard>

    <ExampleCard title="Multimodal search" text="The Shop the Look app shows you how to build multimodal search across text, images, and videos." link="/examples/sample-apps/shop-the-look">
      <Tag text="NextJS" icon="https://mintlify.s3-us-west-1.amazonaws.com/pinecone-2-sample-apps/images/examples/nextjs.svg" />

      <Tag text="Google Vertex AI" icon="/images/google-cloud-vertex-ai.svg" />
    </ExampleCard>

    <ExampleCard title="Pinecone Assistant" text="The Pinecone Assistant app connects a chat interface to your Pinecone Assistant to answer complex questions on your data." link="/examples/sample-apps/pinecone-assistant">
      <Tag text="NextJS" icon="https://mintlify.s3-us-west-1.amazonaws.com/pinecone-2-sample-apps/images/examples/nextjs.svg" />
    </ExampleCard>
  </div>

  <h2 className="examples-h2">More code examples</h2>

  <div className="card-grid not-prose">
    <UtilityExampleCard title="Use the Python SDK with FastAPI" text="A FastAPI app to demonstrate how to use the Pinecone Python SDK with asyncio support." link="https://github.com/pinecone-io/fastapi-pinecone-async-example" />

    <UtilityExampleCard title="Implement semantic search with TypeScript" text="A simple semantic search app written in TypeScript." link="https://github.com/pinecone-io/semantic-search-example" />

    <UtilityExampleCard title="Build an article recommender with TypeScript" text="A simple article recommender app written in TypeScript." link="https://github.com/pinecone-io/recommender-example-typescript" />

    <UtilityExampleCard title="Create a chatbot agent with LangChain" text="A conversational agent built with LangChain and TypeScript." link="https://github.com/pinecone-io/langchain-retrieval-agent-example" />

    <UtilityExampleCard title="Implement image search with TypeScript" text="An image search app written in TypeScript." link="https://github.com/pinecone-io/image-search-example" />
  </div>
</div>



---
**Navigation:** [← Previous](./16-delete-vectors.md) | [Index](./index.md) | [Next →](./18-ai-engine.md)
