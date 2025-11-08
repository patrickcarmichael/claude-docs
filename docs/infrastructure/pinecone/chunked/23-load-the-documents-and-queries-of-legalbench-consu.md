**Navigation:** [← Previous](./22-pulumi.md) | [Index](./index.md) | [Next →](./24-list-collections.md)

# load the documents and queries of legalbench consumer contracts qa dataset
documents = load_dataset('mteb/legalbench_consumer_contracts_qa', 'corpus', cache_dir = './', split='corpus')
queries = load_dataset('mteb/legalbench_consumer_contracts_qa', 'queries', cache_dir = './', split='queries')

```

Each document in `mteb/legalbench_consumer_contracts_qa` contains a `text` field by which we will embed using the Voyage AI client.

```Python Python theme={null}
num_documents = len(documents['text'])
voyageai_batch_size = 128  # Please check the restrictions of number of examples and number of tokens per request here https://docs.voyageai.com/docs/embeddings
embeds = []
while len(embeds) < num_documents:
    embeds.extend(vc.embed(
        texts=documents['text'][len(embeds):len(embeds)+voyageai_batch_size],
        model='voyage-law-2',  # Please check the available models here https://docs.voyageai.com/docs/embeddings
        input_type='document',
        truncation=True
    ).embeddings)
```

Check the dimensionality of the returned vectors. You will need to save the embedding dimensionality from this to be used when initializing your Pinecone index later.

```Python Python theme={null}
import numpy as np

shape = np.array(embeds).shape
print(shape)
```

```
[Out]:
(154, 1024)
```

In this example, you can see that for each of the `154` documents, we created a `1024`-dimensional embedding with the Voyage AI `voyage-law-2` model.

### 3. Store the Embeddings

Now that you have your embeddings, you can move on to indexing them in the Pinecone vector database. For this, you need a Pinecone API key. [Sign up for one here](https://app.pinecone.io).

You first initialize our connection to Pinecone and then create a new index called `voyageai-pinecone-legalbench` for storing the embeddings. When creating the index, you specify that you would like to use the cosine similarity metric to align with Voyage AI's embeddings, and also pass the embedding dimensionality of `1024`.

```Python Python theme={null}
from pinecone.grpc import PineconeGRPC as Pinecone
from pinecone import ServerlessSpec


# initialize connection to pinecone (get API key at app.pinecone.io)
pc = Pinecone(api_key="<YOUR_PINECONE_API_KEY>")

index_name = 'voyageai-pinecone-legalbench'


# if the index does not exist, we create it
if not pc.has_index(index_name):
    pc.create_index(
        index_name,
        dimension=shape[1],
        spec=ServerlessSpec(
            cloud='aws',
            region='us-east-1'
        ),
        metric='cosine'
    )


# connect to index
index = pc.Index(index_name)
```

Now you can begin populating the index with your embeddings. Pinecone expects you to provide a list of tuples in the format (`id`, `vector`, `metadata`), where the `metadata` field is an optional extra field where you can store anything you want in a dictionary format. For this example, you will store the original text of the embeddings.

While uploading your data, you will batch everything to avoid pushing too much data in one go.

```Python Python theme={null}
batch_size = 128

ids = [str(i) for i in range(shape[0])]

# create list of metadata dictionaries
meta = [{'text': text} for text in documents['text']]


# create list of (id, vector, metadata) tuples to be upserted
to_upsert = list(zip(ids, embeds, meta))

for i in range(0, shape[0], batch_size):
    i_end = min(i+batch_size, shape[0])
    index.upsert(vectors=to_upsert[i:i_end])


# let's view the index statistics
print(index.describe_index_stats())
`

`[Out]:
{'dimension': 1024,
 'index_fullness': 0.0,
 'namespaces': {'': {'vector_count': 154}},
 'total_vector_count': 154}
```

You can see from `index.describe_index_stats` that you have a *1024-dimensionality* index populated with *154* embeddings. The `indexFullness` metric tells you how full your index is. At the moment, it is empty. Using the default value of one *p1* pod, you can fit around 750K embeddings before the `indexFullness` reaches capacity. The [Usage Estimator](https://www.pinecone.io/pricing/) can be used to identify the number of pods required for a given number of *n*-dimensional embeddings.

### 4. Semantic search

Now that you have your indexed vectors, you can perform a few search queries. When searching, you will first embed your query using `voyage-law-2`, and then search using the returned vector in Pinecone.

```Python Python theme={null}

# get a sample query from the dataset, "Will Google help me if I think someone has taken and used content Ive created without my permission?" 
query = queries['text'][0]
print(f"Query: {query}")


# create the query embedding
xq = vc.embed(
    texts=[query],
    model='voyage-law-2',
    input_type="query",
    truncation=True
).embeddings


# query, returning the top 3 most similar results
res = index.query(vector=xq, top_k=3, include_metadata=True)
```

The response from Pinecone includes your original text in the `metadata` field. Let's print out the `top_k` most similar questions and their respective similarity scores.

```Python Python theme={null}
for match in res['matches']:
    print(f"{match['score']:.2f}: {match['metadata']['text']}")
```

```[Out]:  theme={null}
0.59: Your content
Some of our services give you the opportunity to make your content publicly available  for example, you might post a product or restaurant review that you wrote, or you might upload a blog post that you created.
See the Permission to use your content section for more about your rights in your content, and how your content is used in our services
See the Removing your content section to learn why and how we might remove user-generated content from our services
If you think that someone is infringing your intellectual property rights, you can send us notice of the infringement and well take appropriate action. For example, we suspend or close the Google Accounts of repeat copyright infringers as described in our Copyright Help Centre.


0.47: Google content
Some of our services include content that belongs to Google  for example, many of the visual illustrations that you see in Google Maps. You may use Googles content as allowed by these terms and any service-specific additional terms, but we retain any intellectual property rights that we have in our content. Dont remove, obscure or alter any of our branding, logos or legal notices. If you want to use our branding or logos, please see the Google Brand Permissions page.

Other content
Finally, some of our services gives you access to content that belongs to other people or organisations  for example, a store owners description of their own business, or a newspaper article displayed in Google News. You may not use this content without that person or organisations permission, or as otherwise allowed by law. The views expressed in the content of other people or organisations are their own, and dont necessarily reflect Googles views.


0.45: Taking action in case of problems
Before taking action as described below, well provide you with advance notice when reasonably possible, describe the reason for our action and give you an opportunity to fix the problem, unless we reasonably believe that doing so would:
cause harm or liability to a user, third party or Google
violate the law or a legal enforcement authoritys order
compromise an investigation
compromise the operation, integrity or security of our services

Removing your content
If we reasonably believe that any of your content (1) breaches these terms, service-specific additional terms or policies, (2) violates applicable law, or (3) could harm our users, third parties or Google, then we reserve the right to take down some or all of that content in accordance with applicable law. Examples include child pornography, content that facilitates human trafficking or harassment, and content that infringes someone elses intellectual property rights.

Suspending or terminating your access to Google services
Google reserves the right to suspend or terminate your access to the services or delete your Google Account if any of these things happen:
you materially or repeatedly breach these terms, service-specific additional terms or policies
were required to do so to comply with a legal requirement or a court order
we reasonably believe that your conduct causes harm or liability to a user, third party or Google  for example, by hacking, phishing, harassing, spamming, misleading others or scraping content that doesnt belong to you
If you believe that your Google Account has been suspended or terminated in error, you can appeal.
Of course, youre always free to stop using our services at any time. If you do stop using a service, wed appreciate knowing why so that we can continue improving our services.

