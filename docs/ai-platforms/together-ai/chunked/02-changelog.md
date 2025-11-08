**Navigation:** [← Previous](./01-create-gpu-cluster.md) | [Index](./index.md) | [Next →](./03-deploying-a-fine-tuned-model.md)

---

# Changelog
Source: https://docs.together.ai/docs/changelog



## November, 2025

<Update label="Nov 3" description="/audio/speech, /audio/transcriptions">
  **Enhanced Audio Capabilities: Real-time Text-to-Speech and Speech-to-Text**

  Together AI expands audio capabilities with real-time streaming for both TTS and STT, new models, and speaker diarization.

  * **Real-time Text-to-Speech**: WebSocket API for lowest-latency interactive applications
  * **New TTS Models**: Orpheus 3B (`canopylabs/orpheus-3b-0.1-ft`) and Kokoro 82M (`hexgrad/Kokoro-82M`) supporting REST, streaming, and WebSocket endpoints
  * **Real-time Speech-to-Text**: WebSocket streaming transcription with Whisper for live audio applications
  * **Voxtral Model**: New Mistral AI speech recognition model (`mistralai/Voxtral-Mini-3B-2507`) for audio transcriptions
  * **Speaker Diarization**: Identify and label different speakers in audio transcriptions with a free `diarize` flag
  * TTS WebSocket endpoint: `/v1/audio/speech/websocket`
  * STT WebSocket endpoint: `/v1/realtime`
  * Check out the [Text-to-Speech guide](/docs/text-to-speech) and [Speech-to-Text guide](/docs/speech-to-text)
</Update>

## October, 2025

<Update label="Oct 31" description="/images">
  **Model Deprecations**

  The following image models have been deprecated and are no longer available:

  * `black-forest-labs/FLUX.1-pro` (Calls to FLUX.1-pro will now redirect to FLUX.1.1-pro)
  * `black-forest-labs/FLUX.1-Canny-pro`
</Update>

