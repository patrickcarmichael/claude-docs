**Navigation:** [← Previous](./26-delete-all-locally-tracked-managed-keys-cli-create.md) | [Index](./index.md) | [Next →](./28-download-a-usage-report.md)

# Install the latest version
pip install pinecone


# Install the latest version with gRPC extras
pip install "pinecone[grpc]"


# Install the latest version with asyncio extras
pip install "pinecone[asyncio]"
```

To install a specific version of the Python SDK, run the following command:

```shell pip theme={null}

# Install a specific version
pip install pinecone==<version>


# Install a specific version with gRPC extras
pip install "pinecone[grpc]"==<version>


# Install a specific version with asyncio extras
pip install "pinecone[asyncio]"==<version>
```

To check your SDK version, run the following command:

```shell pip theme={null}
pip show pinecone
```

<Note>
  To use the [Inference API](/reference/api/introduction#inference), you must be on version 5.0.0 or later.
</Note>

### Install the Pinecone Assistant Python plugin

As of Python SDK v7.0.0, the `pinecone-plugin-assistant` package is included by default. It is only necessary to install the package if you are using a version of the Python SDK prior to v7.0.0.

```shell HTTP theme={null}
pip install --upgrade pinecone pinecone-plugin-assistant
```


## Upgrade

<Warning>
  Before upgrading to `v6.0.0`, update all relevant code to account for the breaking changes explained [here](https://github.com/pinecone-io/pinecone-python-client/blob/main/docs/upgrading.md).

  Also, make sure to upgrade using the `pinecone` package name instead of `pinecone-client`; upgrading with the latter will not work as of `v6.0.0`.
</Warning>

If you already have the Python SDK, upgrade to the latest version as follows:

```shell  theme={null}

# Upgrade to the latest version
pip install pinecone --upgrade


# Upgrade to the latest version with gRPC extras
pip install "pinecone[grpc]" --upgrade


# Upgrade to the latest version with asyncio extras
pip install "pinecone[asyncio]" --upgrade
```


## Initialize

Once installed, you can import the library and then use an [API key](/guides/projects/manage-api-keys) to initialize a client instance:

<CodeGroup>
  ```Python HTTP theme={null}
  from pinecone import Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")
  ```

  ```python gRPC theme={null}
  from pinecone.grpc import PineconeGRPC as Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")
  ```
</CodeGroup>

When [creating an index](/guides/index-data/create-an-index), import the `ServerlessSpec` or `PodSpec` class as well:

<CodeGroup>
  ```Python Serverless index theme={null}
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
    )
  )
  ```

  ```Python Pod-based index theme={null}
  from pinecone.grpc import PineconeGRPC as Pinecone
  from pinecone import PodSpec

  pc = Pinecone(api_key="YOUR_API_KEY")

  pc.create_index(
    name="docs-example",
    dimension=1536,
    metric="cosine",
    spec=PodSpec(
      environment="us-west-1-gcp",
      pod_type="p1.x1",
      pods=1
    )
  )
  ```
</CodeGroup>


## Proxy configuration

If your network setup requires you to interact with Pinecone through a proxy, you will need to pass additional configuration using optional keyword parameters:

* `proxy_url`: The location of your proxy. This could be an HTTP or HTTPS URL depending on your proxy setup.
* `proxy_headers`: Accepts a python dictionary which can be used to pass any custom headers required by your proxy. If your proxy is protected by authentication, use this parameter to pass basic authentication headers with a digest of your username and password. The `make_headers` utility from `urllib3` can be used to help construct the dictionary. **Note:** Not supported with Asyncio.
* `ssl_ca_certs`: By default, the client will perform SSL certificate verification using the CA bundle maintained by Mozilla in the [`certifi`](https://pypi.org/project/certifi/) package. If your proxy is using self-signed certicates, use this parameter to specify the path to the certificate (PEM format).
* `ssl_verify`: SSL verification is enabled by default, but it is disabled when set to `False`. It is not recommened to go into production with SSL verification disabled.

<CodeGroup>
  ```python HTTP theme={null}
  from pinecone import Pinecone
  import urllib3 import make_headers

  pc = Pinecone(
      api_key="YOUR_API_KEY",
      proxy_url='https://your-proxy.com',
      proxy_headers=make_headers(proxy_basic_auth='username:password'),
      ssl_ca_certs='path/to/cert-bundle.pem'
  )
  ```

  ```python gRPC theme={null}
  from pinecone.grpc import PineconeGRPC as Pinecone
  import urllib3 import make_headers

  pc = Pinecone(
      api_key="YOUR_API_KEY",
      proxy_url='https://your-proxy.com',
      proxy_headers=make_headers(proxy_basic_auth='username:password'),
      ssl_ca_certs='path/to/cert-bundle.pem'
  )
  ```

  ```python asyncio theme={null}
  import asyncio
  from pinecone import PineconeAsyncio
  	
  async def main():
      async with PineconeAsyncio(
          api_key="YOUR_API_KEY",
          proxy_url='https://your-proxy.com',
          ssl_ca_certs='path/to/cert-bundle.pem'
      ) as pc:
          # Do async things
          await pc.list_indexes()

  asyncio.run(main())
  ```
</CodeGroup>


## Async requests

Pinecone Python SDK versions 6.0.0 and later provide `async` methods for use with [asyncio](https://docs.python.org/3/library/asyncio.html). Asyncio support makes it possible to use Pinecone with modern async web frameworks such as [FastAPI](https://fastapi.tiangolo.com/), [Quart](https://quart.palletsprojects.com/en/latest/), and [Sanic](https://sanic.dev/en/), and should significantly increase the efficiency of running requests in parallel.

Use the [`PineconeAsyncio`](https://sdk.pinecone.io/python/asyncio.html) class to create and manage indexes and the [`IndexAsyncio`](https://sdk.pinecone.io/python/asyncio.html#pinecone.db_data.IndexAsyncio) class to read and write index data. To ensure that sessions are properly closed, use the `async with` syntax when creating `PineconeAsyncio` and `IndexAsyncio` objects.

<CodeGroup>
  ```python Manage indexes theme={null}
  # pip install "pinecone[asyncio]"
  import asyncio
  from pinecone import PineconeAsyncio, ServerlessSpec

  async def main():
      async with PineconeAsyncio(api_key="YOUR_API_KEY") as pc:
          if not await pc.has_index(index_name):
              desc = await pc.create_index(
                  name="docs-example",
                  dimension=1536,
                  metric="cosine",
                  spec=ServerlessSpec(
                      cloud="aws",
                      region="us-east-1"
                  ),
                  deletion_protection="disabled",
                  tags={
                      "environment": "development"
                  }
              )

  asyncio.run(main())
  ```

  ```python Read and write index data theme={null}
  # pip install "pinecone[asyncio]"
  import asyncio
  from pinecone import Pinecone

  async def main():
      pc = Pinecone(api_key="YOUR_API_KEY")
      async pc.IndexAsyncio(host="INDEX_HOST") as idx:
          await idx.upsert_records(
              namespace="example-namespace",
              records=[
                  {
                      "id": "1",
                      "title": "The Great Gatsby",
                      "author": "F. Scott Fitzgerald",
                      "description": "The story of the mysteriously wealthy Jay Gatsby and his love for the beautiful Daisy Buchanan.",
                      "year": 1925,
                  },
                  {
                      "id": "2",
                      "title": "To Kill a Mockingbird",
                      "author": "Harper Lee",
                      "description": "A young girl comes of age in the segregated American South and witnesses her father's courageous defense of an innocent black man.",
                      "year": 1960,
                  },
                  {
                      "id": "3",
                      "title": "1984",
                      "author": "George Orwell",
                      "description": "In a dystopian future, a totalitarian regime exercises absolute control through pervasive surveillance and propaganda.",
                      "year": 1949,
                  },
              ]
          )

  asyncio.run(main())
  ```
</CodeGroup>


## Query across namespaces

Each query is limited to a single [namespace](/guides/index-data/indexing-overview#namespaces). However, the Pinecone Python SDK provides a `query_namespaces` utility method to run a query in parallel across multiple namespaces in an index and then merge the result sets into a single ranked result set with the `top_k` most relevant results.

The `query_namespaces` method accepts most of the same arguments as `query` with the addition of a required `namespaces` parameter.

<Tabs>
  <Tab title="Python SDK without gRPC">
    When using the Python SDK without gRPC extras, to get good performance, it is important to set values for the `pool_threads` and `connection_pool_maxsize` properties on the index client. The `pool_threads` setting is the number of threads available to execute requests, while `connection_pool_maxsize` is the number of cached http connections that will be held. Since these tasks are not computationally heavy and are mainly i/o bound, it should be okay to have a high ratio of threads to cpus.

    The combined results include the sum of all read unit usage used to perform the underlying queries for each namespace.

    ```python Python theme={null}
    from pinecone import Pinecone

    pc = Pinecone(api_key="YOUR_API_KEY")
    index = pc.Index(
        name="docs-example",
        pool_threads=50,             # <-- make sure to set these
        connection_pool_maxsize=50,  # <-- make sure to set these
    )

    query_vec = [ 0.1, ...] # an embedding vector with same dimension as the index
    combined_results = index.query_namespaces(
        vector=query_vec,
        namespaces=['ns1', 'ns2', 'ns3', 'ns4'],
        metric="cosine",
        top_k=10,
        include_values=False,
        include_metadata=True,
        filter={"genre": { "$eq": "comedy" }},
        show_progress=False,
    )

    for scored_vec in combined_results.matches:
        print(scored_vec)
    print(combined_results.usage)
    ```
  </Tab>

  <Tab title="Python SDK with gRPC">
    When using the Python SDK with gRPC extras, there is no need to set the `connection_pool_maxsize` because grpc makes efficient use of open connections by default.

    ```python Python theme={null}
    from pinecone.grpc import PineconeGRPC

    pc = PineconeGRPC(api_key="YOUR_API_KEY")
    index = pc.Index(
        name="docs-example",
        pool_threads=50, # <-- make sure to set this
    )

    query_vec = [ 0.1, ...] # an embedding vector with same dimension as the index
    combined_results = index.query_namespaces(
        vector=query_vec,
        namespaces=['ns1', 'ns2', 'ns3', 'ns4'],
        metric="cosine",
        top_k=10,
        include_values=False,
        include_metadata=True,
        filter={"genre": { "$eq": "comedy" }},
        show_progress=False,
    )

    for scored_vec in combined_results.matches:
        print(scored_vec)
    print(combined_results.usage)
    ```
  </Tab>
</Tabs>


## Upsert from a dataframe

To quickly ingest data when using the [Python SDK](/reference/python-sdk), use the `upsert_from_dataframe` method. The method includes retry logic and`batch_size`, and is performant especially with Parquet file data sets.

The following example upserts the `uora_all-MiniLM-L6-bm25` dataset as a dataframe.

```Python Python theme={null}
from pinecone import Pinecone, ServerlessSpec
from pinecone_datasets import list_datasets, load_dataset