```

The semantic search pipeline with Voyage AI and Pinecone is able to identify the relevant consumer contract documents to answer the user query.



# Zapier
Source: https://docs.pinecone.io/integrations/zapier



export const PrimarySecondaryCTA = ({primaryLabel, primaryHref, primaryTarget, secondaryLabel, secondaryHref, secondaryTarget}) => <div style={{
  display: 'flex',
  alignItems: 'center',
  gap: 16
}}>
   {primaryLabel && primaryHref && <div style={{
  width: 'fit-content',
  height: 42,
  background: 'var(--brand-blue)',
  borderRadius: 4,
  overflow: 'hidden',
  flexDirection: 'column',
  justifyContent: 'center',
  alignItems: 'center',
  display: 'inline-flex'
}}>
      <a href={primaryHref} target={primaryTarget} style={{
  paddingLeft: 22,
  paddingRight: 22,
  paddingTop: 8,
  paddingBottom: 8,
  justifyContent: 'center',
  alignItems: 'center',
  gap: 4,
  display: 'inline-flex',
  textDecoration: 'none',
  borderBottom: 'none'
}}>
        <div style={{
  textAlign: 'justify',
  color: 'var(--text-contrast)',
  fontSize: 15,
  fontWeight: '600',
  letterSpacing: 0.46,
  wordWrap: 'break-word'
}}>
          {primaryLabel}
        </div>
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" style={{
  marginLeft: 2
}}>
          <path d="M9.70492 6L8.29492 7.41L12.8749 12L8.29492 16.59L9.70492 18L15.7049 12L9.70492 6Z" fill="white" style={{
  fille: "var(--text-contrast)"
}} />
        </svg>
      </a>
    </div>}

    {secondaryLabel && secondaryHref && <div style={{
  width: 'fit-content',
  height: 42,
  borderRadius: 4,
  overflow: 'hidden',
  flexDirection: 'column',
  justifyContent: 'center',
  alignItems: 'center',
  display: 'inline-flex',
  textDecoration: 'none'
}}>
        <a href={secondaryHref} target={secondaryTarget} style={{
  paddingLeft: 11,
  paddingRight: 11,
  paddingTop: 8,
  paddingBottom: 8,
  justifyContent: 'center',
  alignItems: 'center',
  gap: 8,
  display: 'inline-flex',
  textDecoration: 'none',
  borderBottom: 'none'
}}>
          <div style={{
  textAlign: 'justify',
  color: 'var(--brand-blue)',
  fontSize: 15,
  fontWeight: '600',
  letterSpacing: 0.46,
  wordWrap: 'break-word'
}}>
            {secondaryLabel}
          </div>
        </a>
      </div>}

  </div>;

[Zapier](https://zapier.com/) lets you connect Pinecone with thousands of the most popular apps, so you can automate your work and have more time for what matters most — no code required.

With this integration, Pinecone can trigger workflows when your index status changes, and other apps can command Pinecone to perform actions. This means you can automatically add or remove data, run searches, or manage indexes based on events happening in your other tools.

For example, you might use this integration to automatically add spreadsheet entries to your Pinecone index, or build a bot that searches for answers and posts them directly to your team chat. It's all about weaving Pinecone's powerful search and data capabilities into your existing workflows, making everything work together automatically.

<PrimarySecondaryCTA primaryHref={"https://zapier.com/apps/pinecone/integrations"} primaryLabel={"Get started"} secondaryHref={"https://help.zapier.com/hc/articles/38950923151117"} secondaryLabel={"View setup guide"} />



# Model Gallery
Source: https://docs.pinecone.io/models/overview

Pinecone integrations enable you to build and deploy AI applications faster and more efficiently. Integrate Pinecone with your favorite frameworks, data sources, and infrastructure providers.

export const ModelCard = ({logoSrc, company, modelName, description, task, modality, maxInputTokens, price, buttonLabel, buttonHref, buttonTarget, inferenceAPI, isPreviewCard, logoInvert}) => {
  const handleButtonClick = () => {
    if (inferenceAPI) {
      if (buttonTarget === "_blank") {
        window.open(buttonHref, buttonTarget);
      } else {
        window.location.href = buttonHref;
      }
    } else {}
  };
  return <div className="model-card" style={{
    width: "100%",
    height: 400,
    minWidth: 280,
    maxWidth: 640,
    minHeight: 430,
    padding: "20px",
    background: "var(--paper)",
    borderRadius: 4,
    overflow: "hidden",
    border: "1px solid var(--border)",
    flexDirection: "column",
    justifyContent: "flex-start",
    alignItems: "flex-start",
    display: "inline-flex",
    transition: "box-shadow 0.3s ease-in-out"
  }}>
  <div style={{
    display: "flex",
    alignItems: "center",
    marginBottom: 16,
    paddingBlock: 7.6
  }}>
    <img noZoom src={logoSrc} alt={`${company} Logo`} style={{
    width: 45,
    height: 45,
    marginRight: 10,
    marginTop: 0,
    marginBottom: 0
  }} className={logoInvert ? "dark-inverted" : ""} />
    <div>
      <h2 style={{
    margin: 0,
    fontSize: 16,
    fontWeight: "bold"
  }}>
        {modelName}
      </h2>
      <p style={{
    margin: 0,
    fontSize: 12,
    color: "var(--text-secondary)"
  }}>
        {company.toUpperCase()}
      </p>
    </div>
  </div>
  <p style={{
    fontSize: 14,
    margin: 0,
    marginBottom: 20,
    height: 36
  }}>
    {description}
  </p>
  <div style={{
    marginBottom: 0,
    width: "100%",
    maxHeight: 220,
    flexGrow: 1
  }}>
    <table className="model-card-table" style={{
    width: "100%",
    borderCollapse: "collapse",
    height: "auto",
    tableLayout: "fixed",
    marginTop: 0,
    paddingBottom: 0,
    marginBottom: 0
  }}>
      <colgroup style={{
    width: 400
  }}>
        <col style={{
    width: "35%"
  }} />
        <col style={{
    width: "65%"
  }} />
      </colgroup>
      <tbody style={{
    width: "100%"
  }}>
        <tr style={{
    borderBottom: "1px solid var(--border)"
  }}>
          <td>
            <strong style={{
    color: task === "NA" ? "var(--secondary)" : "var(--text-primary)"
  }}>
              Task
            </strong>
          </td>
          <td style={{
    color: task === "NA" ? "var(--secondary)" : "var(--text-primary)"
  }}>
            {task}
          </td>
        </tr>
        <tr style={{
    borderBottom: "1px solid var(--border)"
  }}>
          <td>
            <strong style={{
    color: modality === "NA" ? "var(--secondary)" : "var(--text-primary)"
  }}>
              Modality
            </strong>
          </td>
          <td style={{
    color: modality === "NA" ? "var(--secondary)" : "var(--text-primary)"
  }}>
            {modality}
          </td>
        </tr>
        <tr style={{
    borderBottom: "1px solid var(--border)"
  }}>
          <td>
            <strong style={{
    color: maxInputTokens === "NA" ? "var(--secondary)" : "var(--text-primary)"
  }}>
              Max Input Tokens
            </strong>
          </td>
          <td style={{
    color: maxInputTokens === "NA" ? "var(--secondary)" : "var(--text-primary)"
  }}>
            {maxInputTokens}
          </td>
        </tr>
        <tr style={{
    borderBottom: "0px solid var(--border)"
  }}>
          <td>
            <strong style={{
    color: price === "NA" ? "var(--secondary)" : "var(--text-primary)"
  }}>
              Price
            </strong>
          </td>
          <td style={{
    color: price === "NA" ? "var(--secondary)" : "var(--text-primary)"
  }}>
            {price}
          </td>
        </tr>
      </tbody>
    </table>
  </div>
  <button id={`${modelName}-button`} style={{
    alignSelf: "stretch",
    height: 36,
    background: inferenceAPI ? "var(--brand-blue)" : "var(--secondary)",
    borderRadius: 4,
    overflow: "hidden",
    flexDirection: "column",
    justifyContent: "center",
    alignItems: "center",
    display: "flex",
    cursor: inferenceAPI ? "pointer" : "not-allowed",
    border: "none",
    transition: "background 0.2s ease"
  }} onMouseOver={e => inferenceAPI && (e.currentTarget.style.background = "var(--primary-dark)")} onMouseOut={e => inferenceAPI && (e.currentTarget.style.background = "var(--brand-blue)")} onClick={handleButtonClick}>
    <div style={{
    paddingLeft: 16,
    paddingRight: 16,
    paddingTop: 6,
    paddingBottom: 6,
    justifyContent: "center",
    alignItems: "center",
    gap: 8,
    display: "inline-flex"
  }}>
      <div style={{
    height: 20,
    flexDirection: "column",
    justifyContent: "center",
    alignItems: "center",
    display: "inline-flex"
  }}>
        {inferenceAPI && <svg width="16.63" height="16.63" viewBox="0 0 21 20" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M10.5003 1.68292C5.90859 1.68292 2.18359 5.40792 2.18359 9.99959C2.18359 14.5913 5.90859 18.3163 10.5003 18.3163C15.0919 18.3163 18.8169 14.5913 18.8169 9.99959C18.8169 5.40792 15.0919 1.68292 10.5003 1.68292ZM10.5003 16.6496C6.83359 16.6496 3.85026 13.6663 3.85026 9.99959C3.85026 6.33292 6.83359 3.34959 10.5003 3.34959C14.1669 3.34959 17.1503 6.33292 17.1503 9.99959C17.1503 13.6663 14.1669 16.6496 10.5003 16.6496ZM11.1253 4.16626L7.37526 11.2496H9.99193V15.8329L13.6253 8.74959H11.1253V4.16626Z" fill="white" />
          </svg>}
      </div>
      <div id={`${modelName}-button-label`} style={{
    color: inferenceAPI ? "white" : "#2D3D4D42",
    fontSize: 14,
    fontWeight: "500",
    letterSpacing: 0.4,
    wordWrap: "break-word"
  }}>
        {inferenceAPI ? buttonLabel : "Coming soon"}
      </div>
    </div>
  </button>
  {isPreviewCard && <div>Preview</div>}
</div>;
};

<div className="not-prose">
  <span
    style={{
        fontSize: "34px",
        fontWeight: "600",
        margin: "0px",
        display: "inline-flex",
        alignItems: "center",
        gap: "10px",
    }}
  >
    <span>
      <svg width="34" height="33" viewBox="0 0 21 20" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M10.5003 1.68292C5.90859 1.68292 2.18359 5.40792 2.18359 9.99959C2.18359 14.5913 5.90859 18.3163 10.5003 18.3163C15.0919 18.3163 18.8169 14.5913 18.8169 9.99959C18.8169 5.40792 15.0919 1.68292 10.5003 1.68292ZM10.5003 16.6496C6.83359 16.6496 3.85026 13.6663 3.85026 9.99959C3.85026 6.33292 6.83359 3.34959 10.5003 3.34959C14.1669 3.34959 17.1503 6.33292 17.1503 9.99959C17.1503 13.6663 14.1669 16.6496 10.5003 16.6496ZM11.1253 4.16626L7.37526 11.2496H9.99193V15.8329L13.6253 8.74959H11.1253V4.16626Z" style={{fill: "var(--text-primary)"}} fill="white" />
      </svg>
    </span>

    <span className="inline-flex items-baseline gap-2 !m-0">
      <span style={{margin: 0, color: "var(--text-primary)"}}>Inference</span>
    </span>
  </span>

  <div
    className="flex flex-col md:flex-row justify-between items-start md:items-center gap-5"
    style={{
          display: "flex",
          justifyContent: "space-between",
          marginBottom: "32px",
      }}
  >
    <p>
      Build end-to-end faster with models hosted by Pinecone.
    </p>

    <a href="https://www.pinecone.io/request-a-model/" target="_blank" className="outlined-button">
      Request a model
    </a>
  </div>
</div>

<div className="featured-card-container relative">
  <div
    className="featured-model-cards  overflow-x-auto"
    id="modelCarousel"
    style={{ 
          WebkitOverflowScrolling: 'touch',  // Enable smooth scrolling on iOS
          scrollSnapType: 'x mandatory'       // Enable snap points
      }}
    onScroll={(e) => {
          const carousel = e.target;
          const prevButton = document.getElementById('prevButton');
          const nextButton = document.getElementById('nextButton');
          
          if (!prevButton || !nextButton) return; // Guard against null elements
          
          // Check if we're at the start or end
          const isAtStart = carousel.scrollLeft === 0;
          const isAtEnd = Math.abs(carousel.scrollLeft + carousel.offsetWidth - carousel.scrollWidth) < 1;
          
          // Update button visibility
          prevButton.style.visibility = isAtStart ? 'hidden' : 'visible';
          nextButton.style.visibility = isAtEnd ? 'hidden' : 'visible';
      }}
  >
    <ModelCard logoSrc="https://cdn.sanity.io/images/vr8gru94/production/cc3f1c395c8bcb50e042549b0faa595f5eab7d62-249x165.svg" company="NVIDIA" modelName="llama-text-embed-v2" description="State of the art text embedding model" task="Embedding" modality="Text" maxInputTokens="2048" price="$0.16 / million tokens" buttonLabel="Try this model" buttonHref="/models/llama-text-embed-v2" inferenceAPI={true} />

    <ModelCard logoSrc="https://cdn.sanity.io/images/vr8gru94/production/5b170117926ae5a5e451aa24676b5a124c2fa122-23x23.svg?w=2000&fit=max&auto=format&dpr=2" company="Microsoft" modelName="multilingual-e5-large" description="Top performing text embedding model from Microsoft research." task="Embedding" modality="Text" maxInputTokens="507" price="$0.08 / million tokens" buttonLabel="Try this model" buttonHref="/models/multilingual-e5-large" inferenceAPI={true} />

    <ModelCard logoSrc={"https://cdn.sanity.io/images/vr8gru94/production/33b1cb253308f74fc83248746b7370a89b3c2c05-250x250.svg"} company="Cohere" modelName="cohere-rerank-3.5" description="Cohere's latest reranker with multilingual capabilities." task="Rerank" modality="Text" maxInputTokens="4096" price="$2.00 / 1k requests" buttonLabel="Try this model" buttonHref="/models/cohere-rerank-3.5" inferenceAPI={true} />

    <ModelCard logoSrc={"https://cdn.sanity.io/images/vr8gru94/production/f995ec77f7d3ccf3ed269fb6076ea3efdf22a8a6-724x785.png"} company="Pinecone" modelName="pinecone-sparse-english-v0" description="Sparse vector model for keyword-style search." task="Embedding" modality="Text" maxInputTokens="512" price="$0.08 / million tokens" buttonLabel="Try this model" buttonHref="/models/pinecone-sparse-english-v0" inferenceAPI={true} logoInvert={true} />

    <ModelCard logoSrc={"https://cdn.sanity.io/images/vr8gru94/production/40b1d05ee1325e6d9e4886af4e76ff06d844faff-188x188.jpg"} company="BAAI" modelName="bge-reranker-v2-m3" description="High performance multi-lingual reranker model." task="Rerank" modality="Text" maxInputTokens="1024" price="$2.00 / 1k requests" buttonLabel="Try this model" buttonHref="/models/bge-reranker-v2-m3" inferenceAPI={true} />
  </div>

  <button
    className="carousel-button prev"
    id="prevButton"
    aria-label="Previous slide"
    style={{ visibility: 'hidden' }}
    onClick={() => {
          const carousel = document.getElementById('modelCarousel');
          const scrollAmount = carousel.offsetWidth / 4;
          carousel.scrollBy({
              left: -scrollAmount,
              behavior: 'smooth'
          });
      }}
  >
    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path d="M15 19l-7-7 7-7" stroke="var(--text-primary)" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" />
    </svg>
  </button>

  <button
    className="carousel-button next"
    id="nextButton"
    aria-label="Next slide"
    onClick={() => {
          const carousel = document.getElementById('modelCarousel');
          const scrollAmount = carousel.offsetWidth / 4;
          carousel.scrollBy({
              left: scrollAmount,
              behavior: 'smooth'
          });
      }}
  >
    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path d="M9 5l7 7-7 7" stroke="var(--text-primary)" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" />
    </svg>
  </button>
</div>

<script>
  {`
      const updateButtonVisibility = () => {
          const carousel = document.getElementById('modelCarousel');
          const prevButton = document.getElementById('prevButton');
          const nextButton = document.getElementById('nextButton');
          
          if (!carousel || !prevButton || !nextButton) return;
          
          const isAtStart = carousel.scrollLeft === 0;
          const isAtEnd = carousel.scrollLeft + carousel.offsetWidth >= carousel.scrollWidth;
          
          prevButton.style.opacity = isAtStart ? '0.5' : '1';
          nextButton.style.opacity = isAtEnd ? '0.5' : '1';
      };

      // Initialize button states
      updateButtonVisibility();
      
      // Update button states on scroll and resize
      const carousel = document.getElementById('modelCarousel');
      if (carousel) {
          carousel.addEventListener('scroll', updateButtonVisibility);
          window.addEventListener('resize', updateButtonVisibility);
      }
    `}
</script>

{" "}

<div className="model-search-container">
  <iframe id="model-search-iframe" src="https://www.pinecone.io/tools/model-search/" width="100%" height="100%" target="_parent" loading="eager" />
</div>



# Create an API key
Source: https://docs.pinecone.io/reference/api/2025-04/admin/create_api_key

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-04/admin_2025-04.oas.yaml post /admin/projects/{project_id}/api-keys
Create a new API key for a project. Developers can use the API key to authenticate requests to Pinecone's Data Plane and Control Plane APIs.


<RequestExample>
  ```bash curl theme={null}
  PINECONE_PROJECT_ID="32c8235a-5220-4a80-a9f1-69c24109e6f2"
  PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"

  curl -X POST "https://api.pinecone.io/admin/projects/$PINECONE_PROJECT_ID/api-keys" \
       -H "X-Pinecone-Api-Version: 2025-04" \
       -H "Authorization: Bearer $PINECONE_ACCESS_TOKEN" \
       -d '{ 
             "name": "example-api-key", 
             "roles": ["ProjectEditor"] 
           }'
  ```

  ```bash CLI theme={null}
  # Target the project for which you want to create an API key.
  pc target -o "example-org" -p "example-project"
  # Create the API key
  pc api-key create -n "example-api-key" --roles ProjectEditor
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {
    "key": {
      "id": "62b0dbfe-3489-4b79-b850-34d911527c88",
      "name": "example-api-key",
      "project_id": "32c8235a-5220-4a80-a9f1-69c24109e6f2",
      "roles": [
        "ProjectEditor"
      ],
      "created_at": "2025-10-20T23:40:27.069075Z"
    },
    "value": "..."
  }
  ```

  ```text CLI theme={null}
  ATTRIBUTE     VALUE
  Name          example-api-key
  ID            62b0dbfe-3489-4b79-b850-34d911527c88
  Value         ...
  Project ID    32c8235a-5220-4a80-a9f1-69c24109e6f2
  Roles         ProjectEditor
  ```
</ResponseExample>



# Create a new project
Source: https://docs.pinecone.io/reference/api/2025-04/admin/create_project

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-04/admin_2025-04.oas.yaml post /admin/projects
Creates a new project.

<RequestExample>
  ```bash curl theme={null}
  PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"

  curl -X POST "https://api.pinecone.io/admin/projects" \
       -H "X-Pinecone-Api-Version: 2025-04" \
       -H "Authorization: Bearer $PINECONE_ACCESS_TOKEN" \
       -d '{ "name":"example-project" }'
  ```

  ```bash CLI theme={null}
  # Target the organization for which you want to create 
  # a project.
  pc target -o "example-org"
  # Create the project.
  pc project create -n "example-project"
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {
    "id": "32c8235a-5220-4a80-a9f1-69c24109e6f2",
    "name": "example-project",
    "max_pods": 20,
    "force_encryption_with_cmek": false,
    "organization_id": "-NM7af6f234168c4e44a",
    "created_at": "2025-10-20T20:16:09.144497Z"
  }
  ```

  ```text CLI theme={null}
  ATTRIBUTE           VALUE
  Name                example-project
  ID                  32c8235a-5220-4a80-a9f1-69c24109e6f2
  Organization ID     -NM7af6f234168c4e44a
  Created At          2025-10-20 20:19:51.448431 +0000 UTC
  Force Encryption    false
  Max Pods            5
  ```
</ResponseExample>



# Delete an API key
Source: https://docs.pinecone.io/reference/api/2025-04/admin/delete_api_key

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-04/admin_2025-04.oas.yaml delete /admin/api-keys/{api_key_id}
Delete an API key from a project.

<RequestExample>
  ```bash curl theme={null}
  PINECONE_API_KEY_ID="62b0dbfe-3489-4b79-b850-34d911527c88"
  PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"

  curl -X DELETE "https://api.pinecone.io/admin/api-keys/$PINECONE_API_KEY_ID" \
       -H "X-Pinecone-Api-Version: 2025-04" \
       -H "Authorization: Bearer $PINECONE_ACCESS_TOKEN"
  ```

  ```bash CLI theme={null}
  PINECONE_API_KEY_ID="62b0dbfe-3489-4b79-b850-34d911527c88"

  # Delete the API key. Use --skip-confirmation to skip 
  # the confirmation prompt.
  pc api-key delete -i $PINECONE_API_KEY_ID
  ```
</RequestExample>

<ResponseExample>
  ```text curl theme={null}
  No response payload
  ```

  ```text CLI theme={null}
  [WARN] This operation will delete API key example-api-key from project example-project.
  [WARN] Any integrations that authenticate with this API key will immediately stop working.
  [WARN] This action cannot be undone.
  Do you want to continue? (y/N): y
  [INFO] You chose to continue delete.
  [SUCCESS] API key example-api-key deleted
  ```
</ResponseExample>



# Delete a project
Source: https://docs.pinecone.io/reference/api/2025-04/admin/delete_project

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-04/admin_2025-04.oas.yaml delete /admin/projects/{project_id}
Delete a project and all its associated configuration.
Before deleting a project, you must delete all indexes, assistants, backups, and collections associated with the project. Other project resources, such as API keys, are automatically deleted when the project is deleted.


<RequestExample>
  ```bash curl theme={null}
  PINECONE_PROJECT_ID="32c8235a-5220-4a80-a9f1-69c24109e6f2"
  PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"

  curl -X DELETE "https://api.pinecone.io/admin/projects/$PINECONE_PROJECT_ID" \
       -H "X-Pinecone-Api-Version: 2025-04" \
       -H "Authorization: Bearer $PINECONE_ACCESS_TOKEN"
  ```

  ```bash CLI theme={null}
  PINECONE_PROJECT_ID="32c8235a-5220-4a80-a9f1-69c24109e6f2"

  # Target the organization that contains the project.
  pc target -o "example-org" 
  # Delete the project. Use --skip-confirmation to skip 
  # the confirmation prompt.
  pc project delete -i $PINECONE_PROJECT_ID
  ```
</RequestExample>

<ResponseExample>
  ```text curl theme={null}
  No response payload
  ```

  ```text CLI theme={null}
  [WARN] This will delete the project example-project in organization Pinecone Mesh.
  [WARN] This action cannot be undone.
  Do you want to continue? (y/N): y
  [INFO] You chose to continue delete.
  [SUCCESS] Project example-project deleted.
  ```
</ResponseExample>



# Get API key details
Source: https://docs.pinecone.io/reference/api/2025-04/admin/fetch_api_key

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-04/admin_2025-04.oas.yaml get /admin/api-keys/{api_key_id}
Get the details of an API key, excluding the API key secret.

<RequestExample>
  ```bash curl theme={null}
  PINECONE_API_KEY_ID="62b0dbfe-3489-4b79-b850-34d911527c88"
  PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"

  curl -X GET "https://api.pinecone.io/admin/api-keys/$PINECONE_API_KEY_ID" \
       -H "Authorization: Bearer $PINECONE_ACCESS_TOKEN" \
       -H "accept: application/json" \
       -H "X-Pinecone-Api-Version: 2025-04"
  ```

  ```bash CLI theme={null}
  PINECONE_API_KEY_ID="62b0dbfe-3489-4b79-b850-34d911527c88"

  pc api-key describe -i $PINECONE_API_KEY_ID
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {
    "id": "62b0dbfe-3489-4b79-b850-34d911527c88",
    "name": "example-api-key",
    "project_id": "32c8235a-5220-4a80-a9f1-69c24109e6f2",
    "roles": [
      "ProjectEditor"
    ],
    "created_at": "2025-10-22T19:27:21.202955Z"
  }
  ```

  ```text CLI theme={null}
  ATTRIBUTE     VALUE
  Name          example-api-key
  ID            62b0dbfe-3489-4b79-b850-34d911527c88
  Project ID    32c8235a-5220-4a80-a9f1-69c24109e6f2
  Roles         ProjectEditor
  ```
</ResponseExample>



# Get project details
Source: https://docs.pinecone.io/reference/api/2025-04/admin/fetch_project

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-04/admin_2025-04.oas.yaml get /admin/projects/{project_id}
Get details about a project.

<RequestExample>
  ```bash curl theme={null}
  PINECONE_PROJECT_ID="32c8235a-5220-4a80-a9f1-69c24109e6f2"
  PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"

  curl -X GET "https://api.pinecone.io/admin/projects/$PINECONE_PROJECT_ID" \
       -H "Authorization: Bearer $PINECONE_ACCESS_TOKEN" \
       -H "X-Pinecone-Api-Version: 2025-04" \
       -H "accept: application/json" 
  ```

  ```bash CLI theme={null}
  PINECONE_PROJECT_ID="32c8235a-5220-4a80-a9f1-69c24109e6f2"

  # Target the organization that contains the project.
  pc target -o "example-org" 
  # Fetch the project details.
  pc project describe -i $PINECONE_PROJECT_ID
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {
    "id": "32c8235a-5220-4a80-a9f1-69c24109e6f2",
    "name": "example-project",
    "max_pods": 5,
    "force_encryption_with_cmek": false,
    "organization_id": "-NM7af6f234168c4e44a",
    "created_at": "2025-10-16T23:32:18.014693Z"
  }
  ```

  ```text CLI theme={null}
  ATTRIBUTE           VALUE
  Name                example-project
  ID                  32c8235a-5220-4a80-a9f1-69c24109e6f2
  Organization ID     -NM7af6f234168c4e44a
  Created At          2025-10-16 23:32:18.014693 +0000 UTC
  Force Encryption    false
  Max Pods            5
  ```
</ResponseExample>



# Get an access token
Source: https://docs.pinecone.io/reference/api/2025-04/admin/get_token

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-04/oauth_2025-04.oas.yaml post /oauth/token
Obtain an access token for a service account using the OAuth2 client credentials flow. An access token is needed to authorize requests to the Pinecone Admin API.
The host domain for OAuth endpoints is `login.pinecone.io`.


<RequestExample>
  ```bash curl theme={null}
  PINECONE_CLIENT_ID="YOUR_CLIENT_ID"
  PINECONE_CLIENT_SECRET="YOUR_CLIENT_SECRET"

  # NOTES:
  # - Base URL is login.pinecone.io. 
  # - When including environment variables (as shown here), 
  #   surround the request body in double quotes (not single
  #   quotes). Then, in the JSON, escape double quotes with
  #   a backslash.
  curl -X POST "https://login.pinecone.io/oauth/token" \
       -H "X-Pinecone-Api-Version: 2025-04" \
       -H "Content-Type: application/json" \
       -d "{
             \"grant_type\": \"client_credentials\",
             \"client_id\": \"$PINECONE_CLIENT_ID\",
             \"client_secret\": \"$PINECONE_CLIENT_SECRET\",
             \"audience\": \"https://api.pinecone.io/\"
           }"
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {
    "access_token": "...",
    "expires_in": 1800,
    "token_type": "Bearer"
  }
  ```
</ResponseExample>



# List API keys
Source: https://docs.pinecone.io/reference/api/2025-04/admin/list_api_keys

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-04/admin_2025-04.oas.yaml get /admin/projects/{project_id}/api-keys
List all API keys in a project.

<RequestExample>
  ```bash curl theme={null}
  PINECONE_PROJECT_ID="32c8235a-5220-4a80-a9f1-69c24109e6f2"
  PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"

  curl -X GET "https://api.pinecone.io/admin/projects/$PINECONE_PROJECT_ID/api-keys" \
       -H "Authorization: Bearer $PINECONE_ACCESS_TOKEN" \
       -H "X-Pinecone-Api-Version: 2025-04"
  ```

  ```bash CLI theme={null}
  PINECONE_PROJECT_ID="32c8235a-5220-4a80-a9f1-69c24109e6f2"

  pc api-key list -i $PINECONE_PROJECT_ID
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {
    "data": [
      {
        "id": "62b0dbfe-3489-4b79-b850-34d911527c88",
        "name": "example-api-key",
        "project_id": "32c8235a-5220-4a80-a9f1-69c24109e6f2",
        "roles": [
          "ProjectEditor"
        ],
        "created_at": "2025-10-20T23:39:43.665754Z"
      },
      {
        "id": "0d0d3678-81b4-4e0d-a4f0-70ba488acfb7",
        "name": "example-api-key-2",
        "project_id": "32c8235a-5220-4a80-a9f1-69c24109e6f2",
        "roles": [
          "ProjectEditor"
        ],
        "created_at": "2025-10-20T23:43:13.176422Z"
      }
    ]
  }
  ```

  ```text CLI theme={null}
  Organization: example-organization (ID: -NM7af6f234168c4e44a)
  Project: example-project (ID: 32c8235a-5220-4a80-a9f1-69c24109e6f2)

  API Keys

  NAME                 ID                                      PROJECT ID                              ROLES
  example-api-key      62b0dbfe-3489-4b79-b850-34d911527c88    32c8235a-5220-4a80-a9f1-69c24109e6f2    ProjectEditor
  example-api-key-2    0d0d3678-81b4-4e0d-a4f0-70ba488acfb7    32c8235a-5220-4a80-a9f1-69c24109e6f2    ProjectEditor
  ```
</ResponseExample>



# List projects
Source: https://docs.pinecone.io/reference/api/2025-04/admin/list_projects

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-04/admin_2025-04.oas.yaml get /admin/projects
List all projects in an organization.

<RequestExample>
  ```bash curl theme={null}
  PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"

  curl -X GET "https://api.pinecone.io/admin/projects" \
       -H "Authorization: Bearer $PINECONE_ACCESS_TOKEN" \
       -H "X-Pinecone-Api-Version: 2025-04"
  ```

  ```bash CLI theme={null}
  # Target the organization for which you want to list 
  # projects.
  pc target -o "example-org"
  # List projects in the target organization  
  pc project list
  ```
</RequestExample>

<ResponseExample>
  ```json  theme={null}
  {
    "data": [
      {
        "id": "32c8235a-5220-4a80-a9f1-69c24109e6f2",
        "name": "example-project",
        "max_pods": 20,
        "force_encryption_with_cmek": false,
        "organization_id": "-NM7af6f234168c4e44a",
        "created_at": "2025-10-20T20:16:09.144497Z"
      }
      {
        "id": "f060b981-6e6e-48a8-9f82-63b9610cc139",
        "name": "example-project-2",
        "max_pods": 20,
        "force_encryption_with_cmek": false,
        "organization_id": "-NM7af6f234168c4e44a",
        "created_at": "2025-07-01T13:45:00.357928Z"
      }
    ]
  }
  ```

  ```text CLI theme={null}
  NAME               ID                                     ORGANIZATION ID        CREATED AT                             FORCE ENCRYPTION   MAX PODS
  example-project    32c8235a-5220-4a80-a9f1-69c24109e6f2   -NM7af6f234168c4e44a   2025-10-20 20:19:51.448431 +0000 UTC   false              20 
  example-project-2  f060b981-6e6e-48a8-9f82-63b9610cc139   -NM7af6f234168c4e44a   2024-10-16 14:24:35.170627 +0000 UTC   false              20
  ```
</ResponseExample>



# Update an API key
Source: https://docs.pinecone.io/reference/api/2025-04/admin/update_api_key

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-04/admin_2025-04.oas.yaml patch /admin/api-keys/{api_key_id}
Update the name and roles of an API key.


<RequestExample>
  ```bash curl theme={null}
  PINECONE_API_KEY_ID="62b0dbfe-3489-4b79-b850-34d911527c88"
  PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"

  curl -X PATCH "https://api.pinecone.io/admin/api-keys/$PINECONE_API_KEY_ID" \
       -H "X-Pinecone-Api-Version: 2025-04" \
       -H "Authorization: Bearer $PINECONE_ACCESS_TOKEN" \
       -d '{
             "name": "new-api-key-name",
             "roles": ["ProjectEditor"]
           }'
  ```

  ```bash CLI theme={null}
  PINECONE_API_KEY_ID="62b0dbfe-3489-4b79-b850-34d911527c88"

  # Target the organization that contains the API key.
  pc target -o "example-org" 
  # Update the API key name.
  pc api-key update -i $PINECONE_API_KEY_ID -n "new-api-key-name"
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {
    "id": "62b0dbfe-3489-4b79-b850-34d911527c88",
    "name": "new-api-key-name",
    "project_id": "32c8235a-5220-4a80-a9f1-69c24109e6f2",
    "roles": [
      "ProjectEditor"
    ],
    "created_at": "2025-10-22T19:27:21.202955Z"
  }
  ```

  ```text CLI theme={null}
  ATTRIBUTE     VALUE
  Name          new-api-key-name
  ID            62b0dbfe-3489-4b79-b850-34d911527c88
  Project ID    32c8235a-5220-4a80-a9f1-69c24109e6f2
  Roles         ProjectEditor
  ```
</ResponseExample>



# Update a project
Source: https://docs.pinecone.io/reference/api/2025-04/admin/update_project

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-04/admin_2025-04.oas.yaml patch /admin/projects/{project_id}
Update a project's configuration details.
You can update the project's name, maximum number of Pods, or enable encryption with a customer-managed encryption key (CMEK).


<RequestExample>
  ```bash curl theme={null}
  PINECONE_PROJECT_ID="32c8235a-5220-4a80-a9f1-69c24109e6f2"
  PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"

  curl -X PATCH "https://api.pinecone.io/admin/projects/$PINECONE_PROJECT_ID" \
       -H "Authorization: Bearer $PINECONE_ACCESS_TOKEN" \
       -H "accept: application/json" \
       -H "Content-Type: application/json" \
       -H "X-Pinecone-Api-Version: 2025-04" \
       -d '{ "name": "new-project-name" }'
  ```

  ```bash CLI theme={null}
  PINECONE_PROJECT_ID="32c8235a-5220-4a80-a9f1-69c24109e6f2"

  # Target the organization that contains the project.
  pc target -o "example-org" 
  # Update the project name.
  pc project update -i $PINECONE_PROJECT_ID -n "new-project-name"
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {
    "id": "32c8235a-5220-4a80-a9f1-69c24109e6f2",
    "name": "new-project-name",
    "max_pods": 5,
    "force_encryption_with_cmek": false,
    "organization_id": "-NM7af6f234168c4e44a",
    "created_at": "2025-10-20T20:19:51.448431Z"
  }
  ```

  ```text CLI theme={null}
  ATTRIBUTE           VALUE
  Name                new-project-name
  ID                  32c8235a-5220-4a80-a9f1-69c24109e6f2
  Organization ID     -NM7af6f234168c4e44a
  Created At          2025-10-20 20:19:51.448431 +0000 UTC
  Force Encryption    false
  Max Pods            5
  ```
</ResponseExample>



# Create a backup of an index
Source: https://docs.pinecone.io/reference/api/2025-04/control-plane/create_backup

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-04/db_control_2025-04.oas.yaml post /indexes/{index_name}/backups
Create a backup of an index.


<RequestExample>
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

  curl -X POST "https://api.pinecone.io/indexes/$INDEX_NAME/backups" \
       -H "Api-Key: $PINECONE_API_KEY" \
       -H 'accept: application/json' \
       -H 'Content-Type: application/json' \
       -H "X-Pinecone-API-Version: 2025-04" \
       -d '{
             "name": "example-backup", 
             "description": "Monthly backup of production index"
           }'
  ```
