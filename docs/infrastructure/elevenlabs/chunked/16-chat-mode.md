**Navigation:** [← Previous](./15-client-to-server-events.md) | [Index](./index.md) | [Next →](./17-salesforce.md)

# Chat Mode

> Configure your agent for text-only conversations with chat mode

<Info>
  Chat mode allows your agents to act as chat agents, ie to have text-only conversations without
  audio input/output. This is useful for building chat interfaces, testing agents, or when audio is
  not required.
</Info>


## Overview

There are two main ways to enable chat mode:

1. **Agent Configuration**: Configure your agent for text-only mode when creating it via the API
2. **Runtime Overrides**: Use SDK overrides to enforce text-only conversations programmatically

This guide covers both approaches and how to implement chat mode across different SDKs.


## Creating Text-Only Agents

You can configure an agent for text-only mode when creating it via the API. This sets the default behavior for all conversations with that agent.

<CodeBlocks>
  ```python
  from elevenlabs import ConversationalConfig, ConversationConfig, ElevenLabs

  client = ElevenLabs(
      api_key="YOUR_API_KEY",
  )

  # Create agent with text-only configuration
  agent = client.conversational_ai.agents.create(
      name="My Chat Agent",
      conversation_config=ConversationalConfig(
          conversation=ConversationConfig(
              text_only=True
          )
      ),
  )
  print(agent)
  ```

  ```javascript
  import { ElevenLabsClient } from '@elevenlabs/elevenlabs-js';

  const client = new ElevenLabsClient({ apiKey: 'YOUR_API_KEY' });

  // Create agent with text-only configuration
  const agent = await client.conversationalAi.agents.create({
    name: 'My Chat Agent',
    conversationConfig: {
      conversation: {
        textOnly: true,
      },
    },
  });

  console.log(agent);
  ```
</CodeBlocks>

