**Navigation:** [← Previous](./39-understanding-api-keys.md) | [Index](./index.md) | [Next →](./41-ivfflat-indexes.md)

# Concepts



Embeddings are core to many AI and vector applications. This guide covers these concepts. If you prefer to get started right away, see our guide on [Generating Embeddings](/docs/guides/ai/quickstarts/generate-text-embeddings).



## What are embeddings?

Embeddings capture the "relatedness" of text, images, video, or other types of information. This relatedness is most commonly used for:

*   **Search:** how similar is a search term to a body of text?
*   **Recommendations:** how similar are two products?
*   **Classifications:** how do we categorize a body of text?
*   **Clustering:** how do we identify trends?

Let's explore an example of text embeddings. Say we have three phrases:

1.  "The cat chases the mouse"
2.  "The kitten hunts rodents"
    {/* supa-mdx-lint-disable-next-line Rule004ExcludeWords */}
3.  "I like ham sandwiches"

Your job is to group phrases with similar meaning. If you are a human, this should be obvious. Phrases 1 and 2 are almost identical, while phrase 3 has a completely different meaning.

Although phrases 1 and 2 are similar, they share no common vocabulary (besides "the"). Yet their meanings are nearly identical. How can we teach a computer that these are the same?



## Human language

Humans use words and symbols to communicate language. But words in isolation are mostly meaningless - we need to draw from shared knowledge & experience in order to make sense of them. The phrase “You should Google it” only makes sense if you know that Google is a search engine and that people have been using it as a verb.

In the same way, we need to train a neural network model to understand human language. An effective model should be trained on millions of different examples to understand what each word, phrase, sentence, or paragraph could mean in different contexts.

So how does this relate to embeddings?



## How do embeddings work?

Embeddings compress discrete information (words & symbols) into distributed continuous-valued data (vectors). If we took our phrases from before and plot them on a chart, it might look something like this:

<img src="/docs/img/ai/vector-similarity.png" alt="Vector similarity" width="640" height="640" />

Phrases 1 and 2 would be plotted close to each other, since their meanings are similar. We would expect phrase 3 to live somewhere far away since it isn't related. If we had a fourth phrase, “Sally ate Swiss cheese”, this might exist somewhere between phrase 3 (cheese can go on sandwiches) and phrase 1 (mice like Swiss cheese).

In this example we only have 2 dimensions: the X and Y axis. In reality, we would need many more dimensions to effectively capture the complexities of human language.



## Using embeddings

