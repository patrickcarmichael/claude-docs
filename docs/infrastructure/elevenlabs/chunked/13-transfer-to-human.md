**Navigation:** [← Previous](./12-language.md) | [Index](./index.md) | [Next →](./14-batch-calling.md)

# Transfer to human

> Seamlessly transfer the user to a human operator via phone number based on defined conditions.


## Overview

Human transfer allows a ElevenLabs agent to transfer the ongoing call to a specified phone number or SIP URI when certain conditions are met. This enables agents to hand off complex issues, specific requests, or situations requiring human intervention to a live operator.

This feature utilizes the `transfer_to_number` system tool which supports transfers via Twilio and SIP trunk numbers. When triggered, the agent can provide a message to the user while they wait and a separate message summarizing the situation for the human operator receiving the call.

<Note>
  The `transfer_to_number` system tool is only available for phone calls and is not available in the
  chat widget.
</Note>


## Transfer Types

The system supports two types of transfers:

* **Conference Transfer**: Default behavior that calls the destination and adds the participant to a conference room, then removes the AI agent so only the caller and transferred participant remain.
* **SIP REFER Transfer**: Uses the SIP REFER protocol to transfer calls directly to the destination. Works with both phone numbers and SIP URIs, but only available when using SIP protocol during the conversation and requires your SIP Trunk to allow transfer via SIP REFER.

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


## Numbers that can be transferred to

Human transfer supports transferring to external phone numbers using both [SIP trunking](/docs/agents-platform/phone-numbers/sip-trunking) and [Twilio phone numbers](/docs/agents-platform/phone-numbers/twilio-integration/native-integration).


## Enabling human transfer

Human transfer is configured using the `transfer_to_number` system tool.

<Steps>
  <Step title="Add the transfer tool">
    Enable human transfer by selecting the `transfer_to_number` system tool in your agent's configuration within the `Agent` tab. Choose "Transfer to Human" when adding a tool.

    <Frame background="subtle" caption="Select 'Transfer to Human' tool">
      {/* Placeholder for image showing adding the 'Transfer to Human' tool */}

      <img src="file:3926bc47-4f81-4f26-a542-80f670bef357" alt="Add Human Transfer Tool" />
    </Frame>
  </Step>

  <Step title="Configure tool description (optional)">
    You can provide a custom description to guide the LLM on when to trigger a transfer. If left blank, a default description encompassing the defined transfer rules will be used.

    <Frame background="subtle" caption="Configure transfer tool description">
      {/* Placeholder for image showing the tool description field */}

      <img src="file:2446a980-99cd-48a2-a44e-7f4a6781b162" alt="Human Transfer Tool Description" />
    </Frame>
  </Step>

  <Step title="Define transfer rules">
    Configure the specific rules for transferring to phone numbers or SIP URIs. For each rule, specify:

    * **Transfer Type**: Choose between Conference (default) or SIP REFER transfer methods
    * **Number Type**: Select Phone for regular phone numbers or SIP URI for SIP addresses
    * **Phone Number/SIP URI**: The target destination in the appropriate format:
      * Phone numbers: E.164 format (e.g., +12125551234)
      * SIP URIs: SIP format (e.g., sip:[1234567890@example.com](mailto:1234567890@example.com))
    * **Condition**: A natural language description of the circumstances under which the transfer should occur (e.g., "User explicitly requests to speak to a human", "User needs to update sensitive account information").

    The LLM will use these conditions, along with the tool description, to decide when and to which destination to transfer.

    <Note>
      **SIP REFER transfers** require SIP protocol during the conversation and your SIP Trunk must allow transfer via SIP REFER. Only SIP REFER supports transferring to a SIP URI.
    </Note>

    <Frame background="subtle" caption="Define transfer rules with phone number and condition">
      {/* Placeholder for image showing transfer rules configuration */}

      <img src="file:08509d3b-9c02-4a97-8a4c-18af1f8293e6" alt="Human Transfer Rules Configuration" />
    </Frame>

    <Note>
      Ensure destinations are correctly formatted:

      * Phone numbers: E.164 format and associated with a properly configured account
      * SIP URIs: Valid SIP format (sip:user\@domain or sips:user\@domain)
    </Note>
  </Step>
</Steps>


## API Implementation

You can configure the `transfer_to_number` system tool when creating or updating an agent via the API. The tool allows specifying messages for both the client (user being transferred) and the agent (human operator receiving the call).

<CodeBlocks>
  ```python
  from elevenlabs import (
      ConversationalConfig,
      ElevenLabs,
      AgentConfig,
      PromptAgent,
      PromptAgentInputToolsItem_System,
      SystemToolConfigInputParams_TransferToNumber,
      PhoneNumberTransfer,
  )

  # Initialize the client
  elevenlabs = ElevenLabs(api_key="YOUR_API_KEY")

  # Define transfer rules
  transfer_rules = [
      PhoneNumberTransfer(
          transfer_destination={"type": "phone", "phone_number": "+15551234567"},
          condition="When the user asks for billing support.",
          transfer_type="conference"
      ),
      PhoneNumberTransfer(
          transfer_destination={"type": "sip_uri", "sip_uri": "sip:support@example.com"},
          condition="When the user requests to file a formal complaint.",
          transfer_type="sip_refer"
      )
  ]

  # Create the transfer tool configuration
  transfer_tool = PromptAgentInputToolsItem_System(
      type="system",
      name="transfer_to_human",
      description="Transfer the user to a specialized agent based on their request.", # Optional custom description
      params=SystemToolConfigInputParams_TransferToNumber(
          transfers=transfer_rules
      )
  )

  # Create the agent configuration
  conversation_config = ConversationalConfig(
      agent=AgentConfig(
          prompt=PromptAgent(
              prompt="You are a helpful assistant.",
              first_message="Hi, how can I help you today?",
              tools=[transfer_tool],
          )
      )
  )

  # Create the agent
  response = elevenlabs.conversational_ai.agents.create(
      conversation_config=conversation_config
  )

  # Note: When the LLM decides to call this tool, it needs to provide:
  # - transfer_number: The phone number to transfer to (must match one defined in rules).
  # - client_message: Message read to the user during transfer.
  # - agent_message: Message read to the human operator receiving the call.
  ```

  ```javascript
  import { ElevenLabs } from '@elevenlabs/elevenlabs-js';

  // Initialize the client
  const elevenlabs = new ElevenLabs({
    apiKey: 'YOUR_API_KEY',
  });

  // Define transfer rules
  const transferRules = [
    {
      transferDestination: { type: 'phone', phoneNumber: '+15551234567' },
      condition: 'When the user asks for billing support.',
      transferType: 'conference'
    },
    {
      transferDestination: { type: 'sip_uri', sipUri: 'sip:support@example.com' },
      condition: 'When the user requests to file a formal complaint.',
      transferType: 'sip_refer'
    },
  ];

  // Create the agent with the transfer tool
  await elevenlabs.conversationalAi.agents.create({
    conversationConfig: {
      agent: {
        prompt: {
          prompt: 'You are a helpful assistant.',
          firstMessage: 'Hi, how can I help you today?',
          tools: [
            {
              type: 'system',
              name: 'transfer_to_number',
              description: 'Transfer the user to a human operator based on their request.', // Optional custom description
              params: {
                systemToolType: 'transfer_to_number',
                transfers: transferRules,
              },
            },
          ],
        },
      },
    },
  });

  // Note: When the LLM decides to call this tool, it needs to provide:
  // - transfer_number: The phone number to transfer to (must match one defined in rules).
  // - client_message: Message read to the user during transfer.
  // - agent_message: Message read to the human operator receiving the call.
  </code_block_to_apply_changes_from>
  ```
</CodeBlocks>



# Skip turn

> Allow your agent to pause and wait for the user to speak next.


## Overview

The **Skip Turn** tool allows your conversational agent to explicitly pause and wait for the user to speak or act before continuing. This system tool is useful when the user indicates they need a moment, for example, by saying "Give me a second," "Let me think," or "One moment please."


## Functionality

* **User-Initiated Pause**: The tool is designed to be invoked by the LLM when it detects that the user needs a brief pause without interruption.
* **No Verbal Response**: After this tool is called, the assistant will not speak. It waits for the user to re-engage or for another turn-taking condition to be met.
* **Seamless Conversation Flow**: It helps maintain a natural conversational rhythm by respecting the user's need for a short break without ending the interaction or the agent speaking unnecessarily.

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

### API implementation

When creating an agent via API, you can add the Skip Turn tool to your agent configuration. It should be defined as a system tool, with the name `skip_turn`.

<CodeBlocks>
  ```python
  from elevenlabs import (
      ConversationalConfig,
      ElevenLabs,
      AgentConfig,
      PromptAgent,
      PromptAgentInputToolsItem_System
  )

  # Initialize the client
  elevenlabs = ElevenLabs(api_key="YOUR_API_KEY")

  # Create the skip turn tool
  skip_turn_tool = PromptAgentInputToolsItem_System(
      name="skip_turn",
      description=""  # Optional: Customize when the tool should be triggered, or leave blank for default.
  )

  # Create the agent configuration
  conversation_config = ConversationalConfig(
      agent=AgentConfig(
          prompt=PromptAgent(
              tools=[skip_turn_tool]
          )
      )
  )

  # Create the agent
  response = elevenlabs.conversational_ai.agents.create(
      conversation_config=conversation_config
  )
  ```

  ```javascript
  import { ElevenLabs } from '@elevenlabs/elevenlabs-js';

  // Initialize the client
  const elevenlabs = new ElevenLabs({
    apiKey: 'YOUR_API_KEY',
  });

  // Create the agent with skip turn tool
  await elevenlabs.conversationalAi.agents.create({
    conversationConfig: {
      agent: {
        prompt: {
          tools: [
            {
              type: 'system',
              name: 'skip_turn',
              description: '', // Optional: Customize when the tool should be triggered, or leave blank for default.
            },
          ],
        },
      },
    },
  });
  ```
</CodeBlocks>


## UI configuration

You can also configure the Skip Turn tool directly within the Agent's UI, in the tools section.