</RequestExample>

<ResponseExample>
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
</ResponseExample>



# Create a collection
Source: https://docs.pinecone.io/reference/api/2025-04/control-plane/create_collection

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-04/db_control_2025-04.oas.yaml post /collections
Create a Pinecone collection.
  
Serverless indexes do not support collections.


<RequestExample>
  ```python Python theme={null}
  # pip install "pinecone[grpc]"
  from pinecone.grpc import PineconeGRPC as Pinecone

  pc = Pinecone(api_key="API_KEY")
  pc.create_collection("example-collection", "docs-example")
  ```

  ```javascript JavaScript theme={null}
  // npm install @pinecone-database/pinecone
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({
    apiKey: 'YOUR_API_KEY'
  });

  await pc.createCollection({
    name: "example-collection",
    source: "docs-example",
  });
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Pinecone;

  public class CreateCollectionExample {
      public static void main(String[] args) {
          Pinecone pc = new Pinecone.Builder("YOUR_API_KEY").build();

          pc.createCollection("example-collection", "docs-example");
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

      collection, err := pc.CreateCollection(ctx, &pinecone.CreateCollectionRequest{
          Name: "example-collection", 
          Source: "docs-example",
      })
      if err != nil {
          log.Fatalf("Failed to create collection: %v", err)
      } else {
          fmt.Printf("Successfully created collection: %v", collection.Name)
      }
  }
  ```

  ```csharp C# theme={null}
  using Pinecone;

  var pinecone = new PineconeClient("YOUR_API_KEY");

  var collectionModel = await pinecone.CreateCollectionAsync(new CreateCollectionRequest {
      Name = "example-collection",
      Source = "docs-example",
  });
  ```

  ```shell curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl -X POST "https://api.pinecone.io/collections" \
       -H "Accept: application/json" \
       -H "Content-Type: application/json" \
       -H "Api-Key: $PINECONE_API_KEY" \
       -H "X-Pinecone-API-Version: 2025-04" \
       -d '{
             "name": "example-collection",
             "source": "docs-example"
           }'
  ```
