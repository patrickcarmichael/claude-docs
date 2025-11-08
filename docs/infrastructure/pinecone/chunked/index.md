# Pinecone Documentation - Chunked Version

This documentation has been split into manageable chunks for easier navigation.

## Table of Contents

1. [Concepts](./01-concepts.md)
   - Concepts
   - Organization
   - Project
   - Index
   - Namespace
   - ... and 11 more sections
2. [Check data freshness](./02-check-data-freshness.md)
   - Check data freshness
   - Check the log sequence number
   - Verify record counts
   - Create an index
   - Create a dense index
   - ... and 25 more sections
3. [Delete all chunks for a document](./03-delete-all-chunks-for-a-document.md)
   - Delete all chunks for a document
   - To get the unique host for an index, 
   - see https://docs.pinecone.io/guides/manage-data/target-an-index
   - Step 1: Delete all existing chunks for the document
   - Step 2: Upsert the updated document chunks
   - ... and 21 more sections
4. [Indexing overview](./04-indexing-overview.md)
   - Indexing overview
   - Indexes
   - Namespaces
   - Vector embedding
   - Data ingestion
   - ... and 8 more sections
5. [This is gRPC client aliased as "Pinecone"](./05-this-is-grpc-client-aliased-as-pinecone.md)
   - This is gRPC client aliased as "Pinecone"
   - To get the unique host for an index, 
   - see https://docs.pinecone.io/guides/manage-data/target-an-index
   - Wait for and retrieve responses (in case of error)
   - Upsert limits
   - ... and 34 more sections
6. [Restore a pod-based index](./06-restore-a-pod-based-index.md)
   - Restore a pod-based index
   - Create a pod-based index from a collection
   - Scale pod-based indexes
   - Vertical vs. horizontal scaling
   - Vertical scaling
   - ... and 34 more sections
7. [Back up an index](./07-back-up-an-index.md)
   - Back up an index
   - Create a backup
   - Describe a backup
   - List backups for an index
   - List backups in a project
   - ... and 32 more sections
8. [Manage serverless indexes](./08-manage-serverless-indexes.md)
   - Manage serverless indexes
   - List indexes
   - Describe an index
   - Delete an index
   - Associate an embedding model
   - ... and 17 more sections
9. [Target an index](./09-target-an-index.md)
   - Target an index
   - Target by index host (recommended)
   - Target by index name
   - Update records
   - Update by ID
   - ... and 29 more sections
10. [Use the Pinecone MCP server](./10-use-the-pinecone-mcp-server.md)
   - Use the Pinecone MCP server
   - Tools
   - Before you begin
   - Configure Cursor
   - Configure Claude Desktop
   - ... and 49 more sections
11. [Understanding organizations](./11-understanding-organizations.md)
   - Understanding organizations
   - Projects in an organization
   - Billing settings
   - Organization roles
   - Organization single sign-on (SSO)
   - ... and 17 more sections
12. [Configure audit logs](./12-configure-audit-logs.md)
   - Configure audit logs
   - Enable audit logs
   - View audit logs
   - Edit audit log integration details
   - Disable audit logs
   - ... and 52 more sections
13. [Create a project](./13-create-a-project.md)
   - Create a project
   - Next steps
   - Manage API keys
   - Create an API key
   - View project API keys
   - ... and 31 more sections
14. [Lexical search](./14-lexical-search.md)
   - Lexical search
   - Search with text
   - Search with a sparse vector
   - Search with a record ID
   - Filter by required terms
   - ... and 4 more sections
15. [Search overview](./15-search-overview.md)
   - Search overview
   - Search types
   - Optimization
   - Limits
   - Cost
   - ... and 12 more sections
16. [Delete vectors](./16-delete-vectors.md)
   - Delete vectors
   - Delete a namespace
   - Get index stats
   - Describe a namespace
   - Fetch vectors
   - ... and 6 more sections
