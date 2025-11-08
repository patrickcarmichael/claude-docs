**Navigation:** [← Previous](./33-feature-availability.md) | [Index](./index.md) | Next →

# 2025 releases
Source: https://docs.pinecone.io/assistant-release-notes/2025




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



# Feature availability
Source: https://docs.pinecone.io/assistant-release-notes/feature-availability



This page defines the different availability phases of a feature in Pinecone.

The availability phases are used to communicate the maturity and stability of a feature. The availability phases are:

* **Early access**: In active development and may change at any time. Intended for user feedback only. In some cases, users must be granted explicit access to the API by Pinecone.

* **Public preview**: Unlikely to change between public preview and general availability. Not recommended for production usage. Available to all users.

* **Limited availability**: Available to select customers in a subset of regions and providers for production usage.

* **General availability**: Will not change on short notice. Recommended for production usage. Officially [supported by Pinecone](/troubleshooting/pinecone-support-slas) for non-production and production usage.

* **Deprecated**: Still supported, but no longer under active development, except for critical security fixes. Existing usage will continue to function, but migration following the upgrade guide is strongly recommended. Will be removed in the future at an announced date.

* **End of life (EOL)**: Removed, and no longer supported or available.

<Note>
  A feature is in **general availability** unless explicitly marked otherwise.
</Note>



# Assistant examples
Source: https://docs.pinecone.io/examples/assistant



export const Tag = ({text, icon}) => {
  return <span className="card-tag">
            {icon && <img src={icon} className={`w-4 h-4 object-contain ${icon.includes("openai") ? "dark-inverted" : ""}`} />}
            {text}
        </span>;
};

export const UtilityExampleCard = ({title, text, link}) => {
  return <a href={link} className="example-card group">
            <h2 className="font-bold" style={{
    fontSize: "0.875rem"
  }}>{title}</h2>
            <p style={{
    fontSize: "0.875rem",
    marginTop: "0"
  }}>{text}</p>
        </a>;
};

export const ExampleCard = ({title, text, link, children, arrow, vectors, namespaces}) => {
  return <a href={link} className="example-card group">
            <h2 className="font-semibold text-base">{title}</h2>
            <p>{text}</p>

            {children && <div className="tags">{children}</div>}

            {arrow && <svg xmlns="http://www.w3.org/2000/svg" className="arrow" width="24" height="24" viewBox="0 0 24 24" fill="none">
                <path d="M5.30739 20L4 18.6926L16.8249 5.8677H5.05837V4H20V18.9416H18.1323V7.1751L5.30739 20Z" fill="var(--text-secondary)" />
            </svg>}

            {(vectors || namespaces) && <div className="vectors">
                {vectors && <span>{vectors} vectors</span>}
                {namespaces && <span>{namespaces} namespaces</span>}
            </div>}
        </a>;
};

<div className="card-grid not-prose">
  <ExampleCard title="Quickstart" text="Get started with Pinecone Assistant" link="https://colab.research.google.com/github/pinecone-io/examples/blob/master/docs/assistant-quickstart.ipynb" arrow>
    <Tag text="Python" />
  </ExampleCard>

  <ExampleCard title="Retrieve context snippets" text="Retrieve relevant information snippets for your queries" link="https://colab.research.google.com/github/pinecone-io/examples/blob/master/docs/assistant-retrieve-context-snippets.ipynb" arrow>
    <Tag text="Python" />
  </ExampleCard>

  <ExampleCard title="Pinecone Assistant" text="Connect your existing Pinecone Assistant to a chat interface with citations and file references." link="/examples/sample-apps/pinecone-assistant">
    <Tag text="NextJS" icon="https://mintlify.s3-us-west-1.amazonaws.com/pinecone-2-sample-apps/images/examples/nextjs.svg" />
  </ExampleCard>
</div>



# Get an access token
Source: https://docs.pinecone.io/reference/api/2025-04/admin-assistant/get_token

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-04/oauth_2025-04.oas.yaml post /oauth/token
Obtain an access token for a service account using the OAuth2 client credentials flow. An access token is needed to authorize requests to the Pinecone Admin API.
The host domain for OAuth endpoints is `login.pinecone.io`.