</RequestExample>

<ResponseExample>
  ```json  theme={null}
  {
      "name": "example-collection",
      "status": "Initializing",
      "environment": "us-east-1-aws",
      "dimension": 1536
  }
  ```
</ResponseExample>



# Create an index from a backup
Source: https://docs.pinecone.io/reference/api/2025-04/control-plane/create_index_from_backup

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-04/db_control_2025-04.oas.yaml post /backups/{backup_id}/create-index
Create an index from a backup.

<RequestExample>
  ```python Python theme={null}
  from pinecone import Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  pc.create_index_from_backup(
      backup_id="a65ff585-d987-4da5-a622-72e19a6ed5f4",
      name="restored-index",
      tags={
          "tag0": "val0", 
          "tag1": "val1"
      },
      deletion_protection="enabled"
  )
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' })

  const response = await pc.createIndexFromBackup({
    backupId: 'a65ff585-d987-4da5-a622-72e19a6ed5f4',
    name: 'restored-index',
    tags: {
      tag0: 'val0',
      tag1: 'val1'
    },
    deletionProtection: 'enabled'
  });

  console.log(response);
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Pinecone;
  import org.openapitools.db_control.client.ApiException;
  import org.openapitools.db_control.client.model.*;

  public class CreateIndexFromBackup {
      public static void main(String[] args) throws ApiException {
          Pinecone pc = new Pinecone.Builder("YOUR_API_KEY").build();

          String backupID = "a65ff585-d987-4da5-a622-72e19a6ed5f4";
          String indexName = "restored-index";

          CreateIndexFromBackupResponse backupResponse = pc.createIndexFromBackup(backupID, indexName);
          System.out.println(backupResponse);
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
  	"time"

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

  	indexName := "restored-index"
  	restoredIndexTags := pinecone.IndexTags{"restored_on": time.Now().Format("2006-01-02 15:04")}
  	createIndexFromBackupResp, err := pc.CreateIndexFromBackup(ctx, &pinecone.CreateIndexFromBackupParams{
  		BackupId: "e12269b0-a29b-4af0-9729-c7771dec03e3",
  		Name:     indexName,
  		Tags:     &restoredIndexTags,
  	})

  	fmt.Printf(prettifyStruct(createIndexFromBackupResp))
  }
  ```

  ```csharp C# theme={null}
  using Pinecone;

  var pinecone = new PineconeClient("YOUR_API_KEY");

  var response = await pinecone.Backups.CreateIndexFromBackupAsync(
      "a65ff585-d987-4da5-a622-72e19a6ed5f4", 
      new CreateIndexFromBackupRequest
      {
          Name = "restored-index",
          Tags = new Dictionary<string, string> 
          { 
              { "tag0", "val0" },
              { "tag1", "val1" }
          },
          DeletionProtection = DeletionProtection.Enabled
      }
  );

  Console.WriteLine(response);
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  BACKUP_ID="a65ff585-d987-4da5-a622-72e19a6ed5f4"

  curl -X POST "https://api.pinecone.io/backups/$BACKUP_ID/create-index" \
       -H "Api-Key: $PINECONE_API_KEY" \
       -H "X-Pinecone-API-Version: 2025-04" \
       -H 'Content-Type: application/json' \
       -d '{
             "name": "restored-index",
             "tags": {
               "tag0": "val0",
               "tag1": "val1"
             },
             "deletion_protection": "enabled"
           }'
  ```
