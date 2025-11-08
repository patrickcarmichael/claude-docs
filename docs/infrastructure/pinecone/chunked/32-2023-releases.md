**Navigation:** [← Previous](./31-become-a-pinecone-partner.md) | [Index](./index.md) | [Next →](./33-feature-availability.md)

# 2023 releases
Source: https://docs.pinecone.io/release-notes/2023




## December 2023

### Features

* The free Starter plan now supports up to 100 namespaces. [Namespaces](/guides/index-data/indexing-overview#namespaces) let you partition vectors within an index to speed up queries or comply with [multitenancy](/guides/index-data/implement-multitenancy) requirements.


## November 2023

### Features

* The new [Pinecone AWS Reference Architecture](https://github.com/pinecone-io/aws-reference-architecture-pulumi/tree/main) is an open-source, distributed system that performs vector-database-enabled semantic search over Postgres records. You can use it as a learning resource or as a starting point for high-scale use cases.

### SDKs

* [Canopy](https://github.com/pinecone-io/canopy/blob/main/README.md) is a new open-source Retrieval Augmented Generation (RAG) framework and context engine built on top of Pinecone. It enables you to start chatting with your documents or text data with a few simple commands.\
  The latest version of the Canopy SDK (v0.2.0) adds support for OpenAI SDK v1.2.3. See the [release notes](https://github.com/pinecone-io/canopy/releases/tag/V0.2.0) in GitHub for more details.

### Billing

* Pinecone is now registered to collect Value Added Tax (VAT) or Goods and Services Tax (GST) for accounts based in various global regions. If applicable, add your VAT or GST number to your account under **Settings > Billing**.

### October 2023

### Features

* [Collections](/guides/manage-data/back-up-an-index#pod-based-index-backups-using-collections) are now generally available (GA).

### Regions

* Pinecone Azure support via the [‘eastus-azure\` region](/guides/projects/understanding-projects#project-environments) is now generally available (GA).

### SDKs

* The latest version of our Node SDK is v1.1.2. See the [release notes](https://github.com/pinecone-io/pinecone-ts-client/releases/tag/v1.1.2) in GitHub for more details.

### Console

* The Index Browser is now available in the console. This allows you to preview, query, and filter by metadata directly from the console. The Index Browser can be found within the index detail page.
* We’re improved the design of our metrics page to include new charts for record and error count plus additional latencies (p90, p99) to help triage and understand issues.

### Integrations

* Knowledge Base for Amazon Bedrock is now available in private preview. Integrate your enterprise data via retrieval augmented generation (RAG) when building search and GenAI applications. [Learn more](https://www.pinecone.io/blog/amazon-bedrock-integration/).
* Pinecone Sink Connector for Confluent is now available in public preview. Gain access to data streams from across your business to build a real-time knowledge base for your AI applications. [Learn more](https://www.pinecone.io/confluent-integration).

### Billing

* You can now [sign up for Pinecone billing through Microsoft Marketplace](/guides/organizations/manage-billing/upgrade-billing-plan).

### Privacy

* Pinecone is now HIPAA compliant across all of our cloud providers (AWS, Azure, and GCP).


## September 11, 2023

Pinecone Azure support via the [eastus-azure region](/guides/projects/understanding-projects#project-environments) is now generally available (GA).


## August 14, 2023

Pinecone now supports deploying projects to Azure using the new [eastus-azure region](/guides/projects/understanding-projects#project-environments). This is a public preview environment, so test thoroughly before deploying to production.


## June 21, 2023

The new `gcp-starter` region is now in public preview. This region has distinct limitations from other Starter Plan regions. `gcp-starter` is the default region for some new users.


## April 26, 2023

[Indexes in the starter plan](/guides/index-data/indexing-overview#starter-plan) now support approximately 100,000 1536-dimensional embeddings with metadata. Capacity is proportional for other dimensionalities.


## April 3, 2023

Pinecone now supports [new US and EU cloud regions](/guides/projects/understanding-projects#project-environments).


## March 21, 2023

Pinecone now supports SSO on some Enterprise plans. [Contact Support](https://app.pinecone.io/organizations/-/settings/support) to set up your integration.


## March 1, 2023

Pinecone now supports [40kb of metadata per vector](/guides/index-data/indexing-overview#metadata#supported-metadata-size).


## February 22, 2023

#### Sparse-dense embeddings are now in public preview.

Pinecone now supports [vectors with sparse and dense values](/guides/search/hybrid-search#use-a-single-hybrid-index). To use sparse-dense embeddings in Python, upgrade to Python SDK version 2.2.0.

#### Pinecone Python SDK version 2.2.0 is available

Python SDK version 2.2.0 with support for sparse-dense embeddings is now available on [GitHub](https://github.com/pinecone-io/pinecone-python-client) and [PYPI](https://pypi.org/project/pinecone-client/2.2.0/).


## February 15, 2023

#### New Node.js SDK is now available in public preview

You can now try out our new [Node.js SDK for Pinecone](https://sdk.pinecone.io/typescript/).


## February 14, 2023

#### New usage reports in the Pinecone console

You can now monitor your current and projected Pinecone usage with the [**Usage** dashboard](/guides/manage-cost/monitor-usage-and-costs).


## January 31, 2023

#### Pinecone is now available in AWS Marketplace

You can now [sign up for Pinecone billing through Amazon Web Services Marketplace](/guides/organizations/manage-billing/upgrade-billing-plan).


## January 3, 2023

#### Pinecone Python SDK version 2.1.0 is now available on GitHub.

The [latest release of the Python SDK](https://github.com/pinecone-io/pinecone-python-client/releases/tag/2.1.0) makes the following changes:

* Fixes "Connection Reset by peer" error after long idle periods
* Adds typing and explicit names for arguments in all client operations
* Adds docstrings to all client operations
* Adds Support for batch upserts by passing `batch_size` to the upsert method
* Improves gRPC query results parsing performance



# 2024 releases
Source: https://docs.pinecone.io/release-notes/2024




## December 2024

<Update label="2024-12-23" tags={["Database"]}>
  ### Increased namespaces limit

  Customers on the [Standard plan](https://www.pinecone.io/pricing/) can now have up to 25,000 namespaces per index.
</Update>

<Update label="2024-12-19" tags={["Assistant"]}>
  ### Pinecone Assistant JSON mode and EU region deployment

  Pinecone Assistant can now [return a JSON response](/guides/assistant/chat-with-assistant#json-response).

  ***

  You can now [create an assistant](/reference/api/2025-01/assistant/create_assistant) in the `eu` region.
</Update>

<Update label="2024-12-17" tags={["Database"]}>
  ### Released Spark-Pinecone connector v1.2.0

  Released [`v1.2.0`](https://github.com/pinecone-io/spark-pinecone/releases/tag/v1.2.0) of the [Spark-Pinecone connector](/reference/tools/pinecone-spark-connector). This version introduces support for stream upserts with structured streaming. This enhancement allows users to seamlessly stream data into Pinecone for upsert operations.
</Update>

<Update label="2024-12-10" tags={["Docs"]}>
  ### New integration with HoneyHive

  Added the [HoneyHive](/integrations/honeyhive) integration page.
</Update>

<Update label="2024-12-09" tags={["SDK"]}>
  ### Released Python SDK v5.4.2

  Released [`v5.4.2`](https://github.com/pinecone-io/pinecone-python-client/releases/tag/v5.4.2) of the [Pinecone Python SDK](/reference/python-sdk). This release adds a required keyword argument, `metric`, to the `query_namespaces` method. This change enables the SDK to merge results no matter how many results are returned.
</Update>

<Update label="2024-12-06" tags={["General"]}>
  <img className="block max-w-full" noZoom src="https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/release-notes/launch-week.png?fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=3155e298e3d3636631238d3b3ac05a9f" data-og-width="2038" width="2038" data-og-height="1050" height="1050" data-path="images/release-notes/launch-week.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/release-notes/launch-week.png?w=280&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=36944215c7e424e0c03bdbffc71be67a 280w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/release-notes/launch-week.png?w=560&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=020d85488acfadd9554e2ae19e975fdf 560w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/release-notes/launch-week.png?w=840&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=6b7e05cd22f72c3afb3e01c8ab37d11f 840w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/release-notes/launch-week.png?w=1100&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=e195d61caa0cd69d12339738d532225d 1100w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/release-notes/launch-week.png?w=1650&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=32e430d71f4226fc3045bd2dff063ac9 1650w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/release-notes/launch-week.png?w=2500&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=6267312f97e819865dfa7db6ce869cdd 2500w" />

  ### Launch week: Pinecone Local

  Pinecone now offers Pinecone Local, an in-memory database emulator available as a Docker image. You can use Pinecone Local to [develop your applications locally](/guides/operations/local-development), or to [test your applications in CI/CD](/guides/production/automated-testing), without connecting to your Pinecone account, affecting production data, or incurring any usage or storage fees. Pinecone Local is in [public preview](/release-notes/feature-availability).
</Update>

<Update label="2024-12-05" tags={["General"]}>
  ### Launch week: Enhanced security and access controls

  Support for [customer-managed encryption keys (CMEK)](/guides/production/configure-cmek) is now in [public preview](/release-notes/feature-availability).

  ***

  You can now [change API key permissions](/guides/projects/manage-api-keys#update-an-api-key).

  ***

  Private Endpoints are now in [general availability](/release-notes/feature-availability). Use Private Endpoints to [connect AWS PrivateLink](/guides/production/connect-to-aws-privatelink) to Pinecone while keeping your VPC private from the public internet.

  ***

  [Audit logs](/guides/production/security-overview#audit-logs), now in early access, provide a detailed record of user and API actions that occur within the Pinecone platform.
</Update>

<Update label="2024-12-04" tags={["Database"]}>
  ### Launch week: `pinecone-rerank-v0` and `cohere-rerank-3.5` on Pinecone Inference

  Released [`pinecone-rerank-v0`](/guides/search/rerank-results#pinecone-rerank-v0), Pinecone's state of the art reranking model that out-performs competitors on widely accepted benchmarks. This model is in [public preview](/release-notes/feature-availability).

  ***

  Pinecone Inference now hosts [`cohere-rerank-3.5`](/guides/search/rerank-results#cohere-rerank-3.5), Cohere's leading reranking model.
</Update>

<Update label="2024-12-03" tags={["Database"]}>
  ### Launch week: Integrated Inference

  You can now use [embedding models](/guides/index-data/create-an-index#embedding-models) and [reranking models](/guides/search/rerank-results#reranking-models) hosted on Pinecone as an integrated part of upserting and searching.
</Update>

<Update label="2024-12-05" tags={["SDK"]}>
  ### Released .NET SDK v2.1.0

  Released [`v2.1.0`](https://github.com/pinecone-io/pinecone-dotnet-client/releases/tag/2.1.0) of the [Pinecone .NET SDK](/reference/dotnet-sdk). This version adds support for [index tags](/guides/manage-data/manage-indexes#configure-index-tags) and introduces the `ClientOptions.IsTlsEnabled` property, which must be set to `false` for non-secure client connections.
</Update>

<Update label="2024-12-05" tags={["Docs"]}>
  ### Improved batch deletion guidance

  Improved the guidance and example code for [deleting records in batches](/guides/manage-data/delete-data#delete-records-in-batches).
</Update>

<Update label="2024-12-02" tags={["Database"]}>
  ### Launch week: Released `pinecone-sparse-english-v0`

  Pinecone Inference now supports [`pinecone-sparse-english-v0`](/guides/search/rerank-results#pinecone-sparse-english-v0), Pinecone's sparse embedding model, which estimates the lexical importance of tokens by leveraging their context, unlike traditional retrieval models like BM25, which rely solely on term frequency. This model is in [public preview](/release-notes/feature-availability).
</Update>


## November 2024

<Update label="2024-11-30" tags={["Docs"]}>
  ### Pinecone docs: New workflows and best practices

  Added typical [Pinecone Database and Pinecone Assistant workflows](/guides/get-started/overview) to the Docs landing page.

  ***

  Updated various examples to use the production best practice of [targeting an index by host](/guides/manage-data/target-an-index) instead of name.

  ***

  Updated the [Amazon Bedrock integration setup guide](/integrations/amazon-bedrock#setup-guide). It now utilizes Bedrock Agents.
</Update>

<Update label="2024-11-27" tags={["SDK"]}>
  ### Released Java SDK v3.1.0

  Released [`v3.1.0`](https://github.com/pinecone-io/pinecone-java-client/releases/tag/v3.1.0) of the [Pinecone Java SDK](/reference/java-sdk). This version introduces support for specifying a base URL for control and data plane operations.
</Update>

<Update label="2024-11-25" tags={["Assistant"]}>
  ### Pinecone Assistant: Context snippets and structured data files

  You can now [retrieve the context snippets](/guides/assistant/retrieve-context-snippets) that Pinecone Assistant uses to generate its responses. This data includes relevant chunks, relevancy scores, and references.

  ***

  You can now [upload JSON (.json) and Markdown (.md) files](/guides/assistant/manage-files#upload-a-local-file) to an assistant.
</Update>

<Update label="2024-11-14" tags={["General"]}>
  ### Monthly spend alerts

  You can now set an organization-wide [monthly spend alert](/guides/manage-cost/manage-cost#set-a-monthly-spend-alert). When your organization's spending reaches the specified limit, you will receive an email notification.
</Update>

<Update label="2024-11-14" tags={["SDK"]}>
  ### Released .NET SDK v2.0.0

  Released [`v2.0.0`](https://github.com/pinecone-io/pinecone-dotnet-client/releases/tag/2.0.0) of the [Pinecone .NET SDK](/reference/dotnet-sdk). This version uses the latest stable API version, `2024-10`, and adds support for [embedding](/reference/api/2025-01/inference/generate-embeddings), [reranking](https://docs.pinecone.io/reference/api/2025-01/inference/rerank), and [import](/guides/index-data/import-data). It also adds support for using the .NET SDK with [proxies](/reference/dotnet-sdk#proxy-configuration).
</Update>

<Update label="2024-11-13" tags={["SDK"]}>
  ### Released Python SDK v5.4.0 and v5.4.1

  Released [`v5.4.0`](https://github.com/pinecone-io/pinecone-python-client/releases/tag/v5.4.0) and [`v5.4.1`](https://github.com/pinecone-io/pinecone-python-client/releases/tag/v5.4.1) of the [Pinecone Python SDK](/reference/python-sdk). `v5.4.0` adds a `query_namespaces` utility method to [run a query in parallel across multiple namespaces](/reference/python-sdk#query-across-multiple-namespaces) in an index and then merge the result sets into a single ranked result set with the `top_k` most relevant results. `v5.4.1` adds support for the `pinecone-plugin-inference` package required for some [integrated inference](/reference/api/introduction#inference) operations.
</Update>

<Update label="2024-11-08" tags={["General"]}>
  ### Enabled CSV export of usage and costs

  You can now download a CSV export of your organization's usage and costs from the [Pinecone console](https://app.pinecone.io/organizations/-/settings/usage).
</Update>

<Update label="2024-11-07" tags={["General"]}>
  ### Added Support chat in the console

  You can now chat with the Pinecone support bot and submit support requests directly from the [Pinecone console](https://app.pinecone.io/organizations/-/settings/support).
</Update>

<Update label="2024-11-05" tags={["Docs"]}>
  ### Published Assistant quickstart guide

  Added an [Assistant quickstart](/guides/assistant/quickstart).
</Update>


## October 2024

<Update label="2024-10-31" tags={["SDK"]}>
  ### Cequence released updated Scala SDK

  [Cequence](https://github.com/cequence-io) released a new version of their community-supported [Scala SDK](https://github.com/cequence-io/pinecone-scala) for Pinecone. See their [blog post](https://cequence.io/blog/industry-know-how/introducing-the-pinecone-scala-client-async-intuitive-and-ready-for-action) for details.
</Update>

<Update label="2024-10-28" tags={["Database"]}>
  ### Added index tagging for categorization

  You can now [add index tags](/guides/manage-data/manage-indexes#configure-index-tags) to categorize and identify indexes.
</Update>

<Update label="2024-10-24" tags={["SDK"]}>
  ### Released major SDK updates: Node.js, Go, Java, and Python

  Released [`v4.0.0`](https://github.com/pinecone-io/pinecone-ts-client/releases/tag/v4.0.0) of the [Pinecone Node.js SDK](/reference/node-sdk). This version uses the latest stable API version, `2024-10`, and adds support for [reranking](/guides/search/rerank-results) and [import](/guides/index-data/import-data).

  ***

  Released [`v2.0.0`](https://github.com/pinecone-io/go-pinecone/releases/tag/v2.0.0) of the [Pinecone Go SDK](/reference/go-sdk). This version uses the latest stable API version, `2024-10`, and adds support for [reranking](/guides/search/rerank-results) and [import](/guides/index-data/import-data).

  ***

  Released [`v3.0.0`](https://github.com/pinecone-io/pinecone-java-client/releases/tag/v3.0.0) of the [Pinecone Java SDK](/reference/java-sdk). This version uses the latest stable API version, `2024-10`, and adds support for [embedding](/reference/api/2025-01/inference/generate-embeddings), [reranking](/reference/api/2025-01/inference/rerank), and [import](/guides/index-data/import-data).

  <Warning>
    `v3.0.0` also includes the following [breaking change](/reference/api/versioning#breaking-changes): The `control` class has been renamed `db_control`. Before upgrading to this version, be sure to update all relevant `import` statements to account for this change.

    For example, you would change `import org.openapitools.control.client.model.*;` to `import org.openapitools.db_control.client.model.*;`.
  </Warning>

  ***

  `v5.3.0` and `v5.3.1` of the [Pinecone Python SDK](/reference/python-sdk) use the latest stable API version, `2024-10`. These versions were release previously.
</Update>

<Update label="2024-10-24" tags={["API"]}>
  ### Pinecone API version `2024-10` is now the latest stable version

  `2024-10` is now the latest [stable version](/reference/api/versioning#release-schedule) of the [Database API](/reference/api/2024-10/data-plane/) and [Inference API](/reference/api/2024-10/inference/). For highlights, see [SDKs](#sdks) below.
</Update>

<Update label="2024-10-17" tags={["General"]}>
  ### Pinecone Inference now available on the free Starter plan

  The free [Starter plan](https://www.pinecone.io/pricing/) now supports [reranking documents with Pinecone Inference](/guides/search/rerank-results).
</Update>

<Update label="2024-10-17" tags={["Database"]}>
  ### Customer-managed encryption keys (CMEK) in early access

  You can now use [customer-managed encryption keys (CMEK)](/guides/production/configure-cmek) to secure indexes within a Pinecone project. This feature is in [early access](/release-notes/feature-availability).
</Update>

<Update label="2024-10-07" tags={["Database"]}>
  ### Serverless index monitoring generally available

  Monitoring serverless indexes with [Prometheus](/guides/production/monitoring#monitor-with-prometheus) or [Datadog](/integrations/datadog) is now in [general availability](/release-notes/feature-availability).
</Update>

<Update label="2024-10-03" tags={["Database"]}>
  ### Data import from Amazon S3 in public preview

  You can now [import data](/guides/index-data/import-data) into an index from [Amazon S3](/guides/operations/integrations/integrate-with-amazon-s3). This feature is in [public preview](/release-notes/feature-availability).
</Update>

<Update label="2024-10-02" tags={["Assistant"]}>
  ### Chat and update features added to Assistant

  Added the [`chat_assistant`](/reference/api/2025-01/assistant/chat_assistant) endpoint to the Assistant API. It can be used to chat with your assistant, and get responses and citations back in a structured form.

  ***

  You can now add instructions when [creating](/guides/assistant/create-assistant) or [updating](/guides/assistant/manage-assistants#update-an-existing-assistant) an assistant. Instructions are a short description or directive for the assistant to apply to all of its responses. For example, you can update the instructions to reflect the assistant's role or purpose.

  ***

  You can now [update an existing assistant](/guides/assistant/manage-assistants#update-an-existing-assistant) with new instructions or metadata.
</Update>


## September 2024

<Update label="2024-09-25" tags={["Docs"]}>
  Added the [Matillion](/integrations/matillion) integration page.
</Update>

<Update label="2024-09-23" tags={["Docs"]}>
  Added guidance on using the Node.js SDK with [proxies](/reference/node-sdk#proxy-configuration).
</Update>

<Update label="2024-09-19" tags={["SDK"]}>
  Released [`v5.3.1`](https://github.com/pinecone-io/pinecone-python-client/releases/tag/v5.3.1) of the [Pinecone Python SDK](/reference/python-sdk). This version adds a missing `python-dateutil` dependency.

  ***

  Released [`v1.1.1`](https://github.com/pinecone-io/go-pinecone/releases/tag/v1.1.1) of the [Pinecone Go SDK](/reference/go-sdk). This version adds support for non-secure client connections.

  ***

  Released [`v2.1.0`](https://github.com/pinecone-io/pinecone-java-client/releases/tag/v2.1.0) of the [Pinecone Java SDK](/reference/java-sdk). This version adds support for non-secure client connections.
</Update>

<Update label="2024-09-18" tags={["SDK"]}>
  Released [`v5.3.0`](https://github.com/pinecone-io/pinecone-python-client/releases/tag/v5.3.0) of the [Pinecone Python SDK](/reference/python-sdk). This version adds support for [import](/guides/index-data/import-data) operations. This feature is in [public preview](/release-notes/feature-availability).
</Update>

<Update label="2024-09-18" tags={["Assistant"]}>
  Added the `metrics_alignment` operation, which provides a way to [evaluate the correctness and completeness of a response](/guides/assistant/evaluate-answers) from a RAG system. This feature is in [public preview](/release-notes/feature-availability).

  ***

  When using Pinecone Assistant, you can now [choose an LLM](/guides/assistant/chat-with-assistant#choose-a-model-for-your-assistant) for the assistant to use and [filter the assistant's responses by metadata](/guides/assistant/chat-with-assistant#filter-chat-with-metadata).
</Update>

<Update label="2024-09-18" tags={["Docs"]}>
  Added the [Datavolo](/integrations/datavolo) integration pages.
</Update>

<Update label="2024-09-17" tags={["SDK"]}>
  Released [`v5.2.0`](https://github.com/pinecone-io/pinecone-python-client/releases/tag/v5.2.0) of the [Pinecone Python SDK](/reference/python-sdk). This version adds support for [reranking documents with Pinecone Inference](/guides/search/rerank-results); it is no longer necessary to install the `pinecone-plugin-inference` package separately. This feature is in [public preview](/release-notes/feature-availability).
</Update>

<Update label="2024-09-16" tags={["Database"]}>
  [Prometheus monitoring for serverless indexes](/guides/production/monitoring#monitor-with-prometheus) is now in [public preview](/release-notes/feature-availability).
</Update>

<Update label="2024-09-12" tags={["SDK"]}>
  Released [`v3.0.3`](https://github.com/pinecone-io/pinecone-ts-client/releases/tag/3.0.3) of the [Pinecone Node.js SDK](/reference/node-sdk). This version removes extra logging and makes general internal enhancements.
</Update>

<Update label="2024-09-11" tags={["General"]}>
  If you are upgrading from the [Starter plan](https://www.pinecone.io/pricing/), you can now connect your Pinecone organization to the [AWS Marketplace](/guides/organizations/manage-billing/upgrade-billing-plan), [Google Cloud Marketplace](/guides/organizations/manage-billing/upgrade-billing-plan), or [Microsoft Marketplace](/guides/organizations/manage-billing/upgrade-billing-plan) for billing purposes.
</Update>

<Update label="2024-09-11" tags={["General"]}>
  Refreshed the navigation and overall visual interface of the [Pinecone console](https://app.pinecone.io/organizations/-/projects/-/).
</Update>

<Update label="2024-09-11" tags={["Docs"]}>
  Added Go examples for [batch upserts](/guides/index-data/upsert-data#upsert-in-batches), [parallel upserts](/guides/index-data/upsert-data#send-upserts-in-parallel), and [deleting all records for a parent document](/guides/index-data/data-modeling#delete-chunks).
</Update>


## August 2024

<Update label="2024-08-28" tags={["Docs"]}>
  Added the [Aryn](/integrations/aryn) integration page.
</Update>

<Update label="2024-08-28" tags={["SDK"]}>
  Released [`v3.0.2`](https://github.com/pinecone-io/pinecone-ts-client/releases/tag/3.0.2) of the [Pinecone Node.js SDK](/reference/node-sdk). This version removes a native Node utility function that was causing issues for users running in `Edge`. There are no downstream affects of its removal; existing code should not be impacted.
</Update>

<Update label="2024-08-27" tags={["SDK"]}>
  Released [`v5.1.0`](https://github.com/pinecone-io/pinecone-python-client/releases/tag/v5.1.0) of the [Pinecone Python SDK](/reference/python-sdk). With this version, the SDK can now be installed with `pip install pinecone` / `pip install "pinecone[grpc]"`. This version also includes a `has_index()` helper function to check if an index exists.

  ***

  Released [`v0.1.0`](https://github.com/pinecone-io/pinecone-rust-client/releases/tag/v0.1.0) and [`v0.1.1`](https://github.com/pinecone-io/pinecone-rust-client/releases/tag/v0.1.1) of the [Pinecone Rust SDK](/reference/rust-sdk). The Rust SDK is in "alpha" and is under active development. The SDK should be considered unstable and should not be used in production. Before a 1.0 release, there are no guarantees of backward compatibility between minor versions. See the [Rust SDK README](https://github.com/pinecone-io/pinecone-rust-client/blob/main/README.md) for full installation instructions and usage examples.
</Update>

<Update label="2024-08-27" tags={["SDK"]}>
  Released [`v1.0.0`](https://github.com/pinecone-io/pinecone-dotnet-client/releases/tag/1.0.0) of the [Pinecone .NET SDK](/reference/dotnet-sdk). For usage examples, see [our guides](/guides/get-started/quickstart) or the [GitHub README](https://github.com/pinecone-io/pinecone-dotnet-client/blob/main/README.md).
</Update>

<Update label="2024-08-26" tags={["Database"]}>
  You can now [back up](/guides/manage-data/back-up-an-index) and [restore](/guides/manage-data/restore-an-index) serverless indexes. This feature is in public preview.

  ***

  Serverless indexes are now in [general availability on GCP and Azure](/guides/index-data/create-an-index#cloud-regions) for Standard and Enterprise plans.

  ***

  You can now deploy [serverless indexes](/guides/index-data/indexing-overview) in the `europe-west1` (Netherlands) region of GCP.
</Update>

<Update label="2024-08-26" tags={["SDK"]}>
  Released [`v1.1.0`](https://github.com/pinecone-io/go-pinecone/releases/tag/v1.1.0) of the [Pinecone Go SDK](/reference/go-sdk). This version adds support for generating embeddings via [Pinecone Inference](/reference/api/introduction#inference).
</Update>

<Update label="2024-08-21" tags={["Docs"]}>
  Added the [Nexla](/integrations/nexla) integration page.
</Update>

<Update label="2024-08-15" tags={["Assistant"]}>
  [Pinecone Assistant](/guides/assistant/overview) is now in [public preview](/release-notes/feature-availability).
</Update>

<Update label="2024-08-13" tags={["API"]}>
  The Pinecone Inference API now supports [reranking](https://docs.pinecone.io/guides/search/rerank-results). This feature is in [public preview](/release-notes/feature-availability).
</Update>

<Update label="2024-08-06" tags={["SDK"]}>
  Released [`v1.0.0`](https://github.com/pinecone-io/go-pinecone/releases/tag/v1.0.0) of the [Pinecone Go SDK](/reference/go-sdk). This version depends on Pinecone API version `2024-07` and includes the ability to [prevent accidental index deletion](/guides/manage-data/manage-indexes#configure-deletion-protection). With this version, the Go SDK is [officially supported](/troubleshooting/pinecone-support-slas) by Pinecone.
</Update>

<Update label="2024-08-05" tags={["Docs"]}>
  Added the [Nuclia](/integrations/nuclia) integration page
</Update>


## July 2024

<Update label="2024-07-30" tags={["Docs"]}>
  Added the [Redpanda](/integrations/redpanda) integration page.
</Update>

<Update label="2024-07-26" tags={["Docs"]}>
  Updated the [Build a RAG chatbot](/guides/get-started/build-a-rag-chatbot) guide to use Pinecone Inference for generating embeddings.
</Update>

<Update label="2024-07-19" tags={["Database"]}>
  Added the ability to [prevent accidental index deletion](/guides/manage-data/manage-indexes#configure-deletion-protection).
</Update>

<Update label="2024-07-19" tags={["SDK"]}>
  Released [`v5.0.0`](https://github.com/pinecone-io/pinecone-python-client/releases/tag/v5.0.0) of the [Pinecone Python SDK](/reference/python-sdk). This version depends on Pinecone API version `2024-07` and includes the ability to [prevent accidental index deletion](/guides/manage-data/manage-indexes#configure-deletion-protection). Additionally, the `pinecone-plugin-inference` package required to [generate embeddings with Pinecone Inference](/reference/api/2025-01/inference/generate-embeddings) is now included by default; it is no longer necessary to install the plugin separately.

  ***

  Released [`v3.0.0`](https://github.com/pinecone-io/pinecone-ts-client/releases/tag/v3.0.0) of the [Pinecone Node.js SDK](/reference/node-sdk). This version depends on Pinecone API version `2024-07` and includes the ability to [prevent accidental index deletion](/guides/manage-data/manage-indexes#configure-deletion-protection). Additionally, this version supports generating embeddings via [Pinecone Inference](/reference/api/2025-01/inference/generate-embeddings).

  ***

  Released [`v2.0.0`](https://github.com/pinecone-io/pinecone-java-client/releases/tag/v2.0.0) of the [Pinecone Java SDK](/reference/java-sdk). This version depends on Pinecone API version `2024-07` and includes the ability to [prevent accidental index deletion](/guides/manage-data/manage-indexes#configure-deletion-protection). Additionally, this version includes the following **breaking changes**:

  * `createServerlessIndex()` now requires a new argument: `DeletionProtection.ENABLED` or `DeletionProtection.DISABLED`.
  * `configureIndex()` has been renamed `configurePodsIndex()`.

  For more details, see the [Java SDK v2.0.0 migration guide](https://github.com/pinecone-io/pinecone-java-client/blob/main/v2-migration.md).
</Update>

<Update label="2024-07-19" tags={["API"]}>
  Released version `2024-07` of the [Database API](/reference/api/2024-07/data-plane/) and Inference API. This version includes the following highlights:

  * The [`create_index`](/reference/api/2024-07/control-plane/create_index) and [`configure_index`](/reference/api/2024-07/control-plane/configure_index) endpoints now support the `deletion_protection` parameter. Setting this parameter to `"enabled"` prevents an index from accidental deletion. For more details, see [Prevent index deletion](/guides/manage-data/manage-indexes#configure-deletion-protection).

  * The [`describe_index`](/reference/api/2024-07/control-plane/describe_index) and [`list_index`](/reference/api/2024-07/control-plane/list_indexes) responses now include the `deletion_protection` field. This field indicates whether deletion protection is enabled for an index.

  * The `spec.serverless.cloud` and `spec.serverless.region` parameters of [`create_index`](/reference/api/2024-07/control-plane/create_index) now support `gcp` / `us-central` and `azure` / `eastus2` as part of the serverless public preview on GCP and Azure.
</Update>

<Update label="2024-07-17" tags={["Database"]}>
  Serverless indexes are now in [public preview on Azure](/guides/index-data/create-an-index#cloud-regions) for Standard and Enterprise plans.
</Update>

<Update label="2024-07-10" tags={["Database"]}>
  Released [version 1.1.0](https://github.com/pinecone-io/spark-pinecone/releases/tag/v1.1.0) of the official Spark connector for Pinecone. In this release, you can now set a [source tag](/integrations/build-integration/attribute-usage-to-your-integration). Additionally, you can now [upsert records](/guides/index-data/upsert-data) with 40KB of metadata, increased from 5KB.
</Update>

<Update label="2024-07-01" tags={["Database"]}>
  Serverless indexes are now in [public preview on GCP](/guides/index-data/create-an-index#cloud-regions) for Standard and Enterprise plans.
</Update>

<Update label="2024-07-01" tags={["Docs"]}>
  Added an introduction to [key concepts in Pinecone](/guides/get-started/concepts) and how they relate to each other.

  ***

  Added the [Twelve Labs](/integrations/twelve-labs) integration page.
</Update>


## June 2024

<Update label="2024-06-30" tags={["Docs"]}>
  Added a [model gallery](/models/overview) with details and guidance on popular embedding and reranking models, including models hosted on Pinecone's infrastructure.
</Update>

<Update label="2024-06-28" tags={["SDK"]}>
  Released [version 1.2.2](https://github.com/pinecone-io/pinecone-java-client/releases/tag/v1.2.2) of the Pinecone Java SDK. This release simplifies the proxy configuration process. It also fixes an issue where the user agent string was not correctly setup for gRPC calls. Now, if the source tag is set by the user, it is appended to the custom user agent string.
</Update>

<Update label="2024-06-27" tags={["Database"]}>
  You can now load a [sample dataset](/guides/data/use-sample-datasets) into a new project.

  ***

  Simplified the process for [migrating paid pod indexes to serverless](/guides/indexes/pods/migrate-a-pod-based-index-to-serverless).
</Update>

<Update label="2024-06-25" tags={["Assistant"]}>
  The [Assistant API](/guides/assistant/overview) is now in beta release.
</Update>

<Update label="2024-06-20" tags={["Database"]}>
  The [Inference API](/reference/api/introduction#inference) is now in public preview.
</Update>

<Update label="2024-06-18" tags={["Docs"]}>
  Added a new [legal semantic search](https://docs.pinecone.io/examples/sample-apps/legal-semantic-search) sample app that demonstrates low-latency natural language search over a knowledge base of legal documents.
</Update>

<Update label="2024-06-17" tags={["Docs"]}>
  Added the [Instill](/integrations/instill) integration page.
</Update>

<Update label="2024-06-07" tags={["Docs"]}>
  Added the [Langtrace](/integrations/langtrace) integration page.
</Update>

<Update label="2024-06-06" tags={["Docs"]}>
  Updated Python code samples to use the gRPC version of the [Python SDK](/reference/python-sdk), which is more performant than the Python SDK that interacts with Pinecone via HTTP requests.
</Update>

<Update label="2024-06-06" tags={["SDK"]}>
  Released [version 4.1.1](https://github.com/pinecone-io/pinecone-python-client/releases/tag/v4.1.1) of the Pinecone Python SDK. In this release, you can now use colons inside source tags. Additionally, the gRPC version of the Python SDK now allows retries of up to `MAX_MSG_SIZE`.
</Update>

<Update label="2024-06-05" tags={["Database"]}>
  The Enterprise [quota for namespaces per serverless index](/reference/api/database-limits#namespaces-per-serverless-index) has increased from 50,000 to 100,000.
</Update>

<Update label="2024-06-04" tags={["Docs"]}>
  Added the [Fleak](/integrations/fleak) integration page.
</Update>


## May 2024

<Update label="2024-05-31" tags={["SDK"]}>
  Released [version 1.2.1](https://github.com/pinecone-io/pinecone-java-client/releases/tag/v1.2.1) of the [Pinecone Java SDK](/reference/pinecone-sdks#java-client). This version fixes the error `Could Not Find NameResolverProvider` using uber jar.
</Update>

<Update label="2024-05-31" tags={["Docs"]}>
  Added the [Gathr](/integrations/gathr) integration page.
</Update>

<Update label="2024-05-30" tags={["SDK"]}>
  Released [version 1.1.0](https://github.com/pinecone-io/pinecone-java-client/releases/tag/v1.1.0) of the [Pinecone Java SDK](/reference/pinecone-sdks#java-client). This version adds the ability to [list record IDs with a common prefix](/guides/manage-data/list-record-ids#list-the-ids-of-records-with-a-common-prefix).
</Update>

<Update label="2024-05-29" tags={["SDK"]}>
  Released version [1.2.0](https://github.com/pinecone-io/pinecone-java-client/releases/tag/v1.2.0) of the [Pinecone Java SDK](/reference/pinecone-sdks#java-client). This version adds the ability to [list all record IDs in a namespace](/guides/manage-data/list-record-ids#list-the-ids-of-all-records-in-a-namespace).
</Update>

<Update label="2024-05-29" tags={["Docs"]}>
  Added the following integration pages:

  * [Apify](/integrations/apify)
  * [Context Data](/integrations/context-data)
  * [Estuary](/integrations/estuary)
  * [GitHub Copilot](/integrations/github-copilot)
  * [Jina](/integrations/jina)
  * [FlowiseAI](/integrations/flowise)
  * [OctoAI](/integrations/octoai)
  * [Streamnative](/integrations/streamnative)
  * [Traceloop](/integrations/traceloop)
  * [Unstructured](/integrations/unstructured)
  * [VoyageAI](/integrations/voyage)
</Update>

<Update label="2024-05-21" tags={["General"]}>
  You can now use the `ConnectPopup` function to bypass the [**Connect** widget](/integrations/build-integration/connect-your-users-to-pinecone) and open the "Connect to Pinecone" flow in a popup. This can be used in an app or website for a seamless Pinecone signup and login process.
</Update>

<Update label="2024-05-16" tags={["Database"]}>
  Released [version 1.0.0](https://github.com/pinecone-io/spark-pinecone/releases/tag/v1.0.0) of the official Spark connector for Pinecone. In this release, you can now upsert records into [serverless indexes](/guides/index-data/indexing-overview).
</Update>

<Update label="2024-05-08" tags={["Database"]}>
  Pinecone now supports [AWS PrivateLink](/guides/production/connect-to-aws-privatelink). Create and use [Private Endpoints](/guides/production/connect-to-aws-privatelink#manage-private-endpoints) to connect AWS PrivateLink to Pinecone while keeping your VPC private from the public internet.
</Update>

<Update label="2024-05-01" tags={["SDK"]}>
  Released [version 4.0.0](https://github.com/pinecone-io/pinecone-python-client/releases/tag/v4.0.0) of the Pinecone Python SDK. In this release, we are upgrading the `protobuf` dependency in our optional `grpc` extras from `3.20.3` to `4.25.3`. Significant performance improvements have been made with this update. This is a breaking change for users of the optional GRPC addon ([installed with `pinecone[grpc]`](https://github.com/pinecone-io/pinecone-python-client?tab=readme-ov-file#working-with-grpc-for-improved-performance)).
</Update>


## April 2024

<Update label="2024-04-30" tags={["Docs"]}>
  * The docs now have a new AI chatbot. Use the search bar at the top of our docs to find related content across all of our resources.
  * We've updated the look and feel of our [example notebooks](/examples/notebooks) and [sample apps](/examples/sample-apps). A new sample app, [Namespace Notes](/examples/sample-apps/namespace-notes), a simple multi-tenant RAG app that uploads documents, has also been added.
</Update>

<Update label="2024-04-30" tags={["Database"]}>
  The free [Starter plan](https://www.pinecone.io/pricing/) now includes 1 project, 5 serverless indexes in the `us-east-1` region of AWS, and up to 2 GB of storage. Although the Starter plan has stricter [limits](/reference/api/database-limits) than other plans, you can [upgrade](/guides/organizations/manage-billing/upgrade-billing-plan) whenever you're ready.
</Update>

<Update label="2024-04-26" tags={["General"]}>
  Pinecone now provides a [**Connect** widget](/integrations/build-integration/connect-your-users-to-pinecone) that can be embedded into an app, website, or Colab notebook for a seamless signup and login process.
</Update>

<Update label="2024-04-22" tags={["Docs"]}>
  Added the [lifecycle policy of the Pinecone API](/release-notes/feature-availability), which describes the availability phases applicable to APIs, features, and SDK versions.
</Update>

<Update label="2024-04-22" tags={["Database"]}>
  As announced in January 2024, [control plane](/reference/api/2024-07/control-plane) operations like `create_index`, `describe_index`, and `list_indexes` now use a single global URL, `https://api.pinecone.io`, regardless of the cloud environment where an index is hosted. This is now in general availability. As a result, the legacy version of the API, which required regional URLs for control plane operations, is deprecated as of April 15, 2024 and will be removed in a future, to be announced, release.
</Update>

<Update label="2024-04-15" tags={["Docs"]}>
  Added the [Terraform](/integrations/terraform) integration page.
</Update>

<Update label="2024-04-15" tags={["SDK"]}>
  Released version 0.9.0 of the [Canopy SDK](https://github.com/pinecone-io/canopy/blob/main/README.md). This version adds support for OctoAI LLM and embeddings, and Qdrant as a supported knowledge base. See the [v0.9.0 release notes](https://github.com/pinecone-io/canopy/releases/tag/v0.9.0) in GitHub for more details.
</Update>

<Update label="2024-04-12" tags={["Database"]}>
  You can now deploy [serverless indexes](/guides/index-data/indexing-overview) in the `eu-west-1` region of AWS.
</Update>

<Update label="2024-04-12" tags={["SDK"]}>
  Released version 1.0.0 of the [Pinecone Java SDK](/reference/pinecone-sdks#java-client). With this version, the Java SDK is [officially supported](/troubleshooting/pinecone-support-slas) by Pinecone. For full details on the release, see the [v1.0.0 release notes](https://github.com/pinecone-io/pinecone-java-client/releases/tag/v1.0.0) in GitHub. For usage examples, see [our guides](/guides/get-started/quickstart) or the [GitHub README](https://github.com/pinecone-io/pinecone-java-client/blob/main/README.md). To migrate to v1.0.0 from version 0.8.x or below, see the [Java v1.0.0 migration guide](https://github.com/pinecone-io/pinecone-java-client/blob/main/v1-migration.md).
</Update>


## March 2024

<Update label="2024-03-31" tags={["Docs"]}>
  Added a [Troubleshooting](https://docs.pinecone.io/troubleshooting/) section, which includes content on best practices, troubleshooting, and how to address common errors.

  ***

  Added an explanation of the [Pinecone serverless architecture](/guides/get-started/database-architecture), including descriptions of the high-level components and explanations of the distinct paths for writes and reads.

  ***

  Added [considerations for querying serverless indexes with metadata filters](/guides/index-data/indexing-overview#metadata#considerations-for-serverless-indexes).
</Update>

<Update label="2024-03-30" tags={["SDK"]}>
  Released [version 3.2.2](https://github.com/pinecone-io/pinecone-python-client/releases/tag/v3.2) of the [Pinecone Python SDK](/reference/python-sdk). This version fixes a minor issue introduced in v3.2.0 that resulted in a `DeprecationWarning` being incorrectly shown to users who are not passing in the deprecated `openapi_config` property. This warning can safely be ignored by anyone who is not preparing to upgrade.
</Update>

<Update label="2024-03-29" tags={["SDK"]}>
  Released [version 3.2.0](https://github.com/pinecone-io/pinecone-python-client/releases/tag/v3.2.0) of the [Pinecone Python SDK](/reference/python-sdk). This version adds four optional configuration properties that enable the use of Pinecone [via proxy](/reference/python-sdk#proxy-configuration).
</Update>

<Update label="2024-03-28" tags={["SDK"]}>
  Released [version 2.2.0](https://github.com/pinecone-io/pinecone-ts-client/releases/tag/v2.2.0) of the [Pinecone Node.js SDK](/reference/node-sdk). This releases adds an optional `sourceTag` that you can set when constructing a Pinecone client to help Pinecone associate API activity to the specified source.
</Update>

<Update label="2024-03-27" tags={["SDK"]}>
  Released version 0.4.1 of the [Pinecone Go SDK](/reference/pinecone-sdks#go-client). This version adds an optional `SourceTag` that you can set when constructing a Pinecone client to help Pinecone associate API activity to the specified source.

  ***

  Released version 2.2.0 of the [Pinecone Node.js SDK](/reference/node-sdk).

  ***

  Released [version 0.4.1](https://github.com/pinecone-io/go-pinecone/releases/tag/v0.4.1) of the [Pinecone Go SDK](/reference/go-sdk).
</Update>

<Update label="2024-03-25" tags={["SDK"]}>
  Released version 3.2.1 of the [Pinecone Python SDK](/reference/python-sdk). This version adds an optional `source_tag` that you can set when constructing a Pinecone client to help Pinecone associate API activity to the specified source. See the [v3.2.1 release notes](https://github.com/pinecone-io/pinecone-python-client/releases/tag/v3.2.1) in GitHub for more details.
</Update>

<Update label="2024-03-21" tags={["SDK"]}>
  Released version 0.8.1 of the [Canopy SDK](https://github.com/pinecone-io/canopy/blob/main/README.md). This version includes bug fixes, the removal of an unused field for Cohere chat calls, and added guidance on creating a knowledge base with a specified record encoder when using the core library. See the [v0.8.1 release notes](https://github.com/pinecone-io/canopy/releases/tag/v0.8.1) in GitHub for more details.
</Update>

<Update label="2024-03-20" tags={["Database"]}>
  The [Pinecone console](https://app.pinecone.io) has a new look and feel, with a brighter, minimalist design; reorganized menu items for quicker, more intuitive navigation; and easy access to recently viewed indexes in the sidebar.

  ***

  When viewing the list of indexes in a project, you can now search indexes by index name; sort indexes alphabetically, by how recently they were viewed or created, or by status; and filter indexes by index type (serverless, pod-based, or starter).
</Update>

<Update label="2024-03-15" tags={["SDK"]}>
  Released version 0.4.0 of the [Pinecone Go SDK](/reference/pinecone-sdks#go-client). This version is a comprehensive re-write and adds support for all current [Pinecone API operations](/reference/api/introduction).
</Update>

<Update label="2024-03-14" tags={["Database"]}>
  Fixed a bug that caused inaccurate index fullness reporting for some pod-based indexes on GCP.

  ***

  You can now deploy [serverless indexes](/guides/index-data/indexing-overview) in the `us-east-1` region of AWS.
</Update>

<Update label="2024-03-06" tags={["SDK"]}>
  Released version 2.1.0 of the [Pinecone Node.js SDK](/reference/node-sdk). This version adds support for [listing the IDs of records in a serverless index](/guides/manage-data/list-record-ids). You can list all records or just those with a common ID prefix.
</Update>

<Update label="2024-03-05" tags={["General"]}>
  You can now [configure single single-on](/guides/production/configure-single-sign-on/okta) to manage your teams' access to Pinecone through any identity management solution with SAML 2.0 support, such as Okta. This feature is available on the [Enterprise plan](https://www.pinecone.io/pricing/) only.
</Update>


## February 2024

<Update label="2024-02-29" tags={["Docs"]}>
  Updated the [Langchain integration guide](/integrations/langchain) to avoid a [namespace collision issue](/troubleshooting/pinecone-attribute-errors-with-langchain).
</Update>

<Update label="2024-02-27" tags={["SDK"]}>
  The latest version of the [Canopy SDK](https://github.com/pinecone-io/canopy/blob/main/README.md) (v0.8.0) adds support for Pydantic v2. For applications depending on Pydantic v1, this is a breaking change; review the [Pydantic v1 to v2 migration guide](https://docs.pydantic.dev/latest/migration/) and make the necessary changes before upgrading. See the [Canopy SDK release notes](https://github.com/pinecone-io/canopy/releases/tag/v0.8.0) in GitHub for more details.
</Update>

<Update label="2024-02-23" description="SDK">
  The latest version of Pinecone's Python SDK (v3.1.0) adds support for [listing the IDs of records in a serverless index](/guides/manage-data/list-record-ids). You can list all records or just those with a [common ID prefix](/guides/index-data/data-modeling#use-structured-ids). See the [Python SDK release notes](https://github.com/pinecone-io/pinecone-python-client/releases/tag/v3.1.0) in GitHub for more details.
</Update>

<Update label="2024-02-22" tags={["Docs"]}>
  Improved the docs for [setting up billing through the AWS Marketplace](/guides/organizations/manage-billing/upgrade-billing-plan) and [Google Cloud Marketplace](/guides/organizations/manage-billing/upgrade-billing-plan).
</Update>

<Update label="2024-02-16" tags={["Database"]}>
  It is now possible to convert a pod-based starter index to a serverless index. For organizations on the Starter plan, this requires upgrading to Standard or Enterprise; however, upgrading comes with \$100 in serverless credits, which will cover the cost of a converted index for some time.
</Update>

<Update label="2024-02-01" tags={["Docs"]}>
  Added a [Llamaindex integration guide](/integrations/llamaindex) on building a RAG pipeline with LlamaIndex and Pinecone.
</Update>


## January 2024

<Update label="2024-01-31" tags={["SDK"]}>
  The latest version of the [Canopy SDK](https://github.com/pinecone-io/canopy/blob/main/README.md) (v0.6.0) adds support for the new API mentioned above as well as namespaces, LLMs that do not have function calling functionality for query generation, and more. See the [release notes](https://github.com/pinecone-io/canopy/releases/tag/v0.6.0) in GitHub for more details.
</Update>

<Update label="2024-01-09" tags={["SDK"]}>
  The latest versions of Pinecone's Python SDK (v3.0.0) and Node.js SDK (v2.0.0) support the new API. To use the new API, existing users must upgrade to the new client versions and adapt some code. For guidance, see the [Python SDK v3 migration guide](https://canyon-quilt-082.notion.site/Pinecone-Python-SDK-v3-0-0-Migration-Guide-056d3897d7634bf7be399676a4757c7b) and [Node.js SDK v2 migration guide](https://github.com/pinecone-io/pinecone-ts-client/blob/main/v2-migration.md).
</Update>

<Update label="2024-01-09" tags={["Docs"]}>
  The Pinecone documentation is now versioned. The default "latest" version reflects the new Pinecone API. The "legacy" version reflects the previous API, which requires regional URLs for control plane operations and does not support serverless indexes.
</Update>

<Update label="2024-01-09" tags={["API"]}>
  The [new Pinecone API](/reference/api) gives you the same great vector database but with a drastically improved developer experience. The most significant improvements include:

  * [Serverless indexes](/guides/index-data/indexing-overview): With serverless indexes, you don't configure or manage compute and storage resources. You just load your data and your indexes scale automatically based on usage. Likewise, you don't pay for dedicated resources that may sometimes lay idle. Instead, the pricing model for serverless indexes is consumption-based: You pay only for the amount of data stored and operations performed, with no minimums.

  * [Multi-region projects](/guides/projects/understanding-projects): Instead of choosing a cloud region for an entire project, you now [choose a region for each index](/guides/index-data/create-an-index#create-a-serverless-index) in a project. This makes it possible to consolidate related indexes in the same project, even when they are hosted in different regions.

  * [Global URL for control plane operations](/reference): Control plane operations like `create_index`, `describe_index`, and `list_indexes` now use a single global URL, `https://api.pinecone.io`, regardless of the cloud environment where an index is hosted. This simplifies the experience compared to the legacy API, where each environment has a unique URL.
</Update>



# 2025 releases
Source: https://docs.pinecone.io/release-notes/2025




## November 2025

<Update label="2025-11-03" tags={["Assistant"]}>
  ### n8n quickstarts

  Added new quickstart options to create an n8n workflow that downloads files via HTTP and lets you chat with them using Pinecone and OpenAI.

  * [n8n quickstart for Pinecone Assistant](/guides/assistant/quickstart#n8n)
  * [n8n quickstart for Pinecone Database](/guides/get-started/quickstart#n8n)
</Update>

<Update label="2025-11-03" tags={["SDK"]}>
  ### Released Node.js SDK v6.1.3

  Released [`v6.1.3`](https://github.com/pinecone-io/pinecone-ts-client/releases/tag/v6.1.3) of the [Pinecone Node.js SDK](/reference/node-sdk).

  This version of the SDK fixes a bug in `Assistant.listFiles()`. Previously, when passing a `filter` to `listFiles`, the top-level `metadata` object was not handled correctly. This caused the method to return all files, regardless of the filter.

  It's no longer necessary to provide a top-level `metadata` object. Instead, declare metadata fields directly in the `filter` object:

  * ✅ `const files = await assistant.listFiles({ filter: { document_type: 'manuscript' } });`
  * ❌ `const files = await assistant.listFiles({ filter: { metadata: { document_type: 'manuscript' } } });`

  If you're using the old syntax, update it so that your filter works correctly. For more information about listing the files associated with an assistant, see [Manage files](/guides/assistant/manage-files).
</Update>


## October 2025

<Update label="2025-10-30" tags={["Assistant"]}>
  ### Increased files per assistant on the Starter plan

  On the Starter plan, you can now upload up to 100 files to an assistant. Previously, the limit was 10 files.

  To learn more, see [Assistant limits](/guides/assistant/pricing-and-limits#assistant-limits).
</Update>

<Update label="2025-10-23" tags={["General"]}>
  ### Enhanced monthly spend alerts

  You can now set multiple spend alerts to monitor your organization's monthly spending. These alerts notify designated recipients when spending reaches specified thresholds. The alerts automatically reset at the start of each monthly billing cycle.

  Additionally, to protect from unexpected cost increases, Pinecone sends an alert when spending exceeds double your previous month's invoice amount. While the alert threshold is fixed, you can modify which email addresses receive the alert and enable or disable the alert notifications.

  To learn more, see [Manage cost](/guides/manage-cost/manage-cost).
</Update>

<Update label="2025-10-16" tags={["Docs"]}>
  ### Agentic quickstart

  Added new [agentic quickstart](/guides/get-started/quickstart#cursor) options to help you build Pinecone applications with AI coding agents like Claude Code and Cursor. Instead of copying code snippets, you work with an agent that understands Pinecone APIs and implements production-ready patterns automatically.
</Update>

<Update label="2025-10-16" tags={["Docs"]}>
  ### AI Engine integration

  Added the [AI Engine](/integrations/ai-engine) integration page.
</Update>

<Update label="2025-10-09" tags={["CLI"]}>
  ## Pinecone CLI v0.1.0

  We've released [v0.1.0](https://github.com/pinecone-io/cli/releases/tag/v0.1.0) of the [Pinecone CLI](https://github.com/pinecone-io/cli). The CLI lets you manage Pinecone infrastructure (organizations, projects, indexes, and API keys) directly from your terminal and in CI/CD.

  This feature is in [public preview](/release-notes/feature-availability). We'll be adding more features to the CLI over time, and we'd love your [feedback](https://community.pinecone.io/) on this early version.

  For more information, see the [CLI overview](/reference/cli/overview).
</Update>


## September 2025

<Update label="2025-09-30" tags={["Docs"]}>
  ### Production best practices

  Added a new [error handling guide](/guides/production/error-handling) to help you handle errors gracefully in production, including implementing retry logic with exponential backoff for rate limits and transient errors.

  Updated the [production checklist](/guides/production/production-checklist) with enhanced guidance on data modeling, database limits, and performance optimization.
</Update>

<Update label="2025-09-11" tags={["Docs"]}>
  ### Changing payment methods

  Added a new guide to help customers [change their payment method](/guides/organizations/manage-billing/change-payment-method) for Pinecone's Standard or Enterprise plan, including switching from credit card to marketplace billing and vice versa.
</Update>

<Update label="2025-09-04" tags={["Database"]}>
  ### Released Pinecone Terraform Provider v2.0.0

  Released [v2.0.0](https://github.com/pinecone-io/terraform-provider-pinecone/releases/tag/v2.0.0) of the [Terraform Provider for Pinecone](/integrations/terraform). This version adds support for managing API keys and projects.
</Update>

<Update label="2025-09-02" tags={["Assistant"]}>
  ### Multimodal context for assistants

  Assistants can now gather context from images in PDF files. To learn more, see [Multimodal context for assistants](/guides/assistant/multimodal). This feature is in [public preview](/release-notes/feature-availability).
</Update>


## August 2025

<Update label="2025-08-29" tags={["Database"]}>
  ### Filter lexical search by required terms

  You can now filter lexical search results to require specific terms. This is especially useful for filtering out results that don't contain essential keywords, requiring domain-specific terminology in results, and ensuring specific people, places, or things are mentioned. This feature is in [public preview](/release-notes/feature-availability).

  To learn more, see [Filter by required terms](/guides/search/lexical-search#filter-by-required-terms).
</Update>

<Update label="2025-08-26" tags={["Docs"]}>
  ### Zapier integration

  Added the [Zapier](/integrations/zapier) integration page.
</Update>

<Update label="2025-08-25" tags={["General"]}>
  ### SSO setup improvements

  We've streamlined the SSO setup process, eliminating the need to add placeholder URLs to your identity provider. To learn more, see [Configure SSO with Okta](/guides/production/configure-single-sign-on/okta).
</Update>

<Update label="2025-08-25" tags={["Database"]}>
  ### Update metadata across multiple records

  You can now [update metadata across multiple records](/guides/manage-data/update-data#update-metadata-across-multiple-records) in a namespace. This feature is in [early access](/release-notes/feature-availability).
</Update>

<Update label="2025-08-13" tags={["Database"]}>
  ### Data import from Azure Blob Storage

  Now, you can import data from an Azure Blob Storage container into a Pinecone index. This feature is in [public preview](/release-notes/feature-availability).

  To learn more, read:

  * [Integrate with Azure Blob Storage](/guides/operations/integrations/integrate-with-azure-blob-storage)
  * [Import records](/guides/index-data/import-data)
  * [Pinecone's pricing](https://www.pinecone.io/pricing/)
</Update>

<Update label="2025-08-12" tags={["Assistant"]}>
  ### Assistant MCP server endpoint update

  **Breaking Change**: After August 31, 2025 at 11:59:59 PM UTC, the SSE-based MCP endpoint for assistants (`/mcp/assistants/<YOUR_ASSISTANT_NAME>/sse`) will no longer work.

  Before then, update your applications to use the streamable HTTP transport MCP endpoint (`/mcp/assistants/<YOUR_ASSISTANT_NAME>`). This endpoint follows the current [MCP protocol specification](https://modelcontextprotocol.io/specification/2025-06-18/basic/transports#streamable-http) and provides improved flexibility and compatibility.

  Please note that Assistant MCP servers are in [early access](/release-notes/feature-availability) and are not intended for production usage.

  For more information, see [Use an Assistant MCP server](/guides/assistant/mcp-server).
</Update>

<Update label="2025-08-04" tags={["Docs"]}>
  ### VoltAgent integration

  Added the [VoltAgent](/integrations/voltagent) integration page.
</Update>


## July 2025

<Update label="2025-07-28" tags={["Database"]}>
  ### Increased context window for `pinecone-sparse-english-v0`

  You can now raise the context window for Pinecone's hosted [`pinecone-sparse-english-v0`](/guides/index-data/create-an-index#pinecone-sparse-english-v0) embedding model from `512` to `2048` using the `max_tokens_per_sequence` parameter.
</Update>

<Update label="2025-07-23" tags={["SDK"]}>
  ### Release Go SDK v4.1.0, v4.1.1, and v4.1.2

  Released [`v4.1.0`](https://github.com/pinecone-io/go-pinecone/releases/tag/v4.1.0), [`v4.1.1`](https://github.com/pinecone-io/go-pinecone/releases/tag/v4.1.1), and [`v4.1.2`](https://github.com/pinecone-io/go-pinecone/releases/tag/v4.1.2) of the [Pinecone Go SDK](/reference/go-sdk).

  * `v4.1.0` adds support for admin API operations for working with API keys, projects, and service accounts.
  * `v4.1.1` adds `PercentComplete` and `RecordsImported` to the response when [describing an import](/guides/index-data/import-data#track-import-progress) and [listing imports](/guides/index-data/import-data#list-imports).
  * `v4.1.2` adds support for [migrating a pod-based index to serverless](/guides/indexes/pods/migrate-a-pod-based-index-to-serverless#3-start-migration).
</Update>

<Update label="2025-07-23" tags={["SDK"]}>
  ### Release Node.js SDK v6.1.2

  Released [`v6.1.2`](https://github.com/pinecone-io/pinecone-ts-client/releases/tag/v6.1.2) of the [Pinecone Node.js SDK](/reference/node-sdk). This version adds support for the following:

  * [Migrating a pod-based index to serverless](/guides/indexes/pods/migrate-a-pod-based-index-to-serverless#3-start-migration).
  * Controlling whether `signed_url` is included in the response when [describing a file](/guides/assistant/manage-files#get-the-status-of-a-file) for an assistant.
</Update>


## June 2025

<Update label="2025-06-26" tags={["Assistant"]}>
  ### Unlimited assistant file storage for paid plans

  Organizations on the [Standard and Enterprise plans](https://www.pinecone.io/pricing/) now have [unlimited file storage](/reference/api/assistant/assistant-limits) for their assistants. Previously, organizations on these plans were limited to 10 GB of file storage per project.
</Update>

<Update label="2025-06-23" tags={["Database"]}>
  ### Data import from Google Cloud Storage

  You can now [import data](/guides/index-data/import-data) into an index from [Google Cloud Storage](/guides/operations/integrations/integrate-with-google-cloud-storage). This feature is in [public preview](/release-notes/feature-availability).
</Update>

<Update label="2025-06-20" tags={["SDK"]}>
  ### Released Python SDK v7.1.0, v7.2.0, and v7.3.0

  Released [`v7.1.0`](https://github.com/pinecone-io/pinecone-python-client/releases/tag/v7.1.0), [`v7.2.0`](https://github.com/pinecone-io/pinecone-python-client/releases/tag/v7.2.0), and [`v7.3.0`](https://github.com/pinecone-io/pinecone-python-client/releases/tag/v7.3.0) of the [Pinecone Python SDK](/reference/python-sdk).

  * `v7.1.0` fixes minor bugs.
  * `v7.2.0` adds support for [managing namespaces](/guides/manage-data/manage-namespaces).
  * `v7.3.0` adds support for admin API operations for working with API keys, projects, and service accounts.
</Update>

<Update label="2025-06-16" tags={["SDK"]}>
  ### Released Go SDK v4.0.0 and v4.0.1

  Released [`v4.0.0`](https://github.com/pinecone-io/go-pinecone/releases/tag/v4.0.0) and [`v4.0.1`](https://github.com/pinecone-io/go-pinecone/releases/tag/v4.0.1) of the [Pinecone Go SDK](/reference/go-sdk).

  Go SDK `v4.0.0` uses the latest stable API version, `2025-04`, and includes support for the following:

  * [Managing namespaces](/guides/manage-data/manage-namespaces)
  * [Reusing an index connection with a new namespace](/guides/manage-data/target-an-index#target-by-index-host-recommended) (see the Go example)
  * [Creating and managing backups](/guides/manage-data/back-up-an-index)
  * [Restoring indexes from backups](/guides/manage-data/restore-an-index)
  * [Listing embedding and reranking models hosted by Pinecone](/reference/api/2025-04/inference/list_models)
  * [Getting details about a model hosted by Pinecone](/reference/api/2025-04/inference/describe_model)

  Go SDK `v4.0.1` expands the [`DescribeIndex`](/guides/production/connect-to-aws-privatelink#read-and-write-data) response to include the `private_host` value for connecting to indexes with a private endpoint.
</Update>

<Update label="2025-06-16" tags={["SDK"]}>
  ### Released Node.js SDK v6.1.1

  Released [`v6.1.1`](https://github.com/pinecone-io/pinecone-ts-client/releases/tag/v6.1.1) of the [Pinecone Node.js SDK](/reference/node-sdk). This version adds support for [setting the sampling temperature](/guides/assistant/chat-with-assistant#set-the-sampling-temperature) for an assistant, and expands the [`describeIndex`](/guides/production/connect-to-aws-privatelink#read-and-write-data) response to include the `private_host` value for connecting to indexes with a private endpoint.
</Update>

<Update label="2025-06-12" tags={["Docs"]}>
  ### Data modeling guide

  Added a new guide to help you [model your data](/guides/index-data/data-modeling) for efficient ingestion, retrieval, and management in Pinecone.
</Update>

<Update label="2025-06-05" tags={["SDK"]}>
  ### Released Java SDK v5.1.0

  Released [`v5.1.0`](https://github.com/pinecone-io/pinecone-java-client/releases/tag/v5.1.0) of the [Pinecone Java SDK](/reference/java-sdk). This version adds support for [listing](/reference/api/2025-04/inference/list_models) and [describing](/reference/api/2025-04/inference/describe_model) embedding and reranking models hosted by Pinecone.
</Update>

<Update label="2025-06-05" tags={["SDK"]}>
  ### Released Node.js SDK v6.1.0

  Released [`v6.1.0`](https://github.com/pinecone-io/pinecone-ts-client/releases/tag/v6.1.0) of the [Pinecone Node.js SDK](/reference/node-sdk). This version adds support for [controlling the context snippets sent to the LLM](/guides/assistant/chat-with-assistant#control-the-context-snippets-sent-to-the-llm) by an assistant.
</Update>


## May 2025

<Update label="2025-05-29" tags={["SDK"]}>
  ### Released Python SDK v7.0.1 and v7.0.2

  Released [`v7.0.1`](https://github.com/pinecone-io/pinecone-python-client/releases/tag/v7.0.1) and [`v7.0.2`](https://github.com/pinecone-io/pinecone-python-client/releases/tag/v7.0.2) of the [Pinecone Python SDK](/reference/python-sdk). These versions fix minor bugs discovered since the release of the `v7.0.0` major version.
</Update>

<Update label="2025-05-29" tags={["SDK"]}>
  ### Released Node.s SDK v6.0.1

  Released [`v6.0.1`](https://github.com/pinecone-io/pinecone-ts-client/releases/tag/v6.0.1) of the [Pinecone Node.js SDK](/reference/node-sdk). This version adds pagination to the [`listBackups`](/guides/manage-data/back-up-an-index#list-backups-in-a-project) operation.
</Update>

<Update label="2025-05-19" tags={["API"]}>
  ### Pinecone API version `2025-04` is now the latest stable version

  `2025-04` is now the latest [stable version](/reference/api/versioning#release-schedule) of the [Pinecone APIs](/reference/api/introduction). For highlights, see the SDK releases below.
</Update>

<Update label="2025-05-19" tags={["SDK"]}>
  ### Released Python SDK v7.0.0

  Released [`v7.0.0`](https://github.com/pinecone-io/pinecone-python-client/releases/tag/v7.0.0) of the [Pinecone Python SDK](/reference/python-sdk). This version uses the latest stable API version, `2025-04`, and includes support for the following:

  * [Creating and managing backups](/guides/manage-data/back-up-an-index)
  * [Restoring indexes from backups](/guides/manage-data/restore-an-index)
  * [Listing embedding and reranking models hosted by Pinecone](/reference/api/2025-04/inference/list_models)
  * [Getting details about a model hosted by Pinecone](/reference/api/2025-04/inference/describe_model)
  * [Creating a BYOC index](/guides/production/bring-your-own-cloud#create-an-index)

  Additionally, the `pinecone-plugin-assistant` package required to work with [Pinecone Assistant](/guides/assistant/overview) is now included by default; it is no longer necessary to install the plugin separately.
</Update>

<Update label="2025-05-19" tags={["SDK"]}>
  ### Released Node.js SDK v6.0.0

  Released [`v6.0.0`](https://github.com/pinecone-io/pinecone-ts-client/releases/tag/v6.0.0) of the [Pinecone Node.js SDK](/reference/node-sdk). This version uses the latest stable API version, `2025-04`, and includes support for the following:

  * [Managing namespaces](/guides/manage-data/manage-namespaces)
  * [Creating and managing backups](/guides/manage-data/back-up-an-index)
  * [Restoring indexes from backups](/guides/manage-data/restore-an-index)
  * [Listing embedding and reranking models hosted by Pinecone](/reference/api/2025-04/inference/list_models)
  * [Getting details about a model hosted by Pinecone](/reference/api/2025-04/inference/describe_model)
</Update>

<Update label="2025-05-19" tags={["SDK"]}>
  ### Released Java SDK v5.0.0

  Released [`v5.0.0`](https://github.com/pinecone-io/pinecone-java-client/releases/tag/v5.0.0) of the [Pinecone Java SDK](/reference/java-sdk). This version uses the latest stable API version, `2025-04`, and includes support for the following:

  * [Creating indexes with integrated embedding and reranking](/guides/index-data/indexing-overview#integrated-embedding)
  * [Upserting text to an integrated index](/guides/index-data/upsert-data)
  * [Searching an integrated index with text](/guides/search/semantic-search#search-with-text)
  * [Managing namespaces](/guides/manage-data/manage-namespaces)
  * [Creating and managing backups](/guides/manage-data/back-up-an-index)
  * [Restoring indexes from backups](/guides/manage-data/restore-an-index)
</Update>

<Update label="2025-05-19" tags={["SDK"]}>
  ### Released .NET SDK v4.0.0

  Released [`v4.0.0`](https://github.com/pinecone-io/pinecone-dotnet-client/releases/tag/4.0.0) of the [Pinecone .NET SDK](/reference/dotnet-sdk). This version uses the latest stable API version, `2025-04`, and includes support for the following:

  * [Creating indexes with integrated embedding and reranking](/guides/index-data/indexing-overview#integrated-embedding)
  * [Upserting text to an integrated index](/guides/index-data/upsert-data)
  * [Searching an integrated index with text](/guides/search/semantic-search#search-with-text)
  * [Managing namespaces](/guides/manage-data/manage-namespaces)
  * [Creating and managing backups](/guides/manage-data/back-up-an-index)
  * [Restoring indexes from backups](/guides/manage-data/restore-an-index)
  * [Listing embedding and reranking models hosted by Pinecone](/reference/api/2025-04/inference/list_models)
  * [Getting details about a model hosted by Pinecone](/reference/api/2025-04/inference/describe_model)

  <Warning>
    Before upgrading to `v4.0.0`, update all relevant code to account for the following [breaking changes](/reference/api/versioning#breaking-changes). See the [`v4.0.0`](https://github.com/pinecone-io/pinecone-dotnet-client/releases/tag/4.0.0) release notes for full details.

    * The [`create_index`](/reference/api/2025-04/control-plane/create_index) and [`create_for_model`](/reference/api/2025-04/control-plane/create_for_model) operations:
      * `CreateIndexRequestMetric` has been renamed to `MetricType`.
    * The [`list_indexes`](/reference/api/2025-04/control-plane/list_indexes) operation:
      * `ModelIndexEmbedMetric` has been renamed to `MetricType`.
    * The [`embed`](/reference/api/2025-04/inference/generate-embeddings) operation:
      * `SparseEmbedding.SparseIndices` has changed from `IEnumerable<int>` to `IEnumerable<long>`.
  </Warning>
</Update>

<Update label="2025-05-06" tags={["Docs"]}>
  ### New Docs IA

  We've overhauled the information architecture of our guides to mirror the goals of users, from indexing to searching to optimizing to production.

  This change includes distinct pages for search types:

  * [Semantic search](https://docs.pinecone.io/guides/search/semantic-search)
  * [Lexical search](https://docs.pinecone.io/guides/search/lexical-search)
  * [Hybrid search](https://docs.pinecone.io/guides/search/hybrid-search)

  And optimization techniques:

  * [Increase relevance](https://docs.pinecone.io/guides/optimize/increase-relevance)
  * [Increase throughput](https://docs.pinecone.io/guides/optimize/increase-throughput)
  * [Decrease latency](https://docs.pinecone.io/guides/optimize/decrease-latency)
</Update>


## April 2025

<Update label="2025-04-25" tags={["Database"]}>
  ### Bring Your Own Cloud (BYOC) in GCP

  The [Bring Your Own Cloud (BYOC)](/guides/production/bring-your-own-cloud) offering is now available in GCP. Organizations with high security and compliance requirements can use BYOC to deploy Pinecone Database in their own GCP account. This feature is in [public preview](/release-notes/feature-availability).
</Update>

<Update label="2025-04-21" tags={["Database"]}>
  ### Integrate AI agents with Pinecone MCP

  [Pinecone's open-source MCP server](/guides/operations/mcp-server) enables AI agents to interact directly with Pinecone's functionality and documentation via the standardized [Model Context Protocol (MCP)](https://modelcontextprotocol.io/l). Using the MCP server, agents can search Pinecone documentation, manage indexes, upsert data, and query indexes for relevant information.
</Update>

<Update label="2025-04-21" tags={["Assistant"]}>
  ### Add context to AI agents with Assistant MCP

  Every Pinecone Assistant now has a [dedicated MCP server](/guides/assistant/mcp-server) that gives AI agents direct access to the assistant's knowledge through the standardized [Model Context Protocol (MCP)](https://modelcontextprotocol.io/).
</Update>

<Update label="2025-04-21" tags={["Assistant"]}>
  ### Upload a file from an in-memory binary stream

  You can [upload a file to an assistant directly from an in-memory binary stream](/guides/assistant/upload-files#upload-from-a-binary-stream) using the Python SDK and the BytesIO class.
</Update>

<Update label="2025-04-21" tags={["Database"]}>
  ### Released Pinecone Terraform Provider v1.0.0

  Released [v1.0.0](https://github.com/pinecone-io/terraform-provider-pinecone/releases/tag/v1.0.0) of the [Terraform Provider for Pinecone](/integrations/terraform). This version adds support for [sparse indexes](/guides/index-data/indexing-overview#sparse-indexes), [indexes with integrated embedding and reranking](/guides/index-data/indexing-overview#integrated-embedding), [index tags](/guides/manage-data/manage-indexes#configure-index-tags), and [index deletion protection](/guides/manage-data/manage-indexes#configure-deletion-protection).
</Update>

<Update label="2025-04-13" tags={["SDK"]}>
  ### Released .NET SDK v3.1.0

  Released [`v3.1.0`](https://github.com/pinecone-io/pinecone-dotnet-client/releases/tag/3.1.0) of the [Pinecone .NET SDK](/reference/dotnet-sdk). This version adds support for [indexes with integrated embedding and reranking](/guides/index-data/indexing-overview#integrated-embedding).
</Update>

<Update label="2025-04-04" tags={["Docs"]}>
  ### LLM shortcuts for Pinecone docs

  You can now use the "Copy page" options at the top of every page of the Pinecone documentation to quickly ground LLMs with Pinecone-specific context.
</Update>


## March 2025

<Update label="2025-03-26" tags={["Assistant"]}>
  ### Control the context snippets the assistant sends to the LLM

  You can [control the context snippets sent to the LLM](/guides/assistant/chat-with-assistant#control-the-context-snippets-sent-to-the-llm) by setting `context_options` in the request.
</Update>

<Update label="2025-03-24" tags={["SDK"]}>
  ### Released Go SDK v3.1.0

  Released [`v3.1.0`](https://github.com/pinecone-io/go-pinecone/releases/tag/v3.1.0) of the [Pinecone Go SDK](/reference/go-sdk). This version adds support for [indexes with integrated embedding and reranking](/guides/index-data/indexing-overview#integrated-embedding).
</Update>

<Update label="2025-03-21" tags={["General"]}>
  <img className="block max-w-full" noZoom src="https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/release-notes/launch-week-march-2025.png?fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=a5a2d145f08f688f6ae41242a0b5ff45" data-og-width="2400" width="2400" data-og-height="1260" height="1260" data-path="images/release-notes/launch-week-march-2025.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/release-notes/launch-week-march-2025.png?w=280&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=027b2cf2bccfc3cd36eb24b22a192199 280w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/release-notes/launch-week-march-2025.png?w=560&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=ddedc6d1859e46a1e5d46351b1d58331 560w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/release-notes/launch-week-march-2025.png?w=840&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=99024d848edae3477f5ce28037ea1d68 840w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/release-notes/launch-week-march-2025.png?w=1100&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=9b522179310daff93683d900a63b05ee 1100w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/release-notes/launch-week-march-2025.png?w=1650&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=b0331b0c5e94a1f07f2e1b8b7b7e9b03 1650w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/release-notes/launch-week-march-2025.png?w=2500&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=54db6d1b12f6b6dfc588d0491c72e484 2500w" />

  ### Launch week: Dark mode

  Dark mode is now out for Pinecone's website, docs, and console. You can change your theme at the top right of each site.
</Update>

<Update label="2025-03-20" tags={["General"]}>
  ### Launch week: Self-service audit logs

  You can now enable and [configure audit logs](/guides/production/configure-audit-logs) for your Pinecone organization. [Audit logs](/guides/production/security-overview#audit-logs) provide a detailed record of user, service account, and API actions that occur within Pinecone. This feature is in [public preview](/release-notes/feature-availability) and available only on [Enterprise plans](https://www.pinecone.io/pricing/).
</Update>

<Update label="2025-03-19" tags={["General"]}>
  ### Launch week: Introducing the Admin API and service accounts

  You can now use [service accounts](/guides/organizations/understanding-organizations#service-accounts) to programmatically manage your Pinecone organization through the Admin API. Use the Admin API to [create](/guides/projects/create-a-project) and [manage projects](/guides/projects/manage-projects), as well as [create and manage API keys](/guides/projects/manage-api-keys). The Admin API and service accounts are in [public preview](/release-notes/feature-availability).
</Update>

<Update label="2025-03-18" tags={["Database"]}>
  ### Launch week: Back up an index through the API

  You can now [back up an index](/guides/manage-data/back-up-an-index) and [restore an index](/guides/manage-data/restore-an-index) through the Pinecone API. This feature is in [public preview](/release-notes/feature-availability).
</Update>

<Update label="2025-03-17" tags={["Database"]}>
  ### Launch week: Optimized database architecture

  Pinecone has optimized its [serverless database architecture](/guides/get-started/database-architecture) to meet the growing demand for large-scale agentic workloads and improved performance for search and recommendation workloads. New customers will use this architecture by default, and existing customers will gain access over the next month.
</Update>

<Update label="2025-03-13" tags={["Docs"]}>
  ### Firebase Genkit integration

  Added the [Firebase Genkit](/integrations/genkit) integration page.
</Update>

<Update label="2025-03-10" tags={["Database"]}>
  ### Bring Your Own Cloud (BYOC) in public preview

  [Bring Your Own Cloud (BYOC)](/guides/production/bring-your-own-cloud) lets you deploy Pinecone Database in your private AWS account to ensure data sovereignty and compliance, with Pinecone handling provisioning, operations, and maintenance. This feature is in [public preview](/release-notes/feature-availability) on AWS.
</Update>


## February 2025

<Update label="2025-02-21" tags={["Docs"]}>
  ### Docs site refresh

  We've refreshed the look and layout of the [Pinecone documentation](https://docs.pinecone.io) site. You can now use the dropdown at the top of the side navigation to view documentation for either [Pinecone Database](/guides/get-started/overview) or [Pinecone Assistant](/guides/assistant/overview).
</Update>

<Update label="2025-02-18" tags={["Assistant"]}>
  ### Limit the number of chunks retrieved

  You can now limit the number of chunks the reranker sends to the LLM. To do this, set the `top_k` parameter (default is 15) when [retrieving context snippets](/guides/assistant/retrieve-context-snippets).
</Update>

<Update label="2025-02-21" tags={["Docs"]}>
  ### Assistant Quickstart colab notebook

  Added the [Assistant Quickstart colab notebook](https://colab.research.google.com/github/pinecone-io/examples/blob/master/docs/assistant-quickstart.ipynb). This notebook shows you how to set up and use [Pinecone Assistant](/guides/assistant/overview) in your browser.
</Update>

<Update label="2025-02-18" tags={["SDK"]}>
  ### Released Node.js SDK v5.0.0

  Released [`v5.0.0`](https://github.com/pinecone-io/pinecone-ts-client/releases/tag/v5.0.0) of the [Pinecone Node.js SDK](/reference/node-sdk). This version uses the latest stable API version, `2025-01`, and includes support for [Pinecone Assistant](/guides/assistant/overview) and [sparse-only indexes](/guides/index-data/indexing-overview#sparse-indexes).
</Update>

<Update label="2025-02-11" tags={["Docs"]}>
  ### New integrations

  Added the [Box](/integrations/box) and [Cloudera AI](/integrations/cloudera) integration pages.
</Update>

<Update label="2025-02-10" tags={["Assistant"]}>
  ### Citation highlights in assistant responses

  You can now include [highlights](/guides/assistant/chat-with-assistant#include-citation-highlights-in-the-response) in an assistant's citations. Highlights are the specific parts of the document that the assistant used to generate the response.

  Citation highlights are available in the Pinecone console or API versions `2025-04` and later.
</Update>

<Update label="2025-02-07" tags={["API"]}>
  ### Pinecone API version `2025-01` is now the latest stable version

  `2025-01` is now the latest [stable version](/reference/api/versioning#release-schedule) of the [Pinecone APIs](/reference/api/introduction).
</Update>

<Update label="2025-02-07" tags={["SDK"]}>
  ### Released Python SDK v6.0.0

  Released [`v6.0.0`](https://github.com/pinecone-io/pinecone-python-client/releases/tag/v6.0.0) of the [Pinecone Python SDK](/reference/python-sdk). This version uses the latest stable API version, `2025-01`, and includes support for the following:

  * [Index tags](/guides/manage-data/manage-indexes#configure-index-tags) to categorize and identify your indexes.
  * [Integrated inference](/reference/api/introduction#inference) without the need for extra plugins. If you were using the preview functionality of integrated inference, you must uninstall the `pinecone-plugin-records` package to use the `v6.0.0` release.
  * Enum objects to help with the discoverability of some configuration options, for example, `Metric`, `AwsRegion`, `GcpRegion`, `PodType`, `EmbedModel`, `RerankModel`. This is a backwards compatible change; you can still pass string values for affected fields.
  * New client variants, `PineconeAsyncio` and `IndexAsyncio`, which provide `async` methods for use with [asyncio](https://docs.python.org/3/library/asyncio.html). This makes it possible to use Pinecone with modern async web frameworks such as [FastAPI](https://fastapi.tiangolo.com/), [Quart](https://quart.palletsprojects.com/en/latest/), and [Sanic](https://sanic.dev/en/). Async support should significantly increase the efficiency of running many upserts in parallel.

  <Warning>
    Before upgrading to `v6.0.0`, update all relevant code to account for the following [breaking changes](/reference/api/versioning#breaking-changes). See the [`v6.0.0`](https://github.com/pinecone-io/pinecone-python-client/releases/tag/v6.0.0) release notes for full details.

    * Incorporated the `pinecone-plugin-records` and `pinecone-plugin-inference` plugins into the `pinecone` package. If you are using these plugins, you must unstall them to use `v6.0.0`.
    * Dropped support for Python 3.8, which has now reached official end of life, and added support for Python 3.13.
    * Removed the explicit dependency on `tqdm`, which is used to provide a progress bar when upserting data into Pinecone. If `tqdm` is available in the environment, the Pinecone SDK will detect and use it, but `tdqm` is no longer required to run the SDK. Popular notebook platforms such as [Jupyter](https://jupyter.org/) and [Google Colab](https://colab.google/) already include `tqdm` in the environment by default, but if you are running small scripts in other environments and want to continue seeing progress bars, you will need to separately install the `tqdm` package.
    * Removed some previously deprecated and rarely used keyword arguments (`config`, `openapi_config`, and `index_api`) to instead prefer dedicated keyword arguments for individual settings such as `api_key`, `proxy_url`, etc.
  </Warning>
</Update>

<Update label="2025-02-07" tags={["SDK"]}>
  ### Released Java SDK v4.0.0

  Released [`v4.0.0`](https://github.com/pinecone-io/pinecone-java-client/releases/tag/v4.0.0) of the [Pinecone Java SDK](/reference/java-sdk). This version uses the latest stable API version, `2025-01`, and adds support for [sparse-only indexes](/guides/index-data/indexing-overview#sparse-indexes).

  <Warning>
    Before upgrading to `v4.0.0`, update all relevant code to account for the following [breaking changes](/reference/api/versioning#breaking-changes). See the [`v4.0.0`](https://github.com/pinecone-io/pinecone-java-client/releases/tag/v4.0.0) release notes for full details.

    * [`embed` method](/reference/api/2025-01/inference/generate-embeddings):
      * `parameters` now accepts `Map<String, Object>` instead of `EmbedRequestParameters`.
      * The `Embeddings` response class now has dense and sparse embeddings. You now must use `getDenseEmbedding()` or `getSparseEmbedding()`. For example, instead of `embeddings.getData().get(0).getValues()`, you would use `embeddings.getData().get(0).getDenseEmbedding().getValues()`.

    * [`rerank` method](/guides/search/rerank-results):
      * `documents` now accepts `List<Map<String, Object>>` instead of `List<Map<String, String>>`.
      * `parameters` now accepts `Map<String, Object>` instead of `Map<String, String>`.
  </Warning>
</Update>

<Update label="2025-02-07" tags={["SDK"]}>
  ### Released Go SDK v3.0.0

  Released [`v3.0.0`](https://github.com/pinecone-io/go-pinecone/releases/tag/v3.0.0) of the [Pinecone Go SDK](/reference/go-sdk). This version uses the latest stable API version, `2025-01`, and adds support for [sparse-only indexes](/guides/index-data/indexing-overview#sparse-indexes).

  <Warning>
    Before upgrading to `v3.0.0`, update all relevant code to account for the following [breaking changes](/reference/api/versioning#breaking-changes). See the [`v3.0.0`](https://github.com/pinecone-io/go-pinecone/releases/tag/v3.0.0) release notes for full details.

    * [`embed` operation](/reference/api/2025-01/inference/generate-embeddings):
      * `EmbedParameters` is no longer typed as a pointer.
    * [`create_index` operation](/guides/index-data/create-an-index):
      * `CreateServerlessIndexRequest` and `CreatePodIndexRequest` structs have been updated, and fields are now classified as pointers to better denote optionality around creating specific types of indexes: `Metric`, `Dimension`, `VectorType`, and `DeletionProtection`.
    * Various data operation:
      * `Values` in the `Vector` type are now a pointer to allow flexibility when working with sparse-only indexes.
  </Warning>
</Update>

<Update label="2025-02-07" tags={["SDK"]}>
  ### Released .NET SDK v3.0.0

  Released [`v3.0.0`](https://github.com/pinecone-io/pinecone-dotnet-client/releases/tag/3.0.0) of the [Pinecone .NET SDK](/reference/dotnet-sdk). This version uses the latest stable API version, `2025-01`, and adds support for [sparse-only indexes](/guides/index-data/indexing-overview#sparse-indexes).

  <Warning>
    Before upgrading to `v3.0.0`, update all relevant code to account for the following [breaking changes](/reference/api/versioning#breaking-changes). See the [`v3.0.0`](https://github.com/pinecone-io/pinecone-dotnet-client/releases/tag/3.0.0) release notes for full details.

    * [`embed` operation](/reference/api/2025-01/inference/generate-embeddings):
      * The `Embedding` type has changed from a simple object to a discriminated union, supporting both `DenseEmbedding` and `SparseEmbedding`. New helper methods available on the Embedding type: `IsDense` and `IsSparse` for type checking, `AsDense()` and `AsSparse()` for type conversion, and `Match()` and `Visit()` for pattern matching.
      * The `Parameters` property now uses `Dictionary<string, object?>?` instead of `EmbedRequestParameters`.

    * `rerank` operation:
      * The `Document` property now uses `Dictionary<string, object?>?` instead of `Dictionary<string, string>?`.
      * The `Parameters` property now uses `Dictionary<string, object?>?` instead of `Dictionary<string, string>?`.
  </Warning>
</Update>


## January 2025

<Update label="2025-01-29" tags={["General"]}>
  ### Update to the API keys page

  Added the **Created by** column on the [API keys page](https://app.pinecone.io/organizations/-/projects/-/keys) in the Pinecone Console. This column shows the email of the user who created the API key.
</Update>

<Update label="2025-01-29" tags={["Database"]}>
  ### Sparse-only indexes in early access

  You can now use [sparse-only indexes](/guides/index-data/indexing-overview#sparse-indexes) for the storage and retrieval of sparse vectors. This feature is in [early access](/release-notes/feature-availability).
</Update>

<Update label="2025-01-22" tags={["Assistant"]}>
  <img className="block max-w-full" noZoom src="https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/release-notes/assistant-ga.png?fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=aa42277fa4b0cb3fafd1544c9b65ee24" data-og-width="1774" width="1774" data-og-height="994" height="994" data-path="images/release-notes/assistant-ga.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/release-notes/assistant-ga.png?w=280&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=62a2e6dcf304bc790c6d14098402592d 280w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/release-notes/assistant-ga.png?w=560&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=533b1a0ceed95b2f6def26f206cea23a 560w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/release-notes/assistant-ga.png?w=840&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=ad26bef0b1c7d1ed25535bb7d460883c 840w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/release-notes/assistant-ga.png?w=1100&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=0a04a321697583cf350ba392aad30858 1100w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/release-notes/assistant-ga.png?w=1650&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=e4ce39f7e891321f28f44b446e87c47c 1650w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/release-notes/assistant-ga.png?w=2500&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=325c235b9a924917cf64afc7c3330f9e 2500w" />

  Pinecone Assistant is generally available (GA) for all users.

  [Read more](https://www.pinecone.io/blog/pinecone-assistant-generally-available) about the release on our blog.
</Update>

<Update label="2025-01-09" tags={["SDK"]}>
  ### Released Node SDK v4.1.0

  Released [`v4.1.0`](https://github.com/pinecone-io/pinecone-ts-client/releases/tag/4.1.0) of the [Pinecone Node.js SDK](/reference/node-sdk). This version adds support for [index tags](/guides/manage-data/manage-indexes#configure-index-tags) when creating or configuring indexes. It also adds a new `RetryOnServerFailure` class that automatically retries asynchronous operations with exponential backoff when the server responds with a `500` or `503` [error](/reference/api/errors).
</Update>

<Update label="2025-01-09" tags={["General"]}>
  ### New Billing Admin user role

  Added the Billing Admin [user role](/guides/organizations/understanding-organizations#organization-roles). Billing Admins have permissions to view billing details, usage details, and support plans.
</Update>

<Update label="2025-01-07" tags={["SDK"]}>
  ### Released Go SDK v2.2.0

  Released [`v2.2.0`](https://github.com/pinecone-io/go-pinecone/releases/tag/v2.2.0) of the [Pinecone Go SDK](/reference/go-sdk). This version adds support for [index tags](/guides/manage-data/manage-indexes#configure-index-tags) when creating or configuring indexes.
</Update>



---
**Navigation:** [← Previous](./31-become-a-pinecone-partner.md) | [Index](./index.md) | [Next →](./33-feature-availability.md)
