**Navigation:** [← Previous](./08-manage-serverless-indexes.md) | [Index](./index.md) | [Next →](./10-use-the-pinecone-mcp-server.md)

# Target an index
Source: https://docs.pinecone.io/guides/manage-data/target-an-index

Target an index by host or name for data operations such as upsert and query.

<Warning>
  **Do not target an index by name in production.**

  When you target an index by name for data operations such as `upsert` and `query`, the SDK gets the unique DNS host for the index using the `describe_index` operation. This is convenient for testing but should be avoided in production because `describe_index` uses a different API than data operations and therefore adds an additional network call and point of failure. Instead, you should get an index host once and cache it for reuse or specify the host directly.
</Warning>


## Target by index host (recommended)

This method is recommended for production:

<Note>
  When using Private Endpoints for private connectivity between your application and Pinecone, you must target the index using the [Private Endpoint URL](/guides/production/connect-to-aws-privatelink#run-data-plane-commands) for the host.
</Note>

<CodeGroup>
  ```Python Python {5} theme={null}
  from pinecone.grpc import PineconeGRPC as Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  index = pc.Index(host="INDEX_HOST")
  ```

  ```javascript JavaScript {6} theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  // For the Node.js SDK, you must specify both the index host and name.
  const index = pc.index("INDEX_NAME", "INDEX_HOST");
  ```

  ```java Java {11} theme={null}
  import io.pinecone.clients.Index;
  import io.pinecone.configs.PineconeConfig;
  import io.pinecone.configs.PineconeConnection;

  public class TargetIndexByHostExample {
      public static void main(String[] args) {
          PineconeConfig config = new PineconeConfig("YOUR_API_KEY");
          config.setHost("INDEX_HOST");
          PineconeConnection connection = new PineconeConnection(config);
          // For the Java SDK, you must specify both the index host and name.
          Index index = new Index(connection, "INDEX_NAME");
      }
  }
  ```

  ```go Go {21} theme={null}
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

      // This creates a new gRPC index connection, targeting the namespace "example-namespace"
      idxConnectionNs1, err := pc.Index(pinecone.NewIndexConnParams{Host: "INDEX_HOST", Namespace: "example-namespace"})
      if err != nil {
          log.Fatalf("Failed to create IndexConnection for Host %v: %v", idx.Host, err)
      }

      // This reuses the gRPC index connection, targeting a different namespace
  	idxConnectionNs2 := idxConnectionNs1.WithNamespace("example-namespace2")
  }
  ```

  ```csharp C# {5} theme={null}
  using Pinecone;

  var pinecone = new PineconeClient("YOUR_API_KEY");

  var index = pinecone.Index(host: "INDEX_HOST");
  ```
</CodeGroup>

### Get an index host

You can get the unique DNS host for an index from the Pinecone console or the Pinecone API.

To get an index host from the Pinecone console:

1. Open the [Pinecone console](https://app.pinecone.io/organizations/-/projects).
2. Select the project containing the index.
3. Select the index.
4. Copy the URL under **HOST**.

To get an index host from the Pinecone API, use the [`describe_index`](/reference/api/latest/control-plane/describe_index) operation, which returns the index host as the `host` value:

<CodeGroup>
  ```Python Python theme={null}
  from pinecone.grpc import PineconeGRPC as Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  pc.describe_index(name="docs-example")

  # Response:
  # {'deletion_protection': 'disabled',
  #  'dimension': 1536,
  #  'host': 'docs-example-4zo0ijk.svc.us-east1-aws.pinecone.io',
  #  'metric': 'cosine',
  #  'name': 'docs-example',
  #  'spec': {'serverless': {'cloud': 'aws', 'region': 'us-east-1'}},
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
  //    "host": "docs-example-4zo0ijk.svc.us-east1-aws.pinecone.io",
  //    "deletionProtection": "disabled",
  //    "spec": {
  //       "serverless": {
  //          "cloud": "aws",
  //          "region": "us-east-1"
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
          Pinecone pc = new Pinecone.Builder("YOUR_API_KEY").build();
          IndexModel indexModel = pc.describeIndex("docs-example");
          System.out.println(indexModel);
      }
  }

  // Response:
  // class IndexModel {
  //     name: docs-example-java
  //     dimension: 1536
  //     metric: cosine
  //     host: docs-example-4zo0ijk.svc.us-west2-aws.pinecone.io
  //     deletionProtection: enabled
  //     spec: class IndexModelSpec {
  //         pod: null
  //         serverless: class ServerlessSpec {
  //             cloud: aws
  //             region: us-east-1
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
  // 	"host": "docs-example-govk0nt.svc.apw5-4e34-81fa.pinecone.io",
  // 	"metric": "cosine",
  //  "deletion_protection": "disabled",
  // 	"spec": {
  // 	  "serverless": {
  // 		"cloud": "aws",
  // 		"region": "us-east-1"
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
  //   "host": "docs-example-govk0nt.svc.aped-4627-b74a.pinecone.io",
  //   "deletion_protection": "disabled",
  //   "spec": {
  //     "pod": null,
  //     "serverless": {
  //       "cloud": "aws",
  //       "region": "us-east-1"
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

  curl -i -X GET "https://api.pinecone.io/indexes/docs-example-curl" \
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
  #    "host": "docs-example-4zo0ijk.svc.us-east1-aws.pinecone.io",
  #    "spec": {
  #       "serverless": {
  #          "region": "us-east-1",
  #          "cloud": "aws"
  #       }
  #    }
  # }
  ```
</CodeGroup>


## Target by index name

This method is convenient for testing but is not recommended for production:

<CodeGroup>
  ```Python Python theme={null}
  from pinecone.grpc import PineconeGRPC as Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  index = pc.Index("docs-example")
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  // For the Node.js SDK, you must specify both the index host and name.
  const index = pc.index('docs-example');
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Index;
  import io.pinecone.clients.Pinecone;

  public class GenerateEmbeddings {
      public static void main(String[] args) throws ApiException {
          Pinecone pc = new Pinecone.Builder("YOUR_API_KEY").build();
          Index index = pc.getIndexConnection("docs-example");
      }
  }
  ```

  ```go Go theme={null}
  // It is not possible to target an index by name in the Go SDK. 
  // You must target an index by host.
  ```

  ```csharp C# theme={null}
  using Pinecone;

  var pinecone = new PineconeClient("YOUR_API_KEY");

  var index = pinecone.Index("docs-example");
  ```
</CodeGroup>



# Update records
Source: https://docs.pinecone.io/guides/manage-data/update-data

Update vectors and metadata for existing records

You can [update](/reference/api/latest/data-plane/update) a single record using the record ID or multiple records using a metadata filter.

* When updating by ID, you change the vector and/or metadata of a single record.
* When updating by metadata, you change metadata across multiple records using a metadata filter.

To update entire records, use the [upsert](/guides/index-data/upsert-data) operation instead.


## Update by ID

To update the vector and/or metadata of a single record, use the [`update`](/reference/api/latest/data-plane/update) operation with the following parameters:

* `namespace`: The [namespace](/guides/index-data/indexing-overview#namespaces) containing the record to update. To use the default namespace, set the namespace to `"__default__"`.
* `id`: The ID of the record to update.
* One or both of the following:
  * Updated values for the vector. Specify one of the following:
    * `values`: For dense vectors. Must have the same length as the existing vector.
    * `sparse_values`: For sparse vectors.
  * `setMetadata`: The metadata to add or change. When updating metadata, only the specified metadata fields are modified, and if a specified metadata field does not exist, it is added.

<Warning>
  If a non-existent record ID is specified, no records are affected and a `200 OK` status is returned.
</Warning>

In this example, assume you are updating the dense vector values and one metadata value of the following record in the `example-namespace` namespace:

```
(
    namespace="example-namespace",
    id="id-3", 
    values=[4.0, 2.0], 
    setMetadata={"type": "doc", "genre": "drama"}
)
```

<CodeGroup>
  ```Python Python theme={null}
  from pinecone.grpc import PineconeGRPC as Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  # To get the unique host for an index, 
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  index = pc.Index(host="INDEX_HOST")

  index.update(
  	namespace="example-namespace",
  	id="id-3", 
  	values=[5.0, 3.0], 
  	set_metadata={"genre": "comedy"}
  )
  ```

  ```JavaScript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({ apiKey: "YOUR_API_KEY" })

  // To get the unique host for an index, 
  // see https://docs.pinecone.io/guides/manage-data/target-an-index
  const index = pc.index("INDEX_NAME", "INDEX_HOST")

  await index.namespace('example-namespace').update({
    id: 'id-3',
    values: [5.0, 3.0],
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
          List<Float> values = Arrays.asList(5.0f, 3.0f);
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
          Values: []float32{5.0, 3.0},
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
      Namespace = "example-namespace",
      Values = new[] { 5.0f, 3.0f },
      SetMetadata = new Metadata {
          ["genre"] = new("comedy")
      }
  });
  ```

  ```bash curl theme={null}
  # To get the unique host for an index,
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="INDEX_HOST"

  # Update both values and metadata
  curl "https://$INDEX_HOST/vectors/update" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H 'Content-Type: application/json' \
    -H "X-Pinecone-API-Version: 2025-04" \
    -d '{
          "id": "id-3",
          "values": [5.0, 3.0],
          "setMetadata": {"genre": "comedy"},
          "namespace": "example-namespace"
        }'
  ```
</CodeGroup>

After the update, the dense vector values and the `genre` metadata value are changed, but the `type` metadata value is unchanged:

```
(
    id="id-3", 
    values=[5.0, 3.0], 
    metadata={"type": "doc", "genre": "comedy"}
)
```


## Update by metadata

<Warning>
  This feature is in [public preview](/release-notes/feature-availability) and is available only on the `2025-10` version of the API. See [limitations](#limitations) for details.
</Warning>

To add or change metadata across multiple records in a namespace, use the `update` operation with the following parameters:

* `namespace`: The [namespace](/guides/index-data/indexing-overview#namespaces) containing the records to update. To use the default namespace, set this to `"__default__"`.
* `filter`: A [metadata filter expression](/guides/index-data/indexing-overview#metadata-filter-expressions) to match the records to update.
* `setMetadata`: The metadata to add or change. When updating metadata, only the specified metadata fields are modified. If a specified metadata field does not exist, it is added.
* `dry_run`: Optional. If `true`, the number of records that match the filter expression is returned, but the records are not updated.

  <Note>
    Each request updates a maximum of 100,000 records. Use `"dry_run": true` to check if you need to run the request multiple times. See the example below for details.
  </Note>

For example, let's say you have records that represent chunks of a single document with metadata that keeps track of chunk and document details, and you want to store the author's name with each chunk of the document:

```json  theme={null}
{
    "id": "document1#chunk1", 
    "values": [0.0236663818359375, -0.032989501953125, ..., -0.01041412353515625, 0.0086669921875], 
    "metadata": {
        "document_id": "document1",
        "document_title": "Introduction to Vector Databases",
        "chunk_number": 1,
        "chunk_text": "First chunk of the document content...",
        "document_url": "https://example.com/docs/document1"
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
        "document_url": "https://example.com/docs/document1"
    }
},
...
```

1. To check how many records match the filter expression, send a request with `"dry_run": true`:

   ```bash curl {11} theme={null}
   # To get the unique host for an index,
   # see https://docs.pinecone.io/guides/manage-data/target-an-index
   PINECONE_API_KEY="YOUR_API_KEY"
   INDEX_HOST="INDEX_HOST"

   curl "https://$INDEX_HOST/vectors/update" \
       -H "Api-Key: $PINECONE_API_KEY" \
       -H 'Content-Type: application/json' \
       -H "X-Pinecone-API-Version: 2025-10" \
       -d '{
               "dry_run": true,
               "namespace": "example-namespace",
               "filter": {
                   "document_title": {"$eq": "Introduction to Vector Databases"}
               },
               "setMetadata": {
                   "author": "Del Klein"
               } 
           }'
   ```

   The response contains the number of records that match the filter expression:

   ```json  theme={null}
   {
       "matchedVectors": 150000
   }
   ```

   Since this number exceeds the 100,000 record limit, you'll need to run the update request multiple times.

2. Initiate the first update by sending the request without the `dry_run` parameter:

   ```bash curl theme={null}
   curl "https://$INDEX_HOST/vectors/update" \
       -H "Api-Key: $PINECONE_API_KEY" \
       -H 'Content-Type: application/json' \
       -H "X-Pinecone-API-Version: 2025-10" \
       -d '{
               "namespace": "example-namespace",
               "filter": {
                   "document_title": {"$eq": "Introduction to Vector Databases"}
               },
               "setMetadata": {
                   "author": "Del Klein"
               } 
           }'
   ```

   Again, the response contains the total number of records that match the filter expression, but only 100,000 will be updated:

   ```json  theme={null}
   {
       "matchedVectors": 150000
   }
   ```

3. Pinecone is eventually consistent, so there can be a slight delay before your update request is processed. Repeat the `dry_run` request until the number of matching records shows that the first 100,000 records have been updated:

   ```bash curl {11} theme={null}
   # To get the unique host for an index,
   # see https://docs.pinecone.io/guides/manage-data/target-an-index
   PINECONE_API_KEY="YOUR_API_KEY"
   INDEX_HOST="INDEX_HOST"

   curl "https://$INDEX_HOST/vectors/update" \
       -H "Api-Key: $PINECONE_API_KEY" \
       -H 'Content-Type: application/json' \
       -H "X-Pinecone-API-Version: 2025-10" \
       -d '{
               "dry_run": true,
               "namespace": "example-namespace",
               "filter": {
                   "document_title": {"$eq": "Introduction to Vector Databases"}
               },
               "setMetadata": {
                   "author": "Del Klein"
               } 
           }'
   ```

   ```json  theme={null}
   {
       "matchedVectors": 50000
   }
   ```

4. Once the first 100,000 records have been updated, update the remaining records:

   ```bash curl theme={null}
   curl "https://$INDEX_HOST/vectors/update" \
       -H "Api-Key: $PINECONE_API_KEY" \
       -H 'Content-Type: application/json' \
       -H "X-Pinecone-API-Version: 2025-10" \
       -d '{
               "namespace": "example-namespace",
               "filter": {
                   "document_title": {"$eq": "Introduction to Vector Databases"}
               },
               "setMetadata": {
                   "author": "Del Klein"
               } 
           }'
   ```

5. Repeat the `dry_run` request until the number of matching records shows that the remaining records have been updated:

   ```bash curl {11} theme={null}
   # To get the unique host for an index,
   # see https://docs.pinecone.io/guides/manage-data/target-an-index
   PINECONE_API_KEY="YOUR_API_KEY"
   INDEX_HOST="INDEX_HOST"

   curl "https://$INDEX_HOST/vectors/update" \
       -H "Api-Key: $PINECONE_API_KEY" \
       -H 'Content-Type: application/json' \
       -H "X-Pinecone-API-Version: 2025-10" \
       -d '{
               "dry_run": true,
               "namespace": "example-namespace",
               "filter": {
                   "document_title": {"$eq": "Introduction to Vector Databases"}
               },
               "setMetadata": {
                   "author": "Del Klein"
               } 
           }'
   ```

   ```json  theme={null}
   {
       "matchedVectors": 0
   }
   ```

   Once the request has completed, all matching records include the author name as metadata:

   ```json {10,22} theme={null}
   {
       "id": "document1#chunk1", 
       "values": [0.0236663818359375, -0.032989501953125, ..., -0.01041412353515625, 0.0086669921875], 
       "metadata": {
           "document_id": "document1",
           "document_title": "Introduction to Vector Databases",
           "chunk_number": 1,
           "chunk_text": "First chunk of the document content...",
           "document_url": "https://example.com/docs/document1",
           "author": "Del Klein"
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
           "author": "Del Klein"
       }
   },
   ...
   ```

### Limitations

* This feature is available only on the `2025-10` version of the API.
* Each request updates a maximum of 100,000 records. Use `"dry_run": true` to check if you need to run the request multiple times. See the example above for details.
* You can add or change metadata across multiple records, but you cannot remove metadata fields.


## Data freshness

Pinecone is eventually consistent, so there can be a slight delay before updates are visible to queries. You can [use log sequence numbers](/guides/index-data/check-data-freshness#check-the-log-sequence-number) to check whether an update request has completed.



# Integrate with Amazon S3
Source: https://docs.pinecone.io/guides/operations/integrations/integrate-with-amazon-s3

Set up Amazon S3 integrationfor data import and audit logs.

<Note>
  This feature is in [public preview](/release-notes/feature-availability) and available only on [Standard and Enterprise plans](https://www.pinecone.io/pricing/).
</Note>

This page shows you how to integrate Pinecone with an Amazon S3 bucket. Once your integration is set up, you can use it to [import data](/guides/index-data/import-data) from your Amazon S3 bucket into a Pinecone index hosted on AWS, or to [export audit logs](/guides/production/configure-audit-logs) to your Amazon S3 bucket.


## Before you begin

Ensure you have the following:

* A [Pinecone account](https://app.pinecone.io/).
* An [Amazon S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-buckets.html).


## 1. Create an IAM policy

In the [AWS IAM console](https://console.aws.amazon.com/iam/home):

1. In the navigation pane, click **Policies**.
2. Click **Create policy**.
3. In **Select a service** section, select **S3**.
4. Select the following actions to allow:
   * `ListBucket`: Permission to list some or all of the objects in an S3 bucket. Required for [importing data](/guides/index-data/import-data) and [exporting audit logs](/guides/production/configure-audit-logs).
   * `GetObject`: Permission to retrieve objects from an S3 bucket. Required for [importing data](/guides/index-data/import-data).
   * `PutObject`: Permission to add an object to an S3 bucket. Required for [exporting audit logs](/guides/production/configure-audit-logs).
5. In the **Resources** section, select **Specific**.
6. For the **bucket**, specify the ARN of the bucket you created. For example: `arn:aws:s3:::example-bucket-name`
7. For the **object**, specify an object ARN as the target resource. For example: `arn:aws:s3:::example-bucket-name/*`
8. Click **Next**.
9. Specify the name of your policy. For example:  "Pinecone-S3-Access".
10. Click **Create policy**.

### Targeting a subdirectory (optional)

To write [audit logs](/guides/production/configure-audit-logs) to a specific subdirectory within your S3 bucket (e.g., `my-bucket/pinecone-logs/`), you need to configure your IAM policy differently for `ListBucket` vs. object-level actions:

1. For `ListBucket`, use a **Condition** block with `StringLike` to specify the prefix. Include both the directory path with and without the trailing wildcard:

   ```json  theme={null}
   {
       "Sid": "ListBucketWithPrefix",
       "Effect": "Allow",
       "Action": "s3:ListBucket",
       "Resource": "arn:aws:s3:::example-bucket-name",
       "Condition": {
           "StringLike": {
               "s3:prefix": [
                   "pinecone-logs/",
                   "pinecone-logs/*"
               ]
           }
       }
   }
   ```

2. For `PutObject` and `GetObject`, use the **Resource** specifier with the subdirectory path:

   ```json  theme={null}
   {
       "Sid": "ObjectActionsInSubdirectory",
       "Effect": "Allow",
       "Action": [
           "s3:PutObject",
           "s3:GetObject"
       ],
       "Resource": "arn:aws:s3:::example-bucket-name/pinecone-logs/*"
   }
   ```

**Complete example policy for subdirectory access:**

```json  theme={null}
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "ListBucketWithPrefix",
            "Effect": "Allow",
            "Action": "s3:ListBucket",
            "Resource": "arn:aws:s3:::example-bucket-name",
            "Condition": {
                "StringLike": {
                    "s3:prefix": [
                        "pinecone-logs/",
                        "pinecone-logs/*"
                    ]
                }
            }
        },
        {
            "Sid": "ObjectActionsInSubdirectory",
            "Effect": "Allow",
            "Action": [
                "s3:PutObject",
                "s3:GetObject"
            ],
            "Resource": "arn:aws:s3:::example-bucket-name/pinecone-logs/*"
        }
    ]
}
```

<Note>
  The key difference is that `ListBucket` operates on the bucket resource and uses conditions to filter by prefix, while object-level actions (`PutObject`, `GetObject`) operate directly on object resources specified in the ARN.
</Note>


## 2. Set up access using an IAM role

In the [AWS IAM console](https://console.aws.amazon.com/iam/home):

1. In the navigation pane, click **Roles**.

2. Click **Create role**.

3. In the **Trusted entity type** section, select **AWS account**.

4. Select **Another AWS account**.

5. Enter the Pinecone AWS VPC account ID: `713131977538`

6. Click **Next**.

7. Select the [policy you created](#1-create-an-iam-policy).

8. Click **Next**.

9. Specify the role name. For example: "Pinecone".

10. Click **Create role**.

11. Click the role you created.

12. On the **Summary** page for the role, find the **ARN**.

    For example: `arn:aws:iam::123456789012:role/PineconeAccess`

13. Copy the **ARN**.

    You will need to enter the ARN into Pinecone later.


## 3. Add a storage integration

<Note>
  This step is required for [importing data](/guides/index-data/import-data). It is not required for [storing audit logs](/guides/production/configure-audit-logs).
</Note>

In the [Pinecone console](https://app.pinecone.io/organizations/-/projects), add an integration with Amazon S3..

1. Select your project.
2. Go to [**Manage > Storage integrations**](https://app.pinecone.io/organizations/-/projects/-/storage).
3. Click **Add integration**.
4. Enter a unique integration name.
5. Select **Amazon S3**.
6. Enter the **ARN** of the [IAM role you created](/guides/operations/integrations/integrate-with-amazon-s3#2-set-up-access-using-an-iam-role).
7. Click **Add integration**.


## Next steps

* [Import data](/guides/index-data/import-data) from your Amazon S3 bucket into a Pinecone index.
* [Configure audit logs](/guides/production/configure-audit-logs) to export logs to your Amazon S3 bucket.



# Integrate with Azure Blob Storage
Source: https://docs.pinecone.io/guides/operations/integrations/integrate-with-azure-blob-storage

Set up Azure Blob Storage integration for data import.

<Note>
  This feature is in [public preview](/release-notes/feature-availability) and available only on [Standard and Enterprise plans](https://www.pinecone.io/pricing/).
</Note>

This page describes how to integrate Pinecone with Azure Blob Storage. After setting up an integration, you can [import data](/guides/index-data/import-data) from an Azure Blob Storage container into a Pinecone index hosted on AWS, GCP, or Azure.


## Before you begin

Ensure you have the following:

* A [Pinecone account](https://app.pinecone.io/)
* An [Azure Blob Storage container](https://learn.microsoft.com/azure/storage/blobs/storage-blobs-introduction)


## 1. Create an app registration and service principal

Pinecone uses a service principal to access your Azure Blob Storage container.

1. [Create an app registration](https://learn.microsoft.com/entra/identity-platform/quickstart-register-app) for your Pinecone integration. This automatically creates a service principal.

   When creating your app registration:

   * Do not specify a **Redirect URI**.
   * Copy the **Application (client) ID** and the **Directory (tenant) ID**. You'll use these values when adding a storage integration in Pinecone.

2. [Create a client secret](https://learn.microsoft.com/entra/identity-platform/how-to-add-credentials?tabs=client-secret) for the service principal.

   Copy the secret's **Value** (not its **ID**). You'll use this when creating a storage integration in Pinecone.


## 2. Grant access to the storage account

[Assign the service principal to your storage account](https://learn.microsoft.com/azure/storage/common/storage-auth-aad-rbac-portal#assign-azure-rbac-roles-using-the-azure-portal):

1. In the Azure portal, navigate to the subscription associated with your storage account.
2. Select **Access control (IAM)**.
3. Click **Add** > **Add role assignment**.
4. Select **Storage Blob Data Reader** or another role that has permission to list and read blobs in a container.
5. Click **Next**.
6. Select **User, group, or service principal** and click **Select members**.
7. Select the app you created in the previous step.
8. Click **Review + assign** (you may need to click this twice).


## 3. In Pinecone, add a storage integration

In the [Pinecone console](https://app.pinecone.io/organizations/-/projects), add an integration with Azure Blob Storage:

1. Select your project.
2. Go to [**Manage > Storage integrations**](https://app.pinecone.io/organizations/-/projects/-/storage).
3. Click **Add integration**.
4. Enter a unique integration name.
5. Select **Azure Blob Storage**.
6. For **Tenant ID**, **Client ID**, and **Client secret**, enter the values you copied from Azure.
7. Click **Add integration**.


## Next steps

[Import data](/guides/index-data/import-data) from your Azure Blob Storage container into your Pinecone index.



# Integrate with Google Cloud Storage
Source: https://docs.pinecone.io/guides/operations/integrations/integrate-with-google-cloud-storage

Integrate Google Cloud Storage for bulk data import

<Note>
  This feature is in [public preview](/release-notes/feature-availability) and available only on [Standard and Enterprise plans](https://www.pinecone.io/pricing/).
</Note>

This page shows you how to integrate Pinecone with a Google Cloud Storage (GCS) bucket. Once your integration is set up, you can use it to [import data](/guides/index-data/import-data) from your bucket into a Pinecone index hosted on AWS, GCP, or Azure.


## Before you begin

Ensure you have the following:

* A [Pinecone account](https://app.pinecone.io/)
* A [Google Cloud Storage bucket](https://cloud.google.com/storage/docs/creating-buckets)


## 1. Create a service account and key

Pinecone will use a service account to access your GCS bucket.

1. [Create a service account](https://cloud.google.com/iam/docs/service-accounts-create) for your Pinecone integration.
2. [Create a service account key](https://cloud.google.com/iam/docs/keys-create-delete#creating). Select **JSON** as the key type.

   The key will be downloaded to your computer. You'll use this key when adding a storage integration in Pinecone.


## 2. Grant access to the bucket

[Add your service account as a principal to the bucket](https://cloud.google.com/storage/docs/access-control/using-iam-permissions#bucket-add).

* For the principal, use your service account email address.
* For the role, select **Storage Object Viewer** or another role that has permission to list and read objects in a bucket.


## 3. Add a storage integration

In the [Pinecone console](https://app.pinecone.io/organizations/-/projects), add an integration with Google Cloud Storage:

1. Select your project.
2. Go to [**Manage > Storage integrations**](https://app.pinecone.io/organizations/-/projects/-/storage).
3. Click **Add integration**.
4. Enter a unique integration name.
5. Select **Google Cloud Storage**.
6. Open the JSON key file for your service account.
7. Copy the contents of the key file and paste them into the **Index account key JSON** field.
8. Click **Add integration**.


## Next steps

[Import data](/guides/index-data/import-data) from your GCS bucket into your Pinecone index.



# Manage storage integrations
Source: https://docs.pinecone.io/guides/operations/integrations/manage-storage-integrations

Update and manage cloud storage integrations.

<Note>
  This feature is in [public preview](/release-notes/feature-availability) and available only on [Standard and Enterprise plans](https://www.pinecone.io/pricing/).
</Note>

This page shows you how to manage storage integrations for your Pinecone project.

To set up cloud storage for integration with Pinecone, see the following guides:

* [Integrate with Amazon S3](/guides/operations/integrations/integrate-with-amazon-s3)
* [Integrate with Google Cloud Storage](/guides/operations/integrations/integrate-with-google-cloud-storage)
* [Integrate with Azure Blob Storage](/guides/operations/integrations/integrate-with-azure-blob-storage)


## Update an integration

To update information for a storage integration through the [Pinecone console](https://app.pinecone.io/organizations/-/projects), take the following steps:

1. Select your project.
2. Go to [**Manage > Storage integrations**](https://app.pinecone.io/organizations/-/projects/-/storage).
3. For the integration you want to update, click the *...* (Actions) icon.
4. Click **Manage**.
5. Update the integration details as needed.
6. Click **Add integration**.


## Delete an integration

To delete a storage integration through the [Pinecone console](https://app.pinecone.io/organizations/-/projects), take the following steps:

1. Select your project.
2. Go to [**Manage > Storage integrations**](https://app.pinecone.io/organizations/-/projects/-/storage).
3. For the integration you want to update, click the *...* (Actions) icon.
4. Click **Delete**.
5. Enter the integration name.
6. Click **Confirm deletion**.



# Local development with Pinecone Local
Source: https://docs.pinecone.io/guides/operations/local-development

Develop locally with an in-memory Pinecone emulator.

Pinecone Local is an in-memory Pinecone emulator available as a Docker image.

This page shows you how to use Pinecone Local to develop your applications locally without connecting to your Pinecone account or incurring usage or storage fees.

<Warning>
  Pinecone Local is not suitable for production. See [Limitations](#limitations) for details.
</Warning>

<Note>
  This feature is in [public preview](/release-notes/feature-availability).
</Note>


## Limitations

Pinecone Local has the following limitations:

* Pinecone Local uses the `2025-01` API version, which is not the latest stable version.
* Pinecone Local is available in Docker only.
* Pinecone Local is an in-memory emulator and is not suitable for production. Records loaded into Pinecone Local do not persist after it is stopped.
* Pinecone Local does not authenticate client requests. API keys are ignored.
* Max number of records per index: 100,000.

Pinecone Local does not currently support the following features:

* [Import from object storage](/guides/index-data/import-data)
* [Backup/restore of serverless indexes](/guides/manage-data/backups-overview)
* [Collections for pod-based indexes](/guides/indexes/pods/understanding-collections)
* [Namespace management](/guides/manage-data/manage-namespaces)
* [Pinecone Inference](/reference/api/introduction#inference)
* [Pinecone Assistant](/guides/assistant/overview)


## 1. Start Pinecone Local

You can configure Pinecone Local as an index emulator or database emulator:

* **Index emulator** - This approach uses the `pinecone-index` Docker image to create and configure indexes on startup. This is recommended when you want to quickly experiment with reading and writing data without needing to manage the index lifecycle.

  <Note>
    With index emulation, you can only read and write data to the indexes created at startup. You cannot create new indexes, list indexes, or run other operations that do not involve reading and writing data.
  </Note>

* **Database emulator** - This approach uses the `pinecone-local` Docker image to emulate Pinecone Database more broadly. This is recommended when you want to test your production app or manually create and manage indexes.

### Index emulator

<Tabs>
  <Tab title="Docker Compose">
    Make sure [Docker](https://docs.docker.com/get-docker/) is installed and running on your local machine.

    Create a `docker-compose.yaml` file that defines a service for each index that Pinecone Local should create on startup. In this file, include the `pinecone-index` Docker image, a localhost port for the index to use, and other details:

    ```yaml  theme={null}
    services:
      dense-index:
        image: ghcr.io/pinecone-io/pinecone-index:latest
        container_name: dense-index
        environment:
          PORT: 5081
          INDEX_TYPE: serverless
          VECTOR_TYPE: dense
          DIMENSION: 2 
          METRIC: cosine
        ports:
          - "5081:5081"
        platform: linux/amd64
      sparse-index:
        image: ghcr.io/pinecone-io/pinecone-index:latest
        container_name: sparse-index
        environment:
          PORT: 5082
          INDEX_TYPE: serverless
          VECTOR_TYPE: sparse
          DIMENSION: 0
          METRIC: dotproduct
        ports:
          - "5082:5082"
        platform: linux/amd64
    ```

    For each index, update the environment variables as needed:

    * `PORT`: Specify the port number for the index to listen on.
    * `INDEX_TYPE`: Specify the type of Pinecone index to create. Accepted values: `serverless` or `pod`.
    * `VECTOR_TYPE`: Specify the [type of vectors](/guides/index-data/indexing-overview#indexes) you will store in the index. Accepted values: `dense` or `sparse`.

      <Note>Sparse is supported only with serverless indexes.</Note>
    * `DIMENSION`: Specify the dimension of vectors you will store in the index.

      <Note>For sparse indexes, this must be set to `0`.</Note>
    * `METRIC`: Specify the [distance metric](/guides/index-data/indexing-overview#distance-metrics) for calculating the similarity between vectors in the index. Accepted values for dense indexes: `cosine`, `euclidean`, or `dotproduct`. Accepted value for sparse indexes: `dotproduct`.

    To start Pinecone Local, run the following command:

    ```shell  theme={null}
    docker compose up -d
    ```

    You'll see a message with details about each index.
  </Tab>

  <Tab title="Docker CLI">
    Make sure [Docker](https://docs.docker.com/get-docker/) is installed and running on your local machine.

    Download the latest `pinecone-index` Docker image:

    ```shell  theme={null}
    docker pull ghcr.io/pinecone-io/pinecone-index:latest
    ```

    Start Pinecone Local with one or more indexes:

    ```shell  theme={null}
    docker run -d \
    --name dense-index \
    -e PORT=5081 \
    -e INDEX_TYPE=serverless \
    -e VECTOR_TYPE=dense \
    -e DIMENSION=2 \
    -e METRIC=cosine \
    -p 5081:5081 \
    --platform linux/amd64 \
    ghcr.io/pinecone-io/pinecone-index:latest
    ```

    ```shell  theme={null}
    docker run -d \
    --name sparse-index \
    -e PORT=5082 \
    -e INDEX_TYPE=serverless \
    -e VECTOR_TYPE=sparse \
    -e DIMENSION=0 \
    -e METRIC=dotproduct \
    -p 5082:5082 \
    --platform linux/amd64 \
    ghcr.io/pinecone-io/pinecone-index:latest
    ```

    For each index, update the environment variables as needed:

    * `PORT`: Specify the port number for the index to listen on.
    * `INDEX_TYPE`: Specify the type of Pinecone index to create. Accepted values: `serverless` or `pod`.
    * `VECTOR_TYPE`: Specify the [type of vectors](/guides/index-data/indexing-overview#indexes) you will store in the index. Accepted values: `dense` or `sparse`.

      <Note>Sparse is supported only with serverless indexes.</Note>
    * `DIMENSION`: Specify the dimension of vectors you will store in the index.

      <Note>For sparse indexes, this must be set to `0`.</Note>
    * `METRIC`: Specify the [distance metric](/guides/index-data/indexing-overview#distance-metrics) for calculating the similarity between vectors in the index. Accepted values for dense indexes: `cosine`, `euclidean`, or `dotproduct`. Accepted value for sparse indexes: `dotproduct`.
  </Tab>
</Tabs>

### Database emulator

<Tabs>
  <Tab title="Docker Compose">
    Make sure [Docker](https://docs.docker.com/get-docker/) is installed and running on your local machine.

    Create a `docker-compose.yaml` file that defines a service for Pinecone local, including the `pinecone-local` Docker image, the host and port that Pinecone Local will run on and the range of ports that will be available for indexes:

    ```yaml  theme={null}
    services:
      pinecone:
        image: ghcr.io/pinecone-io/pinecone-local:latest
        environment: 
          PORT: 5080
          PINECONE_HOST: localhost
        ports: 
          - "5080-5090:5080-5090"
        platform: linux/amd64
    ```

    To start Pinecone Local, run the following command:

    ```shell  theme={null}
    docker compose up -d
    ```

    You'll see a message with details about the Pinecone Local instance.
  </Tab>

  <Tab title="Docker CLI">
    Make sure [Docker](https://docs.docker.com/get-docker/) is installed and running on your local machine.

    Download the latest `pinecone-local` Docker image:

    ```shell  theme={null}
    docker pull ghcr.io/pinecone-io/pinecone-local:latest
    ```

    Start Pinecone Local:

    ```shell  theme={null}
    docker run -d \
    --name pinecone-local \
    -e PORT=5080 \
    -e PINECONE_HOST=localhost \
    -p 5080-5090:5080-5090 \
    --platform linux/amd64 \
    ghcr.io/pinecone-io/pinecone-local:latest
    ```

    This command defines the host and port that Pinecone Local will run on, as well as the range of ports that will be available for indexes.
  </Tab>
</Tabs>


## 2. Develop your app

Running code against Pinecone Local is just like running code against your Pinecone account, with the following differences:

* Pinecone Local does not authenticate client requests. API keys are ignored.

* The latest version of Pinecone Local uses [Pinecone API version](/reference/api/versioning) `2025-01` and requires [Python SDK](/reference/python-sdk) `v6.x` or later, [Node.js SDK](/reference/node-sdk) `v5.x` or later, [Java SDK](/reference/java-sdk) `v4.x` or later, [Go SDK](/reference/go-sdk) `v3.x` or later, and [.NET SDK](/reference/dotnet-sdk) `v3.x` or later.

<Note>
  Be sure to review the [limitations](#limitations) of Pinecone Local before using it for development or testing.
</Note>

**Example**

The following example assumes that you have [started Pinecone Local without indexes](/guides/operations/local-development#database-emulator). It initializes a client, creates a [dense index](/guides/index-data/indexing-overview#dense-indexes) and a [sparse index](/guides/index-data/indexing-overview#sparse-indexes), upserts records into the indexes, checks their record counts, and queries the indexes.

<CodeGroup>
  ```python Python theme={null}
  from pinecone.grpc import PineconeGRPC, GRPCClientConfig
  from pinecone import ServerlessSpec

  # Initialize a client.
  # API key is required, but the value does not matter.
  # Host and port of the Pinecone Local instance
  # is required when starting without indexes. 
  pc = PineconeGRPC(
      api_key="pclocal", 
      host="http://localhost:5080" 
  )                                    

  # Create two indexes, one dense and one sparse
  dense_index_name = "dense-index"
  sparse_index_name = "sparse-index"

  if not pc.has_index(dense_index_name):  
      dense_index_model = pc.create_index(
          name=dense_index_name,
          vector_type="dense",
          dimension=2,
          metric="cosine",
          spec=ServerlessSpec(cloud="aws", region="us-east-1"),
          deletion_protection="disabled",
          tags={"environment": "development"}
      )

  print("Dense index model:\n", dense_index_model)

  if not pc.has_index(sparse_index_name):  
      sparse_index_model = pc.create_index(
          name=sparse_index_name,
          vector_type="sparse",
          metric="dotproduct",
          spec=ServerlessSpec(cloud="aws", region="us-east-1"),
          deletion_protection="disabled",
          tags={"environment": "development"}
      )

  print("\nSparse index model:\n", sparse_index_model)

  # Target each index, disabling tls
  dense_index_host = pc.describe_index(name=dense_index_name).host
  dense_index = pc.Index(host=dense_index_host, grpc_config=GRPCClientConfig(secure=False))
  sparse_index_host = pc.describe_index(name=sparse_index_name).host
  sparse_index = pc.Index(host=sparse_index_host, grpc_config=GRPCClientConfig(secure=False))

  # Upsert records into the dense index
  dense_index.upsert(
      vectors=[
          {
              "id": "vec1", 
              "values": [1.0, -2.5],
              "metadata": {"genre": "drama"}
          },
          {
              "id": "vec2", 
              "values": [3.0, -2.0],
              "metadata": {"genre": "documentary"}
          },
          {
              "id": "vec3", 
              "values": [0.5, -1.5],
              "metadata": {"genre": "documentary"}
          }
      ],
      namespace="example-namespace"
  )

  # Upsert records into the sparse index
  sparse_index.upsert(
      namespace="example-namespace",
      vectors=[
          {
              "id": "vec1",
              "sparse_values": {
                  "values": [1.7958984, 0.41577148, 2.828125, 2.8027344, 2.8691406, 1.6533203, 5.3671875, 1.3046875, 0.49780273, 0.5722656, 2.71875, 3.0820312, 2.5019531, 4.4414062, 3.3554688],
                  "indices": [822745112, 1009084850, 1221765879, 1408993854, 1504846510, 1596856843, 1640781426, 1656251611, 1807131503, 2543655733, 2902766088, 2909307736, 3246437992, 3517203014, 3590924191]
              },
              "metadata": {
                  "chunk_text": "AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones.",
                  "category": "technology",
                  "quarter": "Q3"
              }
          },
          {
              "id": "vec2",
              "sparse_values": {
                  "values": [0.4362793, 3.3457031, 2.7714844, 3.0273438, 3.3164062, 5.6015625, 2.4863281, 0.38134766, 1.25, 2.9609375, 0.34179688, 1.4306641, 0.34375, 3.3613281, 1.4404297, 2.2558594, 2.2597656, 4.8710938, 0.5605469],
                  "indices": [131900689, 592326839, 710158994, 838729363, 1304885087, 1640781426, 1690623792, 1807131503, 2066971792, 2428553208, 2548600401, 2577534050, 3162218338, 3319279674, 3343062801, 3476647774, 3485013322, 3517203014, 4283091697]
              },
              "metadata": {
                  "chunk_text": "Analysts suggest that AAPL'\''s upcoming Q4 product launch event might solidify its position in the premium smartphone market.",
                  "category": "technology",
                  "quarter": "Q4"
              }
          },
          {
              "id": "vec3",
              "sparse_values": {
                  "values": [2.6875, 4.2929688, 3.609375, 3.0722656, 2.1152344, 5.78125, 3.7460938, 3.7363281, 1.2695312, 3.4824219, 0.7207031, 0.0826416, 4.671875, 3.7011719, 2.796875, 0.61621094],
                  "indices": [8661920, 350356213, 391213188, 554637446, 1024951234, 1640781426, 1780689102, 1799010313, 2194093370, 2632344667, 2641553256, 2779594451, 3517203014, 3543799498, 3837503950, 4283091697]
              },
              "metadata": {
                  "chunk_text": "AAPL'\''s strategic Q3 partnerships with semiconductor suppliers could mitigate component risks and stabilize iPhone production",
                  "category": "technology",
                  "quarter": "Q3"
              }
          }
      ]
  )

  # Check the number of records in each index
  print("\nDense index stats:\n", dense_index.describe_index_stats())
  print("\nSparse index stats:\n", sparse_index.describe_index_stats())

  # Query the dense index with a metadata filter
  dense_response = dense_index.query(
      namespace="example-namespace",
      vector=[3.0, -2.0],
      filter={"genre": {"$eq": "documentary"}},
      top_k=1,
      include_values=False,
      include_metadata=True
  )

  print("\nDense query response:\n", dense_response)

  # Query the sparse index with a metadata filter
  sparse_response = sparse_index.query(
      namespace="example-namespace",
      sparse_vector={
        "values": [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
        "indices": [767227209, 1640781426, 1690623792, 2021799277, 2152645940, 2295025838, 2443437770, 2779594451, 2956155693, 3476647774, 3818127854, 4283091697]
      }, 
      filter={
          "quarter": {"$eq": "Q4"}
      },
      top_k=1,
      include_values=False,
      include_metadata=True
  )

  print("/nSparse query response:\n", sparse_response)

  # Delete the indexes
  pc.delete_index(name=dense_index_name)
  pc.delete_index(name=sparse_index_name)
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  // Initialize a client.
  // API key is required, but the value does not matter.
  // Host and port of the Pinecone Local instance
  // is required when starting without indexes.
  const pc = new Pinecone({ 
      apiKey: 'pclocal', 
      controllerHostUrl: 'http://localhost:5080' 
  });

  // Create two indexes, one dense and one sparse
  const denseIndexName = 'dense-index';
  const sparseIndexName = 'sparse-index';

  const denseIndexModel = await pc.createIndex({
    name: denseIndexName,
    vectorType: 'dense',
    dimension: 2,
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

  console.log('Dense index model:', denseIndexModel);

  const sparseIndexModel = await pc.createIndex({
      name: sparseIndexName,
      vectorType: 'sparse',
      metric: 'dotproduct',
      spec: {
        serverless: {
          cloud: 'aws',
          region: 'us-east-1'
        }
      },
      deletionProtection: 'disabled',
      tags: { environment: 'development' }, 
    });
    
  console.log('\nSparse index model:', sparseIndexModel);
    
  // Target each index
  const denseIndexHost = (await pc.describeIndex(denseIndexName)).host;
  const denseIndex = await pc.index(denseIndexName, 'http://' + denseIndexHost);
  const sparseIndexHost = (await pc.describeIndex(sparseIndexName)).host;
  const sparseIndex = await pc.index(sparseIndexName, 'http://' + sparseIndexHost);

  // Upsert records into the dense index
  await denseIndex.namespace('example-namespace').upsert([
      {
          id: 'vec1', 
          values: [1.0, -2.5],
          metadata: { genre: 'drama' },
      },
      {
          id: 'vec2', 
          values: [3.0, -2.0],
          metadata: { genre: 'documentary' },
      },
      {
          id: 'vec3', 
          values: [0.5, -1.5],
          metadata: { genre: 'documentary' },
      }
  ]);

  // Upsert records into the sparse index
  await sparseIndex.namespace('example-namespace').upsert([
      {
          id: 'vec1',
          sparseValues: {
              indices: [822745112, 1009084850, 1221765879, 1408993854, 1504846510, 1596856843, 1640781426, 1656251611, 1807131503, 2543655733, 2902766088, 2909307736, 3246437992, 3517203014, 3590924191],
              values: [1.7958984, 0.41577148, 2.828125, 2.8027344, 2.8691406, 1.6533203, 5.3671875, 1.3046875, 0.49780273, 0.5722656, 2.71875, 3.0820312, 2.5019531, 4.4414062, 3.3554688]
          },
          metadata: { 
              chunk_text: 'AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones.', 
              category: 'technology',
              quarter: 'Q3' 
          }
      },
      {
          id: 'vec2',
          sparseValues: {
              indices: [131900689, 592326839, 710158994, 838729363, 1304885087, 1640781426, 1690623792, 1807131503, 2066971792, 2428553208, 2548600401, 2577534050, 3162218338, 3319279674, 3343062801, 3476647774, 3485013322, 3517203014, 4283091697],
              values: [0.4362793, 3.3457031, 2.7714844, 3.0273438, 3.3164062, 5.6015625, 2.4863281, 0.38134766, 1.25, 2.9609375, 0.34179688, 1.4306641, 0.34375, 3.3613281, 1.4404297, 2.2558594, 2.2597656, 4.8710938, 0.5605469]
          },
          metadata: { 
              chunk_text: "Analysts suggest that AAPL's upcoming Q4 product launch event might solidify its position in the premium smartphone market.", 
              category: 'technology',
              quarter: 'Q4' 
          }
      },
      {
          id: 'vec3',
          sparseValues: {
              indices: [8661920, 350356213, 391213188, 554637446, 1024951234, 1640781426, 1780689102, 1799010313, 2194093370, 2632344667, 2641553256, 2779594451, 3517203014, 3543799498, 3837503950, 4283091697],
              values: [2.6875, 4.2929688, 3.609375, 3.0722656, 2.1152344, 5.78125, 3.7460938, 3.7363281, 1.2695312, 3.4824219, 0.7207031, 0.0826416, 4.671875, 3.7011719, 2.796875, 0.61621094]
          },
          metadata: { 
              chunk_text: "AAPL's strategic Q3 partnerships with semiconductor suppliers could mitigate component risks and stabilize iPhone production", 
              category: 'technology',
              quarter: 'Q3' 
          }
      }
  ]);
    
  // Check the number of records in each index
  console.log('\nDense index stats:', await denseIndex.describeIndexStats());
  console.log('\nSparse index stats:', await sparseIndex.describeIndexStats());

  // Query the dense index with a metadata filter
  const denseQueryResponse = await denseIndex.namespace('example-namespace').query({
      vector: [3.0, -2.0],
      filter: {
          'genre': {'$eq': 'documentary'}
      },
      topK: 1,
      includeValues: false,
      includeMetadata: true,
  });

  console.log('\nDense query response:', denseQueryResponse);

  const sparseQueryResponse = await sparseIndex.namespace('example-namespace').query({
      sparseVector: {
          indices: [767227209, 1640781426, 1690623792, 2021799277, 2152645940, 2295025838, 2443437770, 2779594451, 2956155693, 3476647774, 3818127854, 4283091697],
          values: [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
      },
      topK: 1,
      includeValues: false,
      includeMetadata: true
  });

  console.log('\nSparse query response:', sparseQueryResponse);

  // Delete the index
  await pc.deleteIndex(denseIndexName);
  await pc.deleteIndex(sparseIndexName);
  ```

  ```java Java theme={null}
  import com.google.protobuf.Struct;
  import com.google.protobuf.Value;
  import io.pinecone.clients.Index;
  import io.pinecone.clients.Pinecone;
  import io.pinecone.proto.DescribeIndexStatsResponse;
  import org.openapitools.db_control.client.model.DeletionProtection;
  import io.pinecone.unsigned_indices_model.QueryResponseWithUnsignedIndices;

  import java.util.*;

  public class PineconeLocalExample {
      public static void main(String[] args) {
          // Initialize a client.
          // API key is required, but the value does not matter.
          // When starting without indexes, disable TLS and
          // provide the host and port of the Pinecone Local instance.
          String host = "http://localhost:5080";
          Pinecone pc = new Pinecone.Builder("pclocal")
                  .withHost(host)
                  .withTlsEnabled(false)
                  .build();

          // Create two indexes, one dense and one sparse
          String denseIndexName = "dense-index";
          String sparseIndexName = "sparse-index";
          HashMap<String, String> tags = new HashMap<>();
          tags.put("environment", "development");
          pc.createServerlessIndex(
                  denseIndexName,
                  "cosine",
                  2,
                  "aws",
                  "us-east-1",
                  DeletionProtection.DISABLED,
                  tags
          );
          pc.createSparseServelessIndex(
                  sparseIndexName,
                  "aws",
                  "us-east-1",
                  DeletionProtection.DISABLED,
                  tags,
                  "sparse"
          );

          // Get index connection objects
          Index denseIndexConnection = pc.getIndexConnection(denseIndexName);
          Index sparseIndexConnection = pc.getIndexConnection(sparseIndexName);

          // Upsert records into the dense index
          Struct metaData1 = Struct.newBuilder()
                  .putFields("genre", Value.newBuilder().setStringValue("drama").build())
                  .build();
          Struct metaData2 = Struct.newBuilder()
                  .putFields("genre", Value.newBuilder().setStringValue("documentary").build())
                  .build();
          Struct metaData3 = Struct.newBuilder()
                  .putFields("genre", Value.newBuilder().setStringValue("documentary").build())
                  .build();

          denseIndexConnection.upsert("vec1", Arrays.asList(1.0f, -2.5f),  null, null, metaData1, "example-namespace");
          denseIndexConnection.upsert("vec2", Arrays.asList(3.0f, -2.0f),  null, null, metaData2, "example-namespace");
          denseIndexConnection.upsert("vec3", Arrays.asList(0.5f, -1.5f),  null, null, metaData3, "example-namespace");

          // Upsert records into the sparse index
          ArrayList<Long> indices1 = new ArrayList<>(Arrays.asList(
                  822745112L, 1009084850L, 1221765879L, 1408993854L, 1504846510L,
                  1596856843L, 1640781426L, 1656251611L, 1807131503L, 2543655733L,
                  2902766088L, 2909307736L, 3246437992L, 3517203014L, 3590924191L
          ));

          ArrayList<Float> values1 = new ArrayList<>(Arrays.asList(
                  1.7958984f, 0.41577148f, 2.828125f, 2.8027344f, 2.8691406f,
                  1.6533203f, 5.3671875f, 1.3046875f, 0.49780273f, 0.5722656f,
                  2.71875f, 3.0820312f, 2.5019531f, 4.4414062f, 3.3554688f
          ));

          Struct sparseMetaData1 = Struct.newBuilder()
                  .putFields("chunk_text", Value.newBuilder().setStringValue("AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones.").build())
                  .putFields("category", Value.newBuilder().setStringValue("technology").build())
                  .putFields("quarter", Value.newBuilder().setStringValue("Q3").build())
                  .build();

          ArrayList<Long> indices2 = new ArrayList<>(Arrays.asList(
                  131900689L, 592326839L, 710158994L, 838729363L, 1304885087L,
                  1640781426L, 1690623792L, 1807131503L, 2066971792L, 2428553208L,
                  2548600401L, 2577534050L, 3162218338L, 3319279674L, 3343062801L,
                  3476647774L, 3485013322L, 3517203014L, 4283091697L
          ));

          ArrayList<Float> values2 = new ArrayList<>(Arrays.asList(
                  0.4362793f, 3.3457031f, 2.7714844f, 3.0273438f, 3.3164062f,
                  5.6015625f, 2.4863281f, 0.38134766f, 1.25f, 2.9609375f,
                  0.34179688f, 1.4306641f, 0.34375f, 3.3613281f, 1.4404297f,
                  2.2558594f, 2.2597656f, 4.8710938f, 0.5605469f
          ));

          Struct sparseMetaData2 = Struct.newBuilder()
                  .putFields("chunk_text", Value.newBuilder().setStringValue("Analysts suggest that AAPL'\\''s upcoming Q4 product launch event might solidify its position in the premium smartphone market.").build())
                  .putFields("category", Value.newBuilder().setStringValue("technology").build())
                  .putFields("quarter", Value.newBuilder().setStringValue("Q4").build())
                  .build();

          ArrayList<Long> indices3 = new ArrayList<>(Arrays.asList(
                  8661920L, 350356213L, 391213188L, 554637446L, 1024951234L,
                  1640781426L, 1780689102L, 1799010313L, 2194093370L, 2632344667L,
                  2641553256L, 2779594451L, 3517203014L, 3543799498L,
                  3837503950L, 4283091697L
          ));

          ArrayList<Float> values3 = new ArrayList<>(Arrays.asList(
                  2.6875f, 4.2929688f, 3.609375f, 3.0722656f, 2.1152344f,
                  5.78125f, 3.7460938f, 3.7363281f, 1.2695312f, 3.4824219f,
                  0.7207031f, 0.0826416f, 4.671875f, 3.7011719f, 2.796875f,
                  0.61621094f
          ));

          Struct sparseMetaData3 = Struct.newBuilder()
                  .putFields("chunk_text", Value.newBuilder().setStringValue("AAPL'\\''s strategic Q3 partnerships with semiconductor suppliers could mitigate component risks and stabilize iPhone production").build())
                  .putFields("category", Value.newBuilder().setStringValue("technology").build())
                  .putFields("quarter", Value.newBuilder().setStringValue("Q3").build())
                  .build();

          sparseIndexConnection.upsert("vec1", Collections.emptyList(), indices1, values1, sparseMetaData1, "example-namespace");
          sparseIndexConnection.upsert("vec2", Collections.emptyList(), indices2, values2, sparseMetaData2, "example-namespace");
          sparseIndexConnection.upsert("vec3", Collections.emptyList(), indices3, values3, sparseMetaData3, "example-namespace");

          // Check the number of records each the index
          DescribeIndexStatsResponse denseIndexStatsResponse = denseIndexConnection.describeIndexStats(null);
          System.out.println("Dense index stats:");
          System.out.println(denseIndexStatsResponse);
          DescribeIndexStatsResponse sparseIndexStatsResponse = sparseIndexConnection.describeIndexStats(null);
          System.out.println("Sparse index stats:");
          System.out.println(sparseIndexStatsResponse);

          // Query the dense index with a metadata filter
          List<Float> queryVector = Arrays.asList(1.0f, 1.5f);
          QueryResponseWithUnsignedIndices denseQueryResponse = denseIndexConnection.query(1, queryVector, null, null, null, "example-namespace", null, false, true);
          System.out.println("Dense query response:");
          System.out.println(denseQueryResponse);

          // Query the sparse index with a metadata filter
          List<Long> sparseIndices = Arrays.asList(
                  767227209L, 1640781426L, 1690623792L, 2021799277L, 2152645940L,
                  2295025838L, 2443437770L, 2779594451L, 2956155693L, 3476647774L,
                  3818127854L, 428309169L);
          List<Float> sparseValues = Arrays.asList(
                  1.0f, 1.0f, 1.0f, 1.0f, 1.0f, 1.0f,
                  1.0f, 1.0f, 1.0f, 1.0f, 1.0f, 1.0f);

          QueryResponseWithUnsignedIndices sparseQueryResponse = sparseIndexConnection.query(1, null, sparseIndices, sparseValues, null, "example-namespace", null, false, true);
          System.out.println("Sparse query response:");
          System.out.println(sparseQueryResponse);

          // Delete the indexes
          pc.deleteIndex(denseIndexName);
          pc.deleteIndex(sparseIndexName);
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

  	// Initialize a client.
  	// No API key is required.
  	// Host and port of the Pinecone Local instance
  	// is required when starting without indexes.
  	pc, err := pinecone.NewClientBase(pinecone.NewClientBaseParams{
  		Host: "http://localhost:5080",
  	})
  	if err != nil {
  		log.Fatalf("Failed to create Client: %v", err)
  	}

  	// Create two indexes, one dense and one sparse
  	denseIndexName := "dense-index"
  	denseVectorType := "dense"
  	dimension := int32(2)
  	denseMetric := pinecone.Cosine
  	deletionProtection := pinecone.DeletionProtectionDisabled
  	denseIdx, err := pc.CreateServerlessIndex(ctx, &pinecone.CreateServerlessIndexRequest{
  		Name:               denseIndexName,
  		VectorType:         &denseVectorType,
  		Dimension:          &dimension,
  		Metric:             &denseMetric,
  		Cloud:              pinecone.Aws,
  		Region:             "us-east-1",
  		DeletionProtection: &deletionProtection,
  		Tags:               &pinecone.IndexTags{"environment": "development"},
  	})
  	if err != nil {
  		log.Fatalf("Failed to create serverless index: %v", denseIdx.Name)
  	} else {
  		fmt.Printf("Successfully created serverless index: %v\n", denseIdx.Name)
  	}

  	sparseIndexName := "sparse-index"
  	sparseVectorType := "sparse"
  	sparseMetric := pinecone.Dotproduct
  	sparseIdx, err := pc.CreateServerlessIndex(ctx, &pinecone.CreateServerlessIndexRequest{
  		Name:               sparseIndexName,
  		VectorType:         &sparseVectorType,
  		Metric:             &sparseMetric,
  		Cloud:              pinecone.Aws,
  		Region:             "us-east-1",
  		DeletionProtection: &deletionProtection,
  		Tags:               &pinecone.IndexTags{"environment": "development"},
  	})
  	if err != nil {
  		log.Fatalf("Failed to create serverless index: %v", sparseIdx.Name)
  	} else {
  		fmt.Printf("\nSuccessfully created serverless index: %v\n", sparseIdx.Name)
  	}

  	// Get the index hosts
  	denseIdxModel, err := pc.DescribeIndex(ctx, denseIndexName)
  	if err != nil {
  		log.Fatalf("Failed to describe index \"%v\": %v", denseIndexName, err)
  	}

  	sparseIdxModel, err := pc.DescribeIndex(ctx, sparseIndexName)
  	if err != nil {
  		log.Fatalf("Failed to describe index \"%v\": %v", sparseIndexName, err)
  	}

  	// Target the indexes.
  	// Make sure to prefix the hosts with http:// to let the SDK know to disable tls.
  	denseIdxConnection, err := pc.Index(pinecone.NewIndexConnParams{Host: "http://" + denseIdxModel.Host, Namespace: "example-namespace"})
  	if err != nil {
  		log.Fatalf("Failed to create IndexConnection for Host: %v", err)
  	}

  	sparseIdxConnection, err := pc.Index(pinecone.NewIndexConnParams{Host: "http://" + sparseIdxModel.Host, Namespace: "example-namespace"})
  	if err != nil {
  		log.Fatalf("Failed to create IndexConnection for Host: %v", err)
  	}

  	// Upsert records into the dense index
  	denseMetadataMap1 := map[string]interface{}{
  		"genre": "drama",
  	}

  	denseMetadata1, err := structpb.NewStruct(denseMetadataMap1)
  	if err != nil {
  		log.Fatalf("Failed to create metadata map: %v", err)
  	}

  	denseMetadataMap2 := map[string]interface{}{
  		"genre": "documentary",
  	}

  	denseMetadata2, err := structpb.NewStruct(denseMetadataMap2)
  	if err != nil {
  		log.Fatalf("Failed to create metadata map: %v", err)
  	}

  	denseMetadataMap3 := map[string]interface{}{
  		"genre": "documentary",
  	}

  	denseMetadata3, err := structpb.NewStruct(denseMetadataMap3)
  	if err != nil {
  		log.Fatalf("Failed to create metadata map: %v", err)
  	}

  	denseVectors := []*pinecone.Vector{
  		{
  			Id:       "vec1",
  			Values:   &[]float32{1.0, -2.5},
  			Metadata: denseMetadata1,
  		},
  		{
  			Id:       "vec2",
  			Values:   &[]float32{3.0, -2.0},
  			Metadata: denseMetadata2,
  		},
  		{
  			Id:       "vec3",
  			Values:   &[]float32{0.5, -1.5},
  			Metadata: denseMetadata3,
  		},
  	}

  	denseCount, err := denseIdxConnection.UpsertVectors(ctx, denseVectors)
  	if err != nil {
  		log.Fatalf("Failed to upsert vectors: %v", err)
  	} else {
  		fmt.Printf("\nSuccessfully upserted %d vector(s)!\n", denseCount)
  	}

  	// Upsert records into the sparse index
  	sparseValues1 := pinecone.SparseValues{
  		Indices: []uint32{822745112, 1009084850, 1221765879, 1408993854, 1504846510, 1596856843, 1640781426, 1656251611, 1807131503, 2543655733, 2902766088, 2909307736, 3246437992, 3517203014, 3590924191},
  		Values:  []float32{1.7958984, 0.41577148, 2.828125, 2.8027344, 2.8691406, 1.6533203, 5.3671875, 1.3046875, 0.49780273, 0.5722656, 2.71875, 3.0820312, 2.5019531, 4.4414062, 3.3554688},
  	}

  	sparseMetadataMap1 := map[string]interface{}{
  		"chunk_text": "AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones",
  		"category":   "technology",
  		"quarter":    "Q3",
  	}

  	sparseMetadata1, err := structpb.NewStruct(sparseMetadataMap1)
  	if err != nil {
  		log.Fatalf("Failed to create metadata map: %v", err)
  	}

  	sparseValues2 := pinecone.SparseValues{
  		Indices: []uint32{131900689, 592326839, 710158994, 838729363, 1304885087, 1640781426, 1690623792, 1807131503, 2066971792, 2428553208, 2548600401, 2577534050, 3162218338, 3319279674, 3343062801, 3476647774, 3485013322, 3517203014, 4283091697},
  		Values:  []float32{0.4362793, 3.3457031, 2.7714844, 3.0273438, 3.3164062, 5.6015625, 2.4863281, 0.38134766, 1.25, 2.9609375, 0.34179688, 1.4306641, 0.34375, 3.3613281, 1.4404297, 2.2558594, 2.2597656, 4.8710938, 0.560546},
  	}

  	sparseMetadataMap2 := map[string]interface{}{
  		"chunk_text": "Analysts suggest that AAPL's upcoming Q4 product launch event might solidify its position in the premium smartphone market.",
  		"category":   "technology",
  		"quarter":    "Q4",
  	}

  	sparseMetadata2, err := structpb.NewStruct(sparseMetadataMap2)
  	if err != nil {
  		log.Fatalf("Failed to create metadata map: %v", err)
  	}

  	sparseValues3 := pinecone.SparseValues{
  		Indices: []uint32{8661920, 350356213, 391213188, 554637446, 1024951234, 1640781426, 1780689102, 1799010313, 2194093370, 2632344667, 2641553256, 2779594451, 3517203014, 3543799498, 3837503950, 4283091697},
  		Values:  []float32{2.6875, 4.2929688, 3.609375, 3.0722656, 2.1152344, 5.78125, 3.7460938, 3.7363281, 1.2695312, 3.4824219, 0.7207031, 0.0826416, 4.671875, 3.7011719, 2.796875, 0.61621094},
  	}

  	sparseMetadataMap3 := map[string]interface{}{
  		"chunk_text": "AAPL's strategic Q3 partnerships with semiconductor suppliers could mitigate component risks and stabilize iPhone production",
  		"category":   "technology",
  		"quarter":    "Q3",
  	}

  	sparseMetadata3, err := structpb.NewStruct(sparseMetadataMap3)
  	if err != nil {
  		log.Fatalf("Failed to create metadata map: %v", err)
  	}

  	sparseVectors := []*pinecone.Vector{
  		{
  			Id:           "vec1",
  			SparseValues: &sparseValues1,
  			Metadata:     sparseMetadata1,
  		},
  		{
  			Id:           "vec2",
  			SparseValues: &sparseValues2,
  			Metadata:     sparseMetadata2,
  		},
  		{
  			Id:           "vec3",
  			SparseValues: &sparseValues3,
  			Metadata:     sparseMetadata3,
  		},
  	}

  	sparseCount, err := sparseIdxConnection.UpsertVectors(ctx, sparseVectors)
  	if err != nil {
  		log.Fatalf("Failed to upsert vectors: %v", err)
  	} else {
  		fmt.Printf("\nSuccessfully upserted %d vector(s)!\n", sparseCount)
  	}

  	// Check the number of records in each index
  	denseStats, err := denseIdxConnection.DescribeIndexStats(ctx)
  	if err != nil {
  		log.Fatalf("Failed to describe index: %v", err)
  	} else {
  		fmt.Printf("\nDense index stats: %+v\n", prettifyStruct(*denseStats))
  	}

  	sparseStats, err := sparseIdxConnection.DescribeIndexStats(ctx)
  	if err != nil {
  		log.Fatalf("Failed to describe index: %v", err)
  	} else {
  		fmt.Printf("\nSparse index stats: %+v\n", prettifyStruct(*sparseStats))
  	}

  	// Query the dense index with a metadata filter
  	queryVector := []float32{3.0, -2.0}

  	queryMetadataMap := map[string]interface{}{
  		"genre": map[string]interface{}{
  			"$eq": "documentary",
  		},
  	}

  	metadataFilter, err := structpb.NewStruct(queryMetadataMap)
  	if err != nil {
  		log.Fatalf("Failed to create metadata map: %v", err)
  	}

  	denseRes, err := denseIdxConnection.QueryByVectorValues(ctx, &pinecone.QueryByVectorValuesRequest{
  		Vector:          queryVector,
  		TopK:            1,
  		MetadataFilter:  metadataFilter,
  		IncludeValues:   false,
  		IncludeMetadata: true,
  	})
  	if err != nil {
  		log.Fatalf("Error encountered when querying by vector: %v", err)
  	} else {
  		fmt.Printf("\nDense query response: %v\n", prettifyStruct(denseRes))
  	}

  	// Query the sparse index with a metadata filter

  	sparseValues := pinecone.SparseValues{
  		Indices: []uint32{767227209, 1640781426, 1690623792, 2021799277, 2152645940, 2295025838, 2443437770, 2779594451, 2956155693, 3476647774, 3818127854, 4283091697},
  		Values:  []float32{1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0},
  	}

  	sparseRes, err := sparseIdxConnection.QueryByVectorValues(ctx, &pinecone.QueryByVectorValuesRequest{
  		SparseValues:    &sparseValues,
  		TopK:            1,
  		IncludeValues:   false,
  		IncludeMetadata: true,
  	})
  	if err != nil {
  		log.Fatalf("Error encountered when querying by vector: %v", err)
  	} else {
  		fmt.Printf("\nSparse query response: %v\n", prettifyStruct(sparseRes))
  	}
  	// Delete the indexes
  	err = pc.DeleteIndex(ctx, denseIndexName)
  	if err != nil {
  		log.Fatalf("Failed to delete index: %v", err)
  	} else {
  		fmt.Printf("\nIndex \"%v\" deleted successfully\n", denseIndexName)
  	}

  	err = pc.DeleteIndex(ctx, sparseIndexName)
  	if err != nil {
  		log.Fatalf("Failed to delete index: %v", err)
  	} else {
  		fmt.Printf("\nIndex \"%v\" deleted successfully\n", sparseIndexName)
  	}
  }
  ```

  ```csharp C# theme={null}
  using Pinecone;

  // Initialize a client.
  // API key is required, but the value does not matter.
  // When starting without indexes, disable TLS and
  // provide the host and port of the Pinecone Local instance.
  var pc = new PineconeClient("pclocal",
      new ClientOptions
      {
          BaseUrl = "http://localhost:5080",
          IsTlsEnabled = false
      }
  );

  // Create two indexes, one dense and one sparse
  var denseIndexName = "dense-index";
  var sparseIndexName = "sparse-index";

  var createDenseIndexRequest = await pc.CreateIndexAsync(new CreateIndexRequest
  {
      Name = denseIndexName,
      VectorType = VectorType.Dense,
      Dimension = 2,
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

  Console.WriteLine("Dense index model:" + createDenseIndexRequest);

  var createSparseIndexRequest = await pc.CreateIndexAsync(new CreateIndexRequest
  {
      Name = sparseIndexName,
      VectorType = VectorType.Sparse,
      Metric = MetricType.Dotproduct,
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

  Console.WriteLine("\nSparse index model:" + createSparseIndexRequest);

  // Target the indexes
  var denseIndex = pc.Index(denseIndexName);
  var sparseIndex = pc.Index(sparseIndexName);

  // Upsert records into the dense index
  var denseUpsertResponse = await denseIndex.UpsertAsync(new UpsertRequest()
  {
      Namespace = "example-namespace",
      Vectors = new List<Vector>
      {
          new Vector 
          { 
              Id = "vec1", 
              Values = new ReadOnlyMemory<float>([1.0f, -2.5f]),
              Metadata = new Metadata {
                  ["genre"] = new("drama"),
              },
          },
          new Vector 
          { 
              Id = "vec2", 
              Values = new ReadOnlyMemory<float>([3.0f, -2.0f]), 
              Metadata = new Metadata {
                  ["genre"] = new("documentary"),
              },
          },
          new Vector 
          { 
              Id = "vec3", 
              Values = new ReadOnlyMemory<float>([0.5f, -1.5f]),
              Metadata = new Metadata {
                  ["genre"] = new("documentary"),
              } 
          }
      }
  });
  Console.WriteLine($"\nUpserted {denseUpsertResponse.UpsertedCount} dense vectors");

  // Upsert records into the sparse index
  var sparseVector1 = new Vector
  {
      Id = "vec1",
      SparseValues = new SparseValues
      {
          Indices = new uint[] { 822745112, 1009084850, 1221765879, 1408993854, 1504846510, 1596856843, 1640781426, 1656251611, 1807131503, 2543655733, 2902766088, 2909307736, 3246437992, 3517203014, 3590924191 },
          Values = new ReadOnlyMemory<float>([1.7958984f, 0.41577148f, 2.828125f, 2.8027344f, 2.8691406f, 1.6533203f, 5.3671875f, 1.3046875f, 0.49780273f, 0.5722656f, 2.71875f, 3.0820312f, 2.5019531f, 4.4414062f, 3.3554688f])
      },
      Metadata = new Metadata {
          ["chunk_text"] = new("AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones."),
          ["category"] = new("technology"),
          ["quarter"] = new("Q3"),
      },
  };

  var sparseVector2 = new Vector
  {
      Id = "vec2",
      SparseValues = new SparseValues
      {
          Indices = new uint[] { 131900689, 592326839, 710158994, 838729363, 1304885087, 1640781426, 1690623792, 1807131503, 2066971792, 2428553208, 2548600401, 2577534050, 3162218338, 3319279674, 3343062801, 3476647774, 3485013322, 3517203014, 4283091697 },
          Values = new ReadOnlyMemory<float>([0.4362793f, 3.3457031f, 2.7714844f, 3.0273438f, 3.3164062f, 5.6015625f, 2.4863281f, 0.38134766f, 1.25f, 2.9609375f, 0.34179688f, 1.4306641f, 0.34375f, 3.3613281f, 1.4404297f, 2.2558594f, 2.2597656f, 4.8710938f, 0.5605469f])
      },
      Metadata = new Metadata {
          ["chunk_text"] = new("Analysts suggest that AAPL'\''s upcoming Q4 product launch event might solidify its position in the premium smartphone market."),
          ["category"] = new("technology"),
          ["quarter"] = new("Q4"),
      },
  };

  var sparseVector3 = new Vector
  {
      Id = "vec3",
      SparseValues = new SparseValues
      {
          Indices = new uint[] { 8661920, 350356213, 391213188, 554637446, 1024951234, 1640781426, 1780689102, 1799010313, 2194093370, 2632344667, 2641553256, 2779594451, 3517203014, 3543799498, 3837503950, 4283091697 },
          Values = new ReadOnlyMemory<float>([2.6875f, 4.2929688f, 3.609375f, 3.0722656f, 2.1152344f, 5.78125f, 3.7460938f, 3.7363281f, 1.2695312f, 3.4824219f, 0.7207031f, 0.0826416f, 4.671875f, 3.7011719f, 2.796875f, 0.61621094f])
      },
      Metadata = new Metadata {
          ["chunk_text"] = new("AAPL'\''s strategic Q3 partnerships with semiconductor suppliers could mitigate component risks and stabilize iPhone production"),
          ["category"] = new("technology"),
          ["quarter"] = new("Q3"),
      },    
  };

  var sparseUpsertResponse = await sparseIndex.UpsertAsync(new UpsertRequest
  {
      Vectors = new List<Vector> { sparseVector1, sparseVector2, sparseVector3 },
      Namespace = "example-namespace"
  });
  Console.WriteLine($"\nUpserted {sparseUpsertResponse.UpsertedCount} sparse vectors");

  // Check the number of records in each index
  var denseIndexStatsResponse = await denseIndex.DescribeIndexStatsAsync(new DescribeIndexStatsRequest());
  Console.WriteLine("\nDense index stats:" + denseIndexStatsResponse);
  var sparseIndexStatsResponse = await sparseIndex.DescribeIndexStatsAsync(new DescribeIndexStatsRequest());
  Console.WriteLine("\nSparse index stats:" + sparseIndexStatsResponse);

  // Query the dense index with a metadata filter
  var denseQueryResponse = await denseIndex.QueryAsync(new QueryRequest
  {
      Vector = new ReadOnlyMemory<float>([3.0f, -2.0f]),
      TopK = 1,
      Namespace = "example-namespace",
      Filter = new Metadata
      {
          ["genre"] = new Metadata
          {
              ["$eq"] = "documentary",
          }
      },
      IncludeValues = false,
      IncludeMetadata = true
  });
  Console.WriteLine("\nDense query response:" + denseQueryResponse);

  // Query the sparse index with a metadata filter
  var sparseQueryResponse = await sparseIndex.QueryAsync(new QueryRequest {
      Namespace = "example-namespace",
      TopK = 1,
      SparseVector = new SparseValues
      {
          Indices = [767227209, 1640781426, 1690623792, 2021799277, 2152645940, 2295025838, 2443437770, 2779594451, 2956155693, 3476647774, 3818127854, 4283091697],
          Values = new[] { 1.0f, 1.0f, 1.0f, 1.0f, 1.0f, 1.0f, 1.0f, 1.0f, 1.0f, 1.0f, 1.0f, 1.0f },
      },
      Filter = new Metadata
      {
          ["quarter"] = new Metadata
          {
              ["$eq"] = "Q4",
          }
      },
      IncludeValues = false,
      IncludeMetadata = true
  });
  Console.WriteLine("\nSparse query response:" + sparseQueryResponse);

  // Delete the indexes
  await pc.DeleteIndexAsync(denseIndexName);
  await pc.DeleteIndexAsync(sparseIndexName);
  ```

  ```shell curl theme={null}
  PINECONE_LOCAL_HOST="localhost:5080"
  DENSE_INDEX_HOST="localhost:5081"
  SPARSE_INDEX_HOST="localhost:5082"

  # Create two indexes, one dense and one sparse
  curl -X POST "http://$PINECONE_LOCAL_HOST/indexes" \
      -H "Accept: application/json" \
      -H "Content-Type: application/json" \
      -H "X-Pinecone-API-Version: 2025-01" \
      -d '{
              "name": "dense-index",
              "vector_type": "dense",
              "dimension": 2,
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

  curl -X POST "http://$PINECONE_LOCAL_HOST/indexes" \
      -H "Accept: application/json" \
      -H "Content-Type: application/json" \
      -H "X-Pinecone-API-Version: 2025-01" \
      -d '{
              "name": "sparse-index",
              "vector_type": "sparse",
              "metric": "dotproduct",
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

  # Upsert records into the dense index
  curl -X POST "http://$DENSE_INDEX_HOST/vectors/upsert" \
      -H "Content-Type: application/json" \
      -H "X-Pinecone-API-Version: 2025-01" \
      -d '{
              "namespace": "example-namespace",
              "vectors": [
                  {
                      "id": "vec1", 
                      "values": [1.0, -2.5],
                      "metadata": {"genre": "drama"}
                  },
                  {
                      "id": "vec2", 
                      "values": [3.0, -2.0],
                      "metadata": {"genre": "documentary"}
                  },
                  {
                      "id": "vec3", 
                      "values": [0.5, -1.5],
                      "metadata": {"genre": "documentary"}
                  }
              ]
          }'

  # Upsert records into the sparse index
  curl -X POST "http://$SPARSE_INDEX_HOST/vectors/upsert" \
      -H "Content-Type: application/json" \
      -H "X-Pinecone-API-Version: 2025-01" \
      -d '{
              "namespace": "example-namespace",
              "vectors": [
                  {
                      "id": "vec1",
                      "sparseValues": {
                          "values": [1.7958984, 0.41577148, 2.828125, 2.8027344, 2.8691406, 1.6533203, 5.3671875, 1.3046875, 0.49780273, 0.5722656, 2.71875, 3.0820312, 2.5019531, 4.4414062, 3.3554688],
                          "indices": [822745112, 1009084850, 1221765879, 1408993854, 1504846510, 1596856843, 1640781426, 1656251611, 1807131503, 2543655733, 2902766088, 2909307736, 3246437992, 3517203014, 3590924191]
                      },
                      "metadata": {
                          "chunk_text": "AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones.",
                          "category": "technology",
                          "quarter": "Q3"
                      }
                  },
                  {
                      "id": "vec2",
                      "sparseValues": {
                          "values": [0.4362793, 3.3457031, 2.7714844, 3.0273438, 3.3164062, 5.6015625, 2.4863281, 0.38134766, 1.25, 2.9609375, 0.34179688, 1.4306641, 0.34375, 3.3613281, 1.4404297, 2.2558594, 2.2597656, 4.8710938, 0.5605469],
                          "indices": [131900689, 592326839, 710158994, 838729363, 1304885087, 1640781426, 1690623792, 1807131503, 2066971792, 2428553208, 2548600401, 2577534050, 3162218338, 3319279674, 3343062801, 3476647774, 3485013322, 3517203014, 4283091697]
                      },
                      "metadata": {
                          "chunk_text": "Analysts suggest that AAPL'\''s upcoming Q4 product launch event might solidify its position in the premium smartphone market.",
                          "category": "technology",
                          "quarter": "Q4"
                      }
                  },
                  {
                      "id": "vec3",
                      "sparseValues": {
                          "values": [2.6875, 4.2929688, 3.609375, 3.0722656, 2.1152344, 5.78125, 3.7460938, 3.7363281, 1.2695312, 3.4824219, 0.7207031, 0.0826416, 4.671875, 3.7011719, 2.796875, 0.61621094],
                          "indices": [8661920, 350356213, 391213188, 554637446, 1024951234, 1640781426, 1780689102, 1799010313, 2194093370, 2632344667, 2641553256, 2779594451, 3517203014, 3543799498, 3837503950, 4283091697]
                      },
                      "metadata": {
                          "chunk_text": "AAPL'\''s strategic Q3 partnerships with semiconductor suppliers could mitigate component risks and stabilize iPhone production",
                          "category": "technology",
                          "quarter": "Q3"
                      }
                  }
              ]
          }'

  # Check the number of records in each index
  curl -X POST "http://$DENSE_INDEX_HOST/describe_index_stats" \
      -H "Content-Type: application/json" \
      -H "X-Pinecone-API-Version: 2025-01" \
      -d '{}'

  curl -X POST "http://$SPARSE_INDEX_HOST/describe_index_stats" \
      -H "Content-Type: application/json" \
      -H "X-Pinecone-API-Version: 2025-01" \
      -d '{}'

  # Query the dense index with a metadata filter
  curl "http://$DENSE_INDEX_HOST/query" \
      -H "Content-Type: application/json" \
      -H "X-Pinecone-API-Version: 2025-01" \
      -d '{
              "vector": [3.0, -2.0],
              "filter": {"genre": {"$eq": "documentary"}},
              "topK": 1,
              "includeMetadata": true,
              "includeValues": false,
              "namespace": "example-namespace"
          }'

  # Query the sparse index with a metadata filter
  curl "http://$SPARSE_INDEX_HOST/query" \
      -H "Content-Type: application/json" \
      -H "X-Pinecone-API-Version: 2025-01" \
      -d '{
              "sparseVector": {
                  "values": [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
                  "indices": [767227209, 1640781426, 1690623792, 2021799277, 2152645940, 2295025838, 2443437770, 2779594451, 2956155693, 3476647774, 3818127854, 4283091697]
              },
              "filter": {"quarter": {"$eq": "Q4"}},
              "namespace": "example-namespace",
              "topK": 1,
              "includeMetadata": true,
              "includeValues": false
          }'

  # Delete the index
  curl -X DELETE "http://$PINECONE_LOCAL_HOST/indexes/dense-index" \
      -H "X-Pinecone-API-Version: 2025-01"

  curl -X DELETE "http://$PINECONE_LOCAL_HOST/indexes/sparse-index" \
      -H "X-Pinecone-API-Version: 2025-01"
  ```
</CodeGroup>


## 3. Stop Pinecone Local

<Warning>
  Pinecone Local is an in-memory emulator. Records loaded into Pinecone Local do not persist after Pinecone Local is stopped.
</Warning>

To stop and remove the resources for Pinecone Local, run the following command:

<CodeGroup>
  ```shell Docker Compose theme={null}
  docker compose down
  ```

  ```shell Docker CLI theme={null}
  # If you started Pinecone Local with indexes:
  docker stop dense-index sparse-index
  docker rm dense-index sparse-index

  # If you started Pinecone Local without indexes:
  docker stop pinecone-local
  docker rm pinecone-local
  ```
</CodeGroup>


## Moving from Pinecone Local to your Pinecone account

When you're ready to run your application against your Pinecone account, be sure to do the following:

* Update your application to [use your Pinecone API key](/reference/api/authentication).
* Update your application to [target your Pinecone indexes](/guides/manage-data/target-an-index).
* [Use Pinecone's import feature](/guides/index-data/import-data) to efficiently load large amounts of data into your indexes and then [use batch upserts](/guides/index-data/upsert-data#upsert-in-batches) for ongoing writes.
* Follow Pinecone's [production best practices](/guides/production/production-checklist).



---
**Navigation:** [← Previous](./08-manage-serverless-indexes.md) | [Index](./index.md) | [Next →](./10-use-the-pinecone-mcp-server.md)