</RequestExample>

<ResponseExample>
  ```python Python theme={null}
  {'deletion_protection': 'enabled',
   'dimension': 1024,
   'embed': {'dimension': 1024,
             'field_map': {'text': 'chunk_text'},
             'metric': 'cosine',
             'model': 'multilingual-e5-large',
             'read_parameters': {'input_type': 'query', 'truncate': 'END'},
             'vector_type': 'dense',
             'write_parameters': {'input_type': 'passage', 'truncate': 'END'}},
   'host': 'example-dense-index-python3-govk0nt.svc.aped-4627-b74a.pinecone.io',
   'metric': 'cosine',
   'name': 'example-dense-index-python3',
   'spec': {'serverless': {'cloud': 'aws', 'region': 'us-east-1'}},
   'status': {'ready': True, 'state': 'Ready'},
   'tags': {'tag0': 'val0', 'tag1': 'val1'},
   'vector_type': 'dense'}
  ```

  ```javascript JavaScript theme={null}
  {
    restoreJobId: 'e9ba8ff8-7948-4cfa-ba43-34227f6d30d4',
    indexId: '025117b3-e683-423c-b2d1-6d30fbe5027f'
  }
  ```

  ```java Java theme={null}
  class CreateIndexFromBackupResponse {
      restoreJobId: e9ba8ff8-7948-4cfa-ba43-34227f6d30d4
      indexId: 025117b3-e683-423c-b2d1-6d30fbe5027f
      additionalProperties: null
  }
  ```

  ```go Go theme={null}
  {
    "index_id": "025117b3-e683-423c-b2d1-6d30fbe5027f",
    "restore_job_id": "e9ba8ff8-7948-4cfa-ba43-34227f6d30d4"
  }
  ```

  ```csharp C# theme={null}
  {
      "restore_job_id":"e9ba8ff8-7948-4cfa-ba43-34227f6d30d4",
      "index_id":"025117b3-e683-423c-b2d1-6d30fbe5027f"
  }
  ```

  ```json curl theme={null}
  {
      "restore_job_id":"e9ba8ff8-7948-4cfa-ba43-34227f6d30d4",
      "index_id":"025117b3-e683-423c-b2d1-6d30fbe5027f"
  }
  ```
