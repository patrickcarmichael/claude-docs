---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Run the pipeline to transform the text

nodes = pipeline.run(nodes=nodes)
```
```txt title="Output"
/usr/local/lib/python3.10/dist-packages/huggingface_hub/utils/_token.py:88: UserWarning:
The secret `HF_TOKEN` does not exist in your Colab secrets.
To authenticate with the Hugging Face Hub, create a token in your settings tab (https://huggingface.co/settings/tokens), set it as secret in your Google Colab and restart your session.
You will be able to reuse this secret in all of your notebooks.
Please note that authentication is recommended but still optional to access public models or datasets.
    warnings.warn(


tokenizer_config.json:   0%|          | 0.00/7.92k [00:00<?, ?B/s]


tokenization_cohere_fast.py:   0%|          | 0.00/43.7k [00:00<?, ?B/s]


configuration_cohere.py:   0%|          | 0.00/7.37k [00:00<?, ?B/s]


A new version of the following files was downloaded from https://huggingface.co/CohereForAI/c4ai-command-r-v01:
- configuration_cohere.py
. Make sure to double-check they do not contain any added malicious code. To avoid downloading new versions of the code file, you can pin a revision.
A new version of the following files was downloaded from https://huggingface.co/CohereForAI/c4ai-command-r-v01:
- tokenization_cohere_fast.py
- configuration_cohere.py
. Make sure to double-check they do not contain any added malicious code. To avoid downloading new versions of the code file, you can pin a revision.


tokenizer.json:   0%|          | 0.00/12.8M [00:00<?, ?B/s]


special_tokens_map.json:   0%|          | 0.00/429 [00:00<?, ?B/s]


Special tokens have been added in the vocabulary, make sure the associated word embeddings are fine-tuned or trained.
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
