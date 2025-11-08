**Navigation:** [← Previous](./14-batch-calling.md) | [Index](./index.md) | [Next →](./16-chat-mode.md)

# Client to server events

> Send contextual information from the client to enhance conversational applications in real-time.

**Client-to-server events** are messages that your application proactively sends to the server to provide additional context during conversations. These events enable you to enhance the conversation with relevant information without interrupting the conversational flow.

<Note>
  For information on events the server sends to the client, see the [Client
  events](/docs/agents-platform/customization/events/client-events) documentation.
</Note>


## Overview

Your application can send contextual information to the server to improve conversation quality and relevance at any point during the conversation. This does not have to be in response to a client event received from the server. This is particularly useful for sharing UI state, user actions, or other environmental data that may not be directly communicated through voice.

<Info>
  While our SDKs provide helper methods for sending these events, understanding the underlying
  protocol is valuable for custom implementations and advanced use cases.
</Info>


## Event types

### Contextual updates

Contextual updates allow your application to send non-interrupting background information to the conversation.

**Key characteristics:**

* Updates are incorporated as background information in the conversation.
* Does not interrupt the current conversation flow.
* Useful for sending UI state, user actions, or environmental data.

```javascript
// Contextual update event structure
{
  "type": "contextual_update",
  "text": "User appears to be looking at pricing page"
}
```

```javascript
// Example sending contextual updates
function sendContextUpdate(information) {
  websocket.send(
    JSON.stringify({
      type: 'contextual_update',
      text: information,
    })
  );
}

// Usage examples
sendContextUpdate('Customer status: Premium tier');
sendContextUpdate('User navigated to Help section');
sendContextUpdate('Shopping cart contains 3 items');
```

### User messages

User messages allow you to send text directly to the conversation as if the user had spoken it. This is useful for text-based interactions or when you want to inject specific text into the conversation flow.

**Key characteristics:**

* Text is processed as user input to the conversation.
* Triggers the same response flow as spoken user input.
* Useful for text-based interfaces or programmatic user input.

```javascript
// User message event structure
{
  "type": "user_message",
  "text": "I would like to upgrade my account"
}
```

```javascript
// Example sending user messages
function sendUserMessage(text) {
  websocket.send(
    JSON.stringify({
      type: 'user_message',
      text: text,
    })
  );
}

// Usage examples
sendUserMessage('I need help with billing');
sendUserMessage('What are your pricing options?');
sendUserMessage('Cancel my subscription');
```

### User activity

User activity events serve as indicators to prevent interrupts from the agent.

**Key characteristics:**

* Resets the turn timeout timer.
* Does not affect conversation content or flow.
* Useful for maintaining long-running conversations during periods of silence.

```javascript
// User activity event structure
{
  "type": "user_activity"
}
```

```javascript
// Example sending user activity
function sendUserActivity() {
  websocket.send(
    JSON.stringify({
      type: 'user_activity',
    })
  );
}

// Usage example - send activity ping every 30 seconds
setInterval(sendUserActivity, 30000);
```


## Best practices

1. **Contextual updates**

   * Send relevant but concise contextual information.
   * Avoid overwhelming the LLM with too many updates.
   * Focus on information that impacts the conversation flow or is important context from activity in a UI not accessible to the voice agent.

2. **User messages**

   * Use for text-based user input when audio is not available or appropriate.
   * Ensure text content is clear and well-formatted.
   * Consider the conversation context when injecting programmatic messages.

3. **User activity**

   * Send activity pings during periods of user interaction to maintain session.
   * Use reasonable intervals (e.g., 30-60 seconds) to avoid unnecessary network traffic.
   * Implement activity detection based on actual user engagement (mouse movement, typing, etc.).

4. **Timing considerations**

   * Send updates at appropriate moments.
   * Consider grouping multiple contextual updates into a single update (instead of sending every small change separately).
   * Balance between keeping the session alive and avoiding excessive messaging.

<Info>
  For detailed implementation examples, check our [SDK
  documentation](/docs/agents-platform/libraries/python).
</Info>



# Integrate your own model

> Connect an agent to your own LLM or host your own server.

<Note>
  Custom LLM allows you to connect your conversations to your own LLM via an external endpoint.
  ElevenLabs also supports [natively integrated LLMs](/docs/agents-platform/customization/llm)
</Note>

**Custom LLMs** let you bring your own OpenAI API key or run an entirely custom LLM server.


## Overview

