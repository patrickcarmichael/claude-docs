**Navigation:** [← Previous](./06-restore-a-pod-based-index.md) | [Index](./index.md) | [Next →](./08-manage-serverless-indexes.md)

# Back up an index
Source: https://docs.pinecone.io/guides/manage-data/back-up-an-index

Create backups of serverless indexes for protection


## Create a backup

You can [create a backup from a serverless index](/reference/api/latest/control-plane/create_backup) as follows.

<CodeGroup>
  ```python Python theme={null}
  from pinecone import Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  backup = pc.create_backup(
      index_name="docs-example", 
      backup_name="example-backup", 
      description="Monthly backup of production index"
  )

  print(backup)
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' })

  const backup = await pc.createBackup({
    indexName: 'docs-example',
    name: 'example-backup',
    description: 'Monthly backup of production index',
  });

  console.log(backup);
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Pinecone;
  import org.openapitools.db_control.client.ApiException;
  import org.openapitools.db_control.client.model.*;

  public class CreateBackup {
      public static void main(String[] args) throws ApiException {
          Pinecone pc = new Pinecone.Builder("YOUR_API_KEY").build();

          String indexName = "docs-example";
          String backupName = "example-backup";
          String backupDescription = "Monthly backup of production index";

          BackupModel backup = pc.createBackup(indexName,backupName, backupDescription);

          System.out.println(backup);
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
      backupName := "example-backup"
      backupDesc := "Monthly backup of production index"

      backup, err := pc.CreateBackup(ctx, &pinecone.CreateBackupParams{
          IndexName:   indexName,
          Name:        &backupName,
          Description: &backupDesc,
      })
      if err != nil {
          log.Fatalf("Failed to create backup: %v", err)
      }

      fmt.Printf(prettifyStruct(backup))
  }
  ```

  ```csharp C# theme={null}
  using Pinecone;

  var pinecone = new PineconeClient("PINECONE_API_KEY");

  var backup = await pinecone.Backups.BackupIndexAsync(
      "docs-example", 
      new BackupIndexRequest
      {
          Name = "example-backup",
          Description = "Monthly backup of production index"
      }
  );

  Console.WriteLine(backup);
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_NAME="docs-example"

  curl "https://api.pinecone.io/indexes/$INDEX_NAME/backups" \
      -H "Api-Key: $PINECONE_API_KEY" \
      -H 'accept: application/json' \
      -H 'Content-Type: application/json' \
      -H "X-Pinecone-API-Version: 2025-04" \
      -d '{
        "name": "example-backup", 
        "description": "Monthly backup of production index"
        }'
  ```
</CodeGroup>

The example returns a response like the following:

<CodeGroup>
  ```python Python theme={null}
  {'backup_id': '8c85e612-ed1c-4f97-9f8c-8194e07bcf71',
   'cloud': 'aws',
   'created_at': '2025-05-15T00:52:10.809305882Z',
   'description': 'Monthly backup of production index',
   'dimension': 1024,
   'name': 'example-backup',
   'namespace_count': 3,
   'record_count': 98,
   'region': 'us-east-1',
   'size_bytes': 1069169,
   'source_index_id': 'f73b36c9-faf5-4a2c-b1d6-4013d8b1cc74',
   'source_index_name': 'docs-example',
   'status': 'Ready',
   'tags': {}}
  ```

  ```javascript JavaScript theme={null}
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
  ```

  ```java Java theme={null}
  class BackupModel {
      backupId: 0d75b99f-be61-4a93-905e-77201286c02e
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
      createdAt: 2025-05-16T19:42:23.804787550Z
      additionalProperties: null
  }
  ```

  ```go Go theme={null}
  {
    "backup_id": "8c85e612-ed1c-4f97-9f8c-8194e07bcf71",
    "cloud": "aws",
    "created_at": "2025-05-15T00:52:10.809305882Z",
    "description": "Monthly backup of production index",
    "dimension": 1024,
    "name": "example-backup",
    "region": "us-east-1",
    "source_index_id": "f73b36c9-faf5-4a2c-b1d6-4013d8b1cc74",
    "source_index_name": "docs-example",
    "status": "Initializing",
    "tags": {}
  }
  ```

  ```csharp C# theme={null}
  {
      "backup_id": "8c85e612-ed1c-4f97-9f8c-8194e07bcf71",
      "source_index_name": "docs-example",
      "source_index_id": "f73b36c9-faf5-4a2c-b1d6-4013d8b1cc74",
      "name": "example-backup",
      "description": "Monthly backup of production index",
      "status": "Ready",
      "cloud": "aws",
      "region": "us-east-1",
      "tags": {},
      "created_at": "2025-05-15T00:52:10.809305882Z"
  }
  ```

  ```json curl theme={null}
  {
    "backup_id":"8c85e612-ed1c-4f97-9f8c-8194e07bcf71",
    "source_index_id":"f73b36c9-faf5-4a2c-b1d6-4013d8b1cc74",
    "source_index_name":"docs-example",
    "tags":{},
    "name":"example-backup",
    "description":"Monthly backup of production index",
    "status":"Ready",
    "cloud":"aws",
    "region":"us-east-1",
    "dimension":1024,
    "record_count":96,
    "namespace_count":3,
    "size_bytes":1069169,
    "created_at":"2025-05-14T16:37:25.625540Z"
    }
  ```
</CodeGroup>