pc = Pinecone(api_key="API_KEY")

dataset = load_dataset("quora_all-MiniLM-L6-bm25")

pc.create_index(
  name="docs-example",
  dimension=384,
  metric="cosine",
  spec=ServerlessSpec(
    cloud="aws",
    region="us-east-1"
  )
)


# To get the unique host for an index, 

# see https://docs.pinecone.io/guides/manage-data/target-an-index
index = pc.Index(host="INDEX_HOST")

index.upsert_from_dataframe(dataset.drop(columns=["blob"]))
```



# Rust SDK
Source: https://docs.pinecone.io/reference/rust-sdk



<Warning>
  The Rust SDK is in "alpha" and is under active development. The SDK should be considered unstable and should not be used in production. Before a 1.0 release, there are no guarantees of backward compatibility between minor versions. See the [Rust SDK README](https://github.com/pinecone-io/pinecone-rust-client/blob/main/README.md) for full installation instructions and usage examples.

  To make a feature request or report an issue, please [file an issue](https://github.com/pinecone-io/pinecone-rust-client/issues).
</Warning>


## Install

To install the latest version of the [Rust SDK](https://github.com/pinecone-io/pinecone-rust-client), add a dependency to the current project:

```shell  theme={null}
cargo add pinecone-sdk
```


## Initialize

Once installed, you can import the SDK and then use an [API key](/guides/production/security-overview#api-keys) to initialize a client instance:

```rust Rust theme={null}
use pinecone_sdk::pinecone::PineconeClientConfig;   
use pinecone_sdk::utils::errors::PineconeError;
	
