**Navigation:** [← Previous](./11-build.md) | [Index](./index.md) | [Next →](./13-transfer-to-human.md)

# Language

> Learn how to configure your agent to speak multiple languages.


## Overview

This guide shows you how to configure your agent to speak multiple languages. You'll learn to:

* Configure your agent's primary language
* Add support for multiple languages
* Set language-specific voices and first messages
* Optimize voice selection for natural pronunciation
* Enable automatic language switching


## Guide

<Steps>
  <Step title="Default agent language">
    When you create a new agent, it's configured with:

    * English as the primary language
    * Flash v2 model for fast, English-only responses
    * A default first message.

    <Frame background="subtle">
      ![](file:19c7e1bf-dd35-4b76-8040-164e9e9007bc)
    </Frame>

    <Note>
      Additional languages switch the agent to use the v2.5 Multilingual model. English will always use
      the v2 model.
    </Note>
  </Step>

  <Step title="Add additional languages">
    First, navigate to your agent's configuration page and locate the **Agent** tab.

    1. In the **Additional Languages** add an additional language (e.g. French)
    2. Review the first message, which is automatically translated using a Large Language Model (LLM). Customize it as needed for each additional language to ensure accuracy and cultural relevance.

    <Frame background="subtle">
      ![](file:9465637d-313f-4a3e-9b6d-482e08d778e2)
    </Frame>

    <Note>
      Selecting the **All** option in the **Additional Languages** dropdown will configure the agent to
      support 31 languages. Collectively, these languages are spoken by approximately 90% of the world's
      population.
    </Note>
  </Step>

  <Step title="Configure language-specific voices">
    For optimal pronunciation, configure each additional language with a language-specific voice from our [Voice Library](https://elevenlabs.io/app/voice-library).

    <Note>
      To find great voices for each language curated by the ElevenLabs team, visit the [language top
      picks](https://elevenlabs.io/app/voice-library/collections).
    </Note>

    <Tabs>
      <Tab title="Language-specific voice settings">
        <Frame background="subtle">
          ![](file:7a65f94c-cac3-48fd-a706-4e9050f62418)
        </Frame>
      </Tab>

      <Tab title="Voice library">
        <Frame background="subtle">
          ![](file:55735420-a40e-4b28-857d-72e1edee7c16)
        </Frame>
      </Tab>
    </Tabs>
  </Step>

  <Step title="Enable language detection">
    Add the [language detection tool](/docs/agents-platform/customization/tools/system-tools/language-detection) to your agent can automatically switch to the user's preferred language.
  </Step>

  <Step title="Starting a call">
    Now that the agent is configured to support additional languages, the widget will prompt the user for their preferred language before the conversation begins.

    If using the SDK, the language can be set programmatically using conversation overrides. See the
    [Overrides](/docs/agents-platform/customization/personalization/overrides) guide for implementation details.

    <Frame background="subtle">
      ![](file:9f3adae0-6862-4078-8dc1-d9dc77e80175)
    </Frame>

    <Note>
      Language selection is fixed for the duration of the call - users cannot switch languages
      mid-conversation.
    </Note>
  </Step>
</Steps>

### Internationalization

You can integrate the widget with your internationalization framework by dynamically setting the language and UI text attributes.

```html title="Widget"
<elevenlabs-convai
  language="es"
  action-text={i18n["es"]["actionText"]}
  start-call-text={i18n["es"]["startCall"]}
  end-call-text={i18n["es"]["endCall"]}
  expand-text={i18n["es"]["expand"]}
  listening-text={i18n["es"]["listening"]}
  speaking-text={i18n["es"]["speaking"]}
></elevenlabs-convai>
```

<Note>
  Ensure the language codes match between your i18n framework and the agent's supported languages.
</Note>


## Best practices

<AccordionGroup>
  <Accordion title="Voice selection">
    Select voices specifically trained in your target languages. This ensures:

    * Natural pronunciation
    * Appropriate regional accents
    * Better handling of language-specific nuances
  </Accordion>

  <Accordion title="First message customization">
    While automatic translations are provided, consider:

    <div>
      * Reviewing translations for accuracy
      * Adapting greetings for cultural context
      * Adjusting formal/informal tone as needed
    </div>
  </Accordion>
</AccordionGroup>



# Knowledge base

> Enhance your conversational agent with custom knowledge.

**Knowledge bases** allow you to equip your agent with relevant, domain-specific information.


## Overview

A well-curated knowledge base helps your agent go beyond its pre-trained data and deliver context-aware answers.

Here are a few examples where knowledge bases can be useful:

* **Product catalogs**: Store product specifications, pricing, and other essential details.
* **HR or corporate policies**: Provide quick answers about vacation policies, employee benefits, or onboarding procedures.
* **Technical documentation**: Equip your agent with in-depth guides or API references to assist developers.
* **Customer FAQs**: Answer common inquiries consistently.

<Info>
  The agent on this page is configured with full knowledge of ElevenLabs' documentation and sitemap. Go ahead and ask it about anything about ElevenLabs.
</Info>


## Usage

<Tabs>
  <Tab title="Build a knowledge base via the API">
    <CodeBlocks>
      ```python
      # First create the document from text
      knowledge_base_document_text = elevenlabs.conversational_ai.knowledge_base.documents.create_from_text(
          text="The airspeed velocity of an unladen swallow (European) is 24 miles per hour or roughly 11 meters per second.",
          name="Unladen Swallow facts",
      )

      # Alternatively, you can create a document from a URL
      knowledge_base_document_url = elevenlabs.conversational_ai.knowledge_base.documents.create_from_url(
          url="https://en.wikipedia.org/wiki/Unladen_swallow",
          name="Unladen Swallow Wikipedia page",
      )

      # Or create a document from a file
      knowledge_base_document_file = elevenlabs.conversational_ai.knowledge_base.documents.create_from_file(
          file=open("/path/to/unladen-swallow-facts.txt", "rb"),
          name="Unladen Swallow Facts",
      )

      # Then add the document to the agent
      agent = elevenlabs.conversational_ai.agents.update(
          agent_id="agent-id",
          conversation_config={
              "agent": {
                  "prompt": {
                      "knowledge_base": [
                          {
                              "type": "text",
                              "name": knowledge_base_document_text.name,
                              "id": knowledge_base_document_text.id,
                          },
                          {
                              "type": "url",
                              "name": knowledge_base_document_url.name,
                              "id": knowledge_base_document_url.id,
                          },
                          {
                              "type": "file",
                              "name": knowledge_base_document_file.name,
                              "id": knowledge_base_document_file.id,
                          }
                      ]
                  }
              }
          },
      )

      print("Agent updated:", agent)
      ```

      ```typescript
      import fs from "node:fs";

      // First create the document from text
      const knowledgeBaseDocumentText = await elevenlabs.conversationalAi.knowledgeBase.documents.createFromText({
        name: "Unladen Swallow Facts",
        text: "The airspeed velocity of an unladen swallow (European) is 24 miles per hour or roughly 11 meters per second.",
      });

      // Alternatively, you can create a document from a URL
      const knowledgeBaseDocumentUrl = await elevenlabs.conversationalAi.knowledgeBase.documents.createFromUrl({
        name: "Unladen Swallow Facts",
        url: "https://en.wikipedia.org/wiki/Unladen_swallow",
      });

      // Or create a document from a file
      const fileBuffer = fs.readFileSync("/path/to/unladen-swallow-facts.txt");
      const file = new File([fileBuffer], "unladen-swallow-facts.txt", { type: "text/plain" });

      const knowledgeBaseDocumentFile = await elevenlabs.conversationalAi.knowledgeBase.documents.createFromFile({
        name: "Unladen Swallow Facts",
        file: file,
      });

      // Then add the document to the agent
      const agent = await elevenlabs.conversationalAi.agents.update("agent-id", {
          conversationConfig: {
              agent: {
                  prompt: {
                      knowledgeBase: [
                          {
                              type: "text",
                              name: knowledgeBaseDocumentText.name,
                              id: knowledgeBaseDocumentText.id,
                          },
                          {
                              type: "url",
                              name: knowledgeBaseDocumentUrl.name,
                              id: knowledgeBaseDocumentUrl.id,
                          },
                          {
                              type: "file",
                              name: knowledgeBaseDocumentFile.name,
                              id: knowledgeBaseDocumentFile.id,
                          }
                      ]
                  }
              }
          }
      });

      console.log("Agent updated:", agent);
      ```
    </CodeBlocks>
  </Tab>

  <Tab title="Build a knowledge base via the web dashboard">
    Files, URLs, and text can be added to the knowledge base in the dashboard.

    <Steps>
      <Step title="File">
        Upload files in formats like PDF, TXT, DOCX, HTML, and EPUB.

        <Frame background="subtle">
          ![File upload interface showing supported formats (PDF, TXT, DOCX, HTML, EPUB) with a 21MB
          size limit](file:e44d0eb9-b9e5-4f54-a760-9f09b11d1807)
        </Frame>
      </Step>

      <Step title="URL">
        Import URLs from sources like documentation and product pages.

        <Frame background="subtle">
          ![URL import interface where users can paste documentation
          links](file:675541a5-75ac-4114-b443-18b3663ef0b7)
        </Frame>

        <Note>
          When creating a knowledge base item from a URL, we do not currently support scraping all pages
          linked to from the initial URL, or continuously updating the knowledge base over time.
          However, these features are coming soon.
        </Note>

        <Warning>
          Ensure you have permission to use the content from the URLs you provide
        </Warning>
      </Step>

      <Step title="Text">
        Manually add text to the knowledge base.

        <Frame background="subtle">
          ![Text input interface where users can name and add custom
          content](file:a2f22b1d-e6fe-44c6-bfea-2743b6b4a8d8)
        </Frame>
      </Step>
    </Steps>
  </Tab>
</Tabs>


## Best practices

<h4>
  Content quality
</h4>

Provide clear, well-structured information that's relevant to your agent's purpose.

<h4>
  Size management
</h4>

Break large documents into smaller, focused pieces for better processing.

<h4>
  Regular updates
</h4>

Regularly review and update the agent's knowledge base to ensure the information remains current and accurate.

<h4>
  Identify knowledge gaps
</h4>

Review conversation transcripts to identify popular topics, queries and areas where users struggle to find information. Note any knowledge gaps and add the missing context to the knowledge base.


## Enterprise features

Non-enterprise accounts have a maximum of 20MB or 300k characters.

<Info>
  Need higher limits? [Contact our sales team](https://elevenlabs.io/contact-sales) to discuss
  enterprise plans with expanded knowledge base capabilities.
</Info>



# Knowledge base dashboard

> Learn how to manage and organize your knowledge base through the ElevenLabs dashboard


## Overview

The [knowledge base dashboard](https://elevenlabs.io/app/agents/knowledge-base) provides a centralized way to manage documents and track their usage across your AI agents. This guide explains how to navigate and use the knowledge base dashboard effectively.

<Frame background="subtle">
  ![Knowledge base main interface showing list of
  documents](file:5f22aaa4-243a-404d-b36c-5975c9b77f62)
</Frame>


## Adding existing documents to agents

When configuring an agent's knowledge base, you can easily add existing documents to an agent.

1. Navigate to the agent's [configuration](https://elevenlabs.io/app/agents/)
2. Click "Add document" in the knowledge base section of the "Agent" tab.
3. The option to select from your existing knowledge base documents or upload a new document will appear.

<Frame background="subtle">
  ![Interface for adding documents to an
  agent](file:463410de-dab8-48fd-aa50-d829472a02cc)
</Frame>

<Tip>
  Documents can be reused across multiple agents, making it efficient to maintain consistent
  knowledge across your workspace.
</Tip>


## Document dependencies

Each document in your knowledge base includes a "Agents" tab that shows which agents currently depend on that document.

<Frame background="subtle">
  ![Dependent agents tab showing which agents use a
  document](file:968e5efb-7fa1-49ac-bdfb-c41869dced3e)
</Frame>

It is not possible to delete a document if any agent depends on it.



# Retrieval-Augmented Generation

> Enhance your agent with large knowledge bases using RAG.


## Overview

**Retrieval-Augmented Generation (RAG)** enables your agent to access and use large knowledge bases during conversations. Instead of loading entire documents into the context window, RAG retrieves only the most relevant information for each user query, allowing your agent to:

* Access much larger knowledge bases than would fit in a prompt
* Provide more accurate, knowledge-grounded responses
* Reduce hallucinations by referencing source material
* Scale knowledge without creating multiple specialized agents

RAG is ideal for agents that need to reference large documents, technical manuals, or extensive
knowledge bases that would exceed the context window limits of traditional prompting.
RAG adds on slight latency to the response time of your agent, around 500ms.

<iframe width="100%" height="400" src="https://www.youtube-nocookie.com/embed/aFeJO7W0DIk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen />


## How RAG works

When RAG is enabled, your agent processes user queries through these steps:

1. **Query processing**: The user's question is analyzed and reformulated for optimal retrieval.
2. **Embedding generation**: The processed query is converted into a vector embedding that represents the user's question.
3. **Retrieval**: The system finds the most semantically similar content from your knowledge base.
4. **Response generation**: The agent generates a response using both the conversation context and the retrieved information.

This process ensures that relevant information to the user's query is passed to the LLM to generate a factually correct answer.


## Guide

### Prerequisites

* An [ElevenLabs account](https://elevenlabs.io)
* A configured ElevenLabs [Conversational Agent](/docs/agents-platform/quickstart)
* At least one document added to your agent's knowledge base

<Steps>
  <Step title="Enable RAG for your agent">
    In your agent's settings, navigate to the **Knowledge Base** section and toggle on the **Use RAG** option.

    <Frame background="subtle">
      <img src="file:55b6d5a1-7deb-4694-9f88-b8563798359f" alt="Toggle switch to enable RAG in the agent settings" />
    </Frame>
  </Step>

  <Step title="Configure RAG settings (optional)">
    After enabling RAG, you'll see additional configuration options in the **Advanced** tab:

    * **Embedding model**: Select the model that will convert text into vector embeddings
    * **Maximum document chunks**: Set the maximum amount of retrieved content per query
    * **Maximum vector distance**: Set the maximum distance between the query and the retrieved chunks

    These parameters could impact latency. They also could impact LLM cost.
    For example, retrieving more chunks increases cost.
    Increasing vector distance allows for more context to be passed, but potentially less relevant context.
    This may affect quality and you should experiment with different parameters to find the best results.

    <Frame background="subtle">
      <img src="file:a3cc7590-51b1-4428-ac6f-3a2f22efb90b" alt="RAG configuration options including embedding model selection" />
    </Frame>
  </Step>

  <Step title="Knowledge base indexing">
    Each document in your knowledge base needs to be indexed before it can be used with RAG. This
    process happens automatically when a document is added to an agent with RAG enabled.

    <Info>
      Indexing may take a few minutes for large documents. You can check the indexing status in the
      knowledge base list.
    </Info>
  </Step>

  <Step title="Configure document usage modes (optional)">
    For each document in your knowledge base, you can choose how it's used:

    * **Auto (default)**: The document is only retrieved when relevant to the query
    * **Prompt**: The document is always included in the system prompt, regardless of relevance, but can also be retrieved by RAG

    <Frame background="subtle">
      <img src="file:e167c8d0-d0fe-45db-a3c4-e419cb9291f9" alt="Document usage mode options in the knowledge base" />
    </Frame>

    <Warning>
      Setting too many documents to "Prompt" mode may exceed context limits. Use this option sparingly
      for critical information.
    </Warning>
  </Step>

  <Step title="Test your RAG-enabled agent">
    After saving your configuration, test your agent by asking questions related to your knowledge base. The agent should now be able to retrieve and reference specific information from your documents.
  </Step>
</Steps>


## Usage limits

To ensure fair resource allocation, ElevenLabs enforces limits on the total size of documents that can be indexed for RAG per workspace, based on subscription tier.

The limits are as follows:

| Subscription Tier | Total Document Size Limit | Notes                                                |
| :---------------- | :------------------------ | :--------------------------------------------------- |
| Free              | 1MB                       | Indexes may be deleted after inactivity.             |
| Starter           | 2MB                       |                                                      |
| Creator           | 20MB                      |                                                      |
| Pro               | 100MB                     |                                                      |
| Scale             | 500MB                     |                                                      |
| Business          | 1GB                       |                                                      |
| Enterprise        | 1GB                       | Higher limits available based on tier and agreement. |

**Note:**

* These limits apply to the total **original file size** of documents indexed for RAG, not the internal storage size of the RAG index itself (which can be significantly larger).
* Documents smaller than 500 bytes cannot be indexed for RAG and will automatically be used in the prompt instead.


## API implementation

You can also implement RAG through the [API](/docs/api-reference/knowledge-base/compute-rag-index):

<CodeBlocks>
  ```python
  from elevenlabs import ElevenLabs
  import time

  # Initialize the ElevenLabs client
  elevenlabs = ElevenLabs(api_key="your-api-key")

  # First, index a document for RAG
  document_id = "your-document-id"
  embedding_model = "e5_mistral_7b_instruct"

  # Trigger RAG indexing
  response = elevenlabs.conversational_ai.knowledge_base.document.compute_rag_index(
      documentation_id=document_id,
      model=embedding_model
  )

  # Check indexing status
  while response.status not in ["SUCCEEDED", "FAILED"]:
      time.sleep(5)  # Wait 5 seconds before checking status again
      response = elevenlabs.conversational_ai.knowledge_base.document.compute_rag_index(
          documentation_id=document_id,
          model=embedding_model
      )

  # Then update agent configuration to use RAG
  agent_id = "your-agent-id"

  # Get the current agent configuration
  agent_config = elevenlabs.conversational_ai.agents.get(agent_id=agent_id)

  # Enable RAG in the agent configuration
  agent_config.agent.prompt.rag = {
      "enabled": True,
      "embedding_model": "e5_mistral_7b_instruct",
      "max_documents_length": 10000
  }

  # Update document usage mode if needed
  for i, doc in enumerate(agent_config.agent.prompt.knowledge_base):
      if doc.id == document_id:
          agent_config.agent.prompt.knowledge_base[i].usage_mode = "auto"

  # Update the agent configuration
  elevenlabs.conversational_ai.agents.update(
      agent_id=agent_id,
      conversation_config=agent_config.agent
  )

  ```

  ```javascript
  // First, index a document for RAG
  async function enableRAG(documentId, agentId, apiKey) {
    try {
      // Initialize the ElevenLabs client
      const { ElevenLabs } = require('elevenlabs');
      const elevenlabs = new ElevenLabs({
        apiKey: apiKey,
      });

      // Start document indexing for RAG
      let response = await elevenlabs.conversationalAi.knowledgeBase.document.computeRagIndex(
        documentId,
        {
          model: 'e5_mistral_7b_instruct',
        }
      );

      // Check indexing status until completion
      while (response.status !== 'SUCCEEDED' && response.status !== 'FAILED') {
        await new Promise((resolve) => setTimeout(resolve, 5000)); // Wait 5 seconds
        response = await elevenlabs.conversationalAi.knowledgeBase.document.computeRagIndex(
          documentId,
          {
            model: 'e5_mistral_7b_instruct',
          }
        );
      }

      if (response.status === 'FAILED') {
        throw new Error('RAG indexing failed');
      }

      // Get current agent configuration
      const agentConfig = await elevenlabs.conversationalAi.agents.get(agentId);

      // Enable RAG in the agent configuration
      const updatedConfig = {
        conversation_config: {
          ...agentConfig.agent,
          prompt: {
            ...agentConfig.agent.prompt,
            rag: {
              enabled: true,
              embedding_model: 'e5_mistral_7b_instruct',
              max_documents_length: 10000,
            },
          },
        },
      };

      // Update document usage mode if needed
      if (agentConfig.agent.prompt.knowledge_base) {
        agentConfig.agent.prompt.knowledge_base.forEach((doc, index) => {
          if (doc.id === documentId) {
            updatedConfig.conversation_config.prompt.knowledge_base[index].usage_mode = 'auto';
          }
        });
      }

      // Update the agent configuration
      await elevenlabs.conversationalAi.agents.update(agentId, updatedConfig);

      console.log('RAG configuration updated successfully');
      return true;
    } catch (error) {
      console.error('Error configuring RAG:', error);
      throw error;
    }
  }

  // Example usage
  // enableRAG('your-document-id', 'your-agent-id', 'your-api-key')
  //   .then(() => console.log('RAG setup complete'))
  //   .catch(err => console.error('Error:', err));
  ```
</CodeBlocks>



# Tools

> Enhance ElevenLabs agents with custom functionalities and external integrations.


## Overview

Tools allow ElevenLabs agents to perform actions beyond generating text responses.
They enable agents to interact with external systems, execute custom logic, or access specific functionalities during a conversation.
This allows for richer, more capable interactions tailored to specific use cases.

ElevenLabs Agents supports the following kinds of tools:

<CardGroup cols={2}>
  <Card title="Client Tools" href="/agents-platform/customization/tools/client-tools" icon="rectangle-code">
    Tools executed directly on the client-side application (e.g., web browser, mobile app).
  </Card>

  <Card title="Server Tools" href="/agents-platform/customization/tools/server-tools" icon="server">
    Custom tools executed on your server-side infrastructure via API calls.
  </Card>

  <Card title="MCP Tools" href="/agents-platform/customization/mcp" icon="plug">
    Model Context Protocol servers that provide tools and resources to agents.
  </Card>

  <Card title="System Tools" href="/agents-platform/customization/tools/system-tools" icon="computer-classic">
    Built-in tools provided by the platform for common actions.
  </Card>
</CardGroup>



# Client tools

> Empower your assistant to trigger client-side operations.

**Client tools** enable your assistant to execute client-side functions. Unlike [server-side tools](/docs/agents-platform/customization/tools), client tools allow the assistant to perform actions such as triggering browser events, running client-side functions, or sending notifications to a UI.

<iframe width="100%" height="400" src="https://www.youtube-nocookie.com/embed/XeDT92mR7oE?rel=0&autoplay=0" title="YouTube video player" frameborder="0" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen />


## Overview

Applications may require assistants to interact directly with the user's environment. Client-side tools give your assistant the ability to perform client-side operations.

Here are a few examples where client tools can be useful:

* **Triggering UI events**: Allow an assistant to trigger browser events, such as alerts, modals or notifications.
* **Interacting with the DOM**: Enable an assistant to manipulate the Document Object Model (DOM) for dynamic content updates or to guide users through complex interfaces.

<Info>
  To perform operations server-side, use
  [server-tools](/docs/agents-platform/customization/tools/server-tools) instead.
</Info>


## Guide

### Prerequisites

* An [ElevenLabs account](https://elevenlabs.io)
* A configured ElevenLabs Conversational Agent ([create one here](https://elevenlabs.io/app/agents))

<Steps>
  <Step title="Create a new client-side tool">
    Navigate to your agent dashboard. In the **Tools** section, click **Add Tool**. Ensure the **Tool Type** is set to **Client**. Then configure the following:

    | Setting     | Parameter                                                        |
    | ----------- | ---------------------------------------------------------------- |
    | Name        | logMessage                                                       |
    | Description | Use this client-side tool to log a message to the user's client. |

    Then create a new parameter `message` with the following configuration:

    | Setting     | Parameter                                                                          |
    | ----------- | ---------------------------------------------------------------------------------- |
    | Data Type   | String                                                                             |
    | Identifier  | message                                                                            |
    | Required    | true                                                                               |
    | Description | The message to log in the console. Ensure the message is informative and relevant. |

    <Frame background="subtle">
      ![logMessage client-tool setup](file:2e58f181-2923-4efd-b64a-ad99a294ef1d)
    </Frame>
  </Step>

  <Step title="Register the client tool in your code">
    Unlike server-side tools, client tools need to be registered in your code.

    Use the following code to register the client tool:

    <CodeBlocks>
      ```python title="Python" focus={4-16}
      from elevenlabs import ElevenLabs
      from elevenlabs.conversational_ai.conversation import Conversation, ClientTools

      def log_message(parameters):
          message = parameters.get("message")
          print(message)

      client_tools = ClientTools()
      client_tools.register("logMessage", log_message)

      conversation = Conversation(
          client=ElevenLabs(api_key="your-api-key"),
          agent_id="your-agent-id",
          client_tools=client_tools,
          # ...
      )

      conversation.start_session()
      ```

      ```javascript title="JavaScript" focus={2-10}
      // ...
      const conversation = await Conversation.startSession({
        // ...
        clientTools: {
          logMessage: async ({message}) => {
            console.log(message);
          }
        },
        // ...
      });
      ```

      ```swift title="Swift" focus={2-10}
      // ...
      var clientTools = ElevenLabsSDK.ClientTools()

      clientTools.register("logMessage") { parameters async throws -> String? in
          guard let message = parameters["message"] as? String else {
              throw ElevenLabsSDK.ClientToolError.invalidParameters
          }
          print(message)
          return message
      }
      ```
    </CodeBlocks>

    <Note>
      The tool and parameter names in the agent configuration are case-sensitive and **must** match those registered in your code.
    </Note>
  </Step>

  <Step title="Testing">
    Initiate a conversation with your agent and say something like:

    > *Log a message to the console that says Hello World*

    You should see a `Hello World` log appear in your console.
  </Step>

  <Step title="Next steps">
    Now that you've set up a basic client-side event, you can:

    * Explore more complex client tools like opening modals, navigating to pages, or interacting with the DOM.
    * Combine client tools with server-side webhooks for full-stack interactions.
    * Use client tools to enhance user engagement and provide real-time feedback during conversations.
  </Step>
</Steps>

### Passing client tool results to the conversation context

When you want your agent to receive data back from a client tool, ensure that you tick the **Wait for response** option in the tool configuration.

<Frame background="subtle">
  <img src="file:9d4e9558-df69-46f0-939e-7415a0741e5a" alt="Wait for response option in client tool configuration" />
</Frame>

Once the client tool is added, when the function is called the agent will wait for its response and append the response to the conversation context.

<CodeBlocks>
  ```python title="Python"
  def get_customer_details():
      # Fetch customer details (e.g., from an API or database)
      customer_data = {
          "id": 123,
          "name": "Alice",
          "subscription": "Pro"
      }
      # Return the customer data; it can also be a JSON string if needed.
      return customer_data

  client_tools = ClientTools()
  client_tools.register("getCustomerDetails", get_customer_details)

  conversation = Conversation(
      client=ElevenLabs(api_key="your-api-key"),
      agent_id="your-agent-id",
      client_tools=client_tools,
      # ...
  )

  conversation.start_session()
  ```

  ```javascript title="JavaScript"
  const clientTools = {
    getCustomerDetails: async () => {
      // Fetch customer details (e.g., from an API)
      const customerData = {
        id: 123,
        name: "Alice",
        subscription: "Pro"
      };
      // Return data directly to the agent.
      return customerData;
    }
  };

  // Start the conversation with client tools configured.
  const conversation = await Conversation.startSession({ clientTools });
  ```
</CodeBlocks>

In this example, when the agent calls **getCustomerDetails**, the function will execute on the client and the agent will receive the returned data, which is then used as part of the conversation context. The values from the response can also optionally be assigned to dynamic variables, similar to [server tools](https://elevenlabs.io/docs/agents-platform/customization/tools/server-tools). Note system tools cannot update dynamic variables.

### Troubleshooting

<AccordionGroup>
  <Accordion title="Tools not being triggered">
    * Ensure the tool and parameter names in the agent configuration match those registered in your code.
    * View the conversation transcript in the agent dashboard to verify the tool is being executed.
  </Accordion>

  <Accordion title="Console errors">
    * Open the browser console to check for any errors.
    * Ensure that your code has necessary error handling for undefined or unexpected parameters.
  </Accordion>
</AccordionGroup>


## Best practices

<h4>
  Name tools intuitively, with detailed descriptions
</h4>

If you find the assistant does not make calls to the correct tools, you may need to update your tool names and descriptions so the assistant more clearly understands when it should select each tool. Avoid using abbreviations or acronyms to shorten tool and argument names.

You can also include detailed descriptions for when a tool should be called. For complex tools, you should include descriptions for each of the arguments to help the assistant know what it needs to ask the user to collect that argument.

<h4>
  Name tool parameters intuitively, with detailed descriptions
</h4>

Use clear and descriptive names for tool parameters. If applicable, specify the expected format for a parameter in the description (e.g., YYYY-mm-dd or dd/mm/yy for a date).

<h4>
  Consider providing additional information about how and when to call tools in your assistant's
  system prompt
</h4>

Providing clear instructions in your system prompt can significantly improve the assistant's tool calling accuracy. For example, guide the assistant with instructions like the following:

```plaintext
Use `check_order_status` when the user inquires about the status of their order, such as 'Where is my order?' or 'Has my order shipped yet?'.
```

Provide context for complex scenarios. For example:

```plaintext
Before scheduling a meeting with `schedule_meeting`, check the user's calendar for availability using check_availability to avoid conflicts.
```

<h4>
  LLM selection
</h4>

<Warning>
  When using tools, we recommend picking high intelligence models like GPT-4o mini or Claude 3.5
  Sonnet and avoiding Gemini 1.5 Flash.
</Warning>

It's important to note that the choice of LLM matters to the success of function calls. Some LLMs can struggle with extracting the relevant parameters from the conversation.



# Server tools

> Connect your assistant to external data & systems.

**Tools** enable your assistant to connect to external data and systems. You can define a set of tools that the assistant has access to, and the assistant will use them where appropriate based on the conversation.

<iframe width="100%" height="400" src="https://www.youtube-nocookie.com/embed/pB33QxKN8P8?rel=0&autoplay=0" title="YouTube video player" frameborder="0" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen />


## Overview

Many applications require assistants to call external APIs to get real-time information. Tools give your assistant the ability to make external function calls to third party apps so you can get real-time information.

Here are a few examples where tools can be useful:

* **Fetching data**: enable an assistant to retrieve real-time data from any REST-enabled database or 3rd party integration before responding to the user.
* **Taking action**: allow an assistant to trigger authenticated actions based on the conversation, like scheduling meetings or initiating order returns.

<Info>
  To interact with Application UIs or trigger client-side events use [client
  tools](/docs/agents-platform/customization/tools/client-tools) instead.
</Info>


## Tool configuration

ElevenLabs agents can be equipped with tools to interact with external APIs. Unlike traditional requests, the assistant generates query, body, and path parameters dynamically based on the conversation and parameter descriptions you provide.

All tool configurations and parameter descriptions help the assistant determine **when** and **how** to use these tools. To orchestrate tool usage effectively, update the assistant’s system prompt to specify the sequence and logic for making these calls. This includes:

* **Which tool** to use and under what conditions.
* **What parameters** the tool needs to function properly.
* **How to handle** the responses.

<br />

<Tabs>
  <Tab title="Configuration">
    Define a high-level `Name` and `Description` to describe the tool's purpose. This helps the LLM understand the tool and know when to call it.

    <Info>
      If the API requires path parameters, include variables in the URL path by wrapping them in curly
      braces `{}`, for example: `/api/resource/{id}` where `id` is a path parameter.
    </Info>

    <Frame background="subtle">
      ![Configuration](file:c47ec826-fbac-431e-8c3f-9049e175daea)
    </Frame>
  </Tab>

  <Tab title="Authentication">
    Configure authentication by adding custom headers or using out-of-the-box authentication methods through auth connections.

    <Frame background="subtle">
      ![Tool authentication](file:fc240495-be6d-45ce-a4b9-a0a8ab041f54)
    </Frame>
  </Tab>

  <Tab title="Headers">
    Specify any headers that need to be included in the request.

    <Frame background="subtle">
      ![Headers](file:e761fe00-7b05-4a93-944e-bfd635715f30)
    </Frame>
  </Tab>

  <Tab title="Path parameters">
    Include variables in the URL path by wrapping them in curly braces `{}`:

    * **Example**: `/api/resource/{id}` where `id` is a path parameter.

    <Frame background="subtle">
      ![Path parameters](file:109d6f23-22c1-4e53-9fd5-402e46554df2)
    </Frame>
  </Tab>

  <Tab title="Body parameters">
    Specify any body parameters to be included in the request.

    <Frame background="subtle">
      ![Body parameters](file:5a9f38b9-f4ab-4e74-9134-5c04a1dd290d)
    </Frame>
  </Tab>

  <Tab title="Query parameters">
    Specify any query parameters to be included in the request.

    <Frame background="subtle">
      ![Query parameters](file:e97e62f4-4c8b-4ac6-af85-e25148fff816)
    </Frame>
  </Tab>

  <Tab title="Dynamic variable assignment">
    Specify dynamic variables to update from the tool response for later use in the conversation.

    <Frame background="subtle">
      ![Query parameters](file:15c11196-7709-4346-9d58-b4b735c82582)
    </Frame>
  </Tab>
</Tabs>


## Guide

In this guide, we'll create a weather assistant that can provide real-time weather information for any location. The assistant will use its geographic knowledge to convert location names into coordinates and fetch accurate weather data.

<div>
  <iframe src="https://player.vimeo.com/video/1061374724?h=bd9bdb535e&badge=0&autopause=0&player_id=0&app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write; encrypted-media" title="weatheragent" />
</div>

<Steps>
  <Step title="Configure the weather tool">
    First, on the **Agent** section of your agent settings page, choose **Add Tool**. Select **Webhook** as the Tool Type, then configure the weather API integration:

    <AccordionGroup>
      <Accordion title="Weather Tool Configuration">
        <Tabs>
          <Tab title="Configuration">
            | Field       | Value                                                                                                                                                                                                                                                                                                                                                                                  |
            | ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
            | Name        | get\_weather                                                                                                                                                                                                                                                                                                                                                                           |
            | Description | Gets the current weather forecast for a location                                                                                                                                                                                                                                                                                                                                       |
            | Method      | GET                                                                                                                                                                                                                                                                                                                                                                                    |
            | URL         | [https://api.open-meteo.com/v1/forecast?latitude=\{latitude}\&longitude=\{longitude}\&current=temperature\_2m,wind\_speed\_10m\&hourly=temperature\_2m,relative\_humidity\_2m,wind\_speed\_10m](https://api.open-meteo.com/v1/forecast?latitude=\{latitude}\&longitude=\{longitude}\&current=temperature_2m,wind_speed_10m\&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m) |
          </Tab>

          <Tab title="Path Parameters">
            | Data Type | Identifier | Value Type | Description                                         |
            | --------- | ---------- | ---------- | --------------------------------------------------- |
            | string    | latitude   | LLM Prompt | The latitude coordinate for the requested location  |
            | string    | longitude  | LLM Prompt | The longitude coordinate for the requested location |
          </Tab>
        </Tabs>
      </Accordion>
    </AccordionGroup>

    <Warning>
      An API key is not required for this tool. If one is required, this should be passed in the headers and stored as a secret.
    </Warning>
  </Step>

  <Step title="Orchestration">
    Configure your assistant to handle weather queries intelligently with this system prompt:

    ```plaintext System prompt
    You are a helpful conversational agent with access to a weather tool. When users ask about
    weather conditions, use the get_weather tool to fetch accurate, real-time data. The tool requires
    a latitude and longitude - use your geographic knowledge to convert location names to coordinates
    accurately.

    Never ask users for coordinates - you must determine these yourself. Always report weather
    information conversationally, referring to locations by name only. For weather requests:

    1. Extract the location from the user's message
    2. Convert the location to coordinates and call get_weather
    3. Present the information naturally and helpfully

    For non-weather queries, provide friendly assistance within your knowledge boundaries. Always be
    concise, accurate, and helpful.

    First message: "Hey, how can I help you today?"
    ```

    <Success>
      Test your assistant by asking about the weather in different locations. The assistant should
      handle specific locations ("What's the weather in Tokyo?") and ask for clarification after general queries ("How's
      the weather looking today?").
    </Success>
  </Step>
</Steps>


## Supported Authentication Methods

ElevenLabs Agents supports multiple authentication methods to securely connect your tools with external APIs. Authentication methods are configured in your agent settings and then connected to individual tools as needed.

<Frame background="subtle">
  ![Workspace Auth Connection](file:791c1e65-b9c4-4356-b8e9-1bbba87f58d9)
</Frame>

Once configured, you can connect these authentication methods to your tools and manage custom headers in the tool configuration:

<Frame background="subtle">
  ![Tool Auth Connection](file:cfc46c1f-c979-4dd9-95ec-750814c8f15b)
</Frame>

#### OAuth2 Client Credentials

Automatically handles the OAuth2 client credentials flow. Configure with your client ID, client secret, and token URL (e.g., `https://api.example.com/oauth/token`). Optionally specify scopes as comma-separated values and additional JSON parameters. Set up by clicking **Add Auth** on **Workspace Auth Connections** on the **Agent** section of your agent settings page.

#### OAuth2 JWT

Uses JSON Web Token authentication for OAuth 2.0 JWT Bearer flow. Requires your JWT signing secret, token URL, and algorithm (default: HS256). Configure JWT claims including issuer, audience, and subject. Optionally set key ID, expiration (default: 3600 seconds), scopes, and extra parameters. Set up by clicking **Add Auth** on **Workspace Auth Connections** on the **Agent** section of your agent settings page.

#### Basic Authentication

Simple username and password authentication for APIs that support HTTP Basic Auth. Set up by clicking **Add Auth** on **Workspace Auth Connections** in the **Agent** section of your agent settings page.

#### Bearer Tokens

Token-based authentication that adds your bearer token value to the request header. Configure by adding a header to the tool configuration, selecting **Secret** as the header type, and clicking **Create New Secret**.

#### Custom Headers

Add custom authentication headers with any name and value for proprietary authentication methods. Configure by adding a header to the tool configuration and specifying its **name** and **value**.


## Best practices

<h4>
  Name tools intuitively, with detailed descriptions
</h4>

If you find the assistant does not make calls to the correct tools, you may need to update your tool names and descriptions so the assistant more clearly understands when it should select each tool. Avoid using abbreviations or acronyms to shorten tool and argument names.

You can also include detailed descriptions for when a tool should be called. For complex tools, you should include descriptions for each of the arguments to help the assistant know what it needs to ask the user to collect that argument.

<h4>
  Name tool parameters intuitively, with detailed descriptions
</h4>

Use clear and descriptive names for tool parameters. If applicable, specify the expected format for a parameter in the description (e.g., YYYY-mm-dd or dd/mm/yy for a date).

<h4>
  Consider providing additional information about how and when to call tools in your assistant's
  system prompt
</h4>

Providing clear instructions in your system prompt can significantly improve the assistant's tool calling accuracy. For example, guide the assistant with instructions like the following:

```plaintext
Use `check_order_status` when the user inquires about the status of their order, such as 'Where is my order?' or 'Has my order shipped yet?'.
```

Provide context for complex scenarios. For example:

```plaintext
Before scheduling a meeting with `schedule_meeting`, check the user's calendar for availability using check_availability to avoid conflicts.
```

<h4>
  LLM selection
</h4>

<Warning>
  When using tools, we recommend picking high intelligence models like GPT-4o mini or Claude 3.5
  Sonnet and avoiding Gemini 1.5 Flash.
</Warning>

It's important to note that the choice of LLM matters to the success of function calls. Some LLMs can struggle with extracting the relevant parameters from the conversation.



# Model Context Protocol

> Connect your ElevenLabs conversational agents to external tools and data sources using the Model Context Protocol.

<Error title="User Responsibility">
  You are responsible for the security, compliance, and behavior of any third-party MCP server you
  integrate with your ElevenLabs conversational agents. ElevenLabs provides the platform for
  integration but does not manage, endorse, or secure external MCP servers.
</Error>


## Overview

The [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) is an open standard that defines how applications provide context to Large Language Models (LLMs). Think of MCP as a universal connector that enables AI models to seamlessly interact with diverse data sources and tools. By integrating servers that implement MCP, you can significantly extend the capabilities of your ElevenLabs conversational agents.

<Frame background="subtle">
  <iframe width="100%" height="400" src="https://www.youtube.com/embed/m1HgNvafID8" title="ElevenLabs Model Context Protocol integration" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />
</Frame>

<Note>
  MCP support is not currently available for users on Zero Retention Mode or those requiring HIPAA
  compliance.
</Note>

ElevenLabs allows you to connect your conversational agents to external MCP servers. This enables your agents to:

* Access and process information from various data sources via the MCP server
* Utilize specialized tools and functionalities exposed by the MCP server
* Create more dynamic, knowledgeable, and interactive conversational experiences


## Getting started

<Note>
  ElevenLabs supports both SSE (Server-Sent Events) and HTTP streamable transport MCP servers.
</Note>

1. Retrieve the URL of your MCP server. In this example, we'll use [Zapier MCP](https://zapier.com/mcp), which lets you connect Agents Platform to hundreds of tools and services.

2. Navigate to the [MCP server integrations dashboard](https://elevenlabs.io/app/agents/integrations) and click "Add Custom MCP Server".

   <Frame background="subtle">
     ![Creating your first MCP server](file:c6395b1a-d093-4f09-b0d3-f98a6539fbfd)
   </Frame>

3. Configure the MCP server with the following details:

   * **Name**: The name of the MCP server (e.g., "Zapier MCP Server")
   * **Description**: A description of what the MCP server can do (e.g., "An MCP server with access to Zapier's tools and services")
   * **Server URL**: The URL of the MCP server. In some cases this contains a secret key, treat it like a password and store it securely as a workspace secret.
   * **Secret Token (Optional)**: If the MCP server requires a secret token (Authorization header), enter it here.
   * **HTTP Headers (Optional)**: If the MCP server requires additional HTTP headers, enter them here.

4. Click "Add Integration" to save the integration and test the connection to list available tools.

   <Frame background="subtle">
     ![Zapier example tools](file:b99ebebe-48d0-485a-bde3-68acadf70e76)
   </Frame>

5. The MCP server is now available to add to your agents. MCP support is available for both public and private agents.

   <Frame background="subtle">
     ![Adding the MCP server to an agent](file:a71e132c-a66e-4bcf-88d6-a40f7a0f0823)
   </Frame>


## Tool approval modes

ElevenLabs provides flexible approval controls to manage how agents request permission to use tools from MCP servers. You can configure approval settings at both the MCP server level and individual tool level for maximum security control.

<Frame background="subtle">
  ![Tool approval mode settings](file:9eb1f735-761a-4c47-9df2-a14dd31d5bc6)
</Frame>

### Available approval modes

* **Always Ask (Recommended)**: Maximum security. The agent will request your permission before each tool use.
* **Fine-Grained Tool Approval**: Disable and pre-select tools which can run automatically and those requiring approval.
* **No Approval**: The assistant can use any tool without approval.

### Fine-grained tool control

The Fine-Grained Tool Approval mode allows you to configure individual tools with different approval requirements, giving you precise control over which tools can run automatically and which require explicit permission.

<Frame background="subtle">
  ![Fine-grained tool approval
  settings](file:425d60c1-cbaf-49db-96f4-9f7b120e6cfa)
</Frame>

For each tool, you can set:

* **Auto-approved**: Tool runs automatically without requiring permission
* **Requires approval**: Tool requires explicit permission before execution
* **Disabled**: Tool is completely disabled and cannot be used

<Tip>
  Use Fine-Grained Tool Approval to allow low-risk read-only tools to run automatically while
  requiring approval for tools that modify data or perform sensitive operations.
</Tip>


## Key considerations for ElevenLabs integration

* **External servers**: You are responsible for selecting the external MCP servers you wish to integrate. ElevenLabs provides the means to connect to them.
* **Supported features**: ElevenLabs supports MCP servers that communicate over SSE (Server-Sent Events) and HTTP streamable transports for real-time interactions.
* **Dynamic tools**: The tools and capabilities available from an integrated MCP server are defined by that external server and can change if the server's configuration is updated.


## Security and disclaimer

Integrating external MCP servers can expose your agents and data to third-party services. It is crucial to understand the security implications.

<Warning title="Important Disclaimer">
  By enabling MCP server integrations, you acknowledge that this may involve data sharing with
  third-party services not controlled by ElevenLabs. This could incur additional security risks.
  Please ensure you fully understand the implications, vet the security of any MCP server you
  integrate, and review our [MCP Integration Security
  Guidelines](/docs/agents-platform/customization/mcp/security) before proceeding.
</Warning>

Refer to our [MCP Integration Security Guidelines](/docs/agents-platform/customization/mcp/security) for detailed best practices.


## Finding or building MCP servers

* Utilize publicly available MCP servers from trusted providers
* Develop your own MCP server to expose your proprietary data or tools
* Explore the Model Context Protocol community and resources for examples and server implementations

### Resources

* [Anthropic's MCP server examples](https://docs.anthropic.com/en/docs/agents-and-tools/remote-mcp-servers#remote-mcp-server-examples) - A list of example servers by Anthropic
* [Awesome Remote MCP Servers](https://github.com/jaw9c/awesome-remote-mcp-servers) - A curated, open-source list of remote MCP servers
* [Remote MCP Server Directory](https://remote-mcp.com/) - A searchable list of Remote MCP servers



# MCP integration security

> Tips for securely integrating third-party Model Context Protocol servers with your ElevenLabs conversational agents.

<Error title="User Responsibility">
  You are responsible for the security, compliance, and behavior of any third-party MCP server you
  integrate with your ElevenLabs conversational agents. ElevenLabs provides the platform for
  integration but does not manage, endorse, or secure external MCP servers.
</Error>


## Overview

Integrating external servers via the Model Context Protocol (MCP) can greatly enhance your ElevenLabs conversational agents. However, this also means connecting to systems outside of ElevenLabs' direct control, which introduces important security considerations. As a user, you are responsible for the security and trustworthiness of any third-party MCP server you choose to integrate.

This guide outlines key security practices to consider when using MCP server integrations within ElevenLabs.


## Tool approval controls

ElevenLabs provides built-in security controls through tool approval modes that help you manage the security risks associated with MCP tool usage. These controls allow you to balance functionality with security based on your specific needs.

<Frame background="subtle">
  ![Tool approval mode settings](file:9eb1f735-761a-4c47-9df2-a14dd31d5bc6)
</Frame>

### Approval mode options

* **Always Ask (Recommended)**: Provides maximum security by requiring explicit approval for every tool execution. This mode ensures you maintain full control over all MCP tool usage.
* **Fine-Grained Tool Approval**: Allows you to configure approval requirements on a per-tool basis, enabling automatic execution of trusted tools while requiring approval for sensitive operations.
* **No Approval**: Permits unrestricted tool usage without approval prompts. Only use this mode with thoroughly vetted and highly trusted MCP servers.

### Fine-grained security controls

Fine-Grained Tool Approval mode provides the most flexible security configuration, allowing you to classify each tool based on its risk profile:

<Frame background="subtle">
  ![Fine-grained tool approval
  settings](file:425d60c1-cbaf-49db-96f4-9f7b120e6cfa)
</Frame>

* **Auto-approved tools**: Suitable for low-risk, read-only operations or tools you completely trust
* **Approval-required tools**: For tools that modify data, access sensitive information, or perform potentially risky operations
* **Disabled tools**: Completely block tools that are unnecessary or pose security risks

<Warning>
  Even with approval controls in place, carefully evaluate the trustworthiness of MCP servers and
  understand what each tool can access or modify before integration.
</Warning>


## Security tips

### 1. Vet your MCP servers

* **Trusted Sources**: Only integrate MCP servers from sources you trust and have verified. Understand who operates the server and their security posture.
* **Understand Capabilities**: Before integrating, thoroughly review the tools and data resources the MCP server exposes. Be aware of what actions its tools can perform (e.g., accessing files, calling external APIs, modifying data). The MCP `destructiveHint` and `readOnlyHint` annotations can provide clues but should not be solely relied upon for security decisions.
* **Review Server Security**: If possible, review the security practices of the MCP server provider. For MCP servers you develop, ensure you follow general server security best practices and the MCP-specific security guidelines.

### 2. Data sharing and privacy

* **Data Flow**: Be aware that when your agent uses an integrated MCP server, data from the conversation (which may include user inputs) will be sent to that external server.
* **Sensitive Information**: Exercise caution when allowing agents to send Personally Identifiable Information (PII) or other sensitive data to an MCP server. Ensure the server handles such data securely and in compliance with relevant privacy regulations.
* **Purpose Limitation**: Configure your agents and prompts to only share the necessary information with MCP server tools to perform their tasks.

### 3. Credential and connection security

* **Secure Storage**: If an MCP server requires API keys or other secrets for authentication, use any available secret management features within the ElevenLabs platform to store these credentials securely. Avoid hardcoding secrets.
* **HTTPS**: Ensure connections to MCP servers are made over HTTPS to encrypt data in transit.
* **Network Access**: If the MCP server is on a private network, ensure appropriate firewall rules and network ACLs are in place.

### 4. Understand code execution risks

* **Remote Execution**: Tools exposed by an MCP server execute code on that server. While this is the basis of their functionality, it's a critical security consideration. Malicious or poorly secured tools could pose a risk.
* **Input Validation**: Although the MCP server is responsible for validating inputs to its tools, be mindful of the data your agent might send. The LLM should be guided to use tools as intended.

### 5. Add guardrails

* **Prompt Injections**: Connecting to untrusted external MCP servers exposes the risk of prompt injection attacks. Ensure to add thorough guardrails to your system prompt to reduce the risk of exposure to a malicious attack.
* **Tool Approval Configuration**: Use the appropriate approval mode for your security requirements. Start with "Always Ask" for new integrations and only move to less restrictive modes after thorough testing and trust establishment.

### 6. Monitor and review

* **Logging (Server-Side)**: If you control the MCP server, implement comprehensive logging of tool invocations and data access.
* **Regular Review**: Periodically review your integrated MCP servers. Check if their security posture has changed or if new tools have been added that require re-assessment.
* **Approval Patterns**: Monitor tool approval requests to identify unusual patterns that might indicate security issues or misuse.


## Disclaimer

<Warning title="Important Disclaimer">
  By enabling MCP server integrations, you acknowledge that this may involve data sharing with
  third-party services not controlled by ElevenLabs. This could incur additional security risks.
  Please ensure you fully understand the implications, vet the security of any MCP server you
  integrate, and adhere to these security guidelines before proceeding.
</Warning>

For general information on the Model Context Protocol, refer to official MCP documentation and community resources.



# System tools

> Update the internal state of conversations without external requests.

**System tools** enable your assistant to update the internal state of a conversation. Unlike [server tools](/docs/agents-platform/customization/tools/server-tools) or [client tools](/docs/agents-platform/customization/tools/client-tools), system tools don't make external API calls or trigger client-side functions—they modify the internal state of the conversation without making external calls.


## Overview

Some applications require agents to control the flow or state of a conversation.
System tools provide this capability by allowing the assistant to perform actions related to the state of the call that don't require communicating with external servers or the client.

### Available system tools

<CardGroup cols={2}>
  <Card title="End call" icon="duotone square-phone-hangup" href="/docs/agents-platform/customization/tools/system-tools/end-call">
    Let your agent automatically terminate a conversation when appropriate conditions are met.
  </Card>

  <Card title="Language detection" icon="duotone earth-europe" href="/docs/agents-platform/customization/tools/system-tools/language-detection">
    Enable your agent to automatically switch to the user's language during conversations.
  </Card>

  <Card title="Agent transfer" icon="duotone arrow-right-arrow-left" href="/docs/agents-platform/customization/tools/system-tools/agent-transfer">
    Seamlessly transfer conversations between AI agents based on defined conditions.
  </Card>

  <Card title="Transfer to human" icon="duotone user-headset" href="/docs/agents-platform/customization/tools/system-tools/transfer-to-human">
    Seamlessly transfer the user to a human operator.
  </Card>

  <Card title="Skip turn" icon="duotone forward" href="/docs/agents-platform/customization/tools/system-tools/skip-turn">
    Enable the agent to skip their turns if the LLM detects the agent should not speak yet.
  </Card>

  <Card title="Play keypad touch tone" icon="duotone phone-office" href="/docs/agents-platform/customization/tools/system-tools/play-keypad-touch-tone">
    Enable agents to play DTMF tones to interact with automated phone systems and navigate menus.
  </Card>

  <Card title="Voicemail detection" icon="duotone voicemail" href="/docs/agents-platform/customization/tools/system-tools/voicemail-detection">
    Enable agents to automatically detect voicemail systems and optionally leave messages.
  </Card>
</CardGroup>


## Implementation

When creating an agent via API, you can add system tools to your agent configuration. Here's how to implement both the end call and language detection tools:


## Custom LLM integration

When using a custom LLM with ElevenLabs agents, system tools are exposed as function definitions that your LLM can call. Each system tool has specific parameters and trigger conditions:

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

    Learn more: [End call tool](/docs/agents-platform/customization/tools/end-call)
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

    Learn more: [Language detection tool](/docs/agents-platform/customization/tools/language-detection)
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

    Learn more: [Transfer to human tool](/docs/agents-platform/customization/tools/human-transfer)
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

    Learn more: [Skip turn tool](/docs/agents-platform/customization/tools/skip-turn)
  </Accordion>

  <Accordion title="Play keypad touch tone">
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

    Learn more: [Play keypad touch tone tool](/docs/agents-platform/customization/tools/play-keypad-touch-tone)
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

    Learn more: [Voicemail detection tool](/docs/agents-platform/customization/tools/voicemail-detection)
  </Accordion>
</AccordionGroup>

<CodeGroup>
  ```python
  from elevenlabs import (
      ConversationalConfig,
      ElevenLabs,
      AgentConfig,
      PromptAgent,
      PromptAgentInputToolsItem_System,
  )

  # Initialize the client
  elevenlabs = ElevenLabs(api_key="YOUR_API_KEY")

  # Create system tools
  end_call_tool = PromptAgentInputToolsItem_System(
      name="end_call",
      description=""  # Optional: Customize when the tool should be triggered
  )

  language_detection_tool = PromptAgentInputToolsItem_System(
      name="language_detection",
      description=""  # Optional: Customize when the tool should be triggered
  )

  # Create the agent configuration with both tools
  conversation_config = ConversationalConfig(
      agent=AgentConfig(
          prompt=PromptAgent(
              tools=[end_call_tool, language_detection_tool]
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

  // Create the agent with system tools
  await elevenlabs.conversationalAi.agents.create({
    conversationConfig: {
      agent: {
        prompt: {
          tools: [
            {
              type: 'system',
              name: 'end_call',
              description: '',
            },
            {
              type: 'system',
              name: 'language_detection',
              description: '',
            },
          ],
        },
      },
    },
  });
  ```
</CodeGroup>


## FAQ

<AccordionGroup>
  <Accordion title="Can system tools be combined with other tool types?">
    Yes, system tools can be used alongside server tools and client tools in the same assistant.
    This allows for comprehensive functionality that combines internal state management with
    external interactions.
  </Accordion>
</AccordionGroup>

```
```



# End call

> Let your agent automatically hang up on the user.

<Warning>
  The **End Call** tool is added to agents created in the ElevenLabs dashboard by default. For
  agents created via API or SDK, if you would like to enable the End Call tool, you must add it
  manually as a system tool in your agent configuration. [See API Implementation
  below](#api-implementation) for details.
</Warning>

<Frame background="subtle">
  ![End call](file:b911b7ac-3cde-42cf-bda7-75a67b5b1b7a)
</Frame>


## Overview

The **End Call** tool allows your conversational agent to terminate a call with the user. This is a system tool that provides flexibility in how and when calls are ended.


## Functionality

* **Default behavior**: The tool can operate without any user-defined prompts, ending the call when the conversation naturally concludes.
* **Custom prompts**: Users can specify conditions under which the call should end. For example:
  * End the call if the user says "goodbye."
  * Conclude the call when a specific task is completed.

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

### API Implementation

When creating an agent via API, you can add the End Call tool to your agent configuration. It should be defined as a system tool:

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

  # Create the end call tool
  end_call_tool = PromptAgentInputToolsItem_System(
      name="end_call",
      description=""  # Optional: Customize when the tool should be triggered
  )

  # Create the agent configuration
  conversation_config = ConversationalConfig(
      agent=AgentConfig(
          prompt=PromptAgent(
              tools=[end_call_tool]
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

  // Create the agent with end call tool
  await elevenlabs.conversationalAi.agents.create({
    conversationConfig: {
      agent: {
        prompt: {
          tools: [
            {
              type: 'system',
              name: 'end_call',
              description: '', // Optional: Customize when the tool should be triggered
            },
          ],
        },
      },
    },
  });
  ```

  ```bash
  curl -X POST https://api.elevenlabs.io/v1/convai/agents/create \
       -H "xi-api-key: YOUR_API_KEY" \
       -H "Content-Type: application/json" \
       -d '{
    "conversation_config": {
      "agent": {
        "prompt": {
          "tools": [
            {
              "type": "system",
              "name": "end_call",
              "description": ""
            }
          ]
        }
      }
    }
  }'
  ```
</CodeBlocks>

<Tip>
  Leave the description blank to use the default end call prompt.
</Tip>


## Example prompts

**Example 1: Basic End Call**

```
End the call when the user says goodbye, thank you, or indicates they have no more questions.
```

**Example 2: End Call with Custom Prompt**

```
End the call when the user says goodbye, thank you, or indicates they have no more questions. You can only end the call after all their questions have been answered. Please end the call only after confirming that the user doesn't need any additional assistance.
```



# Language detection

> Let your agent automatically switch to the language


## Overview

The `language detection` system tool allows your ElevenLabs agent to switch its output language to any the agent supports.
This system tool is not enabled automatically. Its description can be customized to accommodate your specific use case.

<iframe width="100%" height="400" src="https://www.youtube-nocookie.com/embed/YhF2gKv9ozc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen />

<Note>
  Where possible, we recommend enabling all languages for an agent and enabling the language
  detection system tool.
</Note>

Our language detection tool triggers language switching in two cases, both based on the received audio's detected language and content:

* `detection` if a user speaks a different language than the current output language, a switch will be triggered
* `content` if the user asks in the current language to change to a new language, a switch will be triggered

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


## Enabling language detection

<Steps>
  <Step title="Configure supported languages">
    The languages that the agent can switch to must be defined in the `Agent` settings tab.

    <Frame background="subtle">
      ![Agent languages](file:130fff29-09bd-413f-805d-9da663ce19cd)
    </Frame>
  </Step>

  <Step title="Add the language detection tool">
    Enable language detection by selecting the pre-configured system tool to your agent's tools in the `Agent` tab.
    This is automatically available as an option when selecting `add tool`.

    <Frame background="subtle">
      ![System tool](file:ba464780-199e-4673-bf92-5336e6334bd2)
    </Frame>
  </Step>

  <Step title="Configure tool description">
    Add a description that specifies when to call the tool

    <Frame background="subtle">
      ![Description](file:07248646-122b-4564-9b06-716c038cd547)
    </Frame>
  </Step>
</Steps>

### API Implementation

When creating an agent via API, you can add the `language detection` tool to your agent configuration. It should be defined as a system tool:

<CodeBlocks>
  ```python
  from elevenlabs import (
      ConversationalConfig,
      ElevenLabs,
      AgentConfig,
      PromptAgent,
      PromptAgentInputToolsItem_System,
      LanguagePresetInput,
      ConversationConfigClientOverrideInput,
      AgentConfigOverride,
  )

  # Initialize the client
  elevenlabs = ElevenLabs(api_key="YOUR_API_KEY")

  # Create the language detection tool
  language_detection_tool = PromptAgentInputToolsItem_System(
      name="language_detection",
      description=""  # Optional: Customize when the tool should be triggered
  )

  # Create language presets
  language_presets = {
      "nl": LanguagePresetInput(
          overrides=ConversationConfigClientOverrideInput(
              agent=AgentConfigOverride(
                  prompt=None,
                  first_message="Hoi, hoe gaat het met je?",
                  language=None
              ),
              tts=None
          ),
          first_message_translation=None
      ),
      "fi": LanguagePresetInput(
          overrides=ConversationConfigClientOverrideInput(
              agent=AgentConfigOverride(
                  first_message="Hei, kuinka voit?",
              ),
              tts=None
          ),
      ),
      "tr": LanguagePresetInput(
          overrides=ConversationConfigClientOverrideInput(
              agent=AgentConfigOverride(
                  prompt=None,
                  first_message="Merhaba, nasılsın?",
                  language=None
              ),
              tts=None
          ),
      ),
      "ru": LanguagePresetInput(
          overrides=ConversationConfigClientOverrideInput(
              agent=AgentConfigOverride(
                  prompt=None,
                  first_message="Привет, как ты?",
                  language=None
              ),
              tts=None
          ),
      ),
      "pt": LanguagePresetInput(
          overrides=ConversationConfigClientOverrideInput(
              agent=AgentConfigOverride(
                  prompt=None,
                  first_message="Oi, como você está?",
                  language=None
              ),
              tts=None
          ),
      )
  }

  # Create the agent configuration
  conversation_config = ConversationalConfig(
      agent=AgentConfig(
          prompt=PromptAgent(
              tools=[language_detection_tool],
              first_message="Hi how are you?"
          )
      ),
      language_presets=language_presets
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

  // Create the agent with language detection tool
  await elevenlabs.conversationalAi.agents.create({
    conversationConfig: {
      agent: {
        prompt: {
          tools: [
            {
              type: 'system',
              name: 'language_detection',
              description: '', // Optional: Customize when the tool should be triggered
            },
          ],
          firstMessage: 'Hi, how are you?',
        },
      },
      languagePresets: {
        nl: {
          overrides: {
            agent: {
              prompt: null,
              firstMessage: 'Hoi, hoe gaat het met je?',
              language: null,
            },
            tts: null,
          },
        },
        fi: {
          overrides: {
            agent: {
              prompt: null,
              firstMessage: 'Hei, kuinka voit?',
              language: null,
            },
            tts: null,
          },
          firstMessageTranslation: {
            sourceHash: '{"firstMessage":"Hi how are you?","language":"en"}',
            text: 'Hei, kuinka voit?',
          },
        },
        tr: {
          overrides: {
            agent: {
              prompt: null,
              firstMessage: 'Merhaba, nasılsın?',
              language: null,
            },
            tts: null,
          },
        },
        ru: {
          overrides: {
            agent: {
              prompt: null,
              firstMessage: 'Привет, как ты?',
              language: null,
            },
            tts: null,
          },
        },
        pt: {
          overrides: {
            agent: {
              prompt: null,
              firstMessage: 'Oi, como você está?',
              language: null,
            },
            tts: null,
          },
        },
        ar: {
          overrides: {
            agent: {
              prompt: null,
              firstMessage: 'مرحبًا كيف حالك؟',
              language: null,
            },
            tts: null,
          },
        },
      },
    },
  });
  ```

  ```bash
  curl -X POST https://api.elevenlabs.io/v1/convai/agents/create \
       -H "xi-api-key: YOUR_API_KEY" \
       -H "Content-Type: application/json" \
       -d '{
    "conversation_config": {
      "agent": {
        "prompt": {
          "first_message": "Hi how are you?",
          "tools": [
            {
              "type": "system",
              "name": "language_detection",
              "description": ""
            }
          ]
        }
      },
      "language_presets": {
        "nl": {
          "overrides": {
            "agent": {
              "prompt": null,
              "first_message": "Hoi, hoe gaat het met je?",
              "language": null
            },
            "tts": null
          }
        },
        "fi": {
          "overrides": {
            "agent": {
              "prompt": null,
              "first_message": "Hei, kuinka voit?",
              "language": null
            },
            "tts": null
          }
        },
        "tr": {
          "overrides": {
            "agent": {
              "prompt": null,
              "first_message": "Merhaba, nasılsın?",
              "language": null
            },
            "tts": null
          }
        },
        "ru": {
          "overrides": {
            "agent": {
              "prompt": null,
              "first_message": "Привет, как ты?",
              "language": null
            },
            "tts": null
          }
        },
        "pt": {
          "overrides": {
            "agent": {
              "prompt": null,
              "first_message": "Oi, como você está?",
              "language": null
            },
            "tts": null
          }
        },
        "ar": {
          "overrides": {
            "agent": {
              "prompt": null,
              "first_message": "مرحبًا كيف حالك؟",
              "language": null
            },
            "tts": null
          }
        }
      }
    }
  }'
  ```
</CodeBlocks>

<Tip>
  Leave the description blank to use the default language detection prompt.
</Tip>



# Agent transfer

> Seamlessly transfer the user between ElevenLabs agents based on defined conditions.


## Overview

Agent-agent transfer allows a ElevenLabs agent to hand off the ongoing conversation to another designated agent when specific conditions are met. This enables the creation of sophisticated, multi-layered conversational workflows where different agents handle specific tasks or levels of complexity.

For example, an initial agent (Orchestrator) could handle general inquiries and then transfer the call to a specialized agent based on the conversation's context. Transfers can also be nested:

<Frame background="subtle" caption="Example Agent Transfer Hierarchy">
  ```text
  Orchestrator Agent (Initial Qualification)
  │
  ├───> Agent 1 (e.g., Availability Inquiries)
  │
  ├───> Agent 2 (e.g., Technical Support)
  │     │
  │     └───> Agent 2a (e.g., Hardware Support)
  │
  └───> Agent 3 (e.g., Billing Issues)

  ```
</Frame>

<Note>
  We recommend using the `gpt-4o` or `gpt-4o-mini` models when using agent-agent transfers due to better tool calling.
</Note>

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


## Enabling agent transfer

Agent transfer is configured using the `transfer_to_agent` system tool.

<Steps>
  <Step title="Add the transfer tool">
    Enable agent transfer by selecting the `transfer_to_agent` system tool in your agent's configuration within the `Agent` tab. Choose "Transfer to AI Agent" when adding a tool.

    <Frame background="subtle">
      <img src="file:006089a3-d392-477c-8486-8669a2fb0c4e" alt="Add Transfer Tool" />
    </Frame>
  </Step>

  <Step title="Configure tool description (optional)">
    You can provide a custom description to guide the LLM on when to trigger a transfer. If left blank, a default description encompassing the defined transfer rules will be used.

    <Frame background="subtle">
      <img src="file:47e5426f-ef4c-44d8-9623-0b3bafcf1863" alt="Transfer Tool Description" />
    </Frame>
  </Step>

  <Step title="Define transfer rules">
    Configure the specific rules for transferring to other agents. For each rule, specify:

    * **Agent**: The target agent to transfer the conversation to.
    * **Condition**: A natural language description of the circumstances under which the transfer should occur (e.g., "User asks about billing details", "User requests technical support for product X").
    * **Delay before transfer (milliseconds)**: The minimum delay (in milliseconds) before the transfer occurs. Defaults to 0 for immediate transfer.
    * **Transfer Message**: An optional custom message to play during the transfer. If left blank, the transfer will occur silently.
    * **Enable First Message**: Whether the transferred agent should play its first message after the transfer. Defaults to off.

    The LLM will use these conditions, along with the tool description, to decide when and to which agent (by number) to transfer.

    <Frame background="subtle">
      <img src="file:1e98fff3-fee5-45fa-98f1-5103ba7f3da1" alt="Transfer Rules Configuration" />
    </Frame>

    <Note>
      Ensure that the user account creating the agent has at least viewer permissions for any target agents specified in the transfer rules.
    </Note>
  </Step>
</Steps>


## API Implementation

You can configure the `transfer_to_agent` system tool when creating or updating an agent via the API.

<CodeBlocks>
  ```python
  from elevenlabs import (
      ConversationalConfig,
      ElevenLabs,
      AgentConfig,
      PromptAgent,
      PromptAgentInputToolsItem_System,
      SystemToolConfigInputParams_TransferToAgent,
      AgentTransfer
  )

  # Initialize the client
  elevenlabs = ElevenLabs(api_key="YOUR_API_KEY")

  # Define transfer rules with new options
  transfer_rules = [
      AgentTransfer(
          agent_id="AGENT_ID_1",
          condition="When the user asks for billing support.",
          delay_ms=1000,  # 1 second delay
          transfer_message="I'm connecting you to our billing specialist.",
          enable_transferred_agent_first_message=True
      ),
      AgentTransfer(
          agent_id="AGENT_ID_2",
          condition="When the user requests advanced technical help.",
          delay_ms=0,  # Immediate transfer
          transfer_message=None,  # Silent transfer
          enable_transferred_agent_first_message=False
      )
  ]

  # Create the transfer tool configuration
  transfer_tool = PromptAgentInputToolsItem_System(
      type="system",
      name="transfer_to_agent",
      description="Transfer the user to a specialized agent based on their request.", # Optional custom description
      params=SystemToolConfigInputParams_TransferToAgent(
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

  print(response)
  ```

  ```javascript
  import { ElevenLabs } from '@elevenlabs/elevenlabs-js';

  // Initialize the client
  const elevenlabs = new ElevenLabs({
    apiKey: 'YOUR_API_KEY',
  });

  // Define transfer rules with new options
  const transferRules = [
    {
      agentId: 'AGENT_ID_1',
      condition: 'When the user asks for billing support.',
      delayMs: 1000, // 1 second delay
      transferMessage: "I'm connecting you to our billing specialist.",
      enableTransferredAgentFirstMessage: true,
    },
    {
      agentId: 'AGENT_ID_2',
      condition: 'When the user requests advanced technical help.',
      delayMs: 0, // Immediate transfer
      transferMessage: null, // Silent transfer
      enableTransferredAgentFirstMessage: false,
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
              name: 'transfer_to_agent',
              description: 'Transfer the user to a specialized agent based on their request.', // Optional custom description
              params: {
                systemToolType: 'transfer_to_agent',
                transfers: transferRules,
              },
            },
          ],
        },
      },
    },
  });
  ```
</CodeBlocks>



---
**Navigation:** [← Previous](./11-build.md) | [Index](./index.md) | [Next →](./13-transfer-to-human.md)
