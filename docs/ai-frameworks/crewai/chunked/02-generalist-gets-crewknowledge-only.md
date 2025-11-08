# - generalist gets: crew_knowledge only

**Navigation:** [← Previous](./01-agents.md) | [Index](./index.md) | [Next →](./03-srclatestaidevelopmentcrewpy.md)

---

# - generalist gets: crew_knowledge only
```

#### Example 3: Multiple Agents with Different Knowledge

```python  theme={null}

# Different knowledge for different agents
sales_knowledge = StringKnowledgeSource(content="Sales procedures and pricing")
tech_knowledge = StringKnowledgeSource(content="Technical documentation")
support_knowledge = StringKnowledgeSource(content="Support procedures")

sales_agent = Agent(
    role="Sales Representative",
    knowledge_sources=[sales_knowledge],
    embedder={"provider": "openai", "config": {"model": "text-embedding-3-small"}}
)

tech_agent = Agent(
    role="Technical Expert", 
    knowledge_sources=[tech_knowledge],
    embedder={"provider": "ollama", "config": {"model": "mxbai-embed-large"}}
)

support_agent = Agent(
    role="Support Specialist",
    knowledge_sources=[support_knowledge]
    # Will use crew embedder as fallback
)

crew = Crew(
    agents=[sales_agent, tech_agent, support_agent],
    tasks=[...],
    embedder={  # Fallback embedder for agents without their own
        "provider": "google",
        "config": {"model": "text-embedding-004"}
    }
)


# Each agent gets only their specific knowledge

# Each can use different embedding providers
```

<Tip>
  Unlike retrieval from a vector database using a tool, agents preloaded with knowledge will not need a retrieval persona or task.
  Simply add the relevant knowledge sources your agent or crew needs to function.

  Knowledge sources can be added at the agent or crew level.
  Crew level knowledge sources will be used by **all agents** in the crew.
  Agent level knowledge sources will be used by the **specific agent** that is preloaded with the knowledge.
</Tip>


## Knowledge Configuration

You can configure the knowledge configuration for the crew or agent.

```python Code theme={null}
from crewai.knowledge.knowledge_config import KnowledgeConfig

knowledge_config = KnowledgeConfig(results_limit=10, score_threshold=0.5)

agent = Agent(
    ...
    knowledge_config=knowledge_config
)
```

<Tip>
  `results_limit`: is the number of relevant documents to return. Default is 3.
  `score_threshold`: is the minimum score for a document to be considered relevant. Default is 0.35.
</Tip>


## Supported Knowledge Parameters

<ParamField body="sources" type="List[BaseKnowledgeSource]" required="Yes">
  List of knowledge sources that provide content to be stored and queried. Can include PDF, CSV, Excel, JSON, text files, or string content.
</ParamField>

<ParamField body="collection_name" type="str">
  Name of the collection where the knowledge will be stored. Used to identify different sets of knowledge. Defaults to "knowledge" if not provided.
</ParamField>

<ParamField body="storage" type="Optional[KnowledgeStorage]">
  Custom storage configuration for managing how the knowledge is stored and retrieved. If not provided, a default storage will be created.
</ParamField>


## Knowledge Storage Transparency

<Info>
  **Understanding Knowledge Storage**: CrewAI automatically stores knowledge sources in platform-specific directories using ChromaDB for vector storage. Understanding these locations and defaults helps with production deployments, debugging, and storage management.
</Info>

### Where CrewAI Stores Knowledge Files

By default, CrewAI uses the same storage system as memory, storing knowledge in platform-specific directories:

#### Default Storage Locations by Platform

**macOS:**

```
~/Library/Application Support/CrewAI/{project_name}/
└── knowledge/                    # Knowledge ChromaDB files
    ├── chroma.sqlite3           # ChromaDB metadata
    ├── {collection_id}/         # Vector embeddings
    └── knowledge_{collection}/  # Named collections
```

**Linux:**

```
~/.local/share/CrewAI/{project_name}/
└── knowledge/
    ├── chroma.sqlite3
    ├── {collection_id}/
    └── knowledge_{collection}/
```

**Windows:**

```
C:\Users\{username}\AppData\Local\CrewAI\{project_name}\
└── knowledge\
    ├── chroma.sqlite3
    ├── {collection_id}\
    └── knowledge_{collection}\
```

### Finding Your Knowledge Storage Location

To see exactly where CrewAI is storing your knowledge files:

```python  theme={null}
from crewai.utilities.paths import db_storage_path
import os


# Get the knowledge storage path
knowledge_path = os.path.join(db_storage_path(), "knowledge")
print(f"Knowledge storage location: {knowledge_path}")


# List knowledge collections and files
if os.path.exists(knowledge_path):
    print("\nKnowledge storage contents:")
    for item in os.listdir(knowledge_path):
        item_path = os.path.join(knowledge_path, item)
        if os.path.isdir(item_path):
            print(f"📁 Collection: {item}/")
            # Show collection contents
            try:
                for subitem in os.listdir(item_path):
                    print(f"   └── {subitem}")
            except PermissionError:
                print(f"   └── (permission denied)")
        else:
            print(f"📄 {item}")
else:
    print("No knowledge storage found yet.")
```

### Controlling Knowledge Storage Locations

#### Option 1: Environment Variable (Recommended)

```python  theme={null}
import os
from crewai import Crew


# Set custom storage location for all CrewAI data
os.environ["CREWAI_STORAGE_DIR"] = "./my_project_storage"


# All knowledge will now be stored in ./my_project_storage/knowledge/
crew = Crew(
    agents=[...],
    tasks=[...],
    knowledge_sources=[...]
)
```

#### Option 2: Custom Knowledge Storage

```python  theme={null}
from crewai.knowledge.storage.knowledge_storage import KnowledgeStorage
from crewai.knowledge.source.string_knowledge_source import StringKnowledgeSource


# Create custom storage with specific embedder
custom_storage = KnowledgeStorage(
    embedder={
        "provider": "ollama",
        "config": {"model": "mxbai-embed-large"}
    },
    collection_name="my_custom_knowledge"
)


# Use with knowledge sources
knowledge_source = StringKnowledgeSource(
    content="Your knowledge content here"
)
knowledge_source.storage = custom_storage
```

#### Option 3: Project-Specific Knowledge Storage

```python  theme={null}
import os
from pathlib import Path


# Store knowledge in project directory
project_root = Path(__file__).parent
knowledge_dir = project_root / "knowledge_storage"

os.environ["CREWAI_STORAGE_DIR"] = str(knowledge_dir)


# Now all knowledge will be stored in your project directory
```

### Default Embedding Provider Behavior

<Info>
  **Default Embedding Provider**: CrewAI defaults to OpenAI embeddings (`text-embedding-3-small`) for knowledge storage, even when using different LLM providers. You can easily customize this to match your setup.
</Info>

#### Understanding Default Behavior

```python  theme={null}
from crewai import Agent, Crew, LLM
from crewai.knowledge.source.string_knowledge_source import StringKnowledgeSource


# When using Claude as your LLM...
agent = Agent(
    role="Researcher",
    goal="Research topics",
    backstory="Expert researcher",
    llm=LLM(provider="anthropic", model="claude-3-sonnet")  # Using Claude
)


# CrewAI will still use OpenAI embeddings by default for knowledge

# This ensures consistency but may not match your LLM provider preference
knowledge_source = StringKnowledgeSource(content="Research data...")

crew = Crew(
    agents=[agent],
    tasks=[...],
    knowledge_sources=[knowledge_source]
    # Default: Uses OpenAI embeddings even with Claude LLM
)
```

#### Customizing Knowledge Embedding Providers

```python  theme={null}

# Option 1: Use Voyage AI (recommended by Anthropic for Claude users)
crew = Crew(
    agents=[agent],
    tasks=[...],
    knowledge_sources=[knowledge_source],
    embedder={
        "provider": "voyageai",  # Recommended for Claude users
        "config": {
            "api_key": "your-voyage-api-key",
            "model": "voyage-3"  # or "voyage-3-large" for best quality
        }
    }
)


# Option 2: Use local embeddings (no external API calls)
crew = Crew(
    agents=[agent],
    tasks=[...],
    knowledge_sources=[knowledge_source],
    embedder={
        "provider": "ollama",
        "config": {
            "model": "mxbai-embed-large",
            "url": "http://localhost:11434/api/embeddings"
        }
    }
)


# Option 3: Agent-level embedding customization
agent = Agent(
    role="Researcher",
    goal="Research topics",
    backstory="Expert researcher",
    knowledge_sources=[knowledge_source],
    embedder={
        "provider": "google",
        "config": {
            "model": "models/text-embedding-004",
            "api_key": "your-google-key"
        }
    }
)
```

#### Configuring Azure OpenAI Embeddings

When using Azure OpenAI embeddings:

1. Make sure you deploy the embedding model in Azure platform first
2. Then you need to use the following configuration:

```python  theme={null}
agent = Agent(
    role="Researcher",
    goal="Research topics",
    backstory="Expert researcher",
    knowledge_sources=[knowledge_source],
    embedder={
        "provider": "azure",
        "config": {
            "api_key": "your-azure-api-key",
            "model": "text-embedding-ada-002", # change to the model you are using and is deployed in Azure
            "api_base": "https://your-azure-endpoint.openai.azure.com/",
            "api_version": "2024-02-01"
        }
    }
)
```


## Advanced Features

### Query Rewriting

CrewAI implements an intelligent query rewriting mechanism to optimize knowledge retrieval. When an agent needs to search through knowledge sources, the raw task prompt is automatically transformed into a more effective search query.

#### How Query Rewriting Works

1. When an agent executes a task with knowledge sources available, the `_get_knowledge_search_query` method is triggered
2. The agent's LLM is used to transform the original task prompt into an optimized search query
3. This optimized query is then used to retrieve relevant information from knowledge sources

#### Benefits of Query Rewriting

<CardGroup cols={2}>
  <Card title="Improved Retrieval Accuracy" icon="bullseye-arrow">
    By focusing on key concepts and removing irrelevant content, query rewriting helps retrieve more relevant information.
  </Card>

  <Card title="Context Awareness" icon="brain">
    The rewritten queries are designed to be more specific and context-aware for vector database retrieval.
  </Card>
</CardGroup>

#### Example

```python  theme={null}

# Original task prompt
task_prompt = "Answer the following questions about the user's favorite movies: What movie did John watch last week? Format your answer in JSON."


# Behind the scenes, this might be rewritten as:
rewritten_query = "What movies did John watch last week?"
```

The rewritten query is more focused on the core information need and removes irrelevant instructions about output formatting.

<Tip>
  This mechanism is fully automatic and requires no configuration from users. The agent's LLM is used to perform the query rewriting, so using a more capable LLM can improve the quality of rewritten queries.
</Tip>

### Knowledge Events

CrewAI emits events during the knowledge retrieval process that you can listen for using the event system. These events allow you to monitor, debug, and analyze how knowledge is being retrieved and used by your agents.

#### Available Knowledge Events

* **KnowledgeRetrievalStartedEvent**: Emitted when an agent starts retrieving knowledge from sources
* **KnowledgeRetrievalCompletedEvent**: Emitted when knowledge retrieval is completed, including the query used and the retrieved content
* **KnowledgeQueryStartedEvent**: Emitted when a query to knowledge sources begins
* **KnowledgeQueryCompletedEvent**: Emitted when a query completes successfully
* **KnowledgeQueryFailedEvent**: Emitted when a query to knowledge sources fails
* **KnowledgeSearchQueryFailedEvent**: Emitted when a search query fails

#### Example: Monitoring Knowledge Retrieval

```python  theme={null}
from crewai.events import (
    KnowledgeRetrievalStartedEvent,
    KnowledgeRetrievalCompletedEvent,
    BaseEventListener,
)

class KnowledgeMonitorListener(BaseEventListener):
    def setup_listeners(self, crewai_event_bus):
        @crewai_event_bus.on(KnowledgeRetrievalStartedEvent)
        def on_knowledge_retrieval_started(source, event):
            print(f"Agent '{event.agent.role}' started retrieving knowledge")
            
        @crewai_event_bus.on(KnowledgeRetrievalCompletedEvent)
        def on_knowledge_retrieval_completed(source, event):
            print(f"Agent '{event.agent.role}' completed knowledge retrieval")
            print(f"Query: {event.query}")
            print(f"Retrieved {len(event.retrieved_knowledge)} knowledge chunks")


