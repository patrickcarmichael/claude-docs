**Navigation:** [← Previous](./02-check-data-freshness.md) | [Index](./index.md) | [Next →](./04-indexing-overview.md)

# Delete all chunks for a document
index.delete(
    namespace="example-namespace",
    filter={
        "document_id": {"$eq": "document1"}
    }
)
```

### Update an entire document

When the amount of chunks or ordering of chunks for a document changes, the recommended approach is to first [delete all chunks using a metadata filter](/guides/manage-data/delete-data#delete-records-by-metadata), and then [upsert](/guides/index-data/upsert-data) the new chunks:

```python Python theme={null}
from pinecone.grpc import PineconeGRPC as Pinecone

pc = Pinecone(api_key="YOUR_API_KEY")


# To get the unique host for an index, 

# see https://docs.pinecone.io/guides/manage-data/target-an-index
index = pc.Index(host="INDEX_HOST")


# Step 1: Delete all existing chunks for the document
index.delete(
    namespace="example-namespace",
    filter={
        "document_id": {"$eq": "document1"}
    }
)

print("Deleted existing chunks for document1")


# Step 2: Upsert the updated document chunks
index.upsert(
  namespace="example-namespace", 
  vectors=[
    {
      "id": "document1#chunk1",
      "values": [<updated dense vector>],
      "metadata": {
        "document_id": "document1",
        "document_title": "Introduction to Vector Databases - Updated Edition",
        "chunk_number": 1,
        "chunk_text": "Updated first chunk with new content...",
        "document_url": "https://example.com/docs/document1",
        "created_at": "2024-02-15",
        "document_type": "tutorial",
        "version": "2.0"
      }
    },
    {
      "id": "document1#chunk2",
      "values": [<updated dense vector>],
      "metadata": {
        "document_id": "document1",
        "document_title": "Introduction to Vector Databases - Updated Edition",
        "chunk_number": 2,
        "chunk_text": "Updated second chunk with new content...",
        "document_url": "https://example.com/docs/document1",
        "created_at": "2024-02-15",
        "document_type": "tutorial",
        "version": "2.0"
      }
    }
    # Add more chunks as needed for the updated document
  ]
)

print("Successfully updated document1 with new chunks")
```


## Data freshness

Pinecone is [eventually consistent](/guides/index-data/check-data-freshness), so it's possible that a write (upsert, update, or delete) followed immediately by a read (query, list, or fetch) may not return the latest version of the data. If your use case requires retrieving data immediately, consider implementing a small delay or [retry logic](/guides/production/error-handling#implement-retry-logic) after writes.



# Dedicated read nodes
Source: https://docs.pinecone.io/guides/index-data/dedicated-read-nodes

Reserve dedicated storage and compute resources for predictable query performance.

<Note>
  This feature is in [early access](/release-notes/feature-availability) and not yet available to all users. To request access, [contact support](https://app.pinecone.io/organizations/-/settings/support/ticket).
</Note>

Dedicated read nodes is a new feature that lets you reserve dedicated storage and compute resources for an index, ensuring predictable performance and cost efficiency for queries. It is ideal for workloads with **millions to billions of records** and **moderate to high query rates**.


## Key concepts

When you create an index with dedicated read nodes, Pinecone allocates dedicated storage and compute resources based on your choice of node type, number of shards, and number of replicas.

* **Dedicated storage** ensures that index data is always cached in memory and on disk for warm, low-latency queries. In contrast, for on-demand indexes, [caching is best-effort](/guides/get-started/database-architecture#query-executors); new and infrequently-accessed data may need to be fetched from object storage, resulting in cold, higher-latency queries.

* **Dedicated compute** ensures that an index always has the capacity to handle high query rates. In contrast, on-demand indexes share compute resources and are subject to [rate limits](/reference/api/database-limits#rate-limits) and throttling.

<Note>
  Dedicated read nodes affects only read performance. Write performance is the same as for on-demand indexes.
</Note>

### Node types

There are two node types: `b1` and `t1`. Both are suitable for large-scale and demanding workloads, but `t1` nodes provide increased processing power and memory. Additionally, `t1` nodes cache more data in memory, enabling lower query latency.

### Shards

Shards determine the storage capacity of an index.

Each shard provides 250 GB of storage, making it straightforward to calculate the number of shards necessary for your index size, including room for growth. For example:

| Index size | Shards | Capacity |
| :--------- | :----- | :------- |
| 100 GB     | 1      | 250 GB   |
| 500 GB     | 3      | 750 GB   |
| 1 TB       | 5      | 1.25 TB  |
| 1.6 TB     | 7      | 1.75 TB  |

When [index fullness](#index-fullness) reaches 80%, consider [adding shards](#add-or-remove-shards), especially if you expect continued growth. Adding shards accomplishes the following things:

* Relieves storage (disk) fullness. Data is spread across shards, so adding shards reduces the amount of data on each one.
* Relieves memory fullness. With less data stored on each shard, there's also less data to cache in memory.

<Warning>
  You are responsible for allocating enough shards for your index size. If your index exceeds its storage capacity, write operations (upsert, update, delete) are rejected.
</Warning>

### Replicas

Replicas multiply the compute resources and data of an index, allowing higher query throughput and availability.

* **Query throughput**: Each replica duplicates the compute resources available to the index, allowing increased parallel processing and higher queries per second.

  * In general, throughput scales linearly with the number of replicas, but performance varies based on the shape of the workload and the complexity of [metadata filters](/guides/search/filter-by-metadata).

  * To determine the right number of replicas, test your query patterns or [contact support](https://app.pinecone.io/organizations/-/settings/support/ticket).

* **High availability**: Replicas ensure your index remains available even if an availability zone experiences an outage.

  * When you add a replica, Pinecone places it in a different zone within the same region, up to a maximum of three zones. If you add more than three replicas, additional replicas are placed in zones that already have a replica. This multizone approach allows your index to continue serving queries even if one zone becomes unavailable.

  * To achieve high availability, allocate at least n+1 replicas, where n is the minimum number of replicas required to meet your throughput needs. This ensures that, even if a zone (and its replica) fails, your index still has enough capacity to handle your workload without interruption.

<Tip>
  As your query throughput and availability requirements change, you can [increase or decrease replicas](#add-or-remove-replicas). Adding or removing replicas can be done through the API and does not require downtime, but it can take up to 30 minutes.
</Tip>

### Index fullness

Dedicated read nodes store a search index in memory and record data on disk.

There are three measures of [index fullness](#check-index-fullness):

* `memory_fullness`: How much of the index's memory capacity is currently in use (0 to 1).
* `storage_fullness`: How much of the index's storage capacity is currently in use (0 to 1).
* `indexFullness`: The greater of `memory_fullness` and `storage_fullness`.

In most cases, `storage_fullness` is the limiting factor. However, memory can fill up first in the following scenarios:

* `b1` nodes, a large namespace (hundreds of millions of records), low-dimension vectors (128 or 256 dimensions), and minimal metadata.
* `t1` nodes, high-dimension vectors (1024 or 1536 dimensions), and lots of metadata.

When [index fullness](#index-fullness) reaches 80%, consider [adding shards](#add-or-remove-shards), especially if you expect continued growth. Adding shards accomplishes the following things:

* Relieves storage (disk) fullness. Data is spread across shards, so adding shards reduces the amount of data on each one.
* Relieves memory fullness. With less data stored on each shard, there's also less data to cache in memory.

<Warning>
  You're responsible for allocating enough shards to accommodate your index size. If your index exceeds its storage capacity, write operations (upsert, update, delete) are rejected.
</Warning>


## Using dedicated read nodes

<Note>
  This feature is in [early access](/release-notes/feature-availability) and is not yet available to all users. To request access, [contact support](https://app.pinecone.io/organizations/-/settings/support/ticket).
</Note>

The following sections describe how to create and manage an index deployed on dedicated read nodes, using version `2025-10` of the Pinecone API.

### Calculate the size of your index

To decide how many [shards](#shards) to allocate for your index, calculate the total index size and then add some room for growth. Each shard provides 250 GB of storage.

To calculate the total size of an index, find the aggregate size of all its records. The size of an individual record is the sum of the following components:

* ID size (in bytes)

* Dense vector size (4 bytes \* dense dimensions)

* Sparse vector size (9 bytes \* number of non-zero sparse value)

  <Tip>
    To estimate the sparse vector component of your index size, multiply 9 bytes by the average number of non-zero values per vector.
  </Tip>

* Total metadata size (total size of all metadata fields, in bytes)

Allocate enough shards to accommodate the total size of your index, plus some room for growth. For more details, see [shards](#shards).

### Create an index

To create a dedicated index, call [create an index](https://docs.pinecone.io/reference/api/2025-10/control-plane/create_index).

In the `spec.serverless.read_capacity` object:

* Set `mode` to `Dedicated`.
* Set `dedicated.node_type` to either `b1` or `t1`, depending on the [node type](#node-types) you want to use.
* Set `dedicated.scaling` to `Manual` (currently, `Manual` is the only option, and it must be included in the request).
* Set `dedicated.manual.shards` to the number of [shards](#shards) required to accommodate at least the current size of your index, with a minimum of 1 shard. Each shard provides 250 GB of storage.
* Set `dedicated.manual.replicas` to the number of [replicas](#replicas) for the index, with a minimum of 0 replicas (an index with 0 replicas is [paused](#pause-a-dedicated-index)).

<Note>
  To determine the number of shards required by your index, see [calculate the size of your index](#calculate-the-size-of-your-index).
</Note>

Example request:

<CodeGroup>
  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl "https://api.pinecone.io/indexes" \
    -H "Accept: application/json" \
    -H "Content-Type: application/json" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-API-Version: 2025-10" \
    -d '{
  		"name": "example-dedicated-index",
  		"dimension": 1536,
  		"metric": "cosine",
  		"deletion_protection": "enabled",
  		"tags": {
  			"tag0": "value0"
  		},
  		"vector_type": "dense",
  		"spec": {
  			"serverless": {
  				"cloud": "aws",
  				"region": "us-east-1",
  				"read_capacity": {
  					"mode": "Dedicated",
  					"dedicated": {
  						"node_type": "b1",
  						"scaling": "Manual",
  						"manual": {
  							"shards": 2,
  							"replicas": 1
  						}
  					}
  				}
  			}
  		}
  	}'
  ```
