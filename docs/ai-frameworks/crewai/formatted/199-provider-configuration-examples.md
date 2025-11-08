---
title: "Crewai: Provider Configuration Examples"
description: "Provider Configuration Examples section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

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

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Setting up your LLM](./198-setting-up-your-llm.md)

**Next:** [Streaming Responses →](./200-streaming-responses.md)