17. [Upsert text](./17-upsert-text.md)
   - Upsert text
   - Authentication
   - Get an API key
   - This API key has ReadWrite access to all indexes in your project.
   - Initialize a client
   - ... and 40 more sections
18. [AI Engine](./18-ai-engine.md)
   - AI Engine
   - Airbyte
   - Related articles
   - Amazon Bedrock
   - What are Agents for Amazon Bedrock?
   - ... and 61 more sections
19. [Datadog](./19-datadog.md)
   - Datadog
   - Setup guide
   - Datavolo
   - Estuary
   - Fleak
   - ... and 49 more sections
20. [Set environment variables for API keys](./20-set-environment-variables-for-api-keys.md)
   - Set environment variables for API keys
   - Related articles
   - Langtrace
   - LlamaIndex
   - Setup guide
   - ... and 84 more sections
21. [Integrations](./21-integrations.md)
22. [Pulumi](./22-pulumi.md)
   - Pulumi
   - Redpanda
   - Snowflake
   - Related articles
   - StreamNative
   - ... and 34 more sections
23. [load the documents and queries of legalbench consumer contracts qa dataset](./23-load-the-documents-and-queries-of-legalbench-consu.md)
   - load the documents and queries of legalbench consumer contracts qa dataset
   - initialize connection to pinecone (get API key at app.pinecone.io)
   - if the index does not exist, we create it
   - connect to index
   - create list of metadata dictionaries
   - ... and 26 more sections
24. [List collections](./24-list-collections.md)
   - List collections
   - List backups for an index
   - List backups for all indexes in a project
   - List restore jobs
   - Cancel an import
   - ... and 5 more sections
25. [List available models](./25-list-available-models.md)
   - List available models
   - Rerank documents
   - CLI authentication
   - Authenticating
   - Authenticate in a web browser
   - ... and 4 more sections
26. [Delete all locally tracked managed keys (CLI-created and user-created)](./26-delete-all-locally-tracked-managed-keys-cli-create.md)
   - Delete all locally tracked managed keys (CLI-created and user-created)
   - Delete only CLI-created managed keys
   - Delete only user-created managed keys
   - Local data storage
   - Check authentication status
   - ... and 67 more sections
27. [Install the latest version](./27-install-the-latest-version.md)
   - Install the latest version
   - Install the latest version with gRPC extras
   - Install the latest version with asyncio extras
   - Install a specific version
   - Install a specific version with gRPC extras
   - ... and 43 more sections
28. [Download a usage report](./28-download-a-usage-report.md)
   - Download a usage report
   - Manage API keys
   - Create an API key
   - View project API keys
   - View API key details
   - ... and 53 more sections
29. [Chat through the OpenAI-compatible interface](./29-chat-through-the-openai-compatible-interface.md)
   - Chat through the OpenAI-compatible interface
   - Chat with an assistant
   - Extract the response content
   - Choose a model
   - Filter chat with metadata
   - ... and 35 more sections
30. [Use an Assistant MCP server](./30-use-an-assistant-mcp-server.md)
   - Use an Assistant MCP server
   - Remote MCP server
   - Example code for integrating with LangChain
   - Local MCP server
   - Next Steps
   - ... and 26 more sections
31. [Become a Pinecone partner](./31-become-a-pinecone-partner.md)
   - Become a Pinecone partner
   - Additional information
   - Connect your users to Pinecone
   - Create an integration ID
   - Custom object
   - ... and 51 more sections
32. [2023 releases](./32-2023-releases.md)
   - 2023 releases
   - December 2023
   - November 2023
   - September 11, 2023
   - August 14, 2023
   - ... and 35 more sections
33. [Feature availability](./33-feature-availability.md)
   - Feature availability
   - Billing disputes and refunds
   - Contact Support
   - CORS Issues
   - Create and manage vectors with metadata
   - ... and 125 more sections
34. [2025 releases](./34-2025-releases.md)
   - 2025 releases
   - November 2025
   - October 2025
   - September 2025
   - August 2025
   - ... and 15 more sections


---

[← Back to Pinecone README](../README.md)