</ResponseExample>



# Delete a backup
Source: https://docs.pinecone.io/reference/api/2025-04/control-plane/delete_backup

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-04/db_control_2025-04.oas.yaml delete /backups/{backup_id}
Delete a backup.

<RequestExample>
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
</RequestExample>

<ResponseExample />



# Delete a collection
Source: https://docs.pinecone.io/reference/api/2025-04/control-plane/delete_collection

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-04/db_control_2025-04.oas.yaml delete /collections/{collection_name}
Delete an existing collection.
Serverless indexes do not support collections.


<RequestExample>
  ```python Python theme={null}
  # pip install "pinecone[grpc]"
  from pinecone.grpc import PineconeGRPC as Pinecone

  pc = Pinecone(api_key='API_KEY')
  pc.delete_collection("example-collection")
  ```

  ```javascript JavaScript theme={null}
  // npm install @pinecone-database/pinecone
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' })

  await pc.deleteCollection("example-collection");
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Pinecone;

  public class DeleteCollectionExample {
      public static void main(String[] args) {
          Pinecone pc = new Pinecone.Builder("YOUR_API_KEY").build();
          pc.deleteCollection("example-collection");
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

      collectionName := "example-collection"

      err = pc.DeleteCollection(ctx, collectionName)
      if err != nil {
  	    log.Fatalf("Failed to delete collection: %v\n", err)
      } else {
          if len(collections) == 0 {
              fmt.Printf("No collections found in project")
          } else {
              fmt.Printf("Successfully deleted collection \"%v\"\n", collectionName)
          }
      }
  }
  ```

  ```csharp C# theme={null}
  using Pinecone;

  var pinecone = new PineconeClient("YOUR_API_KEY");

  await pinecone.DeleteCollectionAsync("example-collection");
  ```

  ```shell curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl -X DELETE "https://api.pinecone.io/collections/example-collection" \
       -H "Api-Key: $PINECONE_API_KEY" \
       -H "X-Pinecone-API-Version: 2025-04"
  ```