# Create an instance of your listener
knowledge_monitor = KnowledgeMonitorListener()
```

For more information on using events, see the [Event Listeners](https://docs.crewai.com/concepts/event-listener) documentation.

### Custom Knowledge Sources

CrewAI allows you to create custom knowledge sources for any type of data by extending the `BaseKnowledgeSource` class. Let's create a practical example that fetches and processes space news articles.

#### Space News Knowledge Source Example

<CodeGroup>
  ```python Code theme={null}
  from crewai import Agent, Task, Crew, Process, LLM
  from crewai.knowledge.source.base_knowledge_source import BaseKnowledgeSource
  import requests
  from datetime import datetime
  from typing import Dict, Any
  from pydantic import BaseModel, Field

  class SpaceNewsKnowledgeSource(BaseKnowledgeSource):
      """Knowledge source that fetches data from Space News API."""

      api_endpoint: str = Field(description="API endpoint URL")
      limit: int = Field(default=10, description="Number of articles to fetch")

      def load_content(self) -> Dict[Any, str]:
          """Fetch and format space news articles."""
          try:
              response = requests.get(
                  f"{self.api_endpoint}?limit={self.limit}"
              )
              response.raise_for_status()

              data = response.json()
              articles = data.get('results', [])

              formatted_data = self.validate_content(articles)
              return {self.api_endpoint: formatted_data}
          except Exception as e:
              raise ValueError(f"Failed to fetch space news: {str(e)}")

      def validate_content(self, articles: list) -> str:
          """Format articles into readable text."""
          formatted = "Space News Articles:\n\n"
          for article in articles:
              formatted += f"""
                  Title: {article['title']}
                  Published: {article['published_at']}
                  Summary: {article['summary']}
                  News Site: {article['news_site']}
                  URL: {article['url']}
                  -------------------"""
          return formatted

      def add(self) -> None:
          """Process and store the articles."""
          content = self.load_content()
          for _, text in content.items():
              chunks = self._chunk_text(text)
              self.chunks.extend(chunks)

          self._save_documents()

  # Create knowledge source
  recent_news = SpaceNewsKnowledgeSource(
      api_endpoint="https://api.spaceflightnewsapi.net/v4/articles",
      limit=10,
  )

  # Create specialized agent
  space_analyst = Agent(
      role="Space News Analyst",
      goal="Answer questions about space news accurately and comprehensively",
      backstory="""You are a space industry analyst with expertise in space exploration,
      satellite technology, and space industry trends. You excel at answering questions
      about space news and providing detailed, accurate information.""",
      knowledge_sources=[recent_news],
      llm=LLM(model="gpt-4", temperature=0.0)
  )

  # Create task that handles user questions
  analysis_task = Task(
      description="Answer this question about space news: {user_question}",
      expected_output="A detailed answer based on the recent space news articles",
      agent=space_analyst
  )

  # Create and run the crew
  crew = Crew(
      agents=[space_analyst],
      tasks=[analysis_task],
      verbose=True,
      process=Process.sequential
  )

  # Example usage
  result = crew.kickoff(
      inputs={"user_question": "What are the latest developments in space exploration?"}
  )
  ```

  ```output Output theme={null}
  # Agent: Space News Analyst
  ## Task: Answer this question about space news: What are the latest developments in space exploration?


  # Agent: Space News Analyst
  ## Final Answer:
  The latest developments in space exploration, based on recent space news articles, include the following:

  1. SpaceX has received the final regulatory approvals to proceed with the second integrated Starship/Super Heavy launch, scheduled for as soon as the morning of Nov. 17, 2023. This is a significant step in SpaceX's ambitious plans for space exploration and colonization. [Source: SpaceNews](https://spacenews.com/starship-cleared-for-nov-17-launch/)

  2. SpaceX has also informed the US Federal Communications Commission (FCC) that it plans to begin launching its first next-generation Starlink Gen2 satellites. This represents a major upgrade to the Starlink satellite internet service, which aims to provide high-speed internet access worldwide. [Source: Teslarati](https://www.teslarati.com/spacex-first-starlink-gen2-satellite-launch-2022/)

  3. AI startup Synthetaic has raised $15 million in Series B funding. The company uses artificial intelligence to analyze data from space and air sensors, which could have significant applications in space exploration and satellite technology. [Source: SpaceNews](https://spacenews.com/ai-startup-synthetaic-raises-15-million-in-series-b-funding/)

  4. The Space Force has formally established a unit within the U.S. Indo-Pacific Command, marking a permanent presence in the Indo-Pacific region. This could have significant implications for space security and geopolitics. [Source: SpaceNews](https://spacenews.com/space-force-establishes-permanent-presence-in-indo-pacific-region/)

  5. Slingshot Aerospace, a space tracking and data analytics company, is expanding its network of ground-based optical telescopes to increase coverage of low Earth orbit. This could improve our ability to track and analyze objects in low Earth orbit, including satellites and space debris. [Source: SpaceNews](https://spacenews.com/slingshots-space-tracking-network-to-extend-coverage-of-low-earth-orbit/)

  6. The National Natural Science Foundation of China has outlined a five-year project for researchers to study the assembly of ultra-large spacecraft. This could lead to significant advancements in spacecraft technology and space exploration capabilities. [Source: SpaceNews](https://spacenews.com/china-researching-challenges-of-kilometer-scale-ultra-large-spacecraft/)

  7. The Center for AEroSpace Autonomy Research (CAESAR) at Stanford University is focusing on spacecraft autonomy. The center held a kickoff event on May 22, 2024, to highlight the industry, academia, and government collaboration it seeks to foster. This could lead to significant advancements in autonomous spacecraft technology. [Source: SpaceNews](https://spacenews.com/stanford-center-focuses-on-spacecraft-autonomy/)
  ```
</CodeGroup>


## Debugging and Troubleshooting

### Debugging Knowledge Issues

#### Check Agent Knowledge Initialization

```python  theme={null}
from crewai import Agent, Crew, Task
from crewai.knowledge.source.string_knowledge_source import StringKnowledgeSource

knowledge_source = StringKnowledgeSource(content="Test knowledge")

agent = Agent(
    role="Test Agent",
    goal="Test knowledge",
    backstory="Testing",
    knowledge_sources=[knowledge_source]
)

crew = Crew(agents=[agent], tasks=[Task(...)])


# Before kickoff - knowledge not initialized
print(f"Before kickoff - Agent knowledge: {getattr(agent, 'knowledge', None)}")

crew.kickoff()


# After kickoff - knowledge initialized
print(f"After kickoff - Agent knowledge: {agent.knowledge}")
print(f"Agent knowledge collection: {agent.knowledge.storage.collection_name}")
print(f"Number of sources: {len(agent.knowledge.sources)}")
```

#### Verify Knowledge Storage Locations

```python  theme={null}
import os
from crewai.utilities.paths import db_storage_path


# Check storage structure
storage_path = db_storage_path()
knowledge_path = os.path.join(storage_path, "knowledge")

if os.path.exists(knowledge_path):
    print("Knowledge collections found:")
    for collection in os.listdir(knowledge_path):
        collection_path = os.path.join(knowledge_path, collection)
        if os.path.isdir(collection_path):
            print(f"  - {collection}/")
            # Show collection contents
            for item in os.listdir(collection_path):
                print(f"    └── {item}")
```

#### Test Knowledge Retrieval

```python  theme={null}

# Test agent knowledge retrieval
if hasattr(agent, 'knowledge') and agent.knowledge:
    test_query = ["test query"]
    results = agent.knowledge.query(test_query)
    print(f"Agent knowledge results: {len(results)} documents found")
    
    # Test crew knowledge retrieval (if exists)
    if hasattr(crew, 'knowledge') and crew.knowledge:
        crew_results = crew.query_knowledge(test_query)
        print(f"Crew knowledge results: {len(crew_results)} documents found")
```

#### Inspect Knowledge Collections

```python  theme={null}
import chromadb
from crewai.utilities.paths import db_storage_path
import os


# Connect to CrewAI's knowledge ChromaDB
knowledge_path = os.path.join(db_storage_path(), "knowledge")

if os.path.exists(knowledge_path):
    client = chromadb.PersistentClient(path=knowledge_path)
    collections = client.list_collections()
    
    print("Knowledge Collections:")
    for collection in collections:
        print(f"  - {collection.name}: {collection.count()} documents")
        
        # Sample a few documents to verify content
        if collection.count() > 0:
            sample = collection.peek(limit=2)
            print(f"    Sample content: {sample['documents'][0][:100]}...")
else:
    print("No knowledge storage found")
```

#### Check Knowledge Processing

```python  theme={null}
from crewai.knowledge.source.string_knowledge_source import StringKnowledgeSource


# Create a test knowledge source
test_source = StringKnowledgeSource(
    content="Test knowledge content for debugging",
    chunk_size=100,  # Small chunks for testing
    chunk_overlap=20
)


# Check chunking behavior
print(f"Original content length: {len(test_source.content)}")
print(f"Chunk size: {test_source.chunk_size}")
print(f"Chunk overlap: {test_source.chunk_overlap}")


# Process and inspect chunks
test_source.add()
print(f"Number of chunks created: {len(test_source.chunks)}")
for i, chunk in enumerate(test_source.chunks[:3]):  # Show first 3 chunks
    print(f"Chunk {i+1}: {chunk[:50]}...")
```

### Common Knowledge Storage Issues

**"File not found" errors:**

```python  theme={null}

# Ensure files are in the correct location
from crewai.utilities.constants import KNOWLEDGE_DIRECTORY
import os

knowledge_dir = KNOWLEDGE_DIRECTORY  # Usually "knowledge"
file_path = os.path.join(knowledge_dir, "your_file.pdf")

if not os.path.exists(file_path):
    print(f"File not found: {file_path}")
    print(f"Current working directory: {os.getcwd()}")
    print(f"Expected knowledge directory: {os.path.abspath(knowledge_dir)}")
```

**"Embedding dimension mismatch" errors:**

```python  theme={null}

# This happens when switching embedding providers

# Reset knowledge storage to clear old embeddings
crew.reset_memories(command_type='knowledge')


# Or use consistent embedding providers
crew = Crew(
    agents=[...],
    tasks=[...],
    knowledge_sources=[...],
    embedder={"provider": "openai", "config": {"model": "text-embedding-3-small"}}
)
```

**"ChromaDB permission denied" errors:**

```bash  theme={null}

# Fix storage permissions
chmod -R 755 ~/.local/share/CrewAI/
```

**Knowledge not persisting between runs:**

```python  theme={null}

# Verify storage location consistency
import os
from crewai.utilities.paths import db_storage_path

print("CREWAI_STORAGE_DIR:", os.getenv("CREWAI_STORAGE_DIR"))
print("Computed storage path:", db_storage_path())
print("Knowledge path:", os.path.join(db_storage_path(), "knowledge"))
```

### Knowledge Reset Commands

```python  theme={null}

# Reset only agent-specific knowledge
crew.reset_memories(command_type='agent_knowledge')


# Reset both crew and agent knowledge  
crew.reset_memories(command_type='knowledge')


# CLI commands

# crewai reset-memories --agent-knowledge  # Agent knowledge only

# crewai reset-memories --knowledge        # All knowledge
```

### Clearing Knowledge

If you need to clear the knowledge stored in CrewAI, you can use the `crewai reset-memories` command with the `--knowledge` option.

```bash Command theme={null}
crewai reset-memories --knowledge
```

This is useful when you've updated your knowledge sources and want to ensure that the agents are using the most recent information.


## Best Practices

<AccordionGroup>
  <Accordion title="Content Organization">
    * Keep chunk sizes appropriate for your content type
    * Consider content overlap for context preservation
    * Organize related information into separate knowledge sources
  </Accordion>

  <Accordion title="Performance Tips">
    * Adjust chunk sizes based on content complexity
    * Configure appropriate embedding models
    * Consider using local embedding providers for faster processing
  </Accordion>

  <Accordion title="One Time Knowledge">
    * With the typical file structure provided by CrewAI, knowledge sources are embedded every time the kickoff is triggered.
    * If the knowledge sources are large, this leads to inefficiency and increased latency, as the same data is embedded each time.
    * To resolve this, directly initialize the knowledge parameter instead of the knowledge\_sources parameter.
    * Link to the issue to get complete idea [Github Issue](https://github.com/crewAIInc/crewAI/issues/2755)
  </Accordion>

  <Accordion title="Knowledge Management">
    * Use agent-level knowledge for role-specific information
    * Use crew-level knowledge for shared information all agents need
    * Set embedders at agent level if you need different embedding strategies
    * Use consistent collection naming by keeping agent roles descriptive
    * Test knowledge initialization by checking agent.knowledge after kickoff
    * Monitor storage locations to understand where knowledge is stored
    * Reset knowledge appropriately using the correct command types
  </Accordion>

  <Accordion title="Production Best Practices">
    * Set `CREWAI_STORAGE_DIR` to a known location in production
    * Choose explicit embedding providers to match your LLM setup and avoid API key conflicts
    * Monitor knowledge storage size as it grows with document additions
    * Organize knowledge sources by domain or purpose using collection names
    * Include knowledge directories in your backup and deployment strategies
    * Set appropriate file permissions for knowledge files and storage directories
    * Use environment variables for API keys and sensitive configuration
  </Accordion>
</AccordionGroup>



# LLMs
Source: https://docs.crewai.com/en/concepts/llms

A comprehensive guide to configuring and using Large Language Models (LLMs) in your CrewAI projects


## Overview

CrewAI integrates with multiple LLM providers through providers native sdks, giving you the flexibility to choose the right model for your specific use case. This guide will help you understand how to configure and use different LLM providers in your CrewAI projects.


## What are LLMs?

Large Language Models (LLMs) are the core intelligence behind CrewAI agents. They enable agents to understand context, make decisions, and generate human-like responses. Here's what you need to know:

<CardGroup cols={2}>
  <Card title="LLM Basics" icon="brain">
    Large Language Models are AI systems trained on vast amounts of text data. They power the intelligence of your CrewAI agents, enabling them to understand and generate human-like text.
  </Card>

  <Card title="Context Window" icon="window">
    The context window determines how much text an LLM can process at once. Larger windows (e.g., 128K tokens) allow for more context but may be more expensive and slower.
  </Card>

  <Card title="Temperature" icon="temperature-three-quarters">
    Temperature (0.0 to 1.0) controls response randomness. Lower values (e.g., 0.2) produce more focused, deterministic outputs, while higher values (e.g., 0.8) increase creativity and variability.
  </Card>

  <Card title="Provider Selection" icon="server">
    Each LLM provider (e.g., OpenAI, Anthropic, Google) offers different models with varying capabilities, pricing, and features. Choose based on your needs for accuracy, speed, and cost.
  </Card>
</CardGroup>


## Setting up your LLM

There are different places in CrewAI code where you can specify the model to use. Once you specify the model you are using, you will need to provide the configuration (like an API key) for each of the model providers you use. See the [provider configuration examples](#provider-configuration-examples) section for your provider.

<Tabs>
  <Tab title="1. Environment Variables">
    The simplest way to get started. Set the model in your environment directly, through an `.env` file or in your app code. If you used `crewai create` to bootstrap your project, it will be set already.

    ```bash .env theme={null}
    MODEL=model-id  # e.g. gpt-4o, gemini-2.0-flash, claude-3-sonnet-...

    # Be sure to set your API keys here too. See the Provider
    # section below.
    ```

    <Warning>
      Never commit API keys to version control. Use environment files (.env) or your system's secret management.
    </Warning>
  </Tab>

  <Tab title="2. YAML Configuration">
    Create a YAML file to define your agent configurations. This method is great for version control and team collaboration:

    ```yaml agents.yaml {6} theme={null}
    researcher:
        role: Research Specialist
        goal: Conduct comprehensive research and analysis
        backstory: A dedicated research professional with years of experience
        verbose: true
        llm: provider/model-id  # e.g. openai/gpt-4o, google/gemini-2.0-flash, anthropic/claude...
        # (see provider configuration examples below for more)
    ```

    <Info>
      The YAML configuration allows you to:

      * Version control your agent settings
      * Easily switch between different models
      * Share configurations across team members
      * Document model choices and their purposes
    </Info>
  </Tab>

  <Tab title="3. Direct Code">
    For maximum flexibility, configure LLMs directly in your Python code:

    ```python {4,8} theme={null}
    from crewai import LLM

    # Basic configuration
    llm = LLM(model="model-id-here")  # gpt-4o, gemini-2.0-flash, anthropic/claude...

    # Advanced configuration with detailed parameters
    llm = LLM(
        model="model-id-here",  # gpt-4o, gemini-2.0-flash, anthropic/claude...
        temperature=0.7,        # Higher for more creative outputs
        timeout=120,            # Seconds to wait for response
        max_tokens=4000,        # Maximum length of response
        top_p=0.9,              # Nucleus sampling parameter
        frequency_penalty=0.1 , # Reduce repetition
        presence_penalty=0.1,   # Encourage topic diversity
        response_format={"type": "json"},  # For structured outputs
        seed=42                 # For reproducible results
    )
    ```

    <Info>
      Parameter explanations:

      * `temperature`: Controls randomness (0.0-1.0)
      * `timeout`: Maximum wait time for response
      * `max_tokens`: Limits response length
      * `top_p`: Alternative to temperature for sampling
      * `frequency_penalty`: Reduces word repetition
      * `presence_penalty`: Encourages new topics
      * `response_format`: Specifies output structure
      * `seed`: Ensures consistent outputs
    </Info>
  </Tab>
</Tabs>


## Provider Configuration Examples

CrewAI supports a multitude of LLM providers, each offering unique features, authentication methods, and model capabilities.
In this section, you'll find detailed examples that help you select, configure, and optimize the LLM that best fits your project's needs.

<AccordionGroup>
  <Accordion title="OpenAI">
    CrewAI provides native integration with OpenAI through the OpenAI Python SDK.

    ```toml Code theme={null}
    # Required
    OPENAI_API_KEY=sk-...

    # Optional
    OPENAI_BASE_URL=<custom-base-url>
    ```

    **Basic Usage:**

    ```python Code theme={null}
    from crewai import LLM

    llm = LLM(
        model="openai/gpt-4o",
        api_key="your-api-key",  # Or set OPENAI_API_KEY
        temperature=0.7,
        max_tokens=4000
    )
    ```

    **Advanced Configuration:**

    ```python Code theme={null}
    from crewai import LLM

    llm = LLM(
        model="openai/gpt-4o",
        api_key="your-api-key",
        base_url="https://api.openai.com/v1",  # Optional custom endpoint
        organization="org-...",  # Optional organization ID
        project="proj_...",  # Optional project ID
        temperature=0.7,
        max_tokens=4000,
        max_completion_tokens=4000,  # For newer models
        top_p=0.9,
        frequency_penalty=0.1,
        presence_penalty=0.1,
        stop=["END"],
        seed=42,  # For reproducible outputs
        stream=True,  # Enable streaming
        timeout=60.0,  # Request timeout in seconds
        max_retries=3,  # Maximum retry attempts
        logprobs=True,  # Return log probabilities
        top_logprobs=5,  # Number of most likely tokens
        reasoning_effort="medium"  # For o1 models: low, medium, high
    )
    ```

    **Structured Outputs:**

    ```python Code theme={null}
    from pydantic import BaseModel
    from crewai import LLM

    class ResponseFormat(BaseModel):
        name: str
        age: int
        summary: str

    llm = LLM(
        model="openai/gpt-4o",
    )
    ```

    **Supported Environment Variables:**

    * `OPENAI_API_KEY`: Your OpenAI API key (required)
    * `OPENAI_BASE_URL`: Custom base URL for OpenAI API (optional)

    **Features:**

    * Native function calling support (except o1 models)
    * Structured outputs with JSON schema
    * Streaming support for real-time responses
    * Token usage tracking
    * Stop sequences support (except o1 models)
    * Log probabilities for token-level insights
    * Reasoning effort control for o1 models

    **Supported Models:**

    | Model        | Context Window | Best For                                    |
    | ------------ | -------------- | ------------------------------------------- |
    | gpt-4.1      | 1M tokens      | Latest model with enhanced capabilities     |
    | gpt-4.1-mini | 1M tokens      | Efficient version with large context        |
    | gpt-4.1-nano | 1M tokens      | Ultra-efficient variant                     |
    | gpt-4o       | 128,000 tokens | Optimized for speed and intelligence        |
    | gpt-4o-mini  | 200,000 tokens | Cost-effective with large context           |
    | gpt-4-turbo  | 128,000 tokens | Long-form content, document analysis        |
    | gpt-4        | 8,192 tokens   | High-accuracy tasks, complex reasoning      |
    | o1           | 200,000 tokens | Advanced reasoning, complex problem-solving |
    | o1-preview   | 128,000 tokens | Preview of reasoning capabilities           |
    | o1-mini      | 128,000 tokens | Efficient reasoning model                   |
    | o3-mini      | 200,000 tokens | Lightweight reasoning model                 |
    | o4-mini      | 200,000 tokens | Next-gen efficient reasoning                |

    **Note:** To use OpenAI, install the required dependencies:

    ```bash  theme={null}
    uv add "crewai[openai]"
    ```
  </Accordion>

  <Accordion title="Meta-Llama">
    Meta's Llama API provides access to Meta's family of large language models.
    The API is available through the [Meta Llama API](https://llama.developer.meta.com?utm_source=partner-crewai\&utm_medium=website).
    Set the following environment variables in your `.env` file:

    ```toml Code theme={null}
    # Meta Llama API Key Configuration
    LLAMA_API_KEY=LLM|your_api_key_here
    ```

    Example usage in your CrewAI project:

    ```python Code theme={null}
    from crewai import LLM

    # Initialize Meta Llama LLM
    llm = LLM(
        model="meta_llama/Llama-4-Scout-17B-16E-Instruct-FP8",
        temperature=0.8,
        stop=["END"],
        seed=42
    )
    ```

    All models listed here [https://llama.developer.meta.com/docs/models/](https://llama.developer.meta.com/docs/models/) are supported.

    | Model ID                                            | Input context length | Output context length | Input Modalities | Output Modalities |
    | --------------------------------------------------- | -------------------- | --------------------- | ---------------- | ----------------- |
    | `meta_llama/Llama-4-Scout-17B-16E-Instruct-FP8`     | 128k                 | 4028                  | Text, Image      | Text              |
    | `meta_llama/Llama-4-Maverick-17B-128E-Instruct-FP8` | 128k                 | 4028                  | Text, Image      | Text              |
    | `meta_llama/Llama-3.3-70B-Instruct`                 | 128k                 | 4028                  | Text             | Text              |
    | `meta_llama/Llama-3.3-8B-Instruct`                  | 128k                 | 4028                  | Text             | Text              |
  </Accordion>

  <Accordion title="Anthropic">
    CrewAI provides native integration with Anthropic through the Anthropic Python SDK.

    ```toml Code theme={null}
    # Required
    ANTHROPIC_API_KEY=sk-ant-...
    ```

    **Basic Usage:**

    ```python Code theme={null}
    from crewai import LLM

    llm = LLM(
        model="anthropic/claude-3-5-sonnet-20241022",
        api_key="your-api-key",  # Or set ANTHROPIC_API_KEY
        max_tokens=4096  # Required for Anthropic
    )
    ```

    **Advanced Configuration:**

    ```python Code theme={null}
    from crewai import LLM

    llm = LLM(
        model="anthropic/claude-3-5-sonnet-20241022",
        api_key="your-api-key",
        base_url="https://api.anthropic.com",  # Optional custom endpoint
        temperature=0.7,
        max_tokens=4096,  # Required parameter
        top_p=0.9,
        stop_sequences=["END", "STOP"],  # Anthropic uses stop_sequences
        stream=True,  # Enable streaming
        timeout=60.0,  # Request timeout in seconds
        max_retries=3  # Maximum retry attempts
    )
    ```

    **Supported Environment Variables:**

    * `ANTHROPIC_API_KEY`: Your Anthropic API key (required)

    **Features:**

    * Native tool use support for Claude 3+ models
    * Streaming support for real-time responses
    * Automatic system message handling
    * Stop sequences for controlled output
    * Token usage tracking
    * Multi-turn tool use conversations

    **Important Notes:**

    * `max_tokens` is a **required** parameter for all Anthropic models
    * Claude uses `stop_sequences` instead of `stop`
    * System messages are handled separately from conversation messages
    * First message must be from the user (automatically handled)
    * Messages must alternate between user and assistant

    **Supported Models:**

    | Model                      | Context Window | Best For                                 |
    | -------------------------- | -------------- | ---------------------------------------- |
    | claude-3-7-sonnet          | 200,000 tokens | Advanced reasoning and agentic tasks     |
    | claude-3-5-sonnet-20241022 | 200,000 tokens | Latest Sonnet with best performance      |
    | claude-3-5-haiku           | 200,000 tokens | Fast, compact model for quick responses  |
    | claude-3-opus              | 200,000 tokens | Most capable for complex tasks           |
    | claude-3-sonnet            | 200,000 tokens | Balanced intelligence and speed          |
    | claude-3-haiku             | 200,000 tokens | Fastest for simple tasks                 |
    | claude-2.1                 | 200,000 tokens | Extended context, reduced hallucinations |
    | claude-2                   | 100,000 tokens | Versatile model for various tasks        |
    | claude-instant             | 100,000 tokens | Fast, cost-effective for everyday tasks  |

    **Note:** To use Anthropic, install the required dependencies:

    ```bash  theme={null}
    uv add "crewai[anthropic]"
    ```
  </Accordion>

  <Accordion title="Google (Gemini API)">
    CrewAI provides native integration with Google Gemini through the Google Gen AI Python SDK.

    Set your API key in your `.env` file. If you need a key, check [AI Studio](https://aistudio.google.com/apikey).

    ```toml .env theme={null}
    # Required (one of the following)
    GOOGLE_API_KEY=<your-api-key>
    GEMINI_API_KEY=<your-api-key>

    # Optional - for Vertex AI
    GOOGLE_CLOUD_PROJECT=<your-project-id>
    GOOGLE_CLOUD_LOCATION=<location>  # Defaults to us-central1
    GOOGLE_GENAI_USE_VERTEXAI=true  # Set to use Vertex AI
    ```

    **Basic Usage:**

    ```python Code theme={null}
    from crewai import LLM

    llm = LLM(
        model="gemini/gemini-2.0-flash",
        api_key="your-api-key",  # Or set GOOGLE_API_KEY/GEMINI_API_KEY
        temperature=0.7
    )
    ```

    **Advanced Configuration:**

    ```python Code theme={null}
    from crewai import LLM

    llm = LLM(
        model="gemini/gemini-2.5-flash",
        api_key="your-api-key",
        temperature=0.7,
        top_p=0.9,
        top_k=40,  # Top-k sampling parameter
        max_output_tokens=8192,
        stop_sequences=["END", "STOP"],
        stream=True,  # Enable streaming
        safety_settings={
            "HARM_CATEGORY_HARASSMENT": "BLOCK_NONE",
            "HARM_CATEGORY_HATE_SPEECH": "BLOCK_NONE"
        }
    )
    ```

    **Vertex AI Configuration:**

    ```python Code theme={null}
    from crewai import LLM

    llm = LLM(
        model="gemini/gemini-1.5-pro",
        project="your-gcp-project-id",
        location="us-central1"  # GCP region
    )
    ```

    **Supported Environment Variables:**

    * `GOOGLE_API_KEY` or `GEMINI_API_KEY`: Your Google API key (required for Gemini API)
    * `GOOGLE_CLOUD_PROJECT`: Google Cloud project ID (for Vertex AI)
    * `GOOGLE_CLOUD_LOCATION`: GCP location (defaults to `us-central1`)
    * `GOOGLE_GENAI_USE_VERTEXAI`: Set to `true` to use Vertex AI

    **Features:**

    * Native function calling support for Gemini 1.5+ and 2.x models
    * Streaming support for real-time responses
    * Multimodal capabilities (text, images, video)
    * Safety settings configuration
    * Support for both Gemini API and Vertex AI
    * Automatic system instruction handling
    * Token usage tracking

    **Gemini Models:**

    Google offers a range of powerful models optimized for different use cases.

    | Model                     | Context Window | Best For                                                  |
    | ------------------------- | -------------- | --------------------------------------------------------- |
    | gemini-2.5-flash          | 1M tokens      | Adaptive thinking, cost efficiency                        |
    | gemini-2.5-pro            | 1M tokens      | Enhanced thinking and reasoning, multimodal understanding |
    | gemini-2.0-flash          | 1M tokens      | Next generation features, speed, thinking                 |
    | gemini-2.0-flash-thinking | 32,768 tokens  | Advanced reasoning with thinking process                  |
    | gemini-2.0-flash-lite     | 1M tokens      | Cost efficiency and low latency                           |
    | gemini-1.5-pro            | 2M tokens      | Best performing, logical reasoning, coding                |
    | gemini-1.5-flash          | 1M tokens      | Balanced multimodal model, good for most tasks            |
    | gemini-1.5-flash-8b       | 1M tokens      | Fastest, most cost-efficient                              |
    | gemini-1.0-pro            | 32,768 tokens  | Earlier generation model                                  |

    **Gemma Models:**

    The Gemini API also supports [Gemma models](https://ai.google.dev/gemma/docs) hosted on Google infrastructure.

    | Model       | Context Window | Best For                            |
    | ----------- | -------------- | ----------------------------------- |
    | gemma-3-1b  | 32,000 tokens  | Ultra-lightweight tasks             |
    | gemma-3-4b  | 128,000 tokens | Efficient general-purpose tasks     |
    | gemma-3-12b | 128,000 tokens | Balanced performance and efficiency |
    | gemma-3-27b | 128,000 tokens | High-performance tasks              |

    **Note:** To use Google Gemini, install the required dependencies:

    ```bash  theme={null}
    uv add "crewai[google-genai]"
    ```

    The full list of models is available in the [Gemini model docs](https://ai.google.dev/gemini-api/docs/models).
  </Accordion>

  <Accordion title="Google (Vertex AI)">
    Get credentials from your Google Cloud Console and save it to a JSON file, then load it with the following code:

    ```python Code theme={null}
    import json

    file_path = 'path/to/vertex_ai_service_account.json'

    # Load the JSON file
    with open(file_path, 'r') as file:
        vertex_credentials = json.load(file)

    # Convert the credentials to a JSON string
    vertex_credentials_json = json.dumps(vertex_credentials)
    ```

    Example usage in your CrewAI project:

    ```python Code theme={null}
    from crewai import LLM

    llm = LLM(
        model="gemini-1.5-pro-latest", # or vertex_ai/gemini-1.5-pro-latest
        temperature=0.7,
        vertex_credentials=vertex_credentials_json
    )
    ```

    Google offers a range of powerful models optimized for different use cases:

    | Model                          | Context Window | Best For                                                                                                         |
    | ------------------------------ | -------------- | ---------------------------------------------------------------------------------------------------------------- |
    | gemini-2.5-flash-preview-04-17 | 1M tokens      | Adaptive thinking, cost efficiency                                                                               |
    | gemini-2.5-pro-preview-05-06   | 1M tokens      | Enhanced thinking and reasoning, multimodal understanding, advanced coding, and more                             |
    | gemini-2.0-flash               | 1M tokens      | Next generation features, speed, thinking, and realtime streaming                                                |
    | gemini-2.0-flash-lite          | 1M tokens      | Cost efficiency and low latency                                                                                  |
    | gemini-1.5-flash               | 1M tokens      | Balanced multimodal model, good for most tasks                                                                   |
    | gemini-1.5-flash-8B            | 1M tokens      | Fastest, most cost-efficient, good for high-frequency tasks                                                      |
    | gemini-1.5-pro                 | 2M tokens      | Best performing, wide variety of reasoning tasks including logical reasoning, coding, and creative collaboration |
  </Accordion>

  <Accordion title="Azure">
    CrewAI provides native integration with Azure AI Inference and Azure OpenAI through the Azure AI Inference Python SDK.

    ```toml Code theme={null}
    # Required
    AZURE_API_KEY=<your-api-key>
    AZURE_ENDPOINT=<your-endpoint-url>

    # Optional
    AZURE_API_VERSION=<api-version>  # Defaults to 2024-06-01
    ```

    **Endpoint URL Formats:**

    For Azure OpenAI deployments:

    ```
    https://<resource-name>.openai.azure.com/openai/deployments/<deployment-name>
    ```

    For Azure AI Inference endpoints:

    ```
    https://<resource-name>.inference.azure.com
    ```

    **Basic Usage:**

    ```python Code theme={null}
    llm = LLM(
        model="azure/gpt-4",
        api_key="<your-api-key>",  # Or set AZURE_API_KEY
        endpoint="<your-endpoint-url>",
        api_version="2024-06-01"
    )
    ```

    **Advanced Configuration:**

    ```python Code theme={null}
    llm = LLM(
        model="azure/gpt-4o",
        temperature=0.7,
        max_tokens=4000,
        top_p=0.9,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["END"],
        stream=True,
        timeout=60.0,
        max_retries=3
    )
    ```

    **Supported Environment Variables:**

    * `AZURE_API_KEY`: Your Azure API key (required)
    * `AZURE_ENDPOINT`: Your Azure endpoint URL (required, also checks `AZURE_OPENAI_ENDPOINT` and `AZURE_API_BASE`)
    * `AZURE_API_VERSION`: API version (optional, defaults to `2024-06-01`)

    **Features:**

    * Native function calling support for Azure OpenAI models (gpt-4, gpt-4o, gpt-3.5-turbo, etc.)
    * Streaming support for real-time responses
    * Automatic endpoint URL validation and correction
    * Comprehensive error handling with retry logic
    * Token usage tracking

    **Note:** To use Azure AI Inference, install the required dependencies:

    ```bash  theme={null}
    uv add "crewai[azure-ai-inference]"
    ```
  </Accordion>

  <Accordion title="AWS Bedrock">
    CrewAI provides native integration with AWS Bedrock through the boto3 SDK using the Converse API.

    ```toml Code theme={null}
    # Required
    AWS_ACCESS_KEY_ID=<your-access-key>
    AWS_SECRET_ACCESS_KEY=<your-secret-key>

    # Optional
    AWS_SESSION_TOKEN=<your-session-token>  # For temporary credentials
    AWS_DEFAULT_REGION=<your-region>  # Defaults to us-east-1
    ```

    **Basic Usage:**

    ```python Code theme={null}
    from crewai import LLM

    llm = LLM(
        model="bedrock/anthropic.claude-3-5-sonnet-20241022-v2:0",
        region_name="us-east-1"
    )
    ```

    **Advanced Configuration:**

    ```python Code theme={null}
    from crewai import LLM

    llm = LLM(
        model="bedrock/anthropic.claude-3-5-sonnet-20241022-v2:0",
        aws_access_key_id="your-access-key",  # Or set AWS_ACCESS_KEY_ID
        aws_secret_access_key="your-secret-key",  # Or set AWS_SECRET_ACCESS_KEY
        aws_session_token="your-session-token",  # For temporary credentials
        region_name="us-east-1",
        temperature=0.7,
        max_tokens=4096,
        top_p=0.9,
        top_k=250,  # For Claude models
        stop_sequences=["END", "STOP"],
        stream=True,  # Enable streaming
        guardrail_config={  # Optional content filtering
            "guardrailIdentifier": "your-guardrail-id",
            "guardrailVersion": "1"
        },
        additional_model_request_fields={  # Model-specific parameters
            "top_k": 250
        }
    )
    ```

    **Supported Environment Variables:**

    * `AWS_ACCESS_KEY_ID`: AWS access key (required)
    * `AWS_SECRET_ACCESS_KEY`: AWS secret key (required)
    * `AWS_SESSION_TOKEN`: AWS session token for temporary credentials (optional)
    * `AWS_DEFAULT_REGION`: AWS region (defaults to `us-east-1`)

    **Features:**

    * Native tool calling support via Converse API
    * Streaming and non-streaming responses
    * Comprehensive error handling with retry logic
    * Guardrail configuration for content filtering
    * Model-specific parameters via `additional_model_request_fields`
    * Token usage tracking and stop reason logging
    * Support for all Bedrock foundation models
    * Automatic conversation format handling

    **Important Notes:**

    * Uses the modern Converse API for unified model access
    * Automatic handling of model-specific conversation requirements
    * System messages are handled separately from conversation
    * First message must be from user (automatically handled)
    * Some models (like Cohere) require conversation to end with user message

    [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/models-regions.html) is a managed service that provides access to multiple foundation models from top AI companies through a unified API.

    | Model                   | Context Window     | Best For                                                                                                                              |
    | ----------------------- | ------------------ | ------------------------------------------------------------------------------------------------------------------------------------- |
    | Amazon Nova Pro         | Up to 300k tokens  | High-performance, model balancing accuracy, speed, and cost-effectiveness across diverse tasks.                                       |
    | Amazon Nova Micro       | Up to 128k tokens  | High-performance, cost-effective text-only model optimized for lowest latency responses.                                              |
    | Amazon Nova Lite        | Up to 300k tokens  | High-performance, affordable multimodal processing for images, video, and text with real-time capabilities.                           |
    | Claude 3.7 Sonnet       | Up to 128k tokens  | High-performance, best for complex reasoning, coding & AI agents                                                                      |
    | Claude 3.5 Sonnet v2    | Up to 200k tokens  | State-of-the-art model specialized in software engineering, agentic capabilities, and computer interaction at optimized cost.         |
    | Claude 3.5 Sonnet       | Up to 200k tokens  | High-performance model delivering superior intelligence and reasoning across diverse tasks with optimal speed-cost balance.           |
    | Claude 3.5 Haiku        | Up to 200k tokens  | Fast, compact multimodal model optimized for quick responses and seamless human-like interactions                                     |
    | Claude 3 Sonnet         | Up to 200k tokens  | Multimodal model balancing intelligence and speed for high-volume deployments.                                                        |
    | Claude 3 Haiku          | Up to 200k tokens  | Compact, high-speed multimodal model optimized for quick responses and natural conversational interactions                            |
    | Claude 3 Opus           | Up to 200k tokens  | Most advanced multimodal model exceling at complex tasks with human-like reasoning and superior contextual understanding.             |
    | Claude 2.1              | Up to 200k tokens  | Enhanced version with expanded context window, improved reliability, and reduced hallucinations for long-form and RAG applications    |
    | Claude                  | Up to 100k tokens  | Versatile model excelling in sophisticated dialogue, creative content, and precise instruction following.                             |
    | Claude Instant          | Up to 100k tokens  | Fast, cost-effective model for everyday tasks like dialogue, analysis, summarization, and document Q\&A                               |
    | Llama 3.1 405B Instruct | Up to 128k tokens  | Advanced LLM for synthetic data generation, distillation, and inference for chatbots, coding, and domain-specific tasks.              |
    | Llama 3.1 70B Instruct  | Up to 128k tokens  | Powers complex conversations with superior contextual understanding, reasoning and text generation.                                   |
    | Llama 3.1 8B Instruct   | Up to 128k tokens  | Advanced state-of-the-art model with language understanding, superior reasoning, and text generation.                                 |
    | Llama 3 70B Instruct    | Up to 8k tokens    | Powers complex conversations with superior contextual understanding, reasoning and text generation.                                   |
    | Llama 3 8B Instruct     | Up to 8k tokens    | Advanced state-of-the-art LLM with language understanding, superior reasoning, and text generation.                                   |
    | Titan Text G1 - Lite    | Up to 4k tokens    | Lightweight, cost-effective model optimized for English tasks and fine-tuning with focus on summarization and content generation.     |
    | Titan Text G1 - Express | Up to 8k tokens    | Versatile model for general language tasks, chat, and RAG applications with support for English and 100+ languages.                   |
    | Cohere Command          | Up to 4k tokens    | Model specialized in following user commands and delivering practical enterprise solutions.                                           |
    | Jurassic-2 Mid          | Up to 8,191 tokens | Cost-effective model balancing quality and affordability for diverse language tasks like Q\&A, summarization, and content generation. |
    | Jurassic-2 Ultra        | Up to 8,191 tokens | Model for advanced text generation and comprehension, excelling in complex tasks like analysis and content creation.                  |
    | Jamba-Instruct          | Up to 256k tokens  | Model with extended context window optimized for cost-effective text generation, summarization, and Q\&A.                             |
    | Mistral 7B Instruct     | Up to 32k tokens   | This LLM follows instructions, completes requests, and generates creative text.                                                       |
    | Mistral 8x7B Instruct   | Up to 32k tokens   | An MOE LLM that follows instructions, completes requests, and generates creative text.                                                |
    | DeepSeek R1             | 32,768 tokens      | Advanced reasoning model                                                                                                              |

    **Note:** To use AWS Bedrock, install the required dependencies:

    ```bash  theme={null}
    uv add "crewai[bedrock]"
    ```
  </Accordion>

  <Accordion title="Amazon SageMaker">
    ```toml Code theme={null}
    AWS_ACCESS_KEY_ID=<your-access-key>
    AWS_SECRET_ACCESS_KEY=<your-secret-key>
    AWS_DEFAULT_REGION=<your-region>
    ```

    Example usage in your CrewAI project:

    ```python Code theme={null}
    llm = LLM(
        model="sagemaker/<my-endpoint>"
    )
    ```
  </Accordion>

  <Accordion title="Mistral">
    Set the following environment variables in your `.env` file:

    ```toml Code theme={null}
    MISTRAL_API_KEY=<your-api-key>
    ```

    Example usage in your CrewAI project:

    ```python Code theme={null}
    llm = LLM(
        model="mistral/mistral-large-latest",
        temperature=0.7
    )
    ```
  </Accordion>

  <Accordion title="Nvidia NIM">
    Set the following environment variables in your `.env` file:

    ```toml Code theme={null}
    NVIDIA_API_KEY=<your-api-key>
    ```

    Example usage in your CrewAI project:

    ```python Code theme={null}
    llm = LLM(
        model="nvidia_nim/meta/llama3-70b-instruct",
        temperature=0.7
    )
    ```

    Nvidia NIM provides a comprehensive suite of models for various use cases, from general-purpose tasks to specialized applications.

    | Model                                       | Context Window | Best For                                                                                                                    |
    | ------------------------------------------- | -------------- | --------------------------------------------------------------------------------------------------------------------------- |
    | nvidia/mistral-nemo-minitron-8b-8k-instruct | 8,192 tokens   | State-of-the-art small language model delivering superior accuracy for chatbot, virtual assistants, and content generation. |
    | nvidia/nemotron-4-mini-hindi-4b-instruct    | 4,096 tokens   | A bilingual Hindi-English SLM for on-device inference, tailored specifically for Hindi Language.                            |
    | nvidia/llama-3.1-nemotron-70b-instruct      | 128k tokens    | Customized for enhanced helpfulness in responses                                                                            |
    | nvidia/llama3-chatqa-1.5-8b                 | 128k tokens    | Advanced LLM to generate high-quality, context-aware responses for chatbots and search engines.                             |
    | nvidia/llama3-chatqa-1.5-70b                | 128k tokens    | Advanced LLM to generate high-quality, context-aware responses for chatbots and search engines.                             |
    | nvidia/vila                                 | 128k tokens    | Multi-modal vision-language model that understands text/img/video and creates informative responses                         |
    | nvidia/neva-22                              | 4,096 tokens   | Multi-modal vision-language model that understands text/images and generates informative responses                          |
    | nvidia/nemotron-mini-4b-instruct            | 8,192 tokens   | General-purpose tasks                                                                                                       |
    | nvidia/usdcode-llama3-70b-instruct          | 128k tokens    | State-of-the-art LLM that answers OpenUSD knowledge queries and generates USD-Python code.                                  |
    | nvidia/nemotron-4-340b-instruct             | 4,096 tokens   | Creates diverse synthetic data that mimics the characteristics of real-world data.                                          |
    | meta/codellama-70b                          | 100k tokens    | LLM capable of generating code from natural language and vice versa.                                                        |
    | meta/llama2-70b                             | 4,096 tokens   | Cutting-edge large language AI model capable of generating text and code in response to prompts.                            |
    | meta/llama3-8b-instruct                     | 8,192 tokens   | Advanced state-of-the-art LLM with language understanding, superior reasoning, and text generation.                         |
    | meta/llama3-70b-instruct                    | 8,192 tokens   | Powers complex conversations with superior contextual understanding, reasoning and text generation.                         |
    | meta/llama-3.1-8b-instruct                  | 128k tokens    | Advanced state-of-the-art model with language understanding, superior reasoning, and text generation.                       |
    | meta/llama-3.1-70b-instruct                 | 128k tokens    | Powers complex conversations with superior contextual understanding, reasoning and text generation.                         |
    | meta/llama-3.1-405b-instruct                | 128k tokens    | Advanced LLM for synthetic data generation, distillation, and inference for chatbots, coding, and domain-specific tasks.    |
    | meta/llama-3.2-1b-instruct                  | 128k tokens    | Advanced state-of-the-art small language model with language understanding, superior reasoning, and text generation.        |
    | meta/llama-3.2-3b-instruct                  | 128k tokens    | Advanced state-of-the-art small language model with language understanding, superior reasoning, and text generation.        |
    | meta/llama-3.2-11b-vision-instruct          | 128k tokens    | Advanced state-of-the-art small language model with language understanding, superior reasoning, and text generation.        |
    | meta/llama-3.2-90b-vision-instruct          | 128k tokens    | Advanced state-of-the-art small language model with language understanding, superior reasoning, and text generation.        |
    | google/gemma-7b                             | 8,192 tokens   | Cutting-edge text generation model text understanding, transformation, and code generation.                                 |
    | google/gemma-2b                             | 8,192 tokens   | Cutting-edge text generation model text understanding, transformation, and code generation.                                 |
    | google/codegemma-7b                         | 8,192 tokens   | Cutting-edge model built on Google's Gemma-7B specialized for code generation and code completion.                          |
    | google/codegemma-1.1-7b                     | 8,192 tokens   | Advanced programming model for code generation, completion, reasoning, and instruction following.                           |
    | google/recurrentgemma-2b                    | 8,192 tokens   | Novel recurrent architecture based language model for faster inference when generating long sequences.                      |
    | google/gemma-2-9b-it                        | 8,192 tokens   | Cutting-edge text generation model text understanding, transformation, and code generation.                                 |
    | google/gemma-2-27b-it                       | 8,192 tokens   | Cutting-edge text generation model text understanding, transformation, and code generation.                                 |
    | google/gemma-2-2b-it                        | 8,192 tokens   | Cutting-edge text generation model text understanding, transformation, and code generation.                                 |
    | google/deplot                               | 512 tokens     | One-shot visual language understanding model that translates images of plots into tables.                                   |
    | google/paligemma                            | 8,192 tokens   | Vision language model adept at comprehending text and visual inputs to produce informative responses.                       |
    | mistralai/mistral-7b-instruct-v0.2          | 32k tokens     | This LLM follows instructions, completes requests, and generates creative text.                                             |
    | mistralai/mixtral-8x7b-instruct-v0.1        | 8,192 tokens   | An MOE LLM that follows instructions, completes requests, and generates creative text.                                      |
    | mistralai/mistral-large                     | 4,096 tokens   | Creates diverse synthetic data that mimics the characteristics of real-world data.                                          |
    | mistralai/mixtral-8x22b-instruct-v0.1       | 8,192 tokens   | Creates diverse synthetic data that mimics the characteristics of real-world data.                                          |
    | mistralai/mistral-7b-instruct-v0.3          | 32k tokens     | This LLM follows instructions, completes requests, and generates creative text.                                             |
    | nv-mistralai/mistral-nemo-12b-instruct      | 128k tokens    | Most advanced language model for reasoning, code, multilingual tasks; runs on a single GPU.                                 |
    | mistralai/mamba-codestral-7b-v0.1           | 256k tokens    | Model for writing and interacting with code across a wide range of programming languages and tasks.                         |
    | microsoft/phi-3-mini-128k-instruct          | 128K tokens    | Lightweight, state-of-the-art open LLM with strong math and logical reasoning skills.                                       |
    | microsoft/phi-3-mini-4k-instruct            | 4,096 tokens   | Lightweight, state-of-the-art open LLM with strong math and logical reasoning skills.                                       |
    | microsoft/phi-3-small-8k-instruct           | 8,192 tokens   | Lightweight, state-of-the-art open LLM with strong math and logical reasoning skills.                                       |
    | microsoft/phi-3-small-128k-instruct         | 128K tokens    | Lightweight, state-of-the-art open LLM with strong math and logical reasoning skills.                                       |
    | microsoft/phi-3-medium-4k-instruct          | 4,096 tokens   | Lightweight, state-of-the-art open LLM with strong math and logical reasoning skills.                                       |
    | microsoft/phi-3-medium-128k-instruct        | 128K tokens    | Lightweight, state-of-the-art open LLM with strong math and logical reasoning skills.                                       |
    | microsoft/phi-3.5-mini-instruct             | 128K tokens    | Lightweight multilingual LLM powering AI applications in latency bound, memory/compute constrained environments             |
    | microsoft/phi-3.5-moe-instruct              | 128K tokens    | Advanced LLM based on Mixture of Experts architecture to deliver compute efficient content generation                       |
    | microsoft/kosmos-2                          | 1,024 tokens   | Groundbreaking multimodal model designed to understand and reason about visual elements in images.                          |
    | microsoft/phi-3-vision-128k-instruct        | 128k tokens    | Cutting-edge open multimodal model exceling in high-quality reasoning from images.                                          |
    | microsoft/phi-3.5-vision-instruct           | 128k tokens    | Cutting-edge open multimodal model exceling in high-quality reasoning from images.                                          |
    | databricks/dbrx-instruct                    | 12k tokens     | A general-purpose LLM with state-of-the-art performance in language understanding, coding, and RAG.                         |
    | snowflake/arctic                            | 1,024 tokens   | Delivers high efficiency inference for enterprise applications focused on SQL generation and coding.                        |
    | aisingapore/sea-lion-7b-instruct            | 4,096 tokens   | LLM to represent and serve the linguistic and cultural diversity of Southeast Asia                                          |
    | ibm/granite-8b-code-instruct                | 4,096 tokens   | Software programming LLM for code generation, completion, explanation, and multi-turn conversion.                           |
    | ibm/granite-34b-code-instruct               | 8,192 tokens   | Software programming LLM for code generation, completion, explanation, and multi-turn conversion.                           |
    | ibm/granite-3.0-8b-instruct                 | 4,096 tokens   | Advanced Small Language Model supporting RAG, summarization, classification, code, and agentic AI                           |
    | ibm/granite-3.0-3b-a800m-instruct           | 4,096 tokens   | Highly efficient Mixture of Experts model for RAG, summarization, entity extraction, and classification                     |
    | mediatek/breeze-7b-instruct                 | 4,096 tokens   | Creates diverse synthetic data that mimics the characteristics of real-world data.                                          |
    | upstage/solar-10.7b-instruct                | 4,096 tokens   | Excels in NLP tasks, particularly in instruction-following, reasoning, and mathematics.                                     |
    | writer/palmyra-med-70b-32k                  | 32k tokens     | Leading LLM for accurate, contextually relevant responses in the medical domain.                                            |
    | writer/palmyra-med-70b                      | 32k tokens     | Leading LLM for accurate, contextually relevant responses in the medical domain.                                            |
    | writer/palmyra-fin-70b-32k                  | 32k tokens     | Specialized LLM for financial analysis, reporting, and data processing                                                      |
    | 01-ai/yi-large                              | 32k tokens     | Powerful model trained on English and Chinese for diverse tasks including chatbot and creative writing.                     |
    | deepseek-ai/deepseek-coder-6.7b-instruct    | 2k tokens      | Powerful coding model offering advanced capabilities in code generation, completion, and infilling                          |
    | rakuten/rakutenai-7b-instruct               | 1,024 tokens   | Advanced state-of-the-art LLM with language understanding, superior reasoning, and text generation.                         |
    | rakuten/rakutenai-7b-chat                   | 1,024 tokens   | Advanced state-of-the-art LLM with language understanding, superior reasoning, and text generation.                         |
    | baichuan-inc/baichuan2-13b-chat             | 4,096 tokens   | Support Chinese and English chat, coding, math, instruction following, solving quizzes                                      |
  </Accordion>

  <Accordion title="Local NVIDIA NIM Deployed using WSL2">
    NVIDIA NIM enables you to run powerful LLMs locally on your Windows machine using WSL2 (Windows Subsystem for Linux).
    This approach allows you to leverage your NVIDIA GPU for private, secure, and cost-effective AI inference without relying on cloud services.
    Perfect for development, testing, or production scenarios where data privacy or offline capabilities are required.

    Here is a step-by-step guide to setting up a local NVIDIA NIM model:

    1. Follow installation instructions from [NVIDIA Website](https://docs.nvidia.com/nim/wsl2/latest/getting-started.html)

    2. Install the local model. For Llama 3.1-8b follow [instructions](https://build.nvidia.com/meta/llama-3_1-8b-instruct/deploy)

    3. Configure your crewai local models:

    ```python Code theme={null}
    from crewai.llm import LLM

    local_nvidia_nim_llm = LLM(
        model="openai/meta/llama-3.1-8b-instruct", # it's an openai-api compatible model
        base_url="http://localhost:8000/v1",
        api_key="<your_api_key|any text if you have not configured it>", # api_key is required, but you can use any text
    )

    # Then you can use it in your crew:

    @CrewBase
    class MyCrew():
        # ...

        @agent
        def researcher(self) -> Agent:
            return Agent(
                config=self.agents_config['researcher'], # type: ignore[index]
                llm=local_nvidia_nim_llm
            )

        # ...
    ```
  </Accordion>

  <Accordion title="Groq">
    Set the following environment variables in your `.env` file:

    ```toml Code theme={null}
    GROQ_API_KEY=<your-api-key>
    ```

    Example usage in your CrewAI project:

    ```python Code theme={null}
    llm = LLM(
        model="groq/llama-3.2-90b-text-preview",
        temperature=0.7
    )
    ```

    | Model            | Context Window | Best For                              |
    | ---------------- | -------------- | ------------------------------------- |
    | Llama 3.1 70B/8B | 131,072 tokens | High-performance, large context tasks |
    | Llama 3.2 Series | 8,192 tokens   | General-purpose tasks                 |
    | Mixtral 8x7B     | 32,768 tokens  | Balanced performance and context      |
  </Accordion>

  <Accordion title="IBM watsonx.ai">
    Set the following environment variables in your `.env` file:

    ```toml Code theme={null}
    # Required
    WATSONX_URL=<your-url>
    WATSONX_APIKEY=<your-apikey>
    WATSONX_PROJECT_ID=<your-project-id>

    # Optional
    WATSONX_TOKEN=<your-token>
    WATSONX_DEPLOYMENT_SPACE_ID=<your-space-id>
    ```

    Example usage in your CrewAI project:

    ```python Code theme={null}
    llm = LLM(
        model="watsonx/meta-llama/llama-3-1-70b-instruct",
        base_url="https://api.watsonx.ai/v1"
    )
    ```
  </Accordion>

  <Accordion title="Ollama (Local LLMs)">
    1. Install Ollama: [ollama.ai](https://ollama.ai/)
    2. Run a model: `ollama run llama3`
    3. Configure:

    ```python Code theme={null}
    llm = LLM(
        model="ollama/llama3:70b",
        base_url="http://localhost:11434"
    )
    ```
  </Accordion>

  <Accordion title="Fireworks AI">
    Set the following environment variables in your `.env` file:

    ```toml Code theme={null}
    FIREWORKS_API_KEY=<your-api-key>
    ```

    Example usage in your CrewAI project:

    ```python Code theme={null}
    llm = LLM(
        model="fireworks_ai/accounts/fireworks/models/llama-v3-70b-instruct",
        temperature=0.7
    )
    ```
  </Accordion>

  <Accordion title="Perplexity AI">
    Set the following environment variables in your `.env` file:

    ```toml Code theme={null}
    PERPLEXITY_API_KEY=<your-api-key>
    ```

    Example usage in your CrewAI project:

    ```python Code theme={null}
    llm = LLM(
        model="llama-3.1-sonar-large-128k-online",
        base_url="https://api.perplexity.ai/"
    )
    ```
  </Accordion>

  <Accordion title="Hugging Face">
    Set the following environment variables in your `.env` file:

    ```toml Code theme={null}
    HF_TOKEN=<your-api-key>
    ```

    Example usage in your CrewAI project:

    ```python Code theme={null}
    llm = LLM(
        model="huggingface/meta-llama/Meta-Llama-3.1-8B-Instruct"
    )
    ```
  </Accordion>

  <Accordion title="SambaNova">
    Set the following environment variables in your `.env` file:

    ```toml Code theme={null}
    SAMBANOVA_API_KEY=<your-api-key>
    ```

    Example usage in your CrewAI project:

    ```python Code theme={null}
    llm = LLM(
        model="sambanova/Meta-Llama-3.1-8B-Instruct",
        temperature=0.7
    )
    ```

    | Model            | Context Window       | Best For                              |
    | ---------------- | -------------------- | ------------------------------------- |
    | Llama 3.1 70B/8B | Up to 131,072 tokens | High-performance, large context tasks |
    | Llama 3.1 405B   | 8,192 tokens         | High-performance and output quality   |
    | Llama 3.2 Series | 8,192 tokens         | General-purpose, multimodal tasks     |
    | Llama 3.3 70B    | Up to 131,072 tokens | High-performance and output quality   |
    | Qwen2 familly    | 8,192 tokens         | High-performance and output quality   |
  </Accordion>

  <Accordion title="Cerebras">
    Set the following environment variables in your `.env` file:

    ```toml Code theme={null}
    # Required
    CEREBRAS_API_KEY=<your-api-key>
    ```

    Example usage in your CrewAI project:

    ```python Code theme={null}
    llm = LLM(
        model="cerebras/llama3.1-70b",
        temperature=0.7,
        max_tokens=8192
    )
    ```

    <Info>
      Cerebras features:

      * Fast inference speeds
      * Competitive pricing
      * Good balance of speed and quality
      * Support for long context windows
    </Info>
  </Accordion>

  <Accordion title="Open Router">
    Set the following environment variables in your `.env` file:

    ```toml Code theme={null}
    OPENROUTER_API_KEY=<your-api-key>
    ```

    Example usage in your CrewAI project:

    ```python Code theme={null}
    llm = LLM(
        model="openrouter/deepseek/deepseek-r1",
        base_url="https://openrouter.ai/api/v1",
        api_key=OPENROUTER_API_KEY
    )
    ```

    <Info>
      Open Router models:

      * openrouter/deepseek/deepseek-r1
      * openrouter/deepseek/deepseek-chat
    </Info>
  </Accordion>

  <Accordion title="Nebius AI Studio">
    Set the following environment variables in your `.env` file:

    ```toml Code theme={null}
    NEBIUS_API_KEY=<your-api-key>
    ```

    Example usage in your CrewAI project:

    ```python Code theme={null}
    llm = LLM(
        model="nebius/Qwen/Qwen3-30B-A3B"
    )
    ```

    <Info>
      Nebius AI Studio features:

      * Large collection of open source models
      * Higher rate limits
      * Competitive pricing
      * Good balance of speed and quality
    </Info>
  </Accordion>
</AccordionGroup>


## Streaming Responses

CrewAI supports streaming responses from LLMs, allowing your application to receive and process outputs in real-time as they're generated.

<Tabs>
  <Tab title="Basic Setup">
    Enable streaming by setting the `stream` parameter to `True` when initializing your LLM:

    ```python  theme={null}
    from crewai import LLM

    # Create an LLM with streaming enabled
    llm = LLM(
        model="openai/gpt-4o",
        stream=True  # Enable streaming
    )
    ```

    When streaming is enabled, responses are delivered in chunks as they're generated, creating a more responsive user experience.
  </Tab>

  <Tab title="Event Handling">
    CrewAI emits events for each chunk received during streaming:

    ```python  theme={null}
    from crewai.events import (
      LLMStreamChunkEvent
    )
    from crewai.events import BaseEventListener

    class MyCustomListener(BaseEventListener):
        def setup_listeners(self, crewai_event_bus):
            @crewai_event_bus.on(LLMStreamChunkEvent)
            def on_llm_stream_chunk(self, event: LLMStreamChunkEvent):
              # Process each chunk as it arrives
              print(f"Received chunk: {event.chunk}")

    my_listener = MyCustomListener()
    ```

    <Tip>
      [Click here](https://docs.crewai.com/concepts/event-listener#event-listeners) for more details
    </Tip>
  </Tab>

  <Tab title="Agent & Task Tracking">
    All LLM events in CrewAI include agent and task information, allowing you to track and filter LLM interactions by specific agents or tasks:

    ```python  theme={null}
    from crewai import LLM, Agent, Task, Crew
    from crewai.events import LLMStreamChunkEvent
    from crewai.events import BaseEventListener

    class MyCustomListener(BaseEventListener):
        def setup_listeners(self, crewai_event_bus):
            @crewai_event_bus.on(LLMStreamChunkEvent)
            def on_llm_stream_chunk(source, event):
                if researcher.id == event.agent_id:
                    print("\n==============\n Got event:", event, "\n==============\n")


    my_listener = MyCustomListener()

    llm = LLM(model="gpt-4o-mini", temperature=0, stream=True)

    researcher = Agent(
        role="About User",
        goal="You know everything about the user.",
        backstory="""You are a master at understanding people and their preferences.""",
        llm=llm,
    )

    search = Task(
        description="Answer the following questions about the user: {question}",
        expected_output="An answer to the question.",
        agent=researcher,
    )

    crew = Crew(agents=[researcher], tasks=[search])

    result = crew.kickoff(
        inputs={"question": "..."}
    )
    ```

    <Info>
      This feature is particularly useful for:

      * Debugging specific agent behaviors
      * Logging LLM usage by task type
      * Auditing which agents are making what types of LLM calls
      * Performance monitoring of specific tasks
    </Info>
  </Tab>
</Tabs>


## Structured LLM Calls

CrewAI supports structured responses from LLM calls by allowing you to define a `response_format` using a Pydantic model. This enables the framework to automatically parse and validate the output, making it easier to integrate the response into your application without manual post-processing.

For example, you can define a Pydantic model to represent the expected response structure and pass it as the `response_format` when instantiating the LLM. The model will then be used to convert the LLM output into a structured Python object.

```python Code theme={null}
from crewai import LLM

class Dog(BaseModel):
    name: str
    age: int
    breed: str


llm = LLM(model="gpt-4o", response_format=Dog)

response = llm.call(
    "Analyze the following messages and return the name, age, and breed. "
    "Meet Kona! She is 3 years old and is a black german shepherd."
)
print(response)


# Output:

# Dog(name='Kona', age=3, breed='black german shepherd')
```


## Advanced Features and Optimization

Learn how to get the most out of your LLM configuration:

<AccordionGroup>
  <Accordion title="Context Window Management">
    CrewAI includes smart context management features:

    ```python  theme={null}
    from crewai import LLM

    # CrewAI automatically handles:
    # 1. Token counting and tracking
    # 2. Content summarization when needed
    # 3. Task splitting for large contexts

    llm = LLM(
        model="gpt-4",
        max_tokens=4000,  # Limit response length
    )
    ```

    <Info>
      Best practices for context management:

      1. Choose models with appropriate context windows
      2. Pre-process long inputs when possible
      3. Use chunking for large documents
      4. Monitor token usage to optimize costs
    </Info>
  </Accordion>

  <Accordion title="Performance Optimization">
    <Steps>
      <Step title="Token Usage Optimization">
        Choose the right context window for your task:

        * Small tasks (up to 4K tokens): Standard models
        * Medium tasks (between 4K-32K): Enhanced models
        * Large tasks (over 32K): Large context models

        ```python  theme={null}
        # Configure model with appropriate settings
        llm = LLM(
            model="openai/gpt-4-turbo-preview",
            temperature=0.7,    # Adjust based on task
            max_tokens=4096,    # Set based on output needs
            timeout=300        # Longer timeout for complex tasks
        )
        ```

        <Tip>
          * Lower temperature (0.1 to 0.3) for factual responses
          * Higher temperature (0.7 to 0.9) for creative tasks
        </Tip>
      </Step>

      <Step title="Best Practices">
        1. Monitor token usage
        2. Implement rate limiting
        3. Use caching when possible
        4. Set appropriate max\_tokens limits
      </Step>
    </Steps>

    <Info>
      Remember to regularly monitor your token usage and adjust your configuration as needed to optimize costs and performance.
    </Info>
  </Accordion>

  <Accordion title="Drop Additional Parameters">
    CrewAI internally uses native sdks for LLM calls, which allows you to drop additional parameters that are not needed for your specific use case. This can help simplify your code and reduce the complexity of your LLM configuration.
    For example, if you don't need to send the <code>stop</code> parameter, you can simply omit it from your LLM call:

    ```python  theme={null}
    from crewai import LLM
    import os

    os.environ["OPENAI_API_KEY"] = "<api-key>"

    o3_llm = LLM(
        model="o3",
        drop_params=True,
        additional_drop_params=["stop"]
    )
    ```
  </Accordion>

  <Accordion title="Transport Interceptors">
    CrewAI provides message interceptors for several providers, allowing you to hook into request/response cycles at the transport layer.

    **Supported Providers:**

    * ✅ OpenAI
    * ✅ Anthropic

    **Basic Usage:**

    ```python  theme={null}
    import httpx
    from crewai import LLM
    from crewai.llms.hooks import BaseInterceptor

    class CustomInterceptor(BaseInterceptor[httpx.Request, httpx.Response]):
    """Custom interceptor to modify requests and responses."""

    def on_outbound(self, request: httpx.Request) -> httpx.Request:
        """Print request before sending to the LLM provider."""
        print(request)
        return request

    def on_inbound(self, response: httpx.Response) -> httpx.Response:
        """Process response after receiving from the LLM provider."""
        print(f"Status: {response.status_code}")
        print(f"Response time: {response.elapsed}")
        return response

    # Use the interceptor with an LLM
    llm = LLM(
    model="openai/gpt-4o",
    interceptor=CustomInterceptor()
    )
    ```

    **Important Notes:**

    * Both methods must return the received object or type of object.
    * Modifying received objects may result in unexpected behavior or application crashes.
    * Not all providers support interceptors - check the supported providers list above

    <Info>
      Interceptors operate at the transport layer. This is particularly useful for:

      * Message transformation and filtering
      * Debugging API interactions
    </Info>
  </Accordion>
</AccordionGroup>


## Common Issues and Solutions

<Tabs>
  <Tab title="Authentication">
    <Warning>
      Most authentication issues can be resolved by checking API key format and environment variable names.
    </Warning>

    ```bash  theme={null}
    # OpenAI
    OPENAI_API_KEY=sk-...

    # Anthropic
    ANTHROPIC_API_KEY=sk-ant-...
    ```
  </Tab>

  <Tab title="Model Names">
    <Check>
      Always include the provider prefix in model names
    </Check>

    ```python  theme={null}
    # Correct
    llm = LLM(model="openai/gpt-4")

    # Incorrect
    llm = LLM(model="gpt-4")
    ```
  </Tab>

  <Tab title="Context Length">
    <Tip>
      Use larger context models for extensive tasks
    </Tip>

    ```python  theme={null}
    # Large context model
    llm = LLM(model="openai/gpt-4o")  # 128K tokens
    ```
  </Tab>
</Tabs>



# Memory
Source: https://docs.crewai.com/en/concepts/memory

Leveraging memory systems in the CrewAI framework to enhance agent capabilities.


## Overview

The CrewAI framework provides a sophisticated memory system designed to significantly enhance AI agent capabilities. CrewAI offers **two distinct memory approaches** that serve different use cases:

1. **Basic Memory System** - Built-in short-term, long-term, and entity memory
2. **External Memory** - Standalone external memory providers


## Memory System Components

| Component             | Description                                                                                                                                                                                                                       |
| :-------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Short-Term Memory** | Temporarily stores recent interactions and outcomes using `RAG`, enabling agents to recall and utilize information relevant to their current context during the current executions.                                               |
| **Long-Term Memory**  | Preserves valuable insights and learnings from past executions, allowing agents to build and refine their knowledge over time.                                                                                                    |
| **Entity Memory**     | Captures and organizes information about entities (people, places, concepts) encountered during tasks, facilitating deeper understanding and relationship mapping. Uses `RAG` for storing entity information.                     |
| **Contextual Memory** | Maintains the context of interactions by combining `ShortTermMemory`, `LongTermMemory`, `ExternalMemory` and `EntityMemory`, aiding in the coherence and relevance of agent responses over a sequence of tasks or a conversation. |


## 1. Basic Memory System (Recommended)

The simplest and most commonly used approach. Enable memory for your crew with a single parameter:

### Quick Start

```python  theme={null}
from crewai import Crew, Agent, Task, Process


# Enable basic memory system
crew = Crew(
    agents=[...],
    tasks=[...],
    process=Process.sequential,
    memory=True,  # Enables short-term, long-term, and entity memory
    verbose=True
)
```

### How It Works

* **Short-Term Memory**: Uses ChromaDB with RAG for current context
* **Long-Term Memory**: Uses SQLite3 to store task results across sessions
* **Entity Memory**: Uses RAG to track entities (people, places, concepts)
* **Storage Location**: Platform-specific location via `appdirs` package
* **Custom Storage Directory**: Set `CREWAI_STORAGE_DIR` environment variable


## Storage Location Transparency

<Info>
  **Understanding Storage Locations**: CrewAI uses platform-specific directories to store memory and knowledge files following OS conventions. Understanding these locations helps with production deployments, backups, and debugging.
</Info>

### Where CrewAI Stores Files

By default, CrewAI uses the `appdirs` library to determine storage locations following platform conventions. Here's exactly where your files are stored:

#### Default Storage Locations by Platform

**macOS:**

```
~/Library/Application Support/CrewAI/{project_name}/
├── knowledge/           # Knowledge base ChromaDB files
├── short_term_memory/   # Short-term memory ChromaDB files
├── long_term_memory/    # Long-term memory ChromaDB files
├── entities/            # Entity memory ChromaDB files
└── long_term_memory_storage.db  # SQLite database
```

**Linux:**

```
~/.local/share/CrewAI/{project_name}/
├── knowledge/
├── short_term_memory/
├── long_term_memory/
├── entities/
└── long_term_memory_storage.db
```

**Windows:**

```
C:\Users\{username}\AppData\Local\CrewAI\{project_name}\
├── knowledge\
├── short_term_memory\
├── long_term_memory\
├── entities\
└── long_term_memory_storage.db
```

### Finding Your Storage Location

To see exactly where CrewAI is storing files on your system:

```python  theme={null}
from crewai.utilities.paths import db_storage_path
import os


# Get the base storage path
storage_path = db_storage_path()
print(f"CrewAI storage location: {storage_path}")


# List all CrewAI storage directories
if os.path.exists(storage_path):
    print("\nStored files and directories:")
    for item in os.listdir(storage_path):
        item_path = os.path.join(storage_path, item)
        if os.path.isdir(item_path):
            print(f"📁 {item}/")
            # Show ChromaDB collections
            if os.path.exists(item_path):
                for subitem in os.listdir(item_path):
                    print(f"   └── {subitem}")
        else:
            print(f"📄 {item}")
else:
    print("No CrewAI storage directory found yet.")
```

### Controlling Storage Locations

#### Option 1: Environment Variable (Recommended)

```python  theme={null}
import os
from crewai import Crew


# Set custom storage location
os.environ["CREWAI_STORAGE_DIR"] = "./my_project_storage"


# All memory and knowledge will now be stored in ./my_project_storage/
crew = Crew(
    agents=[...],
    tasks=[...],
    memory=True
)
```

#### Option 2: Custom Storage Paths

```python  theme={null}
import os
from crewai import Crew
from crewai.memory import LongTermMemory
from crewai.memory.storage.ltm_sqlite_storage import LTMSQLiteStorage


# Configure custom storage location
custom_storage_path = "./storage"
os.makedirs(custom_storage_path, exist_ok=True)

crew = Crew(
    memory=True,
    long_term_memory=LongTermMemory(
        storage=LTMSQLiteStorage(
            db_path=f"{custom_storage_path}/memory.db"
        )
    )
)
```

#### Option 3: Project-Specific Storage

```python  theme={null}
import os
from pathlib import Path


# Store in project directory
project_root = Path(__file__).parent
storage_dir = project_root / "crewai_storage"

os.environ["CREWAI_STORAGE_DIR"] = str(storage_dir)


# Now all storage will be in your project directory
```

### Embedding Provider Defaults

<Info>
  **Default Embedding Provider**: CrewAI defaults to OpenAI embeddings for consistency and reliability. You can easily customize this to match your LLM provider or use local embeddings.
</Info>

#### Understanding Default Behavior

```python  theme={null}

# When using Claude as your LLM...
from crewai import Agent, LLM

agent = Agent(
    role="Analyst",
    goal="Analyze data",
    backstory="Expert analyst",
    llm=LLM(provider="anthropic", model="claude-3-sonnet")  # Using Claude
)


# CrewAI will use OpenAI embeddings by default for consistency

# You can easily customize this to match your preferred provider
```

#### Customizing Embedding Providers

```python  theme={null}
from crewai import Crew


# Option 1: Match your LLM provider
crew = Crew(
    agents=[agent],
    tasks=[task],
    memory=True,
    embedder={
        "provider": "anthropic", # Match your LLM provider
        "config": {
            "api_key": "your-anthropic-key",
            "model": "text-embedding-3-small"
        }
    }
)


# Option 2: Use local embeddings (no external API calls)
crew = Crew(
    agents=[agent],
    tasks=[task],
    memory=True,
    embedder={
        "provider": "ollama",
        "config": {"model": "mxbai-embed-large"}
    }
)
```

### Debugging Storage Issues

#### Check Storage Permissions

```python  theme={null}
import os
from crewai.utilities.paths import db_storage_path

storage_path = db_storage_path()
print(f"Storage path: {storage_path}")
print(f"Path exists: {os.path.exists(storage_path)}")
print(f"Is writable: {os.access(storage_path, os.W_OK) if os.path.exists(storage_path) else 'Path does not exist'}")


# Create with proper permissions
if not os.path.exists(storage_path):
    os.makedirs(storage_path, mode=0o755, exist_ok=True)
    print(f"Created storage directory: {storage_path}")
```

#### Inspect ChromaDB Collections

```python  theme={null}
import chromadb
from crewai.utilities.paths import db_storage_path


# Connect to CrewAI's ChromaDB
storage_path = db_storage_path()
chroma_path = os.path.join(storage_path, "knowledge")

if os.path.exists(chroma_path):
    client = chromadb.PersistentClient(path=chroma_path)
    collections = client.list_collections()

    print("ChromaDB Collections:")
    for collection in collections:
        print(f"  - {collection.name}: {collection.count()} documents")
else:
    print("No ChromaDB storage found")
```

#### Reset Storage (Debugging)

```python  theme={null}
from crewai import Crew


# Reset all memory storage
crew = Crew(agents=[...], tasks=[...], memory=True)


# Reset specific memory types
crew.reset_memories(command_type='short')     # Short-term memory
crew.reset_memories(command_type='long')      # Long-term memory
crew.reset_memories(command_type='entity')    # Entity memory
crew.reset_memories(command_type='knowledge') # Knowledge storage
```

### Production Best Practices

1. **Set `CREWAI_STORAGE_DIR`** to a known location in production for better control
2. **Choose explicit embedding providers** to match your LLM setup
3. **Monitor storage directory size** for large-scale deployments
4. **Include storage directories** in your backup strategy
5. **Set appropriate file permissions** (0o755 for directories, 0o644 for files)
6. **Use project-relative paths** for containerized deployments

### Common Storage Issues

**"ChromaDB permission denied" errors:**

```bash  theme={null}

# Fix permissions
chmod -R 755 ~/.local/share/CrewAI/
```

**"Database is locked" errors:**

```python  theme={null}

# Ensure only one CrewAI instance accesses storage
import fcntl
import os

storage_path = db_storage_path()
lock_file = os.path.join(storage_path, ".crewai.lock")

with open(lock_file, 'w') as f:
    fcntl.flock(f.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
    # Your CrewAI code here
```

**Storage not persisting between runs:**

```python  theme={null}

# Verify storage location is consistent
import os
print("CREWAI_STORAGE_DIR:", os.getenv("CREWAI_STORAGE_DIR"))
print("Current working directory:", os.getcwd())
print("Computed storage path:", db_storage_path())
```


## Custom Embedder Configuration

CrewAI supports multiple embedding providers to give you flexibility in choosing the best option for your use case. Here's a comprehensive guide to configuring different embedding providers for your memory system.

### Why Choose Different Embedding Providers?

* **Cost Optimization**: Local embeddings (Ollama) are free after initial setup
* **Privacy**: Keep your data local with Ollama or use your preferred cloud provider
* **Performance**: Some models work better for specific domains or languages
* **Consistency**: Match your embedding provider with your LLM provider
* **Compliance**: Meet specific regulatory or organizational requirements

### OpenAI Embeddings (Default)

OpenAI provides reliable, high-quality embeddings that work well for most use cases.

```python  theme={null}
from crewai import Crew


# Basic OpenAI configuration (uses environment OPENAI_API_KEY)
crew = Crew(
    agents=[...],
    tasks=[...],
    memory=True,
    embedder={
        "provider": "openai",
        "config": {
            "model": "text-embedding-3-small"  # or "text-embedding-3-large"
        }
    }
)


# Advanced OpenAI configuration
crew = Crew(
    memory=True,
    embedder={
        "provider": "openai",
        "config": {
            "api_key": "your-openai-api-key",  # Optional: override env var
            "model": "text-embedding-3-large",
            "dimensions": 1536,  # Optional: reduce dimensions for smaller storage
            "organization_id": "your-org-id"  # Optional: for organization accounts
        }
    }
)
```

### Azure OpenAI Embeddings

For enterprise users with Azure OpenAI deployments.

```python  theme={null}
crew = Crew(
    memory=True,
    embedder={
        "provider": "openai",  # Use openai provider for Azure
        "config": {
            "api_key": "your-azure-api-key",
            "api_base": "https://your-resource.openai.azure.com/",
            "api_type": "azure",
            "api_version": "2023-05-15",
            "model": "text-embedding-3-small",
            "deployment_id": "your-deployment-name"  # Azure deployment name
        }
    }
)
```

### Google AI Embeddings

Use Google's text embedding models for integration with Google Cloud services.

```python  theme={null}
crew = Crew(
    memory=True,
    embedder={
        "provider": "google",
        "config": {
            "api_key": "your-google-api-key",
            "model": "text-embedding-004"  # or "text-embedding-preview-0409"
        }
    }
)
```

### Vertex AI Embeddings

For Google Cloud users with Vertex AI access.

```python  theme={null}
crew = Crew(
    memory=True,
    embedder={
        "provider": "vertexai",
        "config": {
            "project_id": "your-gcp-project-id",
            "region": "us-central1",  # or your preferred region
            "api_key": "your-service-account-key",
            "model_name": "textembedding-gecko"
        }
    }
)
```

### Ollama Embeddings (Local)

Run embeddings locally for privacy and cost savings.

```python  theme={null}

# First, install and run Ollama locally, then pull an embedding model:

# ollama pull mxbai-embed-large

crew = Crew(
    memory=True,
    embedder={
        "provider": "ollama",
        "config": {
            "model": "mxbai-embed-large",  # or "nomic-embed-text"
            "url": "http://localhost:11434/api/embeddings"  # Default Ollama URL
        }
    }
)


# For custom Ollama installations
crew = Crew(
    memory=True,
    embedder={
        "provider": "ollama",
        "config": {
            "model": "mxbai-embed-large",
            "url": "http://your-ollama-server:11434/api/embeddings"
        }
    }
)
```

### Cohere Embeddings

Use Cohere's embedding models for multilingual support.

```python  theme={null}
crew = Crew(
    memory=True,
    embedder={
        "provider": "cohere",
        "config": {
            "api_key": "your-cohere-api-key",
            "model": "embed-english-v3.0"  # or "embed-multilingual-v3.0"
        }
    }
)
```

### VoyageAI Embeddings

High-performance embeddings optimized for retrieval tasks.

```python  theme={null}
crew = Crew(
    memory=True,
    embedder={
        "provider": "voyageai",
        "config": {
            "api_key": "your-voyage-api-key",
            "model": "voyage-large-2",  # or "voyage-code-2" for code
            "input_type": "document"  # or "query"
        }
    }
)
```

### AWS Bedrock Embeddings

For AWS users with Bedrock access.

```python  theme={null}
crew = Crew(
    memory=True,
    embedder={
        "provider": "bedrock",
        "config": {
            "aws_access_key_id": "your-access-key",
            "aws_secret_access_key": "your-secret-key",
            "region_name": "us-east-1",
            "model": "amazon.titan-embed-text-v1"
        }
    }
)
```

### Hugging Face Embeddings

Use open-source models from Hugging Face.

```python  theme={null}
crew = Crew(
    memory=True,
    embedder={
        "provider": "huggingface",
        "config": {
            "api_key": "your-hf-token",  # Optional for public models
            "model": "sentence-transformers/all-MiniLM-L6-v2",
            "api_url": "https://api-inference.huggingface.co"  # or your custom endpoint
        }
    }
)
```

### IBM Watson Embeddings

For IBM Cloud users.

```python  theme={null}
crew = Crew(
    memory=True,
    embedder={
        "provider": "watson",
        "config": {
            "api_key": "your-watson-api-key",
            "url": "your-watson-instance-url",
            "model": "ibm/slate-125m-english-rtrvr"
        }
    }
)
```

### Mem0 Provider

Short-Term Memory and Entity Memory both supports a tight integration with both Mem0 OSS and Mem0 Client as a provider. Here is how you can use Mem0 as a provider.

```python  theme={null}
from crewai.memory.short_term.short_term_memory import ShortTermMemory
from crewai.memory.entity_entity_memory import EntityMemory

mem0_oss_embedder_config = {
        "provider": "mem0",
        "config": {
            "user_id": "john",
            "local_mem0_config": {
                "vector_store": {"provider": "qdrant","config": {"host": "localhost", "port": 6333}},
                "llm": {"provider": "openai","config": {"api_key": "your-api-key", "model": "gpt-4"}},
                "embedder": {"provider": "openai","config": {"api_key": "your-api-key", "model": "text-embedding-3-small"}}
            },
            "infer": True # Optional defaults to True
        },
    }


mem0_client_embedder_config = {
        "provider": "mem0",
        "config": {
            "user_id": "john",
            "org_id": "my_org_id",        # Optional
            "project_id": "my_project_id", # Optional
            "api_key": "custom-api-key"    # Optional - overrides env var
            "run_id": "my_run_id",        # Optional - for short-term memory
            "includes": "include1",       # Optional 
            "excludes": "exclude1",       # Optional
            "infer": True                 # Optional defaults to True
            "custom_categories": new_categories  # Optional - custom categories for user memory
        },
    }


short_term_memory_mem0_oss = ShortTermMemory(embedder_config=mem0_oss_embedder_config) # Short Term Memory with Mem0 OSS
short_term_memory_mem0_client = ShortTermMemory(embedder_config=mem0_client_embedder_config) # Short Term Memory with Mem0 Client
entity_memory_mem0_oss = EntityMemory(embedder_config=mem0_oss_embedder_config) # Entity Memory with Mem0 OSS
entity_memory_mem0_client = EntityMemory(embedder_config=mem0_client_embedder_config) # Short Term Memory with Mem0 Client

crew = Crew(
    memory=True,
    short_term_memory=short_term_memory_mem0_oss, # or short_term_memory_mem0_client
    entity_memory=entity_memory_mem0_oss # or entity_memory_mem0_client
)
```

### Choosing the Right Embedding Provider

When selecting an embedding provider, consider factors like performance, privacy, cost, and integration needs.\
Below is a comparison to help you decide:

| Provider         | Best For                        | Pros                                | Cons                              |
| ---------------- | ------------------------------- | ----------------------------------- | --------------------------------- |
| **OpenAI**       | General use, high reliability   | High quality, widely tested         | Paid service, API key required    |
| **Ollama**       | Privacy-focused, cost savings   | Free, runs locally, fully private   | Requires local installation/setup |
| **Google AI**    | Integration in Google ecosystem | Strong performance, good support    | Google account required           |
| **Azure OpenAI** | Enterprise & compliance needs   | Enterprise-grade features, security | More complex setup process        |
| **Cohere**       | Multilingual content handling   | Excellent language support          | More niche use cases              |
| **VoyageAI**     | Information retrieval & search  | Optimized for retrieval tasks       | Relatively new provider           |
| **Mem0**         | Per-user personalization        | Search-optimized embeddings         | Paid service, API key required    |

### Environment Variable Configuration

For security, store API keys in environment variables:

```python  theme={null}
import os


# Set environment variables
os.environ["OPENAI_API_KEY"] = "your-openai-key"
os.environ["GOOGLE_API_KEY"] = "your-google-key"
os.environ["COHERE_API_KEY"] = "your-cohere-key"


# Use without exposing keys in code
crew = Crew(
    memory=True,
    embedder={
        "provider": "openai",
        "config": {
            "model": "text-embedding-3-small"
            # API key automatically loaded from environment
        }
    }
)
```

### Testing Different Embedding Providers

Compare embedding providers for your specific use case:

```python  theme={null}
from crewai import Crew
from crewai.utilities.paths import db_storage_path


# Test different providers with the same data
providers_to_test = [
    {
        "name": "OpenAI",
        "config": {
            "provider": "openai",
            "config": {"model": "text-embedding-3-small"}
        }
    },
    {
        "name": "Ollama",
        "config": {
            "provider": "ollama",
            "config": {"model": "mxbai-embed-large"}
        }
    }
]

for provider in providers_to_test:
    print(f"\nTesting {provider['name']} embeddings...")

    # Create crew with specific embedder
    crew = Crew(
        agents=[...],
        tasks=[...],
        memory=True,
        embedder=provider['config']
    )

    # Run your test and measure performance
    result = crew.kickoff()
    print(f"{provider['name']} completed successfully")
```

### Troubleshooting Embedding Issues

**Model not found errors:**

```python  theme={null}

# Verify model availability
from crewai.rag.embeddings.configurator import EmbeddingConfigurator

configurator = EmbeddingConfigurator()
try:
    embedder = configurator.configure_embedder({
        "provider": "ollama",
        "config": {"model": "mxbai-embed-large"}
    })
    print("Embedder configured successfully")
except Exception as e:
    print(f"Configuration error: {e}")
```

**API key issues:**

```python  theme={null}
import os


# Check if API keys are set
required_keys = ["OPENAI_API_KEY", "GOOGLE_API_KEY", "COHERE_API_KEY"]
for key in required_keys:
    if os.getenv(key):
        print(f"✅ {key} is set")
    else:
        print(f"❌ {key} is not set")
```

**Performance comparison:**

```python  theme={null}
import time

def test_embedding_performance(embedder_config, test_text="This is a test document"):
    start_time = time.time()

    crew = Crew(
        agents=[...],
        tasks=[...],
        memory=True,
        embedder=embedder_config
    )

    # Simulate memory operation
    crew.kickoff()

    end_time = time.time()
    return end_time - start_time


# Compare performance
openai_time = test_embedding_performance({
    "provider": "openai",
    "config": {"model": "text-embedding-3-small"}
})

ollama_time = test_embedding_performance({
    "provider": "ollama",
    "config": {"model": "mxbai-embed-large"}
})

print(f"OpenAI: {openai_time:.2f}s")
print(f"Ollama: {ollama_time:.2f}s")
```

### Entity Memory batching behavior

Entity Memory supports batching when saving multiple entities at once. When you pass a list of `EntityMemoryItem`, the system:

* Emits a single MemorySaveStartedEvent with `entity_count`
* Saves each entity internally, collecting any partial errors
* Emits MemorySaveCompletedEvent with aggregate metadata (saved count, errors)
* Raises a partial-save exception if some entities failed (includes counts)

This improves performance and observability when writing many entities in one operation.


## 2. External Memory

External Memory provides a standalone memory system that operates independently from the crew's built-in memory. This is ideal for specialized memory providers or cross-application memory sharing.

### Basic External Memory with Mem0

```python  theme={null}
import os
from crewai import Agent, Crew, Process, Task
from crewai.memory.external.external_memory import ExternalMemory


# Create external memory instance with local Mem0 Configuration
external_memory = ExternalMemory(
    embedder_config={
        "provider": "mem0",
        "config": {
            "user_id": "john",
            "local_mem0_config": {
                "vector_store": {
                    "provider": "qdrant",
                    "config": {"host": "localhost", "port": 6333}
                },
                "llm": {
                    "provider": "openai",
                    "config": {"api_key": "your-api-key", "model": "gpt-4"}
                },
                "embedder": {
                    "provider": "openai",
                    "config": {"api_key": "your-api-key", "model": "text-embedding-3-small"}
                }
            },
            "infer": True # Optional defaults to True
        },
    }
)

crew = Crew(
    agents=[...],
    tasks=[...],
    external_memory=external_memory, # Separate from basic memory
    process=Process.sequential,
    verbose=True
)
```

### Advanced External Memory with Mem0 Client

When using Mem0 Client, you can customize the memory configuration further, by using parameters like 'includes', 'excludes', 'custom\_categories', 'infer' and 'run\_id' (this is only for short-term memory).
You can find more details in the [Mem0 documentation](https://docs.mem0.ai/).

```python  theme={null}
import os
from crewai import Agent, Crew, Process, Task
from crewai.memory.external.external_memory import ExternalMemory

new_categories = [
    {"lifestyle_management_concerns": "Tracks daily routines, habits, hobbies and interests including cooking, time management and work-life balance"},
    {"seeking_structure": "Documents goals around creating routines, schedules, and organized systems in various life areas"},
    {"personal_information": "Basic information about the user including name, preferences, and personality traits"}
]

os.environ["MEM0_API_KEY"] = "your-api-key"


# Create external memory instance with Mem0 Client
external_memory = ExternalMemory(
    embedder_config={
        "provider": "mem0",
        "config": {
            "user_id": "john",
            "org_id": "my_org_id",        # Optional
            "project_id": "my_project_id", # Optional
            "api_key": "custom-api-key"    # Optional - overrides env var
            "run_id": "my_run_id",        # Optional - for short-term memory
            "includes": "include1",       # Optional 
            "excludes": "exclude1",       # Optional
            "infer": True                 # Optional defaults to True
            "custom_categories": new_categories  # Optional - custom categories for user memory
        },
    }
)

crew = Crew(
    agents=[...],
    tasks=[...],
    external_memory=external_memory, # Separate from basic memory
    process=Process.sequential,
    verbose=True
)
```

### Custom Storage Implementation

```python  theme={null}
from crewai.memory.external.external_memory import ExternalMemory
from crewai.memory.storage.interface import Storage

class CustomStorage(Storage):
    def __init__(self):
        self.memories = []

    def save(self, value, metadata=None, agent=None):
        self.memories.append({
            "value": value,
            "metadata": metadata,
            "agent": agent
        })

    def search(self, query, limit=10, score_threshold=0.5):
        # Implement your search logic here
        return [m for m in self.memories if query.lower() in str(m["value"]).lower()]

    def reset(self):
        self.memories = []


# Use custom storage
external_memory = ExternalMemory(storage=CustomStorage())

crew = Crew(
    agents=[...],
    tasks=[...],
    external_memory=external_memory
)
```


## 🧠 Memory System Comparison

| **Category**        | **Feature**           | **Basic Memory**       | **External Memory**        |
| ------------------- | --------------------- | ---------------------- | -------------------------- |
| **Ease of Use**     | Setup Complexity      | Simple                 | Moderate                   |
|                     | Integration           | Built-in (contextual)  | Standalone                 |
| **Persistence**     | Storage               | Local files            | Custom / Mem0              |
|                     | Cross-session Support | ✅                      | ✅                          |
| **Personalization** | User-specific Memory  | ❌                      | ✅                          |
|                     | Custom Providers      | Limited                | Any provider               |
| **Use Case Fit**    | Recommended For       | Most general use cases | Specialized / custom needs |


## Supported Embedding Providers

### OpenAI (Default)

```python  theme={null}
crew = Crew(
    memory=True,
    embedder={
        "provider": "openai",
        "config": {"model": "text-embedding-3-small"}
    }
)
```

### Ollama

```python  theme={null}
crew = Crew(
    memory=True,
    embedder={
        "provider": "ollama",
        "config": {"model": "mxbai-embed-large"}
    }
)
```

### Google AI

```python  theme={null}
crew = Crew(
    memory=True,
    embedder={
        "provider": "google",
        "config": {
            "api_key": "your-api-key",
            "model": "text-embedding-004"
        }
    }
)
```

### Azure OpenAI

```python  theme={null}
crew = Crew(
    memory=True,
    embedder={
        "provider": "openai",
        "config": {
            "api_key": "your-api-key",
            "api_base": "https://your-resource.openai.azure.com/",
            "api_version": "2023-05-15",
            "model_name": "text-embedding-3-small"
        }
    }
)
```

### Vertex AI

```python  theme={null}
crew = Crew(
    memory=True,
    embedder={
        "provider": "vertexai",
        "config": {
            "project_id": "your-project-id",
            "region": "your-region",
            "api_key": "your-api-key",
            "model_name": "textembedding-gecko"
        }
    }
)
```


## Security Best Practices

### Environment Variables

```python  theme={null}
import os
from crewai import Crew


# Store sensitive data in environment variables
crew = Crew(
    memory=True,
    embedder={
        "provider": "openai",
        "config": {
            "api_key": os.getenv("OPENAI_API_KEY"),
            "model": "text-embedding-3-small"
        }
    }
)
```

### Storage Security

```python  theme={null}
import os
from crewai import Crew
from crewai.memory import LongTermMemory
from crewai.memory.storage.ltm_sqlite_storage import LTMSQLiteStorage


# Use secure storage paths
storage_path = os.getenv("CREWAI_STORAGE_DIR", "./storage")
os.makedirs(storage_path, mode=0o700, exist_ok=True)  # Restricted permissions

crew = Crew(
    memory=True,
    long_term_memory=LongTermMemory(
        storage=LTMSQLiteStorage(
            db_path=f"{storage_path}/memory.db"
        )
    )
)
```


## Troubleshooting

### Common Issues

**Memory not persisting between sessions?**

* Check `CREWAI_STORAGE_DIR` environment variable
* Ensure write permissions to storage directory
* Verify memory is enabled with `memory=True`

**Mem0 authentication errors?**

* Verify `MEM0_API_KEY` environment variable is set
* Check API key permissions on Mem0 dashboard
* Ensure `mem0ai` package is installed

**High memory usage with large datasets?**

* Consider using External Memory with custom storage
* Implement pagination in custom storage search methods
* Use smaller embedding models for reduced memory footprint

### Performance Tips

* Use `memory=True` for most use cases (simplest and fastest)
* Only use User Memory if you need user-specific persistence
* Consider External Memory for high-scale or specialized requirements
* Choose smaller embedding models for faster processing
* Set appropriate search limits to control memory retrieval size


## Benefits of Using CrewAI's Memory System

* 🦾 **Adaptive Learning:** Crews become more efficient over time, adapting to new information and refining their approach to tasks.
* 🫡 **Enhanced Personalization:** Memory enables agents to remember user preferences and historical interactions, leading to personalized experiences.
* 🧠 **Improved Problem Solving:** Access to a rich memory store aids agents in making more informed decisions, drawing on past learnings and contextual insights.


## Memory Events

CrewAI's event system provides powerful insights into memory operations. By leveraging memory events, you can monitor, debug, and optimize your memory system's performance and behavior.

### Available Memory Events

CrewAI emits the following memory-related events:

| Event                             | Description                                                 | Key Properties                                                  |
| :-------------------------------- | :---------------------------------------------------------- | :-------------------------------------------------------------- |
| **MemoryQueryStartedEvent**       | Emitted when a memory query begins                          | `query`, `limit`, `score_threshold`                             |
| **MemoryQueryCompletedEvent**     | Emitted when a memory query completes successfully          | `query`, `results`, `limit`, `score_threshold`, `query_time_ms` |
| **MemoryQueryFailedEvent**        | Emitted when a memory query fails                           | `query`, `limit`, `score_threshold`, `error`                    |
| **MemorySaveStartedEvent**        | Emitted when a memory save operation begins                 | `value`, `metadata`, `agent_role`                               |
| **MemorySaveCompletedEvent**      | Emitted when a memory save operation completes successfully | `value`, `metadata`, `agent_role`, `save_time_ms`               |
| **MemorySaveFailedEvent**         | Emitted when a memory save operation fails                  | `value`, `metadata`, `agent_role`, `error`                      |
| **MemoryRetrievalStartedEvent**   | Emitted when memory retrieval for a task prompt starts      | `task_id`                                                       |
| **MemoryRetrievalCompletedEvent** | Emitted when memory retrieval completes successfully        | `task_id`, `memory_content`, `retrieval_time_ms`                |

### Practical Applications

#### 1. Memory Performance Monitoring

Track memory operation timing to optimize your application:

```python  theme={null}
from crewai.events import (
    BaseEventListener,
    MemoryQueryCompletedEvent,
    MemorySaveCompletedEvent
)
import time

class MemoryPerformanceMonitor(BaseEventListener):
    def __init__(self):
        super().__init__()
        self.query_times = []
        self.save_times = []

    def setup_listeners(self, crewai_event_bus):
        @crewai_event_bus.on(MemoryQueryCompletedEvent)
        def on_memory_query_completed(source, event: MemoryQueryCompletedEvent):
            self.query_times.append(event.query_time_ms)
            print(f"Memory query completed in {event.query_time_ms:.2f}ms. Query: '{event.query}'")
            print(f"Average query time: {sum(self.query_times)/len(self.query_times):.2f}ms")

        @crewai_event_bus.on(MemorySaveCompletedEvent)
        def on_memory_save_completed(source, event: MemorySaveCompletedEvent):
            self.save_times.append(event.save_time_ms)
            print(f"Memory save completed in {event.save_time_ms:.2f}ms")
            print(f"Average save time: {sum(self.save_times)/len(self.save_times):.2f}ms")


# Create an instance of your listener
memory_monitor = MemoryPerformanceMonitor()
```

#### 2. Memory Content Logging

Log memory operations for debugging and insights:

```python  theme={null}
from crewai.events import (
    BaseEventListener,
    MemorySaveStartedEvent,
    MemoryQueryStartedEvent,
    MemoryRetrievalCompletedEvent
)
import logging


# Configure logging
logger = logging.getLogger('memory_events')

class MemoryLogger(BaseEventListener):
    def setup_listeners(self, crewai_event_bus):
        @crewai_event_bus.on(MemorySaveStartedEvent)
        def on_memory_save_started(source, event: MemorySaveStartedEvent):
            if event.agent_role:
                logger.info(f"Agent '{event.agent_role}' saving memory: {event.value[:50]}...")
            else:
                logger.info(f"Saving memory: {event.value[:50]}...")

        @crewai_event_bus.on(MemoryQueryStartedEvent)
        def on_memory_query_started(source, event: MemoryQueryStartedEvent):
            logger.info(f"Memory query started: '{event.query}' (limit: {event.limit})")

        @crewai_event_bus.on(MemoryRetrievalCompletedEvent)
        def on_memory_retrieval_completed(source, event: MemoryRetrievalCompletedEvent):
            if event.task_id:
                logger.info(f"Memory retrieved for task {event.task_id} in {event.retrieval_time_ms:.2f}ms")
            else:
                logger.info(f"Memory retrieved in {event.retrieval_time_ms:.2f}ms")
            logger.debug(f"Memory content: {event.memory_content}")


# Create an instance of your listener
memory_logger = MemoryLogger()
```

#### 3. Error Tracking and Notifications

Capture and respond to memory errors:

```python  theme={null}
from crewai.events import (
    BaseEventListener,
    MemorySaveFailedEvent,
    MemoryQueryFailedEvent
)
import logging
from typing import Optional


# Configure logging
logger = logging.getLogger('memory_errors')

class MemoryErrorTracker(BaseEventListener):
    def __init__(self, notify_email: Optional[str] = None):
        super().__init__()
        self.notify_email = notify_email
        self.error_count = 0

    def setup_listeners(self, crewai_event_bus):
        @crewai_event_bus.on(MemorySaveFailedEvent)
        def on_memory_save_failed(source, event: MemorySaveFailedEvent):
            self.error_count += 1
            agent_info = f"Agent '{event.agent_role}'" if event.agent_role else "Unknown agent"
            error_message = f"Memory save failed: {event.error}. {agent_info}"
            logger.error(error_message)

            if self.notify_email and self.error_count % 5 == 0:
                self._send_notification(error_message)

        @crewai_event_bus.on(MemoryQueryFailedEvent)
        def on_memory_query_failed(source, event: MemoryQueryFailedEvent):
            self.error_count += 1
            error_message = f"Memory query failed: {event.error}. Query: '{event.query}'"
            logger.error(error_message)

            if self.notify_email and self.error_count % 5 == 0:
                self._send_notification(error_message)

    def _send_notification(self, message):
        # Implement your notification system (email, Slack, etc.)
        print(f"[NOTIFICATION] Would send to {self.notify_email}: {message}")


# Create an instance of your listener
error_tracker = MemoryErrorTracker(notify_email="admin@example.com")
```

### Integrating with Analytics Platforms

Memory events can be forwarded to analytics and monitoring platforms to track performance metrics, detect anomalies, and visualize memory usage patterns:

```python  theme={null}
from crewai.events import (
    BaseEventListener,
    MemoryQueryCompletedEvent,
    MemorySaveCompletedEvent
)

class MemoryAnalyticsForwarder(BaseEventListener):
    def __init__(self, analytics_client):
        super().__init__()
        self.client = analytics_client

    def setup_listeners(self, crewai_event_bus):
        @crewai_event_bus.on(MemoryQueryCompletedEvent)
        def on_memory_query_completed(source, event: MemoryQueryCompletedEvent):
            # Forward query metrics to analytics platform
            self.client.track_metric({
                "event_type": "memory_query",
                "query": event.query,
                "duration_ms": event.query_time_ms,
                "result_count": len(event.results) if hasattr(event.results, "__len__") else 0,
                "timestamp": event.timestamp
            })

        @crewai_event_bus.on(MemorySaveCompletedEvent)
        def on_memory_save_completed(source, event: MemorySaveCompletedEvent):
            # Forward save metrics to analytics platform
            self.client.track_metric({
                "event_type": "memory_save",
                "agent_role": event.agent_role,
                "duration_ms": event.save_time_ms,
                "timestamp": event.timestamp
            })
```

### Best Practices for Memory Event Listeners

1. **Keep handlers lightweight**: Avoid complex processing in event handlers to prevent performance impacts
2. **Use appropriate logging levels**: Use INFO for normal operations, DEBUG for details, ERROR for issues
3. **Batch metrics when possible**: Accumulate metrics before sending to external systems
4. **Handle exceptions gracefully**: Ensure your event handlers don't crash due to unexpected data
5. **Consider memory consumption**: Be mindful of storing large amounts of event data


## Conclusion

Integrating CrewAI's memory system into your projects is straightforward. By leveraging the provided memory components and configurations,
you can quickly empower your agents with the ability to remember, reason, and learn from their interactions, unlocking new levels of intelligence and capability.



# Planning
Source: https://docs.crewai.com/en/concepts/planning

Learn how to add planning to your CrewAI Crew and improve their performance.


## Overview

The planning feature in CrewAI allows you to add planning capability to your crew. When enabled, before each Crew iteration,
all Crew information is sent to an AgentPlanner that will plan the tasks step by step, and this plan will be added to each task description.

### Using the Planning Feature

Getting started with the planning feature is very easy, the only step required is to add `planning=True` to your Crew:

<CodeGroup>
  ```python Code theme={null}
  from crewai import Crew, Agent, Task, Process

  # Assemble your crew with planning capabilities
  my_crew = Crew(
      agents=self.agents,
      tasks=self.tasks,
      process=Process.sequential,
      planning=True,
  )
  ```
</CodeGroup>

From this point on, your crew will have planning enabled, and the tasks will be planned before each iteration.

<Warning>
  When planning is enabled, crewAI will use `gpt-4o-mini` as the default LLM for planning, which requires a valid OpenAI API key. Since your agents might be using different LLMs, this could cause confusion if you don't have an OpenAI API key configured or if you're experiencing unexpected behavior related to LLM API calls.
</Warning>

#### Planning LLM

Now you can define the LLM that will be used to plan the tasks.

When running the base case example, you will see something like the output below, which represents the output of the `AgentPlanner`
responsible for creating the step-by-step logic to add to the Agents' tasks.

<CodeGroup>
  ```python Code theme={null}
  from crewai import Crew, Agent, Task, Process

  # Assemble your crew with planning capabilities and custom LLM
  my_crew = Crew(
      agents=self.agents,
      tasks=self.tasks,
      process=Process.sequential,
      planning=True,
      planning_llm="gpt-4o"
  )

  # Run the crew
  my_crew.kickoff()
  ```

  ````markdown Result theme={null}
  [2024-07-15 16:49:11][INFO]: Planning the crew execution
  **Step-by-Step Plan for Task Execution**

  **Task Number 1: Conduct a thorough research about AI LLMs**

  **Agent:** AI LLMs Senior Data Researcher

  **Agent Goal:** Uncover cutting-edge developments in AI LLMs

  **Task Expected Output:** A list with 10 bullet points of the most relevant information about AI LLMs

  **Task Tools:** None specified

  **Agent Tools:** None specified

  **Step-by-Step Plan:**

  1. **Define Research Scope:**

     - Determine the specific areas of AI LLMs to focus on, such as advancements in architecture, use cases, ethical considerations, and performance metrics.

  2. **Identify Reliable Sources:**

     - List reputable sources for AI research, including academic journals, industry reports, conferences (e.g., NeurIPS, ACL), AI research labs (e.g., OpenAI, Google AI), and online databases (e.g., IEEE Xplore, arXiv).

  3. **Collect Data:**

     - Search for the latest papers, articles, and reports published in 2024 and early 2025.
     - Use keywords like "Large Language Models 2025", "AI LLM advancements", "AI ethics 2025", etc.

  4. **Analyze Findings:**

     - Read and summarize the key points from each source.
     - Highlight new techniques, models, and applications introduced in the past year.

  5. **Organize Information:**

     - Categorize the information into relevant topics (e.g., new architectures, ethical implications, real-world applications).
     - Ensure each bullet point is concise but informative.

  6. **Create the List:**

     - Compile the 10 most relevant pieces of information into a bullet point list.
     - Review the list to ensure clarity and relevance.

  **Expected Output:**

  A list with 10 bullet points of the most relevant information about AI LLMs.

  ---

  **Task Number 2: Review the context you got and expand each topic into a full section for a report**

  **Agent:** AI LLMs Reporting Analyst

  **Agent Goal:** Create detailed reports based on AI LLMs data analysis and research findings

  **Task Expected Output:** A fully fledged report with the main topics, each with a full section of information. Formatted as markdown without '```'

  **Task Tools:** None specified

  **Agent Tools:** None specified

  **Step-by-Step Plan:**

  1. **Review the Bullet Points:**
     - Carefully read through the list of 10 bullet points provided by the AI LLMs Senior Data Researcher.

  2. **Outline the Report:**
     - Create an outline with each bullet point as a main section heading.
     - Plan sub-sections under each main heading to cover different aspects of the topic.

  3. **Research Further Details:**
     - For each bullet point, conduct additional research if necessary to gather more detailed information.
     - Look for case studies, examples, and statistical data to support each section.

  4. **Write Detailed Sections:**
     - Expand each bullet point into a comprehensive section.
     - Ensure each section includes an introduction, detailed explanation, examples, and a conclusion.
     - Use markdown formatting for headings, subheadings, lists, and emphasis.

  5. **Review and Edit:**
     - Proofread the report for clarity, coherence, and correctness.
     - Make sure the report flows logically from one section to the next.
     - Format the report according to markdown standards.

  6. **Finalize the Report:**
     - Ensure the report is complete with all sections expanded and detailed.
     - Double-check formatting and make any necessary adjustments.

  **Expected Output:**
  A fully fledged report with the main topics, each with a full section of information. Formatted as markdown without '```'.
  ````
</CodeGroup>



# Processes
Source: https://docs.crewai.com/en/concepts/processes

Detailed guide on workflow management through processes in CrewAI, with updated implementation details.


## Overview

<Tip>
  Processes orchestrate the execution of tasks by agents, akin to project management in human teams.
  These processes ensure tasks are distributed and executed efficiently, in alignment with a predefined strategy.
</Tip>


## Process Implementations

* **Sequential**: Executes tasks sequentially, ensuring tasks are completed in an orderly progression.
* **Hierarchical**: Organizes tasks in a managerial hierarchy, where tasks are delegated and executed based on a structured chain of command. A manager language model (`manager_llm`) or a custom manager agent (`manager_agent`) must be specified in the crew to enable the hierarchical process, facilitating the creation and management of tasks by the manager.
* **Consensual Process (Planned)**: Aiming for collaborative decision-making among agents on task execution, this process type introduces a democratic approach to task management within CrewAI. It is planned for future development and is not currently implemented in the codebase.


## The Role of Processes in Teamwork

Processes enable individual agents to operate as a cohesive unit, streamlining their efforts to achieve common objectives with efficiency and coherence.


## Assigning Processes to a Crew

To assign a process to a crew, specify the process type upon crew creation to set the execution strategy. For a hierarchical process, ensure to define `manager_llm` or `manager_agent` for the manager agent.

```python  theme={null}
from crewai import Crew, Process


# Example: Creating a crew with a sequential process
crew = Crew(
    agents=my_agents,
    tasks=my_tasks,
    process=Process.sequential
)


# Example: Creating a crew with a hierarchical process

# Ensure to provide a manager_llm or manager_agent
crew = Crew(
    agents=my_agents,
    tasks=my_tasks,
    process=Process.hierarchical,
    manager_llm="gpt-4o"
    # or
    # manager_agent=my_manager_agent
)
```

**Note:** Ensure `my_agents` and `my_tasks` are defined prior to creating a `Crew` object, and for the hierarchical process, either `manager_llm` or `manager_agent` is also required.


## Sequential Process

This method mirrors dynamic team workflows, progressing through tasks in a thoughtful and systematic manner. Task execution follows the predefined order in the task list, with the output of one task serving as context for the next.

To customize task context, utilize the `context` parameter in the `Task` class to specify outputs that should be used as context for subsequent tasks.


## Hierarchical Process

Emulates a corporate hierarchy, CrewAI allows specifying a custom manager agent or automatically creates one, requiring the specification of a manager language model (`manager_llm`). This agent oversees task execution, including planning, delegation, and validation. Tasks are not pre-assigned; the manager allocates tasks to agents based on their capabilities, reviews outputs, and assesses task completion.


## Process Class: Detailed Overview

The `Process` class is implemented as an enumeration (`Enum`), ensuring type safety and restricting process values to the defined types (`sequential`, `hierarchical`). The consensual process is planned for future inclusion, emphasizing our commitment to continuous development and innovation.


## Conclusion

The structured collaboration facilitated by processes within CrewAI is crucial for enabling systematic teamwork among agents.
This documentation has been updated to reflect the latest features, enhancements, and the planned integration of the Consensual Process, ensuring users have access to the most current and comprehensive information.



# Reasoning
Source: https://docs.crewai.com/en/concepts/reasoning

Learn how to enable and use agent reasoning to improve task execution.


## Overview

Agent reasoning is a feature that allows agents to reflect on a task and create a plan before execution. This helps agents approach tasks more methodically and ensures they're ready to perform the assigned work.


## Usage

To enable reasoning for an agent, simply set `reasoning=True` when creating the agent:

```python  theme={null}
from crewai import Agent

agent = Agent(
    role="Data Analyst",
    goal="Analyze complex datasets and provide insights",
    backstory="You are an experienced data analyst with expertise in finding patterns in complex data.",
    reasoning=True,  # Enable reasoning
    max_reasoning_attempts=3  # Optional: Set a maximum number of reasoning attempts
)
```


## How It Works

When reasoning is enabled, before executing a task, the agent will:

1. Reflect on the task and create a detailed plan
2. Evaluate whether it's ready to execute the task
3. Refine the plan as necessary until it's ready or max\_reasoning\_attempts is reached
4. Inject the reasoning plan into the task description before execution

This process helps the agent break down complex tasks into manageable steps and identify potential challenges before starting.


## Configuration Options

<ParamField body="reasoning" type="bool" default="False">
  Enable or disable reasoning
</ParamField>

<ParamField body="max_reasoning_attempts" type="int" default="None">
  Maximum number of attempts to refine the plan before proceeding with execution. If None (default), the agent will continue refining until it's ready.
</ParamField>


## Example

Here's a complete example:

```python  theme={null}
from crewai import Agent, Task, Crew


# Create an agent with reasoning enabled
analyst = Agent(
    role="Data Analyst",
    goal="Analyze data and provide insights",
    backstory="You are an expert data analyst.",
    reasoning=True,
    max_reasoning_attempts=3  # Optional: Set a limit on reasoning attempts
)


# Create a task
analysis_task = Task(
    description="Analyze the provided sales data and identify key trends.",
    expected_output="A report highlighting the top 3 sales trends.",
    agent=analyst
)


# Create a crew and run the task
crew = Crew(agents=[analyst], tasks=[analysis_task])
result = crew.kickoff()

print(result)
```


## Error Handling

The reasoning process is designed to be robust, with error handling built in. If an error occurs during reasoning, the agent will proceed with executing the task without the reasoning plan. This ensures that tasks can still be executed even if the reasoning process fails.

Here's how to handle potential errors in your code:

```python  theme={null}
from crewai import Agent, Task
import logging


# Set up logging to capture any reasoning errors
logging.basicConfig(level=logging.INFO)


# Create an agent with reasoning enabled
agent = Agent(
    role="Data Analyst",
    goal="Analyze data and provide insights",
    reasoning=True,
    max_reasoning_attempts=3
)


# Create a task
task = Task(
    description="Analyze the provided sales data and identify key trends.",
    expected_output="A report highlighting the top 3 sales trends.",
    agent=agent
)


# Execute the task

# If an error occurs during reasoning, it will be logged and execution will continue
result = agent.execute_task(task)
```


## Example Reasoning Output

Here's an example of what a reasoning plan might look like for a data analysis task:

```
Task: Analyze the provided sales data and identify key trends.

Reasoning Plan:
I'll analyze the sales data to identify the top 3 trends.

1. Understanding of the task:
   I need to analyze sales data to identify key trends that would be valuable for business decision-making.

2. Key steps I'll take:
   - First, I'll examine the data structure to understand what fields are available
   - Then I'll perform exploratory data analysis to identify patterns
   - Next, I'll analyze sales by time periods to identify temporal trends
   - I'll also analyze sales by product categories and customer segments
   - Finally, I'll identify the top 3 most significant trends

3. Approach to challenges:
   - If the data has missing values, I'll decide whether to fill or filter them
   - If the data has outliers, I'll investigate whether they're valid data points or errors
   - If trends aren't immediately obvious, I'll apply statistical methods to uncover patterns

4. Use of available tools:
   - I'll use data analysis tools to explore and visualize the data
   - I'll use statistical tools to identify significant patterns
   - I'll use knowledge retrieval to access relevant information about sales analysis

5. Expected outcome:
   A concise report highlighting the top 3 sales trends with supporting evidence from the data.

READY: I am ready to execute the task.
```

This reasoning plan helps the agent organize its approach to the task, consider potential challenges, and ensure it delivers the expected output.



# Tasks
Source: https://docs.crewai.com/en/concepts/tasks

Detailed guide on managing and creating tasks within the CrewAI framework.


## Overview

In the CrewAI framework, a `Task` is a specific assignment completed by an `Agent`.

Tasks provide all necessary details for execution, such as a description, the agent responsible, required tools, and more, facilitating a wide range of action complexities.

Tasks within CrewAI can be collaborative, requiring multiple agents to work together. This is managed through the task properties and orchestrated by the Crew's process, enhancing teamwork and efficiency.

<Note type="info" title="Enterprise Enhancement: Visual Task Builder">
  CrewAI AMP includes a Visual Task Builder in Crew Studio that simplifies complex task creation and chaining. Design your task flows visually and test them in real-time without writing code.

    <img src="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-studio-interface.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=c4f5428b111816273b3b53d9cef14fad" alt="Task Builder Screenshot" data-og-width="2654" width="2654" data-og-height="1710" height="1710" data-path="images/enterprise/crew-studio-interface.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-studio-interface.png?w=280&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=35ea9140f0b9e57da5f45adbc7e2f166 280w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-studio-interface.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=ae6f0c18ef3679b5466177710fbc4a94 560w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-studio-interface.png?w=840&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=6c3e2fe013ab4826da90c937a9855635 840w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-studio-interface.png?w=1100&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=7f1474dd7f983532dc910363b96f783a 1100w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-studio-interface.png?w=1650&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=f1a6d7e744e6862af5e72dce4deb0fd1 1650w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-studio-interface.png?w=2500&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=74aeb1ccd8e2c8f84d4247b8d0259737 2500w" />

  The Visual Task Builder enables:

  * Drag-and-drop task creation
  * Visual task dependencies and flow
  * Real-time testing and validation
  * Easy sharing and collaboration
</Note>

### Task Execution Flow

Tasks can be executed in two ways:

* **Sequential**: Tasks are executed in the order they are defined
* **Hierarchical**: Tasks are assigned to agents based on their roles and expertise

The execution flow is defined when creating the crew:

```python Code theme={null}
crew = Crew(
    agents=[agent1, agent2],
    tasks=[task1, task2],
    process=Process.sequential  # or Process.hierarchical
)
```


## Task Attributes

| Attribute                              | Parameters              | Type                        | Description                                                                                                     |
| :------------------------------------- | :---------------------- | :-------------------------- | :-------------------------------------------------------------------------------------------------------------- |
| **Description**                        | `description`           | `str`                       | A clear, concise statement of what the task entails.                                                            |
| **Expected Output**                    | `expected_output`       | `str`                       | A detailed description of what the task's completion looks like.                                                |
| **Name** *(optional)*                  | `name`                  | `Optional[str]`             | A name identifier for the task.                                                                                 |
| **Agent** *(optional)*                 | `agent`                 | `Optional[BaseAgent]`       | The agent responsible for executing the task.                                                                   |
| **Tools** *(optional)*                 | `tools`                 | `List[BaseTool]`            | The tools/resources the agent is limited to use for this task.                                                  |
| **Context** *(optional)*               | `context`               | `Optional[List["Task"]]`    | Other tasks whose outputs will be used as context for this task.                                                |
| **Async Execution** *(optional)*       | `async_execution`       | `Optional[bool]`            | Whether the task should be executed asynchronously. Defaults to False.                                          |
| **Human Input** *(optional)*           | `human_input`           | `Optional[bool]`            | Whether the task should have a human review the final answer of the agent. Defaults to False.                   |
| **Markdown** *(optional)*              | `markdown`              | `Optional[bool]`            | Whether the task should instruct the agent to return the final answer formatted in Markdown. Defaults to False. |
| **Config** *(optional)*                | `config`                | `Optional[Dict[str, Any]]`  | Task-specific configuration parameters.                                                                         |
| **Output File** *(optional)*           | `output_file`           | `Optional[str]`             | File path for storing the task output.                                                                          |
| **Create Directory** *(optional)*      | `create_directory`      | `Optional[bool]`            | Whether to create the directory for output\_file if it doesn't exist. Defaults to True.                         |
| **Output JSON** *(optional)*           | `output_json`           | `Optional[Type[BaseModel]]` | A Pydantic model to structure the JSON output.                                                                  |
| **Output Pydantic** *(optional)*       | `output_pydantic`       | `Optional[Type[BaseModel]]` | A Pydantic model for task output.                                                                               |
| **Callback** *(optional)*              | `callback`              | `Optional[Any]`             | Function/object to be executed after task completion.                                                           |
| **Guardrail** *(optional)*             | `guardrail`             | `Optional[Callable]`        | Function to validate task output before proceeding to next task.                                                |
| **Guardrail Max Retries** *(optional)* | `guardrail_max_retries` | `Optional[int]`             | Maximum number of retries when guardrail validation fails. Defaults to 3.                                       |

<Note type="warning" title="Deprecated: max_retries">
  The task attribute `max_retries` is deprecated and will be removed in v1.0.0.
  Use `guardrail_max_retries` instead to control retry attempts when a guardrail fails.
</Note>


## Creating Tasks

There are two ways to create tasks in CrewAI: using **YAML configuration (recommended)** or defining them **directly in code**.

### YAML Configuration (Recommended)

Using YAML configuration provides a cleaner, more maintainable way to define tasks. We strongly recommend using this approach to define tasks in your CrewAI projects.

After creating your CrewAI project as outlined in the [Installation](/en/installation) section, navigate to the `src/latest_ai_development/config/tasks.yaml` file and modify the template to match your specific task requirements.

<Note>
  Variables in your YAML files (like `{topic}`) will be replaced with values from your inputs when running the crew:

  ```python Code theme={null}
  crew.kickoff(inputs={'topic': 'AI Agents'})
  ```
</Note>

Here's an example of how to configure tasks using YAML:

````yaml tasks.yaml theme={null}
research_task:
  description: >
    Conduct a thorough research about {topic}
    Make sure you find any interesting and relevant information given
    the current year is 2025.
  expected_output: >
    A list with 10 bullet points of the most relevant information about {topic}
  agent: researcher

reporting_task:
  description: >
    Review the context you got and expand each topic into a full section for a report.
    Make sure the report is detailed and contains any and all relevant information.
  expected_output: >
    A fully fledge reports with the mains topics, each with a full section of information.
    Formatted as markdown without '```'
  agent: reporting_analyst
  markdown: true
  output_file: report.md
````

To use this YAML configuration in your code, create a crew class that inherits from `CrewBase`:

```python crew.py theme={null}

---

**Navigation:** [← Previous](./01-agents.md) | [Index](./index.md) | [Next →](./03-srclatestaidevelopmentcrewpy.md)
