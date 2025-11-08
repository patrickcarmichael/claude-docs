---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Data formats

Together Fine-tuning API accepts three text dataset formats for the training dataset. Your data file must be in the `.jsonl` format with fields that indicate the dataset format. You can have other fields, but they will be ignored during training. To speed up the data uploading and processing steps and to maximize the number of examples per file, we recommend to remove the unused fields.

Also, if the data has two or more possible formats (e.g., it contains both `text` and `messages`), the Together client will show an error at the file check stage before the upload.

### Conversational Data

For conversational fine-tuning, your data file must contain a `messages` field on each line, with `role` and `content` specified for each message. Each sample should start with either a `system` or `user` message, followed by alternating `user` and `assistant` messages. The Together client will reject any dataset that does not follow this pattern.

Optionally, you can add a `weight` field to any message to control its contribution to the training loss. Messages with `weight=0` will be masked during training (their tokens won't contribute to the loss), while messages with `weight=1` (default) will be included. Only values 0 and 1 are supported for the `weight` field.
```Text
{
  "messages": [
    {"role": "system", "content": "This is a system prompt."},
    {"role": "user", "content": "Hello, how are you?"},
    {"role": "assistant", "content": "I'm doing well, thank you! How can I help you?"},
    {"role": "user", "content": "Can you explain machine learning?", "weight": 0},
    {"role": "assistant", "content": "Machine learning is...", "weight": 1}
  ]
}
```

The resulting conversation dataset will be automatically formatted into the model's [chat template](https://huggingface.co/docs/transformers/main/en/chat_templating) if it is defined for that model, or into the default template otherwise. As a general rule, all instruction-finetuned models have their own chat templates, and base models do not have them.

By default, models will be trained to predict only `assistant` messages. Use `--train-on-inputs true` to include other messages in training. See the [API Reference](/reference/post-fine-tunes) for details.

Note that if any message in the conversation has a `weight` field, the `train-on-inputs` setting will be automatically set to `true` to respect provided weights.

Example datasets:

* [allenai/WildChat](https://huggingface.co/datasets/allenai/WildChat)
* [davanstrien/cosmochat](https://huggingface.co/datasets/davanstrien/cosmochat)

### Instruction Data

For instruction-based fine-tuning, your data file must contain `prompt` and `completion` fields:
```Text
{"prompt": "...", "completion": "..."}
{"prompt": "...", "completion": "..."}
```

By default, models will not be trained to predict the text from the prompt. Use `--train-on-inputs true` to include prompts in training. See the [API Reference](/reference/post-fine-tunes) for details.

Here are some examples with this format that you can download from the Hugging Face Hub:

* [meta-math/MetaMathQA](https://huggingface.co/datasets/meta-math/MetaMathQA)
* [glaiveai/glaive-code-assistant](https://huggingface.co/datasets/glaiveai/glaive-code-assistant)

### Generic Text Data

If you have no need for instruction or conversational training, you can put the data in the `text` field.
```Text
{"text": "..."}
{"text": "..."}
```

Here are some examples of datasets that you can download from the Hugging Face Hub:

* [unified\_jokes\_explanations.jsonl](https://huggingface.co/datasets/laion/OIG/resolve/main/unified_joke_explanations.jsonl)
* [togethercomputer/RedPajama-Data-1T-Sample](https://huggingface.co/datasets/togethercomputer/RedPajama-Data-1T-Sample)

### Preference Data

This data format is used for the Preference Fine-Tuning.

Each example in your dataset should contain:

* A context "input" which consists of messages in the [conversational format](/docs/fine-tuning-data-preparation#conversational-data).
* A preferred output (an ideal assistant response).
* A non-preferred output (a suboptimal assistant response).

Each preferred and non-preferred output must contain just a single message from assistant.

The data should be formatted in **JSONL** format, with each line representing an example in the following structure:
```text
{
  "input": {
    "messages": [
      {
        "role": "assistant",
        "content": "Hi! I'm powered by Together.ai's open-source models. Ask me anything!"
      },
      {
        "role": "user",
        "content": "What’s open-source AI?"
      }
    ]
  },
  "preferred_output": [
    {
      "role": "assistant",
      "content": "Open-source AI means models are free to use, modify, and share. Together.ai makes it easy to fine-tune and deploy them."
    }
  ],
  "non_preferred_output": [
    {
      "role": "assistant",
      "content": "It means the code is public."
    }
  ]
}
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