#[tokio::main]
async fn main() -> Result<(), PineconeError> {
    let config = PineconeClientConfig {
        api_key: Some("YOUR_API_KEY".to_string()),
        ..Default::default()
    };

    let pinecone = config.client()?;
    let indexes = pinecone.list_indexes().await?;

    println!("Indexes: {:?}", indexes);

    Ok(())
}
```



# Spark-Pinecone connector
Source: https://docs.pinecone.io/reference/tools/pinecone-spark-connector



Use the [`spark-pinecone` connector](https://github.com/pinecone-io/spark-pinecone/) to efficiently create, ingest, and update [vector embeddings](https://www.pinecone.io/learn/vector-embeddings/) at scale with [Databricks and Pinecone](/integrations/databricks).


## Install the Spark-Pinecone connector

<Tabs>
  <Tab title="Databricks platform">
    1. [Install the Spark-Pinecone connector as a library](https://docs.databricks.com/en/libraries/cluster-libraries.html#install-a-library-on-a-cluster).
    2. Configure the library as follows:
       1. Select **File path/S3** as the **Library Source**.

       2. Enter the S3 URI for the Pinecone assembly JAR file:

          ```
          s3://pinecone-jars/1.1.0/spark-pinecone-uberjar.jar  
          ```

          <Note>
            Databricks platform users must use the Pinecone assembly jar listed above to ensure that the proper dependecies are installed.
          </Note>

       3. Click **Install**.
  </Tab>

  <Tab title="Databricks on AWS">
    1. [Install the Spark-Pinecone connector as a library](https://docs.databricks.com/en/libraries/cluster-libraries.html#install-a-library-on-a-cluster).
    2. Configure the library as follows:
       1. Select **File path/S3** as the **Library Source**.

       2. Enter the S3 URI for the Pinecone assembly JAR file:

          ```
          s3://pinecone-jars/1.1.0/spark-pinecone-uberjar.jar  
          ```

       3. Click **Install**.
  </Tab>

  <Tab title="Databricks on GCP / Azure">
    1. [Install the Spark-Pinecone connector as a library](https://docs.databricks.com/en/libraries/cluster-libraries.html#install-a-library-on-a-cluster).
    2. Configure the library as follows:
       1. [Download the Pinecone assembly JAR file](https://repo1.maven.org/maven2/io/pinecone/spark-pinecone_2.12/1.1.0/).
       2. Select **Workspace** as the **Library Source**.
       3. Upload the JAR file.
       4. Click **Install**.
  </Tab>
</Tabs>


## Batch upsert

To batch upsert embeddings to Pinecone:

<CodeGroup>
  ```python Python theme={null}
  from pyspark import SparkConf
  from pyspark.sql import SparkSession
  from pyspark.sql.types import StructType, StructField, ArrayType, FloatType, StringType, LongType

  # Your API key and index name
  api_key = "PINECONE_API_KEY"
  index_name = "PINECONE_INDEX_NAME"
  source_tag = "PINECONE_SOURCE_TAG"

  COMMON_SCHEMA = StructType([
      StructField("id", StringType(), False),
      StructField("namespace", StringType(), True),
      StructField("values", ArrayType(FloatType(), False), False),
      StructField("metadata", StringType(), True),
      StructField("sparse_values", StructType([
          StructField("indices", ArrayType(LongType(), False), False),
          StructField("values", ArrayType(FloatType(), False), False)
      ]), True)
  ])

  # Initialize Spark
  spark = SparkSession.builder.getOrCreate()

  # Read the file and apply the schema
  df = spark.read \
      .option("multiLine", value = True) \
      .option("mode", "PERMISSIVE") \
      .schema(COMMON_SCHEMA) \
      .json("src/test/resources/sample.jsonl")

  # Show if the read was successful
  df.show()

  # Write the dataFrame to Pinecone in batches 
  df.write \
      .option("pinecone.apiKey", api_key) \
      .option("pinecone.indexName", index_name) \
      .option("pinecone.sourceTag", source_tag) \
      .format("io.pinecone.spark.pinecone.Pinecone") \
      .mode("append") \
      .save()
  ```

  ```scala Scala theme={null}
  import io.pinecone.spark.pinecone.{COMMON_SCHEMA, PineconeOptions}
  import org.apache.spark.SparkConf
  import org.apache.spark.sql.{SaveMode, SparkSession}

  object MainApp extends App {
    // Your API key and index name
    val apiKey = "PINECONE_API_KEY"
    val indexName = "PINECONE_INDEX_NAME"
    val sourceTag = "PINECONE_SOURCE_TAG"

    // Configure Spark to run locally with all available cores
    val conf = new SparkConf()
      .setMaster("local[*]")

    // Create a Spark session with the defined configuration
    val spark = SparkSession.builder().config(conf).getOrCreate()

    // Read the JSON file into a DataFrame, applying the COMMON_SCHEMA
    val df = spark.read
      .option("multiLine", value = true)
      .option("mode", "PERMISSIVE")
      .schema(COMMON_SCHEMA)
      .json("src/test/resources/sample.jsonl") // path to sample.jsonl

    // Define Pinecone options as a Map
    val pineconeOptions = Map(
      PineconeOptions.PINECONE_API_KEY_CONF -> apiKey,
      PineconeOptions.PINECONE_INDEX_NAME_CONF -> indexName,
      PineconeOptions.PINECONE_SOURCE_TAG_CONF -> sourceTag
    )

    // Show if the read was successful
    df.show(df.count().toInt)
    
    // Write the DataFrame to Pinecone using the defined options in batches
    df.write
      .options(pineconeOptions)
      .format("io.pinecone.spark.pinecone.Pinecone")
      .mode(SaveMode.Append)
      .save()
  }
  ```
</CodeGroup>

<Tip>
  For a guide on how to set up batch upserts, refer to the [Databricks integration page](/integrations/databricks#setup-guide).
</Tip>


## Stream upsert

To stream upsert embeddings to Pinecone:

<CodeGroup>
  ```python Python theme={null}
  from pyspark.sql import SparkSession
  from pyspark.sql.types import StructType, StructField, ArrayType, FloatType, StringType, LongType
  import os

  # Your API key and index name
  api_key = "PINECONE_API_KEY"
  index_name = "PINECONE_INDEX_NAME"
  source_tag = "PINECONE_SOURCE_TAG"

  COMMON_SCHEMA = StructType([
      StructField("id", StringType(), False),
      StructField("namespace", StringType(), True),
      StructField("values", ArrayType(FloatType(), False), False),
      StructField("metadata", StringType(), True),
      StructField("sparse_values", StructType([
          StructField("indices", ArrayType(LongType(), False), False),
          StructField("values", ArrayType(FloatType(), False), False)
      ]), True)
  ])

  # Initialize Spark session
  spark = SparkSession.builder \
      .appName("StreamUpsertExample") \
      .config("spark.sql.shuffle.partitions", 3) \
      .master("local") \
      .getOrCreate()

  # Read the stream of JSON files, applying the schema from the input directory
  lines = spark.readStream \
      .option("multiLine", True) \
      .option("mode", "PERMISSIVE") \
      .schema(COMMON_SCHEMA) \
      .json("path/to/input/directory/")

  # Write the stream to Pinecone using the defined options
  upsert = lines.writeStream \
      .format("io.pinecone.spark.pinecone.Pinecone") \
      .option("pinecone.apiKey", api_key) \
      .option("pinecone.indexName", index_name) \
      .option("pinecone.sourceTag", source_tag) \
      .option("checkpointLocation", "path/to/checkpoint/dir") \
      .outputMode("append") \
      .start()

  upsert.awaitTermination()
  ```

  ```scala Scala theme={null}
  import io.pinecone.spark.pinecone.{COMMON_SCHEMA, PineconeOptions}
  import org.apache.spark.SparkConf
  import org.apache.spark.sql.{SaveMode, SparkSession}

  object MainApp extends App {
    // Your API key and index name
    val apiKey = "PINECONE_API_KEY"
    val indexName = "PINECONE_INDEX_NAME"

    // Create a Spark session
    val spark = SparkSession.builder()
      .appName("StreamUpsertExample")
      .config("spark.sql.shuffle.partitions", 3)
      .master("local")
      .getOrCreate()

    // Read the JSON files into a DataFrame, applying the COMMON_SCHEMA from input directory
    val lines = spark.readStream
      .option("multiLine", value = true)
      .option("mode", "PERMISSIVE")
      .schema(COMMON_SCHEMA)
      .json("path/to/input/directory/")

    // Define Pinecone options as a Map
    val pineconeOptions = Map(
      PineconeOptions.PINECONE_API_KEY_CONF -> System.getenv("PINECONE_API_KEY"),
      PineconeOptions.PINECONE_INDEX_NAME_CONF -> System.getenv("PINECONE_INDEX"),
      PineconeOptions.PINECONE_SOURCE_TAG_CONF -> System.getenv("PINECONE_SOURCE_TAG")
    )

    // Write the stream to Pinecone using the defined options
    val upsert = lines
      .writeStream
      .format("io.pinecone.spark.pinecone.Pinecone")
      .options(pineconeOptions)
      .option("checkpointLocation", "path/to/checkpoint/dir")
      .outputMode("append")
      .start()

    upsert.awaitTermination()
  }
  ```
</CodeGroup>


## Learn more

* [Spark-Pinecone connector setup guide](/integrations/databricks#setup-guide)
* [GitHub](https://github.com/pinecone-io/spark-pinecone)



# Access your invoices
Source: https://docs.pinecone.io/guides/assistant/admin/access-your-invoices

View and download billing invoices from Pinecone.

You can access your billing history and invoices in the Pinecone console:

1. Go to [**Settings > Billing > Overview**](https://app.pinecone.io/organizations/-/settings/billing).
2. Scroll down to the **Payment history and invoices** section.
3. For each billing period, you can download the invoice by clicking the **Download** button.

Each invoice includes line items for the services used during the billing period. If the total cost of that usage is below the monthly minimum, the invoice also includes a line item covering the rest of the minimum usage commitment.



# Change your payment method
Source: https://docs.pinecone.io/guides/assistant/admin/change-payment-method

Update billing payment method for your organization.

You can pay for the [Standard and Enterprise plans](https://www.pinecone.io/pricing/) with a credit/debit card or through the AWS Marketplace, Microsoft Marketplace, or Google Cloud Marketplace. This page describes how to switch between these payment methods.

<Note>
  To change your payment method, you must be an [organization owner or billing admin](/guides/organizations/understanding-organizations#organization-roles).
</Note>


## Credit card → marketplace

To change from credit card to marketplace billing, you'll need to:

1. Create a new Pinecone organization through the marketplace
2. Migrate your existing projects to the new Pinecone organization
3. Add your team members to the new Pinecone organization
4. Downgrade your original Pinecone organization once migration is complete

<Tabs>
  <Tab title="Credit card → Google Cloud">
    To change from paying with a credit card to paying through the Google Cloud Marketplace, do the following:

    1. Subscribe to Pinecone in the Google Cloud Marketplace:

       1. In the Google Cloud Marketplace, go to the [Pinecone listing](https://console.cloud.google.com/marketplace/product/pinecone-public/pinecone).
       2. Click **Subscribe**.
       3. On the **Order Summary** page, select a billing account, accept the terms and conditions, and click **Subscribe**.

          <Note>The billing unit listed does not reflect the actual cost or metering of costs for Pinecone. See the [Pinecone Pricing page](https://www.pinecone.io/pricing/) for accurate details.</Note>
       4. On the **Your order request has been sent to Pinecone** modal, click **Sign up with Pinecone**. This takes you to a Google-specific Pinecone sign-up page.
       5. Sign up using the same authentication method as your existing Pinecone organization.

    2. Create a new Pinecone organization and connect it to your Google Cloud Marketplace account:

       1. On the **Connect GCP to Pinecone** page, choose **Select an organization > + Create New Organization**.

          <Note>If you see a message saying that the subscription is still in process, wait a few minutes, refresh the page, and proceed only when the message has disappeared.</Note>
       2. Enter the name of the new organization and click **Connect to Pinecone**.
       3. On the **Confirm GCP marketplace Connection** modal, click **Connect**. This takes you to your new organization in the Pinecone console.

    3. Migrate your projects to the new Pinecone organization:

       1. In the Pinecone console, go to [**Settings > Access > Members**](https://app.pinecone.io/organizations/-/settings/access/members).
       2. Make sure the **Owner** email address for your original organization is set as an **Owner** or **Billing Admin** for your new organization. This allows Pinecone to verify that both the original and new organizations are owned by the same person.
       3. Go to [**Settings > Manage**](https://app.pinecone.io/organizations/-/settings/manage) and copy your new organization ID.
       4. Go to [**Settings > Support > Tickets**](https://app.pinecone.io/organizations/-/settings/support/ticket/create).
       5. For **Ticket category**, select **Project or Organization Management**.
       6. For **Subject**, enter "Migrate projects to a new organization".
       7. For **Description**, enter the following:

          ```
          I am changing my payment method from credit card to Google Cloud Marketplace. 
          Please migrate my projects to my new organization: `<NEW_ORG_ID>`
          ```
       8. Click **Submit**.

    4. Add your team members to the new organization:

       1. In the Pinecone console, go to [**Settings > Access > Members**](https://app.pinecone.io/organizations/-/settings/access/members).
       2. [Add your team members to the new organization](/guides/organizations/manage-organization-members#add-a-member-to-an-organization).

    5. Downgrade your original Pinecone organization:

       <Note>
         Do not downgrade your original organization until you receive a confirmation that Pinecone has finished the migration to your new organization.
       </Note>

       1. In the Pinecone console, go to your original organization.
       2. Go to **Settings > Billing > Plans**.
       3. In the **Starter** section, click **Downgrade**.
       4. Click **Confirm downgrade**.

    Going forward, your usage of Pinecone will be billed through the Google Cloud Marketplace.

    <Warning>
      You can [delete your original organization](/troubleshooting/delete-your-organization). However, before deleting, make sure to [download your past invoices](/guides/organizations/manage-billing/access-your-invoices) since you will lose access to them once the organization is deleted.
    </Warning>
  </Tab>

  <Tab title="Credit card → AWS">
    To change from paying with a credit card to paying through the AWS Marketplace, do the following:

    1. Subscribe to Pinecone in the AWS Marketplace:

       1. In the AWS Marketplace, go to the [Pinecone listing](https://aws.amazon.com/marketplace/pp/prodview-xhgyscinlz4jk).
       2. Click **View purchase options**.
       3. On the **Subscribe to Pinecone Vector Database** page, review the offer and then click **Subscribe**.

          <Note>The billing unit listed does not reflect the actual cost or metering of costs for Pinecone. See the [Pinecone Pricing page](https://www.pinecone.io/pricing/) for accurate details.</Note>
       4. You'll see a message stating that your subscription is in process. Click **Set up your account**. This takes you to an AWS-specific Pinecone sign-up page.
       5. Sign up using the same authentication method as your existing Pinecone organization.

    2. Create a new Pinecone organization and connect it to your AWS account:

       1. On the **Connect AWS to Pinecone** page, choose **Select an organization > + Create New Organization**.

       <Note>If you see a message saying that the subscription is still in process, wait a few minutes, refresh the page, and proceed only when the message has disappeared.</Note>

       1. Enter the name of the new organization and click **Connect to Pinecone**.
       2. On the **Confirm AWS Marketplace Connection** modal, click **Connect**. This takes you to your new organization in the Pinecone console.

    3. Migrate your projects to the new Pinecone organization:

       1. In the Pinecone console, go to [**Settings > Access > Members**](https://app.pinecone.io/organizations/-/settings/access/members).
       2. Make sure the **Owner** email address for your original organization is set as an **Owner** or **Billing Admin** for your new organization. This allows Pinecone to verify that both the original and new organizations are owned by the same person.
       3. Go to [**Settings > Manage**](https://app.pinecone.io/organizations/-/settings/manage) and copy your new organization ID.
       4. Go to [**Settings > Support > Tickets**](https://app.pinecone.io/organizations/-/settings/support/ticket/create).
       5. For **Ticket category**, select **Project or Organization Management**.
       6. For **Subject**, enter "Migrate projects to a new organization".
       7. For **Description**, enter the following:

          ```
          I am changing my payment method from credit card to Google Cloud Marketplace. 
          Please migrate my projects to my new organization: `<NEW_ORG_ID>`
          ```
       8. Click **Submit**.

    4. Add your team members to the new organization:

       1. In the Pinecone console, go to [**Settings > Access > Members**](https://app.pinecone.io/organizations/-/settings/access/members).
       2. [Add your team members to the new organization](/guides/organizations/manage-organization-members#add-a-member-to-an-organization).

    5. Downgrade your original Pinecone organization:

       <Note>
         Do not downgrade your original organization until you receive a confirmation that Pinecone has finished the migration to your new organization.
       </Note>

       1. In the Pinecone console, go to your original organization.
       2. Go to **Settings > Billing > Plans**.
       3. In the **Starter** section, click **Downgrade**.
       4. Click **Confirm downgrade**.

    Going forward, your usage of Pinecone will be billed through the AWS Marketplace.

    <Warning>
      You can [delete your original organization](/troubleshooting/delete-your-organization). However, before deleting, make sure to [download your past invoices](/guides/organizations/manage-billing/access-your-invoices) since you will lose access to them once the organization is deleted.
    </Warning>
  </Tab>

  <Tab title="Credit card → Microsoft">
    To change from paying with a credit card to paying through the Microsoft Marketplace, do the following:

    1. Subscribe to Pinecone in the Microsoft Marketplace:

       1. In the Microsoft Marketplace, go to the [Pinecone listing](https://marketplace.microsoft.com/product/saas/pineconesystemsinc1688761585469.pineconesaas).
       2. Click **Get it now**.
       3. Select the **Pinecone - Pay As You Go** plan.
       4. Click **Subscribe**.
       5. On the **Subscribe to Pinecone** page, select the required details and click **Review + subscribe**.

          <Note>The billing unit listed does not reflect the actual cost or metering of costs for Pinecone. See the [Pinecone Pricing page](https://www.pinecone.io/pricing/) for accurate details.</Note>
       6. Click **Subscribe**.
       7. After the subscription is approved, click **Configure account now**. This redirects you to an Microsoft-specific Pinecone login page.
       8. Sign up using the same authentication method as your existing Pinecone organization.

    2. Create a new Pinecone organization and connect it to your Microsoft Marketplace account:

       1. On the **Connect Azure to Pinecone** page, choose **Select an organization > + Create New Organization**.

       <Note>If you see a message saying that the subscription is still in process, wait a few minutes, refresh the page, and proceed only when the message has disappeared.</Note>

       1. Enter the name of the new organization and click **Connect to Pinecone**.
       2. On the **Connect Azure marketplace connection** modal, click **Connect**. This takes you to your new organization in the Pinecone console.

    3. Migrate your projects to the new Pinecone organization:

       1. In the Pinecone console, go to [**Settings > Access > Members**](https://app.pinecone.io/organizations/-/settings/access/members).
       2. Make sure the **Owner** email address for your original organization is set as an **Owner** or **Billing Admin** for your new organization. This allows Pinecone to verify that both the original and new organizations are owned by the same person.
       3. Go to [**Settings > Manage**](https://app.pinecone.io/organizations/-/settings/manage) and copy your new organization ID.
       4. Go to [**Settings > Support > Tickets**](https://app.pinecone.io/organizations/-/settings/support/ticket/create).
       5. For **Ticket category**, select **Project or Organization Management**.
       6. For **Subject**, enter "Migrate projects to a new organization".
       7. For **Description**, enter the following:

          ```
          I am changing my payment method from credit card to Microsoft Marketplace. 
          Please migrate my projects to my new organization: `<NEW_ORG_ID>`
          ```
       8. Click **Submit**.

    4. Add your team members to the new organization:

       1. In the Pinecone console, go to [**Settings > Access > Members**](https://app.pinecone.io/organizations/-/settings/access/members).
       2. [Add your team members to the new organization](/guides/organizations/manage-organization-members#add-a-member-to-an-organization).

    5. Downgrade your original Pinecone organization:

       <Note>
         Do not downgrade your original organization until you receive a confirmation that Pinecone has finished the migration to your new organization.
       </Note>

       1. In the Pinecone console, go to your original organization.
       2. Go to **Settings > Billing > Plans**.
       3. In the **Starter** section, click **Downgrade**.
       4. Click **Confirm downgrade**.

    Going forward, your usage of Pinecone will be billed through the Microsoft Marketplace.

    <Warning>
      You can [delete your original organization](/troubleshooting/delete-your-organization). However, before deleting, make sure to [download your past invoices](/guides/organizations/manage-billing/access-your-invoices) since you will lose access to them once the organization is deleted.
    </Warning>
  </Tab>
</Tabs>


## Marketplace → credit card

To change from marketplace billing to credit card, you'll need to:

1. Create a new organization in your Pinecone account
2. Upgrade the new organization to the Standard or Enterprise plan
3. Migrate your existing projects to the new organization
4. Add your team members to the new organization
5. Downgrade your original organization once migration is complete

<Tabs>
  <Tab title="Google Cloud → credit card">
    To change from paying through the Google Cloud Marketplace to paying with a credit card, do the following:

    1. Create a new organization in your Pinecone account:

       1. In the Pinecone console, go to [**Organizations**](https://app.pinecone.io/organizations/-/settings/account/organizations).
       2. Click **+ Create organization**.
       3. Enter the name of the new organization and click **Create**.

    2. Upgrade the new organization:

       1. Go to [Settings > Billing > Plans](https://app.pinecone.io/organizations/-/settings/billing/plans).
       2. Click **Upgrade** in the **Standard** or **Enterprise** plan section.
       3. Click **Credit / Debit card**.
       4. Enter your credit card information.
       5. Click **Upgrade**.

       The new organization is now set up with credit card billing. You'll use this organization after completing the rest of this process.

    3. Migrate your projects to the new Pinecone organization:

       1. Go to [**Settings > Manage**](https://app.pinecone.io/organizations/-/settings/manage) and copy your new organization ID.
       2. Go to [**Settings > Support > Tickets**](https://app.pinecone.io/organizations/-/settings/support/ticket/create).
       3. For **Ticket category**, select **Project or Organization Management**.
       4. For **Subject**, enter "Migrate projects to a new organization".
       5. For **Description**, enter the following:

          ```
          I am changing my payment method from Google Cloud Marketplace to credit card. 
          Please migrate my projects to my new organization: `<NEW_ORG_ID>`
          ```
       6. Click **Submit**.

    4. Add your team members to the new organization:

       1. In the Pinecone console, go to [**Settings > Access > Members**](https://app.pinecone.io/organizations/-/settings/access/members).
       2. [Add your team members to the new organization](/guides/organizations/manage-organization-members#add-a-member-to-an-organization).

    5. Downgrade your original Pinecone organization:

       <Note>
         Do not downgrade your original organization until you receive a confirmation that Pinecone has finished the migration to your new organization.
       </Note>

       1. In the Pinecone console, go to your original organization.
       2. Go to [**Settings > Billing > Plans**](https://app.pinecone.io/organizations/-/settings/billing/plans).
       3. In the **Starter** section, click **Downgrade**.
       4. Click **Confirm downgrade**.
       5. On the **Continue your downgrade on the GCP marketplace** modal, click **Continue to marketplace**. This takes you to your orders page in Google Cloud Marketplace.
       6. [Cancel the order](https://cloud.google.com/marketplace/docs/manage-billing#saas-products) for your original organization.

          <Tip>
            If you don't see the order, check that the correct billing account is selected.
          </Tip>

    Going forward, you'll use your new organization and your usage will be billed through the credit card you provided.

    <Warning>
      You can [delete your original organization](/troubleshooting/delete-your-organization). However, before deleting, make sure to [download your past invoices](/guides/organizations/manage-billing/access-your-invoices) since you will lose access to them once the organization is deleted.
    </Warning>
  </Tab>

  <Tab title="AWS → credit card">
    To change from paying through the AWS Marketplace to paying with a credit card, do the following:

    1. Create a new organization in your Pinecone account:

       1. In the Pinecone console, go to [**Organizations**](https://app.pinecone.io/organizations/-/settings/account/organizations).
       2. Click **+ Create organization**.
       3. Enter the name of the new organization and click **Create**.

    2. Upgrade the new organization:

       1. Go to [Settings > Billing > Plans](https://app.pinecone.io/organizations/-/settings/billing/plans).
       2. Click **Upgrade** in the **Standard** or **Enterprise** plan section.
       3. Click **Credit / Debit card**.
       4. Enter your credit card information.
       5. Click **Upgrade**.

       The new organization is now set up with credit card billing. You'll use this organization after completing the rest of this process.

    3. Migrate your projects to the new Pinecone organization:

       1. Go to [**Settings > Manage**](https://app.pinecone.io/organizations/-/settings/manage) and copy your new organization ID.
       2. Go to [**Settings > Support > Tickets**](https://app.pinecone.io/organizations/-/settings/support/ticket/create).
       3. For **Ticket category**, select **Project or Organization Management**.
       4. For **Subject**, enter "Migrate projects to a new organization".
       5. For **Description**, enter the following:

          ```
          I am changing my payment method from AWS Marketplace to credit card. 
          Please migrate my projects to my new organization: `<NEW_ORG_ID>`
          ```
       6. Click **Submit**.

    4. Add your team members to the new organization:

       1. In the Pinecone console, go to [**Settings > Access > Members**](https://app.pinecone.io/organizations/-/settings/access/members).
       2. [Add your team members to the new organization](/guides/organizations/manage-organization-members#add-a-member-to-an-organization).

    5. Downgrade your original Pinecone organization:

       <Note>
         Do not downgrade your original organization until you receive a confirmation that Pinecone has finished the migration to your new organization.
       </Note>

       1. In the Pinecone console, go to your original organization.
       2. Go to [**Settings > Billing > Plans**](https://app.pinecone.io/organizations/-/settings/billing/plans).
       3. In the **Starter** section, click **Downgrade**.
       4. Click **Confirm downgrade**.
       5. On the **Continue your downgrade on the AWS marketplace** modal, click **Continue to marketplace**. This takes you to the [Manage subscriptions](https://console.aws.amazon.com/marketplace) page in the AWS Marketplace.
       6. [Cancel the subscription](https://docs.aws.amazon.com/marketplace/latest/buyerguide/cancel-subscription.html#cancel-saas-subscription) to Pinecone.

    Going forward, you'll use your new organization and your usage will be billed through the credit card you provided.

    <Warning>
      You can [delete your original organization](/troubleshooting/delete-your-organization). However, before deleting, make sure to [download your past invoices](/guides/organizations/manage-billing/access-your-invoices) since you will lose access to them once the organization is deleted.
    </Warning>
  </Tab>

  <Tab title="Microsoft → credit card">
    To change from paying through the Microsoft Marketplace to paying with a credit card, do the following:

    1. Create a new organization in your Pinecone account:

       1. In the Pinecone console, go to [**Organizations**](https://app.pinecone.io/organizations/-/settings/account/organizations).
       2. Click **+ Create organization**.
       3. Enter the name of the new organization and click **Create**.

    2. Upgrade the new organization:

       1. Go to [Settings > Billing > Plans](https://app.pinecone.io/organizations/-/settings/billing/plans).
       2. Click **Upgrade** in the **Standard** or **Enterprise** plan section.
       3. Click **Credit / Debit card**.
       4. Enter your credit card information.
       5. Click **Upgrade**.

       The new organization is now set up with credit card billing. You'll use this organization after completing the rest of this process.

    3. Migrate your projects to the new Pinecone organization:

       1. Go to [**Settings > Manage**](https://app.pinecone.io/organizations/-/settings/manage) and copy your new organization ID.
       2. Go to [**Settings > Support > Tickets**](https://app.pinecone.io/organizations/-/settings/support/ticket/create).
       3. For **Ticket category**, select **Project or Organization Management**.
       4. For **Subject**, enter "Migrate projects to a new organization".
       5. For **Description**, enter the following:

          ```
          I am changing my payment method from Microsoft Marketplace to credit card. 
          Please migrate my projects to my new organization: `<NEW_ORG_ID>`
          ```
       6. Click **Submit**.

    4. Add your team members to the new organization:

       1. In the Pinecone console, go to [**Settings > Access > Members**](https://app.pinecone.io/organizations/-/settings/access/members).
       2. [Add your team members to the new organization](/guides/organizations/manage-organization-members#add-a-member-to-an-organization).

    5. Downgrade your original Pinecone organization:

       <Note>
         Do not downgrade your original organization until you receive a confirmation that Pinecone has finished the migration to your new organization.
       </Note>

       1. In the Pinecone console, go to your original organization.
       2. Go to [**Settings > Billing > Plans**](https://app.pinecone.io/organizations/-/settings/billing/plans).
       3. In the **Starter** section, click **Downgrade**.
       4. Click **Confirm downgrade**.
       5. On the **Continue your downgrade on Azure marketplace** modal, click **Continue to marketplace**.
       6. On the **SaaS** page, click your subscription to Pinecone.
       7. Click **Cancel subscription**.
       8. Confirm the cancellation.

    Going forward, you'll use your new organization and your usage will be billed through the credit card you provided.

    <Warning>
      You can [delete your original organization](/troubleshooting/delete-your-organization). However, before deleting, make sure to [download your past invoices](/guides/organizations/manage-billing/access-your-invoices) since you will lose access to them once the organization is deleted.
    </Warning>
  </Tab>
</Tabs>


## Marketplace → marketplace

To change from one marketplace to another, you'll need to:

1. Subscribe to Pinecone in the new marketplace
2. Connect your existing org to the new marketplace
3. Cancel your subscription in the old marketplace

<Tabs>
  <Tab title="AWS/Microsoft → Google Cloud">
    To change from paying through the AWS or Microsoft Marketplace to paying through the Google Cloud Marketplace, do the following:

    1. Subscribe to Pinecone in the Google Cloud Marketplace:

       1. In the Google Cloud Marketplace, go to the [Pinecone listing](https://console.cloud.google.com/marketplace/product/pinecone-public/pinecone).
       2. Click **Subscribe**.
       3. On the **Order Summary** page, select a billing account, accept the terms and conditions, and click **Subscribe**.

          <Note>The billing unit listed does not reflect the actual cost or metering of costs for Pinecone. See the [Pinecone Pricing page](https://www.pinecone.io/pricing/) for accurate details.</Note>
       4. On the **Your order request has been sent to Pinecone** modal, click **Sign up with Pinecone**. This takes you to a Google-specific Pinecone login page.
       5. Log in to your Pinecone account. Use the same authentication method as your existing Pinecone organization.

    2. Connect your existing org to your Google account:

       1. On the **Connect GCP to Pinecone** page, select the Pinecone organization that you want to change from AWS or Microsoft to Google.

          <Note>If you see a message saying that the subscription is still in process, wait a few minutes, refresh the page, and proceed only when the message has disappeared.</Note>
       2. On the **Confirm GCP marketplace connection** modal, click **Connect**. This takes you to your organization in the Pinecone console.

          Going forward, your usage of Pinecone will be billed through the Google Cloud Marketplace.

    3. Cancel your subscription in the AWS or Microsoft Marketplace:

       * For AWS:
         1. In the AWS Marketplace, go to the [Manage subscriptions](https://console.aws.amazon.com/marketplace) page in the AWS Marketplace.
         2. [Cancel the subscription](https://docs.aws.amazon.com/marketplace/latest/buyerguide/cancel-subscription.html#cancel-saas-subscription) to Pinecone.

       * For Microsoft:
         1. Go to [Azure SaaS Resource Management](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.SaaS%2Fresources).
         2. Select your subscription to Pinecone.
         3. Click **Cancel subscription**.
         4. Confirm the cancellation.
  </Tab>

  <Tab title="Google Cloud/Microsoft → AWS">
    To change from paying through the Google Cloud Marketplace or Microsoft Marketplace to paying through the AWS Marketplace, do the following:

    1. Subscribe to Pinecone in the AWS Marketplace:

       1. In the AWS Marketplace, go to the [Pinecone listing](https://aws.amazon.com/marketplace/pp/prodview-xhgyscinlz4jk) in the AWS Marketplace.
       2. Click **View purchase options**.
       3. On the **Subscribe to Pinecone Vector Database** page, review the offer and then click **Subscribe**.

          <Note>The billing unit listed does not reflect the actual cost or metering of costs for Pinecone. See the [Pinecone Pricing page](https://www.pinecone.io/pricing/) for accurate details.</Note>
       4. You'll see a message stating that your subscription is in process. Click **Set up your account**. This takes you to an AWS-specific Pinecone login page.
       5. Log in to your Pinecone account. Use the same authentication method as your existing Pinecone organization.

    2. Connect your existing org to your AWS account:

       1. On the **Connect AWS to Pinecone** page, select the Pinecone organization that you want to change from Google Cloud or Microsoft to AWS.

          <Note>If you see a message saying that the subscription is still in process, wait a few minutes, refresh the page, and proceed only when the message has disappeared.</Note>
       2. On the **Confirm AWS marketplace connection** modal, click **Connect**. This takes you to your organization in the Pinecone console.

          Going forward, your usage of Pinecone will be billed through the AWS Marketplace.

    3. Cancel your subscription in the Google Cloud Marketplace or Microsoft Marketplace:

       * For Google Cloud Marketplace:
         1. Go to the [Orders](https://console.cloud.google.com/marketplace/orders) page.
         2. [Cancel the order](https://cloud.google.com/marketplace/docs/manage-billing#saas-products) for Pinecone.

       * For Microsoft Marketplace:
         1. Go to [Azure SaaS Resource Management](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.SaaS%2Fresources).
         2. Select your subscription to Pinecone.
         3. Click **Cancel subscription**.
         4. Confirm the cancellation.
  </Tab>

  <Tab title="Google Cloud/AWS → Microsoft">
    To change from paying through the Google Cloud Marketplace or AWS Marketplace to paying through the Microsoft Marketplace, do the following:

    1. Subscribe to Pinecone in the Microsoft Marketplace:

       1. In the Microsoft Marketplace, go to the [Pinecone listing](https://marketplace.microsoft.com/product/saas/pineconesystemsinc1688761585469.pineconesaas).
       2. Click **Get it now**.
       3. Select the **Pinecone - Pay As You Go** plan.
       4. Click **Subscribe**.
       5. On the **Subscribe to Pinecone** page, select the required details and click **Review + subscribe**.

          <Note>The billing unit listed does not reflect the actual cost or metering of costs for Pinecone. See the [Pinecone Pricing page](https://www.pinecone.io/pricing/) for accurate details.</Note>
       6. Click **Subscribe**.
       7. After the subscription is approved, click **Configure account now**. This redirects you to an Microsoft-specific Pinecone login page.
       8. Log in to your Pinecone account. Use the same authentication method as your existing Pinecone organization.

    2. Connect your existing org to your Microsoft account:

       1. On the **Connect Azure to Pinecone** page, select the Pinecone organization that you want to change from Google Cloud or AWS to Microsoft.

          <Note>If you see a message saying that the subscription is still in process, wait a few minutes, refresh the page, and proceed only when the message has disappeared.</Note>
       2. On the **Confirm Azure marketplace connection** modal, click **Connect**. This takes you to your organization in the Pinecone console.

          Going forward, your usage of Pinecone will be billed through the Microsoft Marketplace.

    3. Cancel your subscription in the Google Cloud Marketplace or AWS Marketplace:

       * For Google Cloud Marketplace:
         1. Go to the [Orders](https://console.cloud.google.com/marketplace/orders) page.
         2. [Cancel the order](https://cloud.google.com/marketplace/docs/manage-billing#saas-products) for Pinecone.

       * For AWS Marketplace:
         1. Go to the [Manage subscriptions](https://console.aws.amazon.com/marketplace) page in the AWS Marketplace.
         2. [Cancel the subscription](https://docs.aws.amazon.com/marketplace/latest/buyerguide/cancel-subscription.html#cancel-saas-subscription) to Pinecone.
  </Tab>
</Tabs>


## Credit card → credit card

To update your credit card information in the Pinecone console, do the following:

1. Go to [**Settings > Billing > Overview**](https://app.pinecone.io/organizations/-/settings/billing).
2. In the **Billing Contact** section, click **Edit**.
3. Enter your new credit card information.
4. Click **Update**.



# Configure audit logs
Source: https://docs.pinecone.io/guides/assistant/admin/configure-audit-logs

Track user and API actions with audit log configuration.

This page describes how to configure audit logs in Pinecone. Audit logs provide a detailed record of user, service account, and API actions that occur within Pinecone. Pinecone supports Amazon S3 as a destination for audit logs.

<Note>
  To enable and manage audit logs, you must be an [organization owner](/guides/assistant/admin/organizations-overview#organization-roles). This feature is in [public preview](/assistant-release-notes/feature-availability) and available only on [Enterprise plans](https://www.pinecone.io/pricing/).
</Note>


## Enable audit logs

Before you can enable audit logs, you need to create an IAM policy and role in Amazon S3. To start, ensure you have the following:

* A [Pinecone account](https://app.pinecone.io/).
* An [Amazon S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-buckets.html).

### 1. Create an IAM policy

In the [AWS IAM console](https://console.aws.amazon.com/iam/home):

1. In the navigation pane, click **Policies**.
2. Click **Create policy**.
3. In **Select a service** section, select **S3**.
4. Select the following actions to allow:
   * `ListBucket`: Permission to list some or all of the objects in an S3 bucket.
   * `PutObject`: Permission to add an object to an S3 bucket.
5. In the **Resources** section, select **Specific**.
6. For the **bucket**, specify the ARN of the bucket you created. For example: `arn:aws:s3:::example-bucket-name`
7. For the **object**, specify an object ARN as the target resource. For example: `arn:aws:s3:::example-bucket-name/*`
8. Click **Next**.
9. Specify the name of your policy. For example:  "Pinecone-S3-Access".
10. Click **Create policy**.

### 2. Set up access using an IAM role

In the [AWS IAM console](https://console.aws.amazon.com/iam/home):

1. In the navigation pane, click **Roles**.

2. Click **Create role**.

3. In the **Trusted entity type** section, select **AWS account**.

4. Select **Another AWS account**.

5. Enter the Pinecone AWS VPC account ID: `713131977538`

6. Click **Next**.

7. Select the policy you created.

8. Click **Next**.

9. Specify the role name. For example: "Pinecone".

10. Click **Create role**.

11. Click the role you created.

12. On the **Summary** page for the role, find the **ARN**.

    For example: `arn:aws:iam::123456789012:role/PineconeAccess`

13. Copy the **ARN**.

    You will need to enter the ARN into Pinecone later.

### 3. Connect Pinecone to Amazon S3

1. Go to [**Settings > Audit logs**](https://app.pinecone.io/organizations/-/settings/logging) in the Pinecone console.
2. Enter the **Role ARN** of the IAM role you created.
3. Enter the name of the Amazon S3 bucket you created.
4. Click **Enable audit logging**.

Once you enable audit logs, Pinecone will start writing logs to the S3 bucket. In your bucket, you will also see a file named `audit-log-access-test`, which is a test file that Pinecone writes to verify that it has the necessary permissions to write logs to the bucket.


## View audit logs

Logs are written to the S3 bucket approximately every 30 minutes. Each log batch will be saved into its own file as a JSON blob, keyed by the time of the log to be written. Only logs since the integration was created and enabled will be saved.

For more information about the log schema and captured events, see [Security overview - Audit logs](/guides/assistant/admin/security-overview#audit-logs).


## Edit audit log integration details

You can edit the details of the audit log integration in the Pinecone console:

1. Go to [**Settings > Audit logs**](https://app.pinecone.io/organizations/-/settings/logging).
2. Enter the new **Role ARN** or **AWS Bucket**.
3. Click **Update settings**.


## Disable audit logs

If you disable audit logs, logs not yet saved will be lost. You can disable audit logs in the Pinecone console:

1. Go to [**Settings > Audit logs**](https://app.pinecone.io/organizations/-/settings/logging).
2. Click the toggle next to **Audit logs are active**.
3. Click **Confirm**.


## Remove audit log integration

If you remove the audit log integration, logs not yet saved will be lost. You can remove the audit log integration in the Pinecone console:

1. Go to [**Settings > Audit logs**](https://app.pinecone.io/organizations/-/settings/logging).
2. At the top of the page, click the **ellipsis (...) menu > Remove integration**.
3. Click **Remove integration**.



# Configure SSO with Okta
Source: https://docs.pinecone.io/guides/assistant/admin/configure-sso-with-okta

Enable SSO authentication using Okta integration.

This page describes how to set up Pinecone with Okta as the single sign-on (SSO) provider. These instructions can be adapted for any provider with SAML 2.0 support.

<Note>SSO is available on Standard and Enterprise plans.</Note>


## Before you begin

This page assumes you have the following:

* Access to your organization's [Pinecone console](https://login.pinecone.io) as an [organization owner](/guides/organizations/understanding-organizations#organization-owners).
* Access to your organization's [Okta Admin console](https://login.okta.com/).


## 1. Start SSO setup in Pinecone

First, start setting up SSO in Pinecone. In this step, you'll capture a couple values necessary for configuring Okta in [Step 2](#2-create-an-app-integration-in-okta).

1. In the Pinecone console, go to [**Settings > Manage**](https://app.pinecone.io/organizations/-/settings/manage).
2. In the **Single Sign-On** section, click **Enable SSO**.
3. In the **Setup SSO** dialog, copy the **Entity ID** and the **Assertion Consumer Service (ACS) URL**. You'll need these values in [Step 2](#2-create-an-app-integration-in-okta).
4. Click **Next**.

Keep this window or browser tab open. You'll come back to it in [Step 4](#4-complete-sso-setup-in-pinecone).


## 2. Create an app integration in Okta

In [Okta](https://login.okta.com/), follow these steps to create and configure a Pinecone app integration:

1. If you're not already on the Okta Admin console, navigate there by clicking the **Admin** button.

2. Navigate to **Applications > Applications**.

3. Click **Create App Integration**.

4. Select **SAML 2.0**.

5. Click **Next**.

6. Enter the **General Settings**:

   * **App name**: `Pinecone`
   * **App logo**: (optional)
   * **App visibility**: Set according to your organization's needs.

7. Click **Next**.

8. For **SAML Settings**, enter values you copied in [Step 1](#1-start-sso-setup-in-pinecone):

   * **Single sign-on URL**: Your **Assertion Consumer Service (ACS) URL**
   * **Audience URI (SP Entity ID)**: Your **Entity ID**
   * **Name ID format**: `EmailAddress`
   * **Application username**: `Okta username`
   * **Update application username on**: `Create and update`

9. In the **Attribute Statements** section, create the following attribute:

   * **Name**: `email`
   * **Value**: `user.email`

10. Click **Next**.

11. Click **Finish**.


## 3. Get the sign on URL and certificate from Okta

Next, in Okta, get the URL and certificate for the Pinecone application you just created. You'll use these in [Step 4](#4-complete-sso-setup-in-pinecone).

1. In the Okta Admin console, navigate to **Applications > Pinecone > Sign On**. If you're continuing from the previous step, you should already be on the right page.
2. In the **SAML 2.0** section, expand **More details**.
3. Copy the **Sign on URL**.
4. Download the **Signing Certificate**.

   <Warning>
     Download the certificate, don't copy it. The downloaded version contains necessary `-----BEGIN CERTIFICATE-----` and `-----END CERTIFICATE-----` lines.
   </Warning>


## 4. Complete SSO setup in Pinecone

In the browser tab or window you kept open in [Step 1](#1-start-sso-setup-in-pinecone), complete the SSO setup in Pinecone:

1. In the **SSO Setup** window, enter the following values:

   * **Login URL**: The URL copied in [Step 3](#3-get-the-sign-on-url-and-certificate-from-okta).
   * **Email domain**: Your company's email domain. To target multiple domains, enter each domain separated by a comma.
   * **Certificate**: The contents of the certificate file you copied in [Step 3](#3-get-the-sign-on-url-and-certificate-from-okta).

     <Warning>
       When pasting the certificate, be sure to include the `-----BEGIN CERTIFICATE-----` and `-----END CERTIFICATE-----` lines.
     </Warning>

2. Choose whether or not to **Enforce SSO for all users**.

   * If enabled, all members of your organization must use SSO to log in to Pinecone.
   * If disabled, members can choose to log in with SSO or with their Pinecone credentials.

3. Click **Next**.

4. Select a **Default role** for all users who log in with SSO. You can change user roles later.

Okta is now ready to be used for single sign-on. Follow the [Okta docs](https://help.okta.com/en-us/content/topics/users-groups-profiles/usgp-main.htm) to learn how to add users and groups.



# Create a project
Source: https://docs.pinecone.io/guides/assistant/admin/create-a-project

Create a new Pinecone project in your organization.

This page shows you how to create a project.

If you are an [organization owner or user](/guides/organizations/understanding-organizations#organization-roles), you can create a project in your organization:

<Tabs>
  <Tab title="Pinecone console">
    1. In the Pinecone console, go to [**your profile > Organization settings > Projects**](https://app.pinecone.io/organizations/-/settings/projects).

    2. Click **+ Create Project**.

    3. Enter a **Name**.

       <Note>
         A project name can contain up to 512 characters. For more information, see [Object identifiers](/reference/api/database-limits#identifier-limits).
       </Note>

    4. (Optional) Tags are key-value pairs that you can use to categorize and identify the project. To add a tag, click **+ Add tag** and enter a tag key and value.

    5. (Optional) Select **Encrypt with Customer Managed Encryption Key**. For more information, see [Configure CMEK](/guides/production/configure-cmek).

    6. Click **Create project**.

       To load an index with a [sample dataset](/guides/data/use-sample-datasets), click **Load sample data** and follow the prompts.

    <Note>
      Organizations on the Starter plan are limited to one project. To create additional projects, [upgrade to the Standard or Enterprise plan](/guides/organizations/manage-billing/upgrade-billing-plan).
    </Note>
  </Tab>

  <Tab title="Code">
    <Note>
      An [access token](/guides/organizations/manage-service-accounts#retrieve-an-access-token) must be provided to complete this action through the Admin API. The Admin API is in [public preview](/release-notes/feature-availability).
    </Note>

    <CodeGroup>
      ```bash curl theme={null}
      PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"

      curl "https://api.pinecone.io/admin/projects" \
          -H "X-Pinecone-Api-Version: 2025-04" \
      	-H "Authorization: Bearer $PINECONE_ACCESS_TOKEN" \
      	-d '{
                "name":"example-project"
              }'
      ```

      ```bash CLI theme={null}
      # Target the organization for which you want to 
      # create a project.
      pc target -o "example-org"
      # Create the project and set it as the target 
      # project for the CLI.
      pc project create -n "example-project" --target
      ```
    </CodeGroup>

    The example returns a response like the following:

    <CodeGroup>
      ```json curl theme={null}
      {
        "id": "32c8235a-5220-4a80-a9f1-69c24109e6f2",
        "name": "example-project",
        "max_pods": 0,
        "force_encryption_with_cmek": false,
        "organization_id": "-NM7af6f234168c4e44a",
        "created_at": "2025-03-16T22:46:45.030Z"
      }
      ```

      ```text CLI theme={null}
      [SUCCESS] Project example-cli-project created successfully.

      ATTRIBUTE           VALUE
      Name                example-project
      ID                  32c8235a-5220-4a80-a9f1-69c24109e6f2
      Organization ID     -NM7af6f234168c4e44a
      Created At          2025-10-27 23:27:46.370088 +0000 UTC
      Force Encryption    false
      Max Pods            5

      [SUCCESS] Target project set to example-cli-project
      ```
    </CodeGroup>
  </Tab>
</Tabs>


## Next steps

* [Add users to your project](/guides/projects/manage-project-members#add-members-to-a-project)
* [Create an index](/guides/index-data/create-an-index)



# Downgrade your plan
Source: https://docs.pinecone.io/guides/assistant/admin/downgrade-billing-plan

Downgrade from a paid plan to the free Starter plan.

<Note>
  To change your billing plan, you must be an [organization owner or billing admin](/guides/organizations/understanding-organizations#organization-roles).
</Note>


## Requirements

Before you can downgrade, your organization must be under the [Starter plan quotas](/reference/api/database-limits):

* No more than 5 indexes, all serverless and in the `us-east-1` region of AWS
  * If you have serverless indexes in a region other than `us-east-1`, [create a new serverless index](/guides/index-data/create-an-index#create-a-serverless-index) in `us-east-1`, [re-upsert your data](/guides/index-data/upsert-data) into the new index, and [delete the old index](/guides/manage-data/manage-indexes#delete-an-index).
  * If you have more than 5 serverless indexes, [delete indexes](/guides/manage-data/manage-indexes#delete-an-index) until you have 5 or fewer.
  * If you have pod-based indexes, [save them as collections](/guides/manage-data/back-up-an-index#create-a-backup-using-a-collection) and then [delete them](/guides/manage-data/manage-indexes#delete-an-index).
* No more than 1 project
  * If you have more than 1 project, [delete all but 1 project](/guides/projects/manage-projects#delete-a-project).
  * Before you can delete a project, you must [delete all indexes](/guides/manage-data/manage-indexes#delete-an-index) and [delete all collections](/guides/manage-data/back-up-an-index#delete-a-collection) in the project.
* No more than 2 GB of data across all of your serverless indexes
  * If you are storing more than 2 GB of data, [delete records](/guides/manage-data/delete-data) until you're storing less than 2 GB.
* No more than 100 namespaces per serverless index
  * If any serverless index has more than 100 namespaces, [delete namespaces](/guides/manage-data/delete-data#delete-all-records-from-a-namespace) until it has 100 or fewer remaining.
* No more than 3 [assistants](/guides/assistant/overview)
  * If you have more than 3 assistants, [delete assistants](/guides/assistant/manage-assistants#delete-an-assistant) until you have 3 or fewer.
* No more than 10 files per assistant
  * If you have more than 10 files uploaded to an assistant, [delete files](/guides/assistant/manage-files#delete-a-file) until the assistant has 10 or fewer.
* No more than 1 GB of assistant storage
  * If you have more than 1 GB of assistant storage, [delete files](https://docs.pinecone.io/guides/assistant/manage-files#delete-a-file) until you're storing less than 1 GB.


## Downgrade to the Starter plan

The downgrade process is different depending on how you are paying for Pinecone.

<Warning>
  It is important to start the downgrade process in the Pinecone console, as described below. When you do so, Pinecone checks that you are under the [Starter plan quotas](#requirements) before allowing you to downgrade. In contrast, if you start the downgrade process in one of the cloud marketplaces, Pinecone cannot check that you are under these quotas before allowing you to downgrade. If you are over the quotas, Pinecone will deactivate your account, and you will need to [contact support](https://www.pinecone.io/contact/support/).
</Warning>

<Tabs>
  <Tab title="Credit card">
    If you are paying with a credit card, downgrade as follows:

    1. In the Pinecone console, go to [**Settings > Billing > Plans**](https://app.pinecone.io/organizations/-/settings/billing/plans).
    2. Click **Downgrade** in the **Starter** plan section.

    Your billing will end immediately. However, you will receive a final invoice for any charges accrued in the current month.
  </Tab>

  <Tab title="Google Cloud Marketplace">
    If you are paying through the Google Cloud Marketplace, downgrade as follows:

    1. In the Pinecone console, go to [**Settings > Billing > Plans**](https://app.pinecone.io/organizations/-/settings/billing/plans).
    2. In the **Starter** section, click **Downgrade**.
    3. Click **Confirm downgrade**.
    4. On the **Continue your downgrade on the GCP marketplace** modal, click **Continue to marketplace**. This takes you to your orders page in Google Cloud Marketplace.
    5. [Cancel the order](https://cloud.google.com/marketplace/docs/manage-billing#saas-products) for your Pinecone subscription.

       <Tip>
         If you don't see the order, check that the correct billing account is selected.
       </Tip>

    Your billing will end immediately. However, you will receive a final invoice for any charges accrued in the current month.
  </Tab>

  <Tab title="AWS Marketplace">
    If you are paying through the AWS Marketplace, downgrade as follows:

    1. In the Pinecone console, go to [**Settings > Billing > Plans**](https://app.pinecone.io/organizations/-/settings/billing/plans).
    2. In the **Starter** section, click **Downgrade**.
    3. Click **Confirm downgrade**.
    4. On the **Continue your downgrade on the AWS marketplace** modal, click **Continue to marketplace**. This takes you to the [Manage subscriptions](https://console.aws.amazon.com/marketplace) page in the AWS Marketplace.
    5. [Cancel the subscription](https://docs.aws.amazon.com/marketplace/latest/buyerguide/cancel-subscription.html#cancel-saas-subscription) to Pinecone.

    Your billing will end immediately. However, you will receive a final invoice for any charges accrued in the current month.
  </Tab>

  <Tab title="Microsoft Marketplace">
    If you are paying through the Microsoft Marketplace, downgrade as follows:

    1. In the Pinecone console, go to [**Settings > Billing > Plans**](https://app.pinecone.io/organizations/-/settings/billing/plans).
    2. In the **Starter** section, click **Downgrade**.
    3. Click **Confirm downgrade**.
    4. On the **Continue your downgrade on Microsoft marketplace** modal, click **Continue to marketplace**.
    5. On the **SaaS** page, click your subscription to Pinecone.
    6. Click **Cancel subscription**.
    7. Confirm the cancellation.

    Your billing will end immediately. However, you will receive a final invoice for any charges accrued in the current month.
  </Tab>
</Tabs>



---
**Navigation:** [← Previous](./26-delete-all-locally-tracked-managed-keys-cli-create.md) | [Index](./index.md) | [Next →](./28-download-a-usage-report.md)