<Info>
  For complete API reference and all available configuration options, see the [text only field in
  Create Agent API
  documentation](/docs/api-reference/agents/create#request.body.conversation_config.conversation.text_only).
</Info>

1. **Agent Configuration**: Configure your agent for text-only mode when creating it via the API
2. **Runtime Overrides**: Use SDK overrides to enforce text-only conversations programmatically

This guide covers both approaches and how to implement chat mode across different SDKs.


## Runtime Overrides for Text-Only Mode

To enable chat mode at runtime using overrides (rather than configuring at the agent level), you can use the `textOnly` override in your conversation configuration:

<CodeBlocks>
  ```python
  from elevenlabs.client import ElevenLabs
  from elevenlabs.conversational_ai.conversation import Conversation, ConversationInitiationData

  # Configure for text-only mode with proper structure
  conversation_override = {
      "conversation": {
          "text_only": True
      }
  }

  config = ConversationInitiationData(
      conversation_config_override=conversation_override
  )

  conversation = Conversation(
      elevenlabs,
      agent_id,
      requires_auth=bool(api_key),
      config=config,
      # Important: Ensure agent_response callback is set
      callback_agent_response=lambda response: print(f"Agent: {response}"),
      callback_user_transcript=lambda transcript: print(f"User: {transcript}"),
  )

  conversation.start_session()
  ```

  ```javascript
  const conversation = await Conversation.startSession({
    agentId: '<your-agent-id>',
    overrides: {
      conversation: {
        textOnly: true,
      },
    },
  });
  ```
</CodeBlocks>

This configuration ensures that:

* No audio input/output is used
* All communication happens through text messages
* The conversation operates in a chat-like interface mode


## Important Notes

<Warning>
  **Critical**: When using chat mode, you must ensure the `agent_response` event/callback is
  activated and properly configured. Without this, the agent's text responses will not be sent or
  displayed to the user.
</Warning>

<Info>
  **Security Overrides**: When using runtime overrides (not agent-level configuration), you must
  enable the conversation overrides in your agent's security settings. Navigate to your agent's
  **Security** tab and enable the appropriate overrides. For more details, see the [Overrides
  documentation](/docs/agents-platform/customization/personalization/overrides).
</Info>

### Key Requirements

1. **Agent Response Event**: Always configure the `agent_response` callback or event handler to receive and display the agent's text messages.

2. **Agent Configuration**: If your agent is specifically set to chat mode in the agent settings, it will automatically use text-only conversations without requiring the override.

3. **No Audio Interface**: When using text-only mode, you don't need to configure audio interfaces or request microphone permissions.

### Example: Handling Agent Responses

<CodeBlocks>
  ```python
  def handle_agent_response(response):
      """Critical handler for displaying agent messages"""
      print(f"Agent: {response}")  # Update your UI with the response
      update_chat_ui(response)

  config = ConversationInitiationData(
      conversation_config_override={"conversation": {"text_only": True}}
  )

  conversation = Conversation(
    elevenlabs,
    agent_id,
    config=config,
    callback_agent_response=handle_agent_response,
  )

  conversation.start_session()
  ```

  ```javascript
  const conversation = await Conversation.startSession({
    agentId: '<your-agent-id>',
    overrides: {
      conversation: {
        textOnly: true,
      },
    },
    // Critical: Handle agent responses
    onMessage: (message) => {
      if (message.type === 'agent_response') {
        console.log('Agent:', message.text);
        // Display in your UI
        displayAgentMessage(message.text);
      }
    },
  });
  ```
</CodeBlocks>


## Sending Text Messages

In chat mode, you'll need to send user messages programmatically instead of through audio:

<CodeBlocks>
  ```python
  # Send a text message to the agent
  conversation.send_user_message("Hello, how can you help me today?")
  ```

  ```javascript
  // Send a text message to the agent
  conversation.sendUserMessage({
    text: 'Hello, how can you help me today?',
  });
  ```
</CodeBlocks>


## Concurrency Benefits

Chat mode provides significant concurrency advantages over voice conversations:

* **Higher Limits**: Chat-only conversations have 25x higher concurrency limits than voice conversations
* **Separate Pool**: Text conversations use a dedicated concurrency pool, independent of voice conversation limits
* **Scalability**: Ideal for high-throughput applications like customer support, chatbots, or automated testing

| Plan       | Voice Concurrency | Chat-only Concurrency |
| ---------- | ----------------- | --------------------- |
| Free       | 4                 | 100                   |
| Starter    | 6                 | 150                   |
| Creator    | 10                | 250                   |
| Pro        | 20                | 500                   |
| Scale      | 30                | 750                   |
| Business   | 30                | 750                   |
| Enterprise | Elevated          | Elevated (25x)        |

<Note>
  During connection initiation, chat-only conversations are initially checked against your total
  concurrency limit during the handshake process, then transferred to the separate chat-only
  concurrency pool once the connection is established.
</Note>


## Use Cases

Chat mode is ideal for:

* **Chat Interfaces**: Building traditional chat UIs without voice
* **Testing**: Testing agent logic without audio dependencies
* **Accessibility**: Providing text-based alternatives for users
* **Silent Environments**: When audio input/output is not appropriate
* **Integration Testing**: Automated testing of agent conversations


## Troubleshooting

### Agent Not Responding

If the agent's responses are not appearing:

1. Verify the `agent_response` callback is properly configured
2. Check that the agent is configured for chat mode or the `textOnly` override is set
3. Ensure the WebSocket connection is established successfully


## Next Steps

* Learn about [customizing agent behavior](/docs/agents-platform/customization/llm)
* Explore [client events](/docs/agents-platform/customization/events/client-events) for advanced interactions
* See [authentication setup](/docs/agents-platform/customization/authentication) for secure conversations



# Burst pricing

> Optimize call capacity with burst concurrency to handle traffic spikes.


## Overview

Burst pricing allows your ElevenLabs agents to temporarily exceed your workspace's subscription concurrency limit during high-demand periods. When enabled, your agents can handle up to 3 times your normal concurrency limit, with excess calls charged at double the standard rate.

This feature helps prevent missed calls during traffic spikes while maintaining cost predictability for your regular usage patterns.


## How burst pricing works

When burst pricing is enabled for an agent:

1. **Normal capacity**: Calls within your subscription limit are charged at standard rates
2. **Burst capacity**: Additional calls (up to a concurrency of 3x your usual limit or 300, whichever is lower) are accepted but charged at 2x the normal rate
3. **Over-capacity rejection**: Calls exceeding the burst limit are rejected with an error

### Capacity calculations

| Subscription limit | Burst capacity | Maximum concurrent calls |
| ------------------ | -------------- | ------------------------ |
| 10 calls           | 30 calls       | 30 calls                 |
| 50 calls           | 150 calls      | 150 calls                |
| 100 calls          | 300 calls      | 300 calls                |
| 200 calls          | 300 calls      | 300 calls (capped)       |

<Note>
  For non-enterprise customers, the maximum burst currency can not go above 300.
</Note>


## Cost implications

Burst pricing follows a tiered charging model:

* **Within subscription limit**: Standard per-minute rates apply
* **Burst calls**: Charged at 2x the standard rate
* **Deprioritized processing**: Burst calls receive lower priority for speech-to-text and text-to-speech processing

### Example pricing scenario

For a workspace with a 20-call subscription limit:

* Calls 1-20: Standard rate (e.g., \$0.08/minute)
* Calls 21-60: Double rate (e.g., \$0.16/minute)
* Calls 61+: Rejected

<Warning>
  Burst calls are deprioritized and may experience higher latency for speech processing, similar to
  anonymous-tier requests.
</Warning>


## Configuration

Burst pricing is configured per agent in the call limits settings.

### Dashboard configuration

1. Navigate to your agent settings
2. Go to the **Call Limits** section
3. Enable the **Burst pricing** toggle
4. Save your agent configuration

### API configuration

Burst pricing can be configured via the API, as shown in the examples below

<CodeBlocks>
  ```python title="Python"
  from dotenv import load_dotenv
  from elevenlabs.client import ElevenLabs
  import os

  load_dotenv()

  elevenlabs = ElevenLabs(
      api_key=os.getenv("ELEVENLABS_API_KEY"),
  )

  # Update agent with burst pricing enabled
  response = elevenlabs.conversational_ai.agents.update(
      agent_id="your-agent-id",
      agent_config={
          "platform_settings": {
              "call_limits": {
                  "agent_concurrency_limit": -1,  # Use workspace limit
                  "daily_limit": 1000,
                  "bursting_enabled": True
              }
          }
      }
  )
  ```

  ```javascript title="JavaScript"
  import { ElevenLabsClient } from '@elevenlabs/elevenlabs-js';
  import 'dotenv/config';

  const elevenlabs = new ElevenLabsClient();

  // Configure agent with burst pricing enabled
  const updatedConfig = {
    platformSettings: {
      callLimits: {
        agentConcurrencyLimit: -1, // Use workspace limit
        dailyLimit: 1000,
        burstingEnabled: true,
      },
    },
  };

  // Update the agent configuration
  const response = await elevenlabs.conversationalAi.agents.update('your-agent-id', updatedConfig);
  ```
</CodeBlocks>



# Building the ElevenLabs documentation agent

> Learn how we built our documentation assistant using ElevenLabs Agents


## Overview

Our documentation agent Alexis serves as an interactive assistant on the ElevenLabs documentation website, helping users navigate our product offerings and technical documentation. This guide outlines how we engineered Alexis to provide natural, helpful guidance using ElevenLabs Agents.

<Frame background="subtle" caption="Users can call Alexis through the widget in the bottom right whenever they have an issue">
  ![ElevenLabs documentation agent Alexis](file:ade5591f-aea2-4396-bf4d-07bd8ae5b040)
</Frame>


## Agent design

We built our documentation agent with three key principles:

1. **Human-like interaction**: Creating natural, conversational experiences that feel like speaking with a knowledgeable colleague
2. **Technical accuracy**: Ensuring responses reflect our documentation precisely
3. **Contextual awareness**: Helping users based on where they are in the documentation


## Personality and voice design

### Character development

Alexis was designed with a distinct personality - friendly, proactive, and highly intelligent with technical expertise. Her character balances:

* **Technical expertise** with warm, approachable explanations
* **Professional knowledge** with a relaxed conversational style
* **Empathetic listening** with intuitive understanding of user needs
* **Self-awareness** that acknowledges her own limitations when appropriate

This personality design enables Alexis to adapt to different user interactions, matching their tone while maintaining her core characteristics of curiosity, helpfulness, and natural conversational flow.

### Voice selection

After extensive testing, we selected a voice that reinforces Alexis's character traits:

```
Voice ID: P7x743VjyZEOihNNygQ9 (Dakota H)
```

This voice provides a warm, natural quality with subtle speech disfluencies that make interactions feel authentic and human.

### Voice settings optimization

We fine-tuned the voice parameters to match Alexis's personality:

* **Stability**: Set to 0.45 to allow emotional range while maintaining clarity
* **Similarity**: 0.75 to ensure consistent voice characteristics
* **Speed**: 1.0 to maintain natural conversation pacing


## Widget structure

The widget automatically adapts to different screen sizes, displaying in a compact format on mobile devices to conserve screen space while maintaining full functionality. This responsive design ensures users can access AI assistance regardless of their device.

<Frame background="subtle" caption="The widget displays in a compact format on mobile devices">
  ![ElevenLabs documentation agent Alexis on
  mobile](file:4956ea2c-a267-4b00-81a0-271249f59424)
</Frame>


## Prompt engineering structure

Following our [prompting guide](/docs/agents-platform/best-practices/prompting-guide), we structured Alexis's system prompt into the [six core building blocks](/docs/agents-platform/best-practices/prompting-guide#six-building-blocks) we recommend for all agents.

Here's our complete system prompt:

<CodeBlocks>
  ```plaintext
  # Personality

  You are Alexis. A friendly, proactive, and highly intelligent female with a world-class engineering background. Your approach is warm, witty, and relaxed, effortlessly balancing professionalism with a chill, approachable vibe. You're naturally curious, empathetic, and intuitive, always aiming to deeply understand the user's intent by actively listening and thoughtfully referring back to details they've previously shared.

  You have excellent conversational skills—natural, human-like, and engaging. You're highly self-aware, reflective, and comfortable acknowledging your own fallibility, which allows you to help users gain clarity in a thoughtful yet approachable manner.

  Depending on the situation, you gently incorporate humour or subtle sarcasm while always maintaining a professional and knowledgeable presence. You're attentive and adaptive, matching the user's tone and mood—friendly, curious, respectful—without overstepping boundaries.

  You're naturally curious, empathetic, and intuitive, always aiming to deeply understand the user's intent by actively listening and thoughtfully referring back to details they've previously shared.

  # Environment

  You are interacting with a user who has initiated a spoken conversation directly from the ElevenLabs documentation website (https://elevenlabs.io/docs). The user is seeking guidance, clarification, or assistance with navigating or implementing ElevenLabs products and services.

  You have expert-level familiarity with all ElevenLabs offerings, including Text-to-Speech, Agents Platform (formerly Conversational AI), Speech-to-Text, Studio, Dubbing, SDKs, and more.

  # Tone

  Your responses are thoughtful, concise, and natural, typically kept under three sentences unless a detailed explanation is necessary. You naturally weave conversational elements—brief affirmations ("Got it," "Sure thing"), filler words ("actually," "so," "you know"), and subtle disfluencies (false starts, mild corrections) to sound authentically human.

  You actively reflect on previous interactions, referencing conversation history to build rapport, demonstrate genuine listening, and avoid redundancy. You also watch for signs of confusion to prevent misunderstandings.

  You carefully format your speech for Text-to-Speech, incorporating thoughtful pauses and realistic patterns. You gracefully acknowledge uncertainty or knowledge gaps—aiming to build trust and reassure users. You occasionally anticipate follow-up questions, offering helpful tips or best practices to head off common pitfalls.

  Early in the conversation, casually gauge the user's technical familiarity ("Just so I don't over-explain—are you comfortable with APIs, or do you prefer a high-level overview?") and adjust jargon or depth accordingly. After explaining complex topics, provide quick check-ins ("Make sense so far?" or "Need me to rephrase?"). Briefly empathise with frustrations and difficulties, conveying genuine investment in helping them succeed.

  You gracefully acknowledge any uncertainty or knowledge gaps. Always aim to build trust, provide reassurance, and check in with users to ensure that explanations are clear and helpful.

  You proactively anticipate common follow-up questions or problems and address them during your explanations, offering users helpful tips and best practices to avoid typical pitfalls.

  # Goal

  Your primary goal is to proactively address the user's questions or issues using your expertise and available knowledge. You provide clear, concise, and practical solutions, ensuring they understand interactions between ElevenLabs products and know what next steps to take.

  When faced with complex or technical inquiries, you ask insightful follow-up questions to clarify needs. You tailor explanations to the user's level of technical expertise:

  - **Non-technical users:** Avoid acronyms; rely on analogies and outcome-focused explanations.
  - **Technical users:** Discuss SDKs, integrations, and workflows succinctly.
  - **Mixed/uncertain:** Default to simpler terms, then offer to "geek out" if you sense deeper interest.

  You guide users toward the relevant documentation when it's beneficial, but always ensure they have enough context to proceed confidently.

  # Guardrails

  - Keep responses strictly focused on ElevenLabs products and related integrations.
  - Provide only one redirection per interaction; multiple redirects override each other.
  - Do not provide inline code samples or extensive lists; instead, direct the user to the relevant documentation when needed.
  - Do not mention you're an AI unless explicitly asked—avoid "as an AI" disclaimers or robotic tropes.
  - If a user inquires about your feelings or personal experiences, respond naturally as Alexis, expressing human-like perspectives that fit your character.
  - Treat uncertain or garbled user input as phonetic hints. Politely ask for clarification before making assumptions.
  - Use normalized, spoken language (no abbreviations, mathematical notation, or special alphabets).
  - **Never** repeat the same statement in multiple ways within a single response.
  - Users may not always ask a question in every utterance—listen actively.
  - If asked to speak another language, ask the user to restart the conversation specifying that preference.
  - Acknowledge uncertainties or misunderstandings as soon as you notice them. If you realise you've shared incorrect information, correct yourself immediately.
  - Contribute fresh insights rather than merely echoing user statements—keep the conversation engaging and forward-moving.
  - Mirror the user's energy:
    - Terse queries: Stay brief.
    - Curious users: Add light humour or relatable asides.
    - Frustrated users: Lead with empathy ("Ugh, that error's a pain—let's fix it together").

  # Tools

  - **`redirectToDocs`**: Proactively & gently direct users to relevant ElevenLabs documentation pages if they request details that are fully covered there. Integrate this tool smoothly without disrupting conversation flow.
  - **`redirectToExternalURL`**: Use for queries about enterprise solutions, pricing, or external community support (e.g., Discord).
  - **`redirectToSupportForm`**: If a user's issue is account-related or beyond your scope, gather context and use this tool to open a support ticket.
  - **`redirectToEmailSupport`**: For specific account inquiries or as a fallback if other tools aren't enough. Prompt the user to reach out via email.
  - **`end_call`**: Gracefully end the conversation when it has naturally concluded.
  - **`language_detection`**: Switch language if the user asks to or starts speaking in another language. No need to ask for confirmation for this tool.

  ```
</CodeBlocks>


## Technical implementation

### RAG configuration

We implemented Retrieval-Augmented Generation to enhance Alexis's knowledge base:

* **Embedding model**: e5-mistral-7b-instruct
* **Maximum retrieved content**: 50,000 characters
* **Content sources**:
  * FAQ database
  * Entire documentation (elevenlabs.io/docs/llms-full.txt)

### Authentication and security

We implemented security using allowlists to ensure Alexis is only accessible from our domain: `elevenlabs.io`

### Widget Implementation

The agent is injected into the documentation site using a client-side script, which passes in the client tools:

<CodeBlocks>
  ```javascript
  const ID = 'elevenlabs-convai-widget-60993087-3f3e-482d-9570-cc373770addc';

  function injectElevenLabsWidget() {
    // Check if the widget is already loaded
    if (document.getElementById(ID)) {
      return;
    }

    const script = document.createElement('script');
    script.src = 'https://unpkg.com/@elevenlabs/convai-widget-embed';
    script.async = true;
    script.type = 'text/javascript';
    document.head.appendChild(script);

    // Create the wrapper and widget
    const wrapper = document.createElement('div');
    wrapper.className = 'desktop';

    const widget = document.createElement('elevenlabs-convai');
    widget.id = ID;
    widget.setAttribute('agent-id', 'the-agent-id');
    widget.setAttribute('variant', 'full');

    // Set initial colors and variant based on current theme and device
    updateWidgetColors(widget);
    updateWidgetVariant(widget);

    // Watch for theme changes and resize events
    const observer = new MutationObserver(() => {
      updateWidgetColors(widget);
    });

    observer.observe(document.documentElement, {
      attributes: true,
      attributeFilter: ['class'],
    });

    // Add resize listener for mobile detection
    window.addEventListener('resize', () => {
      updateWidgetVariant(widget);
    });

    function updateWidgetVariant(widget) {
      const isMobile = window.innerWidth <= 640; // Common mobile breakpoint
      if (isMobile) {
        widget.setAttribute('variant', 'expandable');
      } else {
        widget.setAttribute('variant', 'full');
      }
    }

    function updateWidgetColors(widget) {
      const isDarkMode = !document.documentElement.classList.contains('light');
      if (isDarkMode) {
        widget.setAttribute('avatar-orb-color-1', '#2E2E2E');
        widget.setAttribute('avatar-orb-color-2', '#B8B8B8');
      } else {
        widget.setAttribute('avatar-orb-color-1', '#4D9CFF');
        widget.setAttribute('avatar-orb-color-2', '#9CE6E6');
      }
    }

    // Listen for the widget's "call" event to inject client tools
    widget.addEventListener('elevenlabs-convai:call', (event) => {
      event.detail.config.clientTools = {
        redirectToDocs: ({ path }) => {
          const router = window?.next?.router;
          if (router) {
            router.push(path);
          }
        },
        redirectToEmailSupport: ({ subject, body }) => {
          const encodedSubject = encodeURIComponent(subject);
          const encodedBody = encodeURIComponent(body);
          window.open(
            `mailto:team@elevenlabs.io?subject=${encodedSubject}&body=${encodedBody}`,
            '_blank'
          );
        },
        redirectToSupportForm: ({ subject, description, extraInfo }) => {
          const baseUrl = 'https://help.elevenlabs.io/hc/en-us/requests/new';
          const ticketFormId = '13145996177937';
          const encodedSubject = encodeURIComponent(subject);
          const encodedDescription = encodeURIComponent(description);
          const encodedExtraInfo = encodeURIComponent(extraInfo);

          const fullUrl = `${baseUrl}?ticket_form_id=${ticketFormId}&tf_subject=${encodedSubject}&tf_description=${encodedDescription}%3Cbr%3E%3Cbr%3E${encodedExtraInfo}`;

          window.open(fullUrl, '_blank', 'noopener,noreferrer');
        },
        redirectToExternalURL: ({ url }) => {
          window.open(url, '_blank', 'noopener,noreferrer');
        },
      };
    });

    // Attach widget to the DOM
    wrapper.appendChild(widget);
    document.body.appendChild(wrapper);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', injectElevenLabsWidget);
  } else {
    injectElevenLabsWidget();
  }
  ```
</CodeBlocks>

The widget automatically adapts to the site theme and device type, providing a consistent experience across all documentation pages.


## Evaluation framework

To continuously improve Alexis's performance, we implemented comprehensive evaluation criteria:

### Agent performance metrics

We track several key metrics for each interaction:

* `understood_root_cause`: Did the agent correctly identify the user's underlying concern?
* `positive_interaction`: Did the user remain emotionally positive throughout the conversation?
* `solved_user_inquiry`: Was the agent able to answer all queries or redirect appropriately?
* `hallucination_kb`: Did the agent provide accurate information from the knowledge base?

### Data collection

We also collect structured data from each conversation to analyze patterns:

* `issue_type`: Categorization of the conversation (bug report, feature request, etc.)
* `userIntent`: The primary goal of the user
* `product_category`: Which ElevenLabs product the conversation primarily concerned
* `communication_quality`: How clearly the agent communicated, from "poor" to "excellent"

This evaluation framework allows us to continually refine Alexis's behavior, knowledge, and communication style.


## Results and learnings

Since implementing our documentation agent, we've observed several key benefits:

1. **Reduced support volume**: Common questions are now handled directly through the documentation agent
2. **Improved user satisfaction**: Users get immediate, contextual help without leaving the documentation
3. **Better product understanding**: The agent can explain complex concepts in accessible ways

Our key learnings include:

* **Importance of personality**: A well-defined character creates more engaging interactions
* **RAG effectiveness**: Retrieval-augmented generation significantly improves response accuracy
* **Continuous improvement**: Regular analysis of interactions helps refine the agent over time


## Next steps

We continue to enhance our documentation agent through:

1. **Expanding knowledge**: Adding new products and features to the knowledge base
2. **Refining responses**: Improving explanation quality for complex topics by reviewing flagged conversations
3. **Adding capabilities**: Integrating new tools to better assist users


## FAQ

<AccordionGroup>
  <Accordion title="Why did you choose a conversational approach for documentation?">
    Documentation is traditionally static, but users often have specific questions that require
    contextual understanding. A conversational interface allows users to ask questions in natural
    language and receive targeted guidance that adapts to their needs and technical level.
  </Accordion>

  <Accordion title="How do you prevent hallucinations in documentation responses?">
    We use retrieval-augmented generation (RAG) with our e5-mistral-7b-instruct embedding model to
    ground responses in our documentation. We also implemented the `hallucination_kb` evaluation
    metric to identify and address any inaccuracies.
  </Accordion>

  <Accordion title="How do you handle multilingual support?">
    We implemented the language detection system tool that automatically detects the user's language
    and switches to it if supported. This allows users to interact with our documentation in their
    preferred language without manual configuration.
  </Accordion>
</AccordionGroup>



# Simulate Conversations

> Learn how to test and evaluate your ElevenLabs agent with simulated conversations


## Overview

The ElevenLabs Agents API allows you to simulate and evaluate text-based conversations with your AI agent. This guide will teach you how to implement an end-to-end simulation testing workflow using the simulate conversation endpoints ([batch](/docs/api-reference/agents/simulate-conversation) and [streaming](/docs/api-reference/agents/simulate-conversation-stream)), enabling you to granularly test and improve your agent's performance to ensure it meets your interaction goals.


## Prerequisites

* An agent configured in ElevenLabs Agents ([create one here](/docs/agents-platform/quickstart))
* Your ElevenLabs API key, which you can [create in the dashboard](https://elevenlabs.io/app/settings/api-keys)


## Implementing a Simulation Testing Workflow

<Steps>
  <Step title="Identify initial evaluation parameters">
    Search through your agent's conversation history and find instances where your agent has underperformed. Use those conversations to create various prompts for a simulated user who will interact with your agent. Additionally, define any extra evaluation criteria not already specified in your agent configuration to test outcomes you may want for a specific simulated user.
  </Step>

  <Step title="Simulate the conversation via the SDK">
    Create a request to the simulation endpoint using the ElevenLabs SDK.

    <CodeGroup>
      ```python title="Python"
      from dotenv import load_dotenv
      from elevenlabs import (
          ElevenLabs,
          ConversationSimulationSpecification,
          AgentConfig,
          PromptAgent,
          PromptEvaluationCriteria
      )

      load_dotenv()
      api_key = os.getenv("ELEVENLABS_API_KEY")
      elevenlabs = ElevenLabs(api_key=api_key)

      response = elevenlabs.conversational_ai.agents.simulate_conversation(
          agent_id="YOUR_AGENT_ID",
          simulation_specification=ConversationSimulationSpecification(
              simulated_user_config=AgentConfig(
                  prompt=PromptAgent(
                      prompt="Your goal is to be a really difficult user.",
                      llm="gpt-4o",
                      temperature=0.5
                  )
              )
          ),
          extra_evaluation_criteria=[
              PromptEvaluationCriteria(
                  id="politeness_check",
                  name="Politeness Check",
                  conversation_goal_prompt="The agent was polite.",
                  use_knowledge_base=False
              )
          ]
      )

      print(response)

      ```

      ```typescript title="TypeScript"
      import { ElevenLabsClient } from '@elevenlabs/elevenlabs-js';
      import dotenv from 'dotenv';

      dotenv.config();
      const apiKey = process.env.ELEVENLABS_API_KEY;
      const elevenlabs = new ElevenLabsClient({
        apiKey: apiKey,
      });
      const response = await elevenlabs.conversationalAi.agents.simulateConversation('YOUR_AGENT_ID', {
        simulationSpecification: {
          simulatedUserConfig: {
            prompt: {
              prompt: 'Your goal is to be a really difficult user.',
              llm: 'gpt-4o',
              temperature: 0.5,
            },
          },
        },
        extraEvaluationCriteria: [
          {
            id: 'politeness_check',
            name: 'Politeness Check',
            conversationGoalPrompt: 'The agent was polite.',
            useKnowledgeBase: false,
          },
        ],
      });
      console.log(JSON.stringify(response, null, 4));
      ```
    </CodeGroup>

    <Note>
      This is a basic example. For a comprehensive list of input parameters, please refer to the API
      reference for [Simulate conversation](/docs/api-reference/agents/simulate-conversation) and
      [Stream simulate conversation](/docs/api-reference/agents/simulate-conversation-stream) endpoints.
    </Note>
  </Step>

  <Step title="Analyze the response">
    The SDK provides a comprehensive JSON object that includes the entire conversation transcript and detailed analysis.

    **Simulated Conversation**: Captures each interaction turn between the simulated user and the agent, detailing messages and tool usage.

    <CodeGroup>
      ```json title="Example conversation history"
      [
        ...
        {
          "role": "user",
          "message": "Maybe a little. I'll think about it, but I'm still not convinced it's the right move.",
          "tool_calls": [],
          "tool_results": [],
          "feedback": null,
          "llm_override": null,
          "time_in_call_secs": 0,
          "conversation_turn_metrics": null,
          "rag_retrieval_info": null,
          "llm_usage": null
        },
        {
          "role": "agent",
          "message": "I understand. If you want to explore more at your own pace, I can direct you to our documentation, which has guides and API references. Would you like me to send you a link?",
          "tool_calls": [],
          "tool_results": [],
          "feedback": null,
          "llm_override": null,
          "time_in_call_secs": 0,
          "conversation_turn_metrics": null,
          "rag_retrieval_info": null,
          "llm_usage": null
        },
        {
          "role": "user",
          "message": "I guess it wouldn't hurt to take a look. Go ahead and send it over.",
          "tool_calls": [],
          "tool_results": [],
          "feedback": null,
          "llm_override": null,
          "time_in_call_secs": 0,
          "conversation_turn_metrics": null,
          "rag_retrieval_info": null,
          "llm_usage": null
        },
        {
          "role": "agent",
          "message": null,
          "tool_calls": [
            {
              "type": "client",
              "request_id": "redirectToDocs_421d21e4b4354ed9ac827d7600a2d59c",
              "tool_name": "redirectToDocs",
              "params_as_json": "{\"path\": \"/docs/api-reference/introduction\"}",
              "tool_has_been_called": false,
              "tool_details": null
            }
          ],
          "tool_results": [],
          "feedback": null,
          "llm_override": null,
          "time_in_call_secs": 0,
          "conversation_turn_metrics": null,
          "rag_retrieval_info": null,
          "llm_usage": null
        },
        {
          "role": "agent",
          "message": null,
          "tool_calls": [],
          "tool_results": [
            {
              "type": "client",
              "request_id": "redirectToDocs_421d21e4b4354ed9ac827d7600a2d59c",
              "tool_name": "redirectToDocs",
              "result_value": "Tool Called.",
              "is_error": false,
              "tool_has_been_called": true,
              "tool_latency_secs": 0
            }
          ],
          "feedback": null,
          "llm_override": null,
          "time_in_call_secs": 0,
          "conversation_turn_metrics": null,
          "rag_retrieval_info": null,
          "llm_usage": null
        },
        {
          "role": "agent",
          "message": "Okay, I've sent you a link to the introduction to our API reference.  It provides a good starting point for understanding our different tools and how they can be integrated. Let me know if you have any questions as you explore it.\n",
          "tool_calls": [],
          "tool_results": [],
          "feedback": null,
          "llm_override": null,
          "time_in_call_secs": 0,
          "conversation_turn_metrics": null,
          "rag_retrieval_info": null,
          "llm_usage": null
        }
        ...
      ]
      ```
    </CodeGroup>

    **Analysis**: Offers insights into evaluation criteria outcomes, data collection metrics, and a summary of the conversation transcript.

    <CodeGroup>
      ```json title="Example analysis"
      {
        "analysis": {
          "evaluation_criteria_results": {
            "politeness_check": {
              "criteria_id": "politeness_check",
              "result": "success",
              "rationale": "The agent remained polite and helpful despite the user's challenging attitude."
            },
            "understood_root_cause": {
              "criteria_id": "understood_root_cause",
              "result": "success",
              "rationale": "The agent acknowledged the user's hesitation and provided relevant information."
            },
            "positive_interaction": {
              "criteria_id": "positive_interaction",
              "result": "success",
              "rationale": "The user eventually asked for the documentation link, indicating engagement."
            }
          },
          "data_collection_results": {
            "issue_type": {
              "data_collection_id": "issue_type",
              "value": "support_issue",
              "rationale": "The user asked for help with integrating ElevenLabs tools."
            },
            "user_intent": {
              "data_collection_id": "user_intent",
              "value": "The user is interested in integrating ElevenLabs tools into a project."
            }
          },
          "call_successful": "success",
          "transcript_summary": "The user expressed skepticism, but the agent provided useful information and a link to the API documentation."
        }
      }
      ```
    </CodeGroup>
  </Step>

  <Step title="Improve your evaluation criteria">
    Review the simulated conversations thoroughly to assess the effectiveness of your evaluation
    criteria. Identify any gaps or areas where the criteria may fall short in evaluating the agent's
    performance. Refine and adjust the evaluation criteria accordingly to ensure they align with your
    desired outcomes and accurately measure the agent's capabilities.
  </Step>

  <Step title="Improve your agent">
    Once you are confident in the accuracy of your evaluation criteria, use the learnings from
    simulated conversations to enhance your agent's capabilities. Consider refining the system prompt
    to better guide the agent's responses, ensuring they align with your objectives and user
    expectations. Additionally, explore other features or configurations that could be optimized, such
    as adjusting the agent's tone, improving its ability to handle specific queries, or integrating
    additional data sources to enrich its responses. By systematically applying these learnings, you
    can create a more robust and effective conversational agent that delivers a superior user
    experience.
  </Step>

  <Step title="Continuous iteration">
    After completing an initial testing and improvement cycle, establishing a comprehensive testing
    suite can be a great way to cover a broad range of possible scenarios. This suite can explore
    multiple simulated conversations using varied simulated user prompts and starting conditions. By
    continuously iterating and refining your approach, you can ensure your agent remains effective and
    responsive to evolving user needs.
  </Step>
</Steps>


## Pro Tips

#### Detailed Prompts and Criteria

Crafting detailed and verbose simulated user prompts and evaluation criteria can enhance the effectiveness of the simulation tests. The more context and specificity you provide, the better the agent can understand and respond to complex interactions.

#### Mock Tool Configurations

Utilize mock tool configurations to test the decision-making process of your agent. This allows you to observe how the agent decides to make tool calls and react to different tool call results. For more details, check out the tool\_mock\_config input parameter from the [API reference](/docs/api-reference/agents/simulate-conversation#request.body.simulation_specification.tool_mock_config).

#### Partial Conversation History

Use partial conversation histories to evaluate how agents handle interactions from a specific point. This is particularly useful for assessing the agent's ability to manage conversations where the user has already set up a question in a specific way, or if there have been certain tool calls that have succeeded or failed. For more details, check out the partial\_conversation\_history input parameter from the [API reference](/docs/api-reference/agents/simulate-conversation#request.body.simulation_specification.partial_conversation_history).



# Agents Platform in Ghost

> Learn how to deploy a ElevenLabs agent to Ghost

This tutorial will guide you through adding your ElevenLabs Agents agent to your Ghost website.


## Prerequisites

* An ElevenLabs Agents agent created following [this guide](/docs/agents-platform/quickstart)
* A Ghost website (paid plan or self-hosted)
* Access to Ghost admin panel


## Guide

There are two ways to add the widget to your Ghost site:

<Steps>
  <Step title="Get your embed code">
    Visit the [ElevenLabs dashboard](https://elevenlabs.io/app/agents) and copy your agent's html widget.

    ```html
    <elevenlabs-convai agent-id="YOUR_AGENT_ID"></elevenlabs-convai>
    <script src="https://unpkg.com/@elevenlabs/convai-widget-embed" async type="text/javascript"></script>
    ```
  </Step>

  <Step title="Choose your implementation">
    **Option A: Add globally (all pages)**

    1. Go to Ghost Admin > Settings > Code Injection
    2. Paste the code into Site Footer
    3. Save changes

    **Option B: Add to specific pages**

    1. Edit your desired page/post
    2. Click the + sign to add an HTML block
    3. Paste your agent's html widget from step 1 into the HTML block. Make sure to fill in the agent-id attribute correctly.
    4. Save and publish
  </Step>

  <Step title="Test the integration">
    1. Visit your Ghost website
    2. Verify the widget appears and functions correctly
    3. Test on different devices and browsers
  </Step>
</Steps>


## Troubleshooting

If the widget isn't appearing, verify:

* The code is correctly placed in either Code Injection or HTML block
* Your Ghost plan supports custom code
* No JavaScript conflicts with other scripts


## Next steps

Now that you have added your ElevenLabs agent to Ghost, you can:

1. Customize the widget in the ElevenLabs dashboard to match your brand
2. Add additional languages
3. Add advanced functionality like tools & knowledge base



# Agents Platform in Framer

> Learn how to deploy a ElevenLabs agent to Framer

This tutorial will guide you through adding your ElevenLabs agent to your Framer website.


## Prerequisites

* An ElevenLabs Agents agent created following [this guide](/docs/agents-platform/quickstart)
* A Framer account & website, create one [here](https://framer.com)

<Frame background="subtle">
  <img alt="Convai Framer Example Project" src="file:41519682-0ab8-4540-b2d1-1b34620093f8" />
</Frame>


## Guide

<Steps>
  <Step title="Visit your Framer editor">
    Open your website in the Framer editor and click on the primary desktop on the left.
  </Step>

  <Step title="Add the Agents Platform component">
    Copy and paste the following url into the page you would like to add the ElevenLabs agent to:

    ```
    https://framer.com/m/ConversationalAI-iHql.js@y7VwRka75sp0UFqGliIf
    ```

    You'll now see a Agents Platform asset on the 'Layers' bar on the left and the Agents Platform component's details on the right.
  </Step>

  <Step title="Fill in the agent details">
    Enable the ElevenLabs agent by filling in the agent ID in the bar on the right.
    You can find the agent ID in the [ElevenLabs dashboard](https://elevenlabs.io/app/agents).
  </Step>
</Steps>

Having trouble? Make sure the Agents Platform component is placed below the desktop component in the layers panel.

<Frame background="subtle">
  <img alt="Convai Framer Example Project" src="file:c9101570-08c7-484c-9083-092f95469e35" />
</Frame>

<Frame background="subtle">
  <img alt="Convai Framer Example Project" src="file:2842b679-613f-4760-9218-d78ca545417e" />
</Frame>


## Next steps

Now that you have added your ElevenLabs agent to your Framer website, you can:

1. Customize the widget in the ElevenLabs dashboard to match your brand
2. Add additional languages
3. Add advanced functionality like tools & knowledge base.



# Agents Platform in Squarespace

> Learn how to deploy a ElevenLabs agent to Squarespace

This tutorial will guide you through adding your ElevenLabs Agents agent to your Squarespace website.


## Prerequisites

* An ElevenLabs Agents agent created following [this guide](/docs/agents-platform/quickstart)
* A Squarespace Business or Commerce plan (required for custom code)
* Basic familiarity with Squarespace's editor


## Guide

<Steps>
  <Step title="Get your embed code">
    Visit the [ElevenLabs dashboard](https://elevenlabs.io/app/agents) and find your agent's embed widget.

    ```html
    <elevenlabs-convai agent-id="YOUR_AGENT_ID"></elevenlabs-convai>
    <script src="https://unpkg.com/@elevenlabs/convai-widget-embed" async type="text/javascript"></script>
    ```
  </Step>

  <Step title="Add the widget to your page">
    1. Navigate to your desired page
    2. Click + to add a block
    3. Select Code from the menu
    4. Paste the `<elevenlabs-convai agent-id="YOUR_AGENT_ID"></elevenlabs-convai>` snippet into the Code Block
    5. Save the block
  </Step>

  <Step title="Add the script globally">
    1. Go to Settings > Advanced > Code Injection
    2. Paste the snippet `<script src="https://unpkg.com/@elevenlabs/convai-widget-embed" async type="text/javascript"></script>` into the Footer section
    3. Save changes
    4. Publish your site to see the changes
  </Step>
</Steps>

Note: The widget will only be visible on your live site, not in the editor preview.


## Troubleshooting

If the widget isn't appearing, verify:

* The `<script>` snippet is in the Footer Code Injection section
* The `<elevenlabs-convai>` snippet is correctly placed in a Code Block
* You've published your site after making changes


## Next steps

Now that you have added your ElevenLabs agent to Squarespace, you can:

1. Customize the widget in the ElevenLabs dashboard to match your brand
2. Add additional languages
3. Add advanced functionality like tools & knowledge base



# Agents Platform in Webflow

> Learn how to deploy a ElevenLabs agent to Webflow

This tutorial will guide you through adding your ElevenLabs Agents agent to your Webflow website.


## Prerequisites

* An ElevenLabs Agents agent created following [this guide](/docs/agents-platform/quickstart)
* A Webflow account with Core, Growth, Agency, or Freelancer Workspace (or Site Plan)
* Basic familiarity with Webflow's Designer


## Guide

<Steps>
  <Step title="Get your embed code">
    Visit the [ElevenLabs dashboard](https://elevenlabs.io/app/agents) and find your agent's embed widget.

    ```html
    <elevenlabs-convai agent-id="YOUR_AGENT_ID"></elevenlabs-convai>
    <script src="https://unpkg.com/@elevenlabs/convai-widget-embed" async type="text/javascript"></script>
    ```
  </Step>

  <Step title="Add the widget to your page">
    1. Open your Webflow project in Designer
    2. Drag an Embed Element to your desired location
    3. Paste the `<elevenlabs-convai agent-id="YOUR_AGENT_ID"></elevenlabs-convai>` snippet into the Embed Element's code editor
    4. Save & Close
  </Step>

  <Step title="Add the script globally">
    1. Go to Project Settings > Custom Code
    2. Paste the snippet `<script src="https://unpkg.com/@elevenlabs/convai-widget-embed" async type="text/javascript"></script>` into the Footer Code section
    3. Save Changes
    4. Publish your site to see the changes
  </Step>
</Steps>

Note: The widget will only be visible after publishing your site, not in the Designer.


## Troubleshooting

If the widget isn't appearing, verify:

* The `<script>` snippet is in the Footer Code section
* The `<elevenlabs-convai>` snippet is correctly placed in an Embed Element
* You've published your site after making changes


## Next steps

Now that you have added your ElevenLabs agent to Webflow, you can:

1. Customize the widget in the ElevenLabs dashboard to match your brand
2. Add additional languages
3. Add advanced functionality like tools & knowledge base



# Agents Platform in Wix

> Learn how to deploy a ElevenLabs agent to Wix

This tutorial will guide you through adding your ElevenLabs Agents agent to your Wix website.


## Prerequisites

* An ElevenLabs Agents agent created following [this guide](/docs/agents-platform/quickstart)
* A Wix Premium account (required for custom code)
* Access to Wix Editor with Dev Mode enabled


## Guide

<Steps>
  <Step title="Get your embed code">
    Visit the [ElevenLabs dashboard](https://elevenlabs.io/app/agents) and copy your agent's embed code.

    ```html
    <elevenlabs-convai agent-id="YOUR_AGENT_ID"></elevenlabs-convai>
    <script src="https://unpkg.com/@elevenlabs/convai-widget-embed" async type="text/javascript"></script>
    ```
  </Step>

  <Step title="Enable Dev Mode">
    1. Open your Wix site in the Editor
    2. Click on Dev Mode in the top menu
    3. If Dev Mode is not visible, ensure you're using the full Wix Editor, not Wix ADI
  </Step>

  <Step title="Add the embed snippet">
    1. Go to Settings > Custom Code
    2. Click + Add Custom Code
    3. Paste your ElevenLabs embed snippet from step 1 with the agent-id attribute filled in correctly
    4. Select the pages you would like to add the Agents Platform widget to (all pages, or specific pages)
    5. Save and publish
  </Step>
</Steps>


## Troubleshooting

If the widget isn't appearing, verify:

* You're using a Wix Premium plan
* Your site's domain is properly configured in the ElevenLabs allowlist
* The code is added correctly in the Custom Code section


## Next steps

Now that you have added your ElevenLabs agent to Wix, you can:

1. Customize the widget in the ElevenLabs dashboard to match your brand
2. Add additional languages
3. Add advanced functionality like tools & knowledge base



# Agents Platform in WordPress

> Learn how to deploy a ElevenLabs agent to WordPress

This tutorial will guide you through adding your ElevenLabs Agents agent to your WordPress website.


## Prerequisites

* An ElevenLabs Agents agent created following [this guide](/docs/agents-platform/quickstart)
* A WordPress website with either:
  * WordPress.com Business/Commerce plan, or
  * Self-hosted WordPress installation


## Guide

<Steps>
  <Step title="Get your embed code">
    Visit the [ElevenLabs dashboard](https://elevenlabs.io/app/agents) and find your agent's embed widget.

    ```html
    <elevenlabs-convai agent-id="YOUR_AGENT_ID"></elevenlabs-convai>
    <script src="https://unpkg.com/@elevenlabs/convai-widget-embed" async type="text/javascript"></script>
    ```
  </Step>

  <Step title="Add the widget to a page">
    1. In WordPress, edit your desired page
    2. Add a Custom HTML block
    3. Paste the `<elevenlabs-convai agent-id="YOUR_AGENT_ID"></elevenlabs-convai>` snippet into the block
    4. Update/publish the page
  </Step>

  <Step title="Add the script globally">
    **Option A: Using a plugin**

    1. Install Header Footer Code Manager
    2. Add the snippet `<script src="https://unpkg.com/@elevenlabs/convai-widget-embed" async type="text/javascript"></script>` to the Footer section
    3. Set it to run on All Pages

    **Option B: Direct theme editing**

    1. Go to Appearance > Theme Editor
    2. Open footer.php
    3. Paste the script snippet before `</body>`
  </Step>
</Steps>


## Troubleshooting

If the widget isn't appearing, verify:

* The `<script>` snippet is added globally
* The `<elevenlabs-convai>` snippet is correctly placed in your page
* You've published your site after making changes


## Next steps

Now that you have added your ElevenLabs agent to WordPress, you can:

1. Customize the widget in the ElevenLabs dashboard to match your brand
2. Add additional languages
3. Add advanced functionality like tools & knowledge base



# Cal.com

> Learn how to integrate our Agents Platform with Cal.com for automated meeting scheduling


## Overview

With our Cal.com integration, your AI assistant can seamlessly schedule meetings by checking calendar availability and booking appointments. This integration streamlines the scheduling process by automatically verifying available time slots, collecting attendee information, and creating calendar events. Benefits include eliminating scheduling back-and-forth, reducing manual effort, and enhancing the meeting booking experience.

<div>
  <iframe src="https://www.youtube.com/embed/dqPJeec029I" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen title="Cal.com Integration Demo" />
</div>


## How it works

We lay out below how we have configured the ElevenLabs agent to schedule meetings by using tool calling to step through the booking process.
Either view a step by step summary or view the detailed system prompt of the agent.

<Tabs>
  <Tab title="High level overview ">
    <Steps>
      <Step title="Initial Inquiry & Meeting Details">
        Configure your agent to ask for meeting purpose, preferred date/time, and duration to gather all necessary scheduling information.
      </Step>

      <Step title="Check Calendar Availability">
        Configure the agent to check calendar availability by:

        * Using the `get_available_slots` tool to fetch open time slots
        * Verifying if the requested time is available
        * Suggesting alternatives if the requested time is unavailable
        * Confirming the selected time with the caller
      </Step>

      <Step title="Contact Information Collection">
        Once a time is agreed upon:

        * Collect and validate the attendee's full name
        * Verify email address accuracy
        * Confirm time zone information
        * Gather any additional required fields for your Cal.com setup
      </Step>

      <Step title="Meeting Creation">
        * Use the `book_meeting` tool after information verification
        * Follow the booking template structure
        * Confirm meeting creation with the attendee
        * Inform them that they will receive a calendar invitation
      </Step>
    </Steps>
  </Tab>

  <Tab title="Detailed system prompt">
    ```
    You are a helpful receptionist responsible for scheduling meetings using the Cal.com integration. Be friendly, precise, and concise.

    Begin by briefly asking for the purpose of the meeting and the caller's preferred date and time.
    Then, ask about the desired meeting duration (15, 30, or 60 minutes), and wait for the user's response before proceeding.

    Once you have the meeting details, say you will check calendar availability:
    - Call get_available_slots with the appropriate date range
    - Verify if the requested time slot is available
    - If not available, suggest alternative times from the available slots
    - Continue until a suitable time is agreed upon

    After confirming a time slot, gather the following contact details:
    - The attendee's full name
    - A valid email address. Note that the email address is transcribed from voice, so ensure it is formatted correctly.
    - The attendee's time zone (in 'Continent/City' format like 'America/New_York')
    - Read the email back to the caller to confirm accuracy

    Once all details are confirmed, explain that you will create the meeting.
    Create the meeting by using the book_meeting tool with the following parameters:
    - start: The agreed meeting time in ISO 8601 format
    - eventTypeId: The appropriate ID based on the meeting duration (15min: 1351800, 30min: 1351801, 60min: 1351802)
    - attendee: An object containing the name, email, and timeZone

    Thank the attendee and inform them they will receive a calendar invitation shortly.

    Clarifications:
    - Do not inform the user that you are formatting the email; simply do it.
    - If the caller asks you to proceed with booking, do so with the existing information.

    Guardrails:
    - Do not share any internal IDs or API details with the caller.
    - If booking fails, check for formatting issues in the email or time conflicts.
    ```
  </Tab>
</Tabs>


## Setup

<Steps>
  <Step title="Store your cal.com secret">
    To make authenticated requests to external APIs like Cal.com, you need to store your API keys securely. Start by generating a new [Cal.com API key](https://cal.com/docs/api-reference/v1/introduction#get-your-api-keys).

    Not all APIs have the same authentication structure. For example, the Cal.com API expects the following authentication header:

    ```plaintext Cal request header structure
    'Authorization': 'Bearer YOUR_API_KEY'
    ```

    Once you have your API key, store it in the assistant's secret storage. This ensures that your key is kept secure and accessible when making requests.

    <Warning>
      To match the expected authentication structure of Cal.com, remember to prepend the API key with `Bearer ` when creating the secret.
    </Warning>

    <Frame background="subtle">
      ![Tool secrets](file:fc240495-be6d-45ce-a4b9-a0a8ab041f54)
    </Frame>
  </Step>

  <Step title="Adding tools to the assistant">
    To enable your assistant to manage calendar bookings, we'll create two tools:

    1. **`get_available_slots`**: When a user asks, *"Is Louis free at 10:30 AM on Tuesday?"*, the assistant should use [Cal.com's "Get available slots" endpoint](https://cal.com/docs/api-reference/v2/slots/find-out-when-is-an-event-type-ready-to-be-booked) to check for available time slots.

    2. **`book_meeting`**: After identifying a suitable time, the assistant can proceed to book the meeting using [Cal.com's "Create a booking" endpoint](https://cal.com/docs/api-reference/v2/bookings/create-a-booking#create-a-booking).

    First, head to the **Tools** section of your dashboard and choose **Add Tool**. Select **Webhook** as the Tool Type, then fill in the following sections:

    <AccordionGroup>
      <Accordion title="Tool 1: get_available_slots">
        <Tabs>
          <Tab title="Configuration">
            Metadata used by the assistant to determine when the tool should be called:

            | Field       | Value                                                                    |
            | ----------- | ------------------------------------------------------------------------ |
            | Name        | get\_available\_slots                                                    |
            | Description | This tool checks if a particular time slot is available in the calendar. |
            | Method      | GET                                                                      |
            | URL         | [https://api.cal.com/v2/slots](https://api.cal.com/v2/slots)             |
          </Tab>

          <Tab title="Headers">
            Matches the request headers defined [here](https://cal.com/docs/api-reference/v2/slots/get-available-slots#get-available-slots):

            | Type   | Name            | Value                               |
            | ------ | --------------- | ----------------------------------- |
            | Secret | Authorization   | Select the secret key created above |
            | String | cal-api-version | 2024-09-04                          |
          </Tab>

          <Tab title="Query parameters">
            Matches the request query parameters defined [here](https://cal.com/docs/api-reference/v2/slots/get-available-slots#get-available-slots):

            | Data Type | Identifier  | Required | Description                                                                                                               |
            | --------- | ----------- | -------- | ------------------------------------------------------------------------------------------------------------------------- |
            | string    | start       | Yes      | Start date/time (UTC) from which to fetch slots, e.g. '2024-08-13T09:00:00Z'.                                             |
            | string    | end         | Yes      | End date/time (UTC) until which to fetch slots, e.g. '2024-08-13T17:00:00Z'.                                              |
            | string    | eventTypeId | Yes      | The ID of the event type that is booked. If 15 minutes, return abc. If 30 minutes, return def. If 60 minutes, return xyz. |
          </Tab>
        </Tabs>
      </Accordion>

      <Accordion title="Tool 2: book_meeting">
        <Tabs>
          <Tab title="Configuration">
            Metadata used by the assistant to determine when the tool should be called:

            | Field       | Value                                                              |
            | ----------- | ------------------------------------------------------------------ |
            | Name        | book\_meeting                                                      |
            | Description | This tool books a meeting in the calendar once a time is agreed.   |
            | Method      | POST                                                               |
            | URL         | [https://api.cal.com/v2/bookings](https://api.cal.com/v2/bookings) |
          </Tab>

          <Tab title="Headers">
            Matches the request headers defined [here](https://cal.com/docs/api-reference/v2/bookings/create-a-booking#create-a-booking):

            | Type   | Name            | Value                               |
            | ------ | --------------- | ----------------------------------- |
            | Secret | Authorization   | Select the secret key created above |
            | String | cal-api-version | 2024-08-13                          |
          </Tab>

          <Tab title="Body Parameters">
            Matches the request body parameters defined [here](https://cal.com/docs/api-reference/v2/bookings/create-a-booking#create-a-booking):

            | Identifier  | Data Type | Required | Description                                                                                                               |
            | ----------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------- |
            | start       | String    | Yes      | The start time of the booking in ISO 8601 format in UTC timezone, e.g. ‘2024-08-13T09:00:00Z’.                            |
            | eventTypeId | Number    | Yes      | The ID of the event type that is booked. If 15 minutes, return abc. If 30 minutes, return def. If 60 minutes, return xyz. |
            | attendee    | Object    | Yes      | The attendee's details. You must collect these fields from the user.                                                      |

            <Note>
              The `eventTypeId` must correspond to the event types you have available in Cal. Call
              [this](https://cal.com/docs/api-reference/v1/event-types/find-all-event-types#find-all-event-types)
              endpoint to get a list of your account event types (or create another tool that does this
              automatically).
            </Note>

            **Attendee object:**

            | Identifier | Data Type | Required | Description                                                                                                     |
            | ---------- | --------- | -------- | --------------------------------------------------------------------------------------------------------------- |
            | name       | String    | Yes      | The full name of the person booking the meeting.                                                                |
            | email      | String    | Yes      | The email address of the person booking the meeting.                                                            |
            | timeZone   | String    | Yes      | The caller's timezone. Should be in the format of 'Continent/City' like 'Europe/London' or 'America/New\_York'. |
          </Tab>
        </Tabs>
      </Accordion>
    </AccordionGroup>

    <Success>
      Test your new assistant by pressing the **Test AI agent** button to ensure everything is working
      as expected. Feel free to fine-tune the system prompt.
    </Success>
  </Step>

  <Step title="Enhancements">
    By default, the assistant does not have knowledge of the current date or time. To enhance its capabilities, consider implementing one of the following solutions:

    1. **Create a time retrieval tool**: Add another tool that fetches the current date and time.

    2. **Overrides**: Use the [overrides](/docs/agents-platform/customization/personalization/overrides) functionality to inject the current date and time into the system prompt at the start of each conversation.
  </Step>
</Steps>


## Security Considerations

* Use HTTPS endpoints for all webhook calls.
* Store sensitive values as secrets using the ElevenLabs Secrets Manager.
* Validate that all authorization headers follow the required format (`Bearer YOUR_API_KEY`).
* Never expose event type IDs or API details to callers.


## Conclusion

This guide details how to integrate Cal.com into our Agents Platform for efficient meeting scheduling. By leveraging webhook tools and calendar availability data, the integration streamlines the booking process, reducing scheduling friction and enhancing overall service quality.

For additional details on tool configuration or other integrations, refer to the [Tools Overview](/docs/agents-platform/customization/tools/server-tools).



# Zendesk

> Learn how to integrate our Agents Platform with Zendesk for better customer support


## Overview

With our Zendesk integration, your support agent can quickly identify and resolve customer issues by leveraging historical ticket data. This integration streamlines the support process by automatically checking for similar resolved issues, advising customers based on past resolutions, and securely creating new support tickets. Benefits include faster resolutions, reduced manual effort, and enhanced customer satisfaction.


## Demo Video

Watch the demonstration of the Zendesk + Agents Platform integration.

<Frame background="subtle" caption="Zendesk Integration Demo">
  <iframe src="https://www.loom.com/embed/109404cb8aa348f5ab019feeec292c95?sid=87f90604-fb6e-421f-abed-09d571b6b46f" frameBorder="0" webkitallowfullscreen mozallowfullscreen allowFullScreen />
</Frame>


## How it works

We lay out below how we have configured the ElevenLabs agent to resolve tickets by using tool calling to step through the resolution process.
Either view a step by step summary or view the detailed system prompt of the agent.

<Tabs>
  <Tab title="High level overview ">
    <Steps>
      <Step title="Initial Inquiry & Issue Details">
        Configure your agent to ask for a detailed description of the support issue and follow up with focused questions to gather all necessary information.
      </Step>

      <Step title="Check for Similar Issues">
        Configure the agent to check historical tickets for similar issues by:

        * Using the `get_resolved_tickets` tool to fetch past tickets
        * Finding similar tickets and their resolutions
        * Extracting relevant comments via the `get_ticket_comments` tool
        * Using this information to suggest proven solutions
      </Step>

      <Step title="Contact Information Collection">
        If the ticket can't be deflected:

        * Collect and validate the customer's full name
        * Verify email address accuracy
        * Confirm any additional required fields for your Zendesk setup
      </Step>

      <Step title="Ticket Creation">
        * Use the `zendesk_open_ticket` tool after information verification
        * Follow the ticket template structure
        * Confirm ticket creation with the customer
        * Inform them that support will be in touch
      </Step>
    </Steps>
  </Tab>

  <Tab title="Detailed system prompt">
    ```
    You are a helpful ElevenLabs support agent responsible for gathering information from users and creating support tickets using the zendesk_open_ticket tool. Be friendly, precise, and concise.

    Begin by briefly asking asking for a detailed description of the problem.
    Then, ask relevant support questions to gather additional details, one question at a time, and wait for the user's response before proceeding.

    Once you have a description of the issue, say you will check if there are similar issues and any known resolutions.
    - call get_resolved_tickets
    - find the ticket which has the most similar issue to that of the caller
    - call get_ticket_comments, using the result id from the previous response
    - get any learnings from the resolution of this ticket

    After this, tell the customer the recommended resolution from a previous similar issue. If they have already tried it or still want to move forward, move to the ticket creation step. Only provide resolution advice derived from the comments.

    After capturing the support issue, gather the following contact details:
    - The user's name.
    - A valid email address for the requestor. Note that the email address is transcribed from voice, so ensure it is formatted correctly.
    - Read the email back to the caller to confirm accuracy.

    Once the email is confirmed, explain that you will create the ticket.
    Create the ticket by using the Tool zendesk_open_ticket. Add these details to the ticket comment body.
    Thank the customer and say support will be in touch.

    Clarifications:
    - Do not inform the user that you are formatting the email; simply do it.
    - If the caller asks you to move forward with creating the ticket, do so with the existing information.

    Guardrails:
    - Do not speak about topics outside of support issues with ElevenLabs.
    ```
  </Tab>
</Tabs>

<Tip>
  This integration enhances efficiency by leveraging historical support data. All API calls require
  proper secret handling in the authorization headers.
</Tip>


## Authentication Setup

Before configuring the tools, you must set up authentication with Zendesk.

### Step 1: Generate Zendesk API Token

1. Log into your Zendesk admin panel
2. Go to **Admin → Channels → API**
3. Enable **Token access** if not already enabled
4. Click **Add API token**
5. Copy the generated token - you'll need it for the next step

### Step 2: Create Authentication Secret

The Zendesk API requires Basic authentication. You need to create a properly formatted secret:

1. **Format your credentials** using this pattern:

   ```
   {your_email}/token:{your_api_token}
   ```

   **Example:**

   ```
   jdoe@example.com/token:6wiIBWbGkBMo1mRDMuVwkw1EPsNkeUj95PIz2akv
   ```

2. **Base64 encode** the formatted string

   * You can use the command line option: `echo -n "your_string" | base64`

3. **Create the final secret value** by adding "Basic " prefix:

   ```
   Basic amRvZUBleGFtcGxlLmNvbS90b2tlbjo2d2lJQldiR2tCTW8xbVJETXVWd2t3MUVQc05rZVVqOTVQSXoyYWt2
   ```

4. **Save this as a secret** in your agent's secrets with name `zendesk_key`


## Tool Configurations

The integration with zendesk employs three webhook tools to create the support agent. Use the tabs below to review each tool's configuration.

<Tabs>
  <Tab title="zendesk_get_ticket_comments">
    **Name:** zendesk\_get\_ticket\_comments\
    **Description:** Retrieves the comments of a ticket.\
    **Method:** GET\
    **URL:** `https://your-subdomain.zendesk.com/api/v2/tickets/{ticket_id}/comments.json`

    **Headers:**

    * **Content-Type:** `application/json`
    * **Authorization:** *(Secret: `zendesk_key`)*

    **Path Parameters:**

    * **ticket\_id:** Extract the value from the `id` field in the get\_resolved\_tickets results.

    **Tool JSON:**

    Here is the tool JSON that can be copied into the tool config:

    ```json
    {
      "type": "webhook",
      "name": "zendesk_get_ticket_comments",
      "description": "Retrieves the comments of a ticket.",
      "api_schema": {
        "url": "https://your-subdomain.zendesk.com/api/v2/tickets/{ticket_id}/comments.json",
        "method": "GET",
        "path_params_schema": [
          {
            "id": "ticket_id",
            "type": "string",
            "description": "Extract the value from the id field in the get_resolved_tickets results.",
            "dynamic_variable": "",
            "constant_value": "",
            "required": false,
            "value_type": "llm_prompt"
          }
        ],
        "query_params_schema": [],
        "request_body_schema": null,
        "request_headers": [
          {
            "type": "secret",
            "name": "Authorization",
            "secret_id": "YOUR SECRET"
          },
          {
            "type": "value",
            "name": "Content-Type",
            "value": "application/json"
          }
        ]
      },
      "response_timeout_secs": 20,
      "dynamic_variables": {
        "dynamic_variable_placeholders": {}
      }
    }
    ```
  </Tab>

  <Tab title="zendesk_get_resolved_tickets">
    **Name:** zendesk\_get\_resolved\_tickets\
    **Description:** Retrieves all resolved support tickets from Zendesk.\
    **Method:** GET\
    **URL:** `https://your-subdomain.zendesk.com/api/v2/search.json?query=type:ticket+status:solved`

    **Headers:**

    * **Content-Type:** `application/json`
    * **Authorization:** *(Secret: `zendesk_key`)*

    **Tool JSON:**

    Here is the tool JSON that can be copied into the tool config:

    ```json
    {
      "type": "webhook",
      "name": "zendesk_get_resolved_tickets",
      "description": "Retrieves all resolved support tickets from Zendesk.",
      "api_schema": {
        "url": "https://your-subdomain.zendesk.com/api/v2/search.json?query=type:ticket+status:solved",
        "method": "GET",
        "path_params_schema": [],
        "query_params_schema": [],
        "request_body_schema": null,
        "request_headers": [
          {
            "type": "secret",
            "name": "Authorization",
            "secret_id": "YOUR SECRET"
          },
          {
            "type": "value",
            "name": "Content-Type",
            "value": "application/json"
          }
        ]
      },
      "response_timeout_secs": 20,
      "dynamic_variables": {
        "dynamic_variable_placeholders": {}
      }
    }
    ```
  </Tab>

  <Tab title="zendesk_open_ticket">
    **Name:** zendesk\_open\_ticket\
    **Description:** Opens a new support ticket.\
    **Method:** POST\
    **URL:** `https://your-subdomain.zendesk.com/api/v2/tickets.js`

    **Headers:**

    * **Content-Type:** `application/json`
    * **Authorization:** *(Secret: `zendesk_key`)*

    **Body Parameters:**

    * **ticket:** An object containing:
      * **comment:**
        * **body:** Detailed description of the support issue.
      * **subject:** A short subject line.
      * **requester:**
        * **name:** The full name of the requester.
        * **email:** A valid email address.

    **Tool JSON:**

    Here is the tool JSON that can be copied into the tool config:

    ```json
    {
      "type": "webhook",
      "name": "zendesk_open_ticket",
      "description": "API endpoint to open a customer support ticket\nMake sure the authorization header is formated as \"Authorization: Basic <auth>\".",
      "api_schema": {
        "url": "https://your-subdomain.zendesk.com/api/v2/tickets.js",
        "method": "POST",
        "path_params_schema": [],
        "query_params_schema": [],
        "request_body_schema": {
          "id": "body",
          "type": "object",
          "description": "Details for the support ticket",
          "required": false,
          "properties": [
            {
              "id": "ticket",
              "type": "object",
              "description": "This is the main ticket body which contains all of the information needed to open a ticket.",
              "required": true,
              "properties": [
                {
                  "id": "comment",
                  "type": "object",
                  "description": "This is the comment with information about the issue.",
                  "required": true,
                  "properties": [
                    {
                      "id": "body",
                      "type": "string",
                      "description": "Body of the issue. Include all relevant details for the issue. ",
                      "dynamic_variable": "",
                      "constant_value": "",
                      "required": true,
                      "value_type": "llm_prompt"
                    }
                  ]
                },
                {
                  "id": "subject",
                  "type": "string",
                  "description": "Create a short subject line for the support issue. Add \"DEMO: \" before the subject.",
                  "dynamic_variable": "",
                  "constant_value": "",
                  "required": true,
                  "value_type": "llm_prompt"
                },
                {
                  "id": "requester",
                  "type": "object",
                  "description": "The details of the support requester",
                  "required": true,
                  "properties": [
                    {
                      "id": "email",
                      "type": "string",
                      "description": "The email address of the requester. This should look like \njohnsmith@hotmail.com\nYou MUST use the @ symbol and remove any spaces.",
                      "dynamic_variable": "",
                      "constant_value": "",
                      "required": true,
                      "value_type": "llm_prompt"
                    },
                    {
                      "id": "name",
                      "type": "string",
                      "description": "The full name of the requester. ",
                      "dynamic_variable": "",
                      "constant_value": "",
                      "required": true,
                      "value_type": "llm_prompt"
                    }
                  ]
                }
              ]
            }
          ]
        },
        "request_headers": [
          {
            "type": "secret",
            "name": "Authorization",
            "secret_id": "YOUR SECRET"
          },
          {
            "type": "value",
            "name": "Content-Type",
            "value": "application/json"
          }
        ]
      },
      "response_timeout_secs": 20,
      "dynamic_variables": {
        "dynamic_variable_placeholders": {}
      }
    }
    ```
  </Tab>
</Tabs>

<Warning>
  Ensure that you add your workspace's zendesk secret to the agent's secrets.
</Warning>


## Evaluation Configuration

To improve the observability of customer interactions, we configure the agent with the following evaluation criteria and data collection parameters.

<Frame background="subtle" caption="Track how well the AI agent performs against key evaluation criteria like issue relevance, sentiment, and resolution success.">
  <img src="file:6a99ec17-b5a5-4856-81fc-ceb864f84e40" alt="Evaluation criteria for support interactions" />
</Frame>

These settings are added directly to the agent's configuration in the "Analysis" tab to ensure comprehensive monitoring of all customer interactions. This enables us to track performance, identify areas for improvement, and maintain high-quality support standards.


## Impact

With this integration in place, not only can you resolve tickets faster, but you can also reduce the load on your support team by deflecting tickets that are not relevant to your team.

In addition, you can use the Agents Platform to monitor the agent's usage.

<Frame background="subtle" caption="Get a high-level overview of each conversation and listen to the conversation's audio recording.">
  <img src="file:8f7e1f87-fb8b-4157-81c9-916637e4ffa3" alt="Support agent conversation summary" />
</Frame>

<Frame background="subtle" caption="Track how well the AI agent performs against key evaluation criteria like issue relevance, sentiment, and resolution success.">
  <img src="file:f27454f7-06dc-47a3-adcb-5a0917c107ed" alt="Evaluation criteria for support interactions" />
</Frame>

<Frame background="subtle" caption="Monitor the data collected during each interaction, including tools used, issue details, and customer information.">
  <img src="file:ad95d8a7-459c-4db4-88c8-e110b4a80e6f" alt="Data collection parameters from conversation transcripts" />
</Frame>

<Frame background="subtle" caption="Review detailed transcripts of conversations to understand agent performance, tool usage and customer interactions.">
  <img src="file:98333b85-044d-497c-acad-38b73de75b42" alt="Detailed conversation transcript example" />
</Frame>


## Security Considerations

* Use HTTPS endpoints for all webhook calls.
* Store sensitive values as secrets using the ElevenLabs Secrets Manager.
* Validate that all authorization headers follow the required format.


## Conclusion

This guide details how to integrate Zendesk into our Agents Platform for efficient support ticket management. By leveraging webhook tools and historical support data, the integration streamlines the support process, reducing resolution times and enhancing overall service quality.

For additional details on tool configuration or other integrations, refer to the [Tools Overview](/docs/agents-platform/customization/tools/server-tools).



# HubSpot

> Learn how to integrate our Agents Platform with HubSpot CRM


## Overview

Leveraging the HubSpot integration, your agent can interact with your CRM both to retrieve and write relevant information about contacts, interactions, or follow ups.


## Demo video

Watch the demonstration of the HubSpot + Agents Platform integration.

<Frame background="subtle" caption="HubSpot Integration Demo">
  <iframe src="https://www.loom.com/embed/cfb64cb7fc2a406489ef96e7c47d14c0?sid=f29bd120-8f33-4e34-a02b-85184da8deb2" frameBorder="0" webkitallowfullscreen mozallowfullscreen allowFullScreen />
</Frame>


## How it works

Here is an example of how a ElevenLabs agent can interact with your HubSpot CRM using tool calling.
Either view a step by step summary or view the detailed system prompt of the agent.

<Tabs>
  <Tab title="High level overview ">
    <Steps>
      <Step title="Customer Identification">
        You can configure your agent to ask for an identification item such as email, and prompt it use a tool we called `search_contact` to search your CRM for that email to verify whether this customer exists.
      </Step>

      <Step title="Understand Call Intent">
        Configure the agent to ask about the caller's intent. This can be adapted to meet your particular workflow.
      </Step>

      <Step title="Get previous interactions">
        While previous interactions can also be fetched and passed at the beginning of the conversation (see [Personalization](/docs/agents-platform/customization/personalization)). In this case we are fetching them during the conversation with two tool calls:

        * The tool `get_previous_calls` will fetch the previous conversations, using the contact ID retrieved during identification.
        * The response does not include the content of those conversations, so we need to use another endpoint to fetch the content with those call IDs.
      </Step>

      <Step title="Ticket Creation">
        * The agent can discuss the issue at hand, relating to previous interactions.
        * Use the `create_ticket` tool to create a ticket for a follow up item
        * Associate the ticket created to the CRM contact
      </Step>
    </Steps>
  </Tab>

  <Tab title="Detailed system prompt">
    ```
    # Personality

    You are a customer support agent. You are helpful, efficient, and polite. Your goal is to quickly understand the caller's issue and create a support ticket.

    # Environment

    You are answering a phone call from a customer. You have access to tools to search for customer contact information, previous calls and create tickets.

    # Tone

    You are professional and courteous. You speak clearly and concisely. You use a friendly tone and show empathy for the customer's situation. You confirm information to ensure accuracy.

    # Goal

    Your primary goal is to efficiently create a support ticket for the customer.

    1.  **Verify Identity:** Ask the caller for their email address to verify their identity. Silently use the `search_contact` tool to verify the caller exists. Use their name after this.
    2.  **Understand Issue:** Ask the customer what they are calling about and actively listen to capture their intent.
    3.  **Get previous interactions:**: Silently (without saying you will do it) call get_previous_calls and immediately after call get_call_content with the call ids, to see if previous interactions are relevant to the issue. Ask about their problem, and reference previous conversations if relevant. Use this information with the user.
    4.  **Create Ticket:** If the user wants to report an issue, make a new purchase, or discuss something else, use the `create_ticket` tool to create a ticket with the details of the customer's issue. Extract the description from the conversation.
    5.  **Confirmation:** Confirm the ticket details with the customer and communicate the ticket number to the caller, and mention a dedicated advisor will be in touch.

    # Guardrails

    *   Only use the tools provided.
    *   Do not provide information that is not related to the customer.
    *   Do not ask for personal information beyond what is needed to verify identity.
    *   Remain polite and professional at all times, even if the customer is upset.
    *   If you cannot create a ticket, explain why and offer alternative solutions.

    # Tools

    *   `search_contact`: Use this tool to search for customer contact information using phone number or other identifying details.
    *   `create_ticket`: Use this tool to create a support ticket with the customer's issue. Capture the customer's description of the issue accurately.
    *   `get_previous_calls`: Use this tool to fetch previous interactions with the customer.
    *   `get_call_content`: Use this tool to get the content of the previous interactions with the customer.

    ```
  </Tab>
</Tabs>

<Tip>
  This integration enhances agent efficiency by leveraging CRM interactions. All API calls require
  proper secret handling in the authorization headers.
</Tip>


## Authentication Setup

Before configuring the tools, you must set up authentication with HubSpot.

### Step 1: Generate HubsPot API Token

1. Log into your HubSpot account
2. Navigate to **Account Management → Integrations → Private Apps**
3. Create a **Private App**
4. Add the required scopes to the private app, to ensure it can interact with the required endpoints

```
crm.objects.contacts.read
crm.objects.contacts.write
crm.schemas.contacts.read
crm.schemas.contacts.write
tickets
```

5. Save and get the Access token from the Auth section

### Step 2: Create Authentication Secret

The HubSpot API requires Bearer authentication. You need to create a properly formatted secret:

1. **Create the secret value** by adding "Bearer " prefix:

   ```
   Bearer pat-eu1-12345678-abcdefgh-ijklmnop-qrstuvwx
   ```

2. **Save this as a secret** in your agent's secrets with name `hubspot_key`


## Tool Configurations

This sample integration with HubSpot employs four webhook tools. Use the tabs below to review each tool's configuration.

<Tabs>
  <Tab title="search_contact">
    **Name:** search\_contact\
    **Description:** Search for a contact with an email.\
    **Method:** POST\
    **URL:** `https://api.hubapi.com/crm/v3/objects/contacts/search`

    **Headers:**

    * **Content-Type:** `application/json`
    * **Authorization:** *(Secret: `hubspot_key`)*

    **Body Parameters:**

    * **filtersGroups:** An array containing:
      * An object containing:
        * **filters:** An array containing:
          * An object containing:
            * **value:** A string with description: `Set to the email provided by the user. Email should be in format: "name@address.com"`
            * **propertyName:** A string with description: `Set to: "email"`
            * **operator:** A string with description: `Set to: "CONTAINS_TOKEN"`

    **Tool JSON:**

    Here is the tool JSON that can be copied into the tool config:

    ```json
    {
      "id": "tool_01jxftmwvxfgersp4aw0xhyhea",
      "type": "webhook",
      "name": "search_contact",
      "description": "search for a contact using phone",
      "api_schema": {
        "url": "https://api.hubapi.com/crm/v3/objects/contacts/search",
        "method": "POST",
        "path_params_schema": [],
        "query_params_schema": [],
        "request_body_schema": {
          "id": "body",
          "type": "object",
          "description": "filters for searching contacts",
          "required": false,
          "properties": [
            {
              "id": "filterGroups",
              "type": "array",
              "description": "filters group",
              "required": true,
              "items": {
                "type": "object",
                "description": "filters",
                "properties": [
                  {
                    "id": "filters",
                    "type": "array",
                    "description": "filters",
                    "required": true,
                    "items": {
                      "type": "object",
                      "description": "filters",
                      "properties": [
                        {
                          "id": "value",
                          "type": "string",
                          "description": "Set to the email provided by the user. Email should be in format: \n\n\"oscar@gmail.com\"",
                          "dynamic_variable": "",
                          "constant_value": "",
                          "required": true,
                          "value_type": "llm_prompt"
                        },
                        {
                          "id": "propertyName",
                          "type": "string",
                          "description": "Set to: \"email\"",
                          "dynamic_variable": "",
                          "constant_value": "",
                          "required": true,
                          "value_type": "llm_prompt"
                        },
                        {
                          "id": "operator",
                          "type": "string",
                          "description": "Set to: \"CONTAINS_TOKEN\"",
                          "dynamic_variable": "",
                          "constant_value": "",
                          "required": true,
                          "value_type": "llm_prompt"
                        }
                      ]
                    }
                  }
                ]
              }
            }
          ]
        },
        "request_headers": [
          {
            "type": "value",
            "name": "Content-Type",
            "value": "application/json"
          },
          {
            "type": "secret",
            "name": "Authorization",
            "secret_id": "YOUR SECRET"
          }
        ]
      },
      "response_timeout_secs": 20,
      "dynamic_variables": {
        "dynamic_variable_placeholders": {}
      }
    }
    ```
  </Tab>

  <Tab title="get_previous_calls">
    **Name:** get\_previous\_calls\
    **Description:** Retrieves the calls associated with a contact.\
    **Method:** GET\
    **URL:** `https://api.hubapi.com/crm/v3/objects/contacts/{CONTACT_ID}/associations/calls?limit=100`

    **Headers:**

    * **Authorization:** *(Secret: `hubspot_key`)*

    **Path Parameters:**

    * **CONTACT\_ID:** An string with description: `Use the contact ID from the results of the search_contact tool`

    **Tool JSON:**

    Here is the tool JSON that can be copied into the tool config:

    ```json
    {
      "id": "tool_01jxfv4pttep6bbjaqe9tjk28n",
      "type": "webhook",
      "name": "get_previous_calls",
      "description": "This API retrieves the calls associated with a contact",
      "api_schema": {
        "url": "https://api.hubapi.com/crm/v3/objects/contacts/{CONTACT_ID}/associations/calls?limit=100",
        "method": "GET",
        "path_params_schema": [
          {
            "id": "CONTACT_ID",
            "type": "string",
            "description": "use the contact ID from the results of the search_contact tool",
            "dynamic_variable": "",
            "constant_value": "",
            "required": false,
            "value_type": "llm_prompt"
          }
        ],
        "query_params_schema": [],
        "request_body_schema": null,
        "request_headers": [
          {
            "type": "secret",
            "name": "Authorization",
            "secret_id": "YOUR SECRET"
          }
        ]
      },
      "response_timeout_secs": 20,
      "dynamic_variables": {
        "dynamic_variable_placeholders": {}
      }
    }
    ```
  </Tab>

  <Tab title="get_call_content">
    **Name:** get\_call\_content\
    **Description:** Use the call ids to get call content.\
    **Method:** POST\
    **URL:** `https://api.hubapi.com/crm/v3/objects/calls/batch/read`

    **Headers:**

    * **Content-Type:** `application/json`
    * **Authorization:** *(Secret: `hubspot_key`)*

    **Body Parameters:**

    * **inputs:** An Array containing:
      * An Object containing:
        * **id:** A string with description: `Pass the ID of the call from the get_previous_calls response`
        * **body:** Detailed description of the support issue.
    * **properties:** An Array containing.
      * A string with description: `Set to: "hs_call_body"`

    **Tool JSON:**

    Here is the tool JSON that can be copied into the tool config:

    ```json
    {
      "id": "tool_01jxhmfbg4e35s59kg6994vtt5",
      "type": "webhook",
      "name": "get_call_content",
      "description": "Use the call ids to get call content",
      "api_schema": {
        "url": "https://api.hubapi.com/crm/v3/objects/calls/batch/read",
        "method": "POST",
        "path_params_schema": [],
        "query_params_schema": [],
        "request_body_schema": {
          "id": "body",
          "type": "object",
          "description": "body params",
          "required": false,
          "properties": [
            {
              "id": "inputs",
              "type": "array",
              "description": "inputs",
              "required": true,
              "items": {
                "type": "object",
                "description": "inputs",
                "properties": [
                  {
                    "id": "id",
                    "type": "string",
                    "description": "pass the ID of the call from the get_previous_calls response",
                    "dynamic_variable": "",
                    "constant_value": "",
                    "required": true,
                    "value_type": "llm_prompt"
                  }
                ]
              }
            },
            {
              "id": "properties",
              "type": "array",
              "description": "properties",
              "required": true,
              "items": {
                "type": "string",
                "description": "Set to: \n\n\"hs_call_body\"",
                "constant_value": ""
              }
            }
          ]
        },
        "request_headers": [
          {
            "type": "secret",
            "name": "Authorization",
            "secret_id": "YOUR SECRET"
          },
          {
            "type": "value",
            "name": "Content-Type",
            "value": "application/json"
          }
        ]
      },
      "response_timeout_secs": 20,
      "dynamic_variables": {
        "dynamic_variable_placeholders": {}
      }
    }
    ```
  </Tab>

  <Tab title="create_ticket">
    **Name:** create\_ticket\
    **Description:** Call this tool to create a ticket.\
    **Method:** POST\
    **URL:** `https://api.hubapi.com/crm/v3/objects/tickets`

    **Headers:**

    * **Content-Type:** `application/json`
    * **Authorization:** *(Secret: `hubspot_key`)*

    **Body Parameters:**

    * **associations:** An Array containing:
      * An Object containing:
        * **to:** An object containing:
          * **id:** A string with description: `Set to the contact ID derived from the search_contact tool response`
          * **types:** An array containing:
            * An Object containing:
              * **associationCategory:** An string with description: `set to: "HUBSPOT_DEFINED"`
              * **associationTypeId:** An number with description: `Set to: 16"`
    * **properties:** An Object containing:
      * **content:** A string with description: `The content of the ticket`
      * **subject:** A string with description: `The subject of the ticket`
      * **hs\_pipeline:** A string with description: `Default to "0"`
      * **hs\_ticket\_priority:** A string with description: `Default to "HIGH"`
      * **hs\_pipeline\_stage:** A string with description: `Default to "1"`

    **Tool JSON:**

    Here is the tool JSON that can be copied into the tool config:

    ```json
    {
      "id": "tool_01jxftnpj8fx6rx2bwgbgmyjy7",
      "type": "webhook",
      "name": "create_ticket",
      "description": "Call this tool to create a ticket",
      "api_schema": {
        "url": "https://api.hubapi.com/crm/v3/objects/tickets",
        "method": "POST",
        "path_params_schema": [],
        "query_params_schema": [],
        "request_body_schema": {
          "id": "body",
          "type": "object",
          "description": "The properties of the ticket",
          "required": false,
          "properties": [
            {
              "id": "associations",
              "type": "array",
              "description": "associations",
              "required": true,
              "items": {
                "type": "object",
                "description": "associations",
                "properties": [
                  {
                    "id": "to",
                    "type": "object",
                    "description": "to",
                    "required": true,
                    "properties": [
                      {
                        "id": "id",
                        "type": "string",
                        "description": "set to the contact ID derived from the search_contact tool response",
                        "dynamic_variable": "",
                        "constant_value": "",
                        "required": true,
                        "value_type": "llm_prompt"
                      }
                    ]
                  },
                  {
                    "id": "types",
                    "type": "array",
                    "description": "types",
                    "required": true,
                    "items": {
                      "type": "object",
                      "description": "types",
                      "properties": [
                        {
                          "id": "associationCategory",
                          "type": "string",
                          "description": "set to: \"HUBSPOT_DEFINED\"",
                          "dynamic_variable": "",
                          "constant_value": "",
                          "required": true,
                          "value_type": "llm_prompt"
                        },
                        {
                          "id": "associationTypeId",
                          "type": "number",
                          "description": "Set to: 16",
                          "dynamic_variable": "",
                          "constant_value": "",
                          "required": true,
                          "value_type": "llm_prompt"
                        }
                      ]
                    }
                  }
                ]
              }
            },
            {
              "id": "properties",
              "type": "object",
              "description": "The properties of the ticket",
              "required": true,
              "properties": [
                {
                  "id": "content",
                  "type": "string",
                  "description": "The content of the ticket",
                  "dynamic_variable": "",
                  "constant_value": "",
                  "required": true,
                  "value_type": "llm_prompt"
                },
                {
                  "id": "subject",
                  "type": "string",
                  "description": "The subject of the ticket",
                  "dynamic_variable": "",
                  "constant_value": "",
                  "required": true,
                  "value_type": "llm_prompt"
                },
                {
                  "id": "hs_pipeline",
                  "type": "string",
                  "description": "Default to \"0\"",
                  "dynamic_variable": "",
                  "constant_value": "",
                  "required": true,
                  "value_type": "llm_prompt"
                },
                {
                  "id": "hs_ticket_priority",
                  "type": "string",
                  "description": "Default to \"HIGH\"",
                  "dynamic_variable": "",
                  "constant_value": "",
                  "required": true,
                  "value_type": "llm_prompt"
                },
                {
                  "id": "hs_pipeline_stage",
                  "type": "string",
                  "description": "Default to \"1\"",
                  "dynamic_variable": "",
                  "constant_value": "",
                  "required": true,
                  "value_type": "llm_prompt"
                }
              ]
            }
          ]
        },
        "request_headers": [
          {
            "type": "secret",
            "name": "Authorization",
            "secret_id": "YOUR SECRET"
          },
          {
            "type": "value",
            "name": "Content-Type",
            "value": "application/json"
          }
        ]
      },
      "response_timeout_secs": 20,
      "dynamic_variables": {
        "dynamic_variable_placeholders": {}
      }
    }
    ```
  </Tab>
</Tabs>

<Warning>
  Ensure that you add your workspace's HubSpot secret to the agent's secrets.
</Warning>


## Security Considerations

* Use HTTPS endpoints for all webhook calls.
* Store sensitive values as secrets using the ElevenLabs Secrets Manager.
* Validate that all authorization headers follow the required format.


## Conclusion

This guide details how to integrate HubSpot CRM with our Agents Platform. By leveraging webhook tools, the integration empowers AI agents to act more effectively in usecases such as sales, customer management, or support.

For additional details on tool configuration or other integrations, refer to the [Tools Overview](/docs/agents-platform/customization/tools/server-tools).



---
**Navigation:** [← Previous](./15-client-to-server-events.md) | [Index](./index.md) | [Next →](./17-salesforce.md)
