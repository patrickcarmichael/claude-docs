**Navigation:** [← Previous](./28-download-a-usage-report.md) | [Index](./index.md) | [Next →](./30-use-an-assistant-mcp-server.md)

# Chat through the OpenAI-compatible interface
Source: https://docs.pinecone.io/guides/assistant/chat-through-the-openai-compatible-interface

Integrate OpenAI-compatible chat interface with Pinecone Assistant.

After [uploading files](/guides/assistant/manage-files) to an assistant, you can chat with the assistant.

This page shows you how to chat with an assistant using the [OpenAI-compatible chat interface](/reference/api/latest/assistant/chat_completion_assistant). This interface is based on the OpenAI Chat Completion API, a commonly used and adopted API. It is useful if you need inline citations or OpenAI-compatible responses, but has limited functionality compared to the [standard chat interface](/guides/assistant/chat-with-assistant).

<Tip>
  The [standard chat interface](/guides/assistant/chat-with-assistant) is the recommended way to chat with an assistant, as it offers more functionality and control over the assistant's responses and references.
</Tip>


## Chat with an assistant

The [OpenAI-compatible chat interface](/reference/api/latest/assistant/chat_completion_assistant) can return responses in two different formats:

* [Default response](#default-response): The assistant returns a response in a single string field, which includes citation information.
* [Streaming response](#streaming-response): The assistant returns the response as a text stream.

### Default response

The following example sends a message and requests a response in the default format:

<Note>
  The `content` parameter in the request cannot be empty.
</Note>

<CodeGroup>
  ```python Python theme={null}
  # To use the Python SDK, install the plugin:
  # pip install --upgrade pinecone pinecone-plugin-assistant

  from pinecone import Pinecone
  from pinecone_plugins.assistant.models.chat import Message

  pc = Pinecone(api_key="YOUR_API_KEY")

  # Get your assistant.
  assistant = pc.assistant.Assistant(
      assistant_name="example-assistant", 
  )

  # Chat with the assistant.
  chat_context = [Message(role="user", content='What is the maximum height of a red pine?')]
  response = assistant.chat_completions(messages=chat_context)

  print(response)
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });
  const assistantName = 'example-assistant';

  const assistant = pc.Assistant(assistantName);
  const chatResp = await assistant.chatCompletion({
        messages: [{ role: 'user', content: 'Who is the CFO of Netflix?' }]
      });
  console.log(chatResp);
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  ASSISTANT_NAME="example-assistant"

  curl "https://prod-1-data.ke.pinecone.io/assistant/chat/$ASSISTANT_NAME/chat/completions" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -H "X-Pinecone-API-Version: 2025-04" \
    -d '{
    "messages": [
      {
        "role": "user",
        "content": "What is the maximum height of a red pine?"
      }
    ]
  }'
  ```
</CodeGroup>

The example above returns a result like the following:

```JSON  theme={null}
{"chat_completion":
  {
    "id":"chatcmpl-9OtJCcR0SJQdgbCDc9JfRZy8g7VJR",
    "choices":[
      {
        "finish_reason":"stop",
        "index":0,
        "message":{
          "role":"assistant",
          "content":"The maximum height of a red pine (Pinus resinosa) is up to 25 meters."
        }
      }
    ],
    "model":"my_assistant"
  }
}
```

### Streaming response

The following example sends a messages and requests a streaming response:

<Note>
  The `content` parameter in the request cannot be empty.
</Note>

<CodeGroup>
  ```python Python theme={null}
  # To use the Python SDK, install the plugin:
  # pip install --upgrade pinecone pinecone-plugin-assistant

  from pinecone import Pinecone
  from pinecone_plugins.assistant.models.chat import Message

  pc = Pinecone(api_key="YOUR_API_KEY")

  # Get your assistant.
  assistant = pc.assistant.Assistant(
      assistant_name="example-assistant" 
  )

  # Streaming chat with the Assistant.
  chat_context = [Message(role="user", content="What is the maximum height of a red pine?")]
  response = assistant.chat_completions(messages=[chat_context], stream=True)

  for data in response:
      if data:
          print(data)
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });
  const assistantName = 'example-assistant';
  const assistant = pc.Assistant(assistantName);
  const chatResp = await assistant.chatCompletionStream({
      messages: [{ role: 'user', content: 'Who is the CFO of Netflix?' }]
  });

  for await (const response of chatResp) {
      if (response) {
          console.log(response);
      }
  }
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  ASSISTANT_NAME="example-assistant"

  curl "https://prod-1-data.ke.pinecone.io/assistant/chat/$ASSISTANT_NAME/chat/completions" \
    -H "Api-Key: $PINECONE_API_KEY "\
    -H "Content-Type: application/json" \
    -H "X-Pinecone-API-Version: 2025-04" \
    -d '{
    "messages": [
      {
        "role": "user",
        "content": "What is the maximum height of a red pine?"
      }
    ],
    "stream": true
  }'
  ```
</CodeGroup>

The example above returns a result like the following:

```shell  theme={null}
{
  'id': '000000000000000009de65aa87adbcf0', 
  'choices': [
      {
      'index': 0, 
      'delta': 
        {
        'role': 'assistant', 
        'content': 'The'
        }, 
      'finish_reason': None
      }
    ], 
  'model': 'gpt-4o-2024-05-13'
}

...

{
  'id': '00000000000000007a927260910f5839',
  'choices': [
      {
      'index': 0,
      'delta':
        {
          'role': '', 
          'content': 'The'
        }, 
      'finish_reason': None
      }
    ], 
  'model': 'gpt-4o-2024-05-13'
}

...

{
  'id': '00000000000000007a927260910f5839', 
  'choices': [
    {
      'index': 0, 
      'delta': 
        {
        'role': None, 
        'content': None
        }, 
      'finish_reason': 'stop'
      }
    ], 
  'model': 'gpt-4o-2024-05-13'
}
```

There are three types of messages in a chat completion response:

* **Message start**: Includes `"role":"assistant"`, which indicates that the assistant is responding to the user's message.
* **Content**: Includes a value in the `content` field (e.g., `"content":"The"`), which is part of the assistant's streamed response to the user's message.
* **Message end**: Includes `"finish_reason":"stop"`, which indicates that the assistant has finished responding to the user's message.


## Extract the response content

In the assistant's response, the message string is contained in the following JSON object:

* `choices.[0].message.content` for the default chat response
* `choices[0].delta.content` for the streaming chat response

You can extract the message content and print it to the console:

<Tabs>
  <Tab title="Default response">
    <CodeGroup>
      ```python Python theme={null}
      print(str(response.choices[0].message.content))
      ```

      ```bash curl theme={null}
      | jq '.choices.[0].message.content'
      ```
    </CodeGroup>

    This creates output like the following:

    ```bash  theme={null}
    A red pine, scientifically known as *Pinus resinosa*, is a medium-sized tree that can grow up to 25 meters high and 75 centimeters in diameter. [1, pp. 1]
    ```
  </Tab>

  <Tab title="Streaming response">
    <CodeGroup>
      ```python Python theme={null}
      for data in response:
          if data:
              print(str(data.choices[0].delta.content))
      ```

      ```bash curl theme={null}
      |  sed -u 's/.*"content":"\([^"]*\)".*/\1/'
      ```
    </CodeGroup>

    This creates output like the following:

    ```bash Streaming response theme={null}
    The
     maximum
     height
     of
     a
     red
     pine
     (
    Pin
    us
     resin
    osa
    )
     is
     up
     to
     twenty
    -five
     meters

     [1, pp. 1]
    .
    ```
  </Tab>
</Tabs>


## Choose a model

Pinecone Assistant supports the following models:

* `gpt-4o` (default)
* `gpt-4.1`
* `o4-mini`
* `claude-3-5-sonnet`
* `claude-3-7-sonnet`
* `gemini-2.5-pro`

To choose a non-default model for your assistant, set the `model` parameter in the request:

<CodeGroup>
  ```python Python theme={null}
  # To use the Python SDK, install the plugin:
  # pip install --upgrade pinecone pinecone-plugin-assistant

  from pinecone import Pinecone
  from pinecone_plugins.assistant.models.chat import Message

  pc = Pinecone(api_key="YOUR_API_KEY")

  # Get your assistant.
  assistant = pc.assistant.Assistant(
      assistant_name="example-assistant", 
  )

  # Chat with the assistant.
  chat_context = [Message(role="user", content="What is the maximum height of a red pine?")]
  response = assistant.chat_completions(
      messages=chat_context, 
      model="gpt-4.1"
  )
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  const assistantName = 'example-assistant';
  const assistant = pc.Assistant(assistantName);
  const chatResp = await assistant.chatCompletion({
    messages: [{ role: 'user', content: 'What is the maximum height of a red pine?' }],
    model: 'gpt-4.1',
  });

  console.log(chatResp);
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  ASSISTANT_NAME="example-assistant"

  curl "https://prod-1-data.ke.pinecone.io/assistant/chat/$ASSISTANT_NAME/chat/completions" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -H "X-Pinecone-API-Version: 2025-04" \
    -d '{
    "messages": [
      {
        "role": "user",
        "content": "What is the maximum height of a red pine?"
      }
    ],
    "model": "gpt-4.1"
  }'
  ```
</CodeGroup>


## Filter chat with metadata

You can [filter which documents to use for chat completions](/guides/assistant/files-overview#file-metadata). The following example filters the responses to use only documents that include the metadata `"resource": "encyclopedia"`.

<CodeGroup>
  ```python Python theme={null}
  # To use the Python SDK, install the plugin:
  # pip install --upgrade pinecone pinecone-plugin-assistant

  from pinecone import Pinecone
  from pinecone_plugins.assistant.models.chat import Message

  pc = Pinecone(api_key="YOUR_API_KEY")

  # Get your assistant.
  assistant = pc.assistant.Assistant(
      assistant_name="example-assistant", 
  )

  # Chat with the assistant.
  chat_context = [Message(role="user", content="What is the maximum height of a red pine?")]
  response = assistant.chat_completions(messages=chat_context, stream=True, filter={"resource": "encyclopedia"})
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });
  const assistantName = 'example-assistant';
  const assistant = pc.Assistant(assistantName);
  const chatResp = await assistant.chatCompletion({
    messages: [{ role: 'user', content: 'What is the maximum height of a red pine?' }],
    filter: {
      'resource': 'encyclopedia'
    }
  });
  console.log(chatResp);
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  ASSISTANT_NAME="example-assistant"

  curl "https://prod-1-data.ke.pinecone.io/assistant/chat/$ASSISTANT_NAME/chat/completions" \
    -H "Api-Key: $PINECONE_API_KEY "\
    -H "Content-Type: application/json" \
    -H "X-Pinecone-API-Version: 2025-04" \
    -d '{
    "messages": [
      {
        "role": "user",
        "content": "What is the maximum height of a red pine?"
      }
    ],
    "stream": true,
    "filter": 
      {
      "resource": "encyclopedia"
      }
    }'
  ```
</CodeGroup>


## Set the sampling temperature

<Note>
  This is available in API versions `2025-04` and later.
</Note>

Temperature is a parameter that controls the randomness of a model's predictions during text generation. Lower temperatures (\~0.0) yield more consistent, predictable answers, while higher temperatures increase the model's explanatory power and is generally better for creative tasks.

To control the sampling temperature for a model, set the `temperarture` parameter in the request. If a model does not support a temperature parameter, the parameter is ignored.

<CodeGroup>
  ```python Python theme={null}
  # To use the Python SDK, install the plugin:
  # pip install --upgrade pinecone pinecone-plugin-assistant

  from pinecone import Pinecone
  from pinecone_plugins.assistant.models.chat import Message

  pc = Pinecone(api_key="YOUR_API_KEY")
  assistant = pc.assistant.Assistant(assistant_name="example-assistant")

  msg = Message(role="user", content="Who is the CFO of Netflix?")
  response = assistant.chat_completions(
      messages=[msg], 
      temperature=0.8
  )

  print(response)
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  const assistantName = 'example-assistant';
  const assistant = pc.Assistant(assistantName);
  const chatResp = await assistant.chatCompletion({
    messages: [{ role: 'user', content: 'Who is the CFO of Netflix?' }],
    temperature: 0.8,
  });
  console.log(chatResp);
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  ASSISTANT_NAME="example-assistant"

  curl "https://prod-1-data.ke.pinecone.io/assistant/chat/$ASSISTANT_NAME/chat/completions" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -H "X-Pinecone-API-Version: 2025-04" \
    -d '{
    "messages": [
      {
        "role": "user",
        "content": "Who is the CFO of Netflix?"
      }
    ],
    "temperature": 0.8
  }'
  ```
</CodeGroup>



# Chat through the standard interface
Source: https://docs.pinecone.io/guides/assistant/chat-with-assistant

Chat with your assistant using the standard interface and API.

After [uploading files](/guides/assistant/manage-files) to an assistant, you can chat with the assistant.

<Tip>
  You can chat with an assistant using the [Pinecone console](https://app.pinecone.io/organizations/-/projects/-/assistant). Select the assistant to chat with, and use the Assistant playground.
</Tip>


## Chat through the standard interface

The [standard chat interface](/reference/api/latest/assistant/chat_assistant) can return responses in three different formats:

* [Default response](#default-response): The assistant returns a structured response and separate citation information.
* [Streaming response](#streaming-response): The assistant returns the response as a text stream.
* [JSON response](#json-response): The assistant returns the response as JSON key-value pairs.

<Tip>
  This is the recommended way to chat with an assistant, as it offers more functionality and control over the assistant's responses and references. However, if you need your assistant to be OpenAI-compatible or need inline citations, use the [OpenAI-compatible chat interface](#chat-through-the-openai-compatible-interface).
</Tip>

### Default response

The following example sends a message and requests a default response:

<Note>
  The `content` parameter in the request cannot be empty.
</Note>

<CodeGroup>
  ```python Python theme={null}
  # To use the Python SDK, install the plugin:
  # pip install --upgrade pinecone pinecone-plugin-assistant

  from pinecone import Pinecone
  from pinecone_plugins.assistant.models.chat import Message

  pc = Pinecone(api_key="YOUR_API_KEY")
  assistant = pc.assistant.Assistant(assistant_name="example-assistant")

  msg = Message(role="user", content="Who is the CFO of Netflix?")
  response = assistant.chat(messages=[msg])

  # Alternatively, you can provide a dictionary as the message:
  # msg = {"role": "user", "content": "Who is the CFO of Netflix?"}
  # response = assistant.chat(messages=[msg])

  print(response)

  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  const assistantName = 'example-assistant';
  const assistant = pc.Assistant(assistantName);
  const chatResp = await assistant.chat({
    messages: [{ role: 'user', content: 'Who is the CFO of Netflix?' }],
  });
  console.log(chatResp);
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  ASSISTANT_NAME="example-assistant"

  curl "https://prod-1-data.ke.pinecone.io/assistant/chat/$ASSISTANT_NAME" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -H "X-Pinecone-API-Version: 2025-04" \
    -d '{
    "messages": [
      {
        "role": "user",
        "content": "Who is the CFO of Netflix?"
      }
    ],
    "stream": false,
    "model": "gpt-4o"
  }'
  ```
</CodeGroup>

The example above returns a result like the following:

```json JSON theme={null}
{
    "finish_reason": "stop",
    "message": {
        "role": "assistant",
        "content": "The Chief Financial Officer (CFO) of Netflix is Spencer Neumann."
    },
    "id": "00000000...",
    "model": "gpt-4o-2024-11-20",
    "usage": {
        "prompt_tokens": 23633,
        "completion_tokens": 24,
        "total_tokens": 23657
    },
    "citations": [
        {
            "position": 63,
            "references": [
                {
                    "file": {
                        "status": "Available",
                        "id": "76a11dd1...",
                        "name": "Netflix-10-K-01262024.pdf",
                        "size": 1073470,
                        "metadata": {
                            "company": "netflix",
                            "document_type": "form 10k"
                        },
                        "updated_on": "2025-07-16T16:46:40.787204651Z",
                        "created_on": "2025-07-16T16:45:59.414273474Z",
                        "percent_done": 1.0,
                        "signed_url": "https://storage.googleapis.com/...",
                        "error_message": null
                    },
                    "pages": [
                        78,
                        79,
                        80
                    ],
                    "highlight": null
                }
            ]
        }
    ]
}
```

<Warning>
  [`signed_url`](https://cloud.google.com/storage/docs/access-control/signed-urls) provides temporary, read-only access to the relevant file. Anyone with the link can access the file, so treat it as sensitive data. Expires in one hour.
</Warning>

### Streaming response

The following example sends a message and requests a streaming response:

<Note>
  The `content` parameter in the request cannot be empty.
</Note>

<CodeGroup>
  ```python Python theme={null}
  # To use the Python SDK, install the plugin:
  # pip install --upgrade pinecone pinecone-plugin-assistant

  from pinecone import Pinecone
  from pinecone_plugins.assistant.models.chat import Message

  pc = Pinecone(api_key="YOUR_API_KEY")

  assistant = pc.assistant.Assistant(assistant_name="example-assistant")

  msg = Message(role="user", content="What is the inciting incident of Pride and Prejudice?")

  response = assistant.chat(messages=[msg], stream=True)

  for data in response:
      if data:
          print(data)
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });
  const assistantName = 'example-assistant';

  const assistant = pc.Assistant(assistantName);
  const chatResp = await assistant.chatStream({
        messages: [{ role: 'user', content: 'Who is the CFO of Netflix?' }]
      });

  for await (const response of chatResp) {
      if (response) {
          console.log(response);
      }
  }
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  ASSISTANT_NAME="example-assistant"

  curl "https://prod-1-data.ke.pinecone.io/assistant/chat/$ASSISTANT_NAME" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -H "X-Pinecone-API-Version: 2025-04" \
    -d '{
    "messages": [
      {
        "role": "user",
        "content": "What is the inciting incident of Pride and Prejudice?"
      }
    ],
    "stream": true,
    "model": "gpt-4o"
  }'
  ```
</CodeGroup>

The example above returns a result like the following:

```shell  theme={null}
data:{"type":"message_start","id":"0000000000000000111b35de85e8a8f9","model":"gpt-4o-2024-05-13","role":"assistant"}

data:{"type":"content_chunk","id":"0000000000000000111b35de85e8a8f9","model":"gpt-4o-2024-05-13","delta":{"content":"The"}}

...

data:{"type":"citation","id":"0000000000000000111b35de85e8a8f9","model":"gpt-4o-2024-05-13","citation":{"position":406,"references":[{"file":{"status":"Available","id":"ae79e447-b89e-4994-994b-3232ca52a654","name":"Pride-and-Prejudice.pdf","size":2973077,"metadata":null,"updated_on":"2024-06-14T15:01:57.385425746Z","created_on":"2024-06-14T15:01:02.910452398Z","percent_done":0.0,"signed_url":"https://storage.googleapis.com/...", "error_message":null},"pages":[1]}]}}

data:{"type":"message_end","id":"0000000000000000111b35de85e8a8f9","model":"gpt-4o-2024-05-13","finish_reason":"stop","usage":{"prompt_tokens":9736,"completion_tokens":102,"total_tokens":9838}}
```

There are four types of messages in a streaming chat response:

* **Message start**: Includes `"role":"assistant"`, which indicates that the assistant is responding to the user's message.
* **Content**: Includes a value in the `content` field (e.g., `"content":"The"`), which is part of the assistant's streamed response to the user's message.
* **Citation**: Includes a citation to the document that the assistant used to generate the response.
* **Message end**: Includes `"finish_reason":"stop"`, which indicates that the assistant has finished responding to the user's message.

### JSON response

The following example uses the `json_response` parameter to instruct the assistant to return the response as JSON key-value pairs. This is useful if you need to parse the response programmatically.

<Note>
  JSON response cannot be used with the `stream` parameter.
</Note>

<CodeGroup>
  ```python Python theme={null}
  # To use the Python SDK, install the plugin:
  # pip install --upgrade pinecone pinecone-plugin-assistant

  import json
  from pinecone import Pinecone
  from pinecone_plugins.assistant.models.chat import Message

  pc = Pinecone(api_key="YOUR_API_KEY")

  assistant = pc.assistant.Assistant(assistant_name="example-assistant")

  msg = Message(role="user", content="Who is the CFO and CEO of Netflix?")

  response = assistant.chat(messages=[msg], json_response=True)

  print(json.loads(response))
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  const assistantName = 'example-assistant';
  const assistant = pc.Assistant(assistantName);
  const chatResp = await assistant.chat({
    messages: [{ role: 'user', content: 'Who is the CFO and CEO of Netflix?', json_response: true }],
  });
  console.log(chatResp);
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  ASSISTANT_NAME="example-assistant"

  curl "https://prod-1-data.ke.pinecone.io/assistant/chat/$ASSISTANT_NAME" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -H "X-Pinecone-API-Version: 2025-04" \
    -d '{
    "messages": [
      {
        "role": "user",
        "content": "Who is the CFO and CEO of Netflix?"
      }
    ],
    "json_response": true,
    "model": "gpt-4o"
  }'
  ```
</CodeGroup>

The example above returns a result like the following:

```json  theme={null}
{
  "finish_reason": "stop",
  "message": {
    "role": "assistant",
    "content": "{\"CFO\": \"Spencer Neumann\", \"CEO\": \"Ted Sarandos and Greg Peters\"}"
  },
  "id": "0000000000000000680c95d2faab7aad",
  "model": "gpt-4o-2024-11-20",
  "usage": {
    "prompt_tokens": 14298,
    "completion_tokens": 42,
    "total_tokens": 14340
  },
  "citations": [
    {
      "position": 24,
      "references": [
        {
          "file": {
            "status": "Available",
            "id": "cbecaa37-2943-4030-b4d6-ce4350ab774a",
            "name": "Netflix-10-K-01262024.pdf",
            "size": 1073470,
            "metadata": {
              "test-key": "test-value"
            },
            "updated_on": "2025-01-24T16:53:17.148820770Z",
            "created_on": "2025-01-24T16:52:44.851577534Z",
            "percent_done": 1,
            "signed_url": "https://storage.googleapis.com/knowledge-prod-files/bf0dcf22...",
            "error_message": null
          },
          "pages": [
            79
          ],
          "highlight": null
        },
    ...
  ]
}
```


## Extract the response content

In the assistant's response, the message string is contained in the following JSON object:

* `message.content` for the default chat response
* `delta.content` for the streaming chat response
* `message.content` for the JSON response

You can extract the message content and print it to the console:

<Tabs>
  <Tab title="Default response">
    <CodeGroup>
      ```python Python theme={null}
      msg = Message(role="user", content="What is the maximum height of a red pine?")

      response = assistant.chat(messages=[msg])

      print(str(response.message.content))
      ```

      ```javascript JavaScript theme={null}
      const assistant = pc.Assistant(assistantName);
      const chatResp = await assistant.chat({
        messages: [{ role: 'user', content: 'What is the maximum height of a red pine?' }],
      });
      console.log(chatResp.message.content);
      ```

      ```bash curl theme={null}
      | jq '.message.content'
      ```
    </CodeGroup>

    This creates output like the following:

    ```bash  theme={null}
    A red pine, scientifically known as *Pinus resinosa*, is a medium-sized tree that can grow up to 25 meters high and 75 centimeters in diameter. [1, pp. 1]
    ```
  </Tab>

  <Tab title="Streaming response">
    <CodeGroup>
      ```python Python theme={null}
      msg = Message(role="user", content="What is the maximum height of a red pine?")

      response = assistant.chat(messages=[msg], stream=True)

      for data in response:
          if hasattr(data, "delta"):
              print(data.delta.content)
      ```

      ```bash curl theme={null}
      |  sed -u 's/.*"content":"\([^"]*\)".*/\1/'
      ```
    </CodeGroup>

    This creates output like the following:

    ```bash Streaming response theme={null}
    The
     maximum
     height
     of
     a
     red
     pine
     (
    Pin
    us
     resin
    osa
    )
     is
     up
     to
     twenty
    -five
     meters

     [1, pp. 1]
    .
    ```
  </Tab>

  <Tab title="JSON response">
    <CodeGroup>
      ```python Python theme={null}
      import json

      msg = Message(role="user", content="What is the maximum height of a red pine?")

      response = assistant.chat(messages=[msg], json_response=True)

      print(json.loads(response.message.content))
      ```

      ```bash curl theme={null}
      |  sed -u 's/.*"content":"\([^"]*\)".*/\1/'
      ```
    </CodeGroup>

    This creates output like the following:

    ```bash JSON response theme={null}
    {'red pine': 'A red pine, scientifically known as *Pinus resinosa*, is a medium-sized tree that can grow up to 25 meters high and 75 centimeters in diameter.'}
    ```
  </Tab>
</Tabs>


## Choose a model

Pinecone Assistant supports the following models:

* `gpt-4o` (default)
* `gpt-4.1`
* `o4-mini`
* `claude-3-5-sonnet`
* `claude-3-7-sonnet`
* `gemini-2.5-pro`

To choose a non-default model for your assistant, set the `model` parameter in the request:

<CodeGroup>
  ```python Python theme={null}
  # To use the Python SDK, install the plugin:
  # pip install --upgrade pinecone pinecone-plugin-assistant

  from pinecone import Pinecone
  from pinecone_plugins.assistant.models.chat import Message

  pc = Pinecone(api_key="YOUR_API_KEY")

  # Get your assistant.
  assistant = pc.assistant.Assistant(
      assistant_name="example-assistant", 
  )

  # Chat with the assistant.
  chat_context = [Message(role="user", content="What is the maximum height of a red pine?")]
  response = assistant.chat(
      messages=chat_context, 
      model="gpt-4.1"
  )
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  const assistantName = 'example-assistant';
  const assistant = pc.Assistant(assistantName);
  const chatResp = await assistant.chat({
    messages: [{ role: 'user', content: 'What is the maximum height of a red pine?' }],
    model: 'gpt-4.1',
  });

  console.log(chatResp);
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  ASSISTANT_NAME="example-assistant"

  curl "https://prod-1-data.ke.pinecone.io/assistant/chat/$ASSISTANT_NAME" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -H "X-Pinecone-API-Version: 2025-04" \
    -d '{
    "messages": [
      {
        "role": "user",
        "content": "What is the maximum height of a red pine?"
      }
    ],
    "model": "gpt-4.1"
  }'
  ```
</CodeGroup>


## Provide conversation history

Models lack memory of previous requests, so any relevant messages from earlier in the conversation must be present in the `messages` object.

In the following example, the `messages` object includes prior messages that are necessary for interpreting the newest message.

<CodeGroup>
  ```python Python theme={null}
  # To use the Python SDK, install the plugin:
  # pip install --upgrade pinecone pinecone-plugin-assistant

  from pinecone import Pinecone
  from pinecone_plugins.assistant.models.chat import Message

  pc = Pinecone(api_key="YOUR_API_KEY")

  # Get your assistant.
  assistant = pc.assistant.Assistant(
      assistant_name="example-assistant", 
  )

  # Chat with the assistant.
  chat_context = [
      Message(content="What is the maximum height of a red pine?", role="user"),
      Message(content="The maximum height of a red pine (Pinus resinosa) is up to 25 meters.", role="assistant"),
      Message(content="What is its maximum diameter?", role="user")
  ]
  response = assistant.chat(messages=chat_context)
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  ASSISTANT_NAME="example-assistant"

  curl "https://prod-1-data.ke.pinecone.io/assistant/chat/$ASSISTANT_NAME" \
    -H "Api-Key: $PINECONE_API_KEY " \
    -H "Content-Type: application/json" \
    -H "X-Pinecone-API-Version: 2025-04" \
    -d '{
    "messages": [
      {
        "role": "user",
        "content": "What is the maximum height of a red pine?"
      },
      {
        "role": "assistant",
        "content": "The maximum height of a red pine (Pinus resinosa) is up to 25 meters."
      },
      {
        "role": "user",
        "content": "What is its maximum diameter?"
      }
    ]
  }'
  ```
</CodeGroup>

The example returns a response like the following:

```JSON  theme={null}
{
  "finish_reason":"stop",
  "message":{
    "role":"assistant",
    "content":"The maximum diameter of a red pine (Pinus resinosa) is up to 1 meter."
    },
    "id":"0000000000000000236a24a17e55309a",
    "model":"gpt-4o-2024-05-13",
    "usage":{
      "prompt_tokens":21377,
      "completion_tokens":20,
      "total_tokens":21397
      },
      "citations":[...]
}
```


## Filter chat with metadata

You can [filter which documents to use for chat completions](/guides/assistant/files-overview#file-metadata). The following example filters the responses to use only documents that include the metadata `"resource": "encyclopedia"`.

<CodeGroup>
  ```python Python theme={null}
  # To use the Python SDK, install the plugin:
  # pip install --upgrade pinecone pinecone-plugin-assistant

  from pinecone import Pinecone
  from pinecone_plugins.assistant.models.chat import Message

  pc = Pinecone(api_key="YOUR_API_KEY")

  # Get your assistant.
  assistant = pc.assistant.Assistant(
      assistant_name="example-assistant", 
  )

  # Chat with the assistant.
  chat_context = [Message(role="user", content="What is the maximum height of a red pine?")]
  response = assistant.chat(messages=chat_context, stream=True, filter={"resource": "encyclopedia"})
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });
  const assistantName = 'example-assistant';
  const assistant = pc.Assistant(assistantName);
  const chatResp = await assistant.chat({
    messages: [{ role: 'user', content: 'What is the maximum height of a red pine?' }],
    filter: {
      'resource': 'encyclopedia'
    }
  });
  console.log(chatResp);
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  ASSISTANT_NAME="example-assistant"

  curl "https://prod-1-data.ke.pinecone.io/assistant/chat/$ASSISTANT_NAME" \
    -H "Api-Key: $PINECONE_API_KEY "\
    -H "Content-Type: application/json" \
    -H "X-Pinecone-API-Version: 2025-04" \
    -d '{
    "messages": [
      {
        "role": "user",
        "content": "What is the maximum height of a red pine?"
      }
    ],
    "stream": true,
    "filter": 
      {
      "resource": "encyclopedia"
      }
    }'
  ```
</CodeGroup>


## Control the context size

<Note>
  This is available in API versions `2025-04` and later.
</Note>

To limit the number of [input tokens](/guides/assistant/pricing-and-limits#token-usage) used, you can control the context size by tuning `top_k * snippet_size`. These parameters can be adjusted by setting [`context_options`](/reference/api/latest/assistant/chat_assistant#body-context-options) in the request:

* `snippet_size`: Controls the max size of a snippet (default is 2048 tokens). Note that snippet size can vary and, in rare cases, may be bigger than the set `snippet_size`. Snippet size controls the amount of context the model is given for each chunk of text.
* `top_k`: Controls the max number of context snippets sent to the LLM (default is 16). `top_k` controls the diversity of information sent to the model.

While additional tokens will be used for other parameters (e.g., the system prompt, chat input), adjusting the `top_k` and `snippet_size` can help manage token consumption.

<CodeGroup>
  ```python Python theme={null}
  # To use the Python SDK, install the plugin:
  # pip install --upgrade pinecone pinecone-plugin-assistant

  from pinecone import Pinecone
  from pinecone_plugins.assistant.models.chat import Message

  pc = Pinecone(api_key="YOUR_API_KEY")
  assistant = pc.assistant.Assistant(assistant_name="example-assistant")

  msg = Message(role="user", content="Who is the CFO of Netflix?")
  response = assistant.chat(messages=[msg], context_options={snippet_size=2500, top_k=10})

  print(response)
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  const assistantName = 'example-assistant';
  const assistant = pc.Assistant(assistantName);
  const chatResp = await assistant.chat({
    messages: [{ role: 'user', content: 'Who is the CFO of Netflix?' }],
    contextOptions: { topK: 10, snippetSize: 2500 },
  });

  console.log(chatResp);
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  ASSISTANT_NAME="example-assistant"

  curl "https://prod-1-data.ke.pinecone.io/assistant/chat/$ASSISTANT_NAME" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -H "X-Pinecone-API-Version: 2025-04" \
    -d '{
    "messages": [
      {
        "role": "user",
        "content": "Who is the CFO of Netflix?"
      }
    ],
    "context_options": {
      "top_k":10,
      "snippet_size":2500
      }
  }'
  ```
</CodeGroup>

The example will return up to 10 snippets and each snippet will be up to 2500 tokens in size.

<Tip>
  To better understand the context retrieved using these parameters, you can [retrieve context from an assistant](/reference/api/latest/assistant/context_assistant).
</Tip>


## Set the sampling temperature

<Note>
  This is available in API versions `2025-04` and later.
</Note>

Temperature is a parameter that controls the randomness of a model's predictions during text generation. Lower temperatures (\~0.0) yield more consistent, predictable answers, while higher temperatures increase the model's explanatory power and is generally better for creative tasks.

To control the sampling temperature for a model, set the `temperarture` parameter in the request. If a model does not support a temperature parameter, the parameter is ignored.

<CodeGroup>
  ```python Python theme={null}
  # To use the Python SDK, install the plugin:
  # pip install --upgrade pinecone pinecone-plugin-assistant

  from pinecone import Pinecone
  from pinecone_plugins.assistant.models.chat import Message

  pc = Pinecone(api_key="YOUR_API_KEY")
  assistant = pc.assistant.Assistant(assistant_name="example-assistant")

  msg = Message(role="user", content="Who is the CFO of Netflix?")
  response = assistant.chat(
      messages=[msg], 
      temperature=0.8
  )

  print(response)
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  const assistantName = 'example-assistant';
  const assistant = pc.Assistant(assistantName);
  const chatResp = await assistant.chat({
    messages: [{ role: 'user', content: 'Who is the CFO of Netflix?' }],
    temperature: 0.8,
  });
  console.log(chatResp);
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  ASSISTANT_NAME="example-assistant"

  curl "https://prod-1-data.ke.pinecone.io/assistant/chat/$ASSISTANT_NAME" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -H "X-Pinecone-API-Version: 2025-04" \
    -d '{
    "messages": [
      {
        "role": "user",
        "content": "Who is the CFO of Netflix?"
      }
    ],
    "temperature": 0.8
  }'
  ```
</CodeGroup>


## Include citation highlights in the response

<Note>
  Citation highlights are available in the [Pinecone console](https://app.pinecone.io/organizations/-/projects/-/assistant) or API versions `2025-04` and later.
</Note>

When using the [standard chat interface](/reference/api/latest/assistant/chat_assistant), every response includes a `citation` object. The object includes a reference to the document that the assistant used to generate the response. Additionally, you can include highlights, which are the specific parts of the document that the assistant used to generate the response, by setting the `include_highlights` parameter to `true` in the request:

```bash curl theme={null}
PINECONE_API_KEY="YOUR_API_KEY"
ASSISTANT_NAME="example-assistant"

curl "https://prod-1-data.ke.pinecone.io/assistant/chat/$ASSISTANT_NAME" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "Content-Type: application/json" \
  -H "X-Pinecone-API-Version: 2025-04" \
  -d '{
  "messages": [
    {
      "role": "user",
      "content": "Who is the CFO of Netflix?"
    }
  ],
  "stream": false,
  "model": "gpt-4o",
  "include_highlights": true
}'
```

The example returns response like the following:

```json  theme={null}
{
  "finish_reason":"stop",
  "message":{
    "role":"assistant",
    "content":"The Chief Financial Officer (CFO) of Netflix is Spencer Neumann."
    },
    "id":"00000000000000006685b07087b1ad42",
    "model":"gpt-4o-2024-05-13",
    "usage":{
      "prompt_tokens":12490,
      "completion_tokens":33,
      "total_tokens":12523
      },
      "citations":[{
        "position":63,
        "references":[{
          "file":{
            "status":"Available",
            "id":"cbecaa37-2943-4030-b4d6-ce4350ab774a",
            "name":"Netflix-10-K-01262024.pdf",
            "size":1073470,
            "metadata":{"test-key":"test-value"},
            "updated_on":"2025-01-24T16:53:17.148820770Z",
            "created_on":"2025-01-24T16:52:44.851577534Z",
            "percent_done":1.0,
            "signed_url":"https://storage.googleapis.com/knowledge-prod-files/b...",
            "error_message":null
            },
            "pages":[78],
            "highlight":{
              "type":"text",
              "content":"EXHIBIT 31.3\nCERTIFICATION OF CHIEF FINANCIAL OFFICER\nPURSUANT TO SECTION 302 OF THE SARBANES-OXLEY ACT OF 2002\nI, Spencer Neumann, certify that:"
              }
            },
            {
              "file":{
                "status":"Available",
                "id":"cbecaa37-2943-4030-b4d6-ce4350ab774a",
                "name":"Netflix-10-K-01262024.pdf",
                "size":1073470,
                "metadata":{"test-key":"test-value"},
                "updated_on":"2025-01-24T16:53:17.148820770Z",
                "created_on":"2025-01-24T16:52:44.851577534Z",
                "percent_done":1.0,
                "signed_url":"https://storage.googleapis.com/knowledge-prod-files/bf...",
                "error_message":null
                },
                "pages":[79],
                "highlight":{
                  "type":"text",
                  "content":"operations of\nNetflix, Inc.\nDated: January 26, 2024  By:  /S/ SPENCER NEUMANN\n  Spencer Neumann\n  Chief Financial Officer"
                }
            }
          ]
        }
      ]
}
```

<Note>
  Enabling highlights will increase token usage.
</Note>



# Context snippets overview
Source: https://docs.pinecone.io/guides/assistant/context-snippets-overview

Retrieve context snippets from your assistant's knowledge base.

You can [retrieve the context snippets](/guides/assistant/retrieve-context-snippets) that Pinecone Assistant uses to generate its responses. This data includes relevant chunks, relevancy scores, and references.


## Use cases

Retrieving context snippets is useful for performing tasks like the following:

* Understanding what relevant data snippets Pinecone Assistant is providing to the LLM for chat generation.
* Using the retrieved snippets with your own LLM.
* Using the retrieved snippets with your own RAG application or agentic workflow.


## SDK support

The Pinecone [Python SDK](/reference/python-sdk) and [Node.js SDK](/reference/node-sdk) provide convenient programmatic access to [retrieve context snippets](/reference/api/latest/assistant/context_assistant).


## Pricing

Context retrieval usage is [measured in tokens](/guides/assistant/pricing-and-limits#token-usage), similar to Pinecone Assistant. See [Pricing](https://www.pinecone.io/pricing/) for up-to-date pricing information.

<Note>
  Pricing updates specific to context retrieval will be made as the feature becomes generally available.
</Note>



# Create an assistant
Source: https://docs.pinecone.io/guides/assistant/create-assistant

Create and deploy a Pinecone Assistant for your knowledge base.

This page shows you how to create an [assistant](/guides/assistant/overview).

You can [create an assistant](/reference/api/latest/assistant/create_assistant), as in the following example:

<CodeGroup>
  ```python Python theme={null}
  # To use the Python SDK, install the plugin:
  # pip install --upgrade pinecone pinecone-plugin-assistant

  from pinecone import Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  assistant = pc.assistant.create_assistant(
      assistant_name="example-assistant", 
      instructions="Use American English for spelling and grammar.", # Description or directive for the assistant to apply to all responses.
      region="us", # Region to deploy assistant. Options: "us" (default) or "eu".
      timeout=30 # Maximum seconds to wait for assistant status to become "Ready" before timing out.
  )
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  const assistant = await pc.createAssistant({
    name: 'example-assistant',
    instructions: 'Use American English for spelling and grammar.',
    region: 'us'
  });
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl "https://api.pinecone.io/assistant/assistants" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
    "name": "example-assistant",
    "instructions": "Use American English for spelling and grammar.",
    "region":"us"
  }'
  ```
</CodeGroup>

<Tip>
  You can create an assistant using the [Pinecone console](https://app.pinecone.io/organizations/-/projects/-/assistant/-/files).
</Tip>



# Evaluate answers
Source: https://docs.pinecone.io/guides/assistant/evaluate-answers

Measure assistant response quality with LLM-based evaluation.

This page shows you how to [evaluate responses](/guides/assistant/evaluation-overview) from an assistant or other RAG systems using the `metrics_alignment` operation.

You can [evaluate a response](/reference/api/latest/assistant/metrics_alignment) from an assistant, as in the following example:

<CodeGroup>
  ```python Python theme={null}
  # To use the Python SDK, install the plugin:
  # pip install --upgrade pinecone pinecone-plugin-assistant
  # pip install requests

  import requests
  from pinecone_plugins.assistant.models.chat import Message

  payload = {
      "question": "What are the capital cities of France, England and Spain?", # Question to ask the assistant.
      "answer": "Paris is the capital city of France and Barcelona of Spain", # Answer from the assistant.
      "ground_truth_answer": "Paris is the capital city of France, London of England and Madrid of Spain." # Expected answer to evaluate the assistant's response.
  }

  headers = {
      "Api-Key": "YOUR_API_KEY",
      "Content-Type": "application/json"
  }

  url = "https://prod-1-data.ke.pinecone.io/assistant/evaluation/metrics/alignment"

  response = requests.request("POST", url, json=payload, headers=headers)

  print(response.text)
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl "https://prod-1-data.ke.pinecone.io/assistant/evaluation/metrics/alignment" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
    "question": "What are the capital cities of France, England and Spain?",
    "answer": "Paris is the capital city of France and Barcelona of Spain",
    "ground_truth_answer": "Paris is the capital city of France, London of England and Madrid of Spain"
  }'
  ```
</CodeGroup>

```json Response theme={null}
{
  "metrics": {
    "correctness": 0.5,
    "completeness": 0.3333,
    "alignment": 0.4
  },
  "reasoning": {
    "evaluated_facts": [
      {
        "fact": {
          "content": "Paris is the capital city of France."
        },
        "entailment": "entailed"
      },
      {
        "fact": {
          "content": "London is the capital city of England."
        },
        "entailment": "neutral"
      },
      {
        "fact": {
          "content": "Madrid is the capital city of Spain."
        },
        "entailment": "contradicted"
      }
    ]
  },
  "usage": {
    "prompt_tokens": 1223,
    "completion_tokens": 51,
    "total_tokens": 1274
  }
}
```



# Evaluation overview
Source: https://docs.pinecone.io/guides/assistant/evaluation-overview

Learn about evaluating the correctness and completeness of assistant responses.

You can [evaluate the correctness and completeness of a response](/guides/assistant/evaluate-answers) from an assistant or RAG system.


## Use cases

Response evaluation is useful when performing tasks like the following:

* Understanding how well the Pinecone Assistant captures the facts of the ground truth answer.
* Comparing the Pinecone Assistant's answers to those of another RAG system.
* Comparing the answers of your own RAG system to those of the Pinecone Assistant or another RAG system.


## SDK support

You can [evaluate responses](/reference/api/latest/assistant/metrics_alignment) directly or through the [Pinecone Python SDK](/reference/python-sdk).


## Request

The request body requires the following fields:

| Field                 | Description                                           |
| --------------------- | ----------------------------------------------------- |
| `question`            | The question asked to the RAG system.                 |
| `answer`              | The answer provided by the assistant being evaluated. |
| `ground_truth_answer` | The expected answer.                                  |

For example:

```json  theme={null}
{
  "question": "What are the capital cities of France, England and Spain?",
  "answer": "Paris is the capital city of France and Barcelona of Spain",
  "ground_truth_answer": "Paris is the capital city of France, London of England and Madrid of Spain."
}
```


## Response

### Metrics

Calculated scores between `0` to `1` are returned for the following metrics:

| Metric         | Description                                                                  |
| -------------- | ---------------------------------------------------------------------------- |
| `correctness`  | Correctness of the RAG system's answer compared to the ground truth answer.  |
| `completeness` | Completeness of the RAG system's answer compared to the ground truth answer. |
| `alignment`    | A combined score of the correctness and completeness scores.                 |

```json  theme={null}
{
  "metrics": {
    "correctness": 0.5,
    "completeness": 0.333,
    "alignment": 0.398,
  }
},

...
```

### Reasoning

The response includes explanations for the reasoning behind each metric's score. This includes a list of evaluated facts with their entailment status:

| Status         | Description                                                                |
| -------------- | -------------------------------------------------------------------------- |
| `entailed`     | The fact is supported by the ground truth answer.                          |
| `contradicted` | The fact contradicts the ground truth answer.                              |
| `neutral`      | The fact is neither supported nor contradicted by the ground truth answer. |

```json  theme={null}
...

  "reasoning":{
    "evaluated_facts": [
      {
        "fact": {"content": "Paris is the capital of France"},
        "entailment": "entailed",
      },
      {
        "fact": {"content": "London is the capital of England"},
        "entailment": "neutral"
      },
      {
        "fact": {"content": "Madrid is the capital of Spain"},
        "entailment": "contradicted",
      }
    ]
  },

...
```

### Usage

The response includes the number of tokens used to calculate the metrics. This includes the number of tokens used for the prompt and completion.

```json  theme={null}
...

  "usage": {
    "prompt_tokens": 22,
    "completion_tokens": 33,
    "total_tokens": 55
  }
}
```


## Pricing

Cost is calculated by [token usage](#usage). See [Pricing](https://www.pinecone.io/pricing/) for up-to-date pricing information.

Response evaluation is only available for [Standard and Enterprise plans](https://www.pinecone.io/pricing/).



# Files in Pinecone Assistant
Source: https://docs.pinecone.io/guides/assistant/files-overview

Understand supported file types and metadata in Pinecone Assistant.

export const word_0 = "files"

Before you can chat with the assistant, you need to [upload files](/guides/assistant/manage-files#upload-a-local-file). The files provide your assistant with context and information to reference when generating responses. Files are not shared across assistants.

### Supported file types

Pinecone Assistant supports the following file types:

* DOCX (.docx)
* JSON (.json)
* Markdown (.md)
* PDF (.pdf)
* Text (.txt)

<Note>
  For PDF files, assistants support [multimodal context](/guides/assistant/multimodal), allowing them to analyze and gather context from images. This feature is in [public preview](/release-notes/feature-availability).
</Note>

For information about file size and storage limits, see [Pricing and limits](/guides/assistant/pricing-and-limits).

### File storage

Files are uploaded to Google Cloud Storage (`us-central1` region) and to your organization's Pinecone vector database. The assistant processes the files, so data is not sent outside of blob storage or Pinecone.

Some API responses include a `signed_url` field, which provides temporary, read-only access to one of the assistant's files. The URL is [signed](https://cloud.google.com/storage/docs/access-control/signed-urls) and hard to guess, but publicly accessible, so treat it as sensitive. `signed_url` links expire in one hour.

### File metadata

You can [upload a file with metadata](/guides/assistant/manage-files#upload-a-file-with-metadata), which allows you to store additional information about the file as key-value pairs.

<Warning>
  File metadata can be set only when the file is uploaded. You cannot update metadata after the file is uploaded.
</Warning>

File metadata can be used for the following purposes:

* [Filtering chat responses](/guides/assistant/chat-with-assistant#filter-chat-with-metadata): Specify filters on assistant responses so only files that match the metadata filter are referenced in the response. Chat requests without metadata filters do not consider metadata.
* [Viewing a filtered list of files](/guides/assistant/manage-files#view-a-filtered-list-of-files): Use metadata filters to list files in an assistant that match specific criteria.

#### Supported metadata size and format

Pinecone Assistant supports 16 KB of metadata per file.

* Metadata fields must be key-value pairs in a flat JSON object. Nested JSON objects are not supported.
* Keys must be strings and must not start with a `$`.
* Values must be one of the following data types:
  * String
  * Integer (converted to a 64-bit floating point by Pinecone)
  * Floating point
  * Boolean (`true`, `false`)
  * List of strings
* Null metadata values aren't supported. Instead of setting a key to `null`, remove the key from the metadata payload.

**Examples**

<CodeGroup>
  ```json Valid metadata theme={null}
  {
    "document_id": "document1",
    "document_title": "Introduction to Vector Databases",
    "chunk_number": 1,
    "chunk_text": "First chunk of the document content...",
    "is_public": true,
    "tags": ["beginner", "database", "vector-db"],
    "scores": ["85", "92"]
  }
  ```

  ```json Invalid metadata theme={null}
  {
    "document": {       // Nested JSON objects are not supported
      "document_id": "document1",
      "document_title": "Introduction to Vector Databases",
    },
    "$chunk_number": 1, // Keys must not start with a `$`
    "chunk_text": null, // Null values are not supported
    "is_public": true,
    "tags": ["beginner", "database", "vector-db"],
    "scores": [85, 92]  // Lists of non-strings are not supported
  }
  ```
</CodeGroup>

#### Metadata query language

Pinecone's filtering language supports the following operators:

| Operator  | Function                                                                                                                           | Supported types         |
| :-------- | :--------------------------------------------------------------------------------------------------------------------------------- | :---------------------- |
| `$eq`     | Matches {word_0} with metadata values that are equal to a specified value. Example: `{"genre": {"$eq": "documentary"}}`            | Number, string, boolean |
| `$ne`     | Matches {word_0} with metadata values that are not equal to a specified value. Example: `{"genre": {"$ne": "drama"}}`              | Number, string, boolean |
| `$gt`     | Matches {word_0} with metadata values that are greater than a specified value. Example: `{"year": {"$gt": 2019}}`                  | Number                  |
| `$gte`    | Matches {word_0} with metadata values that are greater than or equal to a specified value. Example:`{"year": {"$gte": 2020}}`      | Number                  |
| `$lt`     | Matches {word_0} with metadata values that are less than a specified value. Example: `{"year": {"$lt": 2020}}`                     | Number                  |
| `$lte`    | Matches {word_0} with metadata values that are less than or equal to a specified value. Example: `{"year": {"$lte": 2020}}`        | Number                  |
| `$in`     | Matches {word_0} with metadata values that are in a specified array. Example: `{"genre": {"$in": ["comedy", "documentary"]}}`      | String, number          |
| `$nin`    | Matches {word_0} with metadata values that are not in a specified array. Example: `{"genre": {"$nin": ["comedy", "documentary"]}}` | String, number          |
| `$exists` | Matches {word_0} with the specified metadata field. Example: `{"genre": {"$exists": true}}`                                        | Number, string, boolean |
| `$and`    | Joins query clauses with a logical `AND`. Example: `{"$and": [{"genre": {"$eq": "drama"}}, {"year": {"$gte": 2020}}]}`             | -                       |
| `$or`     | Joins query clauses with a logical `OR`. Example: `{"$or": [{"genre": {"$eq": "drama"}}, {"year": {"$gte": 2020}}]}`               | -                       |

<Note>
  Only `$and` and `$or` are allowed at the top level of the query expression.
</Note>

For example, the following has a `"genre"` metadata field with a list of strings:

```JSON JSON theme={null}
{ "genre": ["comedy", "documentary"] }
```

This means `"genre"` takes on both values, and requests with the following filters will match:

```JSON JSON theme={null}
{"genre":"comedy"}

{"genre": {"$in":["documentary","action"]}}

{"$and": [{"genre": "comedy"}, {"genre":"documentary"}]}
```

However, requests with the following filter will **not** match:

```JSON JSON theme={null}
{ "$and": [{ "genre": "comedy" }, { "genre": "drama" }] }
```

Additionally, requests with the following filters will **not** match because they are invalid. They will result in a compilation error:

```json JSON theme={null}

# INVALID QUERY:
{"genre": ["comedy", "documentary"]}
```

```json JSON theme={null}

# INVALID QUERY:
{"genre": {"$eq": ["comedy", "documentary"]}}
```



# Manage assistants
Source: https://docs.pinecone.io/guides/assistant/manage-assistants

View, update, and delete, and check the status of assistants.


## List assistants for a project

You can [get the name, status, and metadata for each assistant](/reference/api/latest/assistant/list_assistants) in your project as in the following example:

<CodeGroup>
  ```python Python theme={null}
  # To use the Python SDK, install the plugin:
  # pip install --upgrade pinecone pinecone-plugin-assistant

  from pinecone import Pinecone
  pc = Pinecone(api_key="YOUR_API_KEY")

  assistants = pc.assistant.list_assistants()
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  const assistants = await pc.listAssistants();
  console.log(assistants);
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl -X GET "https://api.pinecone.io/assistant/assistants" \
    -H "Api-Key: $PINECONE_API_KEY"
  ```
</CodeGroup>

This operation returns a response like the following:

```JSON  theme={null}
{
  "assistants": [
    {
      "name": "example-assistant",
      "instructions": "Use American English for spelling and grammar.",
      "metadata": {},
      "status": "Initializing",
      "created_on": "2023-11-07T05:31:56Z",
      "updated_on": "2023-11-07T05:31:56Z"
    }
  ]
}
```

You can use the `name` value to [check the status of an assistant](/guides/assistant/manage-assistants#get-the-status-of-an-assistant).

<Tip>
  You can list assistants using the [Pinecone console](https://app.pinecone.io/organizations/-/projects/-/assistant/-/files).
</Tip>


## Get the status of an assistant

You can [get the status and metadata for your assistant](/reference/api/latest/assistant/describe_assistant) as in the following example:

<CodeGroup>
  ```python Python theme={null}
  # To use the Python SDK, install the plugin:
  # pip install --upgrade pinecone pinecone-plugin-assistant

  from pinecone import Pinecone
  pc = Pinecone(api_key="YOUR_API_KEY")

  assistant = pc.assistant.describe_assistant(
      assistant_name="example-assistant", 
  )
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  const assistant = await pc.describeAssistant('example-assistant');
  console.log(assistant);
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  ASSISTANT_NAME="example-assistant"

  curl -X GET "https://api.pinecone.io/assistant/assistants/$ASSISTANT_NAME" \
    -H "Api-Key: $PINECONE_API_KEY"
  ```
</CodeGroup>

This operation returns a response like the following:

```JSON  theme={null}
{
  "name": "example-assistant",
  "instructions": "Use American English for spelling and grammar.",
  "metadata": {},
  "status": "Initializing",
  "created_on": "2023-11-07T05:31:56Z",
  "updated_on": "2023-11-07T05:31:56Z"
}
```

The `status` field has the following possible values:

* Initializing
* Failed
* Ready
* Terminating

<Tip>
  You can check the status of an assistant using the [Pinecone console](https://app.pinecone.io/organizations/-/projects/-/assistant).
</Tip>


## Change an assistant's chat model

The chat model is the underlying large language model (LLM) that powers the assistant's responses. You can change the chat model for an existing assistant through the [Pinecone console](https://app.pinecone.io/organizations/-/projects/-/assistant):

1. On the **Assistants** page, select the assistant you want to update.
2. In the sidebar on the right, select **Settings** (gear icon).
3. Select the **Chat model**.


## Add instructions to an assistant

You can [add or update the instructions](/reference/api/latest/assistant/update_assistant) for an existing assistant. Instructions are a short description or directive for the assistant to apply to all of its responses. For example, you can update the instructions to reflect the assistant's role or purpose.

For example:

<CodeGroup>
  ```python Python theme={null}
  # To use the Python SDK, install the plugin:
  # pip install --upgrade pinecone pinecone-plugin-assistant

  from pinecone import Pinecone

  pc = Pinecone(api_key=YOUR_API_KEY)

  assistant = pc.assistant.update_assistant(
      assistant_name="example-assistant", 
      instructions="Use American English for spelling and grammar.",
      region="us" # Region to deploy assistant. Options: "us" (default) or "eu".
  )
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  await pc.updateAssistant('example-assistant', {
    instructions: 'Use American English for spelling and grammar.',
  });
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl -X PATCH "https://api.pinecone.io/assistant/assistants/example-assistant" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
    "instructions": "Use American English for spelling and grammar.",
    "metadata": {"updated": "2024-09-30"},
    "region": "us"
  }'
  ```
</CodeGroup>

The example above returns a result like the following:

```JSON  theme={null}
{
    "name":"example-assistant",
    "instructions":"Use American English for spelling and grammar.",
    "metadata":{"updated":"2024-09-30"},
    "status":"Ready",
    "created_at":"2024-06-14T14:58:06.573004549Z",
    "updated_at":"2024-10-01T19:44:32.813235817Z"
}
```

<Tip>
  You can add or update instructions for an assistant using the [Pinecone console](https://app.pinecone.io/organizations/-/projects/-/assistant).
</Tip>


## Delete an assistant

You can [delete an assistant](/reference/api/latest/assistant/delete_assistant) as in the following example:

<Warning>
  Deleting an assistant also deletes all files uploaded to the assistant.
</Warning>

<CodeGroup>
  ```python Python theme={null}
  # To use the Python SDK, install the plugin:
  # pip install --upgrade pinecone pinecone-plugin-assistant

  from pinecone import Pinecone
  pc = Pinecone(api_key="YOUR_API_KEY")

  pc.assistant.delete_assistant(
      assistant_name="example-assistant", 
  )
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  await pc.deleteAssistant('example-assistant');
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  ASSISTANT_NAME="example-assistant"

  curl -X DELETE "https://api.pinecone.io/assistant/assistants/$ASSISTANT_NAME" \
    -H "Api-Key: $PINECONE_API_KEY"
  ```
</CodeGroup>

<Tip>
  You can delete an assistant using the [Pinecone console](https://app.pinecone.io/organizations/-/projects/-/assistant).
</Tip>



# Manage files
Source: https://docs.pinecone.io/guides/assistant/manage-files

List, check status, and delete files from your assistant.

<Note>
  File upload limitations depend on the plan you are using. For more information, see [Pricing and limitations](/guides/assistant/pricing-and-limits#limits).
</Note>


## List files in an assistant

### View all files

You can [get the status, ID, and metadata for each file in your assistant](/reference/api/latest/assistant/list_files), as in the following example:

<CodeGroup>
  ```python Python theme={null}
  # To use the Python SDK, install the plugin:
  # pip install --upgrade pinecone pinecone-plugin-assistant

  from pinecone import Pinecone
  pc = Pinecone(api_key="YOUR_API_KEY")

  # Get your assistant.
  assistant = pc.assistant.Assistant(
      assistant_name="example-assistant", 
  )

  # List files in your assistant.
  files = assistant.list_files()
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  const assistantName = 'example-assistant';
  const assistant = pc.Assistant(assistantName);
  const files = await assistant.listFiles();
  console.log(files);
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  ASSISTANT_NAME="example-assistant"

  curl -X GET "https://prod-1-data.ke.pinecone.io/assistant/files/$ASSISTANT_NAME" \
    -H "Api-Key: $PINECONE_API_KEY"
  ```
</CodeGroup>

This operation returns a response like the following:

```JSON  theme={null}
{
  "files": [
    {
      "status": "Available",
      "id": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
      "name": "example_file.txt",
      "size": 1073470,
      "metadata": {},
      "updated_on": "2025-07-16T16:46:40.787204651Z",
      "created_on": "2025-07-16T16:45:59.414273474Z",
      "percent_done": 1.0,
      "signed_url": null,
      "error_message": null
    }
  ]
}
```

You can use the `id` value to [check the status of an individual file](#get-the-status-of-a-file).

<Tip>
  You can list file in an assistant using the [Pinecone console](https://app.pinecone.io/organizations/-/projects/-/assistant). Select the assistant and view the files in the Assistant playground.
</Tip>

### View a filtered list of files

Metadata filter expressions can be included when listing files. This will limit the list of files to only those matching the filter expression. Use the `filter` parameter to specify the metadata filter expression.

For more information about filtering with metadata, see [Understanding files](/guides/assistant/files-overview#metadata-query-language).

The following example lists files that are a manuscript:

<CodeGroup>
  ```Python Python theme={null}
  # To use the Python SDK, install the plugin:
  # pip install --upgrade pinecone pinecone-plugin-assistant

  from pinecone import Pinecone
  pc = Pinecone(api_key="YOUR_API_KEY")

  # Get your assistant.
  assistant = pc.assistant.Assistant(
      assistant_name="example-assistant", 
  )

  # List files in your assistant that match the metadata filter.
  files = assistant.list_files(filter={"document_type":"manuscript"})
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  const assistantName = 'example-assistant';
  const assistant = pc.Assistant(assistantName);
  const files = await assistant.listFiles({
    filter: { document_type: 'manuscript' },
  });
  console.log(files);

  // You can also use filter operators:
  // const files = await assistant.listFiles({
  //   filter: { document_type: { '$ne': 'manuscript' } },
  // });
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  ASSISTANT_NAME="example-assistant"
  ENCODED_METADATA="%7B%22document_type%22%3A%20%22manuscript%22%7D" # URL encoded metadata - See w3schools.com/tags/ref_urlencode.ASP

  curl -X GET "https://prod-1-data.ke.pinecone.io/assistant/files/$ASSISTANT_NAME?filter=$ENCODED_METADATA" \
    -H "Api-Key: $PINECONE_API_KEY"
  ```
</CodeGroup>


## Get the status of a file

You can [get the status and metadata for your assistant](/reference/api/latest/assistant/describe_file), as in the following example:

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

  # Describe a file. 
  # To get a signed URL in the response, set `include_url` to `True`.
  file = assistant.describe_file(file_id="3c90c3cc-0d44-4b50-8888-8dd25736052a", include_url=True)
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  const assistantName = 'example-assistant';
  const assistant = pc.Assistant(assistantName);
  const fileId = "3c90c3cc-0d44-4b50-8888-8dd25736052a";

  // Describe a file. Returns a signed URL by default. 
  const file = await assistant.describeFile(fileId)
  // To exclude signed URL, set `includeUrl` to `false`.
  // const includeUrl = false;
  // const file = await assistant.describeFile(fileId, includeUrl)
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  ASSISTANT_NAME="example-assistant"
  FILE_ID="3c90c3cc-0d44-4b50-8888-8dd25736052a"

  # Describe a file. 
  # To get a signed URL in the response, set `include_url` to `true`.
  curl -X GET "https://prod-1-data.ke.pinecone.io/assistant/files/$ASSISTANT_NAME/$FILE_ID?include_url=true" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-API-Version: 2025-04"
  ```
</CodeGroup>

This operation returns a response like the following:

```JSON  theme={null}
{
  "status": "Available",
  "id": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
  "name": "example_file.txt",
  "size": 1073470,
  "metadata": {},
  "updated_on": "2025-07-16T16:46:40.787204651Z",
  "created_on": "2025-07-16T16:45:59.414273474Z",
  "percent_done": 1.0,
  "signed_url": "https://storage.googleapis.com/...",
  "error_message": null
}                          
```

<Warning>
  [`signed_url`](https://cloud.google.com/storage/docs/access-control/signed-urls) provides temporary, read-only access to the relevant file. Anyone with the link can access the file, so treat it as sensitive data. Expires in one hour.
</Warning>

<Tip>
  You can check the status a file using the [Pinecone console](https://app.pinecone.io/organizations/-/projects/-/assistant). In the Assistant playground, click the file for more details.
</Tip>


## Delete a file

You can [delete a file](/reference/api/latest/assistant/delete_file) from an assistant.

<Warning>Once a file is deleted, you cannot recover it.</Warning>

<CodeGroup>
  ```python Python theme={null}
  # To use the Python SDK, install the plugin:
  # pip install --upgrade pinecone pinecone-plugin-assistant

  from pinecone import Pinecone
  pc = Pinecone(api_key="YOUR_API_KEY")

  # Get your assistant.
  assistant = pc.assistant.Assistant(
      assistant_name="example-assistant", 
  )

  # Delete a file from your assistant.
  assistant.delete_file(file_id="3c90c3cc-0d44-4b50-8888-8dd25736052a")
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  const assistantName = 'example-assistant';
  const assistant = pc.Assistant(assistantName);

  const file = await assistant.deleteFile("070513b3-022f-4966-b583-a9b12e0290ff")
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  ASSISTANT_NAME="example-assistant"
  FILE_ID="3c90c3cc-0d44-4b50-8888-8dd25736052a"

  curl -X DELETE "https://prod-1-data.ke.pinecone.io/assistant/files/$ASSISTANT_NAME/$FILE_ID" \
    -H "Api-Key: $PINECONE_API_KEY"
  ```
</CodeGroup>

<Tip>
  You can delete a file from an assistant using the [Pinecone console](https://app.pinecone.io/organizations/-/projects/-/assistant). In the Assistant playground, find the file and click the **ellipsis (...) menu > Delete**.
</Tip>



---
**Navigation:** [← Previous](./28-download-a-usage-report.md) | [Index](./index.md) | [Next →](./30-use-an-assistant-mcp-server.md)
