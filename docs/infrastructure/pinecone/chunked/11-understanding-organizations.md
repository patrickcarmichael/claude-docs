**Navigation:** [← Previous](./10-use-the-pinecone-mcp-server.md) | [Index](./index.md) | [Next →](./12-configure-audit-logs.md)

# Understanding organizations
Source: https://docs.pinecone.io/guides/organizations/understanding-organizations

Understand organization structure, projects, and billing.

A Pinecone organization is a set of [projects](/guides/projects/understanding-projects) that use the same billing. Organizations allow one or more users to control billing and project permissions for all of the projects belonging to the organization. Each project belongs to an organization.

<Note>
  While an email address can be associated with multiple organizations, it cannot be used to create more than one organization. For information about managing organization members, see [Manage organization members](/guides/organizations/manage-organization-members).
</Note>


## Projects in an organization

Each organization contains one or more projects that share the same organization owners and billing settings. Each project belongs to exactly one organization. If you need to move a project from one organization to another, [contact Support](https://app.pinecone.io/organizations/-/settings/support/ticket).


## Billing settings

All of the projects in an organization share the same billing method and settings. The billing settings for the organization are controlled by the organization owners.

Organization owners can update the billing contact information, update the payment method, and view and download invoices using the [Pinecone console](https://app.pinecone.io/organizations/-/settings/billing).


## Organization roles

Organization owners can manage access to their organizations and projects by assigning roles to organization members and service accounts. The role determines the entity's permissions within Pinecone. The organization roles are as follows:

* **Organization owner**: Organization owners have global permissions across the organization. This includes managing billing details, organization members, and all projects. Organization owners are automatically [project owners](/guides/projects/understanding-projects#project-roles) and, therefore, have all project owner permissions as well.

* **Organization user**: Organization users have restricted organization-level permissions. When inviting organization users, you also choose the projects they belong to and the project role they should have.

* **Billing admin**: Billing admins have permissions to view and update billing details, but they cannot manage organization members. Billing admins cannot manage projects unless they are also [project owners](/guides/projects/understanding-projects#project-roles).

The following table summarizes the permissions for each organization role:

| Permission                           | Org Owner | Org User | Billing Admin |
| ------------------------------------ | --------- | -------- | ------------- |
| View account details                 | ✓         | ✓        | ✓             |
| Update organization name             | ✓         |          |               |
| Delete the organization              | ✓         |          |               |
| View billing details                 | ✓         |          | ✓             |
| Update billing details               | ✓         |          | ✓             |
| View usage details                   | ✓         |          | ✓             |
| View support plans                   | ✓         |          | ✓             |
| Invite members to the organization   | ✓         |          |               |
| Delete pending member invites        | ✓         |          |               |
| Remove members from the organization | ✓         |          |               |
| Update organization member roles     | ✓         |          |               |
| Create projects                      | ✓         | ✓        |               |


## Organization single sign-on (SSO)

SSO allows organizations to manage their teams' access to Pinecone through their identity management solution. Once your integration is configured, you can specify a default role for teammates when they sign up.

For more information, see [Configure single sign-on](/guides/production/configure-single-sign-on/okta).

<Note>SSO is available on Standard and Enterprise plans.</Note>


## Service accounts

<Note>
  This feature is in [public preview](/release-notes/feature-availability) and available only on [Enterprise plans](https://www.pinecone.io/pricing/).
</Note>

[Service accounts](/guides/organizations/manage-service-accounts) enable programmatic access to Pinecone's Admin API, which can be used to create and manage projects and API keys.

Use service accounts to automate infrastructure management and integrate Pinecone into your deployment workflows, rather than through manual actions in the Pinecone console. Service accounts use the [organization roles](/guides/organizations/understanding-organizations#organization-roles) and [project role](/guides/projects/understanding-projects#project-roles) for permissioning, and provide a secure and auditable way to handle programmatic access.


## See also

* [Manage organization members](/guides/organizations/manage-organization-members)
* [Manage project members](/guides/projects/manage-project-members)



# CI/CD with Pinecone Local and GitHub Actions
Source: https://docs.pinecone.io/guides/production/automated-testing

Test Pinecone integration with CI/CD workflows.

Pinecone Local is an in-memory Pinecone Database emulator available as a Docker image.

This page shows you how to build a CI/CD workflow with Pinecone Local and [GitHub Actions](https://docs.github.com/en/actions) to test your integration without connecting to your Pinecone account, affecting production data, or incurring any usage or storage fees.

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


## 1. Write your tests

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


## 2. Set up GitHub Actions

[Set up a GitHub Actions workflow](https://docs.github.com/en/actions/writing-workflows/quickstart) to do the following:

1. Pull the Pinecone Local Docker image.
2. Start a Pinecone Local instance for each test run.
3. Execute tests against the local instance.
4. Tear down the instance after tests complete.

Here's a sample GitHub Actions workflow that you can extend for your own needs:

```yaml  theme={null}
name: CI/CD with Pinecone Local
on:
  pull_request:
    branches:
      - main
  push:
    branches:
      - main

jobs:
  pc-local-tests:
    name: Pinecone Local tests
    runs-on: ubuntu-latest
    services:
      pc-local:
        image: ghcr.io/pinecone-io/pinecone-local:latest
        env:
          PORT: 5080
        ports:
          - "5080-6000:5080-6000"
    steps:
      - name: Check out repository code
        uses: actions/checkout@v4

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install "pinecone[grpc]"

      - name: Run tests
        run: |
          pytest test/
```


## 3. Run your tests

GitHub Actions will automaticaly run your tests against Pinecone Local when the events you specified in your workflow occur.

For a list of the events that can trigger a workflow and more details about using GitHub Actions for CI/CD, see the [GitHub Actions documentation](https://docs.github.com/en/actions).



# Bring your own cloud
Source: https://docs.pinecone.io/guides/production/bring-your-own-cloud

Deploy Pinecone in your AWS or GCP account

Bring your own cloud (BYOC) lets you deploy Pinecone Database in your own AWS or GCP account to ensure data sovereignty and compliance, with Pinecone handling provisioning, operations, and maintenance.

<Note>
  BYOC is in [public preview](/release-notes/feature-availability) on AWS and GCP. To learn more about the offering, [contact Pinecone](https://www.pinecone.io/contact/?contact_form_inquiry_type=Product+Information).
</Note>


## Use cases

Pinecone BYOC is designed for organizations with high security and compliance requirements, for example:

* **Data sovereignty**: If your organization has strict data governance policies, Pinecone BYOC can help ensure that all data is stored and processed locally and does not leave your security perimeter.
* **Data residency**: The standard Pinecone managed service can be deployed in several [AWS or GCP cloud regions](/guides/index-data/create-an-index#cloud-regions). If your organization has specific data residency or latency constraints that require you to deploy in regions that Pinecone does not yet support, Pinecone BYOC gives you that flexibility.


## Architecture

<img className="block max-w-full dark:hidden" noZoom src="https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/byoc.png?fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=01b34857159d1eb8849f4250aa79ed00" data-og-width="2040" width="2040" data-og-height="1240" height="1240" data-path="images/byoc.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/byoc.png?w=280&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=e925a3467600c20f1c37e68e49d38acb 280w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/byoc.png?w=560&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=c2c1b4077bf7f8dc593553a399e5fff6 560w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/byoc.png?w=840&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=6688be4f64b0b4db4fe2ef90e04d6c44 840w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/byoc.png?w=1100&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=4aa2923e28afc6a167bd8dfb28662c58 1100w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/byoc.png?w=1650&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=c5c4c539a148f31e977c39c2ca813733 1650w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/byoc.png?w=2500&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=8669a2c64a678822e7f2abe7dde6fdf0 2500w" />

<img className="hidden max-w-full dark:block" noZoom src="https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/byoc-dark.png?fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=a27381222b26d1f31bc7d52b09f3ace0" data-og-width="2040" width="2040" data-og-height="1240" height="1240" data-path="images/byoc-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/byoc-dark.png?w=280&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=f18f81d0f2a9387d2fd10231a4952284 280w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/byoc-dark.png?w=560&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=7be91ffb937303f692dac9f4c7a812b6 560w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/byoc-dark.png?w=840&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=06ec40f990b9795d42cd670c1f80e603 840w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/byoc-dark.png?w=1100&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=6cc520e19003068137c960d9064648fc 1100w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/byoc-dark.png?w=1650&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=902b44ca748163f9b199f128c5c7f543 1650w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/byoc-dark.png?w=2500&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=6d1fc020dbfb7fc4d144012711c10a2a 2500w" />

The BYOC architecture employs a split model:

* **Data plane**: The data plane is responsible for storing and processing your records, executing queries, and interacting with object storage for index data. In a BYOC deployment, the data plane is hosted in your own AWS or GCP account within a dedicated VPC, ensuring that all data is stored and processed locally and does not leave your organizational boundaries. You use a [private endpoint](#configure-a-private-endpoint) (AWS PrivateLink or GCP Private Service Connect) as an additional measure to secure requests to your indexes.
* **Control plane**: The control plane is responsible for managing the index lifecycle as well as region-agnostic services such as user management, authentication, and billing. The control plane does not hold or process any records. In a BYOC deployment, the control plane is managed by Pinecone and hosted globally. Communication between the data plane and control plane is encrypted using TLS and employs role-based access control (RBAC) with minimal IAM permissions.


## Onboarding

The onboarding process for BYOC in AWS or GCP involves the following general stages:

<Steps>
  <Step title="Set up AWS or GCP account">
    If you don't already have an AWS or GCP account where you want to deploy Pinecone, you create one for this purpose.
  </Step>

  <Step title="Execute Terraform template">
    You download and run a Terraform template provided by Pinecone. This template creates essential resources, including an IAM role with scoped-down permissions and a trust relationship with Pinecone's AWS or GCP account.
  </Step>

  <Step title="Create environment">
    Pinecone deploys a data plane cluster within a dedicated VPC in your AWS or GCP account, and you [configure a private endpoint](#configure-a-private-endpoint) for securely connecting to your indexes via AWS PrivateLink or GCP Private Service Connect.
  </Step>

  <Step title="Validate">
    Once the environment is operational, Pinecone performs validation tests to ensure proper functionality.
  </Step>
</Steps>


## Configure a private endpoint

You use a [private endpoint](#configure-a-private-endpoint) to securely connect to your BYOC indexes. On AWS, you use the [AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html) service; on GCP, you use the [GCP Private Service Connect](https://cloud.google.com/vpc/docs/private-service-connect) service.

<Tabs>
  <Tab title="AWS">
    Follow the instructions in the AWS documentation to [create a VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html#create-interface-endpoint-aws) for connecting to your indexes via AWS PrivateLink.

    * For **Resource configurations**, select the relevant resource for your Pinecone BYOC deployment.

    * For **Network settings**, select the VPC for your BYOC deployment.

    * In **Additional settings**, select **Enable DNS name** to allow you to access your indexes using a DNS name.
  </Tab>

  <Tab title="GCP">
    <Steps>
      <Step title="Create a private endpoint">
        Follow the instructions in the GCP documentation to [create a private endpoint](https://cloud.google.com/vpc/docs/configure-private-service-connect-services#create-endpoint) for connecting to your indexes via GCP Private Service Connect.

        * Set the **Target service** to the following:

          ```
          projects/<YOUR-BYOC-PROJECT>/regions/<YOUR-BYOC-REGION>/serviceAttachments/pinecone-psc
          ```
        * Copy the IP address of the private endpoint. You'll need it later.
      </Step>

      <Step title="Create a private DNS zone">
        Follow the instructions in the GCP documentation to [create a private DNS zone](https://cloud.google.com/dns/docs/zones#create-private-zone).

        * Set the **DNS name** to the following:

          ```
          private.<YOUR-BYOC-ENVIRONMENT>.pinecone.io
          ```
        * Select the same VPC network as the private endpoint.
      </Step>

      <Step title="Add a resource record set">
        Follow the instructions in the GCP documentation to [add a resource record set](https://cloud.google.com/dns/docs/records#add-rrset).

        * Set the **DNS name** to **\***.

        * Set the **Resource record type** to **A**.

        * Set the **Ipv4 Address** to the IP address of the private endpoint.
      </Step>
    </Steps>
  </Tab>
</Tabs>


## Create an index

Once your BYOC environment is ready, you can create a BYOC index in the [Pinecone console](https://app.pinecone.io/organizations/-/projects/-/indexes) or via Pinecone API or [Python SDK](/reference/python-sdk).

To create a BYOC index, set the `spec` parameter to the environment name provided to you during onboarding, for example:

<CodeGroup>
  ```python Python {9-11} theme={null}
  from pinecone import Pinecone, ByocSpec

  pc = Pinecone(api_key="YOUR_API_KEY")

  pc.create_index(
      name="example-byoc-index", 
      dimension=1536, 
      metric="cosine", 
      spec=ByocSpec(
          environment="aws-us-east-1-b921"
      ),
      deletion_protection="disabled",
      tags={
          "example": "tag"
      }
  )
  ```

  ```shell curl {11-15} theme={null}
  curl -s "https://api.pinecone.io/indexes" \
    -H "Accept: application/json" \
    -H "Content-Type: application/json" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-API-Version: 2025-04" \
    -d '{
          "name": "example-byoc-index",
          "vector_type": "dense",
          "dimension": 1536,
          "metric": "cosine",
          "spec": {
              "byoc": {
                  "environment": "aws-us-east-1-b921"
              }
          },
          "tags": {
              "example": "tag"
          },
          "deletion_protection": "disabled"
        }'
  ```
</CodeGroup>


## Read and write data

<Note>
  BYOC does not support reading and writing data from the index browser in the [Pinecone console](https://app.pinecone.io/organizations/-/projects/-/indexes/-/browser).
</Note>

Once your private endpoint is configured, you can run data operations against an index as usual, but you must target the index using its private endpoint URL. The only difference in the URL is that `.svc.` is changed to `.svc.private.`.

You can get the private endpoint URL for an index from the Pinecone console or API.

<Tabs>
  <Tab title="Console">
    To get the private endpoint URL for an index from the Pinecone console:

    1. Open the [Pinecone console](https://app.pinecone.io/organizations/-/projects).
    2. Select the project containing the index.
    3. Select the index.
    4. Copy the URL under **PRIVATE ENDPOINT**.
  </Tab>

  <Tab title="API">
    To get the private endpoint URL for an index from the API, use the [`describe_index`](/reference/api/latest/control-plane/describe_index) operation, which returns the private endpoint URL as the `private_host` value:

    <CodeGroup>
      ```JavaScript JavaScript theme={null}
      import { Pinecone } from '@pinecone-database/pinecone';

      const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

      await pc.describeIndex('docs-example');
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

      ```bash curl theme={null}
      PINECONE_API_KEY="YOUR_API_KEY"

      curl -i -X GET "https://api.pinecone.io/indexes/docs-example" \
          -H "Api-Key: YOUR_API_KEY" \
          -H "X-Pinecone-API-Version: 2025-04"
      ```
    </CodeGroup>

    The response includes the private endpoint URL as the `private_host` value:

    <CodeGroup>
      ```json JavaScript {6} theme={null}
      {
        name: 'docs-example',
        dimension: 1536,
        metric: 'cosine',
        host: 'docs-example-jl7boae.svc.aped-4627-b74a.pinecone.io',
        privateHost: 'docs-example-jl7boae.svc.private.aped-4627-b74a.pinecone.io',
        deletionProtection: 'disabled',
        tags: { environment: 'production' },
        embed: undefined,
        spec: {
          byoc: undefined,
          pod: undefined,
          serverless: { cloud: 'aws', region: 'us-east-1' }
        },
        status: { ready: true, state: 'Ready' },
        vectorType: 'dense'
      }
      ```

      ```go Go {5} theme={null}
      index: {
        "name": "docs-example",
        "dimension": 1536,
        "host": "docs-example-jl7boae.svc.aped-4627-b74a.pinecone.io",
        "private_host": "docs-example-jl7boae.svc.private.aped-4627-b74a.pinecone.io",
        "metric": "cosine",
        "deletion_protection": "disabled",
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
          "environment": "production"
        }
      }
      ```

      ```json curl {12} theme={null}
      {
        "id": "025117b3-e683-423c-b2d1-6d30fbe5027f",
        "vector_type": "dense",
        "name": "docs-example",
        "metric": "cosine",
        "dimension": 1536,
        "status": {
          "ready": true,
          "state": "Ready"
        },
        "host": "docs-example-jl7boae.svc.aped-4627-b74a.pinecone.io",
        "private_host": "docs-example-jl7boae.svc.private.aped-4627-b74a.pinecone.io",
        "spec": {
          "serverless": {
            "region": "us-east-1",
            "cloud": "aws"
          }
        },
        "deletion_protection": "disabled",
        "tags": {
          "environment": "production"
        }
      ```
    </CodeGroup>
  </Tab>
</Tabs>

<Note>
  If you run data operations against an index from outside the Private Endpoint, you will get an `Unauthorized` response.
</Note>


## Monitoring

Pinecone engineers monitor the state of your BYOC deployment and manage incidents if they arise. In addition, you can [monitor performance metrics](/guides/production/monitoring) for your BYOC indexes in the Pinecone Console or with Prometheus or Datadog.

<Note>
  To use Prometheus, your monitoring tool must have access to your VPC.
</Note>


## Limitations

BYOC does not support the following:

* [Integrated embedding](/guides/index-data/indexing-overview#integrated-embedding), which relies on models hosted by Pinecone that are outsite of your AWS or GCP account.

* Reading and writing data from the index browser in the [Pinecone console](https://app.pinecone.io/organizations/-/projects/-/indexes/-/browser). You must use the Pinecone API or SDKs instead.

* Using [customer-managed encryption keys (CMEK)](/guides/production/configure-cmek) to secure data within a Pinecone project.

Also, to [monitor performance metrics with Prometheus](/guides/production/monitoring#monitor-with-prometheus), you must configure Prometheus within your VPC.


## FAQs

<AccordionGroup>
  <Accordion title="What is the difference between BYOC and Pinecone's standard service?">
    In the standard service, Pinecone manages all cloud resources and includes their cost in the service fee. In BYOC, customers provision and pay for cloud resources directly through their AWS or GCP account, providing greater control and data sovereignty as well as access to available AWS or GCP credits or discounts.

    Also, BYOC does not support certain features. See [Limitations](#limitations) for details.
  </Accordion>

  <Accordion title="How is data secured in BYOC?">
    Data is stored and processed exclusively within the customer's AWS or GCP account, with encryption applied at rest and in transit. Communication between the data plane and control plane is encrypted using TLS, and access is controlled via RBAC and scoped IAM permissions. AWS PrivateLink or GCP Private Service Connect is used for secure data plane API calls.
  </Accordion>

  <Accordion title="Is BYOC available in other cloud providers?">
    Currently, BYOC is available in AWS and GCP. Support for Azure is planned for future releases.
  </Accordion>
</AccordionGroup>



---
**Navigation:** [← Previous](./10-use-the-pinecone-mcp-server.md) | [Index](./index.md) | [Next →](./12-configure-audit-logs.md)