<Tip>
  You can create a backup using the [Pinecone console](https://app.pinecone.io/organizations/-/projects/-/backups).
</Tip>


## Describe a backup

You can [view the details of a backup](/reference/api/latest/control-plane/describe_backup) as follows.

<CodeGroup>
  ```python Python theme={null}
  from pinecone import Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  backup = pc.describe_backup(backup_id="8c85e612-ed1c-4f97-9f8c-8194e07bcf71")

  print(backup)
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' })

  const backupDesc = await pc.describeBackup('8c85e612-ed1c-4f97-9f8c-8194e07bcf71');

  console.log(backupDesc);
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Pinecone;
  import org.openapitools.db_control.client.ApiException;
  import org.openapitools.db_control.client.model.*;

  public class CreateBackup {
      public static void main(String[] args) throws ApiException {
          Pinecone pc = new Pinecone.Builder("YOUR_API_KEY").build();

          BackupModel backupModel = pc.describeBackup("8c85e612-ed1c-4f97-9f8c-8194e07bcf71");

          System.out.println(backupModel);
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

  	backup, err := pc.DescribeBackup(ctx, "8c85e612-ed1c-4f97-9f8c-8194e07bcf71")
  	if err != nil {
  		log.Fatalf("Failed to describe backup: %v", err)
  	}
  	fmt.Printf(prettifyStruct(backup))
  }
  ```

  ```csharp C# theme={null}
  using Pinecone;

  var pinecone = new PineconeClient("PINECONE_API_KEY");

  var backup = await pinecone.Backups.GetAsync("8c85e612-ed1c-4f97-9f8c-8194e07bcf71");

  Console.WriteLine(backup);
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  BACKUP_ID="8c85e612-ed1c-4f97-9f8c-8194e07bcf71"

  curl -X GET "https://api.pinecone.io/backups/$BACKUP_ID" \
      -H "Api-Key: $PINECONE_API_KEY" \
      -H "X-Pinecone-API-Version: 2025-04" \
      -H "accept: application/json"
  ```
</CodeGroup>

The example returns a response like the following:

<CodeGroup>
  ```python Python theme={null}
  {'backup_id': '8c85e612-ed1c-4f97-9f8c-8194e07bcf71',
   'cloud': 'aws',
   'created_at': '2025-05-15T00:52:10.809354Z',
   'description': 'Monthly backup of production index',
   'dimension': 1024,
   'name': 'example-backup',
   'namespace_count': 3,
   'record_count': 98,
   'region': 'us-east-1',
   'size_bytes': 1069169,
   'source_index_id': 'f73b36c9-faf5-4a2c-b1d6-4013d8b1cc74',
   'source_index_name': 'docs-example',
   'status': 'Ready',
   'tags': {}}
  ```

  ```javascript JavaScript theme={null}
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
  ```

  ```java Java theme={null}
  class BackupList {
      data: [class BackupModel {
          backupId: 95707edb-e482-49cf-b5a5-312219a51a97
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
    "backup_id": "8c85e612-ed1c-4f97-9f8c-8194e07bcf71",
    "cloud": "aws",
    "created_at": "2025-05-15T00:52:10.809354Z",
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
  }
  ```

  ```csharp C# theme={null}
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
  }
  ```

  ```json curl theme={null}
  {
    "backup_id":"8c85e612-ed1c-4f97-9f8c-8194e07bcf71",
    "source_index_id":"f73b36c9-faf5-4a2c-b1d6-4013d8b1cc74",
    "source_index_name":"docs-example",
    "tags":{},
    "name":"example-backup",
    "description":"Monthly backup of production index",
    "status":"Ready",
    "cloud":"aws",
    "region":"us-east-1",
    "dimension":1024,
    "record_count":98,
    "namespace_count":3,
    "size_bytes":1069169,
    "created_at":"2025-03-11T18:29:50.549505Z"
  }
  ```
</CodeGroup>

<Tip>
  You can view backup details using the [Pinecone console](https://app.pinecone.io/organizations/-/projects-/backups).
</Tip>


## List backups for an index

You can [list backups for a specific index](/reference/api/latest/control-plane/list_index_backups) as follows.

Up to 100 backups are returned at a time by default, in sorted order (bitwise “C” collation). If the `limit` parameter is set, up to that number of backups are returned instead. Whenever there are additional backups to return, the response also includes a `pagination_token` that you can use to get the next batch of backups. When the response does not include a `pagination_token`, there are no more backups to return.

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


## List backups in a project

You can [list backups for all indexes in a project](/reference/api/latest/control-plane/list_project_backups) as follows.

Up to 100 backups are returned at a time by default, in sorted order (bitwise “C” collation). If the `limit` parameter is set, up to that number of backups are returned instead. Whenever there are additional backups to return, the response also includes a `pagination_token` that you can use to get the next batch of backups. When the response does not include a `pagination_token`, there are no more backups to return.

<CodeGroup>
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
      }, class BackupModel {
          backupId: 0d75b99f-be61-4a93-905e-77201286c02e
          sourceIndexName: example-dense-index
          sourceIndexId: f73b36c9-faf5-4a2c-b1d6-4013d8b1cc74
          name: example-backup2
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
          name: example-backup3
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
</CodeGroup>

<Tip>
  You can view all backups in a project using the [Pinecone console](https://app.pinecone.io/organizations/-/projects-/backups).
</Tip>


## Delete a backup

You can [delete a backup](/reference/api/latest/control-plane/delete_backup) as follows.

<CodeGroup>
  ```python Python theme={null}
  from pinecone import Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  pc.delete_backup(backup_id="9947520e-d5a1-4418-a78d-9f464c9969da")
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' })

  await pc.deleteBackup('9947520e-d5a1-4418-a78d-9f464c9969da');
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Pinecone;
  import org.openapitools.db_control.client.ApiException;
  import org.openapitools.db_control.client.model.*;

  public class CreateBackup {
      public static void main(String[] args) throws ApiException {
          Pinecone pc = new Pinecone.Builder("YOUR_API_KEY").build();

          pc.deleteBackup("9947520e-d5a1-4418-a78d-9f464c9969da");
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

  	err = pc.DeleteBackup(ctx, "8c85e612-ed1c-4f97-9f8c-8194e07bcf71")
  	if err != nil {
  		log.Fatalf("Failed to delete backup: %v", err)
  	} else {
  		fmt.Println("Backup deleted successfully")
  	}
  }
  ```

  ```csharp C# theme={null}
  using Pinecone;

  var pinecone = new PineconeClient("PINECONE_API_KEY");

  await pinecone.Backups.DeleteAsync("9947520e-d5a1-4418-a78d-9f464c9969da");
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  BACKUP_ID="9947520e-d5a1-4418-a78d-9f464c9969da"

  curl -X DELETE "https://api.pinecone.io/backups/$BACKUP_ID" \
      -H "Api-Key: $PINECONE_API_KEY" \
      -H "X-Pinecone-API-Version: 2025-04"
  ```
</CodeGroup>

<Tip>
  You can delete a backup using the [Pinecone console](https://app.pinecone.io/organizations/-/projects-/backups).
</Tip>



# Backups overview
Source: https://docs.pinecone.io/guides/manage-data/backups-overview

Learn about backups of serverless indexes in Pinecone.

A backup is a static copy of a serverless [index](/guides/index-data/indexing-overview) that only consumes storage. It is a non-queryable representation of a set of records. You can [create a backup](/guides/manage-data/back-up-an-index) of a serverless index, and you can [create a new serverless index from a backup](/guides/manage-data/restore-an-index). This allows you to restore the index with the same or different configurations.


## Use cases

Creating a backup is useful when performing tasks like the following:

* Protecting an index from manual or system failures.
* Temporarily shutting down an index.
* Copying the data from one index into a different index.
* Making a backup of your index.
* Experimenting with different index configurations.


## Performance

Backup and restore times depend upon the size of the index and number of namespaces:

* For less than 1M vectors in a namespace, backups and restores take approximately 10 minutes.
* For 100,000,000 vectors, backups and restores can take up to 5 hours.


## Quotas

| Metric                | Starter plan | Standard plan | Enterprise plan |
| :-------------------- | :----------- | :------------ | :-------------- |
| Backups per project   | N/A          | 500           | 1000            |
| Namespaces per backup | N/A          | 2000          | 2000            |


## Limitations

Backup limitations are as follows:

* Backups are stored in the same project, cloud provider, and region as the source index.
* You can only restore an index to the same project, cloud provider, and region as the source index.
* Backups only include vectors that were in the index at least 15 minutes prior to the backup time. This means that if a vector was inserted into an index and a backup was immediately taken after, the recently inserted vector may not be backed up. More specifically, if a backup is created only a few minutes after the source index was created, the backup may have 0 vectors.
* You can only perform operations on backups in the current Pinecone project.


## Backup and restore cost

* To understand how cost is calculated for backups and restores, see [Understanding cost](/guides/manage-cost/understanding-cost#backups-and-restores).
* For up-to-date pricing information, see [Pricing](https://www.pinecone.io/pricing/).



# Delete records
Source: https://docs.pinecone.io/guides/manage-data/delete-data

Delete records by ID or metadata filter from indexes

This page shows you how to [delete](/reference/api/latest/data-plane/delete) records from an index [namespace](/guides/index-data/indexing-overview#namespaces).


## Delete records by ID

Since Pinecone records can always be efficiently accessed using their ID, deleting by ID is the most efficient way to remove specific records from a namespace.

<Note>
  To remove records from the default namespace, specify `"__default__"` as the namespace in your request.
</Note>

<CodeGroup>
  ```Python Python theme={null}
  # pip install "pinecone[grpc]"
  from pinecone.grpc import PineconeGRPC as Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  # To get the unique host for an index, 
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  index = pc.Index(host="INDEX_HOST")

  index.delete(ids=["id-1", "id-2"], namespace='example-namespace')
  ```

  ```JavaScript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({ apiKey: "YOUR_API_KEY" })

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

  public class DeleteExample {
      public static void main(String[] args) {
          PineconeConfig config = new PineconeConfig("YOUR_API_KEY");
          // To get the unique host for an index, 
          // see https://docs.pinecone.io/guides/manage-data/target-an-index
          config.setHost("INDEX_HOST");
          PineconeConnection connection = new PineconeConnection(config);
          Index index = new Index(connection, "INDEX_NAME");
          List<String> ids = Arrays.asList("id-1", "id-2");
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

  ```bash curl theme={null}
  # To get the unique host for an index,
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="INDEX_HOST"

  curl "https://$INDEX_HOST/vectors/delete" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H 'Content-Type: application/json' \
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
</CodeGroup>


## Delete records by metadata

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


## Delete all records in a namespace

To delete all of the records in a namespace but not the namespace itself, provide a `namespace` parameter and specify the appropriate `deleteAll` parameter for your SDK. To target the default namespace, set `namespace` to `"__default__"`.

<CodeGroup>
  ```Python Python theme={null}
  # pip install "pinecone[grpc]"
  from pinecone.grpc import PineconeGRPC as Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  # To get the unique host for an index, 
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  index = pc.Index(host="INDEX_HOST")

  index.delete(delete_all=True, namespace='example-namespace')
  ```

  ```JavaScript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({ apiKey: "YOUR_API_KEY" })

  // To get the unique host for an index, 
  // see https://docs.pinecone.io/guides/manage-data/target-an-index
  const index = pc.index("INDEX_NAME", "INDEX_HOST")

  await index.namespace('example-namespace').deleteAll();
  ```

  ```java Java theme={null}
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
          index.deleteAll("example-namespace");
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

      err = idxConnection.DeleteAllVectorsInNamespace(ctx)
      if err != nil {
          log.Fatalf("Failed to delete all vectors in namespace %v: %v", namespace, err)
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
      DeleteAll = true,
      Namespace = "example-namespace",
  });
  ```

  ```bash curl theme={null}
  # To get the unique host for an index,
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="INDEX_HOST"

  curl "https://$INDEX_HOST/vectors/delete" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H 'Content-Type: application/json' \
    -H "X-Pinecone-API-Version: 2025-04" \
    -d '{
      "deleteAll": true,
      "namespace": "example-namespace"
    }
  '
  ```
</CodeGroup>


## Delete an entire namespace

To delete an entire namespace and all of its records, see [Delete a namespace](/guides/manage-data/manage-namespaces#delete-a-namespace).


## Delete an entire index

To remove all records from an index, [delete the index](/guides/manage-data/manage-indexes#delete-an-index) and [recreate it](/guides/index-data/create-an-index).


## Delete limits

**Delete by ID limits:**

| Metric              | Limit                                           |
| :------------------ | :---------------------------------------------- |
| Max IDs per request | 1000 IDs                                        |
| Max request rate    | 5000 requests per second per index or namespace |

**Delete by metadata limits:**

| Metric           | Limit                                                                      |
| :--------------- | :------------------------------------------------------------------------- |
| Max request rate | 5 requests per second per namespace<br />500 requests per second per index |


## Data freshness

Pinecone is eventually consistent, so there can be a slight delay before new or changed records are visible to queries. You can view index stats to [check data freshness](/guides/index-data/check-data-freshness).



# Fetch records
Source: https://docs.pinecone.io/guides/manage-data/fetch-data

Retrieve complete records by ID or metadata filter.

<Tip>
  You can fetch data using the [Pinecone console](https://app.pinecone.io/organizations/-/projects/-/indexes/-/browser).
</Tip>


## Fetch records by ID

To fetch records from a namespace based on their IDs, use the `fetch` operation with the following parameters:

* `namespace`: The [namespace](/guides/index-data/indexing-overview#namespaces) containing the records to fetch. To use the default namespace, set this to `"__default__"`.
* `ids`: The IDs of the records to fetch. Maximum of 1000.

<CodeGroup>
  ```Python Python theme={null}
  from pinecone.grpc import PineconeGRPC as Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  # To get the unique host for an index, 
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  index = pc.Index(host="INDEX_HOST")

  index.fetch(ids=["id-1", "id-2"], namespace="example-namespace")
  ```

  ```JavaScript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({ apiKey: "YOUR_API_KEY" })

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
          log.Fatalf("Failed to fetch vectors: %v", err)
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
      Namespace = "example-namespace"
  });
  ```

  ```bash curl theme={null}
  # To get the unique host for an index,
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="INDEX_HOST"

  curl -X GET "https://$INDEX_HOST/vectors/fetch?ids=id-1&ids=id-2&namespace=example-namespace" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-API-Version: 2025-04"
  ```
</CodeGroup>

The response looks like this:

<CodeGroup>
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
</CodeGroup>


## Fetch records by metadata

<Warning>
  This feature is in [early access](/release-notes/feature-availability) and is available only on the `2025-10` version of the API.
</Warning>

To fetch records from a namespace based on their metadata values, use the `fetch_by_metadata` operation with the following parameters:

* `namespace`: The [namespace](/guides/index-data/indexing-overview#namespaces) containing the records to fetch. To use the default namespace, set this to `"__default__"`.
* `filter`: A [metadata filter expression](/guides/index-data/indexing-overview#metadata-filter-expressions) to match the records to fetch.
* `limit`: The number of matching records to return. Defaults to 100. Maximum of 10,000.

For example, the following code fetches 200 records with a `genre` field set to `documentary` from namespace `example-namespace`:

```shell curl theme={null}

# To get the unique host for an index,

# see https://docs.pinecone.io/guides/manage-data/target-an-index
PINECONE_API_KEY="YOUR_API_KEY"
INDEX_HOST="INDEX_HOST"

curl -X POST "https://$INDEX_HOST/vectors/fetch_by_metadata" \
  -H 'Api-Key: $PINECONE_API_KEY' \
  -H 'Content-Type: application/json' \
  -H "X-Pinecone-API-Version: 2025-10" \
  -d '{
    "namespace": "example-namespace",
    "filter": {"rating": {"$lt": 5}},
    "limit": 2
  }'
```

The response looks like this:

```json curl theme={null}
{
  "vectors": {
    "id-1": {
      "id": "id-1",
      "values": [
        -0.0273742676,
        -0.000517368317,
        ...
      ],
      "metadata": {
        "main_category": "Books",
        "rating": 4,
        "review": "Identical twins have only one purpose in movies and plays: to cause mass confusion...",
        "title": "A comedy of twin-switching"
      }
    },
    "id-2": {
      "id": "id-2",
      "values": [
        -0.00305938721,
        0.0234375,
        ...
      ],
      "metadata": {
        "main_category": "Automotive",
        "rating": 1,
        "review": "If I could rate this 1/2 a star I would! These both broke within 10 minutes  of using it. The only upside is the cloth is removable so it can be used with good old fashioned  elbow grease. Epic waste!",
        "title": "Dont waste your money!"
      }
    }
  },
  "namespace": "example-namespace",
  "usage": {
    "readUnits": 1
  }
}
```


## Fetch limits

**Fetch by ID limits:**

| Metric              | Limit                             |
| :------------------ | :-------------------------------- |
| Max IDs per request | 1000 IDs                          |
| Max request size    | N/A                               |
| Max request rate    | 100 requests per second per index |

**Fetch by metadata limits:**

| Metric                   | Limit                                |
| :----------------------- | :----------------------------------- |
| Max records per response | 10,000 records                       |
| Max response size        | 4MB                                  |
| Max response rate        | 10 requests per second per namespace |


## Data freshness

Pinecone is eventually consistent, so there can be a slight delay before new or changed records are visible to queries. You can view index stats to [check data freshness](/guides/index-data/check-data-freshness).



# List record IDs
Source: https://docs.pinecone.io/guides/manage-data/list-record-ids

List the IDS of records in an index namespace.

You can list the IDs of all records in a [namespace](/guides/index-data/indexing-overview#namespaces) or just the records with a common ID prefix.

Using `list` to get record IDs and not the associated data is a cheap and fast way to check [upserts](/guides/index-data/upsert-data).

<Note>
  The `list` endpoint is supported only for serverless indexes.
</Note>


## List the IDs of all records in a namespace

To list the IDs of all records in the namespace of a serverless index, pass only the `namespace` parameter:

<CodeGroup>
  ```python Python theme={null}
  from pinecone.grpc import PineconeGRPC as Pinecone

  pc = Pinecone(api_key='YOUR_API_KEY')

  # To get the unique host for an index, 
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  index = pc.Index(host="INDEX_HOST")

  for ids in index.list(namespace='example-namespace'):
      print(ids)

  # Response:
  # ['doc1#chunk1', 'doc1#chunk2', 'doc1#chunk3']
  ```

  ```js JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';
  const pc = new Pinecone();

  // To get the unique host for an index, 
  // see https://docs.pinecone.io/guides/manage-data/target-an-index
  const index = pc.index("INDEX_NAME", "INDEX_HOST").namespace("example-namespace");

  const results = await index.listPaginated();
  console.log(results);
  // {
  //   vectors: [
  //     { id: 'doc1#01' }, { id: 'doc1#02' }, { id: 'doc1#03' },
  //     { id: 'doc1#04' }, { id: 'doc1#05' },  { id: 'doc1#06' },
  //     { id: 'doc1#07' }, { id: 'doc1#08' }, { id: 'doc1#09' },
  //     ...
  //   ],
  //   pagination: {
  //     next: 'eyJza2lwX3Bhc3QiOiJwcmVUZXN0LS04MCIsInByZWZpeCI6InByZVRlc3QifQ=='
  //   },
  //   namespace: 'example-namespace',
  //   usage: { readUnits: 1 }
  // }

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
          // get the pagination token
          String paginationToken = index.list("example-namespace", 3).getPagination().getNext();
          // get vectors with limit 3 with the paginationToken obtained from the previous step
          ListResponse listResponse = index.list("example-namespace", 3, paginationToken);
      }
  }

  // Response:
  // vectors {
  //   id: "doc1#chunk1"
  // }
  // vectors {
  //   id: "doc1#chunk2"
  // }
  // vectors {
  //   id: "doc2#chunk1"
  // }
  // vectors {
  //   id: "doc3#chunk1"
  // }
  // pagination {
  //   next: "eyJza2lwX3Bhc3QiOiJhbHN0cm9lbWVyaWEtcGVydXZpYW4iLCJwcmVmaXgiOm51bGx9"
  // }
  // namespace: "example-namespace"
  // usage {
  //   read_units: 1
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

      // To get the unique host for an index, 
      // see https://docs.pinecone.io/guides/manage-data/target-an-index
      idxConnection, err := pc.Index(pinecone.NewIndexConnParams{Host: "INDEX_HOST", Namespace: "example-namespace"})
      if err != nil {
          log.Fatalf("Failed to create IndexConnection for Host: %v", err)
    	}

      limit := uint32(3)

      res, err := idxConnection.ListVectors(ctx, &pinecone.ListVectorsRequest{
          Limit:  &limit,
      })
      if len(res.VectorIds) == 0 {
          fmt.Println("No vectors found")
  	} else {
  		fmt.Printf(prettifyStruct(res))
  	}
  }

  // Response:
  // {
  //   "vector_ids": [
  //     "doc1#chunk1",
  //     "doc1#chunk2",
  //     "doc1#chunk3"
  //   ],
  //   "usage": {
  //     "read_units": 1
  //   },
  //   "next_pagination_token": "eyJza2lwX3Bhc3QiOiIwMDBkMTc4OC0zMDAxLTQwZmMtYjZjNC0wOWI2N2I5N2JjNDUiLCJwcmVmaXgiOm51bGx9"
  // }
  ```

  ```csharp C# theme={null}
  using Pinecone;

  var pinecone = new PineconeClient("YOUR_API_KEY");

  // To get the unique host for an index, 
  // see https://docs.pinecone.io/guides/manage-data/target-an-index
  var index = pinecone.Index(host: "INDEX_HOST");

  var listResponse = await index.ListAsync(new ListRequest {
      Namespace = "example-namespace",
  });

  Console.WriteLine(listResponse);

  // Response:
  // {
  //   "vectors": [
  //     {
  //       "id": "doc1#chunk1"
  //     },
  //     {
  //       "id": "doc1#chunk2"
  //     },
  //     {
  //       "id": "doc1#chunk3"
  //     }
  //   ],
  //   "pagination": "eyJza2lwX3Bhc3QiOiIwMDBkMTc4OC0zMDAxLTQwZmMtYjZjNC0wOWI2N2I5N2JjNDUiLCJwcmVmaXgiOm51bGx9",
  //   "namespace": "example-namespace",
  //   "usage": {
  //     "readUnits": 1
  //   }
  // }
  ```

  ```shell curl theme={null}
  # To get the unique host for an index,
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="INDEX_HOST"

  curl -X GET "https://$INDEX_HOST/vectors/list?namespace=example-namespace" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-API-Version: 2025-04"

  # Response:
  # {
  #   "vectors": [
  #     { "id": "doc1#chunk1" },
  #     { "id": "doc1#chunk2" },
  #     { "id": "doc1#chunk3" },
  #     { "id": "doc1#chunk4" },
  #    ...
  #   ],
  #   "pagination": {
  #     "next": "c2Vjb25kY2FsbA=="
  #   },
  #   "namespace": "example-namespace",
  #   "usage": {
  #     "readUnits": 1
  #   }
  # }
  ```
</CodeGroup>


## List the IDs of records with a common prefix

ID prefixes enable you to query segments of content. Use the `list` endpoint to list all of the records with the common prefix. For more details, see [Use structured IDs](/guides/index-data/data-modeling#use-structured-ids).


## Paginate through results

The `list` endpoint returns up to 100 IDs per page at a time by default. If the `limit` parameter is passed, `list` returns up to that number of IDs per page instead. For example, if `limit=3`, up to 3 IDs be returned per page. Whenever there are additional IDs to return, the response also includes a `pagination_token` for fetching the next page of IDs.

### Implicit pagination

When using the Python SDK, `list` paginates automatically.

```python Python theme={null}
from pinecone.grpc import PineconeGRPC as Pinecone

pc = Pinecone(api_key='YOUR_API_KEY')


# To get the unique host for an index, 

# see https://docs.pinecone.io/guides/manage-data/target-an-index
index = pc.Index(host="INDEX_HOST")

for ids in index.list(namespace='example-namespace'):
    print(ids)


# Response:

# ['doc1#chunk1', 'doc1#chunk2', 'doc1#chunk3']

# ['doc1#chunk4', 'doc1#chunk5', 'doc1#chunk6']

# ...
```

### Manual pagination

When using the Node.js SDK, Java SDK, Go SDK, .NET SDK, or REST API, you must manually fetch each page of results. You can also manually paginate with the Python SDK using `list_paginated()`.

<CodeGroup>
  ```python Python theme={null}
  from pinecone.grpc import PineconeGRPC as Pinecone

  pc = Pinecone(api_key='YOUR_API_KEY')

  # To get the unique host for an index, 
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  index = pc.Index(host="INDEX_HOST")

  namespace = 'example-namespace'

  # For manual control over pagination
  results = index.list_paginated(
      prefix='pref',
      limit=3,
      namespace='example-namespace'
  )
  print(results.namespace)
  print([v.id for v in results.vectors])
  print(results.pagination.next)
  print(results.usage)

  # Results:
  # ['10103-0', '10103-1', '10103-10']
  # eyJza2lwX3Bhc3QiOiIxMDEwMy0=
  # {'read_units': 1}
  ```

  ```js JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';
  const pc = new Pinecone();

  // To get the unique host for an index, 
  // see https://docs.pinecone.io/guides/manage-data/target-an-index
  const index = pc.index("INDEX_NAME", "INDEX_HOST").namespace("example-namespace");

  const results = await index.listPaginated({ prefix: 'doc1#', limit: 3 });
  console.log(results);

  // Response:
  // {
  //   vectors: [
  //     { id: 'doc1#01' }, { id: 'doc1#02' }, { id: 'doc1#03' }
  //   ],
  //   pagination: {
  //     next: 'eyJza2lwX3Bhc3QiOiJwcmVUZXN0LSCIsInByZWZpeCI6InByZVRlc3QifQ=='
  //   },
  //   namespace: 'example-namespace',
  //   usage: { readUnits: 1 }
  // }
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
          ListResponse listResponse = index.list("example-namespace", "doc1#" 2); /* Note: You must include an ID prefix to list vector IDs. */
          System.out.println(listResponse.getVectorsList());
          System.out.println(listResponse.getPagination());
      }
  }

  // Response:
  // vectors {
  //   id: "doc1#chunk1"
  // }
  // vectors {
  //   id: "doc1#chunk2"
  // }
  // pagination {
  //   next: "eyJza2lwX3Bhc3QiOiJhbHN0cm9lbWVyaWEtcGVydXZpYW4iLCJwcmVmaXgiOm51bGx9"
  // }
  // namespace: "example-namespace"
  // usage {
  //   read_units: 1
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

      // To get the unique host for an index, 
      // see https://docs.pinecone.io/guides/manage-data/target-an-index
      idxConnection, err := pc.Index(pinecone.NewIndexConnParams{Host: "INDEX_HOST", Namespace: "example-namespace"})
      if err != nil {
          log.Fatalf("Failed to create IndexConnection for Host: %v", err)
    	}

      limit := uint32(3)

      res, err := idxConnection.ListVectors(ctx, &pinecone.ListVectorsRequest{
          Limit:  &limit,
      })
      if len(res.VectorIds) == 0 {
          fmt.Println("No vectors found")
      } else {
          fmt.Printf(prettifyStruct(res))
      }
  }

  // Response:
  // {
  //   "vector_ids": [
  //     "doc1#chunk1",
  //     "doc1#chunk2",
  //     "doc1#chunk3"
  //   ],
  //   "usage": {
  //     "read_units": 1
  //   },
  //   "next_pagination_token": "eyJza2lwX3Bhc3QiOiIwMDBkMTc4OC0zMDAxLTQwZmMtYjZjNC0wOWI2N2I5N2JjNDUiLCJwcmVmaXgiOm51bGx9"
  // }
  ```

  ```csharp C# theme={null}
  using Pinecone;

  var pinecone = new PineconeClient("YOUR_API_KEY");

  // To get the unique host for an index, 
  // see https://docs.pinecone.io/guides/manage-data/target-an-index
  var index = pinecone.Index(host: "INDEX_HOST");

  var listResponse = await index.ListAsync(new ListRequest {
      Namespace = "example-namespace",
      Prefix = "document1#",
  });

  Console.WriteLine(listResponse);

  // Response:
  // {
  //   "vectors": [
  //     {
  //       "id": "doc1#chunk1"
  //     },
  //     {
  //       "id": "doc1#chunk2"
  //     },
  //     {
  //       "id": "doc1#chunk3"
  //     }
  //   ],
  //   "pagination": "eyJza2lwX3Bhc3QiOiIwMDBkMTc4OC0zMDAxLTQwZmMtYjZjNC0wOWI2N2I5N2JjNDUiLCJwcmVmaXgiOm51bGx9",
  //   "namespace": "example-namespace",
  //   "usage": {
  //     "readUnits": 1
  //   }
  // }
  ```

  ```shell curl theme={null}
  # To get the unique host for an index,
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="INDEX_HOST"

  curl -X GET "https://$INDEX_HOST/vectors/list?namespace=example-namespace" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-API-Version: 2025-04"

  # Response:
  # {
  #   "vectors": [
  #     { "id": "doc1#chunk1" },
  #     { "id": "doc1#chunk2" },
  #     { "id": "doc1#chunk3" },
  #     { "id": "doc1#chunk4" },
  #    ...
  #   ],
  #   "pagination": {
  #     "next": "c2Vjb25kY2FsbA=="
  #   },
  #   "namespace": "example-namespace",
  #   "usage": {
  #     "readUnits": 1
  #   }
  # }
  ```
</CodeGroup>

Then, to get the next batch of IDs, use the returned `pagination_token`:

<CodeGroup>
  ```python Python theme={null}
  from pinecone.grpc import PineconeGRPC as Pinecone

  pc = Pinecone(api_key='YOUR_API_KEY')

  # To get the unique host for an index, 
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  index = pc.Index(host="INDEX_HOST")

  namespace = 'example-namespace'

  results = index.list_paginated(
      prefix='pref',
      limit=3,
      namespace='example-namespace',
      pagination_token='eyJza2lwX3Bhc3QiOiIxMDEwMy0='
  )
  print(results.namespace)
  print([v.id for v in results.vectors])
  print(results.pagination.next)
  print(results.usage)

  # Response:
  # ['10103-0', '10103-1', '10103-10']
  # xndlsInByZWZpeCI6IjEwMTAzIn0==
  # {'read_units': 1}
  ```

  ```js JavaScript theme={null}
  await index.listPaginated({ prefix: 'doc1#', limit: 3, paginationToken: results.pagination.next});

  // Response:
  // {
  //   vectors: [
  //     { id: 'doc1#10' }, { id: 'doc1#11' }, { id: 'doc1#12' }
  //   ],
  //   pagination: {
  //     next: 'dfajlkjfdsoijeowjoDJFKLJldLIFf34KFNLDSndaklqoLQJORN45afdlkJ=='
  //   },
  //   namespace: 'example-namespace',
  //   usage: { readUnits: 1 }
  // }
  ```

  ```java Java theme={null}
  listResponse = index.list("example-namespace", "doc1#", "eyJza2lwX3Bhc3QiOiJ2MTg4IiwicHJlZml4IjpudWxsfQ==");
  System.out.println(listResponse.getVectorsList());

  // Response:
  // vectors {
  //   id: "doc1#chunk3"
  // }
  // vectors {
  //   id: "doc1#chunk4"
  // }
  // vectors {
  //   id: "doc1#chunk5"
  // }
  // vectors {
  //   id: "doc1#chunk6"
  // }
  // vectors {
  //   id: "doc1#chunk7"
  // }
  // vectors {
  //   id: "doc1#chunk8"
  // }
  // pagination {
  //   next: "eyJza2lwX3Bhc3QiOiJhbHN0cm9lbWVyaWEtcGVydXZpYW4iLCJwcmVmaXgiOm51bGx9"
  // }
  // namespace: "example-namespace"
  // usage {
  //   read_units: 1
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

      // To get the unique host for an index, 
      // see https://docs.pinecone.io/guides/manage-data/target-an-index
      idxConnection, err := pc.Index(pinecone.NewIndexConnParams{Host: "INDEX_HOST", Namespace: "example-namespace"})
      if err != nil {
          log.Fatalf("Failed to create IndexConnection for Host: %v", err)
    	}

      limit := uint32(3)
      paginationToken := "dfajlkjfdsoijeowjoDJFKLJldLIFf34KFNLDSndaklqoLQJORN45afdlkJ=="

      res, err := idxConnection.ListVectors(ctx, &pinecone.ListVectorsRequest{
          Limit:  &limit,
          PaginationToken: &paginationToken,
      })
      if len(res.VectorIds) == 0 {
          fmt.Println("No vectors found")
  	} else {
  	    fmt.Printf(prettifyStruct(res))
  	}
  }

  // Response:
  // {
  //   "vector_ids": [
  //     "doc1#chunk4",
  //     "doc1#chunk5",
  //     "doc1#chunk6"
  //   ],
  //   "usage": {
  //     "read_units": 1
  //   },
  //   "next_pagination_token": "eyJza2lwX3Bhc3QiOiIwMDBkMTc4OC0zMDAxLTQwZmMtYjZjNC0wOWI2N2I5N2JjNDUiLCJwcmVmaXgiOm51bGx9"
  // }
  ```

  ```csharp C# theme={null}
  using Pinecone;

  var pinecone = new PineconeClient("YOUR_API_KEY");

  // To get the unique host for an index, 
  // see https://docs.pinecone.io/guides/manage-data/target-an-index
  var index = pinecone.Index(host: "INDEX_HOST");

  var listResponse = await index.ListAsync(new ListRequest {
      Namespace = "example-namespace",
      Prefix = "document1#",
      PaginationToken= "eyJza2lwX3Bhc3QiOiIwMDBkMTc4OC0zMDAxLTQwZmMtYjZjNC0wOWI2N2I5N2JjNDUiLCJwcmVmaXgiOm51bGx9",
  });

  Console.WriteLine(listResponse);

  // Response:
  // {
  //   "vectors": [
  //     {
  //       "id": "doc1#chunk4"
  //     },
  //     {
  //       "id": "doc1#chunk5"
  //     },
  //     {
  //       "id": "doc1#chunk6"
  //     }
  //   ],
  //   "pagination": "dfajlkjfdsoijeowjoDJFKLJldLIFf34KFNLDSndaklqoLQJORN45afdlkJ==",
  //   "namespace": "example-namespace",
  //   "usage": {
  //     "readUnits": 1
  //   }
  // }
  ```

  ```shell curl theme={null}
  # To get the unique host for an index,
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="INDEX_HOST"

  curl -X GET "https://$INDEX_HOST/vectors/list?namespace=example-namespace&paginationToken=c2Vjb25kY2FsbA%3D%3D" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-API-Version: 2025-04"

  # Response:
  # {
  #   "vectors": [
  #     { "id": "doc2#chunk1" },
  #     { "id": "doc2#chunk1" },
  #     { "id": "doc2#chunk1" },
  #     { "id": "doc2#chunk1" },
  #    ...
  #   ],
  #   "pagination": {
  #     "next": "mn23b4jB3Y9jpsS1"
  #   },
  #   "namespace": "example-namespace",
  #   "usage": {
  #     "readUnits": 1
  #   }
  # }
  ```
</CodeGroup>

When there are no more IDs to return, the response does not includes a `pagination_token`:

<CodeGroup>
  ```python Python theme={null}
  from pinecone.grpc import PineconeGRPC as Pinecone

  pc = Pinecone(api_key='YOUR_API_KEY')

  index = pc.Index(host="INDEX_HOST")

  namespace = 'example-namespace'

  results = index.list_paginated(
      prefix='10103',
      limit=3,
      pagination_token='xndlsInByZWZpeCI6IjEwMTAzIn0=='
  )

  print(results.namespace)
  print([v.id for v in results.vectors])
  print(results.pagination.next)
  print(results.usage)

  # Response:
  # ['10103-4', '10103-5', '10103-6']
  # {'read_units': 1}
  ```

  ```js JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';
  const pc = new Pinecone();

  const index = pc.index("INDEX_NAME", "INDEX_HOST").namespace("example-namespace");

  const results = await index.listPaginated({ prefix: 'doc1#' });
  console.log(results);

  // Response:
  // {
  //   vectors: [
  //     { id: 'doc1#19' }, { id: 'doc1#20' }, { id: 'doc1#21' }
  //   ],
  //   namespace: 'example-namespace',
  //   usage: { readUnits: 1 }
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

      idxConnection, err := pc.Index(pinecone.NewIndexConnParams{Host: "INDEX_HOST", Namespace: "example-namespace"})
      if err != nil {
          log.Fatalf("Failed to create IndexConnection for Host: %v", err)
    	}

      limit := uint32(3)
      paginationToken := "eyJza2lwX3Bhc3QiOiIwMDBkMTc4OC0zMDAxLTQwZmMtYjZjNC0wOWI2N2I5N2JjNDUiLCJwcmVmaXgiOm51bGx9"

      res, err := idxConnection.ListVectors(ctx, &pinecone.ListVectorsRequest{
          Limit:  &limit,
          paginationToken: &paginationToken,
      })
      if len(res.VectorIds) == 0 {
          fmt.Println("No vectors found")
    	} else {
  	    fmt.Printf(prettifyStruct(res))
  	}
  }

  // Response:
  // {
  //   "vector_ids": [
  //     "doc1#chunk7",
  //     "doc1#chunk8",
  //     "doc1#chunk9"
  //   ],
  //   "usage": {
  //     "read_units": 1
  //   }
  // }
  ```

  ```csharp C# theme={null}
  using Pinecone;

  var pinecone = new PineconeClient("YOUR_API_KEY");

  var index = pinecone.Index(host: "INDEX_HOST");

  var listResponse = await index.ListAsync(new ListRequest {
      Namespace = "example-namespace",
      Prefix = "document1#",
      PaginationToken= "dfajlkjfdsoijeowjoDJFKLJldLIFf34KFNLDSndaklqoLQJORN45afdlkJ==",
  });

  Console.WriteLine(listResponse);

  // Response:
  // {
  //   "vectors": [
  //     {
  //       "id": "doc1#chunk7"
  //     },
  //     {
  //       "id": "doc1#chunk8"
  //     },
  //     {
  //       "id": "doc1#chunk9"
  //     }
  //   ],
  //   "pagination": null,
  //   "namespace": "example-namespace",
  //   "usage": {
  //     "readUnits": 1
  //   }
  // }
  ```

  ```shell curl theme={null}
  # To get the unique host for an index,
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="INDEX_HOST"

  curl -X GET "https://$INDEX_HOST/vectors/list?namespace=example-namespace&paginationToken=mn23b4jB3Y9jpsS1" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-API-Version: 2025-04"
  # Response:
  # {
  #   "vectors": [
  #     { "id": "doc3#chunk1" },
  #     { "id": "doc5#chunk2" },
  #     { "id": "doc5#chunk3" },
  #     { "id": "doc5#chunk4" },
  #    ...
  #   ],
  #   "namespace": "example-namespace",
  #   "usage": {
  #     "readUnits": 1
  #   }
  # }
  ```
</CodeGroup>



---
**Navigation:** [← Previous](./06-restore-a-pod-based-index.md) | [Index](./index.md) | [Next →](./08-manage-serverless-indexes.md)
