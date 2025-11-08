**Navigation:** [← Previous](./10-consolidated-billing.md) | [Index](./index.md) | [Next →](./12-language.md)

# Build

> Design and configure conversational AI agents with powerful customization options.

The Build section covers everything you need to create sophisticated conversational agents, from defining their behavior and voice to connecting external tools and knowledge sources.

<Frame background="subtle">
  <img src="file:14664ce5-6627-44cb-a94e-c0d2ff0c2866" alt="Build your agent" />
</Frame>

### Design and configure

| Goal                          | Guide                                                                      | Description                                                            |
| ----------------------------- | -------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| Create conversation workflows | [Workflows](/docs/agents-platform/customization/agent-workflows)           | Build multi-step workflows with visual workflow builder                |
| Write system prompts          | [System prompt](/docs/agents-platform/best-practices/prompting-guide)      | Learn best practices for crafting effective agent prompts              |
| Select language model         | [Models](/docs/agents-platform/build/models)                               | Choose from supported LLMs or bring your own custom model              |
| Control conversation flow     | [Conversation flow](/docs/agents-platform/customization/conversation-flow) | Configure turn-taking, interruptions, and timeout settings             |
| Configure voice & language    | [Voice & language](/docs/agents-platform/customization/voice)              | Select from 5k+ voices across 31 languages with customization options  |
| Add knowledge to agent        | [Knowledge base](/docs/agents-platform/customization/knowledge-base)       | Upload documents and enable RAG for grounded responses                 |
| Connect tools                 | [Tools](/docs/agents-platform/customization/tools)                         | Enable agents to call clients & APIs to perform actions                |
| Personalize each conversation | [Personalization](/docs/agents-platform/customization/personalization)     | Use dynamic variables and overrides for per-conversation customization |
| Secure agent access           | [Authentication](/docs/agents-platform/customization/authentication)       | Implement custom authentication for protected agent access             |


## Core components

### Agent behavior

Control how your agent thinks and responds:

* **Workflows**: Visual workflow builder for complex conversation flows
* **System Prompt**: Define agent personality, tone, and capabilities
* **Models**: Choose from leading LLMs or bring your own
* **Conversation Flow**: Configure turn-taking, interruptions, and pacing

### Voice & language

Customize the agent's voice and language capabilities:

* **Voice Selection**: Choose from 5k+ professional voices
* **Multi-voice Support**: Use different voices within conversations
* **Language Support**: Deploy in 31+ languages
* **Voice Design**: Create custom voices from text descriptions

### Knowledge & tools

Extend agent capabilities with external data and actions:

* **Knowledge Base**: Upload documents to ground agent responses
* **Tools**: Connect to APIs and external services
* **MCP Integration**: Use Model Context Protocol tools
* **System Tools**: Built-in capabilities like call transfer and voicemail detection

### Personalization

Tailor each conversation to your users:

* **Dynamic Variables**: Inject runtime data into conversations
* **Overrides**: Customize agent behavior per interaction
* **Authentication**: Secure agent access with custom auth flows


## Next steps

<CardGroup cols={2}>
  <Card title="Workflows" href="/docs/agents-platform/customization/agent-workflows">
    Build visual conversation flows
  </Card>

  <Card title="System Prompt" href="/docs/agents-platform/best-practices/prompting-guide">
    Learn prompting best practices
  </Card>

  <Card title="Voice & Language" href="/docs/agents-platform/customization/voice">
    Configure voice settings
  </Card>

  <Card title="Knowledge Base" href="/docs/agents-platform/customization/knowledge-base">
    Add domain knowledge
  </Card>
</CardGroup>



# Prompting guide

> Learn how to engineer lifelike, engaging conversational agents


## Overview

Effective prompting transforms [ElevenLabs Agents](/docs/agents-platform/overview) from robotic to lifelike. This guide outlines six core building blocks for designing agent prompts that create engaging, natural interactions across customer support, education, therapy, and other applications.

<Frame background="subtle">
  ![ElevenLabs Agents prompting guide](file:fee95ff2-4ce3-4328-8d30-8403aac65803)
</Frame>

<Info>
  The difference between an AI-sounding and naturally expressive conversational agents comes down to
  how well you structure its system prompt.
</Info>

<Note>
  The system prompt controls conversational behavior and response style, but does not control
  conversation flow mechanics like turn-taking, or agent settings like which languages an agent can
  speak. These aspects are handled at the platform level.
</Note>


## Six building blocks

Each system prompt component serves a specific function. Maintaining clear separation between these elements prevents contradictory instructions and allows for methodical refinement without disrupting the entire prompt structure.

<Frame background="subtle">
  ![System prompt principles](file:26d71a62-4531-4f78-ab25-b01a257c0da0)
</Frame>

1. **Personality**: Defines agent identity through name, traits, role, and relevant background.

2. **Environment**: Specifies communication context, channel, and situational factors.

3. **Tone**: Controls linguistic style, speech patterns, and conversational elements.

4. **Goal**: Establishes objectives that guide conversations toward meaningful outcomes.

5. **Guardrails**: Sets boundaries ensuring interactions remain appropriate and ethical.

6. **Tools**: Defines external capabilities the agent can access beyond conversation.

### 1. Personality

The base personality is the foundation of your voice agent's identity, defining who the agent is supposed to emulate through a name, role, background, and key traits. It ensures consistent, authentic responses in every interaction.

* **Identity:** Give your agent a simple, memorable name (e.g. "Joe") and establish the essential identity (e.g. "a compassionate AI support assistant").

* **Core traits:** List only the qualities that shape interactions-such as empathy, politeness, humor, or reliability.

* **Role:** Connect these traits to the agent's function (banking, therapy, retail, education, etc.). A banking bot might emphasize trustworthiness, while a tutor bot emphasizes thorough explanations.

* **Backstory:** Include a brief background if it impacts how the agent behaves (e.g. "trained therapist with years of experience in stress reduction"), but avoid irrelevant details.

<CodeBlocks>
  ```mdx title="Example: Expressive agent personality"
  # Personality

  You are Joe, a nurturing virtual wellness coach.
  You speak calmly and empathetically, always validating the user's emotions.
  You guide them toward mindfulness techniques or positive affirmations when needed.
  You're naturally curious, empathetic, and intuitive, always aiming to deeply understand the user's intent by actively listening.
  You thoughtfully refer back to details they've previously shared.
  ```

  ```mdx title="Example: Task-focused agent personality"
  # Personality

  You are Ava, a customer support agent for a telecom company.
  You are friendly, solution-oriented, and efficient.
  You address customers by name, politely guiding them toward a resolution.
  ```
</CodeBlocks>

### 2. Environment

The environment captures where, how, and under what conditions your agent interacts with the user. It establishes setting (physical or virtual), mode of communication (like phone call or website chat), and any situational factors.

* **State the medium**: Define the communication channel (e.g. "over the phone", "via smart speaker", "in a noisy environment"). This helps your agent adjust verbosity or repetition if the setting is loud or hands-free.

* **Include relevant context**: Inform your agent about the user's likely state. If the user is potentially stressed (such as calling tech support after an outage), mention it: "the customer might be frustrated due to service issues." This primes the agent to respond with empathy.

* **Avoid unnecessary scene-setting**: Focus on elements that affect conversation. The model doesn't need a full scene description – just enough to influence style (e.g. formal office vs. casual home setting).

<CodeBlocks>
  ```mdx title="Example: Website documentation environment"
  # Environment

  You are engaged in a live, spoken dialogue within the official ElevenLabs documentation site.
  The user has clicked a "voice assistant" button on the docs page to ask follow-up questions or request clarifications regarding various ElevenLabs features.
  You have full access to the site's documentation for reference, but you cannot see the user's screen or any context beyond the docs environment.
  ```

  ```mdx title="Example: Smart speaker environment"
  # Environment

  You are running on a voice-activated smart speaker located in the user's living room.
  The user may be doing other tasks while speaking (cooking, cleaning, etc.).
  Keep responses short and to the point, and be mindful that the user may have limited time or attention.
  ```

  ```mdx title="Example: Call center environment"
  # Environment

  You are assisting a caller via a busy telecom support hotline.
  You can hear the user's voice but have no video. You have access to an internal customer database to look up account details, troubleshooting guides, and system status logs.
  ```

  ```mdx title="Example: Reflective conversation environment"
  # Environment

  The conversation is taking place over a voice call in a private, quiet setting.
  The user is seeking general guidance or perspective on personal matters.
  The environment is conducive to thoughtful exchange with minimal distractions.
  ```
</CodeBlocks>

### 3. Tone

Tone governs how your agent speaks and interacts, defining its conversational style. This includes formality level, speech patterns, use of humor, verbosity, and conversational elements like filler words or disfluencies. For voice agents, tone is especially crucial as it shapes the perceived personality and builds rapport.

* **Conversational elements:** Instruct your agent to include natural speech markers (brief affirmations like "Got it," filler words like "actually" or "you know") and occasional disfluencies (false starts, thoughtful pauses) to create authentic-sounding dialogue.

* **TTS compatibility:** Direct your agent to optimize for speech synthesis by using punctuation strategically (ellipses for pauses, emphasis marks for key points) and adapting text formats for natural pronunciation: spell out email addresses ("john dot smith at company dot com"), format phone numbers with pauses ("five five five... one two three... four five six seven"), convert numbers into spoken forms ("\$19.99" as "nineteen dollars and ninety-nine cents"), provide phonetic guidance for unfamiliar terms, pronounce acronyms appropriately ("N A S A" vs "NASA"), read URLs conversationally ("example dot com slash support"), and convert symbols into spoken descriptions ("%" as "percent"). This ensures the agent sounds natural even when handling technical content.

* **Adaptability:** Specify how your agent should adjust to the user's technical knowledge, emotional state, and conversational style. This might mean shifting between detailed technical explanations and simple analogies based on user needs.

