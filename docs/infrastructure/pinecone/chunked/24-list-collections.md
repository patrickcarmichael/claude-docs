**Navigation:** [← Previous](./23-load-the-documents-and-queries-of-legalbench-consu.md) | [Index](./index.md) | [Next →](./25-list-available-models.md)

# List collections
Source: https://docs.pinecone.io/reference/api/2025-04/control-plane/list_collections

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-04/db_control_2025-04.oas.yaml get /collections
List all collections in a project.
Serverless indexes do not support collections.


<RequestExample>
  ```python Python theme={null}
  from pinecone.grpc import PineconeGRPC as Pinecone

  pc = Pinecone(api_key='YOUR_API_KEY')

  active_collections = pc.list_collections()
  ```

  ```javascript JavaScript theme={null}
  // npm install @pinecone-database/pinecone
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
          System.out.println(collectionList);
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

  curl -X GET "https://api.pinecone.io/collections" \
       -H "Api-Key: $PINECONE_API_KEY" \
       -H "X-Pinecone-API-Version: 2025-04"
  ```
</RequestExample>

<ResponseExample>
  ```json  theme={null}
  {
      "collections": [
          {
              "name": "example-collection1",
              "status": "Ready",
              "environment": "us-east-1-aws",
              "size": 3081918,
              "vector_count": 99,
              "dimension": 3
          },
          {
              "name": "example-collection1",
              "status": "Ready",
              "environment": "us-east-1-aws",
              "size": 160087040000000,
              "vector_count": 10000000,
              "dimension": 1536
          }
      ]
  }
  ```
</ResponseExample>



# List backups for an index
Source: https://docs.pinecone.io/reference/api/2025-04/control-plane/list_index_backups

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-04/db_control_2025-04.oas.yaml get /indexes/{index_name}/backups
List all backups for an index.

<RequestExample>
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
</RequestExample>

<ResponseExample>
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
        createdAt: '2025-05-15T00:52:10.809305882Z'
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
</ResponseExample>



# List backups for all indexes in a project
Source: https://docs.pinecone.io/reference/api/2025-04/control-plane/list_project_backups

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-04/db_control_2025-04.oas.yaml get /backups
List all backups for a project.

<RequestExample>
  ```python Python theme={null}
  from pinecone import Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  project_backups = pc.list_backups()

  print(project_backups)
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' })

  const projectBackups = await pc.listBackups();

  console.log(projectBackups);
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Pinecone;
  import org.openapitools.db_control.client.ApiException;
  import org.openapitools.db_control.client.model.*;

  public class CreateBackup {
      public static void main(String[] args) throws ApiException {
          Pinecone pc = new Pinecone.Builder("YOUR_API_KEY").build();

          String indexName = "docs-example";
          BackupList projectBackupList = pc.listProjectBackups();

          System.out.println(projectBackupList);
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

  	limit := 3
  	backups, err := pc.ListBackups(ctx, &pinecone.ListBackupsParams{
  		Limit:     &limit,
  	})
  	if err != nil {
  		log.Fatalf("Failed to list backups: %v", err)
  	}
  	fmt.Printf(prettifyStruct(backups))
  }
  ```

  ```csharp C# theme={null}
  using Pinecone;

  var pinecone = new PineconeClient("PINECONE_API_KEY");

  var backups = await pinecone.Backups.ListAsync();

  Console.WriteLine(backups);
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl -X GET "https://api.pinecone.io/backups" \
       -H "Api-Key: $PINECONE_API_KEY" \
       -H "X-Pinecone-API-Version: 2025-04" \
       -H "accept: application/json"
  ```
</RequestExample>