</RequestExample>

<ResponseExample />



# Describe a backup
Source: https://docs.pinecone.io/reference/api/2025-04/control-plane/describe_backup

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-04/db_control_2025-04.oas.yaml get /backups/{backup_id}
Get a description of a backup.

<RequestExample>
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
</RequestExample>

<ResponseExample>
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
</ResponseExample>



# Describe a collection
Source: https://docs.pinecone.io/reference/api/2025-04/control-plane/describe_collection

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-04/db_control_2025-04.oas.yaml get /collections/{collection_name}
Get a description of a collection.
Serverless indexes do not support collections.


<RequestExample>
  ```python Python theme={null}
  # pip install "pinecone[grpc]"
  from pinecone.grpc import PineconeGRPC as Pinecone

  pc = Pinecone(api_key='API_KEY')
  pc.describe_collection(name="tiny-collection")
  ```

  ```javascript JavaScript theme={null}
  // npm install @pinecone-database/pinecone
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  await pc.describeCollection('tiny-collection');
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Pinecone;
  import org.openapitools.client.model.CollectionModel;

  public class DescribeCollectionExample {
      public static void main(String[] args) {
          Pinecone pc = new Pinecone.Builder("YOUR_API_KEY").build();
          CollectionModel collectionModel = pc.describeCollection("tiny-collection");
          System.out.println(collectionModel);
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

      collectionName := "tiny-collection"

      collection, err := pc.DescribeCollection(ctx, collectionName)
      if err != nil {
          log.Fatalf("Error describing collection %v: %v", collectionName, err)
      } else {
          fmt.Printf("Collection: %+v", collection)
      }
  }
  ```

  ```csharp C# theme={null}
  using Pinecone;

  var pinecone = new PineconeClient("YOUR_API_KEY");

  var collectionModel = await pinecone.DescribeCollectionAsync("tiny-collection");

  Console.WriteLine(collectionModel);
  ```

  ```shell curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl -X GET "https://api.pinecone.io/collections/tiny-collection" \
       -H "Api-Key: $PINECONE_API_KEY" \
       -H "X-Pinecone-API-Version: 2025-04"
  ```
