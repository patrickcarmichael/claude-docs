**Navigation:** [← Previous](./29-chat-through-the-openai-compatible-interface.md) | [Index](./index.md) | [Next →](./31-become-a-pinecone-partner.md)

# Use an Assistant MCP server
Source: https://docs.pinecone.io/guides/assistant/mcp-server

Connect AI agents to Pinecone Assistant via Model Context Protocol.

<Note>
  This feature is in [early access](/release-notes/feature-availability) and is not intended for production usage.
</Note>

Every Pinecone Assistant has a dedicated MCP server that gives AI agents direct access to the assistant's knowledge through the standardized [Model Context Protocol (MCP)](https://modelcontextprotocol.io/). This page shows you how to connect an assistant's MCP server with Cursor, Claude Desktop, and LangChain.

There are two ways to connect to an assistant MCP server:

* [Remote MCP server](#remote-mcp-server) - Use a dedicated MCP endpoint to connect directly to an assistant.
* [Local MCP server](#local-mcp-server) - Run a Docker container locally that connects to an assistant

Both options support a context tool that allows agents to retrieve relevant context snippets from your assistant's knowledge. This is similar to the [context API](/guides/assistant/retrieve-context-snippets) but fine-tuned for MCP clients. Additional capabilities, such as file access, will be added in future releases.


## Remote MCP server

Every Pinecone Assistant has a dedicated MCP endpoint that you can connect directly to your AI applications. This option doesn't require running any infrastructure and is managed by Pinecone.

The MCP endpoint for an assistant is:

```
https://<YOUR_PINECONE_ASSISTANT_HOST>/mcp/assistants/<YOUR_ASSISTANT_NAME>
```

<Warning>
  The previous SSE-based endpoint (with `/sse` suffix) is deprecated and will stop working on August 31, 2025 at 11:59:59 PM UTC. Before then, update to the [streamable HTTP transport](https://modelcontextprotocol.io/specification/2025-03-26/basic/transports#streamable-http) MCP endpoint shown above, which implements the current MCP specification and provides improved flexibility and compatibility.
</Warning>

### Prerequisites

Before you begin, make sure you have the following values, which you'll use in the commands below:

* `<YOUR_PINECONE_API_KEY>`: [A Pinecone API key](/guides/projects/manage-api-keys).
* `<YOUR_PINECONE_ASSISTANT_HOST>`: In the Pinecone console, this is your assistant's **Host** value.
* `<YOUR_ASSISTANT_NAME>`: Your assistant's name, as displayed in the Pinecone console. For example, `example-assistant`.

### Use with Claude Code

You can use the Claude CLI to configure Claude Code to use your assistant's remote MCP server. For more information, see [Claude Code's MCP documentation](https://docs.anthropic.com/en/docs/claude-code/mcp).

1. Add the MCP server using the Claude CLI:

   ```bash  theme={null}
   claude mcp add --transport http my-assistant https://<YOUR_PINECONE_ASSISTANT_HOST>/mcp/assistants/<YOUR_ASSISTANT_NAME> --header "Authorization: Bearer <YOUR_PINECONE_API_KEY>"
   ```

   Replace `<YOUR_PINECONE_API_KEY>` with your Pinecone API key, `<YOUR_PINECONE_ASSISTANT_HOST>` with your Pinecone Assistant host, and `<YOUR_ASSISTANT_NAME>` with your assistant's name.

2. Verify the server was added successfully:

   ```bash  theme={null}
   claude mcp get my-assistant
   ```

3. The MCP server tools should now be available in Claude Code's chat interface.

### Use with Claude Desktop

You can configure Claude Desktop to use your assistant's remote MCP server. However, at this early stage of **remote** MCP server adoption, the Claude Desktop application does not support remote server URLs. In the example below, we work around this by using a local proxy server, [supergateway](https://github.com/supercorp-ai/supergateway), to forward requests to the remote MCP server with your API key.

<Warning>
  [supergateway](https://github.com/supercorp-ai/supergateway) is an open-source third-party tool. Use at your own risk.
</Warning>

1. Open [Claude Desktop](https://claude.ai/download) and go to **Settings**.

2. On the **Developer** tab, click **Edit Config** to open the configuration file.

3. Add the following configuration:

   ```json  theme={null}
   {
     "mcpServers": {
       "Assistant over supergateway": {
         "command": "npx",
         "args": [
           "-y",
           "supergateway",
           "--streamableHttp",
           "https://<YOUR_PINECONE_ASSISTANT_HOST>/mcp/assistants/<YOUR_ASSISTANT_NAME>",
           "--header",
           "Authorization: Bearer <YOUR_PINECONE_API_KEY>"
         ]
       }
     }
   }
   ```

   Replace `<YOUR_PINECONE_API_KEY>` with your Pinecone API key and `<YOUR_PINECONE_ASSISTANT_HOST>` with your Pinecone Assistant host.

4. Save the configuration file and restart Claude Desktop.

5. From the new chat screen, you should see a hammer (MCP) icon appear with the new MCP server available.

### Use with Cursor

You can configure Cursor to use your assistant's remote MCP server directly through the `.cursor/mcp.json` configuration file.

1. Open [Cursor](https://www.cursor.com/) and create a `.cursor` directory in your project root if it doesn't exist.

2. Open `.cursor/mcp.json` (create it if necessary). To learn more, refer to [Cursor's MCP documentation](https://docs.cursor.com/context/mcp).

3. Add the following configuration:

   ```json  theme={null}
   {
     "mcpServers": {
       "pinecone-assistant": {
         "url": "https://<YOUR_PINECONE_ASSISTANT_HOST>/mcp/assistants/<YOUR_ASSISTANT_NAME>",
         "headers": {
           "Authorization": "Bearer <YOUR_PINECONE_API_KEY>"
         }
       }
     }
   }
   ```

   Replace `<YOUR_PINECONE_API_KEY>` with your Pinecone API key, `<YOUR_PINECONE_ASSISTANT_HOST>` with your Pinecone Assistant host, and `<YOUR_ASSISTANT_NAME>` with your assistant's name.

4. Save the configuration file.

5. The MCP server tools should now be available in Cursor's chat interface.

### Use with LangChain

You can use the [LangChain MCP client](https://github.com/langchain-ai/langchain-mcp-adapters) to integrate with LangChain to create a powerful multi-agent workflow.

For example, the following code integrates Langchain with two assistants, one called `ai-news` and the other called `industry-reports`:

```python Python theme={null}

# Example code for integrating with LangChain
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent

from langchain_anthropic import ChatAnthropic

model = ChatAnthropic(model_name="claude-3-7-sonnet-latest", api_key=<YOUR_ANTHROPIC_API_KEY_HERE>)
pinecone_api_key = "<YOUR_PINECONE_API_KEY>"

async with MultiServerMCPClient(
    {
        "assistant_ai_news": {
            "url": "https://prod-1-data.ke.pinecone.io/mcp/assistants/ai-news",
            "transport": "streamable_http",
            "headers": {
                "Authorization": f"Bearer {pinecone_api_key}"
            }
        },
        "assistant_industry_reports": {
            "url": "https://prod-1-data.ke.pinecone.io/mcp/assistants/industry-reports",
            "transport": "streamable_http",
            "headers": {
                "Authorization": f"Bearer {pinecone_api_key}"
            }
        }
    }
) as client:
    agent = create_react_agent(model, client.get_tools())

    response = await agent.ainvoke({"messages": "Your task is research the next trends in AI, and form a report with the most undervalued companies in the space. You have access to two assistants, one that can help you find the latest trends in AI, and one that can help you find reports on companies."})
    print(response["messages"][-1].content)
```


## Local MCP server

Pinecone provides an open-source Pinecone Assistant MCP server that you can run locally with Docker. This option is useful for development, testing, or when you want to run the MCP server within your own infrastructure or expand the MCP server to include additional capabilities.

For the most up-to-date information on the local MCP server, see the [Pinecone Assistant MCP server repository](https://github.com/pinecone-io/assistant-mcp).

### Prerequisites

* Docker is installed and running on your system.
* A Pinecone API key. You can create a new key in the [Pinecone console](https://app.pinecone.io/organizations/-/keys).
* Your Pinecone Assistant host. To find it, go to your assistant in the [Pinecone console](https://app.pinecone.io/organizations/-/assistants). You'll see the assistant **Host** in the sidebar.

### Start the MCP server

Download the `assistant-mcp` Docker image:

```bash  theme={null}
docker pull ghcr.io/pinecone-io/assistant-mcp
```

Start the MCP server, providing your Pinecone API key and Pinecone Assistant host:

```bash  theme={null}
docker run -i --rm \
  -e PINECONE_API_KEY=<PINECONE_API_KEY> \
  -e PINECONE_ASSISTANT_HOST=<PINECONE_ASSISTANT_HOST> \
  pinecone/assistant-mcp
```

### Use with Claude Desktop

1. Open [Claude Desktop](https://claude.ai/download) and go to **Settings**.

2. On the **Developer** tab, click **Edit Config** to open the configuration file.

3. Add the following configuration:

   ```json  theme={null}
   {
     "mcpServers": {
       "pinecone-assistant": {
         "command": "docker",
         "args": [
           "run", 
           "-i", 
           "--rm", 
           "-e", 
           "PINECONE_API_KEY", 
           "-e", 
           "PINECONE_ASSISTANT_HOST", 
           "pinecone/assistant-mcp"
         ],
         "env": {
           "PINECONE_API_KEY": "<YOUR_PINECONE_API_KEY>",
           "PINECONE_ASSISTANT_HOST": "<YOUR_PINECONE_ASSISTANT_HOST>"
         }
       }
     }
   }
   ```

   Replace `<YOUR_PINECONE_API_KEY>` with your Pinecone API key and `<YOUR_PINECONE_ASSISTANT_HOST>` with your Pinecone Assistant host.

4. Save the configuration file and restart Claude Desktop.

5. From the new chat screen, you should see a hammer (MCP) icon appear with the new MCP server available.

### Use with Cursor

1. Open [Cursor](https://www.cursor.com/) and create a `.cursor` directory in your project root if it doesn't exist.

2. Open `.cursor/mcp.json` (create it if necessary). To learn more, refer to [Cursor's MCP documentation](https://docs.cursor.com/context/mcp).

3. Add the following configuration:

   ```json  theme={null}
   {
     "mcpServers": {
       "pinecone-assistant": {
         "command": "docker",
         "args": [
           "run", 
           "-i", 
           "--rm", 
           "-e", 
           "PINECONE_API_KEY", 
           "-e", 
           "PINECONE_ASSISTANT_HOST", 
           "pinecone/assistant-mcp"
         ],
         "env": {
           "PINECONE_API_KEY": "<YOUR_PINECONE_API_KEY>",
           "PINECONE_ASSISTANT_HOST": "<YOUR_PINECONE_ASSISTANT_HOST>"
         }
       }
     }
   }
   ```

   Replace `<YOUR_PINECONE_API_KEY>` with your Pinecone API key and `<YOUR_PINECONE_ASSISTANT_HOST>` with your Pinecone Assistant host.

4. Save the configuration file.


## Next Steps

* Visit the [Pinecone Assistant MCP Server repository](https://github.com/pinecone-io/assistant-mcp) for detailed installation and usage instructions

* Learn about [Model Context Protocol](https://modelcontextprotocol.io/) and how it enables AI agents to interact with tools and data

* Explore [retrieve context snippets](/guides/assistant/retrieve-context-snippets) to understand the underlying API functionality



# Multimodal context for assistants
Source: https://docs.pinecone.io/guides/assistant/multimodal

Process images and charts in PDFs with multimodal assistants.

<Note>
  This feature is in [public preview](/release-notes/feature-availability).
</Note>

Pinecone assistants support multimodal context, allowing them to understand and respond to questions about images embedded in PDF documents.

This enables use cases like:

* Analyzing charts, graphs, and diagrams in financial reports
* Understanding infographics and visual data in research papers
* Interpreting visual layouts in technical documentation

When working with multimodal PDFs, assistants attempt to filter out purely decorative images (such as example logos, background graphics, generic stock photos), so they can focus on images that contain meaningful information.

Additionally, assistants use Optical Character Recognition (OCR) to extract text from images. This allows them to read and analyze scanned PDFs (PDFs that contain images of text, but no actual embedded text).


## How it works

When you enable multimodal context for a PDF:

1. Pinecone extracts text and images (raster or vector) from the file and analyzes their contents. For each image, the assistant generates a descriptive caption and set of keywords. Additionally, when it makes sense, the assistant captures data points found in the image (for example, values from a table or chart).
2. During chat or context queries, the assistant searches for relevant text and image context it captured when analyzing the PDF. Image context can include the original image data (base64-encoded).
3. The assistant passes this context to the LLM, which uses it to generate responses.

<Note>
  For an overview of how Pinecone Assistant works, see [Pinecone Assistant architecture](/reference/architecture/assistant-architecture).
</Note>


## Try it out

The following steps demonstrate how to create an assistant, provide it with a PDF that contains images, and then query that assistant using chat and context APIs.

<Note>
  All versions of Pinecone's Assistant API allow you to upload multimodal PDFs.
</Note>

### 1. Create an assistant

First, if you don't have one, [create an assistant](/reference/api/2025-10/assistant/create_assistant):

<CodeGroup>
  ```Python Python theme={null}
  from pprint import pprint
  from pinecone import Pinecone

  pc = Pinecone("YOUR_API_KEY") 
  assistant = pc.assistant.create_assistant(
      assistant_name="example-assistant-multimodal", 
      instructions="You are a helpful assistant that can understand both text and images in documents.",
      region="us",
      timeout=30
  )

  print(f"Type: {type(assistant).__name__}")
  pprint(assistant)
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl "https://api.pinecone.io/assistant/assistants" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
          "name": "example-assistant-multimodal",
          "instructions": "You are a helpful assistant that can understand both text and images in documents.",
          "region": "us"
        }'
  ```
</CodeGroup>

Response:

<CodeGroup>
  ```shell Python theme={null}
  Type: AssistantModel
  {'created_at': '2025-08-28T23:35:26.917953498Z',
    'host': 'https://prod-1-data.ke.pinecone.io',
    'instructions': 'You are a helpful assistant that can understand both text '
                    'and images in documents.',
    'metadata': {},
    'name': 'example-assistant-multimodal',
    'status': 'Ready',
    'updated_at': '2025-08-28T23:35:28.507639215Z'}
  ```

  ```json curl theme={null}
  {
    "name": "example-assistant-multimodal",
    "instructions": "You are a helpful assistant that can understand both text and images in documents.",
    "metadata": null,
    "status": "Initializing",
    "host": "https://prod-1-data.ke.pinecone.io",
    "created_at": "2025-08-18T23:18:52.858197495Z",
    "updated_at": "2025-08-18T23:18:52.858198077Z"
  }
  ```
</CodeGroup>

<Note>
  You don't need to create a new assistant to use multimodal context. Existing assistants can enable multimodal context for newly uploaded PDFs, as described in [the next section](#2-upload-a-multimodal-pdf).
</Note>

### 2. Upload a multimodal PDF

To enable multimodal context for a PDF, when [uploading the file](/reference/api/2025-10/assistant/upload_file), set the `multimodal` URL parameter to true (defaults to false).

<CodeGroup>
  ```Python Python theme={null}
  from pprint import pprint
  from pinecone import Pinecone

  pc = Pinecone("YOUR_API_KEY") 
  assistant = pc.assistant.Assistant(assistant_name="example-assistant-multimodal")

  # timeout=None allows the SDK to wait for file processing to complete before returning.
  # This parameter is only available in the SDK, not in direct API calls.
  file_model = assistant.upload_file(
      file_path="./document.pdf",
      multimodal=True,
      timeout=None
  )

  pprint(file_model)
  ```

  ```bash curl theme={null}
  ASSISTANT_HOST="YOUR_ASSISTANT_HOST"
  ASSISTANT_NAME="example-assistant-multimodal"
  PINECONE_API_KEY="YOUR_API_KEY"
  LOCAL_FILE_PATH="/path/to/your/document.pdf"

  curl -X POST "https://$ASSISTANT_HOST/assistant/files/$ASSISTANT_NAME?multimodal=true" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -F "file=@$LOCAL_FILE_PATH"
  ```
</CodeGroup>

Response:

<CodeGroup>
  ```shell Python theme={null}
  # Formatted for readability
  FileModel(
    name='document.pdf', 
    id='9c322597-58d6-4ebc-84b5-a398b620da01', 
    metadata=None, 
    created_on='2025-08-28T23:41:41.982805815Z', 
    updated_on='2025-08-28T23:42:09.562949544Z', 
    status='Available', 
    percent_done=1.0, 
    signed_url=None, 
    error_message=None, 
    size=1236044.0, 
    multimodal=True
  )
  ```

  ```json curl theme={null}
  {
    "status": "Processing",
    "id": "a89f678c-9ceb-40ec-8fc7-23913e560b37",
    "name": "document.pdf",
    "size": 1236044,
    "metadata": null,
    "multimodal": true,
    "updated_on": "2025-08-18T23:21:36.516310298Z",
    "created_on": "2025-08-18T23:21:36.516310771Z",
    "percent_done": 0.0,
    "signed_url": null,
    "error_message": null
  }
  ```
</CodeGroup>

<Note>
  * The `multimodal` parameter is only available for PDF files.
  * To check the status of a file, use the [describe a file upload](/reference/api/2025-10/assistant/describe_file) endpoint.
</Note>

### 3. Chat with the assistant

Now, [chat with your assistant](/reference/api/2025-10/assistant/chat_assistant). To tell the assistant to provide image-related context to the LLM:

* Set the `multimodal` request parameter to true (default) in the `context_options` object. Setting `multimodal` to false means the LLM only receives text snippets.
* When `multimodal` is true, use `include_binary_content` to specify what image context the LLM should receive: base64 image data and captions (true) or captions only (false).

<Note>
  Sending image-related context to the LLM (whether captions, base64 data, or both) increases token usage. Learn about [monitoring spend and usage](/guides/assistant/admin/monitor-spend-and-usage).
</Note>

<CodeGroup>
  ```Python Python theme={null}
  from pprint import pprint
  from pinecone import Pinecone
  from pinecone_plugins.assistant.models.chat import Message

  pc = Pinecone("YOUR_API_KEY") 
  assistant = pc.assistant.Assistant(assistant_name="example-assistant-multimodal")

  msg = Message(
      role="user", 
      content="Describe the symbol on the paper tray that indicates the maximum fill level."
  )

  chat_response = assistant.chat(
    messages=[msg],
    context_options={
        "multimodal": True,
        "include_binary_content": True,
        "top_k": 10,
        "snippet_size": 2048
    }
  )

  pprint(chat_response)
  ```

  ```bash curl theme={null}
  ASSISTANT_HOST="YOUR_ASSISTANT_HOST"
  ASSISTANT_NAME="example-assistant-multimodal"
  PINECONE_API_KEY="YOUR_API_KEY"

  curl "https://$ASSISTANT_HOST/assistant/chat/$ASSISTANT_NAME" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
          "messages": [
            {
              "role": "user",
              "content": "Describe the symbol on the paper tray that indicates the maximum fill level."
            }
          ],
          "context_options": {
            "multimodal": true,
            "include_binary_content": true,
            "top_k": 10,
            "snippet_size": 2048
          }
        }'
  ```
</CodeGroup>

Response:

<CodeGroup>
  ```shell Python theme={null}
  # Formatted for readability
  ChatResponse(
    id='00000000000000000fe49626f3ee5164', 
    model='gpt-4o-2024-11-20', 
    usage=Usage(
      prompt_tokens=8703, 
      completion_tokens=41, 
      total_tokens=8744
    ), 
    message=Message(
      content='The symbol on the paper tray that indicates...', 
      role='assistant'
    ), 
    finish_reason='stop', 
    citations=[
      Citation(
        position=209, 
        references=[
          Reference(
              file=FileModel(
                name='document.pdf', 
                id='9c322597-58d6-4ebc-84b5-a398b620da01', 
                metadata=None, 
                created_on='2025-08-28T23:41:41.982805815Z', 
                updated_on='2025-08-28T23:42:09.562949544Z', 
                status='Available', 
                percent_done=1.0, 
                signed_url='https://storage.googleapis.com/...', 
                error_message=None, 
                size=1236044.0, 
                multimodal=True
            ), 
            pages=[3, 4, 5, 6, 7, 8, 9, 10, 11], 
            highlight=None
          )
        ]
      )
    ]
  )
  ```

  ```json curl theme={null}
  {
    "finish_reason": "stop",
    "message": {
      "role": "assistant",
      "content": "The symbol on the paper tray that indicates..."
    },
    "id": "0000000000000000d904dfd3dd4f4597"
    "model": "gpt-4o-2024-11-20",
    "usage": {
      "prompt_tokens": 8414,
      "completion_tokens": 42,
      "total_tokens": 8456
    },
    "citations": [
      {
        "position": 213,
        "references": [
          {
            "file": {
              "status": "Available",
              "id": "a89f678c-9ceb-40ec-8fc7-23913e560b37",
              "name": "document.pdf",
              "size": 1236044,
              "metadata": null,
              "multimodal": true,
              "updated_on": "2025-08-18T23:21:59.697988967Z",
              "created_on": "2025-08-18T23:21:36.498381046Z",
              "percent_done": 1.0,
              "signed_url": "https://storage.googleapis.com/...",
              "error_message": null
            },
            "pages": [ 3, 4, 5, 6, 7, 8, 9, 10, 11 ],
            "highlight": null
          }
        ]
      }
    ]
  }
  ```
</CodeGroup>

<Warning>
  If your assistant uses multimodal context snippets to generate a response, no [highlights](/guides/assistant/chat-with-assistant#include-citation-highlights-in-the-response) are returned—even when `include_highlights` is true.
</Warning>

### 4. Query for context

To query context for a custom RAG workflow, you can [retrieve context snippets](/reference/api/2025-10/assistant/context_assistant) directly. Then, you can pass these snippets to an LLM as context.

To fetch image-related context snippets (as well as text snippets), set the `multimodal` request parameter to true (default). When `multimodal` is true, use `include_binary_content` to specify what image context you'd like to receive: base64 image data and captions (true) or captions only (false).

<CodeGroup>
  ```Python Python theme={null}
  from pprint import pprint
  from pinecone import Pinecone

  pc = Pinecone("PINECONE_API_KEY") 
  assistant = pc.assistant.Assistant(assistant_name="example-assistant-multimodal")
  context_response = assistant.context(
      query="Describe the symbol on the paper tray that indicates the maximum fill level.",
      multimodal=True,
      include_binary_content=True
  )

  pprint(context_response)
  ```

  ```bash curl theme={null}
  ASSISTANT_HOST="YOUR_ASSISTANT_HOST"
  ASSISTANT_NAME="example-assistant-multimodal"
  PINECONE_API_KEY="YOUR_API_KEY"

  curl "https://$ASSISTANT_HOST/assistant/chat/$ASSISTANT_NAME/context" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "accept: application/json" \
    -H "Content-Type: application/json" \
    -d '{
      "query": "Describe the symbol on the paper tray that indicates the maximum fill level.",
      "multimodal": true,
      "include_binary_content": true
    }'
  ```
</CodeGroup>

<Note>
  If you set `multimodal` to true and `include_binary_content` to false, image objects are not returned in the snippets. If you set `multimodal` to false, only text snippets are returned.
</Note>

Response:

<CodeGroup>
  ```shell Python theme={null}
  # Formatted for readability
  ContextResponse(
    id='00000000000000001e3ef84bd493e612', 
    snippets=[
      MultimodalSnippet(
        type='multimodal', 
        content=[
          TextBlock(type='text', text="..."), 
          ImageBlock(
            type='image', 
            caption='...', 
            image=Image(mime_type='image/jpeg', data='...', type='base64')), 
          // ...
        ], 
        score=0.16321887, 
        reference=PdfReference(
          type='pdf', 
          pages=[3, 4, 5, 6, 7, 8, 9, 10, 11], 
          file=FileModel(
            name='document.pdf', 
            id='9c322597-58d6-4ebc-84b5-a398b620da01', 
            metadata=None, 
            created_on='2025-08-28T23:41:41.982805815Z', 
            updated_on='2025-08-28T23:42:09.562949544Z', 
            status='Available', 
            percent_done=1.0, 
            signed_url='https://storage.googleapis.com/...', 
            error_message=None, 
            size=1236044, 
            multimodal=True
          )
        )
      ), 
      // ...
    ], 
    usage=TokenCounts(
      prompt_tokens=7061, 
      completion_tokens=0, 
      total_tokens=7061
    )
  )
  ```

  ```json curl theme={null}
  {
    "snippets": [
      {
        "type": "multimodal",
        "content": [
          {
            "type": "text",
            "text": "# The Online User's Guide..."
          },
          {
            "type": "image",
            "caption": "An image of a control panel...",
            "image": {
              "type": "base64",
              "mime_type": "image/jpeg",
              "data": "..."
            }
          },
          // ...
        ],
        "score": 0.16775002,
        "reference": {
          "type": "pdf",
          "file": {
            "status": "Available",
            "id": "a89f678c-9ceb-40ec-8fc7-23913e560b37",
            "name": "document.pdf",
            "size": 1236044,
            "metadata": null,
            "multimodal": true,
            "updated_on": "2025-08-18T23:21:59.697988967Z",
            "created_on": "2025-08-18T23:21:36.498381046Z",
            "percent_done": 1.0,
            "signed_url": "https://storage.googleapis.com/...",
            "error_message": null
          },
          "pages": [ 3, 4, 5, 6, 7, 8, 9, 10, 11 ]
        }
      },
      // ...
    ],
    "usage": {
      "prompt_tokens": 6778,
      "completion_tokens": 0,
      "total_tokens": 6778
    },
    "id": "000000000000000005b9cd91b1c5446d"
  } 
  ```
</CodeGroup>

<Note>
  Snippets are returned based on their semantic relevance to the provided query. When you set `multimodal` to true, you'll receive the most relevant snippets, regardless of the types of content they contain. You can receive text snippets, multimodal snippets, or both.
</Note>


## Limits

Multimodal context for assistants is only available for PDF files. Additionally, the following limits apply:

| Metric                        | Starter plan | Standard plan | Enterprise plan |
| :---------------------------- | :----------- | :------------ | :-------------- |
| Max file size                 | 10 MB        | 50 MB         | 50 MB           |
| Page limit                    | 100          | 100           | 100             |
| Multimodal PDFs per assistant | 1            | 20            | 20              |

To learn about other assistant-related limits, see [Pinecone Assistant limits](/guides/assistant/pricing-and-limits).



# Pinecone Assistant
Source: https://docs.pinecone.io/guides/assistant/overview

Pinecone Assistant is a service that allow you to build production-grade chat and agent-based applications quickly.

<CardGroup cols={2}>
  <Card title="Assistant quickstart" icon="comments" href="/guides/assistant/quickstart">
    Create an AI assistant that answers complex questions about your proprietary data
  </Card>

  <Card title="Database quickstart" icon="database" href="/guides/get-started/quickstart">
    Set up a fully managed vector database for high-performance semantic search
  </Card>
</CardGroup>


## Use cases

Pinecone Assistant is useful for a variety of tasks, especially for the following:

* Prototyping and deploying an AI assistant quickly.
* Providing context-aware answers about your proprietary data without training an LLM.
* Retrieving answers grounded in your data, with references.


## SDK support

You can use the [Assistant API](/reference/api/latest/assistant/) directly, through the [Pinecone Python SDK](/reference/python-sdk), or through the [Pinecone Node.js SDK](/reference/node-sdk).


## Workflow

You can use the Pinecone Assistant through the [Pinecone console](https://app.pinecone.io/organizations/-/projects/-/assistant) or [Pinecone API](/reference/api/latest/assistant/list_assistants).

<Tabs>
  <Tab title="Overview">
    The following steps outline the general Pinecone Assistant workflow:

    <Steps>
      <Step title="Create an assistant">
        [Create an assistant](/guides/assistant/create-assistant) to answer questions about your documents.
      </Step>

      <Step title="Upload documents">
        [Upload documents](/guides/assistant/upload-files) to your assistant. Your assistant manages chunking, embedding, and storage for you.
      </Step>

      <Step title="Chat with an assistant">
        [Chat with your assistant](/guides/assistant/chat-with-assistant) and receive responses as a JSON object or as a text stream. For each chat, your assistant queries a large language model (LLM) with context from your documents to ensure the LLM provides grounded responses.
      </Step>

      <Step title="Evaluate answers">
        [Evaluate the assistant's responses](/guides/assistant/evaluation-overview) for correctness and completeness.
      </Step>

      <Step title="Optimize performance">
        [Use custom instructions](https://www.pinecone.io/learn/assistant-api-deep-dive/#Custom-Instructions) to tailor your assistant's behavior and responses to specific use cases or requirements. [Filter by metadata associated with files](https://www.pinecone.io/learn/assistant-api-deep-dive/#Using-Metadata) to reduce latency and improve the accuracy of responses.
      </Step>

      <Step title="Retrieve context snippets">
        [Retrieve context snippets](/guides/assistant/retrieve-context-snippets) to understand what relevant data snippets Pinecone Assistant is using to generate responses. You can use the retrieved snippets with your own LLM, RAG application, or agentic workflow.
      </Step>
    </Steps>

    <Note>
      For information on how the Pinecone Assistant works, see [Assistant architecture](/reference/architecture/assistant-architecture).
    </Note>
  </Tab>

  <Tab title="Code sample">
    The following code samples outline the Pinecone Assistant workflow using either the [Pinecone Python SDK](/reference/python-sdk) and [Pinecone Assistant plugin](/reference/python-sdk#install-the-pinecone-assistant-python-plugin) or the [Pinecone Node.js SDK](/reference/node-sdk).

    <CodeGroup>
      ```python Python theme={null}
      # pip install pinecone
      # pip install pinecone-plugin-assistant

      from pinecone import Pinecone
      import requests
      from pinecone_plugins.assistant.models.chat import Message

      pc = Pinecone(api_key="YOUR_API_KEY")

      # Create an assistant.
      assistant = pc.assistant.create_assistant(
          assistant_name="example-assistant", 
          instructions="Use American English for spelling and grammar.", # Description or directive for the assistant to apply to all responses.
          region="us", # Region to deploy assistant. Options: "us" (default) or "eu".    
          timeout=30 # Maximum seconds to wait for assistant status to become "Ready" before timing out.
      )

      # Upload a file to your assistant.
      response = assistant.upload_file(
          file_path="/Users/jdoe/Downloads/Netflix-10-K-01262024.pdf",
          metadata={"company": "netflix", "document_type": "form 10k"},
          timeout=None
      )

      # Set up for evaluation later.
      payload = {
          "question": "Who is the CFO of Netflix?", # Question to ask the assistant.
          "ground_truth_answer": "Spencer Neumann" # Expected answer to evaluate the assistant's response.
      }

      # Chat with the assistant.
      msg = Message(role="user", content=payload["question"])
      resp = assistant.chat(messages=[msg], model="gpt-4o")
      print(resp)

      # {
      #    'id': '0000000000000000163008a05b317b7b', 
      #    'model': 'gpt-4o-2024-05-13', 
      #    'usage': {
      #        'prompt_tokens': 9259, 
      #        'completion_tokens': 30, 
      #        'total_tokens': 9289
      #        }, 
      #        'message': {
      #            'content': 'The Chief Financial Officer (CFO) of Netflix is Spencer Neumann.', 
      #            'role': '"assistant"'
      #            }, 
      #            'finish_reason': 'stop', 
      #            'citations': [
      #                {
      #                    'position': 63, 
      #                    'references': [
      #                        {
      #                            'pages': [78, 72, 79], 
      #                            'file': {
      #                                'name': 'Netflix-10-K-01262024.pdf', 
      #                                'id': '76a11dd1...', 
      #                                'metadata': {
      #                                    'company': 'netflix', 
      #                                    'document_type': 'form 10k'
      #                                    }, 
      #                                    'created_on': '2024-12-06T01:29:07.369208590Z', 
      #                                    'updated_on': '2024-12-06T01:29:50.923493799Z', 
      #                                    'status': 'Available', 
      #                                    'percent_done': 1.0, 
      #                                    'signed_url': 'https://storage.googleapis.com/...', 
      #                                    'error_message': None,
      #                                    'size': 1073470.0
      #                                }
      #                            }
      #                        ]
      #                    }
      #                ]
      #            }

      # Evaluate the assistant's response.
      payload["answer"] = resp.message.content

      headers = {
          "Api-Key": "YOUR_API_KEY",
          "Content-Type": "application/json"
      }

      url = "https://prod-1-data.ke.pinecone.io/assistant/evaluation/metrics/alignment"

      response = requests.request("POST", url, json=payload, headers=headers)

      print(response.text)

      # {
      #    "metrics":
      #    {
      #        "correctness":1.0,
      #        "completeness":1.0,
      #        "alignment":1.0
      #    },
      #    "reasoning":
      #    {
      #        "evaluated_facts":
      #        [
      #            {
      #                "fact":
      #                {
      #                    "content":"Spencer Neumann is the CFO of Netflix."
      #                    },
      #                    "entailment":"entailed"
      #                }
      #            ]
      #        },
      #        "usage":
      #        {
      #            "prompt_tokens":1221,
      #            "completion_tokens":24,
      #            "total_tokens":1245
      #            }
      #        }
      ```

      ```javascript JavaScript theme={null}
      import { Pinecone } from "@pinecone-database/pinecone";

      function sleep(ms) {
        return new Promise((resolve) => setTimeout(resolve, ms));
      }

      async function testPinecone() {
        try {
          console.log("Initializing Pinecone client...");

          const pc = new Pinecone({
            apiKey: "YOUR_API_KEY",
          });

          console.log("Pinecone client initialized successfully.");

          const assistantName = "test-assistant";

          // Create a new assistant.
          console.log(`Creating new assistant: ${assistantName}...`);
          await pc.createAssistant({
            name: assistantName,
            region: "us",
            metadata: { 'test-key': 'test-value' },
          });

          // Validate Assistant was created through describe.
          const asstDesc = await pc.describeAssistant(assistantName);
          console.log(`Described Assistant: ${JSON.stringify(asstDesc)}`);

          // Delay to ensure the Assistant is ready.
          await sleep(4000);

          // Upload file
          const assistant = pc.Assistant(assistantName);
          await assistant.uploadFile({
            path: '/Users/jdoe/Downloads/Netflix-10-K-01262024.pdf',
            metadata: { 'test-key': 'test-value' },
          });
          console.log("File uploaded. Processsing...");

          // Delay to ensure file is available.
          await sleep(45000);

          // Chat
          const chatResp = await assistant.chat({
            messages: [{ role: 'user', content: 'Who is the CFO of Netflix?' }]
          });
          console.log(chatResp);
          
        // Error handling
        } catch (error) {
          console.error("Error:", error);
        }
      }

      // Run the sample code
      testAssistant();
      ```
    </CodeGroup>
  </Tab>
</Tabs>


## Learn more

<CardGroup cols={3}>
  <Card title="API Reference" icon="code-simple" href="/reference">
    Comprehensive details about the Pinecone APIs, SDKs, utilities, and architecture.
  </Card>

  <Card title="Blog" icon="blog" href="https://www.pinecone.io/learn/assistant-api-deep-dive/">
    Four features of the Assistant API you aren't using - but should
  </Card>

  <Card title="Releases" icon="party-horn" href="/release-notes">
    News about features and changes in Pinecone and related tools.
  </Card>
</CardGroup>



# Pricing and limits
Source: https://docs.pinecone.io/guides/assistant/pricing-and-limits

Understand Pinecone Assistant pricing and service limits.

Pricing and limits vary based on [subscription plan](https://www.pinecone.io/pricing/).


## Pricing

The cost of using Pinecone Assistant is determined by the following factors:

* Monthly usage
* Hourly rate
* Tokens used
* Storage

### Minimum usage

The Standard and Enterprise [pricing plans](https://www.pinecone.io/pricing/) include a monthly minimum usage committment:

| Plan       | Minimum usage |
| ---------- | ------------- |
| Starter    | \$0/month     |
| Standard   | \$50/month    |
| Enterprise | \$500/month   |

Beyond the monthly minimum, customers are charged for what they use each month.

**Examples**

<AccordionGroup>
  <Accordion title="Usage below monthly minimum">
    * You are on the Standard plan.
    * Your usage for the month of August amounts to \$20.
    * Your usage is below the \$50 monthly minimum, so your total for the month is \$50.

    In this case, the August invoice would include line items for each service you used (totaling \$20), plus a single line item covering the rest of the minimum usage commitment (\$30).
  </Accordion>

  <Accordion title="Usage exceeds monthly minimum">
    * You are on the Standard plan.
    * Your usage for the month of August amounts to \$100.
    * Your usage exceeds the \$50 monthly minimum, so your total for the month is \$100.

    In this case, the August invoice would only show line items for each service you used (totaling \$100). Since your usage exceeds the minimum usage commitment, you are only charged for your actual usage and no additional minimum usage line item appears on your invoice.
  </Accordion>
</AccordionGroup>

### Hourly rate

For paid plans, you are charged an hourly rate for each assistant, regardless of assistant activity.

| Plan       | Hourly rate |
| ---------- | ----------- |
| Starter    | Free        |
| Standard   | \$0.05/hour |
| Enterprise | \$0.05/hour |

### Tokens

For paid plans, you are charged for the number of tokens used by each assistant.

#### Chat tokens

[Chatting with an assistant](/guides/assistant/chat-with-assistant) involves both input and output tokens:

* **Input tokens** are based on the messages sent to the assistant and the context snippets retrieved from the assistant and sent to a model. Messages sent to the assistant can include messages from the [chat history](/guides/assistant/chat-with-assistant#provide-conversation-history) in addition to the newest message.

* **Output tokens** are based on the answer from the model.

| Plan       | Input token rate            | Output token rate           |
| ---------- | --------------------------- | --------------------------- |
| Starter    | Free (1.5M max per project) | Free (200k max per project) |
| Standard   | \$8/million tokens          | \$15/million tokens         |
| Enterprise | \$8/million tokens          | \$15/million tokens         |

<Note>
  Chat input tokens appear as "Assistants Input Tokens" on invoices and `prompt_tokens` in API responses. Chat output tokens appear as "Assistants Output Tokens"" on invoices and `completion_tokens` in API responses.
</Note>

#### Context tokens

When you [retrieve context snippets](/guides/assistant/context-snippets-overview), tokens are based on the messages sent to the assistant and the context snippets retrieved from the assistant. Messages sent to the assistant can include messages from the [chat history](/guides/assistant/chat-with-assistant#provide-conversation-history) in addition to the newest message.

| Plan       | Token rate                  |
| ---------- | --------------------------- |
| Starter    | Free (500k max per project) |
| Standard   | \$5/million tokens          |
| Enterprise | \$8/million tokens          |

<Note>
  Context retrieval tokens appear as **Assistants Context Tokens Processed** on invoices and `prompt_tokens` in API responses. In API responses, `completion_tokens` will always be 0 because, unlike for chat, there is no answer from a model.
</Note>

#### Evaluation tokens

[Evaluating responses](/guides/assistant/evaluation-overview) involves both input and output tokens:

* **Input tokens** are based on two requests to a model: The first request contains a question, answer, and ground truth answer, and the second request contains the same details plus generated facts returned by the model for the first request.
* **Output tokens** are based on two responses from a model: The first response contains generated facts, and the second response contains evaluation metrics.

| Plan       | Input token rate   | Output token rate   |
| ---------- | ------------------ | ------------------- |
| Starter    | Not available      | Not available       |
| Standard   | \$8/million tokens | \$15/million tokens |
| Enterprise | \$8/million tokens | \$15/million tokens |

<Note>
  Evaluation input tokens appear as **Assistants Evaluation Tokens Processed** on invoices and `prompt_tokens` in API responses. Evalulation output tokens appear as as **Assistants Evaluation Tokens Out** on invoices and `completion_tokens` in API responses.
</Note>

### Storage

For paid plans, you are charged for the size of each assistant.

| Plan       | Storage rate                |
| ---------- | --------------------------- |
| Starter    | Free (1 GB max per project) |
| Standard   | \$3/GB per month            |
| Enterprise | \$3/GB per month            |


## Limits

Pinecone Assistant limits vary based on [subscription plan](https://www.pinecone.io/pricing/).

### Object limits

Object limits are restrictions on the number or size of assistant-related objects.

| Metric                               | Starter plan  | Standard plan | Enterprise plan |
| :----------------------------------- | :------------ | :------------ | :-------------- |
| Assistants per project               | 5             | Unlimited     | Unlimited       |
| File storage per project             | 1 GB          | Unlimited     | Unlimited       |
| Chat input tokens per project        | 1,500,000     | Unlimited     | Unlimited       |
| Chat output tokens per project       | 200,000       | Unlimited     | Unlimited       |
| Context retrieval tokens per project | 500,000       | Unlimited     | Unlimited       |
| Evaluation input tokens per project  | Not available | 150,000       | 500,000         |
| Files per assistant                  | 100           | 10,000        | 10,000          |
| File size (.docx, .json, .md, .txt)  | 10 MB         | 10 MB         | 10 MB           |
| File size (.pdf)                     | 10 MB         | 100 MB        | 100 MB          |
| Metadata size per file               | 16 KB         | 16 KB         | 16 KB           |

Additionally, the following limits apply to [multimodal PDFs](/guides/assistant/multimodal) (currently in [public preview](/release-notes/feature-availability)):

| Metric                        | Starter plan | Standard plan | Enterprise plan |
| :---------------------------- | :----------- | :------------ | :-------------- |
| Max file size                 | 10 MB        | 50 MB         | 50 MB           |
| Page limit                    | 100          | 100           | 100             |
| Multimodal PDFs per assistant | 1            | 20            | 20              |

### Rate limits

Rate limits help protect your applications from misuse and maintain the health of our shared infrastructure. These limits are designed to support typical production workloads while ensuring reliable performance for all users.

**Most rate limits can be adjusted upon request.** If you need higher limits to scale your application, [contact Support](https://app.pinecone.io/organizations/-/settings/support/ticket) with details about your use case.

Requests that exceed a rate limit fail and return a `429 - TOO_MANY_REQUESTS` status.

<Tip>To handle rate limits, implement [retry logic with exponential backoff](/guides/production/error-handling#implement-retry-logic).</Tip>

| Metric                                      | Starter plan | Standard plan | Enterprise plan |
| :------------------------------------------ | :----------- | :------------ | :-------------- |
| Assistant list/get requests per minute      | 40           | 100           | 500             |
| Assistant create/update requests per minute | 20           | 50            | 100             |
| Assistant delete requests per minute        | 20           | 50            | 100             |
| File list/get requests per minute           | 100          | 300           | 6000            |
| File upload requests per minute             | 5            | 20            | 300             |
| File delete requests per minute             | 5            | 20            | 300             |
| Chat input tokens per minute                | 100,000      | 300,000       | 1,000,000       |
| Chat history tokens per query               | 64,000       | 64,000        | 64,000          |



# Pinecone Assistant quickstart
Source: https://docs.pinecone.io/guides/assistant/quickstart

Get started with Pinecone Assistant manually or with no-code tools.

<Tabs>
  <Tab title="Manual">
    Use a Pinecone SDK to create an assistant, upload documents, and chat with the assistant.

    <Tip>
      To get started in your browser, use the [Assistant Quickstart colab notebook](https://colab.research.google.com/github/pinecone-io/examples/blob/master/docs/assistant-quickstart.ipynb).
    </Tip>

    ## 1. Install an SDK

    The Pinecone [Python SDK](/reference/python-sdk) and [Node.js SDK](/reference/node-sdk) provide convenient programmatic access to the [Assistant API](/reference/api/latest/assistant/).

    <CodeGroup>
      ```shell Python theme={null}
      pip install pinecone
      pip install pinecone-plugin-assistant
      ```

      ```shell JavaScript theme={null}
      npm install @pinecone-database/pinecone
      ```
    </CodeGroup>

    ## 2. Get an API key

    You need an API key to make calls to your assistant.

    Create a new API key in the [Pinecone console](https://app.pinecone.io/organizations/-/keys), or use the widget below to generate a key. If you don't have a Pinecone account, the widget will sign you up for the free [Starter plan](https://www.pinecone.io/pricing/).

    <div style={{minWidth: '450px', minHeight:'152px'}}>
      <div id="pinecone-connect-widget">
        <div class="connect-widget-skeleton">
          <div class="skeleton-content" />
        </div>
      </div>
    </div>

    Your generated API key:

    ```shell  theme={null}
    "{{YOUR_API_KEY}}"
    ```

    ## 3. Create an assistant

    [Create an assistant](/reference/api/latest/assistant/create_assistant), as in the following example:

    <CodeGroup>
      ```python Python theme={null}
      from pinecone import Pinecone

      pc = Pinecone(api_key="{{YOUR_API_KEY}}")

      assistant = pc.assistant.create_assistant(
          assistant_name="example-assistant", 
          instructions="Use American English for spelling and grammar.", # Description or directive for the assistant to apply to all responses.
          region="us", # Region to deploy assistant. Options: "us" (default) or "eu".
          timeout=30 # Maximum seconds to wait for assistant status to become "Ready" before timing out.
      )
      ```

      ```javascript JavaScript theme={null}
      import { Pinecone } from '@pinecone-database/pinecone'

      const pc = new Pinecone({ apiKey: "{{YOUR_API_KEY}}" });

      const assistant = await pc.createAssistant({
        name: 'example-assistant',
        instructions: 'Use American English for spelling and grammar.', // Description or directive for the assistant to apply to all responses.
        region: 'us'
      });
      ```
    </CodeGroup>

    ## 4. Upload a file to the assistant

    With Pinecone Assistant, you can upload documents, ask questions, and receive responses that reference your documents. This is known as retrieval-augmented generation (RAG).

    For this quickstart, [download a sample 10-k filing file](https://s22.q4cdn.com/959853165/files/doc_financials/2023/ar/Netflix-10-K-01262024.pdf) to your local device.

    Next, [upload the file](/reference/api/latest/assistant/upload_file) to your assistant:

    <CodeGroup>
      ```python Python theme={null}
      # Get the assistant.
      assistant = pc.assistant.Assistant(
          assistant_name="example-assistant", 
      )

      # Upload a file.
      response = assistant.upload_file(
          file_path="/path/to/file/Netflix-10-K-01262024.pdf",
          metadata={"company": "netflix", "document_type": "form 10k"},
          timeout=None
      )
      ```

      ```javascript JavaScript theme={null}
      const assistantName = 'example-assistant';
      const assistant = pc.Assistant(assistantName);

      await assistant.uploadFile({
        path: '/Users/jdoe/Downloads/example_file.txt'
      });
      ```
    </CodeGroup>

    ## 5. Chat with the assistant

    With the sample file uploaded, you can now [chat with the assistant](/reference/api/latest/assistant/chat_assistant). Ask the assistant questions about your document. It returns either a JSON object or a text stream.

    The following example requests a default response to the message, "Who is the CFO of Netflix?":

    <CodeGroup>
      ```python Python theme={null}
      from pinecone_plugins.assistant.models.chat import Message

      msg = Message(role="user", content="Who is the CFO of Netflix?")
      resp = assistant.chat(messages=[msg])

      print(resp)
      ```

      ```javascript JavaScript theme={null}
      const chatResp = await assistant.chat({
        messages: [{ role: 'user', content: 'Who is the CFO of Netflix?' }],
        model: 'gpt-4o'
      });

      console.log(chatResp);
      ```
    </CodeGroup>

    The example above returns a response like the following:

    ```
    {
        'id': '0000000000000000163008a05b317b7b', 
        'model': 'gpt-4o-2024-05-13', 
        'usage': {
            'prompt_tokens': 9259, 
            'completion_tokens': 30, 
            'total_tokens': 9289
            }, 
            'message': {
                'content': 'The Chief Financial Officer (CFO) of Netflix is Spencer Neumann.', 
                'role': '"assistant"'
                }, 
                'finish_reason': 'stop', 
                'citations': [
                    {
                        'position': 63, 
                        'references': [
                            {
                                'pages': [78, 72, 79], 
                                'file': {
                                    'name': 'Netflix-10-K-01262024.pdf', 
                                    'id': '76a11dd1...', 
                                    'metadata': {
                                        'company': 'netflix', 
                                        'document_type': 'form 10k'
                                        }, 
                                        'created_on': '2024-12-06T01:29:07.369208590Z', 
                                        'updated_on': '2024-12-06T01:29:50.923493799Z', 
                                        'status': 'Available', 
                                        'percent_done': 1.0, 
                                        'signed_url': 'https://storage.googleapis.com/...', 
                                        "error_message": null, 
                                        'size': 1073470.0
                                    }
                                }
                            ]
                        }
                    ]
                }
    ```

    <Warning>
      [`signed_url`](https://cloud.google.com/storage/docs/access-control/signed-urls) provides temporary, read-only access to the relevant file. Anyone with the link can access the file, so treat it as sensitive data. Expires in one hour.
    </Warning>

    ## 6. Clean up

    When you no longer need the `example-assistant`, [delete the assistant](/reference/api/latest/assistant/delete_assistant):

    <Warning>
      Deleting an assistant also deletes all files uploaded to the assistant.
    </Warning>

    <CodeGroup>
      ```python Python theme={null}
      pc.assistant.delete_assistant(
          assistant_name="example-assistant", 
      )
      ```

      ```javascript JavaScript theme={null}
      await pc.deleteAssistant('example-assistant');
      ```
    </CodeGroup>

    ## Next steps

    * Learn more about [Pinecone Assistant](/guides/assistant/overview)
    * Learn about [additional assistant features](https://www.pinecone.io/learn/assistant-api-deep-dive/)
    * [Evaluate](/guides/assistant/evaluate-answers) the assistant's responses
    * View a [sample app](/examples/sample-apps/pinecone-assistant) that uses Pinecone Assistant
  </Tab>

  <Tab title="n8n">
    Create an [n8n](https://docs.n8n.io/choose-n8n/) workflow that downloads files via HTTP and lets you chat with them using Pinecone Assistant and OpenAI.

    ## 1. Get API keys

    Your n8n workflow will need API keys for Pinecone and OpenAI.

    <Steps>
      <Step title="Get a Pinecone API key">
        Create a new API key in the [Pinecone console](https://app.pinecone.io/organizations/-/keys), or use the widget below to generate a key. If you don't have a Pinecone account, the widget will sign you up for the free [Starter plan](https://www.pinecone.io/pricing/).

        <div style={{minWidth: '450px', minHeight:'152px'}}>
          <div id="pinecone-connect-widget">
            <div class="connect-widget-skeleton">
              <div class="skeleton-content" />
            </div>
          </div>
        </div>

        Your generated API key:

        ```shell  theme={null}
        "{{YOUR_API_KEY}}"
        ```
      </Step>

      <Step title="Get an OpenAI API key">
        Create a new API key in the [OpenAI console](https://platform.openai.com/api-keys).
      </Step>
    </Steps>

    ## 2. Create an assistant

    [Create an assistant](https://app.pinecone.io/organizations/-/projects/-/assistant) in the Pinecone console:

    * Name your assistant `n8n-assistant`.
    * Create it in the `United States` region.

    ## 3. Set up n8n

    <Steps>
      <Step title="Create a new workflow">
        In your n8n account, [create a new workflow](https://docs.n8n.io/workflows/create/).
      </Step>

      <Step title="Import a workflow template">
        Copy this workflow template URL:

        ```shell  theme={null}
        https://raw.githubusercontent.com/pinecone-io/n8n-templates/refs/heads/main/quickstart/assistant-quickstart.json
        ```

        Paste the URL into the workflow editor and then click **Import** to add the workflow.
      </Step>

      <Step title="Add credentials to the workflow">
        * Add your Pinecone credentials:
          * In the **Upload file to assistant** node, select **PineconeApi** > **Create new credential** and paste in your Pinecone API key.
          * In the **Pinecone Assistant**, select **Credential for Bearer Auth** > **Create new credential** and paste in your Pinecone API key.

        * Add your OpenAI credentials:
          * In the **OpenAI Chat Model**, select **Credential to connect with** > **Create new credential** and paste in your OpenAI API key.
      </Step>

      <Step title="Activate the workflow">
        The workflow is configured to download recent Pinecone release notes and upload them to your assistant. Click **Execute workflow** to start the workflow.

        <Tip>
          You can add your own files to the workflow by changing the URLs in the **Set file urls** node.
        </Tip>
      </Step>
    </Steps>

    ## 4. Chat with your docs

    Once the workflow is activated, ask it for the latest changes to Pinecone Assistant:

    ```
    What's new in Pinecone Assistant?
    ```

    ## Next steps

    * Modify the workflow to your own use case:
      * Change the urls in **Set file urls** node to use your own files.
      * Customize the system message on the **AI Agent** node to your use case.
      * To help manage token consumption, change the `top_k` value of results returned from your assistant by adding "and should set a top\_k of 3" to the system message.
    * Use n8n, Pinecone Assistant, and OpenAI to [chat with your Google Drive documents](https://n8n.io/workflows/9942-rag-powered-document-chat-with-google-drive-openai-and-pinecone-assistant/).
    * Learn more about [Pinecone Assistant](/guides/assistant/overview).
    * Get help in the [Pinecone Discord community](https://discord.gg/tJ8V62S3sH) or the [Pinecone Forum](https://community.pinecone.io/).
  </Tab>
</Tabs>



# Retrieve context snippets
Source: https://docs.pinecone.io/guides/assistant/retrieve-context-snippets

Access relevant context and citations from Pinecone Assistant.

This page shows you how to [retrieve context snippets](/guides/assistant/context-snippets-overview).

<Tip>
  To try this in your browser, use the [Pinecone Assistant - Context colab notebook](https://colab.research.google.com/drive/1AD4QWsXBG1FQRwq-ModlaggR7Cx7NJCz).
</Tip>


## Retrieve context snippets from an assistant

You can [retrieve context snippets](/reference/api/latest/assistant/context_assistant) from an assistant, as in the following example:

<CodeGroup>
  ```python Python theme={null}
  # To use the Python SDK, install the plugin:
  # pip install --upgrade pinecone pinecone-plugin-assistant

  from pinecone import Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")
  assistant = pc.assistant.Assistant(assistant_name="example-assistant")

  response = assistant.context(query="Who is the CFO of Netflix?")

  for snippet in response.snippets:
      print(snippet)
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  const assistantName = 'example-assistant';
  const assistant = pc.Assistant(assistantName);
  const response = await assistant.context({
    query: 'Who is the CFO of Netflix?',
  });
  console.log(response);
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  ASSISTANT_NAME="example-assistant"

  curl "https://prod-1-data.ke.pinecone.io/assistant/chat/$ASSISTANT_NAME/context" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "accept: application/json" \
    -H "Content-Type: application/json" \
    -H "X-Pinecone-API-Version: 2025-04" \
    -d '{
      "query": "Who is the CFO of Netflix?"
  }'
  ```
</CodeGroup>

The example above returns a JSON object like the following:

```json JSON theme={null}
{
    "snippets":
    [
        {
            "type":"text",
            "content":"EXHIBIT 31.3\nCERTIFICATION OF CHIEF FINANCIAL OFFICER\nPURSUANT TO SECTION 302 OF THE SARBANES-OXLEY ACT OF 2002\nI, Spencer Neumann, certify that: ..."
            "score":0.9960699,
            "reference":
            {
                "type":"pdf",
                "file":
                {
                    "status":"Available",
                    "id":"e6034e51-0bb9-4926-84c6-70597dbd07a7",
                    "name":"Netflix-10-K-01262024.pdf",
                    "size":1073470,
                    "metadata":null,
                    "updated_on":"2024-11-21T22:59:10.426001030Z",
                    "created_on":"2024-11-21T22:58:35.879120257Z", 
                    "percent_done":1.0,
                    "signed_url":"https://storage.googleapis.com...",
                    "error_message":null
                    },
                "pages":[78]
            }
        },
{
    "type":"text",
    "content":"EXHIBIT 32.1\n..."
...
```

<Warning>
  [`signed_url`](https://cloud.google.com/storage/docs/access-control/signed-urls) provides temporary, read-only access to the relevant file. Anyone with the link can access the file, so treat it as sensitive data. Expires in one hour.
</Warning>


## Control the snippets retrieved

<Note>
  This is available in API versions `2025-04` and later.
</Note>

You can limit [token usage](/guides/assistant/pricing-and-limits#token-usage) by tuning `top_k * snippet_size`:

* `snippet_size`: Controls the max size of a snippet (default is 2048 tokens). Note that snippet size can vary and, in rare cases, may be bigger than the set `snippet_size`. Snippet size controls the amount of context given for each chunk of text.
* `top_k`: Controls the max number of context snippets retrieved (default is 16). `top_k` controls the diversity of information received in the returned snippets.

While additional tokens will be used for other parameters, adjusting the `top_k` and `snippet_size` can help manage token consumption.

<CodeGroup>
  ```python Python theme={null}
  # To use the Python SDK, install the plugin:
  # pip install --upgrade pinecone pinecone-plugin-assistant

  from pinecone import Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")
  assistant = pc.assistant.Assistant(assistant_name="example-assistant")

  response = assistant.context(query="Who is the CFO of Netflix?", top_k=10, snippet_size=2500)

  for snippet in response.snippets:
      print(snippet)
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  ASSISTANT_NAME="example-assistant"

  curl "https://prod-1-data.ke.pinecone.io/assistant/chat/$ASSISTANT_NAME/context" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "accept: application/json" \
    -H "Content-Type: application/json" \
    -H "X-Pinecone-API-Version: 2025-04" \
    -d '{
      "query": "Who is the CFO of Netflix?",
      "top_k": 10,
      "snippet_size": 2500
  }'
  ```
</CodeGroup>



# Upload files
Source: https://docs.pinecone.io/guides/assistant/upload-files

Upload local files to an assistant.

<Note>
  File upload limitations depend on the plan you are using. For more information, see [Pricing and limitations](/guides/assistant/pricing-and-limits#limits).
</Note>


## Upload a local file

You can [upload a file to your assistant](/reference/api/latest/assistant/upload_file) from your local device, as in the following example:

<CodeGroup>
  ```python Python theme={null}
  # To use the Python SDK, install the plugin:
  # pip install --upgrade pinecone pinecone-plugin-assistant

  from pinecone import Pinecone
  pc = Pinecone(api_key="YOUR_API_KEY")

  # Get an assistant.
  assistant = pc.assistant.Assistant(
      assistant_name="example-assistant", 
  )

  # Upload a file.
  response = assistant.upload_file(
      file_path="/Users/jdoe/Downloads/example_file.txt",
      timeout=None
  )
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  const assistantName = 'example-assistant';
  const assistant = pc.Assistant(assistantName);
  await assistant.uploadFile({
    path: '/Users/jdoe/Downloads/example_file.txt'
  });
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  ASSISTANT_NAME="example-assistant"
  LOCAL_FILE_PATH="/Users/jdoe/Downloads/example_file.txt"

  curl -X POST "https://prod-1-data.ke.pinecone.io/assistant/files/$ASSISTANT_NAME" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -F "file=@$LOCAL_FILE_PATH"
  ```
</CodeGroup>

It may take several minutes for your assistant to process your file. You can [check the status of your file](/guides/assistant/manage-files#get-the-status-of-a-file) to determine if it is ready to use.

<Tip>
  You can upload a file to an assistant using the [Pinecone console](https://app.pinecone.io/organizations/-/projects/-/assistant). Select the assistant you want to upload to and add the file in the Assistant playground.
</Tip>


## Upload a file with metadata

You can upload a file with metadata. Metadata is a dictionary of key-value pairs that you can use to store additional information about the file. For example, you can use metadata to store the file's name, document type, publish date, or any other relevant information.

<CodeGroup>
  ```Python Python theme={null}
  # To use the Python SDK, install the plugin:
  # pip install --upgrade pinecone pinecone-plugin-assistant

  from pinecone import Pinecone
  pc = Pinecone(api_key="YOUR_API_KEY")

  # Get the assistant.
  assistant = pc.assistant.Assistant(
      assistant_name="example-assistant", 
  )

  # Upload a file.
  response = assistant.upload_file(
      file_path="/Users/jdoe/Downloads/example_file.txt",
      metadata={"published": "2024-01-01", "document_type": "manuscript"},
      timeout=None
  )
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  const assistantName = 'example-assistant';
  const assistant = pc.Assistant(assistantName);
  await assistant.uploadFile({
    path: '/Users/jdoe/Downloads/example_file.txt',
    metadata: { 'published': '2024-01-01', 'document_type': 'manuscript' },
  });
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  ASSISTANT_NAME="example-assistant"
  ENCODED_METADATA="%7B%22published%22%3A%222024-01-01%22%2C%22document_type%22%3A%22script%22%7D" # URL encoded metadata - See w3schools.com/tags/ref_urlencode.ASP
  LOCAL_FILE_PATH="/Users/jdoe/Downloads/example_file.txt"

  curl -X POST "https://prod-1-data.ke.pinecone.io/assistant/files/$ASSISTANT_NAME?metadata=$ENCODED_METADATA" \
      -H "Api-Key: $PINECONE_API_KEY" \
      -F "file=@$LOCAL_FILE_PATH"
  ```
</CodeGroup>

When a file is uploaded with metadata, you can use the metadata to [filter a list of files](/guides/assistant/manage-files#view-a-filtered-list-of-files) and [filter chat responses](/guides/assistant/chat-with-assistant#filter-chat-with-metadata).


## Upload a PDF with multimodal context

Assistants can gather context from images contained in PDF files. To learn more about this feature, see [Multimodal context for assistants](/guides/assistant/multimodal).


## Upload from a binary stream

You can upload a file directly from an in-memory binary stream using the Python SDK and the [BytesIO class](https://docs.python.org/3/library/io.html#io.BytesIO).

<Note>
  When uploading text-based files (like .txt, .md, .json, etc.) through BytesIO streams, make sure the content is encoded in UTF-8 format.
</Note>

```python Python theme={null}
from pinecone import Pinecone
from io import BytesIO

pc = Pinecone(api_key="YOUR_API_KEY")


# Get an assistant
assistant = pc.assistant.Assistant(
    assistant_name="example-assistant", 
)


# Create a BytesIO stream with some content
md_text = "# Title\n\ntext"

# Note: Assistant currently supports only utf-8 for text-based files
stream = BytesIO(md_text.encode("utf-8"))


# Upload the stream
response = assistant.upload_bytes_stream(
    stream=stream,
    file_name="example_file.md",
    timeout=None
)
```



# Attribute usage to your integration
Source: https://docs.pinecone.io/integrations/build-integration/attribute-usage-to-your-integration



Once you have created your integration with Pinecone, specify a **source tag** when instantiating clients with Pinecone SDKs, or pass a source tag as part of the `User-Agent` header when using the API directly.

<Note>
  Anyone can create an integration, but [becoming an official Pinecone partner](/integrations/build-integration/become-a-partner) can help accelerate your go-to-market and add value to your customers.
</Note>

### Source tag naming conventions

Your source tag must follow these conventions:

* Clearly identify your integration.
* Use only lowercase letters, numbers, underscores, and colons.

For example, for an integration called "New Framework", `"new_framework"` is valid, but `"new framework"` and `"New_framework"` are not valid.

### Specify a source tag

| Pinecone SDK                    | Required version |
| ------------------------------- | ---------------- |
| [Python](/reference/python-sdk) | v3.2.1+          |
| [Node.js](/reference/node-sdk)  | v2.2.0+          |
| [Java](/reference/java-sdk)     | v1.0.0+          |
| [Go](/reference/go-sdk)         | v0.4.1+          |
| [.NET](/reference/dotnet-sdk)   | v1.0.0+          |

<CodeGroup>
  ```python Python theme={null}
  # REST client
  from pinecone import Pinecone

  pc = Pinecone(
      api_key="YOUR_API_KEY", 
      source_tag="YOUR_SOURCE_TAG"
  )

  # gRPC client
  from pinecone.grpc import PineconeGRPC

  pc = PineconeGRPC(
      api_key="YOUR_API_KEY", 
      source_tag="YOUR_SOURCE_TAG"
  )
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ 
      apiKey: 'YOUR_API_KEY', 
      sourceTag: 'YOUR_SOURCE_TAG' 
  });
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Pinecone;

  public class IntegrationExample {
      public static void main(String[] args) {
          Pinecone pc = new Pinecone.Builder("YOUR_API_KEY")
                  .withSourceTag("YOUR_SOURCE_TAG")
                  .build();
      }
  }
  ```

  ```go Go theme={null}
  import "github.com/pinecone-io/go-pinecone/v4/pinecone"

  client, err := pinecone.NewClient(pinecone.NewClientParams{
  	ApiKey: "YOUR_API_KEY",
  	SourceTag: "YOUR_SOURCE_TAG",
  })
  ```

  ```csharp C# theme={null}
  using Pinecone;

  var pinecone = new PineconeClient("YOUR_API_KEY", new ClientOptions
  {
      SourceTag = "YOUR_SOURCE_TAG",
  });
  ```

  ```shell curl theme={null}
  curl -i -X GET "https://api.pinecone.io/indexes" \
    -H "Accept: application/json" \
    -H "Api-Key: YOUR_API_KEY" \
    -H "User-Agent: source_tag=YOUR_SOURCE_TAG" \
    -H "X-Pinecone-API-Version: 2025-04"
  ```
</CodeGroup>



---
**Navigation:** [← Previous](./29-chat-through-the-openai-compatible-interface.md) | [Index](./index.md) | [Next →](./31-become-a-pinecone-partner.md)