<ResponseExample>
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
      "created_at": "2025-05-15T20:26:21.248515Z"
  }, {
      "backup_id": "95707edb-e482-49cf-b5a5-312219a51a97",
      "source_index_name": "docs-example2",
      "source_index_id": "b49f27d1-1bf3-49c6-82b5-4ae46f00f0e6",
      "status": "Ready",
      "cloud": "aws",
      "region": "us-east-1",
      "tags": {},
      "name": "example-backup2",
      "description": "Monthly backup of production index",
      "dimension": 1024,
      "record_count": 97,
      "namespace_count": 2,
      "size_bytes": 1069169,
      "created_at": "2025-05-15T00:52:10.809354Z"
  }, {
      "backup_id": "8c85e612-ed1c-4f97-9f8c-8194e07bcf71",
      "source_index_name": "docs-example3",
      "source_index_id": "f73b36c9-faf5-4a2c-b1d6-4013d8b1cc74",
      "status": "Ready",
      "cloud": "aws",
      "region": "us-east-1",
      "tags": {},
      "name": "example-backup3",
      "description": "Monthly backup of production index",
      "dimension": 1024,
      "record_count": 98,
      "namespace_count": 3,
      "size_bytes": 1069169,
      "created_at": "2025-05-14T16:37:25.625540Z"
  }]
  ```

  ```javascript JavaScript theme={null}
  {
    data: [
      {
        backupId: 'e12269b0-a29b-4af0-9729-c7771dec03e3',
        sourceIndexName: 'docs-example',
        sourceIndexId: 'bcb5b3c9-903e-4cb6-8b37-a6072aeb874f',
        name: 'example-backup',
        description: undefined,
        status: 'Ready',
        cloud: 'aws',
        region: 'us-east-1',
        dimension: 0,
        metric: undefined,
        recordCount: 96,
        namespaceCount: 1,
        sizeBytes: 86393,
        tags: undefined,
        createdAt: '2025-05-14T17:00:45.803146Z'
      },
      {
        backupId: 'd686451d-1ede-4004-9f72-7d22cc799b6e',
        sourceIndexName: 'docs-example2',
        sourceIndexId: 'b49f27d1-1bf3-49c6-82b5-4ae46f00f0e6',
        name: 'example-backup2',
        description: undefined,
        status: 'Ready',
        cloud: 'aws',
        region: 'us-east-1',
        dimension: 1024,
        metric: undefined,
        recordCount: 50,
        namespaceCount: 1,
        sizeBytes: 545171,
        tags: undefined,
        createdAt: '2025-05-14T17:00:34.814371Z'
      },
      {
        backupId: '8c85e612-ed1c-4f97-9f8c-8194e07bcf71',
        sourceIndexName: 'docs-example3',
        sourceIndexId: 'f73b36c9-faf5-4a2c-b1d6-4013d8b1cc74',
        name: 'example-backup3',
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
          backupId: 13761d20-7a0b-4778-ac27-36dd91c4be43
          sourceIndexName: example-dense-index
          sourceIndexId: f73b36c9-faf5-4a2c-b1d6-4013d8b1cc74
          name: example-backup-java2
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
      }, class BackupModel {
          backupId: 0d75b99f-be61-4a93-905e-77201286c02e
          sourceIndexName: example-dense-index
          sourceIndexId: f73b36c9-faf5-4a2c-b1d6-4013d8b1cc74
          name: example-backup-java
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
          createdAt: 2025-05-16T19:42:23.804820Z
          additionalProperties: null
      }, class BackupModel {
          backupId: bf2cda5d-b233-4a0a-aae9-b592780ad3ff
          sourceIndexName: example-sparse-index
          sourceIndexId: bcb5b3c9-903e-4cb6-8b37-a6072aeb874f
          name: example-sparse-python
          description: Monthly backup of production index
          status: Ready
          cloud: aws
          region: us-east-1
          dimension: 0
          metric: null
          recordCount: 96
          namespaceCount: 1
          sizeBytes: 86393
          tags: {}
          createdAt: 2025-05-16T18:01:51.531129Z
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
        "backup_id": "8c85e612-ed1c-4f97-9f8c-8194e07bcf71",
        "cloud": "aws",
        "created_at": "2025-05-15T00:52:10.809305882Z",
        "description": "Monthly backup of production index",
        "dimension": 1024,
        "name": "example-backup",
        "namespace_count": 3,
        "record_count": 98,
        "region": "us-east-1",
        "size_bytes": 1069169,
        "source_index_id": "f73b36c9-faf5-4a2c-b1d6-4013d8b1cc74",
        "source_index_name": "docs-example",
        "status": "Ready",
        "tags": {}
      },
      {
        "backup_id": "bf2cda5d-b233-4a0a-aae9-b592780ad3ff",
        "cloud": "aws",
        "created_at": "2025-05-15T00:52:10.809305882Z",
        "description": "Monthly backup of production index",
        "dimension": 0,
        "name": "example-backup2",
        "namespace_count": 1,
        "record_count": 96,
        "region": "us-east-1",
        "size_bytes": 86393,
        "source_index_id": "bcb5b3c9-903e-4cb6-8b37-a6072aeb874f",
        "source_index_name": "example-sparse-index",
        "status": "Ready",
        "tags": {}
      },
      {
        "backup_id": "f73028f6-1746-410e-ab6d-9dd2519df4de",
        "cloud": "aws",
        "created_at": "2025-05-15T20:26:21.248515Z",
        "description": "Monthly backup of production index",
        "dimension": 1024,
        "name": "example-backup3",
        "namespace_count": 2,
        "record_count": 97,
        "region": "us-east-1",
        "size_bytes": 1069169,
        "source_index_id": "f73b36c9-faf5-4a2c-b1d6-4013d8b1cc74",
        "source_index_name": "example-dense-index",
        "status": "Ready",
        "tags": {}
      }
    ],
    "pagination": {
      "next": "eyJsaW1pdCI6Miwib2Zmc2V0IjoyfQ=="
    }  
  }
  ```

  ```csharp C# theme={null}
  {
    "data": [
      {
        "backup_id": "95707edb-e482-49cf-b5a5-312219a51a97",
        "source_index_name": "docs-example",
        "source_index_id": "f73b36c9-faf5-4a2c-b1d6-4013d8b1cc74",
        "name": "example-backup",
        "description": "Monthly backup of production index",
        "status": "Ready",
        "cloud": "aws",
        "region": "us-east-1",
        "dimension": 1024,
        "record_count": 97,
        "namespace_count": 2,
        "size_bytes": 1069169,
        "tags": {},
        "created_at": "2025-05-15T00:52:10.809354Z"
      },
      {
        "backup_id": "e12269b0-a29b-4af0-9729-c7771dec03e3",
        "source_index_name": "docs-example2",
        "source_index_id": "bcb5b3c9-903e-4cb6-8b37-a6072aeb874f",
        "name": "example-backup2",
        "status": "Ready",
        "cloud": "aws",
        "region": "us-east-1",
        "dimension": 0,
        "record_count": 96,
        "namespace_count": 1,
        "size_bytes": 86393,
        "created_at": "2025-05-14T17:00:45.803146Z"
      },
      {
        "backup_id": "d686451d-1ede-4004-9f72-7d22cc799b6e",
        "source_index_name": "docs-example3",
        "source_index_id": "b49f27d1-1bf3-49c6-82b5-4ae46f00f0e6",
        "name": "example-backup3",
        "status": "Ready",
        "cloud": "aws",
        "region": "us-east-1",
        "dimension": 1024,
        "record_count": 50,
        "namespace_count": 1,
        "size_bytes": 545171,
        "created_at": "2025-05-14T17:00:34.814371Z"
      }
    ]
  }
  ```

  ```json curl  theme={null}
  {
    "data": [
      {
        "backup_id": "e12269b0-a29b-4af0-9729-c7771dec03e3",
        "source_index_id": "bcb5b3c9-903e-4cb6-8b37-a6072aeb874f",
        "source_index_name": "docs-example",
        "tags": null,
        "name": "example-backup",
        "description": null,
        "status": "Ready",
        "cloud": "aws",
        "region": "us-east-1",
        "dimension": 0,
        "record_count": 96,
        "namespace_count": 1,
        "size_bytes": 86393,
        "created_at": "2025-05-14T17:00:45.803146Z"
      },
      {
        "backup_id": "d686451d-1ede-4004-9f72-7d22cc799b6e",
        "source_index_id": "b49f27d1-1bf3-49c6-82b5-4ae46f00f0e6",
        "source_index_name": "docs-example2",
        "tags": null,
        "name": "example-backup2",
        "description": null,
        "status": "Ready",
        "cloud": "aws",
        "region": "us-east-1",
        "dimension": 1024,
        "record_count": 50,
        "namespace_count": 1,
        "size_bytes": 545171,
        "created_at": "2025-05-14T17:00:34.814371Z"
      },
      {
        "backup_id": "8c85e612-ed1c-4f97-9f8c-8194e07bcf71",
        "source_index_id": "f73b36c9-faf5-4a2c-b1d6-4013d8b1cc74",
        "source_index_name": "docs-example3",
        "tags": {},
        "name": "example-backup3",
        "description": "Monthly backup of production index",
        "status": "Ready",
        "cloud": "aws",
        "region": "us-east-1",
        "dimension": 1024,
        "record_count": 98,
        "namespace_count": 3,
        "size_bytes": 1069169,
        "created_at": "2025-05-14T16:37:25.625540Z"
      }
    ],
    "pagination": null
  }
  ```
</ResponseExample>



# List restore jobs
Source: https://docs.pinecone.io/reference/api/2025-04/control-plane/list_restore_jobs

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-04/db_control_2025-04.oas.yaml get /restore-jobs
List all restore jobs for a project.

<RequestExample>
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

          // List all restore jobs with default pagination limit (100)
          RestoreJobList restoreJobList = pc.listRestoreJobs(null, null);

          // List all restore jobs with pagination limit of 2
          RestoreJobList restoreJobListWithLimit = pc.listRestoreJobs(null, 2);

          // List all restore jobs with pagination limit and token
          RestoreJobList restoreJobListPaginated = pc.listRestoreJobs("eyJza2lwX3Bhc3QiOiIxMDEwMy0=", 2);

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

  curl -X GET "https://api.pinecone.io/restore-jobs" \
       -H "X-Pinecone-Api-Version: 2025-04" \
       -H "Api-Key: $PINECONE_API_KEY"
  ```
