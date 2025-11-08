# Overview

**Navigation:** [← Previous](./04-mastering-flow-state-management.md) | [Index](./index.md) | [Next →](./06-website-rag-search.md)

---

# Overview
Source: https://docs.crewai.com/en/tools/ai-ml/overview

Leverage AI services, generate images, process vision, and build intelligent systems

These tools integrate with AI and machine learning services to enhance your agents with advanced capabilities like image generation, vision processing, and intelligent code execution.


## **Available Tools**

<CardGroup cols={2}>
  <Card title="DALL-E Tool" icon="image" href="/en/tools/ai-ml/dalletool">
    Generate AI images using OpenAI's DALL-E model.
  </Card>

  <Card title="Vision Tool" icon="eye" href="/en/tools/ai-ml/visiontool">
    Process and analyze images with computer vision capabilities.
  </Card>

  <Card title="AI Mind Tool" icon="brain" href="/en/tools/ai-ml/aimindtool">
    Advanced AI reasoning and decision-making capabilities.
  </Card>

  <Card title="LlamaIndex Tool" icon="llama" href="/en/tools/ai-ml/llamaindextool">
    Build knowledge bases and retrieval systems with LlamaIndex.
  </Card>

  <Card title="LangChain Tool" icon="link" href="/en/tools/ai-ml/langchaintool">
    Integrate with LangChain for complex AI workflows.
  </Card>

  <Card title="RAG Tool" icon="database" href="/en/tools/ai-ml/ragtool">
    Implement Retrieval-Augmented Generation systems.
  </Card>

  <Card title="Code Interpreter Tool" icon="code" href="/en/tools/ai-ml/codeinterpretertool">
    Execute Python code and perform data analysis.
  </Card>
</CardGroup>


## **Common Use Cases**

* **Content Generation**: Create images, text, and multimedia content
* **Data Analysis**: Execute code and analyze complex datasets
* **Knowledge Systems**: Build RAG systems and intelligent databases
* **Computer Vision**: Process and understand visual content
* **AI Safety**: Implement content moderation and safety checks

```python  theme={null}
from crewai_tools import DallETool, VisionTool, CodeInterpreterTool


# Create AI tools
image_generator = DallETool()
vision_processor = VisionTool()
code_executor = CodeInterpreterTool()


# Add to your agent
agent = Agent(
    role="AI Specialist",
    tools=[image_generator, vision_processor, code_executor],
    goal="Create and analyze content using AI capabilities"
)
```



# RAG Tool
Source: https://docs.crewai.com/en/tools/ai-ml/ragtool

The `RagTool` is a dynamic knowledge base tool for answering questions using Retrieval-Augmented Generation.


# `RagTool`


## Description

The `RagTool` is designed to answer questions by leveraging the power of Retrieval-Augmented Generation (RAG) through CrewAI's native RAG system.
It provides a dynamic knowledge base that can be queried to retrieve relevant information from various data sources.
This tool is particularly useful for applications that require access to a vast array of information and need to provide contextually relevant answers.


## Example

The following example demonstrates how to initialize the tool and use it with different data sources:

```python Code theme={null}
from crewai_tools import RagTool


# Create a RAG tool with default settings
rag_tool = RagTool()


# Add content from a file
rag_tool.add(data_type="file", path="path/to/your/document.pdf")


# Add content from a web page
rag_tool.add(data_type="web_page", url="https://example.com")


# Define an agent with the RagTool
@agent
def knowledge_expert(self) -> Agent:
    '''
    This agent uses the RagTool to answer questions about the knowledge base.
    '''
    return Agent(
        config=self.agents_config["knowledge_expert"],
        allow_delegation=False,
        tools=[rag_tool]
    )
```


## Supported Data Sources

The `RagTool` can be used with a wide variety of data sources, including:

* 📰 PDF files
* 📊 CSV files
* 📃 JSON files
* 📝 Text
* 📁 Directories/Folders
* 🌐 HTML Web pages
* 📽️ YouTube Channels
* 📺 YouTube Videos
* 📚 Documentation websites
* 📝 MDX files
* 📄 DOCX files
* 🧾 XML files
* 📬 Gmail
* 📝 GitHub repositories
* 🐘 PostgreSQL databases
* 🐬 MySQL databases
* 🤖 Slack conversations
* 💬 Discord messages
* 🗨️ Discourse forums
* 📝 Substack newsletters
* 🐝 Beehiiv content
* 💾 Dropbox files
* 🖼️ Images
* ⚙️ Custom data sources


## Parameters

The `RagTool` accepts the following parameters:

* **summarize**: Optional. Whether to summarize the retrieved content. Default is `False`.
* **adapter**: Optional. A custom adapter for the knowledge base. If not provided, a CrewAIRagAdapter will be used.
* **config**: Optional. Configuration for the underlying CrewAI RAG system.


## Adding Content

You can add content to the knowledge base using the `add` method:

```python Code theme={null}

# Add a PDF file
rag_tool.add(data_type="file", path="path/to/your/document.pdf")


# Add a web page
rag_tool.add(data_type="web_page", url="https://example.com")


# Add a YouTube video
rag_tool.add(data_type="youtube_video", url="https://www.youtube.com/watch?v=VIDEO_ID")


# Add a directory of files
rag_tool.add(data_type="directory", path="path/to/your/directory")
```


## Agent Integration Example

Here's how to integrate the `RagTool` with a CrewAI agent:

```python Code theme={null}
from crewai import Agent
from crewai.project import agent
from crewai_tools import RagTool


# Initialize the tool and add content
rag_tool = RagTool()
rag_tool.add(data_type="web_page", url="https://docs.crewai.com")
rag_tool.add(data_type="file", path="company_data.pdf")


# Define an agent with the RagTool
@agent
def knowledge_expert(self) -> Agent:
    return Agent(
        config=self.agents_config["knowledge_expert"],
        allow_delegation=False,
        tools=[rag_tool]
    )
```


## Advanced Configuration

You can customize the behavior of the `RagTool` by providing a configuration dictionary:

```python Code theme={null}
from crewai_tools import RagTool


# Create a RAG tool with custom configuration
config = {
    "vectordb": {
        "provider": "qdrant",
        "config": {
            "collection_name": "my-collection"
        }
    },
    "embedding_model": {
        "provider": "openai",
        "config": {
            "model": "text-embedding-3-small"
        }
    }
}

rag_tool = RagTool(config=config, summarize=True)
```


## Conclusion

The `RagTool` provides a powerful way to create and query knowledge bases from various data sources. By leveraging Retrieval-Augmented Generation, it enables agents to access and retrieve relevant information efficiently, enhancing their ability to provide accurate and contextually appropriate responses.



# Vision Tool
Source: https://docs.crewai.com/en/tools/ai-ml/visiontool

The `VisionTool` is designed to extract text from images.


# `VisionTool`


## Description

This tool is used to extract text from images. When passed to the agent it will extract the text from the image and then use it to generate a response, report or any other output.
The URL or the PATH of the image should be passed to the Agent.


## Installation

Install the crewai\_tools package

```shell  theme={null}
pip install 'crewai[tools]'
```


## Usage

In order to use the VisionTool, the OpenAI API key should be set in the environment variable `OPENAI_API_KEY`.

```python Code theme={null}
from crewai_tools import VisionTool

vision_tool = VisionTool()

@agent
def researcher(self) -> Agent:
    '''
    This agent uses the VisionTool to extract text from images.
    '''
    return Agent(
        config=self.agents_config["researcher"],
        allow_delegation=False,
        tools=[vision_tool]
    )
```


## Arguments

The VisionTool requires the following arguments:

| Argument             | Type     | Description                                                                      |
| :------------------- | :------- | :------------------------------------------------------------------------------- |
| **image\_path\_url** | `string` | **Mandatory**. The path to the image file from which text needs to be extracted. |



# Bedrock Knowledge Base Retriever
Source: https://docs.crewai.com/en/tools/cloud-storage/bedrockkbretriever

Retrieve information from Amazon Bedrock Knowledge Bases using natural language queries


# `BedrockKBRetrieverTool`

The `BedrockKBRetrieverTool` enables CrewAI agents to retrieve information from Amazon Bedrock Knowledge Bases using natural language queries.


## Installation

```bash  theme={null}
uv pip install 'crewai[tools]'
```


## Requirements

* AWS credentials configured (either through environment variables or AWS CLI)
* `boto3` and `python-dotenv` packages
* Access to Amazon Bedrock Knowledge Base


## Usage

Here's how to use the tool with a CrewAI agent:

```python {2, 4-17} theme={null}
from crewai import Agent, Task, Crew
from crewai_tools.aws.bedrock.knowledge_base.retriever_tool import BedrockKBRetrieverTool


# Initialize the tool
kb_tool = BedrockKBRetrieverTool(
    knowledge_base_id="your-kb-id",
    number_of_results=5
)


# Create a CrewAI agent that uses the tool
researcher = Agent(
    role='Knowledge Base Researcher',
    goal='Find information about company policies',
    backstory='I am a researcher specialized in retrieving and analyzing company documentation.',
    tools=[kb_tool],
    verbose=True
)


# Create a task for the agent
research_task = Task(
    description="Find our company's remote work policy and summarize the key points.",
    agent=researcher
)


# Create a crew with the agent
crew = Crew(
    agents=[researcher],
    tasks=[research_task],
    verbose=2
)


# Run the crew
result = crew.kickoff()
print(result)   
```


## Tool Arguments

| Argument                     | Type   | Required | Default | Description                                                                |
| :--------------------------- | :----- | :------- | :------ | :------------------------------------------------------------------------- |
| **knowledge\_base\_id**      | `str`  | Yes      | None    | The unique identifier of the knowledge base (0-10 alphanumeric characters) |
| **number\_of\_results**      | `int`  | No       | 5       | Maximum number of results to return                                        |
| **retrieval\_configuration** | `dict` | No       | None    | Custom configurations for the knowledge base query                         |
| **guardrail\_configuration** | `dict` | No       | None    | Content filtering settings                                                 |
| **next\_token**              | `str`  | No       | None    | Token for pagination                                                       |


## Environment Variables

```bash  theme={null}
BEDROCK_KB_ID=your-knowledge-base-id  # Alternative to passing knowledge_base_id
AWS_REGION=your-aws-region            # Defaults to us-east-1
AWS_ACCESS_KEY_ID=your-access-key     # Required for AWS authentication
AWS_SECRET_ACCESS_KEY=your-secret-key # Required for AWS authentication
```


## Response Format

The tool returns results in JSON format:

```json  theme={null}
{
  "results": [
    {
      "content": "Retrieved text content",
      "content_type": "text",
      "source_type": "S3",
      "source_uri": "s3://bucket/document.pdf",
      "score": 0.95,
      "metadata": {
        "additional": "metadata"
      }
    }
  ],
  "nextToken": "pagination-token",
  "guardrailAction": "NONE"
}
```


## Advanced Usage

### Custom Retrieval Configuration

```python  theme={null}
kb_tool = BedrockKBRetrieverTool(
    knowledge_base_id="your-kb-id",
    retrieval_configuration={
        "vectorSearchConfiguration": {
            "numberOfResults": 10,
            "overrideSearchType": "HYBRID"
        }
    }
)

policy_expert = Agent(
    role='Policy Expert',
    goal='Analyze company policies in detail',
    backstory='I am an expert in corporate policy analysis with deep knowledge of regulatory requirements.',
    tools=[kb_tool]
)
```


## Supported Data Sources

* Amazon S3
* Confluence
* Salesforce
* SharePoint
* Web pages
* Custom document locations
* Amazon Kendra
* SQL databases


## Use Cases

### Enterprise Knowledge Integration

* Enable CrewAI agents to access your organization's proprietary knowledge without exposing sensitive data
* Allow agents to make decisions based on your company's specific policies, procedures, and documentation
* Create agents that can answer questions based on your internal documentation while maintaining data security

### Specialized Domain Knowledge

* Connect CrewAI agents to domain-specific knowledge bases (legal, medical, technical) without retraining models
* Leverage existing knowledge repositories that are already maintained in your AWS environment
* Combine CrewAI's reasoning with domain-specific information from your knowledge bases

### Data-Driven Decision Making

* Ground CrewAI agent responses in your actual company data rather than general knowledge
* Ensure agents provide recommendations based on your specific business context and documentation
* Reduce hallucinations by retrieving factual information from your knowledge bases

### Scalable Information Access

* Access terabytes of organizational knowledge without embedding it all into your models
* Dynamically query only the relevant information needed for specific tasks
* Leverage AWS's scalable infrastructure to handle large knowledge bases efficiently

### Compliance and Governance

* Ensure CrewAI agents provide responses that align with your company's approved documentation
* Create auditable trails of information sources used by your agents
* Maintain control over what information sources your agents can access



# Overview
Source: https://docs.crewai.com/en/tools/cloud-storage/overview

Interact with cloud services, storage systems, and cloud-based AI platforms

These tools enable your agents to interact with cloud services, access cloud storage, and leverage cloud-based AI platforms for scalable operations.


## **Available Tools**

<CardGroup cols={2}>
  <Card title="S3 Reader Tool" icon="cloud" href="/en/tools/cloud-storage/s3readertool">
    Read files and data from Amazon S3 buckets.
  </Card>

  <Card title="S3 Writer Tool" icon="cloud-arrow-up" href="/en/tools/cloud-storage/s3writertool">
    Write and upload files to Amazon S3 storage.
  </Card>

  <Card title="Bedrock Invoke Agent" icon="aws" href="/en/tools/cloud-storage/bedrockinvokeagenttool">
    Invoke Amazon Bedrock agents for AI-powered tasks.
  </Card>

  <Card title="Bedrock KB Retriever" icon="database" href="/en/tools/cloud-storage/bedrockkbretriever">
    Retrieve information from Amazon Bedrock knowledge bases.
  </Card>
</CardGroup>


## **Common Use Cases**

* **File Storage**: Store and retrieve files from cloud storage systems
* **Data Backup**: Backup important data to cloud storage
* **AI Services**: Access cloud-based AI models and services
* **Knowledge Retrieval**: Query cloud-hosted knowledge bases
* **Scalable Operations**: Leverage cloud infrastructure for processing

```python  theme={null}
from crewai_tools import S3ReaderTool, S3WriterTool, BedrockInvokeAgentTool


# Create cloud tools
s3_reader = S3ReaderTool()
s3_writer = S3WriterTool()
bedrock_agent = BedrockInvokeAgentTool()


# Add to your agent
agent = Agent(
    role="Cloud Operations Specialist",
    tools=[s3_reader, s3_writer, bedrock_agent],
    goal="Manage cloud resources and AI services"
)
```



# S3 Reader Tool
Source: https://docs.crewai.com/en/tools/cloud-storage/s3readertool

The `S3ReaderTool` enables CrewAI agents to read files from Amazon S3 buckets.


# `S3ReaderTool`


## Description

The `S3ReaderTool` is designed to read files from Amazon S3 buckets. This tool allows CrewAI agents to access and retrieve content stored in S3, making it ideal for workflows that require reading data, configuration files, or any other content stored in AWS S3 storage.


## Installation

To use this tool, you need to install the required dependencies:

```shell  theme={null}
uv add boto3
```


## Steps to Get Started

To effectively use the `S3ReaderTool`, follow these steps:

1. **Install Dependencies**: Install the required packages using the command above.
2. **Configure AWS Credentials**: Set up your AWS credentials as environment variables.
3. **Initialize the Tool**: Create an instance of the tool.
4. **Specify S3 Path**: Provide the S3 path to the file you want to read.


## Example

The following example demonstrates how to use the `S3ReaderTool` to read a file from an S3 bucket:

```python Code theme={null}
from crewai import Agent, Task, Crew
from crewai_tools.aws.s3 import S3ReaderTool


# Initialize the tool
s3_reader_tool = S3ReaderTool()


# Define an agent that uses the tool
file_reader_agent = Agent(
    role="File Reader",
    goal="Read files from S3 buckets",
    backstory="An expert in retrieving and processing files from cloud storage.",
    tools=[s3_reader_tool],
    verbose=True,
)


# Example task to read a configuration file
read_task = Task(
    description="Read the configuration file from {my_bucket} and summarize its contents.",
    expected_output="A summary of the configuration file contents.",
    agent=file_reader_agent,
)


# Create and run the crew
crew = Crew(agents=[file_reader_agent], tasks=[read_task])
result = crew.kickoff(inputs={"my_bucket": "s3://my-bucket/config/app-config.json"})
```


## Parameters

The `S3ReaderTool` accepts the following parameter when used by an agent:

* **file\_path**: Required. The S3 file path in the format `s3://bucket-name/file-name`.


## AWS Credentials

The tool requires AWS credentials to access S3 buckets. You can configure these credentials using environment variables:

