---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Dedicated Models

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

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