</CodeGroup>

Example response:

<CodeGroup>
  ```json curl theme={null}
  {
  	"name": "example-dedicated-index",
  	"vector_type": "dense",
  	"metric": "cosine",
  	"dimension": 1536,
  	"status": {
  		"ready": false,
  		"state": "Initializing"
  	},
  	"host": "example-dedicated-index-bhnyigt.svc.aped-4627-b74a.pinecone.io",
  	"spec": {
  		"serverless": {
  			"region": "us-east-1",
  			"cloud": "aws",
  			"read_capacity": {
  				"mode": "Dedicated",
  				"dedicated": {
  					"node_type": "b1",
  					"scaling": "Manual",
  					"manual": {
  						"shards": 2,
  						"replicas": 1
  					}
  				},
  				"status": {
  					"state": "Migrating",
  					"current_shards": null,
  					"current_replicas": null
  				}
  			}
  		}
  	},
  	"deletion_protection": "enabled",
  	"tags": {
  		"tag0": "value0"
  	}
  }
  ```
</CodeGroup>

### Add a hosted embedding model (optional)

If you'd like Pinecone to host the model that generates embeddings for your data, so that you use Pinecone's API to insert and search by text (rather than vectors generated by an external model), configure your index to use a [hosted embedding model](/guides/index-data/create-an-index#embedding-models). To do this, call [configure an index](/reference/api/2025-10/control-plane/configure_index), and specify the `embed` object in the request body.

Example request:

<Note>
  Remember:

  * Replace `chunk_test` with the name of the field in your data that contains the text to be embedded.
  * Be sure to use a model whose dimension requirements match the dimensions of your index.
</Note>

<CodeGroup>
  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_NAME="YOUR_INDEX_NAME"

  curl -s -X PATCH "https://api.pinecone.io/indexes/$INDEX_NAME" \
      -H "Content-Type: application/json" \
      -H "Api-Key: $PINECONE_API_KEY" \
      -H "X-Pinecone-API-Version: 2025-10" \
      -d '{
              "embed": {
                  "field_map": { "text": "chunk_test" },
                  "model": "llama-text-embed-v2",
                  "read_parameters": { "input_type": "query", "truncate": "NONE" },
                  "write_parameters": { "input_type": "passage" }
              }
          }' 
  ```
</CodeGroup>

Example response:

<CodeGroup>
  ```json curl theme={null}
  {
    "name": "example-dedicated-index-1024",
    "vector_type": "dense",
    "metric": "cosine",
    "dimension": 1024,
    "status": {
      "ready": true,
      "state": "Ready"
    },
    "host": "example-dedicated-index-1024-bhnyigt.svc.aped-4627-b74a.pinecone.io",
    "spec": {
      "serverless": {
        "region": "us-east-1",
        "cloud": "aws",
        "read_capacity": {
          "mode": "Dedicated",
          "dedicated": {
            "node_type": "b1",
            "scaling": "Manual",
            "manual": {
              "shards": 1,
              "replicas": 1
            }
          },
          "status": {
            "state": "Migrating",
            "current_shards": null,
            "current_replicas": null
          }
        }
      }
    },
    "deletion_protection": "enabled",
    "tags": {
      "tag0": "value0"
    },
    "embed": {
      "model": "llama-text-embed-v2",
      "field_map": {
        "text": "dataField"
      },
      "dimension": 1024,
      "metric": "cosine",
      "write_parameters": {
        "dimension": 1024,
        "input_type": "passage",
        "truncate": "END"
      },
      "read_parameters": {
        "dimension": 1024,
        "input_type": "query",
        "truncate": "NONE"
      },
      "vector_type": "dense"
    }
  }
  ```
</CodeGroup>

<Note>
  It's also possible to specify a hosted embedding model when creating a dedicated read nodes index. To do this, call [create an index with integrated embedding](/reference/api/2025-10/control-plane/create_for_model). In the request body, use the `read_capacity` object to configure node type, shards, and replicas.
</Note>

### Check index fullness

To check [index fullness](#index-fullness), call [get index stats](/reference/api/2025-10/data-plane/describeindexstats).

Example request:

<CodeGroup>
  ```bash curl theme={null}
  # To get the unique host for an index,
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="YOUR_INDEX_HOST"

  curl -X POST "https://$INDEX_HOST/describe_index_stats" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-API-Version: 2025-10"
  ```
</CodeGroup>

Example response:

<CodeGroup>
  ```json curl theme={null}
  {
    "namespaces": {
      "example-namespace": {
        "vectorCount": 10282
      }
    },
    "indexFullness": 0.2,
    "memory_fullness": 0.1,
    "storage_fullness": 0.2,
    "totalVectorCount": 7516163,
    "dimension": 1536,
    "metric": "cosine",
    "vectorType": "dense"
  }
  ```
</CodeGroup>

In the response, `indexFullness` describes how full the index is, on a scale of 0 to 1. It's set to the greater of `memory_fullness` and `storage_fullness`.

### Add or remove shards

To add or remove [shards](#shards), [contact support](https://app.pinecone.io/organizations/-/settings/support/ticket). This cannot be done with the API.

### Add or remove replicas

<Note>
  You can add or remove replicas no more than once per hour, starting one hour after index creation. Each change can take up to 30 minutes to complete.
</Note>

Adding or removing [replicas](#replicas) can be done through the API and does not require downtime, but it can take up to 30 minutes. To do this, call [configure an index](/reference/api/2025-10/control-plane/configure_index). In the request body, set `spec.serverless.read_capacity.dedicated.manual.replicas` to the desired number of replicas.

Example request:

<CodeGroup>
  ```bash curl  theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl -X PATCH "https://api.pinecone.io/indexes/example-dedicated-index" \
    -H "Accept: application/json" \
    -H "Content-Type: application/json" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-API-Version: 2025-10" \
    -d '{
          "spec": {
            "serverless": {
              "read_capacity": {
                "dedicated": {
                  "manual": {
                    "replicas": 2
                  }
                }
              }
            }
          }
        }'
  ```
</CodeGroup>

Example response:

<CodeGroup>
  ```json curl highlight={22,28} theme={null}
  {
    "name": "example-dedicated-index",
    "vector_type": "dense",
    "metric": "cosine",
    "dimension": 1536,
    "status": {
      "ready": true,
      "state": "Ready"
    },
    "host": "example-dedicated-index-bhnyigt.svc.aped-4627-b74a.pinecone.io",
    "spec": {
      "serverless": {
        "region": "us-east-1",
        "cloud": "aws",
        "read_capacity": {
          "mode": "Dedicated",
          "dedicated": {
            "node_type": "b1",
            "scaling": "Manual",
            "manual": {
              "shards": 1,
              "replicas": 2 <-- desired state
            }
          },
          "status": {
            "state": "Scaling",
            "current_shards": 1,
            "current_replicas": 1 <-- current state
          }
        }
      }
    },
    "deletion_protection": "enabled",
    "tags": {
      "tag0": "value0"
    }
  }
  ```
</CodeGroup>

### Pause a dedicated index

To pause an index, [set the number of replicas](#add-or-remove-replicas) to 0. This change should take less than a minute to complete, after which the index blocks all writes and reads.

<Note>
  While an index is [paused](#pause-a-dedicated-index), you cannot write to it or read from it.
</Note>

### Change node types

To change the [type of node](#node-types) used for a dedicated index, [contact support](https://app.pinecone.io/organizations/-/settings/support/ticket). This cannot be done with the API.

### Migrate from on-demand to dedicated

<Note>
  You can change the <Tooltip tip="Dedicated or OnDemand">mode</Tooltip> of your index no more than once every 24 hours. The change can take up to 30 mins to complete.
</Note>

To change an on-demand index to dedicated, do the following:

1. Determine the [current size of your index](#calculate-the-size-of-your-index).

2. Call [configure an index](/reference/api/2025-10/control-plane/configure_index).

   In the request body, in the `spec.serverless.read_capacity` object, set the following fields:

   * Set `mode` to `Dedicated`.
   * Set `node_type` to the [node type](#node-types) you want to use (`b1` or `t1`).
   * Set `shards` to the number of [shards](#shards) required for your index. Each shard provides 250 GB of storage.
   * Set `replicas` to the number of [replicas](#replicas) required for your query throughput needs.

   For example, this example migrates an index named `index-to-migrate` to a dedicated index with `b1` nodes, 1 shard, and 1 replica:

   <CodeGroup>
     ```bash curl theme={null}
     curl -X PATCH "https://api.pinecone.io/indexes/index-to-migrate" \
       -H "Accept: application/json" \
       -H "Content-Type: application/json" \
       -H "Api-Key: $PINECONE_API_KEY" \
       -H "X-Pinecone-API-Version: 2025-10" \
       -d '{
             "spec": {
               "serverless": {
                 "read_capacity": {
                   "mode": "Dedicated",
                   "dedicated": {
                     "node_type": "b1",
                     "scaling": "Manual",
                     "manual": {
                       "shards": 1,
                       "replicas": 1
                     }
                   }
                 }
               }
             }
           }'
     ```
   </CodeGroup>

   Response:

   <CodeGroup>
     ```bash curl theme={null}
     {
       "name": "index-to-migrate",
       "vector_type": "dense",
       "metric": "cosine",
       "dimension": 1536,
       "status": {
         "ready": true,
         "state": "Ready"
       },
       "host": "index-to-migrate-bhnyigt.svc.aped-4627-b74a.pinecone.io",
       "spec": {
         "serverless": {
           "region": "us-east-1",
           "cloud": "aws",
           "read_capacity": {
             "mode": "Dedicated",
             "dedicated": {
               "node_type": "b1",
               "scaling": "Manual",
               "manual": {
                 "shards": 1,
                 "replicas": 1
               }
             },
             "status": {
               "state": "Migrating",
               "current_shards": null,
               "current_replicas": null
             }
           }
         }
       },
       "deletion_protection": "disabled",
       "tags": null
     }
     ```
   </CodeGroup>

3. [Monitor the status of the migration](#check-the-status-of-a-change).

   When the migration is complete, the value of [`spec.serverless.read_capacity.status.state`](/reference/api/2025-10/control-plane/describe_index#response-spec-serverless-read-capacity-status-state) is `Ready`.

   An `Error` state means that you didn't allocate enough shards for the size of your index. Migrate to dedicated again, using a sufficient number of shards.

### Migrate from dedicated to on-demand

To change a dedicated index to on-demand, contact [contact support](https://app.pinecone.io/organizations/-/settings/support/ticket). This can't be done with the API.

### Check the status of a change

After changing a dedicated index, check the status of the change by calling [describe an index](/reference/api/2025-10/control-plane/describe_index):

Example request:

<CodeGroup>
  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl "https://api.pinecone.io/indexes/example-dedicated-index" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-API-Version: 2025-10" 
  ```
