**Navigation:** [← Previous](./09-target-an-index.md) | [Index](./index.md) | [Next →](./11-understanding-organizations.md)

# Use the Pinecone MCP server
Source: https://docs.pinecone.io/guides/operations/mcp-server

Use Pinecone MCP server for AI agent integration.

<Note>
  This feature is in [early access](/release-notes/feature-availability) and is not intended for production usage.
</Note>

The Pinecone MCP server enables AI agents to interact directly with Pinecone's functionality and documentation via the standardized [Model Context Protocol (MCP)](https://modelcontextprotocol.io/). Using the MCP server, agents can search Pinecone documentation, manage indexes, upsert data, and query indexes for relevant information.

This page shows you how to configure [Cursor](https://www.cursor.com/) and [Claude Desktop](https://claude.ai/download) to connect with the Pinecone MCP server.


## Tools

The Pinecone MCP server provides the following tools:

* `search-docs`: Search the official Pinecone documentation.
* `list-indexes`: Lists all Pinecone indexes.
* `describe-index`: Describes the configuration of an index.
* `describe-index-stats`: Provides statistics about the data in the index, including the  number of records and available namespaces.
* `create-index-for-model`: Creates a new index that uses an integrated inference model to embed text as vectors.
* `upsert-records`: Inserts or updates records in an index with integrated inference.
* `search-records`: Searches for records in an index based on a text query, using integrated inference for embedding. Has options for metadata filtering and reranking.
* `cascading-search`: Searches for records across multiple indexes, deduplicating and reranking the results.
* `rerank-documents`: Reranks a collection of records or text documents using a specialized reranking model.

<Note>
  The Pinecone MCP supports only [indexes with integrated embedding](/guides/index-data/indexing-overview#vector-embedding). Indexes for vectors you create with external embedding models are not supported.
</Note>


## Before you begin

Ensure you have the following:

* A [Pinecone API key](https://app.pinecone.io/organizations/-/keys)
* [Node.js](https://nodejs.org/en) installed, with `node` and `npx` available on your `PATH`


## Configure Cursor

<Steps>
  <Step title="Add the MCP server">
    In your project root, create a `.cursor/mcp.json` file, if it doesn't exist, and add the following configuration:

    ```json  theme={null}
    {
      "mcpServers": {
        "pinecone": {
          "command": "npx",
          "args": [
            "-y", "@pinecone-database/mcp"
          ],
          "env": {
            "PINECONE_API_KEY": "YOUR_API_KEY"
          }
        }
      }
    }
    ```

    Replace `YOUR_API_KEY` with your Pinecone API key.
  </Step>

  <Step title="Check the status">
    Go to **Cursor Settings > MCP**. You should see the server and its list of tools.
  </Step>

  <Step title="Add Pinecone rules">
    The Pinecone MCP server works well out-of-the-box. However, you can add explicit rules to ensure the server behaves as expected.

    In your project root, create a `.cursor/rules/pinecone.mdc` file and add the following:

    ```mdx [expandable] theme={null}
    ### Tool Usage for Code Generation

    - When generating code related to Pinecone, always use the `pinecone` MCP and the `search_docs` tool.

    - Perform at least two distinct searches per request using different, relevant questions to ensure comprehensive context is gathered before writing code.

    ### Error Handling

    - If an error occurs while executing Pinecone-related code, immediately invoke the `pinecone` MCP and the `search_docs` tool.

    - Search for guidance on the specific error encountered and incorporate any relevant findings into your resolution strategy.

    ### Syntax and Version Accuracy

    - Before writing any code, verify and use the correct syntax for the latest stable version of the Pinecone SDK.

    - Prefer official code snippets and examples from documentation over generated or assumed field values.

    - Do not fabricate field names, parameter values, or request formats.

    ### SDK Installation Best Practices

    - When providing installation instructions, always reference the current official package name.

    - For Pinecone, use `pip install pinecone` not deprecated packages like `pinecone-client`.
    ```
  </Step>

  <Step title="Test the server">
    Press `Command + i` to open the Agent chat. Test the Pinecone MCP server with prompts that required the server to generate Pinceone-compatible code and perform tasks in your Pinecone account.

    Generate code:

    > Write a Python script that creates a dense index with integrated embedding, upserts 20 sentences about dogs, waits 10 seconds, searches the index, and reranks the results.

    Perform tasks:

    > Create a dense index with integrated embedding, upsert 20 sentences about dogs, waits 10 seconds, search the index, and reranks the results.
  </Step>
</Steps>


## Configure Claude Desktop

<Steps>
  <Step title="Add the MCP server">
    Go to **Settings > Developer > Edit Config** and add the following configuration:

    ```json  theme={null}
    {
      "mcpServers": {
        "pinecone": {
          "command": "npx",
          "args": [
            "-y", "@pinecone-database/mcp"
          ],
          "env": {
            "PINECONE_API_KEY": "YOUR_API_KEY"
          }
        }
      }
    }
    ```

    Replace `YOUR_API_KEY` with your Pinecone API key.
  </Step>

  <Step title="Check the status">
    Restart Claude Desktop. On the new chat screen, you should see a hammer (MCP) icon appear with the new MCP tools available.
  </Step>

  <Step title="Test the server">
    Test the Pinecone MCP server with prompts that required the server to generate Pinceone-compatible code and perform tasks in your Pinecone account.

    Generate code:

    > Write a Python script that creates a dense index with integrated embedding, upserts 20 sentences about dogs, waits 10 seconds, searches the index, and reranks the results.

    Perform tasks:

    > Create a dense index with integrated embedding, upsert 20 sentences about dogs, waits 10 seconds, search the index, and reranks the results.
  </Step>
</Steps>


## Configure Claude Code

<Steps>
  <Step title="Add the MCP server">
    Run the following command to add the Pinecone MCP server to your Claude Code instance:

    ```bash  theme={null}
    claude mcp add-json pinecone-mcp \
      '{"type": "stdio",
        "command": "npx",
        "args": ["-y", "@pinecone-database/mcp"],
        "env": {"PINECONE_API_KEY": "YOUR_API_KEY"}}'
    ```

    Replace `YOUR_API_KEY` with your Pinecone API key.
  </Step>

  <Step title="Check the status">
    Restart Claude Code. Then, run the `/mcp` command to check the status of the Pinecone MCP. You should see the following:

    ```bash  theme={null}
      > /mcp 
        ⎿  MCP Server Status

          • pinecone-mcp: ✓ connected

    ```
  </Step>

  <Step title="Test the server">
    Test the Pinecone MCP server with prompts to Claude Code that require the server to generate Pinceone-compatible code and perform tasks in your Pinecone account.

    Generate code:

    > Write a Python script that creates a dense index with integrated embedding, upserts 20 sentences about dogs, waits 10 seconds, searches the index, and reranks the results.

    Perform tasks:

    > Create a dense index with integrated embedding, upsert 20 sentences about dogs, waits 10 seconds, search the index, and reranks the results.
  </Step>
</Steps>



# Decrease latency
Source: https://docs.pinecone.io/guides/optimize/decrease-latency

Learn techniques to decrease latency for search and upsert operations.


## Use namespaces

When you divide records into [namespaces](/guides/index-data/indexing-overview#namespaces) in a logical way, you speed up queries by ensuring only relevant records are scanned. The same applies to [fetching records](/guides/manage-data/fetch-data), [listing record IDs](/guides/manage-data/list-record-ids), and other data operations.


## Filter by metadata

In addition to increasing search accuracy and relevance, [searching with metadata filters](/guides/search/filter-by-metadata) can also help decrease latency by retrieving only records that match the filter.


## Target indexes by host

When you target an index by name for data operations such as `upsert` and `query`, the SDK gets the unique DNS host for the index using the `describe_index` operation. This is convenient for testing but should be avoided in production because `describe_index` uses a different API than data operations and therefore adds an additional network call and point of failure. Instead, you should get an index host once and cache it for reuse or specify the host directly.

You can get index hosts in the [Pinecone console](https://app.pinecone.io/organizations/-/projects/-/indexes) or using the [`describe_index`](/guides/manage-data/manage-indexes#describe-an-index) operation.

The following example shows how to target an index by host directly:

<Note>
  When using Private Endpoints for private connectivity between your application and Pinecone, you must target the index using the [Private Endpoint URL](/guides/production/connect-to-aws-privatelink#run-data-plane-commands) for the host.
</Note>

<CodeGroup>
  ```Python Python {5} theme={null}
  from pinecone.grpc import PineconeGRPC as Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  index = pc.Index(host="INDEX_HOST")
  ```

  ```javascript JavaScript {6} theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  // For the Node.js SDK, you must specify both the index host and name.
  const index = pc.index("INDEX_NAME", "INDEX_HOST");
  ```

  ```java Java {11} theme={null}
  import io.pinecone.clients.Index;
  import io.pinecone.configs.PineconeConfig;
  import io.pinecone.configs.PineconeConnection;

  public class TargetIndexByHostExample {
      public static void main(String[] args) {
          PineconeConfig config = new PineconeConfig("YOUR_API_KEY");
          config.setHost("INDEX_HOST");
          PineconeConnection connection = new PineconeConnection(config);
          // For the Java SDK, you must specify both the index host and name.
          Index index = new Index(connection, "INDEX_NAME");
      }
  }
  ```

  ```go Go {21} theme={null}
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

      idxConnection, err := pc.Index(pinecone.NewIndexConnParams{Host: "INDEX_HOST", Namespace: "example-namespace"})
      if err != nil {
          log.Fatalf("Failed to create IndexConnection for Host %v: %v", idx.Host, err)
      }
  }
  ```

  ```csharp C# {5} theme={null}
  using Pinecone;

  var pinecone = new PineconeClient("YOUR_API_KEY");

  var index = pinecone.Index(host: "INDEX_HOST");
  ```
</CodeGroup>


## Reuse connections

When you target an index for upserting or querying, the client establishes a TCP connection, which is a three-step process. To avoid going through this process on every request, and reduce average request latency, [cache and reuse the index connection object](/reference/api/authentication#initialize-a-client) whenever possible.


## Use a cloud environment

If you experience slow uploads or high query latencies, it might be because you are accessing Pinecone from your home network. To decrease latency, access Pinecone/deploy your application from a cloud environment instead, ideally from the same [cloud and region](/guides/index-data/create-an-index#cloud-regions) as your index.


## Work with database limits

Pinecone has [rate limits](/reference/api/database-limits#rate-limits) to protect your applications and maintain infrastructure health. Rate limits vary based on pricing plan and apply to serverless indexes only.

To handle rate limits effectively:

* [Implement retry logic with exponential backoff](/guides/production/error-handling#handle-rate-limits-429).
* If you need higher limits for your use case, [contact Support](https://app.pinecone.io/organizations/-/settings/support/ticket). Most limits can be adjusted to accommodate your scaling needs.



# Increase search relevance
Source: https://docs.pinecone.io/guides/optimize/increase-relevance

Learn techniques to improve search result quality.

This page describes helpful techniques for improving search accuracy and relevance.


## Rerank results

[Reranking](/guides/search/rerank-results) is used as part of a two-stage vector retrieval process to improve the quality of results. You first query an index for a given number of relevant results, and then you send the query and results to a reranking model. The reranking model scores the results based on their semantic relevance to the query and returns a new, more accurate ranking. This approach is one of the simplest methods for improving quality in retrieval augmented generation (RAG) pipelines.

Pinecone provides [hosted reranking models](/guides/search/rerank-results#reranking-models) so it's easy to manage two-stage vector retrieval on a single platform. You can use a hosted model to rerank results as an integrated part of a query, or you can use a hosted model to rerank results as a standalone operation.


## Filter by metadata

Every [record](/guides/get-started/concepts#record) in an index must contain an ID and a dense or sparse vector, depending on the [type of index](/guides/index-data/indexing-overview#indexes). In addition, you can include metadata key-value pairs to store related information or context. When you search the index, you can then include a metadata filter to limit the search to records matching a filter expression.

For example, if an index contains records about books, you could use a metadata field to associate each record with a genre, like `"genre": "fiction"` or `"genre": "poetry"`. When you query the index, you could then use a metadata filter to limit your search to records related to a specific genre.

For more details, see [Filter by metadata](/guides/search/filter-by-metadata).


## Use hybrid search

[Semantic search](/guides/search/semantic-search) and [lexical search](/guides/search/lexical-search) are powerful information retrieval techniques, but each has notable limitations. For example, semantic search can miss results based on exact keyword matches, especially in scenarios involving domain-specific terminology, while lexical search can miss results based on relationships, such as synonyms and paraphrases.

To lift these limitations, you can search both dense and sparse indexes, combine the results from both, and use one of Pinecone’s hosted reranking models to assign a unified relevance score, reorder the result accordingly, and return the most relevant matches. This is often called hybrid search or cascading retrieval.

For more details, see [Hybrid search](/guides/search/hybrid-search).


## Explore chunking strategies

You can chunk your content in different ways to get better results. Consider factors like the length of the content, the complexity of queries, and how results will be used in your application.

For more details, see [Chunking strategies](https://www.pinecone.io/learn/chunking-strategies/).



# Increase throughput
Source: https://docs.pinecone.io/guides/optimize/increase-throughput

Learn techniques to improve data operation performance and query throughput.


## Import from object storage

[Importing from object storage](/guides/index-data/import-data) is the most efficient and cost-effective method to load large numbers of records into an index. You store your data as Parquet files in object storage, integrate your object storage with Pinecone, and then start an asynchronous, long-running operation that imports and indexes your records.


## Upsert in batches

[Upserting in batches](/guides/index-data/upsert-data#upsert-in-batches) is another efficient way to ingest large numbers of records (up to 1000 per batch). Batch upserting is also a good option if you cannot work around bulk import's current [limitations](/guides/index-data/import-data#import-limits).


## Upsert/search in parallel

Pinecone is thread-safe, so you can send multiple [upsert](/guides/index-data/upsert-data#upsert-in-parallel) requests and multiple [query](/guides/search/semantic-search#parallel-queries) requests in parallel to help increase throughput.


## Python SDK options

### Use gRPC

Use the [Python SDK with gRPC extras](/reference/python-sdk) to run data operations such as upserts and queries over [gRPC](https://grpc.io/) rather than HTTP for a modest performance improvement.

### Upsert from a dataframe

To quickly ingest data when using the Python SDK, use the [`upsert_from_dataframe` method](/reference/python-sdk#upsert-from-a-dataframe). The method includes retry logic and `batch_size`, and is performant especially with Parquet file data sets.


## See also

Read more about [high-throughput optimizations](https://www.pinecone.io/blog/working-at-scale/) on our blog.



# Access your invoices
Source: https://docs.pinecone.io/guides/organizations/manage-billing/access-your-invoices

View and download organization billing invoices.

You can access your billing history and invoices in the Pinecone console:

1. Go to [**Settings > Billing > Overview**](https://app.pinecone.io/organizations/-/settings/billing).
2. Scroll down to the **Payment history and invoices** section.
3. For each billing period, you can download the invoice by clicking the **Download** button.

Each invoice includes line items for the services used during the billing period. If the total cost of that usage is below the monthly minimum, the invoice also includes a line item covering the rest of the minimum usage commitment.



# Change your payment method
Source: https://docs.pinecone.io/guides/organizations/manage-billing/change-payment-method

Update your billing payment method.

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



# Downgrade your plan
Source: https://docs.pinecone.io/guides/organizations/manage-billing/downgrade-billing-plan

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



# Download a usage report
Source: https://docs.pinecone.io/guides/organizations/manage-billing/download-usage-report

Download detailed usage and cost reports.

<Note>
  To view usage and costs across your Pinecone organization, you must be an [organization owner](/guides/organizations/understanding-organizations#organization-owners). Also, this feature is available only to organizations on the Standard or Enterprise plans.
</Note>

The **Usage** dashboard in the Pinecone console gives you a detailed report of usage and costs across your organization, broken down by each billable SKU or aggregated by project or service. You can view the report in the console or download it as a CSV file for more detailed analysis.

1. Go to [**Settings > Usage**](https://app.pinecone.io/organizations/-/settings/usage) in the Pinecone console.
2. Select the time range to report on. This defaults to the last 30 days.
3. Select the scope for your report:
   * **SKU:** The usage and cost for each billable SKU, for example, read units per cloud region, storage size per cloud region, or tokens per embedding model.
   * **Project:** The aggregated cost for each project in your organization.
   * **Service:** The aggregated cost for each service your organization uses, for example, database (includes serverless back up and restore), assistants, inference (embedding and reranking), and collections.
4. Choose the specific SKUs, projects, or services you want to report on. This defaults to all.
5. To download the report as a CSV file, click **Download**.

   <Tip>
     The CSV download provides more granular detail than the console view, including breakdowns by individual index as well as project and index tags.
   </Tip>

Dates are shown in UTC to match billing invoices. Cost data is delayed up to three days from the actual usage date.



# Standard trial
Source: https://docs.pinecone.io/guides/organizations/manage-billing/standard-trial

Get $300 credits for 21 days with the Standard plan trial.

The Standard trial lets you evaluate Pinecone without requiring any up-front payment. You get \$300 in credits over 21 days with access to Standard plan [features](https://www.pinecone.io/pricing/) and [limits](/reference/api/database-limits) that are suitable for testing Pinecone at scale.

<Note>
  If you're building a small or personal project, consider the free [Starter plan](https://www.pinecone.io/pricing/) instead.
</Note>


## Key features

* \$300 in credits
* 21 days of access to Standard plan [features](https://www.pinecone.io/pricing/), including:
  * [Bulk import](/guides/index-data/import-data)
  * [Backup and restore](/guides/manage-data/backups-overview)
  * [RBAC (role-based access control)](/guides/production/security-overview#role-based-access-control)
* [Higher limits](/reference/api/database-limits) for testing at scale
* Access to all [cloud regions](/guides/index-data/create-an-index#cloud-regions)
* Access to [Developer Support](https://www.pinecone.io/pricing/?plans=support\&scrollTo=product-pricing-modal-section)


## Expiration

At the end of the trial, or when you've used up all your credits, you can add a payment method and continue on with the Standard plan, or you can upgrade to an Enterprise plan. Learn more about [pricing](https://www.pinecone.io/pricing/).

Before your Standard trial expires, you can downgrade to a Starter plan. To do so, you must first bring your usage within Starter plan limits:

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

After your Standard trial expires, you can downgrade to a Starter plan **only if** your account is already within Starter plan limits (that is, if you already reduced your usage to within Starter plan limits **before** the trial expired). Otherwise, you'll need to upgrade your account to a paid plan, or let it get deleted.

If you have questions, [contact Support](https://www.pinecone.io/contact/support/).


## Limits

* Each organization is allowed only one trial.
* To activate a Standard plan trial, you must select the trial when registering your account on [https://pinecone.io](https://pinecone.io).
* You cannot activate a Standard trial in the following cases:
  * You already signed up for an account on [https://pinecone.io](https://pinecone.io), and you selected another type of plan (Starter, Standard, or Enterprise).
  * Before registering your account on [https://pinecone.io](https://pinecone.io), your organization subscribed through marketplace partners.

If you have any questions, [contact Support](https://www.pinecone.io/contact/support/).



# Upgrade your plan
Source: https://docs.pinecone.io/guides/organizations/manage-billing/upgrade-billing-plan

Upgrade to a paid plan to access advanced features and limits.

This page describes how to upgrade from the free Starter plan to the [Standard or Enterprise plan](https://www.pinecone.io/pricing/), paying either with a credit/debit card or through a supported cloud marketplace.

<Note>
  To change your plan, you must be an [organization owner or billing admin](/guides/organizations/understanding-organizations#organization-roles).
</Note>

<Tip>
  To commit to annual spending, [contact Pinecone](https://www.pinecone.io/contact).
</Tip>


## Pay with a credit/debit card

To upgrade your plan to Standard or Enterprise and pay with a credit/debit card, do the following:

1. In the Pinecone console, go to [Settings > Billing > Plans](https://app.pinecone.io/organizations/-/settings/billing/plans).
2. Click **Upgrade** in the **Standard** or **Enterprise** plan section.
3. Click **Credit / Debit card**.
4. Enter your credit card information.
5. Click **Upgrade**.

After upgrading, you will immediately start paying for usage of your Pinecone indexes, including the serverless indexes that were free on the Starter plan. For more details about how costs are calculated, see [Understanding cost](/guides/manage-cost/understanding-cost).


## Pay through the Google Cloud Marketplace

To upgrade your plan to Standard or Enterprise and pay through the Google Cloud Marketplace, do the following:

1. In the Pinecone console, go to [Settings > Billing > Plans](https://app.pinecone.io/organizations/-/settings/billing/plans).
2. Click **Upgrade** in the **Standard** or **Enterprise** plan section.
3. Click **Billing through GCP**. This takes you to the [Pinecone listing](https://console.cloud.google.com/marketplace/product/pinecone-public/pinecone) in the Google Cloud Marketplace.
4. Click **Subscribe**.
5. On the **Order Summary** page, select a billing account, accept the terms and conditions, and click **Subscribe**.

   <Note>The billing unit listed does not reflect the actual cost or metering of costs for Pinecone. See the [Pinecone Pricing page](https://www.pinecone.io/pricing/) for accurate details.</Note>
6. On the **Your order request has been sent to Pinecone** modal, click **Sign up with Pinecone**. This takes you to a Google-specific Pinecone login page.
7. Log in to your Pinecone account. Use the same authentication method as your existing Pinecone organization.
8. Select an organization from the list. You can only connect to organizations that are on the [Starter plan](https://www.pinecone.io/pricing/). Alternatively, you can opt to create a new organization.
9. Click **Connect to Pinecone** and follow the prompts.

Once your organization is connected and upgraded, you will receive a confirmation message. You will then immediately start paying for usage of your Pinecone indexes, including the serverless indexes that were free on the Starter plan. For more details about how costs are calculated, see [Understanding cost](/guides/manage-cost/understanding-cost).


## Pay through the AWS Marketplace

To upgrade your plan to Standard or Enterprise and pay through the AWS Marketplace, do the following:

1. In the Pinecone console, go to [Settings > Billing > Plans](https://app.pinecone.io/organizations/-/settings/billing/plans).
2. Click **Upgrade** in the **Standard** or **Enterprise** plan section.
3. Click **Billing through AWS**. This takes you to the [Pinecone listing](https://aws.amazon.com/marketplace/pp/prodview-xhgyscinlz4jk) in the AWS Marketplace.
4. Click **View purchase options**.
5. On the **Subscribe to Pinecone Vector Database** page, review the offer and then click **Subscribe**.

   <Note>The billing unit listed does not reflect the actual cost or metering of costs for Pinecone. See the [Pinecone Pricing page](https://www.pinecone.io/pricing/) for accurate details.</Note>
6. You'll see a message stating that your subscription is in process. Click **Set up your account**. This takes you to an AWS-specific Pinecone login page.

   <Warning>
     If the [Pinecone subscription page](https://aws.amazon.com/marketplace/saas/ordering?productId=738798c3-eeca-494a-a2a9-161bee9450b2) shows a message stating, “You are currently subscribed to this offer,” contact your team members to request an invitation to the existing AWS-linked organization. The **Set up your account** button is clickable, but Pinecone does not create a new AWS-linked organization.
   </Warning>
7. Log in to your Pinecone account. Use the same authentication method as your existing Pinecone organization.
8. Select an organization from the list. You can only connect to organizations that are on the [Starter plan](https://www.pinecone.io/pricing/). Alternatively, you can opt to create a new organization.
9. Click **Connect to Pinecone** and follow the prompts.

Once your organization is connected and upgraded, you will receive a confirmation message. You will then immediately start paying for usage of your Pinecone indexes, including the serverless indexes that were free on the Starter plan. For more details about how costs are calculated, see [Understanding cost](/guides/manage-cost/understanding-cost).


## Pay through the Microsoft Marketplace

To upgrade your plan to Standard or Enterprise and pay through the Microsoft Marketplace, do the following:

1. In the Pinecone console, go to [Settings > Billing > Plans](https://app.pinecone.io/organizations/-/settings/billing/plans).
2. Click **Upgrade** in the **Standard** or **Enterprise** plan section.
3. Click **Billing through Azure**. This takes you to the [Pinecone listing](https://marketplace.microsoft.com/product/saas/pineconesystemsinc1688761585469.pineconesaas) in the Microsoft Marketplace.
4. Click **Get it now**.
5. Select the **Pinecone - Pay As You Go** plan.
6. Click **Subscribe**.
7. On the **Subscribe to Pinecone** page, select the required details and click **Review + subscribe**.

   <Note>The billing unit listed does not reflect the actual cost or metering of costs for Pinecone. See the [Pinecone Pricing page](https://www.pinecone.io/pricing/) for accurate details.</Note>
8. Click **Subscribe**.
9. After the subscription is approved, click **Configure account now**. This redirects you to an Microsoft-specific Pinecone login page.
10. Log in to your Pinecone account. Use the same authentication method as your existing Pinecone organization.
11. Select an organization from the list. You can only connect to organizations that are on the [Starter plan](https://www.pinecone.io/pricing/). Alternatively, you can opt to create a new organization.
12. Click **Connect to Pinecone** and follow the prompts.

Once your organization is connected and upgraded, you will receive a confirmation message. You will then immediately start paying for usage of your Pinecone indexes, including the serverless indexes that were free on the Starter plan. For more details about how costs are calculated, see [Understanding cost](/guides/manage-cost/understanding-cost).



# Manage organization members
Source: https://docs.pinecone.io/guides/organizations/manage-organization-members

Add and manage organization members and roles.

This page shows how [organization owners](/guides/organizations/understanding-organizations#organization-roles) can add and manage organization members.

<Tip>
  For information about managing members at the **project-level**, see [Manage project members](/guides/projects/manage-project-members).
</Tip>


## Add a member to an organization

You can add members to your organization in the [Pinecone console](https://app.pinecone.io):

1. Go to [**Settings > Access > Members**](https://app.pinecone.io/organizations/-/settings/access/members).
2. In the **Invite by email** field, enter the member's email address.
3. Choose an [**Organization role**](/guides/organizations/understanding-organizations#organization-roles) for the member. The role determines the member's permissions within Pinecone.
4. Click **Invite**.

When you invite a member to join your organization, Pinecone sends them an email containing a link that enables them to gain access to the organization or project. If they already have a Pinecone account, they still receive an email, but they can also immediately view the project.


## Change a member's role

You can change a member's role in the [Pinecone console](https://app.pinecone.io):

1. Go to [**Settings > Access > Members**](https://app.pinecone.io/organizations/-/settings/access/members).
2. In the row of the member whose role you want to change, click **ellipsis (...) menu > Edit role**.
3. Select a [**Project role**](/guides/projects/understanding-projects#project-roles) for the member.
4. Click **Edit role**.


## Remove a member

You can remove a member from your organization in the [Pinecone console](https://app.pinecone.io):

1. Go to [**Settings > Access > Members**](https://app.pinecone.io/organizations/-/settings/access/members).
2. In the row of the member you want to remove, click **ellipsis (...) menu > Remove member**.
3. Click **Remove Member**.

<Note>
  To remove yourself from an organization, click the **Leave organization** button in your user's row and confirm.
</Note>



# Manage service accounts at the organization-level
Source: https://docs.pinecone.io/guides/organizations/manage-service-accounts

Create service accounts for organization-level API access.

<Note>
  This feature is in [public preview](/release-notes/feature-availability) and available only on [Enterprise plans](https://www.pinecone.io/pricing/).
</Note>

This page shows how [organization owners](/guides/organizations/understanding-organizations#organization-roles) can add and manage service accounts at the organization-level. Service accounts enable programmatic access to Pinecone's Admin API, which can be used to create and manage projects and API keys.

<Tip>
  Once a service account is added at the organization-level, it can be added to a project. For more information, see [Manage service accounts at the project-level](/guides/projects/manage-service-accounts).
</Tip>


## Create a service account

You can create a service account in the [Pinecone console](https://app.pinecone.io):

1. Go to [**Settings > Access > Service accounts**](https://app.pinecone.io/organizations/-/settings/access/service-accounts).

2. Enter a **Name** for the service account.

3. Choose an [**Organization Role**](/guides/organizations/understanding-organizations#organization-roles) for the service account. The role determines the service account's permissions within Pinecone.

4. Click **Create**.

5. Copy and save the **Client secret** in a secure place for future use. You will need the client secret to retrieve an access token.

   <Warning>
     You will not be able to see the client secret again after you close the dialog.
   </Warning>

6. Click **Close**.

Once you have created a service account, [add it to a project](/guides/projects/manage-service-accounts#add-a-service-account-to-a-project) to allow it access to the project's resources.


## Retrieve an access token

To access the Admin API, you must provide an access token to authenticate. Retrieve the access token using the client secret of a service account, which was [provided at time of creation](#create-a-service-account).

You can retrieve an access token for a service account from the `https://login.pinecone.io/oauth/token` endpoint, as shown in the following example:

```bash curl theme={null}
curl "https://login.pinecone.io/oauth/token" \ # Note: Base URL is login.pinecone.io
	-H "X-Pinecone-Api-Version: 2025-04" \
	-H "Content-Type: application/json" \
	-d '{
		"grant_type": "client_credentials",
		"client_id": "YOUR_CLIENT_ID",
		"client_secret": "YOUR_CLIENT_SECRET",
		"audience": "https://api.pinecone.io/"
	}'
```

The response will include an `access_token` field, which you can use to authenticate with the Admin API.

```
{
    "access_token":"YOUR_ACCESS_TOKEN",
    "expires_in":86400,
    "token_type":"Bearer"
}
```


## Change a service account's role

You can change a service account's role in the [Pinecone console](https://app.pinecone.io):

1. Go to [**Settings > Access > Service accounts**](https://app.pinecone.io/organizations/-/settings/service-accounts).
2. In the row of the service account you want to update, click **ellipsis (...) menu > Manage**.
3. Select an [**Organization role**](/guides/organizations/understanding-organizations#organization-roles) for the service account.
4. Click **Update**.


## Update service account name

You can change a service account's name in the [Pinecone console](https://app.pinecone.io):

1. Go to [**Settings > Access > Service accounts**](https://app.pinecone.io/organizations/-/settings/service-accounts).
2. In the row of the service account you want to update, click **ellipsis (...) menu > Manage**.
3. Enter a new **Service account name**.
4. Click **Update**.


## Rotate a service account's secret

You can rotate a service account's client secret in the [Pinecone console](https://app.pinecone.io):

1. Go to [**Settings > Access > Service accounts**](https://app.pinecone.io/organizations/-/settings/service-accounts).

2. In the row of the service account you want to update, click **ellipsis (...) menu > Rotate secret**.

3. **Enter the service account name** to confirm.

4. Click **Rotate client secret**.

5. Copy and save the **Client secret** in a secure place for future use.

   <Warning>
     You will not be able to see the client secret again after you close the dialog.
   </Warning>

6. Click **Close**.


## Delete a service account

Deleting a service account will remove it from all projects and will disrupt any applications using it to access Pinecone. You delete a service account in the [Pinecone console](https://app.pinecone.io):

1. Go to [**Settings > Access > Service accounts**](https://app.pinecone.io/organizations/-/settings/service-accounts).
2. In the row of the service account you want to update, click **ellipsis (...) menu > Delete**.
3. **Enter the service account name** to confirm.
4. Click **Delete service account**.



---
**Navigation:** [← Previous](./09-target-an-index.md) | [Index](./index.md) | [Next →](./11-understanding-organizations.md)