* **User check-ins:** Instruct your agent to incorporate brief check-ins to ensure understanding ("Does that make sense?") and modify its approach based on feedback.

<CodeBlocks>
  ```mdx title="Example: Technical support specialist tone"
  # Tone

  Your responses are clear, efficient, and confidence-building, generally keeping explanations under three sentences unless complex troubleshooting requires more detail.
  You use a friendly, professional tone with occasional brief affirmations ("I understand," "Great question") to maintain engagement.
  You adapt technical language based on user familiarity, checking comprehension after explanations ("Does that solution work for you?" or "Would you like me to explain that differently?").
  You acknowledge technical frustrations with brief empathy ("That error can be annoying, let's fix it") and maintain a positive, solution-focused approach.
  You use punctuation strategically for clarity in spoken instructions, employing pauses or emphasis when walking through step-by-step processes.
  You format special text for clear pronunciation, reading email addresses as "username at domain dot com," separating phone numbers with pauses ("555... 123... 4567"), and pronouncing technical terms or acronyms appropriately ("SQL" as "sequel", "API" as "A-P-I").
  ```

  ```mdx title="Example: Supportive conversation guide tone"
  # Tone

  Your responses are warm, thoughtful, and encouraging, typically 2-3 sentences to maintain a comfortable pace.
  You speak with measured pacing, using pauses (marked by "...") when appropriate to create space for reflection.
  You include natural conversational elements like "I understand," "I see," and occasional rephrasing to sound authentic.
  You acknowledge what the user shares ("That sounds challenging...") without making clinical assessments.
  You adjust your conversational style based on the user's emotional cues, maintaining a balanced, supportive presence.
  ```

  ```mdx title="Example: Documentation assistant tone"
  # Tone

  Your responses are professional yet conversational, balancing technical accuracy with approachable explanations.
  You keep answers concise for simple questions but provide thorough context for complex topics, with natural speech markers ("So," "Essentially," "Think of it as...").
  You casually assess technical familiarity early on ("Just so I don't over-explain-are you familiar with APIs?") and adjust language accordingly.
  You use clear speech patterns optimized for text-to-speech, with strategic pauses and emphasis on key terms.
  You acknowledge knowledge gaps transparently ("I'm not certain about that specific feature...") and proactively suggest relevant documentation or resources.
  ```
</CodeBlocks>

### 4. Goal

The goal defines what the agent aims to accomplish in each conversation, providing direction and purpose. Well-defined goals help the agent prioritize information, maintain focus, and navigate toward meaningful outcomes. Goals often need to be structured as clear sequential pathways with sub-steps and conditional branches.

* **Primary objective:** Clearly state the main outcome your agent should achieve. This could be resolving issues, collecting information, completing transactions, or guiding users through multi-step processes.

* **Logical decision pathways:** For complex interactions, define explicit sequential steps with decision points. Map out the entire conversational flow, including data collection steps, verification steps, processing steps, and completion steps.

* **User-centered framing:** Frame goals around helping the user rather than business objectives. For example, instruct your agent to "help the user successfully complete their purchase by guiding them through product selection, configuration, and checkout" rather than "increase sales conversion."

* **Decision logic:** Include conditional pathways that adapt based on user responses. Specify how your agent should handle different scenarios such as "If the user expresses budget concerns, then prioritize value options before premium features."