</CodeGroup>

Example response, for an index that is scaling from 1 to 2 replicas:

<CodeGroup>
  ```json curl theme={null}
  {
    "name": "example-dedicated-index",
    "vector_type": "dense",
    "metric": "cosine",
    "dimension": 1536,
    "status": {
      "ready": true,
      "state": "Ready"
    },
    "host": "example-dedicated-index-bhnyigt.svc.aped-4627-b74a.pinecone.io",
    "spec": {
      "serverless": {
        "region": "us-east-1",
        "cloud": "aws",
        "read_capacity": {
          "mode": "Dedicated",
          "dedicated": {
            "node_type": "b1",
            "scaling": "Manual",
            "manual": {
              "shards": 1,
              "replicas": 2
            }
          },
          "status": {
            "state": "Scaling",
            "current_shards": 1,
            "current_replicas": 1
          }
        }
      }
    },
    "deletion_protection": "enabled",
    "tags": {
      "tag0": "value0"
    }
  }
  ```
</CodeGroup>

The status of a change is communicated by the `spec.serverless.read_capacity.status.state` field. Possible values include:

* `Ready`: The dedicated index is ready to serve queries.
* `Scaling`: A change to the node type, number of shards, or number of replicas is in progress.
* `Migrating`: A change to the <Tooltip tip="Dedicated or OnDemand">mode</Tooltip> is in progress.
* `Error`: You did not allocate enough shards for the size of your index. Migrate to dedicated again, using a sufficient number of shards.


## Limits

### Read limits