* **CREW\_AWS\_REGION**: The AWS region where your S3 bucket is located. Default is `us-east-1`.
* **CREW\_AWS\_ACCESS\_KEY\_ID**: Your AWS access key ID.
* **CREW\_AWS\_SEC\_ACCESS\_KEY**: Your AWS secret access key.


## Usage

When using the `S3ReaderTool` with an agent, the agent will need to provide the S3 file path:

```python Code theme={null}

# Example of using the tool with an agent
file_reader_agent = Agent(
    role="File Reader",
    goal="Read files from S3 buckets",
    backstory="An expert in retrieving and processing files from cloud storage.",
    tools=[s3_reader_tool],
    verbose=True,
)


# Create a task for the agent to read a specific file
read_config_task = Task(
    description="Read the application configuration file from {my_bucket} and extract the database connection settings.",
    expected_output="The database connection settings from the configuration file.",
    agent=file_reader_agent,
)


# Run the task
crew = Crew(agents=[file_reader_agent], tasks=[read_config_task])
result = crew.kickoff(inputs={"my_bucket": "s3://my-bucket/config/app-config.json"})
```


## Error Handling

The `S3ReaderTool` includes error handling for common S3 issues:

* Invalid S3 path format
* Missing or inaccessible files
* Permission issues
* AWS credential problems

When an error occurs, the tool will return an error message that includes details about the issue.


## Implementation Details

The `S3ReaderTool` uses the AWS SDK for Python (boto3) to interact with S3:

```python Code theme={null}
class S3ReaderTool(BaseTool):
    name: str = "S3 Reader Tool"
    description: str = "Reads a file from Amazon S3 given an S3 file path"
    
    def _run(self, file_path: str) -> str:
        try:
            bucket_name, object_key = self._parse_s3_path(file_path)

            s3 = boto3.client(
                's3',
                region_name=os.getenv('CREW_AWS_REGION', 'us-east-1'),
                aws_access_key_id=os.getenv('CREW_AWS_ACCESS_KEY_ID'),
                aws_secret_access_key=os.getenv('CREW_AWS_SEC_ACCESS_KEY')
            )

            # Read file content from S3
            response = s3.get_object(Bucket=bucket_name, Key=object_key)
            file_content = response['Body'].read().decode('utf-8')

            return file_content
        except ClientError as e:
            return f"Error reading file from S3: {str(e)}"
```


## Conclusion

The `S3ReaderTool` provides a straightforward way to read files from Amazon S3 buckets. By enabling agents to access content stored in S3, it facilitates workflows that require cloud-based file access. This tool is particularly useful for data processing, configuration management, and any task that involves retrieving information from AWS S3 storage.



# S3 Writer Tool
Source: https://docs.crewai.com/en/tools/cloud-storage/s3writertool

The `S3WriterTool` enables CrewAI agents to write content to files in Amazon S3 buckets.


# `S3WriterTool`


## Description

The `S3WriterTool` is designed to write content to files in Amazon S3 buckets. This tool allows CrewAI agents to create or update files in S3, making it ideal for workflows that require storing data, saving configuration files, or persisting any other content to AWS S3 storage.


## Installation

To use this tool, you need to install the required dependencies:

```shell  theme={null}
uv add boto3
```


## Steps to Get Started

To effectively use the `S3WriterTool`, follow these steps:

1. **Install Dependencies**: Install the required packages using the command above.
2. **Configure AWS Credentials**: Set up your AWS credentials as environment variables.
3. **Initialize the Tool**: Create an instance of the tool.
4. **Specify S3 Path and Content**: Provide the S3 path where you want to write the file and the content to be written.


## Example

The following example demonstrates how to use the `S3WriterTool` to write content to a file in an S3 bucket:

```python Code theme={null}
from crewai import Agent, Task, Crew
from crewai_tools.aws.s3 import S3WriterTool


# Initialize the tool
s3_writer_tool = S3WriterTool()


# Define an agent that uses the tool
file_writer_agent = Agent(
    role="File Writer",
    goal="Write content to files in S3 buckets",
    backstory="An expert in storing and managing files in cloud storage.",
    tools=[s3_writer_tool],
    verbose=True,
)


# Example task to write a report
write_task = Task(
    description="Generate a summary report of the quarterly sales data and save it to {my_bucket}.",
    expected_output="Confirmation that the report was successfully saved to S3.",
    agent=file_writer_agent,
)


# Create and run the crew
crew = Crew(agents=[file_writer_agent], tasks=[write_task])
result = crew.kickoff(inputs={"my_bucket": "s3://my-bucket/reports/quarterly-summary.txt"})
```


## Parameters

The `S3WriterTool` accepts the following parameters when used by an agent:

* **file\_path**: Required. The S3 file path in the format `s3://bucket-name/file-name`.
* **content**: Required. The content to write to the file.


## AWS Credentials

The tool requires AWS credentials to access S3 buckets. You can configure these credentials using environment variables:

* **CREW\_AWS\_REGION**: The AWS region where your S3 bucket is located. Default is `us-east-1`.
* **CREW\_AWS\_ACCESS\_KEY\_ID**: Your AWS access key ID.
* **CREW\_AWS\_SEC\_ACCESS\_KEY**: Your AWS secret access key.


## Usage

When using the `S3WriterTool` with an agent, the agent will need to provide both the S3 file path and the content to write:

```python Code theme={null}

# Example of using the tool with an agent
file_writer_agent = Agent(
    role="File Writer",
    goal="Write content to files in S3 buckets",
    backstory="An expert in storing and managing files in cloud storage.",
    tools=[s3_writer_tool],
    verbose=True,
)


# Create a task for the agent to write a specific file
write_config_task = Task(
    description="""
    Create a configuration file with the following database settings:
    - host: db.example.com
    - port: 5432
    - username: app_user
    - password: secure_password
    
    Save this configuration as JSON to {my_bucket}.
    """,
    expected_output="Confirmation that the configuration file was successfully saved to S3.",
    agent=file_writer_agent,
)


# Run the task
crew = Crew(agents=[file_writer_agent], tasks=[write_config_task])
result = crew.kickoff(inputs={"my_bucket": "s3://my-bucket/config/db-config.json"})
```


## Error Handling

The `S3WriterTool` includes error handling for common S3 issues:

* Invalid S3 path format
* Permission issues (e.g., no write access to the bucket)
* AWS credential problems
* Bucket does not exist

When an error occurs, the tool will return an error message that includes details about the issue.


## Implementation Details

The `S3WriterTool` uses the AWS SDK for Python (boto3) to interact with S3:

```python Code theme={null}
class S3WriterTool(BaseTool):
    name: str = "S3 Writer Tool"
    description: str = "Writes content to a file in Amazon S3 given an S3 file path"
    
    def _run(self, file_path: str, content: str) -> str:
        try:
            bucket_name, object_key = self._parse_s3_path(file_path)

            s3 = boto3.client(
                's3',
                region_name=os.getenv('CREW_AWS_REGION', 'us-east-1'),
                aws_access_key_id=os.getenv('CREW_AWS_ACCESS_KEY_ID'),
                aws_secret_access_key=os.getenv('CREW_AWS_SEC_ACCESS_KEY')
            )

            s3.put_object(Bucket=bucket_name, Key=object_key, Body=content.encode('utf-8'))
            return f"Successfully wrote content to {file_path}"
        except ClientError as e:
            return f"Error writing file to S3: {str(e)}"
```


## Conclusion

The `S3WriterTool` provides a straightforward way to write content to files in Amazon S3 buckets. By enabling agents to create and update files in S3, it facilitates workflows that require cloud-based file storage. This tool is particularly useful for data persistence, configuration management, report generation, and any task that involves storing information in AWS S3 storage.



# MongoDB Vector Search Tool
Source: https://docs.crewai.com/en/tools/database-data/mongodbvectorsearchtool

The `MongoDBVectorSearchTool` performs vector search on MongoDB Atlas with optional indexing helpers.


# `MongoDBVectorSearchTool`


## Description

Perform vector similarity queries on MongoDB Atlas collections. Supports index creation helpers and bulk insert of embedded texts.