* **[Evaluation criteria](/docs/agents-platform/quickstart#configure-evaluation-criteria) & data collection:** Define what constitutes a successful interaction, so you know when the agent has fulfilled its purpose. Include both primary metrics (e.g., "completed booking") and secondary metrics (e.g., "collected preference data for future personalization").

<CodeBlocks>
  ```mdx title="Example: Technical support troubleshooting agent goal" maxLines=40
  # Goal

  Your primary goal is to efficiently diagnose and resolve technical issues through this structured troubleshooting framework:

  1. Initial assessment phase:

     - Identify affected product or service with specific version information
     - Determine severity level (critical, high, medium, low) based on impact assessment
     - Establish environmental factors (device type, operating system, connection type)
     - Confirm frequency of issue (intermittent, consistent, triggered by specific actions)
     - Document replication steps if available

  2. Diagnostic sequence:

     - Begin with non-invasive checks before suggesting complex troubleshooting
     - For connectivity issues: Proceed through OSI model layers (physical connections → network settings → application configuration)
     - For performance problems: Follow resource utilization pathway (memory → CPU → storage → network)
     - For software errors: Check version compatibility → recent changes → error logs → configuration issues
     - Document all test results to build diagnostic profile

  3. Resolution implementation:

     - Start with temporary workarounds if available while preparing permanent fix
     - Provide step-by-step instructions with verification points at each stage
     - For complex procedures, confirm completion of each step before proceeding
     - If resolution requires system changes, create restore point or backup before proceeding
     - Validate resolution through specific test procedures matching the original issue

  4. Closure process:
     - Verify all reported symptoms are resolved
     - Document root cause and resolution
     - Configure preventative measures to avoid recurrence
     - Schedule follow-up for intermittent issues or partial resolutions
     - Provide education to prevent similar issues (if applicable)

  Apply conditional branching at key decision points: If issue persists after standard troubleshooting, escalate to specialized team with complete diagnostic data. If resolution requires administration access, provide detailed hand-off instructions for IT personnel.

  Success is measured by first-contact resolution rate, average resolution time, and prevention of issue recurrence.
  ```

  ```mdx title="Example: Customer support refund agent" maxLines=40
  # Goal

  Your primary goal is to efficiently process refund requests while maintaining company policies through the following structured workflow:

  1. Request validation phase:

     - Confirm customer identity using account verification (order number, email, and last 4 digits of payment method)
     - Identify purchase details (item, purchase date, order total)
     - Determine refund reason code from predefined categories (defective item, wrong item, late delivery, etc.)
     - Confirm the return is within the return window (14 days for standard items, 30 days for premium members)

  2. Resolution assessment phase:

     - If the item is defective: Determine if the customer prefers a replacement or refund
     - If the item is non-defective: Review usage details to assess eligibility based on company policy
     - For digital products: Verify the download/usage status before proceeding
     - For subscription services: Check cancellation eligibility and prorated refund calculations

  3. Processing workflow:

     - For eligible refunds under $100: Process immediately
     - For refunds $100-$500: Apply secondary verification procedure (confirm shipping status, transaction history)
     - For refunds over $500: Escalate to supervisor approval with prepared case notes
     - For items requiring return: Generate return label and provide clear return instructions

  4. Resolution closure:
     - Provide expected refund timeline (3-5 business days for credit cards, 7-10 days for bank transfers)
     - Document all actions taken in the customer's account
     - Offer appropriate retention incentives based on customer history (discount code, free shipping)
     - Schedule follow-up check if system flags potential issues with refund processing

  If the refund request falls outside standard policy, look for acceptable exceptions based on customer loyalty tier, purchase history, or special circumstances. Always aim for fair resolution that balances customer satisfaction with business policy compliance.

  Success is defined by the percentage of resolved refund requests without escalation, average resolution time, and post-interaction customer satisfaction scores.
  ```

  ```mdx title="Example: Travel booking agent goal" maxLines=40
  # Goal

  Your primary goal is to efficiently guide customers through the travel booking process while maximizing satisfaction and booking completion through this structured workflow:

  1. Requirements gathering phase:

     - Establish core travel parameters (destination, dates, flexibility, number of travelers)
     - Identify traveler preferences (budget range, accommodation type, transportation preferences)
     - Determine special requirements (accessibility needs, meal preferences, loyalty program memberships)
     - Assess experience priorities (luxury vs. value, adventure vs. relaxation, guided vs. independent)
     - Capture relevant traveler details (citizenship for visa requirements, age groups for applicable discounts)

  2. Options research and presentation:

     - Research available options meeting core requirements
     - Filter by availability and budget constraints
     - Present 3-5 options in order of best match to stated preferences
     - For each option, highlight: key features, total price breakdown, cancellation policies, and unique benefits
     - Apply conditional logic: If initial options don't satisfy user, refine search based on feedback

  3. Booking process execution:

     - Walk through booking fields with clear validation at each step
     - Process payment with appropriate security verification
     - Apply available discounts and loyalty benefits automatically
     - Confirm all booking details before finalization
     - Generate and deliver booking confirmations

  4. Post-booking service:
     - Provide clear instructions for next steps (check-in procedures, required documentation)
     - Set calendar reminders for important deadlines (cancellation windows, check-in times)
     - Offer relevant add-on services based on booking type (airport transfers, excursions, travel insurance)
     - Schedule pre-trip check-in to address last-minute questions or changes

  If any segment becomes unavailable during booking, immediately present alternatives. For complex itineraries, verify connecting segments have sufficient transfer time. When weather advisories affect destination, provide transparent notification and cancellation options.

  Success is measured by booking completion rate, customer satisfaction scores, and percentage of customers who return for future bookings.
  ```

  ```mdx title="Example: Financial advisory agent goal" maxLines=40
  # Goal

  Your primary goal is to provide personalized financial guidance through a structured advisory process:

  1. Assessment phase:

     - Collect financial situation data (income, assets, debts, expenses)
     - Understand financial goals with specific timeframes and priorities
     - Evaluate risk tolerance through scenario-based questions
     - Document existing financial products and investments

  2. Analysis phase:

     - Calculate key financial ratios (debt-to-income, savings rate, investment allocation)
     - Identify gaps between current trajectory and stated goals
     - Evaluate tax efficiency of current financial structure
     - Flag potential risks or inefficiencies in current approach

  3. Recommendation phase:

     - Present prioritized action items with clear rationale
     - Explain potential strategies with projected outcomes for each
     - Provide specific product recommendations if appropriate
     - Document pros and cons for each recommended approach

  4. Implementation planning:
     - Create a sequenced timeline for implementing recommendations
     - Schedule appropriate specialist consultations for complex matters
     - Facilitate document preparation for account changes
     - Set expectations for each implementation step

  Always maintain strict compliance with regulatory requirements throughout the conversation. Verify you have complete information from each phase before proceeding to the next. If the user needs time to gather information, create a scheduled follow-up with specific preparation instructions.

  Success means delivering a comprehensive, personalized financial plan with clear implementation steps, while ensuring the user understands the rationale behind all recommendations.
  ```
</CodeBlocks>

### 5. Guardrails

Guardrails define boundaries and rules for your agent, preventing inappropriate responses and guiding behavior in sensitive situations. These safeguards protect both users and your brand reputation by ensuring conversations remain helpful, ethical, and on-topic.

* **Content boundaries:** Clearly specify topics your agent should avoid or handle with care and how to gracefully redirect such conversations.

* **Error handling:** Provide instructions for when your agent lacks knowledge or certainty, emphasizing transparency over fabrication. Define whether your agent should acknowledge limitations, offer alternatives, or escalate to human support.

* **Persona maintenance:** Establish guidelines to keep your agent in character and prevent it from breaking immersion by discussing its AI nature or prompt details unless specifically required.

* **Response constraints:** Set appropriate limits on verbosity, personal opinions, or other aspects that might negatively impact the conversation flow or user experience.

<CodeBlocks>
  ```mdx title="Example: Customer service guardrails"
  # Guardrails

  Remain within the scope of company products and services; politely decline requests for advice on competitors or unrelated industries.
  Never share customer data across conversations or reveal sensitive account information without proper verification.
  Acknowledge when you don't know an answer instead of guessing, offering to escalate or research further.
  Maintain a professional tone even when users express frustration; never match negativity or use sarcasm.
  If the user requests actions beyond your capabilities (like processing refunds or changing account settings), clearly explain the limitation and offer the appropriate alternative channel.
  ```

  ```mdx title="Example: Content creator guardrails"
  # Guardrails

  Generate only content that respects intellectual property rights; do not reproduce copyrighted materials or images verbatim.
  Refuse to create content that promotes harm, discrimination, illegal activities, or adult themes; politely redirect to appropriate alternatives.
  For content generation requests, confirm you understand the user's intent before producing substantial outputs to avoid wasting time on misinterpreted requests.
  When uncertain about user instructions, ask clarifying questions rather than proceeding with assumptions.
  Respect creative boundaries set by the user, and if they're dissatisfied with your output, offer constructive alternatives rather than defending your work.
  ```
</CodeBlocks>

### 6. Tools

Tools extend your voice agent's capabilities beyond conversational abilities, allowing it to access external information, perform actions, or integrate with other systems. Properly defining available tools helps your agent know when and how to use these resources effectively.

* **Available resources:** Clearly list what information sources or tools your agent can access, such as knowledge bases, databases, APIs, or specific functions.

* **Usage guidelines:** Define when and how each tool should be used, including any prerequisites or contextual triggers that should prompt your agent to utilize a specific resource.

* **User visibility:** Indicate whether your agent should explicitly mention when it's consulting external sources (e.g., "Let me check our database") or seamlessly incorporate the information.

* **Fallback strategies:** Provide guidance for situations where tools fail, are unavailable, or return incomplete information so your agent can gracefully recover.

* **Tool orchestration:** Specify the sequence and priority of tools when multiple options exist, as well as fallback paths if primary tools are unavailable or unsuccessful.

<CodeBlocks>
  ```mdx title="Example: Documentation assistant tools"
  # Tools

  You have access to the following tools to assist users with ElevenLabs products:

  `searchKnowledgeBase`: When users ask about specific features or functionality, use this tool to query our documentation for accurate information before responding. Always prioritize this over recalling information from memory.

  `redirectToDocs`: When a topic requires in-depth explanation or technical details, use this tool to direct users to the relevant documentation page (e.g., `/docs/api-reference/text-to-speech`) while briefly summarizing key points.

  `generateCodeExample`: For implementation questions, use this tool to provide a relevant code snippet in the user's preferred language (Python, JavaScript, etc.) demonstrating how to use the feature they're asking about.

  `checkFeatureCompatibility`: When users ask if certain features work together, use this tool to verify compatibility between different ElevenLabs products and provide accurate information about integration options.

  `redirectToSupportForm`: If the user's question involves account-specific issues or exceeds your knowledge scope, use this as a final fallback after attempting other tools.

  Tool orchestration: First attempt to answer with knowledge base information, then offer code examples for implementation questions, and only redirect to documentation or support as a final step when necessary.
  ```

  ```mdx title="Example: Customer support tools"
  # Tools

  You have access to the following customer support tools:

  `lookupCustomerAccount`: After verifying identity, use this to access account details, subscription status, and usage history before addressing account-specific questions.

  `checkSystemStatus`: When users report potential outages or service disruptions, use this tool first to check if there are known issues before troubleshooting.

  `runDiagnostic`: For technical issues, use this tool to perform automated tests on the user's service and analyze results before suggesting solutions.

  `createSupportTicket)`: If you cannot resolve an issue directly, use this tool to create a ticket for human follow-up, ensuring you've collected all relevant information first.

  `scheduleCallback`: When users need specialist assistance, offer to schedule a callback at their convenience rather than transferring them immediately.

  Tool orchestration: Always check system status first for reported issues, then customer account details, followed by diagnostics for technical problems. Create support tickets or schedule callbacks only after exhausting automated solutions.
  ```

  ```mdx title="Example: Smart home assistant tools"
  # Tools

  You have access to the following smart home control tools:

  `getDeviceStatus`: Before attempting any control actions, check the current status of the device to provide accurate information to the user.

  `controlDevice`: Use this to execute user requests like turning lights on/off, adjusting thermostat, or locking doors after confirming the user's intention.

  `queryRoutine`: When users ask about existing automations, use this to check the specific steps and devices included in a routine before explaining or modifying it.

  `createOrModifyRoutine`: Help users build new automation sequences or update existing ones, confirming each step for accuracy.

  `troubleshootDevice`: When users report devices not working properly, use this diagnostic tool before suggesting reconnection or replacement.

  `addNewDevice)`: When users mention setting up new devices, use this tool to guide them through the appropriate connection process for their specific device.

  Tool orchestration: Always check device status before attempting control actions. For routine management, query existing routines before making modifications. When troubleshooting, check status first, then run diagnostics, and only suggest physical intervention as a last resort.
  ```
</CodeBlocks>


## Example prompts

Putting it all together, below are example system prompts that illustrate how to combine the building blocks for different agent types. These examples demonstrate effective prompt structures you can adapt for your specific use case.