<Update label="Oct 21" description="/videos, /images">
  **Video Generation API & 40+ New Image and Video Models**

  Together AI expands into multimedia generation with comprehensive video and image capabilities. [Read more](https://www.together.ai/blog/40-new-image-and-video-models)

  * **New Video Generation API**: Create high-quality videos with models like OpenAI Sora 2, Google Veo 3.0, and Minimax Hailuo
  * **40+ Image & Video Models**: Including Google Imagen 4.0 Ultra, Gemini Flash Image 2.5 (Nano Banana), ByteDance SeeDream, and specialized editing tools
  * **Unified Platform**: Combine text, image, and video generation through the same APIs, authentication, and billing
  * **Production-Ready**: Serverless endpoints with transparent per-model pricing and enterprise-grade infrastructure
  * Video endpoints: `/videos/create` and `/videos/retrieve`
  * Image endpoint: `/images/generations`
</Update>

## September, 2025

<Update label="Sep 15" description="/batch_api">
  **Improved Batch Inference API: Enhanced UI, Expanded Model Support, and Rate Limit Increase**

  What’s New

  * Streamlined UI: Create and track batch jobs in an intuitive interface — no complex API calls required.
  * Universal Model Access: The Batch Inference API now supports all serverless models and private deployments, so you can run batch workloads on exactly the models you need.
  * Massive Scale Jump: Rate limits are up from 10M to 30B enqueued tokens per model per user, a 3000× increase. Need more? We’ll work with you to customize.
  * Lower Cost: For most serverless models, the Batch Inference API runs at 50% the cost of our real-time API, making it the most economical way to process high-throughput workloads.
</Update>

<Update label="Sep 13" description="/chat/completions">
  **Qwen3-Next-80B Models Release**

  New Qwen3-Next-80B models now available for both thinking and instruction tasks.

  * Model ID: `Qwen/Qwen3-Next-80B-A3B-Thinking`
  * Model ID: `Qwen/Qwen3-Next-80B-A3B-Instruct`
</Update>

<Update label="Sep 10" description="/fine-tunes">
  **Fine-Tuning Platform Upgrades**

  Enhanced fine-tuning capabilities with expanded model support and increased context lengths. [Read more](https://www.together.ai/blog/fine-tuning-updates-sept-2025)

  **Enable fine-tuning for new large models:**

  * `openai/gpt-oss-120b`
  * `deepseek-ai/DeepSeek-V3.1`
  * `deepseek-ai/DeepSeek-V3.1-Base`
  * `deepseek-ai/DeepSeek-R1-0528`
  * `deepseek-ai/DeepSeek-R1`
  * `deepseek-ai/DeepSeek-V3-0324`
  * `deepseek-ai/DeepSeek-V3`
  * `deepseek-ai/DeepSeek-V3-Base`
  * `Qwen/Qwen3-Coder-480B-A35B-Instruct`
  * `Qwen/Qwen3-235B-A22B` (context length 32,768 for SFT and 16,384 for DPO)
  * `Qwen/Qwen3-235B-A22B-Instruct-2507` (context length 32,768 for SFT and 16,384 for DPO)
  * `meta-llama/Llama-4-Maverick-17B-128E`
  * `meta-llama/Llama-4-Maverick-17B-128E-Instruct`
  * `meta-llama/Llama-4-Scout-17B-16E`
  * `meta-llama/Llama-4-Scout-17B-16E-Instruct`

  ***

  **Increased maximum supported context length (per model and variant):**

  **DeepSeek Models**

  * DeepSeek-R1-Distill-Llama-70B: SFT: 8192 → 24,576, DPO: 8192 → 8192
  * DeepSeek-R1-Distill-Qwen-14B: SFT: 8192 → 65,536, DPO: 8192 → 12,288
  * DeepSeek-R1-Distill-Qwen-1.5B: SFT: 8192 → 131,072, DPO: 8192 → 16,384

  **Google Gemma Models**

  * gemma-3-1b-it: SFT: 16,384 → 32,768, DPO: 16,384 → 12,288
  * gemma-3-1b-pt: SFT: 16,384 → 32,768, DPO: 16,384 → 12,288
  * gemma-3-4b-it: SFT: 16,384 → 131,072, DPO: 16,384 → 12,288
  * gemma-3-4b-pt: SFT: 16,384 → 131,072, DPO: 16,384 → 12,288
  * gemma-3-12b-pt: SFT: 16,384 → 65,536, DPO: 16,384 → 8,192
  * gemma-3-27b-it: SFT: 12,288 → 49,152, DPO: 12,288 → 8,192
  * gemma-3-27b-pt: SFT: 12,288 → 49,152, DPO: 12,288 → 8,192

  **Qwen Models**

  * Qwen3-0.6B / Qwen3-0.6B-Base: SFT: 8192 → 32,768, DPO: 8192 → 24,576
  * Qwen3-1.7B / Qwen3-1.7B-Base: SFT: 8192 → 32,768, DPO: 8192 → 16,384
  * Qwen3-4B / Qwen3-4B-Base: SFT: 8192 → 32,768, DPO: 8192 → 16,384
  * Qwen3-8B / Qwen3-8B-Base: SFT: 8192 → 32,768, DPO: 8192 → 16,384
  * Qwen3-14B / Qwen3-14B-Base: SFT: 8192 → 32,768, DPO: 8192 → 16,384
  * Qwen3-32B: SFT: 8192 → 24,576, DPO: 8192 → 4096
  * Qwen2.5-72B-Instruct: SFT: 8192 → 24,576, DPO: 8192 → 8192
  * Qwen2.5-32B-Instruct: SFT: 8192 → 32,768, DPO: 8192 → 12,288
  * Qwen2.5-32B: SFT: 8192 → 49,152, DPO: 8192 → 12,288
  * Qwen2.5-14B-Instruct: SFT: 8192 → 32,768, DPO: 8192 → 16,384
  * Qwen2.5-14B: SFT: 8192 → 65,536, DPO: 8192 → 16,384
  * Qwen2.5-7B-Instruct: SFT: 8192 → 32,768, DPO: 8192 → 16,384
  * Qwen2.5-7B: SFT: 8192 → 131,072, DPO: 8192 → 16,384
  * Qwen2.5-3B-Instruct: SFT: 8192 → 32,768, DPO: 8192 → 16,384
  * Qwen2.5-3B: SFT: 8192 → 32,768, DPO: 8192 → 16,384
  * Qwen2.5-1.5B-Instruct: SFT: 8192 → 32,768, DPO: 8192 → 16,384
  * Qwen2.5-1.5B: SFT: 8192 → 32,768, DPO: 8192 → 16,384
  * Qwen2-72B-Instruct / Qwen2-72B: SFT: 8192 → 32,768, DPO: 8192 → 8192
  * Qwen2-7B-Instruct: SFT: 8192 → 32,768, DPO: 8192 → 16,384
  * Qwen2-7B: SFT: 8192 → 131,072, DPO: 8192 → 16,384
  * Qwen2-1.5B-Instruct: SFT: 8192 → 32,768, DPO: 8192 → 16,384
  * Qwen2-1.5B: SFT: 8192 → 131,072, DPO: 8192 → 16,384

  **Meta Llama Models**

  * Llama-3.3-70B-Instruct-Reference: SFT: 8,192 → 24,576, DPO: 8,192 → 8,192
  * Llama-3.2-3B-Instruct: SFT: 8,192 → 131,072, DPO: 8,192 → 24,576
  * Llama-3.2-1B-Instruct: SFT: 8,192 → 131,072, DPO: 8,192 → 24,576
  * Meta-Llama-3.1-8B-Instruct-Reference: SFT: 8,192 → 131,072, DPO: 8,192 → 16,384
  * Meta-Llama-3.1-8B-Reference: SFT: 8,192 → 131,072, DPO: 8,192 → 16,384
  * Meta-Llama-3.1-70B-Instruct-Reference: SFT: 8,192 → 24,576, DPO: 8,192 → 8,192
  * Meta-Llama-3.1-70B-Reference: SFT: 8,192 → 24,576, DPO: 8,192 → 8,192

  **Mistral Models**

  * mistralai/Mistral-7B-v0.1: SFT: 8,192 → 32,768, DPO: 8,192 → 32,768
  * teknium/OpenHermes-2p5-Mistral-7B: SFT: 8,192 → 32,768, DPO: 8,192 → 32,768

  ***

  **Enhanced Hugging Face integrations:**

  * Fine-tune any \< 100B parameter CausalLM from Hugging Face Hub
  * Support for DPO variants such as LN-DPO, DPO+NLL, and SimPO
  * Support fine-tuning with maximum batch size
  * Public `fine-tunes/models/limits` and `fine-tunes/models/supported` endpoints
  * Automatic filtering of sequences with no trainable tokens (e.g., if a sequence prompt is longer than the model's context length, the completion is pushed outside the window)
</Update>

<Update label="Sep 9" description="/gpu_cluster">
  **Together Instant Clusters General Availability**

  Self-service NVIDIA GPU clusters with API-first provisioning. [Read more](https://www.together.ai/blog/together-instant-clusters-ga)

  * New API endpoints for cluster management:
    * `/v1/gpu_cluster` - Create and manage GPU clusters
    * `/v1/shared_volume` - High-performance shared storage
    * `/v1/regions` - Available data center locations
  * Support for NVIDIA Blackwell (HGX B200) and Hopper (H100, H200) GPUs
  * Scale from single-node (8 GPUs) to hundreds of interconnected GPUs
  * Pre-configured with Kubernetes, Slurm, and networking components
</Update>

<Update label="Sep 8" description="/evaluation">
  **Serverless LoRA and Dedicated Endpoints support for Evaluations**

  You can now run evaluations:

  * Using [Serverless LoRA](docs/lora-inference#serverless-lora-inference) models, including supported LoRA fine-tuned models
  * Using [Dedicated Endpoints](docs/dedicated-endpoints-1), including fine-tuned models deployed via dedicated endpoints
</Update>

<Update label="Sep 5" description="/chat/completions">
  **Kimi-K2-Instruct-0905 Model Release**

  Upgraded version of Moonshot's 1 trillion parameter MoE model with enhanced performance. [Read more](https://www.together.ai/models/kimi-k2-0905)

  * Model ID: `moonshot-ai/Kimi-K2-Instruct-0905`
</Update>

## August, 2025

<Update label="Aug 27" description="/chat/completions">
  **DeepSeek-V3.1 Model Release**

  Upgraded version of DeepSeek-R1-0528 and DeepSeek-V3-0324. [Read more](https://www.together.ai/blog/deepseek-v3-1-hybrid-thinking-model-now-available-on-together-ai)

  * **Dual Modes**: Fast mode for quick responses, thinking mode for complex reasoning
  * **671B total parameters** with 37B active parameters
  * Model ID: `deepseek-ai/DeepSeek-V3.1`

  ***

  **Model Deprecations**

  The following models have been deprecated and are no longer available:

  * `meta-llama/Llama-3.2-90B-Vision-Instruct-Turbo`
  * `black-forest-labs/FLUX.1-canny`
  * `meta-llama/Llama-3-8b-chat-hf`
  * `black-forest-labs/FLUX.1-redux`
  * `black-forest-labs/FLUX.1-depth`
  * `deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B`
  * `NousResearch/Nous-Hermes-2-Mixtral-8x7B-DPO`
  * `meta-llama/Llama-3.2-11B-Vision-Instruct-Turbo`
  * `meta-llama-llama-3-3-70b-instruct-lora`
  * `Qwen/Qwen2.5-14B`
  * `meta-llama/Llama-Vision-Free`
  * `Qwen/Qwen2-72B-Instruct`
  * `google/gemma-2-27b-it`
  * `meta-llama/Meta-Llama-3-8B-Instruct`
  * `perplexity-ai/r1-1776`
  * `nvidia/Llama-3.1-Nemotron-70B-Instruct-HF`
  * `Qwen/Qwen2-VL-72B-Instruct`
</Update>

<Update label="Aug 19" description="/fine-tunes">
  **GPT-OSS Models Fine-Tuning Support**

  Fine-tune OpenAI's open-source models to create domain-specific variants. [Read more](https://www.together.ai/blog/fine-tune-gpt-oss-models-into-domain-experts-together-ai)

  * Supported models: `gpt-oss-20B` and `gpt-oss-120B`
  * Supports 16K context SFT, 8k context DPO
</Update>

<Update label="Aug 5" description="/chat/completions">
  **OpenAI GPT-OSS Models Now Available**

  OpenAI's first open-weight models now accessible through Together AI. [Read more](https://www.together.ai/blog/announcing-the-availability-of-openais-open-models-on-together-ai)

  * Model IDs: `openai/gpt-oss-20b`, `openai/gpt-oss-120b`
</Update>

## July, 2025

<Update label="Jul 29" description="/chat/completions">
  **VirtueGuard Model Release**

  Enterprise-grade gaurd model for safety monitoring with **8ms response time**. [Read more](https://www.together.ai/blog/virtueguard)

  * Real-time content filtering and bias detection
  * Prompt injection protection
  * Model ID: `VirtueAI/VirtueGuard-Text-Lite`
</Update>

<Update label="Jul 28" description="/evaluation">
  **Together Evaluations Framework**

  Benchmarking platform using **LLM-as-a-judge methodology** for model performance assessment. [Read more](https://www.together.ai/blog/introducing-together-evaluations)

  * Create custom LLM-as-a-Judge evaluation suites for your domain
  * Support `compare`, `classify` and `score` functionality
  * Enables comparing models, prompts and LLM configs, scoring and classifying LLM outputs
</Update>

<Update label="Jul 25" description="/chat/completions">
  **Qwen3-Coder-480B Model Release**

  Agentic coding model with top SWE-Bench Verified performance. [Read more](https://www.together.ai/blog/qwen-3-coder)

  * **480B total parameters** with 35B active (MoE architecture)
  * **256K context length** for entire codebase handling
  * **Leading SWE-Bench scores** on software engineering benchmarks
  * Model ID: `Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8`
</Update>

<Update label="Jul 17" description="/chat/completions">
  **NVIDIA HGX B200 Hardware Support**

  **Record-breaking serverless inference speed** for DeepSeek-R1-0528 using NVIDIA's Blackwell architecture. [Read more](https://www.together.ai/blog/fastest-inference-for-deepseek-r1-0528-with-nvidia-hgx-b200)

  * Dramatically improved throughput and lower latency
  * Same API endpoints and pricing
  * Model ID: `deepseek-ai/DeepSeek-R1`
</Update>

<Update label="Jul 14" description="/chat/completions">
  **Kimi-K2-Instruct Model Launch**

  Moonshot AI's **1 trillion parameter MoE model** with frontier-level performance. [Read more](https://www.together.ai/blog/kimi-k2-leading-open-source-model-now-available-on-together-ai)

  * Excels at tool use, and multi-step tasks and strong multilingual support
  * Great agentic and function calling capabilities
  * Model ID: `moonshotai/Kimi-K2-Instruct`
</Update>

<Update label="Jul 10" description="/audio/transcriptions">
  **Whisper Speech-to-Text APIs**

  High-performance audio transcription that's **15× faster than OpenAI** with support for **files over 1 GB**. [Read more](https://www.together.ai/blog/speech-to-text-whisper-apis)

  * Multiple audio formats with timestamp generation
  * Speaker diarization and language detection
  * Use `/audio/transcriptions` and `/audio/translations` endpoint
  * Model ID: `openai/whisper-large-v3`
</Update>

<Update label="Jul 8" description="Compliance">
  **SOC 2 Type II Compliance Certification**

  Achieved enterprise-grade security compliance through independent audit of security controls. [Read more](https://www.together.ai/blog/soc-2-compliance)

  * Simplified vendor approval and procurement
  * Reduced due diligence requirements
  * Support for regulated industries
</Update>


# Chat
Source: https://docs.together.ai/docs/chat-overview

Learn how to query our open-source chat models.

## Playground

The Playground is a web application offered by Together AI to allow our customers to run inference without having to use our API. The playground can be used with standard models, or a selection of fine-tuned models.

You can access the Playground at [api.together.xyz/playground](https://api.together.xyz/playground).

## API Usage

You can use Together's APIs to send individual queries or have long-running conversations with chat models. You can also configure a system prompt to customize how a model should respond.

Queries run against a model of your choice. For most use cases, we recommend using Meta Llama 3.

## Running a single query

Use `chat.completions.create` to send a single query to a chat model:

<CodeGroup>
  ```python Python theme={null}
  from together import Together

  client = Together()

  response = client.chat.completions.create(
      model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
      messages=[
          {
              "role": "user",
              "content": "What are some fun things to do in New York?",
          }
      ],
  )

  print(response.choices[0].message.content)
  ```

  ```typescript TypeScript theme={null}
  import Together from "together-ai";

  const together = new Together();

  const response = await together.chat.completions.create({
    model: "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
    messages: [{ role: "user", content: "What are some fun things to do in New York?" }],
  });

  console.log(response.choices[0].message.content)
  ```

  ```shell HTTP theme={null}
  curl -X POST "https://api.together.xyz/v1/chat/completions" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -H "Content-Type: application/json" \
       -d '{
       	"model": "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
       	"messages": [
       		{"role": "user", "content": "What are some fun things to do in New York?"}
       	]
       }'
  ```
</CodeGroup>

The `create` method takes in a model name and a `messages` array. Each `message` is an object that has the content of the query, as well as a role for the message's author.

In the example above, you can see that we're using "user" for the role. The "user" role tells the model that this message comes from the end user of our system – for example, a customer using your chatbot app.

The other two roles are "assistant" and "system", which we'll talk about next.

## Having a long-running conversation

Every query to a chat model is self-contained. This means that new queries won't automatically have access to any queries that may have come before them. This is exactly why the "assistant" role exists.

The "assistant" role is used to provide historical context for how a model has responded to prior queries. This makes it perfect for building apps that have long-running conversations, like chatbots.

To provide a chat history for a new query, pass the previous messages to the `messages` array, denoting the user-provided queries with the "user" role, and the model's responses with the "assistant" role:

<CodeGroup>
  ```python Python theme={null}
  import os
  from together import Together

  client = Together()

  response = client.chat.completions.create(
      model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
      messages=[
          {
              "role": "user",
              "content": "What are some fun things to do in New York?",
          },
          {
              "role": "assistant",
              "content": "You could go to the Empire State Building!",
          },
          {"role": "user", "content": "That sounds fun! Where is it?"},
      ],
  )

  print(response.choices[0].message.content)
  ```

  ```typescript TypeScript theme={null}
  import Together from "together-ai";

  const together = new Together();

  const response = await together.chat.completions.create({
    model: "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
    messages: [
      { role: "user", content: "What are some fun things to do in New York?" },
      { role: "assistant", content: "You could go to the Empire State Building!"},
      { role: "user", content: "That sounds fun! Where is it?" },
    ],
  });

  console.log(response.choices[0].message.content);
  ```

  ```shell HTTP theme={null}
  curl -X POST "https://api.together.xyz/v1/chat/completions" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -H "Content-Type: application/json" \
       -d '{
       	"model": "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
       	"messages": [
          {"role": "user", "content": "What are some fun things to do in New York?"},
          {"role": "assistant", "content": "You could go to the Empire State Building!"},
          {"role": "user", "content": "That sounds fun! Where is it?" }
       	]
       }'
  ```
</CodeGroup>

How your app stores historical messages is up to you.

## Customizing how the model responds

While you can query a model just by providing a user message, typically you'll want to give your model some context for how you'd like it to respond. For example, if you're building a chatbot to help your customers with travel plans, you might want to tell your model that it should act like a helpful travel guide.

To do this, provide an initial message that uses the "system" role:

<CodeGroup>
  ```python Python theme={null}
  import os
  from together import Together

  client = Together()

  response = client.chat.completions.create(
      model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
      messages=[
          {"role": "system", "content": "You are a helpful travel guide."},
          {
              "role": "user",
              "content": "What are some fun things to do in New York?",
          },
      ],
  )

  print(response.choices[0].message.content)
  ```

  ```typescript TypeScript theme={null}
  import Together from "together-ai";

  const together = new Together();

  const response = await together.chat.completions.create({
    model: "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
    messages: [
      {"role": "system", "content": "You are a helpful travel guide."},
      { role: "user", content: "What are some fun things to do in New York?" },
    ],
  });

  console.log(response.choices[0].message.content);
  ```

  ```shell HTTP theme={null}
  curl -X POST "https://api.together.xyz/v1/chat/completions" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -H "Content-Type: application/json" \
       -d '{
       	"model": "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
       	"messages": [
       		{"role": "system", "content": "You are a helpful travel guide."},
       		{"role": "user", "content": "What are some fun things to do in New York?"}
       	]
       }'
  ```
</CodeGroup>

## Streaming responses

Since models can take some time to respond to a query, Together's APIs support streaming back responses in chunks. This lets you display results from each chunk while the model is still running, instead of having to wait for the entire response to finish.

To return a stream, set the `stream` option to true.

<CodeGroup>
  ```python Python theme={null}
  import os
  from together import Together

  client = Together()

  stream = client.chat.completions.create(
      model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
      messages=[
          {
              "role": "user",
              "content": "What are some fun things to do in New York?",
          }
      ],
      stream=True,
  )

  for chunk in stream:
      print(chunk.choices[0].delta.content or "", end="", flush=True)
  ```

  ```typescript TypeScript theme={null}
  import Together from 'together-ai';

  const together = new Together();

  const stream = await together.chat.completions.create({
    model: 'meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo',
    messages: [
      { role: 'user', content: 'What are some fun things to do in New York?' },
    ],
    stream: true,
  });

  for await (const chunk of stream) {
    process.stdout.write(chunk.choices[0]?.delta?.content || '');
  }
  ```

  ```shell HTTP theme={null}
  curl -X POST "https://api.together.xyz/v1/chat/completions" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -H "Content-Type: application/json" \
       -d '{
       	"model": "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
       	"messages": [
       		{"role": "user", "content": "What are some fun things to do in New York?"}
       	],
        "stream": true
       }'
       
  ## Response will be a stream of Server-Sent Events with JSON-encoded payloads. For example:
  ## 
  ## data: {"choices":[{"index":0,"delta":{"content":" A"}}],"id":"85ffbb8a6d2c4340-EWR","token":{"id":330,"text":" A","logprob":1,"special":false},"finish_reason":null,"generated_text":null,"stats":null,"usage":null,"created":1709700707,"object":"chat.completion.chunk"}
  ## data: {"choices":[{"index":0,"delta":{"content":":"}}],"id":"85ffbb8a6d2c4340-EWR","token":{"id":28747,"text":":","logprob":0,"special":false},"finish_reason":null,"generated_text":null,"stats":null,"usage":null,"created":1709700707,"object":"chat.completion.chunk"}
  ## data: {"choices":[{"index":0,"delta":{"content":" Sure"}}],"id":"85ffbb8a6d2c4340-EWR","token":{"id":12875,"text":" Sure","logprob":-0.00724411,"special":false},"finish_reason":null,"generated_text":null,"stats":null,"usage":null,"created":1709700707,"object":"chat.completion.chunk"}
  ```
</CodeGroup>

## A note on async support in Python

Since I/O in Python is synchronous, multiple queries will execute one after another in sequence, even if they are independent.

If you have multiple independent calls that you want to run in parallel, you can use our Python library's `AsyncTogether` module:

```python Python theme={null}
import os, asyncio
from together import AsyncTogether

async_client = AsyncTogether()
messages = [
    "What are the top things to do in San Francisco?",
    "What country is Paris in?",
]


async def async_chat_completion(messages):
    async_client = AsyncTogether(api_key=os.environ.get("TOGETHER_API_KEY"))
    tasks = [
        async_client.chat.completions.create(
            model="mistralai/Mixtral-8x7B-Instruct-v0.1",
            messages=[{"role": "user", "content": message}],
        )
        for message in messages
    ]
    responses = await asyncio.gather(*tasks)

    for response in responses:
        print(response.choices[0].message.content)


asyncio.run(async_chat_completion(messages))
```


# Cluster Storage
Source: https://docs.together.ai/docs/cluster-storage



A Together GPU Cluster has 3 types of storage:

### 1. Local disks

Each server has NVME drives which can be used for high speed local read/writes.

### 2. Shared `/home` folder

The `/home` folder is shared across all nodes, mounted as an NFS volume from the head node. This should be used for code, configs, logs, etc. It should not be used for training data or checkpointing, as it is slower.

We recommend logging into the Slurm head node first to properly set up your user folder with the right permissions.

### 3. Shared remote attached storage

The GPU nodes all have a mounted volume from a high-speed storage cluster, which is useful for reading training data and writing checkpoints to/from a central location.


# Cluster User Management
Source: https://docs.together.ai/docs/cluster-user-management



Prior to adding any user to your cluster, please make sure the user has created an account and added an SSH key in the [Together Playground](https://api.together.xyz/playground/). Users can add an SSH key [here](https://api.together.xyz/settings/ssh-key). For more information, please see [Quickstart](/docs/quickstart).

To add users to your cluster, please follow these steps:

Log in to your Together AI account. In the circle in the right hand corner, click into your avatar and select “Settings” from the drop down menu.

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/7039280-Screenshot_2024-06-17_at_3.50.42_PM.png?fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=1218ead38bd916cf9f16cc5a97352edc" alt="" data-og-width="3130" width="3130" data-og-height="562" height="562" data-path="images/7039280-Screenshot_2024-06-17_at_3.50.42_PM.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/7039280-Screenshot_2024-06-17_at_3.50.42_PM.png?w=280&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=623c193a61ff6a32166c1629e14263b0 280w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/7039280-Screenshot_2024-06-17_at_3.50.42_PM.png?w=560&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=a76f1b6dbd8dd7dd94f7f4827f563e86 560w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/7039280-Screenshot_2024-06-17_at_3.50.42_PM.png?w=840&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=c05030df32fa434826140fb49c2fa73e 840w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/7039280-Screenshot_2024-06-17_at_3.50.42_PM.png?w=1100&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=9420b9754716462d3505e20cfb569748 1100w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/7039280-Screenshot_2024-06-17_at_3.50.42_PM.png?w=1650&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=b4f596fb2e23574a8a807f76fcbcdc66 1650w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/7039280-Screenshot_2024-06-17_at_3.50.42_PM.png?w=2500&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=6093eafde65f00d4ae3cbdf911f3e523 2500w" />
</Frame>

On the left hand side, select Members.

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/df1e4dc-Screenshot_2024-06-17_at_3.52.04_PM.png?fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=3268f95f68606b97dab53677ce192985" alt="" data-og-width="560" width="560" data-og-height="1362" height="1362" data-path="images/df1e4dc-Screenshot_2024-06-17_at_3.52.04_PM.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/df1e4dc-Screenshot_2024-06-17_at_3.52.04_PM.png?w=280&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=8a64872993a9ac2ec23c01c0ffc739c1 280w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/df1e4dc-Screenshot_2024-06-17_at_3.52.04_PM.png?w=560&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=0c87acb80355de45d1a8f276670364a0 560w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/df1e4dc-Screenshot_2024-06-17_at_3.52.04_PM.png?w=840&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=69277c43899798c9fc704433e00cbd34 840w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/df1e4dc-Screenshot_2024-06-17_at_3.52.04_PM.png?w=1100&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=ec4a76dcd8784454dd354003d9b04ae5 1100w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/df1e4dc-Screenshot_2024-06-17_at_3.52.04_PM.png?w=1650&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=f3bfbd1b85ab9572a022654b85abdf7b 1650w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/df1e4dc-Screenshot_2024-06-17_at_3.52.04_PM.png?w=2500&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=ecc4ed5f7fc7a3616a54a60089f88d1c 2500w" />
</Frame>

At the top of Members, select “Add User”.

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/c632c65-Screenshot_2024-06-17_at_3.54.41_PM.png?fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=6375254a262786e4e9644cf80114f567" alt="" data-og-width="2552" width="2552" data-og-height="388" height="388" data-path="images/c632c65-Screenshot_2024-06-17_at_3.54.41_PM.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/c632c65-Screenshot_2024-06-17_at_3.54.41_PM.png?w=280&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=ad183719f4871c089350592619b68baa 280w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/c632c65-Screenshot_2024-06-17_at_3.54.41_PM.png?w=560&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=f80e6cfa47b14c0f673e0d9a8691487c 560w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/c632c65-Screenshot_2024-06-17_at_3.54.41_PM.png?w=840&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=8928b806fec063fbb7c52ed888913eed 840w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/c632c65-Screenshot_2024-06-17_at_3.54.41_PM.png?w=1100&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=ce21c20a82635da69ee6afa4c7cfd738 1100w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/c632c65-Screenshot_2024-06-17_at_3.54.41_PM.png?w=1650&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=a376bd9d882ed44e5574bcfef909e090 1650w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/c632c65-Screenshot_2024-06-17_at_3.54.41_PM.png?w=2500&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=5efd0f54b762d699a6c6ca78fbac2560 2500w" />
</Frame>

A popup will appear. In this popup, please enter the email of the user.

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/b141846-Screenshot_2024-06-17_at_3.55.26_PM.png?fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=59fadc91d3bf213aa0384ec587999e22" alt="" data-og-width="1120" width="1120" data-og-height="554" height="554" data-path="images/b141846-Screenshot_2024-06-17_at_3.55.26_PM.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/b141846-Screenshot_2024-06-17_at_3.55.26_PM.png?w=280&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=3371970a8f4c704b8b13d8c3421717bb 280w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/b141846-Screenshot_2024-06-17_at_3.55.26_PM.png?w=560&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=489f57dfc78bbf0571facda02ea24805 560w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/b141846-Screenshot_2024-06-17_at_3.55.26_PM.png?w=840&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=9b13641a8edaa69c43f26487b74a2fb4 840w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/b141846-Screenshot_2024-06-17_at_3.55.26_PM.png?w=1100&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=ac1c5c0b525683cec5b2924d31b8bfb1 1100w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/b141846-Screenshot_2024-06-17_at_3.55.26_PM.png?w=1650&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=90d2c2988bc818d9189917403c39a716 1650w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/b141846-Screenshot_2024-06-17_at_3.55.26_PM.png?w=2500&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=83223a3fc8025b84e314ef2d592cfd6c 2500w" />
</Frame>

If the user does not have an Playground account or SSH key, you will see an error indicating that the user cannot be added.

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/2545b20-Screenshot_2024-06-17_at_3.56.14_PM.png?fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=2e7d1fb192762f8296ba4fbe1dd321d4" alt="" data-og-width="1116" width="1116" data-og-height="604" height="604" data-path="images/2545b20-Screenshot_2024-06-17_at_3.56.14_PM.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/2545b20-Screenshot_2024-06-17_at_3.56.14_PM.png?w=280&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=fd38f9fca5a75c0a4f737d4023919154 280w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/2545b20-Screenshot_2024-06-17_at_3.56.14_PM.png?w=560&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=88c44f0aae349cb052ea5b90635b3805 560w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/2545b20-Screenshot_2024-06-17_at_3.56.14_PM.png?w=840&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=f6ab45b580aeb8966adfbf29e31b4ce3 840w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/2545b20-Screenshot_2024-06-17_at_3.56.14_PM.png?w=1100&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=0830e12c3f755bfcf9b231fc892718d9 1100w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/2545b20-Screenshot_2024-06-17_at_3.56.14_PM.png?w=1650&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=c74d2a52eb627e48c5a3ab1946d43dc7 1650w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/2545b20-Screenshot_2024-06-17_at_3.56.14_PM.png?w=2500&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=41830c3fd2e8e0f41f513c6aaa7abb8e 2500w" />
</Frame>

Once you click add user, the user will appear in the grid.

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/c17a715-Screenshot_2024-06-17_at_3.56.48_PM.png?fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=17502d18fa05c39ead64d32afd115e98" alt="" data-og-width="2444" width="2444" data-og-height="122" height="122" data-path="images/c17a715-Screenshot_2024-06-17_at_3.56.48_PM.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/c17a715-Screenshot_2024-06-17_at_3.56.48_PM.png?w=280&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=bb65d5a00b22f34caa5877207380faa8 280w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/c17a715-Screenshot_2024-06-17_at_3.56.48_PM.png?w=560&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=202d8a1c4494b7c0ba2a6b0fc426aebb 560w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/c17a715-Screenshot_2024-06-17_at_3.56.48_PM.png?w=840&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=b80049eacee77309cddab2d51b59b654 840w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/c17a715-Screenshot_2024-06-17_at_3.56.48_PM.png?w=1100&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=e711784d646aba28cc0213ae8db69640 1100w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/c17a715-Screenshot_2024-06-17_at_3.56.48_PM.png?w=1650&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=9680925e0333e37b08d6f0610797e6af 1650w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/c17a715-Screenshot_2024-06-17_at_3.56.48_PM.png?w=2500&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=cbdcc2a38219895161d6f1c0397f25fc 2500w" />
</Frame>

To remove this user, press the 3 dots on the right side and select “Remove user”.

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/6edcd0e-Screenshot_2024-06-17_at_3.57.34_PM.png?fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=484988edb7eb762456dfd36f30d8172b" alt="" data-og-width="2446" width="2446" data-og-height="192" height="192" data-path="images/6edcd0e-Screenshot_2024-06-17_at_3.57.34_PM.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/6edcd0e-Screenshot_2024-06-17_at_3.57.34_PM.png?w=280&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=d2b26a749d8c3a027f0c71d75a4c453b 280w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/6edcd0e-Screenshot_2024-06-17_at_3.57.34_PM.png?w=560&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=4068e5083677009537f8c7233520b09d 560w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/6edcd0e-Screenshot_2024-06-17_at_3.57.34_PM.png?w=840&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=4a8e35cef6e573472997fed0ed960ced 840w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/6edcd0e-Screenshot_2024-06-17_at_3.57.34_PM.png?w=1100&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=6ed90d4bdbf18e0b301204c3683145af 1100w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/6edcd0e-Screenshot_2024-06-17_at_3.57.34_PM.png?w=1650&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=95d4cf6ef8a4c8dda9365a4a43e5658e 1650w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/6edcd0e-Screenshot_2024-06-17_at_3.57.34_PM.png?w=2500&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=693255bd35620f8fc230d9008f844e90 2500w" />
</Frame>


# Composio
Source: https://docs.together.ai/docs/composio

Using Composio With Together AI

Composio allows developers to integrate external tools and services into their AI applications. It handles tool calling, web-hooks, authentication, and more.

You need to register on a Composio account - Sign up here if you haven't already to get their api key [https://platform.composio.dev/](https://platform.composio.dev/)

## Install Libraries

<CodeGroup>
  ```shell Python theme={null}
  pip install together composio-togetherai
  ```

  ```shell TypeScript theme={null}
  npm install @composio/core @composio/vercel @ai-sdk/togetherai ai
  ```
</CodeGroup>

Set your `TOGETHER_API_KEY` environment variable.

```sh Shell theme={null}
export TOGETHER_API_KEY=***
export COMPOSIO_API_KEY=***
```

## Example

In this example, we will use Together AI to star a repository on GitHub using Composio Tools.

<CodeGroup>
  ```python Python theme={null}
  from composio_togetherai import ComposioToolSet, App
  from together import Together

  client = Together()
  toolset = ComposioToolSet()
  ```

  ```typescript TypeScript theme={null}
  /*
  We use the Vercel AI SDK with the Together provider to 
  enable type checking to work correctly for tools and 
  to simplify the Composio integration. 
  This flow enables us to directly execute tool calls
  without having to use composio.provider.handleToolCalls.
  */

  import { Composio } from "@composio/core";
  import { VercelProvider } from "@composio/vercel";
  import { createTogetherAI } from "@ai-sdk/togetherai";
  import { generateText } from "ai";

  export const together = createTogetherAI({
    apiKey: process.env.TOGETHER_API_KEY ?? "",
  });

  const composio = new Composio({
    apiKey: process.env.COMPOSIO_API_KEY ?? "",
    provider: new VercelProvider(),
  });
  ```
</CodeGroup>

### Connect Your GitHub Account

You need to have an active GitHub Integration in Composio. Learn how to do this [here](https://www.youtube.com/watch?v=LmyWy4LiedQ)

<CodeGroup>
  ```py Python theme={null}
  request = toolset.initiate_connection(app=App.GITHUB)
  print(f"Open this URL to authenticate: {request.redirectUrl}")
  ```

  ```sh Shell theme={null}
  composio login
  composio add github
  ```
</CodeGroup>

### Get All Github Tools

You can get all the tools for a given app as shown below, but you can get specific actions and filter actions using usecase & tags.

<CodeGroup>
  ```python Python theme={null}
  tools = toolset.get_tools(apps=[App.GITHUB])
  ```

  ```typescript TypeScript theme={null}
  const userId = "default"; // replace with user id from composio
  const tools = await composio.tools.get(userId, {
    toolkits: ['github'],
  });
  ```
</CodeGroup>

### Create a Chat Completion with Tools

<CodeGroup>
  ```python Python theme={null}
  response = client.chat.completions.create(
      tools=tools,
      model="meta-llama/Llama-3.3-70B-Instruct-Turbo",
      messages=[
          {
              "role": "user",
              "content": "Star the repo 'togethercomputer/together-cookbook'",
          }
      ],
  )

  res = toolset.handle_tool_calls(response)
  print(res)
  ```

  ```typescript TypeScript theme={null}
  const responseGithub = await generateText({
      model: together("meta-llama/Llama-3.3-70B-Instruct-Turbo"),
      messages: [
        {
          role: "user",
          content: "Star the repo 'togethercomputer/together-cookbook'",
        },
      ],
      tools,
      toolChoice: "required",
  });

  console.log(responseGithub);
  ```
</CodeGroup>

## Next Steps

<Note>
  ### Composio - Together AI Cookbook

  Explore our in-depth [Composio Cookbook](https://github.com/togethercomputer/together-cookbook/blob/main/Agents/Composio/Agents_Composio.ipynb) to learn how to automate emails with LLMs.
</Note>


# Conditional Workflow
Source: https://docs.together.ai/docs/conditional-workflows

Adapt to different tasks by conditionally navigating to various LLMs and tools.

A workflow where user input is classified and directed to a specific task (can be a specific LLM, specific custom prompt, different tool calls etc.). This allows you to handle for many different inputs and handle them with the appropriate set of calls.

## Workflow Architecture

Create an agent that conditionally routes tasks to specialized models.

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/6f2307cf0a62498e41395cd0ce0a435a731e78ae8c07ae7e4596992b202e8c22-conditional.png?fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=8c0e9d6cb57612ddeb9e368a7984c3ce" alt="" data-og-width="3856" width="3856" data-og-height="1792" height="1792" data-path="images/6f2307cf0a62498e41395cd0ce0a435a731e78ae8c07ae7e4596992b202e8c22-conditional.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/6f2307cf0a62498e41395cd0ce0a435a731e78ae8c07ae7e4596992b202e8c22-conditional.png?w=280&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=44ef29058a3bc39dfa1a069f7cdc9c2d 280w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/6f2307cf0a62498e41395cd0ce0a435a731e78ae8c07ae7e4596992b202e8c22-conditional.png?w=560&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=f69056e2e220404e1248d4a7722ab163 560w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/6f2307cf0a62498e41395cd0ce0a435a731e78ae8c07ae7e4596992b202e8c22-conditional.png?w=840&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=d0caf5fe71290e67ae8759da738bd162 840w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/6f2307cf0a62498e41395cd0ce0a435a731e78ae8c07ae7e4596992b202e8c22-conditional.png?w=1100&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=596d41eb07bb193417ce4507ac3f0db4 1100w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/6f2307cf0a62498e41395cd0ce0a435a731e78ae8c07ae7e4596992b202e8c22-conditional.png?w=1650&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=2dbaae745a8d3ca05f65365bee41119b 1650w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/6f2307cf0a62498e41395cd0ce0a435a731e78ae8c07ae7e4596992b202e8c22-conditional.png?w=2500&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=d3c84cb8d21e7a13b18a31b2b9b90f27 2500w" />
</Frame>

## Setup Client & Helper Functions

```py Python theme={null}
import json
from pydantic import ValidationError
from together import Together

client = Together()


def run_llm(user_prompt: str, model: str, system_prompt: str = None):
    messages = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})

    messages.append({"role": "user", "content": user_prompt})

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.7,
        max_tokens=4000,
    )

    return response.choices[0].message.content


def JSON_llm(user_prompt: str, schema, system_prompt: str = None):
    try:
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})

        messages.append({"role": "user", "content": user_prompt})

        extract = client.chat.completions.create(
            messages=messages,
            model="meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo",
            response_format={
                "type": "json_object",
                "schema": schema.model_json_schema(),
            },
        )
        return json.loads(extract.choices[0].message.content)

    except ValidationError as e:
        error_message = f"Failed to parse JSON: {e}"
        print(error_message)
```

## Implement Workflow

<CodeGroup>
  ```py Python theme={null}
  from pydantic import BaseModel, Field
  from typing import Literal, Dict


  def router_workflow(input_query: str, routes: Dict[str, str]) -> str:
      """Given a `input_query` and a dictionary of `routes` containing options and details for each.
      Selects the best model for the task and return the response from the model.
      """
      ROUTER_PROMPT = """Given a user prompt/query: {user_query}, select the best option out of the following routes:
      {routes}. Answer only in JSON format."""

      # Create a schema from the routes dictionary
      class Schema(BaseModel):
          route: Literal[tuple(routes.keys())]

          reason: str = Field(
              description="Short one-liner explanation why this route was selected for the task in the prompt/query."
          )

      # Call LLM to select route
      selected_route = JSON_llm(
          ROUTER_PROMPT.format(user_query=input_query, routes=routes), Schema
      )
      print(
          f"Selected route:{selected_route['route']}\nReason: {selected_route['reason']}\n"
      )

      # Use LLM on selected route.
      # Could also have different prompts that need to be used for each route.
      response = run_llm(user_prompt=input_query, model=selected_route["route"])
      print(f"Response: {response}\n")

      return response
  ```

  ```ts TypeScript theme={null}
  import dedent from "dedent";
  import assert from "node:assert";
  import Together from "together-ai";
  import { z } from "zod";
  import zodToJsonSchema from "zod-to-json-schema";

  const client = new Together();

  const prompts = [
    "Produce python snippet to check to see if a number is prime or not.",
    "Plan and provide a short itenary for a 2 week vacation in Europe.",
    "Write a short story about a dragon and a knight.",
  ];

  const modelRoutes = {
    "Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8":
      "Best model choice for code generation tasks.",
    "Gryphe/MythoMax-L2-13b":
      "Best model choice for story-telling, role-playing and fantasy tasks.",
    "Qwen/Qwen3-Next-80B-A3B-Thinking":
      "Best model for reasoning, planning and multi-step tasks",
  };

  const schema = z.object({
    route: z.enum(Object.keys(modelRoutes) as [keyof typeof modelRoutes]),
    reason: z.string(),
  });
  const jsonSchema = zodToJsonSchema(schema, {
    target: "openAi",
  });

  async function routerWorkflow(
    inputQuery: string,
    routes: { [key: string]: string },
  ) {
    const routerPrompt = dedent`
      Given a user prompt/query: ${inputQuery}, select the best option out of the following routes:

      ${Object.keys(routes)
        .map((key) => `${key}: ${routes[key]}`)
        .join("\n")}

      Answer only in JSON format.`;

    // Call LLM to select route
    const routeResponse = await client.chat.completions.create({
      messages: [
        { role: "system", content: routerPrompt },
        { role: "user", content: inputQuery },
      ],
      model: "meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo",
      response_format: {
        type: "json_object",
        // @ts-expect-error Expected error
        schema: jsonSchema,
      },
    });

    const content = routeResponse.choices[0].message?.content;
    assert(typeof content === "string");
    const selectedRoute = schema.parse(JSON.parse(content));

    // Use LLM on selected route.
    // Could also have different prompts that need to be used for each route.
    const response = await client.chat.completions.create({
      messages: [{ role: "user", content: inputQuery }],
      model: selectedRoute.route,
    });
    const responseContent = response.choices[0].message?.content;
    console.log(`${responseContent}\n`);
  }

  async function main() {
    for (const prompt of prompts) {
      console.log(`Task ${prompts.indexOf(prompt) + 1}: ${prompt}`);
      console.log("====================");
      await routerWorkflow(prompt, modelRoutes);
    }
  }

  main();
  ```
</CodeGroup>

## Example Usage

```py Python theme={null}
prompt_list = [
    "Produce python snippet to check to see if a number is prime or not.",
    "Plan and provide a short itenary for a 2 week vacation in Europe.",
    "Write a short story about a dragon and a knight.",
]

model_routes = {
    "Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8": "Best model choice for code generation tasks.",
    "Gryphe/MythoMax-L2-13b": "Best model choice for story-telling, role-playing and fantasy tasks.",
    "Qwen/Qwen3-Next-80B-A3B-Thinking": "Best model for reasoning, planning and multi-step tasks",
}

for i, prompt in enumerate(prompt_list):
    print(f"Task {i+1}: {prompt}\n")
    print(20 * "==")
    router_workflow(prompt, model_routes)
```

## Use cases

* Routing easy/common questions to smaller models like Llama 3.1 8B and hard/unusual questions to more capable models like Deepseek v3 and Llama 3.3 70B to optimize cost and speed.
* Directing different types of customer service queries (general questions, refund requests, technical support) into different downstream processes, prompts, and tools.
* Different LLMs or model configurations excel at different tasks (e.g., writing summaries vs. generating code). Using a router, you can automatically detect the user's intent and send the input to the best-fit model.
* Evaluating whether a request meets certain guidelines or triggers specific filters (e.g., checking if content is disallowed). Based on the classification, forward it to the appropriate next LLM call or step.
* If one model's output doesn't meet a certain confidence threshold or fails for some reason, route automatically to a fallback model.

<Note>
  ### Conditional Workflow Cookbook

  For a more detailed walk-through refer to the [notebook here](https://togetherai.link/agent-recipes-deep-dive-routing).
</Note>


# Create Tickets In Slack
Source: https://docs.together.ai/docs/create-tickets-in-slack

For customers who have a shared Slack channel with us

## Emoji Ticketing

This feature allows you to easily create support tickets directly from Slack using emoji reactions.

1. Send a message in the Together shared channel
2. Add the 🎫 (ticket) emoji reaction to convert the thread into a ticket
3. A message will pop-up in the channel. Click on the `File ticket` button to proceed
4. In the form modal, fill out the required information and click `File ticket` to submit
5. Check the thread for ticket details

<Note>
  **Note:&#x20;**&#x54;he best practice is to use Slack threads by adding replies to the original post.
</Note>

<Frame>
  ![](https://mintlify-assets.b-cdn.net/1.gif)
</Frame>


# CrewAI
Source: https://docs.together.ai/docs/crewai

Using CrewAI with Together

CrewAI is an open source production-grade framework for orchestrating AI agent systems. It enables multiple AI agents to collaborate effectively by assuming roles and working toward shared goals. The framework supports both simple automations and complex applications that require coordinated agent behavior.

## Installing Libraries

<CodeGroup>
  ```shell Shell theme={null}
  uv pip install crewai
  ```
</CodeGroup>

Set your Together AI API key:

<CodeGroup>
  ```shell Shell theme={null}
  export TOGETHER_API_KEY=***
  ```
</CodeGroup>

## Example

<CodeGroup>
  ```python Python theme={null}
  import os
  from crewai import LLM, Task, Agent, Crew

  llm = LLM(
      model="together_ai/meta-llama/Llama-3.3-70B-Instruct-Turbo",
      api_key=os.environ.get("TOGETHER_API_KEY"),
      base_url="https://api.together.xyz/v1",
  )

  research_agent = Agent(
      llm=llm,
      role="Research Analyst",
      goal="Find and summarize information about specific topics",
      backstory="You are an experienced researcher with attention to detail",
      verbose=True,  # Enable logging for debugging
  )

  research_task = Task(
      description="Conduct a thorough research about AI Agents.",
      expected_output="A list with 10 bullet points of the most relevant information about AI Agents",
      agent=research_agent,
  )

  # Execute the crew
  crew = Crew(
      agents=[research_agent],
      tasks=[research_task],
      verbose=True,
  )

  result = crew.kickoff()

  # Accessing the task output
  task_output = research_task.output

  print(task_output)
  ```
</CodeGroup>

## Example Output

```
[2025-03-09 16:20:14][🚀 CREW 'CREW' STARTED, 42A4F700-E955-4794-B6F3-6EA6EF279E93]: 2025-03-09 16:20:14.069394

[2025-03-09 16:20:14][📋 TASK STARTED: CONDUCT A THOROUGH RESEARCH ABOUT AI AGENTS.]: 2025-03-09 16:20:14.085335

[2025-03-09 16:20:14][🤖 AGENT 'RESEARCH ANALYST' STARTED TASK]: 2025-03-09 16:20:14.096438
# Agent: Research Analyst
## Task: Conduct a thorough research about AI Agents.

[2025-03-09 16:20:14][🤖 LLM CALL STARTED]: 2025-03-09 16:20:14.096671

[2025-03-09 16:20:18][✅ LLM CALL COMPLETED]: 2025-03-09 16:20:18.993612

# Agent: Research Analyst
## Final Answer:
* AI Agents are computer programs that use artificial intelligence (AI) to perform tasks that typically require human intelligence, such as reasoning, problem-solving, and decision-making. They can be used in a variety of applications, including virtual assistants, customer service chatbots, and autonomous vehicles.
* There are several types of AI Agents, including simple reflex agents, model-based reflex agents, goal-based agents, and utility-based agents. Each type of agent has its own strengths and weaknesses, and is suited to specific tasks and environments.
* AI Agents can be classified into two main categories: narrow or weak AI, and general or strong AI. Narrow AI is designed to perform a specific task, while general AI is designed to perform any intellectual task that a human can.
* AI Agents use a variety of techniques to make decisions and take actions, including machine learning, deep learning, and natural language processing. They can also use sensors and other data sources to perceive their environment and make decisions based on that information.
* One of the key benefits of AI Agents is their ability to automate repetitive and mundane tasks, freeing up human workers to focus on more complex and creative tasks. They can also provide 24/7 customer support and help to improve customer engagement and experience.
* AI Agents can be used in a variety of industries, including healthcare, finance, and transportation. For example, AI-powered chatbots can be used to help patients schedule appointments and access medical records, while AI-powered virtual assistants can be used to help drivers navigate roads and avoid traffic.
* Despite their many benefits, AI Agents also have some limitations and challenges. For example, they can be biased if they are trained on biased data, and they can struggle to understand the nuances of human language and behavior.
* AI Agents can be used to improve decision-making and problem-solving in a variety of contexts. For example, they can be used to analyze large datasets and identify patterns and trends, and they can be used to simulate different scenarios and predict outcomes.
* The development and use of AI Agents raises important ethical and social questions, such as the potential impact on employment and the need for transparency and accountability in AI decision-making. It is essential to consider these questions and develop guidelines and regulations for the development and use of AI Agents.
* The future of AI Agents is likely to involve the development of more advanced and sophisticated agents that can learn and adapt in complex and dynamic environments. This may involve the use of techniques such as reinforcement learning and transfer learning, and the development of more human-like AI Agents that can understand and respond to human emotions and needs.


[2025-03-09 16:20:19][✅ AGENT 'RESEARCH ANALYST' COMPLETED TASK]: 2025-03-09 16:20:19.012674

[2025-03-09 16:20:19][✅ TASK COMPLETED: CONDUCT A THOROUGH RESEARCH ABOUT AI AGENTS.]: 2025-03-09 16:20:19.012784

[2025-03-09 16:20:19][✅ CREW 'CREW' COMPLETED, 42A4F700-E955-4794-B6F3-6EA6EF279E93]: 2025-03-09 16:20:19.027344
```


# Upload a Custom Model
Source: https://docs.together.ai/docs/custom-models

Run inference on your custom or fine-tuned models

You can upload custom or fine-tuned models from Hugging Face or S3 and run inference on a dedicated endpoint through Together AI. This is a quick guide that shows you how to do this through our UI or CLI.

### Requirements

Currently, we support models that meet the following criteria.

* **Source**: We support uploads from Hugging Face or S3.
* **Type**: We support text generation and embedding models.
* **Scale**: We currently only support models that fit in a single node. Multi-node models are not supported when you upload a custom model.

## Getting Started

### Upload the model

Model uploads can be done via the UI, API or the CLI.

The API reference can be found [here](/reference/upload-model).

#### UI

To upload via the web, just log in and navigate to models > add custom model to reach [this page](https://api.together.xyz/models/upload):

<Frame>
  <img src="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/c68be312d1d50dab706473dd648224e2a1a132a3149c19ba36a5a23243fdf901-Screenshot_2025-03-27_at_10.09.47.png?fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=d389f0262abf19e2b6b1ca0946b52def" alt="Upload model" data-og-width="3066" width="3066" data-og-height="1100" height="1100" data-path="images/docs/c68be312d1d50dab706473dd648224e2a1a132a3149c19ba36a5a23243fdf901-Screenshot_2025-03-27_at_10.09.47.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/c68be312d1d50dab706473dd648224e2a1a132a3149c19ba36a5a23243fdf901-Screenshot_2025-03-27_at_10.09.47.png?w=280&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=90932cab50d019bf4c320bf7e0b6ca8d 280w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/c68be312d1d50dab706473dd648224e2a1a132a3149c19ba36a5a23243fdf901-Screenshot_2025-03-27_at_10.09.47.png?w=560&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=26ea59655b289f8bd6c616ff5099be1f 560w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/c68be312d1d50dab706473dd648224e2a1a132a3149c19ba36a5a23243fdf901-Screenshot_2025-03-27_at_10.09.47.png?w=840&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=d807ed31fe31f1d833cafe12a1439ee4 840w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/c68be312d1d50dab706473dd648224e2a1a132a3149c19ba36a5a23243fdf901-Screenshot_2025-03-27_at_10.09.47.png?w=1100&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=0aa4c25ab2e40ad4e2c938c9061492f2 1100w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/c68be312d1d50dab706473dd648224e2a1a132a3149c19ba36a5a23243fdf901-Screenshot_2025-03-27_at_10.09.47.png?w=1650&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=3349867879f3b2a4a041b4905683c707 1650w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/c68be312d1d50dab706473dd648224e2a1a132a3149c19ba36a5a23243fdf901-Screenshot_2025-03-27_at_10.09.47.png?w=2500&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=e197ecdc9484daf0f13867d43374994d 2500w" />
</Frame>

Then fill in the source URL (S3 or Hugging Face), the model name and how you would like it described in your Together account once uploaded.

#### CLI

Upload a model from Hugging Face or S3:

<CodeGroup>
  ```bash CLI theme={null}
  together models upload \
    --model-name <your_model_name> \
    --model-source <path_to_model_or_repo> \
    --model-type <model_or_adapter> \
    --hf-token <your_HF_token_if_uploading_from_HF> \
    --description <description_of_your_model>
  ```
</CodeGroup>

### Checking the status of your upload

When an upload has been kicked off, it will return a job id. You can poll our API using the returned job id until the model has finished uploading.

<CodeGroup>
  ```curl cURL theme={null}
  curl -X GET "https://api.together.ai/v1/jobs/{jobId}" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -H "Content-Type: application/json" \
  ```
</CodeGroup>

The output contains a “status” field. When the “status” is “Complete”, your model is ready to be deployed.

### Deploy the model

Uploaded models are treated like any other dedicated endpoint models. Deploying a custom model can be done via the UI, API or the CLI.

The API reference can be found [here](/reference/createendpoint).

#### UI

All models, custom and finetuned models as well as any model that has a dedicated endpoint will be listed under [My Models](https://api.together.ai/models). To deploy a custom model:

Select the model to open the model page.

<Frame>
  <img src="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/7b710ddcba7873b0154ef5945f5aa36bd0627ab3791882f8f73a30e2942e5470-Screenshot_2025-03-13_at_6.14.17_AM.png?fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=7ac4fb3f82d0470fc70cecd4464e363f" alt="My Models" data-og-width="2828" width="2828" data-og-height="560" height="560" data-path="images/docs/7b710ddcba7873b0154ef5945f5aa36bd0627ab3791882f8f73a30e2942e5470-Screenshot_2025-03-13_at_6.14.17_AM.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/7b710ddcba7873b0154ef5945f5aa36bd0627ab3791882f8f73a30e2942e5470-Screenshot_2025-03-13_at_6.14.17_AM.png?w=280&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=ee441ef3255d1bfd8ff63db85bb407fb 280w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/7b710ddcba7873b0154ef5945f5aa36bd0627ab3791882f8f73a30e2942e5470-Screenshot_2025-03-13_at_6.14.17_AM.png?w=560&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=0dcb1f3453ce272baa6f3eefe378f9a5 560w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/7b710ddcba7873b0154ef5945f5aa36bd0627ab3791882f8f73a30e2942e5470-Screenshot_2025-03-13_at_6.14.17_AM.png?w=840&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=7d3fe9d96734cd6835b5febf32a16085 840w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/7b710ddcba7873b0154ef5945f5aa36bd0627ab3791882f8f73a30e2942e5470-Screenshot_2025-03-13_at_6.14.17_AM.png?w=1100&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=8a706e4eea81063b15daf19ca0735be8 1100w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/7b710ddcba7873b0154ef5945f5aa36bd0627ab3791882f8f73a30e2942e5470-Screenshot_2025-03-13_at_6.14.17_AM.png?w=1650&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=66c6adafbe6dde81a1336a37584673fd 1650w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/7b710ddcba7873b0154ef5945f5aa36bd0627ab3791882f8f73a30e2942e5470-Screenshot_2025-03-13_at_6.14.17_AM.png?w=2500&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=f1c66f7007a7c16ecb2609cc1021f52f 2500w" />
</Frame>

The model page will display details from your uploaded model with an option to create a dedicated endpoint.

<Frame>
  <img src="https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/docs/2bdec7e6a9d20983e2279c0e5e7f41985db97a510fb71c5428bd2108e16cbdd7-Screenshot_2025-03-13_at_6.12.55_AM.png?fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=5b945031b73a5d2339b72b7610dc06ba" alt="Create Dedicated Endpoint" data-og-width="1996" width="1996" data-og-height="1278" height="1278" data-path="images/docs/2bdec7e6a9d20983e2279c0e5e7f41985db97a510fb71c5428bd2108e16cbdd7-Screenshot_2025-03-13_at_6.12.55_AM.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/docs/2bdec7e6a9d20983e2279c0e5e7f41985db97a510fb71c5428bd2108e16cbdd7-Screenshot_2025-03-13_at_6.12.55_AM.png?w=280&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=45bccb56729beef135cee05e20c2eef0 280w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/docs/2bdec7e6a9d20983e2279c0e5e7f41985db97a510fb71c5428bd2108e16cbdd7-Screenshot_2025-03-13_at_6.12.55_AM.png?w=560&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=7a38178b02de45df1e4f35d635283d17 560w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/docs/2bdec7e6a9d20983e2279c0e5e7f41985db97a510fb71c5428bd2108e16cbdd7-Screenshot_2025-03-13_at_6.12.55_AM.png?w=840&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=734db4cccfccde307ad00e1c949ad4d8 840w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/docs/2bdec7e6a9d20983e2279c0e5e7f41985db97a510fb71c5428bd2108e16cbdd7-Screenshot_2025-03-13_at_6.12.55_AM.png?w=1100&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=633236b3f4715a4799b85d037ac75547 1100w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/docs/2bdec7e6a9d20983e2279c0e5e7f41985db97a510fb71c5428bd2108e16cbdd7-Screenshot_2025-03-13_at_6.12.55_AM.png?w=1650&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=8f7524a530785ced8dcf5940581c06f1 1650w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/docs/2bdec7e6a9d20983e2279c0e5e7f41985db97a510fb71c5428bd2108e16cbdd7-Screenshot_2025-03-13_at_6.12.55_AM.png?w=2500&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=f4fdde56398b156282787fbc68af058c 2500w" />
</Frame>

When you select 'Create Dedicated Endpoint' you will see an option to configure the deployment.

<Frame>
  <img src="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/c2a00bdf78bf334eabc05da86b06de88a35fe948c1462dd4dab003fa818f63fa-Screenshot_2025-03-13_at_6.13.14_AM.png?fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=fe01ff81c139d77cac9e2b06a73213e0" alt="Create Dedicated Endpoint" data-og-width="2014" width="2014" data-og-height="1284" height="1284" data-path="images/docs/c2a00bdf78bf334eabc05da86b06de88a35fe948c1462dd4dab003fa818f63fa-Screenshot_2025-03-13_at_6.13.14_AM.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/c2a00bdf78bf334eabc05da86b06de88a35fe948c1462dd4dab003fa818f63fa-Screenshot_2025-03-13_at_6.13.14_AM.png?w=280&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=bef7a876d3612d5464c4dd7918c2f678 280w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/c2a00bdf78bf334eabc05da86b06de88a35fe948c1462dd4dab003fa818f63fa-Screenshot_2025-03-13_at_6.13.14_AM.png?w=560&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=07f7eb409c7ad43c7b2e5f6ded97a6bc 560w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/c2a00bdf78bf334eabc05da86b06de88a35fe948c1462dd4dab003fa818f63fa-Screenshot_2025-03-13_at_6.13.14_AM.png?w=840&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=7f1e61ff6898217a0f436234f312456f 840w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/c2a00bdf78bf334eabc05da86b06de88a35fe948c1462dd4dab003fa818f63fa-Screenshot_2025-03-13_at_6.13.14_AM.png?w=1100&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=a328db005b31a0e58797205f60bd8a9d 1100w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/c2a00bdf78bf334eabc05da86b06de88a35fe948c1462dd4dab003fa818f63fa-Screenshot_2025-03-13_at_6.13.14_AM.png?w=1650&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=89f1dba80c45d558c5398ae069f5394e 1650w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/c2a00bdf78bf334eabc05da86b06de88a35fe948c1462dd4dab003fa818f63fa-Screenshot_2025-03-13_at_6.13.14_AM.png?w=2500&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=54da1ced0e5c7849badcd4b34c7af92d 2500w" />
</Frame>

Once an endpoint has been deployed, you can interact with it on the playground or via the API.

#### CLI

After uploading your model, you can verify its registration and check available hardware options.

**List your uploaded models:**

<CodeGroup>`bash CLI together models list `</CodeGroup>

**View available GPU SKUs for a specific model:**

<CodeGroup>
  ```bash CLI theme={null}
  together endpoints hardware --model <model-name>
  ```
</CodeGroup>

Once your model is uploaded, create a dedicated inference endpoint:

<CodeGroup>
  ```bash CLI theme={null}
  together endpoints create \
    --display-name <endpoint-name> \
    --model <model-name> \
    --gpu h100 \
    --no-speculative-decoding \
    --no-prompt-cache \
    --gpu-count 2
  ```
</CodeGroup>

After deploying, you can view all your endpoints and retrieve connection details such as URL, scaling configuration, and status.

**List all endpoints:**

<CodeGroup>`bash CLI together endpoints list `</CodeGroup>

**Get details for a specific endpoint:**

<CodeGroup>
  ```bash CLI theme={null}
  together endpoints get <endpoint-id>
  ```
</CodeGroup>


# Building An AI Data Analyst
Source: https://docs.together.ai/docs/data-analyst-agent

Learn how to use code interpreter to build an AI data analyst with E2B and Together AI.

Giving LLMs the ability to execute code is very powerful – it has many advantages such as:

* Better reasoning
* More complex tasks (e.g., advanced data analysis or mathematics)
* Producing tangible results such as charts
* Immediate testing (and correcting) of the produced output.

In this example, we'll show you how to build an AI data analyst that can read in data and make charts. We'll be using [E2B](https://e2b.dev/docs) for the code interpreter and Together AI for the LLM piece.

## 1. Prerequisites

Create a`main.ipynb` file and save your Together & E2B API keys in there.

Get the E2B API key [here](https://e2b.dev/docs/getting-started/api-key) and the Together AI API key [here](https://api.together.xyz/settings/api-keys). Download the CSV file from [here](https://www.kaggle.com/datasets/nishanthsalian/socioeconomic-country-profiles/code) and upload it to the same directory as your program. Rename it to `data.csv`.

## 2. Install the SDKs

```sh Shell theme={null}
pip install together==1.2.6 e2b-code-interpreter==0.0.10 dotenv==1.0.0
```

## 3. Define your model and system prompt

In the following code snippet, we'll define our API keys, our model of choice, and our system prompt.

You can pick the model of your choice by uncommenting it. There are some recommended models that are great at code generation, but you can add a different one from [here](/docs/serverless-models#chat-models).

For the system prompt, we tell the model it's a data scientist and give it some information about the uploaded CSV. You can choose different data but will need to update the instructions accordingly.

````py Python theme={null}
from dotenv import load_dotenv
import os
import json
import re
from together import Together
from e2b_code_interpreter import CodeInterpreter

load_dotenv()

# TODO: Get your Together AI API key from https://api.together.xyz/settings/api-keys
TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")

# TODO: Get your E2B API key from https://e2b.dev/docs
E2B_API_KEY = os.getenv("E2B_API_KEY")

# Choose from the codegen models:

MODEL_NAME = "meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo"
# MODEL_NAME = "meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo"
# MODEL_NAME = "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo"
# MODEL_NAME = "codellama/CodeLlama-70b-Instruct-hf"
# MODEL_NAME = "deepseek-ai/deepseek-coder-33b-instruct"
# MODEL_NAME = "Qwen/Qwen2-72B-Instruct"
# See the complete list of Together AI models here: https://api.together.ai/models.

SYSTEM_PROMPT = """You're a Python data scientist. You are given tasks to complete and you run Python code to solve them.

Information about the csv dataset:
- It's in the `/home/user/data.csv` file
- The CSV file is using , as the delimiter
- It has the following columns (examples included):
    - country: "Argentina", "Australia"
    - Region: "SouthAmerica", "Oceania"
    - Surface area (km2): for example, 2780400
    - Population in thousands (2017): for example, 44271
    - Population density (per km2, 2017): for example, 16.2
    - Sex ratio (m per 100 f, 2017): for example, 95.9
    - GDP: Gross domestic product (million current US$): for example, 632343
    - GDP growth rate (annual %, const. 2005 prices): for example, 2.4
    - GDP per capita (current US$): for example, 14564.5
    - Economy: Agriculture (% of GVA): for example, 10.0
    - Economy: Industry (% of GVA): for example, 28.1
    - Economy: Services and other activity (% of GVA): for example, 61.9
    - Employment: Agriculture (% of employed): for example, 4.8
    - Employment: Industry (% of employed): for example, 20.6
    - Employment: Services (% of employed): for example, 74.7
    - Unemployment (% of labour force): for example, 8.5
    - Employment: Female (% of employed): for example, 43.7
    - Employment: Male (% of employed): for example, 56.3
    - Labour force participation (female %): for example, 48.5
    - Labour force participation (male %): for example, 71.1
    - International trade: Imports (million US$): for example, 59253
    - International trade: Exports (million US$): for example, 57802
    - International trade: Balance (million US$): for example, -1451
    - Education: Government expenditure (% of GDP): for example, 5.3
    - Health: Total expenditure (% of GDP): for example, 8.1
    - Health: Government expenditure (% of total health expenditure): for example, 69.2
    - Health: Private expenditure (% of total health expenditure): for example, 30.8
    - Health: Out-of-pocket expenditure (% of total health expenditure): for example, 20.2
    - Health: External health expenditure (% of total health expenditure): for example, 0.2
    - Education: Primary gross enrollment ratio (f/m per 100 pop): for example, 111.5/107.6
    - Education: Secondary gross enrollment ratio (f/m per 100 pop): for example, 104.7/98.9
    - Education: Tertiary gross enrollment ratio (f/m per 100 pop): for example, 90.5/72.3
    - Education: Mean years of schooling (female): for example, 10.4
    - Education: Mean years of schooling (male): for example, 9.7
    - Urban population (% of total population): for example, 91.7
    - Population growth rate (annual %): for example, 0.9
    - Fertility rate (births per woman): for example, 2.3
    - Infant mortality rate (per 1,000 live births): for example, 8.9
    - Life expectancy at birth, female (years): for example, 79.7
    - Life expectancy at birth, male (years): for example, 72.9
    - Life expectancy at birth, total (years): for example, 76.4
    - Military expenditure (% of GDP): for example, 0.9
    - Population, female: for example, 22572521
    - Population, male: for example, 21472290
    - Tax revenue (% of GDP): for example, 11.0
    - Taxes on income, profits and capital gains (% of revenue): for example, 12.9
    - Urban population (% of total population): for example, 91.7

Generally, you follow these rules:
- ALWAYS FORMAT YOUR RESPONSE IN MARKDOWN
- ALWAYS RESPOND ONLY WITH CODE IN CODE BLOCK LIKE THIS:
      ```python'
      {code}
      ```'
   - the Python code runs in jupyter notebook.
   - every time you generate Python, the code is executed in a separate cell. it's okay to make multiple calls to `execute_python`.
   - display visualizations using matplotlib or any other visualization library directly in the notebook. don't worry about saving the visualizations to a file.
   - you have access to the internet and can make api requests.
   - you also have access to the filesystem and can read/write files.
   - you can install any pip package (if it exists) if you need to be running `!pip install {package}`. The usual packages for data analysis are already preinstalled though.
   - you can run any Python code you want, everything is running in a secure sandbox environment
   """
````

## 4. Add code interpreting capabilities and initialize the model

Now we define the function that will use the E2B code interpreter. Every time the LLM assistant decides that it needs to execute code, this function will be used. Read more about the Code Interpreter SDK [here](https://e2b.dev/docs/code-interpreter/installation).

We also initialize the Together AI client. The function for matching code blocks is important because we need to pick the right part of the output that contains the code produced by the LLM. The chat function takes care of the interaction with the LLM. It calls the E2B code interpreter anytime there is a code to be run.

````py Python theme={null}
def code_interpret(e2b_code_interpreter, code):
    print("Running code interpreter...")
    exec = e2b_code_interpreter.notebook.exec_cell(
        code,
        on_stderr=lambda stderr: print("[Code Interpreter]", stderr),
        on_stdout=lambda stdout: print("[Code Interpreter]", stdout),
        # You can also stream code execution results
        # on_result=...
    )

    if exec.error:
        print("[Code Interpreter ERROR]", exec.error)
    else:
        return exec.results


client = Together()

pattern = re.compile(
    r"```python\n(.*?)\n```", re.DOTALL
)  # Match everything in between ```python and ```


def match_code_blocks(llm_response):
    match = pattern.search(llm_response)
    if match:
        code = match.group(1)
        print(code)
        return code
    return ""


def chat_with_llm(e2b_code_interpreter, user_message):
    print(f"\n{'='*50}\nUser message: {user_message}\n{'='*50}")

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_message},
    ]

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=messages,
    )

    response_message = response.choices[0].message
    python_code = match_code_blocks(response_message.content)
    if python_code != "":
        code_interpreter_results = code_interpret(
            e2b_code_interpreter, python_code
        )
        return code_interpreter_results
    else:
        print(
            f"Failed to match any Python code in model's response {response_message}"
        )
        return []
````

## 5. Upload the dataset

The CSV data is uploaded programmatically, not via AI-generated code. The code interpreter by E2B runs inside the E2B sandbox. Read more about the file upload [here](https://e2b.dev/docs/sandbox/api/upload).

```py Python theme={null}
def upload_dataset(code_interpreter):
    print("Uploading dataset to Code Interpreter sandbox...")
    dataset_path = "./data.csv"

    if not os.path.exists(dataset_path):
        raise FileNotFoundError("Dataset file not found")

    try:
        with open(dataset_path, "rb") as f:
            remote_path = code_interpreter.upload_file(f)

        if not remote_path:
            raise ValueError("Failed to upload dataset")

        print("Uploaded at", remote_path)
        return remote_path
    except Exception as error:
        print("Error during file upload:", error)
        raise error
```

## 6. Put everything together

Finally we put everything together and let the AI assistant upload the data, run an analysis, and generate a PNG file with a chart. You can update the task for the assistant in this step. If you decide to change the CSV file you are using, don't forget to update the prompt too.

```py Python theme={null}
with CodeInterpreter(api_key=E2B_API_KEY) as code_interpreter:
    # Upload the dataset to the code interpreter sandbox
    upload_dataset(code_interpreter)

    code_results = chat_with_llm(
        code_interpreter,
        "Make a chart showing linear regression of the relationship between GDP per capita and life expectancy from the data. Filter out any missing values or values in wrong format.",
    )
    if code_results:
        first_result = code_results[0]
    else:
        raise Exception("No code interpreter results")


# This will render the image if you're running this in a notebook environment.
# If you're running it as a script, you can save the image to a file using the Pillow library.
first_result
```

## 7. Run the program and see the results

The resulting chart is generated within the notebook. The plot shows the linear regression of the relationship between GDP per capita and life expectancy from the CSV data:

```py Python theme={null}
# Uploading dataset to Code Interpreter sandbox...
# Uploaded at /home/user/data.csv
#
# ==================================================
# User message: Make a chart showing linear regression of the relationship between GDP per capita and life expectancy from the data. Filter out any missing values or values in wrong format.
# ==================================================
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load the data
data = pd.read_csv("/home/user/data.csv", delimiter=",")

# Clean the data
data = data.dropna(
    subset=[
        "GDP per capita (current US$)",
        "Life expectancy at birth, total (years)",
    ]
)
data["GDP per capita (current US$)"] = pd.to_numeric(
    data["GDP per capita (current US$)"],
    errors="coerce",
)
data["Life expectancy at birth, total (years)"] = pd.to_numeric(
    data["Life expectancy at birth, total (years)"],
    errors="coerce",
)

# Fit the linear regression model
X = data["GDP per capita (current US$)"].values.reshape(-1, 1)
y = data["Life expectancy at birth, total (years)"].values.reshape(-1, 1)
model = LinearRegression().fit(X, y)

# Plot the data and the regression line
plt.scatter(X, y, color="blue")
...
plt.xlabel("GDP per capita (current US$)")
plt.ylabel("Life expectancy at birth, total (years)")
plt.show()
# Running code interpreter...
```

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/23.png?fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=b9c58eb9ae30f293b174d5de47bd3e6e" alt="" data-og-width="562" width="562" data-og-height="455" height="455" data-path="images/guides/23.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/23.png?w=280&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=ef900d1b2578e53f74d3e38cc1adc92f 280w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/23.png?w=560&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=48ba12e2e9c29926782161d71ea5f806 560w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/23.png?w=840&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=103f6a96b5a1ed0efb324c46a471d8b6 840w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/23.png?w=1100&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=83986735aa046912f96c3b9e458609de 1100w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/23.png?w=1650&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=6ea6f81d6bfc38da2c89c955b4b31e9c 1650w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/23.png?w=2500&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=d738b701449c700c112de9cfe60037d6 2500w" />
</Frame>

## Resources

* [More guides: Mixture of Agents](/docs/mixture-of-agents)
* [E2B docs](https://e2b.dev/docs)
* [E2B Cookbook](https://github.com/e2b-dev/e2b-cookbook/tree/main)


# Dedicated Endpoints FAQs
Source: https://docs.together.ai/docs/dedicated-endpoints-1



## How does the system scale?

Dedicated endpoints support horizontal scaling. This means that it scales linearly with the additional replicas specified during endpoint configuration.

## How does auto-scaling affect my costs?

Billing for dedicated endpoints is proportional to the number of replicas. For example, scaling from 1 to 2 replicas will double your GPU costs.

## Is my endpoint guaranteed to scale to the max replica set?

We will scale to the max possible replica available at the time. This may be short of the max replicas that were set in the configuration if availability is limited.

## When to use vertical vs horizontal scale?

In other words, when to add GPUs per replica or add more replicas?

### Vertical scaling

Multiple GPUs, or vertical scaling, increases the generation speed, time to first token and max QPS. You should increase GPUs if your workload meets the following conditions:

**Compute-bound** If your workload is compute-intensive and bottlenecked by GPU processing power, adding more GPUs to a single endpoint can significantly improve performance.

**Memory-intensive** If your workload requires large amounts of memory, adding more GPUs to a single endpoint can provide more memory and improve performance.

**Single-node scalability** If your workload can scale well within a single node (e.g., using data parallelism or model parallelism), adding more GPUs to a single endpoint can be an effective way to increase throughput.

**Low-latency requirements** If your application requires low latency, increasing the number of GPUs on a single endpoint can help reduce latency by processing requests in parallel.

### Horizontal scaling

The number of replicas (horizontal scaling) increases the max number of QPS. You should increase the number of replicas if your workload meets the following conditions:

**I/O-bound workloads** If your workload is I/O-bound (e.g., waiting for data to be loaded or written), increasing the number of replicas can help spread the I/O load across multiple nodes.

**Request concurrency** If your application receives a high volume of concurrent requests, increasing the number of replicas can help distribute the load and improve responsiveness.

**Fault tolerance**: Increasing the number of replicas can improve fault tolerance by ensuring that if one node fails, others can continue to process requests.

**Scalability across multiple nodes** If your workload can scale well across multiple nodes (e.g., using data parallelism or distributed training), increasing the number of replicas can be an effective way to increase throughput.

## Troubleshooting dedicated endpoints configuration

There are a number of reasons that an endpoint isn't immediately created successfully.

**Lack of availability**: If we are short on available hardware, the endpoint will still be created but rather than automatically starting the endpoint, it will be queued for the next available hardware.

**Low availability**: We may have hardware available but only enough for a small amount of replicas. If this is the case, the endpoint may start but only scale to the amount of replicas available. If the min replica is set higher than we have capacity for, we may queue the endpoint until there is enough availability. To avoid the wait, you can reduce the minimum replica count.

**Hardware unavailable error**: If you see "Hardware for endpoint not available now. please try again later", the required resources are currently unavailable. Try using a different comparable model (see [whichllm.together.ai](https://whichllm.together.ai/)) or attempt deployment at a different time when more resources may be available.

**Model not supported**: Not all models are supported on dedicated endpoints. Check the list of supported models in your [account dashboard](https://api.together.xyz/models?filter=dedicated) under Models > All Models > Dedicated toggle. Your fine-tuned model must be based on a supported base model to deploy on an endpoint.

## Stopping an Endpoint

### Auto-shutdown

When you create an endpoint you can select an auto-shutdown timeframe during the configuration step. We offer various timeframes.

If you need to shut down your endpoint before the auto-shutdown period has elapsed, you can do this in a couple of ways.

### Web Interface

#### Shutdown during deployment

When your model is being deployed, you can click the red stop button to stop the deployment.

#### Shutdown when the endpoint is running

If the dedicated endpoint has started, you can shut down the endpoint by going to your models page. Click on the Model to expand the drop down, click the three dots and then **Stop endpoint**, then confirm in the pop-up prompt.

Once the endpoint has stopped, you will see it is offline on the models page. You can use the same three dots menu to start the endpoint again if you did this by mistake.

### API

You can also use the Together AI CLI to send a stop command, as covered in our documentation. To do this you will need your endpoint ID.

**Minimal availability**: We may have hardware available but only enough for a small amount of replicas. If this is the case, the endpoint may start but only scale to the amount of replicas available. If the min replica is set higher than we have capacity for, we may queue the endpoint until there is enough availability. To avoid the wait, you can reduce the min replica count.

## Will I be billed for the time spent spinning up the endpoint or looking for resources?

Billing events start only when a dedicated endpoint is successfully up and running. If there is a lag in time or a failure to deploy the endpoint, you will not be billed for that time.

## How much will I be charged to deploy a model?

Deployed models incur continuous per-minute hosting charges even when not actively processing requests. This applies to both fine-tuned models and dedicated endpoints. When you deploy a model, you should see a pricing prediction. This will change based on the hardware you select, as dedicated endpoints are charged based on the hardware used rather than the model being hosted.

You can find full details of our hardware pricing on our [pricing page](https://www.together.ai/pricing).

To avoid unexpected charges, make sure to set an auto-shutdown value, and regularly review your active deployments in the [models dashboard](https://api.together.xyz/models) to stop any unused endpoints. Remember that serverless endpoints are only charged based on actual token usage, while dedicated endpoints and fine-tuned models have ongoing hosting costs.


# Deploying Dedicated Endpoints
Source: https://docs.together.ai/docs/dedicated-endpoints-ui

Guide to creating dedicated endpoints via the web UI.

With Together AI, you can create on-demand dedicated endpoints with the following advantages:

* Consistent, predictable performance, unaffected by other users' load in our serverless environment
* No rate limits, with a high maximum load capacity
* More cost-effective under high utilization
* Access to a broader selection of models

## Creating an on demand dedicated endpoint

Navigate to the [Models page](https://api.together.xyz/models) in our playground. Under "All models" click "Dedicated." Search across 179 available models.

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/35.png?fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=0c3ceeb2256d838d6e80c1e1f17ab67d" alt="" data-og-width="2958" width="2958" data-og-height="1628" height="1628" data-path="images/guides/35.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/35.png?w=280&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=783ad2585a2500311f5ce3550f2dbb30 280w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/35.png?w=560&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=bd83993a17e21a1bc4e0b71294add6e3 560w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/35.png?w=840&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=64d46bb17fde33507417d43a89402708 840w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/35.png?w=1100&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=982c5a1caecd0b3bbfcb8a597d4a6bff 1100w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/35.png?w=1650&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=1314acdae8c3f67405e89e248f6675e3 1650w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/35.png?w=2500&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=0dea60abac384d19a9292ccd48a12dbf 2500w" />
</Frame>

Select your hardware. We have multiple hardware options available, all with varying prices (e.g. RTX-6000, L40, A100 SXM, A100 PCIe, and H100).

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/36.png?fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=fdc2961419e08a0922758f498f7a333a" alt="" data-og-width="2946" width="2946" data-og-height="1626" height="1626" data-path="images/guides/36.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/36.png?w=280&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=7857154644c6d608369538995671133b 280w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/36.png?w=560&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=5b0f7240d4153fffa67b622a070e5b57 560w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/36.png?w=840&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=445ceca56d9b0a97d375cc48816f0ccd 840w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/36.png?w=1100&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=88ccd0e9c3f2f76e39a344f65e3411ac 1100w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/36.png?w=1650&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=6a1460ad7411080ad00ec642da64ed4e 1650w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/36.png?w=2500&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=017357ab49e108ddba11fa229ee791a9 2500w" />
</Frame>

Click the Play button, and wait up to 10 minutes for the endpoint to be deployed.

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/37.png?fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=412baeca7510f61b5a61a254b0260eb1" alt="" data-og-width="2946" width="2946" data-og-height="1610" height="1610" data-path="images/guides/37.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/37.png?w=280&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=4770b214b36f1c2001b30adee6ac1e75 280w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/37.png?w=560&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=677f18bf18d29bcee5fca9b2cbbb83cb 560w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/37.png?w=840&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=30f0c9a759f5e897fc9e26ae00ea6f40 840w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/37.png?w=1100&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=026d721b806446e4e2d92cfd40dfad34 1100w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/37.png?w=1650&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=a431af84de95ddc38912f07a8fcc6b29 1650w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/37.png?w=2500&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=16128130b3906bb33497d05fa28d97d3 2500w" />
</Frame>

We will provide you the string you can use to call the model, as well as additional information about your deployment.

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/38.png?fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=aa6737c9c7dd6c7e29ee09c483708f46" alt="" data-og-width="2942" width="2942" data-og-height="1622" height="1622" data-path="images/guides/38.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/38.png?w=280&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=d6e4f2061e07e38b339c5a75ca2a36e2 280w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/38.png?w=560&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=1da32a6eeb5fdebe5a0904830b1bc58b 560w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/38.png?w=840&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=80c71a29cdee91bd17e6b3085d5ad578 840w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/38.png?w=1100&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=b60edd771e9360f5af9f49fd5a17d8a8 1100w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/38.png?w=1650&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=ff7b08bc1bdb1795b34164eec4ed36d3 1650w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/38.png?w=2500&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=62cb1479549a392c2aa20bc9ac4fe689 2500w" />
</Frame>

You can navigate away while your model is being deployed. Click open when it's ready:

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/39.png?fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=6ea83c6ea056acfb860ecd683b7f4dee" alt="" data-og-width="2954" width="2954" data-og-height="1638" height="1638" data-path="images/guides/39.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/39.png?w=280&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=d429919821e73c9647bba27b708c1e1a 280w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/39.png?w=560&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=9b0b2085536a560b0cde82adfd87a2a8 560w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/39.png?w=840&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=1aca589d3ab7007be037261f223f3b22 840w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/39.png?w=1100&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=9197c1624b1bb3a158a49373302cdcae 1100w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/39.png?w=1650&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=7f92608f147558d8efa462de181afb6f 1650w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/39.png?w=2500&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=ded8dfdc45a8ac7137fd1bd33c2a015b 2500w" />
</Frame>

Start using your endpoint!

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/40.png?fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=04400f84eb6783eea2e86081028b960d" alt="" data-og-width="2946" width="2946" data-og-height="1640" height="1640" data-path="images/guides/40.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/40.png?w=280&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=620f6be6b78462a99ae3f9e81b5df9b1 280w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/40.png?w=560&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=c378f09db28186ba1313170a326ae4d4 560w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/40.png?w=840&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=8b25eb3393e900befac9e6db234550f3 840w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/40.png?w=1100&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=c4977f7fa86efecf0bf25a05eb4993ba 1100w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/40.png?w=1650&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=4fc067cce3d7083c266bd5753f799e23 1650w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/40.png?w=2500&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=d623b0c81d339da962f987466bb1bb31 2500w" />
</Frame>

You can now find your endpoint in the My Models Page, and upon clicking the Model, under "Endpoints"

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/41.png?fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=3eff1812bb11f531a669d3bd7a2bfab9" alt="" data-og-width="2648" width="2648" data-og-height="488" height="488" data-path="images/guides/41.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/41.png?w=280&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=8750849ca56337be5ed6b8bc965c6cdb 280w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/41.png?w=560&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=8c1d8797cbbf966f54987dd0e1bbabed 560w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/41.png?w=840&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=c62a47660be11a6833d7b77c14e45407 840w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/41.png?w=1100&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=921669ce1ffa7400dbf4eb28aba5a1cb 1100w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/41.png?w=1650&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=77b6678a2a311d61d849761fc81e2e20 1650w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/41.png?w=2500&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=b6250a022f964dd604df643a36a35fa0 2500w" />
</Frame>

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/42.png?fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=f50768940462785d1dee1f7c244434ce" alt="" data-og-width="2630" width="2630" data-og-height="1468" height="1468" data-path="images/guides/42.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/42.png?w=280&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=a6cd8b97ee861440b295dced7b761468 280w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/42.png?w=560&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=21851653bc76fe58df140f9bf6f82e21 560w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/42.png?w=840&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=f661b3738aa70fd15dd9761b58c882d7 840w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/42.png?w=1100&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=fdd6601870fc04128ad355952871e65e 1100w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/42.png?w=1650&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=7abb29ed321e934043ee799bfcb21695 1650w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/42.png?w=2500&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=780feb7685f576b30c3323465228cd86 2500w" />
</Frame>

**Looking for custom configurations?** [Contact us.](https://www.together.ai/forms/monthly-reserved)


# Dedicated Inference
Source: https://docs.together.ai/docs/dedicated-inference

Deploy models on your own custom endpoints for improved reliability at scale

Dedicated Endpoints allows you to deploy models as dedicated endpoints with custom hardware and scaling configurations. Benefits of dedicated endpoints include:

* Predictable performance unaffected by serverless traffic.
* Reliable capacity to respond to spiky traffic.
* Customization to suit the unique usage of the model.

## Getting Started

Jump straight into the API with these [docs](/reference/listendpoints) or create an endpoint with this guide below.

### 1. Select a model

Explore the list of supported models for dedicated endpoints on our [models list](https://api.together.ai/models?filter=dedicated).

You can also upload your own [model](/docs/custom-models) .

### 2. Create a dedicated endpoint

To create a dedicated endpoint, first identify the hardware options for your specific model.

To do this, run:

<CodeGroup>
  ```shell Shell theme={null}
  together endpoints hardware --model <MODEL_ID>
  ```
</CodeGroup>

You will get a response like:

<CodeGroup>
  ```shell Shell theme={null}
  together endpoints hardware --model mistralai/Mixtral-8x7B-Instruct-v0.1

  All hardware options:
    2x_nvidia_a100_80gb_sxm
    2x_nvidia_h100_80gb_sxm
    4x_nvidia_a100_80gb_sxm
    4x_nvidia_h100_80gb_sxm
    8x_nvidia_a100_80gb_sxm
    8x_nvidia_h100_80gb_sxm
  ```
</CodeGroup>

From this list, you can identify which of the GPUs can be listed in your command. For example, in this list, the following combinations are possible:

1. `--gpu a100 --gpu-count 2`, `--gpu a100 --gpu-count 4`, `--gpu a100 --gpu-count 8`
2. `--gpu h100 --gpu-count 2`, `--gpu h100 --gpu-count 4`, `--gpu h100 --gpu-count 8`

You can now create a dedicated endpoint by running:

<CodeGroup>
  ```shell Shell theme={null}
  together endpoints create \
  --model mistralai/Mixtral-8x7B-Instruct-v0.1 \
  --gpu h100 \
  --gpu-count 2 \
  --no-speculative-decoding \
  --no-prompt-cache \
  --wait
  ```
</CodeGroup>

This command will finish when the endpoint is `READY`. To let it run asynchronously, remove the `--wait`flag.

You can optionally start an endpoint in a specific availability zone (e.g., us-central-4b). To get the list of availability zones, run:

<CodeGroup>
  ```shell Shell theme={null}
  together endpoints availability-zones
  ```
</CodeGroup>

Then specify the availability zone when creating your endpoint. Only specify an availability zone if you have specific latency or geographic needs as selecting one can limit hardware availability.

<CodeGroup>
  ```shell Shell theme={null}
  together endpoints create \
  --model mistralai/Mixtral-8x7B-Instruct-v0.1 \
  --gpu h100 \
  --gpu-count 2 \
  --availability-zone us-east-1a
  --no-speculative-decoding \
  --no-prompt-cache \
  --wait
  ```
</CodeGroup>

### 3. Get endpoint status

You can check on the deployment status by running:

<CodeGroup>
  ```shell Shell theme={null}
  together endpoints get <ENDPOINT_ID>
  ```
</CodeGroup>

A sample response will look like the following:

<CodeGroup>
  ```shell Shell theme={null}
  ID:		endpoint-e6c6b82f-90f7-45b7-af39-3ca3b51d08xx
  Name:		tester/mistralai/Mixtral-8x7B-Instruct-v0.1-bb04c904
  Display Name:	My Endpoint
  Hardware:	2x_nvidia_h100_80gb_sxm
  Autoscaling:	Min=1, Max=1
  Model:		mistralai/Mixtral-8x7B-Instruct-v0.1
  Type:		dedicated
  Owner:		tester
  State:		READY
  Created:	2025-02-18 11:55:50.686000+00:00
  ```
</CodeGroup>

### 4. Start, stop & delete endpoint

If you added the `--wait`flag on creation or previously stopped the endpoint, you can start it again by running:

<CodeGroup>
  ```shell Shell theme={null}
  together endpoints start <ENDPOINT_ID>
  ```
</CodeGroup>

Stopping the endpoint follows the same pattern:

<CodeGroup>
  ```shell Shell theme={null}
  together endpoints stop <ENDPOINT_ID>
  ```
</CodeGroup>

To fully delete the endpoint, run:

<CodeGroup>
  ```shell Shell theme={null}
  together endpoints delete <ENDPOINT_ID>
  ```
</CodeGroup>

### 5. List your endpoints

You can get a list of all your dedicated endpoints by running:

<CodeGroup>
  ```shell Shell theme={null}
  together endpoints list --mine true 
  ```
</CodeGroup>

To filter dedicated endpoints by usage type:

<CodeGroup>
  ```shell Shell theme={null}
  together endpoints list --mine true --type dedicated --usage-type on-demand
  ```
</CodeGroup>

## Endpoint options

### Replica count

Replicas provide horizontal scaling, ensuring better handling of high traffic, reduced latency, and resiliency in the event of instance failure. They are set with the `--min-replicas`and `--max-replicas`options. The default min and max replica is set to 1. When the max replica is increased, the endpoint will automatically scale based on server load.

### Auto-shutdown

If an endpoint is inactive for an hour, it will shutdown automatically. This window of inactivity can be customized when configuring a deployment in the web interface or by setting `--inactive-timeout` to the desired value.

### Choosing hardware and GPU count

A hardware configuration for a given model follows this format: \[gpu-count]-\[hardware]-\[gpu-type]-\[gpu-link]

Example:`2x_nvidia_h100_80gb_sxm`

When configuring the hardware on the CLI, you can specify which version of the hardware you would like by listing the `--gpu`(or hardware), `--gpu-count`and `gpu-type`

#### Multiple GPUs

Increasing the `gpu-count` will increase the GPUs per replica. This will result in higher generation speed, lower time-to-first-token and higher max QPS.

#### Availability zone

If you have specific latency or geographic needs, select an availability zone when creating your endpoint. It is important to note that restricting to an availability zone can limit hardware availability.

To get the list of availability zones, run:

<CodeGroup>
  ```shell Shell theme={null}
  together endpoints availability-zones
  ```
</CodeGroup>

### Speculative decoding

Speculative decoding is an optimization technique used to improve the efficiency of text generation and decoding processes. Using speculators can improve performance, increase throughput and improve the handling of uncertain or ambiguous input.

Customers who require consistently low tail latencies—such as those running real-time or mission-critical applications—may want to avoid speculative decoding. While this technique can improve average performance, it also introduces the risk of occasional extreme delays, which may be unacceptable in latency-sensitive workloads.

By default, speculative decoding is not enabled. To enable speculative decoding, remove the `--no-speculative-decoding` flag from the create command.

### Prompt caching

Prompt caching stores the results of previously executed prompts, allowing your model to quickly retrieve and return cached responses instead of reprocessing the same input. This significantly improves performance by reducing redundant computations.

By default, caching is not enabled. To turn on prompt caching, remove `--no-prompt-cache` from the create command.


# Dedicated Models
Source: https://docs.together.ai/docs/dedicated-models



export const ModelTable = ({type}) => {
  const models = [{
    id: "Alibaba-NLP/gte-modernbert-base",
    organization: "Alibaba Nlp",
    name: "Gte Modernbert Base",
    apiName: "Alibaba-NLP/gte-modernbert-base",
    type: "embedding",
    contextLength: 8192
  }, {
    id: "arcee_ai/arcee-spotlight",
    organization: "Arcee AI",
    name: "Arcee AI Spotlight",
    apiName: "arcee_ai/arcee-spotlight",
    type: "chat",
    contextLength: 131072
  }, {
    id: "arcee-ai/AFM-4.5B",
    organization: "Arcee AI",
    name: "Arcee AI AFM 4.5B",
    apiName: "arcee-ai/AFM-4.5B",
    type: "chat",
    contextLength: 65536
  }, {
    id: "arcee-ai/coder-large",
    organization: "Arcee AI",
    name: "Arcee AI Coder-Large",
    apiName: "arcee-ai/coder-large",
    type: "chat",
    contextLength: 32768
  }, {
    id: "arcee-ai/maestro-reasoning",
    organization: "Arcee AI",
    name: "Arcee AI Maestro",
    apiName: "arcee-ai/maestro-reasoning",
    type: "chat",
    contextLength: 131072
  }, {
    id: "arcee-ai/virtuoso-large",
    organization: "Arcee AI",
    name: "Arcee AI Virtuoso-Large",
    apiName: "arcee-ai/virtuoso-large",
    type: "chat",
    contextLength: 131072
  }, {
    id: "arize-ai/qwen-2-1.5b-instruct",
    organization: "Togethercomputer",
    name: "Arize AI Qwen 2 1.5B Instruct",
    apiName: "arize-ai/qwen-2-1.5b-instruct",
    type: "chat",
    contextLength: 32768
  }, {
    id: "BAAI/bge-base-en-v1.5",
    organization: "BAAI",
    name: "BAAI-Bge-Base-1.5",
    apiName: "BAAI/bge-base-en-v1.5",
    type: "embedding",
    contextLength: 512
  }, {
    id: "BAAI/bge-large-en-v1.5",
    organization: "BAAI",
    name: "BAAI-Bge-Large-1.5",
    apiName: "BAAI/bge-large-en-v1.5",
    type: "embedding",
    contextLength: 0
  }, {
    id: "black-forest-labs/FLUX.1-dev",
    organization: "Black Forest Labs",
    name: "FLUX.1 [dev]",
    apiName: "black-forest-labs/FLUX.1-dev",
    type: "image",
    contextLength: 0
  }, {
    id: "black-forest-labs/FLUX.1-dev-lora",
    organization: "Black Forest Labs",
    name: "FLUX.1 [dev] LoRA",
    apiName: "black-forest-labs/FLUX.1-dev-lora",
    type: "image",
    contextLength: 0
  }, {
    id: "black-forest-labs/FLUX.1-kontext-dev",
    organization: "Black Forest Labs",
    name: "FLUX.1 Kontext [dev]",
    apiName: "black-forest-labs/FLUX.1-kontext-dev",
    type: "image",
    contextLength: 0
  }, {
    id: "black-forest-labs/FLUX.1-kontext-max",
    organization: "Black Forest Labs",
    name: "FLUX.1 Kontext [max]",
    apiName: "black-forest-labs/FLUX.1-kontext-max",
    type: "image",
    contextLength: 0
  }, {
    id: "black-forest-labs/FLUX.1-kontext-pro",
    organization: "Black Forest Labs",
    name: "FLUX.1 Kontext [pro]",
    apiName: "black-forest-labs/FLUX.1-kontext-pro",
    type: "image",
    contextLength: 0
  }, {
    id: "black-forest-labs/FLUX.1-krea-dev",
    organization: "Black Forest Labs",
    name: "FLUX.1 Krea [dev]",
    apiName: "black-forest-labs/FLUX.1-krea-dev",
    type: "image",
    contextLength: 0
  }, {
    id: "black-forest-labs/FLUX.1-schnell",
    organization: "Black Forest Labs",
    name: "FLUX.1 Schnell",
    apiName: "black-forest-labs/FLUX.1-schnell",
    type: "image",
    contextLength: 0
  }, {
    id: "black-forest-labs/FLUX.1-schnell-Free",
    organization: "Black Forest Labs",
    name: "FLUX.1 [schnell] Free",
    apiName: "black-forest-labs/FLUX.1-schnell-Free",
    type: "image",
    contextLength: 0
  }, {
    id: "black-forest-labs/FLUX.1.1-pro",
    organization: "Black Forest Labs",
    name: "FLUX1.1 [pro]",
    apiName: "black-forest-labs/FLUX.1.1-pro",
    type: "image",
    contextLength: 0
  }, {
    id: "cartesia/sonic",
    organization: "Together",
    name: "Cartesia Sonic",
    apiName: "cartesia/sonic",
    type: "audio",
    contextLength: 0
  }, {
    id: "cartesia/sonic-2",
    organization: "Together",
    name: "Cartesia Sonic 2",
    apiName: "cartesia/sonic-2",
    type: "audio",
    contextLength: 0
  }, {
    id: "deepcogito/cogito-v2-preview-deepseek-671b",
    organization: "Deepcogito",
    name: "Cogito V2 Preview Deepseek 671B Moe",
    apiName: "deepcogito/cogito-v2-preview-deepseek-671b",
    type: "chat",
    contextLength: 163840
  }, {
    id: "deepcogito/cogito-v2-preview-llama-109B-MoE",
    organization: "Deepcogito",
    name: "Cogito V2 Preview Llama 109B MoE",
    apiName: "deepcogito/cogito-v2-preview-llama-109B-MoE",
    type: "chat",
    contextLength: 32767
  }, {
    id: "deepcogito/cogito-v2-preview-llama-405B",
    organization: "Deepcogito",
    name: "Deepcogito Cogito V2 Preview Llama 405B",
    apiName: "deepcogito/cogito-v2-preview-llama-405B",
    type: "chat",
    contextLength: 32768
  }, {
    id: "deepcogito/cogito-v2-preview-llama-70B",
    organization: "Deepcogito",
    name: "Deepcogito Cogito V2 Preview Llama 70B",
    apiName: "deepcogito/cogito-v2-preview-llama-70B",
    type: "chat",
    contextLength: 32768
  }, {
    id: "deepseek-ai/DeepSeek-R1",
    organization: "DeepSeek",
    name: "DeepSeek R1-0528",
    apiName: "deepseek-ai/DeepSeek-R1",
    type: "chat",
    contextLength: 163840
  }, {
    id: "deepseek-ai/DeepSeek-R1-0528-tput",
    organization: "DeepSeek",
    name: "DeepSeek R1 0528 Throughput",
    apiName: "deepseek-ai/DeepSeek-R1-0528-tput",
    type: "chat",
    contextLength: 163840
  }, {
    id: "deepseek-ai/DeepSeek-R1-Distill-Llama-70B",
    organization: "DeepSeek",
    name: "DeepSeek R1 Distill Llama 70B",
    apiName: "deepseek-ai/DeepSeek-R1-Distill-Llama-70B",
    type: "chat",
    contextLength: 131072
  }, {
    id: "deepseek-ai/DeepSeek-R1-Distill-Llama-70B-free",
    organization: "DeepSeek",
    name: "DeepSeek R1 Distill Llama 70B Free",
    apiName: "deepseek-ai/DeepSeek-R1-Distill-Llama-70B-free",
    type: "chat",
    contextLength: 8192
  }, {
    id: "deepseek-ai/DeepSeek-R1-Distill-Qwen-14B",
    organization: "DeepSeek",
    name: "DeepSeek R1 Distill Qwen 14B",
    apiName: "deepseek-ai/DeepSeek-R1-Distill-Qwen-14B",
    type: "chat",
    contextLength: 131072
  }, {
    id: "deepseek-ai/DeepSeek-V3",
    organization: "DeepSeek",
    name: "DeepSeek V3-0324",
    apiName: "deepseek-ai/DeepSeek-V3",
    type: "chat",
    contextLength: 131072
  }, {
    id: "deepseek-ai/DeepSeek-V3.1",
    organization: "DeepSeek",
    name: "Deepseek V3.1",
    apiName: "deepseek-ai/DeepSeek-V3.1",
    type: "chat",
    contextLength: 131072
  }, {
    id: "google/gemma-3n-E4B-it",
    organization: "Google",
    name: "Gemma 3N E4B Instruct",
    apiName: "google/gemma-3n-E4B-it",
    type: "chat",
    contextLength: 32768
  }, {
    id: "intfloat/multilingual-e5-large-instruct",
    organization: "Intfloat",
    name: "Multilingual E5 Large Instruct",
    apiName: "intfloat/multilingual-e5-large-instruct",
    type: "embedding",
    contextLength: 514
  }, {
    id: "lgai/exaone-3-5-32b-instruct",
    organization: "LG AI",
    name: "EXAONE 3.5 32B Instruct",
    apiName: "lgai/exaone-3-5-32b-instruct",
    type: "chat",
    contextLength: 32768
  }, {
    id: "lgai/exaone-deep-32b",
    organization: "LG AI",
    name: "EXAONE Deep 32B",
    apiName: "lgai/exaone-deep-32b",
    type: "chat",
    contextLength: 32768
  }, {
    id: "marin-community/marin-8b-instruct",
    organization: "Marin Community",
    name: "Marin 8B Instruct",
    apiName: "marin-community/marin-8b-instruct",
    type: "chat",
    contextLength: 4096
  }, {
    id: "meta-llama/Llama-2-70b-hf",
    organization: "",
    name: "LLaMA-2 (70B)",
    apiName: "meta-llama/Llama-2-70b-hf",
    type: "language",
    contextLength: 4096
  }, {
    id: "meta-llama/Llama-3-70b-chat-hf",
    organization: "Meta",
    name: "Meta Llama 3 70B Instruct Reference",
    apiName: "meta-llama/Llama-3-70b-chat-hf",
    type: "chat",
    contextLength: 8192
  }, {
    id: "meta-llama/Llama-3-70b-hf",
    organization: "Meta",
    name: "Meta Llama 3 70B HF",
    apiName: "meta-llama/Llama-3-70b-hf",
    type: "language",
    contextLength: 8192
  }, {
    id: "meta-llama/Llama-3.1-405B-Instruct",
    organization: "Meta",
    name: "Meta Llama 3.1 405B Instruct",
    apiName: "meta-llama/Llama-3.1-405B-Instruct",
    type: "chat",
    contextLength: 4096
  }, {
    id: "meta-llama/Llama-3.2-1B-Instruct",
    organization: "Meta",
    name: "Meta Llama 3.2 1B Instruct",
    apiName: "meta-llama/Llama-3.2-1B-Instruct",
    type: "chat",
    contextLength: 131072
  }, {
    id: "meta-llama/Llama-3.2-3B-Instruct-Turbo",
    organization: "Meta",
    name: "Meta Llama 3.2 3B Instruct Turbo",
    apiName: "meta-llama/Llama-3.2-3B-Instruct-Turbo",
    type: "chat",
    contextLength: 131072
  }, {
    id: "meta-llama/Llama-3.3-70B-Instruct-Turbo",
    organization: "Meta",
    name: "Meta Llama 3.3 70B Instruct Turbo",
    apiName: "meta-llama/Llama-3.3-70B-Instruct-Turbo",
    type: "chat",
    contextLength: 131072
  }, {
    id: "meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
    organization: "Meta",
    name: "Meta Llama 3.3 70B Instruct Turbo Free",
    apiName: "meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
    type: "chat",
    contextLength: 131072
  }, {
    id: "meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8",
    organization: "Meta",
    name: "Llama 4 Maverick Instruct (17Bx128E)",
    apiName: "meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8",
    type: "chat",
    contextLength: 1048576
  }, {
    id: "meta-llama/Llama-4-Scout-17B-16E-Instruct",
    organization: "Meta",
    name: "Llama 4 Scout Instruct (17Bx16E)",
    apiName: "meta-llama/Llama-4-Scout-17B-16E-Instruct",
    type: "chat",
    contextLength: 1048576
  }, {
    id: "meta-llama/Llama-Guard-3-11B-Vision-Turbo",
    organization: "Meta",
    name: "Meta Llama Guard 3 11B Vision Turbo",
    apiName: "meta-llama/Llama-Guard-3-11B-Vision-Turbo",
    type: "moderation",
    contextLength: 131072
  }, {
    id: "meta-llama/Llama-Guard-4-12B",
    organization: "Meta",
    name: "Llama Guard 4 12B",
    apiName: "meta-llama/Llama-Guard-4-12B",
    type: "moderation",
    contextLength: 1048576
  }, {
    id: "meta-llama/LlamaGuard-2-8b",
    organization: "Meta",
    name: "Meta Llama Guard 2 8B",
    apiName: "meta-llama/LlamaGuard-2-8b",
    type: "moderation",
    contextLength: 8192
  }, {
    id: "meta-llama/Meta-Llama-3-70B-Instruct-Turbo",
    organization: "Meta",
    name: "Meta Llama 3 70B Instruct Turbo",
    apiName: "meta-llama/Meta-Llama-3-70B-Instruct-Turbo",
    type: "chat",
    contextLength: 8192
  }, {
    id: "meta-llama/Meta-Llama-3-8B-Instruct",
    organization: "Meta",
    name: "Meta Llama 3 8B Instruct",
    apiName: "meta-llama/Meta-Llama-3-8B-Instruct",
    type: "chat",
    contextLength: 8192
  }, {
    id: "meta-llama/Meta-Llama-3-8B-Instruct-Lite",
    organization: "Meta",
    name: "Meta Llama 3 8B Instruct Lite",
    apiName: "meta-llama/Meta-Llama-3-8B-Instruct-Lite",
    type: "chat",
    contextLength: 8192
  }, {
    id: "meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo",
    organization: "Meta",
    name: "Meta Llama 3.1 405B Instruct Turbo",
    apiName: "meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo",
    type: "chat",
    contextLength: 130815
  }, {
    id: "meta-llama/Meta-Llama-3.1-70B-Instruct-Reference",
    organization: "Meta",
    name: "Meta Llama 3.1 70B Instruct",
    apiName: "meta-llama/Meta-Llama-3.1-70B-Instruct-Reference",
    type: "chat",
    contextLength: 8192
  }, {
    id: "meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo",
    organization: "Meta",
    name: "Meta Llama 3.1 70B Instruct Turbo",
    apiName: "meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo",
    type: "chat",
    contextLength: 131072
  }, {
    id: "meta-llama/Meta-Llama-3.1-8B-Instruct-Reference",
    organization: "Meta",
    name: "Meta Llama 3.1 8B Instruct",
    apiName: "meta-llama/Meta-Llama-3.1-8B-Instruct-Reference",
    type: "chat",
    contextLength: 16384
  }, {
    id: "meta-llama/Meta-Llama-Guard-3-8B",
    organization: "Meta",
    name: "Meta Llama Guard 3 8B",
    apiName: "meta-llama/Meta-Llama-Guard-3-8B",
    type: "moderation",
    contextLength: 8192
  }, {
    id: "mistralai/Mistral-7B-Instruct-v0.1",
    organization: "mistralai",
    name: "Mistral (7B) Instruct v0.1",
    apiName: "mistralai/Mistral-7B-Instruct-v0.1",
    type: "chat",
    contextLength: 32768
  }, {
    id: "mistralai/Mistral-7B-Instruct-v0.2",
    organization: "mistralai",
    name: "Mistral (7B) Instruct v0.2",
    apiName: "mistralai/Mistral-7B-Instruct-v0.2",
    type: "chat",
    contextLength: 32768
  }, {
    id: "mistralai/Mistral-7B-Instruct-v0.3",
    organization: "mistralai",
    name: "Mistral (7B) Instruct v0.3",
    apiName: "mistralai/Mistral-7B-Instruct-v0.3",
    type: "chat",
    contextLength: 32768
  }, {
    id: "mistralai/Mistral-Small-24B-Instruct-2501",
    organization: "mistralai",
    name: "Mistral Small (24B) Instruct 25.01",
    apiName: "mistralai/Mistral-Small-24B-Instruct-2501",
    type: "chat",
    contextLength: 32768
  }, {
    id: "mistralai/Mixtral-8x7B-Instruct-v0.1",
    organization: "mistralai",
    name: "Mixtral-8x7B Instruct v0.1",
    apiName: "mistralai/Mixtral-8x7B-Instruct-v0.1",
    type: "chat",
    contextLength: 32768
  }, {
    id: "mixedbread-ai/Mxbai-Rerank-Large-V2",
    organization: "Mixedbread AI",
    name: "Mxbai Rerank Large V2",
    apiName: "mixedbread-ai/Mxbai-Rerank-Large-V2",
    type: "rerank",
    contextLength: 32768
  }, {
    id: "moonshotai/Kimi-K2-Instruct",
    organization: "Moonshotai",
    name: "Kimi K2 Instruct",
    apiName: "moonshotai/Kimi-K2-Instruct",
    type: "chat",
    contextLength: 131072
  }, {
    id: "moonshotai/Kimi-K2-Instruct-0905",
    organization: "Moonshotai",
    name: "Kimi K2-Instruct 0905",
    apiName: "moonshotai/Kimi-K2-Instruct-0905",
    type: "chat",
    contextLength: 262144
  }, {
    id: "openai/gpt-oss-120b",
    organization: "OpenAI",
    name: "OpenAI GPT-OSS 120B",
    apiName: "openai/gpt-oss-120b",
    type: "chat",
    contextLength: 131072
  }, {
    id: "openai/gpt-oss-20b",
    organization: "OpenAI",
    name: "OpenAI GPT-OSS 20B",
    apiName: "openai/gpt-oss-20b",
    type: "chat",
    contextLength: 131072
  }, {
    id: "openai/whisper-large-v3",
    organization: "OpenAI",
    name: "Whisper large-v3",
    apiName: "openai/whisper-large-v3",
    type: "transcribe",
    contextLength: 0
  }, {
    id: "Qwen/Qwen2.5-72B-Instruct",
    organization: "Qwen",
    name: "Qwen2.5 72B Instruct",
    apiName: "Qwen/Qwen2.5-72B-Instruct",
    type: "chat",
    contextLength: 32768
  }, {
    id: "Qwen/Qwen2.5-72B-Instruct-Turbo",
    organization: "Qwen",
    name: "Qwen2.5 72B Instruct Turbo",
    apiName: "Qwen/Qwen2.5-72B-Instruct-Turbo",
    type: "chat",
    contextLength: 131072
  }, {
    id: "Qwen/Qwen2.5-7B-Instruct-Turbo",
    organization: "Qwen",
    name: "Qwen2.5 7B Instruct Turbo",
    apiName: "Qwen/Qwen2.5-7B-Instruct-Turbo",
    type: "chat",
    contextLength: 32768
  }, {
    id: "Qwen/Qwen2.5-Coder-32B-Instruct",
    organization: "Qwen",
    name: "Qwen 2.5 Coder 32B Instruct",
    apiName: "Qwen/Qwen2.5-Coder-32B-Instruct",
    type: "chat",
    contextLength: 16384
  }, {
    id: "Qwen/Qwen2.5-VL-72B-Instruct",
    organization: "Qwen",
    name: "Qwen2.5-VL (72B) Instruct",
    apiName: "Qwen/Qwen2.5-VL-72B-Instruct",
    type: "chat",
    contextLength: 32768
  }, {
    id: "Qwen/Qwen3-235B-A22B-fp8-tput",
    organization: "Qwen",
    name: "Qwen3 235B A22B FP8 Throughput",
    apiName: "Qwen/Qwen3-235B-A22B-fp8-tput",
    type: "chat",
    contextLength: 40960
  }, {
    id: "Qwen/Qwen3-235B-A22B-Instruct-2507-tput",
    organization: "Qwen",
    name: "Qwen3 235B A22B Instruct 2507 FP8 Throughput",
    apiName: "Qwen/Qwen3-235B-A22B-Instruct-2507-tput",
    type: "chat",
    contextLength: 262144
  }, {
    id: "Qwen/Qwen3-235B-A22B-Thinking-2507",
    organization: "Qwen",
    name: "Qwen3 235B A22B Thinking 2507 FP8",
    apiName: "Qwen/Qwen3-235B-A22B-Thinking-2507",
    type: "chat",
    contextLength: 262144
  }, {
    id: "Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8",
    organization: "Qwen",
    name: "Qwen3 Coder 480B A35B Instruct Fp8",
    apiName: "Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8",
    type: "chat",
    contextLength: 262144
  }, {
    id: "Qwen/Qwen3-Next-80B-A3B-Instruct",
    organization: "Qwen",
    name: "Qwen3 Next 80B A3b Instruct",
    apiName: "Qwen/Qwen3-Next-80B-A3B-Instruct",
    type: "chat",
    contextLength: 262144
  }, {
    id: "Qwen/Qwen3-Next-80B-A3B-Thinking",
    organization: "Qwen",
    name: "Qwen3 Next 80B A3b Thinking",
    apiName: "Qwen/Qwen3-Next-80B-A3B-Thinking",
    type: "chat",
    contextLength: 262144
  }, {
    id: "Qwen/QwQ-32B",
    organization: "Qwen",
    name: "Qwen QwQ-32B",
    apiName: "Qwen/QwQ-32B",
    type: "chat",
    contextLength: 131072
  }, {
    id: "Salesforce/Llama-Rank-V1",
    organization: "salesforce",
    name: "Salesforce Llama Rank V1 (8B)",
    apiName: "Salesforce/Llama-Rank-V1",
    type: "rerank",
    contextLength: 8192
  }, {
    id: "scb10x/scb10x-typhoon-2-1-gemma3-12b",
    organization: "",
    name: "Typhoon 2.1 12B",
    apiName: "scb10x/scb10x-typhoon-2-1-gemma3-12b",
    type: "chat",
    contextLength: 131072
  }, {
    id: "togethercomputer/m2-bert-80M-32k-retrieval",
    organization: "Together",
    name: "M2-BERT-Retrieval-32k",
    apiName: "togethercomputer/m2-bert-80M-32k-retrieval",
    type: "embedding",
    contextLength: 32768
  }, {
    id: "togethercomputer/MoA-1",
    organization: "Together AI",
    name: "Together AI MoA-1",
    apiName: "togethercomputer/MoA-1",
    type: "chat",
    contextLength: 32768
  }, {
    id: "togethercomputer/MoA-1-Turbo",
    organization: "Together AI",
    name: "Together AI MoA-1-Turbo",
    apiName: "togethercomputer/MoA-1-Turbo",
    type: "chat",
    contextLength: 32768
  }, {
    id: "togethercomputer/Refuel-Llm-V2",
    organization: "Refuel AI",
    name: "Refuel LLM V2",
    apiName: "togethercomputer/Refuel-Llm-V2",
    type: "chat",
    contextLength: 16384
  }, {
    id: "togethercomputer/Refuel-Llm-V2-Small",
    organization: "Refuel AI",
    name: "Refuel LLM V2 Small",
    apiName: "togethercomputer/Refuel-Llm-V2-Small",
    type: "chat",
    contextLength: 8192
  }, {
    id: "Virtue-AI/VirtueGuard-Text-Lite",
    organization: "Virtue AI",
    name: "Virtueguard Text Lite",
    apiName: "Virtue-AI/VirtueGuard-Text-Lite",
    type: "moderation",
    contextLength: 32768
  }, {
    id: "zai-org/GLM-4.5-Air-FP8",
    organization: "Zai Org",
    name: "Glm 4.5 Air Fp8",
    apiName: "zai-org/GLM-4.5-Air-FP8",
    type: "chat",
    contextLength: 131072
  }];
  const serverlessOnly = ["Alibaba-NLP/gte-modernbert-base", "arcee-ai/coder-large", "arcee-ai/maestro-reasoning", "arcee-ai/virtuoso-large", "arcee_ai/arcee-spotlight", "arcee-ai/AFM-4.5B", "arize-ai/qwen-2-1.5b-instruct", "black-forest-labs/FLUX.1-schnell", "black-forest-labs/FLUX.1-kontext-dev", "black-forest-labs/FLUX.1-dev", "black-forest-labs/FLUX.1.1-pro", "black-forest-labs/FLUX.1-krea-dev", "black-forest-labs/FLUX.1-dev-lora", "BAAI/bge-large-en-v1.5", "BAAI/bge-base-en-v1.5", "cartesia/sonic", "cartesia/sonic-2", "deepcogito/cogito-v2-preview-llama-405B", "deepcogito/cogito-v2-preview-deepseek-671b", "deepcogito/cogito-v2-preview-llama-109B-MoE", "deepcogito/cogito-v2-preview-llama-70B", "deepseek-ai/DeepSeek-R1-Distill-Llama-70B-free", "deepseek-ai/DeepSeek-R1-0528-tput", "intfloat/multilingual-e5-large-instruct", "google/gemma-3n-E4B-it", "lgai/exaone-3-5-32b-instruct", "lgai/exaone-deep-32b", "marin-community/marin-8b-instruct", "meta-llama/Meta-Llama-Guard-3-8B", "meta-llama/LlamaGuard-2-8b", "meta-llama/Llama-3.3-70B-Instruct-Turbo-Free", "meta-llama/Llama-Guard-3-11B-Vision-Turbo", "meta-llama/Llama-3-70b-hf", "meta-llama/Meta-Llama-3.1-70B-Instruct-Reference", "meta-llama/Meta-Llama-3.1-8B-Instruct-Reference", "mistralai/Mistral-Small-24B-Instruct-2501", "mixedbread-ai/Mxbai-Rerank-Large-V2", "moonshotai/Kimi-K2-Instruct", "meta-llama/Meta-Llama-3-8B-Instruct-Lite", "meta-llama/Llama-3-70b-chat-hf", "meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo", "meta-llama/Llama-Guard-4-12B", "scb10x/scb10x-typhoon-2-1-gemma3-12b", "togethercomputer/MoA-1", "togethercomputer/Refuel-Llm-V2-Small", "togethercomputer/MoA-1-Turbo", "togethercomputer/m2-bert-80M-32k-retrieval", "togethercomputer/Refuel-Llm-V2", "Qwen/Qwen3-235B-A22B-Instruct-2507-tput", "Qwen/Qwen3-235B-A22B-Thinking-2507", "Qwen/Qwen3-235B-A22B-fp8-tput", "Qwen/Qwen3-Next-80B-A3B-Thinking", "Virtue-AI/VirtueGuard-Text-Lite", "zai-org/GLM-4.5-Air-FP8"];
  const listedModels = models.filter(m => m.type === type).filter(m => !serverlessOnly.includes(m.id)).sort((a, b) => a.organization === "" ? 1 : a.organization.localeCompare(b.organization));
  return <table className="w-full">
      <thead>
        <th>Organization</th>
        <th>Model name</th>
        <th>API model name</th>
        <th>Context length</th>
      </thead>
      <tbody>
        {listedModels.map(model => <tr>
            <td>{model.organization}</td>
            <td>{model.name}</td>
            <td>{model.apiName}</td>
            <td>{model.contextLength > 0 ? model.contextLength : "-"}</td>
          </tr>)}
      </tbody>
    </table>;
};

## Chat models

<ModelTable type="chat" />

## Rerank models

<ModelTable type="rerank" />


# DeepSeek V3.1 QuickStart
Source: https://docs.together.ai/docs/deepseek-3-1-quickstart

How to get started with DeepSeek V3.1

DeepSeek V3.1 is the latest, state-of-the-art hybrid-inference AI model from DeepSeek, blending "Think" and "Non-Think" modes within a single architecture. It's the newer version of the DeepSeek V3 model with efficient hybrid reasoning.

## How to use DeepSeek V3.1

Get started with this model in 10 lines of code! The model ID is `deepseek-ai/DeepSeek-V3.1` and the pricing is \$0.60 for input tokens and \$1.70 for output tokens.

<CodeGroup>
  ```python Python theme={null}
  from together import Together

  client = Together()
  resp = client.chat.completions.create(
  model="deepseek-ai/DeepSeek-V3.1",
  messages=[{"role":"user","content":"What are some fun things to do in New York?"}],
  stream=True,
  )
  for tok in resp:
  print(tok.choices[0].delta.content, end="", flush=True)

  ```

  ```typescript TypeScript theme={null}
  import Together from 'together-ai';
  const together = new Together();

  const stream = await together.chat.completions.create({
    model: 'deepseek-ai/DeepSeek-V3.1',
    messages: [{ role: 'user', content: 'What are some fun things to do in New York?' }],
    stream: true,
  });

  for await (const chunk of stream) {
    process.stdout.write(chunk.choices[0]?.delta?.content || '');
  }
  ```
</CodeGroup>

<Warning>
  **Current Limitations**. The following features are not yet supported, but
  will be added soon: Function calling and JSON mode.
</Warning>

## Hybrid Thinking

Here's how to enable thinking in DeepSeek V3.1.

<CodeGroup>
  ```python Python theme={null}
  from together import Together
  client = Together()

  stream = client.chat.completions.create(
  model="deepseek-ai/DeepSeek-V3.1",
  messages=[
  {"role": "user", "content": "What are some fun things to do in New York?"}
  ],
  reasoning={"enabled": True},
  stream=True,
  )

  for chunk in stream:
  delta = chunk.choices[0].delta

    # Show reasoning tokens if present
    if hasattr(delta, "reasoning") and delta.reasoning:
        print(delta.reasoning, end="", flush=True)

    # Show content tokens if present
    if hasattr(delta, "content") and delta.content:
        print(delta.content, end="", flush=True)

  ```

  ```typescript TypeScript theme={null}
  import Together from 'together-ai';

  import type { ChatCompletionChunk } from "together-ai/resources/chat/completions";

  const together = new Together();

  async function main() {
    const stream = await together.chat.completions.stream({
      model: "deepseek-ai/DeepSeek-V3.1",
      messages: [
        { role: "user", content: "What are some fun things to do in New York?" },
      ],
      reasoning: {
        enabled: true,
      },
    } as any);

    for await (const chunk of stream) {
      const delta = chunk.choices[0]
            ?.delta as ChatCompletionChunk.Choice.Delta & { reasoning?: string };

      // Show reasoning tokens if present
      if (delta?.reasoning) process.stdout.write(delta.reasoning);

      // Show content tokens if present
      if (delta?.content) process.stdout.write(delta.content);
    }
  }

  main();

  ```
</CodeGroup>

<Warning>
  For TypeScript users, you need to cast the parameters as `any` because `reasoning.enabled: true` is not yet recognized by the SDK. Additionally, the delta object requires a custom type to include the `reasoning` property.
</Warning>

## How is it different from DeepSeek V3?

DeepSeek V3.1 – the newer better version of DeepSeek V3 – has a few key differences:

* Hybrid model w/ two main modes: Non-thinking and Thinking mode
* Function calling only works in non-thinking mode
* Agent capabilities: Built-in support for code agents and search agents
* More efficient reasoning than DeepSeek-R1
* Continued long-context pre-training


# DeepSeek FAQs
Source: https://docs.together.ai/docs/deepseek-faqs



### How can I access DeepSeek R1 and V3?

Together AI hosts DeepSeek R1 and V3 models on Serverless. Find them in our playground: [DeepSeek R1](https://api.together.xyz/models/deepseek-ai/DeepSeek-R1) / [DeepSeek V3](https://api.together.xyz/models/deepseek-ai/DeepSeek-V3).

### Why is R1 more expensive than V3 if they share the same architecture and are the same size?

R1 produces more tokens in the form of long reasoning chains, which significantly increase memory and compute requirements per query. Each user request locks more of the GPU for a longer period, limiting the number of simultaneous requests the hardware can handle and leading to higher per-query costs compared to V3.

### Have you changed the DeepSeek model in any way? Is it quantized, distilled or modified?

* No quantization – Full-precision versions are hosted.
* No distillation — we do offer distilled models but as separate endpoints (e.g. `deepseek-ai/DeepSeek-R1-Distill-Llama-70B`)
* No modifications — no forced system prompt or censorship.

### Do you send data to China or DeepSeek?

No. We host DeepSeek models on secure, private (North America-based) data centers. DeepSeek does not have access to user's requests or API calls. We provide full opt-out privacy controls for our users. Learn more about our privacy policy [here](https://www.together.ai/privacy).

### Can I deploy DeepSeek in Dedicated Endpoints? What speed and costs can I expect?

We recently launched [Together Reasoning Clusters](https://www.together.ai/blog/deploy-deepseek-r1-at-scale-fast-secure-serverless-apis-and-large-scale-together-reasoning-clusters), which allows users to get dedicated, high-performance compute built for large-scale, low-latency inference.

Together Reasoning Clusters include:

✅ Speeds up to 110 tokens/sec with no rate limits or resource sharing\
✅ Custom optimizations fine-tuned for your traffic profile\
✅ Predictable pricing for cost-effective scaling\
✅ Enterprise SLAs with 99.9% uptime\
✅ Secure deployments with full control over your data

Looking to deploy DeepSeek-R1 in production? [Contact us](https://www.together.ai/deploy-deepseek-r1-production?utm_source=website\&utm_medium=blog-post\&utm_campaign=deepseek-r1-reasoning-clusters)!

### What are the rate limits for DeepSeek R1?

Due to high demand, DeepSeek R1 has model specific rate limits that are based on load. For Free and Tier 1 users the rate limits can range from 0.3 RPM to 4 RPM at this time. Billing tiers 2-5 have a rate limit ranging from 240 RPM to 480 RPM. [Contact sales](https://www.together.ai/deploy-deepseek-r1-production?utm_source=website\&utm_medium=blog-post\&utm_campaign=deepseek-r1-reasoning-clusters) if you need higher limits for BT 5/Enterprise/Scale.

### How do I enable thinking mode for DeepSeek V3.1?

DeepSeek V3.1 is a "Hybrid" model. To enable reasoning response generations, you need to pass `reasoning={"enabled": True}` in your request.

Example:

```python  theme={null}
from together import Together

client = Together()

stream = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-V3.1",
    messages=[
        {"role": "user", "content": "What is the most expensive sandwich?"}
    ],
    reasoning={"enabled": True},
    stream=True,
)

for chunk in stream:
    delta = chunk.choices[0].delta

    # Show reasoning tokens if present
    if hasattr(delta, "reasoning") and delta.reasoning:
        print(delta.reasoning, end="", flush=True)

    # Show content tokens if present
    if hasattr(delta, "content") and delta.content:
        print(delta.content, end="", flush=True)
```

Note: For this model, function calling only works in non-reasoning mode (`reasoning={"enabled": False}`).

***


# DeepSeek R1 Quickstart
Source: https://docs.together.ai/docs/deepseek-r1

How to get the most out of reasoning models like DeepSeek-R1.

Reasoning models like DeepSeek-R1 have been trained to think step-by-step before responding with an answer. As a result they excel at complex reasoning tasks such as coding, mathematics, planning, puzzles, and agent workflows.

Given a question in the form of an input prompt DeepSeek-R1 outputs both its chain of thought/reasoning process in the form of thinking tokens between `<think>` tags and the answer.

Because these models use more computation/tokens to perform better reasoning they produce longer outputs and can be slower and more expensive than their non-reasoning counterparts.

<Frame>
  <img src="https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/9f4e73cc93d4bc5477375c97d1ff0e4c0ddefaf1466a05223336f2e098784847-image.png?fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=f6f0a54c08e17e7d3015f4b2840f3cde" data-og-width="2946" width="2946" data-og-height="846" height="846" data-path="images/9f4e73cc93d4bc5477375c97d1ff0e4c0ddefaf1466a05223336f2e098784847-image.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/9f4e73cc93d4bc5477375c97d1ff0e4c0ddefaf1466a05223336f2e098784847-image.png?w=280&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=a2a20a5084ecf855f6f32d15295f7805 280w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/9f4e73cc93d4bc5477375c97d1ff0e4c0ddefaf1466a05223336f2e098784847-image.png?w=560&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=79fffaa220583da7c6e63b59dfd13843 560w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/9f4e73cc93d4bc5477375c97d1ff0e4c0ddefaf1466a05223336f2e098784847-image.png?w=840&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=99521c4258f5bc9c2cff61095b1a6f71 840w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/9f4e73cc93d4bc5477375c97d1ff0e4c0ddefaf1466a05223336f2e098784847-image.png?w=1100&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=06feffe542ddcaa3aa39ee699e5f35a4 1100w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/9f4e73cc93d4bc5477375c97d1ff0e4c0ddefaf1466a05223336f2e098784847-image.png?w=1650&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=4f3da12e9eb0145ffe794abf093a0d6b 1650w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/9f4e73cc93d4bc5477375c97d1ff0e4c0ddefaf1466a05223336f2e098784847-image.png?w=2500&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=e9e70a0268295c5bb127bbe2e852d1d8 2500w" />
</Frame>

## How to use DeepSeek-R1 API

Since these models produce longer responses we'll stream in tokens instead of waiting for the whole response to complete.

<CodeGroup>
  ```python Python theme={null}
  from together import Together

  client = Together()  # pass in API key to api_key or set a env variable

  stream = client.chat.completions.create(
      model="deepseek-ai/DeepSeek-R1",
      messages=[
          {
              "role": "user",
              "content": "Which number is bigger 9.9 or 9.11?",
          }
      ],
      stream=True,
  )

  for chunk in stream:
      print(chunk.choices[0].delta.content or "", end="", flush=True)
  ```

  ```ts TypeScript theme={null}
  import Together from "together-ai";
  const together = new Together();

  const stream = await together.chat.completions.create({
    model: "deepseek-ai/DeepSeek-R1",
    messages: [{ role: "user", content: "Which number is bigger 9.9 or 9.11?" }],
    stream: true,
  });

  for await (const chunk of stream) {
    // use process.stdout.write instead of console.log to avoid newlines
    process.stdout.write(chunk.choices[0]?.delta?.content || "");
  }
  ```

  ```curl cURL theme={null}
  curl -X POST "https://api.together.xyz/v1/chat/completions" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -H "Content-Type: application/json" \
       -d '{
       	"model": "deepseek-ai/DeepSeek-R1",
       	"messages": [
            {"role": "user", "content": "Which number is bigger 9.9 or 9.11?"}
       	]
       }'
  ```
</CodeGroup>

This will produce an output that contains both the Chain-of-thought tokens and the answer:

```plain  theme={null}
<think>
Okay, the user is asking which number is bigger between 9.9 and 9.11.

Let me think about how to approach this.
...
</think>

**Answer:** 9.9 is bigger.
```

## Working with DeepSeek-R1

Reasoning models like DeepSeek-R1 should be used differently than standard non-reasoning models to get optimal results.

Here are some usage guides:

* **Temperature**: Use 0.5–0.7 (recommended 0.6) to balance creativity and coherence, avoiding repetitive or nonsensical outputs.
* **System Prompts**: Omit system prompts entirely. Provide all instructions directly in the user query.

Think of DeepSeek-R1 as a senior problem-solver – provide high-level objectives (e.g., "Analyze this data and identify trends") and let it determine the methodology.

* Strengths: Excels at open-ended reasoning, multi-step logic, and inferring unstated requirements.
* Over-prompting (e.g., micromanaging steps) can limit its ability to leverage advanced reasoning.
  Under-prompting (e.g., vague goals like "Help with math") may reduce specificity – balance clarity with flexibility.

For a more detailed guide on DeepSeek-R1 usage please see [Prompting DeepSeek-R1](/docs/prompting-deepseek-r1) .

## DeepSeek-R1 Use-cases

* **Benchmarking other LLMs**: Evaluates LLM responses with contextual understanding, particularly useful in fields requiring critical validation like law, finance and healthcare.
* **Code Review**: Performs comprehensive code analysis and suggests improvements across large codebases
* **Strategic Planning**: Creates detailed plans and selects appropriate AI models based on specific task requirements
* **Document Analysis**: Processes unstructured documents and identifies patterns and connections across multiple sources
* **Information Extraction**: Efficiently extracts relevant data from large volumes of unstructured information, ideal for RAG systems
* **Ambiguity Resolution**: Interprets unclear instructions effectively and seeks clarification when needed rather than making assumptions

## Managing Context and Costs

When working with reasoning models, it's crucial to maintain adequate space in the context window to accommodate the model's reasoning process. The number of reasoning tokens generated can vary based on the complexity of the task - simpler problems may only require a few hundred tokens, while more complex challenges could generate tens of thousands of reasoning tokens.

Cost/Latency management is an important consideration when using these models. To maintain control over resource usage, you can implement limits on the total token generation using the `max_tokens` parameter.

While limiting tokens can reduce costs/latency, it may also impact the model's ability to fully reason through complex problems. Therefore, it's recommended to adjust these parameters based on your specific use case and requirements, finding the optimal balance between thorough reasoning and resource utilization.

## General Limitations

Currently, the capabilities of DeepSeek-R1 fall short of DeepSeek-V3 in general purpose tasks such as:

* Function calling
* Multi-turn conversation
* Complex role-playing
* JSON output.

This is due to the fact that long CoT reinforcement learning training was not optimized for these general purpose tasks and thus for these tasks you should use other models.



---

**Navigation:** [← Previous](./01-create-gpu-cluster.md) | [Index](./index.md) | [Next →](./03-deploying-a-fine-tuned-model.md)