MongoDB Atlas supports native vector search. Learn more:
[https://www.mongodb.com/docs/atlas/atlas-vector-search/vector-search-overview/](https://www.mongodb.com/docs/atlas/atlas-vector-search/vector-search-overview/)


## Installation

Install with the MongoDB extra:

```shell  theme={null}
pip install crewai-tools[mongodb]
```

or

```shell  theme={null}
uv add crewai-tools --extra mongodb
```


## Parameters

### Initialization

* `connection_string` (str, required)
* `database_name` (str, required)
* `collection_name` (str, required)
* `vector_index_name` (str, default `vector_index`)
* `text_key` (str, default `text`)
* `embedding_key` (str, default `embedding`)
* `dimensions` (int, default `1536`)

### Run Parameters

* `query` (str, required): Natural language query to embed and search.


## Quick start

```python Code theme={null}
from crewai_tools import MongoDBVectorSearchTool

tool = MongoDBVectorSearchTool(
  connection_string="mongodb+srv://...",
  database_name="mydb",
  collection_name="docs",
)

print(tool.run(query="how to create vector index"))
```


## Index creation helpers

Use `create_vector_search_index(...)` to provision an Atlas Vector Search index with the correct dimensions and similarity.


## Common issues

* Authentication failures: ensure your Atlas IP Access List allows your runner and the connection string includes credentials.
* Index not found: create the vector index first; name must match `vector_index_name`.
* Dimensions mismatch: align embedding model dimensions with `dimensions`.


## More examples

### Basic initialization

```python Code theme={null}
from crewai_tools import MongoDBVectorSearchTool

tool = MongoDBVectorSearchTool(
    database_name="example_database",
    collection_name="example_collection",
    connection_string="<your_mongodb_connection_string>",
)
```

### Custom query configuration

```python Code theme={null}
from crewai_tools import MongoDBVectorSearchConfig, MongoDBVectorSearchTool

query_config = MongoDBVectorSearchConfig(limit=10, oversampling_factor=2)
tool = MongoDBVectorSearchTool(
    database_name="example_database",
    collection_name="example_collection",
    connection_string="<your_mongodb_connection_string>",
    query_config=query_config,
    vector_index_name="my_vector_index",
)

rag_agent = Agent(
    name="rag_agent",
    role="You are a helpful assistant that can answer questions with the help of the MongoDBVectorSearchTool.",
    goal="...",
    backstory="...",
    tools=[tool],
)
```

### Preloading the database and creating the index

```python Code theme={null}
import os
from crewai_tools import MongoDBVectorSearchTool

tool = MongoDBVectorSearchTool(
    database_name="example_database",
    collection_name="example_collection",
    connection_string="<your_mongodb_connection_string>",
)


# Load text content from a local folder and add to MongoDB
texts = []
for fname in os.listdir("knowledge"):
    path = os.path.join("knowledge", fname)
    if os.path.isfile(path):
        with open(path, "r", encoding="utf-8") as f:
            texts.append(f.read())

tool.add_texts(texts)


# Create the Atlas Vector Search index (e.g., 3072 dims for text-embedding-3-large)
tool.create_vector_search_index(dimensions=3072)
```


## Example

```python Code theme={null}
from crewai import Agent, Task, Crew
from crewai_tools import MongoDBVectorSearchTool

tool = MongoDBVectorSearchTool(
    connection_string="mongodb+srv://...",
    database_name="mydb",
    collection_name="docs",
)

agent = Agent(
    role="RAG Agent",
    goal="Answer using MongoDB vector search",
    backstory="Knowledge retrieval specialist",
    tools=[tool],
    verbose=True,
)

task = Task(
    description="Find relevant content for 'indexing guidance'",
    expected_output="A concise answer citing the most relevant matches",
    agent=agent,
)

crew = Crew(
    agents=[agent], 
    tasks=[task],
    verbose=True,
)

result = crew.kickoff()
```



# MySQL RAG Search
Source: https://docs.crewai.com/en/tools/database-data/mysqltool

The `MySQLSearchTool` is designed to search MySQL databases and return the most relevant results.


## Overview

This tool is designed to facilitate semantic searches within MySQL database tables. Leveraging the RAG (Retrieve and Generate) technology,
the MySQLSearchTool provides users with an efficient means of querying database table content, specifically tailored for MySQL databases.
It simplifies the process of finding relevant data through semantic search queries, making it an invaluable resource for users needing
to perform advanced queries on extensive datasets within a MySQL database.


## Installation

To install the `crewai_tools` package and utilize the MySQLSearchTool, execute the following command in your terminal:

```shell  theme={null}
pip install 'crewai[tools]'
```


## Example

Below is an example showcasing how to use the MySQLSearchTool to conduct a semantic search on a table within a MySQL database:

```python Code theme={null}
from crewai_tools import MySQLSearchTool


# Initialize the tool with the database URI and the target table name
tool = MySQLSearchTool(
    db_uri='mysql://user:password@localhost:3306/mydatabase',
    table_name='employees'
)
```


## Arguments

The MySQLSearchTool requires the following arguments for its operation:

* `db_uri`: A string representing the URI of the MySQL database to be queried. This argument is mandatory and must include the necessary authentication details and the location of the database.
* `table_name`: A string specifying the name of the table within the database on which the semantic search will be performed. This argument is mandatory.


## Custom model and embeddings

By default, the tool uses OpenAI for both embeddings and summarization. To customize the model, you can use a config dictionary as follows:

```python Code theme={null}
tool = MySQLSearchTool(
    config=dict(
        llm=dict(
            provider="ollama", # or google, openai, anthropic, llama2, ...
            config=dict(
                model="llama2",
                # temperature=0.5,
                # top_p=1,
                # stream=true,
            ),
        ),
        embedder=dict(
            provider="google",
            config=dict(
                model="models/embedding-001",
                task_type="retrieval_document",
                # title="Embeddings",
            ),
        ),
    )
)
```



# NL2SQL Tool
Source: https://docs.crewai.com/en/tools/database-data/nl2sqltool

The `NL2SQLTool` is designed to convert natural language to SQL queries.


## Overview

This tool is used to convert natural language to SQL queries. When passed to the agent it will generate queries and then use them to interact with the database.

This enables multiple workflows like having an Agent to access the database fetch information based on the goal and then use the information to generate a response, report or any other output.
Along with that provides the ability for the Agent to update the database based on its goal.

**Attention**: Make sure that the Agent has access to a Read-Replica or that is okay for the Agent to run insert/update queries on the database.


## Requirements

* SqlAlchemy
* Any DB compatible library (e.g. psycopg2, mysql-connector-python)


## Installation

Install the crewai\_tools package

```shell  theme={null}
pip install 'crewai[tools]'
```


## Usage

In order to use the NL2SQLTool, you need to pass the database URI to the tool. The URI should be in the format `dialect+driver://username:password@host:port/database`.

```python Code theme={null}
from crewai_tools import NL2SQLTool


# psycopg2 was installed to run this example with PostgreSQL
nl2sql = NL2SQLTool(db_uri="postgresql://example@localhost:5432/test_db")

@agent
def researcher(self) -> Agent:
    return Agent(
        config=self.agents_config["researcher"],
        allow_delegation=False,
        tools=[nl2sql]
    )
```


## Example

The primary task goal was:

"Retrieve the average, maximum, and minimum monthly revenue for each city, but only include cities that have more than one user. Also, count the number of user in each city and
sort the results by the average monthly revenue in descending order"

So the Agent tried to get information from the DB, the first one is wrong so the Agent tries again and gets the correct information and passes to the next agent.

![alt text](https://github.com/crewAIInc/crewAI-tools/blob/main/crewai_tools/tools/nl2sql/images/image-2.png?raw=true)
![alt text](https://github.com/crewAIInc/crewAI-tools/raw/main/crewai_tools/tools/nl2sql/images/image-3.png)

The second task goal was:

"Review the data and create a detailed report, and then create the table on the database with the fields based on the data provided.
Include information on the average, maximum, and minimum monthly revenue for each city, but only include cities that have more than one user. Also, count the number of users in each city and sort the results by the average monthly revenue in descending order."

Now things start to get interesting, the Agent generates the SQL query to not only create the table but also insert the data into the table. And in the end the Agent still returns the final report which is exactly what was in the database.

![alt text](https://github.com/crewAIInc/crewAI-tools/raw/main/crewai_tools/tools/nl2sql/images/image-4.png)
![alt text](https://github.com/crewAIInc/crewAI-tools/raw/main/crewai_tools/tools/nl2sql/images/image-5.png)

![alt text](https://github.com/crewAIInc/crewAI-tools/raw/main/crewai_tools/tools/nl2sql/images/image-9.png)
![alt text](https://github.com/crewAIInc/crewAI-tools/raw/main/crewai_tools/tools/nl2sql/images/image-7.png)

This is a simple example of how the NL2SQLTool can be used to interact with the database and generate reports based on the data in the database.

The Tool provides endless possibilities on the logic of the Agent and how it can interact with the database.

```md  theme={null}
 DB -> Agent -> ... -> Agent -> DB
```



# Overview
Source: https://docs.crewai.com/en/tools/database-data/overview

Connect to databases, vector stores, and data warehouses for comprehensive data access

These tools enable your agents to interact with various database systems, from traditional SQL databases to modern vector stores and data warehouses.


## **Available Tools**

<CardGroup cols={2}>
  <Card title="MySQL Tool" icon="database" href="/en/tools/database-data/mysqltool">
    Connect to and query MySQL databases with SQL operations.
  </Card>

  <Card title="PostgreSQL Search" icon="elephant" href="/en/tools/database-data/pgsearchtool">
    Search and query PostgreSQL databases efficiently.
  </Card>

  <Card title="Snowflake Search" icon="snowflake" href="/en/tools/database-data/snowflakesearchtool">
    Access Snowflake data warehouse for analytics and reporting.
  </Card>

  <Card title="NL2SQL Tool" icon="language" href="/en/tools/database-data/nl2sqltool">
    Convert natural language queries to SQL statements automatically.
  </Card>

  <Card title="Qdrant Vector Search" icon="vector-square" href="/en/tools/database-data/qdrantvectorsearchtool">
    Search vector embeddings using Qdrant vector database.
  </Card>

  <Card title="Weaviate Vector Search" icon="network-wired" href="/en/tools/database-data/weaviatevectorsearchtool">
    Perform semantic search with Weaviate vector database.
  </Card>

  <Card title="MongoDB Vector Search" icon="leaf" href="/en/tools/database-data/mongodbvectorsearchtool">
    Vector similarity search on MongoDB Atlas with indexing helpers.
  </Card>

  <Card title="SingleStore Search" icon="database" href="/en/tools/database-data/singlestoresearchtool">
    Safe SELECT/SHOW queries on SingleStore with pooling and validation.
  </Card>
</CardGroup>


## **Common Use Cases**

* **Data Analysis**: Query databases for business intelligence and reporting
* **Vector Search**: Find similar content using semantic embeddings
* **ETL Operations**: Extract, transform, and load data between systems
* **Real-time Analytics**: Access live data for decision making

```python  theme={null}
from crewai_tools import MySQLTool, QdrantVectorSearchTool, NL2SQLTool


# Create database tools
mysql_db = MySQLTool()
vector_search = QdrantVectorSearchTool()
nl_to_sql = NL2SQLTool()


# Add to your agent
agent = Agent(
    role="Data Analyst",
    tools=[mysql_db, vector_search, nl_to_sql],
    goal="Extract insights from various data sources"
)
```



# PG RAG Search
Source: https://docs.crewai.com/en/tools/database-data/pgsearchtool

The `PGSearchTool` is designed to search PostgreSQL databases and return the most relevant results.


## Overview

<Note>
  The PGSearchTool is currently under development. This document outlines the intended functionality and interface.
  As development progresses, please be aware that some features may not be available or could change.
</Note>


## Description

The PGSearchTool is envisioned as a powerful tool for facilitating semantic searches within PostgreSQL database tables. By leveraging advanced Retrieve and Generate (RAG) technology,
it aims to provide an efficient means for querying database table content, specifically tailored for PostgreSQL databases.
The tool's goal is to simplify the process of finding relevant data through semantic search queries, offering a valuable resource for users needing to conduct advanced queries on
extensive datasets within a PostgreSQL environment.


## Installation

The `crewai_tools` package, which will include the PGSearchTool upon its release, can be installed using the following command:

```shell  theme={null}
pip install 'crewai[tools]'
```

<Note>
  The PGSearchTool is not yet available in the current version of the `crewai_tools` package. This installation command will be updated once the tool is released.
</Note>


## Example Usage

Below is a proposed example showcasing how to use the PGSearchTool for conducting a semantic search on a table within a PostgreSQL database:

```python Code theme={null}
from crewai_tools import PGSearchTool


# Initialize the tool with the database URI and the target table name
tool = PGSearchTool(
    db_uri='postgresql://user:password@localhost:5432/mydatabase', 
    table_name='employees'
)
```


## Arguments

The PGSearchTool is designed to require the following arguments for its operation:

| Argument        | Type     | Description                                                                                                                                                                                                    |
| :-------------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **db\_uri**     | `string` | **Mandatory**. A string representing the URI of the PostgreSQL database to be queried. This argument will be mandatory and must include the necessary authentication details and the location of the database. |
| **table\_name** | `string` | **Mandatory**. A string specifying the name of the table within the database on which the semantic search will be performed. This argument will also be mandatory.                                             |


## Custom Model and Embeddings

The tool intends to use OpenAI for both embeddings and summarization by default. Users will have the option to customize the model using a config dictionary as follows:

```python Code theme={null}
tool = PGSearchTool(
    config=dict(
        llm=dict(
            provider="ollama", # or google, openai, anthropic, llama2, ...
            config=dict(
                model="llama2",
                # temperature=0.5,
                # top_p=1,
                # stream=true,
            ),
        ),
        embedder=dict(
            provider="google", # or openai, ollama, ...
            config=dict(
                model="models/embedding-001",
                task_type="retrieval_document",
                # title="Embeddings",
            ),
        ),
    )
)
```



# Qdrant Vector Search Tool
Source: https://docs.crewai.com/en/tools/database-data/qdrantvectorsearchtool

Semantic search capabilities for CrewAI agents using Qdrant vector database


## Overview

The Qdrant Vector Search Tool enables semantic search capabilities in your CrewAI agents by leveraging [Qdrant](https://qdrant.tech/), a vector similarity search engine. This tool allows your agents to search through documents stored in a Qdrant collection using semantic similarity.


## Installation

Install the required packages:

```bash  theme={null}
uv add qdrant-client
```


## Basic Usage

Here's a minimal example of how to use the tool:

```python  theme={null}
from crewai import Agent
from crewai_tools import QdrantVectorSearchTool, QdrantConfig


# Initialize the tool with QdrantConfig
qdrant_tool = QdrantVectorSearchTool(
    qdrant_config=QdrantConfig(
        qdrant_url="your_qdrant_url",
        qdrant_api_key="your_qdrant_api_key",
        collection_name="your_collection"
    )
)


# Create an agent that uses the tool
agent = Agent(
    role="Research Assistant",
    goal="Find relevant information in documents",
    tools=[qdrant_tool]
)


# The tool will automatically use OpenAI embeddings

# and return the 3 most relevant results with scores > 0.35
```


## Complete Working Example

Here's a complete example showing how to:

1. Extract text from a PDF
2. Generate embeddings using OpenAI
3. Store in Qdrant
4. Create a CrewAI agentic RAG workflow for semantic search

```python  theme={null}
import os
import uuid
import pdfplumber
from openai import OpenAI
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process, LLM
from crewai_tools import QdrantVectorSearchTool
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct, Distance, VectorParams


# Load environment variables
load_dotenv()


# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# Extract text from PDF
def extract_text_from_pdf(pdf_path):
    text = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text.append(page_text.strip())
    return text


# Generate OpenAI embeddings
def get_openai_embedding(text):
    response = client.embeddings.create(
        input=text,
        model="text-embedding-3-large"
    )
    return response.data[0].embedding


# Store text and embeddings in Qdrant
def load_pdf_to_qdrant(pdf_path, qdrant, collection_name):
    # Extract text from PDF
    text_chunks = extract_text_from_pdf(pdf_path)

    # Create Qdrant collection
    if qdrant.collection_exists(collection_name):
        qdrant.delete_collection(collection_name)
    qdrant.create_collection(
        collection_name=collection_name,
        vectors_config=VectorParams(size=3072, distance=Distance.COSINE)
    )

    # Store embeddings
    points = []
    for chunk in text_chunks:
        embedding = get_openai_embedding(chunk)
        points.append(PointStruct(
            id=str(uuid.uuid4()),
            vector=embedding,
            payload={"text": chunk}
        ))
    qdrant.upsert(collection_name=collection_name, points=points)


# Initialize Qdrant client and load data
qdrant = QdrantClient(
    url=os.getenv("QDRANT_URL"),
    api_key=os.getenv("QDRANT_API_KEY")
)
collection_name = "example_collection"
pdf_path = "path/to/your/document.pdf"
load_pdf_to_qdrant(pdf_path, qdrant, collection_name)


# Initialize Qdrant search tool
from crewai_tools import QdrantConfig

qdrant_tool = QdrantVectorSearchTool(
    qdrant_config=QdrantConfig(
        qdrant_url=os.getenv("QDRANT_URL"),
        qdrant_api_key=os.getenv("QDRANT_API_KEY"),
        collection_name=collection_name,
        limit=3,
        score_threshold=0.35
    )
)


# Create CrewAI agents
search_agent = Agent(
    role="Senior Semantic Search Agent",
    goal="Find and analyze documents based on semantic search",
    backstory="""You are an expert research assistant who can find relevant
    information using semantic search in a Qdrant database.""",
    tools=[qdrant_tool],
    verbose=True
)

answer_agent = Agent(
    role="Senior Answer Assistant",
    goal="Generate answers to questions based on the context provided",
    backstory="""You are an expert answer assistant who can generate
    answers to questions based on the context provided.""",
    tools=[qdrant_tool],
    verbose=True
)


# Define tasks
search_task = Task(
    description="""Search for relevant documents about the {query}.
    Your final answer should include:
    - The relevant information found
    - The similarity scores of the results
    - The metadata of the relevant documents""",
    agent=search_agent
)

answer_task = Task(
    description="""Given the context and metadata of relevant documents,
    generate a final answer based on the context.""",
    agent=answer_agent
)


# Run CrewAI workflow
crew = Crew(
    agents=[search_agent, answer_agent],
    tasks=[search_task, answer_task],
    process=Process.sequential,
    verbose=True
)

result = crew.kickoff(
    inputs={"query": "What is the role of X in the document?"}
)
print(result)
```


## Tool Parameters

### Required Parameters

* `qdrant_config` (QdrantConfig): Configuration object containing all Qdrant settings

### QdrantConfig Parameters

* `qdrant_url` (str): The URL of your Qdrant server
* `qdrant_api_key` (str, optional): API key for authentication with Qdrant
* `collection_name` (str): Name of the Qdrant collection to search
* `limit` (int): Maximum number of results to return (default: 3)
* `score_threshold` (float): Minimum similarity score threshold (default: 0.35)
* `filter` (Any, optional): Qdrant Filter instance for advanced filtering (default: None)

### Optional Tool Parameters

* `custom_embedding_fn` (Callable\[\[str], list\[float]]): Custom function for text vectorization
* `qdrant_package` (str): Base package path for Qdrant (default: "qdrant\_client")
* `client` (Any): Pre-initialized Qdrant client (optional)


## Advanced Filtering

The QdrantVectorSearchTool supports powerful filtering capabilities to refine your search results:

### Dynamic Filtering

Use `filter_by` and `filter_value` parameters in your search to filter results on-the-fly:

```python  theme={null}

# Agent will use these parameters when calling the tool

# The tool schema accepts filter_by and filter_value

# Example: search with category filter

# Results will be filtered where category == "technology"
```

### Preset Filters with QdrantConfig

For complex filtering, use Qdrant Filter instances in your configuration:

```python  theme={null}
from qdrant_client.http import models as qmodels
from crewai_tools import QdrantVectorSearchTool, QdrantConfig


# Create a filter for specific conditions
preset_filter = qmodels.Filter(
    must=[
        qmodels.FieldCondition(
            key="category",
            match=qmodels.MatchValue(value="research")
        ),
        qmodels.FieldCondition(
            key="year",
            match=qmodels.MatchValue(value=2024)
        )
    ]
)


# Initialize tool with preset filter
qdrant_tool = QdrantVectorSearchTool(
    qdrant_config=QdrantConfig(
        qdrant_url="your_url",
        qdrant_api_key="your_key",
        collection_name="your_collection",
        filter=preset_filter  # Preset filter applied to all searches
    )
)
```

### Combining Filters

The tool automatically combines preset filters from `QdrantConfig` with dynamic filters from `filter_by` and `filter_value`:

```python  theme={null}

# If QdrantConfig has a preset filter for category="research"

# And the search uses filter_by="year", filter_value=2024

# Both filters will be combined (AND logic)
```


## Search Parameters

The tool accepts these parameters in its schema:

* `query` (str): The search query to find similar documents
* `filter_by` (str, optional): Metadata field to filter on
* `filter_value` (Any, optional): Value to filter by


## Return Format

The tool returns results in JSON format:

```json  theme={null}
[
  {
    "metadata": {
      // Any metadata stored with the document
    },
    "context": "The actual text content of the document",
    "distance": 0.95  // Similarity score
  }
]
```


## Default Embedding

By default, the tool uses OpenAI's `text-embedding-3-large` model for vectorization. This requires:

* OpenAI API key set in environment: `OPENAI_API_KEY`


## Custom Embeddings

Instead of using the default embedding model, you might want to use your own embedding function in cases where you:

1. Want to use a different embedding model (e.g., Cohere, HuggingFace, Ollama models)
2. Need to reduce costs by using open-source embedding models
3. Have specific requirements for vector dimensions or embedding quality
4. Want to use domain-specific embeddings (e.g., for medical or legal text)

Here's an example using a HuggingFace model:

```python  theme={null}
from transformers import AutoTokenizer, AutoModel
import torch


# Load model and tokenizer
tokenizer = AutoTokenizer.from_pretrained('sentence-transformers/all-MiniLM-L6-v2')
model = AutoModel.from_pretrained('sentence-transformers/all-MiniLM-L6-v2')

def custom_embeddings(text: str) -> list[float]:
    # Tokenize and get model outputs
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    outputs = model(**inputs)

    # Use mean pooling to get text embedding
    embeddings = outputs.last_hidden_state.mean(dim=1)

    # Convert to list of floats and return
    return embeddings[0].tolist()


# Use custom embeddings with the tool
from crewai_tools import QdrantConfig

tool = QdrantVectorSearchTool(
    qdrant_config=QdrantConfig(
        qdrant_url="your_url",
        qdrant_api_key="your_key",
        collection_name="your_collection"
    ),
    custom_embedding_fn=custom_embeddings  # Pass your custom function
)
```


## Error Handling

The tool handles these specific errors:

* Raises ImportError if `qdrant-client` is not installed (with option to auto-install)
* Raises ValueError if `QDRANT_URL` is not set
* Prompts to install `qdrant-client` if missing using `uv add qdrant-client`


## Environment Variables

Required environment variables:

```bash  theme={null}
export QDRANT_URL="your_qdrant_url"  # If not provided in constructor
export QDRANT_API_KEY="your_api_key"  # If not provided in constructor
export OPENAI_API_KEY="your_openai_key"  # If using default embeddings
```



# SingleStore Search Tool
Source: https://docs.crewai.com/en/tools/database-data/singlestoresearchtool

The `SingleStoreSearchTool` safely executes SELECT/SHOW queries on SingleStore with pooling.


# `SingleStoreSearchTool`


## Description

Execute read‑only queries (`SELECT`/`SHOW`) against SingleStore with connection pooling and input validation.


## Installation

```shell  theme={null}
uv add crewai-tools[singlestore]
```


## Environment Variables

Variables like `SINGLESTOREDB_HOST`, `SINGLESTOREDB_USER`, `SINGLESTOREDB_PASSWORD`, etc., can be used, or `SINGLESTOREDB_URL` as a single DSN.

Generate the API key from the SingleStore dashboard, [docs here](https://docs.singlestore.com/cloud/reference/management-api/#generate-an-api-key).


## Example

```python Code theme={null}
from crewai import Agent, Task, Crew
from crewai_tools import SingleStoreSearchTool

tool = SingleStoreSearchTool(
    tables=["products"], 
    host="host", 
    user="user", 
    password="pass", 
    database="db",
)

agent = Agent(
    role="Analyst", 
    goal="Query SingleStore", 
    tools=[tool], 
    verbose=True,
)

task = Task(
    description="List 5 products", 
    expected_output="5 rows as JSON/text", 
    agent=agent,
)

crew = Crew(
    agents=[agent], 
    tasks=[task],
    verbose=True,
)

result = crew.kickoff()
```



# Snowflake Search Tool
Source: https://docs.crewai.com/en/tools/database-data/snowflakesearchtool

The `SnowflakeSearchTool` enables CrewAI agents to execute SQL queries and perform semantic search on Snowflake data warehouses.


# `SnowflakeSearchTool`


## Description

The `SnowflakeSearchTool` is designed to connect to Snowflake data warehouses and execute SQL queries with advanced features like connection pooling, retry logic, and asynchronous execution. This tool allows CrewAI agents to interact with Snowflake databases, making it ideal for data analysis, reporting, and business intelligence tasks that require access to enterprise data stored in Snowflake.


## Installation

To use this tool, you need to install the required dependencies:

```shell  theme={null}
uv add cryptography snowflake-connector-python snowflake-sqlalchemy
```

Or alternatively:

```shell  theme={null}
uv sync --extra snowflake
```


## Steps to Get Started

To effectively use the `SnowflakeSearchTool`, follow these steps:

1. **Install Dependencies**: Install the required packages using one of the commands above.
2. **Configure Snowflake Connection**: Create a `SnowflakeConfig` object with your Snowflake credentials.
3. **Initialize the Tool**: Create an instance of the tool with the necessary configuration.
4. **Execute Queries**: Use the tool to run SQL queries against your Snowflake database.


## Example

The following example demonstrates how to use the `SnowflakeSearchTool` to query data from a Snowflake database:

```python Code theme={null}
from crewai import Agent, Task, Crew
from crewai_tools import SnowflakeSearchTool, SnowflakeConfig


# Create Snowflake configuration
config = SnowflakeConfig(
    account="your_account",
    user="your_username",
    password="your_password",
    warehouse="COMPUTE_WH",
    database="your_database",
    snowflake_schema="your_schema"
)


# Initialize the tool
snowflake_tool = SnowflakeSearchTool(config=config)


# Define an agent that uses the tool
data_analyst_agent = Agent(
    role="Data Analyst",
    goal="Analyze data from Snowflake database",
    backstory="An expert data analyst who can extract insights from enterprise data.",
    tools=[snowflake_tool],
    verbose=True,
)


# Example task to query sales data
query_task = Task(
    description="Query the sales data for the last quarter and summarize the top 5 products by revenue.",
    expected_output="A summary of the top 5 products by revenue for the last quarter.",
    agent=data_analyst_agent,
)


# Create and run the crew
crew = Crew(agents=[data_analyst_agent], 
            tasks=[query_task])
result = crew.kickoff()
```

You can also customize the tool with additional parameters:

```python Code theme={null}

# Initialize the tool with custom parameters
snowflake_tool = SnowflakeSearchTool(
    config=config,
    pool_size=10,
    max_retries=5,
    retry_delay=2.0,
    enable_caching=True
)
```


## Parameters

### SnowflakeConfig Parameters

The `SnowflakeConfig` class accepts the following parameters:

* **account**: Required. Snowflake account identifier.
* **user**: Required. Snowflake username.
* **password**: Optional\*. Snowflake password.
* **private\_key\_path**: Optional\*. Path to private key file (alternative to password).
* **warehouse**: Required. Snowflake warehouse name.
* **database**: Required. Default database.
* **snowflake\_schema**: Required. Default schema.
* **role**: Optional. Snowflake role.
* **session\_parameters**: Optional. Custom session parameters as a dictionary.

\*Either `password` or `private_key_path` must be provided.

### SnowflakeSearchTool Parameters

The `SnowflakeSearchTool` accepts the following parameters during initialization:

* **config**: Required. A `SnowflakeConfig` object containing connection details.
* **pool\_size**: Optional. Number of connections in the pool. Default is 5.
* **max\_retries**: Optional. Maximum retry attempts for failed queries. Default is 3.
* **retry\_delay**: Optional. Delay between retries in seconds. Default is 1.0.
* **enable\_caching**: Optional. Whether to enable query result caching. Default is True.


## Usage

When using the `SnowflakeSearchTool`, you need to provide the following parameters:

* **query**: Required. The SQL query to execute.
* **database**: Optional. Override the default database specified in the config.
* **snowflake\_schema**: Optional. Override the default schema specified in the config.
* **timeout**: Optional. Query timeout in seconds. Default is 300.

The tool will return the query results as a list of dictionaries, where each dictionary represents a row with column names as keys.

```python Code theme={null}

# Example of using the tool with an agent
data_analyst = Agent(
    role="Data Analyst",
    goal="Analyze sales data from Snowflake",
    backstory="An expert data analyst with experience in SQL and data visualization.",
    tools=[snowflake_tool],
    verbose=True
)


# The agent will use the tool with parameters like:

# query="SELECT product_name, SUM(revenue) as total_revenue FROM sales GROUP BY product_name ORDER BY total_revenue DESC LIMIT 5"

# timeout=600


# Create a task for the agent
analysis_task = Task(
    description="Query the sales database and identify the top 5 products by revenue for the last quarter.",
    expected_output="A detailed analysis of the top 5 products by revenue.",
    agent=data_analyst
)


# Run the task
crew = Crew(
    agents=[data_analyst], 
    tasks=[analysis_task]
)
result = crew.kickoff()
```


## Advanced Features

### Connection Pooling

The `SnowflakeSearchTool` implements connection pooling to improve performance by reusing database connections. You can control the pool size with the `pool_size` parameter.

### Automatic Retries

The tool automatically retries failed queries with exponential backoff. You can configure the retry behavior with the `max_retries` and `retry_delay` parameters.

### Query Result Caching

To improve performance for repeated queries, the tool can cache query results. This feature is enabled by default but can be disabled by setting `enable_caching=False`.

### Key-Pair Authentication

In addition to password authentication, the tool supports key-pair authentication for enhanced security:

```python Code theme={null}
config = SnowflakeConfig(
    account="your_account",
    user="your_username",
    private_key_path="/path/to/your/private/key.p8",
    warehouse="COMPUTE_WH",
    database="your_database",
    snowflake_schema="your_schema"
)
```


## Error Handling

The `SnowflakeSearchTool` includes comprehensive error handling for common Snowflake issues:

* Connection failures
* Query timeouts
* Authentication errors
* Database and schema errors

When an error occurs, the tool will attempt to retry the operation (if configured) and provide detailed error information.


## Conclusion

The `SnowflakeSearchTool` provides a powerful way to integrate Snowflake data warehouses with CrewAI agents. With features like connection pooling, automatic retries, and query caching, it enables efficient and reliable access to enterprise data. This tool is particularly useful for data analysis, reporting, and business intelligence tasks that require access to structured data stored in Snowflake.



# Weaviate Vector Search
Source: https://docs.crewai.com/en/tools/database-data/weaviatevectorsearchtool

The `WeaviateVectorSearchTool` is designed to search a Weaviate vector database for semantically similar documents using hybrid search.


## Overview

The `WeaviateVectorSearchTool` is specifically crafted for conducting semantic searches within documents stored in a Weaviate vector database. This tool allows you to find semantically similar documents to a given query, leveraging the power of vector and keyword search for more accurate and contextually relevant search results.

[Weaviate](https://weaviate.io/) is a vector database that stores and queries vector embeddings, enabling semantic search capabilities.


## Installation

To incorporate this tool into your project, you need to install the Weaviate client:

```shell  theme={null}
uv add weaviate-client
```


## Steps to Get Started

To effectively use the `WeaviateVectorSearchTool`, follow these steps:

1. **Package Installation**: Confirm that the `crewai[tools]` and `weaviate-client` packages are installed in your Python environment.
2. **Weaviate Setup**: Set up a Weaviate cluster. You can follow the [Weaviate documentation](https://weaviate.io/developers/wcs/manage-clusters/connect) for instructions.
3. **API Keys**: Obtain your Weaviate cluster URL and API key.
4. **OpenAI API Key**: Ensure you have an OpenAI API key set in your environment variables as `OPENAI_API_KEY`.


## Example

The following example demonstrates how to initialize the tool and execute a search:

```python Code theme={null}
from crewai_tools import WeaviateVectorSearchTool


# Initialize the tool
tool = WeaviateVectorSearchTool(
    collection_name='example_collections',
    limit=3,
    alpha=0.75,
    weaviate_cluster_url="https://your-weaviate-cluster-url.com",
    weaviate_api_key="your-weaviate-api-key",
)

@agent
def search_agent(self) -> Agent:
    '''
    This agent uses the WeaviateVectorSearchTool to search for 
    semantically similar documents in a Weaviate vector database.
    '''
    return Agent(
        config=self.agents_config["search_agent"],
        tools=[tool]
    )
```


## Parameters

The `WeaviateVectorSearchTool` accepts the following parameters:

* **collection\_name**: Required. The name of the collection to search within.
* **weaviate\_cluster\_url**: Required. The URL of the Weaviate cluster.
* **weaviate\_api\_key**: Required. The API key for the Weaviate cluster.
* **limit**: Optional. The number of results to return. Default is `3`.
* **alpha**: Optional. Controls the weighting between vector and keyword (BM25) search. alpha = 0 -> BM25 only, alpha = 1 -> vector search only. Default is `0.75`.
* **vectorizer**: Optional. The vectorizer to use. If not provided, it will use `text2vec_openai` with the `nomic-embed-text` model.
* **generative\_model**: Optional. The generative model to use. If not provided, it will use OpenAI's `gpt-4o`.


## Advanced Configuration

You can customize the vectorizer and generative model used by the tool:

```python Code theme={null}
from crewai_tools import WeaviateVectorSearchTool
from weaviate.classes.config import Configure


# Setup custom model for vectorizer and generative model
tool = WeaviateVectorSearchTool(
    collection_name='example_collections',
    limit=3,
    alpha=0.75,
    vectorizer=Configure.Vectorizer.text2vec_openai(model="nomic-embed-text"),
    generative_model=Configure.Generative.openai(model="gpt-4o-mini"),
    weaviate_cluster_url="https://your-weaviate-cluster-url.com",
    weaviate_api_key="your-weaviate-api-key",
)
```


## Preloading Documents

You can preload your Weaviate database with documents before using the tool:

```python Code theme={null}
import os
from crewai_tools import WeaviateVectorSearchTool
import weaviate
from weaviate.classes.init import Auth


# Connect to Weaviate
client = weaviate.connect_to_weaviate_cloud(
    cluster_url="https://your-weaviate-cluster-url.com",
    auth_credentials=Auth.api_key("your-weaviate-api-key"),
    headers={"X-OpenAI-Api-Key": "your-openai-api-key"}
)


# Get or create collection
test_docs = client.collections.get("example_collections")
if not test_docs:
    test_docs = client.collections.create(
        name="example_collections",
        vectorizer_config=Configure.Vectorizer.text2vec_openai(model="nomic-embed-text"),
        generative_config=Configure.Generative.openai(model="gpt-4o"),
    )


# Load documents
docs_to_load = os.listdir("knowledge")
with test_docs.batch.dynamic() as batch:
    for d in docs_to_load:
        with open(os.path.join("knowledge", d), "r") as f:
            content = f.read()
        batch.add_object(
            {
                "content": content,
                "year": d.split("_")[0],
            }
        )


# Initialize the tool
tool = WeaviateVectorSearchTool(
    collection_name='example_collections', 
    limit=3,
    alpha=0.75,
    weaviate_cluster_url="https://your-weaviate-cluster-url.com",
    weaviate_api_key="your-weaviate-api-key",
)
```


## Agent Integration Example

Here's how to integrate the `WeaviateVectorSearchTool` with a CrewAI agent:

```python Code theme={null}
from crewai import Agent
from crewai_tools import WeaviateVectorSearchTool


# Initialize the tool
weaviate_tool = WeaviateVectorSearchTool(
    collection_name='example_collections',
    limit=3,
    alpha=0.75,
    weaviate_cluster_url="https://your-weaviate-cluster-url.com",
    weaviate_api_key="your-weaviate-api-key",
)


# Create an agent with the tool
rag_agent = Agent(
    name="rag_agent",
    role="You are a helpful assistant that can answer questions with the help of the WeaviateVectorSearchTool.",
    llm="gpt-4o-mini",
    tools=[weaviate_tool],
)
```


## Conclusion

The `WeaviateVectorSearchTool` provides a powerful way to search for semantically similar documents in a Weaviate vector database. By leveraging vector embeddings, it enables more accurate and contextually relevant search results compared to traditional keyword-based searches. This tool is particularly useful for applications that require finding information based on meaning rather than exact matches.



# CSV RAG Search
Source: https://docs.crewai.com/en/tools/file-document/csvsearchtool

The `CSVSearchTool` is a powerful RAG (Retrieval-Augmented Generation) tool designed for semantic searches within a CSV file's content.


# `CSVSearchTool`

<Note>
  **Experimental**: We are still working on improving tools, so there might be unexpected behavior or changes in the future.
</Note>


## Description

This tool is used to perform a RAG (Retrieval-Augmented Generation) search within a CSV file's content. It allows users to semantically search for queries in the content of a specified CSV file.
This feature is particularly useful for extracting information from large CSV datasets where traditional search methods might be inefficient. All tools with "Search" in their name, including CSVSearchTool,
are RAG tools designed for searching different sources of data.


## Installation

Install the crewai\_tools package

```shell  theme={null}
pip install 'crewai[tools]'
```


## Example

```python Code theme={null}
from crewai_tools import CSVSearchTool


# Initialize the tool with a specific CSV file. 

# This setup allows the agent to only search the given CSV file.
tool = CSVSearchTool(csv='path/to/your/csvfile.csv')


# OR


# Initialize the tool without a specific CSV file. 

# Agent will need to provide the CSV path at runtime.
tool = CSVSearchTool()
```


## Arguments

The following parameters can be used to customize the `CSVSearchTool`'s behavior:

| Argument | Type     | Description                                                                                                                                                               |
| :------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **csv**  | `string` | *Optional*. The path to the CSV file you want to search. This is a mandatory argument if the tool was initialized without a specific CSV file; otherwise, it is optional. |


## Custom model and embeddings

By default, the tool uses OpenAI for both embeddings and summarization. To customize the model, you can use a config dictionary as follows:

```python Code theme={null}
from chromadb.config import Settings

tool = CSVSearchTool(
    config={
        "embedding_model": {
            "provider": "openai",
            "config": {
                "model": "text-embedding-3-small",
                # "api_key": "sk-...",
            },
        },
        "vectordb": {
            "provider": "chromadb",  # or "qdrant"
            "config": {
                # "settings": Settings(persist_directory="/content/chroma", allow_reset=True, is_persistent=True),
                # from qdrant_client.models import VectorParams, Distance
                # "vectors_config": VectorParams(size=384, distance=Distance.COSINE),
            }
        },
    }
)
```



# Directory Read
Source: https://docs.crewai.com/en/tools/file-document/directoryreadtool

The `DirectoryReadTool` is a powerful utility designed to provide a comprehensive listing of directory contents.


# `DirectoryReadTool`

<Note>
  We are still working on improving tools, so there might be unexpected behavior or changes in the future.
</Note>


## Description

The DirectoryReadTool is a powerful utility designed to provide a comprehensive listing of directory contents.
It can recursively navigate through the specified directory, offering users a detailed enumeration of all files, including those within subdirectories.
This tool is crucial for tasks that require a thorough inventory of directory structures or for validating the organization of files within directories.


## Installation

To utilize the DirectoryReadTool in your project, install the `crewai_tools` package. If this package is not yet part of your environment, you can install it using pip with the command below:

```shell  theme={null}
pip install 'crewai[tools]'
```

This command installs the latest version of the `crewai_tools` package, granting access to the DirectoryReadTool among other utilities.


## Example

Employing the DirectoryReadTool is straightforward. The following code snippet demonstrates how to set it up and use the tool to list the contents of a specified directory:

```python Code theme={null}
from crewai_tools import DirectoryReadTool


# Initialize the tool so the agent can read any directory's content 

# it learns about during execution
tool = DirectoryReadTool()


# OR


# Initialize the tool with a specific directory, 

# so the agent can only read the content of the specified directory
tool = DirectoryReadTool(directory='/path/to/your/directory')
```


## Arguments

The following parameters can be used to customize the `DirectoryReadTool`'s behavior:

| Argument      | Type     | Description                                                                                                                                                                                                   |
| :------------ | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **directory** | `string` | *Optional*. An argument that specifies the path to the directory whose contents you wish to list. It accepts both absolute and relative paths, guiding the tool to the desired directory for content listing. |



# Directory RAG Search
Source: https://docs.crewai.com/en/tools/file-document/directorysearchtool

The `DirectorySearchTool` is a powerful RAG (Retrieval-Augmented Generation) tool designed for semantic searches within a directory's content.


# `DirectorySearchTool`

<Note>
  **Experimental**: The DirectorySearchTool is under continuous development. Features and functionalities might evolve, and unexpected behavior may occur as we refine the tool.
</Note>


## Description

The DirectorySearchTool enables semantic search within the content of specified directories, leveraging the Retrieval-Augmented Generation (RAG) methodology for efficient navigation through files. Designed for flexibility, it allows users to dynamically specify search directories at runtime or set a fixed directory during initial setup.


## Installation

To use the DirectorySearchTool, begin by installing the crewai\_tools package. Execute the following command in your terminal:

```shell  theme={null}
pip install 'crewai[tools]'
```


## Initialization and Usage

Import the DirectorySearchTool from the `crewai_tools` package to start. You can initialize the tool without specifying a directory, enabling the setting of the search directory at runtime. Alternatively, the tool can be initialized with a predefined directory.

```python Code theme={null}
from crewai_tools import DirectorySearchTool


# For dynamic directory specification at runtime
tool = DirectorySearchTool()


# For fixed directory searches
tool = DirectorySearchTool(directory='/path/to/directory')
```


## Arguments

* `directory`: A string argument that specifies the search directory. This is optional during initialization but required for searches if not set initially.


## Custom Model and Embeddings

The DirectorySearchTool uses OpenAI for embeddings and summarization by default. Customization options for these settings include changing the model provider and configuration, enhancing flexibility for advanced users.

```python Code theme={null}
from chromadb.config import Settings

tool = DirectorySearchTool(
    config={
        "embedding_model": {
            "provider": "openai",
            "config": {
                "model": "text-embedding-3-small",
                # "api_key": "sk-...",
            },
        },
        "vectordb": {
            "provider": "chromadb",  # or "qdrant"
            "config": {
                # "settings": Settings(persist_directory="/content/chroma", allow_reset=True, is_persistent=True),
                # from qdrant_client.models import VectorParams, Distance
                # "vectors_config": VectorParams(size=384, distance=Distance.COSINE),
            }
        },
    }
)
```



# DOCX RAG Search
Source: https://docs.crewai.com/en/tools/file-document/docxsearchtool

The `DOCXSearchTool` is a RAG tool designed for semantic searching within DOCX documents.


# `DOCXSearchTool`

<Note>
  We are still working on improving tools, so there might be unexpected behavior or changes in the future.
</Note>


## Description

The `DOCXSearchTool` is a RAG tool designed for semantic searching within DOCX documents.
It enables users to effectively search and extract relevant information from DOCX files using query-based searches.
This tool is invaluable for data analysis, information management, and research tasks,
streamlining the process of finding specific information within large document collections.


## Installation

Install the crewai\_tools package by running the following command in your terminal:

```shell  theme={null}
uv pip install docx2txt 'crewai[tools]'
```


## Example

The following example demonstrates initializing the DOCXSearchTool to search within any DOCX file's content or with a specific DOCX file path.

```python Code theme={null}
from crewai_tools import DOCXSearchTool


# Initialize the tool to search within any DOCX file's content
tool = DOCXSearchTool()


# OR


# Initialize the tool with a specific DOCX file, 

# so the agent can only search the content of the specified DOCX file
tool = DOCXSearchTool(docx='path/to/your/document.docx')
```


## Arguments

The following parameters can be used to customize the `DOCXSearchTool`'s behavior:

| Argument | Type     | Description                                                                                                                                                                                                        |
| :------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **docx** | `string` | *Optional*. An argument that specifies the path to the DOCX file you want to search. If not provided during initialization, the tool allows for later specification of any DOCX file's content path for searching. |


## Custom model and embeddings

By default, the tool uses OpenAI for both embeddings and summarization. To customize the model, you can use a config dictionary as follows:

```python Code theme={null}
from chromadb.config import Settings

tool = DOCXSearchTool(
    config={
        "embedding_model": {
            "provider": "openai",
            "config": {
                "model": "text-embedding-3-small",
                # "api_key": "sk-...",
            },
        },
        "vectordb": {
            "provider": "chromadb",  # or "qdrant"
            "config": {
                # "settings": Settings(persist_directory="/content/chroma", allow_reset=True, is_persistent=True),
                # from qdrant_client.models import VectorParams, Distance
                # "vectors_config": VectorParams(size=384, distance=Distance.COSINE),
            }
        },
    }
)
```



# File Read
Source: https://docs.crewai.com/en/tools/file-document/filereadtool

The `FileReadTool` is designed to read files from the local file system.


## Overview

<Note>
  We are still working on improving tools, so there might be unexpected behavior or changes in the future.
</Note>

The FileReadTool conceptually represents a suite of functionalities within the crewai\_tools package aimed at facilitating file reading and content retrieval.
This suite includes tools for processing batch text files, reading runtime configuration files, and importing data for analytics.
It supports a variety of text-based file formats such as `.txt`, `.csv`, `.json`, and more. Depending on the file type, the suite offers specialized functionality,
such as converting JSON content into a Python dictionary for ease of use.


## Installation

To utilize the functionalities previously attributed to the FileReadTool, install the crewai\_tools package:

```shell  theme={null}
pip install 'crewai[tools]'
```


## Usage Example

To get started with the FileReadTool:

```python Code theme={null}
from crewai_tools import FileReadTool


# Initialize the tool to read any files the agents knows or lean the path for
file_read_tool = FileReadTool()


# OR


# Initialize the tool with a specific file path, so the agent can only read the content of the specified file
file_read_tool = FileReadTool(file_path='path/to/your/file.txt')
```


## Arguments

* `file_path`: The path to the file you want to read. It accepts both absolute and relative paths. Ensure the file exists and you have the necessary permissions to access it.



# File Write
Source: https://docs.crewai.com/en/tools/file-document/filewritetool

The `FileWriterTool` is designed to write content to files.


# `FileWriterTool`


## Description

The `FileWriterTool` is a component of the crewai\_tools package, designed to simplify the process of writing content to files with cross-platform compatibility (Windows, Linux, macOS).
It is particularly useful in scenarios such as generating reports, saving logs, creating configuration files, and more.
This tool handles path differences across operating systems, supports UTF-8 encoding, and automatically creates directories if they don't exist, making it easier to organize your output reliably across different platforms.


## Installation

Install the crewai\_tools package to use the `FileWriterTool` in your projects:

```shell  theme={null}
pip install 'crewai[tools]'
```


## Example

To get started with the `FileWriterTool`:

```python Code theme={null}
from crewai_tools import FileWriterTool


# Initialize the tool
file_writer_tool = FileWriterTool()


# Write content to a file in a specified directory
result = file_writer_tool._run('example.txt', 'This is a test content.', 'test_directory')
print(result)
```


## Arguments

* `filename`: The name of the file you want to create or overwrite.
* `content`: The content to write into the file.
* `directory` (optional): The path to the directory where the file will be created. Defaults to the current directory (`.`). If the directory does not exist, it will be created.


## Conclusion

By integrating the `FileWriterTool` into your crews, the agents can reliably write content to files across different operating systems.
This tool is essential for tasks that require saving output data, creating structured file systems, and handling cross-platform file operations.
It's particularly recommended for Windows users who may encounter file writing issues with standard Python file operations.

By adhering to the setup and usage guidelines provided, incorporating this tool into projects is straightforward and ensures consistent file writing behavior across all platforms.



# JSON RAG Search
Source: https://docs.crewai.com/en/tools/file-document/jsonsearchtool

The `JSONSearchTool` is designed to search JSON files and return the most relevant results.


# `JSONSearchTool`

<Note>
  The JSONSearchTool is currently in an experimental phase. This means the tool
  is under active development, and users might encounter unexpected behavior or
  changes. We highly encourage feedback on any issues or suggestions for
  improvements.
</Note>


## Description

The JSONSearchTool is designed to facilitate efficient and precise searches within JSON file contents. It utilizes a RAG (Retrieve and Generate) search mechanism, allowing users to specify a JSON path for targeted searches within a particular JSON file. This capability significantly improves the accuracy and relevance of search results.


## Installation

To install the JSONSearchTool, use the following pip command:

```shell  theme={null}
pip install 'crewai[tools]'
```


## Usage Examples

Here are updated examples on how to utilize the JSONSearchTool effectively for searching within JSON files. These examples take into account the current implementation and usage patterns identified in the codebase.

```python Code theme={null}
from crewai_tools import JSONSearchTool


# General JSON content search

# This approach is suitable when the JSON path is either known beforehand or can be dynamically identified.
tool = JSONSearchTool()


# Restricting search to a specific JSON file

# Use this initialization method when you want to limit the search scope to a specific JSON file.
tool = JSONSearchTool(json_path='./path/to/your/file.json')
```


## Arguments

* `json_path` (str, optional): Specifies the path to the JSON file to be searched. This argument is not required if the tool is initialized for a general search. When provided, it confines the search to the specified JSON file.


## Configuration Options

The JSONSearchTool supports extensive customization through a configuration dictionary. This allows users to select different models for embeddings and summarization based on their requirements.

```python Code theme={null}
tool = JSONSearchTool(
    config={
        "llm": {
            "provider": "ollama",  # Other options include google, openai, anthropic, llama2, etc.
            "config": {
                "model": "llama2",
                # Additional optional configurations can be specified here.
                # temperature=0.5,
                # top_p=1,
                # stream=true,
            },
        },
        "embedding_model": {
            "provider": "google", # or openai, ollama, ...
            "config": {
                "model": "models/embedding-001",
                "task_type": "retrieval_document",
                # Further customization options can be added here.
            },
        },
    }
)
```



# MDX RAG Search
Source: https://docs.crewai.com/en/tools/file-document/mdxsearchtool

The `MDXSearchTool` is designed to search MDX files and return the most relevant results.


# `MDXSearchTool`

<Note>
  The MDXSearchTool is in continuous development. Features may be added or removed, and functionality could change unpredictably as we refine the tool.
</Note>


## Description

The MDX Search Tool is a component of the `crewai_tools` package aimed at facilitating advanced markdown language extraction. It enables users to effectively search and extract relevant information from MD files using query-based searches. This tool is invaluable for data analysis, information management, and research tasks, streamlining the process of finding specific information within large document collections.


## Installation

Before using the MDX Search Tool, ensure the `crewai_tools` package is installed. If it is not, you can install it with the following command:

```shell  theme={null}
pip install 'crewai[tools]'
```


## Usage Example

To use the MDX Search Tool, you must first set up the necessary environment variables. Then, integrate the tool into your crewAI project to begin your market research. Below is a basic example of how to do this:

```python Code theme={null}
from crewai_tools import MDXSearchTool


# Initialize the tool to search any MDX content it learns about during execution
tool = MDXSearchTool()


# OR


# Initialize the tool with a specific MDX file path for an exclusive search within that document
tool = MDXSearchTool(mdx='path/to/your/document.mdx')
```


## Parameters

* mdx: **Optional**. Specifies the MDX file path for the search. It can be provided during initialization.


## Customization of Model and Embeddings

The tool defaults to using OpenAI for embeddings and summarization. For customization, utilize a configuration dictionary as shown below:

```python Code theme={null}
from chromadb.config import Settings

tool = MDXSearchTool(
    config={
        "embedding_model": {
            "provider": "openai",
            "config": {
                "model": "text-embedding-3-small",
                # "api_key": "sk-...",
            },
        },
        "vectordb": {
            "provider": "chromadb",  # or "qdrant"
            "config": {
                # "settings": Settings(persist_directory="/content/chroma", allow_reset=True, is_persistent=True),
                # from qdrant_client.models import VectorParams, Distance
                # "vectors_config": VectorParams(size=384, distance=Distance.COSINE),
            }
        },
    }
)
```



# OCR Tool
Source: https://docs.crewai.com/en/tools/file-document/ocrtool

The `OCRTool` extracts text from local images or image URLs using an LLM with vision.


# `OCRTool`


## Description

Extract text from images (local path or URL). Uses a vision‑capable LLM via CrewAI’s LLM interface.


## Installation

No extra install beyond `crewai-tools`. Ensure your selected LLM supports vision.


## Parameters

### Run Parameters

* `image_path_url` (str, required): Local image path or HTTP(S) URL.


## Examples

### Direct usage

```python Code theme={null}
from crewai_tools import OCRTool

print(OCRTool().run(image_path_url="/tmp/receipt.png"))
```

### With an agent

```python Code theme={null}
from crewai import Agent, Task, Crew
from crewai_tools import OCRTool

ocr = OCRTool()

agent = Agent(
    role="OCR", 
    goal="Extract text", 
    tools=[ocr],
)

task = Task(
    description="Extract text from https://example.com/invoice.jpg", 
    expected_output="All detected text in plain text",
    agent=agent,
)

crew = Crew(agents=[agent], tasks=[task])
result = crew.kickoff()
```


## Notes

* Ensure the selected LLM supports image inputs.
* For large images, consider downscaling to reduce token usage.
* You can pass a specific LLM instance to the tool (e.g., `LLM(model="gpt-4o")`) if needed, matching the README guidance.


## Example

```python Code theme={null}
from crewai import Agent, Task, Crew
from crewai_tools import OCRTool

tool = OCRTool()

agent = Agent(
    role="OCR Specialist",
    goal="Extract text from images",
    backstory="Vision‑enabled analyst",
    tools=[tool],
    verbose=True,
)

task = Task(
    description="Extract text from https://example.com/receipt.png",
    expected_output="All detected text in plain text",
    agent=agent,
)

crew = Crew(agents=[agent], tasks=[task])
result = crew.kickoff()
```



# Overview
Source: https://docs.crewai.com/en/tools/file-document/overview

Read, write, and search through various file formats with CrewAI's document processing tools

These tools enable your agents to work with various file formats and document types. From reading PDFs to processing JSON data, these tools handle all your document processing needs.


## **Available Tools**

<CardGroup cols={2}>
  <Card title="File Read Tool" icon="folders" href="/en/tools/file-document/filereadtool">
    Read content from any file type including text, markdown, and more.
  </Card>

  <Card title="File Write Tool" icon="file-pen" href="/en/tools/file-document/filewritetool">
    Write content to files, create new documents, and save processed data.
  </Card>

  <Card title="PDF Search Tool" icon="file-pdf" href="/en/tools/file-document/pdfsearchtool">
    Search and extract text content from PDF documents efficiently.
  </Card>

  <Card title="DOCX Search Tool" icon="file-word" href="/en/tools/file-document/docxsearchtool">
    Search through Microsoft Word documents and extract relevant content.
  </Card>

  <Card title="JSON Search Tool" icon="brackets-curly" href="/en/tools/file-document/jsonsearchtool">
    Parse and search through JSON files with advanced query capabilities.
  </Card>

  <Card title="CSV Search Tool" icon="table" href="/en/tools/file-document/csvsearchtool">
    Process and search through CSV files, extract specific rows and columns.
  </Card>

  <Card title="XML Search Tool" icon="code" href="/en/tools/file-document/xmlsearchtool">
    Parse XML files and search for specific elements and attributes.
  </Card>

  <Card title="MDX Search Tool" icon="markdown" href="/en/tools/file-document/mdxsearchtool">
    Search through MDX files and extract content from documentation.
  </Card>

  <Card title="TXT Search Tool" icon="file-lines" href="/en/tools/file-document/txtsearchtool">
    Search through plain text files with pattern matching capabilities.
  </Card>

  <Card title="Directory Search Tool" icon="folder-open" href="/en/tools/file-document/directorysearchtool">
    Search for files and folders within directory structures.
  </Card>

  <Card title="Directory Read Tool" icon="folder" href="/en/tools/file-document/directoryreadtool">
    Read and list directory contents, file structures, and metadata.
  </Card>

  <Card title="OCR Tool" icon="image" href="/en/tools/file-document/ocrtool">
    Extract text from images (local files or URLs) using a vision‑capable LLM.
  </Card>

  <Card title="PDF Text Writing Tool" icon="file-pdf" href="/en/tools/file-document/pdf-text-writing-tool">
    Write text at specific coordinates in PDFs, with optional custom fonts.
  </Card>
</CardGroup>


## **Common Use Cases**

* **Document Processing**: Extract and analyze content from various file formats
* **Data Import**: Read structured data from CSV, JSON, and XML files
* **Content Search**: Find specific information within large document collections
* **File Management**: Organize and manipulate files and directories
* **Data Export**: Save processed results to various file formats


## **Quick Start Example**

```python  theme={null}
from crewai_tools import FileReadTool, PDFSearchTool, JSONSearchTool


# Create tools
file_reader = FileReadTool()
pdf_searcher = PDFSearchTool()
json_processor = JSONSearchTool()


# Add to your agent
agent = Agent(
    role="Document Analyst",
    tools=[file_reader, pdf_searcher, json_processor],
    goal="Process and analyze various document types"
)
```


## **Tips for Document Processing**

* **File Permissions**: Ensure your agent has proper read/write permissions
* **Large Files**: Consider chunking for very large documents
* **Format Support**: Check tool documentation for supported file formats
* **Error Handling**: Implement proper error handling for corrupted or inaccessible files



# PDF Text Writing Tool
Source: https://docs.crewai.com/en/tools/file-document/pdf-text-writing-tool

The `PDFTextWritingTool` writes text to specific positions in a PDF, supporting custom fonts.


# `PDFTextWritingTool`


## Description

Write text at precise coordinates on a PDF page, optionally embedding a custom TrueType font.


## Parameters

### Run Parameters

* `pdf_path` (str, required): Path to the input PDF.
* `text` (str, required): Text to add.
* `position` (tuple\[int, int], required): `(x, y)` coordinates.
* `font_size` (int, default `12`)
* `font_color` (str, default `"0 0 0 rg"`)
* `font_name` (str, default `"F1"`)
* `font_file` (str, optional): Path to `.ttf` file.
* `page_number` (int, default `0`)


## Example

```python Code theme={null}
from crewai import Agent, Task, Crew
from crewai_tools import PDFTextWritingTool

tool = PDFTextWritingTool()

agent = Agent(
    role="PDF Editor",
    goal="Annotate PDFs",
    backstory="Documentation specialist",
    tools=[tool],
    verbose=True,
)

task = Task(
    description="Write 'CONFIDENTIAL' at (72, 720) on page 1 of ./sample.pdf",
    expected_output="Confirmation message",
    agent=agent,
)

crew = Crew(
    agents=[agent], 
    tasks=[task],
    verbose=True,
)

result = crew.kickoff()
```

### Direct usage

```python Code theme={null}
from crewai_tools import PDFTextWritingTool

PDFTextWritingTool().run(
  pdf_path="./input.pdf",
  text="CONFIDENTIAL",
  position=(72, 720),
  font_size=18,
  page_number=0,
)
```


## Tips

* Coordinate origin is the bottom‑left corner.
* If using a custom font (`font_file`), ensure it is a valid `.ttf`.



# PDF RAG Search
Source: https://docs.crewai.com/en/tools/file-document/pdfsearchtool

The `PDFSearchTool` is designed to search PDF files and return the most relevant results.


# `PDFSearchTool`

<Note>
  We are still working on improving tools, so there might be unexpected behavior or changes in the future.
</Note>


## Description

The PDFSearchTool is a RAG tool designed for semantic searches within PDF content. It allows for inputting a search query and a PDF document, leveraging advanced search techniques to find relevant content efficiently.
This capability makes it especially useful for extracting specific information from large PDF files quickly.


## Installation

To get started with the PDFSearchTool, first, ensure the crewai\_tools package is installed with the following command:

```shell  theme={null}
pip install 'crewai[tools]'
```


## Example

Here's how to use the PDFSearchTool to search within a PDF document:

```python Code theme={null}
from crewai_tools import PDFSearchTool


# Initialize the tool allowing for any PDF content search if the path is provided during execution
tool = PDFSearchTool()


# OR


# Initialize the tool with a specific PDF path for exclusive search within that document
tool = PDFSearchTool(pdf='path/to/your/document.pdf')
```


## Arguments

* `pdf`: **Optional** The PDF path for the search. Can be provided at initialization or within the `run` method's arguments. If provided at initialization, the tool confines its search to the specified document.


## Custom model and embeddings

By default, the tool uses OpenAI for both embeddings and summarization. To customize the model, you can use a config dictionary as follows. Note: a vector database is required because generated embeddings must be stored and queried from a vectordb.

```python Code theme={null}
from crewai_tools import PDFSearchTool


# - embedding_model (required): choose provider + provider-specific config

# - vectordb (required): choose vector DB and pass its config

tool = PDFSearchTool(
    config={
        "embedding_model": {
            # Supported providers: "openai", "azure", "google-generativeai", "google-vertex",
            # "voyageai", "cohere", "huggingface", "jina", "sentence-transformer",
            # "text2vec", "ollama", "openclip", "instructor", "onnx", "roboflow", "watsonx", "custom"
            "provider": "openai",  # or: "google-generativeai", "cohere", "ollama", ...
            "config": {
                # Model identifier for the chosen provider. "model" will be auto-mapped to "model_name" internally.
                "model": "text-embedding-3-small",
                # Optional: API key. If omitted, the tool will use provider-specific env vars when available
                # (e.g., OPENAI_API_KEY for provider="openai").
                # "api_key": "sk-...",

                # Provider-specific examples:
                # --- Google Generative AI ---
                # (Set provider="google-generativeai" above)
                # "model": "models/embedding-001",
                # "task_type": "retrieval_document",
                # "title": "Embeddings",

                # --- Cohere ---
                # (Set provider="cohere" above)
                # "model": "embed-english-v3.0",

                # --- Ollama (local) ---
                # (Set provider="ollama" above)
                # "model": "nomic-embed-text",
            },
        },
        "vectordb": {
                    "provider": "chromadb",  # or "qdrant"
                    "config": {
                        # For ChromaDB: pass "settings" (chromadb.config.Settings) or rely on defaults.
                        # Example (uncomment and import):
                        # from chromadb.config import Settings
                        # "settings": Settings(
                        #     persist_directory="/content/chroma",
                        #     allow_reset=True,
                        #     is_persistent=True,
                        # ),

                        # For Qdrant: pass "vectors_config" (qdrant_client.models.VectorParams).
                        # Example (uncomment and import):
                        # from qdrant_client.models import VectorParams, Distance
                        # "vectors_config": VectorParams(size=384, distance=Distance.COSINE),

                        # Note: collection name is controlled by the tool (default: "rag_tool_collection"), not set here.
                    }
        },
    }
)
```



# TXT RAG Search
Source: https://docs.crewai.com/en/tools/file-document/txtsearchtool

The `TXTSearchTool` is designed to perform a RAG (Retrieval-Augmented Generation) search within the content of a text file.


## Overview

<Note>
  We are still working on improving tools, so there might be unexpected behavior or changes in the future.
</Note>

This tool is used to perform a RAG (Retrieval-Augmented Generation) search within the content of a text file.
It allows for semantic searching of a query within a specified text file's content,
making it an invaluable resource for quickly extracting information or finding specific sections of text based on the query provided.


## Installation

To use the `TXTSearchTool`, you first need to install the `crewai_tools` package.
This can be done using pip, a package manager for Python.
Open your terminal or command prompt and enter the following command:

```shell  theme={null}
pip install 'crewai[tools]'
```

This command will download and install the TXTSearchTool along with any necessary dependencies.


## Example

The following example demonstrates how to use the TXTSearchTool to search within a text file.
This example shows both the initialization of the tool with a specific text file and the subsequent search within that file's content.

```python Code theme={null}
from crewai_tools import TXTSearchTool


# Initialize the tool to search within any text file's content 

# the agent learns about during its execution
tool = TXTSearchTool()


# OR


# Initialize the tool with a specific text file, 

# so the agent can search within the given text file's content
tool = TXTSearchTool(txt='path/to/text/file.txt')
```


## Arguments

* `txt` (str): **Optional**. The path to the text file you want to search.
  This argument is only required if the tool was not initialized with a specific text file;
  otherwise, the search will be conducted within the initially provided text file.


## Custom model and embeddings

By default, the tool uses OpenAI for both embeddings and summarization.
To customize the model, you can use a config dictionary as follows:

```python Code theme={null}
from chromadb.config import Settings

tool = TXTSearchTool(
    config={
        # Required: embeddings provider + config
        "embedding_model": {
            "provider": "openai",  # or google-generativeai, cohere, ollama, ...
            "config": {
                "model": "text-embedding-3-small",
                # "api_key": "sk-...",  # optional if env var is set
                # Provider examples:
                # Google → model: "models/embedding-001", task_type: "retrieval_document"
                # Cohere → model: "embed-english-v3.0"
                # Ollama → model: "nomic-embed-text"
            },
        },

        # Required: vector database config
        "vectordb": {
            "provider": "chromadb",  # or "qdrant"
            "config": {
                # Chroma settings (optional persistence)
                # "settings": Settings(
                #     persist_directory="/content/chroma",
                #     allow_reset=True,
                #     is_persistent=True,
                # ),

                # Qdrant vector params example:
                # from qdrant_client.models import VectorParams, Distance
                # "vectors_config": VectorParams(size=384, distance=Distance.COSINE),

                # Note: collection name is controlled by the tool (default: "rag_tool_collection").
            }
        },
    }
)
```



# XML RAG Search
Source: https://docs.crewai.com/en/tools/file-document/xmlsearchtool

The `XMLSearchTool` is designed to perform a RAG (Retrieval-Augmented Generation) search within the content of a XML file.


# `XMLSearchTool`

<Note>
  We are still working on improving tools, so there might be unexpected behavior or changes in the future.
</Note>


## Description

The XMLSearchTool is a cutting-edge RAG tool engineered for conducting semantic searches within XML files.
Ideal for users needing to parse and extract information from XML content efficiently, this tool supports inputting a search query and an optional XML file path.
By specifying an XML path, users can target their search more precisely to the content of that file, thereby obtaining more relevant search outcomes.


## Installation

To start using the XMLSearchTool, you must first install the crewai\_tools package. This can be easily done with the following command:

```shell  theme={null}
pip install 'crewai[tools]'
```


## Example

Here are two examples demonstrating how to use the XMLSearchTool.
The first example shows searching within a specific XML file, while the second example illustrates initiating a search without predefining an XML path, providing flexibility in search scope.

```python Code theme={null}
from crewai_tools import XMLSearchTool


# Allow agents to search within any XML file's content 
#as it learns about their paths during execution
tool = XMLSearchTool()


# OR


# Initialize the tool with a specific XML file path 
#for exclusive search within that document
tool = XMLSearchTool(xml='path/to/your/xmlfile.xml')
```


## Arguments

* `xml`: This is the path to the XML file you wish to search.
  It is an optional parameter during the tool's initialization but must be provided either at initialization or as part of the `run` method's arguments to execute a search.


## Custom model and embeddings

By default, the tool uses OpenAI for both embeddings and summarization. To customize the model, you can use a config dictionary as follows:

```python Code   theme={null}
from chromadb.config import Settings

tool = XMLSearchTool(
    config={
        "embedding_model": {
            "provider": "openai",
            "config": {
                "model": "text-embedding-3-small",
                # "api_key": "sk-...",
            },
        },
        "vectordb": {
            "provider": "chromadb",  # or "qdrant"
            "config": {
                # "settings": Settings(persist_directory="/content/chroma", allow_reset=True, is_persistent=True),
                # from qdrant_client.models import VectorParams, Distance
                # "vectors_config": VectorParams(size=384, distance=Distance.COSINE),
            }
        },
    }
)
```



# Tools Overview
Source: https://docs.crewai.com/en/tools/overview

Discover CrewAI's extensive library of 40+ tools to supercharge your AI agents

CrewAI provides an extensive library of pre-built tools to enhance your agents' capabilities. From file processing to web scraping, database queries to AI services - we've got you covered.


## **Tool Categories**

<CardGroup cols={2}>
  <Card title="File & Document" icon="folder-open" href="/en/tools/file-document/overview" color="#3B82F6">
    Read, write, and search through various file formats including PDF, DOCX, JSON, CSV, and more. Perfect for document processing workflows.
  </Card>

  <Card title="Web Scraping & Browsing" icon="globe" href="/en/tools/web-scraping/overview" color="#10B981">
    Extract data from websites, automate browser interactions, and scrape content at scale with tools like Firecrawl, Selenium, and more.
  </Card>

  <Card title="Search & Research" icon="magnifying-glass" href="/en/tools/search-research/overview" color="#F59E0B">
    Perform web searches, find code repositories, research YouTube content, and discover information across the internet.
  </Card>

  <Card title="Database & Data" icon="database" href="/en/tools/database-data/overview" color="#8B5CF6">
    Connect to SQL databases, vector stores, and data warehouses. Query MySQL, PostgreSQL, Snowflake, Qdrant, and Weaviate.
  </Card>

  <Card title="AI & Machine Learning" icon="brain" href="/en/tools/ai-ml/overview" color="#EF4444">
    Generate images with DALL-E, process vision tasks, integrate with LangChain, build RAG systems, and leverage code interpreters.
  </Card>

  <Card title="Cloud & Storage" icon="cloud" href="/en/tools/cloud-storage/overview" color="#06B6D4">
    Interact with cloud services including AWS S3, Amazon Bedrock, and other cloud storage and AI services.
  </Card>

  <Card title="Automation" icon="bolt" href="/en/tools/automation/overview" color="#84CC16">
    Automate workflows with Apify, Composio, and other platforms to connect your agents with external services.
  </Card>

  <Card title="Integrations" icon="plug" href="/en/tools/tool-integrations/overview" color="#0891B2">
    Integrate CrewAI with external systems like Amazon Bedrock and the CrewAI Automation toolkit.
  </Card>
</CardGroup>


## **Quick Access**

Need a specific tool? Here are some popular choices:

<CardGroup cols={3}>
  <Card title="RAG Tool" icon="image" href="/en/tools/ai-ml/ragtool">
    Implement Retrieval-Augmented Generation
  </Card>

  <Card title="Serper Dev" icon="book-atlas" href="/en/tools/search-research/serperdevtool">
    Google search API
  </Card>

  <Card title="File Read" icon="file" href="/en/tools/file-document/filereadtool">
    Read any file type
  </Card>

  <Card title="Scrape Website" icon="globe" href="/en/tools/web-scraping/scrapewebsitetool">
    Extract web content
  </Card>

  <Card title="Code Interpreter" icon="code" href="/en/tools/ai-ml/codeinterpretertool">
    Execute Python code
  </Card>

  <Card title="S3 Reader" icon="cloud" href="/en/tools/cloud-storage/s3readertool">
    Access AWS S3 files
  </Card>
</CardGroup>


## **Getting Started**

To use any tool in your CrewAI project:

1. **Import** the tool in your crew configuration
2. **Add** it to your agent's tools list
3. **Configure** any required API keys or settings

```python  theme={null}
from crewai_tools import FileReadTool, SerperDevTool


# Add tools to your agent
agent = Agent(
    role="Research Analyst",
    tools=[FileReadTool(), SerperDevTool()],
    # ... other configuration
)
```


## **Max Usage Count**

You can set a maximum usage count for a tool to prevent it from being used more than a certain number of times.
By default, the max usage count is unlimited.

```python  theme={null}
from crewai_tools import FileReadTool

tool = FileReadTool(max_usage_count=5, ...)
```

Ready to explore? Pick a category above to discover tools that fit your use case!



# Arxiv Paper Tool
Source: https://docs.crewai.com/en/tools/search-research/arxivpapertool

The `ArxivPaperTool` searches arXiv for papers matching a query and optionally downloads PDFs.


# `ArxivPaperTool`


## Description

The `ArxivPaperTool` queries the arXiv API for academic papers and returns compact, readable results. It can also optionally download PDFs to disk.


## Installation

This tool has no special installation beyond `crewai-tools`.

```shell  theme={null}
uv add crewai-tools
```

No API key is required. This tool uses the public arXiv Atom API.


## Steps to Get Started

1. Initialize the tool.
2. Provide a `search_query` (e.g., "transformer neural network").
3. Optionally set `max_results` (1–100) and enable PDF downloads in the constructor.


## Example

```python Code theme={null}
from crewai import Agent, Task, Crew
from crewai_tools import ArxivPaperTool

tool = ArxivPaperTool(
    download_pdfs=False,
    save_dir="./arxiv_pdfs",
    use_title_as_filename=True,
)

agent = Agent(
    role="Researcher",
    goal="Find relevant arXiv papers",
    backstory="Expert at literature discovery",
    tools=[tool],
    verbose=True,
)

task = Task(
    description="Search arXiv for 'transformer neural network' and list top 5 results.",
    expected_output="A concise list of 5 relevant papers with titles, links, and summaries.",
    agent=agent,
)

crew = Crew(agents=[agent], tasks=[task])
result = crew.kickoff()
```

### Direct usage (without Agent)

```python Code theme={null}
from crewai_tools import ArxivPaperTool

tool = ArxivPaperTool(
    download_pdfs=True, 
    save_dir="./arxiv_pdfs",
)
print(tool.run(search_query="mixture of experts", max_results=3))
```


## Parameters

### Initialization Parameters

* `download_pdfs` (bool, default `False`): Whether to download PDFs.
* `save_dir` (str, default `./arxiv_pdfs`): Directory to save PDFs.
* `use_title_as_filename` (bool, default `False`): Use paper titles for filenames.

### Run Parameters

* `search_query` (str, required): The arXiv search query.
* `max_results` (int, default `5`, range 1–100): Number of results.


## Output format

The tool returns a human‑readable list of papers with:

* Title
* Link (abs page)
* Snippet/summary (truncated)

When `download_pdfs=True`, PDFs are saved to disk and the summary mentions saved files.


## Usage Notes

* The tool returns formatted text with key metadata and links.
* When `download_pdfs=True`, PDFs will be stored in `save_dir`.


## Troubleshooting

* If you receive a network timeout, re‑try or reduce `max_results`.
* Invalid XML errors indicate an arXiv response parse issue; try a simpler query.
* File system errors (e.g., permission denied) may occur when saving PDFs; ensure `save_dir` is writable.


## Related links

* arXiv API docs: [https://info.arxiv.org/help/api/index.html](https://info.arxiv.org/help/api/index.html)


## Error Handling

* Network issues, invalid XML, and OS errors are handled with informative messages.



# Brave Search
Source: https://docs.crewai.com/en/tools/search-research/bravesearchtool

The `BraveSearchTool` is designed to search the internet using the Brave Search API.


# `BraveSearchTool`


## Description

This tool is designed to perform web searches using the Brave Search API. It allows you to search the internet with a specified query and retrieve relevant results. The tool supports customizable result counts and country-specific searches.


## Installation

To incorporate this tool into your project, follow the installation instructions below:

```shell  theme={null}
pip install 'crewai[tools]'
```


## Steps to Get Started

To effectively use the `BraveSearchTool`, follow these steps:

1. **Package Installation**: Confirm that the `crewai[tools]` package is installed in your Python environment.
2. **API Key Acquisition**: Acquire a Brave Search API key at [https://api.search.brave.com/app/keys](https://api.search.brave.com/app/keys) (sign in to generate a key).
3. **Environment Configuration**: Store your obtained API key in an environment variable named `BRAVE_API_KEY` to facilitate its use by the tool.


## Example

The following example demonstrates how to initialize the tool and execute a search with a given query:

```python Code theme={null}
from crewai_tools import BraveSearchTool


# Initialize the tool for internet searching capabilities
tool = BraveSearchTool()


# Execute a search
results = tool.run(search_query="CrewAI agent framework")
print(results)
```


## Parameters

The `BraveSearchTool` accepts the following parameters:

* **search\_query**: Mandatory. The search query you want to use to search the internet.
* **country**: Optional. Specify the country for the search results. Default is empty string.
* **n\_results**: Optional. Number of search results to return. Default is `10`.
* **save\_file**: Optional. Whether to save the search results to a file. Default is `False`.


## Example with Parameters

Here is an example demonstrating how to use the tool with additional parameters:

```python Code theme={null}
from crewai_tools import BraveSearchTool


# Initialize the tool with custom parameters
tool = BraveSearchTool(
    country="US",
    n_results=5,
    save_file=True
)


# Execute a search
results = tool.run(search_query="Latest AI developments")
print(results)
```


## Agent Integration Example

Here's how to integrate the `BraveSearchTool` with a CrewAI agent:

```python Code theme={null}
from crewai import Agent
from crewai.project import agent
from crewai_tools import BraveSearchTool


# Initialize the tool
brave_search_tool = BraveSearchTool()


# Define an agent with the BraveSearchTool
@agent
def researcher(self) -> Agent:
    return Agent(
        config=self.agents_config["researcher"],
        allow_delegation=False,
        tools=[brave_search_tool]
    )
```


## Conclusion

By integrating the `BraveSearchTool` into Python projects, users gain the ability to conduct real-time, relevant searches across the internet directly from their applications. The tool provides a simple interface to the powerful Brave Search API, making it easy to retrieve and process search results programmatically. By adhering to the setup and usage guidelines provided, incorporating this tool into projects is streamlined and straightforward.



# Code Docs RAG Search
Source: https://docs.crewai.com/en/tools/search-research/codedocssearchtool

The `CodeDocsSearchTool` is a powerful RAG (Retrieval-Augmented Generation) tool designed for semantic searches within code documentation.


# `CodeDocsSearchTool`

<Note>
  **Experimental**: We are still working on improving tools, so there might be unexpected behavior or changes in the future.
</Note>


## Description

The CodeDocsSearchTool is a powerful RAG (Retrieval-Augmented Generation) tool designed for semantic searches within code documentation.
It enables users to efficiently find specific information or topics within code documentation. By providing a `docs_url` during initialization,
the tool narrows down the search to that particular documentation site. Alternatively, without a specific `docs_url`,
it searches across a wide array of code documentation known or discovered throughout its execution, making it versatile for various documentation search needs.


## Installation

To start using the CodeDocsSearchTool, first, install the crewai\_tools package via pip:

```shell  theme={null}
pip install 'crewai[tools]'
```


## Example

Utilize the CodeDocsSearchTool as follows to conduct searches within code documentation:

```python Code theme={null}
from crewai_tools import CodeDocsSearchTool


# To search any code documentation content 

# if the URL is known or discovered during its execution:
tool = CodeDocsSearchTool()


# OR


# To specifically focus your search on a given documentation site 

# by providing its URL:
tool = CodeDocsSearchTool(docs_url='https://docs.example.com/reference')
```

<Note>
  Substitute '[https://docs.example.com/reference](https://docs.example.com/reference)' with your target documentation URL
  and 'How to use search tool' with the search query relevant to your needs.
</Note>


## Arguments

The following parameters can be used to customize the `CodeDocsSearchTool`'s behavior:

| Argument      | Type     | Description                                                             |
| :------------ | :------- | :---------------------------------------------------------------------- |
| **docs\_url** | `string` | *Optional*. Specifies the URL of the code documentation to be searched. |


## Custom model and embeddings

By default, the tool uses OpenAI for both embeddings and summarization. To customize the model, you can use a config dictionary as follows:

```python Code theme={null}
tool = CodeDocsSearchTool(
    config=dict(
        llm=dict(
            provider="ollama", # or google, openai, anthropic, llama2, ...
            config=dict(
                model="llama2",
                # temperature=0.5,
                # top_p=1,
                # stream=true,
            ),
        ),
        embedder=dict(
            provider="google", # or openai, ollama, ...
            config=dict(
                model="models/embedding-001",
                task_type="retrieval_document",
                # title="Embeddings",
            ),
        ),
    )
)
```



# Databricks SQL Query Tool
Source: https://docs.crewai.com/en/tools/search-research/databricks-query-tool

The `DatabricksQueryTool` executes SQL queries against Databricks workspace tables.


# `DatabricksQueryTool`


## Description

Run SQL against Databricks workspace tables with either CLI profile or direct host/token authentication.


## Installation

```shell  theme={null}
uv add crewai-tools[databricks-sdk]
```


## Environment Variables

* `DATABRICKS_CONFIG_PROFILE` or (`DATABRICKS_HOST` + `DATABRICKS_TOKEN`)

Create a personal access token and find host details in the Databricks workspace under User Settings → Developer.
Docs: [https://docs.databricks.com/en/dev-tools/auth/pat.html](https://docs.databricks.com/en/dev-tools/auth/pat.html)


## Example

```python Code theme={null}
from crewai import Agent, Task, Crew
from crewai_tools import DatabricksQueryTool

tool = DatabricksQueryTool(
    default_catalog="main", 
    default_schema="default",
)

agent = Agent(
    role="Data Analyst",
    goal="Query Databricks",
    tools=[tool],
    verbose=True,
)

task = Task(
    description="SELECT * FROM my_table LIMIT 10",
    expected_output="10 rows", 
    agent=agent,
)

crew = Crew(
    agents=[agent], 
    tasks=[task],
    verbose=True,
)
result = crew.kickoff()

print(result)
```


## Parameters

* `query` (required): SQL query to execute
* `catalog` (optional): Override default catalog
* `db_schema` (optional): Override default schema
* `warehouse_id` (optional): Override default SQL warehouse
* `row_limit` (optional): Maximum rows to return (default: 1000)


## Defaults on initialization

* `default_catalog`
* `default_schema`
* `default_warehouse_id`

### Error handling & tips

* Authentication errors: verify `DATABRICKS_HOST` begins with `https://` and token is valid.
* Permissions: ensure your SQL warehouse and schema are accessible by your token.
* Limits: long‑running queries should be avoided in agent loops; add filters/limits.



# EXA Search Web Loader
Source: https://docs.crewai.com/en/tools/search-research/exasearchtool

The `EXASearchTool` is designed to perform a semantic search for a specified query from a text's content across the internet.


# `EXASearchTool`


## Description

The EXASearchTool is designed to perform a semantic search for a specified query from a text's content across the internet.
It utilizes the [exa.ai](https://exa.ai/) API to fetch and display the most relevant search results based on the query provided by the user.


## Installation

To incorporate this tool into your project, follow the installation instructions below:

```shell  theme={null}
pip install 'crewai[tools]'
```


## Example

The following example demonstrates how to initialize the tool and execute a search with a given query:

```python Code theme={null}
from crewai_tools import EXASearchTool


# Initialize the tool for internet searching capabilities
tool = EXASearchTool()
```


## Steps to Get Started

To effectively use the EXASearchTool, follow these steps:

<Steps>
  <Step title="Package Installation">
    Confirm that the `crewai[tools]` package is installed in your Python environment.
  </Step>

  <Step title="API Key Acquisition">
    Acquire a [exa.ai](https://exa.ai/) API key by registering for a free account at [exa.ai](https://exa.ai/).
  </Step>

  <Step title="Environment Configuration">
    Store your obtained API key in an environment variable named `EXA_API_KEY` to facilitate its use by the tool.
  </Step>
</Steps>


## Conclusion

By integrating the `EXASearchTool` into Python projects, users gain the ability to conduct real-time, relevant searches across the internet directly from their applications.
By adhering to the setup and usage guidelines provided, incorporating this tool into projects is streamlined and straightforward.



# Github Search
Source: https://docs.crewai.com/en/tools/search-research/githubsearchtool

The `GithubSearchTool` is designed to search websites and convert them into clean markdown or structured data.


# `GithubSearchTool`

<Note>
  We are still working on improving tools, so there might be unexpected behavior or changes in the future.
</Note>


## Description

The GithubSearchTool is a Retrieval-Augmented Generation (RAG) tool specifically designed for conducting semantic searches within GitHub repositories. Utilizing advanced semantic search capabilities, it sifts through code, pull requests, issues, and repositories, making it an essential tool for developers, researchers, or anyone in need of precise information from GitHub.


## Installation

To use the GithubSearchTool, first ensure the crewai\_tools package is installed in your Python environment:

```shell  theme={null}
pip install 'crewai[tools]'
```

This command installs the necessary package to run the GithubSearchTool along with any other tools included in the crewai\_tools package.

Get a GitHub Personal Access Token at [https://github.com/settings/tokens](https://github.com/settings/tokens) (Developer settings → Fine‑grained tokens or classic tokens).


## Example

Here’s how you can use the GithubSearchTool to perform semantic searches within a GitHub repository:

```python Code theme={null}
from crewai_tools import GithubSearchTool


# Initialize the tool for semantic searches within a specific GitHub repository
tool = GithubSearchTool(
	github_repo='https://github.com/example/repo',
	gh_token='your_github_personal_access_token',
	content_types=['code', 'issue'] # Options: code, repo, pr, issue
)


# OR


# Initialize the tool for semantic searches within a specific GitHub repository, so the agent can search any repository if it learns about during its execution
tool = GithubSearchTool(
	gh_token='your_github_personal_access_token',
	content_types=['code', 'issue'] # Options: code, repo, pr, issue
)
```


## Arguments

* `github_repo` : The URL of the GitHub repository where the search will be conducted. This is a mandatory field and specifies the target repository for your search.
* `gh_token` : Your GitHub Personal Access Token (PAT) required for authentication. You can create one in your GitHub account settings under Developer Settings > Personal Access Tokens.
* `content_types` : Specifies the types of content to include in your search. You must provide a list of content types from the following options: `code` for searching within the code,
  `repo` for searching within the repository's general information, `pr` for searching within pull requests, and `issue` for searching within issues.
  This field is mandatory and allows tailoring the search to specific content types within the GitHub repository.


## Custom model and embeddings

By default, the tool uses OpenAI for both embeddings and summarization. To customize the model, you can use a config dictionary as follows:

```python Code theme={null}
tool = GithubSearchTool(
    config=dict(
        llm=dict(
            provider="ollama", # or google, openai, anthropic, llama2, ...
            config=dict(
                model="llama2",
                # temperature=0.5,
                # top_p=1,
                # stream=true,
            ),
        ),
        embedder=dict(
            provider="google", # or openai, ollama, ...
            config=dict(
                model="models/embedding-001",
                task_type="retrieval_document",
                # title="Embeddings",
            ),
        ),
    )
)
```



# Linkup Search Tool
Source: https://docs.crewai.com/en/tools/search-research/linkupsearchtool

The `LinkupSearchTool` enables querying the Linkup API for contextual information.


# `LinkupSearchTool`


## Description

The `LinkupSearchTool` provides the ability to query the Linkup API for contextual information and retrieve structured results. This tool is ideal for enriching workflows with up-to-date and reliable information from Linkup, allowing agents to access relevant data during their tasks.


## Installation

To use this tool, you need to install the Linkup SDK:

```shell  theme={null}
uv add linkup-sdk
```


## Steps to Get Started

To effectively use the `LinkupSearchTool`, follow these steps:

1. **API Key**: Obtain a Linkup API key.
2. **Environment Setup**: Set up your environment with the API key.
3. **Install SDK**: Install the Linkup SDK using the command above.


## Example

The following example demonstrates how to initialize the tool and use it in an agent:

```python Code theme={null}
from crewai_tools import LinkupSearchTool
from crewai import Agent
import os


# Initialize the tool with your API key
linkup_tool = LinkupSearchTool(api_key=os.getenv("LINKUP_API_KEY"))


# Define an agent that uses the tool
@agent
def researcher(self) -> Agent:
    '''
    This agent uses the LinkupSearchTool to retrieve contextual information
    from the Linkup API.
    '''
    return Agent(
        config=self.agents_config["researcher"],
        tools=[linkup_tool]
    )
```


## Parameters

The `LinkupSearchTool` accepts the following parameters:

### Constructor Parameters

* **api\_key**: Required. Your Linkup API key.

### Run Parameters

* **query**: Required. The search term or phrase.
* **depth**: Optional. The search depth. Default is "standard".
* **output\_type**: Optional. The type of output. Default is "searchResults".


## Advanced Usage

You can customize the search parameters for more specific results:

```python Code theme={null}

# Perform a search with custom parameters
results = linkup_tool.run(
    query="Women Nobel Prize Physics",
    depth="deep",
    output_type="searchResults"
)
```


## Return Format

The tool returns results in the following format:

```json  theme={null}
{
  "success": true,
  "results": [
    {
      "name": "Result Title",
      "url": "https://example.com/result",
      "content": "Content of the result..."
    },
    // Additional results...
  ]
}
```

If an error occurs, the response will be:

```json  theme={null}
{
  "success": false,
  "error": "Error message"
}
```


## Error Handling

The tool gracefully handles API errors and provides structured feedback. If the API request fails, the tool will return a dictionary with `success: false` and an error message.


## Conclusion

The `LinkupSearchTool` provides a seamless way to integrate Linkup's contextual information retrieval capabilities into your CrewAI agents. By leveraging this tool, agents can access relevant and up-to-date information to enhance their decision-making and task execution.



# Overview
Source: https://docs.crewai.com/en/tools/search-research/overview

Perform web searches, find repositories, and research information across the internet

These tools enable your agents to search the web, research topics, and find information across various platforms including search engines, GitHub, and YouTube.


## **Available Tools**

<CardGroup cols={2}>
  <Card title="Serper Dev Tool" icon="google" href="/en/tools/search-research/serperdevtool">
    Google search API integration for comprehensive web search capabilities.
  </Card>

  <Card title="Brave Search Tool" icon="shield" href="/en/tools/search-research/bravesearchtool">
    Privacy-focused search with Brave's independent search index.
  </Card>

  <Card title="Exa Search Tool" icon="magnifying-glass" href="/en/tools/search-research/exasearchtool">
    AI-powered search for finding specific and relevant content.
  </Card>

  <Card title="LinkUp Search Tool" icon="link" href="/en/tools/search-research/linkupsearchtool">
    Real-time web search with fresh content indexing.
  </Card>

  <Card title="GitHub Search Tool" icon="github" href="/en/tools/search-research/githubsearchtool">
    Search GitHub repositories, code, issues, and documentation.
  </Card>

  <Card title="Website Search Tool" icon="globe" href="/en/tools/search-research/websitesearchtool">
    Search within specific websites and domains.
  </Card>

  <Card title="Code Docs Search Tool" icon="code" href="/en/tools/search-research/codedocssearchtool">
    Search through code documentation and technical resources.
  </Card>

  <Card title="YouTube Channel Search" icon="youtube" href="/en/tools/search-research/youtubechannelsearchtool">
    Search YouTube channels for specific content and creators.
  </Card>

  <Card title="YouTube Video Search" icon="play" href="/en/tools/search-research/youtubevideosearchtool">
    Find and analyze YouTube videos by topic, keyword, or criteria.
  </Card>

  <Card title="Tavily Search Tool" icon="magnifying-glass" href="/en/tools/search-research/tavilysearchtool">
    Comprehensive web search using Tavily's AI-powered search API.
  </Card>

  <Card title="Tavily Extractor Tool" icon="file-text" href="/en/tools/search-research/tavilyextractortool">
    Extract structured content from web pages using the Tavily API.
  </Card>

  <Card title="Arxiv Paper Tool" icon="box-archive" href="/en/tools/search-research/arxivpapertool">
    Search arXiv and optionally download PDFs.
  </Card>

  <Card title="SerpApi Google Search" icon="search" href="/en/tools/search-research/serpapi-googlesearchtool">
    Google search via SerpApi with structured results.
  </Card>

  <Card title="SerpApi Google Shopping" icon="cart-shopping" href="/en/tools/search-research/serpapi-googleshoppingtool">
    Google Shopping queries via SerpApi.
  </Card>
</CardGroup>


## **Common Use Cases**

* **Market Research**: Search for industry trends and competitor analysis
* **Content Discovery**: Find relevant articles, videos, and resources
* **Code Research**: Search repositories and documentation for solutions
* **Lead Generation**: Research companies and individuals
* **Academic Research**: Find scholarly articles and technical papers

```python  theme={null}
from crewai_tools import SerperDevTool, GitHubSearchTool, YoutubeVideoSearchTool, TavilySearchTool, TavilyExtractorTool


# Create research tools
web_search = SerperDevTool()
code_search = GitHubSearchTool()
video_research = YoutubeVideoSearchTool()
tavily_search = TavilySearchTool()
content_extractor = TavilyExtractorTool()


# Add to your agent
agent = Agent(
    role="Research Analyst",
    tools=[web_search, code_search, video_research, tavily_search, content_extractor],
    goal="Gather comprehensive information on any topic"
)
```



# SerpApi Google Search Tool
Source: https://docs.crewai.com/en/tools/search-research/serpapi-googlesearchtool

The `SerpApiGoogleSearchTool` performs Google searches using the SerpApi service.


# `SerpApiGoogleSearchTool`


## Description

Use the `SerpApiGoogleSearchTool` to run Google searches with SerpApi and retrieve structured results. Requires a SerpApi API key.


## Installation

```shell  theme={null}
uv add crewai-tools[serpapi]
```


## Environment Variables

* `SERPAPI_API_KEY` (required): API key for SerpApi. Create one at [https://serpapi.com/](https://serpapi.com/) (free tier available).


## Example

```python Code theme={null}
from crewai import Agent, Task, Crew
from crewai_tools import SerpApiGoogleSearchTool

tool = SerpApiGoogleSearchTool()

agent = Agent(
    role="Researcher",
    goal="Answer questions using Google search",
    backstory="Search specialist",
    tools=[tool],
    verbose=True,
)

task = Task(
    description="Search for the latest CrewAI releases",
    expected_output="A concise list of relevant results with titles and links",
    agent=agent,
)

crew = Crew(agents=[agent], tasks=[task])
result = crew.kickoff()
```


## Notes

* Set `SERPAPI_API_KEY` in the environment. Create a key at [https://serpapi.com/](https://serpapi.com/)
* See also Google Shopping via SerpApi: `/en/tools/search-research/serpapi-googleshoppingtool`


## Parameters

### Run Parameters

* `search_query` (str, required): The Google query.
* `location` (str, optional): Geographic location parameter.


## Notes

* This tool wraps SerpApi and returns structured search results.



# SerpApi Google Shopping Tool
Source: https://docs.crewai.com/en/tools/search-research/serpapi-googleshoppingtool

The `SerpApiGoogleShoppingTool` searches Google Shopping results using SerpApi.


# `SerpApiGoogleShoppingTool`


## Description

Leverage `SerpApiGoogleShoppingTool` to query Google Shopping via SerpApi and retrieve product-oriented results.


## Installation

```shell  theme={null}
uv add crewai-tools[serpapi]
```


## Environment Variables

* `SERPAPI_API_KEY` (required): API key for SerpApi. Create one at [https://serpapi.com/](https://serpapi.com/) (free tier available).


## Example

```python Code theme={null}
from crewai import Agent, Task, Crew
from crewai_tools import SerpApiGoogleShoppingTool

tool = SerpApiGoogleShoppingTool()

agent = Agent(
    role="Shopping Researcher",
    goal="Find relevant products",
    backstory="Expert in product search",
    tools=[tool],
    verbose=True,
)

task = Task(
    description="Search Google Shopping for 'wireless noise-canceling headphones'",
    expected_output="Top relevant products with titles and links",
    agent=agent,
)

crew = Crew(agents=[agent], tasks=[task])
result = crew.kickoff()
```


## Notes

* Set `SERPAPI_API_KEY` in the environment. Create a key at [https://serpapi.com/](https://serpapi.com/)
* See also Google Web Search via SerpApi: `/en/tools/search-research/serpapi-googlesearchtool`


## Parameters

### Run Parameters

* `search_query` (str, required): Product search query.
* `location` (str, optional): Geographic location parameter.



# Google Serper Search
Source: https://docs.crewai.com/en/tools/search-research/serperdevtool

The `SerperDevTool` is designed to search the internet and return the most relevant results.


# `SerperDevTool`


## Description

This tool is designed to perform a semantic search for a specified query from a text's content across the internet. It utilizes the [serper.dev](https://serper.dev) API
to fetch and display the most relevant search results based on the query provided by the user.


## Installation

To effectively use the `SerperDevTool`, follow these steps:

1. **Package Installation**: Confirm that the `crewai[tools]` package is installed in your Python environment.
2. **API Key Acquisition**: Acquire a `serper.dev` API key at [https://serper.dev/](https://serper.dev/) (free tier available).
3. **Environment Configuration**: Store your obtained API key in an environment variable named `SERPER_API_KEY` to facilitate its use by the tool.

To incorporate this tool into your project, follow the installation instructions below:

```shell  theme={null}
pip install 'crewai[tools]'
```


## Example

The following example demonstrates how to initialize the tool and execute a search with a given query:

```python Code theme={null}
from crewai_tools import SerperDevTool


# Initialize the tool for internet searching capabilities
tool = SerperDevTool()
```


## Parameters

The `SerperDevTool` comes with several parameters that will be passed to the API :

* **search\_url**: The URL endpoint for the search API. (Default is `https://google.serper.dev/search`)

* **country**: Optional. Specify the country for the search results.

* **location**: Optional. Specify the location for the search results.

* **locale**: Optional. Specify the locale for the search results.

* **n\_results**: Number of search results to return. Default is `10`.

The values for `country`, `location`, `locale` and `search_url` can be found on the [Serper Playground](https://serper.dev/playground).


## Example with Parameters

Here is an example demonstrating how to use the tool with additional parameters:

```python Code theme={null}
from crewai_tools import SerperDevTool

tool = SerperDevTool(
    search_url="https://google.serper.dev/scholar",
    n_results=2,
)

print(tool.run(search_query="ChatGPT"))


# Using Tool: Search the internet


# Search results: Title: Role of chat gpt in public health

# Link: https://link.springer.com/article/10.1007/s10439-023-03172-7

# Snippet: … ChatGPT in public health. In this overview, we will examine the potential uses of ChatGPT in

# ---

# Title: Potential use of chat gpt in global warming

# Link: https://link.springer.com/article/10.1007/s10439-023-03171-8

# Snippet: … as ChatGPT, have the potential to play a critical role in advancing our understanding of climate

# ---

```

```python Code theme={null}
from crewai_tools import SerperDevTool

tool = SerperDevTool(
    country="fr",
    locale="fr",
    location="Paris, Paris, Ile-de-France, France",
    n_results=2,
)

print(tool.run(search_query="Jeux Olympiques"))


# Using Tool: Search the internet


# Search results: Title: Jeux Olympiques de Paris 2024 - Actualités, calendriers, résultats

# Link: https://olympics.com/fr/paris-2024

# Snippet: Quels sont les sports présents aux Jeux Olympiques de Paris 2024 ? · Athlétisme · Aviron · Badminton · Basketball · Basketball 3x3 · Boxe · Breaking · Canoë ...

# ---

# Title: Billetterie Officielle de Paris 2024 - Jeux Olympiques et Paralympiques

# Link: https://tickets.paris2024.org/

# Snippet: Achetez vos billets exclusivement sur le site officiel de la billetterie de Paris 2024 pour participer au plus grand événement sportif au monde.

# ---
```


## Conclusion

By integrating the `SerperDevTool` into Python projects, users gain the ability to conduct real-time, relevant searches across the internet directly from their applications.
The updated parameters allow for more customized and localized search results. By adhering to the setup and usage guidelines provided, incorporating this tool into projects is streamlined and straightforward.



# Tavily Extractor Tool
Source: https://docs.crewai.com/en/tools/search-research/tavilyextractortool

Extract structured content from web pages using the Tavily API

The `TavilyExtractorTool` allows CrewAI agents to extract structured content from web pages using the Tavily API. It can process single URLs or lists of URLs and provides options for controlling the extraction depth and including images.


## Installation

To use the `TavilyExtractorTool`, you need to install the `tavily-python` library:

```shell  theme={null}
pip install 'crewai[tools]' tavily-python
```

You also need to set your Tavily API key as an environment variable:

```bash  theme={null}
export TAVILY_API_KEY='your-tavily-api-key'
```


## Example Usage

Here's how to initialize and use the `TavilyExtractorTool` within a CrewAI agent:

```python  theme={null}
import os
from crewai import Agent, Task, Crew
from crewai_tools import TavilyExtractorTool


# Ensure TAVILY_API_KEY is set in your environment

# os.environ["TAVILY_API_KEY"] = "YOUR_API_KEY"


# Initialize the tool
tavily_tool = TavilyExtractorTool()


# Create an agent that uses the tool
extractor_agent = Agent(
    role='Web Content Extractor',
    goal='Extract key information from specified web pages',
    backstory='You are an expert at extracting relevant content from websites using the Tavily API.',
    tools=[tavily_tool],
    verbose=True
)


# Define a task for the agent
extract_task = Task(
    description='Extract the main content from the URL https://example.com using basic extraction depth.',
    expected_output='A JSON string containing the extracted content from the URL.',
    agent=extractor_agent
)


# Create and run the crew
crew = Crew(
    agents=[extractor_agent],
    tasks=[extract_task],
    verbose=2
)

result = crew.kickoff()
print(result)
```


## Configuration Options

The `TavilyExtractorTool` accepts the following arguments:

* `urls` (Union\[List\[str], str]): **Required**. A single URL string or a list of URL strings to extract data from.
* `include_images` (Optional\[bool]): Whether to include images in the extraction results. Defaults to `False`.
* `extract_depth` (Literal\["basic", "advanced"]): The depth of extraction. Use `"basic"` for faster, surface-level extraction or `"advanced"` for more comprehensive extraction. Defaults to `"basic"`.
* `timeout` (int): The maximum time in seconds to wait for the extraction request to complete. Defaults to `60`.


## Advanced Usage

### Multiple URLs with Advanced Extraction

```python  theme={null}

# Example with multiple URLs and advanced extraction
multi_extract_task = Task(
    description='Extract content from https://example.com and https://anotherexample.org using advanced extraction.',
    expected_output='A JSON string containing the extracted content from both URLs.',
    agent=extractor_agent
)


# Configure the tool with custom parameters
custom_extractor = TavilyExtractorTool(
    extract_depth='advanced',
    include_images=True,
    timeout=120
)

agent_with_custom_tool = Agent(
    role="Advanced Content Extractor",
    goal="Extract comprehensive content with images",
    tools=[custom_extractor]
)
```

### Tool Parameters

You can customize the tool's behavior by setting parameters during initialization:

```python  theme={null}

# Initialize with custom configuration
extractor_tool = TavilyExtractorTool(
    extract_depth='advanced',  # More comprehensive extraction
    include_images=True,       # Include image results
    timeout=90                 # Custom timeout
)
```


## Features

* **Single or Multiple URLs**: Extract content from one URL or process multiple URLs in a single request
* **Configurable Depth**: Choose between basic (fast) and advanced (comprehensive) extraction modes
* **Image Support**: Optionally include images in the extraction results
* **Structured Output**: Returns well-formatted JSON containing the extracted content
* **Error Handling**: Robust handling of network timeouts and extraction errors


## Response Format

The tool returns a JSON string representing the structured data extracted from the provided URL(s). The exact structure depends on the content of the pages and the `extract_depth` used.

Common response elements include:

* **Title**: The page title
* **Content**: Main text content of the page
* **Images**: Image URLs and metadata (when `include_images=True`)
* **Metadata**: Additional page information like author, description, etc.


## Use Cases

* **Content Analysis**: Extract and analyze content from competitor websites
* **Research**: Gather structured data from multiple sources for analysis
* **Content Migration**: Extract content from existing websites for migration
* **Monitoring**: Regular extraction of content for change detection
* **Data Collection**: Systematic extraction of information from web sources

Refer to the [Tavily API documentation](https://docs.tavily.com/docs/tavily-api/python-sdk#extract) for detailed information about the response structure and available options.



# Tavily Search Tool
Source: https://docs.crewai.com/en/tools/search-research/tavilysearchtool

Perform comprehensive web searches using the Tavily Search API

The `TavilySearchTool` provides an interface to the Tavily Search API, enabling CrewAI agents to perform comprehensive web searches. It allows for specifying search depth, topics, time ranges, included/excluded domains, and whether to include direct answers, raw content, or images in the results.


## Installation

To use the `TavilySearchTool`, you need to install the `tavily-python` library:

```shell  theme={null}
pip install 'crewai[tools]' tavily-python
```


## Environment Variables

Ensure your Tavily API key is set as an environment variable:

```bash  theme={null}
export TAVILY_API_KEY='your_tavily_api_key'
```

Get an API key at [https://app.tavily.com/](https://app.tavily.com/) (sign up, then create a key).


## Example Usage

Here's how to initialize and use the `TavilySearchTool` within a CrewAI agent:

```python  theme={null}
import os
from crewai import Agent, Task, Crew
from crewai_tools import TavilySearchTool


# Ensure the TAVILY_API_KEY environment variable is set

# os.environ["TAVILY_API_KEY"] = "YOUR_TAVILY_API_KEY"


# Initialize the tool
tavily_tool = TavilySearchTool()


# Create an agent that uses the tool
researcher = Agent(
    role='Market Researcher',
    goal='Find information about the latest AI trends',
    backstory='An expert market researcher specializing in technology.',
    tools=[tavily_tool],
    verbose=True
)


# Create a task for the agent
research_task = Task(
    description='Search for the top 3 AI trends in 2024.',
    expected_output='A JSON report summarizing the top 3 AI trends found.',
    agent=researcher
)


# Form the crew and kick it off
crew = Crew(
    agents=[researcher],
    tasks=[research_task],
    verbose=2
)

result = crew.kickoff()
print(result)
```


## Configuration Options

The `TavilySearchTool` accepts the following arguments during initialization or when calling the `run` method:

* `query` (str): **Required**. The search query string.
* `search_depth` (Literal\["basic", "advanced"], optional): The depth of the search. Defaults to `"basic"`.
* `topic` (Literal\["general", "news", "finance"], optional): The topic to focus the search on. Defaults to `"general"`.
* `time_range` (Literal\["day", "week", "month", "year"], optional): The time range for the search. Defaults to `None`.
* `days` (int, optional): The number of days to search back. Relevant if `time_range` is not set. Defaults to `7`.
* `max_results` (int, optional): The maximum number of search results to return. Defaults to `5`.
* `include_domains` (Sequence\[str], optional): A list of domains to prioritize in the search. Defaults to `None`.
* `exclude_domains` (Sequence\[str], optional): A list of domains to exclude from the search. Defaults to `None`.
* `include_answer` (Union\[bool, Literal\["basic", "advanced"]], optional): Whether to include a direct answer synthesized from the search results. Defaults to `False`.
* `include_raw_content` (bool, optional): Whether to include the raw HTML content of the searched pages. Defaults to `False`.
* `include_images` (bool, optional): Whether to include image results. Defaults to `False`.
* `timeout` (int, optional): The request timeout in seconds. Defaults to `60`.


## Advanced Usage

You can configure the tool with custom parameters:

```python  theme={null}

# Example: Initialize with specific parameters
custom_tavily_tool = TavilySearchTool(
    search_depth='advanced',
    max_results=10,
    include_answer=True
)


# The agent will use these defaults
agent_with_custom_tool = Agent(
    role="Advanced Researcher",
    goal="Conduct detailed research with comprehensive results",
    tools=[custom_tavily_tool]
)
```


## Features

* **Comprehensive Search**: Access to Tavily's powerful search index
* **Configurable Depth**: Choose between basic and advanced search modes
* **Topic Filtering**: Focus searches on general, news, or finance topics
* **Time Range Control**: Limit results to specific time periods
* **Domain Control**: Include or exclude specific domains
* **Direct Answers**: Get synthesized answers from search results
* **Content Filtering**: Prevent context window issues with automatic content truncation


## Response Format

The tool returns search results as a JSON string containing:

* Search results with titles, URLs, and content snippets
* Optional direct answers to queries
* Optional image results
* Optional raw HTML content (when enabled)

Content for each result is automatically truncated to prevent context window issues while maintaining the most relevant information.



---

**Navigation:** [← Previous](./04-mastering-flow-state-management.md) | [Index](./index.md) | [Next →](./06-website-rag-search.md)