<Steps>
  ### Step 1: Add a new tool

  Navigate to your agent's configuration page. In the "Tools" section, click on "Add tool", the `Skip Turn` option will already be available.

  <Frame background="subtle">
    <img src="file:fe292662-c94d-4f38-990c-53e72b8896c3" alt="Add Skip Turn Tool Option" />
  </Frame>

  ### Step 2: Configure the tool

  You can optionally provide a description to customize when the LLM should trigger this tool, or leave it blank to use the default behavior.

  <Frame background="subtle">
    <img src="file:fa5d3caa-6ba9-452f-a0cd-0a8b52fd0380" alt="Configure Skip Turn Tool" />
  </Frame>

  ### Step 3: Enable the tool

  Once configured, the `Skip Turn` tool will appear in your agent's list of enabled tools and the agent will be able to skip turns. .

  <Frame background="subtle">
    <img src="file:4e8bcc2b-b4e5-479f-838b-388eb74dbc1f" alt="Skip Turn Tool Enabled" />
  </Frame>
</Steps>



# Play keypad touch tone

> Enable agents to play DTMF tones to interact with automated phone systems and navigate menus.


## Overview

The keypad touch tone tool allows ElevenLabs agents to play DTMF (Dual-Tone Multi-Frequency) tones during phone calls; these are the tones that are played when you press numbers on your keypad. This enables agents to interact with automated phone systems, navigate voice menus, enter extensions, input PIN codes, and perform other touch-tone operations that would typically require a human caller to press keys on their phone keypad.