<RequestExample>
  ```bash curl theme={null}
  PINECONE_CLIENT_ID="YOUR_CLIENT_ID"
  PINECONE_CLIENT_SECRET="YOUR_CLIENT_SECRET"

  # Note the base URL: login.pinecone.io
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
  ```json  theme={null}
  {
      "access_token":"YOUR_ACCESS_TOKEN",
      "expires_in":86400,
      "token_type":"Bearer"
  }
  ```
</ResponseExample>



# Pinecone Assistant architecture
Source: https://docs.pinecone.io/reference/architecture/assistant-architecture



This page describes the architecture for [Pinecone Assistant](/guides/assistant/overview).


## Overview

[Pinecone Assistant](/guides/assistant/overview) runs as a managed service on the Pinecone platform. It uses a combination of machine learning models and information retrieval techniques to provide responses that are informed by your documents. The assistant is designed to be easy to use, requiring minimal setup and no machine learning expertise.

Pinecone Assistant simplifies complex tasks like data chunking, vector search, embedding, and querying while ensuring privacy and security.

<img className="block max-w-full dark:hidden" noZoom src="https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/assistant-architecture_light.png?fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=fac1ffcff3fc58b8c48abb41070f76bd" data-og-width="1520" width="1520" data-og-height="1320" height="1320" data-path="images/assistant-architecture_light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/assistant-architecture_light.png?w=280&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=da402176da803658c8ffbdda0287e1d8 280w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/assistant-architecture_light.png?w=560&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=05a4da048111f0f38a919f39252e2cc1 560w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/assistant-architecture_light.png?w=840&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=47eb95307afaca43eea69a8914f52ec1 840w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/assistant-architecture_light.png?w=1100&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=96dfe1589dda495073c114a8fc01b9fd 1100w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/assistant-architecture_light.png?w=1650&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=1bc84f97b47498ae2ab7c6969c4ab37d 1650w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/assistant-architecture_light.png?w=2500&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=52df04932cfe358add8585cdbfcca0f4 2500w" />

<img className="hidden max-w-full dark:block" noZoom src="https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/assistant-architecture_dark.png?fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=52f8183973f02f2f1eb8f88d929035c8" data-og-width="1520" width="1520" data-og-height="1320" height="1320" data-path="images/assistant-architecture_dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/assistant-architecture_dark.png?w=280&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=6f77677652e9e12a46ad36facc47c8e4 280w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/assistant-architecture_dark.png?w=560&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=c51b5d995b5f8c5125a7f3f1bbd12995 560w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/assistant-architecture_dark.png?w=840&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=9d1740644d873ac940d8fb5340c9becb 840w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/assistant-architecture_dark.png?w=1100&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=cdfa4ba7f3ae803cdcdd807455cfb165 1100w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/assistant-architecture_dark.png?w=1650&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=c431d99fde890a6f016b06ae1a7f985f 1650w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/assistant-architecture_dark.png?w=2500&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=3c4cbac2096c93879d340740a731d119 2500w" />


## Data ingestion

When a [document is uploaded](/guides/assistant/manage-files), the assistant processes the content by chunking it into smaller parts and generating [vector embeddings](https://www.pinecone.io/learn/vector-embeddings-for-developers/) for each chunk. These embeddings are stored in an [index](/guides/index-data/indexing-overview), making them ready for retrieval.


## Data retrieval

During a [chat](/guides/assistant/chat-with-assistant), the assistant processes the message to formulate relevant search queries, which are used to query the index and identify the most relevant chunks from the uploaded content.


## Response generation

After retrieving these chunks, the assistant performs a ranking step to determine which information is most relevant. This [context](/guides/assistant/context-snippets-overview), along with the chat history and [assistant instructions](/guides/assistant/manage-assistants#add-instructions-to-an-assistant), is then used by a large language model (LLM) to generate responses that are informed by your documents.




---
**Navigation:** [← Previous](./33-feature-availability.md) | [Index](./index.md) | Next →
