**Navigation:** [← Previous](./18-websocket.md) | [Index](./index.md) | [Next →](./20-list-agents.md)

# Get agent

GET https://api.elevenlabs.io/v1/convai/agents/{agent_id}

Retrieve config for an agent

Reference: https://elevenlabs.io/docs/agents-platform/api-reference/agents/get


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Get agent
  version: endpoint_conversationalAi/agents.get
paths:
  /v1/convai/agents/{agent_id}:
    get:
      operationId: get
      summary: Get agent
      description: Retrieve config for an agent
      tags:
        - - subpackage_conversationalAi
          - subpackage_conversationalAi/agents
      parameters:
        - name: agent_id
          in: path
          description: The id of an agent. This is returned on agent creation.
          required: true
          schema:
            type: string
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
                $ref: '#/components/schemas/GetAgentResponseModel'
        '422':
          description: Validation Error
          content: {}
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
    TTSConversationalConfig-Output:
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
    AgentConfigOverride-Output:
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
    ConversationConfigClientOverride-Output:
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
            - $ref: '#/components/schemas/AgentConfigOverride-Output'
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
    LanguagePreset-Output:
      type: object
      properties:
        overrides:
          $ref: '#/components/schemas/ConversationConfigClientOverride-Output'
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
    TransferToNumberToolConfig-Output:
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
    SystemToolConfigOutputParams:
      oneOf:
        - $ref: '#/components/schemas/EndCallToolConfig'
        - $ref: '#/components/schemas/LanguageDetectionToolConfig'
        - $ref: '#/components/schemas/TransferToAgentToolConfig'
        - $ref: '#/components/schemas/TransferToNumberToolConfig-Output'
        - $ref: '#/components/schemas/SkipTurnToolConfig'
        - $ref: '#/components/schemas/PlayDTMFToolConfig'
        - $ref: '#/components/schemas/VoicemailDetectionToolConfig'
    SystemToolConfig-Output:
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
          $ref: '#/components/schemas/SystemToolConfigOutputParams'
      required:
        - name
        - params
    BuiltInTools-Output:
      type: object
      properties:
        end_call:
          oneOf:
            - $ref: '#/components/schemas/SystemToolConfig-Output'
            - type: 'null'
        language_detection:
          oneOf:
            - $ref: '#/components/schemas/SystemToolConfig-Output'
            - type: 'null'
        transfer_to_agent:
          oneOf:
            - $ref: '#/components/schemas/SystemToolConfig-Output'
            - type: 'null'
        transfer_to_number:
          oneOf:
            - $ref: '#/components/schemas/SystemToolConfig-Output'
            - type: 'null'
        skip_turn:
          oneOf:
            - $ref: '#/components/schemas/SystemToolConfig-Output'
            - type: 'null'
        play_keypad_touch_tone:
          oneOf:
            - $ref: '#/components/schemas/SystemToolConfig-Output'
            - type: 'null'
        voicemail_detection:
          oneOf:
            - $ref: '#/components/schemas/SystemToolConfig-Output'
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
    PromptAgentApiModelOutputBackupLlmConfig:
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
    WebhookToolApiSchemaConfigOutputMethod:
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
    ArrayJsonSchemaPropertyOutputItems:
      oneOf:
        - $ref: '#/components/schemas/LiteralJsonSchemaProperty'
        - $ref: '#/components/schemas/ObjectJsonSchemaProperty-Output'
        - $ref: '#/components/schemas/ArrayJsonSchemaProperty-Output'
    ArrayJsonSchemaProperty-Output:
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
          $ref: '#/components/schemas/ArrayJsonSchemaPropertyOutputItems'
      required:
        - items
    ObjectJsonSchemaPropertyOutput:
      oneOf:
        - $ref: '#/components/schemas/LiteralJsonSchemaProperty'
        - $ref: '#/components/schemas/ObjectJsonSchemaProperty-Output'
        - $ref: '#/components/schemas/ArrayJsonSchemaProperty-Output'
    ObjectJsonSchemaProperty-Output:
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
            $ref: '#/components/schemas/ObjectJsonSchemaPropertyOutput'
    WebhookToolApiSchemaConfigOutputRequestHeaders:
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
    WebhookToolApiSchemaConfig-Output:
      type: object
      properties:
        url:
          type: string
        method:
          $ref: '#/components/schemas/WebhookToolApiSchemaConfigOutputMethod'
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
            - $ref: '#/components/schemas/ObjectJsonSchemaProperty-Output'
            - type: 'null'
        request_headers:
          type: object
          additionalProperties:
            $ref: >-
              #/components/schemas/WebhookToolApiSchemaConfigOutputRequestHeaders
        auth_connection:
          oneOf:
            - $ref: '#/components/schemas/AuthConnectionLocator'
            - type: 'null'
      required:
        - url
    WebhookToolConfig-Output:
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
          $ref: '#/components/schemas/WebhookToolApiSchemaConfig-Output'
      required:
        - name
        - description
        - api_schema
    ClientToolConfig-Output:
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
            - $ref: '#/components/schemas/ObjectJsonSchemaProperty-Output'
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
    ObjectOverrideOutput:
      oneOf:
        - $ref: '#/components/schemas/LiteralOverride'
        - $ref: '#/components/schemas/ObjectOverride-Output'
    ObjectOverride-Output:
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
            $ref: '#/components/schemas/ObjectOverrideOutput'
        required:
          type:
            - array
            - 'null'
          items:
            type: string
    ApiIntegrationWebhookOverridesOutputRequestHeaders:
      oneOf:
        - type: string
        - $ref: '#/components/schemas/ConvAIDynamicVariable'
    ApiIntegrationWebhookOverrides-Output:
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
            - $ref: '#/components/schemas/ObjectOverride-Output'
            - type: 'null'
        request_headers:
          type:
            - object
            - 'null'
          additionalProperties:
            $ref: >-
              #/components/schemas/ApiIntegrationWebhookOverridesOutputRequestHeaders
    ApiIntegrationWebhookToolConfig-Output:
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
            - $ref: '#/components/schemas/ApiIntegrationWebhookOverrides-Output'
            - type: 'null'
      required:
        - type
        - name
        - description
        - response_timeout_secs
        - disable_interruptions
        - force_pre_tool_speech
        - assignments
        - tool_call_sound
        - tool_call_sound_behavior
        - dynamic_variables
        - execution_mode
        - tool_version
        - api_integration_id
        - api_integration_connection_id
        - api_schema_overrides
    PromptAgentApiModelOutputToolsItems:
      oneOf:
        - $ref: '#/components/schemas/WebhookToolConfig-Output'
        - $ref: '#/components/schemas/ClientToolConfig-Output'
        - $ref: '#/components/schemas/SystemToolConfig-Output'
        - $ref: '#/components/schemas/ApiIntegrationWebhookToolConfig-Output'
    PromptAgentAPIModel-Output:
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
          $ref: '#/components/schemas/BuiltInTools-Output'
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
          $ref: '#/components/schemas/PromptAgentApiModelOutputBackupLlmConfig'
        tools:
          type: array
          items:
            $ref: '#/components/schemas/PromptAgentApiModelOutputToolsItems'
    AgentConfigAPIModel-Output:
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
          $ref: '#/components/schemas/PromptAgentAPIModel-Output'
    ConversationalConfigAPIModel-Output:
      type: object
      properties:
        asr:
          $ref: '#/components/schemas/ASRConversationalConfig'
        turn:
          $ref: '#/components/schemas/TurnConfig'
        tts:
          $ref: '#/components/schemas/TTSConversationalConfig-Output'
        conversation:
          $ref: '#/components/schemas/ConversationConfig'
        language_presets:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/LanguagePreset-Output'
        vad:
          $ref: '#/components/schemas/VADConfig'
        agent:
          $ref: '#/components/schemas/AgentConfigAPIModel-Output'
    AgentMetadataResponseModel:
      type: object
      properties:
        created_at_unix_secs:
          type: integer
        updated_at_unix_secs:
          type: integer
      required:
        - created_at_unix_secs
        - updated_at_unix_secs
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
    WidgetConfigOutputAvatar:
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
    WidgetConfig-Output:
      type: object
      properties:
        variant:
          $ref: '#/components/schemas/EmbedVariant'
        placement:
          $ref: '#/components/schemas/WidgetPlacement'
        expandable:
          $ref: '#/components/schemas/WidgetExpandable'
        avatar:
          $ref: '#/components/schemas/WidgetConfigOutputAvatar'
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
    ConversationConfigClientOverrideConfig-Output:
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
    ConversationInitiationClientDataConfig-Output:
      type: object
      properties:
        conversation_config_override:
          $ref: '#/components/schemas/ConversationConfigClientOverrideConfig-Output'
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
    AgentWorkspaceOverrides-Output:
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
    SafetyResponseModel:
      type: object
      properties:
        is_blocked_ivc:
          type: boolean
        is_blocked_non_ivc:
          type: boolean
        ignore_safety_evaluation:
          type: boolean
    AgentPlatformSettingsResponseModel:
      type: object
      properties:
        evaluation:
          $ref: '#/components/schemas/EvaluationSettings'
        widget:
          $ref: '#/components/schemas/WidgetConfig-Output'
        data_collection:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/LiteralJsonSchemaProperty'
        overrides:
          $ref: '#/components/schemas/ConversationInitiationClientDataConfig-Output'
        workspace_overrides:
          $ref: '#/components/schemas/AgentWorkspaceOverrides-Output'
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
        safety:
          $ref: '#/components/schemas/SafetyResponseModel'
    PhoneNumberAgentInfo:
      type: object
      properties:
        agent_id:
          type: string
        agent_name:
          type: string
      required:
        - agent_id
        - agent_name
    GetPhoneNumberTwilioResponseModel:
      type: object
      properties:
        phone_number:
          type: string
        label:
          type: string
        supports_inbound:
          type: boolean
        supports_outbound:
          type: boolean
        phone_number_id:
          type: string
        assigned_agent:
          oneOf:
            - $ref: '#/components/schemas/PhoneNumberAgentInfo'
            - type: 'null'
        provider:
          type: string
          enum:
            - type: stringLiteral
              value: twilio
      required:
        - phone_number
        - label
        - phone_number_id
    SIPTrunkTransportEnum:
      type: string
      enum:
        - value: auto
        - value: udp
        - value: tcp
        - value: tls
    SIPMediaEncryptionEnum:
      type: string
      enum:
        - value: disabled
        - value: allowed
        - value: required
    GetPhoneNumberOutboundSIPTrunkConfigResponseModel:
      type: object
      properties:
        address:
          type: string
        transport:
          $ref: '#/components/schemas/SIPTrunkTransportEnum'
        media_encryption:
          $ref: '#/components/schemas/SIPMediaEncryptionEnum'
        headers:
          type: object
          additionalProperties:
            type: string
        has_auth_credentials:
          type: boolean
        username:
          type:
            - string
            - 'null'
        has_outbound_trunk:
          type: boolean
      required:
        - address
        - transport
        - media_encryption
        - has_auth_credentials
    GetPhoneNumberInboundSIPTrunkConfigResponseModel:
      type: object
      properties:
        allowed_addresses:
          type: array
          items:
            type: string
        allowed_numbers:
          type:
            - array
            - 'null'
          items:
            type: string
        media_encryption:
          $ref: '#/components/schemas/SIPMediaEncryptionEnum'
        has_auth_credentials:
          type: boolean
        username:
          type:
            - string
            - 'null'
        remote_domains:
          type:
            - array
            - 'null'
          items:
            type: string
      required:
        - allowed_addresses
        - allowed_numbers
        - media_encryption
        - has_auth_credentials
    LivekitStackType:
      type: string
      enum:
        - value: standard
        - value: static
    GetPhoneNumberSIPTrunkResponseModel:
      type: object
      properties:
        phone_number:
          type: string
        label:
          type: string
        supports_inbound:
          type: boolean
        supports_outbound:
          type: boolean
        phone_number_id:
          type: string
        assigned_agent:
          oneOf:
            - $ref: '#/components/schemas/PhoneNumberAgentInfo'
            - type: 'null'
        provider:
          type: string
          enum:
            - type: stringLiteral
              value: sip_trunk
        provider_config:
          oneOf:
            - $ref: >-
                #/components/schemas/GetPhoneNumberOutboundSIPTrunkConfigResponseModel
            - type: 'null'
        outbound_trunk:
          oneOf:
            - $ref: >-
                #/components/schemas/GetPhoneNumberOutboundSIPTrunkConfigResponseModel
            - type: 'null'
        inbound_trunk:
          oneOf:
            - $ref: >-
                #/components/schemas/GetPhoneNumberInboundSIPTrunkConfigResponseModel
            - type: 'null'
        livekit_stack:
          $ref: '#/components/schemas/LivekitStackType'
      required:
        - phone_number
        - label
        - phone_number_id
        - livekit_stack
    GetAgentResponseModelPhoneNumbersItems:
      oneOf:
        - $ref: '#/components/schemas/GetPhoneNumberTwilioResponseModel'
        - $ref: '#/components/schemas/GetPhoneNumberSIPTrunkResponseModel'
    WorkflowUnconditionalModel-Output:
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
      required:
        - label
        - type
    WorkflowLLMConditionModel-Output:
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
        - label
        - type
        - condition
    WorkflowResultConditionModel-Output:
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
        - label
        - type
        - successful
    ASTStringNode-Output:
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
        - type
        - value
    ASTNumberNode-Output:
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
        - type
        - value
    ASTBooleanNode-Output:
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
        - type
        - value
    ASTLLMNode-Output:
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
        - type
        - prompt
    ASTDynamicVariableNode-Output:
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
        - type
        - name
    AstLessThanOrEqualsOperatorNodeOutputLeft:
      oneOf:
        - $ref: '#/components/schemas/ASTStringNode-Output'
        - $ref: '#/components/schemas/ASTNumberNode-Output'
        - $ref: '#/components/schemas/ASTBooleanNode-Output'
        - $ref: '#/components/schemas/ASTLLMNode-Output'
        - $ref: '#/components/schemas/ASTDynamicVariableNode-Output'
        - $ref: '#/components/schemas/ASTOrOperatorNode-Output'
        - $ref: '#/components/schemas/ASTAndOperatorNode-Output'
        - $ref: '#/components/schemas/ASTEqualsOperatorNode-Output'
        - $ref: '#/components/schemas/ASTNotEqualsOperatorNode-Output'
        - $ref: '#/components/schemas/ASTGreaterThanOperatorNode-Output'
        - $ref: '#/components/schemas/ASTLessThanOperatorNode-Output'
        - $ref: '#/components/schemas/ASTGreaterThanOrEqualsOperatorNode-Output'
        - $ref: '#/components/schemas/ASTLessThanOrEqualsOperatorNode-Output'
    AstLessThanOrEqualsOperatorNodeOutputRight:
      oneOf:
        - $ref: '#/components/schemas/ASTStringNode-Output'
        - $ref: '#/components/schemas/ASTNumberNode-Output'
        - $ref: '#/components/schemas/ASTBooleanNode-Output'
        - $ref: '#/components/schemas/ASTLLMNode-Output'
        - $ref: '#/components/schemas/ASTDynamicVariableNode-Output'
        - $ref: '#/components/schemas/ASTOrOperatorNode-Output'
        - $ref: '#/components/schemas/ASTAndOperatorNode-Output'
        - $ref: '#/components/schemas/ASTEqualsOperatorNode-Output'
        - $ref: '#/components/schemas/ASTNotEqualsOperatorNode-Output'
        - $ref: '#/components/schemas/ASTGreaterThanOperatorNode-Output'
        - $ref: '#/components/schemas/ASTLessThanOperatorNode-Output'
        - $ref: '#/components/schemas/ASTGreaterThanOrEqualsOperatorNode-Output'
        - $ref: '#/components/schemas/ASTLessThanOrEqualsOperatorNode-Output'
    ASTLessThanOrEqualsOperatorNode-Output:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: lte_operator
        left:
          $ref: '#/components/schemas/AstLessThanOrEqualsOperatorNodeOutputLeft'
        right:
          $ref: '#/components/schemas/AstLessThanOrEqualsOperatorNodeOutputRight'
      required:
        - type
        - left
        - right
    AstGreaterThanOrEqualsOperatorNodeOutputLeft:
      oneOf:
        - $ref: '#/components/schemas/ASTStringNode-Output'
        - $ref: '#/components/schemas/ASTNumberNode-Output'
        - $ref: '#/components/schemas/ASTBooleanNode-Output'
        - $ref: '#/components/schemas/ASTLLMNode-Output'
        - $ref: '#/components/schemas/ASTDynamicVariableNode-Output'
        - $ref: '#/components/schemas/ASTOrOperatorNode-Output'
        - $ref: '#/components/schemas/ASTAndOperatorNode-Output'
        - $ref: '#/components/schemas/ASTEqualsOperatorNode-Output'
        - $ref: '#/components/schemas/ASTNotEqualsOperatorNode-Output'
        - $ref: '#/components/schemas/ASTGreaterThanOperatorNode-Output'
        - $ref: '#/components/schemas/ASTLessThanOperatorNode-Output'
        - $ref: '#/components/schemas/ASTGreaterThanOrEqualsOperatorNode-Output'
        - $ref: '#/components/schemas/ASTLessThanOrEqualsOperatorNode-Output'
    AstGreaterThanOrEqualsOperatorNodeOutputRight:
      oneOf:
        - $ref: '#/components/schemas/ASTStringNode-Output'
        - $ref: '#/components/schemas/ASTNumberNode-Output'
        - $ref: '#/components/schemas/ASTBooleanNode-Output'
        - $ref: '#/components/schemas/ASTLLMNode-Output'
        - $ref: '#/components/schemas/ASTDynamicVariableNode-Output'
        - $ref: '#/components/schemas/ASTOrOperatorNode-Output'
        - $ref: '#/components/schemas/ASTAndOperatorNode-Output'
        - $ref: '#/components/schemas/ASTEqualsOperatorNode-Output'
        - $ref: '#/components/schemas/ASTNotEqualsOperatorNode-Output'
        - $ref: '#/components/schemas/ASTGreaterThanOperatorNode-Output'
        - $ref: '#/components/schemas/ASTLessThanOperatorNode-Output'
        - $ref: '#/components/schemas/ASTGreaterThanOrEqualsOperatorNode-Output'
        - $ref: '#/components/schemas/ASTLessThanOrEqualsOperatorNode-Output'
    ASTGreaterThanOrEqualsOperatorNode-Output:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: gte_operator
        left:
          $ref: '#/components/schemas/AstGreaterThanOrEqualsOperatorNodeOutputLeft'
        right:
          $ref: '#/components/schemas/AstGreaterThanOrEqualsOperatorNodeOutputRight'
      required:
        - type
        - left
        - right
    AstLessThanOperatorNodeOutputLeft:
      oneOf:
        - $ref: '#/components/schemas/ASTStringNode-Output'
        - $ref: '#/components/schemas/ASTNumberNode-Output'
        - $ref: '#/components/schemas/ASTBooleanNode-Output'
        - $ref: '#/components/schemas/ASTLLMNode-Output'
        - $ref: '#/components/schemas/ASTDynamicVariableNode-Output'
        - $ref: '#/components/schemas/ASTOrOperatorNode-Output'
        - $ref: '#/components/schemas/ASTAndOperatorNode-Output'
        - $ref: '#/components/schemas/ASTEqualsOperatorNode-Output'
        - $ref: '#/components/schemas/ASTNotEqualsOperatorNode-Output'
        - $ref: '#/components/schemas/ASTGreaterThanOperatorNode-Output'
        - $ref: '#/components/schemas/ASTLessThanOperatorNode-Output'
        - $ref: '#/components/schemas/ASTGreaterThanOrEqualsOperatorNode-Output'
        - $ref: '#/components/schemas/ASTLessThanOrEqualsOperatorNode-Output'
    AstLessThanOperatorNodeOutputRight:
      oneOf:
        - $ref: '#/components/schemas/ASTStringNode-Output'
        - $ref: '#/components/schemas/ASTNumberNode-Output'
        - $ref: '#/components/schemas/ASTBooleanNode-Output'
        - $ref: '#/components/schemas/ASTLLMNode-Output'
        - $ref: '#/components/schemas/ASTDynamicVariableNode-Output'
        - $ref: '#/components/schemas/ASTOrOperatorNode-Output'
        - $ref: '#/components/schemas/ASTAndOperatorNode-Output'
        - $ref: '#/components/schemas/ASTEqualsOperatorNode-Output'
        - $ref: '#/components/schemas/ASTNotEqualsOperatorNode-Output'
        - $ref: '#/components/schemas/ASTGreaterThanOperatorNode-Output'
        - $ref: '#/components/schemas/ASTLessThanOperatorNode-Output'
        - $ref: '#/components/schemas/ASTGreaterThanOrEqualsOperatorNode-Output'
        - $ref: '#/components/schemas/ASTLessThanOrEqualsOperatorNode-Output'
    ASTLessThanOperatorNode-Output:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: lt_operator
        left:
          $ref: '#/components/schemas/AstLessThanOperatorNodeOutputLeft'
        right:
          $ref: '#/components/schemas/AstLessThanOperatorNodeOutputRight'
      required:
        - type
        - left
        - right
    AstGreaterThanOperatorNodeOutputLeft:
      oneOf:
        - $ref: '#/components/schemas/ASTStringNode-Output'
        - $ref: '#/components/schemas/ASTNumberNode-Output'
        - $ref: '#/components/schemas/ASTBooleanNode-Output'
        - $ref: '#/components/schemas/ASTLLMNode-Output'
        - $ref: '#/components/schemas/ASTDynamicVariableNode-Output'
        - $ref: '#/components/schemas/ASTOrOperatorNode-Output'
        - $ref: '#/components/schemas/ASTAndOperatorNode-Output'
        - $ref: '#/components/schemas/ASTEqualsOperatorNode-Output'
        - $ref: '#/components/schemas/ASTNotEqualsOperatorNode-Output'
        - $ref: '#/components/schemas/ASTGreaterThanOperatorNode-Output'
        - $ref: '#/components/schemas/ASTLessThanOperatorNode-Output'
        - $ref: '#/components/schemas/ASTGreaterThanOrEqualsOperatorNode-Output'
        - $ref: '#/components/schemas/ASTLessThanOrEqualsOperatorNode-Output'
    AstGreaterThanOperatorNodeOutputRight:
      oneOf:
        - $ref: '#/components/schemas/ASTStringNode-Output'
        - $ref: '#/components/schemas/ASTNumberNode-Output'
        - $ref: '#/components/schemas/ASTBooleanNode-Output'
        - $ref: '#/components/schemas/ASTLLMNode-Output'
        - $ref: '#/components/schemas/ASTDynamicVariableNode-Output'
        - $ref: '#/components/schemas/ASTOrOperatorNode-Output'
        - $ref: '#/components/schemas/ASTAndOperatorNode-Output'
        - $ref: '#/components/schemas/ASTEqualsOperatorNode-Output'
        - $ref: '#/components/schemas/ASTNotEqualsOperatorNode-Output'
        - $ref: '#/components/schemas/ASTGreaterThanOperatorNode-Output'
        - $ref: '#/components/schemas/ASTLessThanOperatorNode-Output'
        - $ref: '#/components/schemas/ASTGreaterThanOrEqualsOperatorNode-Output'
        - $ref: '#/components/schemas/ASTLessThanOrEqualsOperatorNode-Output'
    ASTGreaterThanOperatorNode-Output:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: gt_operator
        left:
          $ref: '#/components/schemas/AstGreaterThanOperatorNodeOutputLeft'
        right:
          $ref: '#/components/schemas/AstGreaterThanOperatorNodeOutputRight'
      required:
        - type
        - left
        - right
    AstNotEqualsOperatorNodeOutputLeft:
      oneOf:
        - $ref: '#/components/schemas/ASTStringNode-Output'
        - $ref: '#/components/schemas/ASTNumberNode-Output'
        - $ref: '#/components/schemas/ASTBooleanNode-Output'
        - $ref: '#/components/schemas/ASTLLMNode-Output'
        - $ref: '#/components/schemas/ASTDynamicVariableNode-Output'
        - $ref: '#/components/schemas/ASTOrOperatorNode-Output'
        - $ref: '#/components/schemas/ASTAndOperatorNode-Output'
        - $ref: '#/components/schemas/ASTEqualsOperatorNode-Output'
        - $ref: '#/components/schemas/ASTNotEqualsOperatorNode-Output'
        - $ref: '#/components/schemas/ASTGreaterThanOperatorNode-Output'
        - $ref: '#/components/schemas/ASTLessThanOperatorNode-Output'
        - $ref: '#/components/schemas/ASTGreaterThanOrEqualsOperatorNode-Output'
        - $ref: '#/components/schemas/ASTLessThanOrEqualsOperatorNode-Output'
    AstNotEqualsOperatorNodeOutputRight:
      oneOf:
        - $ref: '#/components/schemas/ASTStringNode-Output'
        - $ref: '#/components/schemas/ASTNumberNode-Output'
        - $ref: '#/components/schemas/ASTBooleanNode-Output'
        - $ref: '#/components/schemas/ASTLLMNode-Output'
        - $ref: '#/components/schemas/ASTDynamicVariableNode-Output'
        - $ref: '#/components/schemas/ASTOrOperatorNode-Output'
        - $ref: '#/components/schemas/ASTAndOperatorNode-Output'
        - $ref: '#/components/schemas/ASTEqualsOperatorNode-Output'
        - $ref: '#/components/schemas/ASTNotEqualsOperatorNode-Output'
        - $ref: '#/components/schemas/ASTGreaterThanOperatorNode-Output'
        - $ref: '#/components/schemas/ASTLessThanOperatorNode-Output'
        - $ref: '#/components/schemas/ASTGreaterThanOrEqualsOperatorNode-Output'
        - $ref: '#/components/schemas/ASTLessThanOrEqualsOperatorNode-Output'
    ASTNotEqualsOperatorNode-Output:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: neq_operator
        left:
          $ref: '#/components/schemas/AstNotEqualsOperatorNodeOutputLeft'
        right:
          $ref: '#/components/schemas/AstNotEqualsOperatorNodeOutputRight'
      required:
        - type
        - left
        - right
    AstEqualsOperatorNodeOutputLeft:
      oneOf:
        - $ref: '#/components/schemas/ASTStringNode-Output'
        - $ref: '#/components/schemas/ASTNumberNode-Output'
        - $ref: '#/components/schemas/ASTBooleanNode-Output'
        - $ref: '#/components/schemas/ASTLLMNode-Output'
        - $ref: '#/components/schemas/ASTDynamicVariableNode-Output'
        - $ref: '#/components/schemas/ASTOrOperatorNode-Output'
        - $ref: '#/components/schemas/ASTAndOperatorNode-Output'
        - $ref: '#/components/schemas/ASTEqualsOperatorNode-Output'
        - $ref: '#/components/schemas/ASTNotEqualsOperatorNode-Output'
        - $ref: '#/components/schemas/ASTGreaterThanOperatorNode-Output'
        - $ref: '#/components/schemas/ASTLessThanOperatorNode-Output'
        - $ref: '#/components/schemas/ASTGreaterThanOrEqualsOperatorNode-Output'
        - $ref: '#/components/schemas/ASTLessThanOrEqualsOperatorNode-Output'
    AstEqualsOperatorNodeOutputRight:
      oneOf:
        - $ref: '#/components/schemas/ASTStringNode-Output'
        - $ref: '#/components/schemas/ASTNumberNode-Output'
        - $ref: '#/components/schemas/ASTBooleanNode-Output'
        - $ref: '#/components/schemas/ASTLLMNode-Output'
        - $ref: '#/components/schemas/ASTDynamicVariableNode-Output'
        - $ref: '#/components/schemas/ASTOrOperatorNode-Output'
        - $ref: '#/components/schemas/ASTAndOperatorNode-Output'
        - $ref: '#/components/schemas/ASTEqualsOperatorNode-Output'
        - $ref: '#/components/schemas/ASTNotEqualsOperatorNode-Output'
        - $ref: '#/components/schemas/ASTGreaterThanOperatorNode-Output'
        - $ref: '#/components/schemas/ASTLessThanOperatorNode-Output'
        - $ref: '#/components/schemas/ASTGreaterThanOrEqualsOperatorNode-Output'
        - $ref: '#/components/schemas/ASTLessThanOrEqualsOperatorNode-Output'
    ASTEqualsOperatorNode-Output:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: eq_operator
        left:
          $ref: '#/components/schemas/AstEqualsOperatorNodeOutputLeft'
        right:
          $ref: '#/components/schemas/AstEqualsOperatorNodeOutputRight'
      required:
        - type
        - left
        - right
    AstAndOperatorNodeOutputChildrenItems:
      oneOf:
        - $ref: '#/components/schemas/ASTStringNode-Output'
        - $ref: '#/components/schemas/ASTNumberNode-Output'
        - $ref: '#/components/schemas/ASTBooleanNode-Output'
        - $ref: '#/components/schemas/ASTLLMNode-Output'
        - $ref: '#/components/schemas/ASTDynamicVariableNode-Output'
        - $ref: '#/components/schemas/ASTOrOperatorNode-Output'
        - $ref: '#/components/schemas/ASTAndOperatorNode-Output'
        - $ref: '#/components/schemas/ASTEqualsOperatorNode-Output'
        - $ref: '#/components/schemas/ASTNotEqualsOperatorNode-Output'
        - $ref: '#/components/schemas/ASTGreaterThanOperatorNode-Output'
        - $ref: '#/components/schemas/ASTLessThanOperatorNode-Output'
        - $ref: '#/components/schemas/ASTGreaterThanOrEqualsOperatorNode-Output'
        - $ref: '#/components/schemas/ASTLessThanOrEqualsOperatorNode-Output'
    ASTAndOperatorNode-Output:
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
            $ref: '#/components/schemas/AstAndOperatorNodeOutputChildrenItems'
      required:
        - type
        - children
    AstOrOperatorNodeOutputChildrenItems:
      oneOf:
        - $ref: '#/components/schemas/ASTStringNode-Output'
        - $ref: '#/components/schemas/ASTNumberNode-Output'
        - $ref: '#/components/schemas/ASTBooleanNode-Output'
        - $ref: '#/components/schemas/ASTLLMNode-Output'
        - $ref: '#/components/schemas/ASTDynamicVariableNode-Output'
        - $ref: '#/components/schemas/ASTOrOperatorNode-Output'
        - $ref: '#/components/schemas/ASTAndOperatorNode-Output'
        - $ref: '#/components/schemas/ASTEqualsOperatorNode-Output'
        - $ref: '#/components/schemas/ASTNotEqualsOperatorNode-Output'
        - $ref: '#/components/schemas/ASTGreaterThanOperatorNode-Output'
        - $ref: '#/components/schemas/ASTLessThanOperatorNode-Output'
        - $ref: '#/components/schemas/ASTGreaterThanOrEqualsOperatorNode-Output'
        - $ref: '#/components/schemas/ASTLessThanOrEqualsOperatorNode-Output'
    ASTOrOperatorNode-Output:
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
            $ref: '#/components/schemas/AstOrOperatorNodeOutputChildrenItems'
      required:
        - type
        - children
    WorkflowExpressionConditionModelOutputExpression:
      oneOf:
        - $ref: '#/components/schemas/ASTStringNode-Output'
        - $ref: '#/components/schemas/ASTNumberNode-Output'
        - $ref: '#/components/schemas/ASTBooleanNode-Output'
        - $ref: '#/components/schemas/ASTLLMNode-Output'
        - $ref: '#/components/schemas/ASTDynamicVariableNode-Output'
        - $ref: '#/components/schemas/ASTOrOperatorNode-Output'
        - $ref: '#/components/schemas/ASTAndOperatorNode-Output'
        - $ref: '#/components/schemas/ASTEqualsOperatorNode-Output'
        - $ref: '#/components/schemas/ASTNotEqualsOperatorNode-Output'
        - $ref: '#/components/schemas/ASTGreaterThanOperatorNode-Output'
        - $ref: '#/components/schemas/ASTLessThanOperatorNode-Output'
        - $ref: '#/components/schemas/ASTGreaterThanOrEqualsOperatorNode-Output'
        - $ref: '#/components/schemas/ASTLessThanOrEqualsOperatorNode-Output'
    WorkflowExpressionConditionModel-Output:
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
          $ref: >-
            #/components/schemas/WorkflowExpressionConditionModelOutputExpression
      required:
        - label
        - type
        - expression
    WorkflowEdgeModelOutputForwardCondition:
      oneOf:
        - $ref: '#/components/schemas/WorkflowUnconditionalModel-Output'
        - $ref: '#/components/schemas/WorkflowLLMConditionModel-Output'
        - $ref: '#/components/schemas/WorkflowResultConditionModel-Output'
        - $ref: '#/components/schemas/WorkflowExpressionConditionModel-Output'
    WorkflowEdgeModelOutputBackwardCondition:
      oneOf:
        - $ref: '#/components/schemas/WorkflowUnconditionalModel-Output'
        - $ref: '#/components/schemas/WorkflowLLMConditionModel-Output'
        - $ref: '#/components/schemas/WorkflowResultConditionModel-Output'
        - $ref: '#/components/schemas/WorkflowExpressionConditionModel-Output'
    WorkflowEdgeModel-Output:
      type: object
      properties:
        source:
          type: string
        target:
          type: string
        forward_condition:
          oneOf:
            - $ref: '#/components/schemas/WorkflowEdgeModelOutputForwardCondition'
            - type: 'null'
        backward_condition:
          oneOf:
            - $ref: '#/components/schemas/WorkflowEdgeModelOutputBackwardCondition'
            - type: 'null'
      required:
        - source
        - target
        - forward_condition
        - backward_condition
    Position-Output:
      type: object
      properties:
        x:
          type: number
          format: double
        'y':
          type: number
          format: double
      required:
        - x
        - 'y'
    WorkflowStartNodeModel-Output:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: start
        position:
          $ref: '#/components/schemas/Position-Output'
        edge_order:
          type: array
          items:
            type: string
      required:
        - type
        - position
        - edge_order
    WorkflowEndNodeModel-Output:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: end
        position:
          $ref: '#/components/schemas/Position-Output'
        edge_order:
          type: array
          items:
            type: string
      required:
        - type
        - position
        - edge_order
    WorkflowPhoneNumberNodeModelOutputTransferDestination:
      oneOf:
        - $ref: '#/components/schemas/PhoneNumberTransferDestination'
        - $ref: '#/components/schemas/SIPUriTransferDestination'
        - $ref: '#/components/schemas/PhoneNumberDynamicVariableTransferDestination'
        - $ref: '#/components/schemas/SIPUriDynamicVariableTransferDestination'
    WorkflowPhoneNumberNodeModel-Output:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: phone_number
        position:
          $ref: '#/components/schemas/Position-Output'
        edge_order:
          type: array
          items:
            type: string
        transfer_destination:
          $ref: >-
            #/components/schemas/WorkflowPhoneNumberNodeModelOutputTransferDestination
        transfer_type:
          $ref: '#/components/schemas/TransferTypeEnum'
      required:
        - type
        - position
        - edge_order
        - transfer_destination
        - transfer_type
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
    TTSConversationalConfigWorkflowOverride-Output:
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
    BuiltInToolsWorkflowOverride-Output:
      type: object
      properties:
        end_call:
          oneOf:
            - $ref: '#/components/schemas/SystemToolConfig-Output'
            - type: 'null'
        language_detection:
          oneOf:
            - $ref: '#/components/schemas/SystemToolConfig-Output'
            - type: 'null'
        transfer_to_agent:
          oneOf:
            - $ref: '#/components/schemas/SystemToolConfig-Output'
            - type: 'null'
        transfer_to_number:
          oneOf:
            - $ref: '#/components/schemas/SystemToolConfig-Output'
            - type: 'null'
        skip_turn:
          oneOf:
            - $ref: '#/components/schemas/SystemToolConfig-Output'
            - type: 'null'
        play_keypad_touch_tone:
          oneOf:
            - $ref: '#/components/schemas/SystemToolConfig-Output'
            - type: 'null'
        voicemail_detection:
          oneOf:
            - $ref: '#/components/schemas/SystemToolConfig-Output'
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
    PromptAgentApiModelWorkflowOverrideOutputBackupLlmConfig:
      oneOf:
        - $ref: '#/components/schemas/BackupLLMDefault'
        - $ref: '#/components/schemas/BackupLLMDisabled'
        - $ref: '#/components/schemas/BackupLLMOverride'
    PromptAgentApiModelWorkflowOverrideOutputToolsItems:
      oneOf:
        - $ref: '#/components/schemas/WebhookToolConfig-Output'
        - $ref: '#/components/schemas/ClientToolConfig-Output'
        - $ref: '#/components/schemas/SystemToolConfig-Output'
        - $ref: '#/components/schemas/ApiIntegrationWebhookToolConfig-Output'
    PromptAgentAPIModelWorkflowOverride-Output:
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
            - $ref: '#/components/schemas/BuiltInToolsWorkflowOverride-Output'
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
                #/components/schemas/PromptAgentApiModelWorkflowOverrideOutputBackupLlmConfig
            - type: 'null'
        tools:
          type:
            - array
            - 'null'
          items:
            $ref: >-
              #/components/schemas/PromptAgentApiModelWorkflowOverrideOutputToolsItems
    AgentConfigAPIModelWorkflowOverride-Output:
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
            - $ref: '#/components/schemas/PromptAgentAPIModelWorkflowOverride-Output'
            - type: 'null'
    ConversationalConfigAPIModelWorkflowOverride-Output:
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
                #/components/schemas/TTSConversationalConfigWorkflowOverride-Output
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
            $ref: '#/components/schemas/LanguagePreset-Output'
        vad:
          oneOf:
            - $ref: '#/components/schemas/VADConfigWorkflowOverride'
            - type: 'null'
        agent:
          oneOf:
            - $ref: '#/components/schemas/AgentConfigAPIModelWorkflowOverride-Output'
            - type: 'null'
    WorkflowOverrideAgentNodeModel-Output:
      type: object
      properties:
        conversation_config:
          $ref: >-
            #/components/schemas/ConversationalConfigAPIModelWorkflowOverride-Output
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
          $ref: '#/components/schemas/Position-Output'
        edge_order:
          type: array
          items:
            type: string
        label:
          type: string
      required:
        - conversation_config
        - additional_prompt
        - additional_knowledge_base
        - additional_tool_ids
        - type
        - position
        - edge_order
        - label
    WorkflowStandaloneAgentNodeModel-Output:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: standalone_agent
        position:
          $ref: '#/components/schemas/Position-Output'
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
        - type
        - position
        - edge_order
        - agent_id
        - delay_ms
        - transfer_message
        - enable_transferred_agent_first_message
    WorkflowToolLocator:
      type: object
      properties:
        tool_id:
          type: string
      required:
        - tool_id
    WorkflowToolNodeModel-Output:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: tool
        position:
          $ref: '#/components/schemas/Position-Output'
        edge_order:
          type: array
          items:
            type: string
        tools:
          type: array
          items:
            $ref: '#/components/schemas/WorkflowToolLocator'
      required:
        - type
        - position
        - edge_order
        - tools
    AgentWorkflowResponseModelNodes:
      oneOf:
        - $ref: '#/components/schemas/WorkflowStartNodeModel-Output'
        - $ref: '#/components/schemas/WorkflowEndNodeModel-Output'
        - $ref: '#/components/schemas/WorkflowPhoneNumberNodeModel-Output'
        - $ref: '#/components/schemas/WorkflowOverrideAgentNodeModel-Output'
        - $ref: '#/components/schemas/WorkflowStandaloneAgentNodeModel-Output'
        - $ref: '#/components/schemas/WorkflowToolNodeModel-Output'
    AgentWorkflowResponseModel:
      type: object
      properties:
        edges:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/WorkflowEdgeModel-Output'
        nodes:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/AgentWorkflowResponseModelNodes'
      required:
        - edges
        - nodes
    ResourceAccessInfoRole:
      type: string
      enum:
        - value: admin
        - value: editor
        - value: commenter
        - value: viewer
    ResourceAccessInfo:
      type: object
      properties:
        is_creator:
          type: boolean
        creator_name:
          type: string
        creator_email:
          type: string
        role:
          $ref: '#/components/schemas/ResourceAccessInfoRole'
      required:
        - is_creator
        - creator_name
        - creator_email
        - role
    GetAgentResponseModel:
      type: object
      properties:
        agent_id:
          type: string
        name:
          type: string
        conversation_config:
          $ref: '#/components/schemas/ConversationalConfigAPIModel-Output'
        metadata:
          $ref: '#/components/schemas/AgentMetadataResponseModel'
        platform_settings:
          $ref: '#/components/schemas/AgentPlatformSettingsResponseModel'
        phone_numbers:
          type: array
          items:
            $ref: '#/components/schemas/GetAgentResponseModelPhoneNumbersItems'
        workflow:
          $ref: '#/components/schemas/AgentWorkflowResponseModel'
        access_info:
          oneOf:
            - $ref: '#/components/schemas/ResourceAccessInfo'
            - type: 'null'
        tags:
          type: array
          items:
            type: string
      required:
        - agent_id
        - name
        - conversation_config
        - metadata

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.conversationalAi.agents.get("agent_id");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.conversational_ai.agents.get(
    agent_id="agent_id"
)

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/agents/agent_id"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("xi-api-key", "xi-api-key")

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

url = URI("https://api.elevenlabs.io/v1/convai/agents/agent_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["xi-api-key"] = 'xi-api-key'

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/agents/agent_id")
  .header("xi-api-key", "xi-api-key")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/agents/agent_id', [
  'headers' => [
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/convai/agents/agent_id");
var request = new RestRequest(Method.GET);
request.AddHeader("xi-api-key", "xi-api-key");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["xi-api-key": "xi-api-key"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/agents/agent_id")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
request.allHTTPHeaderFields = headers

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
**Navigation:** [← Previous](./18-websocket.md) | [Index](./index.md) | [Next →](./20-list-agents.md)