On dedicated indexes, read operations (query, list, fetch) have no [rate limits](/reference/api/database-limits#rate-limits). However, if your query rate exceeds the compute capacity of your index, you may observe decreased query throughput. In such cases, consider [adding replicas](#add-or-remove-replicas) to increase the compute resources of the index.

### Write limits

* On dedicated indexes, write operations (upsert, update, delete) have the same [rate limits](/reference/api/database-limits#rate-limits) as on-demand indexes.
* Writes that would cause your index to exceed its storage capacity are rejected. In such cases, consider [adding shards](#add-or-remove-shards) to increase available storage. To determine how close to the limit you are,  [check index fullness](#check-index-fullness).

### Operational limits

| Metric                                                                                  | Limit          |
| :-------------------------------------------------------------------------------------- | :------------- |
| Min shards per index                                                                    | 1              |
| Max namespaces per index                                                                | 1              |
| [Node type](#node-types) or <Tooltip tip="Dedicated or OnDemand">mode</Tooltip> changes | 1 per 24 hours |
| Max shard or replica changes                                                            | 1 per hour     |

### Other limits

* To increase or decrease shards, [contact support](https://app.pinecone.io/organizations/-/settings/support/ticket).
* To change node types, [contact support](https://app.pinecone.io/organizations/-/settings/support/ticket).
* Dedicated indexes do not support backups or bulk imports.
* `memory_fullness` is an approximation and doesn't yet account for metadata.


## Cost

The cost of an index that uses dedicated read nodes is calculated by this formula:

`(Dedicated read nodes costs)` + `(storage costs)` + `(write costs)`

* `(Dedicated read nodes costs)` are calculated as:

  ```
  (Node type monthly rate) * (number of shards) * (number of replicas)
  ```

  <Note>
    Node type rates vary based on [pricing plan](https://www.pinecone.io/pricing/) and cloud region. For exact rates, [contact Pinecone](https://www.pinecone.io/contact/).
  </Note>

* `(Storage costs)` are the [same as for on-demand indexes](/guides/manage-cost/understanding-cost#storage).

* `(Write costs)` are the [same as for on-demand indexes](/guides/manage-cost/understanding-cost#write-units).

Additionally, if you use a [hosted model](/guides/index-data/create-an-index#embedding-models) for search or reranking, there are additional costs for the model usage. See [inference pricing](https://www.pinecone.io/pricing/?plans=inference\&scrollTo=product-pricing-modal-section) for details.

### Example cost calculations

<AccordionGroup>
  <Accordion title="b1 nodes, 2 shards, 2 replicas - Standard plan">
    If the Standard plan rate for `b1` nodes is \$548.96/month, the cost of dedicated read nodes would be as follows:

    ```
    548.96 * 2 * 2 = $2,195.84/month, plus storage and write costs
    ```
  </Accordion>

  <Accordion title="t1 nodes, 2 shards, 2 replicas - Standard plan">
    If the Standard plan rate for `t1` nodes is \$1,758.53/month, the cost of dedicated read nodes would be as follows:

    ```
    1758.53 * 2 * 2 = $7,034.12/month, plus storage and write costs
    ```
  </Accordion>
</AccordionGroup>



# Implement multitenancy
Source: https://docs.pinecone.io/guides/index-data/implement-multitenancy

Use namespaces to isolate tenant data securely.

[Multitenancy](https://en.wikipedia.org/wiki/Multitenancy) is a software architecture where a single instance of a system serves multiple customers, or tenants, while ensuring data isolation between them for privacy and security.

This page shows you how to implement multitenancy in Pinecone using a **serverless index with one namespace per tenant**.

<Note>
  While the Standard and Enterprise plans support up to [100,000 namespaces per index](/reference/api/database-limits#namespaces-per-serverless-index), Pinecone can accommodate million-scale namespaces and beyond for specific use cases. If your application requires more than 100,000 namespaces, [contact Support](https://app.pinecone.io/organizations/-/settings/support/ticket).
</Note>


## How it works

<img className="block max-w-full dark:hidden" noZoom src="https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/multitenant-saas-namepsaces.png?fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=8a85b3a90f4c64964ac2d19b72c9e537" data-og-width="1400" width="1400" data-og-height="880" height="880" data-path="images/multitenant-saas-namepsaces.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/multitenant-saas-namepsaces.png?w=280&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=ecf6f1c273f4802044152a03c2e9990f 280w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/multitenant-saas-namepsaces.png?w=560&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=2636f6f7b3b635bea0c4e7b7c82d6555 560w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/multitenant-saas-namepsaces.png?w=840&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=04e9f5f77a2c242055638347b2949138 840w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/multitenant-saas-namepsaces.png?w=1100&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=719792f97af9dbcba9cbc4030bcf8ae3 1100w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/multitenant-saas-namepsaces.png?w=1650&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=6577382ddaebdc1d1dd2b0ed5849b042 1650w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/multitenant-saas-namepsaces.png?w=2500&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=ff6a56b6d70a48b5f8646f5fb0c75598 2500w" />

<img className="hidden max-w-full dark:block" noZoom src="https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/multitenant-saas-namespaces-dark.png?fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=46f954e9010597b5303aee2984be1e29" data-og-width="1400" width="1400" data-og-height="880" height="880" data-path="images/multitenant-saas-namespaces-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/multitenant-saas-namespaces-dark.png?w=280&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=44cc681389721a2730e2cb0ece7c8bfb 280w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/multitenant-saas-namespaces-dark.png?w=560&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=3ee30fd16eb0d1c99cf4cf26864ed5b3 560w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/multitenant-saas-namespaces-dark.png?w=840&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=b3390cd3c7c51b37934bf94c0927d0ee 840w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/multitenant-saas-namespaces-dark.png?w=1100&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=1621cef8d384c50572c16c206b92e821 1100w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/multitenant-saas-namespaces-dark.png?w=1650&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=5e9e90a83acc40ceab104caa1493f61b 1650w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/multitenant-saas-namespaces-dark.png?w=2500&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=908341daa70cac819162457eb2615763 2500w" />

In Pinecone, an [index](/guides/index-data/indexing-overview) is the highest-level organizational unit of data, where you define the dimension of vectors to be stored in the index and the measure of similarity to be used when querying the index.

Within an index, records are stored in [namespaces](/guides/index-data/indexing-overview#namespaces), and all [upserts](/guides/index-data/upsert-data), [queries](/guides/search/search-overview), and other [data plane operations](/reference/api/latest/data-plane) always target one namespace.

This structure makes it easy to implement multitenancy. For example, for an AI-powered SaaS application where you need to isolate the data of each customer, you would assign each customer to a namespace and target their writes and queries to that namespace (diagram above).

In cases where you have different workload patterns (e.g., RAG and semantic search), you would use a different index for each workload, with one namespace per customer in each index:

<img className="block max-w-full dark:hidden" noZoom src="https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/multitenant-saas-indexes.png?fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=d30f68fcbf1b6e259850350461f10e3c" data-og-width="1560" width="1560" data-og-height="1200" height="1200" data-path="images/multitenant-saas-indexes.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/multitenant-saas-indexes.png?w=280&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=ff79239d5622f8c8430a71d5a64abee8 280w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/multitenant-saas-indexes.png?w=560&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=9e76456ea4ff54d9333b1e330f6622e2 560w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/multitenant-saas-indexes.png?w=840&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=a99629c4e37af33b8c7fe93201cc5075 840w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/multitenant-saas-indexes.png?w=1100&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=5674100409641614c0a2a23d99fe4ce2 1100w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/multitenant-saas-indexes.png?w=1650&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=898ceabfffd1c5d18b3759151aac9276 1650w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/multitenant-saas-indexes.png?w=2500&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=1b5f238711bd3e42f9a19c29e6f096ce 2500w" />

<img className="hidden max-w-full dark:block" noZoom src="https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/multitenant-saas-indexes-dark.png?fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=1c64b2977ebdf57a2bbc8274b91e399e" data-og-width="1560" width="1560" data-og-height="1200" height="1200" data-path="images/multitenant-saas-indexes-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/multitenant-saas-indexes-dark.png?w=280&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=3e38602271765a6cb8e98108b1f0decb 280w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/multitenant-saas-indexes-dark.png?w=560&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=6d6b3925edd6dd5ea1ab0bb3246699d6 560w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/multitenant-saas-indexes-dark.png?w=840&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=93166d83515098bde4f88aa0748feb3f 840w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/multitenant-saas-indexes-dark.png?w=1100&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=7b5a0d541d8b132bd4f7290886dd2372 1100w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/multitenant-saas-indexes-dark.png?w=1650&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=fe477a1edbd28071b43363656d02745f 1650w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/multitenant-saas-indexes-dark.png?w=2500&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=3c49967484298ee8e0675ef7a620eb5b 2500w" />

<Accordion title="Understand the benefits">
  * **Tenant isolation:** In the [serverless architecture](/guides/get-started/database-architecture), each namespace is stored separately, so using namespaces provides physical isolation of data between tenants/customers.

  * **No noisy neighbors:** Reads and writes always target a single namespace, so the behavior of one tenant/customer does not affect other tenants/customers.

  * **No maintenance effort:** Serverless indexes scale automatically based on usage; you don't configure or manage any compute or storage resources.

  * **Cost efficiency:** With serverless indexes, you pay only for the amount of data stored and operations performed. For queries in particular, the cost is partly based on the total number of records that must be scanned, so using namespaces can significantly reduce query costs.

  * **Simple tenant offboarding:** To offboard a tenant/customer, you just [delete the relevant namespace](/guides/manage-data/delete-data#delete-all-records-from-a-namespace). This is a lightweight and almost instant operation.
</Accordion>


## 1. Create a serverless index

Based on a [breakthrough architecture](/guides/get-started/database-architecture), serverless indexes scale automatically based on usage, and you pay only for the amount of data stored and operations performed. Combined with the isolation of tenant data using namespaces (next step), serverless indexes are ideal for multitenant use cases.

To [create a serverless index](/guides/index-data/create-an-index#create-a-serverless-index), use the `spec` parameter to define the cloud and region where the index should be deployed. For Python, you also need to import the `ServerlessSpec` class.

<CodeGroup>
  ```Python Python theme={null}
  from pinecone.grpc import PineconeGRPC as Pinecone
  from pinecone import ServerlessSpec

  pc = Pinecone(api_key="YOUR_API_KEY")

  pc.create_index(
    name="multitenant-app",
    dimension=8,
    metric="cosine",
    spec=ServerlessSpec(
      cloud="aws",
      region="us-east-1"
    )
  )
  ```

  ```JavaScript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({
    apiKey: 'YOUR_API_KEY'
  });

  await pc.createIndex({
    name: 'multitenant-app',
    dimension: 8,
    metric: 'cosine',
    spec: {
      serverless: {
        cloud: 'aws',
        region: 'us-east-1'
      }
    }
  });
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Pinecone;

  public class CreateServerlessIndexExample {
      public static void main(String[] args) {
          Pinecone pc = new Pinecone.Builder("YOUR_API_KEY").build();
          pc.createServerlessIndex("multitenant-app", "cosine", 8, "aws", "us-east-1");
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

      // Serverless index
      indexName := "multi-tenant-app"
      vectorType := "dense"
      dimension := int32(8)
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

  ```csharp C# theme={null}
  using Pinecone;

  var pinecone = new PineconeClient("YOUR_API_KEY");

  var createIndexRequest = await pinecone.CreateIndexAsync(new CreateIndexRequest
  {
      Name = "multitenant-app",
      Dimension = 8,
      Metric = MetricType.Cosine,
      Spec = new ServerlessIndexSpec
      {
          Serverless = new ServerlessSpec
          {
              Cloud = ServerlessSpecCloud.Aws,
              Region = "us-east-1",
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
           "name": "multitenant-app",
           "dimension": 8,
           "metric": "cosine",
           "spec": {
              "serverless": {
                 "cloud": "aws",
                 "region": "us-east-1"
              }
           }
        }'
  ```
</CodeGroup>


## 2. Isolate tenant data

In a multitenant solution, you need to isolate data between tenants. To achieve this in Pinecone, use one namespace per tenant. In the [serverless architecture](/guides/get-started/database-architecture), each namespace is stored separately, so this approach ensures physical isolation of each tenant's data.

To [create a namespace for a tenant](/guides/index-data/indexing-overview#namespaces#creating-a-namespace), specify the `namespace` parameter when first [upserting](/guides/index-data/upsert-data) the tenant's records. For example, the following code upserts records for `tenant1` and `tenant2` into the `multitenant-app` index:

<CodeGroup>
  ```Python Python theme={null}
  from pinecone.grpc import PineconeGRPC as Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")
  index = pc.Index("multitenant-app")

  index.upsert(
    vectors=[
      {"id": "A", "values": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]},
      {"id": "B", "values": [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]},
      {"id": "C", "values": [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3]},
      {"id": "D", "values": [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4]}
    ],
    namespace="tenant1"
  )

  index.upsert(
    vectors=[
      {"id": "E", "values": [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]},
      {"id": "F", "values": [0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6]},
      {"id": "G", "values": [0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7]},
      {"id": "H", "values": [0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8]}
    ],
    namespace="tenant2"
  )
  ```

  ```JavaScript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({ apiKey: "YOUR_API_KEY" });
  const index = pc.index("multitenant-app");

  await index.namespace("tenant1").upsert([
    {
      "id": "A", 
      "values": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
    },
    {
      "id": "B", 
      "values": [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]
    },
    {
      "id": "C", 
      "values": [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3]
    },
    {
      "id": "D", 
      "values": [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4]
    }
  ]);

  await index.namespace("tenant2").upsert([
    {
      "id": "E", 
      "values": [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]
    },
    {
      "id": "F", 
      "values": [0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6]
    },
    {
      "id": "G", 
      "values": [0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7]
    },
    {
      "id": "H", 
      "values": [0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8]
    }
  ]);
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Index;
  import io.pinecone.clients.Pinecone;

  import java.util.Arrays;
  import java.util.List;

  public class UpsertExample {
      public static void main(String[] args) {
          Pinecone pc = new Pinecone.Builder("YOUR_API_KEY").build();
          String indexName = "multitenant-app";
          Index index = pc.getIndexConnection(indexName);
          List<Float> values1 = Arrays.asList(0.1f, 0.1f, 0.1f, 0.1f, 0.1f, 0.1f, 0.1f, 0.1f);
          List<Float> values2 = Arrays.asList(0.2f, 0.2f, 0.2f, 0.2f, 0.2f, 0.2f, 0.2f, 0.2f);
          List<Float> values3 = Arrays.asList(0.3f, 0.3f, 0.3f, 0.3f, 0.3f, 0.3f, 0.3f, 0.3f);
          List<Float> values4 = Arrays.asList(0.4f, 0.4f, 0.4f, 0.4f, 0.4f, 0.4f, 0.4f, 0.4f);
          List<Float> values5 = Arrays.asList(0.5f, 0.5f, 0.5f, 0.5f, 0.5f, 0.5f, 0.5f, 0.5f);
          List<Float> values6 = Arrays.asList(0.6f, 0.6f, 0.6f, 0.6f, 0.6f, 0.6f, 0.6f, 0.6f);
          List<Float> values7 = Arrays.asList(0.7f, 0.7f, 0.7f, 0.7f, 0.7f, 0.7f, 0.7f, 0.7f);
          List<Float> values8 = Arrays.asList(0.8f, 0.8f, 0.8f, 0.8f, 0.8f, 0.8f, 0.8f, 0.8f);

          index.upsert("A", values1, "tenant1");
          index.upsert("B", values2, "tenant1");
          index.upsert("C", values3, "tenant1");
          index.upsert("D", values4, "tenant1");
          index.upsert("E", values5, "tenant2");
          index.upsert("F", values6, "tenant2");
          index.upsert("G", values7, "tenant2");
          index.upsert("H", values8, "tenant2");
      }
  }
  ```

  ```go Go theme={null}
  // Add to the main function:
  idx, err := pc.DescribeIndex(ctx, indexName)
  if err != nil {
      log.Fatalf("Failed to describe index \"%v\": %v", idx.Name, err)
  }

  idxConnection1, err := pc.Index(pinecone.NewIndexConnParams{Host: idx.Host, Namespace: "tenant1"})
  if err != nil {
      log.Fatalf("Failed to create IndexConnection1 for Host %v: %v", idx.Host, err)
  }

  // This reuses the gRPC connection of idxConnection1 while targeting a different namespace
  idxConnection2 := idxConnection1.WithNamespace("tenant2")

  vectors1 := []*pinecone.Vector{
      {
          Id:     "A",
          Values: []float32{0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1},
      },
      {
          Id:     "B",
          Values: []float32{0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2},
      },
      {
          Id:     "C",
          Values: []float32{0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3},
      },   
      {
          Id:     "D",
          Values: []float32{0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4},
      },   
  }

  vectors2 := []*pinecone.Vector{
      {
          Id:     "E",
          Values: []float32{0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5},
      },
      {
          Id:     "F",
          Values: []float32{0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6},
      },
      {
          Id:     "G",
          Values: []float32{0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7},
      },   
      {
          Id:     "H",
          Values: []float32{0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8},
      },   
  }

  count1, err := idxConnection1.UpsertVectors(ctx, vectors1)
  if err != nil {
      log.Fatalf("Failed to upsert vectors: %v", err)
  } else {
      fmt.Printf("Successfully upserted %d vector(s)!\n", count1)
  }

  count2, err := idxConnection2.UpsertVectors(ctx, vectors2)
  if err != nil {
      log.Fatalf("Failed to upsert vectors: %v", err)
  } else {
      fmt.Printf("Successfully upserted %d vector(s)!\n", count2)
  }
  ```

  ```csharp C# theme={null}
  using Pinecone;

  var pinecone = new PineconeClient("YOUR_API_KEY");

  var index = pinecone.Index("multitenant-app");

  var upsertResponse1 = await index.UpsertAsync(new UpsertRequest {
      Vectors = new[]
      {
          new Vector
          {
              Id = "A",
              Values = new[] { 0.1f, 0.1f, 0.1f, 0.1f, 0.1f, 0.1f, 0.1f, 0.1f },
          },
          new Vector
          {
              Id = "B",
              Values = new[] { 0.2f, 0.2f, 0.2f, 0.2f, 0.2f, 0.2f, 0.2f, 0.2f },
          },
          new Vector
          {
              Id = "C",
              Values = new[] { 0.3f, 0.3f, 0.3f, 0.3f, 0.3f, 0.3f, 0.3f, 0.3f },
          },
          new Vector
          {
              Id = "D",
              Values = new[] { 0.4f, 0.4f, 0.4f, 0.4f, 0.4f, 0.4f, 0.4f, 0.4f },
          }
      },
      Namespace = "tenant1",
  });

  var upsertResponse2 = await index.UpsertAsync(new UpsertRequest {
      Vectors = new[]
      {
          new Vector
          {
              Id = "E",
              Values = new[] { 0.5f, 0.5f, 0.5f, 0.5f, 0.5f, 0.5f, 0.5f, 0.5f },
          },
          new Vector
          {
              Id = "F",
              Values = new[] { 0.6f, 0.6f, 0.6f, 0.6f, 0.6f, 0.6f, 0.6f, 0.6f },
          },
          new Vector
          {
              Id = "G",
              Values = new[] { 0.7f, 0.7f, 0.7f, 0.7f, 0.7f, 0.7f, 0.7f, 0.7f },
          },
          new Vector
          {
              Id = "H",
              Values = new[] { 0.8f, 0.8f, 0.8f, 0.8f, 0.8f, 0.8f, 0.8f, 0.8f },
          }
      },
      Namespace = "tenant2",
  });
  ```

  ```bash curl theme={null}
  # The `POST` requests below uses the unique endpoint for an index.
  # See https://docs.pinecone.io/guides/manage-data/target-an-index for details.
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="INDEX_HOST"

  curl "https://$INDEX_HOST/vectors/upsert" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H 'Content-Type: application/json' \
    -H "X-Pinecone-API-Version: 2025-04" \
    -d '{
      "vectors": [
        {
          "id": "A", 
          "values": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
        },
        {
          "id": "B", 
          "values": [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]
        },
        {
          "id": "C", 
          "values": [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3]
        },
        {
          "id": "D", 
          "values": [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4]
        }
      ],
      "namespace": "tenant1"
    }'

  curl "https://$INDEX_HOST/vectors/upsert" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H 'Content-Type: application/json' \
    -H "X-Pinecone-API-Version: 2025-04" \
    -d '{
      "vectors": [
        {
          "id": "E", 
          "values": [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]
        },
        {
          "id": "F", 
          "values": [0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6]
        },
        {
          "id": "G", 
          "values": [0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7]
        },
        {
          "id": "H", 
          "values": [0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8]
        }
      ],
      "namespace": "tenant2"
    }'
  ```
</CodeGroup>

When upserting additional records for a tenant, or when [updating](/guides/manage-data/update-data) or [deleting](/guides/manage-data/delete-data) records for a tenant, specify the tenant's `namespace`. For example, the following code updates the dense vector value of record `A` in `tenant1`:

<CodeGroup>
  ```Python Python theme={null}
  from pinecone.grpc import PineconeGRPC as Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")
  index = pc.Index("multitenant-app")

  index.update(id="A", values=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8], namespace="tenant1")
  ```

  ```JavaScript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({ apiKey: "YOUR_API_KEY" });
  const index = pc.index("multitenant-app");

  await index.namespace('tenant1').update({
   	id: 'A',
   	values: [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]
  });
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Index;
  import io.pinecone.clients.Pinecone;
  import io.pinecone.proto.UpdateResponse;

  import java.util.Arrays;
  import java.util.List;

  public class UpdateExample {
      public static void main(String[] args) {
          Pinecone pc = new Pinecone.Builder("YOUR_API_KEY").build();
          Index index = pc.getIndexConnection("multitenant-app");
          List<Float> values = Arrays.asList(0.1f, 0.2f, 0.3f, 0.4f, 0.5f, 0.6f, 0.7f, 0.8f);
          UpdateResponse updateResponse = index.update("A", values, null, "tenant1", null, null);
          System.out.println(updateResponse);
      }
  }
  ```

  ```go Go theme={null}
  // Add to the main function:
  idxConn1.UpdateVector(ctx, &pinecone.UpdateVectorRequest{
      Id:     "A",
      Values: []float32{0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8},
  })
  if err != nil {
      log.Fatalf("Failed to update vector with ID %v: %v", id, err)
  }
  ```

  ```csharp C# theme={null}
  using Pinecone;

  var pinecone = new PineconeClient("YOUR_API_KEY");

  var index = pinecone.Index("multitenant-app");

  var upsertResponse = await index.UpsertAsync(new UpsertRequest {
      Vectors = new[]
      {
          new Vector
          {
              Id = "A",
              Values = new[] { 0.1f, 0.2f, 0.3f, 0.4f, 0.5f, 0.6f, 0.7f, 0.8f },
          }
      },
      Namespace = "tenant1",
  });
  ```

  ```bash curl theme={null}
  # The `POST` request below uses the unique endpoint for an index.
  # See https://docs.pinecone.io/guides/manage-data/target-an-index for details.
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="INDEX_HOST"

  curl "https://$INDEX_HOST/vectors/update" \
  	-H "Api-Key: $PINECONE_API_KEY" \
  	-H 'Content-Type: application/json' \
    -H "X-Pinecone-API-Version: 2025-04" \
  	-d '{
  			"id": "A",
  			"values": [01., 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8],
  			"namespace": "tenant1"
  		}'
  ```
</CodeGroup>


## 3. Query tenant data

In a multitenant solution, you need to ensure that the queries of one tenant do not affect the experience of other tenants/customers. To achieve this in Pinecone, target each tenant's [queries](/guides/search/search-overview) at the namespace for the tenant.

For example, the following code queries only `tenant2` for the 3 vectors that are most similar to an example query vector:

<CodeGroup>
  ```python Python theme={null}
  from pinecone.grpc import PineconeGRPC as Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")
  index = pc.Index("multitenant-app")

  query_results = index.query(
      namespace="tenant2",
      vector=[0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7],
      top_k=3,
      include_values=True
  )

  print(query_results)

  # Returns:
  # {'matches': [{'id': 'F',
  #               'score': 1.00000012,
  #               'values': [0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6]},
  #              {'id': 'G',
  #               'score': 1.0,
  #               'values': [0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7]},
  #              {'id': 'E',
  #               'score': 1.0,
  #               'values': [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]}],
  #  'namespace': 'tenant2',
  #  'usage': {'read_units': 6}}
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({ apiKey: "YOUR_API_KEY" });
  const index = pc.index("multitenant-app");

  const queryResponse = await index.namespace("tenant2").query({
    topK: 3,
    vector: [0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7],
    includeValues: true
  });

  console.log(queryResponse);

  // Returns:
  {
    "matches": [
      {
        "id": "F",
        "score": 1.00000012,
        "values": [
          0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6
        ]
      },
      {
        "id": "E",
        "score": 1,
        "values": [ 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5
        ]
      },
      {
        "id": "G",
        "score": 1,
        "values": [
          0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7
        ]
      }
    ],
    "namespace": "tenant2",
    "usage": {
      "readUnits": 6
    }
  }
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Index;
  import io.pinecone.clients.Pinecone;
  import io.pinecone.unsigned_indices_model.QueryResponseWithUnsignedIndices;

  import java.util.Arrays;
  import java.util.List;

  public class QueryExample {
      public static void main(String[] args) {
          Pinecone pc = new Pinecone.Builder("YOUR_API_KEY").build();
          String indexName = "multitenant-app";
          Index index = pc.getIndexConnection(indexName);
          List<Float> queryVector = Arrays.asList(0.7f, 0.7f, 0.7f, 0.7f, 0.7f, 0.7f, 0.7f, 0.7f);
          QueryResponseWithUnsignedIndices queryResponse = index.query(3, queryVector2, null, null, null, "tenant2", null, true, false);
          System.out.println(queryResponse);
      }
  }

  // Results:
  // class QueryResponseWithUnsignedIndices {
  //     matches: [ScoredVectorWithUnsignedIndices {
  //         score: 1.00000012
  //         id: F
  //         values: [0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6]
  //         metadata: 
  //         sparseValuesWithUnsignedIndices: SparseValuesWithUnsignedIndices {
  //             indicesWithUnsigned32Int: []
  //             values: []
  //         }
  //     }, ScoredVectorWithUnsignedIndices {
  //         score: 1
  //         id: E
  //         values: [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]
  //         metadata: 
  //         sparseValuesWithUnsignedIndices: SparseValuesWithUnsignedIndices {
  //             indicesWithUnsigned32Int: []
  //             values: []
  //         }
  //     }, ScoredVectorWithUnsignedIndices {
  //         score: 0.07999992
  //         id: G
  //         values: [0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7]
  //         metadata: 
  //         sparseValuesWithUnsignedIndices: SparseValuesWithUnsignedIndices {
  //             indicesWithUnsigned32Int: []
  //             values: []
  //         }
  //     }]
  //     namespace: tenant2
  //     usage: read_units: 6
  // }
  ```

  ```go Go theme={null}
  // Add to the main function:
  queryVector := []float32{0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7}

  res, err := idxConnection2.QueryByVectorValues(ctx, &pinecone.QueryByVectorValuesRequest{
      Vector:        queryVector,
      TopK:          3,
      IncludeValues: true,
  })
  if err != nil {
      log.Fatalf("Error encountered when querying by vector: %v", err)
  } else {
      fmt.Printf(prettifyStruct(res))
  }

  // Returns:
  // {
  //   "matches": [
  //     {
  //       "vector": {
  //         "id": "F",
  //         "values": [
  //           0.6,
  //           0.6,
  //           0.6,
  //           0.6,
  //           0.6,
  //           0.6,
  //           0.6,
  //           0.6
  //         ]
  //       },
  //       "score": 1.0000001
  //     },
  //     {
  //       "vector": {
  //         "id": "G",
  //         "values": [
  //           0.7,
  //           0.7,
  //           0.7,
  //           0.7,
  //           0.7,
  //           0.7,
  //           0.7,
  //           0.7
  //         ]
  //       },
  //       "score": 1
  //     },
  //     {
  //       "vector": {
  //         "id": "H",
  //         "values": [
  //           0.8,
  //           0.8,
  //           0.8,
  //           0.8,
  //           0.8,
  //           0.8,
  //           0.8,
  //           0.8
  //         ]
  //       },
  //       "score": 1
  //     }
  //   ],
  //   "usage": {
  //     "read_units": 6
  //   }
  // }
  ```

  ```csharp C# theme={null}
  using Pinecone;

  var pinecone = new PineconeClient("YOUR_API_KEY");

  var index = pinecone.Index("multitenant-app");

  var queryResponse = await index.QueryAsync(new QueryRequest {
      Vector = new[] { 0.7f, 0.7f, 0.7f, 0.7f, 0.7f, 0.7f, 0.7f, 0.7f },
      Namespace = "tenant2",
      TopK = 3,
  });

  Console.WriteLine(queryRespnose);
  ```

  ```shell curl theme={null}
  # The `POST` requests below uses the unique endpoint for an index.
  # See https://docs.pinecone.io/guides/manage-data/target-an-index for details.
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="INDEX_HOST"

  curl "https://$INDEX_HOST/query" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H 'Content-Type: application/json' \
    -H "X-Pinecone-API-Version: 2025-04" \
    -d '{
      "namespace": "tenant2",
      "vector": [0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7],
      "topK": 3,
      "includeValues": true
    }'
  #
  # Output:
  # {
  #   "matches": [
  #     {
  #       "id": "F",
  #       "score": 1.00000012,
  #       "values": [0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6]
  #     },
  #     {
  #       "id": "E",
  #       "score": 1,
  #       "values": [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]
  #     },
  #     {
  #       "id": "G",
  #       "score": 1,
  #       "values": [0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7]
  #     }
  #   ],
  #   "namespace": "tenant2",
  #   "usage": {"read_units": 6}
  # }
  ```
</CodeGroup>


## 4. Offboard a tenant

In a multitenant solution, you also need it to be quick and easy to offboard a tenant and delete all of its records. To achieve this in Pinecone, you just [delete the namespace](/guides/manage-data/delete-data#delete-an-entire-namespace) for the specific tenant.

For example, the following code deletes the namespace and all records for `tenant1`:

<CodeGroup>
  ```Python Python theme={null}
  from pinecone.grpc import PineconeGRPC as Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")
  index = pc.Index("multitenant-app")

  index.delete(delete_all=True, namespace='tenant1')
  ```

  ```JavaScript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({ apiKey: "YOUR_API_KEY" });
  const index = pc.index("multitenant-app");

  await index.namespace('tenant1').deleteAll();
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Index;
  import io.pinecone.clients.Pinecone;

  public class DeleteVectorsExample {
      public static void main(String[] args) {
          Pinecone pc = new Pinecone.Builder("YOUR_API_KEY").build();
          Index index = pc.getIndexConnection("multitenant-app");
          index.deleteAll("tenant1");
      }
  }
  ```

  ```go Go theme={null}
  // Add to the main function:
  idxConnection1.DeleteAllVectorsInNamespace(ctx)
  if err != nil {
      log.Fatalf("Failed to delete vectors in namespace \"%v\": %v", idxConnection2.Namespace, err)
  }
  ```

  ```csharp C# theme={null}
  var index = pinecone.Index("multitenant-app");

  var deleteResponse = await index.DeleteAsync(new DeleteRequest {
      DeleteAll = true,
      Namespace = "tenant1",
  });
  ```

  ```bash curl theme={null}
  # The `POST` request below uses the unique endpoint for an index.
  # See https://docs.pinecone.io/guides/manage-data/target-an-index for details.
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="INDEX_HOST"
  curl "https://$INDEX_HOST/vectors/delete" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H 'Content-Type: application/json' \
    -H "X-Pinecone-API-Version: 2025-04" \
    -d '{
      "deleteAll": true,
      "namespace": "tenant1"
    }
  '
  ```
</CodeGroup>


## Alternative: Metadata filtering

When tenant isolation is not a strict requirement, or when you need to query across multiple tenants simultaneously, you can store all records in a single namespace and use metadata fields to assign records to tenants/customers. At query time, you can then [filter by metadata](/guides/index-data/indexing-overview#metadata).

For more guidance on this approach, see [Multitenancy in Vector Databases](https://www.pinecone.io/learn/series/vector-databases-in-production-for-busy-engineers/vector-database-multi-tenancy/).



# Import records
Source: https://docs.pinecone.io/guides/index-data/import-data

Import large datasets efficiently from S3, GCS, or Azure into Pinecone indexes.

Importing from object storage is the most efficient and cost-effective way to load large numbers of records into an index.

To run through this guide in your browser, see the [Bulk import colab notebook](https://colab.research.google.com/github/pinecone-io/examples/blob/master/docs/pinecone-import.ipynb).

<Note>
  This feature is in [public preview](/release-notes/feature-availability) and available only on [Standard and Enterprise plans](https://www.pinecone.io/pricing/).
</Note>


## Before you import

Before you can import records, ensure you have a serverless index, a storage integration, and data formatted in a Parquet file and uploaded to an Amazon S3 bucket, Google Cloud Storage bucket, or Azure Blob Storage container.

### Create an index

[Create a serverless index](/guides/index-data/create-an-index) for your data.

Be sure to create your index on a cloud that supports importing from the object storage you want to use:

| Index location | AWS S3 | Google Cloud Storage | Azure Blob Storage |
| -------------- | :----: | :------------------: | :----------------: |
| **AWS**        |    ✅   |           ✅          |          ✅         |
| **GCP**        |    ❌   |           ✅          |          ✅         |
| **Azure**      |    ❌   |           ✅          |          ✅         |

### Add a storage integration

To import records from a public data source, a storage integration is not required. However, to import records from a secure data source, you must create an integration to allow Pinecone access to data in your object storage. See the following guides:

* [Integrate with Amazon S3](/guides/operations/integrations/integrate-with-amazon-s3)
* [Integrate with Google Cloud Storage](/guides/operations/integrations/integrate-with-google-cloud-storage)
* [Integrate with Azure Blob Storage](/guides/operations/integrations/integrate-with-azure-blob-storage)

### Prepare your data

1. In your Amazon S3 bucket, Google Cloud Storage bucket, or Azure Blob Storage container, create an import directory containing a subdirectory for each namespace you want to import into. The namespaces must not yet exist in your index.

   For example, to import data into the namespaces `example_namespace1` and `example_namespace2`, your directory structure would look like this:

   ```
   <BUCKET_OR_CONTAINER_NAME>/
   --/<IMPORT_DIR>/
   ----/example_namespace1/
   ----/example_namespace2/
   ```

   <Tip>
     To import into the default namespace, use a subdirectory called `__default__`. The default namespace must be empty.
   </Tip>

2. For each namespace, create one or more Parquet files defining the records to import.

   Parquet files must contain specific columns, depending on the index type:

   <Tabs>
     <Tab title="Dense index">
       To import into a namespace in a [dense index](/guides/index-data/indexing-overview#dense-indexes), the Parquet file must contain the following columns:

       | Column name | Parquet type  | Description                                                                                                                     |
       | ----------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------- |
       | `id`        | `STRING`      | Required. The unique [identifier for each record](/guides/get-started/concepts#record-id).                                      |
       | `values`    | `LIST<FLOAT>` | Required. A list of floating-point values that make up the [dense vector embedding](/guides/get-started/concepts#dense-vector). |
       | `metadata`  | `STRING`      | Optional. Additional [metadata](/guides/get-started/concepts#metadata) for each record. To omit from specific rows, use `NULL`. |

       <Warning>
         The Parquet file cannot contain additional columns.
       </Warning>

       For example:

       ```parquet  theme={null}
       id | values                   | metadata
       --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
       1  | [ 3.82  2.48 -4.15 ... ] | {"year": 1984, "month": 6, "source": "source1", "title": "Example1", "text": "When ..."}
       2  | [ 1.82  3.48 -2.15 ... ] | {"year": 1990, "month": 4, "source": "source2", "title": "Example2", "text": "Who ..."}
       ```
     </Tab>

     <Tab title="Sparse index">
       To import into a namespace in a [sparse index](/guides/index-data/indexing-overview#sparse-indexes), the Parquet file must contain the following columns:

       | Column name     | Parquet type                  | Description                                                                                                                                                                                     |
       | --------------- | ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
       | `id`            | `STRING`                      | Required. The unique [identifier for each record](/guides/get-started/concepts#record-id).                                                                                                      |
       | `sparse_values` | `LIST<INT>` and `LIST<FLOAT>` | Required. A list of floating-point values (sparse values) and a list of integer values (sparse indices) that make up the [sparse vector embedding](/guides/get-started/concepts#sparse-vector). |
       | `metadata`      | `STRING`                      | Optional. Additional [metadata](/guides/get-started/concepts#metadata) for each record. To omit from specific rows, use `NULL`.                                                                 |

       <Warning>
         The Parquet file cannot contain additional columns.
       </Warning>

       For example:

       ```parquet  theme={null}
       id | sparse_values                                                                                       | metadata
       --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
       1  | {"indices": [ 822745112 1009084850 1221765879 ... ], "values": [1.7958984 0.41577148 2.828125 ...]} | {"year": 1984, "month": 6, "source": "source1", "title": "Example1", "text": "When ..."}
       2  | {"indices": [ 504939989 1293001993 3201939490 ... ], "values": [1.4383747 0.72849722 1.384775 ...]} | {"year": 1990, "month": 4, "source": "source2", "title": "Example2", "text": "Who ..."}
       ```
     </Tab>

     <Tab title="Hybrid index">
       To import into a namespace in a [hybrid index](/guides/search/hybrid-search#use-a-single-hybrid-index), the Parquet file must contain the following columns:

       | Column name     | Parquet type                                          | Description                                                                                                                                                               |
       | --------------- | ----------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
       | `id`            | `STRING`                                              | Required. The unique [identifier for each record](/guides/get-started/concepts#record-id).                                                                                |
       | `values`        | `LIST<FLOAT>`                                         | Required. A list of floating-point values that make up the [dense vector embedding](/guides/get-started/concepts#dense-vector).                                           |
       | `sparse_values` | `STRUCT<indices: LIST<UINT_32>, values: LIST<FLOAT>>` | Optional. A list of floating-point values that make up the [sparse vector embedding](/guides/get-started/concepts#sparse-vector). To omit from specific rows, use `NULL`. |
       | `metadata`      | `STRING`                                              | Optional. Additional [metadata](/guides/get-started/concepts#metadata) for each record. To omit from specific rows, use `NULL`.                                           |

       <Warning>
         The Parquet file cannot contain additional columns.
       </Warning>

       For example:

       ```parquet  theme={null}
       id | values                   | sparse_values                                                                          | metadata
       --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
       1  | [ 3.82  2.48 -4.15 ... ] | {"indices": [1082468256, 1009084850, 1221765879, ...], "values": [2.0, 3.0, 4.0, ...]} | {"year": 1984, "month": 6, "source": "source1", "title": "Example1", "text": "When ..."}
       2  | [ 1.82  3.48 -2.15 ... ] | {"indices": [2225824123, 1293001993, 3201939490, ...], "values": [5.0, 2.0, 3.0, ...]} | {"year": 1990, "month": 4, "source": "source2", "title": "Example2", "text": "Who ..."}
       ```
     </Tab>
   </Tabs>

3. Upload the Parquet files into the relevant subdirectory.

   For example, if you have subdirectories for the namespaces `example_namespace1` and `example_namespace2` and upload 4 Parquet files into each, your directory structure would look as follows after the upload:

   ```
   <BUCKET_OR_CONTAINER_NAME>/
   --/<IMPORT_DIR>/
   ----/example_namespace1/
   ------0.parquet
   ------1.parquet
   ------2.parquet
   ------3.parquet
   ----/example_namespace2/
   ------4.parquet
   ------5.parquet
   ------6.parquet
   ------7.parquet
   ```


## Import records into an index

<Warning>
  Review [import limits](#import-limits) before starting an import.
</Warning>

Use the [`start_import`](/reference/api/latest/data-plane/start_import) operation to start an asynchronous import of vectors from object storage into an index.

* For `uri`, specify the URI of the bucket and import directory containing the namespaces and Parquet files you want to import. For example:

  * Amazon S3: `s3://BUCKET_NAME/IMPORT_DIR`
  * Google Cloud Storage: `gs://BUCKET_NAME/IMPORT_DIR`
  * Azure Blob Storage: `https://STORAGE_ACCOUNT.blob.core.windows.net/CONTAINER_NAME/IMPORT_DIR`

* For `integration_id`, specify the Integration ID of the Amazon S3, Google Cloud Storage, or Azure Blob Storage integration you created. The ID is found on the [Storage integrations](https://app.pinecone.io/organizations/-/projects/-/storage) page of the Pinecone console.

  <Note>
    An Integration ID is not needed to import from a public bucket.
  </Note>

* For `error_mode`, use `CONTINUE` or `ABORT`.

  * With `ABORT`, the operation stops if any records fail to import.
  * With `CONTINUE`, the operation continues on error, but there is not any notification about which records, if any, failed to import. To see how many records were successfully imported, use the [describe an import](#describe-an-import) operation.

<CodeGroup>
  ```python Python theme={null}
  from pinecone import Pinecone, ImportErrorMode

  pc = Pinecone(api_key="YOUR_API_KEY")

  # To get the unique host for an index, 
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  index = pc.Index(host="INDEX_HOST")
  root = "s3://example_bucket/import"

  index.start_import(
      uri=root,
      integration_id="a12b3d4c-47d2-492c-a97a-dd98c8dbefde", # Optional for public buckets
      error_mode=ImportErrorMode.CONTINUE # or ImportErrorMode.ABORT
  )
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  // To get the unique host for an index, 
  // see https://docs.pinecone.io/guides/manage-data/target-an-index
  const index = pc.index("INDEX_NAME", "INDEX_HOST")

  const storageURI = 's3://example_bucket/import';
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
          String uri = "s3://example_bucket/import";

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

      uri := "s3://example_bucket/import"
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

  var uri = "s3://example_bucket/import";

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
    -H 'Api-Key: $YOUR_API_KEY' \
    -H 'Content-Type: application/json' \
    -H 'X-Pinecone-API-Version: 2025-04' \
    -d '{
          "integrationId": "a12b3d4c-47d2-492c-a97a-dd98c8dbefde",
          "uri": "s3://example_bucket/import",
          "errorMode": {
              "onError": "continue"
              }
          }'
  ```
</CodeGroup>

The response contains an `id` that you can use to [check the status of the import](#list-imports):

```json Response theme={null}
{
   "id": "101"
}
```

Once all the data is loaded, the [index builder](/guides/get-started/database-architecture#index-builder) indexes the records, which usually takes at least 10 minutes. During this indexing process, the expected job status is `InProgress`, but `100.0` percent complete. Once all the imported records are indexed and fully available for querying, the import operation is set to `Completed`.

<Tip>
  You can start a new import using the [Pinecone console](https://app.pinecone.io/organizations/-/projects/-/indexes). Find the index you want to import into, and click the **ellipsis (...) menu > Import data**.
</Tip>


## Track import progress

The amount of time required for an import depends on various factors, including:

* The number of records to import
* The number of namespaces to import, and the the number of records in each
* The total size (in bytes) of the import

To track an import's progress, check its status bar in the [Pinecone console](https://app.pinecone.io/organizations/-/projects/-/import) or use the [`describe_import`](/reference/api/latest/data-plane/describe_import) operation with the import ID:

<CodeGroup>
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

  curl -X GET "https://{INDEX_HOST}/bulk/imports/101" \
    -H 'Api-Key: $YOUR_API_KEY' \
    -H 'X-Pinecone-API-Version: 2025-04'
  ```
</CodeGroup>

The response contains the import details, including the import `status`, `percent_complete`, and `records_imported`:

```json Response theme={null}
{
  "id": "101",
  "uri": "s3://example_bucket/import",
  "status": "InProgress",
  "created_at": "2024-08-19T20:49:00.754Z",
  "finished_at": "2024-08-19T20:49:00.754Z",
  "percent_complete": 42.2,
  "records_imported": 1000000
}
```

If the import fails, the response contains an `error` field with the reason for the failure. See the [Troubleshooting](#troubleshooting) section for more information.

```json Response theme={null}
{
  "id": "102",
  "uri": "s3://example_bucket/import",
  "status": "Failed",
  "percent_complete": 0.0,
  "records_imported": 0,
  "created_at": "2025-08-21T11:29:47.886797+00:00",
  "error": "User error: The namespace \"namespace1\" already exists. Imports are only allowed into nonexistent namespaces.",
  "finished_at": "2025-08-21T11:30:05.506423+00:00"
}
```


## Manage imports

### List imports

Use the [`list_imports`](/reference/api/latest/data-plane/list_imports) operation to list all of the recent and ongoing imports. By default, the operation returns up to 100 imports per page. If the `limit` parameter is passed, the operation returns up to that number of imports per page instead. For example, if `limit=3`, up to 3 imports are returned per page. Whenever there are additional imports to return, the response includes a `pagination_token` for fetching the next page of imports.

<Tabs>
  <Tab title="Python SDK">
    When using the Python SDK, `list_import` paginates automatically.

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

    ```json Response theme={null}
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

    <Tip>
      You can view the list of imports for an index in the [Pinecone console](https://app.pinecone.io/organizations/-/projects/-/indexes/). Select the index and navigate to the **Imports** tab.
    </Tip>
  </Tab>

  <Tab title="Other SDKs">
    When using the Node.js SDK, Java SDK, Go SDK, .NET SDK, or REST API to list recent and ongoing imports, you must manually fetch each page of results. To view the next page of results, include the `paginationToken` provided in the response.

    <CodeGroup>
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
        -H 'Api-Key: $YOUR_API_KEY' \
        -H 'X-Pinecone-API-Version: 2025-04'
      ```
    </CodeGroup>
  </Tab>
</Tabs>

### Cancel an import

The [`cancel_import`](/reference/api/latest/data-plane/cancel_import) operation cancels an import if it is not yet finished. It has no effect if the import is already complete.

<CodeGroup>
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

  curl -X DELETE "https://{INDEX_HOST}/bulk/imports/101" \
    -H 'Api-Key: $YOUR_API_KEY' \
    -H "X-Pinecone-API-Version: 2025-04"
  ```
</CodeGroup>

```json Response theme={null}
{}
```

<Tip>
  You can cancel your import using the [Pinecone console](https://app.pinecone.io/organizations/-/projects/-/import). To cancel an ongoing import, select the index you are importing into and navigate to the **Imports** tab. Then, click the **ellipsis (...) menu > Cancel**.
</Tip>


## Import limits

<Note>
  If your import exceeds these limits, you'll get an `Exceeds system limit` error. Pinecone can help unblock these imports quickly. [Contact Pinecone support](https://app.pinecone.io/organizations/-/settings/support/ticket) for assistance.
</Note>

| Metric                    | Limit   |
| :------------------------ | :------ |
| Max namespaces per import | 10,000  |
| Max size per namespace    | 500 GB  |
| Max files per import      | 100,000 |
| Max size per file         | 10 GB   |

Also:

* You cannot import data from an AWS S3 bucket into a Pinecone index hosted on GCP or Azure.
* You cannot import data from S3 Express One Zone storage.
* You cannot import data into an existing namespace.
* When importing data into the `__default__` namespace of an index, the default namespace must be empty.
* Each import takes at least 10 minutes to complete.
* When importing into an [index with integrated embedding](/guides/index-data/indexing-overview#vector-embedding), records must contain vectors, not text. To add records with text, you must use [upsert](/guides/index-data/upsert-data).


## Troubleshooting

When an import fails, you'll see an error message with the reason for the failure in the [Pinecone console](https://app.pinecone.io/organizations/-/projects/-/import) or in the response to the [describe an import](/reference/api/latest/data-plane/describe_import) operation.

<AccordionGroup>
  <Accordion title="Namespace already exists">
    You cannot import data into an existing namespace. If your import directory structure contains a folder with the name of an existing namespace in your index, the import will fail with the following error:

    ```
    User error: The namespace "example-namespace" already exists. Imports are only allowed into nonexistent namespaces.
    ```

    To fix this, rename the folder to use a namespace name that does not yet exist.
  </Accordion>

  <Accordion title="No namespace found">
    In object storage, your directory structure must be as follows:

    ```
    example_bucket/
    --/imports/
    ----/example_namespace1/
    ------0.parquet
    ------1.parquet
    ------2.parquet
    ------3.parquet
    ----/example_namespace2/
    ------4.parquet
    ------5.parquet
    ------6.parquet
    ------7.parquet
    ```

    If a Parquet file is not nested under a namespace subdirectory, the import will fail with the following error:

    ```
    User error: \"test-import/0.parquet\": No namespace detected. Each file should be nested under a subdirectory of the URI prefix. This indicates which namespace it should be imported into.
    ```

    To fix this, move the Parquet file to a namespace subdirectory.
  </Accordion>

  <Accordion title="Parquet files not found">
    Each namespace subdirectory must contain Parquet files with data to import. If a namespace subdirectory does not include Parquet files, the import will fail with the following error:

    ```
    User error: No Parquet files found under \"gs://example_bucket/imports\". Files must be stored with the specified bucket prefix.
    ```

    To fix this, add Parquet files to the namespace subdirectory.
  </Accordion>

  <Accordion title="Invalid import URI">
    In your [start import](/reference/api/latest/data-plane/start_import) request, the import `uri` must specify only the bucket and import directory containing the namespaces and Parquet files you want to import. If the `uri` also contains a namespaces directory or a Parquet filename, the import will fail with the following error:

    ```
    User error: \"test-import/0.parquet\": It looks like you specified a complete path to a parquet file as the URI prefix to import from. Note that the URI prefix should give an ancestor directory with subdirectories to specify each namespace to import into. See https://docs.pinecone.io/guides/data/understanding-imports#directory-structure.
    ```

    To fix this, remove the namespaces directory or Parquet filename from the `uri`.
  </Accordion>

  <Accordion title="Invalid Parquet files">
    When a Parquet file is not formatted correctly, the import will fail with a message like one of the following:

    ```shell File schema errors theme={null}
    Missing required column \"{0}\"
    Unsupported column \"{0}\"
    ```

    ```shell File corruption errors theme={null}
    Parquet footer could not be parsed. Are you sure this is valid parquet?
    ```

    ```shell Type errors theme={null}
    The expected data type for column \"{column}\" is \"{expected}\", but got \"{given}\"
    The expected data type for metadata is a JSON encoded string in UTF-8 format, but got \"{given}\"
    ```

    These errors are returned for both `CONTINUE` and `ABORT` error modes.

    To fix these errors, check the specific error message and follow the instructions in the [Prepare your data](#prepare-your-data) section.
  </Accordion>

  <Accordion title="Invalid records">
    When the `error_mode` is `ABORT` and a file contains invalid records, the import will stop processing on the first invalid record and return an error message identifying the file name and row:

    ```
    User error: error reading record (file \"/0.parquet\", row 0):
    ```

    This will be followed by an error message identifying the specific issue. For example:

    ```shell Missing values theme={null}
    missing required values in column \"{column}\"
    ```

    ```shell Invalid metadata  theme={null}
    Failed to parse metadata: {msg}
    ```

    ```shell Invalid vectors theme={null}
    Upserting dense vectors is not supported for sparse indexes
    ```

    When the `error_mode` is `CONTINUE`, the import will skip individual invalid records. However, if all records are invalid and skipped (for example, the vector type in the file does not match the vector type of the index), the import will fail with a general message:

    ```
    User error: No vectors added, all rows were skipped for namespace: example-namespace
    ```

    To fix these errors, check the specific error message and follow the instructions in the [Prepare your data](#prepare-your-data) section.
  </Accordion>

  <Accordion title="Duplicate records">
    When your import contains duplicate vectors (records with identical vector values), the duplicates are marked as skipped and not imported. Only one occurrence of each unique vector is added to the index.

    This applies to both `CONTINUE` and `ABORT` error modes:

    * With `ABORT`: The import fails when it encounters a duplicate vector within the import.
    * With `CONTINUE`: The import proceeds, skipping duplicate records silently.

    **Example scenario:**
    If your Parquet file contains:

    ```parquet  theme={null}
    id | values
    ---|---------
    1  | [0.1, 0.2, 0.3]
    2  | [0.1, 0.2, 0.3]  ← Duplicate of record 1, will be skipped
    3  | [0.4, 0.5, 0.6]
    ```

    Only records 1 and 3 will be imported.

    To prevent this from happening, deduplicate your source data before creating Parquet files by removing records with identical vector values.
  </Accordion>
</AccordionGroup>


## See also

* [Integrate with Amazon S3](/guides/operations/integrations/integrate-with-amazon-s3)
* [Integrate with Google Cloud Storage](/guides/operations/integrations/integrate-with-google-cloud-storage)
* [Integrate with Azure Blob Storage](/guides/operations/integrations/integrate-with-azure-blob-storage)
* [Pinecone's pricing](https://www.pinecone.io/pricing/)



---
**Navigation:** [← Previous](./02-check-data-freshness.md) | [Index](./index.md) | [Next →](./04-indexing-overview.md)