</RequestExample>

<ResponseExample>
  ```json  theme={null}
  {
      "name": "example-collection",
      "status": "Ready",
      "environment": "us-east-1-aws",
      "size": 3075398,
      "vector_count": 99,
      "dimension": 1536
  }
  ```
</ResponseExample>



# Describe a restore job
Source: https://docs.pinecone.io/reference/api/2025-04/control-plane/describe_restore_job

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-04/db_control_2025-04.oas.yaml get /restore-jobs/{job_id}
Get a description of a restore job.

<RequestExample>
  ```python Python theme={null}
  from pinecone import Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  restore_job = pc.describe_restore_job(job_id="9857add2-99d4-4399-870e-aa7f15d8d326")

  print(restore_job)
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' })

  const restoreJob = await pc.describeRestoreJob('9857add2-99d4-4399-870e-aa7f15d8d326');

  console.log(restoreJob);
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Pinecone;
  import org.openapitools.db_control.client.ApiException;
  import org.openapitools.db_control.client.model.*;

  public class CreateIndexFromBackup {
      public static void main(String[] args) throws ApiException {
          Pinecone pc = new Pinecone.Builder("YOUR_API-KEY").build();

          RestoreJobModel restoreJob = pc.describeRestoreJob("9857add2-99d4-4399-870e-aa7f15d8d326");

          System.out.println(restoreJob);
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

  	restoreJob, err := pc.DescribeRestoreJob(ctx, "e9ba8ff8-7948-4cfa-ba43-34227f6d30d4")
  	if err != nil {
  		log.Fatalf("Failed to describe restore job: %v", err)
  	}

  	fmt.Printf(prettifyStruct(restoreJob))
  }
  ```

  ```csharp C# theme={null}
  using Pinecone;

  var pinecone = new PineconeClient("YOUR_API_KEY");

  var job = await pinecone.RestoreJobs.GetAsync("9857add2-99d4-4399-870e-aa7f15d8d326");

  Console.WriteLine(job);
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  JOB_ID="9857add2-99d4-4399-870e-aa7f15d8d326"

  curl -X GET "https://api.pinecone.io/restore-jobs/$JOB_ID" \
       -H "X-Pinecone-Api-Version: 2025-04" \
       -H "Api-Key: $PINECONE_API_KEY" \
       -H 'accept: application/json'
  ```
</RequestExample>

<ResponseExample>
  ```python Python theme={null}
  {'backup_id': '94a63aeb-efae-4f7a-b059-75d32c27ca57',
   'completed_at': datetime.datetime(2025, 4, 25, 18, 14, 11, 74618, tzinfo=tzutc()),
   'created_at': datetime.datetime(2025, 4, 25, 18, 14, 5, 227526, tzinfo=tzutc()),
   'percent_complete': 100.0,
   'restore_job_id': '9857add2-99d4-4399-870e-aa7f15d8d326',
   'status': 'Completed',
   'target_index_id': '0d8aed24-adf8-4b77-8e10-fd674309dc85',
   'target_index_name': 'restored-index'}
  ```

  ```javascript JavaScript theme={null}
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
  ```

  ```java Java theme={null}
  class RestoreJobModel {
      restoreJobId: cf597d76-4484-4b6c-b07c-2bfcac3388aa
      backupId: 0d75b99f-be61-4a93-905e-77201286c02e
      targetIndexName: restored-index
      targetIndexId: 0d8aed24-adf8-4b77-8e10-fd674309dc85
      status: Completed
      createdAt: 2025-05-16T20:09:18.700631Z
      completedAt: 2025-05-16T20:11:30.673296Z
      percentComplete: 100.0
      additionalProperties: null
  }
  ```

  ```go Go theme={null}
  {
    "backup_id": "8c85e612-ed1c-4f97-9f8c-8194e07bcf71",
    "completed_at": "2025-05-16T20:11:30.673296Z",
    "created_at": "2025-05-16T20:09:18.700631Z",
    "percent_complete": 100,
    "restore_job_id": "e9ba8ff8-7948-4cfa-ba43-34227f6d30d4",
    "status": "Completed",
    "target_index_id": "025117b3-e683-423c-b2d1-6d30fbe5027f",
    "target_index_name": "restored-index"
  }
  ```

  ```csharp C# theme={null}
  {
    "restore_job_id": "9857add2-99d4-4399-870e-aa7f15d8d326",
    "backup_id": "94a63aeb-efae-4f7a-b059-75d32c27ca57",
    "target_index_name": "restored-index",
    "target_index_id": "0d8aed24-adf8-4b77-8e10-fd674309dc85",
    "status": "Completed",
    "created_at": "2025-04-25T18:14:05.227526Z",
    "completed_at": "2025-04-25T18:14:11.074618Z",
    "percent_complete": 100
  }
  ```

  ```json curl theme={null}
  {
    "restore_job_id": "9857add2-99d4-4399-870e-aa7f15d8d326",
    "backup_id": "94a63aeb-efae-4f7a-b059-75d32c27ca57",
    "target_index_name": "restored-index",
    "target_index_id": "0d8aed24-adf8-4b77-8e10-fd674309dc85",
    "status": "Completed",
    "created_at": "2025-04-25T18:14:05.227526Z",
    "completed_at": "2025-04-25T18:14:11.074618Z",
    "percent_complete": 100
  }
  ```
</ResponseExample>



---
**Navigation:** [← Previous](./22-pulumi.md) | [Index](./index.md) | [Next →](./24-list-collections.md)