</RequestExample>

<ResponseExample>
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
</ResponseExample>



# Cancel an import
Source: https://docs.pinecone.io/reference/api/2025-04/data-plane/cancel_import

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-04/db_data_2025-04.oas.yaml delete /bulk/imports/{id}
Cancel an import operation if it is not yet finished. It has no effect if the operation is already finished.

For guidance and examples, see [Import data](https://docs.pinecone.io/guides/index-data/import-data).

<Note>
  This feature is in [public preview](/release-notes/feature-availability) and available only on [Standard and Enterprise plans](https://www.pinecone.io/pricing/).
</Note>

<RequestExample>
  ```python Python theme={null}
  from pinecone import Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  # To get the unique host for an index, 
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  index = pc.Index(host="INDEX_HOST")

  index.cancel_import(id="101")
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  // To get the unique host for an index, 
  // see https://docs.pinecone.io/guides/manage-data/target-an-index
  const index = pc.index("INDEX_NAME", "INDEX_HOST")

  await index.cancelImport(id='101');
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Pinecone;
  import io.pinecone.clients.AsyncIndex;
  import org.openapitools.db_data.client.ApiException;

  public class CancelImport {
      public static void main(String[] args) throws ApiException {
          // Initialize a Pinecone client with your API key
          Pinecone pinecone = new Pinecone.Builder("YOUR_API_KEY").build();

          // Get async imports connection object
          AsyncIndex asyncIndex = pinecone.getAsyncIndexConnection("docs-example");

          // Cancel import
          asyncIndex.cancelImport("2");
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
      idxConnection, err := pc.Index(pinecone.NewIndexConnParams{Host: "INDEX_HOST"})
      if err != nil {
          log.Fatalf("Failed to create IndexConnection for Host: %v", err)
    	}

      importID := "101"

      err = idxConnection.CancelImport(ctx, importID)
      if err != nil {
          log.Fatalf("Failed to cancel import: %s", importID)
      }

      importDesc, err := idxConnection.DescribeImport(ctx, importID)
      if err != nil {
          log.Fatalf("Failed to describe import: %s - %v", importID, err)
      }
  }
  ```

  ```csharp C# theme={null}
  using Pinecone;

  var pinecone = new PineconeClient("YOUR_API_KEY");

  // To get the unique host for an index, 
  // see https://docs.pinecone.io/guides/manage-data/target-an-index
  var index = pinecone.Index(host: "INDEX_HOST");

  var cancelResponse = await index.CancelBulkImportAsync("101");
  ```

  ```bash curl theme={null}
  # To get the unique host for an index,
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="INDEX_HOST"

  curl -X DELETE "https://$INDEX_HOST/bulk/imports/101" \
    -H 'Api-Key: $PINECONE_API_KEY' \
    -H "X-Pinecone-API-Version: 2025-04"
  ```
</RequestExample>

<ResponseExample>
  ```json  theme={null}
  {}
  ```
</ResponseExample>



# Describe an import
Source: https://docs.pinecone.io/reference/api/2025-04/data-plane/describe_import

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-04/db_data_2025-04.oas.yaml get /bulk/imports/{id}
Return details of a specific import operation.

For guidance and examples, see [Import data](https://docs.pinecone.io/guides/index-data/import-data).

<Note>
  This feature is in [public preview](/release-notes/feature-availability) and available only on [Standard and Enterprise plans](https://www.pinecone.io/pricing/).
</Note>

<RequestExample>
  ```python Python theme={null}
  from pinecone import Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  # To get the unique host for an index, 
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  index = pc.Index(host="INDEX_HOST")

  index.describe_import(id="101")
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });


  // To get the unique host for an index, 
  // see https://docs.pinecone.io/guides/manage-data/target-an-index
  const index = pc.index("INDEX_NAME", "INDEX_HOST")

  const results = await index.describeImport(id='101');
  console.log(results);
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Pinecone;
  import io.pinecone.clients.AsyncIndex;
  import org.openapitools.db_data.client.ApiException;
  import org.openapitools.db_data.client.model.ImportModel;

  public class DescribeImport {
      public static void main(String[] args) throws ApiException {
          // Initialize a Pinecone client with your API key
          Pinecone pinecone = new Pinecone.Builder("YOUR_API_KEY").build();

          // Get async imports connection object
          AsyncIndex asyncIndex = pinecone.getAsyncIndexConnection("docs-example");

          // Describe import
          ImportModel importDetails = asyncIndex.describeImport("101");

          System.out.println(importDetails);
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
      idxConnection, err := pc.Index(pinecone.NewIndexConnParams{Host: "INDEX_HOST"})
      if err != nil {
          log.Fatalf("Failed to create IndexConnection for Host: %v", err)
    	}

      importID := "101"

      importDesc, err := idxConnection.DescribeImport(ctx, importID)
      if err != nil {
          log.Fatalf("Failed to describe import: %s - %v", importID, err)
      }
      fmt.Printf("Import ID: %s, Status: %s", importDesc.Id, importDesc.Status)
  }
  ```

  ```csharp C# theme={null}
  using Pinecone;

  var pinecone = new PineconeClient("YOUR_API_KEY");

  // To get the unique host for an index, 
  // see https://docs.pinecone.io/guides/manage-data/target-an-index
  var index = pinecone.Index(host: "INDEX_HOST");

  var importDetails = await index.DescribeBulkImportAsync("101");
  ```

  ```bash curl theme={null}
  # To get the unique host for an index, 
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="INDEX_HOST"

  curl -X GET "https://$INDEX_HOST/bulk/imports/101" \
    -H 'Api-Key: $PINECONE_API_KEY' \
    -H 'X-Pinecone-API-Version: 2025-04'
  ```
</RequestExample>

<ResponseExample>
  ```json  theme={null}
  {
    "id": "101",
    "uri": "s3://BUCKET_NAME/PATH/TO/DIR",
    "status": "Pending",
    "created_at": "2024-08-19T20:49:00.754Z",
    "finished_at": "2024-08-19T20:49:00.754Z",
    "percent_complete": 42.2,
    "records_imported": 1000000
  }
  ```
</ResponseExample>



# List imports
Source: https://docs.pinecone.io/reference/api/2025-04/data-plane/list_imports

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-04/db_data_2025-04.oas.yaml get /bulk/imports
List all recent and ongoing import operations.

By default, `list_imports` returns up to 100 imports per page. If the `limit` parameter is set, `list` returns up to that number of imports instead. Whenever there are additional IDs to return, the response also includes a `pagination_token` that you can use to get the next batch of imports. When the response does not include a `pagination_token`, there are no more imports to return.

For guidance and examples, see [Import data](https://docs.pinecone.io/guides/index-data/import-data).

<Note>
  This feature is in [public preview](/release-notes/feature-availability) and available only on [Standard and Enterprise plans](https://www.pinecone.io/pricing/).
</Note>

<RequestExample>
  ```python Python theme={null}
  from pinecone import Pinecone, ImportErrorMode

  pc = Pinecone(api_key="YOUR_API_KEY")

  # To get the unique host for an index, 
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  index = pc.Index(host="INDEX_HOST")

  # List using a generator that handles pagination
  for i in index.list_imports():
      print(f"id: {i.id} status: {i.status}")

  # List using a generator that fetches all results at once
  operations = list(index.list_imports())
  print(operations)
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  // To get the unique host for an index, 
  // see https://docs.pinecone.io/guides/manage-data/target-an-index
  const index = pc.index("INDEX_NAME", "INDEX_HOST")

  const results = await index.listImports({ limit: 10, paginationToken: 'Tm90aGluZyB0byBzZWUgaGVyZQo' });
  console.log(results);
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Pinecone;
  import io.pinecone.clients.AsyncIndex;
  import org.openapitools.db_data.client.ApiException;
  import org.openapitools.db_data.client.model.ListImportsResponse;

  public class ListImports {
      public static void main(String[] args) throws ApiException {
          // Initialize a Pinecone client with your API key
          Pinecone pinecone = new Pinecone.Builder("YOUR_API_KEY").build();

          // Get async imports connection object
          AsyncIndex asyncIndex = pinecone.getAsyncIndexConnection("docs-example");

          // List imports
          ListImportsResponse response = asyncIndex.listImports(10, "Tm90aGluZyB0byBzZWUgaGVyZQo");

          System.out.println(response);
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
      idxConnection, err := pc.Index(pinecone.NewIndexConnParams{Host: "INDEX_HOST"})
      if err != nil {
          log.Fatalf("Failed to create IndexConnection for Host: %v", err)
    	}

      limit := int32(10)
      firstImportPage, err := idxConnection.ListImports(ctx, &limit, nil)
      if err != nil {
          log.Fatalf("Failed to list imports: %v", err)
      }
      fmt.Printf("First page of imports: %+v", firstImportPage.Imports)

      paginationToken := firstImportPage.NextPaginationToken
      nextImportPage, err := idxConnection.ListImports(ctx, &limit, paginationToken)
      if err != nil {
          log.Fatalf("Failed to list imports: %v", err)
      }
      fmt.Printf("Second page of imports: %+v", nextImportPage.Imports)
  }
  ```

  ```csharp C# theme={null}
  using Pinecone;

  var pinecone = new PineconeClient("YOUR_API_KEY");

  // To get the unique host for an index, 
  // see https://docs.pinecone.io/guides/manage-data/target-an-index
  var index = pinecone.Index(host: "INDEX_HOST");

  var imports = await index.ListBulkImportsAsync(new ListBulkImportsRequest
  {
      Limit = 10,
      PaginationToken = "Tm90aGluZyB0byBzZWUgaGVyZQo"
  });
  ```

  ```bash curl theme={null}
  # To get the unique host for an index,
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="INDEX_HOST"

  curl -X GET "https://$INDEX_HOST/bulk/imports?paginationToken==Tm90aGluZyB0byBzZWUgaGVyZQo" \
    -H 'Api-Key: $PINECONE_API_KEY' \
    -H 'X-Pinecone-API-Version: 2025-04'
  ```
</RequestExample>

<ResponseExample>
  ```json  theme={null}
  {
    "data": [
      {
        "id": "1",
        "uri": "s3://BUCKET_NAME/PATH/TO/DIR",
        "status": "Pending",
        "started_at": "2024-08-19T20:49:00.754Z",
        "finished_at": "2024-08-19T20:49:00.754Z",
        "percent_complete": 42.2,
        "records_imported": 1000000
      }
    ],
    "pagination": {
      "next": "Tm90aGluZyB0byBzZWUgaGVyZQo="
    }
  }
  ```
</ResponseExample>



# Start import
Source: https://docs.pinecone.io/reference/api/2025-04/data-plane/start_import

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-04/db_data_2025-04.oas.yaml post /bulk/imports
Start an asynchronous import of vectors from object storage into an index.

For guidance and examples, see [Import data](https://docs.pinecone.io/guides/index-data/import-data).

<Note>
  This feature is in [public preview](/release-notes/feature-availability) and available only on [Standard and Enterprise plans](https://www.pinecone.io/pricing/).
</Note>

<RequestExample>
  ```python Python theme={null}
  from pinecone import Pinecone, ImportErrorMode

  pc = Pinecone(api_key="YOUR_API_KEY")

  # To get the unique host for an index, 
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  index = pc.Index(host="INDEX_HOST")
  root = "s3://BUCKET_NAME/PATH/TO/DIR"

  index.start_import(
      uri=root,
      error_mode=ImportErrorMode.CONTINUE, # or ImportErrorMode.ABORT
      integration_id="a12b3d4c-47d2-492c-a97a-dd98c8dbefde" # Optional for public buckets
  )
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  // To get the unique host for an index, 
  // see https://docs.pinecone.io/guides/manage-data/target-an-index
  const index = pc.index("INDEX_NAME", "INDEX_HOST")

  const storageURI = 's3://BUCKET_NAME/PATH/TO/DIR';
  const errorMode = 'continue'; // or 'abort'
  const integrationID = 'a12b3d4c-47d2-492c-a97a-dd98c8dbefde'; // Optional for public buckets

  await index.startImport(storageURI, errorMode, integrationID); 
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Pinecone;
  import io.pinecone.clients.AsyncIndex;
  import org.openapitools.db_data.client.ApiException;
  import org.openapitools.db_data.client.model.ImportErrorMode;
  import org.openapitools.db_data.client.model.StartImportResponse;

  public class StartImport {
      public static void main(String[] args) throws ApiException {
          // Initialize a Pinecone client with your API key
          Pinecone pinecone = new Pinecone.Builder("YOUR_API_KEY").build();

          // Get async imports connection object
          AsyncIndex asyncIndex = pinecone.getAsyncIndexConnection("docs-example");

          // s3 uri
          String uri = "s3://BUCKET_NAME/PATH/TO/DIR";

          // Integration ID (optional for public buckets)
          String integrationId = "a12b3d4c-47d2-492c-a97a-dd98c8dbefde";

          // Start an import
          StartImportResponse response = asyncIndex.startImport(uri, integrationId, ImportErrorMode.OnErrorEnum.CONTINUE);
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
      idxConnection, err := pc.Index(pinecone.NewIndexConnParams{Host: "INDEX_HOST"})
      if err != nil {
          log.Fatalf("Failed to create IndexConnection for Host: %v", err)
  	}

      uri := "s3://BUCKET_NAME/PATH/TO/DIR"
      errorMode := "continue" // or "abort"
      importRes, err := idxConnection.StartImport(ctx, uri, nil, (*pinecone.ImportErrorMode)(&errorMode))
      if err != nil {
          log.Fatalf("Failed to start import: %v", err)
      }
      fmt.Printf("Import started with ID: %s", importRes.Id)
  }
  ```

  ```csharp C# theme={null}
  using Pinecone;

  var pinecone = new PineconeClient("YOUR_API_KEY");

  // To get the unique host for an index, 
  // see https://docs.pinecone.io/guides/manage-data/target-an-index
  var index = pinecone.Index(host: "INDEX_HOST");

  var uri = "s3://BUCKET_NAME/PATH/TO/DIR";

  var response = await index.StartBulkImportAsync(new StartImportRequest
  {
      Uri = uri,
      IntegrationId = "a12b3d4c-47d2-492c-a97a-dd98c8dbefde",
      ErrorMode = new ImportErrorMode { OnError = ImportErrorModeOnError.Continue }
  });
  ```

  ```bash curl theme={null}
  # To get the unique host for an index,
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="INDEX_HOST"

  curl "https://$INDEX_HOST/bulk/imports" \
    -H 'Api-Key: $PINECONE_API_KEY' \
    -H 'Content-Type: application/json' \
    -H 'X-Pinecone-API-Version: 2025-04' \
    -d '{
          "integrationId": "a12b3d4c-47d2-492c-a97a-dd98c8dbefde",
          "uri": "s3://BUCKET_NAME/PATH/TO/DIR",
          "errorMode": {
              "onError": "continue"
              }
          }'
  ```
</RequestExample>

<ResponseExample>
  ```json  theme={null}
  {
     "id": "101"
  }
  ```
</ResponseExample>



# Describe a model
Source: https://docs.pinecone.io/reference/api/2025-04/inference/describe_model

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-04/inference_2025-04.oas.yaml get /models/{model_name}
Get a description of a model hosted by Pinecone. 

You can use hosted models as an integrated part of Pinecone operations or for standalone embedding and reranking. For more details, see [Vector embedding](https://docs.pinecone.io/guides/index-data/indexing-overview#vector-embedding) and [Rerank results](https://docs.pinecone.io/guides/search/rerank-results).

<RequestExample>
  ```python Python theme={null}
  from pinecone import Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  model = pc.inference.get_model(model_name="llama-text-embed-v2")

  print(model)
  ```

  ```javascript JavaScript theme={null}
  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  const model = await pc.inference.getModel('llama-text-embed-v2');

  console.log(model);
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Inference;
  import io.pinecone.clients.Pinecone;
  import org.openapitools.inference.client.ApiException;
  import org.openapitools.inference.client.model.ModelInfo;

  public class DescribeModel {
      public static void main(String[] args) throws ApiException {
          Pinecone pinecone = new Pinecone.Builder("YOUR_API_KEY").build();

          Inference inference = pinecone.getInferenceClient();

          ModelInfo modelInfo = inference.describeModel("llama-text-embed-v2");
          System.out.println(modelInfo);
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

      model, err := pc.Inference.DescribeModel(ctx, "llama-text-embed-v2")
      if err != nil {
          log.Fatalf("Failed to get model: %v", err)
      }
      fmt.Printf(prettifyStruct(model))
  }
  ```

  ```csharp C# theme={null}
  using Pinecone;
  using Pinecone.Inference;

  var pinecone = new PineconeClient("YOUR_API_KEY");

  var model = await pinecone.Inference.Models.GetAsync("llama-text-embed-v2");

  Console.WriteLine(model);
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl "https://api.pinecone.io/models/llama-text-embed-v2" \
      -H "Api-Key: $PINECONE_API_KEY" \
      -H "X-Pinecone-API-Version: 2025-04"
  ```
</RequestExample>

<ResponseExample>
  ```python Python theme={null}
  {'default_dimension': 1024,
   'max_batch_size': 96,
   'max_sequence_length': 2048,
   'modality': 'text',
   'model': 'llama-text-embed-v2',
   'provider_name': 'NVIDIA',
   'short_description': 'A high performance dense embedding model optimized for '
                        'multilingual and cross-lingual text question-answering '
                        'retrieval with support for long documents (up to 2048 '
                        'tokens) and dynamic embedding size (Matryoshka '
                        'Embeddings).',
   'supported_dimensions': [384, 512, 768, 1024, 2048],
   'supported_metrics': [cosine, dotproduct],
   'supported_parameters': [{'allowed_values': ['query', 'passage'],
                             'parameter': 'input_type',
                             'required': True,
                             'type': 'one_of',
                             'value_type': 'string'},
                            {'allowed_values': ['END', 'NONE', 'START'],
                             'default': 'END',
                             'parameter': 'truncate',
                             'required': False,
                             'type': 'one_of',
                             'value_type': 'string'},
                            {'allowed_values': [384, 512, 768, 1024, 2048],
                             'default': 1024,
                             'parameter': 'dimension',
                             'required': False,
                             'type': 'one_of',
                             'value_type': 'integer'}],
   'type': 'embed',
   'vector_type': 'dense'}
  ```

  ```javascript JavaScript theme={null}
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
    supportedDimensions: [ 384, 512, 768, 1024, 2048 ],
    supportedMetrics: [ 'Cosine', 'DotProduct' ],
    supportedParameters: [
      {
        parameter: 'input_type',
        type: 'one_of',
        valueType: 'string',
        required: true,
        allowedValues: [Array],
        min: undefined,
        max: undefined,
        _default: undefined
      },
      {
        parameter: 'truncate',
        type: 'one_of',
        valueType: 'string',
        required: false,
        allowedValues: [Array],
        min: undefined,
        max: undefined,
        _default: 'END'
      },
      {
        parameter: 'dimension',
        type: 'one_of',
        valueType: 'integer',
        required: false,
        allowedValues: [Array],
        min: undefined,
        max: undefined,
        _default: 1024
      }
    ]
  }
  ```

  ```java Java theme={null}
  class ModelInfo {
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
  }
  ```

  ```go Go theme={null}
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
  }
  ```

  ```csharp C# theme={null}
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
  }
  ```

  ```json curl theme={null}
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
  }
  ```
</ResponseExample>



# Generate vectors
Source: https://docs.pinecone.io/reference/api/2025-04/inference/generate-embeddings

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-04/inference_2025-04.oas.yaml post /embed
Generate vector embeddings for input data. This endpoint uses Pinecone's [hosted embedding models](https://docs.pinecone.io/guides/index-data/create-an-index#embedding-models).

<RequestExample>
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
</RequestExample>

<ResponseExample>
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
</ResponseExample>



---
**Navigation:** [← Previous](./23-load-the-documents-and-queries-of-legalbench-consu.md) | [Index](./index.md) | [Next →](./25-list-available-models.md)