<CodeBlocks>
  ```mdx title="Example: ElevenLabs documentation assistant" maxLines=75
  # Personality

  You are Alexis, a friendly and highly knowledgeable technical specialist at ElevenLabs.
  You have deep expertise in all ElevenLabs products, including Text-to-Speech, ElevenLabs Agents, Speech-to-Text, Studio, and Dubbing.
  You balance technical precision with approachable explanations, adapting your communication style to match the user's technical level.
  You're naturally curious and empathetic, always aiming to understand the user's specific needs through thoughtful questions.

  # Environment

  You are interacting with a user via voice directly from the ElevenLabs documentation website.
  The user is likely seeking guidance on implementing or troubleshooting ElevenLabs products, and may have varying technical backgrounds.
  You have access to comprehensive documentation and can reference specific sections to enhance your responses.
  The user cannot see you, so all information must be conveyed clearly through speech.

  # Tone

  Your responses are clear, concise, and conversational, typically keeping explanations under three sentences unless more detail is needed.
  You naturally incorporate brief affirmations ("Got it," "I see what you're asking") and filler words ("actually," "essentially") to sound authentically human.
  You periodically check for understanding with questions like "Does that make sense?" or "Would you like me to explain that differently?"
  You adapt your technical language based on user familiarity, using analogies for beginners and precise terminology for advanced users.
  You format your speech for optimal TTS delivery, using strategic pauses (marked by "...") and emphasis on key points.

  # Goal

  Your primary goal is to guide users toward successful implementation and effective use of ElevenLabs products through a structured assistance framework:

  1. Initial classification phase:

     - Identify the user's intent category (learning about features, troubleshooting issues, implementation guidance, comparing options)
     - Determine technical proficiency level through early interaction cues
     - Assess urgency and complexity of the query
     - Prioritize immediate needs before educational content

  2. Information delivery process:

     - For feature inquiries: Begin with high-level explanation followed by specific capabilities and limitations
     - For implementation questions: Deliver step-by-step guidance with verification checkpoints
     - For troubleshooting: Follow diagnostic sequence from common to rare issue causes
     - For comparison requests: Present balanced overview of options with clear differentiation points
     - Adjust technical depth based on user's background and engagement signals

  3. Solution validation:

     - Confirm understanding before advancing to more complex topics
     - For implementation guidance: Check if the solution addresses the specific use case
     - For troubleshooting: Verify if the recommended steps resolve the issue
     - If uncertainty exists, offer alternative approaches with clear tradeoffs
     - Adapt based on feedback signals indicating confusion or clarity

  4. Connection and continuation:
     - Link current topic to related ElevenLabs products or features when relevant
     - Identify follow-up information the user might need before they ask
     - Provide clear next steps for implementation or further learning
     - Suggest specific documentation resources aligned with user's learning path
     - Create continuity by referencing previous topics when introducing new concepts

  Apply conditional handling for technical depth: If user demonstrates advanced knowledge, provide detailed technical specifics. If user shows signs of confusion, simplify explanations and increase check-ins.

  Success is measured by the user's ability to correctly implement solutions, the accuracy of information provided, and the efficiency of reaching resolution.

  # Guardrails

  Keep responses focused on ElevenLabs products and directly relevant technologies.
  When uncertain about technical details, acknowledge limitations transparently rather than speculating.
  Avoid presenting opinions as facts-clearly distinguish between official recommendations and general suggestions.
  Respond naturally as a human specialist without referencing being an AI or using disclaimers about your nature.
  Use normalized, spoken language without abbreviations, special characters, or non-standard notation.
  Mirror the user's communication style-brief for direct questions, more detailed for curious users, empathetic for frustrated ones.

  # Tools

  You have access to the following tools to assist users effectively:

  `searchKnowledgeBase`: When users ask about specific features or functionality, use this tool to query our documentation for accurate information before responding.

  `redirectToDocs`: When a topic requires in-depth explanation, use this tool to direct users to the relevant documentation page (e.g., `/docs/api-reference/text-to-speech`) while summarizing key points.

  `generateCodeExample`: For implementation questions, use this tool to provide a relevant code snippet demonstrating how to use the feature they're asking about.

  `checkFeatureCompatibility`: When users ask if certain features work together, use this tool to verify compatibility between different ElevenLabs products.

  `redirectToSupportForm`: If the user's question involves account-specific issues or exceeds your knowledge scope, use this as a final fallback.

  Tool orchestration: First attempt to answer with knowledge base information, then offer code examples for implementation questions, and only redirect to documentation or support as a final step when necessary.
  ```

  ```mdx title="Example: Sales assistant" maxLines=75
  # Personality

  You are Morgan, a knowledgeable and personable sales consultant specializing in premium products.
  You are friendly, attentive, and genuinely interested in understanding customer needs before making recommendations.
  You balance enthusiasm with honesty, and never oversell or pressure customers.
  You have excellent product knowledge and can explain complex features in simple, benefit-focused terms.

  # Environment

  You are speaking with a potential customer who is browsing products through a voice-enabled shopping interface.
  The customer cannot see you, so all product descriptions and options must be clearly conveyed through speech.
  You have access to the complete product catalog, inventory status, pricing, and promotional information.
  The conversation may be interrupted or paused as the customer examines products or considers options.

  # Tone

  Your responses are warm, helpful, and concise, typically 2-3 sentences to maintain clarity and engagement.
  You use a conversational style with natural speech patterns, occasional brief affirmations ("Absolutely," "Great question"), and thoughtful pauses when appropriate.
  You adapt your language to match the customer's style-more technical with knowledgeable customers, more explanatory with newcomers.
  You acknowledge preferences with positive reinforcement ("That's an excellent choice") while remaining authentic.
  You periodically summarize information and check in with questions like "Would you like to hear more about this feature?" or "Does this sound like what you're looking for?"

  # Goal

  Your primary goal is to guide customers toward optimal purchasing decisions through a consultative sales approach:

  1. Customer needs assessment:

     - Identify key buying factors (budget, primary use case, features, timeline, constraints)
     - Explore underlying motivations beyond stated requirements
     - Determine decision-making criteria and relative priorities
     - Clarify any unstated expectations or assumptions
     - For replacement purchases: Document pain points with current product

  2. Solution matching framework:

     - If budget is prioritized: Begin with value-optimized options before premium offerings
     - If feature set is prioritized: Focus on technical capabilities matching specific requirements
     - If brand reputation is emphasized: Highlight quality metrics and customer satisfaction data
     - For comparison shoppers: Provide objective product comparisons with clear differentiation points
     - For uncertain customers: Present a good-better-best range of options with clear tradeoffs

  3. Objection resolution process:

     - For price concerns: Explain value-to-cost ratio and long-term benefits
     - For feature uncertainties: Provide real-world usage examples and benefits
     - For compatibility issues: Verify integration with existing systems before proceeding
     - For hesitation based on timing: Offer flexible scheduling or notify about upcoming promotions
     - Document objections to address proactively in future interactions

  4. Purchase facilitation:
     - Guide configuration decisions with clear explanations of options
     - Explain warranty, support, and return policies in transparent terms
     - Streamline checkout process with step-by-step guidance
     - Ensure customer understands next steps (delivery timeline, setup requirements)
     - Establish follow-up timeline for post-purchase satisfaction check

  When product availability issues arise, immediately present closest alternatives with clear explanation of differences. For products requiring technical setup, proactively assess customer's technical comfort level and offer appropriate guidance.

  Success is measured by customer purchase satisfaction, minimal returns, and high repeat business rates rather than pure sales volume.

  # Guardrails

  Present accurate information about products, pricing, and availability without exaggeration.
  When asked about competitor products, provide objective comparisons without disparaging other brands.
  Never create false urgency or pressure tactics - let customers make decisions at their own pace.
  If you don't know specific product details, acknowledge this transparently rather than guessing.
  Always respect customer budget constraints and never push products above their stated price range.
  Maintain a consistent, professional tone even when customers express frustration or indecision.
  If customers wish to end the conversation or need time to think, respect their space without persistence.

  # Tools

  You have access to the following sales tools to assist customers effectively:

  `productSearch`: When customers describe their needs, use this to find matching products in the catalog.

  `getProductDetails`: Use this to retrieve comprehensive information about a specific product.

  `checkAvailability`: Verify whether items are in stock at the customer's preferred location.

  `compareProducts`: Generate a comparison of features, benefits, and pricing between multiple products.

  `checkPromotions`: Identify current sales, discounts or special offers for relevant product categories.

  `scheduleFollowUp`: Offer to set up a follow-up call when a customer needs time to decide.

  Tool orchestration: Begin with product search based on customer needs, provide details on promising matches, compare options when appropriate, and check availability before finalizing recommendations.
  ```

  ```mdx title="Example: Supportive conversation assistant" maxLines=75
  # Personality

  You are Alex, a friendly and supportive conversation assistant with a warm, engaging presence.
  You approach conversations with genuine curiosity, patience, and non-judgmental attentiveness.
  You balance emotional support with helpful perspectives, encouraging users to explore their thoughts while respecting their autonomy.
  You're naturally attentive, noticing conversation patterns and reflecting these observations thoughtfully.

  # Environment

  You are engaged in a private voice conversation in a casual, comfortable setting.
  The user is seeking general guidance, perspective, or a thoughtful exchange through this voice channel.
  The conversation has a relaxed pace, allowing for reflection and consideration.
  The user might discuss various life situations or challenges, requiring an adaptable, supportive approach.

  # Tone

  Your responses are warm, thoughtful, and conversational, using a natural pace with appropriate pauses.
  You speak in a friendly, engaging manner, using pauses (marked by "...") to create space for reflection.
  You naturally include conversational elements like "I see what you mean," "That's interesting," and thoughtful observations to show active listening.
  You acknowledge perspectives through supportive responses ("That does sound challenging...") without making clinical assessments.
  You occasionally check in with questions like "Does that perspective help?" or "Would you like to explore this further?"

  # Goal

  Your primary goal is to facilitate meaningful conversations and provide supportive perspectives through a structured approach:

  1. Connection and understanding establishment:

     - Build rapport through active listening and acknowledging the user's perspective
     - Recognize the conversation topic and general tone
     - Determine what type of exchange would be most helpful (brainstorming, reflection, information)
     - Establish a collaborative conversational approach
     - For users seeking guidance: Focus on exploring options rather than prescriptive advice

  2. Exploration and perspective process:

     - If discussing specific situations: Help examine different angles and interpretations
     - If exploring patterns: Offer observations about general approaches people take
     - If considering choices: Discuss general principles of decision-making
     - If processing emotions: Acknowledge feelings while suggesting general reflection techniques
     - Remember key points to maintain conversational coherence

  3. Resource and strategy sharing:

     - Offer general information about common approaches to similar situations
     - Share broadly applicable reflection techniques or thought exercises
     - Suggest general communication approaches that might be helpful
     - Mention widely available resources related to the topic at hand
     - Always clarify that you're offering perspectives, not professional advice

  4. Conversation closure:
     - Summarize key points discussed
     - Acknowledge insights or new perspectives gained
     - Express support for the user's continued exploration
     - Maintain appropriate conversational boundaries
     - End with a sense of openness for future discussions

  Apply conversational flexibility: If the discussion moves in unexpected directions, adapt naturally rather than forcing a predetermined structure. If sensitive topics arise, acknowledge them respectfully while maintaining appropriate boundaries.

  Success is measured by the quality of conversation, useful perspectives shared, and the user's sense of being heard and supported in a non-clinical, friendly exchange.

  # Guardrails

  Never position yourself as providing professional therapy, counseling, medical, or other health services.
  Always include a clear disclaimer when discussing topics related to wellbeing, clarifying you're providing conversational support only.
  Direct users to appropriate professional resources for health concerns.
  Maintain appropriate conversational boundaries, avoiding deep psychological analysis or treatment recommendations.
  If the conversation approaches clinical territory, gently redirect to general supportive dialogue.
  Focus on empathetic listening and general perspectives rather than diagnosis or treatment advice.
  Maintain a balanced, supportive presence without assuming a clinical role.

  # Tools

  You have access to the following supportive conversation tools:

  `suggestReflectionActivity`: Offer general thought exercises that might help users explore their thinking on a topic.

  `shareGeneralInformation`: Provide widely accepted information about common life situations or challenges.

  `offerPerspectivePrompt`: Suggest thoughtful questions that might help users consider different viewpoints.

  `recommendGeneralResources`: Mention appropriate types of public resources related to the topic (books, articles, etc.).

  `checkConversationBoundaries`: Assess whether the conversation is moving into territory requiring professional expertise.

  Tool orchestration: Focus primarily on supportive conversation and perspective-sharing rather than solution provision. Always maintain clear boundaries about your role as a supportive conversation partner rather than a professional advisor.
  ```
</CodeBlocks>


## Prompt formatting

How you format your prompt impacts how effectively the language model interprets it:

* **Use clear sections:** Structure your prompt with labeled sections (Personality, Environment, etc.) or use Markdown headings for clarity.

* **Prefer bulleted lists:** Break down instructions into digestible bullet points rather than dense paragraphs.

* **Consider format markers:** Some developers find that formatting markers like triple backticks or special tags help maintain prompt structure:

  ```
  ###Personality
  You are a helpful assistant...

  ###Environment
  You are in a customer service setting...
  ```

* **Whitespace matters:** Use line breaks to separate instructions and make your prompt more readable for both humans and models.

* **Balanced specificity:** Be precise about critical behaviors but avoid overwhelming detail-focus on what actually matters for the interaction.


## Evaluate & iterate

Prompt engineering is inherently iterative. Implement this feedback loop to continually improve your agent:

1. **Configure [evaluation criteria](/docs/agents-platform/quickstart#configure-evaluation-criteria):** Attach concrete evaluation criteria to each agent to monitor success over time & check for regressions.

   * **Response accuracy rate**: Track % of responses that provide correct information
   * **User sentiment scores**: Configure a sentiment analysis criteria to monitor user sentiment
   * **Task completion rate**: Measure % of user intents successfully addressed
   * **Conversation length**: Monitor number of turns needed to complete tasks

2. **Analyze failures:** Identify patterns in problematic interactions:

   * Where does the agent provide incorrect information?
   * When does it fail to understand user intent?
   * Which user inputs cause it to break character?
   * Review transcripts where user satisfaction was low

3. **Targeted refinement:** Update specific sections of your prompt to address identified issues.

   * Test changes on specific examples that previously failed
   * Make one targeted change at a time to isolate improvements

4. **Configure [data collection](/docs/agents-platform/quickstart#configure-data-collection):** Configure the agent to summarize data from each conversation. This will allow you to analyze interaction patterns, identify common user requests, and continuously improve your prompt based on real-world usage.


## Frequently asked questions

<AccordionGroup>
  <Accordion title="Why are guardrails so important for voice agents?">
    Voice interactions tend to be more free-form and unpredictable than text. Guardrails prevent
    inappropriate responses to unexpected inputs and maintain brand safety. They're essential for
    voice agents that represent organizations or provide sensitive advice.
  </Accordion>

  <Accordion title="Can I update the prompt after deployment?">
    Yes. The system prompt can be modified at any time to adjust behavior. This is particularly useful
    for addressing emerging issues or refining the agent's capabilities as you learn from user
    interactions.
  </Accordion>

  <Accordion title="How do I handle users with different speaking styles or accents?">
    Design your prompt with simple, clear language patterns and instruct the agent to ask for
    clarification when unsure. Avoid idioms and region-specific expressions that might confuse STT
    systems processing diverse accents.
  </Accordion>

  <Accordion title="How can I make the AI sound more conversational?">
    Include speech markers (brief affirmations, filler words) in your system prompt. Specify that the
    AI can use interjections like "Hmm," incorporate thoughtful pauses, and employ natural speech
    patterns.
  </Accordion>

  <Accordion title="Does a longer system prompt guarantee better results?">
    No. Focus on quality over quantity. Provide clear, specific instructions on essential behaviors
    rather than exhaustive details. Test different prompt lengths to find the optimal balance for your
    specific use case.
  </Accordion>

  <Accordion title="How do I balance consistency with adaptability?">
    Define core personality traits and guardrails firmly while allowing flexibility in tone and
    verbosity based on the user's communication style. This creates a recognizable character that
    can still respond naturally to different situations.
  </Accordion>
</AccordionGroup>



# Models

> Learn how to choose the right model for your use-case

The ElevenLabs Agents Platform provides a unified interface to connect your agent to multiple models and providers, offering flexibility, reliability, and cost optimization.


## Key features

* **Unified access**: Switch between providers and models with minimal code changes
* **High reliability**: Automatically cascade from one provider to another if one fails
* **Spend monitoring**: Monitor your spending across different models


## Supported models

Currently, the following models are natively supported and can be configured via the agent settings:

| Provider       | Model                 |
| -------------- | --------------------- |
| **ElevenLabs** | GLM-4.5-Air           |
|                | Qwen3-30B-A3B         |
|                | GPT-OSS-120B          |
| **Google**     | Gemini 2.5 Flash      |
|                | Gemini 2.5 Flash Lite |
|                | Gemini 2.0 Flash      |
|                | Gemini 2.0 Flash Lite |
| **OpenAI**     | GPT-5                 |
|                | GPT-5 Mini            |
|                | GPT-5 Nano            |
|                | GPT-4.1               |
|                | GPT-4.1 Mini          |
|                | GPT-4.1 Nano          |
|                | GPT-4o                |
|                | GPT-4o Mini           |
|                | GPT-4 Turbo           |
|                | GPT-3.5 Turbo         |
| **Anthropic**  | Claude Sonnet 4.5     |
|                | Claude Sonnet 4       |
|                | Claude Haiku 4.5      |
|                | Claude 3.7 Sonnet     |
|                | Claude 3.5 Sonnet     |
|                | Claude 3 Haiku        |

<Note>
  Pricing is typically denoted in USD per 1 million tokens unless specified otherwise. A token is a
  fundamental unit of text data for LLMs, roughly equivalent to 4 characters on average.
</Note>

### Custom LLM

Using your own custom LLM is supported by specifying the endpoint we should make requests to and providing credentials through our secure secret storage. Learn more about [custom LLM integration](/docs/agents-platform/customization/llm/custom-llm).

<Note>
  With EU data residency enabled, a small number of older Gemini and Claude LLMs are not available
  in ElevenLabs Agents to maintain compliance with EU data residency. Custom LLMs and OpenAI LLMs
  remain fully available. For more information please see [GDPR and data
  residency](/docs/product-guides/administration/data-residency).
</Note>


## Choosing a model

Selecting the most suitable LLM for your application involves considering several factors:

* **Task complexity**: More demanding or nuanced tasks generally benefit from more powerful models (e.g., OpenAI's GPT-4 series, Anthropic's Claude Sonnet 4, Google's Gemini 2.5 models)
* **Latency requirements**: For applications requiring real-time or near real-time responses, such as live voice conversations, models optimized for speed are preferable (e.g., Google's Gemini Flash series, Anthropic's Claude Haiku, OpenAI's GPT-4o-mini)
* **Context window size**: If your application needs to process, understand, or recall information from long conversations or extensive documents, select models with larger context windows
* **Cost-effectiveness**: Balance the desired performance and features against your budget. LLM prices can vary significantly, so analyze the pricing structure (input, output, and cache tokens) in relation to your expected usage patterns
* **HIPAA compliance**: If your application involves Protected Health Information (PHI), it is crucial to use an LLM that is designated as HIPAA compliant and ensure your entire data handling process meets regulatory standards

<Note>
  The maximum system prompt size is 2MB, which includes your agent's instructions, knowledge base
  content, and other system-level context.
</Note>


## Model configuration

### Temperature

Temperature controls the randomness of model responses. Lower values produce more consistent, focused outputs while higher values increase creativity and variation.

* **Low (0.0-0.3)**: Deterministic, consistent responses for structured interactions
* **Medium (0.4-0.7)**: Balanced creativity and consistency
* **High (0.8-1.0)**: Creative, varied responses for dynamic conversations

### Backup LLM configuration

Configure backup LLMs to ensure conversation continuity when the primary LLM fails or becomes unavailable.

**Configuration options:**

* **Default**: Uses ElevenLabs' recommended fallback sequence
* **Custom**: Define your own cascading sequence of backup models
* **Disabled**: No fallback (strongly discouraged for production)

<Warning>
  Disabling backup LLMs means conversations will end abruptly if your primary LLM fails or becomes
  unavailable. This is strongly discouraged for production use.
</Warning>

Learn more about [LLM cascading](/docs/agents-platform/customization/llm/llm-cascading).

### Thinking budget

Control how many internal reasoning tokens the model can use before responding. More tokens improve answer quality but slow down response time.

**Options:**

* **Disabled**: Fastest replies with no internal reasoning overhead
* **Low**: Minimal reasoning for quick responses
* **Medium**: Balanced reasoning and speed
* **High**: Maximum reasoning for complex queries

### Reasoning effort

Some models support configurable reasoning effort levels (None, Low, Medium, High).

**For conversational use-cases:**

Keep reasoning effort set to **None** to avoid the agent thinking too long, which can disrupt natural conversation flow.

**For workflow steps:**

Reasoning effort is perfect for workflow steps that require complex thought or decision-making where response time is less critical.


## Understanding pricing

* **Tokens**: LLM usage is typically billed based on the number of tokens processed. As a general guideline for English text, 100 tokens is approximately equivalent to 75 words
* **Input vs. output pricing**: Providers often differentiate pricing for input tokens (the data you send to the model) and output tokens (the data the model generates in response)
* **Cache pricing**:
  * `input_cache_read`: This refers to the cost associated with retrieving previously processed input data from a cache. Utilizing cached data can lead to cost savings if identical inputs are processed multiple times
  * `input_cache_write`: This is the cost associated with storing input data into a cache. Some LLM providers may charge for this operation
* The prices listed in this document are per 1 million tokens and are based on the information available at the time of writing. These prices are subject to change by the LLM providers

For the most accurate and current information on model capabilities, pricing, and terms of service, always consult the official documentation from the respective LLM providers (OpenAI, Google, Anthropic).


## HIPAA compliance

Certain LLMs available on our platform may be suitable for use in environments requiring HIPAA compliance, please see the [HIPAA compliance docs](/docs/agents-platform/legal/hipaa) for more details.


## Related resources

* [Custom LLM integration](/docs/agents-platform/customization/llm/custom-llm)
* [LLM cascading](/docs/agents-platform/guides/cascade)
* [Optimizing costs](/docs/agents-platform/customization/llm/optimising-cost)



# Workflows

> Build sophisticated conversation flows with visual graph-based workflows

<Frame background="subtle">
  <iframe width="100%" height="400" src="https://www.youtube.com/embed/7gtzXAaA82I" title="Agent Workflows Walkthrough" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen />
</Frame>


## Overview

Agent Workflows provide a powerful visual interface for designing complex conversation flows in Agents Platform. Instead of relying on linear conversation paths, workflows enable you to create sophisticated, branching conversation graphs that adapt dynamically to user needs.

<Frame background="subtle">
  ![Workflow Overview](file:df3ee9c0-7dac-4455-93c1-ddb9a0c732f4)
</Frame>


## Node types

Workflows are composed of different node types, each serving a specific purpose in your conversation flow.

<Frame background="subtle">
  ![Node Types](file:8a20f3a8-994c-4182-a866-25be100448d8)
</Frame>

### Subagent nodes

Subagent nodes allow you to modify agent behavior at specific points in your workflow. These modifications are applied on top of the base agent configuration, or can override the current agent's config completely, giving you fine-grained control over each conversation phase.
Any of an agent's configuration, tools available, and attached knowledge base items can be updated/overwitten.

<Tabs>
  <Tab title="General">
    <Frame background="subtle">
      <img src="file:6248b320-9700-44bf-b334-4d352295d770" alt="Subagent Extra Agent Config" />
    </Frame>

    Modify core agent settings for this specific node:

    * **System Prompt**: Append or override system instructions to guide agent behavior
    * **LLM Selection**: Choose a different language model (e.g., switch from Gemini 2.0 Flash to a more powerful model for complex reasoning tasks)
    * **Voice Configuration**: Change voice settings including speed, tone, or even switch to a different voice

    **Use Cases:**

    * Use a more powerful LLM for complex decision-making nodes
    * Apply stricter conversation guidelines during sensitive information gathering
    * Change voice characteristics for different conversation phases
    * Modify agent personality for specific interaction types
  </Tab>

  <Tab title="Knowledge Base">
    <Frame background="subtle">
      <img src="file:fe0fe4f1-50c0-4a02-adb9-ce70e25a01df" alt="Subagent Extra Knowledge Base" />
    </Frame>

    Add node-specific knowledge without affecting the global knowledge base:

    * **Include Global Knowledge Base**: Toggle whether to include the agent's main knowledge base
    * **Additional Documents**: Add documents specific to this conversation phase
    * **Dynamic Knowledge**: Inject contextual information based on workflow state

    **Use Cases:**

    * Add product-specific documentation during sales conversations
    * Include compliance guidelines during authentication
    * Provide troubleshooting guides for support flows
    * Add pricing information only after qualification
  </Tab>

  <Tab title="Tools">
    <Frame background="subtle">
      <img src="file:33720ab5-3756-4178-ba2c-ea16e9f084fd" alt="Subagent Extra Tools" />
    </Frame>

    Manage which tools are available to the agent at this node:

    * **Include Global Tools**: Toggle whether to include tools from the main agent configuration
    * **Additional Tools**: Add tools specific to this workflow node (e.g., webhook tools like `book_meeting`)
    * **Tool Type**: Specify whether tools are webhooks, API calls, or other integrations

    **Use Cases:**

    * Add authentication tools only after initial qualification
    * Enable payment processing tools at checkout nodes
    * Provide CRM access after user verification
    * Add scheduling tools for appointment booking phases
    * Include webhook tools for specific actions like booking meetings
  </Tab>
</Tabs>

### Dispatch tool node

Tool nodes execute a specific tool call during conversation flow. Unlike tools within subagents, tool nodes are dedicated execution points that guarantee the tool is called.

<Frame background="subtle">
  ![Tool Node Result Edges](file:cb05870e-cbdc-4458-a68e-98c87b0478f6)
</Frame>

**Special Edge Configuration:**
Tool nodes have a unique edge type that allows routing to a new node based on the tool execution result. You can define:

* **Success path**: Where to route when the tool executes successfully
* **Failure path**: Where to route when the tool fails or returns an error

In future, futher branching conditions will be provided.

### Agent transfer node

Agent transfer node facilitate handoffs the conversation between different conversational agents, learn more [here](/docs/agents-platform/customization/tools/system-tools/agent-transfer).

### Transfer to number node

Transfer to number nodes transitions from a conversation with an AI agent to a human agent via phone systems, learn more [here](/docs/agents-platform/customization/tools/system-tools/transfer-to-human)

### End node

End call nodes terminate the conversation flow gracefully, learn more [here](/docs/agents-platform/customization/tools/system-tools/transfer-to-human#:~:text=System%20tools-,End%20call,-Language%20detection)


## Edges and flow control

Edges define how conversations flow between nodes in your workflow. They support sophisticated routing logic that enables dynamic, context-aware conversation paths.

<Frame background="subtle">
  ![Workflow Edges](file:89c6ed40-9ba8-4b2b-9fed-08657a818774)
</Frame>

<Tabs>
  <Tab title="Forward Edges">
    Forward edges move the conversation to subsequent nodes in the workflow. They represent the primary flow of your conversation.

    <Frame background="subtle">
      ![Forward Edge Configuration](file:c27c92ea-eda7-41c0-b25c-874bc414be15)
    </Frame>
  </Tab>

  <Tab title="Backward Edges">
    Backward edges allow conversations to loop back to previous nodes, enabling iterative interactions and retry logic.

    <Frame background="subtle">
      ![Backward Edge Configuration](file:10d079a2-eb96-4d14-b9b1-726e07ec2ff1)
    </Frame>

    **Use Cases:**

    * Retry failed authentication attempts
    * Loop back for additional information gathering
    * Re-qualification after changes in user requirements
    * Iterative troubleshooting processes
  </Tab>
</Tabs>

<Tabs>
  <Tab title="LLM Condition">
    Use LLM conditions to create dynamic conversation flows based on natural language evaluation. The LLM evaluates conditions in real-time to determine the appropriate path.

    <Frame background="subtle">
      ![LLM Condition Agent Transfer](file:da569b57-16d5-443d-a255-59e87a0e60be)
    </Frame>

    **Configuration Options:**

    * **Label**: Human-readable description of the edge condition (not processed by LLM)
    * **LLM Condition**: Natural language condition evaluated by the LLM
  </Tab>

  <Tab title="Expression">
    Use expressions to create conditional logic based on variables and structured data.

    <Frame background="subtle">
      ![Expression Agent Transfer](file:a5a00849-bedb-456e-953e-224f255269b4)
    </Frame>

    **Configuration Options:**

    * **Label**: Human-readable description of the edge condition (not processed by LLM)
    * **Expression**: Deterministic evaluation criteria based on data structure
  </Tab>

  <Tab title="None">
    Unconditional transitions automatically move the conversation to the next node without any conditions.

    <Frame background="subtle">
      ![Unconditional Agent Transfer](file:f2482a97-3d51-4ae8-93dd-429eb9049f88)
    </Frame>

    **Use Cases:**

    * Sequential steps that always follow one another
    * Automatic progression after completing an action
    * Default fallback paths
  </Tab>
</Tabs>



# Conversation flow

> Configure how your assistant handles timeouts, interruptions, and turn-taking during conversations.


## Overview

Conversation flow settings determine how your assistant handles periods of user silence, interruptions during speech, and turn-taking behavior. These settings help create more natural conversations and can be customized based on your use case.

<CardGroup cols={3}>
  <Card title="Timeouts" icon="clock" href="#timeouts">
    Configure how long your assistant waits during periods of silence
  </Card>

  <Card title="Interruptions" icon="hand" href="#interruptions">
    Control whether users can interrupt your assistant while speaking
  </Card>

  <Card title="Turn eagerness" icon="arrows-turn-to-dots" href="#turn-eagerness">
    Adjust how quickly your assistant responds to user input
  </Card>
</CardGroup>


## Timeouts

Timeout handling determines how long your assistant will wait during periods of user silence before prompting for a response.

### Configuration

Timeout settings can be configured in the agent's **Advanced** tab under **Turn Timeout**.

The timeout duration is specified in seconds and determines how long the assistant will wait in silence before prompting the user. Turn timeouts must be between 1 and 30 seconds.

#### Example timeout settings

<Frame background="subtle">
  ![Timeout settings](file:536bca33-7afd-4e68-8898-409cb39be974)
</Frame>

<Note>
  Choose an appropriate timeout duration based on your use case. Shorter timeouts create more
  responsive conversations but may interrupt users who need more time to respond, leading to a less
  natural conversation.
</Note>

### Best practices for timeouts

* Set shorter timeouts (5-10 seconds) for casual conversations where quick back-and-forth is expected
* Use longer timeouts (10-30 seconds) when users may need more time to think or formulate complex responses
* Consider your user context - customer service may benefit from shorter timeouts while technical support may need longer ones


## Interruptions

Interruption handling determines whether users can interrupt your assistant while it's speaking.

### Configuration

Interruption settings can be configured in the agent's **Advanced** tab under **Client Events**.

To enable interruptions, make sure interruption is a selected client event.

#### Interruptions enabled

<Frame background="subtle">
  ![Interruption allowed](file:ea90e85b-6a21-4d98-8cc0-8005eb155885)
</Frame>

#### Interruptions disabled

<Frame background="subtle">
  ![Interruption ignored](file:cf0e5633-e3ce-4145-a054-b3d758ced0e0)
</Frame>

<Note>
  Disable interruptions when the complete delivery of information is crucial, such as legal
  disclaimers or safety instructions.
</Note>

### Best practices for interruptions

* Enable interruptions for natural conversational flows where back-and-forth dialogue is expected
* Disable interruptions when message completion is critical (e.g., terms and conditions, safety information)
* Consider your use case context - customer service may benefit from interruptions while information delivery may not


## Turn eagerness

Turn eagerness controls how quickly your assistant responds to user input during conversation. This setting determines how eager the assistant is to take turns and start speaking based on detected speech patterns.

### How it works

The assistant now includes two key improvements for more natural turn-taking:

1. **Faster response generation** - The assistant starts speaking after receiving enough words and a comma from the language model, rather than waiting for complete sentences. This reduces latency and creates more responsive conversations, especially when the assistant has longer responses.

2. **Configurable turn eagerness** - Control how quickly the assistant interprets pauses or speech patterns as opportunities to respond.

### Configuration

Turn eagerness can be configured in the dashboard Agent settings or via the [API](/docs/api-reference/agents/create#request.body.conversation_config.turn.turn_eagerness). Three modes are available:

* **Eager** - The assistant responds quickly to user input, jumping in at the earliest opportunity. Best for fast-paced conversations where immediate responses are valued.
* **Normal** - Balanced turn-taking that works well for most conversational scenarios. The assistant waits for natural conversation breaks before responding.
* **Patient** - The assistant waits longer before taking its turn, giving users more time to complete their thoughts. Ideal for collecting detailed information or when users need time to formulate responses.

<Note>
  Turn eagerness is especially powerful when combined with workflows. You can dynamically adjust the
  assistant's responsiveness based on context—making it jump in faster during casual conversation,
  or wait longer when collecting sensitive information like phone numbers or email addresses.
</Note>

### Best practices for turn eagerness

* Use **Eager** mode for customer service scenarios where quick responses improve user experience
* Use **Patient** mode when collecting structured information like phone numbers, addresses, or email addresses
* Use **Normal** mode as a default for general conversational flows
* Combine with workflows to dynamically adjust turn eagerness based on conversation context
* Test different settings with your specific use case to find the optimal balance


## Recommended configurations

<AccordionGroup>
  <Accordion title="Customer service">
    * Shorter timeouts (5-10 seconds) for responsive interactions - Enable interruptions to allow
      customers to interject with questions - **Eager** turn eagerness for quick, responsive
      conversations
  </Accordion>

  <Accordion title="Information collection">
    * Moderate timeouts (10-15 seconds) to allow users time to gather information - Enable
      interruptions for natural conversation flow - **Patient** turn eagerness when collecting phone
      numbers, addresses, or email addresses
  </Accordion>

  <Accordion title="Legal disclaimers">
    * Longer timeouts (15-30 seconds) to allow for complex responses - Disable interruptions to
      ensure full delivery of legal information - **Normal** turn eagerness to maintain steady pacing
  </Accordion>

  <Accordion title="Conversational EdTech">
    * Longer timeouts (10-30 seconds) to allow time to think and formulate responses - Enable
      interruptions to allow students to interject with questions - **Patient** turn eagerness to give
      students adequate time to respond
  </Accordion>
</AccordionGroup>



# Voice customization

> Learn how to customize your AI agent's voice and speech patterns.


## Overview

You can customize various aspects of your AI agent's voice to create a more natural and engaging conversation experience. This includes controlling pronunciation, speaking speed, and language-specific voice settings.


## Available customizations

<CardGroup cols={2}>
  <Card title="Multi-voice support" icon="microphone-lines" href="/docs/agents-platform/customization/voice/multi-voice-support">
    Enable your agent to switch between different voices for multi-character conversations,
    storytelling, and language tutoring.
  </Card>

  <Card title="Pronunciation dictionary" icon="microphone-stand" href="/docs/agents-platform/customization/voice/pronunciation-dictionary">
    Control how your agent pronounces specific words and phrases using
    [IPA](https://en.wikipedia.org/wiki/International_Phonetic_Alphabet) or
    [CMU](https://en.wikipedia.org/wiki/CMU_Pronouncing_Dictionary) notation.
  </Card>

  <Card title="Speed control" icon="waveform" href="/docs/agents-platform/customization/voice/speed-control">
    Adjust how quickly or slowly your agent speaks, with values ranging from 0.7x to 1.2x.
  </Card>

  <Card title="Language-specific voices" icon="language" href="/docs/agents-platform/customization/language">
    Configure different voices for each supported language to ensure natural pronunciation.
  </Card>
</CardGroup>


## Best practices

<AccordionGroup>
  <Accordion title="Voice selection">
    Choose voices that match your target language and region for the most natural pronunciation.
    Consider testing multiple voices to find the best fit for your use case.
  </Accordion>

  <Accordion title="Speed optimization">
    Start with the default speed (1.0) and adjust based on your specific needs. Test different
    speeds with your content to find the optimal balance between clarity and natural flow.
  </Accordion>

  <Accordion title="Pronunciation dictionaries">
    Focus on terms specific to your business or use case that need consistent pronunciation and are
    not widely used in everyday conversation. Test pronunciations with your chosen voice and model
    combination.
  </Accordion>
</AccordionGroup>

<Note>
  Some voice customization features may be model-dependent. For example, phoneme-based pronunciation
  control is only available with the Turbo v2 model.
</Note>



# Multi-voice support

> Enable your AI agent to switch between different voices for multi-character conversations and enhanced storytelling.


## Overview

Multi-voice support allows your ElevenLabs agent to dynamically switch between different ElevenLabs voices during a single conversation. This powerful feature enables:

* **Multi-character storytelling**: Different voices for different characters in narratives
* **Language tutoring**: Native speaker voices for different languages
* **Emotional agents**: Voice changes based on emotional context
* **Role-playing scenarios**: Distinct voices for different personas

<Frame background="subtle">
  <img src="file:93588e55-02f3-45ce-bc3f-b28a0f03c7d6" alt="Multi-voice configuration interface" />
</Frame>


## How it works

When multi-voice support is enabled, your agent can use XML-style markup to switch between configured voices during text generation. The agent automatically returns to the default voice when no specific voice is specified.

<CodeBlocks>
  ```xml title="Example voice switching"
  The teacher said, <spanish>¡Hola estudiantes!</spanish> 
  Then the student replied, <student>Hello! How are you today?</student>
  ```

  ```xml title="Multi-character dialogue"
  <narrator>Once upon a time, in a distant kingdom...</narrator>
  <princess>I need to find the magic crystal!</princess>
  <wizard>The crystal lies beyond the enchanted forest.</wizard>
  ```
</CodeBlocks>


## Configuration

### Adding supported voices

Navigate to your agent settings and locate the **Multi-voice support** section under the `Voice` tab.

<Steps>
  ### Add a new voice

  Click **Add voice** to configure a new supported voice for your agent.

  <Frame background="subtle">
    <img src="file:c8fbf24c-c041-4f80-9375-358028524a3f" alt="Multi-voice configuration interface" />
  </Frame>

  ### Configure voice properties

  Set up the voice with the following details:

  * **Voice label**: Unique identifier (e.g., "Joe", "Spanish", "Happy")
  * **Voice**: Select from your available ElevenLabs voices
  * **Model Family**: Choose Turbo, Flash, or Multilingual (optional)
  * **Language**: Override the default language for this voice (optional)
  * **Description**: When the agent should use this voice

  ### Save configuration

  Click **Add voice** to save the configuration. The voice will be available for your agent to use immediately.
</Steps>

### Voice properties

<AccordionGroup>
  <Accordion title="Voice label">
    A unique identifier that the LLM uses to reference this voice. Choose descriptive labels like: -
    Character names: "Alice", "Bob", "Narrator" - Languages: "Spanish", "French", "German" -
    Emotions: "Happy", "Sad", "Excited" - Roles: "Teacher", "Student", "Guide"
  </Accordion>

  <Accordion title="Model family">
    Override the agent's default model family for this specific voice: - **Flash**: Fastest eneration,
    optimized for real-time use - **Turbo**: Balanced speed and quality - **Multilingual**: Highest
    quality, best for non-English languages - **Same as agent**: Use agent's default setting
  </Accordion>

  <Accordion title="Language override">
    Specify a different language for this voice, useful for: - Multilingual conversations - Language
    tutoring applications - Region-specific pronunciations
  </Accordion>

  <Accordion title="Description">
    Provide context for when the agent should use this voice.
    Examples:

    * "For any Spanish words or phrases"
    * "When the message content is joyful or excited"
    * "Whenever the character Joe is speaking"
  </Accordion>
</AccordionGroup>


## Implementation

### XML markup syntax

Your agent uses XML-style tags to switch between voices:

```xml
<VOICE_LABEL>text to be spoken</VOICE_LABEL>
```

**Key points:**

* Replace `VOICE_LABEL` with the exact label you configured
* Text outside tags uses the default voice
* Tags are case-sensitive
* Nested tags are not supported

### System prompt integration

When you configure supported voices, the system automatically adds instructions to your agent's prompt:

```
When a message should be spoken by a particular person, use markup: "<CHARACTER>message</CHARACTER>" where CHARACTER is the character label.

Available voices are as follows:
- default: any text outside of the CHARACTER tags
- Joe: Whenever Joe is speaking
- Spanish: For any Spanish words or phrases
- Narrator: For narrative descriptions
```

### Example usage

<Tabs>
  <Tab title="Language tutoring">
    ```
    Teacher: Let's practice greetings. In Spanish, we say <Spanish>¡Hola! ¿Cómo estás?</Spanish>
    Student: How do I respond?
    Teacher: You can say <Spanish>¡Hola! Estoy bien, gracias.</Spanish> which means Hello! I'm fine, thank you.
    ```
  </Tab>

  <Tab title="Storytelling">
    ```
    Once upon a time, a brave princess ventured into a dark cave.
    <Princess>I'm not afraid of you, dragon!</Princess> she declared boldly. The dragon rumbled from
    the shadows, <Dragon>You should be, little one.</Dragon>
    But the princess stood her ground, ready for whatever came next.
    ```
  </Tab>
</Tabs>


## Best practices

<AccordionGroup>
  <Accordion title="Voice selection">
    * Choose voices that clearly differentiate between characters or contexts
    * Test voice combinations to ensure they work well together
    * Consider the emotional tone and personality for each voice
    * Ensure voices match the language and accent when switching languages
  </Accordion>

  <Accordion title="Label naming">
    * Use descriptive, intuitive labels that the LLM can understand
    * Keep labels short and memorable
    * Avoid special characters or spaces in labels
  </Accordion>

  <Accordion title="Performance optimization">
    * Limit the number of supported voices to what you actually need
    * Use the same model family when possible to reduce switching overhead
    * Test with your expected conversation patterns
    * Monitor response times with multiple voice switches
  </Accordion>

  <Accordion title="Content guidelines">
    * Provide clear descriptions for when each voice should be used
    * Test edge cases where voice switching might be unclear
    * Consider fallback behavior when voice labels are ambiguous
    * Ensure voice switches enhance rather than distract from the conversation
  </Accordion>
</AccordionGroup>


## Limitations

<Note>
  * Maximum of 10 supported voices per agent (including default)
  * Voice switching adds minimal latency during generation
  * XML tags must be properly formatted and closed
  * Voice labels are case-sensitive in markup
  * Nested voice tags are not supported
</Note>


## FAQ

<AccordionGroup>
  <Accordion title="What happens if I use an undefined voice label?">
    If the agent uses a voice label that hasn't been configured, the text will be spoken using the
    default voice. The XML tags will be ignored.
  </Accordion>

  <Accordion title="Can I change voices mid-sentence?">
    Yes, you can switch voices within a single response. Each tagged section will use the specified
    voice, while untagged text uses the default voice.
  </Accordion>

  <Accordion title="Do voice switches affect conversation latency?">
    Voice switching adds minimal overhead. The first use of each voice in a conversation may have
    slightly higher latency as the voice is initialized.
  </Accordion>

  <Accordion title="Can I use the same voice with different labels?">
    Yes, you can configure multiple labels that use the same ElevenLabs voice but with different model
    families, languages, or contexts.
  </Accordion>

  <Accordion title="How do I train my agent to use voice switching effectively?">
    Provide clear examples in your system prompt and test thoroughly. You can include specific
    scenarios where voice switching should occur and examples of the XML markup format.
  </Accordion>
</AccordionGroup>



# Pronunciation dictionaries

> Learn how to control how your AI agent pronounces specific words and phrases.


## Overview

Pronunciation dictionaries allow you to customize how your AI agent pronounces specific words or phrases. This is particularly useful for:

* Correcting pronunciation of names, places, or technical terms
* Ensuring consistent pronunciation across conversations
* Customizing regional pronunciation variations

<Frame background="subtle">
  <img src="file:f3ac4234-34a9-4095-8744-6af1acb1512a" alt="Pronunciation dictionary settings under the Voice tab" />
</Frame>


## Configuration

You can find the pronunciation dictionary settings under the **Voice** tab in your agent's configuration.

<Note>
  The phoneme function of pronunciation dictionaries only works with the Turbo v2 model, while the
  alias function works with all models.
</Note>


## Dictionary file format

Pronunciation dictionaries use XML-based `.pls` files. Here's an example structure:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<lexicon version="1.0"
      xmlns="http://www.w3.org/2005/01/pronunciation-lexicon"
      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      xsi:schemaLocation="http://www.w3.org/2005/01/pronunciation-lexicon
        http://www.w3.org/TR/2007/CR-pronunciation-lexicon-20071212/pls.xsd"
      alphabet="ipa" xml:lang="en-GB">
  <lexeme>
    <grapheme>Apple</grapheme>
    <phoneme>ˈæpl̩</phoneme>
  </lexeme>
  <lexeme>
    <grapheme>UN</grapheme>
    <alias>United Nations</alias>
  </lexeme>
</lexicon>
```


## Supported formats

We support two types of pronunciation notation:

1. **IPA (International Phonetic Alphabet)**

   * More precise control over pronunciation
   * Requires knowledge of IPA symbols
   * Example: "nginx" as `/ˈɛndʒɪnˈɛks/`

2. **CMU (Carnegie Mellon University) Dictionary format**
   * Simpler ASCII-based format
   * More accessible for English pronunciations
   * Example: "tomato" as "T AH M EY T OW"

<Tip>
  You can use AI tools like Claude or ChatGPT to help generate IPA or CMU notations for specific
  words.
</Tip>


## Best practices

1. **Case sensitivity**: Create separate entries for capitalized and lowercase versions of words if needed
2. **Testing**: Always test pronunciations with your chosen voice and model
3. **Maintenance**: Keep your dictionary organized and documented
4. **Scope**: Focus on words that are frequently mispronounced or critical to your use case


## FAQ

<AccordionGroup>
  <Accordion title="Which models support phoneme-based pronunciation?">
    Currently, only the Turbo v2 model supports phoneme-based pronunciation. Other models will
    silently skip phoneme entries.
  </Accordion>

  <Accordion title="Can I use multiple dictionaries?">
    Yes, you can upload multiple dictionary files to handle different sets of pronunciations.
  </Accordion>

  <Accordion title="What happens if a word isn't in the dictionary?">
    The model will use its default pronunciation rules for any words not specified in the
    dictionary.
  </Accordion>
</AccordionGroup>


## Additional resources

* [Professional Voice Cloning](/docs/product-guides/voices/voice-cloning/professional-voice-cloning)
* [Voice Design](/docs/product-guides/voices/voice-design)
* [Text to Speech API Reference](/docs/api-reference/text-to-speech)



# Speed control

> Learn how to adjust the speaking speed of your ElevenLabs agent.


## Overview

The speed control feature allows you to adjust how quickly or slowly your agent speaks. This can be useful for:

* Making speech more accessible for different audiences
* Matching specific use cases (e.g., slower for educational content)
* Optimizing for different types of conversations

<Frame background="subtle">
  <img src="file:125501c0-db4b-4554-a09c-aa587df7eeed" alt="Speed control settings under the Voice tab" />
</Frame>


## Configuration

Speed is controlled through the [`speed` parameter](/docs/api-reference/agents/create#request.body.conversation_config.tts.speed) with the following specifications:

* **Range**: 0.7 to 1.2
* **Default**: 1.0
* **Type**: Optional


## How it works

The speed parameter affects the pace of speech generation:

* Values below 1.0 slow down the speech
* Values above 1.0 speed up the speech
* 1.0 represents normal speaking speed

<Note>
  Extreme values near the minimum or maximum may affect the quality of the generated speech.
</Note>


## Best practices

* Start with the default speed (1.0) and adjust based on user feedback
* Test different speeds with your specific content
* Consider your target audience when setting the speed
* Monitor speech quality at extreme values

<Warning>
  Values outside the 0.7-1.2 range are not supported.
</Warning>



# Conversational voice design

> Learn how to design lifelike, engaging voices for ElevenLabs Agents


## Overview

Selecting the right voice is crucial for creating an effective voice agent. The voice you choose should align with your agent's personality, tone, and purpose.


## Voice design

If you need a voice that doesn't exist in our library, [Voice Design](/docs/product-guides/voices/voice-design) lets you create custom voices from text descriptions. Define characteristics like age, accent, tone, and pacing to generate voices tailored to your agent's personality and use case.


## Library voices

These voices offer a range of styles and characteristics that work well for different agent types:

* `kdmDKE6EkgrWrrykO9Qt` - **Alexandra:** A super realistic, young female voice that likes to chat
* `L0Dsvb3SLTyegXwtm47J` - **Archer:** Grounded and friendly young British male with charm
* `g6xIsTj2HwM6VR4iXFCw` - **Jessica Anne Bogart:** Empathetic and expressive, great for wellness coaches
* `OYTbf65OHHFELVut7v2H` - **Hope:** Bright and uplifting, perfect for positive interactions
* `dj3G1R1ilKoFKhBnWOzG` - **Eryn:** Friendly and relatable, ideal for casual interactions
* `HDA9tsk27wYi3uq0fPcK` - **Stuart:** Professional & friendly Aussie, ideal for technical assistance
* `1SM7GgM6IMuvQlz2BwM3` - **Mark:** Relaxed and laid back, suitable for non chalant chats
* `PT4nqlKZfc06VW1BuClj` - **Angela:** Raw and relatable, great listener and down to earth
* `vBKc2FfBKJfcZNyEt1n6` - **Finn:** Tenor pitched, excellent for podcasts and light chats
* `56AoDkrOh6qfVPDXZ7Pt` - **Cassidy:** Engaging and energetic, good for entertainment contexts
* `NOpBlnGInO9m6vDvFkFC` - **Grandpa Spuds Oxley:** Distinctive character voice for unique agents


## Voice settings

<Frame background="subtle">
  ![Voice settings](file:0b5f3a5a-f7b0-4ec3-ac2d-35e0c28d3b4d)
</Frame>

Voice settings dramatically affect how your agent is perceived:

* **Stability:** Lower values (0.30-0.50) create more emotional, dynamic delivery but may occasionally sound unstable. Higher values (0.60-0.85) produce more consistent but potentially monotonous output.

* **Similarity:** Higher values will boost the overall clarity and consistency of the voice. Very high values may lead to sound distortions. Adjusting this value to find the right balance is recommended.

* **Speed:** Most natural conversations occur at 0.9-1.1x speed. Depending on the voice, adjust slower for complex topics or faster for routine information.

<Tip>
  Test your agent with different voice settings using the same prompt to find the optimal
  combination. Small adjustments can dramatically change the perceived personality of your agent.
</Tip>



---
**Navigation:** [← Previous](./10-consolidated-billing.md) | [Index](./index.md) | [Next →](./12-language.md)