By default, we use our own internal credentials for popular models like OpenAI. To use a custom LLM server, it must align with the OpenAI [create chat completion](https://platform.openai.com/docs/api-reference/chat/create) request/response structure.

The following guides cover both use cases:

1. **Bring your own OpenAI key**: Use your own OpenAI API key with our platform.
2. **Custom LLM server**: Host and connect your own LLM server implementation.

You'll learn how to:

* Store your OpenAI API key in ElevenLabs
* host a server that replicates OpenAI's [create chat completion](https://platform.openai.com/docs/api-reference/chat/create) endpoint
* Direct ElevenLabs to your custom endpoint
* Pass extra parameters to your LLM as needed

<br />


## Using your own OpenAI key

To integrate a custom OpenAI key, create a secret containing your OPENAI\_API\_KEY:

<Steps>
  <Step>
    Navigate to the "Secrets" page and select "Add Secret"

    <Frame background="subtle">
      ![Add Secret](file:4b23d52f-e527-45f0-aeef-a76fc3026b54)
    </Frame>
  </Step>

  <Step>
    Choose "Custom LLM" from the dropdown menu.

    <Frame background="subtle">
      ![Choose custom llm](file:5871b388-8f5b-4896-b4cb-3c0f541bbf53)
    </Frame>
  </Step>

  <Step>
    Enter the URL, your model, and the secret you created.

    <Frame background="subtle">
      ![Enter url](file:db1a7a97-b9d6-47b3-8530-e3b171af0683)
    </Frame>
  </Step>

  <Step>
    Set "Custom LLM extra body" to true.

    <Frame background="subtle">
      ![](file:38623647-8ef8-4369-ab3d-987706bddad3)
    </Frame>
  </Step>
</Steps>


## Custom LLM Server

To bring a custom LLM server, set up a compatible server endpoint using OpenAI's style, specifically targeting create\_chat\_completion.

Here's an example server implementation using FastAPI and OpenAI's Python SDK:

```python
import json
import os
import fastapi
from fastapi.responses import StreamingResponse
from openai import AsyncOpenAI
import uvicorn
import logging
from dotenv import load_dotenv
from pydantic import BaseModel
from typing import List, Optional


# Load environment variables from .env file
load_dotenv()


# Retrieve API key from environment
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY not found in environment variables")

app = fastapi.FastAPI()
oai_client = AsyncOpenAI(api_key=OPENAI_API_KEY)

class Message(BaseModel):
    role: str
    content: str

class ChatCompletionRequest(BaseModel):
    messages: List[Message]
    model: str
    temperature: Optional[float] = 0.7
    max_tokens: Optional[int] = None
    stream: Optional[bool] = False
    user_id: Optional[str] = None

@app.post("/v1/chat/completions")
async def create_chat_completion(request: ChatCompletionRequest) -> StreamingResponse:
    oai_request = request.dict(exclude_none=True)
    if "user_id" in oai_request:
        oai_request["user"] = oai_request.pop("user_id")

    chat_completion_coroutine = await oai_client.chat.completions.create(**oai_request)

    async def event_stream():
        try:
            async for chunk in chat_completion_coroutine:
                # Convert the ChatCompletionChunk to a dictionary before JSON serialization
                chunk_dict = chunk.model_dump()
                yield f"data: {json.dumps(chunk_dict)}\n\n"
            yield "data: [DONE]\n\n"
        except Exception as e:
            logging.error("An error occurred: %s", str(e))
            yield f"data: {json.dumps({'error': 'Internal error occurred!'})}\n\n"

    return StreamingResponse(event_stream(), media_type="text/event-stream")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8013)
```

Run this code or your own server code.

<Frame background="subtle">
  ![](file:eec85584-59f4-452e-8e0d-333ce3d6616a)
</Frame>

### Setting Up a Public URL for Your Server

To make your server accessible, create a public URL using a tunneling tool like ngrok:

```shell
ngrok http --url=<Your url>.ngrok.app 8013
```

<Frame background="subtle">
  ![](file:1d13a69e-4f43-473e-ad2f-086f68a67963)
</Frame>

### Configuring Elevenlabs CustomLLM

Now let's make the changes in Elevenlabs

<Frame background="subtle">
  ![](file:b3d42802-0d10-4c3b-a915-286eb187d1ce)
</Frame>

<Frame background="subtle">
  ![](file:f053391c-abb1-4cf6-847c-e236d29605ac)
</Frame>

Direct your server URL to ngrok endpoint, setup "Limit token usage" to 5000 and set "Custom LLM extra body" to true.

You can start interacting with Agents Platform with your own LLM server


## Optimizing for slow processing LLMs

If your custom LLM has slow processing times (perhaps due to agentic reasoning or pre-processing requirements) you can improve the conversational flow by implementing **buffer words** in your streaming responses. This technique helps maintain natural speech prosody while your LLM generates the complete response.

### Buffer words

When your LLM needs more time to process the full response, return an initial response ending with `"... "` (ellipsis followed by a space). This allows the Text to Speech system to maintain natural flow while keeping the conversation feeling dynamic.
This creates natural pauses that flow well into subsequent content that the LLM can reason longer about. The extra space is crucial to ensure that the subsequent content is not appended to the "..." which can lead to audio distortions.

### Implementation

Here's how to modify your custom LLM server to implement buffer words:

<CodeBlocks>
  ```python title="server.py"
  @app.post("/v1/chat/completions")
  async def create_chat_completion(request: ChatCompletionRequest) -> StreamingResponse:
      oai_request = request.dict(exclude_none=True)
      if "user_id" in oai_request:
          oai_request["user"] = oai_request.pop("user_id")

      async def event_stream():
          try:
              # Send initial buffer chunk while processing
              initial_chunk = {
                  "id": "chatcmpl-buffer",
                  "object": "chat.completion.chunk",
                  "created": 1234567890,
                  "model": request.model,
                  "choices": [{
                      "delta": {"content": "Let me think about that... "},
                      "index": 0,
                      "finish_reason": None
                  }]
              }
              yield f"data: {json.dumps(initial_chunk)}\n\n"

              # Process the actual LLM response
              chat_completion_coroutine = await oai_client.chat.completions.create(**oai_request)

              async for chunk in chat_completion_coroutine:
                  chunk_dict = chunk.model_dump()
                  yield f"data: {json.dumps(chunk_dict)}\n\n"
              yield "data: [DONE]\n\n"

          except Exception as e:
              logging.error("An error occurred: %s", str(e))
              yield f"data: {json.dumps({'error': 'Internal error occurred!'})}\n\n"

      return StreamingResponse(event_stream(), media_type="text/event-stream")

  ```

  ```typescript title="server.ts"
  app.post('/v1/chat/completions', async (req: Request, res: Response) => {
    const request = req.body as ChatCompletionRequest;
    const oaiRequest = { ...request };

    if (oaiRequest.user_id) {
      oaiRequest.user = oaiRequest.user_id;
      delete oaiRequest.user_id;
    }

    res.setHeader('Content-Type', 'text/event-stream');
    res.setHeader('Cache-Control', 'no-cache');
    res.setHeader('Connection', 'keep-alive');

    try {
      // Send initial buffer chunk while processing
      const initialChunk = {
        id: "chatcmpl-buffer",
        object: "chat.completion.chunk",
        created: Math.floor(Date.now() / 1000),
        model: request.model,
        choices: [{
          delta: { content: "Let me think about that... " },
          index: 0,
          finish_reason: null
        }]
      };
      res.write(`data: ${JSON.stringify(initialChunk)}\n\n`);

      // Process the actual LLM response
      const stream = await openai.chat.completions.create({
        ...oaiRequest,
        stream: true
      });

      for await (const chunk of stream) {
        res.write(`data: ${JSON.stringify(chunk)}\n\n`);
      }

      res.write('data: [DONE]\n\n');
      res.end();

    } catch (error) {
      console.error('An error occurred:', error);
      res.write(`data: ${JSON.stringify({ error: 'Internal error occurred!' })}\n\n`);
      res.end();
    }
  });
  ```
</CodeBlocks>


## System tools integration

Your custom LLM can trigger [system tools](/docs/agents-platform/customization/tools/system-tools) to control conversation flow and state. These tools are automatically included in the `tools` parameter of your chat completion requests when configured in your agent.

### How system tools work

1. **LLM Decision**: Your custom LLM decides when to call these tools based on conversation context
2. **Tool Response**: The LLM responds with function calls in standard OpenAI format
3. **Backend Processing**: ElevenLabs processes the tool calls and updates conversation state

For more information on system tools, please see [our guide](/docs/agents-platform/customization/tools/system-tools)

### Available system tools

<AccordionGroup>
  <Accordion title="End call">
    **Purpose**: Automatically terminate conversations when appropriate conditions are met.

    **Trigger conditions**: The LLM should call this tool when:

    * The main task has been completed and user is satisfied
    * The conversation reached natural conclusion with mutual agreement
    * The user explicitly indicates they want to end the conversation

    **Parameters**:

    * `reason` (string, required): The reason for ending the call
    * `message` (string, optional): A farewell message to send to the user before ending the call

    **Function call format**:

    ```json
    {
      "type": "function",
      "function": {
        "name": "end_call",
        "arguments": "{\"reason\": \"Task completed successfully\", \"message\": \"Thank you for using our service. Have a great day!\"}"
      }
    }
    ```

    **Implementation**: Configure as a system tool in your agent settings. The LLM will receive detailed instructions about when to call this function.

    Learn more: [End call tool](/docs/agents-platform/customization/tools/system-tools/end-call)
  </Accordion>

  <Accordion title="Language detection">
    **Purpose**: Automatically switch to the user's detected language during conversations.

    **Trigger conditions**: The LLM should call this tool when:

    * User speaks in a different language than the current conversation language
    * User explicitly requests to switch languages
    * Multi-language support is needed for the conversation

    **Parameters**:

    * `reason` (string, required): The reason for the language switch
    * `language` (string, required): The language code to switch to (must be in supported languages list)

    **Function call format**:

    ```json
    {
      "type": "function",
      "function": {
        "name": "language_detection",
        "arguments": "{\"reason\": \"User requested Spanish\", \"language\": \"es\"}"
      }
    }
    ```

    **Implementation**: Configure supported languages in agent settings and add the language detection system tool. The agent will automatically switch voice and responses to match detected languages.

    Learn more: [Language detection tool](/docs/agents-platform/customization/tools/system-tools/language-detection)
  </Accordion>

  <Accordion title="Agent transfer">
    **Purpose**: Transfer conversations between specialized AI agents based on user needs.

    **Trigger conditions**: The LLM should call this tool when:

    * User request requires specialized knowledge or different agent capabilities
    * Current agent cannot adequately handle the query
    * Conversation flow indicates need for different agent type

    **Parameters**:

    * `reason` (string, optional): The reason for the agent transfer
    * `agent_number` (integer, required): Zero-indexed number of the agent to transfer to (based on configured transfer rules)

    **Function call format**:

    ```json
    {
      "type": "function",
      "function": {
        "name": "transfer_to_agent",
        "arguments": "{\"reason\": \"User needs billing support\", \"agent_number\": 0}"
      }
    }
    ```

    **Implementation**: Define transfer rules mapping conditions to specific agent IDs. Configure which agents the current agent can transfer to. Agents are referenced by zero-indexed numbers in the transfer configuration.

    Learn more: [Agent transfer tool](/docs/agents-platform/customization/tools/system-tools/agent-transfer)
  </Accordion>

  <Accordion title="Transfer to human">
    **Purpose**: Seamlessly hand off conversations to human operators when AI assistance is insufficient.

    **Trigger conditions**: The LLM should call this tool when:

    * Complex issues requiring human judgment
    * User explicitly requests human assistance
    * AI reaches limits of capability for the specific request
    * Escalation protocols are triggered

    **Parameters**:

    * `reason` (string, optional): The reason for the transfer
    * `transfer_number` (string, required): The phone number to transfer to (must match configured numbers)
    * `client_message` (string, required): Message read to the client while waiting for transfer
    * `agent_message` (string, required): Message for the human operator receiving the call

    **Function call format**:

    ```json
    {
      "type": "function",
      "function": {
        "name": "transfer_to_number",
        "arguments": "{\"reason\": \"Complex billing issue\", \"transfer_number\": \"+15551234567\", \"client_message\": \"I'm transferring you to a billing specialist who can help with your account.\", \"agent_message\": \"Customer has a complex billing dispute about order #12345 from last month.\"}"
      }
    }
    ```

    **Implementation**: Configure transfer phone numbers and conditions. Define messages for both customer and receiving human operator. Works with both Twilio and SIP trunking.

    Learn more: [Transfer to human tool](/docs/agents-platform/customization/tools/system-tools/transfer-to-human)
  </Accordion>

  <Accordion title="Skip turn">
    **Purpose**: Allow the agent to pause and wait for user input without speaking.

    **Trigger conditions**: The LLM should call this tool when:

    * User indicates they need a moment ("Give me a second", "Let me think")
    * User requests pause in conversation flow
    * Agent detects user needs time to process information

    **Parameters**:

    * `reason` (string, optional): Free-form reason explaining why the pause is needed

    **Function call format**:

    ```json
    {
      "type": "function",
      "function": {
        "name": "skip_turn",
        "arguments": "{\"reason\": \"User requested time to think\"}"
      }
    }
    ```

    **Implementation**: No additional configuration needed. The tool simply signals the agent to remain silent until the user speaks again.

    Learn more: [Skip turn tool](/docs/agents-platform/customization/tools/system-tools/skip-turn)
  </Accordion>

  <Accordion title="Voicemail detection">
    **Parameters**:

    * `reason` (string, required): The reason for detecting voicemail (e.g., "automated greeting detected", "no human response")

    **Function call format**:

    ```json
    {
      "type": "function",
      "function": {
        "name": "voicemail_detection",
        "arguments": "{\"reason\": \"Automated greeting detected with request to leave message\"}"
      }
    }
    ```

    Learn more: [Voicemail detection tool](/docs/agents-platform/customization/tools/system-tools/voicemail-detection)
  </Accordion>
</AccordionGroup>

### Example Request with System Tools

When system tools are configured, your custom LLM will receive requests that include the tools in the standard OpenAI format:

```json
{
  "messages": [
    {
      "role": "system",
      "content": "You are a helpful assistant. You have access to system tools for managing conversations."
    },
    {
      "role": "user",
      "content": "I think we're done here, thanks for your help!"
    }
  ],
  "model": "your-custom-model",
  "temperature": 0.7,
  "max_tokens": 1000,
  "stream": true,
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "end_call",
        "description": "Call this function to end the current conversation when the main task has been completed...",
        "parameters": {
          "type": "object",
          "properties": {
            "reason": {
              "type": "string",
              "description": "The reason for the tool call."
            },
            "message": {
              "type": "string",
              "description": "A farewell message to send to the user along right before ending the call."
            }
          },
          "required": ["reason"]
        }
      }
    },
    {
      "type": "function",
      "function": {
        "name": "language_detection",
        "description": "Change the conversation language when the user expresses a language preference explicitly...",
        "parameters": {
          "type": "object",
          "properties": {
            "reason": {
              "type": "string",
              "description": "The reason for the tool call."
            },
            "language": {
              "type": "string",
              "description": "The language to switch to. Must be one of language codes in tool description."
            }
          },
          "required": ["reason", "language"]
        }
      }
    },
    {
      "type": "function",
      "function": {
        "name": "skip_turn",
        "description": "Skip a turn when the user explicitly indicates they need a moment to think...",
        "parameters": {
          "type": "object",
          "properties": {
            "reason": {
              "type": "string",
              "description": "Optional free-form reason explaining why the pause is needed."
            }
          },
          "required": []
        }
      }
    }
  ]
}
```

<Note>
  Your custom LLM must support function calling to use system tools. Ensure your model can generate
  proper function call responses in OpenAI format.
</Note>


# Additional Features

<Accordion title="Custom LLM Parameters">
  You may pass additional parameters to your custom LLM implementation.

  <Tabs>
    <Tab title="Python">
      <Steps>
        <Step title="Define the Extra Parameters">
          Create an object containing your custom parameters:

          ```python
          from elevenlabs.conversational_ai.conversation import Conversation, ConversationConfig

          extra_body_for_convai = {
              "UUID": "123e4567-e89b-12d3-a456-426614174000",
              "parameter-1": "value-1",
              "parameter-2": "value-2",
          }

          config = ConversationConfig(
              extra_body=extra_body_for_convai,
          )
          ```
        </Step>

        <Step title="Update the LLM Implementation">
          Modify your custom LLM code to handle the additional parameters:

          ```python
          import json
          import os
          import fastapi
          from fastapi.responses import StreamingResponse
          from fastapi import Request
          from openai import AsyncOpenAI
          import uvicorn
          import logging
          from dotenv import load_dotenv
          from pydantic import BaseModel
          from typing import List, Optional

          # Load environment variables from .env file
          load_dotenv()

          # Retrieve API key from environment
          OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
          if not OPENAI_API_KEY:
              raise ValueError("OPENAI_API_KEY not found in environment variables")

          app = fastapi.FastAPI()
          oai_client = AsyncOpenAI(api_key=OPENAI_API_KEY)

          class Message(BaseModel):
              role: str
              content: str

          class ChatCompletionRequest(BaseModel):
              messages: List[Message]
              model: str
              temperature: Optional[float] = 0.7
              max_tokens: Optional[int] = None
              stream: Optional[bool] = False
              user_id: Optional[str] = None
              elevenlabs_extra_body: Optional[dict] = None

          @app.post("/v1/chat/completions")
          async def create_chat_completion(request: ChatCompletionRequest) -> StreamingResponse:
              oai_request = request.dict(exclude_none=True)
              print(oai_request)
              if "user_id" in oai_request:
                  oai_request["user"] = oai_request.pop("user_id")

              if "elevenlabs_extra_body" in oai_request:
                  oai_request.pop("elevenlabs_extra_body")

              chat_completion_coroutine = await oai_client.chat.completions.create(**oai_request)

              async def event_stream():
                  try:
                      async for chunk in chat_completion_coroutine:
                          chunk_dict = chunk.model_dump()
                          yield f"data: {json.dumps(chunk_dict)}\n\n"
                      yield "data: [DONE]\n\n"
                  except Exception as e:
                      logging.error("An error occurred: %s", str(e))
                      yield f"data: {json.dumps({'error': 'Internal error occurred!'})}\n\n"

              return StreamingResponse(event_stream(), media_type="text/event-stream")

          if __name__ == "__main__":
              uvicorn.run(app, host="0.0.0.0", port=8013)
          ```
        </Step>
      </Steps>

      ### Example Request

      With this custom message setup, your LLM will receive requests in this format:

      ```json
      {
        "messages": [
          {
            "role": "system",
            "content": "\n  <Redacted>"
          },
          {
            "role": "assistant",
            "content": "Hey I'm currently unavailable."
          },
          {
            "role": "user",
            "content": "Hey, who are you?"
          }
        ],
        "model": "gpt-4o",
        "temperature": 0.5,
        "max_tokens": 5000,
        "stream": true,
        "elevenlabs_extra_body": {
          "UUID": "123e4567-e89b-12d3-a456-426614174000",
          "parameter-1": "value-1",
          "parameter-2": "value-2"
        }
      }
      ```
    </Tab>
  </Tabs>
</Accordion>



# Cloudflare Workers AI

> Connect an agent to a custom LLM on Cloudflare Workers AI.


## Overview

[Cloudflare's Workers AI platform](https://developers.cloudflare.com/workers-ai/) lets you run machine learning models, powered by serverless GPUs, on Cloudflare's global network, even on the free plan!

Workers AI comes with a curated set of [popular open-source models](https://developers.cloudflare.com/workers-ai/models/) that enable you to do tasks such as image classification, text generation, object detection and more.


## Choosing a model

To make use of the full power of ElevenLabs Agents you need to use a model that supports [function calling](https://developers.cloudflare.com/workers-ai/function-calling/#what-models-support-function-calling).

When browsing the [model catalog](https://developers.cloudflare.com/workers-ai/models/), look for models with the function calling property beside it.

<iframe width="100%" height="400" src="https://www.youtube-nocookie.com/embed/8iwPIdzTwAA?rel=0&autoplay=0" title="YouTube video player" frameborder="0" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen />

<Tip title="Try out DeepSeek R1" icon="leaf">
  Cloudflare Workers AI provides access to
  [DeepSeek-R1-Distill-Qwen-32B](https://developers.cloudflare.com/workers-ai/models/deepseek-r1-distill-qwen-32b/),
  a model distilled from DeepSeek-R1 based on Qwen2.5. It outperforms OpenAI-o1-mini across various
  benchmarks, achieving new state-of-the-art results for dense models.
</Tip>


## Set up DeepSeek R1 on Cloudflare Workers AI

<Steps>
  <Step>
    Navigate to [dash.cloudflare.com](https://dash.cloudflare.com) and create or sign in to your account. In the navigation, select AI > Workers AI, and then click on the "Use REST API" widget.

    <Frame background="subtle">
      ![Add Secret](file:6e4de1a6-2809-404a-8bf2-11240064ca50)
    </Frame>
  </Step>

  <Step>
    Once you have your API key, you can try it out immediately with a curl request. Cloudflare provides an OpenAI-compatible API endpoint making this very convenient. At this point make a note of the model and the full endpoint — including the account ID. For example: `https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}c/ai/v1/`.

    ```bash
    curl https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/v1/chat/completions \
    -X POST \
    -H "Authorization: Bearer {API_TOKEN}" \
    -d '{
        "model": "@cf/deepseek-ai/deepseek-r1-distill-qwen-32b",
        "messages": [
          {"role": "system", "content": "You are a helpful assistant."},
          {"role": "user", "content": "How many Rs in the word Strawberry?"}
        ],
        "stream": false
      }'
    ```
  </Step>

  <Step>
    Navigate to your [AI Agent](https://elevenlabs.io/app/agents), scroll down to the "Secrets" section and select "Add Secret". After adding the secret, make sure to hit "Save" to make the secret available to your agent.

    <Frame background="subtle">
      ![Add Secret](file:b9a17e3a-72e8-40b7-bf1c-b4a4b43ff57b)
    </Frame>
  </Step>

  <Step>
    Choose "Custom LLM" from the dropdown menu.

    <Frame background="subtle">
      ![Choose custom llm](file:5871b388-8f5b-4896-b4cb-3c0f541bbf53)
    </Frame>
  </Step>

  <Step>
    For the Server URL, specify Cloudflare's OpenAI-compatible API endpoint: `https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/v1/`. For the Model ID, specify `@cf/deepseek-ai/deepseek-r1-distill-qwen-32b` as discussed above, and select your API key from the dropdown menu.

    <Frame background="subtle">
      ![Enter url](file:01600230-04c6-4a21-8982-81c3ceb4e044)
    </Frame>
  </Step>

  <Step>
    Now you can go ahead and click "Test AI Agent" to chat with your custom DeepSeek R1 model.
  </Step>
</Steps>



# Groq Cloud

> Connect an agent to a custom LLM on Groq Cloud.


## Overview

[Groq Cloud](https://console.groq.com/) provides easy access to fast AI inference, giving you OpenAI-compatible API endpoints in a matter of clicks.

Use leading [Openly-available Models](https://console.groq.com/docs/models) like Llama, Mixtral, and Gemma as the brain for your ElevenLabs agents in a few easy steps.


## Choosing a model

To make use of the full power of ElevenLabs agents you need to use a model that supports tool use and structured outputs. Groq recommends the following Llama-3.3 models their versatility and performance:

* meta-llama/llama-4-scout-17b-16e-instruct (10M token context window) and support for 12 languages (Arabic, English, French, German, Hindi, Indonesian, Italian, Portuguese, Spanish, Tagalog, Thai, and Vietnamese)
* llama-3.3-70b-versatile (128k context window | 32,768 max output tokens)
* llama-3.1-8b-instant (128k context window | 8,192 max output tokens)

With this in mind, it's recommended to use `meta-llama/llama-4-scout-17b-16e-instruct` for your ElevenLabs Agents agent.


## Set up Llama 3.3 on Groq Cloud

<Steps>
  <Step>
    Navigate to [console.groq.com/keys](https://console.groq.com/keys) and create a new API key.

    <Frame background="subtle">
      ![Add Secret](file:a2da2257-0032-4bed-8c89-3be3f97f4d22)
    </Frame>
  </Step>

  <Step>
    Once you have your API key, you can test it by running the following curl command:

    ```bash
    curl https://api.groq.com/openai/v1/chat/completions -s \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $GROQ_API_KEY" \
    -d '{
    "model": "llama-3.3-70b-versatile",
    "messages": [{
        "role": "user",
        "content": "Hello, how are you?"
    }]
    }'
    ```
  </Step>

  <Step>
    Navigate to your [AI Agent](https://elevenlabs.io/app/agents), scroll down to the "Secrets" section and select "Add Secret". After adding the secret, make sure to hit "Save" to make the secret available to your agent.

    <Frame background="subtle">
      ![Add Secret](file:749ed527-6a82-4877-9cc4-61de0d55282b)
    </Frame>
  </Step>

  <Step>
    Choose "Custom LLM" from the dropdown menu.

    <Frame background="subtle">
      ![Choose custom llm](file:5871b388-8f5b-4896-b4cb-3c0f541bbf53)
    </Frame>
  </Step>

  <Step>
    For the Server URL, specify Groq's OpenAI-compatible API endpoint: `https://api.groq.com/openai/v1`. For the Model ID, specify `meta-llama/llama-4-scout-17b-16e-instruct` as discussed above, and select your API key from the dropdown menu.

    <Frame background="subtle">
      ![Enter url](file:ec4a50d8-ef6e-48ac-baf2-59a918fb12a3)
    </Frame>
  </Step>

  <Step>
    Now you can go ahead and click "Test AI Agent" to chat with your custom Llama 3.3 model.
  </Step>
</Steps>



# SambaNova Cloud

> Connect an agent to a custom LLM on SambaNova Cloud.


## Overview

[SambaNova Cloud](http://cloud.sambanova.ai?utm_source=elevenlabs\&utm_medium=external\&utm_campaign=cloud_signup) is the fastest provider of the best [open source models](https://docs.sambanova.ai/cloud/docs/get-started/supported-models), including DeepSeek R1, DeepSeek V3, Llama 4 Maverick and others. Through an
OpenAI-compatible API endpoint, you can set up your ElevenLabs agent on ElevenLabs in a just few minutes.

Watch this [video](https://www.youtube.com/watch?v=46W96JcE_p8) for a walkthrough and demo of how you can configure your ElevenLabs Agents agent to leverage SambaNova's blazing-fast LLMs!


## Choosing a model

To make use of the full power of ElevenLabs Agents you need to use a model that supports tool use and structured outputs. SambaNova recommends the following models for their accuracy and performance:

* `DeepSeek-V3-0324` (671B model)
* `Meta-Llama-3.3-70B-Instruct`
* `Llama-4-Maverick-17B-128E-Instruct`
* `Qwen3-32B`

For up-to-date information on model-specific context windows, please refer to [this](https://docs.sambanova.ai/cloud/docs/get-started/supported-models) page.

Note that `Meta-Llama-3.3-70B-Instruct` is SambaNova's most battle-tested model. If any model is causing issues, you may report it on SambaNova's [Community page](https://community.sambanova.ai).


## Configuring your ElevenLabs agent with a SambaNova LLM

<Steps>
  <Step>
    Navigate to [cloud.sambanova.ai/apis](https://cloud.sambanova.ai/apis?utm_source=elevenlabs\&utm_medium=external\&utm_campaign=cloud_signup) and create a new API key.

    <Frame background="subtle">
      ![Add Secret](file:3cdaed89-8ea6-4f51-bb27-901c7f0972f4)
    </Frame>
  </Step>

  <Step>
    Once you have your API key, you can test it by running the following curl command:

    ```bash
    curl -H "Authorization: Bearer <your-api-key>" \
     -H "Content-Type: application/json" \
     -d '{
    "stream": true,
    "model": "DeepSeek-V3-0324",
    "messages": [
    	{
    		"role": "system",
    		"content": "You are a helpful assistant"
    	},
    	{
    		"role": "user",
    		"content": "Hello"
    	}
    ]
    }' \
     -X POST https://api.sambanova.ai/v1/chat/completions
    ```
  </Step>

  <Step>
    Create a new [AI Agent](https://elevenlabs.io/app/agents/agents) or edit an existing one.
  </Step>

  <Step>
    Scroll down to the "Workspace Secrets" section and select "Add Secret". Name the key `SAMBANOVA_API_KEY` and copy the value from the SambaNova Cloud dashboard. Be sure to hit "Save" to make the secret available to your agent.

    <Frame background="subtle">
      ![Add Secret](file:2022db04-a2a7-418d-add1-be9b00c57269)
    </Frame>
  </Step>

  <Step>
    Choose "Custom LLM" from the dropdown menu.

    <Frame background="subtle">
      ![Choose custom llm](file:5871b388-8f5b-4896-b4cb-3c0f541bbf53)
    </Frame>
  </Step>

  <Step>
    For the Server URL, specify SambaNova's OpenAI-compatible API endpoint: `https://api.sambanova.ai/v1`. For the Model ID, specify one the model names indicated above (e.g., `Meta-Llama-3.3-70B-Instruct`) and select the `SAMBANOVA_API_KEY` API key from the dropdown menu.

    <Frame background="subtle">
      ![Enter url](file:e2fefe3f-4601-41c9-8f94-12a81c8ad7f5)
    </Frame>
  </Step>

  <Step>
    Set the max tokens to 1024 to restrict the agent's output for brevity. Also be sure to include an instruction in the System Prompt for the model to respond in 500 words or less.

    <Frame background="subtle">
      ![Enter url](file:2fb23075-8353-49fd-9fb0-a525f94c3b29)
    </Frame>
  </Step>

  <Step>
    Save your changes and click on "Test AI Agent" to chat with your SambaNova-powered agent!
  </Step>
</Steps>



# Together AI

> Connect an agent to a custom LLM on Together AI.


## Overview

[Together AI](https://www.together.ai/) provides an AI Acceleration Cloud, allowing you to train, fine-tune, and run inference on AI models blazing fast, at low cost, and at production scale.

Instantly run [200+ models](https://together.xyz/models) including DeepSeek, Llama3, Mixtral, and Stable Diffusion, optimized for peak latency, throughput, and context length.


## Choosing a model

To make use of the full power of ElevenLabs Agents you need to use a model that supports tool use and structured outputs. Together AI supports function calling for [these models](https://docs.together.ai/docs/function-calling):

* meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo
* meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo
* meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo
* meta-llama/Llama-3.3-70B-Instruct-Turbo
* mistralai/Mixtral-8x7B-Instruct-v0.1
* mistralai/Mistral-7B-Instruct-v0.1

With this in mind, it's recommended to use at least `meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo` for your ElevenLabs Agents agent.


## Set up Llama 3.1 on Together AI

<Steps>
  <Step>
    Navigate to [api.together.xyz/settings/api-keys](https://api.together.xyz/settings/api-keys) and create a new API key.

    <Frame background="subtle">
      ![Add Secret](file:eb79f4e4-d848-4608-ab1f-408d55d38ce0)
    </Frame>
  </Step>

  <Step>
    Once you have your API key, you can test it by running the following curl command:

    ```bash
    curl https://api.together.xyz/v1/chat/completions -s \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer <API_KEY>" \
    -d '{
    "model": "meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo",
    "messages": [{
        "role": "user",
        "content": "Hello, how are you?"
    }]
    }'
    ```
  </Step>

  <Step>
    Navigate to your [AI Agent](https://elevenlabs.io/app/agents), scroll down to the "Secrets" section and select "Add Secret". After adding the secret, make sure to hit "Save" to make the secret available to your agent.

    <Frame background="subtle">
      ![Add Secret](file:69f16408-7bdb-4937-97a3-cdb1b66ddd00)
    </Frame>
  </Step>

  <Step>
    Choose "Custom LLM" from the dropdown menu.

    <Frame background="subtle">
      ![Choose custom llm](file:5871b388-8f5b-4896-b4cb-3c0f541bbf53)
    </Frame>
  </Step>

  <Step>
    For the Server URL, specify Together AI's OpenAI-compatible API endpoint: `https://api.together.xyz/v1`. For the Model ID, specify `meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo` as discussed above, and select your API key from the dropdown menu.

    <Frame background="subtle">
      ![Enter url](file:e4656e5d-5d72-4a33-b47a-8f296d87275c)
    </Frame>
  </Step>

  <Step>
    Now you can go ahead and click "Test AI Agent" to chat with your custom Llama 3.1 model.
  </Step>
</Steps>



# LLM Cascading

> Learn how Agents Platform ensures reliable LLM responses using a cascading fallback mechanism.


## Overview

Agents Platform employs an LLM cascading mechanism to enhance the reliability and resilience of its text generation capabilities. This system automatically attempts to use backup Large Language Models (LLMs) if the primary configured LLM fails, ensuring a smoother and more consistent user experience.

Failures can include API errors, timeouts, or empty responses from the LLM provider. The cascade logic handles these situations gracefully.


## How it Works

The cascading process follows a defined sequence:

1. **Preferred LLM Attempt:** The system first attempts to generate a response using the LLM selected in the agent's configuration.

2. **Backup LLM Sequence:** If the preferred LLM fails, the system automatically falls back to a predefined sequence of backup LLMs. This sequence is curated based on model performance, speed, and reliability. The current default sequence (subject to change) is:

   1. Gemini 2.5 Flash
   2. Gemini 2.0 Flash
   3. Gemini 2.0 Flash Lite
   4. Claude 3.7 Sonnet
   5. Claude 3.5 Sonnet v2
   6. Claude 3.5 Sonnet v1
   7. GPT-4o
   8. Gemini 1.5 Pro
   9. Gemini 1.5 Flash

3. **HIPAA Compliance:** If the agent operates in a mode requiring strict data privacy (HIPAA compliance / zero data retention), the backup list is filtered to include only compliant models from the sequence above.

4. **Retries:** The system retries the generation process multiple times (at least 3 attempts) across the sequence of available LLMs (preferred + backups). If a backup LLM also fails, it proceeds to the next one in the sequence. If it runs out of unique backup LLMs within the retry limit, it may retry previously failed backup models.

5. **Lazy Initialization:** Backup LLM connections are initialized only when needed, optimizing resource usage.

<Info>
  The specific list and order of backup LLMs are managed internally by ElevenLabs and optimized for
  performance and availability. The sequence listed above represents the current default but may be
  updated without notice.
</Info>


## Custom LLMs

When you configure a [Custom LLM](/docs/agents-platform/customization/llm/custom-llm), the standard cascading logic to *other* models is bypassed. The system will attempt to use your specified Custom LLM.

If your Custom LLM fails, the system will retry the request with the *same* Custom LLM multiple times (matching the standard minimum retry count) before considering the request failed. It will not fall back to ElevenLabs-hosted models, ensuring your specific configuration is respected.


## Benefits

* **Increased Reliability:** Reduces the impact of temporary issues with a specific LLM provider.
* **Higher Availability:** Increases the likelihood of successfully generating a response even during partial LLM outages.
* **Seamless Operation:** The fallback mechanism is automatic and transparent to the end-user.


## Configuration

LLM cascading is an automatic background process. The only configuration required is selecting your **Preferred LLM** in the agent's settings. The system handles the rest to ensure robust performance.



# Post-call webhooks

> Get notified when calls end and analysis is complete through webhooks.

<iframe width="100%" height="400" src="https://www.youtube-nocookie.com/embed/rqxEz18SS_k?rel=0&autoplay=0" title="YouTube video player" frameborder="0" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen />


## Overview

Post-call [Webhooks](/docs/product-guides/administration/webhooks) allow you to receive detailed information about a call after analysis is complete. When enabled, ElevenLabs will send a POST request to your specified endpoint with comprehensive call data.

ElevenLabs supports three types of post-call webhooks:

* **Transcription webhooks** (`post_call_transcription`): Contains full conversation data including transcripts, analysis results, and metadata
* **Audio webhooks** (`post_call_audio`): Contains minimal data with base64-encoded audio of the full conversation
* **Call initiation failure webhooks** (`call_initiation_failure`): Contains information about failed call initiation attempts including failure reasons and metadata


## Migration Notice: Enhanced Webhook Format

<Warning>
  **Important:** Post-call transcription webhooks will be migrated to include additional fields for
  enhanced compatibility and consistency, ensure your endpoint can handle the extra fields.
</Warning>

### What's Changing

Post-call transcription webhooks will be updated to match the same format as the [GET Conversation response](/docs/api-reference/conversations/get). The webhook `data` object will include three additional boolean fields:

* `has_audio`: Boolean indicating whether the conversation has any audio available
* `has_user_audio`: Boolean indicating whether user audio is available for the conversation
* `has_response_audio`: Boolean indicating whether agent response audio is available for the conversation

### Migration Requirements

To ensure your webhook handlers continue working after the migration:

1. **Update your webhook parsing logic** to handle these three new boolean fields
2. **Test your webhook endpoints** with the new field structure before August 15th, 2025
3. **Ensure your JSON parsing** can gracefully handle additional fields without breaking

### Benefits After Migration

Once the migration is complete:

* **Unified data model**: Webhook responses will match the GET Conversation API format exactly
* **SDK compatibility**: Webhook handlers can be provided in the SDK and automatically stay up-to-date with the GET response model


## Enabling post-call webhooks

Post-call webhooks can be enabled for all agents in your workspace through the Agents Platform [settings page](https://elevenlabs.io/app/agents/settings).

<Frame background="subtle">
  ![Post-call webhook settings](file:511a0c4c-c2cc-4029-a3f4-308102014cd7)
</Frame>

<Warning>
  Post call webhooks must return a 200 status code to be considered successful. Webhooks that
  repeatedly fail are auto disabled if there are 10 or more consecutive failures and the last
  successful delivery was more than 7 days ago or has never been successfully delivered.
</Warning>

<Note>
  For HIPAA compliance, if a webhook fails we can not retry the webhook.
</Note>

### Authentication

It is important for the listener to validate all incoming webhooks. Webhooks currently support authentication via HMAC signatures. Set up HMAC authentication by:

* Securely storing the shared secret generated upon creation of the webhook
* Verifying the ElevenLabs-Signature header in your endpoint using the shared secret

The ElevenLabs-Signature takes the following format:

```json
t=timestamp,v0=hash
```

The hash is equivalent to the hex encoded sha256 HMAC signature of `timestamp.request_body`. Both the hash and timestamp should be validated, an example is shown here:

<Tabs>
  <Tab title="Python">
    Example python webhook handler using FastAPI:

    ```python
    from fastapi import FastAPI, Request
    import time
    import hmac
    from hashlib import sha256

    app = FastAPI()

    # Example webhook handler
    @app.post("/webhook")
    async def receive_message(request: Request):
        payload = await request.body()
        headers = request.headers.get("elevenlabs-signature")
        if headers is None:
            return
        timestamp = headers.split(",")[0][2:]
        hmac_signature = headers.split(",")[1]

        # Validate timestamp
        tolerance = int(time.time()) - 30 * 60
        if int(timestamp) < tolerance
            return

        # Validate signature
        full_payload_to_sign = f"{timestamp}.{payload.decode('utf-8')}"
        mac = hmac.new(
            key=secret.encode("utf-8"),
            msg=full_payload_to_sign.encode("utf-8"),
            digestmod=sha256,
        )
        digest = 'v0=' + mac.hexdigest()
        if hmac_signature != digest:
            return

        # Continue processing

        return {"status": "received"}
    ```
  </Tab>

  <Tab title="JavaScript">
    <Tabs>
      <Tab title="Express">
        Example javascript webhook handler using node express framework:

        ```javascript
        const crypto = require('crypto');
        const secret = process.env.WEBHOOK_SECRET;
        const bodyParser = require('body-parser');

        // Ensure express js is parsing the raw body through instead of applying it's own encoding
        app.use(bodyParser.raw({ type: '*/*' }));

        // Example webhook handler
        app.post('/webhook/elevenlabs', async (req, res) => {
          const headers = req.headers['ElevenLabs-Signature'].split(',');
          const timestamp = headers.find((e) => e.startsWith('t=')).substring(2);
          const signature = headers.find((e) => e.startsWith('v0='));

          // Validate timestamp
          const reqTimestamp = timestamp * 1000;
          const tolerance = Date.now() - 30 * 60 * 1000;
          if (reqTimestamp < tolerance) {
            res.status(403).send('Request expired');
            return;
          } else {
            // Validate hash
            const message = `${timestamp}.${req.body}`;
            const digest = 'v0=' + crypto.createHmac('sha256', secret).update(message).digest('hex');
            if (signature !== digest) {
              res.status(401).send('Request unauthorized');
              return;
            }
          }

          // Validation passed, continue processing ...

          res.status(200).send();
        });
        ```
      </Tab>

      <Tab title="Next.js">
        Example javascript webhook handler using Next.js API route:

        ```javascript app/api/convai-webhook/route.js
        import { NextResponse } from "next/server";
        import type { NextRequest } from "next/server";
        import crypto from "crypto";

        export async function GET() {
          return NextResponse.json({ status: "webhook listening" }, { status: 200 });
        }

        export async function POST(req: NextRequest) {
          const secret = process.env.ELEVENLABS_CONVAI_WEBHOOK_SECRET; // Add this to your env variables
          const { event, error } = await constructWebhookEvent(req, secret);
          if (error) {
            return NextResponse.json({ error: error }, { status: 401 });
          }

          if (event.type === "post_call_transcription") {
            console.log("event data", JSON.stringify(event.data, null, 2));
          }

          return NextResponse.json({ received: true }, { status: 200 });
        }

        const constructWebhookEvent = async (req: NextRequest, secret?: string) => {
          const body = await req.text();
          const signature_header = req.headers.get("ElevenLabs-Signature");
          console.log(signature_header);

          if (!signature_header) {
            return { event: null, error: "Missing signature header" };
          }

          const headers = signature_header.split(",");
          const timestamp = headers.find((e) => e.startsWith("t="))?.substring(2);
          const signature = headers.find((e) => e.startsWith("v0="));

          if (!timestamp || !signature) {
            return { event: null, error: "Invalid signature format" };
          }

          // Validate timestamp
          const reqTimestamp = Number(timestamp) * 1000;
          const tolerance = Date.now() - 30 * 60 * 1000;
          if (reqTimestamp < tolerance) {
            return { event: null, error: "Request expired" };
          }

          // Validate hash
          const message = `${timestamp}.${body}`;

          if (!secret) {
            return { event: null, error: "Webhook secret not configured" };
          }

          const digest =
            "v0=" + crypto.createHmac("sha256", secret).update(message).digest("hex");
          console.log({ digest, signature });
          if (signature !== digest) {
            return { event: null, error: "Invalid signature" };
          }

          const event = JSON.parse(body);
          return { event, error: null };
        };
        ```
      </Tab>
    </Tabs>
  </Tab>
</Tabs>

### IP whitelisting

For additional security, you can whitelist the following static egress IPs from which all ElevenLabs webhook requests originate:

| Region       | IP Address     |
| ------------ | -------------- |
| US (Default) | 34.67.146.145  |
| US (Default) | 34.59.11.47    |
| EU           | 35.204.38.71   |
| EU           | 34.147.113.54  |
| Asia         | 35.185.187.110 |
| Asia         | 35.247.157.189 |

If you are using a [data residency region](/docs/product-guides/administration/data-residency) then the following IPs will be used:

| Region          | IP Address     |
| --------------- | -------------- |
| EU Residency    | 34.77.234.246  |
| EU Residency    | 34.140.184.144 |
| India Residency | 34.93.26.174   |
| India Residency | 34.93.252.69   |

If your infrastructure requires strict IP-based access controls, adding these IPs to your firewall allowlist will ensure you only receive webhook requests from ElevenLabs' systems.

<Note>
  These static IPs are used across all ElevenLabs webhook services and will remain consistent. Using
  IP whitelisting in combination with HMAC signature validation provides multiple layers of
  security.
</Note>


## Webhook response structure

ElevenLabs sends three distinct types of post-call webhooks, each with different data structures:

### Transcription webhooks (`post_call_transcription`)

Contains comprehensive conversation data including full transcripts, analysis results, and metadata.

#### Top-level fields

| Field             | Type   | Description                                                            |
| ----------------- | ------ | ---------------------------------------------------------------------- |
| `type`            | string | Type of event (always `post_call_transcription`)                       |
| `data`            | object | Conversation data using the `ConversationHistoryCommonModel` structure |
| `event_timestamp` | number | When this event occurred in unix time UTC                              |

#### Data object structure

The `data` object contains:

| Field                                 | Type   | Description                                   |
| ------------------------------------- | ------ | --------------------------------------------- |
| `agent_id`                            | string | The ID of the agent that handled the call     |
| `conversation_id`                     | string | Unique identifier for the conversation        |
| `status`                              | string | Status of the conversation (e.g., "done")     |
| `user_id`                             | string | User identifier if available                  |
| `transcript`                          | array  | Complete conversation transcript with turns   |
| `metadata`                            | object | Call timing, costs, and phone details         |
| `analysis`                            | object | Evaluation results and conversation summary   |
| `conversation_initiation_client_data` | object | Configuration overrides and dynamic variables |

<Note>
  As of August 15th, 2025, transcription webhooks will include the `has_audio`, `has_user_audio`,
  and `has_response_audio` fields to match the [GET Conversation
  response](/docs/api-reference/conversations/get) format exactly. Prior to this date, these fields
  are not included in webhook payloads.
</Note>

### Audio webhooks (`post_call_audio`)

Contains minimal data with the full conversation audio as base64-encoded MP3.

#### Top-level fields

| Field             | Type   | Description                               |
| ----------------- | ------ | ----------------------------------------- |
| `type`            | string | Type of event (always `post_call_audio`)  |
| `data`            | object | Minimal audio data                        |
| `event_timestamp` | number | When this event occurred in unix time UTC |

#### Data object structure

The `data` object contains only:

| Field             | Type   | Description                                                                    |
| ----------------- | ------ | ------------------------------------------------------------------------------ |
| `agent_id`        | string | The ID of the agent that handled the call                                      |
| `conversation_id` | string | Unique identifier for the conversation                                         |
| `full_audio`      | string | Base64-encoded string containing the complete conversation audio in MP3 format |

<Warning>
  Audio webhooks contain only the three fields listed above. They do NOT include transcript data,
  metadata, analysis results, or any other conversation details.
</Warning>

### Call initiation failure webhooks (`call_initiation_failure`)

Contains information about telephony call initiation attempts, including failure reasons and telephony-provider metadata.

<Note>
  Call initiation failure webhook events are sent when a call fails to initiate due to connection
  errors, user declining the call, or user not picking up. If a call goes to voicemail or is picked
  up by an automated service, no call initiation failure webhook is sent as the call was
  successfully initiated.
</Note>

#### Top-level fields

| Field             | Type   | Description                                      |
| ----------------- | ------ | ------------------------------------------------ |
| `type`            | string | Type of event (always `call_initiation_failure`) |
| `data`            | object | Call initiation failure data                     |
| `event_timestamp` | number | When this event occurred in unix time UTC        |

#### Data object structure

The `data` object contains:

| Field             | Type   | Description                                              |
| ----------------- | ------ | -------------------------------------------------------- |
| `agent_id`        | string | The ID of the agent that was assigned to handle the call |
| `conversation_id` | string | Unique identifier for the conversation                   |
| `failure_reason`  | string | The failure reason ("busy", "no-answer", "unknown")      |
| `metadata`        | object | Additional data provided by the telephony provider.      |

#### Metadata object structure

The `metadata` object structure varies depending on whether the outbound call was made via Twilio or via SIP trunking. The object includes a `type` field that distinguishes between the two, and a `body` field containing provider-specific details.

**SIP metadata** (`type: "sip"`):

| Field  | Type   | Required | Description                           |
| ------ | ------ | -------- | ------------------------------------- |
| `type` | string | Yes      | Provider type (always `sip`)          |
| `body` | object | Yes      | SIP-specific call failure information |

The `body` object for SIP metadata contains:

| Field             | Type   | Required | Description                                                                                      |
| ----------------- | ------ | -------- | ------------------------------------------------------------------------------------------------ |
| `sip_status_code` | number | Yes      | SIP response status code (e.g., 486 for busy)                                                    |
| `error_reason`    | string | Yes      | Human-readable error description                                                                 |
| `call_sid`        | string | Yes      | SIP call session identifier                                                                      |
| `twirp_code`      | string | No       | [Twirp error code](https://twitchtv.github.io/twirp/docs/spec_v7.html#error-codes) if applicable |
| `sip_status`      | string | No       | SIP status text corresponding to the status code                                                 |

**Twilio metadata** (`type: "twilio"`):

| Field  | Type   | Required | Description                                                                                                                               |
| ------ | ------ | -------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| `type` | string | Yes      | Provider type (always `twilio`)                                                                                                           |
| `body` | object | Yes      | Twilio StatusCallback body containing call details, documented [here](https://www.twilio.com/docs/voice/api/call-resource#statuscallback) |


## Example webhook payloads

### Transcription webhook example

```json
{
  "type": "post_call_transcription",
  "event_timestamp": 1739537297,
  "data": {
    "agent_id": "xyz",
    "conversation_id": "abc",
    "status": "done",
    "user_id": "user123",
    "transcript": [
      {
        "role": "agent",
        "message": "Hey there angelo. How are you?",
        "tool_calls": null,
        "tool_results": null,
        "feedback": null,
        "time_in_call_secs": 0,
        "conversation_turn_metrics": null
      },
      {
        "role": "user",
        "message": "Hey, can you tell me, like, a fun fact about 11 Labs?",
        "tool_calls": null,
        "tool_results": null,
        "feedback": null,
        "time_in_call_secs": 2,
        "conversation_turn_metrics": null
      },
      {
        "role": "agent",
        "message": "I do not have access to fun facts about Eleven Labs. However, I can share some general information about the company. Eleven Labs is an AI voice technology platform that specializes in voice cloning and text-to-speech...",
        "tool_calls": null,
        "tool_results": null,
        "feedback": null,
        "time_in_call_secs": 9,
        "conversation_turn_metrics": {
          "convai_llm_service_ttfb": {
            "elapsed_time": 0.3704247010173276
          },
          "convai_llm_service_ttf_sentence": {
            "elapsed_time": 0.5551181449554861
          }
        }
      }
    ],
    "metadata": {
      "start_time_unix_secs": 1739537297,
      "call_duration_secs": 22,
      "cost": 296,
      "deletion_settings": {
        "deletion_time_unix_secs": 1802609320,
        "deleted_logs_at_time_unix_secs": null,
        "deleted_audio_at_time_unix_secs": null,
        "deleted_transcript_at_time_unix_secs": null,
        "delete_transcript_and_pii": true,
        "delete_audio": true
      },
      "feedback": {
        "overall_score": null,
        "likes": 0,
        "dislikes": 0
      },
      "authorization_method": "authorization_header",
      "charging": {
        "dev_discount": true
      },
      "termination_reason": ""
    },
    "analysis": {
      "evaluation_criteria_results": {},
      "data_collection_results": {},
      "call_successful": "success",
      "transcript_summary": "The conversation begins with the agent asking how Angelo is, but Angelo redirects the conversation by requesting a fun fact about 11 Labs. The agent acknowledges they don't have specific fun facts about Eleven Labs but offers to provide general information about the company. They briefly describe Eleven Labs as an AI voice technology platform specializing in voice cloning and text-to-speech technology. The conversation is brief and informational, with the agent adapting to the user's request despite not having the exact information asked for."
    },
    "conversation_initiation_client_data": {
      "conversation_config_override": {
        "agent": {
          "prompt": null,
          "first_message": null,
          "language": "en"
        },
        "tts": {
          "voice_id": null
        }
      },
      "custom_llm_extra_body": {},
      "dynamic_variables": {
        "user_name": "angelo"
      }
    }
  }
}
```

### Audio webhook example

```json
{
  "type": "post_call_audio",
  "event_timestamp": 1739537319,
  "data": {
    "agent_id": "xyz",
    "conversation_id": "abc",
    "full_audio": "SUQzBAAAAAAA...base64_encoded_mp3_data...AAAAAAAAAA=="
  }
}
```

### Call initiation failure webhook examples

#### Twilio metadata example

```json
{
  "type": "call_initiation_failure",
  "event_timestamp": 1759931652,
  "data": {
    "agent_id": "xyz",
    "conversation_id": "abc",
    "failure_reason": "busy",
    "metadata": {
      "type": "twilio",
      "body": {
        "Called": "+441111111111",
        "ToState": "",
        "CallerCountry": "US",
        "Direction": "outbound-api",
        "Timestamp": "Wed, 08 Oct 2025 13:54:12 +0000",
        "CallbackSource": "call-progress-events",
        "SipResponseCode": "487",
        "CallerState": "WA",
        "ToZip": "",
        "SequenceNumber": "2",
        "CallSid": "CA8367245817625617832576245724",
        "To": "+441111111111",
        "CallerZip": "98631",
        "ToCountry": "GB",
        "CalledZip": "",
        "ApiVersion": "2010-04-01",
        "CalledCity": "",
        "CallStatus": "busy",
        "Duration": "0",
        "From": "+11111111111",
        "CallDuration": "0",
        "AccountSid": "AC37682153267845716245762454a",
        "CalledCountry": "GB",
        "CallerCity": "RAYMOND",
        "ToCity": "",
        "FromCountry": "US",
        "Caller": "+11111111111",
        "FromCity": "RAYMOND",
        "CalledState": "",
        "FromZip": "12345",
        "FromState": "WA"
      }
    }
  }
}
```

#### SIP metadata example

```json
{
  "type": "call_initiation_failure",
  "event_timestamp": 1759931652,
  "data": {
    "agent_id": "xyz",
    "conversation_id": "abc",
    "failure_reason": "busy",
    "metadata": {
      "type": "sip",
      "body": {
        "sip_status_code": 486,
        "error_reason": "INVITE failed: sip status: 486: Busy here (SIP 486)",
        "call_sid": "d8e7f6a5-b4c3-4d5e-8f9a-0b1c2d3e4f5a",
        "sip_status": "Busy here",
        "twirp_code": "unavailable"
      }
    }
  }
}
```


## Audio webhook delivery

Audio webhooks are delivered separately from transcription webhooks and contain only the essential fields needed to identify the conversation along with the base64-encoded audio data.

<Note>
  Audio webhooks can be enabled or disabled using the "Send audio data" toggle in your webhook
  settings. This setting can be configured at both the workspace level (in the Agents Platform
  settings) and at the agent level (in individual agent webhook overrides).
</Note>

### Streaming delivery

Audio webhooks are delivered as streaming HTTP requests with the `transfer-encoding: chunked` header to handle large audio files efficiently.

### Processing audio webhooks

Since audio webhooks are delivered via chunked transfer encoding, you'll need to handle streaming data properly:

<CodeBlocks>
  ```python

  import base64
  import json
  from aiohttp import web

  async def handle_webhook(request):

      # Check if this is a chunked/streaming request
      if request.headers.get("transfer-encoding", "").lower() == "chunked":
          # Read streaming data in chunks
          chunked_body = bytearray()
          while True:
              chunk = await request.content.read(8192)  # 8KB chunks
              if not chunk:
                  break
              chunked_body.extend(chunk)

          # Parse the complete payload
          request_body = json.loads(chunked_body.decode("utf-8"))
      else:
          # Handle regular requests
          body_bytes = await request.read()
          request_body = json.loads(body_bytes.decode('utf-8'))

      # Process different webhook types
      if request_body["type"] == "post_call_transcription":
          # Handle transcription webhook with full conversation data
          handle_transcription_webhook(request_body["data"])
      elif request_body["type"] == "post_call_audio":
          # Handle audio webhook with minimal data
          handle_audio_webhook(request_body["data"])
      elif request_body["type"] == "call_initiation_failure":
          # Handle call initiation failure webhook
          handle_call_initiation_failure_webhook(request_body["data"])

      return web.json_response({"status": "ok"})

  def handle_audio_webhook(data):
      # Decode base64 audio data
      audio_bytes = base64.b64decode(data["full_audio"])

      # Save or process the audio file
      conversation_id = data["conversation_id"]
      with open(f"conversation_{conversation_id}.mp3", "wb") as f:
          f.write(audio_bytes)

  def handle_call_initiation_failure_webhook(data):
      # Handle call initiation failure events
      agent_id = data["agent_id"]
      conversation_id = data["conversation_id"]
      failure_reason = data.get("failure_reason")
      metadata = data.get("metadata", {})

      # Log the failure for monitoring
      print(f"Call failed for agent {agent_id}, conversation {conversation_id}")
      print(f"Failure reason: {failure_reason}")

      # Access provider-specific metadata
      provider_type = metadata.get("type")
      body = metadata.get("body", {})
      if provider_type == "sip":
          print(f"SIP status code: {body.get('sip_status_code')}")
          print(f"Error reason: {body.get('error_reason')}")
      elif provider_type == "twilio":
          print(f"Twilio CallSid: {body.get('CallSid')}")
          print(f"Call status: {body.get('CallStatus')}")

      # Update your system with the failure information
      # e.g., mark lead as "call_failed" in CRM

  ```

  ```javascript
  import fs from 'fs';

  app.post('/webhook/elevenlabs', (req, res) => {
    let body = '';

    // Handle chunked/streaming requests
    req.on('data', (chunk) => {
      body += chunk;
    });

    req.on('end', () => {
      try {
        const requestBody = JSON.parse(body);

        // Process different webhook types
        if (requestBody.type === 'post_call_transcription') {
          // Handle transcription webhook with full conversation data
          handleTranscriptionWebhook(requestBody.data);
        } else if (requestBody.type === 'post_call_audio') {
          // Handle audio webhook with minimal data
          handleAudioWebhook(requestBody.data);
        } else if (requestBody.type === 'call_initiation_failure') {
          // Handle call initiation failure webhook
          handleCallFailureWebhook(requestBody.data);
        }

        res.status(200).json({ status: 'ok' });
      } catch (error) {
        console.error('Error processing webhook:', error);
        res.status(400).json({ error: 'Invalid JSON' });
      }
    });
  });

  function handleAudioWebhook(data) {
    // Decode base64 audio data
    const audioBytes = Buffer.from(data.full_audio, 'base64');

    // Save or process the audio file
    const conversationId = data.conversation_id;
    fs.writeFileSync(`conversation_${conversationId}.mp3`, audioBytes);
  }

  function handleCallFailureWebhook(data) {
    // Handle call initiation failure events
    const { agent_id, conversation_id, failure_reason, metadata } = data;

    // Log the failure for monitoring
    console.log(`Call failed for agent ${agent_id}, conversation ${conversation_id}`);
    console.log(`Failure reason: ${failure_reason}`);

    // Access provider-specific metadata
    const body = metadata.body || {};
    if (metadata?.type === 'sip') {
      console.log(`SIP status code: ${body.sip_status_code}`);
      console.log(`Error reason: ${body.error_reason}`);
    } else if (metadata?.type === 'twilio') {
      console.log(`Twilio CallSid: ${body.CallSid}`);
      console.log(`Call status: ${body.CallStatus}`);
    }

    // Update your system with the failure information
    // e.g., mark lead as "call_failed" in CRM
  }
  ```
</CodeBlocks>

<Note>
  Audio webhooks can be large files, so ensure your webhook endpoint can handle streaming requests
  and has sufficient memory/storage capacity. The audio is delivered in MP3 format.
</Note>


## Use cases

### Automated call follow-ups

Post-call webhooks enable you to build automated workflows that trigger immediately after a call ends. Here are some practical applications:

#### CRM integration

Update your customer relationship management system with conversation data as soon as a call completes:

```javascript
// Example webhook handler
app.post('/webhook/elevenlabs', async (req, res) => {
  // HMAC validation code

  const { data } = req.body;

  // Extract key information
  const userId = data.metadata.user_id;
  const transcriptSummary = data.analysis.transcript_summary;
  const callSuccessful = data.analysis.call_successful;

  // Update CRM record
  await updateCustomerRecord(userId, {
    lastInteraction: new Date(),
    conversationSummary: transcriptSummary,
    callOutcome: callSuccessful,
    fullTranscript: data.transcript,
  });

  res.status(200).send('Webhook received');
});
```

### Stateful conversations

Maintain conversation context across multiple interactions by storing and retrieving state:

1. When a call starts, pass in your user id as a dynamic variable.
2. When a call ends, set up your webhook endpoint to store conversation data in your database, based on the extracted user id from the dynamic\_variables.
3. When the user calls again, you can retrieve this context and pass it to the new conversation into a \{\{previous\_topics}} dynamic variable.
4. This creates a seamless experience where the agent "remembers" previous interactions

```javascript
// Store conversation state when call ends
app.post('/webhook/elevenlabs', async (req, res) => {
  // HMAC validation code

  const { data } = req.body;
  const userId = data.metadata.user_id;

  // Store conversation state
  await db.userStates.upsert({
    userId,
    lastConversationId: data.conversation_id,
    lastInteractionTimestamp: data.metadata.start_time_unix_secs,
    conversationHistory: data.transcript,
    previousTopics: extractTopics(data.analysis.transcript_summary),
  });

  res.status(200).send('Webhook received');
});

// When initiating a new call, retrieve and use the state
async function initiateCall(userId) {
  // Get user's conversation state
  const userState = await db.userStates.findOne({ userId });

  // Start new conversation with context from previous calls
  return await elevenlabs.startConversation({
    agent_id: 'xyz',
    conversation_id: generateNewId(),
    dynamic_variables: {
      user_name: userState.name,
      previous_conversation_id: userState.lastConversationId,
      previous_topics: userState.previousTopics.join(', '),
    },
  });
}
```



# Next.JS

> Learn how to create a web application that enables voice conversations with ElevenLabs AI agents

This tutorial will guide you through creating a web client that can interact with a ElevenLabs agent. You'll learn how to implement real-time voice conversations, allowing users to speak with an AI agent that can listen, understand, and respond naturally using voice synthesis.


## What You'll Need

1. An ElevenLabs agent created following [this guide](/docs/agents-platform/quickstart)
2. `npm` installed on your local system.
3. We'll use Typescript for this tutorial, but you can use Javascript if you prefer.

<Note>
  Looking for a complete example? Check out our [Next.js demo on
  GitHub](https://github.com/elevenlabs/elevenlabs-examples/tree/main/examples/conversational-ai/nextjs).
</Note>

<Frame background="subtle">
  ![](file:8d5cdb91-32be-4026-96a5-da5bf2d00334)
</Frame>


## Setup

<Steps>
  <Step title="Create a new Next.js project">
    Open a terminal window and run the following command:

    ```bash
    npm create next-app my-conversational-agent
    ```

    It will ask you some questions about how to build your project. We'll follow the default suggestions for this tutorial.
  </Step>

  <Step title="Navigate to project directory">
    ```shell
    cd my-conversational-agent
    ```
  </Step>

  <Step title="Install the ElevenLabs dependency">
    ```shell
    npm install @elevenlabs/react
    ```
  </Step>

  <Step title="Test the setup">
    Run the following command to start the development server and open the provided URL in your browser:

    ```shell
    npm run dev
    ```

    <Frame background="subtle">
      ![](file:c17e544d-ab1a-4e6e-a9df-c43fd51230bd)
    </Frame>
  </Step>
</Steps>


## Implement ElevenLabs Agents

<Steps>
  <Step title="Create the conversation component">
    Create a new file `app/components/conversation.tsx`:

    ```tsx app/components/conversation.tsx
    'use client';

    import { useConversation } from '@elevenlabs/react';
    import { useCallback } from 'react';

    export function Conversation() {
      const conversation = useConversation({
        onConnect: () => console.log('Connected'),
        onDisconnect: () => console.log('Disconnected'),
        onMessage: (message) => console.log('Message:', message),
        onError: (error) => console.error('Error:', error),
      });


      const startConversation = useCallback(async () => {
        try {
          // Request microphone permission
          await navigator.mediaDevices.getUserMedia({ audio: true });

          // Start the conversation with your agent
          await conversation.startSession({
            agentId: 'YOUR_AGENT_ID', // Replace with your agent ID
            userId: 'YOUR_CUSTOMER_USER_ID', // Optional field for tracking your end user IDs
            connectionType: 'webrtc', // either "webrtc" or "websocket"
          });

        } catch (error) {
          console.error('Failed to start conversation:', error);
        }
      }, [conversation]);

      const stopConversation = useCallback(async () => {
        await conversation.endSession();
      }, [conversation]);

      return (
        <div className="flex flex-col items-center gap-4">
          <div className="flex gap-2">
            <button
              onClick={startConversation}
              disabled={conversation.status === 'connected'}
              className="px-4 py-2 bg-blue-500 text-white rounded disabled:bg-gray-300"
            >
              Start Conversation
            </button>
            <button
              onClick={stopConversation}
              disabled={conversation.status !== 'connected'}
              className="px-4 py-2 bg-red-500 text-white rounded disabled:bg-gray-300"
            >
              Stop Conversation
            </button>
          </div>

          <div className="flex flex-col items-center">
            <p>Status: {conversation.status}</p>
            <p>Agent is {conversation.isSpeaking ? 'speaking' : 'listening'}</p>
          </div>
        </div>
      );
    }
    ```
  </Step>

  <Step title="Update the main page">
    Replace the contents of `app/page.tsx` with:

    ```tsx app/page.tsx
    import { Conversation } from './components/conversation';

    export default function Home() {
      return (
        <main className="flex min-h-screen flex-col items-center justify-between p-24">
          <div className="z-10 max-w-5xl w-full items-center justify-between font-mono text-sm">
            <h1 className="text-4xl font-bold mb-8 text-center">
              ElevenLabs Agents
            </h1>
            <Conversation />
          </div>
        </main>
      );
    }
    ```
  </Step>
</Steps>

<Accordion title="(Optional) Authenticate the agents with a signed URL">
  <Note>
    This authentication step is only required for private agents. If you're using a public agent, you
    can skip this section and directly use the `agentId` in the `startSession` call.
  </Note>

  If you're using a private agent that requires authentication, you'll need to generate
  a signed URL from your server. This section explains how to set this up.

  ### What You'll Need

  1. An ElevenLabs account and API key. Sign up [here](https://www.elevenlabs.io/sign-up).

  <Steps>
    <Step title="Create environment variables">
      Create a `.env.local` file in your project root:

      ```yaml .env.local
      ELEVENLABS_API_KEY=your-api-key-here
      NEXT_PUBLIC_AGENT_ID=your-agent-id-here
      ```

      <Warning>
        1. Make sure to add `.env.local` to your `.gitignore` file to prevent accidentally committing sensitive credentials to version control.
        2. Never expose your API key in the client-side code. Always keep it secure on the server.
      </Warning>
    </Step>

    <Step title="Create an API route">
      Create a new file `app/api/get-signed-url/route.ts`:

      ```tsx app/api/get-signed-url/route.ts
      import { NextResponse } from 'next/server';

      export async function GET() {
        try {
          const response = await fetch(
            `https://api.elevenlabs.io/v1/convai/conversation/get-signed-url?agent_id=${process.env.NEXT_PUBLIC_AGENT_ID}`,
            {
              headers: {
                'xi-api-key': process.env.ELEVENLABS_API_KEY!,
              },
            }
          );

          if (!response.ok) {
            throw new Error('Failed to get signed URL');
          }

          const data = await response.json();
          return NextResponse.json({ signedUrl: data.signed_url });
        } catch (error) {
          return NextResponse.json(
            { error: 'Failed to generate signed URL' },
            { status: 500 }
          );
        }
      }
      ```
    </Step>

    <Step title="Update the Conversation component">
      Modify your `conversation.tsx` to fetch and use the signed URL:

      ```tsx app/components/conversation.tsx {5-12,19,23}
      // ... existing imports ...

      export function Conversation() {
        // ... existing conversation setup ...
        const getSignedUrl = async (): Promise<string> => {
          const response = await fetch("/api/get-signed-url");
          if (!response.ok) {
            throw new Error(`Failed to get signed url: ${response.statusText}`);
          }
          const { signedUrl } = await response.json();
          return signedUrl;
        };

        const startConversation = useCallback(async () => {
          try {
            // Request microphone permission
            await navigator.mediaDevices.getUserMedia({ audio: true });

            const signedUrl = await getSignedUrl();

            // Start the conversation with your signed url
            await conversation.startSession({
              signedUrl,
            });

          } catch (error) {
            console.error('Failed to start conversation:', error);
          }
        }, [conversation]);

        // ... rest of the component ...
      }
      ```

      <Warning>
        Signed URLs expire after a short period. However, any conversations initiated before expiration will continue uninterrupted. In a production environment, implement proper error handling and URL refresh logic for starting new conversations.
      </Warning>
    </Step>
  </Steps>
</Accordion>


## Next Steps

Now that you have a basic implementation, you can:

1. Add visual feedback for voice activity
2. Implement error handling and retry logic
3. Add a chat history display
4. Customize the UI to match your brand

<Info>
  For more advanced features and customization options, check out the
  [@elevenlabs/react](https://www.npmjs.com/package/@elevenlabs/react) package.
</Info>



# Vite (Javascript)

> Learn how to create a web application that enables voice conversations with ElevenLabs AI agents

This tutorial will guide you through creating a web client that can interact with a ElevenLabs agent. You'll learn how to implement real-time voice conversations, allowing users to speak with an AI agent that can listen, understand, and respond naturally using voice synthesis.

<Note>
  Looking to build with React/Next.js? Check out our [Next.js
  guide](/docs/agents-platform/guides/quickstarts/next-js)
</Note>


## What You'll Need

1. An ElevenLabs agent created following [this guide](/docs/agents-platform/quickstart)
2. `npm` installed on your local system
3. Basic knowledge of JavaScript

<Note>
  Looking for a complete example? Check out our [Vanilla JS demo on
  GitHub](https://github.com/elevenlabs/elevenlabs-examples/tree/main/examples/conversational-ai/javascript).
</Note>


## Project Setup

<Steps>
  <Step title="Create a Project Directory">
    Open a terminal and create a new directory for your project:

    ```bash
    mkdir elevenlabs-conversational-ai
    cd elevenlabs-conversational-ai
    ```
  </Step>

  <Step title="Initialize npm and Install Dependencies">
    Initialize a new npm project and install the required packages:

    ```bash
    npm init -y
    npm install vite @elevenlabs/client
    ```
  </Step>

  <Step title="Set up Basic Project Structure">
    Add this to your `package.json`:

    ```json package.json {4}
    {
        "scripts": {
            ...
            "dev:frontend": "vite"
        }
    }
    ```

    Create the following file structure:

    ```shell {2,3}
    elevenlabs-conversational-ai/
    ├── index.html
    ├── script.js
    ├── package-lock.json
    ├── package.json
    └── node_modules
    ```
  </Step>
</Steps>


## Implementing the Voice Chat Interface

<Steps>
  <Step title="Create the HTML Interface">
    In `index.html`, set up a simple user interface:

    <Frame background="subtle">
      ![](file:4c0807f9-4938-4923-86f9-7179b42b257e)
    </Frame>

    ```html index.html
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="UTF-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            <title>ElevenLabs Agents</title>
        </head>
        <body style="font-family: Arial, sans-serif; text-align: center; padding: 50px;">
            <h1>ElevenLabs Agents</h1>
            <div style="margin-bottom: 20px;">
                <button id="startButton" style="padding: 10px 20px; margin: 5px;">Start Conversation</button>
                <button id="stopButton" style="padding: 10px 20px; margin: 5px;" disabled>Stop Conversation</button>
            </div>
            <div style="font-size: 18px;">
                <p>Status: <span id="connectionStatus">Disconnected</span></p>
                <p>Agent is <span id="agentStatus">listening</span></p>
            </div>
            <script type="module" src="../images/script.js"></script>
        </body>
    </html>
    ```
  </Step>

  <Step title="Implement the Conversation Logic">
    In `script.js`, implement the functionality:

    ```javascript script.js
    import { Conversation } from '@elevenlabs/client';

    const startButton = document.getElementById('startButton');
    const stopButton = document.getElementById('stopButton');
    const connectionStatus = document.getElementById('connectionStatus');
    const agentStatus = document.getElementById('agentStatus');

    let conversation;

    async function startConversation() {
        try {
            // Request microphone permission
            await navigator.mediaDevices.getUserMedia({ audio: true });

            // Start the conversation
            conversation = await Conversation.startSession({
                agentId: 'YOUR_AGENT_ID', // Replace with your agent ID
                onConnect: () => {
                    connectionStatus.textContent = 'Connected';
                    startButton.disabled = true;
                    stopButton.disabled = false;
                },
                onDisconnect: () => {
                    connectionStatus.textContent = 'Disconnected';
                    startButton.disabled = false;
                    stopButton.disabled = true;
                },
                onError: (error) => {
                    console.error('Error:', error);
                },
                onModeChange: (mode) => {
                    agentStatus.textContent = mode.mode === 'speaking' ? 'speaking' : 'listening';
                },
            });
        } catch (error) {
            console.error('Failed to start conversation:', error);
        }
    }

    async function stopConversation() {
        if (conversation) {
            await conversation.endSession();
            conversation = null;
        }
    }

    startButton.addEventListener('click', startConversation);
    stopButton.addEventListener('click', stopConversation);
    ```
  </Step>

  <Step title="Start the frontend server">
    ```shell
    npm run dev:frontend
    ```
  </Step>
</Steps>

<Note>
  Make sure to replace 

  `'YOUR_AGENT_ID'`

   with your actual agent ID from ElevenLabs.
</Note>

<Accordion title="(Optional) Authenticate with a Signed URL">
  <Note>
    This authentication step is only required for private agents. If you're using a public agent, you can skip this section and directly use the `agentId` in the `startSession` call.
  </Note>

  <Steps>
    <Step title="Create Environment Variables">
      Create a `.env` file in your project root:

      ```env .env
      ELEVENLABS_API_KEY=your-api-key-here
      AGENT_ID=your-agent-id-here
      ```

      <Warning>
        Make sure to add `.env` to your `.gitignore` file to prevent accidentally committing sensitive credentials.
      </Warning>
    </Step>

    <Step title="Setup the Backend">
      1. Install additional dependencies:

      ```bash
      npm install express cors dotenv
      ```

      2. Create a new folder called `backend`:

      ```shell {2}
      elevenlabs-conversational-ai/
      ├── backend
      ...
      ```
    </Step>

    <Step title="Create the Server">
      ```javascript backend/server.js
      require("dotenv").config();

      const express = require("express");
      const cors = require("cors");

      const app = express();
      app.use(cors());
      app.use(express.json());

      const PORT = process.env.PORT || 3001;

      app.get("/api/get-signed-url", async (req, res) => {
          try {
              const response = await fetch(
                  `https://api.elevenlabs.io/v1/convai/conversation/get-signed-url?agent_id=${process.env.AGENT_ID}`,
                  {
                      headers: {
                          "xi-api-key": process.env.ELEVENLABS_API_KEY,
                      },
                  }
              );

              if (!response.ok) {
                  throw new Error("Failed to get signed URL");
              }

              const data = await response.json();
              res.json({ signedUrl: data.signed_url });
          } catch (error) {
              console.error("Error:", error);
              res.status(500).json({ error: "Failed to generate signed URL" });
          }
      });

      app.listen(PORT, () => {
          console.log(`Server running on http://localhost:${PORT}`);
      });
      ```
    </Step>

    <Step title="Update the Client Code">
      Modify your `script.js` to fetch and use the signed URL:

      ```javascript script.js {2-10,16,19,20}
      // ... existing imports and variables ...

      async function getSignedUrl() {
          const response = await fetch('http://localhost:3001/api/get-signed-url');
          if (!response.ok) {
              throw new Error(`Failed to get signed url: ${response.statusText}`);
          }
          const { signedUrl } = await response.json();
          return signedUrl;
      }

      async function startConversation() {
          try {
              await navigator.mediaDevices.getUserMedia({ audio: true });

              const signedUrl = await getSignedUrl();

              conversation = await Conversation.startSession({
                  signedUrl,
                  // agentId has been removed...
                  onConnect: () => {
                      connectionStatus.textContent = 'Connected';
                      startButton.disabled = true;
                      stopButton.disabled = false;
                  },
                  onDisconnect: () => {
                      connectionStatus.textContent = 'Disconnected';
                      startButton.disabled = false;
                      stopButton.disabled = true;
                  },
                  onError: (error) => {
                      console.error('Error:', error);
                  },
                  onModeChange: (mode) => {
                      agentStatus.textContent = mode.mode === 'speaking' ? 'speaking' : 'listening';
                  },
              });
          } catch (error) {
              console.error('Failed to start conversation:', error);
          }
      }

      // ... rest of the code ...
      ```

      <Warning>
        Signed URLs expire after a short period. However, any conversations initiated before expiration will continue uninterrupted. In a production environment, implement proper error handling and URL refresh logic for starting new conversations.
      </Warning>
    </Step>

    <Step title="Update the package.json">
      ```json package.json {4,5}
      {
          "scripts": {
              ...
              "dev:backend": "node backend/server.js",
              "dev": "npm run dev:frontend & npm run dev:backend"
          }
      }
      ```
    </Step>

    <Step title="Run the Application">
      Start the application with:

      ```bash
      npm run dev
      ```
    </Step>
  </Steps>
</Accordion>


## Next Steps

Now that you have a basic implementation, you can:

1. Add visual feedback for voice activity
2. Implement error handling and retry logic
3. Add a chat history display
4. Customize the UI to match your brand

<Info>
  For more advanced features and customization options, check out the
  [@elevenlabs/client](https://www.npmjs.com/package/@elevenlabs/client) package.
</Info>



---
**Navigation:** [← Previous](./14-batch-calling.md) | [Index](./index.md) | [Next →](./16-chat-mode.md)