This system tool supports standard DTMF tones (0-9, \*, #) as well as pause commands for timing control. It works seamlessly with both Twilio and SIP trunking phone integrations, automatically generating the appropriate audio tones for the underlying telephony infrastructure.


## Functionality

* **Standard DTMF tones**: Supports all standard keypad characters (0-9, \*, #)
* **Pause control**: Includes pause commands for precise timing (w = 0.5s, W = 1.0s)
* **Multi-provider support**: Works with both Twilio and SIP trunking integrations

This system tool can be used to navigate phone menus, enter extensions and input codes.
The LLM determines when and what tones to play based on conversation context.

The default tool description explains to the LLM powering the conversation that it has access to play these tones,
and we recommend updating your agent's system prompt to explain when the agent should call this tool.

**Parameters**:

* `reason` (string, optional): The reason for playing the DTMF tones (e.g., "navigating to extension", "entering PIN")
* `dtmf_tones` (string, required): The DTMF sequence to play. Valid characters: 0-9, \*, #, w (0.5s pause), W (1s pause)

**Function call format**:

```json
{
  "type": "function",
  "function": {
    "name": "play_keypad_touch_tone",
    "arguments": "{"reason": "Navigating to customer service", "dtmf_tones": "2"}"
  }
}
```


## Supported characters

The tool supports the following DTMF characters and commands:

* **Digits**: `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`
* **Special tones**: `*` (star), `#` (pound/hash)
* **Pause commands**:
  * `w` - Short pause (0.5 seconds)
  * `W` - Long pause (1.0 second)


## API Implementation

You can configure the `play_keypad_touch_tone` system tool when creating or updating an agent via the API. This tool requires no additional configuration parameters beyond enabling it.

<CodeBlocks>
  ```python
  from elevenlabs import (
      ConversationalConfig,
      ElevenLabs,
      AgentConfig,
      PromptAgent,
      PromptAgentInputToolsItem_System,
      SystemToolConfigInputParams_PlayKeypadTouchTone,
  )

  # Initialize the client
  elevenlabs = ElevenLabs(api_key="YOUR_API_KEY")

  # Create the keypad touch tone tool configuration
  keypad_tool = PromptAgentInputToolsItem_System(
      type="system",
      name="play_keypad_touch_tone",
      description="Play DTMF tones to interact with automated phone systems.", # Optional custom description
      params=SystemToolConfigInputParams_PlayKeypadTouchTone(
          system_tool_type="play_keypad_touch_tone"
      )
  )

  # Create the agent configuration
  conversation_config = ConversationalConfig(
      agent=AgentConfig(
          prompt=PromptAgent(
              prompt="You are a helpful assistant that can interact with phone systems.",
              first_message="Hi, I can help you navigate phone systems. How can I assist you today?",
              tools=[keypad_tool],
          )
      )
  )

  # Create the agent
  response = elevenlabs.conversational_ai.agents.create(
      conversation_config=conversation_config
  )
  ```

  ```javascript
  import { ElevenLabs } from '@elevenlabs/elevenlabs-js';

  // Initialize the client
  const elevenlabs = new ElevenLabs({
    apiKey: 'YOUR_API_KEY',
  });

  // Create the agent with the keypad touch tone tool
  await elevenlabs.conversationalAi.agents.create({
    conversationConfig: {
      agent: {
        prompt: {
          prompt: 'You are a helpful assistant that can interact with phone systems.',
          firstMessage: 'Hi, I can help you navigate phone systems. How can I assist you today?',
          tools: [
            {
              type: 'system',
              name: 'play_keypad_touch_tone',
              description: 'Play DTMF tones to interact with automated phone systems.', // Optional custom description
              params: {
                systemToolType: 'play_keypad_touch_tone',
              },
            },
          ],
        },
      },
    },
  });
  ```
</CodeBlocks>

<Note>
  The tool only works during active phone calls powered by Twilio or SIP trunking. It will return an
  error if called outside of a phone conversation context.
</Note>



# Voicemail detection

> Enable agents to automatically detect voicemail systems and optionally leave messages.


## Overview

The **Voicemail Detection** tool allows your ElevenLabs agent to automatically identify when a call has been answered by a voicemail system rather than a human. This system tool enables agents to handle automated voicemail scenarios gracefully by either leaving a pre-configured message or ending the call immediately.


## Functionality

* **Automatic Detection**: The LLM analyzes conversation patterns to identify voicemail systems based on automated greetings and prompts
* **Configurable Response**: Choose to either leave a custom voicemail message or end the call immediately when voicemail is detected
* **Call Termination**: After detection and optional message delivery, the call is automatically terminated
* **Status Tracking**: Voicemail detection events are logged and can be viewed in conversation history and batch call results

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


## Configuration Options

The voicemail detection tool can be configured with the following options:

<Frame background="subtle">
  ![Voicemail detection configuration
  interface](file:4387ea25-f4d4-4030-9b90-3500a09eedec)
</Frame>

* **Voicemail Message**: You can configure an optional custom message to be played when voicemail is detected


## API Implementation

When creating an agent via API, you can add the Voicemail Detection tool to your agent configuration. It should be defined as a system tool:

<CodeBlocks>
  ```python
  from elevenlabs import (
      ConversationalConfig,
      ElevenLabs,
      AgentConfig,
      PromptAgent,
      PromptAgentInputToolsItem_System
  )

  # Initialize the client
  elevenlabs = ElevenLabs(api_key="YOUR_API_KEY")

  # Create the voicemail detection tool
  voicemail_detection_tool = PromptAgentInputToolsItem_System(
      name="voicemail_detection",
      description=""  # Optional: Customize when the tool should be triggered
  )

  # Create the agent configuration
  conversation_config = ConversationalConfig(
      agent=AgentConfig(
          prompt=PromptAgent(
              tools=[voicemail_detection_tool]
          )
      )
  )

  # Create the agent
  response = elevenlabs.conversational_ai.agents.create(
      conversation_config=conversation_config
  )
  ```

  ```javascript
  import { ElevenLabs } from '@elevenlabs/elevenlabs-js';

  // Initialize the client
  const elevenlabs = new ElevenLabs({
    apiKey: 'YOUR_API_KEY',
  });

  // Create the agent with voicemail detection tool
  await elevenlabs.conversationalAi.agents.create({
    conversationConfig: {
      agent: {
        prompt: {
          tools: [
            {
              type: 'system',
              name: 'voicemail_detection',
              description: '', // Optional: Customize when the tool should be triggered
            },
          ],
        },
      },
    },
  });
  ```
</CodeBlocks>



# Personalization

> Learn how to personalize your agent's behavior using dynamic variables and overrides.


## Overview

Personalization allows you to adapt your agent's behavior for each individual user, enabling more natural and contextually relevant conversations. ElevenLabs offers multiple approaches to personalization:

1. **Dynamic Variables** - Inject runtime values into prompts and messages
2. **Overrides** - Completely replace system prompts or messages
3. **Twilio Integration** - Personalize inbound call experiences via webhooks


## Personalization Methods

<CardGroup cols={3}>
  <Card title="Dynamic Variables" icon="duotone lambda" href="/docs/agents-platform/customization/personalization/dynamic-variables">
    Define runtime values using `{{ var_name }}` syntax to personalize your agent's messages, system
    prompts, and tools.
  </Card>

  <Card title="Overrides" icon="duotone sliders" href="/docs/agents-platform/customization/personalization/overrides">
    Completely replace system prompts, first messages, language, or voice settings for each
    conversation.
  </Card>

  <Card title="Twilio Integration" icon="duotone phone-arrow-down-left" href="/docs/agents-platform/customization/personalization/twilio-personalization">
    Dynamically personalize inbound Twilio calls using webhook data.
  </Card>
</CardGroup>


## Conversation Initiation Client Data Structure

The `conversation_initiation_client_data` object defines what can be customized when starting a conversation:

```json
{
  "type": "conversation_initiation_client_data",
  "conversation_config_override": {
    "agent": {
      "prompt": {
        "prompt": "overriding system prompt"
      },
      "first_message": "overriding first message",
      "language": "en"
    },
    "tts": {
      "voice_id": "voice-id-here"
    }
  },
  "custom_llm_extra_body": {
    "temperature": 0.7,
    "max_tokens": 100
  },
  "dynamic_variables": {
    "string_var": "text value",
    "number_var": 1.2,
    "integer_var": 123,
    "boolean_var": true
  },
  "user_id": "your_custom_user_id"
}
```


## Choosing the Right Approach

<Table>
  <thead>
    <tr>
      <th>
        Method
      </th>

      <th>
        Best For
      </th>

      <th>
        Implementation
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        **Dynamic Variables**
      </td>

      <td>
        * Inserting user-specific data into templated content - Maintaining consistent agent
          behavior with personalized details - Personalizing tool parameters
      </td>

      <td>
        Define variables with 

        `{{ variable_name }}`

         and pass values at runtime
      </td>
    </tr>

    <tr>
      <td>
        **Overrides**
      </td>

      <td>
        * Completely changing agent behavior per user - Switching languages or voices - Legacy
          applications (consider migrating to Dynamic Variables)
      </td>

      <td>
        Enable specific override permissions in security settings and pass complete replacement
        content
      </td>
    </tr>
  </tbody>
</Table>


## Learn More

* [Dynamic Variables Documentation](/docs/agents-platform/customization/personalization/dynamic-variables)
* [Overrides Documentation](/docs/agents-platform/customization/personalization/overrides)
* [Twilio Integration Documentation](/docs/agents-platform/customization/personalization/twilio-personalization)



# Dynamic variables

> Pass runtime values to personalize your agent's behavior.

**Dynamic variables** allow you to inject runtime values into your agent's messages, system prompts, and tools. This enables you to personalize each conversation with user-specific data without creating multiple agents.


## Overview

Dynamic variables can be integrated into multiple aspects of your agent:

* **System prompts** to customize behavior and context
* **First messages** to personalize greetings
* **Tool parameters and headers** to pass user-specific data

Here are a few examples where dynamic variables are useful:

* **Personalizing greetings** with user names
* **Including account details** in responses
* **Passing data** to tool calls
* **Customizing behavior** based on subscription tiers
* **Accessing system information** like conversation ID or call duration

<Info>
  Dynamic variables are ideal for injecting user-specific data that shouldn't be hardcoded into your
  agent's configuration.
</Info>


## System dynamic variables

Your agent has access to these automatically available system variables:

* `system__agent_id` - Unique identifier of the agent that initiated the conversation (stays stable throughout the conversation)
* `system__current_agent_id` - Unique identifier of the currently active agent (changes after agent transfers)
* `system__caller_id` - Caller's phone number (voice calls only)
* `system__called_number` - Destination phone number (voice calls only)
* `system__call_duration_secs` - Call duration in seconds
* `system__time_utc` - Current UTC time (ISO format)
* `system__time` - Current time in the specified timezone (ISO format)
* `system__timezone` - User-provided timezone (must be valid for tzinfo)
* `system__conversation_id` - ElevenLabs' unique conversation identifier
* `system__call_sid` - Call SID (twilio calls only)

System variables:

* Are available without runtime configuration
* Are prefixed with `system__` (reserved prefix)
* In system prompts: Set once at conversation start (value remains static)
* In tool calls: Updated at execution time (value reflects current state)

<Warning>
  Custom dynamic variables cannot use the reserved 

  `system__`

   prefix.
</Warning>


## Secret dynamic variables

Secret dynamic variables are populated in the same way as normal dynamic variables but indicate to our Agents platform that these should
only be used in dynamic variable headers and never sent to an LLM provider as part of an agent's system prompt or first message.

We recommend using these for auth tokens or private IDs that should not be sent to an LLM. To create a secret dynamic variable, simply prefix the dynamic variable with `secret__`.


## Updating dynamic variables from tools

[Tool calls](https://elevenlabs.io/docs/agents-platform/customization/tools) can create or update dynamic variables if they return a valid JSON object. To specify what should be extracted, set the object path(s) using dot notation. If the field or path doesn't exist, nothing is updated.

Example of a response object and dot notation:

* Status corresponds to the path: `response.status`
* The first user's email in the users array corresponds to the path: `response.users.0.email`

<CodeGroup>
  ```JSON title="JSON"
  {
    "response": {
      "status": 200,
      "message": "Successfully found 5 users",
      "users": [
        "user_1": {
          "user_name": "test_user_1",
          "email": "test_user_1@email.com"
        }
      ]
    }
  }
  ```
</CodeGroup>

To update a dynamic variable to be the first user's email, set the assignment like so.

<Frame background="subtle">
  ![Query parameters](file:15c11196-7709-4346-9d58-b4b735c82582)
</Frame>

Assignments are a field of each server tool, that can be found documented [here](/docs/agents-platform/api-reference/tools/create#response.body.tool_config.SystemToolConfig.assignments).


## Guide

### Prerequisites

* An [ElevenLabs account](https://elevenlabs.io)
* A configured ElevenLabs Conversational Agent ([create one here](/docs/agents-platform/quickstart))

<Steps>
  <Step title="Define dynamic variables in prompts">
    Add variables using double curly braces `{{variable_name}}` in your:

    * System prompts
    * First messages
    * Tool parameters

    <Frame background="subtle">
      ![Dynamic variables in messages](file:70e1601c-0e4b-43bf-bece-9a30a82aade7)
    </Frame>

    <Frame background="subtle">
      ![Dynamic variables in messages](file:ab42906d-7891-4655-ac62-e78d932dea2e)
    </Frame>
  </Step>

  <Step title="Define dynamic variables in tools">
    You can also define dynamic variables in the tool configuration.
    To create a new dynamic variable, set the value type to Dynamic variable and click the `+` button.

    <Frame background="subtle">
      ![Setting placeholders](file:552ba0e8-7972-4aac-8f1c-889fd7b9d3d9)
    </Frame>

    <Frame background="subtle">
      ![Setting placeholders](file:d45882e4-26ad-4244-93ac-0114d77b83e6)
    </Frame>
  </Step>

  <Step title="Set placeholders">
    Configure default values in the web interface for testing:

    <Frame background="subtle">
      ![Setting placeholders](file:37fcd5e0-d568-4dbf-bd3c-2b9d7da84ccd)
    </Frame>
  </Step>

  <Step title="Pass variables at runtime">
    When starting a conversation, provide the dynamic variables in your code:

    <Tip>
      Ensure you have the latest [SDK](/docs/agents-platform/libraries) installed.
    </Tip>

    <CodeGroup>
      ```python title="Python" focus={10-23} maxLines=25
      import os
      import signal
      from elevenlabs.client import ElevenLabs
      from elevenlabs.conversational_ai.conversation import Conversation, ConversationInitiationData
      from elevenlabs.conversational_ai.default_audio_interface import DefaultAudioInterface

      agent_id = os.getenv("AGENT_ID")
      api_key = os.getenv("ELEVENLABS_API_KEY")
      elevenlabs = ElevenLabs(api_key=api_key)

      dynamic_vars = {
          "user_name": "Angelo",
      }

      config = ConversationInitiationData(
          dynamic_variables=dynamic_vars
      )

      conversation = Conversation(
          elevenlabs,
          agent_id,
          config=config,
          # Assume auth is required when API_KEY is set.
          requires_auth=bool(api_key),
          # Use the default audio interface.
          audio_interface=DefaultAudioInterface(),
          # Simple callbacks that print the conversation to the console.
          callback_agent_response=lambda response: print(f"Agent: {response}"),
          callback_agent_response_correction=lambda original, corrected: print(f"Agent: {original} -> {corrected}"),
          callback_user_transcript=lambda transcript: print(f"User: {transcript}"),
          # Uncomment the below if you want to see latency measurements.
          # callback_latency_measurement=lambda latency: print(f"Latency: {latency}ms"),
      )

      conversation.start_session()

      signal.signal(signal.SIGINT, lambda sig, frame: conversation.end_session())
      ```

      ```javascript title="JavaScript" focus={7-20} maxLines=25
      import { Conversation } from '@elevenlabs/client';

      class VoiceAgent {
        ...

        async startConversation() {
          try {
              // Request microphone access
              await navigator.mediaDevices.getUserMedia({ audio: true });

              this.conversation = await Conversation.startSession({
                  agentId: 'agent_id_goes_here', // Replace with your actual agent ID

                  dynamicVariables: {
                      user_name: 'Angelo'
                  },

                  ... add some callbacks here
              });
          } catch (error) {
              console.error('Failed to start conversation:', error);
              alert('Failed to start conversation. Please ensure microphone access is granted.');
          }
        }
      }
      ```

      ```swift title="Swift"
      let dynamicVars: [String: DynamicVariableValue] = [
        "customer_name": .string("John Doe"),
        "account_balance": .number(5000.50),
        "user_id": .int(12345),
        "is_premium": .boolean(true)
      ]

      // Create session config with dynamic variables
      let config = SessionConfig(
          agentId: "your_agent_id",
          dynamicVariables: dynamicVars
      )

      // Start the conversation
      let conversation = try await Conversation.startSession(
          config: config
      )
      ```

      ```html title="Widget"
      <elevenlabs-convai
        agent-id="your-agent-id"
        dynamic-variables='{"user_name": "John", "account_type": "premium"}'
      ></elevenlabs-convai>
      ```
    </CodeGroup>
  </Step>
</Steps>


## Public Talk-to Page Integration

The public talk-to page supports dynamic variables through URL parameters, enabling you to personalize conversations when sharing agent links. This is particularly useful for embedding personalized agents in websites, emails, or marketing campaigns.

### URL Parameter Methods

There are two methods to pass dynamic variables to the public talk-to page:

#### Method 1: Base64-Encoded JSON

Pass variables as a base64-encoded JSON object using the `vars` parameter:

```
https://elevenlabs.io/app/talk-to?agent_id=your_agent_id&vars=eyJ1c2VyX25hbWUiOiJKb2huIiwiYWNjb3VudF90eXBlIjoicHJlbWl1bSJ9
```

The `vars` parameter contains base64-encoded JSON:

```json
{ "user_name": "John", "account_type": "premium" }
```

#### Method 2: Individual Query Parameters

Pass variables using `var_` prefixed query parameters:

```
https://elevenlabs.io/app/talk-to?agent_id=your_agent_id&var_user_name=John&var_account_type=premium
```

### Parameter Precedence

When both methods are used simultaneously, individual `var_` parameters take precedence over the base64-encoded variables to prevent conflicts:

```
https://elevenlabs.io/app/talk-to?agent_id=your_agent_id&vars=eyJ1c2VyX25hbWUiOiJKYW5lIn0=&var_user_name=John
```

In this example, `user_name` will be "John" (from `var_user_name`) instead of "Jane" (from the base64-encoded `vars`).

### Implementation Examples

<Tabs>
  <Tab title="JavaScript URL Generation">
    ```javascript
    // Method 1: Base64-encoded JSON
    function generateTalkToURL(agentId, variables) {
      const baseURL = 'https://elevenlabs.io/app/talk-to';
      const encodedVars = btoa(JSON.stringify(variables));
      return `${baseURL}?agent_id=${agentId}&vars=${encodedVars}`;
    }

    // Method 2: Individual parameters
    function generateTalkToURLWithParams(agentId, variables) {
      const baseURL = 'https://elevenlabs.io/app/talk-to';
      const params = new URLSearchParams({ agent_id: agentId });

      Object.entries(variables).forEach(([key, value]) => {
        params.append(`var_${key}`, encodeURIComponent(value));
      });

      return `${baseURL}?${params.toString()}`;
    }

    // Usage
    const variables = {
      user_name: "John Doe",
      account_type: "premium",
      session_id: "sess_123"
    };

    const urlMethod1 = generateTalkToURL("your_agent_id", variables);
    const urlMethod2 = generateTalkToURLWithParams("your_agent_id", variables);
    ```
  </Tab>

  <Tab title="Python URL Generation">
    ```python
    import base64
    import json
    from urllib.parse import urlencode, quote

    def generate_talk_to_url(agent_id, variables):
        """Generate URL with base64-encoded variables"""
        base_url = "https://elevenlabs.io/app/talk-to"
        encoded_vars = base64.b64encode(json.dumps(variables).encode()).decode()
        return f"{base_url}?agent_id={agent_id}&vars={encoded_vars}"

    def generate_talk_to_url_with_params(agent_id, variables):
        """Generate URL with individual var_ parameters"""
        base_url = "https://elevenlabs.io/app/talk-to"
        params = {"agent_id": agent_id}

        for key, value in variables.items():
            params[f"var_{key}"] = value

        return f"{base_url}?{urlencode(params)}"

    # Usage
    variables = {
        "user_name": "John Doe",
        "account_type": "premium",
        "session_id": "sess_123"
    }

    url_method1 = generate_talk_to_url("your_agent_id", variables)
    url_method2 = generate_talk_to_url_with_params("your_agent_id", variables)
    ```
  </Tab>

  <Tab title="Manual URL Construction">
    ```
    # Base64-encoded method
    1. Create JSON: {"user_name": "John", "account_type": "premium"}
    2. Encode to base64: eyJ1c2VyX25hbWUiOiJKb2huIiwiYWNjb3VudF90eXBlIjoicHJlbWl1bSJ9
    3. Add to URL: https://elevenlabs.io/app/talk-to?agent_id=your_agent_id&vars=eyJ1c2VyX25hbWUiOiJKb2huIiwiYWNjb3VudF90eXBlIjoicHJlbWl1bSJ9

    # Individual parameters method
    1. Add each variable with var_ prefix
    2. URL encode values if needed
    3. Final URL: https://elevenlabs.io/app/talk-to?agent_id=your_agent_id&var_user_name=John&var_account_type=premium
    ```
  </Tab>
</Tabs>


## Supported Types

Dynamic variables support these value types:

<CardGroup cols={3}>
  <Card title="String">
    Text values
  </Card>

  <Card title="Number">
    Numeric values
  </Card>

  <Card title="Boolean">
    True/false values
  </Card>
</CardGroup>


## Troubleshooting

<AccordionGroup>
  <Accordion title="Variables not replacing">
    Verify that:

    * Variable names match exactly (case-sensitive)
    * Variables use double curly braces: `{{ variable_name }}`
    * Variables are included in your dynamic\_variables object
  </Accordion>

  <Accordion title="Type errors">
    Ensure that:

    * Variable values match the expected type
    * Values are strings, numbers, or booleans only
  </Accordion>
</AccordionGroup>



# Overrides

> Tailor each conversation with personalized context for each user.

<Warning>
  While overrides are still supported for completely replacing system prompts or first messages, we
  recommend using [Dynamic
  Variables](/docs/agents-platform/customization/personalization/dynamic-variables) as the preferred
  way to customize your agent's responses and inject real-time data. Dynamic Variables offer better
  maintainability and a more structured approach to personalization.
</Warning>

**Overrides** enable your assistant to adapt its behavior for each user interaction. You can pass custom data and settings at the start of each conversation, allowing the assistant to personalize its responses and knowledge with real-time context. Overrides completely override the agent's default values defined in the agent's [dashboard](https://elevenlabs.io/app/agents/agents).


## Overview

Overrides allow you to modify your AI agent's behavior in real-time without creating multiple agents. This enables you to personalize responses with user-specific data.

Overrides can be enabled for the following fields in the agent's security settings:

* System prompt
* First message
* Language
* Voice ID

When overrides are enabled for a field, providing an override is still optional. If not provided, the agent will use the default values defined in the agent's [dashboard](https://elevenlabs.io/app/agents/agents). An error will be thrown if an override is provided for a field that does not have overrides enabled.

Here are a few examples where overrides can be useful:

* **Greet users** by their name
* **Include account-specific details** in responses
* **Adjust the agent's language** or tone based on user preferences
* **Pass real-time data** like account balances or order status

<Info>
  Overrides are particularly useful for applications requiring personalized interactions or handling
  sensitive user data that shouldn't be stored in the agent's base configuration.
</Info>


## Guide

### Prerequisites

* An [ElevenLabs account](https://elevenlabs.io)
* A configured ElevenLabs Conversational Agent ([create one here](/docs/agents-platform/quickstart))

This guide will show you how to override the default agent **System prompt** & **First message**.

<Steps>
  <Step title="Enable overrides">
    For security reasons, overrides are disabled by default. Navigate to your agent's settings and
    select the **Security** tab.

    Enable the `First message` and `System prompt` overrides.

    <Frame background="subtle">
      ![Enable overrides](file:3e9da2c7-e6c3-41c5-b0a4-82c0d9229da2)
    </Frame>
  </Step>

  <Step title="Override the conversation">
    In your code, where the conversation is started, pass the overrides as a parameter.

    <Tip>
      Ensure you have the latest [SDK](/docs/agents-platform/libraries) installed.
    </Tip>

    <CodeGroup>
      ```python title="Python" focus={3-14} maxLines=14
      from elevenlabs.conversational_ai.conversation import Conversation, ConversationInitiationData
      ...
      conversation_override = {
          "agent": {
              "prompt": {
                  "prompt": f"The customer's bank account balance is {customer_balance}. They are based in {customer_location}." # Optional: override the system prompt.
              },
              "first_message": f"Hi {customer_name}, how can I help you today?", # Optional: override the first_message.
              "language": "en" # Optional: override the language.
          },
          "tts": {
              "voice_id": "custom_voice_id" # Optional: override the voice.
          }
      }

      config = ConversationInitiationData(
          conversation_config_override=conversation_override
      )
      conversation = Conversation(
          ...
          config=config,
          ...
      )
      conversation.start_session()
      ```

      ```javascript title="JavaScript" focus={4-15} maxLines=15
      ...
      const conversation = await Conversation.startSession({
        ...
        overrides: {
            agent: {
                prompt: {
                    prompt: `The customer's bank account balance is ${customer_balance}. They are based in ${customer_location}.` // Optional: override the system prompt.
                },
                firstMessage: `Hi ${customer_name}, how can I help you today?`, // Optional: override the first message.
                language: "en" // Optional: override the language.
            },
            tts: {
                voiceId: "custom_voice_id" // Optional: override the voice.
            }
        },
        ...
      })
      ```

      ```swift title="Swift" focus={3-14} maxLines=14
      import ElevenLabsSDK

      let promptOverride = ElevenLabsSDK.AgentPrompt(
          prompt: "The customer's bank account balance is \(customer_balance). They are based in \(customer_location)." // Optional: override the system prompt.
      )
      let agentConfig = ElevenLabsSDK.AgentConfig(
          prompt: promptOverride, // Optional: override the system prompt.
          firstMessage: "Hi \(customer_name), how can I help you today?", // Optional: override the first message.
          language: .en // Optional: override the language.
      )
      let overrides = ElevenLabsSDK.ConversationConfigOverride(
          agent: agentConfig, // Optional: override agent settings.
          tts: TTSConfig(voiceId: "custom_voice_id") // Optional: override the voice.
      )

      let config = ElevenLabsSDK.SessionConfig(
          agentId: "",
          overrides: overrides
      )

      let conversation = try await ElevenLabsSDK.Conversation.startSession(
        config: config,
        callbacks: callbacks
      )
      ```

      ```html title="Widget"
        <elevenlabs-convai
          agent-id="your-agent-id"
          override-language="es"         <!-- Optional: override the language -->
          override-prompt="Custom system prompt for this user"  <!-- Optional: override the system prompt -->
          override-first-message="Hi! How can I help you today?"  <!-- Optional: override the first message -->
          override-voice-id="custom_voice_id"  <!-- Optional: override the voice -->
        ></elevenlabs-convai>
      ```
    </CodeGroup>

    <Note>
      When using overrides, omit any fields you don't want to override rather than setting them to empty strings or null values. Only include the fields you specifically want to customize.
    </Note>
  </Step>
</Steps>



# Twilio personalization

> Configure personalization for incoming Twilio calls using webhooks.


## Overview

When receiving inbound Twilio calls, you can dynamically fetch conversation initiation data through a webhook. This allows you to customize your agent's behavior based on caller information and other contextual data.

<iframe width="100%" height="400" src="https://www.youtube-nocookie.com/embed/cAuSo8qNs-8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen />


## How it works

1. When a Twilio call is received, the ElevenLabs Agents platform will make a webhook call to your specified endpoint, passing call information (`caller_id`, `agent_id`, `called_number`, `call_sid`) as arguments
2. Your webhook returns conversation initiation client data, including dynamic variables and overrides (an example is shown below)
3. This data is used to initiate the conversation

<Tip>
  The system uses Twilio's connection/dialing period to fetch webhook data in parallel, creating a
  seamless experience where:

  * Users hear the expected telephone connection sound
  * In parallel, the Agents Platform fetches necessary webhook data
  * The conversation is initiated with the fetched data by the time the audio connection is established
</Tip>


## Configuration

<Steps>
  <Step title="Configure webhook details">
    In the [settings page](https://elevenlabs.io/app/agents/settings) of the Agents Platform, configure the webhook URL and add any
    secrets needed for authentication.

    <Frame background="subtle">
      ![Enable webhook](file:b5c71959-d168-42a6-ae50-2ae681fdd8d8)
    </Frame>

    Click on the webhook to modify which secrets are sent in the headers.

    <Frame background="subtle">
      ![Add secrets to headers](file:f644bc2c-37a7-477c-969a-cb71b680218a)
    </Frame>
  </Step>

  <Step title="Enable fetching conversation initiation data">
    In the "Security" tab of the [agent's page](https://elevenlabs.io/app/agents/agents/), enable fetching conversation initiation data for inbound Twilio calls, and define fields that can be overridden.

    <Frame background="subtle">
      ![Enable webhook](file:934ce04c-b0a1-4748-90a7-f624c867eec9)
    </Frame>
  </Step>

  <Step title="Implement the webhook endpoint to receive Twilio data">
    The webhook will receive a POST request with the following parameters:

    | Parameter       | Type   | Description                            |
    | --------------- | ------ | -------------------------------------- |
    | `caller_id`     | string | The phone number of the caller         |
    | `agent_id`      | string | The ID of the agent receiving the call |
    | `called_number` | string | The Twilio number that was called      |
    | `call_sid`      | string | Unique identifier for the Twilio call  |
  </Step>

  <Step title="Return conversation initiation client data">
    Your webhook must return a JSON response containing the initiation data for the agent.

    <Info>
      The `dynamic_variables` field must contain all dynamic variables defined for the agent. Overrides
      on the other hand are entirely optional. For more information about dynamic variables and
      overrides see the [dynamic variables](/docs/agents-platform/customization/personalization/dynamic-variables) and
      [overrides](/docs/agents-platform/customization/personalization/overrides) docs.
    </Info>

    An example response could be:

    ```json
    {
      "type": "conversation_initiation_client_data",
      "dynamic_variables": {
        "customer_name": "John Doe",
        "account_status": "premium",
        "last_interaction": "2024-01-15"
      },
      "conversation_config_override": {
        "agent": {
          "prompt": {
            "prompt": "The customer's bank account balance is $100. They are based in San Francisco."
          },
          "first_message": "Hi, how can I help you today?",
          "language": "en"
        },
        "tts": {
          "voice_id": "new-voice-id"
        }
      }
    }
    ```
  </Step>
</Steps>

The Agents Platform will use the dynamic variables to populate the conversation initiation data, and the conversation will start smoothly.

<Warning>
  Ensure your webhook responds within a reasonable timeout period to avoid delaying the call
  handling.
</Warning>


## Security

* Use HTTPS endpoints only
* Implement authentication using request headers
* Store sensitive values as secrets through the [ElevenLabs secrets manager](https://elevenlabs.io/app/agents/settings)
* Validate the incoming request parameters



# Agent authentication

> Learn how to secure access to your conversational agents

<iframe width="100%" height="400" src="https://www.youtube-nocookie.com/embed/8hZ4IWL7iqw?rel=0&autoplay=0" title="YouTube video player" frameborder="0" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen />


## Overview

When building conversational agents, you may need to restrict access to certain agents or conversations. ElevenLabs provides multiple authentication mechanisms to ensure only authorized users can interact with your agents.


## Authentication methods

ElevenLabs offers two primary methods to secure your conversational agents:

<CardGroup cols={2}>
  <Card title="Signed URLs" icon="signature" href="#using-signed-urls">
    Generate temporary authenticated URLs for secure client-side connections without exposing API
    keys.
  </Card>

  <Card title="Allowlists" icon="list-check" href="#using-allowlists">
    Restrict access to specific domains or hostnames that can connect to your agent.
  </Card>
</CardGroup>


## Using signed URLs

Signed URLs are the recommended approach for client-side applications. This method allows you to authenticate users without exposing your API key.

<Note>
  The guides below uses the [JS client](https://www.npmjs.com/package/@elevenlabs/client) and
  [Python SDK](https://github.com/elevenlabs/elevenlabs-python/).
</Note>

### How signed URLs work

1. Your server requests a signed URL from ElevenLabs using your API key.
2. ElevenLabs generates a temporary token and returns a signed WebSocket URL.
3. Your client application uses this signed URL to establish a WebSocket connection.
4. The signed URL expires after 15 minutes.

<Warning>
  Never expose your ElevenLabs API key client-side.
</Warning>

### Generate a signed URL via the API

To obtain a signed URL, make a request to the `get_signed_url` [endpoint](/docs/agents-platform/api-reference/conversations/get-signed-url) with your agent ID:

<CodeBlocks>
  ```python
  # Server-side code using the Python SDK
  from elevenlabs.client import ElevenLabs
  async def get_signed_url():
      try:
          elevenlabs = ElevenLabs(api_key="your-api-key")
          response = await elevenlabs.conversational_ai.conversations.get_signed_url(agent_id="your-agent-id")
          return response.signed_url
      except Exception as error:
          print(f"Error getting signed URL: {error}")
          raise
  ```

  ```javascript
  import { ElevenLabsClient } from '@elevenlabs/elevenlabs-js';

  // Server-side code using the JavaScript SDK
  const elevenlabs = new ElevenLabsClient({ apiKey: 'your-api-key' });
  async function getSignedUrl() {
    try {
      const response = await elevenlabs.conversationalAi.conversations.getSignedUrl({
        agentId: 'your-agent-id',
      });

      return response.signed_url;
    } catch (error) {
      console.error('Error getting signed URL:', error);
      throw error;
    }
  }
  ```

  ```bash
  curl -X GET "https://api.elevenlabs.io/v1/convai/conversation/get-signed-url?agent_id=your-agent-id" \
  -H "xi-api-key: your-api-key"
  ```
</CodeBlocks>

The curl response has the following format:

```json
{
  "signed_url": "wss://api.elevenlabs.io/v1/convai/conversation?agent_id=your-agent-id&conversation_signature=your-token"
}
```

### Connecting to your agent using a signed URL

Retrieve the server generated signed URL from the client and use the signed URL to connect to the websocket.

<CodeBlocks>
  ```python
  # Client-side code using the Python SDK
  from elevenlabs.conversational_ai.conversation import (
      Conversation,
      AudioInterface,
      ClientTools,
      ConversationInitiationData
  )
  import os
  from elevenlabs.client import ElevenLabs
  api_key = os.getenv("ELEVENLABS_API_KEY")

  elevenlabs = ElevenLabs(api_key=api_key)

  conversation = Conversation(
    client=elevenlabs,
    agent_id=os.getenv("AGENT_ID"),
    requires_auth=True,
    audio_interface=AudioInterface(),
    config=ConversationInitiationData()
  )

  async def start_conversation():
    try:
      signed_url = await get_signed_url()
      conversation = Conversation(
        client=elevenlabs,
        url=signed_url,
      )

      conversation.start_session()
    except Exception as error:
      print(f"Failed to start conversation: {error}")

  ```

  ```javascript
  // Client-side code using the JavaScript SDK
  import { Conversation } from '@elevenlabs/client';

  async function startConversation() {
    try {
      const signedUrl = await getSignedUrl();
      const conversation = await Conversation.startSession({
        signedUrl,
      });

      return conversation;
    } catch (error) {
      console.error('Failed to start conversation:', error);
      throw error;
    }
  }
  ```
</CodeBlocks>

### Signed URL expiration

Signed URLs are valid for 15 minutes. The conversation session can last longer, but the conversation must be initiated within the 15 minute window.


## Using allowlists

Allowlists provide a way to restrict access to your conversational agents based on the origin domain. This ensures that only requests from approved domains can connect to your agent.

### How allowlists work

1. You configure a list of approved hostnames for your agent.
2. When a client attempts to connect, ElevenLabs checks if the request's origin matches an allowed hostname.
3. If the origin is on the allowlist, the connection is permitted; otherwise, it's rejected.

### Configuring allowlists

Allowlists are configured as part of your agent's authentication settings. You can specify up to 10 unique hostnames that are allowed to connect to your agent.

### Example: setting up an allowlist

<CodeBlocks>
  ```python
  from elevenlabs.client import ElevenLabs
  import os
  from elevenlabs.types import *

  api_key = os.getenv("ELEVENLABS_API_KEY")
  elevenlabs = ElevenLabs(api_key=api_key)

  agent = elevenlabs.conversational_ai.agents.create(
    conversation_config=ConversationalConfig(
      agent=AgentConfig(
        first_message="Hi. I'm an authenticated agent.",
      )
    ),
    platform_settings=AgentPlatformSettingsRequestModel(
    auth=AuthSettings(
      enable_auth=False,
      allowlist=[
        AllowlistItem(hostname="example.com"),
        AllowlistItem(hostname="app.example.com"),
        AllowlistItem(hostname="localhost:3000")
        ]
      )
    )
  )
  ```

  ```javascript
  async function createAuthenticatedAgent(client) {
    try {
      const agent = await elevenlabs.conversationalAi.agents.create({
        conversationConfig: {
          agent: {
            firstMessage: "Hi. I'm an authenticated agent.",
          },
        },
        platformSettings: {
          auth: {
            enableAuth: false,
            allowlist: [
              { hostname: 'example.com' },
              { hostname: 'app.example.com' },
              { hostname: 'localhost:3000' },
            ],
          },
        },
      });

      return agent;
    } catch (error) {
      console.error('Error creating agent:', error);
      throw error;
    }
  }
  ```
</CodeBlocks>


## Combining authentication methods

For maximum security, you can combine both authentication methods:

1. Use `enable_auth` to require signed URLs.
2. Configure an allowlist to restrict which domains can request those signed URLs.

This creates a two-layer authentication system where clients must:

* Connect from an approved domain
* Possess a valid signed URL

<CodeBlocks>
  ```python
  from elevenlabs.client import ElevenLabs
  import os
  from elevenlabs.types import *
  api_key = os.getenv("ELEVENLABS_API_KEY")
  elevenlabs = ElevenLabs(api_key=api_key)
  agent = elevenlabs.conversational_ai.agents.create(
    conversation_config=ConversationalConfig(
      agent=AgentConfig(
        first_message="Hi. I'm an authenticated agent that can only be called from certain domains.",
      )
    ),
  platform_settings=AgentPlatformSettingsRequestModel(
    auth=AuthSettings(
      enable_auth=True,
      allowlist=[
        AllowlistItem(hostname="example.com"),
        AllowlistItem(hostname="app.example.com"),
        AllowlistItem(hostname="localhost:3000")
      ]
    )
  )
  ```

  ```javascript
  async function createAuthenticatedAgent(elevenlabs) {
    try {
      const agent = await elevenlabs.conversationalAi.agents.create({
        conversationConfig: {
          agent: {
            firstMessage: "Hi. I'm an authenticated agent.",
          },
        },
        platformSettings: {
          auth: {
            enableAuth: true,
            allowlist: [
              { hostname: 'example.com' },
              { hostname: 'app.example.com' },
              { hostname: 'localhost:3000' },
            ],
          },
        },
      });

      return agent;
    } catch (error) {
      console.error('Error creating agent:', error);
      throw error;
    }
  }
  ```
</CodeBlocks>


## FAQ

<AccordionGroup>
  <Accordion title="Can I use the same signed URL for multiple users?">
    This is possible but we recommend generating a new signed URL for each user session.
  </Accordion>

  <Accordion title="What happens if the signed URL expires during a conversation?">
    If the signed URL expires (after 15 minutes), any WebSocket connection created with that signed
    url will **not** be closed, but trying to create a new connection with that signed URL will
    fail.
  </Accordion>

  <Accordion title="Can I restrict access to specific users?">
    The signed URL mechanism only verifies that the request came from an authorized source. To
    restrict access to specific users, implement user authentication in your application before
    requesting the signed URL.
  </Accordion>

  <Accordion title="Is there a limit to how many signed URLs I can generate?">
    There is no specific limit on the number of signed URLs you can generate.
  </Accordion>

  <Accordion title="How do allowlists handle subdomains?">
    Allowlists perform exact matching on hostnames. If you want to allow both a domain and its
    subdomains, you need to add each one separately (e.g., "example.com" and "app.example.com").
  </Accordion>

  <Accordion title="Do I need to use both authentication methods?">
    No, you can use either signed URLs or allowlists independently based on your security
    requirements. For highest security, we recommend using both.
  </Accordion>

  <Accordion title="What other security measures should I implement?">
    Beyond signed URLs and allowlists, consider implementing:

    * User authentication before requesting signed URLs
    * Rate limiting on API requests
    * Usage monitoring for suspicious patterns
    * Proper error handling for auth failures
  </Accordion>
</AccordionGroup>



# Integrate

> Deploy your agents across web, mobile, and telephony platforms.

The Integrate section provides everything you need to connect your agents to your users, whether through web widgets, mobile apps, phone systems, or custom integrations.

<Frame background="subtle">
  <img src="file:26fc8805-072c-4da9-893d-a09195b0dc3e" alt="Integration options" />
</Frame>

### Connect and deploy

| Goal                        | Guide                                                                               | Description                                                        |
| --------------------------- | ----------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| Build with React components | [ElevenLabs UI](https://ui.elevenlabs.io)                                           | Pre-built components library for audio & agent apps (shadcn-based) |
| Embed widget in website     | [Widget](/docs/agents-platform/customization/widget)                                | Add a customizable web widget to any website                       |
| Build React web apps        | [React SDK](/docs/agents-platform/libraries/react)                                  | Voice-enabled React hooks and components                           |
| Build iOS apps              | [Swift SDK](/docs/agents-platform/libraries/swift)                                  | Native iOS SDK for voice agents                                    |
| Build Android apps          | [Kotlin SDK](/docs/agents-platform/libraries/kotlin)                                | Native Android SDK for voice agents                                |
| Build React Native apps     | [React Native SDK](/docs/agents-platform/libraries/react-native)                    | Cross-platform iOS and Android with React Native                   |
| Connect via SIP trunk       | [SIP trunk](/docs/agents-platform/phone-numbers/sip-trunking)                       | Integrate with existing telephony infrastructure                   |
| Make batch outbound calls   | [Batch calls](/docs/agents-platform/phone-numbers/batch-calls)                      | Trigger multiple calls programmatically                            |
| Use Twilio integration      | [Twilio](/docs/agents-platform/phone-numbers/twilio-integration/native-integration) | Native Twilio integration for phone calls                          |
| Build custom integrations   | [WebSocket API](/docs/agents-platform/libraries/websocket)                          | Low-level WebSocket protocol for custom implementations            |
| Receive real-time events    | [Events](/docs/agents-platform/customization/events)                                | Subscribe to conversation events and updates                       |


## Demo

This is a Next.js component from [ElevenLabs UI](https://ui.elevenlabs.io/blocks#voice-chat-01). View the source code to integrate it into your application.

<iframe src="https://ui.elevenlabs.io/view/voice-chat-01" width="100%" height="600" allow="microphone; autoplay" />


## Next steps

<CardGroup cols={2}>
  <Card title="Widget" href="/docs/agents-platform/customization/widget">
    Add a web widget to your site
  </Card>

  <Card title="React SDK" href="/docs/agents-platform/libraries/react">
    Build with React components
  </Card>

  <Card title="Twilio" href="/docs/agents-platform/phone-numbers/twilio-integration/native-integration">
    Deploy over phone
  </Card>

  <Card title="WebSocket API" href="/docs/agents-platform/libraries/websocket">
    Build custom integrations
  </Card>

  <Card title="ElevenLabs UI" href="https://ui.elevenlabs.io">
    Pre-built React components
  </Card>
</CardGroup>



# Widget customization

> Learn how to customize the widget appearance to match your brand, and personalize the agent's behavior from html.

<iframe width="100%" height="400" src="https://www.youtube-nocookie.com/embed/XweA70b45Ws?rel=0&autoplay=0" title="YouTube video player" frameborder="0" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen />

**Widgets** enable instant integration of Agents Platform into any website. You can either customize your widget through the UI or through our type-safe [Agents Platform SDKs](/docs/agents-platform/libraries) for complete control over styling and behavior. The SDK overrides take priority over UI customization.
Our widget is multimodal and able to process both text and audio.

<Frame caption="Multimodal conversational agents " background="subtle">
  <iframe width="100%" height="400" src="https://www.youtube.com/embed/TyPbeheubcs" title="Multimodal conversational agents" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />
</Frame>


## Modality configuration

The widget supports flexible input modes to match your use case. Configure these options in the [dashboard](https://elevenlabs.io/app/agents/dashboard) **Widget** tab under the **Interface** section.

<Note>
  Multimodality is fully supported in our client SDKs, see more
  [here](/docs/agents-platform/libraries/).
</Note>

<Frame background="subtle">
  ![Widget interface options](file:db3108ac-f4ff-4fed-89b3-1ae69b7b2479)
</Frame>

**Available modes:**

* **Voice only** (default): Users interact through speech only.
* **Voice + text**: Users can switch between voice and text input during conversations.
* **Chat Mode**: Conversations start in chat (text-only) mode without voice capabilities when initiated with a text message.

For more information on using chat (text-only) mode via our SDKs, see our [chat mode guide](/docs/agents-platform/guides/chat-mode).

<Note>
  The widget defaults to voice-only mode. Enable the text input toggle to allow multimodal
  interactions, or enable text-only mode support for purely text-based conversations when initiated
  via text.
</Note>


## Embedding the widget

<Note>
  Widgets currently require public agents with authentication disabled. Ensure this is disabled in
  the **Advanced** tab of your agent settings.
</Note>

Add this code snippet to your website's `<body>` section. Place it in your main `index.html` file for site-wide availability:

<CodeBlocks>
  ```html title="Widget embed code"
  <elevenlabs-convai agent-id="<replace-with-your-agent-id>"></elevenlabs-convai>
  <script
    src="https://unpkg.com/@elevenlabs/convai-widget-embed"
    async
    type="text/javascript"
  ></script>
  ```
</CodeBlocks>

<Info>
  For enhanced security, define allowed domains in your agent's **Allowlist** (located in the
  **Security** tab). This restricts access to specified hosts only.
</Info>


## Widget attributes

This basic embed code will display the widget with the default configuration defined in the agent's dashboard.
The widget supports various HTML attributes for further customization:

<AccordionGroup>
  <Accordion title="Core configuration">
    ```html
    <elevenlabs-convai
      agent-id="agent_id"              // Required: Your agent ID
      signed-url="signed_url"          // Alternative to agent-id
      server-location="us"             // Optional: "us" or default
      variant="expanded"               // Optional: Widget display mode
    ></elevenlabs-convai>
    ```
  </Accordion>

  <Accordion title="Visual customization">
    ```html
    <elevenlabs-convai
      avatar-image-url="https://..." // Optional: Custom avatar image
      avatar-orb-color-1="#6DB035" // Optional: Orb gradient color 1
      avatar-orb-color-2="#F5CABB" // Optional: Orb gradient color 2
    ></elevenlabs-convai>
    ```
  </Accordion>

  <Accordion title="Text customization">
    ```html
    <elevenlabs-convai
      action-text="Need assistance?"         // Optional: CTA button text
      start-call-text="Begin conversation"   // Optional: Start call button
      end-call-text="End call"              // Optional: End call button
      expand-text="Open chat"               // Optional: Expand widget text
      listening-text="Listening..."         // Optional: Listening state
      speaking-text="Assistant speaking"     // Optional: Speaking state
    ></elevenlabs-convai>
    ```
  </Accordion>
</AccordionGroup>


## Runtime configuration

Two more html attributes can be used to customize the agent's behavior at runtime. These two features can be used together, separately, or not at all

### Dynamic variables

Dynamic variables allow you to inject runtime values into your agent's messages, system prompts, and tools.

```html
<elevenlabs-convai
  agent-id="your-agent-id"
  dynamic-variables='{"user_name": "John", "account_type": "premium"}'
></elevenlabs-convai>
```

All dynamic variables that the agent requires must be passed in the widget.

<Info>
  See more in our [dynamic variables
  guide](/docs/agents-platform/customization/personalization/dynamic-variables).
</Info>

### Overrides

Overrides enable complete customization of your agent's behavior at runtime:

```html
<elevenlabs-convai
  agent-id="your-agent-id"
  override-language="es"
  override-prompt="Custom system prompt for this user"
  override-first-message="Hi! How can I help you today?"
  override-voice-id="axXgspJ2msm3clMCkdW3"
></elevenlabs-convai>
```

Overrides can be enabled for specific fields, and are entirely optional.

<Info>
  See more in our [overrides guide](/docs/agents-platform/customization/personalization/overrides).
</Info>


## Visual customization

Customize the widget's appearance, text content, language selection, and more in the [dashboard](https://elevenlabs.io/app/agents/dashboard) **Widget** tab.

<Frame background="subtle">
  ![Widget customization](file:3ebd441d-a00a-4668-95f5-fb63e95c27f4)
</Frame>

<Tabs>
  <Tab title="Appearance">
    Customize the widget colors and shapes to match your brand identity.

    <Frame background="subtle">
      ![Widget appearance](file:ef0aff78-c848-4dd9-923d-20435ad0084e)
    </Frame>
  </Tab>

  <Tab title="Feedback">
    Gather user insights to improve agent performance. This can be used to fine-tune your agent's knowledge-base & system prompt.

    <Frame background="subtle">
      ![Widget feedback](file:b69249d8-bc77-4de7-b7c5-fae59b544f13)
    </Frame>

    **Collection modes**

    * <strong>None</strong>: Disable feedback collection entirely.
    * <strong>During conversation</strong>: Support real-time feedback during conversations. Additionnal metadata such as the agent response that prompted the feedback will be collected to help further identify gaps.
    * <strong>After conversation</strong>: Display a single feedback prompt after the conversation.

    <Note>
      Send feedback programmatically via the [API](/docs/agents-platform/api-reference/conversations/create) when using custom SDK implementations.
    </Note>
  </Tab>

  <Tab title="Avatar">
    Configure the voice orb or provide your own avatar.

    <Frame background="subtle">
      ![Widget orb customization](file:2dc7e66b-a939-4d2d-b36a-0380749a760a)
    </Frame>

    **Available options**

    * <strong>Orb</strong>: Choose two gradient colors (e.g., #6DB035 & #F5CABB).
    * <strong>Link/image</strong>: Use a custom avatar image.
  </Tab>

  <Tab title="Display text">
    Customize all displayed widget text elements, for example to modify button labels.

    <Frame background="subtle">
      ![Widget text contents](file:a629b860-469a-443b-ac5a-ce1ddd954d72)
    </Frame>
  </Tab>

  <Tab title="Terms">
    Display custom terms and conditions before the conversation.

    <Frame background="subtle">
      ![Terms setup](file:4db605f4-9081-4375-bfbf-058f36dcd264)
    </Frame>

    **Available options**

    * <strong>Terms content</strong>: Use Markdown to format your policy text.
    * <strong>Local storage key</strong>: A key (e.g., "terms\_accepted") to avoid prompting returning users.

    **Usage**

    The terms are displayed to users in a modal before starting the call:

    <Frame background="subtle">
      ![Terms display](file:865d8f33-6e23-4e42-8205-1ccd108ecec0)
    </Frame>

    The terms can be written in Markdown, allowing you to:

    * Add links to external policies
    * Format text with headers and lists
    * Include emphasis and styling

    For more help with Markdown, see the [CommonMark help guide](https://commonmark.org/help/).

    <Info>
      Once accepted, the status is stored locally and the user won't be prompted again on subsequent
      visits.
    </Info>
  </Tab>

  <Tab title="Language">
    Enable multi-language support in the widget.

    ![Widget language](file:fbb049e5-6bc4-4265-a097-dd7a26740695)

    <Note>
      To enable language selection, you must first [add additional
      languages](/docs/agents-platform/customization/language) to your agent.
    </Note>
  </Tab>

  <Tab title="Muting">
    Allow users to mute their audio in the widget.

    ![Widget's mute button](file:25503957-6f19-4f4c-8948-3fd70f8d394f)

    To add the mute button please enable this in the `interface` card of the agent's `widget`
    settings.

    ![Widget's mute button](file:451489a1-5e59-4c34-84c3-89fa95ce7c33)
  </Tab>

  <Tab title="Shareable page">
    Customize your public widget landing page (shareable link).

    <Frame background="subtle">
      ![Widget shareable page](file:1d7efb44-c2c5-4f2d-beb0-24a8eeb077c7)
    </Frame>

    **Available options**

    * <strong>Description</strong>: Provide a short paragraph explaining the purpose of the call.
  </Tab>
</Tabs>

***


## Advanced implementation

<Note>
  For more advanced customization, you should use the type-safe [Agents Platform
  SDKs](/docs/agents-platform/libraries) with a Next.js, React, or Python application.
</Note>

### Client Tools

Client tools allow you to extend the functionality of the widget by adding event listeners. This enables the widget to perform actions such as:

* Redirecting the user to a specific page
* Sending an email to your support team
* Redirecting the user to an external URL

To see examples of these tools in action, start a call with the agent in the bottom right corner of this page. The [source code is available on GitHub](https://github.com/elevenlabs/elevenlabs-docs/blob/main/fern/assets/scripts/widget.js) for reference.

#### Creating a Client Tool

To create your first client tool, follow the [client tools guide](/docs/agents-platform/customization/tools/client-tools).

<Accordion title="Example: Creating the `redirectToExternalURL` Tool">
  <Frame background="subtle">
    ![Client tool configuration](file:fcc726c4-6ec0-4c78-aac8-dd6e28d69dd7)
  </Frame>
</Accordion>

#### Example Implementation

Below is an example of how to handle the `redirectToExternalURL` tool triggered by the widget in your JavaScript code:

<CodeBlocks>
  ```javascript title="index.js"
  document.addEventListener('DOMContentLoaded', () => {
    const widget = document.querySelector('elevenlabs-convai');

    if (widget) {
      // Listen for the widget's "call" event to trigger client-side tools
      widget.addEventListener('elevenlabs-convai:call', (event) => {
        event.detail.config.clientTools = {
          // Note: To use this example, the client tool called "redirectToExternalURL" (case-sensitive) must have been created with the configuration defined above.
          redirectToExternalURL: ({ url }) => {
            window.open(url, '_blank', 'noopener,noreferrer');
          },
        };
      });
    }
  });
  ```
</CodeBlocks>

<Info>
  Explore our type-safe [SDKs](/docs/agents-platform/libraries) for React, Next.js, and Python
  implementations.
</Info>



# SIP trunking

> Connect your existing phone system with ElevenLabs Agents using SIP trunking


## Overview

SIP (Session Initiation Protocol) trunking allows you to connect your existing telephony infrastructure directly to ElevenLabs Agents.
This integration enables all customers to use their existing phone systems while leveraging ElevenLabs' advanced voice AI capabilities.

With SIP trunking, you can:

* Connect your Private Branch Exchange (PBX) or SIP-enabled phone system to ElevenLabs' voice AI platform
* Route calls to AI agents without changing your existing phone infrastructure
* Handle both inbound and outbound calls
* Leverage encrypted TLS transport and media encryption for enhanced security

<Note>
  **Static IP SIP Servers**

  ElevenLabs offers SIP servers with static IP addresses for enterprise clients who require IP allowlisting for their security policies.

  Our static IP infrastructure uses a /24 IP address block containing 256 addresses distributed across multiple regions (US, EU, and India). You must allowlist the entire /24 block in your firewall configuration.

  For the default (US/International) environment, use `sip-static.rtc.elevenlabs.io` as your SIP endpoint. For isolated regions, use `sip-static.rtc.in.residency.elevenlabs.io` or `sip-static.rtc.eu.residency.elevenlabs.io` as needed. When using these endpoints, all traffic will originate exclusively from within that region. Specific whitelisting per-region is not available.

  This feature is available for Enterprise accounts and can also be enabled during Enterprise trials for testing purposes. To request access, [open a support ticket](https://help.elevenlabs.io/hc/en-us/requests/new?ticket_form_id=13145996177937) or contact your account representative. For more information, [contact sales](https://elevenlabs.io/contact-sales?utm_source=docs\&utm_medium=referral\&utm_campaign=static_ip_sip).
</Note>


## How SIP trunking works

SIP trunking establishes a direct connection between your telephony infrastructure and the ElevenLabs platform:

1. **Inbound calls**: Calls from your SIP trunk are routed to the ElevenLabs platform using your configured SIP INVITE address.
2. **Outbound calls**: Calls initiated by ElevenLabs are routed to your SIP trunk using your configured hostname, enabling your agents to make outgoing calls.
3. **Authentication**: Connection security for the signaling is maintained through either digest authentication (username/password) or Access Control List (ACL) authentication based on the signaling source IP.
4. **Signaling and Media**: The initial call setup (signaling) supports multiple transport protocols including TLS for encrypted communication. Once the call is established, the actual audio data (RTP stream) can be encrypted based on your media encryption settings.


## Making calls to ElevenLabs SIP trunk

When initiating calls to the ElevenLabs platform, you need to use the proper SIP URI format.

The ElevenLabs SIP trunk URI is:

```
sip:sip.rtc.elevenlabs.io:5060;transport=tcp
```

To make a call, construct a complete SIP URI that includes an identifier:

```
sip:+19991234567@sip.rtc.elevenlabs.io:5060
```

Where:

* `+19991234567` is the identifier (typically a phone number in E.164 format)
* The identifier can also be any string value, such as `1000` or `john`

<Warning>
  **Common Mistake**: Do not initiate calls directly to `sip@sip.rtc.elevenlabs.io:5060` without an
  identifier. The SIP URI must include a phone number or identifier after the `sip:` prefix and
  before the `@` symbol.
</Warning>

<Info>
  **SIP URI Format**: A [SIP URI](https://en.wikipedia.org/wiki/SIP_URI_scheme) follows the format
  `sip:identifier@domain:port` where the identifier is required to route the call properly.
</Info>


## Requirements

Before setting up SIP trunking, ensure you have:

1. A SIP-compatible PBX or telephony system
2. Phone numbers that you want to connect to ElevenLabs
3. Administrator access to your SIP trunk configuration
4. Appropriate firewall settings to allow SIP traffic
5. **TLS Support**: For enhanced security, ensure your SIP trunk provider supports TLS transport
6. **Audio codec compatibility**:
   Your system must support either G711 or G722 audio codecs or be capable of resampling audio on your end. ElevenLabs' SIP deployment outputs and receives audio at this sample rate. This is independent of any audio format configured on the agent for direct websocket connections.


## Setting up SIP trunking

<Steps>
  <Step title="Navigate to Phone Numbers">
    Go to the [Phone Numbers section](https://elevenlabs.io/app/agents/phone-numbers) in the ElevenLabs Agents dashboard.
  </Step>

  <Step title="Import SIP Trunk">
    Click on "Import a phone number from SIP trunk" button to open the configuration dialog.

    <Frame background="subtle">
      <img src="file:0b9932b1-379e-4a02-a7cd-1530d44d9625" alt="Select SIP trunk option" />
    </Frame>

    <Frame background="subtle">
      <img src="file:afae9a55-a284-4256-a9ed-cbbc5e9556f7" alt="SIP trunk configuration dialog" />
    </Frame>
  </Step>

  <Step title="Enter basic configuration">
    Complete the basic configuration with the following information:

    * **Label**: A descriptive name for the phone number
    * **Phone Number**: The E.164 formatted phone number to connect (e.g., +15551234567)

    <Frame background="subtle">
      <img src="file:8726df0e-82fe-4efb-bc57-572bf3367228" alt="SIP trunk basic configuration" />
    </Frame>
  </Step>

  <Step title="Configure transport and encryption">
    Configure the transport protocol and media encryption settings for enhanced security:

    * **Transport Type**: Select the transport protocol for SIP signaling:
      * **TCP**: Standard TCP transport
      * **TLS**: Encrypted TLS transport for enhanced security
    * **Media Encryption**: Configure encryption for RTP media streams:
      * **Disabled**: No media encryption
      * **Allowed**: Permits encrypted media streams
      * **Required**: Enforces encrypted media streams

    <Frame background="subtle">
      <img src="file:f06cd2f5-f0f7-47a4-8c7f-c48ec9dab865" alt="Select TLS or TCP transport" />
    </Frame>

    <Frame background="subtle">
      <img src="file:b10f4294-8fe6-4d74-b2a1-32dedaebe519" alt="Select media encryption setting" />
    </Frame>

    <Tip>
      **Security Best Practice**: Use TLS transport with Required media encryption for maximum security. This ensures both signaling and media are encrypted end-to-end.
    </Tip>
  </Step>

  <Step title="Configure outbound settings">
    Configure where ElevenLabs should send calls for your phone number:

    * **Address**: Hostname or IP address where the SIP INVITE is sent (e.g., `sip.telnyx.com`). This should be a hostname or IP address only, not a full SIP URI.
    * **Transport Type**: Select the transport protocol for SIP signaling:
      * **TCP**: Standard TCP transport
      * **TLS**: Encrypted TLS transport for enhanced security
    * **Media Encryption**: Configure encryption for RTP media streams:
      * **Disabled**: No media encryption
      * **Allowed**: Permits encrypted media streams
      * **Required**: Enforces encrypted media streams

    <Frame background="subtle">
      <img src="file:8fbea4f4-175a-4b4d-a3cb-90d16d6b859d" alt="SIP trunk outbound configuration" />
    </Frame>

    <Tip>
      **Security Best Practice**: Use TLS transport with Required media encryption for maximum security. This ensures both signaling and media are encrypted end-to-end.
    </Tip>

    <Note>
      The **Address** field specifies where ElevenLabs will send outbound calls from your AI agents. Enter only the hostname or IP address without the `sip:` protocol prefix.
    </Note>
  </Step>

  <Step title="Add custom headers (optional)">
    If your SIP trunk provider requires specific headers for call routing or identification:

    * Click "Add Header" to add custom SIP headers
    * Enter the header name and value as required by your provider
    * You can add multiple headers as needed

    Custom headers are included with all outbound calls and can be used for:

    * Call routing and identification
    * Billing and tracking purposes
    * Provider-specific requirements
  </Step>

  <Step title="Configure authentication (optional)">
    Provide digest authentication credentials if required by your SIP trunk provider:

    * **SIP Trunk Username**: Username for SIP digest authentication
    * **SIP Trunk Password**: Password for SIP digest authentication

    If left empty, Access Control List (ACL) authentication will be used, which requires you to allowlist ElevenLabs IP addresses in your provider's settings.

    <Info>
      **Authentication Methods**:

      * **Digest Authentication**: Uses username/password credentials for secure authentication (recommended)
      * **ACL Authentication**: Uses IP address allowlisting for access control

      **Digest Authentication is strongly recommended** as it provides better security without relying on IP allowlisting, which can be complex to manage with dynamic IP addresses.
    </Info>
  </Step>

  <Step title="Complete Setup">
    Click "Import" to finalize the configuration.
  </Step>
</Steps>


## Client Data and Personalization

To ensure proper forwarding and traceability of call metadata, include the following custom SIP headers in your webhook payload and SIP INVITE request:

* **X-CALL-ID**: Unique identifier for the call
* **X-CALLER-ID**: Identifier for the calling party

These headers enable the system to associate call metadata with the conversation and provide context for personalization.

### Fallback Header Support

If the standard headers above are not present, the system will automatically look for the Twilio-specific SIP header:

* **sip.twilio.callSid**: Twilio's unique call identifier

This fallback ensures compatibility with Twilio's Elastic SIP Trunking without requiring configuration changes.

### Custom Provider Headers

If you're using a SIP provider other than Twilio and your platform uses different headers for call or caller identification please contact our support team.

### Processing Flow

Once the relevant metadata is received through any of the supported headers, the `caller_id` and/or `call_id` are available in the [pre-call webhook](/docs/agents-platform/customization/personalization/twilio-personalization#how-it-works) and as [system dynamic variables](/docs/agents-platform/customization/personalization/dynamic-variables#system-dynamic-variables).


## Assigning Agents to Phone Numbers

After importing your SIP trunk phone number, you can assign it to a ElevenLabs agent:

1. Go to the Phone Numbers section in the Agents Platform dashboard
2. Select your imported SIP trunk phone number
3. Click "Assign Agent"
4. Select the agent you want to handle calls to this number


## Troubleshooting

<AccordionGroup>
  <Accordion title="Connection Issues">
    If you're experiencing connection problems:

    1. Verify your SIP trunk configuration on both the ElevenLabs side and your provider side
    2. Check that your firewall allows SIP signaling traffic on the configured transport protocol and port (5060 for TCP, 5061 for TLS) and ensure there is no whitelisting applied
    3. Confirm that your address hostname is correctly formatted and accessible
    4. Test with and without digest authentication credentials
    5. If using TLS transport, ensure your provider's TLS certificates are valid and properly configured
    6. Try different transport types (TCP only, as UDP is not currently available) to isolate TLS-specific issues

    **Important Network Architecture Information:**

    * ElevenLabs runs multiple SIP servers behind the load balancer `sip.rtc.elevenlabs.io`
    * The SIP servers communicate directly with your SIP server, bypassing the load balancer
    * SIP requests may come from different IP addresses due to our distributed infrastructure
    * If your security policy requires whitelisting inbound traffic, please contact our support team for assistance.
  </Accordion>

  <Accordion title="Authentication Failures">
    If calls are failing due to authentication issues:

    1. Double-check your SIP trunk username and password if using digest authentication
    2. Check your SIP trunk provider's logs for specific authentication error messages
    3. Verify that custom headers, if configured, match your provider's requirements
    4. Test with simplified configurations (no custom headers) to isolate authentication issues
  </Accordion>

  <Accordion title="TLS and Encryption Issues">
    If you're experiencing issues with TLS transport or media encryption:

    1. Verify that your SIP trunk provider supports TLS transport on port 5061
    2. Check certificate validity, expiration dates, and trust chains
    3. Ensure your provider supports SRTP media encryption if using "Required" media encryption
    4. Test with "Allowed" media encryption before using "Required" to isolate encryption issues
    5. Try TCP transport to isolate TLS-specific problems (UDP is not currently available)
    6. Contact your SIP trunk provider to confirm TLS and SRTP support
  </Accordion>

  <Accordion title="Custom Headers Issues">
    If you're having problems with custom headers:

    1. Verify the exact header names and values required by your provider
    2. Check for case sensitivity in header names
    3. Ensure header values don't contain special characters that need escaping
    4. Test without custom headers first, then add them incrementally
    5. Review your provider's documentation for supported custom headers
  </Accordion>

  <Accordion title="No Audio or One-Way Audio">
    If the call connects but there's no audio or audio only flows one way:

    1. Verify that your firewall allows UDP traffic for the RTP media stream (typically ports 10000-60000)
    2. Since RTP uses dynamic IP addresses, ensure firewall rules are not restricted to specific static IPs
    3. Check for Network Address Translation (NAT) issues that might be blocking the RTP stream
    4. If using "Required" media encryption, ensure both endpoints support SRTP
    5. Test with "Disabled" media encryption to isolate encryption-related audio issues
  </Accordion>

  <Accordion title="Audio Quality Issues">
    If you experience poor audio quality:

    1. Ensure your network has sufficient bandwidth (at least 100 Kbps per call) and low latency/jitter for UDP traffic
    2. Check for network congestion or packet loss, particularly on the UDP path
    3. Verify codec settings match on both ends
    4. If using media encryption, ensure both endpoints efficiently handle SRTP processing
    5. Test with different media encryption settings to isolate quality issues
  </Accordion>
</AccordionGroup>


## Limitations and Considerations

* Support for multiple concurrent calls depends on your subscription tier
* Call recording and analytics features are available but may require additional configuration
* Outbound calling capabilities may be limited by your SIP trunk provider
* **TLS Support**: Ensure your SIP trunk provider supports TLS 1.2 or higher for encrypted transport
* **Media Encryption**: SRTP support varies by provider; verify compatibility before requiring encryption
* **Audio format**: ElevenLabs' SIP deployment outputs and receives audio in G711 8kHz or G722 16kHz audio codecs. This is independent of any audio format configured on the agent for direct websocket connections. Your SIP trunk system must either support this format natively or perform resampling to match your system's requirements


## FAQ

<AccordionGroup>
  <Accordion title="Can I use my existing phone numbers with ElevenLabs?">
    Yes, SIP trunking allows you to connect your existing phone numbers directly to ElevenLabs'
    Agents Platform without porting them.
  </Accordion>

  <Accordion title="What SIP trunk providers are compatible with ElevenLabs?">
    ElevenLabs is compatible with most standard SIP trunk providers including Twilio, Vonage,
    RingCentral, Sinch, Infobip, Telnyx, Exotel, Plivo, Bandwidth, and others that support SIP
    protocol standards. TLS transport and SRTP media encryption are supported for enhanced security.
  </Accordion>

  <Accordion title="Should I use TLS transport for better security?">
    Yes, TLS transport is highly recommended for production environments. It provides encrypted SIP
    signaling which enhances security for your calls. Combined with required media encryption, it
    ensures comprehensive protection of your communications. Always verify your SIP trunk provider
    supports TLS before enabling it.
  </Accordion>

  <Accordion title="What's the difference between transport types?">
    * **TCP**: Reliable but unencrypted signaling - **TLS**: Encrypted and reliable signaling
      (recommended for production)

    <Note>
      UDP transport is not currently available. For security-critical applications, always use TLS
      transport.
    </Note>
  </Accordion>

  <Accordion title="What are custom headers used for?">
    Custom SIP headers allow you to include provider-specific information with outbound calls. Common
    uses include call routing, billing codes, caller identification, and meeting specific provider
    requirements.
  </Accordion>

  <Accordion title="How many concurrent calls are supported?">
    The number of concurrent calls depends on your subscription plan. Enterprise plans typically allow
    for higher volumes of concurrent calls.
  </Accordion>

  <Accordion title="Can I route calls conditionally to different agents?">
    Yes, you can use your existing PBX system's routing rules to direct calls to different phone
    numbers, each connected to different ElevenLabs agents.
  </Accordion>

  <Accordion title="Do I need to match the leading + format when importing phone numbers?">
    Yes, the phone number format must be consistent between your SIP URI and your imported phone number configuration. If you call the SIP URI with a leading + (e.g., `sip:+19991234567@sip.rtc.elevenlabs.io:5060`), you must also import the phone number with the leading + (e.g., `+19991234567`). Similarly, if you call without the leading +, import the phone number without it. Mismatched formats will prevent proper call routing.
  </Accordion>
</AccordionGroup>


## Next steps

* [Learn about creating ElevenLabs agents](/docs/agents-platform/quickstart)



---
**Navigation:** [← Previous](./12-language.md) | [Index](./index.md) | [Next →](./14-batch-calling.md)
