**Navigation:** [← Previous](./40-concepts.md) | [Index](./index.md) | Next →

# IVFFlat indexes



IVFFlat is a type of vector index for approximate nearest neighbor search. It is a frequently used index type that can improve performance when querying highly-dimensional vectors, like those representing embeddings.



## Choosing an index

Today `pgvector` supports two types of indexes:

*   [HNSW](/docs/guides/ai/vector-indexes/hnsw-indexes)
*   [IVFFlat](/docs/guides/ai/vector-indexes/ivf-indexes)

In general we recommend using [HNSW](/docs/guides/ai/vector-indexes/hnsw-indexes) because of its [performance](/blog/increase-performance-pgvector-hnsw#hnsw-performance-1536-dimensions) and [robustness against changing data](/docs/guides/ai/vector-indexes/hnsw-indexes#when-should-you-create-hnsw-indexes). If you have a special use case that requires IVFFlat instead, keep reading.



## Usage

The way you create an IVFFlat index depends on the distance operator you are using. `pgvector` includes 3 distance operators:

| Operator | Description            | [**Operator class**](https://www.postgresql.org/docs/current/sql-createopclass.html) |
| -------- | ---------------------- | ------------------------------------------------------------------------------------ |
| `<->`    | Euclidean distance     | `vector_l2_ops`                                                                      |
| `<#>`    | negative inner product | `vector_ip_ops`                                                                      |
| `<=>`    | cosine distance        | `vector_cosine_ops`                                                                  |

Use the following SQL commands to create an IVFFlat index for the operator(s) used in your queries.


### Euclidean L2 distance (`vector_l2_ops`)

```sql
create index on items using ivfflat (column_name vector_l2_ops) with (lists = 100);
```


### Inner product (`vector_ip_ops`)

```sql
create index on items using ivfflat (column_name vector_ip_ops) with (lists = 100);
```


### Cosine distance (`vector_cosine_ops`)

```sql
create index on items using ivfflat (column_name vector_cosine_ops) with (lists = 100);
```

Currently vectors with up to 2,000 dimensions can be indexed.



## How does IVFFlat work?

IVF stands for 'inverted file indexes'. It works by clustering your vectors in order to reduce the similarity search scope. Rather than comparing a vector to every other vector, the vector is only compared against vectors within the same cell cluster (or nearby clusters, depending on your configuration).


### Inverted lists (cell clusters)

When you create the index, you choose the number of inverted lists (cell clusters). Increase this number to speed up queries, but at the expense of recall.

For example, to create an index with 100 lists on a column that uses the cosine operator:

```sql
create index on items using ivfflat (column_name vector_cosine_ops) with (lists = 100);
```

For more info on the different operators, see [Distance operations](#distance-operators).

For every query, you can set the number of probes (1 by default). The number of probes corresponds to the number of nearby cells to probe for a match. Increase this for better recall at the expense of speed.

To set the number of probes for the duration of the session run:

```sql
set ivfflat.probes = 10;
```

To set the number of probes only for the current transaction run:

```sql
begin;
set local ivfflat.probes = 10;
select ...
commit;
```

If the number of probes is the same as the number of lists, exact nearest neighbor search will be performed and the planner won't use the index.


### Approximate nearest neighbor

One important note with IVF indexes is that nearest neighbor search is approximate, since exact search on high dimensional data can't be indexed efficiently. This means that similarity results will change (slightly) after you add an index (trading recall for speed).



## When should you create IVFFlat indexes?

`pgvector` recommends building IVFFlat indexes only after the table has sufficient data, so that the internal IVFFlat cell clusters are based on your data's distribution. Anytime the distribution changes significantly, consider rebuilding indexes.



## Resources

Read more about indexing on `pgvector`'s [GitHub page](https://github.com/pgvector/pgvector#indexing).



# Face similarity search

Identify the celebrities who look most similar to you using Supabase Vecs.

This guide will walk you through a ["Face Similarity Search"](https://github.com/supabase/supabase/blob/master/examples/ai/face_similarity.ipynb) example using Colab and Supabase Vecs. You will be able to identify the celebrities who look most similar to you (or any other person). You will:

1.  Launch a Postgres database that uses pgvector to store embeddings
2.  Launch a notebook that connects to your database
3.  Load the "`ashraq/tmdb-people-image`" celebrity dataset
4.  Use the `face_recognition` model to create an embedding for every celebrity photo.
5.  Search for similar faces inside the dataset.



## Project setup

Let's create a new Postgres database. This is as simple as starting a new Project in Supabase:

1.  [Create a new project](https://database.new/) in the Supabase dashboard.
2.  Enter your project details. Remember to store your password somewhere safe.

Your database will be available in less than a minute.

**Finding your credentials:**

You can find your project credentials on the dashboard:

*   [Database connection strings](/dashboard/project/_/settings/api?showConnect=true): Direct and Pooler connection details including the connection string and parameters.
*   [Database password](/dashboard/project/_/database/settings): Reset database password here if you do not have it.
*   [API credentials](/dashboard/project/_/settings/api): your serverless API URL and `anon` / `service_role` keys.



## Launching a notebook

Launch our [`semantic_text_deduplication`](https://github.com/supabase/supabase/blob/master/examples/ai/face_similarity.ipynb) notebook in Colab:

<a className="w-64" href="https://colab.research.google.com/github/supabase/supabase/blob/master/examples/ai/face_similarity.ipynb">
  <img src="/docs/img/ai/colab-badge.svg" />
</a>

At the top of the notebook, you'll see a button `Copy to Drive`. Click this button to copy the notebook to your Google Drive.



## Connecting to your database

Inside the Notebook, find the cell which specifies the `DB_CONNECTION`. It will contain some code like this:

```python
import vecs

DB_CONNECTION = "postgresql://<user>:<password>@<host>:<port>/<db_name>"


# create vector store client
vx = vecs.create_client(DB_CONNECTION)
```

Replace the `DB_CONNECTION` with your own connection string. You can find the connection string on your project dashboard by clicking [Connect](/dashboard/project/_?showConnect=true).

<Admonition type="note">
  SQLAlchemy requires the connection string to start with `postgresql://` (instead of `postgres://`). Don't forget to rename this after copying the string from the dashboard.
</Admonition>

<Admonition type="note">
  You must use the "connection pooling" string (domain ending in `*.pooler.supabase.com`) with Google Colab since Colab does not support IPv6.
</Admonition>



## Stepping through the notebook

Now all that's left is to step through the notebook. You can do this by clicking the "execute" button (`ctrl+enter`) at the top left of each code cell. The notebook guides you through the process of creating a collection, adding data to it, and querying it.

You can view the inserted items in the [Table Editor](/dashboard/project/_/editor/), by selecting the `vecs` schema from the schema dropdown.

![Colab documents](/docs/img/ai/google-colab/colab-documents.png)



## Next steps

You can now start building your own applications with Vecs. Check our [examples](/docs/guides/ai#examples) for ideas.



# Generate Embeddings

Generate text embeddings using Edge Functions.

This guide will walk you through how to generate high quality text embeddings in [Edge Functions](/docs/guides/functions) using its built-in AI inference API, so no external API is required.



## Build the Edge Function

Let's build an Edge Function that will accept an input string and generate an embedding for it. Edge Functions are server-side TypeScript HTTP endpoints that run on-demand closest to your users.

<StepHikeCompact>
  <StepHikeCompact.Step step={1}>
    <StepHikeCompact.Details title="Set up Supabase locally">
      Make sure you have the latest version of the [Supabase CLI installed](/docs/guides/cli/getting-started).

      Initialize Supabase in the root directory of your app and start your local stack.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      ```shell
      supabase init
      supabase start
      ```
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={2}>
    <StepHikeCompact.Details title="Create Edge Function">
      Create an Edge Function that we will use to generate embeddings. We'll call this `embed` (you can name this anything you like).

      This will create a new TypeScript file called `index.ts` under `./supabase/functions/embed`.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      ```shell
      supabase functions new embed
      ```
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={3}>
    <StepHikeCompact.Details title="Setup Inference Session" fullWidth>
      Let's create a new inference session to be used in the lifetime of this function. Multiple requests can use the same inference session.

      Currently, only the `gte-small` ([https://huggingface.co/Supabase/gte-small](https://huggingface.co/Supabase/gte-small)) text embedding model is supported in Supabase's Edge Runtime.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      ```ts ./supabase/functions/embed/index.ts
      const session = new Supabase.ai.Session('gte-small');
      ```
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={4}>
    <StepHikeCompact.Details title="Implement request handler">
      Modify our request handler to accept an `input` string from the POST request JSON body.

      Then generate the embedding by calling `session.run(input)`.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      ```ts ./supabase/functions/embed/index.ts
      Deno.serve(async (req) => {
        // Extract input string from JSON body
        const { input } = await req.json();

        // Generate the embedding from the user input
        const embedding = await session.run(input, {
          mean_pool: true,
          normalize: true,
        });

        // Return the embedding
        return new Response(
          JSON.stringify({ embedding }),
          { headers: { 'Content-Type': 'application/json' } }
        );
      });
      ```
    </StepHikeCompact.Code>

    <StepHikeCompact.Details fullWidth>
      Note the two options we pass to `session.run()`:

      *   `mean_pool`: The first option sets `pooling` to `mean`. Pooling refers to how token-level embedding representations are compressed into a single sentence embedding that reflects the meaning of the entire sentence. Average pooling is the most common type of pooling for sentence embeddings.
      *   `normalize`: The second option tells to normalize the embedding vector so that it can be used with distance measures like dot product. A normalized vector means its length (magnitude) is 1 - also referred to as a unit vector. A vector is normalized by dividing each element by the vector's length (magnitude), which maintains its direction but changes its length to 1.
    </StepHikeCompact.Details>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={5}>
    <StepHikeCompact.Details title="Test it!">
      To test the Edge Function, first start a local functions server.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      ```shell
      supabase functions serve
      ```
    </StepHikeCompact.Code>

    <StepHikeCompact.Details fullWidth>
      Then in a new shell, create an HTTP request using cURL and pass in your input in the JSON body.

      ```shell
      curl --request POST 'http://localhost:54321/functions/v1/embed' \
        --header 'Authorization: Bearer ANON_KEY' \
        --header 'Content-Type: application/json' \
        --data '{ "input": "hello world" }'
      ```

      Be sure to replace `ANON_KEY` with your project's anonymous key. You can get this key by running `supabase status`.
    </StepHikeCompact.Details>
  </StepHikeCompact.Step>
</StepHikeCompact>



## Next steps

*   Learn more about [embedding concepts](/docs/guides/ai/concepts)
*   [Store your embeddings](/docs/guides/ai/vector-columns) in a database



# Creating and managing collections

Connecting to your database with Colab.

This guide will walk you through a basic ["Hello World"](https://github.com/supabase/supabase/blob/master/examples/ai/vector_hello_world.ipynb) example using Colab and Supabase Vecs. You'll learn how to:

1.  Launch a Postgres database that uses pgvector to store embeddings
2.  Launch a notebook that connects to your database
3.  Create a vector collection
4.  Add data to the collection
5.  Query the collection



## Project setup

Let's create a new Postgres database. This is as simple as starting a new Project in Supabase:

1.  [Create a new project](https://database.new/) in the Supabase dashboard.
2.  Enter your project details. Remember to store your password somewhere safe.

Your database will be available in less than a minute.

**Finding your credentials:**

You can find your project credentials on the dashboard:

*   [Database connection strings](/dashboard/project/_/settings/api?showConnect=true): Direct and Pooler connection details including the connection string and parameters.
*   [Database password](/dashboard/project/_/database/settings): Reset database password here if you do not have it.
*   [API credentials](/dashboard/project/_/settings/api): your serverless API URL and `anon` / `service_role` keys.



## Launching a notebook

Launch our [`vector_hello_world`](https://github.com/supabase/supabase/blob/master/examples/ai/vector_hello_world.ipynb) notebook in Colab:

<a className="w-64" href="https://colab.research.google.com/github/supabase/supabase/blob/master/examples/ai/vector_hello_world.ipynb">
  <img src="/docs/img/ai/colab-badge.svg" />
</a>

At the top of the notebook, you'll see a button `Copy to Drive`. Click this button to copy the notebook to your Google Drive.



## Connecting to your database

Inside the Notebook, find the cell which specifies the `DB_CONNECTION`. It will contain some code like this:

```python
import vecs

DB_CONNECTION = "postgresql://<user>:<password>@<host>:<port>/<db_name>"


# create vector store client
vx = vecs.create_client(DB_CONNECTION)
```

Replace the `DB_CONNECTION` with your Session pooler connection string. You can find the connection string on your project dashboard by clicking [Connect](/dashboard/project/_?showConnect=true).

<Admonition type="note">
  SQLAlchemy requires the connection string to start with `postgresql://` (instead of `postgres://`). Don't forget to rename this after copying the string from the dashboard.
</Admonition>

<Admonition type="note">
  You must use the Session pooler connection string with Google Colab since Colab does not support IPv6.
</Admonition>



## Stepping through the notebook

Now all that's left is to step through the notebook. You can do this by clicking the "execute" button (`ctrl+enter`) at the top left of each code cell. The notebook guides you through the process of creating a collection, adding data to it, and querying it.

You can view the inserted items in the [Table Editor](/dashboard/project/_/editor/), by selecting the `vecs` schema from the schema dropdown.

![Colab documents](/docs/img/ai/google-colab/colab-documents.png)



## Next steps

You can now start building your own applications with Vecs. Check our [examples](/docs/guides/ai#examples) for ideas.



# Semantic Text Deduplication

Finding duplicate movie reviews with Supabase Vecs.

This guide will walk you through a ["Semantic Text Deduplication"](https://github.com/supabase/supabase/blob/master/examples/ai/semantic_text_deduplication.ipynb) example using Colab and Supabase Vecs. You'll learn how to find similar movie reviews using embeddings, and remove any that seem like duplicates. You will:

1.  Launch a Postgres database that uses pgvector to store embeddings
2.  Launch a notebook that connects to your database
3.  Load the IMDB dataset
4.  Use the `sentence-transformers/all-MiniLM-L6-v2` model to create an embedding representing the semantic meaning of each review.
5.  Search for all duplicates.



## Project setup

Let's create a new Postgres database. This is as simple as starting a new Project in Supabase:

1.  [Create a new project](https://database.new/) in the Supabase dashboard.
2.  Enter your project details. Remember to store your password somewhere safe.

Your database will be available in less than a minute.

**Finding your credentials:**

You can find your project credentials on the dashboard:

*   [Database connection strings](/dashboard/project/_/settings/api?showConnect=true): Direct and Pooler connection details including the connection string and parameters.
*   [Database password](/dashboard/project/_/database/settings): Reset database password here if you do not have it.
*   [API credentials](/dashboard/project/_/settings/api): your serverless API URL and `anon` / `service_role` keys.



## Launching a notebook

Launch our [`semantic_text_deduplication`](https://github.com/supabase/supabase/blob/master/examples/ai/semantic_text_deduplication.ipynb) notebook in Colab:

<a className="w-64" href="https://colab.research.google.com/github/supabase/supabase/blob/master/examples/ai/semantic_text_deduplication.ipynb">
  <img src="/docs/img/ai/colab-badge.svg" />
</a>

At the top of the notebook, you'll see a button `Copy to Drive`. Click this button to copy the notebook to your Google Drive.



## Connecting to your database

Inside the Notebook, find the cell which specifies the `DB_CONNECTION`. It will contain some code like this:

```python
import vecs

DB_CONNECTION = "postgresql://<user>:<password>@<host>:<port>/<db_name>"


# create vector store client
vx = vecs.create_client(DB_CONNECTION)
```

Replace the `DB_CONNECTION` with your own connection string. You can find the connection string on your project dashboard by clicking [Connect](/dashboard/project/_?showConnect=true).

<Admonition type="note">
  SQLAlchemy requires the connection string to start with `postgresql://` (instead of `postgres://`). Don't forget to rename this after copying the string from the dashboard.
</Admonition>

<Admonition type="note">
  You must use the "connection pooling" string (domain ending in `*.pooler.supabase.com`) with Google Colab since Colab does not support IPv6.
</Admonition>



## Stepping through the notebook

Now all that's left is to step through the notebook. You can do this by clicking the "execute" button (`ctrl+enter`) at the top left of each code cell. The notebook guides you through the process of creating a collection, adding data to it, and querying it.

You can view the inserted items in the [Table Editor](/dashboard/project/_/editor/), by selecting the `vecs` schema from the schema dropdown.

![Colab documents](/docs/img/ai/google-colab/colab-documents.png)



## Deployment

If you have your own infrastructure for deploying Python apps, you can continue to use `vecs` as described in this guide.

Alternatively if you would like to quickly deploy using Supabase, check out our guide on using the [Hugging Face Inference API](/docs/guides/ai/hugging-face) in Edge Functions using TypeScript.



## Next steps

You can now start building your own applications with Vecs. Check our [examples](/docs/guides/ai#examples) for ideas.



# Amazon Bedrock



[Amazon Bedrock](https://aws.amazon.com/bedrock) is a fully managed service that offers a choice of high-performing foundation models (FMs) from leading AI companies like AI21 Labs, Anthropic, Cohere, Meta, Mistral AI, Stability AI, and Amazon. Each model is accessible through a common API which implements a broad set of features to help build generative AI applications with security, privacy, and responsible AI in mind.

This guide will walk you through an example using Amazon Bedrock SDK with `vecs`. We will create embeddings using the Amazon Titan Embeddings G1 – Text v1.2 (amazon.titan-embed-text-v1) model, insert these embeddings into a Postgres database using vecs, and then query the collection to find the most similar sentences to a given query sentence.



## Create an environment

First, you need to set up your environment. You will need Python 3.7+ with the `vecs` and `boto3` libraries installed.

You can install the necessary Python libraries using pip:

```sh
pip install vecs boto3
```

You'll also need:

*   [Credentials to your AWS account](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html)
*   [A Postgres Database with the pgvector extension](hosting.md)



## Create embeddings

Next, we will use Amazon’s Titan Embedding G1 - Text v1.2 model to create embeddings for a set of sentences.

```python
import boto3
import vecs
import json

client = boto3.client(
    'bedrock-runtime',
    region_name='us-east-1',
	# Credentials from your AWS account
    aws_access_key_id='<replace_your_own_credentials>',
    aws_secret_access_key='<replace_your_own_credentials>',
    aws_session_token='<replace_your_own_credentials>',
)

dataset = [
    "The cat sat on the mat.",
    "The quick brown fox jumps over the lazy dog.",
    "Friends, Romans, countrymen, lend me your ears",
    "To be or not to be, that is the question.",
]

embeddings = []

for sentence in dataset:
    # invoke the embeddings model for each sentence
    response = client.invoke_model(
        body= json.dumps({"inputText": sentence}),
        modelId= "amazon.titan-embed-text-v1",
        accept = "application/json",
        contentType = "application/json"
    )
    # collect the embedding from the response
    response_body = json.loads(response["body"].read())
    # add the embedding to the embedding list
    embeddings.append((sentence, response_body.get("embedding"), {}))

```


### Store the embeddings with vecs

Now that we have our embeddings, we can insert them into a Postgres database using vecs.

```python
import vecs

DB_CONNECTION = "postgresql://<user>:<password>@<host>:<port>/<db_name>"


# create vector store client
vx = vecs.Client(DB_CONNECTION)


# create a collection named 'sentences' with 1536 dimensional vectors

# to match the default dimension of the Titan Embeddings G1 - Text model
sentences = vx.get_or_create_collection(name="sentences", dimension=1536)


# upsert the embeddings into the 'sentences' collection
sentences.upsert(records=embeddings)


# create an index for the 'sentences' collection
sentences.create_index()
```


### Querying for most similar sentences

Now, we query the `sentences` collection to find the most similar sentences to a sample query sentence. First need to create an embedding for the query sentence. Next, we query the collection we created earlier to find the most similar sentences.

```python
query_sentence = "A quick animal jumps over a lazy one."


# create vector store client
vx = vecs.Client(DB_CONNECTION)


# create an embedding for the query sentence
response = client.invoke_model(
        body= json.dumps({"inputText": query_sentence}),
        modelId= "amazon.titan-embed-text-v1",
        accept = "application/json",
        contentType = "application/json"
    )

response_body = json.loads(response["body"].read())

query_embedding = response_body.get("embedding")


# query the 'sentences' collection for the most similar sentences
results = sentences.query(
    data=query_embedding,
    limit=3,
    include_value = True
)


# print the results
for result in results:
    print(result)
```

This returns the most similar 3 records and their distance to the query vector.

```
('The quick brown fox jumps over the lazy dog.', 0.27600620558852)
('The cat sat on the mat.', 0.609986272479202)
('To be or not to be, that is the question.', 0.744849503688346)
```



## Resources

*   [Amazon Bedrock](https://aws.amazon.com/bedrock)
*   [Amazon Titan](https://aws.amazon.com/bedrock/titan)
*   [Semantic Image Search with Amazon Titan](/docs/guides/ai/examples/semantic-image-search-amazon-titan)



# Learn how to integrate Supabase with LlamaIndex, a data framework for your LLM applications.

Learn how to integrate Supabase with LlamaIndex, a data framework for your LLM applications.

This guide will walk you through a basic example using the LlamaIndex [`SupabaseVectorStore`](https://github.com/supabase/supabase/blob/master/examples/ai/llamaindex/llamaindex.ipynb).



## Project setup

Let's create a new Postgres database. This is as simple as starting a new Project in Supabase:

1.  [Create a new project](https://database.new/) in the Supabase dashboard.
2.  Enter your project details. Remember to store your password somewhere safe.

Your database will be available in less than a minute.

**Finding your credentials:**

You can find your project credentials on the dashboard:

*   [Database connection strings](/dashboard/project/_/settings/api?showConnect=true): Direct and Pooler connection details including the connection string and parameters.
*   [Database password](/dashboard/project/_/database/settings): Reset database password here if you do not have it.
*   [API credentials](/dashboard/project/_/settings/api): your serverless API URL and `anon` / `service_role` keys.



## Launching a notebook

Launch our [LlamaIndex](https://github.com/supabase/supabase/blob/master/examples/ai/llamaindex/llamaindex.ipynb) notebook in Colab:

<a className="w-64" href="https://colab.research.google.com/github/supabase/supabase/blob/master/examples/ai/llamaindex/llamaindex.ipynb">
  <img src="/docs/img/ai/colab-badge.svg" />
</a>

At the top of the notebook, you'll see a button `Copy to Drive`. Click this button to copy the notebook to your Google Drive.



## Fill in your OpenAI credentials

Inside the Notebook, add your `OPENAI_API_KEY` key. Find the cell which contains this code:

```py
import os
os.environ['OPENAI_API_KEY'] = "[your_openai_api_key]"
```



## Connecting to your database

Inside the Notebook, find the cell which specifies the `DB_CONNECTION`. It will contain some code like this:

```python
DB_CONNECTION = "postgresql://<user>:<password>@<host>:<port>/<db_name>"


# create vector store client
vx = vecs.create_client(DB_CONNECTION)
```

Replace the `DB_CONNECTION` with your own connection string. You can find the connection string on your project dashboard by clicking [Connect](/dashboard/project/_?showConnect=true).

<Admonition type="note">
  SQLAlchemy requires the connection string to start with `postgresql://` (instead of `postgres://`). Don't forget to rename this after copying the string from the dashboard.
</Admonition>

<Admonition type="note">
  You must use the "connection pooling" string (domain ending in `*.pooler.supabase.com`) with Google Colab since Colab does not support IPv6.
</Admonition>



## Stepping through the notebook

Now all that's left is to step through the notebook. You can do this by clicking the "execute" button (`ctrl+enter`) at the top left of each code cell. The notebook guides you through the process of creating a collection, adding data to it, and querying it.

You can view the inserted items in the [Table Editor](/dashboard/project/_/editor/), by selecting the `vecs` schema from the schema dropdown.

![Colab documents](/docs/img/ai/google-colab/colab-documents.png)



## Resources

*   Visit the LlamaIndex + `SupabaseVectorStore` [docs](https://gpt-index.readthedocs.io/en/latest/examples/vector_stores/SupabaseVectorIndexDemo.html)
*   Visit the official LlamaIndex [repo](https://github.com/jerryjliu/llama_index/)



# Roboflow

Learn how to integrate Supabase with Roboflow, a tool for running fine-tuned and foundation vision models.

In this guide, we will walk through two examples of using [Roboflow Inference](https://inference.roboflow.com) to run fine-tuned and foundation models. We will run inference and save predictions using an object detection model and [CLIP](https://github.com/openai/CLIP).



## Project setup

Let's create a new Postgres database. This is as simple as starting a new Project in Supabase:

1.  [Create a new project](https://database.new/) in the Supabase dashboard.
2.  Enter your project details. Remember to store your password somewhere safe.

Your database will be available in less than a minute.

**Finding your credentials:**

You can find your project credentials on the dashboard:

*   [Database connection strings](/dashboard/project/_/settings/api?showConnect=true): Direct and Pooler connection details including the connection string and parameters.
*   [Database password](/dashboard/project/_/database/settings): Reset database password here if you do not have it.
*   [API credentials](/dashboard/project/_/settings/api): your serverless API URL and `anon` / `service_role` keys.



## Save computer vision predictions

Once you have a trained vision model, you need to create business logic for your application. In many cases, you want to save inference results to a file.

The steps below show you how to run a vision model locally and save predictions to Supabase.


### Preparation: Set up a model

Before you begin, you will need an object detection model trained on your data.

You can [train a model on Roboflow](https://blog.roboflow.com/getting-started-with-roboflow/), leveraging end-to-end tools from data management and annotation to deployment, or [upload custom model weights](https://docs.roboflow.com/deploy/upload-custom-weights) for deployment.

All models have an infinitely scalable API through which you can query your model, and can be run locally.

For this guide, we will use a demo [rock, paper, scissors](https://universe.roboflow.com/roboflow-58fyf/rock-paper-scissors-sxsw) model.


### Step 1: Install and start Roboflow Inference

You will deploy our model locally using Roboflow Inference, a computer vision inference server.

To install and start Roboflow Inference, first install Docker on your machine.

Then, run:

```
pip install inference inference-cli inference-sdk && inference server start
```

An inference server will be available at `http://localhost:9001`.


### Step 2: Run inference on an image

You can run inference on images and videos. Let's run inference on an image.

Create a new Python file and add the following code:

```python
from inference_sdk import InferenceHTTPClient

image = "example.jpg"
MODEL_ID = "rock-paper-scissors-sxsw/11"

client = InferenceHTTPClient(
    api_url="http://localhost:9001",
    api_key="ROBOFLOW_API_KEY"
)
with client.use_model(MODEL_ID):
    predictions = client.infer(image)

print(predictions)
```

Above, replace:

1.  The image URL with the name of the image on which you want to run inference.
2.  `ROBOFLOW_API_KEY` with your Roboflow API key. [Learn how to retrieve your Roboflow API key](https://docs.roboflow.com/api-reference/authentication#retrieve-an-api-key).
3.  `MODEL_ID` with your Roboflow model ID. [Learn how to retrieve your model ID](https://docs.roboflow.com/api-reference/workspace-and-project-ids).

When you run the code above, a list of predictions will be printed to the console:

```
{'time': 0.05402109300121083, 'image': {'width': 640, 'height': 480}, 'predictions': [{'x': 312.5, 'y': 392.0, 'width': 255.0, 'height': 110.0, 'confidence': 0.8620790839195251, 'class': 'Paper', 'class_id': 0}]}
```


### Step 3: Save results in Supabase

To save results in Supabase, add the following code to your script:

```python
import os
from supabase import create_client, Client

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

result = supabase.table('predictions') \
    .insert({"filename": image, "predictions": predictions}) \
    .execute()
```

You can then query your predictions using the following code:

```python
result = supabase.table('predictions') \
    .select("predictions") \
    .filter("filename", "eq", image) \
    .execute()

print(result)
```

Here is an example result:

```
data=[{'predictions': {'time': 0.08492901099998562, 'image': {'width': 640, 'height': 480}, 'predictions': [{'x': 312.5, 'y': 392.0, 'width': 255.0, 'height': 110.0, 'confidence': 0.8620790839195251, 'class': 'Paper', 'class_id': 0}]}}, {'predictions': {'time': 0.08818970100037404, 'image': {'width': 640, 'height': 480}, 'predictions': [{'x': 312.5, 'y': 392.0, 'width': 255.0, 'height': 110.0, 'confidence': 0.8620790839195251, 'class': 'Paper', 'class_id': 0}]}}] count=None
```



## Calculate and save CLIP embeddings

You can use the Supabase vector database functionality to store and query CLIP embeddings.

Roboflow Inference provides a HTTP interface through which you can calculate image and text embeddings using CLIP.


### Step 1: Install and start Roboflow Inference

See [Step #1: Install and Start Roboflow Inference](#step-1-install-and-start-roboflow-inference) above to install and start Roboflow Inference.


### Step 2: Run CLIP on an image

Create a new Python file and add the following code:

```python
import cv2
import supervision as sv
import requests
import base64
import os

IMAGE_DIR = "images/train/images/"
API_KEY = ""
SERVER_URL = "http://localhost:9001"

results = []

for i, image in enumerate(os.listdir(IMAGE_DIR)):
    print(f"Processing image {image}")
    infer_clip_payload = {
        "image": {
            "type": "base64",
            "value": base64.b64encode(open(IMAGE_DIR + image, "rb").read()).decode("utf-8"),
        },
    }

    res = requests.post(
        f"{SERVER_URL}/clip/embed_image?api_key={API_KEY}",
        json=infer_clip_payload,
    )

    embeddings = res.json()['embeddings']

    results.append({
        "filename": image,
        "embeddings": embeddings
    })
```

This code will calculate CLIP embeddings for each image in the directory and print the results to the console.

Above, replace:

1.  `IMAGE_DIR` with the directory containing the images on which you want to run inference.
2.  `ROBOFLOW_API_KEY` with your Roboflow API key. [Learn how to retrieve your Roboflow API key](https://docs.roboflow.com/api-reference/authentication#retrieve-an-api-key).

You can also calculate CLIP embeddings in the cloud by setting `SERVER_URL` to `https://infer.roboflow.com`.


### Step 3: Save embeddings in Supabase

You can store your image embeddings in Supabase using the Supabase `vecs` Python package:

First, install `vecs`:

```
pip install vecs
```

Next, add the following code to your script to create an index:

```python

import vecs

DB_CONNECTION = "postgresql://postgres:[password]@[host]:[port]/[database]"

vx = vecs.create_client(DB_CONNECTION)


# create a collection of vectors with 3 dimensions
images = vx.get_or_create_collection(name="image_vectors", dimension=512)

for result in results:
    image = result["filename"]
    embeddings = result["embeddings"][0]

    # insert a vector into the collection
    images.upsert(
        records=[
            (
                image,
                embeddings,
                {} # metadata
            )
        ]
    )

images.create_index()
```

Replace `DB_CONNECTION` with the authentication information for your database. You can retrieve this from the Supabase dashboard in `Project Settings > Database Settings`.

You can then query your embeddings using the following code:

```python
infer_clip_payload = {
    "text": "cat",
}

res = requests.post(
    f"{SERVER_URL}/clip/embed_text?api_key={API_KEY}",
    json=infer_clip_payload,
)

embeddings = res.json()['embeddings']

result = images.query(
    data=embeddings[0],
    limit=1
)

print(result[0])
```



## Resources

*   [Roboflow Inference documentation](https://inference.roboflow.com)
*   [Roboflow Getting Started guide](https://blog.roboflow.com/getting-started-with-roboflow/)
*   [How to Build a Semantic Image Search Engine with Supabase and OpenAI CLIP](https://blog.roboflow.com/how-to-use-semantic-search-supabase-openai-clip/)



# Building ChatGPT plugins

Use Supabase as a Retrieval Store for your ChatGPT plugin.

ChatGPT recently released [Plugins](https://openai.com/blog/chatgpt-plugins) which help ChatGPT access up-to-date information, run computations, or use third-party services.
If you're building a plugin for ChatGPT, you'll probably want to answer questions from a specific source. We can solve this with “retrieval plugins”, which allow ChatGPT to access information from a database.



## What is ChatGPT Retrieval Plugin?

A [Retrieval Plugin](https://github.com/openai/chatgpt-retrieval-plugin) is a Python project designed to inject external data into a ChatGPT conversation. It does a few things:

1.  Turn documents into smaller chunks.
2.  Converts chunks into embeddings using OpenAI's `text-embedding-ada-002` model.
3.  Stores the embeddings into a vector database.
4.  Queries the vector database for relevant documents when a question is asked.

It allows ChatGPT to dynamically pull relevant information into conversations from your data sources. This could be PDF documents, Confluence, or Notion knowledge bases.



## Example: Chat with Postgres docs

Let’s build an example where we can “ask ChatGPT questions” about the Postgres documentation. Although ChatGPT already knows about the Postgres documentation because it is publicly available, this is a simple example which demonstrates how to work with PDF files.

This plugin requires several steps:

1.  Download all the [Postgres docs as a PDF](https://www.postgresql.org/files/documentation/pdf/15/postgresql-15-US.pdf)
2.  Convert the docs into chunks of embedded text and store them in Supabase
3.  Run our plugin locally so that we can ask questions about the Postgres docs.

We'll be saving the Postgres documentation in Postgres, and ChatGPT will be retrieving the documentation whenever a user asks a question:

<Image
  alt="diagram reference"
  className="max-h-[600px]"
  src={{
    light: '/docs/img/ai/chatgpt-plugins/chatgpt-plugin-scheme--light.png',
    dark: '/docs/img/ai/chatgpt-plugins/chatgpt-plugin-scheme--dark.png',
  }}
  zoomable
/>


### Step 1: Fork the ChatGPT Retrieval Plugin repository

Fork the ChatGPT Retrieval Plugin repository to your GitHub account and clone it to your local machine. Read through the `README.md` file to understand the project structure.


### Step 2: Install dependencies

Choose your desired datastore provider and remove unused dependencies from `pyproject.toml`. For this example, we'll use Supabase. And install dependencies with Poetry:

```bash
poetry install
```


### Step 3: Create a Supabase project

Create a [Supabase project](/dashboard) and database by following the instructions [here](/docs/guides/platform). Export the environment variables required for the retrieval plugin to work:

```bash
export OPENAI_API_KEY=<open_ai_api_key>
export DATASTORE=supabase
export SUPABASE_URL=<supabase_url>
export SUPABASE_SERVICE_ROLE_KEY=<supabase_key>
```

For Postgres datastore, you'll need to export these environment variables instead:

```bash
export OPENAI_API_KEY=<open_ai_api_key>
export DATASTORE=postgres
export PG_HOST=<postgres_host_url>
export PG_PASSWORD=<postgres_password>
```


### Step 4: Run Postgres locally

To start quicker you may use Supabase CLI to spin everything up locally as it already includes pgvector from the start. Install `supabase-cli`, go to the `examples/providers` folder in the repo and run:

```bash
supabase start
```

This will pull all docker images and run Supabase stack in docker on your local machine. It will also apply all the necessary migrations to set the whole thing up. You can then use your local setup the same way, just export the environment variables and follow to the next steps.

Using `supabase-cli` is not required and you can use any other docker image or hosted version of Postgres that includes `pgvector`. Just make sure you run migrations from `examples/providers/supabase/migrations/20230414142107_init_pg_vector.sql`.


### Step 5: Obtain OpenAI API key

To create embeddings Plugin uses OpenAI API and `text-embedding-ada-002` model. Each time we add some data to our datastore, or try to query relevant information from it, embedding will be created either for inserted data chunk, or for the query itself. To make it work we need to export `OPENAI_API_KEY`. If you already have an account in OpenAI, you just need to go to [User Settings - API keys](https://platform.openai.com/account/api-keys) and Create new secret key.

![OpenAI Secret Keys](/docs/img/ai/chatgpt-plugins/openai-secret-keys.png)


### Step 6: Run the plugin

Execute the following command to run the plugin:

```bash
poetry run dev

# output
INFO:     Will watch for changes in these directories: ['./chatgpt-retrieval-plugin']
INFO:     Uvicorn running on http://localhost:3333 (Press CTRL+C to quit)
INFO:     Started reloader process [87843] using WatchFiles
INFO:     Started server process [87849]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

The plugin will start on your localhost - port `:3333` by default.


### Step 6: Populating data in the datastore

For this example, we'll upload Postgres documentation to the datastore. Download the [Postgres documentation](https://www.postgresql.org/files/documentation/pdf/15/postgresql-15-US.pdf) and use the `/upsert-file` endpoint to upload it:

```bash
curl -X POST -F \\"file=@./postgresql-15-US.pdf\\" <http://localhost:3333/upsert-file>
```

The plugin will split your data and documents into smaller chunks automatically. You can view the chunks using the Supabase dashboard or any other SQL client you prefer. The entire Postgres Documentation yielded 7,904 records, which is not a lot, but we can try to add index for `embedding` column to speed things up by a little. To do so, you should run the following SQL command:

```sql
create index on documents
using hnsw (embedding vector_ip_ops)
with (lists = 10);
```

This will create an index for the inner product distance function. Important to note that it is an approximate index. It will change the logic from performing the exact nearest neighbor search to the approximate nearest neighbor search.

We are using `lists = 10`, because as a general guideline, you should start looking for optimal lists constant value with the formula: `rows / 1000` when you have less than 1 million records in your table.


### Step 7: Using our plugin within ChatGPT

To integrate our plugin with ChatGPT, register it in the ChatGPT dashboard. Assuming you have access to ChatGPT Plugins and plugin development, select the Plugins model in a new chat, then choose "Plugin store" and "Develop your own plugin." Enter `localhost:3333` into the domain input, and your plugin is now part of ChatGPT.

![ChatGPT Plugin Store](/docs/img/ai/chatgpt-plugins/chatgpt-plugin-store.png)

![ChatGPT Local Plugin](/docs/img/ai/chatgpt-plugins/chatgpt-local-plugin.png)

You can now ask questions about Postgres and receive answers derived from the documentation.

Let's try it out: ask ChatGPT to find out when to use `check` and when to use `using`. You will be able to see what queries were sent to our plugin and what it responded to.

![Ask ChatGPT](/docs/img/ai/chatgpt-plugins/ask-chatgpt.png)

And after ChatGPT receives a response from the plugin it will answer your question with the data from the documentation.

![ChatGPT Reply](/docs/img/ai/chatgpt-plugins/chatgpt-reply.png)



## Resources

*   ChatGPT Retrieval Plugin: [github.com/openai/chatgpt-retrieval-plugin](https://github.com/openai/chatgpt-retrieval-plugin)
*   ChatGPT Plugins: [official documentation](https://platform.openai.com/docs/plugins/introduction)



# Adding generative Q&A for your documentation

Learn how to build a ChatGPT-style doc search powered using our headless search toolkit.

Supabase provides a [Headless Search Toolkit](https://github.com/supabase/headless-vector-search) for adding "Generative Q\&A" to your documentation. The toolkit is "headless", so that you can integrate it into your existing website and style it to match your website theme.

You can see how this works with the Supabase docs. Just hit `cmd+k` and "ask" for something like "what are the features of Supabase?". You will see that the response is streamed back, using the information provided in the docs:

![headless search](/docs/img/ai/headless-search/headless.png)



## Tech stack

*   Supabase: Database & Edge Functions.
*   OpenAI: Embeddings and completions.
*   GitHub Actions: for ingesting your markdown docs.



## Toolkit

This toolkit consists of 2 parts:

*   The [Headless Vector Search](https://github.com/supabase/headless-vector-search) template which you can deploy in your own organization.
*   A [GitHub Action](https://github.com/supabase/embeddings-generator) which will ingest your markdown files, convert them to embeddings, and store them in your database.



## Usage

There are 3 steps to build similarity search inside your documentation:

1.  Prepare your database.
2.  Ingest your documentation.
3.  Add a search interface.


### Prepare your database

To prepare, create a [new Supabase project](https://database.new) and store the database and API credentials, which you can find in the project [settings](/dashboard/project/_/settings).

Now we can use the [Headless Vector Search](https://github.com/supabase/headless-vector-search#set-up) instructions to set up the database:

1.  Clone the repo to your local machine: `git clone git@github.com:supabase/headless-vector-search.git`
2.  Link the repo to your remote project: `supabase link --project-ref XXX`
3.  Apply the database migrations: `supabase db push`
4.  Set your OpenAI key as a secret: `supabase secrets set OPENAI_API_KEY=sk-xxx`
5.  Deploy the Edge Functions: `supabase functions deploy --no-verify-jwt`
6.  Expose `docs` schema via API in Supabase Dashboard [settings](/dashboard/project/_/settings/api) > `API Settings` > `Exposed schemas`


### Ingest your documentation

Now we need to push your documentation into the database as embeddings. You can do this manually, but to make it easier we've created a [GitHub Action](https://github.com/marketplace/actions/supabase-embeddings-generator) which can update your database every time there is a Pull Request.

In your knowledge base repository, create a new action called `.github/workflows/generate_embeddings.yml` with the following content:

```yml
name: 'generate_embeddings'
on: # run on main branch changes
  push:
    branches:
      - main

jobs:
  generate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: supabase/embeddings-generator@v0.0.x # Update this to the latest version.
        with:
          supabase-url: 'https://your-project-ref.supabase.co' # Update this to your project URL.
          supabase-service-role-key: ${{ secrets.SUPABASE_SERVICE_ROLE_KEY }}
          openai-key: ${{ secrets.OPENAI_API_KEY }}
          docs-root-path: 'docs' # the path to the root of your md(x) files
```

Make sure to choose the latest version, and set your `SUPABASE_SERVICE_ROLE_KEY` and `OPENAI_API_KEY` as repository secrets in your repo settings (settings > secrets > actions).


### Add a search interface

Now inside your docs, you need to create a search interface. Because this is a headless interface, you can use it with any language. The only requirement is that you send the user query to the `query` Edge Function, which will stream an answer back from OpenAI. It might look something like this:

```js
const onSubmit = (e: Event) => {
  e.preventDefault()
  answer.value = ""
  isLoading.value = true

  const query = new URLSearchParams({ query: inputRef.current!.value })
  const projectUrl = `https://your-project-ref.supabase.co/functions/v1`
  const queryURL = `${projectURL}/${query}`
  const eventSource = new EventSource(queryURL)

  eventSource.addEventListener("error", (err) => {
    isLoading.value = false
    console.error(err)
  })

  eventSource.addEventListener("message", (e: MessageEvent) => {
    isLoading.value = false

    if (e.data === "[DONE]") {
      eventSource.close()
      return
    }

    const completionResponse: CreateCompletionResponse = JSON.parse(e.data)
    const text = completionResponse.choices[0].text

    answer.value += text
  });

  isLoading.value = true
}
```



## Resources

*   Read about how we built [ChatGPT for the Supabase Docs](/blog/chatgpt-supabase-docs).
*   Read the pgvector Docs for [Embeddings and vector similarity](/docs/guides/database/extensions/pgvector)
*   See how to build something like this from scratch [using Next.js](/docs/guides/ai/examples/nextjs-vector-search).



# Generate image captions using Hugging Face

Use the Hugging Face Inference API to make calls to 100,000+ Machine Learning models from Supabase Edge Functions.

We can combine Hugging Face with [Supabase Storage](/storage) and [Database Webhooks](/docs/guides/database/webhooks) to automatically caption for any image we upload to a storage bucket.



## About Hugging Face

[Hugging Face](https://huggingface.co/) is the collaboration platform for the machine learning community.

[Huggingface.js](https://huggingface.co/docs/huggingface.js/index) provides a convenient way to make calls to 100,000+ Machine Learning models, making it easy to incorporate AI functionality into your [Supabase Edge Functions](/edge-functions).



## Setup

*   Open your Supabase project dashboard or [create a new project](/dashboard/projects).
*   [Create a new bucket](/dashboard/project/_/storage/buckets) called `images`.
*   Generate TypeScript types from remote Database.
*   Create a new Database table called `image_caption`.
    *   Create `id` column of type `uuid` which references `storage.objects.id`.
    *   Create a `caption` column of type `text`.
*   Regenerate TypeScript types to include new `image_caption` table.
*   Deploy the function to Supabase: `supabase functions deploy huggingface-image-captioning`.
*   Create the Database Webhook in the [Supabase Dashboard](/dashboard/project/_/database/hooks) to trigger the `huggingface-image-captioning` function anytime a record is added to the `storage.objects` table.



## Generate TypeScript types

To generate the types.ts file for the storage and public schemas, run the following command in the terminal:

```bash
supabase gen types typescript --project-id=your-project-ref --schema=storage,public > supabase/functions/huggingface-image-captioning/types.ts
```



## Code

Find the complete code on [GitHub](https://github.com/supabase/supabase/tree/master/examples/edge-functions/supabase/functions/huggingface-image-captioning).

```ts
import { serve } from 'https://deno.land/std@0.168.0/http/server.ts'
import { HfInference } from 'https://esm.sh/@huggingface/inference@2.3.2'
import { createClient } from 'npm:@supabase/supabase-js@2'
import { Database } from './types.ts'

console.log('Hello from `huggingface-image-captioning` function!')

const hf = new HfInference(Deno.env.get('HUGGINGFACE_ACCESS_TOKEN'))

type SoRecord = Database['storage']['Tables']['objects']['Row']
interface WebhookPayload {
  type: 'INSERT' | 'UPDATE' | 'DELETE'
  table: string
  record: SoRecord
  schema: 'public'
  old_record: null | SoRecord
}

serve(async (req) => {
  const payload: WebhookPayload = await req.json()
  const soRecord = payload.record
  const supabaseAdminClient = createClient<Database>(
    // Supabase API URL - env var exported by default when deployed.
    Deno.env.get('SUPABASE_URL') ?? '',
    // Supabase API SERVICE ROLE KEY - env var exported by default when deployed.
    Deno.env.get('SUPABASE_SERVICE_ROLE_KEY') ?? ''
  )

  // Construct image url from storage
  const { data, error } = await supabaseAdminClient.storage
    .from(soRecord.bucket_id!)
    .createSignedUrl(soRecord.path_tokens!.join('/'), 60)
  if (error) throw error
  const { signedUrl } = data

  // Run image captioning with Huggingface
  const imgDesc = await hf.imageToText({
    data: await (await fetch(signedUrl)).blob(),
    model: 'nlpconnect/vit-gpt2-image-captioning',
  })

  // Store image caption in Database table
  await supabaseAdminClient
    .from('image_caption')
    .insert({ id: soRecord.id!, caption: imgDesc.generated_text })
    .throwOnError()

  return new Response('ok')
})
```



# Image Search with OpenAI CLIP

Implement image search with the OpenAI CLIP Model and Supabase Vector.

The [OpenAI CLIP Model](https://github.com/openai/CLIP) was trained on a variety of (image, text)-pairs. You can use the CLIP model for:

*   Text-to-Image / Image-To-Text / Image-to-Image / Text-to-Text Search
*   You can fine-tune it on your own image and text data with the regular `SentenceTransformers` training code.

[`SentenceTransformers`](https://www.sbert.net/examples/applications/image-search/README.html) provides models that allow you to embed images and text into the same vector space. You can use this to find similar images as well as to implement image search.

You can find the full application code as a Python Poetry project on [GitHub](https://github.com/supabase/supabase/tree/master/examples/ai/image_search#image-search-with-supabase-vector).



## Create a new Python project with Poetry

[Poetry](https://python-poetry.org/) provides packaging and dependency management for Python. If you haven't already, install poetry via pip:

```shell
pip install poetry
```

Then initialize a new project:

```shell
poetry new image-search
```



## Setup Supabase project

If you haven't already, [install the Supabase CLI](/docs/guides/cli), then initialize Supabase in the root of your newly created poetry project:

```shell
supabase init
```

Next, start your local Supabase stack:

```shell
supabase start
```

This will start up the Supabase stack locally and print out a bunch of environment details, including your local `DB URL`. Make a note of that for later user.



## Install the dependencies

We will need to add the following dependencies to our project:

*   [`vecs`](https://github.com/supabase/vecs#vecs): Supabase Vector Python Client.
*   [`sentence-transformers`](https://huggingface.co/sentence-transformers/clip-ViT-B-32): a framework for sentence, text and image embeddings (used with OpenAI CLIP model)
*   [`matplotlib`](https://matplotlib.org/): for displaying our image result

```shell
poetry add vecs sentence-transformers matplotlib
```



## Import the necessary dependencies

At the top of your main python script, import the dependencies and store your `DB URL` from above in a variable:

```python
from PIL import Image
from sentence_transformers import SentenceTransformer
import vecs
from matplotlib import pyplot as plt
from matplotlib import image as mpimg

DB_CONNECTION = "postgresql://postgres:postgres@localhost:54322/postgres"
```



## Create embeddings for your images

In the root of your project, create a new folder called `images` and add some images. You can use the images from the example project on [GitHub](https://github.com/supabase/supabase/tree/master/examples/ai/image_search/images) or you can find license free images on [Unsplash](https://unsplash.com).

Next, create a `seed` method, which will create a new Supabase Vector Collection, generate embeddings for your images, and upsert the embeddings into your database:

```python
def seed():
    # create vector store client
    vx = vecs.create_client(DB_CONNECTION)

    # create a collection of vectors with 3 dimensions
    images = vx.get_or_create_collection(name="image_vectors", dimension=512)

    # Load CLIP model
    model = SentenceTransformer('clip-ViT-B-32')

    # Encode an image:
    img_emb1 = model.encode(Image.open('./images/one.jpg'))
    img_emb2 = model.encode(Image.open('./images/two.jpg'))
    img_emb3 = model.encode(Image.open('./images/three.jpg'))
    img_emb4 = model.encode(Image.open('./images/four.jpg'))

    # add records to the *images* collection
    images.upsert(
        records=[
            (
                "one.jpg",        # the vector's identifier
                img_emb1,          # the vector. list or np.array
                {"type": "jpg"}   # associated  metadata
            ), (
                "two.jpg",
                img_emb2,
                {"type": "jpg"}
            ), (
                "three.jpg",
                img_emb3,
                {"type": "jpg"}
            ), (
                "four.jpg",
                img_emb4,
                {"type": "jpg"}
            )
        ]
    )
    print("Inserted images")

    # index the collection for fast search performance
    images.create_index()
    print("Created index")
```

Add this method as a script in your `pyproject.toml` file:

```toml
[tool.poetry.scripts]
seed = "image_search.main:seed"
search = "image_search.main:search"
```

After activating the virtual environment with `poetry shell` you can now run your seed script via `poetry run seed`. You can inspect the generated embeddings in your local database by visiting the local Supabase dashboard at [localhost:54323](http://localhost:54323/project/default/editor), selecting the `vecs` schema, and the `image_vectors` database.



## Perform an image search from a text query

With Supabase Vector we can query our embeddings. We can use either an image as search input or alternative we can generate an embedding from a string input and use that as the query input:

```python
def search():
    # create vector store client
    vx = vecs.create_client(DB_CONNECTION)
    images = vx.get_or_create_collection(name="image_vectors", dimension=512)

    # Load CLIP model
    model = SentenceTransformer('clip-ViT-B-32')
    # Encode text query
    query_string = "a bike in front of a red brick wall"
    text_emb = model.encode(query_string)

    # query the collection filtering metadata for "type" = "jpg"
    results = images.query(
        data=text_emb,                      # required
        limit=1,                            # number of records to return
        filters={"type": {"$eq": "jpg"}},   # metadata filters
    )
    result = results[0]
    print(result)
    plt.title(result)
    image = mpimg.imread('./images/' + result)
    plt.imshow(image)
    plt.show()
```

By limiting the query to one result, we can show the most relevant image to the user. Finally we use `matplotlib` to show the image result to the user.

Go ahead and test it out by running `poetry run search` and you will be presented with an image of a "bike in front of a red brick wall".



## Conclusion

With just a couple of lines of Python you are able to implement image search as well as reverse image search using OpenAI's CLIP model and Supabase Vector.



# Video Search with Mixpeek Multimodal Embeddings

Implement video search with the Mixpeek Multimodal Embed API and Supabase Vector.

The [Mixpeek Embed API](https://docs.mixpeek.com/api-documentation/inference/embed) allows you to generate embeddings for various types of content, including videos and text. You can use these embeddings for:

*   Text-to-Video / Video-To-Text / Video-to-Video / Text-to-Text Search
*   Fine-tuning on your own video and text data

This guide demonstrates how to implement video search using Mixpeek Embed for video processing and embedding, and Supabase Vector for storing and querying embeddings.

You can find the full application code as a Python Poetry project on [GitHub](https://github.com/yourusername/your-repo-name).



## Create a new Python project with Poetry

[Poetry](https://python-poetry.org/) provides packaging and dependency management for Python. If you haven't already, install poetry via pip:

```shell
pip install poetry
```

Then initialize a new project:

```shell
poetry new video-search
```



## Setup Supabase project

If you haven't already, [install the Supabase CLI](/docs/guides/cli), then initialize Supabase in the root of your newly created poetry project:

```shell
supabase init
```

Next, start your local Supabase stack:

```shell
supabase start
```

This will start up the Supabase stack locally and print out a bunch of environment details, including your local `DB URL`. Make a note of that for later use.



## Install the dependencies

Add the following dependencies to your project:

*   [`supabase`](https://github.com/supabase-community/supabase-py): Supabase Python Client
*   [`mixpeek`](https://github.com/mixpeek/python-client): Mixpeek Python Client for embedding generation

```shell
poetry add supabase mixpeek
```



## Import the necessary dependencies

At the top of your main Python script, import the dependencies and store your environment variables:

```python
from supabase import create_client, Client
from mixpeek import Mixpeek
import os

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_API_KEY")
MIXPEEK_API_KEY = os.getenv("MIXPEEK_API_KEY")
```



## Create embeddings for your videos

Next, create a `seed` method, which will create a new Supabase table, generate embeddings for your video chunks, and insert the embeddings into your database:

```python
def seed():
    # Initialize Supabase and Mixpeek clients
    supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
    mixpeek = Mixpeek(MIXPEEK_API_KEY)

    # Create a table for storing video chunk embeddings
    supabase.table("video_chunks").create({
        "id": "text",
        "start_time": "float8",
        "end_time": "float8",
        "embedding": "extensions.vector(768)",
        "metadata": "jsonb"
    })

    # Process and embed video
    video_url = "https://example.com/your_video.mp4"
    processed_chunks = mixpeek.tools.video.process(
        video_source=video_url,
        chunk_interval=1,  # 1 second intervals
        resolution=[720, 1280]
    )

    for chunk in processed_chunks:
        print(f"Processing video chunk: {chunk['start_time']}")

        # Generate embedding using Mixpeek
        embed_response = mixpeek.embed.video(
            model_id="vuse-generic-v1",
            input=chunk['base64_chunk'],
            input_type="base64"
        )

        # Insert into Supabase
        supabase.table("video_chunks").insert({
            "id": f"chunk_{chunk['start_time']}",
            "start_time": chunk["start_time"],
            "end_time": chunk["end_time"],
            "embedding": embed_response['embedding'],
            "metadata": {"video_url": video_url}
        }).execute()

    print("Video processed and embeddings inserted")

    # Create index for fast search performance
    supabase.query("CREATE INDEX ON video_chunks USING ivfflat (embedding vector_cosine_ops) WITH (lists = 100)").execute()
    print("Created index")
```

Add this method as a script in your `pyproject.toml` file:

```toml
[tool.poetry.scripts]
seed = "video_search.main:seed"
search = "video_search.main:search"
```

After activating the virtual environment with `poetry shell`, you can now run your seed script via `poetry run seed`. You can inspect the generated embeddings in your local database by visiting the local Supabase dashboard at [localhost:54323](http://localhost:54323/project/default/editor).



## Perform a video search from a text query

With Supabase Vector, you can query your embeddings. You can use either a video clip as search input or alternatively, you can generate an embedding from a string input and use that as the query input:

```python
def search():
    # Initialize Supabase and Mixpeek clients
    supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
    mixpeek = Mixpeek(MIXPEEK_API_KEY)

    # Generate embedding for text query
    query_string = "a car chase scene"
    text_emb = mixpeek.embed.video(
        model_id="vuse-generic-v1",
        input=query_string,
        input_type="text"
    )

    # Query the collection
    results = supabase.rpc(
        'match_video_chunks',
        {
            'query_embedding': text_emb['embedding'],
            'match_threshold': 0.8,
            'match_count': 5
        }
    ).execute()

    # Display the results
    if results.data:
        for result in results.data:
            print(f"Matched chunk from {result['start_time']} to {result['end_time']} seconds")
            print(f"Video URL: {result['metadata']['video_url']}")
            print(f"Similarity: {result['similarity']}")
            print("---")
    else:
        print("No matching video chunks found")
```

This query will return the top 5 most similar video chunks from your database.

You can now test it out by running `poetry run search`, and you will be presented with the most relevant video chunks to the query "a car chase scene".



## Conclusion

With just a couple of Python scripts, you are able to implement video search as well as reverse video search using Mixpeek Embed and Supabase Vector. This approach allows for powerful semantic search capabilities that can be integrated into various applications, enabling you to search through video content using both text and video queries.



# Vector search with Next.js and OpenAI

Learn how to build a ChatGPT-style doc search powered by Next.js, OpenAI, and Supabase.

While our [Headless Vector search](/docs/guides/ai/examples/headless-vector-search) provides a toolkit for generative Q\&A, in this tutorial we'll go more in-depth, build a custom ChatGPT-like search experience from the ground-up using Next.js. You will:

1.  Convert your markdown into embeddings using OpenAI.
2.  Store you embeddings in Postgres using pgvector.
3.  Deploy a function for answering your users' questions.

You can read our [Supabase Clippy](/blog/chatgpt-supabase-docs) blog post for a full example.

We assume that you have a Next.js project with a collection of `.mdx` files nested inside your `pages` directory. We will start developing locally with the Supabase CLI and then push our local database changes to our hosted Supabase project. You can find the [full Next.js example on GitHub](https://github.com/supabase-community/nextjs-openai-doc-search).



## Create a project

1.  [Create a new project](/dashboard) in the Supabase Dashboard.
2.  Enter your project details.
3.  Wait for the new database to launch.



## Prepare the database

Let's prepare the database schema. We can use the "OpenAI Vector Search" quickstart in the [SQL Editor](/dashboard/project/_/sql), or you can copy/paste the SQL below and run it yourself.

<Tabs scrollable size="small" type="underlined" defaultActiveId="dashboard" queryGroup="database-method">
  <TabPanel id="dashboard" label="Dashboard">
    1.  Go to the [SQL Editor](/dashboard/project/_/sql) page in the Dashboard.
    2.  Click **OpenAI Vector Search**.
    3.  Click **Run**.
  </TabPanel>

  <TabPanel id="sql" label="SQL">
    <StepHikeCompact>
      <StepHikeCompact.Step step={1}>
        <StepHikeCompact.Details title="Set up Supabase locally">
          Make sure you have the latest version of the [Supabase CLI installed](/docs/guides/cli/getting-started).

          Initialize Supabase in the root directory of your app.
        </StepHikeCompact.Details>

        <StepHikeCompact.Details>
          ```bash
          supabase init
          ```
        </StepHikeCompact.Details>
      </StepHikeCompact.Step>

      <StepHikeCompact.Step step={2}>
        <StepHikeCompact.Details title="Create a migrations file">
          To make changes to our local database, we need to create a new migration. This will create a new `.sql` file in our `supabase/migrations` folder, where we can write SQL that will be applied to our local database when starting Supabase locally.
        </StepHikeCompact.Details>

        <StepHikeCompact.Code>
          ```bash
          supabase migration new init
          ```
        </StepHikeCompact.Code>
      </StepHikeCompact.Step>

      <StepHikeCompact.Step step={3}>
        <StepHikeCompact.Details title="Enable the pgvector extension">
          Copy the following SQL line into the newly created migration file to enable the pgvector extension.
        </StepHikeCompact.Details>

        <StepHikeCompact.Code>
          ```sql
          -- Enable pgvector extension
          create extension if not exists vector with schema public;
          ```
        </StepHikeCompact.Code>
      </StepHikeCompact.Step>

      <StepHikeCompact.Step step={3}>
        <StepHikeCompact.Details title="Create the database schema">
          Copy these SQL queries to your migration file. It will create two tables in our database schema.
        </StepHikeCompact.Details>

        <StepHikeCompact.Code>
          ```sql
          -- Stores the checksum of our pages.
          -- This ensures that we only regenerate embeddings
          -- when the page content has changed.
          create table "public"."nods_page" (
            id bigserial primary key,
            parent_page_id bigint references public.nods_page,
            path text not null unique,
            checksum text,
            meta jsonb,
            type text,
            source text
          );
          alter table "public"."nods_page"
            enable row level security;

          -- Stores the actual embeddings with some metadata
          create table "public"."nods_page_section" (
            id bigserial primary key,
            page_id bigint not null references public.nods_page on delete cascade,
            content text,
            token_count int,
            embedding extensions.vector(1536),
            slug text,
            heading text
          );
          alter table "public"."nods_page_section"
            enable row level security;
          ```
        </StepHikeCompact.Code>
      </StepHikeCompact.Step>

      <StepHikeCompact.Step step={4}>
        <StepHikeCompact.Details title="Create similarity search database function">
          Anytime the user sends a query, we want to find the content that's relevant to their questions. We can do this using pgvector's similarity search.

          These are quite complex SQL operations, so let's wrap them in database functions that we can call from our frontend using [RPC](/docs/reference/javascript/rpc).
        </StepHikeCompact.Details>

        <StepHikeCompact.Code>
          ```sql
          -- Create embedding similarity search functions
          create or replace function match_page_sections(
              embedding extensions.vector(1536),
              match_threshold float,
              match_count int,
              min_content_length int
          )
          returns table (
              id bigint,
              page_id bigint,
              slug text,
              heading text,
              content text,
              similarity float
          )
          language plpgsql
          as $$
          #variable_conflict use_variable
          begin
            return query
            select
              nods_page_section.id,
              nods_page_section.page_id,
              nods_page_section.slug,
              nods_page_section.heading,
              nods_page_section.content,
              (nods_page_section.embedding <#> embedding) * -1 as similarity
            from nods_page_section

            -- We only care about sections that have a useful amount of content
            where length(nods_page_section.content) >= min_content_length

            -- The dot product is negative because of a Postgres limitation, so we negate it
            and (nods_page_section.embedding <#> embedding) * -1 > match_threshold

            -- OpenAI embeddings are normalized to length 1, so
            -- cosine similarity and dot product will produce the same results.
            -- Using dot product which can be computed slightly faster.
            --
            -- For the different syntaxes, see https://github.com/pgvector/pgvector
            order by nods_page_section.embedding <#> embedding

            limit match_count;
          end;
          $$;
          ```
        </StepHikeCompact.Code>
      </StepHikeCompact.Step>

      <StepHikeCompact.Step step={5}>
        <StepHikeCompact.Details title="Start Supabase Locally">
          Start Supabase locally. At this point all files in `supabase/migrations` will be applied to your database and you're ready to go.
        </StepHikeCompact.Details>

        <StepHikeCompact.Code>
          ```bash
          supabase start
          ```
        </StepHikeCompact.Code>
      </StepHikeCompact.Step>

      <StepHikeCompact.Step step={6}>
        <StepHikeCompact.Details title="Push changes to your Supabase database">
          Once ready, you can link your local project to your cloud hosted Supabase project and push the local changes to your hosted instance.
        </StepHikeCompact.Details>

        <StepHikeCompact.Code>
          ```bash
          supabase link --project-ref=your-project-ref

          supabase db push
          ```
        </StepHikeCompact.Code>
      </StepHikeCompact.Step>
    </StepHikeCompact>
  </TabPanel>
</Tabs>



## Pre-process the knowledge base at build time

With our database set up, we need to process and store all `.mdx` files in the `pages` directory. You can find the full script [here](https://github.com/supabase-community/nextjs-openai-doc-search/blob/main/lib/generate-embeddings.ts), or follow the steps below:

<StepHikeCompact>
  <StepHikeCompact.Step step={1}>
    <StepHikeCompact.Details title="Generate Embeddings">
      Create a new file `lib/generate-embeddings.ts` and copy the code over from [GitHub](https://github.com/supabase-community/nextjs-openai-doc-search/blob/main/lib/generate-embeddings.ts).
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      ```bash
      curl \
      https://raw.githubusercontent.com/supabase-community/nextjs-openai-doc-search/main/lib/generate-embeddings.ts \
      -o "lib/generate-embeddings.ts"
      ```
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={2}>
    <StepHikeCompact.Details title="Set up environment variables">
      We need some environment variables to run the script. Add them to your `.env` file and make sure your `.env` file is not committed to source control!
      You can get your local Supabase credentials by running `supabase status`.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      ```bash
      NEXT_PUBLIC_SUPABASE_URL=
      NEXT_PUBLIC_SUPABASE_PUBLISHABLE_KEY=
      SUPABASE_SERVICE_ROLE_KEY=

      # Get your key at https://platform.openai.com/account/api-keys
      OPENAI_API_KEY=
      ```
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={3}>
    <StepHikeCompact.Details title="Run script at build time">
      Include the script in your `package.json` script commands to enable Vercel to automatically run it at build time.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      ```json
      "scripts": {
        "dev": "next dev",
        "build": "pnpm run embeddings && next build",
        "start": "next start",
        "embeddings": "tsx lib/generate-embeddings.ts"
      },
      ```
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>
</StepHikeCompact>



## Create text completion with OpenAI API

Anytime a user asks a question, we need to create an embedding for their question, perform a similarity search, and then send a text completion request to the OpenAI API with the query and then context content merged together into a prompt.

All of this is glued together in a [Vercel Edge Function](https://vercel.com/docs/concepts/functions/edge-functions), the code for which can be found on [GitHub](https://github.com/supabase-community/nextjs-openai-doc-search/blob/main/pages/api/vector-search.ts).

<StepHikeCompact>
  <StepHikeCompact.Step step={1}>
    <StepHikeCompact.Details title="Create Embedding for Question">
      In order to perform similarity search we need to turn the question into an embedding.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      ```ts
      const embeddingResponse = await fetch('https://api.openai.com/v1/embeddings', {
        method: 'POST',
        headers: {
          Authorization: `Bearer ${openAiKey}`,
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          model: 'text-embedding-ada-002',
          input: sanitizedQuery.replaceAll('\n', ' '),
        }),
      })

      if (embeddingResponse.status !== 200) {
        throw new ApplicationError('Failed to create embedding for question', embeddingResponse)
      }

      const {
        data: [{ embedding }],
      } = await embeddingResponse.json()
      ```
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={2}>
    <StepHikeCompact.Details title="Perform similarity search">
      Using the `embeddingResponse` we can now perform similarity search by performing an remote procedure call (RPC) to the database function we created earlier.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      ```ts
      const { error: matchError, data: pageSections } = await supabaseClient.rpc(
        'match_page_sections',
        {
          embedding,
          match_threshold: 0.78,
          match_count: 10,
          min_content_length: 50,
        }
      )
      ```
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={3}>
    <StepHikeCompact.Details title="Perform text completion request">
      With the relevant content for the user's question identified, we can now build the prompt and make a text completion request via the OpenAI API.

      If successful, the OpenAI API will respond with a `text/event-stream` response that we can forward to the client where we'll process the event stream to smoothly print the answer to the user.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      ```ts
      const prompt = codeBlock`
        ${oneLine`
          You are a very enthusiastic Supabase representative who loves
          to help people! Given the following sections from the Supabase
          documentation, answer the question using only that information,
          outputted in markdown format. If you are unsure and the answer
          is not explicitly written in the documentation, say
          "Sorry, I don't know how to help with that."
        `}

        Context sections:
        ${contextText}

        Question: """
        ${sanitizedQuery}
        """

        Answer as markdown (including related code snippets if available):
      `

      const completionOptions: CreateCompletionRequest = {
        model: 'gpt-3.5-turbo-instruct',
        prompt,
        max_tokens: 512,
        temperature: 0,
        stream: true,
      }

      const response = await fetch('https://api.openai.com/v1/completions', {
        method: 'POST',
        headers: {
          Authorization: `Bearer ${openAiKey}`,
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(completionOptions),
      })

      if (!response.ok) {
        const error = await response.json()
        throw new ApplicationError('Failed to generate completion', error)
      }

      // Proxy the streamed SSE response from OpenAI
      return new Response(response.body, {
        headers: {
          'Content-Type': 'text/event-stream',
        },
      })
      ```
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>
</StepHikeCompact>



## Display the answer on the frontend

In a last step, we need to process the event stream from the OpenAI API and print the answer to the user. The full code for this can be found on [GitHub](https://github.com/supabase-community/nextjs-openai-doc-search/blob/main/components/SearchDialog.tsx).

```ts
const handleConfirm = React.useCallback(
  async (query: string) => {
    setAnswer(undefined)
    setQuestion(query)
    setSearch('')
    dispatchPromptData({ index: promptIndex, answer: undefined, query })
    setHasError(false)
    setIsLoading(true)

    const eventSource = new SSE(`api/vector-search`, {
      headers: {
        apikey: process.env.NEXT_PUBLIC_SUPABASE_PUBLISHABLE_KEY ?? '',
        Authorization: `Bearer ${process.env.NEXT_PUBLIC_SUPABASE_PUBLISHABLE_KEY}`,
        'Content-Type': 'application/json',
      },
      payload: JSON.stringify({ query }),
    })

    function handleError<T>(err: T) {
      setIsLoading(false)
      setHasError(true)
      console.error(err)
    }

    eventSource.addEventListener('error', handleError)
    eventSource.addEventListener('message', (e: any) => {
      try {
        setIsLoading(false)

        if (e.data === '[DONE]') {
          setPromptIndex((x) => {
            return x + 1
          })
          return
        }

        const completionResponse: CreateCompletionResponse = JSON.parse(e.data)
        const text = completionResponse.choices[0].text

        setAnswer((answer) => {
          const currentAnswer = answer ?? ''

          dispatchPromptData({
            index: promptIndex,
            answer: currentAnswer + text,
          })

          return (answer ?? '') + text
        })
      } catch (err) {
        handleError(err)
      }
    })

    eventSource.stream()

    eventSourceRef.current = eventSource

    setIsLoading(true)
  },
  [promptIndex, promptData]
)
```



## Learn more

Want to learn more about the awesome tech that is powering this?

*   Read about how we built [ChatGPT for the Supabase Docs](/blog/chatgpt-supabase-docs).
*   Read the pgvector Docs for [Embeddings and vector similarity](/docs/guides/database/extensions/pgvector)
*   Watch Greg's video for a full breakdown:

<div class="video-container">
  <iframe src="https://www.youtube-nocookie.com/embed/Yhtjd7yGGGA" frameBorder="1" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />
</div>



# Generating OpenAI GPT3 completions

Generate GPT text completions using OpenAI and Supabase Edge Functions.

OpenAI provides a [completions API](https://platform.openai.com/docs/api-reference/completions) that allows you to use their generative GPT models in your own applications.

OpenAI's API is intended to be used from the server-side. Supabase offers Edge Functions to make it easy to interact with third party APIs like OpenAI.



## Setup Supabase project

If you haven't already, [install the Supabase CLI](/docs/guides/cli) and initialize your project:

```shell
supabase init
```



## Create edge function

Scaffold a new edge function called `openai` by running:

```shell
supabase functions new openai
```

A new edge function will now exist under `./supabase/functions/openai/index.ts`.

We'll design the function to take your user's query (via POST request) and forward it to OpenAI's API.

```ts index.ts
import OpenAI from 'https://deno.land/x/openai@v4.24.0/mod.ts'

Deno.serve(async (req) => {
  const { query } = await req.json()
  const apiKey = Deno.env.get('OPENAI_API_KEY')
  const openai = new OpenAI({
    apiKey: apiKey,
  })

  // Documentation here: https://github.com/openai/openai-node
  const chatCompletion = await openai.chat.completions.create({
    messages: [{ role: 'user', content: query }],
    // Choose model from here: https://platform.openai.com/docs/models
    model: 'gpt-3.5-turbo',
    stream: false,
  })

  const reply = chatCompletion.choices[0].message.content

  return new Response(reply, {
    headers: { 'Content-Type': 'text/plain' },
  })
})
```

Note that we are setting `stream` to `false` which will wait until the entire response is complete before returning. If you wish to stream GPT's response word-by-word back to your client, set `stream` to `true`.



## Create OpenAI key

You may have noticed we were passing `OPENAI_API_KEY` in the Authorization header to OpenAI. To generate this key, go to [https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys) and create a new secret key.

After getting the key, copy it into a new file called `.env.local` in your `./supabase` folder:

```
OPENAI_API_KEY=your-key-here
```



## Run locally

Serve the edge function locally by running:

```bash
supabase functions serve --env-file ./supabase/.env.local --no-verify-jwt
```

Notice how we are passing in the `.env.local` file.

Use cURL or Postman to make a POST request to [http://localhost:54321/functions/v1/openai](http://localhost:54321/functions/v1/openai).

```bash
curl -i --location --request POST http://localhost:54321/functions/v1/openai \
  --header 'Content-Type: application/json' \
  --data '{"query":"What is Supabase?"}'
```

You should see a GPT response come back from OpenAI!



## Deploy

Deploy your function to the cloud by running:

```bash
supabase functions deploy --no-verify-jwt openai
supabase secrets set --env-file ./supabase/.env.local
```



## Go deeper

If you're interesting in learning how to use this to build your own ChatGPT, read [the blog post](/blog/chatgpt-supabase-docs) and check out the video:

<div class="video-container">
  <iframe src="https://www.youtube-nocookie.com/embed/Yhtjd7yGGGA" frameBorder="1" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />
</div>



# Semantic Image Search with Amazon Titan

Implement semantic image search with Amazon Titan and Supabase Vector in Python.

[Amazon Bedrock](https://aws.amazon.com/bedrock) is a fully managed service that offers a choice of high-performing foundation models (FMs) from leading AI companies like AI21 Labs, Anthropic, Cohere, Meta, Mistral AI, Stability AI, and Amazon. Each model is accessible through a common API which implements a broad set of features to help build generative AI applications with security, privacy, and responsible AI in mind.

[Amazon Titan](https://aws.amazon.com/bedrock/titan/) is a family of foundation models (FMs) for text and image generation, summarization, classification, open-ended Q\&A, information extraction, and text or image search.

In this guide we'll look at how we can get started with Amazon Bedrock and Supabase Vector in Python using the Amazon Titan multimodal model and the [vecs client](/docs/guides/ai/vecs-python-client).

You can find the full application code as a Python Poetry project on [GitHub](https://github.com/supabase/supabase/tree/master/examples/ai/aws_bedrock_image_search).



## Create a new Python project with Poetry

[Poetry](https://python-poetry.org/) provides packaging and dependency management for Python. If you haven't already, install poetry via pip:

```shell
pip install poetry
```

Then initialize a new project:

```shell
poetry new aws_bedrock_image_search
```



## Spin up a Postgres database with pgvector

If you haven't already, head over to [database.new](https://database.new) and create a new project. Every Supabase project comes with a full Postgres database and the [pgvector extension](/docs/guides/database/extensions/pgvector) preconfigured.

When creating your project, make sure to note down your database password as you will need it to construct the `DB_URL` in the next step.

You can find your database connection string on your project dashboard, click [Connect](/dashboard/project/_?showConnect=true). Use the Session pooler connection string which looks like this:

```txt
postgresql://postgres.[PROJECT-REF]:[YOUR-PASSWORD]@aws-0-[REGION].pooler.supabase.com:5432/postgres
```



## Install the dependencies

We will need to add the following dependencies to our project:

*   [`vecs`](https://github.com/supabase/vecs#vecs): Supabase Vector Python Client.
*   [`boto3`](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html): AWS SDK for Python.
*   [`matplotlib`](https://matplotlib.org/): for displaying our image result.

```shell
poetry add vecs boto3 matplotlib
```



## Import the necessary dependencies

At the top of your main python script, import the dependencies and store your `DB URL` from above in a variable:

```python
import sys
import boto3
import vecs
import json
import base64
from matplotlib import pyplot as plt
from matplotlib import image as mpimg
from typing import Optional

DB_CONNECTION = "postgresql://postgres.[PROJECT-REF]:[YOUR-PASSWORD]@aws-0-[REGION].pooler.supabase.com:5432/postgres"
```

Next, get the [credentials to your AWS account](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html) and instantiate the `boto3` client:

```python
bedrock_client = boto3.client(
    'bedrock-runtime',
    region_name='us-west-2',
    # Credentials from your AWS account
    aws_access_key_id='<replace_your_own_credentials>',
    aws_secret_access_key='<replace_your_own_credentials>',
    aws_session_token='<replace_your_own_credentials>',
)
```



## Create embeddings for your images

In the root of your project, create a new folder called `images` and add some images. You can use the images from the example project on [GitHub](https://github.com/supabase/supabase/tree/master/examples/ai/aws_bedrock_image_search/images) or you can find license free images on [Unsplash](https://unsplash.com).

To send images to the Amazon Bedrock API we need to need to encode them as `base64` strings. Create the following helper methods:

```python
def readFileAsBase64(file_path):
    """Encode image as base64 string."""
    try:
        with open(file_path, "rb") as image_file:
            input_image = base64.b64encode(image_file.read()).decode("utf8")
        return input_image
    except:
        print("bad file name")
        sys.exit(0)


def construct_bedrock_image_body(base64_string):
    """Construct the request body.

    https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-titan-embed-mm.html
    """
    return json.dumps(
        {
            "inputImage": base64_string,
            "embeddingConfig": {"outputEmbeddingLength": 1024},
        }
    )


def get_embedding_from_titan_multimodal(body):
    """Invoke the Amazon Titan Model via API request."""
    response = bedrock_client.invoke_model(
        body=body,
        modelId="amazon.titan-embed-image-v1",
        accept="application/json",
        contentType="application/json",
    )

    response_body = json.loads(response.get("body").read())
    print(response_body)
    return response_body["embedding"]


def encode_image(file_path):
    """Generate embedding for the image at file_path."""
    base64_string = readFileAsBase64(file_path)
    body = construct_bedrock_image_body(base64_string)
    emb = get_embedding_from_titan_multimodal(body)
    return emb
```

Next, create a `seed` method, which will create a new Supabase Vector Collection, generate embeddings for your images, and upsert the embeddings into your database:

```python
def seed():
    # create vector store client
    vx = vecs.create_client(DB_CONNECTION)

    # get or create a collection of vectors with 1024 dimensions
    images = vx.get_or_create_collection(name="image_vectors", dimension=1024)

    # Generate image embeddings with Amazon Titan Model
    img_emb1 = encode_image('./images/one.jpg')
    img_emb2 = encode_image('./images/two.jpg')
    img_emb3 = encode_image('./images/three.jpg')
    img_emb4 = encode_image('./images/four.jpg')

    # add records to the *images* collection
    images.upsert(
        records=[
            (
                "one.jpg",       # the vector's identifier
                img_emb1,        # the vector. list or np.array
                {"type": "jpg"}  # associated  metadata
            ), (
                "two.jpg",
                img_emb2,
                {"type": "jpg"}
            ), (
                "three.jpg",
                img_emb3,
                {"type": "jpg"}
            ), (
                "four.jpg",
                img_emb4,
                {"type": "jpg"}
            )
        ]
    )
    print("Inserted images")

    # index the collection for fast search performance
    images.create_index()
    print("Created index")
```

Add this method as a script in your `pyproject.toml` file:

```toml
[tool.poetry.scripts]
seed = "image_search.main:seed"
search = "image_search.main:search"
```

After activating the virtual environment with `poetry shell` you can now run your seed script via `poetry run seed`. You can inspect the generated embeddings in your Supabase Dashboard by visiting the [Table Editor](/dashboard/project/_/editor), selecting the `vecs` schema, and the `image_vectors` table.



## Perform an image search from a text query

We can use Supabase Vector to query our embeddings. We can either use an image as the search input or generate an embedding from a string input:

```python
def search(query_term: Optional[str] = None):
    if query_term is None:
        query_term = sys.argv[1]

    # create vector store client
    vx = vecs.create_client(DB_CONNECTION)
    images = vx.get_or_create_collection(name="image_vectors", dimension=1024)

    # Encode text query
    text_emb = get_embedding_from_titan_multimodal(json.dumps(
        {
            "inputText": query_term,
            "embeddingConfig": {"outputEmbeddingLength": 1024},
        }
    ))

    # query the collection filtering metadata for "type" = "jpg"
    results = images.query(
        data=text_emb,                      # required
        limit=1,                            # number of records to return
        filters={"type": {"$eq": "jpg"}},   # metadata filters
    )
    result = results[0]
    print(result)
    plt.title(result)
    image = mpimg.imread('./images/' + result)
    plt.imshow(image)
    plt.show()
```

By limiting the query to one result, we can show the most relevant image to the user. Finally we use `matplotlib` to show the image result to the user.

Go ahead and test it out by running `poetry run search` and you will be presented with an image of a "bike in front of a red brick wall".



## Conclusion

With just a couple of lines of Python you are able to implement image search as well as reverse image search using the Amazon Titan multimodal model and Supabase Vector.


---
**Navigation:** [← Previous](./40-concepts.md) | [Index](./index.md) | Next →
