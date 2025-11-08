**Navigation:** [← Previous](./17-salesforce.md) | [Index](./index.md) | [Next →](./19-get-agent.md)

# WebSocket

> Create real-time, interactive voice conversations with AI agents

<Note>
  This documentation is for developers integrating directly with the ElevenLabs WebSocket API. For
  convenience, consider using [the official SDKs provided by
  ElevenLabs](/docs/agents-platform/libraries/python).
</Note>

The ElevenLabs [Agents Platform](https://elevenlabs.io/agents) WebSocket API enables real-time, interactive voice conversations with AI agents. By establishing a WebSocket connection, you can send audio input and receive audio responses in real-time, creating life-like conversational experiences.

<Note>
  Endpoint: 

  `wss://api.elevenlabs.io/v1/convai/conversation?agent_id={agent_id}`
</Note>


## Authentication

### Using Agent ID

For public agents, you can directly use the `agent_id` in the WebSocket URL without additional authentication:

```bash
wss://api.elevenlabs.io/v1/convai/conversation?agent_id=<your-agent-id>
```

### Using a signed URL

For private agents or conversations requiring authorization, obtain a signed URL from your server, which securely communicates with the ElevenLabs API using your API key.

### Example using cURL

**Request:**

```bash
curl -X GET "https://api.elevenlabs.io/v1/convai/conversation/get-signed-url?agent_id=<your-agent-id>" \
     -H "xi-api-key: <your-api-key>"
```

**Response:**

```json
{
  "signed_url": "wss://api.elevenlabs.io/v1/convai/conversation?agent_id=<your-agent-id>&token=<token>"
}
```

<Warning>
  Never expose your ElevenLabs API key on the client side.
</Warning>


## WebSocket events

### Client to server events

The following events can be sent from the client to the server:

<AccordionGroup>
  <Accordion title="Contextual Updates">
    Send non-interrupting contextual information to update the conversation state. This allows you to provide additional context without disrupting the ongoing conversation flow.

    ```javascript
    {
      "type": "contextual_update",
      "text": "User clicked on pricing page"
    }
    ```

    **Use cases:**

    * Updating user status or preferences
    * Providing environmental context
    * Adding background information
    * Tracking user interface interactions

    **Key points:**

    * Does not interrupt current conversation flow
    * Updates are incorporated as tool calls in conversation history
    * Helps maintain context without breaking the natural dialogue

    <Note>
      Contextual updates are processed asynchronously and do not require a direct response from the server.
    </Note>
  </Accordion>
</AccordionGroup>

<Card title="WebSocket API Reference" icon="code" iconPosition="left" href="/docs/agents-platform/api-reference/agents-platform/websocket">
  See the ElevenLabs Agents WebSocket API reference documentation for detailed message structures,
  parameters, and examples.
</Card>


## Next.js implementation example

This example demonstrates how to implement a WebSocket-based conversational agent client in Next.js using the ElevenLabs WebSocket API.

<Note>
  While this example uses the `voice-stream` package for microphone input handling, you can
  implement your own solution for capturing and encoding audio. The focus here is on demonstrating
  the WebSocket connection and event handling with the ElevenLabs API.
</Note>

<Steps>
  <Step title="Install required dependencies">
    First, install the necessary packages:

    ```bash
    npm install voice-stream
    ```

    The `voice-stream` package handles microphone access and audio streaming, automatically encoding the audio in base64 format as required by the ElevenLabs API.

    <Note>
      This example uses Tailwind CSS for styling. To add Tailwind to your Next.js project:

      ```bash
      npm install -D tailwindcss postcss autoprefixer
      npx tailwindcss init -p
      ```

      Then follow the [official Tailwind CSS setup guide for Next.js](https://tailwindcss.com/docs/guides/nextjs).

      Alternatively, you can replace the className attributes with your own CSS styles.
    </Note>
  </Step>

  <Step title="Create WebSocket types">
    Define the types for WebSocket events:

    ```typescript app/types/websocket.ts
    type BaseEvent = {
      type: string;
    };

    type UserTranscriptEvent = BaseEvent & {
      type: "user_transcript";
      user_transcription_event: {
        user_transcript: string;
      };
    };

    type AgentResponseEvent = BaseEvent & {
      type: "agent_response";
      agent_response_event: {
        agent_response: string;
      };
    };

    type AgentResponseCorrectionEvent = BaseEvent & {
      type: "agent_response_correction";
      agent_response_correction_event: {
        original_agent_response: string;
        corrected_agent_response: string;
      };
    };

    type AudioResponseEvent = BaseEvent & {
      type: "audio";
      audio_event: {
        audio_base_64: string;
        event_id: number;
      };
    };

    type InterruptionEvent = BaseEvent & {
      type: "interruption";
      interruption_event: {
        reason: string;
      };
    };

    type PingEvent = BaseEvent & {
      type: "ping";
      ping_event: {
        event_id: number;
        ping_ms?: number;
      };
    };

    export type ElevenLabsWebSocketEvent =
      | UserTranscriptEvent
      | AgentResponseEvent
      | AgentResponseCorrectionEvent
      | AudioResponseEvent
      | InterruptionEvent
      | PingEvent;
    ```
  </Step>

  <Step title="Create WebSocket hook">
    Create a custom hook to manage the WebSocket connection:

    ```typescript app/hooks/useAgentConversation.ts
    'use client';

    import { useCallback, useEffect, useRef, useState } from 'react';
    import { useVoiceStream } from 'voice-stream';
    import type { ElevenLabsWebSocketEvent } from '../types/websocket';

    const sendMessage = (websocket: WebSocket, request: object) => {
      if (websocket.readyState !== WebSocket.OPEN) {
        return;
      }
      websocket.send(JSON.stringify(request));
    };

    export const useAgentConversation = () => {
      const websocketRef = useRef<WebSocket>(null);
      const [isConnected, setIsConnected] = useState<boolean>(false);

      const { startStreaming, stopStreaming } = useVoiceStream({
        onAudioChunked: (audioData) => {
          if (!websocketRef.current) return;
          sendMessage(websocketRef.current, {
            user_audio_chunk: audioData,
          });
        },
      });

      const startConversation = useCallback(async () => {
        if (isConnected) return;

        const websocket = new WebSocket("wss://api.elevenlabs.io/v1/convai/conversation");

        websocket.onopen = async () => {
          setIsConnected(true);
          sendMessage(websocket, {
            type: "conversation_initiation_client_data",
          });
          await startStreaming();
        };

        websocket.onmessage = async (event) => {
          const data = JSON.parse(event.data) as ElevenLabsWebSocketEvent;

          // Handle ping events to keep connection alive
          if (data.type === "ping") {
            setTimeout(() => {
              sendMessage(websocket, {
                type: "pong",
                event_id: data.ping_event.event_id,
              });
            }, data.ping_event.ping_ms);
          }

          if (data.type === "user_transcript") {
            const { user_transcription_event } = data;
            console.log("User transcript", user_transcription_event.user_transcript);
          }

          if (data.type === "agent_response") {
            const { agent_response_event } = data;
            console.log("Agent response", agent_response_event.agent_response);
          }

          if (data.type === "agent_response_correction") {
            const { agent_response_correction_event } = data;
            console.log("Agent response correction", agent_response_correction_event.corrected_agent_response);
          }

          if (data.type === "interruption") {
            // Handle interruption
          }

          if (data.type === "audio") {
            const { audio_event } = data;
            // Implement your own audio playback system here
            // Note: You'll need to handle audio queuing to prevent overlapping
            // as the WebSocket sends audio events in chunks
          }
        };

        websocketRef.current = websocket;

        websocket.onclose = async () => {
          websocketRef.current = null;
          setIsConnected(false);
          stopStreaming();
        };
      }, [startStreaming, isConnected, stopStreaming]);

      const stopConversation = useCallback(async () => {
        if (!websocketRef.current) return;
        websocketRef.current.close();
      }, []);

      useEffect(() => {
        return () => {
          if (websocketRef.current) {
            websocketRef.current.close();
          }
        };
      }, []);

      return {
        startConversation,
        stopConversation,
        isConnected,
      };
    };
    ```
  </Step>

  <Step title="Create the conversation component">
    Create a component to use the WebSocket hook:

    ```typescript app/components/Conversation.tsx
    'use client';

    import { useCallback } from 'react';
    import { useAgentConversation } from '../hooks/useAgentConversation';

    export function Conversation() {
      const { startConversation, stopConversation, isConnected } = useAgentConversation();

      const handleStart = useCallback(async () => {
        try {
          await navigator.mediaDevices.getUserMedia({ audio: true });
          await startConversation();
        } catch (error) {
          console.error('Failed to start conversation:', error);
        }
      }, [startConversation]);

      return (
        <div className="flex flex-col items-center gap-4">
          <div className="flex gap-2">
            <button
              onClick={handleStart}
              disabled={isConnected}
              className="px-4 py-2 bg-blue-500 text-white rounded disabled:bg-gray-300"
            >
              Start Conversation
            </button>
            <button
              onClick={stopConversation}
              disabled={!isConnected}
              className="px-4 py-2 bg-red-500 text-white rounded disabled:bg-gray-300"
            >
              Stop Conversation
            </button>
          </div>
          <div className="flex flex-col items-center">
            <p>Status: {isConnected ? 'Connected' : 'Disconnected'}</p>
          </div>
        </div>
      );
    }
    ```
  </Step>
</Steps>


## Next steps

1. **Audio Playback**: Implement your own audio playback system using Web Audio API or a library. Remember to handle audio queuing to prevent overlapping as the WebSocket sends audio events in chunks.
2. **Error Handling**: Add retry logic and error recovery mechanisms
3. **UI Feedback**: Add visual indicators for voice activity and connection status


## Latency management

To ensure smooth conversations, implement these strategies:

* **Adaptive Buffering:** Adjust audio buffering based on network conditions.
* **Jitter Buffer:** Implement a jitter buffer to smooth out variations in packet arrival times.
* **Ping-Pong Monitoring:** Use ping and pong events to measure round-trip time and adjust accordingly.


## Security best practices

* Rotate API keys regularly and use environment variables to store them.
* Implement rate limiting to prevent abuse.
* Clearly explain the intention when prompting users for microphone access.
* Optimized Chunking: Tweak the audio chunk duration to balance latency and efficiency.


## Additional resources

* [ElevenLabs Agents Documentation](/docs/agents-platform/overview)
* [ElevenLabs Agents SDKs](/docs/agents-platform/libraries/python)



# Agent WebSockets

GET /v1/convai/conversation

Establish a WebSocket connection for real-time conversations with an AI agent.

Reference: https://elevenlabs.io/docs/agents-platform/api-reference/agents-platform/websocket


## AsyncAPI Specification

```yaml
asyncapi: 2.6.0
info:
  title: V 1 Convai Conversation
  version: subpackage_v1ConvaiConversation.v1ConvaiConversation
  description: >-
    Establish a WebSocket connection for real-time conversations with an AI
    agent.
channels:
  /v1/convai/conversation:
    description: >-
      Establish a WebSocket connection for real-time conversations with an AI
      agent.
    bindings:
      ws:
        query:
          type: object
          properties:
            agent_id:
              description: Any type
    publish:
      operationId: v-1-convai-conversation-publish
      summary: subscribe
      description: >-
        Defines the message types that can be received by the client from the
        server
      message:
        name: subscribe
        title: subscribe
        description: >-
          Defines the message types that can be received by the client from the
          server
        payload:
          $ref: '#/components/schemas/V1ConvaiConversationSubscribe'
    subscribe:
      operationId: v-1-convai-conversation-subscribe
      summary: publish
      description: Defines the message types that can be sent from client to server
      message:
        name: publish
        title: publish
        description: Defines the message types that can be sent from client to server
        payload:
          $ref: '#/components/schemas/V1ConvaiConversationPublish'
servers:
  Production:
    url: wss://api.elevenlabs.io/
    protocol: wss
    x-default: true
  Production-US:
    url: wss://api.us.elevenlabs.io/
    protocol: wss
  Production-EU:
    url: wss://api.eu.residency.elevenlabs.io/
    protocol: wss
  Production-India:
    url: wss://api.in.residency.elevenlabs.io/
    protocol: wss
components:
  schemas:
    ConversationInitiationMetadataConversationInitiationMetadataEvent:
      type: object
      properties:
        conversation_id:
          type: string
        agent_output_audio_format:
          type: string
        user_input_audio_format:
          type: string
    ConversationInitiationMetadata:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: conversation_initiation_metadata
        conversation_initiation_metadata_event:
          $ref: >-
            #/components/schemas/ConversationInitiationMetadataConversationInitiationMetadataEvent
    UserTranscriptUserTranscriptionEvent:
      type: object
      properties:
        user_transcript:
          type: string
    UserTranscript:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: user_transcript
        user_transcription_event:
          $ref: '#/components/schemas/UserTranscriptUserTranscriptionEvent'
    AgentResponseAgentResponseEvent:
      type: object
      properties:
        agent_response:
          type: string
      required:
        - agent_response
    AgentResponse:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: agent_response
        agent_response_event:
          $ref: '#/components/schemas/AgentResponseAgentResponseEvent'
      required:
        - type
    AgentResponseCorrectionAgentResponseCorrectionEvent:
      type: object
      properties:
        original_agent_response:
          type: string
        corrected_agent_response:
          type: string
      required:
        - original_agent_response
        - corrected_agent_response
    AgentResponseCorrection:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: agent_response_correction
        agent_response_correction_event:
          $ref: >-
            #/components/schemas/AgentResponseCorrectionAgentResponseCorrectionEvent
      required:
        - type
    AudioResponseAudioEvent:
      type: object
      properties:
        audio_base_64:
          type: string
        event_id:
          type: integer
    AudioResponse:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: audio
        audio_event:
          $ref: '#/components/schemas/AudioResponseAudioEvent'
      required:
        - type
    InterruptionInterruptionEvent:
      type: object
      properties:
        event_id:
          type: integer
    Interruption:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: interruption
        interruption_event:
          $ref: '#/components/schemas/InterruptionInterruptionEvent'
      required:
        - type
    PingPingEvent:
      type: object
      properties:
        event_id:
          type: integer
        ping_ms:
          type: integer
    Ping:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: ping
        ping_event:
          $ref: '#/components/schemas/PingPingEvent'
      required:
        - type
    ClientToolCallClientToolCall:
      type: object
      properties:
        tool_name:
          type: string
        tool_call_id:
          type: string
        parameters:
          type: object
          additionalProperties:
            description: Any type
    ClientToolCall:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: client_tool_call
        client_tool_call:
          $ref: '#/components/schemas/ClientToolCallClientToolCall'
      required:
        - type
    ContextualUpdate:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: contextual_update
        text:
          type: string
      required:
        - type
        - text
    VadScoreVadScoreEvent:
      type: object
      properties:
        vad_score:
          type: number
          format: double
      required:
        - vad_score
    VadScore:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: vad_score
        vad_score_event:
          $ref: '#/components/schemas/VadScoreVadScoreEvent'
      required:
        - type
    InternalTentativeAgentResponseTentativeAgentResponseInternalEvent:
      type: object
      properties:
        tentative_agent_response:
          type: string
      required:
        - tentative_agent_response
    InternalTentativeAgentResponse:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: internal_tentative_agent_response
        tentative_agent_response_internal_event:
          $ref: >-
            #/components/schemas/InternalTentativeAgentResponseTentativeAgentResponseInternalEvent
      required:
        - type
    V1ConvaiConversationSubscribe:
      oneOf:
        - $ref: '#/components/schemas/ConversationInitiationMetadata'
        - $ref: '#/components/schemas/UserTranscript'
        - $ref: '#/components/schemas/AgentResponse'
        - $ref: '#/components/schemas/AgentResponseCorrection'
        - $ref: '#/components/schemas/AudioResponse'
        - $ref: '#/components/schemas/Interruption'
        - $ref: '#/components/schemas/Ping'
        - $ref: '#/components/schemas/ClientToolCall'
        - $ref: '#/components/schemas/ContextualUpdate'
        - $ref: '#/components/schemas/VadScore'
        - $ref: '#/components/schemas/InternalTentativeAgentResponse'
    UserAudioChunk:
      type: object
      properties:
        user_audio_chunk:
          type: string
    Pong:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: pong
        event_id:
          type: integer
      required:
        - type
    ConversationInitiationClientDataConversationConfigOverrideAgentPrompt:
      type: object
      properties:
        prompt:
          type: string
    ConversationInitiationClientDataConversationConfigOverrideAgent:
      type: object
      properties:
        prompt:
          $ref: >-
            #/components/schemas/ConversationInitiationClientDataConversationConfigOverrideAgentPrompt
        first_message:
          type: string
        language:
          type: string
    ConversationInitiationClientDataConversationConfigOverrideTts:
      type: object
      properties:
        voice_id:
          type: string
    ConversationInitiationClientDataConversationConfigOverride:
      type: object
      properties:
        agent:
          $ref: >-
            #/components/schemas/ConversationInitiationClientDataConversationConfigOverrideAgent
        tts:
          $ref: >-
            #/components/schemas/ConversationInitiationClientDataConversationConfigOverrideTts
    ConversationInitiationClientDataCustomLlmExtraBody:
      type: object
      properties:
        temperature:
          type: number
          format: double
        max_tokens:
          type: integer
    ConversationInitiationClientDataDynamicVariables:
      oneOf:
        - type: string
        - type: number
          format: double
        - type: integer
        - type: boolean
    ConversationInitiationClientData:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: conversation_initiation_client_data
        conversation_config_override:
          $ref: >-
            #/components/schemas/ConversationInitiationClientDataConversationConfigOverride
        custom_llm_extra_body:
          $ref: >-
            #/components/schemas/ConversationInitiationClientDataCustomLlmExtraBody
        dynamic_variables:
          type: object
          additionalProperties:
            $ref: >-
              #/components/schemas/ConversationInitiationClientDataDynamicVariables
      required:
        - type
    ClientToolResult:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: client_tool_result
        tool_call_id:
          type: string
        result:
          type: string
        is_error:
          type: boolean
      required:
        - type
    UserMessage:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: user_message
        text:
          type: string
      required:
        - type
    UserActivity:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: user_activity
      required:
        - type
    V1ConvaiConversationPublish:
      oneOf:
        - $ref: '#/components/schemas/UserAudioChunk'
        - $ref: '#/components/schemas/Pong'
        - $ref: '#/components/schemas/ConversationInitiationClientData'
        - $ref: '#/components/schemas/ClientToolResult'
        - $ref: '#/components/schemas/ContextualUpdate'
        - $ref: '#/components/schemas/UserMessage'
        - $ref: '#/components/schemas/UserActivity'

```


# Create agent

POST https://api.elevenlabs.io/v1/convai/agents/create
Content-Type: application/json

Create an agent from a config object

Reference: https://elevenlabs.io/docs/agents-platform/api-reference/agents/create


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Create agent
  version: endpoint_conversationalAi/agents.create
paths:
  /v1/convai/agents/create:
    post:
      operationId: create
      summary: Create agent
      description: Create an agent from a config object
      tags:
        - - subpackage_conversationalAi
          - subpackage_conversationalAi/agents
      parameters:
        - name: xi-api-key
          in: header
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CreateAgentResponseModel'
        '422':
          description: Validation Error
          content: {}
      requestBody:
        content:
          application/json:
            schema:
              $ref: >-
                #/components/schemas/Body_Create_Agent_v1_convai_agents_create_post
components:
  schemas:
    ASRQuality:
      type: string
      enum:
        - value: high
    ASRProvider:
      type: string
      enum:
        - value: elevenlabs
    ASRInputFormat:
      type: string
      enum:
        - value: pcm_8000
        - value: pcm_16000
        - value: pcm_22050
        - value: pcm_24000
        - value: pcm_44100
        - value: pcm_48000
        - value: ulaw_8000
    ASRConversationalConfig:
      type: object
      properties:
        quality:
          $ref: '#/components/schemas/ASRQuality'
        provider:
          $ref: '#/components/schemas/ASRProvider'
        user_input_audio_format:
          $ref: '#/components/schemas/ASRInputFormat'
        keywords:
          type: array
          items:
            type: string
    SoftTimeoutConfig:
      type: object
      properties:
        timeout_seconds:
          type: number
          format: double
        message:
          type: string
    TurnEagerness:
      type: string
      enum:
        - value: patient
        - value: normal
        - value: eager
    TurnConfig:
      type: object
      properties:
        turn_timeout:
          type: number
          format: double
        initial_wait_time:
          type:
            - number
            - 'null'
          format: double
        silence_end_call_timeout:
          type: number
          format: double
        soft_timeout_config:
          $ref: '#/components/schemas/SoftTimeoutConfig'
        turn_eagerness:
          $ref: '#/components/schemas/TurnEagerness'
    TTSConversationalModel:
      type: string
      enum:
        - value: eleven_turbo_v2
        - value: eleven_turbo_v2_5
        - value: eleven_flash_v2
        - value: eleven_flash_v2_5
        - value: eleven_multilingual_v2
        - value: eleven_expressive
    TTSModelFamily:
      type: string
      enum:
        - value: turbo
        - value: flash
        - value: multilingual
        - value: expressive
    TTSOptimizeStreamingLatency:
      type: string
      enum:
        - value: '0'
        - value: '1'
        - value: '2'
        - value: '3'
        - value: '4'
    SupportedVoice:
      type: object
      properties:
        label:
          type: string
        voice_id:
          type: string
        description:
          type:
            - string
            - 'null'
        language:
          type:
            - string
            - 'null'
        model_family:
          oneOf:
            - $ref: '#/components/schemas/TTSModelFamily'
            - type: 'null'
        optimize_streaming_latency:
          oneOf:
            - $ref: '#/components/schemas/TTSOptimizeStreamingLatency'
            - type: 'null'
        stability:
          type:
            - number
            - 'null'
          format: double
        speed:
          type:
            - number
            - 'null'
          format: double
        similarity_boost:
          type:
            - number
            - 'null'
          format: double
      required:
        - label
        - voice_id
    TTSOutputFormat:
      type: string
      enum:
        - value: pcm_8000
        - value: pcm_16000
        - value: pcm_22050
        - value: pcm_24000
        - value: pcm_44100
        - value: pcm_48000
        - value: ulaw_8000
    PydanticPronunciationDictionaryVersionLocator:
      type: object
      properties:
        pronunciation_dictionary_id:
          type: string
        version_id:
          type:
            - string
            - 'null'
      required:
        - pronunciation_dictionary_id
        - version_id
    TTSConversationalConfig-Input:
      type: object
      properties:
        model_id:
          $ref: '#/components/schemas/TTSConversationalModel'
        voice_id:
          type: string
        supported_voices:
          type: array
          items:
            $ref: '#/components/schemas/SupportedVoice'
        agent_output_audio_format:
          $ref: '#/components/schemas/TTSOutputFormat'
        optimize_streaming_latency:
          $ref: '#/components/schemas/TTSOptimizeStreamingLatency'
        stability:
          type: number
          format: double
        speed:
          type: number
          format: double
        similarity_boost:
          type: number
          format: double
        pronunciation_dictionary_locators:
          type: array
          items:
            $ref: '#/components/schemas/PydanticPronunciationDictionaryVersionLocator'
    ClientEvent:
      type: string
      enum:
        - value: conversation_initiation_metadata
        - value: asr_initiation_metadata
        - value: ping
        - value: audio
        - value: interruption
        - value: user_transcript
        - value: tentative_user_transcript
        - value: agent_response
        - value: agent_response_correction
        - value: client_tool_call
        - value: mcp_tool_call
        - value: mcp_connection_status
        - value: agent_tool_response
        - value: vad_score
        - value: agent_chat_response_part
        - value: internal_turn_probability
        - value: internal_tentative_agent_response
    ConversationConfig:
      type: object
      properties:
        text_only:
          type: boolean
        max_duration_seconds:
          type: integer
        client_events:
          type: array
          items:
            $ref: '#/components/schemas/ClientEvent'
    SoftTimeoutConfigOverride:
      type: object
      properties:
        message:
          type:
            - string
            - 'null'
    TurnConfigOverride:
      type: object
      properties:
        soft_timeout_config:
          oneOf:
            - $ref: '#/components/schemas/SoftTimeoutConfigOverride'
            - type: 'null'
    TTSConversationalConfigOverride:
      type: object
      properties:
        voice_id:
          type:
            - string
            - 'null'
        stability:
          type:
            - number
            - 'null'
          format: double
        speed:
          type:
            - number
            - 'null'
          format: double
        similarity_boost:
          type:
            - number
            - 'null'
          format: double
    ConversationConfigOverride:
      type: object
      properties:
        text_only:
          type:
            - boolean
            - 'null'
    LLM:
      type: string
      enum:
        - value: gpt-4o-mini
        - value: gpt-4o
        - value: gpt-4
        - value: gpt-4-turbo
        - value: gpt-4.1
        - value: gpt-4.1-mini
        - value: gpt-4.1-nano
        - value: gpt-5
        - value: gpt-5-mini
        - value: gpt-5-nano
        - value: gpt-3.5-turbo
        - value: gemini-1.5-pro
        - value: gemini-1.5-flash
        - value: gemini-2.0-flash
        - value: gemini-2.0-flash-lite
        - value: gemini-2.5-flash-lite
        - value: gemini-2.5-flash
        - value: claude-sonnet-4-5
        - value: claude-sonnet-4
        - value: claude-haiku-4-5
        - value: claude-3-7-sonnet
        - value: claude-3-5-sonnet
        - value: claude-3-5-sonnet-v1
        - value: claude-3-haiku
        - value: grok-beta
        - value: custom-llm
        - value: qwen3-4b
        - value: qwen3-30b-a3b
        - value: gpt-oss-20b
        - value: gpt-oss-120b
        - value: glm-45-air-fp8
        - value: gemini-2.5-flash-preview-09-2025
        - value: gemini-2.5-flash-lite-preview-09-2025
        - value: gemini-2.5-flash-preview-05-20
        - value: gemini-2.5-flash-preview-04-17
        - value: gemini-2.5-flash-lite-preview-06-17
        - value: gemini-2.0-flash-lite-001
        - value: gemini-2.0-flash-001
        - value: gemini-1.5-flash-002
        - value: gemini-1.5-flash-001
        - value: gemini-1.5-pro-002
        - value: gemini-1.5-pro-001
        - value: claude-sonnet-4@20250514
        - value: claude-sonnet-4-5@20250929
        - value: claude-haiku-4-5@20251001
        - value: claude-3-7-sonnet@20250219
        - value: claude-3-5-sonnet@20240620
        - value: claude-3-5-sonnet-v2@20241022
        - value: claude-3-haiku@20240307
        - value: gpt-5-2025-08-07
        - value: gpt-5-mini-2025-08-07
        - value: gpt-5-nano-2025-08-07
        - value: gpt-4.1-2025-04-14
        - value: gpt-4.1-mini-2025-04-14
        - value: gpt-4.1-nano-2025-04-14
        - value: gpt-4o-mini-2024-07-18
        - value: gpt-4o-2024-11-20
        - value: gpt-4o-2024-08-06
        - value: gpt-4o-2024-05-13
        - value: gpt-4-0613
        - value: gpt-4-0314
        - value: gpt-4-turbo-2024-04-09
        - value: gpt-3.5-turbo-0125
        - value: gpt-3.5-turbo-1106
        - value: watt-tool-8b
        - value: watt-tool-70b
    PromptAgentAPIModelOverride:
      type: object
      properties:
        prompt:
          type:
            - string
            - 'null'
        llm:
          oneOf:
            - $ref: '#/components/schemas/LLM'
            - type: 'null'
        native_mcp_server_ids:
          type:
            - array
            - 'null'
          items:
            type: string
    AgentConfigOverride-Input:
      type: object
      properties:
        first_message:
          type:
            - string
            - 'null'
        language:
          type:
            - string
            - 'null'
        prompt:
          oneOf:
            - $ref: '#/components/schemas/PromptAgentAPIModelOverride'
            - type: 'null'
    ConversationConfigClientOverride-Input:
      type: object
      properties:
        turn:
          oneOf:
            - $ref: '#/components/schemas/TurnConfigOverride'
            - type: 'null'
        tts:
          oneOf:
            - $ref: '#/components/schemas/TTSConversationalConfigOverride'
            - type: 'null'
        conversation:
          oneOf:
            - $ref: '#/components/schemas/ConversationConfigOverride'
            - type: 'null'
        agent:
          oneOf:
            - $ref: '#/components/schemas/AgentConfigOverride-Input'
            - type: 'null'
    LanguagePresetTranslation:
      type: object
      properties:
        source_hash:
          type: string
        text:
          type: string
      required:
        - source_hash
        - text
    LanguagePreset-Input:
      type: object
      properties:
        overrides:
          $ref: '#/components/schemas/ConversationConfigClientOverride-Input'
        first_message_translation:
          oneOf:
            - $ref: '#/components/schemas/LanguagePresetTranslation'
            - type: 'null'
        soft_timeout_translation:
          oneOf:
            - $ref: '#/components/schemas/LanguagePresetTranslation'
            - type: 'null'
      required:
        - overrides
    VADConfig:
      type: object
      properties: {}
    DynamicVariablesConfigDynamicVariablePlaceholders:
      oneOf:
        - type: string
        - type: number
          format: double
        - type: integer
        - type: boolean
    DynamicVariablesConfig:
      type: object
      properties:
        dynamic_variable_placeholders:
          type: object
          additionalProperties:
            $ref: >-
              #/components/schemas/DynamicVariablesConfigDynamicVariablePlaceholders
    LLMReasoningEffort:
      type: string
      enum:
        - value: minimal
        - value: low
        - value: medium
        - value: high
    DynamicVariableAssignment:
      type: object
      properties:
        source:
          type: string
          enum:
            - type: stringLiteral
              value: response
        dynamic_variable:
          type: string
        value_path:
          type: string
      required:
        - dynamic_variable
        - value_path
    ToolCallSoundType:
      type: string
      enum:
        - value: typing
        - value: elevator1
        - value: elevator2
        - value: elevator3
        - value: elevator4
    ToolCallSoundBehavior:
      type: string
      enum:
        - value: auto
        - value: always
    EndCallToolConfig:
      type: object
      properties:
        system_tool_type:
          type: string
          enum:
            - type: stringLiteral
              value: end_call
    LanguageDetectionToolConfig:
      type: object
      properties:
        system_tool_type:
          type: string
          enum:
            - type: stringLiteral
              value: language_detection
    AgentTransfer:
      type: object
      properties:
        agent_id:
          type: string
        condition:
          type: string
        delay_ms:
          type: integer
        transfer_message:
          type:
            - string
            - 'null'
        enable_transferred_agent_first_message:
          type: boolean
      required:
        - agent_id
        - condition
    TransferToAgentToolConfig:
      type: object
      properties:
        system_tool_type:
          type: string
          enum:
            - type: stringLiteral
              value: transfer_to_agent
        transfers:
          type: array
          items:
            $ref: '#/components/schemas/AgentTransfer'
      required:
        - transfers
    PhoneNumberTransferDestination:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: phone
        phone_number:
          type: string
      required:
        - phone_number
    SIPUriTransferDestination:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: sip_uri
        sip_uri:
          type: string
      required:
        - sip_uri
    PhoneNumberDynamicVariableTransferDestination:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: phone_dynamic_variable
        phone_number:
          type: string
      required:
        - phone_number
    SIPUriDynamicVariableTransferDestination:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: sip_uri_dynamic_variable
        sip_uri:
          type: string
      required:
        - sip_uri
    PhoneNumberTransferTransferDestination:
      oneOf:
        - $ref: '#/components/schemas/PhoneNumberTransferDestination'
        - $ref: '#/components/schemas/SIPUriTransferDestination'
        - $ref: '#/components/schemas/PhoneNumberDynamicVariableTransferDestination'
        - $ref: '#/components/schemas/SIPUriDynamicVariableTransferDestination'
    TransferTypeEnum:
      type: string
      enum:
        - value: conference
        - value: sip_refer
    PhoneNumberTransfer:
      type: object
      properties:
        transfer_destination:
          oneOf:
            - $ref: '#/components/schemas/PhoneNumberTransferTransferDestination'
            - type: 'null'
        phone_number:
          type:
            - string
            - 'null'
        condition:
          type: string
        transfer_type:
          $ref: '#/components/schemas/TransferTypeEnum'
      required:
        - condition
    TransferToNumberToolConfig-Input:
      type: object
      properties:
        system_tool_type:
          type: string
          enum:
            - type: stringLiteral
              value: transfer_to_number
        transfers:
          type: array
          items:
            $ref: '#/components/schemas/PhoneNumberTransfer'
        enable_client_message:
          type: boolean
      required:
        - transfers
    SkipTurnToolConfig:
      type: object
      properties:
        system_tool_type:
          type: string
          enum:
            - type: stringLiteral
              value: skip_turn
    PlayDTMFToolConfig:
      type: object
      properties:
        system_tool_type:
          type: string
          enum:
            - type: stringLiteral
              value: play_keypad_touch_tone
    VoicemailDetectionToolConfig:
      type: object
      properties:
        system_tool_type:
          type: string
          enum:
            - type: stringLiteral
              value: voicemail_detection
        voicemail_message:
          type:
            - string
            - 'null'
    SystemToolConfigInputParams:
      oneOf:
        - $ref: '#/components/schemas/EndCallToolConfig'
        - $ref: '#/components/schemas/LanguageDetectionToolConfig'
        - $ref: '#/components/schemas/TransferToAgentToolConfig'
        - $ref: '#/components/schemas/TransferToNumberToolConfig-Input'
        - $ref: '#/components/schemas/SkipTurnToolConfig'
        - $ref: '#/components/schemas/PlayDTMFToolConfig'
        - $ref: '#/components/schemas/VoicemailDetectionToolConfig'
    SystemToolConfig-Input:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: system
        name:
          type: string
        description:
          type: string
        response_timeout_secs:
          type: integer
        disable_interruptions:
          type: boolean
        force_pre_tool_speech:
          type: boolean
        assignments:
          type: array
          items:
            $ref: '#/components/schemas/DynamicVariableAssignment'
        tool_call_sound:
          oneOf:
            - $ref: '#/components/schemas/ToolCallSoundType'
            - type: 'null'
        tool_call_sound_behavior:
          $ref: '#/components/schemas/ToolCallSoundBehavior'
        params:
          $ref: '#/components/schemas/SystemToolConfigInputParams'
      required:
        - name
        - params
    BuiltInTools-Input:
      type: object
      properties:
        end_call:
          oneOf:
            - $ref: '#/components/schemas/SystemToolConfig-Input'
            - type: 'null'
        language_detection:
          oneOf:
            - $ref: '#/components/schemas/SystemToolConfig-Input'
            - type: 'null'
        transfer_to_agent:
          oneOf:
            - $ref: '#/components/schemas/SystemToolConfig-Input'
            - type: 'null'
        transfer_to_number:
          oneOf:
            - $ref: '#/components/schemas/SystemToolConfig-Input'
            - type: 'null'
        skip_turn:
          oneOf:
            - $ref: '#/components/schemas/SystemToolConfig-Input'
            - type: 'null'
        play_keypad_touch_tone:
          oneOf:
            - $ref: '#/components/schemas/SystemToolConfig-Input'
            - type: 'null'
        voicemail_detection:
          oneOf:
            - $ref: '#/components/schemas/SystemToolConfig-Input'
            - type: 'null'
    KnowledgeBaseDocumentType:
      type: string
      enum:
        - value: file
        - value: url
        - value: text
    DocumentUsageModeEnum:
      type: string
      enum:
        - value: prompt
        - value: auto
    KnowledgeBaseLocator:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/KnowledgeBaseDocumentType'
        name:
          type: string
        id:
          type: string
        usage_mode:
          $ref: '#/components/schemas/DocumentUsageModeEnum'
      required:
        - type
        - name
        - id
    ConvAISecretLocator:
      type: object
      properties:
        secret_id:
          type: string
      required:
        - secret_id
    ConvAIDynamicVariable:
      type: object
      properties:
        variable_name:
          type: string
      required:
        - variable_name
    CustomLlmRequestHeaders:
      oneOf:
        - type: string
        - $ref: '#/components/schemas/ConvAISecretLocator'
        - $ref: '#/components/schemas/ConvAIDynamicVariable'
    CustomLLM:
      type: object
      properties:
        url:
          type: string
        model_id:
          type:
            - string
            - 'null'
        api_key:
          oneOf:
            - $ref: '#/components/schemas/ConvAISecretLocator'
            - type: 'null'
        request_headers:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/CustomLlmRequestHeaders'
        api_version:
          type:
            - string
            - 'null'
      required:
        - url
    EmbeddingModelEnum:
      type: string
      enum:
        - value: e5_mistral_7b_instruct
        - value: multilingual_e5_large_instruct
    RagConfig:
      type: object
      properties:
        enabled:
          type: boolean
        embedding_model:
          $ref: '#/components/schemas/EmbeddingModelEnum'
        max_vector_distance:
          type: number
          format: double
        max_documents_length:
          type: integer
        max_retrieved_rag_chunks_count:
          type: integer
    BackupLLMDefault:
      type: object
      properties:
        preference:
          type: string
          enum:
            - type: stringLiteral
              value: default
    BackupLLMDisabled:
      type: object
      properties:
        preference:
          type: string
          enum:
            - type: stringLiteral
              value: disabled
    BackupLLMOverride:
      type: object
      properties:
        preference:
          type: string
          enum:
            - type: stringLiteral
              value: override
        order:
          type: array
          items:
            $ref: '#/components/schemas/LLM'
      required:
        - order
    PromptAgentApiModelInputBackupLlmConfig:
      oneOf:
        - $ref: '#/components/schemas/BackupLLMDefault'
        - $ref: '#/components/schemas/BackupLLMDisabled'
        - $ref: '#/components/schemas/BackupLLMOverride'
    ToolExecutionMode:
      type: string
      enum:
        - value: immediate
        - value: post_tool_speech
        - value: async
    WebhookToolApiSchemaConfigInputMethod:
      type: string
      enum:
        - value: GET
        - value: POST
        - value: PUT
        - value: PATCH
        - value: DELETE
    LiteralJsonSchemaPropertyType:
      type: string
      enum:
        - value: boolean
        - value: string
        - value: integer
        - value: number
    LiteralJsonSchemaPropertyConstantValue:
      oneOf:
        - type: string
        - type: integer
        - type: number
          format: double
        - type: boolean
    LiteralJsonSchemaProperty:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/LiteralJsonSchemaPropertyType'
        description:
          type: string
        enum:
          type:
            - array
            - 'null'
          items:
            type: string
        is_system_provided:
          type: boolean
        dynamic_variable:
          type: string
        constant_value:
          $ref: '#/components/schemas/LiteralJsonSchemaPropertyConstantValue'
      required:
        - type
    QueryParamsJsonSchema:
      type: object
      properties:
        properties:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/LiteralJsonSchemaProperty'
        required:
          type: array
          items:
            type: string
      required:
        - properties
    ArrayJsonSchemaPropertyInputItems:
      oneOf:
        - $ref: '#/components/schemas/LiteralJsonSchemaProperty'
        - $ref: '#/components/schemas/ObjectJsonSchemaProperty-Input'
        - $ref: '#/components/schemas/ArrayJsonSchemaProperty-Input'
    ArrayJsonSchemaProperty-Input:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: array
        description:
          type: string
        items:
          $ref: '#/components/schemas/ArrayJsonSchemaPropertyInputItems'
      required:
        - items
    ObjectJsonSchemaPropertyInput:
      oneOf:
        - $ref: '#/components/schemas/LiteralJsonSchemaProperty'
        - $ref: '#/components/schemas/ObjectJsonSchemaProperty-Input'
        - $ref: '#/components/schemas/ArrayJsonSchemaProperty-Input'
    ObjectJsonSchemaProperty-Input:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: object
        required:
          type: array
          items:
            type: string
        description:
          type: string
        properties:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/ObjectJsonSchemaPropertyInput'
    WebhookToolApiSchemaConfigInputRequestHeaders:
      oneOf:
        - type: string
        - $ref: '#/components/schemas/ConvAISecretLocator'
        - $ref: '#/components/schemas/ConvAIDynamicVariable'
    AuthConnectionLocator:
      type: object
      properties:
        auth_connection_id:
          type: string
      required:
        - auth_connection_id
    WebhookToolApiSchemaConfig-Input:
      type: object
      properties:
        url:
          type: string
        method:
          $ref: '#/components/schemas/WebhookToolApiSchemaConfigInputMethod'
        path_params_schema:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/LiteralJsonSchemaProperty'
        query_params_schema:
          oneOf:
            - $ref: '#/components/schemas/QueryParamsJsonSchema'
            - type: 'null'
        request_body_schema:
          oneOf:
            - $ref: '#/components/schemas/ObjectJsonSchemaProperty-Input'
            - type: 'null'
        request_headers:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/WebhookToolApiSchemaConfigInputRequestHeaders'
        auth_connection:
          oneOf:
            - $ref: '#/components/schemas/AuthConnectionLocator'
            - type: 'null'
      required:
        - url
    WebhookToolConfig-Input:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: webhook
        name:
          type: string
        description:
          type: string
        response_timeout_secs:
          type: integer
        disable_interruptions:
          type: boolean
        force_pre_tool_speech:
          type: boolean
        assignments:
          type: array
          items:
            $ref: '#/components/schemas/DynamicVariableAssignment'
        tool_call_sound:
          oneOf:
            - $ref: '#/components/schemas/ToolCallSoundType'
            - type: 'null'
        tool_call_sound_behavior:
          $ref: '#/components/schemas/ToolCallSoundBehavior'
        dynamic_variables:
          $ref: '#/components/schemas/DynamicVariablesConfig'
        execution_mode:
          $ref: '#/components/schemas/ToolExecutionMode'
        api_schema:
          $ref: '#/components/schemas/WebhookToolApiSchemaConfig-Input'
      required:
        - name
        - description
        - api_schema
    ClientToolConfig-Input:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: client
        name:
          type: string
        description:
          type: string
        response_timeout_secs:
          type: integer
        disable_interruptions:
          type: boolean
        force_pre_tool_speech:
          type: boolean
        assignments:
          type: array
          items:
            $ref: '#/components/schemas/DynamicVariableAssignment'
        tool_call_sound:
          oneOf:
            - $ref: '#/components/schemas/ToolCallSoundType'
            - type: 'null'
        tool_call_sound_behavior:
          $ref: '#/components/schemas/ToolCallSoundBehavior'
        parameters:
          oneOf:
            - $ref: '#/components/schemas/ObjectJsonSchemaProperty-Input'
            - type: 'null'
        expects_response:
          type: boolean
        dynamic_variables:
          $ref: '#/components/schemas/DynamicVariablesConfig'
        execution_mode:
          $ref: '#/components/schemas/ToolExecutionMode'
      required:
        - name
        - description
    LiteralOverrideConstantValue:
      oneOf:
        - type: string
        - type: integer
        - type: number
          format: double
        - type: boolean
    LiteralOverride:
      type: object
      properties:
        description:
          type:
            - string
            - 'null'
        dynamic_variable:
          type:
            - string
            - 'null'
        constant_value:
          oneOf:
            - $ref: '#/components/schemas/LiteralOverrideConstantValue'
            - type: 'null'
    QueryOverride:
      type: object
      properties:
        properties:
          type:
            - object
            - 'null'
          additionalProperties:
            $ref: '#/components/schemas/LiteralOverride'
        required:
          type:
            - array
            - 'null'
          items:
            type: string
    ObjectOverrideInput:
      oneOf:
        - $ref: '#/components/schemas/LiteralOverride'
        - $ref: '#/components/schemas/ObjectOverride-Input'
    ObjectOverride-Input:
      type: object
      properties:
        description:
          type:
            - string
            - 'null'
        properties:
          type:
            - object
            - 'null'
          additionalProperties:
            $ref: '#/components/schemas/ObjectOverrideInput'
        required:
          type:
            - array
            - 'null'
          items:
            type: string
    ApiIntegrationWebhookOverridesInputRequestHeaders:
      oneOf:
        - type: string
        - $ref: '#/components/schemas/ConvAIDynamicVariable'
    ApiIntegrationWebhookOverrides-Input:
      type: object
      properties:
        path_params_schema:
          type:
            - object
            - 'null'
          additionalProperties:
            $ref: '#/components/schemas/LiteralOverride'
        query_params_schema:
          oneOf:
            - $ref: '#/components/schemas/QueryOverride'
            - type: 'null'
        request_body_schema:
          oneOf:
            - $ref: '#/components/schemas/ObjectOverride-Input'
            - type: 'null'
        request_headers:
          type:
            - object
            - 'null'
          additionalProperties:
            $ref: >-
              #/components/schemas/ApiIntegrationWebhookOverridesInputRequestHeaders
    ApiIntegrationWebhookToolConfig-Input:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: api_integration_webhook
        name:
          type: string
        description:
          type: string
        response_timeout_secs:
          type: integer
        disable_interruptions:
          type: boolean
        force_pre_tool_speech:
          type: boolean
        assignments:
          type: array
          items:
            $ref: '#/components/schemas/DynamicVariableAssignment'
        tool_call_sound:
          oneOf:
            - $ref: '#/components/schemas/ToolCallSoundType'
            - type: 'null'
        tool_call_sound_behavior:
          $ref: '#/components/schemas/ToolCallSoundBehavior'
        dynamic_variables:
          $ref: '#/components/schemas/DynamicVariablesConfig'
        execution_mode:
          $ref: '#/components/schemas/ToolExecutionMode'
        tool_version:
          type: string
        api_integration_id:
          type: string
        api_integration_connection_id:
          type: string
        api_schema_overrides:
          oneOf:
            - $ref: '#/components/schemas/ApiIntegrationWebhookOverrides-Input'
            - type: 'null'
      required:
        - name
        - description
        - api_integration_id
        - api_integration_connection_id
    PromptAgentApiModelInputToolsItems:
      oneOf:
        - $ref: '#/components/schemas/WebhookToolConfig-Input'
        - $ref: '#/components/schemas/ClientToolConfig-Input'
        - $ref: '#/components/schemas/SystemToolConfig-Input'
        - $ref: '#/components/schemas/ApiIntegrationWebhookToolConfig-Input'
    PromptAgentAPIModel-Input:
      type: object
      properties:
        prompt:
          type: string
        llm:
          $ref: '#/components/schemas/LLM'
        reasoning_effort:
          oneOf:
            - $ref: '#/components/schemas/LLMReasoningEffort'
            - type: 'null'
        thinking_budget:
          type:
            - integer
            - 'null'
        temperature:
          type: number
          format: double
        max_tokens:
          type: integer
        tool_ids:
          type: array
          items:
            type: string
        built_in_tools:
          $ref: '#/components/schemas/BuiltInTools-Input'
        mcp_server_ids:
          type: array
          items:
            type: string
        native_mcp_server_ids:
          type: array
          items:
            type: string
        knowledge_base:
          type: array
          items:
            $ref: '#/components/schemas/KnowledgeBaseLocator'
        custom_llm:
          oneOf:
            - $ref: '#/components/schemas/CustomLLM'
            - type: 'null'
        ignore_default_personality:
          type:
            - boolean
            - 'null'
        rag:
          $ref: '#/components/schemas/RagConfig'
        timezone:
          type:
            - string
            - 'null'
        backup_llm_config:
          $ref: '#/components/schemas/PromptAgentApiModelInputBackupLlmConfig'
        tools:
          type: array
          items:
            $ref: '#/components/schemas/PromptAgentApiModelInputToolsItems'
    AgentConfigAPIModel-Input:
      type: object
      properties:
        first_message:
          type: string
        language:
          type: string
        dynamic_variables:
          $ref: '#/components/schemas/DynamicVariablesConfig'
        disable_first_message_interruptions:
          type: boolean
        prompt:
          $ref: '#/components/schemas/PromptAgentAPIModel-Input'
    ConversationalConfigAPIModel-Input:
      type: object
      properties:
        asr:
          $ref: '#/components/schemas/ASRConversationalConfig'
        turn:
          $ref: '#/components/schemas/TurnConfig'
        tts:
          $ref: '#/components/schemas/TTSConversationalConfig-Input'
        conversation:
          $ref: '#/components/schemas/ConversationConfig'
        language_presets:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/LanguagePreset-Input'
        vad:
          $ref: '#/components/schemas/VADConfig'
        agent:
          $ref: '#/components/schemas/AgentConfigAPIModel-Input'
    PromptEvaluationCriteria:
      type: object
      properties:
        id:
          type: string
        name:
          type: string
        type:
          type: string
          enum:
            - type: stringLiteral
              value: prompt
        conversation_goal_prompt:
          type: string
        use_knowledge_base:
          type: boolean
      required:
        - id
        - name
        - conversation_goal_prompt
    EvaluationSettings:
      type: object
      properties:
        criteria:
          type: array
          items:
            $ref: '#/components/schemas/PromptEvaluationCriteria'
    EmbedVariant:
      type: string
      enum:
        - value: tiny
        - value: compact
        - value: full
        - value: expandable
    WidgetPlacement:
      type: string
      enum:
        - value: top-left
        - value: top
        - value: top-right
        - value: bottom-left
        - value: bottom
        - value: bottom-right
    WidgetExpandable:
      type: string
      enum:
        - value: never
        - value: mobile
        - value: desktop
        - value: always
    OrbAvatar:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: orb
        color_1:
          type: string
        color_2:
          type: string
    URLAvatar:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: url
        custom_url:
          type: string
    ImageAvatar:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: image
        url:
          type: string
    WidgetConfigInputAvatar:
      oneOf:
        - $ref: '#/components/schemas/OrbAvatar'
        - $ref: '#/components/schemas/URLAvatar'
        - $ref: '#/components/schemas/ImageAvatar'
    WidgetFeedbackMode:
      type: string
      enum:
        - value: none
        - value: during
        - value: end
    WidgetEndFeedbackType:
      type: string
      enum:
        - value: rating
    WidgetEndFeedbackConfig:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/WidgetEndFeedbackType'
    WidgetTextContents:
      type: object
      properties:
        main_label:
          type:
            - string
            - 'null'
        start_call:
          type:
            - string
            - 'null'
        start_chat:
          type:
            - string
            - 'null'
        new_call:
          type:
            - string
            - 'null'
        end_call:
          type:
            - string
            - 'null'
        mute_microphone:
          type:
            - string
            - 'null'
        change_language:
          type:
            - string
            - 'null'
        collapse:
          type:
            - string
            - 'null'
        expand:
          type:
            - string
            - 'null'
        copied:
          type:
            - string
            - 'null'
        accept_terms:
          type:
            - string
            - 'null'
        dismiss_terms:
          type:
            - string
            - 'null'
        listening_status:
          type:
            - string
            - 'null'
        speaking_status:
          type:
            - string
            - 'null'
        connecting_status:
          type:
            - string
            - 'null'
        chatting_status:
          type:
            - string
            - 'null'
        input_label:
          type:
            - string
            - 'null'
        input_placeholder:
          type:
            - string
            - 'null'
        input_placeholder_text_only:
          type:
            - string
            - 'null'
        input_placeholder_new_conversation:
          type:
            - string
            - 'null'
        user_ended_conversation:
          type:
            - string
            - 'null'
        agent_ended_conversation:
          type:
            - string
            - 'null'
        conversation_id:
          type:
            - string
            - 'null'
        error_occurred:
          type:
            - string
            - 'null'
        copy_id:
          type:
            - string
            - 'null'
    WidgetStyles:
      type: object
      properties:
        base:
          type:
            - string
            - 'null'
        base_hover:
          type:
            - string
            - 'null'
        base_active:
          type:
            - string
            - 'null'
        base_border:
          type:
            - string
            - 'null'
        base_subtle:
          type:
            - string
            - 'null'
        base_primary:
          type:
            - string
            - 'null'
        base_error:
          type:
            - string
            - 'null'
        accent:
          type:
            - string
            - 'null'
        accent_hover:
          type:
            - string
            - 'null'
        accent_active:
          type:
            - string
            - 'null'
        accent_border:
          type:
            - string
            - 'null'
        accent_subtle:
          type:
            - string
            - 'null'
        accent_primary:
          type:
            - string
            - 'null'
        overlay_padding:
          type:
            - number
            - 'null'
          format: double
        button_radius:
          type:
            - number
            - 'null'
          format: double
        input_radius:
          type:
            - number
            - 'null'
          format: double
        bubble_radius:
          type:
            - number
            - 'null'
          format: double
        sheet_radius:
          type:
            - number
            - 'null'
          format: double
        compact_sheet_radius:
          type:
            - number
            - 'null'
          format: double
        dropdown_sheet_radius:
          type:
            - number
            - 'null'
          format: double
    WidgetLanguagePreset:
      type: object
      properties:
        text_contents:
          oneOf:
            - $ref: '#/components/schemas/WidgetTextContents'
            - type: 'null'
    WidgetConfig-Input:
      type: object
      properties:
        variant:
          $ref: '#/components/schemas/EmbedVariant'
        placement:
          $ref: '#/components/schemas/WidgetPlacement'
        expandable:
          $ref: '#/components/schemas/WidgetExpandable'
        avatar:
          $ref: '#/components/schemas/WidgetConfigInputAvatar'
        feedback_mode:
          $ref: '#/components/schemas/WidgetFeedbackMode'
        end_feedback:
          oneOf:
            - $ref: '#/components/schemas/WidgetEndFeedbackConfig'
            - type: 'null'
        bg_color:
          type: string
        text_color:
          type: string
        btn_color:
          type: string
        btn_text_color:
          type: string
        border_color:
          type: string
        focus_color:
          type: string
        border_radius:
          type:
            - integer
            - 'null'
        btn_radius:
          type:
            - integer
            - 'null'
        action_text:
          type:
            - string
            - 'null'
        start_call_text:
          type:
            - string
            - 'null'
        end_call_text:
          type:
            - string
            - 'null'
        expand_text:
          type:
            - string
            - 'null'
        listening_text:
          type:
            - string
            - 'null'
        speaking_text:
          type:
            - string
            - 'null'
        shareable_page_text:
          type:
            - string
            - 'null'
        shareable_page_show_terms:
          type: boolean
        terms_text:
          type:
            - string
            - 'null'
        terms_html:
          type:
            - string
            - 'null'
        terms_key:
          type:
            - string
            - 'null'
        show_avatar_when_collapsed:
          type:
            - boolean
            - 'null'
        disable_banner:
          type: boolean
        override_link:
          type:
            - string
            - 'null'
        mic_muting_enabled:
          type: boolean
        transcript_enabled:
          type: boolean
        text_input_enabled:
          type: boolean
        default_expanded:
          type: boolean
        always_expanded:
          type: boolean
        text_contents:
          $ref: '#/components/schemas/WidgetTextContents'
        styles:
          $ref: '#/components/schemas/WidgetStyles'
        language_selector:
          type: boolean
        supports_text_only:
          type: boolean
        custom_avatar_path:
          type:
            - string
            - 'null'
        language_presets:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/WidgetLanguagePreset'
    SoftTimeoutConfigOverrideConfig:
      type: object
      properties:
        message:
          type: boolean
    TurnConfigOverrideConfig:
      type: object
      properties:
        soft_timeout_config:
          $ref: '#/components/schemas/SoftTimeoutConfigOverrideConfig'
    TTSConversationalConfigOverrideConfig:
      type: object
      properties:
        voice_id:
          type: boolean
        stability:
          type: boolean
        speed:
          type: boolean
        similarity_boost:
          type: boolean
    ConversationConfigOverrideConfig:
      type: object
      properties:
        text_only:
          type: boolean
    PromptAgentAPIModelOverrideConfig:
      type: object
      properties:
        prompt:
          type: boolean
        llm:
          type: boolean
        native_mcp_server_ids:
          type: boolean
    AgentConfigOverrideConfig:
      type: object
      properties:
        first_message:
          type: boolean
        language:
          type: boolean
        prompt:
          $ref: '#/components/schemas/PromptAgentAPIModelOverrideConfig'
    ConversationConfigClientOverrideConfig-Input:
      type: object
      properties:
        turn:
          $ref: '#/components/schemas/TurnConfigOverrideConfig'
        tts:
          $ref: '#/components/schemas/TTSConversationalConfigOverrideConfig'
        conversation:
          $ref: '#/components/schemas/ConversationConfigOverrideConfig'
        agent:
          $ref: '#/components/schemas/AgentConfigOverrideConfig'
    ConversationInitiationClientDataConfig-Input:
      type: object
      properties:
        conversation_config_override:
          $ref: '#/components/schemas/ConversationConfigClientOverrideConfig-Input'
        custom_llm_extra_body:
          type: boolean
        enable_conversation_initiation_client_data_from_webhook:
          type: boolean
    ConversationInitiationClientDataWebhookRequestHeaders:
      oneOf:
        - type: string
        - $ref: '#/components/schemas/ConvAISecretLocator'
    ConversationInitiationClientDataWebhook:
      type: object
      properties:
        url:
          type: string
        request_headers:
          type: object
          additionalProperties:
            $ref: >-
              #/components/schemas/ConversationInitiationClientDataWebhookRequestHeaders
      required:
        - url
        - request_headers
    WebhookEventType:
      type: string
      enum:
        - value: transcript
        - value: audio
        - value: call_initiation_failure
    ConvAIWebhooks:
      type: object
      properties:
        post_call_webhook_id:
          type:
            - string
            - 'null'
        events:
          type: array
          items:
            $ref: '#/components/schemas/WebhookEventType'
        send_audio:
          type:
            - boolean
            - 'null'
    AgentWorkspaceOverrides-Input:
      type: object
      properties:
        conversation_initiation_client_data_webhook:
          oneOf:
            - $ref: '#/components/schemas/ConversationInitiationClientDataWebhook'
            - type: 'null'
        webhooks:
          $ref: '#/components/schemas/ConvAIWebhooks'
    AttachedTestModel:
      type: object
      properties:
        test_id:
          type: string
        workflow_node_id:
          type:
            - string
            - 'null'
      required:
        - test_id
    AgentTestingSettings:
      type: object
      properties:
        attached_tests:
          type: array
          items:
            $ref: '#/components/schemas/AttachedTestModel'
    AllowlistItem:
      type: object
      properties:
        hostname:
          type: string
      required:
        - hostname
    AuthSettings:
      type: object
      properties:
        enable_auth:
          type: boolean
        allowlist:
          type: array
          items:
            $ref: '#/components/schemas/AllowlistItem'
        shareable_token:
          type:
            - string
            - 'null'
    AgentCallLimits:
      type: object
      properties:
        agent_concurrency_limit:
          type: integer
        daily_limit:
          type: integer
        bursting_enabled:
          type: boolean
    PrivacyConfig:
      type: object
      properties:
        record_voice:
          type: boolean
        retention_days:
          type: integer
        delete_transcript_and_pii:
          type: boolean
        delete_audio:
          type: boolean
        apply_to_existing_conversations:
          type: boolean
        zero_retention_mode:
          type: boolean
    AgentPlatformSettingsRequestModel:
      type: object
      properties:
        evaluation:
          $ref: '#/components/schemas/EvaluationSettings'
        widget:
          $ref: '#/components/schemas/WidgetConfig-Input'
        data_collection:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/LiteralJsonSchemaProperty'
        overrides:
          $ref: '#/components/schemas/ConversationInitiationClientDataConfig-Input'
        workspace_overrides:
          $ref: '#/components/schemas/AgentWorkspaceOverrides-Input'
        testing:
          $ref: '#/components/schemas/AgentTestingSettings'
        archived:
          type: boolean
        auth:
          $ref: '#/components/schemas/AuthSettings'
        call_limits:
          $ref: '#/components/schemas/AgentCallLimits'
        privacy:
          $ref: '#/components/schemas/PrivacyConfig'
    WorkflowUnconditionalModel-Input:
      type: object
      properties:
        label:
          type:
            - string
            - 'null'
        type:
          type: string
          enum:
            - type: stringLiteral
              value: unconditional
    WorkflowLLMConditionModel-Input:
      type: object
      properties:
        label:
          type:
            - string
            - 'null'
        type:
          type: string
          enum:
            - type: stringLiteral
              value: llm
        condition:
          type: string
      required:
        - condition
    WorkflowResultConditionModel-Input:
      type: object
      properties:
        label:
          type:
            - string
            - 'null'
        type:
          type: string
          enum:
            - type: stringLiteral
              value: result
        successful:
          type: boolean
      required:
        - successful
    ASTStringNode-Input:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: string_literal
        value:
          type: string
      required:
        - value
    ASTNumberNode-Input:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: number_literal
        value:
          type: number
          format: double
      required:
        - value
    ASTBooleanNode-Input:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: boolean_literal
        value:
          type: boolean
      required:
        - value
    ASTLLMNode-Input:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: llm
        prompt:
          type: string
      required:
        - prompt
    ASTDynamicVariableNode-Input:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: dynamic_variable
        name:
          type: string
      required:
        - name
    AstLessThanOrEqualsOperatorNodeInputLeft:
      oneOf:
        - $ref: '#/components/schemas/ASTStringNode-Input'
        - $ref: '#/components/schemas/ASTNumberNode-Input'
        - $ref: '#/components/schemas/ASTBooleanNode-Input'
        - $ref: '#/components/schemas/ASTLLMNode-Input'
        - $ref: '#/components/schemas/ASTDynamicVariableNode-Input'
        - $ref: '#/components/schemas/ASTOrOperatorNode-Input'
        - $ref: '#/components/schemas/ASTAndOperatorNode-Input'
        - $ref: '#/components/schemas/ASTEqualsOperatorNode-Input'
        - $ref: '#/components/schemas/ASTNotEqualsOperatorNode-Input'
        - $ref: '#/components/schemas/ASTGreaterThanOperatorNode-Input'
        - $ref: '#/components/schemas/ASTLessThanOperatorNode-Input'
        - $ref: '#/components/schemas/ASTGreaterThanOrEqualsOperatorNode-Input'
        - $ref: '#/components/schemas/ASTLessThanOrEqualsOperatorNode-Input'
    AstLessThanOrEqualsOperatorNodeInputRight:
      oneOf:
        - $ref: '#/components/schemas/ASTStringNode-Input'
        - $ref: '#/components/schemas/ASTNumberNode-Input'
        - $ref: '#/components/schemas/ASTBooleanNode-Input'
        - $ref: '#/components/schemas/ASTLLMNode-Input'
        - $ref: '#/components/schemas/ASTDynamicVariableNode-Input'
        - $ref: '#/components/schemas/ASTOrOperatorNode-Input'
        - $ref: '#/components/schemas/ASTAndOperatorNode-Input'
        - $ref: '#/components/schemas/ASTEqualsOperatorNode-Input'
        - $ref: '#/components/schemas/ASTNotEqualsOperatorNode-Input'
        - $ref: '#/components/schemas/ASTGreaterThanOperatorNode-Input'
        - $ref: '#/components/schemas/ASTLessThanOperatorNode-Input'
        - $ref: '#/components/schemas/ASTGreaterThanOrEqualsOperatorNode-Input'
        - $ref: '#/components/schemas/ASTLessThanOrEqualsOperatorNode-Input'
    ASTLessThanOrEqualsOperatorNode-Input:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: lte_operator
        left:
          $ref: '#/components/schemas/AstLessThanOrEqualsOperatorNodeInputLeft'
        right:
          $ref: '#/components/schemas/AstLessThanOrEqualsOperatorNodeInputRight'
      required:
        - left
        - right
    AstGreaterThanOrEqualsOperatorNodeInputLeft:
      oneOf:
        - $ref: '#/components/schemas/ASTStringNode-Input'
        - $ref: '#/components/schemas/ASTNumberNode-Input'
        - $ref: '#/components/schemas/ASTBooleanNode-Input'
        - $ref: '#/components/schemas/ASTLLMNode-Input'
        - $ref: '#/components/schemas/ASTDynamicVariableNode-Input'
        - $ref: '#/components/schemas/ASTOrOperatorNode-Input'
        - $ref: '#/components/schemas/ASTAndOperatorNode-Input'
        - $ref: '#/components/schemas/ASTEqualsOperatorNode-Input'
        - $ref: '#/components/schemas/ASTNotEqualsOperatorNode-Input'
        - $ref: '#/components/schemas/ASTGreaterThanOperatorNode-Input'
        - $ref: '#/components/schemas/ASTLessThanOperatorNode-Input'
        - $ref: '#/components/schemas/ASTGreaterThanOrEqualsOperatorNode-Input'
        - $ref: '#/components/schemas/ASTLessThanOrEqualsOperatorNode-Input'
    AstGreaterThanOrEqualsOperatorNodeInputRight:
      oneOf:
        - $ref: '#/components/schemas/ASTStringNode-Input'
        - $ref: '#/components/schemas/ASTNumberNode-Input'
        - $ref: '#/components/schemas/ASTBooleanNode-Input'
        - $ref: '#/components/schemas/ASTLLMNode-Input'
        - $ref: '#/components/schemas/ASTDynamicVariableNode-Input'
        - $ref: '#/components/schemas/ASTOrOperatorNode-Input'
        - $ref: '#/components/schemas/ASTAndOperatorNode-Input'
        - $ref: '#/components/schemas/ASTEqualsOperatorNode-Input'
        - $ref: '#/components/schemas/ASTNotEqualsOperatorNode-Input'
        - $ref: '#/components/schemas/ASTGreaterThanOperatorNode-Input'
        - $ref: '#/components/schemas/ASTLessThanOperatorNode-Input'
        - $ref: '#/components/schemas/ASTGreaterThanOrEqualsOperatorNode-Input'
        - $ref: '#/components/schemas/ASTLessThanOrEqualsOperatorNode-Input'
    ASTGreaterThanOrEqualsOperatorNode-Input:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: gte_operator
        left:
          $ref: '#/components/schemas/AstGreaterThanOrEqualsOperatorNodeInputLeft'
        right:
          $ref: '#/components/schemas/AstGreaterThanOrEqualsOperatorNodeInputRight'
      required:
        - left
        - right
    AstLessThanOperatorNodeInputLeft:
      oneOf:
        - $ref: '#/components/schemas/ASTStringNode-Input'
        - $ref: '#/components/schemas/ASTNumberNode-Input'
        - $ref: '#/components/schemas/ASTBooleanNode-Input'
        - $ref: '#/components/schemas/ASTLLMNode-Input'
        - $ref: '#/components/schemas/ASTDynamicVariableNode-Input'
        - $ref: '#/components/schemas/ASTOrOperatorNode-Input'
        - $ref: '#/components/schemas/ASTAndOperatorNode-Input'
        - $ref: '#/components/schemas/ASTEqualsOperatorNode-Input'
        - $ref: '#/components/schemas/ASTNotEqualsOperatorNode-Input'
        - $ref: '#/components/schemas/ASTGreaterThanOperatorNode-Input'
        - $ref: '#/components/schemas/ASTLessThanOperatorNode-Input'
        - $ref: '#/components/schemas/ASTGreaterThanOrEqualsOperatorNode-Input'
        - $ref: '#/components/schemas/ASTLessThanOrEqualsOperatorNode-Input'
    AstLessThanOperatorNodeInputRight:
      oneOf:
        - $ref: '#/components/schemas/ASTStringNode-Input'
        - $ref: '#/components/schemas/ASTNumberNode-Input'
        - $ref: '#/components/schemas/ASTBooleanNode-Input'
        - $ref: '#/components/schemas/ASTLLMNode-Input'
        - $ref: '#/components/schemas/ASTDynamicVariableNode-Input'
        - $ref: '#/components/schemas/ASTOrOperatorNode-Input'
        - $ref: '#/components/schemas/ASTAndOperatorNode-Input'
        - $ref: '#/components/schemas/ASTEqualsOperatorNode-Input'
        - $ref: '#/components/schemas/ASTNotEqualsOperatorNode-Input'
        - $ref: '#/components/schemas/ASTGreaterThanOperatorNode-Input'
        - $ref: '#/components/schemas/ASTLessThanOperatorNode-Input'
        - $ref: '#/components/schemas/ASTGreaterThanOrEqualsOperatorNode-Input'
        - $ref: '#/components/schemas/ASTLessThanOrEqualsOperatorNode-Input'
    ASTLessThanOperatorNode-Input:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: lt_operator
        left:
          $ref: '#/components/schemas/AstLessThanOperatorNodeInputLeft'
        right:
          $ref: '#/components/schemas/AstLessThanOperatorNodeInputRight'
      required:
        - left
        - right
    AstGreaterThanOperatorNodeInputLeft:
      oneOf:
        - $ref: '#/components/schemas/ASTStringNode-Input'
        - $ref: '#/components/schemas/ASTNumberNode-Input'
        - $ref: '#/components/schemas/ASTBooleanNode-Input'
        - $ref: '#/components/schemas/ASTLLMNode-Input'
        - $ref: '#/components/schemas/ASTDynamicVariableNode-Input'
        - $ref: '#/components/schemas/ASTOrOperatorNode-Input'
        - $ref: '#/components/schemas/ASTAndOperatorNode-Input'
        - $ref: '#/components/schemas/ASTEqualsOperatorNode-Input'
        - $ref: '#/components/schemas/ASTNotEqualsOperatorNode-Input'
        - $ref: '#/components/schemas/ASTGreaterThanOperatorNode-Input'
        - $ref: '#/components/schemas/ASTLessThanOperatorNode-Input'
        - $ref: '#/components/schemas/ASTGreaterThanOrEqualsOperatorNode-Input'
        - $ref: '#/components/schemas/ASTLessThanOrEqualsOperatorNode-Input'
    AstGreaterThanOperatorNodeInputRight:
      oneOf:
        - $ref: '#/components/schemas/ASTStringNode-Input'
        - $ref: '#/components/schemas/ASTNumberNode-Input'
        - $ref: '#/components/schemas/ASTBooleanNode-Input'
        - $ref: '#/components/schemas/ASTLLMNode-Input'
        - $ref: '#/components/schemas/ASTDynamicVariableNode-Input'
        - $ref: '#/components/schemas/ASTOrOperatorNode-Input'
        - $ref: '#/components/schemas/ASTAndOperatorNode-Input'
        - $ref: '#/components/schemas/ASTEqualsOperatorNode-Input'
        - $ref: '#/components/schemas/ASTNotEqualsOperatorNode-Input'
        - $ref: '#/components/schemas/ASTGreaterThanOperatorNode-Input'
        - $ref: '#/components/schemas/ASTLessThanOperatorNode-Input'
        - $ref: '#/components/schemas/ASTGreaterThanOrEqualsOperatorNode-Input'
        - $ref: '#/components/schemas/ASTLessThanOrEqualsOperatorNode-Input'
    ASTGreaterThanOperatorNode-Input:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: gt_operator
        left:
          $ref: '#/components/schemas/AstGreaterThanOperatorNodeInputLeft'
        right:
          $ref: '#/components/schemas/AstGreaterThanOperatorNodeInputRight'
      required:
        - left
        - right
    AstNotEqualsOperatorNodeInputLeft:
      oneOf:
        - $ref: '#/components/schemas/ASTStringNode-Input'
        - $ref: '#/components/schemas/ASTNumberNode-Input'
        - $ref: '#/components/schemas/ASTBooleanNode-Input'
        - $ref: '#/components/schemas/ASTLLMNode-Input'
        - $ref: '#/components/schemas/ASTDynamicVariableNode-Input'
        - $ref: '#/components/schemas/ASTOrOperatorNode-Input'
        - $ref: '#/components/schemas/ASTAndOperatorNode-Input'
        - $ref: '#/components/schemas/ASTEqualsOperatorNode-Input'
        - $ref: '#/components/schemas/ASTNotEqualsOperatorNode-Input'
        - $ref: '#/components/schemas/ASTGreaterThanOperatorNode-Input'
        - $ref: '#/components/schemas/ASTLessThanOperatorNode-Input'
        - $ref: '#/components/schemas/ASTGreaterThanOrEqualsOperatorNode-Input'
        - $ref: '#/components/schemas/ASTLessThanOrEqualsOperatorNode-Input'
    AstNotEqualsOperatorNodeInputRight:
      oneOf:
        - $ref: '#/components/schemas/ASTStringNode-Input'
        - $ref: '#/components/schemas/ASTNumberNode-Input'
        - $ref: '#/components/schemas/ASTBooleanNode-Input'
        - $ref: '#/components/schemas/ASTLLMNode-Input'
        - $ref: '#/components/schemas/ASTDynamicVariableNode-Input'
        - $ref: '#/components/schemas/ASTOrOperatorNode-Input'
        - $ref: '#/components/schemas/ASTAndOperatorNode-Input'
        - $ref: '#/components/schemas/ASTEqualsOperatorNode-Input'
        - $ref: '#/components/schemas/ASTNotEqualsOperatorNode-Input'
        - $ref: '#/components/schemas/ASTGreaterThanOperatorNode-Input'
        - $ref: '#/components/schemas/ASTLessThanOperatorNode-Input'
        - $ref: '#/components/schemas/ASTGreaterThanOrEqualsOperatorNode-Input'
        - $ref: '#/components/schemas/ASTLessThanOrEqualsOperatorNode-Input'
    ASTNotEqualsOperatorNode-Input:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: neq_operator
        left:
          $ref: '#/components/schemas/AstNotEqualsOperatorNodeInputLeft'
        right:
          $ref: '#/components/schemas/AstNotEqualsOperatorNodeInputRight'
      required:
        - left
        - right
    AstEqualsOperatorNodeInputLeft:
      oneOf:
        - $ref: '#/components/schemas/ASTStringNode-Input'
        - $ref: '#/components/schemas/ASTNumberNode-Input'
        - $ref: '#/components/schemas/ASTBooleanNode-Input'
        - $ref: '#/components/schemas/ASTLLMNode-Input'
        - $ref: '#/components/schemas/ASTDynamicVariableNode-Input'
        - $ref: '#/components/schemas/ASTOrOperatorNode-Input'
        - $ref: '#/components/schemas/ASTAndOperatorNode-Input'
        - $ref: '#/components/schemas/ASTEqualsOperatorNode-Input'
        - $ref: '#/components/schemas/ASTNotEqualsOperatorNode-Input'
        - $ref: '#/components/schemas/ASTGreaterThanOperatorNode-Input'
        - $ref: '#/components/schemas/ASTLessThanOperatorNode-Input'
        - $ref: '#/components/schemas/ASTGreaterThanOrEqualsOperatorNode-Input'
        - $ref: '#/components/schemas/ASTLessThanOrEqualsOperatorNode-Input'
    AstEqualsOperatorNodeInputRight:
      oneOf:
        - $ref: '#/components/schemas/ASTStringNode-Input'
        - $ref: '#/components/schemas/ASTNumberNode-Input'
        - $ref: '#/components/schemas/ASTBooleanNode-Input'
        - $ref: '#/components/schemas/ASTLLMNode-Input'
        - $ref: '#/components/schemas/ASTDynamicVariableNode-Input'
        - $ref: '#/components/schemas/ASTOrOperatorNode-Input'
        - $ref: '#/components/schemas/ASTAndOperatorNode-Input'
        - $ref: '#/components/schemas/ASTEqualsOperatorNode-Input'
        - $ref: '#/components/schemas/ASTNotEqualsOperatorNode-Input'
        - $ref: '#/components/schemas/ASTGreaterThanOperatorNode-Input'
        - $ref: '#/components/schemas/ASTLessThanOperatorNode-Input'
        - $ref: '#/components/schemas/ASTGreaterThanOrEqualsOperatorNode-Input'
        - $ref: '#/components/schemas/ASTLessThanOrEqualsOperatorNode-Input'
    ASTEqualsOperatorNode-Input:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: eq_operator
        left:
          $ref: '#/components/schemas/AstEqualsOperatorNodeInputLeft'
        right:
          $ref: '#/components/schemas/AstEqualsOperatorNodeInputRight'
      required:
        - left
        - right
    AstAndOperatorNodeInputChildrenItems:
      oneOf:
        - $ref: '#/components/schemas/ASTStringNode-Input'
        - $ref: '#/components/schemas/ASTNumberNode-Input'
        - $ref: '#/components/schemas/ASTBooleanNode-Input'
        - $ref: '#/components/schemas/ASTLLMNode-Input'
        - $ref: '#/components/schemas/ASTDynamicVariableNode-Input'
        - $ref: '#/components/schemas/ASTOrOperatorNode-Input'
        - $ref: '#/components/schemas/ASTAndOperatorNode-Input'
        - $ref: '#/components/schemas/ASTEqualsOperatorNode-Input'
        - $ref: '#/components/schemas/ASTNotEqualsOperatorNode-Input'
        - $ref: '#/components/schemas/ASTGreaterThanOperatorNode-Input'
        - $ref: '#/components/schemas/ASTLessThanOperatorNode-Input'
        - $ref: '#/components/schemas/ASTGreaterThanOrEqualsOperatorNode-Input'
        - $ref: '#/components/schemas/ASTLessThanOrEqualsOperatorNode-Input'
    ASTAndOperatorNode-Input:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: and_operator
        children:
          type: array
          items:
            $ref: '#/components/schemas/AstAndOperatorNodeInputChildrenItems'
      required:
        - children
    AstOrOperatorNodeInputChildrenItems:
      oneOf:
        - $ref: '#/components/schemas/ASTStringNode-Input'
        - $ref: '#/components/schemas/ASTNumberNode-Input'
        - $ref: '#/components/schemas/ASTBooleanNode-Input'
        - $ref: '#/components/schemas/ASTLLMNode-Input'
        - $ref: '#/components/schemas/ASTDynamicVariableNode-Input'
        - $ref: '#/components/schemas/ASTOrOperatorNode-Input'
        - $ref: '#/components/schemas/ASTAndOperatorNode-Input'
        - $ref: '#/components/schemas/ASTEqualsOperatorNode-Input'
        - $ref: '#/components/schemas/ASTNotEqualsOperatorNode-Input'
        - $ref: '#/components/schemas/ASTGreaterThanOperatorNode-Input'
        - $ref: '#/components/schemas/ASTLessThanOperatorNode-Input'
        - $ref: '#/components/schemas/ASTGreaterThanOrEqualsOperatorNode-Input'
        - $ref: '#/components/schemas/ASTLessThanOrEqualsOperatorNode-Input'
    ASTOrOperatorNode-Input:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: or_operator
        children:
          type: array
          items:
            $ref: '#/components/schemas/AstOrOperatorNodeInputChildrenItems'
      required:
        - children
    WorkflowExpressionConditionModelInputExpression:
      oneOf:
        - $ref: '#/components/schemas/ASTStringNode-Input'
        - $ref: '#/components/schemas/ASTNumberNode-Input'
        - $ref: '#/components/schemas/ASTBooleanNode-Input'
        - $ref: '#/components/schemas/ASTLLMNode-Input'
        - $ref: '#/components/schemas/ASTDynamicVariableNode-Input'
        - $ref: '#/components/schemas/ASTOrOperatorNode-Input'
        - $ref: '#/components/schemas/ASTAndOperatorNode-Input'
        - $ref: '#/components/schemas/ASTEqualsOperatorNode-Input'
        - $ref: '#/components/schemas/ASTNotEqualsOperatorNode-Input'
        - $ref: '#/components/schemas/ASTGreaterThanOperatorNode-Input'
        - $ref: '#/components/schemas/ASTLessThanOperatorNode-Input'
        - $ref: '#/components/schemas/ASTGreaterThanOrEqualsOperatorNode-Input'
        - $ref: '#/components/schemas/ASTLessThanOrEqualsOperatorNode-Input'
    WorkflowExpressionConditionModel-Input:
      type: object
      properties:
        label:
          type:
            - string
            - 'null'
        type:
          type: string
          enum:
            - type: stringLiteral
              value: expression
        expression:
          $ref: '#/components/schemas/WorkflowExpressionConditionModelInputExpression'
      required:
        - expression
    WorkflowEdgeModelInputForwardCondition:
      oneOf:
        - $ref: '#/components/schemas/WorkflowUnconditionalModel-Input'
        - $ref: '#/components/schemas/WorkflowLLMConditionModel-Input'
        - $ref: '#/components/schemas/WorkflowResultConditionModel-Input'
        - $ref: '#/components/schemas/WorkflowExpressionConditionModel-Input'
    WorkflowEdgeModelInputBackwardCondition:
      oneOf:
        - $ref: '#/components/schemas/WorkflowUnconditionalModel-Input'
        - $ref: '#/components/schemas/WorkflowLLMConditionModel-Input'
        - $ref: '#/components/schemas/WorkflowResultConditionModel-Input'
        - $ref: '#/components/schemas/WorkflowExpressionConditionModel-Input'
    WorkflowEdgeModel-Input:
      type: object
      properties:
        source:
          type: string
        target:
          type: string
        forward_condition:
          oneOf:
            - $ref: '#/components/schemas/WorkflowEdgeModelInputForwardCondition'
            - type: 'null'
        backward_condition:
          oneOf:
            - $ref: '#/components/schemas/WorkflowEdgeModelInputBackwardCondition'
            - type: 'null'
      required:
        - source
        - target
    Position-Input:
      type: object
      properties:
        x:
          type: number
          format: double
        'y':
          type: number
          format: double
    WorkflowStartNodeModel-Input:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: start
        position:
          $ref: '#/components/schemas/Position-Input'
        edge_order:
          type: array
          items:
            type: string
    WorkflowEndNodeModel-Input:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: end
        position:
          $ref: '#/components/schemas/Position-Input'
        edge_order:
          type: array
          items:
            type: string
    WorkflowPhoneNumberNodeModelInputTransferDestination:
      oneOf:
        - $ref: '#/components/schemas/PhoneNumberTransferDestination'
        - $ref: '#/components/schemas/SIPUriTransferDestination'
        - $ref: '#/components/schemas/PhoneNumberDynamicVariableTransferDestination'
        - $ref: '#/components/schemas/SIPUriDynamicVariableTransferDestination'
    WorkflowPhoneNumberNodeModel-Input:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: phone_number
        position:
          $ref: '#/components/schemas/Position-Input'
        edge_order:
          type: array
          items:
            type: string
        transfer_destination:
          $ref: >-
            #/components/schemas/WorkflowPhoneNumberNodeModelInputTransferDestination
        transfer_type:
          $ref: '#/components/schemas/TransferTypeEnum'
      required:
        - transfer_destination
    ASRConversationalConfigWorkflowOverride:
      type: object
      properties:
        quality:
          oneOf:
            - $ref: '#/components/schemas/ASRQuality'
            - type: 'null'
        provider:
          oneOf:
            - $ref: '#/components/schemas/ASRProvider'
            - type: 'null'
        user_input_audio_format:
          oneOf:
            - $ref: '#/components/schemas/ASRInputFormat'
            - type: 'null'
        keywords:
          type:
            - array
            - 'null'
          items:
            type: string
    SoftTimeoutConfigWorkflowOverride:
      type: object
      properties:
        timeout_seconds:
          type:
            - number
            - 'null'
          format: double
        message:
          type:
            - string
            - 'null'
    TurnConfigWorkflowOverride:
      type: object
      properties:
        turn_timeout:
          type:
            - number
            - 'null'
          format: double
        initial_wait_time:
          type:
            - number
            - 'null'
          format: double
        silence_end_call_timeout:
          type:
            - number
            - 'null'
          format: double
        soft_timeout_config:
          oneOf:
            - $ref: '#/components/schemas/SoftTimeoutConfigWorkflowOverride'
            - type: 'null'
        turn_eagerness:
          oneOf:
            - $ref: '#/components/schemas/TurnEagerness'
            - type: 'null'
    TTSConversationalConfigWorkflowOverride-Input:
      type: object
      properties:
        model_id:
          oneOf:
            - $ref: '#/components/schemas/TTSConversationalModel'
            - type: 'null'
        voice_id:
          type:
            - string
            - 'null'
        supported_voices:
          type:
            - array
            - 'null'
          items:
            $ref: '#/components/schemas/SupportedVoice'
        agent_output_audio_format:
          oneOf:
            - $ref: '#/components/schemas/TTSOutputFormat'
            - type: 'null'
        optimize_streaming_latency:
          oneOf:
            - $ref: '#/components/schemas/TTSOptimizeStreamingLatency'
            - type: 'null'
        stability:
          type:
            - number
            - 'null'
          format: double
        speed:
          type:
            - number
            - 'null'
          format: double
        similarity_boost:
          type:
            - number
            - 'null'
          format: double
        pronunciation_dictionary_locators:
          type:
            - array
            - 'null'
          items:
            $ref: '#/components/schemas/PydanticPronunciationDictionaryVersionLocator'
    ConversationConfigWorkflowOverride:
      type: object
      properties:
        text_only:
          type:
            - boolean
            - 'null'
        max_duration_seconds:
          type:
            - integer
            - 'null'
        client_events:
          type:
            - array
            - 'null'
          items:
            $ref: '#/components/schemas/ClientEvent'
    VADConfigWorkflowOverride:
      type: object
      properties: {}
    DynamicVariablesConfigWorkflowOverrideDynamicVariablePlaceholders:
      oneOf:
        - type: string
        - type: number
          format: double
        - type: integer
        - type: boolean
    DynamicVariablesConfigWorkflowOverride:
      type: object
      properties:
        dynamic_variable_placeholders:
          type:
            - object
            - 'null'
          additionalProperties:
            $ref: >-
              #/components/schemas/DynamicVariablesConfigWorkflowOverrideDynamicVariablePlaceholders
    BuiltInToolsWorkflowOverride-Input:
      type: object
      properties:
        end_call:
          oneOf:
            - $ref: '#/components/schemas/SystemToolConfig-Input'
            - type: 'null'
        language_detection:
          oneOf:
            - $ref: '#/components/schemas/SystemToolConfig-Input'
            - type: 'null'
        transfer_to_agent:
          oneOf:
            - $ref: '#/components/schemas/SystemToolConfig-Input'
            - type: 'null'
        transfer_to_number:
          oneOf:
            - $ref: '#/components/schemas/SystemToolConfig-Input'
            - type: 'null'
        skip_turn:
          oneOf:
            - $ref: '#/components/schemas/SystemToolConfig-Input'
            - type: 'null'
        play_keypad_touch_tone:
          oneOf:
            - $ref: '#/components/schemas/SystemToolConfig-Input'
            - type: 'null'
        voicemail_detection:
          oneOf:
            - $ref: '#/components/schemas/SystemToolConfig-Input'
            - type: 'null'
    RagConfigWorkflowOverride:
      type: object
      properties:
        enabled:
          type:
            - boolean
            - 'null'
        embedding_model:
          oneOf:
            - $ref: '#/components/schemas/EmbeddingModelEnum'
            - type: 'null'
        max_vector_distance:
          type:
            - number
            - 'null'
          format: double
        max_documents_length:
          type:
            - integer
            - 'null'
        max_retrieved_rag_chunks_count:
          type:
            - integer
            - 'null'
    PromptAgentApiModelWorkflowOverrideInputBackupLlmConfig:
      oneOf:
        - $ref: '#/components/schemas/BackupLLMDefault'
        - $ref: '#/components/schemas/BackupLLMDisabled'
        - $ref: '#/components/schemas/BackupLLMOverride'
    PromptAgentApiModelWorkflowOverrideInputToolsItems:
      oneOf:
        - $ref: '#/components/schemas/WebhookToolConfig-Input'
        - $ref: '#/components/schemas/ClientToolConfig-Input'
        - $ref: '#/components/schemas/SystemToolConfig-Input'
        - $ref: '#/components/schemas/ApiIntegrationWebhookToolConfig-Input'
    PromptAgentAPIModelWorkflowOverride-Input:
      type: object
      properties:
        prompt:
          type:
            - string
            - 'null'
        llm:
          oneOf:
            - $ref: '#/components/schemas/LLM'
            - type: 'null'
        reasoning_effort:
          oneOf:
            - $ref: '#/components/schemas/LLMReasoningEffort'
            - type: 'null'
        thinking_budget:
          type:
            - integer
            - 'null'
        temperature:
          type:
            - number
            - 'null'
          format: double
        max_tokens:
          type:
            - integer
            - 'null'
        tool_ids:
          type:
            - array
            - 'null'
          items:
            type: string
        built_in_tools:
          oneOf:
            - $ref: '#/components/schemas/BuiltInToolsWorkflowOverride-Input'
            - type: 'null'
        mcp_server_ids:
          type:
            - array
            - 'null'
          items:
            type: string
        native_mcp_server_ids:
          type:
            - array
            - 'null'
          items:
            type: string
        knowledge_base:
          type:
            - array
            - 'null'
          items:
            $ref: '#/components/schemas/KnowledgeBaseLocator'
        custom_llm:
          oneOf:
            - $ref: '#/components/schemas/CustomLLM'
            - type: 'null'
        ignore_default_personality:
          type:
            - boolean
            - 'null'
        rag:
          oneOf:
            - $ref: '#/components/schemas/RagConfigWorkflowOverride'
            - type: 'null'
        timezone:
          type:
            - string
            - 'null'
        backup_llm_config:
          oneOf:
            - $ref: >-
                #/components/schemas/PromptAgentApiModelWorkflowOverrideInputBackupLlmConfig
            - type: 'null'
        tools:
          type:
            - array
            - 'null'
          items:
            $ref: >-
              #/components/schemas/PromptAgentApiModelWorkflowOverrideInputToolsItems
    AgentConfigAPIModelWorkflowOverride-Input:
      type: object
      properties:
        first_message:
          type:
            - string
            - 'null'
        language:
          type:
            - string
            - 'null'
        dynamic_variables:
          oneOf:
            - $ref: '#/components/schemas/DynamicVariablesConfigWorkflowOverride'
            - type: 'null'
        disable_first_message_interruptions:
          type:
            - boolean
            - 'null'
        prompt:
          oneOf:
            - $ref: '#/components/schemas/PromptAgentAPIModelWorkflowOverride-Input'
            - type: 'null'
    ConversationalConfigAPIModelWorkflowOverride-Input:
      type: object
      properties:
        asr:
          oneOf:
            - $ref: '#/components/schemas/ASRConversationalConfigWorkflowOverride'
            - type: 'null'
        turn:
          oneOf:
            - $ref: '#/components/schemas/TurnConfigWorkflowOverride'
            - type: 'null'
        tts:
          oneOf:
            - $ref: >-
                #/components/schemas/TTSConversationalConfigWorkflowOverride-Input
            - type: 'null'
        conversation:
          oneOf:
            - $ref: '#/components/schemas/ConversationConfigWorkflowOverride'
            - type: 'null'
        language_presets:
          type:
            - object
            - 'null'
          additionalProperties:
            $ref: '#/components/schemas/LanguagePreset-Input'
        vad:
          oneOf:
            - $ref: '#/components/schemas/VADConfigWorkflowOverride'
            - type: 'null'
        agent:
          oneOf:
            - $ref: '#/components/schemas/AgentConfigAPIModelWorkflowOverride-Input'
            - type: 'null'
    WorkflowOverrideAgentNodeModel-Input:
      type: object
      properties:
        conversation_config:
          $ref: >-
            #/components/schemas/ConversationalConfigAPIModelWorkflowOverride-Input
        additional_prompt:
          type: string
        additional_knowledge_base:
          type: array
          items:
            $ref: '#/components/schemas/KnowledgeBaseLocator'
        additional_tool_ids:
          type: array
          items:
            type: string
        type:
          type: string
          enum:
            - type: stringLiteral
              value: override_agent
        position:
          $ref: '#/components/schemas/Position-Input'
        edge_order:
          type: array
          items:
            type: string
        label:
          type: string
      required:
        - label
    WorkflowStandaloneAgentNodeModel-Input:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: standalone_agent
        position:
          $ref: '#/components/schemas/Position-Input'
        edge_order:
          type: array
          items:
            type: string
        agent_id:
          type: string
        delay_ms:
          type: integer
        transfer_message:
          type:
            - string
            - 'null'
        enable_transferred_agent_first_message:
          type: boolean
      required:
        - agent_id
    WorkflowToolLocator:
      type: object
      properties:
        tool_id:
          type: string
      required:
        - tool_id
    WorkflowToolNodeModel-Input:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: tool
        position:
          $ref: '#/components/schemas/Position-Input'
        edge_order:
          type: array
          items:
            type: string
        tools:
          type: array
          items:
            $ref: '#/components/schemas/WorkflowToolLocator'
    AgentWorkflowRequestModelNodes:
      oneOf:
        - $ref: '#/components/schemas/WorkflowStartNodeModel-Input'
        - $ref: '#/components/schemas/WorkflowEndNodeModel-Input'
        - $ref: '#/components/schemas/WorkflowPhoneNumberNodeModel-Input'
        - $ref: '#/components/schemas/WorkflowOverrideAgentNodeModel-Input'
        - $ref: '#/components/schemas/WorkflowStandaloneAgentNodeModel-Input'
        - $ref: '#/components/schemas/WorkflowToolNodeModel-Input'
    AgentWorkflowRequestModel:
      type: object
      properties:
        edges:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/WorkflowEdgeModel-Input'
        nodes:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/AgentWorkflowRequestModelNodes'
    Body_Create_Agent_v1_convai_agents_create_post:
      type: object
      properties:
        conversation_config:
          $ref: '#/components/schemas/ConversationalConfigAPIModel-Input'
        platform_settings:
          oneOf:
            - $ref: '#/components/schemas/AgentPlatformSettingsRequestModel'
            - type: 'null'
        workflow:
          $ref: '#/components/schemas/AgentWorkflowRequestModel'
        name:
          type:
            - string
            - 'null'
        tags:
          type:
            - array
            - 'null'
          items:
            type: string
      required:
        - conversation_config
    CreateAgentResponseModel:
      type: object
      properties:
        agent_id:
          type: string
      required:
        - agent_id

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.conversationalAi.agents.create({});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.conversational_ai.agents.create()

```

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/agents/create"

	payload := strings.NewReader("{}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("xi-api-key", "xi-api-key")
	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/convai/agents/create")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["xi-api-key"] = 'xi-api-key'
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/convai/agents/create")
  .header("xi-api-key", "xi-api-key")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/convai/agents/create', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/convai/agents/create");
var request = new RestRequest(Method.POST);
request.AddHeader("xi-api-key", "xi-api-key");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "xi-api-key": "xi-api-key",
  "Content-Type": "application/json"
]
let parameters = [] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/agents/create")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```


---
**Navigation:** [← Previous](./17-salesforce.md) | [Index](./index.md) | [Next →](./19-get-agent.md)