Compared to our 2-dimensional example above, most embedding models will output many more dimensions. For example the open source [`gte-small`](https://huggingface.co/Supabase/gte-small) model outputs 384 dimensions.

Why is this useful? Once we have generated embeddings on multiple texts, it is trivial to calculate how similar they are using vector math operations like cosine distance. A common use case for this is search. Your process might look something like this:

1.  Pre-process your knowledge base and generate embeddings for each page
2.  Store your embeddings to be referenced later
3.  Build a search page that prompts your user for input
4.  Take user's input, generate a one-time embedding, then perform a similarity search against your pre-processed embeddings.
5.  Return the most similar pages to the user



## See also

*   [Structured and Unstructured embeddings](/docs/guides/ai/structured-unstructured)



# Engineering for Scale

Building an enterprise-grade vector architecture.

Content sources for vectors can be extremely large. As you grow you should run your Vector workloads across several secondary databases (sometimes called "pods"), which allows each collection to scale independently.



## Simple workloads

For small workloads, it's typical to store your data in a single database.

If you've used [Vecs](/docs/guides/ai/vecs-python-client) to create 3 different collections, you can expose collections to your web or mobile application using [views](/docs/guides/database/tables#views):

<Image
  alt="single database"
  src={{
    light: '/docs/img/ai/scaling/engineering-for-scale--single-database--light.png',
    dark: '/docs/img/ai/scaling/engineering-for-scale--single-database--dark.png',
  }}
  zoomable
/>

For example, with 3 collections, called `docs`, `posts`, and `images`, we could expose the "docs" inside the public schema like this:

```sql
create view public.docs as
select
  id,
  embedding,
  metadata, # Expose the metadata as JSON
  (metadata->>'url')::text as url # Extract the URL as a string
from vector
```

You can then use any of the client libraries to access your collections within your applications:

{/* prettier-ignore */}

```js
const { data, error } = await supabase
  .from('docs')
  .select('id, embedding, metadata')
  .eq('url', '/hello-world')
```



## Enterprise workloads

As you move into production, we recommend splitting your collections into separate projects. This is because it allows your vector stores to scale independently of your production data. Vectors typically grow faster than operational data, and they have different resource requirements. Running them on separate databases removes the single-point-of-failure.

<Image
  alt="With secondaries"
  src={{
    light: '/docs/img/ai/scaling/engineering-for-scale--with-secondaries--light.png',
    dark: '/docs/img/ai/scaling/engineering-for-scale--with-secondaries--dark.png',
  }}
  zoomable
/>

You can use as many secondary databases as you need to manage your collections. With this architecture, you have 2 options for accessing collections within your application:

1.  Query the collections directly using Vecs.
2.  Access the collections from your Primary database through a Wrapper.

You can use both of these in tandem to suit your use-case. We recommend option `1` wherever possible, as it offers the most scalability.


### Query collections using Vecs

Vecs provides methods for querying collections, either using a [cosine similarity function](https://supabase.github.io/vecs/api/#basic) or with [metadata filtering](https://supabase.github.io/vecs/api/#metadata-filtering).

```python

# cosine similarity
docs.query(query_vector=[0.4,0.5,0.6], limit=5)


# metadata filtering
docs.query(
    query_vector=[0.4,0.5,0.6],
    limit=5,
    filters={"year": {"$eq": 2012}}, # metadata filters
)
```


### Accessing external collections using Wrappers

Supabase supports [Foreign Data Wrappers](/blog/postgres-foreign-data-wrappers-rust). Wrappers allow you to connect two databases together so that you can query them over the network.

This involves 2 steps: connecting to your remote database from the primary and creating a Foreign Table.


#### Connecting your remote database

Inside your Primary database we need to provide the credentials to access the secondary database:

```sql
create extension postgres_fdw;

create server docs_server
foreign data wrapper postgres_fdw
options (host 'db.xxx.supabase.co', port '5432', dbname 'postgres');

create user mapping for docs_user
server docs_server
options (user 'postgres', password 'password');
```


#### Create a foreign table

We can now create a foreign table to access the data in our secondary project.

```sql
create foreign table docs (
  id text not null,
  embedding extensions.vector(384),
  metadata jsonb,
  url text
)
server docs_server
options (schema_name 'public', table_name 'docs');
```

This looks very similar to our View example above, and you can continue to use the client libraries to access your collections through the foreign table:

{/* prettier-ignore */}

```js
const { data, error } = await supabase
  .from('docs')
  .select('id, embedding, metadata')
  .eq('url', '/hello-world')
```


### Enterprise architecture

This diagram provides an example architecture that allows you to access the collections either with our client libraries or using Vecs. You can add as many secondary databases as you need (in this example we only show one):

<Image
  alt="multi database"
  src={{
    light: '/docs/img/ai/scaling/engineering-for-scale--multi-database--light.png',
    dark: '/docs/img/ai/scaling/engineering-for-scale--multi-database--dark.png',
  }}
  zoomable
/>



# Going to Production

Going to production checklist for AI applications.

This guide will help you to prepare your application for production. We'll provide actionable steps to help you scale your application, ensure that it is reliable, can handle the load, and provide optimal accuracy for your use case.

See our [Engineering for Scale](/docs/guides/ai/engineering-for-scale) guide for more information about engineering at scale.



## Do you need indexes?

Sequential scans will result in significantly higher latencies and lower throughput, guaranteeing 100% accuracy and not being RAM bound.

There are a couple of cases where you might not need indexes:

*   You have a small dataset and don't need to scale it.
*   You are not expecting high amounts of vector search queries per second.
*   You need to guarantee 100% accuracy.

You don't have to create indexes in these cases and can use sequential scans instead. This type of workload will not be RAM bound and will not require any additional resources but will result in higher latencies and lower throughput. Extra CPU cores may help to improve queries per second, but it will not help to improve latency.

On the other hand, if you need to scale your application, you will need to [create indexes](/docs/guides/ai/vector-indexes). This will result in lower latencies and higher throughput, but will require additional RAM to make use of Postgres Caching. Also, using indexes will result in lower accuracy, since you are replacing exact (KNN) search with approximate (ANN) search.



## HNSW vs IVFFlat indexes

`pgvector` supports two types of indexes: HNSW and IVFFlat. We recommend using [HNSW](/docs/guides/ai/vector-indexes/hnsw-indexes) because of its [performance](/blog/increase-performance-pgvector-hnsw#hnsw-performance-1536-dimensions) and [robustness against changing data](/docs/guides/ai/vector-indexes/hnsw-indexes#when-should-you-create-hnsw-indexes).

<Image
  alt="dbpedia embeddings comparing ivfflat and hnsw queries-per-second using the 4XL compute add-on"
  src={{
    light: '/docs/img/ai/going-prod/dbpedia-ivfflat-vs-hnsw-4xl--light.png',
    dark: '/docs/img/ai/going-prod/dbpedia-ivfflat-vs-hnsw-4xl--dark.png',
  }}
  zoomable
/>



## HNSW, understanding `ef_construction`, `ef_search`, and `m`

Index build parameters:

*   `m` is the number of bi-directional links created for every new element during construction. Higher `m` is suitable for datasets with high dimensionality and/or high accuracy requirements. Reasonable values for `m` are between 2 and 100. Range 12-48 is a good starting point for most use cases (16 is the default value).

*   `ef_construction` is the size of the dynamic list for the nearest neighbors (used during the construction algorithm). Higher `ef_construction` will result in better index quality and higher accuracy, but it will also increase the time required to build the index. `ef_construction` has to be at least 2 \* `m` (64 is the default value). At some point, increasing `ef_construction` does not improve the quality of the index. You can measure accuracy when `ef_search`=`ef_construction`: if accuracy is lower than 0.9, then there is room for improvement.

Search parameters:

*   `ef_search` is the size of the dynamic list for the nearest neighbors (used during the search). Increasing `ef_search` will result in better accuracy, but it will also increase the time required to execute a query (40 is the default value).

<Image
  alt="dbpedia embeddings comparing hnsw queries-per-second using different build parameters"
  src={{
    light: '/docs/img/ai/going-prod/dbpedia-hnsw-build-parameters--light.png',
    dark: '/docs/img/ai/going-prod/dbpedia-hnsw-build-parameters--dark.png',
  }}
  zoomable
/>



## IVFFlat, understanding `probes` and `lists`

Indexes used for approximate vector similarity search in pgvector divides a dataset into partitions. The number of these partitions is defined by the `lists` constant. The `probes` controls how many lists are going to be searched during a query.

The values of lists and probes directly affect accuracy and queries per second (QPS).

*   Higher `lists` means an index will be built slower, but you can achieve better QPS and accuracy.
*   Higher `probes` means that select queries will be slower, but you can achieve better accuracy.
*   `lists` and `probes` are not independent. Higher `lists` means that you will have to use higher `probes` to achieve the same accuracy.

You can find more examples of how `lists` and `probes` constants affect accuracy and QPS in [pgvector 0.4.0 performance](/blog/pgvector-performance) blogpost.

<Image
  alt="multi database"
  src={{
    light: '/docs/img/ai/going-prod/lists-count--light.png',
    dark: '/docs/img/ai/going-prod/lists-count--dark.png',
  }}
  zoomable
/>



## Performance tips when using indexes

First, a few generic tips which you can pick and choose from:

1.  The Supabase managed platform will automatically optimize Postgres configs for you based on your compute add-on. But if you self-host, consider **adjusting your Postgres config** based on RAM & CPU cores. See [example optimizations](https://gist.github.com/egor-romanov/323e2847851bbd758081511785573c08) for more details.
2.  Prefer `inner-product` to `L2` or `Cosine` distances if your vectors are normalized (like `text-embedding-ada-002`). If embeddings are not normalized, `Cosine` distance should give the best results with an index.
3.  **Pre-warm your database.** Implement the warm-up technique before transitioning to production or running benchmarks.
    *   Use [pg\_prewarm](https://www.postgresql.org/docs/current/pgprewarm.html) to load the index into RAM `select pg_prewarm('vecs.docs_vec_idx');`. This will help to avoid cold cache issues.
    *   Execute 10,000 to 50,000 "warm-up" queries before each benchmark/prod. This will help to utilize cache and buffers more efficiently.
4.  **Establish your workload.** Fine-tune `m` and `ef_construction` or `lists` constants for the pgvector index to accelerate your queries (at the expense of a slower build times). For instance, for benchmarks with 1,000,000 OpenAI embeddings, we set `m` and `ef_construction` to 32 and 80, and it resulted in 35% higher QPS than 24 and 56 values respectively.
5.  **Benchmark your own specific workloads.** Doing this during cache warm-up helps gauge the best value for the index build parameters, balancing accuracy with queries per second (QPS).



## Going into production

1.  Decide if you are going to use indexes or not. You can skip the rest of this guide if you do not use indexes.
2.  Over-provision RAM during preparation. You can scale down in step `5`, but it's better to start with a larger size to get the best results for RAM requirements. (We'd recommend at least 8XL if you're using Supabase.)
3.  Upload your data to the database. If you use the [`vecs`](/docs/guides/ai/python/api) library, it will automatically generate an index with default parameters.
4.  Run a benchmark using randomly generated queries and observe the results. Again, you can use the `vecs` library with the `ann-benchmarks` tool. Do it with default values for index build parameters, you can later adjust them to get the best results.
5.  Monitor the RAM usage, and save it as a note for yourself. You would likely want to use a compute add-on in the future that has the same amount of RAM that was used at the moment (both actual RAM usage and RAM used for cache and buffers).
6.  Scale down your compute add-on to the one that would have the same amount of RAM used at the moment.
7.  Repeat step 3 to load the data into RAM. You should see QPS increase on subsequent runs, and stop when it no longer increases.
8.  Run a benchmark using real queries and observe the results. You can use the `vecs` library for that as well with `ann-benchmarks` tool. Tweak `ef_search` for HNSW or `probes` for IVFFlat until you see that both accuracy and QPS match your requirements.
9.  If you want higher QPS you can increase `m` and `ef_construction` for HNSW or `lists` for IVFFlat parameters (consider switching from IVF to HNSW). You have to rebuild the index with a higher `m` and `ef_construction` values and repeat steps 6-7 to find the best combination of `m`, `ef_construction` and `ef_search` constants to achieve the best QPS and accuracy values. Higher `m`, `ef_construction` mean that index will build slower, but you can achieve better QPS and accuracy. Higher `ef_search` mean that select queries will be slower, but you can achieve better accuracy.



## Useful links

Don't forget to check out the general [Production Checklist](/docs/guides/platform/going-into-prod) to ensure your project is secure, performant, and will remain available for your users.

You can look at our [Choosing Compute Add-on](/docs/guides/ai/choosing-compute-addon) guide to get a basic understanding of how much compute you might need for your workload.

Or take a look at our [pgvector 0.5.0 performance](/blog/increase-performance-pgvector-hnsw) and [pgvector 0.4.0 performance](/blog/pgvector-performance) blog posts to see what pgvector is capable of and how the above technique can be used to achieve the best results.

<Image
  alt="multi database"
  src={{
    light: '/docs/img/ai/going-prod/size-to-rps--light.png',
    dark: '/docs/img/ai/going-prod/size-to-rps--dark.png',
  }}
  zoomable
/>



# Google Colab

Use Google Colab to manage your Supabase Vector store.

<a className="w-64" href="https://colab.research.google.com/github/supabase/supabase/blob/master/examples/ai/vector_hello_world.ipynb">
  <img src="/docs/img/ai/colab-badge.svg" />
</a>

Google Colab is a hosted Jupyter Notebook service. It provides free access to computing resources, including GPUs and TPUs, and is well-suited to machine learning, data science, and education. We can use Colab to manage collections using [Supabase Vecs](/docs/guides/ai/vecs-python-client).

In this tutorial we'll connect to a database running on the Supabase [platform](/dashboard/). If you don't already have a database, you can create one here: [database.new](https://database.new).



## Create a new notebook

Start by visiting [colab.research.google.com](https://colab.research.google.com/). There you can create a new notebook.

![Google Colab new notebook](/docs/img/ai/google-colab/colab-new.png)



## Install Vecs

We'll use the Supabase Vector client, [Vecs](/docs/guides/ai/vecs-python-client), to manage our collections.

At the top of the notebook add the notebook paste the following code and hit the "execute" button (`ctrl+enter`):

```py
pip install vecs
```

![Install vecs](/docs/img/ai/google-colab/install-vecs.png)



## Connect to your database

On your project dashboard, click [Connect](/dashboard/project/_?showConnect=true). The connection string should look like `postgres://postgres.xxxx:password@xxxx.pooler.supabase.com:6543/postgres`

Create a new code block below the install block (`ctrl+m b`) and add the following code using the Postgres URI you copied above:

```py
import vecs

DB_CONNECTION = "postgres://postgres.xxxx:password@xxxx.pooler.supabase.com:6543/postgres"


# create vector store client
vx = vecs.create_client(DB_CONNECTION)
```

Execute the code block (`ctrl+enter`). If no errors were returned then your connection was successful.



## Create a collection

Now we're going to create a new collection and insert some documents.

Create a new code block below the install block (`ctrl+m b`). Add the following code to the code block and execute it (`ctrl+enter`):

```py
collection = vx.get_or_create_collection(name="colab_collection", dimension=3)

collection.upsert(
    vectors=[
        (
         "vec0",           # the vector's identifier
         [0.1, 0.2, 0.3],  # the vector. list or np.array
         {"year": 1973}    # associated  metadata
        ),
        (
         "vec1",
         [0.7, 0.8, 0.9],
         {"year": 2012}
        )
    ]
)
```

This will create a table inside your database within the `vecs` schema, called `colab_collection`. You can view the inserted items in the [Table Editor](/dashboard/project/_/editor/), by selecting the `vecs` schema from the schema dropdown.

![Colab documents](/docs/img/ai/google-colab/colab-documents.png)



## Query your documents

Now we can search for documents based on their similarity. Create a new code block and execute the following code:

```py
collection.query(
    query_vector=[0.4,0.5,0.6],  # required
    limit=5,                     # number of records to return
    filters={},                  # metadata filters
    measure="cosine_distance",   # distance measure to use
    include_value=False,         # should distance measure values be returned?
    include_metadata=False,      # should record metadata be returned?
)
```

You will see that this returns two documents in an array `['vec1', 'vec0']`:

![Colab results](/docs/img/ai/google-colab/colab-results.png)

It also returns a warning:

```
Query does not have a covering index for cosine_distance.
```

You can lean more about creating indexes in the [Vecs documentation](https://supabase.github.io/vecs/api/#create-an-index).



## Resources

*   Vecs API: [supabase.github.io/vecs/api](https://supabase.github.io/vecs/api)



# Hugging Face Inference API



[Hugging Face](https://huggingface.co) is an open source hub for AI/ML models and tools. With over 100,000 machine learning models available, Hugging Face provides a great way to integrate specialized AI & ML tasks into your application.

There are 3 ways to use Hugging Face models in your application:

1.  Use the [Transformers](https://huggingface.co/docs/transformers/index) Python library to perform inference in a Python backend.
2.  [Generate embeddings](/docs/guides/ai/quickstarts/generate-text-embeddings) directly in Edge Functions using Transformers.js.
3.  Use Hugging Face's hosted [Inference API](https://huggingface.co/inference-api) to execute AI tasks remotely on Hugging Face servers. This guide will walk you through this approach.



## AI tasks

Below are some of the types of tasks you can perform with Hugging Face:


### Natural language

*   [Summarization](https://huggingface.co/tasks/summarization)
*   [Text classification](https://huggingface.co/tasks/text-classification)
*   [Text generation](https://huggingface.co/tasks/text-generation)
*   [Translation](https://huggingface.co/tasks/translation)
*   [Fill in the blank](https://huggingface.co/tasks/fill-mask)


### Computer vision

*   [Image to text](https://huggingface.co/tasks/image-to-text)
*   [Text to image](https://huggingface.co/tasks/text-to-image)
*   [Image classification](https://huggingface.co/tasks/image-classification)
*   [Video classification](https://huggingface.co/tasks/video-classification)
*   [Object detection](https://huggingface.co/tasks/object-detection)
*   [Image segmentation](https://huggingface.co/tasks/image-segmentation)


### Audio

*   [Text to speech](https://huggingface.co/tasks/text-to-speech)
*   [Speech to text](https://huggingface.co/tasks/automatic-speech-recognition)
*   [Audio classification](https://huggingface.co/tasks/audio-classification)

See a [full list of tasks](https://huggingface.co/tasks).



## Access token

First generate a Hugging Face access token for your app:

[https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)

Name your token based on the app its being used for and the environment. For example, if you are building an image generation app you might create 2 tokens:

*   "Image Generator (Dev)"
*   "Image Generator (Prod)"

Since we will be using this token for the inference API, choose the `read` role.

<Admonition type="note">
  Though it is possible to use the Hugging Face inference API today without an access token, [you may be rate limited](https://huggingface.co/docs/huggingface.js/inference/README#usage).

  To ensure you don't experience any unexpected downtime or errors, we recommend creating an access token.
</Admonition>



## Edge Functions

Edge Functions are server-side TypeScript functions that run on-demand. Since Edge Functions run on a server, you can safely give them access to your Hugging Face access token.

<Admonition type="note">
  You will need the `supabase` CLI [installed](/docs/guides/cli) for the following commands to work.
</Admonition>

To create a new Edge Function, navigate to your local project and initialize Supabase if you haven't already:

```shell
supabase init
```

Then create an Edge Function:

```shell
supabase functions new text-to-image
```

Create a file called `.env.local` to store your Hugging Face access token:

```shell
HUGGING_FACE_ACCESS_TOKEN=<your-token-here>
```

Let's modify the Edge Function to import Hugging Face's inference client and perform a `text-to-image` request:

```ts
import { serve } from 'https://deno.land/std@0.168.0/http/server.ts'
import { HfInference } from 'https://esm.sh/@huggingface/inference@2.3.2'

const hf = new HfInference(Deno.env.get('HUGGING_FACE_ACCESS_TOKEN'))

serve(async (req) => {
  const { prompt } = await req.json()

  const image = await hf.textToImage(
    {
      inputs: prompt,
      model: 'stabilityai/stable-diffusion-2',
    },
    {
      use_cache: false,
    }
  )

  return new Response(image)
})
```

1.  This function creates a new instance of `HfInference` using the `HUGGING_FACE_ACCESS_TOKEN` environment variable.

2.  It expects a POST request that includes a JSON request body. The JSON body should include a parameter called `prompt` that represents the text-to-image prompt that we will pass to Hugging Face's inference API.

3.  Next we call `textToImage()`, passing in the user's prompt along with the model that we would like to use for the image generation. Today Hugging Face recommends `stabilityai/stable-diffusion-2`, but you can change this to any other text-to-image model. You can see a list of which models are supported for each task by navigating to their [models page](https://huggingface.co/models?pipeline_tag=text-to-image) and filtering by task.

4.  We set `use_cache` to `false` so that repeat queries with the same prompt will produce new images. If the task and model you are using is deterministic (will always produce the same result based on the same input), consider setting `use_cache` to `true` for faster responses.

5.  The `image` result returned from the API will be a `Blob`. We can pass the `Blob` directly into a `new Response()` which will automatically set the content type and body of the response from the `image`.

Finally let's serve the Edge Function locally to test it:

```shell
supabase functions serve --env-file .env.local --no-verify-jwt
```

Remember to pass in the `.env.local` file using the `--env-file` parameter so that the Edge Function can access the `HUGGING_FACE_ACCESS_TOKEN`.

<Admonition type="note">
  For demo purposes we set `--no-verify-jwt` to make it easy to test the Edge Function without passing in a JWT token. In a real application you will need to pass the JWT as a `Bearer` token in the `Authorization` header.
</Admonition>

At this point, you can make an API request to your Edge Function using your preferred frontend framework (Next.js, React, Expo, etc). We can also test from the terminal using `curl`:

```shell
curl --output result.jpg --location --request POST 'http://localhost:54321/functions/v1/text-to-image' \
  --header 'Content-Type: application/json' \
  --data '{"prompt":"Llama wearing sunglasses"}'
```

In this example, your generated image will save to `result.jpg`:

<img src="/docs/img/ai/hugging-face/llama-sunglasses-example.png" alt="Llama wearing sunglasses example" width="400" height="400" />



## Next steps

You can now create an Edge Function that invokes a Hugging Face task using your model of choice.

Try running some other [AI tasks](#ai-tasks).



## Resources

*   Official [Hugging Face site](https://huggingface.co/).
*   Official [Hugging Face JS docs](https://huggingface.co/docs/huggingface.js).
*   [Generate image captions](/docs/guides/ai/examples/huggingface-image-captioning) using Hugging Face.



# Hybrid search

Combine keyword search with semantic search.

Hybrid search combines [full text search](/docs/guides/ai/keyword-search) (searching by keyword) with [semantic search](/docs/guides/ai/semantic-search) (searching by meaning) to identify results that are both directly and contextually relevant to the user's query.



## Use cases for hybrid search

Sometimes a single search method doesn't quite capture what a user is really looking for. For example, if a user searches for "Italian recipes with tomato sauce" on a cooking app, a keyword search would pull up recipes that specifically mention "Italian," "recipes," and "tomato sauce" in the text. However, it might miss out on dishes that are quintessentially Italian and use tomato sauce but don't explicitly label themselves with these words, or use variations like "pasta sauce" or "marinara." On the other hand, a semantic search might understand the culinary context and find recipes that match the intent, such as a traditional "Spaghetti Marinara," even if they don't match the exact keyword phrase. However, it could also suggest recipes that are contextually related but not what the user is looking for, like a "Mexican salsa" recipe, because it understands the context to be broadly about tomato-based sauces.

Hybrid search combines the strengths of both these methods. It would ensure that recipes explicitly mentioning the keywords are prioritized, thus capturing direct hits that satisfy the keyword criteria. At the same time, it would include recipes identified through semantic understanding as being related in meaning or context, like different Italian dishes that traditionally use tomato sauce but might not have been tagged explicitly with the user's search terms. It identifies results that are both directly and contextually relevant to the user's query while ideally minimizing misses and irrelevant suggestions.



## When to consider hybrid search

The decision to use hybrid search depends on what your users are looking for in your app. For a code repository where developers need to find exact lines of code or error messages, keyword search is likely ideal because it matches specific terms. In a mental health forum where users search for advice or experiences related to their feelings, semantic search may be better because it finds results based on the meaning of a query, not just specific words. For a shopping app where customers might search for specific product names yet also be open to related suggestions, hybrid search combines the best of both worlds - finding exact matches while also uncovering similar products based on the shopping context.



## How to combine search methods

Hybrid search merges keyword search and semantic search, but how does this process work?

First, each search method is executed separately. Keyword search, which involves searching by specific words or phrases present in the content, will yield its own set of results. Similarly, semantic search, which involves understanding the context or meaning behind the search query rather than the specific words used, will generate its own unique results.

Now with these separate result lists available, the next step is to combine them into a single, unified list. This is achieved through a process known as “fusion”. Fusion takes the results from both search methods and merges them together based on a certain ranking or scoring system. This system may prioritize certain results based on factors like their relevance to the search query, their ranking in the individual lists, or other criteria. The result is a final list that integrates the strengths of both keyword and semantic search methods.



## Reciprocal Ranked Fusion (RRF)

One of the most common fusion methods is Reciprocal Ranked Fusion (RRF). The key idea behind RRF is to give more weight to the top-ranked items in each individual result list when building the final combined list.

In RRF, we iterate over each record and assign a score (noting that each record could exist in one or both lists). The score is calculated as 1 divided by that record's rank in each list, summed together between both lists. For example, if a record with an ID of `123` was ranked third in the keyword search and ninth in semantic search, it would receive a score of $$\dfrac{1}{3} + \dfrac{1}{9} = 0.444$$. If the record was found in only one list and not the other, it would receive a score of 0 for the other list. The records are then sorted by this score to create the final list. The items with the highest scores are ranked first, and lowest scores ranked last.

This method ensures that items that are ranked high in multiple lists are given a high rank in the final list. It also ensures that items that are ranked high in only a few lists but low in others are not given a high rank in the final list. Placing the rank in the denominator when calculating score helps penalize the low ranking records.


### Smoothing constant `k`

To prevent extremely high scores for items that are ranked first (since we're dividing by the rank), a `k` constant is often added to the denominator to smooth the score:

$$\dfrac{1}{k+rank}$$

This constant can be any positive number, but is typically small. A constant of 1 would mean that a record ranked first would have a score of $$\dfrac{1}{1+1} = 0.5$$ instead of $$1$$. This adjustment can help balance the influence of items that are ranked very high in individual lists when creating the final combined list.



## Hybrid search in Postgres

Let's implement hybrid search in Postgres using `tsvector` (keyword search) and `pgvector` (semantic search).

First we'll create a `documents` table to store the documents that we will search over. This is just an example - adjust this to match the structure of your application.

```sql
create table documents (
  id bigint primary key generated always as identity,
  content text,
  fts tsvector generated always as (to_tsvector('english', content)) stored,
  embedding extensions.vector(512)
);
```

The table contains 4 columns:

*   `id` is an auto-generated unique ID for the record. We'll use this later to match records when performing RRF.
*   `content` contains the actual text we will be searching over.
*   `fts` is an auto-generated `tsvector` column that is generated using the text in `content`. We will use this for [full text search](/docs/guides/database/full-text-search) (search by keyword).
*   `embedding` is a [vector column](/docs/guides/ai/vector-columns) that stores the vector generated from our embedding model. We will use this for [semantic search](/docs/guides/ai/semantic-search) (search by meaning). We chose 512 dimensions for this example, but adjust this to match the size of the embedding vectors generated from your preferred model.

Next we'll create indexes on the `fts` and `embedding` columns so that their individual queries will remain fast at scale:

```sql
-- Create an index for the full-text search
create index on documents using gin(fts);

-- Create an index for the semantic vector search
create index on documents using hnsw (embedding vector_ip_ops);
```

For full text search we use a [generalized inverted (GIN) index](https://www.postgresql.org/docs/current/gin-intro.html) which is designed for handling composite values like those stored in a `tsvector`.

For semantic vector search we use an [HNSW index](/docs/guides/ai/vector-indexes/hnsw-indexes), which is a high performing approximate nearest neighbor (ANN) search algorithm. Note that we are using the `vector_ip_ops` (inner product) operator with this index because we plan on using the inner product (`<#>`) operator later in our query. If you plan to use a different operator like cosine distance (`<=>`), be sure to update the index accordingly. For more information, see [distance operators](/docs/guides/ai/vector-indexes#distance-operators).

Finally we'll create our `hybrid_search` function:

```sql
create or replace function hybrid_search(
  query_text text,
  query_embedding extensions.vector(512),
  match_count int,
  full_text_weight float = 1,
  semantic_weight float = 1,
  rrf_k int = 50
)
returns setof documents
language sql
as $$
with full_text as (
  select
    id,
    -- Note: ts_rank_cd is not indexable but will only rank matches of the where clause
    -- which shouldn't be too big
    row_number() over(order by ts_rank_cd(fts, websearch_to_tsquery(query_text)) desc) as rank_ix
  from
    documents
  where
    fts @@ websearch_to_tsquery(query_text)
  order by rank_ix
  limit least(match_count, 30) * 2
),
semantic as (
  select
    id,
    row_number() over (order by embedding <#> query_embedding) as rank_ix
  from
    documents
  order by rank_ix
  limit least(match_count, 30) * 2
)
select
  documents.*
from
  full_text
  full outer join semantic
    on full_text.id = semantic.id
  join documents
    on coalesce(full_text.id, semantic.id) = documents.id
order by
  coalesce(1.0 / (rrf_k + full_text.rank_ix), 0.0) * full_text_weight +
  coalesce(1.0 / (rrf_k + semantic.rank_ix), 0.0) * semantic_weight
  desc
limit
  least(match_count, 30)
$$;
```

Let's break this down:

*   **Parameters:** The function accepts quite a few parameters, but the main (required) ones are `query_text`, `query_embedding`, and `match_count`.

    *   `query_text` is the user's query text (more on this shortly)
    *   `query_embedding` is the vector representation of the user's query produced by the embedding model. We chose 512 dimensions for this example, but adjust this to match the size of the embedding vectors generated from your preferred model. This must match the size of the `embedding` vector on the `documents` table (and use the same model).
    *   `match_count` is the number of records returned in the `limit` clause.

    The other parameters are optional, but give more control over the fusion process.

    *   `full_text_weight` and `semantic_weight` decide how much weight each search method gets in the final score. These are both 1 by default which means they both equally contribute towards the final rank. A `full_text_weight` of 2 and `semantic_weight` of 1 would give full-text search twice as much weight as semantic search.
    *   `rrf_k` is the `k` [smoothing constant](#smoothing-constant-k) added to the reciprocal rank. The default is 50.

*   **Return type:** The function returns a set of records from our `documents` table.

*   **CTE:** We create two [common table expressions (CTE)](https://www.postgresql.org/docs/current/queries-with.html), one for full-text search and one for semantic search. These perform each query individually prior to joining them.

*   **RRF:** The final query combines the results from the two CTEs using [reciprocal rank fusion (RRF)](#reciprocal-ranked-fusion-rrf).



## Running hybrid search

To use this function in SQL, we can run:

```sql
select
  *
from
  hybrid_search(
    'Italian recipes with tomato sauce', -- user query
    '[...]'::extensions.vector(512), -- embedding generated from user query
    10
  );
```

In practice, you will likely be calling this from the [Supabase client](/docs/reference/javascript/introduction) or through a custom backend layer. Here is a quick example of how you might call this from an [Edge Function](/docs/guides/functions) using JavaScript:

```tsx
import { createClient } from 'npm:@supabase/supabase-js@2'
import OpenAI from 'npm:openai'

const supabaseUrl = Deno.env.get('SUPABASE_URL')!
const supabaseServiceRoleKey = Deno.env.get('SUPABASE_SERVICE_ROLE_KEY')!
const openaiApiKey = Deno.env.get('OPENAI_API_KEY')!

Deno.serve(async (req) => {
  // Grab the user's query from the JSON payload
  const { query } = await req.json()

  // Instantiate OpenAI client
  const openai = new OpenAI({ apiKey: openaiApiKey })

  // Generate a one-time embedding for the user's query
  const embeddingResponse = await openai.embeddings.create({
    model: 'text-embedding-3-large',
    input: query,
    dimensions: 512,
  })

  const [{ embedding }] = embeddingResponse.data

  // Instantiate the Supabase client
  // (replace service role key with user's JWT if using Supabase auth and RLS)
  const supabase = createClient(supabaseUrl, supabaseServiceRoleKey)

  // Call hybrid_search Postgres function via RPC
  const { data: documents } = await supabase.rpc('hybrid_search', {
    query_text: query,
    query_embedding: embedding,
    match_count: 10,
  })

  return new Response(JSON.stringify(documents), {
    headers: { 'Content-Type': 'application/json' },
  })
})
```

This uses OpenAI's `text-embedding-3-large` model to generate embeddings (shortened to 512 dimensions for faster retrieval). Swap in your preferred embedding model (and dimension size) accordingly.

To test this, make a `POST` request to the function's endpoint while passing in a JSON payload containing the user's query. Here is an example `POST` request using cURL:

```tsx
curl -i --location --request POST \
  'http://127.0.0.1:54321/functions/v1/hybrid-search' \
  --header 'Authorization: Bearer <anonymous key>' \
  --header 'Content-Type: application/json' \
  --data '{"query":"Italian recipes with tomato sauce"}'
```

For more information on how to create, test, and deploy edge functions, see [Getting started](/docs/guides/functions/quickstart).



## See also

*   [Embedding concepts](/docs/guides/ai/concepts)
*   [Vector columns](/docs/guides/ai/vector-columns)
*   [Vector indexes](/docs/guides/ai/vector-indexes)
*   [Semantic search](/docs/guides/ai/semantic-search)
*   [Full text (keyword) search](/docs/guides/database/full-text-search)



# Keyword search

Learn how to search by words or phrases.

Keyword search involves locating documents or records that contain specific words or phrases, primarily based on the exact match between the search terms and the text within the data. It differs from [semantic search](/docs/guides/ai/semantic-search), which interprets the meaning behind the query to provide results that are contextually related, even if the exact words aren't present in the text. Semantic search considers synonyms, intent, and natural language nuances to provide a more nuanced approach to information retrieval.

In Postgres, keyword search is implemented using [full-text search](/docs/guides/database/full-text-search). It supports indexing and text analysis for data retrieval, focusing on records that match the search criteria. Postgres' full-text search extends beyond simple keyword matching to address linguistic nuances, making it effective for applications that require precise text queries.



## When and why to use keyword search

Keyword search is particularly useful in scenarios where precision and specificity matter. It's more effective than semantic search when users are looking for information using exact terminology or specific identifiers. It ensures that results directly contain those terms, reducing the chance of retrieving irrelevant information that might be semantically related but not what the user seeks.

For example in technical or academic research databases, researchers often search for specific studies, compounds, or concepts identified by certain terms or codes. Searching for a specific chemical compound using its exact molecular formula or a unique identifier will yield more focused and relevant results compared to a semantic search, which could return a wide range of documents discussing the compound in different contexts. Keyword search ensures documents that explicitly mention the exact term are found, allowing users to access the precise data they need efficiently.

It's also possible to combine keyword search with semantic search to get the best of both worlds. See [Hybrid search](/docs/guides/ai/hybrid-search) for more details.



## Using full-text search

For an in-depth guide to Postgres' full-text search, including how to store, index, and query records, see [Full text search](/docs/guides/database/full-text-search).



## See also

*   [Semantic search](/docs/guides/ai/semantic-search)
*   [Hybrid search](/docs/guides/ai/hybrid-search)



# LangChain



[LangChain](https://langchain.com/) is a popular framework for working with AI, Vectors, and embeddings. LangChain supports using Supabase as a [vector store](https://js.langchain.com/docs/modules/indexes/vector_stores/integrations/supabase), using the `pgvector` extension.



## Initializing your database

Prepare you database with the relevant tables:

<Tabs scrollable size="small" type="underlined" defaultActiveId="dashboard" queryGroup="database-method">
  <TabPanel id="dashboard" label="Dashboard">
    1.  Go to the [SQL Editor](/dashboard/project/_/sql) page in the Dashboard.
    2.  Click **LangChain** in the Quick start section.
    3.  Click **Run**.
  </TabPanel>

  <TabPanel id="sql" label="SQL">
    ```sql
    -- Enable the pgvector extension to work with embedding vectors
    create extension vector;

    -- Create a table to store your documents
    create table documents (
      id bigserial primary key,
      content text, -- corresponds to Document.pageContent
      metadata jsonb, -- corresponds to Document.metadata
      embedding extensions.vector(1536) -- 1536 works for OpenAI embeddings, change if needed
    );

    -- Create a function to search for documents
    create function match_documents (
      query_embedding extensions.vector(1536),
      match_count int default null,
      filter jsonb DEFAULT '{}'
    ) returns table (
      id bigint,
      content text,
      metadata jsonb,
      similarity float
    )
    language plpgsql
    as $$
    #variable_conflict use_column
    begin
      return query
      select
        id,
        content,
        metadata,
        1 - (documents.embedding <=> query_embedding) as similarity
      from documents
      where metadata @> filter
      order by documents.embedding <=> query_embedding
      limit match_count;
    end;
    $$;
    ```
  </TabPanel>
</Tabs>



## Usage

You can now search your documents using any Node.js application. This is intended to be run on a secure server route.

```js
import { SupabaseVectorStore } from '@langchain/community/vectorstores/supabase'
import { OpenAIEmbeddings } from '@langchain/openai'
import { createClient } from '@supabase/supabase-js'

const supabaseKey = process.env.SUPABASE_SERVICE_ROLE_KEY
if (!supabaseKey) throw new Error(`Expected SUPABASE_SERVICE_ROLE_KEY`)

const url = process.env.SUPABASE_URL
if (!url) throw new Error(`Expected env var SUPABASE_URL`)

export const run = async () => {
  const client = createClient(url, supabaseKey)

  const vectorStore = await SupabaseVectorStore.fromTexts(
    ['Hello world', 'Bye bye', "What's this?"],
    [{ id: 2 }, { id: 1 }, { id: 3 }],
    new OpenAIEmbeddings(),
    {
      client,
      tableName: 'documents',
      queryName: 'match_documents',
    }
  )

  const resultOne = await vectorStore.similaritySearch('Hello world', 1)

  console.log(resultOne)
}
```


### Simple metadata filtering

Given the above `match_documents` Postgres function, you can also pass a filter parameter to only return documents with a specific metadata field value. This filter parameter is a JSON object, and the `match_documents` function will use the Postgres JSONB Containment operator `@>` to filter documents by the metadata field values you specify. See details on the [Postgres JSONB Containment operator](https://www.postgresql.org/docs/current/datatype-json.html#JSON-CONTAINMENT) for more information.

```js
import { SupabaseVectorStore } from '@langchain/community/vectorstores/supabase'
import { OpenAIEmbeddings } from '@langchain/openai'
import { createClient } from '@supabase/supabase-js'

// First, follow set-up instructions above

const privateKey = process.env.SUPABASE_SERVICE_ROLE_KEY
if (!privateKey) throw new Error(`Expected env var SUPABASE_SERVICE_ROLE_KEY`)

const url = process.env.SUPABASE_URL
if (!url) throw new Error(`Expected env var SUPABASE_URL`)

export const run = async () => {
  const client = createClient(url, privateKey)

  const vectorStore = await SupabaseVectorStore.fromTexts(
    ['Hello world', 'Hello world', 'Hello world'],
    [{ user_id: 2 }, { user_id: 1 }, { user_id: 3 }],
    new OpenAIEmbeddings(),
    {
      client,
      tableName: 'documents',
      queryName: 'match_documents',
    }
  )

  const result = await vectorStore.similaritySearch('Hello world', 1, {
    user_id: 3,
  })

  console.log(result)
}
```


### Advanced metadata filtering

You can also use query builder-style filtering ([similar to how the Supabase JavaScript library works](/docs/reference/javascript/using-filters)) instead of passing an object. Note that since the filter properties will be in the metadata column, you need to use arrow operators (`->` for integer or `->>` for text) as defined in [PostgREST API documentation](https://postgrest.org/en/stable/references/api/tables_views.html?highlight=operators#json-columns) and specify the data type of the property (e.g. the column should look something like `metadata->some_int_value::int`).

```js
import { SupabaseFilterRPCCall, SupabaseVectorStore } from '@langchain/community/vectorstores/supabase'
import { OpenAIEmbeddings } from '@langchain/openai'
import { createClient } from '@supabase/supabase-js'

// First, follow set-up instructions above

const privateKey = process.env.SUPABASE_SERVICE_ROLE_KEY
if (!privateKey) throw new Error(`Expected env var SUPABASE_SERVICE_ROLE_KEY`)

const url = process.env.SUPABASE_URL
if (!url) throw new Error(`Expected env var SUPABASE_URL`)

export const run = async () => {
  const client = createClient(url, privateKey)

  const embeddings = new OpenAIEmbeddings()

  const store = new SupabaseVectorStore(embeddings, {
    client,
    tableName: 'documents',
  })

  const docs = [
    {
      pageContent:
        'This is a long text, but it actually means something because vector database does not understand Lorem Ipsum. So I would need to expand upon the notion of quantum fluff, a theoretical concept where subatomic particles coalesce to form transient multidimensional spaces. Yet, this abstraction holds no real-world application or comprehensible meaning, reflecting a cosmic puzzle.',
      metadata: { b: 1, c: 10, stuff: 'right' },
    },
    {
      pageContent:
        'This is a long text, but it actually means something because vector database does not understand Lorem Ipsum. So I would need to proceed by discussing the echo of virtual tweets in the binary corridors of the digital universe. Each tweet, like a pixelated canary, hums in an unseen frequency, a fascinatingly perplexing phenomenon that, while conjuring vivid imagery, lacks any concrete implication or real-world relevance, portraying a paradox of multidimensional spaces in the age of cyber folklore.',
      metadata: { b: 2, c: 9, stuff: 'right' },
    },
    { pageContent: 'hello', metadata: { b: 1, c: 9, stuff: 'right' } },
    { pageContent: 'hello', metadata: { b: 1, c: 9, stuff: 'wrong' } },
    { pageContent: 'hi', metadata: { b: 2, c: 8, stuff: 'right' } },
    { pageContent: 'bye', metadata: { b: 3, c: 7, stuff: 'right' } },
    { pageContent: "what's this", metadata: { b: 4, c: 6, stuff: 'right' } },
  ]

  await store.addDocuments(docs)

  const funcFilterA: SupabaseFilterRPCCall = (rpc) =>
    rpc
      .filter('metadata->b::int', 'lt', 3)
      .filter('metadata->c::int', 'gt', 7)
      .textSearch('content', `'multidimensional' & 'spaces'`, {
        config: 'english',
      })

  const resultA = await store.similaritySearch('quantum', 4, funcFilterA)

  const funcFilterB: SupabaseFilterRPCCall = (rpc) =>
    rpc
      .filter('metadata->b::int', 'lt', 3)
      .filter('metadata->c::int', 'gt', 7)
      .filter('metadata->>stuff', 'eq', 'right')

  const resultB = await store.similaritySearch('hello', 2, funcFilterB)

  console.log(resultA, resultB)
}
```



## Hybrid search

LangChain supports the concept of a hybrid search, which combines Similarity Search with Full Text Search. Read the official docs to get started: [Supabase Hybrid Search](https://js.langchain.com/docs/modules/indexes/retrievers/supabase-hybrid).

You can install the LangChain Hybrid Search function though our [database.dev package manager](https://database.dev/langchain/hybrid_search).



## Resources

*   Official [LangChain site](https://langchain.com/).
*   Official [LangChain docs](https://js.langchain.com/docs/modules/indexes/vector_stores/integrations/supabase).
*   Supabase [Hybrid Search](https://js.langchain.com/docs/modules/indexes/retrievers/supabase-hybrid).



# Choosing a Client



As described in [Structured & Unstructured Embeddings](/docs/guides/ai/structured-unstructured), AI workloads come in many forms.

For data science or ephemeral workloads, the [Supabase Vecs](https://supabase.github.io/vecs/) client gets you started quickly. All you need is a connection string and vecs handles setting up your database to store and query vectors with associated metadata.

<Admonition type="tip">
  Click [**Connect**](/dashboard/project/_/?showConnect=true) at the top of any project page to get your connection string.

  Copy the URI from the **Shared pooler** option.
</Admonition>

For production python applications with version controlled migrations, we recommend adding first class vector support to your toolchain by [registering the vector type with your ORM](https://github.com/pgvector/pgvector-python). pgvector provides bindings for the most commonly used SQL drivers/libraries including Django, SQLAlchemy, SQLModel, psycopg, asyncpg and Peewee.



# RAG with Permissions

Fine-grain access control with Retrieval Augmented Generation.

Since pgvector is built on top of Postgres, you can implement fine-grain access control on your vector database using [Row Level Security (RLS)](/docs/guides/database/postgres/row-level-security). This means you can restrict which documents are returned during a vector similarity search to users that have access to them. Supabase also supports [Foreign Data Wrappers (FDW)](/docs/guides/database/extensions/wrappers/overview) which means you can use an external database or data source to determine these permissions if your user data doesn't exist in Supabase.

Use this guide to learn how to restrict access to documents when performing retrieval augmented generation (RAG).



## Example

In a typical RAG setup, your documents are chunked into small subsections and similarity is performed over those sections:

```sql
-- Track documents/pages/files/etc
create table documents (
  id bigint primary key generated always as identity,
  name text not null,
  owner_id uuid not null references auth.users (id) default auth.uid(),
  created_at timestamp with time zone not null default now()
);

-- Store the content and embedding vector for each section in the document
-- with a reference to original document (one-to-many)
create table document_sections (
  id bigint primary key generated always as identity,
  document_id bigint not null references documents (id),
  content text not null,
  embedding extensions.vector (384)
);
```

Notice how we record the `owner_id` on each document. Let's create an RLS policy that restricts access to `document_sections` based on whether or not they own the linked document:

```sql
-- enable row level security
alter table document_sections enable row level security;

-- setup RLS for select operations
create policy "Users can query their own document sections"
on document_sections for select to authenticated using (
  document_id in (
    select id
    from documents
    where (owner_id = (select auth.uid()))
  )
);
```

<Admonition type="tip">
  In this example, the current user is determined using the built-in `auth.uid()` function when the query is executed through your project's auto-generated [REST API](/docs/guides/api). If you are connecting to your Supabase database through a direct Postgres connection, see [Direct Postgres Connection](#direct-postgres-connection) below for directions on how to achieve the same access control.
</Admonition>

Now every `select` query executed on `document_sections` will implicitly filter the returned sections based on whether or not the current user has access to them.

For example, executing:

```sql
select * from document_sections;
```

as an authenticated user will only return rows that they are the owner of (as determined by the linked document). More importantly, semantic search over these sections (or any additional filtering for that matter) will continue to respect these RLS policies:

```sql
-- Perform inner product similarity based on a match_threshold
select *
from document_sections
where document_sections.embedding <#> embedding < -match_threshold
order by document_sections.embedding <#> embedding;
```

The above example only configures `select` access to users. If you wanted, you could create more RLS policies for inserts, updates, and deletes in order to apply the same permission logic for those other operations. See [Row Level Security](/docs/guides/database/postgres/row-level-security) for a more in-depth guide on RLS policies.



## Alternative scenarios

Every app has its own unique requirements and may differ from the above example. Here are some alternative scenarios we often see and how they are implemented in Supabase.


### Documents owned by multiple people

Instead of a one-to-many relationship between `users` and `documents`, you may require a many-to-many relationship so that multiple people can access the same document. Let's reimplement this using a join table:

```sql
create table document_owners (
  id bigint primary key generated always as identity,
  owner_id uuid not null references auth.users (id) default auth.uid(),
  document_id bigint not null references documents (id)
);
```

Then your RLS policy would change to:

```sql
create policy "Users can query their own document sections"
on document_sections for select to authenticated using (
  document_id in (
    select document_id
    from document_owners
    where (owner_id = (select auth.uid()))
  )
);
```

Instead of directly querying the `documents` table, we query the join table.


### User and document data live outside of Supabase

You may have an existing system that stores users, documents, and their permissions in a separate database. Let's explore the scenario where this data exists in another Postgres database. We'll use a foreign data wrapper (FDW) to connect to the external DB from within your Supabase DB:

<Admonition type="caution">
  RLS is latency-sensitive, so extra caution should be taken before implementing this method. Use the [query plan analyzer](/docs/guides/platform/performance#optimizing-poor-performing-queries) to measure execution times for your queries to ensure they are within expected ranges. For enterprise applications, contact [enterprise@supabase.io](mailto:enterprise@supabase.io).
</Admonition>

<Admonition type="tip">
  For data sources other than Postgres, see [Foreign Data Wrappers](/docs/guides/database/extensions/wrappers/overview) for a list of external sources supported today. If your data lives in a source not provided in the list, contact [support](/dashboard/support/new) and we'll be happy to discuss your use case.
</Admonition>

Let's assume your external DB contains a `users` and `documents` table like this:

```sql
create table public.users (
  id bigint primary key generated always as identity,
  email text not null,
  created_at timestamp with time zone not null default now()
);

create table public.documents (
  id bigint primary key generated always as identity,
  name text not null,
  owner_id bigint not null references public.users (id),
  created_at timestamp with time zone not null default now()
);
```

In your Supabase DB, let's create foreign tables that link to the above tables:

```sql
create schema external;
create extension postgres_fdw with schema extensions;

-- Setup the foreign server
create server foreign_server
  foreign data wrapper postgres_fdw
  options (host '<db-host>', port '<db-port>', dbname '<db-name>');

-- Map local 'authenticated' role to external 'postgres' user
create user mapping for authenticated
  server foreign_server
  options (user 'postgres', password '<user-password>');

-- Import foreign 'users' and 'documents' tables into 'external' schema
import foreign schema public limit to (users, documents)
  from server foreign_server into external;
```

<Admonition type="tip">
  This example maps the `authenticated` role in Supabase to the `postgres` user in the external DB. In production, it's best to create a custom user on the external DB that has the minimum permissions necessary to access the information you need.

  On the Supabase DB, we use the built-in `authenticated` role which is automatically used when end users make authenticated requests over your auto-generated REST API. If you plan to connect to your Supabase DB over a direct Postgres connection instead of the REST API, you can change this to any user you like. See [Direct Postgres Connection](#direct-postgres-connection) for more info.
</Admonition>

We'll store `document_sections` and their embeddings in Supabase so that we can perform similarity search over them via pgvector.

```sql
create table document_sections (
  id bigint primary key generated always as identity,
  document_id bigint not null,
  content text not null,
  embedding extensions.vector (384)
);
```

We maintain a reference to the foreign document via `document_id`, but without a foreign key reference since foreign keys can only be added to local tables. Be sure to use the same ID data type that you use on your external documents table.

Since we're managing users and authentication outside of Supabase, we have two options:

1.  Make a direct Postgres connection to the Supabase DB and set the current user every request
2.  Issue a custom JWT from your system and use it to authenticate with the REST API


#### Direct Postgres connection

You can directly connect to your Supabase Postgres DB using the [connection info](/dashboard/project/_/?showConnect=true) on a project page. To use RLS with this method, we use a custom session variable that contains the current user's ID:

```sql
-- enable row level security
alter table document_sections enable row level security;

-- setup RLS for select operations
create policy "Users can query their own document sections"
on document_sections for select to authenticated using (
  document_id in (
    select id
    from external.documents
    where owner_id = current_setting('app.current_user_id')::bigint
  )
);
```

The session variable is accessed through the `current_setting()` function. We name the variable `app.current_user_id` here, but you can modify this to any name you like. We also cast it to a `bigint` since that was the data type of the `user.id` column. Change this to whatever data type you use for your ID.

Now for every request, we set the user's ID at the beginning of the session:

```sql
set app.current_user_id = '<current-user-id>';
```

Then all subsequent queries will inherit the permission of that user:

```sql
-- Only document sections owned by the user are returned
select *
from document_sections
where document_sections.embedding <#> embedding < -match_threshold
order by document_sections.embedding <#> embedding;
```

<Admonition type="caution">
  {/* supa-mdx-lint-disable-next-line Rule004ExcludeWords */}

  You might be tempted to discard RLS completely and simply filter by user within the `where` clause. Though this will work, we recommend RLS as a general best practice since RLS is always applied even as new queries and application logic is introduced in the future.
</Admonition>


#### Custom JWT with REST API

If you would like to use the auto-generated REST API to query your Supabase database using JWTs from an external auth provider, you can get your auth provider to issue a custom JWT for Supabase.

See the [Clerk Supabase docs](https://clerk.com/docs/integrations/databases/supabase) for an example of how this can be done. Modify the instructions to work with your own auth provider as needed.

Now we can use the same RLS policy from our first example:

```sql
-- enable row level security
alter table document_sections enable row level security;

-- setup RLS for select operations
create policy "Users can query their own document sections"
on document_sections for select to authenticated using (
  document_id in (
    select id
    from documents
    where (owner_id = (select auth.uid()))
  )
);
```

Under the hood, `auth.uid()` references `current_setting('request.jwt.claim.sub')` which corresponds to the JWT's `sub` (subject) claim. This setting is automatically set at the beginning of each request to the REST API.

All subsequent queries will inherit the permission of that user:

```sql
-- Only document sections owned by the user are returned
select *
from document_sections
where document_sections.embedding <#> embedding < -match_threshold
order by document_sections.embedding <#> embedding;
```


### Other scenarios

There are endless approaches to this problem based on the complexities of each system. Luckily Postgres comes with all the primitives needed to provide access control in the way that works best for your project.

If the examples above didn't fit your use case or you need to adjust them slightly to better fit your existing system, feel free to reach out to [support](/dashboard/support/new) and we'll be happy to assist you.



# Semantic search

Learn how to search by meaning rather than exact keywords.

Semantic search interprets the meaning behind user queries rather than exact [keywords](/docs/guides/ai/keyword-search). It uses machine learning to capture the intent and context behind the query, handling language nuances like synonyms, phrasing variations, and word relationships.



## When to use semantic search

Semantic search is useful in applications where the depth of understanding and context is important for delivering relevant results. A good example is in customer support or knowledge base search engines. Users often phrase their problems or questions in various ways, and a traditional keyword-based search might not always retrieve the most helpful documents. With semantic search, the system can understand the meaning behind the queries and match them with relevant solutions or articles, even if the exact wording differs.

For instance, a user searching for "increase text size on display" might miss articles titled "How to adjust font size in settings" in a keyword-based search system. However, a semantic search engine would understand the intent behind the query and correctly match it to relevant articles, regardless of the specific terminology used.

It's also possible to combine semantic search with keyword search to get the best of both worlds. See [Hybrid search](/docs/guides/ai/hybrid-search) for more details.



## How semantic search works

Semantic search uses an intermediate representation called an “embedding vector” to link database records with search queries. A vector, in the context of semantic search, is a list of numerical values. They represent various features of the text and allow for the semantic comparison between different pieces of text.

The best way to think of embeddings is by plotting them on a graph, where each embedding is a single point whose coordinates are the numerical values within its vector. Importantly, embeddings are plotted such that similar concepts are positioned close together while dissimilar concepts are far apart. For more details, see [What are embeddings?](/docs/guides/ai/concepts#what-are-embeddings)

Embeddings are generated using a language model, and embeddings are compared to each other using a similarity metric. The language model is trained to understand the semantics of language, including syntax, context, and the relationships between words. It generates embeddings for both the content in the database and the search queries. Then the similarity metric, often a function like cosine similarity or dot product, is used to compare the query embeddings with the document embeddings (in other words, to measure how close they are to each other on the graph). The documents with embeddings most similar to the query's are deemed the most relevant and are returned as search results.



## Embedding models

There are many embedding models available today. Supabase Edge Functions has [built in support](/docs/guides/functions/examples/semantic-search) for the `gte-small` model. Others can be accessed through third-party APIs like [OpenAI](https://platform.openai.com/docs/guides/embeddings), where you send your text in the request and receive an embedding vector in the response. Others can run locally on your own compute, such as through Transformers.js for JavaScript implementations. For more information on local implementation, see [Generate embeddings](/docs/guides/ai/quickstarts/generate-text-embeddings).

It's crucial to remember that when using embedding models with semantic search, you must use the same model for all embedding comparisons. Comparing embeddings created by different models will yield meaningless results.



## Semantic search in Postgres

To implement semantic search in Postgres we use `pgvector` - an extension that allows for efficient storage and retrieval of high-dimensional vectors. These vectors are numerical representations of text (or other types of data) generated by embedding models.

1.  Enable the `pgvector` extension by running:

    ```sql
    create extension vector
    with
      schema extensions;
    ```

2.  Create a table to store the embeddings:

    ```sql
    create table documents (
      id bigint primary key generated always as identity,
      content text,
      embedding extensions.vector(512)
    );
    ```

    Or if you have an existing table, you can add a vector column like so:

    ```sql
    alter table documents
    add column embedding extensions.vector(512);
    ```

    In this example, we create a column named `embedding` which uses the newly enabled `vector` data type. The size of the vector (as indicated in parentheses) represents the number of dimensions in the embedding. Here we use 512, but adjust this to match the number of dimensions produced by your embedding model.

For more details on vector columns, including how to generate embeddings and store them, see [Vector columns](/docs/guides/ai/vector-columns).


### Similarity metric

`pgvector` support 3 operators for computing distance between embeddings:

| **Operator** | **Description**        |
| ------------ | ---------------------- |
| `<->`        | Euclidean distance     |
| `<#>`        | negative inner product |
| `<=>`        | cosine distance        |

These operators are used directly in your SQL query to retrieve records that are most similar to the user's search query. Choosing the right operator depends on your needs. Inner product (also known as dot product) tends to be the fastest if your vectors are normalized.

The easiest way to perform semantic search in Postgres is by creating a function:

```sql
-- Match documents using cosine distance (<=>)
create or replace function match_documents (
  query_embedding extensions.vector(512),
  match_threshold float,
  match_count int
)
returns setof documents
language sql
as $$
  select *
  from documents
  where documents.embedding <=> query_embedding < 1 - match_threshold
  order by documents.embedding <=> query_embedding asc
  limit least(match_count, 200);
$$;
```

Here we create a function `match_documents` that accepts three parameters:

1.  `query_embedding`: a one-time embedding generated for the user's search query. Here we set the size to 512, but adjust this to match the number of dimensions produced by your embedding model.
2.  `match_threshold`: the minimum similarity between embeddings. This is a value between 1 and -1, where 1 is most similar and -1 is most dissimilar.
3.  `match_count`: the maximum number of results to return. Note the query may return less than this number if `match_threshold` resulted in a small shortlist. Limited to 200 records to avoid unintentionally overloading your database.

In this example, we return a `setof documents` and refer to `documents` throughout the query. Adjust this to use the relevant tables in your application.

You'll notice we are using the cosine distance (`<=>`) operator in our query. Cosine distance is a safe default when you don't know whether or not your embeddings are normalized. If you know for a fact that they are normalized (for example, your embedding is returned from OpenAI), you can use negative inner product (`<#>`) for better performance:

```sql
-- Match documents using negative inner product (<#>)
create or replace function match_documents (
  query_embedding extensions.vector(512),
  match_threshold float,
  match_count int
)
returns setof documents
language sql
as $$
  select *
  from documents
  where documents.embedding <#> query_embedding < -match_threshold
  order by documents.embedding <#> query_embedding asc
  limit least(match_count, 200);
$$;
```

Note that since `<#>` is negative, we negate `match_threshold` accordingly in the `where` clause. For more information on the different operators, see the [pgvector docs](https://github.com/pgvector/pgvector?tab=readme-ov-file#vector-operators).


### Calling from your application

Finally you can execute this function from your application. If you are using a Supabase client library such as [`supabase-js`](https://github.com/supabase/supabase-js), you can invoke it using the `rpc()` method:

```tsx
const { data: documents } = await supabase.rpc('match_documents', {
  query_embedding: embedding, // pass the query embedding
  match_threshold: 0.78, // choose an appropriate threshold for your data
  match_count: 10, // choose the number of matches
})
```

You can also call this method directly from SQL:

```sql
select *
from match_documents(
  '[...]'::extensions.vector(512), -- pass the query embedding
  0.78, -- chose an appropriate threshold for your data
  10 -- choose the number of matches
);
```

In this scenario, you'll likely use a Postgres client library to establish a direct connection from your application to the database. It's best practice to parameterize your arguments before executing the query.



## Next steps

As your database scales, you will need an index on your vector columns to maintain fast query speeds. See [Vector indexes](/docs/guides/ai/vector-indexes) for an in-depth guide on the different types of indexes and how they work.



## See also

*   [Embedding concepts](/docs/guides/ai/concepts)
*   [Vector columns](/docs/guides/ai/vector-columns)
*   [Vector indexes](/docs/guides/ai/vector-indexes)
*   [Hybrid search](/docs/guides/ai/hybrid-search)
*   [Keyword search](/docs/guides/ai/keyword-search)



# Structured and Unstructured

Supabase is flexible enough to associate structured and unstructured metadata with embeddings.

Most vector stores treat metadata associated with embeddings like NoSQL, unstructured data. Supabase is flexible enough to store unstructured and structured metadata.



## Structured

```sql
create table docs (
  id uuid primary key,
  embedding extensions.vector(3),
  content text,
  url text
);

insert into docs
  (id, embedding, content, url)
values
  ('79409372-7556-4ccc-ab8f-5786a6cfa4f7', array[0.1, 0.2, 0.3], 'Hello world', '/hello-world');
```

Notice that we've associated two pieces of metadata, `content` and `url`, with the embedding. Those fields can be filtered, constrained, indexed, and generally operated on using the full power of SQL. Structured metadata fits naturally with a traditional Supabase application, and can be managed via database [migrations](/docs/guides/deployment/database-migrations).



## Unstructured

```sql
create table docs (
  id uuid primary key,
  embedding extensions.vector(3),
  meta jsonb
);

insert into docs
  (id, embedding, meta)
values
  (
    '79409372-7556-4ccc-ab8f-5786a6cfa4f7',
    array[0.1, 0.2, 0.3],
    '{"content": "Hello world", "url": "/hello-world"}'
  );
```

An unstructured approach does not specify the metadata fields that are expected. It stores all metadata in a flexible `json`/`jsonb` column. The tradeoff is that the querying/filtering capabilities of a schemaless data type are less flexible than when each field has a dedicated column. It also pushes the burden of metadata data integrity onto application code, which is more error prone than enforcing constraints in the database.

The unstructured approach is recommended:

*   for ephemeral/interactive workloads e.g. data science or scientific research
*   when metadata fields are user-defined or unknown
*   during rapid prototyping

Client libraries like python's [vecs](https://github.com/supabase/vecs) use this structure. For example, running:

```py
#!/usr/bin/env python3
import vecs


# In practice, do not hard-code your password. Use environment variables.
DB_CONNECTION = "postgresql://<user>:<password>@<host>:<port>/<db_name>"


# create vector store client
vx = vecs.create_client(DB_CONNECTION)

docs = vx.get_or_create_collection(name="docs", dimension=1536)

docs.upsert(vectors=[
  ('79409372-7556-4ccc-ab8f-5786a6cfa4f7', [100, 200, 300], { url: '/hello-world' })
])

```

automatically creates the unstructured SQL table during the call to `get_or_create_collection`.

Note that when working with client libraries that emit SQL DDL, like `create table ...`, you should add that SQL to your migrations when moving to production to maintain a single source of truth for your database's schema.



## Hybrid

The structured metadata style is recommended when the fields being tracked are known in advance. If you have a combination of known and unknown metadata fields, you can accommodate the unknown fields by adding a `json`/`jsonb` column to the table. In that situation, known fields should continue to use dedicated columns for best query performance and throughput.

```sql
create table docs (
  id uuid primary key,
  embedding extensions.vector(3),
  content text,
  url string,
  meta jsonb
);

insert into docs
  (id, embedding, content, url, meta)
values
  (
    '79409372-7556-4ccc-ab8f-5786a6cfa4f7',
    array[0.1, 0.2, 0.3],
    'Hello world',
    '/hello-world',
    '{"key": "value"}'
  );
```



## Choosing the right model

Both approaches create a table where you can store your embeddings and some metadata. You should choose the best approach for your use-case. In summary:

*   Structured metadata is best when fields are known in advance or query patterns are predictable e.g. a production Supabase application
*   Unstructured metadata is best when fields are unknown/user-defined or when working with data interactively e.g. exploratory research

Both approaches are valid, and the one you should choose depends on your use-case.



# Python client

Manage unstructured vector stores in PostgreSQL.

Supabase provides a Python client called [`vecs`](https://github.com/supabase/vecs) for managing unstructured vector stores. This client provides a set of useful tools for creating and querying collections in Postgres using the [pgvector](/docs/guides/database/extensions/pgvector) extension.



## Quick start

Let's see how Vecs works using a local database. Make sure you have the Supabase CLI [installed](/docs/guides/cli#installation) on your machine.


### Initialize your project

Start a local Postgres instance in any folder using the `init` and `start` commands. Make sure you have Docker running!

```bash

# Initialize your project
supabase init


# Start Postgres
supabase start
```


### Create a collection

Inside a Python shell, run the following commands to create a new collection called "docs", with 3 dimensions.

```py
import vecs


# create vector store client
vx = vecs.create_client("postgresql://postgres:postgres@localhost:54322/postgres")


# create a collection of vectors with 3 dimensions
docs = vx.get_or_create_collection(name="docs", dimension=3)
```


### Add embeddings

Now we can insert some embeddings into our "docs" collection using the `upsert()` command:

```py
import vecs


# create vector store client
docs = vecs.get_or_create_collection(name="docs", dimension=3)


# a collection of vectors with 3 dimensions
vectors=[
  ("vec0", [0.1, 0.2, 0.3], {"year": 1973}),
  ("vec1", [0.7, 0.8, 0.9], {"year": 2012})
]


# insert our vectors
docs.upsert(vectors=vectors)
```


### Query the collection

You can now query the collection to retrieve a relevant match:

```py
import vecs

docs = vecs.get_or_create_collection(name="docs", dimension=3)


# query the collection filtering metadata for "year" = 2012
docs.query(
    data=[0.4,0.5,0.6],      # required
    limit=1,                         # number of records to return
    filters={"year": {"$eq": 2012}}, # metadata filters
)
```



## Deep dive

For a more in-depth guide on `vecs` collections, see [API](/docs/guides/ai/python/api).



## Resources

*   Official Vecs Documentation: [https://supabase.github.io/vecs/api](https://supabase.github.io/vecs/api)
*   Source Code: [https://github.com/supabase/vecs](https://github.com/supabase/vecs)



# Vector columns



Supabase offers a number of different ways to store and query vectors within Postgres. The SQL included in this guide is applicable for clients in all programming languages. If you are a Python user see your [Python client options](/docs/guides/ai/python-clients) after reading the `Learn` section.

Vectors in Supabase are enabled via [pgvector](https://github.com/pgvector/pgvector/), a Postgres extension for storing and querying vectors in Postgres. It can be used to store [embeddings](/docs/guides/ai/concepts#what-are-embeddings).



## Usage


### Enable the extension

<Tabs scrollable size="small" type="underlined" defaultActiveId="dashboard" queryGroup="database-method">
  <TabPanel id="dashboard" label="Dashboard">
    1.  Go to the [Database](/dashboard/project/_/database/tables) page in the Dashboard.
    2.  Click on **Extensions** in the sidebar.
    3.  Search for "vector" and enable the extension.
  </TabPanel>

  <TabPanel id="sql" label="SQL">
    ```sql
     -- Example: enable the "vector" extension.
    create extension vector
    with
      schema extensions;

    -- Example: disable the "vector" extension
    drop
      extension if exists vector;
    ```

    Even though the SQL code is `create extension`, this is the equivalent of "enabling the extension".
    To disable an extension, call `drop extension`.
  </TabPanel>
</Tabs>


### Create a table to store vectors

After enabling the `vector` extension, you will get access to a new data type called `vector`. The size of the vector (indicated in parenthesis) represents the number of dimensions stored in that vector.

```sql
create table documents (
  id serial primary key,
  title text not null,
  body text not null,
  embedding extensions.vector(384)
);
```

In the above SQL snippet, we create a `documents` table with a column called `embedding` (note this is just a regular Postgres column - you can name it whatever you like). We give the `embedding` column a `vector` data type with 384 dimensions. Change this to the number of dimensions produced by your embedding model. For example, if you are [generating embeddings](/docs/guides/ai/quickstarts/generate-text-embeddings) using the open source [`gte-small`](https://huggingface.co/Supabase/gte-small) model, you would set this number to 384 since that model produces 384 dimensions.

<Admonition type="tip">
  In general, embeddings with fewer dimensions perform best. See our [analysis on fewer dimensions in pgvector](/blog/fewer-dimensions-are-better-pgvector).
</Admonition>


### Storing a vector / embedding

In this example we'll generate a vector using Transformers.js, then store it in the database using the Supabase JavaScript client.

```js
import { pipeline } from '@xenova/transformers'
const generateEmbedding = await pipeline('feature-extraction', 'Supabase/gte-small')

const title = 'First post!'
const body = 'Hello world!'

// Generate a vector using Transformers.js
const output = await generateEmbedding(body, {
  pooling: 'mean',
  normalize: true,
})

// Extract the embedding output
const embedding = Array.from(output.data)

// Store the vector in Postgres
const { data, error } = await supabase.from('documents').insert({
  title,
  body,
  embedding,
})
```

This example uses the JavaScript Supabase client, but you can modify it to work with any [supported language library](/docs#client-libraries).


### Querying a vector / embedding

Similarity search is the most common use case for vectors. `pgvector` support 3 new operators for computing distance:

| Operator | Description            |
| -------- | ---------------------- |
| `<->`    | Euclidean distance     |
| `<#>`    | negative inner product |
| `<=>`    | cosine distance        |

Choosing the right operator depends on your needs. Dot product tends to be the fastest if your vectors are normalized. For more information on how embeddings work and how they relate to each other, see [What are Embeddings?](/docs/guides/ai/concepts#what-are-embeddings).

Supabase client libraries like `supabase-js` connect to your Postgres instance via [PostgREST](/docs/guides/getting-started/architecture#postgrest-api). PostgREST does not currently support `pgvector` similarity operators, so we'll need to wrap our query in a Postgres function and call it via the `rpc()` method:

```sql
create or replace function match_documents (
  query_embedding extensions.vector(384),
  match_threshold float,
  match_count int
)
returns table (
  id bigint,
  title text,
  body text,
  similarity float
)
language sql stable
as $$
  select
    documents.id,
    documents.title,
    documents.body,
    1 - (documents.embedding <=> query_embedding) as similarity
  from documents
  where 1 - (documents.embedding <=> query_embedding) > match_threshold
  order by (documents.embedding <=> query_embedding) asc
  limit match_count;
$$;
```

This function takes a `query_embedding` argument and compares it to all other embeddings in the `documents` table. Each comparison returns a similarity score. If the similarity is greater than the `match_threshold` argument, it is returned. The number of rows returned is limited by the `match_count` argument.

Feel free to modify this method to fit the needs of your application. The `match_threshold` ensures that only documents that have a minimum similarity to the `query_embedding` are returned. Without this, you may end up returning documents that subjectively don't match. This value will vary for each application - you will need to perform your own testing to determine the threshold that makes sense for your app.

If you index your vector column, ensure that the `order by` sorts by the distance function directly (rather than sorting by the calculated `similarity` column, which may lead to the index being ignored and poor performance).

To execute the function from your client library, call `rpc()` with the name of your Postgres function:

```ts
const { data: documents } = await supabaseClient.rpc('match_documents', {
  query_embedding: embedding, // Pass the embedding you want to compare
  match_threshold: 0.78, // Choose an appropriate threshold for your data
  match_count: 10, // Choose the number of matches
})
```

In this example `embedding` would be another embedding you wish to compare against your table of pre-generated embedding documents. For example if you were building a search engine, every time the user submits their query you would first generate an embedding on the search query itself, then pass it into the above `rpc()` function to match.

<Admonition type="tip">
  Be sure to use embeddings produced from the same embedding model when calculating distance. Comparing embeddings from two different models will produce no meaningful result.
</Admonition>

Vectors and embeddings can be used for much more than search. Learn more about embeddings at [What are Embeddings?](/docs/guides/ai/concepts#what-are-embeddings).


### Indexes

Once your vector table starts to grow, you will likely want to add an index to speed up queries. See [Vector indexes](/docs/guides/ai/vector-indexes) to learn how vector indexes work and how to create them.



# Vector indexes



Once your vector table starts to grow, you will likely want to add an index to speed up queries. Without indexes, you'll be performing a sequential scan which can be a resource-intensive operation when you have many records.



## Choosing an index

Today `pgvector` supports two types of indexes:

*   [HNSW](/docs/guides/ai/vector-indexes/hnsw-indexes)
*   [IVFFlat](/docs/guides/ai/vector-indexes/ivf-indexes)

In general we recommend using [HNSW](/docs/guides/ai/vector-indexes/hnsw-indexes) because of its [performance](/blog/increase-performance-pgvector-hnsw#hnsw-performance-1536-dimensions) and [robustness against changing data](/docs/guides/ai/vector-indexes/hnsw-indexes#when-should-you-create-hnsw-indexes).



## Distance operators

Indexes can be used to improve performance of nearest neighbor search using various distance measures. `pgvector` includes 3 distance operators:

| Operator | Description            | [**Operator class**](https://www.postgresql.org/docs/current/sql-createopclass.html) |
| -------- | ---------------------- | ------------------------------------------------------------------------------------ |
| `<->`    | Euclidean distance     | `vector_l2_ops`                                                                      |
| `<#>`    | negative inner product | `vector_ip_ops`                                                                      |
| `<=>`    | cosine distance        | `vector_cosine_ops`                                                                  |

For pgvector versions 0.7.0 and above, it's possible to create indexes on vectors with the following maximum dimensions:

*   vector: up to 2,000 dimensions
*   halfvec: up to 4,000 dimensions
*   bit: up to 64,000 dimensions

You can check your current pgvector version by running: `SELECT * FROM pg_extension WHERE extname = 'vector';` or by navigating to the [Extensions](/dashboard/project/_/database/extensions) tab in your Supabase project dashboard.

If you are on an earlier version of pgvector, you should [upgrade your project here](/dashboard/project/_/settings/infrastructure).



## Resources

Read more about indexing on `pgvector`'s [GitHub page](https://github.com/pgvector/pgvector#indexing).



# HNSW indexes



HNSW is an algorithm for approximate nearest neighbor search. It is a frequently used index type that can improve performance when querying highly-dimensional vectors, like those representing embeddings.



## Usage

The way you create an HNSW index depends on the distance operator you are using. `pgvector` includes 3 distance operators:

| Operator | Description            | [**Operator class**](https://www.postgresql.org/docs/current/sql-createopclass.html) |
| -------- | ---------------------- | ------------------------------------------------------------------------------------ |
| `<->`    | Euclidean distance     | `vector_l2_ops`                                                                      |
| `<#>`    | negative inner product | `vector_ip_ops`                                                                      |
| `<=>`    | cosine distance        | `vector_cosine_ops`                                                                  |

Use the following SQL commands to create an HNSW index for the operator(s) used in your queries.


### Euclidean L2 distance (`vector_l2_ops`)

```sql
create index on items using hnsw (column_name vector_l2_ops);
```


### Inner product (`vector_ip_ops`)

```sql
create index on items using hnsw (column_name vector_ip_ops);
```


### Cosine distance (`vector_cosine_ops`)

```sql
create index on items using hnsw (column_name vector_cosine_ops);
```

For pgvector versions 0.7.0 and above, it's possible to create indexes on vectors with the following maximum dimensions:

*   vector: up to 2,000 dimensions
*   halfvec: up to 4,000 dimensions
*   bit: up to 64,000 dimensions

You can check your current pgvector version by running: `SELECT * FROM pg_extension WHERE extname = 'vector';` or by navigating to the [Extensions](/dashboard/project/_/database/extensions) tab in your Supabase project dashboard.

If you are on an earlier version of pgvector, you should [upgrade your project here](/dashboard/project/_/settings/infrastructure).



## Example with high-dimensional vectors

For vectors with more than 2,000 dimensions, you can use the `halfvec` type to create indexes. Here's an example with 3,072 dimensions:

```sql
CREATE TABLE documents (
    id bigint GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    content text,
    embedding vector(3072)
);

CREATE INDEX ON documents
    USING hnsw ((embedding::halfvec(3072)) halfvec_cosine_ops);
```



## How does HNSW work?

HNSW uses proximity graphs (graphs connecting nodes based on distance between them) to approximate nearest-neighbor search. To understand HNSW, we can break it down into 2 parts:

*   **Hierarchical (H):** The algorithm operates over multiple layers
*   **Navigable Small World (NSW):** Each vector is a node within a graph and is connected to several other nodes


### Hierarchical

The hierarchical aspect of HNSW builds off of the idea of skip lists.

Skip lists are multi-layer linked lists. The bottom layer is a regular linked list connecting an ordered sequence of elements. Each new layer above removes some elements from the underlying layer (based on a fixed probability), producing a sparser subsequence that “skips” over elements.

<Image
  alt="visual of an example skip list"
  src={{
    light: '/docs/img/ai/vector-indexes/hnsw-indexes/skip-list--light.png',
    dark: '/docs/img/ai/vector-indexes/hnsw-indexes/skip-list--dark.png',
  }}
/>

When searching for an element, the algorithm begins at the top layer and traverses its linked list horizontally. If the target element is found, the algorithm stops and returns it. Otherwise if the next element in the list is greater than the target (or `NULL`), the algorithm drops down to the next layer below. Since each layer below is less sparse than the layer above (with the bottom layer connecting all elements), the target will eventually be found. Skip lists offer O(log n) average complexity for both search and insertion/deletion.


### Navigable Small World

A navigable small world (NSW) is a special type of proximity graph that also includes long-range connections between nodes. These long-range connections support the “small world” property of the graph, meaning almost every node can be reached from any other node within a few hops. Without these additional long-range connections, many hops would be required to reach a far-away node.

<Image alt="visual of an example navigable small world graph" src="/docs/img/ai/vector-indexes/hnsw-indexes/nsw.png" className="max-h-[600px] mx-auto" zoomable />

The “navigable” part of NSW specifically refers to the ability to logarithmically scale the greedy search algorithm on the graph, an algorithm that attempts to make only the locally optimal choice at each hop. Without this property, the graph may still be considered a small world with short paths between far-away nodes, but the greedy algorithm tends to miss them. Greedy search is ideal for NSW because it is quick to navigate and has low computational costs.


### **Hierarchical +** Navigable Small World

HNSW combines these two concepts. From the hierarchical perspective, the bottom layer consists of a NSW made up of short links between nodes. Each layer above “skips” elements and creates longer links between nodes further away from each other.

Just like skip lists, search starts at the top layer and works its way down until it finds the target element. However, instead of comparing a scalar value at each layer to determine whether or not to descend to the layer below, a multi-dimensional distance measure (such as Euclidean distance) is used.



## When should you create HNSW indexes?

HNSW should be your default choice when creating a vector index. Add the index when you don't need 100% accuracy and are willing to trade a small amount of accuracy for a lot of throughput.

Unlike IVFFlat indexes, you are safe to build an HNSW index immediately after the table is created. HNSW indexes are based on graphs which inherently are not affected by the same limitations as IVFFlat. As new data is added to the table, the index will be filled automatically and the index structure will remain optimal.



## Resources

Read more about indexing on `pgvector`'s [GitHub page](https://github.com/pgvector/pgvector#indexing).



---
**Navigation:** [← Previous](./39-understanding-api-keys.md) | [Index](./index.md) | [Next →](./41-ivfflat-indexes.md)
